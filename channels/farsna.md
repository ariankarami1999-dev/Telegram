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
<img src="https://cdn4.telesco.pe/file/bW6ZOHDRiJ7isjHmAw30g7F0CM8osxjz0rsXHRM9mPErjNGoYWG-fqpbALY9hCiFnJcFMpsecnmW6xXqbdvnnlJIltgZ6E_Dwg-hA0F2HQiVSd-x4K-7DNoFDW_M1WALRwJKkl09rQ4UCPFQ-MLt35YAC2GBy71J13p2UqmROYvHLG2SO9kELF0meo3hldsfCAlb3Cb4n8SV04fFOTcE5OH3MZR1QOpgmgfO_sFJkaWGIllV7VSeNY5l6MbSEX3-OtgV9DTlk1zvpbKil4tXIG_FpthxdDpMMeq67S3p8lVXq9r7yvb8uUb8dzOKSJtq899C1zVEVvxACkhANJYEKg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 09:48:57</div>
<hr>

<div class="tg-post" id="msg-462172">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6XHOHG4IHq0v-58JfFtHcgpppm-TKPgV6C8WvMT0ofKel8JCrIyKKOHOrIlG19weJTtxCa75QNlVUxL0Xb6XY4N73xaPIlU9hwQHa-UVsaDN8_iPrOrXEyXRHYlz_sLRaMTZvwXwy3lyBRBrMjtAE4NTacjWpUUiOT0laSeQUMMsi_EI2JpN3PeVMM7bQG3eh0HVntIXfL_ibjtATVHIBfIRuIVEc8ft7jz1VTHXImbRs9NnV6ke68O8BDfsLttLycnUrZLZyFabJ0_dHk7wI9AgdR-I8c613QHnhv0izntg2BtzTWt0rjw4qt540r8F36MULzK2Fjnp6ZmeGaCdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: ارتش مایۀ افتخار ایران است
🔹
سردار محبی در دیدار امیر اکرمی‌نیا: ارتش مایۀ افتخار ایران اسلامی و سازمانی قوی، مردمی و دشمن‌ستیز است؛ در تاریخ ایران، هرگز ارتشی این‌چنین قدرتمند، مردمی، آرمان‌خواه و پای کار وجود نداشته است.
🔹
همدلی و همراهی موجود…</div>
<div class="tg-footer">👁️ 177 · <a href="https://t.me/farsna/462172" target="_blank">📅 09:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462171">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDLWh6L0xInEnpyjq_joG4fC4-jFEBU3hD1w2sf5lO2aJLWsMkjGWd8FBMgJkwl9m1LJOSMozbOM1Ucc4aAOxvXcvBZDw-5-ZW7_GtJ0-PxN9iTkk5alFMdchnpt61iYN9VsNxVUsgmpQ1pJBVOJ87YzLp6Z4mu1akQzvdPWgahqEiVLeZc2YcrQG749IauTNv4E8l-Xv5lh6FjSXTOBQ-fXR9TsZdCeXlTqjFv_yBGi4EQxzmxBJZaUXFzBXL_MGJvjOfLYJ_1UI1BcxaxWNklwVv9e7HA8m1iBbr8ACrf6OHs8VDd7BxuMMOAK_0Z6oOfX09s1Op51Xuq4JeB-ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: ارتش مایۀ افتخار ایران است
🔹
سردار محبی در دیدار امیر اکرمی‌نیا: ارتش مایۀ افتخار ایران اسلامی و سازمانی قوی، مردمی و دشمن‌ستیز است؛ در تاریخ ایران، هرگز ارتشی این‌چنین قدرتمند، مردمی، آرمان‌خواه و پای کار وجود نداشته است.
🔹
همدلی و همراهی موجود میان ارتش و سپاه و مجموعه نیروهای مسلح با یکدیگر، نیروهای مسلح با دولت و مردم و همچنین همراهی و وحدت مردم در میدان و خیابان، باید در تاریخ ثبت و ماندگار شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 875 · <a href="https://t.me/farsna/462171" target="_blank">📅 09:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462170">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtAeS0UrkQM0Uff4snyNxFotCmHy91exD9ptNSrnijvbMDKvZfgczGPLdgvwDU99kHgdvny2P9f1Vuu9GlpvonPZCP8Smvf4BhNAOaDSfYgBX7h6ppjiyaN-dGwXWFyIkM0BNxWm-I_n2AEFSm4BBGRU-Rzl8YrTyxhvL-ejEea6jtQf4TmD9SZiuqprS9MB-8tgnlk3izkzateEjyKpCXo5XGpX54G4P-LkGfA96P7sjlCKSPxhHjNz75CFWPNnlDpDQcM2GYXLNqIrliwNgWVQDJ1qLDlMkXIkWT37TP_htFYuUaLX8BLwW4HurEfdAcFu0AgF4kroPip6va3vwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 940 · <a href="https://t.me/farsna/462170" target="_blank">📅 09:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462169">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anPlKMrmQnn3tXCRUI9itb-XBrDBAVz07oE-NvDTkrr7iDO0a-kfjYtEU7xPOXBcd2MOalIzYZeH0HvrXGnhsHSqRCyrxv2lHdStxRMjyOVmwk59PlCuTB2QDy7cqKbLcveNu-fUBLd0i-_lbtZpOXfTmd83Knnbg2_BjYUrvtOGWxKPdEUY65I8K88iOpigd2za482MiRzFbw42kEgUj6lVJDLs42jzeT_mJTSvCcP0g6a00-JkLLURwZxNlH3Bd3vR7H0lQI-Uqijid9An2n-f9Kg-5HX_AbW8v4XlpX4P5i9p8m2wmg4j0XrftwvAO-8iMlHrW9Ejm5GgLgK-aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابلاغ دستورالعمل اجرایی نکوداشت پدافند غیرعامل
🔹
دستورالعمل اجرایی نکوداشت پدافند غیرعامل در سال ۱۴۰۵ در ۳ وضعیت محتمل
🔹
۱- شرایط عادی (خاتمه جنگ)
🔹
۲- شرایط بینابین (نه‌جنگ‌نه‌صلح، مانند آتش‌بس)
🔹
۳- جنگ تمام‌عیار به‌منظور ایجاد وحدت رویه و استفاده از تمامی ظرفیت‌های فرهنگ‌سازی و آموزش عمومی دستگاه‌های کشور
🔹
در ۱۰ ماده از سوی رئیس ستادکل نیروهای مسلح و رئیس کمیته دائمی پدافند غیرعامل کشور ابلاغ شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/farsna/462169" target="_blank">📅 09:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462168">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af7467f44.mp4?token=NlnnNzCwUeJCAPwcxsO4XRkw9CXJV8hxgSfI4_2F0MDOt5EakIEmdwqlwoOr5PcfyVob9W2ZXHG-pJWvtrkTD8kSIhWiqedru9ReKVgQoGeaoiBQ5LVNgmie7jNfazO45C6oTiawDIPyWvTCVE0WgNw0DSsVljEq7jrS6ihc1nvWETNnPXdD5DK_C1To1mNjKT7tliokfXlrRoRdavIs813rFyhe8qrw2uF7U9bVexpT2UJEi4rD_5uB1hmxZrJ4FSLxgWvThDy-sa_pT7PwEl2VAUhizXoAcOgRrNVQ0uoQpokymFQ_ZPwc3--8fJOvx88qTFxXbcKdlMnYnLrMjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af7467f44.mp4?token=NlnnNzCwUeJCAPwcxsO4XRkw9CXJV8hxgSfI4_2F0MDOt5EakIEmdwqlwoOr5PcfyVob9W2ZXHG-pJWvtrkTD8kSIhWiqedru9ReKVgQoGeaoiBQ5LVNgmie7jNfazO45C6oTiawDIPyWvTCVE0WgNw0DSsVljEq7jrS6ihc1nvWETNnPXdD5DK_C1To1mNjKT7tliokfXlrRoRdavIs813rFyhe8qrw2uF7U9bVexpT2UJEi4rD_5uB1hmxZrJ4FSLxgWvThDy-sa_pT7PwEl2VAUhizXoAcOgRrNVQ0uoQpokymFQ_ZPwc3--8fJOvx88qTFxXbcKdlMnYnLrMjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
رحیم‌پور ازغدی: ترور شهید گرگیج به‌دست عوامل اسرائیل و تجزیه‌طلبان تکفیری، ادامۀ جنایات جنگی دشمن است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/farsna/462168" target="_blank">📅 09:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462167">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7tCsh_-mK19xgS7p8-VAczhcc_kmKdEmlVqed_7PFUBPKGE5pySOERA3KexszJ2tbOzKoDyvLMaY0fE998Podguo59wVBAsBA7OlFV24UEo7TJ6wuTKyu51dR_tFY7WIt8-rohZdS5ytXvGPf4elPhfHnAP3j7_QYsbNnfTEc4OWmACuHjcsa8nG8vc5mQSD75PVGPWyT9fmBb_GPD2Y29eYY_ZtQzs5cLmibNmaKdG--AfuimLyM4XuovFxcIkuZYaMkn4_Zw48Br0bJFR0a1yiSSzIlv0gDVZpmjGoshGArF9AAHKtU9tA5TUs8_d_3EXFjgYJ-Z4SdgU1PM8Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
آخرین مصاحبهٔ مولوی شهید یوسف گرگیج: راه شهدا با اقتدار ادامه دارد  @Farsna</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/farsna/462167" target="_blank">📅 09:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462166">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0ddab11d0.mp4?token=bMCTyu0wcz_Lf0rh52my0-I5IZp3Ur2nws3Z6Ee_xTP9NlhrM1cJhdI5ryqrL09QboDAVfc8x_DtEstOr93Wnr2LCONQDNwhoQZ_HEcEQqJOIH1l2rl_ifJVQ26i1QkHoAH5C1xmL3siZIhDsLwbM-CAp7Q_uo1hVrmFK3Pw0cWh84Ap8vu6SYtrx2kMbydSx-IumRrzERHsf0LPsPfZ33KLdZU-gZxwbXFpPwThfbxhji0bkGiy7O21iDwAPRPkcytw4a-YUcXsmHFXBIJECIIc6rFOgLKVYhWBbASgpNAFMii_EofnJrBCZgvmRaLMuKM99f8oYU57S_13cIbkBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0ddab11d0.mp4?token=bMCTyu0wcz_Lf0rh52my0-I5IZp3Ur2nws3Z6Ee_xTP9NlhrM1cJhdI5ryqrL09QboDAVfc8x_DtEstOr93Wnr2LCONQDNwhoQZ_HEcEQqJOIH1l2rl_ifJVQ26i1QkHoAH5C1xmL3siZIhDsLwbM-CAp7Q_uo1hVrmFK3Pw0cWh84Ap8vu6SYtrx2kMbydSx-IumRrzERHsf0LPsPfZ33KLdZU-gZxwbXFpPwThfbxhji0bkGiy7O21iDwAPRPkcytw4a-YUcXsmHFXBIJECIIc6rFOgLKVYhWBbASgpNAFMii_EofnJrBCZgvmRaLMuKM99f8oYU57S_13cIbkBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: بارش‌های پراکنده‌ای در بخش‌هایی از کشور طی ساعت‌های آینده خواهیم داشت.
@Farsna</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/462166" target="_blank">📅 08:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462165">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🎥
پزشکیان: رقم کالابرگ قطعاً افزایش خواهد یافت
🔹
حتماً در حوزهٔ بهداشت و درمان بازنشستگان و معیشت، تصمیمات سازنده‌ای گرفته خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/farsna/462165" target="_blank">📅 08:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462164">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNJEZfN8egFOe86zbc7Tt7qE5QQ3aF7ZiSdKT1efZ7ntbTQe5DO5q4wXEE-frvfxfOkIESc92LsZZaBpY41wEewjLk8axyaHvLnZISoyiz6u7rj8DB6C6Pn0ZrOHKPAWHF_ZCvMG3iAZHCsw3cpknwNYY8WUD1Y2abeTt2T0rGAuRn2KqwpLCimsmB0m1gi6Gtb0SWz29g0HT_4LyS7STwA0JOV7cUDLtTlHA66yH7_8Xq18DVOH2DDe9ymFB4QTg-ipEFP9NZ2PDTn92WalG6VxYry7aKm8iCocaog-5juehPQ_qe3K2oY4dnefDnvKROc6XDv-opGLSF0Gk5XU7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده هوافضای سپاه: عظمت و شکوه بعثت در خیابان‌ها را با حفظ انسجام و اتحاد مقدس در همۀ ساحات حفظ نمایید
🔹
پیام سردار سید مجید موسوی در آستانۀ دویستمین شب بعثت ملت ایران: ملت غیور و شجاع ایران، امت ولایت‌مدار؛ درود و رحمت الهی نثار شما شایستگان که در عمل به تکلیف دینی و ملی خود، چون کوه‌ها استوار، چون رودها پر خروش و چون تکه‌های گداخته آهن پرحرارت، با حضوری معجزه گون، خستگی‌ناپذیر، حماسی و دشمن‌شکن دویستمین شب بعثت خود را در خیابان‌ها در خونخواهی امام شهید و امتثال امر ولی فقیه حفظ کرده‌اید.
🔹
قیام شبانۀ شما که در دفاع از هویت استقلال و موجودیت کشور تداوم یافته، جهانیان را متحیر نموده و نمایشی از تراز بالای عقلانیت ملی، ارزش‌های والای دینی و فرهنگ و تمدن برجسته ملی، چهره برتری از یک ملت با عظمت را در منظر و مرآی سایر ملل جهان قرار داده است.
🔹
امروز دشمنان متحیر و متعجب از این ایستادگی، عظمت شما را تصدیق و دوستان آزادگان جهان خرسند از این عزتمندی، امیدوار به پیروزی نهایی حق در برابر ظلم و استکبار گشته‌اند.
🔹
این حضور آگاهانه، پشوانه‌ای مطمئن و دلگرم‌کننده برای رزمندگان اسلام در همه سنگرهای دفاعی کشور و پیامی دلنشین برای پایمردی و تاب‌آوری سربازان جان بر کف شما ملت عزیز در نیروی هوافضای سپاه برای محافظت از کیان اسلامی ایران سربلند و خون‌خواهی امام شهیدمان می‌باشد.
🔹
ضمن آرزوی تحقق آخرین وعده آن امام سفر کرده، در چشیدن طعم پیروزی در کام ملت سرافراز، متواضعانه توصیه دارم که عظمت و شکوه این حضور را با حفظ انسجام و اتحاد مقدس در همه ساحات و پشتیبانی از تلاش خادمان خود در دولت مردمی و مقامات فعال در میدان سیاسی و رزمندگان اسلام با سرمشق قرار دادن تدابیر حکیمانه مقام معظم رهبری حضرت آیت الله سید مجتبی خامنه‌ای عزیز حفظ نمایید.
@Farsna</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/462164" target="_blank">📅 08:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462163">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کلاهبردار ۱۷۱ میلیاردی بانکی قبل از فرار از کشور دستگیر شد
🔹
دادستان تهران: یکی از کارکنان حفاظت شبکه‌های بانکی که با نفوذ و دسترسی غیرمجاز، اقدام به کلاهبرداری اینترنتی و تحصیل ۱۷۱ میلیارد تومان از اموال بانک کرده و قصد خروج از مرزهای غربی کشور را داشت، با اقدام به‌موقع همکاران دادسرای ویژه رسیدگی به جرایم رایانه‌ای و ضابطان، دستگیر و تحت پیگرد قضایی قرار گرفت.
🔹
متهم پس از تفهیم اتهام، با قرار تأمین کیفری متناسب به زندان معرفی شد و بخش عمده‌ای از اموال تحصیلی نیز توقیف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/462163" target="_blank">📅 07:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462162">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2KuZ7SQiwE9KeQ9Q70b_ByFJpllmFVX3FZuNlOHpcK3OcZubDoBgc1vo6X3Qkkir5QU1N1X7MhuZi7hdW70QaFyu_5Yn7MLTpli5csDywxBoovHN6Q7KCLN3db6rbC0RjfBrbvcKRex_A4CQu1v-GbxqSgcVnpVdQTgR4OooBXXejkH-mswcfG87ERipIZ3zZZ_cxKm4lUqJUleIe9KcRvFOoeZp_O6ahUdv5iJmz3UqZ6JXTGXxWBJKZ2hVR0sMqhNm4MVDiomorCB1nhdUbCsdnOq1M_xQ1I5KyOyMsI2mTDXdisurm7NbU-KmM-QZu8LJ6BXYAal_RiVcRgiqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر آموزش‌وپرورش: برای بازگشایی حضوری مدارس آماده‌ایم
🔸
برخی خانواده‌ها نسبت به حضوری بودن مدارس از مهر تردید دارند. اما حالا آموزش‌وپرورش اعلام کرد که برنامه‌ریزی‌ها برای بازگشایی مدارس انجام شده است.
🔹
در همین رابطه، وزیر آموزش‌وپرورش از رصد لحظه‌ای وضعیت استان‌ها و تعیین نماینده معین برای هر استان خبر داد و گفت، گزارش نهایی آمادگی استان‌ها برای آغاز سال تحصیلی در نشست مدیران کل استان‌ها بررسی خواهد شد تا مهر امسال با آرامش و آمادگی حداکثری آغاز شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/462162" target="_blank">📅 07:54 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462161">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">درخواست کمک ریاض از لندن برای حمله به یمن
🔹
بعد از مخالفت آمریکا با حملۀ به یمن،‌ عربستان سعودی این‌بار از انگلیس خواست که در این کشور مداخله نظامی انجام دهد.
🔹
بلومبرگ به نقل از منابع مطلع گزارش داد که ریاض از لندن خواسته حملاتی را به نیروهای یمنی انجام دهد اما نخست‌وزیر انگلیس هنوز تصمیم نهایی را نگرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/farsna/462161" target="_blank">📅 07:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462160">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">هوای تهران امروز هم «قابل‌قبول» است
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۸۶، و در وضعیت قابل‌قبول قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/462160" target="_blank">📅 07:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462159">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اعتراف پنتاگون به خسارت سنگین حملات ایران به آمریکا
🔹
بازرس کل پنتاگون در نخستین گزارش رسمی دربارۀ جنگ علیه ایران، برای اولین ‌بار به خسارات سنگین حملات ایران اذعان کرد و گفت صدها ساختمان و سازۀ آمریکایی در منطقه آسیب دیده یا تخریب شده‌اند.
🔹
این گزارش بازۀ زمانی آغاز جنگ در ۲۸ فوریه تا ۳۰ ژوئن را بررسی کرده و همچنین کاهش شدید ذخایر برخی تسلیحات کلیدی آمریکا را مورد تأیید قرار داده است.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/462159" target="_blank">📅 07:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462158">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8edbd4d8c.mp4?token=RVaodpQIW915Uz4IoHnXTUI7UsXBWtvPKDIkSY96wTZ9ws_mIjXwlaaq43Tnt9UZJNT6nx3SdrSaL0QQxsV_qtFFlSSI6N_tb8F-bktb3lTuQHQ7mf-lzlZQvX_qRJBupsrTIeL3uHIE7FCDdk0O-Qn_R6Ht9rDXTp9DkDwtloXM3Bh26AZk84SBLa8CV6_mw02REgPBJi73AgfzMhklGPMbXZLfGcvDwrGARv0kabGngX3DYaOXKbq-EQwZ8DBbqiVQydWVblVy3mPUsEku6dNZaXDVEbmwow6dQjniaGMZitNhODzFpqSuaVDpapsvq66qdVZoZjDLMQk9iyLvMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8edbd4d8c.mp4?token=RVaodpQIW915Uz4IoHnXTUI7UsXBWtvPKDIkSY96wTZ9ws_mIjXwlaaq43Tnt9UZJNT6nx3SdrSaL0QQxsV_qtFFlSSI6N_tb8F-bktb3lTuQHQ7mf-lzlZQvX_qRJBupsrTIeL3uHIE7FCDdk0O-Qn_R6Ht9rDXTp9DkDwtloXM3Bh26AZk84SBLa8CV6_mw02REgPBJi73AgfzMhklGPMbXZLfGcvDwrGARv0kabGngX3DYaOXKbq-EQwZ8DBbqiVQydWVblVy3mPUsEku6dNZaXDVEbmwow6dQjniaGMZitNhODzFpqSuaVDpapsvq66qdVZoZjDLMQk9iyLvMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سد خمینی‌شهر بشاگرد سرریز شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/462158" target="_blank">📅 07:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462157">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">انهدام یک فروند پهپاد پیشرفتۀ MQ1 در تنگۀ هرمز
🔹
روابط عمومی سپاه: بامداد امروز یک فروند پهپاد پیشرفتۀ MQ1 در آسمان غرب تنگۀ هرمز رهگیری و منهدم شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/462157" target="_blank">📅 06:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462156">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0a53af483.mp4?token=ls2ywoIixfjjlGXzd81CHvKo1ScajTFSUBtSGNezXmoGf5aLLl251JuhngQy8qwX8J57KXKXNftctKgk0rtiz76Yk68Of-qQo0DJyHWIs5Zh50cZ6AzQ3vmNyDwCwxVCV53RuziYliYWx6Vs5jmGTxx4buEp8uA3XDDtYzvIdu4Vr4EO2fSnoJN79v_7DMM0RWI8NHuqbWy4QUiEImdjha5UHgsbvhS5sYIGzoSaLxgkH_BU_5UOdj-jQIuD865SAWnhBvUXma1sL_Vtj0fs_WBYgdAnJ5UaaGk2uywVchoF30kPGleWVbwifxYT35Ugt1bf0xXEfka-sa-e-iZh5i1jxuXPekM-qbCaiXKMAInRaPnal_fWDWHUgKhNP8O-Izt7mLD3hiGR4eefV570ZLkGocnD4T8GGtBAnglA0IVGLDOoWGqMY6Xy5A_M_OkX4Bd7cxGC3FUADeMTMfbRpXRT4l83XUBI-WeSdNij-k8XkHRr3EztXk4IzDL-bIrv-W4fiH0P-ZWmbhTS3SJXD3Y3oyJk6zGr9B854X4QZgIAeuT8vnpxFnnyAGb7dfoVz4pJVIVUugVTwszCul41WUIPTSf4RUUUPYwOHaLJ4VMNNynN5TEXGJsExLydlIkumqEVwhEPpKlHrxtUkZ5H89HRzhPAWnG_kzHifCI49iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0a53af483.mp4?token=ls2ywoIixfjjlGXzd81CHvKo1ScajTFSUBtSGNezXmoGf5aLLl251JuhngQy8qwX8J57KXKXNftctKgk0rtiz76Yk68Of-qQo0DJyHWIs5Zh50cZ6AzQ3vmNyDwCwxVCV53RuziYliYWx6Vs5jmGTxx4buEp8uA3XDDtYzvIdu4Vr4EO2fSnoJN79v_7DMM0RWI8NHuqbWy4QUiEImdjha5UHgsbvhS5sYIGzoSaLxgkH_BU_5UOdj-jQIuD865SAWnhBvUXma1sL_Vtj0fs_WBYgdAnJ5UaaGk2uywVchoF30kPGleWVbwifxYT35Ugt1bf0xXEfka-sa-e-iZh5i1jxuXPekM-qbCaiXKMAInRaPnal_fWDWHUgKhNP8O-Izt7mLD3hiGR4eefV570ZLkGocnD4T8GGtBAnglA0IVGLDOoWGqMY6Xy5A_M_OkX4Bd7cxGC3FUADeMTMfbRpXRT4l83XUBI-WeSdNij-k8XkHRr3EztXk4IzDL-bIrv-W4fiH0P-ZWmbhTS3SJXD3Y3oyJk6zGr9B854X4QZgIAeuT8vnpxFnnyAGb7dfoVz4pJVIVUugVTwszCul41WUIPTSf4RUUUPYwOHaLJ4VMNNynN5TEXGJsExLydlIkumqEVwhEPpKlHrxtUkZ5H89HRzhPAWnG_kzHifCI49iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت سیدمحمود رضوی، تهیه‌کننده از توجه ویژۀ رهبر شهید انقلاب به دغدغه‌های فرهنگی هنرمندان
@Farsna</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/462156" target="_blank">📅 06:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462155">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKnsb3zJafCBvmq88MVguK1ZtGNZEMbr5U0KOUVWy6pmD4EdIXAkYhG_rwBtsOfYWaxjqysRplCy6ssa0pnOcWuD7uIwe8v9eipJJZgZMCyX8EbcGnE6PNYk8ciId46cdX8QdhQRHwxfJpUJ9U7PSW6oQbrhcg37_I9GD3uV1M9UbqlxuroDRWqgoauhK_bDA37A2YzxiScqXsgWmseaJMRehdJ74qNncqOKsPqLT06MK12SiaEouW5vb4UGlQb3QABzDHP_iqyy-aU7As4kMAxDrMp3gsmWBNtOux9B9SjUw1NElrdmmmylaCT9SZBAi-0xIGFQMJ6tzjma0AdJhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخۀ اروپا برای فضای‌مجازی نوجوانان
🔹
اتحادیۀ اروپا قصد دارد دسترسی افراد زیر ۱۵ سال به شبکه‌های اجتماعی، پلتفرم‌های اشتراک ویدئو، چت‌بات‌های هوش مصنوعی و بازی‌های آنلاین را محدود کند.
🔹
طبق این طرح، کودکان ۳ تا ۱۲ سال تنها با کنترل والدین و در خدمات مناسب سن خود امکان استفاده خواهند داشت و نوجوانان ۱۳ و ۱۴ ساله نیز به حساب‌های محدود و تحت نظارت والدین دسترسی خواهند داشت.
🔹
شرکت‌های فناوری نیز موظف می‌شوند احراز سن کاربران، ابزار کنترل والدین و سازوکار گزارش محتوای زیان‌آور را تقویت کنند.
🔹
این پیشنهاد هنوز نهایی نشده و برای تبدیل شدن به قانون باید در پارلمان اروپا و میان کشورهای عضو بررسی و تصویب شود.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/462155" target="_blank">📅 06:21 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462154">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">تکمیلی/ حملات موشکی گسترده یمن به سعودی‌ها
🔹
در پی حملات موشکی و پهپادی گسترده نیروهای مسلح یمن، آژیرهای هشدار در مناطق «ینبع»، «الطائف»، «الجده»، «أبها»، «جازان» و «العلا» به صدا درآمد.
🔹
این عملیات تنبیهی در واکنش به تجاوز جنگنده‌های سعودی علیه «صنعاء»…</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/462154" target="_blank">📅 05:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462153">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K268qIBbLioor7vYxseWuTvLTt19wkGmoBcX8Ic7j-Pg7cbz-f7erLvN1YNQNqseAHKM6caJHgGY90JUZWztCGM-eLsZTNP7I6V9SlFUSdun6Xu4pLX6jM_76E1FEr_-5qqmZtUJNPVA2CxMmyGnhz-kuB7YDk70M8HTQLsOWx9HaVMT0YNKjuYgRV8JPDaOjGH_Gsix03NU4OHDT47FIuk4VkaKD9kMKsCVHXyYJV7OWZspMd3CfyvfjmOUsEW3U-635CgY9fKswjUCqw_vmI1iks1El_Jujy5i4V39DNl4cmF6FTfJeO2mBf02O-PDkF7iq1BL_JfqBP4D-4MgbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تکمیلی/
حملات موشکی گسترده یمن به سعودی‌ها
🔹
در پی حملات موشکی و پهپادی گسترده نیروهای مسلح یمن، آژیرهای هشدار در مناطق «ینبع»، «الطائف»، «الجده»، «أبها»، «جازان» و «العلا» به صدا درآمد.
🔹
این عملیات تنبیهی در واکنش به تجاوز جنگنده‌های سعودی علیه «صنعاء» پایتخت یمن انجام شد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/462153" target="_blank">📅 05:38 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462152">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">منابع عربی از حملۀ یمن به اهدافی در عربستان سعودی خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/462152" target="_blank">📅 05:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462151">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">منابع عربی از حملۀ یمن به اهدافی در عربستان سعودی خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/462151" target="_blank">📅 05:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462150">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5aab5fe58b.mp4?token=ZoL_5o96wdtET57mw25WwvU_EnXGEa66nFg7E4MAEIWylh_ItUfI_UrVaPnEyP5qIBCIE65nU8a6XDNxPO0abMYdSVYuKepjsx8D1T8BJpK4ObiFM4hKz1O7QXdcopeXW3Z9-ZvZIupjC9fdRPwd5_TfhRlZPTJsUhYeAv2JB9mIV_hvK6TQSz6fPHJ8nAJaDl_DVvCU68Xx8EsS74h1xK4Q9s082fuvZamY0b8VSAKndzbQYj05Kpr5iP9pJZsZNWDfjCS13DqJQ47q2jYjJNVCZK2Zq1EQMHULn0bv1mknl5EDYBgCELYxvjLs08gONaf7Z7Dc9dygSIFNomSINQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5aab5fe58b.mp4?token=ZoL_5o96wdtET57mw25WwvU_EnXGEa66nFg7E4MAEIWylh_ItUfI_UrVaPnEyP5qIBCIE65nU8a6XDNxPO0abMYdSVYuKepjsx8D1T8BJpK4ObiFM4hKz1O7QXdcopeXW3Z9-ZvZIupjC9fdRPwd5_TfhRlZPTJsUhYeAv2JB9mIV_hvK6TQSz6fPHJ8nAJaDl_DVvCU68Xx8EsS74h1xK4Q9s082fuvZamY0b8VSAKndzbQYj05Kpr5iP9pJZsZNWDfjCS13DqJQ47q2jYjJNVCZK2Zq1EQMHULn0bv1mknl5EDYBgCELYxvjLs08gONaf7Z7Dc9dygSIFNomSINQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از خودفراموشی خیلی بترسید
🔹
رهبر شهید: عاقبت خدافراموشی، خودفراموشی است. خودفراموشی بدترین مصیبت‌ها برای انسان است.
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/462150" target="_blank">📅 05:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462149">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajNsCT37vNehqYrWTpxHNsVzFizuzumIeD77FFCrgcrPKLpMungv9p4m179chcUNM3jcPuRnFz4hHIFUbytU61NuPVviIBx31ax8X8DSHZn_YVsBKmNY2IoTz--WQToJNjtX2BiRewJCIuAdNhxHAFa161KIrpqmPlTQbm9KlS93IMuteSDmW72aL7LZnvMfWAb8x5xu1S9S3Io-pTQTtSXcLqX-nTkKJLSZBUNIJtxwUPuC7Pq_lwuEKoOcl-PBtLT2p458lhcrLXM0h-gj_PJmJUoacZmemx1hFnmRyp95f5bjzTOc2-kOnM4_JS0z--bvHGr2diPrrPAG46F4CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملۀ دوبارۀ اوکراین به پالایشگاهی در روسیه
🔹
هواپیماهای بدون سرنشین اوکراینی پالایشگاه نفت شهر سیزران در فاصلۀ حدود یک هزار کیلومتری خاک روسیه را هدف قرار دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/462149" target="_blank">📅 04:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462148">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/462148" target="_blank">📅 04:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462147">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGbyyaEGWthc7tgAYyCaXvZ4td4cZKKvlW0ZoU5dyliQZhTZI6IIxv6Jvy8JJE0XUYGWlY7mWPgg1jhLa6fE_hjP1SjpipmbFNhkk4ufdiT05myB9KbAYGXQPHwYZxLaToyj7h_eiJPVGnfuYHvE34uoSrwwK25Acu7PXngfHcg09m1CzMbwgnRx47l5qsWehoENcWMLGnTrWvcD6GHPkczjSaicaQFq3aVNOyZ1HHgsXtcl4FCiqIw0T0E5oRUse7edZuSUrXqNZeUx8x_ObLUuZn9KOgmSEVZAPAtKvm8_Qf85tQVY8cLdfUN5qfaRSmShd6KLlZt9nOqnKBrP1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسۀ شورای امنیت دربارۀ وضعیت «باب المندب»
🔹
منابع دیپلماتیک می‌گویند شورای امنیت سازمان ملل متحد روز سه‌شنبه جلسه‌ای اضطراری دربارۀ تحولات پیرامون تنگۀ باب‌المندب برگزار می‌کند.
🔸
تسلط ارتش و نیروهای مسلح یمن بر خط ساحلی تنگۀ باب‌المندب و عجز و لابه‌های رژیم سعودی به غرب، شورای امنیت را به برگزاری جلسه‌ای در این زمینه واداشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/462147" target="_blank">📅 04:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462146">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JE17J3zfKaQTblNjgbiRwIeCGAA4di0_ap6Mx2eTMUPKd0TgLqmaAETidDbEGp-WpvALb7RGdxEuxKksLGyZq0T-4MJDQlLDbS6clc6WG2faOhDPKVWLFF8C8uZBEBUDxw-TqDsHVraHqNpGZKxQk-rmYB5GQoLZ-Jc_ixkAB7hGT-mYqG1A9cE31x9EILmqdnoNYP0jPWLex5drWuJBaGFA_eXAIyS0kEQJCM8CGqjlVlBrYPi5078Fyo9cuCOIIDyK-5lHOxo9NtDwkBIzxnrqa2RNALQghn4p09eOejySsoItia0CE5uG64E0LbgExRrvYfEWASyJfDKtO-bkfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از درخشش بانوان ایرانی در جهان، تا افتتاح آب‌شیرین‌کن و CNG رایگان برای تاکسی‌های اینترنتی؛ ۱۲ خبر خوب از ایران
🔹
«بستۀ خبری امید امروز» روایتی است از اتفاق‌هایی که شاید هرکدام به‌تنهایی یک خبر باشند، اما کنار هم تصویری بزرگ‌تر از حرکت، ساختن، ادامه‌دادن،…</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/462146" target="_blank">📅 03:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462145">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دفاع مدنی عربستان سعودی برای شهر ابها و استان خمیس مشیط‌ هشدار خطر صادر کرد. @Farsna</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/462145" target="_blank">📅 02:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462144">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دفاع مدنی عربستان سعودی برای شهر ابها و استان خمیس مشیط‌ هشدار خطر صادر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/462144" target="_blank">📅 01:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462142">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5db5249518.mp4?token=GPYJcqcH918pzQT1e5ElF-8qwwJ1W9WMtQCnjjYqd20SjMJoDrUv_-QZlYunkyOlXbGWbl8sdGAHCCS2626n8HaPTB7qb8g44YZK8lc8oULvRkA3JLjVdkmoL0nU6TfIGuHJmEy_wo3piJanwIFC5qZTwCjy6lGhjX33XedOmEIzK4xppzoZ4wdFSywQnOeFiin05IdlEYO1rXvT__7MisrnKa_trWPmeN5_zqRwh4hCoQSfECjKh3klmdb0_4R4zHz7CLWQfKXV2wQZBk3eKZhsko9tRdckkIIZliFADxb_6cd83N9Bftg-2lrqaKbKjUjdWupPkKM_bhWkwmIAUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5db5249518.mp4?token=GPYJcqcH918pzQT1e5ElF-8qwwJ1W9WMtQCnjjYqd20SjMJoDrUv_-QZlYunkyOlXbGWbl8sdGAHCCS2626n8HaPTB7qb8g44YZK8lc8oULvRkA3JLjVdkmoL0nU6TfIGuHJmEy_wo3piJanwIFC5qZTwCjy6lGhjX33XedOmEIzK4xppzoZ4wdFSywQnOeFiin05IdlEYO1rXvT__7MisrnKa_trWPmeN5_zqRwh4hCoQSfECjKh3klmdb0_4R4zHz7CLWQfKXV2wQZBk3eKZhsko9tRdckkIIZliFADxb_6cd83N9Bftg-2lrqaKbKjUjdWupPkKM_bhWkwmIAUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترور یکی از فرماندهان گردان‌های القسام در غزه
🔹
منابع فلسطینی گزارش دادند که در حملۀ هوایی رژیم صهیونیستی به یک خودرو در شمال شهر غزه، «أبو اسامة البطش» یکی از فرماندهان شاخۀ نظامی حماس به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/462142" target="_blank">📅 01:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462138">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LJxZAeQMLJVtVvK0LZTbgzjAnQsJ_jRkIw0zDLfoY1Sf_U0XYLH3d9oCnzrmboFUtyFofjgvuzWQ-lcMOZTwTmWkcYzcKhpj0-qStSgFEuihH9UakPiUO47Tbf81olz-5amwgVEyQiLDvpyq9HhUKMUN0bbQCNN3tPo9Q5gl8wIPwfW8geOIpn4NR1KAXVj1aSf33U52Xd1iQ-NAYialWZLM4yxM8IpGWWrP_K1NIbHE8ApY_LIV9jDH3RksyzYmMm-uvnrvhkeTA_0-KvWBwsatS4GkOYK1GPQDA-fqts6ofyjnXVQHeQ3-bZiRYtFeMfvU68UNLuE9yi0W9mROrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/awuN9MCnY97BotKf_IAZeYftBk3xyEJwZV_nLFJOK9bH_5nyHmlPu7rRpluKrxHp4l3LNWT7oEW-s7Uv_th9kgesvCLRJ0HlZXL7HWs-aql0qilWSJd2H_9aIX7XIm5uoBoGr9mY4vXhX0DaG4PzSuUTKl2cQt4f-TtBNTtbd6X_pJvLSxw7KmS7sM8TYctkikSTPanvrog0JFFWlRE74lKnQTyGH_F_-nJ1XiNg_v7BLyR2OPSi6Z-Mg_FwXOXGDBCywnp4STuA8Nk-1zDkjd0J-BaDb1CNkcvnaaskpWcltZlzIdaX7Px9HgVtR087fikeer7NMy3bBLtXGLcWJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IBqb8YPsHTVFJS7-7Yb___xkp3jjpQ4aTurRwV8veQHQHTSo2W7RHxsFwHY3UtQpesdPsG0XOYfEKADXU6TkUxKLYRSycUjo4oweq0-ktztQimPOGGOoXlMtv1d2YQA_W71_n-eE5nKF4tyk8mOlWQMkS11zVPWQIpS9s1aWk3bI2QCz2D5zZBWl_iIy3i4jVuZ1NImA0X0XwBM6WZt21qMgvbmNg0SsU8mukkeUPQQv2QijyY4qd2j0RlVv3netcXxZr3u0OTTbdtSZT_KMcAZNluZkwKF0OuX-Qc5l3Yl6EfO3aTtE2L_uclIojgsrXJ_7KO1oWvVaIkJPZql6vA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dcaf7c0df.mp4?token=Pdb-MNQrJISnzWHuj1kjyiNQMVPHtf_OpyVDYUWV_syzqpQCWyVX84rark9B2AeeMKQ7K_uCAK55_z9AmgSif9sS-T0IM94V05Xjlak1ngDhMBVSEWoVPqHzmCsMxvMH6-v-CCo2wBVOR6PGkZG7MI1GTEqUOHkAe6g_a1AgsH72A_Q-DwVVLwNcdWX-FVNtuBauaAnMIQIVqvEx-EZiBkbVPWRbpDokXmFA9X9RwdnCrDKHbau8w9YNEAMzmjslnihfqZzH_HfjpUR2R9sb0dMq9K-ui_uZj_I-MhChPtkjyD3RR1l86ydLNpMRuUAzBImmT2ElrVnc_YQIckvZbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dcaf7c0df.mp4?token=Pdb-MNQrJISnzWHuj1kjyiNQMVPHtf_OpyVDYUWV_syzqpQCWyVX84rark9B2AeeMKQ7K_uCAK55_z9AmgSif9sS-T0IM94V05Xjlak1ngDhMBVSEWoVPqHzmCsMxvMH6-v-CCo2wBVOR6PGkZG7MI1GTEqUOHkAe6g_a1AgsH72A_Q-DwVVLwNcdWX-FVNtuBauaAnMIQIVqvEx-EZiBkbVPWRbpDokXmFA9X9RwdnCrDKHbau8w9YNEAMzmjslnihfqZzH_HfjpUR2R9sb0dMq9K-ui_uZj_I-MhChPtkjyD3RR1l86ydLNpMRuUAzBImmT2ElrVnc_YQIckvZbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
حال‌وهوای مزار رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/462138" target="_blank">📅 01:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462137">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/948ece81c4.mp4?token=AFTmIsU9HBSWgipjAYkM_1dwxr8jIFWZtDa0vB617Eo4rY-lAvdXU1tOhDdk9PUlbGS5GEtxLBsuZmVxOQZ-H8XhF8K01fPPPSLpzv4Yer7uCjgTF2r45EfUoMECndTLJa23x5ZP77666kzVkG4e71L6oKrcw5VvItZ_QNax67wiFMUnHS5j57G9o_1SaDxo5XjemVoZMI6MJtyynUJGoC3Ksndu7C8kYUdB4-QGw8DlSWzeYN2G6MT_p-ysC3YnmUm_Usl0hJHuhqQS4ePpjwZc2V1GpwM-UOujlQJY_ycyvyab5P78h7GI3L6Xrrq4msrjn_OaPBokB3XZ_niaDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/948ece81c4.mp4?token=AFTmIsU9HBSWgipjAYkM_1dwxr8jIFWZtDa0vB617Eo4rY-lAvdXU1tOhDdk9PUlbGS5GEtxLBsuZmVxOQZ-H8XhF8K01fPPPSLpzv4Yer7uCjgTF2r45EfUoMECndTLJa23x5ZP77666kzVkG4e71L6oKrcw5VvItZ_QNax67wiFMUnHS5j57G9o_1SaDxo5XjemVoZMI6MJtyynUJGoC3Ksndu7C8kYUdB4-QGw8DlSWzeYN2G6MT_p-ysC3YnmUm_Usl0hJHuhqQS4ePpjwZc2V1GpwM-UOujlQJY_ycyvyab5P78h7GI3L6Xrrq4msrjn_OaPBokB3XZ_niaDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۹۸ شب از خون‌خواهی مردم قم؛ داغی که سرد نمی‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/462137" target="_blank">📅 00:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462136">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DT1Db4YYp7Xk4D41sD9IVPDJhZXrW_SvdZYlCos2SJ-KjKe6b5TyvNuLctpQhoPuTJVY64wEFoOmPJLzRxqnWEMG_c5Ge1liWil91KrGg-cSLIGmCb7C6wuRsSDl3XKpOH0fnTE9ptwX-3tAczaKpHaziuVpKj1uL6PRPUzjhzAePj-HZYx6GvY1P82RQu3B2pI5JG95iY29AK-rNsU_NAklHitl4slfdWigsHPdw-gNiEOk1U6LvrNtDNawActvLYLlBVf-2oaD_tg41jiTnpLdPBx0O7uAOgjbthN0figsQVDK6b02eDv5jPIBte4HxaKB1-3D-5tNs6erT-d5aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دبیر شورای‌عالی امنیت ملی: تا زمانی که شروط ایران محقق نشود، هیچ مذاکره‌ای در کار نخواهد بود
🔹
با سیگنال‌های متناقض رئیس‌جمهور آمریکا حواستان پرت نشود؛ از «مذاکره نمی‌کنیم» تا «برای گفت‌وگو آماده‌ایم»
🔹
معادلات مربوط به نفت و تنگه‌ها تغییر کرده است. دست و پا زدن برای کنترل تبعات، جلوی آنچه در راه است را نخواهد گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/462136" target="_blank">📅 00:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462135">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkzf-OM2Bryb25K1t3-jQ6hRsO7Q-DgoJSd_ZlzPcwqAkADaNnKR3jT8lyYP1wICEuX0DnIBjUivmfb1JYJFGO7XaxIDusCRTorM0kYegFxsyb80fdvFARqwigXgZUB6zOjPjlRha5Kjf-ct9IEOS00C_NCRPf3JKPhHVuU9zjOVPEjFdUBrQNTskUVRTWLg0yNCFSYKG4tkuxu8T0_vLvJ5LtHkcmgGMw6yFaf0QbpcSmtM9IfXKF7bqj-mt9SMwrXFi78Z9QsknkkfpqkvSOjDKyLjfrWNCYwyvBHpv1zFA9DNBE4m-DU9LLWVjBIw_qEVdn_b7s_Jw_6CbYYnsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه شد که پس از ۶ ماه، مصاحبۀ جنجالی خلبان آمریکایی منتشر شد؟
🔹
روز گذشته، شبکه آمریکایی «CBS» در مستندی مدعی شد با خلبان جنگنده‌ای که در ایران بود، مصاحبه کرده است؛ یکی از بخش‌هایی که در این مصاحبه مورد توجه کاربران خارجی قرار گرفت، این است که فرد مصاحبه‌شونده می‌گوید با سرعتی بین ۱۱۰ تا ۱۶۰ کیلومتر بر ساعت سقوط کرده و بعد از شکستگی در کمر و چند نقطه، توانسته تا ارتفاع ۷۰۰۰ پایی فرار کند!
🔸
مصاحبه با خلبان ادعایی آمریکا، با تأخیر حدود ۶ ماه منتشر شده است. جدای از داستان عجیب و نسبتا تخیلی در این مصاحبه، انتشار آن در چنین زمانی، می‌تواند دو هدف را برای آمریکا و شخص ترامپ، در پی داشته باشد.
🔹
کلید اول حل مسئله، این است که داستان را از روزهای اوج جنگ ببینیم، نه صرفا روایت نجات. در طول جنگ ۴۰ روزه، ایران جنگنده‌های متعددی از انواع مختلف آن شامل F-15، F-35 و A-10 را هدف قرار داد.
🔸
در ماجرای یکی از هواپیماهای هدف گرفته شده، اخباری مبنی بر سقوط دو خلبان آمریکایی در ایران منتشر شد؛ ایالات‌متحده نیز مدعی بود دو عملیات نجات برای فراری دادن این خلبان‌ها انجام داده که یک مورد آن، به طبس ۲ معروف شد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/462135" target="_blank">📅 00:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462134">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15b6db87a3.mp4?token=FxIZUeaQb6la_YCKPF8tVFR_pbHpEccF6QwCSg3svwYZpGsylEvdI6BogjKqCfuVw9FD-k5rdNeen2qJHQT4AcwML0I6a4RcpaPOU7DoOqERhj1rMyomAXz_-owjHo-g_q5NdcgMwVjaXtCaRtW9QyCJ-YvRmDKu0QvWZR4OxFY6Sw2eNVJ9b9p6tuCRsfw80121g5k-sGd5Z-MEIc1aJFwx7yXYp6tt6LGMaW8Z8kQP-t64s6HKODS54JQd-lz98igj7GerMTzWr2VFWAdbzeCLy3jYinQgtC4pwz0tD_gHwFLAKEaYC5ZNzcBbrs_WgY-7lfyS5n9b0aEIC4LMzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15b6db87a3.mp4?token=FxIZUeaQb6la_YCKPF8tVFR_pbHpEccF6QwCSg3svwYZpGsylEvdI6BogjKqCfuVw9FD-k5rdNeen2qJHQT4AcwML0I6a4RcpaPOU7DoOqERhj1rMyomAXz_-owjHo-g_q5NdcgMwVjaXtCaRtW9QyCJ-YvRmDKu0QvWZR4OxFY6Sw2eNVJ9b9p6tuCRsfw80121g5k-sGd5Z-MEIc1aJFwx7yXYp6tt6LGMaW8Z8kQP-t64s6HKODS54JQd-lz98igj7GerMTzWr2VFWAdbzeCLy3jYinQgtC4pwz0tD_gHwFLAKEaYC5ZNzcBbrs_WgY-7lfyS5n9b0aEIC4LMzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۹۸ شب پرچمداری نیشابوری‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/462134" target="_blank">📅 23:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462133">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9938f8719.mp4?token=CQvO-x9PEGTGVyDp2QXrt8L2YABhsTPOxEglSNKd96KSvinmNf97wPLIpdAcQS2JLUkCSLtiG_PKSw1rVF-sIhM5XA7DxFrl3C2klxWNhEzreatUkgICoFB6qgC-NDKutQZqMA4UdH1jDnauhr8aKKugW6cpA-HO1P0e8NLAejr0KWOUKEX_6XVDh7cKNwBt6ihWNmYwz8L8lWEpdGi9NhV81v-MQ00HxbRQa1SApxxoOGVTJf-vhJbW9IFeVkcJARNxuttyeVp0UC6_r2s62KwbGYTVdC8J-1iqhoRSvNnGnm62EwQy1jIlB1fSSAEENkmp6fwiirOWWrb5q0qwZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9938f8719.mp4?token=CQvO-x9PEGTGVyDp2QXrt8L2YABhsTPOxEglSNKd96KSvinmNf97wPLIpdAcQS2JLUkCSLtiG_PKSw1rVF-sIhM5XA7DxFrl3C2klxWNhEzreatUkgICoFB6qgC-NDKutQZqMA4UdH1jDnauhr8aKKugW6cpA-HO1P0e8NLAejr0KWOUKEX_6XVDh7cKNwBt6ihWNmYwz8L8lWEpdGi9NhV81v-MQ00HxbRQa1SApxxoOGVTJf-vhJbW9IFeVkcJARNxuttyeVp0UC6_r2s62KwbGYTVdC8J-1iqhoRSvNnGnm62EwQy1jIlB1fSSAEENkmp6fwiirOWWrb5q0qwZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی ناگفته از جنایت آمریکا در سیریک
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/462133" target="_blank">📅 23:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462132">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOG3-VBpmVXoVyHSs8XJCMCJ062Ygy8tQOG97nLZtrgRAwtrJiBibbKFM5XHj_L4BoPd0S6zqufPxLesjyW5lqSI52PeWLSEsShKiRCKeU9Vr1uINJIcuM-tPhlWfzELkABIJjdRqJ1Oa-wE0VQlOU8Gi6VAom36O1UkRHTd8ptRkNrU6PL8mwTNht6DLHeF27USQmV_1xP8o7MEDMdoA8RM2eWXNqSMnWoVkOJl5CNC-tQeOXY4LMITDv3dtEYdlj8Ha3mU5AVjmKtORnCvjDdBBXJttQSnvzfZB_met9dDWcG3UeIydjmjQdH5S5iN8TfBtrDkJeI0f_BtvHsGRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهنمای بقا در طوفان، چگونه از صاعقه در امان بمانیم؟
🔹
با نزدیک شدن به روزهای پاییزی و افزایش فعالیت‌های رعدوبرقی در آسمان کشور توجه به توصیه‌های ایمنی برای پیشگیری از حوادث ناشی از صاعقه اهمیت بیشتری پیدا می‌کند.
🔹
کارشناسان ایمنی همواره تأکید دارند که با آغاز رعدوبرق، بهترین اقدام ترک سریع فضای باز و پناه‌گرفتن در یک مکان امن و مسقف است.
اگر فردی در فضای باز گرفتار رعدوبرق شود و دسترسی فوری به سرپناه نداشته باشد، باید این ۳ نکته مهم را به خاطر داشته باشد:
🔹
از نقاط مرتفع، تپه‌ها، بلندی‌ها و درختان تک‌افتاده فاصله بگیرید.
🔹
از اشیای فلزی و رسانا مانند دوچرخه و میله‌های فلزی دور شوید.
🔹
اگر موهای بدن‌تان سیخ شد یا صدای وزوز و احساس غیرعادی در اطراف خود داشتید، پاها را کنار هم نگه دارید و تماس بدن با زمین را به حداقل برسانید.
🔹
توصیه می‌شود افراد دست‌کم ۳۰ دقیقه پس از آخرین صدای رعد همچنان در محل امن باقی بمانند و سپس با اطمینان از پایان شرایط خطرناک، محیط را ترک کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/462132" target="_blank">📅 23:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462131">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
حمله پهپادی به ۲ قایق صیادی در آب‌های هرمزگان؛ تعدادی از صیادان مفقود شدند
🔹
معاون سیاسی استاندار هرمزگان: شامگاه دوشنبه ۲ فروند قایق صیادی در حوالی بندر کرگان در آب‌های خلیج فارس مورد حمله پهپادی دشمن جنایتکار قرار گرفتند.
🔹
درپی این حمله، تعدادی از صیادان حاضر در این ۲ قایق مفقود شده‌اند و عملیات جست‌وجو و امدادرسانی برای یافتن آنان آغاز شده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/462131" target="_blank">📅 23:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462130">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJVqPD6BgLDgpnGcyA1syrk10nLSkJcqOWfrUZYn0TQj8NoEE-cFZS_fYBhuD7Y_UzqYCd4Q4Q67W_GvvmetFf48MTbfXZAIjcaWmJgh7OQ_ixb9Hl9hI25MvKrYJwb4UaTvDMRJ31lV_hMeTE9_yXfAK9PHhSIeZPE1W741cQEj7jR532_xN3AZB3vfXyTeO_GLhkwwPVi-B0QFfdu0auM_z1XjXCPMXIctYpd0OS9gAcB5GtIA9lDIpi21FPYGdzS6ahemkYhZPrUivkKi5CKsrsTxz-44X856k1KZ7dbWYekSLPy0ZfYnjwnVDUiYAPIDedYHx4bU1iWoc_HYVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🎥
گل سوم استقلال به السد توسط قلی‌زاده
⚽️
استقلال ایران ۳ - ۰  السد قطر @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/462130" target="_blank">📅 23:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462129">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65187ac504.mp4?token=ICd7x4Obotafep_eO3MdAvNsNXJMSK6ymepf-IfRSWM20BU7TLTz6ToRwUUh4RUo-lGdbd2lYc5nTwbbVZ8nfBLRP-UHEXJ1FfC-BqaD1hmWMXGIYbFhHjZfkgjksahiu_eEQC0tPEVuNvDFS0ljAzgOySWxiJvqYzYJ_u-ZoVlDdigMNdZ6sfVLncQOkZNxLuYlJ8Bhv70QkT1MeBVjygpl09RSp2_cstfYVAsUFMTF5cKHcONKJswooo9oj7X90ROs2PnrBVav3anDL9NhUdIuzMpkQnhh3piDhz1heBAC4vscDB6lvrGsogmeo-Qn7Hntzx9o1lqFFSBlscDIGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65187ac504.mp4?token=ICd7x4Obotafep_eO3MdAvNsNXJMSK6ymepf-IfRSWM20BU7TLTz6ToRwUUh4RUo-lGdbd2lYc5nTwbbVZ8nfBLRP-UHEXJ1FfC-BqaD1hmWMXGIYbFhHjZfkgjksahiu_eEQC0tPEVuNvDFS0ljAzgOySWxiJvqYzYJ_u-ZoVlDdigMNdZ6sfVLncQOkZNxLuYlJ8Bhv70QkT1MeBVjygpl09RSp2_cstfYVAsUFMTF5cKHcONKJswooo9oj7X90ROs2PnrBVav3anDL9NhUdIuzMpkQnhh3piDhz1heBAC4vscDB6lvrGsogmeo-Qn7Hntzx9o1lqFFSBlscDIGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درخواست جالب حردانی از نیمکت استقلال برای اعتراض به داوری پس‌از دریافت کارت زرد  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/462129" target="_blank">📅 23:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462128">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a62c00b98b.mp4?token=t3oCClXy4uxybVNjKqf8bq7AmV9lIDVOS91dSp0SkeKYlBH7y01yvJpf7qK6Th4C_rlQdcZkMDdoXaKdPDi8A5_we0ba6bRBxBwUuupW045ac1V9RSv5VVukafNeDhav-zt1Dz5tyJCuz1YyV2jCCI8DOaX8TFITF9dImbodjPyXjzok8xij8NJiKGowU_Tv2KHn4v8hzEd1u5TDit-kWPUSgYu_BCGpDphO9obma2XxFKCzT-K1xplyz9OQJ1UHbcgvMhy2FHtX2uxiIX8br6JrphgtWaX_vnj-zVKbHyVgbKgpR72S4-0JmraOueHgUpb9v_I7nl8wg5Ys7E5vnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a62c00b98b.mp4?token=t3oCClXy4uxybVNjKqf8bq7AmV9lIDVOS91dSp0SkeKYlBH7y01yvJpf7qK6Th4C_rlQdcZkMDdoXaKdPDi8A5_we0ba6bRBxBwUuupW045ac1V9RSv5VVukafNeDhav-zt1Dz5tyJCuz1YyV2jCCI8DOaX8TFITF9dImbodjPyXjzok8xij8NJiKGowU_Tv2KHn4v8hzEd1u5TDit-kWPUSgYu_BCGpDphO9obma2XxFKCzT-K1xplyz9OQJ1UHbcgvMhy2FHtX2uxiIX8br6JrphgtWaX_vnj-zVKbHyVgbKgpR72S4-0JmraOueHgUpb9v_I7nl8wg5Ys7E5vnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تداوم حضور مردم گناباد در شب ۱۹۸
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/462128" target="_blank">📅 23:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462127">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTQ0XUKDbOv828Hsm5tYMAzBjuaJRt003jIi2FFu9Haz4lfLnr7thecFqIUPRwduTOqZ-9L8KAs3PILgWPEUW7aWq6cnEY9oR0hfcqcRCslQrxbDH1fyjLox37MAJxLUEg2EHHggLcfcojZMTJBC_UTsDhPj4thHhupo0PaC-VMfqrLcCMd4MsmIrIj1mjzK10MJ6Xp75LvjTRESZG25fKzp0a5WxgCwc09XlFQEBEWNHPBxw-DXez0mWUdCMUWoZWeDKXBjM0emxhTxCKLft0vZpZUIKjDfVKRaYzLVjqPwUMgr7g6CrCOgsff_414wM6NaHpMpoM0MGIrg1_n-jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسلط ارتش یمن بر ارتفاعات مشرف بر تنگۀ باب‌المندب
🔹
منابع یمنی امروز از پیشروی میدانی جدید نیروهای انصارالله خبر داده و گفتند این نیروها بر ارتفاعات راهبردی کهبوب مسلط شدند.
🔹
شبکه خبری اسکای‌نیوز به نقل از این منابع گزارش داد ارتفاعات کهبوب بر تنگه باب المندب…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/462127" target="_blank">📅 23:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462126">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a5d1d8cf1.mp4?token=LastXynXNKkeiveA6BUtklKFb2CiRRvi5NOjGXKUiXmfNhIRe_FNuPJEMpvGRE7hD4o7kuNR5U0LnnyzWrKeyht1Yx4s8K66cLspe53KnMqLvviN9wkgqvdo1pOGf6djVh_lEnP3Hz1OIMZmXkby1YzBvCiK1BV0AVBYbWdXg4qryjpqPWq9jtt89t92B9YCvcEGUudanysPvI6xr1Q84SCEGPM4Aq3vkUy8YR9Qx-N1mwxoGFVwa3lP20hVKteJfBTDB3Gu-kYsV8ay-imDZtxQL7spOH7rogHmDKtbhEseeH9b3fCcyYPPnZErhmBUpNdvfHPDVGGB5U3AAsJHGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a5d1d8cf1.mp4?token=LastXynXNKkeiveA6BUtklKFb2CiRRvi5NOjGXKUiXmfNhIRe_FNuPJEMpvGRE7hD4o7kuNR5U0LnnyzWrKeyht1Yx4s8K66cLspe53KnMqLvviN9wkgqvdo1pOGf6djVh_lEnP3Hz1OIMZmXkby1YzBvCiK1BV0AVBYbWdXg4qryjpqPWq9jtt89t92B9YCvcEGUudanysPvI6xr1Q84SCEGPM4Aq3vkUy8YR9Qx-N1mwxoGFVwa3lP20hVKteJfBTDB3Gu-kYsV8ay-imDZtxQL7spOH7rogHmDKtbhEseeH9b3fCcyYPPnZErhmBUpNdvfHPDVGGB5U3AAsJHGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🎥
گل فیرمینو به استقلال که به دلیل هند مردود اعلام شد  @Farsna</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/462126" target="_blank">📅 23:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462125">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZByaiu_AckIfEi9Vahxz4lvs02yhXmMmZYhh42uz0fbd1XLWsiVDqsl2Ce_HRwFsuwKE1OzUl2UX2MFAMpx0YVdUTR9R6oqZdHot8bnm-YUtj-2mgqDCNqrUvQiow3bOAB3iaHJ_3HNi3NXktX0M4hATR5cSOwnBwaJ48rAy8zLDTzteAPXv5V2FwFn3B_LEoaI-OHLd9ZQFvDcLoQyf54-JYQqwj1ZTmaH-FQzKCUwNrAvu8yRxJTZsCXnTA3hH7FS2UKTQPWAR3He4G8VlWooBinXHZjdI9JnjMsAK3ubCU4ntodnwybXgpPwGM1WjeV2PjjIfbIcpaf1elZ0jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیف و کتاب را خریدید، اما این یکی را فراموش نکنید!
🔹
با نزدیک‌شدن به بازگشایی مدارس، آماده‌کردن کودک فقط به خرید کیف و لوازم مدرسه خلاصه نمی‌شود؛ آمادگی عاطفی، به‌ویژه برای کلاس‌اولی‌ها، اهمیت زیادی دارد.
🔹
درباره مدرسه با کودک صادقانه صحبت کنید و فقط از خوبی‌های آن نگویید؛ دلتنگی و سختی‌های روزهای اول هم طبیعی است.
🔹
مسیر و برنامه روز مدرسه را با او مرور کنید و اگر لازم است، در خانه مدرسه رفتن را تمرین کنید.
🔸
اگر کودک ترسید یا دلتنگ شد، چطور باید با او رفتار کنیم؟
🔗
در
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/462125" target="_blank">📅 23:20 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462124">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVJM2J0UxmRl0bL7mGtdoglPQNC5qH6xsATfPyU45asWc6NtpNs-nGuUeSr04YKsPPOi54yr_PMVdobUpnEqh3kvU92afrLH_HqSTLKRo_rEm_c3wWeHapc5diBnJ1J4MVHlYSG1xtF-nophT237ayh86FvGJl67As6tudWBD_CIb4vNxfXqFDc0Bp0h0W1YpGwnc5MpyobpeSzOfpSXRMKgVUfVmsLDnG2zGYTCblP4tkH2gheMhQkqAngd49kIX0A2sS6m05DrMAy8RU_iJivMURpPP9OlAOcd1U8pDmYGTefLw8iqpWAjCgSTJXNelHAtzp5tKXdyk7cqWrmADw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی نیروهای مسلح یمن: جنگنده‌های سعودی را با پدافند فراری دادیم
🔹
یحیی سریع: نیروهای مسلح یمن دقایقی پیش موفق شدند دو جنگندۀ سعودی که از پایگاه‌های خمیس مشیط و طائف برخاسته بودند را در استان صعده رهگیری کنند.
🔹
این جنگنده‌ها با استفاده از موشک‌های پدافندی تولید داخل، هدف قرار گرفتنه و مجبور به عقب‌نشینی و بازگشت شدند.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/462124" target="_blank">📅 23:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462123">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/py3zumxgrRkm2uZWRvQyEufVg4s0mXV5TEmOs0an5c9RX2QxLuLWwhU_6FfOHCkrvMxdYx4qGtKX8LZ5e_UwbwyPV2RgrOdTegcGUXVTxvO0lmHT8TOKFxHihWTKB0-homeEnNw_Ji79LNrUzDmcIyrJ1zvlt5yoBm2HhSUEtst7KJgCDNDzxSdPevWQD85sGLKHns84e-_N1mNsyawbiFhC7mg3yvdtvajU0jj4FJ8JukJQCdiaPtgQOwmCyRA1Ar_PX6WNmW9XI7nzj1zFm8NbCN5Nj0MDZeYVRHe4VGqqJ3be1wwcAUtOwEkZ4XbGBXFJLuagcayYS39gxDFLVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اقداماتی که در ایست قلبی می‌تواند جان‌بخش باشد
🔹
در شرایطی که فردی ناگهان بیهوش می‌شود و پاسخ مناسبی به محرک‌ها نمی‌دهد، نخستین اقدام، حفظ آرامش و اطمینان از ایمنی محیط است.
🔹
امدادگر باید پیش از نزدیک‌شدن به مصدوم، از نبود خطر برای خود و فرد حادثه‌دیده اطمینان پیدا کند و سپس ارزیابی اولیه را آغاز کند.
🔹
پس از اطمینان از ایمنی صحنه، هوشیاری مصدوم را بررسی و در صورت پاسخ‌ندادن، فوراً با اورژانس ۱۱۵ تماس بگیرید.
🔹
سپس تنفس و نبض را حداکثر طی ۱۰ ثانیه بررسی کنید و در صورت نبود نبض یا وجود تنفس غیرطبیعی، بدون تأخیر احیا را آغاز کنید.
🔗
چطور عملیات احیا و ماساژ قلبی را انجام دهیم؟
در
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/462123" target="_blank">📅 23:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462116">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P0NmSQeeHTcSVxqyAwBhkaM4-rZk8B_qrwkn34Mjc4p1dRYQCuGOrGnMDWSxdezEn1wzIcbp27Z1iX3-aIA8GrBdmPL9k2AbodR5Fi2uB0REQ4wqsFzDg6rqcnPnZ-KFzu81e9AcvwXCYOZe8XAFCgEqceecAtOm_GHIl-jci3bSJZMIppr7gyh3go-NsNeDgmTb9hNL09EFnxy9EG2GnecKOMlKwhaR875ccDvOLyQeFakUzPfXI_9HuTt4RMfILzxKftNyqGeLe-bVVncTkrYnDQQ-bm04IWb_JzDn-SWfOCgvGWAdoRaowQo_q8bDZjw26RoM6osF4EkGiBX4JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d-D--Nzpp-XOCvUphJ1wF6UfhmxcK-QRo5LJTJQgCRadYa4vUDPIN19ic3lNinE3oq_WJsHSMylzQOxstncdrWdG31Mlz3aILOJKrDNiPU1SS9euv3rYt33-NLirsd4t6cfQ34Jro9wj9G4vfllsBUEp81ICtoGRM62vbBqV-G1-lsjYMmjRXP1QSkUZOvbtn7VV3Fgok7ItPJYqMfKdIQHXmwU2cRUH_fAkVVAMixSw3INuRxDirVACOC5vHx1fchczicePUXTEriNNPkD7AU31mSYr6tgW280rzoiPgGhtSM9cQUJmCMiiiE5M630CZHheMdYlwwr3aEDTeXV0Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nzRgQVWveiV6rb6EW6gJVBkmwxqE5-a7DIR8bBZv3uZkwn6qkIX0DQo9QgJ2QF7XMkFKO3qfrkoxJjeYRYMgyLhzxPObMWCAqOdN1QRopJjw9x-9d_KdSV0E_oa4dFrZ7EsMeylNWcgp6w4rTKvdoBjeMll2Ni1cME1j8jCwy-aYDKNBQj50kSIZJ_1TYrDx0Apq4JSC-vAZIb6biTk8vR22c1xNZE-G5N_K_SeFXypxjXIICVumFMm9KhUZCRlzJOjn3lXMopNBYFzHZpcb77q2bL-HN6mDH-pC-7Ngg9ka3d9cy-1kRSY9MJepJvhfRkV_ree5HYShuoVd6_Ap3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HFsl6511J0CFQl35i_Wjn-QNZ-Yyn79F5kD_vtxknX3DKupYkL5ALCYOZcxxt21yt5bdlKbZ25WOQnJUTz8P5htQSWwFx1d19TQSSB2m4u1lWsGli7ArkEoMXiyr-U9OB2QmmlEN3d-1ZNAxBDllxA3438ze7hXdlkRRY6HpquoGys31FSKQ6DyoDN2mvzzSPwNCLO74DIjgVim3b3lhJEmwXYu3KrCbZqoBgBFNPAtUenmvfitgBW3n5iE-mnsztH9H4A7wKx9SzOSIQJIteUrmMdN5E8kqrnW0Jb3-cpSpFJOtLJmCRXKzUwktPxCaPpB9PvuC1ZqbGim-CYrtzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sHkGA_EzTqa0Ec5fDmsyi2VNM9MwaCTpZ339SJ0KASgAgeFX7qXV3iui8Tu3-k0-kV1abPoFJrE4CoG16O486GD6dUhRZto7fZYC7nBncH9__NIFopOwUqgcJRsG6PGBBp4owOuYoenpr0u0pze-yP33n5-H7XRR-8C5n6KlLpAFnM8A9J_IJElmZI8OuPxFyZHPrlHjwhUkFA5ton6mwYcF9I4ONc38pqEwILgloKwath7R2pO7sWYWci9aY9oKsVS9_LuatKaN0Qdggdsuw0lOwhxX73jMO0D4B_oSfj3YSrdYTdoAUjDErvleWPhS-wX_2r1uG4e2mCCHTP9Dnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WCUdy5WJEg-c1MBe3NeMG9NBdN3-Rh6Wt7W57xt0xaNOiK2hN4FV5eV_tD8ytewhab_8pWBimtV2O6ZL6uju5iNygaksINjudZpch9geWf1baT-0CyauJWcx79_3bbC-WuV8HD5ohpZTwzHzq-lA0tR1d_I1QFZNdzyPaVKFAxfY_eCGNXSjNhCT9Py9-U4xwHQ0tm2lRXSbNK2qqkZ528lDtMUctokMQD0lO0dkQuGM4xMHU69OF40b7TfAsCKeJ9cvV4Hhx47G36BkhvcfZQpflSCpkr31Ah0mEiutV93_7p9MeRJED9V6A6p3RBdsUor2ufEpsOUjW1sg92C1Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mHhrrWRuvgxs460SOFazBP2Ta98zFjXFxdb_rBTu0ZWua__tHC3cGNRkN6DB16Z_1UGB44HGhmVMSnX_5N-x9z0QtQuH3_0KRCy4bFUuXmiOdx7zAZN1lWwer95TsOWLmmQSyJKCz-bRRex9V7fPO1QVRLJpnXKID6lcaOpzrtHXwnEyLAyaD54WW68Ico4EPYvQp96J9-C5XB6VF5WADKZ8496qRNSrWTIbjIwX09zvgDpLK3qu0sibxt4nE7aYe_NUVjhDGL9jiDkgD_7CQRUxA5d3n0bMKnUlh8Q4OJdI8X7SAgLI9kbIAxe0jOJzXzkbAFNeRgu5t4cpJHGQ6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب‌هایی از حضور رهبر شهید انقلاب در جبهۀ حق علیه باطل در دوران ۸ سال دفاع مقدس
‌
@Farsna</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/462116" target="_blank">📅 23:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462115">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/519889c5e4.mp4?token=RE_MQ_VgmC5Q4B_xZG2-ZYp_dLUi3zNVU5MMnROyxzlWbMSbvAYKxq1ko6i28CSv3twMKM1fLZfvumLzhJZaeqtKAix3UIz6-Evkm2wAJ2_2eOS588j2ZqIMnOSEL43ffXQ6nJZoYE5EadRzS670PqevHFAjPv1xcJoLwQHawT7C0xRycz6l2yIT6T-7B0vP_64TxDuRUdPki-aeyhV0wupi676ufL5A3DyX20X-DOLcfeSw-XjgtTbMQmxBpXk9EDgd_qrozcV32x14u2OtOnku8Bb8Hh-6EyHn_Pci98k54QVIIWbmYmZW3V8F1xmcur-Pyg2Z5Xzpxm_Go2ykRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/519889c5e4.mp4?token=RE_MQ_VgmC5Q4B_xZG2-ZYp_dLUi3zNVU5MMnROyxzlWbMSbvAYKxq1ko6i28CSv3twMKM1fLZfvumLzhJZaeqtKAix3UIz6-Evkm2wAJ2_2eOS588j2ZqIMnOSEL43ffXQ6nJZoYE5EadRzS670PqevHFAjPv1xcJoLwQHawT7C0xRycz6l2yIT6T-7B0vP_64TxDuRUdPki-aeyhV0wupi676ufL5A3DyX20X-DOLcfeSw-XjgtTbMQmxBpXk9EDgd_qrozcV32x14u2OtOnku8Bb8Hh-6EyHn_Pci98k54QVIIWbmYmZW3V8F1xmcur-Pyg2Z5Xzpxm_Go2ykRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل دوم استقلال به السد توسط سحرخیزان
⚽️
استقلال ایران ۲ - ۰ السد قطر @Farsna</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/462115" target="_blank">📅 23:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462114">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5992d64136.mp4?token=bDwNYl30RZ0Shg5nyfi6KaJG-9bIWflB4JbL3EWQ53eOvX8WtrtWtlIPajqZuUvZ-lotu7jOkHOOHlvgSxSjXurNhKZKa031OQrkNpIHdDlAn2hhWIf4puAi6WzJt0pVH8O3EMWfUoOhTtPARPPrvzo3H39f0W3UOkFN09oQ9ed_hlXjhS24235Oggdj31abIQKkjaCBo9s0trfatV8Z2cYl5Er-yU1tGLBhGAIGxZ4bdtZ8VMoiOjC2jvrphmTirsX1yNEu9LzTUR3LmQS-3JmKFKUCfj6uMQUzjlABqrZHzVKp4F-rbFMzabQk2caCm_r0D4wgXrdOdbmwZGCbOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5992d64136.mp4?token=bDwNYl30RZ0Shg5nyfi6KaJG-9bIWflB4JbL3EWQ53eOvX8WtrtWtlIPajqZuUvZ-lotu7jOkHOOHlvgSxSjXurNhKZKa031OQrkNpIHdDlAn2hhWIf4puAi6WzJt0pVH8O3EMWfUoOhTtPARPPrvzo3H39f0W3UOkFN09oQ9ed_hlXjhS24235Oggdj31abIQKkjaCBo9s0trfatV8Z2cYl5Er-yU1tGLBhGAIGxZ4bdtZ8VMoiOjC2jvrphmTirsX1yNEu9LzTUR3LmQS-3JmKFKUCfj6uMQUzjlABqrZHzVKp4F-rbFMzabQk2caCm_r0D4wgXrdOdbmwZGCbOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۳ قدم مانده تا وعدهٔ دیدار دویستم مردم در میدان اقتدار
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/462114" target="_blank">📅 22:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462113">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91cf20989c.mp4?token=bNZQwQ0klB4iNjSQgn4GgxXDLZP4eupUEGI7aLOd0yvBpJ0HhSZTx0c8YRH3nPhNHPbUaIfyE4y2YUcGSNEoEJIvVrnKULLRD_noRFCam_XmVLMmWjretQPpa7jwEcvW5HEeeqtqvVJpB2n3XdWfrSZpZHcsl2U18MCKriBrWi5UpUA0SguY7-pSJIlF5pE0uHhuVS63vuSYO7n2KtY4vAf7GslNQl8SMOl2UEEqdpHxYr_JfNpWvMSx1bJ7jAepF97UZf4Y5wJkN5U5vGVwEzrBH8md78kXkL5p0eWX3LJOM9EkCOZagSDiMRE2b4leoRO5fR6aAlDEeaafAMNfBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91cf20989c.mp4?token=bNZQwQ0klB4iNjSQgn4GgxXDLZP4eupUEGI7aLOd0yvBpJ0HhSZTx0c8YRH3nPhNHPbUaIfyE4y2YUcGSNEoEJIvVrnKULLRD_noRFCam_XmVLMmWjretQPpa7jwEcvW5HEeeqtqvVJpB2n3XdWfrSZpZHcsl2U18MCKriBrWi5UpUA0SguY7-pSJIlF5pE0uHhuVS63vuSYO7n2KtY4vAf7GslNQl8SMOl2UEEqdpHxYr_JfNpWvMSx1bJ7jAepF97UZf4Y5wJkN5U5vGVwEzrBH8md78kXkL5p0eWX3LJOM9EkCOZagSDiMRE2b4leoRO5fR6aAlDEeaafAMNfBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: آمادگی داریم در چابهار با هند مشارکت اقتصادی کنیم  @Farsna</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/462113" target="_blank">📅 22:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462112">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26fb118626.mp4?token=qMG8j8BUl6TZ_lar8M5bc04n-hJWBhDX4ZpJephQaOr2HnxDrSFrbKE7efx5sNVEV33NPRzIhata8-FizR-0uzZSQ_YC1PHi_Tw7fuHEvXI8c_ZSQlZASOXeK6tzO8kF-tZ5Cnmpg02yYN6R7DhW4pjHjRAIaQ4gFVwevEW-_E1qF9sI-nPZmWEGVNqf4dO2_-Ko1Vsw6tBYecYexU0VNc1WFLc9zJkayOx1COKPkO0PuC4vm3ImqL0f8IpbjYnsUqXIbDkhuvKXANRn0AarEhq6x3JMPq_JXfIi5InSykhiwssfQ6Z-eTBn8P4tgA5vqdLv2_sUQOjPM-mhKHD3Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26fb118626.mp4?token=qMG8j8BUl6TZ_lar8M5bc04n-hJWBhDX4ZpJephQaOr2HnxDrSFrbKE7efx5sNVEV33NPRzIhata8-FizR-0uzZSQ_YC1PHi_Tw7fuHEvXI8c_ZSQlZASOXeK6tzO8kF-tZ5Cnmpg02yYN6R7DhW4pjHjRAIaQ4gFVwevEW-_E1qF9sI-nPZmWEGVNqf4dO2_-Ko1Vsw6tBYecYexU0VNc1WFLc9zJkayOx1COKPkO0PuC4vm3ImqL0f8IpbjYnsUqXIbDkhuvKXANRn0AarEhq6x3JMPq_JXfIi5InSykhiwssfQ6Z-eTBn8P4tgA5vqdLv2_sUQOjPM-mhKHD3Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موقعیت خوب برای استقلال که سحرخیزان توپ را به بیرون زد  @Farsna</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/462112" target="_blank">📅 22:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462111">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/980fe41e1d.mp4?token=aACrFqoFSAjjZHAFLAkUIrPRhVek7bGW_pwRecGVBxBH_5Gk1LBpSblfr5Vx76HYhnaHy7wMCdCehOLqYFXIBS0zvgtzrKf3J7IIffA4rGNjecisR9UMfaU-aqNo_wlFRnGYqR-G3M62AgUPAQkvk5-0QY3kypkJ3QNKH0mrzcqigPddqbpejCMRzMD0bvJ06G9-W9fJyGmhtcJBKdljzBDJye5jH8vsHBtIkb54Bx8eSNuY8klj8c4AMWxqC7bPNEcs4hUdfSS3QcxCI-0ADDi4zdrXt5ioockRAKYqI3gOkHPGPHJLAh7u9sHbO9zdOnzqC4ncjW0ewpdiVbXPGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/980fe41e1d.mp4?token=aACrFqoFSAjjZHAFLAkUIrPRhVek7bGW_pwRecGVBxBH_5Gk1LBpSblfr5Vx76HYhnaHy7wMCdCehOLqYFXIBS0zvgtzrKf3J7IIffA4rGNjecisR9UMfaU-aqNo_wlFRnGYqR-G3M62AgUPAQkvk5-0QY3kypkJ3QNKH0mrzcqigPddqbpejCMRzMD0bvJ06G9-W9fJyGmhtcJBKdljzBDJye5jH8vsHBtIkb54Bx8eSNuY8klj8c4AMWxqC7bPNEcs4hUdfSS3QcxCI-0ADDi4zdrXt5ioockRAKYqI3gOkHPGPHJLAh7u9sHbO9zdOnzqC4ncjW0ewpdiVbXPGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: نه حزب‌الله، نه حماس و نه ما آغازگر جنگ با آمریکا و اسرائیل نبودیم
🔹
با محاصره و تحریم نمی‌توانند ایران را وادار به تسلیم کنند. @Farsna</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/462111" target="_blank">📅 22:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462110">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4yH7oGCvPgzsi2RIG5GMxDVrzyD6yyLdGIUsuAvMiaXMXCIj7B10pL33Upzm2rB5-aP2l6BQK8IEFogs8BOz5NqSiIccGmobIjzo6F-IUBlx__y3R1_WwYPZdaIRSv4aOWlQ_OP8CA_RSDML2TFaL8o9eN1o6R1vSLNRdf-VvB_Mv27bkOrgEKGNr3d-07ABzYU9JO4ZnKMezMV397EENWuLlCmWaqym7Wnfl-weluu9Cdke0ZfxWbe0sgzWP6V_3hqyGI5m06y-23pvrAUJz0VT4ioLxB9_0O6dDn9cV083yNsGnx8GBfSzw7UIco5yBsL5WxkdlKvo2LPEYUs6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان در تنگنای یمن؛ گزینه‌های اندک، هزینه‌های سنگین
🔹
شبکه خبری سی‌ان‌ان: این هفته، جنبش انصارالله جزیرهٔ راهبردی پریم در دهانهٔ دریای سرخ را به همراه شهر بندری موکا تصرف کردند و به دنبال کنترل تنگهٔ باب‌المندب، یکی از مسیرهای کلیدی انرژی جهان، هستند. …</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/462110" target="_blank">📅 22:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462109">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dce738851.mp4?token=gm8yul8LnFMBFWPVTtiK8Bj3xDuhPoaItjkGDRDZagYwDEnnIVuPmhG4wsVCz09qyvJpJfOruFQmAb-IiyHFWWr1RuFrILvXsVNu1C6E0W_U1UJfhhlXShV--SKDelw-UVnnYyx0cVwNDL7HuMllunHC1Jg2VswMUCss3NZy2M2ro4XakcptH-9doXdf4Fws3rqLckTIp1wWPQMTbzsOr_y-zn918DZILt42QhVyI6s_amjV0qjEABilxfm-869IYWRww-5KwUvMxNw1oFZZDn8eB2GTqM1IDt2lPIj6DeCSI9E8ewtnoea0sRuuM2LiwiwxotwfeLPQcDoF6DrCWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dce738851.mp4?token=gm8yul8LnFMBFWPVTtiK8Bj3xDuhPoaItjkGDRDZagYwDEnnIVuPmhG4wsVCz09qyvJpJfOruFQmAb-IiyHFWWr1RuFrILvXsVNu1C6E0W_U1UJfhhlXShV--SKDelw-UVnnYyx0cVwNDL7HuMllunHC1Jg2VswMUCss3NZy2M2ro4XakcptH-9doXdf4Fws3rqLckTIp1wWPQMTbzsOr_y-zn918DZILt42QhVyI6s_amjV0qjEABilxfm-869IYWRww-5KwUvMxNw1oFZZDn8eB2GTqM1IDt2lPIj6DeCSI9E8ewtnoea0sRuuM2LiwiwxotwfeLPQcDoF6DrCWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: دلخوری کشورهای منطقه از حملات ما به آنها غیرمنطقی است
🔹
آن‌ها اجازه دادند دشمن از خاکشان به ما حمله کند و مردم بی‌گناه ما را شهید کند آنوقت توقع دارند ما واکنشی نداشته باشیم؟ @Farsna</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/462109" target="_blank">📅 22:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462108">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
خبرگزاری لبنان: ارتش رژیم صهیونیستی یک مدرسه در شهرک کفرتبنیت در جنوب لبنان را تخریب کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/462108" target="_blank">📅 22:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462107">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47f45f42be.mp4?token=b2BME40WcHeRA98mqOQLAHe8dSQG36gcHIWSfchWJzYGeOIL_jG9xzpUEq51gino4zeFssEjLz0asgbukwc95mS9vbrMiLdlMC68Pw0yagLYe7hPmOmXtYmkGTwacNMNJBqP-gpcPtRTv5T5clm3dhGp5_6X4iDLtc1Rbc4jKebkPF_sgi1XAsVbqnSPLmv91XW0al1kCCiR0Nvbo2fXE_4Ww9d56Qgl-TzIOGrscpFn0BTP_pQYdCyYwimdal3DIJlfc4HzWP52sJx2gTqCOvDUvV4mXhQuQoUHsWKrq98W0WqzdkVdJQaEkBek0FGaurNEoTge8ntIlFyklGUevA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47f45f42be.mp4?token=b2BME40WcHeRA98mqOQLAHe8dSQG36gcHIWSfchWJzYGeOIL_jG9xzpUEq51gino4zeFssEjLz0asgbukwc95mS9vbrMiLdlMC68Pw0yagLYe7hPmOmXtYmkGTwacNMNJBqP-gpcPtRTv5T5clm3dhGp5_6X4iDLtc1Rbc4jKebkPF_sgi1XAsVbqnSPLmv91XW0al1kCCiR0Nvbo2fXE_4Ww9d56Qgl-TzIOGrscpFn0BTP_pQYdCyYwimdal3DIJlfc4HzWP52sJx2gTqCOvDUvV4mXhQuQoUHsWKrq98W0WqzdkVdJQaEkBek0FGaurNEoTge8ntIlFyklGUevA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: رهبر شهید در قلب مردم ایران بود و برای ما سخت است که با آمریکا تفاهم کنیم
🔹
آن‌ها از اول انقلاب به دنبال سرنگونی ما بودند و باید اعتماد ما را جلب کنند. @Farsna</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/462107" target="_blank">📅 22:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462106">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ef922ebc.mp4?token=jESy7qMix299Q5ayal3iqDOnXvtQsZ0eVVFveuEFejeBDE9NTvQkoEvnBVvY4oUPq7r9b6bN9txu-R9-MAVDHxDoMhScAhkEW1buH28G586xAXFU13RYSLzptSWUyioIqQAZPWAfXSxMGAUC_l3_TmtCWi0uehgtNw9uV9WhYvxSDzC3W5aeJSOdYsnjviAXBrk5qTVXpeDLxqhQwRbpjO04PjYOwACYagH7lC1ESppe4WZJil-3j48cgbNRh06QR7e7DeVpDYWY8eT6RXWPeVPi6HrXe0opBcdEIynC3nt_iuTkezESgkTsSgFGYr2NalzEN5oGZF3sBUD89cboaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ef922ebc.mp4?token=jESy7qMix299Q5ayal3iqDOnXvtQsZ0eVVFveuEFejeBDE9NTvQkoEvnBVvY4oUPq7r9b6bN9txu-R9-MAVDHxDoMhScAhkEW1buH28G586xAXFU13RYSLzptSWUyioIqQAZPWAfXSxMGAUC_l3_TmtCWi0uehgtNw9uV9WhYvxSDzC3W5aeJSOdYsnjviAXBrk5qTVXpeDLxqhQwRbpjO04PjYOwACYagH7lC1ESppe4WZJil-3j48cgbNRh06QR7e7DeVpDYWY8eT6RXWPeVPi6HrXe0opBcdEIynC3nt_iuTkezESgkTsSgFGYr2NalzEN5oGZF3sBUD89cboaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: آمریکا چون نمی‌تواند رهبر ما را پیدا کند، درباره سلامتی او شایعه می‌سازد
🔹
رهبر انقلاب در سلامت کامل هستند و تصمیم آخر را ایشان می‌گیرند. @Farsna</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/462106" target="_blank">📅 22:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462105">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aea3f8962.mp4?token=k6Pho_yOsyuTvXxQdJ7jTgARpHXxv_HyQfkN3ltUMvkr-HjC2-4SR2lZNA7J2Jep08Q3s1KFSbIwLsSt49WnBFRAH3c0FeIjgpbfV-P5fi0L-0pL9vfbUEv2FTGwDZffyAEgy_E_PkCEOrsYwtRSVVBEMSbhNyZ678BFyH0Rsg_BO2nN39Wom9VoP-Mtn2mYelsBeGLZtVi6RJhGXJDE26UFR0cLiavUMmKYVdkPf99WcrngXPo29MuMhzqXjpyqA5J0c6eqHE5v09oNHBcPXsH3epWlnMxdlt1C80vFczHqB63y_LoHJb8nzhvf9qBzu-fulSEH_Lmc0oxcbCnw-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aea3f8962.mp4?token=k6Pho_yOsyuTvXxQdJ7jTgARpHXxv_HyQfkN3ltUMvkr-HjC2-4SR2lZNA7J2Jep08Q3s1KFSbIwLsSt49WnBFRAH3c0FeIjgpbfV-P5fi0L-0pL9vfbUEv2FTGwDZffyAEgy_E_PkCEOrsYwtRSVVBEMSbhNyZ678BFyH0Rsg_BO2nN39Wom9VoP-Mtn2mYelsBeGLZtVi6RJhGXJDE26UFR0cLiavUMmKYVdkPf99WcrngXPo29MuMhzqXjpyqA5J0c6eqHE5v09oNHBcPXsH3epWlnMxdlt1C80vFczHqB63y_LoHJb8nzhvf9qBzu-fulSEH_Lmc0oxcbCnw-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: تفاهم‌نامه ایران و آمریکا چه مشکلی دارد که بخواهیم دوباره مذاکره کنیم؟
🔹
خواسته‌های ما همان خواسته‌های قبلی است. @Farsna</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/462105" target="_blank">📅 22:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462104">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c779575c9.mp4?token=E7wAP0yvEgk8AXFmKKYhevrE6Qy8NQU4fFMg5j7DRHUoUP2CVPds4We1TdQRi2n8yDoBY9rb_QdW5vPyXPcW6Pf6og4Hb5FnMpunMA9qquBf7DmS78LiwM3ZaF3Y3Fk-UAcXjK4vPn0Dlu6YeXysADldi0hhJTO6xvMti7GlhtiPcy6Nu4uD0XSWDrCPTkhZDvos0TNMuV2m9vSLpPMfjAlicyAU6ZF3dmwS6ztrp_S77Nx1NZLla_45EoLwsIUsL_4RumChFIhtFWkA5ZGQ5LEP5_MTUc9AOzv20cqa3iVE5SrNAfqDYh1xy-klfxaN7Mr_tJvyAdT0WRwnH62-wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c779575c9.mp4?token=E7wAP0yvEgk8AXFmKKYhevrE6Qy8NQU4fFMg5j7DRHUoUP2CVPds4We1TdQRi2n8yDoBY9rb_QdW5vPyXPcW6Pf6og4Hb5FnMpunMA9qquBf7DmS78LiwM3ZaF3Y3Fk-UAcXjK4vPn0Dlu6YeXysADldi0hhJTO6xvMti7GlhtiPcy6Nu4uD0XSWDrCPTkhZDvos0TNMuV2m9vSLpPMfjAlicyAU6ZF3dmwS6ztrp_S77Nx1NZLla_45EoLwsIUsL_4RumChFIhtFWkA5ZGQ5LEP5_MTUc9AOzv20cqa3iVE5SrNAfqDYh1xy-klfxaN7Mr_tJvyAdT0WRwnH62-wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: چگونه می‌توانیم با آمریکا مذاکره کنیم، در حالی که آنها هیچ وقت به تعهدات خود پایبند نبودند؟!  @Farsna</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/462104" target="_blank">📅 22:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462103">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea280d0891.mp4?token=GKtK-froIqPe7d4P29BGAtxY8stxdjL9EAlik5XQExwaj-vP4bOU4ybpU53u8kyzqdaor3ejqIkxEZtppS342m6ZpMkECZxqhYWlcqUFcznHC_bAwKzVgs0WUtQMmrV_dbp44Znj9VblsDAaQ92xM5EgE4sl0SePq1-InchoRFxweDl9d_UtVTr6JqIOnvQr3xVIMP9YxRqFQ9MP3Jt4Bn7KloCk_yXAZKFwXZQ9Gf_cP6kwT0dbOKkMHzSkSvoEV-dOpnc3C8yKA8xLXjsjWuafSKE4WpJPrETJtYBxAnpwETgij2SYvmM6kR7wXiznTbE4mnOnExAeXCgILAI9Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea280d0891.mp4?token=GKtK-froIqPe7d4P29BGAtxY8stxdjL9EAlik5XQExwaj-vP4bOU4ybpU53u8kyzqdaor3ejqIkxEZtppS342m6ZpMkECZxqhYWlcqUFcznHC_bAwKzVgs0WUtQMmrV_dbp44Znj9VblsDAaQ92xM5EgE4sl0SePq1-InchoRFxweDl9d_UtVTr6JqIOnvQr3xVIMP9YxRqFQ9MP3Jt4Bn7KloCk_yXAZKFwXZQ9Gf_cP6kwT0dbOKkMHzSkSvoEV-dOpnc3C8yKA8xLXjsjWuafSKE4WpJPrETJtYBxAnpwETgij2SYvmM6kR7wXiznTbE4mnOnExAeXCgILAI9Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: اینکه ایران دنبال سلاح هسته‌ای است، مثل بقیه ادعاهای آمریکا دروغ است
🔹
این ادعاها بهانه‌ای برای حمله به ایران است؛ رهبر شهید ما بارها اعلام کرده بود که ما دنبال سلاح هسته‌ای نیستیم. @Farsna</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/462103" target="_blank">📅 22:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462102">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c02f54044.mp4?token=DvCIUVg8CUy81UPHjjJaLvzSQ0bpgrhA2bz0pOKLZU0XsdDcOlyAb5-GQg1dSmxoEWpyKmmCjd51MV7ZV6B8S1cMCTevrY6iqnb4S3f9aRZ45oOkcFA8PgYmVhp3pRGZj-FdwUJJZ94MB43Kn4VLrkj6us5xLxZK0aQsn8v5UppbPsznfRg7Y6_I-c4423Ds1t8j79hRERkYNPCSg6DFzSMObWcHmSoxOzSiEpkxM7vubcApDTQOBrswZDx14xezaUVBxlyHKLvav4IV3R25u2B5tZZ_dIsPZPSXwIUHug4yHNHZ8z0zyYqxJtR3yfJD3j9YWovPBIww32Y3n3YgHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c02f54044.mp4?token=DvCIUVg8CUy81UPHjjJaLvzSQ0bpgrhA2bz0pOKLZU0XsdDcOlyAb5-GQg1dSmxoEWpyKmmCjd51MV7ZV6B8S1cMCTevrY6iqnb4S3f9aRZ45oOkcFA8PgYmVhp3pRGZj-FdwUJJZ94MB43Kn4VLrkj6us5xLxZK0aQsn8v5UppbPsznfRg7Y6_I-c4423Ds1t8j79hRERkYNPCSg6DFzSMObWcHmSoxOzSiEpkxM7vubcApDTQOBrswZDx14xezaUVBxlyHKLvav4IV3R25u2B5tZZ_dIsPZPSXwIUHug4yHNHZ8z0zyYqxJtR3yfJD3j9YWovPBIww32Y3n3YgHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: مردم ما بعد از حملۀ آمریکا به ایران متحدتر شدند
🔹
مردم منطقه از آمریکا متنفرتر شدند. @Farsna</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/462102" target="_blank">📅 22:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462101">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57740b849d.mp4?token=hEw3rZw3mmMFMq6hHQTGHwA7i0tSpNsQXpq0OKqVIdshAD_rK4xyfusflOYsyXCSNqnsliFyc8fTgu9XuSufY3D7ti2iwC9agoW7JcXvaEal0P19ralFJPdoOX5x7oRnQTAjxQIjN7MsHyuFAKL8Xi4fysU8YXEAYapyXxeufLabizf8RmFtTTBBfCXZVsup7c9S0qsAYj7reua1mu6Qxjiu6zPIiI_5O1rfvoPXYNarKJgcuO_RdFkOLiBD-8dGIfPiGAqkPIJuMoxskRAjvVhAHoGoPclPM1Bi_UBnBc42LV3AIU9RdTcPXPXboE_5IotJyv0dpxl69p2v1-xy-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57740b849d.mp4?token=hEw3rZw3mmMFMq6hHQTGHwA7i0tSpNsQXpq0OKqVIdshAD_rK4xyfusflOYsyXCSNqnsliFyc8fTgu9XuSufY3D7ti2iwC9agoW7JcXvaEal0P19ralFJPdoOX5x7oRnQTAjxQIjN7MsHyuFAKL8Xi4fysU8YXEAYapyXxeufLabizf8RmFtTTBBfCXZVsup7c9S0qsAYj7reua1mu6Qxjiu6zPIiI_5O1rfvoPXYNarKJgcuO_RdFkOLiBD-8dGIfPiGAqkPIJuMoxskRAjvVhAHoGoPclPM1Bi_UBnBc42LV3AIU9RdTcPXPXboE_5IotJyv0dpxl69p2v1-xy-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: ما با کشورهای منطقه مشکل نداریم بلکه با پایگاه‌های آمریکا مشکل داریم
🔹
آمریکا هم پول نفت را می‌گیرد و هم کشورها را به جان هم می‌اندازد. @Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/462101" target="_blank">📅 22:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462100">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/028c0dfdbc.mp4?token=HsVyr6LlgOs_B-B_NujYjxPMOtisvoyb638SW-99ZvDWlFjhKbkzz7sfzNpwMk49mIaGMU4DZp3bHs-crrAfuKQ3I6Av70TL_1Dta0auN9Pe7Dm-lj7P5L9Hy_nsVHBAgWGtGOclAtq0DPeVv3ONSS6dACCOe65qYBDCSW54QHb7XRba343C370dzNnZVevbuteEW8CT0SXz2Mzoi_TMI_vQLrjKCqGS9BV9NzaSRGyFSOAMmb0E0svVeSqcuEQKiaBrGTUD24n60xeDnK5WzEi4-cIeSBwQbJ-HkPf_iceHmSNsR7fb0BxaUv9hEKNqurVu29FYJ4vD_zNll12SDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/028c0dfdbc.mp4?token=HsVyr6LlgOs_B-B_NujYjxPMOtisvoyb638SW-99ZvDWlFjhKbkzz7sfzNpwMk49mIaGMU4DZp3bHs-crrAfuKQ3I6Av70TL_1Dta0auN9Pe7Dm-lj7P5L9Hy_nsVHBAgWGtGOclAtq0DPeVv3ONSS6dACCOe65qYBDCSW54QHb7XRba343C370dzNnZVevbuteEW8CT0SXz2Mzoi_TMI_vQLrjKCqGS9BV9NzaSRGyFSOAMmb0E0svVeSqcuEQKiaBrGTUD24n60xeDnK5WzEi4-cIeSBwQbJ-HkPf_iceHmSNsR7fb0BxaUv9hEKNqurVu29FYJ4vD_zNll12SDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: ارتباط ما با نخست‌وزیر هند روزبه‌روز بهتر می‌شود
🔹
در تلاشیم بر پایه فرهنگ و رابطه دیرینۀ ۲ کشور، مقابل تمامیت‌خواهی بایستیم. @Farsna</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/462100" target="_blank">📅 22:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462099">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01bebc1764.mp4?token=PNUEiFTam6cgF-q__6wnAAZjFu1UupqVzTFZDj290YhZwXLCF-iezco5GPAJS_rmp_wSQzuoAdpYgnv59KfobvdUBrLIso7kP1MeLM4KL-A51PuX_aprnWZDEwhnGcIjy9GJIDVvlXdrUA9bwboSt8lJcWBtlxAqYGHkqyyfjSDwNEFs06n6K7vT44RcSEyvC3SW_KnGUUKs3S3t0JDCxF5b9qrPLC2dl6WIIMXuOBRfDJgYstgXAqgq3_xIWIJkQSv_xgQS3R8RJIR3o8EcvLoswHhLPYuyKP8ws_fZw77wh6uitebvw6_NCXIwjeLNVnFv0mVWsyePo49b9rddRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01bebc1764.mp4?token=PNUEiFTam6cgF-q__6wnAAZjFu1UupqVzTFZDj290YhZwXLCF-iezco5GPAJS_rmp_wSQzuoAdpYgnv59KfobvdUBrLIso7kP1MeLM4KL-A51PuX_aprnWZDEwhnGcIjy9GJIDVvlXdrUA9bwboSt8lJcWBtlxAqYGHkqyyfjSDwNEFs06n6K7vT44RcSEyvC3SW_KnGUUKs3S3t0JDCxF5b9qrPLC2dl6WIIMXuOBRfDJgYstgXAqgq3_xIWIJkQSv_xgQS3R8RJIR3o8EcvLoswHhLPYuyKP8ws_fZw77wh6uitebvw6_NCXIwjeLNVnFv0mVWsyePo49b9rddRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: آمریکا با ادعای حقوق بشر پس از شکست نظامی و زدن زیرساخت‌ها، راه ورود دارو و غذا به ایران را بسته است
@Farsna</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/462099" target="_blank">📅 22:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462098">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb959d3636.mp4?token=INoTX3WVGKTEAyIX1-E7NRlVeZXB6ZfGHjSE8Io2dhqqhMCNbfZiJO0UkRFm6SnKlmy22Tgm9S8DnZaf8ChVc0PpkGtsGAzNXuIdR6Q02ZM6NwTBgZ7AXuHRWXgGNrWr-Cr4D_wCWcScrjjL-YYcmzGXakXayaIV1tZNt2249RQb4f-jZITWu0CA0aU5mIPFeDNo1EBeXNLiFDF9igz2SbMggQR2TjDW6TPApDRI1A9VGWHEceWpORIzn0dTZe5ln2NCDxxNfD_HWom0EAhqjs5cfi1pS_2jftwE_M8ll7qDgLN8lrU6OnUYsuxtJABlb6nEvepGZ5PTK2orkJFGqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb959d3636.mp4?token=INoTX3WVGKTEAyIX1-E7NRlVeZXB6ZfGHjSE8Io2dhqqhMCNbfZiJO0UkRFm6SnKlmy22Tgm9S8DnZaf8ChVc0PpkGtsGAzNXuIdR6Q02ZM6NwTBgZ7AXuHRWXgGNrWr-Cr4D_wCWcScrjjL-YYcmzGXakXayaIV1tZNt2249RQb4f-jZITWu0CA0aU5mIPFeDNo1EBeXNLiFDF9igz2SbMggQR2TjDW6TPApDRI1A9VGWHEceWpORIzn0dTZe5ln2NCDxxNfD_HWom0EAhqjs5cfi1pS_2jftwE_M8ll7qDgLN8lrU6OnUYsuxtJABlb6nEvepGZ5PTK2orkJFGqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شوت دیدنی رزاقی‌نیا با واکنش دروازه‌بان السد راهی کرنر شد  @Farsna</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/462098" target="_blank">📅 22:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462097">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc6f43ecde.mp4?token=FUt7arLwc2eZPz6JdWiLkUhx0fnw75TDSTcBmWuVXLhaptIIrNv49dMi3Mbjw1Ju7sPEHkNNWmr53iWZh5bFD8BM1tvwxjUgje_4GX3VYck6E3_cCaN8ZthvAa9X6BuRYXsZ7EVpjA_Y9ekaYbYM6S8shfDVs3-eXxCkeu9XwXmJKfMZXgqy2x-4KtIEdIkwBeTH9Mw9FVucg2CE1CcssWOpgRboCh_Yz-xWDmN5d11brbfcMRcdZ-qB5bKJ3ZdwrZeSXM_Hibm_zTgsAfTNEE9kENi-WIkDCHOTPDRby1NUJAAI-RMO1SOvNQqpxUPPF0NNl7dVl4TOTIqxwjK51TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc6f43ecde.mp4?token=FUt7arLwc2eZPz6JdWiLkUhx0fnw75TDSTcBmWuVXLhaptIIrNv49dMi3Mbjw1Ju7sPEHkNNWmr53iWZh5bFD8BM1tvwxjUgje_4GX3VYck6E3_cCaN8ZthvAa9X6BuRYXsZ7EVpjA_Y9ekaYbYM6S8shfDVs3-eXxCkeu9XwXmJKfMZXgqy2x-4KtIEdIkwBeTH9Mw9FVucg2CE1CcssWOpgRboCh_Yz-xWDmN5d11brbfcMRcdZ-qB5bKJ3ZdwrZeSXM_Hibm_zTgsAfTNEE9kENi-WIkDCHOTPDRby1NUJAAI-RMO1SOvNQqpxUPPF0NNl7dVl4TOTIqxwjK51TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شگفتی شبکه دولتی فرانسه از سیل مردمی ثبت‌نام کننده در پویش جان‌فدا
🔹
شبکه دولتی فرانسه اعلام کرد هر روز که می‌گذرد مردم ایران نسبت به آمریکا و اسرائیل بیشتر منزجر و حول حاکمیت بسیج می‌شوند؛ گواه آن آمار بیش از ۱۴ میلیونی پویش «جان‌فدا» است.
🔹
پویش جانفدا در پایان کار خود به بیش از ۳۰ میلیون داوطلب رسید.
@Farsna</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/462097" target="_blank">📅 22:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462096">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6277c9b4b5.mp4?token=mzkEnaI8oOfYf5N5hfPnu4a8KYFq-kiYGAiWpTdjvTCgm8-uw2c-vzGN8coZoc1RDQHS86Ettr_kaHqvG6bgUY3bCfEQR0n5wpa0s0P61bDYx7SDgkBHDK2gGETyDw9lUK5lDs6B0XJywYRhGd0f0b67aT-d8EBh5NmLHSKG8AfrFyQBmQ8tmNh_T7vyUDUR1sh5NhwmsdnMUr6k1sIuk9KXTrdv56Z04eAHn_DyKG4P2t2xBx_8WMPx12Ygb-vrEpEZs77JmuGb2OYbYB34wUACC737v4sqLgEW0X-KCUlkaIz8PfpPIk1w9rjJCNKhLJipT-Qw4WpXxFWABb--PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6277c9b4b5.mp4?token=mzkEnaI8oOfYf5N5hfPnu4a8KYFq-kiYGAiWpTdjvTCgm8-uw2c-vzGN8coZoc1RDQHS86Ettr_kaHqvG6bgUY3bCfEQR0n5wpa0s0P61bDYx7SDgkBHDK2gGETyDw9lUK5lDs6B0XJywYRhGd0f0b67aT-d8EBh5NmLHSKG8AfrFyQBmQ8tmNh_T7vyUDUR1sh5NhwmsdnMUr6k1sIuk9KXTrdv56Z04eAHn_DyKG4P2t2xBx_8WMPx12Ygb-vrEpEZs77JmuGb2OYbYB34wUACC737v4sqLgEW0X-KCUlkaIz8PfpPIk1w9rjJCNKhLJipT-Qw4WpXxFWABb--PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تماشاگران استقلال در بصرۀ عراق بی‌وقفه تیم خود را تشویق می‌‌کنند  @Farsna</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/462096" target="_blank">📅 22:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462095">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZASH96lO8HtUNvTyXbZhjMqAUbu0Pj0V5Cuh_AsAKv3RD4cMqUrPNBV6-Y9tfvDVO8qZ4RwZWXlV-IK_nrIWCYcJ-aH01qYwsw55p_qHLdvwRBwAAfKs2qPms_uqtxipc01KKVp0W8amxf8CRXkMtZGLWiStaAEoU9crL9ikYQl_nPkyQJG-RP38aXvxS8T1T7sqxZFIX40pUqxYmJUT1Us5T_Ged_-CCnFeHgsu9jSwKXhgiN3QGQdEk2J5QkyD8qKOUPJgKVVNbNMH4jFec7vSkxhLif4bIod8zVoSXH3iYd_MmNMMoMspep0XoRguuZslDdIT4FdagTqTJ1Otng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
برخورد یک سوپرنفتکش متخلف به مین‌های ایرانی تنگۀ هرمز
🔹
نیروی دریایی سپاه: سوپر نفتکش «الگایا» به شماره دریانوردی 9325336 که قصد عبور از منطقۀ ممنوعه در جنوب تنگه هرمز را داشت، بر اثر برخورد با مین‌های دریایی منفجر شد؛ تلاش برای مهار آتش بی نتیجه بوده و کل نفتکش در شعله‌های آتش گرفتار شده است.
🔹
پیش از این نسبت به خطرناک بودن معبر غیر قانونی هشدار داده شده بود، نیروی دریایی سپاه با قاطعیت اعلام می کند تنگه هرمز مسدود و همچنان تحت کنترل هوشمند ما می باشد.
@Farsna</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/462095" target="_blank">📅 22:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462094">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cca582c11a.mp4?token=HywflNyg-P8x9AhWr0cifm2GbG0fWsh1swdkx7heQi4WxQz2geXt9af4NQ93KkXsGH_gDJjNOC6ClGvk8xCmtRMpRWjDsc-ipcekOyIqEHCSmuOc1KoRNIqugpV44LdXxIPelzry1OuZxvN8iMPHSlPirzhjmbUoWGIHZ-WX12iU9cfXVlyRMzeQS8elW12HzvlcB69y25OO9r37n_Pa3MUkPc82g4YfFb49p5SFbUjfIwhuyiNyzdAOAi1YNM-3_7p1Lb3_wflZCQPNEmc4jOMx10pyAI9MB9AL9ioGJtGkzvbGGVZuOt8WWyHc-OkBBWt0WvKuBX329qoxjIPTlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cca582c11a.mp4?token=HywflNyg-P8x9AhWr0cifm2GbG0fWsh1swdkx7heQi4WxQz2geXt9af4NQ93KkXsGH_gDJjNOC6ClGvk8xCmtRMpRWjDsc-ipcekOyIqEHCSmuOc1KoRNIqugpV44LdXxIPelzry1OuZxvN8iMPHSlPirzhjmbUoWGIHZ-WX12iU9cfXVlyRMzeQS8elW12HzvlcB69y25OO9r37n_Pa3MUkPc82g4YfFb49p5SFbUjfIwhuyiNyzdAOAi1YNM-3_7p1Lb3_wflZCQPNEmc4jOMx10pyAI9MB9AL9ioGJtGkzvbGGVZuOt8WWyHc-OkBBWt0WvKuBX329qoxjIPTlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: ارتباط ما با نخست‌وزیر هند روزبه‌روز بهتر می‌شود
🔹
در تلاشیم بر پایه فرهنگ و رابطه دیرینۀ ۲ کشور، مقابل تمامیت‌خواهی بایستیم.
@Farsna</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/462094" target="_blank">📅 22:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462093">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9597355cae.mp4?token=ppX7pjQU4mBfyJ7m6UWMgwq2u2CKyMFTdhIMeQe0UcEsZcpdRU1kYh6qhJISBcq3s0zp1ht3dJPhLRaSIdYNYTBk4yfPasT5l1-3kqBpTRrhnfB625XAx2Pe58qXX2oOpCDxJxhRSpye3Vvodp9uxHPwB44Cv43xM9KXwoG_s7mKtuJybaRC7ThZ_Iv6YELYDHfBP5to5kPRhT3sGKOknYCV6ymfXrTPa3BfeTAy5lg3HOPoJHF_clyJTL3Fi1I7loN_mBrT6r9QdVe_j_gc91P1k6COMVk3QAhXsZTSiHDPRS9Y8CNKvMi-VDRVn1fBoRClP-JRMETceprvAnnhkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9597355cae.mp4?token=ppX7pjQU4mBfyJ7m6UWMgwq2u2CKyMFTdhIMeQe0UcEsZcpdRU1kYh6qhJISBcq3s0zp1ht3dJPhLRaSIdYNYTBk4yfPasT5l1-3kqBpTRrhnfB625XAx2Pe58qXX2oOpCDxJxhRSpye3Vvodp9uxHPwB44Cv43xM9KXwoG_s7mKtuJybaRC7ThZ_Iv6YELYDHfBP5to5kPRhT3sGKOknYCV6ymfXrTPa3BfeTAy5lg3HOPoJHF_clyJTL3Fi1I7loN_mBrT6r9QdVe_j_gc91P1k6COMVk3QAhXsZTSiHDPRS9Y8CNKvMi-VDRVn1fBoRClP-JRMETceprvAnnhkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول استقلال به السد توسط آسانی
⚽️
استقلال ایران ۱ - ۰ السد قطر @Farsna</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/462093" target="_blank">📅 22:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462092">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
الجزیره: وزارت خزانه‌داری آمریکا یک بانک روسی را به‌دلیل همکاری با ایران تحریم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/462092" target="_blank">📅 22:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462091">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
منابع عربی از فعال‌شدن آژیرهای هشدار درپی حملۀ موشکی انصارالله یمن به منطقۀ نجران در عربستان سعودی خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/462091" target="_blank">📅 22:20 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462090">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-dOgtuA7O4pahgKIJLQPn_8mVoMIif9Mq94czljxcJuh-BS-6OcFFr_f-jbAqCJzZVIYfdPqEqGX7DWvyJNGesDLbfQZeb5sX0j_uBw9gzAtKOe13caCDhFm-9Vmrqf9FpdBH10oLizDZk-9V9ojxN9oVoe98TdNbqtemZW4xgGkm314Zy-yeUSOLrq3KHvgU-fkDCz8OCJp7vVMPbGS23wKGaq-GwNZ8UxhFmR5nsf-fTuNRB1EX6vkSRYWxn3PYcDM0U_0K2pCFeRpJDxnoc_BHe2CE7sZXcMh3TXgbFdbSPTw-iNTvQgyyNsDA5PpdZ5xCVdz1GWB3pY9nCuSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه شد که پس از ۶ ماه، مصاحبۀ جنجالی خلبان آمریکایی منتشر شد؟
🔹
روز گذشته، شبکه آمریکایی «CBS» در مستندی مدعی شد با خلبان جنگنده‌ای که در ایران بود، مصاحبه کرده است؛ یکی از بخش‌هایی که در این مصاحبه مورد توجه کاربران خارجی قرار گرفت، این است که فرد مصاحبه‌شونده می‌گوید با سرعتی بین ۱۱۰ تا ۱۶۰ کیلومتر بر ساعت سقوط کرده و بعد از شکستگی در کمر و چند نقطه، توانسته تا ارتفاع ۷۰۰۰ پایی فرار کند!
🔹
مصاحبه با خلبان ادعایی آمریکا، با تاخیر حدود ۶ ماه منتشر شده است. جدای از داستان عجیب و نسبتا تخیلی در این مصاحبه، انتشار آن در چنین زمانی، می‌تواند دو هدف را برای آمریکا و شخص ترامپ، در پی داشته باشد.
🔹
کلید اول حل مسئله، این است که داستان را از روزهای اوج جنگ ببینیم، نه صرفا روایت نجات. در طول جنگ ۴۰ روزه، ایران جنگنده‌های متعددی از انواع مختلف آن شامل F-15، F-35 و A-10 را هدف قرار داد. این در حالی بود که ایالات‌متحده مدعی نابودی کامل پدافند و تسلط بر آسمان ایران بود.
🔹
در ماجرای یکی از هواپیماهای هدف گرفته شده، اخباری مبنی بر سقوط دو خلبان آمریکایی در ایران منتشر شد؛ ایالات‌متحده نیز مدعی بود دو عملیات نجات برای فراری دادن این خلبان‌ها انجام داده که یک مورد آن، به طبس ۲ معروف شد.
🔹
در این عملیات، ایران بیش از ۸ پرنده آمریکایی را منهدم کرد و به تعبیر تحلیلگران «آمریکا برای نجات یک خلبان، یک اسکادران از دست داد.»
دو دلیل برای انتشار مصاحبه در زمان فعلی
🔸
آمریکا به روزهای انتخابات خود نزدیک شده و ترامپ نه‌فقط در میان دموکرات‌ها، بلکه در پایگاه اصلی جمهوری‌خواهان هم حمایت خود را از دست داده است. درنتیجه، برای احیای چهره شکست‌خورده خود، به هر ابزار کوچک و بزرگی چنگ میزند و یک مورد کوچک آن، قهرمان سازی از خلبانی بود که جنگنده فوق پیشرفته‌اش با پدافندی که ترامپ می‌گفت نابود شده، ساقط شد.
🔸
رسانه‌های آمریکایی سعی کردند از تکنیک «گذر زمان» استفاده کنند. به این معنی که امید داشتند با گذشت ۶ ماه از آن ماجرا و انبوهی از اتفاقات پرسرعت در این مدت، تصویر شکست اصلی در ذهن مخاطب کمرنگ شده و حال با ارائه یک تصویر قهرمانانه، بتوانند جایگاه خود را احیا کند.
🔹
حتی اگر فرض کنیم آمریکا، خلبان خود را نجات داده و شخص مصاحبه شونده همان خلبان است، صفر تا صد فرآیند ساقط شدن جنگنده، عملیات نجات و زمین‌گیر شدن نیروی هوایی ایالات‌متحده داخل خاک ایران، یک تصویر را ارائه می‌کند: «شکست قطعی ترامپ.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/462090" target="_blank">📅 22:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462089">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd8c4473cc.mp4?token=AhGjZ6MG-z7IeTRpdQYVNOYoTlWrDE6nCjSEEyp8Xy9UcA8y5yBHSeebKo7-NP5W67BRlTDvOV8ehqkfHxV7Osi6pehh23LSvnCS1IVXQvQMxT0BWOIj3s0ImVFBFMw9kTCBrY2I0TmSauC4B2BnAh65IrJ33_gYR-ZMBI2AVSiJ6VNVkedhIW8pWX17DdV7MRSd9IGoX4Bukwb0J77VJ6uoGBrlxJKyH8AGqX92PG8iP2fNgx5WYh6ixNK5wFpfnmaeHmm7BCI6ldZRpbJPjAMlkrnMW8gRzyWNwH3Hcl0LK2rjuEBIj8rE_-skg3KjR7B4EZIRlm3r2lY5_1bOeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd8c4473cc.mp4?token=AhGjZ6MG-z7IeTRpdQYVNOYoTlWrDE6nCjSEEyp8Xy9UcA8y5yBHSeebKo7-NP5W67BRlTDvOV8ehqkfHxV7Osi6pehh23LSvnCS1IVXQvQMxT0BWOIj3s0ImVFBFMw9kTCBrY2I0TmSauC4B2BnAh65IrJ33_gYR-ZMBI2AVSiJ6VNVkedhIW8pWX17DdV7MRSd9IGoX4Bukwb0J77VJ6uoGBrlxJKyH8AGqX92PG8iP2fNgx5WYh6ixNK5wFpfnmaeHmm7BCI6ldZRpbJPjAMlkrnMW8gRzyWNwH3Hcl0LK2rjuEBIj8rE_-skg3KjR7B4EZIRlm3r2lY5_1bOeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بالیوود آمریکایی
🔹
تصاویر دیده نشده از خلبان امریکایی که با سرعت ۱۶۰ کیلومتر در اصفهان سقوط کرده، زنده مانده و با بدنی شکسته از کوه بالا رفته است!
@Farsna</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/462089" target="_blank">📅 22:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462088">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
منابع عراقی از وقوع انفجار و آتش‌سوزی در منطقۀ شمامک در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/462088" target="_blank">📅 22:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462087">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🎥
پرچم ایران در قلب میدان انقلاب چهار محال‌و‌بختیاری چرخید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/462087" target="_blank">📅 22:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462086">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPpzBkVuWRnO18G6azM5uMMje6xRHw5Y6dlozhSB3EWLubkSDmnVY6JNzESFHvZyDHtlZZzMj0cx966-59-TwS3Whu1Pw3X8jVgqPaE_6nsgOa7VV3J2_bOZDLYd_H4zrgSF6hbE1YcgnW_vARkxstaJR9k4UfNMAEtN39QjsmPCM95A-EQbjTkKc-mW58YT_gM_P_G5VEiti36sKKNCuN5TIP75_PuLHRvx-HrPZN6DB5mBNV1zOaF_FGhrrZdZON9Cnja4x2K5iXxsWnpMqgdw-yI1TSsVRZPXzVOM2Tk0rECaVISj_K5YC5OCP7OYytrIvIKAszpPSRs4iA9Jvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس اتحادیۀ میهنی کردستان عراق به تهران می‌آید
🔹
سخنگوی وزارت خارجه اعلام کرد بافل طالبانی رئیس اتحادیۀ میهنی کردستان عراق سه‌شنبه به تهران می‌آید تا با مقامات ایرانی دربارۀ تقویت ثبات و همکاری‌‎های مرزی گفت‌وگو کند.
🔸
اتحادیۀ میهنی کردستان یکی از ۲ حزب اصلی در ساختار سیاسی کردستان عراق است.
@Farsna</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/462086" target="_blank">📅 22:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462085">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb252f09ef.mp4?token=UaWwiyOAPoFW4dptNWHIGRTklZpzs_-EgAcnRGuK4EvB37EYjHp7fscRgMTKSXdhVj8HMrokcuacyU9Vf864N3GWUI3jvE98_A2Qr5j53ltxfeApcAlH_VRWag_G8S7w1yIyrdL38M07UbFKnAuMtYkqyejeSLx-lazTFvJO32EfywNaNnfnZXTdlBL2kz8DQdKZmaLbIpVWfJLD55Z8rZuHzGWMxiN7bUsiRa4jKIj8uWoJwMHqGJh4L2Kp-XNaUGiVedamM0GKWZ7N0myIb8M0FfaRD2cfKzro8C_F9sQPSKhLMI2rXURmedk04d04A-hyDfChiIDy2RGcuaJiRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb252f09ef.mp4?token=UaWwiyOAPoFW4dptNWHIGRTklZpzs_-EgAcnRGuK4EvB37EYjHp7fscRgMTKSXdhVj8HMrokcuacyU9Vf864N3GWUI3jvE98_A2Qr5j53ltxfeApcAlH_VRWag_G8S7w1yIyrdL38M07UbFKnAuMtYkqyejeSLx-lazTFvJO32EfywNaNnfnZXTdlBL2kz8DQdKZmaLbIpVWfJLD55Z8rZuHzGWMxiN7bUsiRa4jKIj8uWoJwMHqGJh4L2Kp-XNaUGiVedamM0GKWZ7N0myIb8M0FfaRD2cfKzro8C_F9sQPSKhLMI2rXURmedk04d04A-hyDfChiIDy2RGcuaJiRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چراغ این خیابان‌ها ۱۹۸ شب خاموش نشده
است
@Farsna</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/462085" target="_blank">📅 21:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462084">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9555c33a5d.mp4?token=ema_XQdwC2Ii8TQjhxhubn3s4gyge8miYegO0Mjsenohp2iAXzOgMvN_lL37z2z_6jvXKpX7tzB-G-0_-KVjkrSr6lNUanlXXi3yrcoNa2G4KCOY0ZmIzCIEOwNtocpHNIv8uOgIB0N8YPiXVmWs7GUedlRG5ITlU0ioMR7HYxNxFVHGUK1ar8K8efOyy1vfyZ2ofm_Yaf0RdG83zmu1-fM5_d8fzk2h9BzStS5Igy1kO3poBDSxbbs6JM6AoMncS9EcWVvZKzOJWhXK8f-BKd4YPQAjCZvZnFstBe0fuC2v_2Z-cqFeCPO0K4sc29A3nrLg4NNxvWDX8BSzQU-pzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9555c33a5d.mp4?token=ema_XQdwC2Ii8TQjhxhubn3s4gyge8miYegO0Mjsenohp2iAXzOgMvN_lL37z2z_6jvXKpX7tzB-G-0_-KVjkrSr6lNUanlXXi3yrcoNa2G4KCOY0ZmIzCIEOwNtocpHNIv8uOgIB0N8YPiXVmWs7GUedlRG5ITlU0ioMR7HYxNxFVHGUK1ar8K8efOyy1vfyZ2ofm_Yaf0RdG83zmu1-fM5_d8fzk2h9BzStS5Igy1kO3poBDSxbbs6JM6AoMncS9EcWVvZKzOJWhXK8f-BKd4YPQAjCZvZnFstBe0fuC2v_2Z-cqFeCPO0K4sc29A3nrLg4NNxvWDX8BSzQU-pzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول استقلال به السد توسط آسانی
⚽️
استقلال ایران ۱ - ۰ السد قطر
@Farsna</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/462084" target="_blank">📅 21:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462082">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4NG3jzx3pg8YEs9kRLT7j95kCAEHZp8Yu4-fykPU3pWe8TQSJIGbMVEKxVgYsf-uRCqn78YBmYzfFYkYNVUjZg69q_ooroZWgB3onfrw13S2Tq8zE761AycVn4vV4W6Xk2bdAfgyoILevSVX_g05YX0gbO1WVk_J6M1sVFx-En0aDm4Y-IQXyGezu25HDZM22PBE_2DqNELsuGlj9EEEtagYIt70rBjc77CPxn-Ptr-kX16aCPHMndM9sAB7wTKnDpxW5XNj29GzPQdthTlfUXKeqUEr6zEZsonyAv8pDI_aIEhBS6eebAt2PkRULMAnvjGDgE7Ztr6eiFCzsQgcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
مسیر فرار نفت عربستان از هرمز در آتش سوخت
🔹
تصاویر ماهواره‌ای جدید یک ایستگاه پمپاژ متعلق به خط لولهٔ راهبردی عربستان سعودی موسوم به «شرق–غرب» را نشان می‌دهد که درپی حملهٔ پنجشنبهٔ گذشتهٔ یمن، به‌شدت آسیب دیده است.
🔸
این خط لوله حدود ۱۲۰۰ کیلومتر طول دارد…</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/462082" target="_blank">📅 21:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462081">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ef0e89bac.mp4?token=FlONqNMDnxPiuBtnaNGQJalJOfRA38n9BbyUfntFSs-WFo_25xsDKkp4ZJlGnQGM2T0uStdN85Iuds-xkzA9_h350_H9vYqZHCE_HD6SRFORd3nVxqhcWXNQZlyFAwkzJ9qCp68gMcuuzlLu2bA3xGHp93XOc-NTS_j7GRW4m2SYfOcR4JguC-Id6lMaSXtzej3I928nq8LLw7Jxzf2scE3DWO_Hl-vgKgKHdYv4UtkSo7p71iHjwu_BAEzsP0rBW_dnNrsHVigmBwLqOY9ujkEjeSAtlJ84xoNc3MjZ7d4tOTzXz_pqMpuwQx2JvCaGr1qr3DKM_vvDawoUaNrcow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ef0e89bac.mp4?token=FlONqNMDnxPiuBtnaNGQJalJOfRA38n9BbyUfntFSs-WFo_25xsDKkp4ZJlGnQGM2T0uStdN85Iuds-xkzA9_h350_H9vYqZHCE_HD6SRFORd3nVxqhcWXNQZlyFAwkzJ9qCp68gMcuuzlLu2bA3xGHp93XOc-NTS_j7GRW4m2SYfOcR4JguC-Id6lMaSXtzej3I928nq8LLw7Jxzf2scE3DWO_Hl-vgKgKHdYv4UtkSo7p71iHjwu_BAEzsP0rBW_dnNrsHVigmBwLqOY9ujkEjeSAtlJ84xoNc3MjZ7d4tOTzXz_pqMpuwQx2JvCaGr1qr3DKM_vvDawoUaNrcow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهید مظلوم اهل سنت، امروز چگونه به شهادت رسید؟
@Farsna</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/462081" target="_blank">📅 21:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462080">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QA7efWOk1O0bUK32SpgLm9o-g1tSv-uI6fPKpbXHut7glsk34N663GuXI3gSnF4eqa8tT9IXN9z2qXqOc1V2BqqpOGFuYHZSRRVQcSe4pEsa7SXvMvSAjdU3a-Z6Wcx3x0a3nKhrEwfp7ySTgYgBqbOE8H1myWqx2ue5IxnYv_5_zC5IVwKJg3AZaL0YketI32mIYP1fLzypReSZlyQXE_8AWOvVmm9ru7sE0RWHf5XTgO4WQOt34uUfP80qpdmZdCYsQxO3hBN0Js6qg8OGr-0-UEtrRmAR5qhr1U1LxcK3nefqyglCwgDe3Ny8Ezq5AFv3fvd0gqSQ0cws-wWQKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آمادگی مردمی تا آموزش؛ دوره‌های «جان‌فدا» آغاز می‌شود
🔹
دوره‌های آموزش نظامی و امدادی ویژه داوطلبان پویش مردمی «جان‌فدا» از سه‌شنبه ۲۵ شهریور آغاز خواهد شد.
🔹
داوطلبان برای شرکت در این دوره‌ها می‌توانند عدد ۱ را به شماره ۳۰۰۰۱۱۵۵ ارسال کنند و به سایت
JANFADAA.IR
مراجعه کنند.
@Farsna</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/462080" target="_blank">📅 21:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462079">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEF4HWmlGWiQLfG9Vs7LrIdpMBTRWiMfJzxN38HIRZ2E7IbQ037oDHVv1x60hntltmE0izRz1mnnF8-_-MWb_pED2huGFVieYUAOaZL5J6o5-BaxWDCNp4Mtap1x099K_zgi0fEtFAtyAchKFtEPwPW75-_724MxmJ2zVCET6vWwEuuMVDhYn0lNuubuc6iqaf1FT2_l4TdSqSQwRqX54wB2i6dBylz6N8yrd_uIW7I6BbtnIY7D0-AqQxpaLjXU_ygZwGTz3sD-au4LDYAYnADtz77ahRx_5o7odPq1lQUtkb5czIaZqJw5Tf6IdOxX5ZfGSNSbmhkaqW9zfRmAig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان خطاب به آمریکایی‌ها: حداقل مردانه بجنگید
🔹
آمریکایی‌ها دولت تروریستی تشکیل داده‌اند و هر کس را بخواهند ترور می‌کنند.
🔹
مدعیان حقوق بشر و انسانیت، اگر صادق هستید، چرا کودکان، بیمارستان‌ها و زیرساخت‌های مردم را هدف قرار می‌دهید؟
🔹
اگر مرد میدان هستید،…</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/farsna/462079" target="_blank">📅 21:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462078">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e1590b887.mp4?token=TSG_dNrih1EO9Qx6xnviAd3ba_pZmRwnS81v5m1Jwl0G4stxE-VwTl20scAeuzKZfK8vLZ5j45YFZjEsI5UC540aKz_AngN85QxerQGq5su_mLxGkdSp0-EUwXsYYEf3XLb1OvzzedPEvJNTCZSxWUZdFP_WyBdXegrxBbJE7CH8R-9jD4SzwLXiZsGAtVmiU6tzs1_10WAxB35250vtrJoV_4KIHBL7IPbQ1DiWfBAYAD6djNJIf7oRXndtzE2nOela1B3OyF3BHRjtWvpxxP3nY7OGcUl3MGDRDl9GUbMMJ9lRVnz3UNXnwAxxWNaoKCsOqPseok4Utq_oNAlwrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e1590b887.mp4?token=TSG_dNrih1EO9Qx6xnviAd3ba_pZmRwnS81v5m1Jwl0G4stxE-VwTl20scAeuzKZfK8vLZ5j45YFZjEsI5UC540aKz_AngN85QxerQGq5su_mLxGkdSp0-EUwXsYYEf3XLb1OvzzedPEvJNTCZSxWUZdFP_WyBdXegrxBbJE7CH8R-9jD4SzwLXiZsGAtVmiU6tzs1_10WAxB35250vtrJoV_4KIHBL7IPbQ1DiWfBAYAD6djNJIf7oRXndtzE2nOela1B3OyF3BHRjtWvpxxP3nY7OGcUl3MGDRDl9GUbMMJ9lRVnz3UNXnwAxxWNaoKCsOqPseok4Utq_oNAlwrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر تعاون: بازنشستگان می‌توانند طلای مورد نیاز ۳ ماه آینده خود را از سامانه بانک رفاه خریداری کنند؛ هزینه آن متناسب با میزان خرید از حقوق ماهانه‌شان کسر می‌شود و قیمت طلا تا ۳ ماه ثابت خواهد ماند.
@Farsna</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/462078" target="_blank">📅 21:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462076">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef043e7560.mp4?token=eHdh3YkS6xCPXqSSdcAD5qal24lTbJ-b2nhVpXCRmmbC1xmf1xJ5Ydze6HQ1i7HQ7NnXt-GsZObth4TtatoE0F-4sGkubBtiD3hPOEFv7kAG16TsUNIPxRq3AuK5TUa8u3KxtoBwoXNA4_BS1yfCjt79dguaQmkB3EojQg7AReorTSOybmmqgN4uP8mIm6qrAZhfyO__jWeO_ngDAUQVUMTwLVPsDDySP8s6tgF8wHvTJSGuPdNCii7wo2t7eCtrZa1oLVAioS3PB9e6FQltaCHbovp0Gq-nGWr0v0_Z2HarUYMrzwvhZxSZDJxCzbyRJ2VrRzo3RK1zVsCec65kTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef043e7560.mp4?token=eHdh3YkS6xCPXqSSdcAD5qal24lTbJ-b2nhVpXCRmmbC1xmf1xJ5Ydze6HQ1i7HQ7NnXt-GsZObth4TtatoE0F-4sGkubBtiD3hPOEFv7kAG16TsUNIPxRq3AuK5TUa8u3KxtoBwoXNA4_BS1yfCjt79dguaQmkB3EojQg7AReorTSOybmmqgN4uP8mIm6qrAZhfyO__jWeO_ngDAUQVUMTwLVPsDDySP8s6tgF8wHvTJSGuPdNCii7wo2t7eCtrZa1oLVAioS3PB9e6FQltaCHbovp0Gq-nGWr0v0_Z2HarUYMrzwvhZxSZDJxCzbyRJ2VrRzo3RK1zVsCec65kTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرمربی استقلال: در کشور دوست یعنی عراق می‌توانیم از شرایطی شبیه به میزبانی برای بازی با السد استفاده کنیم  @Farsna</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/462076" target="_blank">📅 21:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462075">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUtK65TmFuts19aagx19tkm-BPiNntjMF-d7wWNmmIfd2ye2BXsctFiakDWX78mHb8nr5A7OKutDtnZtkfto3bNwj_2jI8hFG_GVUQoFGJnBejIrgX750BtQqLweli9EN5k5KCX83HACXXzwT_oEGXzHtaz-uM50uol9VG4Ag5milfUu8wlDOwFkmR7acUhvvAdZSAU7frAMgvGxIZJ_zJRNDZinhNs6q80tXKqrA1svP9QqjiD_Wg_f9seBcP2Afxlh1l9jthQwYUDdhh3WYSRGLaL6rvKWLgimT8HkGx8h5KmEEQnTjluUzxvVZ9EDTvYRX72R7Aes3wBDQ0EM2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانه‌هایی که برای فروش نیستند!
🔹
«در تهران بیش از یک میلیون مسکن خالی داریم که به نوعی احتکار شده‌اند» این جمله رئیس مجلس محمدباقر قالیباف است.
🔹
دولت می‌تواند با گرفتن مالیات از خانه‌های خالی، مالکان را به سمت اجاره یا فروش ملک سوق دهد، اما میزان مالیات اخذ شده از خانه‌های خالی در ۴ ماهه نخست سال ۱۴۰۵ «صفر تومان» بوده است.
🔹
طبق اعلام مدیرکل سابق دفتر اقتصاد مسکن ابوالفضل نوروزی، در ایران برخی افراد بیش از ۱۰۰۰ ملک دارند.
🔸
کارشناسان معتقدند اجرای مؤثر قانون مالیات بر خانه‌های خالی و مالیات بر عایدی سرمایه می‌تواند به افزایش عرضه و کاهش سفته‌بازی در بازار مسکن کمک کند.
🔗
حالا جمعی از مخاطبان فارس در پویش خواستار مقابله با احتکار خانه شده‌اند؛ اگر می‌خواهید از این پویش حمایت کنید
اینجا
کلیک کنید.
@Farsnews_My
-
Link</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/462075" target="_blank">📅 21:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462074">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4a188659f.mp4?token=itBcc3MsUltiMoIHYqFE9oAhMxwumM-u0VRY3Xjm9h3-hpsXFDNZiyZWOZhlo9w1QC4KmaW65lepixcz-N96FpL_OcDhU4RcduvQIEkwNmzN_34hu1uBH40atYsWi5gHyiqkEph2EC9mNpUloK-W51YJOaGrR3BxAeZcsLoFNe9GtzVI5b1WL3CUEe13sqKM9dQevCeDwMDrWKAvErqGzYpTPPtP1ZizAUTvwShqHN9NEzjf9mAR29cD_abVumIrIWdt3M9Qai-Tq2cZBJh_PeSaqtRP8CqRaaxKMb8j1vDEuuP0txUdHUZpueTLaAhaINwNCPes_BDWCsM2bCdVb6lY8rFb2L7psZiqkSv9miylZ9S5jNynQDCNq6vFAVyew39ioKOoeFtg7F150kHsKDaYwJI3HY6XsVUhCg9QAWsXOdcGzGD6vtz1lFiF_ADKHzhz3U6N2Z97fMCRIGeTeqI36YTEiuKPJ0fJo0aHGNBk9vex0M_PMyy5AH8Q7vxZXPMbGnLn5ZbWQ8PKRtfisKkpAXbX2XYPAhz_hQGrcrTbmn8bfvYWPdznISB9d9FThk92ySKDjD5TVtp2I7SHtv7mqqEM-FtmlaGNssIiWGkTLMko3eg5joUWTmBfq0zr8PzhL9OJWj0GXAt-QnEckVJ1wdaor4XgYOZFLSxR6Dk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4a188659f.mp4?token=itBcc3MsUltiMoIHYqFE9oAhMxwumM-u0VRY3Xjm9h3-hpsXFDNZiyZWOZhlo9w1QC4KmaW65lepixcz-N96FpL_OcDhU4RcduvQIEkwNmzN_34hu1uBH40atYsWi5gHyiqkEph2EC9mNpUloK-W51YJOaGrR3BxAeZcsLoFNe9GtzVI5b1WL3CUEe13sqKM9dQevCeDwMDrWKAvErqGzYpTPPtP1ZizAUTvwShqHN9NEzjf9mAR29cD_abVumIrIWdt3M9Qai-Tq2cZBJh_PeSaqtRP8CqRaaxKMb8j1vDEuuP0txUdHUZpueTLaAhaINwNCPes_BDWCsM2bCdVb6lY8rFb2L7psZiqkSv9miylZ9S5jNynQDCNq6vFAVyew39ioKOoeFtg7F150kHsKDaYwJI3HY6XsVUhCg9QAWsXOdcGzGD6vtz1lFiF_ADKHzhz3U6N2Z97fMCRIGeTeqI36YTEiuKPJ0fJo0aHGNBk9vex0M_PMyy5AH8Q7vxZXPMbGnLn5ZbWQ8PKRtfisKkpAXbX2XYPAhz_hQGrcrTbmn8bfvYWPdznISB9d9FThk92ySKDjD5TVtp2I7SHtv7mqqEM-FtmlaGNssIiWGkTLMko3eg5joUWTmBfq0zr8PzhL9OJWj0GXAt-QnEckVJ1wdaor4XgYOZFLSxR6Dk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از واقعیت تا قهرمان پوشالی
🔸
خلبانان آمریکایی برخلاف ادعای مکرر رئیس‌جمهور آمریکا دربارهٔ نابودی پدافند ایران، به قدرت رصد، رهگیری و شکار جنگنده‌های خود اعتراف می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/462074" target="_blank">📅 21:26 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462073">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6hxW6Q4xFoErN159S140CDdeBquZLg4Rxwydz7wePgVpwG4iolJks6EPsJER3mqrx_pj08nM0JlNBJJzKJqA9aGc4H1T7BGfvyehG8HE00Bwum85uKG08hKryfHE1wiHwfCNl_OZhUW09Ik4VnB0OlDIe8j5TixvziFpaTJ53I_PIX3Ra_8pOPO63E_LJMEV5QYyIhc90IFPP60QHArP6ZceHpEZSlSKLo_kiMUrjfhzU-A3DRD9Cjo-iklkmqYaS2EWkf0XxThUueKPmlrTcOCggQSoskFmwM3MZYgKIV_fNgtTnEfArcrkcSd2zsS35xBjRVc8DcDM0F8Uejz7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
گل اول الاهلی به تراکتور توسط سزار روی اشتباه خلیل‌زاده
⚽️
شباب الاهلی ۱ - ۰ تراکتور @Farsna</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/462073" target="_blank">📅 21:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462072">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyEh4rrEmzJQKHI1_fsKLTOOWK8ETABO3QBEXu7NxhnaHeLXq_vjJi1geYjAVyRJ8XVOv9e1FKYxE5_ywhGzAAWpDYHG3utmM_unV0Lwy97Jhb7y9xSCk3oKXKRvWxM4GN_HRVVQPte4lsK34Z5NIZlSMbNz0Zi0p_dje7PXcBS1_vLMafV80g8UwpYUd3YMkbZtdHvjsZLSdrahhwCxKNeqexVPjuurKkey2dFFcVurIGCDC6gg27-Kd2kV4l7upp2dJruUJEPbJuFk2n2kpcfTwYeK7orutgzoSX_-Ht8dgdcO09mA4Z1UhsBZZUE9GwopvrJosebfpG5Lanh_hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان خطاب به آمریکایی‌ها: حداقل مردانه بجنگید
🔹
آمریکایی‌ها دولت تروریستی تشکیل داده‌اند و هر کس را بخواهند ترور می‌کنند.
🔹
مدعیان حقوق بشر و انسانیت، اگر صادق هستید، چرا کودکان، بیمارستان‌ها و زیرساخت‌های مردم را هدف قرار می‌دهید؟
🔹
اگر مرد میدان هستید، بجنگید؛ نه اینکه با ابزار و تکنولوژی، انسان‌های بی‌گناه را محروم و آواره کنید.
🔹
امام حسین(ع) در کربلا به دشمنان فرمودند: «اگر دین ندارید، لااقل آزاده باشید». اگر انسانیت دارید، حداقل مردانه بجنگید.
🔹
راه را بسته‌اند و تحریم می‌کنند؛ تحریم به چه کسی صدمه می‌زند جز مردم؟ کسانی هم دم از ایرانی‌بودن می‌زنند و دیگران را به این اقدامات تحریک می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/462072" target="_blank">📅 21:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462071">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fm2k0lpWJjumGPX0LBGwsNbjg9f9IYWLInKQqu6P0TnHJvC7LbnTYQm2bqoE83CdrljXoF6TEJBa0uPqBz1-s0gp85qIX5OOc-NV8sXnmoSxtnI4tE6eb-UvRogG4pi0OmwxDSEbkr1P54y5dprroHZC58Pjztmc2jRgUj8r5oFGHpuUyO5mXDL4-GU7rWdwDydr9pRcmy2c5rkazOlpHrkXCs4BhomGnSC9zOu4b5nnVs5dh3VdA32hfsn9deqWojzkBe74zz88CgV3smvAB6Be1JKcevCK_vsXLZjM8pwIAR54qW9GMCdVN0u7ic8pQXdgUAW4HEHO1vSe21obAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدرسه‌ای که قابش از کلاس درس به رقص و قمار رسید
🔹
انتشار ویدیویی از صفحه رسمی دبیرستان غیردولتی «صعود» شهرکرد، حاشیه‌ساز شده است؛ ویدیویی که در آن صحنه‌هایی از رقص، بلاگری و استفاده از ابزارهای قمار در فضای مدرسه دیده می‌شود.
🔹
این تصاویر این سؤال را ایجاد کرده که چنین برنامه‌ای چگونه در یک محیط آموزشی برگزار شده و چه نظارتی بر آن وجود داشته است؟
🔹
مدیر روابط‌عمومی آموزش‌وپرورش چهارمحال‌وبختیاری گفته این مدرسه مجوز آموزش‌وپرورش را دارد و موضوع در شورای نظارت بر مدارس غیردولتی بررسی می‌شود.
🔹
به‌گفتۀ او، مدیر مدرسه مدعی شده تصاویر مربوط به یک دورهمی خانوادگی بوده که در فضای مدرسه برگزار شده و انتشار ویدیو نیز به‌اشتباه توسط ادمین صفحه انجام شده است.
🔹
با این حال، آموزش‌وپرورش تأکید کرده مدرسه محل برگزاری مهمانی و دورهمی نیست و در صورت احراز تخلف، شورای نظارت درباره آن تصمیم‌گیری خواهد کرد.
🔸
حالا سؤال اصلی این است: چطور رقص، تولید محتوای بلاگری و نمایش ابزارهای قمار، آن هم در فضای یک دبیرستان، امکان برگزاری و ثبت و انتشار پیدا کرده است؟
🔸
با توجه به محتوای منتشرشده، انتظار می‌رود در صورت وجود جنبه عمومی یا عنوان مجرمانه، مراجع قضایی نیز موضوع را بررسی کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/462071" target="_blank">📅 21:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462070">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6978f750b.mp4?token=kHkXRHm9BnOt6IURT_0lh1n7O3Sog6uoO80ASPSmbEuluN6agwoAxXOc4NsbQ4OHKX2TX9EbQ5JgxT5Kme7f_q1DT-oqpIGJp4BieIe-7C_it8ajge7_z3PPO2OTY90tGEy1PTAB5pvtdXd441OhfQxOTcgMgWX7pOpLmkheBlp1rybi7hwnaim5aol7Wp6FauNyexGnCAl7B5n6Yfbl9hCeFSX-O_QkcACwIbAxbtNAWbSHdUe1k1Vz29ttt3643e9sA6X6YwevmvEaEB9fSjh0rs-MORACcgIoPhIWTOX6GoTLsJLVIRO0DQDc6qI8bpM4ZBIFVz1jxO83inUIHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6978f750b.mp4?token=kHkXRHm9BnOt6IURT_0lh1n7O3Sog6uoO80ASPSmbEuluN6agwoAxXOc4NsbQ4OHKX2TX9EbQ5JgxT5Kme7f_q1DT-oqpIGJp4BieIe-7C_it8ajge7_z3PPO2OTY90tGEy1PTAB5pvtdXd441OhfQxOTcgMgWX7pOpLmkheBlp1rybi7hwnaim5aol7Wp6FauNyexGnCAl7B5n6Yfbl9hCeFSX-O_QkcACwIbAxbtNAWbSHdUe1k1Vz29ttt3643e9sA6X6YwevmvEaEB9fSjh0rs-MORACcgIoPhIWTOX6GoTLsJLVIRO0DQDc6qI8bpM4ZBIFVz1jxO83inUIHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر راه‌ و شهرسازی: هر وعده‌ای که می‌دهید باید انجام دهید
@Farsna</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/farsna/462070" target="_blank">📅 21:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462069">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebc8faeb94.mp4?token=ZAI12z75sK9kQMobV4zTxNuTSNCybjNBhWukGDpmBicS4AfXIKLTmi9ybdQQ1lyi-t_nD3gvmdm6QAIrB7ULvOF6-tblQP0_bM-0ulbpf9WbbJd9E-53-a4Yb2cGk94U_L5MT-bVqQPuuadNbN4J_OvdnkGR5nyeJT90jXYDWe-3_nKTd5SZflaMO9TU25NnTKLBZCTqmqW45dlawg04SEnDdw4HxHsw74BBprRv29mqq4OpyxvnKvDjxfJIj0xWM8h2eJ8lIDk97ieXwEVPfB6OieJExHUBQHRN8NLrJUWlj4Xz5cG93Ztyz6jfMNpCHGfmXkXIYnzqDEh77iEuoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebc8faeb94.mp4?token=ZAI12z75sK9kQMobV4zTxNuTSNCybjNBhWukGDpmBicS4AfXIKLTmi9ybdQQ1lyi-t_nD3gvmdm6QAIrB7ULvOF6-tblQP0_bM-0ulbpf9WbbJd9E-53-a4Yb2cGk94U_L5MT-bVqQPuuadNbN4J_OvdnkGR5nyeJT90jXYDWe-3_nKTd5SZflaMO9TU25NnTKLBZCTqmqW45dlawg04SEnDdw4HxHsw74BBprRv29mqq4OpyxvnKvDjxfJIj0xWM8h2eJ8lIDk97ieXwEVPfB6OieJExHUBQHRN8NLrJUWlj4Xz5cG93Ztyz6jfMNpCHGfmXkXIYnzqDEh77iEuoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاربران فضای مجازی از روایتگری غیرهنرمندانهٔ یک بازیگر اینگونه انتقاد کردند
@Farsna</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/462069" target="_blank">📅 21:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462068">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaFpZoVeTcUfzue6sOWcqRxKTdaQFSLFzJ0zxlojUM27z1f6Bt6yye0nrGGQediLFraUrNMtNMlUgP_As6XUF4X5gRlRAchf02WbytHaE-zFp3AsLyCxbibyYRfR5KL-nIJzdN0iWr7RTJMg6LcMSLHxwOmtLbGUwSQiVcEergFny4JasSx8IorKNp1Sg0stMheFtKDd0E7YBY59A3gv-uXSJwKqAs5mcxB2mfYitan7X8rJpk057u436miMR8grNdfsRRzjTGJMGDS-BiukXB8guZQIR6tjdfccKtV-P9DasRXb-A4U_-XmIg4UPPWzahQCdp2Joeltb9OsUsWVFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
زاکانی: ۲۰۰ شب است که مردم خیابان‌ها و میادین را رها نکرده‌اند تا دشمن را عقب نگهدارند، خطای محاسباتی مسئولین را اصلاح کنند، وحدت‌بخش و انسجام آفرین باشند، از ایران و انقلاب صیانت کنند و دست بیعت با امام خامنه‌ای را بالا نگهدارند.
🔹
خداقوت به ‌ملت مبعوث شده و قهرمان ایران
@Farsna</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/462068" target="_blank">📅 21:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462067">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5dcf505a3.mp4?token=FKyA6ZW2wXTgq9Tf4bXh5Y9IIr7nvgnQWbDcidrt8cvU9i0B88EYDsFjCGVgqcS8DO873d_7SP8gSrc4jLRWLkTJO65rFReIpzeKRk1INCFB12Fjdnqwgpi4fgdt0itgdGygL_RtyzZRIXV0wB_XtEvdsue7jgoZC6IsKj5Boyn3MDFJmsAdkNrbQE0bQQL9OB_UXzpSyVMrjflFlguE5wBt79ySfcNP1QMt8F8DI7-spDLWeU5YH8sQOb1zyiAR3MuYn0DxgSXP11QewCA358dJe49h48z49fwq7OOl6fk7TDsV6HG2XAao1v2cS0rupkMNUJeOvnHlvtLDsARp3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5dcf505a3.mp4?token=FKyA6ZW2wXTgq9Tf4bXh5Y9IIr7nvgnQWbDcidrt8cvU9i0B88EYDsFjCGVgqcS8DO873d_7SP8gSrc4jLRWLkTJO65rFReIpzeKRk1INCFB12Fjdnqwgpi4fgdt0itgdGygL_RtyzZRIXV0wB_XtEvdsue7jgoZC6IsKj5Boyn3MDFJmsAdkNrbQE0bQQL9OB_UXzpSyVMrjflFlguE5wBt79ySfcNP1QMt8F8DI7-spDLWeU5YH8sQOb1zyiAR3MuYn0DxgSXP11QewCA358dJe49h48z49fwq7OOl6fk7TDsV6HG2XAao1v2cS0rupkMNUJeOvnHlvtLDsARp3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر دادگستری: پزشکیان گفت از کارهای دیگر بزنید اما کالابرگ را افزایش دهید  @Farsna</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farsna/462067" target="_blank">📅 21:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462066">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0537cc5087.mp4?token=MDbUH9Yb7oq0Pn1_YQUfJ0ivHKM3uDGLlvaPfrFXIO_blt3qyX9B7KnjRXzUyeFkc2n4cYrE99CmRrJq0cgOiqp_KvZ4iQM7yaFDD_2hgSsWf2M2Q0jq2qtIEyFj-ifCS6HfGzfkUBDkl4Z82yUO-7DFIG37s0KkovchTTc6GEW0ZDCQ9UQLTwWMlI2EgjBy-AmEmOn_7h_AvKoi2Ebsw853oJBsBgrrUBb52NS2TwPqtON6fT6-X4Y1KKf0yICLqkTpGg1RXA1gjzFLTQ5PfT2K60TYJjZ_-nFbIYFU76FqTafW4SJ4gB_F30jCBCp_11C6LhvQ3xkTxloDCICOmTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0537cc5087.mp4?token=MDbUH9Yb7oq0Pn1_YQUfJ0ivHKM3uDGLlvaPfrFXIO_blt3qyX9B7KnjRXzUyeFkc2n4cYrE99CmRrJq0cgOiqp_KvZ4iQM7yaFDD_2hgSsWf2M2Q0jq2qtIEyFj-ifCS6HfGzfkUBDkl4Z82yUO-7DFIG37s0KkovchTTc6GEW0ZDCQ9UQLTwWMlI2EgjBy-AmEmOn_7h_AvKoi2Ebsw853oJBsBgrrUBb52NS2TwPqtON6fT6-X4Y1KKf0yICLqkTpGg1RXA1gjzFLTQ5PfT2K60TYJjZ_-nFbIYFU76FqTafW4SJ4gB_F30jCBCp_11C6LhvQ3xkTxloDCICOmTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردان روزهای جنگ دوباره به میدان آمدند
@Farsna</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/462066" target="_blank">📅 21:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462065">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/384d8d2925.mp4?token=cMTDQv5jcdZ4kcBIAKBOtGy5NUIiApMDHSn7LID0Dzj1N2RkvvLZdcxDrvX5yaLJu4u-dKZDkN_onHy1LH4_Ec0Lkm7SQc6OLv8ydTPEZ3_o1bMOBed_p5gEbbBR6oZIJgO3UAXmrfcfxc62CFMhIW5cS7W4pSXORcu4Xe_vuKgtCGpV66MqvjIxgKgfCMopKF1nzwpZoJwzvjCqc6C9b0LRwXwAGBAyqBbmitHyJYuuA2gahO6uITXMlOm8kX5lNKyTbjcR6Z_e3T6eqeUuY1zXSsX2q7cY8bj7QFlx5KhEAxvzpVKxaph_2VipkCyTSvp91Iw5Odwfa1HSKA5Avg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/384d8d2925.mp4?token=cMTDQv5jcdZ4kcBIAKBOtGy5NUIiApMDHSn7LID0Dzj1N2RkvvLZdcxDrvX5yaLJu4u-dKZDkN_onHy1LH4_Ec0Lkm7SQc6OLv8ydTPEZ3_o1bMOBed_p5gEbbBR6oZIJgO3UAXmrfcfxc62CFMhIW5cS7W4pSXORcu4Xe_vuKgtCGpV66MqvjIxgKgfCMopKF1nzwpZoJwzvjCqc6C9b0LRwXwAGBAyqBbmitHyJYuuA2gahO6uITXMlOm8kX5lNKyTbjcR6Z_e3T6eqeUuY1zXSsX2q7cY8bj7QFlx5KhEAxvzpVKxaph_2VipkCyTSvp91Iw5Odwfa1HSKA5Avg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر دادگستری: کارگروهی تشکیل شده که اختلافات بین دولت و قوه قضائیه در آن حل شود و رسانه‌ای نشود  @Farsna</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/462065" target="_blank">📅 21:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462064">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBw37ZZXt7MwjvACScKmrhmRLoG2WXAR4TWOy34JWCfGamBmJn3MkHiQ-xutv6o9Fnn05Vx9KDELsiskX8EOldsFFVCQMWSQq_tcjYG2xHfhTHDw6s4B3kf-9eDSoJ9IdisKk_x3wauwG8GTZPZC2nDmQg_rwdQcyXhzLbaMfPRm-cltH9zZ66YJN73b978X8r0ngJA35sDrRBGFRacaQmn-bqfKd7FwdpxglJtLH37AzplkvKHCQUfFzbGj12-78peSzIpe4p8qHHASFqRRvGsQebKTzoSoGT057YS0THL_kpav7bvOunhC6x64ACCWqTrEpAVauOyM-nxPjo6OIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: نشست ایران و کشورهای منطقه به‌درخواست عربستان به‌تعویق افتاد.  @Farsna</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/462064" target="_blank">📅 20:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462063">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‌
🔴
منابع یمنی: منطقۀ المخا هدف ۳ حملۀ جنگنده‌های دشمن سعودی قرار گرفت.
🔹
همچنین در حملۀ عربستان به یک پل، دو غیرنظامی کشته و یک نفر زخمی شد. @Farsna</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/462063" target="_blank">📅 20:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462062">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-a7WR-UGDA8Hy0hzGjmLGc_jOg0j6BhaU9TvZFB-XZAX38N4M7RuwPlx4T3PdHXk-GJV5r7g-Mo31wv5qo6T1G3Kq3nkYSdio75bDBTVGco4wGfRekgKFWyA0RzP1I4ubWwmnzS70aZnCQXob4dLfgfUp59gTnEfubFoNqEdBPBsWTqqhSTFcvE3Addss9ycMcpB2IFRNkV6lzUx3XF5Mowxy4fB2nC7nJTxIew3t0KCuD7IWs1sHM2oeOUWUvlirgoTdE9eaD0Opn-_87ZpdVZ_xL7qEfkfMZHu9iEr3qxCjNpeihFyAyNfE8hWMDPD12oW4AuBns1GVMeEE7nxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش و سازماندهی ۱۰۰۰ گردان جان‌فدا آغاز می‌شود
🔹
اطلاعیهٔ شماره یک قرارگاه مردمی جان فدای ایران: پس‌از شکل‌گیری ظرفیت عظیم پویش جان‌فدا که تحسین دوست و تحیر دشمن را رقم زد و با توجه به استقبال بی نظیر و پیگیری مدام مردم برای قرارگرفتن در کنار نیروهای مسلح…</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/462062" target="_blank">📅 20:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462061">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61bd07adf1.mp4?token=D3ISSAq2gTLC_RrT1rGe4zPDVYe7guQARNjmZf2qdJWpvlgy2Zkm_cBlTD3-SoSoEN_05qIcxMUlci6ky-50RR3WtoLItTIDIGWkOuFyV2_knyW7zbxjy5C61QHOmLhzSjvdEcvopSErd0V1CUrpjJ4ajhPTb4AeTlu9xtIDtiyQnq9oQaaSMmhFeGjSionpgOKzSbkaO0ELhxMz6KKCS4pqhZkBwY1Gdp12gkr4870X_ZiYO135oJris5Uc9OylcPSRXJUC6Z4TIQ1A8bX7icxIx6G71g5Ei8AsYEcpAe2-XZUwai7X0fkAhIw34APK5QCQBewWQSG90_CFfHdDCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61bd07adf1.mp4?token=D3ISSAq2gTLC_RrT1rGe4zPDVYe7guQARNjmZf2qdJWpvlgy2Zkm_cBlTD3-SoSoEN_05qIcxMUlci6ky-50RR3WtoLItTIDIGWkOuFyV2_knyW7zbxjy5C61QHOmLhzSjvdEcvopSErd0V1CUrpjJ4ajhPTb4AeTlu9xtIDtiyQnq9oQaaSMmhFeGjSionpgOKzSbkaO0ELhxMz6KKCS4pqhZkBwY1Gdp12gkr4870X_ZiYO135oJris5Uc9OylcPSRXJUC6Z4TIQ1A8bX7icxIx6G71g5Ei8AsYEcpAe2-XZUwai7X0fkAhIw34APK5QCQBewWQSG90_CFfHdDCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خائنین خارجی زیر ذره‌بین سامانهٔ علاج
@Farsna</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/462061" target="_blank">📅 20:44 · 23 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
