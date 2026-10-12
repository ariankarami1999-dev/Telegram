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
<img src="https://cdn4.telesco.pe/file/c6jDA7oCxujPTFyqkEY6q03e8wj-kl6GB-RqIqMEdA9XHrEfTlWyt0TGwvccepL_c3_jemkPbHlC8j-ConfxZhvJLAV_yV0k3MzEL5woUYgVTbD3sJMRS9eVGtkVQupyObw-K5KEMKJPdA5M4xz3GYBM4VMHBZGKDaLpFIm27zv3lcCO0HaXkzyOSH1mbqNS8ZFkxGOAhr9CeZQkkbQJ59Zruni6dOYUyMZ318RKQ1DODnmS0npVUKS0yOVuwj_i6TY2GKub8n_OqXL9M02yXateqYZQUhD-scbw1Mzssl3EHnzYLLQBZjKEHKgPiQQiPpzizUPQ_jWb1YeQAmNkLA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 495K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 11:11:52</div>
<hr>

<div class="tg-post" id="msg-25473">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">این آقا امروز به‌خاطر جوابی که در مناظره‌اش با نامزد دموکراتها داد ستاره شده. یعنی حتی حریفش سناتور بوکر دموکرات هم چنانکه در آخر این کلیپ می‌بینید مات و مبهوت ماند و میگوید «واو»
سناتور کوری بوکر (دموکرات)
: اگر رئیس‌جمهور با شما تماس بگیرد و بگوید: «هر کاری بخواهی برایت انجام می‌دهم؛ در مورد ایران چه کار کنم؟» پاسخ شما چیست؟
جاستین مورفی، نامزد جمهوری‌خواه مجلس سنای آمریکا از نیوجرسی
: کار را تمام کنید. این جنگ را به شکلی مثبت به پایان برسانید. نمی‌توانیم تا نیمه راه پیش برویم و بعد تصمیم بگیریم که دیگر نمی‌خواهیم این کار را ادامه دهیم.سپاه پاسداران سازمانی تروریستی و افراطی است که مردم ایران را از تاریخ و زندگی شایسته محروم کرده و با قتل، تجاوز، شکنجه، ترور و حمایت از تروریسم، به‌ویژه در خاورمیانه، به مردم منطقه و جهان آسیب رسانده است. من در کودکی شاهد حمله تروریست‌های اسلام‌گرای افراطی به سفارت آمریکا در نوامبر ۱۹۷۹ و گروگان‌گیری ۵۲ آمریکایی به مدت ۴۴۴ روز بودم. از آن زمان، سپاه جز صدور تروریسم، خشونت و سرکوب کاری نکرده است. چهار دهه کافی است؛ مردم ایران به‌اندازه کافی رنج کشیده‌اند و وقت آن رسیده که این وضعیت پایان یابد.
و من به آقای رئیس‌جمهور می‌گویم:
کلاه کابویی‌تان را بر سر بگذارید، وارد میدان شوید، یه درِکونی حسابی به آنها بزنید و این کار را تمام کنید؛ آن هم به‌درستی!
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/withyashar/25473" target="_blank">📅 11:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25472">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">افشاگر تحرکات هواپیماهای عملیات ویژه آمریکا: خبر بد برای جمهوری اسلامی؛ ادعا شده چند فروند هواپیمای عملیات ویژه MC-130J Commando II آمریکا، معروف به «شوالیه‌های خاموش»، صبح امروز در فرودگاهی در مشاهده شده‌اند. نیروی هوایی آمریکا تنها ۱۰ فروند از این هواپیماها را در اختیار دارد. این هواپیماها قرار بود در آوریل ۲۰۲۶ در مأموریتی محرمانه برای بازیابی و انتقال محموله اورانیوم غنی‌شده ایران، با نفوذ به عمق خاک ایران و فرود در شهرهای شهرضا و کوشک نصرت، مشارکت کنند. این هواپیماها به رادار پیشرفته پرواز در ارتفاع پایین مجهز هستند و احتمال داده شده است که به‌زودی در نزدیکی ایران مستقر شوند؛ با این حال، وی تأکید کرد که محل فعلی این هواپیماها و مقصدشان را فاش نخواهد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/withyashar/25472" target="_blank">📅 10:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25471">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اسحاق هرتزوگ، رئیس‌جمهور اسرائیل، در کنفرانس «مردم کشور» که به میزبانی «وای‌نت» (Ynet) و روزنامه «یدیعوت آحارونوت» برگزار شد، اظهار داشت که اگر انتخابات به نتیجه‌ای قاطع منجر نشود، «تمام تلاش خود را برای جلوگیری از تکرار انتخابات به کار خواهم بست. باید بدانیم که چالش‌های ملی ما بسیار عظیم هستند.»
@WarRoom</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/withyashar/25471" target="_blank">📅 10:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25470">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">روزنامه ژاپنی «آساهی شیمبون» گزارش داد: ناو هواپیمابر هسته‌ای که قرار است از «یوکوسوکا» در ژاپن بازدید کند، ناو «یو‌اس‌اس تئودور روزولت» (CVN-71) و گروه ضربت همراه آن است.
این ناو احتمالاً طی ۵ تا ۶ روز آینده، یعنی در بازه زمانی ۱۵ تا ۲۰ اکتبر، وارد منطقه خواهد شد.
پیش‌تر در مطلبی که در ادامه آمده است، تاریخ ورود این ناو بین ۱۰ تا ۱۴ اکتبر اعلام شده بود؛ اما اکنون به دلیل شرایط نامساعد جوی ناشی از طوفان‌های «نولو» (Nolo) و «کوگوما» (Koguma)، ورود آن با تأخیر مواجه شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/withyashar/25470" target="_blank">📅 09:38 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25469">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/300e6c2aa9.mp4?token=vMs-fXygc-ZF63mGD9-CkHNhnrvkv2yFTfGUKy2wPXIRXgXLGw_Uvyr0D9ar8wAjEspxjb7gC92uSVcRC5h1i2gTQnRzswNk7Aq4sDbZF4Rca_iDzFYdQTxEoJOP39YcWBoYKOHpPJVvJ1qQfZphhu83WyaEj1JLfpj45cvT9cphUnbvBpcej4tXR5C9xtG1VuCzWqLHFaWucNp9e0KW1fBU5AleucPnu1k3v-flS7gAgRPMP5L_J9dj0BQOzg4w1rxW9SXA22aCrjECDoWzQJqK6KDQXgJHawbkwxAyI70ayRKXzyqPRjzzqFDZuJh2dzecPyBHF3hrwA-VtOFoRzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/300e6c2aa9.mp4?token=vMs-fXygc-ZF63mGD9-CkHNhnrvkv2yFTfGUKy2wPXIRXgXLGw_Uvyr0D9ar8wAjEspxjb7gC92uSVcRC5h1i2gTQnRzswNk7Aq4sDbZF4Rca_iDzFYdQTxEoJOP39YcWBoYKOHpPJVvJ1qQfZphhu83WyaEj1JLfpj45cvT9cphUnbvBpcej4tXR5C9xtG1VuCzWqLHFaWucNp9e0KW1fBU5AleucPnu1k3v-flS7gAgRPMP5L_J9dj0BQOzg4w1rxW9SXA22aCrjECDoWzQJqK6KDQXgJHawbkwxAyI70ayRKXzyqPRjzzqFDZuJh2dzecPyBHF3hrwA-VtOFoRzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سناتور دارلین گراهام (خواهر لیندسی): اسرائیل متحد بسیار قدرتمندی است و من کاملاً معتقدم که باید در کنار آن بایستیم. همان کسانی که می‌خواهند به اسرائیل آسیب بزنند و به آن حمله کنند، به سراغ ما هم خواهند آمد. تروریست‌هایی که به دستیابی به سلاح هسته‌ای نزدیک…</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/withyashar/25469" target="_blank">📅 09:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25468">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e3e3beb9e.mp4?token=Ja5J6CbrxhOuEezcg8Cs_yubUPTT1EuWWbxWccf8a7AMzD9fhRN0ciHmvjy0NRyV3lxjzWRhPqCE-gRXKJhbUcJkDmUgyEy4DNR00MASA4ElFSZMekoWWyP0zj6dQyFW0-Fs_DZu8Vh8iTQaDexGGY_i_6Q_GOFVjrJawLJ-2kQ7p3liSJYOQaJFI6DtsT3ftXb8YT3STUlkPLVNYy3QUPwaVD-iFYHAocxWPBLHB8fYmWJcoRIV2ES_eGGU0UQxzDP08ZO8kqTaDM_4v5EGBMuCkm1OmF6Xom6_vNsEyf1m1slQdcuEnYUmHs9lZODLRpmPZggscWMT7opLoo9JAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e3e3beb9e.mp4?token=Ja5J6CbrxhOuEezcg8Cs_yubUPTT1EuWWbxWccf8a7AMzD9fhRN0ciHmvjy0NRyV3lxjzWRhPqCE-gRXKJhbUcJkDmUgyEy4DNR00MASA4ElFSZMekoWWyP0zj6dQyFW0-Fs_DZu8Vh8iTQaDexGGY_i_6Q_GOFVjrJawLJ-2kQ7p3liSJYOQaJFI6DtsT3ftXb8YT3STUlkPLVNYy3QUPwaVD-iFYHAocxWPBLHB8fYmWJcoRIV2ES_eGGU0UQxzDP08ZO8kqTaDM_4v5EGBMuCkm1OmF6Xom6_vNsEyf1m1slQdcuEnYUmHs9lZODLRpmPZggscWMT7opLoo9JAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمای‌ نزدیک از‌ نفتکشی که در اطراف تنگه هرمز با مین دریایی برخورد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/withyashar/25468" target="_blank">📅 09:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25467">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">به گفته مقامات اوکراینی که با شبکه ABC صحبت کردند : خارکیف یک نیروگاه در شرق اوکراین امشب حداقل دو بار مورد حمله قرار گرفت، این اتفاق پس از آن رخ می‌دهد که ترامپ از توقف "فوری" حملات به تاسیسات انرژی خبر داد . پیشتر‌ مقامات روسی هم گفته بودند این پست ترامپ…</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/withyashar/25467" target="_blank">📅 09:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25466">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQ9B0yqVb5RKkpXWJAqMw_C74xcKaIKkiM512RzMMCXrZHv1m6OFCwe9ndt67tvIEkb9NCuNpwP0WUDVv3cQBN6JxnhmPkKwkcG03ZOjOFceNIDk8YuA-Bo3IH5gS9Pz42Y9GMB3p-itFnzZ0RJk9gsstNhVRgMR8R3QbwQn2Rr8afuJHPp1ENfbi5AmR89Ygw8ahf0XOBoxfGwO-l95uu7mdsaEjp-9rBLna63Khk6zxWXHg3lyFJ2cLV2OElDqCYKbNBfQHj7uBFQMrHVvQLHFoU5x94mJcvo6UIAXR6SeKMGVq3IoIkex3mvUUNjC7ez3yuGf0Qligwm5P8KNUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس‌نیوز: ارتش آمریکا راهنمای شناسایی تصویری (تهدید را بشناس) را برای کمک به سربازان آمریکایی در شناسایی نیروهای ارتش ایران ، منتشر کرده است. این راهنما شامل تصاویر یونیفرم‌ها، علائم درجه و تجهیزات نظامی ایران، از جمله سلاح‌های کلاشینکف، تفنگ مصاف ۲ و نارنجک‌انداز آرپی‌جی ۷ و… است
@WarRoom</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/withyashar/25466" target="_blank">📅 09:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25465">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">شبکه ۱۳ : ترامپ و نتانیاهو طی هفته‌های اخیر، در پی گزارش‌ها درباره بازسازی کارخانه‌های موشکی و پهپادی در ایران ، گفت‌وگوهای فوری داشته‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/25465" target="_blank">📅 04:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25464">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hK03Xg2VoRicEURmoFqTwMIVQ2AlVLsX7-NYofaH02RMmMK2SuA2Eee1QrZ72NWJ3SPQT9eQdPKSu1mvQK_ZVFa6xDecA-NWCgYmYArsq-GjofDs9b-D5CfnHhi3L3MZPp8AQGb2fG8ziPYAljjnQeqlh4eRvRM-R4w11u1pHDnUp63UsiPrUOIvXyGdJQnNSlgLJdAWwLawOn1LEV3vszUwb7gLe_E1G7BtR9l9EieE6q_7hU6h10g72fOBJe6cBXHj3o7kpdZATwZUj7RVkhO-SAEJKgXBkbmRcvkzT3IJTdm5q5n2poR9dy7IRXSqmwxN4mDy-i7dhzk7_MvZxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله افراد مسلح به پاسگاه مورتان در بخش پارود شهرستان راسک و درگیری شدید با نیروهای مستقر در پاسگاه گزارش شده است. بر اساس اطلاعات اولیه، درگیری از دقایقی پیش آغاز شده و دو طرف به تبادل آتش پرداخته‌اند؛ تاکنون جزئیاتی درباره تلفات احتمالی یا وضعیت نیروهای پاسگاه منتشر نشده و هویت و وابستگی مهاجمان نیز مشخص نیست. این حادثه در حالی رخ می‌دهد که طی روزهای اخیر چندین مورد درگیری و حادثه امنیتی در سیستان‌وبلوچستان، از جمله زاهدان، سراوان و ایرانشهر، گزارش شده است. جمعه گذشته نیز سرهنگ زن نصرت افتخاری پودینه، معاون فرهنگی و اجتماعی فرماندهی انتظامی استان، در انفجار بمب کنار جاده‌ای در محور چشمه‌زیارت زاهدان کشته شد؛ جبهه مبارزین مردمی مسئولیت آن حمله را برعهده گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/25464" target="_blank">📅 03:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25463">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a2b70e41.mp4?token=ulRHHvIYJf_sObIwGFNtElhqdxsI9tKTB0TX0TpQYTj-zBo7HueiDaIO1y6UVO2frMclyId-wDDxAcbOFm6-ZGTA5lLQGzo_yM7lm-ImKmHjbEZzDwmOMDjcTpqG3m5Cm_ZmFPqJbI5d2sQ2fe_pvLf76RoaU_fB09Ijua7SYUfBDymzwRqkyAJfgqJ8ombZIgPb0FUSy0KqtXDcDEaPvld5t0ATcPEZrwH3ALjmuBbbFU6x2fSCc28gOFQorWyco5hvoF-uUYIW9OmJIFJxif-fvKp5zxOr0aqXKjsoAKXHhxnuX5e9owMXOXTnNOAI9V7JbkxmnNsJU57UpF_UFjW7_DcToQ6wVZTI8-ThIPdXv-UkugAPnRuI7JSF55Rmg1myPReM1-uWu9QOtqvDzQkVPvOsQmglHjlEAlYtCqDa_aUUZDixxxdjLEWIblrx2W2p5OrJVslRox1KgoDTcsRrX3F1Z-ejHTOYfGzeZCLBVW5uSzIAeKUBYV6uNFm36J_cPsNY4cBhxw3_iy2P89Qw6ruTeDs_gYgd1OdR3tADvp0x1eahU8MvO-6VRs5L8_Z_mHWPFPpdJHWqzvvixHSc8LuK6Tu0ilUCMaIyoEq001QrViqEvpcwjJ3MS5i18aSayryoaWPtwEev1Nc-Ngtf93_F0Q-E_7LRNMTX48I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a2b70e41.mp4?token=ulRHHvIYJf_sObIwGFNtElhqdxsI9tKTB0TX0TpQYTj-zBo7HueiDaIO1y6UVO2frMclyId-wDDxAcbOFm6-ZGTA5lLQGzo_yM7lm-ImKmHjbEZzDwmOMDjcTpqG3m5Cm_ZmFPqJbI5d2sQ2fe_pvLf76RoaU_fB09Ijua7SYUfBDymzwRqkyAJfgqJ8ombZIgPb0FUSy0KqtXDcDEaPvld5t0ATcPEZrwH3ALjmuBbbFU6x2fSCc28gOFQorWyco5hvoF-uUYIW9OmJIFJxif-fvKp5zxOr0aqXKjsoAKXHhxnuX5e9owMXOXTnNOAI9V7JbkxmnNsJU57UpF_UFjW7_DcToQ6wVZTI8-ThIPdXv-UkugAPnRuI7JSF55Rmg1myPReM1-uWu9QOtqvDzQkVPvOsQmglHjlEAlYtCqDa_aUUZDixxxdjLEWIblrx2W2p5OrJVslRox1KgoDTcsRrX3F1Z-ejHTOYfGzeZCLBVW5uSzIAeKUBYV6uNFm36J_cPsNY4cBhxw3_iy2P89Qw6ruTeDs_gYgd1OdR3tADvp0x1eahU8MvO-6VRs5L8_Z_mHWPFPpdJHWqzvvixHSc8LuK6Tu0ilUCMaIyoEq001QrViqEvpcwjJ3MS5i18aSayryoaWPtwEev1Nc-Ngtf93_F0Q-E_7LRNMTX48I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سناتور دارلین گراهام (خواهر لیندسی): اسرائیل متحد بسیار قدرتمندی است و من کاملاً معتقدم که باید در کنار آن بایستیم. همان کسانی که می‌خواهند به اسرائیل آسیب بزنند و به آن حمله کنند، به سراغ ما هم خواهند آمد. تروریست‌هایی که به دستیابی به سلاح هسته‌ای نزدیک شده‌اند،( جمهوری اسلامی ) به آمریکا هم خواهند آمد. بنابراین، باید از قوی‌ترین متحد خود در خاورمیانه حمایت کنیم؛ نگران دموکرات‌های سوسیالیست هستم؛ زیرا در ۷ اکتبر، زمانی که حماس بیش از هزار اسرائیلی را کشت، دموکرات‌ها در خیابان‌های نیویورک به‌خاطر کشته شدن این افراد جشن گرفتند. حماس گروهی بی‌رحم و شرور است.
@WarRoom</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/25463" target="_blank">📅 03:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25462">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">طبق گزارشات دقایقی پیش یک نفتکش در مسیر جنوبی با پرچم هند در تنگه هرمز توسط سپاه هدف قرار گرفت؛ دو نفر از خدمه مفقود شده‌اند و ٩ نفر دیگر نجات یافته‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/25462" target="_blank">📅 02:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25461">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faSyzEWDZaI2yAe8M3nYnxZSRMftaJxDgykLshyVLLMoyXnM3pYdx_UX4MEg4SBEeFYBUQ8_AGQFhofaJGY0xNU7RgUQC7C8NB1NTlLVUl_57Mo6MEc2gY3V_VPMmxvuaqTn0g5ALAmLArf454YGtFCh_0VcNGTuBw0vJd3pX83GqWP7rjnrIsVyjLBuT-T-OMndXD5aKwNlzl7YIrl_Tc3u1dqfgAUzAoGkx1_Ra6ZwrI9EnBb3bkBcw-d6CSlGnVfSuvaLKXl6BZPxt0aBwGjbeck16qi69rQUWsZyQsUiD83IL1CX6cHO-22QFLGPQ1qJwxWLAQpx-5lMuC5RBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با بازشدن مارکت ها قیمت نفت برنت به ۱۰۵ دلار افزایش یافت
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/25461" target="_blank">📅 02:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25460">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZXLtLDYeE1ECnNx0RTEcfrjjM_gVr7tDXzDoFtRhG22vsxku9s1FgaEkd0NAJ9GgEgsV7vVuVUO6MGFvFbAN_5cTRrDUKV7HH2yPKKqWo0_f6DtG3EImXg2P37aNkw4MKa5_6Lxtr1lM582VkXbDsoKTDV0s7dhCU4SRkqr3RuepNBCfSYcRkRTdcPCV_Ufj3pKjPtjlO8vVGoTGVF6eA3fyHU3Vl3GibyrrzX9JayS_4gki6NTAm1MfSdmIQ1g8E6GU-GSE8RrYymxCUN5PHB_2QTo0de0XTB5IgYcvNbQx8yFkcUpb_hDbdVCAvcvJds9B0ODXZYgQWiF1Fo4qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاطمه مهاجرانی، سخنگوی دولت : پروژه ایجاد ترس از ایران و تضعیف روابط این کشور با جهان، «افسانه‌ای است که دشمنان ترویج می‌کنند» @WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25460" target="_blank">📅 01:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25459">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYDq2l-xIYeu28v6Jyl2-bdScmzUQRKepcQlEnU4IrzNpWUnfy3jBujlqFnRXWoahqv95hRIYUHKqfPp89-_EwD7jZWpC2n6oCxiq6LudOnCd5JofaX33EL9J2CJSfqesYC2PpNtR8ZKOwwU3dOOdJhNImj2FwbGX7Z6selcuw_yAwWv-DF25ARbY4gNAyTkrOULtZoNO2ZAL8Dt_7otJhYRa9DZih3SnEMn9kJbr5Jo0ZiN80-StwafiWC4ovdnUs7KRmpwAUR4dmnoNXGBas_kLc7vSD5pgT8aILEHUQtclpLqy3MzU_U1gchwiv0yklbXAgSOgH84oySluHnQUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند جنگنده چندمنظوره F-15 نیروی هوایی ایالات متحده (USAF) در حال پرواز تمرینی حمله به ایران بر فراز عراق مشاهده شد.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25459" target="_blank">📅 01:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25458">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyYAiN4oyNbjh8zMFr8mFMaaFlVWFUKHDofnouYjglDF2Y3sjU0cugaCMivkY3f6WR-4v1C7bLGFrtAgJFx9UFaEBHfatvCU6PoDblyXVDVhDX42oLybupK1fa5iKKE5HPXfVzSWk32dq3rkcjztdyf_pf3FibrbPck6n9GJsS-8RxeI9jDSi0-FH345PYa3vrC04O1tdNc4fC_eH0pzPkdUbN5-_mgb3nMGzRtufhr1Dp7NofP7K5_iFLvsaA9tnWafR_LI0vAOAy2tdNjBNzhxLIaYNElze8ZW_gbHnW5UJp8WUnv8A83QNtmEdR3GbGaeGKeeOL5bQktJjDPUGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی مبنی بر وقوع حادثه‌ای برای یک نفت‌کش در نزدیکی لنگرگاه «صحار» در عمان دریافت کرده است.
پس از تأیید اصابت یک پهپاد (UAV) به نفت‌کش، UKMTO ماهیت این حادثه را به «حمله» تغییر داد. مقامات محلی در حال همکاری برای تخلیه خدمه هستند؛ با این حال، در زمان این به‌روزرسانی، اطلاعاتی درباره میزان خسارات و پیامدهای زیست‌محیطی در دست نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25458" target="_blank">📅 00:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25457">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گنده‌گوز منطقه کنترل بخشهای زیاد و جاده‌های سیستان و بلوچستان رو از دست داده
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/25457" target="_blank">📅 00:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25456">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ممجواد ظریف : هرجور شده باید با آمریکا توافق کنیم. حتی اگر عین قرارداد ترکمنچای یه جایی رو هم بدیم.«ترکمنچای امضا‌شد چون بقا درخطر بود»
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25456" target="_blank">📅 00:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25454">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترابری نظامی وحشتناک آمریکا از ۲۴ ساعت گذشته تا همین الان الان. شما فقط سرانگشتی حساب کن، اگه اینا خالی بخوان برن بیان، میلیون‌ها دلار هزینه داره. ترامپ بیست دلاری رو چند بار چک می‌کنه.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25454" target="_blank">📅 00:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25453">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">فایننشال تایمز : آمریکا تهدید کرده که جریان تسلیحات به اوکراین را از طریق مکانیسم PURL متوقف خواهد کرد.
این مکانیسمی است که در آن اروپایی‌ها از بودجه خود برای خرید تسلیحات آمریکایی که به کی‌یف ارسال می‌شود، هزینه می‌کنند. واشنگتن هیچ هزینه‌ای در این زمینه پرداخت نمی‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25453" target="_blank">📅 00:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25451">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فیلم لحظه برخورد موشک بالستیک گروه تروریست حوثی‌ها (انصارالله) به ترمینال ۳ فرودگاه بین‌المللی ملک خالد ریاض در روز گذشته را نشان می‌دهد
این حمله تا الان ۱۳ کشته و بیش از ۳۰۰ زخمی برجای گذاشته
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25451" target="_blank">📅 23:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25450">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یک مقام کاخ سفید به اکسیوس : ترامپ واقعاً عصبانی است. او احساس می‌کند زلنسکی آمریکا را بدیهی فرض می‌کند و قدر حمایت‌های آن را نمی‌داند.
استیو ویتکاف و جرد کوشنر هم سفر برنامه‌ریزی‌شده خود به مسکو را به تعویق انداخته‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/25450" target="_blank">📅 23:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25449">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNK1LXJ_ziwGaltx1Io4OYaDynm1lYHSD6ZNLgi539tN_Adz84oPSuEIrn-ruXFcEv7hnhUav3ehOaROlxCbTRNiRrs8IKlqq1Iwwo-VfFwMAdvInZpE6J1HEiGrbe6GmIWtBV1E3vGItlcHrXbg0EpHxJ0xLFelAf3SALHYhdWQzXUuRqtyYO7z6SysUI9H9-w7R0RkPv1IqmaOe5PWLeonPCslpMF6LV0C2DH-pue_o68-BLNbRdCiYQ3946tgFWjzxLgXGbs24Gz54aS3L0Zu3nIamepzxCf-V--UGCWqH1v4xkkpjpT30vLQZZOYvb_d7gulh-Zof8ODT7ELtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جنگ حتمی سوم، سخنگوی گروه تروریستی سپاه با انتشار تصویری در شبکه ایکس نوشت «ما منتظریم»
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/25449" target="_blank">📅 23:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25448">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">به گفته مقامات اوکراینی که با شبکه ABC صحبت کردند : خارکیف یک نیروگاه در شرق اوکراین امشب حداقل دو بار مورد حمله قرار گرفت، این اتفاق پس از آن رخ می‌دهد که ترامپ از توقف "فوری" حملات به تاسیسات انرژی خبر داد . پیشتر‌ مقامات روسی هم گفته بودند این پست ترامپ…</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/25448" target="_blank">📅 23:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25447">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ورود گسترده هواپیماهای نظامی آمریکا به اروپا برای پشتیبانی حمله احتمالی
نیروی هوایی ایالات متحده در حال انتقال گسترده هواپیماهای سوخت‌رسان و ترابری نظامی از خاک اصلی آمریکا به پایگاه‌های اروپایی است.
حدود ۲۰ فروند از این هواپیماها طی ۴۸ ساعت گذشته به این پایگاه‌ها رسیده‌اند.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/25447" target="_blank">📅 23:22 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25446">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">آسوشیتدپرس ، بن‌بست مذاکرات ایران و آمریکا؛ تهران پاسخ واشینگتن را ناکافی دانست:
محسن رضایی اعلام کرد پاسخ اخیر آمریکا به پیشنهاد ایران برای پایان جنگ، خواسته‌های تهران را تأمین نمی‌کند و واشینگتن باید موضع خود را درباره موارد مبهم روشن کند. به گفته او، آمریکا برخی از هفت شرط ایران را پذیرفته، اما وضعیت سایر شروط مشخص نیست.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25446" target="_blank">📅 23:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25445">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کاظم دستکج ، غریب‌آبادی: اقدامات کنترلی ایران در تنگه هرمز تا زمانی ادامه می‌یابد که آمریکا به این نتیجه برسد راه‌حل مسائل موجود نظامی نیست. به گفته او، ایران در حال پیگیری ثبت تفاهم با عمان در سازمان بین‌المللی دریانوردی است؛ اما این تفاهم به معنای بازگشایی فوری تنگه هرمز نیست و ایران تا زمان اجرای تعهدات آمریکا، خود را ملزم به بازگشایی این آبراه نمی‌داند.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25445" target="_blank">📅 23:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25444">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szeNtTMlAYaXADQJqGpbcB02lFopV4z1WO_FfiDfR-eVm9F-gE-EGDo9IlTVB9s_rnI7YWi6cfI19mXgjncQvACBWIdsS8waXgCOLptJelE4NwOjNnEtvnlRI6onE2dY_MfxIRm1e8fXn16GQjlvHoIOJzUIiuPMNbG_nndUqmRJ8GyNWX6TyLEd2xpIkkGi2XN7a-q1UbBn4bVy_iHHnUyFBXK0VOgpBnWi6JOKrw5r0bbXEnBp1XEWRU-_f0MsTQo8PaVbSMg62eJ4QBjUFpAvZ4AsmH4pku7Lm5JjHSrKE5Fbv5TdMa8KETNCTf5aUOAJ8lkjAMxuurYMxE4V_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آزمایش موشکی دقایقی پیش
سپاه پاسداران در این چند روز آزمایشهای موشکی و تستهای پدافند خود را بیشتر کرده تا بازدارندگی را ایجاد کند و هم از عملکرد خود اطمینام داشته باشد چون میداند که جنگ سوم حتمی است.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/25444" target="_blank">📅 22:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25443">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ادعای شبکه ۱۳ اسرائیل:
نتانیاهو امشب پس از اظهارات ترامپ درباره احتمال ازسرگیری حملات به ایران، رایزنی‌های امنیتی برگزار می‌کند
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/25443" target="_blank">📅 22:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25442">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خبرگزاری رژیم تسنیم از رصد پرواز هواپیماهای نظامی آمریکا در آسمان عراق خبر داد و مدعی شد پنج فروند سوخت‌رسان KC-135، دو جنگنده F-16 و دو جنگنده F-35 در این پروازها حضور داشته‌اند. این پروازها از پایگاه‌هایی در اردن و اسرائیل انجام شده‌اند و در حال تمرین حمله به ایران میباشند
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/25442" target="_blank">📅 22:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25441">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">به گفته مقامات اوکراینی که با شبکه ABC صحبت کردند : خارکیف یک نیروگاه در شرق اوکراین امشب حداقل دو بار مورد حمله قرار گرفت، این اتفاق پس از آن رخ می‌دهد که ترامپ از توقف "فوری" حملات به تاسیسات انرژی خبر داد . پیشتر‌ مقامات روسی هم گفته بودند این پست ترامپ برای کنترل مارکت است
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/25441" target="_blank">📅 22:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25440">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCQYhM0FiTzrYGwaxmsqvls3HQz12elxEASmbJ12xAE_AGCoVhUTvj7kz1e2AWO5k7HByN5J6rb_iDi0NSwOJ3TByfD7iCqAa4qAaGvLZeo-ZkWx0N5LwLQBitAqsgbgvL0xJd6XPrpzw6ENs7VvLlpbI03wTPoSK-5eg5GHCDW7O6Cf0z7C7l-DQOirqhmbZPmuzzwRD9h0mGH1AdTT3yta5O66PloQqi3CZeSB-LPfe9Tt2cEJnl0sV9OrH_gH12TfgkEqQSkog8gt2DVYAr4DibL2oqTIca2W4jEKG11lDz1_im3zV4l6QeZMFV7XrmvyVVjDgAZsPJNve3IB6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خرمشهر
😁
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25440" target="_blank">📅 22:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25439">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghiPQgN1Ee5FppvIUgPTWbl_4Xpvqm2y7xTFEDXZysMTMCIaK9NkL_iz37NlBsN4kkh5oQ5i3RtmPLzRu1dVIWcaNZpQtxzgcKCdX7oX6Emu-hKuC1aFO3kDxTs1RBcgtKVS5fpIaOEINQBN8kRZ9Vo93zI2BsO341ER3cH6Q5H-vMwiuIfTLaFYz_g7EoaSaCkOx3bVHVA_ZC8ZoXsNCpE7qfU1aRasPXXCV8HWoR3pq9Kbq2TtFaL0jBc4f8icqA5WJSTMnoFA5kBJYF3zbOsV89pQDhKVmCJqpYzdaAuB_qpRDy-onda7FWVjT6TQrY59s723HafV--_M40-nPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تبلیغ فیکه مراقب باشید ، فقط هی روش الکی کلیک کنید اعتبارش بره کار دیگه انجام ندید
🤣
🙌🏾
⚠️</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/25439" target="_blank">📅 22:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25438">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا:
گزارشی درباره وقوع حادثه‌ای برای یک نفتکش در نزدیکی بندر صحار عمان دریافت شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/25438" target="_blank">📅 22:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25437">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">فایننشال تایمز: به دلیل حملات یمن، مدیران ارشد شرکت‌های نفتی شروع به ترک کنفرانس جهانی نفت (WPC) کرده‌اند که قرار است در ریاض برگزار شود.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/25437" target="_blank">📅 21:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25436">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9db3e49ede.mp4?token=j2HQMWYUPaSJy3ihD2OY3BAHbeiUFdpvP0bywNz6AuBgysySDVLzNCbeOlavJzxfnSaywTvHXKefekk0ZHmGoLvnRqChA7ZRtNGZrPOZvkL7EhboDLEElOGw-ncfcsixQY5DuP_OhRAOPxT04eUh792p0NKYIi5rHlD9YoyBUDM-zcGCBrA3C6Tgkp-TmGv_svbp47fPNEbtwQ9QLR3hBJftJdpC7W3qhPahumKb7CUzxC0b1DE9e27zRaQphBcd3kx639DxKFsDvEYOW41pko_8o-wZlLzRQ2ZvGLKtV6NZ-DWwjwBbmS5lDyA05FVNGJPwEdX5pZ975jJnUOZ0ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9db3e49ede.mp4?token=j2HQMWYUPaSJy3ihD2OY3BAHbeiUFdpvP0bywNz6AuBgysySDVLzNCbeOlavJzxfnSaywTvHXKefekk0ZHmGoLvnRqChA7ZRtNGZrPOZvkL7EhboDLEElOGw-ncfcsixQY5DuP_OhRAOPxT04eUh792p0NKYIi5rHlD9YoyBUDM-zcGCBrA3C6Tgkp-TmGv_svbp47fPNEbtwQ9QLR3hBJftJdpC7W3qhPahumKb7CUzxC0b1DE9e27zRaQphBcd3kx639DxKFsDvEYOW41pko_8o-wZlLzRQ2ZvGLKtV6NZ-DWwjwBbmS5lDyA05FVNGJPwEdX5pZ975jJnUOZ0ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران تصاویری از آتش‌سوزی گسترده و نشت نفت از یک نفت‌کش منتشر کرده است؛ نفت‌کشی که به گفته این نیرو، در تنگه هرمز هدف برخورد مین دریایی قرار گرفته است. @WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25436" target="_blank">📅 21:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25435">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">کانال ۱۵ اسرائیل : تحولی در تحقیقات مربوط به پرواز تروریستی: سفارت مالدیو اعلام کرد که دو خلبای دیگر شرکت "فلای دبی" دستگیر شده‌اند. به احتمال زیاد، این دو نفر در همان ساختمان با کمک خلبان تروریست زندگی می‌کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/25435" target="_blank">📅 21:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25434">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f5401b52.mp4?token=TTO2KysPU9ZDTz0Mo9y-hG00SBFW963X6RmyW72WDVIrjdrqcIeyKRgYHC5EJvAK2zC_6M951gnbSdv7-rel_XviUxwrM7tJ3oicJno95nCJokmF1PbuDIkB0ePzwNGxjcbWaYAX03xA-8OP416wsqt1sZwPFysJt0K1Rpo2Wf7zufkph8dKwFi1fqvkaT1gbdO0yq9fpOpUapuBf6DRVQcge2QrGgFsukYvl7C3SxkfK8FbeSDqQM_FoQKLSSzfSBlnjRqhLvqrSnHTck_BJuKBtTJjgqfualknoSBJalsuuxPVQXlknAPPEUm2OUVtyZtvy3bj0653i33vpPSYjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f5401b52.mp4?token=TTO2KysPU9ZDTz0Mo9y-hG00SBFW963X6RmyW72WDVIrjdrqcIeyKRgYHC5EJvAK2zC_6M951gnbSdv7-rel_XviUxwrM7tJ3oicJno95nCJokmF1PbuDIkB0ePzwNGxjcbWaYAX03xA-8OP416wsqt1sZwPFysJt0K1Rpo2Wf7zufkph8dKwFi1fqvkaT1gbdO0yq9fpOpUapuBf6DRVQcge2QrGgFsukYvl7C3SxkfK8FbeSDqQM_FoQKLSSzfSBlnjRqhLvqrSnHTck_BJuKBtTJjgqfualknoSBJalsuuxPVQXlknAPPEUm2OUVtyZtvy3bj0653i33vpPSYjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روباه قطبی ، ممجواد ظریف : هر کسی که هنوز فکر می‌کند سلاح‌های هسته‌ای می‌توانند بازدارندگی ایجاد کنند، کافی است به اسرائیل نگاه کند. به اسرائیل در طول یک سال و نیم گذشته نگاه کنید.
بله، اسرائیل غزه را ویران کرد، اما آیا سلاح‌های هسته‌ای از اسرائیل محافظت کردند؟ آیا سلاح‌های هسته‌ای از فروپاشی اتحاد جماهیر شوروی جلوگیری کردند؟ اتحاد جماهیر شوروی بزرگترین زرادخانه هسته‌ای را در اختیار داشت.
علاوه بر این، ما به اندازه کافی اورانیوم برای ساخت یک سلاح هسته‌ای نداریم.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/25434" target="_blank">📅 21:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25433">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نبرد سرنوشت‌ساز برای بازپس‌گیری باب‌المندب از حوثی‌ها
دولت یمن‌ امشب اعلام کرد نیروهای دولتی با حمایت ائتلاف به رهبری عربستان، پس از بازپس‌گیری ذوباب و مواضع راهبردی اطراف آن و قطع مسیر ارتباطی با المخا، به‌سوی کنترل تنگه راهبردی باب‌المندب پیشروی می‌کنند. دولت یمن این عملیات را مرحله‌ای سرنوشت‌ساز برای بازپس‌گیری حاکمیت بر سراسر کشور و پایان دادن به کنترل حوثی‌ها دانست. همچنین حملات حوثی‌ها به فرودگاه بین‌المللی عدن و فرودگاه‌ها و تأسیسات غیرنظامی عربستان را محکوم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/25433" target="_blank">📅 20:56 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25432">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کابینه امنیتی اسرائیل : امشب (یکشنبه شب) جلسه‌ای با محوریت بررسی اوضاع در چند جبهه از جمله لبنان، سوریه، غزه و ایران تشکیل خواهدشد @WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/25432" target="_blank">📅 20:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25431">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXiI14A0872tyXJP0z7_fbEe4M5csjmcNNlUoA9kzeTFOwQA0M3leA_mBeyoSiwR3Dac07SqFKHb6dpxvYPdnRRxFUwlqLOPsrHyPRTNvRdv7SrG5ZAQ815Fl8IIyzK36quBX_IjXw9WL3S8ap-0eR9-Lo_yfIWKqsg-SAxuToQgoNWM_ay5mLAOXjh30Dsia5kPC7Q0qLDzVfIFnIAHjKRRgPrBXxNFDT1JxfWsOy_9TrouVJ1zZHb0gtmi7pBMUKOgPGfTKS4ZXn2f0zKEgVwywguL_5RQh3LBty5o1bbgTtaSd7o75X4cir6PoASEfgEgaPPkJkWQ1FV4EL9M2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های رژیم : زینب ابوطالبی مجری جنجالی «مملکت مال حزب‌اللهی هاست، هر کس نمی‌خواهد جمع کند از ایران برود»، از کشور رفت
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/25431" target="_blank">📅 20:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25430">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کابینه امنیتی اسرائیل : امشب (یکشنبه شب) جلسه‌ای با محوریت بررسی اوضاع در چند جبهه از جمله لبنان، سوریه، غزه و ایران تشکیل خواهدشد @WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/25430" target="_blank">📅 20:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25429">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEJq9sskJ1GZucvPQbv0yDxmBkW6o5DTk5dyY0UWvoIoA1Z_ZeyfedU8lbjp4Xx_bGckTpWJ7SyKx3TkgUqXyVpjfbksZ-Nlcf1mf3N_7f9TDP4Wf_RzgX7j1GzR3xg2g1KCR6TsLHKVquSP-FgihIeNyvfKp42YSWQS__TizL9ubO89W7tyIGBx6IMF8P4K5_mUHcNzcm47p5tLvBYPoFnmJ0EIqq_LCJygJz_pUW45kbFv99bS29g-YLlj_x2P0EJQSlJtiDO7ZqQWUsNvIGv8TFn7feNdbvnJdoTNXtHKq_kjF-aK6AUlRCf6PFEiBZj0scqtKP34i-jjWqkLvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی ، کج بند : می‌توانستیم تنگه هرمز را کاملاً ببندیم، اما به دلایل انسان‌دوستانه این کار را نکردیم
اگه دوباره جنگ بشه اینبار به تاسیسات هوش مصنوعی و دارایی های ایلان ماسک تو منطقه هم حمله میکنیم
تهران به رویه‌های دیپلماتیک گذشتۀ خود باز نخواهد گشت
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25429" target="_blank">📅 20:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25428">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کابینه امنیتی اسرائیل : امشب (یکشنبه شب) جلسه‌ای با محوریت بررسی اوضاع در چند جبهه از جمله لبنان، سوریه، غزه و ایران تشکیل خواهدشد
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25428" target="_blank">📅 20:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25427">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbRY2QtHAXsYLOaHTcmalnrM2zUDMowINQ_qekldtQ03e87FfaX0vqS4-ysK9EOuQwQufhlIEffjXxG0iD9qYJAapDB0sGlcgMsAtWiMfKM6diry5u_KuuwPG273JGtZZdSyEi2xyS7qQH9uH-NNw9jp98-ZLzAC5lB5mBD70YFE4pmHUr-KniM7DKplGp2Er2RgGvFgRz-Zb5JqgnNq6oFJkm-9gZROea8txTkQLJfzWNaf161c6AE-L_5Q-7JlVutpMrgg91XYdJW0ScnDgXmkJyDXRy3Msr1GWRuP80lDB0PkyRPUV8mm1k5NHOPVWYiQi6F00p2NfHCtkC6xPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: ملوانان نیروی دریایی آمریکا در حال انجام تعمیر و نگهداری جنگنده اف/ای-۱۸ سوپر هورنت روی ناو هواپیمابر «یواس‌اس جورج واشنگتن» (CVN-73) هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25427" target="_blank">📅 20:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25426">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">شاهزاده رضا پهلوی: «حمله وحشتناک به فرودگاه ملک خالد در ریاض، تازه‌ترین نشانه آن است که رژیم تهران هرگز به دنبال صلح نخواهد بود. از سال ۱۹۷۹، جمهوری اسلامی چه مستقیم و چه از طریق نیروهای نیابتی خود، علیه عربستان جنگ به راه انداخته و به دنبال بی‌ثباتی بوده است. به ملک سلمان، محمد بن سلمان و مردم عربستان به‌خاطر جان‌باختگان این حمله تروریستی تسلیت می‌گویم. کارزار آشوب حوثی‌ها زمانی پایان می‌یابد که ایران آزاد شود و روابط دوستانه میان دو کشورمان از سر گرفته شود.»
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25426" target="_blank">📅 20:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25425">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">روسیه: شمار کارکنان روس‌اتم در نیروگاه هسته‌ای بوشهر به ۱۳۵ نفر رسید
الکسی لیخاچف، مدیرعامل شرکت دولتی روس‌اتم، اعلام کرد با بازگشت ۹ نیروی دیگر برای انجام تعمیرات برنامه‌ریزی‌شده واحد اول نیروگاه بوشهر، شمار کارکنان فنی و مهندسی این شرکت در محل نیروگاه به ۱۳۵ نفر رسیده است. این نیروها در واحد فعال و دو واحد در حال ساخت بوشهر فعالیت می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/25425" target="_blank">📅 20:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25424">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اسکات بسنت: ما بخش عمده‌ای از موشک‌ها و پهپادهای ایران را نابود کرده‌ایم و ۸۵ تا ۹۰ درصد توانایی این کشور برای بازسازی و تولید مجدد آن‌ها را از بین برده‌ایم. کارگران در حال حاضر سر کار حاضر نمی‌شوند، ایران به بازار دلار دسترسی ندارد و برای جبران مشکلات مالی…</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/25424" target="_blank">📅 20:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25423">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا: ما پس از یک سال کارزار فشار حداکثری، اکنون وارد کارزار انزوای مطلق ایران شده‌ایم و هدفمان قطع ارتباط این کشور با جهان خارج است. تا روز گذشته، حدود ۱.۲ میلیارد بشکه نفت برای آمریکا از منطقه خارج شده، درحالی‌که سهم ایران صفر…</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/25423" target="_blank">📅 20:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25422">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا: ما پس از یک سال کارزار فشار حداکثری، اکنون وارد کارزار انزوای مطلق ایران شده‌ایم و هدفمان قطع ارتباط این کشور با جهان خارج است. تا روز گذشته، حدود ۱.۲ میلیارد بشکه نفت برای آمریکا از منطقه خارج شده، درحالی‌که سهم ایران صفر بوده است. ایران اکنون هیچ نفتی روی آب ندارد و با جریان نقدینگی منفی مواجه است. ما خدمات هوایی ایران به جهان را قطع کرده‌ایم. مقام‌های جمهوری اسلامی دیگر نمی‌توانند به بستگانشان در لندن، دوستانشان در پاریس یا پولشان در سوئیس دسترسی داشته باشند. فشارها را از طریق توقیف رمزارزها و متوقف‌کردن کشتی‌های ایران ادامه می‌دهیم. ایران کنترل تنگه هرمز را در اختیار ندارد؛ پهپادهایش را هر شب به پرواز درمی‌آورد، اما توان راداری ندارد و گاهی به کشتی‌ها آسیب می‌زند، درحالی‌که کشتی‌ها همچنان عبور می‌کنند.
@WarRoom
ویدیو کامل ۱۲ دقیقه ، متن ۱/۳</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25422" target="_blank">📅 20:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25421">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سازمان هواپیمایی عربستان سعودی تأیید کرد که فرودگاه بین‌المللی «ملک خالد» در ریاض عصر امروز هدف حمله جدیدی قرار گرفته است.
دیروز ترمینال ۳ و امروز ترمینال ۴  این فرودگاه مورد هدف قرار گرفته
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/25421" target="_blank">📅 20:02 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25420">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">فایننشال تایمز به نقل از مقامات ۵ سازمان اطلاعاتی اروپایی گزارش داد روسیه در حال گسترش برنامه‌های ترور مدیران ارشد صنایع دفاعی، به‌ویژه تأمین‌کنندگان پهپاد برای اوکراین است.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/25420" target="_blank">📅 19:56 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25419">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQ_cDI_Pi847BiVyVd2EnA1rm5M8czdt4Fd1GEe2A8wk46Xa8ERlg4I8bkqsHc6Yh3DKqjkEQbE-5ehaZ0m0VKRkeLaYXPYjp3WAjGQjJV8QPzMTg9rf0WcddmGU3QmaOT86581T2PQJdyo4C-PuxssuDY1gMYcCQ6lcw_ZeJ3JGVD8DGOoJGBZjmUIfYO2tDXrT6-AdwuK9khd7uIknXo1qBBz1e5XCQbTCoMx2LaCHX1t7C4yuZzPzoe_B_T3JXadghPlVnGorAoZ1og6O1G-mPYGMxZ1MB0IW9cjdH5SNVvQU18kr41mq-AYSN1zzi1-8APqAm1O-6CU7mT1EHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث: «از همین لحظه، آتش‌بس انرژی در جنگ روسیه و اوکراین برقرار است. هر دو طرف موافقت کرده‌اند. آن را نقض نکنید! از توجه شما به این موضوع سپاسگزارم.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/25419" target="_blank">📅 19:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25418">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c92b0af8e.mp4?token=FLdz7sPB3iFI1cr3-v2lfDovFmBHRzQ0_jUtPvfmA9W1kmM8sNPMKYeYKIUCmjKEp2sp-abbjS9eghvCQN2-2P020ouDDG8p1kUuffFPJ1ywtAFmSMl44ufHbnouUD21jyfE9mfGt1x6YmQOfcNmpwNDYhQBL5x8HR0XOR5pLy0Q1FjS0cZpRd_rpEK1qEsqMPgziQq2idydbVGBQzNweqVP6l8gWf_Inlnj1wtShaPAv7c3B7JmNxbeemPhVVMSo0LRjGZPbLdJmBdM13lHh8_dEmW8WRaC9IHZK4LUtTGLZuvhFU2NauNJSk1nva6ggODzdVAu2wp_X3OaE7L0NTOi483PIsfts6gnBoDkxEUF0PDbF2TR8UWNiM3YtoOwhlufnlXsqUGJPa0g5KUi4b8oHOFNMlt-I3F8aS0XbAv7Xb4Uy4OtneQQNwJTQWqMirj-u3G_Ni9OodrqfU-KabixOrwQ1MunUszDtKXI7iWixakX98zBWptBROlcAXaH4-fWmoaIUkvQHxdWsfSZadoRbDrHIqYmKJQhaDSdP322el02DVilXpUUooeKOQl_HOZmK0h8IckmcSHwrYAb2RX-qc-giWmaC93dp_n1vXCT-sh5-rJqxMDZK4ZznRkogYjjmv2J4KvyWlm_BAegM993vpu2wdHgEZu_fMCT62E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c92b0af8e.mp4?token=FLdz7sPB3iFI1cr3-v2lfDovFmBHRzQ0_jUtPvfmA9W1kmM8sNPMKYeYKIUCmjKEp2sp-abbjS9eghvCQN2-2P020ouDDG8p1kUuffFPJ1ywtAFmSMl44ufHbnouUD21jyfE9mfGt1x6YmQOfcNmpwNDYhQBL5x8HR0XOR5pLy0Q1FjS0cZpRd_rpEK1qEsqMPgziQq2idydbVGBQzNweqVP6l8gWf_Inlnj1wtShaPAv7c3B7JmNxbeemPhVVMSo0LRjGZPbLdJmBdM13lHh8_dEmW8WRaC9IHZK4LUtTGLZuvhFU2NauNJSk1nva6ggODzdVAu2wp_X3OaE7L0NTOi483PIsfts6gnBoDkxEUF0PDbF2TR8UWNiM3YtoOwhlufnlXsqUGJPa0g5KUi4b8oHOFNMlt-I3F8aS0XbAv7Xb4Uy4OtneQQNwJTQWqMirj-u3G_Ni9OodrqfU-KabixOrwQ1MunUszDtKXI7iWixakX98zBWptBROlcAXaH4-fWmoaIUkvQHxdWsfSZadoRbDrHIqYmKJQhaDSdP322el02DVilXpUUooeKOQl_HOZmK0h8IckmcSHwrYAb2RX-qc-giWmaC93dp_n1vXCT-sh5-rJqxMDZK4ZznRkogYjjmv2J4KvyWlm_BAegM993vpu2wdHgEZu_fMCT62E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک والتز، سفیر آمریکا در سازمان ملل: ترامپ توافق بد را نمی‌پذیرد. او کار این رژیم را تمام میکند
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/25418" target="_blank">📅 16:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25417">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ارتش اسرائیل و سازمان «شین‌بت» اعلام کردند که طی ۲۴ ساعت گذشته، زیرساخت‌های حماس را در سراسر نوار غزه منهدم کرده‌اند. از جمله این زیرساخت‌های منهدم‌شده می‌توان به یک مرکز فرماندهی و دیده‌بانی در منطقه «درج-تفاح»، یک سکوی پرتاب راکت و سه انبار تسلیحات اشاره کرد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/25417" target="_blank">📅 16:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25416">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">چند آبگرمکن گازوئیلی و پیکنیکی گازی به سمت تنگه پرتاب شد
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25416" target="_blank">📅 16:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25415">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddvJY01NTqMFjjyAZOxJejwMKOl6Ol4kScxm_eoDdJDY9oHNVaCtUc1jombj1zY4QVcn3qaPuplcsv1AgPE2J0CRLC5Dk7vFERTkH9kptfYn7KalXxe85SqV20ojfA0I6pcNO7J4g5Vpzmfk0AEg54uSfgFaE2dvtiqjtXHHmkkO3Q6PSg_ZaxiNBJaG3S167KHCtsAI186RfoMPS4afcFy8ZvnzShzTmwLNiFu1qbzbfl8k8JYEnVPJj46w5CX-1CRGuTLIYzJb6hnwjNiL6ULloUVQqBOQ_eM5UqiiFzpZs_omLC290ep8DQvRJ3lvLSNxVnnH2mGD8TAQEPwCwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایلان ماسک : با ترامپ موافقم وقتشه اوکراین یه رهبر جدید داشته باشه.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/25415" target="_blank">📅 16:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25414">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enwVHq7oqZrKjtfRhSjH_mGwbX5znTmDrxbMkVRzEvBbFB1tpnbslcvoag1T5Szy2CT2mTLcYI4_c-8IHDvxoy5WhZl1mDlBoSY-n832wSG_g3TwQiw6e_82oneelPFfKLiAEKANP5rEJXm5Quc7Z-mfOqWo8nCz5v-jR9NhiRSZ_jvzjK3QxpbIQzJvplEyJteYG_KYof2g6MQnlmwY_QgX-IbEvO5hCfaMipflabnB0Uew-tgjaoleRcGTl6YDtiMiMNFBbJQX2TgyEp4M5M5tTtWdrJgOo-hJo82K8eUII6TAmAeABx8yBhQgqqDT29Fdj9vi12j1gCC6QUOOtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامبیز حسینی‌ مجری‌ اینترنشنال ، مریم رجوی را در پلتفرم ایکس(توییتر سابق) فالو کرد
@WarRoom
⚠️
⚠️
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25414" target="_blank">📅 15:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25413">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">خبرنگار رویترز: آمریکا ممکن است نیروهای نخبه را برای عملیات های خاص قبل از شروع جنگ در ایران مستقر کرده باشد
.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25413" target="_blank">📅 15:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25412">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cb45997b4.mp4?token=KHDoV24a3EWvytmT-moxCNN2TTc-K433gPvVfXPsSDaPv6xgvw70v1fFrmQynGUFm5sL7e2D0qPjqQUOHi3WI8uY2A_CDrUn1IlCUSxwy9r3Cxu7T37Wnm9Q3lPbQemDWiAf4vjmiHIfQEpnNXLRxHCeJqSOmPlL59HaVcg9VnlsvXQ4qHQYVIQK4hrp7SngJPbrm87EbUg4TBmrTstePjbynH7SlpC1iRIcvFZg3HVgjdPFiCF0MkHW_lwmwpB9juXsuESfJNdTETNK5CjDDZ8AAbWBhufNBZALN5ZO4rbv_zjKXruDJylyTfZVIod5cGMSgFrT3BC2eY2IZMYEMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cb45997b4.mp4?token=KHDoV24a3EWvytmT-moxCNN2TTc-K433gPvVfXPsSDaPv6xgvw70v1fFrmQynGUFm5sL7e2D0qPjqQUOHi3WI8uY2A_CDrUn1IlCUSxwy9r3Cxu7T37Wnm9Q3lPbQemDWiAf4vjmiHIfQEpnNXLRxHCeJqSOmPlL59HaVcg9VnlsvXQ4qHQYVIQK4hrp7SngJPbrm87EbUg4TBmrTstePjbynH7SlpC1iRIcvFZg3HVgjdPFiCF0MkHW_lwmwpB9juXsuESfJNdTETNK5CjDDZ8AAbWBhufNBZALN5ZO4rbv_zjKXruDJylyTfZVIod5cGMSgFrT3BC2eY2IZMYEMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون تنگه هرمز یک کشتی در آتش میسوزد
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/25412" target="_blank">📅 15:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25411">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3515553bf.mp4?token=RFNIZKO6jKPPEaO6afr8maDixL5AwdkZs94xKYqG1D36Ujp-7sWUxZ9cUkR0BFrw3zE1OrmJwPp1U2mTAe62kniDb374lmUddV9lVfr5-MV1r9V56r--eomnu-MaOYQoGsTOVhzvuXOFFuN1E1JGbwD1cDKPDq7De8Hpfo5tEcuH90Q5H0JPInLhNYn7kORsjlTs3H_zLiXPPdXTM3fdfcIhqgWM2lDErXCe8_eCn3BlhUN1rHQZMnqJl8AVSCxU4VzyfdF-rKhEVi3nmL-RArHlufdZ_gY632kvqX8B_RoKXGdGVlyvN0fJ-78AUhHlTbMu3RnEgO1MJPpnpTJOBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3515553bf.mp4?token=RFNIZKO6jKPPEaO6afr8maDixL5AwdkZs94xKYqG1D36Ujp-7sWUxZ9cUkR0BFrw3zE1OrmJwPp1U2mTAe62kniDb374lmUddV9lVfr5-MV1r9V56r--eomnu-MaOYQoGsTOVhzvuXOFFuN1E1JGbwD1cDKPDq7De8Hpfo5tEcuH90Q5H0JPInLhNYn7kORsjlTs3H_zLiXPPdXTM3fdfcIhqgWM2lDErXCe8_eCn3BlhUN1rHQZMnqJl8AVSCxU4VzyfdF-rKhEVi3nmL-RArHlufdZ_gY632kvqX8B_RoKXGdGVlyvN0fJ-78AUhHlTbMu3RnEgO1MJPpnpTJOBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه ‎صادر کردن دستور یک حمله تلافی‌جویانه قاطع علیه حوثی‌ها توسط محمد بن سلمان، ولیعهد عربستان سعودی
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/25411" target="_blank">📅 15:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25410">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سخنگوی سازمان انرژی اتمی: منافع‌مان را یا با دیپلماسی می‌گیریم یا با نبرد. اگر منافع ما در دیپلماسی به دست آید، چه بهتر. صنعت هسته‌ای ریشه در ایران دارد و نمی‌تواند با ضربه از بین برود؛ متاسفانه دشمن این را هنوز هم نفهمیده.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/25410" target="_blank">📅 14:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25409">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a78cb2396.mp4?token=lOKCWuVdrVP_oEm5bipfM1Nr0TW7-S1hBseMKCZXwaHZP6Rdihd8eXcfBGytsMIII6CfsXNP1QV6OxffOD_jyYH5dmLpXK5w_9JfkLQ1kPIqavYOM8Pjo_Ev0Actv309HMkLG-NR7l047Qcsf-QPeQnTGrMu1q_g_4bRlOO0IWki4K4ffLlbHWhkzqKrsmwx6iW3OaVaZF3-9_Oac7QiKotKMB93waWikIMtysoiiHmMTAkzOxngIdll6HzvBzcvtS5lhJmP1IPJXjX3bAGOMC6twuJnWnVs974n-eaZH-w2mBckrvS9e5QxDD9b4Mip1IBaVNU1SqnGEfxl_v9uCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a78cb2396.mp4?token=lOKCWuVdrVP_oEm5bipfM1Nr0TW7-S1hBseMKCZXwaHZP6Rdihd8eXcfBGytsMIII6CfsXNP1QV6OxffOD_jyYH5dmLpXK5w_9JfkLQ1kPIqavYOM8Pjo_Ev0Actv309HMkLG-NR7l047Qcsf-QPeQnTGrMu1q_g_4bRlOO0IWki4K4ffLlbHWhkzqKrsmwx6iW3OaVaZF3-9_Oac7QiKotKMB93waWikIMtysoiiHmMTAkzOxngIdll6HzvBzcvtS5lhJmP1IPJXjX3bAGOMC6twuJnWnVs974n-eaZH-w2mBckrvS9e5QxDD9b4Mip1IBaVNU1SqnGEfxl_v9uCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: حله … اشکالی نداره این موضوع منو آرام می‌کنه،  آن‌ها احتمالاً پیش از انتخابات کمی بیشتر داستان درست کنند ، چون فکر می‌کنند این کاراشون به ضرر ما تمام می‌شه . ما می‌توانیم خیلی سریع به این داستان پایان بدیم باورشون نمیشه چقدر تمیز کارشون تموم میشه . آن‌ها نمی‌دانند من چقدر با آن‌ها خوب تا کردم؛ نمی‌دانند چقدر تازه باهاشون با ملایمت رفتار کردم
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/25409" target="_blank">📅 13:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25405">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sBHWCfAP14e0tGtsk7pw0XHfrr-cDI9IJamoFAi098phQkpMFgTELc-AkEi4WzpFAC1i5pP-WnPjRE-Y7kh37YvPDWVn8kJs58Ei7n0kzxhOwi48-5SDh6KJ7nNziGuP7XTmDoV3zdb7uQ5bQWYDGpzmNOGnsjnINHPlOq1B2uEbe-mgIgTg_4TbQOBWcNn3ZdukkABfH5Pw-R9rTUyRKNao5oOBJR03Ycld7l6U6Gr0GYT-WPw10C50nQUZGrZcwWhIuTgBRHkSg-xXRvaFZvJhkS47vBOBuxb-UqLrbc8gooMZ3SDocmQeL_rp3995nMrCUkclyYn7MUINMli24w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KBfqdFdE-_akPxqk9_bWRxErengLATZ8Zl2Pv4aP5dzuQdKoFktA4L3hZkwKeLP6imdgcZvISn-zffJ9Xyl3uaFuOMhl4Imk4_t47lr9VUwytWATGDcrQaLCBtz37a3PjSAopb2nORyWXjnAWg5-m82i5jjodPmGvKZasL8Z1TbCxOVZeYkHhUPN-TGnga62hFiDvjQUIxAezhFfNB-Lp7jV9RbXWrhRT_EfmMdHe6aKT87rv3fEs7ezifO2ZZ_QNkN84eQN1mn9NLyaon3UEuUUYyPULTztkP6UGgLSdFRzQEzoEAaJYWPbdmKWJxtmNRnLh8PK70uSu1ooLi7Seg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U-jObulJuTruZ7b2szqw9lPlVM58Fbq18_vm2RhvWD20DOZ6BgAAwUQni3WaW_ZGo2zyebSHtKKfsLRbFXpUPOaEnsEzCTQN_-8DsCYmpKpOu5mCGYRxhfDxKR8LdK6qNk1zJjKUYL4I6SyBVQ6OAgNTmvDiO10VuivTc7axw8nwG7Onf0zZyQeUj7WPlL-tq6oJu4tQmDgAnm-Z_7ZZsYV0w0ImS9ATJC_MX47wYnNs5HG_RqcHbxB1tGPlx_R14SqzKxaTYmj4HAV5vr40nRvsj7wWZFb5tMfxNCj4ZYwhXqMe0hMsLAOD26WLSx3M7IyN_YgsHjtt0FjrUk6S7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آسمان تهران ، آبگرمکن رو کات دار زدن
😂
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/25405" target="_blank">📅 12:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25404">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گزارشهای بسیار از‌ پرتاب آبگرمکن از اطراف تهران/کرج
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/25404" target="_blank">📅 12:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25403">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">محمدمهدی هاشمی، نویسنده روزنامه خراسان نزدیک به ممباقر قالیباف ، در یادداشتی که امروز، منتشر شد، مدعی شد با بررسی تحولات و اظهارات هفته گذشته ترامپ و روبیو می‌توان نتیجه گرفت که
آمریکا و اسرائیل تصمیم خود را برای آغاز دور بعدی جنگ گرفته‌اند
. او نوشت تبادل پیام‌ها میان تهران و واشنگتن نیز احتمالاً تا پیش از درگیری بعدی تأثیر ملموسی نخواهد داشت
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/25403" target="_blank">📅 12:22 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25402">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqrBdLvmYkEkalncD6-RKZMO4MvppoPKVDEMotmsgEtVuu4QG6QtvcVt_sigyC7qaw5XN7GPC4j9XcLjdzJBhk1meXeqhOswaEJfFObQGwHCbQH-rwU3nzz_Qv0-ABmfNefF5W8u_RvyqLOJWKz8XoWNi9pKz0IfojWqhbAhED-cGR9EEjOO2UJhvHMHYR2KCcg3IxmqS6M1V1M8jBJ0kc5OplU9TbDTHZoAHj1ptlcDC7bDzStl7wWTv8ycXdZGqw9NCrMt2TROuMEFSoNst0lMj-c3K65kGJ6ECtSTRGvFlRTl28BPM6n_ui6VLb1Tx_OZNbnXnWivm7UgcnMyLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز جهانی دختر بر تمام دختران ایران زمین خجسته باد.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/25402" target="_blank">📅 12:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25401">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuqHiqDntn8pSfN6UCcYQPnULKSy69mH1U7ICY4h4d3N_PMKoqtxvvD9GJFhbQi2sbPERgG6fxVRoTjOIx1meJziFjiXFpxfhGDECFbc9ypMSvw6E-ph7ZOIKyuFl07yu95OlI5dRMWFmwanGMrPrZ0ar7009SGyJLlG-hgvbsPwInMEWL9E3Dec2vtNfFZ2Tca5nw2zO6G2twtX59OFUCY68rZSYoLwFIQUr-sIdvVwKasmra9dv4hi-6u0BlO-njcxsBslO-2gTzxl0SnKWtGYDXpfT1PZJQANrndVoeamDp1CGbFymNK9FNsKVx5BvJmZPeT1uwxdaBBRaFCuhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود یک ساعت پیش، چندین انفجار در نزدیکی کوه صفه در اصفهان، واقع در مرکز ایران، شنیده شد.علت این انفجارها هنوز مشخص نیست؛ با این حال، بگم که این کوه محل استقرار بسیاری از پرتابگرهای موشکی رژیم هم است.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/25401" target="_blank">📅 11:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25400">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پزشکیان : اگر ما ایرانیان کنار هم باشیم، نمی توانند ما را بشکنند و به ما آسیب بزنند
@WarRoom
🤡</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/25400" target="_blank">📅 11:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25399">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2f5a8ccb.mp4?token=tRLHdXQsG5GbA6l8lDmLzLtonUhL2RJZ8JrWOl6sJYl9ejAsJwVVpRpC-Ygdxi19J0r1FwFhzaYAz8_oM9A9pSJQKbAnmMVYOaF4IDaYqRPP6wxZMKHh_5WYZCd3tdjX0YnbQIWLys2EtM8RlCWX-wpzJebZ43t-PXMad1qKolzcMFwGP_iyOIVW9dn7FmZ8fPvtnCW9WHk_7wAiUDkU-ljfanUo_-sNcN3jX-IArcW7r2sf6L5W7d27NnBspHikZks7FMR-fMylXpo4zCZ_g5X4DVN9cp_Xz2O6EBnDRKtxpMUcRpfN38LYWlc0B7k_8jCU7nzWVQw2AI0f7EEdAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2f5a8ccb.mp4?token=tRLHdXQsG5GbA6l8lDmLzLtonUhL2RJZ8JrWOl6sJYl9ejAsJwVVpRpC-Ygdxi19J0r1FwFhzaYAz8_oM9A9pSJQKbAnmMVYOaF4IDaYqRPP6wxZMKHh_5WYZCd3tdjX0YnbQIWLys2EtM8RlCWX-wpzJebZ43t-PXMad1qKolzcMFwGP_iyOIVW9dn7FmZ8fPvtnCW9WHk_7wAiUDkU-ljfanUo_-sNcN3jX-IArcW7r2sf6L5W7d27NnBspHikZks7FMR-fMylXpo4zCZ_g5X4DVN9cp_Xz2O6EBnDRKtxpMUcRpfN38LYWlc0B7k_8jCU7nzWVQw2AI0f7EEdAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ: قبلاً هم گفتم که باید برای خاموش کردن آتش به ایران حمله کنیم . ما با یک مشکل جدی روبه‌رو هستیم؛ با دولتی بسیار شرور که رتبه اول جهان در حمایت از تروریسم را دارد. نمی‌توان چنین سلاحی را در اختیار آن‌ها گذاشت؛ آن‌ها بدون هیچ تردیدی از آن استفاده خواهند کرد. می‌دانید، خیلی‌ها حاضر به استفاده از چنین سلاحی نیستند، اما آنها…
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/25399" target="_blank">📅 10:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25398">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1b_y1ilPxWWsyVx1pXjvrXGZ1DEDN4dWvwVuPvHgPcA-ISKELH7q1DZxlLALdTF0v0aOAWDVSYDU_8sJxD5t85MolfL3KeM7fKtyOw3-Jeg2josmU-qyYaKqZkp1OxlbR5FVzuzm2FVHVXxyfGWSFmPWehxBGxkAZHy9yt6lrBtb_CVdKefFJUf2Wp14Kba2sSqoJjC2MsBdai9dic12b8SePorARfyjDMMR4wJZJBCPrpZO3dItw3IMwuU0uQJ1crIdFCjZhW7DRnCu-TqBT8z3B2ut8Use69SC2cQMNwOU9tP2Djvai_gNd3-4W5G6WSOQToWbQ0lN6ZHmIrUjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاطمه مهاجرانی، سخنگوی دولت : پروژه ایجاد ترس از ایران و تضعیف روابط این کشور با جهان، «افسانه‌ای است که دشمنان ترویج می‌کنند»
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/25398" target="_blank">📅 10:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25397">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce60ee997d.mp4?token=iOT6Qv0UxwyWxpcMcWSJNB6PoRE4y_B3ZvWF3CiXMDLo_xB5_4esOpcL6IJlDV-EqfokCOfHhI6qtZI1sWuYVtaHkNai2upOE_MJo8CcyPad1a2yksSJsQhJjAwbnSGbSHwWm2kQKrd6w5zusuYguoz6VueK-gGlAaGTRg9BOKwQQm-bJnUmCFDfs-9y_-GS9TQyQtRaEExsWj28FDlE_BY1RRomO9_SjFznIpRR0RDDoYHqcxRa1_zlyeZw-0wOotE3uwHSJgeldP0h6J7jiM-uJrJB9MoM7x0SveP4BrHg4xVPwuA0AguutD_h9Doriv61vwLvMbilx4DpcKORAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce60ee997d.mp4?token=iOT6Qv0UxwyWxpcMcWSJNB6PoRE4y_B3ZvWF3CiXMDLo_xB5_4esOpcL6IJlDV-EqfokCOfHhI6qtZI1sWuYVtaHkNai2upOE_MJo8CcyPad1a2yksSJsQhJjAwbnSGbSHwWm2kQKrd6w5zusuYguoz6VueK-gGlAaGTRg9BOKwQQm-bJnUmCFDfs-9y_-GS9TQyQtRaEExsWj28FDlE_BY1RRomO9_SjFznIpRR0RDDoYHqcxRa1_zlyeZw-0wOotE3uwHSJgeldP0h6J7jiM-uJrJB9MoM7x0SveP4BrHg4xVPwuA0AguutD_h9Doriv61vwLvMbilx4DpcKORAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: درباره حمله مرگبار حوثی‌ها به فرودگاه ریاض چه نظری دارید؟
ترامپ: به‌نظرم وحشتناک است
خبرنگار: آیا آمریکا را وارد این درگیری خواهید کرد؟
ترامپ: خب، به‌زودی متوجه خواهید شد.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/25397" target="_blank">📅 10:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25396">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سازمان حقوق بشر کارون: بیش از ۱۰ کارگر متخصص و بومی شرکت پتروپارس در هویزه، پس از اعتراض به اخراج و تمدیدنشدن قراردادهای کاری خود، به ۷۴ ضربه شلاق تعزیری و پرداخت ۲۰۰ میلیون ریال جریمه نقدی (۲۰ میلیون تومان) محکوم شده‌اند. به گزارش این سازمان، حکم شلاق اجرا شده است. این کارگران که در پروژه توسعه میدان نفتی آزادگان جنوبی سابقه فعالیت داشتند، پس از تجمع اعتراضی با شکایت شرکت و پیگیری قضایی روبه‌رو شدند. حکم در ۱۳ تیر ۱۴۰۵ صادر شده و کارگران همچنان خواستار بازگشت به کار هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/25396" target="_blank">📅 09:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25395">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/564786cc15.mp4?token=oVfFumcuLlT7Mvh95uuaBBSRblNN0VwISLNMTEMDgxdHbGzUiAYvkMuaMceZnVuVRFvdyh2F3ZOwNmyC_65wfOKRn1JS8HGCJYRcizR8P6fsP-H55BU3SPSfT0bp3xweMtNWFMenxThBjZs8PIkxg7QI1G3YkTYm8S6RultJYb0j6rZMbYN52rn2PAA6dij2QOSZUqIH_vW8py7ns7OdQx0dw88xEL8UZ9wz11cIn2eXVrRrVjorcia95_l-XCsU5Dft3r9Jpar3HciQ_vBGFI0niiraQ4VFWY_lwLLukzj8zbwwkjS7IR7jYgbhEBv_Uppm47Dmbw9rdrIRrhPOkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/564786cc15.mp4?token=oVfFumcuLlT7Mvh95uuaBBSRblNN0VwISLNMTEMDgxdHbGzUiAYvkMuaMceZnVuVRFvdyh2F3ZOwNmyC_65wfOKRn1JS8HGCJYRcizR8P6fsP-H55BU3SPSfT0bp3xweMtNWFMenxThBjZs8PIkxg7QI1G3YkTYm8S6RultJYb0j6rZMbYN52rn2PAA6dij2QOSZUqIH_vW8py7ns7OdQx0dw88xEL8UZ9wz11cIn2eXVrRrVjorcia95_l-XCsU5Dft3r9Jpar3HciQ_vBGFI0niiraQ4VFWY_lwLLukzj8zbwwkjS7IR7jYgbhEBv_Uppm47Dmbw9rdrIRrhPOkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پنتاگون آمار تلفات نظامی آمریکا در جنگ با ایران را به‌روزرسانی کرد: با اضافه شدن ۲ کشته و ۴ مجروح به آمار قبلی، شمار نظامیان آمریکایی کشته‌شده به ۲۱ نفر و تعداد مجروحان به ۸۶۵ نفر افزایش یافت. @WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25395" target="_blank">📅 09:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25394">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">شفق نیوز نیز به نقل از یک منبع امنیتی عراقی گزارش کرده: دو هواپیمای عازم ایران بامداد یکشنبه پس از آنکه مقام‌های ایرانی به دلیل ملاحظات امنیتی اجازه ورود آن‌ها به حریم هوایی ایران را ندادند، به فرودگاه نجف بازگشتند.هویت پروازها هنوز روشن نیست. جزئیات بیشتری درباره علت این تصمیم هم اعلام نشده است. تردد غیرنظامی در حریم هوایی عراق نیز به‌طور موقت متوقف شده، اما بسته‌شدن کامل حریم هوایی تأیید نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/25394" target="_blank">📅 09:21 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25393">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">آخرین آمار حمله به فرودگاه ملک خالد ریاض: مقام‌های سعودی کشته شدن ۱۲ نفر و زخمی شدن ۳۰۹ نفر را در حمله موشکی روز شنبه تأیید کردند. در میان کشته‌شدگان، ۴ شهروند سعودی و ۸ تبعه خارجی از جمله
یک شهروند آمریکایی
حضور دارند. مقام‌های سعودی از وخامت حال تعدادی از مجروحان و وارد شدن خسارت به فرودگاه خبر داده‌اند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/25393" target="_blank">📅 09:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25392">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اتاق جنگ با یاشار : میانگین ۸ نظرسنجی انتخابات اسرائیل تا دیروز: حزب لیکود به رهبری بنیامین نتانیاهو ۲۲٫۴ کرسی و حزب یاشار به رهبری گادی آیزنکوت ۲۱٫۲ کرسی پیش‌بینی‌شده دارند. در سطح بلوک‌ها، بلوک نتانیاهو ۵۵ کرسی و بلوک صهیونیستی(یک جنبش سیاسی و ملی‌گرایانه است که با هدف ایجاد و سپس حفظ یک خانهٔ ملی برای یهودیان در سرزمین تاریخی اسرائیل شکل گرفته و توهین نیست )مخالف او ۴۸٫۴ کرسی دارد؛ احزاب عربی و سایر احزاب نیز در تعیین امکان تشکیل دولت نقش مهمی خواهند داشت. برای تشکیل دولت، کسب حمایت دست‌کم ۶۱ نماینده از مجموع ۱۲۰ کرسی کنست ضروری است.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/25392" target="_blank">📅 09:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25391">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سنتکام : محاصره دریایی کشتی‌های ورودی و خروجی بنادر ایران از ۲۳ تیر از سر گرفته شد و طی سه ماه اجرای مجدد آن،
۴ کشتی از کار انداخته شده و مسیر ۱۳۵ کشتی تغییر داده شده است.
نیروهای ما در همین مدت ۱۰ نفتکش مرتبط با شبکه مالی غیررسمی چندمیلیارددلاری سپاه پاسداران را منهدم کرده‌اند.همچنین از دریانوردان خواستیم به هشدارهای محاصره توجه کنند و هنگام تردد در دریای عمان و مسیرهای منتهی به تنگه هرمز، اطلاعیه‌های دریانوردی را دنبال کنند و در کانال ۱۶ ارتباط رادیویی دریایی با نیروهای ما تماس بگیرند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/25391" target="_blank">📅 08:36 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25390">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09a18e92af.mp4?token=WGS4Qw__lQo58If76exTliCqJ8kHXlamdu0_vlbG2pfAsU8toUrai1VjaAzNSaKjgKCPEBJIshI679Sj8ITjHtkPK4KXK_iWJa43NH53MlFl6eNlwg6-PPdcf3yU2Zg5fD-v32QO-CegzJbOn7IBSyFJfASFaB4KX-NQPie3vC8wCrGSf8FBzfA1rOpDapa7tO7gV6cpR4iZqGM--40aNO_BGg0Fal3useICO2bp10148dd4UeX55RFZSFfmpRXIuFkRXANoabLeT1QqerszgLppu-RtZjB-9lU0rJ8S7ad-rYPROKteCEshtrYZlQIK2zC8P1VvpPMbvFCczj3dFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09a18e92af.mp4?token=WGS4Qw__lQo58If76exTliCqJ8kHXlamdu0_vlbG2pfAsU8toUrai1VjaAzNSaKjgKCPEBJIshI679Sj8ITjHtkPK4KXK_iWJa43NH53MlFl6eNlwg6-PPdcf3yU2Zg5fD-v32QO-CegzJbOn7IBSyFJfASFaB4KX-NQPie3vC8wCrGSf8FBzfA1rOpDapa7tO7gV6cpR4iZqGM--40aNO_BGg0Fal3useICO2bp10148dd4UeX55RFZSFfmpRXIuFkRXANoabLeT1QqerszgLppu-RtZjB-9lU0rJ8S7ad-rYPROKteCEshtrYZlQIK2zC8P1VvpPMbvFCczj3dFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام :  نیروهای آمریکایی دیشب ، یک کشتی باری تجاری را در دریای عمان پس از بی‌توجهی خدمه به هشدارهای مکرر و تلاش برای عبور از محاصره دریایی بنادر ایران، از کار انداختند. به گفته سنتکام، یک جنگنده آمریکایی با شلیک مهمات دقیق به بخش عقب کشتی با پرچم پاناما به نام
M/V Ocean Molica
که با نام «Arika Sun» نیز شناخته می‌شود، سامانه پیشران آن را کاملاً از کار انداخت؛ اما به خدمه آسیبی نرسید. این کشتی پیش‌تر از یکی از بنادر ایران حرکت کرده بود.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/25390" target="_blank">📅 08:27 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25389">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65cc3b20f5.mp4?token=ka1wvzSmaXa-fL8uNvrmAGM0lTcCdJU3hWiZjaKYDeokDcIDV1di7OmhaEA82KcfmbPLUvfOLbghloHbzeM071I3jGKYqmJpHxwC_wOiesfI0wz0Hl6tX1lKF90y0m07s5VWhC3XVkDCZoW97NkeHpeW12eR4QAWk_PtvfjJ575nVczV9BdtfNPfS2m7UKYpS74fT0pHRfQrFhRI0Pqa2syP_oScAyDzoYeIoco4SBYs-XiOw510E6zX3CVZILwBuOSEcKYh2mOnQvDcCCD6sgSFBhnTqoCxPYUsToMxh8HHhq8G00h3Gxz8pCDbzsIZLbY2-A68-M8XUjbIoeb6VzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65cc3b20f5.mp4?token=ka1wvzSmaXa-fL8uNvrmAGM0lTcCdJU3hWiZjaKYDeokDcIDV1di7OmhaEA82KcfmbPLUvfOLbghloHbzeM071I3jGKYqmJpHxwC_wOiesfI0wz0Hl6tX1lKF90y0m07s5VWhC3XVkDCZoW97NkeHpeW12eR4QAWk_PtvfjJ575nVczV9BdtfNPfS2m7UKYpS74fT0pHRfQrFhRI0Pqa2syP_oScAyDzoYeIoco4SBYs-XiOw510E6zX3CVZILwBuOSEcKYh2mOnQvDcCCD6sgSFBhnTqoCxPYUsToMxh8HHhq8G00h3Gxz8pCDbzsIZLbY2-A68-M8XUjbIoeb6VzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سناتور جک کین: پس از انتخابات میان‌دوره‌ای، احتمالاً ترامپ علاوه بر فشارهای اقتصادی، در کنار اسرائیل فشار نظامی گسترده و کوتاه‌مدتی علیه جمهوری اسلامی اعمال خواهد کرد تا زمینه سقوط رژیم فراهم شود. به گفته او، در مرحله بعد، سازمان سیا و موساد می‌توانند با تضعیف حکومت و کمک به شهروندان مسلح مخالف، به پیشبرد این روند کمک کنند. کین معتقد است این سناریو محتمل‌ترین مسیر پیش رو است.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/25389" target="_blank">📅 02:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25388">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سخنگوی نیروهای ائتلاف: حمله به فرودگاه بین‌المللی ملک خالد، یک عمل تروریستی است و به شدت به آن واکنش نشان خواهیم داد.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/25388" target="_blank">📅 02:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25387">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اخ اگه تاریخ تکرار‌ بشه ….</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/25387" target="_blank">📅 01:18 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25386">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fdb2d73bd.mp4?token=ojYvDEEx9y1rBO0BhqUl8nv55neGMpTXcwGGRxvle9PFArWPLcICInI3bpnLH-6e1XZ5USvJaGmjzIUJGFUtofLkpHDedcEkzRdzIp08f_Z9bMH1HZcvw8J03Bmi8c17MtotK7ZIDty0xdeli5cHZ6w0k2v1GdyCam3VSUCinnKUh1_ojvQwAgLEpnAqjgRjA9syZsO13DrTHcDyyPJ4o2x_lnBRG7t7uzNMo78lIfs8IooSnAPSx2Bw2jIYpLVD78Idt4rvSKqKr_RbA144gyArqSHU2VVQzNdhkuCb8EnQCBYtLePg7_cWd2FrGIF_eKUNzIwY7JSmLWIBqDB5nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fdb2d73bd.mp4?token=ojYvDEEx9y1rBO0BhqUl8nv55neGMpTXcwGGRxvle9PFArWPLcICInI3bpnLH-6e1XZ5USvJaGmjzIUJGFUtofLkpHDedcEkzRdzIp08f_Z9bMH1HZcvw8J03Bmi8c17MtotK7ZIDty0xdeli5cHZ6w0k2v1GdyCam3VSUCinnKUh1_ojvQwAgLEpnAqjgRjA9syZsO13DrTHcDyyPJ4o2x_lnBRG7t7uzNMo78lIfs8IooSnAPSx2Bw2jIYpLVD78Idt4rvSKqKr_RbA144gyArqSHU2VVQzNdhkuCb8EnQCBYtLePg7_cWd2FrGIF_eKUNzIwY7JSmLWIBqDB5nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:میتونیم خیلی سریع به این جنگ پایان بدیم. اونا هنوز نمیدونن چقدر باهاشون راه اومدم و مهربون بودم.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/25386" target="_blank">📅 00:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25385">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1194293ab9.mp4?token=FlKWnR9JwDOLe9dXrZ40zwlI8gq7mjIKVrDBXoOoGy57s05eWWwWKeJlny7EPkGyG6y-vkiWKvSJsISfe8JVHyQSXDy2h1CUB7HFJN9iDb9vxV5L55tEIUFf4Aw9Tl9bwFeg493Jj2iEaEm9aEAc6lAkd5fU1JTYOJjEP6wqnfwrqJ_JVFBJi5qtxY-UHsMVsyWC3s13fcyThlfKzlX_VXO_BgoQdcj0CrpQzbDqd5LmWtiIp8XIw9U95MP8dVdj1a_J0cAqvbNamU6WeDH_063OahtdgMDD3OPFJGUrOr3EF5hXxioH2Tsj4_dI5oOxG6p1To30PrW4S15aR1XmBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1194293ab9.mp4?token=FlKWnR9JwDOLe9dXrZ40zwlI8gq7mjIKVrDBXoOoGy57s05eWWwWKeJlny7EPkGyG6y-vkiWKvSJsISfe8JVHyQSXDy2h1CUB7HFJN9iDb9vxV5L55tEIUFf4Aw9Tl9bwFeg493Jj2iEaEm9aEAc6lAkd5fU1JTYOJjEP6wqnfwrqJ_JVFBJi5qtxY-UHsMVsyWC3s13fcyThlfKzlX_VXO_BgoQdcj0CrpQzbDqd5LmWtiIp8XIw9U95MP8dVdj1a_J0cAqvbNamU6WeDH_063OahtdgMDD3OPFJGUrOr3EF5hXxioH2Tsj4_dI5oOxG6p1To30PrW4S15aR1XmBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ
رو یه مردم آمریکا
: داریم به این فکر می‌کنیم
( از باسن سوزی رژیم )
که نام تنگه هرمز را به تنگه ترامپ تغییر بدهیم.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/25385" target="_blank">📅 00:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25384">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46a5493e67.mp4?token=eqg1A5_KcWbOg5dFZKXOY27QE6FkQxjyvcPqccTCG2-wI71_ve2XMHBKxu2LU5hMlaOaioiDesCOw5GHFuOHiFRa0N4clKmDniPdeMpP2uWQxW2x9ohX61FQsExaEdPO2XzzxoSqf1yA88lW06GtMg-QOMP9OHdJoPBOkjXTiuml1KiHbtLm8WUdcur9mkyuYQMLpmrBe7fjlnQu6j8hiEESjjFBQBRC6iJa5mBGF47LB0sQFx7c5a9ad2jAZKgJltFUnpMNCKHc-PzPMxLYfA_jz9_fT9EhsvTwpCoAQLM9-qV0Kx_Fw0rn8DZpjUcGvhj8ib7tIGBivkhRuGiIWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46a5493e67.mp4?token=eqg1A5_KcWbOg5dFZKXOY27QE6FkQxjyvcPqccTCG2-wI71_ve2XMHBKxu2LU5hMlaOaioiDesCOw5GHFuOHiFRa0N4clKmDniPdeMpP2uWQxW2x9ohX61FQsExaEdPO2XzzxoSqf1yA88lW06GtMg-QOMP9OHdJoPBOkjXTiuml1KiHbtLm8WUdcur9mkyuYQMLpmrBe7fjlnQu6j8hiEESjjFBQBRC6iJa5mBGF47LB0sQFx7c5a9ad2jAZKgJltFUnpMNCKHc-PzPMxLYfA_jz9_fT9EhsvTwpCoAQLM9-qV0Kx_Fw0rn8DZpjUcGvhj8ib7tIGBivkhRuGiIWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: «حاکمان ایران می‌گن: ما همه رو می‌کشیمممم! همه روووو!
همچنین می‌گن: الحمدلله! الحمدلله! الحمدلله!
منم می‌گم: بابا، شماها دیوونه‌اید! واقعاً دیوونه‌اید.»
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/25384" target="_blank">📅 00:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25383">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">رویترز: در حمله روز شنبه به فرودگاه بین‌المللی ملک خالد در ریاض، چندین نفر زخمی شدند و بیش از ۱۲ آمبولانس به محل اعزام شد. طبق گزارش گاردین، ده‌ها نفر مجروح و ۵ نفر در بخش مراقبت‌های ویژه بستری شدند. آمار رسمی نهایی تلفات حمله شنبه هنوز اعلام نشده است. ولی بر اساس‌آخرین اعلام رسمی عربستان، حملات امروز به فرودگاه ریاض و یک هواپیمای سعودی، ۳ کشته و شماری مجروح بر جای گذاشت
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/25383" target="_blank">📅 00:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25382">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/563c5da19b.mp4?token=JreEBSqfzwyE7S9teLQflaXUc76wVcKATqFdV48Jk8Kz7LRwnL-Aq7lnwSikXDDJVly-ra6S6hXgyiCl_D0mYGtQV4MRTMWqxS3TZDdG0wBRrfrfuuDGHfMpwdOTqui_JPJapWUXRWEtWSOZuUmscyMpCYn9vEi8FXoJ7z3yfwbV9Di2Dg6syWvgiBKlmockrbBmGVGYRNELwEl_0wPade0evb-BOc3wJb7PhrtAIKpneiOfkXzAOdk8CQC6lsgki8cB6g2s4dKchSEeUdymRz7XBsQ2BycoVMzo2x1MWQEIzQfd0TxLflcJsdSGCOFrkhVVlhq7uSSlSptHEDLIJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/563c5da19b.mp4?token=JreEBSqfzwyE7S9teLQflaXUc76wVcKATqFdV48Jk8Kz7LRwnL-Aq7lnwSikXDDJVly-ra6S6hXgyiCl_D0mYGtQV4MRTMWqxS3TZDdG0wBRrfrfuuDGHfMpwdOTqui_JPJapWUXRWEtWSOZuUmscyMpCYn9vEi8FXoJ7z3yfwbV9Di2Dg6syWvgiBKlmockrbBmGVGYRNELwEl_0wPade0evb-BOc3wJb7PhrtAIKpneiOfkXzAOdk8CQC6lsgki8cB6g2s4dKchSEeUdymRz7XBsQ2BycoVMzo2x1MWQEIzQfd0TxLflcJsdSGCOFrkhVVlhq7uSSlSptHEDLIJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/25382" target="_blank">📅 23:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25381">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fadf07bd65.mp4?token=r7RieFPYUXMkwriZ4ofZvJUhD3fiB1Zjb_pakK3rihWdSSxe4p7Uau8elndlv3Npm5pFYMdUP1Jd96fBYie0qm7uJ-IPeAB6x1vobUyxYUUI8Vmc2e0rgrzcKHm8CaL8VGaD63tv4ql6vVNdbzXd7e_2VoPdgEmijOot26aBqtfoHiSuTD0KasJTbb6jOyu0C3o02PkZNbjlo8LvtH-Jm_9lwkIu6QPBotszcRarGSM7jgKv0HUL3eRYSlrE60oDjHw6Fvb6xCBjd7N6RqG9mDxsWEzLfVhRTd5cJGVj8_VKxcmx7uq6UXx4jUmrjFRFeGwRakymXJqHOqfmssgmvoM8LI4i828kn9pL1CxiTTSQZTv97I9tStpfKFtsBiD8foFe2IPBCWIKoNV7m67Zju9tL9ffsxl900htSYAgANAAmhcm5VzdALCi0wXUoAPkvgkz-8jkgr9GoxX87GBvw9kWmwxJoWJ8atOsGzBbkjVOFzT7g8IMEkLiZvYFz1DPZKepdxdWnPQarf-Vj_cG-WdKX2cCD7n1Msf7DYrFN5xBTJQObGYhbDcn3qCwU3PPIHOqYAIHSuuGLVlmF9ipoHdJEeD760jVO_AbGsAyxYQl-QnzK1dvR46uq8CDUMcWFwZC8NNHmKBDqGPjqHCll6A0XBvzom8065Q5_vMm1VM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fadf07bd65.mp4?token=r7RieFPYUXMkwriZ4ofZvJUhD3fiB1Zjb_pakK3rihWdSSxe4p7Uau8elndlv3Npm5pFYMdUP1Jd96fBYie0qm7uJ-IPeAB6x1vobUyxYUUI8Vmc2e0rgrzcKHm8CaL8VGaD63tv4ql6vVNdbzXd7e_2VoPdgEmijOot26aBqtfoHiSuTD0KasJTbb6jOyu0C3o02PkZNbjlo8LvtH-Jm_9lwkIu6QPBotszcRarGSM7jgKv0HUL3eRYSlrE60oDjHw6Fvb6xCBjd7N6RqG9mDxsWEzLfVhRTd5cJGVj8_VKxcmx7uq6UXx4jUmrjFRFeGwRakymXJqHOqfmssgmvoM8LI4i828kn9pL1CxiTTSQZTv97I9tStpfKFtsBiD8foFe2IPBCWIKoNV7m67Zju9tL9ffsxl900htSYAgANAAmhcm5VzdALCi0wXUoAPkvgkz-8jkgr9GoxX87GBvw9kWmwxJoWJ8atOsGzBbkjVOFzT7g8IMEkLiZvYFz1DPZKepdxdWnPQarf-Vj_cG-WdKX2cCD7n1Msf7DYrFN5xBTJQObGYhbDcn3qCwU3PPIHOqYAIHSuuGLVlmF9ipoHdJEeD760jVO_AbGsAyxYQl-QnzK1dvR46uq8CDUMcWFwZC8NNHmKBDqGPjqHCll6A0XBvzom8065Q5_vMm1VM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترابری دیوانه کننده آمریکا در ۲۴ ساعت گذشته
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/25381" target="_blank">📅 23:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25380">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : فیک نیوز های دزد تلگرام یک عکس‌مربوط به خبر ۱۷ اسفند ۱۴۰۴ را قسمت بالایش را بریدند و پایین را به عنوان کیل لیست جدید اسرائیل معرفی کرده‌اند که جو بدن! فاکس نیوز در این گزارش قدیمی میگفت چندین مقام ارشد در جریان عملیات مشترک آمریکا و اسرائیل…</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/25380" target="_blank">📅 23:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25379">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbDCmirpS5V1gMg7Fn_CJI8ySfXhmWzHAI4pa8bp7Llxu80xJGWiSqHn903Zu4_zAoMUjjB3A7TIAkMn1rBOniK_fjRGWK367L6H3vwAnRln9z-h6r2WaSozyCpFVewzE2c36Wj3gTBdfxUYy90tmwyVYphhxS_Zm3vMEDYQ__gIQgwBNTAy-i-OsJw1zM8J4FSGC9F6AqGTpIP2vHZFtDiCvZGB1mJE_W33vUanUhrmvUIjtEw6N1fYhV0QzBk61rhYFx7WmvvVLuXBCU4M9bSWED_1Od1LXozgbUli1ysg2sdUWz5agGRr6GFO0pKej1Xw8W989fHh7H6Vb1X9wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث‌:
دموکرات‌ها، همراه با شرکای جرم خود، رسانه‌های خبری جعلی، در حال تلاش برای ایجاد روایت کاذب هستند که دونالد ترامپ آنقدر «نامحبوب» است که جمهوری‌خواهان شکست خواهند خورد.
در واقع، دقیقاً برعکس است. من آنقدر «محبوب» هستم که جمهوری‌خواهان پیروز خواهند شد و این موضوع با میتینگ‌های رکوردشکنی‌مان اثبات می‌شود (از جمله میتینگ در تنسی که تا چند دقیقه دیگر در آن حضور خواهم داشت — به زودی می‌بینمتان!).
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/25379" target="_blank">📅 22:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25378">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">باراک راوید، خبرنگار آکسیوس، به نقل از دو مقام آمریکایی و یک مقام اسرائیلی گزارش داد که آمریکا از اسرائیل نخواسته است پیش از انتخابات میان‌دوره‌ای آمریکا، حمله‌ای علیه ایران انجام دهد. این گزارش در حالی منتشر می‌شود که موضوع احتمال ازسرگیری عملیات نظامی علیه ایران همچنان مطرح است و پنتاگون نیز برای افزایش آمادگی نظامی در منطقه اقداماتی انجام داده است. انتخابات میان‌دوره‌ای آمریکا قرار است ۳ نوامبر برگزار شود.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/25378" target="_blank">📅 22:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25377">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/905abba452.mp4?token=GqUKHxCfS8h6fwmGw9ZBHXyWzvEMznkwOVuIvNPtgIIoip6Vg1Q6oYatPZRtqPINRRZX-y6hQdhcWecEulSwMM9_C_obgYt76SN2_NX_Mkw9oC3m8xtoDlvOr8ZBtomEicUTtqXROKlUz9oCeNqHIc4422a6kdyvBZk1UJ__tI34peMiuAxgtiDtr7xXIBzgawR3aidwlWX7O29dLFCWz6Ne4A4VHrd03QR2q0URYcAEiNhP0fFu0xMKTAaFQ-U2QJ724JvFtAqkGy4MlbheTojmjlF-apU-SEK0I7TnhJ6AxvYjZYdJeH9vm9vH5cmqC83Hnx2RMz23anKFqJhagg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/905abba452.mp4?token=GqUKHxCfS8h6fwmGw9ZBHXyWzvEMznkwOVuIvNPtgIIoip6Vg1Q6oYatPZRtqPINRRZX-y6hQdhcWecEulSwMM9_C_obgYt76SN2_NX_Mkw9oC3m8xtoDlvOr8ZBtomEicUTtqXROKlUz9oCeNqHIc4422a6kdyvBZk1UJ__tI34peMiuAxgtiDtr7xXIBzgawR3aidwlWX7O29dLFCWz6Ne4A4VHrd03QR2q0URYcAEiNhP0fFu0xMKTAaFQ-U2QJ724JvFtAqkGy4MlbheTojmjlF-apU-SEK0I7TnhJ6AxvYjZYdJeH9vm9vH5cmqC83Hnx2RMz23anKFqJhagg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران تصاویری از آتش‌سوزی گسترده و نشت نفت از یک نفت‌کش منتشر کرده است؛ نفت‌کشی که به گفته این نیرو، در تنگه هرمز هدف برخورد مین دریایی قرار گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/25377" target="_blank">📅 22:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25376">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">الجزیره: بمباران‌های اسرائیل، ۳ خانه را در شهر غزه و شمال منطقه تخریب کرد
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/25376" target="_blank">📅 22:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25375">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">شبکه ۱۳ اسرائیل به نقل از یک مقام امنیتی گزارش داد که اخیراً میان بنیامین نتانیاهو و دونالد ترامپ درباره گزینه حمله به ایران گفت‌وگوهایی انجام شده، اما هنوز تصمیم نهایی درباره حمله اتخاذ نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/25375" target="_blank">📅 21:04 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25374">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کانال ۱۲ اسرائیل به نقل از یک مقام ارشد گزارش داد که اسرائیل تا پیش از برگزاری انتخابات، هیچ حمله‌ای به ایران انجام نخواهد داد.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/25374" target="_blank">📅 21:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25373">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5697d70b60.mp4?token=t94AcMf0QXUipUYokTr8B4B3zoHlp1hnAorjLQVJA5UUZfnk4psY8Sy9lmmcJQstnPnQlH1OOdi-MB9DglTqc-tURQD10W39RhZiewvGP78RYjEvaXNcEqR_oNpsY2I7LRsgHOKc5Wx0zUlEtXDDf-Fj0K2hK24-e2RI5n469wmU5w4_CHOz5AxMt3i8B4EOQht-2qrfZjfNZ7ExXZuO5unZL7ypZ_xCkMYO1IAapG2hWdDm8mxiEAWUizqN2N1bhGpLAi2RgotPclcpe0m1kAOtAHoF03HpoK6B4Yd1QDJPU0bu6-F2JtxSG0nU-4_hSk9wyBgO9_QkTiIFeQQLFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5697d70b60.mp4?token=t94AcMf0QXUipUYokTr8B4B3zoHlp1hnAorjLQVJA5UUZfnk4psY8Sy9lmmcJQstnPnQlH1OOdi-MB9DglTqc-tURQD10W39RhZiewvGP78RYjEvaXNcEqR_oNpsY2I7LRsgHOKc5Wx0zUlEtXDDf-Fj0K2hK24-e2RI5n469wmU5w4_CHOz5AxMt3i8B4EOQht-2qrfZjfNZ7ExXZuO5unZL7ypZ_xCkMYO1IAapG2hWdDm8mxiEAWUizqN2N1bhGpLAi2RgotPclcpe0m1kAOtAHoF03HpoK6B4Yd1QDJPU0bu6-F2JtxSG0nU-4_hSk9wyBgO9_QkTiIFeQQLFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشگر: شما گفته بودید که قبل از انتخابات میان‌دوره‌ای به ایران حمله نخواهید کرد. آیا این حمله اخیر در عربستان سعودی این موضوع را تغییر داد؟
ترامپ: ما این موضوع را بررسی خواهیم کرد
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/25373" target="_blank">📅 20:51 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25372">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9cbf3c2b2.mp4?token=c0ltpZ0pj1t6V4xlAFcB58gOTGUf7xH9KQRr0-fZCrBb-ELkbI9zxQhL_kmVHeqLvcKLW17gaGzCrptmLx9eUCEa1_gV_rVpvicEZj-8jIqKJ7QuP4kTKfge3t7GU8U4nGbnyAadJBxLs0EYw95tFoTuRnHF-GCQqD64KvjTn4DdXrTtYHzGjcAPtlD_4Hm7XH7QRRhTWn9jdUIM38HfcIS2bvkM1_InMo9DUO8mXBYy4ti136TMu5ICWxVTFuFdYD_t-qMyGcbt9AjSekq2pkoFBG-QqbkFguTfqe8oVKRLtqp6FSKRKEz9ABXvNHCSXJZczuTJes2_BL_Dn7oaqZVGzLTpcXkj60pLuwQ_vgm4If8U7est35r-PGJ_0FDsUF284ILHWk3wplfxOH_skUhSzWYuVA4lI6j2GcW0uU3mBCxUXN2HqNOneYzxHUcQYkebOYmH9dzSIvjJvq1hUxbNwMYcOLdXkzR_AowNeI3oovDGE42HVqqi3eWYwNNMh5U_vTiScjVA2CX2D82oruN-JnGJde56RiyNZ0OalcZsA0sFUYiIa5hl2nbXFW5W5Cp8rAsW0M81PsM9y7JQfcVbikJzex1qfH7bsHDS7ogBWMERiyAcyFDNMqzN0oNFJfzcSAemfb1hoHk6fiOXKBG4Qubal-Kc5WYV8NcF1WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9cbf3c2b2.mp4?token=c0ltpZ0pj1t6V4xlAFcB58gOTGUf7xH9KQRr0-fZCrBb-ELkbI9zxQhL_kmVHeqLvcKLW17gaGzCrptmLx9eUCEa1_gV_rVpvicEZj-8jIqKJ7QuP4kTKfge3t7GU8U4nGbnyAadJBxLs0EYw95tFoTuRnHF-GCQqD64KvjTn4DdXrTtYHzGjcAPtlD_4Hm7XH7QRRhTWn9jdUIM38HfcIS2bvkM1_InMo9DUO8mXBYy4ti136TMu5ICWxVTFuFdYD_t-qMyGcbt9AjSekq2pkoFBG-QqbkFguTfqe8oVKRLtqp6FSKRKEz9ABXvNHCSXJZczuTJes2_BL_Dn7oaqZVGzLTpcXkj60pLuwQ_vgm4If8U7est35r-PGJ_0FDsUF284ILHWk3wplfxOH_skUhSzWYuVA4lI6j2GcW0uU3mBCxUXN2HqNOneYzxHUcQYkebOYmH9dzSIvjJvq1hUxbNwMYcOLdXkzR_AowNeI3oovDGE42HVqqi3eWYwNNMh5U_vTiScjVA2CX2D82oruN-JnGJde56RiyNZ0OalcZsA0sFUYiIa5hl2nbXFW5W5Cp8rAsW0M81PsM9y7JQfcVbikJzex1qfH7bsHDS7ogBWMERiyAcyFDNMqzN0oNFJfzcSAemfb1hoHk6fiOXKBG4Qubal-Kc5WYV8NcF1WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: من جلوی چین و تایوان را گرفتم، اما جایزه نوبل را به کسی دادند که هیچ‌کس تا به حال اسمش را هم نشنیده بود. فکر می‌کنم او به‌شدت ضداسرائیل است. با این حال، جایزه نوبل را به او دادند. به نظرم یک جای کار در نروژ می‌لنگد.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/25372" target="_blank">📅 20:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25371">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5bf39d5eb.mp4?token=WzT6Y5RHxjpkA1hcVLHO4l9COFxEcD4_XTGgWFdYKfiz-6fXho94qr7vZ4vmzOwIReufxz3MW_qOjjcAISsDQt74Y3rZ4DQTsJr4Mpx0mPtM6TQ-WPApuE_t921uUsTb_LrDzrfEn8TXxoo-SJZcafJMTMAr6kqCCt4l80vap7AnewZwFt6cR8rHVS620nMetjZknj6cRKZ0Jvg6Q47-WNgsUkmXiU6vQQVtfqx0l0d47sj8O-Bf3WhoNSIDW2SunSp38GoCh8tmC_atruLCBTzAbwaj-lbvDpI64GddGYW1bBjw0zpb8jbXAyLHXcSd_7ZhgquA0Ww24CVmRzaK0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5bf39d5eb.mp4?token=WzT6Y5RHxjpkA1hcVLHO4l9COFxEcD4_XTGgWFdYKfiz-6fXho94qr7vZ4vmzOwIReufxz3MW_qOjjcAISsDQt74Y3rZ4DQTsJr4Mpx0mPtM6TQ-WPApuE_t921uUsTb_LrDzrfEn8TXxoo-SJZcafJMTMAr6kqCCt4l80vap7AnewZwFt6cR8rHVS620nMetjZknj6cRKZ0Jvg6Q47-WNgsUkmXiU6vQQVtfqx0l0d47sj8O-Bf3WhoNSIDW2SunSp38GoCh8tmC_atruLCBTzAbwaj-lbvDpI64GddGYW1bBjw0zpb8jbXAyLHXcSd_7ZhgquA0Ww24CVmRzaK0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: متعهد هستید که نتیجه انتخابات میان‌دوره‌ای را، فارغ از اینکه کدام حزب پیروز شود، بپذیرید؟
ترامپ: البته که می‌پذیرم. اما نمی‌خواهیم تقلبی صورت بگیرد.
خبرنگار: پس اگر جمهوری‌خواهان شکست بخورند…
ترامپ: نمی‌خواهیم تقلبی صورت بگیرد. متوجه منظورم هستید؟
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/25371" target="_blank">📅 20:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25370">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ: در جریان حمله به فرودگاه ریاض قرار گرفتم و تصمیم خواهم گرفت؛ شاید به حملات عربستان به یمن بپیوندیم
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/25370" target="_blank">📅 20:23 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25369">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ: زلنسکی بارها می‌توانست جنگ اوکراین را پایان دهد، اما نخواست , زمان آن رسیده که اوکراین رئیس‌جمهور جدیدی داشته باشد
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/25369" target="_blank">📅 20:23 · 18 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
