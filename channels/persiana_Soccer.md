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
<img src="https://cdn4.telesco.pe/file/ke3b3Gc471rX_h0QW-7LvCQQIhGdjPTTFbT9vtWB-DVPMhbzrA_OG7pX3TxZoD5X9oSv8QZX08TOIblWwfUkBhCNPxfOcP_QNoL5QIFWFJ1jA65qG9oiXk4bQgj56OsJJ9Ve-UraBGRC--1hu0jT0SjtvXkoMh63rKTXfiQ1-b6NotS6pE84nyHVC9JIF_GeHEtzy8ZgtQacCd0I8cpCQHwNAJDjesPJl76r_ifUpMbhGhTJEjTAQsxvuYkqvCuFA-MhGoyfLEeHmCBGkWOsTJpaQi19Y8ygkBFhCbLFin_yV4Fv2yqWtI-kOWTg4h6ybrqZYIQwC5Icfh2bhzMgEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 169K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 10:00:44</div>
<hr>

<div class="tg-post" id="msg-23035">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3RhCZ9anrdLFf2QfGWe7b8PVRe2TfBA0iajAPjBJMyxNb8Q8xBAS2VglrY_fWAIYyzawB93o_CrI3v6R77k_-0c-ZutdKECHcx9nizigLzlQ2QJ_-rxbOe09TqCSGPJA4GpTVR1mXQKj3ECqb2hLl2aFGe6IrvE-I3H5RP6y_38UeYC0vnFB-9tA_a7YlhSloJIGBApeRc4hucXuj_6DAogg_BjevkBG0ewGtZxHl7uAQagtIEpSOe-DHMUxIaVcri9CJ0t9zeSd7o0UBfS6R6mVr10tsJ1tWH_0Ffe4XzaYiZYlzIYrDufpmQuhDBh14UtawRKC3GLARurPaFisw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
سوپرگل استثنایی مایکل اولیسه ستاره فرانسوی مدنظر رئال مادرید دربازی دوستانه امشب فرانسه ایرلند پیش از شروع رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/persiana_Soccer/23035" target="_blank">📅 09:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23034">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCaXGm5RyyCJFbozdJzf6XSutEqafz7ppi7FdWipmRZhhD3LLsSUbbhNaaPo5d006GrZB_8B3-ytGVqne4RqxzA3Ahq9l2IF_aMI2MTEujgQ_M4j8dbTpVs3pRFECOIESwBLcFsvs6iplRcND884S692Hag55rXuYXwlTLyOY3Lbx63Drq3p1QmLoUdcfuRNFUHhRi9bjTmjulzoNSMA_5UelRULfX0gLebYXxQHvPg8B1ioaJ0S1Kos7egWYEc4HU2ZKpzKbRocvpE3HlLJhbwjoqgPYrg2Wb71gsIIl9l5Nih4OrZjrQ9E5ibv-rVHkCwEo4BWfwQEoOLBMd5tWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات
|دیمارتزیو:
فرانک کسیه پیشنهاد تمدید قرارداد 12 میلیون‌ یورویی الاهلی رو رد کرده و میخوادبه‌رقابت‌های‌سری‌آ ایتالیا برگرده‌. یوونتوس علاقمند به عقد قراردادی سه ساله با این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/persiana_Soccer/23034" target="_blank">📅 09:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23033">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j16g0JHaoOcYGUS5ejxQOtefppzEGSTnXQqHWfmZEdVEitKzM389Bm4py03I0_F7OHXtr7eTqNdF6M2bMS2rB4wYPfH1-bke_MVVx3YKj7AhvLGVRJuBqVq7RWWiJHo3lYGRVo9aAbx3dlK_b6mBAsLyAlnzAbJJvesFpnXRwz6XAaWSkRVnwWMpfyEgIDlQgHk4-LlaMmPxYNTdJG8J13XpaXu4dphr4e76w6yPh0KOmO48culHhCarxX3w4xkBXMrA0ksxIWC3t5xiP4jH7bSBNzWTqv50t3Qlgvt3kIRs7Z6a5w34gsPnzImleBgJpHZyoV-49vo39uVt614rLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛برخی‌دیگه‌ازشبکه‌‌های‌ماهواره‌‌ای‌که‌بازی های جام جهانی رو به بهترین شکل پوشش میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/persiana_Soccer/23033" target="_blank">📅 09:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23032">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9BKKOWpPrn0xAlsesRggXa368rH6NB0TYvs-xbbBtuskhCQQ320xD143xHSPLhb_l7khi--qLKQiQolgX4vA50CfuoZQ4-gVFZe3aBMh9ZSUocqJhb_8N2ZdcnrgY-RQp-e56j216roi5zCOoo2UdCxYILu94BMgFVw2VUy3tfFB6FjM1cy2bp1VYXVeSlCLfOuEr4UwblwiCp5iyFZom4MI2PEQ3jOrawdhsjQ0q0LXqZzh3Hvo7Aiu1HAXuP2KhFxNL2HxQnmyDeIolWzi74x6nOABjfr0GJFhhXGNsaWqgWO4HRLJw8ok9eE9_mVUXBYlEPuswR2WDaEIT0p2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/23032" target="_blank">📅 01:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23031">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8torLvQiBYaqHZl_jscxmntEGCy1ZQo9aEZzY7xgEnl5YHJMWanMlFwCAAI1UJwFgxtZJXQ3o8FNH_xw2dgk96R6iHXYrQvHBaFijywN0A7cfwFHNQLC830FJanb9xAxckhiXtuC4h8bYf6UBlw29LKDqNfqyACzC-7UBLk934nOwUpvo168oRe6Muxj8UOWMslaRVgx2SP8bL0cPHA5ElrwPBGqVjBXu87PLcXXDpzrOxDvrtFr5RbB6zNzS0pZr6baXHdyl0VAKORE17KD7CZOTdp4raGaay6IlWonSGY59KFJs8vQ9-hspl7V19y88swlKzzzd-pcHNMZCHT5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه ‌‌‌دیدارهای ‌‌‌امروز؛
نبرد تدارکاتی ماتادورها مقابل تیم ملی پرو در صبح امروز در فاصله تنها 48 ساعت تا شروع بزرگ ترین تورنمت تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/23031" target="_blank">📅 01:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23030">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_sEoDag8A7Srtv4-x_Zupv-hN0AWk1OiNpIp5FUZSMvbmpYzJCChRZY2dIsdfw1T9g6ehXyi-iJMLDuBjjeOtNkJzTGSVYKkOT_LKlEUm5S1ReDIRkwv8rti39Ta8N29nSIczH8LGWztRhoKdh8ZBUEMCYDrMrQgKkiUkpEk4Nyn7p1_0naIhQhfbX7WwY-2V1WSS9_RNlqcxAktJUXqJzWxJyVxQiMsk5jHpN91zZcb1s3AoIKBizltrAzh6j8XWvNEBnj504dmyrSyiV8m3W1CE8VZRjqFFwDgdqw4oRgmBf1p74PE38ah7cdgFDRY-BDcTANofr3jr-dAAuoqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌دیروز؛
ازبردسخت‌هلندی‌ها مقابل ازبکستان تا برتری خروس‌ها در شب هتریک اولیسه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/23030" target="_blank">📅 01:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23029">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb89dc70af.mp4?token=KMZTRbMbN9JpUT-mrybGjjQtoL6wqI1iZwND5fgqFLx-R7Hw7IC619dj9x0Zf8_7JlxInOfLHsaNsDFkcL8IGk5LAcWyeAD0qD0EvxjBiwEm8PDgrLMw7icdXbPk5ne4i4R2BJ_DFiM7PCoXXfMUxGsQpoQ7y3qRHa30OvnQuPPRg5kbi4r1kJHDo9m46eo_hoXRB5SamKGXQTxkbaUNCsBY76SMtq7twwsyVHN1Iu0fIMeK7ggHLGLDTOC7ErjLEPX0nMP_tBGDEFosM6sPrnxh4zS8B-uqvCBFsI-95BvAwbWTHmpVPFwXIJRQJktGRt6L2PvwmpcmyR-PLfS87g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb89dc70af.mp4?token=KMZTRbMbN9JpUT-mrybGjjQtoL6wqI1iZwND5fgqFLx-R7Hw7IC619dj9x0Zf8_7JlxInOfLHsaNsDFkcL8IGk5LAcWyeAD0qD0EvxjBiwEm8PDgrLMw7icdXbPk5ne4i4R2BJ_DFiM7PCoXXfMUxGsQpoQ7y3qRHa30OvnQuPPRg5kbi4r1kJHDo9m46eo_hoXRB5SamKGXQTxkbaUNCsBY76SMtq7twwsyVHN1Iu0fIMeK7ggHLGLDTOC7ErjLEPX0nMP_tBGDEFosM6sPrnxh4zS8B-uqvCBFsI-95BvAwbWTHmpVPFwXIJRQJktGRt6L2PvwmpcmyR-PLfS87g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
سوپرگل استثنایی مایکل اولیسه ستاره فرانسوی مدنظر رئال مادرید دربازی دوستانه امشب فرانسه ایرلند پیش از شروع رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/23029" target="_blank">📅 00:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23028">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbZ3T09J7RaB3T8BV9VqRFWhAsQumkN6Gu6TWNXNSQvYna7iJ_tHKmehuW4wNSPzmg0gImO3dleXj1lLgB_kK6jUiQw4eiwx2tjN181mo6BDLXa8640ypwIjaYRoPsoixwkFtUQ5VYjyg4Yh3Sa7o6tlX27fSVH8cZk7hXup9D_iHj6qKa0ZPKRySY4xoCSRDZMPHyPz9leqm1psqAIe2Zvm70V0vImzBIcTMVZNA5CvDg3tYcaU-d8xgt5iCysHLcgbJFFzkjnhJm_k9h29EKgacrzXQ_v8XXmkL3gznfpw-Vqls-iwue_bFPRSymELrBNg_--oDgpzBHFYieXXkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
🇵🇹
برناردو سیلوا:
فکر می‌کنم قهرمانی در جام‌جهانی‌پایان‌بی‌نظیری‌ برای دوران حرفه‌ای کریس رونالدو خواهد بود؛ رونالدو همیشه‌سخت‌‌کوش‌‌ترین بازیکنیه که می‌شناسم و لیاقت بردن آن را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/23028" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23027">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91f877f10f.mp4?token=X8hJYnzePk4xaM8jHdZKzjvCJk_FvLOOVungrXR5MhB9nu_Y1AipTMBo7SO6iDSHyfst7YuoUq2p2DoQiQJurdmVpjLeHTWEmVrVa78tyiVIa1YgnXXOFHzuM8CIPeHCKFIwQHw8eqWHiLf5lTsxWcJTuMnucDSjvu89hLYIB1k-eR2_rECYDe_1paq16dvLBHmuTpZ7EoUfLIBDCd1ZNgvTPpAI0HQIbohzVUCc0eD7RTsvhDLQBGHXRmSuh4mI-kusCwXS6w4tECAVT2QXgt2QR_6XlDnKjLejsIry6aJTgG5jONKm_W4qXUbUHfnJ_4ZrWsQJNDI8_FGVQS_jnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91f877f10f.mp4?token=X8hJYnzePk4xaM8jHdZKzjvCJk_FvLOOVungrXR5MhB9nu_Y1AipTMBo7SO6iDSHyfst7YuoUq2p2DoQiQJurdmVpjLeHTWEmVrVa78tyiVIa1YgnXXOFHzuM8CIPeHCKFIwQHw8eqWHiLf5lTsxWcJTuMnucDSjvu89hLYIB1k-eR2_rECYDe_1paq16dvLBHmuTpZ7EoUfLIBDCd1ZNgvTPpAI0HQIbohzVUCc0eD7RTsvhDLQBGHXRmSuh4mI-kusCwXS6w4tECAVT2QXgt2QR_6XlDnKjLejsIry6aJTgG5jONKm_W4qXUbUHfnJ_4ZrWsQJNDI8_FGVQS_jnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
باتاییدرامون‌آلوارز؛
مورینیو سرمربی فصل جدید رئال‌ مادرید برای کنترل‌کامل رختکن تیم رئال، پپه رو بعنوان دستیار خودش انتخاب کرده تا بتونه حواشی بازیکن های داخل رختکن رو کنترل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/23027" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23026">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rW46pvTa-DxQVwlTTU3JsM8itvPNmmnlVJBW8GrAfnnxbME3RyUAE0bqYSFFUkrriN-cAyqd9psLpFG-bwWSW42nu07hi-ahw0z3JCDbYF6iQgjvvqjI1BkRGAEqy6e0D37Eqmx85HQbknqDXT7rTvDWC3JWbB3QixKGG7XBWG-KFxjWChNfSw7ya4HqM_IHZ9ZWwXgeV9Dk2QEXdG4c4iy8nAGqLHLSZfDo3xNmj3NmPUeZAx_z5i93F85qrhTppC1y5zxLht7MPUhg9ArbtcWXAJlczS2xeMNNO-kYH9DVg4GymwSk1S_zatysEo3GUYgcFpuOzS4YM9YYCJmNhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
توم‌میخوای‌ازمسابقات جام جهانی فوتبال پول دربیاری
؟
🥇
✅
کانال
ورسوس بت
کارش تحلیل و پیش بینی مسابقات جام جهانی به صورت حرفه ای
🍑
⚠️
توم‌میتونی‌از پیش‌بینی جام جهانی خیلی راحت پول دربیاری فقط کافیه با کانال ورسوس بت همراه شی
📣
🌐
ادرس عضویت کانالشون:e18
👇
🔪
https://t.me/+vEPd1hF2Y38yMWI0
🔪
https://t.me/+vEPd1hF2Y38yMWI0</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/23026" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23025">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61689d1d82.mp4?token=lJ__Ac87F3B9yXCcq5bl_hOm5tlczZA9ab0hex773P4jvYDxtXYNSXDRAYd5XYf22b28UtdbBmoRFY6fqHSV_kbqlUsOwgZFE8PM8qY7J6L4BBLkwzkeeO7417RVyYxHc0KHH-QAMRMI_b3PxCZcWgcjgunmGgoGDcJAuGlSqlZGiqZmqWNZlp-ZVSpiojypwJw4OC5ylaElTCXF0Y3ggK8WZHmHDsdBhDXMvbE3T98NqzFOsmTcW1nTcZhKMcgvcwbQG2sf-n4mX3ylyDqnfU5_j-qEvTy7YCKQo7HCcNNBEBxA4oByqDyeThOQVXOY0cOsqhKGx102hqN3O23-yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61689d1d82.mp4?token=lJ__Ac87F3B9yXCcq5bl_hOm5tlczZA9ab0hex773P4jvYDxtXYNSXDRAYd5XYf22b28UtdbBmoRFY6fqHSV_kbqlUsOwgZFE8PM8qY7J6L4BBLkwzkeeO7417RVyYxHc0KHH-QAMRMI_b3PxCZcWgcjgunmGgoGDcJAuGlSqlZGiqZmqWNZlp-ZVSpiojypwJw4OC5ylaElTCXF0Y3ggK8WZHmHDsdBhDXMvbE3T98NqzFOsmTcW1nTcZhKMcgvcwbQG2sf-n4mX3ylyDqnfU5_j-qEvTy7YCKQo7HCcNNBEBxA4oByqDyeThOQVXOY0cOsqhKGx102hqN3O23-yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
خوزه فلیکس: فلورنتینو پرز در کنار اینکه 150 میلیون یورو برای جذب مایکل اولیسه کنار گداشته؛ 150 میلیون یورو برای جذب یک فوق ستاره دیگهه کنار گذاشته. پرز میخواد این پنجره دو فوق ستاره به‌ارزش 300 میلیون یورو برای مورینیو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/persiana_Soccer/23025" target="_blank">📅 00:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23024">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05fac563f1.mp4?token=Ha-ANJEzsPqUnyH8xRDjXq41zqJxGxt6zQYh8dFLtKmcmJXcxJnEcrXu5JVlVpi6nz2Y_dx5cxNIG4yk2cCrisyWZ4JkhIYfa_duePkp10hI_yN0BT2k8uT49_j0ANtXoT6aJZZLutyvMGe0ehSBSflDa3RFi6_00eFMjMYHcgw6ATf_ugGok3B2vcJuGzZFg1DhIcJKyN8Ut_kHM_y8-B5bMpyL2zHkEOSG7ljfFkyfeM0ocd9jolUs8DmT6WN-gp_1X5NLRa5Ep-HRXdD4k7W8v1RgKSQarGmUyuEG6XNjatNu9B0R5W0dt5qD3mO69F_iqUUShQKSgq-YBE59FlYF4zZdijW-MbAnv_a76BCaOkxixhOPnVxtwVnKHwYLPBPohQjGgcRPyCO1JxTiPNaZCSdxsme9ID3rz8DE0r7bNYuskZshbd7gFmUdasQMhCnCgq4-AnlAbAoJ2EjRo-WYa-Ez3YOVtCEpZvfLbuthvnnXJMEVFXAYyUlBH9d5B36-9J14jN0JpiItbkgGFDGf-YFL6cV4BkfejtdnAAb_cFXicyuVLHNS0jBNaBx3JPEZtfp4yj9bP1d5d_c1rvQvi-cCIRmnMZl2byzPMLH1h38NbT2YbfbMa5RJlJR4Kl9U9nvFNP90tqcVqHEadfwwEwl_B14N-bzmbzR5hA0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05fac563f1.mp4?token=Ha-ANJEzsPqUnyH8xRDjXq41zqJxGxt6zQYh8dFLtKmcmJXcxJnEcrXu5JVlVpi6nz2Y_dx5cxNIG4yk2cCrisyWZ4JkhIYfa_duePkp10hI_yN0BT2k8uT49_j0ANtXoT6aJZZLutyvMGe0ehSBSflDa3RFi6_00eFMjMYHcgw6ATf_ugGok3B2vcJuGzZFg1DhIcJKyN8Ut_kHM_y8-B5bMpyL2zHkEOSG7ljfFkyfeM0ocd9jolUs8DmT6WN-gp_1X5NLRa5Ep-HRXdD4k7W8v1RgKSQarGmUyuEG6XNjatNu9B0R5W0dt5qD3mO69F_iqUUShQKSgq-YBE59FlYF4zZdijW-MbAnv_a76BCaOkxixhOPnVxtwVnKHwYLPBPohQjGgcRPyCO1JxTiPNaZCSdxsme9ID3rz8DE0r7bNYuskZshbd7gFmUdasQMhCnCgq4-AnlAbAoJ2EjRo-WYa-Ez3YOVtCEpZvfLbuthvnnXJMEVFXAYyUlBH9d5B36-9J14jN0JpiItbkgGFDGf-YFL6cV4BkfejtdnAAb_cFXicyuVLHNS0jBNaBx3JPEZtfp4yj9bP1d5d_c1rvQvi-cCIRmnMZl2byzPMLH1h38NbT2YbfbMa5RJlJR4Kl9U9nvFNP90tqcVqHEadfwwEwl_B14N-bzmbzR5hA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیوخفن‌ببینید اززوج‌های‌مخوف‌حاضر در جام جهانی؛ مراحل‌حذفی‌قراره‌بازی‌های‌جذابی رو ببینیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/23024" target="_blank">📅 00:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23023">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7x35l6y5pb0X2_VWxkRrS4PLf1cj3T3NUx-f_DbQdYR_0V_9CTTC5AfFlP7srTCCm66AqK6TMlAHG8xVU6yyWtlPJd6jfFByKCkAIha2rIS4v2Ne2-_KqWtQ7_fJBBZeGeDqWh38SJ6AjbODc0uxvPvHBU8V4VTh2tHZ8CAn-TnLK25hrMiE7mndThessg7MK1Nr5QcVM-oheJMaqAmZ9ZMQ2AnvyQ_ZzljpbM4YZ_s9OGeWKieZea-MU9LpEmFWdBeG34oPQNKuNdFDKBKxHsBvmz1CwdacUE5UQdxlm4QZwq7bMKQ0MZPGqj8hvI9WwYRePoiAjWhkMEZm2uKgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جام‌جهانی‌فوتبال‌قراره از 21 خرداد شروع بشه. لیگ‌ملت‌های‌والیبال هم از 22 خرداد شروع خواهد شد؛ برنامه‌دیدارهای‌هفته‌اول لیگ ملت‌های والیبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/23023" target="_blank">📅 22:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23022">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9su5uUHDZv13ifItH1MDNVxbIL_cyTcbJeIlOkLKhembWD_c0KG3ip0A-EE2Ddp2XUfAPoxj3vPXdU6HleHZXQsqaQEquL-NmYJQj_CYul2R_CCpqZZ9egRjo4jdCbJUVyx0ePYHitVIZtruhz0hvgI1WCKIwNOGGCKQ9rhnkrVENGZRbGoC6qJmwxd334shEssEyPWepPntnbxwEqvh4SPFzDlpZ8lLFt0MfHMode3veECCEmX1mqZcpdp-PdZMIZ6vA4TA6S-VDsupv1Wb3B3O8_PG_3XTn7Wj_PovkjBcul-77EfID_3UxXWAEImEZ7GjkRcBWibHWHmvL9TWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/23022" target="_blank">📅 22:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23021">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eI6dAyJ9M5RdZkvu6C5YI30L1Auv-9-ljqz_BDCa718dqgTxb3bpdfUoOhsAwrEQPDeMAURwnXhh4aRzgdFW-V9dtnM1fEOTsj1XXXbiJ7XFWOhLMJUrfsUKaGvm4BVkVlGuODUH7JYdMiAwBHodTcOtQgHYKZ7Yb-8v-ROJ0q3PvIe916pNUlL9F1vnXrxqEQQt47w1vonc0p1wBpd0ma99q5lRR1yA4koyUFScMpBNhcn9_iC_8ivOGqI9mC2aA7_An4msxJNv6EELI_18RDV8sWEOKhddZKtYo1e0BIbIjgV01nbMaMXA0pGzndJRpD9C6_qogCatjnAaAMw-qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رودریگو لاسمار، پزشک تیم ملی برزیل، نیمار جونیور از مصدومیت درجه۲ساق پا رنج می‌برد و ۲ الی ۳ هفته از میادین دورخواهد بود. به این ترتیب، نیمار دو دیداردوستانه‌مقابل پاناما و مصر و احتمالا اولین دیدار سلسائو بامراکش را ازدست خواهد داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/23021" target="_blank">📅 22:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23020">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f3b11f90.mp4?token=My_O1A98D8LJ0ezyM2yD4fgc9PL4SKLsKbbnkCaw6sfq5wgpBI3jTAjKM_P2qE_jA-Qjcu-GgDpQ7BrCdG9i-t0q6lsLfPYXEbdIKyz83FS0sLZVBol3gFPzr3hQVdmQi-scG0ItdlRue9dbQ0IaRM_E8IVMMzldydNg2vAdeyZzLkvS1iPfntVFJRcJBCsVyUjEtPpziLSHQ0nTnCxC7wgbPl_lMZcvfyeKwQ_i5QJzsZRcQSUiEGuvTKTzgUosR7Sodwff2N3o8ZcWQDHqDAuP9msmFX_iwJptRmOvubZlOl7KzlbaEyWwE66sirV99nMowAUtUAmTZgiQcHaBQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f3b11f90.mp4?token=My_O1A98D8LJ0ezyM2yD4fgc9PL4SKLsKbbnkCaw6sfq5wgpBI3jTAjKM_P2qE_jA-Qjcu-GgDpQ7BrCdG9i-t0q6lsLfPYXEbdIKyz83FS0sLZVBol3gFPzr3hQVdmQi-scG0ItdlRue9dbQ0IaRM_E8IVMMzldydNg2vAdeyZzLkvS1iPfntVFJRcJBCsVyUjEtPpziLSHQ0nTnCxC7wgbPl_lMZcvfyeKwQ_i5QJzsZRcQSUiEGuvTKTzgUosR7Sodwff2N3o8ZcWQDHqDAuP9msmFX_iwJptRmOvubZlOl7KzlbaEyWwE66sirV99nMowAUtUAmTZgiQcHaBQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تایید خبر اختصاصی‌پرشیانا توسط علی تاجرنیا رئیس هیات مدیره استقلال: وکلای ما خبرهای بسیار خوبی درخصوص‌پنجره‌باشگاه به ما دادند و تا هفته آینده پنجره نقل و انتقالاتی باشگاه باز خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/23020" target="_blank">📅 22:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23019">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CoOk__lUQxzF-um1A9asGb1MxMX9ZaLYYwi1BF3LHS8dy9SQFoMZ4xAoISnnAKgUqHFHx2MLDKMmYw6HuwAXprR9p5W3Rl1tvJ-Fv8GTpe55_xlSLW_Kz7B7PwcOHd4DiDLj1tX0dg8Imv-bIT3cWI8L6aJ-x2qeEhn6wRG242j4KTDkXUH62XZsZ1tPUfYWZmvGcWIuc_1yrtvajLeOTQeeFyWC7AvioyP0KXWLmEUcLFFGfUI-ApGNLo7UARu-BG6q4aiy_N9QZxW_siLvTJUAZWlHhPZP2av9_O5PNSbkoDD9QeRePFI0t3SJZOWKavDdGRcOp-B6SfiI8Kzyxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛نشریه‌مارکا: فلورنتینو پرز عزمش رو برای جذب خولیان آلوارز در همین تابستون جزم کرده و میخواد بزودی 150 میلیون یورو به حساب باشگاه‌اتلتیکومادرید پرداخت کنه و این فوق ستاره آرژانتینی رو از چنگ فلیک و آبی اناری‌ها در بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/23019" target="_blank">📅 22:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23018">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdfUg5RoYL6e8f1KTqwO37rEo5oo6OScHpvuIytu7FraghLeCOJq8Pm3lCEGQ1RaBKivPw3Afrm8tLO6OaDqTZNjSCHG8ErETLiRYPFyG__f4tsmKGU1Ta0NtBzQWyRRWq8CzSpWhQQ-4ifP47V9Fy6LSK7ELY6_2X7GAZB7qm5fv5OxdlBM2xKCgSfYNZITTKwyBkAwX4BmTvPV3o_4er8Y57ZZeXyEfib78IEPffpYU9ZCIh7czJHat9UqMdWX_peylJeKJpi-3lzsBAaa_g2DsGdlU7T3_gH14eaP6TuIcw0AspiaXA94wHWkfVs7sjfI2Ci-dL4xxfouHWWP1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی اسطوره‌داوری ایران در اعتراض به کشتار بیش از ۵۰ هزار نفر توسط نیروی سرکوب جمهوری اسلامی در جریان انقلاب ملی ایرانیان، با بازنشر یک‌ویدیونوشت: «برای بقای کثیف خودتون، جون عزیزانمونو بلعیدید. قرار ما با شما؛ نه دادگاه، نه‌بخشش. رقص و پایکوبی روی…</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/23018" target="_blank">📅 21:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23017">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2huXpSMcXWKFDAAzzYxHQ58XrtJRGCTwwPlZnTq4wIlmaN82YeSBUApT0Z8CFqEqQlSSPeoC2TN6neS2Dtoni4Z6Cipjm_HxdnSHGsr0v4qudEwpA35MJ_64KL-jaDyKXzBzL332qGz4EHW-tGVL3EHKPsv4MklDPUos7rT90rwJUbzHHIV1lDBsFvGfGo7NLNf8oEEhNI2reNoYSlQ94BOBNZP2U5XB58c8ZNeAtaSMyqJBzGUUaWXVwF5D7P-1Hz3LUAiRVscO122_FtlfmB5J1ZZ8vwbVd4urKMp2xN0_djcINopcnmUdtVH5RfIAcdqx1JUmClZV9bgUUY2Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇦🇷
جدول رکورداران کسب بیشترین تعداد جام دربین‌بازیکنان؛ لیونل‌مسی بااختلاف درصدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/23017" target="_blank">📅 21:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23016">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Icg5iHs-Bt91nXWzbCzbgfCIIgt6Y0fID3paa5J2UGA9oU7fDio_IPudUSJ1s9aRALB97TE6PYPy2mZzncRbfrZFqfvDE1ndlK0R14H6BsHeIN2xVLPzwJRvoPahr6tjKJC4mT1RcIuGByJrz6xirPxMfn276cRYWhuI1XoXnhfExldTDy2CD6gbZUF7vMdmoSDLpyLdaPb9QxWpfKdoN7bCcWZi-PXL2PNKMkvboUGtQ7O4oPSZC_YeqZn-QPiDv_fcNBMo5n-Q9QfFCQRcXXLbIiIpjEF8OMJr_wf6IHZ_rwALxQ-NIdpmp4kkJe8r8EiEE_0s4Aw2zh3p66q8mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/23016" target="_blank">📅 21:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23015">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPMxCMZA8bUJhYvRkCMEaiIDM5MHMjFtI6pCl7bosHnapSiY5LEwLHcotcb7zF0KYJcOrdgvu3YGuC-7EJKD58uZYcKuizaxKphP7pRqiGrJOgcKfvyxuK0E_7szKhsrXE9BpcdIq1ZgZnBMIgQYHg7cWxong26seg_UyLkFzmkQ14gXmaASbczvDW0PhyRlBPwn3J2r8ry_5YHt-FPwAAZD84ldZ1rL6sijXD0r-nlLKeyPnQLwZTTg1NcOQW9oT8ta0_4F1QQpZPBMdzVe3Z6HxNYiEYb0FZIY3kAJr9bYfys_0jjc3R9a2XblJbbSSzaKWDBfZiYXIGw6Ysik-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اینکه خبرمیزنن پنجره نقل و انتقالاتی باشگاه استقلال بازشد زمانی صحت داره که درسایت استعلام فیفازمانیکه‌نام باشگاه استقلال رو سرچ کنی بالا نیاره. شماهمین‌الان هم نام باشگاه استقلال دو در سایت استعلام پنجره فیفا سرچ کنید بالا میاره چون هنوز بسته است…</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/23015" target="_blank">📅 20:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23014">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60571c2f92.mp4?token=AldWCLXBTHyyKXqkCEfPfEooKom_XKnPrC8LhQB5OZc52xSQqVTm9BqAHibDTngIUVGiHxaWDiEhu2Cc4-fRbBol36qE5TMlOFwhGW4pxcl03CLDNXdaBKByp-8j0-ttJTymZqTiTNmXNAMFfzHSpeb0xbFCs1yyoXNidcljXyyunRU0gOgfHPIJ2HpE8SgnxAZ_T5q-qQ4hYxADS5x9OYX5PQ5MC3gTBk10htvSxIq6b-fFzlQOQMD4QoeYmBDtaniMjp8eODTj_u-IdAIOT4wWKPy59Y1BnZJlGsDDnybSObR_z1YtXuipGp8X1mdb9yIDa91TEBlqw5I4hP-LbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60571c2f92.mp4?token=AldWCLXBTHyyKXqkCEfPfEooKom_XKnPrC8LhQB5OZc52xSQqVTm9BqAHibDTngIUVGiHxaWDiEhu2Cc4-fRbBol36qE5TMlOFwhGW4pxcl03CLDNXdaBKByp-8j0-ttJTymZqTiTNmXNAMFfzHSpeb0xbFCs1yyoXNidcljXyyunRU0gOgfHPIJ2HpE8SgnxAZ_T5q-qQ4hYxADS5x9OYX5PQ5MC3gTBk10htvSxIq6b-fFzlQOQMD4QoeYmBDtaniMjp8eODTj_u-IdAIOT4wWKPy59Y1BnZJlGsDDnybSObR_z1YtXuipGp8X1mdb9yIDa91TEBlqw5I4hP-LbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ما
مردمی بودیم
عاشق فوتبال، تو فوتبال هیچ دستاوردی نداشتیم ولی باز هم عاشقانه دنبال کننده بودیم و دل‌کنده‌نمیشدیم‌حتی وقتی هربار بعد از یک شکست‌جمله‌کلیشه‌ای "این باخت چیزی از ارزش‌های تیم ما کم نکرد" میشینیدیم. بامردم ایران که در جام‌ جهانی 2018 روسیه بابت خراب کردن اون موقع طلایی مقابل پرتغال اشک ریختن چیکار کردین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/23014" target="_blank">📅 20:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23013">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GI2jzO_6c5VZgFdSNKiw0SN-ZKtpKSZwApDsv3F4vzLWxwc1HzG3ewPtQ474rJyzgn_okS12CNw5OlFDjkNuL9qF1ByncVOqKMxPDCV0wuXQXPmvoWPYoGyKFaMbk46T03dL1qqPMqIRVxZT0ulWANb4zgXEuXBDveh0uwYZF1_jv11dtvkTya6TUL27a5SwyOvbIx5Z49pS7pbVDtFMzNwyKDa0BSehhJaRR--WWkt8-QUMSB8FZ2AqCEP0QOZtNkljws1In3fFUb-Ig-IVC8Ydv01RkB4VVtw8_b7NzhkXqPGU8Foc6lcQR10FRzJd93q2fvicN4SwTLYWTDMuYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/23013" target="_blank">📅 20:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23012">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbAp2fx5XydXLenPLnJGUwURU4GAFzyVfJiJ4Qw6qhvw4S6WGlxJinZCOj3AlwD9CbRFWGFwK4z9449QmAxwJ5rGmu7qIsV7FDKFMSF8_jhxRZlSYiWmWhJLCXmpzlShvMXF0gWXwPo0aGkrUG9cg1aiNQHnhjoJPN1Dy64c8ZVEe4GQ55sJq0kCYsQaQK_iZIxl1KNqSe8kGt52hNcuyMdJpcoebXYykCJ3oaujk-KCQMVBNQqF7p20rG0m6mc0fD8gmNkCxRy57W-F9aHJCgR6KZbp7PfIimn26D55Q89oIrOljVB-CtHv6d6mqwskKulQppmOcDIAuAqqbaWfRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/23012" target="_blank">📅 20:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23011">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29259cd165.mp4?token=vRzkHXmncDEQEevXAPfUi7aVElcB9uvTGTuYmycaCe9lrMsibgGSpH47C5lsyRfqMNTtnCh8i-522I4h02FS4U1jLFO-gF_vtx4pYrh8SlDdfzjIAjlxc3qjrHMRSc3wvDGvL_dczfa1ammsS1K84q_gVL1NkLeIQzEq1LKVIYach2R9dDD7HtdSywT6vBBNHWMFd3BtqX6039g6GM0BwAANwO85bhenuAcLcZZRApWWzImn2lRyz1NeBvd9bYbzOIwX4kX6tMElak0_N9-TwrLMKTt1lRyjzlC4wnfLcTBKo-2nZfRhc4Kj4xtj4bc2ax9gC-Eb8PO0tSa9D2sGjlbPoR5U1PBEx47BLTzkNbk4Np983sKkRENjGpoGLD0mGDBvrWndQ3KoPr9-5EdCiUIZFPklka6NJgIyCG2iOREaXfYQKaF9cF-aJd4VSnUemOBdqKb29R8xDrYkUj_HOTA1xTj39zOlZFrRAozk6gLdtu11MQxRASE_KHWloIMAGm1XyhMvvt-7mP-9s9wmbcVCDgd9oMviR21cSpX766S61Q24EplLkNYgn03AUqRZ6KIbG_ITR6rKqQYmsU3Gsn1slaZGLHCS5lJRvwHGgZ2mLHn0V9tlsIJHVrMdwVMfxSeeewoD7OSFlhLwrwAlb9xbcqhk-85Vdq3wd8LVHc8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29259cd165.mp4?token=vRzkHXmncDEQEevXAPfUi7aVElcB9uvTGTuYmycaCe9lrMsibgGSpH47C5lsyRfqMNTtnCh8i-522I4h02FS4U1jLFO-gF_vtx4pYrh8SlDdfzjIAjlxc3qjrHMRSc3wvDGvL_dczfa1ammsS1K84q_gVL1NkLeIQzEq1LKVIYach2R9dDD7HtdSywT6vBBNHWMFd3BtqX6039g6GM0BwAANwO85bhenuAcLcZZRApWWzImn2lRyz1NeBvd9bYbzOIwX4kX6tMElak0_N9-TwrLMKTt1lRyjzlC4wnfLcTBKo-2nZfRhc4Kj4xtj4bc2ax9gC-Eb8PO0tSa9D2sGjlbPoR5U1PBEx47BLTzkNbk4Np983sKkRENjGpoGLD0mGDBvrWndQ3KoPr9-5EdCiUIZFPklka6NJgIyCG2iOREaXfYQKaF9cF-aJd4VSnUemOBdqKb29R8xDrYkUj_HOTA1xTj39zOlZFrRAozk6gLdtu11MQxRASE_KHWloIMAGm1XyhMvvt-7mP-9s9wmbcVCDgd9oMviR21cSpX766S61Q24EplLkNYgn03AUqRZ6KIbG_ITR6rKqQYmsU3Gsn1slaZGLHCS5lJRvwHGgZ2mLHn0V9tlsIJHVrMdwVMfxSeeewoD7OSFlhLwrwAlb9xbcqhk-85Vdq3wd8LVHc8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
یادی ‌کنیم از مصاحبه تاریخی مورینیو بمناسبت بازگشت دوباره به‌یکی‌از داغ‌ترین نیمکت های جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/23011" target="_blank">📅 20:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23010">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYuy5VYV3-BebA4gB8_S4riHk1yL0RIdMUjld6v9AmYvRm39bcC6rPNyIn5nglZBz_3EekZQHQmNihww_bwI_Hi7xIE_oqW3KYF0ZIE7MtBZYeTesgzjFwXzya3Vw1TYDro3I66jWIUzXE14MSyFiPich3M0vmFGNGmocxTu6MrZlDB3WS2G37qJvpYHL-WCoPKUMqJHJ2xjlDDl_JFsCxE7-49OeYt_RCv1i4nLU3Yn104skW0saC91uw0ISBKr6QuzdkTkadTv0gPFNrWJmz6LDTQJ66vStg1UICj_GSy_nDeDzO07WqBLhlAY0AhqggcoXn_LjctkF_MT7EiXVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ ایجنت محمد جواد حسین نژاد به باشگاه‌استقلال اعلام‌کرده‌مبلغ 1.5 الی 2 میلیون دلار برای رضایت‌نامه حسین‌نژاد کنار بگذارند. خودِ حسین نژاد موافقت خود را با عقد قرار داد سه ساله با آبی پوشان پایتخت در این تابستان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/23010" target="_blank">📅 20:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23009">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j92rMftzWhqto5RtBsyTKgz74zgizpLk37Oij546OmIFGfIjbLBBg6P_DXosVfLirQcI8MaFJvCXi0JNJnaw3xkVq83TZ_kmIPSNYjsA_TvRvZRv2gRWnvXlIF93scfW_MDJBZSsTwVtAq9Y3-aGSmyJMiLdnecNc5gDo2jRhu_W982N755GIbXHXfWH87f18_r-S5YxlqKKOIPS-NkKbd75VQmHAo4zReldfeqx2OVOgqORy-Z-laABJK3ianeEjh0HeYrsala8_4GYZivMXiRRUF0fXFtpsXBAiu-hlnOWP3ueeSWRqXiwDP1Yiq_FWTHDEQaY1RjSzGg6i6iT5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
لیست ورودی و خروجی مدنظر اوسمار ویرا برای فصل اینده رقابت‌ها به دستمون رسیده و بزودی کامل پوشش‌خواهیم‌داد. علت اینکه یه چند روز صبر کردیم این بود که همه دوستان عزیز کانال به اینترنت دسترسی پیداکنند. ویو کانال قبل‌جنگ 65 70 کا بود الان با وجود اینکه نت وصله…</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/23009" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23008">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc2809ee8.mp4?token=slROzlJYtpUqsKLSw5S7llqc9ebP8-YPX9UbNBrD26krcTg8lm9umE2q0R6QbsoVS8Ua8Fh5UQFMur8u8Hjf3h8wM9Nek2D_pTbdSYvSBdTLwFPfUOfGHw8W5bqwgyvrUFH7Jrq558QeXX3C1_ggllO16Kr-0xnkpwieeXL6TY-Uq2ea766zSZnpIxS3ys34ZbALZqcosXDy-vcr-okytqZE0UeFNYHWohEUJWwu2z6tagek1BECJlFOG8Q5_23AaRtb9O5I22OhxzfJr7L2QvX1Y45v_my8Jmk9EECShTpR0bb-GuFAXBePC9MP8E41C8Jd6fbHvR6sb3Df3rvhcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc2809ee8.mp4?token=slROzlJYtpUqsKLSw5S7llqc9ebP8-YPX9UbNBrD26krcTg8lm9umE2q0R6QbsoVS8Ua8Fh5UQFMur8u8Hjf3h8wM9Nek2D_pTbdSYvSBdTLwFPfUOfGHw8W5bqwgyvrUFH7Jrq558QeXX3C1_ggllO16Kr-0xnkpwieeXL6TY-Uq2ea766zSZnpIxS3ys34ZbALZqcosXDy-vcr-okytqZE0UeFNYHWohEUJWwu2z6tagek1BECJlFOG8Q5_23AaRtb9O5I22OhxzfJr7L2QvX1Y45v_my8Jmk9EECShTpR0bb-GuFAXBePC9MP8E41C8Jd6fbHvR6sb3Df3rvhcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از کواراتسخلیا و کول پالمر تا میتوما و فرمین لوپز؛ 30 غایب بزرگ جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/23008" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23007">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZiJ5b2qhaY4CB_dBCNXXN_uxIZtwLpiTvXxj2ir-JyJM-_ctkUIaDhNCS_pDG4P1R1qUklGVqs8dC_CPL8J9r3pyxQSAnjXS7DZsanswuF5lT1D-roZif7ixcryHK7vnyAIVrNaFEQBXXOVcGq26oJTlNkinsOu6gIAaxeHMYrKNhhpqFF1T0uCFxlFAJV6fDi0ribpAEfeW73HZBaA7SW-8wjt00CJr31Dtkt57ZRtSX4qbe1SHNsFaLul-i7g0ksDZpQoMvIcicJUogW_CgfeAHtSAgtXmzCbEaNiaJN4Z3gdI-Yh6IfqVdKVEcjCUVXx4qhYersMRiuWR6_99Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
باارزدیجیتال‌حسابتو شارژ کن
🅰️
🅰️
🅰️
شارژ اضافی بگیر
✅
🎁
20% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
همراه با درگاه‌
#ریالی
#RomaBet
📣
‌
#بدون_احراز_هویت
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
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
18
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/23007" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23006">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZG6WUdoVbDz4X4WdpPlK3BmEQXjglsrAXaFamEtXI658NYGgjH4VaLAXfctY3IZrgIA0NrwGs045ACPDqUA0fNd6IC-CyGJODUiZMftXwKoKXXkHFHQSwqxAyJCLxiWdTe2QnUVnr3ofmPzi87Xf6ElC8NaX8fmuBfGRh2HJJsgtgfManGm3K-1VsfpS4ms_7sdUuINEVImkbJeRwWIlRcKsd6xqbIHqg29b5148Xps8YEPPOxfELLpn0uwOEhcM1o__9_QkZcdiFZNNZ9R2qklJf_gNzKW4Q1iYPXCWbEQFNg94nmZoWfolMzFFOPFyXPhpZz7im3fjzmdPrJvsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
دبل اولیویه ژیرو ستاره39ساله لیل در بازی شب گذشته این‌تیم‌درلوشامپیونه؛ ژیرو در این دیدار نمره 9.0 دریافت کرد و بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/23006" target="_blank">📅 18:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23005">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiEFI69UkyialnEvwgqA7HUeyldxMovLhzZQ2MYPEV3parpgrhf88mb6HT6_dF0bLUgWR3U8sKDOHsqnCVqbmP2UBwP3wO-Wu0gSGiILdS_fvn33zLXuK6RBDllQxczfM-B5UAd3gCTmTw6wvV29WGBGfix-upVmaIHNALWJvqn7woffoMN3A1i4-ZAC2iqa-3byGRJ0zT_BkAuqNTJNgQosDtSeAtlmo2vOmZAUZh-lWTEEBLzv-v-kCG6YQxV9NSMVn66TlsPS5CwP3nv1T_865lg98BVM49KCBQeCgTcrnMADLKkgPw7yDt__NpPn392MYeaVeDU_hjyyKMBm-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه رسمی فیفا: دیدار دو تیم ایران
🆚
مصر قطعا دیدارافتخارهمجنسگرایان‌خواهدبود و به هیچ عنوان این رویدادلغونخواهدشد.  دراین دیدار ارزش های همجنسگرایی را به جهان نشان خواهیم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23005" target="_blank">📅 18:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23004">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11a90d5e78.mp4?token=FTMzygIlojK3Tw0dPd80DYxQSjmzIWGe94WhX4br-2DspiyaZ0MdDziklZqazGZHegbJg4ZW44nRNZSV3rQcwdjX9qiB7QSmOasmqqt93wqscCMVjv-XpINfp36G_OQDgzPD7JlCiyEu_doe6O3fp5ZYZmwuDtpmdP1_IuQO0_4YpPh8XoBXSVWrBwCQ8WJPFe1w5dyV_-p-X0L-_R2vJwNKltrR-df2vpylzZwsImp5EZGK-lBOUUJyx-3v7tafJyVRbyImOj58TvpjHEBnLgLWwaILGZPeA3VKOzv5tO1-vFWHDm9OFsRB0BJ1dIdVxWPEoCF7cXFlmvPsu4EUkrN5or-ZSNyIUFeFKqktZgsQhxOFkNe64mqrLykoJWxTkEZDfyLNNRZEQoZ04eTtqcrinYnaXktNAZGC4esB5HrTEvHFtwN8b0uoyKc7isdBGBaOF49U6r3ODXzlQJytwPf--Hnfk6EeRvRiFQiqd36vuKDuRNufy___pT8eYrwyNoxQR5RIHiMbs0wHsUu88vhsmygLh5bTTTnKbfkjviV1i2zUOom2Ww73OmG5DoUc-gk5tLUTYa8asihUf27NUBRv5_qdke-cQUjPhEB36hhnDAHFFLerfHW8HBZQlxEQcHOtmTiAL9nIb1XMdu7vzniQDZ9eEWWTBxycwig2QKU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11a90d5e78.mp4?token=FTMzygIlojK3Tw0dPd80DYxQSjmzIWGe94WhX4br-2DspiyaZ0MdDziklZqazGZHegbJg4ZW44nRNZSV3rQcwdjX9qiB7QSmOasmqqt93wqscCMVjv-XpINfp36G_OQDgzPD7JlCiyEu_doe6O3fp5ZYZmwuDtpmdP1_IuQO0_4YpPh8XoBXSVWrBwCQ8WJPFe1w5dyV_-p-X0L-_R2vJwNKltrR-df2vpylzZwsImp5EZGK-lBOUUJyx-3v7tafJyVRbyImOj58TvpjHEBnLgLWwaILGZPeA3VKOzv5tO1-vFWHDm9OFsRB0BJ1dIdVxWPEoCF7cXFlmvPsu4EUkrN5or-ZSNyIUFeFKqktZgsQhxOFkNe64mqrLykoJWxTkEZDfyLNNRZEQoZ04eTtqcrinYnaXktNAZGC4esB5HrTEvHFtwN8b0uoyKc7isdBGBaOF49U6r3ODXzlQJytwPf--Hnfk6EeRvRiFQiqd36vuKDuRNufy___pT8eYrwyNoxQR5RIHiMbs0wHsUu88vhsmygLh5bTTTnKbfkjviV1i2zUOom2Ww73OmG5DoUc-gk5tLUTYa8asihUf27NUBRv5_qdke-cQUjPhEB36hhnDAHFFLerfHW8HBZQlxEQcHOtmTiAL9nIb1XMdu7vzniQDZ9eEWWTBxycwig2QKU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیووک اوریگی مهاجم31ساله سابق لیورپول ساعتی‌قبل‌خیلی‌زود از دنیای‌فوتبال خداحافظی کرد. اوریگی با اون گل تاریخی‌اش به بارسا راه قهرمانی لیورپولِ مدل یورگن کلوپ در UCL رو هموار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23004" target="_blank">📅 18:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23003">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1416a6883e.mp4?token=IzwDTawScy-UXyerjY3lyB7e_BOwpoVJW1rxyUU3BS1ssapq0eIU_zBN80V2681lbpNdC44S5b2iYjqkOn2WNkjspeDTsHmR2tJ59bc-55JCbYU4OkNlB6FzMSTqWieSbAsbLUgs2g5mdHdNTRW2LfLaJ9MBPqEq6O374AMbrhOBBF1CvtymI8qwprOXF47CcpWNKQEt4k3Lq_cUB801OZx_6ucdxG2SpAiGrEHlZNgTK3wqOtHvsLyAdMX22mbZ1aEb0BVuN7U8wdMizZrUNxvNCJYy_lTmyTEqNfGIuSFHtI4khz-KxnXcykZoe8R21OWjDU9ho88zvUYSxSwbdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1416a6883e.mp4?token=IzwDTawScy-UXyerjY3lyB7e_BOwpoVJW1rxyUU3BS1ssapq0eIU_zBN80V2681lbpNdC44S5b2iYjqkOn2WNkjspeDTsHmR2tJ59bc-55JCbYU4OkNlB6FzMSTqWieSbAsbLUgs2g5mdHdNTRW2LfLaJ9MBPqEq6O374AMbrhOBBF1CvtymI8qwprOXF47CcpWNKQEt4k3Lq_cUB801OZx_6ucdxG2SpAiGrEHlZNgTK3wqOtHvsLyAdMX22mbZ1aEb0BVuN7U8wdMizZrUNxvNCJYy_lTmyTEqNfGIuSFHtI4khz-KxnXcykZoe8R21OWjDU9ho88zvUYSxSwbdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
رحمان عموزاد شب گذشته در حالی که مسابقه اش‌رو 8 بر 0 از حریف‌بلعارستانی‌خود عقب بود در نهایت با یک کامبک تاریخی 17 بر 10 پیروز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23003" target="_blank">📅 17:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23002">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C78TFYd9rWRqQpFCr69_irg2Qds5CNDPufoEEAa3yBqY25PJQsNE9NQeQ6w-wHVWQsm-UAE157a3-2KCOBI69K9djyhoItu9VJys51tt9UhI55ght7DL7bTMLMB2sW-A9g40UCIHUjDXbzUMKTQ5_eElKo2IcE1q-wEeMifvGlBsgw-5-UJ1wBpFi7pGWGd2mkwRPTeoivOlfladsejjf9ytQqmO_3yt8XZGjCQptM3EvyneWtAF1lwYj386TKStaRuKACfwkJYIxdiCkng2oKVFYTHXjJVKqyme6iSU4czhNEiiqLxpSlHnZPZjPu-mXMeaoY6yOsU-u-FkrZj79w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
پُردرامدترین بازیکنان حاضر در جام جهانی 2026؛
کریس رونالدو با اختلاف در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23002" target="_blank">📅 17:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23001">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUS5oQvLBGceHA7-JkT_PpMcZv5HTPD-aVRYQiExPia6TKm1_y5Fo9_yJgmygzeDqF1K0udac9Vor1hiYk8GC1pIX1jIjo41MxqD1FoMQxdimIzYiOHEnCOsq-EyeW4w-xxP77giE3HMc88oREtkHtNGF2LgBZ3-J2XCDwNzQgQ3mpHX7tJDWdPsdHKYpnGHpqZZ2h2iNKbo_usSbo6EHIO4lcCprOl05wlSszh7c4Kw6X2NnPldzn7eeLcdvOn8Jqtl_loH0e0yBI3Y3Kfavb5yY2OtFFTyeIxgsPnu2Z88qpbmBov0zmXkiLMSAdByswlPD9aIPT6AFr0IeGkj0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌پرسپولیس‌بزودی‌باانتشار بیانیه‌ای جدایی مجتبی فخریان و یاسین سلمانی رو اعلام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23001" target="_blank">📅 17:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23000">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S41UrDQ07KVKIe1R_PNXGjy3e6Mw11N1SquGuNSRNcmuUwgeRxi07rTS4JCvXJHbMqopLIvM3oZ9o3rFtPjSpAj7iyw1fOUJ1zHx4jRTbfbsIBiIohM4bZdogfAV1vzUjjwkacEdUuPqSiQAKV-M4k71izTH2nuE8UXQbqBspiKmlCQuzKfIkFLT5qZtY9aDNG-4GJ82L4ZpLm8ziZheal4143-J0TT2uL8WI3d2miHbusar2uxWw_Stq311sat8eL430WbQgJ9DUyWBsGI6GoCBEjgehltF1CbxCTKz_O9iz0edacyXBZuxNX0a70IBozgy40bNMxEEKjYV3BMYUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در این تیم، همیشه جایی برای پیرمردها هست؛
ایران و پاناما پیرترین تیم‌های جام جهانی ۲۰۲۶
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23000" target="_blank">📅 16:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22999">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvhFn_ILQc21JtcMMfQVw99qCmzukuy2V9Xxi7UmTeQ6vKlSorAhVQwUFIg5nWQH60j3Y6JPtkpfShbbJpQPjGY_pjM8Dh11oy3Cdo-0f6WlOrzRKu-HQxDsFCGrES0oXYTwR9FsnJ-HW255dEN-EjeKQ1J5Szh14CpKpxnBirw8l_lW3cYwpC2motMLMJvDdyR6yqQCxF9BGr048UDB2Ik9ArqMbziNQOUrxD7CtIUxmkSKNGdIuNMmUZgFhZjha1u9rf6iPwwgAkpUnytu19nbwygHiHxqkbKrPQjNeb-METxr_YC4kuVQlAmArU5GUHQms4LjR5AzfDW_pjBvMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛برخی‌دیگه‌ازشبکه‌‌های‌ماهواره‌‌ای‌که‌بازی های جام جهانی رو به بهترین شکل پوشش میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22999" target="_blank">📅 15:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22998">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbXD-9APXbkff5q35CVGalgeaEGaNhOIRWKck1tQv4wZ9QLz_wPDK3sPS5aFh6dlYicGd9Vd7wASSIyOeTejZJQ0_aMz2sDVaegM2DsRbi7Ux7TZ9gVFs9Hb4Fks1kbpOlacMZeUldHwDBZu6tXH2mw9qZ_i2hZ-jFUuf-_nlQ9ZNi48YgWO2yuo6My6QhC66pRr2J5ycSWN3E7tC4ptVJ_XYELjXxkQq57dZzsmS6hvZZTSg28fKGLk9F2orEsoNEaQZNOOkT3YZA8c3mztfkqhCNAQJChr95QGC0-v69-DJwSlVmulzzL7deeAhKZBEpG961PvBzYzHk_UBnEvsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22998" target="_blank">📅 15:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22997">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bklOUlYy-s8v9tOcURqqQqcxsxyMgzjtEsS5rTrjDdVQ5RylDCVTKNhi7K5iMTkSGMtODULbKxYrJtMQUtdFwH485dakIpvBKFwPX66ZOZ0SlLEJnKoRjxvX9IAbytvlZteKMHahgXzm16oFF5TYig1wRuoPpplTUylKLxXf9-frzoEh0zNxl-1WPq3CR5YcwGdRr1mNC8TrFfRP9D7af8tMg5SUQGZ6c_GswRFacsEcgJxXGmBErxKrrU1jYKpGtlxlTqoqJwjYSTfoDYmYG5jlScZZtmxNobr6wJ2vGlwTkd1bD_sy7rjLif_c2TZHCCLqOY97hJhjIXA9Q_Az9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
#تکمیلی؛ رئیس‌اتلتیکومادرید: هر باشگاهی خولیان آلوارز رو میخواهد باید 150 میلیون یورو به حساب باشگاه ما واریز کند. نماینده آلوارز به ما گفته که اولویت او پیوستن به باشگاه بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22997" target="_blank">📅 15:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22996">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d3e29ee7.mp4?token=oxJvlBSHllabLS9qVKnyHRov36pGXaRpdRIEa0_oaPZKpm8EHgeG-8duJ7r-MtcFhfm8WjI81eDwmOtsfledhhm4MCefMdsgoSJ4VzE9tRedPG7RymwkFaA5uGiFCx8nLR3hqkeragSyq0g7JHP4y2VNsHzZ_jUWjGhA-7DSc1Gxj_ykEabp6nbqS0v3tXMVwVFQosksZqDF9XxJ3kh2Q1_omPqBRcdWkqIuohu28oAs2-NENN9C2Nrj67LNxnxaQcVv_wIB3inAB77iUgptpfob-gUIzVfaxJjWzBqiSV_F-wgIR6i4rwcVYP7xAYjH6MGSCEk83rroWOUMKFwvLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d3e29ee7.mp4?token=oxJvlBSHllabLS9qVKnyHRov36pGXaRpdRIEa0_oaPZKpm8EHgeG-8duJ7r-MtcFhfm8WjI81eDwmOtsfledhhm4MCefMdsgoSJ4VzE9tRedPG7RymwkFaA5uGiFCx8nLR3hqkeragSyq0g7JHP4y2VNsHzZ_jUWjGhA-7DSc1Gxj_ykEabp6nbqS0v3tXMVwVFQosksZqDF9XxJ3kh2Q1_omPqBRcdWkqIuohu28oAs2-NENN9C2Nrj67LNxnxaQcVv_wIB3inAB77iUgptpfob-gUIzVfaxJjWzBqiSV_F-wgIR6i4rwcVYP7xAYjH6MGSCEk83rroWOUMKFwvLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین‌یامال ستاره تیم‌ملی اسپانیا و بارسلونا درباره دلیل بستن باند روی دستش در حین بازی‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22996" target="_blank">📅 15:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22995">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jr3wMHcUV3Cu27VEi4W5LbyjfxORGvWADtBFpmwe5GS7mrL_l0xDK6MblU6DDoPgPXENPyA2DRkw7v4aezKR-jT5r6-yftFP9Z8B7SsZl58r9GwYm9Gx2zLXIoIZPZQgmOPARV8g9-7B1MNq2KqcnEbATyBkCBZu8Ndu-FTs74d0e2LnrYPruqw_socWORQY2cz8sgwvYHWvqgDUpRetuO3I3WS_lXRNRAE1wPsa0fAtRrZDLfbuxiP_qjxI5xr8hcRQEYoR1lM9c8VmlP951rOCK-vVbzZgvoixs-LyszHzyUT8wO7QlwGkAqtbNvSz98fDDPwo_tfBoftXakqjKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نقل و انتقالات تابستانی امسال برخلاف تصورات بخاطر بحران‌ مالی‌ باشگاه‌ها؛ بمب های بسیاری زیادی ترکونده خواهدشد. هم پرسپولیس هم استقلال و هم تراکتور و سپاهان خرید های خفنی خواهند داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/22995" target="_blank">📅 14:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22994">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b9e0c4e99.mp4?token=RzlaFDZQs1DNbcnNJ3wGuhNVmsORbAzfRZKS4RljY1T-PQjnRjA6PDRvy6eSy9gHqoKPHLmIax4zdK-89KqHaojmdDpeKBFy0T80XRRJ-ItbYle5JrdYe0NE3vwJucZnTvh9bDJ1gteF-edRBELBf4oBxVp5v1hyQqEuwSZE6Tekn1HdE5_ZIau0LGhAs_ejy_6ccIJn4Oh5A-0GIapn4sAhF4j4sxeTOVjZZR-r7Ua6p_KpjIAuveGQEWnIzAjTWo7m2RxOoTjW8s628bfa3nlt546M34H_zlTIxSuP2rQH3SVa5eFox3HWaW1zudzyNjpDuXGflYjCJJoDWcqL3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b9e0c4e99.mp4?token=RzlaFDZQs1DNbcnNJ3wGuhNVmsORbAzfRZKS4RljY1T-PQjnRjA6PDRvy6eSy9gHqoKPHLmIax4zdK-89KqHaojmdDpeKBFy0T80XRRJ-ItbYle5JrdYe0NE3vwJucZnTvh9bDJ1gteF-edRBELBf4oBxVp5v1hyQqEuwSZE6Tekn1HdE5_ZIau0LGhAs_ejy_6ccIJn4Oh5A-0GIapn4sAhF4j4sxeTOVjZZR-r7Ua6p_KpjIAuveGQEWnIzAjTWo7m2RxOoTjW8s628bfa3nlt546M34H_zlTIxSuP2rQH3SVa5eFox3HWaW1zudzyNjpDuXGflYjCJJoDWcqL3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بازیکنای تیم ملی فرانسه بعد دیدن اون عکس و ژست سمی رایان چرکی اداشو درمیارن
😂
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/22994" target="_blank">📅 13:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22993">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TD3zhFJaY11pGuR26nPG4rYIMS6mcTka2a37c3qhLOWYQ_GfxWIfHIzaz64QCghFwJ64Rb6XGeVOSV6C75EY7JDxjj-rFpeq_S49W2NpjnHeHKRVLqxCKuDPnJQ4MOxURzYS1pI0e3r_tHsfzgx_7MAL3-ojDUPvJkpxiGx6MpQaXHzI40NQeFf4MmrNM-uBN1X4bsXaYHVNm4zze6qagatKkB9_KSqGzi0m6BVWJKRe8yKk_vqYZd6ibOtkK2jC6zp-sQML5RNrsAgqb6Ox2N-qG8plZz4NeJbe2rzEGu92zY08XHRQ7oBBbjHYvoIrl-ZzY8NeB9J4dLMkwAPqwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/22993" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22992">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3daebznO1DsruZYjrS8MBgR97IbbqNJcWTU7JGPTfngNhHH4lAFpJpfCmBS8o2aASMgZudlNvG8Gb5kRdERszltzHEka0EZ5fUuTcxOVATxxKWoTREogfxRhxHM58l0BRgoRZApouy1F_L_pVTQt0JHRWd4rZDUq7zAwNivwS1p1z1vENdnp4CcCNCXL1C-ZC6wrAXDAhXJI-C6pUxcvEyoS1dEjTXwnXWh81vbY_Aj_p_wvPcUUfFaD-Vlpt6TVPk8lzyeDcmcNCNJpMoUkxwnWjgoIJQmNAZ1iowuLbg5jnwSsMrnRwQQKUJUPlkSn45F8KUVvdgaior7IN5heQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/22992" target="_blank">📅 13:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22991">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2579758a5.mp4?token=SQnm-ek13C_4o-UmtyCATneEH8yGNW6cBrYP2XMaMZ2IfZqqym3rd5kLZwlyomnJyibqsfPKaZx6mFamQ-DjjtPbnu9c-fnOisQbTp7npZ5XSWmwlJGBQ9f7kWQUIlHKvpACzdSX7NjobSRa6YIOfJsVDIHR4gsz_lX_BTK6TAzGVBYBtEZlS5ObHfs6b5DdwLwrHu9WTTAZncgTCCMmu2AOYbpTeyHX9wK6EGXvSBUssZrtQ32sQK1l_IluNh1AX81yPQdQcBBV7c1Pn7iNXGK4TlOl51kFv-WvCL_s5Oryn9YNPGhiOD--9sQPoKY5blqUT5sLBiA7yziSe-oFYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2579758a5.mp4?token=SQnm-ek13C_4o-UmtyCATneEH8yGNW6cBrYP2XMaMZ2IfZqqym3rd5kLZwlyomnJyibqsfPKaZx6mFamQ-DjjtPbnu9c-fnOisQbTp7npZ5XSWmwlJGBQ9f7kWQUIlHKvpACzdSX7NjobSRa6YIOfJsVDIHR4gsz_lX_BTK6TAzGVBYBtEZlS5ObHfs6b5DdwLwrHu9WTTAZncgTCCMmu2AOYbpTeyHX9wK6EGXvSBUssZrtQ32sQK1l_IluNh1AX81yPQdQcBBV7c1Pn7iNXGK4TlOl51kFv-WvCL_s5Oryn9YNPGhiOD--9sQPoKY5blqUT5sLBiA7yziSe-oFYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرد البرز که بهترین خط دفاعی لیگ یک را دارد و هیچوقت دریک دیدار ۲ گل دریافت نکرده بود. اما فرزاد حسین خانی با چای نبات و شاگردانش در مس کرمان موفق شد در ورزشگاه خانگی فرد البرز به این تیم ۲ گل بزند و ۳ یا ۴ گل هم ۱۰۰ درصدی هم نزدند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/22991" target="_blank">📅 12:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22989">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpicdXgpGshiyEh0FBIVED321cxdiVzqfYC4WowsfIzxmyIRplQsJxGPkutBEpv6VJM7RHkpd4Pn40abvOlTAr-PZ9M_RVDPTEVNQ59r4KYMLRseUkFQXgyacQSFRShMOkAfMIY6vCxfjFbZjP0GeSVCzKO6BEPd0D3Qi_ZcgN1vC5cwR6NQSUfXQ4vf48CbX5Hbq_fPT4v0ye_u9Nm0yAciAJcL20jmZuMNGD3Qv4de6bkegNdSD4Xx1DZElA1cqYb2hsdpA00sWY4KomxbXcI5U-nXcqSY6mD-vpikXWrBgwecPv-qIjbcr6SjFMQ93k-02nA46xM0JHMLNs36lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اگه‌اتفاق‌خاصی‌رخ‌ندهد؛ اوسمار ویرا برزیلی چهارشنبه یااواخر همین‌هفته‌وارد تهران خواهد شد تا برنامه‌های‌آماده‌سازی‌پرسپولیس‌را از نزدیک دنبال‌کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/22989" target="_blank">📅 11:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22988">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sm9AO2RFlxjmFEZoYn6_dFWVAqSFEzoEVyr4VnpK-itatjNQj2dUcHVohj3xCwWw3HdCd6zM3JO1QF9zvMv7IMgo6BBKGlPPax90jTbjjUasVpVPF9OSyhkHXMkprRF20ZSKF-76-1QD2VPe1ltsTQqlYLTF6U3Ey6uSd-biU9_gYwe6W558-Swn9EUkJHL80Il7NC2pSDgN5UpumWcCmJ6Q_mBMC9J1oQvHqMVsB92lqDJGkXei3OsgYUE9BOCgJl_EOo79UTDsnnjaAcWJJn0FTzuhhwXn5bMkTgxyKoyufHIqs6bqAkhZ5SJCCZYtTTbfIskX3fBxA7GG7luaOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌ اخباردریافتی‌رسانه پرشیانا؛ بعد از مطرح شدن نام جواد نکونام بعنوان سرمربی جدید گل گهر سیرجان؛ مهدی تارتار از مدیریت این باشگاه دلخور شده و به دنبال جدایی از این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/22988" target="_blank">📅 11:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22987">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c19cf6b3c.mp4?token=WcVjHSv25mnNceyCTkIlUKdyz5JnBClUCTPleqIi_jrCLFLlvIfVnZI_1AYlJewGj8InInfVxoxMtndApl3QraU4fEoo-l-gelrZc3QFOF0MA0gu3aXtcrFgVcVsyNVSqZFgBJTRFdRC9vtY3pniWIKJbKNe-Cp_wxNF7pRq13suBIeLSRjXPLl0gp4Ui8RK4_i1tqhUYYa7q58KB8CUN81F1VEROPbhzA3cUivxUy-_WqZ3190hGvOMbuIz_y9UsadeMA4I7Dh11Qqk3p-GBLiHD840qBCvl2IP30obzJ8y28yuD4md6ypE_4rxqKla-doY3ghyeaCtNbNSGD7IcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c19cf6b3c.mp4?token=WcVjHSv25mnNceyCTkIlUKdyz5JnBClUCTPleqIi_jrCLFLlvIfVnZI_1AYlJewGj8InInfVxoxMtndApl3QraU4fEoo-l-gelrZc3QFOF0MA0gu3aXtcrFgVcVsyNVSqZFgBJTRFdRC9vtY3pniWIKJbKNe-Cp_wxNF7pRq13suBIeLSRjXPLl0gp4Ui8RK4_i1tqhUYYa7q58KB8CUN81F1VEROPbhzA3cUivxUy-_WqZ3190hGvOMbuIz_y9UsadeMA4I7Dh11Qqk3p-GBLiHD840qBCvl2IP30obzJ8y28yuD4md6ypE_4rxqKla-doY3ghyeaCtNbNSGD7IcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نه‌داداش جبر جغرافیایی توی پیشرفت آدما اصلا تاثیر نداره؛ محمدصلاح اگه تو مازندران بدنیا میومد:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/22987" target="_blank">📅 10:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22986">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d73e5ee7c.mp4?token=d8aQaRMBaRLcglC1kw1hcVzLmvENeyn3TQ-os6yPrTSUZ7CI48jnIEmQiitiek5SexXdxXbrnACiTY9dmPpNfPjaKWMWHrq-_VHtrmbLIkFQBp_jPzJHA1F-a3fHos04UKUXF3AV0T4NMTS0_WhBNoeEIxYBRpG-INQuul1KVyVekY_nq8B3pfscV6_z0TOELu4H-ZIxM0AdAQ-YQjPP4tNUeOFDS6faZbzxdNY19SNsuTc5PP2UT1znwVZjnWhB-NpNmGRjhPy08fr1o_B9_LIptTqGdfL8Y1-uXc8F9aqnP1n6iGnFkpvvSpZ8_IlgUBgkNuBql1CP5XCPd13xag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d73e5ee7c.mp4?token=d8aQaRMBaRLcglC1kw1hcVzLmvENeyn3TQ-os6yPrTSUZ7CI48jnIEmQiitiek5SexXdxXbrnACiTY9dmPpNfPjaKWMWHrq-_VHtrmbLIkFQBp_jPzJHA1F-a3fHos04UKUXF3AV0T4NMTS0_WhBNoeEIxYBRpG-INQuul1KVyVekY_nq8B3pfscV6_z0TOELu4H-ZIxM0AdAQ-YQjPP4tNUeOFDS6faZbzxdNY19SNsuTc5PP2UT1znwVZjnWhB-NpNmGRjhPy08fr1o_B9_LIptTqGdfL8Y1-uXc8F9aqnP1n6iGnFkpvvSpZ8_IlgUBgkNuBql1CP5XCPd13xag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
#فکت‌تلخ
؛
مردم‌ایران تنها مردم دنیا هستن که‌موقع جنگ‌بیشتر از اینکه استرس جنگ رو داشته باشن استرس قطع‌شدن اینترنت بین‌الملل رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/22986" target="_blank">📅 10:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22984">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e_WURKYkKsI-ve_V1pObFT0QyszY-ZmFpc6j0btWXYjjkDFq-EFrK1E093J57SBH-EfLt4lQuTI-GPw62XEVR_eK_ron5X55EWwLTbRgT61Lta5Jpt17OuS--MruDbuSptx7WtQWj6A8KUyWtNyrZumuGwVeHZr7Qfs4nMOg7bi6q_1tqAGC8vat0-HK1UTfAKqJ9nJJorBB163AHmd6lLztWcblNsF3yCq3sLUYgfqigRCEee2KP555KaN5IjLV0OgwlddUiY-HP96VPkUGJKy-hUDSD-Xvg159sg6kqUg0B07w_VggpDLPoBaV-eRWqfpA3LhOjx6c7an6IeEQCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J1yDCxWUUPspAVP685MhrvLYaQ085h_zQv1pG6-adpCC7jW2B448-zR07OcAW1yV-UzQ7oo6XcuGLVsFjFFLV_DW40KjQIwj_VAXbXvlxvaFYuJYTm9-AUeAGakdPt2gL69zraIx9r5CscAYR3fSJwTmVFPNl-BksSCCaKr5HnSoR2LhvdKiBcw-nFjyCvJN215oK00WuLSoNkibgZOCMsAGFKgoqu07cI2lrarBwivtEJF-DgltRJHoa_WJbuXrkdxn3lzHdXbyGXvlw8uZjZjD1dkJObpLzdO1j-RWiifKd580NCD3y_jJEDAJH5bPfIqHWbTfl_fJbAyzM14b_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
بماند به یادگار؛ یه ریاضی‌ دان آلمانی به نام Joachim Klement که قهرمان سه جام جهانی اخیر را با مدل خود درست پیش‌ بینی کرده، معتقده قهرمان جام جهانی ۲۰۲۶ هلنده.  مدل او که عواملی مانند تولید ناخالص داخلی، جمعیت، فرهنگ و رتبه‌بندی را در نظر می‌گیرد سناریوی…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22984" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22983">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fa0118288.mp4?token=UEwp_Z2hcqkrrVRt_nSE6haRefcYNve0-Qc8gT3Uefii6tQBnD-xeIzXO8sQ9CmEJtDtKqt-1yiC6wNwpiOGnRdS66pfklbDCeRhb9JSAnA32BwihGMDWPOs34T9OuEl43pEGc2e3GgPIIW_mXc8PQSjJE5dagBqw3wgoiSc7e8weD4WEAmuvg_3oMS1w_XYa0vcVEXNTlW0gPNy3IGuLqNfkGMbCyNwarypZKUqe2onhvmjJiZ1Y7YM7cp9AYqG2510dYOsrAeJijv2kK8jh6xarhFfjF4rGiI_4E6HkY2-bbLuqJ1114p8a_V2r6MtTAjcSi8eDJ1zn9wKMX0vMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fa0118288.mp4?token=UEwp_Z2hcqkrrVRt_nSE6haRefcYNve0-Qc8gT3Uefii6tQBnD-xeIzXO8sQ9CmEJtDtKqt-1yiC6wNwpiOGnRdS66pfklbDCeRhb9JSAnA32BwihGMDWPOs34T9OuEl43pEGc2e3GgPIIW_mXc8PQSjJE5dagBqw3wgoiSc7e8weD4WEAmuvg_3oMS1w_XYa0vcVEXNTlW0gPNy3IGuLqNfkGMbCyNwarypZKUqe2onhvmjJiZ1Y7YM7cp9AYqG2510dYOsrAeJijv2kK8jh6xarhFfjF4rGiI_4E6HkY2-bbLuqJ1114p8a_V2r6MtTAjcSi8eDJ1zn9wKMX0vMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
نشریه ESPN: بازی دوتیم ایران - مصر در جام جهانی به احتمال فراوان بازی حمایت از همجنسگرا ها خواهد بود و فیفا نظرش رو تغییر نخواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22983" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22981">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qa9xRyebGmjArO8GWfT6doHRx9e8WVeV9az_JObnVNOKZyp7AAbLW3ZBjvzL64NhE_MkUswrRmQVlpGh08Z0gO_F8vxSTaTfbHa0UqmurK5a8p3pVSGVvxiCETIXtX12Iq4r8xY8NAK-gSUEgiEfmiPoLa6t7NolKk4aWJkvn3tbu1Sipqfba1DTeIiBPvNarKHOpJG768NMDAgKIfDktt_I6UzCu96gSRK0hHF_kZDFw7h7y-RshTNcLtCqTL8Kk3zcf5vXXLnlkjUTfTCnSQ7bv234nvZYIV8yiDErOApbRyReUCl43yburRD8ukiVFQQBAeF_I7OBB17_MNmsKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22981" target="_blank">📅 10:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22980">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWBr0lKGa_YIdwT4dNaqCCMkqfooau7dTFqFQZgYpo2zWIjmastrwWTmlit6B1cQjVaH7cZt_rEU8iDaiSnlGwxKFuk5f6EffejSZyKRZKIBEVAHikMsANYRXKHXD35qIpmVbOU3HIwIHnU16EEIDEzZrzzNyj-bFxIzUT2XcFL26mwDJgW10dlsy_4UxyMFL26ZipiUYJUsMrScOcyI2DAvXzgH2NeOgVpMGiFrqgvXSY2P2InV95aPOx2twdiI4b_UPZAL03i-DDG13TDzfmpfttiDnkw9wnrMnWLgvL4sGg_YpXmSu8Db2JesxpLHTr69bG8REkVD4k5sddf5kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌انتقالات
|موندو:
مارک‌کوکوریا به سران چلسی گفته که دراین‌تابستون‌میخواد از این تیم جدا شه. اولویت‌او بازگشت به بارساست. چلسی برای این انتقال حدود 50 میلیون یورو از بارسا میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/22980" target="_blank">📅 09:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22979">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxwVMMtlIxhPl8xoBXFOSGEhKHLSTTgeY1LwTz1PuTDNuH-2gcrx9PQfk4R_QtJvB_fpUgEsD835-Q8rzA7qbPHPHwhCUbRgnmixGUbyL5PVkGOEgl3N984gvSgcpMVvGtwkG4xLcwatqBE83i5lVk172lIg_Y0Jv_8ubXYhw8yWIeBSjbq_YGP3pGCmhaoen-ULcSdxVEvK7zyn1INHUZasA9oAncy6hjAtVYE9yPFEOuLW38BjSglnAsAnVnZ1xZK4CRp6vOesVWqTKDh9ygKsMT0nchZ6ZHWBcVYckMKCsuRpyWVLVOY9I0KbLflL6Pl25fm7k5RYF98TJUjyPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تموم شبکه‌ های ماهواره ای مختلف که قراره رقابت‌های جام جهانی رو با کیفیت پوشش بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/22979" target="_blank">📅 09:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22978">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jn_AsmsaF1wjq3emxfouRSXbMbguh9HAlCg2fmY8RCH_r9QYEKGjnwFaD0LAMXBw4t7Wy1JLeJINHYrDiLvzxirpwg23lymgJsVdKxr4zLLhE5dMsNGQmQ5KHo4wMeT5mHf3lvf7wFZQO_G-LHYWp0HGL0eQ7l8QJ38KbbgIu0IcsgnMz15xgDpNKy0vPmkrBj7aoDgT-6mLBIq8kAUzZD-mWJtgFwW4yXC6glmdKVSEoyEfI0dayvRZf3RT2ufprUP2hx5COS44YF68_eyV36aHHbK1NroCVgcwwpwrHhQWvGGv17jf9c8Uenta0s8w-W8KNi6AilpeWVFqDSex3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/22978" target="_blank">📅 02:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22977">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGPRCqzfsjkoTYGbN9ojrTGhab7tKEtfEicS8iNTauc3DwBrWWIHQbawTQxROxttyh8FSmPtBWnF2AOCffxJeEmrpvRVU0MUzv1IdYbW2s_YdCibEwztDu3joJmbbQOVFjUIQ2t6BJNeRVCwlxXCIkt3ywgdl_fpoeiSen3o50JsZvozcVEylf5qBPDwIiCZoEK8iBycLLRRvmbj8NwgOtoxVhKbgBCgwyn9BTdCoQxuqS3n7xJ2ndZVYIZh9RFrL3wIOq2kMeOZPOHgnEuvO4XmbZsWiOoxai_P7VCgY8-Jgja0hYqh3aPMWiEyMj0_L7sRnQ6NdrTpOB6QVaUH5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/22977" target="_blank">📅 01:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22976">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSTrEcTXGhixTKyfPcup0uEExaOIB9JZ1bxppemdrvM12GeafdPHEB0CeLU2jZO0Eed_joJzuLyep8W3IY3eAEKXccm0KQHfFXN8vhGF8hA9hb9Acj4PDEpIGgr0Zv5XdzFcS8J6LK7bCHzRys2h5lZ0gMKZ4lLa07xQpiohN37cz6c2WCrtS8g4y3W9GFQv_N7Rk67i2XNNikWVBkG4aAdZraA9VLtvYORgr2FXlDJyj5FJVJ8GDxGw8A9YxUTMrStvnVUIkha_c_bsxh4kzYCmnZEbmBzfXNMt5kbT0Im1Qcm4Ti_ezvjs0impkIC33Oe4bXH7LwZZ9JDFMQQzRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛پرسپولیسی‌های‌حاضر دراردوی تیم ملی از آریا یوسفی مدافع‌راست سپاهان خواسته‌ اند که برای فصل بعد راهی این تیم شود. یوسفی از پرسپولیس آفر قابل توجهی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/22976" target="_blank">📅 01:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22974">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHKBTIoBrOs5UMNvVZzs-8MQC2Ky-lHqHsCar53tjd7nLDgL2YSeRF72cIuu_tHIEeLN_QCs70Puz9NImNRhQXFtr--13oeoxelM4ESJyQsjG-Xq7c01L9Ktawo_o1yjBXoPe3ouVVHTMyeIsPZXixkoDewqHXZRzqrkKUhaPLCA1k61Td2K4j0JEfIa24WV-0E2pXVUfp1fEtEdFbkEdHrWsYv-5F0kGfWdP61FjfU-q2LfQ9vEImkDum7l6peBpUGtyJj2OJzRt2jOHAUmBc4GnEEYM_aC3unQRb7ovIPqjvcigixbN0qyK4QH16Zvkmc_b45BOgnC2zYBfwcHyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارهای‌‌‌امروز؛
از دوئل تدارکاتی شاگردان کومان و کاناوارو تا آخرین بازی فرانسوی‌ها پیش‌ از سفر به کشور آمریکا و جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/22974" target="_blank">📅 01:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22973">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fu3gk0nfk61jfUIQLq3pf23w2AEnlU5U3UTTkOABJGMyd6w_BdiI31F_tu3vkgd6lP9MlK8mkyPfPAzYNpVemTckxt4H3eSfrwRN6BGHHF_8QxGGeWKPtBAIB5_aGW8OFZ3cDDA-Ex9iuP2HxxlpCY2O-Kmk6Vd_jNpyZUxjJEUpbfbpsJXlrPWS2rl8pQfNMjQrWRJIcOeaB0lezHEmnmKqeJya4uTSscDQUv0bsKhXMYj0vqwNTNbHAxEyLhRGJPeK5sm9nmo0E9_SMCUF7WX_mgSsCy4HCgu-_yfwsxOy4KTIFdDXraSaw_HIIwLDP2063s5y9zsGdc4zapvr8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌روزگذشته؛
از برد آرژانتینی‌ها در شب‌‌استراحت‌مسی‌تاتساوی درجدال نروژ و مراکش
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22973" target="_blank">📅 01:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22972">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3KdmgdjgeUCEeUvYFtWd9iWJ3RZaNJX4LV3E_miCDVS0buzyMJBpq6X4qXSgcFizoOhGbey9UZgpaRarDjfn9dQ9_iRlOuUYu-Y7aIE1OcdgxOBrt6_SivLlxCMZ-greWNnT1evrg1iHTpOEu-3YpQDJU8jJBeyd-PEqkr1CWeUidui-nK8ySx_GeMXnG9F-E0NyWhyZe0TWIxBoDelzY4VwL1tDpCNW01lmcJXHMCaGrWwIiDj5PBEJKYCX2f3dAXZkFYiRhrarnk6eRdOJ58ck5LwnErxH8sphx8hXs4gH5RqsMWOs5soBFCriwvUdfzPWCclxhXmpSGstATbWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوشش‌کامل‌اخبار جنگ در کانال مردمی مجله 21؛ نمیدونم چرا سرنوشت ماها اینجوریه. انگار نباید آب خوش از گلومون پایین بره. امیدواریم که حداقل نت‌ ها باز قطع نشه که هم اخبار داغ نقل و انتقالات تیما رو بزاریم و هم برای جام جهانی دور هم باشیم بازی هارو پوشش بدیم…</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22972" target="_blank">📅 01:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22971">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a6fa71d1.mp4?token=UKiA0ACOHgomAWv4mNYB6Y-eAx-oMfVm21CbQjn4pqXBu7OEOIF732u4RdZnqJXqvSekcBGaruB5M8ItZW3AW8Pdu9E_5W9y41nT1bADnbC3qi9Yn8fBR0YTYeh9OwfJtdfGTCYgVeZixYt_S-hnSHI_4S3w6bYkNIcrGPgmcY6hwtGDOYP0j7m-XHDgcPhfaNvbUlelObjfqn9KxiUjYTEnYaA1SYSR8sVPRwWQrwCEig3Z6pcXBjaHQ4Y7cYVO8APHHG_yscDBi3_G0qp9QZKuz2oI9jIwDG57c1CwakjSheC9kSwICRbKp9WPZZo9RHzrxNikV1_u83pSgVdok1BL_eOWNDpJ4NVD3dAUVbnNJxUCOYuElE5Rd3JUoaaLrX6cejypzLvVvtT24hk8PG8uBx91SeLPvZzsxyVfCoIwdYMVS74P0LGNjnlrFxIes6AofVf5dbCg91jpr53sePEilmZlDo1xYoa6gfINp7N3udjmVydbIpX2o6zSItAdu9naVOeHAA7BNTLjgzSPZorllrZJibxBdY3Wkuv9_1K6K9_F0i-wZ4bKQrVO17xhaQOkRc3XGDEGD2hTQfz8V-0AzrQNZht1Z-Ybk04kDwbyaGJwKM_wBMjlFlMyRpOuU4njgpmBj6VIk3X4Y-Qimf6Jd_n_H6UpoCQfLDnFjP4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a6fa71d1.mp4?token=UKiA0ACOHgomAWv4mNYB6Y-eAx-oMfVm21CbQjn4pqXBu7OEOIF732u4RdZnqJXqvSekcBGaruB5M8ItZW3AW8Pdu9E_5W9y41nT1bADnbC3qi9Yn8fBR0YTYeh9OwfJtdfGTCYgVeZixYt_S-hnSHI_4S3w6bYkNIcrGPgmcY6hwtGDOYP0j7m-XHDgcPhfaNvbUlelObjfqn9KxiUjYTEnYaA1SYSR8sVPRwWQrwCEig3Z6pcXBjaHQ4Y7cYVO8APHHG_yscDBi3_G0qp9QZKuz2oI9jIwDG57c1CwakjSheC9kSwICRbKp9WPZZo9RHzrxNikV1_u83pSgVdok1BL_eOWNDpJ4NVD3dAUVbnNJxUCOYuElE5Rd3JUoaaLrX6cejypzLvVvtT24hk8PG8uBx91SeLPvZzsxyVfCoIwdYMVS74P0LGNjnlrFxIes6AofVf5dbCg91jpr53sePEilmZlDo1xYoa6gfINp7N3udjmVydbIpX2o6zSItAdu9naVOeHAA7BNTLjgzSPZorllrZJibxBdY3Wkuv9_1K6K9_F0i-wZ4bKQrVO17xhaQOkRc3XGDEGD2hTQfz8V-0AzrQNZht1Z-Ybk04kDwbyaGJwKM_wBMjlFlMyRpOuU4njgpmBj6VIk3X4Y-Qimf6Jd_n_H6UpoCQfLDnFjP4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از کواراتسخلیا و کول پالمر تا میتوما و فرمین لوپز؛ 30 غایب بزرگ جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22971" target="_blank">📅 01:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22970">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32598b0bc1.mp4?token=K96CGfCHHmZ73Sg73My8qGYyvmRY2d71fDpSD_q0gEswehiJM2x7dyMjQ966qtxY7iNVEJRMyYNpAphGteYXpBK4fQRjAorOyJMhnwqAGO0N7TmBQ616HYnZddN7DIOJjfC1rucnOjFVIr8e5x-CkhnS_6ezmBsfBW1K_npAy0y3rXIc6kYhhRAdLGq6rpn62bm3bxrewqKGo9AT0a6h3XrfbhtdFp756Fv_BvseE3kSk_Vkrosy2NygbyG8ylrv5GuCTUw0rbK9FRL2uDvbFoY40geBthmg95110XJL8XKKQ9zpo1lyB7s8jv8cV1q2QTSxJaVHgfTF5DzXh4jsRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32598b0bc1.mp4?token=K96CGfCHHmZ73Sg73My8qGYyvmRY2d71fDpSD_q0gEswehiJM2x7dyMjQ966qtxY7iNVEJRMyYNpAphGteYXpBK4fQRjAorOyJMhnwqAGO0N7TmBQ616HYnZddN7DIOJjfC1rucnOjFVIr8e5x-CkhnS_6ezmBsfBW1K_npAy0y3rXIc6kYhhRAdLGq6rpn62bm3bxrewqKGo9AT0a6h3XrfbhtdFp756Fv_BvseE3kSk_Vkrosy2NygbyG8ylrv5GuCTUw0rbK9FRL2uDvbFoY40geBthmg95110XJL8XKKQ9zpo1lyB7s8jv8cV1q2QTSxJaVHgfTF5DzXh4jsRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ایکرکاسیاس گلراسبق رئال‌مادرید در مصاحبه با روماریو: «مسی خواب‌وخوراک‌رو ازم گرفته بود.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22970" target="_blank">📅 01:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22968">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sp8gp4w6jvaI-mIK34y0czt4Rywnp9a5eH9G1grAp-HsBF2o0ztIhNkoOWmKjoyhPjA37uzmMPBZoljrzMbwEuqV4OKLKcMxooJgqLPh58vO2uuRd6cuDA83N6_g56eAujP58MPEPp9ThWNnyMv5Rv5huF5rewOrXU8CyRiVzrvQpHN3aYYTLu-1OyEUP-e-SBd5zPxUXKfDnFsQABaUbPcYvqqnsippQl-M2-KvR4McwwIVWSJFeGNbAACuGJERQ1v4G6ZFGUyzPnmf3oxJ0X_0_aW578YBVNq6eU5e0KFLCn4FpHvlJ9PBzh7e4Fohs2e9kzZ6xh0ZYBJuhaASvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای رسانه‌های روسیه‌ای: دو باشگاه ایرانی خواستار برای جذب کسری طاهری ستاره 20 ساله روبین کازان روسیه به این باشگاه نامه زده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/22968" target="_blank">📅 00:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22967">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca6abec005.mp4?token=Sr3wkceVzpipnU6Je0T0Vb7M0_0wmdGsjidO3-6LE3LOOpuyHqp54DHeEN3QbeTWU5hL9xS860spc-C5ut13STHkllSMXQSrBiPydh8-9Q8X0iiFvkKWPS3HmXHFhnpQrHUoKG8FGn5060reFCiaVLnjJd_AwpyqEd9ljmwrEXQ0cW0aRWdz9ZSa2qvciYGL7sxCV_mEqI1fCfhUzr7-ZAH--oBDit82vYZG3qJBViyVBj6GJH3IC0We3UqzvDX1AjhrV4D4JhGCaGhvEcqxAp_atq7JyJxtdhYRbo9J6a2278N-LofRHLslzWQ05S5PavkDosFIYV27r4_yTxYnqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca6abec005.mp4?token=Sr3wkceVzpipnU6Je0T0Vb7M0_0wmdGsjidO3-6LE3LOOpuyHqp54DHeEN3QbeTWU5hL9xS860spc-C5ut13STHkllSMXQSrBiPydh8-9Q8X0iiFvkKWPS3HmXHFhnpQrHUoKG8FGn5060reFCiaVLnjJd_AwpyqEd9ljmwrEXQ0cW0aRWdz9ZSa2qvciYGL7sxCV_mEqI1fCfhUzr7-ZAH--oBDit82vYZG3qJBViyVBj6GJH3IC0We3UqzvDX1AjhrV4D4JhGCaGhvEcqxAp_atq7JyJxtdhYRbo9J6a2278N-LofRHLslzWQ05S5PavkDosFIYV27r4_yTxYnqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🇵🇹
امسال مدعی ترین پرتغال رو پس از سال‌ ها در جام جهانی داریم اما جای یه نفر خیلی خالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/22967" target="_blank">📅 00:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22966">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TjkAbphPv2MnJIq-sVbbH9bOp0DlX5QWKrhNnsmbmZ8Ibi_H9s3EBhIXauQOMcW4GjR0WG_5l16DnsxXadVjVHpDKPgx8IAB1KA-i82f6WgbXbfnpmKugrWnPazwrVTvHzssY6UT7l6mBAEjko02Vl55-I5__KwpWzIGzUj8JEhJMpalKedq30BlPpw6lBPo17F224lF9tH7sZ05QddfuSvrPjRSe_Kv4Ie5ZqC_l_FyD6XvAGDpqAcM0uD1_8FTYTHtxM88ZYIX8ybHSV-S3ZBNi-FqlN_hBe2CTHlrHBTV4yLloYBUscL02O3wFHQSMlVhzMQmppdqVw0VvGSM-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال خطاب به‌تیم‌های خارجی که خواهان به‌خدمت‌گرفتن امیر محمد رزاقی نیا هافبک 19 ساله این باشگاه هستند: 3 میلیون یورو پرداخت کنید رضایت نامه این بازیکن رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/22966" target="_blank">📅 23:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22965">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDkQO32bqRNP2dcrS972t09ZfxR6jv92gvlSPGHuzQYlvXJ5uso05egh8992o42_tMauj9OS-6aGRkE5aVBiej9IlkI5ixGfeKRQw-oEUMaY2fo_Kv55Lo3ydWBpCf0lwv5rC-ILHSv6OwfnjbhO26TTCigaoNsEsf9FrI-YckFiYf9IXWLXZehlDVAbLFtic71nF1CZkClIp8Df5skdpBqSBCb5rmHAPz05vfwbkPGpcr80nPB-rWPBDFxQkC_Pkg0_8tUd53Moi3YYIUCukwcYJ2UTile_VednyQaXepP-W4bMMhrfT0mwNd_VQ0nzFmrcCVq0GIfAimQYNfLBIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوشش‌کامل‌اخبار جنگ در کانال مردمی مجله 21؛ نمیدونم چرا سرنوشت ماها اینجوریه. انگار نباید آب خوش از گلومون پایین بره. امیدواریم که حداقل نت‌ ها باز قطع نشه که هم اخبار داغ نقل و انتقالات تیما رو بزاریم و هم برای جام جهانی دور هم باشیم بازی هارو پوشش بدیم…</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/22965" target="_blank">📅 23:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22964">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eaff3256e.mp4?token=d3DOQNARXsAW0pNHeqALgOySHXC3ucRvg9WEgfJbFrtHAGiHn3C7v4FnKPuLbVEmhLJFQ0aielu18bCjaRhlmGNIfxcXIhI7lInHkNnV4dudOOGgKG8SOn5Ms3YoCm3hAYCAND-MqO8pYogVAdTG750wVougZhELm9RLnNuU7jwzTRMpG66jqmGEXcNjs_58EFuUVGAaiLGbtRvMAMnTaztd5MIRVoeTcvgIMqRi-lmIzQGmxbu69JvNgk_VwKkdfbn8panfmOGfcNVRP0KGnT5NSa0g4usYnny16nAYrMA-eyzTxL5bt-tETN45QWDAsdav6XBB98DM-KXmhwbGjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eaff3256e.mp4?token=d3DOQNARXsAW0pNHeqALgOySHXC3ucRvg9WEgfJbFrtHAGiHn3C7v4FnKPuLbVEmhLJFQ0aielu18bCjaRhlmGNIfxcXIhI7lInHkNnV4dudOOGgKG8SOn5Ms3YoCm3hAYCAND-MqO8pYogVAdTG750wVougZhELm9RLnNuU7jwzTRMpG66jqmGEXcNjs_58EFuUVGAaiLGbtRvMAMnTaztd5MIRVoeTcvgIMqRi-lmIzQGmxbu69JvNgk_VwKkdfbn8panfmOGfcNVRP0KGnT5NSa0g4usYnny16nAYrMA-eyzTxL5bt-tETN45QWDAsdav6XBB98DM-KXmhwbGjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/22964" target="_blank">📅 23:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22963">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇱
🚨
شمال اسرائیل آژیر ها روشن شد دوباره  موشک ها از تبریز و کرمانشاه ارسال شد</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/22963" target="_blank">📅 23:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22962">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDOfXHQjRhbR2qJOKNws1zqKOnqWFqWRDtINSaG4J7wzcCZgegfiFkqSimsBFus5ZqQXsu30i4OJSdhqCi6Ib-sudMcU21Ldu-9ebnYsVzuhnX-ZYkCiCrVVRrWXniY978iJHXRy1G5NkElVFO-UjdgxRRNwlYiqCNuex2L1RYGnJ8Cn3GRmwy703NVw39_sXtBPUeaAwK8-NLcOuaSDL2VDyHN7MghU7BvovFokNCyFsyoEXnY-WufXKzXTh31nUnom8CPL0N0qVWY0YYGNqW9gSHmm8lzV_nhkMg2XCUIUCuH1w5CDcapgMOaUYa4DIcDWKeLdVHgqDeCj4c9I9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اتحادیه‌فوتبال دانمارک رسما اعلام کرد کریستین اریکسن هوشیاره و تحت شرایط خوبی قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/22962" target="_blank">📅 22:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22961">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLLfkI6ropFmUrS9nYvO90VkZc2UjfWVvrAvMCIUbsizslpjVA0U-0QRBdlemT_dDOebZ2wsDIUx_uy6X9-so3ogcDuYDAvram8_Jn32i520MfFvwOMtMRCf5EvOTYfb77YI7nmlVW-nPkCqR7CuV3VHfY2KONEh9ECs6MOBHXEKeJ20bFmLUt-zPLo35Z6ctvf9x14yhCGKhg1-dF90ZSnjzYGXXPHYRSDRp9uHBX6SQZbsI72Xkh2U1HTirOXiJvC_0jMdAH2I_Q0o-reYlLkDTETTk47eCEz59uTaHEmB5AGERJ1O2grV5nPscRpDW_wsQYQTh6kd7nsnYujSRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/22961" target="_blank">📅 22:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22960">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqXM7Kpk15dUwjIRUbKX6Z0Bda-Mm7SwCpIUtVCADS-ZmxATp7Gwppx5mNYlCUxtRIgzr3SRM3BMygZkpFEQc8SmcZmkbfEmZH8nJS84Q5xWG_IzB8e7wqjPzZDpdtfCV8cjRLAyfF4eUUIQJ4dbVnwP6XhFtyfm8-plMjhqTmvzygUktAY5xClmKnJaC_1XBJHajj670Jr4iu766x5JThIhiBtUt0qMoZK_-PGvWehKV4ok_ob5PwEp_YDC0yPUJpjbYGD-4CLDVTZ36zJtJvUj-03Xd2BowbPLgXTPQNLiMGJUbmeelbuGMBkxPEIEP3B_dpMHeZwWqUiHq5sN-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری
؛ شنیده‌میشود محمد عباس زاده مهاجم سابق پرسپولیس، فولاد، نساجی و تراکتور به دلیل مشکل قلبی از دنیای فوتبال خداحافظی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/22960" target="_blank">📅 22:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22959">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ws8XYDB15gbLR3uFo_d7V96rX8xN28fdHRNhkLHzwn4CRHZsSg0KwueEOslARjdhFbJ_gzW8c82Z5a7x6mZDb5ekWYNyULA0T_jEgLyXFhfYw0IJPip_UKAo6wMrcgsExNM31FkEXdotcDBG9Nh3Izb6jkGVB9Ubz9aOG0-oULv9UKt4zRTJV4ZnCgVqveSPKk5CY0WyVIUWJ-BNfF7GGOXzeBCj9AODsExKO7MU9K-GCAEOp5yxrVnK5nk_WxypUS4mj73A2eONk18Ef3-dV-I76l7f8c36a54Lql8Yrpre-Iy5hcfRc49vMFjsIcHKjMadJDqdpLBYzvnXMKQd4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فوری؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22959" target="_blank">📅 22:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22958">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bffa01c1d.mp4?token=ZjIG_wXn3jQal3Uyz5ixKkrUQsaO_6eI6nRA6-7aFq6epVjDYnNIX5aytZYOeG9rskTVCQKHV8Z1J-25aSZ72csj09dLTm9CMFIiLST4JGHv9OHVtErLfXnDEJr_5moVgNRFEblllWhgkm58iKmF7vbm2rrMLzivwzoX-A4jZXVJzjgmanxJQtwBWjV1DF5CbKevFIgWuhMnUFlEqy8V7_tN4Ma-aJQOrkZfIVKQbTjtesFunH43esu_3M4afobca_cVqKR27dUV_Ae4DUjcwWwIbVknUtw2rrJOAt72Qipvhnf9HvfFuuxdPlcVC8Ihc_xYkT-RbVFIwTOgk7dtFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bffa01c1d.mp4?token=ZjIG_wXn3jQal3Uyz5ixKkrUQsaO_6eI6nRA6-7aFq6epVjDYnNIX5aytZYOeG9rskTVCQKHV8Z1J-25aSZ72csj09dLTm9CMFIiLST4JGHv9OHVtErLfXnDEJr_5moVgNRFEblllWhgkm58iKmF7vbm2rrMLzivwzoX-A4jZXVJzjgmanxJQtwBWjV1DF5CbKevFIgWuhMnUFlEqy8V7_tN4Ma-aJQOrkZfIVKQbTjtesFunH43esu_3M4afobca_cVqKR27dUV_Ae4DUjcwWwIbVknUtw2rrJOAt72Qipvhnf9HvfFuuxdPlcVC8Ihc_xYkT-RbVFIwTOgk7dtFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#فوری؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22958" target="_blank">📅 22:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22957">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GI6Jv8SQyf4h7mQmMJkmUnDJMLUVc5PfVrMPQPiJ_kXYPquiQphF9dhFWlYKaZK3ytOMB1MpT6soc93TdBp7PVHikWqVT6igT-X8T8rGANq6VwswGnBAxwrAb7qnU_aT2sRaqwrv5VuYRLBP93os5S2yo-mXCd7m1bD8_8QCGIlXNk4ATHdo-rnG2QCn7UIENbq_a_ind2GjcxIJj9ezqOS7ef89eVExPf2gU70QQqzPtZ9dwuA7fuEN1ZTxFwVVzTo3tve0ODnFK_DKB0szom5jvDNyA0Qi-DVBNjX2BL6K0xnX2pLR17uJJuXWHaGkTHrNObppzdGUV110CGkATA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛ به‌احتمال فراوان آنتونیو آدان راهی لیگ امارات خواهدشد. او دو آفر از باشگاه‌ های اماراتی‌دریافت‌کرده.همانطور در روزهای‌قبل خبر دادیم جدایی آدان از استقلال قطعی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22957" target="_blank">📅 21:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22956">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b1b174faf.mp4?token=hWMD0dXJrJJMd-_dJi3HYE_a2q1RwEJpfblxJ5ABTpe5-5UeH-iOsxuGC9PpaBwCn6ZaUw4KXUCYUIaZDTxmrwCmI0VBQwBj3rGSaQM5CQuqvEB3AEC8c6PJhDB0FDvw4s5te-jsGTOMe6c5IA7xTj-njaLrbf4VutdDqg95li_Ezq7_yZHhuWm6VVhokSz0hXyj0DwA4WkiUohOgktT1oGyuPRnL1Q8RjHxau32O5FIqAG0LaWgzUzyvcW_79_0YiOXK7uVqiFl-wPKz1SZu-AnSfH1xDdR3WaJwgV0eXs6okyX-CA4c3VzChjyF9jkE-i2F8-IXF3VIxQ8aeXUIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b1b174faf.mp4?token=hWMD0dXJrJJMd-_dJi3HYE_a2q1RwEJpfblxJ5ABTpe5-5UeH-iOsxuGC9PpaBwCn6ZaUw4KXUCYUIaZDTxmrwCmI0VBQwBj3rGSaQM5CQuqvEB3AEC8c6PJhDB0FDvw4s5te-jsGTOMe6c5IA7xTj-njaLrbf4VutdDqg95li_Ezq7_yZHhuWm6VVhokSz0hXyj0DwA4WkiUohOgktT1oGyuPRnL1Q8RjHxau32O5FIqAG0LaWgzUzyvcW_79_0YiOXK7uVqiFl-wPKz1SZu-AnSfH1xDdR3WaJwgV0eXs6okyX-CA4c3VzChjyF9jkE-i2F8-IXF3VIxQ8aeXUIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#فوری
؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22956" target="_blank">📅 21:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22955">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKtZU7mhPpHt2DzukLKulOBfE0yH2merK76yyXZ8p0eE8WFfvJxLtTBsbBeG1g9dHJlfF31wF_6dMR76OzO0HLmy_uK422AOoBciGxZFcJXEE1UDG7Q2kFeRv4RpiScPEjf7IGOrSBeHEPnVAUsXgZfeMzVIt6DKH7F2qcHAc52hyXDY9eJpNKcGEFLjpddfwgom8c5GT3o2drGesZGdwXvxfq3-6NItKjXDTbBupTvcM1xcIDrx564QTZ0CH5N-26jYIoOR9XOcwbk3MeIOWS24ZqNuRXyh1dxxdGcT7eF1uO6RhGsIvjh5fopKhWcD3gfRHC1yavAie9IE4kYhkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#تکمیلی؛ کادناسر: بعیده که‌سرانPSG ویتینیا یا ژائو نوس رو با رقم 150 میلیون یورو بفروشند. برای هرکدوم از این دو نفر حداقل 200M€ میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22955" target="_blank">📅 21:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22953">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DyJWzAOQsu7uXRYssZxY7UU3xWBTviZGHYe5e1qH0ywiZB3H1a1yr4hx3u29yv_9aozHmBTlGcsEDU0r62T3J0VkcCrj-R5kIzzt4Rb7_oYLOnrgIlw_MeSIHcMO83UCwtAdYHiQ8Xh1UAEOB_bsqi1B5EgxBlZ6CxU9XKyPOC46rPFp0T-L84DKl5CAteUlPnrQKyQJgBm21otzUaYkc4_uR98UCSoIxzPsGieBL1cs_gvpMOscNFqv8WtLlhXS9NNpchBPCfHr7-sjyQIPkc6cWzpBsDZ2fxSillAj1_IQz3z-1fmBJ5pVe1urd_mXScAnnIai02dRoWDYxL7hgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OQlu1EQis6kV6Q9mUeHbzuNkgf84OjviqNc9ssm-bNLR9pkIxn0ohSKtPFq5-vimjUsW_m0vVoTv-VeUwz5x2_S6MWyO4rBT9nsQwWaFIywFOo9QuTfgHOslCEz1MVXgOKWFyjWHkh_4v0MhXfuNxTKWcRuaOV7VYBJg0EQTTgoGHwIlk2r3ABcMfkPFn2q05CU1C5YDoAZtZ87u9k40VAlwgd0iMZrI2u11x8ikwL6LHS_VidTpwJv-4bsICQyyOPraYYzykbFt9r87CasU9Q2S9s460r1sk9Q9-ImPFED9UedUvmleEOD_1EeWlvU93zOeKPrdLMHM9PlFeqtIag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22953" target="_blank">📅 21:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22952">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qn6rsbKKInYIwgUmimFsyTg79nDTFe33rjNp6veW2mdUOZ3z9aDV3HOPe7qmnbZGf9k35napCCsCyKSLsdhsHDkXIXRe09-o6T--5vo9VcGqsIXWTM4ogsPRQzRozM8MM4FIW-xQWHpnjt7pttWg4OFzx_oTfyL8jcaAbjV-ZQdZwHtOYoGYab9551jVdNbjeYZRZ-kHXxZz0nAKe7R6uFiV-FeoSVMf-TDiJTQ-NGXj9w-KuPz5Nn66EI6b8x2q9_Q4JgKvtCrzXpcbCPld6dLI6O8Wq34U0vLdAgJNyZiBsMnYVlsL8Z1Y4lVHxqnUWRclsJ6S93J3F1LF0T13fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
حواشی‌ دیدارآینده ایران
🆚
مصر در رقابت‌ های جام جهانی 2026 از نگاه هوش مصنوعی ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22952" target="_blank">📅 21:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22951">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c25ae3aa7.mp4?token=HACGIo9zGKBOKg2QZn2THrWh75S3-n5ai_-5S2zBGtFJupN5I4O6Telo5ADCJtX9kr6_Adgu3lNmG3ZYg-zg92wIJoQhUSQsOdmmhnsRUn26MN1ycyNSoY4I71RyJ6mEyv5bs8DX6hCa0kABY6nUbTzuwTEfKkANcaepgDn96uHyoCZZECB-namdH0bl5WjMO5QQI8cSiFuD5xZSdJMoEIrsyW7B05P5nqfKeOK1C2GJHXa6L2vTA1utOiTs_gAGr0Rr25l-GiGAitPxuf2faTEUWoaN94lyA65XPb-NVN3sQeM5BY0ISphoS4Ry8757-4_b3hBRjbutWKmpai-bKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c25ae3aa7.mp4?token=HACGIo9zGKBOKg2QZn2THrWh75S3-n5ai_-5S2zBGtFJupN5I4O6Telo5ADCJtX9kr6_Adgu3lNmG3ZYg-zg92wIJoQhUSQsOdmmhnsRUn26MN1ycyNSoY4I71RyJ6mEyv5bs8DX6hCa0kABY6nUbTzuwTEfKkANcaepgDn96uHyoCZZECB-namdH0bl5WjMO5QQI8cSiFuD5xZSdJMoEIrsyW7B05P5nqfKeOK1C2GJHXa6L2vTA1utOiTs_gAGr0Rr25l-GiGAitPxuf2faTEUWoaN94lyA65XPb-NVN3sQeM5BY0ISphoS4Ry8757-4_b3hBRjbutWKmpai-bKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تیکه‌های سنگین ابوطالب حسینی به تاج رئیس فدراسیون فوتبال درباره عدم صادر شدن ویزاش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22951" target="_blank">📅 20:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22950">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7VS65HIpH0uPOLc27O8aTJVgNzOS3qmEpSM4XqWjErM_-DgyxRlqzRCSy8AMc1Y6xZAgA3obTVV0bgK2k26y-2nStBYCdPuJfFTOd6mPWq5NlOamxh_VsWSaYTJeNS-8G3h1vPhkeA07ksC5VusEn73ZeorzJz5Jy3FbVcYIIkaab9T-4xV4a5kPkEeZMmMZr1OLbvl0NvrsdH-8Br3oyRo6g64EDpn7J7Dw6Ze09OFYuqOeJEISvEsCZmGULxzbwcxwioYvZmykVpjR2oKIhLrFhY6FODmgy4qYmY0DSdok8TDGKPPUj28rhjvJ7RYm83xpFC-97wXkyQcCEUOUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌فعلی‌آبی‌پوشان موافقت خود را با پذیزفتن دستیاری دراگان اسکوچیچ درصورت عقد قرارداد با استقلال به علی تاجرنیا اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22950" target="_blank">📅 20:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22949">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dheMC_5fLzhveHhElIME-EkOS5t6ozViEqkr_JZBusrxnP32T9OpDkRJG24kTlzWfNVc5eLGZ1zxmEb2ov5hgYPTjmEgE1ILnOeBzRlk0Bt2OxS-MU-f2aAQBGNGwlX5v3EamCHkakGeDivH_rFJzzGAhVYtvdyPNKRPo5bMlfTWqFC2kfqGsBRU2px1uh8rZw8Mve6mj4NPVHu6S1RAco2Eunwi7qqY_LEx-W08n7OEyuFaGXKiqYy1GjQqkWoIRzuBTs62tyz1Njf8hIwDNlKS7-Srctt0LY2O2xnU4bCooLw1vYMqI055vp1RCpAFDNy3YkaIJ5Ssydj7H4SVoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#فکت؛ اگه کریس رونالدو در جام جهانی 2026 موفق به گلزنی شود؛ به مسن ترین بازیکن تاریخ این رقابت ها تبدیل خواهد شد که گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22949" target="_blank">📅 19:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22948">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLZMvP-fWXeyqfc1clV-HksPEK9btxJ7jOKurX-hvsQnJ0ePdXWS5N6t-gkjKia7-xD2q76zGAWYC704AdwmLqTMQbyyRL_MrfDJZdh7SovAIowib8L5uVq0IQ61sNZLk-LHC3wT9sDGTmyfLhI3ZUG0z6tN2PZFRgdayZliIlDIdy2Zm6Glxg9C0cpQwU2RsUilnh03vKytZgNPydQ7pHd9ufhicSnFmudUPKisfOEZe25V8VIsABFtD72bcubbjo7b69rvra0e_2m674kjbzIBW4TYp0kw1cu8qqRGIK8bIU2AkLgtRBBYhnWLboUdUu64Q1gNE4Yy3CEx8J1FTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ باشگاه روبین‌کازان‌روسیه به مدیر برنامه‌های کسری طاهری اعلام کرده هر باشگاهی که کسری طاهری رومیخواهد باید مبلغ یک میلیون دلار بعنوان رضایت‌ نامه به‌ باشگاه ما پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22948" target="_blank">📅 19:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22947">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c78767e61.mp4?token=SwTRBq8lB4ecJnIwq_WVfZXCwTDCUXofAipKjEZHDZ2gRTGadUAMfYx8D_upn7S8ltZrbdbSxyyu4ZmyIi4mYqvMaiWd3MEdrbFz1bY9knW2zIwN5s4UjVzhi_pGGFKrpobyo7YzFpgjpXAJuvnmctF6PpJ75iHYKgM-BVEHc5wqH3Wn_O2jSbRn7U8ip3961aNydnXDjmzSuXuRQvrzmdw8Qm6i9OZPI_dhk3GlX0WCu61WuzzZiXqloC43mK7XzEqbJ2fJdm8_-ZC3xb2EbXDK-MN3PIElqyW5RFpS2wi9c_vcRS3TySHYJqmEjkwBu-5RbTLL5XYDR2RPbUkdbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c78767e61.mp4?token=SwTRBq8lB4ecJnIwq_WVfZXCwTDCUXofAipKjEZHDZ2gRTGadUAMfYx8D_upn7S8ltZrbdbSxyyu4ZmyIi4mYqvMaiWd3MEdrbFz1bY9knW2zIwN5s4UjVzhi_pGGFKrpobyo7YzFpgjpXAJuvnmctF6PpJ75iHYKgM-BVEHc5wqH3Wn_O2jSbRn7U8ip3961aNydnXDjmzSuXuRQvrzmdw8Qm6i9OZPI_dhk3GlX0WCu61WuzzZiXqloC43mK7XzEqbJ2fJdm8_-ZC3xb2EbXDK-MN3PIElqyW5RFpS2wi9c_vcRS3TySHYJqmEjkwBu-5RbTLL5XYDR2RPbUkdbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
آقای‌ممفیس‌دپای‌هستن مهاجم هلندی اسبق بارسا منچستر و اتلتیکو که داخل و بیرون زمین می‌نوازد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22947" target="_blank">📅 19:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22945">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzVG6l3nogxe8ZnpmHm6slZPjiXqQ625x1zC4XiXNs5OYZ_1pCbqsFf-ZiQTexRMBh721TPalBJdgeeK3PWXgCWOq_ODw6PHgUsP8ez3wdBEARekAvuequg70UTo3hT4C2E285FHed_BLzDeVaQnVnCOdiIVmsP4192IBPio59aDZzhpYm1PskODpTIM26tmgyMi-1dYfgRQY5kBWZWvzq0gcATK-l4RPth6BWKvet0fGl94M3BV00Qlz3Iq4wWdbilxyR2jwqm_a5AgLVrYqOw4oDj6S6x1r1jvvsp8s60V23_MhO6WNEbqoc6hTq2kHowOPVxq6uFhgyH8-DBcbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22945" target="_blank">📅 18:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22944">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhGFZdjG66HFnMig82CquvjSX6LWo2lTnPfmUm57NTkLIkeJ22PDpgmnSCMhyVmaUK2-wZ7Wob3mrYY12KRHuDMAOk_odFEEASMlqSbnHs5v-kHPvnSn3CS_ZDYp-FZ83y550fmaEr0GAeAKzyUUHWtLn4p1xRL6HALHSVypaRVRIt9dw3A7_Ku_lJWtiUribKoTHgYa6uSykyqK41xLZb7vxikoCSf_xR9xRqJhy4Gk3U1_CaXOTMo8jdfhdRVU0_wbPGWYRd4VBXuTbHVYaRUQx-BkL2E8EqtY_si2LtccfagTsSpAIRROzrL7X6qMSiBIgH969V5bd8e8RglxAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: منتظرحمله‌این هفته فلورنتینو پرز برای نهایی کردن قرار داد مایکل اولیسه از بایرن مونیخ باشید. پرز قصد داره به هر قیمتی که شده فوق‌ستاره‌فرانسوی باواریایی‌ها رو جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22944" target="_blank">📅 18:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22943">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOwmPAMqjmz9fkgiyxkO7TLX8u4qjbH7xMCdNe-Fhi1K6t75DanDRtuhfxjcIQgTMVGIVmfvRPxcjQi-cpNEryuJFYFwzAlzB9Zp81moUBVSD7judf87y7VSscElTCeipk7Fq3wP_O5Xnk-cXx7Jq1QudXUqeNc83bzeWYaKV2yK6KrOTeWuVs2n3SKaIGa9EZNXyTKSe_fSHgpOv2AsXTHBctLsifZEzl2deAnFpZqE436E2OvyumuDFRtJ7_6IBdUIz_fGISqHRnqRo_6pwSApYO2gTU7vDKikrtxqZeHcc8NuhPxpmCiR8x4KpaMGtyBdxnu17_g7WArE4yVXYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22943" target="_blank">📅 18:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22942">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ebed3078.mp4?token=A0n-NJDIWGtSABq_4AXPCY8Foy88kpCgb1cNC02Xfg-zyeZaTgRAa9cLfV8eg_PqLunMulJQEYo7ubIA1wUj3FN1dfKBqM3A4vkZNn74ulj3mLo4aMZfuGw21DQc6keisUP7QsXUsqNL3NULad1tm7Az66MleAehRHNzH2-dkQxiWfA1SIfJoxJFq_PEW-UIZVUzMuPrcIu3Z8Vqu25RPm86rnLsQJIqu5Dr7uhEvrVHjM29x96L__8RUAdbQYhzILmzjKTIoNIHhHe0yfCv7P8JUrPZ0DS4bLoLpxEQ9zAcpW5SQHD1H_knXW42QS8xTVKIsw-BAmY5yYSWlQxtAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ebed3078.mp4?token=A0n-NJDIWGtSABq_4AXPCY8Foy88kpCgb1cNC02Xfg-zyeZaTgRAa9cLfV8eg_PqLunMulJQEYo7ubIA1wUj3FN1dfKBqM3A4vkZNn74ulj3mLo4aMZfuGw21DQc6keisUP7QsXUsqNL3NULad1tm7Az66MleAehRHNzH2-dkQxiWfA1SIfJoxJFq_PEW-UIZVUzMuPrcIu3Z8Vqu25RPm86rnLsQJIqu5Dr7uhEvrVHjM29x96L__8RUAdbQYhzILmzjKTIoNIHhHe0yfCv7P8JUrPZ0DS4bLoLpxEQ9zAcpW5SQHD1H_knXW42QS8xTVKIsw-BAmY5yYSWlQxtAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظاتی‌از مسابقه‌کاراته‌معلولین؛ این چه حرکتی بود تو زدی آخه؟ چرا از روی‌ویلچره انداختیش پایین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22942" target="_blank">📅 17:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22941">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBKe271TjaZ76VIf5dTQ-h-_Yjpb6tZYpdPA2W4qB3y1h7qrJr-9Q7YrpbrqrHK43-fyn6CF3vUii6JmX15k9iTJtwAhfBhDZvcdS39jt3X2N_mFcaBKMHxjdfkgLCe2oYoZFej9cEHEng52dkJHmsUiXlGkWCb9rB1nrXRC8XPqmSL5CHtCvLKp705CSWRa0tLaMe5U_nU0ZFRMaFYOgE9ChzZvw9Be5VZZicgKPjwqBH4qIq_ZtPJGiyicYWY9jSOYYUi4Yh72LupgF6lAxb7yfkvhrrn9Di2ojfqBn_l20o0I0ZQTUFADHFBDY3A4QHXdwLGfDSzohzOaA1H_Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22941" target="_blank">📅 17:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22940">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gr_uj8UPV3Axng-67rg0ZhhbAUCOCBZsvOrfAJx3xiitdSWiIKfSmKC3_r7onjwp9B7GPtKHEbPBQ0IfDjvPKuYGI05neBGcFZREIm49aNL70U41ZiwlUm1QwK2trduTr5geTxeMTN6hjykBgwIWcoLctaNmkCOcPA3epl55aJxHy34RZW5k7Z3SRCBhmpeDrpVczO_JnAmJliQ7jbHsp8tbRaLo4Sneb0Z1_fV4kgenmJZpVZ0dXoq1H1vpD6c3awKpE8Qj-tnwhY-pjP2qDoyQf7E6rJAe4hFuMVeootEkXRhSyBjTlRNaW9TWWrHwdMYE5xBh9E9VfU9ImiMFBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ مدیریت باشگاه استقلال به دراگان اسکوچیچ پیشنهادداده‌که تنها دستیاری ایرانی‌اش در فصل آینده سهراب بختیاری‌زاده باشد که درصورتیکه جنگ پیش آمد و اسکوچیچ مجبور به ترک ایران شد بختیاری زاده سکان هدایت تیم رو بر عهده بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22940" target="_blank">📅 17:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22939">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCOCvxRCkCrf237EP6fj_Km5KnyGQtVAf6qoevnwjzRucR9Y9zZ_-IIb16_hJYd5Uh8B9L9RjykasPtgJeGL2xdUiHvC8k74HSNO41ighmrn-1c6Hv279IkWUqiS5GoMYGx0xqG5Q5qdNRsjfBKZS_vqKRcZlyX5JNY3ieD7uYFLlPDCTeT0EeMSHKBsuWfvyAM_a4Vg59JA-_dXl-hSCPqbIZb8sVCUemgGKRr6I8bd0fSBbZ6Ymvx8DXIazLkSLKr3ikZvlSbXhB0wemUaPmceo-Pals-UPH6i8WvhlE3T1Y8WDV8LW9fyCzuHGZpWGo0fArImsmLCglvaHvHRAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌ های رسانه پرشیانا؛ باشگاه پرسپولیس در تلاشه که مجوز فعالیت افشین پیروانی در لیگ برتر رو از نهادهای ذیربط بگیره و در فصل جدید رقابت‌ها به نیمکت سرخپوشان برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22939" target="_blank">📅 17:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22938">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgSYUSGq_CKzmlvUWLXxWyEdQFyxOt89CzeKgU_N7j88GUk6Wo4-OxA93vGR-hYDi8SRbu5y8VyLsuk9IdI6601-zlBkDVV3bz2SXeTQPTgCEylfFdy-WGX5BqLUAovPnjwroqDLmfN41keFXCbU_sjvCmdwS1df7ySFlOLVdHusnsAD8frCHNZuq1Q_pxmxVqBOH2hd-zBBLFdCRkiEsLyUEAG6ai7Qw3wjXn5sSUS9sfW09utRHO5Gr-Pe2Fo47WosfskLQdkI5Yw3u3klb0lq6eYmLBBqmXeh9_r-61fG2E0w7yyW-MJVhjPdLz6mfkXfK1YfC9V7XTYsXXtj_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
تا این لحظه فلورنتینو پرز در شمارش آرا از انریکه ریکلمه جلوتره و به احتمال زیاد امشب او بار دیگر بمدت 4 سال رئیس‌باشگاه رئال مادرید خواهد شد و از مورینیو،کوناته و دامفریس رونمایی خواهد کرد و سپس روز سه شنبه آفر 150 میلیون یورویی خود را برای جذب مایکل اولیسه…</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22938" target="_blank">📅 17:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22937">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca0d90aad.mp4?token=q_9e8d6dLF-tYBAGP9xMgFy8aIjdhF-yB-1cZEOgpFq_q6FOMzoC04Vh8FrIWEQlfwPoPhw2dw6J_koPVXmVhIOxv7HhPpU4e6SjMY8hylIW2umJrYEPvbFyoXOJ8PRtA0e71jbgW4E8rFfOyD-Lg9c6Fukmoj4e96X9sMlRyqcwW4ZxH8TUDEBN7QG11k7FrWeP0hLrQ3FZdjIDT-FhbfqgJhw6M45LcD2S3b5KX8uWZUH_ZKutq3xXsT44Kg61zpGfpfJegOLtznhxhk1IgDU3ypeDDK0m_MQ1W4kHmihH5-8TwKhKEkBGUVAiwn5q6eF1q6L6qpT1ELGYZ60a7ZFx-Q6s-E4yfYbsLv41T2b1zUArr95c4BqzIZo9Bk4rWhApRzDreOhqSYsbGch70GKXe6vADqSQQYJKmbZozj3XyGmcDxoiYhdahYdETdr25IXTbG5k7mru2yDztXB-nc8en70LTWk5RE8lh74GU_IVQOSInAEvY1LCJ5JI32GHGkO-oY31Q16m4G2ppTST5PMx8wfevsRAGzmCiPU9hGNpStrb4MJJyABVd0Hq_qdciin7bWONEwQMSDvQguBwq47tTH10ylCfXSQZF9PGy0rq5g7mOIToXaHdDSLDs8tX2s2UmPbInKUN1pDcGltPPV_zTuzslWboJ9SQHaB5IHc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca0d90aad.mp4?token=q_9e8d6dLF-tYBAGP9xMgFy8aIjdhF-yB-1cZEOgpFq_q6FOMzoC04Vh8FrIWEQlfwPoPhw2dw6J_koPVXmVhIOxv7HhPpU4e6SjMY8hylIW2umJrYEPvbFyoXOJ8PRtA0e71jbgW4E8rFfOyD-Lg9c6Fukmoj4e96X9sMlRyqcwW4ZxH8TUDEBN7QG11k7FrWeP0hLrQ3FZdjIDT-FhbfqgJhw6M45LcD2S3b5KX8uWZUH_ZKutq3xXsT44Kg61zpGfpfJegOLtznhxhk1IgDU3ypeDDK0m_MQ1W4kHmihH5-8TwKhKEkBGUVAiwn5q6eF1q6L6qpT1ELGYZ60a7ZFx-Q6s-E4yfYbsLv41T2b1zUArr95c4BqzIZo9Bk4rWhApRzDreOhqSYsbGch70GKXe6vADqSQQYJKmbZozj3XyGmcDxoiYhdahYdETdr25IXTbG5k7mru2yDztXB-nc8en70LTWk5RE8lh74GU_IVQOSInAEvY1LCJ5JI32GHGkO-oY31Q16m4G2ppTST5PMx8wfevsRAGzmCiPU9hGNpStrb4MJJyABVd0Hq_qdciin7bWONEwQMSDvQguBwq47tTH10ylCfXSQZF9PGy0rq5g7mOIToXaHdDSLDs8tX2s2UmPbInKUN1pDcGltPPV_zTuzslWboJ9SQHaB5IHc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اجرا چالش فوق العاده سخت ورزشکار روسی توسط یک ورزشکار ایرانی با رکورد زنی روسی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22937" target="_blank">📅 16:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22936">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8gweAgS2Akwd9elV5dWkVovMu56VdwjQ5duzfaU4v5WdOSoW4hGBhDUi6R-28gE2sq5wMrRVk60JFLk15W4hj01CvVVLTkSf1Evrji8rxDnYp8sPabYklNiBRQiz_uilZ1CL-DHvr6Li8QnFSkK6ZX-XNxBTA7cxbdhB5LyLx4SCAUMFoTJ52WU15fWb5c0U1xtYGg4kqPkZC2mnp4nPWNg9hmNy69z2NxRG-IZbH5RJrG4uIzM8xvvaubQx7bOEDnKL5MTerft_ulYJfT4NJnqe1rRX-S1j3eZzXrPXVXN0vBI-WZTMC9j49vXZgWK4UEjXKXCTvMGnDm66ERqyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22936" target="_blank">📅 16:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22935">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzEYx9pnXAJeJ1gCM35GOkvACHrW9JqQdE9BPqr8UWuZWbpTh7LRbR6AgcQJk0cWTxuQSAs8bigSf5-IPCGXgfePrQRvsWVQ7C94LMfy-vn94Zb-hf7aWRXqFAfdbXA2jNl6YRxKQLcon3Kt1feeONXOg1E6A433EEGbolpkmpBgcrR3lAtuJKa52gInqbeThGIxz1hNc0e48DXEnnCPsDT8SF0vKBneedvLnMX0WDo79RMdRkcovsBxonceF8xnpaD0KuyQOwk2zE77wtR6aPn2-0jNCw9Z_oUT9-Olueev2K9AgZ__tAFlqMZZnKQOT95DpGLywLA4f648VPKVQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌انتقالات|گستون‌ایدول‌ خبرنگار آرژانتینی: با جرأت بگم که آلوارز درنهایت از اتلتیکومادرید جدا میشه. مقصد بعدی آلوارز صدرصدر بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22935" target="_blank">📅 16:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22934">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJlRYxhgmhrMIwcJlqXWLSfIdqK_33Kamor2i9tSmmDeyiowJx7pnHsQz_XaloFQV4a4S96-WEf3mNks9_W4oLIlrxzb_jcJNQN_XhA0VmRcv1y2ftD4IOAVaw5c6X0h6MJJ8Ao3KFvNk3GP1G8xUQvwY1ZjSAYNAQKxtdUmYY3A4Fs-y9ThEE18GmH-HEr6BWJ4NSmhFRrwjCZh9Fxp4XnA5EHD7lIKnrMqJ1IxclpgNNSvRqTaeJtmmH4F6uSYt9ZGmKjXEIS-3MMdNxly0nFDT6Wnwe_xQtl1QrXPJ6KF96I0AjTIHHRA5PpotKoOBZ7JtQ0j5a9gXb8OXddypA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
تا این لحظه فلورنتینو پرز در شمارش آرا از انریکه ریکلمه جلوتره و به احتمال زیاد امشب او بار دیگر بمدت 4 سال رئیس‌باشگاه رئال مادرید خواهد شد و از مورینیو،کوناته و دامفریس رونمایی خواهد کرد و سپس روز سه شنبه آفر 150 میلیون یورویی خود را برای جذب مایکل اولیسه…</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22934" target="_blank">📅 16:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22933">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139c25f87f.mp4?token=aU3NT2xQBACZMTT0hSSBqPcRXoMBi8QXslNDOXu5jaoOSvXsEjjMujM3HczZqv1qQ7BT0f_0tv3BDBkPDTU4Nn6fKI1ZAn4dUWpm2BGcw0xOWz1gk-BBhI_2R-ve-dgqekFOVW3ADtS_wku4SuuA5X9-MHiW0E2xWLysgPIvNycerXfCK0MDrOXIXhbEDL2-4OCEaFZduo7FpHLi9ZQ0L8dHcJDOP3jZdgW6FktTyyoi3qtQwSxLtVpqrS7Gmjd3deIJeAo7OSTFqFuwMTn7cTJdHdB9nnTF0ZCzSdZTBmlxL7LFP1Xie2wCOUbIrn5Iw_znJvy8kCjtXPL1YE_pFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139c25f87f.mp4?token=aU3NT2xQBACZMTT0hSSBqPcRXoMBi8QXslNDOXu5jaoOSvXsEjjMujM3HczZqv1qQ7BT0f_0tv3BDBkPDTU4Nn6fKI1ZAn4dUWpm2BGcw0xOWz1gk-BBhI_2R-ve-dgqekFOVW3ADtS_wku4SuuA5X9-MHiW0E2xWLysgPIvNycerXfCK0MDrOXIXhbEDL2-4OCEaFZduo7FpHLi9ZQ0L8dHcJDOP3jZdgW6FktTyyoi3qtQwSxLtVpqrS7Gmjd3deIJeAo7OSTFqFuwMTn7cTJdHdB9nnTF0ZCzSdZTBmlxL7LFP1Xie2wCOUbIrn5Iw_znJvy8kCjtXPL1YE_pFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
آدریانا اولیوارس مدل مکزیکیم رو بدنش عکس تک تک بازیکنای جام‌جهانی رو چسبوند و از دخترای مکزیکی دیگم خواست این چالشو انجام بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22933" target="_blank">📅 15:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22932">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRwmBTj1-vp6ozNIQvT18cRXJM3M9T76E5PoMk1iC8YUc7F9F3Bh-UINFCfA1VCSdK17QTuIpupEJ49hlqPoA3OOkvWX0U0ExIshaWHUdBDrCOfQOCOSNpvw5N89eyeCxHzPk07TsLW-jBOF6DhWnQ2wxfIeSmukPCuw4gpkTPD8_rcLigx3C9baVPD6AvZ6OUAXF5WSuQj3ZTNZ0k-lgBT38yjq1WdIcEujvkSwxooQ4o_l3tl1d4kwuhbs29VlVJkRXpXnuzFvrOueiMVZftIQhhQ_cNG4xSq2Xy3zj6BOEadpPXfPoJbYJCkL0n78sUBcVpdJ_ut1C6cNaTkFPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
انتخابات‌ریاست‌باشگاه رئال‌مادرید از دقایقی قبل شروع شده و تاپایان امشب هم مشخص خواهد شد ریاست کهکشانی‌ها به کی خواهد رسید. شانس فلورنتینو پرز بسیار بیشتر از انریکه خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22932" target="_blank">📅 15:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22931">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJpuRKqSAOcusZagbBFypMqjnvDkpkj4wBThO-n5MgDruGvRIwDCm7_szCMRFty00FzisGuP3nq4euJS7vHCurTSJsJL0-C9yL40aAw5x415E0uVINIuxW_9t8tLJSHbK2w0XwMKLXkrwLQUJ642G-evB3SVC1kayqqx1AMhkCSv4EynkE_pICDhSaDeo-uX5lgGMusnnZPMY8gjziV2OG8ECR7ARsQC-1j4GEp9XZe0kDdAt52VcCcKMMu3JWvD3rbOq6VUaIY-CWjw8iA09A59WL0SRyGnmkOe4oPZKoW7DME6E4vCuv8IFQZjkBBCJTL_dkUvqbBX2HhMTwYkHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال خطاب به‌تیم‌های خارجی که خواهان به‌خدمت‌گرفتن امیر محمد رزاقی نیا هافبک 19 ساله این باشگاه هستند: 3 میلیون یورو پرداخت کنید رضایت نامه این بازیکن رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22931" target="_blank">📅 15:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22930">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-9w5DFH1GIsp31nrfn-JGOiCfAT6ALKXAOalM90Bi9nEsN6_ImKlKNTJZLK9_XhfKs_giwQhJJzdorxGdHZ1wkRFGwGTIeBGiB20iKmNovfq5KjHl2PQ-Eq15qY-WPdcwNZWzmXEZAQhCXEyLvgLlt6w0OUhHhMyaVY3XKWy2i3_VwdpBANxfOukP3Hx7Hqge4ekztfFuSm6ydkdqaGbxgSOarydAlWAxJFkZ97KTNlLb5eoGOBX5m5-OW3KvV3go-uxrgr5eKoegekdS6XFqeM_Az3Nqbz0UX4Fdb7lKQPoKbCLyeuKGDDfuuGlVllVTW-LD6ikhGHT-rsEnoEDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
معرفی دو تیم بلژیک و مصر برای رقابت‌های جام جهانی؛ جفت تیم‌ها حریفان تیم قلعه نویین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22930" target="_blank">📅 14:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22929">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIVd3ajQpu_PT5DrmgIbZn62z8ggQcx7T2qFrD8Ij26xygqX7-Cyg3-jRjVB-9V7ADlDv7kZ4MYdb9PDcxvRgtPXZlYBpxH-ewl2oAKiaPQKNxJvoVGQQQP-R7GXifFNllBA2UrZbvsJeRJrfGRAFcgbP61LYn2stcAQTPjjhJcmUg0F6lBHYrJG-D9k50uehjbfapfQGgoblXx0rKrq3TYf9Vg-0S6Pbj7B5pNVDTEZk69wRO8dZvxJWndL62NMeDQD8AvArqhaHuwe2-JbynCztGcwd1G_3RnRaDMjvExKqijH-1vk-kCV3gw3ixQJpE8iZlhzL17NWD7flpxvXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22929" target="_blank">📅 14:23 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
