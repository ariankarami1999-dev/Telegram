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
<img src="https://cdn4.telesco.pe/file/lrwVBpeIKeEicp3YX4wDP_i2gOYKbdoo_gXW89bHRZgskEmRVv7AfJ6DP6G2vN5HoQfO_Ybb39DOrNXXtUovlmlAILJcUchy8VeJ_iN_YysOEfLk1GZTQADXow2eMs-A2NZ9Pf77nggC2ENZpHwmKK1NXmvAaISnd5yaCzqDZbceC4AyG-JqSamQmq4P9_2i3WtZ74ZSIFd4ZboorUEr5g1JuAEuYlnkwiy-xSkCe9dQLG0GBXGCZvE8fjG_PiZWWFjf1MFg7NDQwpNP9KAuw0IoZmblBP6ECVTQsCQDRRH_Mmolzzhqk3zbMdmVI-uzEubEF1qxKQD3NOKzTRNANA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 106K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 08:42:09</div>
<hr>

<div class="tg-post" id="msg-72021">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f75dfbec.mp4?token=CPmHGB-VPHDDzKe0FFhATXdqLFCG_Z5SOeJbiML0Xrc6yPEzBXgfpkqzHGfBeNVdjgJ1GeHv6bDF56A72_0m-oa7RuGhGGTDSlAW5AHUTJoe2IwaKizU8_UPftgVBP_dyj2YEolZ6zabq00e8FCHSYf6jzSv24WHfT518SlimCccPZaJxPjmd-USAvEPbWMMukDwO9zJnzASQj4tgyb9xRASSvfCFTpa1SPIuKdL5c5bJdL_r6N-1CCjftJtv4C8l6kTIM3AZsdd-Bk2YzOi5Cg2pk2K39D28tirxmhYO6e55fPUnD-5uAWX9VIq10CzXSsHGYvqzT9ods22pKu9kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f75dfbec.mp4?token=CPmHGB-VPHDDzKe0FFhATXdqLFCG_Z5SOeJbiML0Xrc6yPEzBXgfpkqzHGfBeNVdjgJ1GeHv6bDF56A72_0m-oa7RuGhGGTDSlAW5AHUTJoe2IwaKizU8_UPftgVBP_dyj2YEolZ6zabq00e8FCHSYf6jzSv24WHfT518SlimCccPZaJxPjmd-USAvEPbWMMukDwO9zJnzASQj4tgyb9xRASSvfCFTpa1SPIuKdL5c5bJdL_r6N-1CCjftJtv4C8l6kTIM3AZsdd-Bk2YzOi5Cg2pk2K39D28tirxmhYO6e55fPUnD-5uAWX9VIq10CzXSsHGYvqzT9ods22pKu9kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ سی‌ان‌ان، ام‌اس‌ناو و پولیتیکو رو به خاطر «فیک‌نیوز» از کاخ سفید ممنوع کرد.
فاکس‌نیوز + ABC، CBS و NBC در اعتراض، پوشش تلویزیونی مشترک (TV Pool) رویدادهای ترامپ رو متوقف کردن.
نتیجه: مراسم‌ها بدون صدای زنده پخش شد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/news_hut/72021" target="_blank">📅 07:35 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72020">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72020" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/news_hut/72020" target="_blank">📅 01:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72019">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMVROq-CC8O0zdQ1cVMoWw_HoVHez-oGGftX1DM3pREWgZTMC6Wt-n278ZduH94NxvqnML7yIXrT9pLLGYxiCRJJgv-Pvgjl9zyfPBtqzP7lnhTH7b3AzveDndU5SpmqazD-GI7qw8fZlbQBWjbefG2Ya2uOTZDW6lb0CZEQnk2yVc6eAZN65ql4_NUtHIWn9WuWiZUlFxeyp-K2mt0kITy391_S1uRvxSrDBM2L8vtI3BhH2wkvc-Tsjtrplk9qb4nHYohd7gzEqdpnU-1F2huNRmM580iBfiFCrirFSfVQrgXyeFG79G0lnkBg8ZjiszlDhmQxVUBSJjVYKjrIgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/news_hut/72019" target="_blank">📅 01:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72018">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d99b0ae83d.mp4?token=JOFKBSZeA4TXeyZZ0XupZF_ko8SE1JpcvF-6FRgMFddY5mvAJam46cGBumle3oCBnb0lX3SmqO8Jrfjho1j-Wmk4Ff279KCLQV6xSopEKAh1vInBjozIkuZ59PvchBM8q645zqt71ZCKKYrhzPReHml9lky-K0-yCCpqMQjoCD-EJf7KxfC4412_1OhnLz9MI_3zOClA8IxSi58AZeQ6jBYOWEfm3FOnTELIw18a0BxZNZQhckhVfBzp0BuKsx9hpmIBnb3sU46XN8jfuR5Rxr8krPFcdHOa1aNYrd7RjEWPeBIA_cfa7tA3gg5LlmOqsirm3HRkODq7GvJhINRRrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d99b0ae83d.mp4?token=JOFKBSZeA4TXeyZZ0XupZF_ko8SE1JpcvF-6FRgMFddY5mvAJam46cGBumle3oCBnb0lX3SmqO8Jrfjho1j-Wmk4Ff279KCLQV6xSopEKAh1vInBjozIkuZ59PvchBM8q645zqt71ZCKKYrhzPReHml9lky-K0-yCCpqMQjoCD-EJf7KxfC4412_1OhnLz9MI_3zOClA8IxSi58AZeQ6jBYOWEfm3FOnTELIw18a0BxZNZQhckhVfBzp0BuKsx9hpmIBnb3sU46XN8jfuR5Rxr8krPFcdHOa1aNYrd7RjEWPeBIA_cfa7tA3gg5LlmOqsirm3HRkODq7GvJhINRRrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، برای شرکت در مجمع عمومی سازمان ملل وارد نیویورک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/72018" target="_blank">📅 01:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72017">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e2686a0e6.mp4?token=japXbHE4KBLcRGCm2j7-waFEEMlkR_k6R8zAT5wOQvzIsHkA4LrdXF3QZhtRY235SyXkNb3_vq2U25QK2igifXnmipB4HXq0TMy-Zn-uq7UR-rJbhvbeakNsfJghKbTiHUSX-R3p00EGiv3mr4HQxXqMA1Bn7dz3nH3fb9ojWHyI6NG0Wwmj_upV99xSnL0vzEDnmFB3tGtHJkDY3nKJ5n-jRVRk-wYslLaDmUbAf3-8oZTB-lShNiXCZ70jlONQ4AsdODi_IdVo8cH94RiCx-Uxm1uRLcyuU68Lvs-_s1d1adXzItXz0IQo7pl02iJIN2SEXcspPmVsX3hyfKajdUqayfgsKNyfpDQnbwK9FLreQP6xSRwy9LbU1wGClXNMMNkrhxgc0IOssbU1_Pd8ZrlGmPIZWJPUWEIYttqq9srgfbPFjk47ZsQ0h2qUYVlAymJ597SwmOrLy3pnuZi52oM4FwCbEm445oRUqfdOJD-Sj2UKG-P8pM-ksxY7zAFNy2YHk-ES96vNCYH26DZ624HmQ4anuWB0Y1DZmfgmRPh5xyVSUK-w3xuxB6UuQJCEpYhQxiWE_D28lfiuSF2fSPR2rMYzqcogSRcynGAv8BPMlm94buTSU4ynod870lriZa60hmQckKVe1f8WQPXMRBMxLatqOKnM__naLKbyb5o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e2686a0e6.mp4?token=japXbHE4KBLcRGCm2j7-waFEEMlkR_k6R8zAT5wOQvzIsHkA4LrdXF3QZhtRY235SyXkNb3_vq2U25QK2igifXnmipB4HXq0TMy-Zn-uq7UR-rJbhvbeakNsfJghKbTiHUSX-R3p00EGiv3mr4HQxXqMA1Bn7dz3nH3fb9ojWHyI6NG0Wwmj_upV99xSnL0vzEDnmFB3tGtHJkDY3nKJ5n-jRVRk-wYslLaDmUbAf3-8oZTB-lShNiXCZ70jlONQ4AsdODi_IdVo8cH94RiCx-Uxm1uRLcyuU68Lvs-_s1d1adXzItXz0IQo7pl02iJIN2SEXcspPmVsX3hyfKajdUqayfgsKNyfpDQnbwK9FLreQP6xSRwy9LbU1wGClXNMMNkrhxgc0IOssbU1_Pd8ZrlGmPIZWJPUWEIYttqq9srgfbPFjk47ZsQ0h2qUYVlAymJ597SwmOrLy3pnuZi52oM4FwCbEm445oRUqfdOJD-Sj2UKG-P8pM-ksxY7zAFNy2YHk-ES96vNCYH26DZ624HmQ4anuWB0Y1DZmfgmRPh5xyVSUK-w3xuxB6UuQJCEpYhQxiWE_D28lfiuSF2fSPR2rMYzqcogSRcynGAv8BPMlm94buTSU4ynod870lriZa60hmQckKVe1f8WQPXMRBMxLatqOKnM__naLKbyb5o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش خبری فاکس نیوز به نقل از ترامپ:
«در حال تصمیم‌گیری هستم.»
اریک شان، خبرنگار ارشد فاکس‌نیوز، گزارش می‌دهد که دونالد ترامپ، رئیس‌جمهور، در حال بررسی گام بعدی خود در قبال ایران است؛ آن هم در شرایطی که برای دیدار با رهبران کشورهای حوزه خلیج فارس در حاشیه مجمع عمومی سازمان ملل در روز سه‌شنبه آماده می‌شود.
ترامپ در حالی که گزینه‌هایی همچون اقدام نظامی، تداوم فشار اقتصادی یا تلاشی دیگر برای دستیابی به توافق را سبک‌سنگین می‌کند، به فاکس‌نیوز می‌گوید: «سؤال من این است که آیا و چه زمانی کل کشور [ایران] را نابود کنم؟ بهتر است آن‌ها درست رفتار کنند.»
این هشدار هم‌زمان با تشدید تنش‌ها در منطقه مطرح می‌شود. ایران تهدید کرده است که در صورت انجام حملات جدید از سوی واشنگتن، علیه منافع آمریکا دست به تلافی خواهد زد؛ این در حالی است که حوثی‌های مورد حمایت ایران نیز به سمت عربستان سعودی موشک شلیک کرده‌اند.
ترامپ همچنین می‌گوید که برای دیدار با مسعود پزشکیان، رئیس‌جمهور ایران، در هفته جاری آمادگی دارد، اما در حال حاضر هیچ دیداری میان این دو رهبر در برنامه گنجانده نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/72017" target="_blank">📅 01:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72016">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/612f18036a.mp4?token=t3Ocls12Ch-m2DAsSBZYhL3xcHeWbTsaOuzFEeEn68PlTS7F4m0ARS11nGAy1uBKOS2FPy7nE0U900yq7OhVH2_mqJL6omrhuKm6jBgkkW1RH32po6Dz2VkAulHHFpwkzCnaSYD0yHlzD4IH3MDe0d22xpip-68DszNzHF-HtXQTlXcIo2fPjaLhmeyDZgF-bUA4KPjXmA1kMyZAYlrvWTAkCGjj6utsDz80ZpUNkw6TU4prbaJG-qNF33Wx8rZ8iKgNTv_SEmjz5m2rn-L82F2YGmVwSABSOFgp4OuAIVOPTtzF5Y8Sozkrrlij6qZLhJDgcOOF25jAK6RYd7P0JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/612f18036a.mp4?token=t3Ocls12Ch-m2DAsSBZYhL3xcHeWbTsaOuzFEeEn68PlTS7F4m0ARS11nGAy1uBKOS2FPy7nE0U900yq7OhVH2_mqJL6omrhuKm6jBgkkW1RH32po6Dz2VkAulHHFpwkzCnaSYD0yHlzD4IH3MDe0d22xpip-68DszNzHF-HtXQTlXcIo2fPjaLhmeyDZgF-bUA4KPjXmA1kMyZAYlrvWTAkCGjj6utsDz80ZpUNkw6TU4prbaJG-qNF33Wx8rZ8iKgNTv_SEmjz5m2rn-L82F2YGmVwSABSOFgp4OuAIVOPTtzF5Y8Sozkrrlij6qZLhJDgcOOF25jAK6RYd7P0JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ترامپ درباره ایران:
وضعیتشان خوب نیست. در واقع، امروز جلساتی در این باره دارم. عملکردشان بسیار ضعیف است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/72016" target="_blank">📅 01:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72015">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqSixJ_p0xRjmInAUAztuzp89ZSqOqUCMsnftT6Xp6DzH0iX6M6UbiSRyDski2QEKU2stuvYRpOP2Gt5DMwlGL3EI3jUvOgYMPfSN1m9oby3shPuWLKfjktJx9xEjmnGj29xSv5bKK-hGHKSeD_Uc_RjVQBm7GSzF4GckXAV0jPudfCGMs0raUBh_v_cqVxaUY3yGwH3hvOH_fl7n4jzwhdFR7oUoyMdE80ki1cfAyK-KHd64Pl-fNA5-6pWZs1_miM1QHcDSPSgs7UQng8RT6pVoHHMTCN9EtUW3wSZWYQoeerzABDnsISf7ISQ1mQhowubQAYLr_ARRCQbDQ-bQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امجد طاها، روزنامه‌نگار و تحلیلگر اماراتی، با انتشار پیامی کوتاه نوشت:
«اتفاقی عظیم در راه است؛ حرکتی تاریخی و بی‌سابقه. آماده باشید.»
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/72015" target="_blank">📅 00:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72014">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترکیش ایرلاینز پروازهای ایران را تا مارس ۲۰۲۷ متوقف کرد؛
یک نماینده شرکت هواپیمایی ترکیش ایرلاینز اعلام کرد تمامی پروازهای این شرکت به ایران دست‌کم تا مارس ۲۰۲۷ در برنامه پروازی قرار ندارند.
این شرکت همچنین اعلام کرده بازگشت پروازها پس از این تاریخ نیز تضمین نشده است.
این تصمیم در پی تشدید محدودیت‌ها و فشارهای بین‌المللی بر صنعت هوانوردی ایران اتخاذ شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/72014" target="_blank">📅 00:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72013">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GblVJmG04v3yRx_PDH_muhEwr5j4lH1mIbDC0Uc-tj4LvdaL7wzk-QyFHgdgSG5h-1x6QplQ5RF7xWV-7UAgM_0P6BjTpA5xRrA4LEA0NJHyrwJ7Eiv9Ts8eF4xCXNv1AnNGebTh3Gme_EHboAiUHxW0hiGMqG3zRZmMxycgiTn9vcBh-eBaM6ZQoMQ7muMiYtoTgRLBeVy2c35MbpVn7HYQVrF3spZTFd_SaC0yqe8PLhkrlpPT211ukeCjQHmDxBypUMkL4hHkq8dL3wn25QmwfVQV1XGpyYnIIK8C3WzO5vurMkBGxAvTzuGWQMXi-qdiaii6gEcLRaD9KWGGBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛مقامات استان لوبلین لهستان در پی حمله هوایی جاری روسیه به اوکراین، هشداری مبنی بر احتمال بروز خسارات جانبی صادر کردند.
هوانوردی لهستان در حریم هوایی کشور در حال فعالیت است و وضعیت تحت نظارت قرار دارد. به ساکنان توصیه می‌شود منتظر اطلاعیه‌های بعدی باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/72013" target="_blank">📅 00:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72012">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">#فوری
؛حدود ۵۰ دقیقه پیش، هشدارهایی در پی احتمال وجود تهدیدی در حریم هوایی منطقه «کراسلاوا» (Krāslava) در لتونی — که در امتداد مرز با بلاروس و در نزدیکی مرز روسیه واقع شده است — فعال شد.
جنگنده‌های ناتو به منطقه اعزام شدند. هنوز جزئیات بیشتری منتشر نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72012" target="_blank">📅 00:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72011">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59e699259b.mp4?token=hdmdTH2-cNstkLIJh8Zo7VxVAwaHF0ffEnAHKhXNC1YhMkxJ4vHFF5sM6rU-3zE5gbVZTmUFhb-6OfWYIFZID4-gKzJTkOTzZd4NgjaFNRS6Z5-uJ04BdHVrkwRT8IOIexJ7Vhu9Hjhojn-jYYDu95C77WRuwZvxZ2mbTG3GnE-FHVU4F99O703QyyHb0Rs3eIu0pUATuHHgrX2kDfGn6-QyZjedSrSxbrNh5Uhik2miqxJQxF0J-Sdn7Lh2jDljlGHvUzztiDF8x5meSzZSDVonMMdZFCOO-tOCHbutesvkPqoJNOUEH-hQwWESIOiWcdYbbBg6dHIVi7saHJhZxk5dO1calg_KtGoDQWttmejMjm1wtyzF5kdef7Fx7aGYsMLP7SmFv6Bg6BCs4g_5DFRNgoR7NYNrbV5iypVSkvaNoc5EgL9YbJz4zNcS1UqfwTCp-hiAuxPxlWKit6RVD51_soNlJl0b9REvipuGagNL5sFG7KFd_w7DsfnXLrfrDF0N3ka0UcMpiXpua7ksKbyrtwuMwWJZlo8UKHl1D0jJ1UV2ZbWGxHk8bRKDku2opgd4HaDTHcpC1ljEdrFuBE3Zr3cLpC7rQ_uCMqqxvcoaGUsgnnXd76dVcW5LWBMN_9F9u82x1-qbFmIXDXSY6p-2zDJ8bifLSjimYKVMhY0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59e699259b.mp4?token=hdmdTH2-cNstkLIJh8Zo7VxVAwaHF0ffEnAHKhXNC1YhMkxJ4vHFF5sM6rU-3zE5gbVZTmUFhb-6OfWYIFZID4-gKzJTkOTzZd4NgjaFNRS6Z5-uJ04BdHVrkwRT8IOIexJ7Vhu9Hjhojn-jYYDu95C77WRuwZvxZ2mbTG3GnE-FHVU4F99O703QyyHb0Rs3eIu0pUATuHHgrX2kDfGn6-QyZjedSrSxbrNh5Uhik2miqxJQxF0J-Sdn7Lh2jDljlGHvUzztiDF8x5meSzZSDVonMMdZFCOO-tOCHbutesvkPqoJNOUEH-hQwWESIOiWcdYbbBg6dHIVi7saHJhZxk5dO1calg_KtGoDQWttmejMjm1wtyzF5kdef7Fx7aGYsMLP7SmFv6Bg6BCs4g_5DFRNgoR7NYNrbV5iypVSkvaNoc5EgL9YbJz4zNcS1UqfwTCp-hiAuxPxlWKit6RVD51_soNlJl0b9REvipuGagNL5sFG7KFd_w7DsfnXLrfrDF0N3ka0UcMpiXpua7ksKbyrtwuMwWJZlo8UKHl1D0jJ1UV2ZbWGxHk8bRKDku2opgd4HaDTHcpC1ljEdrFuBE3Zr3cLpC7rQ_uCMqqxvcoaGUsgnnXd76dVcW5LWBMN_9F9u82x1-qbFmIXDXSY6p-2zDJ8bifLSjimYKVMhY0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هلندی ها به این شکل پرچم فلسطین رو از دیوار کشیدن پایین
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72011" target="_blank">📅 23:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72010">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39a7c63375.mp4?token=mWNruglmY7bRSFUCwXuYKNgmouS5J3CP_tRDsRS3LnQeCwhYHdhDlLG6oFPYGP_wrBf2t_mSV5lCMxgeBM5sfLlWqxnweZm-Zoe7fwfnr_k8OfkjHIPQ0_w_Co9qjwVUhaJXA6WJySzqfaxVRVZsYtqtXiRyFGwTLnEHCoKeBY-fwTNJ2eRn7-Jd8sPPi2Fzmt7xVnZM_A9pqqkJE8p5i2r2GiGFR_arEi81V0l0-13phQCa-cf70PGyhy9pTW_sVBXi-q9Z5Wwc1etuxQTX9oG9wbyNlC_ecR8BHGv7_98Lj6BQo2_tyJZGvF8qnUlQAlkCFCTz53v5yXxAUB2pBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39a7c63375.mp4?token=mWNruglmY7bRSFUCwXuYKNgmouS5J3CP_tRDsRS3LnQeCwhYHdhDlLG6oFPYGP_wrBf2t_mSV5lCMxgeBM5sfLlWqxnweZm-Zoe7fwfnr_k8OfkjHIPQ0_w_Co9qjwVUhaJXA6WJySzqfaxVRVZsYtqtXiRyFGwTLnEHCoKeBY-fwTNJ2eRn7-Jd8sPPi2Fzmt7xVnZM_A9pqqkJE8p5i2r2GiGFR_arEi81V0l0-13phQCa-cf70PGyhy9pTW_sVBXi-q9Z5Wwc1etuxQTX9oG9wbyNlC_ecR8BHGv7_98Lj6BQo2_tyJZGvF8qnUlQAlkCFCTz53v5yXxAUB2pBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پدر این پسر رفته تو اتاقش سیگار پیدا کرده
و پسره هم این شاهکار رو خلق کرد:
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72010" target="_blank">📅 22:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72009">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ مراسم افتتاحیه (بریدن روبان) پد جدید بالگرد کاخ سفید را برگزار کرد، اما به دلیل غلبه صدای بالگرد بر فضای مراسم، سخنان او اصلاً شنیده نمی‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72009" target="_blank">📅 22:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72008">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05f4ea7396.mp4?token=FyreOsYmwtapTf9Jlz4HsdzJZyti2lpuTlsLRb8k20wx8CLU_y_mGy1JMBZDmZkr-XdChIWwKyK6N3G-rZHV5XsqOVF-8Q35DWZsMYgg_kwrfJjZpSKB2tYdIiUPu5MtpDeMu2f3FgJWTWJEeJzJyLekq16Mmp4qp4y7LDSwr8rwA6kbvwJnm4Hqo_Hbz4dsScNMT2IicBsIvqRfDfX7Zb-k59_BC_jn2-PUikD9e8tQb_8jOt06xgGZYbT-hXgEwngI-bt46A3OUl4fSlLZZA0uBEcc4K6_HBD3_9VzIOvB7-1-lCovr7mFVKp0gAQC0vCW6z52i-wb355C8XU7Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05f4ea7396.mp4?token=FyreOsYmwtapTf9Jlz4HsdzJZyti2lpuTlsLRb8k20wx8CLU_y_mGy1JMBZDmZkr-XdChIWwKyK6N3G-rZHV5XsqOVF-8Q35DWZsMYgg_kwrfJjZpSKB2tYdIiUPu5MtpDeMu2f3FgJWTWJEeJzJyLekq16Mmp4qp4y7LDSwr8rwA6kbvwJnm4Hqo_Hbz4dsScNMT2IicBsIvqRfDfX7Zb-k59_BC_jn2-PUikD9e8tQb_8jOt06xgGZYbT-hXgEwngI-bt46A3OUl4fSlLZZA0uBEcc4K6_HBD3_9VzIOvB7-1-lCovr7mFVKp0gAQC0vCW6z52i-wb355C8XU7Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس:
ماه نوامبر پیشِ رو، لحظه‌ای سرنوشت‌ساز است؛ یا در برابر این دیوانگی می‌ایستید و یا با آن همراه می‌شوید. و ما قصد داریم در برابر آن بایستیم و با آن مبارزه کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72008" target="_blank">📅 21:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72007">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9de7ae59a.mp4?token=ANCF9JV5XU_nH2bXOIdWdiiBolBaXCf_0fc77otJCagXOIy58sCWcp_UsnCs9XN6KzsL3-zbcJ5j2fhTF_NbKdUye7CRdVLuQaJbK7WkHuW7QLh5q88XKsv2GD3qJ6VOsxymoNfH2mzOJvZhSDMVbUb9cWLNFfPCRfZPFvHFu21lyhPXUBsZOHrCbzgX-1NeGfy_kAQDpkz6Xw6sB_EPOS9STApyo0VC5UufwQKu2-j54o4QJjy-22R2GTEt6Rt46bJlolYYwr1vkm6YquWVjx4o_5oEcIhcWBeBX4oqKT-pgfBrEazgu9UuIjZyaB1OoY7stpV9VFlz-J9z2b7Mww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9de7ae59a.mp4?token=ANCF9JV5XU_nH2bXOIdWdiiBolBaXCf_0fc77otJCagXOIy58sCWcp_UsnCs9XN6KzsL3-zbcJ5j2fhTF_NbKdUye7CRdVLuQaJbK7WkHuW7QLh5q88XKsv2GD3qJ6VOsxymoNfH2mzOJvZhSDMVbUb9cWLNFfPCRfZPFvHFu21lyhPXUBsZOHrCbzgX-1NeGfy_kAQDpkz6Xw6sB_EPOS9STApyo0VC5UufwQKu2-j54o4QJjy-22R2GTEt6Rt46bJlolYYwr1vkm6YquWVjx4o_5oEcIhcWBeBX4oqKT-pgfBrEazgu9UuIjZyaB1OoY7stpV9VFlz-J9z2b7Mww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ونس:
این انتخابات میان‌دوره‌ای، رقابتی است میان کسانی که معتقدند این کشور باید آینده‌ای داشته باشد و کسانی که ترجیح می‌دهند شاهد نابودی آن و بازسازی‌اش از پایه باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72007" target="_blank">📅 21:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72006">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0543c701.mp4?token=mwWrvQXsdQf4HUy_8PoiKBrwSk40e-Ga60UvkB4S0KuAWcFNcuqyxBQMSoieC9On8ZHqUeIvzqDCMzYdr2uqdc_2nZ0eoajHBFhFlsr1bTK302mai6vi6m7Q2R9kpCVll-8dzniHhvTk7njBNmZLhr-413imALXN7yVLFLKRwQDtk_oQ8MVhbddYJhO8CtfMVFY_LJm0I7IBvcgMwzkVAmCvy8KZNjA_7IDNPXKXGF1DPGBNZFR13qzBgGmnzLsUUUGrnqkwAtJDXB9eb1is0uFLur4U4Rk9h1PKnGr_hx77Ux7SKciWWQVW7JExMVs60T-lu-UUsbIVAvHQ5sAMJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0543c701.mp4?token=mwWrvQXsdQf4HUy_8PoiKBrwSk40e-Ga60UvkB4S0KuAWcFNcuqyxBQMSoieC9On8ZHqUeIvzqDCMzYdr2uqdc_2nZ0eoajHBFhFlsr1bTK302mai6vi6m7Q2R9kpCVll-8dzniHhvTk7njBNmZLhr-413imALXN7yVLFLKRwQDtk_oQ8MVhbddYJhO8CtfMVFY_LJm0I7IBvcgMwzkVAmCvy8KZNjA_7IDNPXKXGF1DPGBNZFR13qzBgGmnzLsUUUGrnqkwAtJDXB9eb1is0uFLur4U4Rk9h1PKnGr_hx77Ux7SKciWWQVW7JExMVs60T-lu-UUsbIVAvHQ5sAMJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو از آواز خوندن یه مرد ژاپنی خیلی وایرال شده به اکسپلور ایرانیا نفوذ کرده.
و حالا کامتای شاهکار ایرانیا:
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72006" target="_blank">📅 21:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72005">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a929447dff.mp4?token=gp8lfzS19qxjKr9NjUFsGlV8eXS2zRo8uJkTediYVwQOL1MKOEVWn96uGdLy3aG0skmMb3yNvJF90LJEIcEsEMc0w3bQmr34Ya8BkcP2qceXPXMh8rmoTiScHb-FBD_w8qrBqZ_WvMraMPkt1XFziYjLjAvwm5leTLWMLGNmno_qkM43Su0fp5WsS8ODSMKKN4_jzZ-uR5geN35y7lOAb4qFNCIbODOFU_2m67Icnctm3cp_1wxSh28k9nAg3laEYsVQMVpQyNhzp7WZI8yi-Ceol2msffXBCen5fcozKI5A6RlgkgBvENSdxEr8fKaUkok15MAX7FpJIXGv6_biTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a929447dff.mp4?token=gp8lfzS19qxjKr9NjUFsGlV8eXS2zRo8uJkTediYVwQOL1MKOEVWn96uGdLy3aG0skmMb3yNvJF90LJEIcEsEMc0w3bQmr34Ya8BkcP2qceXPXMh8rmoTiScHb-FBD_w8qrBqZ_WvMraMPkt1XFziYjLjAvwm5leTLWMLGNmno_qkM43Su0fp5WsS8ODSMKKN4_jzZ-uR5geN35y7lOAb4qFNCIbODOFU_2m67Icnctm3cp_1wxSh28k9nAg3laEYsVQMVpQyNhzp7WZI8yi-Ceol2msffXBCen5fcozKI5A6RlgkgBvENSdxEr8fKaUkok15MAX7FpJIXGv6_biTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید حساب کاخ سفید در پلتفرم ایکس:
چیزی در راه است. منتظر باشید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72005" target="_blank">📅 20:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72003">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ad0122e6.mp4?token=IrU5ss7i0eZFSfctcPMZuaA5fU8T3HIT6V9WsBHFN5SnzCR6mOgue6NrxEGtjgc_jkwSdekXQjqJy19oVWe34GGRMI7i0gy7M_HntBHlx1QO4Mm_VRYmuu4YzfaA9Jkz5XIEJb8o-Ck409sWVvLGxu20p8FaVSTZCBXHcB2bcDk3NypOApTiAxEaLHjpD3OhFAoHsKT5cRrxT917hWU417erBcbpnouPZoWdMHnsKdDxOhKAldq9huyTATtVpP5ywz-htqQbysEr3ZTzq-_XWRyUf6RPw1Yh5uGvBgEvfZAryBkLYFoLA4DNcW6PQoHg9C4-NeY96YdQH98KbOOEcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ad0122e6.mp4?token=IrU5ss7i0eZFSfctcPMZuaA5fU8T3HIT6V9WsBHFN5SnzCR6mOgue6NrxEGtjgc_jkwSdekXQjqJy19oVWe34GGRMI7i0gy7M_HntBHlx1QO4Mm_VRYmuu4YzfaA9Jkz5XIEJb8o-Ck409sWVvLGxu20p8FaVSTZCBXHcB2bcDk3NypOApTiAxEaLHjpD3OhFAoHsKT5cRrxT917hWU417erBcbpnouPZoWdMHnsKdDxOhKAldq9huyTATtVpP5ywz-htqQbysEr3ZTzq-_XWRyUf6RPw1Yh5uGvBgEvfZAryBkLYFoLA4DNcW6PQoHg9C4-NeY96YdQH98KbOOEcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر ماهواره‌ای حداقل ۲۵ تانکر نیروی هوایی ایالات متحده را در پایگاه هوایی العدید در قطر نشان می‌دهد که بزرگترین حضور تانکرها در آنجا از زمان آغاز جنگ ایران در فوریه است.
این تانکرها در ابتدا به دلیل تهدید حملات موشکی ایران از آنجا خارج شدند و حدود ماه ژوئن شروع به بازگشت کردند.
برخلاف پارکینگ تانکرهای بسیار متراکم مشاهده شده در پایگاه هوایی شاهزاده سلطان در عربستان سعودی، به دلیل اقدامات احتیاطی مداوم علیه حملات ایران، هواپیماها همچنان به طور گسترده در سراسر محوطه پایگاه پراکنده هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72003" target="_blank">📅 20:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72002">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f71861d0c.mp4?token=ng9P0AVe2ORmhhpexhq4WpS9tGHJSRFIr_vDMe-4lebN8DomdOFQ0dcIhVh3cShYCfbb4kNv1k51VTeTu07e7njD8XPqxwK9EJToEzrtmffp2MIR4Uodm38ZtZ1VfrJRsnpq3ZwqJTz5bYv01c-7LebuAbSnHUHjZ5uoKBTvJCLzPfpNHGE2eKIQFKsDDBnBJr0H913_QZ_ymUHzaF0J8uTeBwZKGe5LsKmekLZ-i9Hcm2cBkYy1nBMtMUbBl1R09OL1Th2488QPkboMdajyMi0Oxn8dWRxFHV5uIuUyC5PoIZx2COSJD9Sst-NXjZv7VHBQdskhoffo88G5_TZbfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f71861d0c.mp4?token=ng9P0AVe2ORmhhpexhq4WpS9tGHJSRFIr_vDMe-4lebN8DomdOFQ0dcIhVh3cShYCfbb4kNv1k51VTeTu07e7njD8XPqxwK9EJToEzrtmffp2MIR4Uodm38ZtZ1VfrJRsnpq3ZwqJTz5bYv01c-7LebuAbSnHUHjZ5uoKBTvJCLzPfpNHGE2eKIQFKsDDBnBJr0H913_QZ_ymUHzaF0J8uTeBwZKGe5LsKmekLZ-i9Hcm2cBkYy1nBMtMUbBl1R09OL1Th2488QPkboMdajyMi0Oxn8dWRxFHV5uIuUyC5PoIZx2COSJD9Sst-NXjZv7VHBQdskhoffo88G5_TZbfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مربی بدن‌سازی:
خیلی از جوونا هستن باشگاه ثبت نام میکنن ولی تو تایم باشگاه، میرن پارک با دوستاشون مواد میکشن
وقتی هم که خانوادشون بهشون میگه چرا لاغر شدی و قیافت اینجوری شده بهشون میگن رژیم گرفتیم و طبیعیه
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72002" target="_blank">📅 19:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72001">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e4e4fa6b9.mp4?token=XLiWn-Y3E4YPv9yIOJvW4Uk9R1LVetW7E6uMUOk4j-1T04UOpgPtGQh3vN5TIcI0YzD23cNwMHxLl_-cR9kxL2jz6vgivsNeMmmVkfX5NM5HSUsNcihwfRPLkosrNvi8cYYRzobGEb09JQdPbOgiwSiYp1v1By0NF8vROREjiUqHTcgc8rgslbJLSz8usC39A5vcL6xDBA5dnMjeaU4ZKpHDHEv9mBWTYWYDlEuwQdxYI4xhZW6-vC-oPSMCziMB7Xk_fLSJMhr2RWKJ0wg46ccocr9OJeQHwnwSCYWFOt8SpzJ2gdIEm9Uo3J91BvP0MWx3nNFtKxMRxzB5hbhpSxM39A8qW1-Juei3WnbK40y3KNYu6hd1n8d27acQZ9h6fadRlNyxTbi1QyU2Fw6I6WXhS5R32rQHGCAx0NZq2WGz6u6bLMgUHB_dkhIH4Owz0OCZgF2JCYELrR9s1XVZ-GDyotE8G6LoyMRdHQl0aTEFH7buk31b2UQZs1gwzvliQXUkrEKAfe4TcMLWHIqXVz1Lz_R_5n-cl2ueyAzXltmI-kd0Fwei63TsLezY9PaCskhKRJRliipVuSqHoz17cuhM4QOeXffNmPlWZQwLWcL3V03w7a0d-u-knmyo4b6hSHanxIAl_pewkTD7bqczUHskuLRJrTxIDtFwnjNr_Rs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e4e4fa6b9.mp4?token=XLiWn-Y3E4YPv9yIOJvW4Uk9R1LVetW7E6uMUOk4j-1T04UOpgPtGQh3vN5TIcI0YzD23cNwMHxLl_-cR9kxL2jz6vgivsNeMmmVkfX5NM5HSUsNcihwfRPLkosrNvi8cYYRzobGEb09JQdPbOgiwSiYp1v1By0NF8vROREjiUqHTcgc8rgslbJLSz8usC39A5vcL6xDBA5dnMjeaU4ZKpHDHEv9mBWTYWYDlEuwQdxYI4xhZW6-vC-oPSMCziMB7Xk_fLSJMhr2RWKJ0wg46ccocr9OJeQHwnwSCYWFOt8SpzJ2gdIEm9Uo3J91BvP0MWx3nNFtKxMRxzB5hbhpSxM39A8qW1-Juei3WnbK40y3KNYu6hd1n8d27acQZ9h6fadRlNyxTbi1QyU2Fw6I6WXhS5R32rQHGCAx0NZq2WGz6u6bLMgUHB_dkhIH4Owz0OCZgF2JCYELrR9s1XVZ-GDyotE8G6LoyMRdHQl0aTEFH7buk31b2UQZs1gwzvliQXUkrEKAfe4TcMLWHIqXVz1Lz_R_5n-cl2ueyAzXltmI-kd0Fwei63TsLezY9PaCskhKRJRliipVuSqHoz17cuhM4QOeXffNmPlWZQwLWcL3V03w7a0d-u-knmyo4b6hSHanxIAl_pewkTD7bqczUHskuLRJrTxIDtFwnjNr_Rs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ونس درباره ایران:
ما کاملاً واقفیم که قیمت انرژی به دلیل اقدامات تروریستی ایران علیه کشتیرانی بین‌المللی، افزایش یافته است.
ما تمام تلاش خود را به کار می‌گیریم تا ضمن مهار این قیمت‌ها، در این فاصله باری از دوش مردم آمریکا برداریم.
یکی از اقداماتی که ترامپ درباره آن صحبت کرده، تشویق برخی ایالت‌ها به کاهش یا حذف مالیات بنزین برای مردم آمریکا است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72001" target="_blank">📅 18:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72000">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8571b32102.mp4?token=lrgS3LxUEtGLKuJnvMzyF-amSuV9nWxo_GMGC5jNwm9dJMeMu3eliH8YTC3qKNZy9ADb6lJ1-T7JOny1HcQ8ngwX9EgMb59vXq-uaUX6YBMJxm4iQZWDw61O-Nmu3uMrzmudjOUlZkJZU36Hj76v0R6MsMtZCcOWd-MtP5T4PznyFNevlFX-k1l5zedNQ8WN8K9ZxCW5L247pTcXLSdzEH2FKSeK6-sjf8vMNCnYE95ACPycjebInVy7B-OKqY_ephqa0zGJtMFnpv9DeNcw8dx_1ZsgXJaO7YNMCwX1sNVx-Ctn7kG9q1_yvB2fV2I2ViC-0n4RjuVJUQ8XNb4dkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8571b32102.mp4?token=lrgS3LxUEtGLKuJnvMzyF-amSuV9nWxo_GMGC5jNwm9dJMeMu3eliH8YTC3qKNZy9ADb6lJ1-T7JOny1HcQ8ngwX9EgMb59vXq-uaUX6YBMJxm4iQZWDw61O-Nmu3uMrzmudjOUlZkJZU36Hj76v0R6MsMtZCcOWd-MtP5T4PznyFNevlFX-k1l5zedNQ8WN8K9ZxCW5L247pTcXLSdzEH2FKSeK6-sjf8vMNCnYE95ACPycjebInVy7B-OKqY_ephqa0zGJtMFnpv9DeNcw8dx_1ZsgXJaO7YNMCwX1sNVx-Ctn7kG9q1_yvB2fV2I2ViC-0n4RjuVJUQ8XNb4dkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ونس درباره ایران:
با وجود اینکه ایرانی‌ها هر روز برای کشتی‌ها ایجاد وحشت می‌کنند، ما همچنان شاهد جریان حجم قابل‌توجهی از نفت و گاز از طریق تنگه هرمز هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72000" target="_blank">📅 18:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71999">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i97u8l4PoawtrMoe0373WyQuIA7JUPuzcATZE5c1I3TJR3Fd_HigLXcCwcMzmVMwzRT23xaj3DuqA7o9hris2rjY7LUss-AAWCs4XB1CoTYHyuOrFTKKRhw3PKP8VSrk6NwxTlno9X4m6u9h3zm7RMHKloBDJPrxvKmtDT2J4eEptL9XaC2TsHdv7IRykKswMEzhiLdOQJBklu15_HcvW5fZM8PQ2aCEHUN_bWpG-VIwnDS-DIpZi-URnPhrwMHbKX0MerMaojk-FmWq8ukKjgReedWDoNwwAn4bTao9z0rVce8WxclGUZwCQ3kKY89u9SBGMJYj-SqnLAMvbvU5HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدای دو انفجار از سمت تنگه هرمز شنیده شد.  @News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71999" target="_blank">📅 18:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71998">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d9e105be9.mp4?token=OyF8gricTlmbwVQ8N2V7ZpAxqA19y-6H705UGVov7vgwkvQEB-zpJQHVGWquJUfQaAOPMF4dE3s0MZvGDtyNnzfrvyu1GVm36lueKrJLg_IjTVdMnpflHAapo0D41jSX4ZCoOmpYjJDcrhKhTvG8ipMtb5quJnkh_a61AKR_PZI2mhW_Ysvi1I-hEANdT3QLOdzMciAxXa4j3fg_kP4Gk1_4WWVgJdJJN-V5nSrZdQPiHpLlZIEi5SoxF2rvyeFHoce69NLn2piqJ6y2uqCrTe58NfYFKTd-driX-sm5P_gnWU3cQNdqebQQLG1yvZqEJUmDv2m85HYZlJZjOW_65A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d9e105be9.mp4?token=OyF8gricTlmbwVQ8N2V7ZpAxqA19y-6H705UGVov7vgwkvQEB-zpJQHVGWquJUfQaAOPMF4dE3s0MZvGDtyNnzfrvyu1GVm36lueKrJLg_IjTVdMnpflHAapo0D41jSX4ZCoOmpYjJDcrhKhTvG8ipMtb5quJnkh_a61AKR_PZI2mhW_Ysvi1I-hEANdT3QLOdzMciAxXa4j3fg_kP4Gk1_4WWVgJdJJN-V5nSrZdQPiHpLlZIEi5SoxF2rvyeFHoce69NLn2piqJ6y2uqCrTe58NfYFKTd-driX-sm5P_gnWU3cQNdqebQQLG1yvZqEJUmDv2m85HYZlJZjOW_65A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه پاسداران ویدیویی منتشر کرد که مدعی است لحظه رهگیری و انهدام یک پهپاد MQ-1 ارتش آمریکا در صبح امروز را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/71998" target="_blank">📅 18:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71997">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71997" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/71997" target="_blank">📅 18:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71996">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxFINv-sJH4G46uAr_7JPIAvWFSrzOFVKdW-51T6WWV6KPjlyKlbD5vIBvVTP01cknDyfpR9p0tWOTwPQwKn4EaKaWVYARseETfyBePp99u_40zCh57AOE9u8Ip6_x8qArhATG9suzlPyPPSwzutubngKIWg1s7j0ffaYZEiu1jp0Dl18rG559Onj3BMrw5RNvw1evqBtnV7cPMvT1ELzqS_jkgj7HeLxo3q2AH0Ym1KEfEQ_4-2WKRhtSfNzM6SojZJCwVxwkQ64QyqxsUTtygkFHbry4QL8KY9tL9AKEAqhd8cdXvGY_icmXqjeM9WZNy-5Gm9lJownXNXLDtfOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71996" target="_blank">📅 18:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71995">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5dd9ae6ba.mp4?token=Atb1dHSbfy-Su2jZ9XGkSOX0_DRAix4pdYlILC2sED-i6b6VV91gZ5tXzTMqOnmlgXTIqkFLXdW4VZbrd5fNXJyMMFBpbRjKSnppBqtu8TTnDjJIr0Mmd0B7pHikH1rtGEfR_vVHn7G_A953WEGs_uJ9WcbMD3krAgksrILyJOwFAah6xwWUfjRS-AmGNfaqBoiENThcbNTOHgUouaWFfPyxJgBCftZnURT3fieuGAfcRwxYt4lmU3P_rXEqzao5byZ6ujZhMz41y3TAk7EYARv6Zy0KgPq91SQDtCNNqKyx253MURLPKVVn0sn4TMT_2XMFN1eXkPcucnRJmal5Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5dd9ae6ba.mp4?token=Atb1dHSbfy-Su2jZ9XGkSOX0_DRAix4pdYlILC2sED-i6b6VV91gZ5tXzTMqOnmlgXTIqkFLXdW4VZbrd5fNXJyMMFBpbRjKSnppBqtu8TTnDjJIr0Mmd0B7pHikH1rtGEfR_vVHn7G_A953WEGs_uJ9WcbMD3krAgksrILyJOwFAah6xwWUfjRS-AmGNfaqBoiENThcbNTOHgUouaWFfPyxJgBCftZnURT3fieuGAfcRwxYt4lmU3P_rXEqzao5byZ6ujZhMz41y3TAk7EYARv6Zy0KgPq91SQDtCNNqKyx253MURLPKVVn0sn4TMT_2XMFN1eXkPcucnRJmal5Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک: این آینده‌ای است که آن را به واقعیت تبدیل خواهیم کرد
ایلان ماسک با انتشار ویدیویی آینده‌نگرانه از تعامل انسان و ربات، فناوری‌های پیشرفته و سفرهای فضایی، چشم‌انداز خود از آینده را به تصویر کشید و نوشت: «این آینده‌ای است که آن را به واقعیت تبدیل خواهیم کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71995" target="_blank">📅 17:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71994">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">صدای دو انفجار از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71994" target="_blank">📅 16:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71993">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f918318e4.mp4?token=dkGRsyXoXysWe8JvstlNxIn1CmmGDAb3rMrZ979qnFEqMf4jkAmfVhmL7RjlnmYD6mjoCDVxBQXTM-i1q3UZt5hf66tlaFrlKy5LXAwTZ2VraQVMRa-Zhb6WUhnv7e_xkfkbbH7OMoew2uesOCS-hl-aY6pdEOSf4ayIVVVGBTppWU7ptWQQ9NGD_uQyvyYM-QJAqIpXpFz2QdmqXVKxk23Ls0Ob55wnfRzMWhLY4ntXGafwC4dsE7bBLADBGqHDn_WycHYi9Vu1i83BnFXTrLRJY-8VKXLslR781p7VxChDqg0L507XkgM072KrxOh4YWD4BqlPh-RIBnV-4JAQRDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f918318e4.mp4?token=dkGRsyXoXysWe8JvstlNxIn1CmmGDAb3rMrZ979qnFEqMf4jkAmfVhmL7RjlnmYD6mjoCDVxBQXTM-i1q3UZt5hf66tlaFrlKy5LXAwTZ2VraQVMRa-Zhb6WUhnv7e_xkfkbbH7OMoew2uesOCS-hl-aY6pdEOSf4ayIVVVGBTppWU7ptWQQ9NGD_uQyvyYM-QJAqIpXpFz2QdmqXVKxk23Ls0Ob55wnfRzMWhLY4ntXGafwC4dsE7bBLADBGqHDn_WycHYi9Vu1i83BnFXTrLRJY-8VKXLslR781p7VxChDqg0L507XkgM072KrxOh4YWD4BqlPh-RIBnV-4JAQRDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛اسکات بسنت درباره ایران:
در ۲۳ سپتامبر، فعالیت تمام شرکت‌های هواپیمایی ایران در سراسر جهان متوقف خواهد شد.
چگونه این کار را انجام می‌دهیم؟
اگر آن‌ها فرود بیایند، شما نمی‌توانید به آن‌ها سوخت یا خدمات فرودگاهی ارائه دهید و نمی‌توانید به آن‌ها بلیت بفروشید؛
وگرنه از سیستم دلاری کنار گذاشته خواهید شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71993" target="_blank">📅 16:57 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71992">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">#مهم
؛اسکات بسنت وزیر خزانه‌داری آمریکا در گفتگو با CNBC: فعالیت ایرلاین‌های ایران از ۲۳ سپتامبر(اول مهر) با محدودیت های جدی مواجه خواهد شد.
اسکات بسنت، وزیر خزانه‌داری آمریکا، روز دوشنبه ۲۱ سپتامبر اعلام کرد ایالات متحده از ۲۳ سپتامبر (اول مهر) با اعمال تحریم‌های ثانویه علیه ارائه‌دهندگان خدمات هوانوردی، در پی متوقف کردن فعالیت بین‌المللی ایرلاین‌های ایرانی است.
بسنت گفت شرکت‌هایی که به هواپیماهای ایرلاین‌های ایرانی سوخت‌رسانی کنند، خدمات فرودگاهی ارائه دهند یا برای آنها بلیت بفروشند، ممکن است با خطر قطع دسترسی به نظام مالی و دلاری آمریکا مواجه شوند.
این اظهارات پس از آن مطرح شد که وزارت خزانه‌داری آمریکا در ۸ سپتامبر، ۳۶ فرد و نهاد مرتبط با بخش هوانوردی ایران، از جمله ۲۷ ایرلاین ایرانی، را تحریم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71992" target="_blank">📅 16:43 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71990">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/939066a7e6.mp4?token=UBX_ZLKwYtosqZFMM8A43xjaXF3rDqVIm4SNvlgIq9fFDLuhzANAk3Z4Lk0FrmV3GPsjp7axyjMrnvsnrjTxz7l_GtGJ0X1uINYSe7_7u4Wd36IFNc_En22zi04qwM_soifP98POwC8zp9x1w1s5N_s9zd-gz7hH60vDEFYUTY87iWKOyf5bMfN0ufJBJ3_vDzMg_i-4_GEy9LfyRBijgmndMR8dKSOr7lh2LfotpY-55XwSeq9pWQl52ITYVwb-Ex2rxmOEUI3nuiYHHvB2o0wa3pKnfPm0zzkCWqvQKbd1NcffqM5iB41YK6kZUsunWjW-q7sW8sCsz0baW1sDZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/939066a7e6.mp4?token=UBX_ZLKwYtosqZFMM8A43xjaXF3rDqVIm4SNvlgIq9fFDLuhzANAk3Z4Lk0FrmV3GPsjp7axyjMrnvsnrjTxz7l_GtGJ0X1uINYSe7_7u4Wd36IFNc_En22zi04qwM_soifP98POwC8zp9x1w1s5N_s9zd-gz7hH60vDEFYUTY87iWKOyf5bMfN0ufJBJ3_vDzMg_i-4_GEy9LfyRBijgmndMR8dKSOr7lh2LfotpY-55XwSeq9pWQl52ITYVwb-Ex2rxmOEUI3nuiYHHvB2o0wa3pKnfPm0zzkCWqvQKbd1NcffqM5iB41YK6kZUsunWjW-q7sW8sCsz0baW1sDZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگنده نسل جدید J-36 چین به پروازهای آزمایشی خود در طول روز ادامه می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71990" target="_blank">📅 16:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71989">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34a5f81c8.mp4?token=m3o_9rCeEqFofg0I3Vy1v7D5ifdmAD0iBhzQWQoIFUfYe_NJHzD6f4D3zToM8qc-WvXbWAoq78VvlLHhY9Chm_HtXFKO9ToGHJ30fzAGT-LfqvAOmhD--Avq6Exbl9yABgNiSuDaGrQ2qWTyR-NjBZU2FHeTq6ZLYun6tDl9pyo_Ojb5NCpfVpUyNyFxYAigXY1Nf3QsXA4aKYRjkeagzFaTy3u8m2NeeWB1DShiS6wvN1AURhQtYbHKmW-0WygNcmtD7iImUdh6XRf2irdZ6UmeHFyxcpjfWTHli1EOL8tXHuXgNyBN9N_I-O2Bjuc3YVJOVzYdQcJKuZBo62nQLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34a5f81c8.mp4?token=m3o_9rCeEqFofg0I3Vy1v7D5ifdmAD0iBhzQWQoIFUfYe_NJHzD6f4D3zToM8qc-WvXbWAoq78VvlLHhY9Chm_HtXFKO9ToGHJ30fzAGT-LfqvAOmhD--Avq6Exbl9yABgNiSuDaGrQ2qWTyR-NjBZU2FHeTq6ZLYun6tDl9pyo_Ojb5NCpfVpUyNyFxYAigXY1Nf3QsXA4aKYRjkeagzFaTy3u8m2NeeWB1DShiS6wvN1AURhQtYbHKmW-0WygNcmtD7iImUdh6XRf2irdZ6UmeHFyxcpjfWTHli1EOL8tXHuXgNyBN9N_I-O2Bjuc3YVJOVzYdQcJKuZBo62nQLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرکی به نام صدا و سیمای جبلی!
با تراکتور اومده وسط برنامه؛ میگه میخوام باهاش اسرائیل رو شخم بزنم!!!
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71989" target="_blank">📅 16:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71988">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZL6RjJp5Jz7lEOqz_kEwHYwKMEfYJJIVzukqLw6tXcNsU-qD2aDUvJBF1eAYtLLcmHwr8VXBqgq-xJ_kYhGH5-ZpaG2VYmJIb_VBrGcFkQybUHkqtfjUL9UyC1w6oq16ku6u4_4ndLLede818JBoGzpMPJTI43VpyW7TYp0JifpiAlPySy8-lqajP1dEx_OcbSa92vXBEGKMtB7-wkCMBVihq9LKzvri4KLLUNZjnbDMBN4wuewGwbulKlvD7cBm6SfEe73Qw84QH_wu7R670hLhAnlRhTUPQmbzmMTOtqkqFQnkELyakJToikEVaixySA7UHZUlvy96OKeAFievgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس:انتقال سهمیۀ بنزین به کارت بانکی از مهر در ۵ استان اجرا می‌شود؛
سخنگوی کمیسیون انرژی مجلس:
این طرح تاکنون ۲ مرتبه در چند جایگاه به اجرا درآمده و قرار است از ابتدای مهرماه، در پنج استان کشور به‌صورت آزمایشی آغاز شود.
طرح انتقال سهمیۀ بنزین به کارت بانکی به‌تدریج تا پایان سال در سراسر کشور اجرایی خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71988" target="_blank">📅 15:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71987">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86993a4fad.mp4?token=kk4BDdEB5sXjbZSFt0_9OcBE5o0nXyojvK4qKwNvjYEgpDQPe3gZXI9kCp8j2AKVbQsERzolhlgAg02Tk_k_6RBuo9oLqs6FxKDCXU1Re5hzvo1HtyNHJZ9AXHowdBCVAY3w_EWmGWz4i7E0kuJO8ASP72-pDci1rDPB31me30ipsOrfh6NQdayr1z9Dp9MxuhF4dPCfPeUT524dioiTuTOI3K9YkLxVx1Bk3lkIrnXuG30-q-PJph1Xq3o-tQdP0vYic-PbgzP5T3WyZqJrlhNoILBV5AoQqQ9m6OCb0z8aRtQnFk-RO7uYqxylPyMZabn95fgae9K9L-mYmdspaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86993a4fad.mp4?token=kk4BDdEB5sXjbZSFt0_9OcBE5o0nXyojvK4qKwNvjYEgpDQPe3gZXI9kCp8j2AKVbQsERzolhlgAg02Tk_k_6RBuo9oLqs6FxKDCXU1Re5hzvo1HtyNHJZ9AXHowdBCVAY3w_EWmGWz4i7E0kuJO8ASP72-pDci1rDPB31me30ipsOrfh6NQdayr1z9Dp9MxuhF4dPCfPeUT524dioiTuTOI3K9YkLxVx1Bk3lkIrnXuG30-q-PJph1Xq3o-tQdP0vYic-PbgzP5T3WyZqJrlhNoILBV5AoQqQ9m6OCb0z8aRtQnFk-RO7uYqxylPyMZabn95fgae9K9L-mYmdspaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک خلبان در جریان یک پرواز چهار ساعته بر فراز ایالت های اوکلاهما و آرکانزاس آمریکا، مسیر هواپیمای خود را به شکل چهره مونالیزا ترسیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71987" target="_blank">📅 15:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71986">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1qjpIeZHuRQHMfiU_iCrUf3S_bvW6u5QZ-LqORKRTT4dmxsKmfqoXIsQpRIWTlYvBd9BPI2POi_Vb2dgzgRWbhnwaNNlgi1cNtYJuTpzjZho8z5O-kpfjVBab5KGCHRP9Y4Htao4NttYp9vYAX93lG5LRVPcxvPKbmYyA_KO31qiKTx1QrDg-u1ARyj2Xd6-piIWxr4d_fsQHX6muVspiyp0JgmHbOl8NRJV33-Zb4wJPIoLEiCOvrAxHc-xCngtnl0wEEatcobJp-NvxM-RI72gaRW32WFHnTzEHbkez6ixniX9TkGiHTGBQKFNwP_DvRqNmwW1mvQEIX-RNfZjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش پولیتیکو، سی‌ان‌ان، ام‌اس ناو و پولیتیکو پس از لغو دسترسی مطبوعاتی‌شان توسط کاخ سفید، از دولت ترامپ شکایت کرده‌اند و استدلال می‌کنند که این اقدام نقض متمم اول قانون اساسی است.
این رسانه‌ها می‌گویند که به دلیل گزارش‌هایشان هدف قرار گرفته‌اند، در حالی که رئیس جمهور ترامپ از این ممنوعیت دفاع کرد و گفت که ملزم به پذیرش رسانه‌هایی که «داستان‌های منفی» منتشر می‌کنند، در کاخ سفید نیست.
انتظار می‌رود درخواست اضطراری از یک قاضی فدرال در واشنگتن دی سی ارائه شود که احتمالاً منجر به جلسات استماع و استدلال‌هایی از سوی دولت در این هفته خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71986" target="_blank">📅 14:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71985">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba57cb4ffa.mp4?token=VxR0EIHUbfwep-DBDnu89oz_Y9dvSHRwY_JTY55hSxIKvFtOXnNlUnZeIJcU3p1Kdl1l1AHBnWTEA8Tm-Al53onrBrnZSZIUMjq5sBI88pdxxKMDaAE9bkDSktzuvFNYKkfoaTX7H-DwM1p7TeBUbRNTHeOTnFvvpAKcS3f-dv0XlUBT0ZlNnwaUzgo5k4anI0Lv9ORIfJz1xR_Hecl0Nxd7cNKb9e1fKnWRAq4gmjR8xD6obzQrTnJWwTE-dfK2XODic2dR7TZjGLAZEYEZYTvIyhjrCWjTmWPyELUMoaUwZaXuXc2Bu7cO7zkr-RmFfkyZ51ib1JIt_Z3upHk3aJ4JyMIXBeTb-0-f3VkIrfCDoP99PAMihcES8JHtF8GD8yEdo69ZL6N_m-v3lwLK3h4Qlm-ocbG5sIQ2hNH8OxoEowMOaQis-cbNm9a_GUX-mThZ4LkSdfCLRv-IM2x1SYh7NydPX9WKw1ihPEt8hrHISDmH8Y-B1QMJ2_DMFy5ZL7tUAB8onO5yfjU6hK9Is8fQX7FLrVsKnpU-bvjrBN4zhLKc1HmVs8vtwv0oJTxkfeJnSDN8TV1MueLmI_jLFNsgxbaiPJsO3NFJHZlPJrvnGgqwr9Hiv4Of9Z5EfL769kRMUarxT_x0JZEd_k_SsGhvOav8WjqFGG7eNnTHRoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba57cb4ffa.mp4?token=VxR0EIHUbfwep-DBDnu89oz_Y9dvSHRwY_JTY55hSxIKvFtOXnNlUnZeIJcU3p1Kdl1l1AHBnWTEA8Tm-Al53onrBrnZSZIUMjq5sBI88pdxxKMDaAE9bkDSktzuvFNYKkfoaTX7H-DwM1p7TeBUbRNTHeOTnFvvpAKcS3f-dv0XlUBT0ZlNnwaUzgo5k4anI0Lv9ORIfJz1xR_Hecl0Nxd7cNKb9e1fKnWRAq4gmjR8xD6obzQrTnJWwTE-dfK2XODic2dR7TZjGLAZEYEZYTvIyhjrCWjTmWPyELUMoaUwZaXuXc2Bu7cO7zkr-RmFfkyZ51ib1JIt_Z3upHk3aJ4JyMIXBeTb-0-f3VkIrfCDoP99PAMihcES8JHtF8GD8yEdo69ZL6N_m-v3lwLK3h4Qlm-ocbG5sIQ2hNH8OxoEowMOaQis-cbNm9a_GUX-mThZ4LkSdfCLRv-IM2x1SYh7NydPX9WKw1ihPEt8hrHISDmH8Y-B1QMJ2_DMFy5ZL7tUAB8onO5yfjU6hK9Is8fQX7FLrVsKnpU-bvjrBN4zhLKc1HmVs8vtwv0oJTxkfeJnSDN8TV1MueLmI_jLFNsgxbaiPJsO3NFJHZlPJrvnGgqwr9Hiv4Of9Z5EfL769kRMUarxT_x0JZEd_k_SsGhvOav8WjqFGG7eNnTHRoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر قطر:
از زمان جام جهانی، دیگر روی آرامش را ندیده‌ام.
پس از آن، ماجرای هفتم اکتبر پیش آمد و از آن زمان تاکنون، هیچ‌کس حاضر نیست به ما فرصتی برای نفس کشیدن بدهد.
از همه خواهش می‌کنم؛ ما برای سال ۲۰۲۷ به سالی سرشار از صلح و آرامش نیاز داریم.
لطفاً، ما به کمی استراحت نیاز داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71985" target="_blank">📅 13:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71984">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boo1eh6LDvEu_HsF3m4pujXAQE4VXJUqEERR45Wg8emCCFddk8kq0tyPTev4e_ZsrVcgN12e9K7NBuVaN-YgL8rzSbDWU9LTZ102Usa0p1qbWrJrhyXs7w3_UO4jiY2j2oJsqrcBCS9P_fxfD2k5FH8V1lZQ4uoEpy3wAHh3P7z2Rxu2s9DpCK5iHBNsjngtOkhsc9mg0CqgnNinZbe9706t8Fs3Uow2_KAC_vSWaNCL0m_YzlS1mlterIdHfr8zEiwPBdq4z4APAo5lOGZsicukWY_Mnv0pjtNeKPS8xHt8PFg13nKwGsMJ7vKfzBi3QYm9iSv4souAOxKxOHbtmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
در هشدار شماره ۲۶-۱۴۰ که ساعت ۰۷:۳۰ به وقت هماهنگ جهانی (UTC) صادر شد، گزارش داد که یک نفتکش در حال عبور به سمت داخل تنگه هرمز، مورد اصابت یک پرتابه ناشناس قرار گرفته است. دو تن از خدمه دچار جراحات سطحی شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71984" target="_blank">📅 13:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71983">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ada732dd6.mp4?token=kT3o8In0uccgE9NtOTr_XzTFy9s1vuXRX3etPGUtPpBB4ZcpmlBN9T3VWj00b-qx-FVbR-BIzzqv-POafQKcO84pjHKBjG_3mOTSjVWeJ64_QDYECokAvmce9KbxBKJLsyhEWPAyNx_X9hvG1FUrXDHqIR5I1qXQd_wPwQErzQVvdvw7indjOywXu2C6DseNaFcYI5KBCf74pY_fYO0UhXcKw0CqzGweLvitP0rEKIOLrxozIfZ8Cn8KkUqUiWIrn8Ta5GdHVClChxmlW8E2CPJ-QOSzyelm50AjItv8WwTDuhq5POUJrTs34feibLEKaF0xmimoRi-IzDMB9g_Umg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ada732dd6.mp4?token=kT3o8In0uccgE9NtOTr_XzTFy9s1vuXRX3etPGUtPpBB4ZcpmlBN9T3VWj00b-qx-FVbR-BIzzqv-POafQKcO84pjHKBjG_3mOTSjVWeJ64_QDYECokAvmce9KbxBKJLsyhEWPAyNx_X9hvG1FUrXDHqIR5I1qXQd_wPwQErzQVvdvw7indjOywXu2C6DseNaFcYI5KBCf74pY_fYO0UhXcKw0CqzGweLvitP0rEKIOLrxozIfZ8Cn8KkUqUiWIrn8Ta5GdHVClChxmlW8E2CPJ-QOSzyelm50AjItv8WwTDuhq5POUJrTs34feibLEKaF0xmimoRi-IzDMB9g_Umg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: آیا ایران دردسرساز است؟
نخست‌وزیر قطر: کاملاً آشکار است که آن‌ها صلح‌جو نیستند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71983" target="_blank">📅 12:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71982">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0a06bd3e5e.mp4?token=d7t79yUWGvGzblk2anI4UupXZgcU3oFtzMoihzocLzcUPK7OwhSN_cVo4HX8HByXXKxGqedT3YB779gsS5DyuuoOo1gzohophXVmYoOpPrDLEEZCicFg2n9EvaaplvG2zw4EwfCoLnOGdO8o6BYYu3K8bVmeff1HG5sXDe-5AIP_r8wRBAQjFd0bBdc4Zjz2gw8nkVAvxkfpIJwCvn4LB6syW0JDZDc-iVfdYrSxYpN04yKtIZMWG9L67P3EqJBVsIuKTg6YnpDDRYkt9M62pBPktiKGJlvcqzy5vudccyMOAatL_N2SUnME_kBy5k_SzQAk-i2O5mhJeN-BfkecVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0a06bd3e5e.mp4?token=d7t79yUWGvGzblk2anI4UupXZgcU3oFtzMoihzocLzcUPK7OwhSN_cVo4HX8HByXXKxGqedT3YB779gsS5DyuuoOo1gzohophXVmYoOpPrDLEEZCicFg2n9EvaaplvG2zw4EwfCoLnOGdO8o6BYYu3K8bVmeff1HG5sXDe-5AIP_r8wRBAQjFd0bBdc4Zjz2gw8nkVAvxkfpIJwCvn4LB6syW0JDZDc-iVfdYrSxYpN04yKtIZMWG9L67P3EqJBVsIuKTg6YnpDDRYkt9M62pBPktiKGJlvcqzy5vudccyMOAatL_N2SUnME_kBy5k_SzQAk-i2O5mhJeN-BfkecVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان هم به این شکل زنگ آغاز سال تحصیلی جدید رو به صدا درآورد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71982" target="_blank">📅 12:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71981">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71981" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71981" target="_blank">📅 12:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71980">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tK2m1n-cqbf1L512EwIBmj_nvbtiCdomYJIkBXoq8AnRTuh8EqAn3Ghe0I1A8A86QHMtR_lfT7GEFNaCz-87TBYwbnmkerONJ0DYpP7ln4GojjXC9Uy7ONnALNi7yOov3GBxO-qZHEUItMvSHuhDLboUA_4ZZshEKA0mGRmc-3xGynnQ-w7n_tM-sxizG-wIslC-HSvvQuNFNjoIYY0jFxLB9rXdXUkhVVrdoNk2_L5LMiGgZJWLLRmTaTed81EpTcVgmNLxIQToblpP9iVbyvYO3GuCWMQIpACP8w5F9Nd5rmQnb7AIq4sRJvxYHc_7un4HS1R11snYlkXQFE40Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مسابقات
UFC Fight Night
شروع شد!
🦖
یک شب پر از مبارزات هیجان‌انگیز، رقابت‌های نزدیک و لحظه‌هایی که نتیجه می‌تونه در چند ثانیه تغییر کنه.
مبارزات رو زنده دنبال کن، عملکرد فایترها رو بررسی کن و پیش‌بینی خودت رو در
TrexBet
ثبت کن.
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71980" target="_blank">📅 12:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71979">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/19ac1824ad.mp4?token=GotKPvZDbue0eLRq8SJ34k05rOqJ6zspBfjxd0Orz1hyxeToq-45Tm46xBde81gyXiYiDr1Xht9dUmMlJ_HqrugZdmJgaQedCMFEL5nIGnHI906IYKAoV-10tNjOYRHjw-XQfu8o_85BuGj82mi0I2Qkyzrq6ntnA45_H01NbOHxq1R8o1xwiWHLw7TVCaNv-3YkMIGy2pf3v46heV3ys3ZfVj6kTxSKAGVSd8hFl4kuKr32Nx6jkxBaqII-Djz8kpMVM4rARU2vmGW7DaKe58mKNd-r_R3uh-syhvlPM6PANKNgxLA3CZEPAe18oDRjXpTLacdp8cth29Oj4r6zkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/19ac1824ad.mp4?token=GotKPvZDbue0eLRq8SJ34k05rOqJ6zspBfjxd0Orz1hyxeToq-45Tm46xBde81gyXiYiDr1Xht9dUmMlJ_HqrugZdmJgaQedCMFEL5nIGnHI906IYKAoV-10tNjOYRHjw-XQfu8o_85BuGj82mi0I2Qkyzrq6ntnA45_H01NbOHxq1R8o1xwiWHLw7TVCaNv-3YkMIGy2pf3v46heV3ys3ZfVj6kTxSKAGVSd8hFl4kuKr32Nx6jkxBaqII-Djz8kpMVM4rARU2vmGW7DaKe58mKNd-r_R3uh-syhvlPM6PANKNgxLA3CZEPAe18oDRjXpTLacdp8cth29Oj4r6zkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید باورتون نشه ولی، یه دختر نصف شب، این شکلی دختر خالشو سورپرایز کرد:
یه دسته گل بزرگ+ آیفون ۱۸ پرومکس+ کلی شکلات!
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71979" target="_blank">📅 12:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71978">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfc3620090.mp4?token=l7dsCVex1XaiZzMq3SqKe7R4F_Qpi3AARrV06xloUjqLWDhw3TdIvP7FaJaBRv-8mpFb7ZXKsH5Oje1LjC68Cm7SsZK9bT3HzKhXtH4KYQJtDxQcN7ambKAnRstfEFH5rPE9emih0EPQ9YQk1KJnsS8S-ifRQH9motSRvBDbXVggHm53G7c6BcF5s32gj_5osMJgEvJfJ_t_L2NL9jTHl1gNI-k_9XN8GePU26fcOg1UZDmWDRsUl0VVdSZWxwT6MFRrQV7PVYngoigdN6oVpo_dqASwfroN1OLTYBaIgHmZrcpQ9tmtRKsPH0V9LekSTB2MpB8v8B37OZCM6TUHLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfc3620090.mp4?token=l7dsCVex1XaiZzMq3SqKe7R4F_Qpi3AARrV06xloUjqLWDhw3TdIvP7FaJaBRv-8mpFb7ZXKsH5Oje1LjC68Cm7SsZK9bT3HzKhXtH4KYQJtDxQcN7ambKAnRstfEFH5rPE9emih0EPQ9YQk1KJnsS8S-ifRQH9motSRvBDbXVggHm53G7c6BcF5s32gj_5osMJgEvJfJ_t_L2NL9jTHl1gNI-k_9XN8GePU26fcOg1UZDmWDRsUl0VVdSZWxwT6MFRrQV7PVYngoigdN6oVpo_dqASwfroN1OLTYBaIgHmZrcpQ9tmtRKsPH0V9LekSTB2MpB8v8B37OZCM6TUHLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از دو دختر جانفدا به اسم پرنسس های جنگجو؛
میگه همه با دوست پسراشون میان رزمایش من با دوست دخترم
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71978" target="_blank">📅 11:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71977">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">محبی، سخنگوی سپاه پاسداران:
در صورت وقوع حمله‌ای دیگر از سوی آمریکا، ایران واکنش نظامی خود را — از جمله «جغرافیای جنگ» و تسلیحات مورد استفاده — به‌طور قابل‌توجهی تغییر خواهد داد.
«ما تسلیحات جدیدی با قابلیت‌های تازه به میدان نبرد خواهیم آورد و جهانیان شگفت‌زده خواهند شد.»
محبی افزود که ایران همچنین «اهداف جدیدی» در اختیار دارد که تاکنون مورد حمله قرار نگرفته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71977" target="_blank">📅 10:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71975">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9961c391f4.mp4?token=JYdpY_HTc4XunZEMtN_iAE4A51E4Sih1uCWEKCIod3JdMSOaNluh8r1xAInjpAV2hfqU_U3ENcl-fhODmH-Lw9pJRfXogp3kexuzraCjJOOzXHnikWa1Zm-Oje9yLfuS42wSMD8sUx157sPe8bERwm28KnOun-rDAYlZVgyu6nU5XYplTlVQGb3jicZs6rUF2LcKAFu6DhCJuwu41v7bJ5AkEFcy3Kk84ViSIQyDxN06E_kNEXjsSRw33dglb0u4RXuP5mEwrRW6-F-IG-VyqfdXF-wmns4ykWXoKgp2516WzVfzyHp1WeMVpK9ZavWwjUJsnfKhj7qqLmht5X2QFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9961c391f4.mp4?token=JYdpY_HTc4XunZEMtN_iAE4A51E4Sih1uCWEKCIod3JdMSOaNluh8r1xAInjpAV2hfqU_U3ENcl-fhODmH-Lw9pJRfXogp3kexuzraCjJOOzXHnikWa1Zm-Oje9yLfuS42wSMD8sUx157sPe8bERwm28KnOun-rDAYlZVgyu6nU5XYplTlVQGb3jicZs6rUF2LcKAFu6DhCJuwu41v7bJ5AkEFcy3Kk84ViSIQyDxN06E_kNEXjsSRw33dglb0u4RXuP5mEwrRW6-F-IG-VyqfdXF-wmns4ykWXoKgp2516WzVfzyHp1WeMVpK9ZavWwjUJsnfKhj7qqLmht5X2QFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات پهپادی روسیه به زاپوریژیا به یک مرکز خرید و قدیمی‌ترین ساختمان دانشگاه ملی زاپوریژیا آسیب رساند.
در حملاتی جداگانه در منطقه اودسا، انبارهای مواد غذایی که گفته می‌شود متعلق به فروشگاه‌های زنجیره‌ای «سیلپو» (Silpo) هستند، هدف قرار گرفتند.
در استان کی‌یف، این حملات به ۳۴ نقطه در پنج منطقه، از جمله خانه‌ها، انبارها و زیرساخت‌ها، خسارت وارد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71975" target="_blank">📅 10:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71974">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08216dc24f.mp4?token=VxF2mmS-Jn5SOdl8IWe5lCmpx5F8qTJIjcs73rEBkw9nNygEa-pu8W8kYbKLdNXWimdGo54Tfzy4E6UBYlPqNdk2omK_fjoangluVApCA__4d0Q9OIKAMkEYqO1e8C9Xv1WHXjDSJfS7JGCCELczTcODmEyV881DyH2oq5p9QxnkgrLPXZ2AJB3sgGGYnxy_4a0LKmwioVcqcjizCnHvud7D3xchqp4Zc7O7sXevjSd0ApDE3oDvUrz8RVoM5jJeKawDg_MRgvDj4QGW6LHif8PmAsmfOp3XLEm2Mf262KJZ0hT9mhtAFO4bWb4mvC_NMThKZiCvP8uOtcxFtv6teQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08216dc24f.mp4?token=VxF2mmS-Jn5SOdl8IWe5lCmpx5F8qTJIjcs73rEBkw9nNygEa-pu8W8kYbKLdNXWimdGo54Tfzy4E6UBYlPqNdk2omK_fjoangluVApCA__4d0Q9OIKAMkEYqO1e8C9Xv1WHXjDSJfS7JGCCELczTcODmEyV881DyH2oq5p9QxnkgrLPXZ2AJB3sgGGYnxy_4a0LKmwioVcqcjizCnHvud7D3xchqp4Zc7O7sXevjSd0ApDE3oDvUrz8RVoM5jJeKawDg_MRgvDj4QGW6LHif8PmAsmfOp3XLEm2Mf262KJZ0hT9mhtAFO4bWb4mvC_NMThKZiCvP8uOtcxFtv6teQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مونا محبی، تراپیست :
«یه بیمار داشتم که سه تا پسر داشت؛ فقط پسر اول بچه شوهرش بود. پسر دوم بچه عموی شوهرش و پسر سوم هم بچه شوهرعمه شوهرش بود!
حالا بچه دوم یه مشکل خونی پیدا کرده و برای تشخیص باید
آزمایش ژنتیک
بده؛ آزمایشی که ممکنه مشخص کنه بچه، بچه شوهرش نیست و این راز بعد از سال‌ها لو بره.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71974" target="_blank">📅 10:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71973">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b710ab2e63.mp4?token=bPB9k5xpfgF6m8fGTVtntwHyWV54TK16_3bvPwi5M0N4RNh2RNhVvKncqB29v9yjzBFaEQ4lRuYpCinAy7zJqOEdTjmYDSxWK3KVvkJAUhxyuxf2UyX6Yiozr07Q6bnzKAmT5SkKym_xOVaIShJwuI7_dNBtmhy0HLHjAdVxzy7XmDgqOGWdmZ1E8qQvEH2zZTS1UPkUsnqVzeDO8O8XyuQQzcdhEPYJD05Tnqb63-1moRMBCLEECTJiPRipuA9a6I5Goc_QBToi9lqo0kVqiqi31ryEE38KA13KaYMG1FmFzKTMlAGE6FgCD8YzJ50jmDpL07SGTIu3XIEV99_N3aCdpuT5551trwokzlGIQGP2Z4iIpYr5FmiLr0UWWZqEy59a1vAdkANf1KcEESXfO30kZrzeo-eOVTacLrVhpvEzPAdNHTZTpc_AQDt4FdPutr18MhvqrBpX9N00IlZsX3kSV3sF3tvssTyEbOJahL_215CncFjeOJt3g1uOlVb8kEtEQeipfUetEBNQdOQXie2GaF2EkVMLApoTBSxDmxT1fPx3g7XsxLjeBQysPXbPbI-abq2v1sX_HmDn4nc-9co1JUwTJT8ZSvbgDcZgidbCReZtWeTPSl80F4GOUMQrUslDOwfZ_lfXzZGXffokmCvXLFHv9AxiGXCLmbNPNrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b710ab2e63.mp4?token=bPB9k5xpfgF6m8fGTVtntwHyWV54TK16_3bvPwi5M0N4RNh2RNhVvKncqB29v9yjzBFaEQ4lRuYpCinAy7zJqOEdTjmYDSxWK3KVvkJAUhxyuxf2UyX6Yiozr07Q6bnzKAmT5SkKym_xOVaIShJwuI7_dNBtmhy0HLHjAdVxzy7XmDgqOGWdmZ1E8qQvEH2zZTS1UPkUsnqVzeDO8O8XyuQQzcdhEPYJD05Tnqb63-1moRMBCLEECTJiPRipuA9a6I5Goc_QBToi9lqo0kVqiqi31ryEE38KA13KaYMG1FmFzKTMlAGE6FgCD8YzJ50jmDpL07SGTIu3XIEV99_N3aCdpuT5551trwokzlGIQGP2Z4iIpYr5FmiLr0UWWZqEy59a1vAdkANf1KcEESXfO30kZrzeo-eOVTacLrVhpvEzPAdNHTZTpc_AQDt4FdPutr18MhvqrBpX9N00IlZsX3kSV3sF3tvssTyEbOJahL_215CncFjeOJt3g1uOlVb8kEtEQeipfUetEBNQdOQXie2GaF2EkVMLApoTBSxDmxT1fPx3g7XsxLjeBQysPXbPbI-abq2v1sX_HmDn4nc-9co1JUwTJT8ZSvbgDcZgidbCReZtWeTPSl80F4GOUMQrUslDOwfZ_lfXzZGXffokmCvXLFHv9AxiGXCLmbNPNrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پاراگلایدر سوار لحظاتی را که در حین فرود به سرعتی بیش از ۱۲۵ کیلومتر در ساعت می‌رسید، ثبت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71973" target="_blank">📅 09:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71972">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c67a57267.mp4?token=RCsTkQQyD-_zUFRuiMhZg0CUFGByeOuUWKC6XUwp8j9Q-XgiLYlK8tsGWYH9e_WA1ki32aIvFTMsF78S1cjzNn82XQUfbEaO5XLiocgsWh-xQRf0WVS77Sim9jG44NJwrDP7DaiPkfUcpaP5g24RtLBenETlpT1aAf020lNbwnkYzLPhejnXD6LYK3oqUJvq9bzYrtvDZf56-ERq-0B41iTAQbPgYTgAu5uc2bSsZis9Krgj_o0iIiuR7i_naTQpa8TtjXOtOuwAxdcb6bNGZy9VFXZ70BTu8L1VrN_WUgL7iZ8lQpcSUPbGhl2MGm52kdn-laG4hTCfYj5yafzecA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c67a57267.mp4?token=RCsTkQQyD-_zUFRuiMhZg0CUFGByeOuUWKC6XUwp8j9Q-XgiLYlK8tsGWYH9e_WA1ki32aIvFTMsF78S1cjzNn82XQUfbEaO5XLiocgsWh-xQRf0WVS77Sim9jG44NJwrDP7DaiPkfUcpaP5g24RtLBenETlpT1aAf020lNbwnkYzLPhejnXD6LYK3oqUJvq9bzYrtvDZf56-ERq-0B41iTAQbPgYTgAu5uc2bSsZis9Krgj_o0iIiuR7i_naTQpa8TtjXOtOuwAxdcb6bNGZy9VFXZ70BTu8L1VrN_WUgL7iZ8lQpcSUPbGhl2MGm52kdn-laG4hTCfYj5yafzecA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد شجاعی، از روحانیون حامی جمهوری اسلامی:
امام‌زمان برای ظهور به لشکر نیاز دارد
۵۰ روستا در لبنان را که سال گذشته بازسازی کرده بودیم، از بین رفتند
دیشب طرح آبرسانی به مردم غزه را آغاز کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71972" target="_blank">📅 09:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71969">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPSNVfUFiI5ikZzYTYW-uYPjn3dc_owb6GcUV3zZSrBewglCBiQU38jnpASBDGkynIfuJGkLKDA8ngx2J0WIasruLAyvvuhStNUcPPD2IQSx6cpzWi19nkUoaxHbiFr1uBz8NlkRzj_ioqVgkYTDfYG46rsp11MZe98jCENwrLSLfM9qm03JFyUY5VsJrs7kPCdm1gTEXW_dHPbw29YLyd8b55oUOJv1Y5gIoS-maJEByIRY_-8pc5jkxhaac3TAhTtKay35Ps2p0ql4fdDjlTMKhTt7-7vQWJ5QzoRJGmW36IeWl1APoVtXxidi7UR5wtXqGnwk76VgusxlGHnxmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5e7e08059.mp4?token=Hk-rEsPT1txxKuf9lMjKn1ASyfGxqGF2_GBVkrffktacC-hW7x3h3QUsAGcePE1qE-RumTQSuErmc7nJSbeCZWkzIs45SWuAzHpZwVtemoYKFE1UMNQSVLbDqAiAnSL9MPYazJFDpnPWd8syrlTr8k1sFJCKzfMYUqPAEB08gV6jI2iAm9gILNgTboOsHIPJWcR0GoVIJ9WGSqAvir5Vu_4fNr-kSV9AxtNZFGT8Em9Kvp1dPMiQxLnpUXoZ7eB1UtolZ9-D47gxB54vPAiIhrLDfc0KvSegZ1mqBdmF44mTtRF3aOEO3BpC21UOpAV5LnI-N_WzVOVLoz3h1oKlyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5e7e08059.mp4?token=Hk-rEsPT1txxKuf9lMjKn1ASyfGxqGF2_GBVkrffktacC-hW7x3h3QUsAGcePE1qE-RumTQSuErmc7nJSbeCZWkzIs45SWuAzHpZwVtemoYKFE1UMNQSVLbDqAiAnSL9MPYazJFDpnPWd8syrlTr8k1sFJCKzfMYUqPAEB08gV6jI2iAm9gILNgTboOsHIPJWcR0GoVIJ9WGSqAvir5Vu_4fNr-kSV9AxtNZFGT8Em9Kvp1dPMiQxLnpUXoZ7eB1UtolZ9-D47gxB54vPAiIhrLDfc0KvSegZ1mqBdmF44mTtRF3aOEO3BpC21UOpAV5LnI-N_WzVOVLoz3h1oKlyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند ساعت قبل شخصی این ویدیو رو با این توضیحات منتشر کرده؛صحت ویدیو تایید یا تکذیب نمیشه:
تهران ، اتوبان آزادگان
29 شهریور
از اجرام ناشناخته آسمانی فیلم گرفتم
واقعا نمیدونم چی هست ولی نزدیک ابرها بود نور های خاصی داشت و بدون هیچ صدایی در فضا معلق بود !!!
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71969" target="_blank">📅 06:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71968">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71968" target="_blank">📅 01:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71967">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/71967" target="_blank">📅 01:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71966">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d2ba66ac5.mp4?token=LZzNJhL-me2nbJYu6nJ4H3p2RMBud2OLHPzHOtMC5zsp0ZBp_I_X0r0wAR6tztAAZZwkteJ7_NffpIVsOOEm0ZhmfWQfKtWQj8odRqMSXnegDX49x6dQ2yLT2BGcKVD3xgWocxaKbuXa_WPhttQJAeml66zDFksVmq4PS3Lp5XVwMO9S3NZX4mXkmpySaMke9ZqlfhtrtzIkbzOxHsrEvl0ZMIrs1vhkSHWDOt2y1A9QTeekSwwlI7zv0O1_wOSAJf2-LCW-ZQE89TQMwb4DZVz1_J4b0SV56PpDYGK3_hEzKfBqiKtLXLuf3b1cQ7fP9a90viW6EGeTs8FPtYXKsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d2ba66ac5.mp4?token=LZzNJhL-me2nbJYu6nJ4H3p2RMBud2OLHPzHOtMC5zsp0ZBp_I_X0r0wAR6tztAAZZwkteJ7_NffpIVsOOEm0ZhmfWQfKtWQj8odRqMSXnegDX49x6dQ2yLT2BGcKVD3xgWocxaKbuXa_WPhttQJAeml66zDFksVmq4PS3Lp5XVwMO9S3NZX4mXkmpySaMke9ZqlfhtrtzIkbzOxHsrEvl0ZMIrs1vhkSHWDOt2y1A9QTeekSwwlI7zv0O1_wOSAJf2-LCW-ZQE89TQMwb4DZVz1_J4b0SV56PpDYGK3_hEzKfBqiKtLXLuf3b1cQ7fP9a90viW6EGeTs8FPtYXKsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حوثی ها:
آری، امروز ما حرمین شریفین را هدف قرار خواهیم داد؛ آن‌ها را هدف می‌گیریم تا از وجود آل سعود پاک‌شان کنیم.
ما این حرمین شریفین را هدف قرار می‌دهیم تا به چراغ راهی برای مسلمانان آزاده بدل شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/71966" target="_blank">📅 00:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71965">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89dd2a1fad.mp4?token=VHw23xSPTpk8N4ApkVNA74bqPUJACyxlWRjcGFsU1HXTXjgCGZ1SrvHBOYmgm-4qp5l7p9O8pnIyUEYOMZVLR-9aiTODzczSwbLryTO25rQNvHAIpKT2cQG43gqX0SGzXWcd0StzXB6C9BARA5NCK2BLjdMfrYyT5fYClNn8chU8WovmduZz4JO2G55xD57-ICf-aQRoQajJQ0-VBvlKjRBIMgkE4p7uCUaamBrCSD6BeHA-NqLxkeMB2tz9z51qFlNU2EPu6wPRTw9r7eqURI1l_KYdQSjrWDG5aITingRdVgwS-4qClXKImiCm_r8OwHvkij7Qay6nygRqqgElWIhmSKJLLlw1T4Q7NPHw5lKQsTvKrK1zr8ByvlmLP3KexW48Ug-ipGMGKv5DlC1koqJPwY9jjerEMUmVCP-NtzB-HVpt4QnnZ32nxC6hB2of1P657Q-v2tKxFg_HEmTrNS5tg9nZrAPoN1RD32l7kjG-WZXlNyQnfkdjgLP90HR38shdf9oz5hrC0Ssr3tYqzSWmPcLN3G_FrXExIJmTb5Jv_uRDzakaA1WPTgGjP09Eln0k3oyFBKB-C9H3W58EaJDmpkh048pVa-1b6d9A5eTxEo2QZi3BTh6X8XJhNQQTMbtCe25_hDQMUCsVX4C9UPptbU9BMIL07Ku073W3SoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89dd2a1fad.mp4?token=VHw23xSPTpk8N4ApkVNA74bqPUJACyxlWRjcGFsU1HXTXjgCGZ1SrvHBOYmgm-4qp5l7p9O8pnIyUEYOMZVLR-9aiTODzczSwbLryTO25rQNvHAIpKT2cQG43gqX0SGzXWcd0StzXB6C9BARA5NCK2BLjdMfrYyT5fYClNn8chU8WovmduZz4JO2G55xD57-ICf-aQRoQajJQ0-VBvlKjRBIMgkE4p7uCUaamBrCSD6BeHA-NqLxkeMB2tz9z51qFlNU2EPu6wPRTw9r7eqURI1l_KYdQSjrWDG5aITingRdVgwS-4qClXKImiCm_r8OwHvkij7Qay6nygRqqgElWIhmSKJLLlw1T4Q7NPHw5lKQsTvKrK1zr8ByvlmLP3KexW48Ug-ipGMGKv5DlC1koqJPwY9jjerEMUmVCP-NtzB-HVpt4QnnZ32nxC6hB2of1P657Q-v2tKxFg_HEmTrNS5tg9nZrAPoN1RD32l7kjG-WZXlNyQnfkdjgLP90HR38shdf9oz5hrC0Ssr3tYqzSWmPcLN3G_FrXExIJmTb5Jv_uRDzakaA1WPTgGjP09Eln0k3oyFBKB-C9H3W58EaJDmpkh048pVa-1b6d9A5eTxEo2QZi3BTh6X8XJhNQQTMbtCe25_hDQMUCsVX4C9UPptbU9BMIL07Ku073W3SoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
من به تمام کشورهای عربی و همسایه می‌گویم: اگر آمریکایی‌ها تلاش کنند در روابط تجاری و مالی ما اخلال ایجاد کنند، ما دو اقدام انجام خواهیم داد.
نخست اینکه قطعاً به شرکت‌های آمریکایی — از جمله شرکت‌های حفاری آمریکایی که فعالیت گسترده‌ای در پیرامون ما دارند، و همچنین شرکت‌های تجاری و بنگاه‌های اقتصادی آمریکا — حمله خواهیم کرد.
ما آن‌ها را هدف قرار خواهیم داد و اعلام می‌کنیم: این حمله‌ای به اقتصاد آمریکا در پاسخ به حمله آمریکا به اقتصاد ایران است؛ یعنی مقابله‌به‌مثل در برابر حمله.
از سوی دیگر، به کشورهای همسایه نیز می‌گوییم: با آمریکا همکاری نکنید، زیرا ما نیز اقدام متقابل انجام خواهیم داد. اگر کشوری همسایه در اعمال محاصره اقتصادی علیه ایران — برای مثال در امور مالی و فعالیت‌های مرتبط با ما — با آمریکایی‌ها همکاری کند، ما کشتی‌های آن کشور را در تنگه هرمز تنبیه خواهیم کرد.
ما بر تردد و عبور و مرور آن‌ها و برخی فعالیت‌هایشان محدودیت‌هایی اعمال خواهیم کرد، یا در زمینه همکاری‌های اقتصادی، اقدام متقابل انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/71965" target="_blank">📅 23:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71964">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d864b0e8a.mp4?token=LmOldGVsG6zDinibIn2yr2fhkg5iDIOxcZyHxloFXCzL3ZMa2M8fe-SwN88-1O68Sq9B8WKdnMsOpVBgSdZxJWCyvOaItZuNO0wsPZ6x1rQiTVnNahUML0LC02eg16B1O-GW_SFSS7E0gLg_LjS6uxrjfXAwhMCursXoaKCbBvx3LCHslbLIs9mqUe7P-jHXicfeQD1uYNBK_80s786K_oXhOfhtPpJTOP8pbzK42kKlKCsjuI48k7hwgGjiWArAmDlypN7jfaMmDGDEuGdUB9GFDEdkmyiPbK5FlIyFkU_FwJRH7qDbHbAcmQ-MlH_aFQpuYA8k0aa1unRNY2pc0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d864b0e8a.mp4?token=LmOldGVsG6zDinibIn2yr2fhkg5iDIOxcZyHxloFXCzL3ZMa2M8fe-SwN88-1O68Sq9B8WKdnMsOpVBgSdZxJWCyvOaItZuNO0wsPZ6x1rQiTVnNahUML0LC02eg16B1O-GW_SFSS7E0gLg_LjS6uxrjfXAwhMCursXoaKCbBvx3LCHslbLIs9mqUe7P-jHXicfeQD1uYNBK_80s786K_oXhOfhtPpJTOP8pbzK42kKlKCsjuI48k7hwgGjiWArAmDlypN7jfaMmDGDEuGdUB9GFDEdkmyiPbK5FlIyFkU_FwJRH7qDbHbAcmQ-MlH_aFQpuYA8k0aa1unRNY2pc0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تهران دختره بعد از اینکه پروفایل اکسشو‌ چک میکنه و میبینه اکسش رفته با یکی دیگه درجا سکته میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/71964" target="_blank">📅 23:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71963">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3758b5713d.mp4?token=RID7FyUkSMa21WWaKjf50Z3F8kaNK57VwR8imdWWG-U66dRTfh2dTMkMtWh3bmQA0hc-pdFygOZ7cxHVUof5pBzHf8W4U6Qxg7VqHQ7cjQ2xsjaQVO4IZ18MxOQUeZdvRd8tbyoZuDvsKNoui3ZX3xjK6i5OytzQ0gduu2zK0RF3cV-a_mqhxR16ZeCXo7-OmCB0MDd735qRRnn4uw0GaF5MBNaztYSpSBXgiWTlIqox3pb9agXUefjM2o2Ved-T8ACT8aZl1k6epqCUzs016M8SKYvf8OZjLNiZNSGF68EQB5I3RbFO3ZjlEMBF116a3MK7yCbEybsnDk2liqEvcg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3758b5713d.mp4?token=RID7FyUkSMa21WWaKjf50Z3F8kaNK57VwR8imdWWG-U66dRTfh2dTMkMtWh3bmQA0hc-pdFygOZ7cxHVUof5pBzHf8W4U6Qxg7VqHQ7cjQ2xsjaQVO4IZ18MxOQUeZdvRd8tbyoZuDvsKNoui3ZX3xjK6i5OytzQ0gduu2zK0RF3cV-a_mqhxR16ZeCXo7-OmCB0MDd735qRRnn4uw0GaF5MBNaztYSpSBXgiWTlIqox3pb9agXUefjM2o2Ved-T8ACT8aZl1k6epqCUzs016M8SKYvf8OZjLNiZNSGF68EQB5I3RbFO3ZjlEMBF116a3MK7yCbEybsnDk2liqEvcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیر ایرانی چند ماه پیش:
کیرم تو جمهوری اسلامی! کیرم تو قبر خامنه‌ای، ایشالا تو جهنم میسوزه!
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/71963" target="_blank">📅 22:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71962">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf9813dda.mp4?token=elx9SwIVwdRGVINPxHLKFZNxDZa_HLQityyj2gJO9J16IOtSMVjofBF3A7y0VuV165EmjJt14-swCD8p8OOSwga-7rbR-gJi_w8pKcVNAINOaYK0JyRF60hRO25za6LAchcfo7iFr9pp3534mVX0As4CUASVD9KhXOctWmRe_H6RjxR_UOvCXRXO2tKVyPRW20vaFtVzIqa15ZTxtc-VwhwvBTZz80f9FnYJCMD854szwddfpbZk-GCfl-joF7oSRWAWB1MYVK3veMmx29IElKt1JqTSzFUDq71vk7SINk06MsCcPKXhMb6W7IMkZ1bOCo7507eymzB6u5jJ3jF-kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf9813dda.mp4?token=elx9SwIVwdRGVINPxHLKFZNxDZa_HLQityyj2gJO9J16IOtSMVjofBF3A7y0VuV165EmjJt14-swCD8p8OOSwga-7rbR-gJi_w8pKcVNAINOaYK0JyRF60hRO25za6LAchcfo7iFr9pp3534mVX0As4CUASVD9KhXOctWmRe_H6RjxR_UOvCXRXO2tKVyPRW20vaFtVzIqa15ZTxtc-VwhwvBTZz80f9FnYJCMD854szwddfpbZk-GCfl-joF7oSRWAWB1MYVK3veMmx29IElKt1JqTSzFUDq71vk7SINk06MsCcPKXhMb6W7IMkZ1bOCo7507eymzB6u5jJ3jF-kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر خانومی تو تهران میره به پسرا پیشنهاد میده که با حساب خودش برن کافه، اما هیچ پسری قبول نمیکنه و دست رد به سینه این بانو میزنه.
آخر سر هم کلش خراب میشه میگه پسرا پرنسس شدن و تنها میره کافه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/71962" target="_blank">📅 21:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71961">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxsy91slQQbEvKAtjVNXF7ota4d1AZKBbHjcpImQY-72GnJLrJ32ZWmMB7SEwaCYBgl73eE4M8DTcK4cN98ohdatDEpAnrGBZlItC-78CpLrHjYzP6OixCdn4a4Z8YNhUQRpwGZ602afunzGuPoytGM2zgBVeAnaTf-xC9CmieMRO7jJNsLWqHbX6aBjp6OXUTMQdOes2NKOm_76e2SP1sUtatDDzJSCCzA33fN_ZvYVEWpWOQDIqu62HBgAh9C_K_fM_4P8AZWhQ6z9KDaAX2_RAFirj5NKIBctMXSxUagIik5Obi5g7dNS6QCDoRcgHwTGkQkEptbP8lhAYS3BjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ در تروث سوشال
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/71961" target="_blank">📅 20:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71959">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10eceadf6.mp4?token=p3seBeImpwxzxGtnLNsQAVGbNI5rS2wa1TqBkcwcqVPwMM4nFryhHf1K6Dx1XRrOrKgHhKRDoWQ5jleLBfUST6yGaRkUhdhD_2AGjYigQEJcu6BgHK6dLDYd6eKwhnSP6UpNR-mBWfgI3u9iIY9AIFUrmJ3OS6DoQIZMk7NVICs5UVjz42su51uNUqJCizpPAlsrwmdcPSxsf0mWYZQWOYhqW4jyw-z-4cxThaFE6TIl4fDHt0_oZSM-I8Sfdv6y4PEMAQuTtFZM2kCxPMuOo2S1ozfhsliWQo_uU4WAkh873nPPBh8RlEEuN3xaGFl4qpIPAhWFe-RTcaToQmXOcUjBIiISE2teHbgXfuwKc7TMLzLyFwsbMX7LlCIgrbJydM2CGpGBc8CEq5EZpuuDmoRj_TJEuTgBS7nOHwSDY930DC07l8uuhuWp9gvvAvElAQHxlvBoU65agzz0zwPujtSCCDk42e1vZT8Kh-HMmw4gQWQrfxhrbS5VKrH6jQBgvvzVlZ8MAFsFG3UXo8shMPcZKpH4qMf_JcZjQxdQ0a7Wk5a2MeRReOK6p9bP_o4o39DusAZXr_2ob8eDV3G19k3qHT8iNriVgx2vsXG7G0vR_ati1EvF-piEBEt7XOEdcd3HaTFpFQGJTCZAxICgeV8mV5hb4uUAwKXO1yX8UBo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10eceadf6.mp4?token=p3seBeImpwxzxGtnLNsQAVGbNI5rS2wa1TqBkcwcqVPwMM4nFryhHf1K6Dx1XRrOrKgHhKRDoWQ5jleLBfUST6yGaRkUhdhD_2AGjYigQEJcu6BgHK6dLDYd6eKwhnSP6UpNR-mBWfgI3u9iIY9AIFUrmJ3OS6DoQIZMk7NVICs5UVjz42su51uNUqJCizpPAlsrwmdcPSxsf0mWYZQWOYhqW4jyw-z-4cxThaFE6TIl4fDHt0_oZSM-I8Sfdv6y4PEMAQuTtFZM2kCxPMuOo2S1ozfhsliWQo_uU4WAkh873nPPBh8RlEEuN3xaGFl4qpIPAhWFe-RTcaToQmXOcUjBIiISE2teHbgXfuwKc7TMLzLyFwsbMX7LlCIgrbJydM2CGpGBc8CEq5EZpuuDmoRj_TJEuTgBS7nOHwSDY930DC07l8uuhuWp9gvvAvElAQHxlvBoU65agzz0zwPujtSCCDk42e1vZT8Kh-HMmw4gQWQrfxhrbS5VKrH6jQBgvvzVlZ8MAFsFG3UXo8shMPcZKpH4qMf_JcZjQxdQ0a7Wk5a2MeRReOK6p9bP_o4o39DusAZXr_2ob8eDV3G19k3qHT8iNriVgx2vsXG7G0vR_ati1EvF-piEBEt7XOEdcd3HaTFpFQGJTCZAxICgeV8mV5hb4uUAwKXO1yX8UBo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کشتی «لوچینگ یوان‌یو ۱۰۸» با پرچم چین و یک کشتی باری با پرچم پاناما در نزدیکی سواحل سنگاپور با یکدیگر برخورد کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/71959" target="_blank">📅 20:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71958">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4d61320a9.mp4?token=JRzcv9HD8ffkuYLGJh3D1zks4lWzjqUKGeGJX5BQ7R8ZCfw1aM7RGPVcZunaudmMHkWMLS6hMgfvcDmZssWkCW8Gsb5Pk224digbpXTGuDKfpJB2qDHvRqEr9zfABj5anuPVFxE9UGRWWn7yhtQi6hvEDI9erU8X-TyPgm5mtr3p8dfrvTKTkSUUE-TqtQnt8VmHx5ZHpVSzmuEX3Z6etfml5Ex3-6MnFByed_fPVq_wC9-YgdjM2AKdQvw5AM91wiilKKTxZ3pTVZjuThR8tC0xBoDQiJGN6IFuFYUiMG_Xsk2E99fiUtrkFyA_biDGCHNzvK6x4fFhm_GxNLrVcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4d61320a9.mp4?token=JRzcv9HD8ffkuYLGJh3D1zks4lWzjqUKGeGJX5BQ7R8ZCfw1aM7RGPVcZunaudmMHkWMLS6hMgfvcDmZssWkCW8Gsb5Pk224digbpXTGuDKfpJB2qDHvRqEr9zfABj5anuPVFxE9UGRWWn7yhtQi6hvEDI9erU8X-TyPgm5mtr3p8dfrvTKTkSUUE-TqtQnt8VmHx5ZHpVSzmuEX3Z6etfml5Ex3-6MnFByed_fPVq_wC9-YgdjM2AKdQvw5AM91wiilKKTxZ3pTVZjuThR8tC0xBoDQiJGN6IFuFYUiMG_Xsk2E99fiUtrkFyA_biDGCHNzvK6x4fFhm_GxNLrVcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک هموطن به مایک جانسون رئیس مجلس نمایندگان آمریکا:
لطفا کار مربوط به ایران را تمام کنید
۸۰ میلیون ایرانی منتظر شما هستند
مایک جانسون:
میدونم ، قطعا و علامت پیروزی
✌🏻
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/71958" target="_blank">📅 19:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71957">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b0937658f.mp4?token=OzGoPDj98vrRzy5L9-S9ohXmlZz4VPUbMOMPIbpsV1uK1k96jWdJzmXRj0WY_r4v_RV-zz5nD5MqdXzNwdDc7aghr23HYrs-4T8DL9kqB7Ay9Hm8sqzHLBgM0QwR2s564NG7RLCU0XRSnC29T4GAPQHgHoliPw6KdyVXak6tTNUo6CHaeR4ZBat_VShxFyAQDn-yXBfJovGRIlPHOP1IYkItECsbJSyHPhyFgzYgrubBQyN3fp9-Fkxxz2qcVBpCJ-7y4MhexP0u_RMMtG6VQrE5geonHvaJOwoVPmMOmnBlZDDdLdDE9uPWbJS6nyHZnxH2KO8t5irZo--6_1s4Mh2XuuhWRg3LnSz7ehSYIZsU8UQgvfigs7dNZz7fybtVhLGlrb6MSesYJlsQFy4EFe3ayyelHGADziKvZ7HZmn5KoS20bw7RWYQs7P_iFMygfi96xW4VxRlxs2F-VhVg9eFWJBSc7Lg8F3P4MwhJSu6e3vXcIqirqsGNk3zIMADJHljqbEL6D_PH8djoKnmYm6PH5ByG0BaFC4ynAxwJHbaRBSZZuPWJM5P3O1Aad_1WB0kit3SX7QdJHMN03fN5JK2wMRkNoA9BXg-Mbuh-FCb8df4GsO7F0pRT-7vLCfiqvQGBYVtPmxtu99blcb7xDG_-EY7dM89Z-qE83BLValo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b0937658f.mp4?token=OzGoPDj98vrRzy5L9-S9ohXmlZz4VPUbMOMPIbpsV1uK1k96jWdJzmXRj0WY_r4v_RV-zz5nD5MqdXzNwdDc7aghr23HYrs-4T8DL9kqB7Ay9Hm8sqzHLBgM0QwR2s564NG7RLCU0XRSnC29T4GAPQHgHoliPw6KdyVXak6tTNUo6CHaeR4ZBat_VShxFyAQDn-yXBfJovGRIlPHOP1IYkItECsbJSyHPhyFgzYgrubBQyN3fp9-Fkxxz2qcVBpCJ-7y4MhexP0u_RMMtG6VQrE5geonHvaJOwoVPmMOmnBlZDDdLdDE9uPWbJS6nyHZnxH2KO8t5irZo--6_1s4Mh2XuuhWRg3LnSz7ehSYIZsU8UQgvfigs7dNZz7fybtVhLGlrb6MSesYJlsQFy4EFe3ayyelHGADziKvZ7HZmn5KoS20bw7RWYQs7P_iFMygfi96xW4VxRlxs2F-VhVg9eFWJBSc7Lg8F3P4MwhJSu6e3vXcIqirqsGNk3zIMADJHljqbEL6D_PH8djoKnmYm6PH5ByG0BaFC4ynAxwJHbaRBSZZuPWJM5P3O1Aad_1WB0kit3SX7QdJHMN03fN5JK2wMRkNoA9BXg-Mbuh-FCb8df4GsO7F0pRT-7vLCfiqvQGBYVtPmxtu99blcb7xDG_-EY7dM89Z-qE83BLValo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعاتی پیش، یک موشک رهگیر پدافند هوایی اوکراین در حومه کی‌یف موفق به اصابت به پهپاد جت‌سوز روسی «گران-۵» (Geran-5) نشد و این پهپاد لحظاتی بعد به هدف برخورد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/71957" target="_blank">📅 18:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71954">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12842b3342.mp4?token=khIX51yn8tLBKF93hsCIxumijNlEs_phvltZ0vJ0tD-0qQ4ZTCM-Qgtf_JYOZpMJlw0AYT99IWu81EQ_Y0vM4kjJ3Wxv_1AX4oM6nmzsWNv765ibJyIOXkNZb1-YO9qc0arY6l1SDK8Zj6GyjqgFeNRqouSMM1cnuM2TIwNXBk8_UziozLAp_q9ZMVX5tcqYk3m2GDWOsQgwybF4OygU9pa4aRLbaIfO2nIWLzEzE-XCbjaV9RKnYM1pTh7kfDSCQW_CO29haIUhcoLilpl5HC4GM9mJsSiVPE0qzHfTLtS0ABXx0Crnlttj6FufQgVzQhyg2wajRp-Jp6g1L7VHXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12842b3342.mp4?token=khIX51yn8tLBKF93hsCIxumijNlEs_phvltZ0vJ0tD-0qQ4ZTCM-Qgtf_JYOZpMJlw0AYT99IWu81EQ_Y0vM4kjJ3Wxv_1AX4oM6nmzsWNv765ibJyIOXkNZb1-YO9qc0arY6l1SDK8Zj6GyjqgFeNRqouSMM1cnuM2TIwNXBk8_UziozLAp_q9ZMVX5tcqYk3m2GDWOsQgwybF4OygU9pa4aRLbaIfO2nIWLzEzE-XCbjaV9RKnYM1pTh7kfDSCQW_CO29haIUhcoLilpl5HC4GM9mJsSiVPE0qzHfTLtS0ABXx0Crnlttj6FufQgVzQhyg2wajRp-Jp6g1L7VHXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به گزارش رویترز، سامانه‌های پدافند هوایی در اربیل (واقع در اقلیم کردستان عراق) یک پهپاد را در نزدیکی فرودگاه اربیل سرنگون کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71954" target="_blank">📅 18:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71953">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی:
دخل و خرج زندگی مردم آمریکا با هم نمی‌خواند و آمریکایی‌ها در مسائل داخلی به جان هم افتاده‌اند
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71953" target="_blank">📅 18:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71952">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71952" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71952" target="_blank">📅 18:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71951">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7HxBsuRMhYyxrgxuSfbcRqpy1UZGDlNrlInviQYvq5ZC3t4jYgNFSV4O9J_qI21KoWCgP_XSVrfbHcgSOAkvxEOKSm6j9qCA5P9Cvh8RjqwOyNwtqlcS1AOv0hwasnOTn9kuskCaQuEtZNBdfZAwZZ66QyMPiXHLXH4mHy4I65rEJHO31w3NlnrVD7LW74LFHKMWgqdc8beGTGm0tYVYG0WtQlbQA3e-nDQq5gDFaeO4aZ19_CTGvActbI03nDaI19P--DQZ61YPieBySxeM8zrxWZBpuQgy6E-5V-7_aWzHfd8LgbbDqfyYZW0y0xH8IHKdPeDaPJVVXi1JFe6Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71951" target="_blank">📅 18:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71950">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ea24117fc.mp4?token=P2G6CKPo1MITCkfnmWRygsYyH31iNX4FVXcpUuEnvKRfpCX_vMLTDW-kSU8op1HAI9rH6_TtUJOyitZb-2k0DzUhn591hr9aJ8pZhs_pr_OXVmjbHig7eOb2HQmiUd1nekKcFkXusLEXrLugDjTXI5OVKwIE4jyjQFce9hwTW66wgcwRH9J9G-AbR3W6XcDPpc15SDfbbQhUMp9sAWMVGY0NiuiYobiC2d9YSN4VTgiHrOmi61L0-dOJUkOeOnfNy3TPVrt3y0mQ0rdZVj9xacliTSDywRpiWSX5YqxEYJh1ycevgE7bGCDZZp4WXC5HNqCh9-ozAiACq8I78zUP5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ea24117fc.mp4?token=P2G6CKPo1MITCkfnmWRygsYyH31iNX4FVXcpUuEnvKRfpCX_vMLTDW-kSU8op1HAI9rH6_TtUJOyitZb-2k0DzUhn591hr9aJ8pZhs_pr_OXVmjbHig7eOb2HQmiUd1nekKcFkXusLEXrLugDjTXI5OVKwIE4jyjQFce9hwTW66wgcwRH9J9G-AbR3W6XcDPpc15SDfbbQhUMp9sAWMVGY0NiuiYobiC2d9YSN4VTgiHrOmi61L0-dOJUkOeOnfNy3TPVrt3y0mQ0rdZVj9xacliTSDywRpiWSX5YqxEYJh1ycevgE7bGCDZZp4WXC5HNqCh9-ozAiACq8I78zUP5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
برخی از مقامات ایرانی همچون موش‌ها پنهان شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71950" target="_blank">📅 17:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71949">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ درباره ایران:  در «مرحله تصمیم‌گیری» هستم و در آینده‌ای نه چندان دور، اتفاقات بسیار بزرگی رخ خواهد داد.  گزینه‌ها عبارتند از: نابودی کامل ایران، رها کردن آن‌ها تا از نظر اقتصادی بپوسند، یا دستیابی به توافق.  بهتر است درست رفتار کنند!  @News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71949" target="_blank">📅 17:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71948">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0471fa6ac.mp4?token=XqD6yGII9NmQ-fJ4GUQXnxnRzGwrnUyVom3l9R_zzA9HUbiqtwCp9yO951CViM81O9mq3qkP7tLdMiJHXJ3NU0rCpTM6SAhIfq_csfgquQlHr6xzjj_cvRYGw9v-swriGocCSHX5ziqU1BJ3ZDO9Evy3BM_fCUsF3u9N26kzvm-OS2z5m1oaM1JFGtGd_BCnSBNa0oW2JWPgUFErUrHYMN6KPw3GAVjBicJN7lh9MVTZxvdw8RVMt7x1Fo9pvrWOYtpbJ8fXGWkQoTzeMK7PuFSbftVKVFYLBP1PLRdiYGrYoDteNPUnflAUPiRCbo1v6fJSjBC0RRAueoLY97qjaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0471fa6ac.mp4?token=XqD6yGII9NmQ-fJ4GUQXnxnRzGwrnUyVom3l9R_zzA9HUbiqtwCp9yO951CViM81O9mq3qkP7tLdMiJHXJ3NU0rCpTM6SAhIfq_csfgquQlHr6xzjj_cvRYGw9v-swriGocCSHX5ziqU1BJ3ZDO9Evy3BM_fCUsF3u9N26kzvm-OS2z5m1oaM1JFGtGd_BCnSBNa0oW2JWPgUFErUrHYMN6KPw3GAVjBicJN7lh9MVTZxvdw8RVMt7x1Fo9pvrWOYtpbJ8fXGWkQoTzeMK7PuFSbftVKVFYLBP1PLRdiYGrYoDteNPUnflAUPiRCbo1v6fJSjBC0RRAueoLY97qjaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس نیوز به نقل از ترامپ:
ترامپ می‌گوید «احتمالاً» برای دیدار با مسعود پزشکیان، رئیس‌جمهور ایران، در حاشیه مجمع عمومی سازمان ملل آمادگی دارد
😂
پزشکیان هفته آینده در نیویورک خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71948" target="_blank">📅 17:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71947">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6e65f0569.mp4?token=rlqdNwsMpggdYDoh-XKBtdmQRpEvJmWyMBLoLuur8EjeEXh1BO_eELr6ezu2mJyaxxx61UnH7uZZ87aXsUeX4KhC6D-0HhsJ6W0CGBRFxZ3OFaz3H5EdpEkKwmLQ9ZzizdZF1-vVWTWkZqBUL254T5DL2tRGiNnijb0j4t5DO3CV9BgrTW0pRF7XxziDM9fZ0socaCBJvp7XaqAO_W742p1-5R44dPX7Hr4tuiB-d17ys-TulVo5TyuluOM75r_C93p4tAg0Y_wKM8Z97sjb7SScC7Lj9JAbCXRtUSRfEQQjOTOljxfb026xZ-xvayOlOvlfo9arOcTlLYZr7tAQQYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6e65f0569.mp4?token=rlqdNwsMpggdYDoh-XKBtdmQRpEvJmWyMBLoLuur8EjeEXh1BO_eELr6ezu2mJyaxxx61UnH7uZZ87aXsUeX4KhC6D-0HhsJ6W0CGBRFxZ3OFaz3H5EdpEkKwmLQ9ZzizdZF1-vVWTWkZqBUL254T5DL2tRGiNnijb0j4t5DO3CV9BgrTW0pRF7XxziDM9fZ0socaCBJvp7XaqAO_W742p1-5R44dPX7Hr4tuiB-d17ys-TulVo5TyuluOM75r_C93p4tAg0Y_wKM8Z97sjb7SScC7Lj9JAbCXRtUSRfEQQjOTOljxfb026xZ-xvayOlOvlfo9arOcTlLYZr7tAQQYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
در «مرحله تصمیم‌گیری» هستم و در آینده‌ای نه چندان دور، اتفاقات بسیار بزرگی رخ خواهد داد.
گزینه‌ها عبارتند از: نابودی کامل ایران، رها کردن آن‌ها تا از نظر اقتصادی بپوسند، یا دستیابی به توافق.
بهتر است درست رفتار کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71947" target="_blank">📅 17:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71946">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3687d7bcf.mp4?token=pITrQoQlUitHvOzUZwOdKB6qkBXJiX25y_xtpRB66XMxYoP8b_x-6yNBAkY2FhuWAQk3lud4Lej9uU76kTmR7DZmMotUS0MEsF3tRTHaRX8fSS3K1GxLcWHZfZEmAueHI76k7DO9L34dVgmkK2t4zdfjmqWlndCoyGhWC9eOgr2Zihziz8PArVTNF-yFwrKoSv7L0QcG3LcHhQalS_iSAigRs48kwWivlC2WZHwdhaRk2FaCoecXWgupSPapzIIdR580NuTDXY8aozx9RbDcmnCcCNLSQPlVuPMmMM_yLH5qr7QW2GHLsvM0PfgRCaLzyBIpWEnCNXg2QX_6iFdxUjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3687d7bcf.mp4?token=pITrQoQlUitHvOzUZwOdKB6qkBXJiX25y_xtpRB66XMxYoP8b_x-6yNBAkY2FhuWAQk3lud4Lej9uU76kTmR7DZmMotUS0MEsF3tRTHaRX8fSS3K1GxLcWHZfZEmAueHI76k7DO9L34dVgmkK2t4zdfjmqWlndCoyGhWC9eOgr2Zihziz8PArVTNF-yFwrKoSv7L0QcG3LcHhQalS_iSAigRs48kwWivlC2WZHwdhaRk2FaCoecXWgupSPapzIIdR580NuTDXY8aozx9RbDcmnCcCNLSQPlVuPMmMM_yLH5qr7QW2GHLsvM0PfgRCaLzyBIpWEnCNXg2QX_6iFdxUjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهراب قاسم‌خانی نویسنده سریال پاورچین :
تو سریال یه اصطلاحی بین مهران مدیری و سحر زکریا ( نقش زن و شوهر ) بود که درباره " کوه رفتن " به هم میگفتن؛
مثلا زکریا به مدیری میگفت بیا بریم کوه، یا میگفت تو اوایل ازدواجمون بیشتر میومدی کوه،
ولی اصلا موضوع کوه نبود و داشتن درباره رابطه‌شون صحبت میکردن.
بعد از 5,6 قسمت مسئولان صداوسیما متوجه شدن و دیگه اجازه ندادن این دیالوگ تو سریال رد و بدل بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71946" target="_blank">📅 17:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71945">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/152e7c05de.mp4?token=A346TUMm2ldPDvhpEkxx_UuojC4ioiLm3GrWnA9NKYLS7ZGz9CDg0CzwNFLCBrXepVsBE4owsbQ7PLEoWbMTcMDcvEKzd6pcjdb2XIPpJGqojKrzYRcIiOtDPSc5pKdK64vyq92Oz8P_xTiQDLUG1rLSaK6308zc02nvdUnQDi95bytjZnTnmkXd3j1y9XrBOyXgMIsq4w3-_-LqeX293HIJzcB_muazPMFopVRFVQjNDzy8g0k6_Q5T-amwK5OBNhT2KgMuTgheodTpmAVfmMBu7DzPQTK3ITWgPaWZXt4mOWUtAl1ipDMICAtuWKnFtfaLBcGVW3SU9iKofTcfrIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/152e7c05de.mp4?token=A346TUMm2ldPDvhpEkxx_UuojC4ioiLm3GrWnA9NKYLS7ZGz9CDg0CzwNFLCBrXepVsBE4owsbQ7PLEoWbMTcMDcvEKzd6pcjdb2XIPpJGqojKrzYRcIiOtDPSc5pKdK64vyq92Oz8P_xTiQDLUG1rLSaK6308zc02nvdUnQDi95bytjZnTnmkXd3j1y9XrBOyXgMIsq4w3-_-LqeX293HIJzcB_muazPMFopVRFVQjNDzy8g0k6_Q5T-amwK5OBNhT2KgMuTgheodTpmAVfmMBu7DzPQTK3ITWgPaWZXt4mOWUtAl1ipDMICAtuWKnFtfaLBcGVW3SU9iKofTcfrIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار سلطانی :
100 میلیون بشکه نفت تو مملکت گم شده !
کسی که مسئول نظارت رو این موارد بود بهم گفته که 100 میلیون بشکه نفت رو نمیدونیم چی شده. نه تو دریا ریخته شده، نه امریکا تحریمش کرده و نه دزدای دریایی دزدیدنش.
به نیروی مسلح، قرارگاه فلان‌جا، نیروی انتظامی و ستاد کل چه ربطی داره که همشون دارن نفت میفروشن؟
اطلاعاتی نباید نفت بفروشه؛
اطلاعاتی سواد و فهمش رو نداره، درک نمیکنه. اطلاعاتی‌ای که 50 میلیون حقوق میگیره، میلیارد دلار، ترانزکشن، بیمه، حمل و نقل و این چیزها رو نمیفهمه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71945" target="_blank">📅 16:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71944">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1367899db.mp4?token=lrMYtRAb3GlgfvrPHveivT_UbSx667XTaAGI4USoOHNb_NHdrZclEsSdNv0EiyIswc0lyPg_9M0I261KPtIsYr3OpqpAgoKlp1MqBSvh9UgHuK0CcL6gH4YNSiRqKgCSrll3sc1JR9xq12yJsZrgl5dq8P-nQlVy8dE9bnN9L7hb7-vUHWHIHeYUHS4_14zfRLNUbxg7JCM24qj96O6ESgOUk_N-qq5V1NDGfy1uHVx3B0sFwjgYPQb6NZoUmHJOcZLkEDLNM-pzQgV1hnfaSa8tacIfBbWxFLp8gsBXN0_pa6taDRk5p6SG6n4_tQlBOZqDkntahaZv8Iz-fxMqTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1367899db.mp4?token=lrMYtRAb3GlgfvrPHveivT_UbSx667XTaAGI4USoOHNb_NHdrZclEsSdNv0EiyIswc0lyPg_9M0I261KPtIsYr3OpqpAgoKlp1MqBSvh9UgHuK0CcL6gH4YNSiRqKgCSrll3sc1JR9xq12yJsZrgl5dq8P-nQlVy8dE9bnN9L7hb7-vUHWHIHeYUHS4_14zfRLNUbxg7JCM24qj96O6ESgOUk_N-qq5V1NDGfy1uHVx3B0sFwjgYPQb6NZoUmHJOcZLkEDLNM-pzQgV1hnfaSa8tacIfBbWxFLp8gsBXN0_pa6taDRk5p6SG6n4_tQlBOZqDkntahaZv8Iz-fxMqTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساجده سلیمانی، مجری شبکه یک:
آقای جبلی میگن ۷۰ درصد مردم صداوسیما رو دنبال میکنن
والا من ۵ سال تو شبکه یک مجری بودم وقتی میرفتم بیرون جز یه مشت پیرمرد و پیرزن که صبح برای نماز بلند میشدن و تلویزیون میدیدن دیگه کسی منو نمیشناخت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71944" target="_blank">📅 16:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71941">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebc55859ee.mp4?token=Ro47h1HLyE_48AP5ffSNTq5w1wbXGv_1ftopYlp0HIQ2nhpni2rrvTKF7VLztqqhwYvvmsiIeN0llDzrWUcIXDTPjAdN9JtsPcHfx9aeDGCkn1KeEYUFmK_GRjgOHKaARwgcuHrCDzLvwBHrpLVqrZyPi2e_cdDOCuHp19WowFYHRlgN1astTNXYuClwn1OJ5XGP47l2gQWh1niOXSGTyjO3lImPKuAJUL22xCFhbSIruVa24fqWvIrO-CJINkD7IgjEdG5jL6o2czy8ZLZRL7uucOZbFRcr2yrFMhXSiYWE-apRrr_s8yWha--DiSChCex1a2_HXIAyGyJk9gygF2ZhVVprkUD0vSnI6I2g27pOKJzq2eIm62wd_ZM6T756oo_urR12AVX-pTR3ZQ4I9ZvjTWF0WX_XanMcLMvJWgXH1W4_Yw3iWKAuf3z7R-zNQbNUmWyA63pQjn1amwgJw56gQKOPDJ-9uQ7i9QIlXvjFsY2AQqixyQviVXrxZEiBVB3uVvH0x3wydzVdG6y5IHOe2o0OO9PUPCjZuo8Me2bzLuuNo35VwximRRHjXxrZRXr4_m5-XzkOe6OWRcYOqcTt_yH_BD7KXNqRj_vJtIvLXH3mO8NhS9SS9TNvI6_ftmUevFWpff8E38iq3t7Xn9MSg_-4eI3JKk-Sk6B0UuI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebc55859ee.mp4?token=Ro47h1HLyE_48AP5ffSNTq5w1wbXGv_1ftopYlp0HIQ2nhpni2rrvTKF7VLztqqhwYvvmsiIeN0llDzrWUcIXDTPjAdN9JtsPcHfx9aeDGCkn1KeEYUFmK_GRjgOHKaARwgcuHrCDzLvwBHrpLVqrZyPi2e_cdDOCuHp19WowFYHRlgN1astTNXYuClwn1OJ5XGP47l2gQWh1niOXSGTyjO3lImPKuAJUL22xCFhbSIruVa24fqWvIrO-CJINkD7IgjEdG5jL6o2czy8ZLZRL7uucOZbFRcr2yrFMhXSiYWE-apRrr_s8yWha--DiSChCex1a2_HXIAyGyJk9gygF2ZhVVprkUD0vSnI6I2g27pOKJzq2eIm62wd_ZM6T756oo_urR12AVX-pTR3ZQ4I9ZvjTWF0WX_XanMcLMvJWgXH1W4_Yw3iWKAuf3z7R-zNQbNUmWyA63pQjn1amwgJw56gQKOPDJ-9uQ7i9QIlXvjFsY2AQqixyQviVXrxZEiBVB3uVvH0x3wydzVdG6y5IHOe2o0OO9PUPCjZuo8Me2bzLuuNo35VwximRRHjXxrZRXr4_m5-XzkOe6OWRcYOqcTt_yH_BD7KXNqRj_vJtIvLXH3mO8NhS9SS9TNvI6_ftmUevFWpff8E38iq3t7Xn9MSg_-4eI3JKk-Sk6B0UuI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حمله گسترده پهپادی اوکراین به پالایشگاه کاپوتنیا در مسکو، روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71941" target="_blank">📅 15:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71940">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8ac28a42.mp4?token=RVRKHASNxq5wLFAqbBYkbqUMWtNt06Ta2Cb6Z2HCXoYOy-Aya8a6p5EsyFLEQ06IMM251QMTr5t111ef1BxiEyWD0Va6dv_qnbQN9wwG640C-081SCiQigjw5RnwbaP7JrdMeEUWgbQ2LM_xEiAL7kVbYOk9HvKhpdOlFVLRGUTLTf-80PhxUP9ri1MzHqZp_MTXh8-lNrXmp-Axju4b090DuQbxRd45WUqWvtPW5g2kVGeqgZOYAKfkm6iKVPpYGkzXyYMIAEjLwe1wsN9kMhJOQS9MDfgpnvRR4tRxh8HTqII26gWHrFzlUlksCe2zpXi5WdXiI8C2cdK69-qdpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8ac28a42.mp4?token=RVRKHASNxq5wLFAqbBYkbqUMWtNt06Ta2Cb6Z2HCXoYOy-Aya8a6p5EsyFLEQ06IMM251QMTr5t111ef1BxiEyWD0Va6dv_qnbQN9wwG640C-081SCiQigjw5RnwbaP7JrdMeEUWgbQ2LM_xEiAL7kVbYOk9HvKhpdOlFVLRGUTLTf-80PhxUP9ri1MzHqZp_MTXh8-lNrXmp-Axju4b090DuQbxRd45WUqWvtPW5g2kVGeqgZOYAKfkm6iKVPpYGkzXyYMIAEjLwe1wsN9kMhJOQS9MDfgpnvRR4tRxh8HTqII26gWHrFzlUlksCe2zpXi5WdXiI8C2cdK69-qdpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانگین آی‌کیو یمنی‌ها:
یه حوثی پین نارنجک رو کشید واسه اینکه نشون بده خدا باهاشه و نتیجه شد این.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71940" target="_blank">📅 15:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71939">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">قرارگاه خاتم الانبیا:
هرگونه حمله به ایران، منجر به حملات «مداوم، مؤثر و دردناک» به تمامی پایگاه‌ها و منافع آمریکا در منطقه، «بدون هیچ‌گونه محدودیتی» خواهد شد.
کشورهای منطقه‌ای که با تجاوز آمریکا همراهی کنند، شریک این حمله محسوب شده و نباید انتظار خویشتن‌داری ایران را داشته باشند.
بر اساس اطلاعات دریافتی آمریکا با چراغ سبز متحدان منطقه‌ای خود و بر اساس هماهنگی‌های صورت‌گرفته در یک نشست اروپایی، در حال برنامه‌ریزی اقداماتی جدید علیه ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71939" target="_blank">📅 14:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71938">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abf3ef96ed.mp4?token=byYZ15O1KHTXIDVWEukG_-cInwMdWQfzXQZ3OiUc1x_Ioi_qImMEBv396PBwlNOLFO5IpfR-wSZt5U2g-Bd1jR1jo1DrtAZIK-7r6ortIN1em23BPrp8YcLQKEYNmclCu3CltNQLqvlaaB7Fzpm_nGCQ8rO92cJxWrRiCOHxJLLRDxfuosY_tYZoeF1BBi0OpezKkpgGS0I4Yh7UOQGS-cE_9hF7JNGYDd7taYGwBJHoo_vdPwqsM6DcWWCg9ZEhGXgRV550-quw36x_2Pjnb20G7uC-u36LmQSrSmGjTddpiUs7SAn1IXZSt6mdnjGVmg8_g3E7SbFNK730mARC6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abf3ef96ed.mp4?token=byYZ15O1KHTXIDVWEukG_-cInwMdWQfzXQZ3OiUc1x_Ioi_qImMEBv396PBwlNOLFO5IpfR-wSZt5U2g-Bd1jR1jo1DrtAZIK-7r6ortIN1em23BPrp8YcLQKEYNmclCu3CltNQLqvlaaB7Fzpm_nGCQ8rO92cJxWrRiCOHxJLLRDxfuosY_tYZoeF1BBi0OpezKkpgGS0I4Yh7UOQGS-cE_9hF7JNGYDd7taYGwBJHoo_vdPwqsM6DcWWCg9ZEhGXgRV550-quw36x_2Pjnb20G7uC-u36LmQSrSmGjTddpiUs7SAn1IXZSt6mdnjGVmg8_g3E7SbFNK730mARC6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نجمه امینی، دانشجوی ۲۳ ساله و بازداشت شده در جریان انقلاب ملی در مشهد که او را محکوم به اعدام کرده‌اند، در تماسی تلفنی از زندان وکیل‌آباد مشهد از همه مردم خواست تا صدای او باشند.
درود به مردم عزیز ایران، حکم اعدام من صادر شده، لطفا صدای من باشین، من یه جوونم با کلی آرزو.
تروخدا فقط صدای منو نشنوین، اونو نشر بدین و صدای من باشین، من بی گناهم.
شاید این آخرین صدایی باشه که از من میشنوین چون شاید دیگه نتونم حرف بزنم، ولی تنها امیدم ایران آباد و آزاده.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71938" target="_blank">📅 13:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71937">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4daecc7856.mp4?token=IewjoSoMjC0tMe74seiKBgFbjavnCahpxYxSSoqO5p9cF9vOBAukqFMadbmKF7z8sD645yeatsmVCwHNVpW-8H4aEn-gdOVzao2-cZfVCwhNPvUOdiLBYRghh1tcO0B7uwyYildyo5AwgzGzIFrzQa-fswmi1ng6tLnWm0GJA_hLHfGKmreRuVbNiOLNOn3ZK_qrceTDmfxzJ_Hi5NriwKBW5q9FxbmWIPf5V9ictrZCtWT0cfsIjAbAkgOs3WgWioqtTQzICyxK6iq5I148MjUu4XK9A_dnb9EK-rSUs2jGlYEpgwWxXhZCrSicfPX-AvmJX3mN0Q4SI3VdZBD13A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4daecc7856.mp4?token=IewjoSoMjC0tMe74seiKBgFbjavnCahpxYxSSoqO5p9cF9vOBAukqFMadbmKF7z8sD645yeatsmVCwHNVpW-8H4aEn-gdOVzao2-cZfVCwhNPvUOdiLBYRghh1tcO0B7uwyYildyo5AwgzGzIFrzQa-fswmi1ng6tLnWm0GJA_hLHfGKmreRuVbNiOLNOn3ZK_qrceTDmfxzJ_Hi5NriwKBW5q9FxbmWIPf5V9ictrZCtWT0cfsIjAbAkgOs3WgWioqtTQzICyxK6iq5I148MjUu4XK9A_dnb9EK-rSUs2jGlYEpgwWxXhZCrSicfPX-AvmJX3mN0Q4SI3VdZBD13A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
اسرائیلی‌ها تونل‌های خالی در لبنان را برای اهداف تبلیغاتی و نمایش انتخاباتی منفجر کردند. آن‌ها عکس و فیلم گرفتند و گفتند: «ببینید نتانیاهو چقدر قدرتمند است.»
همه این‌ها تبلیغات است و همگی به انتخابات مربوط می‌شود.
اما کار ما مبتنی بر اصول است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71937" target="_blank">📅 12:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71936">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ea49a57b9.mp4?token=NEKEbPLPTCPHueRAW4QNW8LoRIHhg73xvNChHi_djKNjE9r3QzDyDnN_fqab2pNI2o0Rgv4oVbuwS_BK2UeQQcdKq8e6gw6xnft3DirsALGlWx3Nzfl-XWkblUlr_u2A4vyc4iC6DP2qoa-IANqGi24VHYca990HDGKbtI9YgdvMSls7ekKaA40LcMNy5n4KKOy7PKmfsNmjkMC3nycLdx6ISNDvpSDuYOcSw-oP0Nn0N1qxHAPbfusjWi6M2zanlpEKgiSYp2I18aQuY8LGQ98gUjCTzu2CAwt8x1au5-jDee0H5mEfHp8ofBlrkf_WeojFjBI6hzevtzvU3Z4-Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ea49a57b9.mp4?token=NEKEbPLPTCPHueRAW4QNW8LoRIHhg73xvNChHi_djKNjE9r3QzDyDnN_fqab2pNI2o0Rgv4oVbuwS_BK2UeQQcdKq8e6gw6xnft3DirsALGlWx3Nzfl-XWkblUlr_u2A4vyc4iC6DP2qoa-IANqGi24VHYca990HDGKbtI9YgdvMSls7ekKaA40LcMNy5n4KKOy7PKmfsNmjkMC3nycLdx6ISNDvpSDuYOcSw-oP0Nn0N1qxHAPbfusjWi6M2zanlpEKgiSYp2I18aQuY8LGQ98gUjCTzu2CAwt8x1au5-jDee0H5mEfHp8ofBlrkf_WeojFjBI6hzevtzvU3Z4-Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضایی:
پرسش من از مقامات عرب این است: اگر ایران مقاومت نمی‌کرد و ناچار به تسلیم می‌شد، آیا اسرائیل امروز به عربستان سعودی حمله نمی‌کرد؟ آیا اسرائیل تا دمشق پیشروی نمی‌کرد؟ آیا اسرائیل به عراق حمله نمی‌کرد؟
ما در اینجا شهید دادیم و از کشورهای عربی دفاع کردیم. اگر بینی آمریکا و اسرائیل را در اینجا، در ایران، به خاک نمی‌مالیدیم و اگر آن‌ها در ایران احساس پیروزی می‌کردند، دیگر کسی در منطقه باقی نمی‌ماند که بتواند در برابرشان بایستد.
اسرائیل به تمام کشورهای عربی حمله می‌کرد و آمریکا نیز از آن حمایت می‌نمود. ما مقاومت کردیم — بله، ما از کشور خودمان دفاع کردیم — اما دفاع ما به نفع کشورهای عربی نیز تمام شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71936" target="_blank">📅 12:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71935">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c2df1caeb.mp4?token=tBY4Fsl3TIDxHygO7d3fK90qp4-B8tk3LlPbx--ziyAZQo4qoWeWgZ1V6yDkyOFV_3Qbqb6cBqOeL2QAjL3ahZevmD3ZVdNcfohIJtu7qerI19gWilTnRbvIALzuf66qEPhkynAJRo5XMkRfneodrcJdMMjPzz34Y1yyVxBxwemSReHgXsS2sy2s1X4_MBJUMqn5kPMT0a4_Tqj3M06Q59iosE9HyFg0CnkQx8eE9x7pjju1PCps-K16v-5I63DU3UV1VEXrv8iiMqCJi6q-dMeRMzSatf13OOd-MaGL3MKxmWjE2abwB2CcD8p04Va01acZJr-PSM3Hb5KJCRaGsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c2df1caeb.mp4?token=tBY4Fsl3TIDxHygO7d3fK90qp4-B8tk3LlPbx--ziyAZQo4qoWeWgZ1V6yDkyOFV_3Qbqb6cBqOeL2QAjL3ahZevmD3ZVdNcfohIJtu7qerI19gWilTnRbvIALzuf66qEPhkynAJRo5XMkRfneodrcJdMMjPzz34Y1yyVxBxwemSReHgXsS2sy2s1X4_MBJUMqn5kPMT0a4_Tqj3M06Q59iosE9HyFg0CnkQx8eE9x7pjju1PCps-K16v-5I63DU3UV1VEXrv8iiMqCJi6q-dMeRMzSatf13OOd-MaGL3MKxmWjE2abwB2CcD8p04Va01acZJr-PSM3Hb5KJCRaGsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
آمریکا و ترامپ خواهند رفت. همه می‌دانند که اقتصاد آمریکا در واقعیت، در مسیر فروپاشی قرار دارد. آمریکا طی ۱۰ سال آینده، دیگر آن کشوری نخواهد بود که امروز هست.
اما ما و کشورهای عربی باقی خواهیم ماند. ما خودمان باید وضعیت منطقه را سامان دهیم. ما باید امنیت خلیج فارس را برقرار کنیم، پیمانی برای همکاری اقتصادی شکل دهیم و در منطقه با یکدیگر دوست باشیم.
ما یک خانواده هستیم؛ خانواده خلیج فارس. ما هشت کشوریم و باید بر بازسازی و توسعه اقتصادی تمرکز کنیم، با یکدیگر همکاری داشته باشیم، در سرمایه‌گذاری‌های هم مشارکت کنیم و حتی به سمت ایجاد واحد پولی مشترک و بازار مشترک واحد حرکت کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71935" target="_blank">📅 12:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71934">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed047a6e6.mp4?token=ogBwV-JeMLJBrXXG_zwRwM05q4NElTc8sOYWmhfI2VFnKh2UTEgAh4KMnbxHyrjcFon7SsU9ohYjY5mOCLLR9fAbXvUt-M4Z1ObJlhgX6pVC8iilCtwRancluzuCHNgPoW2vlgempKeMuAZzCUA3wxAiNLPqr52qjHZMJa6nqefYvCDjLSCokoMllhIGKk8SEjLQgM6dOV9kV1EF-o4LVcrtf8T4QX55vMPaMLjdo11q_1FN6yHBscyF6hgRfdXjqVkiup8NFyIaO36uBrhiYbRedWjpN_XnxTMWs8zCBhisQ4iYlmlwQD5sD6ReflB80DwSGt5D27ycCwf5mqwpfwIdup5RJcVBRiSus5y1i2_jyoQ7kDdH6-UMfLikyWvB5k2zosDQRdkukO_RekYkpMHjXX8SMO4LAGdKWk_0idVe0g2vf-r0rTTDEIlfQrhMtGDirFp8Mv7AuoxPhgpya0sNVskov1WWCq2VMS9qCxBkWySaG5Ogy3EvKEMklqBP6YK-QaJ70COZqQvM9SK_ZhQUIJxS8ZVkgqgaZY9MlObZXfGL_koZYdTx-Zn8lzZqsFqQdoBT8Cep46gd32qsv_qHTska7YXVAnp6HnZbteL8YX-lxbKX4BoDkryXaGMxaF8zU-kraTnJQMEQEeR6QjLBNRA4zu1waCsUwj-Yhxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed047a6e6.mp4?token=ogBwV-JeMLJBrXXG_zwRwM05q4NElTc8sOYWmhfI2VFnKh2UTEgAh4KMnbxHyrjcFon7SsU9ohYjY5mOCLLR9fAbXvUt-M4Z1ObJlhgX6pVC8iilCtwRancluzuCHNgPoW2vlgempKeMuAZzCUA3wxAiNLPqr52qjHZMJa6nqefYvCDjLSCokoMllhIGKk8SEjLQgM6dOV9kV1EF-o4LVcrtf8T4QX55vMPaMLjdo11q_1FN6yHBscyF6hgRfdXjqVkiup8NFyIaO36uBrhiYbRedWjpN_XnxTMWs8zCBhisQ4iYlmlwQD5sD6ReflB80DwSGt5D27ycCwf5mqwpfwIdup5RJcVBRiSus5y1i2_jyoQ7kDdH6-UMfLikyWvB5k2zosDQRdkukO_RekYkpMHjXX8SMO4LAGdKWk_0idVe0g2vf-r0rTTDEIlfQrhMtGDirFp8Mv7AuoxPhgpya0sNVskov1WWCq2VMS9qCxBkWySaG5Ogy3EvKEMklqBP6YK-QaJ70COZqQvM9SK_ZhQUIJxS8ZVkgqgaZY9MlObZXfGL_koZYdTx-Zn8lzZqsFqQdoBT8Cep46gd32qsv_qHTska7YXVAnp6HnZbteL8YX-lxbKX4BoDkryXaGMxaF8zU-kraTnJQMEQEeR6QjLBNRA4zu1waCsUwj-Yhxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
اگر آمریکایی‌ها جدی هستند، بگذارند سربازانشان بیایند و وارد ایران شوند. چرا وارد نمی‌شوند؟
در جنگ‌ها، این نیروهای زمینی هستند که همیشه حرف آخر را می‌زنند.
چرا لشکر‌های هوابرد نمی‌آیند؟ چرا نیروهای زمینی آمریکا وارد ایران نمی‌شوند؟ چرا فقط از آسمان بمباران می‌کنند و سپس می‌روند؟
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71934" target="_blank">📅 12:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71933">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4920ecc6.mp4?token=rIARMMiA34TfZVJKig5qk32HNuyTGbKk_IP3t-b3N8nTSfRAeMct7AYDQ1fBi-Zz-7F_Z0bPmbrk2H4Aw0zx2HAl3cV69l9Mgvzbrk_lFNIiYLbgfAKo3JOisjVIETkTRdlfyhkuQr97GwhuNT6W1MydE8CIcB5J2Kjzn5kMMsp8F9vbFWElbPvATecQz8WX7XC3ZjEb8rtzFz7DpKTN-TRZFWIiamm5BP85Q_dFy7wETW3uRYIwEkvW3LyuMcOlD7HAnTWMomuH87ZKUYkrRebKRnr56g1GidvfNbOSnxIqWVXFFR58ACnbcoHAaGra5GuYKRpOqTbXmO_sybcFCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4920ecc6.mp4?token=rIARMMiA34TfZVJKig5qk32HNuyTGbKk_IP3t-b3N8nTSfRAeMct7AYDQ1fBi-Zz-7F_Z0bPmbrk2H4Aw0zx2HAl3cV69l9Mgvzbrk_lFNIiYLbgfAKo3JOisjVIETkTRdlfyhkuQr97GwhuNT6W1MydE8CIcB5J2Kjzn5kMMsp8F9vbFWElbPvATecQz8WX7XC3ZjEb8rtzFz7DpKTN-TRZFWIiamm5BP85Q_dFy7wETW3uRYIwEkvW3LyuMcOlD7HAnTWMomuH87ZKUYkrRebKRnr56g1GidvfNbOSnxIqWVXFFR58ACnbcoHAaGra5GuYKRpOqTbXmO_sybcFCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
اگر جنگی دوباره آغاز شود، کشتی‌های آمریکا — مگر اینکه اقیانوس هند را ترک کنند — در هر کجای این اقیانوس که باشند، هدف حمله قرار خواهند گرفت. ما به این توانمندی‌ها دست یافته‌ایم.
ما سرعت موشک‌های هایپرسونیک (مافوق صوت) خود را از ۶ ماخ به ۱۰ ماخ افزایش داده‌ایم.
همچنین سامانه‌های جنگ الکترونیک خود را توسعه داده و پدافند هوایی‌مان را ارتقا بخشیده‌ایم؛ علاوه بر این، تدابیر دیگری نیز داریم که در زمان مناسب از آن‌ها استفاده خواهیم کرد.
بنابراین، ما کاملاً آماده‌ایم. اگر آمریکا جنگی را آغاز کند، با نیرویی بیشتر و ضرباتی پرتعدادتر و دردناک‌تر با آن مقابله خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71933" target="_blank">📅 12:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71932">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71932" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71932" target="_blank">📅 12:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71931">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ch2KGntZ6Cp4LG3EeIhSa6F4R4F0fzt5rn-PGlyrPTI9flT-qRKolu9erxPnczQUUqQMKrtGut4YVZ73g-xZ6gRnYhSpqQihNV4cb629vtpDMF79Q3G9-xo4Q4zQTcbdZj7i5ULj-sdecTs8bOaO0OWPXOeVvd5nKrGCZU65IDN47WNA9GEalY93aXb1q2jaZeAcpCmFHA1h88Kng-Ydc6h3g9MU7VuZ1NTLBei6yY8kpMhlqL1jgIn7iuAqQFeaS0oyMbMtSkdHZ0jQotZRfSLXLt6neEIOWM8K6QhhXrf3qlSfhOX06hWZN8R7NpsxpiQNwTAs1P4-FLfWgFPsAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
رویارویی غول‌های مادرید!
🦖
نبرد هیجان انگیز رئال مادرید
🆚
اتلتیکو مادرید را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ رویارویی اخیر دو تیم:
رئال مادرید: ۳ برد، ۲ شکست و ۹ گل زده
اتلتیکو مادرید: ۲ برد، ۳ شکست و ۱۰ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71931" target="_blank">📅 12:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71930">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf2e9358bf.mp4?token=qnBJH03fvYu5yua106HEyl4oGKNnfJKSU3rF-57TbZHbZwoEZmD3RKg37yAwz2zfMrkFGBPArDYoNmZHUP_I9fi53h8ez-kIOPgfL4koZELYou6xdiCYwnnWpMG8vwIVu5LflYBVGuYuk5erVOuvIjGlayZSCY9lHbnDUHNEKGxTL43D5TfBHP9LsIFoDZd7H96EMAhzYmfgtkuLfgULHYbl6ISEblYdRcZsCC9w0lkifu1aUNWT3i7bnC29x6_CgKWd2718gHVcSWd50dvuzh709IU2TEsIveRGk8qMbse5zVe1gYionB1YniyVUWIQaoHmp97dJu9Gs-F0d4Iq2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf2e9358bf.mp4?token=qnBJH03fvYu5yua106HEyl4oGKNnfJKSU3rF-57TbZHbZwoEZmD3RKg37yAwz2zfMrkFGBPArDYoNmZHUP_I9fi53h8ez-kIOPgfL4koZELYou6xdiCYwnnWpMG8vwIVu5LflYBVGuYuk5erVOuvIjGlayZSCY9lHbnDUHNEKGxTL43D5TfBHP9LsIFoDZd7H96EMAhzYmfgtkuLfgULHYbl6ISEblYdRcZsCC9w0lkifu1aUNWT3i7bnC29x6_CgKWd2718gHVcSWd50dvuzh709IU2TEsIveRGk8qMbse5zVe1gYionB1YniyVUWIQaoHmp97dJu9Gs-F0d4Iq2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لیلی فلیپس پورن استار آمریکایی، موقع انجام کار‌ نیک راهی بیمارستان شد.
امروز در حین تلاش برای شکستن رکورد بیشترین تعداد سکس تو ۲۴ ساعت، دقایقی بعد از آغاز عملیات یکی از مردایی که باهاش رابطه داشت پاشید تو صورتش و بیناییش بشدت به مشکل خورد و راهی بیمارستان شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71930" target="_blank">📅 11:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71929">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146935a692.mp4?token=qAbfMOb4YzL3wBEmA1J6Uax7xFcrEYSrnA-q64wF1MTQ-fORl-hY3Wvz1PBiPIXvMhFk4DgxQapXwUtKLolupnL4V3a2mGYH-bwCi5UtC7cFgbr1ylD8OAw3QR2vYfYeeIaACKj7Sv80DTH_UTM4O9EvyfpcEIX3lq-xeB7AKDlAcMy-COcdaTMEHhquwpCr0knLSeZj3xMHllVsY11djzfemexk7Kn72nHazSKEbUR0ctBk2GnfDcZKYZxlB34Ia4IB8V8H5ozrl97K8jNZmtSgHZAzN3KgFOOzdOaOmQAQHzfhV2NeHjyhJA4WUx_SxXT_nJbeQD5-gT9xOpXVjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146935a692.mp4?token=qAbfMOb4YzL3wBEmA1J6Uax7xFcrEYSrnA-q64wF1MTQ-fORl-hY3Wvz1PBiPIXvMhFk4DgxQapXwUtKLolupnL4V3a2mGYH-bwCi5UtC7cFgbr1ylD8OAw3QR2vYfYeeIaACKj7Sv80DTH_UTM4O9EvyfpcEIX3lq-xeB7AKDlAcMy-COcdaTMEHhquwpCr0knLSeZj3xMHllVsY11djzfemexk7Kn72nHazSKEbUR0ctBk2GnfDcZKYZxlB34Ia4IB8V8H5ozrl97K8jNZmtSgHZAzN3KgFOOzdOaOmQAQHzfhV2NeHjyhJA4WUx_SxXT_nJbeQD5-gT9xOpXVjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوکراین شب گذشته یکی از بزرگترین حملات پهپادی خود را علیه مسکو انجام داد.
روسیه مدعی است که بیش از ۱۶۰۰ پهپاد، از جمله ۴۵۰ پهپادِ عازمِ مسکو، سرنگون شده‌اند.
این حملات به پالایشگاه نفت «کاپوتنیا» (بزرگترین پالایشگاه مسکو) و ساختمان‌های مسکونی اصابت کرد که منجر به کشته شدن دو نفر در منطقه مسکو و تخلیه ۴۰۰ نفر از ساکنان شد.
محدودیت‌های پروازی در فرودگاه‌های مسکو اعمال شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71929" target="_blank">📅 11:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71926">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f7f510c35.mp4?token=o3eGMNUgRybh-xXN0Fr99HFCsTzHfnOK4Lb1cOajOC3M5Mt2pYa4jFC8iKkwWW5B3yDZt06i1CM7GVTD8pcgV0TF_X047BxqZpMzRE6Y_Blxqwc0hUiWI6EvmOLSX03ksOHjLINwLcWLyf7DjoOWhExSzxzT2UmKuEaRccBCwWtknF0Vuc9bdLLOCvTEaNvjLIub1SWA18tdmKHP3rKjvgsUqbuy1nGdnUchDa30ET-QalFpNQGi_gIqtgMQ0AZjQ_KEyAs84ZOo-pJagJYHhja7SrRAFO0ciSv1dhpTNyDm10AlJvGYefnQgooqfubxD7lhwZP1Li81zJ3BWpujiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f7f510c35.mp4?token=o3eGMNUgRybh-xXN0Fr99HFCsTzHfnOK4Lb1cOajOC3M5Mt2pYa4jFC8iKkwWW5B3yDZt06i1CM7GVTD8pcgV0TF_X047BxqZpMzRE6Y_Blxqwc0hUiWI6EvmOLSX03ksOHjLINwLcWLyf7DjoOWhExSzxzT2UmKuEaRccBCwWtknF0Vuc9bdLLOCvTEaNvjLIub1SWA18tdmKHP3rKjvgsUqbuy1nGdnUchDa30ET-QalFpNQGi_gIqtgMQ0AZjQ_KEyAs84ZOo-pJagJYHhja7SrRAFO0ciSv1dhpTNyDm10AlJvGYefnQgooqfubxD7lhwZP1Li81zJ3BWpujiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزارت امور خارجه آمریکا با توجه به تحولات منطقه، هشداری امنیتی برای آمریکایی‌های ساکن خاورمیانه در خصوص احتمال بسته شدن حریم هوایی صادر کرده است.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71926" target="_blank">📅 10:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71925">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">شاهزاده رضا پهلوی:
با توجه به شرایط جدید، تاکتیک‌ها و روش‌های اجرایی مخالفان جمهوری اسلامی تغییر کرده، اما هدف همچنان سرنگونی جمهوری اسلامی و دستیابی به ایرانی آزاد و آباد است.
«ما امروز با تجربه‌تر و مصمم‌تر از هر زمان دیگری هستیم. هدف ما مشخص است، سرنگونی جمهوری اسلامی و رسیدن به یک ایران آزاد و آباد.»
ایشان گفتند: «چهار اصل کلیدی ما مشخص است:
حفظ تمامیت ارضی ایران
جدایی دین از حکومت
آزادی‌های فردی و برابری همه شهروندان در قانون
حق ملت در مشخص کردن شکل آینده حاکمیت ایران از طریق صندوق رای آزاد و منصفانه
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71925" target="_blank">📅 09:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71924">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eacbff262.mp4?token=kD-hoL80ZkzAMRJmxb5rTum2c3vtXib08WYfVgqDzjp-M9O6L7ett3JGj0hWLULeyApdpQY1q95nIKximCE7QprhANgCZKIhiX2Ly71aJhNDVUcAt0CFhRzfHk3isdqVKXJsslTrWlu5xAjjv75I7rVifmMq7EUVJU02c-WqYjyrnGnyeVSzvOufLhxIpFRP4f4dFTD3_ZWo9WqeDufaPpc2yJYQPsyKTW8297BPL_6daNJjSNR4saMiydGm3FX4IM3vofedFslJV_JqcjXiLlnVgpz3ByW6DZHQ6H7ZVnUxf8TF_l5VqTK74Itloa7mN49QOndzMDJyu7YOc6WBbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eacbff262.mp4?token=kD-hoL80ZkzAMRJmxb5rTum2c3vtXib08WYfVgqDzjp-M9O6L7ett3JGj0hWLULeyApdpQY1q95nIKximCE7QprhANgCZKIhiX2Ly71aJhNDVUcAt0CFhRzfHk3isdqVKXJsslTrWlu5xAjjv75I7rVifmMq7EUVJU02c-WqYjyrnGnyeVSzvOufLhxIpFRP4f4dFTD3_ZWo9WqeDufaPpc2yJYQPsyKTW8297BPL_6daNJjSNR4saMiydGm3FX4IM3vofedFslJV_JqcjXiLlnVgpz3ByW6DZHQ6H7ZVnUxf8TF_l5VqTK74Itloa7mN49QOndzMDJyu7YOc6WBbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی:مجتبی مفقود است و اگر هم زنده باشد در تاریکی زیرزمین جرأت آن را ندارد که حتی صدایی از خود منتشر کند :))
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71924" target="_blank">📅 09:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71923">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d403914707.mp4?token=IAuBQoRLi3s-60O_JrpLhoiD15uikpe0jeGcZEYKhQsZgn5pLiwBFUAF5ZSzNZ3AaNrFTU5HR8nxkQ3Dzq695oGZTkUsYJEMwuBjkhcZAHj-3P-o_5fcvVUVOnetB-LBZUram22Xchi9ot5IPVTErbmNeTYSe0Pctr-49xmACwNjktaN0JbmBPJ-HYRB7E5aIXAoTdImitZ81IkIHBACcGcbqOBdRyK4g1vE27JquG_eNd3XnI7q_hz18i2lYa1-cEg9z-OQh1kFpS7nsEwOCbUL4uSL-EBnZJ0EMWXMnwV09dFlTVRMoEECTHkscRXWT0240r3gaAIy9qJWdEFGCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d403914707.mp4?token=IAuBQoRLi3s-60O_JrpLhoiD15uikpe0jeGcZEYKhQsZgn5pLiwBFUAF5ZSzNZ3AaNrFTU5HR8nxkQ3Dzq695oGZTkUsYJEMwuBjkhcZAHj-3P-o_5fcvVUVOnetB-LBZUram22Xchi9ot5IPVTErbmNeTYSe0Pctr-49xmACwNjktaN0JbmBPJ-HYRB7E5aIXAoTdImitZ81IkIHBACcGcbqOBdRyK4g1vE27JquG_eNd3XnI7q_hz18i2lYa1-cEg9z-OQh1kFpS7nsEwOCbUL4uSL-EBnZJ0EMWXMnwV09dFlTVRMoEECTHkscRXWT0240r3gaAIy9qJWdEFGCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده‌ رضا پهلوی:
«امروز این (جاویدشاه) یک شعار است .
یک شعار پشتیبانی و من از صمیم قلب سپاس گزارم.
کاری بکنیم که اون روزی که صندوق رای در تهران برقرار شد تبدیل  به رای بشه , نه یک شعار .»
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71923" target="_blank">📅 09:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71922">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71922" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71922" target="_blank">📅 01:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71921">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/el7u-DRvv-1jrdw8SnhkoL3UX5jbKrIVMF5Bl2J8qT_3x63x8GnQs9lXfVAAH-nY2y-1AXVTU7hnDq-M3Y-6cwJoZMKIuLmUqoq1ZFouddiP3EYP5gIH8CaSBnpCeZ1ncpenWljq7isolFbbefflc3yFnixj2z_I_d3SXl0RhpTHxHITAEqGriEPliamKDTLQ8Rd3S4goub38-PTEFPEV1I6iPW0kNB_RHH2O7N7aKnrrJbSblX0QIhw7baq55LRD3cpXpy3KiliBvVwtnZ8sr54dSFQ78pmL_gSYrjjVOteQg7Zt37BuKB3dZQ6br3B5ino7edL3RYunE_oJcUv8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه‌ای و تجربه‌ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71921" target="_blank">📅 01:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71920">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEN6xc7yb57EP-cpwGGSxZaiO2qQOs59Gg-qt7LdwRBhkJHFaCBDG3rmv78bb1S17DpdAha0yTnF8V0_B5Nuv7FwfrvKvqTgDWqZE6b_SrjXO_AOc3A5RV5VzgKTHCYPLC0tBAMR-NSTWQAdRvxFOkPViiIwyGAMsGIC3_GAWnD8FWrVJft1h5lZwOVgXSN09usNDiUA9A-aRXgdS9pZc-pZTmzvZABMz2600LiHe7D4BpN1mo6RgzJRO4z83_p9yBTwKIH1ioXlnJ3Z6JC-i9050ycGS1U0WOZ0dBR8mMr6d7JrKU11JDOiUO7T_sEwdWGkfmlfDJayVy18fK-pzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه آمریکا با توجه به تحولات منطقه، هشداری امنیتی برای آمریکایی‌های ساکن خاورمیانه در خصوص احتمال بسته شدن حریم هوایی صادر کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71920" target="_blank">📅 01:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71919">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">هشدار جدید آمریکا برای شهروندانش در خاورمیانه:
بر اساس آخرین اطلاعات منتشرشده، عربستان سعودی، بحرین، کویت و قطر در سطح «۳؛ تجدیدنظر در سفر» قرار دارند.
آمریکا در مورد عربستان نسبت به خطر حملات پهپادی و موشکی، درگیری مسلحانه و تهدیدهای تروریستی هشدار داده است.
در بحرین نیز آمریکا به تهدید حملات پهپادی و موشکی و اختلال در پروازهای تجاری اشاره کرده و سفر به این کشور را در سطح «تجدیدنظر در سفر» قرار داده است.
هشدار آمریکا درباره کویت نیز همچنان در سطح ۳ قرار دارد و از تهدید درگیری مسلحانه و حملات پهپادی و موشکی به‌عنوان عوامل اصلی این هشدار نام برده شده است.
در قطر نیز وزارت خارجه آمریکا نسبت به تهدید ناشی از درگیری مسلحانه، اختلال در پروازها و خطرات مرتبط با وضعیت امنیتی منطقه هشدار داده و از شهروندان خود خواسته برای احتمال تشدید شرایط آماده باشند.
در همین حال، لبنان در سطح بالاتری از هشدار قرار دارد و وزارت خارجه آمریکا از شهروندانش خواسته به لبنان سفر نکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71919" target="_blank">📅 01:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71915">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TCMzeM_0EJy_zWoG8wDJHdts3UrUe4D4CrYaIJsiAZTTZA1X7ZQcdzN_1qHYCs5B_kgSFbfuUdjKxUjl8IiaVT-GedanjkdcYx13fz2HYsTdMrHSZ-FNVfdgCRH2zX488PhqloFIIvAWh_3mp5ELnvE3789GGX7Fjg0ECKXARE0yBTlgZazPRgQURvoeKhgdjiavNovYXcSlDdF0IZ3yUyNCrS1YFaNsjyiGyIys5XzCLswRu-VISDGjqDv2GqB0EQU8ktmVB2bZPZ5x2qi2eKDJwN8yowmqycyBFJurwuNdEajpjBSzq7p-Jdur0AXDm6IC3wk3bcuwq3Q_3m84ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7ac25f2861.mp4?token=KuIbkqYHPkN2P3fx5qceiuXUfE2fsLRqfOm-E0cVqe4KMFS1_nsqMYVJDsgbKSl4CY38oLRXT5fCLiUZuMkWqZNBM9I9boS2O0tucGogNn-DGbTZwJvKQLW0UFu6zX-8pMQglkXfL6Wpr9jzhk5DEXSPOdraHsUIQFQF_LUYAELnq5KhsBCIWZ94N0hnfhrIWyvoy25h2drnopXx1bv2oiAvmTr3s63m9r-Qa35LuYjJlzDR0VDeZoRxl1KeXzX0854gPEqqHqfVwbXVhDPeHwsSSDtZQYu_6ldhWgL4S1lencrwYXAOly8Q7DFKZWMEBr3M9K2Bk9Frn5jDHzSkNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7ac25f2861.mp4?token=KuIbkqYHPkN2P3fx5qceiuXUfE2fsLRqfOm-E0cVqe4KMFS1_nsqMYVJDsgbKSl4CY38oLRXT5fCLiUZuMkWqZNBM9I9boS2O0tucGogNn-DGbTZwJvKQLW0UFu6zX-8pMQglkXfL6Wpr9jzhk5DEXSPOdraHsUIQFQF_LUYAELnq5KhsBCIWZ94N0hnfhrIWyvoy25h2drnopXx1bv2oiAvmTr3s63m9r-Qa35LuYjJlzDR0VDeZoRxl1KeXzX0854gPEqqHqfVwbXVhDPeHwsSSDtZQYu_6ldhWgL4S1lencrwYXAOly8Q7DFKZWMEBr3M9K2Bk9Frn5jDHzSkNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور شاهزاده رضا پهلوی در مراسم بزرگداشت کوروش بزرگ در تورنتو کانادا و استقبال فوق‌العاده مردم از ایشان.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71915" target="_blank">📅 01:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71914">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxTVNeDY-XtoT_vPDQeyb3h5FuVKz7bGFLA7sbrQ0TSQ-2HbmuFhTCqrHvDC0CaxX73e2UsRxd3G_x-iQEUSIGAOfENUMEuAQodoRW6Uf2_B2KxnKBOlYQGlcYHZctBl6RYqRPHP-ETbdz2Uvfo_iFTtUPIAUN4Jjf8suLH-H5WxjgOarEReNytjnP1UZcZJAtouL5CyZSunfpVs1Iw9FefwhBAHXsCItl9rDJ-ZlAJVgXj6tY6pG3AMgR056aSfkfqW26Wptft2G7urmLOz36m3kzVl7N6hkXnRjZBT5FR9S-APeePls84RbseaguG9nod8d3fytqaMlDV_ed-PjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:
ایران هفت شرط را برای آغاز هرگونه مذاکره به دولت آمریکا اعلام کرده است.
پیام تهران روشن و صریح است؛ اگر واشنگتن می‌خواهد از باتلاقی که خود برای خویش ایجاد کرده رهایی یابد و از گرفتارتر شدن در آن پرهیز کند، چاره‌ای جز پذیرش حقوق و شروط ایران ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71914" target="_blank">📅 00:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71913">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/654a3cad3e.mp4?token=SZCsNeJWulwb7W-28I7JUuB_Kpi_i1Ew_WQJtU1YwUZAsrApJ76bqbuRJN8wVKMVxjofa-8ol7UzlWQY3tu7ka77sXDfWlLPHwill-EZPDyLcdPp6hIQ1T6vrUaWRAgL7hHHmlUAZlXyci4fCvGO5hbOKdXSHA9c8FlTlf9X3Sgkvc_2sdf41NAIQOj-sH-aQIko4nJ6lFlmhBcv688ZWnhmTu-XDvmkFcgystlLKzBIMPh3kUzI9FDmLsKKMwazJ_9dSbRcr-G5QLgx7rLM_xbLc19f1nuEBDNwRn87aCMWEQ6jXeyKO-ab4pXFvPZ9YhcaWhzP5eUf2ZOGdxTIgHAaSllie_uS-4Ve_tB-SnHpE1CRUDu-dKsToJrRb9SM7YOvsie2Y87c5X9Zongy7o1w4m1k6ZN610y2fC0vA5ArQcNjnZEkGn4Bw45uIQIHjsHXILsqmHMtnuhZ_w_XcwsD0EvRXmRRf9Je7KHH92c0PK5ytYrM0S6L7LvoiQHyAQXtep6yQiIgUr_fA9ayTZEx6Ci3CT931GHiWjLSuPY-XuZwgmLHV-JIaKlFzYfpMhY1LJTjdlKxjvvQaxhSEidq_ghtw3bIrVx--pJDNVT04p_YKE8Un4V05NBtfygXQro643HTkePkmYn19cjBZaxk0vrBg6z1EzgFl5exPec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/654a3cad3e.mp4?token=SZCsNeJWulwb7W-28I7JUuB_Kpi_i1Ew_WQJtU1YwUZAsrApJ76bqbuRJN8wVKMVxjofa-8ol7UzlWQY3tu7ka77sXDfWlLPHwill-EZPDyLcdPp6hIQ1T6vrUaWRAgL7hHHmlUAZlXyci4fCvGO5hbOKdXSHA9c8FlTlf9X3Sgkvc_2sdf41NAIQOj-sH-aQIko4nJ6lFlmhBcv688ZWnhmTu-XDvmkFcgystlLKzBIMPh3kUzI9FDmLsKKMwazJ_9dSbRcr-G5QLgx7rLM_xbLc19f1nuEBDNwRn87aCMWEQ6jXeyKO-ab4pXFvPZ9YhcaWhzP5eUf2ZOGdxTIgHAaSllie_uS-4Ve_tB-SnHpE1CRUDu-dKsToJrRb9SM7YOvsie2Y87c5X9Zongy7o1w4m1k6ZN610y2fC0vA5ArQcNjnZEkGn4Bw45uIQIHjsHXILsqmHMtnuhZ_w_XcwsD0EvRXmRRf9Je7KHH92c0PK5ytYrM0S6L7LvoiQHyAQXtep6yQiIgUr_fA9ayTZEx6Ci3CT931GHiWjLSuPY-XuZwgmLHV-JIaKlFzYfpMhY1LJTjdlKxjvvQaxhSEidq_ghtw3bIrVx--pJDNVT04p_YKE8Un4V05NBtfygXQro643HTkePkmYn19cjBZaxk0vrBg6z1EzgFl5exPec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پورن‌استار ایرانی ملقب به «شیر ایرانی» با شروع بسم الله و کشیدن علامت صلیب توبه کرد :
خدایا منو ببخش و از این آتیش جهنم دورم کن بعد این همه گناهی که کردم
بدترین انسان نیستم ولی بهترین انسان هم نیستم به همه میگم خوبی بکنن کارای مثبت بکنن
دنیا خرابه جنگ زیاده سختی زیاده اصلا سختی دنیا زیاد شده و سختی عمر اعصاب آدما رو خراب کرده
خدایا نه فقط من بلکه همه آدمای دنیا رو از آتیش جهنم دور کن
الله اکبر خدایا منو ببخش خدایا دنیا رو جای خوبی بکن خدایا جنگ ها رو تموم بکن
خدایا منو نجات بده نزدیک خودت بکن میخام آدم خوبی بشم خواهرام و برادرام هم میخام بهت نزدیک بشن الحمدلله
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/71913" target="_blank">📅 23:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71912">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJivZ09NHxVI-EbKdyO-aWgtF08QyxZKd1Tda88nGItU3Wkwubd86igUU2XReOVUBRKO_PPYRh4c7ofP3AHUVdGARzfgCphxvlvTx_91fLhy1Yhiu1Z-2sEh4m3DXs9yHbxX6BiKJPdlRtj4VDRleAX4T4A8o5K2MJZ3qtWRgYYIB_QMmqxO5yUnM0MuNn9VHsS0Y5ATSwCpw0ghwFapnSivpEda5c7Yf7tXjC-dUaQE-qKcznupIo92nQ5pD_7lVSwov7PpuHdZ87vPk-pqKFwQSFafLxzxu6Aw7b5cWWBMjgKVzh-BGk6MoTW5bH5gMxfp1ayfZNJmTpQUsloNmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ بعد دیدن این عکس دستور حسینیه شدن کاخ سفید رو صادر کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71912" target="_blank">📅 23:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71911">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZ4dj_NAmgLmcc2Yv8JVLoWSgq3Ov0r9AnIBNndMfLvZc7Vs4acNTZqpdq060L6KOQFSTh_lipA-mYXUJSLg8e5MOECQnMAil0-CJWMSfGbKI827n5uZRu71ucLY2HD_ssu_qcwvnBrv6Q5AnhaLlSTTYw7Rq7WbIZwRWqpGXOk1bq8EIdiYtwrGaoN1rnt7t1FKWgQMpIs3YbAZ9Fq_ZP-jCZPImt9diggdAnXMrX_JBiCj5m4vlX-kf-zekI9EPLS4axXVHSK0JVfMjx4Ut7FejMrSAKnHxL0MHyZ4aD7_HOa-SNXWp5B6KTLYN7Ik4aVGEYkwvdWIsFC2Up_Ufw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه سی‌ان‌ان اعلام کرد که روز شنبه به دلیل ممنوعیت اعمال‌شده از سوی ترامپ، از ورود خبرنگارانش به محوطه کاخ سفید جلوگیری شده است؛ این شبکه اقدام مذکور را «تعرضی غیرقانونی» به حقوق خود ذیل متمم اول قانون اساسی توصیف کرد.
سی‌ان‌ان با تأکید بر اینکه «قاطعانه از تیم خود در کاخ سفید حمایت می‌کند»، اظهار داشت: «ما از انجام وظیفه خود در پاسخگو نگه داشتن دولت و سایر نهادهای عمومی، باز نخواهیم ایستاد.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71911" target="_blank">📅 22:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71910">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411c3a472b.mp4?token=LcdaTLPdZNggQ7O-Kh-tE_yxUsusziysxWOAtnYfm8ROYIgg2AWQ0zuQsgQJrCRuDeU8gNrOOImLw1ogShb5LHIGJ4z6ig2NZ_G0GeIaoSZmxwoz590GNoRT5jKwLBIxI8VsFlTbpaoUgiDDwz8tKMOGehMgM6tSoW7pJ73hC5bfpvLOIY6nA7Gzb3S2xcJ5OFngmpiirR_J2Y4fwr9aFOvEkn558TgFPqXQbaTjdEHyXNmgFccUa1p9VtGuv1GqQ_i-QwMSVmMs_sQyAJvmoT_JOdr7IL70lNkhlK_JmliI_wauWYmXTgHA9JiOaylyOxfSMWuvm1aFcDLsNdcXZD2wltU-su5968HArNE-qEbhpXXfuXvCKG6vpw5TB9plaawWH4BinT5_jqSpmd2HdM1LvVOli8D6FLLxtfbxGC1cWsL20to-AndCtn9umrtwa8NsA6B5wKVJj5ekF4F7HnRXuh_FnY3q0bBS9UU80txTAVvrMChgGMQp2qru6MZttk_DNBc3Q5tugE8wY8i35wjNMd63shg3HgKFTy9biIF8uP3Ovn4SVqKGErHSSkENyswMd6usOX3SRZCVaueNCEU07LN4kNqgbMLFpOQHaxeBYNF3p85qlDgp2bAhKRNjpe5y9HFl5keNd2fFulmlFOuRyGFK_bCK0ZhP9SHWjZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411c3a472b.mp4?token=LcdaTLPdZNggQ7O-Kh-tE_yxUsusziysxWOAtnYfm8ROYIgg2AWQ0zuQsgQJrCRuDeU8gNrOOImLw1ogShb5LHIGJ4z6ig2NZ_G0GeIaoSZmxwoz590GNoRT5jKwLBIxI8VsFlTbpaoUgiDDwz8tKMOGehMgM6tSoW7pJ73hC5bfpvLOIY6nA7Gzb3S2xcJ5OFngmpiirR_J2Y4fwr9aFOvEkn558TgFPqXQbaTjdEHyXNmgFccUa1p9VtGuv1GqQ_i-QwMSVmMs_sQyAJvmoT_JOdr7IL70lNkhlK_JmliI_wauWYmXTgHA9JiOaylyOxfSMWuvm1aFcDLsNdcXZD2wltU-su5968HArNE-qEbhpXXfuXvCKG6vpw5TB9plaawWH4BinT5_jqSpmd2HdM1LvVOli8D6FLLxtfbxGC1cWsL20to-AndCtn9umrtwa8NsA6B5wKVJj5ekF4F7HnRXuh_FnY3q0bBS9UU80txTAVvrMChgGMQp2qru6MZttk_DNBc3Q5tugE8wY8i35wjNMd63shg3HgKFTy9biIF8uP3Ovn4SVqKGErHSSkENyswMd6usOX3SRZCVaueNCEU07LN4kNqgbMLFpOQHaxeBYNF3p85qlDgp2bAhKRNjpe5y9HFl5keNd2fFulmlFOuRyGFK_bCK0ZhP9SHWjZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب حامیان حکومت تو تجمعات شبانه شهر بابلِ استان مازندران داشتن دورهم «کلاغ پر» بازی میکردن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/71910" target="_blank">📅 21:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71909">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTo7AR0eVGMz0-zThjoWwD8igVqtiKDmSrREVmK8JcZqTTI_wtZhJfB9vyzIyNB43NdU-o412cB7SVAjCE6qRsFoq5ANY9kaCg9aiX6G9XbmJ1NJP6Rd-jup48jwvCnct-96kfhSyqb6QHKRhXNrXltlNZjS-saTXfsYD2jRyptkvG31ZENVZ0ben6oJi0OJIHoFsFEDDA2pveBvR7TWi_Tz-7jbGgg_A8V12Rb7QomChXO3vuP6BOCq38RhV07Z_dtznhJ6doxfAAg0zL047F84MgEAwwSw_wxShYWJ14dQUYLyMXVIIEiMY1lbIg0kQmLiFuQrcSBsW0HPkt2TvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:نام فعلی هوش مصنوعی چرته و از رأی‌دهندگان می‌پرسه که آیا نام «هوش مصنوعی» باید به «هوش برتر»، «هوش فوق‌العاده» یا «هوش متعالی» تغییر کنه یا نه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71909" target="_blank">📅 21:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71908">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c50e52af4f.mp4?token=oACoK5TBS310ICijkoaqjNV3QHwgwQEkQHglgBFx7EO4sWF5lJ1qwYUkeF5V22-lVXy5PSqR0Nh3xaYSEYlbUVQyDfIAt3fMEesMppo2bzceVmiuUuCpEby9zCWf7IqpupOwNSNTn55uZ5NVCYGsLfd6G72A1BmWSFweBofBcwAwfA64rYzoW2wzRTZHIE6h_qtKN-S20dS8-k4xqOhG0OiRYhfnAgvLHMXO__lWdhNxzClHMXDFNiNseyJdPiVZcNb0V2RigxOC_UCgTl7wGDsuwFO3i5gj33RAwQAkZoNTSwaM8w8_9wwDK79pPdjTeA5dV3i6T3uPm1sZW6vpbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c50e52af4f.mp4?token=oACoK5TBS310ICijkoaqjNV3QHwgwQEkQHglgBFx7EO4sWF5lJ1qwYUkeF5V22-lVXy5PSqR0Nh3xaYSEYlbUVQyDfIAt3fMEesMppo2bzceVmiuUuCpEby9zCWf7IqpupOwNSNTn55uZ5NVCYGsLfd6G72A1BmWSFweBofBcwAwfA64rYzoW2wzRTZHIE6h_qtKN-S20dS8-k4xqOhG0OiRYhfnAgvLHMXO__lWdhNxzClHMXDFNiNseyJdPiVZcNb0V2RigxOC_UCgTl7wGDsuwFO3i5gj33RAwQAkZoNTSwaM8w8_9wwDK79pPdjTeA5dV3i6T3uPm1sZW6vpbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تست اکتان بنزین در عربستان …
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/71908" target="_blank">📅 20:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71907">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErWBmpdRwdIiIHj5L8IEIKVpGPLSoLHs5Q8dCB7bY1qwU4iUpwqF-_RKt3-3xBusYJkorZAeee8e3dv6Pfj8kcCtvy5AlQ0lXFSn2_ZDBLwP4JcXGSLmi8V1jLUpRvLim4RHpxulcQXLP7UIsElynCOVfXlFot2KDfHuXu9ywNni1TuDkE8l-ynmvjujDzKIypR6PsinzDP5Pe2kaxGVg-uOcesw6esVflhes1zboSPBulj-ykqhZUdGaGMC6v2B2mi5Ht5g5bmonuC45x1U7vRkcs_bWmEYxl8x2lcQme0-r1H1tcZBqtiahy6PvrRkiSW6apzoqymJUmnHE82olA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان هواشناسی: طبق پیش‌بینی‌های فصلی، بارش پاییز امسال در مجموع فراتر از نرمال خواهد بود؛ تمرکز بیشتر بارش‌ها نیز در غرب، جنوب‌غرب، دامنه‌های زاگرس و بخش‌هایی از البرز پیش‌بینی شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71907" target="_blank">📅 19:52 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
