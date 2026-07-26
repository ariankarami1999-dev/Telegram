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
<img src="https://cdn4.telesco.pe/file/o9dZy5nQlUhSL222gtmk9640dRbnHsLVsUe3zxCjFF4TFWKqQp_lbfEj83AuxWBH7F-bqSoDBg3e_aDofWl_3soe6FsX_GxsDmhNyJ_Q_jggjpBsbNHt4jzZzrWlRAmqAKErtRZNKBGHQHrFr95JhJa9tTKvKOY75kUzqsxsdqdJGgcnH3lmm57gESSR1gmZ0P_LPjh594PNKQoFHInAmXSBTV5fPLgDhlq0kzxPopyHEh39las_X5QQu3vylqKd0-iNwwbiHrA8csi6qnfUqkBDRb-mo7R-TDkGG37_NxRr1alp4pXBtszy-gx6HL5RjPvvPSzu8aJ1RKW4Zi8NaQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 951K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 22:28:22</div>
<hr>

<div class="tg-post" id="msg-137765">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdYUWOLrx8BIx1xs88-ucMwOF8pulGGp86V9eMrD0iCxzItVDnnYxyvSwrIqrrwTEVBuOb2TrrH7D3qriQnyJwqpowRxGtiZu4zGuFwvjc8vGjY3-Db7zUVSLbnLlaQL-tzKc-J8FQAljuQEjD3VZaMTZWop2EjxE2jaRKGMztUZPyZCfWE8KCh0rJB3wm-MOBHWwGcOzMsayQBdrZr9Per90TiemKPwOK7JnbaY14sZHeQV6oBUP7N4Q2pTNjQ4Db2KQCcezM-hSY_OUnDSKlTxmbf7f2jSsaDItXMIlFb3ouHSrqiZd5-AFOz3I5HqVnxnFbMQumheRS3S2ml79w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی:
مردم فقط دنبال انتقامن نه چیز دیگه
🔴
پ.ن: با این نخبه موافقید؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/alonews/137765" target="_blank">📅 22:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137764">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmkZQL0coNMw4fkMkkzix6TPKsgmmSFbgmRuPY5v6ftUEFXhfglA2NXDjjetk3d9BQH-TaRZr5ae0ZRiLyeoYvF6F1S4OfnPJQPGokfjN04M3rtdvfbLJmxxUJnZxHtG3RXWRsgmfIEw5LKUAZ6ObRhVFeRExIRkrxnkcu8ZiKEp00zU-8jc_2RCr9LSjdMbL5SpbS6q-F2TmgQjXRQV0UsnPM5n-0aoS9vu5HVhcmzT6jLfjtvtSdMMBku8GG4qDUTQtzDZJb4H_xR1Ercjd3JD4gQOnCcG-A9aetMTffjwwq26OIFYGPk5rxHQfwcN4JZyvFLg1Hga8x_v-Lz26g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون فعالیت گسترده تیم مذاکره کننده آمریکایی در منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/137764" target="_blank">📅 22:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137763">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
المیادین: نیروهای مسلح یمن طی ۴۸ ساعت گذشته ۳ نفتکش سعودی را هدف قرار داده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/137763" target="_blank">📅 22:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137762">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViLOBKTwE4-tJaLXtbbdIYRAtP_E4KFaZNt_L-rKVONUlOT-_empjdrKp6Q1hIvQ2PdASftoiWLP8IMS5g3HHnnHK1F_UytGo8WIFBlaJ5H4kVvOwIN3tD63uWvq6Zt4uJZzxJHCviEQehtultw5qsjkvZF6v8c_sqrYEQm3b8e3pWEy5e2GObhIKE5TWZZqRuwan_sAs_MFSd1yJwUxt_9cf7AZ5GF8FD0ucKBe24YdWscHLnabbvit4-Kzm8_URowae5Of9fTK5L3nEsrCxABJ90-LomrinQGrLGbJ5YX4Q6I2gNgk_cfzl_1XkboJpmaVKRsCIljArfjmV5BWtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آرام جوینده همسر سپهر حیدری اسطوره پرسپولیس: برای پیشرفت نیاز داشتم پارتنر بهتری پیدا کنم برای همین از سپهر طلاق گرفتم
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/137762" target="_blank">📅 22:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137761">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c2b00254.mp4?token=PFE9rHl_K6JePeHyDqIK5Tj5uFm8VNDETYiA6-1aMpjOR5BRpltqRhlHetG-zftvTrJA67JgO-I8ub2uH9N9k_iBbaKw3Ez_9BLf3Dak-GmCQPAQHIsOQuNGrJXhKH1epypouIc17OjcjI7nqD_Mb6W810ueCHNrV_Upvfcj1o84_WCJ2pGIHI2mN5vENFJCGTG-a4L8X0l9_wtO4Jy5BZXUPLqMAOGg_iXyz7mgBoW6wczDuyond3-ij7U5x_qEVUMc3UP96JvmPAWn6h5iQcYyOiV93nOXd7TQy242FJoiqZI7LfReEq_bSX9P11kec9F7K7Tk1qqAel35YIdHTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c2b00254.mp4?token=PFE9rHl_K6JePeHyDqIK5Tj5uFm8VNDETYiA6-1aMpjOR5BRpltqRhlHetG-zftvTrJA67JgO-I8ub2uH9N9k_iBbaKw3Ez_9BLf3Dak-GmCQPAQHIsOQuNGrJXhKH1epypouIc17OjcjI7nqD_Mb6W810ueCHNrV_Upvfcj1o84_WCJ2pGIHI2mN5vENFJCGTG-a4L8X0l9_wtO4Jy5BZXUPLqMAOGg_iXyz7mgBoW6wczDuyond3-ij7U5x_qEVUMc3UP96JvmPAWn6h5iQcYyOiV93nOXd7TQy242FJoiqZI7LfReEq_bSX9P11kec9F7K7Tk1qqAel35YIdHTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توی موزه ملی کره‌شمالی دو تا پنکه گذاشتن رو به روی عکس رهبرکره شمالی که یه وقت تو عکس گرمش نشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/137761" target="_blank">📅 22:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137760">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⭕️
چند نکته بسیار مهم برای حفظ امنیت شما در تلگرام
🔴
برای تنظیم بیشتر موارد، وارد مسیر Settings > Privacy and Security شوید.  ۱. مخفی‌کردن شماره تلفن وارد Phone Number شوید و این گزینه‌ها را تنظیم کنید: Who can see my phone number: روی Nobody Who can find me…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/137760" target="_blank">📅 22:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137759">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTA68JVP53UT48SJtEeaEqdaX5SeA3xIh_OHT_Xp1j1UlehmtHFQbNQ7X81Q2MsFHE4G-ykg3_JnxHqLTp2E0WCmNbDEyif2F0F1eHXD9sCUlPsVSg4SeMP4z9KU3Q7BSxJjSVv-IgLFToLgE5qjUFnECzbCl_EaNdCdtZi2C0oC8TVUi_KTO_yDy8f1NTtBFya_XsSTsJ3BChzA2RudGPzQsGMq8X13BVjjDkITvtRvOOqBrVEsXvPggj72Yqt5KYsAvzP8kv-qiKK7Alr7hkIF3D7_pWxTnqrJgjqT8jr1BGVjbmWpTrDCGBlk5lkx8DckrAlocuXm694FeYap8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آرام جوینده همسر سپهر حیدری اسطوره پرسپولیس: برای پیشرفت نیاز داشتم پارتنر بهتری پیدا کنم برای همین از سپهر طلاق گرفتم
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/137759" target="_blank">📅 22:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137758">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
باد شدید در هنگ‌کنگ داربست بزرگ یک آسمان‌خراش را فرو ریخت.
🔴
رسانه‌ها گزارش داده‌اند این حادثه در پی وزش بادهای شدید ناشی از نزدیک شدن طوفان «نول» به وقوع پیوسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/137758" target="_blank">📅 21:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137757">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
مدیرکل راهداری هرمزگان: کنارگذر هر ۹ پلی که در حملات آمریکا به هرمزگان آسیب دیده بودند، آسفالت و فعال شده است و عملیات بازسازی پل‌ها نیز در تمامی نقاط آغاز شده و در کوتاه‌ترین زمان انجام خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/137757" target="_blank">📅 21:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137756">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ادعای العربیه درباره رد کامل پیشنهادهای عمان توسط ایران و خروج هیئت عمانی از تهران، تاکنون از سوی منابع رسمی تأیید نشده است.
🔴
گزارش‌ها فقط از ادامه رایزنی‌ها و اختلاف‌نظر درباره سازوکار تردد در تنگه هرمز حکایت دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/137756" target="_blank">📅 21:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137755">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/567a79a6d9.mp4?token=spJhQ6SQ5jgITvR9ERfzRoKwK5prAyoVhDSgcFFPlbN4MkwurEAtgfhoAYtEiw4GeMqhnAM0_W1GwetcRq7cpIt7za3JlOzBpqXBw6o9WlQI8sP1XHEf9O0-oHFcue3cHToTdLc1e6Bnk3mwTZlgr6U9oIOXMJjcrV6mY4Y3DqAE5RarxN3mngZkTjAoGMkBew50rsigNF4kd7Uc-aOr88WNGZes5cZjlRVnsR7ynIDRAW2KJmdpZlNjehcs2h5w3EN6txuvMmWgJ7MVKNxb7FJLPnTqdBN8nyk6LTkbnIDo1WHsPzJCIWkW04PZPcpx3pJ7o5hUM4gQ1iFGX8JjcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/567a79a6d9.mp4?token=spJhQ6SQ5jgITvR9ERfzRoKwK5prAyoVhDSgcFFPlbN4MkwurEAtgfhoAYtEiw4GeMqhnAM0_W1GwetcRq7cpIt7za3JlOzBpqXBw6o9WlQI8sP1XHEf9O0-oHFcue3cHToTdLc1e6Bnk3mwTZlgr6U9oIOXMJjcrV6mY4Y3DqAE5RarxN3mngZkTjAoGMkBew50rsigNF4kd7Uc-aOr88WNGZes5cZjlRVnsR7ynIDRAW2KJmdpZlNjehcs2h5w3EN6txuvMmWgJ7MVKNxb7FJLPnTqdBN8nyk6LTkbnIDo1WHsPzJCIWkW04PZPcpx3pJ7o5hUM4gQ1iFGX8JjcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئوی عجیب از جنوب اوکراین که یک قطار روسی را پس از حمله پهپاد اوکراینی در حال آتش سوزی و البته نشت سوخت در طول مسیر نشان می دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/137755" target="_blank">📅 21:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137754">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
حوثی‌ها (انصارالله) فیلمی از پهپاد شناسایی و مسلح بایراکتار آکینجی ساخت ترکیه که توسط ائتلاف تحت رهبری عربستان سعودی عملیات می‌کرد و بر فراز استان الجوف سرنگون شد، منتشر کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/137754" target="_blank">📅 21:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137753">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVNZ2cklUXkgUXl15GcJ6COuOoQcN05VOa4gKRPK7Pj-eeqdoyHb-x2LQbs4j22Wja-qP4tV_rxxn3sQYEksTu0DLkXjF3rZ7c9Zj-llttxKJshDwdmWcnoaxcRrgc71MSgpeLep-IookjV-DOdEKElHkng6kzGDJ8wtDajB56xodXasU_d8pfGJCz0eLNZ1TjnT2VIGi0c2UF2c-7AZimN-4yBZ_WG0X-MAXA1Bb_RCgMN5a2kiq2CNq3vFPyoEttdjok-oCU6CVJV-Y3NUK3UjXfCtUWSTRYEl6AdlBq7Oe-5F_eim_33H5qOhmJ767DXYWSUiqZ13VHj4VpIaOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجیب اما واقعی ، لیستی از عجیب‌ترین و پشم ریزون ترین دلایل طلاق :
دومی عالیه ، طلاق مرد از زن چون زنش مهمون که میاد خونشون میگوزه
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/137753" target="_blank">📅 21:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137752">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">۱۰ دقیقه تحلیل مولتی بازار | سیگنال های طلاجهانی،نقره جهانی، نفت و بیت‌کوین!  عزیزانی که تو وبینار «سبد ضدبحران» بودن این اپدیت تحلیلی است که اونجا بهتون دادم و با هم سبد بستیم.   راستی امروز کانال سیگنال کریپتو(ارزدیجیتال) ۲۰۰ نفر ظرفیت باز میکنیم دیگه میره…</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/137752" target="_blank">📅 21:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137751">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npgFwUlG-yAaqim0D6x6ksvZ1yQ2QNXyB_8sM2eUea_wssLx4GCyP3FJG-QvsR1lWxGvjw1aSBdEZ6u12y-tUNWj4aLKZlymS4F22KJoQuBLpJF0NRzDjIJcHdkarZdYUm3ttdz5WkLNkXo_BjV4_MQYfiHEQnZad1ulM9_gdxFF32Gu0s6aG4rPn3hsUSmNzm53OiBen_UDAGmSS8OWkrx8KRNTeE3nsrmqlWCLZyInYDmlJXaWzXd9nQfaTYBa5avozyktDNaL7UYhaBiuckmoHxgJUvaf6vTmmv9ekcKWlFqZcUVbHghScvV_DXcSFAt4W0XsvZhQ7dVusUMOnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: تو عراق به من میگن عباس قهرمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/137751" target="_blank">📅 21:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137750">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
کان : نتانیاهو به وزیرهای کابینه گفته؛
آمریکا ازمون خواسته به‌طور گسترده از غزه، سوریه و لبنان عقب‌نشینی کنیم
🔴
اما نتانیاهو با این خواسته‌ها مخالفت کرده و جوابش به آمریکا اینه : «نه
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/137750" target="_blank">📅 21:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137747">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VX_iQ7cRo56Nb4yWebzSwyaFSSXEXK6qjpaf3FPx4PC-ZJLKynpMzg5uZq4PHGOeAqhFcPBvsmIpUtWdPmUN53vF5aGvGhMQB-6YlTnQtRPLlGl_oXO_39lSYLfQ3YrZmqW9mE3gpZkVBWjZnsPzWDQ2KxyCGGBBXryewH9uqX9MM6jO_u2vQVtZtoeyW-h_U6hK1aDbZ9ESfcVwA07T4W0ICIW5NfoQuLNhEK4bxk6vKCl0PrkSnQGjyQLLa-vXDQXxYXrYiSNE51XH6W0Uz6ocTcZHtu-DKQbIO2PuJbQcwmiIamR8kRHyG42Jg8fy0IjOWB_VuMMUkJF_IuiCjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EbC4a5l262FtQwHK0vnzyXoKedtbUMlcxvEpZWrKcDvuo8Sdpdzih6zq-fuN_oxgjT8uy_uP28LI18qi9Rxz6MYOogZZED46RN7Nprc9EUcwJdrSULGIHCPuQxn9kZUkAhDUgvtB1XBnrYs3-w7jeJa6sWWzgRyaj70ip82qO0vWGOchBE2cH0sTiQPyO68S7OfOeLASqsr_HteWWal_KWnrQIfBJzcorhXl_Yexf2KWeJkgBBdD3VOUQDYWXNmr9tgk7Jd-pilMPGJ5Bp09dbwBkob_K7PjpElwYeIX0odmUQeSyRlIFpZQ65foZODt3NxKK2zpFIji5I9aqfp7aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qgZWfArUz3LvUJFpN9pwS327KHwjLDvjI9uE8ic4LnJrtfVBNepp55j8nuYhHmOsrSnNdeKCqaC79V3dQzeHGunTmjawcLrl4LwnNmL4C1G_sh8tICY_4tXShuWKPi2gNQ69Q_JbPmkm_TNmeURRipEV81IdFDszPPFrXzTaNbL3tv6MTdN1latf0TCBO-D8i0GURliOHenvZ0FlnJ0i4HWbJttY1N1Khuhu2ad4u5ABmzOB_vTitR8Rvpt0EwFEpZebsG-rW361UTe8lrbYQ1aWx9cU3LTNz8sR7A3GQNopiHUd2svzRj52EAam1zJWrOXCbcMkFrnU5tfyGLrkjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از سرنگونی پهپاد «بیرقدار» ترکیه متعلق به نیروهای سعودی در یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/137747" target="_blank">📅 21:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137746">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
آکسیوس مدعی شد: آمریکا و بریتانیا هنوز در حال بحث دربارهٔ کنفرانس بین‌المللی هستند که می‌خواهند اواخر این هفته برای تشکیل ائتلافی به منظور حفاظت و پاکسازی مین‌های تنگه هرمز برگزار کنند.
‏
🔴
تاریخ نهایی این نشست هنوز تعیین نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/137746" target="_blank">📅 21:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137745">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
سی‌ان‌ان: عمان پیشنهادی شامل پرداخت داوطلبانه برای خدمات ارائه شده در هرمز داد اما گویا ایران آن را رد کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/137745" target="_blank">📅 21:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137744">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
بیانیه مجتبی خامنه‌ای  :
🔴
نامه شما، رزمنده‌های مؤمن و شجاع حزب‌الله، باعث افتخار و قدردانیه
🔴
امروز که مردم دنیا از ظلم آمریکا و رژیم صهیونیستی به ستوه اومدن
🔴
راهی جز جهاد و مقاومت باقی نمونده. هر کسی هم تو این مسیر پایداری کنه، وعده نصرت الهی شامل حالش می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/137744" target="_blank">📅 20:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137743">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6KaC_H2y_4KsumjaXPacOcB38Df9HfAn1t1PsT2LEwv6PzH9bzIGKeI1LCTHRL6SWaEIy2x187KLLho4NlQmo_S0aQXs1DAYXy9SzMWSEsaWniDUq5SGcCbD70YRwP5mR2rx7G7CVXUXHGEqC01GG6m-xvvw-haaxV64pOyssagvTiKbt8ugb1b5XdDtRRLaR1N_jDUfXwXidiOANR1NCrLCmq1yKdPxUOnwtorU_tVAcqJPvgf_Kw-jNx6v4XwTnzRUGgNsqtgPK1g5T3TTYh_3k4klVR1pWMuoK8NgfGl5nKsp3EPhUbMfBj21bCQdMbJPunKCwEKgIipMAwQ6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غلامعلی حداد عادل : سید مجتبی خامنه‌ای همراه با همسر و سه فرزندش تو ی آپارتمان ۱۰۰ متری زندگی میکرد
.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/137743" target="_blank">📅 20:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137742">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
العربیه: ایران با تمام پیشنهادات عمان برای ایجاد گذرگاه جدید در تنگه هرمز مخالفت کرده است، هیئت دیپلماتیک عمانی پس از مخالفت های ایران، تهران را ترک کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/137742" target="_blank">📅 20:42 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137741">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fMUdUVmdZdOBGFv-vEwCmU707YcgcnMx6hbp04c9ASZHE0kbjZWx3kMkAyJyFVZHgimovCwJiJDM7h_lO7j2mTOqBbJgSd6JtCI_NuFybrleb597vY5ON0k6No-lM2hYWM8r1GCtHSz9MFvjEbQbd2Do_POqSVmDDvrF5FpDXtspG7iQOJBRoOOSjWFICyp-g3hnTr7f0RWemQTE2QX82wV1aPcrn0pKSsQokunXe2Td-9gYfLBmGrSZxTEFFvVGCiylIUX4wRCWVzXbuWQBYj276y2vw9g563DHMyQTSYD-s9NsX_gs9oNYf0GXQYZqAVgywaEKCo3GV5roZM0QXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکسیوس : ژنرال برد کوپر فرمانده سنتکام، پیشنهاد داد که عملیات بمباران در اطراف تنگه هرمز متوقف شود، با این استدلال که این عملیات به حداکثر کارایی خود رسیده و بیشتر اهداف تکراری شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/137741" target="_blank">📅 20:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137740">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f700083cc1.mp4?token=mwk7RHZ_4DXxyiLiU-aoLGB5nTCildx1PDhA-4BDUaCl_4zx4iPCvO4LZGRgYw3wTdhAaym7SoyqZkTimljEsFhTLfTVRcMlPf3fk4eTpkEs7df003Sc1YziZtROQHmcLka6D_94LsxAB3aKzGPCSawhpfwsbnrPF8vdGiWlCCmO6rYaelhEkVyOcZidYc7gI2Z5U9quV7b8K_uCD7EwXiNtOAOoTmjRoClLcfQP2vickMUntcU93BB3kYIM7GwbWjLv3T5ZJ0YLg4pE9at0xHXq0Srtsr-j-gBiGhL6AlcRsURfwPHmOlaK1K42mmqA5BiduxO1U5ipb3GtIM5cRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f700083cc1.mp4?token=mwk7RHZ_4DXxyiLiU-aoLGB5nTCildx1PDhA-4BDUaCl_4zx4iPCvO4LZGRgYw3wTdhAaym7SoyqZkTimljEsFhTLfTVRcMlPf3fk4eTpkEs7df003Sc1YziZtROQHmcLka6D_94LsxAB3aKzGPCSawhpfwsbnrPF8vdGiWlCCmO6rYaelhEkVyOcZidYc7gI2Z5U9quV7b8K_uCD7EwXiNtOAOoTmjRoClLcfQP2vickMUntcU93BB3kYIM7GwbWjLv3T5ZJ0YLg4pE9at0xHXq0Srtsr-j-gBiGhL6AlcRsURfwPHmOlaK1K42mmqA5BiduxO1U5ipb3GtIM5cRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو، نخست‌وزیر اسرائیل:
ممدانی خود را با این قاتلان همسو کرده است مراقب کارهایش باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/137740" target="_blank">📅 20:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137739">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
نتانیاهو : الله‌اکبر، الله‌اکبر»... شما خودتون می‌دونید این عبارت یعنی چی!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/137739" target="_blank">📅 20:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137738">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
نتانیاهو : من برای شرکت توی مجمع عمومی سازمان ملل به نیویورک میام
🔴
از هیچ چیزی هم نگرانی ندارم
🔴
بیشتر اسرائیلی‌ها می‌دونن که باید با حزب‌الله بجنگیم
🔴
ما هم این کار رو با عملکردی فوق‌العاده انجام می‌دیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/137738" target="_blank">📅 20:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137737">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psz4k2wUv-HQdLI_HrHAadbnfd93EU2we5PU39P8HV79SgzrsB7Z2P4EvEZ4mPmvQsAfe15hvccwidkp6-omkDlk3rh6jndNq4yJQKcdTJuZPnyz5uU89npKH-4P_PbqgGXHWcOCiEPne_oijAmSuqATTJmaODdd7o_Vmp05RximudW4ORtAPFqzlkmRcOwhd7dOI0_6bhHBKFAw-FduRa-ZXOp7hfIbCvGyalO5PWUdcwjpXtDGPqCP6vvr0S15s4gJJscrGufrJXRmclu98h22MaBOZJXA_AUN_9wYgWrrWzOrn3RPSbRVUT-eYLTYBSYz8wcVOk-fofkVIMQ5Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برنی سندرز، سناتور ورمونت، در گفت و گو با سی بی اس، عنوان کرد که به ترامپ گفته باید با حکومت ایران سر میز مذاکره بنشیند تا کشتار و خسارت به اقتصاد آمریکا متوقف شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/137737" target="_blank">📅 20:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137736">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c20258523.mp4?token=OQqmFa-ygj0ojnOEKDVbgzGVKng7zzm1b66KL5T2zCfA1jWDsGDu5VT2ukqxnkyc9BtLY5p52MoQK5J_otIdifdk1vdaSvh2bdnmw97jp4VdMzzlug_cilqAGeaxFdum6Q0vJ9XW3TOp0hWSBRZkyKM8IY-8B40zFUxPA91nhkNgtKbow9lMl9-UQPUVuYXYRsgG_wakWLHmuu8nheIrWOFHy55kWR7EKO78T696YG-z6Vxwk2m-Y-II25-agIcfoiW_uYACH984mDGJISCQGM1nLkyQeshB1jBuUCSmQy4q9HBnz6KZtyK_04Oq0mqMpHijmvt40zD0VN7CqaT1gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c20258523.mp4?token=OQqmFa-ygj0ojnOEKDVbgzGVKng7zzm1b66KL5T2zCfA1jWDsGDu5VT2ukqxnkyc9BtLY5p52MoQK5J_otIdifdk1vdaSvh2bdnmw97jp4VdMzzlug_cilqAGeaxFdum6Q0vJ9XW3TOp0hWSBRZkyKM8IY-8B40zFUxPA91nhkNgtKbow9lMl9-UQPUVuYXYRsgG_wakWLHmuu8nheIrWOFHy55kWR7EKO78T696YG-z6Vxwk2m-Y-II25-agIcfoiW_uYACH984mDGJISCQGM1nLkyQeshB1jBuUCSmQy4q9HBnz6KZtyK_04Oq0mqMpHijmvt40zD0VN7CqaT1gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایلان ماسک: تا سال 2036 پول دیگه اون اهمیتی که امروز داره رو نخواهد داشت. وقتی هوش مصنوعی و ربات‌ها بتونن بیشتر از نیاز همه انسان‌ها کالا و خدمات تولید کنن، دیگه پول قراره چه کاربردی داشته باشه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/137736" target="_blank">📅 20:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137735">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
وزارت نفت ایران: در طول جنگ، ۱۱.۵ میلیارد دلار و در دوره آتش‌بس، ۶.۵ میلیارد دلار نفت فروخته شده و با این میزان فروش، بیش از ۶۰ درصد درآمد سالانه پیش‌بینی‌شده نفت در بودجه تحقق یافته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/137735" target="_blank">📅 19:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137734">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
عراقچی: اقدام اوکراین بی پاسخ نخواهند ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/137734" target="_blank">📅 19:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137733">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLZ4n-JRk1UWmTeorcPErt51x6EJkEUyIFOiepMuLzhmrWk_VYwhDT5jByLA6iTvIPmO-foCvqHv7c1I3wSaHlrZtjYUu-z6X5bWwVSOoVSHkgwvqb3akGbTQd1soJQ8D1WoHmaNjvCx9kO5k3p6DKesoVSaVjzNIh8aDUjQGAp_-ZSpiJwg2-q7ounKPLmzcxKFOQylIRIT6U9PonV5XAp1KEos-fwn4JcV6-MPINXSVHQY1eWRYAR3yZ5YAeV7ZF36VyseORAVz2qWrim5--fwExRPsX2D0LFI851CIwGqFbRZEpyaVD3Zt0QgwPTykudVSS2LV3T-m--YEQpYXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: اقدام اوکراین بی پاسخ نخواهند ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/137733" target="_blank">📅 19:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137732">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
وکیل پژمان جمشیدی: موکلم در رأی نهایی پرونده، به‌طور کامل از اتهام تجاوز به عنف تبرئه شد و تنها به ۹۰ ضربه شلاق تعزیری محکوم شده که در نوبت اجراست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/137732" target="_blank">📅 19:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137731">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: پس از تصمیم دولت آمریکا برای توقف گسترش خصومت ها، یک منبع سعودی نزدیک به دولت ریاض به N12 گفت: "ایرانی ها با ترامپ بازی می کنند، آنها به او اعتماد ندارند. درک نحوه رفتار او بسیار ناامید کننده است. هیچ کس روش کار او را نمی فهمد، او گیج کننده است و هیچ کس به او اعتماد نمی کند. همه از رفتار او ناامید شده اند."
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/137731" target="_blank">📅 19:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137730">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmReNP6jA2Hf5iY36An0-H19IXmFoQdQG7deRJNY85Xbbi77UQO0_Tdnz0k9VKsIxWC3TW6Smlp2qgJbzXwQsCfPKFOeq3Bb86f5rD-MBK26dAtXghxQHOq6Y7dR5gSoIxtSvIKdGQllg-BeKctqDUE8e71JklRLVPtX0Wtweq7n1UUFiltmLikOzVHOb09pXPBha4BfMkh9CHSQCvNFdrhu-AdVieGA6lVAAk3FgjIoK41h7LjBPKVLAlwjInOEAJ-6pqWKLmITYsvRVVbiPaNO8QaoSXo3ebrw-gPpbXBB5pKzCdL1RCmb9_hGjqaOA4IMoOsBOlVL4ey1ZRVR9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت عجیب عضو کمیسیون انرژی مجلس:  فقط نفت!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/137730" target="_blank">📅 19:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137729">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
احتمال شنیده‌شدن صدای انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/137729" target="_blank">📅 19:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137728">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24096cdef.mp4?token=ehyW3yu-PAIXoXDRbw2Luhe0fX18OHODJjTOMC7oK2TWAjEMFtUCWHZIKGHCDt2b36ljrJsUzX1G6JxeGXpvckkEJiiF2p4I6LCBXO9Ln4boIk3fUVvdi0b_FwpM-uhc_gM9gANzsVcYEJk3LTW5wlQGJWBnfxzj3Kk4bvDYpLSb4ovp3xQOvtV3Ik2IcGw1kKk7rkmdOyDgDlvi1-Q_FgUHG96nEDCm80jrQ4HwofVlU2tG5k4OtrIFqnUPgt4vFK99mn_lGiWljO2GFWOePr13VjWUOZL_xcimROI4c87snCXpmPxOuPqAKHQ5nOzpV3TAYxVdABsN1Iys372gIIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24096cdef.mp4?token=ehyW3yu-PAIXoXDRbw2Luhe0fX18OHODJjTOMC7oK2TWAjEMFtUCWHZIKGHCDt2b36ljrJsUzX1G6JxeGXpvckkEJiiF2p4I6LCBXO9Ln4boIk3fUVvdi0b_FwpM-uhc_gM9gANzsVcYEJk3LTW5wlQGJWBnfxzj3Kk4bvDYpLSb4ovp3xQOvtV3Ik2IcGw1kKk7rkmdOyDgDlvi1-Q_FgUHG96nEDCm80jrQ4HwofVlU2tG5k4OtrIFqnUPgt4vFK99mn_lGiWljO2GFWOePr13VjWUOZL_xcimROI4c87snCXpmPxOuPqAKHQ5nOzpV3TAYxVdABsN1Iys372gIIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ولادیمیر پوتین، رئیس‌جمهور روسیه:
تلاش‌ها برای منزوی کردن روسیه، حتی در چنین حوزه حساسی مانند دفاع و امنیت، شکست کاملی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/137728" target="_blank">📅 19:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137727">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
نتانیاهو: عربستان سعودی در ازای عادی‌سازی روابط با اسرائیل، یک برنامه هسته‌ای غیرنظامی دریافت خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/137727" target="_blank">📅 19:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137726">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
نتانیاهو، نخست وزیر اسرائیل: اگر ایران به اسرائیل حمله کند، چه مستقیم و چه از طریق نیروهای نیابتی، چه با موشک‌های بالستیک یا پهپادها یا هواپیماهای بدون سرنشین، اشتباه وحشتناکی مرتکب خواهد شد.
🔴
زیرا پاسخ اسرائیل بسیار بسیار قاطع خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/137726" target="_blank">📅 19:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137725">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8Fm0CRPoyvAFAPIjcE-x4H59F5Ker7vPkd8hyyLLueXHxAyww1t9J3xRP32QdDnDaor-by4SSex484Hbsms-1Od5Ubkx89p_KH-1DljAKJdBZk6YfVn0S8K_7sQOc1Cl_QTKuWX8TS9kgIzdMqMniCuomLTMEbmH8V_2EmVtfwRvBPrO1fJ8RmUOaX0AjjtKxhisHYSEhHZRH8Ag7DDk4y3-zZLQkdDBV_coJUVJHeCK20fY7sGGrhsfqHSoa7WsdhMk62kXobRKdzfrHpbiFhOMc9h_l2BHg-89GJREiiZV3102ALl8ylXFENtoQaxsAjyd_VFz0cKvRY20x_djQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/137725" target="_blank">📅 19:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137724">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
پادشاه بحرین حمد آل خلیفه با رئیس‌جمهور اسرائیل ایساک هرتسوغ تماس تلفنی برقرار کرد که توسط پادشاه بحرین آغاز شد، طبق گزارش روزنامه تایمز اسرائیل.
🔴
دو رهبر درباره تحولات منطقه‌ای و بین‌المللی، همچنین تقویت روابط دوجانبه در چارچوب توافق‌نامه‌های ابراهیم برای ترویج امنیت، ثبات و رفاه در منطقه گفتگو کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/137724" target="_blank">📅 19:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137723">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59abab6717.mp4?token=EsQlYn12S9VeerXtvOpNYy_LUcD_QLz81rFVVH107pbl3dECRrD3XumTu3SDDkVzWNvakJuDgpLYXtg632dBX_8NMAWnFJKAuGr6jjdYz_27aYdJQ_6mQ8XMcYk52yw2o15GxgLZBwD5eT0ivWDD6LK43SzsQQxzRc2fXqLs6LGhyBBulxQm3rjBYto5gonNKljzdEZs94BZ8C8Bz0gjktZWt3oLjLGhC87w24ot72FZeKiQXEZqAQWTkSTUtV0TAfPnn7kDf165IsagYrT1jQaZH5dpwdlLjVkT2T7GakPn9Zw_mexvhYIG923MhCV7w8HCzs0KJGX-SO-wq0jHmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59abab6717.mp4?token=EsQlYn12S9VeerXtvOpNYy_LUcD_QLz81rFVVH107pbl3dECRrD3XumTu3SDDkVzWNvakJuDgpLYXtg632dBX_8NMAWnFJKAuGr6jjdYz_27aYdJQ_6mQ8XMcYk52yw2o15GxgLZBwD5eT0ivWDD6LK43SzsQQxzRc2fXqLs6LGhyBBulxQm3rjBYto5gonNKljzdEZs94BZ8C8Bz0gjktZWt3oLjLGhC87w24ot72FZeKiQXEZqAQWTkSTUtV0TAfPnn7kDf165IsagYrT1jQaZH5dpwdlLjVkT2T7GakPn9Zw_mexvhYIG923MhCV7w8HCzs0KJGX-SO-wq0jHmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بارتیرمو از فاکس نیوز: انتظار دارید کدام کشورها به توافق‌نامه‌های ابراهیم بپیوندند؟
🔴
نخست وزیر کشور اسرائیل بنیامین نتانیاهو: آن‌هایی که می‌خواهم بپیوندند، با افشای نام آن‌ها در اینجا احتمال پیوستنشان را کاهش نخواهم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/137723" target="_blank">📅 18:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137722">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
کریستن ولکر از شبکه ان‌بی‌سی:  آیا حملات برای چند روز آینده به طور موثر متوقف شده‌اند، یا می‌توانیم انتظار داشته باشیم که امشب، فردا و در روزهای آینده حملاتی را ببینیم؟
🔴
مایک والتز:  اگر من رژیم ایران بودم، رئیس‌جمهور را بسیار جدی می‌گرفتم. ارتش ایالات متحده…</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/137722" target="_blank">📅 18:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137721">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNJP7GQ-oASFsBaOvGLsz-2x2SCSmMwVP7Cmh-vcVyRH1LGdC5YaybkAlIAyJUh8mkGj2ynL9_rKgeY_1LHdKbdhB3tJPibyBZpmp9W0jVolCEzY5CwiuYZSM1zsS0F-VPD8I_jTqeFoiwcnwmjTNvTcKZBLOVWQ-5VUBpmwm8JUq3mdPNCtxIDm33Z2c-6KExRKIzHY3HI4T1E2yD6Z-0RqdXqoOjs2UHwhVj1dt68X47gKwY-D-nRujB0-j-mWUld0QYI6d5-gqBffOJmbDuw8uKq-ZbMpRBCWJBhEsYFGeeqmUNZ32p4cOlPlGha7b7C15sOt8BTKj5NNUWVxPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تو عراق یه دختر بچه مظلوم ۱۰ ساله توسط پدرش کشته شد
حالا دلیلش چی بود؟ بدون حجاب تو تیک‌تاک از خودش ویدئو گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/137721" target="_blank">📅 18:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137720">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLZ4Si3gEJbu5m2aAfcJ4OaFAuY1ocRUj_3kfmqdY_21N-0WQvboh5R34She3vWmH4Iv-LA0hHAtKIyIWp2IAwCcUlCFzH8xRrRK-IQ2vkJNouupxKkR4Lq-sj25r6TvK7ZqOEZ_bloiAGRPxmXBb8n6IcQN-34d4Y-_YDJm1RJe2cmlorqr520E4TLWf9enwoGURERM0XVmjY361zMs8DD1Kzl7HivBfaaqlwZBahU7UuW-FColoXFqVRsvsNwMSPhOB0ZkkvxU4Cpi9aRCmwxpRPK1RMsgxYoLETkwGK9i1FX1GaD-opBdW65_h7FKTAf72kuKZqrDS4QCth7ytw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رضا پهلوی با گروهی از اعضای جامعه‌ کوییر ایرانی (کونی‌ها
🏳️‍🌈
، دوجنس‌گراها و تراجنسیتی‌ها
🏳️‍⚧️
) تو پاریس دیدار کرد؛
🔴
شش خواسته این جامعه که تو دیدار با رضا پهلوی مطرح کردن:
حق تشكيل خانواده
حق زندگی تحصیل و کار تو محیط امن
جرم انگاری کوییر ستیزی
صدور مدارک شناسایی متناسب برای افراد ترنس
دسترسی به خدمات درمانی متناسب
آموزش و افزایش آگاهی عمومی درباره مسائل جنسیتی
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/137720" target="_blank">📅 18:44 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137719">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87da6000db.mp4?token=flmCJhzw5aLs6AWAG7-DUj1EgIUKyrh2TpChCxGcLcPuLnNE9MkWWT4oEtLnfUIj9aeOkhIJ0VZBmmYzn3NhCjVPWS7BoCi16PBVbPpxmWLmtAHRvVxmSoXl5H0ueQ-X1jm-Tx_L22mClyEZ9rEl4jP7kcNPkUvdFdFbBKynTvGzIaarWY2u3cLCdTrkSDHZZj6BwEQHcqtdN3Y91pBh6QRC4I7bq3pGsFfuFc8WUVYQDLOuE9wFP7esDvnYGgR6xw4UdxR1nShOgec524c8GW6NMTrq-9WOgEy5Ok29NNaIiJgv40-HSdvkSJ7ferEKwSAMW1TV-Q9koYI-NopPLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87da6000db.mp4?token=flmCJhzw5aLs6AWAG7-DUj1EgIUKyrh2TpChCxGcLcPuLnNE9MkWWT4oEtLnfUIj9aeOkhIJ0VZBmmYzn3NhCjVPWS7BoCi16PBVbPpxmWLmtAHRvVxmSoXl5H0ueQ-X1jm-Tx_L22mClyEZ9rEl4jP7kcNPkUvdFdFbBKynTvGzIaarWY2u3cLCdTrkSDHZZj6BwEQHcqtdN3Y91pBh6QRC4I7bq3pGsFfuFc8WUVYQDLOuE9wFP7esDvnYGgR6xw4UdxR1nShOgec524c8GW6NMTrq-9WOgEy5Ok29NNaIiJgv40-HSdvkSJ7ferEKwSAMW1TV-Q9koYI-NopPLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محمدرضا باهنر درمورد رادیکال ها:
اینها در کشور، ۱۰ درصد هستند، پس باید به اندازه ۱۰ درصد توقع داشته‌ باشند، نه اندازه ۹۰ درصد جامعه
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/137719" target="_blank">📅 18:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137718">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
نتانیاهو به فاکس نیوز: اگر ایران چه مستقیم چه غیر مستقیم، چه با موشک چه پهباد به اسرائیل حمله کنه، جواب اسرائیل بسیار سنگین خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/137718" target="_blank">📅 18:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137717">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3da6c5df1.mp4?token=VTTD1D-DEAUJyL79Casa6X0w9KkvYNj_gtfW-wlpDXY6KvIaArgPK0TEttVmxuTt4vhsg17P7-j_t6PxOZzK6u5uWA2p1pPbewsUI6iaqGRaNwxvZoqbVm0i0iWvCHy1yoIgSRWLb_fC7le0yi-LijM0PAI92hjjFiTchyr-zvD0NTGGkkqca2ny5nloL4e8ELFcXuGwomphu2hBnQWv3bjUvZ2YHcuVPrjLR4NAgwSVkRzS8rsFmu1-toJUJJJNUgGJgtBNhaAElvTXTX56sOyHApBm3yEX7B9sZvRat-H8Ap3IIUni1ZIYKwWOwJZzJjr3jA4tapL15yyN3bcXpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3da6c5df1.mp4?token=VTTD1D-DEAUJyL79Casa6X0w9KkvYNj_gtfW-wlpDXY6KvIaArgPK0TEttVmxuTt4vhsg17P7-j_t6PxOZzK6u5uWA2p1pPbewsUI6iaqGRaNwxvZoqbVm0i0iWvCHy1yoIgSRWLb_fC7le0yi-LijM0PAI92hjjFiTchyr-zvD0NTGGkkqca2ny5nloL4e8ELFcXuGwomphu2hBnQWv3bjUvZ2YHcuVPrjLR4NAgwSVkRzS8rsFmu1-toJUJJJNUgGJgtBNhaAElvTXTX56sOyHApBm3yEX7B9sZvRat-H8Ap3IIUni1ZIYKwWOwJZzJjr3jA4tapL15yyN3bcXpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو به فاکس نیوز:
اگر ایران چه مستقیم چه غیر مستقیم، چه با موشک چه پهباد به اسرائیل حمله کنه، جواب اسرائیل بسیار سنگین خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/137717" target="_blank">📅 18:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137716">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/851a7f43dd.mp4?token=nlC-a3LNevLUrgZ-PnB5owUxG-L5ZEMxc9HJUPUIxYp7sduNT_8shqCTcsBV95_3l1D2dsNLO-tsjjC5CHIGHlsj2M6cNUQ6hHPZhn7p0TbVWUeVhZ_STOQTpoaJM8979Wvb0O3OmKw4v_j_qZ2MRERjxsaCgsXTb3ctx4KaiaxEZugut3s5p-BDwTgI4txsh_R7KjQMVNdGRZ084cVFvODacEY-OSBBhOUBPUzTAcFvsXSueveQ77llqNIAaY-hWAkSKXXAvZxgpbajrOiEwD4RU0-ede3Qb2a42SugCxXxZ5KjsIo_W0ER9UhLAZIO7VsALf6Ep7jOu-vNw3-8HDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/851a7f43dd.mp4?token=nlC-a3LNevLUrgZ-PnB5owUxG-L5ZEMxc9HJUPUIxYp7sduNT_8shqCTcsBV95_3l1D2dsNLO-tsjjC5CHIGHlsj2M6cNUQ6hHPZhn7p0TbVWUeVhZ_STOQTpoaJM8979Wvb0O3OmKw4v_j_qZ2MRERjxsaCgsXTb3ctx4KaiaxEZugut3s5p-BDwTgI4txsh_R7KjQMVNdGRZ084cVFvODacEY-OSBBhOUBPUzTAcFvsXSueveQ77llqNIAaY-hWAkSKXXAvZxgpbajrOiEwD4RU0-ede3Qb2a42SugCxXxZ5KjsIo_W0ER9UhLAZIO7VsALf6Ep7jOu-vNw3-8HDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کریستن ولکر از شبکه ان‌بی‌سی:
آیا حملات برای چند روز آینده به طور موثر متوقف شده‌اند، یا می‌توانیم انتظار داشته باشیم که امشب، فردا و در روزهای آینده حملاتی را ببینیم؟
🔴
مایک والتز:
اگر من رژیم ایران بودم، رئیس‌جمهور را بسیار جدی می‌گرفتم. ارتش ایالات متحده آماده و مسلح است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/137716" target="_blank">📅 18:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137715">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
سفیر آمریکا تو سازمان ملل گفته ترامپ حملات به ایران رو موقتا لغو کرده تا یه فرصت دیگه به دیپلماسی بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/137715" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137713">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e19b1e9d73.mp4?token=seXWceEFwNzzQKnXvrj2Pf822U4HnrI0ZZ2P7j3umqvSevKxTBKYiOOODANkrF-SzPyzcyljy-5ksQNsEc22wMMgesE9W-dSV-Em1WHeQO7RTQWFkZxOwG1pQz2kRj2hnOaE1dD_YcQCH5wL45eFFhV3cke-g3GS_eZ-JCr_xS5rn4TxAgEF5_wfcuVE7ST6JfZ5ukDoT9bCBgWUDjuJ7HZn0xVpKpvwJEjCutVhh4FOOd3R1QfRWPExJ7-2oNI7FEJrjQn1zQgzcaFd_d-WWfu5ttWR0-9dxlOJA2H0V-q0thUJnyWbKqE1quzSRoQRzyeuqQsOLasUqr1bQCb-cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e19b1e9d73.mp4?token=seXWceEFwNzzQKnXvrj2Pf822U4HnrI0ZZ2P7j3umqvSevKxTBKYiOOODANkrF-SzPyzcyljy-5ksQNsEc22wMMgesE9W-dSV-Em1WHeQO7RTQWFkZxOwG1pQz2kRj2hnOaE1dD_YcQCH5wL45eFFhV3cke-g3GS_eZ-JCr_xS5rn4TxAgEF5_wfcuVE7ST6JfZ5ukDoT9bCBgWUDjuJ7HZn0xVpKpvwJEjCutVhh4FOOd3R1QfRWPExJ7-2oNI7FEJrjQn1zQgzcaFd_d-WWfu5ttWR0-9dxlOJA2H0V-q0thUJnyWbKqE1quzSRoQRzyeuqQsOLasUqr1bQCb-cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هجوم عجیب مردم به سمت بازیگران در مراسم اکبر عبدی برای سلفی گرفتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/137713" target="_blank">📅 17:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137712">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed262802b.mp4?token=aTtuiuph2EkThJNfaob6wMLfl-1TPML6kjXS19eYbpHx06jSlEIxqd1cuK8Kd5PT62xRVr80mQofmbExRC1Ez3k28QL_yTCtAFf8tnIR-7OAD0hJN_I0YBR42zWxDyD-F7NRM08ljDNc4vxD3s9hL0XvLRbMP1dbJ94h77RVLax2esxZXiD7QbKsgS0s7tJNRr7Bu4fZZgSlvCvUB5X0qBvwX3Dt9xcpe91cvH48_DVy_u3ixsCr1gIPFTgC8Z6EESgaGhzO-mcVZ3yfs2Rz-qua51w60Oinhn1-MhwRKmJKgPcUVgesyKAfmNhNow-CniGAGNf781D2rHQwG8uqaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed262802b.mp4?token=aTtuiuph2EkThJNfaob6wMLfl-1TPML6kjXS19eYbpHx06jSlEIxqd1cuK8Kd5PT62xRVr80mQofmbExRC1Ez3k28QL_yTCtAFf8tnIR-7OAD0hJN_I0YBR42zWxDyD-F7NRM08ljDNc4vxD3s9hL0XvLRbMP1dbJ94h77RVLax2esxZXiD7QbKsgS0s7tJNRr7Bu4fZZgSlvCvUB5X0qBvwX3Dt9xcpe91cvH48_DVy_u3ixsCr1gIPFTgC8Z6EESgaGhzO-mcVZ3yfs2Rz-qua51w60Oinhn1-MhwRKmJKgPcUVgesyKAfmNhNow-CniGAGNf781D2rHQwG8uqaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهروز تابانی قهرمان سنگین وزنِ چین شد و مجددا جواز مسترالمپیا رو گرفت
🔥
بهروز تنها نماینده مردم ایران در در المپیا است
@AloSport</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/137712" target="_blank">📅 17:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137711">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
روسیه ناوشکن اقیانوس‌پیمای ۹۵۰۰ تنی جدید برای نیروی دریایی می‌سازد
🔴
فرمانده نیروی دریایی روسیه گفت: این شناورها از نظر جابه‌جایی به‌مراتب بزرگ‌تر خواهند بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/137711" target="_blank">📅 17:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137710">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
مقام‌های فرانسوی اعلام کردند آتش‌سوزی مهیب در منطقه ژیروند، محل استقرار شهر بوردو، همچنان از کنترل خارج است و تنها در شب گذشته ۵۵ هزار نفر دیگر از ساکنان پنج منطقه در جنوب‌غرب این شهر تخلیه شدند. با این تخلیه‌ها، شمار افراد جابه‌جا شده در منطقه ژیروند به حدود ۲۲۰ هزار نفر رسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/137710" target="_blank">📅 17:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137709">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
فعالیت‌های دریایی در خزر ممنوع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/137709" target="_blank">📅 17:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137708">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
رویترز به نقل از یک منبع بلندپایه ایرانی: اگر واشنگتن به توقف حملات خود ادامه دهد، ما نیز حملات خود را متوقف خواهیم کرد.
‏
🔴
پس از توقف حملات ترامپ علیه ایران، تردیدها بیش از خوش‌بینی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/137708" target="_blank">📅 17:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137707">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
اولیانوف: درگیری ایران و آمریکا راه‌حل نظامی ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/137707" target="_blank">📅 17:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137706">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPtB6lflaxaOEO7cRKROWxLG_dy6ZwxLI-fOxMoP0uo7ZQ2-yaohV7UT2C5_dsN88J-W30FxUJI_Oz4L8vu252WFLYW14bUp8kk8OGYT2uTD0V4csJcm5weGkZtNqqWWBk0PXhPz4nwgK0rQ5agQRCKMvdel4Gb6VmIOPUpiK3p8XWmQQYFPUTdETuVA4OBdSiAdJ5vYZNMsGa4woeSPE6I0jPbwikfwel67EJAEKcL2Jz3B_aQLGePTtRoyv-FkX_8auQMrHydeF9oenfS2m4THaCTaWI-lwFRZIKfoqvUhq53v8Co10hLSLWm5ffJKVBFBsZdDjoHx9CuIkgv1SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
العربیه:  ایران آمادگی خود را به پاکستان برای ادامه مذاکرات در ژنو یا دوحه یا اسلام آباد اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/137706" target="_blank">📅 17:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137705">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
مقام ایرانی به المیادین: ما آتش‌بس را آغاز می‌کنیم به شرط آنکه طرف امریکایی نیز به آن پایبند باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/137705" target="_blank">📅 16:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137704">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
فوری/ الحدث: واشنگتن و تهران، پیشنهاد پاکستان و قطر مبنی بر از سرگیری مذاکرات را رد کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/137704" target="_blank">📅 16:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137703">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
منابع سعودی:‌ ایران به پاکستان اطلاع داده است که با ایجاد یک کریدور جدید در تنگه هرمز مخالف است.
🔴
ایران خواستار از سرگیری مذاکرات در مورد تنگه هرمز، سپس دارایی‌های مسدود شده و در نهایت موضوع هسته‌ای است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/137703" target="_blank">📅 16:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137702">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
الحدث به نقل از یک منبع بلندپایه:
ایران به مسئولان پاکستانی اعلام کرده است که از مذاکرات خارج نشده، بلکه «آن را به تعلیق درآورده است»
🔴
ایران به پاکستان تأکید کرده است که ادامهٔ مذاکرات بر اساس یادداشت تفاهم ضرورت دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/137702" target="_blank">📅 16:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137701">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfU4xEmFDb4UFd1WSFDJABER5cHaIN7VoyhsUEBpyYmJzea8p8kRS_OLk9IgcwPbih5Wb1IS7pdiZGRSRHMQNZepDdj9wPVndeoWqmVVchk4FlGsfqKolM1IuTkMqK5Hb5_eKHlLniJ68V30Z6Ex_mV7iA7hVU7IrhUFCJQHTNNBYCMfkegXeCDhwyyZ3xhVCtXpQS_bMAJ8-qPfOQpiqaWWYzzIcXa48piPbGSuYDuptGUUbV8jbhwoncRCeCbKvwFN-SzjsiSOCl48g_22SbIEBfGUwQR2caLTVvdg8YPX4rjAvKOsS9cQ94WeobbySaHu2kZNCkGOVG-Oxp5log.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امجد طاها تحلیلگر مشهور عرب:
ترامپ حملات علیه ایران رو به تعویق انداخت؛ نه بخاطر مذاکرات، بلکه برای اینکه منتظر جلسه رهبران اسرائیل و گزارش بعدی اونا بمونه.
🔴
این وقفه بیشتر شبیه زمان خریدنه تا تغییر مسیر. تعویق به معنی توقف نیست؛ آخر هفته آینده میتونه تعیین‌کننده باشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/137701" target="_blank">📅 16:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137700">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAR03uXTFhPVeQ0hHEEpsT4W7oVA766JKtSgaN-SDZnRWzKOhT88X2sWNxeuZTIr4l9cF2PPC2mLp0vGvo1LW2HChmk2CYleK8ea0NxvOe7h6iQZSej6rHy741yprKTMRqa3xpeW5eST9ktfSmtd4zmuQkLAnxg8OKJmi_NS0MXWFF-iTSZUa6kcTY_ZrGzFzePDJRBoVE9z0QbbDm2ld3wFZCNgbuJQq_CXwylc-skF-xdw1HSv8cf-4zljks-eTrc0y1QOJKX3QV0rqyL5u8fIi7pXRLaP0GlU2zKndAPJbwz64AJtOv1GwlLMPh2T_vrzyFX58HHXn7HAecOVIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حدود ۶۰ تا ۶۴ تانکر سوخت‌رسانی هوایی نیروی هوایی ایالات متحده تا ۲۵ ژوئیه در سراسر اسرائیل مستقر شدند که نشان‌دهنده تغییر قابل توجهی در پایگاه‌های این کشور است. ناوگان به جای تمرکز صرف در فرودگاه بن گوریون، اکنون در پایگاه هوایی اودا و فرودگاه رامون (ایلات) در جنوب اسرائیل پراکنده شده است.
🔴
فرودگاه بن گوریون: ۲۷ تانکر
🔴
پایگاه هوایی اودا: ۱۳ تا ۱۷ تانکر
🔴
فرودگاه رامون (ایلات): ۲۰ تانکر
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/137700" target="_blank">📅 16:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137699">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
سفیر آمریکا در سازمان ملل متحد به شبکه فاکس نیوز: رئیس‌جمهور ترامپ فرصتی را برای مسیر دیپلماتیک با ایران فراهم می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/137699" target="_blank">📅 16:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137697">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ES3laskisRInyiLGYWShg_ko2qoIrI-GLeEQDpTqn6U5EfmqUkjDQ5dk7R7SjJUyg8yoEPvFU6goBPT_dYjUrGrAIkQsUBE0dKhSLn-9rRTcz1j6PuhZGmeAHcW8Zef4M6zM0gIV9IkYVRpf3WrnD0uSsqwIZ9dZus1RMrx6qMIIajukp5AD1ExqcoxNjRrE-7BJNcjKAfsYShO7ryJpkRebusOenxFcEyvOAULlpc76SXjsw2pIJl8eAk_LCeq3T6jn8IrWj0Z1OfchDTZHy3qX7TBCugawnvvcSzd4xuga1n4g5l5kpLpZE6SLhUcpR2ZODF4ctYiiMWR_us2jWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pyrHeisv1KRH0jZ0_n2spCyZLPn9xBKdcYsNgbwzQ_0UOp2bIm-hjaNznyIggUOPKtcRNzOoG3R84ZOCk_GC9OmSY3JXZCBdVvJercuB-KwfKAzpw_v6Ap4_UJ2FEt19IPPSsf7pMhDFfl5xh8GmiTfZN_er2bQ52lv6-Aw0FKWcNhQa62LW5W1hx5L3liZ9G8xLyJQTIPMdVTScgW7rxTvxsJoWUqLPpIrxpne5Rxgnuw0LXmwnmhhgge9pBYIySzGnr0B1usJa83EdwYr_TdzdrFq0ROcQ-5sEfgk1nsRTiveenlfiUvPFW5m78qDnM_U5vmcauH0N_H9BUMMW-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای ناسا، آتش‌سوزی‌های گسترده در پالایشگاه نفت جازان را نشان می‌دهد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/137697" target="_blank">📅 16:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137696">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHtklxFPGmCGsf65jNdKSOnajw_Qcz45TC9TI1n2JNGI4LxdsOZtd81SuP9UL31pGURbW1Ic2FU_F9OrfuRHU2C1wD2uIL7zDmGztfKnhgSoMKJx-4_jqLw71nirAQl2X-aAjT3dS2GpOEGwPDOOVUvNjS9Wy0XHPAV1vV7GpFcimDZpm9n_zVRmv_jXx5RNXtRMVLYEe903NSpZoFzEjpcXk7MVCq-wV9-F5XkXCMBLcGKd5umr3Urn4Tft_Gdi5_rulGk4rMn5yM3jt5qYoAHGJEu72qrSvW_xRi4jlb5X2BCAR6dnajRL5SvYuU2PSs3c40OgcH8ull2E3KRJHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جاویدنام #طاها_نادری_سمیرمی
🔴
گاهی برای «آزادی»، باید از «خود» گذشت. طاها، ۱۸ ساله و ته‌تغاریِ خانواده و عاشقِ کوه و هنر، در میانه‌ی میدانِ حقیقت، ایستادگی را انتخاب کرد. در اعتراضات دیماه ۱۴۰۴ گلوله‌ای که شریانِ پایش را درید، نتوانست روحِ بزرگش را تسلیم…</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/137696" target="_blank">📅 16:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137695">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5797ffb0d1.mp4?token=uaPVIOWSEQWBjeF3oWqNMk9GxryRz6BkmyHaH8LlXOjiWSTq6fj4XJqy38LJXmIhVDBxRIaqMW-skl88fU7bXrUWkjA-1hs-nw8Dw4xgzwtqn87fTb3xTU7pgvLD0LTqHee045jk5iI9tIwR1svU-nVGYVqGyEinH1V7HCQcAi7C8wgMeb4f04_IMHYhlZRqU6qSnbK7gSFHWJAFhPJWjLOBj_Zk77O2byaZYkntoUnqoZGwK7vINjIDE-ODOMAI9j4lMSDLlA43Ll9Ug7n7-XHC01Z7xcp7JwYrhDxH7N3KWwdFlU8FYKmduxz4NbrrU3HmoYOFwm7K9cU093zDIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5797ffb0d1.mp4?token=uaPVIOWSEQWBjeF3oWqNMk9GxryRz6BkmyHaH8LlXOjiWSTq6fj4XJqy38LJXmIhVDBxRIaqMW-skl88fU7bXrUWkjA-1hs-nw8Dw4xgzwtqn87fTb3xTU7pgvLD0LTqHee045jk5iI9tIwR1svU-nVGYVqGyEinH1V7HCQcAi7C8wgMeb4f04_IMHYhlZRqU6qSnbK7gSFHWJAFhPJWjLOBj_Zk77O2byaZYkntoUnqoZGwK7vINjIDE-ODOMAI9j4lMSDLlA43Ll9Ug7n7-XHC01Z7xcp7JwYrhDxH7N3KWwdFlU8FYKmduxz4NbrrU3HmoYOFwm7K9cU093zDIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بالگردهای CH-47 شینوک آمریکا
تو ارتفاع پایین در دیرالزور سوریه دیده شده
🔴
منابع محلی میگن این نوع پرواز برای نیروهای ائتلاف غیرعادی بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137695" target="_blank">📅 16:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137694">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b4cd8f6ff.mp4?token=tcyG7Nh18zi3ZNdySpKz7j9dPwlUwehovHqo7iOPYZlsJ-7PadTLvMINjo3VE7FbWaMFouXQRdaS-fXo6jbLhyRocrL7z6Xa6ewmKsESGvXWyFubqfugkKC1SS5GUuUTu0a-anvrzQQLb75gRCAVAVGSZ7Wzu4i1ynT_RWR2lpwfoyOPvsGWcz51zuhwc_k-zaDsZRkpbYDYtx4nEmpUDOgjbvklLBpzJ11D4PeAZsHlFN5sCWdlkuBSs78GDwwTa3M7QUE4cMbeHBH53hDqfDpgUo4IQXDxpWm4Cc_e9dkIPMBIo54KtwLuyN0G2se1Cjp_wHVkkvxPmcMjkIXSHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b4cd8f6ff.mp4?token=tcyG7Nh18zi3ZNdySpKz7j9dPwlUwehovHqo7iOPYZlsJ-7PadTLvMINjo3VE7FbWaMFouXQRdaS-fXo6jbLhyRocrL7z6Xa6ewmKsESGvXWyFubqfugkKC1SS5GUuUTu0a-anvrzQQLb75gRCAVAVGSZ7Wzu4i1ynT_RWR2lpwfoyOPvsGWcz51zuhwc_k-zaDsZRkpbYDYtx4nEmpUDOgjbvklLBpzJ11D4PeAZsHlFN5sCWdlkuBSs78GDwwTa3M7QUE4cMbeHBH53hDqfDpgUo4IQXDxpWm4Cc_e9dkIPMBIo54KtwLuyN0G2se1Cjp_wHVkkvxPmcMjkIXSHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منابع عربی: دود غلیظی مناطق وسیعی در اطراف پالایشگاه نفت شهر جازان در عربستان سعودی را فراگرفته‌است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/137694" target="_blank">📅 16:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137693">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f32055b970.mp4?token=rSetmW7G041ieLtBzfmXRqIa70qgwc8alLJbLpiEqMJ5qSLesIjwCDxG8f9d4NF0SRRscPvfSqRp5YT4tOKf6JjMWA_F7IdtknYzc_8GQFwsk69VNkT93dD9nGXfEdbG8KqvNUCICt3_2mtIBNdu-ecMXNovt9Gb-17__0MGva19YwjX2HSzRG1Z-7sSIvUbxAScfdNM3XmzyRPCVzP4qBIIGwxfdFfs-vt0EkKQxNilMcVYG8fI16SHCbsrLXYy9be7EA85V8Wilz3efJewWN1n3S43CgOb6vXkx5RfYZVf_kcARi7kKhwWWTvZJSk4R9wcJCvVg2fuJPm2CEsS6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f32055b970.mp4?token=rSetmW7G041ieLtBzfmXRqIa70qgwc8alLJbLpiEqMJ5qSLesIjwCDxG8f9d4NF0SRRscPvfSqRp5YT4tOKf6JjMWA_F7IdtknYzc_8GQFwsk69VNkT93dD9nGXfEdbG8KqvNUCICt3_2mtIBNdu-ecMXNovt9Gb-17__0MGva19YwjX2HSzRG1Z-7sSIvUbxAScfdNM3XmzyRPCVzP4qBIIGwxfdFfs-vt0EkKQxNilMcVYG8fI16SHCbsrLXYy9be7EA85V8Wilz3efJewWN1n3S43CgOb6vXkx5RfYZVf_kcARi7kKhwWWTvZJSk4R9wcJCvVg2fuJPm2CEsS6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزارت دفاع روسیه تصاویری از آزادسازی شهر شیفتشینکو در جمهوری خلق دونتسک منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/137693" target="_blank">📅 16:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137692">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
سی‌بی‌اس: مذاکرات ایران و عمان  شاهد پیشرفت بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/137692" target="_blank">📅 16:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137691">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
فوری/ الحدث: واشنگتن و تهران، پیشنهاد پاکستان و قطر مبنی بر از سرگیری مذاکرات را رد کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/137691" target="_blank">📅 16:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137689">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fodtex7QUwq6RLixIzn4zqxi3AQmOQqU9Qv2sYyN5xH5j0gVUGqiJtg0AttlGffp9U4HNyW8v0usGPkRbBUDPbHStlXEGKiR4g1SSfm-3JYqtuGzzOSp8x0J4Nfy_hw0_p7ur37DqdfoDBasmA20tK5RdVcMnIROVYlQvaBd5nH6DJsGd547Sx_BDRMJL9LqGobwawrsb-jk9uNSP2CDtWW0S-sdKNeTMODbfXR4Nd9Xkw14UAxH6kYwsSiSHDZnithrphYO6drwT-QZfH0P3vEfGWaHeCAJVMZsBvdtjZtD2SEJUcvQVf-BD1FsoIDA685UWDjFshkLPe9DhjSqUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dZPASV0NJqJ55iuYfBKP9mdmQBeDY2kKFQZFYnEShEwbRMSLaIeyCtonOdgabct69aUjzVSy0VLMGHT-spaJ13WjHi6lemJHmo6OO49vE_lYBGk66mOPWyzGKuF_aHcWV0bz_K2t8hCxwwPwOYKp2U8EP0zC59RxTPlcfBiUnEwaVInuTxZNCQfj039UKysupEUipheeoWoXHNmSny4u4cHvvfFq5XE2_TYlcTIZw6wz4pfUY7y3G1t5RZr0QoVryKqsEtMrTa6fJI4tT0Jx1XRXprs_KTLFrf_UF7JzSm6d6qltPa4Tq6aKitq7VcJF5wds0RFVL9zhrwWpjlFXnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
برای اولین بار: اسرائیل سلاح لیزری را با گنبد آهنین ادغام می‌کند، اقدامی که می‌تواند معادله دفاع هوایی را تغییر دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/137689" target="_blank">📅 15:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137688">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
فایننشال تایمز: بیمه‌گران اعلام کرده‌اند که پوشش بیمه‌ای برای محموله‌های مرتبط با عربستان در دریای سرخ را متوقف خواهند کرد
🔴
این تصمیم پس از حملات انصارالله به دو نفت‌کش سعودی اتخاذ شده.
🔴
برخی شناورهای سعودی برای جابه‌جایی محموله‌ها، تغییر مسیر می‌دهند، بعضی هم سیستم جی‌پی‌اس خود را خاموش می‌کنند تا از باب‌المندب عبور کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/137688" target="_blank">📅 15:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137687">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
به گزارش بلومبرگ، الکساندر نواک، معاون نخست‌وزیر روسیه اعلام کرد مسکو محدودیت صادرات بنزین را تا پایان سال ادامه خواهد داد؛ اقدامی که در پی تلاش دولت برای مقابله با کمبود سوخت داخلی انجام شده است. روسیه همچنین قصد دارد پس از بهبود شرایط بازار، ممنوعیت صادرات گازوئیل را لغو کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/137687" target="_blank">📅 15:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137686">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
کویت به‌طور رسمی توافقنامه همکاری دفاعی با پاکستان را تصویب کرد.
🔴
اقدامی که به گزارش رسانه‌های پاکستانی، گامی مهم در تقویت روابط نظامی و امنیتی بین دو کشور به شمار می‌رود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/137686" target="_blank">📅 15:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137685">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
شخبرگزاری آناتولی به نقل از منابع دولتی پاکستان، بدون ارائه جزئیات، از پاسخ ایران و آمریکا به پیشنهاد مشترک اسلام‌آباد و دوحه برای پایان دادن به درگیری‌ها و تشدید تلاش‌های میانجی‌گرانه میان دو طرف خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/137685" target="_blank">📅 15:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137684">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
امیدیه و اهواز با ثبت دمای ۴۷.۷ و ۴۷.۶ درجه سانتی‌گراد، در فهرست ۱۰ شهر گرم جهان قرار گرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/137684" target="_blank">📅 15:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137683">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1173bc5673.mp4?token=WCLNsgYpLltfx0mJRasrxFR3cBxcbDDuk8k8mIl7VPt5laxpkkkdi6o1v3D4f_8JzLRTBL1uC2L0T2pFPnqNlcWyOdeE1PicxnPgYbqcfI4LkyqQ5f4Yi2u0WLEpqmKj8K7JVgqT2gtMi3QwLpH6xrPRuG8DaJ_dwdpSBte5-_iRKkiWcgF5CzjeZq7bGnwRkhysll-5xLWHdqiFJvmXSC7IhAitevK3i27hQq9iv_Ild4Rx_DCQkBB1oUeruZx8NMS_VNnyRXemvpsFl0CFCR2dGSNWD0V2KPVwmsZQu4dffXNuCeJj2HZ_BztA544rp34F1Hez8yhUyvQLHdifLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1173bc5673.mp4?token=WCLNsgYpLltfx0mJRasrxFR3cBxcbDDuk8k8mIl7VPt5laxpkkkdi6o1v3D4f_8JzLRTBL1uC2L0T2pFPnqNlcWyOdeE1PicxnPgYbqcfI4LkyqQ5f4Yi2u0WLEpqmKj8K7JVgqT2gtMi3QwLpH6xrPRuG8DaJ_dwdpSBte5-_iRKkiWcgF5CzjeZq7bGnwRkhysll-5xLWHdqiFJvmXSC7IhAitevK3i27hQq9iv_Ild4Rx_DCQkBB1oUeruZx8NMS_VNnyRXemvpsFl0CFCR2dGSNWD0V2KPVwmsZQu4dffXNuCeJj2HZ_BztA544rp34F1Hez8yhUyvQLHdifLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بن‌بست در تنگه هرمز همچنان ادامه دارد، زیرا این وضعیت ناشی از محاصره آمریکا و مقررات ایران است.
🔴
طبق گزارش خبرگزاری ایرنا، در ۲۴ ساعت گذشته، شش کشتی مجبور شده‌اند به دلیل دریافت هشدار از سوی سپاه پاسداران، در آب‌های این منطقه لنگر انداخته باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/137683" target="_blank">📅 15:44 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137682">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
یاایر لاپید، رهبر اپوزیسیون اسرائیل: تل‌آویو باید تمام تلاش خود را برای جلوگیری از توافق پیشنهادی هسته‌ای غیرنظامی بین ایالات متحده و عربستان سعودی انجام دهد، حتی اگر این به معنای آن باشد که ریاض از پیوستن به توافق ابراهیم خودداری کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/137682" target="_blank">📅 15:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137681">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
حدود یک سال پس از قتل فاطمه سلطانی، دختر ۱۸ ساله‌ای که مقابل محل کارش در اسلامشهر با ضربات چاقوی پدرش به قتل رسید، دادگاه حکم بدوی این پرونده را صادر کرد.
🔴
بر اساس رأی دادگاه، پدر فاطمه به ۸ سال حبس تعزیری و پرداخت دیه محکوم شده است. برادر فاطمه سلطانی اعلام کرد این حکم روز ۳ مرداد به خانواده ابلاغ شده و آن‌ها نسبت به رأی صادرشده اعتراض خواهند کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/137681" target="_blank">📅 15:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137679">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ne3fYycpta3BUWkhvZxTZpvR1YIqPfOGz9bZBHVLPGkQVNG6r2j_8G2UH_YYUKiIZW-yp4aYR2_QDbTqBApykEljNMYlROSqpLhctgiHPmON-A6zs8OtaZSLbAQuulr3x2d7uXqwWOT4XqtV-cd3gTpxpR694liSSnKi3gaXTaSUIATTXFm1D4-0gk_KeH6RxpxW9vZZC_HGN36jYaDESqilTF2Q_JGnz-5q9hxsPqXodh_XMhHCHZxYhgRZHAWMYNRXJEHreo-VbhSrGy8eQhLODqR3usNQpzb9ofyqqCM850gWgoN4nojSecbZD9WJK4YHc0fEXelR_mMbsveHHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i1uW1-95uzJEKP2KQwKO5J2m4JOGaQcDiNzzdYp57bjUCMdL-I7_E_QxyuIh2UUKNIGyhoU6A-BgLBNXrv_oBTcSvvxKvIBxD9m05nWTLXq8LhX093dWd6lHWqyevuqeuoZ7Jnhi2ruq3b8eROnRiTH14fF-Qy6FWYjp9zBDN_LXbi72dnz94SkrzQ5hhzLGb5KdbHyfr7rp8MBD9cDpULjEFaZFTmion9rw722X3vPRs1ef4RAB0VBIENk3yAdRXrzR0_FiM7z5aRjq8cyNDFY9OrYkculdCu71dLXuokm012hGj1BgRKazu6UqF7rVUdxI8SBEcgu5YpCSrY6CkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
برای دومین روز متوالی، آتش‌سوزی‌ها در مخازن پالایشگاه جازان در عربستان سعودی همچنان ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/137679" target="_blank">📅 15:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137678">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
دفاع پرس: انفجار نفتکش در تنگه هرمز با مین دریایی
🔴
یک منبع آگاه اظهار داشت: ساعتی پیش یک نفتکش متخلف در تنگه هرمز که از مسیر مشخص شده توسط جمهوری ایران خارج شده بود، بعد از برخورد با مین دریایی منفجر شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/137678" target="_blank">📅 15:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137677">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48b85e271b.mp4?token=N1eRg4B-z5IzFUDtkNSp0f05JXYyTI6g7hjymPGW_0wGrTMbVMomd3CmL6Vxz36hO47MoJ7fFM8_iOUJTUFxv2tEueZMWZHm87CtdKwwp3TfrpH6iKD3qsdjsbjqiLRDWOTpfXEAo7W-H16_XNKr-5tgZp6ySyxTZalh-yecFVPKExvxPlaA1-kLzA7__BI1JfEdAuuUq5a8alMu1RqlJuyeJbaDMGb28E9Zb37dDRnhOyL3v_As1SEGorL_SdB9uibnBLtlyBFZ9I8ib6VuHQmcUmWKrI3kVncWrgPKMwYXzy_HRe8om6bQ5UOUs2BCg6aJqnkOUmHQovRJxZy9kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48b85e271b.mp4?token=N1eRg4B-z5IzFUDtkNSp0f05JXYyTI6g7hjymPGW_0wGrTMbVMomd3CmL6Vxz36hO47MoJ7fFM8_iOUJTUFxv2tEueZMWZHm87CtdKwwp3TfrpH6iKD3qsdjsbjqiLRDWOTpfXEAo7W-H16_XNKr-5tgZp6ySyxTZalh-yecFVPKExvxPlaA1-kLzA7__BI1JfEdAuuUq5a8alMu1RqlJuyeJbaDMGb28E9Zb37dDRnhOyL3v_As1SEGorL_SdB9uibnBLtlyBFZ9I8ib6VuHQmcUmWKrI3kVncWrgPKMwYXzy_HRe8om6bQ5UOUs2BCg6aJqnkOUmHQovRJxZy9kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فضانوردان روسی و یک فضانورد آمریکایی با فضاپیمای سایوز از ایستگاه فضایی بین‌المللی به زمین بازگشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/137677" target="_blank">📅 15:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137676">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
الجولانی: ما در تلاش هستیم تا به یک توافق امنیتی با اسرائیل، با مشارکت تعدادی از کشورها، برسیم.
🔴
ما از درگیری با اسرائیل اجتناب می‌کنیم و هیچ علاقه‌ای به آن نداریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/137676" target="_blank">📅 15:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137675">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
عضو شورای شهر: گردن‌کلفت‌ها جای پارک را به مردم می‌فروشند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/137675" target="_blank">📅 15:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137674">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
گزارش از شبکه العربیه عربستان سعودی: آمریکا و ایران به پیشنهاد پاکستان و قطر برای از سرگیری مذاکرات پاسخ دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/137674" target="_blank">📅 15:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137673">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJe4fSHHw-2bew_bJK5SXbo-4pcfm7pOzzV4178WTcdSZmfksqqa3HKOD3Aj-kwvaZhQKaU8PYujo2l5DI5VDan64avEfyjxV5niPlCdeTqfcqI_VFCa29-JdpLxQYpPJJ1QAgy9Tjg6uSSgNWDFdC-FGRCb0rUbXeQLpI0t4INsHe7bUBJ87ULLf8sIeI6FJaN4bVFaeo38yCdiNmYwBvKxhnttmcdfXOrRFYnwrcAwck5xH4fFSuyj_vEVYnqKr4oTKZv9ogSsYoxNsMlFb-7NGzmmzi12GPiTsxF-PxyS4LG2o3jzXW1TYkaD4Y9Fj9tUWFgn4a_PxTY96DwAFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: خسارات واردشده به زیرساخت‌های حمل‌ونقل باید از مراجع بین‌المللی پیگیری شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/137673" target="_blank">📅 15:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137672">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
عراقچی: ما حاضریم روابط خود با کشور های همسایه را از نو بسازیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/137672" target="_blank">📅 15:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137671">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
خبرنگار حوادث: تو قلعه مرغی تهران جسد یه دختر جوون رو پیدا کردن که خانوادش چند وقت پیش اعلام کرده بودن گم شده و خبری ازش ندارن.
🔴
لیست تماساش رو درمیارن میبینن اخرین کسی که باهاش تماس گرفته دوست پسرش بوده و آخرین جایی هم که رفته خونه دوس پسرش بوده، پسره رو میگیرن و اعتراف میکنه که خودم کشتمش، بهش میگن چرا کشتیش؟
🔴
میگه چندین سال بود باهم بودیم اون روز که اومد پیشم خیلی بهم اصرار کرد که برم خواستگاری منم عصبی شدم با یه چیزی زدم تو سرش و کشتمش
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/137671" target="_blank">📅 15:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137670">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72b207bf62.mp4?token=SrxfavkvodM41u8PrB5kwSTKh3yJqSKhgT3GCT8E56jPld215VVA7_VbBlFbO1fr88zrue3Wr8DErw96YjFjRfIzbGvO5xGqofX6aq9c2UVB1b7LNrek_ivplV9EPkQeyGbP-irwomTuVJpuQ_b2kl6gBaVc0L308iFcZ4NipFAy_ZZZvOp3XAgASmLhx9AVPtLp0d76hbrF2bkkjRCYR3yeCax-OApvnkPT4S_1xVjQBOAR-JiaoGWgSS0TkOhknhOCwt--8ggg1Ow91CX9Q0-keGPZx1GQrGooQ_shfOgh4pnoVQoqa8giMiG-zWU0aEFzG5iE-qdqD73dOe9KUYO9tRlruaq_AbuRGetsg5YBGUPF6HA_NmJJl5Y9IHCPsgXY2lEkl1kkMH8UXjfpoRxmXL0rwYfQcxXFooNo_PWj_fT2iXrlL_kTZQhoE0-DlZZsdXjHPTISAty9Bbe9Os1HMQN9n38finPNq-lAnwvTiv6YyzornEAQIwd_XffIKcYGQ_HSK-rOHKt0JTIrin0KRkufqgMM6mzfJxHIte5V1OXCS-Dyo0I3lObFSqu1d2Uhl4TCFI9_w96vxwmGe2Ovav0veDqizkR76IFA4Jm7JUvDSd2NOHRUIFg4hk_99GO49Ox2bExH4vwYnGeZmB_bUVo8dJ-UlvanVtDSN_E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72b207bf62.mp4?token=SrxfavkvodM41u8PrB5kwSTKh3yJqSKhgT3GCT8E56jPld215VVA7_VbBlFbO1fr88zrue3Wr8DErw96YjFjRfIzbGvO5xGqofX6aq9c2UVB1b7LNrek_ivplV9EPkQeyGbP-irwomTuVJpuQ_b2kl6gBaVc0L308iFcZ4NipFAy_ZZZvOp3XAgASmLhx9AVPtLp0d76hbrF2bkkjRCYR3yeCax-OApvnkPT4S_1xVjQBOAR-JiaoGWgSS0TkOhknhOCwt--8ggg1Ow91CX9Q0-keGPZx1GQrGooQ_shfOgh4pnoVQoqa8giMiG-zWU0aEFzG5iE-qdqD73dOe9KUYO9tRlruaq_AbuRGetsg5YBGUPF6HA_NmJJl5Y9IHCPsgXY2lEkl1kkMH8UXjfpoRxmXL0rwYfQcxXFooNo_PWj_fT2iXrlL_kTZQhoE0-DlZZsdXjHPTISAty9Bbe9Os1HMQN9n38finPNq-lAnwvTiv6YyzornEAQIwd_XffIKcYGQ_HSK-rOHKt0JTIrin0KRkufqgMM6mzfJxHIte5V1OXCS-Dyo0I3lObFSqu1d2Uhl4TCFI9_w96vxwmGe2Ovav0veDqizkR76IFA4Jm7JUvDSd2NOHRUIFg4hk_99GO49Ox2bExH4vwYnGeZmB_bUVo8dJ-UlvanVtDSN_E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جاویدنام
#طاها_نادری_سمیرمی
🔴
گاهی برای «آزادی»، باید از «خود» گذشت. طاها، ۱۸ ساله و ته‌تغاریِ خانواده و عاشقِ کوه و هنر، در میانه‌ی میدانِ حقیقت، ایستادگی را انتخاب کرد. در اعتراضات دیماه ۱۴۰۴ گلوله‌ای که شریانِ پایش را درید، نتوانست روحِ بزرگش را تسلیم کند.
🔴
او حتی در آخرین لحظات هم، نمادِ استقامت در برابرِ تاریکی بود. امروز، کوه‌های شهرضا بیش از همیشه دلتنگِ گام‌هایِ استوارِ او هستند.
راهش پُررهرو و نامش جاودان.
🕊
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/137670" target="_blank">📅 15:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137669">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c97f68de8.mp4?token=fNmK2Ydfml0oMPzZcm_TpTin0Pej_fq_NALvU3mg40fsEN9_zgV86Lo-xZ7kKxsZkO-SIt9IJSdQtcgx_bwtVkbHDebQrxkYhX0H1Stpx1b48UaHVugAIhgoE8SIv8brB9n-bOa6vA2lht9sqjdaILrZlWa5ZhfABfKTJ80N3-YgB6XGWbw5b5gSaPCQkX0FyhkvF5XOVGMrAD8B5FOzoT5DHYO45qYjgjXsQOK3VUY2LLcnPFB8mdCtsT1i1cEB8z74ElYriYW9_NmDXEf_gBoitoYJOiydkmBOQP4YZL1itqCpcOMMZLHEsdxop8-EEMOw60GUsbqlP16v3u0NBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c97f68de8.mp4?token=fNmK2Ydfml0oMPzZcm_TpTin0Pej_fq_NALvU3mg40fsEN9_zgV86Lo-xZ7kKxsZkO-SIt9IJSdQtcgx_bwtVkbHDebQrxkYhX0H1Stpx1b48UaHVugAIhgoE8SIv8brB9n-bOa6vA2lht9sqjdaILrZlWa5ZhfABfKTJ80N3-YgB6XGWbw5b5gSaPCQkX0FyhkvF5XOVGMrAD8B5FOzoT5DHYO45qYjgjXsQOK3VUY2LLcnPFB8mdCtsT1i1cEB8z74ElYriYW9_NmDXEf_gBoitoYJOiydkmBOQP4YZL1itqCpcOMMZLHEsdxop8-EEMOw60GUsbqlP16v3u0NBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هدف‌قراردادن کشتی ترکیه‌ای توسط روسیه
🔴
یک کشتی باری تحت مدیریت یک شرکت ترکیه‌ای در نزدیکی منطقهٔ اودسا در سواحل دریای سیاه اوکراین هدف حملهٔ یک پهپاد روسی قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/137669" target="_blank">📅 14:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137668">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
سنتکام: محاصره دریایی اعمال شده توسط آمریکا بر ایران همچنان به طور کامل برقرار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/137668" target="_blank">📅 14:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137667">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
نیکزاد، نایب‌رئیس مجلس :اقدام نابخردانه دولت اوکراین بی‌جواب نمی‌مونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/137667" target="_blank">📅 14:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137666">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
هدف قرار گرفتن یک کشتی سعودی دیگر در دریای سرخ.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/137666" target="_blank">📅 14:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137665">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLwvP4tMOhVAp6fKaZhPfRhxRLeLr00MrcC2jKzFSOxZyQb5j92vqRU6ELr_GjVoNaJZobDj5m3TvCNUALP7kDeLlG8DOLguy3It_Mn-u1tbJB94QW5k57v3PXTDpxF9nX-R-31djVCsN1wgwaSUfSdl5t6kT2F-pZSLbHFxvUJPhOZ_RIqS2fTro_-aLxlaEMTkBQEx95YueweGaWMuEbr8kEC30QgFgy9nkBdRr4hX_W9bDGNPP_glFpowfgLA_QqF_ljfiurG-TzaPptQbegyejkexYfRS5tSyTL_VoPKm7AlUacVyN-rWw_U2mntZ_TwLDEYjveJcpdXIBIBGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هدف قرار گرفتن یک کشتی سعودی دیگر در دریای سرخ.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/137665" target="_blank">📅 14:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137664">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3_ZCo43GAUNLQbkkICBh4gaMFWlugvT26GqJ-KLr7b-WXLSidAPeZuniXSw23ATPmVqOi2Kh5P7l5Qlj7p6jiKKrK0iuJ2DoBsic0sVpC30STOTezM0esapD6niyJM34IaurdbDT7lM_2Z2SEGMLCuM9rP18taPFptSHVWWbZYQGvzj5h-NsoBsu8FUWnsCeMZD3ISOwhyVqFBu-sBieHtsy_KbJ0bIe1sc23I69RUVrwEKhfWlSo0awt-CimML-Qs-Mp6kDHnuDMkIdvEaKHloKmbfU3s6ygVRaORwREqyoxN1bqVs_XgXX8trtrQ5RTIX9k1jPECh_bsDAPhS0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به دلیل جنگ ایران و آمریکا، گرندپری فرمول یک بحرین به کشور مالزی منتقل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/137664" target="_blank">📅 14:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137663">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
الحدث به نقل از برخی منابع گزارش داد که امریکا و ایران پاسخ خود به پیشنهاد پاکستان و قطر برای ازسرگیری مذاکرات را تحویل دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/137663" target="_blank">📅 14:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137662">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
وزارت خارجه آمریکا: هر شخص یا نهادی با شبکه فساد «بابک زنجانی» داد و ستد کند تحت تحریم‌های همه جانبه قرار خواهد گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/137662" target="_blank">📅 14:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137661">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
پزشکیان: حمله به پایانه بنادر و همچنین حمله به زیرساخت ها و راه های ریلی و جاده ای محکوم است و از طریق مراجع بین‌المللی این جنایات را پیگیری میکنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/137661" target="_blank">📅 14:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137660">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHO-UGwMk8rbB62mZ2n7hKecbxJbfGFRQNPKbi-8YlZtKqJlIccHDz4ufLHHAtwmi24uH4S0C5q2NnfNk6tx9UryfPFM6ulKaMDPT2KT_omlLpATDp6DOKjrhCCEOHV4HGjGZagfJszoBmsQdFpm3mMTfEVcXs9JKrPrvsR00XjCIsuxxgzW8nqI8aqWeLtcvmK7HJBZWsT6hIFjRjSRj2pfaVuebem_nbT1dZCPA6vgaBqPeNlR4Dui7eWzaGTKUmbfK-M9CUT2e8Twm9FiYHnjGr2zyjsHA4iNOO9Q-U50QWZug0o-bewIkvEfDKzNew9W-s34amMThEeQPFJo3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
گزارش شبکه NBC News:کمبود موشک‌های رهگیر به حدی شدید شده که فرماندهان محلی آمریکا ناچارند تصمیم بگیرند کدام پرتابه‌های ایرانی را رهگیری کنند و اجازه دهند کدام‌یک بدون رهگیری عبور کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/137660" target="_blank">📅 13:56 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
