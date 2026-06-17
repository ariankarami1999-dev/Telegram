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
<img src="https://cdn4.telesco.pe/file/kKowCpNPJWYoPs0AGJhnEIXmHNELLZlPiz0xaPkmljxdzBYOsJWZAQuSXVHvxEwxB9wKZYLUeSr0V9ZIsonXBhW96qZcUiQdWExkajDCU-GHlZjD2orpfmOLfXTJdd7Q1vQQetV_UDt2XTbHLVGOsPOCXSWPOhC77x028mFdEFnau39T8j5xtxiLJjAyL28nGMbZ5Pfv9S73fcFkl5UnfyZMYzoXLJob1uPLm9E_lU0uS986M23m6Ezn6icD0YSlf3nYCo_t9y4quvIx81VAm5c3WiaLR7DQ8NO9FyVCHNDNA4ksRSzHjEgS9HOOsy4djnDTRkiwxsypqA89N3MUaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 223K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 03:51:59</div>
<hr>

<div class="tg-post" id="msg-66334">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/news_hut/66334" target="_blank">📅 01:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66333">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/izX9t_nHwSuFKRcgpXxrV17WlcwJshmHTqzUN0IAPS6ndyEi2xJSF-RCt1zjennBqukmGeQbxvvNuLjBxnvBfkQ8hAVgOlHqX_Gk4Y6LhRmC83M5ZFsREJfmTVYVyZC-1PATCB4g1S6SvbqHQWk4lt8ElDkSjKYUL0QPlFVCAMl7nyNSRwOeh4npPRAfu91_wakTZ6D4ACm14gYcquyPXQLiPNBUCndGg6_9VSUr8UH7SOZ4mvrBQrxX88U85RwpjfeNiEWn5-pK4YDmyKPuBWj81sSgdjrnctc_1kyQCfW_Ua--md2LGdXSEb-p1zcXxcH_pyaybH_GBqVxlBH99w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/news_hut/66333" target="_blank">📅 01:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66331">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
به ادعای باراک راوید مفاد توافق ایران و آمریکا به شکل زیر است:
ایران، ایالات متحده و متحدانشان خصومت‌ها را متوقف خواهند کرد، از جمله در لبنان.
ایران تعهد خود را به عدم توسعه یا دستیابی به سلاح‌های هسته‌ای مجدداً تأکید می‌کند
ایالات متحده و ایران متعهد می‌شوند مسئله دفع ذخایر اورانیوم غنی‌شده ایران را حل کنند.
ایالات متحده و ایران درباره غنی‌سازی اورانیوم و نیازهای انرژی هسته‌ای غیرنظامی ایران گفتگو خواهند کرد.
ایران وضعیت موجود برنامه هسته‌ای خود را در طول مدت مذاکرات حفظ خواهد کرد.
ایالات متحده محاصره دریایی را برمی‌دارد، از تحمیل تحریم‌های جدید خودداری می‌کند و در طول مذاکرات حضور نظامی خود در منطقه را افزایش نخواهد داد.
ایران ترتیبات لازم را برای تضمین عبور ایمن کشتی‌های تجاری از تنگه هرمز، بدون هزینه، به مدت ۶۰ روز فراهم خواهد کرد.
ایالات متحده متعهد می‌شود دارایی‌های منجمد شده ایران را پس از اجرای تفاهم‌نامه در دسترس قرار دهد.
اگر توافق نهایی حاصل شود، ایالات متحده نیروهای خود را ظرف ۳۰ روز خارج کرده و تمام تحریم‌ها علیه ایران را لغو خواهد کرد
.
هر توافق نهایی شامل برنامه‌ای برای ایجاد صندوق ۳۰۰ میلیارد دلاری برای بازسازی ایران خواهد بود
ایالات متحده به ایران معافیت‌های موقتی تحریمی برای اجازه فروش نفت در دوره مذاکرات اعطا خواهد کرد
مذاکرات بین ایران و عمان با مشارکت کشورهای خلیج فارس برگزار خواهد شد تا ترتیبات مربوط به حمل و نقل و خدمات دریایی تعیین شود.
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/66331" target="_blank">📅 00:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66330">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9122af9759.mp4?token=DlCvA-Ppuoce8qQCp3mAihszzejvoZ5L6tU_i5Dv0oMOqukNMmshgybS5CRg3e3N_bN_4NnExe0V6eNfYrYXjIkbkxJUUeLo7CF6IYzABl8NpiPocg5eqhvko0No2hcEZL9aLgOj7b5EiGaP3XDZXSuewyY5vzfKopXwM_cNTCeKlyn_3m0-2h9OHVvTqHn-O75YoSIr4bYJCqlPu2W8PgVY1dc6GRv-JDX8RzkRl40swHLZLXlZhEE417mM59-kDmf7NqJz7k61mll_t3GhVkgSvl7HCKRTrHTVZmBHVdwOvWvB-PLEIJhekdJYyr9wE8-9Ab9m4kTvsvr7doK6O29Rt4Y3e5z7HuHBixQPYOFOHnzQrz_tj8wLvzY75LwRM2faCSwZvNIeqhRUOld6AV47Cb_dvXR6ocEXCgMszib-eKG1kyLGNPP5BsRCt43-YHO0uSOgq8D8QHWyFBqIEQKHgEEJnQSZsiEUHSiZIl0ueS2apzeajXQvFQSDvk3ZCShiXxahYfod0yYwS63JP74XktpKn4z7JWAYi0fuOjfHdpWL6_vaZsAOPrkRJvhvQVJhUYLleOyFlBHlXGUrcu_rrWVKk37aAp-LhRnn2EzVfxYauuC-Z1ArbJp3xV8xvn2vCFp2cp8gY1EG3YYDkYpHcJMpfM9mdT3RxA1XueQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9122af9759.mp4?token=DlCvA-Ppuoce8qQCp3mAihszzejvoZ5L6tU_i5Dv0oMOqukNMmshgybS5CRg3e3N_bN_4NnExe0V6eNfYrYXjIkbkxJUUeLo7CF6IYzABl8NpiPocg5eqhvko0No2hcEZL9aLgOj7b5EiGaP3XDZXSuewyY5vzfKopXwM_cNTCeKlyn_3m0-2h9OHVvTqHn-O75YoSIr4bYJCqlPu2W8PgVY1dc6GRv-JDX8RzkRl40swHLZLXlZhEE417mM59-kDmf7NqJz7k61mll_t3GhVkgSvl7HCKRTrHTVZmBHVdwOvWvB-PLEIJhekdJYyr9wE8-9Ab9m4kTvsvr7doK6O29Rt4Y3e5z7HuHBixQPYOFOHnzQrz_tj8wLvzY75LwRM2faCSwZvNIeqhRUOld6AV47Cb_dvXR6ocEXCgMszib-eKG1kyLGNPP5BsRCt43-YHO0uSOgq8D8QHWyFBqIEQKHgEEJnQSZsiEUHSiZIl0ueS2apzeajXQvFQSDvk3ZCShiXxahYfod0yYwS63JP74XktpKn4z7JWAYi0fuOjfHdpWL6_vaZsAOPrkRJvhvQVJhUYLleOyFlBHlXGUrcu_rrWVKk37aAp-LhRnn2EzVfxYauuC-Z1ArbJp3xV8xvn2vCFp2cp8gY1EG3YYDkYpHcJMpfM9mdT3RxA1XueQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❌
جی‌دی ونس درباره ایران:
🔻
ترامپ هیچ‌وقت نگفته که هدفش این است که رضا پهلوی را به عنوان رهبر جدید ایران منصوب کند. چیزی که او گفته این است که اگر مردم ایران بخواهند قیام کنند، عالی است. این کار خودشان است. این موضوع بین آنها و دولتشان است.
چیزی که ما می‌خواهیم، توقف برنامه هسته‌ای ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/66330" target="_blank">📅 00:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66329">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
جی‌دی ونس:
🔻
فرض کنید امارات متحده عربی که یکی از بهترین متحدان ما در منطقه است، بخواهد در یک نیروگاه هسته‌ای در ایران سرمایه‌گذاری کند. عملاً بدون اینکه ما بعضی از تحریم‌های موجود در سیستم مالی جهانی را برداریم، این کار ممکن نیست.
🔴
حالا سؤال این است: آیا اماراتی‌ها در ایران سرمایه‌گذاری می‌کنند؟ یا آمریکا اجازه می‌دهد اماراتی‌ها در ایران سرمایه‌گذاری کنند؟ نه.
🔴
برخی می‌گویند خب، شما به ایران پول می‌دهید. نه، نه، نه. ما می‌گوییم فقط اجازه می‌دهیم برخی از این کشورهای دیگر در بازسازی کشورشان سرمایه‌گذاری کنند و برای مردمشان رفاه ایجاد کنند. این چیز خوبی است، مگر نه؟
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/66329" target="_blank">📅 00:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66328">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/400d2a3a78.mp4?token=V6USDBApyFXCuHXhA3Jh-4EvC-nKpt8_8QW_zj-mtXQDoSDjxM1XORiq2XaREC9Rtz8LyhQBianLeQURAWfYjUv4x8iGwNUm6X0aXqzm_55CbQOLIJyJoC-psdbVTafvulCKSWIyIPHt8wrdj0hhaEORBH-wf8WzymKtHuwLqfqdOplPVMx7GVXEL72Gyc8-Wd0-WpQmoL69QupFVFa6-iPdgr38WPp56PqAHhWhWCrnmmyDXgy6mnXaO2ZLVbIiP1tDu-UDt76-6iTgle1cWqGTls0UAOJvuasi-45Q_B-UDU0qcAUij1yohDNNrbqNZRUwm2AdxH6GJvSvfHP1LYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/400d2a3a78.mp4?token=V6USDBApyFXCuHXhA3Jh-4EvC-nKpt8_8QW_zj-mtXQDoSDjxM1XORiq2XaREC9Rtz8LyhQBianLeQURAWfYjUv4x8iGwNUm6X0aXqzm_55CbQOLIJyJoC-psdbVTafvulCKSWIyIPHt8wrdj0hhaEORBH-wf8WzymKtHuwLqfqdOplPVMx7GVXEL72Gyc8-Wd0-WpQmoL69QupFVFa6-iPdgr38WPp56PqAHhWhWCrnmmyDXgy6mnXaO2ZLVbIiP1tDu-UDt76-6iTgle1cWqGTls0UAOJvuasi-45Q_B-UDU0qcAUij1yohDNNrbqNZRUwm2AdxH6GJvSvfHP1LYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🎙
جی‌دی ونس:
🔻
یک نفر گفت - یادم نیست کی - که این توافق مثل اجرای طرح مارشال وقتی نازی‌ها هنوز سر کار هستند، می‌ماند. این حرف از چند جهت غلط است.
🔴
اول اینکه طرح مارشال با پول مالیات مردم آمریکا انجام شد، اما اینجا قرار نیست پول آمریکا خرج شود.
🔴
دوم اینکه ما می‌گوییم فقط وقتی از مزایای این توافق بهره‌مند می‌شوید که رفتارتان را عوض کنید.
🔻
(البته کسی که این حرف را زد، سناتور لیندسی گراهام بود.)
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/66328" target="_blank">📅 00:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66327">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7276198054.mp4?token=twf-8c9Mk6exaHa-BXrCIhjXZuQ8Ghuylzs2D8dUyT-6VRlsswdsAKrEnuc21GDPCSF14OROyIkwx1G0Dxy_nXKME6OWsysPdXN8Oqo8_hxYYe19xDPmHykEvcIUnXSBt30IqNMwwt4UGjrnd3WN6Gvjt7ff49wxmcQZucSvZOW-_FVgTpQZIuJ-52EmpTiZMP153mhsP_G8Eh9eLcRU6ZM-4S3b_wZQ3iHGi4V3A5B_FJJwM2d-zbhaKldxBN1NI-w9w6M6kxH0L2lsH6UHwEHa0pAF7rhopHdULSC-WmKB93yt94OhdmeSp94ev5XEPAcFLFWIb8O3joQjZohe1xMwcRwmZMNKTIXtPQoirgelxVuZX86czn88_mJPqElj9tvdy74qsfhLm_TxUT64zSuV5n5qmvTgL9Cg6tmIuPeyh3X_RLObBsC_6WdViLyyiscs4M3UsuKqJRomZj0-6UqF_XqqwWEAJPV1u0x2J_RjeMIlV9FBUhKIkSCN0joc10HQsnL7DJyAm4AmKt0XjLqgovMwRamUWpA--WoZpT3Gs7ZUULekXqxqika19cMA2Hz6CXXe0zFGRM1OuBaGpF0iDR0eu26MqElGzic3LdyO8pkxNPE2p6MdhALQ9HomaibSgb89oSP5UUXhYr-Y0Xzb6uOCSoDAbIdiG0a3FSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7276198054.mp4?token=twf-8c9Mk6exaHa-BXrCIhjXZuQ8Ghuylzs2D8dUyT-6VRlsswdsAKrEnuc21GDPCSF14OROyIkwx1G0Dxy_nXKME6OWsysPdXN8Oqo8_hxYYe19xDPmHykEvcIUnXSBt30IqNMwwt4UGjrnd3WN6Gvjt7ff49wxmcQZucSvZOW-_FVgTpQZIuJ-52EmpTiZMP153mhsP_G8Eh9eLcRU6ZM-4S3b_wZQ3iHGi4V3A5B_FJJwM2d-zbhaKldxBN1NI-w9w6M6kxH0L2lsH6UHwEHa0pAF7rhopHdULSC-WmKB93yt94OhdmeSp94ev5XEPAcFLFWIb8O3joQjZohe1xMwcRwmZMNKTIXtPQoirgelxVuZX86czn88_mJPqElj9tvdy74qsfhLm_TxUT64zSuV5n5qmvTgL9Cg6tmIuPeyh3X_RLObBsC_6WdViLyyiscs4M3UsuKqJRomZj0-6UqF_XqqwWEAJPV1u0x2J_RjeMIlV9FBUhKIkSCN0joc10HQsnL7DJyAm4AmKt0XjLqgovMwRamUWpA--WoZpT3Gs7ZUULekXqxqika19cMA2Hz6CXXe0zFGRM1OuBaGpF0iDR0eu26MqElGzic3LdyO8pkxNPE2p6MdhALQ9HomaibSgb89oSP5UUXhYr-Y0Xzb6uOCSoDAbIdiG0a3FSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇱🇧
جی‌دی ونس
:
🔻
اگر ایران حزب‌الله را تامین مالی می‌کند، ما اجازه نخواهیم داد که مجموعه‌ای از دارایی‌های بلوکه شده به ایرانی‌ها منتقل شود
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/66327" target="_blank">📅 00:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66326">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8b2573c92.mp4?token=L5PJNXhgEX9qhvi_gmdaBDE7DNRGesKMEnN88scOHZ5L_KtLK9Z4_Yp5CipcR0jLOjn0NEZvMMeM1yJWcYVhmNSzn_nZm-r9pI7rcNafrwE0unZZaUmhuUxWmrvt0BP_iqbOacxk1ChBPPR3f_K3FOhhRdX_gGbRE0lTEkmPfN46T5ctn4y_t9NM6JzIWj9QKh2sqtUsG8W1EYqz6w8FfH1bMji1OxhrzVldOocieNmiTh0blNtX9Sq-SebCjL458GW4SPIWycDHekamVKjg548ViBaCi8OPWkzq-uDtX4wTjuIit2zAYJ3LKxk5yFHE50qTRnGr3LmzwPVd-r1THg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8b2573c92.mp4?token=L5PJNXhgEX9qhvi_gmdaBDE7DNRGesKMEnN88scOHZ5L_KtLK9Z4_Yp5CipcR0jLOjn0NEZvMMeM1yJWcYVhmNSzn_nZm-r9pI7rcNafrwE0unZZaUmhuUxWmrvt0BP_iqbOacxk1ChBPPR3f_K3FOhhRdX_gGbRE0lTEkmPfN46T5ctn4y_t9NM6JzIWj9QKh2sqtUsG8W1EYqz6w8FfH1bMji1OxhrzVldOocieNmiTh0blNtX9Sq-SebCjL458GW4SPIWycDHekamVKjg548ViBaCi8OPWkzq-uDtX4wTjuIit2zAYJ3LKxk5yFHE50qTRnGr3LmzwPVd-r1THg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آخوند و تعریف و تمجید از ترامپ
😂
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/66326" target="_blank">📅 00:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66325">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1190f45b0e.mp4?token=mN-K8KBjOJnlvKEK5kjHpQXNfpr326lDyy-VjKXa2miSeqJ5_AlXCcfvbstLpcWoqa0fP2dce0OEnvtN7yEzwquABH89l3Y1LO4cgmyjZOBs4B6o9HU8CeVu7b9rXL9CVYDdM_oXKtP0n5DSRgee-wCbwjVt4GEvcNd6YUwVp__NDkopbik6ZE1KcQL68QQO4WzDAkSVuLeLmjx4_h2AsO-VlhlroCEXjEmHWQTb9N8FyjcpwrS9EREqImpu4ZB4Ygro5AitNKvT2DmskzElMIk2Eb6SYvuMzmaz4s-nWvTCChqm8rt1hDxFKVgHLMalcrwhoRf6wk8fIFObYsH2HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1190f45b0e.mp4?token=mN-K8KBjOJnlvKEK5kjHpQXNfpr326lDyy-VjKXa2miSeqJ5_AlXCcfvbstLpcWoqa0fP2dce0OEnvtN7yEzwquABH89l3Y1LO4cgmyjZOBs4B6o9HU8CeVu7b9rXL9CVYDdM_oXKtP0n5DSRgee-wCbwjVt4GEvcNd6YUwVp__NDkopbik6ZE1KcQL68QQO4WzDAkSVuLeLmjx4_h2AsO-VlhlroCEXjEmHWQTb9N8FyjcpwrS9EREqImpu4ZB4Ygro5AitNKvT2DmskzElMIk2Eb6SYvuMzmaz4s-nWvTCChqm8rt1hDxFKVgHLMalcrwhoRf6wk8fIFObYsH2HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضاییان بازیکن تیم جمهوری اسلامی به خبرنگار خارجی:
مسائل داخلی ایران به شما ربطی ندارد؛ مسائل خارج از فوتبال، بین خود ماست و خودمان آن را حل خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/66325" target="_blank">📅 23:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66324">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fcce5ba4b.mp4?token=PfQ5T9rqMoOld9OViIVjjT4IZOgXCswiED8dz8vhbO2HR0TPve_XE04zta31IiyT7MrYTQGk7yl7ruQQDEh8DmWYedqn1KtBFxYPT_yYzDVAzNwbNg906PPfsG74n1ChNWGVFQivk3RNmdfjJP795EciacJYM2B8Z2YIxBBDfABNNhOPs5oNA4rqDV0HExtN8s6nWWal5nWjAV-xqiDhoyYVNKj7KWkYTOKlHRhHppHBbIiULEiPe-IzfqyJUwvxWSQN6O0KrzwIDBHQQiUPrXoU0YVf8BUAjgkC4iNDdjtGJRVAl7JBW4X7F9LIkLZec6Lf494sDClkihPdSGvr_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fcce5ba4b.mp4?token=PfQ5T9rqMoOld9OViIVjjT4IZOgXCswiED8dz8vhbO2HR0TPve_XE04zta31IiyT7MrYTQGk7yl7ruQQDEh8DmWYedqn1KtBFxYPT_yYzDVAzNwbNg906PPfsG74n1ChNWGVFQivk3RNmdfjJP795EciacJYM2B8Z2YIxBBDfABNNhOPs5oNA4rqDV0HExtN8s6nWWal5nWjAV-xqiDhoyYVNKj7KWkYTOKlHRhHppHBbIiULEiPe-IzfqyJUwvxWSQN6O0KrzwIDBHQQiUPrXoU0YVf8BUAjgkC4iNDdjtGJRVAl7JBW4X7F9LIkLZec6Lf494sDClkihPdSGvr_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرزیدنت پزشکیان:
مشکلات خودتون رو خودتون حل کنید، من سیاستمدار نیستم من دکترم، برا سلامت مردم اومدم
😔
.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/66324" target="_blank">📅 23:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66323">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9ab7bce46.mp4?token=eedHCo01_Evqx5hizymjkal3gVo3twRcd6JUEt8My8fJ_7l4DVWm-Nj4Wh22O7eTgvu2KwJo9s5JW_OSQYKKhY3lXVkN5HDMmOilfSUDWarUSqunuYDVfmdYCt3sOST13VCtV4BZg-Edys6hCRCShBx-iwcrYGA5clp2RkMNUic0vrPW1dqBpAZmRkX8CbcQmpI5Xon9YPGU1mx6k3YMa3_IiKGEwrjtmIqnZqhTIr9Vfgiir5rxQvquPj5UbQQfTInsASu5wxQTjeMJa5FH1V2JAdBTM115hGV0eos0ty8IBOIbsv_rZT96QHP9liFBj79T5nCHlLTR8yEVS68QhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9ab7bce46.mp4?token=eedHCo01_Evqx5hizymjkal3gVo3twRcd6JUEt8My8fJ_7l4DVWm-Nj4Wh22O7eTgvu2KwJo9s5JW_OSQYKKhY3lXVkN5HDMmOilfSUDWarUSqunuYDVfmdYCt3sOST13VCtV4BZg-Edys6hCRCShBx-iwcrYGA5clp2RkMNUic0vrPW1dqBpAZmRkX8CbcQmpI5Xon9YPGU1mx6k3YMa3_IiKGEwrjtmIqnZqhTIr9Vfgiir5rxQvquPj5UbQQfTInsASu5wxQTjeMJa5FH1V2JAdBTM115hGV0eos0ty8IBOIbsv_rZT96QHP9liFBj79T5nCHlLTR8yEVS68QhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عرزشی:
چرا با کسی که به رهبر عزیزمون اتهام جنسی میزنه مذاکره میکنید
😂
.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66323" target="_blank">📅 22:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66322">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
قرارگاه مرکزی خاتم الانبیا:
ارتش اسرائیل، طی دو روز گذشته پس از اعلام پایان جنگ از سوی ترامپ، «۸۴ بار آتش‌بس در جنوب لبنان را نقض کرده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66322" target="_blank">📅 22:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66321">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
#فورییی
؛قرارگاه مرکزی خاتم الانبیاء:
اگر ارتش رژیم صهیونیستی حملات خود را در جنوب لبنان متوقف نکند، باید منتظر پاسخ سختی از سوی ما باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66321" target="_blank">📅 22:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66320">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e376d329d7.mp4?token=lcmk2ciSB4_wn7terkBf0tfJwEtCSR_YcVjcV3J0FNVzzVZKS3FLL1Bt_naQZ05k7DXwOaal3rv_nohS2GJjQLwmPMTjlnvtTMMPN87JV-eI9hZAMy0D5OdTDaMKxGolIDcQc_OPATydL8-Q0GALLdMMnV5f8L8GGNb-0nfv-cJc6v3DeitexcHQ56IU3SxTVHv8S1ddz9NhrZw0fD4D4TOADCASjzo0PpUQBUH7_b-shdfwdIRzYi5XOLq-vROunbBPhHyZFcGjHLD5tw9OQ0_lvfWkqogyvY_W5zWkozVyVhM_s5hR4iGVurkGrXb7cJLILuOAzwA8NnXwFKrWsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e376d329d7.mp4?token=lcmk2ciSB4_wn7terkBf0tfJwEtCSR_YcVjcV3J0FNVzzVZKS3FLL1Bt_naQZ05k7DXwOaal3rv_nohS2GJjQLwmPMTjlnvtTMMPN87JV-eI9hZAMy0D5OdTDaMKxGolIDcQc_OPATydL8-Q0GALLdMMnV5f8L8GGNb-0nfv-cJc6v3DeitexcHQ56IU3SxTVHv8S1ddz9NhrZw0fD4D4TOADCASjzo0PpUQBUH7_b-shdfwdIRzYi5XOLq-vROunbBPhHyZFcGjHLD5tw9OQ0_lvfWkqogyvY_W5zWkozVyVhM_s5hR4iGVurkGrXb7cJLILuOAzwA8NnXwFKrWsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هنوز سواله برام؛چرا خارج شد؟
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66320" target="_blank">📅 22:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66319">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUnZvHqLex3OsEzFq3uqVkGTQ3Y47oNabE926BKr4XFV5Z5UJZKo7UIL7kca-mFU0U426r-719nd0ozBJQ7bBg-8g3KanyNuyFoNNOXMo-HIwH7ZTRTbi_eQULoI9Tz1A8eZBE8oTrfmuMsfhz85nuNraooC9yyH9zPZj4LhrhxhAX13vZXQHWI2Jf-5x5YnYLHUyOvJRRRkobty6mr-l9Lzi4BhsA4RFiB1icLbDvAL0h6vfa44EZQjOxn0Zixrnu46AT6OWYfD5E3f05aQZdy1_I0p0Q55ot98wZ0487PEr4VgUQ9FZwSug1d9WgM_fS9iGKmesCqJ5FtZt3ubFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نفتالی بنت یکی از نامزد های نخست وزیری اسرائیل در انتخابات آینده:
توافق فعلی بین رژیم جمهوری اسلامی و آمریکا فقط یک توافق موقت است.به ملت شریف ایران می‌گویم که امیدتان را از دست ندهید، جمهوری اسلامی رژیم فاسدی است که سقوط خواهد کرد. نوبت بعد که مردم ایران قیام کنند ما ابزارهای لازم را در اختیارشان قرار می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66319" target="_blank">📅 21:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66318">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/837293596a.mp4?token=N74ucms-Vbn5QGya8AsEME6yLP6psoi1r3QygyhrX5r7Xv_CChK1X9sLi9lq58bkZPWxAwdgRRjlhql8LITiUGPiqnitXBbtUwSPy1WIlzGSPuOJSe_a1bRK0pqB6uH9z3kcB51MN4liJOFbitOvzFcp_IB2Ha2Xgbo2RIzRwyH4V5RHF7sl2Zkawkd2buY_dMUrBRmTpzCA8-daQNzMKFzyub-xDBe-0dvrDlTrOcBPV1rHQ7d7rh2SThA-Vwrx878StGaHZveYukmKe9bIrT74S0EUjSqVMhwLvqgzHja2q2WQ5ibAlwK8cIeRGZvXZNk7FdURz7CWWe9QzrtRyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/837293596a.mp4?token=N74ucms-Vbn5QGya8AsEME6yLP6psoi1r3QygyhrX5r7Xv_CChK1X9sLi9lq58bkZPWxAwdgRRjlhql8LITiUGPiqnitXBbtUwSPy1WIlzGSPuOJSe_a1bRK0pqB6uH9z3kcB51MN4liJOFbitOvzFcp_IB2Ha2Xgbo2RIzRwyH4V5RHF7sl2Zkawkd2buY_dMUrBRmTpzCA8-daQNzMKFzyub-xDBe-0dvrDlTrOcBPV1rHQ7d7rh2SThA-Vwrx878StGaHZveYukmKe9bIrT74S0EUjSqVMhwLvqgzHja2q2WQ5ibAlwK8cIeRGZvXZNk7FdURz7CWWe9QzrtRyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی‌دی ونس:
اگر مردم ایران خواهان رفاه بیشتر هستند، رهبرانشان باید پیشقدم شوند و رفتار خود را تغییر دهند اگر این کار را انجام دهند، عالی است. اگر ندهند، ایالات متحده قبلاً چیزهای زیادی به دست آورده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66318" target="_blank">📅 21:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66317">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحامیان جبهه اصلاحات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMHTwvGauQlvqmS2JROyT3KRPuC7V5dOKsYOgMneceIC_COmGhEl_hkU25ruQZLmDE_O7ZUhoxDk4pFR2X-l_-7Faj8mx1vzVRlqw4AGl2kD55Rd6dWVdjvF1Ru_9Oo-Y-wIy7sky6VPgQvB2eIFDIOsEK4o6-1BJsi8lHqknwV11r5EHbKVi3KTDCN6nD9hjrSZYowQB4ZCRhAOahIrvubT7olswhMZkOBGxB3Re14CeMZdIABebT3XXHXSlOq585zGjVknfVRygAuKpzbcXAJt9ZjuW6PkSHtdLXoJzqQwFMdWpQfaza472_Hn_LfJcKqPbMCriX2cwQ34OxDBvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدون شرح!
@iranwprldnews</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/66317" target="_blank">📅 21:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66313">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDqBYpUrx2D629fdBomvu1fNPtXIaIBxIMohCXHVFuWrluUiXrdBIcLreWqyVuQshsvzNO6T0UmdEPvbTJuIpRIfV_L1Mi_T8H7jV6u3z6cEM45OOotqAsprntU51zbWM8msVEAnf8wW3d4UEMNPL0ctEtFCbJukwYRsyp92z3QL4QswoDkFc9jhAk2RbJxjA9q4CY38guO-sOAtBIgdGlY7pQmseYOBGeOGrqiZMZgvBGEOmFjkR6iUADVzA9_EygpAOVbLIG3eBWjP8YHHTsfs4AVqOmvBC8dmCi4VhDQSW-v0w-NiWvegE-WPPUNvG8UxiUfPWvgHWx9WOz157w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
زیر نویس شبکه خبر:
حمله پهبادی اسرائیل به دو روستا در نبطیه در جنوب لبنان ۴کشته و تعدادی زخمی برجا گذاشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66313" target="_blank">📅 20:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66312">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9Y4oaiyMjXIaVQgchuwCTdPHiYFkFOWPthXbQ-1LHSB3H_sk161u9wPtYeouh_z8VsG7B9R83ggVJfuSkfdjJd8O00Fuy-anZECDQOMP2Nua3fc5fDjliVeK6mfzU6Dl2dN-pzrWTQjfR7Gmo1hNlXU9kq-joi3SZ0cIo2wdqmGJJvCFq9vKsBXVL8gjp3RwCJURpu76AKC5F572sOxMWZdCqkKOTKGQt0HZqlDhzk3x-4cT0ntrRt3dddwQBlZrRYWOtpKu5BFZP09nkDpjAOA3djBYD2Jn_6wz1VaSEiTpj5flKV7omSFYlM7UmlWAsZKlng2zTATmkCvTMDWYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اتاق جنگ اسرائیل:
لانچری که به سمتمون موشک شلیک کرد رو هدف قرار دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66312" target="_blank">📅 20:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66311">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c47f7533b.mp4?token=ZUXV93mgLaPTK5GprjFd3ZDk8eo7arbYhipqC6_uSx9vLxw14Eopo5CmqSxsoc7gm6m3APmnWED0G91NbOLnwd8xsqLG1Ww-op0mkHCEj14DHsDbz6q_eYKwmP_3mWuU8W9SbMqgQ8ljOKt5SveTEchrrjOju7yUtqeqao02hIOXs2Ao_LeqIaYvEq6NPfi_W3lO4edmEBYEAUAgNQjzHgja7YjWT1SaeaMzj2Uvj28daW3v8zKFuXIMOf88LyWSxUsHhKkrWTaGJa33bfca0-s5i5zLO3vaefgxWFMr36vnH-v1uyAynLLiYWOwArmZaW6RcYt2UbzMd9DdyovyqFn52ag8fRcW_g_kNahY4qLzud8oPqXusuhCSXo_htYdo_mSIhzQOohwifVX8xd1cIn985fFPED2ozhEmo5EgE-g1kSn9y_BDVW-lspvw7VrvHpyn2nGshkNcvw6UfmH_-3OKBO1PXLPb08BhHK91zUohKihs_ex5yqgdmdJLFFuTYYex-nYncR-UaVqrqqMqYS9Rg7kAti_R1q7i9x0AdZsNQfEhAxazIvSFv_Yx1AzXIKfD4vcRVHXK-03I5wz2BAX4KjbMffqsQhXU-nV4lrz9YgQ1e1B876Z3XH0EskeTkl_NjghF5CE6uYjq3HL-Ul-zW2esTzAhzwwxyqJDwY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c47f7533b.mp4?token=ZUXV93mgLaPTK5GprjFd3ZDk8eo7arbYhipqC6_uSx9vLxw14Eopo5CmqSxsoc7gm6m3APmnWED0G91NbOLnwd8xsqLG1Ww-op0mkHCEj14DHsDbz6q_eYKwmP_3mWuU8W9SbMqgQ8ljOKt5SveTEchrrjOju7yUtqeqao02hIOXs2Ao_LeqIaYvEq6NPfi_W3lO4edmEBYEAUAgNQjzHgja7YjWT1SaeaMzj2Uvj28daW3v8zKFuXIMOf88LyWSxUsHhKkrWTaGJa33bfca0-s5i5zLO3vaefgxWFMr36vnH-v1uyAynLLiYWOwArmZaW6RcYt2UbzMd9DdyovyqFn52ag8fRcW_g_kNahY4qLzud8oPqXusuhCSXo_htYdo_mSIhzQOohwifVX8xd1cIn985fFPED2ozhEmo5EgE-g1kSn9y_BDVW-lspvw7VrvHpyn2nGshkNcvw6UfmH_-3OKBO1PXLPb08BhHK91zUohKihs_ex5yqgdmdJLFFuTYYex-nYncR-UaVqrqqMqYS9Rg7kAti_R1q7i9x0AdZsNQfEhAxazIvSFv_Yx1AzXIKfD4vcRVHXK-03I5wz2BAX4KjbMffqsQhXU-nV4lrz9YgQ1e1B876Z3XH0EskeTkl_NjghF5CE6uYjq3HL-Ul-zW2esTzAhzwwxyqJDwY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه ای که سپاه داره لانچرو برا شلیک موشک آماده میکنه و ایشون هم شروع میکنه به فیلم گرفتن.
واکنش سپاه:
😡
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66311" target="_blank">📅 19:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66310">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66310" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66310" target="_blank">📅 19:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66309">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gI4UiqLpnjwIYGCPE6SyqCvgeCCnTqcYtFuYGCOHeMjYlgHGBxwEkrhsUbJptZSpYM486I9mQSkqQhPfa2fY0IX1OLZGXjUKDYmxkGkosuoH5XMvS3YpIMQu-iStnDEZ3yfZNr2wFk52q0uEMdpxpm6BRazno-zzKAx5f-8ukGqlI99ag0AD4WKUtklyedfptFS2K5kmJVrMRgZXcKP5ELHUIHZFiLbkQrwqWb9iYl6ETstMmb5S-azr2mCPomQ2KpyMQ_TG27-3f_8OyZgVFzU8eSGQwVJX40mAScftYvBODeA7OzK0Du7jG_cEVg9RaYWKZimIxzFYBaVm28vBJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66309" target="_blank">📅 19:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66308">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bd23rZ_Pik6bU2bSpDMlGfvf2BImaHBlN8IIoyqSExRTGgcToQ5MGchyrZxefEi0Mh6xlyzWcr_ZDsEcTYxduZrTqxWv_Ih44WeqnopaUFEDPU_VLEXJVRwKgr4CCtiRWR_YDe4QA_03EFQ21OH-ew-GEGTQ-ANS6Um5GrLk2gEhEyj4cI6LYt050uAoRvlZ-GK7jYC2AGA--pDI0hKBmq9O0mMOKj0tFFKZ6Lkn0x16uotlMqh1O_J6rOt1P-Wer_AtGitd8Mv3iUaFZldCX7hgEKRQyqLTLbPq35-2zwc-ABXUiEjGNnpBl_B0vq3ijG0a43rEvXWC0Z1TL-1DrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فاکس نیوز:
اف‌بی‌آی یک توطئه تروریستی گسترده و چند مرحله‌ای را که قصد داشت رویداد UFC Freedom 250 روز یکشنبه را در چمن جنوبی کاخ سفید هدف قرار دهد، خنثی کرد.
به گفته مقامات فدرال، این نقشه وحشتناک برای "ایجاد حداکثر تلفات" طراحی شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66308" target="_blank">📅 19:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66307">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCELI6vb_N_1uT_fBIlQ-F7p8IUVZqpaYnAE5HdWMXAoZ2KFW1wYkXZfLu9whd3YPyu-1Zw63d7ESerkql8w1_k-50R7IIPfOfr8y_YvOtzaflQlmhKQxSV4rMqnOCq8r2akMJkO4aUwNIraINtm6kyO_BG2xxNMfpgKWXsKfQOq1iL5BR--dl6T1TAvBy8c4TEvcZPcjdCbpkQIw6kgXOqceBBn2fcJEDl3QMqQeSRGj7U6LVGaQyJZ_Kjs5tl4-ZMZlXdkA7Nj3priC2UuebjpXjrdJKimbV1PyU_9PtfQRhG_YC6kCwrznhTniq9IY4vYcMX3ERz5jkIF_5LPqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ارتش اسرائیل، منطقه میفدون در جنوب لبنان را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66307" target="_blank">📅 18:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66306">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecc0108dd2.mp4?token=J-sfDDHV86HHxz4TDiDIz4IRRiK3tD8VbmhvFohZrxOB88EWPWLZ43qVnrhsRpfbAYPaYuGKY4jqjZAvSQt1wIqIJOop3dSkNen1qmbMIU8oZ_ouOvbPM9YDNySQxbNtt6HD_97n-1l7Yq8hvQI7TxJ9t3_-ow4LSpfHvHxJT1ARDkX9tNAbJW1BvqFRjMTOBoKULFJQ45jgyP1CS8fl5YZRDokRUX-pPukc6xJmStnDG1mTQB7FMSv9vhjC7HOpopnKrehGD-aOJSoyculuyM_-Y4FlFxXJdTZAJcd3FzfT94laWvc0VnJOda50nbEnss4Oss35nM0DYJzDW3weXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecc0108dd2.mp4?token=J-sfDDHV86HHxz4TDiDIz4IRRiK3tD8VbmhvFohZrxOB88EWPWLZ43qVnrhsRpfbAYPaYuGKY4jqjZAvSQt1wIqIJOop3dSkNen1qmbMIU8oZ_ouOvbPM9YDNySQxbNtt6HD_97n-1l7Yq8hvQI7TxJ9t3_-ow4LSpfHvHxJT1ARDkX9tNAbJW1BvqFRjMTOBoKULFJQ45jgyP1CS8fl5YZRDokRUX-pPukc6xJmStnDG1mTQB7FMSv9vhjC7HOpopnKrehGD-aOJSoyculuyM_-Y4FlFxXJdTZAJcd3FzfT94laWvc0VnJOda50nbEnss4Oss35nM0DYJzDW3weXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ:
ممکن است شخصاً یک کنفرانس خبری برگزار کنم و متن یادداشت تفاهم میان آمریکا و جمهوری اسلامی را با صدای بلند بخوانم تا رسانه‌ها آن را به درستی پوشش دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66306" target="_blank">📅 18:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66305">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HooidtglM31xh8_nI9wG6J0Eq7zhzvIxSi6P02znIir6jRANnfYTSApS3i-QvRw5WA_xlSkw3pDPTNfFl5j8K0W2C6rGjN0EL8Y6PsPUWaMaQwoNKtUyJ1wyL-UHY6rntryUFLPc77wLiB0mHjvd8ZyCEumhc8lLBKZ0f6QxFPV8BeY-eiT0Qu-6gLM82VRdSAYPEXFJglKB_7PyI5ytcvUlTyUHkYWhMPUE01ugYxpFcjEWlOJKcBdEnMHkGEkkooJrq9k1bSV3dzklqyQg1wpUK-XpIzLOLtAxNE3Yz8qucIQsiiKucTjQLN_8JsegKFHqnru3KY6pUyqk7viXKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جام جهانی رو پیش‌بینی کن و جایزه ببر
🏆
با ربات تلگرامی «نتیجه‌باز» می‌تونین بازی‌های جام جهانی رو پیش‌بینی کنین و جوایز نقدی برنده شین.
😎
۶۰میلیون تومان جایزه برای نفرات برتر
⚽️
تازه امکان دعوت دوستاتون رو هم دارین و به کسی که بیشترین دعوت رو داشته باشه هم یه جایزه ۱۰میلیون تومنی تعلق میگیره.
فرصت رو از دست ندین و همین حالا از طریق لینک زیر وارد ربات شین:
@NatijehBaz_bot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66305" target="_blank">📅 18:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66304">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqIadPe6qZRQM991yk1s2JNY7PD5PimCLAq0Swio3yoPSp0qdeWiDL2euBMPZQk3YVO7amrn7p9PZAEZCufTBKWeCLiQ37pdjeYzXmjz0yfbKL9WbTbhEcKZXfPhSP-MVn4lgP5n6uZ18MO_97UNQ_5lQEl6RCcCUARy3x1RFKOwjQfkZ_qn-HYDhbll11XvHZvsdhlcrSzwf4keZWPYl3fIL5M9v9m6PCODABzvNTGsNM9fZIZEBcZBbbX73wMjpxvYqOFkPCcJZm9rzcXej3m8O5Uy0e4j0ZOE6oyhZS3nhy1KxhqEZYm0yJHegSZC3NgOkJvFO7dCJRZt9Xn8kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وزارت امور خارجه سوئیس:
قرار است یادداشت تفاهم ایران و آمریکا روز جمعه در بورگنشتوک، در مرکز این کشور، امضا شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66304" target="_blank">📅 17:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66303">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7yrJ8xWw0XArHJ8YjLtK43RNTHsk0ZKpLs743zHoIBWQTJ64eIuR-vUOf-AfevLvH2b8nKmp9DLA68s39M0_CwHotsjP40ZUtTpPSIbGDoqGrNV-S7djPh1sHYkCffJIxWp2Em0Q5Loqc7fkM0-So_TzboMHNGKOyHQxjEHteChcNKE815WP9NGss0RMLyTT-ehaPiH04WzCWUa978HttnqJBU5ap75BH3JEGAjE_7mneos-NyU0g2j2sdbENlSsAnnLXyh_UWNhKf7e8ZV3iLPoOn6S5YVHjpPk49GWilvEap7PFL2sNzz8052LJCwsmnlqH0WWQXxpdULKAg4hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویر تیم جمهوری اسلامی که آمریکا و اسرائیل ویزای جهنمشون رو اوکی کرد.
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66303" target="_blank">📅 17:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66302">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66302" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66302" target="_blank">📅 17:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66301">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmAirgoDNld2Iq_A896Py7ykyRbF7zkm1vumxV3mo2pDhQn3_BiVUQ7LQk7fSvWfQqT57aKceRJP5XsPfJomFOPmjzmlFMpo6QpDVGboPeH_Gv46Aq1LXrErlZCDQBo-0rfk8JCHcS-DgWJYClXFSmjDtvTYEmCh0R3-vZCBhIRZhb7CT9tMWJda8ddkSfoFkG07yJHdJWs5YPXqLfYk2pw__2oy6bsr9NioBlwagmPCMlgYOLBIjwxdSlAFZxmc_unH_R0fDLhTyLcos1S-boNcNdxR1_io5TAY7ip_iPwfR1IRfEigM6dGlHNjFTkjpCCSbKap5QodtpUrMDr3Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66301" target="_blank">📅 17:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66300">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d1538e700.mp4?token=pM1NNP0TPAOJoCN1Jn4sP0RAouCHuwE8OOo4EsbMU1Sq3w1ZBxVDRfYVkdUXOvl3IV26gPp4R-yMGuByrHJN_E3UmG_yD77yp3UHA-Xfqa_zLTl-_MaLaHu2TZRQBO18q0c0AQg3cgnU5WoxhM_hLYz-r-a8wqdjLlQr97w6N9dOpcW2jSEtCMqDCA88I4hCW05k_RkZ-xIZ8qY5kJF5O5OsThN_h5dg0h00C9OEwPs_uXR017f3xslVaL82ewsiDk2N9rDz8WdoFOfxKNZ-lqP81Ej3a5fZ9eLNqcKDpoO3GimY5dF2qr5XNJ27u5X5tpiB_c5I46eFSf97J3b23Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d1538e700.mp4?token=pM1NNP0TPAOJoCN1Jn4sP0RAouCHuwE8OOo4EsbMU1Sq3w1ZBxVDRfYVkdUXOvl3IV26gPp4R-yMGuByrHJN_E3UmG_yD77yp3UHA-Xfqa_zLTl-_MaLaHu2TZRQBO18q0c0AQg3cgnU5WoxhM_hLYz-r-a8wqdjLlQr97w6N9dOpcW2jSEtCMqDCA88I4hCW05k_RkZ-xIZ8qY5kJF5O5OsThN_h5dg0h00C9OEwPs_uXR017f3xslVaL82ewsiDk2N9rDz8WdoFOfxKNZ-lqP81Ej3a5fZ9eLNqcKDpoO3GimY5dF2qr5XNJ27u5X5tpiB_c5I46eFSf97J3b23Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هنگام بمباران بیت رهبری هرکسی که اونجا بوده کشته شده جز مجتبی.
مجتبی همون لحظه:
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66300" target="_blank">📅 17:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66296">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ki0DX59vR3XXe9trvVz-SmBlgOCcT761CXZ_v41DmwCEgmpjwbxWL-GvKBoMRBS7ZUCKiml_OUUz8FhhwyJ5q1eizjqMgngQiILn_3kvn4M9fyXMOmgFOUsWgM7sEH8Y5Kh6iC8N1DLYCjTpTd7f40jssx52AvdBlsC_nW8sJOQJpZKwlUomb1Yy5trtQRTvhANTapL2yOvYwlldJ8g079VBPPs-ULr5Plo02AQZjCVziId10p_AO6AeP8Fc3HpIJ62zA2PlLAMXNudE-k_pK1WwYpN1D5Ydvs-0EaODL03-SFZCU1mXP3iLXbyJbqU0a4nSG06n3OrKNepb7jfA0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TxYhek32LuzjOVTsrgGIOAOTBucu6as_bMr8gDenQ2PFcglQD1gj1tEZ5K-kKnM3dG824AqeP041zK6OSF6h2a7ZRz874USewEc754M3PqRLYDCnP6P3gXKkdb92JqTZ2H82PTOE9MGLKsT2xEQ3gQs_AYkGjBvcr8wjkZJP6cpS6WwsLH3lB1cFyLBunB_REwgptx7qnip77vespE-S48oRndl1w5v45YUosn9lKDORqqggRj2zxaJesnS8gxlBG3_gBhk4COHHSpGRXKqFqZLQ28HyTB_BNmIuVIaTylKc2M0k8doBc7Z2NTgFh8atNfx2pJEzB3El0j-1IMyxDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZycVQmRxGkXKm7CXg7Ca1gmICLCTB8uNctC0KJ1Ml7U2aW1mK2fNtBHY9aSXsczk0UqfRDt3xoV1Mo06JsSuUocBtCukYyhBUsA7oOpPLRjEjR4BAW8nR2StrM3fQJXjLEWf1-qQ96dUl7gejRFxvriNCD02cJ2ImlEKOERkKtzpyiGNZkOw9oBtOxXjRBZsIwzVIWWO7ZQgp9m-GMwArZyEsdBgBgC82HZzOXiKqubar87ENuOg-BdDj6mVI_euqVBccqBt1FCgvPPni-FX1Nxg2ygy-PXCRH9cNGxex7-DOJVuvqNRTlsWBynxWoPPqOqDLkB6K9zarMB3njp7WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hsmEHCExZLsXGLDrE0khscKMLpGasy69wRUZDq7LL5dTsN3GlvUyBzdf3Q_Ok-HcD2_KG2zG13E_AHMxJd_r6zen5D0itHEYje8_6glw5FdjlSaB23I7pZzCDN7Q1cpO0voTL8XLSvyaP3AdkSleFwM3wWycDWRI3A8G4TgLsU7kp9VlKyCUf09G-QjXl99eDP6l2H_0ZPUWc5i92hR2hCckiveUMPLasB230Hyr5stBAGfMAqUFWFxJof3auTpvf2zasjoz-NSncI_g74JwZnNo5agRF_IRBHimOWy8yFX6XOfqi4F3kspzG3hOOJa1IrEfeaZBaPm6md66AQJfkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ویتنی رایت پورن استار مشهور آمریکایی دیشب در استادیوم حضور داشته و از تیم جمهوری اسلامی حمایت کرده
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66296" target="_blank">📅 16:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66295">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c34b0ffff.mp4?token=fqQJ9Qhwz1B36yn5dzqLjStdLHzro4DfImDhtLUnPKQsFWYPDUbpjZ0xzlwOqq52DZI1g13vi1m-VrMsikouahvb5Buv0lqQwl_UVHG1lT4PJW4ssjaBvfywBL4FZg3h-YISj3bXaWLfftrOXvcSGfY-aSpq4Wwa-G-8S1nyeSi3uOMB07e5Vw7uxXSsLVGJwXwM7Ni0pwyNBEOP1d8aYKhBFtTykmz048iGZ75TmLHUUNCVke3ytJed7viwCF5oCBc2Kcc2HHWdRmfrGvXq_2TFcZzL31kisnT4REE2S3y8A9iWgUdIqGoORlDqFCJ1m4lQY1hmbAdF7w4ErMN45g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c34b0ffff.mp4?token=fqQJ9Qhwz1B36yn5dzqLjStdLHzro4DfImDhtLUnPKQsFWYPDUbpjZ0xzlwOqq52DZI1g13vi1m-VrMsikouahvb5Buv0lqQwl_UVHG1lT4PJW4ssjaBvfywBL4FZg3h-YISj3bXaWLfftrOXvcSGfY-aSpq4Wwa-G-8S1nyeSi3uOMB07e5Vw7uxXSsLVGJwXwM7Ni0pwyNBEOP1d8aYKhBFtTykmz048iGZ75TmLHUUNCVke3ytJed7viwCF5oCBc2Kcc2HHWdRmfrGvXq_2TFcZzL31kisnT4REE2S3y8A9iWgUdIqGoORlDqFCJ1m4lQY1hmbAdF7w4ErMN45g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استادیوم فوق‌العاده زیبای مرسدس بنز در شهر آتلانتا در آمریکا میزبان بازی های جام جهانی
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66295" target="_blank">📅 16:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66294">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">واقعا حق اسپانیا تو بازی اول خورده شد باید ۱۶ تا به کیپ ورد میزدن   @sammfoott</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66294" target="_blank">📅 15:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66293">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ta757FkxnMmOfFch7KLl3uac1bGs1U75-fGlGznoJOe2hokyqRX06C-ATsyKRY34jdfZF9N2T7-ZC3itFDNwNMczAHej-zHCWNPqCSm6C2L7djC42_F7ZoOn2OykO3ApOebh0XgHwBOoL9nhCHIpQ3yymae8cR8AsscXH9f5YDQ9ydbBZYjzL1atGZZvkBZP8NK0xIJZ5g2LFJ1sYJ6vU1K35WdznZKWCNOgOvY7UTFyAJhP6IZ6pK5z5SEDNfGKxy5le7NGvTvB8xOezE2blVymPjxf0EQ8610A_j-3UVIENXdoXpGrYpwvxZH844dPdZYHPBaMACUv-a8g-ZYoqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی:
جمهوری اسلامی هم‌زمان با امضای تفاهم‌نامه‌ «صلح»، دو تن دیگر از معترضان ۱۸ و ۱۹ دی‌ به نام‌های جواد زمانی و ابوالفضل ساعدی را اعدام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66293" target="_blank">📅 15:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66292">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52f8c1feb4.mp4?token=aju4buIU6k5xYOv11NiOoazyRYBqKScK2-GKwCg-z9uOllQ3eiGHsD9LVOTa6kHON9kWIP43oJMs1CqfBbAQ6Yak1Pmi8Pm8GVM0oQzNBVRORIEEu7py62_sDGWgHC4llFyL6Qcb9XX1kOSAqx-e24GR4ZmOlV07_xU9yeBqVBbxKPtJ-huLk1kzpsBgRJRC3VtH4mywjXr5ROMrH-thvlQDCPzHwt4jbJ0BvoLGiP72MqGHRZcPzP4rJd4vfFIibbQRQue0tvbJxspRmUMOjPLHz_8GNE6Y82aG4VVgXIyRKQxFFGVD9S2CDIPOOu5WIeRwY79F0obGHbiBa_WfuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52f8c1feb4.mp4?token=aju4buIU6k5xYOv11NiOoazyRYBqKScK2-GKwCg-z9uOllQ3eiGHsD9LVOTa6kHON9kWIP43oJMs1CqfBbAQ6Yak1Pmi8Pm8GVM0oQzNBVRORIEEu7py62_sDGWgHC4llFyL6Qcb9XX1kOSAqx-e24GR4ZmOlV07_xU9yeBqVBbxKPtJ-huLk1kzpsBgRJRC3VtH4mywjXr5ROMrH-thvlQDCPzHwt4jbJ0BvoLGiP72MqGHRZcPzP4rJd4vfFIibbQRQue0tvbJxspRmUMOjPLHz_8GNE6Y82aG4VVgXIyRKQxFFGVD9S2CDIPOOu5WIeRwY79F0obGHbiBa_WfuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
انتقاد ترامپ از روشی که اسرائیل در لبنان به کار گرفته است:
لازم نیست هر بار که دنبال کسی می‌گردید، یک آپارتمان را خراب کنید.افراد زیادی در آن خانه‌ها هستند و می‌توانم به شما بگویم که همه آنها حزب‌الله نیستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66292" target="_blank">📅 14:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66291">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db26cc81b.mp4?token=hQXMDjVrO8qc2kX1zEcHGuDmPWw5OGgyAuUD6WJNlZNck_6AGg9TLTmkge8F0AS8BLnJLdHnxrxw6EmUQhRyHNoPiy3WbyEcbTfKa6V-gF8kpjsQXzOc3UsPNHgFwUVtFMAnkb33drTXam6a6RDs8HMRKrDU_OwuQslVByXEZAlLKJY8QreT4kNSwn_3tysf1PGoXS0tsLKyTvEUCwGc4_4i0PpU1Sf5vbmk07BvctDrpfXCFVG-4UscC1tDciKmohbnM2EEMvR7OqfqStokLqYNVJsYMtDwJE-7TY9_6Isbdq34FqZfyiY4j9lNWLZgbzLMmcea_Q1Lzn1qGbKh6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db26cc81b.mp4?token=hQXMDjVrO8qc2kX1zEcHGuDmPWw5OGgyAuUD6WJNlZNck_6AGg9TLTmkge8F0AS8BLnJLdHnxrxw6EmUQhRyHNoPiy3WbyEcbTfKa6V-gF8kpjsQXzOc3UsPNHgFwUVtFMAnkb33drTXam6a6RDs8HMRKrDU_OwuQslVByXEZAlLKJY8QreT4kNSwn_3tysf1PGoXS0tsLKyTvEUCwGc4_4i0PpU1Sf5vbmk07BvctDrpfXCFVG-4UscC1tDciKmohbnM2EEMvR7OqfqStokLqYNVJsYMtDwJE-7TY9_6Isbdq34FqZfyiY4j9lNWLZgbzLMmcea_Q1Lzn1qGbKh6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
در توافق من، اگر ایران به سلاح هسته‌ای دست یابد، منفجر می‌شود.
در توافق اوباما، به آنها اجازه داده شد که سلاح هسته‌ای داشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66291" target="_blank">📅 14:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66290">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaeee1ba07.mp4?token=f-OGi25nDAbF09VYJcY9XnuP6tLAyawNRsNUlXx4TGXMXQVJlB6khRmEOWR3DW0YJ6kpuGBRfL25ayA4aWbUMprxURhtTOvAaTJL1IufHY9BUHCZPRle7ElMSXlucpH0sweEFkn3eLPq9DvKEqQ0EK4C2jO-aBC3fdLLBAHJLRW7t83zo3396CIhA4oPpt3S1X-dB0x2dcHLwKUbkHZAH-9yascMFch-V-GkQ5gNkmiU5kEbMErUBx6zkusSJ4aK8TUZuOCJyGQ_qgdrGf5zpSOmQmWQskJZJ6nyoRAmLVjrOSr__VWvo0TfEvS7K7RBclEq3wcrFqOK3YS8kVL4sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaeee1ba07.mp4?token=f-OGi25nDAbF09VYJcY9XnuP6tLAyawNRsNUlXx4TGXMXQVJlB6khRmEOWR3DW0YJ6kpuGBRfL25ayA4aWbUMprxURhtTOvAaTJL1IufHY9BUHCZPRle7ElMSXlucpH0sweEFkn3eLPq9DvKEqQ0EK4C2jO-aBC3fdLLBAHJLRW7t83zo3396CIhA4oPpt3S1X-dB0x2dcHLwKUbkHZAH-9yascMFch-V-GkQ5gNkmiU5kEbMErUBx6zkusSJ4aK8TUZuOCJyGQ_qgdrGf5zpSOmQmWQskJZJ6nyoRAmLVjrOSr__VWvo0TfEvS7K7RBclEq3wcrFqOK3YS8kVL4sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
گروه اول و دوم رهبران همگی مرده اند.
رهبری فعلی ایران افراد بسیار منطقی هستند. تعامل با آنها خوب است؛ آنها افرادی قوی و باهوش هستند.آنها رادیکال نشده‌اند و به دنبال کمک به کشورشان هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66290" target="_blank">📅 14:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66289">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/059a9cad8e.mp4?token=oTBBwHKhw18gpn3bgV6N6TxPam7604ehOBNRjoJthy0LGoNkJatdW837eif1pPSop8-22-_VK08BmFGDTLVggcdnwT0J0Yfke2TfpeUpoByyRh2B45XMi9g9rRurOIWn7H1sczFTZGdosMbvSlFTTdeSSTQKJZ20X0LSX7Q1BtXwYvRE8YGNP7-H-YUJPp_k3Cyq6l8WNykPdKVxmuRvkJjjpts5XU7vWh8ne4oS7-4cU4OMPq87fT0RBUf1Hz-x2wE6MsNH7nFpQK2oAzwyQKK1oSoyeiYrGOenci4RUPjNBG9sKCVZ3sTR5lfYmUg93Vv5sEXlp26zbIe7NtdX1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/059a9cad8e.mp4?token=oTBBwHKhw18gpn3bgV6N6TxPam7604ehOBNRjoJthy0LGoNkJatdW837eif1pPSop8-22-_VK08BmFGDTLVggcdnwT0J0Yfke2TfpeUpoByyRh2B45XMi9g9rRurOIWn7H1sczFTZGdosMbvSlFTTdeSSTQKJZ20X0LSX7Q1BtXwYvRE8YGNP7-H-YUJPp_k3Cyq6l8WNykPdKVxmuRvkJjjpts5XU7vWh8ne4oS7-4cU4OMPq87fT0RBUf1Hz-x2wE6MsNH7nFpQK2oAzwyQKK1oSoyeiYrGOenci4RUPjNBG9sKCVZ3sTR5lfYmUg93Vv5sEXlp26zbIe7NtdX1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏خبرنگار: رژیم ایران همچنان به کشتن مردم خود ادامه می‌دهد.
ترامپ: بیشتر این اتفاقات در دوران رژیم اول و دوم رخ داده است، خیلی بیشتر از الان.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66289" target="_blank">📅 14:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66288">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b6ac4ffe1.mp4?token=URfB6yUyWtcr0hIEqPwdUPU_KseRQZyGnWrHoiq-jzCeBrFUprjbpZhJtlrssswfLAQx5DQ1ScBspGzCYtOGdX3kXnjUR2wSyWDefBSs57kd8h6QJuDkKy51NnxZ5F8MXr90vslMY2Uh8xoZT1PNPeCGFpjg5PtSMsQWiDEgf2TVLk0PjAGDbcZ7A6yE3eL0tcixrl7f3NtattjhSz9GA1HjtMRhRR5IgtqCF4bld8l0IDCycmoLhOnlenEJgepalpQlny3jFzLpVBp1wo2CIhRiAYH8DV7za8KzSjkgfJY2o0j4LfdFwpZUr9jdHjF7bHN4oHiru0whrq0wGa1kkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b6ac4ffe1.mp4?token=URfB6yUyWtcr0hIEqPwdUPU_KseRQZyGnWrHoiq-jzCeBrFUprjbpZhJtlrssswfLAQx5DQ1ScBspGzCYtOGdX3kXnjUR2wSyWDefBSs57kd8h6QJuDkKy51NnxZ5F8MXr90vslMY2Uh8xoZT1PNPeCGFpjg5PtSMsQWiDEgf2TVLk0PjAGDbcZ7A6yE3eL0tcixrl7f3NtattjhSz9GA1HjtMRhRR5IgtqCF4bld8l0IDCycmoLhOnlenEJgepalpQlny3jFzLpVBp1wo2CIhRiAYH8DV7za8KzSjkgfJY2o0j4LfdFwpZUr9jdHjF7bHN4oHiru0whrq0wGa1kkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد گرد و غبار هسته‌ای:
شما می‌توانید این استدلال را مطرح کنید: چرا اصلاً خودتان را به زحمت می‌اندازید؟ چون واقعاً ارزشمند نیست.اما فکر می‌کنم از نظر روانی، ما می‌خواهیم آن را به دست آوریم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66288" target="_blank">📅 14:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66287">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77169efe09.mp4?token=TFDzOTYrS-gWDZc1Jo7fOf1wbRufVcNpxM4ZKvM0UECmZPHuCZL-Yag0JUm1MKOprZkfIRfGZ2q5nHjtfsXLEg0IGIwBxw7V_9CK1rD_YLwnw5CWUDFA124bpFgWbqDwJly-L7LiSE74W1BxaGcZEo90yTWnpVbkvyBWeP02meBM5i7ZrmRs9AGxUksfrN3km4sGBtHJM7HwnBdEjB5GknbQTjkKfWxUw0YE6jfLEkMWodUp0q_6FkZocqATm4CnG6gZRYHuZ1s5sFh_hI0qoUUErfky3Hyf0GtPYewGaU1tEJzY3C3nDZynd7zBK20IN6FiIDzNCFuqaQsQkSdU8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77169efe09.mp4?token=TFDzOTYrS-gWDZc1Jo7fOf1wbRufVcNpxM4ZKvM0UECmZPHuCZL-Yag0JUm1MKOprZkfIRfGZ2q5nHjtfsXLEg0IGIwBxw7V_9CK1rD_YLwnw5CWUDFA124bpFgWbqDwJly-L7LiSE74W1BxaGcZEo90yTWnpVbkvyBWeP02meBM5i7ZrmRs9AGxUksfrN3km4sGBtHJM7HwnBdEjB5GknbQTjkKfWxUw0YE6jfLEkMWodUp0q_6FkZocqATm4CnG6gZRYHuZ1s5sFh_hI0qoUUErfky3Hyf0GtPYewGaU1tEJzY3C3nDZynd7zBK20IN6FiIDzNCFuqaQsQkSdU8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
ایران حتی یک بار هم به ترکیه حمله کرد. من هرگز نفهمیدم. هیچ کس قرار نیست بفهمد.
مشکل این است. آنها افرادی کاملاً غیرمنطقی هستند و این افراد اکنون رفته‌اند.
من فکر می‌کنم ایران اکنون رهبری منطقی دارد
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66287" target="_blank">📅 14:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66286">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5225dce7ab.mp4?token=GqDBnSTLxEU7cjSQ1KS2uv_DZ2xgJ35RVr6W57-7Am53_h8BfpeviQjgHyO8uh6B2885EL0FSVoPaSqLMPFwdTHOv-TaYwPMD6F1fdGFaMRQBhFQ0j7IIICEwYhO6ENbaiPfZH8hYwoOnflsGaczYnvaRowB1KgpLQvF7wtCMEpautMaWqS2ONv7qpo0AJxFWq3_sdFWy0z4QntLUV3NOaE6ZWvUa1frIbfoDQivoOnAwFtFVwYkd-_FSTcsfNO1NUa3xO5apCCa8QqYFRAG3tQ-1eViVP6b_K7AZkFwpySWS8-bNlFeyW8cnvITb-ch3Ku2GU9fgd5HAqsVoVVIzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5225dce7ab.mp4?token=GqDBnSTLxEU7cjSQ1KS2uv_DZ2xgJ35RVr6W57-7Am53_h8BfpeviQjgHyO8uh6B2885EL0FSVoPaSqLMPFwdTHOv-TaYwPMD6F1fdGFaMRQBhFQ0j7IIICEwYhO6ENbaiPfZH8hYwoOnflsGaczYnvaRowB1KgpLQvF7wtCMEpautMaWqS2ONv7qpo0AJxFWq3_sdFWy0z4QntLUV3NOaE6ZWvUa1frIbfoDQivoOnAwFtFVwYkd-_FSTcsfNO1NUa3xO5apCCa8QqYFRAG3tQ-1eViVP6b_K7AZkFwpySWS8-bNlFeyW8cnvITb-ch3Ku2GU9fgd5HAqsVoVVIzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگن مجتبی تو LA رویت شده
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66286" target="_blank">📅 14:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66284">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j57zoQDGo7e3PLwx7_4U17_ke7C1I4439R3BJebPXPUNhBEDuFyIBImBqVW4N2X-DkNoJDX_Lu9oaHCpvY4vgAdO8YhBh_HXtXYdh-eZ4lh2gDTCSIwlxZdagGEyyFpGiyJjklfhDtms4OCsF4eNgIU1tURbGAs9sEckZ5MnY9ica9NmnuG-ZCdkS00g6GWMJ6xT4PQTyBe4MF0ThcpY-E47KllBg9UbJ2ttY9dHnabkiJgWqdV6HuT86PdArx_eqia9Rm_YWIfCRxY0nY06nSHrXQbZWLI1ZsiHv09gmhGT-idqcsADG5MimX9QLy9_CFNNfwFRX2R0VX-g88PDqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PiaIuGcH0VILN5pGa3eUB11T9tB80FPm76YUZSHo2_q80yFPZUFODru4KRDoCu-2ai1mEZstXOdC2AOBcQlD6vF3VXZ3Ze3FvNkHHOON4slcbVgJwQQdxBxbla5Jz3iezDIxkFfdmKWKywX8XwPk6K0F5KEPzdiXOscQpJQKCLBbXjXDbBEBUREcWN52lbY8AoJSGeO0lazishlwJiE9tsYIPFxFLjOyaZZ2Aev_LOik62_bOzlP-2QklG245JSehEbxCR6Wx6lhaF4Z7hkKl3c2pcjYp3oqIs6hH1TqYlTEg4XgFK51q0DFtwWhY95Tus1hYaF1A34r-hrgqVImfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
برنامه جدید امتحانات نهایی پایه های یازدهم و دوازدهم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66284" target="_blank">📅 13:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66283">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
ترامپ:
من به اسرائیل پیشنهاد دادم که سوریه مسئولیت حزب‌الله را بر عهده بگیرد.
جنگ لبنان مسئله‌ی فرعی است و توافق هسته‌ای با ایران می‌تواند پابرجا بماند.
به اسرائیل گفتم حمله اش به بیروت برایم خوشایند نیست.
نتانیاهو اکنون باید در قبال لبنان مسئولیت‌پذیرتر باشد.من از نحوه برخورد اسرائیل با لبنان و حزب‌الله راضی نیستم.بدون من اسرائیل وجود نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66283" target="_blank">📅 13:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66282">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
ترامپ:تلاش هایی برای تغییر رژیم در ایران وجود داشت اما موفق نشدند.
اگر ما برنامه جامع اقدام مشترک اوباما با ایران را لغو نمی‌کردیم، ممکن بود این کشور به سلاح هسته‌ای دست یابد.
ما می‌خواستیم برای گرفتن اورانیوم غنی‌شده به ایران برویم، اما این اتفاق نیفتاد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66282" target="_blank">📅 13:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66281">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
ترامپ:
توافق با ایران به مرحله دوم منتقل میشود.ما یک توافق منصفانه و خوب با ایران داریم، اما هیچ پولی در آنجا سرمایه‌گذاری نمی‌کنیم.
چیزی که مرا به امضای این یادداشت تفاهم ترغیب کرد، تضمین این بود که ایران سلاح هسته‌ای نخواهد داشت.
چیزی که برای من مهم است این است که ایران به هیچ شکلی سلاح هسته‌ای نداشته باشد.
اگر ایران به دنبال سلاح هسته ای برود جهنم به روی او گشوده خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66281" target="_blank">📅 13:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66280">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54b4a7171c.mp4?token=ET6_1x7sDG96ibB022v0iNX-r79AdDXiEGXXIvX2-050NecpZHl8y0TNow2a6cMQy2HWh5xj-GdPd_ogGdY5f5Vc7x-YAeBHMRjEOuh53aGQRExFUIn_BKD6HRy9emS8KmLqiKdf9A2PtKrDQzcEB-YDAynDDJTfD7UuzGX6yXTcQ_Rc1pDEvu7KEVnTDWsacwpoTWdXAwJ2e4buAJ2T0SAywMBX8eOnBIO5KJYILACLkMUC5ys-iYqy7DELqZ46-RYUihZ5_aMVpqE_gvQmyYvOEz2l-6_fGro9ZsbfJ2gcnmaJ-Pfyu-6jhUX4eirDpnOY6kaiKhGmWuaoPcBNPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54b4a7171c.mp4?token=ET6_1x7sDG96ibB022v0iNX-r79AdDXiEGXXIvX2-050NecpZHl8y0TNow2a6cMQy2HWh5xj-GdPd_ogGdY5f5Vc7x-YAeBHMRjEOuh53aGQRExFUIn_BKD6HRy9emS8KmLqiKdf9A2PtKrDQzcEB-YDAynDDJTfD7UuzGX6yXTcQ_Rc1pDEvu7KEVnTDWsacwpoTWdXAwJ2e4buAJ2T0SAywMBX8eOnBIO5KJYILACLkMUC5ys-iYqy7DELqZ46-RYUihZ5_aMVpqE_gvQmyYvOEz2l-6_fGro9ZsbfJ2gcnmaJ-Pfyu-6jhUX4eirDpnOY6kaiKhGmWuaoPcBNPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
هادی هوتیت، خبرنگار  پرس تی‌وی، وارد منطقه‌ای در جنوب لبنان شد که نیروهای ارتش اسرائیل هنوز در آنجا مشغول عملیات هستند. فیلم نشان می‌دهد که او در جریان این حادثه مورد اصابت ترکش قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66280" target="_blank">📅 13:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66279">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60b685347f.mp4?token=bsuAElJfSI0JOPUoxTT9MZfs_eqCMhVZSLnCYon7sgBiXD8F--1zCeuSmLPryr_bmo_XREKkV3X5r9L1rTlJ8yTczCini_JT9B9NVKXNKZ-UOeJzGupwTnci4YDVBYYkNroMu5kCUQZrAVcViezdT6if5e8zOvEvOQojNLuGgjh-nVrg9SZ2RQEd3ViiuqKLTDPBRQ2hNC8II8MCFcAA-mJQbMjepWZJyJ8TQQJRG4LvAerfuuofkPkHndBx-Ny6fujQrfsqJA7jw43tjgSP_TgjOLPBI8HZtJyKNknu5iErKg_JHhwd2mHiR9Szd3D580kJeytG3PKU0kPomnLHfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60b685347f.mp4?token=bsuAElJfSI0JOPUoxTT9MZfs_eqCMhVZSLnCYon7sgBiXD8F--1zCeuSmLPryr_bmo_XREKkV3X5r9L1rTlJ8yTczCini_JT9B9NVKXNKZ-UOeJzGupwTnci4YDVBYYkNroMu5kCUQZrAVcViezdT6if5e8zOvEvOQojNLuGgjh-nVrg9SZ2RQEd3ViiuqKLTDPBRQ2hNC8II8MCFcAA-mJQbMjepWZJyJ8TQQJRG4LvAerfuuofkPkHndBx-Ny6fujQrfsqJA7jw43tjgSP_TgjOLPBI8HZtJyKNknu5iErKg_JHhwd2mHiR9Szd3D580kJeytG3PKU0kPomnLHfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمدرضا شاه پهلوی مردی بود که دستش نمک نداشت
👑
.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66279" target="_blank">📅 12:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66278">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
عراقچی:
ما واشنگتن و اسرائیل را یک طرف این یادداشت تفاهم می‌دانیم، در حالی که ایران و حزب‌الله طرف دیگر را نمایندگی می‌کنند.
پایان جنگ در لبنان بخش جدایی‌ناپذیر پایان جنگ در ایران است و شامل خروج اسرائیل از خاک لبنان نیز می‌شود.
هرگونه حمله نظامی اسرائیل به لبنان و ادامه اشغال، نقض تفاهم‌نامه است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66278" target="_blank">📅 12:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66277">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d988cc6faa.mp4?token=kbz_Shmuq78nRQ0fCfj_bqphJmE42sco-ycBLfCZ7RR3z2fflrt0OrZTEwRl49n4UpYuNnwYRhHs6ZIfcxpmE6Qd4nfOIiK7kM_CINCHxuFkJtj5tuIZuDaKqwpa0wEpzw3eZRjfrzzzhX-3JVxHyzfzwt5cmkbFmZm73mrddf52BHBVl5rVsW06-m-5W0gPbr6wRlsLnjKWfSvWwN0be7QOJP7imBAwHMPDJ4voKJ1CTsO3xVLA_IDEoYAuNqcSjl0g9t4Qti4c5g7tRkxT9wPELTweA0Y3v6TdouRuO-W-9NaT1nLXJfdAn25Lqn9jUsVyfHpmyM9Dh72NS4sD9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d988cc6faa.mp4?token=kbz_Shmuq78nRQ0fCfj_bqphJmE42sco-ycBLfCZ7RR3z2fflrt0OrZTEwRl49n4UpYuNnwYRhHs6ZIfcxpmE6Qd4nfOIiK7kM_CINCHxuFkJtj5tuIZuDaKqwpa0wEpzw3eZRjfrzzzhX-3JVxHyzfzwt5cmkbFmZm73mrddf52BHBVl5rVsW06-m-5W0gPbr6wRlsLnjKWfSvWwN0be7QOJP7imBAwHMPDJ4voKJ1CTsO3xVLA_IDEoYAuNqcSjl0g9t4Qti4c5g7tRkxT9wPELTweA0Y3v6TdouRuO-W-9NaT1nLXJfdAn25Lqn9jUsVyfHpmyM9Dh72NS4sD9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایرانیان وطن پرست سنگ تموم گذاشتن و اینقد پرچم شیروخورشید زیاد بوده که میساکی فشاری شده و پرچم جمهوری اسلامی نشون میده میگه این پرچم ایرانه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66277" target="_blank">📅 11:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66276">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944350c2ea.mp4?token=J6kFrw5XgMuxBWc8rHrfEkTeb70IEeYwEcOlpOsg3IP7AbZa-qypTQk1RpG01cz2rjahMljoM4JOHEU8jFOuNac1on5p8BQKfRf-HEVJrqJAienlfM2LKC--7h57KXf39-AkIvhN9iTpNxNiNAMlulrDWCoPR44NQ69-GJeMRkbDqjbkDbTr-vJq4FDGVzFzGuL4V-4rl12QHcudZUcSyua3bDsscBPwjeX3ab28AxDGEmzFiS5cmVjrvQD06b0K4aHxgY1Y0mKUYsGiJDjfGsWE4VrMtyIISloTWycpg9_etpMdwlb1bE85SGZp1wO2WuS7b4Eytj83sraefEaKJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944350c2ea.mp4?token=J6kFrw5XgMuxBWc8rHrfEkTeb70IEeYwEcOlpOsg3IP7AbZa-qypTQk1RpG01cz2rjahMljoM4JOHEU8jFOuNac1on5p8BQKfRf-HEVJrqJAienlfM2LKC--7h57KXf39-AkIvhN9iTpNxNiNAMlulrDWCoPR44NQ69-GJeMRkbDqjbkDbTr-vJq4FDGVzFzGuL4V-4rl12QHcudZUcSyua3bDsscBPwjeX3ab28AxDGEmzFiS5cmVjrvQD06b0K4aHxgY1Y0mKUYsGiJDjfGsWE4VrMtyIISloTWycpg9_etpMdwlb1bE85SGZp1wO2WuS7b4Eytj83sraefEaKJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دلیل سود نکردن من تو بازار بعد چندسال
😂
.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66276" target="_blank">📅 10:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66275">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78c971246f.mp4?token=IYBiTprSUkFRoqCRyNNe-BgVsCmnQZUPXmQLgxH6xrU3TS9IC9C0kH1ku5LEV_HbvYP-eWN1VSjE127HFMhaYbVt9sbwZFgRcdyijGkyQHWEqKIMlO02ZyAD8MQACsd_xDI1YuEbsb8VFcjJl4Mbyon76LtvOmxbNh7cPbvuHc17oiGsLDUfwdYIKik4iHg_nEYELsTBIgDozKDTm45AYsdc7vKmreJIwybpDnHizHXKKlDkpu-yLhOrFcqIBNQdGut8hF3BmG_7M97fxcQqlziPAgFPp-W0rCdESXsz0ivpHgbtZvhHksw4jpytRCaB8FDrgCmEsuy9iCKjWgEQ6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78c971246f.mp4?token=IYBiTprSUkFRoqCRyNNe-BgVsCmnQZUPXmQLgxH6xrU3TS9IC9C0kH1ku5LEV_HbvYP-eWN1VSjE127HFMhaYbVt9sbwZFgRcdyijGkyQHWEqKIMlO02ZyAD8MQACsd_xDI1YuEbsb8VFcjJl4Mbyon76LtvOmxbNh7cPbvuHc17oiGsLDUfwdYIKik4iHg_nEYELsTBIgDozKDTm45AYsdc7vKmreJIwybpDnHizHXKKlDkpu-yLhOrFcqIBNQdGut8hF3BmG_7M97fxcQqlziPAgFPp-W0rCdESXsz0ivpHgbtZvhHksw4jpytRCaB8FDrgCmEsuy9iCKjWgEQ6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تصاویری از پالایشگاهی در حومه مسکو که در اثر حمله پهبادی اوکراین دچار آتش سوزی شده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66275" target="_blank">📅 10:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66274">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/696afa1a70.mp4?token=lgxnw23N0Y4Zieg4nAMW_-0nis5DV6Yba73lWn4znfHZjS0GSC2Z5Qo8pctuOtGZX1yzqKzdoLLJitD0_R96NEDr4_fWmIU7a7t6NStFW3e9s91LqiyewWayCVg5vvzpUaeHlkbrtIC59drW-826QMz4TDB-EEKYi0s2g-2D5IAfmnctB-TG_WEKVcDUgpmLJmkPt6uz7FZEJZy6P58ysDcnoma6qXsjwj3HOC9xTtfGDJPhF-E72oEKGVr_nomC7Eetbo4IsATjqt20atTu1-1aiC_Vax7TgBOjsn0FlkhLrrPHL3SXDZX4AEPiO6HiGB_dDw_c_ketgvwOdl4Mgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/696afa1a70.mp4?token=lgxnw23N0Y4Zieg4nAMW_-0nis5DV6Yba73lWn4znfHZjS0GSC2Z5Qo8pctuOtGZX1yzqKzdoLLJitD0_R96NEDr4_fWmIU7a7t6NStFW3e9s91LqiyewWayCVg5vvzpUaeHlkbrtIC59drW-826QMz4TDB-EEKYi0s2g-2D5IAfmnctB-TG_WEKVcDUgpmLJmkPt6uz7FZEJZy6P58ysDcnoma6qXsjwj3HOC9xTtfGDJPhF-E72oEKGVr_nomC7Eetbo4IsATjqt20atTu1-1aiC_Vax7TgBOjsn0FlkhLrrPHL3SXDZX4AEPiO6HiGB_dDw_c_ketgvwOdl4Mgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هو کردن هوادارن حاضر در ورزشگاه هنگام پخش شدن سرود تیم جمهوری اسلامی.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66274" target="_blank">📅 09:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66273">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44f96ea995.mp4?token=uHiawf_QtTfInDWhr16afut15syyvBCN1FS2sUM0EKdm4Lr3TDc3fKpcSMV7VfgCP-YwwfD5YxTEDXp25wBXk7wmbYCQf9U-4NUi5nJcpEUZAls5hn6PoAQsb9zMG2VW2evJFgOcz-r---Vp9WPkNOtpHSz7VQqZu4bIAieoJ-msFRvhkAJtlK_j5jwcA8TG4oTzxkdsvpc8OS6PnvTae8rBLGMNUAIBEeo0_A-XQHK5NfQhgQNTyxFlEPvSPMJ1dV0V5FAyjwlBVwcn_5Ruqbnbxs1JiWl8aGbC5O9ccs5YbI54QKx0oU1XpJYj5v2t3Kec4CPtOa-diEF7mHGPuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44f96ea995.mp4?token=uHiawf_QtTfInDWhr16afut15syyvBCN1FS2sUM0EKdm4Lr3TDc3fKpcSMV7VfgCP-YwwfD5YxTEDXp25wBXk7wmbYCQf9U-4NUi5nJcpEUZAls5hn6PoAQsb9zMG2VW2evJFgOcz-r---Vp9WPkNOtpHSz7VQqZu4bIAieoJ-msFRvhkAJtlK_j5jwcA8TG4oTzxkdsvpc8OS6PnvTae8rBLGMNUAIBEeo0_A-XQHK5NfQhgQNTyxFlEPvSPMJ1dV0V5FAyjwlBVwcn_5Ruqbnbxs1JiWl8aGbC5O9ccs5YbI54QKx0oU1XpJYj5v2t3Kec4CPtOa-diEF7mHGPuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ثابتی نماینده مجلس:
عراقچی نوچه و اراذل اوباش آمریکا در کشور است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66273" target="_blank">📅 09:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66272">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iaxoS4qGRuei7tSnzKWuiRsmmUh46ccMqMMGadS4Ww8iPH3fD6TFKIfLo3ENbxkd5yyWbJzktcGpy19-5h5TadOaIboP0FxQTa4qqr6M_w-g5mC516EVh-5d94pLYLQGbQvXFUKYn-QJ03haBAnNQ63SNih1F3vDlNMDeYhLG5bOpPmnXeBS43qCr0DMMU6Gtg-T_Wzw3mquhWSzOVJ9vAdub9QhXIJwRDXlYvTVD0jB4Dn7GXaWjr9Xy5_7YiF42bV5W8jx6rICQ8PBY5iZYKORbYoUkKazv1KdfIRYuFhUMLyfjXAMPjSDgPDt_xnBiGQ0DbRrRltDfshKIjThvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🏆
پایان‌بازی
🇳🇿
نیوزیلند
😀
-
😀
ایران
🇮🇷
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/66272" target="_blank">📅 06:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66266">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گل دوم محبی
#hjAly‌</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66266" target="_blank">📅 06:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66263">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🇳🇿
گل‌دوم نیوزیلند به منتخب ایران دقیقه ۵۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/66263" target="_blank">📅 05:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66258">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
سخنگوی قرارگاه خاتم‌الانبیا: گل زدن نیوزلند به ایران قطعا بی پاسخ نخواهد ماند
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/66258" target="_blank">📅 05:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66257">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پایان نیمه اول
فرزندان برحق وینتون روفرو ۱
کاکولد های گروهبان قندلی ۱
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/66257" target="_blank">📅 05:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66255">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یه حسی بم‌ می‌گه بازی مساوی تموم می‌شه
#hjAly‌</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66255" target="_blank">📅 05:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66254">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🏆
گل‌تساوی توسط رامین‌رضاییان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66254" target="_blank">📅 05:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66251">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6kcDlzGv69D-znqm52yqpRagD16z7D3cigTSc0nMdCuEpl5m45Nd6UzfJlwyKUzYk_XAzCVNGL3zGSyO86qr9N8FHXp7ZUlb2DYYkHquTSVHirmj7Zd3sjCT5J1JKEI3uhjRJflnLgvETq90eY-LAvuTi8Mic4eNhOVPcOTqAt3FngLwnmz1EOvvWJbBJiID8RlCWGAAi1Kk-dsDhz_yLG3TzlQ4AV5yw07tpZvdmW7FCI0eAacSYqJgNgTJds7X-p6SKXnnBE4mmAit45Z_1MB4I4px8CVaLoAQeN67PNFA69RG6q58RC_8EmAKc58yXH-M33uDniMUkStCrII2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظه بازگشایی تنگه بیرانوند
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66251" target="_blank">📅 05:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66248">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🇳🇿
گل‌اول نیوزیلند به منتخب قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66248" target="_blank">📅 04:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66244">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-poll">
<h4>📊 دوست دارین کدوم تیم ببره؟</h4>
<ul>
<li>✓ تیم منتخب امیرقلعه‌نویی🇮🇷</li>
<li>✓ تیم ملی نیوزلند🇳🇿</li>
</ul>
</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66244" target="_blank">📅 04:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66243">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQi7corMc9PC6xXM77VBpYSrNlnjzUyUhbothzVf--QMx5TdmIlkUBzINs0AASCSJdxM9j00fnaoeccEYsGHZn6SC7yi8rBgig8QsGK3bTQeWbpeYxl4Fuz4uepdpx5G0T6_46n_qndL-Yc4TA9lNY41qupyvK6msLyacd5zRTLwNxDqKEL8h869dC9LuP8sN19QBS6_uK9p2sKb65B2FIFQzWmC66TNLV8ni2Wer7BPmzJrIAUUHUtDq8LvxMMIUwH_3f_olBrslqHlsXU9_6FE8gqCrh764G29fMGjFdOV5BuXsI--BZ8Otjx8wRhIsqsWx2a4uO_WKDtQF3vx_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبل بازی
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66243" target="_blank">📅 03:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66242">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">حاج علی یکمی تحلیل کن</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66242" target="_blank">📅 03:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66241">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirhossein ؛)</strong></div>
<div class="tg-text">حاج علی یکمی تحلیل کن</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66241" target="_blank">📅 03:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66240">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇷</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66240" target="_blank">📅 03:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66239">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇷</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66239" target="_blank">📅 03:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66238">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QzVn1NkNy2KJSKnO9M0RcROFLUEtETJwQ5LBhVljag2C17a5_wYNcfbH7irIYKTFyqc0gZH8dQxFDLwzGdsHgYEfJbq5JOqi2kslCDr1Ra1nssveNHsE7JAST2AZ43Mk5rR7bnRoLq9H_xsdu7ebNCXY-xEfECv12gH6C5E2Da0lSc6UWBUdKvQDMH88Ycn2ry8MWfO_CwtP7oW7W6gwWuG0FesNC4HcutRacDuYjuEGEmyFyYM1lPHVXs8OZ_ysag8ymE0APIwS1ZEfZQXkket-u-bP1hcVlVV2AqQLvoALI1gjF6hR-LTcGP8LyGEDuEkNPjtZdixhUnUMH6wyoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
👌
تصویر تراز امشب:
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66238" target="_blank">📅 03:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66237">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
صحبت‌های ایرانیان مقیم آمریکا قبل ورود به استادیوم
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66237" target="_blank">📅 03:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66236">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3BvMnf-LMmSbdUG2MNRaJDfoubj0yhOEZsm35xKyDHhoIQgPXFWobje-Db_ztYdRGdPIQLikd54OqSWMcYU2sMK_QiC2rkMDHxuw3Rc9Mq-qkHrulhrJZDPdYCbTkYO3nvd7FxWjAgD0SP_UewDj1qTOWi8PbyN_DXvrM-JH9Wv-8x5j45aTkhbnnY-8d5icgvxSMihL5yVXpB6XJOGbFDvvK0YZzUsDeeIHTqHXZ7Khdf-3EtdxhfAe5HDb2BJ41jBJP296ib3Buast0dFDAOxw4RX3BnkS70R5bdYzQQq1QurSuEwkDgon04OedwQUhVJyK7r7uWkN2tGLL09uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی از اسمش مشخصه، باید برای ملت باشه، من نمی‌تونم رو این تیم، پسوند ملی بزارم، یه مشت آدم منفعت‌طلب جیر‌ه‌خورن که برای ۱۰ دلار بیشتر ناموسشونم در اختیار ج.ا می‌زارن همونطور که تو ۲۰۲۲ وقتی مردم داشتن کشته می‌شدن اینا دنبال حواله خودرو بودن.  آخرین باری…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66236" target="_blank">📅 03:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66234">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c366b2c0bb.mp4?token=mDbAEAWmsFhA_G5HpaxKWcdKpI0MAFhwrbalMegw-1F8VJmTNuzivrvMc5endQdeoMEgSF5KoMF_WCeQsHdmIVp0b299lC-uyBSVuOSG6N4Zmd7qLEJbvZLWEL219bDpStB_zWKC04JrZhIK5O43F_d3sCbxHSkY1LZguB99h75204b2RnTsg9xEm5Kq-orto3Y1f_UB0R3Kvt6r5rxiAulrXcGLtSMNHpbowgCMZ4g_93TaLNiQXeVSICuD-DPxLGXkPdYMNU7f_wt0_tIANyzBude6bUHyPNQyjMfAC01OuQThCbgfSFamXUBprI_rY5qt1Zzau0BChmZAL02jLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c366b2c0bb.mp4?token=mDbAEAWmsFhA_G5HpaxKWcdKpI0MAFhwrbalMegw-1F8VJmTNuzivrvMc5endQdeoMEgSF5KoMF_WCeQsHdmIVp0b299lC-uyBSVuOSG6N4Zmd7qLEJbvZLWEL219bDpStB_zWKC04JrZhIK5O43F_d3sCbxHSkY1LZguB99h75204b2RnTsg9xEm5Kq-orto3Y1f_UB0R3Kvt6r5rxiAulrXcGLtSMNHpbowgCMZ4g_93TaLNiQXeVSICuD-DPxLGXkPdYMNU7f_wt0_tIANyzBude6bUHyPNQyjMfAC01OuQThCbgfSFamXUBprI_rY5qt1Zzau0BChmZAL02jLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
تجمع هموطنان خارج از کشور مقابل ورزشگاه محل بازی تیم جمهوری اسلامی:
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66234" target="_blank">📅 02:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66232">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8cBqWevKFJl7O0_EIelvPhDeaksGkMTfki02B7MbpLXu4gP8dpEwOwmwj32n4cb43P1i8esKNDDHgKpDWAQlosXHRHf5XEUyAVcnHUcpUTkzdwZv5NH_nK7tGPZZy-YsAWyN6Dr-3HBIQ0DUFa2-HwZYbwomvUan1BmZ-czc0t0dD176J9gUpCiL2w7gsz6u-mJuYvcBM5P5dECw-f3qgAx4eUzmHfPRR39-N9aKJWCg0dGRCbWkpIJHLZF3zb9ERq9jWXL9u0yAPAkuz7ksfadsNCrFgVwe5WJwMxHSHugvodPPaQZo_x67sHCI1oVKJCovQUDdYqWW5ewvbEGJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی از اسمش مشخصه، باید برای ملت باشه، من نمی‌تونم رو این تیم، پسوند ملی بزارم، یه مشت آدم منفعت‌طلب جیر‌ه‌خورن که برای ۱۰ دلار بیشتر ناموسشونم در اختیار ج.ا می‌زارن همونطور که تو ۲۰۲۲ وقتی مردم داشتن کشته می‌شدن اینا دنبال حواله خودرو بودن.  آخرین باری…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66232" target="_blank">📅 02:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66231">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
#فوری
؛ترامپ:
ایران موافقت کرده که هرگز سلاح هسته ای نداشته باشد.
همچنین ادعایی مبنی بر اینکه واشنگتن مبلغ ۳۰۰میلیون دلار به ایران پرداخت میکند جعلی است و توسط دموکرات های احمق تبلیغ شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66231" target="_blank">📅 02:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66230">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
صف ایرانیان مقیم آمریکا برای دریافت تیشرت مخصوص ورود به استادیوم که تصاویر جاویدنامان انقلاب دی‌ماه روش حک شده  @News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66230" target="_blank">📅 02:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66229">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10adb291f.mp4?token=n6U97nk-XQ0hIrhFDQndmGO3Z1oU4X9ukIrFxFlr22aMzBiXLwXMuIdTfKq6752qS_Cl91aKuMqpJ0uD78X76XagREg9hzTNDnYUdVfV7akUyEzXDD9vpEhnfvfK_M2_n-W_7nw_h30StC6UxUQBn_C5Q3RIvaJ6UW9hcNG7Pe2sQfcIs1aUavEIAM6UtzQ20zzcZAOwAw6gKG2_f7ucvjjVIkUODkq9n4CImBlx3_O_TLge4dhETEDw8ZRU7bOdOGixsyp62PwW_x8sELXVeER5LdT4MNQNNpk156R5oIGsYDh1QFhnFDJvAViSuEeFjQyp0j9Ov2WUE7utdXqj4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10adb291f.mp4?token=n6U97nk-XQ0hIrhFDQndmGO3Z1oU4X9ukIrFxFlr22aMzBiXLwXMuIdTfKq6752qS_Cl91aKuMqpJ0uD78X76XagREg9hzTNDnYUdVfV7akUyEzXDD9vpEhnfvfK_M2_n-W_7nw_h30StC6UxUQBn_C5Q3RIvaJ6UW9hcNG7Pe2sQfcIs1aUavEIAM6UtzQ20zzcZAOwAw6gKG2_f7ucvjjVIkUODkq9n4CImBlx3_O_TLge4dhETEDw8ZRU7bOdOGixsyp62PwW_x8sELXVeER5LdT4MNQNNpk156R5oIGsYDh1QFhnFDJvAViSuEeFjQyp0j9Ov2WUE7utdXqj4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
صف ایرانیان مقیم آمریکا برای دریافت تیشرت مخصوص ورود به استادیوم که تصاویر جاویدنامان انقلاب دی‌ماه روش حک شده
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66229" target="_blank">📅 02:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66228">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tid66OSoo0x6t_McUx8bC9GX08Pd8gfWwq_xQOHiPlpe1fQd54YCKiNp6fO3BLZLFouLcAo5OFSvgju_lPqEFJwYQNhT_nkes-eT-WwwB74ojbOb3iYRLcYl_ja27cvIhOzILLSvQjF03k81UWOZU1BtHxcdq-eBbfj6m_dAy-IKyjkRFH9_3po9zqAkCMe_HsHh2LBRenT1XKjnUGPaeYJOpmORoj_0gEvKvANnHNqSkrDkHFNNWAcWy6egbo6emlAbDriF-QVERZ7OEcmUb0kOuPVn7LkfFZiw9F0pzbs81WGWJRtwMgcw4wD9Hzh0PrndfEjBx2hsTb8wzBel3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
رتکلیف، مدیر سازمان سیا، به رئیس جمهور ترامپ و دیگر مقامات گفت که اطلاعات جمع‌آوری‌شده توسط ایالات متحده، تردیدهای جدی در مورد تمایل ایران به دادن امتیازات هسته‌ای مورد نظر ایالات متحده در هرگونه توافق نهایی ایجاد کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66228" target="_blank">📅 02:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66227">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTYw8UQc7ZTuM7C_zZppL6aM3Wyn8hiDV21hnXjv5zkEXIHugMqU-uYDeJ4Hip2UNUI94Jpotd5Ng-qK91eQ871MVKNJSVAnKofd7KMBgb4grhlafQ0sGYG4Gy9E7a8IKUi90x41ZmV10xaSeysfn0A5TmHi-Poigon-1pORu4rMGp8c8-3u1E5E1pqthhimAq9NB1t0dMOmhD1fxztgC1BaZGK3hLmAyCZizveDslF8RS-rnfY0VaPMxPbMJNgsEKFYnv-vLPx2DLdoEGGIpB5Az4tGosDsZ_DjocbDF0gYXnhlsnPh4Ey6Y5qRkfBRiRLRka8brXHYxk-uqbFjTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فاکس نیوز:
نیروی هوایی ایالات متحده روز دوشنبه اعلام کرد که معتقد است هشت خدمه در پی سقوط یک بمب‌افکن B-52 اندکی پس از برخاستن در پایگاه نیروی هوایی ادواردز در کالیفرنیا کشته شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66227" target="_blank">📅 02:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66226">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‼️
ونس به سی‌ان‌ان:
یادداشت تفاهم با ایران حدود یک صفحه و نیم است و به همین دلیل یک سند عمومی محسوب می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66226" target="_blank">📅 01:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66225">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c31d4a9328.mp4?token=q_ggYiSBWGJxIc2bOMWsFm3CeYfmG-l69QVEfNTPjbMe8iUieHKHoicV4OP8tmRtFI-WkYCh3iuNtXZwwddXV3ePxSTacSOLXDJ4NQ7Zj3q7kZnP8qRztWM1xDHzyx0MguvXHsYLD9Te6Jq5Jkm5VKfDmmnyuek40rkApWMN27nPO-S4Ug2bRhiqn2a-z_mp9esXL0mm4mgTCTxqivMCI7xjSfCvqHlWOykLIwdYxakIX9u9xZ4nzJcgHRCLThJWbqdRf1z7eio5955oWQkyxlq7FqGrzWJ0IDy-EICeXyi-J0VIGMaGu68rhGr9s-c8d_XerTSlKfWtNdcAcYc0QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c31d4a9328.mp4?token=q_ggYiSBWGJxIc2bOMWsFm3CeYfmG-l69QVEfNTPjbMe8iUieHKHoicV4OP8tmRtFI-WkYCh3iuNtXZwwddXV3ePxSTacSOLXDJ4NQ7Zj3q7kZnP8qRztWM1xDHzyx0MguvXHsYLD9Te6Jq5Jkm5VKfDmmnyuek40rkApWMN27nPO-S4Ug2bRhiqn2a-z_mp9esXL0mm4mgTCTxqivMCI7xjSfCvqHlWOykLIwdYxakIX9u9xZ4nzJcgHRCLThJWbqdRf1z7eio5955oWQkyxlq7FqGrzWJ0IDy-EICeXyi-J0VIGMaGu68rhGr9s-c8d_XerTSlKfWtNdcAcYc0QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه ای خطاب به قالیباف و عراقچی
🤣
:
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66225" target="_blank">📅 01:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66224">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b930a8766.mp4?token=OcGOX4tvmflqKP_K52_b1OoAI_hZOg4X4gYjzN6HLz54ySllCk-GVwY4t_brNCdExDiHF16btTAl2TiYhfYLC7JpU3mAiYJIpuI2EOzSwerjjUdOJvlui7m-zzn0I_dIKz0u3EvhJByvTZ8XChKKWC9M5VvxhQrWHZH37zbIo50ahjg2cktCcd9R4DaEt_Agea0ERjiWpTwvV0DiKNIAZwLUlO4OQD2MOODameup7FGWc7ujcNiBQWooTgFT8avrkw6hjA5YDVAhGj6CO7LSjGunoAuY5DlcrAf-K_PLO6AOGuCX3SPU0PvnBbNwZh67EHCPHMDP98GcQ1mW7EdJXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b930a8766.mp4?token=OcGOX4tvmflqKP_K52_b1OoAI_hZOg4X4gYjzN6HLz54ySllCk-GVwY4t_brNCdExDiHF16btTAl2TiYhfYLC7JpU3mAiYJIpuI2EOzSwerjjUdOJvlui7m-zzn0I_dIKz0u3EvhJByvTZ8XChKKWC9M5VvxhQrWHZH37zbIo50ahjg2cktCcd9R4DaEt_Agea0ERjiWpTwvV0DiKNIAZwLUlO4OQD2MOODameup7FGWc7ujcNiBQWooTgFT8avrkw6hjA5YDVAhGj6CO7LSjGunoAuY5DlcrAf-K_PLO6AOGuCX3SPU0PvnBbNwZh67EHCPHMDP98GcQ1mW7EdJXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حرف های متناقض اسماعیل قاآنی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66224" target="_blank">📅 00:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66223">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66223" target="_blank">📅 00:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66221">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromProxy MTProto | پروکسی(|•𝓗𝓸𝓼𝓼𝓮𝓲𝓷🥀•|)</strong></div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66221" target="_blank">📅 00:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66220">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‼️
قاآنی فرمانده نیروی قدس سپاه پاسداران:
هیچ کس نمی‌تواند در مقابل حزب‌الله در لبنان بایستد و هر آنچه از حزب‌الله در لبنان دیده‌اید، تنها نوک کوه یخ است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66220" target="_blank">📅 00:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66219">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2752783b15.mp4?token=Kme5mBmb0A26joX-1wo03AFqqFAGJxP0CiLsvwpc5EUrVUFfHwdaGW20d5E9FJFv6Kh8E9iwGp6l5QLT3J8kaPKMmgo1OsRukIF9vYDviJ9Q_3saVxedGnTdMSX1hSFpdVPl4N1Km09TZkBpvvCy07i2R76F04k5I8419qXsjnO9Ay3EwDZhTudkRZ4Pvzm9IgfAUx7GH8ujaUqGMs2h6s_aJ2Awnajzaf4W9UPy0hC8KiTiz3K8ZhGdBjmwyZPtlluDk4BQ-9_QAPvTfT95L7Z5k0IdFFMsJDRig6vyNHkeLlPRp8YTj90ejNVFMaRWU0PKY-BXshKMhsz_qRqxVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2752783b15.mp4?token=Kme5mBmb0A26joX-1wo03AFqqFAGJxP0CiLsvwpc5EUrVUFfHwdaGW20d5E9FJFv6Kh8E9iwGp6l5QLT3J8kaPKMmgo1OsRukIF9vYDviJ9Q_3saVxedGnTdMSX1hSFpdVPl4N1Km09TZkBpvvCy07i2R76F04k5I8419qXsjnO9Ay3EwDZhTudkRZ4Pvzm9IgfAUx7GH8ujaUqGMs2h6s_aJ2Awnajzaf4W9UPy0hC8KiTiz3K8ZhGdBjmwyZPtlluDk4BQ-9_QAPvTfT95L7Z5k0IdFFMsJDRig6vyNHkeLlPRp8YTj90ejNVFMaRWU0PKY-BXshKMhsz_qRqxVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
شبیه سازی سیستم عوارضی تنگه هرمز:
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66219" target="_blank">📅 00:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66218">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f287535d76.mp4?token=h_3RLJX8gVs57koiIErQybMmi1mxUuoN9z0Li_G9fmm88zjoVEis2NCgXt_dqMpYk91fdP9JwDcxm7aKiAoxbnwIgwvrytUn1xquGEgX8JMA1vVaKgM7q0wvBRIPaFVrcZvi8YchD1u4sQlSqNJF-IdURo8Y1efwHB0Ch-z3dxBbWBULZfNo4EnjW-XqZ9eFXWDTuAEXk8IK5g0K4e0tVUNDfCm0D5wLK4_XwXbWrArLKskC6q--dzLu-Tz9sZUnifi7J9znSfJ_gwHbolQuygkW3i175pJjfbqpGagNCI1luvpWqOHwCWOkN2-LMVFFlgxgTKXAxETx-KyKjIQ3jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f287535d76.mp4?token=h_3RLJX8gVs57koiIErQybMmi1mxUuoN9z0Li_G9fmm88zjoVEis2NCgXt_dqMpYk91fdP9JwDcxm7aKiAoxbnwIgwvrytUn1xquGEgX8JMA1vVaKgM7q0wvBRIPaFVrcZvi8YchD1u4sQlSqNJF-IdURo8Y1efwHB0Ch-z3dxBbWBULZfNo4EnjW-XqZ9eFXWDTuAEXk8IK5g0K4e0tVUNDfCm0D5wLK4_XwXbWrArLKskC6q--dzLu-Tz9sZUnifi7J9znSfJ_gwHbolQuygkW3i175pJjfbqpGagNCI1luvpWqOHwCWOkN2-LMVFFlgxgTKXAxETx-KyKjIQ3jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عراقچی:
جمعه در سوئیس تفاهم امضا می‌شود و پس از آن اولین دور مذاکرات بعدی را خواهیم داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66218" target="_blank">📅 23:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66217">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">تو فاک بت یجوری وین میدن انگار بت زدن ساده ترین کار دنیاست
🔥
از جام جهانی تا تنیس های کصشر دنیا !  هیچ فوتبال و ورزشی و از دست گروه انالیز حرفه ای ما در فاک بت در نمیره !
💵
@FutballFuckBet
💵
@FutballFuckBet
💵
@FutballFuckBet</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66217" target="_blank">📅 23:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66216">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmkn6k0dOZ1L4U3NeAiCMUlFdvisdCKc4PgiwOYcjDK4Q5OIiwPdQ3zV6Zlz4w9rsOr_AsrfTv5DWO4b_sBedl2VYzFTgKZHXGLp7GMHuglsUJ1A6Hn8NtUFH091uGj-J5XtPgvLsrLZqm-6NpZzl_a7HBwp_aZ68dMi5aS5916foqLmWnVNFUAJ6GRbBJGE2z2Il3rg5EYiwFe4s-7SfkHAmDW2j7pZRKwkRo3DBiKs2uP_RyXaVyNB6XfndPzQ_maR3Pno-uC6-CHP_L2lUOS_uCxF5TEqqPgUsLuViax9JyU9sn-k8_Jdguc5Wk4xodRqyWpdqGkeWB0SEHkU8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو فاک بت یجوری وین میدن انگار بت زدن ساده ترین کار دنیاست
🔥
از جام جهانی تا تنیس های کصشر دنیا !
هیچ فوتبال و ورزشی و از دست گروه انالیز حرفه ای ما در فاک بت در نمیره !
💵
@FutballFuckBet
💵
@FutballFuckBet
💵
@FutballFuckBet</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66216" target="_blank">📅 23:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66213">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qoWa3FbtGd5ZjhwwFU0b-RLDk9k9DO7ADdQg6rRN_il8uMPv7XO2WODwxsYS728UodLipRdRSbhTz6Lu7T20xU0viaLIpYG39bIruMXbwqnJ_Z2wyGPTo_mJVMGDCBdBUEtmibhUcO95NFlObnBSeEHp4kngnGkl2PHeFxYO9Jm_C7gZezIxeMA4P_5QxXX599ywiKs0hRYjTlrxWZhu5IA6JqSjvWCEc7dQUfBX53UQlrZx69f23KH00vkQsVV4x6mkBXkAKvu5tYVuwNOi-YnfyS5hGyqVMFvjCPt51Vgu6onAbDTEWelujhuuxZM6ma3XguBSYj3WFSjWrB7F7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m4I2JJlI8ytia3oKPXOPeEE6igWLBW52PrAIfbrEfz2Oh2AHkfJgmh0mlKUB_i7Rh6WBIAguw3H8IFe1oU2L1H1WoRfHNci1Bf1RZdV1UZCIw7ZVJ9UmAP9WmYLGG_GQblXjWE-_TJ7ElWqDfEcts6c8tmstHhU9iP0BU6fbrNqbjwLzBQTU4vVd6nK2UzfXTClmUcYd7PWwKPIVfoTCOGOYENLKxwnW--TV4YY-FaM6mAzbItmNF-Ht83n3RUARtcJXYDJISprQoRmFZaXcDURRAk5LMOOSMBkcxrYxVGykVQ3z0iqGw9ZRkrGpdDDX1NTjWPNuGjmSWUBqCRMtsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df8fefe1cb.mp4?token=nwQgPQK-DbGsshq420n03mDIxNFPd17qNO7nfEJFTFUiC1FfHdd4JQyQjEra0bv49tQRCXBG4jTpBLhbl3HzD8Oyk9Ta5TUwNB2rrIPSMGN5zMWna1-1e3vHZWvyY2capnzp3FZFpnwzHEGnxsVinGassHiKYbDpQhXUdm1-H9Afea4vsOzsTh_Ad_5CGQ4EVioNCKW2MxyDDC0v5ZXsCEctZYB_h2o1XtTWLgJzz5A-t-iVcPq0qW1kr8n-OUvt9YWgQlR0GhYlQgsTMmx_9VlYsC__7Mi8R3LiHWPdwxysQ0HaGqqX5OKGynNcp9ykrRzurOtP8g4p6Sjw9uNqTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df8fefe1cb.mp4?token=nwQgPQK-DbGsshq420n03mDIxNFPd17qNO7nfEJFTFUiC1FfHdd4JQyQjEra0bv49tQRCXBG4jTpBLhbl3HzD8Oyk9Ta5TUwNB2rrIPSMGN5zMWna1-1e3vHZWvyY2capnzp3FZFpnwzHEGnxsVinGassHiKYbDpQhXUdm1-H9Afea4vsOzsTh_Ad_5CGQ4EVioNCKW2MxyDDC0v5ZXsCEctZYB_h2o1XtTWLgJzz5A-t-iVcPq0qW1kr8n-OUvt9YWgQlR0GhYlQgsTMmx_9VlYsC__7Mi8R3LiHWPdwxysQ0HaGqqX5OKGynNcp9ykrRzurOtP8g4p6Sjw9uNqTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گزارش‌ها از سقوط یک بمب‌افکن استراتژیک B-52 آمریکا در کالیفرنیا خبر میدن.
این بمب‌افکن دقایقی پس از برخاستن از پایگاه هوایی ادواردز دچار سانحه و سقوط شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66213" target="_blank">📅 23:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66212">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMain Online پشتیبانی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVXFXfrtpQxolMP0gbrCCAoG57n4TbjDL-jZ37uvGhqgzrxuLWqYhPNz9LoUdmvuByMEt8S-yboQhMoH6CEGyPaRAq3WNK66z-ucL4WPZ1rZpACHvXBB7z3WcCMUenw0tvssgl3tt4tBHG8QG6YGwZLmWcwOeiJfjoRz313l8Fr7l-LEptnUHnWqYawf3hQ2GfVCLVqt_nYAwdPUPynMTVHieHHt6KwtrS9G_DCryJCX_ZrvHKWx4-uaRhF97h9daCFB72ntHeGhOwj4NJ-4M6nP40Y4JU2CK6LrbUe9D9SR2bP_Q0vuQ7r_XM90B5uhIyrGn_MEIElghSU1NsZ8yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فیلترشکن فقط گیگی ۵ هزار تومان
✅
👥
| بدون محدودیت کاربر 999+ نفر
🔥
| بالاترین کیفیت یعنی تانل شده
🎁
| کد تخفیف : 50
▫️
5 گیگ 25 هزار تومان
▫️
10 گیگ 50 هزار تومان
▫️
15 گیگ 75 هزار تومان
▫️
20 گیگ 100 هزار تومان
▫️
30 گیگ 150 هزار تومان
▫️
40 گیگ 200 هزار تومان
▫️
50 گیگ 250 هزار تومان
⚠️
| تنها راه خرید مراجعه به ربات
🤖
| ربات :
@YOUPINGROBOT
⚡️
| ارزون ترین قیمت بالاترین کیفیت</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66212" target="_blank">📅 23:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66211">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/007bf57d46.mp4?token=YRPe9o9D_MWs2Uuk5g6vaDi6_-kRy2TPjZSYz6gkziC5x_ojGa5NNKhAaUSUjNQizVrX4L6jrLc-4pt0dqOl1Jg8vTx5LLeozEJ2mGWRl2wrzGkZxcIvddb4kYMq3dMI2E5TL_CeayNvNkRP3I4L6orowxSDJ3JZsHrCKsYJQ7pUJZKGZ8_HTkWd-SvqirMXG9Ljy989zE15KBmwyUNmhBCtXa8UxkJcIT_ZzluvyqEImtogZdHpg0wtTowJQzvvBgE69u2LP2S-Gl-RRx71ud70E2zWHNubxvPE3EpJ2za7gnDA3elDIRVv8q6Sgv-urHzl2Y7v2F_psNQWcs4ErhriKmvxV4SVxcg2vhmHqDdFwBTpCuvlfp5ZmNxJdaExNsILK0d3RDChg3hAxI-1-Ao0-2i8ynJkKMuJr4R795-44aNBkI6i5BchjDYLm-Oe5qwQcP0GJsGp51M7HnKErXUvBBXOHMUtZM7EA2XoVhxAjIjjR5I6uXGFwng7pQI08XEWD7Y9HxQZJSBXyBAX0WYuMg042A6-hYq0t5C7aokoiT4hW7knX5sF79pNDKLt8baZCeVIk_mPXhS7zj9shiVDWtx8_ZZyNmD08xwm77HbMhmlFgqQXkja_pSKw8pwYkJQOeQSd3qf1F191K0Vk2sAT8n4YoG7qTjU_jHi928" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/007bf57d46.mp4?token=YRPe9o9D_MWs2Uuk5g6vaDi6_-kRy2TPjZSYz6gkziC5x_ojGa5NNKhAaUSUjNQizVrX4L6jrLc-4pt0dqOl1Jg8vTx5LLeozEJ2mGWRl2wrzGkZxcIvddb4kYMq3dMI2E5TL_CeayNvNkRP3I4L6orowxSDJ3JZsHrCKsYJQ7pUJZKGZ8_HTkWd-SvqirMXG9Ljy989zE15KBmwyUNmhBCtXa8UxkJcIT_ZzluvyqEImtogZdHpg0wtTowJQzvvBgE69u2LP2S-Gl-RRx71ud70E2zWHNubxvPE3EpJ2za7gnDA3elDIRVv8q6Sgv-urHzl2Y7v2F_psNQWcs4ErhriKmvxV4SVxcg2vhmHqDdFwBTpCuvlfp5ZmNxJdaExNsILK0d3RDChg3hAxI-1-Ao0-2i8ynJkKMuJr4R795-44aNBkI6i5BchjDYLm-Oe5qwQcP0GJsGp51M7HnKErXUvBBXOHMUtZM7EA2XoVhxAjIjjR5I6uXGFwng7pQI08XEWD7Y9HxQZJSBXyBAX0WYuMg042A6-hYq0t5C7aokoiT4hW7knX5sF79pNDKLt8baZCeVIk_mPXhS7zj9shiVDWtx8_ZZyNmD08xwm77HbMhmlFgqQXkja_pSKw8pwYkJQOeQSd3qf1F191K0Vk2sAT8n4YoG7qTjU_jHi928" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😔
مصاحبه با رکورددار عمل جراحی در ایران: بالای ده میلیارد خرج عمل کردم که همشو دوست پسرم میداد!
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66211" target="_blank">📅 23:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66210">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64b5122b70.mp4?token=Bn_uwh3epX4_OTKVyoy3qDUvMp4y6L6gtE26u8mzPCn6lQ0a-tUujydKK3wrYQLOKevkK5zNzYeUQl2FfberRcstyMaw3xBuBolTTPiDzR6B0n2kdXMNBkyI_rVyPyIAAOG6OHUulSRpxUit0HIKn--v3Fi51flHZnK1IYCU3QsmndGLxCk69VP92mkSRTFU8B08rQrVqDy2KyW0tB57XlFjfTZUxVYQnpjmZUKgs--xBnfdiAh-QrU6DLPDNAn89P-75O8r7eU7KGTxBe9QuywRSvb6ElqgWacBfnUQ4BpR6RtAK5yM-H_xODqe6IVlpbIf1Hk04OqM4XQY_Nzu6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64b5122b70.mp4?token=Bn_uwh3epX4_OTKVyoy3qDUvMp4y6L6gtE26u8mzPCn6lQ0a-tUujydKK3wrYQLOKevkK5zNzYeUQl2FfberRcstyMaw3xBuBolTTPiDzR6B0n2kdXMNBkyI_rVyPyIAAOG6OHUulSRpxUit0HIKn--v3Fi51flHZnK1IYCU3QsmndGLxCk69VP92mkSRTFU8B08rQrVqDy2KyW0tB57XlFjfTZUxVYQnpjmZUKgs--xBnfdiAh-QrU6DLPDNAn89P-75O8r7eU7KGTxBe9QuywRSvb6ElqgWacBfnUQ4BpR6RtAK5yM-H_xODqe6IVlpbIf1Hk04OqM4XQY_Nzu6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ پای تلفن به دستیار نتانیاهو:
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66210" target="_blank">📅 23:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66209">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">این BISS کد جدید شبکه سه و ورزش رو Starsat چیه شبای اول جام جهانی اوکی بود الان پریده! دایرکت بدین  #hjAly</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66209" target="_blank">📅 22:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66208">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏
🚨
🚨
نتانیاهو برای استقلال نظامی ارتش اسرائیل بودجه دیوانه کننده ۱۲۱ میلیارد دلاری اختصاص داد!
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66208" target="_blank">📅 22:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66207">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">این BISS کد جدید شبکه سه و ورزش رو Starsat چیه شبای اول جام جهانی اوکی بود الان پریده! دایرکت بدین
#hjAly</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66207" target="_blank">📅 22:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66206">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bb332cca2.mp4?token=TJvzRSwL2Ac97rcSRZxcb7B9CKPqnpQu6uGoI4_h1p7YMfkJdlpNtfIi-YB1TjDlDvyzcoEgb7AweRPZBLfCklFyuBT0CBZBEliPdLRbaRD5PSxXs-kPei2i45Zy8xlCFJN6sCTxM1_sNtsUY7eVXaJsdvy-godqOLsnQ_ll7G3cpWLeRch1tOgm1PdQv48cYOoTouO99825EzmU9mE3p3n5t5YABN__lTrY0jyrOokVfwhyChi7eIdfRGiS-osPrFGzBjUbY2xRz9l1PYs7dAIGYHOngJuNoy4XAmrW3NeokiQzpGmsi2j2BO_VD9BhIcZNFfgeS5kbdImysWMXAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bb332cca2.mp4?token=TJvzRSwL2Ac97rcSRZxcb7B9CKPqnpQu6uGoI4_h1p7YMfkJdlpNtfIi-YB1TjDlDvyzcoEgb7AweRPZBLfCklFyuBT0CBZBEliPdLRbaRD5PSxXs-kPei2i45Zy8xlCFJN6sCTxM1_sNtsUY7eVXaJsdvy-godqOLsnQ_ll7G3cpWLeRch1tOgm1PdQv48cYOoTouO99825EzmU9mE3p3n5t5YABN__lTrY0jyrOokVfwhyChi7eIdfRGiS-osPrFGzBjUbY2xRz9l1PYs7dAIGYHOngJuNoy4XAmrW3NeokiQzpGmsi2j2BO_VD9BhIcZNFfgeS5kbdImysWMXAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
خبرنگار: چرا ترامپ مانند بایدن عمل کرد و چنین توافقی را امضا کرد؟
نتانیاهو: من این مقایسه را نمی‌کنم.
ما هنوز نمی‌دانیم توافق چه خواهد بود.
همچنین نتانیاهو درباره انتخابات گفت که قصد دارم نامزد شوم و همچنین قصد پیروز شدن را دارم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66206" target="_blank">📅 22:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66205">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
نتانیاهو درباره توافق ایران ترامپ:
این توافق توسط ایالات متحده، توسط رئیس جمهور ایالات متحده، حاصل شده است و او معتقد است که می‌تواند هم به نظارت و هم به برچیدن برنامه هسته‌ای دست یابد.
گفتم: این تصمیم اوست. تکرار می‌کنم: این تصمیم اوست. او آن را رهبری می‌کند.
البته، من نظراتم را در گفتگوهای مختلف بیان کردم.
از سوی دیگر، گفتم که ما منافع خودمان را داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66205" target="_blank">📅 22:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66204">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
ما ضیف، هنیه و بسیاری از رهبران حماس را کشتیم ، تقریباً همه آنها را.
فکر می‌کنم هنوز یک نفر باقی مانده است؛ او هم کشته خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66204" target="_blank">📅 22:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66203">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
در ایالات متحده، می‌گویند که رئیس جمهور ترامپ هر کاری را که من بخواهم انجام می‌دهد، و در اسرائیل، برعکس می‌گویند که من هر کاری را که او بخواهد انجام می‌دهم. بنابراین این درست نیست، و این درست نیست.
این رابطه بین شرکایی است که مدت‌هاست یکدیگر را می‌شناسند.
بسیاری از اوقات ما موافقیم؛ گاهی اوقات نیز مخالفیم. این در بهترین خانواده‌ها اتفاق می‌افتد
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66203" target="_blank">📅 22:19 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
