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
<img src="https://cdn4.telesco.pe/file/oY6b9zbiSkKI7AQwSRFxYk2EnNX6LvnzNADCgDKX3r-fOCfbDoTb7vO5GCz3PNpt4DxVXzq4okc91nlozY1ZdMb2GpwAbzsnOww2PlqzA8qxRUDAvsEGL7Z32Y9VHNPYymLFDdjBCvbD-KWzXU6hRGb9TzWi_ZeMkro_pbUzbbCOYnwU-L3RrRMNfW98InSH_GDgJFDfkCBnh84zW_Ep4qBBxSwd8XJ9mJEAiLKVO-FhmOWrxdu695vqbErkerYvKHxao0RyNo27JqrC5jocAAsnJQqkjCaxutkIe1eGLioLdBgyLMiKapf_opp6hHWm-bDRptXaPLT0737Kp5v_lA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 451K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 07:40:32</div>
<hr>

<div class="tg-post" id="msg-23338">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مدیریت اتاق جنگ : گزارشهای زیاد شما دایرکت و منفجر کرده که تهران صداهای عجیب می‌آید، گزارش پدافند، صدای جنگنده و غیره. بررسیهای من نشان میدهد که این گزارشات در حد «باد و بود» است فعلاً و به مرحله«زارتان زورتان» نرسیده‌ایم. با تشکر از توجه شما به این مطلب.
@WarRoom
😁</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/withyashar/23338" target="_blank">📅 03:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23337">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">حقیقت‌یاب اتاق جنگ:
ویدئوی منتشرشده از
دیوید کیس، سخنگوی سابق نتانیاهو
قدیمی است و مربوط به
ژوئن ۲۰۲۵
است. کیس در این ویدئو مدعی شده بود جمهوری اسلامی «ظرف چند هفته» سقوط خواهد کرد و حتی زمان آن را
دقیقاً دو هفته، سه روز، شش ساعت و چهارده دقیقه
اعلام کرده بود. این ویدئو امروز بدون اشاره به تاریخ اصلی، مجدداً در برخی رسانه‌های زرد منتشر شده و به‌عنوان اظهارنظری جدید درباره تحولات جاری ایران بازنشر شده است؛ در حالی که اصل ویدئو مربوط به بیش از یک سال پیش است.
@WarRoom
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/withyashar/23337" target="_blank">📅 03:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23336">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نیویورک‌تایمز:
نهادهای اطلاعاتی آمریکا درباره احتمال
دسترسی چین به فناوری‌های حساس جنگنده F-35 از طریق عربستان سعودی
هشدار داده‌اند. طبق گزارش، یک ارزیابی آژانس اطلاعات دفاعی پنتاگون درباره توان ریاض برای حفاظت از فناوری‌های F-35 ابراز نگرانی کرده و به
دسترسی چین به تأسیسات سعودی و استفاده عربستان از تجهیزات مخابراتی چینی
اشاره کرده است. این نگرانی‌ها در حالی مطرح شده که دولت ترامپ در حال پیشبرد فروش
۴۸ فروند F-35 به ارزش حدود ۲۴ میلیارد دلار
به عربستان است. نگرانی مشابهی پیش‌تر درباره فروش F-35 به امارات و روابط رو به گسترش ابوظبی با چین باعث تأخیر در این معامله شده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/withyashar/23336" target="_blank">📅 02:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23335">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/537de6d757.mp4?token=H81rtZBT1-K1qIwOsUFIjdtlpGMdSnOC4ZKpSwyYgtJih6K_73_xKxD0BGckbrtvkgoMLCScFCwwNakz4b0hODj-5gk1_BrEEjk3Y2FYiiOpFUALvkZiH_jILdNfPyvXELdMenHCIE9b26Vyi38edNGKhZPSy87pQWhIIjmZu0L2S3Iqnu93rOxuliAGdSiBOiENl3dRIJ8X7t81rruMFLu_UZ0mSoyksqlWtbLFuUw-qaPphlpc-OERlMnnPpFT0RhWtCjTargMY2IO_HLJLp23WIT0SV3x2Ia3ZR67LAYPi2B12mQnqNNr1c5BlMNdX53qT5gDcNs9YFG4YcK96w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/537de6d757.mp4?token=H81rtZBT1-K1qIwOsUFIjdtlpGMdSnOC4ZKpSwyYgtJih6K_73_xKxD0BGckbrtvkgoMLCScFCwwNakz4b0hODj-5gk1_BrEEjk3Y2FYiiOpFUALvkZiH_jILdNfPyvXELdMenHCIE9b26Vyi38edNGKhZPSy87pQWhIIjmZu0L2S3Iqnu93rOxuliAGdSiBOiENl3dRIJ8X7t81rruMFLu_UZ0mSoyksqlWtbLFuUw-qaPphlpc-OERlMnnPpFT0RhWtCjTargMY2IO_HLJLp23WIT0SV3x2Ia3ZR67LAYPi2B12mQnqNNr1c5BlMNdX53qT5gDcNs9YFG4YcK96w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
«آیا قبول دارید که آنها برای کاهش قیمت‌ها، به‌دلیل جنگ با ایران، نرخ بهره را افزایش می‌دهند؟»
ترامپ:
«نه، آنها نرخ بهره را افزایش می‌دهند تا شرایط برای ترامپ تا حد ممکن بد پیش برود. مشکل آنها این است که ما
بهترین اقتصاد تاریخ
را داریم.»
@WarRoom</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/withyashar/23335" target="_blank">📅 02:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23334">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfa149f9d4.mp4?token=lkBXGIbXx-rzUBWBBn1V9yOXDRm3MMTLm45QsT_qFPOXZzvUQdI_AEsjIEDEtsmwEsZ4wcUeb2wq4yPvexbz6idNXKPDwm7Y8-4yDmfbXHXePw8oLS2AOz1USbgYLeuG6OosxedXxrdWOuanJl4N70Ei-EeM9L321kr_PR6_iq-hYUlUMbHLLlsq11gOdaka-OGiaGq1I_ikTeNh6-sHM7-Y0bey6IMkXS62jspHs4E1O4i2vygU7dCBt-7PkEjA9IwyDskmD2sbQCYw5X4F9YP426UBZ1-tlntbLF87sM9r_2nPgrVD2C3vmJRZDqj0OkwyhNocZcmqzxp23h1f_4x3iTFwd5s8hZwVegNpGilRhYuK68Bf0np-162Km74MT0_ekSjobfDNV64VluKyXVADvsNaVtxzpJTOWafQISVos6BUOps_mAm1GgOdkznO8ZkEOaxGz3WjrbVbtIvYzKx6-UvKxQU7KAstOrGdfJ0viHbvOMyV1u5W63Zc1nYGJFH5Q0LWRvmnywD_akLeQAlKMhbh7P8Q8NThmE4QSoEXMAVlMPt1vQnmxRuCjEl7v7L9R2fzXUwg0pfjYCHXyPIUY6mrcDbazqjZY9w_IxbSI_k_j8Q6Mx30ZODiDTCrdDEHDoPHXS2_yuJeTidBjVRkxP3-xZV9OHrOoRDvSxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfa149f9d4.mp4?token=lkBXGIbXx-rzUBWBBn1V9yOXDRm3MMTLm45QsT_qFPOXZzvUQdI_AEsjIEDEtsmwEsZ4wcUeb2wq4yPvexbz6idNXKPDwm7Y8-4yDmfbXHXePw8oLS2AOz1USbgYLeuG6OosxedXxrdWOuanJl4N70Ei-EeM9L321kr_PR6_iq-hYUlUMbHLLlsq11gOdaka-OGiaGq1I_ikTeNh6-sHM7-Y0bey6IMkXS62jspHs4E1O4i2vygU7dCBt-7PkEjA9IwyDskmD2sbQCYw5X4F9YP426UBZ1-tlntbLF87sM9r_2nPgrVD2C3vmJRZDqj0OkwyhNocZcmqzxp23h1f_4x3iTFwd5s8hZwVegNpGilRhYuK68Bf0np-162Km74MT0_ekSjobfDNV64VluKyXVADvsNaVtxzpJTOWafQISVos6BUOps_mAm1GgOdkznO8ZkEOaxGz3WjrbVbtIvYzKx6-UvKxQU7KAstOrGdfJ0viHbvOMyV1u5W63Zc1nYGJFH5Q0LWRvmnywD_akLeQAlKMhbh7P8Q8NThmE4QSoEXMAVlMPt1vQnmxRuCjEl7v7L9R2fzXUwg0pfjYCHXyPIUY6mrcDbazqjZY9w_IxbSI_k_j8Q6Mx30ZODiDTCrdDEHDoPHXS2_yuJeTidBjVRkxP3-xZV9OHrOoRDvSxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:امیدواریم که به انتهای "جنگ" با ایران برسیم. ایران خیلی زیاد می‌خواهد یک توافق منعقد کند.
خبرنگار: آیا از طرف آن‌ها با شما هیچ تماس‌هایی برقرار شده است؟
ترامپ: بله.
@WarRoom</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/withyashar/23334" target="_blank">📅 02:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23333">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مجلس نمایندگان آمریکا با رأی ۲۵۲ موافق در برابر ۱۵۴ مخالف، اصلاحات سنا در طرح «قانون تحریم روسیه و ایرانِ لیندسی اُ. گراهام در سال ۲۰۲۶» را تصویب کرد. در این رأی‌گیری، ۱۹۷ جمهوری‌خواه، ۵۴ دموکرات و یک نماینده مستقل رأی موافق دادند. در مقابل، ۶ جمهوری‌خواه…</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/withyashar/23333" target="_blank">📅 02:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23332">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvUqqSFTnwoHTvrwIcDzsJZVNRGMnpmpWc-VeMPy5eFD4YItMi1oT4FI6--UxXamiu6kTeWIv3i2WNWxUda9-7NRGYrKtLCJAj2HoOGnoPi830aipMVZtPgsQGuL8fLqS6t2QHIDvkHwDl1KhOymw79GVXGgpNqcKKBRQNCT3W5alxeXMAx-yyfMechFxmHpkXYgDbb-zFtfzk6I5APwcgaZqsgrtSEJAuceQO7z9ltbCO_Es5YnqVnPn2dSZJZZ98F2h-MGJ_P6zqotqxKNaxVndxxTZTvVxzZdBP7TUfSmM2iMRv5c0YMQ-t7IazZHssO20tF9kb1N024Nkr8qmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلس نمایندگان آمریکا با رأی ۲۵۲ موافق در برابر ۱۵۴ مخالف، اصلاحات سنا در طرح «قانون تحریم روسیه و ایرانِ لیندسی اُ. گراهام در سال ۲۰۲۶» را تصویب کرد. در این رأی‌گیری، ۱۹۷ جمهوری‌خواه، ۵۴ دموکرات و یک نماینده مستقل رأی موافق دادند. در مقابل، ۶ جمهوری‌خواه و ۱۴۸ دموکرات مخالفت کردند و ۲۷ نماینده نیز رأی ندادند. این طرح با هدف تشدید فشار بر روسیه به‌دلیل جنگ اوکراین پیش می‌رود و تحریم‌های جدید و احتمال اعمال تعرفه‌های تنبیهی را در بر دارد. قرار گرفتن نام ایران در این قانون نیز نشان می‌دهد که واشنگتن قصد دارد فشارها علیه تهران و مسکو را هم‌زمان افزایش دهد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/withyashar/23332" target="_blank">📅 02:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23331">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUJLgziIuSvX4Vc41_oc5XygOfPp2WSCIVkixsOrEGWtDXW6YxXhVoI7s4L0Qu7Td_ivSC5H_nCZCCKkEo6cSipo9jJ0bBdd2goF_wM8ARXCHD-lowP9PXUkO-sxILhmQUxFGhSQhirDHMzxRwx9CNitz-OVy9VCSrobXV3NPqKSnN1mI46DQPlllfwtiUeipAqpoFKHkVt9niGANNNDrbqFeB2Uj-SpAFjzym9qJSqI-2sTV-ZjxubQ2oZ1R_rFZexuHAfay6DZZzncQBBDRdTo5GrQSk47VeHxlWwTa7l_JkHkFo5DF7mUJiwFb4ieaY1UrBKE8KEYEw0OtWdDxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : یک فروند هواپیمای ایلوشین Il-76TD روسی که حدود چهار ساعت پیش وارد تهران شده بود، پس از تخلیه محموله، هم‌اکنون در حال ترک تهران است. این هواپیمای ترابری سنگین قابلیت حمل حدود ۵۰ تن بار و به‌طور خاص برای جابه‌جایی محموله‌های حجیم و سنگین نظامی طراحی شده. نکته قابل توجه، ارتباط این پرواز با شبکه شرکت روسی Gelix Airlines و کال‌ساین GLX است؛ شرکتی که سابقه استفاده از هواپیماهای Il-76 در مأموریت‌های لجستیکی مرتبط با ساختارهای نظامی روسیه دارد. حتی در سوابق رسمی اوکراین، یکی از هواپیماهای مرتبط با Gelix به انتقال ۳۵ تن مهمات از بلاروس به سوریه در سال ۲۰۲۴ نسبت داده شده است. هواپیماهای این شرکت همچنین طی سال‌های اخیر چندین بار در مسیر روسیه–ایران مشاهده شده‌اند و در فوریه ۲۰۲۶ نیز چندین پرواز Il-76 مرتبط با Gelix در فاصله کوتاه وارد تهران و فرودگاه پیام کرج شدند. بنابراین این هواپیما و اپراتور آن قطعاً سابقه فعالیت در لجستیک نظامی دارند
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/withyashar/23331" target="_blank">📅 01:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23330">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مجید شاکری، مشاور قالیباف: استفاده آمریکا از بمب اتمی تاکتیکی علیه ایران، قفل استفاده از این سلاح را برای روس‌ها و چینی‌ها باز می‌کند
@WarRoom
یاشار : این دیگه خدایی عضو کاناله ویس ها رو گوش میکنه</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/23330" target="_blank">📅 00:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23329">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">رويترز:اعضای مجلس سنای آمریکا از دولت ترامپ خواسته‌اند که اسناد و جزئیات کامل توافق هسته‌ای مدنی پیشنهادی با عربستان سعودی را منتشر کند، از جمله دو نامه محرمانه که همراه با این توافق ارائه شده‌اند. آن‌ها تأکید کرده‌اند که بررسی این اسناد برای آگاهی از تعهداتی که بر دوش واشنگتن و ریاض قرار خواهد گرفت، ضروری است.
@WarRoom</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/23329" target="_blank">📅 00:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23328">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htF1y3ensZtWSFI22qtuO3s41vgrGxZJh-wuQCde1PXQF6vGQQBBEfY8GMG5LtjXX-muVPPXS1Fps4odjV9CBwsJtQ3lTtgZ8w4dtka-gpNseFuYMlLQBKh4ZdWLSkm_-42TQGfxVWTNhGNtt6x-khek3iLnfoOjIFyOhtRQu7HqzkKpNxDMsj_p101Iq9VXUWQHNSw2pFe4UD2uaBweFASDKo8K8lcxnGzin-_dsJ6Ya5YpR87XMiX9pW1-q6CDqvbpZEADJsvcD7EdvkqC3T0KEWwk5rFxsTaeIAfRaOhFWFGhk1Nm4Wew2CuMfNBE3PXQqzVafQczCrY3pdH9dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : نرخ بهره در ایالات متحده باید ۱ درصد یا حتی کمتر باشد، چون ما با فاصله زیاد معتبرترین اعتباردهنده در جهان هستیم. کشور ما با سرمایه‌گذاری‌های جدید در حال رونق گرفتن است! اگر تجارت با تمام کشورهایی را که با آنها کسری تجاری داریم ــ که بیشتر کشورهای جهان را شامل می‌شود ــ متوقف کنیم، دست‌کم سالانه ۱.۵ تریلیون دلار درآمد خواهیم داشت. واژه «کسری» چیزی بیشتر از یک کلمه شیک برای «زیان» نیست. ما تقریباً هزینه و بار اقتصادی بسیاری از کشورهای جهان را به دوش می‌کشیم و این وضعیت دیگر نمی‌تواند ادامه پیدا کند. نرخ بهره ایالات متحده آمریکا را سریع و به‌شدت کاهش دهید!
@WarRoom</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/23328" target="_blank">📅 00:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23327">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">علی قلهکی: یکی از پیشنهاداتی که اخیرا «عاصم منیر» در سفری که به تهران داشت، مطرح کرده بود پیوستن ایران به «پیمان مکه» بود
@WarRoom</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/23327" target="_blank">📅 00:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23326">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کانال ۱۴ اسرائیل : توطئه ایران برای ترور دانشمند هسته‌ای خنثی شد؛ دادگاه اورشلیم چهار ساکن شرق این شهر را به اتهام همکاری با اطلاعات ایران محکوم کرد. طبق کیفرخواست، آنها برای شناسایی یک دانشمند هسته‌ای اسرائیلی و خانواده‌اش، تهیه سلاح و نارنجک و اجرای حملات…</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23326" target="_blank">📅 23:39 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23325">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ارومیه و تبریز آتیش بازیه
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23325" target="_blank">📅 23:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23322">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23322" target="_blank">📅 23:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23321">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66843f77e7.mp4?token=GI8USrI9oZEv3HMDIF8xTK_kGkisWRTzPowS_r8h_jFdHU3M8qTKWhY8hNGg6-NWAcnyXLhzA28rLj9mZynA9_CpwM0I3ixn2NTe5ZrWDCtX8yIB-0mWSanW0trONPD6nBOKKDtlc8HqNfzkHwZz8mMLph0EyJtiZHspT1l_igc75o_lNvmmTcR_p8Vjtj9zF_d7I08LR7YjAttDtxT-GihIH4emVt1ezkJdiSDrPnS2xJfF7OuvZ-P6FHNW-tLO-ugIc-J1z3sOBm4KVplHczC89kBd3zPRINT_QELZQSexHEKM9e9YtLl7L-VRtH56mJ4Gxwkr6TcS8RcrOtOnFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66843f77e7.mp4?token=GI8USrI9oZEv3HMDIF8xTK_kGkisWRTzPowS_r8h_jFdHU3M8qTKWhY8hNGg6-NWAcnyXLhzA28rLj9mZynA9_CpwM0I3ixn2NTe5ZrWDCtX8yIB-0mWSanW0trONPD6nBOKKDtlc8HqNfzkHwZz8mMLph0EyJtiZHspT1l_igc75o_lNvmmTcR_p8Vjtj9zF_d7I08LR7YjAttDtxT-GihIH4emVt1ezkJdiSDrPnS2xJfF7OuvZ-P6FHNW-tLO-ugIc-J1z3sOBm4KVplHczC89kBd3zPRINT_QELZQSexHEKM9e9YtLl7L-VRtH56mJ4Gxwkr6TcS8RcrOtOnFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش‌های منابع عربی حاکی از وقوع آتش‌سوزی گسترده در تأسیسات نفتی کرکوک عراق است.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23321" target="_blank">📅 23:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23320">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XH7NgQzjCUfBc1DJLB7nXIWqYjUoYpH7dHT6Ou65zzI88xVRzD-yFeUFa9hQGhWQob20lnfCUKMJMABPHRRFJhvIc0adJOVUUQpdofP5Ii6G4sKp8uuuSSOcMtYmLED47HmBP5UGFx8pFNXuQMqB7k_XrRfNi03voVvf-Kdk-dEgydkGCjMiNc0awFnvj1QE-gpW5g6kWqNcp4z3SQNbn1yVEU9hksabZnnOKbDB_p6E-4SWrQzXPsMxtKHvvOpZVEVBuLvfdlkqOV8S3azDT2CEyrDIcXa-yriPksTuUU7k9JGsuwBJ5qAgDJXNZoyOqrKAOsEVKtVuwBolcwn6Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل اعلام کرد سه عضو شاخه‌های نظامی حماس و جبهه آزادی‌بخش فلسطین را در شمال نوار غزه هدف قرار داده است:
سعید اسعد سعید اخرم
، فرمانده گردان دراج تفاح حماس، که به گفته ارتش مسئول برنامه‌ریزی حملات و کارگذاری بمب علیه نیروهای اسرائیلی بود؛
نمر یاسر نمر ارشی
، عضو شاخه نظامی جبهه در گردان دراج تفاح و مرتبط با شلیک موشک به اسرائیل؛ و
احمد بهات صالح شاعر
، عضو گردان شجاعیه حماس که به گفته ارتش در کارگذاری بمب نقش داشته است. ارتش اسرائیل مدعی است فعالیت این افراد نقض آتش‌بس و تهدیدی برای نیروهایش بوده و آنها برای خنثی کردن این تهدید هدف قرار گرفته‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23320" target="_blank">📅 23:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23319">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دیدبان اتاق جنگ :  همین الان جاده امام رضا به سمت پاکدشت @WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23319" target="_blank">📅 23:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23318">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کان اسرائیل: عربستان گفته اگه اسرائیل به ما کمک کنه ما هم روابطمون رو عادی سازی میکنیم
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23318" target="_blank">📅 22:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23317">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پدافند تبریز فعال شد
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23317" target="_blank">📅 22:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23315">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMfcUnhMzFuvvLkOTZi_ei_BUGl2jJMJYX7oZ0ZM1R_QIXopA-dMwElA3DPgOQTabog5ttt1O20WmnBUEg2KFvLQyCtGwBTbFR9DXGen56IdREmBTv4lYIWRUBVtjXVogbbMeXmmpnmaXKOuH07gdxaC2seSc-8kN8bZLzJc6PqHcPYPVesS-6gkOeo9zgjJgIDlkAHJUdP3htGlLaVW175Ryo1kYb2bjJ7-Gee0COWFl85L4qkLukzZcnDnX0lR14HlEX39KR2s1dASTZqIyA3SztEWw4UJ21XW4xdxZc_hE17KImbH0Nh4Kd-5iZWBJ7Cr6_o7nrrrBPhOw3DSBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری جدید هادی پت پتی
😂
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23315" target="_blank">📅 22:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23314">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وزیر دارایی ترکیه: جنگ آمریکا علیه ایران، تورم سالانه ترکیه را دست‌کم ۵ تا ۷ درصد افزایش داده است
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23314" target="_blank">📅 22:16 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23313">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تصاویر منتشر شده گروه تروریستی حوثی های یمن از منهدم کردن یک جنگنده F15 سعودی و سقوط آن در استان مأرب @WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23313" target="_blank">📅 21:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23312">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23312" target="_blank">📅 21:39 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23311">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">هشدار نوسان در بازار : امشب ساعت ۲۱:۳۰ به وقت ایران تصمیم فدرال رزرو درباره نرخ بهره اعلام می‌شود و ساعت ۲۲:۰۰ کنفرانس خبری رئیس فدرال رزرو برگزار خواهد شد. انتظار می‌رود بازار بیت‌کوین و سایر رمزارزها در این بازه با نوسانات شدید همراه باشد. نکته مهم اینکه…</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23311" target="_blank">📅 21:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23310">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یک مقام نظامی اسرائیلی:
مادامی که تهدیدات حزب‌الله ادامه دارد از جنوب لبنان خارج نخواهیم شد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23310" target="_blank">📅 21:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23309">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اردوغان
: با پادشاهی عربی سعودی اعلام همبستگی کرده و در کنار آن می‌ایستیم. تلاش حوثی‌ها برای حمله به مکه را به شدت محکوم می‌کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23309" target="_blank">📅 21:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23308">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">هشدار نوسان در بازار : امشب
ساعت ۲۱:۳۰ به وقت ایران
تصمیم فدرال رزرو درباره نرخ بهره اعلام می‌شود و
ساعت ۲۲:۰۰
کنفرانس خبری رئیس فدرال رزرو برگزار خواهد شد. انتظار می‌رود بازار بیت‌کوین و سایر رمزارزها در این بازه با
نوسانات شدید
همراه باشد. نکته مهم اینکه حتی اگر واکنش اولیه بازار منفی باشد، در جریان کنفرانس خبری ممکن است سیگنال‌های مثبت درباره مسیر آینده سیاست پولی دریافت شود و جهت حرکت بازار تغییر کند؛ بنابراین بهتر است معامله‌گران تا مشخص شدن موضع کامل فدرال رزرو، نسبت به نوسانات لحظه‌ای محتاط باشند
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23308" target="_blank">📅 21:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23307">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ایرنا و ایسنا:
الحاق بخشی از حریم درجه دو تخت‌جمشید به محدوده شهری مرودشت همچنان با اعتراض و مخالفت میراث فرهنگی روبه‌روست
. این طرح مربوط به محدوده روستای مهدیه است و گزارش‌ها از
الحاق حدود ۱۱۰ هکتار
و در برخی گزارش‌ها از محدوده‌ای حدود
۱۶۰ هکتار
سخن می‌گویند. وزارت میراث فرهنگی و شورای راهبری پایگاه‌های جهانی پارسه و پاسارگاد با این طرح مخالفت کرده‌اند و مدیرکل میراث فرهنگی فارس گفته
این الحاق تاکنون اجرایی نشده و باید بازنگری شود
. همزمان گزارش‌هایی درباره
استعفای محمدجواد جعفری، سرپرست پایگاه میراث جهانی تخت‌جمشید
منتشر شده است. جامعه باستان‌شناسی ایران نیز با ارسال نامه‌ای به مسعود پزشکیان خواستار
اقدام فوری برای حفاظت از حریم تخت‌جمشید
شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23307" target="_blank">📅 21:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23306">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تیم هاوکینز ,سخنگوی فرماندهی مرکزی ایالات متحده در گفت‌وگو با الجزیره: کشتیرانی همچنان از طریق تنگه هرمز جریان دارد و ایران آن را کنترل نمی‌کند.محاصره بنادر ایران توسط آمریکا «آهنین و غیرقابل شکستن»است ، ما به تسهیل عبور بیش از ۹۰۰ میلیون بشکه نفت خام از تنگه هرمز کمک کردیم. ما مین‌زدایی از خطوط کشتیرانی بین‌المللی در هرمز را تکمیل کرده‌ایم
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23306" target="_blank">📅 21:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23305">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23305" target="_blank">📅 21:09 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23304">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmin</strong></div>
<div class="tg-text">سوباسا هم به دوست پسر ننش میگفت عمووو</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23304" target="_blank">📅 21:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23303">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خبرگزاریCNN:
مایک جانسون، رئیس مجلس نمایندگان آمریکا، اعلام کرد مجلس برای یک تعطیلات هفت‌هفته‌ای انتخاباتی زودتر از موعد واشنگتن را ترک می‌کند
و نمایندگان تا پس از انتخابات میان‌دوره‌ای نوامبر به واشنگتن بازنمی‌گردند. در نتیجه،
رأی‌گیری درباره استیضاح پیت هگستث، وزیر دفاع آمریکا، به تعویق افتاد
؛ این طرح از سوی نماینده جمهوری‌خواه توماس مَسی در ارتباط با نحوه مدیریت جنگ ایران مطرح شده بود. نمایندگان پیش از ترک واشنگتن،
رأی نهایی درباره لایحه تحریم‌های روسیه و ایران
را در دستور کار دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23303" target="_blank">📅 20:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23302">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5WrBI184XN7pY9I4toJHNdLAmvocwFWD7NKpIJI971LtQrkbULj7WHOAwCVVHIpT1Ov6jkZSP3VR1dT6pr8NEY8ZcBTpORBFG7bhNSFLXXpc-_SZIUmORwZ5KE3VSCXy5jQfA6_AU8SQkJIxR9KsDw5UlsIdY-JUrFrwSRpiaHpzQ6nEk5olidWH1OGSSQ2K09hbZpw4gfLll8_8yXXDSBAWEqfPDDUpkzLFjEeps5HsCMrcrNppg9Up-WfKT3K8AoasZCS8Uq9_i_RB3n2ChqmccN-uCP-MkJkjqcwKAlX8xpJNlCVVp4rc17d2vkxjrmrtXnk8zOzyaq8b4fj6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : سلام  یاشار جان اومدیم سمت بابلسر  یکی از کشتی ها که تو صفه داره میسوزه معلوم  نیست چیه داستان. گشت ساحلی میومد میرفت همش
@WarRoom
یاشار: چیزی‌نیست این کار عمو زلینکشتیسکی هست</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23302" target="_blank">📅 20:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23301">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">میدل ایست اسپکتور:
چیزی در حال وقوع است
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23301" target="_blank">📅 20:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23300">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxPqP5s4LGgKB4WYGSQfUqMe3fEgwYukWzN8v4LjcunORUxszx_Uu32C3tZTWdUfnJRznZVoGKnQp1YMNr9SbIDs6VLXpeMLm0cYTbnsSM_WO8tpSs2orwAIgyMEqAiEKdON2IYkt6iHrWs_4KtnldZwF7RwiL2mQ8eS4omwDEm1m3c2hO7DNig2aKuJw6i_RhUeKW_3wDnQBIv5Q80obw1bz4yRdWFQHYujoQ5A-tJcLsxWmUuszx8VLBm-yMCW0FhkyPlfuZB6iXTQaASE2cBF9w5bJrE12_u14viYP0MlK3XmK_cMlllZTWwG7uHnjZe1JCBnuKt0oDijO7tzUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ :  همین الان جاده امام رضا به سمت پاکدشت
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23300" target="_blank">📅 20:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23299">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اتاق جنگ با یاشار:
ویدئوی جدید حوثی‌ها از هدف قرار گرفتن F-15 سعودی، از نظر تصویر و شیوه رهگیری شباهت قابل‌توجهی به تصاویر پدافند ایران دارد و به‌نظر می‌رسد از سامانه
الکترواپتیکی/حرارتی (EO/IR) و دوربین FLIR
برای کشف و دنبال‌کردن هدف استفاده شده است. اما نکته مهم این است که
این لزوماً به معنی یک سامانه بزرگ زمینی نیست
؛ با توجه به سابقه حوثی‌ها در استفاده از موشک‌های شانه‌پرتاب
MANPADS
، چنین سناریویی کاملاً ممکن است. ترامپ نیز پیش‌تر درباره سرنگونی F-15E توسط ایران گفته بود که هواپیما با یک
موشک حرارتی شانه‌پرتاب
زده شده است. حوثی‌ها علاوه بر
میثاق-۲ ایرانی
، موشک‌های روسی/شوروی مانند
R-27 و R-73
را به سامانه‌های زمین‌به‌هوا تبدیل کرده‌اند و
صقر-۳۵۸
با منشأ فناوری ایرانی را نیز دارند. از طرف دیگر، گزارش‌هایی درباره ورود
MANPADS چینی QW-12، QW-18 و QW-19
به ایران منتشر شده است؛ بنابراین منشأ دقیق تجهیزاتی که در ویدئوی امروز دیده می‌شود هنوز مشخص نیست و
نمی‌توان فعلاً آن را قطعی ایرانی، روسی یا چینی دانست
. آنچه روشن‌تر است، شباهت جدی در معماری پدافندی و انتقال فناوری و تجربه میان ایران و حوثی‌هاست.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23299" target="_blank">📅 19:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23298">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یک تحلیلگر ارشد رسانه‌ای سعودی: "غیرقابل فهم است که چگونه اسرائیل در طول 3 سال گذشته، بدون هیچ مانعی، در ایران و هر کجا که خواسته، گشت‌زنی و حمله کرده است، در حالی که ما برای مقابله هوایی با حوثی‌ها با مشکل مواجه هستیم."
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23298" target="_blank">📅 19:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23297">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">رسانه های عبری ، تحلیلگران مسائل خاورمیانه مدعی‌اند: «بزرگترین حمله قرن علیه ایران، با مشارکت تمامی کشورهای منطقه، به‌زودی به وقوع خواهد پیوست؛ با این حال، ایران در پی آن، کشورهای کوچک‌تر منطقه نظیر کویت و بحرین را  ویران و خساراتی سنگین و قابل‌توجه به مابقی وارد خواهد ساخت.»
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23297" target="_blank">📅 19:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23296">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuplHZo6ArVR4ILhbHyhDR6sQqlIw3YnsoyFbrfrCadt0X_z0LCmaJk5YsJkijvAWuFBF-Vw9J3jWrzApnZCQgza5yJQqUCU9QzYwZ_9eiWQRgEmiJRSfddPzYpS8xWrmA8Rv6TnDyOThlSV8dvTxqwPMxD0OI1C7ru9hUf08aeiTcCcdsm65eY7daPiEjXZ_NLLrnTLgXH8EboVECF3e3yefFPALVql_ltY3Za6blXXjSTh8yppE5yMBxVDMS3KQtkJFfcYNZH_PxICUC2CY_UPLpjTEkZd8HjGbN9If_49vMl_H9RCIs0Kz_HcLOBDLwBhBpbltQWd6rfFtJYhMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماره شناسه این هواپیما 5529 است، که نشان می‌دهد این یک جنگنده پیشرفته از مدل F-15SA است و ارزش آن حدود 110 میلیون دلار یا بیشتر است. همچنین، این هواپیما دو صندلی دارد، به این معنی که دو خلبان در آن حضور داشتند
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23296" target="_blank">📅 19:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23295">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کانال ۱۴ اسرائیل :
توطئه ایران برای ترور دانشمند هسته‌ای خنثی شد
؛ دادگاه اورشلیم چهار ساکن شرق این شهر را به اتهام
همکاری با اطلاعات ایران
محکوم کرد. طبق کیفرخواست، آنها برای
شناسایی یک دانشمند هسته‌ای اسرائیلی و خانواده‌اش، تهیه سلاح و نارنجک و اجرای حملات ساختگی با هدف تبلیغات
مأموریت‌هایی انجام داده بودند. این پرونده بخشی از مجموعه پرونده‌های اخیر درباره تلاش اطلاعات ایران برای جذب نیرو در اسرائیل عنوان شده است.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23295" target="_blank">📅 18:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23294">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92f2003af5.mp4?token=sKL2OQ3Vpje8CKpd33l3wzAttHoVIwaX-CvI62dylxDxDEkJDWwzP_-ZpwrSL2SatBuIrUZbqWQq48FUNGr-gXlpOUP-AJgqDut5XZQy--iH7btMuLKCj7KQKHABTy3nqwT3TFjoM6Z-iKceY_OjRwO18lXJ51oqucfDe9FauSEWRdjHwhI1VBf9lzCtQYg_z2-E1FPz-3R7Ufvf5BfRQZxJMZ4s7CQ9iB4Zx0s2hayHdcZh8MjVKL1d_JBLRaHYAiki9AUl_Zsy_t9hd3E0mRepq_8FDEQhjwqPztjM79SihL0Hpm_4Yg3hV4CjV3RtXMZ-GcEIBYwv6DNOWL5veRvbKt5lJFENve0Z4_Cu-UOs6mgrdD3ieNF96u4kycK-ywcKawimGZrT1fJXnkW7RKep44S12vWmiOq15Q-aUzRZDgL_e1yQCI0_4Wpgxaap5Swea0T9Uhwgck1VEiDeeciD8ivpIABx-Hte5O0QI5aBGNNrJqT50SgCSYg8YYkTcVWvCLX--hQJnu6BBzFcKMYt-9tquHUYb9LsswngLykvDdMakR26GjkBb2Q6X-N3JuuClDhgK_15qXTfNlVRlvpxjkEjzvCOW_FDn1G2I8JeOjC2GH0A8fjd1dN9Bqvynv7g4aStytx7qw5cPUvKDtH58G7oAggGgEwkDt4YCCI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92f2003af5.mp4?token=sKL2OQ3Vpje8CKpd33l3wzAttHoVIwaX-CvI62dylxDxDEkJDWwzP_-ZpwrSL2SatBuIrUZbqWQq48FUNGr-gXlpOUP-AJgqDut5XZQy--iH7btMuLKCj7KQKHABTy3nqwT3TFjoM6Z-iKceY_OjRwO18lXJ51oqucfDe9FauSEWRdjHwhI1VBf9lzCtQYg_z2-E1FPz-3R7Ufvf5BfRQZxJMZ4s7CQ9iB4Zx0s2hayHdcZh8MjVKL1d_JBLRaHYAiki9AUl_Zsy_t9hd3E0mRepq_8FDEQhjwqPztjM79SihL0Hpm_4Yg3hV4CjV3RtXMZ-GcEIBYwv6DNOWL5veRvbKt5lJFENve0Z4_Cu-UOs6mgrdD3ieNF96u4kycK-ywcKawimGZrT1fJXnkW7RKep44S12vWmiOq15Q-aUzRZDgL_e1yQCI0_4Wpgxaap5Swea0T9Uhwgck1VEiDeeciD8ivpIABx-Hte5O0QI5aBGNNrJqT50SgCSYg8YYkTcVWvCLX--hQJnu6BBzFcKMYt-9tquHUYb9LsswngLykvDdMakR26GjkBb2Q6X-N3JuuClDhgK_15qXTfNlVRlvpxjkEjzvCOW_FDn1G2I8JeOjC2GH0A8fjd1dN9Bqvynv7g4aStytx7qw5cPUvKDtH58G7oAggGgEwkDt4YCCI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو:
ما با یک
حمله جهانی علیه دولت و ارتش اسرائیل
روبه‌رو هستیم. در این حمله، اسرائیل و سربازانش نه‌تنها به‌عنوان
مرتکبان جنایات جنگی
معرفی می‌شوند که به گفته من، ادعایی بسیار مضحک درباره منصف‌ترین ارتش جهان است بلکه اسرائیل را به
آزار اقلیت‌ها
نیز متهم می‌کنند. اسرائیل یک
جزیره پیشرفت، تحمل و امنیت
است و من این را درباره همه جوامع می‌گویم.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23294" target="_blank">📅 18:17 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23293">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">شاهزاده رضا پهلوی: چهار سال از روزی می‌گذرد که جلادان ضحاک، جان دختر ایران، مهسا امینی، را گرفتند؛ اما
خون مهسا پایمال نشد و یک ایران برای او به پا خاست.
پس از آن، نیکا و سارینا، کیان و خدانور و صدها فرزند دیگر ایران نیز جان باختند. چهار سال بعد، ملت ایران در ادامه همان مبارزه ایستاده است؛ مسیری که از
دی ۹۶، آبان ۹۸ و خیزش‌های ۱۴۰۱ و ۱۴۰۴
گذشت و امروز به
انقلاب ملی شیر و خورشید
رسیده است؛ با یک هدف ملی:
بازپس‌گیری ایران از رژیمی که نزدیک به نیم قرن میهن‌مان را به گروگان گرفته است.
یاد مهسا و همه جان‌باختگان راه آزادی ایران جاودانه خواهد ماند.
ما راه آنان را تا آزادی و بازپس‌گیری ایران ادامه خواهیم داد. پاینده ایران
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23293" target="_blank">📅 18:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23291">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuXPfT4fPCIzG1IU7w50_J7w0hkzvZNRPRrLWA5lZcJuCsvhCoQKRIFfcoTSeduLqDxoTly8JNvF7mJR1CFCVNEMnwivMjWVgmm-Y-h2TpyrROFg6qAk3nDWz6xcBfSuFqnvU3a7y9jeur2zhhsg6oPSPyqpljqCTOjQ-w0QUYUFvG1YQlacDw1b70nERf97twIvczWQ4Gf7hsOc_iKtASZrkT3CDGFx29fUp32nMdiFwLxc6VzE8_0L-WSN9ytbcqd3dnp18s0enacV1MiwPI0ws7njkjmDdN7L6cf8WTdCbb3Q9g3Hp4xuCOD1XIAd2jGeTL3W7ozc4F_Di2XRBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسوشیتدپرس , گزارش تأییدنشده: حوثی‌ها مدعی سرنگونی یک جنگنده اف‌ـ۱۵ سعودی در مأرب شده‌اند، اما تاکنون مدرک تصویری یا تأیید مستقل معتبری برای این ادعا منتشر نشده است. @WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23291" target="_blank">📅 18:00 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23288">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c87986bd5.mp4?token=lxlgYjkJ4QuT8iPAV5tDhQlYZ_U3s-YlT4Nmb7GBZNA0JO22xH3kJ29lxULLVc1YXsOvf1J29N0WeTkegfzoS0FtRdByRajigoc3q_jNVs27hhOijVi5RwyiYAAOUSJpyFtdzsF1RcyEfL5ysc-vPrF4TpTK0gupySRDwtrUo8F8swzwMUd_jHN8wClXiksO0Xz0yFDwSF1rUjUxEg6Afk1xUiIq_V65VONSrF3QYeAnUOIjLZWS6Z4SdnjBo4cnfXtlH7dbpCuwlRDL1Q36wxM_wka5TvbIzQISOjwzEaau-LVBHPmRKk6cFFSpdczjaGLx4LC_OGFj3wdSdmAulw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c87986bd5.mp4?token=lxlgYjkJ4QuT8iPAV5tDhQlYZ_U3s-YlT4Nmb7GBZNA0JO22xH3kJ29lxULLVc1YXsOvf1J29N0WeTkegfzoS0FtRdByRajigoc3q_jNVs27hhOijVi5RwyiYAAOUSJpyFtdzsF1RcyEfL5ysc-vPrF4TpTK0gupySRDwtrUo8F8swzwMUd_jHN8wClXiksO0Xz0yFDwSF1rUjUxEg6Afk1xUiIq_V65VONSrF3QYeAnUOIjLZWS6Z4SdnjBo4cnfXtlH7dbpCuwlRDL1Q36wxM_wka5TvbIzQISOjwzEaau-LVBHPmRKk6cFFSpdczjaGLx4LC_OGFj3wdSdmAulw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سناتور جمهوری‌خواه تد کروز درباره جمهوري اسلامي ایران:
آیا ترامپ قرار است صدها هزار سرباز را به زمین بفرستد و سعی کند ایران را به سوئیس تبدیل کند؟ نه.این وظیفه نیروهای نظامی نیست. وظیفه نیروهای نظامی این است که جلوی دیوانگان را بگیرند تا ما را به قتل نرسانند
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23288" target="_blank">📅 17:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23287">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
مقامات سعودی از عدم اقدام قاطع آمریکا علیه حوثی‌ها به‌شدت خشمگین هستند
و معتقدند واشنگتن در برابر حملات انصارالله
«تصمیم عملی» اتخاذ نکرده است
. یک منبع سعودی نزدیک به خانواده سلطنتی گفت حوثی‌ها از این وضعیت سوءاستفاده می‌کنند و در نتیجه
عربستان مجبور شده هزینه مقابله با آنها را در میدان بپردازد
. یک مقام سعودی دیگر نیز از نبود حمایت عملی منطقه‌ای گلایه کرد و گفت:
«از پاکستان یا ترکیه جز بیانیه‌ها چیزی دریافت نکرده‌ایم.»
به گفته این مقام، ریاض در شرایطی که در حال بررسی
راهبرد جدید برای تأمین امنیت دریای سرخ
است، احساس می‌کند رها شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23287" target="_blank">📅 17:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23286">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6IXgeWbNBklS4DL75olctuTyIBaeI8w92y68sqFYIBsu912zc_mCYkCKC8esD68tUtc-XGOSHZF1gSqUGTFQ6_GKvcdrO9Vb05oZ6CLYvUjwiCBFD2ZrbDozGLS00qu_LJ09Z35X5T8mo4lXKZFQ--EfSTo9j-H0dP5mTZDxyRZXOtgiUQqLV9qcwLMmqeMbW4YJqGGVjWpFLVTKDKAhGdxaE4pvl4TWCGg4a-0TxrelGyQe6gmQSGpjxlcPnDMmUNLNMfGYzKM2T0Gly805B4hNhKDfhji-RJFDU0L0Zl9crstGYQiX0iKlQeCUTyzdqN9SvltjiBe4mJs8T3HKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو منبع به فاکس‌نیوز گفتند که اوایل این هفته، یک کشتی طرف قرارداد ایالات متحده در جریان حمله‌ای از سوی ایران هدف قرار گرفت.
این حادثه «در حوالی تنگه هرمز» رخ داد و در آن چهار پهپاد و دست‌کم یک موشک ایرانی دخیل بودند.
یکی از پرتابه‌ها به کشتی اصابت کرد و موجب جراحات جزئی، از جمله عوارض ناشی از استنشاق دود، شد. مجروحان در یکی از کشورهای حوزه خلیج [فارس] تحت درمان هستند. تعدادی از «پرسنل آمریکایی» نیز در این کشتی حضور داشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23286" target="_blank">📅 17:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23283">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9011b5dbf.mp4?token=e60EAErHI8xpGIn-feNt9ZtF6i5-mLgKL64nMY5cs5Dv9eLOt558sjpQWaVTd_q9i-4H_BwbdIlDxUvgoP8EsqAuK-A0rGaKUodHHFEvWtb2eZ7EvSC_A9Z72ov0EJPNRYkqWJPsEUMJ_ufNGPrbKZhrBwf3m1LCOZgGPObN3eUNdIC4dq3p4WcZUiPRAWdG29ay1C3NAbdoz50M99pM_wDx2JfqYghUFTjmi7SmBgbnEIkvDEXmpvozAGA391ddcKfmu8BhGGFMMKQKL_btfWb8cGWUmCKoLw1fnsKWKgHvYbi7PXbS5jAji8Uwa_mFe424g9uu-pVlYV1-Koqhjp0r2sC0OXAFAdVDMr1VWWNMWsD50MrpuNQXmlusYbLudqrnbeMEXjUnKzzLqgES3nN-H9LYrqemp2LL2NTVs7rEku4Us7Phldtockhxp7A771JQ5lCATq_Sv5Ek-XDjwcADVDp5e3qVR5S4uaa75XCfuhjpBGthJWrRJcLrQ9jpQc5uKAKf0xin61NSGstUortHtqqEcp3swilALDbJlTDA8VbGbq4sGtEMthKlCTQzKLQUk5qhx1U_pnl2gnCt3CHXzjWemkTCHfJvedwUU5sn61Zdmx02IliuBonyGaZR-qrtgj8UqzcRTopq4_nxcWkK8J20uZsJKaSF0zXJt4I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9011b5dbf.mp4?token=e60EAErHI8xpGIn-feNt9ZtF6i5-mLgKL64nMY5cs5Dv9eLOt558sjpQWaVTd_q9i-4H_BwbdIlDxUvgoP8EsqAuK-A0rGaKUodHHFEvWtb2eZ7EvSC_A9Z72ov0EJPNRYkqWJPsEUMJ_ufNGPrbKZhrBwf3m1LCOZgGPObN3eUNdIC4dq3p4WcZUiPRAWdG29ay1C3NAbdoz50M99pM_wDx2JfqYghUFTjmi7SmBgbnEIkvDEXmpvozAGA391ddcKfmu8BhGGFMMKQKL_btfWb8cGWUmCKoLw1fnsKWKgHvYbi7PXbS5jAji8Uwa_mFe424g9uu-pVlYV1-Koqhjp0r2sC0OXAFAdVDMr1VWWNMWsD50MrpuNQXmlusYbLudqrnbeMEXjUnKzzLqgES3nN-H9LYrqemp2LL2NTVs7rEku4Us7Phldtockhxp7A771JQ5lCATq_Sv5Ek-XDjwcADVDp5e3qVR5S4uaa75XCfuhjpBGthJWrRJcLrQ9jpQc5uKAKf0xin61NSGstUortHtqqEcp3swilALDbJlTDA8VbGbq4sGtEMthKlCTQzKLQUk5qhx1U_pnl2gnCt3CHXzjWemkTCHfJvedwUU5sn61Zdmx02IliuBonyGaZR-qrtgj8UqzcRTopq4_nxcWkK8J20uZsJKaSF0zXJt4I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استوری های اینستاگرام که درخواست زیاد بود که چنل هم قرار بدم
❤️‍🩹
🙌🏾
instagram.com/yashar
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23283" target="_blank">📅 16:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23282">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پروازهای ماهان به استانبول، آنکارا و مسقط متوقف شد هواپیمایی ماهان پروازهای بین‌المللی خود در مسیرهای ترکیه و عمان را تا اطلاع ثانوی تعلیق کرد. بر اساس بخشنامه‌های ابلاغ‌شده، مسیر تهران-مسقط از ۲۶ شهریور و مسیرهای تهران-استانبول و تهران-آنکارا از ۳۰ شهریور…</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23282" target="_blank">📅 16:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23281">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پروازهای ماهان به استانبول، آنکارا و مسقط متوقف شد
هواپیمایی ماهان پروازهای بین‌المللی خود در مسیرهای ترکیه و عمان را تا اطلاع ثانوی تعلیق کرد.
بر اساس بخشنامه‌های ابلاغ‌شده، مسیر تهران-مسقط از ۲۶ شهریور و مسیرهای تهران-استانبول و تهران-آنکارا از ۳۰ شهریور لغو می‌شوند. اطلاعیه‌های این تصمیم به دفاتر خدمات مسافرت هوایی ارسال شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23281" target="_blank">📅 16:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23280">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23280" target="_blank">📅 16:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23279">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHosiin 27</strong></div>
<div class="tg-text">داداش نبینم بغضتو
🫡
🫡
😓
سرت سلامت
😘
💙
🫡</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23279" target="_blank">📅 16:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23278">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromR</strong></div>
<div class="tg-text">درود آقا یاشار تا شما گفتین بهتره  شاهزاده در موضوع.مهسا امینی ورود کنن
دقیقا دو ساعت بعد یک پست برای مهسا امینی گذاشتن و تمام جاوید نام های اون زمان</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23278" target="_blank">📅 16:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23277">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromsina</strong></div>
<div class="tg-text">آقا خیلی دوست داریم، دمت گرم که پشت مردمی، اولین بار و تنها باری که دیدمت توی همایش ثباتی توی جاجرود بود که با مازراتیت اومده بودی و یکم باهم صحبت کردیم
❤️</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23277" target="_blank">📅 16:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23276">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">آسوشیتدپرس , گزارش تأییدنشده: حوثی‌ها مدعی سرنگونی یک جنگنده اف‌ـ۱۵ سعودی در مأرب شده‌اند، اما تاکنون مدرک تصویری یا تأیید مستقل معتبری برای این ادعا منتشر نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23276" target="_blank">📅 15:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23275">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رویترز: وانگ‌یی، وزیر خارجه چین، در دیدار با عباس عراقچی خواستار خویشتنداری ایران و آمریکا و ازسرگیری مذاکرات شد و گفت بازگشایی تنگه هرمز برای ثبات حمل‌ونقل انرژی ضروری است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23275" target="_blank">📅 15:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23274">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">وال‌‌استریت ژورنال:
دست‌کم
دو نفتکش خارجی
که در مسیر آمریکا بودند، در اوایل ماه اوت هنگام عبور از
تنگه جبل‌الطارق
هدف حملات سایبری قرار گرفتند. یکی از این کشتی‌ها، نفتکش بزرگ
«وی‌ال پراسپریتی»
با پرچم
لیبریا
بود که نفت حمل می‌کرد و مقصدش
گالوستون تگزاس
بود. گارد ساحلی آمریکا و اف‌بی‌آی پس از رسیدن کشتی‌ها به خلیج مکزیک، در روزهای ۲۱ و ۲۴ اوت آنها را بازرسی کردند، زیرا شواهدی از نفوذ به شبکه‌های عملیاتی و فناوری اطلاعات کشتی‌ها وجود داشت.
آمریکا تاکنون عامل این حملات را شناسایی نکرده است
و مقام‌ها در حال بررسی احتمال نقش
ایران
یا دیگر بازیگران خارجی هستند. نام و پرچم نفتکش دوم در گزارش عمومی وال‌استریت ژورنال اعلام نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23274" target="_blank">📅 14:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23273">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">رویترز:
مقام‌های آمریکایی طی آخر هفته در سفارت آمریکا در مسقط، پایتخت عمان، با نمایندگان حوثی‌های یمن دیدار کردند؛ موضوعی که تاکنون علنی نشده بود و پنج منبع آگاه آن را تأیید کرده‌اند. این دیدار چند روز پس از آن انجام شد که حوثی‌های مورد حمایت ایران در یک عملیات گسترده، بخش‌هایی استراتژیک از ساحل دریای سرخ را تصرف کردند و نیروهای مورد حمایت عربستان را عقب راندند. جزئیات دقیق مذاکرات مشخص نیست
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23273" target="_blank">📅 14:39 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23272">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDanush</strong></div>
<div class="tg-text">تهرانپارس فلکه سوم صدا داد و فریاد جاوید شاه میاد</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23272" target="_blank">📅 14:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23270">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e38033fdf.mp4?token=dpH_nq7WkhExEtd-y6ZWLJinHpvz4oQ7NrI9TlI7WE4r_0V7rXUe-9uCqBn5_SxKF7PC94aG8wjpKnm99uYhRfLEUPLp2AIS5XUyxWidM3-6FTHoM9em0cUbF-2fbIICPIDFdU0MQTjSTRChlcaWkXUb-WGPzYA3Myn_joVMFPBTSxhI6WXX--2CFhXP9l4p20chn2SK8r2hC49tao6832y6rwAT7DE6PIyPNrLAk2HZuwtJ3s3le0Eamun34x_Y5QWk5qMjvQijvScZiOSsmKLCBDUTD3iMFGGu_dpHjXjp5cr1eD-o5ExYbAZnW-11-DEP55a1TGT5ZVi4O7VJ1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e38033fdf.mp4?token=dpH_nq7WkhExEtd-y6ZWLJinHpvz4oQ7NrI9TlI7WE4r_0V7rXUe-9uCqBn5_SxKF7PC94aG8wjpKnm99uYhRfLEUPLp2AIS5XUyxWidM3-6FTHoM9em0cUbF-2fbIICPIDFdU0MQTjSTRChlcaWkXUb-WGPzYA3Myn_joVMFPBTSxhI6WXX--2CFhXP9l4p20chn2SK8r2hC49tao6832y6rwAT7DE6PIyPNrLAk2HZuwtJ3s3le0Eamun34x_Y5QWk5qMjvQijvScZiOSsmKLCBDUTD3iMFGGu_dpHjXjp5cr1eD-o5ExYbAZnW-11-DEP55a1TGT5ZVi4O7VJ1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کردستان در اعتصاب سراسری؛
‏تا الان اعتصاب سراسری در این شهر ها تایید شده: سقز , کرمانشاه, مهاباد , ‏سنندج , پیرانشهر ، دیواندره ، مریوان ، اشنویه ، بانه ، بوکان
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23270" target="_blank">📅 14:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23269">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">زلنسکی: روسیه دو بار تلاش کرد هواپیمای من را هدف قرار دهد
رئیس‌جمهور اوکراین در مصاحبه با CBS گفت پهپادهای روسی در دو نوبت اخیر حریم هوایی مولداوی را نقض کردند؛ هر دو مورد زمانی رخ داد که هواپیمای ریاست‌جمهوری او در حال عبور از منطقه بود. زلنسکی گفت این حوادث ممکن است بخشی از تلاش روسیه برای ایجاد تهدید و ارعاب او و دیگر رهبران خارجی باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23269" target="_blank">📅 12:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23268">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خبرگزاری واپو: دولت ترامپ در حال آماده‌سازی یک فروش تسلیحاتی به ارزش ۲.۸ میلیارد دلار به اسرائیل است که شامل ۴۰,۰۰۰ بمب ۲,۰۰۰ پوندی (۲۰,۰۰۰ بمب MK-84 و ۲۰,۰۰۰ بمب BLU-117) به علاوه ۲۰,۰۰۰ سر جنگی نفوذگر I-2000 خواهد بود. @WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23268" target="_blank">📅 12:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23267">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23267" target="_blank">📅 12:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23266">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23266" target="_blank">📅 12:17 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23265">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سی‌ان‌ان:
۱۴ ماهواره جاسوسی روسیه در روزهای پیش از حمله موشکی و پهپادی ایران به پایگاه هوایی پرنس سلطان آمریکا در عربستان سعودی، چندین بار از فراز این پایگاه عبور کرده‌اند. مقام‌های آمریکایی در حال بررسی این احتمال هستند که اطلاعات جمع‌آوری‌شده توسط این ماهواره‌ها در اختیار ایران قرار گرفته و به تهران در شناسایی دقیق اهداف و اجرای حمله کمک کرده باشد. این موضوع در حالی مطرح شده که حملات ایران به مواضع آمریکا در منطقه، خسارات و تلفات قابل‌توجهی به نیروهای آمریکایی وارد کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23265" target="_blank">📅 12:16 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23264">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23264" target="_blank">📅 12:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23263">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23263" target="_blank">📅 12:06 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23262">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23262" target="_blank">📅 12:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23261">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">تازه‌ترین گزارش‌ها حاکی از آن است که در شهرهای سنندج، کرمانشاه، سقز، مهاباد، پاوه، بوکان، مریوان، اشنویه و دیواندره، بسیاری از مغازه‌ها و واحدهای صنفی تعطیل هستند و کسبه محلی به مشارکت در این اعتصاب  سنگین ادامه می‌دهند. @WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23261" target="_blank">📅 12:00 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23260">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a55785df5e.mp4?token=XqSU0v7415ZLbmAICYB0IXdVCmgMxYu2FV-lwDf-3ecGL3SU1EzgyVGnbc4_fhxh8WuiDRONhXEiN_LY0XwnvTFhkr2S3yGnNlNlaei2QzFrRxUSxBiObt8LHAnnRZLKV3SXPadjCtMR5pDalWjRUB0G_gS7nmQPhcAJNE4zmxFLnBGCpVvXcvJT7WvE9fT9LGd3W49vTaXas1EBlRBntYVt83O5MOrRJP0IbY2OsUYVmZ7qlaUWcU0pGLCIPjG8r0HrjEjod3O7mwplPLY3FC_H_XaieqJIAuLbAe5Lu_kq5T77JcHioaUHgIllNoQBEn2OS1tBwa4UknHt-karhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a55785df5e.mp4?token=XqSU0v7415ZLbmAICYB0IXdVCmgMxYu2FV-lwDf-3ecGL3SU1EzgyVGnbc4_fhxh8WuiDRONhXEiN_LY0XwnvTFhkr2S3yGnNlNlaei2QzFrRxUSxBiObt8LHAnnRZLKV3SXPadjCtMR5pDalWjRUB0G_gS7nmQPhcAJNE4zmxFLnBGCpVvXcvJT7WvE9fT9LGd3W49vTaXas1EBlRBntYVt83O5MOrRJP0IbY2OsUYVmZ7qlaUWcU0pGLCIPjG8r0HrjEjod3O7mwplPLY3FC_H_XaieqJIAuLbAe5Lu_kq5T77JcHioaUHgIllNoQBEn2OS1tBwa4UknHt-karhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تازه‌ترین گزارش‌ها حاکی از آن است که در شهرهای سنندج، کرمانشاه، سقز، مهاباد، پاوه، بوکان، مریوان، اشنویه و دیواندره، بسیاری از مغازه‌ها و واحدهای صنفی تعطیل هستند و کسبه محلی به مشارکت در این اعتصاب  سنگین ادامه می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23260" target="_blank">📅 11:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23259">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23259" target="_blank">📅 11:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23258">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23258" target="_blank">📅 11:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23257">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‏اعتصاب عمومی در سنندج و شماری دیگر از شهرهای استان کردستان ایران آغاز شده است. @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23257" target="_blank">📅 11:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23256">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5da33205e.mp4?token=g6O8HvkMOX2gO2coZotPiY_VGJ5YTFhc-_Zuo4v5XZIOLQF4J584l1nFG0yH6vNQsbaplP5qh1MU4k0g-6tvg_LSutZaifHXJYphH9-jfJURLfkhs_mY85Iw5Me-E_lxAoqINn3_WhEfgnVPbnwczSRDpcmv8Ewq3htdHT55UGp8UchzWByoYLCw_-mS87BzYAeHXAbPy7AZYwqP_s0ccDo7F8DlH71Fio0NSjA6LB22tzSZcRKbcFaw0bA8uWe8s7O3SiqJLCa-j_XoM7y2PR9jYCdyZRxkugxqb9TW648YWAik-7AIKOIWDVTM7zyjzJv75zfUAnzphGnwK31SjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5da33205e.mp4?token=g6O8HvkMOX2gO2coZotPiY_VGJ5YTFhc-_Zuo4v5XZIOLQF4J584l1nFG0yH6vNQsbaplP5qh1MU4k0g-6tvg_LSutZaifHXJYphH9-jfJURLfkhs_mY85Iw5Me-E_lxAoqINn3_WhEfgnVPbnwczSRDpcmv8Ewq3htdHT55UGp8UchzWByoYLCw_-mS87BzYAeHXAbPy7AZYwqP_s0ccDo7F8DlH71Fio0NSjA6LB22tzSZcRKbcFaw0bA8uWe8s7O3SiqJLCa-j_XoM7y2PR9jYCdyZRxkugxqb9TW648YWAik-7AIKOIWDVTM7zyjzJv75zfUAnzphGnwK31SjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏اعتصاب عمومی در سنندج و شماری دیگر از شهرهای استان کردستان ایران آغاز شده است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23256" target="_blank">📅 11:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23255">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : هیچ هدف‌گیری‌ای داخل شهر مکه مکرمه صورت نگرفته است. دو پایگاه هوایی در نزدیکی مکه قرار دارند: پایگاه هوایی ملک فهد در طائف و پایگاه هوایی ملک عبدالله در جده. هواپیماهای جنگی سعودی از این پایگاه‌ها برای انجام عملیات و بمباران در یمن پرواز…</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23255" target="_blank">📅 11:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23254">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رئیس‌جمهور ترامپ: راستش را بخواهید، عمویم احتمالاً بهترینِ تمام دوران بود؛ او ۴۱ یا ۴۲ سال استاد دانشگاه ام‌آی‌تی (MIT) بود و به عنوان یکی از درخشان‌ترین افراد شناخته می‌شد. بنابراین، اگر به «نظریه وراثت» (یا قدرت ژنتیکی) اعتقاد داشته باشید، من هم از چنین…</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23254" target="_blank">📅 11:06 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23253">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23253" target="_blank">📅 11:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23251">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QORi6FVSXr5Bj9twe-cn8cdGDxZJeJCKIroQiCba9RCVwbQvTY4OWLh8NhfIl9lbYkspm7BkBW0PEFwsNiRqTuiaTYuPeUKf3jlTVIqCmHhvzbVlgKMh5M_zmNYGyoaI38bwDEWo_tMUmxe21zQa2A_wlzG-FKXNB3_cpksXWoGVLxeV5E912lcxR6uj9Yrat69XkzAQHeUkpapv1DdamoZYSKaHveEhfjkYdA4X4srQwmRhmNmaZWtftJV96IHhitANf3dwS9Wcbx9K1-EOPEAsebLLkGudhyDGUniMN5pUmcNuf8d7j20GE7fzEg6kfyV1JDBEXcl8ZYoCY03v2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e27cc230e.mp4?token=PV9namPFhxkTYXRAk9ZE_FINGzILoea8JNvloYbJ-8rjBU5iZe15Y0W1Tr0H42VZBHy6hURa_hm-hgOatUVFxfEJIncwBK3S0gkwcilsrn8eVXp7lhUmSrCkEdp_v6qFMlukG5bB-2pBF2OCpc70Q01saprgz1Oc5Pz-86068SrOE-qwtV6PYo9ZjbU7t_n25Gpgy32j02OW2weFBMg41O1nEOFlBDhSp-V1bxRwIXiVCB-fqVstI9NmDLSj_V_9rTXFsUtQv63caavR_8N3le-K9XO-c_PV2ywH4b3QBR2SVEIl8-8hxnpLC9BOPMhhemWIKPVWmKxgFE_yR5f8qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e27cc230e.mp4?token=PV9namPFhxkTYXRAk9ZE_FINGzILoea8JNvloYbJ-8rjBU5iZe15Y0W1Tr0H42VZBHy6hURa_hm-hgOatUVFxfEJIncwBK3S0gkwcilsrn8eVXp7lhUmSrCkEdp_v6qFMlukG5bB-2pBF2OCpc70Q01saprgz1Oc5Pz-86068SrOE-qwtV6PYo9ZjbU7t_n25Gpgy32j02OW2weFBMg41O1nEOFlBDhSp-V1bxRwIXiVCB-fqVstI9NmDLSj_V_9rTXFsUtQv63caavR_8N3le-K9XO-c_PV2ywH4b3QBR2SVEIl8-8hxnpLC9BOPMhhemWIKPVWmKxgFE_yR5f8qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : این ویدیو قدیمی و مربوط به سال ۲۰۲۵ است؛ زمانی که پدافند عربستان موشکی را که از یمن به سمت اسرائیل در حرکت بود، سرنگون کرد. نکته خنده دار این اصلا مکه نیست، بلکه مدینه است!!!! خاک بر سر ادمین های زرد بی سواد
😂
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23251" target="_blank">📅 10:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23250">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amu5shG-YTFzyfz8PGvpxn9aue8loqUyZbmxgUh-KTMmF7e07pZBCpHmKPL9zf_uh2K7HysRd7QNT_5OxuvMofR43bjXsA5QzHb3CsR-LqzuhFAs7lu3FpekBD0tXjghz9xAts9mD1XRMeiEIzrI7l4HiGacUOmVWVUZ9O6xbPU8ooQKz44ba2GHKCucY_LlqDUIVCMmmEHS6G6ft7QZEOLZh5-fb209Bsc5IIw-iCjcQikJNQy1xtoJmvme_hV9tu06DMIg2D0ZW6Od_fgMWJxpy4kApFsZBtxjIhwg-uU5NqpQgqBxQIxqiez9TNMGj1EDg0VsBh4IfhgabkEDGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نظرسنجی جدید کانال ۱۴ اسرائیل: لیکود به رهبری بنیامین نتانیاهو با ۳۰ کرسی همچنان بزرگ‌ترین حزب است، اما یک کرسی کاهش داشته؛ حزب «یاشار» به رهبری گادی آیزنکوت نیز از ۲۲ به ۲۱ کرسی رسیده است. شاس ۱۰ کرسی، دموکرات‌ها ۹، صهیونیسم مذهبی-زهوت و عوتسما یهودیت هرکدام ۸ کرسی دارند. حزب نفتالی بنت و یهودیت متحد تورات هرکدام به ۸ کرسی رسیده‌اند و اسرائیل بیتنو از ۷ به ۶ کرسی کاهش یافته است. در میان احزاب عرب، حدش-تعال-بلد از ۶ به ۷ و رعام از ۶ به ۵ کرسی رسیده‌اند؛ مجموع احزاب عرب ۱۲ کرسی باقی مانده است. در سطح بلوک‌ها نیز راست ۶۴، چپ ۴۴ و احزاب عرب ۱۲ کرسی دارند و موازنه نسبت به هفته گذشته تغییری نکرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/23250" target="_blank">📅 05:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23249">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وال‌استریت ژورنال، به نقل از مقام‌های آمریکایی و منطقه‌ای مطلع از موضوع: نیروهای آمریکایی برای مقابله با حمله موشکی بالستیک ایران به پایگاه‌های آمریکا در اردن که هفته گذشته با حدود ۲۰ موشک بالستیک انجام شد،
۶۰ تا ۷۰ رهگیر MIM-104 پاتریوت و بیش از ۱۲ رهگیر تاد
شلیک کردند. مقام‌ها همچنین به وال‌استریت ژورنال تأیید کردند که ایران در این حمله از
مهمات خوشه‌ای
استفاده کرده و برخی موشک‌های بالستیک از سامانه‌های دفاع هوایی عبور کرده و به هواپیماهای نظامی، از جمله جنگنده‌ها، در پایگاه هوایی موفق‌السلطی اصابت کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23249" target="_blank">📅 05:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23248">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کانال ۱۴ اسرائیل : ترکیه به یک شریان حیاتی مهم برای ایران تبدیل شده و به تهران کمک می‌کند از فروپاشی اقتصادی جلوگیری کند؛ از جمله از طریق ارزهای دیجیتال و مسیرهای تجاری زمینی و دریایی. بر اساس اطلاعات منابع اطلاعاتی، ایران همچنین ده‌ها میلیون دلار را از طریق کریدور ترکیه به حماس در ترکیه منتقل کرده است؛ در حالی که تهران برای حمایت از نیروی نیابتی خود تلاش می‌کند.
@WarRoom
🚨
🚨
🚨
🚨
مارک لوین با بازنشر این خبر : اردوغان در حال تأمین مالی رژیم ایران و حماس است.</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23248" target="_blank">📅 04:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23247">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">معاون رئیس‌جمهور، جی‌دی ونس، درباره ایران: «ببینید، رئیس‌جمهور ترامپ روی کار آمد و بله، او می‌خواست آمریکا را از درگیری‌ها و گرفتارشدن در مناقشات خارجی دور نگه دارد. اما او همچنین گفت که متعهد است اجازه ندهد ایران به سلاح هسته‌ای دست پیدا کند. به نظر من، اینکه…</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23247" target="_blank">📅 04:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23246">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/660d9d9e22.mp4?token=WlLJ-pxxKQNirNMW6IH4ezcj4bB5AHufI3uBvKolgsXusfZOq_3xBqZBGmiNXEaW2VrvqFTjINPY5TIoCc6hnotYtN4bizSMKh8oi_wdU4xsn6hQVb8gOcfMlUeGzVnZMbnBrQJwRW1sqFRw2GnDYWeY2RQAcb6AwluwpApwGw_wgpVv9egso6z9qi8TKXWiP3wIhMfGeaGBjX5sUTCvoh52vmv3kyBdBSAuQeP1TH9XLFPaoLMup7HZdpGrNFrVXg4JpXy_joMyOeyXBm-JpqhYjKKqbwc6DfpJHseZZlZ6AiIbPICn09GJrtP6A8SokU9MsfnX7kFHaUdRgfcACA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/660d9d9e22.mp4?token=WlLJ-pxxKQNirNMW6IH4ezcj4bB5AHufI3uBvKolgsXusfZOq_3xBqZBGmiNXEaW2VrvqFTjINPY5TIoCc6hnotYtN4bizSMKh8oi_wdU4xsn6hQVb8gOcfMlUeGzVnZMbnBrQJwRW1sqFRw2GnDYWeY2RQAcb6AwluwpApwGw_wgpVv9egso6z9qi8TKXWiP3wIhMfGeaGBjX5sUTCvoh52vmv3kyBdBSAuQeP1TH9XLFPaoLMup7HZdpGrNFrVXg4JpXy_joMyOeyXBm-JpqhYjKKqbwc6DfpJHseZZlZ6AiIbPICn09GJrtP6A8SokU9MsfnX7kFHaUdRgfcACA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس‌جمهور، جی‌دی ونس، درباره ایران: «ببینید، رئیس‌جمهور ترامپ روی کار آمد و بله، او می‌خواست آمریکا را از درگیری‌ها و گرفتارشدن در مناقشات خارجی دور نگه دارد. اما او همچنین گفت که متعهد است اجازه ندهد ایران به سلاح هسته‌ای دست پیدا کند. به نظر من، اینکه بخواهیم آمریکا را از درگیری‌های خارجی دور نگه داریم،
به این معنا نیست که هرگز نمی‌توان از نیروی نظامی برای تحقق اهداف مردم آمریکا استفاده کرد
.»
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23246" target="_blank">📅 04:14 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23245">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fwd5D4WmZKDXfpVVwlPq_QwAS0lK-4ULObv68yCutqkYe__evZBQsLLyKzzU3xowfFJ6YFRg99WxNe7SN0BTAhyW4J79GJpZS_BTKnuZpvFUHgfQtQmXnHrHgrOFSoSVHQaqybvXnmZFXPV_TDekul4ou7-omI1QL27bYNqZ1xgSl8SGgl_da6s4bHHWhELKz1YbMr3gshCdtnuatvaEKsjExxpQmuHzT_QI1m2nNLTiDmO9ljBx9atFAdBNye32TwXMLUrn2CwztMkEN79OD1MTy-m_H-JfYKd6-eBfDGukKUcTPuirb1SJjihbsMnHe7mq0QiMtXwkEaDT1M2dOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفارت آمریکا
در ریاض سطح هشدار سفر به عربستان سعودی را به سطح ۳، یعنی «در سفر تجدیدنظر کنید»، افزایش داده است. در این هشدار، به خطرات ناشی از حملات پهپادی و موشکی ایران علیه منافع آمریکا، درگیری‌های مسلحانه و تروریسم اشاره شده است. این هشدار همچنین درباره احتمال ممنوعیت خروج از عربستان و خطرات مرتبط با قوانین سعودی در زمینه فعالیت در شبکه‌های اجتماعی هشدار می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/23245" target="_blank">📅 04:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23240">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cHrTlzLlD2DOMVg6x0Mkz7fA9XQO88M4IEYNuZyly2kDpTZst5--sZdi7orghnsHbn1Nn6kGBRWG3PLupQfN3ZrrRrAKo8Ivg0DcnbO4UFthyW1ZeqT9c95JKmXRu4W8mSL2Ya2z1aNGGto_8VlBsQWFnOpMxaYBDgWBBdrLz2GGlCBmnNWARhot6snOurMpdaNv3zulFLDiUX3oRLE2YYmrLvyd40Vf6tdlWh9UX1BAl0Sw-Hr5aVxEd9R14kVTxZoyPv3LqAYrh8mzdKklgfUREA4-xEKikkzOG8qME0924GVPZwsrDaeVDs-nsI3CQDMFUaiT6nxt9spNeAvaiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NDi-gSNlYxK_HPCUYZD25K96y-6nVp2xNFloJZ30nzsgSGjQg8odPkSXCxuF4K97TJwf_TJ_TMPMtTV9WuAkUy2Mp0o61mC4fdzHtGojhdW_IhzRCGEUx72iCkP6GjDNWU9QTsvrVPjdgqMZdb6nPBwwaYPwBR-rFxtzFvFvzljrjCxSYhSUYRH8L_FRwqevwiWB6fWC2kn-11HlDiIbhsvuBSZOsVM3r6AXQaocVVrBrgoVs89N8skDC4R8NAWCBeITWZgKDuDoiL5x2EudgXyd1KjClz8xB1sX6QSJCX99ns7dFMaaJx2Y5e30Q9p698RIFu9-7N_9ALYbdv1alg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rORYUDrcnTrMvLb17ObCySeqJNgm6krE7RXORPVmv4qj04pDvMWb0U0sfr8Pw6CGDypM7_UhS1AXGSbAT8rE24iSEpZuibMDAoPzjwnS8ZECa1aZZ_kKM-tATqi5dq3KkirN4RPi1VwhNRKMXdH99ZG8smQ5DhkHpNw4Urx5SZaaxJItCAPa0nhNvQbxkt3Kr2pV2z7vvbgPy3vm-F5gyyjUHLXUIv6l5cAq8vixNzsjrFq64Z9Wxwd5oXX7eSXfr7ho2OYIhSBNDlz7rNk1AKy9TN1u59JpJUZIBb_m6k9alYDyMwwF2jpnV8fmBlBZXHQUx6aFFLtICxMO6VMjMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SGFSyGmus-B4QBVOQCru4ssHBhTjv9IbJUl8seoF93bMpEFOD_6abBw5aNJ9j6omVKNLCaWjJPbWa5ofML6GXW46vik5ifyL8YzDKl4ZZn5pjIVkShakQZqcF_p2k78XIvmrMamHG1w17XnXm-Ec5P-ryjoTBc_wEgV7rtQYe_WFIZcrIx89XpHlrqTOhXM3fz8So8rUmVVtxGjenQzAmBSJSNRXIILTgxe8_4bULeP4DXjvluUHMT50X_cdcFnnV7PeU2_wOwa90aq1D4ptGbev02xojxOCvCbO-rvMzq1Xe6N206JoaZvsQ4Q-vQPvSueS9vWEiHTR3AF4bFI7bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CL3pYOOFt1YALSXvRSFLZMp1TnnurBMa9fYMyW3Sfx2ZW-06A_diy2MOqyXrICpOb7IsaWVMh1TKG70Z-QqSRWAMHvHyzLwR2hJ7bnGQHFra1j_hNAWHKQop0O0Mi5_BDYR6SRf5I8nCoBBeXB8xCAB2yQbZ9AwHQrjLnjR8SYm4WSuYsyWeeBzHNxsCpjQlL_EJ_jI9OHSV1h83D0QkJcrkf3RRx6xV9m7_Xh2v7EU4T40BP0oi_1zKwtEBRVmtLoAGS967FagvgtMcYAQYlb4cBXUgc-qRrFLPYQAPWgTEcNYWKu4gGVjg0xWl8uZYxP8VkjvCjadIZ5zdpuzW3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر جدید، خسارت گسترده حملات موشکی و پهپادی ایران به مواضع آمریکا در خاورمیانه را نشان می‌دهد:
تصاویر اختصاصی که توسط چند نظامی آمریکایی و به‌صورت ناشناس برایمان ارسال شده، آسیب شدید به پایگاه‌های آمریکا در
عربستان و کویت
را نشان می‌دهد. در یکی از تصاویر، یک فروند
هواپیمای آواکس E-3 Sentry
در پایگاه هوایی پرنس سلطان عربستان دیده می‌شود که بخش پشتی و دم آن بر اثر اصابت منهدم شده است. تصاویر دیگری نیز ساختمان‌ها، خودروها و تأسیسات آسیب‌دیده در کمپ بوریحینگ و کمپ عریفجان کویت را نشان می‌دهد. همزمان، گزارش جدید بازرس کل وزارت دفاع آمریکا از
تا ۳.۷ میلیارد دلار خسارت تجهیزات، شامل نزدیک به ۶۰ فروند هواپیما
خبر داده و تأیید کرده که حملات ایران پایگاه‌های آمریکا در سراسر خاورمیانه را هدف قرار داده است
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23240" target="_blank">📅 03:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23239">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bada91535.mp4?token=dnGCLwn8NiiXaZXSTdLVkCdeTvB2tpe6eUZos_2P_yY-w326IpzQXL6P2-RDX5nEl6NLn4qYlGfp4PQyJhFUTn2TCJrTmsrYWtKF9vyswdtx-afanukJ2CXr5cN1yxlATHH7Zm3b6CWgYN0Azak1cHNytnkoYhEoDmi28jQLUwUfRMvU2lIYtoZ_kKlPCzLVmG7kb1IigyYWKNwPAW4yRTrXSOWH_Yhpgf0vMeXphvKn-XtyJXL109Fu0hlIjcuD-xJnukfCJbnWslMa8XW_S3io3S7gdOJ8xw3ukrYZxCY5O8ZogaFbC8cGjcFukjxrl6jNAQPHCouFfxZz8yTqEjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bada91535.mp4?token=dnGCLwn8NiiXaZXSTdLVkCdeTvB2tpe6eUZos_2P_yY-w326IpzQXL6P2-RDX5nEl6NLn4qYlGfp4PQyJhFUTn2TCJrTmsrYWtKF9vyswdtx-afanukJ2CXr5cN1yxlATHH7Zm3b6CWgYN0Azak1cHNytnkoYhEoDmi28jQLUwUfRMvU2lIYtoZ_kKlPCzLVmG7kb1IigyYWKNwPAW4yRTrXSOWH_Yhpgf0vMeXphvKn-XtyJXL109Fu0hlIjcuD-xJnukfCJbnWslMa8XW_S3io3S7gdOJ8xw3ukrYZxCY5O8ZogaFbC8cGjcFukjxrl6jNAQPHCouFfxZz8yTqEjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا درباره ایران:
«ما شاهد شلیک ایرانی‌ها به کشتی‌های تجاری حتی در جریان مذاکرات صلح بوده‌ایم. فکر می‌کنم رئیس‌جمهور ترامپ در اینجا کار مسئولانه‌ای انجام داده و تلاش کرده اطمینان حاصل کند که با وجود اقدامات ایران، جریان نفت و گاز در بازارهای انرژی جهان ادامه داشته باشد. اگر آمریکا به خاورمیانه بگوید “خودتان از پس خودتان بربیایید”، تا زمانی که ایران به شلیک به کشتی‌ها ادامه دهد، نتیجه آن ناگزیر یک
بحران جهانی انرژی
خواهد بود. رئیس‌جمهور ترامپ مسیر مسئولانه را در پیش گرفته است. او ضمن حفاظت از منافع و دارایی‌های آمریکا در منطقه، اطمینان حاصل می‌کند که بازارهای انرژی جهان همچنان به عرضه نفت و گاز دسترسی داشته باشند.»
@WarRoom</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/23239" target="_blank">📅 03:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23238">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">رویترز: بسنت می‌گوید آمریکا با چین درباره فشار بر کشورهایی که به ایران کمک می‌کنند مذاکره کرده است. وزیر خزانه‌داری آمریکا گفت واشنگتن در گفت‌وگوهای خصوصی با چین درباره برخورد با کشورهایی که از ایران حمایت می‌کنند پیشرفت داشته و قرار است آخر هفته با هه لیفنگ، معاون نخست‌وزیر چین، دیدار کند؛ این موضوع احتمالاً در دیدار آینده ترامپ و شی جین‌پینگ نیز مطرح خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/23238" target="_blank">📅 03:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23237">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">For Terminators Only
@WarRoom</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/23237" target="_blank">📅 03:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23236">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/23236" target="_blank">📅 02:59 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23235">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23235" target="_blank">📅 02:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23234">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAli</strong></div>
<div class="tg-text">سلام داداش یه چیز میخوام بگم که البته به من مربوط نیست ولی چون واقعا دوست دارم باهات حال میکنم میگم گفتن این خاطراتت به نظرم من جالب نیست به چند دلیل اول یه قشری که ندارن دیگه باهات همزادپنداری نخواهند کرد دوم که من نمیدونم و قضاوت نمیکنم ولی به ظاهر چون بیشتر ما شناخت نداریم ازت به دور از واقعیات میرسه و سوم بردار من از قدیم گفتن درخت هر چه …..و به نظر من با این مسائل داری از هدف اصلیت دور میشی چون ما تورو به عنوان یک لیدر میبینیم امیدوار متوجه حرفام شد باشی و ناراحت نشی
🙏
🙏</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23234" target="_blank">📅 02:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23233">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">تحولات بسیار قابل‌توجهی در خاورمیانه در حال وقوع است و احتمال یک تشدید بزرگ و جدید درگیری‌ها مطرح شده است. در طول امروز، جنگنده‌های اسرائیلی در چند نوبت وارد حریم هوایی ایران شدند، بدون آنکه حمله هوایی انجام دهند؛ اما این پروازها موجب فعال‌شدن پدافند هوایی…</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23233" target="_blank">📅 02:16 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23232">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23232" target="_blank">📅 01:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23231">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23231" target="_blank">📅 01:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23230">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23230" target="_blank">📅 01:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23229">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23229" target="_blank">📅 01:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23228">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23228" target="_blank">📅 01:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23227">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tP8zuh_AN-ww2OnqJeJsWfKVIpKPTu1FCsEYzAK0fiGl7j3wjkM8MiUFpCbPMMrAShqPOwCIqHBgbWrKH3jNhB9bpUCTtDSJxzsY2R2iA6cmvnjJIwexMho44o78G2q9fRBCh_Y_CbCMa1qmaqQJGki9BpUyBJaKr7inhwoDRp-dB3oQh1ar8vAyto_jluQMcC48NSJHlcEhn_iBCSsLkk73W9-tby07sx0MFPNRIf_bOe93_4Mfpauj6lB9NVteD9BAzZrNoG5eYLBIFbdu5_oJzCMfCCiGOOiqpbalbzNMYbyS5N2_QdaD3IeyJpc8_yk9lpHWyd4ifHIrzkElSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر نوری، بازیگر چند روز بعد از انجام مصاحبه‌ای و اعلام پولدار بودن ، در پی یک حادثه رانندگی در یکی از بیمارستان‌های تهران بستری شد.
طبق آخرین اطلاعات منتشرشده از وضعیت پزشکی، سطح هوشیاری او پایین است ولی در مقایسه با ساعات ابتدایی پس از حادثه افزایش یافته و شرایط او از این نظر بهتر شده است.
با این حال، روند درمان هنوز به پایان نرسیده و پزشکان با توجه به آسیب‌های ناشی از تصادف، انجام یک عمل جراحی را برای او در نظر گرفته‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23227" target="_blank">📅 01:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23226">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoLOKjvh6X5PU7kHc5ssykAaKCtLIx8rRbVSZQ_O_e2rRe_G9C2c43jD0Zjm5jltgUKbfMh_49h2eAjkFwqnolsx7_GCHrbNRzFcuKJYtQ5w-d5rweHBJ4dG6bqGjPK_gIWtXt60NmPKXo7hPu1LkKafwynOXrXrE7C_w_-HvpdC2-b4q5ClO_dv9wOh6ZF-MAdMz7L5CiilVUnYhA1Qngv55BfNr8eVIx-QeCdPBiRgzEizlT9hU8soFC_V0d0_FZQoh0RbxhGP12IH3nwHahtCh4DIs2cxeBvOKy4n1E5p8srFRhcsUW3xwGUmxWHXewcPp3ZAXUn6n6ck0u8mzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحولات بسیار قابل‌توجهی در خاورمیانه در حال وقوع است و احتمال یک تشدید بزرگ و جدید درگیری‌ها مطرح شده است.
در طول امروز، جنگنده‌های اسرائیلی در چند نوبت وارد حریم هوایی ایران شدند، بدون آنکه حمله هوایی انجام دهند؛ اما این پروازها موجب فعال‌شدن پدافند هوایی ایران و مهم‌تر از آن،
تخلیه و اعلام وضعیت آماده‌باش در برخی پایگاه‌های سپاه پاسداران
شده است. از سوی دیگر، هفته گذشته یک نشست سطح‌بالای نظامی در آلمان به ابتکار
دریاسالار برد کوپر، فرمانده سنتکام
برگزار شد که فرماندهان نظامی اسرائیل، آمریکا و کشورهای عربی منطقه از جمله عربستان، امارات، بحرین، کویت، قطر، اردن و مصر در آن حضور داشتند. این نشست به‌صورت محرمانه برگزار شد و به گفته آکسیوس درباره
جنگ با ایران و افزایش تنش‌های منطقه‌ای
بود. با این حال، هنوز مشخص نیست این تحولات مقدمه یک عملیات جدید است و
نشانه قطعی و مستقیمی از قریب‌الوقوع بودن حمله جدید وجود ندارد
.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23226" target="_blank">📅 01:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23225">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdjbiCRnvaE4AXbdkOudn3tGN69fMNjMLpSTcuxbecI3ki2OwZnnL9ValRnzftqODHb87hCyjryuukB-yxIluz86-9tgM5iw1r1OT-cwXt9LMCrKWDyxldT-dPRTo3_UKdT3ss3Ng9MQ247yEfBKCRWEdwZ68dXHovmHL8JVxJ0exYy0_MM8uFbgjbCQsmZzTIpRw_ooSF2BTusBkG9zJrf-4remRNI4LyQhU0onr9xZUSxS7bsXdELlDXgixulyIAxwCyRw_HlasPjZ45eHh_63ix0WYqzxH3JGy0z3dWKxNivlu1FDhtdpf3IftHV0YxJMtpFA7P9v8dniO07Bgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادر ابی رئیسی                  فوت کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23225" target="_blank">📅 01:09 · 25 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
