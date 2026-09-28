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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-06 12:39:35</div>
<hr>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4Xu-1Sv90oyw714rx6EwCm8pyPA1QzJzkpoobjrS0xEIstln6p6BVQFAWDdNBc0i9vgMbSwNhynf9temTE6hoGPeazJfnoWbNLt9KJuEw2x1kM39CcK08xuRQsKq6A5IL6TmB77y6M4AKJl-Nqk1z8lp3556EP_CXBSlbOHP4kGXI4DP1Lhp0achH3MRLxSRjn97t6PPcv65QeAnQrq9oc9M34Z_3WkRHUyJMouT2glyogky1kN_YhKevps6watjL9NT7pe0wrxUFjh7sxTP_r7MCUCE_3nTuHpKLN-B67sE4T6kG8QSPRIRo37NQdJPoh7X-ZgdkxObB0tRFZWQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tSst-zfn1pTNCF_3W8CENYPwILfNgPAH1yvzW5jVV4tTsAq2oVU7kePzd7VdJDkylbG5CBhaOFu2vqAkfnGlOo5kMBubuzRbRj49nNWOnXQrLZNrFXAUWUIndadao0IbR4twPpYd-cDQNakjf_5yYz9h9Ft-BaeyR1jXaSje3q6Cq3Akeobm9P3yBzCgf0UF6k87GDRoZhyWpGaMmZ1yitSgNeYUNRZgJH88Ag79MOf55Zf4FMHFkCsJX-7QstByh0kdymtZ_EoF6AA4p-g5JsGLaKDbhRup7psbu_Mq8qTlLMC1G1ppxvjC_yWw63rtVnqrNP92IdhDQ3mVmUZYVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eJ1k7dm_GhiESAkJNSxJvmEyIW7HntmC-P8kywaMtdJEub-atDUktxYwqddoqOeRAQNLZpviPRXGd7UVGkfv-D4_Fc2uM7WgbV7mrwl1l8ZbRfPfxNJ16Rec-CszkJaTZam8bSOsya8k4jUhGcXPPKX_Y1adOhp60RTaBJiDmHyHEj4m53iZf4BSVLzXzxc4jOPH6UO-pz9uyzyG30FWPClTe1Yr1iAky0ge9kOQ_PUJI1IbY9uV78lesbhHIICJ1L69SrJ2Z5RGl7AEDbSYP5qdvTLfNuBPGszUuKyYo6b53Mseb5PF2IaIdG_3OjYhKHwB3MOT_Kp4fCYBWvcoYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=IJrlJ80pk48V2nrK6GhvJK2jG4_a5MeKzKlUvcMhBu9GKkQCypxFbLr_7N0VqCt-RRNzQioBZqKUdXxGz3H65BOxjQbMGjT27oTnGVTANc4uvqbonh6DvFhFRWhQc_vbR_Qre4P01lafgsaBkT9A_qUgfHvzuJHo3gMU0hdXVz-k8AwFT6cuWaMgM03iEmYP1kDgAu5IjrUKfCwRFlunTvQFKq2Zjh5hDOctprJ6Yxdxb3x_AxQijfqnFyf31My61pMu48arX2tvCjRQgBaxC-UMelFt5vlAf59icRlToecZ0222-zQq8Uy85kuHKUpAAwbPJl3GdXl-_1sxYdQXZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=IJrlJ80pk48V2nrK6GhvJK2jG4_a5MeKzKlUvcMhBu9GKkQCypxFbLr_7N0VqCt-RRNzQioBZqKUdXxGz3H65BOxjQbMGjT27oTnGVTANc4uvqbonh6DvFhFRWhQc_vbR_Qre4P01lafgsaBkT9A_qUgfHvzuJHo3gMU0hdXVz-k8AwFT6cuWaMgM03iEmYP1kDgAu5IjrUKfCwRFlunTvQFKq2Zjh5hDOctprJ6Yxdxb3x_AxQijfqnFyf31My61pMu48arX2tvCjRQgBaxC-UMelFt5vlAf59icRlToecZ0222-zQq8Uy85kuHKUpAAwbPJl3GdXl-_1sxYdQXZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1ZpdqpsBzE27rK5Z_5mJKT9IBaFpahsusZ_-0P24q3ZgKmErguuwwVSps6ytinY53g_hqwMVDONsCP4g1smpjBjH6kPGWNuTmXayUWkLM1IEm-Pbc6IDWmENnk8wDzdsDu0n8hcdX0JEph8wcbRT-1vxyGsey6hnath9Erxyf0VkimOK0HolzIGrUU-z7qt-OpNbOT2KlxzguXSyVLh9cMsEghp8wZXQ-JmwwRiWXYTlwVDc6ELWdOU_907l5bCMCFsQuOJ8gIhSFi-4IDM1Sq2XIc7ey_d8Aj2Awu8wNAhyNo0lOJBpfcQCAYKrUvkn1EteQl5cJK1lFjoQ90Tyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=U6ZycOvFuYlPi9N3KWcEOv5k2r7HN9LG27e_ynm1zdbaa8rLwHYHj1qObwC1Z51Mo-vB6QS0zZOMy09XwIQnkw5kPVPFqfSjLOC_22FBF6I2ChFCgfFQnSkvvB11eMr5xEysxReVDtZvmt8MY-kjRIjQi7O-ALFcEnAo751A1W0yXUSvX0etaM6cBRa6W_HEOYEy1_KMLSYYgOOVr-yjxVlEj8_z8UQZAXhy_8toflFTS2O9ilXGX29yxjqtOVpfW2Sw2w8tmD5IC-debB8iDvnMywH704HamO2ozoVSg6QgPi-rdLOxqHHRBfQIRuMa--p2CtS9Oif-iUqANGgBaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=U6ZycOvFuYlPi9N3KWcEOv5k2r7HN9LG27e_ynm1zdbaa8rLwHYHj1qObwC1Z51Mo-vB6QS0zZOMy09XwIQnkw5kPVPFqfSjLOC_22FBF6I2ChFCgfFQnSkvvB11eMr5xEysxReVDtZvmt8MY-kjRIjQi7O-ALFcEnAo751A1W0yXUSvX0etaM6cBRa6W_HEOYEy1_KMLSYYgOOVr-yjxVlEj8_z8UQZAXhy_8toflFTS2O9ilXGX29yxjqtOVpfW2Sw2w8tmD5IC-debB8iDvnMywH704HamO2ozoVSg6QgPi-rdLOxqHHRBfQIRuMa--p2CtS9Oif-iUqANGgBaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMkz5sX9PTeEjCiNSA9jacT4khR_vwGc8ITb05O1NmZh7rhkjkJHvoNoQryB6BrhMxengYInqgRdd6XFKuN3PogMiLgwKplKWfOZqxQ1M99jWwWHVAk5vJ4221314fnfK8rUOkUg-X5oFtQvLP5uEtV5wgiKp6CkTeCfcbDgiXqwiByVjiS9RORqam2zua0MFQf-F3COKUyGNBN_x8ocr44B-Ln82InY1EmxRwrOM72am1Ef_x0v--j0XYfKg76Ljkb0X3FU73SSkiWRRcN9cTh2JxbcJw99Kspd0LEY4scLajweA6VgAPnV34ThUryrsMZ3kTR45WlZVxRUldKDmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=e28JKAmo-C1f02KuZCDZ3FiVvFP7rKcv_KWcgEsa_qnnPs3ckZtMwPC-elMMSrnxWhsOQbI1Rl7ISfW3xfTX_2cWPJvqDDxrd--23T_ahIwHhfdXaJXtHLzK4Ln7eSQP98qxtmt6AY4N5mJIj-M8z0p81NKkvSSMdoDisEAnFcfwxT-Ya4r2LpjVKcMr-bx_yOmTPdWvWADHLdh-rrZwZXEi6W774edvCP3tiV6W062hZPoTuqouvDDffWc-3YBVbMnwIRkCGhQNb2BWV8BltFORgOeOz_8k3WatU0JdRIBTjcmpsQaxsEdDb8cRKlKTVyzGXHf7Dn9dWtaS2Vi_jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=e28JKAmo-C1f02KuZCDZ3FiVvFP7rKcv_KWcgEsa_qnnPs3ckZtMwPC-elMMSrnxWhsOQbI1Rl7ISfW3xfTX_2cWPJvqDDxrd--23T_ahIwHhfdXaJXtHLzK4Ln7eSQP98qxtmt6AY4N5mJIj-M8z0p81NKkvSSMdoDisEAnFcfwxT-Ya4r2LpjVKcMr-bx_yOmTPdWvWADHLdh-rrZwZXEi6W774edvCP3tiV6W062hZPoTuqouvDDffWc-3YBVbMnwIRkCGhQNb2BWV8BltFORgOeOz_8k3WatU0JdRIBTjcmpsQaxsEdDb8cRKlKTVyzGXHf7Dn9dWtaS2Vi_jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1i8nL2018cOSIgcnX6Kq35ow18aHD2JE-6y1OEmJG1JIxqYIWNhu-I_lTo23eQD7ous07OyYNxdbYqAKRWw0ilubNYN9tbU_Xjj9PfFMuSgQNdNHrArPD26b6yD_UpGn2o6zDTY8cbA-rgA1rOQs754QIDu6VvvTBPI0t7-BnbegYSyIwS5Uc3-BQwF0QAr3A1js0ZZoXVpqfd1hCRd3z67qsNajpPATRVj6BnAIUO8ImlSLd_GQybuTxel3bYPFDsgtzNfcYsaaas3LFA8EreZ26mmC3gjTQwIYzLe74_F7qua_bECvL9c1qh_kwutJBferEDzdfKR_fhwK19Fmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLTniYphpNmFoB37EJxs61PtjfWe2uKoJObnn7MSmNRanI5ZSwCky4CGN5QKDoA2i0mAoAxpoTvFojXatxi-emNB4aEqJqHnnkF-JPwDJDj1GzoYaseAdvXgsfoccpJx4zMbS1pEiFFgkhGFhNcUc0j6Iv294poICVvamhJA1BtHXp-pOfMt7hp4BoxOZoz41OiWvY-iARiREKI0dhPd3aOtXH3Xl7B-hOTWEPbTGt1sS1TIKWHIRNaZlAFQVGvcMDLEgK5LBZMDl6VnW_Edenteeo3QyL4sAhxAMSgJ-83iBhZ3RxjH-smhsS94XzVguH3dzJXN2dfars-oRTrx2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=t2nWC9wSG-7uIAgV6QjgbOxu-HuYqiqtFwtHS_Uw0aeQiVePMr0B2nRUuTe5b_ciRnvowFmJC6QGHEw6UYlFyHFsZKfxwoMUA9QEZLuEwLdJMEyxs-xFbNB1jTdRJERrDQ0DiWm_2TFaffpNEkMUcmRI47sfRkiQumuXZS906x4dnLdzLxK97MdGKr29KAIv-ahFcQMCXBFbFr01utc5eQCokALOqvojEm9yt9-EHdZTYnLlhk-W73kzYF4-wvNh9o_R_QO7DyJ5H-tyvJc_3BeESG_tVkG7oyb4KRTNFiOcnvjJaM71jmDo3NnDbQcA36UATBIpWyv18OwQeqizhE48rFeAj0lsFONQCHOpOW6_zQA6k7raFOsqMprNeChDfrdDtBv1Bkfz8WON7CP2Jr8LcZVm91hLkpz7Ztfm6wGoh9MogItef1SNWgo6IkggTcdwLSk2HXWqdpLXG09qSiUuycMXJJaXrVG17yd4L5uegYe8z7ROABlhiNTsOnNxbGcU5LhaqokMY2jzVIvHtgOJyqKdffuCkOd9x-OiaYvqhq5xXAFthxHI3IFCL5c-8ztrcpd4PXYQTJWzLzU05hLLGY_ZcJ1tzp4ougXDO9Ft_06-Wn_iuD-xpADo-ZMnZ09ptnqLaF9Ps0esYNjmVJk78I9O6YvuJm6pv2oizqc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=t2nWC9wSG-7uIAgV6QjgbOxu-HuYqiqtFwtHS_Uw0aeQiVePMr0B2nRUuTe5b_ciRnvowFmJC6QGHEw6UYlFyHFsZKfxwoMUA9QEZLuEwLdJMEyxs-xFbNB1jTdRJERrDQ0DiWm_2TFaffpNEkMUcmRI47sfRkiQumuXZS906x4dnLdzLxK97MdGKr29KAIv-ahFcQMCXBFbFr01utc5eQCokALOqvojEm9yt9-EHdZTYnLlhk-W73kzYF4-wvNh9o_R_QO7DyJ5H-tyvJc_3BeESG_tVkG7oyb4KRTNFiOcnvjJaM71jmDo3NnDbQcA36UATBIpWyv18OwQeqizhE48rFeAj0lsFONQCHOpOW6_zQA6k7raFOsqMprNeChDfrdDtBv1Bkfz8WON7CP2Jr8LcZVm91hLkpz7Ztfm6wGoh9MogItef1SNWgo6IkggTcdwLSk2HXWqdpLXG09qSiUuycMXJJaXrVG17yd4L5uegYe8z7ROABlhiNTsOnNxbGcU5LhaqokMY2jzVIvHtgOJyqKdffuCkOd9x-OiaYvqhq5xXAFthxHI3IFCL5c-8ztrcpd4PXYQTJWzLzU05hLLGY_ZcJ1tzp4ougXDO9Ft_06-Wn_iuD-xpADo-ZMnZ09ptnqLaF9Ps0esYNjmVJk78I9O6YvuJm6pv2oizqc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nb64PhowCIuvmhDVUkgpJq7v85KlZU66c1nSRk59VKf9iWSKhwlQe9iTl77b25deFa-8DDblAvJJ8jzNlrmYkAgOqyzU1GwbjzeHCZRRQK0o6lrLcp_kn6wdPgu0pIrIRY1jF9i1N0VSuSOD9f2hlS1B5UZ5gObkgiyzyDjq08_sBGqfH9kFNLwEnm832mS43iwiOOYSvD3nNnDDmsc5WShnBPNAhRSnjoGjWWHiMrC-ZlSw-M-GYDyDYTyMPxyQEGyzbQHmfnJ4lWm-YCzOgJJP7R8kaGaZfFJCLSRn33SWYSoGPgycVIkw8RKxFuCe2C3t-AuchO5aYL-jrKjNgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOiWX3LizRZsJLS1nKiqK-wq7UAaGVxGexcz1IVt3EUkWWW3Ajhj9BnuwAgXpxTEcYf0ptWSWoYQEDaZgMHYDibQlymuosLE1G9OklXAsLniSXpChG1DrkTHRVJWu55LCgDevrKhZ_qJy5S9UCXTzdgld4f-Z-zm1qfx02gRZHfKQlmnLSzZkX4iJDUqn7ifofK0EKPfqC36xdA_QV8KpHQyKb5OpCCWYh3e7VL7N_114NC7wM5PxyVV0CgLQi3OjYWFPNlTNg3Iwr9dn31oj6KnQCYywpRF6U6Bb-Ma3TW8jYCXkKb0biLAdMarTEPft-bxws0MN4hqWZeHP9Uj1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=MthsD2Zz-2gtjWVPjiVUVp4rRofFqV06icOvyX-coVYOvUnHgFPpq7aqr6h1NzMI__5efdfz31jmOQeHRi8XTz2ym7ZsVS6NYv47Qae8bdoFlQBgRKgLjga0mDpJ519IH49Ph_8VaiNgm_1B-V4iZokoYhFBQuEtctWXKzdA_k-Y6h1wfhBdl8W-NuWeKceNZx8Wi4eTQmSMeNsvmv6CssbcL07lpg2ye8LQhnErRlz_5CWZ0Cyf7p7-6KaoxLavo2RbGZR402veplYicW1knua2Y4ycwCkkPzzCB4k0yPl-g7S-kJPPQhLB1HPtwhyJgyrfDQQNFXUz6HAaFwuLzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=MthsD2Zz-2gtjWVPjiVUVp4rRofFqV06icOvyX-coVYOvUnHgFPpq7aqr6h1NzMI__5efdfz31jmOQeHRi8XTz2ym7ZsVS6NYv47Qae8bdoFlQBgRKgLjga0mDpJ519IH49Ph_8VaiNgm_1B-V4iZokoYhFBQuEtctWXKzdA_k-Y6h1wfhBdl8W-NuWeKceNZx8Wi4eTQmSMeNsvmv6CssbcL07lpg2ye8LQhnErRlz_5CWZ0Cyf7p7-6KaoxLavo2RbGZR402veplYicW1knua2Y4ycwCkkPzzCB4k0yPl-g7S-kJPPQhLB1HPtwhyJgyrfDQQNFXUz6HAaFwuLzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=h-ZtR5EqcEY5sZKomGqLK8-dhpVo_3qYNZu4FqbwCUOAWrhYAXwTUoSoHwkucJImIhQacItQj7NKCNIdfQVOtB4vBL6YyLzI0UmMlMnsSOZb6Rm4PmL_2RwsYjjUYfb2k2FBEDgdVYa1rdTtUPost5B05fqt3cBJUDy_oZGXEiEypU6vvsDrabfXuYb9dVPAMk96M4v8rX5b172gojSfZGDFoVr87JUOMLLZdLQzEi4-sJ9D003uvHMwX1y4uGfTnK5cc-40zPBXv0Tx2tugEq2V1MzL4KwyzeFPDj1b2u72EESIcDMR65QrfJ9lfwBzEvz9UH8xAtKp_Oertf7kbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=h-ZtR5EqcEY5sZKomGqLK8-dhpVo_3qYNZu4FqbwCUOAWrhYAXwTUoSoHwkucJImIhQacItQj7NKCNIdfQVOtB4vBL6YyLzI0UmMlMnsSOZb6Rm4PmL_2RwsYjjUYfb2k2FBEDgdVYa1rdTtUPost5B05fqt3cBJUDy_oZGXEiEypU6vvsDrabfXuYb9dVPAMk96M4v8rX5b172gojSfZGDFoVr87JUOMLLZdLQzEi4-sJ9D003uvHMwX1y4uGfTnK5cc-40zPBXv0Tx2tugEq2V1MzL4KwyzeFPDj1b2u72EESIcDMR65QrfJ9lfwBzEvz9UH8xAtKp_Oertf7kbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HclCGP9U6io8zD1oWg6bN9UCGyPMG8OQFK0WIkOI9y-vh7VyoL7Ci2q9hJd5gfKtIF-mQuhYRWQcd3nSAy-1rNMdnmryyJ7JwvPgA2te5br1DXCtTnbahIG3DxEtLzYmTI94YdMXyGS03z9AWMuWE3s2KkiCqQXtcUs2lxoQHFqiygloNtKs90LpFXmKJ6SZfY64MzIN5ZxJfqHU6P-Yy7WPHbwVcQrXCxlswEWbMQicV5ja4mNdhNHJj8LFNKc4DCvy54N8TlqQ6bfLPY4DzW2UeqVEk0bmaXrx2_NHhN7j9pBsFHjPklqukZ3w-iVFs5CbNtRLeNbUDIN_XRtJRg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8AC1h3ZfFCD5AP8LjZ51GzRSSCg8X-mcrsuhraH-lgUyL9eAuFnCvb9-VXdEUnJSRr42JzFmXwH7B3zzHX6MRxwinRnvp-PyqA0hUAsNg7Aqur1D5KG4PMDCfAeLygveLB3YcYgwIU0dJXtvZMxna_d4N_IJHnzZZ9frJJj3ByD3ZB2oJ5nSeXjSvY59PIEDs3r3OFly0m5rfEzFXKO2xH2jox5c_8Rlz4lW3uXXtBgID0qtr91tnSkRVIEIa6vrjDzdP3Q4gVNcMmAgUBeDt7eH3MLQF6SWk2Sl6ci7L4TsBeRjaixluZyFe1fLyUARU9ot-dsPnI4FT-zybezjHf4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8AC1h3ZfFCD5AP8LjZ51GzRSSCg8X-mcrsuhraH-lgUyL9eAuFnCvb9-VXdEUnJSRr42JzFmXwH7B3zzHX6MRxwinRnvp-PyqA0hUAsNg7Aqur1D5KG4PMDCfAeLygveLB3YcYgwIU0dJXtvZMxna_d4N_IJHnzZZ9frJJj3ByD3ZB2oJ5nSeXjSvY59PIEDs3r3OFly0m5rfEzFXKO2xH2jox5c_8Rlz4lW3uXXtBgID0qtr91tnSkRVIEIa6vrjDzdP3Q4gVNcMmAgUBeDt7eH3MLQF6SWk2Sl6ci7L4TsBeRjaixluZyFe1fLyUARU9ot-dsPnI4FT-zybezjHf4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=mpPegpOKo0ZPUwR7aJpRjGqXNsBAx58bS1C6ixCiw3D3S47iQGX7XUr3Jo0_0o_2FsBAp1bSgyjHmrErxNHoY_7DxxWK6VseuVUMGq1bXqN7p5V0ZFl4ylc4ZjZC4E8WxGaP1LqZb8amGSzFCm1mx1dcCC7l4p-g8Rb0ZNQBok-XxXzzesMkchYs-e5i7mnmfm59taxanEpSUZJdFirW1n4370kbJquKw2Ox1gM5mBFfc9HwN2qwjVLd8zPtWdIxwD75YiVeBOggiIQk0qTT38LByTyN4VCb1MU_P5HdXd4AjDogkTOnfHwMu2Sk_Zn2ka22-HIjzXT19xRvLrjSLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=mpPegpOKo0ZPUwR7aJpRjGqXNsBAx58bS1C6ixCiw3D3S47iQGX7XUr3Jo0_0o_2FsBAp1bSgyjHmrErxNHoY_7DxxWK6VseuVUMGq1bXqN7p5V0ZFl4ylc4ZjZC4E8WxGaP1LqZb8amGSzFCm1mx1dcCC7l4p-g8Rb0ZNQBok-XxXzzesMkchYs-e5i7mnmfm59taxanEpSUZJdFirW1n4370kbJquKw2Ox1gM5mBFfc9HwN2qwjVLd8zPtWdIxwD75YiVeBOggiIQk0qTT38LByTyN4VCb1MU_P5HdXd4AjDogkTOnfHwMu2Sk_Zn2ka22-HIjzXT19xRvLrjSLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtpTOy78WXfbsTgr9e9YXiSNP608Q18ElT083YBtk9H_OeblVPVc4EZstSh0xgmaSs4vT-19ghNndZVItwAaBT5K0akwc2cTP4RScgGBsHZj0efs6Q78uv0Qc58embBI01x_he9mopalTNixOE1q7TyV_OgfN1DRq-T_-S2dUS_y99lv-6cUJ-QjmNsgNvER51w8nlXJa8ej-s8J7EECy4NITqluCCBG6-RHMB01Z8Ya_9b6gbVje8bGdUpCh0djH_-fG1K6FWMVGosPqHuAMVTzfFZI0I0_N2dykg5qYj8jg4pHaOnBWCLTkziPTOwZPV79pSKqvwFxCAZ5hYlBgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=gBn9UBFiFftGUPnTKGdroVayyNGMNqRjFH67nPsHHBGcJT_4L441bUC1v888Q8g4qJGdUlWdcTck42bezymsgouSHLNwTOmwLH35LPawZelvpirETT4c2YiaFRnAzkDPE2FQlGuiXGs0G-mYMd8VPzxfbi1_kQ2nDMM0hDUK8nb4LPHlskmk0rPdSaHItxIT3pLwcbvqG7rGySCvUCPfVO8Em-pHFi8Ezp4lUPUl8VBYtcSINRy9vvGDGaq2X1-r9lnfnogz_z5P4yHgWalUObgK4yD1_V9E8l53O5tL_JV6L2LpxbnBQ4zIudtYPAtV0M72GH7EZJt-bPAI5LIk4UyqY5PRIwgze5Y-dkHPEyDLEynLyQAdMLh_cSbw5gOT9b5W_KodVQLfdxGiLmdJYYT6HnZWtZ409eSvoHynuFXqJrm5uqO11GT0Q7O_xDwCXjTC6H8eoGpLB-zN31TJotXNFD8vrecAdAawx2l-IB2v75n8OIrh_YSkoQQpoiXI1p6wS8Rr91DhRcjPrK2K0js27ZoWBg5CLQie8zjY_C0HElOTwclB_VeE8eOu4SobpuGMqTzo0Q0g6TJaBVLiJiiWtkMtFtmE4z59J1I1aFKSfMLtQjH-MmfdVgjD1aAulTaeCSu5543WyXU5uURDWWPmKixJJwo_2bulffU7w1o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=gBn9UBFiFftGUPnTKGdroVayyNGMNqRjFH67nPsHHBGcJT_4L441bUC1v888Q8g4qJGdUlWdcTck42bezymsgouSHLNwTOmwLH35LPawZelvpirETT4c2YiaFRnAzkDPE2FQlGuiXGs0G-mYMd8VPzxfbi1_kQ2nDMM0hDUK8nb4LPHlskmk0rPdSaHItxIT3pLwcbvqG7rGySCvUCPfVO8Em-pHFi8Ezp4lUPUl8VBYtcSINRy9vvGDGaq2X1-r9lnfnogz_z5P4yHgWalUObgK4yD1_V9E8l53O5tL_JV6L2LpxbnBQ4zIudtYPAtV0M72GH7EZJt-bPAI5LIk4UyqY5PRIwgze5Y-dkHPEyDLEynLyQAdMLh_cSbw5gOT9b5W_KodVQLfdxGiLmdJYYT6HnZWtZ409eSvoHynuFXqJrm5uqO11GT0Q7O_xDwCXjTC6H8eoGpLB-zN31TJotXNFD8vrecAdAawx2l-IB2v75n8OIrh_YSkoQQpoiXI1p6wS8Rr91DhRcjPrK2K0js27ZoWBg5CLQie8zjY_C0HElOTwclB_VeE8eOu4SobpuGMqTzo0Q0g6TJaBVLiJiiWtkMtFtmE4z59J1I1aFKSfMLtQjH-MmfdVgjD1aAulTaeCSu5543WyXU5uURDWWPmKixJJwo_2bulffU7w1o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZiy0jMOc2c5SoBOwV2ZMiCiYexDmOTRMniEIRN7ve1mjEWGtnqHa2mQDaTQm9kqDgXKg5g5jZlv2imNk1GB4SoAoRZ1gMSILChiWlAWP9mMfBK7MDeAtchMxIhwLeGb_SjSvfrT9tynhGrCWgF27fszCcgp0AiCEjoLZeXYGAD6TsZZhK-bbymWofQrySe_YGr5V3iR4WJcxF_OkCQqTvgXGo0K_Np6UsIKFZIEy2DCsysXKAbw2dcSZQqsNPwzQdp1O3QtHG2ZJvQsWMVdjPnJ9aaANxQi9oaxVS0CbfIG13hOx_0gnL6OqLZuSU-7UPj9Hc801tvIp5XVFNVBFw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=jWlhoRFaUsAAZtW5xlYVDygUxt60-yoHMCgas2TOBeFOJJ9mZJpUALV4sME-weaYYov114ZhwuRq1jxZ0wdBzaY6_cVGPILqHFiu_trYbEl42JsagYDvsBcqR0Yy4QQSOC14WBINve-3qKFUWTMhfUz3vXNeghuMVTWs_EI-zH63YNtEtPM1lkclwv5a5zL-PUKKK77Fc4aQ-mrFQthEhHMvHAGsJh9et8hBn8N_SG0Ldbw1zFWYJimGxOfXN1sLbyNlQaDYwOhxySlpr6OTenWhpgrx-DZEe1Tlv-ON0OHCwdKgBXAb45XtP13s9Opah5Vq8FDuvV3QAfm7-qrYqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=jWlhoRFaUsAAZtW5xlYVDygUxt60-yoHMCgas2TOBeFOJJ9mZJpUALV4sME-weaYYov114ZhwuRq1jxZ0wdBzaY6_cVGPILqHFiu_trYbEl42JsagYDvsBcqR0Yy4QQSOC14WBINve-3qKFUWTMhfUz3vXNeghuMVTWs_EI-zH63YNtEtPM1lkclwv5a5zL-PUKKK77Fc4aQ-mrFQthEhHMvHAGsJh9et8hBn8N_SG0Ldbw1zFWYJimGxOfXN1sLbyNlQaDYwOhxySlpr6OTenWhpgrx-DZEe1Tlv-ON0OHCwdKgBXAb45XtP13s9Opah5Vq8FDuvV3QAfm7-qrYqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCK6Eb1t01myZ7fY0Pjdi_DgONsRtLIZwKgiEifPpMZDVv2rIif4IN9Yge16rMt-_hAn_eIO_w5t6RfDsof8KWx-e1jpfDR0Dcg6NneZMqsZ2rzJGbXuhfxcjFj-8Pz2yyGuAr1BE8xxW4OktoBOqE0p4cAN6wZGk1ZGfCXE6CzvZmlT_BTYIpe1hb8YWNJ63ED1cSITj8hVWfc29t6TiQe_rIYTdZd3W5R48VQMBschAZwbBuUuUrQdg0Nb6tg_bkHxw_Vn7TSKoPKoU4J-bUwIEykUjHIOLE3x0V4R_z7uYsjAViUn3gayEMZKZJfeC111K0PRCHjpCEtnHFnr8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViAnM8EpbA0nxbrrW06HluozV6mDp3xp1VES6dwALHubc7Vouv3cWpELEqyKO1IHoFpSxIxoaEyZ5mzSlB42fr5yMG_OheoPJKNUR0sJcDsjxMysA8WCKfSbBZLoC_T35ep0UbBW-JuuEwOLO6vvr76ACmFhGuDqNnKtHuQYkssbOave3Jq-1D9exq6tebjS8qaw0nRMp5MFPeiWbZA_niJye1rBgh1ahhlkKTxA_cYLh8jtxoT_qyHUnibtlspYZsUhOQoyP2qxH3fHNNFknGcKF0ngKQSbsmc2MO8zuYR2Busogo9mOZJP26rEpiPfpP7Ak2wILq7UafvWwaXUBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaUB3WHBTa_GLHL5MW7A2Hm6yrIZd7KPE_cgJ05O7PHxv72-_W7fRR9lqxSAk-GbEUkXXvniCKMYlZJK0TfxxUc2kqJIEwvG70aVf_3zOQt1hVY59EEhw6wBdunAP4XBwADSq01gry80aYtIY-dapyi9IEzFJARNVDH9BY-oO3IjVDhWe3GBYLo4cWdyOs1eQW0CkCS2pcAnpFWgeiDLCiVcZ2zYxNKFepSxFYF56VvKI_1MzW9yZuhlLuF3n0bUAbPyJKKOWEV-cdAozmLc0zLsAy8HZPpTsUJQL3np7DoH-BuPIaQsxsGUeDYmjKZvrt3W8_xDVIiLPi5rELP0KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=JOgZa9f9znXyv81olchxHRij61ghU1OV8J9f4eQF5Y7CObqOtBJRGbYP9YuuVShAn4Mg9FSj608j6mVTLMTsNfcj_Y4W-vx_sZPpYcX3wEVYUq8QzWNpKO74wh5U0VVZPpvv28xYDUN0PmC6uCCMZP0hDXKXl1GNsjLISxSOuYKMA6b_n043j2YRXZPns4Fca1h5Y_SkEsZSntb2dqd0N7AKgX13v_XdgZauS5nsQ_Iq1XA-ZEK2FZvul4nDlzxV8DUu9odXSIIFRPRPx30No70P1mMR6xhtnbpakHuyfKo23KcOeTucBOE0XLUi9WuM3WEVx-2n6D87zHLlqoOBSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=JOgZa9f9znXyv81olchxHRij61ghU1OV8J9f4eQF5Y7CObqOtBJRGbYP9YuuVShAn4Mg9FSj608j6mVTLMTsNfcj_Y4W-vx_sZPpYcX3wEVYUq8QzWNpKO74wh5U0VVZPpvv28xYDUN0PmC6uCCMZP0hDXKXl1GNsjLISxSOuYKMA6b_n043j2YRXZPns4Fca1h5Y_SkEsZSntb2dqd0N7AKgX13v_XdgZauS5nsQ_Iq1XA-ZEK2FZvul4nDlzxV8DUu9odXSIIFRPRPx30No70P1mMR6xhtnbpakHuyfKo23KcOeTucBOE0XLUi9WuM3WEVx-2n6D87zHLlqoOBSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtWxik1aoDWkKmjpOaCd8VKR11hiZtgkpInhTNW5dulCH9w8z0EYuqZmDbHLAXgDyMAD0-PvPJN8XQIe10Po4sJvcAyZWXd24h-U7xFU4pA8uNLYAji3LF8RPwhDV0oHDb9Qk3uxS6QhQv1adRhIH4i2Dh2mEdUeip1qTcacOs7uhSM2n6JQG3TApUlaEAs1Zkd0E70dKp-bq4pKp6UdablRg6ToMOvtf_UBqlzQBRwCdmVJhArA7313NYxefGU9SGCc9qd7yX02yCBE18Kdql3cyT59nkz40_JmBcEsL3KkKLAInhOTL1938a17F6-kWPOgQYKw2fjsd22ijTtyZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=ngcFTQTvxuoQfUrDutcjYcKZffNOkgkpsP-BdNILgwKsRjzwCQ6XSq5GaFXhXn0ElqgtYb64z3LvdxIC1Gd3COObywVDJiti89knzBQot5dl0lyqeNF7-F7Lh5BzIhaaVA4irAfuQ8-4oH5eAnCdquDWboweXGukPhtB-Jo7TigSSWj2c313k8U9vILbzMQ4Qdz3foaZQzqqCVX3wyJ2-0MTb5NDejwncmqItAe6rUe525C98yiqxRZZFYHqFHVN9MrDE_RKObPluBJ-FvSRQp3o4rrwR33DcOgtMdg18c7MnlNOdUIsC0BNEwPyQOgoXWZuLZoI4DWe4cdFXAzp6SjJs2562lg3DLo4Hr08Z03aZKXHrta9HtRN_1jFRj8r60bVfb0OvTKMBDLkigSs6RZOtczeOZLWPIOLbX-G9ngj9luZaEHWsQLShqgz-j4bw2Xvdfu4I5hjGVP5VAmE1gtPRgHfiee9x2c7hr1sGy4zr0jP8VZef6rkzeQSiNo8XSg6W-KZW2u7evsfHvUIAvzJI3YTd-mJwSnvBZCBoYgVP6q4VRO24ko8M4cZu24lNRGJNxyhgXo03YF6Xf6eXz10lqLx3oS8v8lmugGYhARDYnCe66ZdsCuDDqmg0YNYREiBvOdSPsDTHeaiKXS-freQ91zenfKnNZu3sUTxTyM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=ngcFTQTvxuoQfUrDutcjYcKZffNOkgkpsP-BdNILgwKsRjzwCQ6XSq5GaFXhXn0ElqgtYb64z3LvdxIC1Gd3COObywVDJiti89knzBQot5dl0lyqeNF7-F7Lh5BzIhaaVA4irAfuQ8-4oH5eAnCdquDWboweXGukPhtB-Jo7TigSSWj2c313k8U9vILbzMQ4Qdz3foaZQzqqCVX3wyJ2-0MTb5NDejwncmqItAe6rUe525C98yiqxRZZFYHqFHVN9MrDE_RKObPluBJ-FvSRQp3o4rrwR33DcOgtMdg18c7MnlNOdUIsC0BNEwPyQOgoXWZuLZoI4DWe4cdFXAzp6SjJs2562lg3DLo4Hr08Z03aZKXHrta9HtRN_1jFRj8r60bVfb0OvTKMBDLkigSs6RZOtczeOZLWPIOLbX-G9ngj9luZaEHWsQLShqgz-j4bw2Xvdfu4I5hjGVP5VAmE1gtPRgHfiee9x2c7hr1sGy4zr0jP8VZef6rkzeQSiNo8XSg6W-KZW2u7evsfHvUIAvzJI3YTd-mJwSnvBZCBoYgVP6q4VRO24ko8M4cZu24lNRGJNxyhgXo03YF6Xf6eXz10lqLx3oS8v8lmugGYhARDYnCe66ZdsCuDDqmg0YNYREiBvOdSPsDTHeaiKXS-freQ91zenfKnNZu3sUTxTyM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=ZW1e2VRay1jOY5b7R3y_CD93rAThPIRLUNkIspylav-9zoIgwT5uqIz1r9OIQayZnDnX7dTQ_E2kQhIK-kn3q2mEXkqu98-6g_Kheax9sFaXSUrZc2IItNG0CnKl9Nsa28qRjzuYT8pcF78SfzJuqpeQ9NhzoSSiASYXgXY-mz2H6NLgvR5ZWPMpZle5UI_iMyIuDBUYZ49fA8XQIuVbObr_OZdxd2Upm_kuP2dub8sIwtw_7vkzIp0UZtwivcRKTQ1pSdg91h4SN-rVao-29zBDwI5N_2dnq9aCzGJTRzPJlMmPBndC8M-N1ekGJFunKQu2J132tZ_y8XHTcxzgqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=ZW1e2VRay1jOY5b7R3y_CD93rAThPIRLUNkIspylav-9zoIgwT5uqIz1r9OIQayZnDnX7dTQ_E2kQhIK-kn3q2mEXkqu98-6g_Kheax9sFaXSUrZc2IItNG0CnKl9Nsa28qRjzuYT8pcF78SfzJuqpeQ9NhzoSSiASYXgXY-mz2H6NLgvR5ZWPMpZle5UI_iMyIuDBUYZ49fA8XQIuVbObr_OZdxd2Upm_kuP2dub8sIwtw_7vkzIp0UZtwivcRKTQ1pSdg91h4SN-rVao-29zBDwI5N_2dnq9aCzGJTRzPJlMmPBndC8M-N1ekGJFunKQu2J132tZ_y8XHTcxzgqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=ZlyLzgpvsFRk5G_jnPr51G5IylwenstW4YquXU13sGmFpgAtJdsZJ1BaVC2-qcLeFaz6jW6QAEZ3n41VkcJRlW4YpZ-DOSbYHvpSdVadea0mfUo7vb9XMJF_HcsY0n8wn5umk5Ld8NPar3nSTVyDqPY5e9AkGrWx2JfcHVkfoiTrCsd8ENqbrtRxQljzGceZGGQQruE0SN0OM_TdhaT8liepblJLkapYLGUZ4yyFyLcQiodgCyXCYi_nKWs3emXryGSZkwzmmFyB4Ab5dZTJXbLy1n6czO-mW-ihNeW8d5clZFYR2UUE_n7RE6EqFlDio3Lbg1-LDRa3iCsdbctKl7c15rsDl8AcmGkqFSYgcR81wQHpEGOR7CCzt0_H3uUzwK--oZL652qzNOzJ3kKXIvhPDZ3MeAveixYZzCVlxRWRGp6RT3Kk8ri1_pNSPqRVZGHTSgXz1aWZDv9xKX-Fz-RQHVo51n8WFmD3b6vSYcOZh45Xa9eqEQn4HeL75VHlBs0FyMAxgFl8w6iHinuPltcSm_RZxNp3go_jGH9Qu242vUdP3Ml8lQcMQa0AwOtow9nlLYJVDwA5VGUzqU0_v8_o1ZClAp796VML4YKmukSUAPbtU1R4LNU9LIaR0kh529qqrnIFkoV1XGDcPib8PbDwnwyG9t0w5OAjpz6Os9I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=ZlyLzgpvsFRk5G_jnPr51G5IylwenstW4YquXU13sGmFpgAtJdsZJ1BaVC2-qcLeFaz6jW6QAEZ3n41VkcJRlW4YpZ-DOSbYHvpSdVadea0mfUo7vb9XMJF_HcsY0n8wn5umk5Ld8NPar3nSTVyDqPY5e9AkGrWx2JfcHVkfoiTrCsd8ENqbrtRxQljzGceZGGQQruE0SN0OM_TdhaT8liepblJLkapYLGUZ4yyFyLcQiodgCyXCYi_nKWs3emXryGSZkwzmmFyB4Ab5dZTJXbLy1n6czO-mW-ihNeW8d5clZFYR2UUE_n7RE6EqFlDio3Lbg1-LDRa3iCsdbctKl7c15rsDl8AcmGkqFSYgcR81wQHpEGOR7CCzt0_H3uUzwK--oZL652qzNOzJ3kKXIvhPDZ3MeAveixYZzCVlxRWRGp6RT3Kk8ri1_pNSPqRVZGHTSgXz1aWZDv9xKX-Fz-RQHVo51n8WFmD3b6vSYcOZh45Xa9eqEQn4HeL75VHlBs0FyMAxgFl8w6iHinuPltcSm_RZxNp3go_jGH9Qu242vUdP3Ml8lQcMQa0AwOtow9nlLYJVDwA5VGUzqU0_v8_o1ZClAp796VML4YKmukSUAPbtU1R4LNU9LIaR0kh529qqrnIFkoV1XGDcPib8PbDwnwyG9t0w5OAjpz6Os9I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=agufmiJxN316vle3zVEhxxWxMd_Gr-JnnyNfErDYPAxi3cIytWuo8uWapOWHtvPde_1tWKwZGaCO9XaOc8DLsE7tEnIEQ4k2NlvdQthByw6n-d9dUsRkoHG7rtZ5ptHoO0txH-XVxl--TfGnAe-w4W02QVIDt9yQEJQjaa5kd_2gq1M4Q2P3133KdhtG8Ti7o81oJDIMdqvX_Jjr3K_xqrr7VUyMjfxXQMS-NTibKyUmnF37XNN_Klyrl4j3hiH-bMm8OH4Q1NuOBYaGMsBU6MwILhfVUDaoZe1M0_veE_rJsVjSdBboveMec3pvIRXTY_7tTP7nrIMJUGIbQNHZOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=agufmiJxN316vle3zVEhxxWxMd_Gr-JnnyNfErDYPAxi3cIytWuo8uWapOWHtvPde_1tWKwZGaCO9XaOc8DLsE7tEnIEQ4k2NlvdQthByw6n-d9dUsRkoHG7rtZ5ptHoO0txH-XVxl--TfGnAe-w4W02QVIDt9yQEJQjaa5kd_2gq1M4Q2P3133KdhtG8Ti7o81oJDIMdqvX_Jjr3K_xqrr7VUyMjfxXQMS-NTibKyUmnF37XNN_Klyrl4j3hiH-bMm8OH4Q1NuOBYaGMsBU6MwILhfVUDaoZe1M0_veE_rJsVjSdBboveMec3pvIRXTY_7tTP7nrIMJUGIbQNHZOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxLrfshLD_canyEMJzNDMxpNfzDll2Jp2AyKKMBF__Xj4KjEBFg6jz8Jfg60Qt9plfyejt_3xiqm3WCSJs7xch_WUdaqy-dAf8TE6uPfMMwSdbMYmnjIzGRkemNNVV5UgjsvkmbNWHDeSKJKLVwbN3QbYkw0flgu4BkduPuoqD3nWv3gUoh4FgDZD7R8WqmM3kPhur4TuUQZl6u6a_nLzQ7hSuv5M7YJWPgjT2cFEa2bkE3Xgzedo5olAK4ztK7SSRwu3SRyob315yd7WH-QhG3e60gJ1SbuQgL5UO1GIbmcGAw9or8OAO3Up87BeTz5z8anXkMojOyYsfJnf-Gwvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=PLSNauzFXVukP4tI76SdsEvMQfqsfZKu1XXsB_GP7jBEbZWETPHYqtBz3IeUHUXxz9r73Dl8bTXc9CUrfh7uR2dhLgr4RQ3EStyQLdyMPNK__HEABnExliZrV1-itkS_XFE-341VmnyU2afKun6t1tdBtsp0ZUpk3QMbA-Fk_xuWWnIfYR8tDlbHZSJUn3h8Jy8xr0MHKajUUz4jhGiXPVfDTyk_QUySQiXxonWJNRx8XvYQOtLsJ6G77-bHxfkEmv_hnzD-lUbydzZVVBaBP84xAdfcUY8MsDNDyKv147i47TksnonjO1SxKByHG_ozG-bPMiyAfs55QWz8jO9jNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=PLSNauzFXVukP4tI76SdsEvMQfqsfZKu1XXsB_GP7jBEbZWETPHYqtBz3IeUHUXxz9r73Dl8bTXc9CUrfh7uR2dhLgr4RQ3EStyQLdyMPNK__HEABnExliZrV1-itkS_XFE-341VmnyU2afKun6t1tdBtsp0ZUpk3QMbA-Fk_xuWWnIfYR8tDlbHZSJUn3h8Jy8xr0MHKajUUz4jhGiXPVfDTyk_QUySQiXxonWJNRx8XvYQOtLsJ6G77-bHxfkEmv_hnzD-lUbydzZVVBaBP84xAdfcUY8MsDNDyKv147i47TksnonjO1SxKByHG_ozG-bPMiyAfs55QWz8jO9jNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=W6uT7dJTRoDD6Ghs0i_noPdJt2Msfe-pahMf2orvDC1eten1cYVuVEy3EAzXZMotcDBc56UA7LF1g03fNcIchPCDNDLCKCPlbuQTHOj-WJ7jkaz-iPC_JMZOYKnPzO6oiSJ_en8KMi5aur-97zJYCEfREQAkBW4hvxKScrLL3Rs4csq8wi3hm-j31BZggUALA87ib7CNv_3jILs63a3hIlc_j2C_m4V36rFlXxxXYy9nXxQMsF-zLQAL_TJSFV1IbKp2jE8wQ34zlN7ZTM3YI_89qAr_Ah_5kJJVkGsTiX_n64YtWs-4KlflZVfz2yu3Lpc43BHh29zZbEfMSbRB9SO_Jv9krTK7JrTiuzR2QTkskBS_wfgrfaRLrDdszGXe95xIgGINz6P5O9qnPmcSmaVEdf-EfZMa3lKeGGo29aVWkYHThlpbhrT0GDwp47bZSnclVZDR2XrtbRcWvlzzxwfj_-RqmgfgMyJjX2x_maSw-LD3k3Uq9FTJjfGMgpGTWvHdYQiuP4mCkU6OM-fcXu1081UyZMWAejFctLnat4tyKqN3KplT__ZGTyMejOmBDALz_GfD2r8DAASpb0D5dvAuHXSN7jaAoPk4eneiVi62kdQG_CmpQvMw-YbVor93J_dxjUAeOS0VvEAUvuj25vT2EJdPeWMF73u-YnLLUFo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=W6uT7dJTRoDD6Ghs0i_noPdJt2Msfe-pahMf2orvDC1eten1cYVuVEy3EAzXZMotcDBc56UA7LF1g03fNcIchPCDNDLCKCPlbuQTHOj-WJ7jkaz-iPC_JMZOYKnPzO6oiSJ_en8KMi5aur-97zJYCEfREQAkBW4hvxKScrLL3Rs4csq8wi3hm-j31BZggUALA87ib7CNv_3jILs63a3hIlc_j2C_m4V36rFlXxxXYy9nXxQMsF-zLQAL_TJSFV1IbKp2jE8wQ34zlN7ZTM3YI_89qAr_Ah_5kJJVkGsTiX_n64YtWs-4KlflZVfz2yu3Lpc43BHh29zZbEfMSbRB9SO_Jv9krTK7JrTiuzR2QTkskBS_wfgrfaRLrDdszGXe95xIgGINz6P5O9qnPmcSmaVEdf-EfZMa3lKeGGo29aVWkYHThlpbhrT0GDwp47bZSnclVZDR2XrtbRcWvlzzxwfj_-RqmgfgMyJjX2x_maSw-LD3k3Uq9FTJjfGMgpGTWvHdYQiuP4mCkU6OM-fcXu1081UyZMWAejFctLnat4tyKqN3KplT__ZGTyMejOmBDALz_GfD2r8DAASpb0D5dvAuHXSN7jaAoPk4eneiVi62kdQG_CmpQvMw-YbVor93J_dxjUAeOS0VvEAUvuj25vT2EJdPeWMF73u-YnLLUFo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_2eWqm0LbE1G-JAt_6ORKkK7K5mC_qBdONU1o-CLIKItqb3SbKU116XLFZRHGk4WfA12SzTNUjL4l1UGHivQUtXZRV0bVgmQFV54aYiWnW-q9_InNSFVHGF33G7I-ZwMqwwTSChsekS-4t2Rhqt0OSguT6cAiB9PB6dN1fY6NW_LoOscQboFQL5GWEIPvAOSPke5BM1Zc92e1CJ6mGw5VIX4L37RJ2K63tKMulzBpJSRZD3cuSOYfe8Rw-c8fVB7U4LzQzJnluM53xd9b6gs00WE2LITpA9XmAfZeMtEM6h-1p144pb16Ez4fmwTAjgtX4Q15mYHzRkKEdt7vkNdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=gT0EkB5DW1jlVHgjb3q1VOznz7pQqdOekdgeCYAozmGQGOCcWji8c4LZbNZ5QGAkWY5RDr3PN2x2KRHF66-ojvdUbzJ0InhHkaAkfB7xNj-8hr2VcAI-FR5MhzLZwBob5ZoKbzwBxwEeZegbQYKWMR7M-P2fz-n7najzejKy269RFrvRemAQbNv8Pe7wIVyScct6pTH6GlHw3j_Oa0aZtCdAf99os8lLuUnUl62o30iYSrGNfr7__uTrHcGrTO189JhYFCD_eR6uq0cvWPDP9jTer1AmXINk_UjBYjDkgQQFwDmEW0oBSAWRdDY0hs5lk6N7TzQxLG_wjoFOQyVW4zHJrBwLVKgUGlR2QFmqQa6-0Z4EvOHrtwnuw27OI0bwnKnRTIu7jq8puLrE129wluiCYnYiHW9yPI9Mq6sOLXDGU0yUPWyROFzWPz8F-GjsNRf578n1sGAABVKJh5uuU4unO-GbV0TjhgAEO_wrx8ExjmAAAPFmm45lS7qcYSQU3LJRr1XxAPM_pqjLBCvOScL_IxpGeDPGMSQt7zGj-xljAKc-QvIOACpI8nXshgYGOr5L34asXrthKpQarOvPe1ms-Noqyhy-GmTyk9su94LTlGEmlhHM4zvZ5AvLvB1aLWQla4UmPaAQVB3NEqSknYPe7e1CQjyj8CQ04leP1NE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=gT0EkB5DW1jlVHgjb3q1VOznz7pQqdOekdgeCYAozmGQGOCcWji8c4LZbNZ5QGAkWY5RDr3PN2x2KRHF66-ojvdUbzJ0InhHkaAkfB7xNj-8hr2VcAI-FR5MhzLZwBob5ZoKbzwBxwEeZegbQYKWMR7M-P2fz-n7najzejKy269RFrvRemAQbNv8Pe7wIVyScct6pTH6GlHw3j_Oa0aZtCdAf99os8lLuUnUl62o30iYSrGNfr7__uTrHcGrTO189JhYFCD_eR6uq0cvWPDP9jTer1AmXINk_UjBYjDkgQQFwDmEW0oBSAWRdDY0hs5lk6N7TzQxLG_wjoFOQyVW4zHJrBwLVKgUGlR2QFmqQa6-0Z4EvOHrtwnuw27OI0bwnKnRTIu7jq8puLrE129wluiCYnYiHW9yPI9Mq6sOLXDGU0yUPWyROFzWPz8F-GjsNRf578n1sGAABVKJh5uuU4unO-GbV0TjhgAEO_wrx8ExjmAAAPFmm45lS7qcYSQU3LJRr1XxAPM_pqjLBCvOScL_IxpGeDPGMSQt7zGj-xljAKc-QvIOACpI8nXshgYGOr5L34asXrthKpQarOvPe1ms-Noqyhy-GmTyk9su94LTlGEmlhHM4zvZ5AvLvB1aLWQla4UmPaAQVB3NEqSknYPe7e1CQjyj8CQ04leP1NE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=dcUM9RhcOl6zT-WC0lYHDwpNl0iQQhqwQjBUekEOvicuH2ZRrju_-nWiVK8dM6Pnuwytydoeb7yhxUvdzEgsNWPbZFA6Q0x0nKPT5tSD_M2VNZY0Jtu38_Lpj66LDh4RsJLNOZuHH0_TLJlPKzoY7ai7vsu0drDLTJV1qoH2ptd4CNdEXVFEBSs1TDGwHQGzi0tWCoJ-yYK5V1suifBPC5wgYhBSdjCcBSG6waTuaiC7_mU0rCP3k96X0M8vpWDd8PtujOOKYcElxvMAQMw4QWXRONrHXNZH-Dy8ZfTHLLzSVgf6cdiUDEcFn7MekrxXn291ETUBxTJBta_AwjaN3RXo5A1c56S49puVVIjETd64gaI3In7lDaR6TKGYvdBHXwd6C7PKdaXiUQ3PjY8AyGBjDBhzDhfixi40XChsbpATn21JSdO6mwd9boPAwnEfOX4RHkz3ma96d4wB2KcbSctBMSL_MiFZ-WcFyeRFC7zY0pPYpO8bFMDEgzQJFFmV8aChG-6QHiFGSj0OpGlFVku-CMwE4UGlYQP9ajyqpP8qVolKdKkVJVCQ1Mhxgz3V010egz0IGtiLqGYt2BJ4R5DW1O_Nifu7UoMxA_3x5zi3h2GLCk8MFfaUiLD97oLy91CvgSJBh6jrM9hBqcA4zW5bCjyCP02ddk0v3QKmhy8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=dcUM9RhcOl6zT-WC0lYHDwpNl0iQQhqwQjBUekEOvicuH2ZRrju_-nWiVK8dM6Pnuwytydoeb7yhxUvdzEgsNWPbZFA6Q0x0nKPT5tSD_M2VNZY0Jtu38_Lpj66LDh4RsJLNOZuHH0_TLJlPKzoY7ai7vsu0drDLTJV1qoH2ptd4CNdEXVFEBSs1TDGwHQGzi0tWCoJ-yYK5V1suifBPC5wgYhBSdjCcBSG6waTuaiC7_mU0rCP3k96X0M8vpWDd8PtujOOKYcElxvMAQMw4QWXRONrHXNZH-Dy8ZfTHLLzSVgf6cdiUDEcFn7MekrxXn291ETUBxTJBta_AwjaN3RXo5A1c56S49puVVIjETd64gaI3In7lDaR6TKGYvdBHXwd6C7PKdaXiUQ3PjY8AyGBjDBhzDhfixi40XChsbpATn21JSdO6mwd9boPAwnEfOX4RHkz3ma96d4wB2KcbSctBMSL_MiFZ-WcFyeRFC7zY0pPYpO8bFMDEgzQJFFmV8aChG-6QHiFGSj0OpGlFVku-CMwE4UGlYQP9ajyqpP8qVolKdKkVJVCQ1Mhxgz3V010egz0IGtiLqGYt2BJ4R5DW1O_Nifu7UoMxA_3x5zi3h2GLCk8MFfaUiLD97oLy91CvgSJBh6jrM9hBqcA4zW5bCjyCP02ddk0v3QKmhy8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=GplwWUjceQtatuNd5aoyNXE_1viJm2SCXURZFA2_KU7BTPboyjhkd5PU_Wonyu0HGJlNtaw4L0n8mzkzvBahVZKNrcv7U-5sGWtNZF3ifGfs3ikbhHlaeTE7IzQ45yAx8kKD3px_jxVjB2lvILRLW8-9JbfSVY2ISdPTmVfaVgLoK0Htj7X17QDtS-fIgveL0K7GHSf_SUUmIcJRDpfCqQHyT_dfAm3xm_Nk8ay4ZkcM_vIxTMwkyzkxSlwqLqNo1IwzI23uErvDilaqwpjOTJI4ycAu6mJqaLj6xb4XLDX4SHJF2MN8cPyHSh47T74HuqS0RBuibxNrF2WJAruhgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=GplwWUjceQtatuNd5aoyNXE_1viJm2SCXURZFA2_KU7BTPboyjhkd5PU_Wonyu0HGJlNtaw4L0n8mzkzvBahVZKNrcv7U-5sGWtNZF3ifGfs3ikbhHlaeTE7IzQ45yAx8kKD3px_jxVjB2lvILRLW8-9JbfSVY2ISdPTmVfaVgLoK0Htj7X17QDtS-fIgveL0K7GHSf_SUUmIcJRDpfCqQHyT_dfAm3xm_Nk8ay4ZkcM_vIxTMwkyzkxSlwqLqNo1IwzI23uErvDilaqwpjOTJI4ycAu6mJqaLj6xb4XLDX4SHJF2MN8cPyHSh47T74HuqS0RBuibxNrF2WJAruhgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=j3DDTrUbKaZ6nPo19H-VCTh3XberMuHW7OEeovQjakW0Sdg7bL0yC9chM1n_5sOld6MTfLDURAiMu7aSW1bg6YMkHg7QI54STFN-V5n_kVMD4ZUwBdCXPNnwkVZ_0QjqDUqXX2OVc6vhoVLWZvssIO8yYjKUjXFkPxrz0Xk6nTx2qSJuQSc6EHTZrAKkrOC_Da9XGG4jiQXUTKk0vFN8wLMATZzftbEUUztbVWqtp-3Jji2oAK8-2IXS3cXGifFUI31E6fkAksLDX87vXNkmAdLw5pea5VRGFNOs8zoVB46XSslEhEaCIzRAd7lMbwquXXoyNOcGJ2UiS-iE7FrW0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=j3DDTrUbKaZ6nPo19H-VCTh3XberMuHW7OEeovQjakW0Sdg7bL0yC9chM1n_5sOld6MTfLDURAiMu7aSW1bg6YMkHg7QI54STFN-V5n_kVMD4ZUwBdCXPNnwkVZ_0QjqDUqXX2OVc6vhoVLWZvssIO8yYjKUjXFkPxrz0Xk6nTx2qSJuQSc6EHTZrAKkrOC_Da9XGG4jiQXUTKk0vFN8wLMATZzftbEUUztbVWqtp-3Jji2oAK8-2IXS3cXGifFUI31E6fkAksLDX87vXNkmAdLw5pea5VRGFNOs8zoVB46XSslEhEaCIzRAd7lMbwquXXoyNOcGJ2UiS-iE7FrW0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=Pg7KQru3PQ-CIA3YZBxKQnFUTNyqVBEM3HD2xJ1f9yeil4CkxGacA_YGxUpIrMLnL02DMOyRIvxbzyJLQ2lNyULRkIq_7dKsr8bfAypU43tLRATwctCtXhahzrU3AC-PLPgOd1myljptTELQaqit-rENcOTaePry_g3_-BzFulNZs5IL-cnpoOgEd65LS703I_nnddUOfiPgZGNYVls039qnT3LtwIYzYkFvxQjGTrgOwnPPgCe27Wd_VzinBRUNrM-gVvz05r_1kVsBnQj95HPoSL5wcxEePqswg1vxx69DdA0JOsyuKC2GwXPk1CMs0W7A3h8ZU-XaCyBBbAqpUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=Pg7KQru3PQ-CIA3YZBxKQnFUTNyqVBEM3HD2xJ1f9yeil4CkxGacA_YGxUpIrMLnL02DMOyRIvxbzyJLQ2lNyULRkIq_7dKsr8bfAypU43tLRATwctCtXhahzrU3AC-PLPgOd1myljptTELQaqit-rENcOTaePry_g3_-BzFulNZs5IL-cnpoOgEd65LS703I_nnddUOfiPgZGNYVls039qnT3LtwIYzYkFvxQjGTrgOwnPPgCe27Wd_VzinBRUNrM-gVvz05r_1kVsBnQj95HPoSL5wcxEePqswg1vxx69DdA0JOsyuKC2GwXPk1CMs0W7A3h8ZU-XaCyBBbAqpUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=V_aMo9wQB-32Ch_bVmCoUekD_vHkkjBlkKx8BFbnf9b3m8C4B_fRSBCZYbMxppPuLbQhlhuFCe651QNb9IBfYVY-2rv4VwygpRJyTqsoxohzZpkCz6TJ7crwDKrPskGTgGLvwqrIUssD9yu8QxCnJYNbiDVDglqKGTdYr2TiW-t-_-gaFytgyYtQ9WeGvK9N1SXuex3tOQDVhUsRuO6ws1Dh3p82cQGYpXkL1i0vpvbr3qDHiUOZ8nJmhrwefP2ljC-p0jd0lN0s8rcLcAew9D0i3Qw9S9lvsc4HmJI2hcYyT68xdHUlNDC0gxCb5PN-mBtpvn6EpZlo0H0An4m8Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=V_aMo9wQB-32Ch_bVmCoUekD_vHkkjBlkKx8BFbnf9b3m8C4B_fRSBCZYbMxppPuLbQhlhuFCe651QNb9IBfYVY-2rv4VwygpRJyTqsoxohzZpkCz6TJ7crwDKrPskGTgGLvwqrIUssD9yu8QxCnJYNbiDVDglqKGTdYr2TiW-t-_-gaFytgyYtQ9WeGvK9N1SXuex3tOQDVhUsRuO6ws1Dh3p82cQGYpXkL1i0vpvbr3qDHiUOZ8nJmhrwefP2ljC-p0jd0lN0s8rcLcAew9D0i3Qw9S9lvsc4HmJI2hcYyT68xdHUlNDC0gxCb5PN-mBtpvn6EpZlo0H0An4m8Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=YXCWBZXynuQI5nq2Iufkzqb6hc3KbzxkGydSTzb7PX5UdmzCmzN0ClqKTb3KBERjClkagGEp6iP6sbq-_5X5KrDhx09ICDNl_ehDW7yqnbN_iNse8OgSup-YtKPm2fNndzUae8UDUVhdYuA-OUNXqlcEzs1vxE8rTKOFkzxY9mMFpGg8XHH8m77-8CwYwOXQRtMu4hASpoRFQYmYM2oFnlapXQoG-iPHW8wP-1yyba5N0GnEaEFCY_n543tcD4Fxz_6fLeBI13OOS1G1XnH7ljn__mrj-59xu_DHR5z0W4gRN6OVG0QbjATRyarQ_V1fAyK1lJmBp2KnGj2G5Y4mGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=YXCWBZXynuQI5nq2Iufkzqb6hc3KbzxkGydSTzb7PX5UdmzCmzN0ClqKTb3KBERjClkagGEp6iP6sbq-_5X5KrDhx09ICDNl_ehDW7yqnbN_iNse8OgSup-YtKPm2fNndzUae8UDUVhdYuA-OUNXqlcEzs1vxE8rTKOFkzxY9mMFpGg8XHH8m77-8CwYwOXQRtMu4hASpoRFQYmYM2oFnlapXQoG-iPHW8wP-1yyba5N0GnEaEFCY_n543tcD4Fxz_6fLeBI13OOS1G1XnH7ljn__mrj-59xu_DHR5z0W4gRN6OVG0QbjATRyarQ_V1fAyK1lJmBp2KnGj2G5Y4mGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=QBaibRxOvR0_lppuAyRxBWXsfPPp_genUlEpx0QqmJlcbW-HDKuK5PB7oBCd_Fi3u-RCXDBlj2XZ5fhpV0Pzf82chifVQM6xzMdGMXMWCA1Af1uBpPpzMk9JRl2cvDP-sTiTPqjHxDZh7QGKDlc533bwrPhvZQ1phh0C95Y8MlKiqLk777JUf3m0tSgLvhqut06_RNGybEI4ZMl32uMz8NvC4bHfdZY1fhazqENgs1ivWisQkMMd3r4pJAlZfGszp5636XzfHB_EYtDDs6nkRmIK0xqzpwDwLwumheJQGceCHH9znKlwV1gB_XETIsQBkMtgYT9VclaWdW5GMlPXBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=QBaibRxOvR0_lppuAyRxBWXsfPPp_genUlEpx0QqmJlcbW-HDKuK5PB7oBCd_Fi3u-RCXDBlj2XZ5fhpV0Pzf82chifVQM6xzMdGMXMWCA1Af1uBpPpzMk9JRl2cvDP-sTiTPqjHxDZh7QGKDlc533bwrPhvZQ1phh0C95Y8MlKiqLk777JUf3m0tSgLvhqut06_RNGybEI4ZMl32uMz8NvC4bHfdZY1fhazqENgs1ivWisQkMMd3r4pJAlZfGszp5636XzfHB_EYtDDs6nkRmIK0xqzpwDwLwumheJQGceCHH9znKlwV1gB_XETIsQBkMtgYT9VclaWdW5GMlPXBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=bPYYUvR1ej1f2vnKIydVWetRR5xWKwEBrg-G1ddxNN4zJ-hKC5E9PURslPIiJHyd_siK2XETKOluSwr3CuHwBQFkSXsiFYFjQJ3lbBB9yD3QfbU10vx0Hsg22-TZYiqmIutUrg_hig9q4aKm6aSdeiycpyw3p4KvdYXmfTWcaQgmVY7b2ddfNY6k--65z02uI6ohyPkGIHpm3Orj5stcMRSI2hw1-EsOAqTWYqSF8NFQRvzJh8fVxiSw-tQgeVUfhA1LokbrQuR4bbXGSwN4g_p_a018BJt5yv9vQGBXxwLUCb8TCD9qVpHUueH8yXQqTEdd2zUDfKWlh7D2k7XqqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=bPYYUvR1ej1f2vnKIydVWetRR5xWKwEBrg-G1ddxNN4zJ-hKC5E9PURslPIiJHyd_siK2XETKOluSwr3CuHwBQFkSXsiFYFjQJ3lbBB9yD3QfbU10vx0Hsg22-TZYiqmIutUrg_hig9q4aKm6aSdeiycpyw3p4KvdYXmfTWcaQgmVY7b2ddfNY6k--65z02uI6ohyPkGIHpm3Orj5stcMRSI2hw1-EsOAqTWYqSF8NFQRvzJh8fVxiSw-tQgeVUfhA1LokbrQuR4bbXGSwN4g_p_a018BJt5yv9vQGBXxwLUCb8TCD9qVpHUueH8yXQqTEdd2zUDfKWlh7D2k7XqqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4en2ngsqlzMS4ZykOVGOWoh46hxe9C29wrO3jbBWXPuC0xu_OkYfwNUjIaiJ_I8grsQwAuLrINpNBYVgrMUxI_f555LRfLiGjiUvfdGjy13AqHFL90qkoZLStKRJC5DEN6nxQgY1339h440iWaEwm3LRR7hVSXeyuRcxkHr2KppcXZ7fFSPqIRbjNE50f0qWWZon6pyMO40QZufbHPyV4ZotQF0b7BFVzUdCfZxO8Ala7zLyOfkHnjZp77KcRr2bsNj6JJPRrk3V-mcJxRaI51y3qLUGcOJeO_9ZGnR69AbpgogkguubyK0eiBCpwKqjBZ8dEr5vdTXC6hwoQCGjQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=fa6h-n82rNYUufdmNGAvsXHtWnppPiWw5uMXXltVvS9vP4EZMOGH03l7wSjJMGWwRjpcX9HKkcNfozStznQpiHLDqRw468Gn-4N6kNIBG5rCoAkRydxPtjJNAczOsIOC145x0u3VZW4a0GkY7jQAYeGQ7L9xliRvRZUNeEBqG9Kz32s6EsW-CoLAlTZ-EzXkC6Z1iHxGIW6ZxJNU2QkFtQ73kSCQk4YKSU-jWzcW0rZ1eSsKBZx2NTYskJsCgSC_EOPni4oMueOEPlZyzo2np72hMSb9nBbLvJ14RLOGYTv3Qwr-UjR3azfI2GB_TLJcmR46glKuDbbMrIPS41B1yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=fa6h-n82rNYUufdmNGAvsXHtWnppPiWw5uMXXltVvS9vP4EZMOGH03l7wSjJMGWwRjpcX9HKkcNfozStznQpiHLDqRw468Gn-4N6kNIBG5rCoAkRydxPtjJNAczOsIOC145x0u3VZW4a0GkY7jQAYeGQ7L9xliRvRZUNeEBqG9Kz32s6EsW-CoLAlTZ-EzXkC6Z1iHxGIW6ZxJNU2QkFtQ73kSCQk4YKSU-jWzcW0rZ1eSsKBZx2NTYskJsCgSC_EOPni4oMueOEPlZyzo2np72hMSb9nBbLvJ14RLOGYTv3Qwr-UjR3azfI2GB_TLJcmR46glKuDbbMrIPS41B1yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=uNtH6DdaHgcMgonM3IiYcb4lthTfiKbPGjVnAnz05X-XVxbSZvEB4v5AppqJigNb1hxWscnOsXI9hEr-9z5YNYU1Gpjjaen052qsC4XyQ79ru_tIYtpei3EEGeFUIfD0_EktP89KV4f5UHKa4IlQ-yQUj_w0YFgU9UuUsAEBEtfSukH0maLv6dyoHFLeaGUchLiJhhATW_EtWI-taDCEajWCLGhE56IUQHyYzY58t_u0Bn_cULFqWQP9rlxHBy60ux6MJYNRvotu677c8YPK_i4Hcd6N3q10RoQR2H4nnKvbN75l9umuHWouxb4bzCkT4UnnON8ghGU7shXnkqNdMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=uNtH6DdaHgcMgonM3IiYcb4lthTfiKbPGjVnAnz05X-XVxbSZvEB4v5AppqJigNb1hxWscnOsXI9hEr-9z5YNYU1Gpjjaen052qsC4XyQ79ru_tIYtpei3EEGeFUIfD0_EktP89KV4f5UHKa4IlQ-yQUj_w0YFgU9UuUsAEBEtfSukH0maLv6dyoHFLeaGUchLiJhhATW_EtWI-taDCEajWCLGhE56IUQHyYzY58t_u0Bn_cULFqWQP9rlxHBy60ux6MJYNRvotu677c8YPK_i4Hcd6N3q10RoQR2H4nnKvbN75l9umuHWouxb4bzCkT4UnnON8ghGU7shXnkqNdMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=G4rppuPcjVtWD50w1QPMlISU6-zHvyp_6lm21E4QNMRYhaXAHJ7xf6O7hbWuyNmuEl4rhyGf1ZwsaVtkxYl2gtrUvuy8j__qg8M98JSfNeo9lld0fj7Sl3xyUCIxxZVn2gVklNYHpnn5nWQ4W8uN8Cc5Di0Yv6oKU8JD8AdY0hIJTSokkA2egOsVa4tjsJ8kiY61XaeI1SdRJXwnV3PxNsawuAKU3bQquZiM16s7130zTb3Zo1DFbnwpSURJChYZ-v79powWp654f-xxeIT7hbWZKJEwH0EGE59Gn3GVmOWobWeNRmU2V5auEnzAyqLAsx_dO9zNZkyvttICdgTcNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=G4rppuPcjVtWD50w1QPMlISU6-zHvyp_6lm21E4QNMRYhaXAHJ7xf6O7hbWuyNmuEl4rhyGf1ZwsaVtkxYl2gtrUvuy8j__qg8M98JSfNeo9lld0fj7Sl3xyUCIxxZVn2gVklNYHpnn5nWQ4W8uN8Cc5Di0Yv6oKU8JD8AdY0hIJTSokkA2egOsVa4tjsJ8kiY61XaeI1SdRJXwnV3PxNsawuAKU3bQquZiM16s7130zTb3Zo1DFbnwpSURJChYZ-v79powWp654f-xxeIT7hbWZKJEwH0EGE59Gn3GVmOWobWeNRmU2V5auEnzAyqLAsx_dO9zNZkyvttICdgTcNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=L__X5nGPFRhgaFcEE-RhwROp_egJkZKXD9IS3rbQX5OXMPbYzycditi9AR0bjKawQWX3FxE9jj5B63T5rTBFq9SyYwBhWyNwS4BsvdjYFVhQ1lbewI01v5_SUZJ6BOb5x9hjad2QKc0MYSXW6Duo7OWVeXg7ija60vGAzgEpW3IPMFwQbrQUL-I3rC7pWunp3IYT4ful96au-L8KgC27sS7y-p6VsLUHLOuvvVVEdywI2LLBjXwcrohOx3arqXrozyj4LVn9SBz--RMargzkHqznAz2xAqvCbAmN-OdjcZw12V3ANDDXkjKHwY_1VRb33sy2hakzHVKjCjDJ08PqdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=L__X5nGPFRhgaFcEE-RhwROp_egJkZKXD9IS3rbQX5OXMPbYzycditi9AR0bjKawQWX3FxE9jj5B63T5rTBFq9SyYwBhWyNwS4BsvdjYFVhQ1lbewI01v5_SUZJ6BOb5x9hjad2QKc0MYSXW6Duo7OWVeXg7ija60vGAzgEpW3IPMFwQbrQUL-I3rC7pWunp3IYT4ful96au-L8KgC27sS7y-p6VsLUHLOuvvVVEdywI2LLBjXwcrohOx3arqXrozyj4LVn9SBz--RMargzkHqznAz2xAqvCbAmN-OdjcZw12V3ANDDXkjKHwY_1VRb33sy2hakzHVKjCjDJ08PqdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJDf9psXi56spZrdk-cn7nDI3_owIoNlIEtrKY0sde95KXd3f8GdQe7yKfjE_fcGPlEjmFUddBPq7egnKldXi-XhZTObMqNsp1eXmYV-CtFxh3mA2APDlDhGvsLCKcSIx3Az3j6-qaCGL2qm3--qcA1tH6g9FyBDf48Nt6Sz3WY_hR9-P_10e53mdAtj9S9arowah8KuMmQAHQoTp_7w9EhNjRVQyP_kmi1c94ew8gcH2x1z55wRm5FEawWjgpE2PXIHqIJ0wVgL2lCg5a0kAHmnBhrc8P0eCjDiWBgQWz_SJlTip8awVbR4C--zT8fszEyrpYuQPAsShZ0HvMxmkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=Rji20RunSHnZCXf1RCpkENaV_Lq6g6D-6GdsVys_QQg01_CVx_HZy7CqRIDd0cSh2kZedFORbJTkYJgfzjBCJVcVqS-ZL2nK4M6Zd6N9zu0RfLVcRAkgTlLyrsKAk-XSphXqMWrIarF0CfY3AR4RSrzHMhYOb_lG_efovelT0uk2XBI0tj3y8fZJvrAxNkNyQno5x491QcUP3XM4DDlVK6bpXGaAwUSeYfZLlHhJxMnQzupZbSltDqgP2oKMwoIQiKkNoc_1QUCVJCDUNqDPUOPd8-0NiHP5job0l0DSpaCQZ0tD17Phu3dxZwT5SYOMPXrIqyBaUaAhOXIrYI7S8zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=Rji20RunSHnZCXf1RCpkENaV_Lq6g6D-6GdsVys_QQg01_CVx_HZy7CqRIDd0cSh2kZedFORbJTkYJgfzjBCJVcVqS-ZL2nK4M6Zd6N9zu0RfLVcRAkgTlLyrsKAk-XSphXqMWrIarF0CfY3AR4RSrzHMhYOb_lG_efovelT0uk2XBI0tj3y8fZJvrAxNkNyQno5x491QcUP3XM4DDlVK6bpXGaAwUSeYfZLlHhJxMnQzupZbSltDqgP2oKMwoIQiKkNoc_1QUCVJCDUNqDPUOPd8-0NiHP5job0l0DSpaCQZ0tD17Phu3dxZwT5SYOMPXrIqyBaUaAhOXIrYI7S8zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=CO33BwDX_bBp9kD3rBN0JTe2SDiTzWWMSVu2dQDqZbtuPEK8sR-KZd0UlK2qj4S7_2WSkZtJedlaSN6ywdSqlac0uU-bAbdHAzNqzRKJ6wxTR8HqFRpYAa-3UUWC5kF49fCT0jvPnD1gzP8zkrjPuIKP12zfBkl80fSir6TcXoCHC5Kgs936AvH3fhLBB-cgryh_PT61DT3SFtEXH7A7M40csD_Ecv-g8HEYOsQk3Z6gEjtziSffaT5oSICF4mxlQogfb3BJWfqGw1UakGh7v0_sJYjKXr4znqnXndm0_KcDyWySJIC-ZirGMoXedHKGbuwJrFHDF_EPwld66_yDjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=CO33BwDX_bBp9kD3rBN0JTe2SDiTzWWMSVu2dQDqZbtuPEK8sR-KZd0UlK2qj4S7_2WSkZtJedlaSN6ywdSqlac0uU-bAbdHAzNqzRKJ6wxTR8HqFRpYAa-3UUWC5kF49fCT0jvPnD1gzP8zkrjPuIKP12zfBkl80fSir6TcXoCHC5Kgs936AvH3fhLBB-cgryh_PT61DT3SFtEXH7A7M40csD_Ecv-g8HEYOsQk3Z6gEjtziSffaT5oSICF4mxlQogfb3BJWfqGw1UakGh7v0_sJYjKXr4znqnXndm0_KcDyWySJIC-ZirGMoXedHKGbuwJrFHDF_EPwld66_yDjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GwnNaFC4dB4icKKGJuk8kHJMt8HHann5-kV8dlzGrt_K0Ot8wQVHVcGiggVBYJ7NivDmn_Nc7AMyozpFMIxdFdzXKuarNXys_W9DUKJ326wcJDGmy1vJI5VfqH81xYXVDk-jE2DwXZptRr5MVYT57nsAUUQaJ7R074AtdQvicMri_SAtnOtXIpDqhKjoQNiAmuwaxC3OfakqRMXw01xNt38f1S9mkmz5IhTAvyDahJgHg0uMSoBpxbMODEvsPhCHDRYW-BlGDYXSz0OGsca6A6l7-d-bqo103fzd5sPopZ8r4F03VtQOBFAE-ep2esE5nHJ0lM17S2JBlE8v_LYrlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vSGY1JJYaq4EUDFX42gzCXrjByfJdmdVMa4lG0GHwDGuiBBwIqxn_nXqdsaPvRXmVSvLGe2uGGg8IWvU8DcwdXqtceyVv529atruKUGlkc_T28OMXPzbR02X-ocpEkbRQqwPlgxtWFA6_OXRDijy_p5FDI_quqbYvXuOlkEnIzf9nmyHBcoaaeyk7h1xkYECe2rxtX7nlBA2s5TgtLulVAJ4yy4fmeZCI2uCtKuLnoIDhrw2wPr2qjPbF0BPAdiIlZrw7oYLgYRsuwrxTRZ_XwDl9y1DmmIrQJQVfEu6LdPb77TOU_05CG13GTgeBEb9mEhNuXxQsbX6pDTOzQZdAw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=aws1AC-8CZ9BmJlakQjs5NTmgP_a8a2gqJbcH6OfsG-Maj4Yg4TbqusiokuAJMLwmdX9MyAGclW6_qONTWlgVP_bMvcYCCvhF9h1VHnweteY4defdIrMiffJPDoO6_Wj4gPMsDj4KdN6A3UUO7jXuXI7sAebMQ9HZK12XL6HCuYiMRFI8dFOn7HVSetppy4s9Dk1cHpDSpCeU1dPQ4_NIQF94PcKxAVqpRi5K46eZlCszj2CSt4f7CBNhkNwe3iBAGWD1mtHmT50RluqXbWSPdAKfyDWNx0CDYpGjY8Hwe2OBoeucrNnRqkUejkzRVleNTsTsequjRZfGQg4vfQbIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=aws1AC-8CZ9BmJlakQjs5NTmgP_a8a2gqJbcH6OfsG-Maj4Yg4TbqusiokuAJMLwmdX9MyAGclW6_qONTWlgVP_bMvcYCCvhF9h1VHnweteY4defdIrMiffJPDoO6_Wj4gPMsDj4KdN6A3UUO7jXuXI7sAebMQ9HZK12XL6HCuYiMRFI8dFOn7HVSetppy4s9Dk1cHpDSpCeU1dPQ4_NIQF94PcKxAVqpRi5K46eZlCszj2CSt4f7CBNhkNwe3iBAGWD1mtHmT50RluqXbWSPdAKfyDWNx0CDYpGjY8Hwe2OBoeucrNnRqkUejkzRVleNTsTsequjRZfGQg4vfQbIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApXuYqhK2uByZZYDbJKJPMKnMIq6rfItUXTCzdJBk4bAEkP2fqvMrc4_FtcJe1IaTVdw2D87dpp6rRCYLKCZ_ezfms89EF5nf088tc4-EAC71LMzp2ePdH3ppqRlhO1T7CMUgID2fA9W9divDriG36AoPz9AREfYir292m8HVnfACzUtl4ihqcKtwj_gqdkbiHwI8JFxlmllK3y8PwPhNJnv0bSBrN6EZQ04sW7u3oNHIiSzaQFuef8B49dtw5yG0s5onA805dl8EjNfIPpGmIevBl9NwKKO83W9tBWFPETgADYvrrNju0cJqTSQZYccLGezp7bABNfbgHBok3W2Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GENz-Tpv7peaG6NyYAo_kkqqCvCec6BHcA6GV98uiIBithyvgGtKZgO9VaPIgUrkcl04BgO6IvJZ7UzH-V74ARmsAvi29LErVI0MxjzuoLd04UzJC3zaaY9OgcHLFsLYTLib3ODFLzorE6p3o_tWs42ql1-XfCxDF3e2WQ0D5GCczRaX3kwiVRLBt4i8q0Uc8fsaqibwCah6VJmJAe3ppctRCW4MDFxdcPwIzZrNjL_YX8WI9qDuSjvqnbEh4IO-Rvqb4itFH5zNI6CB8hi9jkjyYuB_MNN0KN6Q7eXYOhryCirFLg0I5U_kQtrckUFZd9bcf9RzP8FWiZcvX5DIdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3uRypumBa6OLCmjHZsOrAMniUOgov9MS-aDEPgrU3gnaQCIm8uBDsmwVPRyj1dOyvKrc8Y0MzYj1GtEP-CvcpmAiw3U7tjGcgUom-wdQswq7zp8Ghugq8u8QAtD3bxjMKdFEYXJgExMj-YF2prjklh2Kf2G1uL-rS6lOnnr5HLDC-Xvit5bnaJKwuURvCZUdWYhXxRAsufgkflSBTnrxkE2PUUZiO5uhGAV3Pt5hEkqDldzLjnd8Nr_Sw8d1Nv079vItjgQf4clifNi1kyIhAmEREEh-kf10XpsG8xzyXONbo8j6-7v4Y3WUXaXGkztBf8iv8dG54KuDp9GtIuGTw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=hjBUhGCA1AwR8i5DBLNL7yF-B0K2TCee7QSF-BkvwKvaS4RQ1dsWqupx53D90X2A6V4-mPnmQAKp78eEvtu4w-TrVgdgk9pjcvT9Ff2L9t9Bi8Nnr-OwaEli5wkkT8USblu3uxUkpcKVmzjEW3kbw0WJTJ2mYQJZPDtIXvo581j0OBdAaPZhAz1a10s_g7yfWHvZD4zpC1nRr0UNyuLQBUc3EbgA7O0oQ5uZo2DD4BcjgYgyCx3JSzxtiALvnM5HMaiSPjZITZyy7hHWfZDQEMuG6_3Wpjs9dEXnjMluqlCBes1LnA2NG6_ZAX6XfQlT-ZKC8I3zUH29GiYU7lUylA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=hjBUhGCA1AwR8i5DBLNL7yF-B0K2TCee7QSF-BkvwKvaS4RQ1dsWqupx53D90X2A6V4-mPnmQAKp78eEvtu4w-TrVgdgk9pjcvT9Ff2L9t9Bi8Nnr-OwaEli5wkkT8USblu3uxUkpcKVmzjEW3kbw0WJTJ2mYQJZPDtIXvo581j0OBdAaPZhAz1a10s_g7yfWHvZD4zpC1nRr0UNyuLQBUc3EbgA7O0oQ5uZo2DD4BcjgYgyCx3JSzxtiALvnM5HMaiSPjZITZyy7hHWfZDQEMuG6_3Wpjs9dEXnjMluqlCBes1LnA2NG6_ZAX6XfQlT-ZKC8I3zUH29GiYU7lUylA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=SGymrtjkTFpufIFJ1AD0NX9LM4R1WPkRLv8rk0WrM9RSCEmw5TcgQG0NDOANIp9UFoLdt9YT5UWtmdPEPB8DdGqn3JBd7ALYpMVLIs78Drys9iUMiLxBn7QlTxfk7vQYqP2XihNKUzdQBwhvN0Tkr7WDUaG1m1Fhcvdy95C0Ce-crwPSIxfGwfKQws0p8vQ_2_sDEklVftVev2M3AVs47DgWie2NqmI7uxuE84GNbjxbHukTgioPHME-q8IEbpQdxoR5K7K_bTOvDjoKb5dU4MX8GfzI67rwyXAk9JURp_zwySjKPYc7e1Hqk-l2iqPcN-i2Ooz99VeJ7DqF59g-Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=SGymrtjkTFpufIFJ1AD0NX9LM4R1WPkRLv8rk0WrM9RSCEmw5TcgQG0NDOANIp9UFoLdt9YT5UWtmdPEPB8DdGqn3JBd7ALYpMVLIs78Drys9iUMiLxBn7QlTxfk7vQYqP2XihNKUzdQBwhvN0Tkr7WDUaG1m1Fhcvdy95C0Ce-crwPSIxfGwfKQws0p8vQ_2_sDEklVftVev2M3AVs47DgWie2NqmI7uxuE84GNbjxbHukTgioPHME-q8IEbpQdxoR5K7K_bTOvDjoKb5dU4MX8GfzI67rwyXAk9JURp_zwySjKPYc7e1Hqk-l2iqPcN-i2Ooz99VeJ7DqF59g-Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=glnBLpYnI3WBcNPqCzX50AcdiCAWlxHF2cUKeHta-GPbmf-N5DWiM2PGfQ5ptZ2xmWKTysQO5gGTt23KnI8prgUesp9UN8KE6RYH7yJiEAXVauCqkljZfrTM9xeW1hf50X2lNV95uosxX3tp423J-orawgQ-EgtUXoi6n64kHSHlfihnvTxKACuvsvMbRndB3wq2Q-g6kVOlisNmVnODurNEy4s6fefMTpU44Gfz-sh1RBSaZmi7r5fRv02AI-wis2bwlMJ2G8x2q0uJESnKzb7bVGytB9T4vaSiEzufPIqzeo-u0f1pdNva_W0Lyyzkr92yWq0n6zpIyZFDAVvqgDbdoQ_6WJ6tPctyQkVsm1iItO7gaSGwhrA_-w6Bj2fye8QIBaREMkuU0pQvA23vkk9fOEJ7Pd-b1JCsml5ohETrqBPKWztLVEvHsKbsSWxcc-fpOebwMQ5La82gGs55wEYu9uvq55ZAwfWLQ3XZV9sPzRi4AxEhrkmgSnZDMfuyv9tSZzRv7UUCyXv43Y_0WlVdY9GolbaaKb8i_LDybnbLLyXDqLaznJG6qlOTZA_Y22qg7ohAHy4BuzcidU71A4G-b-9gTBg7BCLi1dZpFYHcavYJWjkEy2tVniaaqLrNq7WR_1fMm47I9G62DBpSD5V8oQlsFsXc9H0Uuqn_qGI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=glnBLpYnI3WBcNPqCzX50AcdiCAWlxHF2cUKeHta-GPbmf-N5DWiM2PGfQ5ptZ2xmWKTysQO5gGTt23KnI8prgUesp9UN8KE6RYH7yJiEAXVauCqkljZfrTM9xeW1hf50X2lNV95uosxX3tp423J-orawgQ-EgtUXoi6n64kHSHlfihnvTxKACuvsvMbRndB3wq2Q-g6kVOlisNmVnODurNEy4s6fefMTpU44Gfz-sh1RBSaZmi7r5fRv02AI-wis2bwlMJ2G8x2q0uJESnKzb7bVGytB9T4vaSiEzufPIqzeo-u0f1pdNva_W0Lyyzkr92yWq0n6zpIyZFDAVvqgDbdoQ_6WJ6tPctyQkVsm1iItO7gaSGwhrA_-w6Bj2fye8QIBaREMkuU0pQvA23vkk9fOEJ7Pd-b1JCsml5ohETrqBPKWztLVEvHsKbsSWxcc-fpOebwMQ5La82gGs55wEYu9uvq55ZAwfWLQ3XZV9sPzRi4AxEhrkmgSnZDMfuyv9tSZzRv7UUCyXv43Y_0WlVdY9GolbaaKb8i_LDybnbLLyXDqLaznJG6qlOTZA_Y22qg7ohAHy4BuzcidU71A4G-b-9gTBg7BCLi1dZpFYHcavYJWjkEy2tVniaaqLrNq7WR_1fMm47I9G62DBpSD5V8oQlsFsXc9H0Uuqn_qGI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=M6nqKtCY8R4FpDPASHRfWzL3j3AnnnJPVvN3ctSxj692E4VZCefDAc22bFtVhQs-EEfcLRwxYQn0ETufyaj3Bb-DtGvrDGp1nFtmp2COi0O2cb65x_bhk3vTZ3kwDyyzEAe79dx6lpmbAfiyOvhJ8l-n_G4ER5xccvT9jZC3XI9BPyEG1DIJep5cIHnPmbWsd9iqGuOjVYS0gkp1_6nxPa9vfaenIiTwzXmS7tDvwVIf_tIM95Iz46nP_r7a8K6UPQOquSfpSFW56IA7pzqEqHm_IiFXvvbQWo0ap_YTGKYZAuXwZ-QSOZIs1MdmXns7vngAqSRI1PqrBq3W2rm7bHxaibYjV2Yy4JhtOOZO7BILhj5jEkLjqlpB0uAlzOiRIes8j-ItJZrK18lmYh79tXc8-zxtR7iaROA9sfCc-MtAL4JJYLIosNpc5QgW66taoAPGVH41FZUOqYK1zCmj0g1oXwU6-bAbuWqjYPeoCerin9LvT3w0SVx1ARMfVOxreri1PniRyrs_0L-SCxhKTxMWcc9D-rUQ__Z5N7nu6h2zOWyoPwzWU1qeYDKET051CR9tfDutYoBoSkJO6vTDetSRhcQ89gb7j59u5pRDAEZwivTLUIhDPYB1R9GKSJpLk-qOgqFxd1Bwaysmy3ckyj_W3emqsDVUH6WcX3-jRW0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=M6nqKtCY8R4FpDPASHRfWzL3j3AnnnJPVvN3ctSxj692E4VZCefDAc22bFtVhQs-EEfcLRwxYQn0ETufyaj3Bb-DtGvrDGp1nFtmp2COi0O2cb65x_bhk3vTZ3kwDyyzEAe79dx6lpmbAfiyOvhJ8l-n_G4ER5xccvT9jZC3XI9BPyEG1DIJep5cIHnPmbWsd9iqGuOjVYS0gkp1_6nxPa9vfaenIiTwzXmS7tDvwVIf_tIM95Iz46nP_r7a8K6UPQOquSfpSFW56IA7pzqEqHm_IiFXvvbQWo0ap_YTGKYZAuXwZ-QSOZIs1MdmXns7vngAqSRI1PqrBq3W2rm7bHxaibYjV2Yy4JhtOOZO7BILhj5jEkLjqlpB0uAlzOiRIes8j-ItJZrK18lmYh79tXc8-zxtR7iaROA9sfCc-MtAL4JJYLIosNpc5QgW66taoAPGVH41FZUOqYK1zCmj0g1oXwU6-bAbuWqjYPeoCerin9LvT3w0SVx1ARMfVOxreri1PniRyrs_0L-SCxhKTxMWcc9D-rUQ__Z5N7nu6h2zOWyoPwzWU1qeYDKET051CR9tfDutYoBoSkJO6vTDetSRhcQ89gb7j59u5pRDAEZwivTLUIhDPYB1R9GKSJpLk-qOgqFxd1Bwaysmy3ckyj_W3emqsDVUH6WcX3-jRW0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=sEMmkXVYXBMsbDsUuJknYVnNjBJbcitA9MxeDDaLO_Df6aMoWr64ClDS28xVYqgMGfm80nljfB09ymI03VN9MrqnVl6cQi7W7KtAXdgpDFJYhK1TBha7HzKVEWmo7_orHhpgdFe0rbYKBMviz0c15OPILG1Nc4L_VDLlZas9otAHOgEEusV1gvnItYkdqdplVpoR73MYZsJAIO7-w3C5eIgrXAmQxp029EGAzinCFJxfvltiE7DmvIu3B2G3rOhtFdWDqGHsY9oh-S1JhIOL6Dp0xrToAKWwl-Zc6ORW_gbPlpNQlM5qR9LPR-5RQvaY1X0l0gjMR2yyChWm4B9kgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=sEMmkXVYXBMsbDsUuJknYVnNjBJbcitA9MxeDDaLO_Df6aMoWr64ClDS28xVYqgMGfm80nljfB09ymI03VN9MrqnVl6cQi7W7KtAXdgpDFJYhK1TBha7HzKVEWmo7_orHhpgdFe0rbYKBMviz0c15OPILG1Nc4L_VDLlZas9otAHOgEEusV1gvnItYkdqdplVpoR73MYZsJAIO7-w3C5eIgrXAmQxp029EGAzinCFJxfvltiE7DmvIu3B2G3rOhtFdWDqGHsY9oh-S1JhIOL6Dp0xrToAKWwl-Zc6ORW_gbPlpNQlM5qR9LPR-5RQvaY1X0l0gjMR2yyChWm4B9kgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrIXInfDPkFGwpsschbBX1OXeQA4qpWM8iDNccMc7Ybn8SaaMLlg2Hmt6N4BTn8cLk_dxYpBRO7JyL2LPojPysMQjj_lnogRjeIsrn_EAMHOAJdwdfVxPYEmmlkRt31CaiAbOZtM7tahKLg20T3BKKJ71IpbRGG1Jt3QzcEPtkFTgA7M4XoQWV3QN6rT6jpNXzp86QIyGCK6hkbRTGfJT8J1Jzv8r-4Ds9VvuGTy6D0cXMko3TyuII6XBAis9sZMy5rC2S7Qd0rt6rLeSXyLUZjfEeFApp1nHYX0g9gmThgEV8qrzJAZRQDkVNPNcbt1JDx5hdszrQcfK1QaWhU1iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=mGzA8i4yeYyl5HWzWPXIaHM3-cJwKPWCsQh8blGT4gl0QbV3tM9t5jPRJzGlAOponGhbGlQHUP8I1NdrX5lnJH6l9fCe7fxmpupUXGXJbqQIMkCk2ug9fqyYreD4Lc8OemdHNpVvF9TMzky5qz0SVQfUmyQLVOlDXZ6YfxUTLNp15Vl493mHS_gsob9SrR3edi046bf4u0YJaWSeCltAU7DzS16K4YjhPZN47RO7Ysn4-2DRrkaLh3ZW85OUeH9Ltq_YStg7uiMw-cyVKtdgwkR22qZwURL5WD15u33O4dogs-S78N6EzsLJ9WtN8IsVibTs9TVQDct30Aq-clU14Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=mGzA8i4yeYyl5HWzWPXIaHM3-cJwKPWCsQh8blGT4gl0QbV3tM9t5jPRJzGlAOponGhbGlQHUP8I1NdrX5lnJH6l9fCe7fxmpupUXGXJbqQIMkCk2ug9fqyYreD4Lc8OemdHNpVvF9TMzky5qz0SVQfUmyQLVOlDXZ6YfxUTLNp15Vl493mHS_gsob9SrR3edi046bf4u0YJaWSeCltAU7DzS16K4YjhPZN47RO7Ysn4-2DRrkaLh3ZW85OUeH9Ltq_YStg7uiMw-cyVKtdgwkR22qZwURL5WD15u33O4dogs-S78N6EzsLJ9WtN8IsVibTs9TVQDct30Aq-clU14Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=H93hRB2Ii62yK4ey6MIswz8cQResniRx7eZkBmVRoexFvujfs0xdHvHvhZtWUUEN__tqoD17XzyOe8k611b_6OWfJ7b3kyt6UV8xR7aGhCQ5_-gWXgQatXCgaaJZdHEADKdeJ4HaMKPFl8c9p1HCImmL6BSRqx6PNQ7fC6rr_P_e4vFy4u6ZdO3UWScxELcu27SGbhquF2M3iC8p1YzKmemYS7AEeUPFZZk6F46dI3hwMvPV9UFHIHT3Ghj_qH1uVDKuRxPhYkQU3Lrv1UzvHRrf1y4VJHnsgvBEjPrNGvnXw4vs4dD0V_-maGMwc-awIlhcEfOsSBtAbnOsPOB9GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=H93hRB2Ii62yK4ey6MIswz8cQResniRx7eZkBmVRoexFvujfs0xdHvHvhZtWUUEN__tqoD17XzyOe8k611b_6OWfJ7b3kyt6UV8xR7aGhCQ5_-gWXgQatXCgaaJZdHEADKdeJ4HaMKPFl8c9p1HCImmL6BSRqx6PNQ7fC6rr_P_e4vFy4u6ZdO3UWScxELcu27SGbhquF2M3iC8p1YzKmemYS7AEeUPFZZk6F46dI3hwMvPV9UFHIHT3Ghj_qH1uVDKuRxPhYkQU3Lrv1UzvHRrf1y4VJHnsgvBEjPrNGvnXw4vs4dD0V_-maGMwc-awIlhcEfOsSBtAbnOsPOB9GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s88OXIm-6E6fLwOuLAmv5cglrFa8yX9kpy9khxFT_eBJvEnfro5E56cDLoWlwxDA3pfLw3En0CYYgqv4yyHjWAXOqohWxum9-iS-sD0Y0V5Xnyk9jF-AULkB4anVob435vRVBZCfHKom_xSdsWJEa7Aj9kKuZkqRPtZ88SY_-JcvMzH8jr2eAGT5-RINu3hJMBcKWoV3VsjDHkDInouwUpyX-bATtwvBCPiilNTMkCox1z3rTJ4OsUJv1NFVhxddDEbGvC0ELxDd-HaSj5lEA4xTCxi_wF_zd6HTfoukfGTzmpWdHzvP1ckgkrS05bkLjAskOlsc2-s7RfMQK3P_ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKXisXfeSRHtqtoyd1zuPHO85wKRE2rvWt-Vo4OnNPXxkCgYRlvJv4MNWEpegbydTjGqS7nR2bwCLcgZNhwqteFFQr1a9fFKWGICnCsqxfwNsW9XF78B4oS3peYNCp0ygFikTkK1DpPZYuDdp35X_9c_oeYW2UVvZ0JDqqCqavRoSo9zUnZxvEd3fgSzCjyr6T_5h3K0jGONBT0OUQVQ6yuN7tIL3Wn5eLaOMWl-fvYj3szYnGZ6EUfx0RMssX600gvuu4eXegRc70XhxcyJO7qI160kU2NWwMh961Kzwn-UhmDmSxhDKCmXvzjPj9T5UZe58nBvpQdzfRgcYmOTlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sO6RDd6tOb9NCFDMznQiFQTbmVMVmeJ3fCTH-g03VFXUreiMFfLF7MvfgPOtPYFS3QaOzyofUbM0ByChDzoOiDFcO45XKC863Ls608R2vzC2xshl5PDNKZxTk3QkgtI2KjXmdAmNuYqYFS_8_jYNIB1yyj3oZXXykBV_t4sZezEJ7G9AOMdav2mbfMKLQtsF2MdidfwTcHMV9docImAbVe0zudateVDUfKQtaRUe5eBUnCXoM2m9M8_Pcxx1pH3FSVO85LwhI0p_7Ma3MzA_Hy_XTrg0fFM0ygdT15L-thaDpIulZx8Fvlkig1xzSBEHq1INXC_QzIBpMsMD_L2c9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pb3ND_phWzVSLkXa5vqBYX39Y75HWupr9KM3I5icbjMxYw2mMt5eS_7LS7jE0N8wsz4MiNq__omiY9O1l-yVDfCiaR5MHwo_jBx29cZ2btW-UWBkxld-Mw0Dr3WPhU_QVb1zLzwYzgmizcSB75-ohLouAqbHPYe-jarOXzDHEngCw53E6txGd3r56P1iCevvsEvRpsyp63jBioYV-AgYfeoghGb1cBtt7UxjtyvihfMkLl3reJDWCesjaxI5LvR7nIv6D0w1CHBkgTgAhx-d-oqVaH7OFDN4EapjqjON-9tefSCkGpOsZCwWY348CnTKd1200B1P8CgK5FKjcSwQKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRskBWO8zm1-OMZtRszTBhkNQvXr1mP9CtraCnvYH0caXXYu2NHDOPetvFI4cT2ST7aI303ZYWTjfwNuHdq6iLO4iIesO3Xhq6FBHlM173OxODuDCeRtkLs9h0Pp7jbFjO8rjkATa_4mFO99T7sWNADsMZxGVQlmtThqNIzG-lgv34hHmFfzjXoe0FEguyIKZocOiveJRNufIObUT1czAJ7ZMTB-5YIVmhsf0Pgn3SFu6Kn8Y6UGHp-FLAOA9dVLu1q83_4oFq4usGS3Om9tnXZDAT9HMdW75oEtbPsJNNMIFdOFyjqGUv7trpMVW8tP1xJ44HZKYI-VRPmo2HrTxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hg9XAylKrIWosjIVEzsvuoDGmA43eW_tAAdCtBRKbl3yEMV2e2aS6aJswJjTl-K9Go8jFrSHjZIpNGrvN-b1IstFZ8W6WLCMyLE8G7jPh8pQI2TKuxqd5uZLQSTOZ5kW-ipSdU-6TDjZR6Smsi8_2B3qZAqosbziubkDtxnJbZ7uSctjMQEyWjCbHrpGeoeoJmcxpP-crcfYo98Py256B8g6aSoJJIRpQg_dQyslE8PXO9NFkLjzc-Y_9FkkT6T3bk9oFB8-HzuiNxWwboj_NTQqnPRH38XFLVA2wxvKtHvKVWHVTRlCHYvVNUmbhD5FuRiH7G28LGGkto3Me-oQxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRyad-sv-yhhOQIB9ucCv8xLjw-dnPEOyJ_7GZzmfBMfeVBtoTkIkEBLAkiYHmELtI740MFgo7I_kTGBCCQIttcKt-uNurGwgGxjaV9SCxSDbBNTN0Jy_Z7iFE6tQO8FZ1282Vugkl2Luetsbuk0mhFO5MXA0D41t0rA8bz2pvah9OkwKVfKRX8oleYJ0GrTzqHsY7KMBXdza-vf_dSEJp0_Ykg_tCRYP0strGzYGUurbk40leCfNuKMoIn2VVWtaOvShnuicWGo2KQ0alLQcHJWAc3AuemD7sKHqz8qNooIhWxhvl6YgXkJYrO14dCK4K2clxCqNtz5krjDMuSnfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZzeNZ2oq_aWvgA6zjLSxoprcoBw5s41lGiK-yFie3AmHkC41T59SP3ZCYwsUL83Pv2jLj3lGHbah8gx7osKhTUB8zY5IHp1GbcIczJo71ZvGvXdzA56QnUKXwN0zRBk82A8Lbivr1oGxwtg6DUmAptK7Hd8kOheN9pw-iPlRcPbDvbfH0Qr0ztRlRi8Tu-Wo_pLy3A8jX7rNSRcxYKP97FyWlz4J_q5n6jqr4fc3YBdDuNeAwcFle9ZkjVJhHPD974RVHt_Ti0gcetW1hvCFAnYubmtcLRP5-t6NAljTNHQtiM6-5NZZgt1PWP6ibm6P5MFYgFyn5JUfFIm2O7HsPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vVq5Bci1jaovivzk_nRYe0eWMSOTvAar4_dc3Qnvlw_OZgppFOnYfAO78JfLqNV9x7Yb3Ur8mZZfJwUTh5RvyyAHci7GhNaTewwnVe94Rm2lgvblyISo-V-HXI1rCaUWlI5Nbh3Ame0JBQN5EfqqJRvv9gppvkB1_jxM6EVWBhDx_XQg0wFP9r8JZ-s53N7nXnlKxJ8EE5ScfmK-dqcyczWLtAwsUQBOpZ8m6ZxPP_nPXuGJMESVRkREIFM2end8d8EylIMoGs9m43YdN42EVOunjTemrw_iy1ouBX7SwPBdqOTQtMV_OH_yBCrnznGVUO2sCzTICyySCJqPvH22CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vheFZ7STRgGBWgKI5OazeI8Q6W1j8CQI8NKRt4VEMOJYkjhmFWjGyNt6P93iX0RV753YC5bL-JHgcp5H7ZYMAASgETPlG5g-Q_1rkl4JKN10gfwij7YS5y60JuBuZaTYVb7vHQxGzQsTq3gPTy99icrZK6f_1H0RuAhVApC9QQbP6OawpFO1QOLlZHpgTK8gnEPfy8Ic3z1qtnNn9Sy4lYLzjMyNOc6BPiyVX1CvaiWTLRjVmqK--_I1UsLRZkglQuqOu-hjZlb83gMDxpPTDVxtz8KQO-8GMAK0ED9tURICIcYRm6sBt9uwxrD-PL6TGRliwDiWYGVJaSa0PP-8EQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=r1Kc-3DlWzLa9Cbzxq4AUBgyjuzMdqTYIRwpUTC2N2H1QFKDp6rQFq-VmuNZIiF83COgcPI70hGY0XELWWna11OicmV0bRFr83eJyY6UAnN5q-RrSPXuqFa_cYRFc9tT3_S1WHPRS5lnxKryHyzr1mESBLe0kLh2sHt3rBJ4DWFyoqRl8IMjspO91T7s4jGMp8HWgNqpXgatixi-fBBunxlKnEk75OzY4qoaaIAsY1BkYVOwkCJnPboy1f0iV-TDv2yV0lAkufC3z93h3KnnZCtbFl7pEnBc91CRRn-iQWJvh2e1UpOgGvEnKMpvMCzFNlAa6pD7BAZKpQBLySVEBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=r1Kc-3DlWzLa9Cbzxq4AUBgyjuzMdqTYIRwpUTC2N2H1QFKDp6rQFq-VmuNZIiF83COgcPI70hGY0XELWWna11OicmV0bRFr83eJyY6UAnN5q-RrSPXuqFa_cYRFc9tT3_S1WHPRS5lnxKryHyzr1mESBLe0kLh2sHt3rBJ4DWFyoqRl8IMjspO91T7s4jGMp8HWgNqpXgatixi-fBBunxlKnEk75OzY4qoaaIAsY1BkYVOwkCJnPboy1f0iV-TDv2yV0lAkufC3z93h3KnnZCtbFl7pEnBc91CRRn-iQWJvh2e1UpOgGvEnKMpvMCzFNlAa6pD7BAZKpQBLySVEBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
