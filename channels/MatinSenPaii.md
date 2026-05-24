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
<img src="https://cdn1.telesco.pe/file/YH9ncQOy9ia6Bz6P0PXN8SlkpmbxRNjpC54uApeyZBXJg42LGSGlyjq3muH2DGFeQGNKPMBrVBMHF90ocGxGQe9j24tBRdrJafAGbIJiepNLIovDid0myezvK-VKthYKO0BwqUWitt7x3ZC0kqAVjrJbcqy8Zus8y_oaVs_XD_HI6KGG5ZmVM6TKt8d3JXhSrsk2rievAAQvJh7tY2HEgRQ4KnGlhfKy1IyU_8u7D8KItFJ4FXxG86AJoOzzznKI3Ja3i8rGWlWWt0Xx8U82EleLjkeqzkjqXP2MRc1Av5YIrsZiO5vh8V6YEJvjajjrX06Zl36RW6ZaavdOXVVsWQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 148K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 یوتوبر انیمه و مانگا(الان کمی شبکه؟!) - برنامه‌نویسِ ایده‌های باحال•YouTube:http://www.youtube.com/@Matin_SenPai•AniList:https://anilist.co/user/MatinSenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-03 11:48:48</div>
<hr>

<div class="tg-post" id="msg-3399">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکلاینت شیر و خورشید</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ShirOKhorshid-2026.05.24.apk</div>
  <div class="tg-doc-extra">25 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3399" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/MatinSenPaii/3399" target="_blank">📅 10:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3395">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکلاینت شیر و خورشید</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/riL9T0IV1E0dFlpIizkbDz3ibZxEevuV39mgq1ozugoYKb84krMIhoU1Vj2XXWuJ5SL87wPEL_nyKWDF3zWcNa6i7zOTTpb61jZ6kuCiP1ADR72JtVSe1x-1iyC6C9rEi0WFicH9vomFmH3FKS1MHjnaFKbc5ErqkqIaISZrDocQEqbi8XC_vXaiGoyiU8fPRglhNtbpMoMYs0DJ4YwBfhpwL-e3M40xUZRVMt74DlWUpjEXtIzy7BvwTFyO6J2X6zjsLAFRXkVL59c4mWiYNxZMnr9KfuTnwuqBt8jSzLvxFEChTAkCq1ECqbtsppNzGxCkOKKCnyGqsgTTpGwQ6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hkzPMyDZ6eTdZzfhvWFUHpvuPm3Vo_a_IltCU9H3EsgVJHpR1scRfWVOVBCWsxsT5RHgKe2xqgusTqyy3nk8JnU2_McPNP_jIkIUPf81XsvUeZQaRDbKhOPb0D_8WNlkXhPVUppYhEZ79r4spsAxGFSKeJDva422EF4ZYTPAxGmyvQaDwaNEyWGK8UTuhs47AyPrfDxGOQIGA11EsRqwKz5Qp1UokhzHuz8LCJGTbiSzxDlGHwycyPCejEtsl3zgvJuOMU0g62z5HIMhf_yoaNK1ZklOPyG1iey3JNbiRAaPDrxtf2RJiBIRWsyEIUB6EBhWEhkakfMuGzwNjfFXrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XBXXavW0A8iv1xT22iP4W0kgR2MeFOygz806ysPAmZY7Ty49PNvbY3bGjPXGHGcfoN4NoRxu_6n4lhw3dg6rYtnFhz-rOLbhidVIMqcI9B7qU0VvgzADFTt0ZAT_4gl521KzugEn-JYm6k3iSnMqDWfPHfx-tC9ZVqukmM3DwiaG3qZLdws2YitprWZHKIujcZZsPFm55hN7422nFIGI141CdNLhVTPOpdZkPXebyEcOVYKiEMCwDVskR9y-BAxEqGqn_9O4lp5QUo2JuS3C1e4Dl0h0JqY6w2OS6Rz1tikCtm_oQlPwyWVuqPqgYZ8EjMkG1n_fxBCw6e5u6WR0jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EkQ5UB31uXd4CWGWbnRTdys-8iJNXCDlS1IH57p-YfSV1fhfy_1dmJh5u9sD4CrqTtLpvzCXXv8AJuBzOJpQ3bafOxYDqtJ6-SHwWqpSRApfu7jSfERGzxXhh-cXScwC_i6D7Wc-jS1_e5fQKSo9UqgKs4nTrzJZ65dGbMMPCw7SDadDyC5cnQ5JSViumzhetNlE2Z_7qh0FfB_4W4N4vm9ckhsEvNXehh16HXrZN0rZ5lsCjw5swrrl-S7M7lDPZWC2MnuOKDHSAaoooW9kVB_ZGw3MZRWWu9ZOQfFkk39TQajW4AFVDbIKxwSZh_A-eJ54prUIg0zQUKg_ZhXnfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آپدیت جدید کلاینت شیر و خورشید 2026.05.24:
- آپدیت Beast Mode برای درست کار کردن روی CDN Fronting
- اضافه شدن اسکنر ای‌پی. برنامه لیست خیلی بزرگی از ای‌پی های ممکن را داره٬ پس اگر در اتصال مشکلی دارید پیشنهاد میکنم تنظیمات قدیمی ای‌پی ها و SNI رو از قسمت settings برنامه حذف کنید (خالی باشه)‌ و اجازه بدید برنامه خودش کار رو انجام بده. دقت کنید ممکن هست بار اول خیلی طول بکشه٬ حتی چند ساعت!
- اضافه شدن پروتکل های بیشتری که با CDN Fronting کار میکنند. احتمال اتصالتون و سرعت باید یکمی بهتر باشه الان
- قابلیت غیر فعال کردن سایتی که زمان اتصال٬ سایفون باز میکنه!
- قابلیت تنظیم پورت مورد نظر خودتون برای LAN Proxy ها.
- قابلیت تنظیم username و password مورد نظر خودتون برای LAN Proxy ها. این تنظیم دلخواه است و اگر تنظیم کنید فقط با این username و password در شبکه خانگی میتونن به شما وصل بشوند.
- آپدیت شدن هسته سایفون
میتونید از اینجا دانلود و نصب کنید و ممنون میشم اگه به اشتراک بگذارید که تعداد بیشتری ببینند:
https://github.com/shirokhorshid/shirokhorshid-android/releases/tag/v2026.05.24-a3b91cf</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/MatinSenPaii/3395" target="_blank">📅 10:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3392">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/orm2v3JO8DESqy2vU_ZLQUfAF3tj_9NDX6hGWZHNAzdNqqHZYS1tZsrVhRyQtH8ZGas0C_jIlmEtoQq2aFQ1LmEAF8iCCpbpYxLVCQ0HSfvgGh62OSqlrvpp1WkCL83jbRSgJ5EsVg8_kbi-_x7zGuIHRj8Fptb7A2P_c5HLkaZ4uA7vQPT2UPU09UD98SFYVAnP9UFL3OMFKvn4MeyttVnpNd3Ic9PlvCCKLZ4kGdN4vaFUirTOK8FYYOEFtfXSwvAwGaksUicVWLAb_3a021ksvazP46JuLjhzXPjA96RYNgPw7fhMVtuK1meZ7MVT6cEJyesOiMDZnRKJ1ZImjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش کامل راه اندازی MasterDNS و استفاده از WhiteDNS ویندوز و اندروید
⚡️
لینک داخلی ویدئو: https://up.theazizi.ir/download.php?t=7c97d6d4997fe6ad02da91e2b5381ff779e6
⚡️
فایل‌های استفاده شده در ویدئو: https://t.me/MatinSenPaii/3373
⭐️
توی این ویدئو این…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/MatinSenPaii/3392" target="_blank">📅 09:48 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3391">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">سلام خدمت همه همراهان عزیز
ویدیو آموزش ساخت سرور شخصی که متین عزیز تهیه کردند دقیق همه مسایل رو ‌توضیح‌ میده.
تنها‌ نکته‌ای که باید اشاره کنم، متین از ترمینال برای وارد کردن دستورات و نصب MasterDNS استفاده کرده.
من پیشنهاد میکنم برای راحتی کار شما، بعد از خرید دامنه و اتصال DNS از ربات
@WhiteDNS_installer_bot
استفاده کنید.
اگر از این‌ ربات استفاده کنید، فقط با پروکسی کردن تلگرام‌ میتونید سرور خودتون رو مدیریت کنید و در شرایط بحرانی فقط از طریق تلگرام همه چیز رو مدیریت بکنید.
ممنون
@WhiteDNS</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/MatinSenPaii/3391" target="_blank">📅 09:11 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3390">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اما تا ۵۰-۶۰ گیگ روزانه نباید موردی داشته باشه. سرور رایگان هم خواستید از سرورهای کانال مسیر سفید می‌تونید استفاده کنید ولی خب تفاوت سرعت رو توضیح دادم توی ویدئو که به چه شکلی هستش:
https://t.me/Masir_Sefid</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/3390" target="_blank">📅 08:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3389">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z2SAp59Nm0PtRfVltJChPeJ2GlPbL3kyNZyEuXL3ADZlykZFZsS1LW04Yy3XhAED9wIAxIzk0JeBs9zg2ZCXInaSmdYccltgiSEdbQmuVgdxm766D0-2aIho0ISPivl7aUdQcgcvtlUmBw8Dd3SwiHjse3iaIB9uRVVLtiXuxav3NY-9RxtwYNPoKie6FKjk7cHnLS9y6BbcTM2NAheb2dwetSCQKXE_aw33WdUHPg37P1ht92A-LCUZFPOE0beFvXz7EjeHyiUDo6nWK28jmlDyq5KBFS13HljcMKaP5fo4eT6Q1__APD8-eS5HcUUH1xzeXmqXj-ynzkECMipQ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ حجم دقیقی وجود نداره عزیزان. اما از چند ده گیگ متفاوته تا ترابایت حتی
گاهی اوقات فیلتر شدنه کاملا شانسیه متاسفانه</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/3389" target="_blank">📅 08:02 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3387">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ProxifierSetup.exe</div>
  <div class="tg-doc-extra">5.2 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3387" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این هم پروکسیفایر و یه لیست از Activision Key های مادام‌العمرش (برای مک و ویندوز)</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/3387" target="_blank">📅 03:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3382">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.1-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3382" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه Universal اندروید لینک داخلی:
https://up.theazizi.ir/download.php?t=e8a7a62516394e4aecbd26ca36dbb113e0aa</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/3382" target="_blank">📅 03:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3374">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta3-linux-amd64.deb</div>
  <div class="tg-doc-extra">17.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3374" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه ویندوز X64 لینک داخلی:
https://up.theazizi.ir/download.php?t=4b31fefbad0c08f180216f8e4c1eecc316d7
نسخه لینوکس amd64 Debian لینک داخلی:
https://up.theazizi.ir/download.php?t=bb6cfd1d86d4ed7a1826a4850b901ed46c58
نسخه مک amd64 لینک داخلی:
https://up.theazizi.ir/download.php?t=acbf869993172d51c2286fc812931ef48fd4</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/3374" target="_blank">📅 03:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3373">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Master-White-DNS-@MatinSenPaii.zip</div>
  <div class="tg-doc-extra">25.2 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3373" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">حاوی فایل دستورات سرور
