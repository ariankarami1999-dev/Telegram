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
<img src="https://cdn4.telesco.pe/file/rseRqp8ULYMRQ0XxW9xjCcamxCZz1gT9EF1dXN51FWiw3jZuBxSn3KGtcC9vRnOsLHfjVAl3i4PJD-vFzpbfEeKINU0B1ZnLlyMuaJWHxwKG_iIIs3yii6SBsqlRA1_iynGnEll5OUoQB5WypdUlATV0GEorTYNHcB1GGMnnGltmySGM857Zjsm009v2EfNIzNE4NDL3qHv0HZxe99AhUUfytI-Ssl9GcxqjeLU8xSI4lNVjx64g8pgzMiHB7wnIXy_MrsNxROjnCjsh38pb66wczkSUsCGH-wuDNEI7BcIcksvVQArHgAsq2f0O9UlrBiOa3yl1RTw6C6SbtqxGZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.85M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 20:10:43</div>
<hr>

<div class="tg-post" id="msg-467121">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
پیام فرمانده معظّم کل قوا به‌ مناسبت هفته نیروی انتظامی تا دقایقی دیگر منتشر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 639 · <a href="https://t.me/farsna/467121" target="_blank">📅 20:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467119">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXE9EXgZH0aWL6AvbYf2O3QnL5RDqremx8W2A5nrZN9eZ1KuSEjwvOfh2bsLRiUf0k7QtXwKHSBDu2w7pLB7jqk31q1t5qD3eShmApOr76-IPZN87HKbUXVOAh2KGTVc06hu9WH7w1WYwTZiZlSWAvNnApDlV2YgHm6SMht_9oDqFAodWsp9y4jjLrJm2oIgibqg7dnCY7QTILipTq0153IB7n82DU2W_5uq0iPiWVK2XcKXryEjK6MJzyC24Cma_YyDaZBrlJ2m3BOlCCEsT6dzNKkiAgnuCV9DAesN0T8ry5vr9PrSxarohVNfsZixF9ychzD6askmezrjJ8xICA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ترامپ: همه باید به‌جای «هوش مصنوعی» بگویند «هوش برتر»
🔹
از این به بعد، در همه اسناد آمریکا و امیدوارم در اسناد سراسر جهان، به‌جای واژه «هوش مصنوعی» (AI) از واژه بسیار دقیق‌تر «هوش برتر» (SI) استفاده خواهد شد. ببینیم این اصطلاح جا می‌افتد یا نه؛ خیلی بهتر…</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/farsna/467119" target="_blank">📅 20:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467118">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سلطان شکنجۀ ایران
🔹
داستان پرویز ثابتی از آنجا شروع شد که دنبال کار می‌گشت و افکار ناجوری هم داشت. سال ۱۳۳۵ که ساواک تأسیس شد و او از عده‌ای از اطرافیانش درباره یک سری کارهای مخفی شنید و ۲ سال بعد فهمید که دلش می‌خواهد ساواکی شود تا بتواند کارهای متفاوت انجام…</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/farsna/467118" target="_blank">📅 19:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467117">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">قطعی برق برخی مناطق تهران درپی وزش باد شدید
🔹
درپی وزش باد شدید و وقوع طوفان در شهر تهران، برق برخی مناطق پایتخت قطع شد.
🔹
عملیات رفع خاموشی در مناطق آسیب‌دیده درحال انجام است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/farsna/467117" target="_blank">📅 19:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467116">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6L5AvSiEp9Lg8rOtnWvVEP7YPyQ-MsNXVf7QBDQrtPg4MAltZfCcOwfCuvh1vsfuL6LRVezSxBTBMjUyRGVFX7KjHaRp1CgGeRhl-ptIMi0Xc_0qtztXXbSSrkKN7NwF5yFjCZZ4IDnNIB82XEoPDq135jY5AjGqXcStKPhfsq5iUNOkRlE7cXxnNeWOvSPd-ZzU7hZSrZ3-gHbWSOrS5qkHTAPXvvn0vquBnRRa4fBNSpVU3W_N6GKdqd3EuH4mbfdgL13yfmRdW3mq-ZzU8zb8vfY2c3hhiQ-Lh6GPAw6Kw7oyTJsrYzHIphiUD8t_t_VFhYNic8ADcJqWpJdig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یحیی سریع: به فرودگاه‌های عربستان حمله کردیم
🔹
سرتیپ یحیی سریع، سخنگوی نیروهای مسلح یمن اعلام کرد شامگاه امروز پنجشنبه فرودگاه ملک خالد در ریاض با دو موشک کروز و فرودگاه نجران و پایگاه هوایی خمیس مشیط هم با موشک‌های بالستیک مورد اصابت دقیق و مستقیم قرار گرفت.
🔸
سرتیپ سریع تصریح کرد که در نتیجه این حملات موشکی، پروازها در دو فرودگاه مذکور متوقف شد و خسارت‌هایی به پایگاه خمیس مشیط وارد آمد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/farsna/467116" target="_blank">📅 19:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467113">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gmrlQt5xHQ-G3qN7bwAlhd36Y1YGTIv6b93YO3fFSrnE27F-x7KFJOmMkL941XUptVyQQLkfrIQMz8T9xQPVlJhQyWrZZfDEuk81DFf2YaP44Q2TmAF6zGu-ShiC1rv8E7PImrZ5ZOI0nhFoSlLiCBSkL-u3iWxNLcEoTRA_0ryN-pz3CaZllViOO3JNAWdwKKHIsUwC_e_UPFCD23lljaKCPMiZ1uJUi_bC7NyqhCxtiKVtNdY5Y2f5r13IOuRDSbQ7r0K0D0I4rT3-QyqyyVLaMS2mJaGAZG9VeKTwzUQNQN_zbq11AouLvf0LeKAW7RKBJKJWkHpdzeu5AUoPRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CXoXm6nTnfNvlIwbkD-g6Zkyyn8s4mHl8ZKpFW48Xgt8gNFXZSSUHYusmDUOUaQ9XBud5jayZT8ZFAQSdiIH5cf7nWnwkln2TZvDsjRZZPN2YbwjiRHM4Dw8z78M6MTY7Ckune4osvYdXwMx5eH1fVDmm_hrxxjjcIrNjySIasdiP3poC3JLCXGl6v_322YEUEk1t9fpcTytAylwYl2GMWqj5k4OjXwAuEdRcK7wTNrA5Nsg0Uo8Fr477B3efN7f89o9eH7WqA5hAXFm-viIx9dIbaihtfGxuxVUpqC0JjcjeqMbETtyPvqruXJbqqnCnQ5aDrPBhc0Fr2qck4ojTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IW8km67MTBwM9yHz9ObXQUz3tY9N7VlSgeZmRhrIab4g8a8LVcMzchRa8dI_6Z0L2rJ8MedBW-_8JEMV3dLByrjAITHbMk5uGAHem5X-rw5OKtRQplP-rpwQr9EpEFUA1rHRxuGQIy0_jary8n47fZh-OiNynUJikrZmTWxSJkU-bProAjk68noEkkEhdiWOeKSuXKjDVRQ1nSxIz-Hfy_pIC-hLGNkQ3S4K2QC_H45qeS9vcJlZz4h4DLV-yqxYQOT2QcGjemKDT-Hin6QIB8q-J9XVcQnVVY22jhetcwc4FTxMRHZ8Pdj38ZIqlclXvqkNkunryaW55f5WVPFsXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
پزشکیان: در سفر به ترکمنستان با سران کشورها دربارهٔ مسئلهٔ خزر که با خطر مواجه است، گفت‌وگو خواهیم کرد.
🔹
‌رئیس‌جمهور پیش‌از سفر به ترکمنستان: خزر سرمایه‌ای برای نسل‌های آینده و محیط زیست ماست که اگر از بین برود، مشکلات بسیار زیادی برای همه کشورهایی که در…</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/farsna/467113" target="_blank">📅 19:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467112">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
فرمانده‌کل سپاه:  تنگه هرمز، خط قرمز راهبردی ایران است
🔹
هیچ قدرت فرامنطقه‌ای حق تهدید، حضور سلطه‌گرانه و دخالت در تنگه هرمز و خلیج فارس را ندارد. @Farsna</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/farsna/467112" target="_blank">📅 19:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467111">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJy3SnkqIjF_DVILuB6qbHchlnwhJpUwxqq0H4frh5FG8ZIkHX5hUkEP3BhfA7z1ODzme2WroXE1Kvb-mqgbHuCaSal-BNOY_NebvSmD7-YrXrwgq0F10tZNEy3hF9C5Oiyap9w4k-wZyhZtyRfBv1BXDssqQ5VT3dYAn_RiOiHZLzwXMWohdIKLmvPX-3pqeeocJIwOCc-un4fnFSA87GjBOurVRWnG8agee8O5AdNAnYj6nUIGrAyIt2SzO83dNjH9Tr_eyFvldNjHzo-vEoFiEEi7nG9s-JBMqBYuc7Rf74ZCu-vFfVdkpFppU3dlgWVE7TU1bOh3yaW4XOJgRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فرمانده‌کل سپاه:  تنگه هرمز، خط قرمز راهبردی ایران است
🔹
هیچ قدرت فرامنطقه‌ای حق تهدید، حضور سلطه‌گرانه و دخالت در تنگه هرمز و خلیج فارس را ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/farsna/467111" target="_blank">📅 19:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467108">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7262159e9.mp4?token=tzdKgOd4ammatsgrQ1y8GDQw16g_4LmVXi7X4MRorF07GzxjxbVT-ZRwVTesGgisBYUiypKp3tpwccUxXI2KL4lvIbGiy-zKIRCSHlqhFg5fYgzjmCC2aN6OpqVmnQkyywABkZmFTuCn1ttVQjH-63OTN9qC5bcEdStNFF4yqYI9EWOFcE3YwX8H2TyRj_ZB8uOAv0S5_KFMixBxmmwnpeYYzkSfaR4GO6CVxGXhsyB6H3i3QTwz7nQVcNRdATUgxMSzTzJm9T_IUnS89m9iGYN7p_HkchkQayZHvlll3qW6GuN3Fd9-igxzBGyl9krPbicy7Nj5RhDoYqq4VWFNTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7262159e9.mp4?token=tzdKgOd4ammatsgrQ1y8GDQw16g_4LmVXi7X4MRorF07GzxjxbVT-ZRwVTesGgisBYUiypKp3tpwccUxXI2KL4lvIbGiy-zKIRCSHlqhFg5fYgzjmCC2aN6OpqVmnQkyywABkZmFTuCn1ttVQjH-63OTN9qC5bcEdStNFF4yqYI9EWOFcE3YwX8H2TyRj_ZB8uOAv0S5_KFMixBxmmwnpeYYzkSfaR4GO6CVxGXhsyB6H3i3QTwz7nQVcNRdATUgxMSzTzJm9T_IUnS89m9iGYN7p_HkchkQayZHvlll3qW6GuN3Fd9-igxzBGyl9krPbicy7Nj5RhDoYqq4VWFNTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درگیری شدید بین شهرک‌نشینان صهیونیست و نیروهای امنیتی اسرائیل در قدس اشغالی
@Farsna</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/farsna/467108" target="_blank">📅 19:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467107">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/805fc7f33c.mp4?token=Mk8wdZ8_A8HN42DgQevWCHycVVSt4IiGm2tlM_rHez6mO7-oh3d7KYdfNQboubZjshs7danIZMvmEJRoN4y3o-yYf_Ad91h6uxImDavyv0uZkna_tSEF4s5UKsrOoZiCXa9FI71JvvInk7no6_Dnj1MqJ0ou5kltWF7djjXLc3dgbVCc6vxOdXblh1TFNu7jx9ZE1CgQBME3ywBRv5XMjPK3JPjWDbFm5KgbCt8hwnHsnVyLe6CGgVtB7pEXKUaKLwm_57Al-5xFqHqFGZxIopjwoKAk-m-ifSZn2MOORkd8lF0UfIgYqlyQQNsJAhTamtUUTPMiRcKBBy3Ke-fLzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/805fc7f33c.mp4?token=Mk8wdZ8_A8HN42DgQevWCHycVVSt4IiGm2tlM_rHez6mO7-oh3d7KYdfNQboubZjshs7danIZMvmEJRoN4y3o-yYf_Ad91h6uxImDavyv0uZkna_tSEF4s5UKsrOoZiCXa9FI71JvvInk7no6_Dnj1MqJ0ou5kltWF7djjXLc3dgbVCc6vxOdXblh1TFNu7jx9ZE1CgQBME3ywBRv5XMjPK3JPjWDbFm5KgbCt8hwnHsnVyLe6CGgVtB7pEXKUaKLwm_57Al-5xFqHqFGZxIopjwoKAk-m-ifSZn2MOORkd8lF0UfIgYqlyQQNsJAhTamtUUTPMiRcKBBy3Ke-fLzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ستون  دود در فرودگاه ملک‌خالد عربستان پس‌از حملات یمنی‌ها
@Farsna</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/farsna/467107" target="_blank">📅 19:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467106">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrzpXv17wcJHvsoMymkv9IRCnTe7IO5oq9IqD5RrG__jCroBk0uTdocZdiFp0E1Nm6MgUleRvSRXKobqeoeeeYZsRvqQetfv5Bek0igxbrqTm2heNCBYmA98KZk2UsRYCJgocvpyn3k7e6Fb97425xxQCB-V8j0xDSA2KZPXe0PmwaWEAkill721iG9-SpzjXwWfXFzQz2miFs36Q-nDWzYEp9jNgB_SoUgZ7r8hDfwufT_l6-fH1LHgCufScAhzFLAUO2Kun4EBrbEFMd5EG_GON2JQJ2BiV_8uqnr4RvO0PZET07h8J7v9Gz44p03ugUeFz17aa0UieGy5yJo7kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
گل مساوی تراکتوربه استقلال توسط حسینی
⚽️
تراکتور ۱ - ۱ استقلال @Farsna</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/farsna/467106" target="_blank">📅 18:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467105">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b616c846f9.mp4?token=MuEIc_CgIrHaQTEjObAcHz8Fau35oB611SW-eWSKnUpJjHv0kFXS9VkbgkkwzTzW_H1-QU_0-aSQY1DZ-NRKyZtWU_teKbNAWRWcti0lnL7OUf86_rA_WgN_hiLXJ2AxlK1fVxvzlNu0k4Q0xukrNcgwnACgKlkl9QZD5NabyWsFKKcPUcrcXvRazn_XxKWBSEex6QSkMyYZJ_27_LE3RKcU9tQoc5Iq8xjAeS0U42bkzqnUu8mOelw8TvtxmoKoiLQfVysymVODoyizyCCAUt2hYzJvv0mhxbARO840ofUvc4k1q1B2wW6ibcjmhn7LaUNlkaANimzskEuqAt31LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b616c846f9.mp4?token=MuEIc_CgIrHaQTEjObAcHz8Fau35oB611SW-eWSKnUpJjHv0kFXS9VkbgkkwzTzW_H1-QU_0-aSQY1DZ-NRKyZtWU_teKbNAWRWcti0lnL7OUf86_rA_WgN_hiLXJ2AxlK1fVxvzlNu0k4Q0xukrNcgwnACgKlkl9QZD5NabyWsFKKcPUcrcXvRazn_XxKWBSEex6QSkMyYZJ_27_LE3RKcU9tQoc5Iq8xjAeS0U42bkzqnUu8mOelw8TvtxmoKoiLQfVysymVODoyizyCCAUt2hYzJvv0mhxbARO840ofUvc4k1q1B2wW6ibcjmhn7LaUNlkaANimzskEuqAt31LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل تراکتور به استقلال که توسط داور مردود اعلام شد  @Farsna</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/farsna/467105" target="_blank">📅 18:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467104">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d32a4cdc.mp4?token=fzA2Z6IbXNZL-Y8w4GC7a720J3quApNiyd67FVWpiyHyYd0SKTaWqzlqcbxOzh-lauGhZFUwY4QtPaEPzxzKkjD3o-YyFyXHjJYxCfOvPEXoa8akGiRKF9WZ1crwqUv66GW0Tnhr-Uu0YoRjwReh5McryQ-DHzJYy-HbJxnfvTiYBqMcLqWKEQfQwwpaHh4tstyLugFY-a9xrHn-7q94LNnfSbYoWMdvIrsTiu8on3GOLe52pd4NlaGDjb7rCaZj3sWhd4dFA8WnkcGD7XYoI_9NatdgiUIwqXpKOh5ShLCcGbFhyOCL41ycVs49cbI-GsD9uBMJMXNleCVDlgDPEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d32a4cdc.mp4?token=fzA2Z6IbXNZL-Y8w4GC7a720J3quApNiyd67FVWpiyHyYd0SKTaWqzlqcbxOzh-lauGhZFUwY4QtPaEPzxzKkjD3o-YyFyXHjJYxCfOvPEXoa8akGiRKF9WZ1crwqUv66GW0Tnhr-Uu0YoRjwReh5McryQ-DHzJYy-HbJxnfvTiYBqMcLqWKEQfQwwpaHh4tstyLugFY-a9xrHn-7q94LNnfSbYoWMdvIrsTiu8on3GOLe52pd4NlaGDjb7rCaZj3sWhd4dFA8WnkcGD7XYoI_9NatdgiUIwqXpKOh5ShLCcGbFhyOCL41ycVs49cbI-GsD9uBMJMXNleCVDlgDPEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول استقلال به تراکتور توسط سحرخیزان در دقیقۀ ۲۸
⚽️
تراکتور ۰ - ۱ استقلال @Farsna</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/467104" target="_blank">📅 18:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467096">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZzFco-7KP4VNkXQ0vlT7yIiZC0Lj8wfbtzAVldq2rE6Xl-aM-8P46FCNyWu4XoP6htvxtsupiuYL5UEG4UlCkyt2-Zt6uW2fzCxFtN7Lq3dVK8KXuKoQGIASlt5Hr8i0iwgifQXEGD_EemB5dFn__P4epQ3wfwz-hX2pFN0wvnhPFOy5819LYsPC1cN1v8jkYC1vK6vhqB55uVx60xQI_JAMb08oQj5sBp98-pT_ZABz_eTX5ugwOAAAcGK1MKRxHYIrbG_S41w-8cfNA0TwZ0lbbFfg7sK2RVfqCQ3dxjz3oIcZrFJQb32BUzjUoqHcneqOGYhiv2K6iLW_ughdaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PrGd-ZlOaU0cc9UnbL7UtosGpeP1-6dicaKjxXW2mP1IXw2AhbwDItpXZCZR5WBfOqoCQ5PvFtBY7qWMMuP4tWKlVjXTcHbtSEgoa8K-hBQs4N9BslovkpsQfNhizBG3FDSVT7NQcs7fP5hc9CUYX-SOb-c23wA3ceHAMh5uE7ntP_S3MPIqJsh8yDzChQOFii2mlMzvTVi1F9Vi07XmQU4gy5e7mzlyRailZNlyrvypa5vYrTS8AfWN2GZlj0PC_EnQdkuHtq_B3R5PKJo5fllPK4dokQqYEPJdrIcez2BZeheLQOJZibb4iEPG0L96HOm-v9fvrNY87wrAUSIWOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LyxZzsWRWoARs0JOTmj-unUueiUNZ-twyUV2BRG9IHvFeHqE7r0nVc-r-Mk3aq6Hrzbj6NIN8J84WffOscdLpfGeba_ekF4ESU9-kBb6zK8VwQdPdU_70ZPzDd6PCtwT15M0Occ2D9sWeYilsleQio14qnvKKc1uf1jO2GJAc_F8n1RaI9KbGpSQ7FMwtfcu6rpp5Wm8gZQ7X7QCublmNh8wz6AAZ1QxWw0o_s1c0pThTDmivz1N1BDsDwdWs95DEIwpWuDVnAXttABLaC7GmKdMAGwa4Lw3_p9H0zSjU0Nq9jriUsZXGnKzytcoeh_hOJMWE-jp3b-rdhYDFuqrsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bWWpjMpwn6QCf3BmDkJpu_jM5qMIOz2LccyG9ThNVaTtsESJ6X8hYIl41MI9r26TWwHQrZ6XDfRw-YNEfKqUjRkGDx1F89br4JrGR1u3zQ3NvEgDEYqvvM3_mlneBSyLxVUrztARnrr_w8gNNsvy-qRq1SIfKtnVO5U-c9yVqismLk3V-SR_EgThL600W5LhQff8hy7TX2Izs6X0F1MKV4k03GY0q4BERAOeAHpGGsNEN1clqTM3BAuD_4JXCUuJrOaIjqj3E25zVh7UH4WLLbkURcZufXK5T0TUUz92_ggOiLMWdAeH-XRl3J4ilX0Zq93Yz0hWGxUu578Ku8ULOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I6cvihBQIsVug1F7iCPo4cFxDfBn4NPQwVTwvkwCpdFU_tSAUvpSjq8cp4kyQjtC6UaHJjAMtPgjoZfcWqB25CfD4x_sBQN-Y_6SPwCPRUsLAoYT5vkyHUQZEkTf27jRSvKoCLgJRxlkYiKpb-TK2wQtWxfF0yjVGNfnIvJQ6Np6ztGVCjkx_4QKKG4_3z1EXihMARQhpiLtWb2SSRnlswmKK3GzEg98EPnXUwxBm2rMg9yuxheRBzDg_ITavW2Cl2iM2qVFfVq1FVY3XKUnuhJZJLblp3jhmCsA87DzpRrzK_5FcSjqINao6cUMAkP29uRdECcdu1iCjbU0pGqA9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vtJY_KzA3kt2UNx7g9y4Fpf_nzYpSiggVGUeRHWdAGTtIkbetvF4rr6Hp80TFYCvXjQyXZcvj4ED7sTyafUFxtOvLWW97WyF1dRUnOl6OKZ8rFWe_FEszwNO4aQGyiW-O7U9k4SIHr_EABgl-Ldyv0yOKXdyRsjpnbdp52hm-0C95k1dJKUioV2pgqRqPBPauqjGw60oKFqjd91lHAI_qWmlFjkwfo9XU594xleSBOp8sS_ZtILZn7LAAUTfTbFRSyYn3vMAjAb34w0w9Y6AAXi2g3kLcDyFBg8q-U-wFPq6bttn0Rt4GvnQtsRgE_YAduvc1HNuRTKrwjNKTJ4dFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rk0EXEXoy_WdM1IArJ-1f4cX_TTDC1N0gitkEa04dNM4jVtDjOABvdKKYDL5kllg2dgUEYSyYK_s_lDlp3Xgz98ywSUGDu8noUrwkMDBdi6mu1_mzIHFr4ECU0pKrGxOC_Tai8qm3BIXxavzTtTr_G3dPYiwpwL_44xhT9GHxn7TnL3nr50YWaWL3_5f1cDZ3uTkhEkpWRRf-3A0_ftvFUuFT0ROfDo_VWRSDFjQ2Hk1UbDPAlfdu59nA4smE01jr7EUkhHgap5n84vwVjKpgAuvHCcL7VU7c-jazCznc-xUj0i0h9vx4phkIn9uiBZ6FFFbhDmH3s45afv4bnafvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eBDNpqxQyH3R4o22fuk7WzjCqi-VLxbXwgPtOug7zaSwLNmY-iXQepIpfJoxOgfkireW_oq1H2SpLO013wSf7wmRHQCZXiFU4q6u4rI_F_RxiUx-kzgTg7HeGfYBDGh9_toOno34BL-gPPAUw2fLF_yCGJSTXSagxsMZLvyzHNXTPF6G7tSJZACW88fNu-xzrtJeR8lfa7ej-CDg-ohxRoUPl0HfyMPsjz-SzKZ4rh-oA62bQYWgiT1kuiu7ifSnHQvIAZzktN89Xm4imvg7n9azl1gKqge4Brk7_pvE6LJ0wI38sIysO__h-XQ7R-ESmsbcGejCONfmjfrZml5B6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رزمایش جان‌فدایان وطن در گلستان
عکس:
علی دهقان
@Farsna</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/467096" target="_blank">📅 18:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467095">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwa7rPSzPUNdJzu3LRjKj4rUSgJQOAuKF8hE41f4a7zhiNZIn746kAxMv8U7L_vyI7GU_u2ar9YG9HODF1k93F7tahDqc3LmnKeuahUVQ9nZEZNESMnDCi9wKOEjBuaFB2l4qrUpABBudyks3EGyAw2sguwwPxWgutShJATCN3roVASAXCIv89DKvJV-JjhmPbGe7jdVFKojkQ0bU691u-skQPR8JwXHRZgPC39nKjCvx5tjQvr2i3gQWxu5SGw1x51ybu9r5IAykHH5liiyXUv7hXS3daMFIHzgWJwKQNFRb6lxncn0K3dZ0KO4QDZ5Z75YAI05l6_ENVS1diuA3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهلت انتخاب رشتۀ کنکور تا پایان روز یکشنبه ۱۹ مهر تمدید شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/farsna/467095" target="_blank">📅 17:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467094">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqngpXb23eNA5Aa87dg8qJjz8AZGJtJS6aXuHw92IXAL3gzzKoJjZND6vityftRpCkzM369T1w3xQAwxkv7AKmtQixkE1W-3544F4FoPqlzmdzU62X4lzFn7fl2qymKkB_V5U4ofDIS9qtntNldl86tq6ZP4xX4lryzm38xn6jAJQkl9oVSwNa4F5ttj99zUozEw5Ro1TTyFr4fYLYX4uPmDzx9P_NcomPZNVRje7l_Wd8D8V58_dyD7hspf3whZ2n5lKqiwEaVb_IpD45JbLSn7n56atLzgM0usYPDrOzAKiwfKy2EQWREXXM5zbCyCneEo5kyQAmCopblPfcJ9uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از شهید همدانی و شهید سلیمانی در کنار رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/467094" target="_blank">📅 17:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467093">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chZpo-BoXY1F36NqjvdGauJEPy5SzcJOdpzOiyU65IJAIQ8VMPr205CLJaGL1ImsJ02nbJq3Xw-3wkArUwV8K0_WiW6am3MXlwUifG9hC-CH7Pdk9KNNyG5c7QKkgLD11xXPwSLgOqlT-ucKLrM4UowoJjvvSumRckw3YcuNhdmHEk1zMVNMUhwXZuERbHTGrQ1iPufBQl0Nd5nOq67G7vm1qRk644eVFcrZ4KQDXUwlW7YeGInqKwWKJOrQehcMdhzr1ozmR2eWwaXXqjXqFdOxdknGV232jJs8uebCdBPqnxpGm-fCXbYyGYq6aYtE48Zfj_IEPgsavRvCzqipLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
رهبر انصارالله: از هر کشور و نظام انتظار می‌رود که برای حمایت از مردم فلسطین در این مسئله‌ای که هیچ ابهامی در آن برای همه ملت‌های جهان وجود ندارد، وارد عمل شود. @Farsna</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/farsna/467093" target="_blank">📅 17:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467092">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f297caae75.mp4?token=uJL9pUuW8cDsbDGKO7TTkgz3tiNTmYnesTS7_y6FbeA0LoVRObPQ2c09diaoffp8K9bP14Yd2MPkXY1DtMm6lgAOBVA-tWemmihDCmAt7A_BaRPEPZoSiv_ulMhU9_yTcmfSgIpfZY6us5CaFTh-mobNkHCjcSYSyfbbUJAXy7ZNIvSEfIPbxOUjva4m-OPvDT5y2XzcToxA6HBvTEBxRJg7FTecD2L1Fvu2qqtBVlbawV770YkhGYBNIaWaE5brYy4hpAhm04cCk3R9OxrolaVQxkt1ZV-Pk2Zsx3bdkvOQzTowA-7DTDNJk58L1Zgj4BFLkEzKLvgbErt_VUPLUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f297caae75.mp4?token=uJL9pUuW8cDsbDGKO7TTkgz3tiNTmYnesTS7_y6FbeA0LoVRObPQ2c09diaoffp8K9bP14Yd2MPkXY1DtMm6lgAOBVA-tWemmihDCmAt7A_BaRPEPZoSiv_ulMhU9_yTcmfSgIpfZY6us5CaFTh-mobNkHCjcSYSyfbbUJAXy7ZNIvSEfIPbxOUjva4m-OPvDT5y2XzcToxA6HBvTEBxRJg7FTecD2L1Fvu2qqtBVlbawV770YkhGYBNIaWaE5brYy4hpAhm04cCk3R9OxrolaVQxkt1ZV-Pk2Zsx3bdkvOQzTowA-7DTDNJk58L1Zgj4BFLkEzKLvgbErt_VUPLUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول استقلال به تراکتور توسط سحرخیزان در دقیقۀ ۲۸
⚽️
تراکتور ۰ - ۱ استقلال
@Farsna</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/467092" target="_blank">📅 17:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467091">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyyDW0ZdKf9fXgCToTllFPTu1v_2SyOqoZnMoqSQr15hZETkwCX4T1b2pKta539IHx4Q8KsPQxFv_9wHarcBgPz3BGhOcq7iYNRuoYz5XhQhMQpg8DVxXyoY1SYndhY1JVP4_KAiTnEHWX10EexVP_D89MYUVFPbTGOrKsWoqL6JEkX0L38JUfk3NY7_b8E1AsS-5CfskG3eRcPrqEL__xGskGJ5APd40eyTqg4FiAfRh-PtI1UHb1Ee-jwt3HGBjPxZWxp_rktmV4ySUxQlM-fdx7Cw06ul1wLu6maIHigTdoueR4JYPhzPsjYImeiIsCb1TzEG7acyE2V6f9YQcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ادعای نیویورک‌تایمز درباره مشارکت جنگنده‌های پاکستانی در حملات به یمن
🔹
یک مقام ارشد نظامی پاکستان که نخواست نامش فاش شود، به روزنامه نیویورک‌تایمز گفت که از جنگنده‌های نیروی هوایی پاکستان در حملات به یمن استفاده شده است. @Farsna</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/467091" target="_blank">📅 17:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467090">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: هر کسی که از متجاوز سعودی حمایت کند یا خود را در صحنه اسلامی با او درگیر کند، خود را در هر معنای کلمه، در گناه، تجاوز و جنایت درگیر می‌کند و این امر پیامدهایی در ترازوی عدالت الهی خواهد داشت. @Farsna</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/467090" target="_blank">📅 17:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467089">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: مردم ما هر روز بیشتر به مظلومیت و عدالتخواهی پرونده‌شان اطمینان پیدا می‌کنند و با عزمی راسخ‌تر در برابر رژیمی که کودکان و زنان را به قتل می‌رساند، مقاومت می‌کنند. @Farsna</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/farsna/467089" target="_blank">📅 17:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467088">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: یکی از اهداف متجاوز سعودی با جنایاتش، شکستن اراده مردم ما و مجبور کردن آن‌ها به تسلیم است، اما این یک توهم است. @Farsna</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/farsna/467088" target="_blank">📅 17:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467087">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: کسی که به طور مداوم کودکان و زنان را به قتل می‌رساند، چگونه می‌تواند تحت عنوان "حفاظت از مقدسات" عمل کند؟ @Farsna</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/467087" target="_blank">📅 17:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467086">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: برخی تصور می‌کنند که با حمایت آمریکا، می‌توانند از جنایات خود محافظت کنند، اما این افراد خداوند را فراموش کرده‌اند. این همان چیزی است که توسط متجاوز سعودی انجام می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/467086" target="_blank">📅 17:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467085">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: نظام سعودی، نه سنت محمدی را و نه مکتب سنت را نمایندگی نمی‌کند، بلکه رویکرد صهیونیستی را نمایندگی می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/farsna/467085" target="_blank">📅 17:17 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467084">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: دشمن سعودی با جنایات خود، به وضوح در برابر تمام ملت‌های جهان، با ماهیت جنایتکارانه‌اش که به آن شناخته می‌شود، آشکار شده است. @Farsna</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/farsna/467084" target="_blank">📅 17:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467083">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: دشمن سعودی، شهروندان را در خانه‌هایشان و در بازارها، مانند آنچه در منطقه "ماویه" رخ داد، هدف قرار می‌دهد، و رسانه‌های دشمن درباره "تجمعات حوثی" صحبت می‌کنند. @Farsna</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/farsna/467083" target="_blank">📅 17:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467082">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: نیروهای نظامی که دشمن سعودی آموزش می‌دهد، باید با اسرای به روشی وحشیانه برخورد نکنند؛ این رفتار هیچ ارتباطی با آموزه‌ها و ارزش‌های اسلام و همچنین با فرهنگ و اخلاق مردم یمن ندارد. @Farsna</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/farsna/467082" target="_blank">📅 17:13 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467081">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: دشمن سعودی برای دستیابی به اهداف خود، به آمریکایی‌ها و انگلیسی‌ها تکیه می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/farsna/467081" target="_blank">📅 17:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467080">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: دشمن سعودی، از زمانی که به تشدید تنش‌ها بازگشته، به همان روش قبلی در هدف قرار دادن دانشجویان، کودکان و زنان روی آورده است. @Farsna</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/farsna/467080" target="_blank">📅 17:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467079">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: جنایات متعددی توسظ عربستان رخ داده است و از جمله برجسته‌ترین آن‌ها، بمب‌گذاری عطان است که در آن از بمبی استفاده شد که به طور بین‌المللی ممنوع است، و میزان تخریبی که به خانه‌های مردم وارد کرد، بسیار زیاد بود. @Farsna</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/farsna/467079" target="_blank">📅 17:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467078">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
رهبر انصارالله: شمشیر داخل پرچم عربستان هرگز در برابر دشمنان امت به میدان نرفته است
🔹
رژیم سعودی خود را به عنوان حامل پرچم اسلام معرفی می‌کند و کلمه "توحید" را در پرچم ملی خود قرار داده است، و شمشیری را که فقط در برابر ملت ما به کار گرفته شده است.
🔹
چه زمانی…</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/467078" target="_blank">📅 17:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467077">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
رهبر انصارالله: شمشیر داخل پرچم عربستان هرگز در برابر دشمنان امت به میدان نرفته است
🔹
رژیم سعودی خود را به عنوان حامل پرچم اسلام معرفی می‌کند و کلمه "توحید" را در پرچم ملی خود قرار داده است، و شمشیری را که فقط در برابر ملت ما به کار گرفته شده است.
🔹
چه زمانی رژیم سعودی یک بار هم در مقابل آمریکا و اسرائیل موضع نظامی اتخاذ کرده است؟
@Farsna</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/467077" target="_blank">📅 17:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467071">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j8nmSujnith8h8wSyE5qfN8B6QrmzjtoFiWrmlaxtzXG4eccK7peLPXckF220hI2FVB8VEQWeuyXg868Z-5Fm0shGU0qcCjfqer0CQrXeH0rsiW7i1Q05g_qwqfBZmqiBYGRFeXqZqRt7v3WERh5GXCQuHodlcimSURildmlPvq0rNiLHeNjFgORmjZr4gRxzOd2nUlxcHFq3TGPyLM-TLpYvOequNlkfw6Zm3mxwxAggXUn2TE7VVNhftmONE4reGJaEWStmLUGpIuh3FhnwCMfSOr5_CVN4CrqBjaYGEOlDF0AcFH0pzTl0HVG76TlkTkVm24Jmp3RGz1jQw7BbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EKY34uW6xiMIyIBq71ITvOSG2vvU5CXjFUkx3hI8gQBbv8ibXTe9oCVN6FJJw1WzOLZ3WclAXFaAnqpsNkmXE3dAzN_0J_nPkzV2i7IuTPd4RF-EvqoP07R6zAEfk_TRFj6-5jRYZyPByQ9y35Ix0qxbZ4iGrjBP_6wk2MVNS7_2iVOAgaNPhsCcxJvf-Z_hmt7CzaNdAId9M4y9oMq_jnzKj-rXLkMhCF_bWPcrE4qVZenHn2cszaUJzUEqb5UDmXRx9VtctzdnbgTw4UcrL2swl_yxrYMAy4-JFlJGeOHfXD9QwiNtzwyYv2ZlNTOLjtr9F0i_qj0AWymkeOcZ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ifgGKB5AHU47m16LlYKR-ziKWRWvxOJvYv-9MO9XOCNtGwK2OsRAyX1-MsURmYsrIcoAntMA6A43KU9heig_owsbcaowofKhf2h6iSs4pXiLD0ne0JmCbq9HWI3MkJK1-zp0c7mrqKjY2REVGP5XmskVZ1ZOrKC2iqEO6wjHAesTt4jG9PLAT_5YFs5SX45w3fr1tTnKB3GHMfCi9wwpcNj1IFr1SjRkwCfZoswMkcIbkNinEDSEHfckezY269lFuiNbCLCbsBdhvPxoJELQQ_Mbb7GSvpPpyn_5jP4SGg7iGhDmiXWALjdxrOa7ryvupSJUP9v1a78ELk4fwOoMdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lCfmlxhzfDYTa4OUr1Q-Q5SDhMw16zrnb6RgCHo-6s3lAxPtsA6MaRUQe7ZdXmsvbu_mnrkVWDk7Pbb_B0w7Ih9qIQWXW7BDwmcTwqXlYqA4RWafoSYZaaxrfqGCDT6H8wG8-t_YWpLZeoEThSrH0gFqA0BIn1uIpyWFPsbf7KCckr3IPJqU4kOSk1DMndeN1aP0gtUfdqI6p96c7gzw4xy63WtkViCygW5TreFTeeTdtjJwguhwy1Qix6P-a_6wfh5FC3RhUk-0tFhTuqNGwOBeSkhEtEslb3js9xNT1vlm-DF7DohZ-8cxhT9efWwlHDWeEc-yrZw9lq6QA58rvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wBDcb1Ek65Hcn7gmlG-myYPmnOEY5hjdy8r-UPBKoqacCEn9iA1li-hhW3Goi6rMafiH3zzhMrdZLy1cnHbDxdraZ1ufA3pbW_oIF3sCToTnoFhXEQOxOhf_RyMlEl1fVXet1E01D9ijIB5-AYwv-gjA6AUEexrcNL09L1mHVZLCttPs4EL1JBsmMBUIB-8PIXS0qITOuoSZ_bVYXHjsq7znn1hxSpXKuXkwSOaFl-hBXtrLRwPDfSWYdr5ZD3dkGYoC_OdbPds7z0ARQCku4cza-xkgmzs6Y-Nux5MEVrI_Sj9bf4OVV4Sf_L4We5zbh5A5_HrAt84u01bE-gmbQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rRxNLkzSfOErLs_OcNcHNn1VDZgoLWkXiHyyE7FDfYrBOB2REPN5UA6ie6IkSUtVQMYhpRJgls2dbxl9BvCWY4lNtGNIatzMWIgf0DHume40bNHRbG9xI6mwc4fOLPB9urlTJdzN_9TEJw0Tj4fo7DFyczRX7RuAUbYDVaYmuKVY0CaAYpcfQPamhLt5AISP4nm607dAfDQ4Mlwc3AP6rFw7i6PHWjLT02Uzm50TIyrUNgSg70N5X2G4h7ijp_By2iMmQi7t2cZ7Xf-QeXaIT1h6jAxdH0zeSrfFd0ZjHQXfTle9lQuPuKN3kT2el3fb3jr3Thi9B6gPjmfZhJELPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از گرم‌کردن بازیکنان تیم‌های استقلال و تراکتور پیش‌از آغاز بازی
⚽️
این بازی ساعت ۱۷ در ورزشگاه یادگار امام تبریز برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farsna/467071" target="_blank">📅 16:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467070">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a74cabda4.mp4?token=dv7fD-kkezY2GtxOgDi4A530Xr69EqeQ0jFoq-8_ouYgQhm973MxqnDeBnqPTn6osCQyngvZXOnS_Jtc5QHOLmF5-q-3P1eveIaOpmHbOfcIjYMyk2AXVzq2b6gqELLb7-SP2NXwkbJV0-IayMYAAnxHT19jxzMaf1vyLxIBIuT5sHZSfWurg9dQJ6b1-RzyPv2-aBF-iVoPifGv3dzgh1Q0Be1CQ3YdOkYUK1Dgb1pS7em6wjeMAUuSAPV66H-eIeS_SC9PVx0mEk_6ZYb7SJxxCtIYB9iHIN5HCdh0iEHXnvDqDkQVZt4ZElDu3lSzECn_-pzqAv-YDguav_8ahg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a74cabda4.mp4?token=dv7fD-kkezY2GtxOgDi4A530Xr69EqeQ0jFoq-8_ouYgQhm973MxqnDeBnqPTn6osCQyngvZXOnS_Jtc5QHOLmF5-q-3P1eveIaOpmHbOfcIjYMyk2AXVzq2b6gqELLb7-SP2NXwkbJV0-IayMYAAnxHT19jxzMaf1vyLxIBIuT5sHZSfWurg9dQJ6b1-RzyPv2-aBF-iVoPifGv3dzgh1Q0Be1CQ3YdOkYUK1Dgb1pS7em6wjeMAUuSAPV66H-eIeS_SC9PVx0mEk_6ZYb7SJxxCtIYB9iHIN5HCdh0iEHXnvDqDkQVZt4ZElDu3lSzECn_-pzqAv-YDguav_8ahg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای از خسارات جدید آرامکو در رابغ
🔹
تصاویر ماهواره‌ای که روز گذشته ثبت شده، آسیب‌دیدن چندین مخزن ذخیرهٔ نفت و مخازن تحت فشار در پالایشگاه شرکت آرامکوی عربستان در رابغ را نشان می‌دهد.
🔹
به‌گزارش صفحه اوسینت، دست‌کم یکی از این مخازن درپی حملات نیروهای مسلح یمن به‌طور کامل منهدم شده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farsna/467070" target="_blank">📅 16:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467069">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09a8871ad5.mp4?token=Y2GeKJsr_lAaCCWwg0pnrRy3Lw1dWkZ3XraWo30Xz_jH1xo30PoWEbjSO2aQbq11lwwrhMnvXqwlhSIX9t3lYEGTu5YDBo3Pgi94rkp6iog5gnVYh0ZTGZuQZ8R3_WWbOccPrNzkndps6kjzBDyo_ZNxSZbiamJuIG5AfI6NL_wJTSNpgpS-g4ahW8wnUFXmFTfDoQF05BLhCXeSvfUk5ALecSCmgcjpTedqsljQAUYkTpC92wpqRL3W7TrKHtOkxcTPQUUhGXPkiqUDZPDuKqertkz-XSuFaSREpnE0tv3EWTTugXWlFFj3MrDq6ggkifg7UncU957VzK8WNLsx7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09a8871ad5.mp4?token=Y2GeKJsr_lAaCCWwg0pnrRy3Lw1dWkZ3XraWo30Xz_jH1xo30PoWEbjSO2aQbq11lwwrhMnvXqwlhSIX9t3lYEGTu5YDBo3Pgi94rkp6iog5gnVYh0ZTGZuQZ8R3_WWbOccPrNzkndps6kjzBDyo_ZNxSZbiamJuIG5AfI6NL_wJTSNpgpS-g4ahW8wnUFXmFTfDoQF05BLhCXeSvfUk5ALecSCmgcjpTedqsljQAUYkTpC92wpqRL3W7TrKHtOkxcTPQUUhGXPkiqUDZPDuKqertkz-XSuFaSREpnE0tv3EWTTugXWlFFj3MrDq6ggkifg7UncU957VzK8WNLsx7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: در سفر به ترکمنستان با سران کشورها دربارهٔ مسئلهٔ خزر که با خطر مواجه است، گفت‌وگو خواهیم کرد.
🔹
‌رئیس‌جمهور پیش‌از سفر به ترکمنستان: خزر سرمایه‌ای برای نسل‌های آینده و محیط زیست ماست که اگر از بین برود، مشکلات بسیار زیادی برای همه کشورهایی که در…</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/farsna/467069" target="_blank">📅 16:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467068">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f50e11eb2.mp4?token=Hj5oH8WYaw0GZlYV33IX4qCHFWl4aWwKoIppj6k8Mct7EmE_RlCn6dCjvKW_9jUQEXmrlN9YX8wOJmlBvdkgsh3CaISbL14haW_xBB8HiQu_qNaAyHqz0OeGCCzevVQ1bhptad6eo8kyztgslL1jsCr7-MrQlNXN7VwYxF6nrffTReF8JFSiE1lN5eijJ4tDR6w6Vu5-G_HNMnR9SXIeBIuGCtJlDTkHabCRKmBpHooMFU-SRQlYAtrYM0a-0F5lS0KTrw3s0bt7afjXcY7_nmT8cOlvXOqD4DZZoDu5tCEys8fGZO8aNHvjvjMZGkzmyGfnjwEYk2SuzVBjlMXSEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f50e11eb2.mp4?token=Hj5oH8WYaw0GZlYV33IX4qCHFWl4aWwKoIppj6k8Mct7EmE_RlCn6dCjvKW_9jUQEXmrlN9YX8wOJmlBvdkgsh3CaISbL14haW_xBB8HiQu_qNaAyHqz0OeGCCzevVQ1bhptad6eo8kyztgslL1jsCr7-MrQlNXN7VwYxF6nrffTReF8JFSiE1lN5eijJ4tDR6w6Vu5-G_HNMnR9SXIeBIuGCtJlDTkHabCRKmBpHooMFU-SRQlYAtrYM0a-0F5lS0KTrw3s0bt7afjXcY7_nmT8cOlvXOqD4DZZoDu5tCEys8fGZO8aNHvjvjMZGkzmyGfnjwEYk2SuzVBjlMXSEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان فردا به ترکمنستان می‌رود
🔹
رئیس‌جمهور، فردا به‌منظور شرکت در هفدهمین کنفرانس دولت‌های عضو کنوانسیون تنوع زیستی، عازم ترکمنستان می‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/467068" target="_blank">📅 16:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467067">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOoYUSLK_env5WLdHLxidFy-vjHlQbHjRH5PRTj21dT_NEmRBbvGie_MHg5naK9vKw4qoLlkJ3UrrU7JtiNMgTSAFv5HBJNc0vmC8ui-tWD9ymFbl7BH05B0mc0QkYZawm5TBGekFWCVc3tyX9XNdcfDMaVbf8dEl35Yzuiza6bwzwNXK6Q-SLVmgK0LsAoSEjvDsncZQJ0FqeewoWNfYQxOm_hWHyAsi_52M252c-L7Bxycoq5cxTTjHRzjnRItmbgP6TY6DJOJIUBt_1xlJ-xyZt1Tc86fLzA1QGXwed35XEUqYqOAmgakmQ4N9xhQLWjAVd7vXKvv4CW5txN1SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسلامی:‌ سبد رادیوداروهای کشور به ۷۸ محصول رسید
🔹
رئیس سازمان انرژی اتمی در مراسم افتتاح اولین مرکز دانشگاهی تشخیص و درمانی سرطان کودکان: ایران از نخستین کشورهایی است که داروهای آلفازا را وارد عرصهٔ درمان کرده است؛ سبد رادیوداروهای کشور به ۷۸ محصول رسیده است.…</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/467067" target="_blank">📅 16:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467066">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
سخنگوی نیروهای مسلح یمن: فرودگاه بین‌المللی خالد در ریاض را با یک موشک بالستیک مورد هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/farsna/467066" target="_blank">📅 16:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467065">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یمن به کارکنان تأسیسات نفتی سعودی: به مناطق هدف عملیات نزدیک
نشوید
🔹
نیروهای مسلح یمن: به تمامی کارکنان، از جمله کارشناسان، مهندسان و کارگران در تمامی تاسیسات نفتی عربستان سعودی هشدار می‌دهیم که از حضور در مکان‌هایی که هدف نیروهای ما قرار دارند، خودداری کنند تا از به خطر افتادن جان خود جلوگیری شود.
🔹
هشدار خود را به شرکت‌های هواپیمایی فعال در فرودگاه‌ها و حریم هوایی عربستان سعودی و همچنین به مسافران و کارکنان این شرکت‌ها که قبلاً اعلام شده بود، تکرار می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/467065" target="_blank">📅 15:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467064">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R66WtCZbYXqK6Pxg95tASBlZaIFeuqRs58BZ7uhenUvl0b7kP2bXDhhjXnKctR17bTrwc5HrUqk9F6RWGH5JH-xoe8Yw6UYoCihXVh29B21mt_kYcsro1Rmry1tJJf92O7yo6xHFkiNH0iN283ydfv69cHP7R6wpp4O_DR78yV9ZPh3AQv_b5shm__zmDsq19DcOyWObVmp536yWjoDESUOdMycdS2A0T_vmBR374Y8Y7is4ZqHtOYMiMNUgzkixskIignSJDH_eNJSo1lAN0TC1Z3UjYKrQXzmID-1KfSVTkGoiXkzKCWTPecba_HzPqqtrBDGXqBiCGKsL7Qz6MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برندهٔ جایزهٔ نوبل ادبیات اعلام شد
🔹
جایزه نوبل ادبیات ۲۰۲۶ به «آن کارسون»، نویسنده کانادایی، اعطا شد.
🔹
آکادمی نوبل اعلام کرد این جایزه به‌دلیل مجموعه آثار جسورانه و خلاقانهٔ او که در گفت‌وگویی بازیگوشانه با سنت کلاسیک، فرم‌های تازه‌ای برای ادبیات معاصر خلق کرده است به این نویسنده تعلق گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/467064" target="_blank">📅 15:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467063">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svC82rKD1FaU8alfjWN5SgyfcdPA6eUyeCxL5ucTAeLqZBp0utm7zjmwiiyVTvknIzGktuXLqR0NXtahbPCWKPhNwtvOaiRBlg_zy2PmMIReWL5jI9072uv26LpMrnPdXGYn2sJnOuZbrphXsaZlJrTwbrMfGHYIq4vcaZncDLiZNRQUGxfVm8kXMm4akWOS0UO73t_iq1p370qDaGmeziYUGz0cs7rwOKWDG1M1eCHvAVehk3g_deSgEq0nbXj7Q7qqHwULIWmGXK-C_q4hMmUC4Qtob5HuC1JSJG7u2IeFyUzBL-qGjkBfraUGDqeMSHya4QvKKwWf13OqWnz3JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: ظرف چند روز آینده جواب آمریکا را می‌دهیم
🔹
ما طرحمان را که تحت عنوان طرح ۷ روزه بوده را ارائه دادیم و دیدگاه‌های آمریکایی‌ها را در مقابلش شنیدیم، الان مشغول بررسی آن‌ها هستیم؛ فکر می‌کنم ظرف چند روز جواب می‌دهیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/467063" target="_blank">📅 15:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467062">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOoTmF_esNNbCERUQ_B6eQOIL-rJtxN4Oo90axIQSft8VoRn758sEnBNXIkBpZO_4qKwFsuhtQK8ZSAAU1Kbpv6NytYPgHkpnWum7DPoJFaV3ESqrgi-j4fqh9qMO_dPbHV15-ZjdxHh4aLiWrKLMLkJ5pHVhKfCbdxzOpNIObLseYLjsKA45-kNS2cz8gzTx0K8vkJlRT4rDo9Yh_HCENT-R_bVEUCNiXphk-z3qPZFqsKzt7xfDhEsU8MnOYThjIcAW-tvsTrAzyq_KDrCcMv9ZoQfmTmvhf5rUu1VNTRPBYoI4YRrNynK2hOTX3mIgLF70u0SR7dv1Qf6E_nbXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: باید با اتحاد و انسجام ایران را به جایگاه اصلی خود برسانیم.
@Farsna</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/467062" target="_blank">📅 15:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467061">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">انصارالله: جنگنده‌های ائتلاف سعودی، فرودگاه الحدیده را هدف قرار دادند.
@Farsna</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/467061" target="_blank">📅 15:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467054">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C8bujUALtp30RQhVDdQlRIBcJMEfMzVOm1JSeAwRVyRXKYsTXrpfZAIYdilLP1aRbbwKeYtUYsdkS4x-rF9SaKYdxboQcL0ISAERjBG9XA9Wdmj_wiZROb_mFoEzb2VPeCXIaZMkHLhqg4SmCuavdllKcuAM2FY27eTBE8FbXP2lmeHLK-KO7YYf4JwDLecXRrqW_C_g9fDR3GRH0XLJ-S67IHLi5xfKHYtZpMGNaFT0woRvPbMQwd1UX8JYcck6sQPdPSIs0CXrLAxpqGyzCRMz_rb4l0X-FvgcaXrAeW-utQXpFM2fwPB4yZXtLRRYiCzipkRHVDkYiZbtNuIOKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c2xyB1hWEnjge_DtwKJEA6qOwIBWMNx3r33Gp9olT3bNHJqc7TnSEKhIn7J9D3RV8-C3vgw5lsrKisWUjP8OQ9plv0GNh3V_oLqYVpkRt7-SwrnZ5cynGPEG7-sQeSGxEeSJ0AL0OK5G4cSMNVB9YWJVRmWIU3OX5JDbVBmOdQj28SS9kwkGNc8Re_DxLT09b2pQCm5edVg7-pHBqdFY67RhQKfSjvTYYiuLPc_K4RFtcJL4vFRsERfcp7cNbCJdH6AtQfYUrVEo2LZ9YSLf_q3obLzXqIa0KFk90io8HrVfhDFJmd3Owez75fVowgzXp4eH-8z9atwyfmZBPU1wKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hLnOEfeWBRqt2YkufbcIWq6ITUmH1MOYGSX8BmYw4_17-ZYIAEzLreVTEFhFZgU-ct0p25M6MNOffSLG5SN5RlVgXOHI0l8bGV5WvOJpfyDnJvPgVVMc5CHOecg30N5ItgfuWWdCQxWDINVUQr0IXPLoMrL_kroLq8bx3QPz9MJMZJYMelcCSWhNLQQf5kGDy7fgsUEw-oyHeLcikJNDENi26C8hPdb7DdMu9pPm58YXSXyMEVQH03P9Y-IEA5GSaChnKJyzV32_Ei70IEZ3nsEsINvL32xOMI4_RMkOrVDJ3dgbMReo-OnYtEfPed6PVTxgTKZotmehxmJ44D0LMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iPQhhEq8pRik4RqOUi6eK4ASiJysmKi_BEKJpkubD5Chddl8baQkwopp0Y7BElkOBS9Fs5TkcN5QoXuONqxYsiCMc1k4gHgRYAF412pebJW3GGmCb7OqoAkarvCXF3enWF7x7RzR7nwJyjUXijwJOimceofRgKB8stcu1YfUNXt8_dkE3PoUGTJ9vBVdyhbUrKqczi7wXghDx3AsyH-Nwsqj6K75Nxf3dxk-P-otHE9K45GqLlC0u6H2_7nGoOEfIOLk6ua63DJaBUmLqaKmt3bEgCfyRymfEUQoPyncpfUfQFI6qBMYX6rLGtTcX6T7K5cqxT3kcfKfVRBe9x8zoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bc49bJMk4crRj5GJ9dhRCy9W8pZxk4508gHUwj2w4oKj1h0qucatMIKwfPCchDKiAhKwXZHId4H1cNx5NlhNNAquaScuCYiRclOCcIO-SLW6SupYvidPN8ecpUplpoay8iIlXo-DN8sGtxPxNzLk6LRCvmNTFjoxe5pLmQs9QgeSXOvg2EDnXAPsd5GUOC4wfxQ5-16pnLHtqJf_C1LhAmEmqXhpmJZWgN5obkZU3c0f5ktUUR3oA_gSVtzsbrevSu5FlRPTtl_0aJzam1XjnfoILVCTimIrmEHyxkuuKslJc4bcmC73vbAYFQSmj1f-PIbjyN1BitValj1hySsAhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hr_A-pP0OokSeGoGY4AzdS4oI6QshWSzEastO8V08jSNb0y2A4QAJFzPbnbDPxq2pWWqg5Rs10o90UsSlHVXDDtokxyqnLaYQaqgvu7kxwzsHz-8TURDvN6_Hqt1MeJQUQJwFgLIE8lb5bQCjCuJL7idm1aOEswk2HZwcxxbh7RsJYFtA3b4B1bjf0QvLPxKD37tFSdCx6_Fl5fO3upLa0VxSogqli6PSSpn0OQ2T-Vn-LA05TR-akIffC1E_8mGe4rztm5cysFvla2LZl8KS1mdxzo5azTlFQFFR0ZN31aN9JCbkSb2x52ektQebsnysaQt0DxSBaiEjni--sFmog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LA8-GCGK49umO0qfyCPjbdpvgW7SETG40h1Y8HE6pXtn9o7F-F5Xs-1guz484hUB3PHHjMpUahNtvmbWhbcHjLBF-_RfulqCwBgw_oaDt_VMBVumBb_Ra__AwKlwKAPl_xuZuCD7o7cMlbT1ISn_FUfk-uYdSKAH7PGf3Y5XqZTPUdZuGFRArO73OOix1aqVsjIZ1ksfk7yivNUCRGdKIGQMtt2D3nMXXiuCGT1C6LGhJ6qgvcEk380dY_15CHkXY42DbmJL2_NwN_nmOzjnQ4d_mv8juAitrkNWnRv-tAxPKXahUSdBu-kN1vyYnZPIOQ0s9xRcYfSu8tm8YBP-1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مسابقات سنگ‌نوردی قهرمانی کشور در همدان برگزار شد
عکس:
امیرحسین ترکمن
@Farsna</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/467054" target="_blank">📅 15:13 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467053">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhY7rpJYWQQAVJWX7y2ZDlr_DzNlwAAbiW9NDoxKJ9AjNoI1YV5Gvlv6vl90Syn3QZuGzzJ8klJ50H34dE72jVHouoX02hoqUoN_3eFy_y4n3clCDv2Ntz-FXq5slw6Lgynm9a6oWcX8Wlt6yhn1Yrp3JzLCsddxy317NemJ2pJfiGNC4cME8RbO5FXIVUmt9l22FNfS6XcJx1-9fk4inwbyNe8G6TIjtQ2AQ_2K0GC5axq1Xa3roDxjLZDOaBeGNPP1OQpsCG1HGgm-5Xd82kmKCbY30TxqXSzRzPEbw2UhJL3VeTzqaKeGWYafUzVzbY9UyuOYMUrU_es-wI3BQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیه: برای جنگ با کشورهای دیگر نیرو نمی‌فرستیم
🔹
وزیر خارجهٔ ترکیه: کشور ما تحت پیمان مکه نیروهای خود را برای حمله به کشورهای دیگر اعزام نخواهد کرد؛ این توافق، یک پیمان دفاعی است.
@Farsna</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/467053" target="_blank">📅 15:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467052">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1CrgWn3FZk-OxnupYv6nROy6slUUfizPuwiDG22uVRIkrlRBFbqSyvJBDLknyBSFNBfve_ccszlFC91RpFlgyPyTiHmHSNGrFxNWtEeoEewIH1tNRLQaSKv7xaGKX3xrrS0ZoSGsXoo0RBvU5Yd58bY8sviAI3jiF_EJcFOOd0NyR61bL0lpJGDxfg3ahLlMqFthpmmSNBVnN9mSvuKDdcmlxVbkv3jCEGo9YLbyZF3y1mEcYOjNmbDblhJe2WXyzBsuoDlx5NljGAiqz8mVD02UXFgA-Oh-RiXl9FRk4C6YLItbLD7W3kbgUxENPnDe7OCQvwy8fB3QGvHf25G-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پولیتیکو: پهپادهای ایران ضعف آمریکا را برملا کرد
🔹
در حالی که فشارها در آمریکا علیه جنگ دونالد ترامپ با ایران ادامه دارد، وبگاه «پولیتیکو» گزارشی تحلیلی از آشکار شدن ضعف نظامی واشنگتن در برابر تهران منتشر کرد.
🔹
به گزارش این رسانه آمریکایی، ایران با استفاده از پهپادهای خود برای مقابله با تجاوزگری‌های آمریکا، باعث تغییر در ماهیت‌ جنگ‌ در جهان شده است.
🔹
پولیتیکو نوشت: «رئیس‌جمهور آمریکا دونالد ترامپ اصرار دارد که ارتش ایران بر اثر هشت ماه حملات نیروهای آمریکایی و اسرائیلی "کاملاً نابود" شده است اما تهران همچنان با استفاده از پهپادهای ارزان‌قیمت "شاهد" دست به حملات متقابل می‌زند؛ پهپادهایی که مانع بازگشت نیروی دریایی آمریکا به بنادر دوست در خاورمیانه شده و آسیب‌های سنگینی به یک پایگاه هوایی آمریکا در نزدیکی ایران وارد کرده‌اند.»
🔹
طبق این گزارش، «هشدارهای مربوط به پهپادهای ایرانی حتی منجر به تخلیه تمامی بمب‌افکن‌های آمریکایی از پایگاه هوایی "فرفورد" بریتانیا شد و در ماه جولای نیز ترامپ را واداشت تا هنگام ترک اجلاس ناتو در آنکارای ترکیه، با عجله پشت یک چرخ‌دستی پذیرایی (کامیون حمل غذا) پناه بگیرد. این رویدادها گویای گستردگی این تهدیدهای جدید و همچنین میزان عدم آمادگی مقامات آمریکایی و اروپایی برای مقابله با این نوع جدید از جنگ است.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/467052" target="_blank">📅 14:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467051">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54e4259ce7.mp4?token=o-lFJy4G5lEYrgGXa532MFn5WwiSfVHsujMYdZ9VJCUQgRE6aEnAobddbbcLjPB_na3cVaRX-oU0083ddIKQ7k64fVCE7jwwR-6RgU3rkJ_gDPhszop6hbQgYQ-3PnmDlho9I9YT2xfTok1yZvUKsUQOUC-iIZAjBFMdi3PcF36ftKj8bIsGAHENIBSQqXeeADJvIwp3hgaMSZvb6EBUcpR9XNTrM20INIaQn9JwBkLtDcaaZ4hvAYZeoS1k-MsQa3ElfSbPe91azmF6GA3mdtpYSB6ALAPGaTw-zOmih-U66YKnt6siEaqwHXOlSowm32bV8Cx_rXo-yXzu1y-lQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54e4259ce7.mp4?token=o-lFJy4G5lEYrgGXa532MFn5WwiSfVHsujMYdZ9VJCUQgRE6aEnAobddbbcLjPB_na3cVaRX-oU0083ddIKQ7k64fVCE7jwwR-6RgU3rkJ_gDPhszop6hbQgYQ-3PnmDlho9I9YT2xfTok1yZvUKsUQOUC-iIZAjBFMdi3PcF36ftKj8bIsGAHENIBSQqXeeADJvIwp3hgaMSZvb6EBUcpR9XNTrM20INIaQn9JwBkLtDcaaZ4hvAYZeoS1k-MsQa3ElfSbPe91azmF6GA3mdtpYSB6ALAPGaTw-zOmih-U66YKnt6siEaqwHXOlSowm32bV8Cx_rXo-yXzu1y-lQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ افزایش اعتبار کالابرگ به روزهای آینده موکول شد
🔹
معاون رفاه وزیر تعاون: چون تیم اقتصادی دولت هنوز بابت عدد و تعداد دقیق مشمولان طرح افزایش اعتبار کالابرگ به توافق نهایی نرسیده‌اند،‌ افزایش اعتبار کالابرگ به روزهای آینده موکول شد.
🔸
پیش از این وعده داده شده…</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/467051" target="_blank">📅 14:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467050">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">هشدار فرمانده حنظله به امارات: بیش از این با آتش بازی نکنید
🔹
فرمانده حنظله: آنچه در اتاق‌های بسته می‌گذرد، برای ما پشت درهای بسته نمی‌ماند؛ از جلسات به‌ظاهر سری تا تحرکات و شیطنت‌های شما در کشورهای منطقه، همه رصد می‌شود.
🔹
برای حفظ چند صندلی و منصب سیاسی، بیش از این با آتش بازی نکنند.
🔹
در صورت تکرار «آزمودن محاسبات ما» پاسخ طرف مقابل به‌گونه‌ای خواهد بود که هزینهٔ راهبردی آن، تا مدت‌ها از توان جبران‌شان خارج باشد.
🔹
گاهی عاقلانه‌ترین تصمیم برای بقا، این است که بدانید کجا باید متوقف شوید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/467050" target="_blank">📅 14:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467049">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rqd1BfB04pBzU4zftL9BsaCVbzjLSyy_zEvfyhHwLmOe1znkjvGKdE-xkxjEFXjWJ4vacgqWgXsV7unKpkrjys-36zui5pbKL2SVVl3qI9XCb6qQXTfQZxHyf4-uDMQ-Yvcywaq5bfQmlXsumyZtXGt2QMWoOwiTagWcC3EoXGUhxPni5__uJKcuDY_jWAu4OcdR3lt5t-fFiA7rCaYL6_G0bBM2r1qXhJenGDQOcLXtiP_5dmubp8j4AM15cGZlxJ_aoBv8VPA77gSpIi-tzfqoY45LyeZBMgZc80qN462uNMXyKltzsEQaxsdOQrnDXYQrOR3nuJ8_NTSa3cZnew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سردار ابن‌الرضا خطاب به سران آمریکا: اشتباهی سربزند تقسیم‌بندی جدیدی خواهید دید
🔹
سرپرست وزارت دفاع: او هنوز جنگ را در مهدکودک پنتاگون نقاشی می‌کند؛ غافل از اینکه جهان را با سخنرانی و نمایش نمی‌توان تقسیم کرد. «میدان» حرف آخر را می‌زند.
🔹
فاصلهٔ شما با ما را موشک‌های ما تعیین می‌کند. دیروز دریای عمان، امروز اقیانوس هند و فردا خلیج خوک‌ها. اشتباهی سربزند تقسیم‌بندی جدیدی خواهید دید.
@Farsna</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/467049" target="_blank">📅 14:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467048">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWhl1gxkdCc360K0DgOszqe3knDMySria67R-XVrXvT16xGAc-wTpFw4YTs70jG0Kox5QwpNsdOmJ6pzgRqWtgnE5gQ76J61zH_cfpNOlWByPNuGVk1x83t8GGrozBrK7Btc-d6m5gaxJTkKbTnrFylsUbsssvVed7P-x2Uc8GOIpojSzgt4pxk0hqzxZ1zv3IlwcUS8VBNGuiv-GsvI0nIyyHNyjlEPgJnCn2ooow9aHsIT0owmV2_BgWwm2aZC4leZNQoC2ZYgVfE_VlcJUFfZZwGjo0UjgVVNrWHDV7d1Z77CeMkOunao79TmXRWkPgq-MGwAyXlTEtj2r9dvJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اداره‌کل صمت مازندران: در بازرسی از یک واحد، ۵ هزار ماینر قاچاق کشف شد.
عکس: وحید بیات
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/467048" target="_blank">📅 14:15 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467047">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f94a138de7.mp4?token=TNiX-3v61PaTI8gvCUyPc52KSuo1N1dRj3scRibQ_495ufGGJCr27rX47RegitbqRGr6O_rFG6KM6cBy2_IIDvCUbGGrrou-rDbfz40guyLqVyiiBY0XGBxGcpzgHWkmMGwP1hg7QCGHxV6XD2Q5uGwGCo7kMkKgklD-4x8ZSvVLPmhnfmjE0T61r6EtKZDdFkq46DvN6qVBrb6mFJJ3Y2bO62TS6Oe2HHiO9KlS3aoIpDKoAPA6-OZikY9zp67_Vv2udhNUIXtGWOed3t1Vi4NJ2krsZuPrGEw06NOpC3KLGor_KzYstXzWJOEbNX4J1aFbgblTzDiIYMqj6eJU-BFMwMuh9ZJPqalV6jYR22dCyU9T73Qol9CEMYR4nv287YfdeHCcE4RRtPvxFDvFfiZ2Ls5booYuIvn_z08mx2nsdKGvmrw0D_Mm1T-MSg47Q1XUHvDanDC9RcbS9VTu5hdYBGwyhoN8DzBjVrEvAKE4wI0FQ_9f1_l5zA82fUDL1Hayuw4FkGP85iN-YeAFF8Twxr_jn0ZdQOp9AhyLDu833o1J-_v5-zh_YV1nw61vSpgNCQUMU2LyYWMf0kDzDLqhDhpU304jcbsrOHtldUmfFyKx-MMDdmfRjOdIP4vOGtav66wEHycwVdtbbwq5xHGYax75HHAI4bAB4vRgJLU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f94a138de7.mp4?token=TNiX-3v61PaTI8gvCUyPc52KSuo1N1dRj3scRibQ_495ufGGJCr27rX47RegitbqRGr6O_rFG6KM6cBy2_IIDvCUbGGrrou-rDbfz40guyLqVyiiBY0XGBxGcpzgHWkmMGwP1hg7QCGHxV6XD2Q5uGwGCo7kMkKgklD-4x8ZSvVLPmhnfmjE0T61r6EtKZDdFkq46DvN6qVBrb6mFJJ3Y2bO62TS6Oe2HHiO9KlS3aoIpDKoAPA6-OZikY9zp67_Vv2udhNUIXtGWOed3t1Vi4NJ2krsZuPrGEw06NOpC3KLGor_KzYstXzWJOEbNX4J1aFbgblTzDiIYMqj6eJU-BFMwMuh9ZJPqalV6jYR22dCyU9T73Qol9CEMYR4nv287YfdeHCcE4RRtPvxFDvFfiZ2Ls5booYuIvn_z08mx2nsdKGvmrw0D_Mm1T-MSg47Q1XUHvDanDC9RcbS9VTu5hdYBGwyhoN8DzBjVrEvAKE4wI0FQ_9f1_l5zA82fUDL1Hayuw4FkGP85iN-YeAFF8Twxr_jn0ZdQOp9AhyLDu833o1J-_v5-zh_YV1nw61vSpgNCQUMU2LyYWMf0kDzDLqhDhpU304jcbsrOHtldUmfFyKx-MMDdmfRjOdIP4vOGtav66wEHycwVdtbbwq5xHGYax75HHAI4bAB4vRgJLU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: با تصویب مصوبهٔ حمل یک‌سرهٔ کالا در هیئت دولت، مرزهای کشور تنها محل گذر کالا خواهند بود و تشریفات اصلی گمرکی در داخل کشور انجام می‌گیرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/467047" target="_blank">📅 14:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467046">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gECFkzfMJ3A32AOOJokTYcjFSVB1o0Vw2by0d3eWDbUODXi97CqlgSjmcSYjSBbizC2pOfGAWjpMJ3C2pke_4vjj1L6nq7lMTqEElC5Pz6Vo6gOxBExfeIRctBxa2E4LSX5_ANCn1tLXk9VCxOLpxOrCDVm5_pvPJyDBxJhyJA5TmJBft3Td1bd_RPy1EOo29RzmNLtrLBJUeOyouVzjx4ccf59ywcKecF1l8ERPahZfM9N8OtRC2l4vUnqWNetmK90vTFdJXLJxQsDqV7wD-o1EYFUaGeg53OR0idhuJxQXXuGYEgjDSfc1d2jraMcNymIgw1cXlWteNRPicZGHPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
نخستین مرکز دانشگاهی تشخیص و درمان سرطان کودکان کشور افتتاح شد  عکس: محمدمهدی دهقانی @Farsna</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/467046" target="_blank">📅 13:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467045">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/345eeb05db.mp4?token=mi_q2L2XNpuHq313KwTKww0FjHdlNgw9ZeYGVi1Sn7Tis8xGNWgLES1szxdZTUYIE5XGsK5a7vIxUJQU6cirTJpdkk1R4rNWC5s0u-iRGorFIyLAW87DZyd446TmjdK2hEEBafgICzZJbV86vUXnQBGOGMEBKPj_36cRT90ogRk-skzx0DcnrluNvTs2Qzn--W2rDkl8yxLwSfABtNcEMbQkb5LPMJgUsPiheuV4uPF6_CHHUAE381T1jHxqaJRQUGKx-en92B3YZgZ8d-bJ_WtQkZOoh6RkLpk75kX7X0XrVWOjrwIaCTKcPAPHS5meL2oPQK-JphDIrQ1iWgsnhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/345eeb05db.mp4?token=mi_q2L2XNpuHq313KwTKww0FjHdlNgw9ZeYGVi1Sn7Tis8xGNWgLES1szxdZTUYIE5XGsK5a7vIxUJQU6cirTJpdkk1R4rNWC5s0u-iRGorFIyLAW87DZyd446TmjdK2hEEBafgICzZJbV86vUXnQBGOGMEBKPj_36cRT90ogRk-skzx0DcnrluNvTs2Qzn--W2rDkl8yxLwSfABtNcEMbQkb5LPMJgUsPiheuV4uPF6_CHHUAE381T1jHxqaJRQUGKx-en92B3YZgZ8d-bJ_WtQkZOoh6RkLpk75kX7X0XrVWOjrwIaCTKcPAPHS5meL2oPQK-JphDIrQ1iWgsnhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🖼
سخنگوی شهرداری تهران: روز گذشته و همزمان با شروع طرح چشم‌روشنی حساب ٣٣ هزار مادر تهرانی در پلتفرم شهرزاد شارژ شد.  ‏
🔹
از روزگذشته تاکنون ٨ هزار مادر وارد شهرزاد شده و هدیهٔ خود را دریافت کرده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/467045" target="_blank">📅 13:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467044">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">احتمال شنیدن صدای انفجار و تیراندازی در مرز مهران
🔹
فرماندار مهران: رزمایش آمادگی نیروهای مرزبانی عراق امروز ساعت ۱۶ در مرز مهران و داخل خاک عراق برگزار خواهد شد؛ احتمال شنیدن صدای انفجار و تیراندازی ناشی‌از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/467044" target="_blank">📅 13:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467043">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MlbqgUR_1VYyqRD6Ryq2W-K4lItdCDiwqb2H_6VIEqH7hrGFwzZqwrEMHFKS8CfT-KQ-Nci99X4FbRd8myxlquIgJ4OSf_I9TJxzU0vWsi9epzcX5VfPBD6zoajoIF_WtTfnJo6MYaoycOUpsXK1F3vp5whTQqZ1OSvwXeHFOC9YBmZDL_WRwIy_NIfXhVxf-afQJsOidLfbStvo2qYyoQy2JJoeBJ8QQi2QdRMP09WCd3Qg718kQqI_foeddSQcUltjPGzgmQShmDzJte1ZfNwIQwN4aI982PNNMoWyupxZr6S2eUvKz7AHzrXmcsRrMHRp0N5aXryDy8F8-x0m-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ماجرای طرح هدیۀ ماهانه ۳.۵ تا ۴ میلیون به نوزادان متولد ۱۴۰۵ تهرانی چیست؟
🔹
شهردار تهران: اعتبار خرید، خدمات فرهنگی و سلامت و بهداشت به نوزادان متولد ۱۴۰۵ تهرانی تحت عنوان طرح «چشم‌روشنی» اختصاص داده ‌شده ‌است.
🔹
اعتبار پایۀ این طرح ماهانه ۳ میلیون و ۵۰۰…</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/467043" target="_blank">📅 13:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467042">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‌  عضو دفتر سیاسی انصارالله: بعید می‌دانیم ترکیه و پاکستان مستقیما وارد جنگ یمن شوند
🔹
البخیتی: تلاش می‌کنیم روابط دوستانه‌ای بین کشورهای عربی و اسلامی وجود داشته باشد اما دخالت خارجی در امور یمن را نیز نمی‌پذیریم. @Farsna</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/467042" target="_blank">📅 13:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467041">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
منابع خبری از شنیده‌شدن صدای چند انفجار در پایتخت عربستان و توقف پروازهای فرودگاه ریاض خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/467041" target="_blank">📅 13:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467034">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gv1Un7iA0T5sV2FZ_-gfnu9kPsYmiPwDjHF8lDRy3Vhdl1koZkj9yYjfv0N2cuH9WRDIVi6K5WIDzUrN2gQdUQp7pkQApSmlkULk-HLTWH4sbOmzkjPG6OZYChyUUaW6_R5OqeH6pOuoNeP95pPT-aP1DgJ63yFXHldzCmjoP-yWFOmKPW9Yfmtlc10q1kN9kFDvMmh6LBjbEBxnt-PDwcvxIbycxqqWbBOU1BAvX83kRz9yshjinC6CYd3i5YNo1IWh8pct6cs61ltjmFVkhNrxP0m7mDp3cSf8dyv0aJ_tMFd17Ya_a-wP_zLQ_FK50njT5ywq01aPPJ4pzpo-zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tw3gh1vzI355mh5RyZLnZjU80ZLkUCbTKpYOp_yE81QoVA1e1zwWnEuIkDW4KPS97qfWcPMBJxWgXofgGqTWptEGe1v9Sj_Wf2QEzyG4BI54XHDo7yhajXiLe2TdnR1QCOm_th2iBrFrL4kBnFBbbzdrRwBIH2FwJOqR2mOWjeozdlO39euDscKhSIfC3iXqRlkiD9HSKafw1dZZj78Dr-iivNZNdwhMrUgTGPBz4kv2yNIkrcHmXcw4wZuCc3x9NlRKrPZUnL67lV6IuxDtiCEDpxH5WAY8uNEyVTVjzRZapGSaf05eQ-odoCyXgbgOnXHysFtwGRfOmYZfLBJbHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aIt9bGMk0JW9f36X0RLJjuMGF1rNtI5DXhJe1Lc4luBKHKu0l93heaAcGGTKBDdKUh2Wv4TyWt9YunbXGV5dad3aznKpq8SidQ23vWR_uCJsrBvHBUfkpadLeCmVBU1tV8QAFKJBZVJxQfdtJDINmS2bMFRrLFcasI5GVU1bz32OPrMlLiGnAcUQQ-LhkQbtqQzppR0nPkUX2UpZCZZXcRXkN8JLWJymwABwZuoDJ2ir0urvKGFU2rfjuRCPLmATovUa7YvutWh37xEiPm2TkRHgIINpfFnsrpfvmiSjB6YHwbmClS8_a0zYWnEdwX3KkFBE4LN7jYidrZComXtHqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rarQdnBpK5BuAFcdOyCL6xlxQ2M6lpuNAlBohzkLN0GbTO6rdeVpklSeohonMfBBlNdtljM7yjrKNHy_F22siDpuJGvxEf0ZwbAI9bDBA9PZtGz4zmtlraG6woPm-fQt9ksMAugo1esfxXhosEW60M-fVJXd26r0nxpu0EfsveeQT58JxveYHVWxWpcY_-7RZ2_G0lnyojXxvq58PyRRYiJjur-8c7KK6gL_pUhV364dFgGeD7pMwc1Oa2M2hR5Tyem9pWz9DGXlgdXhdapeDzDY24n4BwdXVLU-vLPhRJg-uhYOLw12T5rULAsfm4qvrqQ4IU2boH4mU6vz5HJo8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LgDpzrmYn3Da_OQpNm9e2t1ccPkjyVtREiYCd3ORnQnv2iFUJU2DSSzmcbbpiuf7XTMjj-qoJ2SBOX7c1AI2QOaSnFuAUN7YF_5_LylqinH_xcUHRZuNd1Pxnfkn_LPDDK55eEBklOr1AH9iGbIqU2D96QI02ZVt0Yz6ZvP2xw3DWHI70_7v2dTrlPwqyeCX3UoEb5XqImwcY1DdndgPBoHdpTD3PHeIz0LtnMrQzch5rRHyR-neizePDomF3I4BhA2vkQYmk-OhScK_MICNjirLMFubkKfCTQzm_JU9Lz67nZFDj3uJugVEjopd-x3-xCUiupb2wvTGKpih-6_JJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X-bzurtR_4zHV6tRHg0UILo35tlK5B1jwMxI14C3LIyd0A5wIR_cJUE10RWG9BOR--M94ssY-2x5xfF6pqc8XuVRa-TGQQ_HN5QCHeH_LKUqC5Y0x5F-OfUQK_PTDHap5ugTezaQO-TxdjOSZiyHZ8tgQfagBPEuPZzh-ULf4XaS5aCaTkTATI3HorF1O2LF5xkxZU125vk5A5j9CH3jE4Ah1krbIhsr0Tb-3iesgbuiuMD1KplOcA2ygMJs2LVhcVVGvilZjNB0in8sLSDoF7_iBwmwyoOs50UDP50S7PBlPuWf6GxKag9f2pLwLFGH3Gmh62GE2ZO4V2ISbg0OxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dxz3DwQMkqj70ykuIBeKQ1frFA8c3TK7_VS7XN5NWzP4cKizsNDr83ka_NJUyr4l5dM6Po0vvmUrEp1HOLcT8kBLysSYnYHdRkvp0sptcebfXsPKivUYbjfM4XS6wUF_bc7oLAAbzqwj0cbMZ5zCMpPBXAu6L6cvLZw-0ke6ZSg2sFL-CTEmymrUYcKVctTNBlVeqCYeCDGrim2PQIq6CfAM9PuTG3x_hDTurRlYOGGU-d7CkRD0SZm5aW3j5mywpRdjIIX_zpttNxCNBXHXDLRdR2WUlNDwGS9eeJIrhIY9kIGIFf52jmltpyUe0Kgyujz65pDtOAWn-vcNDHZmPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نخستین مرکز دانشگاهی تشخیص و درمان سرطان کودکان کشور افتتاح شد
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/467034" target="_blank">📅 13:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467033">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmpaUpEh7iT475yUGoKrGGqmGNb3RD7PpknPU-pn1jjEBtURVvriAXIeclOR4LfoqFAkJOTy1fyu0sYs4M3OBqMeovIyAbnCehWbGW16nltlBS5Vev9VLyZtl3kR70WmmUhkOTpcC5iGlTnHsdlEGOAKvr-UuVFJ5LCxxooT6tEmlldc4tVeq4ODCQRDzBpi-q3W9HdF5fOqD4gn991VHFxm9LpjiHd6SNuJpK9rjYMwDkdlUX1YJWfrzfT_hzPY0vLUO4RW6EAxrXpkESdXgiNv_wf7naoHGEOZLAAo7N-1_AkmQaRsgupd0338tTKFFHwfwEpMoSeuQlxkcemgSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار عظمایی: پیروزی میوهٔ جان‌فشانی‌هایی است که در پاسداری از وطن رقم خواهد خورد
🔹
پیام فرمانده نیروی دریایی سپاه به‌مناسبت روز نیروی دریایی سپاه: در نبرد بين لشكر حق و باطل همواره نام نيروى دريايى سپاه به عنوان طلايه‌دار جبهه حق ثبت شده است.
🔹
۱۶ مهر ماه به نام روز نيروى دريايى سپاه نامگذارى شده است؛ روزى كه دلاورمردى‌هاى پاسداران خمینی كبير(ره) را يادآورى مى‌كند كه نه تنها با فولاد وتكنولوژى بلكه با ايمان پولادين خود تلاطم دريا را به تسخير درآوردند.
🔹
تاريخ هرگز فراموش نخواهد كرد زمانى راكه فرزندان تربيت‌يافتهٔ مكتب حسين‌بن‌على(ع) با دستانى پر از جراحت و قلبی مجروح در فراق قائد شهيد امت درحالى‌كه خون گلگون شهيدان ازهمكاران و فرزندان مدرسه شجره طيبه بردستانشان نقش بسته بود، لجام نابرابرى را كشيدند و شكوه حاكميت ايران اسلامى را بر پهنهٔ خليج فارس تنگهٔ هرمز و درياى عمان به جهانيان نشان دادند و شجاعانه ثابت كردند كه در راه آرمان‌هاى بلند انقلاب اسلامى تا پاى جان ايستاده‌اند.
🔹
ما امروز براين باور استواريم كه پيروزى نه‌تنها با سلاح و تجهيزات بلكه ميوه صبر و استقامت و جانفشانى‌هايى است كه در پاسدارى ازوطن بانور ايمان رقم خواهد خورد.
🔹
شهدا با تقديم خون سرخ خود صراط مستقيم را براى ما روشن ساختند و امروز ما با تكيه بر ميراث شهدا همجون موج‌هاى خروشان براين صراط مستقيم و مسير اقتدار استوار و پابرجا هستيم.
@Farsna</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/467033" target="_blank">📅 13:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467025">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LowMGNJZP3WJF58cYuNjAwVLM_i-LV4uUZuKSIjG7vSA5Iawq7qOt3QPKT4GJo0uGJmBfOZRcpPKsG41F3cZYy9BymRuTCLWL_UTW0gZkoqTqcLlgcSZgdmqcf-m8KAMczPSOAK3JhGJ0hmJKXAheozUp8LYU9Ui4mwEJi1983j3giOoEXMR15aZAvgrvOHVAM7kGyt8rfVV9BJV8wYAgjIBrF4_LNxHiSWNWOPHs9KemHQPH5PyAeQPwjFXSgJBCDsPxQ5A44rlvfRo7_4V5SbA8djP55gMlVnRRA-RxL_tNubPmu1MBEzrkNfb-8H1V66-5itAFKKgHsr0g7K3hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زخم‌های اقتصاد اسرائیل ۳ سال پس‌از طوفان الاقصی
🔹
۳ سال پس‌از عملیات «طوفان‌الاقصی»، اقتصاد اسرائیل همچنان با پیامدهای سنگین جنگ از جمله افزایش بدهی، کاهش تولید، مهاجرت معکوس و تعطیلی کسب‌وکارها مواجه است.
🔹
بانک مرکزی اسرائیل هزینهٔ مالی جنگ از ۲۰۲۳ تا ۲۰۲۶ را حدود ۳۵۰ میلیارد شکل برآورد کرده و می‌گوید اقتصاد این رژیم تا پایان ۲۰۲۵ حدود ۱۷۷ میلیارد شکل تولید بالقوه را از دست داده است.
🔹
بیش‌از ۶۹ هزار اسرائیلی در سال ۲۰۲۵ از این رژیم خارج شدند و حدود ۶۱ هزار کسب‌وکار نیز در همین سال تعطیل شدند.
🔹
بحران اقتصادی در مناطق جنگ‌زده شمال و جنوب همچنان ادامه دارد و بازسازی برخی مناطق تا سال ۲۰۲۷ طول خواهد کشید.
🔹
بانک مرکزی اسرائیل هشدار داده است که اقتصاد این رژیم حتی تا پایان ۲۰۲۷ نیز ممکن است به روند پیش‌از جنگ بازنگردد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/467025" target="_blank">📅 12:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467023">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/duMBZ7FeftGuzHbKySavk9Ogl2DFTF212wcqm9HbJygWLES7wjO3-60KfEKOToPOwmTIQ3KdbICrc_Ms0oov1zPUHJaoiZBej5JQ9w1t7kmK45r5hRi85dP86QUIo14558hLN6oBVBLjWuPiU-88FGFvqfnM0stAoLPxtp9vDvoEJFE_ZFt0L8syQlJfdfF__dXRn7-cvhUQSdEcjUPdlCcdBm8_exg2jvyl2dmFdWfv7lBN-DMHKfwyvCTbkHrjgD99_JixwHCM3kJ-KZjxFnlkcthmYuIBo06KoGtFS0XSDGaJZo7tLoKCd_WyBUyE0nA2ykegA51sGLDgXBKVvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4fiQZk6tSwvcEirSK3uZVG0BSP__4d7tpZZoIrIE-3Z-K03BiQIuEw3yyatF6XerRfeD1xeF9k0Ox6ZPJkNasIzaUB7EuY2rIZuGwC_fbAumMHdILK-1QXMCVUeFTyCvkKc7bukxWXW1xyoyCTOGYTh0Sn0EXoMwleXX43wwX5eQTjNM21iYaDE0ZkV7j5LuNCLF-WicoXKyYan7w1FUMun7NxrtfHtjapP4T1zXQOPWyMyQ_onlPd_fF_SVnUZ9HtZswy67LFH1h7nXEkF_wlk6yX2nzg-PNKSFjil03DNNBq-7l1VRC8FFF96hmVsFU2tTNDt9AkBi6KkcgAz_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رصد قایق «شبه‌نظامی» چین در ساحل تایوان
🔹
در حالی که تنش‌های غرب با چین بر سر تایوان ادامه دارد، رویترز از شناسایی یک قایق «شبه‌نظامی» چینی در سواحل اقیانوس آرامِ تایوان خبر داد.
🔹
به روایت این رسانه غربی، در ماه آگوست یک قایق شبه‌نظامی چینی به همراه دو شناور دیگر در سواحل تایوان مشاهده شد که این نخستین مورد ثبت‌شده از حضور چنین شناوری در این منطقه حساس است.
🔹
به روایت این رسانه، «مقامات تایوان معتقدند که چین با استفاده هم‌زمان از امکانات نظامی، شبه‌نظامی و غیرنظامی، در حال تمرین برای محاصره دریایی احتمالی است.»
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/467023" target="_blank">📅 12:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467018">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h6oGFsEU8XPBGx8peg_T2VPR0mSfwelKzlZK3UVMsgJehdU4mOB75n0JwidUJkrFrutW9KOv-qF0-pTkdg7R1tbn-4lUa8qiokSQ4kz1CwxE0He3BaW1qR5kCWQwhYIZVFPHrWzqIQfYNeE0Z5-lX9Cr9CH5g5ePppWvx0_88atlESuO79yk6DSkX6Hn_kAc7mAKX5KzbnOm9n_rLAElKWqKEYt3zw7fTSkh7iBWseQMnEmRZGDusumUXsN0jj5rMEVxvd2Vpc50hr3IhLbNb8w7ppYIWG3pKa2050d2U2KSjh7GGGYKTWrxEhPrKLZyUI1cPpD3mi9hzxfjtGF2dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YtWyDGUQ57J00FCPyOc6xBja3U4KqDM3vSedLqazgE6PCDxghNmPm7t93M1r823pxZ4Uz2suob_kfN9ycChIpC2218k7pKLxLCPHbAfZAdLfgRkORlJA-e9NVkE9YJ7o4qcBPiSB6ajLC6jvNK3ocA8wt6BbirNwyrJclUAghPWO12zepAsj59I1XBaMWIvuiDiNm__IXXBXnYynSwUUAbS9gXoqUrAIagDkbVoU-dKhqExYGt2kTc4JnXmhRoaQdNGPXCJKCjaKv-brIxbz9tbJNUsTUtL2ai7MNIQCw4I2wEYjCq9G51EVxp4tio8WWZ6hhlKStQwgaNKiucbHCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qmgr86B1Ge9F7EWnX9N0CkSbaPuJ-OTSYt2Q_AHYkOwHOg6tS7yMwdng3nNvuaScFAztldQd8sWJ_SZIodi6QrhEzl0dRLWi_TGrsbp1tPia-yaYvBTr6MCAYScSCvtitKDKo7jEAV_lzLmTKXjwILdGAKIQYp07f2HrEZut2-XDKa890Asn2rTuzzSDpSrwjvtCA09kA7mhJEHVCFCXg2XJjBQCeCr4jCoHWGZWrA3HqSsQSleMTZELYgWA-tSuAZah7E4EbtKlV5uhrkAWUuUQwkKZqrg8S7dptqZKtmna9Qzf5Fu0GcVr6YHdj8KnEq2jSFGNX7zJE3GamWpt8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gpy8DmAVumJAJeDfRuBpJDY7NzYkZ5pO_haTcOS6P0QmT_-QWASPW19OK37nCP4qm7-DtjWqiv-Sbu4Hx0aJRSlen4a2Dvnf2ekXW_pcjBEbsBz4Q_CatfFzu6zBQ8IoQJDWs5e2tdJHH7_oi1UCHOveglfFvzmRb7tj_HSX10KmY874zajhd6jq43ycvjb4GqiGm7gJwe3OqlEwXYJTAb8C1rnstTnspI145NjrZNtoMA4xhLMGAiusf29cKIA5C85hGoCC1ZXb8ImAi5H_UV8M1yybGH1dbUgOxI4bcSxPok1PT_eZsUXXnd15SqFKIAJFRoy4dcSzODJ9DvuH7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kYDjbo8j3Awlq6WoRriv7aJJDfsWkwLISEbA10i2Wy1GWbX7cyRc84ligfDd9x34MsZlebAIUGj0H7g1iY7pwkbNvgIGiHziT8sb5MwuwsSPZ6_PShYnFhIJL7V8LcnxhG9EdLdAfhXo0AqJOf231CYgKbqKBzVGgVq74MgxnOX642Q2gHFmthJT2KoTemoKpslauopfmuhJG97413AK_P5o6Wctf_NLNZifsbTpolJ4_WvwyjYZlWcUiwpsWNaKDp7WVilxtx1M6ojLBR_pFPGrmko25M-BXSUnt7_OeQXgly3pn2vaekcfFPPPyjhF2frFpjJK2JBC3ECkQ7T8bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور پزشکیان در جمع فرماندهان نیروی انتظامی کشور
@Farsna</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/467018" target="_blank">📅 12:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467016">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea3dbd405f.mp4?token=TUrs0G6RpR3_IqHzH0lra9Q2uzAabOYOr01btyjilmiw5ziMHdUDQO_cB8QK2zlXIpHM_mho8gNl9V5hHsa3Px40ijCcP-rU2Ss2p6FQLY0PJxyex7xcKfWcyrD3yVGQn6q_BuEvEcfwaLLa1XGcNLytv0yqYrcoDY4O72vQdwH3jDfVUd3zBQpnipTgvoW4tfsMGKhJRL1sFfvvdGJoafBfUu7MskEDavxjz9hcL789OqwGrpF6blQYramSSgGC513GpL_k1jZQg-1uHBXanyk5hRWavHrP6XlxGr_N0vqGIlOTixs25VIjJfUC1pQHNNOk6OgSrix4QCN7iCpgWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea3dbd405f.mp4?token=TUrs0G6RpR3_IqHzH0lra9Q2uzAabOYOr01btyjilmiw5ziMHdUDQO_cB8QK2zlXIpHM_mho8gNl9V5hHsa3Px40ijCcP-rU2Ss2p6FQLY0PJxyex7xcKfWcyrD3yVGQn6q_BuEvEcfwaLLa1XGcNLytv0yqYrcoDY4O72vQdwH3jDfVUd3zBQpnipTgvoW4tfsMGKhJRL1sFfvvdGJoafBfUu7MskEDavxjz9hcL789OqwGrpF6blQYramSSgGC513GpL_k1jZQg-1uHBXanyk5hRWavHrP6XlxGr_N0vqGIlOTixs25VIjJfUC1pQHNNOk6OgSrix4QCN7iCpgWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای از خسارات جدید به آرامکوی عربستان
🔹
تصاویر ماهواره‌ای نشان می‌دهد که به بخشی از تأسیسات آسیب‌دیدهٔ آرامکو در جنوب ریاض خسارات جدیدی وارد شده است.
🔹
به‌گزارش پایگاه تحلیل تصاویر ماهواره‌ای «سور اطلس»، یک مخزن ذخیرهٔ سوخت منهدم شده و لکه‌ای تیره در سمت راست آن نیز مشاهده می‌شود که می‌تواند نشانه نشت نفت باشد.
@Farsna</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/467016" target="_blank">📅 12:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467015">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pepnm0g27_J6LBu_luubIcstbQAr8EXOhUTs69JQmC86H6G4QLNmHp4nL53Im2pK6tV056kmOLtovf0WPDu8t0yU-vg9uvjfWIdasyKeXQ2zF7pzrYL5guzPzNbVxNAfCN8LASj5ktoYMdmgaxubqaSYTXtXZqDVtYtywkBr7QMkDG3rng4li8aOquDGBW3yFBpqcNeB_Sw6YYInbuyfE8K9grxwk3rz7SmX_Z8muxRZnnCIRklVLyadl_A_APJklYm4gspwlbHGVLzWDXD1orJwhDNBWqu34Gy6Z1H1ltH4MLOSej50oMs6QbYwywf9uGbrkso-ZfRZKrwPysUBkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پزشکیان از آیت‌الله نوری همدانی عیادت کرد
@Farsna</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/farsna/467015" target="_blank">📅 12:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467014">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رسمی هلدینگ تاپیکو</strong></div>
<div class="tg-text">🎥
ببینید
👇
👇
روایت مجمع تاپیکو؛ گزارش عملکرد سال  ۱۴۰۴
🔸
تاپیکو در سال گذشته به‌رغم دو جنگ و یک ناآرامی عملکرد درخشانی از خود به‌جا گذاشت.
🔸
اینک تاپیکو ۱۰ درصد صنعت پالایش کشور و ۱۰ درصد صنعت پتروشیمی کشور را در اختیار دارد و جزو ۸ شرکت برتر بازار سرمایه ایران است.
🔶
روح‌الله شهیدی پور مدیرعامل در بخش اول به دستاوردهای تاپیکو در سال ۱۴۰۴ اشاره‌ می‌کند.
@tappico1381</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/467014" target="_blank">📅 12:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467013">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7i4DMadLdva8MjxGutmb5xYhQYlXdbdcXiYut_0xyhfXr85nxpvK9sJWdJADogiEnYR1-rZ6Lnf0uFmLcFOuLZZVF3oIEgSziPzbrV6iWCPUy-rNG3FnUrXhPlIPpW93hWwtLyxbfPNpU0i5mcMZaB4YmoL87xj1hD2W28d_LWp36gAbvnJXyPmSdGDTubJ7_1kv_wPqx0SKosBbn1rLXGZQ7xVAb-Gd3pTxe_G455bOUXIARs4SCm4MNOUaVUvN-fbFec40nbpbYuZm7NhFmkckb0BJX-HDo08_A1N2RMazjiUTYFD8ruhHQPC-gCLpivxlCbInglYfWdOqsVuOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یار دبستانی اُپارک شروع شد!
🎒
💦
شروع مدرسه رو با یه خاطره هیجان‌انگیز برای کوچولوها همراه کنید!
🥳
اُپارک به نوآموزان متولد سال‌های ۱۳۹۸، ۱۳۹۹ و ۱۴۰۰ یک بلیت هدیه می‌ده.
🎁
📅
۴ تا ۳۰ مهر
🎟️
کافیه هنگام مراجعه، کارت شناسایی معتبر کودک رو همراه داشته باشید تا بلیت هدیه‌تون رو دریافت کنید.
👇
برای مشاهده شرایط کامل و اطلاعات بیشتر، همین حالا وارد لینک زیر شوید:
🔗
لینک</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/467013" target="_blank">📅 12:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467012">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/467012" target="_blank">📅 12:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467011">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حملهٔ مسلحانه به مینی‌بوس حامل کارکنان نزاجا در زاهدان
🔹
روابط‌عمومی لشکر ۸۸ زرهی نزاجا: ساعتی قبل مینی‌بوس حامل کارکنان لشکر مستقر در سواحل مکران که برای تعویض شیفت در مسیر بودند، مورد حملهٔ مسلحانه قرار گرفت.
🔹
در این درگیری یک نفر به‌نام محمدرضا اوکاتی به‌شهادت رسید و ۳ نفر مجروح شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/467011" target="_blank">📅 12:13 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467010">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLEx04oe4a0pKCSDqFoYGVtqSxnC6isDgBLq3nHQN9Vxb7CNkGSZZc1RaIOknznuy7MYLrY5acLaAd64x1c29_3ihPSyGKUUO8vfNi7CVTZDNc1EA5z0lTI333gYVZGvYbYSGXbwNaKeVhubHSL1eEqh5COHdJT7cN_WP6Y4Z14qgaw13fPNC3wqCMvzB_0EXuJ9YZJJ9UNyqxZWDz4d30jiIWowxJyEO6r5YvvV8rCTSq5p8lehlXgdDyScrpEsQWz5KSjewxG_Ffxy3-waxNYn2V5W3vS-nV_uJ8YyE2mq_CnaVbnvjkhi4Te4IzVWvSXLXkG3DAoJV6nOJef0lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیاتی از پرونده محسن بابائیان؛ کسی که با خودرو حافظان امنیت را زیر گرفت
🔹
رسانه‌های ضدانقلاب مدعی شدند «محسن بابائیان» صرفاً به دلیل حضور در اعتراضات دی‌ماه ۱۴۰۴ به اعدام محکوم شده است؛ روایتی که تنها بخشی از ماجرا را برجسته می‌کند.
🔹
پیگیری‌های فارس نشان می‌دهد موضوع پرونده صرفاً حضور در تجمعات نبوده و بر اساس اطلاعات یک منبع آگاه، بابائیان به اقدام خشونت‌آمیز با خودروی پراید علیه مردم و نیروهای حافظ امنیت متهم شده است.
🔹
این منبع آگاه همچنین گفته است که وی در جریان رسیدگی قضایی، به ارتکاب این اقدام اعتراف کرده است.
🔹
تقلیل یک پرونده امنیتی و قضایی به «مجازات اعتراض» بدون اشاره به اتهامات مطرح‌شده، تصویری ناقص از پرونده ارائه می‌کند و برای قضاوت درباره حکم صادرشده باید مجموعه اتهامات و مستندات پرونده را مورد توجه قرار داد.
🔗
متن کامل گزارش را
اینجا
بخوانید
@Farspolitics</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/467010" target="_blank">📅 12:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467009">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f385332896.mp4?token=ZB1puJQnFOXJBOF3xmbzluxydEb8ErMqlpp9Z7PGS6MyoXMQQ3rWahAf7ekxtDUxttNYxSEPxrS_ExUrzK2koPIojWjNdm1EBn04lgzM5NXiXToOagbxRtl-G4R0u-EN8bXgeZVUi3-MDCZ6cBmuVtz8jpWrgRk-DUSwunb_z66K9VlzliUCvQ8yS677enHNdycOIxJn1S9j6H-y03ieJzpU6SakDtRsRvKZ22tky4N0nu1ph-d2mu3Eh9EmLCVUPWBlWTOfYKpc5c_k8F3nml4UIRpyy0ftL6AL-Y7yJidVEKvlsWFvREagmBaVBn36AZx0pde5DbkZvHa4jc6P2WVEaqV64sKK3hsvKZfn6Id93g0Uve6ht5DEdK8pkvnK0YsVe0Tg2GaPf500fXL4g3aHxyMMd6Dcr4CLz9gbPg0nMVNkhy993RFLaJU95m4vRNePZuPlXwrluhQhuCKF6LeIw3Kp0fCHCdcVCH9SAB-QAMOL783fVsguwp_uBa2XHJ-f8X-uz_L4oxBXsyyiuKn7t3KgHzZchnmuH5FkBhdIdGi3ZiUno_2dxgcjt3_MvYBtft5uvM_4vDADcMBT3JunsLOMk2DtvV1mkJWOq7TSPwCgNiwinxjs0cWE-8g_ubHZXH6akacWtPn5IXFpG78HTrD3-XrZFq6iCLbuqe8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f385332896.mp4?token=ZB1puJQnFOXJBOF3xmbzluxydEb8ErMqlpp9Z7PGS6MyoXMQQ3rWahAf7ekxtDUxttNYxSEPxrS_ExUrzK2koPIojWjNdm1EBn04lgzM5NXiXToOagbxRtl-G4R0u-EN8bXgeZVUi3-MDCZ6cBmuVtz8jpWrgRk-DUSwunb_z66K9VlzliUCvQ8yS677enHNdycOIxJn1S9j6H-y03ieJzpU6SakDtRsRvKZ22tky4N0nu1ph-d2mu3Eh9EmLCVUPWBlWTOfYKpc5c_k8F3nml4UIRpyy0ftL6AL-Y7yJidVEKvlsWFvREagmBaVBn36AZx0pde5DbkZvHa4jc6P2WVEaqV64sKK3hsvKZfn6Id93g0Uve6ht5DEdK8pkvnK0YsVe0Tg2GaPf500fXL4g3aHxyMMd6Dcr4CLz9gbPg0nMVNkhy993RFLaJU95m4vRNePZuPlXwrluhQhuCKF6LeIw3Kp0fCHCdcVCH9SAB-QAMOL783fVsguwp_uBa2XHJ-f8X-uz_L4oxBXsyyiuKn7t3KgHzZchnmuH5FkBhdIdGi3ZiUno_2dxgcjt3_MvYBtft5uvM_4vDADcMBT3JunsLOMk2DtvV1mkJWOq7TSPwCgNiwinxjs0cWE-8g_ubHZXH6akacWtPn5IXFpG78HTrD3-XrZFq6iCLbuqe8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروش حامیان فلسطین در قلب توکیو علیه اسرائیل
🔹
در سالروز طوفان‌الاقصی، صدها نفر از حامیان فلسطین در توکیوی ژاپن تظاهرات برپا کردند و خواهان پایان اشغالگری رژیم صهیونیستی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/467009" target="_blank">📅 11:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467008">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">حملهٔ تروریستی به خودروی پلیس در نصرت‌آباد زاهدان
🔹
ساعتی پیش یک خودروی پلیس در منطقهٔ نصرت‌آباد زاهدان هدف حملهٔ تروریستی قرار گرفت.
🔹
در جریان این حمله چند فرد مسلح به‌سمت خودروی پلیس تیراندازی کردند.
📝
اخبار تکمیلی متعاقبا اعلام خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/467008" target="_blank">📅 11:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466998">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HksqV50FhxOa8WmAz_MQiEZksDe20KP_dPjeRB7aXMG-cnTDWHwx-6kYWzmF6rlpzH_Hbbd9p2TGMNjdG7Ym7NZml4rXtHUkif-1OFOUlPBPDj3XFn1eAJzjS2CGWYo39HOnWytuIw2YKmzWJ0kUl1hVW5hj2gWMbBpPNfUgRijeYksxcaXlcCnxGa4s2SawVooSX2yRZtkfvowzPOVTITUvx-dwIdDdG2ciNMgSIUMEvZb-g-TawZVBMWmiAlOKtnxx3fAqxaib5FrnM5QJp5ZoS-2igGQZrMkZLGSzzpWCRTkZTXJ0U5f29iL9jg-srYN6NhYfdWjnGZhO_2saGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dEU70HpWH45yR278C2FtMO9d2jPEF0xY_MEkxvZvaJttHqNgyYB1rmXMPfryxKKG9D1zqTo1qryCfXqikuq1cwG0NXGRZosKbqRrDKqkYHoELbdZFB2Kyx5_Kp6uZwJe15MVejHlxXFYz8eLLVvkWyH3MzOxcG_mee30ZBfOrksgVSyaodxTKLqidHVKBsdzjxydh5BiHkymS7v1lSgS6PcgM_RmCuZLxQCTR2tgWSgKTCXJo6XumxkIpFsBgkmyo4aXZWrKdpPlqAhSFu1a6pDWrIeOJ_2LaHxp4LI2cax9gulrsyWbp1nUtxwopNMeli3W_0kbP-Q2QEUIzPSn7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MN3g3JtP_wmfdBSP7o-eQjb8PTSYZBqEB0Jj7rYNiqpDQSb9WOxWXpoSQ7FIcGTYmjRpoyGeR7SfY4UI0XLA1H_eXaF-wFCId3UKV6UtNGtWa92GOoNimWKj6RzWn2KN1aRWj55OQ7ERqjmXUVA7Bep7e0DIZRWEDcjVxtEoqwntn9Oak9-epNFaOabqavzEHoTIeBKaQMLTysF2bxCzCGMBUI1G_GPh405SaFh6agYyVyLAh-GeV4zAWFDleTXR5DyNsTadtZAhyBnRybaLcZ7W97aWhkiazD86m4CA3T05-Zi0-7qlMVg3f6Ahjook3nUYzskIXQOx8-AHe9LV4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sOU5hKtU7KCAdnwJRnYHT9KPnvqnK1snOzc3CgACFPZZgPGo6yUctW1iNGLQK_630ruS_bj3EM2ZIKC9AfH6Musovw2TrB9NnOr2joM7SMdQOc14S56Xt3uELVw_0gz_ai7Cx4WYSV4xIqrqMGk0e4ZKXHcTh6EJmLwj_D6UwPZTPZ7HJaj-RZg66fy_wCc0Wny6x5ITeYyJRux9m9KxN_AYkEskRm2w2piLJSPvdS62pXDMPiK1I07zey40zF9tBqi3tYkIvMgqDK5kl1KCWtDv6ziYY6gnZr7ZryXdse-7-pBDgSTcgb7BidsZx1XGNXJupGn1nOLulbbveIsD6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ua0-UYs8jfqyAnExrDRb0WGojzB40hhV4kseSGltSUZScIRbvt6L3XefwRCwiqdSPe8njtmS3EE5MAwTLHK15v-C5N_jG6UjVvwicRvgMEZOtbULzRVZr6sp_ZXeEp6dIuV3_geNKV_MZGrPYb7hmFsFHqwWGF0Ev1i57Hs_ucrYs2BO4YzQtIp2naOFtbfmAZ5w0_EmC-PVMGhkJARt-yBSI-GDWNly6HzvGTGphmgVj07R-rRMA0sFTyobnogtThqB1XAdVgIxWiuxBRj_r3o0hrIawkTg347lnUVpXit_xOADE16isNYaMQzcEfL8uscmWDLjtfGJa-kAuTCD5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tUEiQ_xwe_8OgdpN144q6vCeq0AjSU9tzszUEBOZQZ3LvULyfVi9wUlDIr3BTyVleUrOVk0xJa6iK_vGMaH06vBz9egY4O30cfiy7xjjTgRvQ9-IJybHQH-60aVXQo71dJTqBmXLebpTzG3bFA708-dS9N010l4cMcMKMa1PZondzbaLNBLYmiu43Lr-m1_iAu42gqeOYvnfGc0asWRErJ9ZKaL1wyg-MScJzJfecdGprVJY2MOrqU1xaxKR2vHl4wDKLd0nNLgixbfC6Qux8h_6slcOMeFCUO_jkrKb1JcgrTTtmMwN8ASZbPzJfwcDogeww9j8ZvpvfkAqDzF0XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SSSl3DFAniOjAP4wyt7n3M7AltutbDYeCfytlHJowpcrYiVPKbJgu_I-EaFpG0_XSReCKf5RkotP8bluajQbFX6p6M6SHvN3xV-uAzSR_aUj0XQUk5rASFqvYijlI7flkN1AVPjASxjyJaRajKmn-miNrj1QE1RlD9I4Yseo0TLwo-0E81bercBpSS0LF9RFjthdlyUq0SEdjiS4tVgHFKdyTXk6dlKt5Jou-JcqyEcJvuUQ0ariEtN7DFHXCtpGBhIaM0oqdNSMSTZnH2dKv1emwgMRHW9_pMFTp9Ylz19aqnyPEVpJr0XA21AkalHrIbrdCrRZegyy43-pcTI7Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qJuYGIul0L0UUsEAHfMTNDFjXKP4mX4FWnrsCvaU07WYF_OAvlbSQDVRyiqXh80G7n-nyHJR5CYExsuPTGXfVtd9uDDM-fjP5UMGZk6sH03uYq568voDz7mz_z-NWPmWAusSK0K4GCyP3bZ2NUU5VOjsVsDy2LUa0IR62eANLFG5V4KJYonbQrvgTLjJ1I432i67XcQxgiCcgku4vbG2qHALRWEy-PaMJJXSKpwr68I3oQCRYVPTpZ3bAaZ56lHBz7P8mITfPrkxX3TOBXVh9aZb7DX0EdVdeWozag7ibjf0XMt9cjifCAL-gWgL5Qn5j4vu3VXshBk9rgsdExNSdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TM9KNLyYO3vR6i-NrN0pPHQ71AFQ2H9PnxkiMM_g71aNThjr2sZ3PiZqoIg82ClkY-z-XAzlwG0_jVwCtX6hd6HAopgAF_FcOrvBLH7vpxA4TX6UaqO0cprzv8hiC2OAdDfQIy7YR5XlrrUyAGy8Sn-BEIskOwWWvyzfMgnLr2vfnPASIICJK_LwG1D4kE0m7P40o279Hu_wOIBaeJXlPqB5qNxrS6x92ZLilZudMmpx29_AAXJeZafF6rZMwQItHWpdXjcFn2Qq7iCVRPIoJGoW4xoEYjCua1ldGnbCD8E2A0EV3P70FBwXVA89eOLiQ2ljM541_Wz8l1PL_BVylw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pLhv9BJiSppHfM3_Zb1mMB8BeKKd0Gjhuy4P_cIRIKMPs_sC4ynxtoTii47SSFVErQ1146e3bm-BSdzXRJRyh_wAVe02NP_tAphFD6OX4ukiaTdJqtuzJ3IgpEsLoH0siQgA28sk-XRj5_0p99B2VJRVwKItOnTuWJ132o4pHUgxyoMAXWdCDP1Os-pKcUNP64gj1GjbuFMWwBCbUHc3iY-hwpQUOaixySjHEZBD4Jk5qU91fEl7K7Y20TKLPH723aIxBqnjmSB6AeVj9p535UbvFKzfxhWA-uGdkVKnpOg4v7E3piZBkJ9vHjOEvR-alG57bkDVdiCq7w4i2Hb2aA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خط
‌
ونشان جان‌فدایان چهارمحال‌وبختیاری برای آمریکا
🔹
رزمایش ۳۰ هزار نفری جان‌فدایان در چهارمحال‌وبختیاری برگزار شد.
عکس:
رضا کمالی‌دهکردی
@Farsna</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/466998" target="_blank">📅 11:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466997">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bABdjIxU3eYYTyAzpxGVgWsEpj-jy5EsjjjYQ9TzbhkDyx_-XWsJPEg79j8sZWvQdrm37md52pmWhZdHdv111Og-f0RVxDEOYgiTzTZeeWyP6AIUieCt_OHjOYHoDLHKqVlhlsW8ZlwWNaa4abHlZmp1fSUWU147tFckaIvmd456FAP1jmA3tyRqE0nLt1CKNDXyTZdwofxmDHtalHSCVny-ic4jsd-p6frV8YRdof6qRusaPfomU9yY1d-6Pb63IuNMkAMP6t54NLPQc7nZWE4ictiNpDQc9-2LrPh75z4jjPbqiMxVnGx0kJQ9qCZLDYsMpluEerElRbjqrT6ZgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمدهٔ اشکالات آیین‌نامه جذب هیئت علمی اصلاح شد
🔹
رئیس سازمان بسیج اساتید: عمدهٔ اشکالات آیین‌نامهٔ استخدامی اعضای هیئت علمی جدید با ابلاغ اصلاحیه برطرف شد.
🔹
برخی نکات همچنان نیازمند بررسی است که از جملهٔ آنها می‌توان به کمرنگ‌شدن نقش هیئت‌های اجرایی جذب، به‌ویژه در فرآیند تبدیل وضعیت اعضای هیئت علمی، اشاره کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/466997" target="_blank">📅 11:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466996">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b64EuSiec5Hovc4x3TrhN1HuwmDieqYaS6TO3yFIYbl8x_uo9zvzUhLEpXEHUV5APjbUFjWPkRtTO-6RaG2vm6YjvAUEDDfXEuXa2ndjER1RXdDNMxAq_TNIJR7fBQK24x4HPq6qekykpJjY__zzStgP5q80r-zQjCnSwS-LD5TNZXhVB6GdHOJYwqCi1OmKSZi2FBMyxRxcU1fnenGsFCJbgslE3XBF_uDLvv9EnrYs5XGi26VmnllXduZXdj3rOSW6ZOjCp6ilsE4oVbgnEbsdK9sJLOC4hIrynmSjRI1zNVpc1ZRz_d_tlo9dMKR-QKWCK3pHTV7Tg3w2YO3bjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عبور از هرمز به پایین‌ترین حد ۲ ماه رسید
🔹
داده‌های حمل‌ونقل نشان می‌دهد شمار کشتی‌های عبوری از تنگهٔ هرمز به پایین‌ترین سطح خود در بیش‌از ۲ ماه گذشته کاهش یافته است.
🔹
این اتفاق پس‌از آن رخ داد که حملات به نفتکش‌های عبوری از این آبراه حیاتی، هفتهٔ گذشته به بالاترین سطح خود از زمان آغاز جنگ آمریکا و اسرائیل علیه ایران رسید.
🔹
براساس داده‌های منتشرشده از سوی شرکت کپلر، تنها ۷ کشتی باری روز سه‌شنبه از این تنگه عبور کردند که کمترین شمار از ۲۳ ژوئیه (اول مرداد) تاکنون است.
🔸
گفتنی است قیمت برنت در‌حال‌حاضر به ۱۰۴ دلار در هر بشکه رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/466996" target="_blank">📅 11:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466995">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">انفجار کنترل‌شدهٔ مهمات عمل‌نکرده در سیریک
🔹
فرمانداری سیریک: به‌دلیل انهدام مهمات عمل‌نکرده در روستای سرخور طاهرویی تا ساعت ۱۲ امروز، احتمال شنیدن صدای انفجار ناشی‌از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/466995" target="_blank">📅 11:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466988">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f6NxsqSx87V-b7HUjxTBtf0_bfQlHH4ZLbGkqXadxEOq8JEfMVuBbD3NvojbtLl0XdWyuS_2SkulX821cbsCQh0TTo7K_cerFjYBCyYoyoDRkAwgOsV6NM8LKMjXU7XgeCa21pBvrUOqPp6P0neYJHXKW26PVpzyQvvcUtI6gc45kcfPN_f3rNb_0eh39m__E7Hsa8gA_-Z9TJ5lt1yK9GQskYiT0QOJRSigwqyddTbH5GwQCTWbLDqZXYH2YGBzUqznj8l4AmDEC5rnciWprNwCmjAwDjTDsQ3ug8fywoBWIwbrw7a-5IYNZkROqvx6byz1u1Hhd6VRKbpDNOCoMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WgqXCWROStlVwfP-1G3DD2v8-LxZb8dB4165UX7Nsj6E6W-HoY_gTOK7KGfxgQakoOXy0UPQm6bKxm2h38gAUtLdjvsJZF_XJ73NYuf71V2Yg1UBBwUrFDzrmv6Gik3o87KxFqg96TxipDjLqZMqRPUHclpcq5JIz5JuSJBTT3i4I87LnBR90b74bfTc6Z2T-FtWpJrT_ekirWmbn7si9drb0fz_BjMXfvpYSKdcaqIxxBM0kp2BgeeVo-56jNBm7lFvEqdP9x-mPD98nX3430OzfEgSlrPzmla9DZmOYz_ZI9Aym7G_vWhqNbMbs0_-R06mRv4qO57ByfNbL0B2IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PB0_-HmqjnauxD_zRTLn7mtTOhKEmK5udr0Nlw3F9UrY-tue5TiJ6qGOSN-lu-ccqckbfnGBx5TdUsUsZ4lC0kK5zSPTQxRHL5zha3-sAeDsJlqN8rXH3ctp01fBBMUf39yGIPZouef7-qeamcUQTQQA_2oEm7gLUB9DFwwzDnB30Co6gcJVxaxaWJw0qjzzJcJ-MvEXiE_VClCt2RsPCsg8V-f2YbrIH-1vTXbNGZf2ubvrlnOeYAM35FW3qjX9QwN3bRUl2K-9P_lqf7pyxMPW3b1MuO8l39pEHrOlCZAMLWdx15sR9zfQ7oOJ2TgHiIZIxfmwE0G0iHwc_GMTgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l0YSck7kHqYVrwOJHwyaTpGnx6z73w8m_2LB_cHhNIem-sKlr6gnggbD3CYBBoSB41-ujnb6zK2eX8a5zd4WxytSZP6yCdxHAnbt2NlLtDDgDwReQuDoThTFqayrEsf_Erg8Rt9fbO9SnYxAIQbuZyQrrD7k9W2u7ENAi6MChd99rcZZGMNgzA5xH4v-LFmR3R6fqzTX4dVz3w-1vzSlfq9Wdhg9oRZgW21vMTwJTtXZaLEvTX4V76z_DrKkhwUTsK34F-lShCYTeDike6VuIGkBMlbiF7l57TWRFVQHe4JAPNiXZxWlML_N-KFQdy66JQYbtvW-aVf03-MRDmWgyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sz-ffJRlW7PGIh4N05YFHnbOrKbU6NF_nlCFackcDs1rPT-FCUDOGVxtzbdj4dHrLSgjxBkG_gt0gPbQgMvlIf_945eCA5n9ehOi4kybaI3Cq2yxAWrBPU3VnOJQRvgHRMU0CdJzgHVcFXlTHDUpvzgy5ujli8_XTwPXoB5_VCtZD_CYa8_u1VbY59QaK4kZMDP-g3L2XlKjlewfhJ1ZRhVYo31k1lmo0pF7mcg_REVom5xMtEjcwX618X9pBnqZZHjanxY0C-vb1hIDJz4zVdOoJmUGNZS3RqmFo9SaEAZ7xIbFB_20ms9mcRl7i4bqgE4ruLxQwdB6M3dtFUpXsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ez9QiCmrwMYCo-j0WE9ZZOQJsszmKNuxkhxQo1ZZEs36oI9dNnjT2Fe6uzWOLDezmswPELq4LfzEJTKo-KPbp5IXJlAeLts6mgpgv_Iyx_BcLyJm2qYD951tJ6ul8zdq-6nLOOzMiv43wU2EQ8le1RCaKkUM4VX_xzSIORWhwKs5q7he38YPDP2ssqcN53bpK0OevPSSungsxsIpg6fqA0aVX60MwrK-IwCq4rEOtpUsgENF61HRpNqSm40cIgvRbASAoiR4gj1giJJnccZaYr5kW8KNU_92bkiw1_sluFjF3yW05RazaoRh10wiKL1RK5u_8fqZXdDYcaiUyg0vMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ks2MZaDoOjrOgzVmzvbm2UhxeQwIXnsT2jvhJztx4A4as0C6zunGzZiWfCLFC2wNEC4DfkfGHacqI_acxWRUT5Gx6zUXXmrwk4G0pt_QEkTnTgNVnejp_riaQcGC-OG2RpsoTtmNpoqUYuFRXV92TCYX4Z6bVAefTcXn9atDqBw6STj-y8mXbgu6Ibs1Rk7lLIlksiEO1xE6Jrb3la1wBpNSZ7APXHZOLigJojuJGd2bcGQzXjiwiwzB2lvWVKZYLaJ4nr1MdiE7gGq0gYAuU0yAKXCGslbflMRIt8uWvixej_KLDAcGoA5qMpZwkOK2AEZ_2nDGFDr4jRdkw-aFpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پرواز بادبادک‌ها در آسمان خلیج فارس
عکس:
احمدرضا مجیدی
@Farsna</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/466988" target="_blank">📅 11:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466987">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LS76ksDWC-_mivSvtQrB2uX_YhkZB6bXUOtPPNDEi7WjdnaJUTb5aKZJUQ7Ff-Fap6QrV5subVeIsfIQli6r0MykgzlfLkGptnp4fu3CYIVGO-WQ8ZPdIzGse-T8IyeVYUygipBmBKKBZAGWhLBSXzbn8h1S_nek4_J4_-UkxPp39pGAH5bovRDD2cix8CnuZsbufFrDm7SdiycR7AZUezplthxd_ipMPWYPNgaaGloKQxH7qBdv0lrANIW_PfK9xkswVeDAkanSq22crtsY3zkcW3QNH8tWYiP0-0w5rmBET3f_vUkWI7OxXQatlx4ZSubCznVC8a6tOqpjgP_3CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احضار ۲ عضو هیئت‌رئیسهٔ فدراسیون فوتبال به کمیتهٔ اخلاق
🔹
علی خطیر و حجت کریمی، ۲ عضو هیئت‌رئیسه فدراسیون فوتبال، که دوشنبهٔ این هفته در یک برنامهٔ تلویزیونی اظهارات غیرمسئولانه‌ای داشتند به کمیتهٔ اخلاق احضار شده‌اند.
🔹
این ۲ مسئول دوشنبه علیه یکدیگر اتهام‌زنی و حتی محتویات جلسات خصوصی فدراسیون را هم عنوان کرده بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/466987" target="_blank">📅 10:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466986">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
منابع خبری از شنیده‌شدن صدای چند انفجار در پایتخت عربستان و توقف پروازهای فرودگاه ریاض خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/466986" target="_blank">📅 10:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466985">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nqtja2YPOkxt3Evr4pbpgCeSN6MnkBlwXcaeVNaZrmX6qqoCLHIBZ2RTC6mhVLptw7aG4Xei2RLRWnU6aDu-iyOXIukrqCTINBwhlpzISMl5wRnwfmva_MgESu5q2mUr1hVuDVT6ZfUE5v9pQ1nCwvf3qj6XE-ijeZ4p2HnTrUDodvX6asaLd8jmoNxP0sPbYTUJjIUdyfU3dLDaJlJUnk2loc2k8D3y5Fd8paKToQsUtC1vSyUbKm2AiMokXh5CiPv1ORaJm3fKtAyz8c8GyxpzDPYkh65iAJgz8SXANi_u5GJEJ8_gx2OfQvDYCFASFq5uWyGk79sIUHpG3lHleQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست مقامات عالی‌رتبهٔ کشورهای ساحلی خزر در ترکمنستان با حضور ایران
🔹
گروه کاری مقامات عالی‌رتبه کشورهای ساحلی دریای خزر، با حضور نمایندگان ویژهٔ این کشورها در امور خزر از جمله معاون وزیر خارجهٔ ایران در شهر آوازهٔ ترکمنستان برگزار شد.
🔹
در این نشست، آخرین تحولات و ابعاد مختلف پدیدهٔ کاهش سطح آب دریای خزر و پیامدهای آن مورد بررسی قرار گرفت و بر ضرورت تقویت همکاری‌های ۵ جانبه برای شناسایی دلایل این معضل و مقابله با آثار و تبعات آن تأکید شد.
🔹
یکی از مهم‌ترین موضوعات مورد بررسی در این نشست، پیشنهاد تشکیل کمیسیون کشورهای ساحلی خزر برای بررسی مسائل مرتبط با کاهش سطح آب دریای خزر بود که با حضور مقامات عالی‌رتبهٔ کشورهای ساحلی تشکیل خواهد شد و بررسی مستمر ابعاد و پیامدهای کاهش سطح آب خزر و مقابله با آن را در دستورکار خود قرار خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/466985" target="_blank">📅 10:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466984">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">حملهٔ تروریستی به خودروی پلیس در نصرت‌آباد زاهدان
🔹
ساعتی پیش یک خودروی پلیس در منطقهٔ نصرت‌آباد زاهدان هدف حملهٔ تروریستی قرار گرفت.
🔹
در جریان این حمله چند فرد مسلح به‌سمت خودروی پلیس تیراندازی کردند.
📝
اخبار تکمیلی متعاقبا اعلام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/466984" target="_blank">📅 10:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466983">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDAQvJiGmsY7CvipZyGndfLx9_qP9KykHzHaXFWTdExLzbf1DkElJJ4NWJVWXtXaP4OAzhy7zK7_zzDOoLYky1v4bTiruFt5foL-JK06SC3dvrdrCTeYtLAZbNZWdPD2kHLf-WVJ9RQ1JqJTJ6Jir2Y5FPkRLYTmVZx1Q_CGhVFTGiQs3DOOA7hV8JcytJ2Cb1JKx5odle-DtlX98fM7AsDZGR9KUxy9qxjI7V5B0WdekrX7nsfInDyr_o4jO_axZzveCxJRfLKdTs31PQ6LG70B_K7aFvR4fTbOQtLZen8hluWyCTU64gw_JguFINNoj5QN_MGEAUN4tRXzAxRkGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دمشق: در کنار عربستانیم اما نیرو نمی‌فرستیم
🔹
پس از آنکه اکسیوس، طرح ریاض و دمشق برای اعزام هزاران نظامی سوری به یمن را فاش کرد، مشاور رسانه‌ای ابومحمد الجولانی با رد این ادعا گفت که سوریه در کنار عربستان می‌ایستد، اما خبر اعزام نیروهای سوری به یمن صحت ندارد.
🔹
«احمد موفق زیدان» طی پستی در «ایکس» (توییتر سابق) نوشت: «امنیت پادشاهی عربستان سعودی و منطقه خلیج [فارس] از امنیت سوریه جدا نیست. ما در دمشق در کنار برادران خود در سرزمین حرمین شریفین، محکم و قاطعانه ایستاده‌ایم؛ با این حال، ادعاهای مطرح‌شده توسط برخی رسانه‌ها درباره درخواست پادشاهی برای اعزام نیروهای سوری به عربستان سعودی یا یمن، نادرست و بی‌اساس است. خداوند پادشاهی را از شر بدخواهان حفظ کند».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/466983" target="_blank">📅 10:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466982">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fk0zzKuM4__eaQvMpP34UtjUFaG9MtR4fha5aS8EfouYBDeFrIPTWkJ-pDxJWX0nvw20acxoo3ldRjgKCcH1wAAkyipBnnvd6VTdZrc05cO3FoAjLOxcCDBOvCz8kCojMNC7PkXj6cgi8_mewvu7m_74NRvsuTs9gBchKBJxrbN3c__vshrxY-WXoaFyj2hM0kOwB9WtNQEoZVK7D90gWWWAJOpU0LiMQ6DkTDc1jjk-V6eCqLgoNBeT-TMIb4E-nq9Pd8ownLq5dmLkkYxfnmTZkPi00AfvvjN-Y253xk4vzOXTcUAe4PwdIO2ITHu3vjpbi9tPTdntyQ0dcF7Q4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ام‌دی‌ها به آسمان ایران برمی‌گردند
🔹
سازمان هواپیمایی کشوری با بررسی شرایط فنی، مجوز ادامه پرواز هواپیماهای خانواده MD را با رعایت الزامات و دستورالعمل‌های صلاحیت پروازی صادر کرد.
🔹
براساس نامهٔ مدیرکل دفتر صلاحیت پرواز، موتورهای JT8D-200 که تا ۳۱ شهریور از مراکز تعمیراتی داخلی ترخیص شده‌اند، در صورت رعایت الزامات فنی می‌توانند به فعالیت خود ادامه دهند.
🔸
این تصمیم در شرایطی گرفته شده که ممنوعیت پرواز برخی هواپیماهای MD باعث کاهش ظرفیت پروازی و نگرانی درباره افزایش قیمت بلیت و فشار مالی بر ایرلاین‌ها شده بود.
🔸
با این حال، سازمان هواپیمایی پیشنهاد کرده تا زمان تعیین تکلیف امریه صلاحیت پروازی سال ۲۰۲۱، ورود هواپیماهای MD-80 جدید به کشور همچنان ممنوع باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/466982" target="_blank">📅 10:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466981">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZiAzA6XdaDrQojhjK9vxhsgAbrDiIV2Pb42njtw817lEeTXnNtKYC5qkZ_MrXR_CDZ2i207qScYx3JQI9Kr95b2ntnjLIU5T8TmOJFxaElVakGPz4xlyE_ODffpQp3lBlDjFaOTbUkTHEzTyH4N1ZhrhuOOaVOfHqLZgKYbIxpB0zyc4cJPmPveqGBFzMQNJBRlQNqlw6DQSCfAzEcYcM1azGDhbqP6bxb9jzCCgKB83i1CD0kf4I9HIeo8jiqzZFte_wDvxLkYWZIBDmpSiCxKtXadJ34WlIV_PmfLa-wuQCZJqVdDe-duRjirDxJa0WQGD-w4SACAwbCjZlSP5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط ۳۷ درصد اسرائیلی‌ها خود را پیروز جنگ غزه می‌دانند
🔹
درحالی‌که نتانیاهو خود را پیروز نسل‌کشی غزه می‌داند، تازه‌ترین نظرسنجی در اراضی اشغالی نشان می‌دهد تنها ۳۷ درصد اسرائیلی‌ها معتقدند رژیم صهیونیستی در جنگ غزه پیروز شده است.
🔹
درحالی‌که ۶۳ درصد بر این باورند که احتمال وقوع مجدد حمله‌ای مشابه عملیات ۷ اکتبر (طوفان‌الاقصی) وجود دارد.
🔹
این نظرسنجی با مشارکت ۱۰۱۳ نفر  با میزان خطای ۲.۵ درصدی انجام و نتایج آن از طریق شبکهٔ ۱۳ تلویزیون اسرائیل منتشر شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/466981" target="_blank">📅 10:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466980">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">صدای انفجار در بندرعباس مربوط به امحای مهمات است
🔹
استانداری هرمزگان: انهدام مهمات عمل‌نکردهٔ دشمن در بندرعباس امروز انجام می‌شود؛ صدای انفجار دقایقی قبل در بندرعباس نیز ناشی از همین عملیات است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/466980" target="_blank">📅 09:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466979">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a0424389.mp4?token=bGZR-ZIKObf34z0XYJ8vl-INWAIaGHzm4XE30P7azUOvdMWRS-ASy9kdV_wifUjBmDVsh2OEIoHx_-yj4glhyMg5n7rU1IzkH-TunqrRyDImZ73DAI1R9qGnhw6QYIOSmHIw64jz6ywCmELWiFavqknb0GCag2L9gqUbs-_tIavVssGGP116KVV7POmld9spJvQMsnBM436u-wziymo9g67JmFhCSK0GE_xoIqn_xpee7lAdRo2GkzmnnwxsVQRaLczGM7JHH9lkVZwI-MpRl3c69aXreCWFBwTpOSZk-baEGA4LzWOq37tv2M1mCCoURqVnI8ibXh9kyqj11S4bDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a0424389.mp4?token=bGZR-ZIKObf34z0XYJ8vl-INWAIaGHzm4XE30P7azUOvdMWRS-ASy9kdV_wifUjBmDVsh2OEIoHx_-yj4glhyMg5n7rU1IzkH-TunqrRyDImZ73DAI1R9qGnhw6QYIOSmHIw64jz6ywCmELWiFavqknb0GCag2L9gqUbs-_tIavVssGGP116KVV7POmld9spJvQMsnBM436u-wziymo9g67JmFhCSK0GE_xoIqn_xpee7lAdRo2GkzmnnwxsVQRaLczGM7JHH9lkVZwI-MpRl3c69aXreCWFBwTpOSZk-baEGA4LzWOq37tv2M1mCCoURqVnI8ibXh9kyqj11S4bDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
النجار، تحلیل
‌
گر سیاسی: موازنهٔ قدرت به‌نفع ایران است
🔹
آمریکا با تمام عظمتش، اسرائیل، اروپا و همهٔ کشورهای حاشیهٔ خلیج فارس با همهٔ ثروت و اموالشان، قادر نیستند تنگهٔ هرمز را باز کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/466979" target="_blank">📅 09:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466978">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cY13EbzDW-XQ4QIGbRK_42tCYvl1wS6wvc8azKDGpKRNVsiTAmOSyphuWWbtI2pbt8e6Iw6ztGT9OLGTM7rw0mZDAFAxN3eCLBZOm8JSbpUggfmU4q09QBGiYFnhKpZ6pXcyNUeWNxD3SihOtctIElq2S8tlIZSBtqjXNYooJ6elZkdBBhZ6MPj1sxuFaWlJC8Hrb1Y2nRrI91ePGYHcHrnSpuFPELnH1jQE9wjgA75QGPKzVXU1mH7pzlNs6MmOTDAztnqwLV6gzyRLiMrw3kLYCDPOvHr4hxJxLfT7XsAvAOPFdr3AXiaNchYunsuRr8DaAvtTCYQKxNYszavc-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عراقچی خطاب به سنتکام: نمی‌توانید مردم را برای همیشه فریب دهید
🔹
واکنش وزیر خارجه به پنهان‌کاری سنتکام از خسارات وارد آمده به ارتش امریکا: در ماه می، سرویس پژوهشی کنگرهٔ آمریکا اذعان کرد که نیروهای مسلح ایران ۴۲ فروند از هواپیماهای نظامی آمریکا را از چرخه خارج کرده‌اند. اکنون این رقم به ۸۱ فروند رسیده است. تعداد واقعی به‌مراتب بیشتر است.
🔹
مدرک؟ سنتکام اجازه نمی‌دهد حتی یک سناتور کنگره از پایگاه‌هایی که مدعی است وضعیتشان کاملاً عادی است، بازدید و آن‌ها را بررسی کند.
🔹
نمی‌توانید مردم را برای همیشه فریب دهید.
@Farsna</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/466978" target="_blank">📅 09:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466976">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشکده خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWOsejSyhQjFaI94HMhAz6v0po4jxemYIxKI109sbapHCLLM_xPtS1s2VPiSkes_k6wfeKKXVUDjx03c-ASWGnMuoD2-nMmMneM0UY5D1bbfv3cQvnFOpSjwZrbd70lXY2WzDsqLjX6L0Dh1SU9T5SuWz4qcnFbfjRlH2SNKeFzVvx3gdHHEjAlcDLEx3c-9ddORYWL3pVCPrWW8LdIIJHl9Jn66asQAK5J8M6aXsLr8vXoLwo0-zysl0EmovNjoIKnGm4g_Rai3xPn62Oq7at22n6xWoEIoliHqAXRRk53kb4UfeUaG3pvzQK44TOsV_lR0WRzUZYvODKQWMftpnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔰
مهلت ثبت‌نام و انتخاب رشته در پذیرش دوره های کاردانی و کارشناسی ناپیوسته دانشکده خبرگزاری فارس تا ۱۵ مهرماه تمدید شد.
🏷
براساس اعلام سازمان سنجش آموزش کشور، مهلت ثبت‌نام و انتخاب رشته در پذیرش دوره کاردانی و کارشناسی ناپیوسته دانشگاه جامع علمی کاربردی
از امروز تا۱۵ مهرماه تمدید شد.
📚
رشته‌های تحصیلی:
🎙
خبرنگاری
📸
عکاسی خبری
🎞
سینما‑تدوین فیلم
🤝
روابط‌عمومی
🎤
گویندگی و دوبله
ارسال  عدد ۱۴ را به شماره ۵۰۰۰۱۰۱۴
🌐
لینک سایت ثبت‌نام
🔗
futurix.ir/go/rxDxXO
☄️
☄️
این فرصت رو از دست ندهید
🎓
مرکز آموزش علمی کاربردی خبرگزاری فارس
🎓</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/farsna/466976" target="_blank">📅 09:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466975">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNcyUXBDty-DinLZYs90clVtC3WizbXF62Dttz7oiJ-Di8yeciIVl3EptppRuiRwrlqUO4P5V1GOMimAhMn9jfWCD-KS1iyhSzb2JBXKJXSV8S6X1qdXKqnqhvDubOY979VKmETE9wLrYFQfxW_hW9rlbe5yeDWU74VuUKbombZWUGdMDVLtpdlM0H71RXjZnxom02sHu6rQ3pgCjA-uP1Xnomzps325JtADLOb-ZkvCcG-hgfpRKYK1VLQ8DfJWdaiSSpVX2trF88zP8g8EGLjX97gVJS1dg2cnX5vFlO8btmorC-adYNv4IIR_gMf0sO2oEtnfMZ2lFxax0oWGtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندار کالیفرنیا: ترامپ دیوانه و خطرناک است
🔹
فرماندار کالیفرنیا در واکنش به اظهارات اخیر دونالد ترامپ، او را «دیوانه و خطرناک» خواند و گفت رئیس‌جمهور پس از فرستادن گارد ملی و تفنگداران دریایی برای اشغال کالیفرنیا، اکنون خواستار هدف قرار گرفتن لس‌آنجلس و…</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/466975" target="_blank">📅 09:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466974">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76d1b4d0d.mp4?token=jfqHGOh3UmXAaG2dtXQF_596Fnhv9aZs1rIiRPVJIGBOoDbjOyysXoEMgjJz0dmXLJf8lW9JTOdMcRm0ZySlyUzevOtqq7Ed5vFtvlgmAbcdThCnnY2mUEHP33FKu20B_Ff96oSCr83NYRqeMXEIT01jsQNyySOKlCsXDRvsJQdt1E0KpjEFl9QzmMXAfSpMUT2WQYBLHFb8lmVuxZFXfQ9yHRYeEbHpVTykcJsP4W9HhNtvxc5MBFtEVY_H6nfCLs7u5wCKd8hjKMfK6KSM3MS6cCb3focFEvntN5ISeAj9939RVGyEDIR3cI5I9Mjjeb45psg4ehoz2WOxvJ_JWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76d1b4d0d.mp4?token=jfqHGOh3UmXAaG2dtXQF_596Fnhv9aZs1rIiRPVJIGBOoDbjOyysXoEMgjJz0dmXLJf8lW9JTOdMcRm0ZySlyUzevOtqq7Ed5vFtvlgmAbcdThCnnY2mUEHP33FKu20B_Ff96oSCr83NYRqeMXEIT01jsQNyySOKlCsXDRvsJQdt1E0KpjEFl9QzmMXAfSpMUT2WQYBLHFb8lmVuxZFXfQ9yHRYeEbHpVTykcJsP4W9HhNtvxc5MBFtEVY_H6nfCLs7u5wCKd8hjKMfK6KSM3MS6cCb3focFEvntN5ISeAj9939RVGyEDIR3cI5I9Mjjeb45psg4ehoz2WOxvJ_JWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: بارندگی‌ها تا شنبه در برخی نقاط شمالی کشور همچنان ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/466974" target="_blank">📅 08:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466973">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHwHge1jD9Dmq9JP1ns3hnIWUnxgruDBhSwzDZWe1C5j81s-6My9Ypox-U_D4g-lwMNen2hBeDZMdsbCrsQgHaQPBL8xyTtMIW41iLEBJldxCQPBlgojQvyjuolt45c-c5obnFNxsmytTr5zFhIDaegNgXMWLCSTPD5O9gWmQP2ZIoOEcaqE-0u-KuSz1vHONJ5Q7M-KCXXz2RP1MaJLqr8ny9iOnLtE5BF7fUWHMii5yWaquVuJmA8ky_N68aosIGWjGXwFF99PytV-hJcc5X9JzqpJa2tTLmr_kFJKnOW34A_EF0-7K31hcYfPx4GZPIrVoxh6Rv9gDkypfutu-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت ۱۰۰ دلاری کمر اوراق آمریکا را شکست
🔹
قیمت نفت برنت با عبور از ۱۰۰ دلار، نگرانی‌ها دربارهٔ بازگشت تورم را افزایش داد و موج تازه‌ای از فروش اوراق خزانهٔ آمریکا را رقم زد.
🔹
بازده اوراق ۱۰ سالهٔ آمریکا تا ۵.۳۶۴ درصد بالا رفت و به بالاترین سطح ۲۴ سال گذشته رسید؛ بازده اوراق ۳۰ ساله نیز با ثبت ۵.۶۹۶ درصد، رکورد ۲۴ ساله زد.
🔹
افزایش قیمت نفت و نگرانی از ماندگاری تورم باعث شده سرمایه‌گذاران دربارهٔ مسیر نرخ بهرهٔ آمریکا دوباره تجدیدنظر کنند.
🔹
از سوی دیگر، ورود شرکت‌هایی مانند اسپیس‌ایکس به بازار بدهی و برنامهٔ این شرکت برای جذب حدود ۴۰ میلیارد دلار سرمایه، رقابت بر سر منابع مالی را بیشتر کرده است.
🔹
تحولات بازار اوراق درحالی ادامه دارد که تداوم ناامنی‌های منطقه‌ای و نگرانی دربارهٔ امنیت مسیرهای انتقال انرژی، به‌ویژه تنگهٔ هرمز، می‌تواند فشار بیشتری بر قیمت نفت و در نتیجه تورم آمریکا وارد کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/466973" target="_blank">📅 08:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466966">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nFs8y_Qq83Gr3OClNSEO9PyWHjkUwdu8v_nGozggwcx7yB7HpNUVKljH1F9IHB2aPBDZ16OwTssT08GUTeGS94JM-CXFBDQRe06H-jpirFnLxg7WLsOjZd674dxjxN1eaER-t10j2-uzCEOrr0tF11_yJ0LK3YkKXgBACMXiEexziNIOFAZE1PIbAGslVaCo2u6VYdjmCdI2chlatq9SnAfkXUgbctO0SxAX7xIvXCe3CJvB_QpnNkXoG9Mfoxyaqt95U3-I2MA-k2vEOMogQVGassvFJyTiHlhMtP7sv3MPmM1d2MfRidgJwZ4XgqVMVWGy5WwfY7pD6U1phZyXMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VMWyWPlePKRpYA4CmyHYVQCgzLLbT5M3r2Y6-6nYUsHTqNEOELSCJvxeh_R_2dUN9vBgUw6D3SPyV3GWaG2E2VTVJXNlqAZc7dSOz4i9uPstB-y6pM0mkoRaEMFePgynCxvJaoAVq6Lu5FomXczZokL5c96KVRNQb-ruW3cktWwkmHlJHP0yaNaMRamb7hXgim0Urpe1iQtCbLzO4tPin6Rr6efdSex5ZeYDmjE3cV3B2I68u8tQKI4waF8Q2or1dg7zbSOmW0lxXV8-MqnnWV5DBlkyqVe5XBvN3Wr9Ml0Bg5tEOlZmrBddj5Qe0vxsBJOlRSRmxYaJI7A36_4eEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mcZplas9t_NWCb_dllZ4q0VZa1KlqGJ28T6hpjJmsh5T8Z9xUxHG81HrJi_VI9IRPqrg5RfnW1OTwcccRlGjVk8o65FLE-szevxY9de2gZR9dJavt_mGWxGyrikK-aXIos_bDRjTi6kfuPYTuLCa9y5sgGaSrL3uQiyHo6cqMsn6vzp0WbRVlmRAr87pPpFgyPVto2Gm4UcLBZgByrgvppHiL4flqctBbbVXTyKF76_4HANfRi-kxScewJLytx6nud7B_1envLGjM44D-orUgyQtLh7JFimC05FwwYB2TTMcPa_Zhe7OvEPxLJdTPn4pobgiGvpBSUIL2S97CjlDvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YkLyvUAJIemwNpZTzUls3xoZNuHD3ndb7njcke9a9ehnocUkgdfTmPs6u1oJKGnUxrOrk6Suv-_mjVfwfuvaE-L3U1Eew4701ksvcTIxDdP-6o0-tFaTd8lOFYXEplpMVDkRYv1dFH9YpQggrLHnyVTCqBVv7ZWDGeAjXgK2ewqzuWESNRNVYv6pQBGm4Y0lrONJ4egxJ_1Lp71CmybhKkusdIoqP1Nz10OdmeAEk3vNaUvSYv4sG9ArG-jv0_AJOAJcwhJUIgfKyAHgoGV9siQE7etSiy0pandN0odMfvReF3eJ9Ns1JSpP1vCFb7pioxylUmA3wkZjpOCBLFfTQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qig4JB15E585cpU3FV51Ks-S5fZHY6Uo4nus-aHwwgS-oZhcLlDRQTsbWUJLIG6uIM8TycnMksrRbaW_60kUmhHUF1Lrvve_xsoGEeVmZ3WkJMJIqCsGCGTwwk0ARP6PMC_csxnaMS8X7UUSJOPfqF0HyH4VxgBE59cPwt11eyLT5b1_YQtwsRTKSJEWlvJagA8drkICa4GKx2N5EPZ03FYTtA2SgjU05M-wtioOStrct0yYN7SAFYDv6V6MDikCCXmYryDX_t5TIjucHvss1WgjL1pnk7Df5nUJqVEP8EoO0cVDpCS6fDeRCcJdcfOhqmn5dSIoQd3Bp3gfb3aMEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bKr_5WShJMJ1FeRtX6knmLBWcrK02qNeMxE_GgE6mu9IcH9kl5X5EONI0rgN-CSrhDjjqWPYtpoeb1ByB41sGx6hQROAfJBe_PsglZFr5TwFMlk1h4MNsvFhAzICgJtPJvTeeN-MQvhuC6y9ShfemKDjA690umZYoG3nkrx0rfOIktKuqvGuUrhO3Q8b41eWSBw_cwryEgS4MUJ8j0WD_ber8yf9bYsfriVwD-Z9SPTAyzjiQU_1NiiFlYW2S82Zni4q410RbL27OBVlHmJevsU9GKl_foqwK8ScdqpuEPdiX543M5JFJvBexGT3i1ikMs8bj03AnK1G9iFqFSp4XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FHZ_sp8DQ2GpmmCKgzTDtErH4B_OV59vNLkQDM_DiXlB_Mn-vxwiyx6TOmQfg9IPDEjaTqXW7TxpayzThan6MhaN3uQDMY5fQV4kBvGMYqA8PorknOiHVzWEprgJQqyjyu0wA76-as5mcrgXj3wHi15mfeIxmnuzsN_2nRu8l3W8U9io6INCc9xxAdmF9xbdJOqERmlPlclGIYxC0-80GI9SUAzzuJr54Akz260_5n0U43R8Rghb3hCEIbXMu7cNZNyhvyEH8uVmNa75BNeHjqi0CrLhOU1zw6yLtuph5DClEva0DnrYii8HPNjcgZO3-oWcYBSPcKMsKFoEvW4lFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مزرعهٔ پرورش کروکودیل در ملایر
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/466966" target="_blank">📅 08:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466965">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16d416136e.mp4?token=FctqSbUCx0tJPBTKB67fTVH4lWMcAIA1b0uJtsyYYohSvGbrDtmiWa5fSGVA9OXPcR2q1hJL7hPYRkKvSR7S5mbzicVd0l-qVtR0hujLAsGfVrLwQeOeTCBeApFG_JNB31O4c4emKjPdoLj07_BEH1V0HmHYLWm9beBScPjp6lKSu3-jMRrdni077zcj83WXQbMSlXWN9csCki6JTaGyjzwNVKOd3T6qt3N-npXVx3NO9uC2o37gkdvUV7DIEfVZnm55aZl7JGnlaTK7z-dIrsPY5QYxQvadxSwwgCn6D_FDhP2JP2S2UnPzAhVXjVm1hUVFXxHQ5CBAIsoz30-t8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16d416136e.mp4?token=FctqSbUCx0tJPBTKB67fTVH4lWMcAIA1b0uJtsyYYohSvGbrDtmiWa5fSGVA9OXPcR2q1hJL7hPYRkKvSR7S5mbzicVd0l-qVtR0hujLAsGfVrLwQeOeTCBeApFG_JNB31O4c4emKjPdoLj07_BEH1V0HmHYLWm9beBScPjp6lKSu3-jMRrdni077zcj83WXQbMSlXWN9csCki6JTaGyjzwNVKOd3T6qt3N-npXVx3NO9uC2o37gkdvUV7DIEfVZnm55aZl7JGnlaTK7z-dIrsPY5QYxQvadxSwwgCn6D_FDhP2JP2S2UnPzAhVXjVm1hUVFXxHQ5CBAIsoz30-t8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورزش‌نکردن مثل سیگار کشیدن است!
@Farsna</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/466965" target="_blank">📅 08:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466964">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پرواز نجف-تهران به زمین نشست
🔹
نخستین پرواز بین‌المللی پس از دوران جنگ چهل روزه، صبح امروز از مبدأ نجف در فرودگاه بین‌المللی امام خمینی(ره) تهران به زمین نشست.
🔹
این پرواز به‌صورت رفت و برگشت خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/466964" target="_blank">📅 07:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466963">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: فرودگاه ملک خالد در رياض را با یک فروند موشک بالستیک هدف قرار دادیم.   @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/466963" target="_blank">📅 07:38 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466962">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vntNpJcUEbtcGLnfMclMUTKy8-uTQy9a01jbUYkvT_ZVKBhhpfemMOk8lysG__5mSgUf-gYyX30dLBYv4c2HiLrffIiCsEkknkajcxtI70gJ-9im_28bPbd38CAs3XsoiFeWnN5Mj8k33tmGUkw_b_9z9KcMEKtWDwiKL3sXLpL5_eko47REIHjU4GqRTMcICGQm1kWTAYnUwTz8yiL2d-WESveajCVayOhkM7bskIdthezQAigCS_M8AKcXSJOXirW3D9KKFuA4OXDXAf72Am3b7Bjoc0ZoZ-dNnk4PmHE0Yb1yaLQEvMjFr661PXicmZMSoN2GHhCwqmsYHWknbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار یک نفتکش در نزدیکی قطر
🔹
سازمان تجارت دریایی انگلیس: یک نفتکش در نزدیکی قطر هدف چند اصابت قرار گرفته است. @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/466962" target="_blank">📅 07:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466961">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">هوای تهران در مرز آلودگی است
🔹
شاخص امروز کیفیت هوای پایتخت با رسیدن به عدد ۹۶ در محدودۀ «قابل‌قبول»، اما در مرز وضعیت آلودگی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/466961" target="_blank">📅 07:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466960">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoTkKaPXrgqoFdf7RPNXnCz4lWxOAy7QTVxCtek3PgUezjv-4ChUIAeoCDaRFG5ZaF5fsXP2CZvDqwZFKXg13tUc-7PyItrkH8FczJHnf3rAh0fCkPN1m4kjDSACLCDEAugfQ7AAnFMFC3FdbuaNNT9vhggJBf3nk383l58dcaYKo4zpNcsqBg6t64FFO6yV4fdGNUxhbw_dAF7nXL_FvVfBiBNyQDKJvn6XTTDGBDeJObrd59wzZTVWET6_OKec4J6mVzK5ykfvzhwpetTkwCiLxjrJQoc6k58HaNIpfn_C2kd-MztsSlPwFMAX2bh9LaaE-UqGTyLV7nu9LTN5RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگزاری انتخابات میان‌دورهٔ آمریکا بدون ناظران اروپایی
🔹
برای اولین‌بار در ۲۴ سال اخیر، یک انتخابات فدرال در آمریکا بدون حضور ناظران سازمان امنیت و همکاری اروپا برگزار خواهد شد.
🔹
دولت آمریکا به ریاست دونالد ترامپ تروریست، از دعوت ناظران سازمان امنیت و همکاری اروپا برای نظارت بر انتخابات میان‌دوره‌ای ۲۰۲۶ خودداری کرده است.
🔸
سازمان امنیت و همکاری اروپا از سال ۲۰۰۲ بر تمام انتخابات فدرال در آمریکا نظارت داشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/466960" target="_blank">📅 07:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466958">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سخنگوی نیروهای مسلح یمن: با موشک‌های بالستیک تجمع مزدوران سعودی را در پادگانی در منطقهٔ «رأس العاره» هدف قرار دادیم.   @Farsna</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/466958" target="_blank">📅 06:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466957">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">معاون سیاسی نیروی دریایی سپاه: بازار نفت هم دروغ‌گویی ترامپ را فهمیده است
🔹
علی محمدی، معاون سیاسی نیروی دریایی سپاه در واکنش به ادعای آمریکا دربارهٔ عبور نفت و کشتی‌ها از تنگهٔ هرمز گفت: اگر واقعاً نفت و کشتی از تنگهٔ هرمز عبور می‌کنند، چرا بازار نفت متناسب با این ادعا واکنش نشان نمی‌دهد؟ چون بازار هم می‌فهمد شما دروغ می‌گویید.
🔹
اگر نیروی دریایی سپاه را نابود کرده‌اید، چرا در فاصلهٔ ۶۰۰ تا ۷۰۰ کیلومتری قرار گرفته‌اید و به تنگهٔ هرمز نزدیک نمی‌شوید؟
🔹
نیروی دریایی سپاه بر تردد شناورها در خلیج فارس، تنگهٔ هرمز و دریای عمان اشراف کامل دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/466957" target="_blank">📅 06:43 · 16 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
