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
<img src="https://cdn4.telesco.pe/file/tZ1CiN2Qtmi1p-7tx9iFkCrLSN0ZyybLcO1J49ho7ZJHIdzNTU-X7cZBlxC8xryoYRAQBxRm3I0QZTQ_f4zXJnZKE8KyFe--_12N13iVYz49FGHAMbBh9n63JfvePFo_MdSMWZFhWZS_5nc5p8pCnzPAhDz20zJyhv_RKapKNTDPc-z2Ahb7EkLHaO5DIhchLR6kDkZl9kq73MXUnGOewshSZER5N5_1rwIA4B9YBdijpDB19nbcoAOiIRaX73WORcUGYPX5WqqSU0PX-HCO3QfwiQQ0eYMvtL9_1zKz7kmkDjSSdoImkDHfS_vGfCfQcJTCEZXRfxFTTRJxIo2oBg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 354K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 22:25:15</div>
<hr>

<div class="tg-post" id="msg-24773">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdKkiOeWpcFAkScvjbROlAoALKZgSp-HZxGw9AlDZwUX8nGJQqCbmysz2atnVpjzMCZX3uhQrzDnV4pikDnGSz8iyrCCj9jSkDywaPTWUIw70x8M9QjctkRaXzfrBPvgFnmlbViqkpJnllUQjFpfOZlgarCVI5jLg0gyMMXFYHZ_FZPYQM9Ge6phrwEzQCmmAqalKXR8FWbmTJN6-0wtLbnZlrw6tPritJ5GaXsQCqB9x8B-Kn3Ywv0M5ia-ZxN5T64Np-S9zMmeOQ_8aV9fhQXuXSts-MwUfJCYtK-Gpnt99t0TqkUMv1hZxrZCcXI4wdRJzXwcB72VTysf_yi_Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇧🇷
این داداشمون کل بیخیال تماشای بازی برزیل مقابل ایسلند شده و کلاهدفش‌از اومدن به استادیوم یه چیز دیگه بوده که تو عکس مشخصه دیگه:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/persiana_Soccer/24773" target="_blank">📅 22:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24772">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LT3cBFGggEsSzzLq5qArCVIEBfpKRdc94q2tIyQ97vgeNHy5ePo7zvkGDWPuNoVQifV0enH6vnS1gDA_s6t-bZqaDbAZVKi7uFP6a95WA02L0ezgerl9tCnaaEPNUF7WF2IVE5Nj--IWIT9b-jbLqh8uy3tRwU0Fo_rl0K-hRufRoO4CSqAac3VdxjLcgHU4t23hzd1UEduIou9qevqml8UsBZpi_JyldMOPi99pow5ieOV7alGAoUr94cuFBSeWmITxhk8uO5aGhpbrFopohXDnUblaRoK3SP4t0GjCYXot57xAudItJpK9iCeaM41gtQrZ1iJl_oQNOW6NkEsHDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبراختصاصی دوهفته‌پیش پرشیانا؛ یاسر آسانی ستاره البانیایی استقلال ساعاتی قبل به تهران رسید و در تمرین امروز عصر ابی‌ها شرکت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/24772" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24771">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80508f67e6.mp4?token=pSXRmNbnbTEZj2Hnl_XSODfyV-KaKrr-3dbVXGM6W6AQdNbxid_2xsRlBqbjlSpTsKgKqgw1QfGwLxyEcJtmv--6CyRX40aA4VNAWyxvxi9QAh_4alRQueD0as0olxTF1aRTo4x6H_XQIrVde2f7MJ9CLv_oNv52USQBsEnD3WMECFB6E5EEYNQ_GK1yBXom1ZPSWINmp10EbKzb0spd_RrF_LKlq7zHnciW0ZYRj3Fg4dVYD8QPQ4zwv_3ex9PxF4dhu6IvoRVB7M3g1Sm4JUGceWvJO_Jrb2SldBqKfIclabHlfwsd8vdfgsTtIAaLBPu7UdqZntE2-SpaD0xr7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80508f67e6.mp4?token=pSXRmNbnbTEZj2Hnl_XSODfyV-KaKrr-3dbVXGM6W6AQdNbxid_2xsRlBqbjlSpTsKgKqgw1QfGwLxyEcJtmv--6CyRX40aA4VNAWyxvxi9QAh_4alRQueD0as0olxTF1aRTo4x6H_XQIrVde2f7MJ9CLv_oNv52USQBsEnD3WMECFB6E5EEYNQ_GK1yBXom1ZPSWINmp10EbKzb0spd_RrF_LKlq7zHnciW0ZYRj3Fg4dVYD8QPQ4zwv_3ex9PxF4dhu6IvoRVB7M3g1Sm4JUGceWvJO_Jrb2SldBqKfIclabHlfwsd8vdfgsTtIAaLBPu7UdqZntE2-SpaD0xr7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جدال‌جذاب جواد خیابانی
🆚
خداداد عزیزی در ویژه برنامه رقابت‌های جام جهانی 2026؛ سرپرست تراکتور میگه آقا جواد واقعا دیوانم کردی دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/24771" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24770">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/goV0QbORaP532yl3gM8JxB1lv0wpizHpYmjv4yrdHZ16xl33u6I_ov1bUyWcd03KFmwh1KryxD4pGQvEZpfCkzuu0pPchKgpTMP0mywKdLDGOc3uoNKq1g5yEcCXXC56ZK1GNUGDsgprvnlqx87Rld7AYPzQE27JdWG9QIuN5aLISUvju5DVEVyUWLTskXGucgWJagDOdPel6VvRizz6ctukbwO3weRTKpqCODEa_oG0-dlaA2SOd5h25I6W2md11jBKoOd-Fyty85wXPk84QJmccjFdy8ReJ1LgW5PBB1KLiBX1ux1Cn9wm_8kyanAi0oqXBzlCKRZkCua_Bu0SXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
😐
پشماممممممممممم
❌
❌
❌
مکزیکیا بعد از صعود کلا کارای عجیبی کردن که یه بخشیش قابل پخش تو چنل نیست تو رباتمون گذاشتیم:
دختره رو، بدنتش رو در میاره نشون میده به همه.
🔞
مشاهده کامل فیلم
دیدن فیلم
/start
https://t.me/nod_ppbot?start=d3c61e4fde78</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/24770" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24769">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/515246fe2d.mp4?token=pgRK16rMNrrlsjp7aO4xcdM0o7S2Hf4FgA8dmJsYWp6LmmO2DAL1LXKVWWFFK8DPCpr-scrYhyj0IESkZrklFe8KBsLxVkTISBoxd7-AE0mXagRmNFxSNsjNtTbmQzCTFzhTazm4eBLnaL7RfddMlxBQgvw-YIwDESiPNEFIgocJkEf_21eNkKCWXf6ZxlwvjLpFeARq7jH1bXHU_RR5irawKXKbEEoa11mMZ2McTQvOLkAoinxqhVaNXz9Q90-3387F49qMvBMnXuJWIp9IqOmcFr2srG0XQSl-DpSTKMT5x-4J6MJ-P5zR4-y1UPBIg1f4J8dRga63Ns8w-fMjjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/515246fe2d.mp4?token=pgRK16rMNrrlsjp7aO4xcdM0o7S2Hf4FgA8dmJsYWp6LmmO2DAL1LXKVWWFFK8DPCpr-scrYhyj0IESkZrklFe8KBsLxVkTISBoxd7-AE0mXagRmNFxSNsjNtTbmQzCTFzhTazm4eBLnaL7RfddMlxBQgvw-YIwDESiPNEFIgocJkEf_21eNkKCWXf6ZxlwvjLpFeARq7jH1bXHU_RR5irawKXKbEEoa11mMZ2McTQvOLkAoinxqhVaNXz9Q90-3387F49qMvBMnXuJWIp9IqOmcFr2srG0XQSl-DpSTKMT5x-4J6MJ-P5zR4-y1UPBIg1f4J8dRga63Ns8w-fMjjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هواداران تیم‌ملی‌آرژانتین میگن: آلمان داره تقاص این فینالو پس میده؛ جاییکه این دو صحنه به راحتی میتونستن سرنوشت قهرمان جهان در سال 2014 رو تعیین کنند اماسرنوشت جور دیگه ای پیش رفت ولی حالا آلمان بدترین روزهای تاریخش رو در جام جهانی تجربه میکنه. تیم ملی المان بعد از قهرمانی در سال 2014 در سه جام‌جهانی متوالی به ⅛ نرسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/24769" target="_blank">📅 21:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24768">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vL7mkKiJ63VSCJLA81Lv_cjpWEi-PrsW1S1sQ6PxESbBZa-rp16nVzMcKmGobFkhgfYBaWfMi6GAJ6Bcjwdj24PKb9aD8tqY-NuNEwdeezuqEAbdnD_5EPDV_ArLOCVBFZgJzS-AaHETNh6rzfl0Pddt3wo1orbGk2PQ_DsBwDISw0k_fRyxPiDhwt3lfJFHgWmysZQ94PK6mQU8VBGE7Ro5Hidi16AiDFiFrLTiARf2-542a6FB_9NIGIVGPqD8dARqq9HGqviUrBXGwuEf2l3E9Ldk50PXyVQUfpB5K70ZlTpUDV7CFP2DThfrlK6QjnCSS9UpI9cOk5QP8GkLEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نجات‌توماس‌توخل در10دقیقه توسط ستاره سه شیرها؛ هری‌کین باگلزنی در دقایق 75 و 88 مانع شکست فاجعه بار انگلیس مقابل تیم ملی کنگو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/24768" target="_blank">📅 21:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24767">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skCCnd6-z-6YFO6dT-QZdpN3anZ7YSXEFgrNzTFTdFKw7tFJHjQxJ8AYHg_AxbHwRGMWe4vWu7Cy8Lsz1Efa75JDxxEFJJGYRNezBiYlOHd5QHs5fQtEFiQC3gm3MiWBwYbvtiqb8Yc19c1NagJmrhgug56KEqWkxu1bkn44KKNEhe8wYEMdK6LmUlq5jNnqAKkg-gFM-X2PJCM75CwzlGXnKBjkM2inzAsNuoTaCWzjr5JCWYTfTIGhrEJNp0ql18He2i9MryilB3b6AxvZafR1lRMt20CgtcJZZMwyOqYaApleZmfA2a6jF8URM8cdPFK0mcnpV2mlS5fpB_bS1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دروازه‌بان31ساله کنگو درنیمه اول دیدار امشب باانگلیس سه‌سوپرسیودیدنی و نمره فوق العاده 8.3 دریافت کرد... باید ببینیم نیمه دوم هم میتونه مقابل فوق ستاره‌های انگلیس مقاومت کنه یا نه. بازی نیمه اول با برتری یک بر صفر کنگو به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/24767" target="_blank">📅 21:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24766">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfAiwpHM7XFKkvI8D8H4hLWZ0BFwoQpFXU9OYYYZRMNmoUBmpdwsJKlAQK_dmanusfvynpprHAYJOewskUT0KfHtdlVzaXbGUhZm_-e9_lN0att2TuVbmGtaRIElrk5_1tQJB2SGLbKYRb1Vfmvxogzd3UW2kZfX-GqC7ZWWXxdyQQH8g-WnIP5EjnznOZNhDO9UlHgMHH_7jXGg619enjVh7A4EKIZxEA1nsQODwmGvdoE34PsdmHtk1M1vw9tGxW7830mTdSy-DahwQD6W6rvzE85AjsGeRAEY6QEZjmiwgiYV7zLBmyXKjBpj3tdn1DFDhsnCCBogs91PKJnCGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم‌نهایی جام جهانی؛ شماتیک ترکیب انگلیس برای دیدار مقابل کنگو؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/24766" target="_blank">📅 20:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24765">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47867a7c2d.mp4?token=TgJTDt2S5T5pbmCnxWiyYkZVoJQNwDDeWpvLZFXyes-V7VS-_pONAZfu7sL769WGed-O9WKHd4R6QUuLaRzNLN8TVfa-x_ghYGzPoV8YNiJ2xDWlPI9xfmbFUZHCdB7A8QnfyyzcfJM3LqXHgP55qr4SFZhdc8ZnnSD77IzuGUDztMbSLrzRl1WeApBIr5AL7VRlPDwiHrGLTOnIJTDGTQkxJTx2s2asDL9Bqi98cbY-nNvTUKCoCZt4I-K7Ia-DRXz1wlRsZGTWwJy9zQV7GqaHHcvsKa-alocKljazmJngylLYAJ41hG7ccA2QUJMM0REaeoO6GLxUrH4HK-RZoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47867a7c2d.mp4?token=TgJTDt2S5T5pbmCnxWiyYkZVoJQNwDDeWpvLZFXyes-V7VS-_pONAZfu7sL769WGed-O9WKHd4R6QUuLaRzNLN8TVfa-x_ghYGzPoV8YNiJ2xDWlPI9xfmbFUZHCdB7A8QnfyyzcfJM3LqXHgP55qr4SFZhdc8ZnnSD77IzuGUDztMbSLrzRl1WeApBIr5AL7VRlPDwiHrGLTOnIJTDGTQkxJTx2s2asDL9Bqi98cbY-nNvTUKCoCZt4I-K7Ia-DRXz1wlRsZGTWwJy9zQV7GqaHHcvsKa-alocKljazmJngylLYAJ41hG7ccA2QUJMM0REaeoO6GLxUrH4HK-RZoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروز کریمی تو پخش زنده شبکه ورزش:
تمام بچه‌ها زحمت کشیدن. آقای قلعه‌نویی گفت خدا سر سازگاری با ما نداشت و ما ۱، ۵ و ۱۰ سانت رو تحمل کردیم. حالا اگه به قول شما لپی بوده، مال ما لپی‌تر میشه؛ ۱ سانت، ۵ سانت،۱۰ سانت رو تحمل کرد، ولی ۳۰سانت رو دیگه قلعه‌نویی می‌خواد کجاش بزاره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/24765" target="_blank">📅 20:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24764">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVrXXsBZu0Xll6bVqdMfgpgoqZnnv7WzxHygGx1V-zjNmjIBcr7H75qbWz6Y3SagKzyCABG1qxT96hGUyDWEqDsfEfuVLZbqPxhKKkB0CpX6mzHWKjKuuUUa09jCN7KmE4l4hQWruGBwNrubQeohoaXRrICpoS-JAIjPhQzOSTfUFOJIRWH-iakcPb12IEftHxbKlfEprNK5mnO-zTNl9sr-j1oIANCwF348tq5cW_Hm3CCQ4Pasp7n92jCGqJFRQUMfTmv8Em5Br6ODzADpUskPDatmCornXf_rZH8zsZ7fM17yr9_A5ofyaDtNHjZUDs0AIPQ7VVCUtT8X_U8yAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل‌ سایبری ستاره تیم‌ملی‌مراکش در اوج روزهای سختش دوست‌دخترش او رو رها کرد چون گفته بود که اسماعیل نمیتونه یه زندگی لاکچری در اختیارم‌بزاره. بعدیمدت میگذره و سایبری‌باقراردادی نجومی به بایرن مونیخ میپونده که دوست دخترش بهش پیام میده و میگه من روببخش…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/persiana_Soccer/24764" target="_blank">📅 20:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24763">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f2228f.mp4?token=MMRFQkSyNLlQ8yDgyxZ-z2vI___9HniIMRaPZYegUm433RRfk_8fB_-2rNSucdin82t0PiA5m-C12k00YySlXjdXH7SpxbU9nFchJ9objKmwooeFxZdPqnT5II9F5PqArBeV_EP1TSc7Qj5Jlx70BxS1_PohlIU8C9qn0RqqvRRwdJ7NXvn10OeCYrJc-Vk64XXSNiteb6pjXEXNWPcB5s2JQV78FS02VB9D8YGfzxBDY-r_lJvofEhlz7idQJ_XxyGCGqFsHMpW5a1wceZAMMeyzOCRze25Gez74mmxirGCQY4AZfw0zQJUSummwqfp3Zo5Q8SPZdESuMYpTM351g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f2228f.mp4?token=MMRFQkSyNLlQ8yDgyxZ-z2vI___9HniIMRaPZYegUm433RRfk_8fB_-2rNSucdin82t0PiA5m-C12k00YySlXjdXH7SpxbU9nFchJ9objKmwooeFxZdPqnT5II9F5PqArBeV_EP1TSc7Qj5Jlx70BxS1_PohlIU8C9qn0RqqvRRwdJ7NXvn10OeCYrJc-Vk64XXSNiteb6pjXEXNWPcB5s2JQV78FS02VB9D8YGfzxBDY-r_lJvofEhlz7idQJ_XxyGCGqFsHMpW5a1wceZAMMeyzOCRze25Gez74mmxirGCQY4AZfw0zQJUSummwqfp3Zo5Q8SPZdESuMYpTM351g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره آبی‌ها به کادرفنی تیم استقلال خبر داده بعد از بازگشت به تهران 72 ساعت استراحت خواهد کرد و سپس به تمرینات استقلال برای فصل جدید مسابقات اضافه‌میشود. این درحالیه به تموم‌ بازیکنان ملی پوش 14 روز استراحت…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/24763" target="_blank">📅 19:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24762">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCVE6HlAWxg1NzjucKpHQrHg5zHGdtpSg22err0LnLIxi0YaICPHPJOFadFO5BhIQdoVoZ2m2fipH-jbgS010ley82XeXQqdpajpq_zcTiBaH0mCRAF72qhMqOMF_k3e_S_zs7sAXlKwlDjSn-GXgp70UakuJ4goy8KlSkVF29El3dyndnXC4Iw5S53IiqBSZbrgfMi6l2u99VCmzgOn30ehE9bJfHi0rCYLDZJs_o0LZ1NvfRDRzs0o7AbjL0pavXcrK6GYq5UWhesHZLCaOJM3DCutFIJenNUxUWm4_NSzeFpBZat57OBkrKNQouwH4ALZzQYyhd9WV33pzFlb_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
پوستر باشگاه پرسپولیس برای اوسمار ویرا به‌مناسبت‌جدایی‌او از جمع سرخپوشان؛ همانطور که وعده داده بودیم پوستر دراگان اسکوچیچ هم آماده منتشره و بزودی توسط باشگاه منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/24762" target="_blank">📅 19:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24761">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8851fdf93.mp4?token=kL0qjiLGHGCUT4T0lH8XdqK3q-4wWZaYxg-PtSJeUi1Q_EGsP028AStl-BBwWtUM_VRBPnSBRdlGvqTI-1WpCcT3oq5Ypp5Sjz0CZ5JhTf7K8JWe19JcMC3Whxp9Wbvr6rPjFDLe_meTbhuGvYTUmizKpAUz2e6aYXuIyBIokHr8iciKb9KjcAlHRwu_37nZfnZGPiarWDUvC8f4Dmf98CsNcN2tU_iexP8q453dRIod0pltbWm9sdY3ObrdGlvEA9LZcTZY7DwO0W8c2sCFmNwURewQRQhK0LKWkwXYnq2hLYWVHhleq6OnAVvP1TTOqJyti5eki69U2LqT2DvIwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8851fdf93.mp4?token=kL0qjiLGHGCUT4T0lH8XdqK3q-4wWZaYxg-PtSJeUi1Q_EGsP028AStl-BBwWtUM_VRBPnSBRdlGvqTI-1WpCcT3oq5Ypp5Sjz0CZ5JhTf7K8JWe19JcMC3Whxp9Wbvr6rPjFDLe_meTbhuGvYTUmizKpAUz2e6aYXuIyBIokHr8iciKb9KjcAlHRwu_37nZfnZGPiarWDUvC8f4Dmf98CsNcN2tU_iexP8q453dRIod0pltbWm9sdY3ObrdGlvEA9LZcTZY7DwO0W8c2sCFmNwURewQRQhK0LKWkwXYnq2hLYWVHhleq6OnAVvP1TTOqJyti5eki69U2LqT2DvIwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لامین یامال ستاره تیم ملی اسپانیا:
«من اصلاً دلم نمیخواهد که‌همه ورزشگاه‌ها تشویقم کنند! هیچ نیازی ندارم که در همه استادیوم‌ها تشویق شوم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/24761" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24760">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ye7pbdCQVrLc1N1lqIiyUJ7FtyXPhSdjngbOwwKdDZj2Lqx2OkWzQZRXsSsIm1_YBp9yJxLenD8zvkHSmM5mV6wXhUkPqQnbgDppKdVr6KccSRx7jxCf9F1cNxm7GRIZ5Q_7f6FcPu7Z2owN1oLF39aOpBnQMj9KZLYGBrW4gShQneROTFjaEZCxNOmeTsc9VUjlyfq5BsdwsFZb7UTgOcJQtHX7iJRgtXFHiYO2elcpi9fRGJGPyhTBT2JY_NJ2X97A3KYsKA1AD5MaiUCMBCV6S4zJOt5-wu2ItzyDlOFkqjSoioIkUBRlN9t-JAvaIWL02e0g-3VlrajldVPhwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جدول رده بندی بهترین گلزنان تاریخ جام‌ های‌جهانی+جدول بهترین‌گلزنان جام جهانی  2026؛ کیلیان امباپه تنها یک‌گل برای رسیدن به رکورد مسی درجدول بهترین گلزن تاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/24760" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24759">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTKWkkTwTjGE2_jXoAZzvfkW9JBHMgyzx4mj4QECP9TE6AZE4lpz7SctNHmgzu50PguQFzOk7QtO-FO7bhiyfffH0Qc46ON6fWzlLPMZ8CVwA9gR5dveXliJ4Rj8RIUcJWdFDJXn9tBoAI4dCD4UfALe6ZO6k0j_meCUqScEQI9kHxHgmVod6PPmOQ2tcDv6LJVVMv75tkKrse4LwFgjDBCWKwVsvuOwxrQBKMf4fTWsXBiSFxOtcQo7c0D6-MFwsL-oero8cwXVRF-y_mi6AeYyXWLIOwYVOrtHjlZmLDHgotD35MVraTz2hD-Z_W5Ynxv8jT316TDHuggLZOhLAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
مسابقات جام جهانی 2026
🏆
🔥
⏰
شروع ساعت   20:30
🔥
20% شرط هدیه ویژه شارژ ارزهای دیجیتال
💳
امکان شارژ با درگاه پرداخت
🎲
آپشن های متنوع با ضرایب بالا
🎁
10 درصد فری بت به ازای هر بار شارژ
⭐️
برداشت زیر 15 دقیقه دلاری
🔥
همراه با درگاه‌
#ریالی
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://halvirox9371.bar
✅
کانال تلگرامی
#رومابت
10
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/24759" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24758">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPZ0ECAd-KglmWEFVZY1mDBiPdFXafp0Kb0bPrOVXvHIOOQ0OhvlEKQyPk5Ib78EiUKsSQfb_rEO98nUSCw3cnrP0o9qsi25V-JljK4dWwGc1d-GGvN2X__OqcqTIJL13uj6SstEUA2w84xQYdmcmvJb2A_Gv1Zt6hAEaXXjiq7xPL1mpUnAjIXBaB3qwc0hCwV31vRXJ96Idnar49Hu7na0Bh38FWhIfnpS3qyZ8eKUVFxdnuF5ruuW6JGW9pG6mzIm_ZPjpAP9kqnmO3XLMNVH5E9LkyQivuvQxKg8McpVofUp8M0ZZaDP83tb43u-I2bw3vA2TC757TmxaAKhfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/24758" target="_blank">📅 18:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24757">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5L20TwjVN4Kg-WsEnjGXvp7AK45ZTP1HRIX_SSLF6MAH45BbPjDsYSjsLVlNtnPgU3zAHnprYJtfjsGfBdfWFxZVaE-df0H9ClOfSUw2tCLkfHvamR5xBcOgYv9rXSSwSLaU3e1Zwmnxti0ewKTAd1LZxwrPqh8vj2UXuOyCoORa2HvfwMl7J6FHZrEqG3fJX2hzwTeKDawFGgr-PZ_-f6F229s-KbCrhug3yrvvNyuJDMiW5OjjkTniICeL7kSvEz3wUV6o7p_ZN0lqPmsAr6CAHs75beWRKKztKVRe6mYFHW0jEQhcafVK_i_PHWGAfz89RKOdrab4N_h7DA0aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم‌نهایی جام جهانی
؛ شماتیک ترکیب انگلیس برای دیدار مقابل کنگو؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/24757" target="_blank">📅 18:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24756">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkTiw9gGANDHHg-HQJq__aCJ-bKJTUrvWBXDLJ-1fNnzpiETHU7cF2AeQBYNUUiqj_IrJj9qUslvpS15A80D_PBOmCPHcawKlWeU_erbIgfTf1yGclrb1wD5enNwS_2SSjm1g7FZh7MO8PdWfHeyxcovQlT6FxdfgUOQOWc3fTPq6NYv-wOHRfeBaSg4fKahPwmzfNXDY5oDY6zhCyVKlf_DT_adcQTPDcpGZUojyQ3cllI9QwWhHITfV6Q42USpALXjAbDe77uKz1ReMsfMVQ85Q_7WwU1137W5GPFCZRhF9FKLB-H_LdUUqtwicr0c7C2vXJfT8SWWQsuD_BxYnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/24756" target="_blank">📅 18:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24755">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRq2fCDXZuftFze_hnX_ozeAyhB30sAiQlJX-RcIRziXO1ddeeFSKqvzqLk7jGIWg6G5qJ0a-oiWIzhTXYQh6n-w7JQdB65yQsSjD4kxsOt9BgOhkI4PVoJcuptmbuSJCkoBHdaZDywMzRmTfnDzHshtMPbRuDa4oy4jQ6oyNnr-jrK5ih2nSe-xat3iR_S3NOt3FpqhQXhA4OhbeYvIblMoBNrbLcQ0rlDiTb3u49Q24A6OVdo60-7QymQFSkh_l3rm-aF5YMcM9hbSqBryTq2L2Y9LLQ50f2GM6i-nPDXJXuCEYxKdlumU_ueFwPnbNnppCa1mUsWTdFOxRuZ0WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ طبق آخرین اخباردریافتی‌رسانه‌پرشیانا؛ اوسمار ویرا دقایقی قبل رسما قراردادش رو با باشگاه پرسپولیس فسخ کرد و از جمع سرخپوشان پایتخت جدا شد‌. بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/24755" target="_blank">📅 17:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24754">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dba2ae9cd.mp4?token=vUTPMXYYQ86Ia6mPJ_-miqTxv4eOD52xkKDLBgTu5wMybTeYAyzIHYgxr8xED_oIGXXGoEJ919QLPoql9fA_QMFP6q5xR8xJ1KVM3oIQoGwr4QfdwKzV_-kuygcIIjxfLWpsl2XFphV4UZlMBzS6jg1Sbl5KSuKo5MWJlVqWonrDQluvyXNxPpzcXvUEJr_Y9DHGV77ory8RvSKgusk3tu_NhYg_lFnKCTReSV3HpmG926QWYWWsWkPqEgVjujqgu-mnhwlBKQbT6nzUIZISy8S4Gk_-OOwAUEaNOYZj0Nu1ZK6a3La_EOyUDBF0cf21D_jtTFB1cUbiudxqqbttan1rPo2K9fx6bucvQlbyNHiJtkBK_sIUIUIk6kxF6uGnZjC8xua27Yp-T2oEaEq2e0zp2Q9oAvkfqP-ec7ScvmImMBXnY1fJEkIpKQMDjp6WG0u-jf3azy7fACTA31EavD4EhoM_QJ3PEmLg9sNISq_VXl6Tp6l65hPke23t0DBthkSCqX97fGYOyjeUWsV8Mfr_4zmNiGVKjZhPbHZgU_uZQxAYi2CJIFXNjiP86yFI3XXA6EQv1IbprWOAzh8p1QZXJE7qxBFq6Bn3d9OaWyssRMh6lQ_6p1WluBmu92J4O1Hh5as-CrBVoJrE80GOO875OwRm2c4fkjqGrYRow70" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dba2ae9cd.mp4?token=vUTPMXYYQ86Ia6mPJ_-miqTxv4eOD52xkKDLBgTu5wMybTeYAyzIHYgxr8xED_oIGXXGoEJ919QLPoql9fA_QMFP6q5xR8xJ1KVM3oIQoGwr4QfdwKzV_-kuygcIIjxfLWpsl2XFphV4UZlMBzS6jg1Sbl5KSuKo5MWJlVqWonrDQluvyXNxPpzcXvUEJr_Y9DHGV77ory8RvSKgusk3tu_NhYg_lFnKCTReSV3HpmG926QWYWWsWkPqEgVjujqgu-mnhwlBKQbT6nzUIZISy8S4Gk_-OOwAUEaNOYZj0Nu1ZK6a3La_EOyUDBF0cf21D_jtTFB1cUbiudxqqbttan1rPo2K9fx6bucvQlbyNHiJtkBK_sIUIUIk6kxF6uGnZjC8xua27Yp-T2oEaEq2e0zp2Q9oAvkfqP-ec7ScvmImMBXnY1fJEkIpKQMDjp6WG0u-jf3azy7fACTA31EavD4EhoM_QJ3PEmLg9sNISq_VXl6Tp6l65hPke23t0DBthkSCqX97fGYOyjeUWsV8Mfr_4zmNiGVKjZhPbHZgU_uZQxAYi2CJIFXNjiP86yFI3XXA6EQv1IbprWOAzh8p1QZXJE7qxBFq6Bn3d9OaWyssRMh6lQ_6p1WluBmu92J4O1Hh5as-CrBVoJrE80GOO875OwRm2c4fkjqGrYRow70" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برسی‌کامل‌ودقیق‌شدیدترین‌مصدومیتهای مرحله گروهی جام جهانی 2026؛ عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/24754" target="_blank">📅 16:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24753">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bce6bf7fb.mp4?token=KHEsPo2TEIpHe0zC_AtwSGCqE_Jms9BHb8o1yBbXdGlu3C46nLnp1j6hAq1WHgvVpGxIoJWoTJ3K5FOt6i5QqJ8nPGT97cNW9jJU_tJqEBqcP0lIG-42vbpDx1pt747bVINWukCgpzQ2c00mJ7ogLYfmTc0a5PtNn8cUS2-qoqGI45OKFhfnSHkLU17-S2CRllohfccXZgg0Wj9C_x_-d-H8fbrXEaJAtv7iqlS4ILeAK5FeKuieZ_rZP6cp6DZrgDRcP7LMEqVzLkMMMJAiLMlfod7PPDSpaNL95vCGaU8jPDjX5Ggrl8axz3U6SVb9ikkL7U-zwdnN44fMaZHE9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bce6bf7fb.mp4?token=KHEsPo2TEIpHe0zC_AtwSGCqE_Jms9BHb8o1yBbXdGlu3C46nLnp1j6hAq1WHgvVpGxIoJWoTJ3K5FOt6i5QqJ8nPGT97cNW9jJU_tJqEBqcP0lIG-42vbpDx1pt747bVINWukCgpzQ2c00mJ7ogLYfmTc0a5PtNn8cUS2-qoqGI45OKFhfnSHkLU17-S2CRllohfccXZgg0Wj9C_x_-d-H8fbrXEaJAtv7iqlS4ILeAK5FeKuieZ_rZP6cp6DZrgDRcP7LMEqVzLkMMMJAiLMlfod7PPDSpaNL95vCGaU8jPDjX5Ggrl8axz3U6SVb9ikkL7U-zwdnN44fMaZHE9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های‌فیروزکریمی‌درباره‌مراسم فدراسیون برای استقبال از شاگردان‌قلعه‌نویی: اس چه تقبالی؟ خودِ فدراسیون از این کارش خجالت نمیشکه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/24753" target="_blank">📅 16:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24752">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRnw_GU1CytL86oa5O7CG0tOlyL69GvoDfJehcNntEwngaPuomeDvaHP9Y14RhoamHHkOoGKvsvQH0BA0ooyY-0xP-Zf5ahHMD34oIOjVxH1kyyar5hVCbYw6rEFg3KOlvMWlvtsIrmP7mZFdp-o1jseskgjopA3o6_78Rm5rfjfrK_XYVJRGYM2WFUJtPJDmpYduic4qeBk-8bWyMHAw4_y33irZf1ybed6NdSkASsX3PryfwRNv_LbPZxn0MnkQEtEh1it3TMg9yPIDovlfnBsgdauRPji6j7011_s91APQfPXFAf5ZzcY1kxawlStE2A_q3y4zNRDybaMov_OTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال بسیار زیاد بخش رسانه ای باشگاه پرسپولیس فردا پوستر رونمایی از دراگان اسکوچیچ سرمربی‌جدید خود رو منتشر خواهد کرد‌.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/24752" target="_blank">📅 16:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24751">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdee128ed3.mp4?token=DicaOTwROlBfv_Mm0qCKAi1ImVwnT4gX_yO13MWqUDw0XrzoTZCTbxeUMAdGmQ9urj6xUFbydxc5GE6UqU0cJPUFuZSSfY8I4xycpaANH4mXWfxowV5BZOUtB_c-l0YYusXe_5xci1coOe1yn6vdGesoObdRgnpPcl5ifmRj2oN3SHoECkZcvvMgaHC3GOt9GPAWLY9Q1YwHZZTrk0WmLvlZRvLyPmELEMogedZHqZssmlP4gieC-hsqpFVg_pGLQWf88S1hLMi3F0JSlCo6zovIuw9vrXf62cCkIbUbPshZtcJ-1BZ-fs0rlCL3MH4zJCHEyJchDa1bC1b0rRGRPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdee128ed3.mp4?token=DicaOTwROlBfv_Mm0qCKAi1ImVwnT4gX_yO13MWqUDw0XrzoTZCTbxeUMAdGmQ9urj6xUFbydxc5GE6UqU0cJPUFuZSSfY8I4xycpaANH4mXWfxowV5BZOUtB_c-l0YYusXe_5xci1coOe1yn6vdGesoObdRgnpPcl5ifmRj2oN3SHoECkZcvvMgaHC3GOt9GPAWLY9Q1YwHZZTrk0WmLvlZRvLyPmELEMogedZHqZssmlP4gieC-hsqpFVg_pGLQWf88S1hLMi3F0JSlCo6zovIuw9vrXf62cCkIbUbPshZtcJ-1BZ-fs0rlCL3MH4zJCHEyJchDa1bC1b0rRGRPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#نقل‌انتقالات
|شهاب زاهدی مهاجم سابق آویسپا فوکوکا به تیم‌جوهوردارلتعظیم قهرمان فصل گذشته مالزی پیوست تافصل آینده در لیگ نخبگان بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/24751" target="_blank">📅 15:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24750">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‼️
دیگه وقتی سرمربیت اینجوری بهت تعظیم میکنه فقط یه بازیکن ساده نیستی؛ کیلیان دیکتاتور
😂
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24750" target="_blank">📅 15:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24749">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=cl78DbGVKdChXjVzJxyTBFzU8vuthMM45JDPZ1VxYst6j33lwnJfd2m3FZxLOzPStywNmZUUgH9s1v7wt1guqBq0owugpD2iYHaTrHpMlL4HPBRCCioJzvfQEwWJo6ZAt6LkYGbJwqAWVj65hzH0GUQ5OUeHoA0UEf_1-WDLAwYaOYnHjGYa43SdaVTPnwx1_1kV5_WobGE-9CcpGRsf2mzpvRdj1TWwpK1S6W0IYHXDQnisUhqIHYjLw5r_bWTl86vzBOvsi1lEaQpftknt747lHU3_6uYuQuAzIuBkGbnhzLvZ--FXwlZ-DVrP9eUefbTt6PcV0_C9MTI2y_YxBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=cl78DbGVKdChXjVzJxyTBFzU8vuthMM45JDPZ1VxYst6j33lwnJfd2m3FZxLOzPStywNmZUUgH9s1v7wt1guqBq0owugpD2iYHaTrHpMlL4HPBRCCioJzvfQEwWJo6ZAt6LkYGbJwqAWVj65hzH0GUQ5OUeHoA0UEf_1-WDLAwYaOYnHjGYa43SdaVTPnwx1_1kV5_WobGE-9CcpGRsf2mzpvRdj1TWwpK1S6W0IYHXDQnisUhqIHYjLw5r_bWTl86vzBOvsi1lEaQpftknt747lHU3_6uYuQuAzIuBkGbnhzLvZ--FXwlZ-DVrP9eUefbTt6PcV0_C9MTI2y_YxBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یه‌فلش‌بک بزنیم به این صحبت‌های مهدی طارمی بعد از دیدار ایران - ازبکستان در کاپ کافا: اگه تو جام جهانی پنالتی برای‌مابگیرند من نباشم کی میتونه توپ رو گل کنه. جز من هیشکی نمیتونه پنالتی بزنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24749" target="_blank">📅 14:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24748">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhtbR9qeh9prcM24m5ScxjAF1n0l4_ZVTIbjGZ-84A9hwA6D8b9YD98npou6_wsgJachA0_4ePHNL9TeE7F1UQpen3QOfWGnTMvlQr0D53dDbPBboRbK0a5ukgc0tXCj6aHWnpicQ6aOYS9zc79YZKJQ5JY8I3Y9UphLs8DkP_Bt6zDcl60Vr1ZnoIQb98BcR8DywdU9woqdrMRqyd60MG0OGYqX28LZogwM4Zy65Bf8i-ivJDSQPshAT9aPenb_siYTfDmIqWKXHwpoPmrzsLtu78rJ6Qf68srxce6EwnvXcMvzRYwiZGUFG6c7QwW0NxCqB3UWH4kC_nZx6vnpGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرمربی اکوادور که خیلی عکسش از لب گرفتن از همسرش بعد برد جلوی آلمان وایرال شده بود، بعد باخت جلو مکزیک استعفا داد. اونوقت فدراسیون ما برای‌حذف‌از آسون‌ترین گروه مراسم استقبال میزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24748" target="_blank">📅 14:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24747">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrsXn43jIztpHSZgNdu2NvMZ2F27R86l2uIOIJanMRpBU-Cj74m2myE_yV4qV1eaU8G3fS7jDx0EZJYKFfxCQJms60UIdd-hwCPVxfCv9jH0OVsnx3_rIbAh9JK1ucgOjfwxogQFVi59fDJTB8Rii-D14Xsts_MlP9TqmIm5zt4r5Oql4gND0EwoGp8WHrlxk9QyRMeRqNMguJGFC3rVA1Ja6YYQnlZ3LqOoivhY9xtFk26ZfRrUtphLK2OP_blKzr20OyDvPy7e5CCkyMywh0CSJtLvmT2dGZWaGaCO86_QlmLAK3QkHyXabOUaaG6LBpA03WTDxu9g0MrlxuhqWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان…</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24747" target="_blank">📅 14:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24746">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0YplsTaHE8JAb01TahYihD-8mPI3AfzfZD7pSBiuHitSVi5DjZU-1Zoy0ckPiCuFMdiKAMZhLLhiaFnaSP8Etww4Frg6pDDY-Co1s0sXz3GB7_XUCRzRlhGJ-16b1G6-3sTsGQNTcqLHLHzxdNFaiJP9EWQlGS23ErcyA0mTeWbXWltxWHmw6p4LfKbzzuVZWDuDkbMrHpcVqjZ-D72jHdi8BY3UQjiec0d42ezYxMUpZpNIxX6y0V9G6FizLhYl3k_FlNH527_9v9o29HMjTBnvkZOhv6foRc6Mw-nbh6hM4_elx676Z0SnG2WgVRE_eVz2ZPuCGj6-h_KNKNnog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان با باشگاه دورتموند بست.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24746" target="_blank">📅 13:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24745">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhi3D5es-O2gEJzkTwNWOAltu5nNPkvvyLg9qcEDd5l-WPAn_sDp0btOeIgEWLwxNq39a8HHUZp8-4whTcu_8K7lePdocE7Of1YpAmoas0N8xDjZuhQNjksbQhBHXlOryyPYi9pcK8mi_Wk8OID--jTTTt2BZkcxRUcg55cUvrwnb0aRPbFRLB6hHyvdrCpAfxuS4HzbVEwOZ8tWsbFJ3yninj4NoGKs1bcYp3P1kHkSNtR0b8xK5oN5TuT-pPpK509D7rIO1S-aafyYudWjys3vr8nssi52V6nN6si55hjAH7oqnoV2_GTndHHO5ARPUydaMoxvy5qXJOV5RI-XNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا بیرانوند دروازه‌بان تیم تراکتور از شهریور ماه سربازه و احتمالا راهی سربازی خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24745" target="_blank">📅 13:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24744">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16504ba5c1.mp4?token=kU2a9vrGnSkP79ZUaqAYF2ctRnhChYHmiFfToehG7j4mOQUlwz1wdQgUfqfiXtPySlw-5S0EHBN-mMUHD1OKNg5J1J2tsLRBjUhRef4ASeUZFTKfsd-uGAi4vOhOdH0txc-U0Fzo5TcrNhYfgQe3MbA6LH2-rZqpfgYx8obRqeWkwRMlhnF6TPooZ5HusEIndZHI2twibrxwfkDTqhNbW5bV251W0MpKHN3fqyGw5VJAL64MyUZhSQqm-Aej-ZGrkvQJ1rWh0Ztg0b_LhLfSyfjvD_BJ83uhkKNX8pp2OQazp6i18EphEZLK-96qnaGZQVH_RsSd62FCsGXo3nZjDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16504ba5c1.mp4?token=kU2a9vrGnSkP79ZUaqAYF2ctRnhChYHmiFfToehG7j4mOQUlwz1wdQgUfqfiXtPySlw-5S0EHBN-mMUHD1OKNg5J1J2tsLRBjUhRef4ASeUZFTKfsd-uGAi4vOhOdH0txc-U0Fzo5TcrNhYfgQe3MbA6LH2-rZqpfgYx8obRqeWkwRMlhnF6TPooZ5HusEIndZHI2twibrxwfkDTqhNbW5bV251W0MpKHN3fqyGw5VJAL64MyUZhSQqm-Aej-ZGrkvQJ1rWh0Ztg0b_LhLfSyfjvD_BJ83uhkKNX8pp2OQazp6i18EphEZLK-96qnaGZQVH_RsSd62FCsGXo3nZjDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاویر ارناندس ملقب‌به‌چیچاریتو که در تیمایی چون منچستریونایتد، رئال مادرید، بایرن لورکوزن و وستهام بود، از افتخارات میشه به دو قهرمانی لیگ جزیره، یک قهرمانی سوپر جام انگلیس، قهرمانی در جام باشگاه های جهان و قهرمانی در جام کونکاکاف اشاره کرد، وی به دلیل طلاق از همسرش به شدت از اوج خود دور ماند و دچار افسردگی بسیار شدید شد و در نهایت سن 36 سالگی از فوتبال خدافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24744" target="_blank">📅 13:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24743">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKNsUSCOa-EeUKMPSqTX3zpKHkRTLTSteiigjxAcOzraRFTnwmkW3BU-mKics8c9Sw73dOTPE35Ke7KOBW-UOMxwZFmOu1jtNKp-0IxjzT2l4orqMEZSoeABs9SaN8iYEPDIxLJY7XbMEuXr4jfq5Z_-kMeGle4hzd7y7RCsNF2EjWDqqkcespcIVG_tBOG-R1WPg-E7IRkvrtprixtGq4FR8m90es8bQSBNSDn5kfFbO9XF6v6EPVKa_FVADJWuWmnfDRzPaJGs3gvoEY4NkS7TILHKiyIANCF4BN4wvlnEYznX162UGieC1ob6KmuFTOMUS4rWX13dsDKK4jF6pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛باشگاه تراکتور به‌ سید حسین حسینی اعلام کرده مدیر برنامه هایش روتغییر بدهد با او قراردادی 3 ساله امضا خواهد کرد. پرشورها قصد دارند در صورتیکه علیرضا بیرانوند در این تیم نماند با گلر سابق استقلال قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24743" target="_blank">📅 13:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24742">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYILsgJH-MdXIhhSMgOSVyFPpwye9fgiK_ZkAD7Zj6MiLVnqoqdWk-kY9J13EG13euC3y4gTTsG4vbjQQxfjtw0uJBHxU6ntlHNi6yNfJowPG-Em34HDY0wzjMCq4E1rk1lYV1DYpQvXk3Fe6arwSaxkmDvCiwketBNMWXFwhTaG0LYl340iTf-UIsxqF7GkB5eE89u5uWCnq8E1HLz9McsNnJG5k4CkCUWBwbPk1KiCwA7njh5OLDT0EY6X1eV4wqGMwx4pfZEUUxgxU5gMfeTqpkPu6io5Og4ZUTEuC7TJANrzOYyXr9_U7al7VjPYs15ZESjGng3urp6ULq4eWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل‌ سایبری ستاره مراکش در جام جهانی ۲۰۲۶ و بازیکن‌باشگاه‌پی‌اس‌وی آیندهوون که اکنون در آستانه انتقالی بزرگ به بایرن مونیخ قرار دارد، مسیر همواری را برای رسیدن به این جایگاه پشت سر نگذاشته است؛ او در ۱۴ سالگی به دلیل اضافه وزن و عدم آمادگی فیزیکی با…</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24742" target="_blank">📅 12:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24741">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290b5bc8ca.mp4?token=JyWLcGW2f_OOTJLHa3aDhsDPKMbj2ufWyKX2oowzFwy6RaUbxQdQYHGEYranZAeYuk749O-uGq_9jiy_sGAHSWSHDFB7OLEpEibON_-8mMEqwzd0WQzJnEz7xM3IxBj44HTBAJN8Vf-jNFpqDYX3UFCptShXVWgEtmC3XBquhY7dOEIxwyVLL8vjrmyRkdqFUoXoKtYZLn9M94CbNC6DLE2_CVz-1URLSvOyicZKFD1n5tAdstRciu1Q161Z-IJyX7H0z010dQI5NHYfiq8DoqG_0FJCSkqHgUUu1cmWitC7ePsSv7nPzNv9J_7Fq4BzCre0E9kQb5uVIaeEvvJOZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290b5bc8ca.mp4?token=JyWLcGW2f_OOTJLHa3aDhsDPKMbj2ufWyKX2oowzFwy6RaUbxQdQYHGEYranZAeYuk749O-uGq_9jiy_sGAHSWSHDFB7OLEpEibON_-8mMEqwzd0WQzJnEz7xM3IxBj44HTBAJN8Vf-jNFpqDYX3UFCptShXVWgEtmC3XBquhY7dOEIxwyVLL8vjrmyRkdqFUoXoKtYZLn9M94CbNC6DLE2_CVz-1URLSvOyicZKFD1n5tAdstRciu1Q161Z-IJyX7H0z010dQI5NHYfiq8DoqG_0FJCSkqHgUUu1cmWitC7ePsSv7nPzNv9J_7Fq4BzCre0E9kQb5uVIaeEvvJOZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ته این داستان شد عزت یا آزمایش ژنرال؟
امیر قلعه نویی سرمربی تیم ملی در جمع مردم تیخوانا در زمان خداحافظی: خیلی دستاورد بدست آوردیم، این عزتی بود که خدا بهمون داد؛ وی پس از بازی با مصر گفته بود گویا خدا دارد من را آزمایش میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24741" target="_blank">📅 12:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24740">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoCoLQ1yihLj3I2KwAhoh3bf8lemCILfKzSwwRs5AlPje2QpbJKOKoa755oA74yGThLsJhAJWfgp7_G1pbOBrcJ6Du_WAJF-6Nv3hk6DRj8uJD0CdEpNOp4YlT9_lhO-DmKEbYndcNVkRmNmdFfrHpnm2ooeso_ZVXtuRXZH4CaM7ARadbNa22l3uURiMoPXkBjFZ8lQQ_x3l6NzTKXDp4dw6Tw7QjO5QwVv8NHJth0vve8LskrGF1VnLS124pVy-sagqbBCm1-0-OuPvne7MwezJU4RZMCNOAZCHxPFqgbZcy3SBubmn-ERkFdFuDy2zCh-0wfdszGjYug3t55mKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فابریزیو رومانو: ماتئدس فرناندز که علاقه زیادی به پیوستن‌به‌منچستریونایتد داشت در نهایت با عقد قراردادی‌چهارساله به تاتنهام پیوست‌‌ فرناندز بخاطریونایتد پیشنهاد رئال مادرید رو رد کرد اما به یک باره با رقم فوق نجومی سر از تاتنهام دراورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24740" target="_blank">📅 12:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24739">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRiLQ6ikgqKiTK3mwM68_euOi3CQCkXcaf88c2gOs8XvKS1ocikt8-TlywuqCkZ78YVJXM99_n6DzC4-YZ2ZfUm4RwwDG34_ptXTADExTFDUalrE5FOUqYVe5lKYhyOLq698bvoFbqJLY9VdTL8tJniU4Crjk3RjbVyvz-J6aUyGS0X7bV7f70k7j9brraTn9y9j7-BjJatDdHvHiR40xGAj8nU6RFhmdGHoJXhvmSGxrrnFXP7qVVVvdxyjzRsmhX5C_1bkxMdN2XqFQwNisJrFbYvZIwrg3puq-Xw1ntVnW2kn74-9o1d0Led9NreSBB0UgOFBy6qIszDOVTRoBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم
؛ سال 2016 دقیقا در چنین روزی؛
باشگاه منچستر یونایتد با عقد قراردادی آزاد زلاتان ابراهیموویچ رو به‌خدمت‌ گرفت. زلاتان در مصاحبه بعد از عقدقرارداد گفت به‌جرات میتونم بگم که من بهترین‌خرید باشگاه منچستریونایتد خواهم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24739" target="_blank">📅 12:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24738">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1Vq4_RT6u2rKuvq51cReUsqL9kg9gQrpyktzxQ0OOMlXoca43zBGXh8uVeWLKiKmFxJsXgWFJck4Ga0HU2YsWt7aKrQvALfIYOA6zpACvypZFHza_aDfM4PEnOOCL7zIYXKqPXflijCAXkB0eojnqpLjvmgufVLF93gwTkVjeosgW0n2-GtrdgSQTkzQK1ICHUuDbZRs-iAc5cJ2vCA7oBOWjJc4LkEzAlXaAI4pZbzcq8foFodZj_IrFx48rPnIqqrX6-FFPddqsLXR6KcdS68oqZB4pPHg3334rIw3iPxfITNEuRaGtCEEwcCxk-5fGg9tDJpRHINr3CdNoM9Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت:
کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24738" target="_blank">📅 11:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24737">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogDFmLLuhlEUGN-v0slLXkXv7NmWnOCICevzibDAKckAxnA_Z-d9_fX-rOLmXqkeUNUwCUO5novntWYsx7aYBPcPhoYldm66Ke-wrip3SV55ltaKcUHhCzfWwchcoIQ9w3t7THlXxODzVORVlFuk1_9QzzMDWcAM_jdU92LayueXpfyI8PM9wwRxLqrfqGdmP76N5DBHj0h26m406EiMEWQMO1W8NhFBkzWrFUSW_vzxkfPriTHt3-XLQ2AYXR9H5-Jnb-Di3ZZa1fxZFGq_05AtQov0rcRXkE3pyqqkp3tTpVD60TD6LiUMxAFLtJQqRRte5LuXI6Bbt5um02ep8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جدول رده بندی بهترین گلزنان تاریخ جام‌ های‌جهانی+جدول بهترین‌گلزنان جام جهانی  2026؛ کیلیان امباپه تنها یک‌گل برای رسیدن به رکورد مسی درجدول بهترین گلزن تاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24737" target="_blank">📅 11:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24736">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc031d7910.mp4?token=kUlSAilANt9UlUYIh3hyqyULdtJaEYCkmOT5BKCuuz4HALfcMRtTZPpAvXyDqkf68qmzynp08olicTluowworKvEUOnwu2q4voLoegmlo83Ib1yqKrMKd5qIBF7jzoMU1MJ9ZQVWJkb1uK5qxuVYt2ZSsL6swWUmItpK0inZdqE5-aGubE-_XhZvQmWhspDjqkqCSmcXTbsIniRMHQL5U6ym8aUD4p2_MdDzCKOQZwEcsBy97yym2JMnY2p9TsQY9VjUtO4tHjnBMHTganhjGFPExptSzj_1PfdFOtO9LhtVArPqK1I53Z4oO-Kfsd2SVg_hx-1X2xZSLFgH42rf2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc031d7910.mp4?token=kUlSAilANt9UlUYIh3hyqyULdtJaEYCkmOT5BKCuuz4HALfcMRtTZPpAvXyDqkf68qmzynp08olicTluowworKvEUOnwu2q4voLoegmlo83Ib1yqKrMKd5qIBF7jzoMU1MJ9ZQVWJkb1uK5qxuVYt2ZSsL6swWUmItpK0inZdqE5-aGubE-_XhZvQmWhspDjqkqCSmcXTbsIniRMHQL5U6ym8aUD4p2_MdDzCKOQZwEcsBy97yym2JMnY2p9TsQY9VjUtO4tHjnBMHTganhjGFPExptSzj_1PfdFOtO9LhtVArPqK1I53Z4oO-Kfsd2SVg_hx-1X2xZSLFgH42rf2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه‌جدید آقای‌امیرقلعه‌نویی، سلطان اعتماد به سقف بعد از حذف از جام‌جهانی با یه ادیت عالی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24736" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24735">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbe8695009.mp4?token=BdvwpwgqPL8-R4oblje7fkQFfUpEdgfIvlpmy3fSmuljmC49llZBNKprZkYlIq-1j3yQzxHQJ5AFvDunnKvKfFjqsawraE-NLJj6Lo3dkHEdMFg8l58N3A10O_o0adrnfdL3nyPiZbehvuC02a9nvyDF3Z_z4TCRKx-8AM04a_PPuG7BUgejmGPNsawrV6JdOxsoBPiWS9Z_DT8GHP1m6SxEV-g04s8vcPTrm4OOiQzMqWXHSdNSacGt8p9U7ecxJqUjLOxx3kDUpTa4Ng6sKdvjuDy_TFM0lOcrT3_vS95LHUWEGi-mAu3ITF53dTPp0XOcRqPHDnDVgaInq1JVHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbe8695009.mp4?token=BdvwpwgqPL8-R4oblje7fkQFfUpEdgfIvlpmy3fSmuljmC49llZBNKprZkYlIq-1j3yQzxHQJ5AFvDunnKvKfFjqsawraE-NLJj6Lo3dkHEdMFg8l58N3A10O_o0adrnfdL3nyPiZbehvuC02a9nvyDF3Z_z4TCRKx-8AM04a_PPuG7BUgejmGPNsawrV6JdOxsoBPiWS9Z_DT8GHP1m6SxEV-g04s8vcPTrm4OOiQzMqWXHSdNSacGt8p9U7ecxJqUjLOxx3kDUpTa4Ng6sKdvjuDy_TFM0lOcrT3_vS95LHUWEGi-mAu3ITF53dTPp0XOcRqPHDnDVgaInq1JVHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
منصف مثل سید مهدی رحمتی
؛ ارزیابی حضور هشت ساله کارلوس کی‌روش روی نیمکت تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24735" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24734">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lxrp0D9sZdk0mO_3hvt99ihu7lAxSVoQXkdhK4ge3IM4eLj5s0fNFOXiwHmli7lJnB-ykxEERy2I544-PIATdeYCsxHibmCQYG2lrYIinUFfzKsZpSdcODltjjO5kgmFlhO9GjnHMNKo_uwDOqs68crJyjLGzNB3xXm2Ha6Sf8z1eh2UYOT4NDCG-N-nPLov8ca7QGVGrosuTZq20egMwPsoTt5i0Wx6Q4BJCIRaj-910uCVDUV5U6sQp-y42lIWnTT-PKJE7iX4CJYwSZuph7t2iQTWEA-LEe8fCBMJhA5ZoaSS0eXcV_b3JrHNhocY3yICmbVUXCAW0lxUDCuPIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
توصیه میکنم بازی های جام جهانی رو فقط توی سایت بت اینجا پیشبینی کنید
🅰️
📌
اینقدرنتایج‌امسال‌عجیب و غیر قابل پیش بینی بوده که ما تصمیم گرفتیم به شما کمک کنیم:
🤩
🤩
🅰️
بابت هر شارژ موجوی اضافی بگیر
🤩
🤩
🅰️
کش بک بابت هر باخت
✅
این بونوس ها بدون
#قیدو
شرط و نامحدود هست
.
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r10
@betinjabet</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24734" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24733">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQM2z_9uocs_zHt0d_6YivDo2Dn_HoypWMzpSDKeGU30TpzM6M508jC160ZmNbzSr_rvNU8736CHGplE6zaiIvJsGsFmZfag1ahNXTKgFNyopV28nFPXwKu2CfwWI2gbhSKNrMH1QaXtKDHlxwlS6XLyOU1KFOlVBElp8u0EEjcAA5E4454nX40GFNEwJf1jlteNk7sOTzo7mlDbfv-9ntyBPojjyYBqwvbB5RlBg3VXX7XQohCeMJ2PrAbrDTVEB0uMh95uywJAeBTFrZBjxObhbuP5FaNFL1K_vh--RXIwCsZl9OxjM34kQJQTVzIFmyWMpi810GWPn7I_XB_B4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24733" target="_blank">📅 10:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24732">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/118e0a09b6.mp4?token=VyEGl4gpy_h7sIFTdQP-cdZ-_fShJq7kiFn9AizkJl_3ktvuVXb8-WXzEtT4jNHVYWRwxGsP2Y9T8c7yiL85-hEReOOngKJ3U-rOt_NkZLEQSKz-OTXf5Js_DcjJop-vCocKOWv4EbCdxvgI0Lz7HWOOIDOv-RAlHOQHoqjk-vjsDOKDaVxnnrOCO9Vm_skdRPxap5y8RP9wBwGTbbfPOAJFhm3PvDok_wCGOeueP4QTIdnZ9fOEzDsEd7dnEc2I8Ydssii5pzfBlOLAog78nkNi_gvbJN-jN1MbT5eCD4XtgJPWAjxE257N4qEGImKKsGZkk4-uLq-aDi2SHo6kKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/118e0a09b6.mp4?token=VyEGl4gpy_h7sIFTdQP-cdZ-_fShJq7kiFn9AizkJl_3ktvuVXb8-WXzEtT4jNHVYWRwxGsP2Y9T8c7yiL85-hEReOOngKJ3U-rOt_NkZLEQSKz-OTXf5Js_DcjJop-vCocKOWv4EbCdxvgI0Lz7HWOOIDOv-RAlHOQHoqjk-vjsDOKDaVxnnrOCO9Vm_skdRPxap5y8RP9wBwGTbbfPOAJFhm3PvDok_wCGOeueP4QTIdnZ9fOEzDsEd7dnEc2I8Ydssii5pzfBlOLAog78nkNi_gvbJN-jN1MbT5eCD4XtgJPWAjxE257N4qEGImKKsGZkk4-uLq-aDi2SHo6kKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24732" target="_blank">📅 10:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24731">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=FNF6uPQFwxtG8fT2pwtMnWHLKd1lDJ63FGvliaqI83Ix1AL3Oonwshe0RZnhDWpD2MZJZLK5xucbTqGSksuPZLhDgOqzOsfdW9RPz5jgilkMAdHjWT-ipr_Mk9KTSIABppqofkZ4esNX24MaRsv0NNClqN7j258GSJ9IT6agOpVCoXLPEEPkuyyu2x8CEtme2cSS-u56S6f_wydg4mDRBHzz9ZrhHz1jZP4BXjbRNIw7ed-SGAQupoF1RV0LZk30jm8phk6gePvZ3jxqRYDjE6p4r8va4LED3H-a907LQxWeGQbC8WWTjJj-PodrZKPwp3aZ597c_BA-pfGMpyjvyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=FNF6uPQFwxtG8fT2pwtMnWHLKd1lDJ63FGvliaqI83Ix1AL3Oonwshe0RZnhDWpD2MZJZLK5xucbTqGSksuPZLhDgOqzOsfdW9RPz5jgilkMAdHjWT-ipr_Mk9KTSIABppqofkZ4esNX24MaRsv0NNClqN7j258GSJ9IT6agOpVCoXLPEEPkuyyu2x8CEtme2cSS-u56S6f_wydg4mDRBHzz9ZrhHz1jZP4BXjbRNIw7ed-SGAQupoF1RV0LZk30jm8phk6gePvZ3jxqRYDjE6p4r8va4LED3H-a907LQxWeGQbC8WWTjJj-PodrZKPwp3aZ597c_BA-pfGMpyjvyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فوری
؛بااعلام‌دولت؛
سه‌شنبه ۱۶ تیر ماه استان تهران تعطیله. همون چیزی که قلعه نویی گفت اتفاق افتاد و یک هفته تعطیل شد. شنبه و یکشنبه و‌ سه شنبه تهران. دوشنبه کل کشور. پنجشنبه مشهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24731" target="_blank">📅 09:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24730">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rt7HZLm_0qoNTN0FhGKl9CVt38ZZyhIlUJXpS0wcGkJLHQlFwMvqJveYiOgSGIKEhCXi55i0_QTRIpJ8iCtYU-8-4uZxIK9kiZRsStVS8CymHAlZphBDZR-pkghN96-k5DuHPu0BE9J8b3DklmsMr3I7NSE9eI62mjKnfea6bGPaK6DLfjGsKr0s5KQttYGyuFDAtJ0JExlQjROmVLkxBC_cfGvyZT6UzslauRaCfKiJhyLRDSiXtat74s6eK6KVNOBhqzlkmYwrZmsrjvykz5aDa_RR1IwQGcHeDEt5wp1j9vSdKIFUvHi3j84Up_FwPDI7u1hxvNupMbY-Go99hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی 2026؛ فرانسهِ دشان حریف پاراگوئه در یک هشتم نهایی جام شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24730" target="_blank">📅 09:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24729">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJBooxuUxZglMOw4QpyjF6OE1OmmaUVjiXW4F4zrBgD9BU9MJlGshNuhvQfvR9d3UhoU3Zi_a8_1UanddMPraAsf-hy5xCe7KQ7X2CiJe6m-Gq0PhJ32GUk2GB64HbNXrBblacb-1iI_3zwYdqBs8kFm7P2e-1rmTHcMO87Otz37sjappSO8dYFDBsiSujjDmjrsPHAtpNd4j8MoJaLSeCR4aMluh4Cxowx9xW1k3B4tOCLFjoVshoVZ_6ogOJypgeC6d-hW_lXyVgmuCucErDerkGs2Yb9GDTlDaXMrnZ4X0sf3FhH8oLAT4Q8lZh9GUao042AEoYtdjPSn8uA8YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ اوسمار ویرا برای عقد قرارداد سه ساله با باشگاه تراکتور خواستار مبلغ 5.5 میلیون‌دلار برای‌ خودش و اعضای کادر فنی اش شده. درصورتیکه مدیریت باشگاه تراکتور با این درخواست موافقت کنند اوسمار راهی تبریز میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24729" target="_blank">📅 09:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24728">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ku4fKnUm5bt6AXgDcgRPeS9t5gbWIdLX8zbZ0EYh4yQEjK3Ar-zKCnCLGofjWAC3r1n0QMnQFppRy-gZ9zEO-GugJ9-lsjB97FiE9yQ9HhFUdI_VMIL3gmayTCLz7danPl7_S7cjLLyFh-RW5m7mrHfZ6h8VwithfgEV2PdZYhaUtwXDQOZqGgULEAbO90QVahJNtRZHZjBLMntsBwU0TWUlCkxruhqJ1mdI7RVLRG9xNhw3OUV-9rzClFITdUVlKQk6upe4RKLvgVStRZUdlEXQnv63u5UoklLkS1b8BH08dDm-OBm7PxVYLK8p3SvPPCciA6YcHghFfG_aT4drvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانردهم نهایی جام جهانی؛ خروس ها با درخشش کیلیان امباپه قاطعانه راهی مرحله بعدی شدند. گل‌های این دیدار دیدنی رو مشاهده کنید.
🇸🇪
سوئد
0️⃣
-
3️⃣
فرانسه
🇫🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24728" target="_blank">📅 02:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24727">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Un5Zgkaop5lngOVOrd_vP8rde8duMeR8ph_DBUWjFV8XK6hq3YzddYc2lQbnFkvlLHkCFsq7VLf7RMcqXDg2xzk1kgH9SEA9prWhpRzmzXhOvkPLtrUyLBsRt3A0y581_6VbgoUFv6mCwSaXEpAjAubUshPgR3EneY3SlY3tZejK_irz-KCyJihQlWnoKvahlX6nYWiWRmFcwDgI7rz15Dst2jjBdhvu0Laa16wUvBEAKoyJfdJbRAe8o-gJerTSnLlFujfN7dRALaE3pfs6P5hSJhSJvhrYjVUx8x-UNnBYCQrPvCNJkLL_asWIuR3OvYfot12rG_bjkMqubmHaeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24727" target="_blank">📅 02:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24726">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
برنامه‌‌‌دیدارها‌ی‌‌امروز؛ از مصاف سه‌شیرها مقابل کنگو تا دوئل جذاب یاران امباپه
🆚
گیوکرش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24726" target="_blank">📅 02:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24723">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e80e84f3dd.mp4?token=n_nttilNGa5ScRRxx5BXBuUm5jYzQ6f_4WBAWoDpQSc7FAT-uG_nE9KimZO3s8eeKKZaScHF-9TGwLPIoTpCha0VQAKyen4OThvWeADGxK1_QmZ2P6pEmedAd7Gmrc9ha_KCtdoKD2wovNLxDX0j5z99QkfJJgHRaAxUfUq6eH-6ScP8qBl0lo4bYRA9vbZhKLLGOF2oA2IpS-t9YXPXSi8cs1ijdlrGO3LuP8tNofhbDezK8386E4GHSBZDhELU6gqxfip1C6ILOQMWpAsLVckWHI_XT-ODK7ReHU3okk-oRcZ26xP8TTKwlkwikvm24R67wm41Jm_12ZyWPplkHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e80e84f3dd.mp4?token=n_nttilNGa5ScRRxx5BXBuUm5jYzQ6f_4WBAWoDpQSc7FAT-uG_nE9KimZO3s8eeKKZaScHF-9TGwLPIoTpCha0VQAKyen4OThvWeADGxK1_QmZ2P6pEmedAd7Gmrc9ha_KCtdoKD2wovNLxDX0j5z99QkfJJgHRaAxUfUq6eH-6ScP8qBl0lo4bYRA9vbZhKLLGOF2oA2IpS-t9YXPXSi8cs1ijdlrGO3LuP8tNofhbDezK8386E4GHSBZDhELU6gqxfip1C6ILOQMWpAsLVckWHI_XT-ODK7ReHU3okk-oRcZ26xP8TTKwlkwikvm24R67wm41Jm_12ZyWPplkHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇯🇵
اشتباه مرگ‌بار و فاجعه‌بازیکنان‌تیم ژاپن در بازی شب‌گذشته‌مقابل برزیل که باعث حذف این تیم شایسته از جام جهانی شد؛ با گزارش عادل ببینید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24723" target="_blank">📅 02:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24722">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjF4PyeMyYTeTHrltmwxcuyjlNHcw9YCb4mmHXr4hJpCSWPsLxnEomglDRNVigWplS2KJHcihxpEwDWdD2OKQg4yUO1_ULBFDOEp_XZ-TQstdiZAYi3RPWc-pxQO794xue4Q_hmlq30KHxbUG1VkzitRKVpcef082cwkiDFgDfew-5gAPg-2UFlOFNxM2pcu0fQNfA9GKqsKMI5_gFVj5NFQo6UbPvoi_KoSX414jQ2DFGwD_isd3Myp0xfSz1QmdVIOp2why1j59qYa7-JitQon-pRpVrZ9AdTmY1VpOSqDpURZeb0tIXiNBemgaz0H5U4zoPejdJdKDjRcbUsNVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بعداز آسانی؛ منیر الحدادی نیز چراغ سبز نشون داد: تاابتدای هفته‌آینده با خانواده‌ام به تهران برمیگردیم. بااستقلال قرارداد دارم و به آن متعهدم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24722" target="_blank">📅 01:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24721">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de066ea2ae.mp4?token=nG1WY89YMvZSwwuOm3dExE0_AVST7eKqGPuGwssBj4CcNFPsl8ASilJpd8qjEFkUBpu9EkxoyvodI9P-Hp3ofJfPKIXH7tMZxlGyD4WNkMeNVBnkQP-yQ6bczPnr6_Yd2nsKpBVEn4hKXeu-wbriw2YxjVdnqcqLfEawiQ5sf3LDSzNKy2pdm0V7QApINbeuooAzrXGfdTtzBO8xcE-w1oKjchcwt4m9IWram4fQZ4GoG7j3X3FNf8upWSb7d_7S-lRzSQGUI2-EU9XZ7Sf_dMBUdfXNAKH26O5A96GVYAGxhjRdlZK35CI1ZveuhnjLP1_GgKZqP6hPSZbaFcQCsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de066ea2ae.mp4?token=nG1WY89YMvZSwwuOm3dExE0_AVST7eKqGPuGwssBj4CcNFPsl8ASilJpd8qjEFkUBpu9EkxoyvodI9P-Hp3ofJfPKIXH7tMZxlGyD4WNkMeNVBnkQP-yQ6bczPnr6_Yd2nsKpBVEn4hKXeu-wbriw2YxjVdnqcqLfEawiQ5sf3LDSzNKy2pdm0V7QApINbeuooAzrXGfdTtzBO8xcE-w1oKjchcwt4m9IWram4fQZ4GoG7j3X3FNf8upWSb7d_7S-lRzSQGUI2-EU9XZ7Sf_dMBUdfXNAKH26O5A96GVYAGxhjRdlZK35CI1ZveuhnjLP1_GgKZqP6hPSZbaFcQCsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
داستان عجیب ازدواج و جدایی محسن مسلمان ستاره سال‌های نچندان‌دور باشگاه پرسپولیس: دو تا خونه و ۱۱۴سکه‌به‌نیت ۱۱۴ معصوم توهمون سال ۹۶ دادم رفت! دیگه هیجوقت سمت زن گرفتن نمیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24721" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24720">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkIKVo2fNb_v8HTMG3JwjMQgU9gUquSXYgwMvG5NyOru39uLmMelyZtCC0rRVN9TmyUgB9L_V-Ic8kzaH3Prk_RhfvivAcUofydn3WKp02J70AtksxpnOCD7u2xuzQxtYjupNTzi3-IatdnXK73u8IXqHcVIEOyq_f6uzcsDvOMNcs95Qm3LqFGiaPf1vVkNY4ikruE83iU2vr34afgqBOmKcNKXR_9R36fJqjczuA-Biek4D8DCDhLl6_0oX34DjHIJdve1AGEaxp2kfi3IULQLGV0xXF5IljVR-lbE27MYXPDANSW6df_qU878ren26pqQEDJL-Pt1Bz3uKJSaEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نشریه بیلد: هری کین اگه با بایرن مونیخ قراردادش رو تمدید نکنه مقصد بعدی او قطعا بارسا خواهد بود اما الان هدف اصلی بارسا جذب آلوارز و هدف کین تمدید قراردادش با باواریایی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24720" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24718">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCxUzDLbJGwRhMlp5v0qZ2KyXeJ4jjxQ0QY67R_hFGf_7A0ZNGpE_7SCLDbzeYH6QtSt9ds8ggCEb5onFsvi-YSby7RcBo6w2TpD_eabdrLjX4jB62JgG_0rYV8yiRrkruQNjniYp8tasDYt-iTJdkMEUuGYpUl7Hfz6wp0YCBmzow-t6OFTbpDkiR2WJlsk4dUeNLsGbHpZFMleLSq4Bs09t8KjeeKrXHgSTKEFU0yP5cTvg6unqp48858rT5Ne6U9hyNo3RNhffXoIUcOgBq4tNwT-Ba_5e2a16pDxUgKFuBRr0EIQMCswQZjpFxrfrMk3YPf6JqT55rabMY6ofw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
نشریهESPN
: علیرضا فغانی باعملکرد فوق العاده خود در رقابت های جام جهانی به اصلی ترین گزینه فیفا برای‌‌قضاوت بازی فینال جام تبدیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24718" target="_blank">📅 01:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24717">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vALPIZXL1LrYWIrbBK4xcIcqlyvymadTWgA9ZhZ2egFepxiYrwTEL17MNnkALraIiUx3RDAwytvtFJGL4VAWhtRIXj3wLnzOFtL5aLIjTutRerBFYwoqKmmOE04kmTRkNZhUzlR0a6SaHYNFtWtGE2wj7uKif7j2NKYyPwSfMUKAUvLzTx9Nqfm3i10M1pYUOS0vygIc857t-ChDMsSysZqOd8HW0in_LN3Ni8t3cfe3poK_QJX_yK01Es1X5jfsTomPMrXx_ND_wNfMad9NsX4K18YCfpbkKS1nSvVA1MI30AtNQkPld9UjB5yXTpdH09IWJxKjw3YeN-S_OOCcYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24717" target="_blank">📅 01:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24715">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxCBeLLTMd8SL5EI2XXZeqeVxLega95dSv5RbaU6fVNd_qxUmoFkkb-PFhl2m9jUBiR9K_Ig4tzZCQBT-16FzNR--oX0C81iO2hJIG5BXZSRLV9mL3jsm6UdOYGQOUvmzcG47HiDwI6gYeDlDxw2Y9yJ_7uNYSY7l04jTsM0HotQO27of72HC-3io-hEkWoLYs7l5k4TLVt6JX-CLrL8y9Ng8y-YUsQM2x1egT-4umKMulTjY7XhQH8ZJ9pFULnYs0irICf2nczmHcV0xnjboxZoiUvoRMYQgZuuUdi_MSfV2628myKBt8ErwAfheQsvbSzRjb9LE78C1fzSXO9_dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
جیانی‌اینفانتینو رئیس‌فیفا تو دوهفته گذشته 24 مسابقه رو تو جام‌‌جهانی از نزدیک نگاه کرد و بیش از 50 هزار کیلومتر رو در یک جت خصوصی گذروند.
‼️
براساس‌برآوردهای بی بی سی، تاثیر آب و هوایی سفر جت اینفانتینو در این دو هفته با انتشار سالانه گازهای گلخانه ای حدود…</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24715" target="_blank">📅 01:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24714">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNtsVdxc1D-0L-e_k8VYtUE3Ip0TaR7hF2rcWsL5adCyg-tgRDFmBV0wB_we5lN7gykp0TBF0Q_Dy1L5NBYkDEIk8czGuJCiqC9H-wqfSZiCavOWxKSbtWXkrcdfNIiHoF7NKDfjcFU_VRNG5V4h2hQFpqI4ohwuze_XIa8_2ETCG7-ll2bpInA3NiozprpDxRZsm3H8EPd8MW4GYyrVOfXJyfykLQZnKc1kh-a5cp5hMbaqpCHH1cPt1KXBL64egVg0_cQhnKdzNqUUfK3GxpcEBxflagZd39dTRR5Q4vQIIrPQINaqlZnYWZ_N3ar4s9JjHhJWgWpw-tysg-pS7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌چجوری‌هرروزکل‌بازیارومیبینه‌اصلا میخوابه چیزی میخوره؟ چجوری به‌این‌سرعت جابجا میشه؟ منی‌که‌میدونم از اینفانتینو دو تا هست ولی نمیتونم ثابت کنم‌. مگه‌میشه‌به‌این سرعت استادیوما رو بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24714" target="_blank">📅 00:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24713">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ID211Jl81SIIqATe1sxEMAmLEy23fe4MgnnAJdahaSx0QL_U2vF6xVEQfA69dElYV3y1-f81S_NzPIiFoHwXQsRPRx-nh5xolYjLMpKYQ-p53_LOdbC9eVIEswrhLh6INhhzhCXq1JL_YegsNHR6LMNHGBNL8LIEIVcTt2qCBUjDhOdIgAF243ddLBCwvPZJxsfgr69LDnNxCCDGWGvkMOXjYiOTS342PuaH9_BVMtpgj9KhThkIVzEMMLMNMjpMgGNl1YZYvmaSTn1APWLGOMATJ8Sx4jCWfuB3rcJ9FFCWxWyPwhPv7_fBcQpeYhNkwMQBvfIjxn_vSPOlSh8Q7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اگراتفاق خاصی رخ‌ندهد گابریل پین مربی ایتالیایی سابق تیم ملی ایتالیا با عقد قرار دادی 1+1 ساله به جمع آبی پوشان پایتخت باز خواهد گشت. توافقات نهایی بین طرفین در ساعات گذشته انجام شده و با دریافت پیش پرداختی قرارداد…</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24713" target="_blank">📅 00:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24712">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8zNqfv8OarafMuVpXEGM-N4RRIqDcMRyTmEyRAUyRVXIX0FQubyOR88VLeFSvVAsqV-RQ4iZLFJegzZfAwvnEb50hrrqc2SbitEXTa87DjoBKytbh2tZgPqAKontCztH7uh6s_N3ZMcQdluFenJx2LlyaGUU6GtOpcGh7bvU1fkdJLJdmzUvuloIu9lr8sad4OIh9u647cpS2qHqWbu4Kg-aMtNd_NqIPX5FAWosxOI_eg6BD28rPOURiS8NjuiFNdWfKYIPcsk-aqP83nq15LNnHiTel_Tlr7LyctLXK0q3_RtXrSyJmIm9lCoL-kPkQJQUmDVFDxpZrV3HTDEEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24712" target="_blank">📅 00:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24710">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0V1RUBq9SZuxxi5gpnal76mtSXcJrT56KjzRfA3FiTyi29UmKCSlYhcJ_6DeWXggjzh9-yfcre6s3m3pxhccx69k5F9MEZ34oAsCu2sqi0QFvCbQmbzHAxmQ-M_zbeBn_aeqrXGFiXHEBz55R3burjyJWNXj0a8cr9boJm8qC7-k9Z7QWLfTpy84YbkTAuAPJgCvPnwGyMdQx5a_mjpqpDwoUcKv6y6twjbmDNFP4A9iHZ9JZauSCxfurkc5NuRWBVCKPi6L7xSGuiOCgqAYJsS9qPOWQzhM7gom48baX2iQV5eZjELamxDxngrcOPD64qxxKuw5_5OzW4Dhtwltg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارها‌ی‌‌امروز؛
از مصاف سه‌شیرها مقابل کنگو تا دوئل جذاب یاران امباپه
🆚
گیوکرش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24710" target="_blank">📅 23:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24709">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgYKdOq5TWZRP7Fe2tBsG-Jn9pC2qy3Bc7sqhd-9kfTPYDhQiiOtP5MicqnTuzlOgowcDZyxqP2gSX0_1NoqlRp3m2-whCpODYA_Lsv7-MIYeKLQBcVshNBPZTDJRM2iUu0HwS9A19WxIwyDMlXgRJjYKJxwfuAh7lWhxdd0TJVwcZiMHPEFHsD6M7HVO3IqC_YBCSKCGH3uBwzDNVqgpuMQcKmJ1FSAMlout3JcMB56-H79dTNxiKE1KEarY5fxiM90AbBvQe2bnMNTFZV9BBOusFyQFhafMI8h27mm2nYLlxAQ3NRTycFNWz6Zxq4JZj07NQ0qrkJHN8u9S8huIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دیروز؛
از وداع زودهنگام هلند و آلمان با جام‌جهانی تا برتری بزرگ نروژ با گلزنی هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24709" target="_blank">📅 23:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24708">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgB9uY0QVR8lCH8neBx0q4sSxVdrIg02FiozqE0kW8poAQKK6o0NLXqTeGOHccW9aewMbCBMUOoW3RaGFUmyXZK82djGjNI0XhbvdfSTOJYN7daEHJTDZJK_9A2W8IwbrTgbpOj3Q29R9rC4zAw20ADNyWif9zNmbtgIOnO8ZZtQZAQ78cP0LwEgz2oeAxQf45aXx8DhdJysL4AFU97md5ltJ0D28lKvhLPLdoI6ojX4fquh5O3yqKXeHkU2GN3Par2YCNP_9kIuCFi2RkKBgsfaQ_xAQ_VPVQl7vrgMfYTBeOh727L7wWwUQns3LZifgpTna1N96dor0k09E8SSAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
مقایسه جذاب عملکرد بردلی بارکولا و لامین یامال دوستاره‌پاریسن‌ژرمن
🆚
بارسلونا در کل دوران حرفه‌ایشون؛ بارکولا بسیار علاقمنده که بعد از رقابت های جام جهانی از PSG جدا و راهی بارسا بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24708" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24707">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwtP7PHeNp_nPRPqIGA_I5cdlO66WSKbtn9uK8DIZvTn3Cp-VQd28wnaYri2hr12fwRAGV9bAysebvxy__6N2Q3yZq_RtJSKOoS5yhuiDhgEBQ4zGniWbiI4N-WWr1MsZy9t6ZE828YaV4wYoJcOQmsIc1Qsx2TBAIWM_4pP7LrPqsywWAGOqw1D9G-_aHMPMDvgHGvLeJw8HpA1rzk7Dm8HOIdJWwHhkWJKInsG1v2Hu9FWCSmEuvkcNxghI-UJottnW-x4NayIXYp3E51e0RHyGCq5JwScG1lEB2Q1HS9rzAGKf3fCYIUTbH4U4Tzfc8VfR-R0hmsovevMS1-bZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نروژ باگل دقیقه 86 هالند ساحل‌عاج‌رو شکست داد و حریف برزیل در یک هشتم جام جهانی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24707" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24705">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oWIY3fR5sXUPmBS3-3swfd_8FmVD3H3h6eCpKiY5UhcwdgpxZ4VKHsYISMwAUOg5BzW-H0_7h1ymlX732YTRe767hArA5burLfwQRJKWn_dpAQki-AfPF2AvurMC0rVfndYfXq-g5VfiLoynKfvM6ACNMDmjzsewLObp6ayMAFa7A3YUi6j_RyeCVuBH1iRMKCJLxb-mJ8bDHGLB1btKDLrRNSJmkJltLMoil3o1rtS8mfsBY27VixamgKSweXf9WgAMVfTgRyDJ0i_LKri27V0XsaMMI1tbw8SNdPhB4As5nKOermd0i4T_hk5VZJsF-VCiUrAOnKc6y9twe3yW5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l4qRP9ULE85IGKn0pOZHgQHyx_tfo-HFdxb4sdYF0Il6RPT-uyHsRWb3MYDaZ0hGTsx4JnPk4hFUZCk8mPLSZHZjiZZwChKxpoAIJjHSr_TihyMETZQPUnRr1tOMgst2GQBhy9MhpbcWE_RhglvF9QyAB5Va67cXV3xvjFFi9YI7MrK47cL9x1ba-L-SnKID51FhfxJGyljCDj1YjvdHJI8QkMKfgEIpgsWkb4AKSdGFbTy9cLXtRxshvHzEX5kbhDWzc7RhvBLddt7Kj-SFk6-Mu-bf7zalCj5DqIwQPVL706GK7Gal9YCIV_RV2z6QrgLJcRsUWxjlyorjJ0UwkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇽
🆚
🇻🇪
🗓️
۱۰ تیر
⏰
۰۴:۳۰
مکزیک
🆚
ونزوئلا
صعود مکزیک یا شگفتی ونزوئلا؟
⚽
🔥
مکزیکِ به عنوان یکی از میزبانها این رقابتها برای ادامه مسیر به میدان می‌آید، اما ونزوئلا با انگیزه ادامه شگفتی‌هایش به دنبال حذف یکی از میزبانان است.
👀
⚡️
میزبان صعود می‌کند یا شگفتی در این جام ادامه دارد؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24705" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24703">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FHR4gMOnJrVoB3_Rdr7osIBZT1BOTH_EckXEex4cBJpj7bNLisT6MXVyog7GKV63ed9v18g0SRMUmFnzzLQYC7BQcJXsl9XQILWKmKzkH-yhIvopkz3uFRINotXZlJT3E-YTv5vq06hxihAroshwVa1L5BfLde-Cfsp4jFN3JDLhsm84J6fSjhcbezBHo9NKoWLhxZLdk-b-OVI7CYm2B1yORf6o2vLVYsCPKdHsxYXeYNq6Qm_UqRopR-YQJChYkO22ELm9SEf7zKKLQMv-th14Weu-H-YuFz1b42liY2nGHYpcH9bHoscZZGKL1hmXlfytfR7fVGa8dHc0MSj86A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UtK7gpCpXYi1XdOYc3-yBqF4PZMAiuOpwjQPyqFYYvP5XDPLwlbJ_FZ6NiOysd8JqDSbYTGqchSilyGRm-CRpkEgu2H-qh8eyPld1flALoYw9-w8VLOTyLifWaxg3aM_MlCX_NymFrUpfTAoHESUGsziE2F0YpLS9ca3MGuUIVrQg1krtgftg4fNfx6c5ZA3WGWU3Jof8i9IensGvvur8DuzQjTrStZHslQyu3nyGR41vEM_plVoqlPJ3k_xIOeyWGdEiucnMKXCaBWttcRd8kWrNDbS8XPmb1y_PH6IYBV_aJhV4xG7l_XlRdvqw1zacSDgUfJkoZV-L5IABcVLUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌هفته‌اول لالیگا و الکلاسیکوهای رفت و برگشت پس از انجام قرعه‌کشی فصل جدی
د
‼️
دیدار رفت ال‌کلاسیکو:‌ یکشنبه 3 آبان 1405 در نوکمپ؛ دیدار برگشت ال‌کلاسیکو:‌ یکشنبه 19 اردیبهشت ماه 1406 در ورزشگاه برنابئو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24703" target="_blank">📅 23:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24702">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtJlTsCiM5mqfmXdzzvaAo03IyNgxtWJ7VNnt2DiD5iFl428yh4JnAkRXzG7sYiywxImA1iRPkaj03L3AuE5AaaDxgb6brSK8WlzdiZkYlPA2pcxBbHCEOG1zZh09S31skBSkva63YOBIL6uJUw9JYz3dGaNXDtF0XlSQ6JMKKTKCkFwVB9yVXxklcwhoO4oHLuGRN43w9QYEgw3d9HeQM87lxmRc1mFGnlVN9VVlRWrFcySjfx0NsDAGzmbcbjF9nGsnFB06JFg1TBi9XcOgzYpui0PvDSOmdpHNHwjNa4tBbIbFReShRlT_m5Degk22vy7juRldxfQkLCvp96ztg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخباردریافتی پرشیانا؛ باشگاه پرسپولیس تا پایان‌هفته‌از دراگان اسکوچیچ، مهدی تیکدری و کسری طاهری سه خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24702" target="_blank">📅 22:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24701">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxQH78p0OfNpsS_m-6PohUBwtLCguR7sSDHi20SxjvFjF2X18Z9cRF892-Btg0yK-rlcgQOaEjaKG9tELFByKcLkIet3mo8YwaLWzweuWCpzA-XPml-4tlWEzKT4y31d05BOQFAHGgQbBVYMy9FZ0K5Xzp_bQyedczJMmCZPk5jnEQ0fGaEjeUCTudMJIJeDBW_NNpJoo0ZuHTBMhSiAQKpmvsRWU1RjLPtyj-hngso1uJdsdd9_UkGfOxHVEPvludDoDizBPJHy5KMLpiLB_8aQTNa6Y-a1nhwGwO6KdjeJKxu27A7ZMHKENPjrvV1kRDSc9zo-je_BiaLyhBCg4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تااینجای‌جام‌جهانی 2026؛ خطرناک‌ترین چیز نه پنالتی بوده، نه وار فقط و فقط یه عکس یادگاری!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/24701" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24700">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LY5QyDXCZTkZm7nNhH5rhLZpdheTPx8d9qBoh3rER4sLev1D4A1-qkymyiFNVvK_R3zHq7HSvGI-JbS2p0hNhpgzTfhLBlgd89_zuKHwpVhXSgWjXxPklJFOnMD_eWEeGN4putSpq2Cw2lYMJczOusLmhMnOfo6b-TC4oYRWo5q-E_ABreMHDhnsZjc8M4lj_B6A-3t1WCfpUhVNozPQNR8lHQKIhqZp5BfkUeTkEqOWuxvoxsxqAVdYdFYVvvY5m5EEiHIvGThassvV7exCc6sucXZecovT77rArYbl_5lBVkOamoABmxuxubySk_k-PtvD-NA6f8PPhfS2cLMx8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇳🇴
سوپرگل‌دیدنی نروژی‌ها در بازی امشب مقابل ساحل عاج در یک شانردهم نهایی؛ چه کاتی برداشت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24700" target="_blank">📅 22:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24699">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1GKT6rH7mwboYPsvgzhL_aDfIV6XO3ggM60KmYcPDAgaJW7E6VtQ80o-MtNPVRfJlHLc6EX3ZTxkfimwweonsXZq9XKdHuAYY0RIEVFBbp3MJCWm3R7L8V2qwQubHKAHToSWd0FQhxA8_NLaDs--mMQ5wKfBq-bJvZ6h3wwh--WKd6yAwS6eTfwDik1fxsvi8js4-H9-MiAp7rasjhD414aEhODtrkan0IUx3yVcUcW8ldp5yAWdzYrt_3jGypvQIHto10IMDOFGXU9yqW3biMi3rueYIB6PDQ-t6dzpVzjK4C2B4vXWEuC5gDpVE6kJxchjmKtahO8jUuPBaTTIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال بسیار زیاد بخش رسانه ای باشگاه پرسپولیس فردا پوستر رونمایی از دراگان اسکوچیچ سرمربی‌جدید خود رو منتشر خواهد کرد‌.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/24699" target="_blank">📅 22:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24698">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JA3mtVM6HeA0RLiu3L9u7DPqX819UwBYsWmrP6KHtuqrMsW4RCIdqh72hZ7XKXTrNCDQvXNodtnmEgp8kr2A0toIFMRwzamqbBzMjZQFlVNXxSS2NFvL6F0tQpmLbGz7itViV1BJG_sYHmT6Xto7p0QSkBa3q5ZdSBySo78X6HJQPj6tHxY3Uk8jraKTLn_JcXiLd19EkZmBXFnbe1pR7jsf0xdC9M_7hxHkerS1zVO1TY9sTDHSxCkSn8CgtEznd8yIZ3c79W1eA2BD8kWpjDfsVzNAnspnY7DzsP0zZkGKG7DO2oXyqHyzjIS7PzzPar9grvNlrCdLLU02FqcLRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خداداد عزیزی در ویژه برنامه امشب جام جهانی اعلام کرد بنا به دلایلی پیوستنش به تیم پرسپولیس منتفی شده و فصل بعد نیز در تراکتور خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/24698" target="_blank">📅 22:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24697">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b011e22cad.mp4?token=SdtTegZL7FAWMgP8gq__9uAjESYMBECIViQeEQTGC1Rt31ydF1fLhso9CLQRd3J9hliAuzqiAhzuNT1Tr4V93AWgdCgodHwfjAfa8iCOcDQhvUkHnZEitwvPl17qXMwcg_95Jt9DU_XdLJculxbBwfDb6cLg7jX8psICDiCoot6OsJMC9Gn08MpcsNXxA43s4unJx5JNe6rphPfkV27doG6245Iz2pMBQgcAA4XsEefxfqgUWHR5z0X3dfTH3cmQ35PinAlzAjOOSQs3B30L49s4jvhFH4OHMcAJvezvgo8GWieYtFeZQVKdXe6GpJIwGKXd9_SHEJ1OP4x5UNMtew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b011e22cad.mp4?token=SdtTegZL7FAWMgP8gq__9uAjESYMBECIViQeEQTGC1Rt31ydF1fLhso9CLQRd3J9hliAuzqiAhzuNT1Tr4V93AWgdCgodHwfjAfa8iCOcDQhvUkHnZEitwvPl17qXMwcg_95Jt9DU_XdLJculxbBwfDb6cLg7jX8psICDiCoot6OsJMC9Gn08MpcsNXxA43s4unJx5JNe6rphPfkV27doG6245Iz2pMBQgcAA4XsEefxfqgUWHR5z0X3dfTH3cmQ35PinAlzAjOOSQs3B30L49s4jvhFH4OHMcAJvezvgo8GWieYtFeZQVKdXe6GpJIwGKXd9_SHEJ1OP4x5UNMtew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اون‌بازیکن‌تیم‌ملی‌هائیتی‌که‌کارش‌هندونه کاشتن و فروختنه، وقتی میفهمه من رو کلین شیت مراکش بت زدم: این چه سوپرگل برگ ریزونی بود که زدن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/24697" target="_blank">📅 21:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24696">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGPb9cEUuzU3K46x_-UjYoioaplQaT21y_ya9ip5DDvIbAp58Paq0JDpRR7BEr31iBfmOMWkk311k9hX-ALxdXUSkfvg-PrQJ8Z2Bkw17pfwlCZvLQcYE6uns8fXvRaSNliWPOYKlfdiVBk-0AVda22XnhuwWeHfZDissQ-mQKxzX1BiZY5DBwb2bEJfFj6m3XxDIO2yXSRCLz2FSp-TtHJuOeQJ4CTLuduenkDv7UHoyZEHF_WbN-mN5Ca90_QQbqit3PVpq9B7VLB5N-fWNe041vfBl43k4RyOKBzrFzZ9xbVooW9YwU1p3YQY_h86QHWTv3C3Ig0OXPInQX3ojg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
لامین‌یامال:
شانس تیم‌ملی اسپانیا برای قهرمانی درجام‌جهانی‌بسیار بیشتر از بقیه تیم هاست. فرانسه بسیار ضعیف‌شده و تیمی نیست که بخواد ما روتهدیدکنه. هرچند بازی دیگه با اونا داشته باشیم باز هم با اختلاف میبریمشون؛ ضمن این‌که تو عکسه هم خبرنگاره سرشوخی رو با سپهر حیدری هم بازی کرد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/24696" target="_blank">📅 21:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24695">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9726fa772b.mp4?token=Ufu5sxQm5mMAgNgEaSq4akT7OaNOD3Am6WtrziZ4AArLoytCOpbwipkkXeMnPzcJ_ActVDRdSFb7keEcWNBF3GaJV-rHkrKJY2EtL_9YG8MmZwWGnXCCUn-iQtWb2Zckk-3_wzuPLY1ArfqowYxn5PnoiPTABXLhq5FivdcaMzNM-MlmDr1wf1PWNyXC6PpypxNa36T4SkDh2CEHT-kXQ2SLnHuaglB5gXrvi2PJ6m1ApKKnRsZEKT7NkavEgwlBjtcpW0lVovB6ipAwrENQz2iL9JsuY612uptm3zz7uNLwejNQfqNo_8aauRPeZgtz4tdC0lBDCZhSJ_ehi9b1xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9726fa772b.mp4?token=Ufu5sxQm5mMAgNgEaSq4akT7OaNOD3Am6WtrziZ4AArLoytCOpbwipkkXeMnPzcJ_ActVDRdSFb7keEcWNBF3GaJV-rHkrKJY2EtL_9YG8MmZwWGnXCCUn-iQtWb2Zckk-3_wzuPLY1ArfqowYxn5PnoiPTABXLhq5FivdcaMzNM-MlmDr1wf1PWNyXC6PpypxNa36T4SkDh2CEHT-kXQ2SLnHuaglB5gXrvi2PJ6m1ApKKnRsZEKT7NkavEgwlBjtcpW0lVovB6ipAwrENQz2iL9JsuY612uptm3zz7uNLwejNQfqNo_8aauRPeZgtz4tdC0lBDCZhSJ_ehi9b1xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ فردا؛ از مصاف مانشافت برابر پاراگوئه تا نبرد تماشایی هلند vs مراکش و جدال حساس یاران هالند مقابل ساحل عاج
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/24695" target="_blank">📅 21:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24694">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72b5a564e.mp4?token=NnVoINh1nJ_I-cwy3GA9b0mdUYOFzTdSlLCm32O60sNZ_ea7Q_6aRRFhn0DfDrr_GylFikucx0fNzjPIkwG7YpPkZQjQo28M6D4bczMvAd05zkadmI8Ss_41o4OXQudDM6QMNpCEulR8baj8Q7qZMNeULTklSqPlgWhC8BcNoeM5h9FWWzR5J1IAW1oZc2zz99yFhtCwMa-RQW3CLalefitwueKZUtSE9tGVoZJhLn7iHnuqyEwfR1krD2KYXRpnJo2hMwyAmoARq7InL3d-z-jL1rMhxhjJ9UyuFBFRTXOrn-py9aJVed_OJs43XZDcg-qF2nB9bEghen1_1Tjt9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72b5a564e.mp4?token=NnVoINh1nJ_I-cwy3GA9b0mdUYOFzTdSlLCm32O60sNZ_ea7Q_6aRRFhn0DfDrr_GylFikucx0fNzjPIkwG7YpPkZQjQo28M6D4bczMvAd05zkadmI8Ss_41o4OXQudDM6QMNpCEulR8baj8Q7qZMNeULTklSqPlgWhC8BcNoeM5h9FWWzR5J1IAW1oZc2zz99yFhtCwMa-RQW3CLalefitwueKZUtSE9tGVoZJhLn7iHnuqyEwfR1krD2KYXRpnJo2hMwyAmoARq7InL3d-z-jL1rMhxhjJ9UyuFBFRTXOrn-py9aJVed_OJs43XZDcg-qF2nB9bEghen1_1Tjt9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
👤
باشگاه پرسپولیس در اقدامی عجیب در روزهای گذشته با خداداد عزیزی سرپرست فصل قبل تراکتورصحبت‌‌های‌‌مفصلی  داشته‌اند و قصد دارند که او رو برای فصل بعنوان بعنوان سرپرست جدید سرخ ها انتخاب کنند. فعلا قراردادی امضانشده اما احتمال اینکه عزیزی به پرسپولیس بیاید…</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/24694" target="_blank">📅 20:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24693">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fa40FrcHxuWXrBAqSzNePWiuyXXViZRU1G2L55N-dPVoR8E05nHvvsaWECuXBY3yV6zBWWGcuN0MeSFOP3W8HOL-Tqorzl8L9WGPExYmiE5OePjL7JbsgIIws_0TM83bxoe3VronUxgJbRvTsRYMCpkcuJvkooaUWXykqQ5lYk2S7A7sYtpYHMlarvZpckMZIGT2rqj0tBWblPtclpD6MlxrRbn5x2tIO0Ikrm6wT90XdARXyrY2GFOOjbVeFjKTSmXqHKNURnBT4IGMRstXSj1jHk4BSK6rVnVXdP6YlEhDD03Ha_Wzouln5LkIr_C6IfTo5Ao5ql1Wl_xMJsXvxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
همانطور که پیش‌تر خبر دادیم؛ یاسر آسانی ستاره آلبانیایی استقلال بامدادفردا وارد تهران خواهد شد و در تمرینات آبی پوشان پایتخت شرکت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/24693" target="_blank">📅 20:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24692">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNzg5n3tp8f0Ot4EmerHLBB6G4VUdRgp_vqDRB3oWAcIgvDPKgDuAjdubUzXuW088vvMjCI_-ekxuQYWGsJsbwx0uu_XCPVGYQglmcXxjyDEvGwvechYRyyc70tvG45k_73WSE9sBlcuJq194Y8A5N0CpGuJYKU2YJgN6JN3WZiZSEyUNplfj-PvhXxWWBC-Bt4ru3KXx9ldBbbmNxt9Bb2PqaKNDKIHdW9rJ-PHpfcm2YxQljphSUt_uwuETp3rH7dOIeCsYOjOUC5RyKBSgvRBiVwaPfYgoUoaSFj2DXT1hvQuW5tTWUPUeGl-ZSDyXq8H-A7AFzJ9_hj6yMiB4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فلورین‌پلتنبرگ: سران‌منچستریونایتد با ماتئوس فرناندز برای عقد قراردادی پنج ساله به توافق کامل رسیده و حالا توافق با وستهم باقی مونده است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/24692" target="_blank">📅 20:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24691">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bv0VYbNc7rpFqgkw64D_8AdL03EeHFWMa4Ro1TLW4epTeuV_Hu9ESRNN4RgKqKQYM5sbi8fSrM6T5Y1NFjJMII-UGngIYumLv7s2qqOCk0tDIjRGT_V2t7yd7ht1ZyD0LZhsmwzbuKAwQMu4ieaKh5I6Nuvgb2uF2-G3c-rmKroiYNvqpMPZXU9AKfwhvH-QRBwNsnAUXVvaC2fTQxQPDUL_JcsmlQeBCLOwvSnpIrsOhtBlQLgY7NNzPXe0sa6Bjq6H8o2uKZtgr19W21XzWJYdotJjUq7rW-eMrg1zCymMZqDdABj9_vTVX9YqmJW5lsYK7ZecjCMOPp282bfKsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ باشگاه پرسپولیس درتلاشه امروز برای دراگان اسکوچیچ بلیط‌تهیه‌کنه و این سرمربی کروات ظرف 48 ساعت‌آینده با دستیارانش وارد تهران شود.
‼️
بعد از رونمایی‌ از سنگ‌ اندازی این مدت بازیکن کهنه‌کارباندباز سرخپوشان‌پایتخت خواهیم گفت. این بازیکن از وقتی فهمید…</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/24691" target="_blank">📅 19:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24690">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHGk0N1ZrRQUnVFTICjbqYpq0UzPugwACv9CqoJjitoTBTMtRhRHNFsy-arnKPHnqyiD3wVLee2x_NehSAiP3Jddppard3u8EsQ6Q0nW1_YNfTloeHaIDp2rKHG0AdHuXLkHROrL7IOyIJxBlwkGNpgslHykGkId6jBdxBncYE1sAVC4bECqrmCoCUw3pBmBYqkxzw5VhUeSevqPgY9dh3p6v77JmTqU6oHJZpJQEwRPDkW_t2JrPfcqWWj3MhWjlhUL8VVrcDAy3s7xPBldT1hTM8r9n0cnFON7ozDxb9WmOI6bwd1rfOXvgSQBxNUSowrKBVytPN1ohRwCw_CDQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛باشگاه پرسپولیس و بانک شهر مبلغ توافق شده به اوسمار ویرا و کادرش روفراهم کرده و فرداصبح قراره‌این‌مبلغ به حساب او واریز کنه و رسما پوستر برکناری‌اش رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/24690" target="_blank">📅 19:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24689">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ul4QcIReselJ2qFZpUkc39yYsbobOrotYvAAfEedXb-bAs0LT7uZCX7Buo3FYhxEAwaw3IBkpxWWO1joKQ7gr1-JB9nDSA7p7njguvlMTsmFOtzaTk2cFXllf1iW4yIJBzHZMSV-JFf95fOJhBW_HH-8tZfUQvVGGPjhElfy2R-2g7aqkyexMT21V5p7LBSXHDv8xJl5J8D2O7KdlRlbOpA8pV1s7irEs6IDPfgq87qWI_b1vIO8PDFoLeenJ9HiIihGS9dNw-8WyJeJrNqWVfPK4_NvnJ8IO05I8gRoZvXzKGfPKuT9Z__Gn2Prbra8Blb7zxF9kbk_F_dC_GOqZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ضربات پنالتی دیدار امشب آلمان
🆚
پاراگوئه در مرحله یک شانردهم نهایی رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/24689" target="_blank">📅 19:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24686">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e47b5880.mp4?token=Uy-mWfLNp4rUJTPfW5KwCTr9J1YvdcZDI12wzW6vL_Qj_qw0PgUqra1fJTPBdwzqtIyKK6VWTWfrrLcibqzyQ1rt3uBPZjkuH9FOcUDWM1HckJrnI6mMaEm2ZRJTg_qVNcFR_YaMeX7plys_-ZFYE89JW0xz3J8kzWM_tPEmFIGhqFbKwVHUIkpNdLhy2di8Is-pEhphy4g4vVGQXNtAmV3A1QFd5YpMLL8GXDzuF3zsuq7jT8Zj7C1zcKWA87ChPAWRIJUmX2CiRSlsjDpkQbT0ZgazVRO4QF6bp_06zo51NhYdU18bWHl81CxRz0ng7A66ujACyD2TD8GzdUXsxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e47b5880.mp4?token=Uy-mWfLNp4rUJTPfW5KwCTr9J1YvdcZDI12wzW6vL_Qj_qw0PgUqra1fJTPBdwzqtIyKK6VWTWfrrLcibqzyQ1rt3uBPZjkuH9FOcUDWM1HckJrnI6mMaEm2ZRJTg_qVNcFR_YaMeX7plys_-ZFYE89JW0xz3J8kzWM_tPEmFIGhqFbKwVHUIkpNdLhy2di8Is-pEhphy4g4vVGQXNtAmV3A1QFd5YpMLL8GXDzuF3zsuq7jT8Zj7C1zcKWA87ChPAWRIJUmX2CiRSlsjDpkQbT0ZgazVRO4QF6bp_06zo51NhYdU18bWHl81CxRz0ng7A66ujACyD2TD8GzdUXsxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
سبک خاص و جذاب پنالتی گرفتن یاسین بونو که قبلا هم دیده بودیمش؛ پنالتی امروز صبح هلند رو به صورت عادی شیرجه میبست عمرا میگرفتش ولی اینطوری راحت سیوش کرد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24686" target="_blank">📅 18:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24685">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c85d949fba.mp4?token=JkYxwhB-OanxmmAEIh2cec47eTMcra_2_gtdMJp75H8ejHf0j3LMm9vWYrbhE2iLJqmeuJzAFKk5FU40Lqi63N4RrKcQ_-jC_gcyrBRH47s-wq2HqZVdkFxzIPDKQwtBv5vDg2OPq_LEw3nKuYm0gAs_Qni1SXKGlpJO1a8ZyLEapm0luEMPmenHRdAsVRt9NAqx03Ipd-v8AyCBJFdS8GcUi6xtFTQh3QD3kQ0kN8aihqfG2HU4eoQkcIknHdeNOrjXcIZDZts3v985r1i-7WQqZH076pNYLE8SJra5ASDZCaUOdh9jB4JBImsPiiKxzFfml9Uyx3CrdhZS7xq4XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c85d949fba.mp4?token=JkYxwhB-OanxmmAEIh2cec47eTMcra_2_gtdMJp75H8ejHf0j3LMm9vWYrbhE2iLJqmeuJzAFKk5FU40Lqi63N4RrKcQ_-jC_gcyrBRH47s-wq2HqZVdkFxzIPDKQwtBv5vDg2OPq_LEw3nKuYm0gAs_Qni1SXKGlpJO1a8ZyLEapm0luEMPmenHRdAsVRt9NAqx03Ipd-v8AyCBJFdS8GcUi6xtFTQh3QD3kQ0kN8aihqfG2HU4eoQkcIknHdeNOrjXcIZDZts3v985r1i-7WQqZH076pNYLE8SJra5ASDZCaUOdh9jB4JBImsPiiKxzFfml9Uyx3CrdhZS7xq4XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
تیم‌ملی‌آلمان همینجا حذف شد، نه مقابل تیم ملی پاراگوئه؛ اصلا بعداین‌دیگه نتونستن درست بازی کنند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24685" target="_blank">📅 18:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24684">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YidUpWp-tvbH7gw3wuBmJPc0ldS58I33cC-1DDsYryMtOIgFrbOrTEkxuRiClvMjfj3QuTXOwS_c6V8mCfBRhzJ82wfgDNJGiJIxilk8IAJRRMi2n8aFXErROnFsoNutcl4p2GGDmz1AVERk226esy8ix-77p5B5ndNi3CI6PScFXj4YAhMc5M8wfeh3obE0KXnOxUd1gDxdlGHfPXJgR2An44PcfzQ9Dw2WAKXrEEGT7Kc4RvLTDkCwpVFaKSAFv9TCHoQhHryK7YMhBjhdQTCt8AkKHA47uxMYZ5awINEvtAGjafO44RHX-2t5m0dyAHdPSFiYWbQtcs6t9bwmGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
جادوگر تیم ملی غنا: در طالع و سرنوشت کریستیانو رونالدو نوشته‌شده‌که امسال قهرمان جام جهانی 2026 خواهد شد. سخت و دراماتیک است اماپرتعال بشکل باور نکردنی قهرمان خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24684" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24683">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXylgCPKBRYL1UD7Wwv5jaaxYlrxTuWxQc0Xo5jqFoH28j52kOqlMPvK08JS4HrRuiKTMq9aiXQz5YsK99N_uPxZzYc0dwbZJ7yvys7cxOB34_JkO6UuxOa49Hbp-2kvMEIf9fQQfpfAH4VoQKeCO_oRzPhUMMpzEnBVC73Gj5YZT8xyoZBtCEJHhn2oB3e9AouN9cyUC_r0QEaxkVDzKHb84FMqb5VYoDe0bsiwbn5hcbX3Nx51FXdOGwx9cLSn9lqRqk1dPTnrTuTj9lnLRLsWQNBQw4SAF7z1j6alq3MQECMJ4OSI6J-MFkRTXDBz3BEeM33OhJYN72otMHhaKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: باتوجه به علاقه اینترمیلان به نیکو پاز؛ فلورنتینو پرز میخواد او رو با الساندرو باستونی مدافع 27 ساله این باشگاه معاوضه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24683" target="_blank">📅 17:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24682">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9RlFWvgwbaPHLKHwKVE-afV51feOvfIMKCBEPHESwk1Mvmy1K8lqFF9Xd8LhYcJOiOuJ-HHKbzJLq7d6aeF9Yl3qcu112AZBBi7EaAOaeFl3c503dyN8o5Rs2Cu-vc3ICWRgKbg5hJOx70jnRfrJzrZZsXqJLn2F-VR__Sfan3ZSGTXh72rCkyTLiiQnDnG_H8AlxeH_STJG1lCSYbRJvja30_3HAgfMshLd8DSF5Eu_AKvif-8_7B5cGMUo7S7mIqznIulIABgDTyGEdTGT33kwKcHcMbQlU8HdD0rtc-2imd00zIGc6dMMsct5SZt24ioDjeQALo-VbTatfZbsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/24682" target="_blank">📅 17:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24681">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b6727cd80.mp4?token=WrBmwFi7VumAHFCSkQuve9Fr5Yaf7sdNil81hH8vKYeVYdGLtHdSgZCh3jIHEDnS3a-Wg0YZ4docsqYbXVZevoCoFunqw_S9a_VLu41xk52L93SbOApbFe6qdkvEvdGdsSqdRMrwlW43tMkFKyeK1-QJXBcsPfiuWp1lA-mhTSBZ_pYbUoCU3v56a7onaMTBHORZHGEhAQhn_j0NPZj64E_koe3IYTucJw5UkT_ryYgmezDnQh09dfPUM0a_8aovM1d5VTFdkP6YwUczpdlxDqyTMKC5jsAoSmCJliIyWAkO0NA--lDCPnkHFsF-k3264uF35sBc5lQH7kwFXW9Gkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b6727cd80.mp4?token=WrBmwFi7VumAHFCSkQuve9Fr5Yaf7sdNil81hH8vKYeVYdGLtHdSgZCh3jIHEDnS3a-Wg0YZ4docsqYbXVZevoCoFunqw_S9a_VLu41xk52L93SbOApbFe6qdkvEvdGdsSqdRMrwlW43tMkFKyeK1-QJXBcsPfiuWp1lA-mhTSBZ_pYbUoCU3v56a7onaMTBHORZHGEhAQhn_j0NPZj64E_koe3IYTucJw5UkT_ryYgmezDnQh09dfPUM0a_8aovM1d5VTFdkP6YwUczpdlxDqyTMKC5jsAoSmCJliIyWAkO0NA--lDCPnkHFsF-k3264uF35sBc5lQH7kwFXW9Gkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
#تکمیلی؛ بعد از حذف آلمان از جام جهانی؛ مانوئل نویر گلر 40 ساله ژرمن‌ها رسما اعلام کرد که از بازی های ملی خداحافظی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24681" target="_blank">📅 17:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24680">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEXIW_EL0wlXh8xK7eStsT7I9kOnPiwPEAgCiiEMHUUUwTaCbr_GjzBFzYpj5N9NbvO3x6SFKyQbHvpK6qMFgCSWY8_I9-YWGL3Wtv2bYOD2d7nSycgNLTH3Rx_KMsjYy8KkHrurG8la3nEFIua8hD7n2OqoJjpYLzLv-8JZB5MkbEhHhxcjXDQXzyuQxdAUJ7-kUCjsde4Kq6uqo0a7MvReh4n8KS7KRG6g6St1-kMQmb7QfSNZVaUuSOkR6GewClXqdxvM8jz9QtZyi5ZZLwUXLAZNdw9iLh1PLXWUX6ahq-938x7PdTxhP0IVVRaH8m-STb-UrnSPzrP0105HBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مسیر به‌ظاهرآسون تیم‌ملی آرژانتین و لیونل مسی برای رسیدن به فینال جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24680" target="_blank">📅 17:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24679">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L558meqKYbjKzZ1S4569_jMbc3PpMrSxYYAV7doLxSKwr8UwumrcGuh5vIpRN74F5TMhMvUXkQU_sXpjcIuBENsXLsJSS0U_QBc7y_xVYKW7cBTzOWubfArQ_Bp7daLiTsZPlwt8kIf8LozWXKT78b9nf6cetSYrEB_3K_xCoY4ZtRU5m6hmRBNvuHmYhDI8gPuAbcP7Gn9WUMpn2nmP2SLYeM_zh5kRmJAYdAHRdvVJYnrZk68_jPCK6Q6WOqFrp9QNfRkvdsTwabG99mY3rl9LkcZ4wFFKXJfv59OWb_pUal8M3zwqhK9RwOejfBH6ltn6lfOTQxRjAbwomMmzIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تااینجای‌جام‌جهانی 2026؛ خطرناک‌ترین چیز نه پنالتی بوده، نه وار فقط و فقط یه عکس یادگاری!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24679" target="_blank">📅 16:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24678">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9bjaLmQcgQsVnZlCymkvrvtN3efwqCw63kQANMlIa3mPCK_kdQLaNb0d3yOAKR4Xtf9vBLL-8anIGSk7Afle3wbAzwY-XqpN1R__qOWnY1h2d7uomhmd-c5uWkftR2eL48HlJIVUNqtr3ZRs9jFaxsg6bSquIDk6eKTuEHbDF7m_xQGh3nIWXysZYj18eaUS_pciLwqyXgPF7IYQpmNIG1MrEdMV53Ue6WaARRGAzEqzlIaZhrbbkuQqsNDz9z7TfvJkqpkSgw0-hMtaPwtJ5F13ZjobfU3VNzix48VpkWR9sf_dNWfkAHSF3xN-vviFJ83V-PHYtURdxQ46K_gPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24678" target="_blank">📅 16:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24677">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYjNmB2lRJIs67EDd1LKSmT9m7eeXl2YRtYDCFfcKZjiXdk5nR-mhcu7uxCGjx3vFtKoWsRykXRnj-O2B-a9aXbPNWu4EzC5Nw9ktOPRAwn1yNK8DEdugKgT8evd6-nGDjighIeuejBni_c4OfEVm3sdsfaAODnnZ8fhGxmMQk0e_Rskc95qKhSvlOAWruQIuaM4ZzXTtrWvgACnTWE2NYPjx6d1jr-uUUgobbJkLfENid3NtZsWMn-4NqVlfz_ylZ9hWZRFrAUUpO58dovdtPkd1t4WschQTzOODsBza5w8gh9OlzceI3ddF1MoUjPDQuivZ3yTjkGfkWbEfxmYbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
شش بازی بین آمریکای جنوبی و اروپا در جام جهانی 2026: 5 برد یا صعود تیمهای آمریکای جنوبی. 1برد تیمهای اروپایی. فوتبال اروپا این دوره بد ریده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/24677" target="_blank">📅 15:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24676">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJ5jKngQNOBYRZlVwKHzkKG6edYmykq1tAirfTVKCe7dHJkD7K0JnZHnKPBSi0QMuPuVJP0Gp5C-umystGdPcA8VY54ZGaICXK7z7sXubtk-swNt35Niz-QFtBWeiJ-8ZoZMwmq-s3z9ArENj9sRzPlpKieDncdWBrdjmtaLeIKnBEXktyh9SgckONhg6Fu-I3kEINHrHkAXnGLVFtcBGgl_33vK3S21jerW88IAuTUdNcnJiXI2f_Mk7d1aQlffDHPP5Bw48Hk5mSt1pL7aJovTYnwNcI9xd97D-MtPDFyBANessK1tYOnHZyLXkInIWd-Yhlgt-wnJMk_3gVABWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛باشگاه تراکتور به‌ سید حسین حسینی اعلام کرده مدیر برنامه هایش روتغییر بدهد با او قراردادی 3 ساله امضا خواهد کرد. پرشورها قصد دارند در صورتیکه علیرضا بیرانوند در این تیم نماند با گلر سابق استقلال قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/24676" target="_blank">📅 15:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24675">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cA2iE4rU2sgw7iusHhwkmjDgw81JhWMdYGhWGe4OI0HFfnI8uyH6kLF6GL035NJeyqe-GoomPR7AhLfM2wWYChZDjli2JEZNoOMpmeHovPpoVoHxzgbxUrnIIP3bBUazc9u1erMHsy_jkv7ZsyYUn3SyavZkHW93i1FGWiQoUCYE8htJYgojSvMcHBU2TqPrqZ96MXW77NjwCjDw3f03GJiR5voSSBlYcJMPcrrjyKkEZEoB5PGs7EwObGr1DXieWTRQPMUGrv7-UKZO2PSzUaOU3ReqzXqAqqtxEwOAh1tDMlastbaIbgDx2YPSJYwlcYvJk9CsKWdMXEd0kNbSeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24675" target="_blank">📅 14:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24674">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nW8pa1kK2eFcuRRA1WSMNFeGVjHWHdAU0oHZUMeK9EDcgvuBgR5-8oSjeuyI6AC6N_D5AEQtDrK0ibRRvVKZAV6-vcqnPf3TTJoCIUUZ1W8Mvks-fptDl28dqeeDFuU6SC1nY9BTv7DfYZhpGBA4dHGMkrataBzlbY9PDJS7iU2V_DGD-NOlbSNllcJkTJRcPhMb94VQs3EVxxHyKhWG9Df9D-s_6HKcsuZWQ7J4Miuenbo2pSlw4sCU7-bH_ABAL6CLjo-hCtT6S6EWD05sXLSdw8obvDkgLqpz8UL4fE5AKDtrtxEy9mXrgrShCmLU8SZSCfCTev_VUofsCaIduw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه تراکتور در روزهای گذشته علاوه بر تمدید قرار داد دانیال اسماعیلی‌ فر؛ قرارداد خلیل زاده به مدت یک‌ فصل و قرار داد محمد نادری رو به مدت دو فصل با پرشورها تمدید کرده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24674" target="_blank">📅 14:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24673">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlWrMaBoy8URmNVFt8WyzMiFW0z_ZNSRgTnQ5JMaP5G7w-xrB1aeXrUnNvSn-rrOaS-KFbSyxWD-XjErJPKSqWMxgqHHCTegpuYnBI_Z4SSZPD3bOtvGmzthyGLogucRUBmc2oxYCLpTQ4CgNj0r5cRvOEwmYGs4WeYfQbZT6TJM-vuXXop0RRoqscU5tiyNhXQwxGJQhvjbWdyp-hpo7a_XNubiwpH80SfD8ADSdzzROdQM7_lA9Xbp7VHJhOAmMMGNwDraxYR4Ias6Ikm29FOk6bzaKTJqGh9eQMvN6OJZcPvl3hRxTdpL57eJyVpzi4qiwExNJv_kloztOZNNVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌استقلال باید مبلغ 150 هزار دلار نیز به حساب جوئل کوجو بابت فسخ قراردادش واریز کنه تا پرونده این بازیکن به فیفا کشیده نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24673" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24672">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82624c7740.mp4?token=KoDcOGfpLXXeI9Q_XW1gMbDTY8wQk95v_d5PTVtvbpywJnOoU9FZrsBWXtvm2j8enqVyYxMXgmL-VBp0CKM4n6wiq-qZXjkTA9cEFcmkO30xed8jXY5mivRnn5MaBQovd5oLZlN38TfinM56_leht6WCQwviPJvm8sqSn9d6bawew5jfiERMFjeCXpeyPg3uIbDf8E_IEaN6WUC-_ZhHJq_uMhh7oSPBEeGNLpOGrBTTAAUPN8I4_L0_2dcjr5MT_ywa21buab4Q6MZAo8i85m6UveZUFhlPAeBM8ZjgKtIU0S-cd8kGsCb3IPZ7LDrhwEhcxCywKguTQbe20bcObA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82624c7740.mp4?token=KoDcOGfpLXXeI9Q_XW1gMbDTY8wQk95v_d5PTVtvbpywJnOoU9FZrsBWXtvm2j8enqVyYxMXgmL-VBp0CKM4n6wiq-qZXjkTA9cEFcmkO30xed8jXY5mivRnn5MaBQovd5oLZlN38TfinM56_leht6WCQwviPJvm8sqSn9d6bawew5jfiERMFjeCXpeyPg3uIbDf8E_IEaN6WUC-_ZhHJq_uMhh7oSPBEeGNLpOGrBTTAAUPN8I4_L0_2dcjr5MT_ywa21buab4Q6MZAo8i85m6UveZUFhlPAeBM8ZjgKtIU0S-cd8kGsCb3IPZ7LDrhwEhcxCywKguTQbe20bcObA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
میثاقی ژاپنی که بعنوان بهترین تیم اسیا اونم نه مقابل هرتیمی مثل‌نیوزیلند و مصر، بلکه مقابل برزیل پرافتخار ترین تیم جام‌ جهانی حذف شد رو مسخره میکنه؛ جوری میگه منتظر 2050 باشین اینا میخوان قهرمان‌جهان‌بشن انگارخودمون‌خیلی‌وضعمون خوبه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24672" target="_blank">📅 13:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24671">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ie4EvrSy3bmUxd4eQvTiJqhScfKs4Xk8iXknRHhyv8TkUtqsT3tMjxIgSMnyN_B6-FM_pX8GN_fP_06wFXGHaTPWU32dlr8e45ISc7p7EDuLsLKeiiZFhwBEjyLCoYzgBFOUT3CaaQwXa3diLXRFdFobnwVcLe1cu0siN9hRrs1nRdGmsxppH1F28X4zsd3ZQ1z7ZDhvKEIwSI1zBxiup9VEUgL2pvXtkAMdJyAj2lm4kYbGCOGHyr0FU_LF0NH_voYhbQ4dMFsXrn-qtwaHLpSRtR15_1aEtBhFM-jGH4XytUUCMNni-XRy6hOcb8Xo1QdphlxViA5trf1sO6cNjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنهابازی‌مهم‌امروز؛ گذر شاگردان آنجلوتی از سد سامورایی‌ها با گل نجات‌بخش مارتینلی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24671" target="_blank">📅 13:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24670">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjX8PFJpXRI0sxqwXZfK7PVFSC6GueDD7jpbLpnolJS-5Hgny26UTaPvsUAMl9slSri2YpV8I_8A5ZQwwpTYEGpQyy1M7Nx_o637THfnGeuMHdy1HeQQYiSxTcb9DMlK9NgnnbuUwEMa9cYRywQZpNCc7O3oiugWKlji9skaP214A0_Mt0CO6Z_mHOOD5BBYfe4dX7vIc83w9e_thKGJFx0NxAGCpz6YUWUQiGjEuNTpDHX0fslQTqNWBETkEfrwx8kMobbwVkrb0NurdB36pP5ITt66VPotFxKf8uiTEpaWegHt0G4dkQvmDHfX584ztwiZip73rawFlXvJjlukRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24670" target="_blank">📅 12:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24669">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68e8477068.mp4?token=q8AKHdMx98VWFKvh_7Bn1ke1957BTDlcoO-3iO5gfsii0su9uFqKB0bhD9BUxTiNaWB17ArwTXxZZFuqnt9EWkNc9zT2qEjM4fHTo7s1yA7FuypY_IHqIodPdVJ7ASdGC8t6o_8lqX3h2TOJfJ0s-w0hRgh_YhFwlxN7ulKOOoq7b-OLH_Hu6-0oZAC4Pfsj1LndGZKKZvr9jpMzjFfM80H_p4JtgWUbQUN6tGZ0liA3r9iaL5gZOnL2cWlwo9MQPpKYmgVlT7lJmZGK2xo3OcjPM7Ly3qMIp1apHJKzu_CRqkH0nzmz3oOpnrLci3kYLYK9IHkehLuK2j9WUNvirw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68e8477068.mp4?token=q8AKHdMx98VWFKvh_7Bn1ke1957BTDlcoO-3iO5gfsii0su9uFqKB0bhD9BUxTiNaWB17ArwTXxZZFuqnt9EWkNc9zT2qEjM4fHTo7s1yA7FuypY_IHqIodPdVJ7ASdGC8t6o_8lqX3h2TOJfJ0s-w0hRgh_YhFwlxN7ulKOOoq7b-OLH_Hu6-0oZAC4Pfsj1LndGZKKZvr9jpMzjFfM80H_p4JtgWUbQUN6tGZ0liA3r9iaL5gZOnL2cWlwo9MQPpKYmgVlT7lJmZGK2xo3OcjPM7Ly3qMIp1apHJKzu_CRqkH0nzmz3oOpnrLci3kYLYK9IHkehLuK2j9WUNvirw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
یان سومر دروازه‌بان37ساله سوئیسی‌ تیم اینتر میلان بعد از چند فصل حضور در این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24669" target="_blank">📅 12:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24668">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786ffe7041.mp4?token=gm3miFVNRp0STQGqw7Fsjtf_ZoLOT8fX0GU9rlQ8qN2HepjXjQCX7ryzjPK2fWl9gVKb81UmKnL2xWnRHPqZ6q0G_J9HfMoL978m_5WCYDwTEUf4WEz1ulTI-rraG2N3HBQQ0qbK4KiXYhf5Y9JhccUPfUDe9SGzTaBVqDnXlKXTE5BV8zjsomx-1L7jO_vVFhiIQFkC7VS53uk1pK4vIMCTZmdEDcVgEGr7vUQ3nOJJXB-HB6w51WjfG6H_NfH1s7ve4ltDR9EX8WIWNpCvoxlbqr3Znj1a3lrquC6uqwXcf-KYgbLIJn6IiOSe24vPpx2OLE1M4R5Z4eBR3gKysA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786ffe7041.mp4?token=gm3miFVNRp0STQGqw7Fsjtf_ZoLOT8fX0GU9rlQ8qN2HepjXjQCX7ryzjPK2fWl9gVKb81UmKnL2xWnRHPqZ6q0G_J9HfMoL978m_5WCYDwTEUf4WEz1ulTI-rraG2N3HBQQ0qbK4KiXYhf5Y9JhccUPfUDe9SGzTaBVqDnXlKXTE5BV8zjsomx-1L7jO_vVFhiIQFkC7VS53uk1pK4vIMCTZmdEDcVgEGr7vUQ3nOJJXB-HB6w51WjfG6H_NfH1s7ve4ltDR9EX8WIWNpCvoxlbqr3Znj1a3lrquC6uqwXcf-KYgbLIJn6IiOSe24vPpx2OLE1M4R5Z4eBR3gKysA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی درگفتگو با ESPN گفته شک ندارم که آرژانتین باتموم‌ ستاره‌هاش مقابل کیپ ورد غافل‌گیرمیشه و خیلی‌زود از جام 2026 کنار میره!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24668" target="_blank">📅 11:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24667">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d5676f715.mp4?token=fNcIxOEmaKuaP9g12JxfAqzDEyOHyfY1eoXVTdQedRbpSxLDwUDN3P1HMRdG_oMKz4NXlQYC3h5LPoAusz3FZE-b1hcNBXhfZbHzhYzlwA6PPqagNAQU3HAcPOEeIML1iLA49F42TE6RfmzpG_FntWvLsoJbsK9eNiHbTW5YqlcxUpQE18a7xRKEr2Hz8OLqMHahAJV95Fz2PqKu_ciMbDBOGGafiejySqjB3N-D7ou6_1s8Ii2wKUCws79wUaIgKe3RujzJDBmC6pICTB3Cj3o_-jHcVmM7uXmSKVviMqRI0vvTiI8TSPsN9GBvXqbeKaFrcZChcOEOCtiNdf9ObQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d5676f715.mp4?token=fNcIxOEmaKuaP9g12JxfAqzDEyOHyfY1eoXVTdQedRbpSxLDwUDN3P1HMRdG_oMKz4NXlQYC3h5LPoAusz3FZE-b1hcNBXhfZbHzhYzlwA6PPqagNAQU3HAcPOEeIML1iLA49F42TE6RfmzpG_FntWvLsoJbsK9eNiHbTW5YqlcxUpQE18a7xRKEr2Hz8OLqMHahAJV95Fz2PqKu_ciMbDBOGGafiejySqjB3N-D7ou6_1s8Ii2wKUCws79wUaIgKe3RujzJDBmC6pICTB3Cj3o_-jHcVmM7uXmSKVviMqRI0vvTiI8TSPsN9GBvXqbeKaFrcZChcOEOCtiNdf9ObQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداگذاری‌باورنکردنی جوادخیابانی مجری ویژه برنامه جام جهانی روی آرناتوویچ و خداداد عزیزی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24667" target="_blank">📅 11:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24666">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgTxB_4vAak--25-2rhxDYtl18yjZKNRoq-b7LA5bJwkKuQym6knMZIRm6EaLYrMSehDQYoY1pQsTeNgxWdC68jtkDtKppX1Esmm5jEShFK921NVZRGk04CUu2s8Jlue7ox31h2QzpiaJFyoeEHHxqTwQvBTLKxbzRG1wjGSEDrDPqEc-vbXZLWVB2pz25l1XMma68vNi_x6SFYoWOemjGTSN54HyoiZXdgEH1EOXyVu2DHc2M6Na5PMbrTke4TtNYylNnrEzpHzqIhj8utmbd1l50Tf5h0eqdcRT7Tebd_66ikuKcUqNnlbBBHPfIPoYu0AdSmcptYh9xOdiaFSgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه‌پرشیانا؛
به احتمال فراوان باشگاه استاندارد لیژ قرارداد دنیس اکرت مهاجم 28 ساله خود را فسخ خواهد کرد و این مهاجم ایرانی الاصل احتمالا به لیگ برتر ایران خواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24666" target="_blank">📅 11:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24665">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LIv78ZIVbhuouQXa1fV4-ZYgFh1Wg0XVO1vgiDUFtQSR3MBoW3IiFP7e1RLRplBHXskMhFeFt8GVPX7FtqCAwwUidbFWjI1mFDMQIq7WlD0iSBp5DRYsplyZGHPvDM4l2fo2BwicaMv5qdBfEhlymkaIm6SR0otUqHQ1Tr49LrZdpUf77yGt9bQ493Ix3SH1ARGpVFDkxiO6QLGiP5974oxfeMMvf5yPe8uXRT3-DEf_7LKZ_5F1b7uE0QXhoBAFjORq6U3SMNJraskmWSvm4q7GKCPI1DFxlQaIy06-d07gKgEIWcbO6gkhsbJftYpQLRKmZIuVEjOujCOvXY-VDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی 2026؛ صعود ارزشمند و شیرین کانادا به یک‌هشتم نهایی رقابت‌ها باپیروزی دیر هنگام و سخت مقابل آفریقای جنوبی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24665" target="_blank">📅 11:02 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
