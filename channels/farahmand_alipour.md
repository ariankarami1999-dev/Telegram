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
<img src="https://cdn4.telesco.pe/file/vveoeBcQmTg4aTHwCOBfIIMcGUHqqQA-PDJ6RznmxwynlJsouxtWtsBm_Rxqr3gnx8hrR5xstnxQEINDJ9TZq05l_NMRrC-WCCoxeFbwTr9rNc1rZJAFOSvLg_M8AqFIrI75f9hpxPnw-l7sP_A59dJRoQTeEsXCIJYtjbtan7OcwJU6vtS0vpTt4hNuvYwlpAd9UoTB-ltXcqKaKa1dh7BIzc6_7FJxJQueM4PdYLstDt9n-btoyX63WXFUkMLf22sUIJKkl1qm9tvgxOGiqhw4NUhZf-6paB-BNn0FWUioqKKmTS1jhHizshQvXwvrHvKUiRZw72TtAttv19pXvw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.8K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-06 21:14:38</div>
<hr>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4Xu-1Sv90oyw714rx6EwCm8pyPA1QzJzkpoobjrS0xEIstln6p6BVQFAWDdNBc0i9vgMbSwNhynf9temTE6hoGPeazJfnoWbNLt9KJuEw2x1kM39CcK08xuRQsKq6A5IL6TmB77y6M4AKJl-Nqk1z8lp3556EP_CXBSlbOHP4kGXI4DP1Lhp0achH3MRLxSRjn97t6PPcv65QeAnQrq9oc9M34Z_3WkRHUyJMouT2glyogky1kN_YhKevps6watjL9NT7pe0wrxUFjh7sxTP_r7MCUCE_3nTuHpKLN-B67sE4T6kG8QSPRIRo37NQdJPoh7X-ZgdkxObB0tRFZWQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1ZpdqpsBzE27rK5Z_5mJKT9IBaFpahsusZ_-0P24q3ZgKmErguuwwVSps6ytinY53g_hqwMVDONsCP4g1smpjBjH6kPGWNuTmXayUWkLM1IEm-Pbc6IDWmENnk8wDzdsDu0n8hcdX0JEph8wcbRT-1vxyGsey6hnath9Erxyf0VkimOK0HolzIGrUU-z7qt-OpNbOT2KlxzguXSyVLh9cMsEghp8wZXQ-JmwwRiWXYTlwVDc6ELWdOU_907l5bCMCFsQuOJ8gIhSFi-4IDM1Sq2XIc7ey_d8Aj2Awu8wNAhyNo0lOJBpfcQCAYKrUvkn1EteQl5cJK1lFjoQ90Tyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgCqLA_DdIPrnizY3P1iylZBLxJO721Xw8cVeA4V8w3CwZStumvXfQkYwdf43jgGZtJBsJS5XJ48BEd_7xeRdXGWRQBydXXCtFYZ-tAcWT-BtneYlSs3pc7FtNNtnycX-SswNQmQ0ZUTbm1Q0dKSVtWMGxVrtvDIulIP_9ZsSxW8VFxQx36uXvRLvuz_wmn77O-KTgwGgwzep9cSWmGQLvXeTA9nhq_8O-SCDOxfhML50T974xKV1R4Y1IdcgOUJ_BNTQHVBlod4XuV7THNdyBTIptZ-mgUKsqDeaMUCFY3oHnVjLlK4uHSfUZZrjTuCOOeSwWGayWpkVCSc0H1LJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gcwe6u2j0vunHd4bFAIX-wyJKNNjg5HdIqfNxSdW4Jw4irGkjCz8ZpkHPO6YOJtHq6yWsiGPwNS6fFVEveIUkNUqG1jCLoTXOyQ4Sf_dbAxe2rxomn8hutqZYhrllc_FtvNsj6-w229exrZO37vU-4fBd9rIBCjE10Y_ULdUlaKXAB51cLN7s_DSHnuCGYa7DjXB2motv0qHjNLIHeU2Z7I95lW5JVIqqk9CoHDpMwYuiVOp3ZqnBurILqBLtxiVDBdZlQJ6LiplYwJdlwQOqMbPfntYwJlpCaoBWYMW033r3Y5im73x0fp8Dd-tqraJB8QivvrMWidR3gw57tyIZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nb64PhowCIuvmhDVUkgpJq7v85KlZU66c1nSRk59VKf9iWSKhwlQe9iTl77b25deFa-8DDblAvJJ8jzNlrmYkAgOqyzU1GwbjzeHCZRRQK0o6lrLcp_kn6wdPgu0pIrIRY1jF9i1N0VSuSOD9f2hlS1B5UZ5gObkgiyzyDjq08_sBGqfH9kFNLwEnm832mS43iwiOOYSvD3nNnDDmsc5WShnBPNAhRSnjoGjWWHiMrC-ZlSw-M-GYDyDYTyMPxyQEGyzbQHmfnJ4lWm-YCzOgJJP7R8kaGaZfFJCLSRn33SWYSoGPgycVIkw8RKxFuCe2C3t-AuchO5aYL-jrKjNgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qF3-g3e1agODtTDysxmphWsvsITNOdL4atCiy12UeIv_hV34ugftvssceTiWpCvKKQXjjDlYdH74oHrIWBvTBlrPAop7534aGfXaLwhGF64B5x_17j2pQkcXeu5InEZynBXTDG7OZYN5WHNfQ5HK5hYlNZU9q7w9z8zzGCTYpN5gmmeMz_4W0yNtdd9OHtZ6tq7_0ZwtvKLis2Ec4SqJ8-gW5yYSjqHCR_dwkFCZsXoqYOTdZwz_SJ1kN-sGf9WU7xlQwTdKcH-cJmNG49QAaRPRRijrx5C2DW_sKLdMDY91SRIyO1pQOJp-qnC5s7p51L-Bk2nqp2e3yrPL1_v6iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=pBJyJHaozhExItRTMlpkhABlQItkN-N7v3sywh2fRtrxeWotKptl4uJN7I95Wd-zdWGPg_F46eo65H1fQc9hwsbO8-3W59ezRmsXNbOuCBxqzpJRvlUYWOdZ4TwfxQYBYk1QPEpwAC8eMbo5bqyv0xer9RabvQCo-FUApa--XjVw3Hdwx7m3eNoYq1Is0KKbGyfyvuGmiPbhWSSVa1hj1_ibgJLWsWKuC1Vtou37856uNwiyh9CL8rTFCN4uAvy9VKR56lPeJo5-gnG7VUKHed3HSxMcsg7Rj1HvGRnZb7E0Sd4LgSheySp1UHf5xOPYPDQalYoOhIDTCS-1vyj3kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=pBJyJHaozhExItRTMlpkhABlQItkN-N7v3sywh2fRtrxeWotKptl4uJN7I95Wd-zdWGPg_F46eo65H1fQc9hwsbO8-3W59ezRmsXNbOuCBxqzpJRvlUYWOdZ4TwfxQYBYk1QPEpwAC8eMbo5bqyv0xer9RabvQCo-FUApa--XjVw3Hdwx7m3eNoYq1Is0KKbGyfyvuGmiPbhWSSVa1hj1_ibgJLWsWKuC1Vtou37856uNwiyh9CL8rTFCN4uAvy9VKR56lPeJo5-gnG7VUKHed3HSxMcsg7Rj1HvGRnZb7E0Sd4LgSheySp1UHf5xOPYPDQalYoOhIDTCS-1vyj3kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVSl3ge9eMRPBQ663lOSWJBQzrP99YeQ39kcR58WvPuXVbvKTL5ejPtRbLXQ0n3Qe8vO_GEs7NcSlmjS9KbI4TzlkIRnPAuxOZV042igNMrXrabSPpFCdqeVUJmTNybknOabDfYYpI1_EQTSPLrpp-L-XFsr3Jrfyn3-LQU1uV5-IvdDG-_H4LKXPpaQfEmUTpEtbd8tGj_UXOlVHM7HaCuxyRk3t5fzkh-4aSM5WE0SEko0DrsrRytKGknFcbLMnNykSTZQLkrkMvTKIToaNPkYPEmRUTjSVjrxruYGkn6M8-v-blwwuwFH8ZgjYBQmutkpNX-TBPqMZmKzcJYOjw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8G8GiC1xK4MdwpGEjU3nInXVlAIIkLCg5qUc9F5-xlZotizjpdBPoWXVq-1IdamnoTbKeuoBrKrMvPzARu5107cg8YV4e_ZvXhxZI0467jmqSh2sllmxeOQn7f0_46bsVx5aSbLXch2jNaGVhIibH4bkWLNE8rKXXA2nbMaEjQBzc4usyb7XCwAEF0L1Je4ypI1uwOkxPgFKuQLDm_-EeNgeI9ujlRcYzuyZIXZv3j0CUrVxyx6G3Y3stXRES6UUjfdiqeoSVtuebfq7JiyoTFQVL7X8WlOYPVoBk0yjVwvCBOU34cO1XA1_5X9vnPF8KLB5rM2aaaFq9TbyufCkCiU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8G8GiC1xK4MdwpGEjU3nInXVlAIIkLCg5qUc9F5-xlZotizjpdBPoWXVq-1IdamnoTbKeuoBrKrMvPzARu5107cg8YV4e_ZvXhxZI0467jmqSh2sllmxeOQn7f0_46bsVx5aSbLXch2jNaGVhIibH4bkWLNE8rKXXA2nbMaEjQBzc4usyb7XCwAEF0L1Je4ypI1uwOkxPgFKuQLDm_-EeNgeI9ujlRcYzuyZIXZv3j0CUrVxyx6G3Y3stXRES6UUjfdiqeoSVtuebfq7JiyoTFQVL7X8WlOYPVoBk0yjVwvCBOU34cO1XA1_5X9vnPF8KLB5rM2aaaFq9TbyufCkCiU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=r5oPG7UNO_aliA7I1DFwB2K8Nlh3sK7kEFxQ8JxIH26Y_FQXCoIOkXzeD3lmdb3OFvc_2q7IFfrqByq38ufRtQVDmkVRSW_vta-llVnEwl-ihqgW10vyqfcV-Hka1XZJfc6A5zqeJNqyzRLwxk6tDUDci_-zERmYW8AI0l9IOYYPFeCWgXOuzPY85zW2_PdG3p-g1-5l9vjJ-XExCgyroxiPy_U4K88uLKRC0MGbe-HWAkn3-TUDaRt0fCCyjeYJ5IEDLRiHTkshOIne_mCFL1GNrX6vnC48jGjZOkOGvP5I2aJ_mNMx7MvKnqOKhJ-wEHC3-9nkPbhB4p_7eA1jUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=r5oPG7UNO_aliA7I1DFwB2K8Nlh3sK7kEFxQ8JxIH26Y_FQXCoIOkXzeD3lmdb3OFvc_2q7IFfrqByq38ufRtQVDmkVRSW_vta-llVnEwl-ihqgW10vyqfcV-Hka1XZJfc6A5zqeJNqyzRLwxk6tDUDci_-zERmYW8AI0l9IOYYPFeCWgXOuzPY85zW2_PdG3p-g1-5l9vjJ-XExCgyroxiPy_U4K88uLKRC0MGbe-HWAkn3-TUDaRt0fCCyjeYJ5IEDLRiHTkshOIne_mCFL1GNrX6vnC48jGjZOkOGvP5I2aJ_mNMx7MvKnqOKhJ-wEHC3-9nkPbhB4p_7eA1jUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQpjWodFZAINRBzakHcvfKD_VyY6gw4xcrf-HFnryDVD6iCHnl17_ypbmYKTJNHJqhMGWh44QQzhfE2rZAuQ-WHX_hXBrvCs-0R-uKfafmldVAExbHWzIUx25C9h7PQcKEkrBzxoPL7c1vlkvuj-Vrld4Iu2jXHKH8M5W_Br7e2uAoA82oA0dqKUzLs0ibiQ_OX7s_R5JElFkhf6jcPQ01gWS3nvev15tdvKnEZAmzJmGYlCZ_iQTZf0IP_yZVKSNJurRsD1p3-yvnS9HRsQndpQeNDrIFtLGs-R4iFntp-hVsk5rgxxPRGkDKKMzHuUVpWboR6JeOXU-HjITqNiRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=oYFtwG1Kc9bRVg5Z2d4ed0P5q8IfPcmmtTL164xijdmcLsj0_qsJCPCntUaMHs9lFKXLHkWpz-XP45ZKSL_mIVvkHcUaqd2xMM0kn_pw4qCkWGA2YgXgAcJnUosC7cHwy-kBDHetTE-6nys9O7PaOj9bdtNUnfXTeuXMkVYUlJ_8I8a_t89Z6z_OD9Hpy1nqKb14hmepMeaJBiUN-6vepzIWjhL-9OyUTAwhjRv32a8_8BnoQxtGyzjazVKHcwZcD_8H3HaK42l3cQnRnzGiO4OqB-TEwYynmtu2tLsYMVSehH25V7il3Zvq88zsfIlJeHZHpRA88rnvOuo35-I5plxHtM_NlnlZc3TtZH4LZdA2C6Fl1iWZAbNNhhqt1WDP1UpiIe5a_wiQsVj4mQ1WBK4MrikrNOn6fvcNtidHQfIPLJv5gz0sKA6x8JlQPT8V2ehhNd682Lbzk_Wkph3GYGckg1m0MjJNdrosWxxgO3UaZ4JodsUtJypp4BWTOHFRib2qCQx7nUbAeHUqDU4E_k7wLeN4k7Iq-O-51Rm1j5Nl6xnFuVipU_RMqGT-teT_KzxqlbpL4YLWR617c9oPlDPGxf0FofDMoZwbS0DdffSF3B16pbqkNHjf4OX7WHA9AfeRF7QLtyR05T5MS-2nRxYSetpjo-NgUeoPUAZazJ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=oYFtwG1Kc9bRVg5Z2d4ed0P5q8IfPcmmtTL164xijdmcLsj0_qsJCPCntUaMHs9lFKXLHkWpz-XP45ZKSL_mIVvkHcUaqd2xMM0kn_pw4qCkWGA2YgXgAcJnUosC7cHwy-kBDHetTE-6nys9O7PaOj9bdtNUnfXTeuXMkVYUlJ_8I8a_t89Z6z_OD9Hpy1nqKb14hmepMeaJBiUN-6vepzIWjhL-9OyUTAwhjRv32a8_8BnoQxtGyzjazVKHcwZcD_8H3HaK42l3cQnRnzGiO4OqB-TEwYynmtu2tLsYMVSehH25V7il3Zvq88zsfIlJeHZHpRA88rnvOuo35-I5plxHtM_NlnlZc3TtZH4LZdA2C6Fl1iWZAbNNhhqt1WDP1UpiIe5a_wiQsVj4mQ1WBK4MrikrNOn6fvcNtidHQfIPLJv5gz0sKA6x8JlQPT8V2ehhNd682Lbzk_Wkph3GYGckg1m0MjJNdrosWxxgO3UaZ4JodsUtJypp4BWTOHFRib2qCQx7nUbAeHUqDU4E_k7wLeN4k7Iq-O-51Rm1j5Nl6xnFuVipU_RMqGT-teT_KzxqlbpL4YLWR617c9oPlDPGxf0FofDMoZwbS0DdffSF3B16pbqkNHjf4OX7WHA9AfeRF7QLtyR05T5MS-2nRxYSetpjo-NgUeoPUAZazJ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLhrSBhxZzOgGiYNgDfHx2K-yA2YD9VALzMFKfu7pNC_f22N9UxK6wwscJrXtDQ6HuXgpZj5eVfgXEUeYGRzH5eunfpagvpbQKtPCPyThlIuLrEX41QNU2DXmWP3Hjn2riffPQxn3xDfgWqgDOyVyVf2DUp6lAr_OhMo_S9y1Pc8Ah_F9ojV06H8bf4DgXNOtX7yC4MExbMczHdXrrTTE-huPX0fMPN92a00wvQ02UYprJ6GklAhkRWiyxvYrNSGNAFG5x8kXzGjzXXh1-n-2UWQDEL8QVsYlsXLPZaToT748SgFfDXpo1FjtvmxU89Lc3N4-jmWyY_kwM6Gnp8ERw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=Wjw5itJZKFyuh6m5r8jdBmeaiQvnrJzKyKPlZorSyegKS-HKWgpSycGc3VqW3O5INtVmJ9UGRn4Du1ynXo-gAlNAFXsRcEceElxegnjJ_ShMAm7TBF9dqz_MBGx143sgHjjqnuluDB_WRTO2BZkscL2h-9VUFeZF_X6DkiJz68ZV10dwVAd2aXrQ1YG9uCPERTUmQ7LahskVoftuwhQaiVwFLwb_e0eTRTnGUISdNar6gidnc7QMGk4CaF6ar3w_llxUSyLEhjHkW-ei_77QqxMVyqbVHq84ZIc35aMqmY2Cn3BGB8eOdunZ15FNcLDIQ1KnBqEfCXDxRAchBXSeGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=Wjw5itJZKFyuh6m5r8jdBmeaiQvnrJzKyKPlZorSyegKS-HKWgpSycGc3VqW3O5INtVmJ9UGRn4Du1ynXo-gAlNAFXsRcEceElxegnjJ_ShMAm7TBF9dqz_MBGx143sgHjjqnuluDB_WRTO2BZkscL2h-9VUFeZF_X6DkiJz68ZV10dwVAd2aXrQ1YG9uCPERTUmQ7LahskVoftuwhQaiVwFLwb_e0eTRTnGUISdNar6gidnc7QMGk4CaF6ar3w_llxUSyLEhjHkW-ei_77QqxMVyqbVHq84ZIc35aMqmY2Cn3BGB8eOdunZ15FNcLDIQ1KnBqEfCXDxRAchBXSeGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxjabJSV0VGtlugXZmuR6oZAnhVn69sNjCXZEpeL1qAB_e8wPbnQ-3okzMQWQCclUiJryx9Zg8lCi-giyCCbvegeK_dttLr9vFJ8CMAcFX7DBjfYVAay_E51BZAcYJLFKxUio_7V51q3LSaOB7tcuHk2xauXtE_EpP5qCIz7pEbUhoPhlaXjEzaYwuGQDfGqB0dxichfWA_tuUAQvrsicodxF6mQZOYvZK4nJnu-_PR_mGLwGIxJbBuDvyAdoeSS53fzOqn8PPlqxLQfpduTgYsfT4pHO4G8b9G7F1svx03V7Id0-rYrsLpkrReO5AJmoR40s4ZYPOlRlVpoO6o9Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqRymbVFQNBDid8UBuPP6c1pXUmBR4faK8ipCSQWFjnT3oMNhjh2QYTqeOAJ6kb-ytDaNLDyxeZo4YpehnupaW_AVaQUYt1S6EWLrXZO0m7FjxPRjKAEO4sDG3CqxbyiqhWu_VbAlAq9lmFyGc1Q7Kwv3MXvtTh9HjJpAIg9buKztJRk9kyAY01IiZTj5EYYwh_8plGsr3JmbO1mrvFTEQlMNoZhZILMMumi0As5u-khI7XBQkM9dnlzECXzSfR_hW1hmiAz4Gdq3rdEUpSiPEsZI0s8I_Uxwxdi_INCLOBqVTt4PBOfDWW7y-tlPaigdTDafksSXeKbc4t0hIaSLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcZ7iWjyVvESHwfe0hJfPz7L8UhbwM433ir6pNfthT7ESeyOyiTOXqgSoxH5CNdsPPiUSrzg4syVHQ5F8DMHiU6bHNztQopy-loq3QzIj-mlBMFsvTb4rBR-KSHV5IGpxOwhxpsnn7yFSryIR9PjM9wnnN6RG56hf8u1Rxwoucbht__IT7SSH5MD1USJzwG1rSybuCH3-ZPrriFxtXYZ46cHes62_qnoKAQytH40awR53v3OBRinUoS2qjq2JgvvwfiUnY5Qi56JTT8AJ7EaAMtG9luzW3cSkvhCP6Ll2GW0Uu442wNUf_405q8edOH_K9HMIPLZBTysN4UqK5e-OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=AEezezgdjhvMDFQLchUt_B1qA_4PPrFD8BsEu0jJO5IiN0fu2KT8lHxBZIz3SEiRCmX9z03YtUiHD8YC1I5dMXAEDRwrq1UfQiVfNogO90EEe4aBobpdeDrUgOWKiJYNEJOZCKOpumPvZqukLZiLbeu-giXEtDOmrmnVSF3riSu5dxn2l0unfJv8_24_J2VKFH8PC9HyweHUENC1VCANEAvOVQ6QE5JOQ-eyZoDywcRWujVV6e5LAku0LGmfdAiY0S-5ZI-lhbTMFAGkzAJvOW7d6FtQKp1igAgyLkPa6WhrvqaR9r0hWKgYn86DM6v1RHd1-p5Sgc-muT2Mv2x4pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=AEezezgdjhvMDFQLchUt_B1qA_4PPrFD8BsEu0jJO5IiN0fu2KT8lHxBZIz3SEiRCmX9z03YtUiHD8YC1I5dMXAEDRwrq1UfQiVfNogO90EEe4aBobpdeDrUgOWKiJYNEJOZCKOpumPvZqukLZiLbeu-giXEtDOmrmnVSF3riSu5dxn2l0unfJv8_24_J2VKFH8PC9HyweHUENC1VCANEAvOVQ6QE5JOQ-eyZoDywcRWujVV6e5LAku0LGmfdAiY0S-5ZI-lhbTMFAGkzAJvOW7d6FtQKp1igAgyLkPa6WhrvqaR9r0hWKgYn86DM6v1RHd1-p5Sgc-muT2Mv2x4pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiBzmLLfk6bO4-ynLb8Hbd2OlemDymZ5BdOXSTdti8gpG-CU1dE8Cfdu4JVj6rkfeNYlbp2acVhhTqzBIEm_8AnflSx3opYEbdWUWrSywBgDMb820i6fixUK0Lqv9NFx6fajS7EdRC4TAbMyMgugDnpjYaiGKPtjPftuLPTkN1_5qZIr-qQX39x9ry17yyf51dncbe-3frcKWAfbZoGlU_KEc1uGL9JWo0CAD-SqZsOXxJ8uSMiB9qBN8WK_d_co7bRY2luX6CDQmeVrPwRMw2dhlwvzczEka9EODB9FYww2FVBaYxGeBjO-Nj7TXYCQsyDlMjum3SsQpkrKwFCXlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFJEa9z-2i8t_CCt5qJ4v4PkE4s5zhtBTVKZ39Ieo17kluKmkVEuASRSi-U3lZy0xDFJKsh08vDHGS4zeyMa1A2ufmESsdKVsOnQuMBJmRGfxvhK8sDTqhRgSLbokf-E3THLLQbOIgffLaSoZPKVdXoOLTG3RczWLdKtAUDP26m0xwM3_f0ySwCGT77Y3daNbjYEXgsRp_dvm8Icantv7zH3IX95xiJTOXDfkQsVKekpTHSc0PkxuRmdtFX4dYPy4bF8x4nKxRtdXUsLaxzNIg2LsGjpPSyJFcuktoDNFxr6hwl488c_ASyf3ehd28VIzZBfrxR_1pUUykb5Kgnhv0r4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFJEa9z-2i8t_CCt5qJ4v4PkE4s5zhtBTVKZ39Ieo17kluKmkVEuASRSi-U3lZy0xDFJKsh08vDHGS4zeyMa1A2ufmESsdKVsOnQuMBJmRGfxvhK8sDTqhRgSLbokf-E3THLLQbOIgffLaSoZPKVdXoOLTG3RczWLdKtAUDP26m0xwM3_f0ySwCGT77Y3daNbjYEXgsRp_dvm8Icantv7zH3IX95xiJTOXDfkQsVKekpTHSc0PkxuRmdtFX4dYPy4bF8x4nKxRtdXUsLaxzNIg2LsGjpPSyJFcuktoDNFxr6hwl488c_ASyf3ehd28VIzZBfrxR_1pUUykb5Kgnhv0r4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=XQ8NATL9cAXMQtifp48u-faWFXkEkbDmJ3AUa6ps7Npc3yarE-aSvQl05NlCsAzEnCjbpHgdcHMlnHaKSrwN43gpYr_XpTHkxKUMTdnju7T3aH_BnyB91LSq1bcrjJnCm0f4P4CwNaHCkfJkwRW05x4jPF36D_ud4R98fNFzK96qpH7OkYca5XZVwLt4BEZdTTGU-42ajxIk10ZIwvq7IBP2tjm6CpW92wzTdckr2ZNAVLbvPL6yqk3B0DxnltSNNiTsJ5Z0UIR6eg1kJ8o5OBB3mQ_oMLHfns0xUNE1-kT3KAFTqO5zhTsjHp_qfLoHkVo72Wa0EBrP4O8D5fXp8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=XQ8NATL9cAXMQtifp48u-faWFXkEkbDmJ3AUa6ps7Npc3yarE-aSvQl05NlCsAzEnCjbpHgdcHMlnHaKSrwN43gpYr_XpTHkxKUMTdnju7T3aH_BnyB91LSq1bcrjJnCm0f4P4CwNaHCkfJkwRW05x4jPF36D_ud4R98fNFzK96qpH7OkYca5XZVwLt4BEZdTTGU-42ajxIk10ZIwvq7IBP2tjm6CpW92wzTdckr2ZNAVLbvPL6yqk3B0DxnltSNNiTsJ5Z0UIR6eg1kJ8o5OBB3mQ_oMLHfns0xUNE1-kT3KAFTqO5zhTsjHp_qfLoHkVo72Wa0EBrP4O8D5fXp8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=SzlVN-6I5WjUwjrng27YET5VD-pz1BLNGNADcR9ukR42s1-E79-lbicg8ln_h5S3Gzfu4seNs-7hSHwWU_0af19pQzU0OuHSSQBC9kuMaRpD0DlhQGSwlH43WIGJX-wY2qbQRRpjv59Vxwopbqoc2aur6HlpLO9gNC4uubYR7o21xfh8Nv-Wu0JEUuMAYTv9vcw1HTs701EQx1rB-bgubpkmZlgmGJsfWfZP8hU6BEDop2SWCb_m3KDS6eBfFQ3l03VrRPLZsZDIh7MoGBAlXpaa8VNd-0zugFKZ0zrEPHnoGVHMSXKIIeyyrV-kk5BA7ps7tTtBnTlETiJ-4naSXhLCIZ_TfkNQn-xrLViNq81eF5hxBori6eZ-6wGdvrJGWF7Z72pddm2VbSWpbL7nTNirCDFxlxAJJEruQouiCrslfLJdutCHSR1MwVq39W7g7EyTSAb35-Ti-PAoatbmlP-sIB-_hiM1itkVLrPcy8edeNnpu55CIKRZvU4L8O18N-7cRWq-oRIRyy89wNf5Qo9I-ILuhm93TQ90C25RbvYuxdysZ7xzfg9ePY662H6mhdItrO-2JUCvQU3UVmHkBnjPPDY2eV1sWMlXNohi6-X1EziqnaIyTGtpLh5c4XNv-WwmSbKiIrcp9q763ZXRohvOKHlgQKYlWmUFnlAoVAo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=SzlVN-6I5WjUwjrng27YET5VD-pz1BLNGNADcR9ukR42s1-E79-lbicg8ln_h5S3Gzfu4seNs-7hSHwWU_0af19pQzU0OuHSSQBC9kuMaRpD0DlhQGSwlH43WIGJX-wY2qbQRRpjv59Vxwopbqoc2aur6HlpLO9gNC4uubYR7o21xfh8Nv-Wu0JEUuMAYTv9vcw1HTs701EQx1rB-bgubpkmZlgmGJsfWfZP8hU6BEDop2SWCb_m3KDS6eBfFQ3l03VrRPLZsZDIh7MoGBAlXpaa8VNd-0zugFKZ0zrEPHnoGVHMSXKIIeyyrV-kk5BA7ps7tTtBnTlETiJ-4naSXhLCIZ_TfkNQn-xrLViNq81eF5hxBori6eZ-6wGdvrJGWF7Z72pddm2VbSWpbL7nTNirCDFxlxAJJEruQouiCrslfLJdutCHSR1MwVq39W7g7EyTSAb35-Ti-PAoatbmlP-sIB-_hiM1itkVLrPcy8edeNnpu55CIKRZvU4L8O18N-7cRWq-oRIRyy89wNf5Qo9I-ILuhm93TQ90C25RbvYuxdysZ7xzfg9ePY662H6mhdItrO-2JUCvQU3UVmHkBnjPPDY2eV1sWMlXNohi6-X1EziqnaIyTGtpLh5c4XNv-WwmSbKiIrcp9q763ZXRohvOKHlgQKYlWmUFnlAoVAo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=pPWXgFQTq8LjnzOpnc7GrTytuUi2OzZrxolew2hwTnH5ZXNUDzEEF534D3tBddy9kl6z9xjLRzfqbkAys1OIgZBcucfmVPQWKWdpV7qFhBk4U0TxCjTA7YSPWLL67vbXcFUQJlYEfOy3MTRwiMluZRGjMKD8P70Ib8jh2c-N0LDg6f-GzQmd7ikVTI-ur5xi3QV5yL_12kCCTU4kekwcSlBkaphm5LmFxf3GLANKNVhOGKiuqeocKMppoQokesdQc5vT2ooSgAnOZHZzVUK4Htm2OUwkhqgQ66cMrKYhX0Uw_jh9StcGt0fOCKqYUrVh-TZABDe7SAPQK7vaeeXHRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=pPWXgFQTq8LjnzOpnc7GrTytuUi2OzZrxolew2hwTnH5ZXNUDzEEF534D3tBddy9kl6z9xjLRzfqbkAys1OIgZBcucfmVPQWKWdpV7qFhBk4U0TxCjTA7YSPWLL67vbXcFUQJlYEfOy3MTRwiMluZRGjMKD8P70Ib8jh2c-N0LDg6f-GzQmd7ikVTI-ur5xi3QV5yL_12kCCTU4kekwcSlBkaphm5LmFxf3GLANKNVhOGKiuqeocKMppoQokesdQc5vT2ooSgAnOZHZzVUK4Htm2OUwkhqgQ66cMrKYhX0Uw_jh9StcGt0fOCKqYUrVh-TZABDe7SAPQK7vaeeXHRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fysO5Xr6KBW64g6Gul7OREXEWiXhQrkS-nFbLKeH5uaHB7RftWwFX5r6f9m_qIH1OSiJTfovrTNVYmuYB3pe-qFJ9wm1ApDpLX9AEJyYDhJyVvt5Jjo3Mp_bPrXT0GGdG6jPAx5plZJWgPHUavhhSmWCiYmbUDijI2bVWmUU0mMEjaujFcbsK6vYHf4OajT2Fbj17azpVuVvgwASxNddOog63ODgAmkGjodR0u0ar0WzTHsJpaOe9Iq4JATauwO9sBD3TADhwJl7NKPdR-Y4fKpRMCZnRqZoW4PJvSyCnXtMX-beoOco5q-Zgv3koeviXRNLi0P7l29akss2IXkrkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=KnSLkAV-BIBm77crqc5mOHPYj5xD92PYMb5oadywBq3mZyMbWnfOMfzhGiQgfQQ5EDyTqA3a6xNIKg6pfdIYPkozuIR4Z8jCmZECuMawLsuwLqTDVGx0Jr5HGDd-Y3nhGr4Inyn0gyzZ0le3N5lwog7sBnbRrKwy9Mj9_mkqmS2ikw24w2WbypH6T7JokRvHBqtNso8d78UKZTl86pELZIo5FNL2qhoEXd8EUCC3jpWpuph_GqycAvjIot8YoiRftB-CprQeXybqLIC2NOeHsv-EOVoi5ckcTgtt4ebYNEaFO7o8uKqFt6G-SUoHe_q76qO1t9z4PINUuFcNkNtwMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=KnSLkAV-BIBm77crqc5mOHPYj5xD92PYMb5oadywBq3mZyMbWnfOMfzhGiQgfQQ5EDyTqA3a6xNIKg6pfdIYPkozuIR4Z8jCmZECuMawLsuwLqTDVGx0Jr5HGDd-Y3nhGr4Inyn0gyzZ0le3N5lwog7sBnbRrKwy9Mj9_mkqmS2ikw24w2WbypH6T7JokRvHBqtNso8d78UKZTl86pELZIo5FNL2qhoEXd8EUCC3jpWpuph_GqycAvjIot8YoiRftB-CprQeXybqLIC2NOeHsv-EOVoi5ckcTgtt4ebYNEaFO7o8uKqFt6G-SUoHe_q76qO1t9z4PINUuFcNkNtwMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=YyPF-pPr9iPG1NKQoQoMNwoIltykZDZ_r9_X5X9ss4eHFdjP-bo7U9yvNh5oULlStodVfrPPh0rH_jjjFvabxaBOyNn6c_uVXbAiIU7YLAdOrZDpBhwNHnPLK1irq4j1EPCDUf2ikSIWkEt51kRJVgmmTYsbcjmF9i0mblJ7TV9hllaSY1v9mYyVNKRe24trV_iFfODTYQqfCk24L9_T78eJDbd5iuaItV2HXubGpcyWFoONKPly-Tc76VEgVdnPkAMoTLK8RPkvJJ1air7S0zSRUxOrXdKupjpfcUnafy4STyYZHUMb0I4KTbdG0XZSpdV_8dJHRx62RZX8oHw5GmUOhNn7YYnmoKvwFm0ti-dBQ9CmNKmzHGEeZroiohbuUflEBSt8KSnYE_C-D84Vm7lJLrBVRRP-5jCqpnsHsKGMHDpPsx7et1lThM2gwHvSX838YCmdSNBFERrZO4WdYn5GNRgdjeS0NENAswOCBbXypV6xns2HoAEXEq8OiOQHBVCVm7o9hP4HSwVS0_W2hnceFzxL46SvqL0xb-obY62IFUrMShFE0CpHWSAv_0fV3GJjU11Hy5s3lTDxkezTQwwChY78w9vc9ZYTNnT22SAsODhOzBvQEdAL0Yvea97Lbc_7hSrAVnn1DOg5t5dtfq5I767iMT9_hQ81MLe7dbc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=YyPF-pPr9iPG1NKQoQoMNwoIltykZDZ_r9_X5X9ss4eHFdjP-bo7U9yvNh5oULlStodVfrPPh0rH_jjjFvabxaBOyNn6c_uVXbAiIU7YLAdOrZDpBhwNHnPLK1irq4j1EPCDUf2ikSIWkEt51kRJVgmmTYsbcjmF9i0mblJ7TV9hllaSY1v9mYyVNKRe24trV_iFfODTYQqfCk24L9_T78eJDbd5iuaItV2HXubGpcyWFoONKPly-Tc76VEgVdnPkAMoTLK8RPkvJJ1air7S0zSRUxOrXdKupjpfcUnafy4STyYZHUMb0I4KTbdG0XZSpdV_8dJHRx62RZX8oHw5GmUOhNn7YYnmoKvwFm0ti-dBQ9CmNKmzHGEeZroiohbuUflEBSt8KSnYE_C-D84Vm7lJLrBVRRP-5jCqpnsHsKGMHDpPsx7et1lThM2gwHvSX838YCmdSNBFERrZO4WdYn5GNRgdjeS0NENAswOCBbXypV6xns2HoAEXEq8OiOQHBVCVm7o9hP4HSwVS0_W2hnceFzxL46SvqL0xb-obY62IFUrMShFE0CpHWSAv_0fV3GJjU11Hy5s3lTDxkezTQwwChY78w9vc9ZYTNnT22SAsODhOzBvQEdAL0Yvea97Lbc_7hSrAVnn1DOg5t5dtfq5I767iMT9_hQ81MLe7dbc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7mylopo1RAVUHq9snrt2Tb_VUYPtzGhR3qeXUmrm-Z4iA5NLcBbD3VszQos3EMIxH5uwdJazr64XEPNKRdkRKSYao7muaiD-ZL01Qxa01-zO3oWGndjkwpDiuK0dTWxps5lFbHgTQK2X2RXtmVzoy9dAZx9LuEzXF1qH5aU4ZdhiPf4k4bVu5Nn_Ho7YzPZHpNz9fpqM0MtbPdIW47SSTBKoiPldDs8rLvAcIvGYAPqgURfDpaLJ7tWHWbiL_yUhtI4OsnOsjQ4rTwIjIZ_0JmIQX7Ox4Qri-u_-rqWanhZeHltetf2UF5pJSZ7x-XFvqmDFq1Db5AkzIOWW5zqjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=NrWEnkhhwGdcEXftmIHFJQcerNsVVizD9-FIo7YuWeaReed77TFsVXNO_g3H4uMklLifVvY8oNUwjJJwviQTcQ9uC6Zcoqlvj5GCyEPxMtSN1jp6Zp4-XGEMPY84TznlljVl1CxH98gLfkOy9RJMSqBtD1RGpcGVFhpz6FgwB8lPzjjiz_FrJcSwGwNVIRB6Gi0xzgZ4Lj3Cgxx062TU8hMnm_ACiQRSVsYX_qtDOfGhkr_-4q1qOuabHXfhywUCE3e6Ivc0ftdz1n0qV0D3OObO1gc99Ei6WCbb_6CDQdalZWRb8AoOlcf8TbPFo5nTb3xhCbu63Fpw6X_X9Y1ALZAzevPkZZvkpiEzGVO5dhDUGFbmde7ViYYQfiBYUnSXMgcykVFBayrtTwPjTuz5IGaePtsxiyTmxJj7sWkLUk9HLpI6pB-NGzyq5Svec8T8Sb3DZ6Y9n8KlcQYFVDnP1AE_FwFor2dJI_PbrJqga7KqY2sNSG5L2ylhJZrRqOvxk7aNmpGr8R8Njbb9AtQAq04TE1SupUMXxyKkkYlo3PeiJh_kwGu5SNcR8yuv7CIou5VAq5qScuq_t3tE7CiZUqXwGCYnHnNs7vLitiu5OLiv6havHNmHNaUQwPNpWtLXVp8sc5PtA9zZSniZaMBCROwdp6-grYji4N-WaPuRtgU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=NrWEnkhhwGdcEXftmIHFJQcerNsVVizD9-FIo7YuWeaReed77TFsVXNO_g3H4uMklLifVvY8oNUwjJJwviQTcQ9uC6Zcoqlvj5GCyEPxMtSN1jp6Zp4-XGEMPY84TznlljVl1CxH98gLfkOy9RJMSqBtD1RGpcGVFhpz6FgwB8lPzjjiz_FrJcSwGwNVIRB6Gi0xzgZ4Lj3Cgxx062TU8hMnm_ACiQRSVsYX_qtDOfGhkr_-4q1qOuabHXfhywUCE3e6Ivc0ftdz1n0qV0D3OObO1gc99Ei6WCbb_6CDQdalZWRb8AoOlcf8TbPFo5nTb3xhCbu63Fpw6X_X9Y1ALZAzevPkZZvkpiEzGVO5dhDUGFbmde7ViYYQfiBYUnSXMgcykVFBayrtTwPjTuz5IGaePtsxiyTmxJj7sWkLUk9HLpI6pB-NGzyq5Svec8T8Sb3DZ6Y9n8KlcQYFVDnP1AE_FwFor2dJI_PbrJqga7KqY2sNSG5L2ylhJZrRqOvxk7aNmpGr8R8Njbb9AtQAq04TE1SupUMXxyKkkYlo3PeiJh_kwGu5SNcR8yuv7CIou5VAq5qScuq_t3tE7CiZUqXwGCYnHnNs7vLitiu5OLiv6havHNmHNaUQwPNpWtLXVp8sc5PtA9zZSniZaMBCROwdp6-grYji4N-WaPuRtgU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=V1Kov6hSWE9H-qszA5lNRLkX_6V2HnyyY4GpTAsZxbMRfiUClN8nqGae8z2jfoD07c0VJcnDxWiawEYVNfuYgJEUtB9nwDH0JQpzw2fIws3mY2-fI3G9ceRBNUikpNPXxQnocQLUO17606TK_Y0SJm0deh5M0XpxNfs98dilfv3-FCgT4r7eNHFe2fRTfe_YplMIye97bZBLxMacrLpfRiKBZHt-yUq4lHOkR8dCng964ImzPU-BGTHKzJfZUOaCj7GOQyraCDzg-w5Y23O6yGZ7bmHgHyrR-CGTmTmaP-s3X2f5dD9x0RPf4vtlJil9qzVKhCcSHUG2DBearsMQ72vSQKexkKvJvh2JtYzuPKspp1q-2fF7MjEmRjCc7a03rq9vPcjVair0TmS84HOwokCjfKPh6mc16M9Mi3XpM3FT-MLpIT3SF4T1jioL7yzFjwCL5kPh3TRAWpEiOay35ea71AeCvS0o_0dEPMMz4Wi8bp-o2VoP8CrHS4_r0K08ZK7hCoFzEdUQ0pR4SPDRYAdO7qsOvl4yH0i2mfpt39pb6eEPP-yjqzn-TnP67hOToWxmFW2-TshGeQWIevRJ7ILJFFNUf7Vzj6Ba4QR37gm4T2h8NBAkgpUVXelzA2dKNySoH3cgM-z0Mmcdp-j5Q4NMNjcAbWXXo8LiBpmdoUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=V1Kov6hSWE9H-qszA5lNRLkX_6V2HnyyY4GpTAsZxbMRfiUClN8nqGae8z2jfoD07c0VJcnDxWiawEYVNfuYgJEUtB9nwDH0JQpzw2fIws3mY2-fI3G9ceRBNUikpNPXxQnocQLUO17606TK_Y0SJm0deh5M0XpxNfs98dilfv3-FCgT4r7eNHFe2fRTfe_YplMIye97bZBLxMacrLpfRiKBZHt-yUq4lHOkR8dCng964ImzPU-BGTHKzJfZUOaCj7GOQyraCDzg-w5Y23O6yGZ7bmHgHyrR-CGTmTmaP-s3X2f5dD9x0RPf4vtlJil9qzVKhCcSHUG2DBearsMQ72vSQKexkKvJvh2JtYzuPKspp1q-2fF7MjEmRjCc7a03rq9vPcjVair0TmS84HOwokCjfKPh6mc16M9Mi3XpM3FT-MLpIT3SF4T1jioL7yzFjwCL5kPh3TRAWpEiOay35ea71AeCvS0o_0dEPMMz4Wi8bp-o2VoP8CrHS4_r0K08ZK7hCoFzEdUQ0pR4SPDRYAdO7qsOvl4yH0i2mfpt39pb6eEPP-yjqzn-TnP67hOToWxmFW2-TshGeQWIevRJ7ILJFFNUf7Vzj6Ba4QR37gm4T2h8NBAkgpUVXelzA2dKNySoH3cgM-z0Mmcdp-j5Q4NMNjcAbWXXo8LiBpmdoUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=Egxjom7uNE87GNYTLTW_bG_fvy9iOJ5YBz77q7gYewhtFRXAnDW503a5fgqunPEhqF2u-zr8gzUo078qMGfwUV5cWVgo92VJ8s0DF7bVbd7sqfi2Mz25h1h_1ZvO4ft1z5Uy-bVymXXrIsGedsswYQxZrPra3bdraB0cC328nof5qDu4PhD_x_jGCwyeTllvLr8spaTtwu15KsRWaZrZtRS_at7m_QjsjQoa_OzIZYiBSESE_HLKlwWDgd1NPiPY6i-4cNEHm0W_oMjkqhZnY8yBoOTmKZhGPhqLpjAf8A-SvTP5eC5182X3tZ21EdWg8DRc39qKXsJuSclPFO4lRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=Egxjom7uNE87GNYTLTW_bG_fvy9iOJ5YBz77q7gYewhtFRXAnDW503a5fgqunPEhqF2u-zr8gzUo078qMGfwUV5cWVgo92VJ8s0DF7bVbd7sqfi2Mz25h1h_1ZvO4ft1z5Uy-bVymXXrIsGedsswYQxZrPra3bdraB0cC328nof5qDu4PhD_x_jGCwyeTllvLr8spaTtwu15KsRWaZrZtRS_at7m_QjsjQoa_OzIZYiBSESE_HLKlwWDgd1NPiPY6i-4cNEHm0W_oMjkqhZnY8yBoOTmKZhGPhqLpjAf8A-SvTP5eC5182X3tZ21EdWg8DRc39qKXsJuSclPFO4lRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=h11A-Np9czSHdKonjHK3yD455v_Ap2_q7a71PBLW2yOH7wfuYlcEJbANpfwZPuoPU-MjYtrmXyF7z6zM-qnQAxYOayPZb5guFMkXXmcdlMsOfzKVgww7xSjhciZ0r4Vhq-TAPI7ScAOLwuAwygfPVBZt9ruVysM3gkPd_JsUGBW0PNxFAyQVhiE_5SEVU3zshT9xSf_2TO5HHZKPhwu72xziSwZ6TycEn53EnP7PuVftDKixf6hn9aVDpqU7tQd28WdKYUGra_UM2TsUD9HAa6Jk5HUm4l4RA5QH2TE_40DaeHxTeOEO_qfeO8DLo4BRDGwT3VAPYP1e1rqmFjmpZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=h11A-Np9czSHdKonjHK3yD455v_Ap2_q7a71PBLW2yOH7wfuYlcEJbANpfwZPuoPU-MjYtrmXyF7z6zM-qnQAxYOayPZb5guFMkXXmcdlMsOfzKVgww7xSjhciZ0r4Vhq-TAPI7ScAOLwuAwygfPVBZt9ruVysM3gkPd_JsUGBW0PNxFAyQVhiE_5SEVU3zshT9xSf_2TO5HHZKPhwu72xziSwZ6TycEn53EnP7PuVftDKixf6hn9aVDpqU7tQd28WdKYUGra_UM2TsUD9HAa6Jk5HUm4l4RA5QH2TE_40DaeHxTeOEO_qfeO8DLo4BRDGwT3VAPYP1e1rqmFjmpZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=qqW1z1QVzweLaGt8IvKLt_niSpMV_36IB3Kt0YWfEpcK5sEgQTt8iFc4NpZPnA1OOxCXvJqUaWXUARIUzTQRjcsfpsSVumLlQT4vmllXP1CGzqk3Yo_foqeVnhLeRbJdoK5hini3r5du0rFm9WkPi8wIL1B7w9JRMkPdHPd7_fR71CoVwndortFim8-X2RsLhjdaHO6XIzqb7vvozTH3QfMW3ow__RZLaJh-3p6MKwRB0YjRylyAzUA4HwZFCcslb6bUnPA8CAONmQ5Ubyd-XUZLRpi9uvfkhfj0Me26NmfZGdEeggCv3HXxzO5qq9PuPBov_yDMNfgCVMOtMMerAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=qqW1z1QVzweLaGt8IvKLt_niSpMV_36IB3Kt0YWfEpcK5sEgQTt8iFc4NpZPnA1OOxCXvJqUaWXUARIUzTQRjcsfpsSVumLlQT4vmllXP1CGzqk3Yo_foqeVnhLeRbJdoK5hini3r5du0rFm9WkPi8wIL1B7w9JRMkPdHPd7_fR71CoVwndortFim8-X2RsLhjdaHO6XIzqb7vvozTH3QfMW3ow__RZLaJh-3p6MKwRB0YjRylyAzUA4HwZFCcslb6bUnPA8CAONmQ5Ubyd-XUZLRpi9uvfkhfj0Me26NmfZGdEeggCv3HXxzO5qq9PuPBov_yDMNfgCVMOtMMerAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=RLcE8Mios9kdFiwqZ_8H9ApC6QSny4s1W5JrzxXzqBpaq510u03eXLGAz9wKSP3MSm7nJGjkOCW3s5O10avXbStJnBRjM1uSMEQ34MRFMinXUSx4eDASyKuDhvJitPokIjeDzP1vf4rkOki4J60OpzgS_YowNbr4z4Xamc4nOV3Ge-O3b7bb9TqcTZ8Vjze4r6whWBU6IngFfTVCnAcjVd1cSrANbCcZWCxDp80CaCA9VnBoA8U5_Gtpm_fbmWzDsoYvhmx5ro16gZ2iFtjdZR5r63-SBPA2BUPg9griPg9EgclJrj-TJyFCz5mZ7DBfM8XwSG2nvQnTY-pv-O7kjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=RLcE8Mios9kdFiwqZ_8H9ApC6QSny4s1W5JrzxXzqBpaq510u03eXLGAz9wKSP3MSm7nJGjkOCW3s5O10avXbStJnBRjM1uSMEQ34MRFMinXUSx4eDASyKuDhvJitPokIjeDzP1vf4rkOki4J60OpzgS_YowNbr4z4Xamc4nOV3Ge-O3b7bb9TqcTZ8Vjze4r6whWBU6IngFfTVCnAcjVd1cSrANbCcZWCxDp80CaCA9VnBoA8U5_Gtpm_fbmWzDsoYvhmx5ro16gZ2iFtjdZR5r63-SBPA2BUPg9griPg9EgclJrj-TJyFCz5mZ7DBfM8XwSG2nvQnTY-pv-O7kjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=R1HBHQSuf8wEEP12EMJ2CaEzgQCa_Y7Zyh2KMstXuL3hDIJxKdQkAMDKRI00GblST0MTqt3aMc5XfILkwJ5EkemgRNLW2SLTZqiH75sOgpI9rNL1RVZjpG9ec3gzX_bFKHDPaYQJ5K5UufbmW_UgTrSOF_g_sfrNUaqiLCC2krRDuUdxNsZ9n477LLSUGa_7ufR7FneG3TBHGhKOGkbh2SMj7ovsWgYkFteHr4Lh3qxuV5tlwURyBtS38r55Uj6Ek-RHeGhhtHF_qGJU_vUcR06ckgoNE3M0DX6BEYh6ZGNkOWhJGPf6jM-L4cr9RIIOz2Sf9romP18iKzkjHvArYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=R1HBHQSuf8wEEP12EMJ2CaEzgQCa_Y7Zyh2KMstXuL3hDIJxKdQkAMDKRI00GblST0MTqt3aMc5XfILkwJ5EkemgRNLW2SLTZqiH75sOgpI9rNL1RVZjpG9ec3gzX_bFKHDPaYQJ5K5UufbmW_UgTrSOF_g_sfrNUaqiLCC2krRDuUdxNsZ9n477LLSUGa_7ufR7FneG3TBHGhKOGkbh2SMj7ovsWgYkFteHr4Lh3qxuV5tlwURyBtS38r55Uj6Ek-RHeGhhtHF_qGJU_vUcR06ckgoNE3M0DX6BEYh6ZGNkOWhJGPf6jM-L4cr9RIIOz2Sf9romP18iKzkjHvArYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=qytWd7LE85UBbMvf9dEDLamwp4VV6kWbeFNYRh3aqnrpN5XuTeoR4OwJdvD7SSbxUcIkqL_f7vykATEijFwAExV9hb_D-kqHHMg1Vsy2PzKBAjFs-RyxsW_wRs67jUJv8o0-dwDcRi-Lv3tIxZzqqrSb2zwPSEQRWszcJsq6VOShdAJC7zdlAo7N6y80h9ocGIJ-BIDEAqZMhdMCFBsRpXmjyGoyga1MSLCFTQG_auF4T7XHLbcprq1jpuYccygkZ3hfU76MjlGtrl4NLv-hPNf_AT_6qaPwGemdln09_FOhBDVE8mR_Zdj4u58Jahfqq6QsnAZeGp4WEL783oUlDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=qytWd7LE85UBbMvf9dEDLamwp4VV6kWbeFNYRh3aqnrpN5XuTeoR4OwJdvD7SSbxUcIkqL_f7vykATEijFwAExV9hb_D-kqHHMg1Vsy2PzKBAjFs-RyxsW_wRs67jUJv8o0-dwDcRi-Lv3tIxZzqqrSb2zwPSEQRWszcJsq6VOShdAJC7zdlAo7N6y80h9ocGIJ-BIDEAqZMhdMCFBsRpXmjyGoyga1MSLCFTQG_auF4T7XHLbcprq1jpuYccygkZ3hfU76MjlGtrl4NLv-hPNf_AT_6qaPwGemdln09_FOhBDVE8mR_Zdj4u58Jahfqq6QsnAZeGp4WEL783oUlDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=MBNt9qDp18fxE1TMxYWJ2c7PsyCIAD21wAHgSI1LClJmIqoslat0QQNVry6eyKIajjnLnch0lCtEnWKBWVt1nQVJ7IdZx5Dj-HCHTUqrm6gsZ8LST7i1yNEwEKVKF8JOjJtWwOzZladSUYBayuKmXu9xTscPHVnF3HFtXDoSQfUSJ5YuXtUOVT3Q9Cg7ejr3RMbLBhH9m3Tpz3fZFWsAQUwToDszV3Nfz2-kpx3sDgsLYvQu6pkbnHw3_doQ5MxM-TD0ggbkyXH2go-KGax2bJEUohiMdx9ZPTTStqwD9SUWTV0VOlJffxd0scPfnua5uCqhSwmsk9LbdLzmt9pdww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=MBNt9qDp18fxE1TMxYWJ2c7PsyCIAD21wAHgSI1LClJmIqoslat0QQNVry6eyKIajjnLnch0lCtEnWKBWVt1nQVJ7IdZx5Dj-HCHTUqrm6gsZ8LST7i1yNEwEKVKF8JOjJtWwOzZladSUYBayuKmXu9xTscPHVnF3HFtXDoSQfUSJ5YuXtUOVT3Q9Cg7ejr3RMbLBhH9m3Tpz3fZFWsAQUwToDszV3Nfz2-kpx3sDgsLYvQu6pkbnHw3_doQ5MxM-TD0ggbkyXH2go-KGax2bJEUohiMdx9ZPTTStqwD9SUWTV0VOlJffxd0scPfnua5uCqhSwmsk9LbdLzmt9pdww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IILrCWMMOsuzbgORbAtXAV5xnkmfkMQWrmf38TO2HDgRPRGfmzyefBDsKGrGswtqx06R2gPFgEX-ihBvBjkCgQBV85vOXimEr0w8VgcqPvNqXG12lB0BGjjes9glczU6UnXWKrskv8m3v7nhhBNnEYB1qpCnJQnjtK25xMOkQ4uktpr1sSepNlft36gsZ9RjtRmIlKkEMAwSI1XSgLA7xAKyzNsPmQGsm84d5sl2g69ir1hYHXOcDlWRhkpeOcoFlED_Z9ImUmsW8njWygqXuRFiRHVCo6aWZXIHj6yTYmm8eWnBShWzdUx7HDPJFngYjIQOSQFhpKiQBpimM7DzPQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=JUEqsmMz-NvYgSwrkgCZb-z96H1tGMNaee925Eep07I5jV57M1B4L9Igawkp9YR-A4KsuHnlqKJPSnnNxpW7iT-1bmFTU7TWZJ8rXcCFf699kQMUM4fSulMDk9mmCsa1Tn7BMcDDCey6cUCVC060_zPQOm4DUQK7rPaDqfYntrArDCh_Hn46HXZ3LVNxPevP4dG2wD_gHCX3nFWzynZNcEPqUzMjSin4Pwjl2Soy0lv8cNjBBRJR-TEs8co7TV0hwuyWa57Ejo1ovSu6jJS0omkldLIWrHeB_bwYK2AAAluoLa7yRATJ-EmMWMwv9oZa6eIxUsJrTQAhHe4R9Ik5Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=JUEqsmMz-NvYgSwrkgCZb-z96H1tGMNaee925Eep07I5jV57M1B4L9Igawkp9YR-A4KsuHnlqKJPSnnNxpW7iT-1bmFTU7TWZJ8rXcCFf699kQMUM4fSulMDk9mmCsa1Tn7BMcDDCey6cUCVC060_zPQOm4DUQK7rPaDqfYntrArDCh_Hn46HXZ3LVNxPevP4dG2wD_gHCX3nFWzynZNcEPqUzMjSin4Pwjl2Soy0lv8cNjBBRJR-TEs8co7TV0hwuyWa57Ejo1ovSu6jJS0omkldLIWrHeB_bwYK2AAAluoLa7yRATJ-EmMWMwv9oZa6eIxUsJrTQAhHe4R9Ik5Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=qmVBAnJixGr5OE7tf89Xt621O5BLeOUJbRoGX1NIBv-B_rmFBca57q0EqKiacorb9HO-GWJErx51_thlnH1mE9amAEtsxCAsCtClIKCoNSHhmtOz6EpjpF9KWtCNT4KwuEZWfijxiCm4Owwnwmbz7dhTfCjDbc5vQNaP8f40ezR1M2Yxvl726AheRqoWY28nFNWLYO7wDAM2xqX36QiPJ-OeY5NKN3toqLLvSO4g68EUDLU6IEBEqvqgmun7GbLo_G0kbRa2G33xilNWnzRprrOATLymv1O2MWgRHHYNL6sjz73LOn7r0rbNOzI83OzRkQIeRe2OgcNSi3hAVG2ulw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=qmVBAnJixGr5OE7tf89Xt621O5BLeOUJbRoGX1NIBv-B_rmFBca57q0EqKiacorb9HO-GWJErx51_thlnH1mE9amAEtsxCAsCtClIKCoNSHhmtOz6EpjpF9KWtCNT4KwuEZWfijxiCm4Owwnwmbz7dhTfCjDbc5vQNaP8f40ezR1M2Yxvl726AheRqoWY28nFNWLYO7wDAM2xqX36QiPJ-OeY5NKN3toqLLvSO4g68EUDLU6IEBEqvqgmun7GbLo_G0kbRa2G33xilNWnzRprrOATLymv1O2MWgRHHYNL6sjz73LOn7r0rbNOzI83OzRkQIeRe2OgcNSi3hAVG2ulw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=gPGehNPYp1_TgPxYuc08aNHbtbtFldfGp4zBxr1hN2ILMCmndRG8i4nWJK7bfyR6uNcjYHDBwiDhzpa1t2kC3tQSS18Z87nbTTetE-w43Ei-FCSUnnF5Pl5rW91i005hBTvT-dvcL0ievsIatjRElrhAuG6ACF4G-sPqWIWbcdbwBbo7qfZuKDGzSrQ-qT25dm2OdFT55b8fPBx0A1HxT6VyTcqmInGAJgHdbLia1NNhtJ3FlmMHxu1Kz1MTmvSnO_XPoqwR4FgRR043qEGUHjS00hp2llu3_iuutO0ehGg4Jf7KFJxgH2dasnnj-bEoEqqdEKwIr6gJHrhlWJHMwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=gPGehNPYp1_TgPxYuc08aNHbtbtFldfGp4zBxr1hN2ILMCmndRG8i4nWJK7bfyR6uNcjYHDBwiDhzpa1t2kC3tQSS18Z87nbTTetE-w43Ei-FCSUnnF5Pl5rW91i005hBTvT-dvcL0ievsIatjRElrhAuG6ACF4G-sPqWIWbcdbwBbo7qfZuKDGzSrQ-qT25dm2OdFT55b8fPBx0A1HxT6VyTcqmInGAJgHdbLia1NNhtJ3FlmMHxu1Kz1MTmvSnO_XPoqwR4FgRR043qEGUHjS00hp2llu3_iuutO0ehGg4Jf7KFJxgH2dasnnj-bEoEqqdEKwIr6gJHrhlWJHMwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=JN_UJQqr2Y0E8WpBTeViy5vzf18FSND07s-OMXu33-bynNeK8NRi6yMUeq_r4qgfBzUhwAIj3tg2wElGyzFcFcTx5KWgUUB0dYMHl91IL3eof7NzAv--vVJnFBLSVrsucSCwmlhIKFHxy4bd_AzVg62Q_kexmyhO-nt7KNHnmSyvY7CfT5xCdmwhaYZyK32bhG9WaQiEo8dECWWgH_0-sBifatcoCzZl1D2SOwQWYHiG1c-y6KkI8MOQPJrRTPqeBd9WZgZEJIlLlYG7C_xpdjjCl3g2HNDGCbEV13rWK8HhLAmvI0QgNb-ZCNzcc5chxAhHkx2ZWuuex2O_MULiKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=JN_UJQqr2Y0E8WpBTeViy5vzf18FSND07s-OMXu33-bynNeK8NRi6yMUeq_r4qgfBzUhwAIj3tg2wElGyzFcFcTx5KWgUUB0dYMHl91IL3eof7NzAv--vVJnFBLSVrsucSCwmlhIKFHxy4bd_AzVg62Q_kexmyhO-nt7KNHnmSyvY7CfT5xCdmwhaYZyK32bhG9WaQiEo8dECWWgH_0-sBifatcoCzZl1D2SOwQWYHiG1c-y6KkI8MOQPJrRTPqeBd9WZgZEJIlLlYG7C_xpdjjCl3g2HNDGCbEV13rWK8HhLAmvI0QgNb-ZCNzcc5chxAhHkx2ZWuuex2O_MULiKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItOzikZizivLiSMZJkg_FYPWdErTQrzSWVsS5lWqf8BhN9EldAWEnp5optBeuxw5WG3yP2b9d3Uj7KpF9Xha39x4PB0fdtWJCtKdkWYsLf4YbyNnj6wwcyBTbn4SCTXCm96xUe_WfqfobxM77fJQGCMMdiCX3Qt_rOgHhM30dywCbxEUjcUi5MjYXrrCE4fyBV_RU3ff3YNDyvItVuK60L56ePT0XZ3EW-bCZJHbTSxg3CIm-pZqKrhkbjYBTHDOKvwNgYKrNti8LztawmP9wCqbSYjav7fpahKx8bcmzuKxUgziSUE1n6M3lbuuhWMX-8-yR3YtUUPJKNS5MGrbiA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=nWFcvl4wOnBdLJN5hNYodXKuqFN_-EmwV4QvLO0k7rQDMGnlQtqNAzhy5Gk4flaf-gtlB_Clkn_L2rpTqYt6Tb8ldsdY-BF790qO4610LyqW2y8btmD23PPZZSoqysdxP587fWx05aA7S5cTdNXB3Ze4XdOeMrQyoj6UIlMYLjwjHRwZ9QW0lSNsu_E-0Da70Golvj3gPKHuqM07i66IIgBMYFxr8SbyneQTyuWvydn9v-i_KIsR8q0OA2FVszgVjzC1V4dTU_XKUrM4I0SGoXYFkmeQkjhb4lVSPcU_uHHpca3lYzfObztSkL_203YlLZQxkNIZc1FtgCb9xIN3GDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=nWFcvl4wOnBdLJN5hNYodXKuqFN_-EmwV4QvLO0k7rQDMGnlQtqNAzhy5Gk4flaf-gtlB_Clkn_L2rpTqYt6Tb8ldsdY-BF790qO4610LyqW2y8btmD23PPZZSoqysdxP587fWx05aA7S5cTdNXB3Ze4XdOeMrQyoj6UIlMYLjwjHRwZ9QW0lSNsu_E-0Da70Golvj3gPKHuqM07i66IIgBMYFxr8SbyneQTyuWvydn9v-i_KIsR8q0OA2FVszgVjzC1V4dTU_XKUrM4I0SGoXYFkmeQkjhb4lVSPcU_uHHpca3lYzfObztSkL_203YlLZQxkNIZc1FtgCb9xIN3GDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=USdcm-UO4FzYXZ3ElZ6fN34xMJIvXC263_8fpimkSoacSdnP5NKCMZaMnilsRPU34lO6y4ZTXGu4V1FP5CpMDqTtpdS3XOGArV3rjmHo5Ly9DuQXAuRVl019GszWLH4sczFnrffZNRIipQnpk4ZSo7w6DTyJANU0HwEXRGq4o1JWNspg08ERT6Q8NBFOZF2LyIduJh0bNX1HF0p0t_ij5VB1NS4ztODVGY_LThsICy2HLi6_Q6x-v9hIT6QWxxL3_sp1VjZDIycuc6herqJ_pBuDzK6Qm-0lgBoGa8JCydGZ8hudwznIApahZbiFesZrc0bhwEuxvR5Iejtz1r25uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=USdcm-UO4FzYXZ3ElZ6fN34xMJIvXC263_8fpimkSoacSdnP5NKCMZaMnilsRPU34lO6y4ZTXGu4V1FP5CpMDqTtpdS3XOGArV3rjmHo5Ly9DuQXAuRVl019GszWLH4sczFnrffZNRIipQnpk4ZSo7w6DTyJANU0HwEXRGq4o1JWNspg08ERT6Q8NBFOZF2LyIduJh0bNX1HF0p0t_ij5VB1NS4ztODVGY_LThsICy2HLi6_Q6x-v9hIT6QWxxL3_sp1VjZDIycuc6herqJ_pBuDzK6Qm-0lgBoGa8JCydGZ8hudwznIApahZbiFesZrc0bhwEuxvR5Iejtz1r25uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WgrZEMmSLnC0TK3uGqdpXaTXZk8hLedky0Mi5ROU5oGQbyse9rCLD17MjEB3so8zt4ThLGQQz79lwWnc47rBxuYuV0mrlEw39LVQM1bn27lyXnnMDqoD3Tf2v_xT0GSvwRFy2N_Rr3x9JSzj_2c7vOUG5eMoDUmMSlGs5uQQe2GDqE97yT0PUy1PJEwLoucnX4aFXZuEEaFPXgKkiEllgu9i2FSQetiJGDqPERToq4KmEfxmKhmwH5g2NSju77NTLGtfM3h5Ki5R8JBXmF2Rn87EP8cnTfb0ZnWalfTrvUv9RzDSmqCdyqcZDhQJiEvN_yQXcRFbNLmuBmwOyffGSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cTF-VuglxEq7pA6zQt3gcWtqMtW3WidEZxmUVGUpxs0u-XVJPlw-8gVlIa9rV8VFoqWHzVY3_O6YJi37wldBziDhSt_btcw4UItGVpuBB8epYGQJpkKd35HOFNGc3UZmkg6_IDLwXn--XUKhjYCNgtyxV36g2shPGMRYXupzwyuSp3uL3J1NfGAaawUfRs8UDt6-eA8HV2zuagegN_ASzPo4Mr11eK2FkcjOjGkhA9xdyBuetSqxzkUOt4N5YBqUBGkAtcjvh5EKhns7f3VIkbJpUYGdv5FuF5ePlzdy__-uI9aMn3cI2wVqDNuI_EV__BdNY8nrjsMCIEzECNQ7lg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=CSNk7nn-aZvlN6EoMKg6iq2pD94Snssl4_7vyoZR4b-EC9xXQD6hxFcKE_taL4e6Jxr6wXepRv_4zwNcnpOVKBO9OCnq1I4caMYQIyIc1I-3JE38B37-HEMHSE4Xitbi8WX5OmTn-B91m_38ydBvZ2EAjQGbMsGd1ysfW1nExABgEwR9m-B-RZtC2fj6BoahL8FYBm9ghrrKaRc2QLJPMp-FNJt-wxPmbc1v_DE7jTktqhIX8RBEHVJojd_2HTv9S6YqOAT0DG34h0nrwyRZPwspEMveGEU6EP3cqhGL6Js9kS6Zz-KPgwiex8kXxjP9HyJ8Kr8nlWzwomBfKWRoyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=CSNk7nn-aZvlN6EoMKg6iq2pD94Snssl4_7vyoZR4b-EC9xXQD6hxFcKE_taL4e6Jxr6wXepRv_4zwNcnpOVKBO9OCnq1I4caMYQIyIc1I-3JE38B37-HEMHSE4Xitbi8WX5OmTn-B91m_38ydBvZ2EAjQGbMsGd1ysfW1nExABgEwR9m-B-RZtC2fj6BoahL8FYBm9ghrrKaRc2QLJPMp-FNJt-wxPmbc1v_DE7jTktqhIX8RBEHVJojd_2HTv9S6YqOAT0DG34h0nrwyRZPwspEMveGEU6EP3cqhGL6Js9kS6Zz-KPgwiex8kXxjP9HyJ8Kr8nlWzwomBfKWRoyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFy3Fr9CvVVvyTLI0WAjLKxHUMcUeK7-3gCpccCYpSwu9fV9YzUl4cuO6wSkhGJcJnSqJr99A6hLi6CMIv4rfpGeyqQU29RtYLtp6XlE3DbhhSmlNdiJr63untiKGI4htrj-Vg6MCGbSIOvPAULAlh-WOpgp9u9Htb-YpxAO4ZADKalT4g5sDv_2lTBgFgIZMw47_mrmuF4jNAjGkAVgPrl2gfEYKCghKySHXNo5oQclCRwvFu0Hk0kPMw-oawsoWNDBzaAlHvwJAOeK0Qcv-Sae7fIexqTsGgP0jgCeoR40-CIsqUTF-ajOlYCvNgAryRXvb8KxV8RF6bbEc6M6ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhbD264CMZAmGzTsy9SdWEXKT_Xioy9ZG3GOAJMEUqhLBhY-EdiMlM2XuAVJ67emQqv4A8MnFiFan0TDJUiKYnVTBeQtSC9UYkd_TnZD_o9uZ7s7D1JAJJ81ggQZy8nNWRCw6Ed-4WrK9nCcOK3LjRa2B5y9NqrTD4tlDD08RqbLBk-1oPhzjePmltMWf50WiwlwlKDbsg29W2PxyhSCeAQfmL8TD3Qul5n2q91IjS0rxeDjUX0LEESEXf6JCgZhEfgEqoNVOryZNRFJaAbpw4bCIR0pmcIHAhtCin-gPts6OVgLPn71HT98pb6HTo-fGMRuFi7rLHyxgPQF5EOHfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2LX5WYarxdHadOXbOGsF4Q1m5ePLDSHIfEB34_4YL9vr2XMPG7TbOIOy3ZJlHYwSQvXcmd58fVYebx37peZ7S3aPuuLokRKUvj61yNW9509ly4rclMnkgMM2mGqZVZ1i1fw4V1op65THL-5sc1taOabnWpzziS2aFLJS2SORAJIXqlKgoWdXKaFW1VowdS209jDL4ysfn5HxB6UR_dMZDTAs8CXiv2mAZpK7Bto41s4-9QCO0Iq4OOBAjNanAtnSaJA7WHaXEFewScRDW0pVdza_GWJP8oPSUEgUJldbj4tUwhBWDF3SISdHUbQGZ95w7M8KnKHTqjEw_SZ4unhKg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=LZxLR7LeGnzLJG5c426-jZo3LEKjQZOgIEfCByAWC78InXeBgkPE70je0wayxu9a1mMt4fFZj4_ASQz5IOHXuvUWWXsHiOVxOweWX5ileaH7qhKxqUmr0TPwbbYGcEdMWoa-l1v5piJeCUR-r0YMJxG69Ou5OypMfN4nr1Xp_uU3nnuA2bQ3lWlyPC-IeeD7pL0wg13kJ2Wmm_S-D0YhlTRUiJYBZsKReghCMU4EJhc_FeDuZwRRHbtq9cL1H2Uit4iALRz0q9le4irFZjsrOzDrBDm_XzlSqgf9c_QzWT4RWDew4hEuP9HU5RxFzHdznIRCM6l3QK7z-6si58AUvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=LZxLR7LeGnzLJG5c426-jZo3LEKjQZOgIEfCByAWC78InXeBgkPE70je0wayxu9a1mMt4fFZj4_ASQz5IOHXuvUWWXsHiOVxOweWX5ileaH7qhKxqUmr0TPwbbYGcEdMWoa-l1v5piJeCUR-r0YMJxG69Ou5OypMfN4nr1Xp_uU3nnuA2bQ3lWlyPC-IeeD7pL0wg13kJ2Wmm_S-D0YhlTRUiJYBZsKReghCMU4EJhc_FeDuZwRRHbtq9cL1H2Uit4iALRz0q9le4irFZjsrOzDrBDm_XzlSqgf9c_QzWT4RWDew4hEuP9HU5RxFzHdznIRCM6l3QK7z-6si58AUvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=pRd85HHUE1JAazc4ULkYCqlq8UGwcCAgPV-17o7UtyetUUCQThYPR-zfqWobCQfssEWWC0lVqMB6IoEA_UNNrtWb1m-0a18yEWELVe-5pU_3bXuaYU__gnvhNT8nu_iSMkZlhHdbpaPQf7g-dcLGB6mX2VH45_tTuzuiS08syEpxNP48v5_feHfD8Qn9abNKtbhZEw73VH91BRPQyLIZzXw8HG68zNsAT2njAX7PPQY-ykHeVUkYyn0XWK5crxvznNQPERbBgppriScM27dxG4VFqaoP8zkTOdUDM471CSTZD8vL1h1iVQ4FB3f07v7MyRR3j9GgzRU3p5jKv0xeoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=pRd85HHUE1JAazc4ULkYCqlq8UGwcCAgPV-17o7UtyetUUCQThYPR-zfqWobCQfssEWWC0lVqMB6IoEA_UNNrtWb1m-0a18yEWELVe-5pU_3bXuaYU__gnvhNT8nu_iSMkZlhHdbpaPQf7g-dcLGB6mX2VH45_tTuzuiS08syEpxNP48v5_feHfD8Qn9abNKtbhZEw73VH91BRPQyLIZzXw8HG68zNsAT2njAX7PPQY-ykHeVUkYyn0XWK5crxvznNQPERbBgppriScM27dxG4VFqaoP8zkTOdUDM471CSTZD8vL1h1iVQ4FB3f07v7MyRR3j9GgzRU3p5jKv0xeoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=crLILh_eiT6MHZ-Xsim6VTbbBmQQGu5cdehORzwYQn84KYT6nKObQ1a8ocLmbszFGBhUIoeAdCn2MR-sytUoL7Du6GgmLxmKlMm51oqf1qW6xJdZqPAJy2pJyn_lNp_z0JBjCAJsJCSM5_tH1S4pmYdkE109WvZiuk4XeHZ2ry3q4Z7-4hi0Pb8KvQfJWCxZqeE3u4p1q-2BzE94JS905OWUHMbsl9F2g3cFonUib70yRPgpPM7VfTqi36-ZkkyVHUflDnOOKA0WXSAzjU9Rf5kQB-3MhsoHrsyDOSBK3poY2IQLmNonfCrsY6LjxK8WRPyMSAoZGIBiDFgwu7LFu58o_HcKYOVv2OoFuCo1Dm90RL5JtsQmPBuJqD__xL4Npyb5rKswpWizIAVagrnAeKs5n2hF_9xgbr0iRp4lXbJnGrcMoTJwo8ZklMnE85Qe0T_tQq1uIn-GebyOFw31-uyZJV7drBbOLLalLx25fFpvIF2iZBDsJ5it0PLWMEpSOnSHCrpWc7Y8_ALcL5sZdmvUEWMVaD09wm-sTwzheldV1F1Ae2Bdo6kUoHGa7b20hJ5DCFYuEXhUvGtWHrcRIeRSt6htmrQB3hrr0coCX4xFPMN6571YpvQJwYzyEQupXRhQpDDaVZllRn3aLc7UHNMIDS0XRbvRyMasEMZonvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=crLILh_eiT6MHZ-Xsim6VTbbBmQQGu5cdehORzwYQn84KYT6nKObQ1a8ocLmbszFGBhUIoeAdCn2MR-sytUoL7Du6GgmLxmKlMm51oqf1qW6xJdZqPAJy2pJyn_lNp_z0JBjCAJsJCSM5_tH1S4pmYdkE109WvZiuk4XeHZ2ry3q4Z7-4hi0Pb8KvQfJWCxZqeE3u4p1q-2BzE94JS905OWUHMbsl9F2g3cFonUib70yRPgpPM7VfTqi36-ZkkyVHUflDnOOKA0WXSAzjU9Rf5kQB-3MhsoHrsyDOSBK3poY2IQLmNonfCrsY6LjxK8WRPyMSAoZGIBiDFgwu7LFu58o_HcKYOVv2OoFuCo1Dm90RL5JtsQmPBuJqD__xL4Npyb5rKswpWizIAVagrnAeKs5n2hF_9xgbr0iRp4lXbJnGrcMoTJwo8ZklMnE85Qe0T_tQq1uIn-GebyOFw31-uyZJV7drBbOLLalLx25fFpvIF2iZBDsJ5it0PLWMEpSOnSHCrpWc7Y8_ALcL5sZdmvUEWMVaD09wm-sTwzheldV1F1Ae2Bdo6kUoHGa7b20hJ5DCFYuEXhUvGtWHrcRIeRSt6htmrQB3hrr0coCX4xFPMN6571YpvQJwYzyEQupXRhQpDDaVZllRn3aLc7UHNMIDS0XRbvRyMasEMZonvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=JhNU74wwJGsHzxr94aDw28iD9rZWl-LMuuXaflDETANFxBbEdPWqEWjrZykKUA5cYXY9p2jt7wjdo-l0timTwLgntfYJUyTLD3GCesGy2mwoPH_bjjL8CsUTXduyPypBOmId_zak0jlvgt9NaOvi3NXqxJyYvMmrzMK9IopZjR8vRK0lNTNkT31WKdbWk7gj8ykaWnkEg-i8pJq1iKK3Z88kbCqvJTn7eQjq_qW-7BhW2a3WR2G5D-5jX2KkA2WiySo1p6GOA3dhqp9OHrQoSRsl-M_4YbnxHMfQJ_myM5GWglmYYiiGef80PR5S6MfrvMxKkjm2lqRGgaimYtCvqr2eVHXWCW1JNZ58u9qk9WVQEC0fJrJ6W9nuvH1RioSJ5RL5A4sQehgoDIlpsp4dPLmfuezSe1yJSO8_2I3ufLaCwZrkAo6QpE90zCiJK_LUdXCxMLa8vIvKeDQi6voFgERSZ5iXgyLnbp4hrUSpRjGXAf66qSCG709exHXSI2MmmzaTaTKwhw-kKMt0IIK5aFYz_aP3MzsRRlBMkvxCgKQEa8ed9NJwggQMajatPhvMey43wdJPSS5ujbMRXfIA0-Pzu_pBlKyEk7_PYPFctVS0oo6HmZZIX6ArO2EjZild0QzzZXgCpEplm2me_Ac4FN5eI-rzyz1AlYXQM1MTqZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=JhNU74wwJGsHzxr94aDw28iD9rZWl-LMuuXaflDETANFxBbEdPWqEWjrZykKUA5cYXY9p2jt7wjdo-l0timTwLgntfYJUyTLD3GCesGy2mwoPH_bjjL8CsUTXduyPypBOmId_zak0jlvgt9NaOvi3NXqxJyYvMmrzMK9IopZjR8vRK0lNTNkT31WKdbWk7gj8ykaWnkEg-i8pJq1iKK3Z88kbCqvJTn7eQjq_qW-7BhW2a3WR2G5D-5jX2KkA2WiySo1p6GOA3dhqp9OHrQoSRsl-M_4YbnxHMfQJ_myM5GWglmYYiiGef80PR5S6MfrvMxKkjm2lqRGgaimYtCvqr2eVHXWCW1JNZ58u9qk9WVQEC0fJrJ6W9nuvH1RioSJ5RL5A4sQehgoDIlpsp4dPLmfuezSe1yJSO8_2I3ufLaCwZrkAo6QpE90zCiJK_LUdXCxMLa8vIvKeDQi6voFgERSZ5iXgyLnbp4hrUSpRjGXAf66qSCG709exHXSI2MmmzaTaTKwhw-kKMt0IIK5aFYz_aP3MzsRRlBMkvxCgKQEa8ed9NJwggQMajatPhvMey43wdJPSS5ujbMRXfIA0-Pzu_pBlKyEk7_PYPFctVS0oo6HmZZIX6ArO2EjZild0QzzZXgCpEplm2me_Ac4FN5eI-rzyz1AlYXQM1MTqZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=p4wKMG15NVkSaR37zHmSpXNUL3Qu9NtR5Fur8FsUjCN2ZUgO0sNJVmSs8k0khQkcKlVGnb4f58wQMDTk4aT51BbbPkFxcu8TcHiFMH_pPzYfJRYfupO6nOfbw4T6x9UujByIrJZfv-cdXTsEWbJ05HhQWnELYDlNQYCRAk7GRQ2JmDdhoN7L3aLQysd0CqP267lUudcU1NuGNBpjXmSOyHNoa7MmRLX4XMgl98T8_IrjsXKZsOQJeYUaC453Xdg6J_LI8I4XKYPB4kbVSoKXoCHE8ayh1vYunDJQ4U2dyUO-cLo5G0KIIGtuVmkwBJ_a9B1U4Gatud7Ejk1j19WhcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=p4wKMG15NVkSaR37zHmSpXNUL3Qu9NtR5Fur8FsUjCN2ZUgO0sNJVmSs8k0khQkcKlVGnb4f58wQMDTk4aT51BbbPkFxcu8TcHiFMH_pPzYfJRYfupO6nOfbw4T6x9UujByIrJZfv-cdXTsEWbJ05HhQWnELYDlNQYCRAk7GRQ2JmDdhoN7L3aLQysd0CqP267lUudcU1NuGNBpjXmSOyHNoa7MmRLX4XMgl98T8_IrjsXKZsOQJeYUaC453Xdg6J_LI8I4XKYPB4kbVSoKXoCHE8ayh1vYunDJQ4U2dyUO-cLo5G0KIIGtuVmkwBJ_a9B1U4Gatud7Ejk1j19WhcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHET8KTU49m2ex35RoYmeVrS8tJQJt1BZytfy8wyAE7bgN4la1dHfILCPLZWKS1Q7fVVzzwnNyyEA2NkjoQwRpJngQl7Pyd7tKmiafGZjrpv7BkAQhp20rn11qVTczxeCmd56YBvnZ9-ZZpY6027JYG6wxIwama02DGlxUmck5tyanbvm2hoRrvSiY1q_bW1DXPykH89t-27Kh2ZK2jZKR8-lqKI4CfmJg4EjYPgqmc6X0hM0eQkaV-v8xsDO92tSFEcXu6YwAlS6lhNdg4vznm6A_dMwobCloI8UKNBZFhl6tnqeqZ8tJoFWb6JocPCanfNhAHYOhs8An1sv8Tt3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=XAVmfdKHMXiai_NOBF4CTp7i3lIZYWpZJoKh9fh7ZLxsOFf6xq1K9f5-BC6wv5ARuucrR8OwMKttPN5dcktIrW0Yne5-g4dJgk694J1Btpyz6A0A2AGWD5WPOvSsPUAuf94XxlRRX7Aip0AotIIFMtKv_5lawWhSwySbFCIk7krWJSbGz6i7lucA_lnnjzTL58CcqlGUS7ZF6P5dFxHxHHEe5O7ELiBUdM6xAxnlaza1msJpdPecjvkOZVSxttYoqsAduIkMDA-6h6RZxOD-uiCAn3ZUJ4vs_LxfzTbp8wXsYzmjErv6h62uqDCZ9PUrPzMPFH6CnHhy1s21xZ-z8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=XAVmfdKHMXiai_NOBF4CTp7i3lIZYWpZJoKh9fh7ZLxsOFf6xq1K9f5-BC6wv5ARuucrR8OwMKttPN5dcktIrW0Yne5-g4dJgk694J1Btpyz6A0A2AGWD5WPOvSsPUAuf94XxlRRX7Aip0AotIIFMtKv_5lawWhSwySbFCIk7krWJSbGz6i7lucA_lnnjzTL58CcqlGUS7ZF6P5dFxHxHHEe5O7ELiBUdM6xAxnlaza1msJpdPecjvkOZVSxttYoqsAduIkMDA-6h6RZxOD-uiCAn3ZUJ4vs_LxfzTbp8wXsYzmjErv6h62uqDCZ9PUrPzMPFH6CnHhy1s21xZ-z8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=Yym_yHH-7iQ36SvczXYlxxCRkwBqDVnGBhcg5eym6hEH3MqZXzwpPBl34rQFE-8BFIR27JV0jnk4F1gKdtModDcaLLEgoFYF4brl5vfY6JMgUUwFhAx9pwzWbSmFf-xEW9B8dlieWCgNIJKfXPyFTjTxVYOpOtLo9FJpBZE0zq9yNoEsZlEUXP3i_mPCoaezxmxTwCWhJLv9AYOuyvK2G2XasNT1AIcU92k2Go-uhTBt3TVlrRDN_oDbO4XRvJmD0VqX3vIbwVxMIfFweqOVmx1q5sad8mISGJX2sxTca5ve4kh2ey2ymFFrb8qVFIV1tcPSc0p4Tk4rwSGlk39hJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=Yym_yHH-7iQ36SvczXYlxxCRkwBqDVnGBhcg5eym6hEH3MqZXzwpPBl34rQFE-8BFIR27JV0jnk4F1gKdtModDcaLLEgoFYF4brl5vfY6JMgUUwFhAx9pwzWbSmFf-xEW9B8dlieWCgNIJKfXPyFTjTxVYOpOtLo9FJpBZE0zq9yNoEsZlEUXP3i_mPCoaezxmxTwCWhJLv9AYOuyvK2G2XasNT1AIcU92k2Go-uhTBt3TVlrRDN_oDbO4XRvJmD0VqX3vIbwVxMIfFweqOVmx1q5sad8mISGJX2sxTca5ve4kh2ey2ymFFrb8qVFIV1tcPSc0p4Tk4rwSGlk39hJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r94-RGAu0lSJDhRoth9p9IuS2pnzrgj7Kw0Ih_o08Yny3Xf_5I7gjvC8nFPiG_v-gZaeerXEqHdsCoMd_o1o5bJ_ItlPcYStJtbnsZJjnnSJ81RzjK6Wa6fbQdSxi0wEvyRndDCHLdoA-R6zG5k5SgGdg9vxfOLI-H3_W3EZfvthQ74gCjnY9zTt1Ghc95wGtQUvP2AL11fKZUxBF-JOqk4iZBLOPGN2OAf1pCf1JmosogDQLWsh6yrR7v5k4W7xJNHO8nsTTWVzA9Dth3y4gkpsPe11Z5eezTfz4MLdiRqFRfFLxH47y3zr7ItLXjGr9oTbTb7v_UFtm1aK7fLRJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5xRg4odyK0FOdF1BP4biR5zuO50BWXzEVkh51qGeddguUlnLugpOomvm7pf6Lb1kAv2zkOOZxapzMzzZKIraax6KZ4FLnhPp3S2yXg5rbVGaLDY5MRtIObB5p_Jx7L64dt3Oil35nBgMPbQcWjAk2CzsKnTrhxP8SjdPj5vjs9WKgPixg9IISOlFazm-S08GqJIS2_HHNle-dJMFW1rrbSMB6MhzpYbpRZkvjgkB0mqB7YNKloX4TweB369KA51mYY6btYHHkQlE9DJDjoronq3ASG1e3E9mUWyFnH3kZtorTGeuDtGWAfyo2daKgENSz3mhaRkDfRCAdpSLcxvEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Py1II06NF36IZha0am_Cjuo7gJiionyC5eKpnROj-j3720tO1EPqQXbzQIWmRyOPWj5rDbL77pHI3mbbE_ZvyylZBnnSOPbL1jI81cWBFhuTTcWruWY3BUSNfCRcHmmZw7jnBkG7aV3lhZHIrebbs4sV7kG19B3o4xYPVdHeIjj4h8pKVCcJn8bvv_TaJRO5KGga9kz18W661ZXGpZtd1LLoVStnAoMK1wJVqYIRmYOxvIYo6gIWHsfTqN-w1tYFgjwPYltWvefbpLjXsbQPiW6FYhURkwINLIjzzY05l3Om2RXGY7Iuf3Sj-NUJO4b-N-gkJyBz3xBbafrAzMPejg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psSnx3VfqoQ1juXKxP0ojVt3_oIIZcviwLH2c_sCjWJSZacgQc_mob-DEhYWvkYpXtB_vvPuqT44bWzfoqZ4SOxw4gmYU0KuF8hCw6bKVzVc9zmchuCTMWdTtWvUuNvruzN9ea9ziQNTtXuY4weBJRMapzMWQYu-Hx36V9b1Tt_LzKPZXQW6Ca16sO6sov0bUvAl56L693nDHyIvX9BfS4ZzPTQC8A2WfBdnmngiTUIK3m-o743syqk-jO_uekAFEKC_FmHHZUEK304aDCBxb_eXze1Wc6vdrBy6IWlyscUuIOvghj-NQr0KtuxLGJL8M14yWy-agalIghiZSsPYJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/blDkzhXIddcgu3X_rtkaKczgWKqHh1n4tFxOdWACV-su3WKBVCg8JFBga56oFo2Pzvuimw3vMmK2c2bYP8b7-18awqwzWF3XrU97nbxfg3rTSCQwYVOXGmfY7bkB-uv_itopJvhN29MkxNZ45jI4fgec_fu7ZwutczyXE_2f3osVyn0clIDI19uAwqgHsnnzuUhcO9J-eWC-JjffN-b9f0ZWg10j8Z_EXWtHOssRdIPLoxCbL-_Wj2JKfm52Xm8OhCDM1tCL8ENbnZinflPSdD1p2Rsonz7sTpCs0Ozw3aRNnFbCLlclMilYyBeWDDEembS7_RaxxwGYNGJXFPZw_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnbhM3XXlicckxyEHXwf4JYxwpOt6lzLK0Aj2xl0IJkDYsE8CVtY65i3vX5_eU0votDSPRnOLjDIIU4lH4_GCOKrwzHqHpL54ax175KkPNAhM-RB14bytONW83A1MGTYgcPN3WGidzlq99IO2wsDmbiYZz6lzDY8lv79YZVoeoJNpF3OJAR--U88pWQplXniIpoPiFTw-0qJPWHsr-MwUEIRDZxlSbaTls9Ldrsag2vsPl6ZE-T82OqACwpvpv42-NWuDGDi25yLx3rl4I9pIcqzKoe6FJlFZuX2dvPDvIgCGJ8bzn5xWmR4VX9TYAd9CIo7t4kJgoQglLzNhSvdCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t21qizGcNWBlcf0fEh9pl2f2mpJBRYkL75-G2XkBBGkEP13wx16gvy7ncDqdiTUD_thxSxtK80JknPzF7rwnNoCJm7R2CLbrHYRbaFCNRseJ06TV28kaJzxHECN7Wkuq1KjZO10TJez897aPjY9WJP3DUZFijgbmUQ4Q5qPYzrDb-ck5H0xW41-fv1HjheVjAHaqT21ZXzuko91XaounM-SeCvasBv02LRlyMigmyhnWGCkgOaZWYVa4b06icxnJFQPs5dLmVedbkD9Pi8I6e8Or0f37VJSNSPtJwnJKY3hLUCT7eGQKwgd1T3CqLfd6cpx3I_wL2Gz3DN6K9MOL7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lNY1-si32nGLvoOXW0woRUC1pNY4xOQrIX_HaprOkSs9MJWUgVblxmhgz2riWgvpj8HdLv8C5KGPRrQemNVu1dIoLCzhxaPGcjER0MyGtcjWSm2-JuORXdKzyz6JXAE_ilJCrFXlbJerZisV6XvVKubVDGPuiIkxCJEeV9At0TIJakytX3GI13DTl8oVyMYDUZ_WDBWATi4yflCiMkSWE2wJGsGnT2gZwbPT6DhFVmb0-Si6jhi3CYqv98KI3LOTVwYkM4_QdAuSqEpixewfGeCU_KvbgpkRGMK63M62K0X47dTs7N9LewPWwk4Zt_eWnaAzMzq3TZGqMbk-Cr7w-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F2Z_Wawa-8pUzO8jnwnHORBoQUOxCVfGMCk41w8HrhAvaOl1iBIQCZkbwpPVH0uFPxGY7XG_RZCAJz-rV4AEDCc3SFbHJ9JylqWORLl7not9Ck3UHXFTru9wXylMouZlCo-ZVFFRXy-HKbqanmOkNrfLzwoYP8ObWkJn96UsslG6nUUxSL1aRwupUorvGCgI1yDr3LgEzCNxdge3JwMv2oSAMvjalUxsrDQbV_hOedO3c0u4FGIMCXosVbn20FXomvXpEv0gTNBVkT3O7za9z7B39-ySy-fTrvCj-A52YLuH_jRbRoWnIdk7QLSFecMr3slb0WXatMWUcjW86d_lQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZUU7XXi-QwvLj3JmRWNuEn2eoJEFTzePUWN09awQ-xsYFk_8Tjtt7O5tXZvTXh0J8I8TYQRIuqOfJOBeM8CxN_eg1i6rbFdeJjemAzjPh1PPDXMGRgVxaB4ocZ3vK4XzXpH7RWi8nogobAnnjwQ_ZsIE5zbuikV8vncXoQjSNXkaxFqo7auXMNYNBPHoF7JGcxs-kpQNoCYcVu0z43-SpAcoRPALrRG3i1efDz36KFxVieS5-9dBQvFf0_YIX8f4SR7UTUVYwXhNi2EellJjS8gYGYOLDvT3fncU2S_Y9vel-AQhYU82_MgdpI2OENg4IFZ3cmw4maSurrBn0QTWQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=Ap2vHZwCpquRoJ5gxcds_4I0XolCPX8PvSBnNieXTN2MzH_WLjr56Ipq6bdNZ5taO3CXa3NJdim8INksrfWhNSzwvmfKLVOgCl7d6SMFDUmCc9VnpYqpcN6klYthXLNIYLkPKHL2ccA9qN64nDzIBqFy2YC0yZ2kQyLhMBkgT1rK7Xa7ecrx2XZUi7GUsRj2coonfcW7qd2a2-Kvl0ghMkeCOZdZYIWAo67mqTuWc8bSyzVZnwHeRrZL2DAF-Mlmlc4r6HqkMBJ41-kYj-Cw2puXWDRjUes4awgfMsYqS1ad3BOWd4g0VdF3fD2MFzY4bzuF2Cf4cgm6HCSBnc05EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=Ap2vHZwCpquRoJ5gxcds_4I0XolCPX8PvSBnNieXTN2MzH_WLjr56Ipq6bdNZ5taO3CXa3NJdim8INksrfWhNSzwvmfKLVOgCl7d6SMFDUmCc9VnpYqpcN6klYthXLNIYLkPKHL2ccA9qN64nDzIBqFy2YC0yZ2kQyLhMBkgT1rK7Xa7ecrx2XZUi7GUsRj2coonfcW7qd2a2-Kvl0ghMkeCOZdZYIWAo67mqTuWc8bSyzVZnwHeRrZL2DAF-Mlmlc4r6HqkMBJ41-kYj-Cw2puXWDRjUes4awgfMsYqS1ad3BOWd4g0VdF3fD2MFzY4bzuF2Cf4cgm6HCSBnc05EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