فایل لینک تمامی سایت‌ها
فایل 5800 ریزالور جمع‌آوری شده توسط بنده از سرتاسر تلگرام
لینک داخلی:
https://up.theazizi.ir/download.php?t=b9162802b5da63cf5b39b02133170f4ad2bf</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/3373" target="_blank">📅 03:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3372">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">☠️
آموزش کامل راه اندازی MasterDNS و استفاده از WhiteDNS ویندوز و اندروید
⚡️
لینک داخلی ویدئو:
https://up.theazizi.ir/download.php?t=7c97d6d4997fe6ad02da91e2b5381ff779e6
⚡️
فایل‌های استفاده شده در ویدئو:
https://t.me/MatinSenPaii/3373
⭐️
توی این ویدئو این مراحل رو پیش میریم:
1- خرید دامنه و سرور ارزان با کریپتو(+آموزش)
2- تانل کردن ترمینال با Proxifier و ssh زدن با خود ترمینال
3- تنظیم دامنه در کلودفلر و راه‌اندازی ساده‌ی سرور MasterDNS
4- استفاده از سرور MasterDNS در کلاینت های ویندوز و اندروید WhiteDNS
5- توضیح استفاده از Parallel Testing در WhiteDNS
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این متد نیاز به خریداری یک عدد سرور لینوکسی و دامنه داره(مجموعا 5 دلار نزدیک به 800 هزار تومان) کافی برای اتصال نزدیک به 5 نفر
کانال مستر دی ان اس:
1-
https://t.me/masterdnsvpn
گروهشون:
2-
https://t.me/MasterDnsVPNGroup
کانال وایت دی ان اس:
1-
https://t.me/whitedns
گروهشون:
2-
https://t.me/whitedns_group
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/MatinSenPaii/3372" target="_blank">📅 03:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3352">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ScJEvJlw97j5i28fXuiHCPEppK3t-Y0OlB9150grV5qahpBgh9cHoHQ55ZbqGGh308EcQW06fTokqwbe23ovYv2y55Hj25-BWH_1f1U2X5sYPxdF9Fu2pX_qb4lj0VdbC3POiaTB8dc0FCeNrEUADInXrvNz5twaNVxyIzUXKozzPBysjfaU5iUk1gg8FTM1DHaCUOOBsLQofsrfgw-llK8uTnOaZCXiFMBRdJ-wAWLnLxY3MZp1bbYqLkgGa2c81BGbN5EMLYznZJzBmFi4ivlLkbaw20inyJSlCRGSlZnsEakD_B4X5ndCWXtWKDgfprcgnq1PdzZGa0nJ8WchUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدرام وقتی
یه پروژه جدید
میزنه و مردم میریزن سرش هی سؤال میپرسن ازش:</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/MatinSenPaii/3352" target="_blank">📅 22:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3351">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">آموزش بعد از یک ساعت و نیم تایم نفس‌گیر تموم شد ضبطش(خودش شاید اخرش نیم ساعت بشه اما مشکلات فنی‌ای پیش اومد اواسطش که متأسفانه باعث شد طول بکشه اما در عوض خیلی کامل و جامع شد)
نیم ساعت دیگه میرم برای ادیت، تا ۲-۳ صبح ایشالا حاضر میشه
با تشکر از همه‌ی بچه‌های گل تیم وایت دی‌ان‌اس و مستر دی‌ان‌اس</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/MatinSenPaii/3351" target="_blank">📅 22:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3350">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">Matin SenPai
pinned «
ببینید همراه اول میتونید وصل بشید؟  {   "LISTEN_HOST": "127.0.0.1",   "LISTEN_PORT": 40443,   "CONNECT_IP": "85.9.112.219",    "CONNECT_PORT": 443,   "FAKE_SNI": "www.hcaptcha.com" }
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3350" target="_blank">📅 19:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3349">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i_nNwFug5IfOxeSnEgWInzwJqcRAaZMxbc-AWJLhZnuqAV4SzHFRpHpyeOw2vjFndTAa0U1-hd6qT3FIxTRTR_mD_noxxpyxaeXq9ClgRHOAfPo0AzKeSeOwb36hft1bOC8CY7sEZYwz3_qvZ0YCRI94T1SHct4QTRJfalQz14fi3oV6QJ2-8bN2zqKpxv_KlwtX6oL1_D4JTgAljOMiXPemA45Ezo_i_Rfu0ajV7NPuLSqoF6CccgDJnkZKlVp3jNj_r2Vcl4N3rTIi_Gq0k2hngVumUtudiPnIbNZaEs3YEi26jhvP32rn87HWjuA5W3fzJibvcFH0aDMHFlZP9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متد مستر دی‌ان‌اس که توی WhiteDNS ازش استفاده می‌کنیم، مبتنی بر DNS و برای شرایطی که گوگل هم قطع هستش. لطفا انتظارتون رو ازش بالا نبرید در حد دانلود و پینگ پایین و...
بهش به چشم برادر ارتقا یافته‌ی dnstt نگاه کنید. که نیازی نیست در به در دنبال تک تک ریزالور بگردید واسش.
و یک متد اضطراری هستش هرچی نباشه. شاید بهترین کارت و برگ برنده‌ی اضطراری ما باشه، اما همچنان اضطراریه.
برای شرایط الآن، شاید Goose یا Skirk یا Mhr برای شما بهتر جواب بده. به این دقت کنید لطفا. Dns برای خاموشیِ مطلقه.
پینگ و سرعتش نوسان داره، اما مقابل خاموشی‌ای که هفته‌ی اول جنگ تجربه کردیم؟
بهشته عملا.</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/MatinSenPaii/3349" target="_blank">📅 18:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3347">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pJO6ymom2bmcQC6564vrU9sUsV4BGfK8oNRXXDqxuIQoYIuIoSjHzjEHv3aiZFt7oDwWe8PFNbYAZCjAl_X4JYGAhq8CxP2Whgz_0St8GHSU8rAn3eCd3fKugqmuvf7cKb3ITt0mE69Mftv_A7_h1bb_eSCY4uKoZ5T3T3L9KDB9UHfUg2s4x3Z7PZJ3xFIF7666_n0p0HLRia62BoDIdxH4-O4xpwXjDw62bFeScDjWwoBOMyu--GkCa-6sFHnAf5jh7GOw7qj_rJisgpLKRY9tgk1CQS8fK4iq75-4K3xvLuBnOohtujz3Twk5C67Qtt_nQ-HRwh1p_66G0bkYXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YeH_wfPIhGcWD4AU9o1cF667GfYOdtm_LnTtBmN1QQ2zgVcEVFST6wKc8A-voUyagB255OiIIddKjzlY_SveqERbbnRLU9oODLxOOmzD_FiqFBlXHaqCwM2AcczzvSw7frVmObGtj2CBT_wlO8emb2QAR6F72kMdPnXC-yoJrRMMaZbmAbpdRKOJQzbJUkrjcL_V6XQykedj1gv9rgHxQoqaRT9zbWTL4NN6SP2PwSGc4sW0hl6Ze_kvzRfDYDxSKG2e1aPhk_EZbcxKR9m5H5wb84gcZxdOPjrEwpXoEVNgwagppJYlE4qYLE1jROCmvnYMkd78Odslg0x2yEdsRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حدودا ۳۰ به ۷۰ انگار وصله توی یه سری مناطق
هم همراه اول شنیدم هم ایرانسل</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/MatinSenPaii/3347" target="_blank">📅 18:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3346">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">V3-Spoof-Configs-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">7.6 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3346" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لیست جدید 40 تایی کانفیگ‌های ویژه‌ی متد SNI-Spoof که از سرتاسر تلگرام جمع‌آوری شده و همه هم پینگ میدن</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/MatinSenPaii/3346" target="_blank">📅 18:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3345">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ببینید همراه اول میتونید وصل بشید؟
{
"LISTEN_HOST": "
127.0.0.1
",
"LISTEN_PORT": 40443,
"CONNECT_IP": "
85.9.112.219
",
"CONNECT_PORT": 443,
"FAKE_SNI": "
www.hcaptcha.com
"
}</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/MatinSenPaii/3345" target="_blank">📅 18:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3343">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pWHQCkzumW7sGLNtAphfwgcLsWYRU8TCIrCwC4KrU74HZq6lzBiFtlvl-CAkXbnIZ5YN1Ge6CmJYcG0pamvo-kLGA7Xi4E3Kn1DDMAm7ZU-7gBuElarNaHOKjEi_cWqsaAYMZZQ180fQ3O9TQKb7ROe44tjZr7dGGkBJTlJ13zB8wn1QgBz2AF-XGNmfRcczPwQwH0yeONbQbbsZV8oJVLuj_TERuGXvxW3QXOfype6wXVR_JZIj3_UqP5LM9qDWwB0AQ0vzirQqyCxJfACGOychoREsmZ5OB3p4BBahK1PTdNiLQx_VEqzTiHh8IXmzoolrp_FqzF5D_w93mtd06g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سایت خوب برای خرید سرور با رمز ارز بهتون معرفی میکنم که قیمتش حدودا فکر کنم 4 دلار بیفته با کارمزد و اینها، و میگم که چه شکلی با صرافی‌ها کار کنید و از طریق چه ارزی بخرید.
منتها نکته‌ی مهم اینه که تصور شما اشتباهه از بسته بودن دیجیتال اوشن.
دوست من الان همه چیز بسته‌ست. همه چیز
و اگر چیزی باز بود که دیگه از DNS استفاده نمیکردیم.
پس بله، شما اگر VPS بیکار داشته باشید، میتونید این رو ستاپ کنید. دوستان خارج از کشور هم میتونن واستون ستاپ کنن طبق آموزش اگر که حوصله کنن. هرچند برای تعداد بالای 255 تا، قوی‌ترین سرور هم جوابگو نیست که خب این رو هم مجددا توضیح میدم که چه کار کنید. فلگ شدن دامنه هم توسط کلودفلر و هم توسط DPI ایران رو هم همینطور</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/MatinSenPaii/3343" target="_blank">📅 16:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3342">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oGUVwWNwBCHSq5vkxbaNoMBg1toz0Ri54_HACvP56rOWP-xQBlcT5Y8NSiFxK3Ks8osO-Ug7fVhA0odVwIGo49JG30LHwnhtMoSBZKr8_D_DsVXOfVD0rCtWI6S5tuqPExW2QUAXFg9PaBgThDnn_8LI6aGst3IglkojxiSjArjycBbPFrkHGM-KnVsuL2SKIUZo6KTYKv6-0q9qTkup0JO1lNEGp0R-hbHP58KizR2uQnsQetGsVJFvcYs2AMHAnUtAmiOO2fEYt4XL_EM3DMEq9A-mnaU0L_gb2ofdCLER07WtDeQWEeLpTay1C9oTu1PIZFItx1iW6BerloSQXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصلا آموزش "برای" سرور شخصی هستش. و برای ios هم تنظیمات به همین شکله چیز متفاوتی نداره. خودم آیفونی ندارم که بشه روش یاد داد متاسفانه اما طبق آموزش پیش برید، همین مسیره</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/MatinSenPaii/3342" target="_blank">📅 16:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3341">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tgspx6i4EkbCvRIEiTKkvwzhlO4IKdu3Llr_LjpsHIh8IcI9dTJtqfxIWYbDmSjCW3TQKz67r6YCUMPhuRHfppqYPYoEP_rFHNvk72cz6BC-KMqPKt21zCCKk-o7uDWdPloWsZF5FKqNgMubcq65iyUEBcRqYW_MNmVNCvvsKyAvTpdwIN4q21MaF9qgxytwkPjsllXFOBFBsRVIAODrPfNh8Ss7ooV4RdodLinNOZh4NMpekflWrwpRh7d6TJCZSu543KEcg82ebHFyB5V4tr5mBXs6P00Lfbzi9JN_rDLKjdXA-KNgCYyqeN05NHAs1xjil1gB3MMWEfzv1P_4DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ترفند جذب مخاطب نیست واقعا:)) بلکه هیجان خودم از متدیه که به شدت خفنه و میتونه ما رو نجات بده توی شرایط خاموشی مطلق
خیلیا پرسیدن که چطوری داری این سرعت رو میگیری؟ مگه میشه اصلا؟
بله میشه و توی ویدئویی  که تا شب می‌ذارمش 2-3 تا علتی که باعث میشده شما سرعت خوبی نگیرید و کندی تجربه کنید رو بهتون میگم</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/MatinSenPaii/3341" target="_blank">📅 16:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3340">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ebddd60447.mp4?token=Cb06nKMjjopLb7p4iEKpwB3O0UF7FVYTUuNeAMqU6mav7_pl-bAAU4rfPkqEGNcEhKaGDAj7b9t9prNfBFcKpl5jEw0g4B-zNB-d5pGxfV1tkapGQBx8jfZXTPrAa0RsYitoXDSuxJwIRqRH8hus_I6bayugKBu8bwWQeUUDLw6l0oLtFcpQgCwxlcO1tfwRY1S79wds_llVi6zE0lIbwPmWFOKpHqXV5Zex2gaciaeXwVMPI2mPSpw-_32DQ5efs3czw6dZFW2-Dgwaol4Vzj4xJAnnJ2Hi7Qe7COqm716BGyImFPd-btrbErcPXoB8uQyStzqWq8egnqI0G1oUgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ebddd60447.mp4?token=Cb06nKMjjopLb7p4iEKpwB3O0UF7FVYTUuNeAMqU6mav7_pl-bAAU4rfPkqEGNcEhKaGDAj7b9t9prNfBFcKpl5jEw0g4B-zNB-d5pGxfV1tkapGQBx8jfZXTPrAa0RsYitoXDSuxJwIRqRH8hus_I6bayugKBu8bwWQeUUDLw6l0oLtFcpQgCwxlcO1tfwRY1S79wds_llVi6zE0lIbwPmWFOKpHqXV5Zex2gaciaeXwVMPI2mPSpw-_32DQ5efs3czw6dZFW2-Dgwaol4Vzj4xJAnnJ2Hi7Qe7COqm716BGyImFPd-btrbErcPXoB8uQyStzqWq8egnqI0G1oUgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حقیقتا به نظرم سرعت Master+White برای شرایطی که جنگ بود و هیچ چیزی جز DNS و کانفیگ گیگی خدا تومن کار نمیکرد، مقابل مابقی روش‌های DNS مثل Dnstt و slipstream خیلی خیلی بهتره. کما اینکه نیازی نیست در به در دنبال ریزالور بگردید به اون صورت. نیاز به اسکن و... هم که ندارید</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/MatinSenPaii/3340" target="_blank">📅 16:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3339">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LpLNrgmidcuJQkw6bUAVBM-L3Pf09FIUgQomn64aeq7GnyvHNmpVDziqKE93GeCM4Y4RidcZNd5xhV3fbEOJuSQsoaH9cMITrplZIzt2QYt3l57Hjn4N2HYntqdxbHvzih4kVZdINgHn7HWCHytgOWEvUHAR0XkYE4i_nxeNHg7sbHRFrCq5ILAy0wKvG3yQCLGkHuAeKkmh5flAzsC0AqzUIlAN2uugU-QkWzAC-CmCJJ94YRop1-i8xdcx2aWbkxzhvFll2nxYdY9t1wHnDQC2sD0fU1Qy-HDP-7Wc6ddzimibNFYjkUBPSLppnyN5Dd0qGIiTBR94buObxJJCnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نزدیک به یک ساعته وصلم، کلا 100 مگ رفته
اینم برای اونایی که از ورژنای قدیمی میترسیدن که یهو دو دقیقه 200 مگ میرفت</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/MatinSenPaii/3339" target="_blank">📅 15:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3338">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">از MHR و Goose relay واقعا لذت‌بخش تره</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/MatinSenPaii/3338" target="_blank">📅 15:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3337">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">این عکس‌ها و پست و همه چیز رو هم دارم الان با همین متد ارسال میکنم</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/MatinSenPaii/3337" target="_blank">📅 15:37 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3336">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خب دوستان، باید بهتون بگم که WhiteDNS روی سرور شخصی خداست.   با MasterDNS ستاپ کردم. که خیلی خفن تر از Storm بهم پرفرمنس داد تمام تنظیماتش رو هم ویدئو میگیرم و بهتون یاد میدم. به همراه یه لیست 6 هزارتایی ریزالور که جمع‌آوری کردم  به شدت ساده‌ست و بچه‌های تیم…</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/MatinSenPaii/3336" target="_blank">📅 15:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3334">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hi-wfsrAasZgfgPPxMTSiOnKSSKlcrexo8nLbUcSzfePYrYZejFoMN2PV73pzM8wXalRLnqYs-HJqC1uSCnVJ6TzUPGOojiC1kPZkUgrkG7qCFUX1suCPFKVU7psJJ2smg8z6PcW92GIBLJWHy_1V8bsNVNDJPNoQvghWLlucdcph0GQxYnl5ioGdycr-coTmadsFJuvutQOkRO9oeLVnsOpG-Svl2_zSTKXH9iudmafJktz4dAhyzmY0iCrVAk_vk0XgMwF6TD9bM_xLKUCiN16gq6jiSZLz1eGx2cWYvAneSZwtrSOLRJ8moA7guHms_5N-hxb7bOrtw-JpflaiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mBf1E5EuDJzQIdbtndSA3UxTDiopXMxqZU3BW3Bplhz7qOOLsJG6oPoluU9DhVOW2oRyC6OX9IeWaUdKnJK9l1ZmPK5QvCaj93Ki1lEPI3RrAiE98r4KOFQMsmnyqMHSVhcm6EZC71x5-lPB7D9UFGxM71IgN5p_akfrQVxslrFFCgV0NGr3JItS-tfaA14kqtkFe-fkNnmK5fv1nQqOKKQzRW55xyZdHlEVtKgcfYLpbTu8itakjSEb3VCamZshgWlsifiKiy0Lmj03E-RNzavoyr8Jrn-o-w0Te2VhWarXegKK2jdU3psaUR0jP5wx8BeZ3upxFZyyOlODxFMZtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب دوستان، باید بهتون بگم که WhiteDNS روی سرور شخصی خداست.
با MasterDNS ستاپ کردم. که خیلی خفن تر از Storm بهم پرفرمنس داد
تمام تنظیماتش رو هم ویدئو میگیرم و بهتون یاد میدم. به همراه یه لیست 6 هزارتایی ریزالور که جمع‌آوری کردم
به شدت ساده‌ست و بچه‌های تیم در تلاش هستن ساده‌ترش هم بکنن واستون
سرعت دانلود تقریبا 500 کیلوبایت بر ثانیه. بیشتر هم میشه بسته به نت و ریزالور
اینستا راحت باز میکنه
توییتر همه چی به راحتی لود میشه
و مصرف حجم مثل ورژن‌های قبل اصلا بالا نیست</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/MatinSenPaii/3334" target="_blank">📅 15:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3333">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">آموزش Goose Relay رو می‌تونید از اینجا ببینید: https://www.youtube.com/watch?v=tzjVg4O6dVs  چیزی که دیدم، روی اینترنت‌های متفاوت از بد تا خیلی عالی جوابگو بوده</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/MatinSenPaii/3333" target="_blank">📅 15:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3332">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">آموزش Goose Relay رو می‌تونید از اینجا ببینید:
https://www.youtube.com/watch?v=tzjVg4O6dVs
چیزی که دیدم، روی اینترنت‌های متفاوت از بد تا خیلی عالی جوابگو بوده</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/MatinSenPaii/3332" target="_blank">📅 15:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3331">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3331" target="_blank">📅 13:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3330">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IGiRQ3v2uClBf1QI6Mpdkya_GKYhVtsFHVZoK9U0ZcD9TOGRnez_pNWg2Wz6p2LR3RUv1p6WnzRi2-rQx4lY2TPO9MgmKQ6_Fmn5aOie8PzJNRX6mnWG0YA5UG4TqHFo0ljq8ujPYerAHUozDZNi0n4MpnfLXCFRDg9TMfjs-8oZOxbhbE0GLZDvqnPk1D7wIErLDhPcJNMm8YkPcQMrplUaSpZwmDKEstgHrqN7DoODm2xNquIHg7UvXnBXXHZPDyfEehPOwvomCLcm0L3g0amaNFMSp_cjGDHUF3GFgYw5eLhz5YxDabg3jNsq8AUu1ZWq4clfEmKANaR3SdhgWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک سری از دوستان روی مخابرات و اینترنت‌های خونگی دارن با SNI-Spoof وصل میشن مجددا. زیاد دیدم از صبح  hcaptcha.com  46.38.137.156 81.12.32.136  امتحانش ضرری نداره</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/MatinSenPaii/3330" target="_blank">📅 11:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3329">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ojGEJYg2dVpkuuHg0lOh-B4qU5rqIRmSVN3dfqj1oziNWH4xXKUdLv42xBW1tQ8keY0GRHf7lyo5sJqaP83wWFoPcmeT67hF9hZXXbZQRbfRdtFf3QNC5hXzRaCCQO1eIdtDlmMdW2R8ofEUpUq8G2F18B9oYVbCQKm-8nUNO5I0xQ2jQdfX6opzs5pgUutbvkxoNuDQDjK5iasY2TY5loTBT5WaJRgpWwTVnhZi3tyleYDjdGEzF_JBrhW0_AJTaWZfNQgtbj_E7Coj6fc7-Cf0zRt9xFwPmsfbi3OrfuUA0S4j0E0MU87aA6VGkJid66CEihDxNxJlvo84EfaAAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر خاطرتون باشه دی‌ماه حدودا دو هفته میگفتن فردا وصل میشه، این هفته وصل میشه، پس‌فردا وصل میشه، آخرشم تک و توک روی یه سری اینترنتای خاص آیپی‌های کلودفلر رو باز کردن و بعدش هم من Paqet رو یاد دادم و ادامه‌ی ماجرا
برای همین خیلی دل نبندید به این صحبتای صد من یه غاز</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/MatinSenPaii/3329" target="_blank">📅 11:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3328">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مجددا آموزش share کردن اینترنت از شیر و خورشید بر روی تمامی دستگاه ها(باید به یه اینترنت وصل باشن)</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/MatinSenPaii/3328" target="_blank">📅 11:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3327">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K9pPTs1-27eWi4uib3Gkx1VvU_zSKXwF4YAhV5WAV6urs-NaayZgYTxTuEgM8APUrZKAuo7epwfnTdHM7w2fz2ojlIfIgAinhtdrQbkj4XDIOaCqvsC80SYVh5tsjQxHWsKpJrlUss1mtV9o87w4bZwzoA-TvS5ucmaS1WMlhT-AejLO2idfA-wbWFsQEDPtk5_pBfvoRkcR4A8DS87fOo5heLf5f4JAkMJdLCWWrEsUbM3e4URW-fIjxvXK6oNt2kiSWmCeibIge8x5sS3LTpweHCqrRpsI_JEHGb8yUueYk1ted8gC-7IzpGKY6-KmMflQ-_PclHZtm4XUSIaqoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک سری از دوستان روی مخابرات و اینترنت‌های خونگی دارن با SNI-Spoof وصل میشن مجددا. زیاد دیدم از صبح  hcaptcha.com  46.38.137.156 81.12.32.136  امتحانش ضرری نداره</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/MatinSenPaii/3327" target="_blank">📅 11:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3326">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یک سری از دوستان روی مخابرات و اینترنت‌های خونگی دارن با SNI-Spoof وصل میشن مجددا. زیاد دیدم از صبح
hcaptcha.com
46.38.137.156
81.12.32.136
امتحانش ضرری نداره</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/MatinSenPaii/3326" target="_blank">📅 11:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3325">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">150 مگابایت همراه اول مصرف کردم با VPN، بسته‌ی اینترنتم نزدیک به 1 گیگ مصرف شد
چه خبره؟؟؟ ضریب زدین روی نت بین‌الملل یا آب قاطیشه؟!</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/MatinSenPaii/3325" target="_blank">📅 11:10 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3324">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZjIufLQzcuRbP-ju3jdCcHVDPaf385eY90RR9wNjxgmnuYooH9enFMjI4j9CKVaYMh0nXjlyE6B4KC34iq0EzMhbIVDZ9nmD-NcaeUpRjj5cR5UgSVjQkrjcdZAuGt01-GzhE0CQ2UgVN2TI9iQG3SZFaISxMJpmMrK6jJQNwqwchVgJb_XzY5wcuYcT80YxZb3SRGc0URorEVLDJ73JE8AYW68iZAX5KBpU2gR0KJu0xVgbVn3lerQZ3SpQc0aoK6nc6D7lGdYCPnc1SWq_TajtYUISUj2YeHeMlQ218iE2T17B0IQg0LOOnyvCKykcw1vGbreN_Mh05gYDcnjhZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
استفاده از نانو بنانا و Veo گوگل برای تولید تصویر و ویدئو با هوش مصنوعی، رایگان و با اینترنت ملی:
⚡️
پیش‌نیاز: ابتدا متد رایگان و کم دردسر MITM( https://t.me/MatinSenPaii/3151 ) رو برای خودتون ستاپ کنید.  1- سپس وارد وبسایت vids.google.com بشید.
❗️
نکته‌ی…</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/MatinSenPaii/3324" target="_blank">📅 10:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3321">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hqKvWeAtTglAZvaUazAwCj2ZTqJcNRblOLwaJZFQWvnWu4gfB97ZVYvwJLm7Pxits161L8A8lrM_FXMKaKlPbrHyeT8TA_wPbFrWAtMihVC-BH2fPMR7z2JW4A2IJh7YsKwFzPJylqJPBmThWk6BgeYXs2r6mAz4EQxMeB1QbNkMoxhJUg6jKL2TPl43qrRGJxxHoAPPuP3Fga4H6C39Zwo5VT5oaEgoEwAjWdCJH-KxbexGWAaLuLbGQkrDi6zcKXW9qcP2gZ2IWHDkTDvAM1BOC0wo0VKLSiVW-ymUHkje3EPRbP5q9TzseD6yltvMxwd11A5G6m6mDG9LTaGjug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ajENmVKLT6QvTRMGJA1eYiMjvh8QNH50udXaXwzId8q1STsjWPZBUsPV4tgSjgT8ADtZ2aEbuES7UB7IDR_41UNCBI_xle4VNz9B4vcUoocQdJgMSYZkma6lngWaOBfQa1CFImeYWUG2RsyMbMERMBOAAcRHGMEnPru3GEzN72JrV3wc6NvsbIxvg-uNUva_qKGJvnJ3bu7lmm4bOf5XfoereQfJfKUBGR0ohiQ-FmmqcJIreDADBjLxd01n2Of2m1G8HqVtTiV7S8Ys3tznmCeVQdyaR6bJ6BkV1cWxZ3YLfdXIFKlP82GCItdgEp7_nee184b_iERDfJXw39LgXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ROAIoSMVpwMpufM-MFnWoZB9M30gSJ55FSc3tWCdqDFRPzmeUgM0Nf_0qdiD15PWp6UmXnrY_tQzPdSlVbe0IBTyaFTPez7wdjkd0Iz_J6upZOsCYySW7JC6UeGV2q7-SgizOvIoDfBB9F5XgwsCnrEiJfJLKvuDx_SNgqiw5I-5xUBu08r9eZW-lfQ2uhVt7xJtk45SqU-B1vBNa8z8AN1TAuvA_YPM-5i7pw9q4nSpm9CZpHZj7OPw4Hs0f9zelBCWA9JdmOjs1VX2MVnQuDuGozf58U4oxym_lZcLO56ASCBva7zeQGbXUwG6aS5LjAggQCcs625J6EXLrmCe7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">☠️
استفاده از نانو بنانا و Veo گوگل برای تولید تصویر و ویدئو با هوش مصنوعی، رایگان و با اینترنت ملی:
⚡️
پیش‌نیاز: ابتدا متد رایگان و کم دردسر MITM(
https://t.me/MatinSenPaii/3151
) رو برای خودتون ستاپ کنید.
1- سپس وارد وبسایت
vids.google.com
بشید.
❗️
نکته‌ی مهم: اگر با گوشی وارد می‌شید حتما روی Desktop Mode بذارید تا لود بشه.
2- برای تصویر از قسمت image استفاده کنید.
3- برای ویدئو از قسمت Veo استفاده کنید.
4- اگر برای ساخت ویدئو با سقف روزانه مواجه شدید از اکانت‌های دیگه‌ی جمیلتون استفاده کنید.
❗️
نکته: در صورتی که در بار اول تصویر و یا ویدیو جنریتش تموم شد و چیزی نمایش نداد مجدد صفحه رو رفرش کنید و مجدد پرامپت وارد کنید و مجدد جنریت کنید، بعدش درست میشه و نمایش میده.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/MatinSenPaii/3321" target="_blank">📅 10:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3320">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">☠️
(اندروید و ویندوز) رفع تحریم سرویس‌های گوگل از جمله میت، جیمیل و درایو بر روی تمامی اینترنت‌ها به صورت نامحدود  این ویدئو، مقدمه‌ی اون روشیه که برای یوتوب گفتم و ویدئوی اون هم پشت این ضبط میکنم و قرار میدم خدمتتون.  لینک داخلی ویدئو: https://up.theazizi…</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/MatinSenPaii/3320" target="_blank">📅 09:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3318">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAzizi’s Warm Corner((AZIZI)⚡️)</strong></div>
<div class="tg-text">دوستان پرسیدید که روی
آپ موز
زیاد اگر آپلود کنیم چی میشه و ممکنه سرور کم بیاری و این حرفا
باید بگم که نه موردی نیست اونقدری سرور دانلود ها جا دارن که مشکلی پیش نیاد راحت باشید فقط مشکل دانلود شروع نشدن روی سرور لبه 5 دست من نیست دست آسیاتکه و خب 2 شبه میخوان درستش کنن والا دیگه نمیدونم کی قراره پیگیری کنن</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/MatinSenPaii/3318" target="_blank">📅 09:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3317">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سیمکارتی که خیلی شنیدم ازش جواب بگیرن بدون هیچ تنظیمات خاصی، سامانتل بوده تا الان طبق گزارش بچه‌ها
به علاوه رایتل و ایرانسل بهتر از همراه و شاتل بودن</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/MatinSenPaii/3317" target="_blank">📅 09:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3316">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یک سری از دوستان هم گفتن برای اینکه روی همراه اول و ایرانسل وصل بشه، باید از بخش About Phone, Status, Ip address آیپی رو ببینید و برای همراه اول باید با 29 شروع بشه، برای ایرانسل با 26 و باید انقدر بزنید روی هواپیما و بردارید تا روی این عدد بیفته ابتدای آیپی.…</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/MatinSenPaii/3316" target="_blank">📅 07:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3315">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">آیپی ارسالی شیر و خورشید، رایتل:
142.54.178.211
5.144.129.174
80.191.243.226
2.16.53.50
79.175.169.59
95.38.201.199
5.160.13.85
2.23.170.80
193.148.67.117
2.16.53.11</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/MatinSenPaii/3315" target="_blank">📅 07:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3314">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کلا وضعیت اتصال به شیر و خورشید خیلی بهتر شد از دیشب تا به الآن. خیلیها رو دیدم حتی بدون آیپی وصل شدن، کسایی که یک بار هم واسشون وصل نشده بود.
با زمان‌های متفاوت
برای یکی ۵ ثانیه‌ای، برای یکی ده دقیقه‌ای</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/MatinSenPaii/3314" target="_blank">📅 07:19 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3312">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">☠️
دانلود از یوتوب و Torrent با اینترنت ملی، به صورت نامحدود!(پارت2)  توجه: ابتدا باید قسمت اول این ویدئو(https://t.me/MatinSenPaii/3151) رو دیده باشید.  لینک داخلی: به زودی قرار میگیرد
⚡️
لینک پروژه عزیزی: https://github.com/TheGreatAzizi/AzuDL-GC2GD (با استار…</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/MatinSenPaii/3312" target="_blank">📅 03:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3310">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAzizi’s Warm Corner((AZIZI)⚡️)</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vNwfM0VyjYCXlFwFj-N2Y4TqUh5v9e-VxratbMQO3PUL8ZuIR3Lj7fzYREwKfetEgQAksQItBorNfpZPYE0WHu0R1u2jM0Jmb5WdYtpusqLFKt_5IpOTSgA1tQ1awbPf8xCzN30bJvWESqzBmmdxAadwPaqTujVe2QmnPrPtFym_ZJX20G32sqXn2_5fhPA3L8V2EOYWDGg7zGdhbs2S8zUKMw5CjrTRvWJVBLjmVpyye4wLz3TprbPhVsxYRaTzrpVsFxLLBmLJGsBenNa1k1gPkcBX4zT7hyOxdFhFifOYP_er9j6pgJ_1f0Fflt9ELccUoAUhFCY18yh9dViy2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rXquiMThEFg1jf-sKIMZgoitsVY_I4rsUJblPSzyvOMV2yLRVGwdv4_GuLYiF9yyKnUMRAqoP0iVmspq0reQ94xl4RRI5BvBVGI8CtfgikAe9R4PHrY66669zyTa54IAooFniQF3yzgDMv7QrgeBbL6uRi_ardPKtEeIGP_FrBiJUPmjBkozgtWvsGRrWxUKOgDbhnm_wZvcu0PdAWidL7SqUifqvKulAfC8Sts00NaYveAh7s7ZI6vn7tVZkcBIgohmCaqQkSYeGKdOnvh-GYLnWwPRL2GqUKeG02TDyjPUFZuFgAqMKdDJooHJ0f3029uGMCDLY8HJRzWZOU1k2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آپ موز
🍌
یک آپلودسنتر سریع، ساده و امن برای اشتراک‌گذاری فایل!
📌
با آپ موز می‌توانید فایل‌های خود را آپلود کنید، لینک دانلود اختصاصی دریافت کنید و در صورت نیاز برای فایل‌ها رمز عبور قرار دهید.
✔️
از امکانات آپ موز:
➕
آپلود فایل با رابط کاربری ساده و سریع
➕
امکان رمزگذاری روی فایل‌ها
➕
دانلود با ترافیک داخلی (نیم‌بها)
➕
دریافت فایل از نزدیک‌ترین سرور در کشور به شما (تهران، اصفهان، مشهد، تبریز، شیراز)
❗️
آپ موز با هدف ارائه یک تجربه سریع، امن و سبک برای آپلود و اشتراک‌گذاری فایل طراحی شده است.
🗣️
پ.ن: احتمال خطا و مشکلات پیرامون لینک دریافتی به علت تازه اجرا شدن پروژه و همچنین اختلالات پیرامون شبکه لبه آسیاتک بالاست!
برای کاهش رخداد خطا های احتمالی به صورت zip و یا rar آپلود کنید.
👀
توسعه و برنامه‌نویسی توسط
theazizi.ir
با مشارکت
MatinSenPai
لینک پروژه:
🍷
🌐
https://up.theazizi.ir
🗣
@luluch_code
🏠
theazizi.ir</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/MatinSenPaii/3310" target="_blank">📅 01:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3308">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یک سری از دوستان هم گفتن برای اینکه روی همراه اول و ایرانسل وصل بشه، باید از بخش About Phone, Status, Ip address آیپی رو ببینید و برای همراه اول باید با 29 شروع بشه، برای ایرانسل با 26 و باید انقدر بزنید روی هواپیما و بردارید تا روی این عدد بیفته ابتدای آیپی.…</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/MatinSenPaii/3308" target="_blank">📅 01:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3307">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یک سری از دوستان هم گفتن برای اینکه روی همراه اول و ایرانسل وصل بشه، باید از بخش About Phone, Status, Ip address آیپی رو ببینید و برای همراه اول باید با 29 شروع بشه، برای ایرانسل با 26
و باید انقدر بزنید روی هواپیما و بردارید تا روی این عدد بیفته ابتدای آیپی. من خودم حقیقتا ۱۵-۲۰ بار گذاشتم نشد اعصابم نکشید. شما چک کنید محض اطمینان</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/MatinSenPaii/3307" target="_blank">📅 01:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3306">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/thrcjVSYVuDZ_aME4i8fKSepoDjLMa0opwX01M5QvmoLzx2SEtMxbpaI-T7RkiPg2v7sPz8DNWLJ7ECf3X-C6ZfCc3i7K-I1owxfPcUzHfp0Bm1dAkp2n2ctvLQWTA8WmRhjPCmhWztG8dY3fX5KVY9o6TN-8OPbEqzhM5GakdWivJSoZCPyozBAKc-M5Qecb6Huu6K1_R6j89glRRdm9kQ4xEaCp7wkP0Nf1LNxV4DmUJAGkjCDwZ4udXNJMqFF0hf9ZBXA0v_UbYmfE8RK8I6lEr-olRdKbuXmZSNKxeDDLPq3Ojmlnn93O4coYOCpHyLRiUn7st_-YHfwoGqNJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">والله مع‌الصابرون
😂
😂
😂
اگر گوشی بی‌کار دارید، با آیپی‌هایی که بالا گذاشتم تست کنید و Beast mode رو هم روشن کنید و بذارید بمونه.</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/MatinSenPaii/3306" target="_blank">📅 01:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3304">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uF7f2V7bd1RGNcAiIH3ZqN8Z1CINHIo4wDIqD9bD0C6ST1PXApHxBBhHjSd4zJulfad14g7Stpxuv1bo-K4j-7ShyO-5Do4hs_iYpz2h7hza0OHKbd2MhT-9ZjMHZ7QF94gwO_JGuXVQR8GuV5Sm6JmDh1Nv8eqBarBxS-WqDpjwhznv2vktj0dieYTijN85h7AY3kzzhyVsF1eQJzESH-W74FARWJgESY-agWKNhKIHpQ2wc-jZHQQXQWenOm8fu2EUa0vPSXmEdKkwzFVPkVZ3K6BGg8n1gXzjNAS7jGvSEgiac_N2-syuixjoca6j6Vg13H24kyhe4GUF-ZR0Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RilZEQMAQJTYXFGDVxZBpE5O0iEbvCeZpryGn6zhM1gIKDFE2ItBuIBVDmkDcmyQeZ69b6Gb5lpq6q6pXRIHsBDVfaiXoahe8rEFNMXLLefIysX1xkUgAEhSU9hfX7VXUDjpV23yEnxQK34cEsW5JUVWpi97SvkljJYrRK4rUHQfybcR_X-rweEOr4NGrZ0bfjcMA7iPTH9Bkuw9x23lHnZUgHxXYz_XwyeR15lZ5ahxR3KGg31_svGRbnE4XxiqEnoMgOUmifBdFfdjkJOUj6PN3e9XmY_WQnMW0qwsfz2V64I2AIPjez_4Ln_KgdwZ7TJ_MwdUdLd_lhM2zP8OIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آیپی ارسالی برای شیر و خورشید: اقا سلام ایرانسل شیر و خورشید وصلم الان ۵ دقیقه زمان میخواد 5.160.13.85 2.16.53.11 2.16.53.50 167.82.48.223 2.16.221.37 167.82.48.223 151.101.192.223 2.16.19.136 172.237.127.6 2.21.2.104 185.200.232.43 2.23.168.7 2.23.169.111…</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/MatinSenPaii/3304" target="_blank">📅 23:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3301">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eZMUgXWTJtRexbrAC-OicIJ-VSM6IKsxPBt3Pi2KhSl5AXaj1R-B4o95RiiyIFyN7lBdhelCC-XdeDeTLyC_TM5NCO2tVOyT3t-IEps0Ex6j68tQAAe4hh8KjWAKgAV8Eu6rxcpgBkKvuQKX5nWqGT5EAslQLrUrEQnHEL_6XJkDHJ_dZq-hc9BFG2Ww_wnw3aaUf6MdjsGG8iKzsyy9-pipA9muQoaWgMhYaweHpoyYwaeEma4Ar4_Nsi3iTFW7rksoSedZ0aPLDdWzFEZ_bvgleQslXWenOGfSFXgiqV9NwwWBcOurIvtiWmfJJ2fDtzv7QZLbczxcNF7OaxmndA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TfU5PZE5pC1Z3x1pqLvkjbRYTliUx4B1uMgRCiOtdRyu2tXYrn5to6_ZhfsaRgdss6zEsnl3pPwUk4nahVjHCgBC_9OmhSL3v_tA3iJw9TOzsYdy3HfoY9M02SWkmI3SGf5u0CCRf7NOmBuW5dLvmmoi_sRRKt_x5TfvMsclQX931Z6vONxRcoDdDpDwXj8OIsK4SNCrDxx4qwsyaSNG-3zuuUMJZFX196vCyZ8yakbkW64xNkc3nTw8s2S9f3aXD-_kPr_2Vjk0ozozuVsjt5a5Y4Mn6PJfMV77Lit4mv_5n-JePQZnzjUdXbwXE18yu1AI3ACEGeQsu-v_GnRPVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c0wdsdiH4BcuasWuMTyXUHCHsWSksgE39DYP2KBO2KCFntg4HSDCXgEQLy4bc2DC-YfkjmWLZuTKJWDPVdZjtpsRGFouS60MrigqiE1648C8iVcekPTQOjZgMXANORuByuB67uxty0HHb1Fqr8vi2eDs9V15tj2tNrvC_wJ6rqrNTAxWtD9HpoPztDl-itQcYJ46itLvwG88Z61APuys8TGIzjuQb6suwazX_UPMFesr1uST4clbpNASOgqXNgZzJWKTDS_zUUkLg83-MnyWifz9-BkbpZ2iaYsMfg4MAJdI74SQKOZTjuDCrIKd18n2NmdcQFigV4JvSn5dYI3rwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚠️
گزارش اختلال:
یکی از دوستان روی ایرانسل دوتا از آیپی‌های BPB اش روی پورت 443 شروع کرده به کار کردن.
محض اطمینان یه پینگ بگیرید.
آموزش ساختنش رو اینجا دادم:
https://t.me/MatinSenPaii/1965
منتها اگر نداشتید از قبل، دست نگه دارید و وقتتون رو الکی سر این نذارید ببینیم اختلاله یا شروع شده به وصل شدن</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/MatinSenPaii/3301" target="_blank">📅 23:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3300">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">☠️
(اندروید و ویندوز) رفع تحریم سرویس‌های گوگل از جمله میت، جیمیل و درایو بر روی تمامی اینترنت‌ها به صورت نامحدود  این ویدئو، مقدمه‌ی اون روشیه که برای یوتوب گفتم و ویدئوی اون هم پشت این ضبط میکنم و قرار میدم خدمتتون.  لینک داخلی ویدئو: https://up.theazizi…</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/MatinSenPaii/3300" target="_blank">📅 23:07 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3299">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آیپی ارسالی برای شیر و خورشید:
اقا سلام ایرانسل شیر و خورشید وصلم الان ۵ دقیقه زمان میخواد
5.160.13.85
2.16.53.11
2.16.53.50
167.82.48.223
2.16.221.37
167.82.48.223
151.101.192.223
2.16.19.136
172.237.127.6
2.21.2.104
185.200.232.43
2.23.168.7
2.23.169.111
151.101.128.223
185.200.232.25
2.23.169.105
185.200.232.24
2.23.169.105
2.16.53.50
2.16.53.11
185.200.232.50
185.200.232.42
95.101.133.42
151.101.128.223
2.23.168.254
2.16.19.136
2.23.168.213
2.23.168.144
151.101.192.223
2.23.169.12
2.23.168.174
185.200.232.11
2.23.168.254
2.23.169.111
2.23.168.174
2.23.168.213
2.23.168.213
2.23.168.174
185.200.232.43
185.200.232.43
2.23.168.144
2.23.169.42
2.23.168.144
185.200.232.43
104.103.65.5
2.23.168.7
172.234.159.58
172.234.159.58
172.234.159.58
172.234.199.15
172.234.199.15
172.234.199.15
184.84.221.34
2.23.41.22
﻿</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/MatinSenPaii/3299" target="_blank">📅 22:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3298">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اتصال به اینترنت آزاد با کمک گوگل درایو!
😮
🔥
آموزش متد جدید اسکیرک!
📣
برای این متد نیاز دارید به یه سرور لینوکسی ضعیف خارج کشور!
📹
لینک ویدیوی آموزشی روی یوتیوب
🔗
لینک ویدیوی‌ آموزشی از زیرساخت داخلی  (مدت زمان یک روز)(اختصاصی)
🔗
لینک ویدیوی آموزشی از…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/MatinSenPaii/3298" target="_blank">📅 20:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3297">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">چیزی که می‌تونم بگم به اندازه‌ی قطعی اینترنت روی اعصاب و روان من اثر گذاشته، اختلال GPS هست
سه بار توی شهرهای مختلف گم شدم توی جاده تا الان</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/MatinSenPaii/3297" target="_blank">📅 19:28 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3296">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAzizi’s Warm Corner((AZIZI)⚡️)</strong></div>
<div class="tg-text">اتصال به اینترنت آزاد با کمک گوگل درایو!
😮
🔥
آموزش متد جدید اسکیرک!
📣
برای این متد نیاز دارید به یه سرور لینوکسی ضعیف خارج کشور!
📹
لینک ویدیوی آموزشی روی یوتیوب
🔗
لینک ویدیوی‌ آموزشی از زیرساخت داخلی
(مدت زمان یک روز)(اختصاصی)
🔗
لینک ویدیوی آموزشی از زیرساخت داخلی دوم
(مدت زمان یک روز)
📱
گیت‌هاب پروژه اسکیرک
💳
حمایت مالی از من
🗣
اینترنت برای همه، یا هیچ‌کس!
🗣
@luluch_code
🏠
theazizi.ir</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/MatinSenPaii/3296" target="_blank">📅 18:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3295">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کلا باگ پنل سنایی بود. از اون طرف باگ سایفون هم بود
متد ترکیبی یه روز کار کرد، تا دو روز بعدش هممون سر کار بودیم حتی با چند تا از بزرگان من صحبت می‌کردم نمی‌تونستیم بفهمیم چه خبر شده</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/MatinSenPaii/3295" target="_blank">📅 15:58 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3294">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/abafd93842.webm?token=hkLChrRRVOdl6WLQlDNRp2FhhQGRe7RyHoqDEdUdOZR4xln8W64lx8H6PAwfhGpZElmXbcA76Q_x8_Du9zGT2uRgBBUuXB9FoFochmB-wSzaFP6NmWlBilkPHwLxKXihkRnRNTHMrrV9XxBDluaKwkfjRqfQeUHuWhnm6chiKc6HFL2bPXlAwJmBxJFf3Qe57XlbleVuSlVY3uE0PvZMA196RXwi_YN2DF3TpByQ8aHmh2hmB3x-0VBRIL-cbBAIR5vwgyS2OiGAxJWvKLRKfT1rHXV5bDfNawJs7UMFz3L4NO6sGMjCh_CDJuTxSCqcw3OEBpV61kd31HyOazQq6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/abafd93842.webm?token=hkLChrRRVOdl6WLQlDNRp2FhhQGRe7RyHoqDEdUdOZR4xln8W64lx8H6PAwfhGpZElmXbcA76Q_x8_Du9zGT2uRgBBUuXB9FoFochmB-wSzaFP6NmWlBilkPHwLxKXihkRnRNTHMrrV9XxBDluaKwkfjRqfQeUHuWhnm6chiKc6HFL2bPXlAwJmBxJFf3Qe57XlbleVuSlVY3uE0PvZMA196RXwi_YN2DF3TpByQ8aHmh2hmB3x-0VBRIL-cbBAIR5vwgyS2OiGAxJWvKLRKfT1rHXV5bDfNawJs7UMFz3L4NO6sGMjCh_CDJuTxSCqcw3OEBpV61kd31HyOazQq6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/MatinSenPaii/3294" target="_blank">📅 15:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3293">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A3WkGVhdYrdnAsIbNyHBukyhcEw9UXShVX9ymHu8QkOm-6vHvcWsv6FZIHgAn9R0uhkk3lgDZkkAwFPIwferlAJvXEA7BnmZqtbfJV9wavIeof17LqhKys6bzXYCIgQhvSzk3dz79cmx5q3ifnBGE7AyH9zPEfJog3vTcf9OZvThNlMGSPjElaSbM44sUGKab6Cye5XBNsPQWuDaCw7EYf8PPUX7MWad_Sb54c3JMwvTY-nh6qzvx-oULrLq1lt-WxL0MzTGqQqeYjg5fQEiMBVXZYxgPZvvavK_8-2XUneLWBSHuaMoLcg7AwdYJ0iYvefJ5-2g1J4jOPIw0D6aBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان عزیز، همونطور که عزیزانی که از زمان ترکیب با سایفون(اواخر اسفند) یادشون هست، این کار به ظاهر جادویی(!) باعث نمیشه از حجم کانفیگ جدیده مصرف بشه. بلکه همچنان از حجم کانفیگ پولیتون داره استفاده میشه. خواهشا همچین مطلب اشتباهی رو نشر ندید</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/MatinSenPaii/3293" target="_blank">📅 15:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3292">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KxW2MKHYNjTuxitgk8v7Xf1Tm2j2iZYtote_GwzwQcIGfEl1tY6tQCfl2p1SrTElr_vOJ1ZAL5nZ1Vyu_Wt1v_tAgOcDv0XSQOqe6VdnMNwMlHagTAyyygyYaQ1X3vE1TxomsVMzzWw8AKg5oOmg_7hJdEOZkNXfXQVIhk0gD5EHeB9ebskjTIETIHvjuC3TX4_u5EOLULzwuQfw3RXA-BcJoT2nVB_Xr5hB3xIzqaFKXJYpa23RyIAKQ84RsE2ya2WWfFgWKYPIb4AhsQsTtmxUGwqMeYROckwEbqkY4oNrcC8mhJlno6KaIEKjkR3YqjRnJjkx6OAnvwV7wrc78g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان عزیز، همونطور که عزیزانی که از زمان ترکیب با سایفون(اواخر اسفند) یادشون هست، این کار
به ظاهر جادویی
(!) باعث نمیشه از حجم کانفیگ جدیده مصرف بشه. بلکه همچنان از حجم کانفیگ پولیتون داره استفاده میشه.
خواهشا همچین مطلب اشتباهی رو نشر ندید</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/MatinSenPaii/3292" target="_blank">📅 15:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3291">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یه سری تک و توک هنوز بهم میگن که اسپوف وصله اما خب ۹۹ درصد بسته شده. روی سرورهای ایرانتون تست بگیرید
✅</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/MatinSenPaii/3291" target="_blank">📅 14:40 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3290">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gVIB-jNqdf8AXe5xLiRIfUEmO_OdyLC7JlEHgBqERYnXpzl7eL1JX9C7034hAEjJR_Kiuhb98PbK_zHQzSBa844sQaecXXpCUfBAn259gxy8rIIIDuYN4vaPoDzzSE2KlqMSdZRhsmmyMHggAAGNqwi8tJoMqo26qX1iIp8H_I0dnPlUotNYgPWLvSi2MPBAY-2fv40jbFc4W50Rs7nGZunxH4w7HLBlCHk2LWJBu7qUnqvDr8kjhWGGQF9_gV30XFUNK2By4WuNdtvoh71k9cfrrxbTZ2ISVESjzfbCWnnFJy1A8Hze5p8u17PqxGUCNMOFNKGjsrfNTTDdasdjlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر آیپی تمیز کلودفلر داشته باشید، ۱- آدمای عادی(مثل من) می‌تونید با
https://youtu.be/svYBcv4bSzo
به صورت رایگان پنل ادج بسازید، و جای address هرکدوم از کانفیگا، اگر آیپی تمیزتون رو بذارید کار میکنه.
۲- کسایی که پنل دارید می‌تونید یه inbound وب سوکت(WS) یا Xhttp بسازید با هاست و sni روی دامنه‌ای که به آیپیتون point کنه و پروکسی کلودفلرش روشن باشه، و جای address، آیپی تمیزتون رو بذارید. این شکلی باید کار کنه</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/MatinSenPaii/3290" target="_blank">📅 14:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3289">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b6YIuaBt1QB3oxT8cQE9QGbDWdM718DxygzwvkQ1Fk4gRSvcFL8_z9R93Qkw14foje_6dX7C2iKWUVvl0c76ItOwGIgHZYeQyC03eRqudXvvgvNoogON97HflDDKB8SPgho1cFbT279qBYMZRKh5eUBa4LDG4vS4BCYFaFELgK3XgUbHm69EuvZ_ZoEOj04mAeMewsuybz0vgy3kXdN8D6e765Bvrdl883wCzPz14rG4hmTLTnCcKIUuPbF3wPq0CUrLEqnMG5bdM2RikSdz5q3pe53KE64Q8PldtSA-VLUyN9GsYCYai-BPgrEDut4NsxZnuIVTTwcFOYtEB_t5tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری تک و توک هنوز بهم میگن که اسپوف وصله اما خب ۹۹ درصد بسته شده.
روی سرورهای ایرانتون تست بگیرید
✅</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/MatinSenPaii/3289" target="_blank">📅 11:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3288">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EYPR20_EaPMEAf8RLnVVaHBErf0Tn_R4zeIiBkeKxnbI7wboxbu29GXkoB0wsBjHhmWlVvQXuXIyjar5msltOw5JStNjWHJSXfULKvA7LbqrfHdBoNwhUFlAtENXgjhl2gnRjJimBlpw7LHuysXXdORiXeEDD3fHItN5AgZFuKKwaxQr08TDzGzqcSp38B6SC60tGuiREywBpEYKCFn0703ktkCimP6QtPfZkMKzPOo7FH563IYQrGOuaEiFJFHEQXpumcMkJI0gsr_mFyxSoVX2sMJbfxFJapVPp8BOysydbVuBn0Bsby9IePtR1wSkvbpPxkU2EkXZ1Lk74P4-Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چنین بود، افسانه‌ی شیر و خورشید
🫠</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/MatinSenPaii/3288" target="_blank">📅 23:08 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3287">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvToMp1ic8KcHJ-ZZNFcROBkjDrIVZUO98Xgyv05qV8hpLkxb_uuQWbJw20FJ3TVhoCStBOZRncW8dij2FDMiKHT2LSwDNia60mtX0gFkw1eI5I7sxgNVH55We4dPkzIA4GQpo3v551LzI4fF1LFZ6NkdiiK82vyDeyENs-e12um-mvlBfUZXL21xNGY5bdnI5lqU0RpoSWvBagZtiyodVa8wtDIOjD38e50a9Qg1jpDAsNpCfxA81QcO2o6brswqe4HiccyoeGcgU72TOToWvvNCAknT6-uavxrX2SQXqeM7SGNEspQI9Aof0OpCje7kac3-mCzA7Zi5XcM9KTEQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داخل گروه اصلی تاپیکی ساختیم به اسم «اولین شروع» که یک توضیح کامل از وایت دی ان اس هستش + یک سری رکورد صدا که آموزش و نحوه استفاده کلی از اپلیکیشن رو آموزش میده.
لینک گروه
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/MatinSenPaii/3287" target="_blank">📅 22:47 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3286">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نکته‌ی مهم راجب سرورهای StormDNS و MasterDNS که روی WhiteDNS استفاده می‌کنیم:
هر سرور و پورت 53، فقط ظرفیت 255 کانکشن رو داره و دامنه برای تعداد بالاتر باید لودبالانس(توزیع بار) بشه.
خلاصه اینکه اگر با سرورهای رایگان سرعت نسبتا پایینی رو تجربه می‌کنید، به خاطر تعداد بالای کانکشن روی اون سرور هستش. اگر سرور شخصی خودتون رو راه‌اندازی کنید(که آموزشش رو ضبط می‌کنم واستون) به هیچ وجه سرعت پایینی نخواهید داشت</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/MatinSenPaii/3286" target="_blank">📅 19:44 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3285">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نیاز داشتم روی هاست X ایرانی که اسمشو نمی‌برم یه سرویس بخرم
می‌گه دامنه می‌خواد
رفتم دامنه گرفتم
میگه فقط دامنه .ir قبوله
حالا رفتم از خودش دامنه گرفتم
میگه احراز هویت سطح 3 نداری توی ایرنیک
رفتم ایرنیک میگه سامانه هدا نصب کن داخلش احراز کن
سامانه هدا نصب کردم عکس قیافه الان منو با عکس ۱۵ سالگیم که روی کارت ملیم هست می‌خواد تطبیق بده و نمیتونه
میرم میبینم نوشته شماره پشتیبانی ۱۵۱۰ هست. حالا هرچی زنگ میزنیم هیچکس جواب نمیده
و دیدم هرچی دامین داشتم هم پریده نمیتونم تمدید کنم با اینکه پولشو ازم گرفتن
رسما دیوونه خونست</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/MatinSenPaii/3285" target="_blank">📅 19:08 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3284">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ورژن جدید WhiteDNS Desktop واقعا خفنه. الانم با سرور رایگان وصلم هر سؤالی هم دارید توی کانال تیم جواب داده شده: @WhiteDNS</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/MatinSenPaii/3284" target="_blank">📅 16:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3282">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PNH4PqSuXdNk1IwTkPHXVaxrCGh0JOyfj_VgHejL3nQObVxn1ghytpbhorlNbrU6n15zEzSEB-XsTY5gYiTaYpgq2EjNRavrq5vihe5A32hGaGFfWKYwgyHiDs2LrhC-Ms8jZJ87tXBWJtqC3uZseWyk0pB_7Vnd_83ryqfwFcgRvmwS9ZdEQDQIul_tmXYxwRTMuWx6dU2DQdB_54v9V2J2vwHj7qNqWHwOzZ0WeGn4sJrN2ajPpIy1dRzjThyyJSUEzge0_Blfi3o4gugz7RvAexKGxfbCMZtMlJoKQTzCGK-vIJY2U6HvOelEf229qoGdlbx6xnPH5WsVmGnjhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IADLsc6GPxBBrUOfybFjitmbsTijmm3YDQXYtGnJqI8YFUKYaDF3KxPFDx3wj9POAiy8qaoQTDPtkbyn0y1CHCMexDAeWnvl9RT9YoF1kAWlgSwWCqjK9f8g-DmQ8bq59W7RG4n6LF7hxN98_tMjH9PHjGIVUPMZOcB-sTE8FEs5Ap8tD9nJ5efj203vEn2WE0zdplrI5mqPjvgcW5Et1-qmOuaxQ04dhoCsE2bIb0nkOmFRL2D6dLCoFWseUU4yz_8_bRURCWbkDSHs8-ZRt_ZPcQt0OnCPcuFtPUT4urwfi0kSaAAWdIyYf3jBiLBPy6JOaRPgPNdD1Lfxe4wXcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ورژن جدید WhiteDNS Desktop واقعا خفنه. الانم با سرور رایگان وصلم
هر سؤالی هم دارید توی کانال تیم جواب داده شده:
@WhiteDNS</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/MatinSenPaii/3282" target="_blank">📅 16:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3281">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اگر رایتل دارید و کسب کار ندارید با این حال اس ام اس پرو اومده جدی نگیریدش چون اول ازتون پول میگیرن، بسته فعال میشه و بعد از دوروز بسته قطع میشه با این بهانه که شما صاحب کسب و کار نیستید و پیامک اشتباهی اومده.
پولتونم برنمیگردونن.
این عین دیالوگی بود که با کارمند رایتل داشتم
✍️
شیوان</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/MatinSenPaii/3281" target="_blank">📅 16:08 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3280">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bf8snLATBsGYHK_ZtcrUwegnFNoGZcAaaggGF2G1MQpxFxTIxT-kyXI95su9vJt9nN0t1R4NBR82rUaco4636Z1850xrmlFFlyg5R4lZnhs9KGpvRLHpsYweikA98lbXIaik2lL7PY-9xVP_R6OwnecJ2k6f4ZMn7MDKYUeJad_0XQpJrgQktLW9TskFSUC1962uNFn39CQDsAXB3cW2cHRUi0pnbLTKl6MFkSfnhYNlzrluHfokoonMsdONMCb3KAqPBoO_eZ6mb2_pE8vjxLnTlPe_pMASCSLCLjVRVf8PkjOwc7AlXVxOrJCW3lvDhhRd1qBBonfW53sN9O8ytQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چنل‌های این چنینی هم دنبال گرفتن ویو هستن و مدام در حال نشر دادن اطلاعات غلطن. به حرفشون توجه نکنید.
الکی برگشته میگه حتما قبل از اتصال به یه اپلیکیشن IP های اپ رو چک کنید
😂
انگار مردم متخصص شبکه‌ان بشینن Wireshark بزنن پکت‌های شبکه رو رصد کنن. جمع کنید مسخره بازیهاتون رو
"از ابزارهای معتبر استفاده کنید"
چشم الان میرم اینترنت پرو میخرم جناب</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/MatinSenPaii/3280" target="_blank">📅 15:38 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3279">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SoWkEiYYhdaGfpuCuWWef8gLIwP8ky35Ac9BNFt2GZdu00r3OLj7JjqrMI3Dm0QdvQR203CA3btD63mveNDmGWVNzk4QLrTSb_arG-747lBpkvywC9609g40GeqyR1nEiTDL5XgDJ9nImpDU8-bat1M49xfUH6w0b3SKy9au29mo5dnvELjKVUr7TavESoJGLsKWPnH5S1bQPPaKQaTGogDkFUnKSHPdG_MGjXGDbDBocvYDXP6dl0GItZc_GcGnqLZpxTqz9Bf4GSEOkaCt0u_1jjQPSBzB3VL60bcJlmFQV64tRD4w7IbPRTJ8p36LKp9z_ByVm-LVFjmFkOXlAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها پروپاگاندای حکومته طبیعتا. یه مدتی هم ریخته بودن میگفتن SNI Spoofing امن نیست یه مدت هم میگفتن Npv امن نیست و...
کلا ما از این چیزا زیاد دیدیم. توجه نکنید.
اگر به من اعتماد دارید، حرف من رو گوش کنید و با خیال راحت استفاده کنید.</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/MatinSenPaii/3279" target="_blank">📅 15:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3278">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ju9qwa-WeSe4bkzfbzJAO2TjpP1p7jytODr9iO2YlrSFZWKyTCiYjvvzSgTLR2j4cqvZARNOvZWKB_yftss5tO64l8T6EziwGkS-SBeVy-JhWeK407gSMdzHLEbh6g6V4N4gcL9kZNrVHoW-iJ71Jg4wRcEb5F7V1OV93wNXHXQg_wnQJShzIGf4UEDvfTGA0ol7DfM5mLJRH8lUmsslSmwTPafNgbpU5uw_jPur7RNDYOKtMRwtWgdXCTBn8ppx0-bqtCsbDjH-TH6dBaxt_3vLzmK05sNpN3pSsHWyDiT3AY7_-5tAvoqd_ShYWp22aRzP9xXibCXlDJXEcnkOQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیر و خورشید توسط یکی از افراد مورد اعتماد بنده نوشته شده و کدهاش هم به صورت متن‌باز، روی گیتهاب هست و میتونید برید مطالعه کنید:
https://github.com/shirokhorshid/shirokhorshid-android
این اپ هیچ چیز ناامنی نداره و یه فورک از سایفون هستش. اگر این اپ ناامن باشه، طبیعتا یعنی سایفون ناامنه. که خب درست نیست</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/MatinSenPaii/3278" target="_blank">📅 15:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3277">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hEr7RnkN3RNpvcAxohIZBeWFxHbuLM1vME3rMJRVLv_QcSvgxu6liqon7Cg6Poml-OFD9aZJGQPh-KWIzd04YtPnZOcUdtSF9VxQByYjBgMHhm5iV0TcFhRbK1MMkegsBxkrhxMFrAh1zC61MjeenLe7ezIKDaUSBLLb1JEVYer5Vpfu7nGct_hhK9sPagw6xqdbIm9D5EWRG8FisUDe34GQUrI-9CIbZStjhsofbsnGRJtkmqVE_Q2b097Twp2dTB6AbhPOKCcLCqpWCOzvx2DbhBILnguvq3AN0mFHkv1oZidKggKjuF6Vtls5Fd5RK9uUcQW2fOJz6O2CVAYUuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتباطات زیرساخت و سیستم DPI تمام ترافیک شما رو رصد میکنه. در این مقیاس شما نمیتونی بدون رانت و پارتی سروری پیدا کنی که بشه این حجم ترافیک از روش رد کرد. متد خاصی هم پیدا کنی، درجا میفهمن سرورتو به یک طریقی وصل کردی به خارج. کلا تانل زدن و سرور خریدن رو از سرتون بیرون کنید و با WhiteDNS و MHR و Goose و Skirk و مابقی متدهای رایگان وصل بشید. به محض اینکه بشه تانل زد یا روش کم هزینه‌ای پیدا بشه من بهتون آموزش میدم</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/MatinSenPaii/3277" target="_blank">📅 14:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3276">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اکثر وی‌پی‌ان فروش‌هایی که شما می‌بینید عمده میخرن به عنوان واسطه و مجدد به شما میفروشن. خودشون کاره‌ای نیستن. منظور من کسایی بودش که مستقیم سرورشون رو وایت می‌کنن از بالا و ترابایت ترابایت ترافیک رد می‌کنن</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/MatinSenPaii/3276" target="_blank">📅 14:21 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3275">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">Matin SenPai
pinned «
متدهایی که در حال حاضر متصل هستن:  برای وقتی که گوگل وصله:  متد دانلود از یوتوب و رفع تحریم سرویس‌های گوگل پارت 1: https://t.me/MatinSenPaii/3151 پارت 2:  https://t.me/MatinSenPaii/3230   MHR-CFW: https://youtu.be/L3lJZrAqqUQ?si=Iby4iSumzgAXj_GG  MHRV-RUST:…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3275" target="_blank">📅 13:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3274">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/MatinSenPaii/3274" target="_blank">📅 13:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3271">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tRyvLMEzn-Iy4DPKu5dNtwG6dqt2wGIn1EnWM-TqRB-QG8kz1LjG35cIT3Yn5NRxm3a9O5ruhNcV8xel4Tu3EHkpq0jOCUUzsiX5wpnXdVDZfDgKKixvDJ7vXsmxZIOjzi6TD-tvx0YXz-oTXSx5G9ShKHuVabBGNgOg3IaENnOcVBiLiwXrjD5VMNP3rS5aAfLTE_wX1XVJXkEOZQoILZsh6ekcy4w5WYg3BnTn2ETDzcfH9IHUAvZCdFhUC5l-6lc7-cTKKrl4X4DREvvEol7ld3i6MzE6zSFY-YMbHhYlo6Ipj41Zdy_0zSE5NOfgMNnV1OYdiAGIetU0LLrTZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/g5XW-g-cs1nNikxqWilj5TfnV_QDekNTJ0fzK3hUB8N1VYk-pKzFfCbBXiG5-o1LDfXvHtMzNZ-U1sP3rdDz_p74HqIW-MvGmsQvNR0-AMAWiGQQKabYE3TgRtMEpuoYwVjDUfKxLHRMmypCmLRtC4zz0a74d66MFe9PU1MsuLNebdmEi_oCfI_ZjW8CxVPAwoTuDbBzxLw2lZgskXNwG9RH0lkDhf-PsvjXw8IxcUS-cU8y9AJT05W_VQe7Sd39eTbiKlblzDy7BDJixTSqGLKLBN7sk79jgvMDNqTSXwwPK4MX7gTqpLiHAaATAdy3-IHbU2gHeBDtn3FmDg9ONA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ksx4DhrdnYHb11Vy2EylQsHxnYfDXwBeoqJDYIyOmpcz6TcBTsbFmClNbC4005c_7D_hQ5rpMEem7VdpL-tIhKkEF-cSaqc3f3qj-IaSGxkLXMveijLMAqclllV3T0NxsFzfdsq_mC4giGyVxLRrHRliXrA_JSqSJlqQFddyMwE20aCXceRVL834mwFELvvuYbf-FFZREPb8wESkLHnaYxKarpTnHYpNnM3gci7vwDJYUMgF0zsvhWfOyFIkMPu5j0Pjs2xFSWlR1w8L964eJcS7ShvctoL6nQLu9mPe06H9HT1fSZEd8N1RzRcJO2vUHs5J3ZX6g6S3j1Q1WbIsEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دوستان mitivpn این SNI Spoofing رو توی ده دقیقه از کار انداخت که VPN خودش رو بفروشه. کارشو تموم کنید
🔴</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/MatinSenPaii/3271" target="_blank">📅 12:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3270">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کسانی که قبلاً کانفیگ می‌خریدن، الان ترجیح میدن دیگه نخرن. دلیلش هم تکراری شدن خبرهاست. دنبال کردن مجازی دیگه اون‌قدر براشون ارزش نداره که بخوان بابت هر گیگش خدا تومن پول بدن.
از اون طرف، کسایی هم که سیم‌کارت پرو گرفتن، خیلی‌هاشون توی کسب‌وکار خودشون موندن چون درسته اونها اینترنت دارن، ولی دیگه کسی نیست که بخواد تبلیغشون رو بخونه، تقریبا اون چرخه‌ای که باید بین محتوا، دیده شدن و فروش می‌چرخید، به بن بست خورده و کل سیستم رو از کار انداخته.
✍️
آمینواسید</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/MatinSenPaii/3270" target="_blank">📅 12:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3269">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dc90I21GGRl9mtQYXKE0AHNuLtgzkcHN1QYLqEYBFiEFwPra2TMMb_-A75V7OX0bpdmdog3PAur9UueiPGd_s37BsGBBxr4iAGioGJ-ht1JxLOxgs60nW_6Bm60ctN-advFgmC3za_Sjch7tV6yUQiZJ-ccZN3_6LG19_PsaBNY9WUvWtlMHP_gBpleUvACD1YEdIx3wHocbRtGu1vjTb2mV6vJCy-MZN_MWmKZZsTqyxP2dIt8c15_YVrVlcTkH1mCQ8w7KBEjVujViQkM5iy_PK8dcHCKG9zC5puWuKJZmO7QpaICxH-Z_i9a-chrzmcoEC309D8PZA2Osgz20yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقدر خرافات راجب شیر و خورشید شکل گرفت این یک هفته که فکر کنم کم کم یه فرقه‌ی جدید راه بیفته.
عزیزان تنها نکته‌ی مهم، اینه که چندتا از آیپی‌های CDN رو بذارید، و انقدر بزنید هواپیما و بردارید که روی Range شما باز بشه و بتونید متصل بشید به اپ.
اگر هم وصل میشه در حال حاضر، به هیچ وجه گوشی رو ری‌استارت نکنید یا حالت هواپیما نزنید</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/MatinSenPaii/3269" target="_blank">📅 12:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3268">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cD6fy7TMGa9CYvGMSIopAlbDYRXP9iDhJ_uBGFOM1mCDKJZnurd5AuNRWyvp3V7h0FqyIYUybHlfg7B3IkNXDvE-vMmkxxIPoD-ICeru4luNh7rQxre8yxCjfl_ZcmIXEQ6MrI6NpbpoAUoNUoYUgyiKfWAy6wLJoS09US3ZhV4gi_Y5RpxN2OiA_5LjHjHg_SPvQES392dTLW2a5SRRt0JWZwS21MT676QINQN-kyVNpDtvOy_BjjgSkDvNpKHQmE0byPHKJym_zJMIijtaJsONg5lQqTYH2Te4ZChN3bO_KXYImgOJqWZVCHeT92JTBsyXegBmH09Ze-xMexeE6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرنوشت Spoof</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/MatinSenPaii/3268" target="_blank">📅 12:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3267">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">☠️
آموزش ساخت متد MHR با گوشی + کاهش مصرف ریکوئست های گوگل
⚡️
لینک‌های داخلی جهت دانلود: https://t.me/MatinSenPaii/2969  لینک پروژه اصلی: https://github.com/therealaleph/MasterHttpRelayVPN-RUST
⭐️
توی این ویدئو بهتون یاد میدم که چطوری متد MHR رو صفر تا صد…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/MatinSenPaii/3267" target="_blank">📅 11:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3266">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یک سری از گروه‌های ارسال کانفیگ و کمک و اینهایی که از سرتاسر تلگرام دیدم و خب نمیدونم مال کی هستن اکثرا، می‌ذارم خدمتتون توی پست بعد</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/MatinSenPaii/3266" target="_blank">📅 11:05 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3265">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یک سری از گروه‌های ارسال کانفیگ و کمک و اینهایی که از سرتاسر تلگرام دیدم و خب نمیدونم مال کی هستن اکثرا، می‌ذارم خدمتتون توی پست بعد</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/MatinSenPaii/3265" target="_blank">📅 10:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3264">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">فقط چون علی جان تهدید کرد</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/MatinSenPaii/3264" target="_blank">📅 09:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3263">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RGpLXrLadhNMzUF6qogrZw7fnGi-j1SBbJPIBRPxTwiYO7v1OVouUgA4KSCJVwdse6lz2wkVPbVxcibaJTJ7YtWML6i6dDh1zfOycq-4A4Ka6ltphkZa7-LDJtu-OV2sz58IiTo_NbDVaiw2OpKxFVJ7EwJu8JRQWMDPD989z6PXJWV31HFCwUTEZ_v_C6XmZ9t0Y3Fn8IuXyWynA564-0bmhYbr7Sxusi0-wYWGnUDh_jCoNHE1GLdmTcZoIcj9kolx6a0PIwXxYASZDk1CaHxeZBKxz46e8aB5ENcwNKU9FswGgUJRFdggC3R1TvVIvYIqpokGh2nh8wxEszqvsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این کانال من نیست عزیزان من هم تبلیغش نمیکنم و تلگرام خودش اینها رو می‌ذاره. خواهش میکنم اسکم نشید</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/MatinSenPaii/3263" target="_blank">📅 09:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3262">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9f0b6810cc.mp4?token=YdfJcoz0LVGGEAVJLBnWEgETmMv61MbFqMsD3ubTTI5efUeE67drPtCgYnKt4M97u1fR_KxWdD_g7PqVgOfqQTwgrs5xdyxgdNLMdUA4MuKeokaIu1neILnA3fbA3De6ZuNPv8F-pLHF1fY2YfVnvZ78e74Dru52sMKDhAUCjHVWwXKh742bB8oJxqbYfK54QIQfp9Yrwy3utjYNOtdiyrWzydiJx6_0QNrcc-IblOdWvergUQwx1dUFCY3_7p3iySBA19lhp5i6AdJh_yV_bNpwNZ4ypEqN4gDuK9WL-u13RCxMJMAxTaQp5JQSrepscn5r2PZpj7jP1YYvf2NoEg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9f0b6810cc.mp4?token=YdfJcoz0LVGGEAVJLBnWEgETmMv61MbFqMsD3ubTTI5efUeE67drPtCgYnKt4M97u1fR_KxWdD_g7PqVgOfqQTwgrs5xdyxgdNLMdUA4MuKeokaIu1neILnA3fbA3De6ZuNPv8F-pLHF1fY2YfVnvZ78e74Dru52sMKDhAUCjHVWwXKh742bB8oJxqbYfK54QIQfp9Yrwy3utjYNOtdiyrWzydiJx6_0QNrcc-IblOdWvergUQwx1dUFCY3_7p3iySBA19lhp5i6AdJh_yV_bNpwNZ4ypEqN4gDuK9WL-u13RCxMJMAxTaQp5JQSrepscn5r2PZpj7jP1YYvf2NoEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط چون علی جان تهدید کرد</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/MatinSenPaii/3262" target="_blank">📅 09:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3261">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KMJB0-VU2jnDvjZ91UDv-w7KHha3bNOmcaY54urjEAqK1sLYpnQBRldxak5U6aPaz-tiVX6ejiVN0vX2ET6-oDrNOW3ZMeMWqn1bCDeW7vhRcWiOneH9cDQag2Koyqf0_xpg1gg6-Y3ly7YzXsp-v1rxNvJzQf4AqUh76ydBDDX_czncJ196QqNotCRfH-aDVG_BkgHQanwoESU5BlNnQFpcsHOPPENKQuuBmT0sLH8iAD3Ms5zelJ-hJyGPtj0_K-JeN_oZC7tt2cvN-dxcp7VlqQOb-iveeEyls7pAZKembKfkzb4XQfzKuf1MCraL_R1H7qddHAy2QWTQs10G8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/MatinSenPaii/3261" target="_blank">📅 09:14 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3259">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خبر بد اینکه hcaptcha.com رو بستن کلا.  خبر خوب اینکه مشخص شد متد هنوز در بسیاری از isp ها بسته نشده و صرفا کلودفلرو کلا قطعش میکنن یا میبرن پشت reverse-proxy.</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/MatinSenPaii/3259" target="_blank">📅 08:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3258">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">خبر بد اینکه
hcaptcha.com
رو بستن کلا.
خبر خوب اینکه مشخص شد متد هنوز در بسیاری از isp ها بسته نشده و صرفا کلودفلرو کلا قطعش میکنن یا میبرن پشت reverse-proxy.</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/MatinSenPaii/3258" target="_blank">📅 08:21 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3257">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">متدهایی که در حال حاضر متصل هستن:
برای وقتی که گوگل وصله:
متد دانلود از یوتوب و رفع تحریم سرویس‌های گوگل پارت 1:
https://t.me/MatinSenPaii/3151
پارت 2:
https://t.me/MatinSenPaii/3230
MHR-CFW:
https://youtu.be/L3lJZrAqqUQ?si=Iby4iSumzgAXj_GG
MHRV-RUST:
https://youtu.be/7YdJIJloIxY?si=WJgiFKDcCmISyDdB
شیر و خورشید همچنان وصلن با آیپی‌ها:
https://t.me/MatinSenPaii/3247
متد اسکریک که شبیه به گوگل درایوه اما اون نیست:
https://t.me/ShahabSL/9223
برای وقتی گوگل هم قطعه:
WhiteDNS(برپایه MasterDNS و Storm):
https://t.me/MatinSenPaii/3130?single
کلا دیگه سمت dnstt و اسلیپ نرید مقابل Master و Storm به شدت اذیت میکنن سر ریزالور</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/MatinSenPaii/3257" target="_blank">📅 07:54 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3256">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AL-EHU6MSJQejgZveHaHn9BZ880s5R7Wy59GRpJ3B0-yr7nbv1vWagbzwGKMvb7y_a8ScmFp4dFrNd642ATMvEfVIzg3niy-JYTrtprgb2oXcfXO8pDNQV5jivStiWZxYC6k76Bq7i1MVjb6kX0hbBfe971G_Ugglgt7vmsuEcPzbOy6iAKMp5uivncPo9yDV5kQiRWfPjAPlDFRkqgE9apas4etdceH1Ofv8JBGZVEqifnam8l-fs9kSvCJxrDH5Gi4Ujo0UpRKesrGdUlRb9OrnXOQuJGX2Su7K3QK7n8RovNFUFmyRFKKmBYdYFD59Y9TU8-r2q88bRSdP4tDfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیگه از شوخی گذشت
😑</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/MatinSenPaii/3256" target="_blank">📅 07:41 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3255">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">و اینکه دوستم عزیزی ران‌تایم‌های برنامه‌نویسی مثل پایتون و راست و گولنگ و  تمام نسخه‌های ادیتور VScode و Notepad++ رو گذاشته اینجا برای هر سیستم عاملی:
https://dlhub.465978.ir.cdn.ir</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/MatinSenPaii/3255" target="_blank">📅 00:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3254">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">☠️
دانلود از یوتوب و Torrent با اینترنت ملی، به صورت نامحدود!(پارت2)  توجه: ابتدا باید قسمت اول این ویدئو(https://t.me/MatinSenPaii/3151) رو دیده باشید.  لینک داخلی: به زودی قرار میگیرد
⚡️
لینک پروژه عزیزی: https://github.com/TheGreatAzizi/AzuDL-GC2GD (با استار…</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/MatinSenPaii/3254" target="_blank">📅 00:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3253">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">و اینکه اگر Spoof واستون وصله و نتتون اوکیه، حتما متدهای جایگزین رو ستاپ کنید واسه‌ی خودتون. از جمله:  برای وقتی گوگل وصله:   MHR-CFW: https://youtu.be/L3lJZrAqqUQ?si=Iby4iSumzgAXj_GG  MHRV-RUST: https://youtu.be/7YdJIJloIxY?si=WJgiFKDcCmISyDdB  برای وقتی…</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/MatinSenPaii/3253" target="_blank">📅 00:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3252">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afb36e0d0.mp4?token=B-Fu2rt0KQNN7nXrfM8hzFXG94to3pWfndiZlLK6f2DM8LI5oWsVpLcbkbRQhfvVf2FM0nAoArVc7NeLpKmBvUwoIoqgzS-TgRA-86jZPa7iXZYyHh4IJUymWvh7EquNkQvzDctV2TcHM1tBBK1FQXRSBu2E4mKMkhGbfMucWM2cpnHMY1tPyNFv1q0xq5n9PO1ahL5WxexRX1AetshAW-PelRjCHxDb_DXuPDf-xiGevl13tX095BqYGaknix66dmuSLPHtdWnGbNL74LizPNqoRN8zZHc1s_FU47-iVjOtT_YIzIMqAY6oJPjeHjlIIe_pDJvshJLoRbYJKyNAVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afb36e0d0.mp4?token=B-Fu2rt0KQNN7nXrfM8hzFXG94to3pWfndiZlLK6f2DM8LI5oWsVpLcbkbRQhfvVf2FM0nAoArVc7NeLpKmBvUwoIoqgzS-TgRA-86jZPa7iXZYyHh4IJUymWvh7EquNkQvzDctV2TcHM1tBBK1FQXRSBu2E4mKMkhGbfMucWM2cpnHMY1tPyNFv1q0xq5n9PO1ahL5WxexRX1AetshAW-PelRjCHxDb_DXuPDf-xiGevl13tX095BqYGaknix66dmuSLPHtdWnGbNL74LizPNqoRN8zZHc1s_FU47-iVjOtT_YIzIMqAY6oJPjeHjlIIe_pDJvshJLoRbYJKyNAVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/MatinSenPaii/3252" target="_blank">📅 23:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3251">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JMSlQjjkbaFf6oWGjMlPbFr5xYfhNXICMppa70YyxJycSYaC4Dn2k47In1kZr24dGg3HOlfGHiuxQe72m639y2XPctRkmFcQWUPA-Guq0Ac6VDqp-00O1ohi1lsV-pc8hO4IVEgkv39t0kkOA7cQ4_XrNiX5ZMMZmJJgf2NErGWb8zi-HHD6WkVMWQHPkOaIWATjilPWFWmZrl5Pevi7RFUO6-tlj4qmmGvsdbxCG8CKA0RhZI04c_izGwFaJfc1LFcHifunGwWgPtt_w_ojU0mTsKpnwGmWqzykd0_ksezCoCsdc13bJFDv_Rs7jpy7kqL4mIALtwgnzmBj3dMA2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محدود کردن دسترسی اینترنت به اپلیکیشن‌های خاص بر روی ویندوز
این زخم رو من وقتی خوردم که با کانفیگ گیگی ۷۰۰ تومن اوایل جنگ ویندوزم تصمیم گرفت خودش رو آپدیت کنه و من وقتی فهمیدم که خیلی دیر شده بود:))
از طریق اپلیکیشن TunnelX، می‌تونید انتخاب کنید که به چه مسیرهایی روی ویندوزتون اینترنت بدید
با پشتیبانی از:
- WireGuard
- V2Ray / Xray
- OpenVPN
- l2tp
- SOCKS / HTTP Proxy
از اینجا می‌تونید این نرم‌افزار متن‌باز رو دانلود کنید:
https://github.com/MaxiFan/TunnelX/releases/latest
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/MatinSenPaii/3251" target="_blank">📅 23:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3250">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">و اینکه اگر Spoof واستون وصله و نتتون اوکیه، حتما متدهای جایگزین رو ستاپ کنید واسه‌ی خودتون. از جمله:
برای وقتی گوگل وصله:
MHR-CFW:
https://youtu.be/L3lJZrAqqUQ?si=Iby4iSumzgAXj_GG
MHRV-RUST:
https://youtu.be/7YdJIJloIxY?si=WJgiFKDcCmISyDdB
برای وقتی گوگل هم قطعه:
WhiteDNS:
https://t.me/MatinSenPaii/3130?single
theFeed:
https://t.me/MatinSenPaii/3109</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/MatinSenPaii/3250" target="_blank">📅 21:36 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3249">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">این متد ناامن نیست دوستان، بلکه امنیتش کاملاً کنترل‌شده و لوکاله. شاید توضیحات من باعث شده که فکر کنید ناامنه، و نگرانی شما از کلمه‌ی «MITM» منطقیه، چون خب MITM حمله‌ایه که هکر وسط ارتباط می‌شینه و ترافیک رو می‌خونه و یا تغییر می‌ده. اما اینجا MITM داخل دستگاه خود ما و با سرتیفیکیت خود شما انجام می‌شه، نه توسط شخص ثالث.</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/MatinSenPaii/3249" target="_blank">📅 21:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3248">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y_sqmodx_MHImDXoZBjrnLHRBQ6LMDYcTcNEr8KNhtfyIEDCYghnJiUMN7YkQQthsj2mqAGBfdH2xNOZWe3Q77MmxCb4OIToXrsMqjHjB5rUkii78PbQTJAlvYPkrifITDnHq36zbxhWVnmhK3lvkl1AAa2zjwlUsPTud0yrD19b7hd3o0BV_rt7cYRQ1_e-4H03xkoOdljfSGNB04WG0xHYVURzHj_ChFXyiV_DI74E3kwXfTPZ6KjIf5be6rr5VXirN-UgJAPAGSIuvt82jn5a-WuPFiRumVKT_JowHG50MYCNw50hG2ud6DQ-LrPoaN32s7nc9nHReRIIcNIYEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">kharabam
:
[موقت]
شیروخورشید یا سایفون MahsaNG برید Connection Protocol رو بذارید رو Direct یا Normal تست کنید ببینید براتون وصل میشه یا نه.</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/MatinSenPaii/3248" target="_blank">📅 19:57 · 30 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
