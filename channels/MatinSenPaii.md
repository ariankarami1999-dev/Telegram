<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn1.telesco.pe/file/uHkvLsn4XVLrnVQOp70YVYpEsfs8tEJnSei1n7oO0g0ZxINTmLU3VisGtYuD2QWtn_yAZF5OXZRC9X5OTk_ImNGecDyqiLE4gIZ-CRSAAa8hOMVYsNQ2yABmMCw1qA3_LloFFq59gBhcx7vMihi1kIRZ9HsplkhVA9n4j59Bf_o2KGBk6RLUOc9u1-tU5txX6uo6XZwrbVRx9a8SIh8uC6feh43xfSx9n3Mz4uGIEZnAfVcFJthKpbGr9ual-nOUHbe12tu8VYbP79G0KkL6QVN5C5GCjCI7GZza1Q3JdusId3Vp7SDqbdlEstAWIXZUR9Hg_d8IL_PAWS_3x7NGfw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 157K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 12:47:33</div>
<hr>

<div class="tg-post" id="msg-4823">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=k3srkto4mmCLfiu9WNg-ILXHiIw630URbpLyEgjUYUbku_MP8dSAF-pVMho6EcmXs9TDCRGIrho8Vua0bYKLFwOzAv9T-c3ZVBCCj7YTrKfA03TT0ebE7VBwV0yYZAgNr2SoD9lQ9onlsiRgKyYhUryD3RQyhJ5JCqXRolfZIPMkNx78w0t4GiOLKOog5dhL7iYMO56hdDlP67nAjDqZ7Ct5a6GQaA-Kal53upYvgoyz3wa-nz5fEsvPYRhtnu_N93gq5198QRiyrBrAX3PJx5ief2-L-0FgrtQdLEgO8Ee9VPRNcoCkR8wHqsmZ-SNLM7iMNNp6zRVVndblQ7hgNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=k3srkto4mmCLfiu9WNg-ILXHiIw630URbpLyEgjUYUbku_MP8dSAF-pVMho6EcmXs9TDCRGIrho8Vua0bYKLFwOzAv9T-c3ZVBCCj7YTrKfA03TT0ebE7VBwV0yYZAgNr2SoD9lQ9onlsiRgKyYhUryD3RQyhJ5JCqXRolfZIPMkNx78w0t4GiOLKOog5dhL7iYMO56hdDlP67nAjDqZ7Ct5a6GQaA-Kal53upYvgoyz3wa-nz5fEsvPYRhtnu_N93gq5198QRiyrBrAX3PJx5ief2-L-0FgrtQdLEgO8Ee9VPRNcoCkR8wHqsmZ-SNLM7iMNNp6zRVVndblQ7hgNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍷
درود به همه رفقا...
آموزش
سا
خت کانفیگ Amnezia VPN(وارپ)
• صبرکنید ای پی ها رو لود کنه
• بعد یکی انتخاب کنید
• تیک فعال سازی پارامترهای امنزیا 1.5 حتما بزنید
• بزنید روی ساخت کانفیگ Amneziawg
• دانلود کنید وارد کنید داخل Amnezia VPN
• میتونیدم کانفیگو کپی کنید + بزنید بعد insert بزنید کانفیگ اضافه بشه
💡
نکته:روی تمام اپراتور ها متصله هست.
لینک ابزار(ساخت کانفیگ):
👇
https://darknessshade.github.io/Amnezia-VPN-Config/
دانلود اپلیکیشن ios
دانلود اپلیکیشن اندروید
@xsfilterrnet
👑
@ConfigWireguard
✅</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/MatinSenPaii/4823" target="_blank">📅 08:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4822">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K422wDvVgPRfWf5GiW4FKY2KYN8mdR2oNHDSEn6mmjYqIAb5GPt_mNlUmsReZS493QigzvJYCtxkfMrou1fMblmgtbxrleCLil8uZqiTgofQ7cLlw0dMns1h_u3YNvddQBUQ9uUXeRb21HGrH4s4eB3xDSCwY9dY9q1RwvqAi47bgrN3hq2InEsauCDOonW_cqtbO0WPb0ZbX3vGUsExd7t0a7Ecm4tgohKTi7BlKp8wbKzP0NcdVnTzW1OoaHGa--15hNEKl6AEfDuYWI_s2BXzOv2TRQ6mMTpDd2pzekCIUVxkrknWHyP9nI_6u0ltS40PzaiVC4LysjXPNkWSeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)  بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.  مهم‌ترین تغییرات:
🖥
یک GUI کامل…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/MatinSenPaii/4822" target="_blank">📅 03:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4821">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CrzecgBWv4o_a5mBehiKXj9eXnuLolYCURBgqcxKNrBCSj25H5lAhO7YI04CY2bFiTbswmMzeZL6zp8Mj-BDybblpBS54-U09m1PUT3mQbRgsCxHVyiMfLUjUHqDQ1_MiuiUQ5Q4CDSeWfJiB0-9FHkFNI7TgpRWzQUI8O6pSyDlFdB-TkY-d2KbLBqkt7as9Nt_arYjocM06XMYeLOX2vQlB6x4cqRGIxxEDxHyu5-qeFxVfzsFXZGKhAhm5bS2AFy98s-rz1sVXJO2d4ytrcH-iCEqz0s4HjaWSZQFif_r4rXVrRaOSGtm2ZivMk7oGwVMNdBl2wfh49H9tNA8cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)
بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.
مهم‌ترین تغییرات:
🖥
یک GUI کامل دسکتاپ برای Windows، Linux و macOS
📱
اندروید از نو بازطراحی شده؛ Kotlin + Jetpack Compose + Material 3، پشتیبانی از اندروید 7 به بالا، APK جدا برای ARM64/ARM32/Universal
⚡️
دیگه لازم نیست منتظر پایان اسکن بمونید — هر وقت IP سبز کافی پیدا شد، متوقفش کنید و فقط از همون‌ها تست سرعت بگیرید!
📋
امکان کپی نتایج (همه IPهای سبز، ۲۰ تای برتر یا یک endpoint خاص) حتی وقتی اسکن هنوز در حال اجراست
🔎
اسکن همسایه (Neighbor Scan) دیگه اختیاریه و به‌صورت پیش‌فرض خاموشه
🌐
تشخیص ISP و ASN چندمرحله‌ای با چند منبع (Cloudflare، IPWhois، IPinfo، Team Cymru + دیتابیس داخلی رنج‌های ایران)
🛡
اعتبارسنجی واقعی کانفیگ‌ها با هسته Xray؛ پشتیبانی از VLESS، Trojan و VMess
📦
خروجی مستقیم به IP:Port خام، Share URL، Base64 Subscription، Sing-box JSON و Clash YAML
🧠
موتور اسکن بهتر: الگوریتم weighted-random برای رنج‌های Cloudflare، جلوگیری از IP تکراری، پشتیبانی چندپورتی، خواندن ورودی از IP/CSV/CIDR
جزئیات کامل و دانلود:
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v1.0.0</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/MatinSenPaii/4821" target="_blank">📅 02:55 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4820">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hallelujah</div>
  <div class="tg-doc-extra">Leonard Cohen</div>
