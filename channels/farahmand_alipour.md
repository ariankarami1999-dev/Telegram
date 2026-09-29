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
<img src="https://cdn4.telesco.pe/file/j34SWsMMNKefLB3l5HeGNx17rMvueVLzFfC3CwHbpjYKBRVpMEQZ0SV2iEn923mYO0SI3SHJjTfc61byDDq7FCFOpYKtLvqIXIPWMMnwh22GF9UuRTA7Hg9VpAjrePLkoEI44JY_X5hd9HmhwR1_UuFzF3HSxRu7SPBBlbLhNUR40h2dEKow6BDIb0Ytj00yWyGDkUGsWG0KjiySDoOSzfzTTjwcA8SgLSq-OU-djthPc_28knxUg0vkpRaig8QegXP7CtPm_YEqVL6MqeHzv6Jl381fp6xDT1Sy0exyPMucpSVgG4cmbFo_uPmdgB3lwy879aivTvSubp8ZX86SFw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.8K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 05:55:29</div>
<hr>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ol7lceJ1P8XC0E7DmUvWkV_mzPEFyQmV7Z19fI5vsLr_MJw90QP1Jm_ENhf1UBmOhYike1j5X0HnNcYJ91wy7LSR439p90zVdfnfO-STYedjHSaxRNW39CUbRspLcIjHTIDiz_oWuQPDid6JSdTUjA7jFY-CLX1TSI40lxEIPzBmhq2XEZB8vyE2x72d-Tfg7k-oar-Kp5QAipB6vKruzT-mPpnAhbJDqzfYSjvPg2nwhiQ8qtSTMETCtrx_YZAncPzMDE3gKYp17fIo401rqTWpCwwTw7iUl3Nqwjj1fO9OhwSKTMXSW6uymuWh69f1z7ycIIa8vnCg2EuuAJ9yvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/keG9GU51WSFWKKYGYmba9kWD6kxVcUAH1xNdzWh9cnvjA926Mo_rxff-1u320uY4Cu4v6KUK56JSAJXyo47lVNKoqJoYZsu-Q-SMjC8N4z2BTS83xzsg7icr9IzlsUyG7d6RFN-WPEqayzloPWN-h7aCFVA83M6ym_gN_T6VcsoeeeVJvFgZVwQxhSnM2xYsj2ABxzEK33AalFEGFNeoLUxUyruKPbnnYEgerJGVKEDVfPhXcpaNlDR132ZGpjn8GpLnoTsEJm2i1cH9wx4i7BYjubWbHKcXLVrIwtT1-cmDZrMEyYoj8p-4OhENtKaEsHE_wjfU0Cn48yYNpTN-pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tnagLuuyrnbRQOCQu0GP3QNYW_KFarKZg0RKh2nroarhOCpj7sz0uRQJH9TyFcV97g-TWbnEj81r1Ko-Yi_N27I4U5pGf95ptY7EbG8e4L_EEfWJIE-R7GVuglQh4qLy-qQrVEf_01ur4Dok4NJhY3ACmwVolDdMWNsN-6Y0G082HGtMgSN_W5bzTdbayXwaAWptySkNAY7T3EKdgd30XJONLRojgLrxMWnOVdJiXu-HCpJRosu2bMo0aeAz6o95VTuQkiiUp_jyvuEbhAYOvEX5emkYwNPbdFmjTSRCqt8jHGcP-iFfCSs5xbwtAhUda8Yr163c4RI2lR2EYrxdlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=Jh_URKdTKR2kEHtfpyZo6fCPk6fz-OM9Kt2BfmghqS1dHWH0ozaz4KoNVOcWU4zQtDjC_vdkXBKstUqyZsnKXt3A9IWuMQlK6qv9e6cUMbuQptoqEDHhCMfMPMXYH3OGRFWbyaq_hO5aODK-4d-bAg3gtZPL0UcxGGoXq3vWQAlkph8gXEGyIPezUHpRMNiIInKaK6WDK6e5b-Tjj6aroYacoQQOSNNrdkgxH08Q6GwSp0QFhpVkDWj-JAZ6u8Q3-duWZhDVuC4Ivllqjsu5IryOzqEvUfJwUGDAAkmIwcYkhL3A3qOq62gA_igSNb2mUQ_OfkJjRpR9EdC635WF6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=Jh_URKdTKR2kEHtfpyZo6fCPk6fz-OM9Kt2BfmghqS1dHWH0ozaz4KoNVOcWU4zQtDjC_vdkXBKstUqyZsnKXt3A9IWuMQlK6qv9e6cUMbuQptoqEDHhCMfMPMXYH3OGRFWbyaq_hO5aODK-4d-bAg3gtZPL0UcxGGoXq3vWQAlkph8gXEGyIPezUHpRMNiIInKaK6WDK6e5b-Tjj6aroYacoQQOSNNrdkgxH08Q6GwSp0QFhpVkDWj-JAZ6u8Q3-duWZhDVuC4Ivllqjsu5IryOzqEvUfJwUGDAAkmIwcYkhL3A3qOq62gA_igSNb2mUQ_OfkJjRpR9EdC635WF6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو سال پیش
حسن نصرالله، رهبر گروه تروریستی
حزب الله لبنان، برای چند هفته،
ویدئوهای تهدید آمیز می‌ساخت!
کج نگاه میکنه! انگشت میزنه روی میز!
رد میشه و…!
رسانه‌های جمهوری اسلامی هم جشن گرفته بودن که آقا اسرائیل «با یک ویدئو!!» بهم ریخت!
تا اینکه در روزی چون امروز
(۲۷ سپتامبر)  ارتش اسرائیل با احداث یک گودال ۳۰ متری (به اندازه یک ساختمان ۹ طبقه) در بیروت، به تهدیدها و ویدئوها  و گنده گویی‌ها پایان داد!
به همین سادگی! فقط چند ثانیه زمان برد!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=dD2L3piOWdltF_NX0ujYwHNyUMZgxfXWlobBV3QWdgKyTv2RDeNdI1IPKXunL3li4LynY1OJ3yjZrDMBBhW5b4n2ZvPLvaSb0bsfY_G5T2BDYk2ypyI43PdZjQvs3geMN0BkvUJrB6N5n_tE55g8GKhlLe7Hy8uxzkHaevnK4dpNsdh_c_iHgqQNIAN1P-jVdOkqxxTVfa71uc9lCUZnJds-JRoHeWydoqI-JHWoLJo7KAuToR1bnfQBsqNMHuV7PA14bAhboiJ9LpJd5yiD6y1V20WASunJezNfy8O7mOSRGl_Uq-wxRb4hIDYoeLTFUsVhGNzRLA_og1Kh_DZCXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=dD2L3piOWdltF_NX0ujYwHNyUMZgxfXWlobBV3QWdgKyTv2RDeNdI1IPKXunL3li4LynY1OJ3yjZrDMBBhW5b4n2ZvPLvaSb0bsfY_G5T2BDYk2ypyI43PdZjQvs3geMN0BkvUJrB6N5n_tE55g8GKhlLe7Hy8uxzkHaevnK4dpNsdh_c_iHgqQNIAN1P-jVdOkqxxTVfa71uc9lCUZnJds-JRoHeWydoqI-JHWoLJo7KAuToR1bnfQBsqNMHuV7PA14bAhboiJ9LpJd5yiD6y1V20WASunJezNfy8O7mOSRGl_Uq-wxRb4hIDYoeLTFUsVhGNzRLA_og1Kh_DZCXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1ZpdqpsBzE27rK5Z_5mJKT9IBaFpahsusZ_-0P24q3ZgKmErguuwwVSps6ytinY53g_hqwMVDONsCP4g1smpjBjH6kPGWNuTmXayUWkLM1IEm-Pbc6IDWmENnk8wDzdsDu0n8hcdX0JEph8wcbRT-1vxyGsey6hnath9Erxyf0VkimOK0HolzIGrUU-z7qt-OpNbOT2KlxzguXSyVLh9cMsEghp8wZXQ-JmwwRiWXYTlwVDc6ELWdOU_907l5bCMCFsQuOJ8gIhSFi-4IDM1Sq2XIc7ey_d8Aj2Awu8wNAhyNo0lOJBpfcQCAYKrUvkn1EteQl5cJK1lFjoQ90Tyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=DBcX6eiLcSubfNbxJlbb-NZrC_jW7o3We5xTcWm2QZPESdUDc4OfWsJ7l-pceitLAUBr_ghB4DRiE-wdP5fgIHpgXnnnzLKx5CLXzAnULYn2Hd3msf8SQLfFBNv-6bmNMFpFPMLmSOIRhT67g8tpQ-a5FEhdCqVtn0ZEKb937fwVGNnwKRPY2b17xInGaTcCf0YVibVt_dPvtlcLQTUsBZlXnQ2g49TfD7-zRs-Yd6euBl14_p3oEhG8YtIeywq90zMlBDBheN0hug1O25lj7s3NAuPk9C0S1mi-hHxjVeOEpPSYNmbkSTPdN8b9yjZiphlEhG8XNmbgSEJvwPUjqzaM7RfA0UTxaeac9K4ikwpuwXFc-Scrk8pRv86ruWeqhJn-Qbtn2vL7qsNJq_KbKAO0z4mm53LxarJpgmNYjUhUVn7DbXe5ANLLVICM_pSQc361-FinXXZUI8D-vYJFH_nJRImdg88FL-jlVKky2YhEf3bwSzH781QEUst7CkLTgdVu6WUaduQGtXtNzlLL5JOgBC8Zmp8_9J-f5jiCZD5B85JlI0Vf2DhujcoLDljHD_3PY7nqdUn3bJeDK9PfKdY4BgtJHLoGkcbBbU6yTD_ytGB1Dtg5yAI7l73jeUNvGQkP7sFsjvJgT2CVxvYyUuNBgpoxQOXK490CyyWV9Uk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=DBcX6eiLcSubfNbxJlbb-NZrC_jW7o3We5xTcWm2QZPESdUDc4OfWsJ7l-pceitLAUBr_ghB4DRiE-wdP5fgIHpgXnnnzLKx5CLXzAnULYn2Hd3msf8SQLfFBNv-6bmNMFpFPMLmSOIRhT67g8tpQ-a5FEhdCqVtn0ZEKb937fwVGNnwKRPY2b17xInGaTcCf0YVibVt_dPvtlcLQTUsBZlXnQ2g49TfD7-zRs-Yd6euBl14_p3oEhG8YtIeywq90zMlBDBheN0hug1O25lj7s3NAuPk9C0S1mi-hHxjVeOEpPSYNmbkSTPdN8b9yjZiphlEhG8XNmbgSEJvwPUjqzaM7RfA0UTxaeac9K4ikwpuwXFc-Scrk8pRv86ruWeqhJn-Qbtn2vL7qsNJq_KbKAO0z4mm53LxarJpgmNYjUhUVn7DbXe5ANLLVICM_pSQc361-FinXXZUI8D-vYJFH_nJRImdg88FL-jlVKky2YhEf3bwSzH781QEUst7CkLTgdVu6WUaduQGtXtNzlLL5JOgBC8Zmp8_9J-f5jiCZD5B85JlI0Vf2DhujcoLDljHD_3PY7nqdUn3bJeDK9PfKdY4BgtJHLoGkcbBbU6yTD_ytGB1Dtg5yAI7l73jeUNvGQkP7sFsjvJgT2CVxvYyUuNBgpoxQOXK490CyyWV9Uk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد
تا به دنیا فشار بیاره،
اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=GgKbsD5yTLeNEDEBMc4ZvkxCLQ9vAfKur7r2fK7geHIkkLIpxw5r2UOksD-nCNuYiDYQuDHWsotIm-wFOqxCr0mRARhtZGkCHS6wD8ecU2WLu7yWr7OWRcAOQixcYd1h4Wq9bv_iD8wU-y5Ap1oyElE-OcgUFWhXpLHWZNrai0fx-dftNYhyG1BIHK0rTqeDmJTLatiClN7d7s7hbOS9fCV84LvdzAOJHnBdzteFO2nJFIkiuO5Xqzz2gvxHJJ9KS61_vfjAzfcb1VutI0wnkWQFoYIl3tGdW8m1Nd2-KKSGAfwM3TdFtZP9G7BIT-IaFmDqY4WjlhsV_DuDUAhDVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=GgKbsD5yTLeNEDEBMc4ZvkxCLQ9vAfKur7r2fK7geHIkkLIpxw5r2UOksD-nCNuYiDYQuDHWsotIm-wFOqxCr0mRARhtZGkCHS6wD8ecU2WLu7yWr7OWRcAOQixcYd1h4Wq9bv_iD8wU-y5Ap1oyElE-OcgUFWhXpLHWZNrai0fx-dftNYhyG1BIHK0rTqeDmJTLatiClN7d7s7hbOS9fCV84LvdzAOJHnBdzteFO2nJFIkiuO5Xqzz2gvxHJJ9KS61_vfjAzfcb1VutI0wnkWQFoYIl3tGdW8m1Nd2-KKSGAfwM3TdFtZP9G7BIT-IaFmDqY4WjlhsV_DuDUAhDVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgCqLA_DdIPrnizY3P1iylZBLxJO721Xw8cVeA4V8w3CwZStumvXfQkYwdf43jgGZtJBsJS5XJ48BEd_7xeRdXGWRQBydXXCtFYZ-tAcWT-BtneYlSs3pc7FtNNtnycX-SswNQmQ0ZUTbm1Q0dKSVtWMGxVrtvDIulIP_9ZsSxW8VFxQx36uXvRLvuz_wmn77O-KTgwGgwzep9cSWmGQLvXeTA9nhq_8O-SCDOxfhML50T974xKV1R4Y1IdcgOUJ_BNTQHVBlod4XuV7THNdyBTIptZ-mgUKsqDeaMUCFY3oHnVjLlK4uHSfUZZrjTuCOOeSwWGayWpkVCSc0H1LJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=u8VWF0PVNgISfRNOJC-iyznPkxCBDf-mL89GP6uZMh0VP1RjaJRJm_p7zjd3xPFv7uDSRIcaM8Y7beOPtq8Nx_NR8WdplJerDIY27APcJBnfYRej5S2SIc0tf2gPZHw_32NVw9IzZsuhShqpIhmo2Chcwf-DmXWxdWD-tva7mnaeefRS9WB9mbnQXERdwM-3AU57BIArG0GOMqTYA2aA6qOMZgOKVemq-MVI5CWG_yF-yvn88Z2pJfYJJHg395KlerQhWya_hGN8Eq7ODTRoFict-9exzZqjVlqHlhW5BUgDv_S4K9iF_JglMoyuFnMmfr4PyCgWlvCFuG0y_0bVgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=u8VWF0PVNgISfRNOJC-iyznPkxCBDf-mL89GP6uZMh0VP1RjaJRJm_p7zjd3xPFv7uDSRIcaM8Y7beOPtq8Nx_NR8WdplJerDIY27APcJBnfYRej5S2SIc0tf2gPZHw_32NVw9IzZsuhShqpIhmo2Chcwf-DmXWxdWD-tva7mnaeefRS9WB9mbnQXERdwM-3AU57BIArG0GOMqTYA2aA6qOMZgOKVemq-MVI5CWG_yF-yvn88Z2pJfYJJHg395KlerQhWya_hGN8Eq7ODTRoFict-9exzZqjVlqHlhW5BUgDv_S4K9iF_JglMoyuFnMmfr4PyCgWlvCFuG0y_0bVgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو و این حرکت
یادآور داستان‌های عهد عتیق است!
شجاعت و جسارت فرزندان داوود!
که در عین جوانی و نحیف و خرد بودن،
مصمم و بی‌هراس،
مستقیم به چهره دشمنان خود می‌نگرند!
مثل داوود، نوجوانی ظریف و آواز خوان!
خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه زده بود، اما اسرائیلِ ۸۰ ساله، از این نهراسید!
یا از اینکه جمعیت ایران ۱۰ برابر اسرائیل است!
یا اینکه مساحت ایران ۷۵ برابر اسرائیل است!
در قطع سر حکومت جمهوری اسلامی تردید نکرد!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gcwe6u2j0vunHd4bFAIX-wyJKNNjg5HdIqfNxSdW4Jw4irGkjCz8ZpkHPO6YOJtHq6yWsiGPwNS6fFVEveIUkNUqG1jCLoTXOyQ4Sf_dbAxe2rxomn8hutqZYhrllc_FtvNsj6-w229exrZO37vU-4fBd9rIBCjE10Y_ULdUlaKXAB51cLN7s_DSHnuCGYa7DjXB2motv0qHjNLIHeU2Z7I95lW5JVIqqk9CoHDpMwYuiVOp3ZqnBurILqBLtxiVDBdZlQJ6LiplYwJdlwQOqMbPfntYwJlpCaoBWYMW033r3Y5im73x0fp8Dd-tqraJB8QivvrMWidR3gw57tyIZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADHJG8NxrpoivTOGon6hQ4vrLH8s1bJoREucEo_f2EXmpFI2Cu4E6cRzQAmm1E7o9seXS3_stPx9sSHrXQHIBdhyfS5QWLv69aV0sBLs0uEbphy3lXYpXZm9YQBHc63kRepZaOhmUtDSQuJgzy9qzZ3M_wfKOakdeU1mNG_TPvJlshGvF4IN9Yf_vXrAeGjRybENmhpyfyrH-RNLSO19qrCGa4k9dJs5paavvx6whDqvk4QLEz3hrUJ-Tu8f3kqkDSjd5XjEaDskFBNJnKjifY5oaiGxTgbYE2lRewjU9KGS6aneRHqDEnb0iwMEpf4dKjc0N3Ngh9Y85KelnLByAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود
که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.
.
این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،
و نقش میانجی‌گری این کشور.
(وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،
باز هم ترکیه این مسیر رو باز نگه داشت و گرچه  از انتقادها هم مصون نماند، اما کار خودش رو ادامه داد و سود بالایی هم برد)
🔴
با توجه به وضعیت افغانستان، پروازهای ایرانی به سمت شرق (چین و..) هم احتمالا ادامه داشته باشه
🔴
و از روی خزر پروازها به روسیه ادامه خواهد یافت.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=hiTLlYSx4LbU8qTKBqOPcO3lvHWIN_vFYhxfCFC6mnUfMH_6gQEhIDZqRnAUoNXJVGRM4UWldJkcm33LJ8ILPt4LUWZaB1hx7O8QDEIFMQXX6EALJG3nXcWqu2igcaQ1JtgaBmkZPpwUCGB33q5MRw_jIFwRh8Xc9p_LxXOVSJz-YxTHujtH4e7azgZycsS0XuTOr-jA7VEvcLpFu7cdEj_DzH1_CygrX6x05Eu-DQmgNqaLPIQ_34GaUNYcdEFc92DKB6hDVVwjyGm4LQnM5l0Q1wSilat4ou13qyl8aeP_9K9lQYPykpGLqpMU-ovqOIWl0gVtuuGpE_Yc6vLCHgVzG362BDVe0_z7TQDh9muALyK4XHv9kNU-dt7J18_phx-MYfQWeXm8H3xXd99q4Zk0NIGNQnOGMwVUVL63Qo7YrLjJ1BNzluC48SYlktKCLmRSaoMLUiibeQzJquCEqB6DZz9v2Mc2GGeERducdviDIlhmh9S1NHZu_PfRkEMJCGp4VJ6h7DL46GT1PRYF4_2vFUKLyuDScS-4rD-mpbU5SiMsLO9EQvAyy1-BL0_fGivTqfh2SAFgZRfI10JmAvE9tR069sy8lX8i-xkBlK5mFWo_PmXoHfAO4A8Bk_Da1RuVtpAk_a7bf3bXAx1Vl9TWvwLbS-uSCBHRQc30k0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=hiTLlYSx4LbU8qTKBqOPcO3lvHWIN_vFYhxfCFC6mnUfMH_6gQEhIDZqRnAUoNXJVGRM4UWldJkcm33LJ8ILPt4LUWZaB1hx7O8QDEIFMQXX6EALJG3nXcWqu2igcaQ1JtgaBmkZPpwUCGB33q5MRw_jIFwRh8Xc9p_LxXOVSJz-YxTHujtH4e7azgZycsS0XuTOr-jA7VEvcLpFu7cdEj_DzH1_CygrX6x05Eu-DQmgNqaLPIQ_34GaUNYcdEFc92DKB6hDVVwjyGm4LQnM5l0Q1wSilat4ou13qyl8aeP_9K9lQYPykpGLqpMU-ovqOIWl0gVtuuGpE_Yc6vLCHgVzG362BDVe0_z7TQDh9muALyK4XHv9kNU-dt7J18_phx-MYfQWeXm8H3xXd99q4Zk0NIGNQnOGMwVUVL63Qo7YrLjJ1BNzluC48SYlktKCLmRSaoMLUiibeQzJquCEqB6DZz9v2Mc2GGeERducdviDIlhmh9S1NHZu_PfRkEMJCGp4VJ6h7DL46GT1PRYF4_2vFUKLyuDScS-4rD-mpbU5SiMsLO9EQvAyy1-BL0_fGivTqfh2SAFgZRfI10JmAvE9tR069sy8lX8i-xkBlK5mFWo_PmXoHfAO4A8Bk_Da1RuVtpAk_a7bf3bXAx1Vl9TWvwLbS-uSCBHRQc30k0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4xQpLylnjD35tKHL0jOetLd6Tjl5tjEF8Fyg_IdwmNFNR83CmqNH-BVJM3JSSpbOB4bszn6LwGLBxXDW1FEfbfPCqKCqRzktoCkJFz50dDMoSjjqtT-ON4iDDOgCRJFRnNueqEnUvPntvGNjyNGtxTC0PzXhroz1BhLPEbt7TDy4wS7qNwlyLcdJP_jzVLovgmT95wm_7dLNyZIV9fTo_gt0OSVAbHe3XOglbdOnjW9lU_3lVrzYaiKhkT6jGBm-LF7Pm3GwMBrYliAgUSqgvMG4Gt_9kLzqB7oQwUCFeLIVWRMRcC7-E-mTXPb7i1mrSdNUItFxkB3NV2VFBnP4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qF3-g3e1agODtTDysxmphWsvsITNOdL4atCiy12UeIv_hV34ugftvssceTiWpCvKKQXjjDlYdH74oHrIWBvTBlrPAop7534aGfXaLwhGF64B5x_17j2pQkcXeu5InEZynBXTDG7OZYN5WHNfQ5HK5hYlNZU9q7w9z8zzGCTYpN5gmmeMz_4W0yNtdd9OHtZ6tq7_0ZwtvKLis2Ec4SqJ8-gW5yYSjqHCR_dwkFCZsXoqYOTdZwz_SJ1kN-sGf9WU7xlQwTdKcH-cJmNG49QAaRPRRijrx5C2DW_sKLdMDY91SRIyO1pQOJp-qnC5s7p51L-Bk2nqp2e3yrPL1_v6iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=kzoun5T-u3kaSAMvXuVzXPQkyAoqlPzTRh8A1hIpIUuZUrSFIGn5AvNoQvtSK8nCBV84uC_87DNJLjd-Wg1mcC5nIjy0r8Qi-Gyh421wIatTtU00xFMKn5fFuzj0JSAWvASmJ9eLckPogaEF25Pm8GUOMQUJgFtkVAn40yX3qRVQlpyrFAPViTuC7zlXda1b8GKRFLGfEKz8UdOZB5FCTcJMdO_2cYgltdU11otXJc7RQnzWfZy8-AhrF2fIJJYmLC-1gdq9fkRXNhekoQH30TFewHeJuOiyXiArYsPNhkbR-aN9VW5n4N9fzg-aoS_wjQQ9CdoZViw4LiR91HbxNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=kzoun5T-u3kaSAMvXuVzXPQkyAoqlPzTRh8A1hIpIUuZUrSFIGn5AvNoQvtSK8nCBV84uC_87DNJLjd-Wg1mcC5nIjy0r8Qi-Gyh421wIatTtU00xFMKn5fFuzj0JSAWvASmJ9eLckPogaEF25Pm8GUOMQUJgFtkVAn40yX3qRVQlpyrFAPViTuC7zlXda1b8GKRFLGfEKz8UdOZB5FCTcJMdO_2cYgltdU11otXJc7RQnzWfZy8-AhrF2fIJJYmLC-1gdq9fkRXNhekoQH30TFewHeJuOiyXiArYsPNhkbR-aN9VW5n4N9fzg-aoS_wjQQ9CdoZViw4LiR91HbxNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=ikQ_OkJ9ync0Zekc6xfM8JItjF5xMZuI8oaS0p3PG09Cjv6jGHayh1RdMyp0oz2cNFRXoUEdQNtCUfqK6BBFaF9WsqciuFq9CQxGm3F49z6xiY7bMlHZB3-C2XIL3WUfBZna5QOlJtUj7QykjAWeMSnyZKvffBjS6T9YgSazsDyA7fy18D01kjZNmI-QMM4Y_soPs7fuNaz1mWRp7Ym_3nR0WEtK7f4Fj82B17PqMjvigIdupusxSQRuZp6huVDXQr0B0V_L5Mu1zBCiHefOjv6MwNx08ZZjQQjNOWD_FoGVoueZ4ySocwLD1-lkn7-500s8m-suasFONQ8pKc2dNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=ikQ_OkJ9ync0Zekc6xfM8JItjF5xMZuI8oaS0p3PG09Cjv6jGHayh1RdMyp0oz2cNFRXoUEdQNtCUfqK6BBFaF9WsqciuFq9CQxGm3F49z6xiY7bMlHZB3-C2XIL3WUfBZna5QOlJtUj7QykjAWeMSnyZKvffBjS6T9YgSazsDyA7fy18D01kjZNmI-QMM4Y_soPs7fuNaz1mWRp7Ym_3nR0WEtK7f4Fj82B17PqMjvigIdupusxSQRuZp6huVDXQr0B0V_L5Mu1zBCiHefOjv6MwNx08ZZjQQjNOWD_FoGVoueZ4ySocwLD1-lkn7-500s8m-suasFONQ8pKc2dNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=DH4rTBYW8ssgKrobaSOmd-UMnU6gK8c8BoNjj5SzdUDMWBnQVYTjUDBCN-r9c27HSaHATKb1X3fP88v27FPxzPmTOcyGpliYE5qrCnXR9jjSuG2808GDcEOORLLBo-YN8-oCdpbz6pOmYUaphc6qIvM2zPvWixXC0tGuXuqzAagy_puqyRCInewBj6lqGAAuV3diHBQKWsjg9AmJMFXKuiSuI1iwYpP0gJkmLBwQZZg_EW9rg24ivoYq2-49-IuqVTw_Hqp8BUuEblwqY3lqOBP7LxLR-BslrTZ-V_ofzkQDUsk8zfR33wvEpk70kDgQpRLNhRbZr1C_ZmyN2L368g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=DH4rTBYW8ssgKrobaSOmd-UMnU6gK8c8BoNjj5SzdUDMWBnQVYTjUDBCN-r9c27HSaHATKb1X3fP88v27FPxzPmTOcyGpliYE5qrCnXR9jjSuG2808GDcEOORLLBo-YN8-oCdpbz6pOmYUaphc6qIvM2zPvWixXC0tGuXuqzAagy_puqyRCInewBj6lqGAAuV3diHBQKWsjg9AmJMFXKuiSuI1iwYpP0gJkmLBwQZZg_EW9rg24ivoYq2-49-IuqVTw_Hqp8BUuEblwqY3lqOBP7LxLR-BslrTZ-V_ofzkQDUsk8zfR33wvEpk70kDgQpRLNhRbZr1C_ZmyN2L368g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو :
«نصرالله، دو سال پیش هنوز در پناهگاهش نشسته بود. الان کجاست؟ با من تکرار کنید: پررررر!
و سنوار کجاست؟
پررررر!
و ضیف کجاست؟
پرررر!
و هنیه کجاست؟
پررررر!
و با خامنه‌ای چه کردیم؟
پرررر!
«سران ترور را یکی پس از دیگری هدف قرار دادیم.»</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpqUBTztxT_2wtV2JfElFXKVkWUJc3qhHXsqXTWNpdY9n_MQqfzqpeDyUeJHA0UzTPnXYDdMDyHO16vs7hTGZGdSF2dtxxqsamW6_vBlCzleYhU6T7oKxutE8dhiWl4DzPcRbtrbvnRgUoVaoM_qgd0Yf7vkZly4yK5dGaseocTGG-lv5UQR8Av9GwpPZ0VxPuaTtqFhWSyxjgy24F6BQlz47bcHjSAxQUZvUaRqk-9zCOeo0p6NaVLCL1Zvnaui-ekJa4N_m1UfBwzn4qoc3qYm6dPdoTjnBJTldfZgjm3KnLiW_bT-WFR5S5p0LLwSC_pVsujCL2aKYavXxJzUYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8FLKvXMpomh3IBFhz_gUyyZGo_l3QpFoh_BMZm7ZdXfwQcPtCbqp8DSWGZYZeeGAgxf0muW7NPahq21xVfJdvJBE7CbOgTiOXnt6dBGWXxP1k7eoYJEUh6aaXdeb9LKYMKdPX6r5b0pvJ3ZFK3ta2KtzLfESzM2bxqMmhrnvp8jHE41nnOkdMQF8RwmJvLeo1sclBwbdjNgOSEy_z1dFfPQUP9ur1ACDZsu0IdKJakispHqEnQCViEpUKljj95ezaxsdTXki2if_pSISE3F_vEVKZpGzzcXDD5oVvtS2-puxNYXgt1qtos8yUgKHspZUtjQdzKSEVMUGx7jSUHpYRws" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8FLKvXMpomh3IBFhz_gUyyZGo_l3QpFoh_BMZm7ZdXfwQcPtCbqp8DSWGZYZeeGAgxf0muW7NPahq21xVfJdvJBE7CbOgTiOXnt6dBGWXxP1k7eoYJEUh6aaXdeb9LKYMKdPX6r5b0pvJ3ZFK3ta2KtzLfESzM2bxqMmhrnvp8jHE41nnOkdMQF8RwmJvLeo1sclBwbdjNgOSEy_z1dFfPQUP9ur1ACDZsu0IdKJakispHqEnQCViEpUKljj95ezaxsdTXki2if_pSISE3F_vEVKZpGzzcXDD5oVvtS2-puxNYXgt1qtos8yUgKHspZUtjQdzKSEVMUGx7jSUHpYRws" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=qaI0XqLG8iDjJ77jNYEy3RBe_LM35onY-4mZEaDxBpFGw29x13sEDki6dmqFcg2LbEAjJzBZrmyQpHFLNybHuvtqkSduVFNV9AMXihxg9B7HNE4awd0adHLqgnncaHt_6vOb5_d5alXZjDriT-2aIKjsO86evmSJtlvcEe2dbMNX1xkIg9xYX6RiZsPyLao8PwdpVWqOQN-DIJ0Ue7rQ0yVOQt_m71JmoTS-VXk6xIfZo5GOVcSEZs8q5IOgl29xoeEAVZu1psH6H6ClI1TB5BU6bnzoagoe9zmZkThofd6O__58EEUOz-ygcliRkMNxLysfId4_lPN20blcmaizJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=qaI0XqLG8iDjJ77jNYEy3RBe_LM35onY-4mZEaDxBpFGw29x13sEDki6dmqFcg2LbEAjJzBZrmyQpHFLNybHuvtqkSduVFNV9AMXihxg9B7HNE4awd0adHLqgnncaHt_6vOb5_d5alXZjDriT-2aIKjsO86evmSJtlvcEe2dbMNX1xkIg9xYX6RiZsPyLao8PwdpVWqOQN-DIJ0Ue7rQ0yVOQt_m71JmoTS-VXk6xIfZo5GOVcSEZs8q5IOgl29xoeEAVZu1psH6H6ClI1TB5BU6bnzoagoe9zmZkThofd6O__58EEUOz-ygcliRkMNxLysfId4_lPN20blcmaizJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhK-qjM1foJm6BUOGGjv9CtABssDu3ITw4xUx7havI1s6F0__nuh46d_lGqGNX6sLYr61C5HMjf4mRN7zGADNwL7X7dJtYtRmXULgDeYNecI6Foyw1ZEPci-xg-5sZjqPpqlPvtqrfixLQdUqzy6Gisdmz9Q9nUG0IgSqQacTMDY6js1J6mwMgKjL87RtCtqlCK8McAVsDgnoZ41D6eabS267YNcDo2C8uLVvas5sY3bksNs1IL8NNNPmmOdoC0WP0VXCIzW_cR_gOB35hwhXmaBKEugwMOO2eLy8uhMa-bOIBdieC5NwbZmK0tpwSrxf6eR3Z5hSb1ZCw5Rd1WG-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=cWVZavutX8dVxpNx0etnPhGPgQRcd1ul4wKdwP2qGoBr8ZYJ0WWjFIDZijWFuFUsDX7HuDenwo9QBeAwRoK7BwUI7FhxuK3tI7zCfWtRC8mtk9-GZpSzL1eAKThgsainl7_lO7w_0cc-i_bJnOFXh-lRzw9jd0Q1zXPwCiK8xRwioqu1yb6RfqpGSoXCA8uGIX8790oO2MZSgH3IVpWTAXiDIdqay2DF9Gd-ZN8asfHUVKb1KaHHeVri8B1tQcbtf5V1N7DFA-31wUBrCbo6En42SyPpzDcp455bImHW1RLOKUNLur0iJECVYWSHDR11-TVEwdZy3dPPjWpGOTgMEL5DYIyURGGpgiFrkFiXH0T6HswXSvB9aCOywThEUlwMCL_tBKZ384jpb9F-cfEcrzppWZpxJL9CNyHlIhVVJFUE4dIOE9k61z3FKNRZEvflpuhLycXxcdOQP0SnYFXd3Z3a9xolqWZ_w9n9YlRqi1zMzc9voYMFt1j8e-n07BeFaMz4psu5zuwZDNs3RbSDhNCGTvqjtMbsKsWMoBApFxBMqDJa1KeYsIfj0UTR1X-D9lrHySTbeG43gbatWAnII7BfaPOFLZ5CHAdCt-4zT2yu_e34sMiLf5Eu2rkNnIvud9s4m2JqVohkHrIAKS-lLIvFLLjDNonUI-iJdcrr_fI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=cWVZavutX8dVxpNx0etnPhGPgQRcd1ul4wKdwP2qGoBr8ZYJ0WWjFIDZijWFuFUsDX7HuDenwo9QBeAwRoK7BwUI7FhxuK3tI7zCfWtRC8mtk9-GZpSzL1eAKThgsainl7_lO7w_0cc-i_bJnOFXh-lRzw9jd0Q1zXPwCiK8xRwioqu1yb6RfqpGSoXCA8uGIX8790oO2MZSgH3IVpWTAXiDIdqay2DF9Gd-ZN8asfHUVKb1KaHHeVri8B1tQcbtf5V1N7DFA-31wUBrCbo6En42SyPpzDcp455bImHW1RLOKUNLur0iJECVYWSHDR11-TVEwdZy3dPPjWpGOTgMEL5DYIyURGGpgiFrkFiXH0T6HswXSvB9aCOywThEUlwMCL_tBKZ384jpb9F-cfEcrzppWZpxJL9CNyHlIhVVJFUE4dIOE9k61z3FKNRZEvflpuhLycXxcdOQP0SnYFXd3Z3a9xolqWZ_w9n9YlRqi1zMzc9voYMFt1j8e-n07BeFaMz4psu5zuwZDNs3RbSDhNCGTvqjtMbsKsWMoBApFxBMqDJa1KeYsIfj0UTR1X-D9lrHySTbeG43gbatWAnII7BfaPOFLZ5CHAdCt-4zT2yu_e34sMiLf5Eu2rkNnIvud9s4m2JqVohkHrIAKS-lLIvFLLjDNonUI-iJdcrr_fI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nf7nS0JtC9yQliSLnKZk9wQNwiKzIYI8OJGKuVYTLCTeac8vvcx2ACRvtF68nuwwy5Thqj0qUTk-ZTgd64te8EYR-tPkC7JUsKnhIY73dJWLD7XLUFPY9eAGN43T-VvYMH1wArLN38o5aNcBz1fSIZtYE5k5HBRMlM-EkqFaNnBidb7myIIz3z8nBHpqn6GlymnTq1BdA0FRNOw_eA7XJBT1jOEdedjrXs_L6hPAX7HQMnPi6fa8T-eqbFfU25FtD9jpwRyVUuhk0sHTAqNNsBLhRvDgqoF_QuVVMFM9eGEun9OPZLwTjAJAFxoxolh4q33z7SAkUph16IM3RzPRAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی این روزها
برای عروسی در یمن شیرینی میدن،
۳ سال پیش برای عروسی
در غزه شیرینی میدادن،
پارسال برای جنوب لبنان!
عروسی‌هاتون و پیروزی‌هاتون پی در پی
✌🏼
۲ میلیون اهالی غزه سه ساله زیر چادر هستن
۶۰۰ هزار شیعه لبنانی ۵ ماهه
توی توالت‌ها و گاراژهای محله‌های مسیحی و سنی پناه گرفتن!  پیروزی‌هاتون پر تکرار!</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=N_mja22lRD0w68C2ziX5T0YO_B7YJe1bTzaYCrQbkbHI-6e8Ak347pq9TLtujTgTW5-Vh2S1kDPN24GHBcp-KlQisP2j9Zz4gRuF11OP2y45Xtbnkhl2UrKxJEukd0gOu4r1MWFafEZJ8k4XmyaUMSe0coZQcg2bHIp2VP9OQK428eRc5yxvDyDv7aXmul_hF884UxUaDr-gY5ElSPVe7RXAFxefV-cEHEYMI9dRvVEmhQ46eKlp3QQ_pOU_V8yE6Z-5ZT1tayMXqGzF3FwTEtazCX03yCv4-7g0bptdKcBot0bNdzG_e2lW6CHP2ec-f2OzQ3xCSm4HJvnCb9ndeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=N_mja22lRD0w68C2ziX5T0YO_B7YJe1bTzaYCrQbkbHI-6e8Ak347pq9TLtujTgTW5-Vh2S1kDPN24GHBcp-KlQisP2j9Zz4gRuF11OP2y45Xtbnkhl2UrKxJEukd0gOu4r1MWFafEZJ8k4XmyaUMSe0coZQcg2bHIp2VP9OQK428eRc5yxvDyDv7aXmul_hF884UxUaDr-gY5ElSPVe7RXAFxefV-cEHEYMI9dRvVEmhQ46eKlp3QQ_pOU_V8yE6Z-5ZT1tayMXqGzF3FwTEtazCX03yCv4-7g0bptdKcBot0bNdzG_e2lW6CHP2ec-f2OzQ3xCSm4HJvnCb9ndeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUjnYYroSj25gBzC3H83Bb3PQmqhNXekpeY3yGWizkQKgZjJ63-PFkhXijh6dT3wxq1SI1mY-hx6lz9ZJ3tjRKRFrOBsaOSA-1c4QaprUWrEukX4i6PyKTJWX9evSJ6Ac85BjwI3Q-tr8JI17FmJo2NEn1nf_0U7G8DSogNKd5hD3CfURU4uW9TpN-7o515NEWMMi5ExRabJ71HIAo2IHVS5M9asPvQOh5UoIsVzfFbhzbKwR4rclMiL73IZ58BpXJ1AwB6qyD5I8_yQ8nahOFKjlPJyQiL-OfweyrnBfbvoiJQImjh-iQUwDJ8R6vtpk5R_vKgeJ0Y-6QqInlbTkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-h9AxIIg-rz-vzM1jPLAIr8_XUPaHX3OiaIVDT4P9M_B_PV0ZaG3qJkyp3EpBY7JiBQ-Sv082vRhckLU_w3ZIwKFW6VqzZ6FMPvl5lVCvFY938BdmKBZnZLONnK4t_VhklRu8pDjotnaygiI07aCQq1NQlAv3DJTWBGPpqWlR5aaGfCgi7leT2mVkOTlcUigsfDacXDSwqnX7Ruoh-WMN4P4Zx-VMyB-_M1qw91UOZSxpuHwCXMIhoaaXPxqq9Fdcy7_7M2fKl9-1xvsuYyGsaE4tfQfwkLQ39AhmzdxSsFHrHwTE2TaEWF7bbzQiFtKshkqnApAxQ6ybKvrqgbBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUKo80Fltrk5zG-sfJL7DQ0aFDEGIs72Fny4_fpoegK0VyW2StHCjrQvBhXzUNo09da78iekY0rmyOTSklQm1FEJpj81Br42GLpfN5tvO9T7I9OqoYWnY5EEiBrCR9HBd-9bO1NUDodWSB_9_kJxK2aL7Hs_hQWMB7Wga0szgu37dpRBWb26Nn2xrhrU0pwj2JuwF1Fu7Dn2PzBCmQU90rSHsDx9cC6XeutkVtfDotrL4V_RBg4EwrRaw6YW205LVpYf4lerqvcSKb0p7QZX7q-TWu-MSVb1SpWOOqwyEmh6_VEaRb2ZA-8aApeeUgoRcpk55HN5jyqU3KZ6yotPpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=Lru8DlRece44wutcGsbbLu23h_GKxQ3iA43COsFlgIoiycnpLcAvvQ9F0awNPU8KJ7yAgum6TTRIVMfgOhj3wpZBCkvRWgt3aWS-QL0k9Ld4CItVAm5JUJnLLmnpnNiQHc_VuOEi3exEVbOO9IqVt24_Ozl7RQYtrCJ251uI2MggL2065ijMLYppZ36xRjL_nQdibe7SDvHBgbiGrEHAJzhwBJ4FW6J1gq2wHC1d-HfjcvBdkY56qFuvOMyPIbl2zyLKlgklfNGtdLCFN4buXtf4JOZzkJ37J1K9oBMnd6N61QVPx_BxGclcA9X1pediNWjyyA7yy2fNXryf1WU4KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=Lru8DlRece44wutcGsbbLu23h_GKxQ3iA43COsFlgIoiycnpLcAvvQ9F0awNPU8KJ7yAgum6TTRIVMfgOhj3wpZBCkvRWgt3aWS-QL0k9Ld4CItVAm5JUJnLLmnpnNiQHc_VuOEi3exEVbOO9IqVt24_Ozl7RQYtrCJ251uI2MggL2065ijMLYppZ36xRjL_nQdibe7SDvHBgbiGrEHAJzhwBJ4FW6J1gq2wHC1d-HfjcvBdkY56qFuvOMyPIbl2zyLKlgklfNGtdLCFN4buXtf4JOZzkJ37J1K9oBMnd6N61QVPx_BxGclcA9X1pediNWjyyA7yy2fNXryf1WU4KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Id74eKtcp8iBHSXORzc3k5X3yqD__0Wp-9NxuKElRYUiEGVByYSv7IJ8cn_jfpB8teCenkCpj_vMXg06j-_S_Zbu_uMflPpyG_c9Gi6ZT4c9NfhwFb-X9iCIYc_BPQIw3WI1NWsAPAEKLjPFApYW2IxCzBCiHa3INvOUzAxcnlubidEoF9_pkzLLvftFmDlrX48ibBGTGuBNV3pAr97a_Vw7gOQhC25N5w3chHOrewgf3tDiBi_jrjdAJquxZj7ylwQ50KltrnylPxGcTnu2rrC0jtiHsBGmb2n4gbRzIn5fgoxKQVe5QxBgvi8R9QV-EETYIHIgHFB_TXdGLFz-yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu0ZRUI-V06tEjshIM7jQmYwReQ8umvTci6kf_6DPvqPXso-k6lgs7NCb1L7jiSPmF-muACr5fmkffvKvoXSEpEqtPJMNNXPfHeC-4P0pMFyK8cZzH0EUaA98Yy_1NSB9xPKQAPxXGP5tgLttsKsCRLIDOJFxDlR_u0NPE2w_GsjpHVCsB4UqSz7NobKaO-aIpA4MupWcY1B2B_Ato0svskuLqnSKd3JsrKGmNtz7OcOK98yRy1yfFUz6Hs_khufq0OeVASS-SRAWoqQiX69B_m-k1UoY5vrYVgQu1tQSSVG3rJi7jgr8sRKpm3Td5-cTpm2MCcln-OFqh-lU58g7Va4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu0ZRUI-V06tEjshIM7jQmYwReQ8umvTci6kf_6DPvqPXso-k6lgs7NCb1L7jiSPmF-muACr5fmkffvKvoXSEpEqtPJMNNXPfHeC-4P0pMFyK8cZzH0EUaA98Yy_1NSB9xPKQAPxXGP5tgLttsKsCRLIDOJFxDlR_u0NPE2w_GsjpHVCsB4UqSz7NobKaO-aIpA4MupWcY1B2B_Ato0svskuLqnSKd3JsrKGmNtz7OcOK98yRy1yfFUz6Hs_khufq0OeVASS-SRAWoqQiX69B_m-k1UoY5vrYVgQu1tQSSVG3rJi7jgr8sRKpm3Td5-cTpm2MCcln-OFqh-lU58g7Va4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=QJaFssWXWZtsKu8SvmPas63Jl-4Vm6QZN-EQKyB1VGjoZQAsbGDZW2OGfv7NSNP1JA8Ex4t2rlbSc7mLCcU_ihL1XtFDk_2kY1DxUIQ6k1VE4HOrA1TLFYplpQcyutyO5DeWwGisnIUuID7wLV-DW3wyG6EuNLsJ7wzls7DNMwMPv6TAnP6V4n1Mjo3aHO1o8gbjb5dHz2K8oNoxZQN6osZYbSRgTdvpj6jiYYGy5fTxeRnzVWDN0EQdSwafwv6Iymf3xX5JbP-fOp2XyQvI_VYzy4b8rDe493ijj2Wx23fOdSbB2qTHKMh9eEV0Z1KH0239gTgFoZWlcaeIvKwmCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=QJaFssWXWZtsKu8SvmPas63Jl-4Vm6QZN-EQKyB1VGjoZQAsbGDZW2OGfv7NSNP1JA8Ex4t2rlbSc7mLCcU_ihL1XtFDk_2kY1DxUIQ6k1VE4HOrA1TLFYplpQcyutyO5DeWwGisnIUuID7wLV-DW3wyG6EuNLsJ7wzls7DNMwMPv6TAnP6V4n1Mjo3aHO1o8gbjb5dHz2K8oNoxZQN6osZYbSRgTdvpj6jiYYGy5fTxeRnzVWDN0EQdSwafwv6Iymf3xX5JbP-fOp2XyQvI_VYzy4b8rDe493ijj2Wx23fOdSbB2qTHKMh9eEV0Z1KH0239gTgFoZWlcaeIvKwmCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=GeOh_j9xi0_LBcrhtzXoFys857UK8Sazy-hbdI3lzadvJVYRhYAbkDmxPim2_WWk-_vKdM0aV4c1Ib9BnNoV27mS02DXcE2sKr4Hd6EOO6RgpmCIeE82Xeo0XIobBnH-JBTp3qskXFkLnrlDJwGMg0rk0JSG5BRVHlw0s7nGnnoMbKNpvgskCAiHCyurFH1pvLQbvbhPLMh4dL4M1K0ZKQQgXp2xNZXJGJW76RTSxmZWqRWU2nc4FwJJiGTApf0NfWmw2Kl1hV33SmdTjnLPGQ6K1w0SIyfhbbVJAyj5OVHA2RJiGJPLBo8ka_U-ddtVU3sBiRa8VMybH6J8oegfjYW4pUWuqUHWc2NbFq9zcryGBFcNWWVHuvljooFa-4eR5VkQdVtDEpjvLBT82-yx3_GaIR1ruG8HCKl0ZWULP-JI1u-AitnX7Vs1ul45FA-5MLpSyRBRs8qRb05FirlhW6bTVaRmw4SZ53FkfJ-pCEjNSbc_n98I6lvR7S-M4TR_qTssnNYUIOqTnn26XJwLNR49Pzc4bFwiRv4ro9EWyflpA937Nb5sxJfj7RkZpCzSdCWTTe_2rp037pnOLX2EmGe2Ce4djaVKH0WPXzWVOadY_487wBIoY8xeSnL7BbaDLpJ-Zc_uAZLmYPUFFwYRdgn4hS3iGRhetxjqjC62Z2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=GeOh_j9xi0_LBcrhtzXoFys857UK8Sazy-hbdI3lzadvJVYRhYAbkDmxPim2_WWk-_vKdM0aV4c1Ib9BnNoV27mS02DXcE2sKr4Hd6EOO6RgpmCIeE82Xeo0XIobBnH-JBTp3qskXFkLnrlDJwGMg0rk0JSG5BRVHlw0s7nGnnoMbKNpvgskCAiHCyurFH1pvLQbvbhPLMh4dL4M1K0ZKQQgXp2xNZXJGJW76RTSxmZWqRWU2nc4FwJJiGTApf0NfWmw2Kl1hV33SmdTjnLPGQ6K1w0SIyfhbbVJAyj5OVHA2RJiGJPLBo8ka_U-ddtVU3sBiRa8VMybH6J8oegfjYW4pUWuqUHWc2NbFq9zcryGBFcNWWVHuvljooFa-4eR5VkQdVtDEpjvLBT82-yx3_GaIR1ruG8HCKl0ZWULP-JI1u-AitnX7Vs1ul45FA-5MLpSyRBRs8qRb05FirlhW6bTVaRmw4SZ53FkfJ-pCEjNSbc_n98I6lvR7S-M4TR_qTssnNYUIOqTnn26XJwLNR49Pzc4bFwiRv4ro9EWyflpA937Nb5sxJfj7RkZpCzSdCWTTe_2rp037pnOLX2EmGe2Ce4djaVKH0WPXzWVOadY_487wBIoY8xeSnL7BbaDLpJ-Zc_uAZLmYPUFFwYRdgn4hS3iGRhetxjqjC62Z2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=sQNuSYAtRCiTto6dLN9rYknEIWzapxsh4xmZgfdoqNe_M-gYGiZioc_LS9BnBwofLCGcxOiGaQ1ZjYq5cAedHObJ6KvwZHrYuQy9bgmiWxQGnJGJYSP_ivfcamnFK9ZIibW3Lsln9YPwB1N3bn89KXlCIMuu5tNbhko-fndUR9AXq-DZvwN40aIq4rKY5omCUTPZFu4nq5KiE4HgjMAV36jfjTj6XjnGP4ipGkxQULKnoKsmNMJEA7g1M0uWCH_5ifs7I6yUnbCrxrQwfN1gS9KLDeOvYejHUmiCo90sI1RBTn9ZaBudEvp20SUxAgb7bJVePWhxolWqPVfpw14H5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=sQNuSYAtRCiTto6dLN9rYknEIWzapxsh4xmZgfdoqNe_M-gYGiZioc_LS9BnBwofLCGcxOiGaQ1ZjYq5cAedHObJ6KvwZHrYuQy9bgmiWxQGnJGJYSP_ivfcamnFK9ZIibW3Lsln9YPwB1N3bn89KXlCIMuu5tNbhko-fndUR9AXq-DZvwN40aIq4rKY5omCUTPZFu4nq5KiE4HgjMAV36jfjTj6XjnGP4ipGkxQULKnoKsmNMJEA7g1M0uWCH_5ifs7I6yUnbCrxrQwfN1gS9KLDeOvYejHUmiCo90sI1RBTn9ZaBudEvp20SUxAgb7bJVePWhxolWqPVfpw14H5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDrPLQ1kFmJ3Nchxn1pX2d-acn65GfTDyZLNcHZ4aS4qHBNlER9-JYjn23nS_kbPtJPEDXG4jh_ydYwmXfNirtEP6e9XdqgCOdgULt5sd2xyF2c_RSPG5XyMEBogktOAS9tv4r5-2LDMaEFzP8F9SfcYxvPKYfH9YzmrdlWW9b7AmZXeCOQMX7-ymYxgNDFGUPaKlLx7ueH9QHM8UZlSO9Uykl_U_ZtWgD2vs1-FqSWyXj2VNnImZGzyW3muZx268Vb-y5sC6cdjGgr1VBpU4sMezFQhQX2tN-NV-Cdf_Yr1gYbTmIwz8o2ubUK7Gl82MOEk7-ctWjvKjOfHDO1HTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=jqG1iovdxUiHiO67QuOMhXuqm8LcyGnsaPeFn2_9aF4b5Y68GWMrOlHIr_iEH17nhNkoaovDNrbhmoVcrXU_Ydgsp3fTEHlSZvE1q6iMNeHcbXAuXv_X-00HWJ-15sX6UTutphN3POUlhzvyBrrgjgw8aL-YVJmFU6r7H5kwRNNkDJoVj9RXYtXUElEdKI6SHCFIeA0uRbw-CE98qNab5bm86dOG1DuIF9mmg6VjDZ5C2aloUKGDYQxrUtroayps5-4A3uDH3uXxat0l1oSpcIagGqpf8S0ImJ_2pI4lEeFs6mLOS-Un3pxzglXBxtQCZ7rq0OgtMwnwgFZv1TirWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=jqG1iovdxUiHiO67QuOMhXuqm8LcyGnsaPeFn2_9aF4b5Y68GWMrOlHIr_iEH17nhNkoaovDNrbhmoVcrXU_Ydgsp3fTEHlSZvE1q6iMNeHcbXAuXv_X-00HWJ-15sX6UTutphN3POUlhzvyBrrgjgw8aL-YVJmFU6r7H5kwRNNkDJoVj9RXYtXUElEdKI6SHCFIeA0uRbw-CE98qNab5bm86dOG1DuIF9mmg6VjDZ5C2aloUKGDYQxrUtroayps5-4A3uDH3uXxat0l1oSpcIagGqpf8S0ImJ_2pI4lEeFs6mLOS-Un3pxzglXBxtQCZ7rq0OgtMwnwgFZv1TirWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=J4XP_wFtytb4BoCHYFupstk_LzcWkk0QOkp-PGWtxWSTWo5miGBLo7gLrZD-kzYFLxnLNNQ1vvWqQ1B4SAe9QG_YjmNyfpnLIGYVXOo8vzml9mAg05sq4loNUiEBjEIz00DFqCPmOZQFbwtfFyXtlVPJ6fLtM6BmqJaXTqta-119ux5hy5hFYWb65j6M8leYSnkK3_g3yfyDxYETn08b3SRvVxj_EG51B9S92ulcwLaUnTTpRoRLC2SNZzydAPaBh3qFi5dJXxBcuqpbiYEKKmjilsTTwFg8o_N4mk35cH0Q8-At4VcsBsz7WANa8_KLOFGn8do51X02DZcbTQVRtVx6937l4esqws2FB_uMI2DY9vdrn-lCeGdKubmIyZY4NO571XkfMXw4_LdBVjqP8F-YWzMKWp9VbcyM7i1ZMgClaxI695VRHaKtNTlXRZbR926HorKbxVFi-1i5zTFqfqVSukmnWGOoQPHpTMAA1vxohL_ijUoGpz6iXVkNAycpL8KUPmnlafRMBAH9fTDn_9zeAsMXn0mAHCumwcueNNm2a3zO07hdv7kexY85Ntgtct8Ng69eMrFQZVG1fWDuoTt_9GVfxnSebmBIg_bPDwDW4KfmrKzZ2VGUUK4QESyM16c8tCjz_yH5cQduH4Of1doz_GV_47s0kuPaeXB5Pqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=J4XP_wFtytb4BoCHYFupstk_LzcWkk0QOkp-PGWtxWSTWo5miGBLo7gLrZD-kzYFLxnLNNQ1vvWqQ1B4SAe9QG_YjmNyfpnLIGYVXOo8vzml9mAg05sq4loNUiEBjEIz00DFqCPmOZQFbwtfFyXtlVPJ6fLtM6BmqJaXTqta-119ux5hy5hFYWb65j6M8leYSnkK3_g3yfyDxYETn08b3SRvVxj_EG51B9S92ulcwLaUnTTpRoRLC2SNZzydAPaBh3qFi5dJXxBcuqpbiYEKKmjilsTTwFg8o_N4mk35cH0Q8-At4VcsBsz7WANa8_KLOFGn8do51X02DZcbTQVRtVx6937l4esqws2FB_uMI2DY9vdrn-lCeGdKubmIyZY4NO571XkfMXw4_LdBVjqP8F-YWzMKWp9VbcyM7i1ZMgClaxI695VRHaKtNTlXRZbR926HorKbxVFi-1i5zTFqfqVSukmnWGOoQPHpTMAA1vxohL_ijUoGpz6iXVkNAycpL8KUPmnlafRMBAH9fTDn_9zeAsMXn0mAHCumwcueNNm2a3zO07hdv7kexY85Ntgtct8Ng69eMrFQZVG1fWDuoTt_9GVfxnSebmBIg_bPDwDW4KfmrKzZ2VGUUK4QESyM16c8tCjz_yH5cQduH4Of1doz_GV_47s0kuPaeXB5Pqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCI95HQffbj2xN8TzZM01qmvr2-D9_uGbnxWcyRIzKmbeoK3RIOLKZ3npgMLT5wlII-2863BVebcL55RjW8viAG6WbYCkGjLGrNalcW6VArWonKsDrfVqeFgWyR7P8Q-2MY71Xg5K9Hhed0ePBlkyiJZU3RYaSnTaox95T13T0KCw-DluQecNtBUp7eLQD7RvMPvabY6QZlPWFvOr9N5su_G7YjUVctrUdA1Cc_XtDK1wFQXJBy081q7E3BC0gGqFst8TivKuefTeyXy97_V0RDqkIUKvmuUBThBnwC_a5YGtmrZRdNcXhTyRWDZSKBqqQGMMToZVT9_V2FWO0OK5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=HlyqUrl6aHprXX5XQI3CZF5fkvTqzLCEwrHYDOuk_osdgORge7UFy_fQAicHBppROyMPtcRhX0JBUP03_9BxNVBMOLZh0e2PD6mpMAvhUYNXQnuYzDWBjs2FpxuBA2Otv9hxd5o0hK71Az-iIBZBfuWflEo6WpeIAQBcHg9FIHyxruuTTz053wDHsnngwFvv1fKcrYP6-UFOBxCt0x8IR0i23U3GYHdXPLcy9i5dexc3qQUkM0-zqyyRPSYJZI-lEz09bY4h4pLOCGv0Tp4BA32BW-22tylVqAiJWdMFkpfslYAa1ZX52wEOlAYfWh_ozoOev6XS46BVKU2Ty_ix0iLNz4sQxvoju12n03b_tYI95tXR1PaskC6vjWO974zg7aTcPxeE3i0aq8iD8n1lVCBZG9d_H2DuCGh1XsWhA_8S-lwcDN0i0crhmTJWBocfzLNFF4zLqxvZRsuvFuGc-9Ym6npTMoZKzE5JjsymXcKoBa8tLAgeda7ipkpUa3b3A_tBjEu7VoPJb-ikLZb0tUxBNhlf5TixD-9W2XtWdnCtDxvUWGJWBU9vVZXZeM_SxIDvOMLi1ZFPed28alBXQ-CXxtF9bpckwlPDs0JjI1EcWgOf9Xu-EN3iL0YmHOf--wsn1R1LkYRUODn4As-dmW44Z6fi8rf2zQ3xjbp9doE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=HlyqUrl6aHprXX5XQI3CZF5fkvTqzLCEwrHYDOuk_osdgORge7UFy_fQAicHBppROyMPtcRhX0JBUP03_9BxNVBMOLZh0e2PD6mpMAvhUYNXQnuYzDWBjs2FpxuBA2Otv9hxd5o0hK71Az-iIBZBfuWflEo6WpeIAQBcHg9FIHyxruuTTz053wDHsnngwFvv1fKcrYP6-UFOBxCt0x8IR0i23U3GYHdXPLcy9i5dexc3qQUkM0-zqyyRPSYJZI-lEz09bY4h4pLOCGv0Tp4BA32BW-22tylVqAiJWdMFkpfslYAa1ZX52wEOlAYfWh_ozoOev6XS46BVKU2Ty_ix0iLNz4sQxvoju12n03b_tYI95tXR1PaskC6vjWO974zg7aTcPxeE3i0aq8iD8n1lVCBZG9d_H2DuCGh1XsWhA_8S-lwcDN0i0crhmTJWBocfzLNFF4zLqxvZRsuvFuGc-9Ym6npTMoZKzE5JjsymXcKoBa8tLAgeda7ipkpUa3b3A_tBjEu7VoPJb-ikLZb0tUxBNhlf5TixD-9W2XtWdnCtDxvUWGJWBU9vVZXZeM_SxIDvOMLi1ZFPed28alBXQ-CXxtF9bpckwlPDs0JjI1EcWgOf9Xu-EN3iL0YmHOf--wsn1R1LkYRUODn4As-dmW44Z6fi8rf2zQ3xjbp9doE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=JxCSayD2lviC1J8zfFFuzIQPUQLYNEymly2IwPWF9C8YnBFDNfGD7MwIsKoS6FVqUCPVroV4nGurC6zBMnKKRfdoEMrG3MqX4sPEBbpfrwLdnBbs7bsvFC7afzNN3FTSJHK7wRkJU6Gsh7EuoADzqxtCdkJ5OeZP5K03Qb4QyGhK9hnhbJiY48z1BQ5VJzBwtFuaXoJ5ThuJBBu5D7bKQc3YKguBie_B0BYW1qIWDLYgJEf4eJ34loefWDczP2kw-XXn1nKnuAZwPElXsWCvNAR4VR5Erzeg1gcwYObyJ8wf5cS2Wi5VxYfGMdZ6Ga0o8yvOboLt5B_gwvjqhb-ViitnOTrOrBNmGVYrbOh23bdWAHK8CwtVhZZovqR4cYrx-HTykosHhr7eFyg8dM98pW7xU3Zf976ZVhby-PUQJgFYR-g3XkGszixfNVdNJ6QSuJxJTd7e4DWp9YeT6WJER43P4_hl2A_WrTz1YUFEzmGzm9tWMg32hQCYzhM7SvAL3e4ISvQnT064TrbhNWxOvWBtDtQVWuoiMQKZiUYAuicIBiEjZHhTJqxYloooMemdSz2PlLAVrZ19unswzATMC4LV0nFZ5t5M1DQd4m32m1J3AjgQg-fdPDn_hvOg4Rw4pQ4sZBML4BTI4wdbFzqtWVR6u4aX6PujU29p9KB98rE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=JxCSayD2lviC1J8zfFFuzIQPUQLYNEymly2IwPWF9C8YnBFDNfGD7MwIsKoS6FVqUCPVroV4nGurC6zBMnKKRfdoEMrG3MqX4sPEBbpfrwLdnBbs7bsvFC7afzNN3FTSJHK7wRkJU6Gsh7EuoADzqxtCdkJ5OeZP5K03Qb4QyGhK9hnhbJiY48z1BQ5VJzBwtFuaXoJ5ThuJBBu5D7bKQc3YKguBie_B0BYW1qIWDLYgJEf4eJ34loefWDczP2kw-XXn1nKnuAZwPElXsWCvNAR4VR5Erzeg1gcwYObyJ8wf5cS2Wi5VxYfGMdZ6Ga0o8yvOboLt5B_gwvjqhb-ViitnOTrOrBNmGVYrbOh23bdWAHK8CwtVhZZovqR4cYrx-HTykosHhr7eFyg8dM98pW7xU3Zf976ZVhby-PUQJgFYR-g3XkGszixfNVdNJ6QSuJxJTd7e4DWp9YeT6WJER43P4_hl2A_WrTz1YUFEzmGzm9tWMg32hQCYzhM7SvAL3e4ISvQnT064TrbhNWxOvWBtDtQVWuoiMQKZiUYAuicIBiEjZHhTJqxYloooMemdSz2PlLAVrZ19unswzATMC4LV0nFZ5t5M1DQd4m32m1J3AjgQg-fdPDn_hvOg4Rw4pQ4sZBML4BTI4wdbFzqtWVR6u4aX6PujU29p9KB98rE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=bpqotkG7EnxwkiFhghl6iR5nOClJEJyhVspM9-iqy4tNWO2B_gSvHu-9scEIq4u5NhEAgPmlotuxfEWDwW-hc3aG9NY_C_xaHYmkanA9STnFcL3ZbPLpzDDFzj9H3KUEJdGv4yU_gzdFsQ0kt96gJHWNgqRiY4iipEfK5ZQxSTWmcBkFuUssAMLT5SEMYaWQ0rCpHOO_g4KaUONB0e3LhtCEEjAuA9SMhdYYayHaVUH9EGLIwWAcGAaphmhB-33qocATTgZF9ti3fAReOxHDDe9aI02pvessV9VJD0lmRS7h8wtsjnXUAkPNyW2JiOsV8Mp2KdqVlII3C6LbkXvB_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=bpqotkG7EnxwkiFhghl6iR5nOClJEJyhVspM9-iqy4tNWO2B_gSvHu-9scEIq4u5NhEAgPmlotuxfEWDwW-hc3aG9NY_C_xaHYmkanA9STnFcL3ZbPLpzDDFzj9H3KUEJdGv4yU_gzdFsQ0kt96gJHWNgqRiY4iipEfK5ZQxSTWmcBkFuUssAMLT5SEMYaWQ0rCpHOO_g4KaUONB0e3LhtCEEjAuA9SMhdYYayHaVUH9EGLIwWAcGAaphmhB-33qocATTgZF9ti3fAReOxHDDe9aI02pvessV9VJD0lmRS7h8wtsjnXUAkPNyW2JiOsV8Mp2KdqVlII3C6LbkXvB_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=RPys_y5cldQXZZOfMp085__Y-lst9QID-S1q8KQjIMtVgLveMtAL5HK3sGJwLB2CM3GkcwuAEVSCFoyKDHYzztDre0zOi1vMnTleE9Ne3cffzvhoYQbVjGd_A5hYoXgW6WEi_gMnL8wTiwWTa3VwsjA6wLUzgCeRUwit8nGfihLjRo2Zf6NHdqtECGmsdWxwQRTUuPxND2aXFfgRX8uobtcG0suO3z3jHwhimM069Fv_8N-VWuov5wZDPbPRDE99hWfIJkz5vW58KLDWV3T1_HYljKBz7lcYVMGCqY--KUQBI7CtkfKTUy02I2tRmBft7GE9fBkK_AbbpIOymbGFsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=RPys_y5cldQXZZOfMp085__Y-lst9QID-S1q8KQjIMtVgLveMtAL5HK3sGJwLB2CM3GkcwuAEVSCFoyKDHYzztDre0zOi1vMnTleE9Ne3cffzvhoYQbVjGd_A5hYoXgW6WEi_gMnL8wTiwWTa3VwsjA6wLUzgCeRUwit8nGfihLjRo2Zf6NHdqtECGmsdWxwQRTUuPxND2aXFfgRX8uobtcG0suO3z3jHwhimM069Fv_8N-VWuov5wZDPbPRDE99hWfIJkz5vW58KLDWV3T1_HYljKBz7lcYVMGCqY--KUQBI7CtkfKTUy02I2tRmBft7GE9fBkK_AbbpIOymbGFsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=hEA-rPLV2h5ZlIhI-3Azg-DYL1yXc5ETMjxmMdnAt8ZgF8uf8n5lR9Nvv0k38SOdIGLGULTjGGDHK4kMUCVwbMGxsySucO9YTMS9DQn72hB_IVMbYbwVKYLHmRBPFzPd0y6bEG5x3HrkzCD2nNW6pS3yeze66Kn32_QeMCiD5i0W0NU2zQVl7aSzLnR9O8j4ElNZWzDbNAqfHZOC-mJiJM__bA0RbRZtRLQ-4EdgCrVdekyvVo6ioji_t4R4uDlQ_vXvmFTQrpELs4Y4Ye8HqUza5sEPjXkk17mmgtL1KhdvRH1l5xI6affyeVBkcPgFXFbrMn195dxUROPoBaBfCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=hEA-rPLV2h5ZlIhI-3Azg-DYL1yXc5ETMjxmMdnAt8ZgF8uf8n5lR9Nvv0k38SOdIGLGULTjGGDHK4kMUCVwbMGxsySucO9YTMS9DQn72hB_IVMbYbwVKYLHmRBPFzPd0y6bEG5x3HrkzCD2nNW6pS3yeze66Kn32_QeMCiD5i0W0NU2zQVl7aSzLnR9O8j4ElNZWzDbNAqfHZOC-mJiJM__bA0RbRZtRLQ-4EdgCrVdekyvVo6ioji_t4R4uDlQ_vXvmFTQrpELs4Y4Ye8HqUza5sEPjXkk17mmgtL1KhdvRH1l5xI6affyeVBkcPgFXFbrMn195dxUROPoBaBfCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=uHXWhnCmTwlDy06TxNHpzApmF3fUrQgdH2yPzIkA9cpJeSUMKfv2hj1l8mv0Cw8eZRJjg3vRIsTSXuDnq5ZbLHEYupcQKjN2ZYl3lxxIDq9f2u0ivS4VsbUEquBO1RQ7DxhprS3dGxKHiBzrIpR90h5nOrUtA_0aAhcX1VMzFHPpcb2Fatr877PZjj82YrWXfhJXXSA9LOIhbWR8PGPK4RYxlqZwZNHsPLWX2vtUiU2zjDRtRUDEW5mnWtTLPqeb4tkMrRMlO3u6zFLyfT7vssnbBYHhwahJ25cYERanww9dE5RLgplHoiu2TpiC3y-77mmezL5Y4BxbMNgIiqkloQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=uHXWhnCmTwlDy06TxNHpzApmF3fUrQgdH2yPzIkA9cpJeSUMKfv2hj1l8mv0Cw8eZRJjg3vRIsTSXuDnq5ZbLHEYupcQKjN2ZYl3lxxIDq9f2u0ivS4VsbUEquBO1RQ7DxhprS3dGxKHiBzrIpR90h5nOrUtA_0aAhcX1VMzFHPpcb2Fatr877PZjj82YrWXfhJXXSA9LOIhbWR8PGPK4RYxlqZwZNHsPLWX2vtUiU2zjDRtRUDEW5mnWtTLPqeb4tkMrRMlO3u6zFLyfT7vssnbBYHhwahJ25cYERanww9dE5RLgplHoiu2TpiC3y-77mmezL5Y4BxbMNgIiqkloQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=o5OhqMvSU5AKaT8xvq-dlbsZGGgEM35LNzLINe73J4h2-Vq-sfVYb0eKakrpSVSfz14ZV8Jxjx46Jtvwj10Drcm-29FpHxuitf55Km4Eq_YZGDwtxjxzrAKa59clfLTy8PPCrziDPBzbljtnz4f3OS6X2l1YHTheRfnCrD-jTHb4c-lAwNKdR4BnkG3jmTKv-IBjcJljQpwjwAiG6ctvlVDDBco5Kxk0ck9K2-BEAaeDEOmfS6iX7aOxUoh992Gv4kkASu2bTsP-pe4lQfCbnyyCFsVXNp61CTL62c-kH7A4cyBqzGGttgIh7hKM8onT4V3a1_PkNswlHJRygx0mGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=o5OhqMvSU5AKaT8xvq-dlbsZGGgEM35LNzLINe73J4h2-Vq-sfVYb0eKakrpSVSfz14ZV8Jxjx46Jtvwj10Drcm-29FpHxuitf55Km4Eq_YZGDwtxjxzrAKa59clfLTy8PPCrziDPBzbljtnz4f3OS6X2l1YHTheRfnCrD-jTHb4c-lAwNKdR4BnkG3jmTKv-IBjcJljQpwjwAiG6ctvlVDDBco5Kxk0ck9K2-BEAaeDEOmfS6iX7aOxUoh992Gv4kkASu2bTsP-pe4lQfCbnyyCFsVXNp61CTL62c-kH7A4cyBqzGGttgIh7hKM8onT4V3a1_PkNswlHJRygx0mGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=WNK1voygsVpSPY-otuztHPfOrqaxiLW3EIwkd8MBuABzC1v78o93gfcgy0ZSuPazR5twxxKS0L95G2NPxq0LIfkDo5AY9lNaaAP4qzW5bPNPolFZP9axrU9zeWOdjsOUD0JyPLtxpYGMCqw1S8fUKPA2rsIVyf7UtfCqhuoeLHIpRTfCMILIUd7EdhByTJDqWAhKR53gT8jIHbbojyY_glKX63e6MxLrIvTBLLpDtGtW7FTIyKyh_Zb27X4Cb_j4vvg9ka7hwAGcJUsSWDgSjjvYFB9aYUBnkTYD8gdJK2YxnArw-JM7B61aDBKkUgieIG3ViuYlcA9eMeBrcMtltA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=WNK1voygsVpSPY-otuztHPfOrqaxiLW3EIwkd8MBuABzC1v78o93gfcgy0ZSuPazR5twxxKS0L95G2NPxq0LIfkDo5AY9lNaaAP4qzW5bPNPolFZP9axrU9zeWOdjsOUD0JyPLtxpYGMCqw1S8fUKPA2rsIVyf7UtfCqhuoeLHIpRTfCMILIUd7EdhByTJDqWAhKR53gT8jIHbbojyY_glKX63e6MxLrIvTBLLpDtGtW7FTIyKyh_Zb27X4Cb_j4vvg9ka7hwAGcJUsSWDgSjjvYFB9aYUBnkTYD8gdJK2YxnArw-JM7B61aDBKkUgieIG3ViuYlcA9eMeBrcMtltA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=DQV6UKFmh6NEFjfdwXXh6-5N7WDwgU9kitOaQ26X7qYwTxwTA13kmvgR4Qxx9lmSDm0Hm-5yAgias3AzOs7tAraAH0MQ_-OtdmjVXXaNMoBF1xEKOcmgcRxKW51DZl1bEkU8cLIHZHwR7OYExKr96zIA-E3_tYMbaZfXrQUVBZlomhkr1Wce1pT1TFESWyYugqY81WZRnRCNjGd9z8apMdbnvd1JzeO9r3cv19GK5yJ-fx4PMoaTgQCbar0l8BWfdtLX7rybkikvKUn9824QeyF26mnSXhQVrGqcKJ2MZE2P6r6nOOxi6-r_eGm7Lk38UcpW-0-uxMF4Z8xuYzlkUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=DQV6UKFmh6NEFjfdwXXh6-5N7WDwgU9kitOaQ26X7qYwTxwTA13kmvgR4Qxx9lmSDm0Hm-5yAgias3AzOs7tAraAH0MQ_-OtdmjVXXaNMoBF1xEKOcmgcRxKW51DZl1bEkU8cLIHZHwR7OYExKr96zIA-E3_tYMbaZfXrQUVBZlomhkr1Wce1pT1TFESWyYugqY81WZRnRCNjGd9z8apMdbnvd1JzeO9r3cv19GK5yJ-fx4PMoaTgQCbar0l8BWfdtLX7rybkikvKUn9824QeyF26mnSXhQVrGqcKJ2MZE2P6r6nOOxi6-r_eGm7Lk38UcpW-0-uxMF4Z8xuYzlkUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQ5i_CALfKqhz1WAJxu7-5Q5hw_G240-IZrUX0PdqClp42nz92RjlesWKfXLjUgXwT-yPdubNBl7fKF6Hy6W9mbis3Gm_v202NAQIg1UGHBeu68NEEazWnuQEHOF6DO7RgTXvBfdQvmsuOhZie0_MshJEKZZKMf5HUH8CefgXtfWfi6wQhb0TYZr5nGR01zo5xcp-lKITHuyn893NT1ycF0gnPhi1UkZTSe4LfjbPVsU_E4ivjKUYWR8GcqO6rfMGaLqsoQFPFv_hEiRVtR9P2nC-bEts7R2usaWBpsEJi4zffZKpzU841Nrjw-Qym3fuWPWsKLlKE4szdwQo1ayug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=Muxt62yDGlOqHQbnFlvXvK2IYFny-iKuZIM9z8D20tJE1q2cwO6awkCpyA3QQUPKUVri3xZt-Nl9fRcbMrA3YXUSCzwd9nT5Vh8bmuPFRAlJxRIT9RVoD11cqBaxH6hImhBlTWxkZKJDGW36Qe6UCTqHOuXa7Xv7SnRU4zEQiFpofC-eln36PHIFw2iby8a0iAtO_WmSow3Ix_8vP_pdaNr-NSCCaCrc72oH5MfDRmGJAtfaa-JjeqvEH_x0zTyu2fW1C0rHrjMjSeR7WsHiFO_sniRByJLAtnPsqPWDgrnge2QzCzE17kcqQgaFPBVU1LJk24nA4Mt5PKa1K6VLqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=Muxt62yDGlOqHQbnFlvXvK2IYFny-iKuZIM9z8D20tJE1q2cwO6awkCpyA3QQUPKUVri3xZt-Nl9fRcbMrA3YXUSCzwd9nT5Vh8bmuPFRAlJxRIT9RVoD11cqBaxH6hImhBlTWxkZKJDGW36Qe6UCTqHOuXa7Xv7SnRU4zEQiFpofC-eln36PHIFw2iby8a0iAtO_WmSow3Ix_8vP_pdaNr-NSCCaCrc72oH5MfDRmGJAtfaa-JjeqvEH_x0zTyu2fW1C0rHrjMjSeR7WsHiFO_sniRByJLAtnPsqPWDgrnge2QzCzE17kcqQgaFPBVU1LJk24nA4Mt5PKa1K6VLqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=FfrWp28JQcmFNRsxNyspbdyTZvuqI_k6o3V-K8LJ5kTIrPh_KTf2oT2dxMT07oTPa-Rk8seYJlXPYe0-2GRuUA5Sxdd_pGvJ566xCMtHOXnDyKQs-BQhYo2-Jhl725ebUvdbi-bKnJdCG2hcS5g-7yPGX45PWLTN4KsbpQbUmZNX2AiRxmrZKottoXG4N1lN6P5nlzbZJLjbLoilUo8INKiK-OjI-DRSt9l3bV-RP7AlhVDr_VUZP2vo17to_2tRERMkaUnbAvFhz5cpcQr28hoJfgtkUIm6um3RB93lEfNwI3YT0HxkixVctLUhpy3rcj181Zz-32DECN7DjAm9fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=FfrWp28JQcmFNRsxNyspbdyTZvuqI_k6o3V-K8LJ5kTIrPh_KTf2oT2dxMT07oTPa-Rk8seYJlXPYe0-2GRuUA5Sxdd_pGvJ566xCMtHOXnDyKQs-BQhYo2-Jhl725ebUvdbi-bKnJdCG2hcS5g-7yPGX45PWLTN4KsbpQbUmZNX2AiRxmrZKottoXG4N1lN6P5nlzbZJLjbLoilUo8INKiK-OjI-DRSt9l3bV-RP7AlhVDr_VUZP2vo17to_2tRERMkaUnbAvFhz5cpcQr28hoJfgtkUIm6um3RB93lEfNwI3YT0HxkixVctLUhpy3rcj181Zz-32DECN7DjAm9fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=jNmynLxPc2jTwzt15DHInSo83kGr3TkHN_TBJgSitDgcevxo5i467g3pRQjCDEosxqcmgN3BmlYeTPSAHEwDNqovf-7iWelORj3Ek3ieBEEtADhKeG8ahbA8dKFs8OoQo1cJ79Bjnf4wZdu6kwYyPxPJHe2ZvFqbXjzT1UZbCgYBsMfQd69fRZcq0EXmp6AQFdw4VtxR2Aw9_hr5RRT9Aml9nHT6n2F6FeMLzKjCqpud8Lnb_9mM-edLo5PizQ4yW-WadUeBDLMW14z92-rnfqGI1w5MN_dDHQYUeIwwM8l414GdTmg49VUN38fGAKpKxI6mCKXdZkaV5vOJpZJxfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=jNmynLxPc2jTwzt15DHInSo83kGr3TkHN_TBJgSitDgcevxo5i467g3pRQjCDEosxqcmgN3BmlYeTPSAHEwDNqovf-7iWelORj3Ek3ieBEEtADhKeG8ahbA8dKFs8OoQo1cJ79Bjnf4wZdu6kwYyPxPJHe2ZvFqbXjzT1UZbCgYBsMfQd69fRZcq0EXmp6AQFdw4VtxR2Aw9_hr5RRT9Aml9nHT6n2F6FeMLzKjCqpud8Lnb_9mM-edLo5PizQ4yW-WadUeBDLMW14z92-rnfqGI1w5MN_dDHQYUeIwwM8l414GdTmg49VUN38fGAKpKxI6mCKXdZkaV5vOJpZJxfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=khS8LXroivlfwODCqL8UnpASwxIe0mvxFZqVVWaBwWm0uiXyYlrPLzM6tGhidg0Qa3PsSfBi3J1w64mN3cOIyjEHkE0ltYjiZQHv4aamL9PnWZTj1rs_xF6j1L868q4i9by34xEpzSKC72YHGWFbekcaaeG1a6jEarSxBn4ST7jg8xkTlxj65QRUgHskRwVhEoQEtTaYO7XJZ5qAGxuBQkhP_k1U84Z9Socgghx0I4cyL-BQzYY5GYXBaLdkvODMSeTHAv1eR5ijbp-0a1SSG-fHkHwds9jd9aw9KngVVMRKu06rkKxQ6D237C9b84Tcox_ZeY5GIPNuX9WZAL6tPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=khS8LXroivlfwODCqL8UnpASwxIe0mvxFZqVVWaBwWm0uiXyYlrPLzM6tGhidg0Qa3PsSfBi3J1w64mN3cOIyjEHkE0ltYjiZQHv4aamL9PnWZTj1rs_xF6j1L868q4i9by34xEpzSKC72YHGWFbekcaaeG1a6jEarSxBn4ST7jg8xkTlxj65QRUgHskRwVhEoQEtTaYO7XJZ5qAGxuBQkhP_k1U84Z9Socgghx0I4cyL-BQzYY5GYXBaLdkvODMSeTHAv1eR5ijbp-0a1SSG-fHkHwds9jd9aw9KngVVMRKu06rkKxQ6D237C9b84Tcox_ZeY5GIPNuX9WZAL6tPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmPMS9hKNORYEGcnmNG4vMfUSzgJFk6QJQIjEdVVs11JnrHniFGO1hPJL8e4bZmf_9ipLnWnvFB2sSRirwJMS0lDTKEhlJcZ1Syv23_QN_Xp8tiqBcLrh9jSZEdA1wtVu4J7IVy4gGiVZe3p3DtvD5VxBDnvRgkULjHI1aRuHGuKnKZqJYYNXtbO_jLOyv42_H72PUAqAiYvYU09QrzCbpNfgGwdUh7Vgn3cuTmSY_QeeLOByaYdsV2WeOBXwW0fJGgFcCLtSai7wXoC-5AGhdWByHLWF8Od8vdlmHbttZHZunSWqZVtrOk8t7nstts4u4dm0UUaLqzPmqf2qO-L-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=MUaQGdofEaE28z6clzZ6opvBw667vP1sBpm-HIkFIOSpryNcQqXqkOH6IfnP4NCnpLLNyCD9_M8Za7qcGCe-ZZoldtSsiX4GJ4z8t2SfCNYtnBrwJEkUEX6XGdby-S0mzM9l5PKGcUUue_Vpaywgqr9VdaBxHJXXfsO0OqFVqrwJGEF7DDygl6JBFII86sOR1HRr6zjzU7LjNnlhckwxQCUZKFmxvG9hRJjOquxxUYlSL5rnvgbRi4ZHK-jGOOqs1rD175kB_rcNPOdh1L1ZfAy2HiqJ7qymnln-4_U_xvl7HbftMeDXgGWW3zjb1drPQUY-zBticUnl3YON5mpm-jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=MUaQGdofEaE28z6clzZ6opvBw667vP1sBpm-HIkFIOSpryNcQqXqkOH6IfnP4NCnpLLNyCD9_M8Za7qcGCe-ZZoldtSsiX4GJ4z8t2SfCNYtnBrwJEkUEX6XGdby-S0mzM9l5PKGcUUue_Vpaywgqr9VdaBxHJXXfsO0OqFVqrwJGEF7DDygl6JBFII86sOR1HRr6zjzU7LjNnlhckwxQCUZKFmxvG9hRJjOquxxUYlSL5rnvgbRi4ZHK-jGOOqs1rD175kB_rcNPOdh1L1ZfAy2HiqJ7qymnln-4_U_xvl7HbftMeDXgGWW3zjb1drPQUY-zBticUnl3YON5mpm-jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=ohF9iVmhWnZJ6NAZAer9NK28GaDzCA12gmO8WEZ9q3WhytwPJtWMIPC9djztNQRKsWRChWICLQfGn5t6GpswU2CZekk47wBs72PRPfzGhUiqIQlzHYjW8STzl-QPujhQxzVGXIcwrzbSvtnybAaHotwKwVL1CgOenIpfcHADs9IjvBQ2wQ05g38llmVbhM046MPISpdt2ktvOovtlPdrrrpwYv40hhTrvvxCwotOvrVXTL2_HZ6H-A1jXAHbCJWJasCrODTG_I14j-l2foU37zbKMTr07fF7q_QOkWSvgFc59fj7A351N-LrGpQmZfChhXEtfdGpjo32qpSWxefY0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=ohF9iVmhWnZJ6NAZAer9NK28GaDzCA12gmO8WEZ9q3WhytwPJtWMIPC9djztNQRKsWRChWICLQfGn5t6GpswU2CZekk47wBs72PRPfzGhUiqIQlzHYjW8STzl-QPujhQxzVGXIcwrzbSvtnybAaHotwKwVL1CgOenIpfcHADs9IjvBQ2wQ05g38llmVbhM046MPISpdt2ktvOovtlPdrrrpwYv40hhTrvvxCwotOvrVXTL2_HZ6H-A1jXAHbCJWJasCrODTG_I14j-l2foU37zbKMTr07fF7q_QOkWSvgFc59fj7A351N-LrGpQmZfChhXEtfdGpjo32qpSWxefY0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fs8EEKlZmzJg7LLmhmU8Fw6MKIo4ZaRMO9H8eP9Slah_iLjD9aLjVVTuW0AMhqxkX9_Fe0Medr5-baT9w8VR4wtoLuNoXCIDfwJf9fZBkzxq_Yrtmza6nuXkMNuTFSA4RIJ_5P3AGQuRDIruJwXdHKCV6tEjRjaqw_bFqbQ0OnZ7yP-oGrTJYcJUh5c_p3J1HWjcGnsMNnFZ0--yQh3UTm4J9p9G7yqAIESlAYr0HId9eDbFIHZVevRoTVlvpNF1RhfHpFt0sRVbv-8ocIAR8jpukDmYyH4-uB8eNABVd-FEGPQRmUpeO1iVQUEKg7suA3Tyde8k65_wB9HCTUgi3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XtF1LQ2nSPxZs_9JGPurPrjkCtEkPnPMLNh8Okp7zHLx673KliQn4Pgrl_xBavz9X_wHcNHfbEhWRTW5Y31CkS-a0KHkedBucxHnBNnhVWkmub0M5IcVVHySXevvutbP6HEcznrVeeOs2aBsbBWeP_33d2KAfp6KWZcf5d7zJybHHO2udSrLi0mneD-0pdrWhu4XUVtVK_iodQPMKJ4qCVmBQE7HrA_4vfbVv6DhiYGsFHb6fqHtS2s7IuXSVPguMWS8Q9sJWBWSmnlIn28m_TJasErckNOy66FwIkymFzAR0i5GB5kJWfn8BkvTwIRGCdkXpuOCoB24Opp7gN9bqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=BSa4G7C7ivwWLCqS74JVEsqnbxCFA_RzoGv6NFigGUIxXiLFgcffJ7FZgIS7OIXa3_M64o8_bb__a0cyeEvSN9aBVfvdizteCBD7lptZ9Dc302Jmz3LUbYX1W8Z3XXxyDQhBoofIEl5pJpEjj2ZLkAUofXiKbDBvbmQfiiAJM92TwjUgbR11Q7Fbfyzy6g0LAeneHRGXaGc_0jnda2gXfU7U0Wcp15kRPHse4wdf_LW8RmucPlWESGL5ZtwOY2qjkW9c92Ll0HU_NX8udxUFG89AW8rCHYij5HmLXhMf_g4oPEcDefnSVM7Rb7KrstLRUt-kB0ktKrRw7oNACNjcdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=BSa4G7C7ivwWLCqS74JVEsqnbxCFA_RzoGv6NFigGUIxXiLFgcffJ7FZgIS7OIXa3_M64o8_bb__a0cyeEvSN9aBVfvdizteCBD7lptZ9Dc302Jmz3LUbYX1W8Z3XXxyDQhBoofIEl5pJpEjj2ZLkAUofXiKbDBvbmQfiiAJM92TwjUgbR11Q7Fbfyzy6g0LAeneHRGXaGc_0jnda2gXfU7U0Wcp15kRPHse4wdf_LW8RmucPlWESGL5ZtwOY2qjkW9c92Ll0HU_NX8udxUFG89AW8rCHYij5HmLXhMf_g4oPEcDefnSVM7Rb7KrstLRUt-kB0ktKrRw7oNACNjcdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DO758VIsUU5urpw7JYWo1cRsat4MWu921zvdxZjoYahn-GS6aXLPBADgIJUhNzXnCHbl_49-NuaWIarWAbs75hKZlTGWMqdxD9zKWZw6b3iGUwon-5ycE1iL6UlXqXrGL0zeit0W60z0gokCSlwbwzfELhK7cIlBGrm0aP7IMO3C8zyT10kBAp8PpPszzBDVNdplYWPpDJoAeZ0gWqgozKCzaWFFcajd_basQFR4V2nhgrREO2JCoJf4vZ_exM5H1snpjtSSjUdHigKc3h4LrALNpfOJOA0hIXKKYdEXcdvtysK6lU086jt5pxrOsXKJ7_FxoWaAhNsTCetUQrFq5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLb_PS1ZaCmL1osPS9SBH508rKFm9KVN3IrlPqQE60A6GXSQLcYF46Ng6Xzf_5YPjzmmlGEbGuvh0LDPGhzTqyaKLOyvudBkvKFFUWw4sSYiOgDnOMEsIFK9kY1x7Ki8qRQh4gilFnw65k7BmCSBOzkhdtDVsY4yi9Oo-nC5s_v_6bN--XPKjuJSGwNkCARNmJT5MdVXhzy_hmV7p0eRALwUyPbATdAay59YjGHmhDja1aVaLqgaffqdyN18Obt8UGnxt5aHD5bfzsraR_ubMldqecAqIeyT1ra57oubEQ8xJbonW-8bf7gvVi2g765gByjvpZMXM1pbi7QZOuSSGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjO666A-vTlp91JZtsg3BE7hocq8BrCZO1B6nS1Nu2eU1OXzSFBbsOuHxF1SqDLGkPwwHi5iRCYxfhgRIncDDeb6q_UC-BenYIuh2th8SPGRg1curFGWjEyvXUS5623j_4zt7-s0akju-X_RMmrlPW2dpBX-r-KTMXshgNoPm1-WGgNaITx4_AeVzWaEs0eLNH3kazvLzyhYj6pjurTOWDuyRtm8UuPM5SyDtV8kfMuZVyXAGLwvUQLYRJbyxNm0T9sdPGUQWMBqHtVSuOfUD_orfKb8xFGcWvCXDhhrExPPoLNgIbfGh40dXYnUD4USDQ_CTG3dquaORvIdPGib7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=Nq-gZT-QCrrUChliDEZ320zvF4PZy2dzNcdj_CCQDUr8NoYV0Ox9TdFI05aPTUeVUqhVkw6LLnmM5MysGiqLC6JnLbK9TlSyjhQ0U8SP72JeOEJVpuboroCGh2fh7rKmCbajam4GE31SRYOeT8e0GPM1v_wl4R2GZN0J_PfrLih3WZYqqcXQZ10L7ltSrWpWcwjYe9OHfeSmZx74Pc2DQx8ro1GOmsDAhjf72VILhEDVjui73HUcyrfosJHrimS_aWiE65X3c2F9hzToMs-zbi70oIDBVcENNnvHer5cNiZahoj89ou0ageQ7SYXUfEil6AfYye3p2tZFPD71f3Qkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=Nq-gZT-QCrrUChliDEZ320zvF4PZy2dzNcdj_CCQDUr8NoYV0Ox9TdFI05aPTUeVUqhVkw6LLnmM5MysGiqLC6JnLbK9TlSyjhQ0U8SP72JeOEJVpuboroCGh2fh7rKmCbajam4GE31SRYOeT8e0GPM1v_wl4R2GZN0J_PfrLih3WZYqqcXQZ10L7ltSrWpWcwjYe9OHfeSmZx74Pc2DQx8ro1GOmsDAhjf72VILhEDVjui73HUcyrfosJHrimS_aWiE65X3c2F9hzToMs-zbi70oIDBVcENNnvHer5cNiZahoj89ou0ageQ7SYXUfEil6AfYye3p2tZFPD71f3Qkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=eahYJkGtZjEEawagJ6fh7pnacuqHyEOfDXApI9ejfczFKBfve_q6Wjxpbxnwv0C_ukmq0KhC9TQ5lbiMF0vEVjHiAGGdck0waeQRgQ6bJkQLCHp-ui0E4Z6e_VtGIbCs1mbUh0zpIAf9xv-QOL32SjMmwa58qIc6PeAnl_KzUgGa8xb8DrwJHEo1IYsi-hbHzV_hp8e3JYAfV_7jDENRhOODANrSlyflPMcP2gHljhPHy3ZsCSx5_p9A4qTRTNzMoNBbnVjYqF2_lENzvjDvgLQPU8FnxqVvHETS-mevLDGC1-5tnMW_PAFTkV3Kvz8w5_aqNFwgVB1Vun8Rp8zd7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=eahYJkGtZjEEawagJ6fh7pnacuqHyEOfDXApI9ejfczFKBfve_q6Wjxpbxnwv0C_ukmq0KhC9TQ5lbiMF0vEVjHiAGGdck0waeQRgQ6bJkQLCHp-ui0E4Z6e_VtGIbCs1mbUh0zpIAf9xv-QOL32SjMmwa58qIc6PeAnl_KzUgGa8xb8DrwJHEo1IYsi-hbHzV_hp8e3JYAfV_7jDENRhOODANrSlyflPMcP2gHljhPHy3ZsCSx5_p9A4qTRTNzMoNBbnVjYqF2_lENzvjDvgLQPU8FnxqVvHETS-mevLDGC1-5tnMW_PAFTkV3Kvz8w5_aqNFwgVB1Vun8Rp8zd7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=GN5fcHXNpQsSuFV1qSVaRcUhoDDqgTFnEhxx4zWV5I_UoJj3vLnDYGSNTA2VzP-cPEm61_IiCwNcrdWrD6EkFWHEB8pCvW9XIN2vXO42XTj2fNRSh-5gi8TxgpbdrHFKA_EHGa3R5bMI-EAJZi1amF1j02zdLbfcf-qQYv9lYomYUooplueLuQcyq8onCA42MdO1HcigsT18ZriMsh3fuM78EilnLNIm9aPU4SuPAVVj3WQbjqmeB6q9XGzOqgcRykor_r3BIxcCcJfzht-uswsST6E92wSY5iyGRjOvktFXWsLaQPKOg5_InCnKx2HLcQVi1dYwk6mdriSX3bEhGxSJMu6lmPMAs36oppyLNZKkebBNa5jTIN4ShOpBTysZFmrSrCoZCOGXNT9npFOJ3gaWahqSyvVgOzxEfmG7s-MjYZoCbG9LSC3tuxLX1DkJTf7jaci5YXqamsZctg27i7NaZ9kF-eeOSuOTlNr5vT2_yLbFuCIDI0iMaLFcLv8raHdVDFeLeZnEFWCr96-va_4UrkvNpCRPQJtKcqrRg7E_b5pnBEa8cmMD7eWbaDG71cHZbzqwjN_Dow0jvtnscJYORa6v8Q98icMtQedy3yb48oSPa44M3gW-uihxZXvPruZCUdGj5EL9osqX5XgYdXvMrxGgyENwuyOS_HzJLrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=GN5fcHXNpQsSuFV1qSVaRcUhoDDqgTFnEhxx4zWV5I_UoJj3vLnDYGSNTA2VzP-cPEm61_IiCwNcrdWrD6EkFWHEB8pCvW9XIN2vXO42XTj2fNRSh-5gi8TxgpbdrHFKA_EHGa3R5bMI-EAJZi1amF1j02zdLbfcf-qQYv9lYomYUooplueLuQcyq8onCA42MdO1HcigsT18ZriMsh3fuM78EilnLNIm9aPU4SuPAVVj3WQbjqmeB6q9XGzOqgcRykor_r3BIxcCcJfzht-uswsST6E92wSY5iyGRjOvktFXWsLaQPKOg5_InCnKx2HLcQVi1dYwk6mdriSX3bEhGxSJMu6lmPMAs36oppyLNZKkebBNa5jTIN4ShOpBTysZFmrSrCoZCOGXNT9npFOJ3gaWahqSyvVgOzxEfmG7s-MjYZoCbG9LSC3tuxLX1DkJTf7jaci5YXqamsZctg27i7NaZ9kF-eeOSuOTlNr5vT2_yLbFuCIDI0iMaLFcLv8raHdVDFeLeZnEFWCr96-va_4UrkvNpCRPQJtKcqrRg7E_b5pnBEa8cmMD7eWbaDG71cHZbzqwjN_Dow0jvtnscJYORa6v8Q98icMtQedy3yb48oSPa44M3gW-uihxZXvPruZCUdGj5EL9osqX5XgYdXvMrxGgyENwuyOS_HzJLrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=UV5vfe1Aaaq48HWdoX4St9sQA8g9PjfpNAPU1kufBfpIjerRh4LltZ5Eq_jCDZ4tXdVE-IzcZx1Ofxab9K69aPSeHN0pEKePtEJ4LyYt2lN_pDvq1wipSpFwUslwkGABj3Td_9RNDxMFm9k20ccWEHjKCJMUveUXH6LOXlfLqsevx-Sg5_AjcWEcOrEzmQV1kIUug1LLKaVquLjs83XVBWICFcWxzgPWqAr_UwuX03RIUZ7USOiYW-AHgVDF4hXiOUK32YpAeJgyqOaO6eG25HeihIhfMt5uoYZPhcsly74l_rwBXVojCyQPkcozwxs8tf0m_UTgVaN6gFXfyVJ-X4QF0d_EHBvaIukEfgo1zspS38BsvR2tCrByAIbUJK_wWXouRJ6ejy4XClFrbgQxaHH-DxHrGlnhv-TfWHRVSEW0NczSb6ouzNr71K2Hkx88rqFE_7MK16R2XFpGQK08xBA3zioZhnP1WqAKrpgxAWfs-FW0aeObPoFRE6TPawHsajYk5GdpU2A17skesKwii8Ay85qvGP_gtMnY3BVHdoWhpbdOJMcOGKYt0wW4RQypsPI3ReeOvUx9DBBW3M-4SnucAiTnhbAfEfJ3mXR38JGiRuk2cTdfR5ieO-rZD0OuEGubIZDllPAUedpAkWK3fwMEX2f9OczKiEWlUM4yu4k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=UV5vfe1Aaaq48HWdoX4St9sQA8g9PjfpNAPU1kufBfpIjerRh4LltZ5Eq_jCDZ4tXdVE-IzcZx1Ofxab9K69aPSeHN0pEKePtEJ4LyYt2lN_pDvq1wipSpFwUslwkGABj3Td_9RNDxMFm9k20ccWEHjKCJMUveUXH6LOXlfLqsevx-Sg5_AjcWEcOrEzmQV1kIUug1LLKaVquLjs83XVBWICFcWxzgPWqAr_UwuX03RIUZ7USOiYW-AHgVDF4hXiOUK32YpAeJgyqOaO6eG25HeihIhfMt5uoYZPhcsly74l_rwBXVojCyQPkcozwxs8tf0m_UTgVaN6gFXfyVJ-X4QF0d_EHBvaIukEfgo1zspS38BsvR2tCrByAIbUJK_wWXouRJ6ejy4XClFrbgQxaHH-DxHrGlnhv-TfWHRVSEW0NczSb6ouzNr71K2Hkx88rqFE_7MK16R2XFpGQK08xBA3zioZhnP1WqAKrpgxAWfs-FW0aeObPoFRE6TPawHsajYk5GdpU2A17skesKwii8Ay85qvGP_gtMnY3BVHdoWhpbdOJMcOGKYt0wW4RQypsPI3ReeOvUx9DBBW3M-4SnucAiTnhbAfEfJ3mXR38JGiRuk2cTdfR5ieO-rZD0OuEGubIZDllPAUedpAkWK3fwMEX2f9OczKiEWlUM4yu4k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=CP8ezhj7iyQSgF0IG3B78uUO_I-fgfOdTkimFUI2mz58ZDy1oXFVSbo3I-u5LNHbRh0UiEaGMQ9-RNLtLOkBYInoFzFlv-51BAmVF0kg_6QH7sUyG02E739LwBMc06oNtd4Q749__rGatPucRQvIAd3OAup4_zNNjusDP-GqhSZ9wxOuAU3k_B5e7uj16hxcM28bHGb4dUivVZFd6Eiw4BKv68fb2HmsB3Lc1JknwBrqdK2lAIzUUEYzR207FFL6FGsrbMNK7ssVvjBDJdvweKOrnWYaMr4cSa61pp_R6leseJyNT7CEJsgmAx2qJjP-13dL7wKxHZnb5JBSIHcvoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=CP8ezhj7iyQSgF0IG3B78uUO_I-fgfOdTkimFUI2mz58ZDy1oXFVSbo3I-u5LNHbRh0UiEaGMQ9-RNLtLOkBYInoFzFlv-51BAmVF0kg_6QH7sUyG02E739LwBMc06oNtd4Q749__rGatPucRQvIAd3OAup4_zNNjusDP-GqhSZ9wxOuAU3k_B5e7uj16hxcM28bHGb4dUivVZFd6Eiw4BKv68fb2HmsB3Lc1JknwBrqdK2lAIzUUEYzR207FFL6FGsrbMNK7ssVvjBDJdvweKOrnWYaMr4cSa61pp_R6leseJyNT7CEJsgmAx2qJjP-13dL7wKxHZnb5JBSIHcvoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSB5SIw848zY92MaR42-Zt1P5KhHgdxK8bwYkM6NubBkKEpsYK8dZsQo_iVPn2NyKNAgvew6yyQq8l43Gu8MzFbCSCwIViE8ptsWC4wgsEgRN5ZeHGoUmEza0MnTuWPy5ksrTfYWWvlI64GCziFQZmFH-dT8_Qny3qgmo6vSTfuqQtMY02gKT4SgzUtInMcvJDPcdeZic26mJe30iYBblCYemnjLywkL7C5ZaNMSnk_UJrK-zgbKUy71UtBL2MikhGZ-I6fJ5NB1Yyowwb72yLc-s1OZbLDkXPD9Y4MR2hMTrEtzvbrC2lZPyJD6X5DnCAopu9laTsK34WHj14jeLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=VPdZ-NEDga7I-yoFcj-4JLKWa5bKb1Lw_MCrjThU4c2qKKZAhDIbfJ_AnlY6wWaa4nHkhqz8aOlWaL1iLG5etT54IrvdQGP6bbJ4SBkk9o0cKUKSw7jVxBatFF84RAu1PizPgO4MnjKyrfdjJbMenrpmi5hGM6flYl6VpAYmcZuszpsswOBGot2JIBhmXljCq6QnGiIg52OeszvJUFyL8REggymHt2uz-4w4G6lgQP-s9Xqcc5nWW3ZlpUGsb9v-9DlpOU1h0-kuPph9NxXm_FVhNOyvB1n3I8JvW-NtGJ-rO1GTs527FWLR0nr6lsp870t0bGoRvHaxclOcRsaSgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=VPdZ-NEDga7I-yoFcj-4JLKWa5bKb1Lw_MCrjThU4c2qKKZAhDIbfJ_AnlY6wWaa4nHkhqz8aOlWaL1iLG5etT54IrvdQGP6bbJ4SBkk9o0cKUKSw7jVxBatFF84RAu1PizPgO4MnjKyrfdjJbMenrpmi5hGM6flYl6VpAYmcZuszpsswOBGot2JIBhmXljCq6QnGiIg52OeszvJUFyL8REggymHt2uz-4w4G6lgQP-s9Xqcc5nWW3ZlpUGsb9v-9DlpOU1h0-kuPph9NxXm_FVhNOyvB1n3I8JvW-NtGJ-rO1GTs527FWLR0nr6lsp870t0bGoRvHaxclOcRsaSgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=D7Jujv-TGahzAnCDOIop-MsExqoJuNNJaDKEiEi1-YdYkWTsm1wGeu4KVfMNVUcIFFnxNaQQW6KavI0FnY2LWqzfubnVHtIqFyN0hLM5PfuZj88IrHM2lGrKdUH26LCRxa-eQAv-eeuPg-0BQ9-bKDRpzb9qYVoynTeMQvRdmooQg3MWKKSIoQv03A6S0hEj8TJmKmw10v-aekWfpp5xJFKBPtGbt1uJsAeT7RvRI-s0ZvR1HJIqzxhfcU1K0idYVh6fykr_A5M17CXVRDekd5y1QwThNumrw10CO753Wh22oyRsnD6ZvJrXUjQdVsONz-JknqfXPmqm8-UjIQtU4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=D7Jujv-TGahzAnCDOIop-MsExqoJuNNJaDKEiEi1-YdYkWTsm1wGeu4KVfMNVUcIFFnxNaQQW6KavI0FnY2LWqzfubnVHtIqFyN0hLM5PfuZj88IrHM2lGrKdUH26LCRxa-eQAv-eeuPg-0BQ9-bKDRpzb9qYVoynTeMQvRdmooQg3MWKKSIoQv03A6S0hEj8TJmKmw10v-aekWfpp5xJFKBPtGbt1uJsAeT7RvRI-s0ZvR1HJIqzxhfcU1K0idYVh6fykr_A5M17CXVRDekd5y1QwThNumrw10CO753Wh22oyRsnD6ZvJrXUjQdVsONz-JknqfXPmqm8-UjIQtU4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FArZ7SybQuypg7v_1SIlX_t0Z5mJvW9C02mtwBvmQdV5cunEPC-COIed9c4bQB2tszdixqm1dNHDxaYaW1WzzyxpKSjz3dhltGFj7xcVaz2UMJqCZFutkfhJR-QCUSR24by9Em-EPhZQ5qfNByS-SUpvFcw6czMpnQ3h6DyEPCFBMKRySwzNRo4iX5dbWLNDycAVFoYTvOBD9Hega32w6ET1C75cyXF-3bpnHSMkfNYBWS5-WLuvW6W6EN9iNTPOlqKgrxTYst7PrN_PotFZ4p60px3mGy8zYRC0TyKk9cI2CMmULquuCDMwY5cTjQ5R7ri18RfP4VfiOpeQ_udJQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPu1yUMNWoOMNoRHhH--QrHeWq6ZxH17V__aq--OMEt_5vER0xf9h-TWj5zxs41kIDS9wIM7CP865MC_cdxfKZWe0OQbl9dXNzzwDpgRVMO-kMqc4uTsutofKPGRV5JW4QYlzBxK412NixJvQOlEmHbXh1NZ9lE93D1H9WaDusBKbcgnHqLhpaebuAfZKyaDtTHyWOYepfdB5Qat1j-pBn5Vd6jP5CM-_WvntW5Kh3CPoNa_D1zfdwuBQYHt3g9HSyWSaf0TwLymvRUNniQER74CYp_F0Fv87W7cvCaA-wggvMjmRFN72rXE5YexzdudqmyUDymY2Ezeuajp4dG4bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4PiZoaq7p63ZWGhBpbEjE0Zdgcq4FYrw09_jVtcsozq8KWgt2f8Rgq0f1BmENipBucw9LGCtnr5-FQ0-BjAgJTqxP_rxR9G_YnpgGvdwFzA0ZjxJSY4yOxrUTCd7ZyV7__J-IbroBe2ibPcMPIZcxQWulUFwX2g2Vd3Lb2hUBfB9GKeQnpaF0iUcoliaKd06Q3uVegQG_tDbVPTjvtq1kRtQrfdLwFtobEIrodqx4b4DO9o5RV_T7ks7x3q3dQTU_hDALdIXhzfx4gQPuH1x84fJ58qH0pvA7HsEzDA1_j0zr_kK2PVWcCumky88dYnRqxGJStrWe4zmvuX8RZzig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mi459p7dcWCJ_Z7jUSU-FfjyRtOMO0P27UkZGqzZacr5fLAOKdHd2-twJE5bEKXZgpTdh2kWK_nc_vLgKM6CNwOOe22VCM3IT_XC5yvCYdT8WvTyOIO2o2kWseDOy7SdAaxjoEMfUQBsowz5DSI7vVmkuERxs7m53Qjp19ZsXJNwV0ZLPb17-jv3gzXxI_29bWzozGNwMTi8N7MFeSf-9z4pVnzegJ1cHEV5wU-_VvnSq58EjLCdzNY0iBdPzu_FJbAW1OZ0O3mpOf_yfwp5x7e7aa65EjIc1xDRl9i3_mf39wkMAcklqnJBqtU9rY0NXPDX_TTIfqHS4yvEXfggdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXihvzj6WzVwQFuc5ZJYn4QeVVLnvwZ61Dmuv-c1hGMojog-IUGYrQKF923JqLAMVVrdLA-0LrWhqnFCnRyJsX1piT548N_9takaNXxPS8y0ppuwBXxHaxZY8-krcsGynlMu_iB3YtuF2q3Ok-zBNS36ZPnmEhkIsj5uJNVifFEUTkkxbxJD3ABPz_ZmRWjktA0PCKMsZX5MFsXc3x3SyHAIqGpcbXN3fWyUJEqeIP4-dNDCs7JWYHCQUixFcFw9siNuVBm9wTsgK3ZwgIE6ZpdZF3nPbv6S3hIF1minTX0bObputBrXLiOXrfyzN7mG8lEuv_JhFfdw9qdtJS8-ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhdI2oYdab_RXxVycifs4hBbBovDYN9qSog_aKbbG4_kr6fcUxdHkb1vabUwFFsfUviFQePvn3tu5e-bgRYG9EPMHppJoRE7mjxMmjwXDrukLD_Q3HlmtY405hsN-r-nMmrwxPfXiKcp2WIL01NyfWJyvTD3LnImR000-dnH3Ll7VKoGnIFhUs-UQpc809RiAHfmhIGiQhijFk2X9mX0X6dYsvQUTOazxaJnjamcAN7xbr1ug7SaH0sROwS443tYs-LGPW5snx0jNYorjv1E3oAsACoJ2C4N6Vw4kwKdJRfEiwimjQ4qjp3Yn5_CJVtgBrMn_N8CxA_Cp8svAv4qZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMcClJqeXZ1Ey-zuC0URCLFxTR0dRE_aHXm0-_-eA305YWxN_wvRmUeY69z6BaVwCbxJ8md6Wi8eOkEIDWswS8H7VXBvzDSfbU8ALzvw1I1ZmhpXzqNK59RBvfpJIl-6JI8TJju5DIUjAjD3Eqb1A_uisge1Cbbp7qvxV-X34fkA9IHXNuxPLeAp8tRlX0BBGxN246tM2yRiy5HS_wqS3mJecLn160LGTVBuy9D8dfS5YFKOMfrzoWy98noKitYy8BI7HW-Q0Lb7C7A2KTCStRLsEdaBpubh6Yzb1amhzjUpzJ3zq26oEcp0rB8C8BSMpz8LEyXF-k6nTyhEKv6lqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N4xIXN9J-GhU3-5HWcwkhVYfo0p-q_PEIO26367NAcx9H7AHthwFe77VGqbL8ySCkSQ-Y-uN2r1v3xhtcnlz7tclIfOn7YJuJt4WBMW6TLmS9RI81jP7wU7IIFvamBkXeE-599yABQknOoWNxKNoD-2pUolBgwZm3b5ecy5_OvfCyLJ4IMi8pTUPTa-WshQdNFy7eTJ2_svueyxpwWj3_v3YG0ZY-6x2NfFd6Mzpdi5zMJwan0RvKj0GSMCqq5Dv6qF2_diMuiOVR-_6Zlf0BIph_3dT_dihzLM9bswG3SrhVaPaVgmPeUwkTPoE9fVZzMDdp4JH8jJWu-jOFl0OXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hqBTQLSc7CYJk5j6hZsPude9TkyH_jhJ154IhzfA1lyAquoFd0fUNOKc4ufZJ-Ml9BuP2q6NMp7ZVKNWODALtu0UkjgGQA2wdUmaQ4wJhWLX6i-PyZwOGJSN3Ja1rH8YCwCUKHLm_ygeOHPPgfAfjFbMZadNYownYhjAnZsg6Dp7gHHqm4W3WLZSPcGhlmleVOZ7LzPQd4D3HXa7S8EX-qUk-eaUgZ712CzkAV6ouZuLqlghhADBLu9-FtPfYA9SEjqFxaUy8DqylEzeAitjcwUEVZSHZElpTCeWtevzdv_-I3-Ij4B6WVnrImZFcIRHKoLN4vlMy83_goTnoit_Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cANhsDF5Ujl4ZERCKL3nVoVkg-OZvyfFofKhiUevCMs6OOiVxvJt6xrkCi9G2CIoLPB0TsMIPG7L5YKv4otZrQXv1_oYSTWKUFy3ky1n_06vGcQZpnPTppmH-qfbQ3ILBLDOzGh_xLS5B48PG-K5A9X23dldrnqlR5ck_diOS1UN4hkibJIrl1Oga-1Zp_1dRs2Wk0pVAX7gSB4W6owPY9tlog1u9e3QYPK_Lmt3dCB75jYJPzpeKiBx1573cEEWdJW6v5_dEPoY4UYb5_ygQNuGAuNd-fpS0l6NHjkTH6EdUhWlMEw10nsdsJq4-fIr2AertpUYZ1vdnA5eVa_AYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=Ndyz3o0yHSluziRd8rim3WJR1iz5yQqRA8Seuo2YUJWJnW7LlM_PygKUnbV6cQPwDPdsm3yx87B27RXZEy_FzD0RsGWjfCqEIW5qsQ48NqBz-Wx2Wfpx-lH2t6z2hnuKqA5sjXFeLD8CIwOa__ns8q6edxc7JoArf_b17aShSVvkdt8YRGqADCJuHL6AHmpZk9Ja92vO-QKKNpmRMsi4P1wk_1i0zVcQ2pIrjbNp0THODiQkX22oz1uTqlZM8wWuQYNn7YsP1LeCMCk04vplXHbRpqQ5rBPeZHKy8MMaObC7jX5_f0TeT7U5jwCk2xYKewTUzitA_upq0FbgKfYfGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=Ndyz3o0yHSluziRd8rim3WJR1iz5yQqRA8Seuo2YUJWJnW7LlM_PygKUnbV6cQPwDPdsm3yx87B27RXZEy_FzD0RsGWjfCqEIW5qsQ48NqBz-Wx2Wfpx-lH2t6z2hnuKqA5sjXFeLD8CIwOa__ns8q6edxc7JoArf_b17aShSVvkdt8YRGqADCJuHL6AHmpZk9Ja92vO-QKKNpmRMsi4P1wk_1i0zVcQ2pIrjbNp0THODiQkX22oz1uTqlZM8wWuQYNn7YsP1LeCMCk04vplXHbRpqQ5rBPeZHKy8MMaObC7jX5_f0TeT7U5jwCk2xYKewTUzitA_upq0FbgKfYfGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
