from kivy.app import App
from kivy.uix.browser import WebView # Bazı sürümlerde jnius gerekebilir
from kivy.core.window import Window

class SiberGozApp(App):
    def build(self):
        # Bu kısım Android içinde bir web görünümü açar
        from android.webkit import WebView, WebChromeClient
        from android.view import ViewGroup
        from pythonforandroid.toolchain import Context
        
        activity = Context.get_python_activity()
        view = WebView(activity)
        view.getSettings().setJavaScriptEnabled(True)
        view.getSettings().setDomStorageEnabled(True)
        view.getSettings().setAllowFileAccess(True)
        
        # Senin index.html dosyanı yükler
        view.loadUrl("file:///android_asset/index.html")
        activity.setContentView(view)
        return view

if __name__ == '__main__':
    SiberGozApp().run()