</div>
<a href="https://t.me/MatinSenPaii/4820" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">00:21</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/MatinSenPaii/4820" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4819">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دارم با پدی نسخه‌ی جدید WhiteVPN رو تست می‌کنم که چند ساعت دیگه میرسونه دستتون اول از همه، روی همراه اول با سرعت فوق‌العاده کانکت میشه(زیر ۵ ثانیه) و بعد از اون هم آیپی/سرور شما رو یادش می‌مونه و درجا کانکت میشه. همینطور قابلیت ip fronting هم داره و سرعتش…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/4819" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4818">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">⛏
۲ نکته برای بهبود سرعت WhiteVPN
۱. بعد از اتصال روی دکم
ه اتصال مجدد
کلیک کنید تا به سرور جدید وصل بشید.
۲. همچنین میتونید به صورت دستی تمام سرور هارو پینگ بگیرید و به بهترین سور به انتخاب خودتون وصل بشید.
آموزش تصویری</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/MatinSenPaii/4818" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4813">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN1.2.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.6 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4813" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/MatinSenPaii/4813" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4812">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxLPPdgcQ2vQKIhOvJuBOK-fw_du4ZEXH-LYj1ZQAFuX-Y-De1wNTo71dV_LS__C_3uVikotCdxDGHnt36iCYBEznMClD9uMCeyV7Q_62fakPKupVYE_g8tWBiQG-Gqc3Kcryz8OcHizMHwFaqnzr5nSgZdEKUMg3ZV7BI_lfOxbyoV814vlL_elyzmF_PQmxxIXInDA4Vn4rr188_lPL40Ie5nte-wlmi_-RfYUJsvtClnPDT60xeXUmU8nsSdz5d6eJQ1aGqbwAdmrQ3KwUaTwaUa_zu4ZIt4GNJra8aBXr0u75UT6ekDbPm2K2SfHyQHRg2gia3shq6_ArTWIzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت WhiteVPN 1.2.0
✍️
تمرکز این نسخه فقط روی اتصال
سریع‌تر و پایدارتر بوده است.
امکانات و بهبودهای جدید:
•  شروع اتصال سریع‌تر
•  انتخاب هوشمند بهترین سرور
•  جابه‌جایی خودکار در صورت اختلال سرور
•  کاهش خطا و نیاز به چندبار زدن دکمه اتصال
•  بهبود Real Delay Test
•  رفع مشکل متوقف‌شدن اتصال در مرحله شروع
هیچ تنظیم خاصی لازم نیست؛ فقط برنامه را به‌روزرسانی کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/MatinSenPaii/4812" target="_blank">📅 11:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4811">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ihQby5hrS-BGHyLGzjRtDsY_KvjtbECdQIWS7BdrEq3lGbIquzPGVTkB3mfJZbCTk3nu1fE1ABp8-GgaWO-b_Q-3yvrvSak3gKzYqr-M9c5NfzZ3xuz5fFN6TT9zzuS9mtzwhfuzO_NmU5XHHBJkwXRr5ixGCjAJLtu3fibO8Gf5CYyP66jZ4EXuOk1L94mAlCzHCEOyU_Ob83tzBQMmIJBSZtYD9O7tHvRkdXrdwdP-KHqNK3yNciLc30jQY0G-oX3-oJ6FZPldDPUde8fvdglMsQv7jsfeZxkZApzcIS-ck3_EYFpeeFcre3R_Sp-7sK93eXzfBJinn3e_s1jHEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه پرومو رایگانش تموم شد:)</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/MatinSenPaii/4811" target="_blank">📅 10:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4810">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V1DungaoXtJKkPBdirnavxIuVf506CzO6cCqX2B5GWMo8ooYFBZ9YaOx3VrJnW_e3MQeaZ2tB3ZEjnzhZQtGjGqLaiaOb7wzo9yxRAOn64bnVdUOp7z1b5efKWDHzuLH0KprlaxW0t_HeqvYC3mtE6cvV0MhkdjEol7KOhNhj-3oS7XjeE5UWEE5qMJYD-f7W9J4Zd6wLE6LVq_AtffPUNJHNdU4wl2i0EOl32LDVBkkIsuIJiXWiYDa87XPwxNJUuBM8yl8JXtQVi5sZYJ0uVfnqkWNwrus7q8XIh1fLwBIfTx6-1KK01jPUUwtajccelkh7fgpnVJIURSpZLqorw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان بیشتر مدل‌های دنیا وارد «منطقه کشتار DeepSeek» شدن.
یعنی مدل‌هایی که توانایی‌شون کمتره و قیمت‌شون بالاست، دیگه رقابت سختی دارن و ممکنه کم‌کم کنار برن.
✍️
Ali</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/4810" target="_blank">📅 09:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4809">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دوستان توی infron.ai میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.  ممنون از confesious عزیز بابت معرفی. فعلا دارم باهاش کار میکنم ببینم چه شکلیه  تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/4809" target="_blank">📅 06:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4808">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سرعت آپلودش هم عالیه.
قابلیت‌هایی توش پیاده‌سازی شده که از همیشه استیبل‌تر بشه</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/4808" target="_blank">📅 06:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4806">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u0L2lNIZiiv0gm4R9KCPvnp-mIlaP3RGT2SjRA1mctbqAFWbXEBrLIMJ1SLJtdTsiiwOGTgh11OCzmucbJTCQg6XnqMx1cYp9NlOq823FD_JXSDmXiZSiPXbnxd4tbUTK7UDBdTKxOCXREDZvI_U0FGWlXfSXEayx-MdiO_Y38QKwQOylEsGEe-YbqApBhvOYO-uB-1bktPTBTSPz8DPGU67f7Cns7QjTiDKq2O3KwvmRFP24tKCzfWsSyaQGIDmVyPtr57QHzrgBkkehsdvscyFdm32azXqUxQq2G8LgOBlbo_sYC-SxYwNE0zC8UBa0TDV01SwdeZq5GIm3JQWGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AMvzf1rYjhB2MYWO9cdOZe9yLeRLxFFDtmVW094TkTnsHMn6yGKJCC8uIv6yL5S9tn_MUBMzFNhFc3hVzu3wVdBOImLmbPr84ABgT2C5TeJ702YZhmqeClT1e0qWj32AjM-zgh1a52sTsZPxtU2LI2OZGBgJB3pRLkSRg-dO5Hef7zsczeNt2TXRCLk2XTVNZGQejQcP5-26tWLRJNBu_nOA0CLgxzvhSJQ4debu5XdUtONaVMXdMFBg9nwW9icLo0sWNH6nmbcms7MJQGGafCxd3COtYlopoW5h5Q1qYCgaaEXSUHzDuWHQxMt7cdzm_mRwP2l-1UHFDezJAETbAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دارم با پدی نسخه‌ی جدید WhiteVPN رو تست می‌کنم که چند ساعت دیگه میرسونه دستتون
اول از همه، روی همراه اول با سرعت فوق‌العاده کانکت میشه(زیر ۵ ثانیه) و بعد از اون هم آیپی/سرور شما رو یادش می‌مونه و درجا کانکت میشه.
همینطور قابلیت ip fronting هم داره
و سرعتش عالیه(حداکثر سرعتی که اینترنتم میده)
دم بچه‌های WhiteDNS گرم واقعا
❤️
🔥</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4806" target="_blank">📅 06:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4805">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دقیقا این اتفاق برای منم افتاده بود و سه ساعت داشتم میگشتم ببینم کجا پروکسی روشنه که بدون وی‌پی‌ان داره آلمان نشون میده
🫩
🫩
روانیمون کردن</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/4805" target="_blank">📅 05:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4804">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3DHouse-Qwen-3.8-preview.html</div>
  <div class="tg-doc-extra">44.4 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4804" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایلی که الان با Qwen رایگان ساختم</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/4804" target="_blank">📅 04:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4803">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3DHouse-Kimi-K3.html</div>
  <div class="tg-doc-extra">41.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4803" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایل 4 میلیونی‌ای که توی ویدئو ساختم</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/4803" target="_blank">📅 04:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4802">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پرامپت ویدئو آخریم رو که با KIMI3 رفته بودم، الان دادم بهش و واقعا نزدیک بهش در آورد
