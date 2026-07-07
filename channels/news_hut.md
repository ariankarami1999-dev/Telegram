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
<img src="https://cdn4.telesco.pe/file/JkcmrJKE4WdavYJdmHBxrv6Bp0Ih1wPm_zhMBBiRFxmXFdPqKrI9Hs0LCRTbuq8jmWGp22wmfaoB3QSUCokxRQ07kOUj-ewfSbbRmZsDtXP6cX3ZPndaEVi3mPtQ2XCPq5AXkNs7uewLNks24EURkn-RKCAmVHsbaxrkp52rAQqFyZeyI-WXCASKY5_pR8nTMfK86EAWJM6ROudzAKsJbDONWA8CVQ_N0GEF_S4x-iMUEzMSgfjhBT0FO7rsKRfYXtcxYqh9CCHPAw2i9cax9DT-HpWaLWevug27rAtM_IeKlzX042F87o2dKfrZlkTmbsm1GEl7YxRJKGEpGif-rw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 198K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 07:59:57</div>
<hr>

<div class="tg-post" id="msg-67406">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/news_hut/67406" target="_blank">📅 03:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67404">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cBtE8Oq7qdCNA_z8-N74SdgSUpYRZaWHJ9U89xZhuS2Qn-J8KLKKiF6sXB387TtRi9no_g-rLioy5yHRlgEWd3jeQPEDL0jgYW5CqF4sgP82OFkTPVRhM826m-KAZmbIRW2ZKoI2Tc-rcsy5CAkGehLi8aMiiRN5vSAg3dmKxwlHLzmcifLHoLIzslUVGMSmwBqV7QFJ-onD_tFvfUtyTl8b9N5ZVp6vaYuVX8dy9h-paasujLfrclUyzCpahmz2EwlHti9zntRha2ATLMACUcm414eiP_iyvwpd4lwNprss1Bwsc7Afh-EOE1kdxYz1_6-dh87x8fllmc75hkcfFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/67404" target="_blank">📅 01:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67403">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmeGBYTX-1t_vob9flAPg1dBIEIxR5Wncg1UU5XfqBgXKr6CE9Y4NpCX88a0aKpIdf_52PO45-w1uPTkw5VxuilUXpwyDy72Tjg_1ZuOYbqE-XRv6M9iwjBekDa3U3exwdCfYyqsjz21yPcV6DkQJQmohrkF51N0_xmhzGyV_KyEBWc7jPX7YxUoOVDw7uQznYlZtyWBUWOWddt16JulzHVVdWLL62B7NU60LVFjNeZnhkrp4tu86KjeX7PccXP-R7fNlOw7AzqaxpO3oKQ6mrlhzKSrBW6MTwQM6SIDU7aZoLdyd40fVbrJ2RXOE8h98Ros2uHiMUtdP8-6OouSLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی 2026
| حذف کریستیانو رونالدو و یاران با شکست مقابل اسپانیا در دقایق پایانی
💔
🇵🇹
پرتغال 0-1 اسپانیا
🇪🇸
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/67403" target="_blank">📅 00:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67402">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9EPOMo_EwGK5TWXy-w27uzWFe30iPPNfNcZmXyKj7oWeXNgMaTfH1i2faLYmketlENwqqYYsPzpFfQOrutPzZhxTnWwRnU8zNeDWyZl1Vk7mTbeivjxelxmytsZFjAxZhzLNwXQX0VK9PZ3VX_4F35GuJdCDHcc5ePoJDBeUreNNqM5BWLgPpxiMNMANnZMNy02pxlAic90AgYlMo946Sol-qHfOWcbo98VlDkiv-hMBg9IlRzd7ZG4CO43BhcK4bWIatHeDUq_4FET2l94bDF9aBvZ1c8QqrEtlnNKMX9lQFEMsGrGs-j-txxdIQ5R4QOLOD3LrXdTHWA1f9fH8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ادعای کانال 14 اسرائیل:مجتبی خامنه‌ای در مراسم پدرش حاضر بوده.
🔴
حضور مجتبی در مراسم تشییع تأیید شد
🔴
مأموران اطلاعاتی خارجی، مجتبی خامنه‌ای را در جریان مراسم تشییع امروز در نزدیکی میدان آزادی شناسایی کردند.
🔴
گزارش‌ها حاکی از آن است که وی با پنهان شدن در میان گروهی از دانش‌آموزانِ حاضر در جمعیت، تلاش کرد از ردیابی بیومتریک بگریزد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67402" target="_blank">📅 00:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67401">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/781360aa4f.mp4?token=gv7vtphSTaY52hmHj5eFLxwd5MwEwdaBvoiq38fxkdmzB4LG5URQpHGo4x5qJH-butoo_MTM30QwyaFNryf55-2H7Ifi6XPxtc5-_WyPtTFIuajXIrNpc1YCxQthYiugBTmNxtrbw7xdeXfjgACJAiZH5BF3lH2Ef5oWIr6qPySaZhS40T-z8jOLBcQMK9qN_TAXSz8cFCp8xtYwBDSUpZCvH8nTJahvAfXnR8jSVaDju3Z6YW1tIxOG-KCZLiD6gdlbrD8xLE1o9ixaWKlxomRUUWFk9Ovm1siHGXdVY8VF80AxqlbEGwQsLeB4huSBplORKDqN_UGBD5YMco8Tjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/781360aa4f.mp4?token=gv7vtphSTaY52hmHj5eFLxwd5MwEwdaBvoiq38fxkdmzB4LG5URQpHGo4x5qJH-butoo_MTM30QwyaFNryf55-2H7Ifi6XPxtc5-_WyPtTFIuajXIrNpc1YCxQthYiugBTmNxtrbw7xdeXfjgACJAiZH5BF3lH2Ef5oWIr6qPySaZhS40T-z8jOLBcQMK9qN_TAXSz8cFCp8xtYwBDSUpZCvH8nTJahvAfXnR8jSVaDju3Z6YW1tIxOG-KCZLiD6gdlbrD8xLE1o9ixaWKlxomRUUWFk9Ovm1siHGXdVY8VF80AxqlbEGwQsLeB4huSBplORKDqN_UGBD5YMco8Tjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعارها برعلیه پزشکیان
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/67401" target="_blank">📅 00:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67400">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتلوبیون اسپرت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GT0SrnmGJJrvFyDQk04ksgojZ-BWkm1irBlfzd3gzz5vbtOPkpxo8i6ZeZ0dHaQSpxJILhTl4KpEtMdY-ftcpL6c1YtAOslnx_7UEvWKhYokxiXitCmkpPeVRxFSCJ0M8MB3XCRNZBx2KRInKtgDxgifVRBtN193l6abmgSACLxIODzUuaSNqTr9iCrkh7EgHETQzfEe9Ap2-EKTK1j-sfRw3rngsB_syO2JUd-gopaXjMqaVXELLYOnv31xjgT7DVynTNcTjDiaH9gF5-W-GpfvoCaiW85tAdso59mtFP71ELXze7nWFnw21QSN6sJJmPtNnvj2T7TIS-WHMhfQRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
اسپانیا یا پرتغال؟ انتخاب با توئه؛ تا از رقیب عقب نیافتادی از تیمت حمایت کن و پلی‌استیشن ببر!
🏆
👇
👇
👇
👇
🔗
همین حالا حمایتت رو از رونالدو یا یامال در لینک زیر اعلام کن و با بازی کردن پلی استیشن برنده شو!
👉
Https://tcup26.com
👉
Https://tcup26.com
📢
این پیام رو برای دوستات بفرست و به این چالش بزرگ دعوتشون کن!
🤩
@telewebionsport</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/67400" target="_blank">📅 00:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67399">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/733e727650.mp4?token=crH_ZBmmMjbHk6ZeCPhCAVAj0P3giHM01Y2jQnF6xWYi8CDvBhFBYBDgR-bOuEUTsg0u2Al9JEkweu58QD-mUsN2xjOB6gHoneZfrMzySJcUYgT-UWWx8YWNsceNBdk-MfHpMum003qDqaxhso9vahPkISSmdEzz99bk736ect0cCpPsSW-uCZjLNlrfOESbkbrVL7KHhz9eG-NJGOup7my2J0ppm9SMI94ry2oe8pYZaUqAkmF1VWvJbUbJXNJPq1EpZ7adXY17ID4mdNneA68JdFGnep0IM_GVJTF9P2JGbAS2mv2cY_FhSK-IR6-elSmy7zHKF4eqbCUi_EvXEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/733e727650.mp4?token=crH_ZBmmMjbHk6ZeCPhCAVAj0P3giHM01Y2jQnF6xWYi8CDvBhFBYBDgR-bOuEUTsg0u2Al9JEkweu58QD-mUsN2xjOB6gHoneZfrMzySJcUYgT-UWWx8YWNsceNBdk-MfHpMum003qDqaxhso9vahPkISSmdEzz99bk736ect0cCpPsSW-uCZjLNlrfOESbkbrVL7KHhz9eG-NJGOup7my2J0ppm9SMI94ry2oe8pYZaUqAkmF1VWvJbUbJXNJPq1EpZ7adXY17ID4mdNneA68JdFGnep0IM_GVJTF9P2JGbAS2mv2cY_FhSK-IR6-elSmy7zHKF4eqbCUi_EvXEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
عجیب‌ترین چیزی که امروز میتونید ببینید:
نیسانی که با یک چرخ جلو بدون مشکل داره حرکت می‌کنه و سگی که داره راننده رو قانع می‌کنه تا دست از رفتار‌های کصخلانه خودش برداره
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67399" target="_blank">📅 23:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67398">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aad6611348.mp4?token=Jdgotm308lj4ID9_cegzyhOhu0DVrefvROUXOI9edm2mZeN4QRcsTp6CiZKoM5Nt6uVL-hRw6Eu55yfXYgCziBQMWhhcTq8oDHkD30ELYEhpb2UEW5NdfiJqviZq921Hx6zGsfrdbF-4j4wtSzZDLw5wv-staOz3tNR5hKhfDQTsP67Euq-u2Xh94GFp7DbzSBs-vhIRPksAecCzscq8qk_jYyL1X2WXwKw-XsrRnJmmoElYgidR2bClIllCI5uAjAdfphmI7p3DqZX1iVK2m2DuVKNeGhEGh5zjRlTxhStwrKO_0UH5bZgrjUV7q9AXtro0X_RS8_xk2qdcpKIGJjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aad6611348.mp4?token=Jdgotm308lj4ID9_cegzyhOhu0DVrefvROUXOI9edm2mZeN4QRcsTp6CiZKoM5Nt6uVL-hRw6Eu55yfXYgCziBQMWhhcTq8oDHkD30ELYEhpb2UEW5NdfiJqviZq921Hx6zGsfrdbF-4j4wtSzZDLw5wv-staOz3tNR5hKhfDQTsP67Euq-u2Xh94GFp7DbzSBs-vhIRPksAecCzscq8qk_jYyL1X2WXwKw-XsrRnJmmoElYgidR2bClIllCI5uAjAdfphmI7p3DqZX1iVK2m2DuVKNeGhEGh5zjRlTxhStwrKO_0UH5bZgrjUV7q9AXtro0X_RS8_xk2qdcpKIGJjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فحاشی وحید خزایی به خامنه ای
رادان کلاهتو بزار بالاتر!
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67398" target="_blank">📅 22:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67395">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sSY-X2EF8UTgN2_qkAK5hkqTY1VT82FDalU-AxPj5CKPQ95ZqDw85BKrx_brpZgfr7s0moL3kzDKI-ZNYcXloSdit3RvOnin_epxTEhWeJUiTPf2rjXk0OTqcTRNunEAQts2ubQHGiz3DKYPG1qQPMzVaJhECCX4NwKCAX17hY4Mh1Dh7bygAnBJjeR-hQ_u09wBz0UdIZW3HLCrQkoZm3-feJxMRodpePw6pBbV2zwzTy5EN7SQ9yc36JWZMhx_e0bOlt0HkJk8PFKIixa7fvoG6y8smoCCVmhyp0qzCk4ANEntk01TgOqK-6IbLeorO8uBChJEIENZSC-fQSz8Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DkvG6CuaqMHkUuzoApGzAhyZe0ehRo-rJRT4lu59bjh-7IOG5aK2LzRlo0GZp0dWLwFtzEjNR7Oh4DHZ5v2ga8gJeY3GmusHjdbut81O6UfJGUlXOfR6Rb4gkAcHLcMxK06mzh3RjQYbDkrDWZfE_5z5ZQtx9VmZ4TcCRVBwYi9I8lp-BY1CZNO2mVlvtGYETtlh6hsoxebZ5X64D8p0cF74HIR0qSx71qImMQUlvndPbyLl9fkP7ixn2K2LLBKBT7NvShX-UXw1SGUVHtV5eGjy4XKSWqiKNiW_W2pAzJ-l-j-2vXtiGrkmnNP5xtj1fOopbD3Rbhs4lvZ-9LawUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/886967cfe3.mp4?token=HKYqC08KFpd6BiaF__GgTOZ8KbQR-6QVOB-7d11QJZjZVTowNYHFP9TP5jDsiobF_z-3_cT0RgFnlYB64dOaGqrTU2JzcDx1sAE9-iPcJuyBuEDjO653HMstyvji3Yv6VUjeCKVeb-Xphs4n44V4oNeogq6uojSe0QjR1kmsP0RaiJBRh1fKtLgWeGlRXonHdC1HyKpKur-81JgucINBxAIsXZSh5dPUAKmaYn83bpmFj-1TsoEyuFNXGkmiEjg4x8n6cIAyYKMtLw2zkulTUqFoWP_5vCx03KWHFgxAluTJYmtiNK21pBEjravXDTzp4ia9v_sk5bJlxvoGzRHmcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/886967cfe3.mp4?token=HKYqC08KFpd6BiaF__GgTOZ8KbQR-6QVOB-7d11QJZjZVTowNYHFP9TP5jDsiobF_z-3_cT0RgFnlYB64dOaGqrTU2JzcDx1sAE9-iPcJuyBuEDjO653HMstyvji3Yv6VUjeCKVeb-Xphs4n44V4oNeogq6uojSe0QjR1kmsP0RaiJBRh1fKtLgWeGlRXonHdC1HyKpKur-81JgucINBxAIsXZSh5dPUAKmaYn83bpmFj-1TsoEyuFNXGkmiEjg4x8n6cIAyYKMtLw2zkulTUqFoWP_5vCx03KWHFgxAluTJYmtiNK21pBEjravXDTzp4ia9v_sk5bJlxvoGzRHmcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فیلم اول تصویر کوچکی از جمعیت یک میلیون و هفتصدهزار حجاج است که امسال برای حج به مکه رفته بودند
مقایسه کنید با:
🔴
فیلم دوم جمعیتی که روز شنبه ۱۳ تیرماه، با وجود واردات عوامل جیره‌خور نظام از ده‌ها کشور در مصلی جمع کرده‌اند
آن هم در تهران با جمعیت ۱۵ میلیون نفری!
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67395" target="_blank">📅 21:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67394">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1d208e49.mp4?token=cp1KQvesViQCLMXLLWAcoxleH0MWuYBIhp_3_gmWSUi5r_drGhdcWBjV0Q-qE-xNXwqNqJzC_DJKPhCW3BwAhtXBCFaTB1pygSjJWzOltnM8VnF-jcVERT6YZ1SIcJvv5kbcOOWDZceBlwQW98bocFL2o22hPmD9MmbkhJByS9lS0kIESOa8jqktmOWXjPx-pMMwQ4W4ZiiHVQxHJ3Ey4-K1mOlOPvqJbTXeNJopdOX3zyNBGxIlRlypHCgaVS40wumSJS2L-ykUJG5EGAyZSaG0OjpVnpAu1SMBXtXo2vvEblpL6vPBPMzJpixA324usA-3NFMCzRervjsSR0rcxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1d208e49.mp4?token=cp1KQvesViQCLMXLLWAcoxleH0MWuYBIhp_3_gmWSUi5r_drGhdcWBjV0Q-qE-xNXwqNqJzC_DJKPhCW3BwAhtXBCFaTB1pygSjJWzOltnM8VnF-jcVERT6YZ1SIcJvv5kbcOOWDZceBlwQW98bocFL2o22hPmD9MmbkhJByS9lS0kIESOa8jqktmOWXjPx-pMMwQ4W4ZiiHVQxHJ3Ey4-K1mOlOPvqJbTXeNJopdOX3zyNBGxIlRlypHCgaVS40wumSJS2L-ykUJG5EGAyZSaG0OjpVnpAu1SMBXtXo2vvEblpL6vPBPMzJpixA324usA-3NFMCzRervjsSR0rcxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره مقامات تهران:
ما بسیار خوب پیش می‌رویم.
می‌شنوم آنها میگویند که«بسیار خوب پیش می‌روند.» آن‌ها اصلاً خوب پیش نمی‌روند.
آن‌ها آن‌قدر شدیداً می‌خواهند که یک توافق انجام دهند. آن‌ها باید توافق درست را انجام دهند.
آن‌ها با بسیاری از چیزهایی که بسیاری از افراد گفتند با آن‌ها توافق نخواهند کرد، توافق کرده‌اند.
ما به یک روش یا روش دیگر پیروز می‌شویم: روش مهربانانه یا روش غیرمهربانانه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67394" target="_blank">📅 20:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67393">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e3a38b86.mp4?token=pzxj6cPgT2GTuQiy-cF7gTrZqFwcgf_JpaaQ1QyU5KvDSPFxHj_PhIGgrxTGU8GcZSBlfop3Xi9EyI21AxfSWXbZWmJBJCPg197pzl2443l5Oy6rGG8Lbv5-VCMpMTZTBVx69QJ09G0kymKneY1_ZcqZ0bnDKl_QzhbbgEaS6sAAqsBQ_b50cm6GnowNAQLKmtxWG_tycmktLnivQZlIVhEDZ54bgE_xdJiOmQ37-63-0JF2KmlAHzmGxo1Qi_hPeFTK_ubwexKm0GfeeHZ5eyExgGBmmw0wmW1Snorh1SgVmaeQnRPRZa8G_5ofBVPxGZLE0nXfGzf8WlNucyNWbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e3a38b86.mp4?token=pzxj6cPgT2GTuQiy-cF7gTrZqFwcgf_JpaaQ1QyU5KvDSPFxHj_PhIGgrxTGU8GcZSBlfop3Xi9EyI21AxfSWXbZWmJBJCPg197pzl2443l5Oy6rGG8Lbv5-VCMpMTZTBVx69QJ09G0kymKneY1_ZcqZ0bnDKl_QzhbbgEaS6sAAqsBQ_b50cm6GnowNAQLKmtxWG_tycmktLnivQZlIVhEDZ54bgE_xdJiOmQ37-63-0JF2KmlAHzmGxo1Qi_hPeFTK_ubwexKm0GfeeHZ5eyExgGBmmw0wmW1Snorh1SgVmaeQnRPRZa8G_5ofBVPxGZLE0nXfGzf8WlNucyNWbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سطح عقل عرزشی رو ببین
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67393" target="_blank">📅 20:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67390">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QL0_JW9igrdy62CoMf5qgwoZwos7uiOE7waADHhyAoF-8_LhlysGAEpnxL57YKxpbfuoSYkFUDGuJp_6fu_TYss1CEB7DYkQMy1KoDa8ExK2ruIdAmTUCDlTZQQOgoCvWcw4ys7HzL7FAnceNVtthOfuYcIPMQD9HoKv35IoNEnYSENnKfsUzt0IhG1NW_-2besoe6vR5GMKLk6E5Bah5neOxXVhfHMuox9XJqO3OuCVpdJmXDVtqNCyK2NzJr_3qQheArKDi21R7KcNfUe04QRO5zzdaEvMyEsKTQjbvpPOmznOy-8geMWFIpxxck36rvut8gy236KQaNQg5apYQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GhX6TvNKLyvH68G6xCUJKV8wslMf2C9eDldLCg1EzNM7p7zPpS6Bv8Ynk6enW_mIVBqvqMfOVNduH1QS-byDUh4c05kQ9Xzn1SjK3hoES6Fshw7Bj3sJ4yQvoMttEbsjWI2KqoRfXoyCMcNBolFqf2cRWStLV0Y6-8junPQqF93tCS9t8JEMqcgqDKYVh-b-iIQ-lNDcF4bE5x3KzTElpq8pUrkyva5gT0DFF2K_tOHC15pM2PDnwf7wF8cHbd2TCmSjiOVmagF9mF0wBeEBQXqFDZNdhOUeo2Bqlgn2EPyMD5xS6yGeTYHtuq2mUhJuPedXrW5k33rFHraRbz-MCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bea0c04d9.mp4?token=fyyacducrAVsvgaBoqBJRUBqqv4oA5mF1goYXd42SCcKo8tSoQ5QOINjXEtFYPD-4B2D6Pc2aDNMp8cPFXxtjuuiHAQSQ9WSrGQhdltw5sRN6KsyzZdyskCTvTnsuAlR1T7pZVwS91cogYaQUgY8oUBRqbM9_KE9fHm_c2H0RSBMSgWK32BeJTvgsK5NmAZoZwhazU3moL-DEN_lXETl6TvaADIF_PmSIM4X0MF5eIO9e02deBvF7q3BixW7VtEmEs0s9Z2mq1S3dwcEFg1WqJ7GJMBargmx1gHCorRNz4ciN8BYG3ERYKAGyzrfmrqMDDVMpL-BKb8ZOzETe8Ms6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bea0c04d9.mp4?token=fyyacducrAVsvgaBoqBJRUBqqv4oA5mF1goYXd42SCcKo8tSoQ5QOINjXEtFYPD-4B2D6Pc2aDNMp8cPFXxtjuuiHAQSQ9WSrGQhdltw5sRN6KsyzZdyskCTvTnsuAlR1T7pZVwS91cogYaQUgY8oUBRqbM9_KE9fHm_c2H0RSBMSgWK32BeJTvgsK5NmAZoZwhazU3moL-DEN_lXETl6TvaADIF_PmSIM4X0MF5eIO9e02deBvF7q3BixW7VtEmEs0s9Z2mq1S3dwcEFg1WqJ7GJMBargmx1gHCorRNz4ciN8BYG3ERYKAGyzrfmrqMDDVMpL-BKb8ZOzETe8Ms6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
پهپادهای اوکراینی اوایل امروز به پالایشگاه نفت اومسک، بزرگترین پالایشگاه روسیه، حمله کردند.
این پالایشگاه در فاصله ۲۷۰۰ کیلومتری از خاک اوکراین واقع شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67390" target="_blank">📅 19:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67389">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee21b0d93c.mp4?token=bCx5QDu9oKEGm-MJoinJvu0kK5oKfu6wHKCrKnXwEY1oWR7PG8rhTe_bHeAl4nB4gKkbWgzREIoSw-dTb7N7QlbWXwmKOIhImwB1r8xnxRX9qqAM8MTezSSCZL7OFlI13NV2FbsUKiZbOFvm84JyYQkmCIkWytB6M7tgs6Oyv-MHKeLmxQUPLKms8bfEyKJW4ml82ZIf6mFM-eFfWGLpDzjaFjLc5YNcR4GCQ_4kqThozTM00k7qVHEzkUM88zuXzVOUrr9geCeHNzWTGt6iG12od088M7nuXoWFAB77WPYLSQ7lBE5H7dmhukQW_cJNffKZMMrKNh463enQXpJ41Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee21b0d93c.mp4?token=bCx5QDu9oKEGm-MJoinJvu0kK5oKfu6wHKCrKnXwEY1oWR7PG8rhTe_bHeAl4nB4gKkbWgzREIoSw-dTb7N7QlbWXwmKOIhImwB1r8xnxRX9qqAM8MTezSSCZL7OFlI13NV2FbsUKiZbOFvm84JyYQkmCIkWytB6M7tgs6Oyv-MHKeLmxQUPLKms8bfEyKJW4ml82ZIf6mFM-eFfWGLpDzjaFjLc5YNcR4GCQ_4kqThozTM00k7qVHEzkUM88zuXzVOUrr9geCeHNzWTGt6iG12od088M7nuXoWFAB77WPYLSQ7lBE5H7dmhukQW_cJNffKZMMrKNh463enQXpJ41Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ در مورد جنگ پهپادی:
چه کسی فکر می‌کرد که پهپادها به چنین عاملی تبدیل می‌شوند؟ آن‌ها ماشین‌های کشنده هستند. شگفت‌انگیز است. شما پشت درختی پنهان می‌شوید و آن می‌آید و شما را می‌گیرد. و من صحنه‌هایی را دیده‌ام که نمی‌خواهم ببینم و نمی‌خواهم شما هم ببینید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67389" target="_blank">📅 18:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67388">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02a06527a7.mp4?token=qbaoIW3536WIEQ9v1zVKjtlmXLOOUkbks-TVidZ6DNCMUaEbEJC3a-6T0NW_jwKD7UBzCAQz2dc2V9E-gqtwssxS3jZ8-07XfBp4CpMU4P2plzGd6_jRK-kUhj6Tz82x3VlNiGghDABw60iEgEzGX1vpJXGUlyZU6INlTjjr6DPToNhqLCL-SgxuYMpprUJszXtwvUDKysUuXC44pVwYiT9iSe_JR4bKHc0aAbablQZKsTBTPixTSd5rQWnQwREx9OSh1kqjviyJbBCL5ccybO12CUstVlQbZAceiKUJLdy-KDYgUK0EhSJHI9hL3b17zfPNwYQb4ac-PUlXKwjltw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02a06527a7.mp4?token=qbaoIW3536WIEQ9v1zVKjtlmXLOOUkbks-TVidZ6DNCMUaEbEJC3a-6T0NW_jwKD7UBzCAQz2dc2V9E-gqtwssxS3jZ8-07XfBp4CpMU4P2plzGd6_jRK-kUhj6Tz82x3VlNiGghDABw60iEgEzGX1vpJXGUlyZU6INlTjjr6DPToNhqLCL-SgxuYMpprUJszXtwvUDKysUuXC44pVwYiT9iSe_JR4bKHc0aAbablQZKsTBTPixTSd5rQWnQwREx9OSh1kqjviyJbBCL5ccybO12CUstVlQbZAceiKUJLdy-KDYgUK0EhSJHI9hL3b17zfPNwYQb4ac-PUlXKwjltw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ درباره کارت قرمز بالوگان:
من درخواست بازبینی کردم چون فکر نمی‌کردم این یک خطا باشد.
این یک نفر نبود که به صورت کسی مشت بزند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67388" target="_blank">📅 18:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67387">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e1e1775aa.mp4?token=pjC_DEJEPCMHqnfRvewQGpYGYFsIz95PFIVTSfFUR8btOGsP7oodDUfblt1c1b1Dtf5hGIj9ev_wESn3ZQC3LIS0MzMdPnq3Buz1piRhIGBVyoHp5bDCZbTahYGjc8te4uK9xmc4I5LjTp8SIm6sNcA7F9MyoFLqTuqbyqWjOjbIjpy4cGrsCelvI4kyGohSiZVlGNFTDJV0hf3B32jZBGZXW9tlwSHMlqS6N30SNFfVGYLO8Z-PsmPC1AmvoODvG8TfIFy8PlwlwTxeAqPV47vNYq6qs6XgvcbQ6Ni3zlFtyeV_N8L7anTiAbLP-dsF8qdf4zQmoHnjCFTdUVqpkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e1e1775aa.mp4?token=pjC_DEJEPCMHqnfRvewQGpYGYFsIz95PFIVTSfFUR8btOGsP7oodDUfblt1c1b1Dtf5hGIj9ev_wESn3ZQC3LIS0MzMdPnq3Buz1piRhIGBVyoHp5bDCZbTahYGjc8te4uK9xmc4I5LjTp8SIm6sNcA7F9MyoFLqTuqbyqWjOjbIjpy4cGrsCelvI4kyGohSiZVlGNFTDJV0hf3B32jZBGZXW9tlwSHMlqS6N30SNFfVGYLO8Z-PsmPC1AmvoODvG8TfIFy8PlwlwTxeAqPV47vNYq6qs6XgvcbQ6Ni3zlFtyeV_N8L7anTiAbLP-dsF8qdf4zQmoHnjCFTdUVqpkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ درباره بالوگان بازیکن تیم فوتبال آمریکا:
بالوگان بهترین بازیکن ماست. او کارت قرمز گرفت. من نمی‌دانستم این چه معنایی دارد، اما بعد شنیدم که به این معنی است که شما نمی‌توانید در بازی بعدی بازی کنید. این بسیار ناعادلانه است. چگونه او را برای بازی‌ای که هنوز بازی نشده است جریمه می‌کنید؟ من درخواست بازبینی توسط فیفا را دادم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67387" target="_blank">📅 18:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67386">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af665dba5e.mp4?token=VlmayypIcIKJpM_Q8MdwUyYzoz6xEc3RsOfDGeW1LwwsyfcTTjwUqWaU-2sdzwTj_B_47nyRsxdtIByTrZfP0xsKOfGEImWud5sUshbBPGuDcKx12msUmMPkuh_1Hu9yztCaOywDiqHxZ7c5KbL38SjYeDN7SHcVTh08KraVU_MIy_tLWtFDczuJ22L8Zd8AVYbhIkmgueLr1_OItV3RcdZnYHRbS6NLPNAy7XTzQ3NVolr_-frDzfDgmkqvQHEjUIzitclSV1hO-YJ06f6SjFZblLlMf5f8SZUlKVl7RgSIyv5CtkCOwLcIb-njVpxB8-Lqw66W40sOOXsSScUtnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af665dba5e.mp4?token=VlmayypIcIKJpM_Q8MdwUyYzoz6xEc3RsOfDGeW1LwwsyfcTTjwUqWaU-2sdzwTj_B_47nyRsxdtIByTrZfP0xsKOfGEImWud5sUshbBPGuDcKx12msUmMPkuh_1Hu9yztCaOywDiqHxZ7c5KbL38SjYeDN7SHcVTh08KraVU_MIy_tLWtFDczuJ22L8Zd8AVYbhIkmgueLr1_OItV3RcdZnYHRbS6NLPNAy7XTzQ3NVolr_-frDzfDgmkqvQHEjUIzitclSV1hO-YJ06f6SjFZblLlMf5f8SZUlKVl7RgSIyv5CtkCOwLcIb-njVpxB8-Lqw66W40sOOXsSScUtnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
یا قرار است توافق کنیم، یا قرار است کار را تمام کنیم، باشه؟ و تمام کردن کار سخت نخواهد بود. ترجیح می‌دهم توافق کنم چون نمی‌خواهم به ۹۱ میلیون نفر آسیب بزنم. می‌توانیم پل‌هایشان را در یک ساعت خراب کنیم. می‌توانیم تأمین انرژی آن‌ها را قطع کنیم، تمام آن کارخانه‌های بزرگ که ساخته‌اند، بزرگ، زیبا و مدرن. آن‌ها اکنون هیچ پولی ندارند. ما به آن‌ها پولی نداده‌ایم. می‌توانیم کارخانه‌های تولید برق آن‌ها را، به قول من، در بخش کوچکی از یک بعدازظهر از کار بیندازیم. هر کارخانه‌ای از بین خواهد رفت و آن‌ها این را می‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67386" target="_blank">📅 18:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67385">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f387513a36.mp4?token=MWPi6f1dieF6Mxft7ppZjdcwqwG6whkQMbD4CXRMwdCCJqVck5GcQXg5zbXXtrBx67juQyTyvHLWMRtJxM6cRk_BBMc8rc6avHyrzhUY0LeTHt0f8S5BGnjOB3v0xWEq2SqEsplLimRysicV53Lza2R4QV_tfhI5sEwriyQx-mGf2dKsEb74M0rKqpkgwx8U4aBmzGmI0U_6c_CitwCp2zUEogPBBrc7WU7m1OQNU5_hDJVBK7lbdtAZaZ6tWLjUqApJtiy1kyttNqIqE5LHqmbdL0b1kmODR39L10IzKa_kKrUmXwvbQt7dbHYX25do_72iBb4MIolrsl_y_YD3ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f387513a36.mp4?token=MWPi6f1dieF6Mxft7ppZjdcwqwG6whkQMbD4CXRMwdCCJqVck5GcQXg5zbXXtrBx67juQyTyvHLWMRtJxM6cRk_BBMc8rc6avHyrzhUY0LeTHt0f8S5BGnjOB3v0xWEq2SqEsplLimRysicV53Lza2R4QV_tfhI5sEwriyQx-mGf2dKsEb74M0rKqpkgwx8U4aBmzGmI0U_6c_CitwCp2zUEogPBBrc7WU7m1OQNU5_hDJVBK7lbdtAZaZ6tWLjUqApJtiy1kyttNqIqE5LHqmbdL0b1kmODR39L10IzKa_kKrUmXwvbQt7dbHYX25do_72iBb4MIolrsl_y_YD3ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
تنگه هرمزِ معروف؛ هیچ‌کس تا حالا اسمش را نشنیده بود، اما عجب ماشین پول‌سازی است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67385" target="_blank">📅 18:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67384">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b6983cd6.mp4?token=DGfm8AuMlSxU-zVI8ftoIWkfIBAL8KbOaks0PHs5MrubQGMKaVuSKNCAK9oIwoFu9NUwDkHWQA6sd-vQCViBXwSPuse7Od22KksLd1i8JwDLv9Es9YgvLwhC2pMxeBRRxt36zuCVU1O4j3CDtmUBCT9wA0lspD9DuyGn8OFs9ViuIPJjby0LTSiXP5jgoO8Wd7hCXE6ue-r1scGtptFjTkVFd1bNrFYt0WWGyxUKI-krrVqaTVGT7U5PjjUEDMribwPdM6VYOimfv_scYZ1Lam0WOsxrp80nlgtFop7AedW0BzB6LXFlmgvW7UVf5aJAKlmPV7OUHGcNg2sbix0ZXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b6983cd6.mp4?token=DGfm8AuMlSxU-zVI8ftoIWkfIBAL8KbOaks0PHs5MrubQGMKaVuSKNCAK9oIwoFu9NUwDkHWQA6sd-vQCViBXwSPuse7Od22KksLd1i8JwDLv9Es9YgvLwhC2pMxeBRRxt36zuCVU1O4j3CDtmUBCT9wA0lspD9DuyGn8OFs9ViuIPJjby0LTSiXP5jgoO8Wd7hCXE6ue-r1scGtptFjTkVFd1bNrFYt0WWGyxUKI-krrVqaTVGT7U5PjjUEDMribwPdM6VYOimfv_scYZ1Lam0WOsxrp80nlgtFop7AedW0BzB6LXFlmgvW7UVf5aJAKlmPV7OUHGcNg2sbix0ZXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
به یک دلیل وارد شدم: ایران نمی‌تواند سلاح هسته‌ای داشته باشد.
من به دنبال تغییر رژیم نیستم، اگرچه این تغییر رژیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67384" target="_blank">📅 18:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67383">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d6c7e39a.mp4?token=hZq1KGW0DRg1Cr67bd24K9ZNHzY1a_LTAubyTuIDVhFHsa7exKsPG9KjDw1Mayzk0yO3HD-84HTFeZaLSZkKcYhm6TUzAlZeBIHHRHAE141mwkDkmEMSrs_JZa4P7VFj5NvK0cNsWfc6GCly9iss2C3qi8mJAGDRWwcTQU4hgYGuZubiq3HPI-rNLFjmxL9gdDwo4wIUh2noy-6vkagGCaTgg5D2sDq_X4m-9B7Dby2JKIRAAJ3qaQPeSLUCfZdASuxrugW7oSNK4NZ0wOksIdJgrI5HcpvxjgI7yzu8ar6uIA18X1-yNkaSPlVIo2hDD9Jk7PDZVrsgKpCoBVbf9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d6c7e39a.mp4?token=hZq1KGW0DRg1Cr67bd24K9ZNHzY1a_LTAubyTuIDVhFHsa7exKsPG9KjDw1Mayzk0yO3HD-84HTFeZaLSZkKcYhm6TUzAlZeBIHHRHAE141mwkDkmEMSrs_JZa4P7VFj5NvK0cNsWfc6GCly9iss2C3qi8mJAGDRWwcTQU4hgYGuZubiq3HPI-rNLFjmxL9gdDwo4wIUh2noy-6vkagGCaTgg5D2sDq_X4m-9B7Dby2JKIRAAJ3qaQPeSLUCfZdASuxrugW7oSNK4NZ0wOksIdJgrI5HcpvxjgI7yzu8ar6uIA18X1-yNkaSPlVIo2hDD9Jk7PDZVrsgKpCoBVbf9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
مقایسه اجرای سحر امامی، مجری تلویزیون جمهوری اسلامی، بعد از مرگ علی خامنه‌ای (10 تیر 1405)
و اجرای ری چون‌هی، مجری تلویزیون کره شمالی، بعد از مرگ کیم جونگ ایل (28 آذر1390)
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67383" target="_blank">📅 17:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67382">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3237168e66.mp4?token=klCqk6OD-l4Tp0fl8hjD6jH8n-MKsksh5LxOAb2G5okC5Vyn7yPm-hZiOwHSiyTW6lmzthehaSNwPYDqWL8fItW4Kib4WPmUhzGZfDHqKpz2hH15HZcKDtQuZksRhRwK4W1bmcpgaWRQr12AAR74UqSJUcBz2RfY7BNhuRV8iLz-CxyfIcHJliEAE3AfYjIVNc6ero3oF1NV9GFMvq9d5jdELncnEaV_FqFrkMfGM7j0X8tB8KkAfTNaI0Cf2CGBfqaFU3HUEIUMRYd6OKcCJHqooNe2Rzy2tC9aEcB5XYDJEyLMjxqmtpdl9dObg3Wwaloj41wdr1r16FzdRSPP6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3237168e66.mp4?token=klCqk6OD-l4Tp0fl8hjD6jH8n-MKsksh5LxOAb2G5okC5Vyn7yPm-hZiOwHSiyTW6lmzthehaSNwPYDqWL8fItW4Kib4WPmUhzGZfDHqKpz2hH15HZcKDtQuZksRhRwK4W1bmcpgaWRQr12AAR74UqSJUcBz2RfY7BNhuRV8iLz-CxyfIcHJliEAE3AfYjIVNc6ero3oF1NV9GFMvq9d5jdELncnEaV_FqFrkMfGM7j0X8tB8KkAfTNaI0Cf2CGBfqaFU3HUEIUMRYd6OKcCJHqooNe2Rzy2tC9aEcB5XYDJEyLMjxqmtpdl9dObg3Wwaloj41wdr1r16FzdRSPP6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
مارکو روبیو: سوسیال دموکراسی همان کمونیسم با ظاهری آراسته است.
مارکو روبیو، وزیر خارجه آمریکا، با انتقاد از سوسیالیسم و کمونیسم گفت تنها کسانی که کمونیسم را از نزدیک تجربه کرده‌اند، درک می‌کنند که سوسیال دموکراسی در واقع همان کمونیسم با ظاهری آراسته است و پشت این ظاهر، همان ایدئولوژی خطرناک و ویرانگر کمونیسم قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67382" target="_blank">📅 17:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67381">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54408a1a4b.mp4?token=O0RI5UjuBwGZ3cQkODBRXUlEF9xzRtslHq1Pzw9Ny3bdjerxQuEIvnWxfb-NMss2O2IuP0aw74dnHAv7yWS6BCEK9DevFlSeyXEFo3hmebAvRQInKtlpDHxRNf_0Q-tIYJMOv4nYAO1QNzLeqhhb1DWuoUwPx31iNAd9TmNyz1qy3py_1ehZkaPlHNl9-QvaJZ45AG6wiPlhxhopG7l5r7BDL2N5Ztf2pVARU0kj9yUJUdTlLQtTFnWsmETYa9oxDv5EW9s95vVwYMbo5sFtm2zATZJRCYDTzBPrTfAmd3gdKMKxQE97QDRroq3mRyaSre0DLd5R366hdFDr-LGvGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54408a1a4b.mp4?token=O0RI5UjuBwGZ3cQkODBRXUlEF9xzRtslHq1Pzw9Ny3bdjerxQuEIvnWxfb-NMss2O2IuP0aw74dnHAv7yWS6BCEK9DevFlSeyXEFo3hmebAvRQInKtlpDHxRNf_0Q-tIYJMOv4nYAO1QNzLeqhhb1DWuoUwPx31iNAd9TmNyz1qy3py_1ehZkaPlHNl9-QvaJZ45AG6wiPlhxhopG7l5r7BDL2N5Ztf2pVARU0kj9yUJUdTlLQtTFnWsmETYa9oxDv5EW9s95vVwYMbo5sFtm2zATZJRCYDTzBPrTfAmd3gdKMKxQE97QDRroq3mRyaSre0DLd5R366hdFDr-LGvGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در برنامه ای در صداوسیما حدود بیست دقیقه کارشناس برنامه اسامی سران و مقامات جمهوری اسلامی که توسط آمریکا و اسرائیل ترور شدن رو خوند
بعدش مجری به کارشناس گیر داد که الان بیست دقیقه وقت برنامه رو گرفتی که اینها رو لیست کنید و در ادامه میگه به جای اینکه به مسولان و مردم دلگرمی بدی داری دلشون رو خالی می‌کنی.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67381" target="_blank">📅 16:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67380">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84629e4c7d.mp4?token=EdVhtrH86cYFIcb6zSIheIsI3nUyK7DEPkEbctaSdVzde16-GzP6IPrZBeJyTebZ-nM0eurCbDti_yi-k50p9Ag_fH5F7NSwXYGIwE8ejsyYmCnNckGGsulAI3xGnnrJZ4Hurs_o3EMGodpchfQxf6HnxH7HPzRjDDWYVT4LR56lbKyJXHD3fPecl6A0A_bOYZwc0j6pT8cPxdehbMnb3m8wZRMt61qVp-UZpQGV8-E_SfjWKON3KMmIenHufqHvogX1gebalRS3QjM2WwcWPJ4IKnBNiA0DBCJpS7zgzgtPcAh4r_egcUDJqBQJlgn-K_HnTsDqaNWcDU4o8HI9pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84629e4c7d.mp4?token=EdVhtrH86cYFIcb6zSIheIsI3nUyK7DEPkEbctaSdVzde16-GzP6IPrZBeJyTebZ-nM0eurCbDti_yi-k50p9Ag_fH5F7NSwXYGIwE8ejsyYmCnNckGGsulAI3xGnnrJZ4Hurs_o3EMGodpchfQxf6HnxH7HPzRjDDWYVT4LR56lbKyJXHD3fPecl6A0A_bOYZwc0j6pT8cPxdehbMnb3m8wZRMt61qVp-UZpQGV8-E_SfjWKON3KMmIenHufqHvogX1gebalRS3QjM2WwcWPJ4IKnBNiA0DBCJpS7zgzgtPcAh4r_egcUDJqBQJlgn-K_HnTsDqaNWcDU4o8HI9pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو در گفتگو با فاکس نیوز:
ایران کشوری با حدود ۹۰ میلیون نفر جمعیت است و حدود ۸۰ درصد مردم آن از این رژیم متنفرند. اقلیتی که شعار «مرگ بر ترامپ» و البته «مرگ بر من» سر می‌دهند نماینده مردم ایران نیستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67380" target="_blank">📅 16:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67379">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336146a8b7.mp4?token=nPE6bDupT4GIP-xGdrtBMU7EMchQrHS8xgd4MoN4dmOh1hfor14wDVluvHbZoY7OZmzF1weyYUDfX1etbJblXHnZK46tH2OBgczqn0L6NOMulC9n7mwFCLtwyW7sxNYYHogtyJGYCyVKIANQTpLZSet8rtsXNN8n-j2-HGttjWQleGYzihGGo5zYxi0QBi-ZFXYosoWFFNRxelbR6xw-hAYiLU57lRcus2xUEmBd4XW9--DPM1PwdAr8CvxqHZs5DH2RTlRG584ZY0a4TP7RqIgTDGU6HXEOSG6d8_pxARZdxhATKMBVYmjJKUIV3-uFTCyepB7Yxk4rI1fmtTaBUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336146a8b7.mp4?token=nPE6bDupT4GIP-xGdrtBMU7EMchQrHS8xgd4MoN4dmOh1hfor14wDVluvHbZoY7OZmzF1weyYUDfX1etbJblXHnZK46tH2OBgczqn0L6NOMulC9n7mwFCLtwyW7sxNYYHogtyJGYCyVKIANQTpLZSet8rtsXNN8n-j2-HGttjWQleGYzihGGo5zYxi0QBi-ZFXYosoWFFNRxelbR6xw-hAYiLU57lRcus2xUEmBd4XW9--DPM1PwdAr8CvxqHZs5DH2RTlRG584ZY0a4TP7RqIgTDGU6HXEOSG6d8_pxARZdxhATKMBVYmjJKUIV3-uFTCyepB7Yxk4rI1fmtTaBUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مجری:چرا آن دولت هنوز در ایران پابرجاست؟
🔴
نتانیاهو: زیرا چند صد هزار مزدور دارد که در روشنایی روز می‌کشند و قتل‌عام می‌کنند و در شب مردم خودشان را می‌کشند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67379" target="_blank">📅 15:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67378">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCR70sBKizt4YglVMh3lmIlMzdE8dtlY5RsVCVvSdHd1fnc71zWiI6jPiRZ45z1lIJPPWDqZ5mhWwYR8WNKzVuTM9uFVMSqbLZPfPZ6Kc3c-xuIQgZMW6Is2wZ5--rJ9BpZ_4WlIjQ3TFuSb_pJ-C9P8a2PaCC2988jvsoRnjQYnr8NFfDUav-RnHjl0BACyWhu9_8P9BBXEhhhmopjuS4xTzb45cbL7fe0ui9wyMhI7pwiuk6lz6bJKygKrJPIIVwr0ZtYGiF5Z_P_3qDbeF0k7t25tKm-TZwpffMlmd6LL0XStp3BqpqGR6xQpCxpAPEtGJV8_ymjkqPCJ4wN6Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
واسه کشتن نتانیاهو وترامپ 100 قطعه زمین 2000 متری جایزه گذاشتن،آیدی رو هم زدن اون پایین و گفتن انجام دادید پیام بدید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67378" target="_blank">📅 15:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67377">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHPK3gCcrt5q1zv4zqayexWNEBiCLoLq5htV9IugQihHjBteUExkF76zUpwuVss1TGO2QCKnRYOApZMYrh5pBm0jM-r2_HBPuPUtsThiPPyiphEPqUbC0aqXWRvOB_DrZBGGeUCoek61SApFhg6HJ5T-rvFx_mdpiZMG4BwRO4i9yUtPaXXzMXkHTYS02zlEIymX0AehFMksKIJQ2DsQVoaKbUGynxoOxMRiE2gW8_xu9bUS6J9Cx1bmkeJy2xdiEt4rm1QJdcRaraiFjOyeCcAtHhKY1nF7C7l7jclPSectIycmWC9217k57anjFHDNpM5kcjomS224BVspu9fvJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دو حمله پهپادی هدفمند اسرائیل در جنوب لبنان.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67377" target="_blank">📅 14:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67376">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NH5QX5AiQhcF4AxPhGxADPBZLRNRgkCTAHlq1LaF9h-wjyMChhCvQTStm1DTpz5wTB2udpIa9HfkIxFnwoe2RV1G3EYN-iHEl46W4f0BpjJwETAqhFcJJuFKgZCD_yEf8KMSG_DaDShxa6Amvf1V8x3wqDitt030eRuEuPQJWZGKsFWIYgMUb7fnUAvBptMaDVlY5wrmHjDiqU3nbT2AWg1hBASF9__x7uBeQz74jEt39i2GsqT8tYtgMumaV9snugk1TVCFcuIhmxcs1abm-DpDBiflaFZrjGBYBcZBXnkesnXyWIvD0V4TkPBvwkpeIcSp3MJK99MBL1PqcYiu8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏شبکه ۱۴ اسرائیل :
سپاه قدس واحد جدیدی به نام « یگان مختار» تشکیل داده است که با کارتل های مواد مخدر مکزیکی و آمریکایی و همچنین ایرانیان خارج از کشور برای ترور ترامپ و ژنرال های آمریکایی همکاری می‌ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67376" target="_blank">📅 14:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67375">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8dkeoMt1dN3m8IM7GE1bNQ7w5N4PnxGkBe0V6E9k-ewAQGCVZi9X5zL6BFhux7TqGpVeE1zlmjWbyKmtbAcY0ZjtV2UfoMw7ckbpq-GCsvcDrxiltb9DyElxY9feTDyIRSmpan0Or7zjoxHF-N3JxM5vWyPXuxAnhRhmzJWseh2d1ADqEqhA24H7g_SasrT2f3WGIsW2TbxFPWCiTcitIXBAo4OMSmzQYZYeeX7xjwBsK2zx3EFA_0vP2njW5fUNuR8WkJEX8zAODPI0sQL3OyR2p20yTR0Z-Ds4vWcSUEE_KjbQDJa5kfNG4FdTfbb4Pcri99K0O982_NKQ7LTIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یک بنر در مراسم:
دونالد، نابودت می‌کنیم! از توجه شما به این موضوع سپاسگزاریم!
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67375" target="_blank">📅 13:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67374">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjSIh5MDBSTY5LaJwBnRqe55HxgYx32iQUoJW1Ldxn75QpwGD9aqg3z-NzVt2Wl2rHYvxc9WryEItnKkYXWg4DJdwjiE0yQ0eMYY2qLLWdQkt_VLDeaNgCVY0iDZGvw62HIll3qOhCdxAqXo6mvk7ieQIbSjYDV-08EdMERRwNuwXyPz2Q6c2buEsKKHFpUD8AzKTUKRU9myMS2khDYWRYwY4vhatMqG1mhD3l8apzCwK_OmiZ8N6VmzABjKHB68CIUUOocdct0Ccf5opdla99t-k9owloXFHqbtPZWzmbRH9grAHe1bRyH4kFnYHWeIN_ZMWH1pjD1-glsP3domBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
ادعای
نجاح محمد علی کارشناس عراقی مسائل خاورمیانه و از حامیان نظام جمهوری اسلامی:
در مراسم تشییع امام سید خامنه‌ای رضوان‌الله‌علیه در تهران، فرزند ایشان، بقیةُالسَّیف، آیت‌الله سید مجتبی نیز حضور داشت. او پنهان نشده بود، بلکه در جایگاهی قرار گرفته بود که کمتر به چشم می‌آمد.
هماهنگی بسیار خوبی با نیروهای ویژهٔ امنیتی و فرماندهان ارشد سپاه پاسداران انجام شده بود…
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67374" target="_blank">📅 13:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67373">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4acsZ0MfuVjjL8R0NvzhCcsMnSL8Wq5t1XRedr5_8Hj6DoDXgWr8zqgV7emA7HTf9dQRORnpvNh3oQ57uRu2xBuTn_IZGPpP8Vajh2kfkPyGzBtlaBLrQK2qkquQnF7s5G7gBa0nRg1VXZhqY_dpMYaSlFCdr80KPFhCxLMP0_AmT7RgF20gwZm52graYlXcmuN4Gq-G8NMf1hpSPKVmstgB_N-TU1YACNFVe_SpeVUwVnjGmKoYQHlswazKdv4sgu02OjX5xUx4nzULLAYrNBnqydJsst38uia6pTb0_fFYuk9mvm2t71NhCu9qLgJY_UeWH_y8vLTvmQKgCcHpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
«آیت‌الله خامنه‌ای که مراسم خاکسپاری‌اش هم‌اکنون در حال برگزاری است، توسط اسرائیل حذف شد. هر رهبر ایرانی دیگری که برای پیشبرد طرح‌های نابودی اسرائیل تلاش کند و اسرائیل را تهدید کند نیز حذف خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67373" target="_blank">📅 12:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67372">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22aca7392a.mp4?token=AbmDqQiBkUzRwYs3MPnEFjxdvqimvcDUkSYdE6scGeccL4dKO4OYx5ZVkIsa2y8acAM9BxiZ0_hSHVEEqSoSiqCVJBP7oJN1PVl3ogkn7BslU4al3R9KN_TQFKKoywhl_ZPmEDsZfLOm6eJOqFc0gQ158U5YWR2h4yamo975uuTl02i6aGFRwZ8ipL0x6PRWc2chLVQcRzrGCNC-ew43ETNnaWZ20vUh9_TrP9Ihq_NShn9YP_URNnP2RHOvk6fuyZMEwvp6ddzC3nWgyGF2E1GBR34e5o2EUhxS_ygoYtj9-RuZk1PVztHAk8-1yNfsziam241ZMZsMhTcEHZq-dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22aca7392a.mp4?token=AbmDqQiBkUzRwYs3MPnEFjxdvqimvcDUkSYdE6scGeccL4dKO4OYx5ZVkIsa2y8acAM9BxiZ0_hSHVEEqSoSiqCVJBP7oJN1PVl3ogkn7BslU4al3R9KN_TQFKKoywhl_ZPmEDsZfLOm6eJOqFc0gQ158U5YWR2h4yamo975uuTl02i6aGFRwZ8ipL0x6PRWc2chLVQcRzrGCNC-ew43ETNnaWZ20vUh9_TrP9Ihq_NShn9YP_URNnP2RHOvk6fuyZMEwvp6ddzC3nWgyGF2E1GBR34e5o2EUhxS_ygoYtj9-RuZk1PVztHAk8-1yNfsziam241ZMZsMhTcEHZq-dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور احمد جنتی در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67372" target="_blank">📅 12:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67371">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad63d7f30.mp4?token=FzyNmCCjBJWKONfiw-BQTSqI3CIIAZ3ir76_cNu9-VRJYli0EC59yCVM_jE-aUU_l1VijTiYm5F7ERgdhgg-reSDFJUV9Zz2FwzT3jxVO9ejQRWMV-021F1WJD0TyPg-mdrtvOln84wgu5eXKhKNIX2Bz-5m5HklgKJkMQKEyrThhszY5z6brl1q4P1BRA_-D_MnlRYe5U91LhAMYW56Wno_-i9D4MFJhRZCe6uXQoj7yQ4DUH6nkpNVmNhGPrVpUEn36Ud9tmf-bXVZlRI7SUE5ERZmswInfOamgMQl2Q35OsF8Qg5Qk3tba3IBeUxtC2G8RyzVqxC2Gy9bxLw_wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad63d7f30.mp4?token=FzyNmCCjBJWKONfiw-BQTSqI3CIIAZ3ir76_cNu9-VRJYli0EC59yCVM_jE-aUU_l1VijTiYm5F7ERgdhgg-reSDFJUV9Zz2FwzT3jxVO9ejQRWMV-021F1WJD0TyPg-mdrtvOln84wgu5eXKhKNIX2Bz-5m5HklgKJkMQKEyrThhszY5z6brl1q4P1BRA_-D_MnlRYe5U91LhAMYW56Wno_-i9D4MFJhRZCe6uXQoj7yQ4DUH6nkpNVmNhGPrVpUEn36Ud9tmf-bXVZlRI7SUE5ERZmswInfOamgMQl2Q35OsF8Qg5Qk3tba3IBeUxtC2G8RyzVqxC2Gy9bxLw_wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیوی عجیب منتشر شده از وحید خزایی شاخ اینستاگرام با سردار رادان که میگه کار دارم با وطن فروشای لاشی،ترامپ گفته گوه خوردم
من سلطان دختربازی ایرانم ،حتی سردارچندبارمچ منو روی کار بادخترخالم گرفت ! اماخداشاهده آنقدرمهربونه،هیچ کاری باهام نداشت و ولم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67371" target="_blank">📅 12:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67370">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a17dafc375.mp4?token=FMBo3_GlL7bFubvH6AfTd1xbtrvx1vzsZ4n3TRZgGlNZKiMHQ78hQraWKm9kOieA3Ib1TWfeudjC2P85cP8Dq2JfEAKlov-UyQ9ERHx3CpGZg33abreELGdTz0Ngvpsk7wX0H5I4P-vVT-yV8pwTZrSQ4NuFqgzMe-m4ZALjt01fFb0TTKae9hrbkKeT22utzMgfqYNzb7a009JlovbA3GYkDgQ5naZGPFhTIf4OrrJVqlh2mE37LLo2uXCQ9zHMp4zl_NILqeixdHfACCS7SBKWHdi3WkQvlIU9cSj6fzj1iySeOJgS9DV9cMGR3PGkas0at6XUQ-UjXZbjkBqcWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a17dafc375.mp4?token=FMBo3_GlL7bFubvH6AfTd1xbtrvx1vzsZ4n3TRZgGlNZKiMHQ78hQraWKm9kOieA3Ib1TWfeudjC2P85cP8Dq2JfEAKlov-UyQ9ERHx3CpGZg33abreELGdTz0Ngvpsk7wX0H5I4P-vVT-yV8pwTZrSQ4NuFqgzMe-m4ZALjt01fFb0TTKae9hrbkKeT22utzMgfqYNzb7a009JlovbA3GYkDgQ5naZGPFhTIf4OrrJVqlh2mE37LLo2uXCQ9zHMp4zl_NILqeixdHfACCS7SBKWHdi3WkQvlIU9cSj6fzj1iySeOJgS9DV9cMGR3PGkas0at6XUQ-UjXZbjkBqcWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وحیدی فرمانده کل سپاه با موتور اومده مراسم
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67370" target="_blank">📅 11:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67369">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abfc46c7e6.mp4?token=AE-pleoyYwU0Ds0oNPeIHKv-7gf9Xlia16W_UfxT4ZDGK64PZAz52m_nf-2m6dYWKBLShu7hN4WQXwt3RGoybJFOiyQKxb9amOGUKzdUSrAVYsLkoD2IYu-SNaiGad5m1H_meKR_nD_dH08qPE0WGltcA_CKWmtar4jhKyHaanmpX9CrCDHF9kKOdi8il03gAHOYdE2LoLDFefPLkrktm7wI1p1SdZkTc9ePOn23v_yjtTSHaD6v438ohl8WOWUyYohPuXlVICzE6CKyIYI78jLStDFq675Ygcyq9lJK3Fevy0KARw0cptJ2avd4h4sb5oSmI6JxGJMbZ1Xuwm486A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abfc46c7e6.mp4?token=AE-pleoyYwU0Ds0oNPeIHKv-7gf9Xlia16W_UfxT4ZDGK64PZAz52m_nf-2m6dYWKBLShu7hN4WQXwt3RGoybJFOiyQKxb9amOGUKzdUSrAVYsLkoD2IYu-SNaiGad5m1H_meKR_nD_dH08qPE0WGltcA_CKWmtar4jhKyHaanmpX9CrCDHF9kKOdi8il03gAHOYdE2LoLDFefPLkrktm7wI1p1SdZkTc9ePOn23v_yjtTSHaD6v438ohl8WOWUyYohPuXlVICzE6CKyIYI78jLStDFq675Ygcyq9lJK3Fevy0KARw0cptJ2avd4h4sb5oSmI6JxGJMbZ1Xuwm486A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عباس موزون، مجری صداوسیما:
چند بار [روح علی خامنه‌ای] از بدنش جدا شده بود و تا ارتفاعی بالا رفته بود.
«اصلا بعید نیست آنهایی که علیه بشریت عمل می‌کنند، از نیروهای شیطانی کمک گرفته باشند.»
چی میگه این
😢
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67369" target="_blank">📅 11:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67368">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqaCpDqsKm_R0C0GmlQXdJRxRpWQxpA04ovUAOU-Z-CrQ20JDHZWQ5um0tiXSMIgXYqnf043qnYi7W1Vq-23rNvOuHn4r8yrk4Q8MiDOsHU1Bw6tGVc3KqLxZEhB-ft_VTHyMl42RyJ_nPnrYHj09-l6wNFElZwv_MLcnrPWk1hWdnCdmoXhsxT9Q2OvE4QZbYy9omWGacJ1yIFcd4fpQII8XmB4lfu7g4iemThB02RpncdHhiKAR-4_1YhtBSCTbXM3O5jUnBUEoyCe9Aqhj6mnC4KtuC0Oh5O5zquVLciH3Lk3EXCBYpEeHMqSLVdG3NsXUee8Mo8cxMyhDErCmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکبر هاشمی رفسنجانی،24 اردیبهشت 1370:
سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67368" target="_blank">📅 10:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67367">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c47b7b97.mp4?token=F87pC0aYtvfko7f-1M9m5-GfAGc_GWWw61a2qmnYZq-IcBCQaNTHCPMf_cW0WcTGVPYxMeHKbcak-LGnbCuAgTi_E3OU0Z6eODmlmrmYAOm_GPXcf2J9v8I69bshaSwgjp6gGsbEjIMYyc1UpYsF1CiXlip29beSJblw8-Gpc3N7T51G7Ughb51Qk-M0UonEsUNWnVFEhIsvJfZkqD-hm38LazjRJA_AT0cDjNU-2q3Jm9YbXmPwNAoZcgrdKfo5vySLB8tzm5sWSnml8UuGnKEQKS5tlKL7V-S_fv75XIOr1JseeIb_EXPF2NaRgMKigjALVk8ekR9UZ9m2kYK_FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c47b7b97.mp4?token=F87pC0aYtvfko7f-1M9m5-GfAGc_GWWw61a2qmnYZq-IcBCQaNTHCPMf_cW0WcTGVPYxMeHKbcak-LGnbCuAgTi_E3OU0Z6eODmlmrmYAOm_GPXcf2J9v8I69bshaSwgjp6gGsbEjIMYyc1UpYsF1CiXlip29beSJblw8-Gpc3N7T51G7Ughb51Qk-M0UonEsUNWnVFEhIsvJfZkqD-hm38LazjRJA_AT0cDjNU-2q3Jm9YbXmPwNAoZcgrdKfo5vySLB8tzm5sWSnml8UuGnKEQKS5tlKL7V-S_fv75XIOr1JseeIb_EXPF2NaRgMKigjALVk8ekR9UZ9m2kYK_FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان:
خرافات پدر ایران رو در آورده.
آینده ایران در یک جمله است؛رنسانس.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67367" target="_blank">📅 10:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67366">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33573d06e9.mp4?token=XWvUHE9YN9sDCyFpBpR0qcMapdNcHxhfiPFXZIt1tBgtlG-D1X-hr9HgASYCLju5kAOmF8Ozt2qk6vtx3eV2vZkQq1GxDDHpIK434POmRETzCW1gxYyGvMLyx_i27WiBmo2FGyVdW5dZrMHRKgSsVj9BhZ7j5Tx7bjRh2VwLfUWUDyex-I5dTX_LxObjINir_saW37XHAx2M-_qtUIwic0KQXxgHCEpCOcqhxuLf7i8kMiLWOkuHamsQuAZUBFI-gQcorIBTfKhnblPswpVmOktygB5W_1fD0GR5tNsayCdY1GxuYTFwiG4N9aCA2Wh48W2LxRH3yGEm8UGIZqM-Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33573d06e9.mp4?token=XWvUHE9YN9sDCyFpBpR0qcMapdNcHxhfiPFXZIt1tBgtlG-D1X-hr9HgASYCLju5kAOmF8Ozt2qk6vtx3eV2vZkQq1GxDDHpIK434POmRETzCW1gxYyGvMLyx_i27WiBmo2FGyVdW5dZrMHRKgSsVj9BhZ7j5Tx7bjRh2VwLfUWUDyex-I5dTX_LxObjINir_saW37XHAx2M-_qtUIwic0KQXxgHCEpCOcqhxuLf7i8kMiLWOkuHamsQuAZUBFI-gQcorIBTfKhnblPswpVmOktygB5W_1fD0GR5tNsayCdY1GxuYTFwiG4N9aCA2Wh48W2LxRH3yGEm8UGIZqM-Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مراسم وداع با جنازه علی خامنه‌ای، وقتی نوه‌های خمینی میرن جلوی تابوت سید علی خامنه ای، قاری این آیه از سوره نساء رو به کنایه می‌خونه:
آن گروه از مؤمنانی که بدون بیماری جسمی در خانه نشسته‌ان، با مجاهدانی که در راه خدا با اموال و جان‌هایشان جهاد کردند، برابر نیستند.
اونا هم برمی‌خوره بهشون وسط آیه ول میکنن میرن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67366" target="_blank">📅 09:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67365">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6YGU-en8y4k8viJir56Os5d-gMBIIfPa3a8PRfVdWfKOWjrnI8ddVuRI-lKOQ9qunphXSqP3wPeQOJPqu48UY8FpG5ngIW51OJOdewTk7Lary1IZYS75dwVqGYZk7Nb75R0rRQxgX5sAatowDd46dvH_ZUU_ParIHv6eBNXWXOZhtmi4f49Bid8iy5A707j2SAgxZvUV0_QQ2aLbAK2QXzSm1D5s_uuM-mpzSH3YCGNAegxvBOtXgdr26RvZwJmCe5XuBa6v7d5FwbUUqZ0jAP_IxIwLOsV2kLNP9x_nx6yY27faBBXKyMytNgIucnvPcLTW2BPeWO5VIIzNeWgpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
قالیباف در گفتگو با محمد درویش، رئیس شورای حماس:صلحی با آمریکا وجود ندارد و اسرائیل را به رسمیت نمی‌شناسیم!
🔴
دیپلماسی باید در خدمت حفظ و تثبیت دستاوردهای نظامی باشد.
🔴
مذاکره زمانی موفق خواهد بود که کشور همزمان آمادگی دفاعی خود را حفظ کند.
🔴
ایران بر حفظ تمامیت ارضی کشورهای منطقه و پایان جنگ علیه متحدان خود در محور مقاومت تأکید کرده است.
🔴
جمهوری اسلامی صلحی با آمریکا ندارد و اسرائیل را به رسمیت نمی‌شناسد و حمایت از جبهه مقاومت را در قالب‌های مختلف ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67365" target="_blank">📅 09:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67364">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67364" target="_blank">📅 03:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67362">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qmz5rJPBmwRWFuIJAClUmo8diliY8fZUikn8IbEwRjGz8BPmqbcRa8EEtjje5u4caHgQe5K2q-rkVqlPU9lZTF9WboxhZj8LfAaM5B91c9Cl-lZw8tbdYkIHPGIdw7xdJFLEtw64mESg7iGd_SiwP2zdyjcApQZXjH9BI-9IHfEAO21oFvh_PtQfi8j6Zu-BH8BL5M2UcQQXkqsH322Za8TQn6JkHlp1mA56__RmYRDXVC2pXov21qt5w7d4SKI7yBAKITUjEWCVs49sCPnBAdBbMEoz0cXenMJ915-grkgJsoLQs_JaxuvHopLHNJpstcifgYuwza3-OQvXUFulPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67362" target="_blank">📅 02:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67361">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1fe48304.mp4?token=opccwdwsi2RmXdG_mwg2P8zX7T_pEQkKmMF59KNv5QrZiU3REfVREJZFUShgXCyWRM-cfm_7yHPjPf_CEBc60QeyXAzqqCmDRPZz1-5KQwK_XwA9baa1pt95kiQTXIXCVA70inz2H-v1lTZrqJL6-wCVUgwco_R9f16FG2NVqnHGYu9XqMZFhhwIEmcxQ6qz9r-_1hUe5TEfJzSC_GOTYJgdXDODmOxl4pI3ILUBDBTXKezCor4mJF1nnV7TB7M4bkpgiS3WD0hz8uqLT2AKHVlSx5l62Hb5Z0IIAi-V3EgV3FYxbX6xm2MCOJvEGM7kp5HwDsXbpypuuxpCt-qozA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1fe48304.mp4?token=opccwdwsi2RmXdG_mwg2P8zX7T_pEQkKmMF59KNv5QrZiU3REfVREJZFUShgXCyWRM-cfm_7yHPjPf_CEBc60QeyXAzqqCmDRPZz1-5KQwK_XwA9baa1pt95kiQTXIXCVA70inz2H-v1lTZrqJL6-wCVUgwco_R9f16FG2NVqnHGYu9XqMZFhhwIEmcxQ6qz9r-_1hUe5TEfJzSC_GOTYJgdXDODmOxl4pI3ILUBDBTXKezCor4mJF1nnV7TB7M4bkpgiS3WD0hz8uqLT2AKHVlSx5l62Hb5Z0IIAi-V3EgV3FYxbX6xm2MCOJvEGM7kp5HwDsXbpypuuxpCt-qozA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
ارتش دفاعی اسرائیل:
پس از فعالیت در نزدیکی نیروها: ارتش اسرائیل یک هسته تروریستی وابسته به سازمان تروریستی حزب‌الله را در منطقه العقیده هدف حمله قرار داد
امروز (یکشنبه)، نیروهای تیپ کماندو یک هسته تروریستی وابسته به سازمان تروریستی حزب‌الله را که با موتورسیکلت در منطقه العقیده، در نزدیکی منطقه امنیتی محل فعالیت نیروهای ارتش اسرائیل، در حال فعالیت بود شناسایی کردند.
فعالیت این تروریست‌ها تهدیدی برای نیروهای ما محسوب می‌شد.
پس از شناسایی، ارتش اسرائیل در یک حمله دقیق، این تروریست‌ها را با هدف رفع تهدید هدف قرار داد.
ارتش اسرائیل به فعالیت برای رفع هرگونه تهدید علیه نیروهای خود ادامه خواهد داد و به سازمان تروریستی حزب‌الله اجازه نخواهد داد به شهروندان اسرائیل و نیروهای ارتش اسرائیل آسیب برساند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67361" target="_blank">📅 01:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67359">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/beH0Uzjy2AKJp6LgmHVKVwDupO6US96nMYx-VZTmRavJCcKTKYz_c2zN38_2tWGa-KImOb8uz_Ak-2JEo7O5odDewClz9cOM9i7yashD1BhN1iKXtcIyiWYzcCjkX8nZfTJt6-KJrny1dSU55CJ7cpLHHkGYL67vaDRurXvJ5ENrr0EptxGeoDF-UStmCXX22ATc_g9vSBLe8KzQf94PojpTRqHqd4RLKZLEYyHSMT7cNwu8n-T7jqwTUofobZfh68kpgUirXuMbb_nbYS8wyyWxftmAlpKac0XryV9zY4ScLeIaFRzFOICBvHAC4q5auMeIwFGqtLXXTnzFgw5Qkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کانال ۱۴ اسرائیل:
انتظار می‌رود نخست‌وزیر اسرائیل(نتانیاهو)هفته آینده برای دیدار با رئیس‌جمهور ترامپ — که هشتمین دیدار آن‌ها از زمان بازگشت وی به قدرت خواهد بود — راهی واشنگتن شود؛ دیداری که در آن برنامه هسته‌ای ایران و خرید احتمالی جنگنده‌های اف-۳۵ توسط ترکیه در صدر دستور کار قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67359" target="_blank">📅 01:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67358">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6d2fa6e6a.mp4?token=CLnr9YTpbOLo9fLbXQd17WoKCaEuNB_oNQRy8zwrUY6CtU0dPNrkJzH72w3hZE7j4JOSdkx0-UyTRXXd_iCN3Dr3PnlkoXrIekcTG7hlAl-BwTRJaEg3UjHfLExUhcX4YjVCG0UOkTLMzDDQDZbkFS7pydNEWDKgv7YnwNNRSzBN6-S6igW82ogztn8fIAVdoP6cDxY5aKH9fwmXliHUl9ZtUqx5tLEgkgKe8dR-51WWjB5onvJz8JUxbenrc0RVitO0fLf14oEaj8vrQKsib-pUdbr8VGHwnRy2gIKt4ZU_s5Edlwfqjhnt43FMiW8V19gIZoWZWfxmJaXg_Dd4gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6d2fa6e6a.mp4?token=CLnr9YTpbOLo9fLbXQd17WoKCaEuNB_oNQRy8zwrUY6CtU0dPNrkJzH72w3hZE7j4JOSdkx0-UyTRXXd_iCN3Dr3PnlkoXrIekcTG7hlAl-BwTRJaEg3UjHfLExUhcX4YjVCG0UOkTLMzDDQDZbkFS7pydNEWDKgv7YnwNNRSzBN6-S6igW82ogztn8fIAVdoP6cDxY5aKH9fwmXliHUl9ZtUqx5tLEgkgKe8dR-51WWjB5onvJz8JUxbenrc0RVitO0fLf14oEaj8vrQKsib-pUdbr8VGHwnRy2gIKt4ZU_s5Edlwfqjhnt43FMiW8V19gIZoWZWfxmJaXg_Dd4gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو ای که فرستادن به صداوسیما از لحظه حمله به خونه نتانیاهو و ترامپ و گرفتن انتقام علی خامنه‌ای
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67358" target="_blank">📅 00:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67357">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/237c10defa.mp4?token=Xi9VO_3b--09fuUHfUbg-Jn58WFDBp9wftiLte_JFx3h2rvqPmwFvGgH90vV4v-TdOnWF8zPao4LLhDdDMMsGii7fHdU7cAeay3MVqF3bHdhjKKheR5lO0SVPFVcUjFyzZH6r0CXXzpax0qI9roM0H6IVsCDZXGDKWEhL394QEJqXyWxPowWB_kKV1BBFnEyBZrBWrMyveDzY2TUbi2-qWri5_thzHBcHPO8G3uv02v4Kg_2JnyiAuBcw3qM_ph1GcvyJDdfR715R6NgptB5_ULnSbYVMG5Gp4_H0PrRjVf_skyN2z0gypnG375GDte9vDkQtVL7ZcZ1nf2d0qtqJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/237c10defa.mp4?token=Xi9VO_3b--09fuUHfUbg-Jn58WFDBp9wftiLte_JFx3h2rvqPmwFvGgH90vV4v-TdOnWF8zPao4LLhDdDMMsGii7fHdU7cAeay3MVqF3bHdhjKKheR5lO0SVPFVcUjFyzZH6r0CXXzpax0qI9roM0H6IVsCDZXGDKWEhL394QEJqXyWxPowWB_kKV1BBFnEyBZrBWrMyveDzY2TUbi2-qWri5_thzHBcHPO8G3uv02v4Kg_2JnyiAuBcw3qM_ph1GcvyJDdfR715R6NgptB5_ULnSbYVMG5Gp4_H0PrRjVf_skyN2z0gypnG375GDte9vDkQtVL7ZcZ1nf2d0qtqJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پهپاد اوکراینی یه سرباز روس ـ افریقایی رو تو یه مزرعه تو شرق اوکراین بدون شلوار حین دسشویی کردن گیر اورده و افتاده دنبالش
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67357" target="_blank">📅 23:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67356">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twS1fefRDED55WkkOJg14W-9TM9td0cxpl0T2l9-M1wDAhvIg5h_PJqsywb-suyNLklcbOKIBIpMMNqVuuL0-VQwF-JaKswbMD8ptYcXmpp_nOBT9xbzmEUUkOtiY1wYFLu5DxgxGJrJdmyfD1FIQlelxeaJ0USc7BDR2lYkU572HmpIqnB7Aby8N-EnN0hfTTue0odDP9hvzAVRrVpwkvtOVum5n27WUnhPNMe2tReEm_R45J5UlUg2zEkK_xaog-uxqM-KP3_dOa1CcvgcZMh2aEe2188m6idlGBKiVK6sKpf8y8VyoXq3JEULOaqjj1sKU-TZu2uNHNIixcwGGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سنتکام:
یک چترباز ارتش ایالات متحده اعزام به خاورمیانه، آموزش تیراندازی انجام می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67356" target="_blank">📅 23:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67355">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb140a8f9.mp4?token=fEGX-cS2HSSKCE32z3DQoz9jVD_WAcQkSgbWE-SaIl2v7jNBBoQS7v7tTByCaLn4RfbaaCuP1WuSQaIOu-CSSWo_Ly8Aye72yArH0cV51fBI4r7kW5Kh9FlUBVtOkBm7AvhcGwsAIEeUOy3ytTWbaE1Kf9PL-I4z2NEbg4XHGofOnoqp7LBN9cX610GT9BpI1MjnGbKwlGZYLFZ43m-QrbxonvwH0Soedobg1O7Ua85ylD0o6BcLraQ99efA1wntLYmVSOr-PYt68vI9iR3V6F5MVI2yeBAbpAaqZa-T2etg-TVGSp6ppsVk1CdjoVsgjiMdJabvVrDqPc6tFeOtJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb140a8f9.mp4?token=fEGX-cS2HSSKCE32z3DQoz9jVD_WAcQkSgbWE-SaIl2v7jNBBoQS7v7tTByCaLn4RfbaaCuP1WuSQaIOu-CSSWo_Ly8Aye72yArH0cV51fBI4r7kW5Kh9FlUBVtOkBm7AvhcGwsAIEeUOy3ytTWbaE1Kf9PL-I4z2NEbg4XHGofOnoqp7LBN9cX610GT9BpI1MjnGbKwlGZYLFZ43m-QrbxonvwH0Soedobg1O7Ua85ylD0o6BcLraQ99efA1wntLYmVSOr-PYt68vI9iR3V6F5MVI2yeBAbpAaqZa-T2etg-TVGSp6ppsVk1CdjoVsgjiMdJabvVrDqPc6tFeOtJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خایه کنین؛ توی اردبیل چند تا آقا نشستن با یه خرس نون و پنیر میخورن
🗿
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/67355" target="_blank">📅 22:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67353">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWjkhGDwvDJ11HT8-24EzBGNmwSHuz5DZ6Ip8NcPhjurrrBJssqCcXwB09SN7yP1NxzfiZLD8pOi0uKwPcAA6qDCDkdbB6srs58pyKL5MD2GTKt8OAY_REuIcqamGc5kEqjAo3qluYVFkuCCMgZzst8Mei_V9docUxKU0YL3V8AnF89Q1nritJxxkERO8uqVJX_NIrNnTQb7clU4KB53_o-9fB1KU4vkUjMyO4xx--1_ysieU3iuCoTEnQzeopvNMwY2pqeZBhgY38SB0U3wKIl0NzaC2lpPmgQ75-A4xjk5S_6VIgk4WMLMbCaqiaCP02PiiuMcA7t5GfMQf0qyrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسرائیل به فارسی:
مثل اینکه مجتبی هم بوده
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67353" target="_blank">📅 22:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67352">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=KrnvJepFHIrNsiBgs-vhtVGTSr3sYBJQeaNdkyKuSnXjC6qUzXOBDHptOi_WuGQG_dOgowcSbz0BrMJSrMaxBdUrQZL8F24Z0RgeYGadOPx2eXHRBetbfQY6E1ZKOc7j7JcfeN8sL-qFkTWo75gcoe_faLtMy3Y1LBJTe0h3JsfQw_kys38hGmKG4GGa-rNaIu1HQL0H-1d1iZEKH8EXH-s5jgu1aVYZfHqER7_SXVyZXIpfvZthp5XUZtvS5x9SxCHHR3In87BSLSGzBJdcGGlkvDNIW71RkzmFv9JkQ96zbLYTHwI6rJbYwUJ2bP95VocPm2_9Zar_DEFDDeR2fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=KrnvJepFHIrNsiBgs-vhtVGTSr3sYBJQeaNdkyKuSnXjC6qUzXOBDHptOi_WuGQG_dOgowcSbz0BrMJSrMaxBdUrQZL8F24Z0RgeYGadOPx2eXHRBetbfQY6E1ZKOc7j7JcfeN8sL-qFkTWo75gcoe_faLtMy3Y1LBJTe0h3JsfQw_kys38hGmKG4GGa-rNaIu1HQL0H-1d1iZEKH8EXH-s5jgu1aVYZfHqER7_SXVyZXIpfvZthp5XUZtvS5x9SxCHHR3In87BSLSGzBJdcGGlkvDNIW71RkzmFv9JkQ96zbLYTHwI6rJbYwUJ2bP95VocPm2_9Zar_DEFDDeR2fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمزه صفوی :
یکی از گرون‌ترین سیستم‌های حفاظت در بین رهبران جهان مربوط به علی خامنه‌ای بود، اما نتونستیم اونو حفاظت و پنهان کنیم و از دستش دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67352" target="_blank">📅 21:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67351">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
ترامپ:  از فیفا برای انجام کار درست و جبران یک بی‌عدالتی بزرگ سپاسگزارم!  @News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67351" target="_blank">📅 21:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67350">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOtn4cfjJrcExy3mR8liXemehIysyVdhgQdR-GT-GhNe6tpURwDrSjQ1NnwMU41Na-F3UYlqT1nJSeekN8Mlw4x3oN5540Ajw2RT3qvnHIoGnYHiDoiUpBe3bkvbVvgUHPJ-k29XzaY8NW0RjPRp5rKzsZJC7jdr_7QgWQeSrv-RLkRUUD987YBLByU0-YPBeSwwlXA5wdaTrzZxtYRQx5xeBQFM7U0b3i-RAMr1qUDwFCDhBBi775UzmtBil4UcMn_bBeMtFuuipf7l2IgO9YUEqH7rDiGG26k7sO-kObPaA1SOgQ3K20YTNbkH91pKVUBqvfUtn--ZklZohDca4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ:
از فیفا برای انجام کار درست و جبران یک بی‌عدالتی بزرگ سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67350" target="_blank">📅 21:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67349">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d12e972bb.mp4?token=Qi62q07BDtRrREN0dTZkJ9JtjC2UiBb7J-aemF46JL611LUC7UsRMNA9DR6ySAULDDeaCoYZIjtG6D5hHe52znNZmXgyK43mtKaEqxB8c5vB9aFwkbdZLXcl1ePQ2_H3TDDIQ7f9nYxXzb4bXP024l25qMoBoz8881JM0cGtpO2jXo2WQQERx_LOFpaNmU08bnCSQ8QBK7qyQ9lD1lL_csBCEqsg9fiIopbjq-1eK3scCg6sJTz7_vBve70QCFzswcHnYq53N9fSjs2UvLRNKMTpodpmVHv-V-e6YOxTqEHuyPXuq3f-wmr_cUDcrkqBfqT0QBARUct8rMLtpnCzJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d12e972bb.mp4?token=Qi62q07BDtRrREN0dTZkJ9JtjC2UiBb7J-aemF46JL611LUC7UsRMNA9DR6ySAULDDeaCoYZIjtG6D5hHe52znNZmXgyK43mtKaEqxB8c5vB9aFwkbdZLXcl1ePQ2_H3TDDIQ7f9nYxXzb4bXP024l25qMoBoz8881JM0cGtpO2jXo2WQQERx_LOFpaNmU08bnCSQ8QBK7qyQ9lD1lL_csBCEqsg9fiIopbjq-1eK3scCg6sJTz7_vBve70QCFzswcHnYq53N9fSjs2UvLRNKMTpodpmVHv-V-e6YOxTqEHuyPXuq3f-wmr_cUDcrkqBfqT0QBARUct8rMLtpnCzJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد مخبر مشاور علی خامنه‌ای:
قاتلان امام شهید به مرگ طبیعی نخواهند مرد و نظام آنها را به قتل خواهد رساند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67349" target="_blank">📅 20:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67348">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5503b743a2.mp4?token=FZs0a-cW5l0k0CTE_ynGsFSsSCQyI18cHXAgYePIRAR01zOmW1gq8w3PB_8i2_0IfPWoGzvsZ5CSpfXyZALMXvWcr6MwRufah2xi67vzBjOU7GGu1x-IL7VCkfgIfVH9wL7hh5KmPeT3nh7Ppu16V9NmQgPY6h4SaEscBk6a5-E-1fCZ05G6zYy3ZAsweGrVluQ_BJPATCI1D9QVJrQ9UKu8nGrPMqKprpujxIfhTLtsHXoQBw1CDnjLMBbDk5RVnWnUqQp5OCdeAQifJtmvpsUFqhIouXbrdsUHBi2zcUHm7lNUT_KyEnxm83ym9mLkIc3biWrCxA6aH7J1rgSKag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5503b743a2.mp4?token=FZs0a-cW5l0k0CTE_ynGsFSsSCQyI18cHXAgYePIRAR01zOmW1gq8w3PB_8i2_0IfPWoGzvsZ5CSpfXyZALMXvWcr6MwRufah2xi67vzBjOU7GGu1x-IL7VCkfgIfVH9wL7hh5KmPeT3nh7Ppu16V9NmQgPY6h4SaEscBk6a5-E-1fCZ05G6zYy3ZAsweGrVluQ_BJPATCI1D9QVJrQ9UKu8nGrPMqKprpujxIfhTLtsHXoQBw1CDnjLMBbDk5RVnWnUqQp5OCdeAQifJtmvpsUFqhIouXbrdsUHBi2zcUHm7lNUT_KyEnxm83ym9mLkIc3biWrCxA6aH7J1rgSKag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
قول میدم راه امام شهید رو ادامه بدم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67348" target="_blank">📅 20:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67345">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lIUdAZNwSOG21lpRrIniPO1dIchgdTWOUl557TawMFZDkjoJeCZ1Dqe8KrqnhJ7cOljSQkSyAYogHaI-ZjUCEkaq-xLlCnIauZ-Xw27ClM133QFB0tUO0KSNhNdJMVCwyGEf0n6Us-ukdiqqC0-DyAYMXICUVTYQZPXZBDfuHB_0g-vVxScDm4e1mE4CvB2Gwr2bfprRqwPquPywPnBj2k1aBp_ezH_UCad2Mchf3xWbfOR87KFxV_yRABAl8Ntdbr4gQXVVehi3TAMLyzAZ6NC7rQPdisgdkrj_c0USqAg2YHuO3yMyoq_18NVxBTU2I97T7QBlcr0zjQSso_9KnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kcLka_1OkqWfaP7Dwc-WNEL1Q99KbsJWwUWC8mls24WiPOJjxYp5DD2CpVt1VY5Kf7VPZub-VOtWrPJGEQGrVmXXBFYohxYreOYjvWdzVYqkEf59TWWr1XTOLNhh8iE2ALB2NIi2GDxaHEi6EkZnxN4CxqE9zhSnOOak0Ct7KLFtWAjmmC0cihH67TWWNoVsSEgQ8Kr-VPtgszOHlEtuu8MDHxOeURxx9YEN2WdwHwTKDn2ErQbutwI1kSal3FYIvM2XDtmFX4O05MVoH1nGpRQ6EnBu2_exbCOFwS_W0CuOW6hGa5nHOF-KE0q4ZPP3Ij9-wwjXXuZC5K2EIm2mKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a975887416.mp4?token=q5fubZlMrEjnGtBBqWjhJbWmCZaVa1cH5SBeMReAGUJBnEcJMNAE0asp1BUiPLJxc4dmcAPormALTbUIfObqYeg06Yohk2mFPBRR9oO5Gz2kORzmueoVdDWmrtyB_vah09lA2DqfMApee-o59vhio8xEY6NGJiL3VnWnFLq0RFiRBIyok49BgA4A8g0uqPplRaQM6G2fvs9FDDKypctVxJLeZKm7xUpPRV-Dlg61UlQf3OmCQD0a0ix78SBHwR_nwCYaHT8AhOU4-lLxQPYTi2Zpf1Wg77uX5u3JbUBtSc06Pg7yinimkVhqvg7cgm0R2mV0iKX1-P2gQXeFTnFD7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a975887416.mp4?token=q5fubZlMrEjnGtBBqWjhJbWmCZaVa1cH5SBeMReAGUJBnEcJMNAE0asp1BUiPLJxc4dmcAPormALTbUIfObqYeg06Yohk2mFPBRR9oO5Gz2kORzmueoVdDWmrtyB_vah09lA2DqfMApee-o59vhio8xEY6NGJiL3VnWnFLq0RFiRBIyok49BgA4A8g0uqPplRaQM6G2fvs9FDDKypctVxJLeZKm7xUpPRV-Dlg61UlQf3OmCQD0a0ix78SBHwR_nwCYaHT8AhOU4-lLxQPYTi2Zpf1Wg77uX5u3JbUBtSc06Pg7yinimkVhqvg7cgm0R2mV0iKX1-P2gQXeFTnFD7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
حملات ارتش اسرائیل به نبطیه الفوقا در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67345" target="_blank">📅 19:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67344">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4c05c580.mp4?token=Tqqybg7wZFniC5CxexO11V5KpvuE2QQckqrbH5N7QqqEemORTLna2aFK8QQV-ktNg9Qx_kXJcmZZBwXJmZ3bGbGM-pmP6UjVUAEz1XOZvUMd3jcyWc53nLwG5DhQFROCLWBXH_pF68DiQ-zBW6GNY0EQsJ0EFCh8nhJCdGxCib6P18iv89pb_aGNG476JoY0uKJDQF7IEOGJOtLJ2Cm2Q_XFoHvb6KIRkdpMj4CzCG8E6uo6cNof1K8qAgdj5PLlo2cqkOCa587KcL5vuorhzwbO9xe_srSSjV2sbVMa1jy_fEXtqj0khq0rirNVM7O2NKQm34KUY5XahVRsJW1AdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4c05c580.mp4?token=Tqqybg7wZFniC5CxexO11V5KpvuE2QQckqrbH5N7QqqEemORTLna2aFK8QQV-ktNg9Qx_kXJcmZZBwXJmZ3bGbGM-pmP6UjVUAEz1XOZvUMd3jcyWc53nLwG5DhQFROCLWBXH_pF68DiQ-zBW6GNY0EQsJ0EFCh8nhJCdGxCib6P18iv89pb_aGNG476JoY0uKJDQF7IEOGJOtLJ2Cm2Q_XFoHvb6KIRkdpMj4CzCG8E6uo6cNof1K8qAgdj5PLlo2cqkOCa587KcL5vuorhzwbO9xe_srSSjV2sbVMa1jy_fEXtqj0khq0rirNVM7O2NKQm34KUY5XahVRsJW1AdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
ما در وضعیت دائمی جنگ نیستیم.
من خودم، به همراه رئیس‌جمهور ترامپ، چهار توافق صلح را به پیش بردیم.
تنها مسیحیان لبنان نیستند که از ما درخواست حفاظت می‌کنند.
دروزی‌ها هستند، مسلمانان هستند، مسلمانان سنی هستند و حتی تعدادی از مسلمانان شیعه نیز همین‌طور.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67344" target="_blank">📅 19:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67343">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a4244b191.mp4?token=apunJWBhy2iH3lEZWgnkk6YNf1ULiKn3_fv-BGD5LvUkDT41Zt3NDxjsD1JeArzchjQqq1wu4Z_w7nw8-WWlumuassreGlR5TGlTec6wifF6FZMr3Cafb8Nvof_TjO1hqDqERvQ3tWrdkEsNaTc-CLU8Dq0eAAsfoCTdi3dj8KWFHjyVE6xMJ3hPJ_lep3BcxtkRyMKQcr7Apowcdt953GiTGGdbekKy90jv8zHEh5KePWRMaZzSjVtUI5EatTimWn50M6MeItqzJV2ZViaa3qH2dG61ZWHe68015VefCNKDTMyC9UXMJ0ftmbckgEnQWwoAcV4gc5INvEKjVcFjGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a4244b191.mp4?token=apunJWBhy2iH3lEZWgnkk6YNf1ULiKn3_fv-BGD5LvUkDT41Zt3NDxjsD1JeArzchjQqq1wu4Z_w7nw8-WWlumuassreGlR5TGlTec6wifF6FZMr3Cafb8Nvof_TjO1hqDqERvQ3tWrdkEsNaTc-CLU8Dq0eAAsfoCTdi3dj8KWFHjyVE6xMJ3hPJ_lep3BcxtkRyMKQcr7Apowcdt953GiTGGdbekKy90jv8zHEh5KePWRMaZzSjVtUI5EatTimWn50M6MeItqzJV2ZViaa3qH2dG61ZWHe68015VefCNKDTMyC9UXMJ0ftmbckgEnQWwoAcV4gc5INvEKjVcFjGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
روستاهای مسیحی در لبنان...
برخی از آن‌ها در واقع درخواست الحاق به اسرائیل را داده‌اند زیرا ما آن‌ها را در برابر حزب‌الله محافظت می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67343" target="_blank">📅 19:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67341">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd048f948.mp4?token=o1CkL3ikf1gqGQFuaMWkJh15gQNJzbXMNJf2tCdUO5gWPVn2gQxkBBNWOXoL6sHRDsX77t8QjPDb9LFmq58A0OVXchRxplYMFxp6ZGvfXjLg_pyltO1kSBo2DS-lOWKICg1IJAwTorqfBNJXyJn1JQEAjUUgQ2WzFinLOgeqVOVsVeTti7ykAlp-zhTfLSyjb1TBsXFIchuiPz-ySiNVT8MQpjpsGJj1e82ZZGY8QWppSgAYQChAE79cWev_oMfuhpqK6_YiGoZf1nlnfJDbSNpE0Uwb9mxe2xtWpI7OLFHvpKEnKdPqy2Jj4pNQfnYPadVS15g1RcRa1KtoxQ1ZEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd048f948.mp4?token=o1CkL3ikf1gqGQFuaMWkJh15gQNJzbXMNJf2tCdUO5gWPVn2gQxkBBNWOXoL6sHRDsX77t8QjPDb9LFmq58A0OVXchRxplYMFxp6ZGvfXjLg_pyltO1kSBo2DS-lOWKICg1IJAwTorqfBNJXyJn1JQEAjUUgQ2WzFinLOgeqVOVsVeTti7ykAlp-zhTfLSyjb1TBsXFIchuiPz-ySiNVT8MQpjpsGJj1e82ZZGY8QWppSgAYQChAE79cWev_oMfuhpqK6_YiGoZf1nlnfJDbSNpE0Uwb9mxe2xtWpI7OLFHvpKEnKdPqy2Jj4pNQfnYPadVS15g1RcRa1KtoxQ1ZEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار تسنیم : نظرتون درباره رهبری مجتبی چیه؟
🔴
زن عرزشی : چی بگم؟! نمی‌دونم ما که همه منتظر بودیم مجتبی حداقل برای تشییع جنازه پدرش بیاد و حضوری باهامون صحبت کنه، ولی بازم نیومد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67341" target="_blank">📅 18:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67340">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c05464482.mp4?token=Eg48GJGZbBH-pC5P35AsUDnexc5ecrePMOP9sLoaiNuKpWaOD3nrq5gbA8j1o79VbuAb5LGolCCs7eBUotI8m8ByVOM7IKj1ALsE_PDgjEqpPHzX4FDeWSf0huT_eSjzn-IAhr_UkOQGuy7QKEE6MX9EHIsniByqJCEWl_UV5cybXmO9c9-Nc-BY6Gc6zkaYVBR-Do2YnUJTAAy8eJRiU1CLdpLL4ZkWy7Ec1MCUPDyWBJ7ec_CBSKBZD4iZhbI0FtQBAIHwvWqJ6LPt7sPo_e8B3Woc68gWC5xyMhivn3T9jXfkMSJrUh8JaL6mRqt-pq5CD4_d45LfCfMjgVnk3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c05464482.mp4?token=Eg48GJGZbBH-pC5P35AsUDnexc5ecrePMOP9sLoaiNuKpWaOD3nrq5gbA8j1o79VbuAb5LGolCCs7eBUotI8m8ByVOM7IKj1ALsE_PDgjEqpPHzX4FDeWSf0huT_eSjzn-IAhr_UkOQGuy7QKEE6MX9EHIsniByqJCEWl_UV5cybXmO9c9-Nc-BY6Gc6zkaYVBR-Do2YnUJTAAy8eJRiU1CLdpLL4ZkWy7Ec1MCUPDyWBJ7ec_CBSKBZD4iZhbI0FtQBAIHwvWqJ6LPt7sPo_e8B3Woc68gWC5xyMhivn3T9jXfkMSJrUh8JaL6mRqt-pq5CD4_d45LfCfMjgVnk3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زینب سلیمانی:
شهادت آقا برای ما سنگین‌تر از شهادت حاج قاسم بود
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67340" target="_blank">📅 18:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67339">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjMIIXvPEP083csFfzkZhCBe-L6a0LZOYN48_0X6Fd1BGlkEvOqxTqZ6osUgHheKc_5Vcs_4Uv2-gFi_R6J8RnUPSK-0_VRQcZch3DTXQXkvexLm7zKzhEoLePHeF4Tyas9Y4AO8KSageSfbcec660-LQltnYRngoaIOL6M2_JenwZQ1WaH6eQQBPyxXN_rMMbHLQHd3LmE-LKpNZDw5yGISgeGKzaHMV9mmvuqPGei5sb3wMb2EeM0nFmi3BoGy7OWcsZopd8VkeD8XaLwFHDFEjv3CDF0bKD_W4ckfnEuACMyRVXphuEkbZagv8iA38as2bRfezPA2d06lfA68zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دفتر شاهزاده رضا پهلوی:
🔴
‏تلویزیون بی‌بی‌سی فارسی در صفحات رسمی خود، با انتشار بخش‌هایی تقطیع‌شده از گفت‌وگوی شاهزاده رضا پهلوی، تصویری نادرست و گمراه‌کننده از اظهارات ایشان ارائه کرده است. تیتر و متن این پست، با اتکا به نقل‌قول‌هایی ناقص که پیش‌تر نیز توسط رسانه‌ها و حساب‌های وابسته به جمهوری اسلامی برای تحریف سخنان ایشان بازنشر شده بود، به‌گونه‌ای تنظیم شده که به مخاطب این برداشت نادرست را القا می‌کند که شاهزاده رضا پهلوی آغاز جنگ یا تصمیم به حمله را به سفر خود به اسرائیل نسبت داده‌اند. برداشتی که هیچ نسبتی با محتوای کامل گفت‌وگو ندارد.
🔴
آنچه شاهزاده رضا پهلوی تصریح کرده‌اند، این است که سفر ایشان به اسرائیل، در کنار تلاش‌های گسترده میلیون‌ها ایرانی، به روشن‌تر شدن این واقعیت برای افکار عمومی جهان کمک کرد که مردم ایران دشمن جهان آزاد نیستند، و از این رو دنیا در برخورد با جمهوری اسلامی باید حساب مردم ایران را از این رژیم جدا کند. اینکه مسئول اصلی بحران، جنگ و بی‌ثباتی در ایران و منطقه، جمهوری اسلامی است. ایشان همچنین بارها تأکید کرده‌اند که هدفشان پیروزی مبارزه ملت ایران با کمترین هزینه انسانی ممکن است. چنان‌که در همین گفت‌وگو نیز تصریح کردند: «تمام هدف من این است که این مبارزه با کمترین تلفات جانی به نتیجه برسد… هر انسانی که جانش را از دست بدهد برای من واقعاً دردناک است.»
🔴
این‌گونه رفتارهای غیرحرفه‌ای و تحریف‌های آشکار از سوی بی‌بی‌سی فارسی در حالی صورت می‌گیرد که چندی پیش، مدیرعامل کل بنگاه رسانه‌ای بی‌بی‌سی و رئیس بخش خبر این سازمان به دلیل رسواییِ دستکاری، جرح‌وتعدیل و ادیت مغرضانه سخنان و مصاحبه‌ها ناچار به استعفا شدند. از رسانه‌ای که هزینه آن از مالیات شهروندان بریتانیایی تأمین می‌شود و با وجود ادعای راستی‌آزمایی، به دلیل نقض مکرر استانداردهای بی‌طرفی با بحران جدی اعتبار مواجه است، انتظار می‌رود فوراً نسبت به اصلاح این گزارش مغرضانه اقدام کرده و سخنان شاهزاده رضا پهلوی را به طور دقیق و امانت‌دارانه منعکس نماید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67339" target="_blank">📅 17:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67338">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d7e9ec8c8.mp4?token=j3Y-dqVnjRKRVb0p9M3xYX1DCCNhNf4VZvrwJ71uzvN30JdefmHPRjiG6qnzcJ7q2HevS0tJse6qJOOH2lqDIVz0ANPd1GXNwAoEObqA82bZtbqhms_CloAL4i64X20b0puIOcalC7dcX3lOWFOawvRO65AusO47aaegWAUEs-nBPBMOMkzHe2OIEWzhQwYI2abvykIN2bpXLx6NoYEqWBOv6Yiupmx04jhHsrDUH6lt0-Tbjez5qBXyscOeKixNovalh3emKejgDuzQXKKdXXWbUayK4tX1zvOJVKHEvYc4vpEWMEIkQtYQJUPWRfbuFXfLS6P-c5Xe7T0O9xUucQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d7e9ec8c8.mp4?token=j3Y-dqVnjRKRVb0p9M3xYX1DCCNhNf4VZvrwJ71uzvN30JdefmHPRjiG6qnzcJ7q2HevS0tJse6qJOOH2lqDIVz0ANPd1GXNwAoEObqA82bZtbqhms_CloAL4i64X20b0puIOcalC7dcX3lOWFOawvRO65AusO47aaegWAUEs-nBPBMOMkzHe2OIEWzhQwYI2abvykIN2bpXLx6NoYEqWBOv6Yiupmx04jhHsrDUH6lt0-Tbjez5qBXyscOeKixNovalh3emKejgDuzQXKKdXXWbUayK4tX1zvOJVKHEvYc4vpEWMEIkQtYQJUPWRfbuFXfLS6P-c5Xe7T0O9xUucQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بزرگترین آتش بازی تاریخ آمریکا در واشنگتن دی سی به مناسبت ۴ جولای روز استقلال آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67338" target="_blank">📅 17:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67337">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNUvB5oDER4Dmz0WJqZeg7gU0zBNX1xx_Rws0UuBJo-YkL-XpdmYvmj-4NlJpu4glh40-mrtqnjXtmxIK9oKbENuFfghsCZyRDz80RPYpgkzKqWye5gYc042au3ddFt_k3onq3bQozLBsSHDCuwgSoYi0oYbDYleuPQYLG4Y-vDmgAUMdwByZdXMt4F1md4vC0jE7ipoJ4wzdIOABtetdzUumz_iygdps6zr7vd2XpdXvIjbA-Q-vkrNl41av-ZfKg773f3Ny9bixtC24KbVYelDxi_-4143bn2LFc1XwMtetkhWdJEeyTvp-icFrYEkZyowcHDG_7uIf5YE-Rl_3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
تنها دلیلی که ما امروز تشییع جنازه خامنه‌ای را بمباران نکردیم آن است که 10 هزار مأمور موساد در میان آنان داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67337" target="_blank">📅 16:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67336">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e644784ac.mp4?token=uCwex1Y6X3hfOacrbXTeidjnmaWclGdhgKFhyOoDPdqYtPzi3rfKOqUMnPR8yGl-AgTYsV--WMGwwuPo2XuzNf6m7-Bo_fNDrYOeUdSm0ewseFv3tqu5E3mSpr_IMVtVeNwOgYB708zKPHfNuVZjYBskciJ1CZdK3DlfrUFEOSjQOPsKsFr-5McIfmDr0K80ijK1h6W4LVCIoARU1PHeJdQ1SRDtNPrHMJCaZg1rqPvvtQt9W_k7TtZ5KvtKuZL01xUW0aod8C29yXv-m-gOp2T5CVD60O4uXJhYBc3aYLOP379SPBcFLhK8Mqtj3feot8hZ-VSny1tPlBxfPPO0SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e644784ac.mp4?token=uCwex1Y6X3hfOacrbXTeidjnmaWclGdhgKFhyOoDPdqYtPzi3rfKOqUMnPR8yGl-AgTYsV--WMGwwuPo2XuzNf6m7-Bo_fNDrYOeUdSm0ewseFv3tqu5E3mSpr_IMVtVeNwOgYB708zKPHfNuVZjYBskciJ1CZdK3DlfrUFEOSjQOPsKsFr-5McIfmDr0K80ijK1h6W4LVCIoARU1PHeJdQ1SRDtNPrHMJCaZg1rqPvvtQt9W_k7TtZ5KvtKuZL01xUW0aod8C29yXv-m-gOp2T5CVD60O4uXJhYBc3aYLOP379SPBcFLhK8Mqtj3feot8hZ-VSny1tPlBxfPPO0SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اگه اهل دعواهای خیابونی هستی، این ویدیو از استاد طِقه زنی رو تا آخر ببین تا به امید خدا پیروز میدان نبرد بشی؛
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67336" target="_blank">📅 16:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67335">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67335" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67335" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67334">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67334" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67333">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0GITYIQt6CXmugxBrmLF1mnazwx8F-G9EQeCrc1lqk0r8S-R-wN0F4PmzehlboXqd-4E2be_LMbvOrgGigvis4wdrTVFYICchM3UoL2TivHlYvlDeHqOGIq4z5sVwPy2wSRhMXA13qKzeBoP21bQrC6vxlIy6Z0UNL05K7KjWzoBQRwNuM1nr2BhhTUszQe66FkPMbdvGVzLTJk-1n9z3Jm7A4l7V1Tk38M-zTbtzjp0oeP6PKPwK-A98OekmTdUzs-TeV7JTF-ZtlIsg5ZiCiaes6FjpYlImTH7Ph08PLgxdyaMThumwCZQZ1QQzd8tww2NifbLE-QgU-qX21zoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گویا کامیون حمل جنازه علی خامنه‌ای مبلغ2,298,000 هزار تومان خلافی داره
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67333" target="_blank">📅 16:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67332">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYMC3_YGsmVYQD3qvwhfU2NyGMu13RS_lUzSE4hE6bqujiKuSaX6tzJL81FZx59e_adaTBa-HWnZDBfCnWvlRzJ6wTTzDQLzkh1IC1J6W-rPDTPdEQS3a1HTdmkZCnOa5IVz1XZ_VJ8-vaTOQaWdHnqRlmFbYBMc0dVjTnsvz9Fo0efSylpjXn180N1PNz3vD_eTAMaKyXsqjpjP6E6fXEo2uYMDDq1kZfvsrb3-I0NALW7p6A_hfj7Eb-qh0yb9zzpsh3Shzus_pHScm7katMU4wQnWIVU8YNglkbay85uh42bBI8ECHxXEJmYIC0JF8Y_W6c6aCQJ-RgTr7yZCUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
محمد اکرمی‌نیا سخنگوی ارتش:
«هرگونه اشتباهی از سوی دشمن، با پاسخ قاطع نیروهای مسلح ایران مواجه خواهد شد. ما بارها اعلام کرده‌ایم که از فرصت آتش‌بس برای ارتقای توانمندی‌های رزمی خود بهره می‌بریم. ما حتی یک لحظه را هم هدر نمی‌دهیم و تمرکز خود را از این مأموریت برنمی‌داریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67332" target="_blank">📅 15:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67331">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو در جلسه دولت:
شنیدم در رسانه‌ها گفته شده که رئیس‌جمهور ترامپ خواسته علیه تونل‌های تروریستی در لبنان اقدامی انجام نشود. این یک افسانه و خبر جعلی است.
او حتی یک کلمه هم در این باره به من نگفت و من هم از او چیزی نپرسیدم. ما بر اساس ملاحظات و تصمیمات خودمان عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67331" target="_blank">📅 15:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67330">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-eEmKLvlKBPV3eQbbGOrjkR2ljejTuff8Vpcrv2sIf4KtDZEv1iz3ghCw1NDzC0jT6gQZs_itnoC2cMmAxQqi2F28vpEoWPhI6DW4md3KUflxQUzQVb4NkspKgndpIVh2BxyxHdqHQlpCbYWyLCpHKSGUJAil0RVaoDSMESgt2EYtlDf0UYuP1EDcOeIzq1JB9W2ZJyA3oOXaahOx2ZNTpZNjwZUAXKt6qCDYY9BCvlSH18M2kiQg1X2PkTRN-6-u2J0vpcEPJhmSIsaaZoe062c5H3Zvadml8WVFXQR19Uqq6tZBCTAlOyChjOhmd50jDKaE0MrT05SR1RoCynEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویر ترامپ در مراسم وداع با جنازه علی خامنه‌ای که روش نوشته شده:
خواهیم دید چه می شود
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67330" target="_blank">📅 14:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67329">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpv_ItQf55AB6ccjO5fym1YLFtDmuFOGlve2hP7h_Sdgnv5QPHtBUalJPcLXl_GsOwZeKMYjra22BEMx-FQqQ66Kl7Yq7o1cxGQEsD8RPNiiB-H4slLCJNHabZAN8ah6Hf4glDSKMp9iZBMrh2pt5ZhPSn9z0uLbXuCTleVT__oov1uMf_-Fg1n7Q0w-po8ihJfmEFTsceqviWC_y0HH3oq6bhyU5D1DovU0QoLf1UQyoHjBULcsweGvqrRGby90wpzoz-ihJa7DtEQqd_By_cNMBH2VmTDuRFmRyTryhptvgx3ICnU7ImU0R27kvsD_dHtv_YyF_l-alBq3jPWU_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسرائیل به فارسی:
بهرام که گور میگرفتی همه عمر
دیدی که چگونه گور بهرام گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67329" target="_blank">📅 14:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67328">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=dOUr3wdWgx05m2OAAtbtrxwoAegZYh9lG-Jtlb5sVe-afrYxSBueHybjD0Y1oLH26zJ71SPC0vTnmQI0JfKomFYXiDIL9aqHPB-nENtVMDzIQP6iKrLNLH8zgQdMpw9RDhPybZGYTr5T6BMq2vJPthecZj0CR6LfQhgyDLr3yHdfMYN171WXhryQHw6bqXun10C2S9_FfRsJoFoqHrFP2On6roUBlfubVnmdXNwszLRkSuf43vLYTSoMDlBgjjxB1B_zAhv2JOoywJJ-CHU7B26hiKgivL4W6AK58erQbloyI5kNlIW_u_tGNN3JyvieEP6Kb-VR63zcSchuV3DnBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=dOUr3wdWgx05m2OAAtbtrxwoAegZYh9lG-Jtlb5sVe-afrYxSBueHybjD0Y1oLH26zJ71SPC0vTnmQI0JfKomFYXiDIL9aqHPB-nENtVMDzIQP6iKrLNLH8zgQdMpw9RDhPybZGYTr5T6BMq2vJPthecZj0CR6LfQhgyDLr3yHdfMYN171WXhryQHw6bqXun10C2S9_FfRsJoFoqHrFP2On6roUBlfubVnmdXNwszLRkSuf43vLYTSoMDlBgjjxB1B_zAhv2JOoywJJ-CHU7B26hiKgivL4W6AK58erQbloyI5kNlIW_u_tGNN3JyvieEP6Kb-VR63zcSchuV3DnBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این بزرگوار که قبلا گفته بود بخاطر یه تیکه نون به سگ دادم اومده داره ترامپو تهدید میکنه میگه بیا کوت عبدالله ببین چیکارت میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67328" target="_blank">📅 13:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67327">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
❌
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
تنها دلیلی که ما امروز تشییع جنازه خامنه‌ای را بمباران نکردیم آن است که 10 هزار مأمور موساد در میان آنان داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67327" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67326">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0be756a04.mp4?token=lwsr3_hSFEE6MhvICoRpB8sLJMpYKMTm8PnxVYwDGkr7rnl7NeZ8nFP7Nj5JxiYqW-EFvUvGjcGO_ax8z_w6iY-5undlpLmIkeW7eq3jUQ0CVSsOJoZZERfdFgCX_guM3bK57jzP_DO6G5h8vUy6E1fXbbqR8a3QoUA6hUUeimWUZ91_FzBmVHhsUdzfEEB3mdNCeR0sfoFlRqB5sTo_WJPB6A9ePuHPM_RIIw1pEVFnABOGCVIxjbCZYvffWny7n92wArfERFGoOD7z2Usoq8GqdZNVOLgObPBe36cN9PlG1pJV5owfdefTaUAlzQ9YeceuWaaBrRS9OjW9fHyOEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0be756a04.mp4?token=lwsr3_hSFEE6MhvICoRpB8sLJMpYKMTm8PnxVYwDGkr7rnl7NeZ8nFP7Nj5JxiYqW-EFvUvGjcGO_ax8z_w6iY-5undlpLmIkeW7eq3jUQ0CVSsOJoZZERfdFgCX_guM3bK57jzP_DO6G5h8vUy6E1fXbbqR8a3QoUA6hUUeimWUZ91_FzBmVHhsUdzfEEB3mdNCeR0sfoFlRqB5sTo_WJPB6A9ePuHPM_RIIw1pEVFnABOGCVIxjbCZYvffWny7n92wArfERFGoOD7z2Usoq8GqdZNVOLgObPBe36cN9PlG1pJV5owfdefTaUAlzQ9YeceuWaaBrRS9OjW9fHyOEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جمهوری اسلامی پس از ۴۷ سال در مهم‌ترین رژه‌ی خود حتی به‌اندازه‌ی بند پوتین‌های ارتش شاهنشاهی هم نظم نداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67326" target="_blank">📅 12:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67325">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWGH5ATAgEYDkyTu-WPPI6fDSDfGrXgNGG06JjHa7jmIo1ddfpdJ57b3hQm4Nyo5_SRqS6_c7VKQpH1NHfRoXhh9zdB7uE0w-B_PgoMYe2W4u7F-a9G4A9_k6lazRUaheCbmdYleo419HZ0npfB6bHUZl6orwNuHUFkAmRe_Hl-DtBP987BsWQWsPlmAqPwipDzTAaF7An44jQo04h58Jo0l6qJDOB0hcVFhM_AIi7vpogLQj4J9eHWzusOpVvQIk9-peWATVD6jsmGZsNHptZDggnwEOAORFx8pkcPvKzkqH93lIZ8cKYL_htS47p5hYhaMG8oUEvs5xCjejHCf8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هرمزلتر:
🔴
نیروی دریایی سپاه با استفاده از قایق‌های تندرو، کریدور مورد حمایت آمریکا در تنگه هرمز را به طور کامل متوقف کرده و در نیم روز هیچ شناوری از این مسیر عبور نکرده
🔴
سپاه صبح امروز از طریق بی‌سیم به تمامی کشتی‌ ها هشدار داد و همزمان قایق‌های گشتی نیروهای ویژه را برای اعمال کنترل ایران بر تنگه هرمز مستقر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67325" target="_blank">📅 12:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67323">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrC1Txm8TvpiFnfWoEMeY8bORXwIvfVnaFdXoBboPMk-lohj5qF9LvQYhnja4_oPm8Y3NUqYOO_juS7Vo_7eN3FiGoi-ZA__pVRCg7ud5oA6c0nYc0x3ildEXok9d6_MMLG-K1AeXntML77Q19fIWp-h4OMe6KOiWkOYgs0B9GkZQNvlzbL6r78kHM3irxg2FBLCCG1Ih0hM9X_rdzcRvUuOyN7HJBdc9KQuj8-iY1HvaZiO1ecwpZLjkZvJ3WvSz2V8m58SUaV1jbTIbqwDCAU23hH-Ip0hUMWKf9RToF9WoAumkZLJ6YtZbOq_pn3PBEefIP5N7xk-1AsB2OoXyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=A8ckIqPW4UeEjzAh0WHYYsZOrpaH3iM5T4VxZV7H9O1EV1T6YJMgMHHHy3ING60QUT2T5w9Is6UaJExpS-iiLD3jua9OFcHVLPEQal3Si4tXZ3AIY74HH_z0Cc739N_ypIvwpBzpXhg9CJ8TQRAv1Q0d9MZYmzfyudTp1w2nqAQET50OvZ3oCQa5mt7wBSPQH7rSVS429lBgaKvP65a-j-ea4Qv-8BSkIOFAcJlNyRSqVzzgavfgIAsP4h8sFXmMMlx0mNmAJV0HtJkJe1-EgEVc52IZpGJMMNETw67Y_JqlisXrx_3cZ4RqR129OjNmm3PwSx036gqp4XtYW42oiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=A8ckIqPW4UeEjzAh0WHYYsZOrpaH3iM5T4VxZV7H9O1EV1T6YJMgMHHHy3ING60QUT2T5w9Is6UaJExpS-iiLD3jua9OFcHVLPEQal3Si4tXZ3AIY74HH_z0Cc739N_ypIvwpBzpXhg9CJ8TQRAv1Q0d9MZYmzfyudTp1w2nqAQET50OvZ3oCQa5mt7wBSPQH7rSVS429lBgaKvP65a-j-ea4Qv-8BSkIOFAcJlNyRSqVzzgavfgIAsP4h8sFXmMMlx0mNmAJV0HtJkJe1-EgEVc52IZpGJMMNETw67Y_JqlisXrx_3cZ4RqR129OjNmm3PwSx036gqp4XtYW42oiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
و بعد از چهار ماه همچنان عامل این جنایت و قاتل فرزندان ایران چال نشده و اجازه چال کردنش رو از قاتلش گرفتن!
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67323" target="_blank">📅 11:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67322">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=h7KntTHOb5omNXLNkupCiwb4Og1aE2WrOAXQNTSDm1JURCFGxcImL1EhUMlG9vwXcxi53HADKnKMBQ2NcXkMfYKurvj_y9VtvUertOE1Q23SkVC2mfc9Dj-FpDB325RqaijXrAGtNs9QsmsMLUgNPAv_pd1-bPkwPUiZN21IzevU-XNQ2aJK_md6q7s_8GgJbr8D7QCgHKbO2MZI0dv3dup2dPxkwM4VI3-02P4u1UsgL5owvTrXt7WT6QZ85eS4DCL1K8-pnG-60RaNqiNfF5l9EewWOn91SjyxALFd1ylI496PL-TMJ3zzSOGZg6Xd5cbA5hp2JyUAIourR5MR4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=h7KntTHOb5omNXLNkupCiwb4Og1aE2WrOAXQNTSDm1JURCFGxcImL1EhUMlG9vwXcxi53HADKnKMBQ2NcXkMfYKurvj_y9VtvUertOE1Q23SkVC2mfc9Dj-FpDB325RqaijXrAGtNs9QsmsMLUgNPAv_pd1-bPkwPUiZN21IzevU-XNQ2aJK_md6q7s_8GgJbr8D7QCgHKbO2MZI0dv3dup2dPxkwM4VI3-02P4u1UsgL5owvTrXt7WT6QZ85eS4DCL1K8-pnG-60RaNqiNfF5l9EewWOn91SjyxALFd1ylI496PL-TMJ3zzSOGZg6Xd5cbA5hp2JyUAIourR5MR4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی رسولی  مداح بیت رهبری میگه برای خون‌خواهی اومدیم؛
شما هنوز خونخواهی سلیمانی و... رو نگرفتید بعد میخواید اینو بگیرید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67322" target="_blank">📅 11:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67321">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=LGMYsoDUBCnEJ27M1kRfSaJipwOJcyc5lnzeKKcJVzT8OCmhitBfILuv3Nb4FHu2ANfsYH1fmSJdbRy3r-U8t0eA60G4jeq5lcbCuwDPv2lk14v2iplJQRZ4h0AD4HY7uMj8B6WBF1EF5FmOFZgVisAOrsX5HSalENzZ6s1J8nlFs55EApBNIzyx_6CRzGbK1jaG4MOYpV3-eeiIPnUew0NujeeGVe1Fnub6VmWxkYg33nhfTWfTZMHF6entr0RQ40xExzRw0-Vr6UQsW7ofYP3X45SL9hm2vZKcSV0NBjIRCYqOcgA80kjGyoNHwaLx4vbrTB1p1Vu161En4elK_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=LGMYsoDUBCnEJ27M1kRfSaJipwOJcyc5lnzeKKcJVzT8OCmhitBfILuv3Nb4FHu2ANfsYH1fmSJdbRy3r-U8t0eA60G4jeq5lcbCuwDPv2lk14v2iplJQRZ4h0AD4HY7uMj8B6WBF1EF5FmOFZgVisAOrsX5HSalENzZ6s1J8nlFs55EApBNIzyx_6CRzGbK1jaG4MOYpV3-eeiIPnUew0NujeeGVe1Fnub6VmWxkYg33nhfTWfTZMHF6entr0RQ40xExzRw0-Vr6UQsW7ofYP3X45SL9hm2vZKcSV0NBjIRCYqOcgA80kjGyoNHwaLx4vbrTB1p1Vu161En4elK_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف یه 20-30 سالی هست درحال گریه کردنه
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67321" target="_blank">📅 10:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67320">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/810ada8a67.mp4?token=DXCM9_WPQ7h-iyEJZhaAKQGk5EgHqu_G4z9qnTzgkzQ5IIY4Y4B9l_OU8wEuvJqu1F5rqncZ95pMTQRxJFLG5BgeDD953rS7h8l2_Mlr7zvE0XBmSylnK0xcKOKJ0KGcJ9Ua069jz9P9nOYsOLfbcMepgknvCct_oyPnam2eV3Hm2bJKFe0zadKqcNy1ksHJ_GgSXBeWGx9Eoe6-6BKM7wSPUhfxi3c8mKZm55C0a-to20nFE9ZUFEFadTKLeSg7-TnRrMjOyMtyTFkjN9Nlwwayv2Tmp1D4CLjP0plP8HEkjIyk0ClDJWs73uLzEtIGWD5lLFJa4_ZAloGy40lNgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/810ada8a67.mp4?token=DXCM9_WPQ7h-iyEJZhaAKQGk5EgHqu_G4z9qnTzgkzQ5IIY4Y4B9l_OU8wEuvJqu1F5rqncZ95pMTQRxJFLG5BgeDD953rS7h8l2_Mlr7zvE0XBmSylnK0xcKOKJ0KGcJ9Ua069jz9P9nOYsOLfbcMepgknvCct_oyPnam2eV3Hm2bJKFe0zadKqcNy1ksHJ_GgSXBeWGx9Eoe6-6BKM7wSPUhfxi3c8mKZm55C0a-to20nFE9ZUFEFadTKLeSg7-TnRrMjOyMtyTFkjN9Nlwwayv2Tmp1D4CLjP0plP8HEkjIyk0ClDJWs73uLzEtIGWD5lLFJa4_ZAloGy40lNgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان مراسم افتتاحیه مسابقات «فولسوم پرو رودئو» در ایالت کالیفرنیای آمریکا، یک چترباز پس از آنکه پرچم همراهش به درختی گیر کرد، تعادل خود را از دست داد و به شکل خطرناکی روی یک چادر سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67320" target="_blank">📅 10:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67319">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca0cec0e0.mp4?token=kJ5dEUu8fuZ2Wk2Kv0T6URv7MeWw6B-ipeZ4TosVgkFPA9xkZ_JnmTVL7W8666aFNfj70Y9SFx0NFYB9IgiLC1PeW6yhTkKeOctD1rbnVQDGT738sCU7odrrNISw6APSQpko0S1C8vw8iv-cnw-SDZ6C52tt92K5HzIj8109e2XIilumtIdz9NgcmmKPRXGnUgt9ZcV7KwLSnKHOxXhXGm7YsU3YkaC48MjW2kcsrlTcEuWJ6RCrMrDDPUbnqjokBJ99VSlTdDDgiXdJNuqUups09UG2bLSZ-MrdyBFLJoVTyFLD5WCiPQqTdjduisEJBdR1tP1aesaX4xsY7XXqNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca0cec0e0.mp4?token=kJ5dEUu8fuZ2Wk2Kv0T6URv7MeWw6B-ipeZ4TosVgkFPA9xkZ_JnmTVL7W8666aFNfj70Y9SFx0NFYB9IgiLC1PeW6yhTkKeOctD1rbnVQDGT738sCU7odrrNISw6APSQpko0S1C8vw8iv-cnw-SDZ6C52tt92K5HzIj8109e2XIilumtIdz9NgcmmKPRXGnUgt9ZcV7KwLSnKHOxXhXGm7YsU3YkaC48MjW2kcsrlTcEuWJ6RCrMrDDPUbnqjokBJ99VSlTdDDgiXdJNuqUups09UG2bLSZ-MrdyBFLJoVTyFLD5WCiPQqTdjduisEJBdR1tP1aesaX4xsY7XXqNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین حضور عمومی مصطفی، میثم و مسعود، سه پسر علی خامنه‌ای، در مراسم تشییع او در مصلای تهران.
مجتبی خامنه‌ای، جانشین علی خامنه‌ای، اما همچنان در انظار عمومی ظاهر نشده و در این مراسم غایب بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67319" target="_blank">📅 09:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67318">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=OyGBBSk1hXFrBl4f9BK0hAoCFaPjYUs6Bn934Ir6Of-cRiG_q_zRkvCPaUPUSi8cCDyJiOQKbLmhcWqxws3dinYVX_FOH8MTIcCEG9zoIi8yPr2HFvds1mFsYDMa9GDisl5GxKwGwqfdfpVnbdx9oPxFIlY2wDy7vRw2vEtQ8-SUVutoDCtPL1BM6QWivP7E-Jsm9qOWuZYf1KJeWIhu9ig-1uU50eBRtnRXTypC_pyoceTCrI1gBG9IRAqqFNBY8bpdA-jjRWvot_5Rf1EhfR2kITTt_DekSK2Erjdy_K0XJQHFBNHFz6awcE_LKrvNfvpivPEsOQCGlmF8uxGGfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=OyGBBSk1hXFrBl4f9BK0hAoCFaPjYUs6Bn934Ir6Of-cRiG_q_zRkvCPaUPUSi8cCDyJiOQKbLmhcWqxws3dinYVX_FOH8MTIcCEG9zoIi8yPr2HFvds1mFsYDMa9GDisl5GxKwGwqfdfpVnbdx9oPxFIlY2wDy7vRw2vEtQ8-SUVutoDCtPL1BM6QWivP7E-Jsm9qOWuZYf1KJeWIhu9ig-1uU50eBRtnRXTypC_pyoceTCrI1gBG9IRAqqFNBY8bpdA-jjRWvot_5Rf1EhfR2kITTt_DekSK2Erjdy_K0XJQHFBNHFz6awcE_LKrvNfvpivPEsOQCGlmF8uxGGfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زاکانی و برخی از مسئولین تو حاشیه مراسم رفتن چلوکباب خوردن، عرزشیا هم اون بیرون زیر آفتاب، صف وایسادن تا تخم مرغ آب پز بخورن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67318" target="_blank">📅 09:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67317">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNOpDADnBZ2Fr2JoR7TsqCWYRVjjPilmV_Xlyicz-ItcT8kTNa8V2d_ZWHVN2kK_wmq5ziRSxS1ukPwmebYOS05XlvRs8jhmktNYq3r-9eDyET5UyJNqeNwuhIcTXJz4oKfXOLYxDMwzKlIc7vGeqoEBY1l-MhodU2-EyyEY8aRJfYeQitc_mqsoxHTevTIn-GVSySsM1vlZSaOo9Kt9fBSAStus4nMJEncb4WfddhzH4iBfzG7-0PMMkuVZ3yLufgy3Pn-dpTd1pt5jboIaz8CgkYj1SMBMvXqtTJgtk4d4PfFZugLH35hTCtcJiEZDfpgD6NusJFxz8E4ex53dTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
8فروند جنگنده A-10 Warthog در پایگاه هوایی موفق سلطی اردن مستقر شده‌اند.
🔴
این جنگنده ها برای پشتیبانی عملیات زمینی استفاده میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67317" target="_blank">📅 09:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67316">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67316" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67315">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kMYAgJaaX_QpI4XuCiJavtRS2n8egBF-zxTQ6yTjEghtHzrY-xo46SKderBkn1JGdnk8mKLUqnBXKvt7Cdn4_m60kg0tyF7lYuaHREBm3r9Vr-VQ4Xl_nV9at_4E2GgS8foqCTu9rHowBy010k9Its8Pd5BOG6Vw9Zpy4OSBWQzkZaeENk4Z1K_m1zwdVUt-ynrj3EIrOY5p8fpHJdc2P-JFiu8oehkS4b9oqPqHNPQLXyv6Np_eEFSqmGjvz5v_AmxcmFTiOYIjUfSzECa4Os1nVJgUeqbdmxv14fqGsLf2rzgAgF6bajKYlDXJV8_VYz_ZJgneoQuz88I5NuohIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67315" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67314">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Net4QFIXRbxzFhpNDAH-Aspl0XcQoy_TNRf_Utv0qsus2u3Qz0fQ3cWgQy_PP3xiJL4kdcCmdNBrn0uTql29iScVJXmiMvLbosZ3MG00bpkVtTkKKsyk7ULn-UyskJihk_v4n4GlpXk2it8n8KXyfS3jieWyExVLOvCkNMlKWaB1yRSfXC0HCIzMq6YgLoXxxJITxTeXyiYRnuwzpLQFbp0NOPHXnrdsM8JbF1BC_wGsTFAG2FAqc9pE8972gh5DVHWzr0MO-hWDW0WnLFIlJDf6rD2vtHqdP_QhctV15jdc4oIjN7tXCYLsFWU6osaElxgTAsPoHMsH8a9NsiCDCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
ولادیمیر پوتین، رئیس‌جمهور روسیه، با دونالد ترامپ تماس گرفت و دویست و پنجاهمین سالگرد استقلال ایالات متحده را به او تبریک گفت. کرملین اعلام کرد که این گفتگو یک ساعت و نیم به طول انجامید. پوتین از ترامپ برای سفر به روسیه دعوت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67314" target="_blank">📅 02:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67313">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79806b6dec.mp4?token=O0gMvdGU48YEWXOZoF7wfvJNK8KtMWFF-Z-vLMRuD2l9wa4bL7ZySnEPO4zYJKPsiw0KSA6nayJmVXkiIB2BAiCU07QjLhTRzbjFaH6BL9uiXWiUFRvhoQkjLwnPQ6kgnIa5z6_eM_Am3hIXHjj5DASqYOofEJKM7tm_zu3CPFQ6QAQeeL6SFmbghqtVqnNyZBBF0_Yndo_1ts8oF1ryOU44XHchHtSZHM3NXb7LJm7bjXUcE8onwN2kNcWaEYY8x_acUh87mUT8CX6tFnoiDe6u5kw5t7JJpUYAoFKoKZqsN0qgUxqr8phf6KW2OYO7sERtB4ieqdnbjYCBZsV0CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79806b6dec.mp4?token=O0gMvdGU48YEWXOZoF7wfvJNK8KtMWFF-Z-vLMRuD2l9wa4bL7ZySnEPO4zYJKPsiw0KSA6nayJmVXkiIB2BAiCU07QjLhTRzbjFaH6BL9uiXWiUFRvhoQkjLwnPQ6kgnIa5z6_eM_Am3hIXHjj5DASqYOofEJKM7tm_zu3CPFQ6QAQeeL6SFmbghqtVqnNyZBBF0_Yndo_1ts8oF1ryOU44XHchHtSZHM3NXb7LJm7bjXUcE8onwN2kNcWaEYY8x_acUh87mUT8CX6tFnoiDe6u5kw5t7JJpUYAoFKoKZqsN0qgUxqr8phf6KW2OYO7sERtB4ieqdnbjYCBZsV0CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جمعیت هموطنانمون در تجمع چند ماه پیش تورنتو رو ببینید و با جمعیتی که در مراسم تشییع جنازه علی خامنه‌ای اومدن مقایسه کنید
🔴
فرقش میدونید چیه؟ ۸۰ درصد جمعیت در مراسم خامنه ای اصلا ایرانی نیستند. کلی لبنانی عراقی یمنی و فاطمیون افغانی گرسنه رو با پول و... آوردن بازهم نتونستن مصلی رو پر کنن!
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67313" target="_blank">📅 01:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67312">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDt0mgrMcoCM_8lrvpgs5z5garik9C0WcdiZC5tCnVdNQKJsf2FhfEnBY66HvVAFQTbmJAUkOx9lMSQ9-HSpSTZ35pB8Tke5Ymdc6EbGfWWM_589R5pnxr-zWFCGrncPxnaa48OnMdm2TXQkOV6jsf27G90VkkshpZHZpfz0ErZN_6agulZCjkRUK4bMUhC5Jar0gJnF-7cz7DbK-fiCDu6nje2Z_mBhKuuUtiNHSugw-deq238vJ0Lwc-iVis-wsnhhY-igKWSPhbphasJTRuIw1ar2q9Cj9k10vU2sSfstM8o1ByS-p60IrwKLCufIwOZe2biLyA49W3TpwsLUXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیروهای ارتش اسرائیل در حال عملیات در منطقه حداتا در جنوب لبنان هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67312" target="_blank">📅 00:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67311">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5be218b45.mp4?token=afjb2wRgaD_0ghEn4nVSoK0dOSMa5zaHLVoOHaqAjLhrlkqaC5Lv7nuqglhbxPFSRSKYUad6uBjTIJQW3o_u5eg4bGATuDVJSZ1JBw0fSkYLZgRO5JlI7ll4EK4l_U6DzQGEa1nuyiHdXtnF_RSz1Su9J32sOqFb92wm3qXAHYUPLXZWV9CfjJe7I7ZMK2b-N8CIapBgqtwBVK7qpDIg-M4AX1s2AQtVPFCmr-oP636E8A8NHp7k2_1RSaxm6LcZUQVIec62RN9ahJiGz_h-hkTmcxPP4cizuLUNVNsKFVVafMchMgd7GvQCEI_vrfwQnbX30aekfMYn_tLxISh34g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5be218b45.mp4?token=afjb2wRgaD_0ghEn4nVSoK0dOSMa5zaHLVoOHaqAjLhrlkqaC5Lv7nuqglhbxPFSRSKYUad6uBjTIJQW3o_u5eg4bGATuDVJSZ1JBw0fSkYLZgRO5JlI7ll4EK4l_U6DzQGEa1nuyiHdXtnF_RSz1Su9J32sOqFb92wm3qXAHYUPLXZWV9CfjJe7I7ZMK2b-N8CIapBgqtwBVK7qpDIg-M4AX1s2AQtVPFCmr-oP636E8A8NHp7k2_1RSaxm6LcZUQVIec62RN9ahJiGz_h-hkTmcxPP4cizuLUNVNsKFVVafMchMgd7GvQCEI_vrfwQnbX30aekfMYn_tLxISh34g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی خامنه‌ای،‌ 3 بهمن 1403:
ده‌ها متوهم به درک واصل شده‌اند. من به شما عرض می‌کنم به فضل الهی این تجربه تکرار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67311" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67310">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67310" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67309">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ua2goFrAhJoQSTMToA1vW_zE94ALDT1E8R0H4yTCSFl7l_0T0mZ6wikzxCo2X30JKvRZoKlCoCgDLbGvrzwjhs1g-NHutQ0KyuYj92FlaXQgx0cQIeJVCl-8ybgLYWld-5S8QHR9GXrlLMtgxXQDSrkMFJBM6wdZvliOd9PBP_AJra8feTwiC-iFO04xAFVdoqbmhYcIPYz4ueyMjNJoOH-4I8XpuKyzFz7BrFTki4NXzwswZVlzDR8oA5Xv7ipk8uUJi8l9n457Ta2QOvx7HqQCqPDasA-st-8wWvUMnErRMwIprp_WaehfNLj4TPq20IToH8zadrJu0S9WzgfKXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67309" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67308">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/842bb5b4aa.mp4?token=eezhuWiu49TOEbkWm-SXzS13O4X_P3xKKAr9XDZ5QPlCT2t_UEd2lQoa3J-lByqOb75MaYubs2DaM0jzvEzUs2ANEixAar6wE0ruon3lJleUWZlWekwN0WNYJvR5aT8Ciy6OpnZN-afu0sIAz7c0zsGj4-Tnhga73sk3w_NvdiynQ4VZOtPCJw8i4jiJR0sLKhrRx39Pnok0mJKBTz0Eyu65nC2pNeZGN_MW3M28P1XwPCLOqPsZ5UQElUYdmLndpYflvemAj4EuYbwPLZHzZXtGdpEjDooroLbmiIKcoacTNMILm5SkITmrn-SOZbICTL7ZyfuoxEUdtJT9lZnWbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/842bb5b4aa.mp4?token=eezhuWiu49TOEbkWm-SXzS13O4X_P3xKKAr9XDZ5QPlCT2t_UEd2lQoa3J-lByqOb75MaYubs2DaM0jzvEzUs2ANEixAar6wE0ruon3lJleUWZlWekwN0WNYJvR5aT8Ciy6OpnZN-afu0sIAz7c0zsGj4-Tnhga73sk3w_NvdiynQ4VZOtPCJw8i4jiJR0sLKhrRx39Pnok0mJKBTz0Eyu65nC2pNeZGN_MW3M28P1XwPCLOqPsZ5UQElUYdmLndpYflvemAj4EuYbwPLZHzZXtGdpEjDooroLbmiIKcoacTNMILm5SkITmrn-SOZbICTL7ZyfuoxEUdtJT9lZnWbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس‌هایی لو رفته از ابویسانی، معاون وزیر اموزش پرورش حین گفت‌وگو با دانش‌اموزان معترض ؛
دانش آموز:
نه اجازه میدین تشییع رهبرمون شرکت کنیم ، نه اجازه می‌دین پیاده‌روی اربعین شرکت کنیم، چه کار مهمی الان دارین؟
+ ابویسانی :
اربعین بخوره کمرتون!
دانش آموز:
ما می‌خوایم تشییع آقا رو شرکت کنیم.
ابویسانی:
برو بابا تشییع تشییع..
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67308" target="_blank">📅 00:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67306">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHckRfbbJVG55UfUQgsNEt4WIPW3s85UXGfyryJwKCU06bwaplrLmBpVpTREsuyOJpTHQP7npyaikc0J6mPvMOruY1o0q5Xm2awzLP6H1gFJWQKQNI3E0UR35dAamWYgu8pWVUZ-QTHF4U3QQhCXsjCmjmVmqSPxZXLWK_C2smz3nL3s8nzU4szvlBDjAfM576bHl77qxyDYpws9RnAO9jOiLvCCNqY0MYLwmYpnsEPoqq3UkikKQZFxdj0WhtcHS2IXFngpJ99BkzQrrCggpREuwHscx7jPdkHG9XiSjhKsdIJt4bVja9WM6U6SqGlAgJxCCuguQo2ptObtP-kMmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7ffa7579f.mp4?token=orDQpVu1NU2lvpl0l-lzXzPNLKkqTr9_7dNtBtjBUYZtHfzM8fnDk_a38J1GpW40tTwcABw53x2PrFGfrsCod1IszgKGnSPEECWtA5i1dUL21QiGnEIPvz595j4AoeMND1rpqdYn5ZXOp5YT-sX4DjROS0ugDWk6AYd7D-hwiE3MFYMZNt24-QzZJ9gM9S0xaSRa-Yp4QruVFELVE0t4THxtrNJJmxvbSwN2Q8JSFEJyNe6iW3xX9zBfTpih25n0l1qP7TBFW0Ld7jqTfDB7Mcd5T9EDSSTlpeqxdO4W4_HrtKncCOhEZziprbKCrxOhZrG4AaPPuOIv0D3s9-IgBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7ffa7579f.mp4?token=orDQpVu1NU2lvpl0l-lzXzPNLKkqTr9_7dNtBtjBUYZtHfzM8fnDk_a38J1GpW40tTwcABw53x2PrFGfrsCod1IszgKGnSPEECWtA5i1dUL21QiGnEIPvz595j4AoeMND1rpqdYn5ZXOp5YT-sX4DjROS0ugDWk6AYd7D-hwiE3MFYMZNt24-QzZJ9gM9S0xaSRa-Yp4QruVFELVE0t4THxtrNJJmxvbSwN2Q8JSFEJyNe6iW3xX9zBfTpih25n0l1qP7TBFW0Ld7jqTfDB7Mcd5T9EDSSTlpeqxdO4W4_HrtKncCOhEZziprbKCrxOhZrG4AaPPuOIv0D3s9-IgBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعد از مزدوران نیجریه‌ای حالا یک فاطی کماندو از بوسنی و هرزگوین ببینید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67306" target="_blank">📅 23:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67305">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af68b2c3a9.mp4?token=nINcUx5nxvHm3CIKvpafJCSrvYqStbp_cs_Yu6aW08aPQ_to8WvSB6zEgnosn2xr1yidXulxF89HS9_ZceYKHCbRmC0ZM74zW3MUjehRm9ZIp1agjPyfpDcqej1-wlEE3PmZT1V33LnWmjl9hIPrWLms4OpXIowAjeXW4x-0cU_hld2GdAhpTcpONjzYjcaLqBsGIEqbK7gF0xnBJb8GuC27ffh6liUgGociBJQ-FgDK1iriYvEvzWy6IWNIgv6NgRdX-oOpXQa0M7kKTkXhEyPKTyRKXkti4B7Gts59JaxkVCaivfspslYJ0L5xq5v3RbUDU6LAllxhWqlp_dyzbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af68b2c3a9.mp4?token=nINcUx5nxvHm3CIKvpafJCSrvYqStbp_cs_Yu6aW08aPQ_to8WvSB6zEgnosn2xr1yidXulxF89HS9_ZceYKHCbRmC0ZM74zW3MUjehRm9ZIp1agjPyfpDcqej1-wlEE3PmZT1V33LnWmjl9hIPrWLms4OpXIowAjeXW4x-0cU_hld2GdAhpTcpONjzYjcaLqBsGIEqbK7gF0xnBJb8GuC27ffh6liUgGociBJQ-FgDK1iriYvEvzWy6IWNIgv6NgRdX-oOpXQa0M7kKTkXhEyPKTyRKXkti4B7Gts59JaxkVCaivfspslYJ0L5xq5v3RbUDU6LAllxhWqlp_dyzbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلم خاکسپاری رضاشاه بزرگ در تهران، زمانی که جمعیت تهران فقط ۹۰۰ هزار نفر بود و بیش از ۲۰۰ هزار نفر در مراسم شرکت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67305" target="_blank">📅 23:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67303">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RWds6Q07lUca2qtU4tTXax6q5A8RsbQHKLpAOGyZ4jBCpuTyhT89bnJLVCHt9_7h01YJXe57hov-aczVo7eL3c1y02AwO5inPdgCQY9sNjJ3AHTVeo848WS0q2zrLcUTc0qRfrdpBvSosL1VaqotbVk6NqXbCZmSw7dxZ86Q3gybquXPElk3vORFxykkTNj7xaUMJavzyPClpw8BB7WHSMKeqlx0KoPhGvAD8W1zteU9vQYl4mZJbU3FDYUJ8URIo9bWodjQAA8OuJUb1En_Hc_nvXTKL0KQtcdfpU9MDAfQx_mN7--HU6YGNbF65N3W979ke8y9qgMx8Hrp9D13uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JcrrvOOI3Qu4jGkm3lJFaenYcicCxFeEeYpJmEY1Xjn4YE_97zdD78JPs2HC0zOGg6coQr3Icg7gm_hMYIszsPVYrN3qZgGWzh8xpdzFXVoVvyql0X1LYmEaf9elc7l8bdQueIm2AaOdcE8cywy01pNDRvSD4ih-TF_1ov_T3aUkQCupS9bMPN1WGLu_Z1xyy6dTdo05WPZ19utaACgyw313Fh_MuebAo5VVeQtiIJnCfWM5vFy8qHihtpgDQq2suFMsWa9shmEurZ5mbanfFlV3lOTs61KOwUPKHp26lTkNNBdqUjuorO9yUXPG6p51eKM5_96AFkaKqfIcPJji6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
زمین گرده...
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67303" target="_blank">📅 23:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67302">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDDzCydj7LQJx5FIc6Q8GoD15D7i355RzWlVzjf1I4R5ORVssbMocMehFBpMOq2AUYti1skjHcsdkOMykt4wH0Xws4B6LqAhskpTS8VrrUhrzeul2M7yDjIy0tO6C2kZSXXzobJJ_MjR4KuronxRyk8a2stQCGU4OFv5q7A5Z3XtZkp__t_wiJx66KyM99N2WKhSeIxVKZdJm3e6ag5e-Sm5NtYVKRoxOPCLToKYPbgoLFmQL1gcFlUeX8OwkJBYkTlFWZkBWLoaHDHSjBqA7GwAzmPjBg4uDqTbvsxI1ZyLEAcalBojj9Z6r_4ac4LDcVjel5UhmlLb2LseH9TsgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
دو مقام آمریکایی به من گفتند که مسیر جنوبی در تنگه هرمز همچنان فعال است.
یک مقام آمریکایی مدعی شد که اکثر کشتی‌ها با سامانه شناسایی الکترونیکی خاموش تردد می‌کنند تا توسط پلتفرم‌های اطلاعاتیِ «منبع‌باز» (Open-source) رصد نشوند.
این مقام تأیید کرد که ایرانی‌ها تلاش می‌کنند از طریق رادیو VHF برای کشتی‌ها ایجاد ارعاب کنند.
مقام دوم آمریکایی اظهار داشت که سرعت تردد در مسیر جنوبی طی روزهای اخیر افزایش یافته است (حدود ۵۰ کشتی عبور کرده‌اند) و این مسیر همچنان باز است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67302" target="_blank">📅 23:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67301">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0711bc2f95.mp4?token=BTizWqyKyKrN6fxiQ9KDOcsGAFIYiTIc9xaTZAUpCSVfsGTGalziWiE_-b_v2r8OeQl3JrpDO3A_PIJLVZO2Nc94ZqkfB7CYvYvGZW6PtmN9HuMmK7pNEOSf630M2Wq2Kle0I0JEkrsd6buoGLBZUJjM5s-SGlZZs6dJ_T0qKQNK1EhOumX5ncJamyWRx4hANaXx2H2iH9yz9CzUIB3hDLLsOKyRQEuoAWUGV-CtTt_wfrzifkuiEMfew17YeI_Wio3fgM_zTuIlm7H8KHyW58MeC8bZ2XfJWXdXE7-1oJPl_SyM4YOQ8XthatJvzI8Af5vOGIGU7L5EyBtHqy0FiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0711bc2f95.mp4?token=BTizWqyKyKrN6fxiQ9KDOcsGAFIYiTIc9xaTZAUpCSVfsGTGalziWiE_-b_v2r8OeQl3JrpDO3A_PIJLVZO2Nc94ZqkfB7CYvYvGZW6PtmN9HuMmK7pNEOSf630M2Wq2Kle0I0JEkrsd6buoGLBZUJjM5s-SGlZZs6dJ_T0qKQNK1EhOumX5ncJamyWRx4hANaXx2H2iH9yz9CzUIB3hDLLsOKyRQEuoAWUGV-CtTt_wfrzifkuiEMfew17YeI_Wio3fgM_zTuIlm7H8KHyW58MeC8bZ2XfJWXdXE7-1oJPl_SyM4YOQ8XthatJvzI8Af5vOGIGU7L5EyBtHqy0FiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مردم اروپا با دمای نهایت ۳۶ درجه
🆚
مردم خاورمیانه با دمای حداقل ۵۰ درجه
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67301" target="_blank">📅 22:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67300">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=JLT_tbQiCLsBeCev5JxXsAylXuGofcehAjPWobbOPQctbGnJfvKYXyNNN1tU41g0M5--5Plnf8Q4TSLODTD0yBtIDE-UkxPocFZDi6qY7x4Tq2VFdzGFCTqiYgV4mLC1xpfMJR1xj6bDmG1VrBsA0KIzpshEMXe04SiNCNL7nsgZqUSG285R2R9dd1gEW15j4lfMEOWQ47u2dcjabPEAKetnime2VlpJnPtPE99cvuEy16aRS_DypWZ9depGnDTWm0Xr4CbaVu35KK3mNNlu6q5xR0Cr40e886NgPVuFW4a2-nQdtPOTssd1KHCWv9FgyaS7aUY7iiBKMoUiC3BXCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=JLT_tbQiCLsBeCev5JxXsAylXuGofcehAjPWobbOPQctbGnJfvKYXyNNN1tU41g0M5--5Plnf8Q4TSLODTD0yBtIDE-UkxPocFZDi6qY7x4Tq2VFdzGFCTqiYgV4mLC1xpfMJR1xj6bDmG1VrBsA0KIzpshEMXe04SiNCNL7nsgZqUSG285R2R9dd1gEW15j4lfMEOWQ47u2dcjabPEAKetnime2VlpJnPtPE99cvuEy16aRS_DypWZ9depGnDTWm0Xr4CbaVu35KK3mNNlu6q5xR0Cr40e886NgPVuFW4a2-nQdtPOTssd1KHCWv9FgyaS7aUY7iiBKMoUiC3BXCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیام نتانیاهو به آمریکا به مناسبت دویست و پنجاهمین سالگرد استقلال:
🔴
«۲۵۰ سال آزادی. ۲۵۰ سال دفاع از آزادی.» او این مناسبت را به عملیات «انتبه» در ۵۰ سال پیش (که در آن برادرش «یونی» حین نجات گروگان‌ها جان باخت) پیوند داد و اظهار داشت که آمریکا و اسرائیل در ارزش‌ها، سرنوشت و مبارزه با مستبدانی که شعار «مرگ بر آمریکا» و «مرگ بر اسرائیل» سر می‌دهند، اشتراک دارند. یادآوریِ یک اتحاد مستحکم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67300" target="_blank">📅 22:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67299">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toV1IILOL5xz3Bf0YgyPeU95h8awNO75x6lW0EHvKDLa5Jhad1YcoPO1os3hYlA7fOOgoJW6D_kNPbCt5JyA1ab00pEVSu3LNe8LBjEA98ZRZhE_3TUt-03csQrL9Pgur1TDHkJ5liFTDQk0H3eGjlMdLCoER72OflD6t-VPD9x-PG2H30Y5v5R59jKwtjtiQvZ-cZm7L9fwISZGFrnwBjZiMLrpxOIxgMNob4FKlNrCTO1m-rNVq-bw0na_qyj1VA6S0o7vtLCQJql7pw4NTxPHOtgVdKVR9xmhcFJ4vSE9DyYn5HY_IqoBjsRoJaReiYmOwjgVe8m2hufRzMKQMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه:
دور بعدی مذاکرات ایالات متحده آمریکا و ایران در تاریخ 11 ژوئیه (21 تیر) به میزبانی پاکستان در اسلام آباد برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67299" target="_blank">📅 21:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67298">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqXwJSvdxUr2QuJEhpagqvPhnUCYrGMF6fKoanld3yJDOsbMAsV8YkoZlKkBymNFuEMw2tQ8ookIublxHOkModTyVyK283_xVvVIeVSMdcuGaKLoJsdV-R1UT7bPP7hekg9CdMjUn8oq_SlMdmOZOVRhCcwEJ94P6OaG2uLfjRMU3gKKNkKOYM4um1D_braqy_ujO7ih3WozaJ-tM8vbP5RACRg32ZbYVYdqlLuodeGRgaHuXOc1zd5D26JzCSiJG6AC1FtRXbxqtERhU-lWuekotHnpEljZC7Wb7AAsyPS3RSnN9R8ar9wxLsfzk_KZ4GMYZA-j-qqn6XbYykcxeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترامپ:
فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67298" target="_blank">📅 21:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67297">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGtFDuwu89oHzdMOLxt6U7Jf_VgA3sSz5GNKxLzP5APk3gb-byAJBotC69n-uyKd0yfGGOzQHjWO323jhbSkQej8VLYWtLjkcOc266Kw93MDREU2p4WS_TIBHZlwKvxaJGMKkzoV4H2wVQu3ed8bpZag2ETT2w-tZgEa8oeW4CahI6EpxppGNiJFKrCHnLbqt3BS4zL_zWOV1BMUaGcccbr9qFy2scAJt03zYImTbLHe1emeFs_FykIeFkzYjqppMQ3PbhtpVuvefYDA-LQz_o-lkMC78yilASiH3QBFfl9MOdycV0ucLnFldyaxRpSacJsz1-b0OPyrP0NlrviKeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ به آکسیوس:
نتانیاهو میداند رئیس کیست.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67297" target="_blank">📅 20:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67296">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
پرزیدنت ترامپ:
نتانیاهو درخواست ملاقات در کاخ سفید کرده است و این ملاقات ممکن است همین هفته آینده رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67296" target="_blank">📅 20:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67295">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ به اکسیوس:
از دیدن ایرانی‌هایی که در مراسم خاکسپاری خامنه‌ای گریه می‌کردند، شگفت‌زده شدم. من فکر می‌کردم مردم از او متنفر بودند.فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67295" target="_blank">📅 20:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67294">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
پرزیدنت ترامپ به آکسیوس:
«همه آن‌ها آنجا هستند. یک گلوله [و می‌توانیم همه آن‌ها را از بین ببریم]، اما ما این کار را نخواهیم کرد، زیرا در آن صورت، هیچ‌کس برای مذاکره با ما نخواهد ماند.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67294" target="_blank">📅 20:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67293">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/589cc62912.mp4?token=czrVtlL3Ucs_hzIkzKVQhR1lkUVzSHfgP1O_3T860los8Al-3mZGPx4ldYmcx24qYofztFnIztsvesq-QoKSWV8f5F8GJ8z1BAmf2ziBEcPh0qEJHz1Uqm1aWVow-nnZ7x7D7X1xhOQfF53fyM_60Kd6K0fTukgNJDkwF2L2B33fvAWuLSNkVG94p_I1cYHhw76raL_P-9Z7Wbf9I8BhbMBbK4FVNVTNxDMugLYr_3MG_Ly058W4_ppF812MLbzJIXDrqmdEUPwOttRIPQQ1mUGdQIfrsLUwc9gIwR4SDCyUmFhUdbizEk8FgQHYvAyanXH2GXz9M5YE2VkorE-t0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/589cc62912.mp4?token=czrVtlL3Ucs_hzIkzKVQhR1lkUVzSHfgP1O_3T860los8Al-3mZGPx4ldYmcx24qYofztFnIztsvesq-QoKSWV8f5F8GJ8z1BAmf2ziBEcPh0qEJHz1Uqm1aWVow-nnZ7x7D7X1xhOQfF53fyM_60Kd6K0fTukgNJDkwF2L2B33fvAWuLSNkVG94p_I1cYHhw76raL_P-9Z7Wbf9I8BhbMBbK4FVNVTNxDMugLYr_3MG_Ly058W4_ppF812MLbzJIXDrqmdEUPwOttRIPQQ1mUGdQIfrsLUwc9gIwR4SDCyUmFhUdbizEk8FgQHYvAyanXH2GXz9M5YE2VkorE-t0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
۲۸ دسامبر ۲۰۱۱؛ مراسم تشییع جنازه کیم جونگ ایل، رهبر کره شمالی؛ مراسمی که تصاویرش به یکی از عجیب‌ترین صحنه‌های تاریخ معاصر تبدیل شد.
وقتی این تصاویر را می‌بینیم، شاید اولین واکنشمان تعجب از شدت گریه و شیون مردم باشد. اما واقعیت احتمالاً پیچیده‌تر از چیزی است که در چند ثانیه ویدئو دیده می‌شود. در کره شمالی، مردم دهه‌هاست در یکی از بسته‌ترین نظام‌های جهان زندگی می‌کنند. از کودکی به آن‌ها آموزش داده می‌شود که رهبر، شخصیتی فراتر از یک سیاستمدار است و باید بی‌چون‌وچرا به او وفادار بود.
از سوی دیگر، در چنین حکومت‌هایی، ابراز احساسات در مراسم‌های رسمی همیشه یک انتخاب شخصی نیست. بسیاری از تحلیلگران معتقدند که آنچه در این تصاویر می‌بینیم، ترکیبی از باور واقعی، سال‌ها تبلیغات حکومتی، فشار اجتماعی، ترس از حکومت و گاهی هم منافع شخصی است.
شاید مهم‌ترین درس این تصاویر این باشد که وقتی دسترسی مردم به اطلاعات آزاد محدود شود و فقط یک روایت سال‌ها تکرار شود، همان روایت می‌تواند واقعیت ذهن بسیاری از افراد را شکل دهد.
تاریخ بارها نشان داده که پرستش شخصیت، فقط به یک کشور محدود نیست؛ هر جامعه‌ای که آزادی بیان، نقد و گردش آزاد اطلاعات را از دست بدهد، ممکن است در همان مسیر قدم بگذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67293" target="_blank">📅 20:12 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