🔥
به نظر باید منتظر یه مدل خفن باشیم. فعلا توی Preview هست مدل  تازه Kimi نتونست One Shot کنه، و این One Shot کرد اونم فعلا رایگان! کیمی نزدیک 3-4 میلیون پولمو خورد
😂</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/4802" target="_blank">📅 04:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4800">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fJJp9Nmi0iBhfP-L9bDQj6PIBUzDMVfpBvy067LsH4dNYvzR8uY0rtxToTE-bUWFqwtvfPVZSfACsAgl6CcRiTG44FJi10UtKkNwZhHYEbINyZzUNUWh-uVtj2WnBcP1dQA5lIHdv4ypx0LTNYh9upKiwF-NjI49NRGGLcwklzbNSWLadz6GG2vaGSdYT5DkDQFGxRsIRmFSMR0iWaTCDDVa0BqHcfjf-8HV1nPZq1ZU_QumhA1nc8OjbbkDFzW-Ktvdadb70VMrehjS6TyTBnOxyQr26aOhZFAyvCUURvFtfCLAP8u6cHlZPkfM60CD-ZSDSXE8rIubEZns3ukynQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/E1XvujtDNxtPV8Zk-49JqP09NMpRFOUO94aVRO0yOZBVMrF9IrQlniMPf9rCfB7c6BMZu2CsKqo4D1GQtwiQzWr5KCkvxI2SsViXdU27gqtVD41DhvyY0E-59baPpQOJnzhg1fykiDqf_vYCklrFVmOu7MJ6JVQrJuRWEQrzVy6n05Br7yKA2m3dVX9fIDJpJpoGMAk-Uo1XQfnxmrbMWRtFEPIHgDbJlhpLlyNpU8fDMBHCQfzrm-2ZCYrKaUsC3VCsyEjYYdZv0aK-8EcoaZN8NmDasRSCivTuQvrOPX5XfQiZu5EyiLa01N7e8WhdWwzvQZqN5TpKQoBhpmsdbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دوستان توی infron.ai میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.  ممنون از confesious عزیز بابت معرفی. فعلا دارم باهاش کار میکنم ببینم چه شکلیه  تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/4800" target="_blank">📅 04:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4799">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MOgzx3NXsw20mPOujBDL8ketrrkpx6KU2kjpAiqLLHNbGiONhjfZlDfpDII85UIEwqy_UGUoYo6AkyHnZeZE9kC045lbSUzDrRIxRbMfUpgH9cyXbYcK02BpFEgNTlbAYlAW6Zwxx9s-CU-2rHl6bXXcXWUsC7dcBdCoy8PeC0yvTm05eL55xWMJ0zxglNjbKE8pv-cHBoaLI6OPH4vPfPMC0e5c8Wr90TpR93eFbXKS0vKId1_9Ljerf3YpoW2BQK2HuIpnNkBCruNrlag3El0Zo4KxU8UwKUWTMnCDEpZQ42ccJDAu4B5GFdTqAZyeFbutQXESKEjNrrviSwgLeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان توی
infron.ai
میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.
ممنون از confesious عزیز بابت معرفی.
فعلا دارم باهاش کار میکنم ببینم چه شکلیه
تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/4799" target="_blank">📅 03:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4798">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">برای منم روی فیبر مخابرات فرقی نداشت تا اینکه یه پینگ از همراه اول گرفتم دیدم همه چی رسما قطعه
🫤</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/4798" target="_blank">📅 02:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4797">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">برای منم روی فیبر مخابرات فرقی نداشت
تا اینکه یه پینگ از همراه اول گرفتم دیدم همه چی رسما قطعه
🫤</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/4797" target="_blank">📅 01:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4796">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-poll">
<h4>📊 از گوشه کنار زیاد میشنوم اینترنت دچار اختلال شده. مال شما چطوره؟</h4>
<ul>
<li>✓ به زور به تلگرام وصلم⚠️</li>
<li>✓ اینترنتم کند تر شده🔴</li>
<li>✓ فرقی نکرده✅</li>
<li>✓ ایران نیستم👌دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/4796" target="_blank">📅 01:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4795">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">خدا رو شکر توی قطعی نت دستاوردهای بزرگی داشتیم و اپراتورها از وی‌پی‌ان فروش‌ها ضریب دادن رو یاد گرفتن
😑</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/4795" target="_blank">📅 00:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4794">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KLoWgm4rxS5F6eczwrleSj-CUza05b70BOiSjTa0ofYNnAwl1yzuDkmRmAovpKdaP-mf8IGISgp6gJyUq2BIS3uUqOr4xTv2Wf_BUgurYVgnX0FtCJD2ghgFjql_Aa_N8FxxnAZhYNaVMYHScVTph0f47xiSzKnZD6wvTJWqb3fJhyx7U-CJ5QiPnY7eR8OGeA2_S9STVr-RSX5_b-8eLMEPlHuhXLqyYFXzFeaBKbcD2iocERZFl7CijwPGQmzLKAIhALf4tIQ7ZHBUFosH6QmLpz4Uf96OMQTIX4DnBMfuj4JC_R30fBzEg9RarMtVlWqkybrxYxyxUVfh820G_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت کنجکاوی در مورد موضوع ضریب جدید روی اینترنت بین‌الملل، ۱ گیگ دانلود کردم و توی پنل دیدم ۲ گیگ محاسبه شده!
©
Farshad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/4794" target="_blank">📅 00:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4793">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">+000000000
😔
شرکت PCCW Global</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/4793" target="_blank">📅 00:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4792">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPqRNrrJ_PcvBzvIKujJLo4A4o_C2WUQ1fDfXRvyHvs6z1eNb0x7qmYnBqo-Sp6aVM2EkDtsDwXnjsda_A-DBmJjn4t0WXSJY6xSJl0c2DLaBpWZC4mydMYHS-Vi08CNHSrqDomHdou4HXZWrn9MMunDUHum3wj3NpF-Sx2pLqLQFOY6A4mEy6HmqvgwapbagvlH9qNS0f1Vb8djkeoJiwQ2Yoid2vqkxmEFjVZ_0MdMJrmDscbOttjPp4Sqk7S2TogCjjWGJOF6xVwiq5TnhdUHxaJjlrLQZEO3Y0M7MEUT1zqm0K1yBhsMEsZM-b03ZnRHEc3jJQ5nLe2FP4zxLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+000000000
😔
شرکت PCCW Global</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/4792" target="_blank">📅 00:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4791">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">به نظرم یه تماس بگیریم باهاشون</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/4791" target="_blank">📅 00:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4790">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ظاهرا تغییراتی در مسیر های اینترنت بین الملل زیرساخت ایران به وجود آمده ، دیگر به جای اذربایجان و شرکت دلتا تلکام شرکت المانی PCCW Global و ایپی رنج 205.252.xxx.xxx داره نمایش داده میشه ، وضعیت بهتر که نشد هیچ بدتر هم شده ، مثلا پینگ تایم کلودفلر رو 5g ایرانسل…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/4790" target="_blank">📅 00:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4788">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CrbaQnLdxlkggbMWDGQgHHjtz1b-f1QG_bhQzBZKuSbppH8ah10DHqayeqck4xcm4J-UfLJGHzd2skZcCZBDvPy3h54bFPPsHaJtIfbELIEI3WaFhRrJ1UoXtnGWL_K3ZWwN0JipxZTwKpR0GxMIX7CNovCpfsmoiYgKRA9pbcVhTFoLjNKgUBcdqjR1TKRnZNI4zUVwVhJ-SV9iqRYE1XksbZkwFk89oxwFsNBcUZ30oJJldeKaT6ftB3UYVZH591Eqgq7JPzMV06aWNy8WamW6Bjlfkk7jWvLmW-IWLD38H_N84X-UNR0eZstCl-2ggUrq0vNKwotNjNmEWiI9Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sqc5zDpLgwfbRTOXSPzHciXMK-uPmoTF2MjXnbWgpCuMq6IeCzd2Kavqn4Zb0H-zgFPM7D28ZGXpoJ_UhSyg0-4AY_8HserNLdho6vJih2zEHGYYTvvgK3PI18lU1SSoux5HttypctdESKE5dmFWjBv5nmTVdr2G_MEpDNciDXOPkgUWuOVc-5G0Gu_bMfOfZ7MCrluDPhWIBMW7L2-dPSQkAT0oPViTEGg3B3KcAvpjZytL2bauexH2cq__fEgLqE9yTY7ADHs1IbfXCA4b5SI0lr5IV4dkQERQWWzZ77tUyfyFMxOjhTD9bluWg1Qd5JlUXDb4nBIgVeLq1yEEwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ظاهرا تغییراتی در مسیر های اینترنت بین الملل زیرساخت ایران به وجود آمده ، دیگر به جای اذربایجان و شرکت دلتا تلکام شرکت المانی PCCW Global و ایپی رنج
205.252.xxx.xxx
داره نمایش داده میشه ، وضعیت بهتر که نشد هیچ بدتر هم شده ، مثلا پینگ تایم کلودفلر رو 5g ایرانسل قبل محدوده 80 90 بود الان 140 160 ، درنهایت این وضعیت nat کردن اینترنت در ایران داره به یک روال عادی تبدیل میشه که جای تاسف دارد</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/4788" target="_blank">📅 00:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4787">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vV7ha5sb4aeRF-KnuWkqxvgeQ1H0aFmrOlNJLKasd2qzTGVgk8Rhl5oidhGAujlEFQPq0rTui-Q_pBqItLP4FMTkiidNoRr-Bp_z-QzrHPPtFQMKgJ6Bj7uvOqMY1JZn4D4bGliXOa2dYr-TZHA7i_MgZHRWAfq3FRS5ajBs1ZsVXmQhaPEaIL8qr9qk-dbtGHFXtTeOk7VGIeBAgrgX3drMMK8wmrkS_OkMRaG_RE-xME4rcDmLv4nSaSiRtSOO-BHoyELt9zRkUQ5RIXOqXK20cNh8saBOpZQs6oEQ2AP33o4IWZagi1O2PLuTHOuTDOG1b5aSr5-fw4zAW1hhAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فریم‌ورک Science One گوگل
💡
گوگل یه فریم‌ورک تحقیقاتی خودمختار و «قابل‌تأیید» معرفی کرده با Chain-of-Evidence — یعنی مدل فقط نتیجه رو نمی‌گه، بلکه زنجیره‌ی شواهد رو هم ارائه می‌ده تا کارش قابل راستی‌آزمایی باشه. قدم خوبی به سمت تحقیق و توسعه "کم‌خطا‌تر" با AI
🔗
https://research.google/blog/science-one-framework-a-verifiable-autonomous-research-framework-via-chain-of-evidence/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/4787" target="_blank">📅 22:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4785">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Bu_zmAfWkxQ_E3wVxXSVPPYZBZMHZEiaqmNAqXbMWiTeGaa71_PpoVmkdl1ux424NOVLo1MemQtTRsnqnFWHs_zWF5GqvhhQ3sj171wbnzah8eJmvQq6_RQ5MngO9xXUkGh9Vxj1uIVwTJq4jheBMTTgnV1Pp4NsWukqwEoFhRJ_iUOC82w3X7uP7LdjP641yEKKRL0IdYB5MnHjIIOGZ9ALJAIZTM6cO6XHFKI0H7l69y-oytZCXr11QK1x6dURqhONg0hJCImZoPBM_wYXKV9-bPUEwG1zmuQynr0QJn5brbYPTeDx9NlMitGJGmvbW3g1FCfoPb_qQHjnl81V3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Qc4PFcZiofLJO2vekCf06Od4oxcPdFByozoSpnaW9BC9BYLkphk1VQkvqgg8XuDiZzjyx3k-0zJUTUn0Xr0JFkhhunFCMAxqrniLQ-ZHrSKb9pWz9uaOExLQaoVt7NZfnh8tJMyqO8t0bWOPObqL2P420BdacTHmeGDYexxBAGMoG_eIe24VOXOMY8pSxh7R5jVdT2R_AgS_7YGkFDUr_R_R6x1YR4qvy8CDObqxlfysuPceOD3Y-HDjIEjh_idLG_H2mn-S3ANHrWYg36TlhsEim3rmeEjYopfSbGnB_ziEIes7MEQcUaoz5ETbS3PU6hSTA8EG3Hr5xYuyfZZz3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">☠️
استفاده مجانی از Claude و کلاد کد روی سیستم خودتون!
⚡️
دستورات استفاده شده توی ویدئو + پرامپت سه بعدی: https://t.me/MatinSenPaii/4770
⭐️
توی این ویدئو: 1- بهتون میگم که Harness چیه و دوتا پروژه با یه پرامپت یکسان که با مدل یکسان ولی Harnessهای متفاوت…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4785" target="_blank">📅 21:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4784">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4784" target="_blank">📅 18:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4783">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">برق رفت
🥀</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4783" target="_blank">📅 18:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4782">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">این پرامپت‌های ساخت بازی سه بعدی واقعا به درد نخورن(توی سنجش قدرت واقعی مدل) اما از طرفی اعتیاد آورن. هرچی میرسه زیر دستم پرامپت ویدئو آخری رو بهش میدم ببینم چیکار میکنه
😂</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4782" target="_blank">📅 18:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4781">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">☠️
استفاده مجانی از Claude و کلاد کد روی سیستم خودتون!
⚡️
دستورات استفاده شده توی ویدئو + پرامپت سه بعدی: https://t.me/MatinSenPaii/4770
⭐️
توی این ویدئو: 1- بهتون میگم که Harness چیه و دوتا پروژه با یه پرامپت یکسان که با مدل یکسان ولی Harnessهای متفاوت…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4781" target="_blank">📅 18:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4780">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سلام رفقا
ما به رسم هر سال، نزدیک مدارس که می‌شه پول جمع می‌کنیم و واسه بچه‌های سیستان‌وبلوچستانی که بخاطر وضعیت بد مالی نمی‌تونن ادامه تحصیل کنن کیف‌کفش و لوازم مورد نیاز واسه یک‌سال تحصیلی رو می‌خریم و بهشون میدیم.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4780" target="_blank">📅 17:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4779">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">با پنج دلار ویزا کارت خریدم، ایشالا که کلاهبرداری نیست
😂
اگه خرید کردم و اوکی بود بهتون میگم. برای Claude که حقیقتا جرأت نمی‌کنم</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/4779" target="_blank">📅 08:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4778">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یه هارنس چندنفره برای اجرا کردن Agent‌ها. یعنی چند نفر می‌تونن همزمان روی یه تیم از Agent‌ها کار کنن — یه جور VS Code مولتی‌پلیر ولی برای اجرا و مدیریت agent
👍
🔗
https://github.com/yc-software/qm
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/4778" target="_blank">📅 01:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4777">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
پترنیها یه اپلیکیشن مشابه v2rayng زده که به نظرم از خود v2 هم بهتره چرا؟
هسته بروز که توسط خود پترنیها داخل اپ قرار گرفته و بروز بودنش حتی از v2 هم زودتره(بیشتر آپدیت هسته v2rayng از سمت پترنیها بوده)
رابطه کاربری روان تری داره.
مهم ترین نکته اش اینه با قابلیتی که واسه
#فرگمنت
اضافه کرده شما دیگه محدودیت آپلود داخل کانفیگ هاتون ندارید(بیشتر کلودفلره) ولی بعَی سرور شخصی ها هم مشکل آپلود دارن که طبق تنظیمات پترنیها اکی میشه
🔥
دانلود اپ از گیتهاب:
💓
https://github.com/patterniha/v2rayNG/releases
تنظیمات مربوطه به آپلود:
📝
https://t.me/patt_channel_x/94?single
💡
دوستانی که پترنیها رو نمیشناسن:پتنریها خالق sni spoof و شیر و خورشید و همچنین کلی از کارای بزرگتری بوده و داشته از جمله خود v2ryang و...
@xsfilterrnet
👑
@patt_channel_x
✅</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4777" target="_blank">📅 00:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4776">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4776" target="_blank">📅 17:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4775">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">با تینا پارتنرم مشورت کردم و یه سری تصمیمات خیلی عالی گرفتم واسه‌ی کانال و چند ماه آینده
فعلا لو نمیدیم
🎨</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/MatinSenPaii/4775" target="_blank">📅 16:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4774">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">این ویدئوی پرایم واقعا خوب بود مخصوصا راجب این Demo های وان شات https://www.youtube.com/watch?v=LmXU6SEH3Ks  جمله‌ی کلیدیش این بود: The Demo is cool, but not actually a game این یعنی شما نباید با دیدن یه چیزی که یه نفر با ai اومده کدشو زده، یه وقت این توهم…</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/MatinSenPaii/4774" target="_blank">📅 04:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4773">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MbGBhDaUrbgnV6uuPrg5eUFWOPQelWf1ySe3JjmvgK7kxPgJzs5cCX-BIi7BHUBtw_M8hI_e7SugTpu8h48_LiTALDNP0wQ41x-x9gXLMH_NGlTK2TXdSyWR4bbirNEkLsTdzQaMtnD7WT0mbljfHZaP9eiLp6flAThxbrrvmffP970TLrmiYDkIALKUmgB6A25iyHO9ZbSmHfbtSJfZyov7blY15kr4zT1RixA3ge4EBS4HZdBSj8O0OHpeP0Qg3LJ3jUZnpdMdC7sRB733rLfluJO6ZUu8xvAaSkcwzTfPae8OARc-WEYkj4PGENEc4FaZM-kSMtZdL8VJIsUaHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئوی پرایم واقعا خوب بود
مخصوصا راجب این Demo های وان شات
https://www.youtube.com/watch?v=LmXU6SEH3Ks
جمله‌ی کلیدیش این بود:
The Demo is cool, but not actually a game
این یعنی شما نباید با دیدن یه چیزی که یه نفر با ai اومده کدشو زده، یه وقت این توهم رو داشته باشید که می‌تونید همین الان(حتی با یه اشتراک 200 دلاری کلاد)، بازی بسازید بدون هیچ دانشی!
طبیعتا کار رو خیلی سریعتر می‌کنه، اما باید مراقب این باشید که ai، لااقل هنوز به این درجه نرسیده(و به نظر من امکانش هست که هیچوقت به این درجه نرسه که دانش پایه حذف بشه از این چرخه) و خلاصه، یادگیری رو متوقف نکنید. حالا توی هر حوزه‌ای که هستید
نه جزو اون دسته‌ای باشید که میگه ai به درد نمی‌خوره و Anti-AI هستن،
نه جزو اون دسته‌ای باشید که ai تبدیل به بُت‌شون شده و می‌پرستنش!</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/MatinSenPaii/4773" target="_blank">📅 04:09 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4772">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سی‌ان‌ان:
فرماندهی مرکزی ایالات متحده (سنتکام) در حال آماده‌سازی برای یک دوره دو هفته‌ای از بمباران شدید پایگاه‌های موشکی است.</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/4772" target="_blank">📅 03:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4771">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یکی کامنت گذاشته بود، بعد کلی که تایپ کردم راه حلش رو دیدم کامنته غیب شد. رفرش کردم دیدم پاک کرده
😭
خوشحالم که خودت راه حلت رو پیدا کردی مشتی ولی این رسمش نبود</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/MatinSenPaii/4771" target="_blank">📅 03:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4770">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Claude-Free.txt</div>
  <div class="tg-doc-extra">4.6 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4770" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">مربوط به ویدئو بالا</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/MatinSenPaii/4770" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4769">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WdBQGptnrnmGydaSKFHqdrLFAglZokbGLGh2GsnWckPASRtMPFS4FdZ1XWIcg-5H9Qg7yXy-A-UkP69ECZqEldMossnTCRfe0qyQBtMpTZDh4onaxe1otIntrRIIDFTBQCYOYpkut_Ikel0OJY-eDTdJZ_Nlz23-40jpl6d4zvKqdnAjKEcPgCm77xbKXnh6PTNIagHB8zf562wLhTmXAjTTwJizCsb-ENFwRHIAAAIm2CQSsNawFIvLp4BSllXp2x1FfcGjTvodgtUzDH1jM0_pdnY5L4Uj6MkakWKW2JjFkZHlsDSJIwPMu4IuZaOG5Ks_ZpyQW1vK_NkpELs0Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
استفاده مجانی از Claude و کلاد کد روی سیستم خودتون!
⚡️
دستورات استفاده شده توی ویدئو + پرامپت سه بعدی:
https://t.me/MatinSenPaii/4770
⭐️
توی این ویدئو:
1- بهتون میگم که Harness چیه و دوتا پروژه با یه پرامپت یکسان که با مدل یکسان ولی Harnessهای متفاوت زدم رو بهتون نشون میدم
2- کلاد رو نصب میکنیم روی سیستم و به روش استفاده‌ی رایگان ازش رو یاد میگیریم
3- با استفاده از 9Router، بهش Mimo رایگان شیائومی رو وصل میکنیم و استفاده می‌کنیم ازش توی Claude Code
4- با استفاده از API از Kimi3(مدل قدرتمند Moonshot که توی بنچمارک‌های فرانت‌اند در حد Fable5 قدرتمند ظاهر شده بود) هم استفاده می‌کنیم
5- با Hermes+Mimo و با Claude+Mimo و با Claude+Kimi، و با یه پرامپت یکسان، یه بازی سه‌بعدی می‌سازیم و خروجی رو مقایسه می‌کنیم
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/MatinSenPaii/4769" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4768">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E4AH1qMjMJEVWYRWqjamfjJ96daAGd6KDlAiFOpH2teVJ6N06b3ZlXyTMM72WfunhbM9ti6D1GK4_g-bXRbeVnbZBQelg36gbJABIeu988gryYmPLh2qyZAYh3hVeLgxXhywf6og78wp-XtzP_h_9f_BrTTGFqa1c5y_QHYm7pD6P_-h8aXQHuvWansgLx2Y8EK-JorFuRfQeDN2Xs9gZ0CUfr25Jvw5j9A1BKwuovtLzrzo5df9CI6r698n3dQqoeTMQzfzeysgUFmTCehF64hzvQJzPeuEpXUeq8QYNzW7cI4HkAU-PUO8-nbUgXq9C76uVS4o5b-WnIC74Jq-5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قراره اولین ویدئوی گیمینگ چنل باشه
😂
😂
(بازی سه بعدی توی یه فایل HTML که 15 دلار پول رفته سرش)</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/4768" target="_blank">📅 00:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4767">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یه آموزش باحال AI هم سر همین سایت ادوبی داریم</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/4767" target="_blank">📅 00:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4766">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.7.0 منتشر شد!
➖
هستهٔ Aether از 1.4.0 به 1.5.0 ارتقا یافت؛ شامل بهبودهای اتصال مجدد، اسکن، پایداری و امنیت SOCKS5.
➖
پشتیبانی کامل Zero Trust اضافه شد: Team، ورود با کد ایمیل، Service Token، Access Token و Gateway سازمانی.
➖
DNS سفارشی…</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/4766" target="_blank">📅 00:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4765">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بچه‌ها اگه خواستید شما هم توی هاگوارتز ثبت نام کنید
من نفر 37 هستم
🥰
https://potterhead.ir/?ref=WL-1B24AC#waitlist</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/4765" target="_blank">📅 00:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4764">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">(با کلاد رایگان زدیمش ولی)</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/4764" target="_blank">📅 00:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4763">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bvdJ_TPZ82pRuDidF3Hf1EZ_KeipHrdqtdzUGhaA0VwPWfs_eHdrS-iIR1rIGW2suJdiNf_43rppsCY-e-eHIGVDGTUl34aVl2dVrv5aguUa51avIEO5TJsXv8SHAejzr4f3-Mv6Ot9HkoLLD3MjAz4yIJtCo9PwdEHJTYXbqZDcqaex_nJzRR4TyChkkrBH2Eziim55aylILAmP4sS8tYvW_n8zGpTCLAkKw4GMWEPf-DcUMQmRoMqeM2ml4YHqZjZzi9wx300CePtT5TAeDvckaMp_C4Xsnb55DjJACWNUQEQjdnkLztVicCx_S_VQRTospNE0AXBWh7-qPlnCBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قراره اولین ویدئوی گیمینگ چنل باشه
😂
😂
(بازی سه بعدی توی یه فایل HTML که 15 دلار پول رفته سرش)</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/MatinSenPaii/4763" target="_blank">📅 00:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4762">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">صحبت بسیار جالبی بودش</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4762" target="_blank">📅 23:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4761">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JzUWsYcdyLrj8znC3EccjqYmg8qnU578ZaMYvH6mdtARJ9QqRAVMg8bu0cttkz5AAOn1HqePRoCqhJ5GeUIcFWDq1ieYsgrm_Wh22XG5ErfmMXLvS-7OjqykuP1SQhI3LPiJMT82JDV-5zpopHkUAIXdRP21YVpbHWsdZsl5ygmMdDyQlCLSKRdZxi5Rb5oSCJ--Y0B5dnkaJZNcQhT3dWtMkBcY2KTAk4jjI2POUqz1emaBuR0lLLSdjHOAST1g2l1ULX_jbFcGOJG8zYATYF8B1oYtRil1La5qR6yOt85Ro4SdiS5ahHacsATQQI7a5qkr0qG8xZtP4Ss_-PcHbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحبت بسیار جالبی بودش</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4761" target="_blank">📅 23:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4760">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q_W_O082osMbMYcvkEHHIxLiyH_uZ-rztnOxY2LRdj_rbJtlV--fywS9-rlSsnQ4Fc0NptLOirmZ_6mdoQS4kbSVLHzfYe2KyiWqNgtr3hHQO1_UEi2Gv3yD4zWJnO0BduvpXRptpvapIboVpnnfZB0VT19iWdNLPCE4o_0Hxl0VOwsjQmZoOx0sZEvO5gXVlN9yzGvoHv5y5hNQVw4AxZ5RygtUM8UetrvT1U8mRHytWGR8djHUNF0X1wbIv3E6rW0xRJP55HiKaTEXez7V_x2BeS6gL9HrZYgr-Dgd1bi-giqSIR8LtbXc3o3O15_tlphLKiaFGiNhhxmPI2nh4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه پرامپت دادم به هرمس که تمام اتصالات سی پی یو لپ تاپم رو داره میسوزونه</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/4760" target="_blank">📅 18:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4759">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CZGTf5R-nz9lbbkZkUzT0TM096CK1WNOyTp7OU8tBwhwo92R8iB5kNvxLA_DUBPmeYryxYaykn5k4-2kB6NgemfZNYNZiyH5Jsyr8LThU7xxLTppRvr9dRmf7DneRO2YYY8QHmaZwktwlNv4iAMMaJnmgbcfKRsViUyqJIAiJnJr-Lm4-f3Zubd_ZgddQN7XuyXoNMcpqiXFrRynOEIdD8UcfM3anz3TwRxjQoKCp6Z7zCXgonM9y7k4i_rklWfwQuW6wYGlXSb0suOWq4-OgatTMRrthqWXY8Diax_Fr2-Yy9aJWUm8tqMwXz6UedKiWN-zEioRT-8bSDA07iExXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.6.0 منتشر شد!   هسته‌ی برنامه رو به نسخه‌ی جدید v1.4.0 ارتقا دادم. تو این نسخه تمرکز اصلی سازنده روی تأمین امنیت MASQUE، فیکس کردن باگ‌های مموری و بالا بردن پایداری اتصالات WireGuard و Gool بوده. منم یه مشارکت کوچولویی روی خود هسته…</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4759" target="_blank">📅 18:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4758">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">و روی یه سری قابلیت خیلی عالی برای SenPai Scanner دارم کار میکنم که به زودی ریلیز میشه</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4758" target="_blank">📅 17:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4757">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LjRjdAn6Pws_pREpqiGAmrCe4N4MH8UAPVSF28yklZhLJ7J3ScIWdCqDAiSG17hhdgvTtXBwWPn2w8AMTir7hEj0U1wFYwVLwcoFIjVSLbFOC_pBWYPUnagseEV7VQCA-U6yhOry84xUZdYsOesuy-uOMDCEqgdwBMwk-5tRSR2Zz6kuEC7aj9heWi3IX2GCUeAtZ4uCj5of0jK-bmfl9nLNdCH8GDSQJUmlSPcMTqPACE8HlYIXiGgY_5jTjsMYMDVRr4sPs06d4q6vHdytkuk-IjYLw4FeLxVh9ycqSJiJTOGx9X8hzLSrzL1bLQWDPnM_uHPQRLra8LJvxS3v5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن جدید Aether GUI هم به زودی آپلود میشه روی گیتهاب</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4757" target="_blank">📅 16:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4756">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNima Aksoy</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21266e3b26.mp4?token=i5MbvBWatH6LD11NndCEb718eb7Scr5jGiJkBXqnYLJAKJwQw9qnb3LbDSUAR9nogwhzRWXywaab53uuoSYgw5ZP7QBAo9evGXHyLUAfyFEcr__E6keeSpng3pIggPI6sWzvtNKXbLsjwmKsGQRNdHc8gHTVcCAKCS01ZO1T_R8mZBvqNL_Rst12aBxMJl5sgK32bOFD02xu3xHmvvFRKzzi_ehJxeTilO4erdCjVTsjDtECjV7kn8erYfgzbOfOCDj4xJbfioTanrA270XUBj5WVrdm_l2d6Wjsb_59VUfTE4i4Uy9Y1qgz5eH4a0D0S6mbDK-D_f5mG9ncbGHuVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21266e3b26.mp4?token=i5MbvBWatH6LD11NndCEb718eb7Scr5jGiJkBXqnYLJAKJwQw9qnb3LbDSUAR9nogwhzRWXywaab53uuoSYgw5ZP7QBAo9evGXHyLUAfyFEcr__E6keeSpng3pIggPI6sWzvtNKXbLsjwmKsGQRNdHc8gHTVcCAKCS01ZO1T_R8mZBvqNL_Rst12aBxMJl5sgK32bOFD02xu3xHmvvFRKzzi_ehJxeTilO4erdCjVTsjDtECjV7kn8erYfgzbOfOCDj4xJbfioTanrA270XUBj5WVrdm_l2d6Wjsb_59VUfTE4i4Uy9Y1qgz5eH4a0D0S6mbDK-D_f5mG9ncbGHuVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه نفر با QR Code یه سیستم جالب برای انتقال فایل از یه گوشی به گوشی دیگه ساخته.
فایل رو به تعداد زیادی QR Code تبدیل می‌کنه که با سرعت پشت سر هم نمایش داده می‌شن و گوشی دوم با دوربین اون‌ها رو می‌خونه و دوباره فایل رو می‌سازه.
بدون نیاز به اینکه دو گوشی روی یک شبکه باشن
https://github.com/bashalarmistalt/decimen-optical-transfer/</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4756" target="_blank">📅 16:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4755">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مصرف GPT خیلی خوب شده الان که تست کردم
گویا از خود GPT-5.6-Sol استفاده کردن که مصرف هزینه‌ها رو کاهش بدن
😂
شرکت OpenAI امروز قیمت GPT-5.6 رو به شکل چشمگیری کاهش داد: مدل Luna حدود ۸۰٪ ارزان‌تر شده و Terra هم ۲۰٪ تخفیف خورده. نکته جالب اینه که خود مدل 5.6 Sol (قدرتمندترین نسخه) برای بهینه‌سازی load balancing و حتی بهینه‌سازی forward pass مدل‌های کوچک‌تر استفاده شده — یعنی یک مدل هوش مصنوعی داره مدل‌های دیگه رو بهینه‌تر می‌کنه.
این هم خبرش بود</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4755" target="_blank">📅 16:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4754">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⚠️
Confirmed: Network data show that major internet provider TurkNet in #Turkey is currently experiencing a nation-scale outage, corroborating widespread user complaints; the company says engineers are working to restore service
📉</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4754" target="_blank">📅 14:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4753">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">⚠️
Confirmed: Network data show that major internet provider TurkNet in #Turkey is currently experiencing a nation-scale outage, corroborating widespread user complaints; the company says engineers are working to restore service
📉</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/4753" target="_blank">📅 14:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4752">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNetBlocks</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkZdbesV5DSOzBnZ82r6oTmru-vkZsZRfbgosHJAL-P2pfdNeU_yuOFH8O8s2ouH_EMg5eIOgTvZATcIyWGagd0rqjci-9HpjmJgwowjMjQaxRCt21BlG_SUvtuUC1vILZmy8byQNnU-F6RDUPG_Pj6GWfDV0TsdN0umI1k7h53s5oB9q0sDxXQt0DBgezWLeAg-kvHJR-6ifCohJz10ay-8mi55iGUm-Yy_SjL0lD49ln6nA8ncGy7DBsR0IMc2x5YI2QrKa7WL2rN46wBhWDISe9czltORzcPvAFYymJ1Y4w2BZUGXqMpfmN5jKHV5hW85m9OALS9RQAENhrhQQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
Confirmed: Network data show that major internet provider TurkNet in
#Turkey
is currently experiencing a nation-scale outage, corroborating widespread user complaints; the company says engineers are working to restore service
📉</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4752" target="_blank">📅 14:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4751">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a9ec28d83.mp4?token=mTBhjnuyLCuYBkrikPPP0OkEmT4ScpXWdaL7bca1cBclZOR3dUB9R0r_jL3JGCJrsmj5jjwDCNLpxAPrBkdyeVfgm80_IET0S2Dtw-yJQIlOpgEvdm3IX8XfenGQeWchhoLFB-rYtNplNhTpJzLeiLaYPVgDh5T2e3p3GkxE0VIOwM67ylOhxza30DkgmO8BproX4fWLg19by9Erq7e5_whAeevuxBgGupjAU6VeQKS2F14kxiK_MvEJTS_scjdyEwaXXJeJ6lFsxeHf-IjWMGuOEQL21j_Jn38ZHkDlowD7ERHumNrJHXzUW_GbAG8DUwGQAGGp5LqJaY4afatV8Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a9ec28d83.mp4?token=mTBhjnuyLCuYBkrikPPP0OkEmT4ScpXWdaL7bca1cBclZOR3dUB9R0r_jL3JGCJrsmj5jjwDCNLpxAPrBkdyeVfgm80_IET0S2Dtw-yJQIlOpgEvdm3IX8XfenGQeWchhoLFB-rYtNplNhTpJzLeiLaYPVgDh5T2e3p3GkxE0VIOwM67ylOhxza30DkgmO8BproX4fWLg19by9Erq7e5_whAeevuxBgGupjAU6VeQKS2F14kxiK_MvEJTS_scjdyEwaXXJeJ6lFsxeHf-IjWMGuOEQL21j_Jn38ZHkDlowD7ERHumNrJHXzUW_GbAG8DUwGQAGGp5LqJaY4afatV8Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
آموزش ساخت رایگان، شخصی سریع پروکسی تلگرام کاملا رایگان و بدون نیاز به سرور
https://youtu.be/epG70Xl1xGI
@WhiteDNS</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4751" target="_blank">📅 13:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4750">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">طبق گزارش Science، استارتاپ‌های لبه‌تکنولوژی مثل OpenAI و Anthropic دیگه مثل گذشته دستاوردهای تحقیقاتی خودشون رو در قالب مقالات علمی منتشر نمی‌کنند. این موضوع که به خاطر رقابت تجاری و نگرانی‌های ایمنی پیش اومده، باعث شده تا روند پیشرفت علم در آکادمی‌ها و به اشتراک‌گذاری دانش توی حوزه AI به شدت کند و محدود بشه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/4750" target="_blank">📅 07:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4749">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHaoodi Senpai</strong></div>
<div class="tg-text">یادش بخیر، یک زمان اروپایی‌ها فکر می‌کردن مهاجرین غیرقانونی قراره بیان و با گذر زمان در جوامعشون integrate بشن
🥀</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/4749" target="_blank">📅 03:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4748">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">چیز بامزه‌ای شد Mimo 2.5 free + Claude Code و مجددا بهم ثابت شد که یه مدل معمولی با harness قوی، از یه مدل قوی با harness معمولی به شدت قدرتمند‌تر ظاهر میشه</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/4748" target="_blank">📅 01:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4747">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f09fb91ef.mp4?token=ADDF6VF_FXXTKYsWEl8HhVMjfY_2CDWRweV1Yaqvsnlu40bQyqyep_igJLaTMEGgMKfah5DggIr7HZ2zNXbtdVaFl_A8M-W5o4iT8FzDff2vL4GeNlpi-qY8yeujMcUmTuL6toJC8lrthoqchTF96lSzQtRvw_j9sWW53lWK3AmSsPSU5HXWSvXGVYN93CQeHMVC7fuzc3ohBIg-MNQ9arcV81tlUR_RS9MPA4J0UJvZNLsk-bakwhg0rwBck5Ccq-BmT7uWun2aYM0FuAu8O8d_b0BWtRkMKas7ZVwf0TtgYWhw-YdfE69IfW1uFKFtBho_2prIqImWuUz1GDsOMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f09fb91ef.mp4?token=ADDF6VF_FXXTKYsWEl8HhVMjfY_2CDWRweV1Yaqvsnlu40bQyqyep_igJLaTMEGgMKfah5DggIr7HZ2zNXbtdVaFl_A8M-W5o4iT8FzDff2vL4GeNlpi-qY8yeujMcUmTuL6toJC8lrthoqchTF96lSzQtRvw_j9sWW53lWK3AmSsPSU5HXWSvXGVYN93CQeHMVC7fuzc3ohBIg-MNQ9arcV81tlUR_RS9MPA4J0UJvZNLsk-bakwhg0rwBck5Ccq-BmT7uWun2aYM0FuAu8O8d_b0BWtRkMKas7ZVwf0TtgYWhw-YdfE69IfW1uFKFtBho_2prIqImWuUz1GDsOMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چیز بامزه‌ای شد
Mimo 2.5 free + Claude Code
و مجددا بهم ثابت شد که یه مدل معمولی با harness قوی، از یه مدل قوی با harness معمولی به شدت قدرتمند‌تر ظاهر میشه</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/4747" target="_blank">📅 01:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4746">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uGDGQq-kw4qocsuhsk8JP6rJxEcaE-J0PpN0sO-96URoGE6nTXZO9KaKKn7YUDd5xm9CqmAbWpxiOk-CYqoKvdBaLoNDOPc1NOjkJkpsPdg5O2wQv0Jjhhv3TpGPEZwTLVC6sSzHtw-yBNS-zHxRy1IvNnjSiBG4J1pN9tUZhNJqYR5x1B0qsEIYioDT4Of2Hqg1U4eeUGmOl5dfzGWkZb2MaJJ6xZXDy2p-bo40ZiGtAN6JQzKNepAoAok34ZQFMktxKLMg5lc4AYgyPvuggrta306iTlfObRv2S9jm6CFwqKUHCLSNHDF4pzimlrQ5oc7V-mrjdwgfDdDtvg_VNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه پلنی نوشت برام که اصلا GOD Tier</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/4746" target="_blank">📅 00:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4743">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dgWKVvbycDHl-TrqHFKjy-8i1N1C3gUyVZXdZvTSqCboQEYxDCRvcSb1XRZ8KOGJSZA5kbcvLw6OQ74rfucGGD-chAxQUwfrdfnBYG7I8hARtIneUkyV89QQ9oFHH5NGRF0VQkvtxRb6SpO9TYHgfBJ3ZqHc_1naOh5c86_5PNGY5xxSGlUrwYOgMs4g9iNbrDsqDVdJpYRGpHZzYgO4UmJEXweIdf1VjSoIpE9mxCvv1Un9M6IAHhNZLKG2DFBTOdQtWtO0qMcDNepJ84eYecMqzqTfsSectm6zvGv5KQJwqp3hd59LrUgGNHF4XxKCSaCLxXk4b265UTaF_JU1kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای گول زدنش به طریق‌های مختلف هم یه کارایی قراره بکنیم</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4743" target="_blank">📅 00:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4742">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">به زودی ویدئو داریم ازش
هم اپ دسکتاپ Claude
هم Claude Code
و هم Claude Code CLI</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/4742" target="_blank">📅 00:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4741">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">توی opencode همچنان کار میکنه mimo
با با ratelimit سختگیرانه‌تر</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/4741" target="_blank">📅 00:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4740">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AOa5Ze45n79k52bgy3JkG3ucpEpYklpRekJQJ1CEUPfQvHGK0NvWSojsN-ckM5rl_Uv8wZT--vmWv4dO6GWUjFpfUhVjop-NQ1ude5Ukf3kRj_F9CZ-aiy0SromJl0rQGGtTn6g-4uAahZHLGbHQtZPOpLP6E1AkyD57ywU948pCGU_8INXt6fUHGrOXqqxfLyPCoGvrPfJv5juNK5T3JRbHqhko3ODEW2gzCdfzLVQfm5kMMao7D4RQlDrts0UVZghUp_kUgDJdk5O5hyrj18XcGtMoBI37CF8QlnKvQfr1mFB7Ru-pfXseO-8iK3gdMuhpFApeAdJYU8cbAGycbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌اکنون سقوط سهام آنتروپیک
😂
😂
استفاده از mimo چینی در Claude آمریکایی</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/4740" target="_blank">📅 00:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4739">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.6.0 منتشر شد!</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/4739" target="_blank">📅 15:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4738">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">知的な戦い</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/4738" target="_blank">📅 09:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4737">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">知的な戦い</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/MatinSenPaii/4737" target="_blank">📅 03:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4736">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">روسیه دیگه دید زورش به اوکراین نمیرسه، گیر داد به پاول</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/MatinSenPaii/4736" target="_blank">📅 23:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4735">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگیفت بازار | Gift news(𝗂𝖼𝖾(𝜶))</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsqrnYjhXfhKPbuV1WXNctP0ssUTyTlRhy_CpOlkwFXAl8vPIzt3dsSArNCaZBXd9Yr56oxvonHN6ya5A5rg1En79hHNKRGWMO2bngOJwhT1eUGTGFEOinKtojthV32l4gcD-R2l3LdvCScq9HjU_qdE_bqZ2IOepHkx_L8M48FEbqzggnyoO2iX3OZ9pi2GSa4nxTE2Y4eaY190GnRx4iKoYlKZt9boyJAazDlbFV6LENh8jvmU01H8YREeftR3Jt-MrjkYum3Nb5f-k19kbD3KvYHw9Z4mpHqERWiryPvwW750A9Ge8E78t6W9tUM1JKrWf68KqrBfWSctSpzv2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوری | روسیه پاول دوروف را تحت پیگرد قرار داد
💸
بر اساس گزارش رسانه‌های بین‌المللی،
سازمان امنیت فدرال روسیه (FSB)
علیه
پاول دوروف
، بنیان‌گذار و مدیرعامل تلگرام، به اتهام
«تسهیل فعالیت‌های تروریستی»
اعلام جرم کرده و نام او را در
فهرست افراد تحت تعقیب بین‌المللی
قرار داده است.
💸
این اقدام می‌تواند پیامدهای حقوقی و سیاسی قابل‌توجهی برای
تلگرام و فعالیت‌ جهانی این پیام‌رسان
به همراه داشته باشد.
💸
بر اساس ادعای مقام‌های روسی، تلگرام اقدام کافی برای حذف
کانال‌ها، چت‌ها و ربات‌هایی
که به گفته این نهاد توسط
سرویس‌های ویژه اوکراین و گروه‌های تروریستی و افراطی
برای هماهنگی اقدامات خرابکارانه، تروریستی و جرایم سایبری استفاده می‌شدند، انجام نداده است.</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/MatinSenPaii/4735" target="_blank">📅 23:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4734">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JIdfIClbCjUdCg0vvyxnsnJbEb9hPNYaG4TQrVdisiBqiIV8u_44i1wzjbkU57gUa_1vyqincwME0uXFfDSaoUzOAEi4FgLG7hHcL2GgrVQCONiU81bq7MKDEeVEfc7OSHfsd3KgAGs_gZDrUTFnvvFYpH6g3aqHHu2VQnv4JGNHs0OHr-X32cYeE1MG-pMm5tmZzmsgpRMo6SCUZYCf62qv5HvEE8va93qKf9NKNDLGhgX1tDmmNP9KwRj85OdSCKLKSG9n7h_zMopKp9BVAgCIHt2nfIZv9yMqzqudXBT8GPvG6yWlSXOYm2iY9bdgzOafJLMki6Nor0DMTZemxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم این کار خیلی قشنگیه که هم برای حمایت از پروژه‌های اوپن سورس و هم برای تبلیغ کسب و کارتون، می‌تونید انجام بدید</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/4734" target="_blank">📅 23:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4733">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">آپدیت جدید Aether:
https://github.com/CluvexStudio/Aether/releases/tag/v1.5.0
\\\\\\
بزرگ‌ترین آپدیت تا الان رو دادم دو تا قابلیت جدید و یه سری فیکس امنیتی. توصیه میکنم حتما آپدیتش کنید مهمه و خیلی بهترش کردم و بشدت بهینه شده و شانس وصل شدنتون هم روی شبکه های پر اختلال هم بیشتر شده:
- پشتیبانی از Zero Trust (وارپ سازمانی) "وارپ پلاس"
قبلا Aether همیشه به عنوان یه دستگاه معمولی وصل میشد. الان اگه اکانت Zero Trust دارید میتونید با همون وصل شید. هم روی مسک هم وایرگارد کار میکنه.
(پلن رایگان داره کلی فیچر اضافه بهتون میده نیازش داشتید میتونید بگیرید و وارپ از حالت معمولیش میشه پلاس ولی بیشتر برای Enterprise ها هست چون Egress Policy داره میشه لوکیشن خروجی تنظیم کرد)
موقع اجرا گزینه ۴ رو میزنید
نام تیمتون و ایمیلتون رو میدید یه کد براتون ایمیل میشه وارد میکنید و لاگین میشید.
توی داشبورد کلودفلر Zero Trust نیازه ستاپ کنید..
\\\\\\
قواعد مسیریابی مثل Xray اضافه کردم:
یکی برای بلاک کردن کامل یکی برای اینکه از اینترنت خودتون بره و تونل رو دور بزنه (مثلا برای اپ بانکی یا سایت‌های داخلی که آی‌پی خارج رو قبول نمیکنن) لیست بلند رو هم میتونید از فایل بدید.
\\\\\\
فیکس باگ گول که بی‌صدا قطع میشد. این رو یکی از دوستان گزارش داد (issue #65)
\\\\\\
قطعی‌ های کوچیک شبکه دیگه کل تونل وایرگارد رو نمیبندن...
مصرف رم روی سشن های طولانی با قطعی زیاد فیکس شد.
-----
ترتیب اسکن رنج آی‌پی‌ هم فیکس شد الان طبق داکیومنت کلودفلر اسکن میکنه...
\\\\\\
روی شبکه‌هایی که سرور ثبت‌نام کلودفلر رو بسته بودن
به دلیل فلگ شدن آی‌پی یا هر دلیلی... کاربر اصلا نمیتونست وصل شه.
الان یه راه جایگزین داره...
کلی فیکس و آسیب پذیری هم رفع شده اینجا جاش نبود بگم...
ممنون از همه کسایی که issue دادن و گزارش کردن :))
لینک اصلی پروژه:
https://github.com/CluvexStudio/Aether</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/4733" target="_blank">📅 23:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4732">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4732" target="_blank">📅 22:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4731">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bZASuWWBrDSZ5-_ulYxVJ5pV1AECBabDs5-edsK_Eo3MH3AxA5WUhK3YeKx6btsYBq_P9H3il2v8WbkhQFeoGTyVtjwa-uEtpnLyNgYOkO11EcUAA49r2RScpXxzUI5youvDMKH3dy9waeIVs_kx1_KmK0fPh05wU-NigufgvSoUUWOdZYbJ1sYsVtV4luzz-GQHI6AtM4FjgmhW3irq11sgOQok9S7ClVWHxvskwL7os-G5wwE3PifFArPWZhaolbMsZT0WeUQxTMJZ9YeuCnGFySDYjziqM16PBnsNrRCiZK5SjKmfBHU9qhTLdXy9xmyk8VUZP8aLO_XXmpBA5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین دسکتاپ لینوکسی که کامل توسط AI نوشته شده!
یه پروژه به اسم Starling منتشر شده که ادعا می‌کنه اولین دسکتاپ لینوکسیه که از صفر تا صد توسط هوش مصنوعی نوشته شده. این نشون می‌ده که توانایی AI توی کدنویسی و توسعه نرم‌افزار به سطح کاملاً جدیدی رسیده:
https://starling.build
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/4731" target="_blank">📅 19:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4730">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/00a76c08a4.webm?token=pWFUGhFhUoTcO12biyTy4UQp04FeDmqjH1qv4062fb1pA0t4lGOIIxfRtlv7NtKVts9hjf1gWRAXdKllf6igvs9rRMOyU_NT5AVefynOQFgUeV_ZNX2SICovW9EaHDqTShhbFEFgkxIIaxGlq0Dsj3To1Eedflu2fDq4en2KnZ4tHsAJ0MmNqX_Sj_LJUjPTmc3b2E-O7jGa1Jk_FDoFe7623fvCBqz-_8vz-m7E-b6b00KBDrlVAD6ZTJSfjBilK9qXZp_l2GrpuDkaBKr1ZwEAuPpFbJcQ6Ar0Ynbfb0JQqct8lIClFRmHj71Y11-z6BllKCn-xmTRgKfGzXsIww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/00a76c08a4.webm?token=pWFUGhFhUoTcO12biyTy4UQp04FeDmqjH1qv4062fb1pA0t4lGOIIxfRtlv7NtKVts9hjf1gWRAXdKllf6igvs9rRMOyU_NT5AVefynOQFgUeV_ZNX2SICovW9EaHDqTShhbFEFgkxIIaxGlq0Dsj3To1Eedflu2fDq4en2KnZ4tHsAJ0MmNqX_Sj_LJUjPTmc3b2E-O7jGa1Jk_FDoFe7623fvCBqz-_8vz-m7E-b6b00KBDrlVAD6ZTJSfjBilK9qXZp_l2GrpuDkaBKr1ZwEAuPpFbJcQ6Ar0Ynbfb0JQqct8lIClFRmHj71Y11-z6BllKCn-xmTRgKfGzXsIww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/4730" target="_blank">📅 06:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4729">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">چقد جمعمون همه پولیسیم
خوشم اومد</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/4729" target="_blank">📅 06:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4728">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HHgu9VcYwSEOA7wpQpdAoyXWtTIbDYh7qcvYbf-07RXcwdnu7WhtLVyTSglV8HgVI-3xU1lojSh8EbyZEKmIB1018c2M6hrp7YRT3RthNUUaCQnRvP3ldLsRBqxQm81Dji09a82j2G13ueRLyVfONWl81ff8jGeQpFbSBqRhkvSj9xMcxAQZ-Rr0vTIEbliLXHkRK1w7bJaw0h-WRMp4Atr9JGvS-gM1z4rTahDgKbSavQ0GDWTX2UulfkPVq0GgwjdaLN0kGkUEAmKgXspLKKXtR0S5dZ58QGbkCTWQF3Jo4uGeEbTkNCg0eyC4lYvq8nSgvg_UeJWM-Frk9OWd0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقریبا بیست روز پیش هم این اتفاق افتاده بود</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/4728" target="_blank">📅 06:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4727">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QdnT4x8CPG9vTbv7SLQ_2ts7IUnFyTJJjT_Z9Mnndm-_QKydWIxRj--JaYU2EobPUCEf8eT5oV5JOuDH4V0yRzRc6h_rdvzeKZrLlpRq1hST9N_3A4NIcrgO9FsvTa91QmifYrc9CHKDziAu0CMbc8pJSW4XwrNa87tlSGyeH3dLAAlDTWJvyru1-m7VxJvpvNfeufFs3pGO7lLApNRlmH0tqVQdO9qi43LgJLb5Ntepk-uwl8c8i5tQpvacsK0j4rwVcq8ji0ebf2CwTBl8cGzpycxFl5Hverw6p7odHo7tj6eHr0jhv3DWnchyreLV2eTBiM_rlXqdGv7jXxI1PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه چیز خیلی عجیبی که دیدم و تست کردم، این بودش که اکثر بات‌های روسی/انگلیسی دانلود تیک‌تاک و اینستاگرام و یوتوب و Shazam و... همه یا مال یک نفرن؛ یا از یک زیرساخت استفاده می‌کنن. یکیشون اگه خاموش باشه برای چند دقیقه اگه همزمان به چندتای دیگشون هم پیام بدید…</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/4727" target="_blank">📅 06:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4726">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دیشب گویا روی نت هم یه گندهایی زدن
زیاد شنیدم از بچه‌ها که ۵-۳۰ دقیقه نت قطع یا به زور وصل بوده روی اپراتورهای مختلف</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/4726" target="_blank">📅 06:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4725">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یه چیز خیلی عجیبی که دیدم و تست کردم، این بودش که اکثر بات‌های روسی/انگلیسی دانلود تیک‌تاک و اینستاگرام و یوتوب و Shazam و...
همه یا مال یک نفرن؛
یا از یک زیرساخت استفاده می‌کنن.
یکیشون اگه خاموش باشه برای چند دقیقه
اگه همزمان به چندتای دیگشون هم پیام بدید
می‌بینید خاموشن:)
ماشالا به هوش کسی که پشت ایناست</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4725" target="_blank">📅 06:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4724">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W4xlaH0HQJmGd2Y6w-h47QaxCuvBQKBRPWPh-ygxNffi9mhc27hOeom6KKdkLxrgkP9ERFORYBPEwBvlqONE-juIqjRo2zWuXfRFUpvzVnKs4AjHW6_M47N2cre_lqFd9lbjrl1KhsnwILTKu7t1rIIPHrvn9pqZeSY16GTpO9ytpUP0oITPMOECx3EnLKUEyLEmj8My3c59EmLawEJrIUgZ0ykfJjqzk0oieesFP3CSEXPPs6iNmqcLoUdN_Iinq0CX74j2HnPxytjKzcxyaoTHFiHo18rmZe7BqguIv28QqXr_cjfpUnfvWBHRq5GohyLBMtussZgrlUGWrAuFYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دیشب به شدت این اپلیکیشن رو توی کانال‌های تلگرامی مختلفی دارم میبینم که گذاشته میشه به عنوان توییتر.
از هر کانالی که داره نشر میده تقاضا می‌کنم که نشر ندید و لینک گوگل پلی بدید.
به خدا گوگل پلی نه فیلتره نه چیزی.
نشر دادن این apk ها توی این شرایط یا از حماقته واقعا، یا از ندونستنِ مردم سؤاستفاده کردن.</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4724" target="_blank">📅 23:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4723">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dj5q1VzqQa04fBNvuCPM9FiRTevezNL_osFPxRRyd7NoZGo6O1SQzjc6a1cOgAvysM-yPG3TbSiZIGWM3JrXkxu7Dl-VP_jwioDSLVITdE1Ri--SsuK5n6GSUTUjEXHhj2P-S_XM4i9tDh3YF9HV1yuRwm4NepU4dhq76rPIoUm52cHL67wtHsvHqCRAh3Wp4-QNtcOAiqvDj1pzkKmPuGQnhkdHDAgzJgYSZe8yNMVRNb9kJbjiF40TpEJYr_KCut94VMvgnt96N4UXv6rmPbxUGJtT1wjy5wHeXj6F9PcEjkj-rbFwyYWOJs4ZJfFIBKI9HOfx3J2xyaZ4WETQ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت Moonshot AI بالاخره مدل Kimi K3 رو اوپن‌سورس کرد و همون روز اول Telnyx بردش رو Inference API خودش. مدلش خیلی گنده‌ست (2.8T) و برای ران کردنش زیرساخت خفنی می‌خواد، به قول یکی از بچه‌ها در حد نیم میلیون دلار. ولی چون تلنیکس GPUهای خودشو داره ادعا کرده که سرعت و تاخیر رو خیلی خوب کنترل می‌کنه.
قیمتش هم فعلا در حد Sonnet 5 هست تقریبا، با قدرتی که میگن معادل Fable 5 هست که نمیدونم چقدر درسته واقعا
https://telnyx.com/release-notes/kimi-k3-telnyx-inference
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4723" target="_blank">📅 20:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4721">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lJygiJacWxF_614ZfqNff9EjtB_0wCXlHcUwW6SFi6nYdjlSt5cLZWlrHed7WGI5RSosTz9IlQsPFdRrFbPkG5DO5wG438lasV8mb73mC6aCBuR0TtvEg5Sxk70rMASVB4-0gwFzezxStgo21bThNZIDEVHC7qjd36y8BDGpmPveYD-OEjPOw5Lk3l_d3EiMjAGuNWB7ARIi_cib8J4sSXEliJcQZ1dlyeKwye2h-kl7KdcQQil0uxixsVNWodX_7jkLHLL9kTCCLTeHfrnIvGicTHh3pxsCYsTJq6JctFENSGKH59NmSsDwy2lugTO8uDVb1bR18_DWiCWi4y_5dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gQEPRINMhCRN4A2nWnRe1EOI8mFgcxLLq_wghbRhcdzaC0jl5TEOTCkNEplCSkRvhL9c5-SWdomU9d-gL9db5Dz92qpU_mM0g20DjItryy2aI5JfSSq9TOJILYPzc-YLk6ERJjY2pAXdiXCsQ3PqeAKvbdydAnEcBllY7R7oxP9vh2w2BbYR3SNd1fp8QZMvkU7XuzkQW6CvahboV1h4mfOAuJ9YNIhnKwpbLl1QS615Nhs1fhH3DCWsi1qGk3kd1k2yngz3Iwyp9ORjVhVnYqdnIID-zvpn7a5guzr4Sz_I0A_2dD7Sn0VaU-qxyN3PlI0WBDuNenOF9eAYSfulSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سرور جدید CottonDNS برای تست در نسخه 1.6.0
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید  cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiZ2dzIiwic2VydmVyIjp7ImRvbWFpbiI6InYuYXNoZW50YWppci5zYnMsIGMuYXNoZW50YWppci5zaX…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4721" target="_blank">📅 14:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4720">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بچه‌های WhiteDNS انقدر زود به زود آپدیتای خفن میدن من اصلا فرصت نمیکنم بذارم:)</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4720" target="_blank">📅 14:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4719">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">به زودی کارهایی برای Aether-GUI انجام میدم
دلیل بررسی نشدن PRها همین بود</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4719" target="_blank">📅 14:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4718">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
👆
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
❤️
سرور تست CottenDNS   cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcn…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4718" target="_blank">📅 14:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4717">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
👆
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
❤️
سرور تست CottenDNS
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcnlwdGlvbl9rZXkiOiIyZGRlYjlkZjJjMmJhNGQzIiwiZW5jcnlwdGlvbl9tZXRob2QiOjN9fX0</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/4717" target="_blank">📅 14:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4712">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.6.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">8.8 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4712" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/4712" target="_blank">📅 14:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4711">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXeNHUh11GuB-UXZ-APZrsqpSuzoN4cRK6T_tcIYY_SLr4g1iSrFmy971-m7ztM7TJ9aAt_n1up8du-D9ffxEij8DDUlhYyo5x6fjftSX9xPqkoYiisnG-HfEVmZnbtdVxnC3QLVNFvlEM_Aq8BZhd9upfl8DF_Yd89ZGFzAvQlaxOvq5zEJyZTefqA98jIMFPDAM30bZ1d_66-Y_kcUQAzBGS5ZdQ5rq2I6c8ZNprF9uNM1Da-M6zQ7_3-U4MyULnyR6PU6fs7oqx_vksinUp9NCqaNkSw9MEGb82XA_UcwRNButLT_jj83q1Ds-x5pdqy-ehTO3IFbyOEa4GYX2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
در این نسخه، پشتیبانی رسمی از موتور
CottenDNS
به WhiteDNS اضافه شده است.
CottenDNS برای اتصال پایدارتر در شبکه‌های دارای فیلترینگ، پکت‌لاس، DNS Poisoning و اختلال شدید طراحی شده و در هر دو حالت
Proxy
و
Full VPN
قابل استفاده است.
مهم‌ترین تغییرات
* اضافه‌شدن موتور CottenDNS
* پشتیبانی از چند دامنه در هر پروفایل
* تنظیم مستقل MTU، FEC، Duplication، رمزنگاری و روش انتقال
* بهبود Import و Export پروفایل‌ها
* بهبود رابط کاربری و دسترس‌پذیری
* سازگاری بهتر با Android 15
* ادامه پشتیبانی از پروفایل‌های StormDNS و MasterDNS
این نسخه انتخاب و مدیریت روش اتصال را متناسب با شرایط مختلف شبکه ساده‌تر و انعطاف‌پذیرتر می‌کند.
📱
دانلود WhiteDNS ورژن ۱.۶.۰
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.0
⚠️
⚠️
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
سرور تست CottenDNS
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcnlwdGlvbl9rZXkiOiIyZGRlYjlkZjJjMmJhNGQzIiwiZW5jcnlwdGlvbl9tZXRob2QiOjN9fX0
@WhiteDNS</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/4711" target="_blank">📅 14:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4709">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/33e9f6f644.webm?token=h-sDW_RtLHt736VdpxBYUEtQ7sCDAGmvJDAOhGHx-ulDXIf6spFzAYokRV6JuzIlx0ALOew4PiNrQzqR9SLg0YSKaTekX-6JVOUMtbWSYxeSPg76MlWi4eNigCYgLsBSuxa7TReUTxpnJGph53JhaI8WM01dGMcRfS0MC7YkJ4i8qAXNYyapRh6ahgJ9tJaocvnO7E9ZzUYmzXBEmqsrwotbymuof8yrAY1l0V3HInqQOG37R0lE2079uHCGP5Qh6vCyxf1-vU_M0KNNC--tgIwpx3p03ADoKX6nHwOB91BGjm5GEyM8Z_QH5_A4SWnFrGT1NgWN7n0crvhjDoQf8g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/33e9f6f644.webm?token=h-sDW_RtLHt736VdpxBYUEtQ7sCDAGmvJDAOhGHx-ulDXIf6spFzAYokRV6JuzIlx0ALOew4PiNrQzqR9SLg0YSKaTekX-6JVOUMtbWSYxeSPg76MlWi4eNigCYgLsBSuxa7TReUTxpnJGph53JhaI8WM01dGMcRfS0MC7YkJ4i8qAXNYyapRh6ahgJ9tJaocvnO7E9ZzUYmzXBEmqsrwotbymuof8yrAY1l0V3HInqQOG37R0lE2079uHCGP5Qh6vCyxf1-vU_M0KNNC--tgIwpx3p03ADoKX6nHwOB91BGjm5GEyM8Z_QH5_A4SWnFrGT1NgWN7n0crvhjDoQf8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تخریب چرا؟ اندازه پنج جلسه تراپی کمکش کردم.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4709" target="_blank">📅 00:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4708">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بانو یه جوری تخریب کرد که فکر کنم طرف کلا توییتر رو دیلیت کنه بره به درس و مشق و کلاس‌های تابستونه کانون پرورشی برسه</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4708" target="_blank">📅 00:30 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
