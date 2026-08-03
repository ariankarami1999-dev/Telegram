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
<img src="https://cdn4.telesco.pe/file/jG8lb3WrLKFdL9tZMulcP6Pi6-_bKDPMzqvTsBq4TLAj2tALaDJCEtYI27Fpln92udpfY-TVzldOw3twUQWFH6TEQyiMYGtGyvOvsalMrk9Schd5m8AF8o2BD2HjwViiRHoZlsfKIyTA5CymoHdTL6D8vPam_a4Yow9fffSYuyjoIuaW3BZT0wcld-mOOy14uSvCkyNQjWKGFGXK5q6ZctdloOFqwk77motg4-cqnvAzHDYswGtk3OtSOSPhTsxx-kxni0weC4ZCph3j_Ob8GEE-npklHVOeCzC2uYqrr8pFLtkgQDBBWwjfrIeggQq027KdTYCtQr6qI427q48nDQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.06M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 20:14:56</div>
<hr>

<div class="tg-post" id="msg-678143">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
وزارت جنگ آمریکا: توافقی را برای افزایش تولید موشک‌ های پدافند هوایی پاتریوت  به ۳ برابر و ضدبالستیک تاد به ۴ برابر امضا کردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19 · <a href="https://t.me/akhbarefori/678143" target="_blank">📅 20:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678142">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
تغییر مسیر ۶ نفتکش سعودی از ترس حملات یمن
🔹
اطلاعات مربوط به ردیابی کشتی‌ها روز دوشنبه نشان داد ۶ نفتکش غول‌پیکر با پرچم عربستان سعودی طی چند روز گذشته مسیر خود را در خلیج عدن تغییر دادند.
🔹
خبرگزاری رویترز با اعلام این خبر گزارش داد که نفتکش‌های سعودی در حال حاضر، به سمت آفریقای جنوبی در حرکت هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/akhbarefori/678142" target="_blank">📅 20:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678141">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YARfU4rBGmfrlwHxVQd95pmq2xHZtUT7LW2deCejXJqwKcX9ZYsRhXkZHvh6EOfMuzT9QILmTIEXWBaLTd9YLeoPv4a00Nh8tq5LMubZtg0_-rlHaAx3UaA6flVQmwSbO5dWiZTC8aNYOBAo3t5YYNPkEiFIoUoJLkaL7sJZAftQrxvjIvG_-AFwK24ZZV55b5-PqzN1aIoieFDEcAfb3RQeaT2BOBF-HN3PsoWwG60nWs7aQ-jgApO28PN95iHw_SBMz5KXxXiwAbqi_sw2mob2y8qyOdvDubeSXsa3TjZimvpMg8ql5ajajQzUK5IDzglJjiXNPOcE-YJLM9dPQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/678141" target="_blank">📅 20:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678140">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
امارات به اسرائیل سفارش فوری بمب دقیق و پهپاد داده است
روزنامه اسرائیلی هاآرتص:
🔹
امارات متحده عربی از شرکت البیت خواسته تا به سرعت شش پهپاد پیشرفته هرمس ۹۰۰، که در ارتش اسرائیل با نام کوکاف (ستاره) شناخته می‌شوند، را در اختیار این کشور قرار دهد.
🔹
امارات برنامه‌ای گسترده‌تر برای گسترش این گروه به ۴۵ فروند در قالب ۱۵ سامانه کامل دارد که ارزش کل آنها حدود ۱.۳ میلیارد دلار تخمین زده می‌شود. اسناد، یک پروژه تسلیحاتی دیگر به نام «یاسمین ۳» را فاش می‌کند که شامل تولید ۶۰۰۰ کیت بمب هدایت‌شونده تنها در سه ماه است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/akhbarefori/678140" target="_blank">📅 20:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678139">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjHkmLjEMVMzMyZMXEpFH_-0eRN1ddODDHZ0eSm4xPEfBL61UHRr76NlXhRbGYU1ou7rp_qyjryyMVHFNUQPPv8S5Q08KKOX5l-RniPm4-SJwkUrlbA1N0YpeC9k2nEX7myd3atqLuaSXbK119cBsjztgqOKZ_59lxek6Mz1ctQ51rDmGGbv0_h7RC-gyHgw9CHozEfWG4xdm87baulqyHKNtW2OJgCj9nOLzTB94VlaycVsABmhRy6bPYu8nGDrV8hNJoQe7UJHJ1BwjIcr5dQly7Ls9X5k0e5Tb-mHm0BIgpzHKo7KzFw43i0zGSQe_3VAXpGRk9wJQ4Z5idmItw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منابع غیر رسمی از جدا شدن امیر و رهام و منحل شدن ماکان باند خبر می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/678139" target="_blank">📅 19:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678138">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c65d289641.mp4?token=OI5C4NuURHpOr4vbjFdSInpnROH5HJueHKommdDKg2A95GoYdqJ1eFaZGcAHxiICdKZoGz8BkUWDC_8lvcJZxbl-YwCZZM3hFSjusPX19cVUjrwlYq8o_WuXCpyiY8c6aSzaffN79TNm-ZvLYx2LfuvVhl5Zkt6JAdrS0XjyC6PRRhKin71fldRoxzcbHAw6yzur_QWV50sKNk3qVkdlPHXQk0nyGRxcYAvYGkVYdlMZZ2IuC9ryQRjsNmKs6Fo8B3CG9GaLm0GH8l2O4nxEOaTnwdbgGmIqn05jPeq1UakK6cPsaOfCYVq66AyQV3A---RB2YdTj8uoHf_oZ0myug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c65d289641.mp4?token=OI5C4NuURHpOr4vbjFdSInpnROH5HJueHKommdDKg2A95GoYdqJ1eFaZGcAHxiICdKZoGz8BkUWDC_8lvcJZxbl-YwCZZM3hFSjusPX19cVUjrwlYq8o_WuXCpyiY8c6aSzaffN79TNm-ZvLYx2LfuvVhl5Zkt6JAdrS0XjyC6PRRhKin71fldRoxzcbHAw6yzur_QWV50sKNk3qVkdlPHXQk0nyGRxcYAvYGkVYdlMZZ2IuC9ryQRjsNmKs6Fo8B3CG9GaLm0GH8l2O4nxEOaTnwdbgGmIqn05jPeq1UakK6cPsaOfCYVq66AyQV3A---RB2YdTj8uoHf_oZ0myug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی در نجف: سالی یک بار به اینجا می‌آییم و انرژی می‌گیریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/678138" target="_blank">📅 19:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678137">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
رویترز: ذخایر نفت در آمریکا به پایین‌ترین سطح از سال ۱۹۸۳ رسیده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/678137" target="_blank">📅 19:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678133">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rNis4YRMCqr23D4PPWtErjshrpkRZjejJyOf1o5Xju2Ca7z3Ww-WH6IDkbm_xz2Ai6TVUGfDsWCmSD0EEbjSw7IeGGS6Jgr_dCcqsuLb8HWuUgOkcCmJ9voDgr64749A5KcDSrclgwZAoG4f3nEhbp8E5JDffFHfIu0FESTWjk5F3odddIPX3SOVcon7JMQvAyZWCO98gOOs_6jDH1mWnRtdavFkJz9C2Qmd3hEYiuy9eq4d23S_a7F9lm7Ejsok7h0iw0BSBMLc_cCCarcvikRipzQEXYeWgtQkgTI1bqJsYhnulHuJQFhzCsO5efTCRfiyy90t-WLFWCFyQkkmfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zg45gV_EJa6fCU6LXpGkNCgotc2rBpCtu7orGFZZDfz8oB-Bv-vkVNRM8XAvvqr0fK8e67Tyu5ctBQgJe2G0GN6FKvSrh5Uc43xyIBM3d8AzUvP360xiyoNwh4U5Dd0eYqAd9IuOqtAp3KitZMRchWlwVLPtAeMHDP5Yk5xXL_MbvkaSmyXPEpQDSshe_9AmManBUb1Bw15YVmEuPbij99fTkYXNM0qR8EzMo-MNXXmEGqtMdtl2nQuYPVrU2Ep_E_VkmcXVnOpXKhKuIO2xtLBbcobbeuRL5YU2FFaNlGpybwVmgLVnTfLLC3-m4CvC3xQ6-LIK_1xg2h6mKIIdig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oxUwYkOGLFGNVTaWHwsu9Vf_fCoi7J__8-yWW6uZ7S7vOyNYoVjE-wM7iRi7UBzoGKapDCPgkeipPnSzvOyEBJZDaDMoe7bkZsNMeVhxUNmb7rAFDNOLwQy__57VX1VYG-sGXZm9XMX-2PndxmzsJKSBV0IMbXszxdTkF8cwaSbxiVZyFWVFNoMPNn2yXnMLdRTHnvpIhZlAUWInpjONV9IOOGdGYTkZBwHGc4M9cRj8QANfWU6pDZKC7kil4Snxp2s68yBtw_a6xKDw3b3Cxnl30xCYcH7yuH_4nJmc2FSGvj2WKgmyj_vyUS8_uRbAqHekQA9otNRVPhlefdIjGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R-x1yxOxDPS-hl7dnMoNeNDJ6VW0ovzYgoBPDeB_FOPyazlXNAnZ_kMh9_YTOp_DkDJchKqx2rgkDH7kFCb12bcQamTPylarbK8IAkKpH_RJ-XxadF5TiRK2EXn5fz-IwoVtY_1uqBPxZgzZd9xwv2hP9ZCj8wHCOE34SCG6B3fUWv5hMERtfBrDzkeSMEaYd_ATAziJSz1iSdn0YPxwbLMx4N7QjSFQh-JOeCkM1q6YbhXyFRv-nQTRmBV4eM3fEHZgnTJrWoaFBJH93896O-5Gdhp5kSn8KvNVbJrNvZXXJbM8VeiN38MEHQDfjg3ZLu3cohPYoWeW1fpYl91dtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
میدونستی
نیازهای مهم بچه‌ها که ۹۸ درصد والدین
نمی‌دونن؛ چیه؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/678133" target="_blank">📅 19:31 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678131">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebee8d7d54.mp4?token=JB6MpWvT_uAtpxpQE4HFWVKG8beCFdtUat-3cqrFauStC2NmJNDkq23wPuanBzI3gL-aHryvHPajUMMclCFhgYVdNJRDe8P6ky9_BCR4NuOE1mqHM3eh4-NcepyH2uu7xAMzloTpB6BH13vCSAj_LrYAJgHksrO4f3oyYRMrGBHnvwQroS2mw4weft3GTf6PqHVeDJcYWN84H9bbs_SL2BoN3Fp5nWzcE2cAA0sPt7hqOGQd6WWj6rSXEtcmrWT96vgVtUSZDyOjoqdJOEDvZhel9txc45HrkagfUvZbNuNctdnt8UmuWfzHSJMIub8zhXNxSOQ1erZw5gaJvUgdYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebee8d7d54.mp4?token=JB6MpWvT_uAtpxpQE4HFWVKG8beCFdtUat-3cqrFauStC2NmJNDkq23wPuanBzI3gL-aHryvHPajUMMclCFhgYVdNJRDe8P6ky9_BCR4NuOE1mqHM3eh4-NcepyH2uu7xAMzloTpB6BH13vCSAj_LrYAJgHksrO4f3oyYRMrGBHnvwQroS2mw4weft3GTf6PqHVeDJcYWN84H9bbs_SL2BoN3Fp5nWzcE2cAA0sPt7hqOGQd6WWj6rSXEtcmrWT96vgVtUSZDyOjoqdJOEDvZhel9txc45HrkagfUvZbNuNctdnt8UmuWfzHSJMIub8zhXNxSOQ1erZw5gaJvUgdYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساخت روزانه ۱۰ ویدیوی انیمیشنی با AI به صورت رایگان
🔹
سایت Digen AI روزانه ۳۰۰ اعتبار رایگان برای ساخت ویدیو ارائه می‌دهد که با آن می‌توان حدود ۱۰ ویدیوی انیمیشنی تولید کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/678131" target="_blank">📅 19:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678130">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b33d8fc781.mp4?token=DHUJFLqqarUZkf5K0KnCs5Oc5fdSZfB15G0fHQslU6qQ5ujTueGxcDoUmvVnza9UAWvlOAbA7DqteWtrA0qfVUizOIQUfc0E0svbpJszG0KnbPZukdL8Hxs5fkU1TJ9Dsal_w08OazTxMstgStzpNJBd35vCbRTq6gRUZPItc5oyBVM6YK0B4uOrdegXOzx1hKxzLu7gibmkG-NldPl_RAITpp1vdkkRFa7SXbBYkjY8-CndUzGf0QcBmJOvJHxiA7DplCCN-2vog748WHc6bAuj5QdD5gcuCoOW3c8rDk9wuSd0-owFdAr18dZ_Yl0ZhX58nT2BN1yW0DjngOQlYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b33d8fc781.mp4?token=DHUJFLqqarUZkf5K0KnCs5Oc5fdSZfB15G0fHQslU6qQ5ujTueGxcDoUmvVnza9UAWvlOAbA7DqteWtrA0qfVUizOIQUfc0E0svbpJszG0KnbPZukdL8Hxs5fkU1TJ9Dsal_w08OazTxMstgStzpNJBd35vCbRTq6gRUZPItc5oyBVM6YK0B4uOrdegXOzx1hKxzLu7gibmkG-NldPl_RAITpp1vdkkRFa7SXbBYkjY8-CndUzGf0QcBmJOvJHxiA7DplCCN-2vog748WHc6bAuj5QdD5gcuCoOW3c8rDk9wuSd0-owFdAr18dZ_Yl0ZhX58nT2BN1yW0DjngOQlYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسنوند مدیر مرکز توسعه پایدار انرژی: عمان خودش باید عوارض بدهد، نه اینکه شریک ایران در تنگه هرمز شود، عمان ۴ پایگاه تامین لجستیک امریکا را داشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/678130" target="_blank">📅 19:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678129">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
‏
ادعای خوک زرد: رهبری ایران به شکلی باورنکردنی فریبکار است
🔹
آن‌ها درخواست برگزاری جلسه می‌کنند؛ حتی بعضی‌ها "التماس می‌کنند". گفت‌وگوها آغاز می‌شود و حتی برای آینده نزدیک نیز زمان جلسات بعدی تعیین می‌شود، اما سپس با افتخار اعلام می‌کنند که هیچ مذاکره‌ای در جریان نیست، هیچ موضوعی در حال بررسی نیست و فقط با "عمان" در ارتباط هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/678129" target="_blank">📅 19:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678128">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-l7VXkezWazeonTwDMBK-WjfA5sXXkj_eaUWXlbYcdciy3CLnbyiyMJeqg-WRf0Ly-FsETLYso01GJxbW7HUaHN9H9jxug_0No-Of6SlOnD2mKbh206k-K5IH8P3fGNMWlINQw2NTJQSd0-e5gNmDILB0kxvxfWV5ykHyIMmsDux6aNW0_HWKcJPimieVHpM713bXBnJZkZ96FePvQVcyTBRIWFiVVxyTOO_ywe-WXcxrlQniumaM-n4_qn-73AcZlNVN0pqIW6TZIYgWIO3ZVv7M6H5r7dnyTUiMo3MHeecy2rlEryNZVm3NWF77cmrB9vpBJCW175PVutv5ImRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خوک نجس: هیچ چیز بدون خواست آمریکا به ایران نمی‌رسد
ادعای ترامپ در تروث سوشیال:
🔹
«در حالی که برخی حتی می‌گویند ایران برای برگزاری این دیدار "التماس" کرده، مذاکرات آغاز شده و قرار است در آینده نزدیک نشست‌های بیشتری برگزار شود، اما آن‌ها آشکارا و با افتخار مدعی هستند که هیچ گفت‌وگویی در جریان نیست، هیچ موضوعی مطرح نشده و فقط با عمان در ارتباط هستند.
🔹
سپس طبق معمول ادعا می‌کنند که تنگه هرمز را با قدرت اداره خواهند کرد؛ در حالی که این آبراه هم‌اکنون به‌طور کامل تحت کنترل نیروی دریایی ایالات متحده و آنچه ما "محاصره" و برخی "دیوار فولادی آمریکا" می‌نامند، قرار دارد.
🔹
هیچ چیز بدون خواست ما به ایران نمی‌رسد و تا زمانی که توافقی حاصل نشود یا ایران به‌طور کامل تسلیم نشود، هیچ چیز هم نخواهد رسید. ایران چه این واقعیت را بپذیرد و چه نپذیرد، ما در حال گفت‌وگو برای حل مشکلی هستیم که خود این کشور طی دهه‌ها ایجاد کرده است.
🔹
موضوع کاملاً روشن است؛
ایران هرگز به سلاح هسته‌ای دست نخواهد یافت.
»
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/678128" target="_blank">📅 19:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678126">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
سردار کرمی: در کمین تروریست‌‌ها و آماده پاسخ قاطعیم
فرمانده نیروی زمینی سپاه:
🔹
شمال‌غرب، سرزمین دلاوری‌ها و غیرت باکری‌ها، در کمینِ هرگونه خطای محاسباتی دشمنان فرامنطقه‌ای و گروهک‌های تروریستی است. رزمندگان با اشراف اطلاعاتی، آمادگی عملیاتی و بهره‌گیری از ایمان، فناوری و علوم روز، آماده پاسخ قاطع به هرگونه تهدید هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/678126" target="_blank">📅 19:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678123">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/078d1d0337.mp4?token=gZ-FWCP-qsPJQCu2czwdiGkHitHqqCbeWGOB_Y-E78nDcbsy9uI5BDzBnKFPseNhEkVn5cMEub13sly7fN0qtDV1Rm3RKf7pGkIKg5_aKoaO1hvv2IfbvL8vazgZrYIK5nRj2EDWcrPw9R2oyv7pSp5CNpQHq6Pc6YLhTXyeHz-jsiDUeLT5M58Wn7PvH6LiGn24MOMVHjGO4HPROk63ob3e69DR-uWlpdToFvhH4nTlDy0qaOud-RWRyS3uc5JVXxOeQkVMXJ_FdkMhfJb5rW9VE0VIjO_dm3W5L_xHQJN43p2kbWs3s9sg7PfWFMHJzbjblhYu2rGd04lIQGC3bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/078d1d0337.mp4?token=gZ-FWCP-qsPJQCu2czwdiGkHitHqqCbeWGOB_Y-E78nDcbsy9uI5BDzBnKFPseNhEkVn5cMEub13sly7fN0qtDV1Rm3RKf7pGkIKg5_aKoaO1hvv2IfbvL8vazgZrYIK5nRj2EDWcrPw9R2oyv7pSp5CNpQHq6Pc6YLhTXyeHz-jsiDUeLT5M58Wn7PvH6LiGn24MOMVHjGO4HPROk63ob3e69DR-uWlpdToFvhH4nTlDy0qaOud-RWRyS3uc5JVXxOeQkVMXJ_FdkMhfJb5rW9VE0VIjO_dm3W5L_xHQJN43p2kbWs3s9sg7PfWFMHJzbjblhYu2rGd04lIQGC3bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚿
ماشینت رو مثل روز اول برق بنداز!
با نازل کارواش سرشلنگی بدون نیاز به دستگاه کارواش، فقط با اتصال به شیلنگ آب، فشار آب رو بیشتر کن و به‌راحتی ماشین، موتور، حیاط، پارکینگ و حتی فرش و موزاییک رو تمیز کن.
✅
نصب آسان
✅
پرتاب آب قدرتمند
✅
بدنه مقاوم و بادوام
✅
مناسب شستشوی خودرو، حیاط، باغچه و سطوح مختلف
💰
فقط ۸۹۸ هزار تومان
🔥
قیمت قبل: 1,098,000  تومان
🛒
فرصت رو از دست نده، با کمترین هزینه یه شستشوی حرفه‌ای داشته باش!
خرید از سایت
👇
https://memarket24.ir/product/brief/58365/180124/</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/678123" target="_blank">📅 19:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678122">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd23435855.mp4?token=vsu1iLpZp6Sdo8kQ2cXdVozn9BKl1WuDPryFy-w8t4x0r3-LXhr5s-NsGQ8XYHXdzqb-RDHOcF-4jSkLItv55VmU9n6_FkKfm8Xga7XEQfcyr5exrNXgMfgqmSFFgM0t78hbgwq2bESKqrkajqPdb3SgJrvr6qGmv9Im-ujuP_un7YYtFUTZo12wyqfoPhfFOzg4IilJRtvexvqdT_GA-i5Qs0JCnrgvE50wtZg3WIxaPb25L_St5k5NUl8bg5MG_vFgEVjNdzZhdpb5xmV_vUBAYkr2uMbwlarwPvYBeDkrn4TU9J6RzYcRZq44958e5ftdyAqWGbWfiXqE6MI5uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd23435855.mp4?token=vsu1iLpZp6Sdo8kQ2cXdVozn9BKl1WuDPryFy-w8t4x0r3-LXhr5s-NsGQ8XYHXdzqb-RDHOcF-4jSkLItv55VmU9n6_FkKfm8Xga7XEQfcyr5exrNXgMfgqmSFFgM0t78hbgwq2bESKqrkajqPdb3SgJrvr6qGmv9Im-ujuP_un7YYtFUTZo12wyqfoPhfFOzg4IilJRtvexvqdT_GA-i5Qs0JCnrgvE50wtZg3WIxaPb25L_St5k5NUl8bg5MG_vFgEVjNdzZhdpb5xmV_vUBAYkr2uMbwlarwPvYBeDkrn4TU9J6RzYcRZq44958e5ftdyAqWGbWfiXqE6MI5uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای مضحک نتانیاهوی خیال‌باف: اکثریت  مردم ایران، اسرائیل را تحسین می‌کنند #Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/678122" target="_blank">📅 18:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678121">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a25ac02ca5.mp4?token=Ur16-GSvf609-JeQj-jAvj14QHVj2zip27U5Z8vlvG56CrG3Kd39nliTLaDjxGfJ0hItZNiegU5Jm3H24b46Pnc10JZzX3i6WxhEdFqpyrbc91CEAfnlAm1PYuMzY5LOVKggK85dAxYDcPOpRxuqu-RBuHeWMvFQQyv-Ifv6D69egkxbA9WSvichzhVhgs8hjPf0aoaDDXhXvTa3P7zxv64tTqm1W5kaI5gAfVoJeTIOygnui5VzNsmvROXgUg_OukmNe2LjMdCzauCbBrvx-a3Dd3hN3R1_n8aAzFGbiroJQuiMq0IqV22yu-2ZXszP4gZVVuTGxHpMTTdbbN9wSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a25ac02ca5.mp4?token=Ur16-GSvf609-JeQj-jAvj14QHVj2zip27U5Z8vlvG56CrG3Kd39nliTLaDjxGfJ0hItZNiegU5Jm3H24b46Pnc10JZzX3i6WxhEdFqpyrbc91CEAfnlAm1PYuMzY5LOVKggK85dAxYDcPOpRxuqu-RBuHeWMvFQQyv-Ifv6D69egkxbA9WSvichzhVhgs8hjPf0aoaDDXhXvTa3P7zxv64tTqm1W5kaI5gAfVoJeTIOygnui5VzNsmvROXgUg_OukmNe2LjMdCzauCbBrvx-a3Dd3hN3R1_n8aAzFGbiroJQuiMq0IqV22yu-2ZXszP4gZVVuTGxHpMTTdbbN9wSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری و تحلیلگر سیاسی آمریکایی: آمریکا نمی‌تواند از ۵۰ هزار نیروی زمینی خود در منطقه محافظت کند چون موشک دفاعی‌اش تمام شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/678121" target="_blank">📅 18:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678120">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORBKVVuYrbILwLlBJHJujcE0xl6e98IhoQ7FAPG6veLHSxYYA-2FFjNDTH-xp5cswaMKTraWT3QzRNOMwNnoguiVYDA3pefmHVC-w9IWxRanBqjbx7pQzHHx8zHdSUFCAtv6CATJLbIAJ27YcxCkLCLcUOW92ej02ko0DiycTVSFCCnzHz6MJbrvuB1ZWq8MW6bJGwPtqbl5FJ-es_tDH-npAuw3uaUULxQUJ4yRf6YuWIFE32J8-CEvJlevTjRD_US73kKEgRMOonPxa18IMlK3wrWPdUcNYwB8VFklUVvjGnAPeqATC9k4BgJcq_GGzo5QTNxPUUcyPJgCPX0O8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایده غیرمتعارف برای حمله به ایران | پنتاگون در جست‌وجوی گزینه‌های تازه برای فشار بر ایران
🔹
گزارش اختصاصی سی‌ان‌ان از درخواست فرماندهی مرکزی ارتش آمریکا، سنتکام، برای ارائه ایده‌های «خلاقانه و غیرمتعارف» به‌منظور افزایش فشار بر ایران خبر می‌دهد؛ درخواستی که به گفته منابع آگاه، بازتاب‌دهنده دشواری واشنگتن در یافتن راهی برای پیشبرد اهداف خود در رویارویی جاری با تهران است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3235318</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/678120" target="_blank">📅 18:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678119">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b886a5807.mp4?token=aaI-Nx_QgZ84BmRJaKsBEkexD4lfpx4ViGeKKvY55iG2FRrhOZVBWyOMyfmzIYMenrDyOwwdxBvotQ9un3SXlHqwX3fJuV7FDqEEinnWeTotoKEfXfau0khgs8MAoHn5gbcXGwTkbayI7oCIjmy_UI5q4w2I2UfiX18QfXP63pbjSg8X-IYdk5NPKF1Eh-8O6go2bYvOc5Mu3C2VQ-LiVZmHbIncPIPrCUPv8AJSpfiMfsZ5jcNTW4W6f46_LYsp_1oPrOddQb8ncfvTsdYfONRXGZonG_QH1ZGd3183ocVN3YzW5fbUfFbrNffBLEP97sx6F9aUZi25yvQj__YD9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b886a5807.mp4?token=aaI-Nx_QgZ84BmRJaKsBEkexD4lfpx4ViGeKKvY55iG2FRrhOZVBWyOMyfmzIYMenrDyOwwdxBvotQ9un3SXlHqwX3fJuV7FDqEEinnWeTotoKEfXfau0khgs8MAoHn5gbcXGwTkbayI7oCIjmy_UI5q4w2I2UfiX18QfXP63pbjSg8X-IYdk5NPKF1Eh-8O6go2bYvOc5Mu3C2VQ-LiVZmHbIncPIPrCUPv8AJSpfiMfsZ5jcNTW4W6f46_LYsp_1oPrOddQb8ncfvTsdYfONRXGZonG_QH1ZGd3183ocVN3YzW5fbUfFbrNffBLEP97sx6F9aUZi25yvQj__YD9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری | به نیابت از رهبر در مسیر اربعین
🔹
صدای زائرانی که در مسیر پیاده‌روی اربعین، ارادت خود را به «رهبر شهید» با قدم‌هایشان نشان دادند.
🔸
پیام صوتی خود را ارسال کنید
👇
#زیارت_به_نیابت
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/678119" target="_blank">📅 18:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678118">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbgb5NsG1H7hMTEEw93hA_edXoHlG-_SlIs5Dd6eOdfEeWQYTekfgJ7G0NmufRL9yG2Gzuouj6OnZtdkyruHlVNix45PCKRPzslgOmxbAzBkWXwqAsSm6q2ExiOUARf2DBviAujnyL3EnJCiZrycIMgVxGSa5q8DH_7F7goT8AB_H7zaMoIYTU4qKD53TSjYJG-mszY4_WOvajHj_DuvjlvpTbVGrQ1f7A-Ru75DGyFTxhZQcBmfQOzsAnszxnrvDTYOtbp4Tvnkck8j_zpKezYkKtTpef-jnIgBwdugNBhZX7mQ2j3HCW6CCnamEZQWayPN_kJjgzsbu5I4MbubzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر جای بدنت یه علامت داره؛ کمبود ویتامین‌هات رو لو می‌ده!
💊
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/678118" target="_blank">📅 18:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678117">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ageWgMSaHM8-EwtASLoc8YAjr0EkSfMwHAe7F-TkWJALZZP7heL35ezw1885ZdQ6QpgRnLaZmtfEiO97BxnhtLRYABKi-dvydmgPTAkWin7Yb0oc9cQD94B6JnIzvVzRfiYm52KkFp1DLx4aY4dbOWpQOU08tVlSfCFIZp5TYI-efqxORlt3Z6Zy9zF1c_DM8oVDmceZn4dftN4lWYPtbXoq3lzhibFpzJ5RTIPV8KLJXbYku63xYIyUFjVzntoGW7mfAhO_HYbrmotfLhIBBkwdT8BK02qcS5VCYIfrld5sCc1cPULZxMjubDdNvZVcRwJi23bwSKRk-SgkbEuzyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صنایع خلاق؛ پیشران جدید رشد اقتصادی در عصر اقتصاد توجه
🔹
نشست تخصصی «بررسی ظرفیت‌های تأمین مالی و صادراتی وزارت ارتباطات و فناوری اطلاعات در حوزه صنایع فرهنگی و خلاق» با حضور سید صادق پژمان، مدیرعامل مؤسسه کمک به توسعه فرهنگ و هنر، حسن میثمی، مدیرکل توسعه و فناوری‌های نوین و تحول دیجیتال وزارت ارتباطات، حامد لدنی، مدیرکل دفتر راهبری طرح‌های کلان فناورانه وزارت ارتباطات و جمعی از فعالان و مدیران کسب‌وکارهای خلاق برگزار شد. در این نشست، توسعه زیرساخت‌های تأمین مالی، حمایت از صادرات، تقویت تولید محتوای دیجیتال و گسترش همکاری میان وزارت ارتباطات و زیست‌بوم صنایع فرهنگی و خلاق مورد بررسی قرار گرفت.
🔹
سید صادق پژمان در این نشست با تأکید بر اینکه اقتصاد آینده، «اقتصاد توجه» است، گفت: «در دنیایی که مهم‌ترین رقابت میان کشورها و کسب‌وکارها بر سر جلب و حفظ توجه مخاطبان شکل گرفته، صنایع فرهنگی و خلاق به یکی از مهم‌ترین ابزارهای خلق ارزش اقتصادی، توسعه نفوذ فرهنگی و افزایش صادرات غیرنفتی تبدیل شده‌اند. ایران با برخورداری از پیشینه تمدنی، سرمایه انسانی خلاق و ظرفیت‌های گسترده فرهنگی، از مزیت‌های قابل توجهی برای حضور در این اقتصاد برخوردار است؛ اما تحقق این ظرفیت، مستلزم تغییر نگاه سیاست‌گذاری، توسعه زیرساخت‌های تأمین مالی، تقویت نظام مالکیت فکری و حمایت هدفمند از کسب‌وکارهای خلاق است تا اقتصاد فرهنگ بتواند به یکی از پیشران‌های اصلی رشد اقتصادی کشور تبدیل شود و برای این هدف نیازمند همکاری و هم‌افزایی بین دستگاهی هستیم.
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/678117" target="_blank">📅 18:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678116">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔻
ماجرای سیا ساکتی و صندلی کودک!
🔹
صندلی کودک، فقط یک وسیله اضافه نیست؛ «کمربند امنیت» فرشته‌ کوچک زندگی شماست.
#سیا_ساکتی
#راهنمایی_و_رانندگی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/678116" target="_blank">📅 18:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678115">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95ec6b5082.mp4?token=H7fTFWcIUoo4N40UWLIzqIIjCXYyj9z_o6rqr3SrlXQ5CSuQoPTDRJktvoNUDdEG78SgdLr4BcH8-VzzYiNA5bk0Hrr7E5eBWU4d_ZuoOAUTozShKG6H3trsUSVKLiOZlt4_jIINgK6wW0zi2iWwCwWX5RJCE6KY2u00JNGgZ9UXTt_-dlXWzQb9EnXGhmuFLqsA7Itsbpvl5IrBu7ZAJc-WqmG4-3oJYbVgoQatPf-g6eqRaDxVqyjqW6JT2oYiuM6v0Dn_mdkKkXuukVMADcN-ohDYRQj6r9YN1QsTcmgdZHpu3CzDl8j4WDlIjT71BYs7CRTEc1yUHcafyqr0VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95ec6b5082.mp4?token=H7fTFWcIUoo4N40UWLIzqIIjCXYyj9z_o6rqr3SrlXQ5CSuQoPTDRJktvoNUDdEG78SgdLr4BcH8-VzzYiNA5bk0Hrr7E5eBWU4d_ZuoOAUTozShKG6H3trsUSVKLiOZlt4_jIINgK6wW0zi2iWwCwWX5RJCE6KY2u00JNGgZ9UXTt_-dlXWzQb9EnXGhmuFLqsA7Itsbpvl5IrBu7ZAJc-WqmG4-3oJYbVgoQatPf-g6eqRaDxVqyjqW6JT2oYiuM6v0Dn_mdkKkXuukVMADcN-ohDYRQj6r9YN1QsTcmgdZHpu3CzDl8j4WDlIjT71BYs7CRTEc1yUHcafyqr0VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای مضحک نتانیاهوی خیال‌باف: اکثریت  مردم ایران، اسرائیل را تحسین می‌کنند
#Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/678115" target="_blank">📅 18:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678114">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
وزیر کشور پاکستان به‌زودی به تهران سفر می‌کند  منابع آگاه پاکستانی:
🔹
وزیر کشور پاکستان قصد دارد ظرف یک یا ۲ روز آینده به ایران سفر کند.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/678114" target="_blank">📅 18:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678113">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5466c4816.mp4?token=HNiuoswXUJJlD90funrwe_xhsXeqDhpsWpqf4qdhgRaZsQHe3iT-sPozZ3TZy8jizvwvQtYQ3yOFXjWG7KKMIdcLhs2D7Le61sXwjA0f3TmbM58l2cZMdxnrpnZf7lf4_KjW4FHIwe1VFQuBepLgTHzINeuF6-k2UXMS_V9FgDT7q5TZnmajRZmSoKx2cFDpiTLuvoduiPnP-1fgLHC9-DF8cUF-O3bbp7VLtX6DensZxv_kWg0CaQa_Wnfun6bZQvitVUpWINbEL49A5X1kbX8kQULEOCJzwekHa_H3AiOsLlUvPh8OixJdUpWbZ-ozkBZpTXv8GaB4soQONy7Pdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5466c4816.mp4?token=HNiuoswXUJJlD90funrwe_xhsXeqDhpsWpqf4qdhgRaZsQHe3iT-sPozZ3TZy8jizvwvQtYQ3yOFXjWG7KKMIdcLhs2D7Le61sXwjA0f3TmbM58l2cZMdxnrpnZf7lf4_KjW4FHIwe1VFQuBepLgTHzINeuF6-k2UXMS_V9FgDT7q5TZnmajRZmSoKx2cFDpiTLuvoduiPnP-1fgLHC9-DF8cUF-O3bbp7VLtX6DensZxv_kWg0CaQa_Wnfun6bZQvitVUpWINbEL49A5X1kbX8kQULEOCJzwekHa_H3AiOsLlUvPh8OixJdUpWbZ-ozkBZpTXv8GaB4soQONy7Pdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
السلام ای شاه مظلوم و غریب
السلام ای آیه ی امن یجیب
السلام ای نور چشم مصطفی
السلام ای خامس آل عبا
فرا رسیدن اربعین حسینی تسلیت باد
🏴
🖤
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/678113" target="_blank">📅 18:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678112">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
وزارت خارجه پاکستان: وزیر امور خارجه از عراقچی دعوت کرد در کوتاه‌ترین زمان ممکن به پاکستان سفر کند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/678112" target="_blank">📅 18:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678111">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
بیکاری ۴۵۰ هزار نفر در جنگ تحمیلی سوم و محاصره اقتصادی
🔹
بهار ۱۴۰۵، نرخ مشارکت اقتصادی ۴۰/۷ درصد، تعداد شاغلان ۴۵۰ هزار نفر کاهش، نرخ بیکاری ۹/۱ درصد (رشد ۱/۸ درصدی).
🔹
بیشترین بیکاری: کرمانشاه، خوزستان، بوشهر؛ کمترین بیکاری: خراسان جنوبی، زنجان، مازندران. بیکاری در ۲۱ استان افزایش یافته است./ جریان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/678111" target="_blank">📅 18:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678109">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E7eWNDaLRqct5BlsA56U6mR7IrXXVX_uEg8D85bFfC4eEGEa3MnL-5VrI1a8ZP9q0Oy0tPI5lB_kl1I7S9wS4rdfObdbWJ7gwLyvvMB77NtI99OHOi-oF49RqJmBXiSdAWyPpOUXGfJEvdzrmf613HmeRt8diYkN0ooAcoybSK3Xq2nlkDfiuKM5fqYZpnhmtUL242Cfqsl-_-fNm73P-mkT-wf7ea3ZDYQLkEUiSwlnZyMYpv6VQqoieQu7gEn4yE6g_BGISN2G7TPtPs_X-aqYZzMSOCzQhXOCAvgmqY_QDVPk4NcvdX9dPxYATQQ0OqB77h_Hn-4Ov9T5a27G3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uzG18SaRd-XVh61lrGUL99xqUmJHuJ40mVec33zPJuWf8ncYJeLUmLq7mXd6-WJ5r-3Y3lQ_5edzmqAUUP7HSCNqv4dy6vMzWFTR9UOG111GTmDNycthuB72A_XTkawC5UnxbI2EBPtAw8PRk6wq-PNitJZA9QTcR-wXN88oYjXdjClgrBBnilBgI4E4jggDFzxoxuTrol-s3-aCUj_-rhnTbNa8IiT-FD6LbZJrXQjuOChkVYSvQkcAQkLLTmUPoU4ycw7B87_qOnmfX7TUSpe51lqc-_8P_tkA8btdGoeh-ZP3laYUCVqWzC3miP33hsLFkkw85hxCRp9Ez08f6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر کشور چقدر برای توسعه هوش مصنوعی آماده است؟
بر اساس آمار، دولت آمریکا با امتیاز ۸۸.۳ از ۱۰۰ بیشترین آمادگی را برای توسعه هوش مصنوعی دارد و پس از آن، کشورهای فرانسه و بریتانیا در رتبه‌های بعدی قرار گرفته‌اند.
ایران با امتیاز ۴۸.۴ در رتبه ۷۶ جهان قرار دارد و کشورهای عربستان و امارات پیشتازان منطقه در این زمینه هستند.
نکته قابل توجه این است که ایران در مؤلفه «ظرفیت سیاست‌گذاری» با امتیاز ۸۴.۵ وضعیت مناسبی دارد، اما در بخش «توسعه عملی هوش مصنوعی» امتیاز ۳۷.۶ را به خود اختصاص داده است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/678109" target="_blank">📅 18:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678108">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
جدیدترین روش پایین آوردن قیمت نفت: التماس سگ زرد به شرکت‌های نفتی
ترامپ:
🔹
«قیمت‌های نفت مصرفی خود را فوراً پایین بیاورید، همین حالا!
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/678108" target="_blank">📅 18:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678107">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
اعتراف بی‌سابقه در پخش زنده: ما کشورهای حاشیه خلیج فارس آلت دستیم، اختیاری از خود نداریم!
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عربی دنبال کنید
👇
@AkhbareFori_Ar</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/678107" target="_blank">📅 18:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678106">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNnpTC9LfUH3RM60Et8itoRy1DZ62d_qYwyWiS9MrNSsUAaR8FsnnUhrHxjIK7MLr4ktyCFMOyuF7r4NZNIqeWGFyRFk5DktXSEYehkv8WwqQP-VkSaKmnm7zulScE6iZEaSBU9FDiLZhWERYa_EmGM-IrBo_fxo2R9yTuf_BWHHgK6O8iPVVT3RSpKwnEhavkj64pA97b2NpQ_to6ri38KL_O0t4tyoeWWu2oEdvQp9BBAwCAgEewQIcvkzjLvbC4pF-K3PEJqvmC6mbAYdcCn_ZchC8Bj8PAc4NdMP7qo5-DZNwEpbqeBHQWCMlJvkfFz_9jy1AT61kUbKSAUWag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طلا یا دلار؟ کدام یک پس انداز بهتری بوده است؟
برخلاف ارزهای خارجی هر سال به دلایل تورمی داخلی کشورها بخشی از ارزش خود را از دست میدهند، در سمت مقابل به دلیل تغییرات قیمت جهانی طلا میتواند رشد دلاری هم داشته باشد.
در سال های اخیر، صندوق های طلا ابزاری مطمئنی بودند که زیر نظر سازمان بورس فعالیت میکنند و امنیت بالاتری از حفظ دارایی های طلا در خانه دارند. یکی از گزینه های مطمئن، صندوق
#جام_طلا
هست که میتوان به آسانی تنها با چند کلیک آن را خرید و فروش کرد. برای تحقیق و بررسی های بیشتر میتوانید از این لینک استفاده کنید.
خرید آسان طلا</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/678106" target="_blank">📅 18:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678105">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
وزارت خارجه پاکستان: وزیر امور خارجه از عراقچی دعوت کرد در کوتاه‌ترین زمان ممکن به پاکستان سفر کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/678105" target="_blank">📅 18:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678104">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_n5_SGJ2GrkP4QWQrYp7PhwI9Jh9vLDukYpy8rAZaIGRuRD9fhdkyXcHnQUrrblV2xTCr2q5IUYA5O_6NYSssmh_3kapDJzcgE9HdBWadEOLFlnAJIhvKXxSgUHJsHVIJxWKhlfbmdlRu_wmRJkKdV28y-YlJvwunhFi_0jXnuN1b6xIhjid5J26spcAqA-B2E8gDxzunDYjvnBAk7KwNmmaIyYUh8oQzkD6B71sFgU05yXAgfFFP5i0eHu7S4vABsEeqSVY_CUldTVzCDyRyUnP5z4AG1zzQixBnO1hJgK4EF5RAzJ5-0BZ4OhFfgie6VixnQeJkCVxUGvFJSGLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
♦️
بالاخره اسرائیل نابود می‌شود!
تصویری دیده نشده از رهبر آزادیخواهان جهان، حضرت آیت‌الله سیدمجتبی خامنه‌ای
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/678104" target="_blank">📅 18:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678103">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFUt9yZAd6CDy0siPdLTNH3Biaa9jYU4bopBOhent4m3J2TKq04EgQfOrG_y8dw5BN0LVZWZoGYEU-76D_0uX8BQQHYOGGMPUI2IlPRK5BpAXR6lpeIR-_dcv3UDx_kJDxuHA56ah0VTgH0d_dAno9yevtXIgA6WQjMk32AnlgBHsskigwBrGyomyZKRwcpKqDZ373UdoVj5U3nLp16h3QON5sV1avRDno4IFrVjdasx7x5xjXDcpLY8RUdRLwbwlNJyBmf4uLsiFAOBRqXOFbqHrQrADLAA_Lnszo0Yr0CuMSPN2HtjvlENF4RviolGdZl0Jd9KgPE2M2-sKxK37A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک تایمز:
ر
ئیس‌جمهور آمریکا صرفاً در حال سبک‌سنگین کردن و بررسی گزینه‌هایی است که هیچ‌یک برای او مطلوب و ایده‌آل نیستند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/678103" target="_blank">📅 18:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678102">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPfaKJ3h6hlx6a83ZezhNOLEiRCZkM3rrJj8vbx36IRrD3XnjcNjC6eerw2qxTm2cGRSEWu3UGDTuQPgViEkxVUNxjdw-dUkB3MBEK9xLTNJTDQOJyEYD_5ZmcR0B7mgMx8cTZ9SnjwqUiULGvrFrtFCt03hYzSY2ZaULs4nNs4rArJs8S1G1yRW7B9XURF6nIS5gU_pMmt_dkm3N8Z7x_hhyplEfgG5xHubVpmKgSAFn34KcdY211xpA3xcHb9XnXUUKVMNm_I-MfXHb9bBYcg7x0MuF4q9tMCILMOzlBU1LyKyjV34EtcOsVz6puIyORoSSCkqGL9Z7nobPY1d3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمانروایی که از دل آشوب برخاست؛ نادرشاه افشار
🔹
نادرشاه یکی از برجسته‌ترین فرماندهان تاریخ ایران بود؛ مردی که با قدرت نظامی، تدبیر و لشکرکشی‌های گسترده، بخش بزرگی از سرزمین‌های ازدست‌رفته ایران را بازپس گرفت و دودمان افشاریه را بنیان گذاشت.  رویدادهای…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/678102" target="_blank">📅 18:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678101">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/678101" target="_blank">📅 18:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678100">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
انفجار کپسول گاز در دبی با ۱ کشته و ۵ زخمی به همراه داشت
🔹
ادعای سفیر آمریکا در ناتو: در حال حاضر ما دیپلماسی و مذاکره را انتخاب می‌کنیم
🔹
سخنگوی وزارت امور خارجه سوئیس: با ایران و آمریکا در خصوص مذاکرات احتمالی در تماسیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/678100" target="_blank">📅 17:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678099">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
برخی منابع عربی از شنیده شدن صدای انفجار در امارات متحده عربی خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/678099" target="_blank">📅 17:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678098">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f75305259.mp4?token=DQO8f6m02wxeTjc-dS63k-HN1_Z2sd3dzdvTa4YRwCDdW6jzFROM-brrFa_Obqwhn0lyvo8Yra8yms2QmLS4tBxPoKqEDehvsrElqveejCiRWrlozWQtXm2spAcKnTcvZPTHlBtq2YlnBZQsMwdnzkd45cHxqeGkMgKXTRYPp4KXiVQY8Y5gR67nBx5XDrAc9KE8CQkRLjWqyjkQUBXP3kr76aGs8zZAeD0eBfi4XIUQlMGJXssz6Gjq2BN225dCqlLs0ald3-VxkuhnHSfU25Oh-6Cm-i2QaeFpw90SNCHThDU9of72SfMhR6OmN1ZNTljZFe7cYPNJZyrOsTgcuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f75305259.mp4?token=DQO8f6m02wxeTjc-dS63k-HN1_Z2sd3dzdvTa4YRwCDdW6jzFROM-brrFa_Obqwhn0lyvo8Yra8yms2QmLS4tBxPoKqEDehvsrElqveejCiRWrlozWQtXm2spAcKnTcvZPTHlBtq2YlnBZQsMwdnzkd45cHxqeGkMgKXTRYPp4KXiVQY8Y5gR67nBx5XDrAc9KE8CQkRLjWqyjkQUBXP3kr76aGs8zZAeD0eBfi4XIUQlMGJXssz6Gjq2BN225dCqlLs0ald3-VxkuhnHSfU25Oh-6Cm-i2QaeFpw90SNCHThDU9of72SfMhR6OmN1ZNTljZFe7cYPNJZyrOsTgcuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚗
هر آقایی یکی از این جاروها توی ماشینش نیاز داره
👨‍🔧
🎥
برای دیدن کاراییش ویدیو رو حتما ببین
❗️
✅
سه روز ضمانت بازگشت
🏠
پرداخت درب منزل
تعداد محدود! همین الان کلیک کن روی لینک زیر،
تخفیف ویژه
رو دریافت کن
👇
khabarfouritel.affdn.com/lead/44273
➖
➖
➖
➖
➖
➖
➖
➖
➖
5000 محصول تخفیفی دیگر
👇
khabarfouritel.affdn.com</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/678098" target="_blank">📅 17:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678097">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0geMGIEh1G8ETTKnAArdBkzTjAuMMINHswIjg7QICS2chY1xdO4Cu2W2sfAk57R2F2a-8akUSj899HJnzr_BhnulF1PqhHAt8ZltNV1-KdMkXtUCKFIziVC6LuXqhDKZwB-9iUfO2477YN7ALrZnBJ0zjuPGgOv3LIKsnfe5T0bMKmu_UpfizmhZ88r70QqQmm_0wvB5CEUeLd_BiVNPtCdRHZwbTgVTFXzHstXvcdomO-g_w-mxB-s3y9hGViQ--FvITx27YDH_DVTysLuZlfbO6wyiaNaQljylUwMrlIWLLsEPgnJ1d3qh0gwjubStP8IeiwMCp_lvE_Yg_lzlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت مژده لواسانی از اولین زیارت اربعین مادران داغدیده میناب؛ روایتی از دل‌هایی که سوخت
🔹
مژده لواسانی از روایت مستندی با حضور خانواده‌های شهدای جنگ رمضان خبر داد که اولین زیارت و اربعین آنها پس از شهادت فرزندانشان محسوب می‌شد.
🔹
لواسانی درباره روایت این مستند عنوان کرد: من هر ساله در اربعین حضور دارم و معمولا برنامه‌ای برای اجرا به من پیشنهاد می‌شود که همیشه استقبال کرده ام. اما امسال به دلیل ماهیت گفتگومحور و متفاوت این مستند، اتفاق بسیار ویژه ای برایم بود. به نظرم الگوهای تکراری مانند حضور چهره‌ها و مهمانان معروف کلیشه‌ای شده است، اما این فضا همچنان بکر و تازه بود و خود من نیز از آن تأثیر عمیقی گرفتم.
🔹
مستند راویان پرچم سرخ به زودی از شبکه یک پخش می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/678097" target="_blank">📅 17:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678096">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
آکسیوس به نقل از یک مطلع: نماینده ارشد شورای صلح و مشاور این شورا امروز با نتانیاهو دیدار کرده و به او ابلاغ کردند که باید حملات به غزه متوقف شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/678096" target="_blank">📅 17:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678095">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/069f15d0bb.mp4?token=Ska2EqK5tWie-3eSgkGj6gXusKIgFg3zNdig7J4HaXS2tu10XG-IEBC-YSUDylrRaKbwnKTFXIR7fhc_dKcJKeXsANPDqqNZWEm8VNUO6f1tPGnqIJqsKO3EP3AZW61r5hkeSirHOnBkos712KXW-1-W3qiA6r8q2_BB_o-2odrqZHXvIcIE5DNtk7qpnSNzuv2BW4vB1tN5kEUKmb3EOC7B76xka87SpOV5b--5NOQlLaYGtfc5LnH6SXq2c-X0WtWbDDHHbkg4qv2ysNAqagDV1JvYN62i7VWQ_omOePXqU7uwXp4MX8EMZuU5t9K61AbBphj3J6wwgZ0VZQN8qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/069f15d0bb.mp4?token=Ska2EqK5tWie-3eSgkGj6gXusKIgFg3zNdig7J4HaXS2tu10XG-IEBC-YSUDylrRaKbwnKTFXIR7fhc_dKcJKeXsANPDqqNZWEm8VNUO6f1tPGnqIJqsKO3EP3AZW61r5hkeSirHOnBkos712KXW-1-W3qiA6r8q2_BB_o-2odrqZHXvIcIE5DNtk7qpnSNzuv2BW4vB1tN5kEUKmb3EOC7B76xka87SpOV5b--5NOQlLaYGtfc5LnH6SXq2c-X0WtWbDDHHbkg4qv2ysNAqagDV1JvYN62i7VWQ_omOePXqU7uwXp4MX8EMZuU5t9K61AbBphj3J6wwgZ0VZQN8qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عاشقانه‌ای از جنس فلز و سیلیکون؛ اولین ازدواج ربات‌ها در دبی!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/678095" target="_blank">📅 17:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678094">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
سی‌ان‌ان: سنتکام برای مقابله با مقاومت ایران ایده کم آورد
🔹
شبکه سی‌ان‌ان به نقل از منابع آگاه گزارش داد فرماندهی مرکزی نیروهای تروریستی آمریکا در یک ایمیل به تحلیلگران نظامی از آن‌ها خواسته است برای آنچه «مقابله خلاقانه و غیرمتعارف» با ایران خوانده شده است، راهکار ارائه دهند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/678094" target="_blank">📅 17:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678093">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7hecKzL5HZyJblfWMFNcjCKeqEuQvQCRgUXh2zb4lYClIvR0QPbPfdWCR1zbN2VBvOcp9xJnNXVgbfPE3HEyPndYktZhcAaSRicIgiPa65Nl6Pgj2zQNHrfQay3WSgUp5vNVRr6FgeFiweoDmNMqKUzw1_kS40MUeoLgXhnOc9kOia-TsFSBBnh_TECaGgA3sQGAif21vjR2IMfbch2bg2hv9XqRvr1zb5zeAUMXf8M1or7abBxlJ4LSmhcl_uKETGXS2W7SRo0iv21HPGhJbWTN1JqpXaMydiSxHA5yy_LwqrIJXi5tFpjgEIyeh1EqZHP3Jg5KXoPKR9YF855VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیست هزینه‌های ساختمان که هر مالک و مستاجری باید بدانند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/678093" target="_blank">📅 17:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678092">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
تیزر قسمت بیستم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای علی لعل یوسف که با خوردن یک آبمیوه مسموم، روح از جسم ایشان جدا شده و توسط یک دست قدرتمند آمیخته با خشم و مهربانی به سمت بالا می‌رود و در آنجا آیه‌های قرآن را به تکرار شنیده و اینکه مهم‌ترین اصل آفرینش افراد در همه ادیان الهی، انسان بودن و زندگی انسانی قابل قبول درگاه خداوند است را درک کرده و بخاطر کارهای نیک و بد دنیوی‌اش پاسخگو میشود را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: علی لعل یوسف
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/678092" target="_blank">📅 17:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678091">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
نمایش بنر منقش به ابرمرد شهید تاریخ در بین‌الحرمین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/678091" target="_blank">📅 17:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678090">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fp8iE47rDGKBxbkD9LRFbamWUs9bo0k430iucY1T1IjKw1OyYpjUtec6lkaQIPAxX27A2jQGXtSvZd9n8FiQDs0KlEVefYU6b_VUmKqz_gEejYeM_I3ZpHsz9_SIGOF-P8MccZOLDjiDJVihThS69-bZJuhvKN86i-TLiFWN6IcGAGr7yh3i6MM9uHa0wY6Wtn5kJS8qumzn7YpzCrSn5stKYIebTqb_Qd9jcElrWlVLIJux6GbbJhbSJsXWxc9xHsxmHkrD16bPTR9hAWEiwL0xVahQ9oBk3BsIlLeL2YD1KQqhCDot4uvtaCm5FJwU-Rj6R6dVJSsfpNYynY7Fxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کمیسیون شوراها در مجلس: خدمات شهرداری تهران در اربعین رضایت‌بخش بود
🔹
سخنگوی کمیسیون امور داخلی کشور و شوراها در مجلس در ارزیابی اقدامات شهرداری تهران، بیان کرد: شهرداری تهران در مراسم‌های مختلف، از جمله تشییع پیکر رهبر انقلاب، عملکرد بسیار خوبی داشت که جای تقدیر و تشکر از همه کارکنان این مجموعه دارد. واقعاً خدمات ارائه‌شده بی‌نظیر بود و آن چیزی که نیاز بود، تا حد امکان انجام شد.
🔹
بیاتی درباره نقش شهرداری تهران در خنثی‌سازی جنگ رسانه‌ای دشمن نیز گفت: دشمن در کنار جنگ نظامی، جنگ رسانه‌ای را نیز به راه انداخته است و موفقیت‌هایی را که ندارند، بزرگ‌نمایی می‌کنند. البته در میدان عمل دیده می‌شود که شهرداری و دیگر مدیران حکومتی ما به بهترین شکل در حال تلاش و کار هستند.
🔹
وی همچنین عملکرد شهرداری تهران در خدمات‌رسانی، برگزاری مراسم‌ها و فعالیت‌های فرهنگی مرتبط با اربعین را مثبت ارزیابی کرد و از تلاش کارکنان این مجموعه قدردانی کرد./ مهر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/678090" target="_blank">📅 17:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678089">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8HDegnBjK6xrw1ChuBygfOrZVPIYZ0LZoeFrTUcsBRT88YCPGdgO2QoYJvaLpBO-OedoZTrr8dAjVk6HASJcPiwr5rUHmyjBZrlgOrFfzkzzw8D7lZYt0LHfj4klT8fPwpTIzDymKL1SiqWr0B4yE9Gw7dPuJIqshCStOwp3mHWhVGuvVbBCmaj62tHeUrx8WYI4CvydPEFJO2QLNfPaHkWQ4vb7ux1-FAE8_ibmx9Be0-qllJMX0ozPmQsT_mKrdAc4mKHdbFVWtslSjE8SRdSt0BH9XwEt72kYv95l0-CwCfaAZS26pDdtMU60tvBpJ-xme8yE784Ni9FI-rcmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۲ عامل موساد اعدام شدند
🔹
امید بهزاد و پوریا صفوت، به جرم همکاری اطلاعاتی با رژیم صهیونیستی و ارسال مختصات و اطلاعات مراکز نظامی و امنیتی، بامداد امروز پس از طی مراحل قانونی و تأیید دیوان عالی کشور اعدام شدند.
🔹
این افراد در جریان جنگ رمضان و جنگ ۱۲ روزه…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/678089" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678088">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
به‌صدا درآمدن آژیرهای خطر در سفارت آمریکا واقع در منطقه سبز بغداد در مرکز عراق
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/678088" target="_blank">📅 17:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678087">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHVPcwFcHQFW0HikVTqm8D70WbYW8PcXK8TuEeRUsHNmJmYyQ_kP2PdlXOWtIbN4PibWD2rKl45P8w9OzvPT8gWojzZMJ7_4zmv-3KvgHDtIGaReiQOGNaoaABDAxlSrXrno1g3e3R_WYpC_Lmx_yndWbqqJ0MRXdhciRIsNM86GNTbm8JRkDWaFoKSVR_A6qGkMCO8w9YTo4HPUNjLvajo4XNc4_r6-wDXPgnrLrIUGxdYc67EA8lcdlqDuOkblXqTN2WKdUCqH-q5Rup86kNIFKfdo3rvrQ_EWtAvFZmLZf5GZSQUP_JsiC-oWAcesf41fWZFW1xZJjOVk1OL8AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هاآرتص: مشکل اصلی کاهش ذخایر موشک‌های رهگیر پدافندی است که سریع‌تر از تولید جایگزین می‌شوند. ادامه جنگ با ایران برای آمریکا و اسرائیل پرهزینه‌تر می‌شود و ترامپ این هزینه را فهمیده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/678087" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678086">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
ادعای سنتکام: نیروهایمان هوشیار و آماده هر مأموریتی‌اند و از کشتی‌های تجاری مایل به عبور از تنگه هرمز پشتیبانی می‌کنیم؛ از مه تاکنون به عبور هزار کشتی کمک کرده‌ایم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/678086" target="_blank">📅 17:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678085">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e43657be2.mp4?token=ogLrwhtuEtVunXwTHf2CoxFPmxAhk1Wu7nWb7eLPWX8pC62hXjJIuuaIGhMdhoXVztfYneLS8yviGxioUy-MhOqBq8wtJnkaNwmVKp87SPbXGlAgco5yPnSsSvbk-JfnMURCTA9rufqJjCDOOKfqcOJAZIIYHuXHuRYq4orMlbr9LTaKNaPO6idfHRhkkLN4vofeJynSW1b3BHEPEkn2_r6wnRy7AJccyBSrNAmztcF1U5YAPl9kn9GGf15r7TO8ZR9HFN3bMErSVKyl2a1rJwc3YDNBt4Cf5VK9fC4XsEPubFZ7EIMt4Etz2QDK2ygkSQZi3akKQw3DZwKR-2kzlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e43657be2.mp4?token=ogLrwhtuEtVunXwTHf2CoxFPmxAhk1Wu7nWb7eLPWX8pC62hXjJIuuaIGhMdhoXVztfYneLS8yviGxioUy-MhOqBq8wtJnkaNwmVKp87SPbXGlAgco5yPnSsSvbk-JfnMURCTA9rufqJjCDOOKfqcOJAZIIYHuXHuRYq4orMlbr9LTaKNaPO6idfHRhkkLN4vofeJynSW1b3BHEPEkn2_r6wnRy7AJccyBSrNAmztcF1U5YAPl9kn9GGf15r7TO8ZR9HFN3bMErSVKyl2a1rJwc3YDNBt4Cf5VK9fC4XsEPubFZ7EIMt4Etz2QDK2ygkSQZi3akKQw3DZwKR-2kzlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام شهاب مرادی در مستند راویان پرچم‌های سرخ: ایستادگی مقابل ظلم و دفاع از عزت مسلمانان، مسیر یاران امام حسین(ع) است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/678085" target="_blank">📅 17:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678084">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlxUoRSm0Uc8JxLABeXvzExPCg-QUDyX7LDXVC1OlFBofFI-KX8VANx_rOunsVJA6KtciUn2oJSlE-Ns-8KtyMakNa7je84jm9Y5lqlIRubBPtoeRKHgPX0giLxpYAhw4mrnn_FlP8y31jGQw1awSZzSq7gXGY2UamyQzNpk04QCEQZ3SHMW9N5wSw_CTyt0xE-ewOjFJ3cStRVN7IX2r3cfzvxoJk4lOY_zSH2wDDCmxTRG4hL21l4YhIhO17aQIP3T5UJemfvnVJYlzcT9rfrDZ9utgHnJs6J0C8r7jf5eUeCAqukOu1UaOTQUpDa9J-UKzz4JZnWnKC3TGF9X9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صفر تا صد ساخت پیج میلیونی اینستاگرام با هوش مصنوعی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/678084" target="_blank">📅 17:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678083">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
۶ نفتکش بزرگ سعودی در پی محاصره دریایی یمن، مسیر خود را تغییر داده و به‌جای عبور از باب‌المندب، مسیر جنوب قاره آفریقا را در پیش گرفتند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/678083" target="_blank">📅 17:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678082">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
المیادین: ایالات متحده در موضوع مربوط به بسته ماندن مسیر جنوبی در تنگه هرمز، امتیازی به ایران ارائه کرده است
المیادین به نقل از یک منبع ایرانی:
🔹
ایران در پاسخ به آخرین پیشنهاد آمریکا، با رد این پیشنهاد اعلام کرده است که تا پایان کامل جنگ، تنگه هرمز را باز نخواهد کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/678082" target="_blank">📅 16:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678081">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
بقایی: پاکستان میانجی‌گر ایران و آمریکا است/ میانجی‌گر جدیدی از جمله چین اضافه نشده  سخنگوی وزارت امور خارجه:
🔹
پاکستان میانجی‌گر مباحث مرتبط با ایران و آمریکا است. قطر هم در مواردی که لازم باشد کمک می‌کند.
🔹
ما با چین رابطه‌ای بسیار دوستانه و همکاری‌ای نزدیک…</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/678081" target="_blank">📅 16:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678080">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QaXu1ZRt7McGADIs0w96CCtYKvXmjG9q6_kdDyjATIWEOo83haI3XKXXl855ti3rj6vXkkiRvkFmp_43BP7QY0_Wifl8im4gPQ_7sZ5jlirbHHv2HlQzYq3caQCObChN5-O-banLq7Pqa7ceHjJZn-LENEovHat7xn8gP5i6HHLoTGGcf50ZDV5Xg8_57YGJ8-g-28q9o3gv-C0zeADlGIfn67m-csByx-H8g3Yu5fN9d33Bgkb2YxEP_9ar-5wFvsd0DbyJa3edd_EP_fBcNWcGJv7j4aMdEczzEVk9TSnN1Lv9eJ0f7mmCQtQRM-bH79Lbk-4IDLfgQ6gigywCRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از خفیف تا خطرناک؛ کبد چرب گرید ۱، ۲ و ۳ چه فرقی با هم دارن؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/678080" target="_blank">📅 16:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678079">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkRsxp94bNY6JU8X9MySi9Rsd8cHrFqPkXgMj_U4CUYK9NzMOrw3Vl2F_peXA6Hrod_kpeJecW_uCxabsQKejjRiS5IeW3wi1AyrlRv4mOdBQR_rgTVex-YpKqJzJfLjdr64WvnYFjfEsvu-4Yi0SE-Crcz6PD7MHEHMEmQcBnS5FiJpkcZ1vjIrh4mRYcRfyffG4if3IAn5ReF3SLUxUCIYhUSQDVskYT0gkrLY5pCqTlGZAFqa88XGsMUg-m0yXezeIfrDXuOqKNxXhgdPvlGPnT9FX4POm1IGwjZHAWb_AeTkn4cwVUMLBfU623uJNhEXDGR9nmSM7oLEeAxkaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
نمونه واقعی کاهش درصد چربی بدن با تزریق زیکورپا
روند ۱۷ هفته‌ای درمان آقای ۴۳ساله، در کلینیک ایرانیان
⏲️
در درمان چاقی، مهمه کاهش وزن بیشتر از چربی‌ اضافی بدن باشه و عضلات، تا حدامکان حفظ بشن.
این نمودار، نمونه‌ واقعی روند کاهش چربی مراجعه‌کننده عزیز با
آمپول لاغری زیکورپا
هست.
در کلینیک ایرانیان، پزشک بعد از آنالیز بدن، درمان با
زیکورپای عبیدی
را شروع و روند درمان را پایش می‌کند.
👨‍⚕️
برای دریافت
مشاوره رایگان پزشکی
، اقدام کنید.
کلینیک ایرانیان
مجهزترین کلینیک زیبایی و لاغری ایران و خاورمیانه</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/678079" target="_blank">📅 16:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678076">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
جان مرشایمر: ترامپ دچار سردرگمی و دست‌وپا زدن بی‌نتیجه شده
جان مرشایمر، دانشمند علوم سیاسی
:
🔹
ضربه اصلی و مهلک ما به ایران از ۲۸ فوریه تا ۸ آوریل به طول انجامید و با شکست مواجه شد
🔹
ایران برنده جنگ شده اما ترامپ از پذیرش این واقعیت سر باز می‌زند و در وضعیت فاجعه‌باری گرفتار شده/او هیچ راهبرد نظامی معقولی ندارد و فاقد هرگونه دکترین پیروزی است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/678076" target="_blank">📅 16:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678075">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
معاون اطلاع‌رسانی دفتر رئیس‌جمهور: در آستانۀ سومین سال ریاست‌جمهوری، گفت‌وگوی پزشکیان با مردم به‌زودی پخش خواهد شد.
🔹
توانیر: از هفته جاری در تمامی شهرک‌های صنعتی کشور محدودیت یک‌روزه برق اعمال می‌شود.
🔹
نتایج آزمون‌های ورودی سمپاد و نمونه دولتی هفته آینده منتشر می‌شود.
🔹
رئیس ستاد مرکزی اربعین: یک میلیون و ۱۰۰ هزار زائر ایرانی همچنان در عراق هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/678075" target="_blank">📅 16:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678074">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbnOoze-MqooJBEJk_FluCkjHppG_x00Rd-JDgrPigDImzGi1Aawi6hLG0o0Oy_ojFDO3AiEvsSFpXVKbJ_nwxUwqRiR-HejWUa6cJ7mWUQ42HA42FWlc1S_koIAiUSkhKXs-be-R5BCxSV8TofOANSpzksbvH0CsB8_Dp4YJuyMgmvLRj0avuV84C4-EZXGt8lOHnAerxt0PfOuzm_lQcw2g8VwqYqdiuXwVyr07mQSkyBCXjq2ZGfRyHEA9d2BoFRDrHVKkidfT3Q5X2ovrLlu4pcGCHzYGT5pESwA2dYeVdhGUTQN9Mft5ywxUh5XJfyU5UGf2V2dQfzca2M_nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هوش مصنوعی نقاشی‌های گمشده را پیدا می‌کند
🔹
یک چت‌بات هوش مصنوعی برای ردیابی آثار هنری غارت‌شده توسط نازی‌ها توسعه یافته است.
🔹
نازی‌ها بین سال‌های ۱۹۳۳ تا ۱۹۴۵ حدود ۶۵۰ هزار اثر هنری را سرقت یا به فروش اجباری وادار کردند.
🔹
محققان دانشگاه سانتا کلارا امیدوارند با این ابزار به شناسایی و بازگرداندن حدود ۱۰۰ هزار اثر مفقود کمک کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/678074" target="_blank">📅 16:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678073">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
پزشکیان: ایران خواهان گسترش تنش و ناامنی در منطقه نیست
رئیس‌جمهور:
🔹
ایران خواهان گسترش تنش و ناامنی در منطقه نیست، اما در دفاع از امنیت، منافع ملی و تمامیت ارضی کشور با تمام توان عمل خواهد کرد.
🔹
نگاه دولت به اداره کشور، نگاهی سلامت‌محور است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/678073" target="_blank">📅 16:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678072">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0607e9ae8.mp4?token=bOWBZZX30Oa1mu3c0vkBcffcu4X4zucDXfkO20f4_EwVQLCSzGO5sBPXWvuLfXqkcL3tqTM6KRXJ6S9Sm-jhbpqf_wfL1w-HOFVSdCh2xvEbGmXqL5W_w2BWvHbHbje2HfMs3MUpfEGZmSTsovHZ9603ZrcsACYDm1uU2sUnkTqeteUiVVpaz9PbWStO135dvcuQ88nRb97mxcMsG2MjfMafQw4Pghy3izysyuRQdD4qxoOKVwo-nqZn9IopJT501ocDOuxyJZQoyUUs8-RLq4-2HdgRKhnf1qnJGmLaJMT2Wx2DHvzWWrz5_mAkPBgP3CCSQ2-4jp3NFVxl4bLXGE1C9CuF-n3EB4mbJ-W593A-yWEL0u4kiQPAZMi74yGQkxVWbg5KTycVkgA71i35JBMWWFhyB0XpLtsOSBBczCKI2VgJ_RBYX9hb1eODSarBdZKwVEmjZeXicJ7SZDi9SgCFb_yLW0t6kiKt3SvFV1HVA_VcshR7_ndl-rbF98qKmtgiZCcMaOIvu7AD1r8mYG91g3yG6YLrbrFXZhuFuYxP2iNEOTcDQ7mRPh_lymNoMG7L17eCUkEsnN5RidhmySefRmd3Hqnyyjwcj088af6xAakVRSnovzBa1rUqTJN3k2-P-uPAJahkOWtcyQIvlDVsWUcu8cs239Kx5cvCoNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0607e9ae8.mp4?token=bOWBZZX30Oa1mu3c0vkBcffcu4X4zucDXfkO20f4_EwVQLCSzGO5sBPXWvuLfXqkcL3tqTM6KRXJ6S9Sm-jhbpqf_wfL1w-HOFVSdCh2xvEbGmXqL5W_w2BWvHbHbje2HfMs3MUpfEGZmSTsovHZ9603ZrcsACYDm1uU2sUnkTqeteUiVVpaz9PbWStO135dvcuQ88nRb97mxcMsG2MjfMafQw4Pghy3izysyuRQdD4qxoOKVwo-nqZn9IopJT501ocDOuxyJZQoyUUs8-RLq4-2HdgRKhnf1qnJGmLaJMT2Wx2DHvzWWrz5_mAkPBgP3CCSQ2-4jp3NFVxl4bLXGE1C9CuF-n3EB4mbJ-W593A-yWEL0u4kiQPAZMi74yGQkxVWbg5KTycVkgA71i35JBMWWFhyB0XpLtsOSBBczCKI2VgJ_RBYX9hb1eODSarBdZKwVEmjZeXicJ7SZDi9SgCFb_yLW0t6kiKt3SvFV1HVA_VcshR7_ndl-rbF98qKmtgiZCcMaOIvu7AD1r8mYG91g3yG6YLrbrFXZhuFuYxP2iNEOTcDQ7mRPh_lymNoMG7L17eCUkEsnN5RidhmySefRmd3Hqnyyjwcj088af6xAakVRSnovzBa1rUqTJN3k2-P-uPAJahkOWtcyQIvlDVsWUcu8cs239Kx5cvCoNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایتی کوتاه اما ماندگار از پیوند اربعین با یاد شهیدانی که امنیت و عزت این سرزمین را با خون خود رقم زدند؛ یادی که در مسیر کربلا هرگز فراموش نخواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/678072" target="_blank">📅 16:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678071">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVO_oXiVO19dbwBruR2Cn3dIWhObePzHLF7RGT0vrw3OetMZtg_oykr4Ab6eM4Rgp6B28V6C5un8RK0VJpmCWnruTVjF260Eh-efJC32aGBafsdVuf_ItfB8hRfMALx8nMlEEDRdZfA7ai8m7QLWBEaPmn-UMKRhr2U2Yi7xvyPqDxKAK8RX-9Se2mvVKa8ou_rV_uC2x5mXvK04ZqVSbC_7RPqigbqrL66tVdH4BpROsFkIKfAZMwzxMEj49kciRvnvgvD_OvR6sdU7e5HdWcG7akL7479fYWo9FZEkIJhTyOm5mjOA0WyDDu4ykfl-bs_tKyUEk-tHYtdGgNAF_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدام الگوهای مصرف نیازمند فرهنگ‌سازی‌اند؟
🔸
در این نظرسنجی بیش از ۳۲ هزار نفر شرکت کردند که سهم روبیکا ۵۶، تلگرام ۱۵ و بله حدود ۲۹ درصد بوده است.
🔸
به عقیده ۳۵٪ شرکت‌کنندگان، الگوی مصرف انرژی و از نظر ۱۶٪ نیز الگوی استفاده از رسانه و شبکه‌های اجتماعی در ایران نیاز به اصلاح و فرهنگ‌سازی دارد.
🔸
اصلاح الگوی مصرف و تقویت فرهنگ استفاده صحیح از منابع، یکی از مهم‌ترین پیش‌نیازهای توسعه پایدار و افزایش بهره‌وری در کشور است.
@amarfact</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/678071" target="_blank">📅 16:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678070">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
چیپ مغزی ایلان ماسک، ویلچر را با فکر حرکت می‌دهد
🔹
شرکت Neuralink ایلان ماسک قابلیت جدیدی رو به چیپ مغزیش اضافه کرده که به افراد دارای معلولیت حرکتی اجازه میده فقط با استفاده از سیگنال‌های مغزشون، ویلچر برقی رو کنترل و هدایت کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/678070" target="_blank">📅 16:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678069">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4f484d0e6.mp4?token=Mb79eRDeNRoPOdRUqipQzC8UlJgXR5K_Ts-mIjV7HhUPBNKgS2A1lMKCSeGrgnGp9vvScEdBheZ2uZDULn_ZWSpDOTCmr9hNCmbay0FiyQ7pRxZ5h_n-3ZKqP48wNOaX91eYXSOZsYOcPUhaqn2JuZZRsdkbMj5U2dGkukRz5Zxh3KXpyaUSiz5LduNnJ9MhCNvgr3TNwiB4lBmXq79Qe8Ge5LrPEg1HoJpJtV24us40550g-GlEiAg9dj05hmt7mOzjTguhoq7WACdPJhc8ta0xlHUY50-HUyUUvidiwiFbtyGiaY3iyKbSeukyH5PTOs5aqFhOZHiskE7ImXq0JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4f484d0e6.mp4?token=Mb79eRDeNRoPOdRUqipQzC8UlJgXR5K_Ts-mIjV7HhUPBNKgS2A1lMKCSeGrgnGp9vvScEdBheZ2uZDULn_ZWSpDOTCmr9hNCmbay0FiyQ7pRxZ5h_n-3ZKqP48wNOaX91eYXSOZsYOcPUhaqn2JuZZRsdkbMj5U2dGkukRz5Zxh3KXpyaUSiz5LduNnJ9MhCNvgr3TNwiB4lBmXq79Qe8Ge5LrPEg1HoJpJtV24us40550g-GlEiAg9dj05hmt7mOzjTguhoq7WACdPJhc8ta0xlHUY50-HUyUUvidiwiFbtyGiaY3iyKbSeukyH5PTOs5aqFhOZHiskE7ImXq0JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مزایای سرمایه‌گذاری در املاک دیجیتال در یک نگاه #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/678069" target="_blank">📅 16:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678068">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxePGyUODxay-RS4XJ6wYAeGyu7a6WHdNNPZAcfgkQWhYRAaBUrXbbj-rUK0uo1eUSvNDKAm-3ZmP6AJSxF1xEDq2MbY0dwFk8ZAGDqS0ryZlcop9DsihGn75FoflQHSXAbfT4ic5nw8J8NMyH0f-L5QExj1pnVr3ZDJqA64a0Ni-J0Xe3PDVPpvgtF_IUUY2FaZFjJu1iVNhh4g8vtm00nUkVtjCUcEoL6mMUzCZvQC3oYjDbyPAqOrzcwzdlAyHycftMdl958kq-jFj2cw9ICpegyr7Jyy683Bg-eCVQksUk0x5-k2LuI61K9UZaTuzXYb_9Xtp4xCILJZK0IlXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاسبی جدید با سهمیه اقامت برای واردات خودرو
🔹
با مجاز شدن واردات خودرو با ارز شخصی برای ایرانیان مقیم خارج، بازار خریدوفروش «سهمیه اقامت» داغ شده است.
🔹
قیمت این سهمیه‌ها از حدود ۲.۵ تا ۸ میلیارد تومان اعلام می‌شود. /خودرو یک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/678068" target="_blank">📅 15:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678067">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWdKWE6hm7OKtEOIsCk9JJ2o3RIzMCC4u6i3w8CWO7ePYfzkr-A1rz4Ge3A0Hmo9agpCDqoceGA1m_jMyebv3Bm1S3OK2A7xmGHSYVQY8r__1kzy3rf7WcOozhd5L6mXKjKQF9_sUemBGawX6ttohF_5O2MVugnEkru_6DqlJEhruf3al7gHxmqqwFURU0MvKmWvP4TvEjuli3OzQAqLcAYO7qh0vXlp_clzPaBekRzlwjatSrYljRvSehZyPAo6ATA5J3oWJybOwKniFEUHJG2GxJcjcp_0k9xwiS7Dqg09F3RB6y33ED_QvcjmHLx63CLzeNkqgATsr2rn3veiPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عضو کمیسیون صنایع و معادن مجلس: قاچاقچیان برنده اصلی ممنوعیت واردات لوازم خانگی هستند
🔹
مصطفی پوردهقان، عضو کمیسیون صنایع و معادن مجلس، با انتقاد از تداوم ممنوعیت واردات برخی اقلام لوازم خانگی، این سیاست را عامل گسترش قاچاق، افزایش قیمت‌ها، شکل‌گیری رانت و تضییع حقوق مصرف‌کنندگان دانست و گفت:
🔹
ممنوعیت واردات، قاچاقچیان را به برندگان اصلی بازار لوازم خانگی تبدیل کرده است.
🔹
مصرف‌کنندگان مجبورند کالاهای باکیفیت را با قیمت‌های چندبرابری و از مسیرهای غیررسمی تهیه کنند.
🔹
ممنوعیت واردات، نه‌تنها به تولید داخلی کمک نکرده، بلکه بازارهای زیرزمینی و قاچاق را تقویت کرده است. درآمدهای گمرکی هم به جای خزانه دولت، به جیب قاچاقچیان می‌رود.
🔹
رقابت، مهم‌ترین عامل کاهش قیمت و افزایش کیفیت محصولات است و تولیدکننده داخلی باید با کیفیت و نوآوری رقابت کند، نه با انحصار.
🔹
تجربه بازار خودرو نشان می‌دهد، سیاست‌های انحصاری، هزینه‌های سنگینی را به مردم تحمیل کرده ااست.
🔹
دولت با همراهی مجلس باید هرچه سریع‌تر ممنوعیت واردات را بازنگری کرده و زمینه حذف رانت و مقابله با قاچاق را فراهم کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/678067" target="_blank">📅 15:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678066">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/647dbbcc5b.mp4?token=e4xYvcXXsdLfrslCm_tMdwRgx-pmoVZpQkw-j1o7Deafe8Gf74MphIIs80H-c8F6C7y4AljxGmuMsZ-qLar3N_LKlVRhm2O7ESJ7saXULf0okI0MZiWWnpsb_FyIUtIHK0l4E4vkMZ6zvHMjtyvocRfzjE_w7MjTbcUo5RRj1xfOMypBDdRIBbCqD6XUueaRxj3Hiuhh0KsCwcT2h4yN5p3K48NWVOiRd7ZmKn-advB1yf3rCc-BW5P1cdPPzr3zbe60MDa88lkVe4KgNtTLOSxjazA2v-7agIYOIo20wUms6rxyfDgTxt3HcEVwAnroJV543kkuQzRNYtZJ0pvfOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/647dbbcc5b.mp4?token=e4xYvcXXsdLfrslCm_tMdwRgx-pmoVZpQkw-j1o7Deafe8Gf74MphIIs80H-c8F6C7y4AljxGmuMsZ-qLar3N_LKlVRhm2O7ESJ7saXULf0okI0MZiWWnpsb_FyIUtIHK0l4E4vkMZ6zvHMjtyvocRfzjE_w7MjTbcUo5RRj1xfOMypBDdRIBbCqD6XUueaRxj3Hiuhh0KsCwcT2h4yN5p3K48NWVOiRd7ZmKn-advB1yf3rCc-BW5P1cdPPzr3zbe60MDa88lkVe4KgNtTLOSxjazA2v-7agIYOIo20wUms6rxyfDgTxt3HcEVwAnroJV543kkuQzRNYtZJ0pvfOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از این ترفند کاربردی برای روغن ریختن داخل ظروف استفاده کن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/678066" target="_blank">📅 15:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678065">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
وال‌ استریت ژورنال: مثل همیشه باید ببینیم ایران چه می‌کند و چه می‌گوید، نه ترامپ و دولتش!
نشریه آمریکایی:
🔹
پس از توافق ۱۷ ژوئن، بعید است ایران وعده‌های ترامپ و آمریکا را باور کند و باید عملکرد ایران را سنجید، نه اظهارات واشنگتن.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/678065" target="_blank">📅 15:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678064">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f21018831f.mp4?token=XH2eOIlap5cpke4qapkN1pKtVoPFXSJ0Y9il4ppMR3sDVJE4JTON3tm7wFiuNv1G1oKOHnG1WGZ4LjFVAM8OM09toJmB3OG5wnGJSNMH_Q7XcUThoVt2bHQUyqPdoYJtSWe0s8J_8JzuFM8UGWNkC-w0kceZzfr80p5_RjcvKqEgvpUAvCnXRcp4SLDFOxzzi7-MZQAak8PiFhrGwMgJE2c1yo_9woSEGX0t-M0Jea7gw73RRzR9NFixU8hooFRuLjoDEUBmB2Fyj8wNKRbBL00tWQoN9oUxRlgMNa_nBSqsuDpHXD430LT4epHJHVc7RNQ7F8UdHALe11dy2Bxn8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f21018831f.mp4?token=XH2eOIlap5cpke4qapkN1pKtVoPFXSJ0Y9il4ppMR3sDVJE4JTON3tm7wFiuNv1G1oKOHnG1WGZ4LjFVAM8OM09toJmB3OG5wnGJSNMH_Q7XcUThoVt2bHQUyqPdoYJtSWe0s8J_8JzuFM8UGWNkC-w0kceZzfr80p5_RjcvKqEgvpUAvCnXRcp4SLDFOxzzi7-MZQAak8PiFhrGwMgJE2c1yo_9woSEGX0t-M0Jea7gw73RRzR9NFixU8hooFRuLjoDEUBmB2Fyj8wNKRbBL00tWQoN9oUxRlgMNa_nBSqsuDpHXD430LT4epHJHVc7RNQ7F8UdHALe11dy2Bxn8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حدیث میرامینی: با اولین حقوقم دوو ماتیز خریدم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/678064" target="_blank">📅 15:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678062">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
پاول دورف و تلگرام به برندگان المپیاد بین‌المللی هوش مصنوعی جایزه می‌دهند
🔹
«پاول دورف» اعلام کرده که به همراه تلگرام به برندگان المپیاد بین‌المللی هوش مصنوعی ۲۰۲۶ جوایزی اهدا خواهد کرد. تلگرام قصد دارد به منظور تقدیر از فعالان این عرصه، ۲۴۰ جام دیجیتال اختصاصی به مدال‌آوران اهدا کند.
🔹
این جام‌های دیجیتال در سه سطح طلا، نقره و برنز عرضه می‌شوند و حداقل قیمت بازخرید آن‌ها از ۳۰۰ تا ۱۰۰۰ دلار متغیر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/678062" target="_blank">📅 15:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678061">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47a0937f99.mp4?token=eBtkfgWgNcuIsaBmbrkM9-GdaqwCifRCt0e0JxGVWiRniBiHoCE6JOwUpBgUifegExboCtTJZYt2QFG8Kbq1y3pHDPcIRzWNhsaEfE1Arn7sdEvMUM7Y7103Zrmn-nQ6WrnUohf4A80dbXiAO_5oSpvaAm3po1QUH8RDOxFNSUtC6Ri0dmtCGdBbDP7knCaMecoGWhvGnbe3LljnGfavAh46IkwpZEKmpk-1TNHGcFeKRcmACzLHTTZT_shq-Qhb6Or5r9pk3lGF4u6qgCq90LGPcbBl6ft-rE1XRxFURN6LtU53PP3MbLzZpzkC0D4cJVVCO_FEv70LKJAX34xyVV5cQ0cmsiWsS7yYejhsZ5Pp77_l6LTtEvfeZbUIgZAkPczJuAH4C_FzGkptjlP7vgNXZWopx98gkP77vmvJjW4Y4YZQaM89BEHk-qd2Row-uYdiC3uAmIU_rzK3tzPHsY198zk5fpXM1JXP0yw3mwigVdkoZG8UaOQ7Wg7uOrF1ntY-LERGXkBLmJ0gjMvcPhWh4vUBlCA-NkIbc4nKsCQo_mLKguecLGd_vQNQOHbowdRT-y9T6mEEK_mW5dFEXgB6afc8YAvvsQrm3hYMhVzKzCqbdC2M4Dey41OrLVixpffKpTbrjmuGbiykHQlputsWz7c1HY5nXzlJH0jXe8s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47a0937f99.mp4?token=eBtkfgWgNcuIsaBmbrkM9-GdaqwCifRCt0e0JxGVWiRniBiHoCE6JOwUpBgUifegExboCtTJZYt2QFG8Kbq1y3pHDPcIRzWNhsaEfE1Arn7sdEvMUM7Y7103Zrmn-nQ6WrnUohf4A80dbXiAO_5oSpvaAm3po1QUH8RDOxFNSUtC6Ri0dmtCGdBbDP7knCaMecoGWhvGnbe3LljnGfavAh46IkwpZEKmpk-1TNHGcFeKRcmACzLHTTZT_shq-Qhb6Or5r9pk3lGF4u6qgCq90LGPcbBl6ft-rE1XRxFURN6LtU53PP3MbLzZpzkC0D4cJVVCO_FEv70LKJAX34xyVV5cQ0cmsiWsS7yYejhsZ5Pp77_l6LTtEvfeZbUIgZAkPczJuAH4C_FzGkptjlP7vgNXZWopx98gkP77vmvJjW4Y4YZQaM89BEHk-qd2Row-uYdiC3uAmIU_rzK3tzPHsY198zk5fpXM1JXP0yw3mwigVdkoZG8UaOQ7Wg7uOrF1ntY-LERGXkBLmJ0gjMvcPhWh4vUBlCA-NkIbc4nKsCQo_mLKguecLGd_vQNQOHbowdRT-y9T6mEEK_mW5dFEXgB6afc8YAvvsQrm3hYMhVzKzCqbdC2M4Dey41OrLVixpffKpTbrjmuGbiykHQlputsWz7c1HY5nXzlJH0jXe8s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
اولین کسی که به زیارت امام حسین (ع) رفت چه کسی بود؟
#طریق_الحسین
#اربعین
@Heyate_gharar</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/678061" target="_blank">📅 15:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678060">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/816bc40848.mp4?token=UK__7fDUCPg9VBR_hkXpLCIRMEdsB7teZ6qxNN0NeszUNx4pB7-Cq5a9qN1yy6iK2i9xvfXnx8Fzbb9SrfOViKBDh19VQdM8rs7VSaai5jlD9l457SZn4tb-kWSGkMnAjLgtjpnZ5GnLE_siGjmAXob0LqNW52AdcTBTAwccCDP_8Mj0forb34Itz8TsrYUFIVhtS8K92aaly99NCoAeESgirXH9p-t2_i6hJpaigUmj69SCHLlFtu-YvvAXgJdTODYwkAww_XZw-eA8f544fzD8SwOzx5Nzw3N2-TqH4fJY9S1mf8i-nVLJ4ivkpgswpfuFRt036mjN_598dtpPzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/816bc40848.mp4?token=UK__7fDUCPg9VBR_hkXpLCIRMEdsB7teZ6qxNN0NeszUNx4pB7-Cq5a9qN1yy6iK2i9xvfXnx8Fzbb9SrfOViKBDh19VQdM8rs7VSaai5jlD9l457SZn4tb-kWSGkMnAjLgtjpnZ5GnLE_siGjmAXob0LqNW52AdcTBTAwccCDP_8Mj0forb34Itz8TsrYUFIVhtS8K92aaly99NCoAeESgirXH9p-t2_i6hJpaigUmj69SCHLlFtu-YvvAXgJdTODYwkAww_XZw-eA8f544fzD8SwOzx5Nzw3N2-TqH4fJY9S1mf8i-nVLJ4ivkpgswpfuFRt036mjN_598dtpPzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش سفارت ایران در کنیا به عقب‌نشینی مجدد ترامپ
🔹
سفارت ایران در کنیا با انتشار انیمیشنی از «عقابِ عصابه‌دست» و «موش صهیون» در فیس‌بوک، مدعی شد عقب‌نشینی دوباره ترامپ نتیجه حملات اخیر ایران، بن‌بست راهبردی آمریکا و هزینه‌های سنگین گسترش جنگ است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/678060" target="_blank">📅 15:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678059">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
یک تدوین زیبا از آهنگ «تلک قضیه» درباره داغ این روزهای فلسطین/
فریادی علیه دوگانگی‌های سیاست‌مداران درباره غزه
🔹
حجم فاجعه و جنایت در غزه به حدی رسیده که آدمی نمی‌داند با چه زبانی، با چه اقدامی، با چه کاری می‌تواند خشم و بغض و غضب خودش را فریاد بزند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/678059" target="_blank">📅 15:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678058">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRaLw-RJq-9KHsO9OPBAE8oVirQt-yvKfYJzohD9L1WKseh5gfKZIkMrvzsIOZYBjD2Wh7bDIpPquR2nwUsm5Jv2zdbOwnuyxRgNXW2Q6r-Z5jgoy7ub4zWuOek3gkwSkRmdnDZmZbsJIbam4311ghHxcaMIrCzfPWIrxq9nuYg5Q5lfIob3Upqw5qIviEDiPIKNcUAuXDiznxkB_HkpUjOWBw_BBgPR0sQkLUdq-TW-uWhjfQvv6QbV9uzKA9eFPR0oLT-hgHUSOFrqfX3DtRLcTW8RaZ5F2jsvqSYLirIIRFqc65RgkWrGSv4RxOMn9pq7QtbHIDy3hRwvePTIvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس فیفا دست به دامن سگ زرد شد
بن جیکوبز، خبرنگار انگلیسی:
🔹
جیانی اینفانتینو قرار است با مقامات ارشد دولت ترامپ دیدار کند.
🔹
او به دنبال جلب حمایت برای ادامه فعالیت خود در فیفا است.
🔹
اینفانتینو در حالی که فشارهای فزاینده برای استعفای او شدت گرفته، با فدراسیون‌ها تماس گرفته و از آن‌ها خواسته است تا علناً از او حمایت کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/678058" target="_blank">📅 15:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678057">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d685dd8189.mp4?token=dj-kN72vbV0Fhq2V9fkYspMBzFOwv1JX6w6rUmEbZN0EcdEngqJGfzAKPMFROz7yCUIekwIuZog5YwZUr6Ih89Dhn53lPlY_z4eJ-36o4vOQ2L5wddwEgANW-SwF_SiyC-KfitnNPlqaD2JaMksrkzL9hA9g_5uoN1KhVyBFkEzNpJR3KUE2-Si_nW5WDh9iI-t_C2r6x3wbD2xTC8z7SATaVSGu7d9EQ93m4xRxYeAJ_QRddj8SNUTpVkLN3DxTHUXmG1GEKGZ4nViRZ-4oiiL-mBbz4e4J86UL1rpYZF7l5Kbos_I0eH6sVjbNfZM-tzaNkLE6ol8LA-EMAKXBeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d685dd8189.mp4?token=dj-kN72vbV0Fhq2V9fkYspMBzFOwv1JX6w6rUmEbZN0EcdEngqJGfzAKPMFROz7yCUIekwIuZog5YwZUr6Ih89Dhn53lPlY_z4eJ-36o4vOQ2L5wddwEgANW-SwF_SiyC-KfitnNPlqaD2JaMksrkzL9hA9g_5uoN1KhVyBFkEzNpJR3KUE2-Si_nW5WDh9iI-t_C2r6x3wbD2xTC8z7SATaVSGu7d9EQ93m4xRxYeAJ_QRddj8SNUTpVkLN3DxTHUXmG1GEKGZ4nViRZ-4oiiL-mBbz4e4J86UL1rpYZF7l5Kbos_I0eH6sVjbNfZM-tzaNkLE6ol8LA-EMAKXBeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وجود برق روی بدنه وسایل؛ خطری که نباید نادیده بگیرید
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/678057" target="_blank">📅 15:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678056">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
ادارات و بانک‌های کدام استان‌ها چهارشنبه؛ ۱۴ مردادماه تعطیل شدند
؟
🔹
قم
🔹
هرمزگان
🔹
ایلام
🔹
کرمانشاه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/678056" target="_blank">📅 15:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678055">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
مهم‌ترین زیرساخت‌های هسته‌ای منطقه در تیررس موشک‌های ایران
🔹
در پی گمانه‌زنی‌ها درباره احتمال حمله به تأسیسات هسته‌ای ایران، هشدار داده شده در صورت هرگونه تعرض، مراکز هسته‌ای منطقه نیز در معرض پاسخ متقابل قرار خواهند گرفت.
🔹
از مهم‌ترین این مراکز می‌توان به دیمونا و سورک در اسرائیل، نیروگاه براکه در امارات، راکتور تحقیقاتی ملک عبدالعزیز در عربستان و راکتور تحقیقاتی اردن اشاره کرد./ جریان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/678055" target="_blank">📅 15:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678054">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZDp88JT10WU49M0T2Tc3thqy2ivY0dst6RTAgRalOcziE39YXHZ99MpdG21PHmt641ncGuJZng9HUs2z4qC87IOtGpQyF947Fizw8eN2wZe_yBq3iL_EgrIouKN3J3GgSV5aFS4EJZ9S7BQ21L0z3jqvvOor1h8Z08sBUY-0RAQwBleRf9X8uz9AisX0dDSPZ2P9RMt_sA26TQXdADKlHKHgJ9r7Jkq659ju2jFKGtqZqDdTysl4ay_M7jnjU_1uH-m81EsXDRlPpYbn1qbARqE4apE8VPgavDu-O_q3j6idVjbXrX9srIygNfvlRo1GfdlELNJG0F74dVr3X7-nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۲٠ کشور برتر جهان بر اساس میانگین آیکیو در سال ۲٠۲۶ با قرارگیری ایران در رده چهارم
🧠
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/678054" target="_blank">📅 15:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678053">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fddbf2f7f2.mp4?token=s5UCGKQuiCVWBSJnVpJQfv7q9Ep0LZWp6JeMpktEGrmF4KZIwiCYymfPBneqBwtWnJF-3MASi-A_1EcgyC0HmLVupJCPVZ7rIz2QS3fu5AjNUgHnPAqbZOiqNN4fNw1VAmBFm_gf-gZhZjR0fwlsjJifcIvkFHJIHn71rPQrR9sKRsQ5FKsusJvb9rI1J2ZGsJQiYb5LkwJH5vJHbvLz_5-cHRn4xptPEWpC7Bqlfko61NXpSutCEcJy9OUeTWjdkhwaVGd3w15XiNyFxNTkhShq1WuaKZ-J3GPlmb5KiImPWyjRBMUs3flWttWX1BXWyVDCmRKAAijoqXYNVo6p-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fddbf2f7f2.mp4?token=s5UCGKQuiCVWBSJnVpJQfv7q9Ep0LZWp6JeMpktEGrmF4KZIwiCYymfPBneqBwtWnJF-3MASi-A_1EcgyC0HmLVupJCPVZ7rIz2QS3fu5AjNUgHnPAqbZOiqNN4fNw1VAmBFm_gf-gZhZjR0fwlsjJifcIvkFHJIHn71rPQrR9sKRsQ5FKsusJvb9rI1J2ZGsJQiYb5LkwJH5vJHbvLz_5-cHRn4xptPEWpC7Bqlfko61NXpSutCEcJy9OUeTWjdkhwaVGd3w15XiNyFxNTkhShq1WuaKZ-J3GPlmb5KiImPWyjRBMUs3flWttWX1BXWyVDCmRKAAijoqXYNVo6p-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استقبال گرم پلیس مراکش از مهاجران بازگردانده‌شده از اسپانیا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/678053" target="_blank">📅 14:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678052">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
عملیات ویژه ارتش ایران در عراق؛ ضربه سنگین به ضدانقلاب
مشاور فرمانده کل ارتش ایران:
🔹
تکاوران تیپ ۲۳ نوهد طی ۱۴ عملیات زمینی در مناطق سلیمانیه و اربیل عراق، مواضع ضدانقلاب را هدف قرار دادند، شماری را به اسارت گرفتند و بدون تلفات به کشور بازگشتند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/678052" target="_blank">📅 14:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678051">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6sRe-qsVKGTXXbYf6Ev0GyQKIFVRMsEujiefTLpGMsIPa6cFpphAunvPtZ6R2sKZTVYibqdo4m8WDBUD8MlguTUNetIu_hWoC-Zgk-_BQjslM3SHRcimjtaH9x76K5Y6U1rErFJoHUn4t_oSea-lWYpQqFg_9YsFFIm18rphNkmOhEGF00Q9wr0g4KWtI4GdNV1F571MVBKrcuLBfQv1JK_oB1W1DGhPq1dZbSprvOxRpVOnozbyom0kKUVEQQ5segXoD_Sw5OnYVexVVTDVmFwILOE_hJEw35u8XNDydEdGcI_bNu36D715pOADiGg-Ht_B046-pXAuje5DcHJTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا از صبح سه تا ترابری سنگین نظامی فرستاده امارات
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/678051" target="_blank">📅 14:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678047">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mAXW5_rXlAEqOoD16fw01C77dnEYgvZSncvMcLEdN7EnVnDo89A9S-4wQid4OTynsiV2O9HA8GvoKG9Cj2tQwqJ10LLia9CWEpzy5nelH4A-CcclFHXeX2tJ176SD0_gtV5yC4SUJtlKqmGM91TIvC3Ez71sf2w7HV4lAqzN4LH7yyNiv0Ufc7Gom1jr4JwOX0LI1IRz4f0Coqs0sr3WAnFl4GAhW3ZJIGQvNoqitZpBK31vVz2OcZI8YKqacD90ENLu6_otSFWfIneA7KA6XgYmi9PdKa8nnxMaLhBqh9DSwkIkEFE5r2xPFA3UeRybHRhy-p9GGrCuOT4PKKdQFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fa-0a77W4mTQJJgHZ_4M_UYmATNI2RfJu7kzjIdw7lDuQJtm8QiX41WnmG-WCxoXAk8otTKSK64eEMeAJyhQ8nqbH9NGSL1aWNM-HGXuaH1rcmTSehaxr3qYee-rOPOw5SxSFDzrN6ikXcGpGUqV-yyuwnkGzk6d_Fl3O46_02I3tO4UxkaglzvUGHilOl4z5RSC5B6v2jn9O-CHEw9BoLu3eneaVbIcFDcZZJMeke0_4ijJp5OdCUHuqDlnIhL1E6Rv-xUw8gYXs9xuWwUN1Ne7VPVZwZvarsFQi0mTlUdmjasgkjDADFYZbRz7Ou-5c0buj1rNea2cKDZ1Km-xdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LEMTrytwElQL-FfrU0QbEHygXRDDUwrkkFh7Zg1laGJOeDd2LsWE3ambi_H-0nqh14_rR93MWdtanQ5pIBAWAv4GSXm273a5m9x_AFir0tgMjsR7RM6AHO8ZrUE2v2a3KHvAVzFnwell0_g28jfD0HGn4I69LjltlQ6l7Mm18WC7RkSTcSgcqFfnBWVE7sMQJ9COXLuWAm3FZ_qKCjfKZoaaNiWfdNPII2kM_h4Ti_TWRJoRrhBZO6RRygqElWCnyUkcXBBWgoIQCPY4Lb5QScjWKdUOaVz6zAWQdJ7mEvVDZDB-JzjUDc5lgcuOn-9AYlsLImn7uVLDlPSGdw0xwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IDhYb8tmbYcz4Tz-OiBnp_3dnCIh7DN-3Vvl4LWuhaStEsDp0_RYuKbqTFoENUCgGl8bV3F9iO-pFt_q48CY-IVba6xkvit-x_G-erNLFMNGgAKHBKI0agx8Ua5A_tMtUGYZ_MVnqclLTLSfpCRQFeOxwMvGfb_JVkIFnHK7wUkvo8cbQGsPPXkclR07nwcxezoMfVam4FbYGZ_SdxcYP-OMVB7lxfJCEhiC6oENIsnna_X04cgIOs1aYmFlCLvC76MWuXu1pBLz_oF_Y9oTdpJK8JHyJlZoUQEchY2MFEPuPhwB7eCI3Wv7u4igedHNo63MGfq0cNN6UYG-NDnzdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
همه باهم برای ایران
🔹
حفظ منابع آب، با انتخاب‌های ساده و مسئولانه روزانه آغاز می‌شود.
🔸
هنگام اصلاح صورت، شیر آب را باز نمی‌گذارم.
🔸
در صورت مشاهده نشتی یا شکستگی لوله آب، آن را گزارش می‌دهم.
🔸
از شستن پیاده‌رو و خودرو با آب خودداری می‌کنم.
🔸
مخزن فلاش‌تانک را تنظیم می‌کنم تا آب کمتری مصرف شود.
🔸
الوفوری را دنبال کنید
👇
#همه_باهم_برای_ایران
@Alo_fori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/678047" target="_blank">📅 14:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678042">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
احراز اقامت، شرط ادامه دریافت یارانه و کالابرگ
سخنگوی دولت:
🔹
افرادی که پیامک دریافت کرده‌اند، تا پایان شهریور فرصت دارند با مراجعه به دفاتر پیشخوان دولت، اقامت خود را احراز کنند؛ در غیر این صورت یارانه و کالابرگ آنها متوقف می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/678042" target="_blank">📅 14:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678041">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAcdYvzMx7vuuParSMZNkrz9KE_Z1R1nkL_MBpew8VC_98sTSotDGyGauznCQLF1e7aCw-my51RGSClrbF7xtGeLAFUGoQOY7ts1QGZIN0LYN3PYtnaflKbpN4ed42f4zyk_hk97jrKcX9bfWGl9Tf_dAnP6_7Sz_gUeJusZwlJCkRwJCEB_uRrZt05cGvfJU3TZggaK9yva6hNV6ZDyILNHJmCpbx7xhrJjPGDeeZumdHRgteZ_b1ZmNVHIxmJUaCu4QX-RnR9MyIvNUtlFuTmfpY9OIaucpfbCPq-_H4MJgu3z4erO9dMAX5NsnXOoho5VslUYQsmJWdiNqQzoHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شلیل؛ میوه‌ای طلایی برای سلامتی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/678041" target="_blank">📅 14:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678040">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyP6eePhP2A8nzBMVykYBN8zBrjsFlNHcGZhEmCBG8oPtHPAU90PauylJHt4IdQzgf8Xzyqje0qZkQ3Di38HXX-PKgIrhhiAV0W6qoQQTpbKfbxJrQO5oIxJ-m_xoKJw8vjngYLzlVvzD0Lwlfh9OQIp4S80dtgQxALqrqBZTcmCcb9QhA2rCnTMKeiWoWazufw6KJ2z1CHKJczg6jKXOqtb5Ejmwl_CvwPasD0Azc4cu4voZkP1qk-O9qrq4pgsUcTz0neSnnH_mb5_qdouG2wcQpaSGRAqkzkY0Dxr76Yc_WyjmQOLA2-9XlOjhjf3BkwjHNWj2EIEDZPyKZJxkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله به زیرساخت‌های ایران، این مراکز انرژی را در منطقه نابود می‌کند
🔹
اگر ترامپ بخواهد زیرساختهای ایران را هدف قرار دهد، کدام مراکز انرژی منطقه در تیررس خواهد بود؟
جزئیات بیشتر را اینجا بخوانید و ببینید
👇
khabarfoori.com/fa/tiny/news-3235237</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/678040" target="_blank">📅 14:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678039">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
تکذیب خبر بازگشایی مدارس از آبان ماه
وزیر آموزش و پرورش:
🔹
سال تحصیلی جدید از اول مهرماه به صورت حضوری آغاز می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/678039" target="_blank">📅 14:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678037">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7319b39b1a.mp4?token=RjFDcCByZnwxbCa-85NH46JfmgqC9j1-9x-CZ0ZU_Lp3IqyNO_M2oc_Eni-5LK8sDlWt2UyrFxIM7X7JTyTYhgzaKpKFxV8Obaz_I6kRWV4ts3WMKfsq0-fJ3NpHX7-6q4LTr7vVmhelJsHcBYbzmkROfV6UyDYmLWRvbOICSNLHuFfq0MwNq9nUfqM2b71QM6JrROWR1GfpiFDe8RUqgnjZUlZrvywwQqyYeeMnXgPEn08BFIqDEoGyAYyBQ5jFf8ThdRrlOB2K8l7ZrdrhepN5_KrX-EAMruo2rMHH0dyFc7v49pgxB_iGNsTA3dGWaMXuHWgOgRmca-zZX8hf9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7319b39b1a.mp4?token=RjFDcCByZnwxbCa-85NH46JfmgqC9j1-9x-CZ0ZU_Lp3IqyNO_M2oc_Eni-5LK8sDlWt2UyrFxIM7X7JTyTYhgzaKpKFxV8Obaz_I6kRWV4ts3WMKfsq0-fJ3NpHX7-6q4LTr7vVmhelJsHcBYbzmkROfV6UyDYmLWRvbOICSNLHuFfq0MwNq9nUfqM2b71QM6JrROWR1GfpiFDe8RUqgnjZUlZrvywwQqyYeeMnXgPEn08BFIqDEoGyAYyBQ5jFf8ThdRrlOB2K8l7ZrdrhepN5_KrX-EAMruo2rMHH0dyFc7v49pgxB_iGNsTA3dGWaMXuHWgOgRmca-zZX8hf9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات‌های چینی حالا بسته‌های پستی را هم با دقت مرتب می‌کنند!
🔹
ربات انسان‌نما در حال تشخیص، برداشتن و جابه‌جایی انواع بسته‌ها روی نوار نقاله است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/678037" target="_blank">📅 14:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678036">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwZR7_yDAHdCFIB7xHD5lJsqFImHe4fPQXPF32lnBiMg3TUweK2lDFJlXXSs7YyJHdSZ8oYl8YqQeGeLDVZ4Meq9hX05pibsY3mDM8KTZu71zYbvIwdsjTGJb-oEYuF1nGCek_whl3tgHgXcEhzcwuAuoRTJRPOQVc8tI7W7sk3O-6vkg6q7nkgp8_kn9GIzHzaoi9c28VwKMSWzrpfIdCT3bVc8BRISonCX0VKmqqoRy2TU4NskhxZ21-5u8dEetuUFuv1TakvCKB9nN1uua5ZELBrP7ZtnIhbMlBptKgXlFGZ-pQnPwXOfh4-WoAmvUFx48KcC6lJDmtvwWPtBPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۲۵ کشوری که بیشترین مقدار قهوه را در جهان تولید می‌کنند
☕️
🔹
در سال ۲۰۲۵/۲۶، برزیل با تولید ۶۳ میلیون کیسه ۶۰ کیلویی، ۳۵ درصد قهوه جهان را تولید کرده و بزرگ‌ترین تولیدکننده قهوه است.
🔹
بیشتر تولیدکنندگان در «کمربند قهوه» بین دو مدار رأس‌السرطان و رأس‌الجدی قرار دارند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/678036" target="_blank">📅 14:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678031">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jgOyYycDRwYiU0-Z3mn6Q9torMe6dAsE5SJtsHoETra1gZ64eh-E_uiFUam2RWMX8VkL8a5A6JEKWNgCAtKlfUwCGGoIx8139sULD7x5q22hkA1cMRKav0x9PGZyQm5iEidKmPHEHzWzM8fEwFxraLv3dpKh2PCN1z2Oc2PIQVoP8vt-r9FUn-aRsz_eNg0rFAg9trd-imAU5-54Gt4eYwtJwP9ZLPifx8jXgfWf8rkrMHIRBhNK91pkNFAIwv-CvzBEKe7dWjm8NVNb8SPtI3g4l1lGsJjDD5Q3LU7p11BCy50vj7U-8hiMPbiYc4Zazi0MVs0LqRYqHq6-bqv-Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j0Pi3TvSorhL9X41zgLVdE1E8iJsAMLS3V64_3uZCawxJYM4dfoqhh3OK8CGzpo6-LOqkrtMr5A_xjK_B0vjlzJ6eRkXFESFSwb0WxU628bN0OpyUIGyx5N8Ro1wTS9Ep8Gqw_nnIuqC2_qfzAz0ru0IZVIr61b9rwqorCItlkPN_pUgtIVPzr5RoLZh1qD4SHNWLeX5-Y_LUDxrObIo4EdMsJHxy9NzBj4q2yEtXMfBwQWEAQkPtQ_q1tRdqcvGIJ3ciI7fivqk3Sz21EBLbYhGP2uVe8arpPeGe9uaMgAR1xcBc8jIp7smUuC8256X0HT8HXG6BJPVJlWCM5fI4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
این ۱۶مدل آستین رو هر دختری باید بلد باشه #فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/678031" target="_blank">📅 14:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678030">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromوحید یامین پور</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c06f8046c6.mp4?token=e6PMXiNNjTlMe2dvVW1efP3FEQHjVQe8p_nJER3nPlCFl_AH9Ug_FOmhuwHbNLOXSacXUNVpmgy5PIHbdmDOZEkB9mzP__75ZHWBYDYuEeixq3aeAcqLlB50SVL_MnhyhNXy0_ZELo0r8VgIpkIkT0O_ddlZ0QZdljCoRrfeOocayFmavH7QyelDeKvxczNO49EYyJH3ZCuMP20bE8ywZKuJLXjGqATGSSv_s_oi6hGXNw_mdtpm8ObjHdpld0LJCjsrGtM3a25XyJkk86ddywUezuNNDnnrcNzxgyZ5bAEForJyErzCzisPLNd1srom40fUf8ucLqL2vK30wSA0Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c06f8046c6.mp4?token=e6PMXiNNjTlMe2dvVW1efP3FEQHjVQe8p_nJER3nPlCFl_AH9Ug_FOmhuwHbNLOXSacXUNVpmgy5PIHbdmDOZEkB9mzP__75ZHWBYDYuEeixq3aeAcqLlB50SVL_MnhyhNXy0_ZELo0r8VgIpkIkT0O_ddlZ0QZdljCoRrfeOocayFmavH7QyelDeKvxczNO49EYyJH3ZCuMP20bE8ywZKuJLXjGqATGSSv_s_oi6hGXNw_mdtpm8ObjHdpld0LJCjsrGtM3a25XyJkk86ddywUezuNNDnnrcNzxgyZ5bAEForJyErzCzisPLNd1srom40fUf8ucLqL2vK30wSA0Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان آزادی عراق را خواندید. این هم داستان "آزادی سوریه".
❌
وضعیت اقتصادی سوریه در فردای «آزادی» زیر سایه محور ناتو ـ اخوانی و حکومت جولانی
سوریه‌ای که با شعار آزادی به ورطه آشوب کشیده شد، امروز با واقعیتی تلخ‌تر روبه‌روست؛ اقتصاد فروپاشیده، زیرساخت‌های ویران، گسترش فقر، ناامنی معیشتی و آینده‌ای مبهم برای مردمی که بهای سنگین پروژه‌های خارجی را می‌پردازند.
➕️
@yaminpour</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/678030" target="_blank">📅 14:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678028">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGGzbs_cxih9kJb00DODxSIM0v0yBxmP3hLSSfyY38N8kK_n7p8HBJYMXwt7WYWiJW96LTbU8N5ImCNoTkrXGZYHFLrZ183eHDHK7PsEtOpQK9i7uAU5Q8pjjHGwR3DCZ7_3QIAD5AJBVKQy4hLnmlRJJBFFqrQKTQuhthC5DCvfZdWMw89HXBaMzJB6Vk-zNvFnPC4rCxP-Z66fhIQhF9_efGXnupSgXwhptilROo5y1VZMsjUrXsi7pdLLE9yWe2jqMQp2OzUXmWO0KY5QdEisEHofoGEY51mWZHNt2SpKGXgPGLt9iE1Y1JBRMT5jztU4Lu-yBtovJRcWrvMcdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر زیبایی از دماوند از داخل هواپیما
🔹
محمد حسن مقدم‌نیا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/678028" target="_blank">📅 13:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678027">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/il0--cvtX6yj1_8F0pDcz3jWqf_IgbLZo-0QlnVuoT2Kzq3UgkGrCoQonuluzhZq7nybClHNWQJSL5LlQWxMUwAct6V9CqQpMXIsqLYjJeg0yhlTnRhvpDoPPohheseIbgh6AL0nfrZMYtBIQUz9le3OCYKp2eUJidTw179ySVZbtl_rKDza1yoDF8HiDfqbR7fHWDzkeNRDAibelZ0XY1vYjUvWSslQCgvcYEswMZJK9DCh1ZPTyBJd4_Kf8iunf4Do716YuJisQqfd6YGP_WdAAFyxc3ketx9Bbg4wQVkKKYvj-pEh64mCdkBoxGFlhdRwn7TyFYCC3epAgiAluA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زیاده‌گویی
سناتور جمهوری‌خواه: باید فشار حداکثری را حفظ کنیم؛ تحریم‌ها، محاصره و بمباران کوه کلنگ!
جان کِنِدی درباره احتمال توافق میان واشنگتن و تهران:
🔹
از تلاش برای صلح حمایت می‌کند، اما حاضر نیست توافقی را که به‌زعم او «بد» باشد، بپذیرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/678027" target="_blank">📅 13:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678025">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4074d30983.mp4?token=ucqqI-2tt8I8XjUWL96Dl8IrTQ4Mu8q6x2a_rw9480GyEnWnwF_1iUupWW4-RlIIz0RiF_6YQJCqRwhStvUv6e-d5Iia6JRkQA-8UZsxsv7h85Vy--7IqdVinPZm4OQk_1L1GW6CASIqjyLND7XPBDqbSgx7GN5BiuUDPS56JSGo6i5aNiQDlYqtnAopaExz21IfTEzAhKslOitIQb8e2M5XE0-t1vGO4ZjtoMFzE3JiQ_mnNkGopqqaQ9xV8XVJYtPOycrfZSLYdrKCZSRpu4kOMY4o1FJfe9LxmiwmvCbIIqG7Tn9SqF36cRY5k74S_rZ6zEizXyfuqvfMFwEsgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4074d30983.mp4?token=ucqqI-2tt8I8XjUWL96Dl8IrTQ4Mu8q6x2a_rw9480GyEnWnwF_1iUupWW4-RlIIz0RiF_6YQJCqRwhStvUv6e-d5Iia6JRkQA-8UZsxsv7h85Vy--7IqdVinPZm4OQk_1L1GW6CASIqjyLND7XPBDqbSgx7GN5BiuUDPS56JSGo6i5aNiQDlYqtnAopaExz21IfTEzAhKslOitIQb8e2M5XE0-t1vGO4ZjtoMFzE3JiQ_mnNkGopqqaQ9xV8XVJYtPOycrfZSLYdrKCZSRpu4kOMY4o1FJfe9LxmiwmvCbIIqG7Tn9SqF36cRY5k74S_rZ6zEizXyfuqvfMFwEsgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تغییر نظر ونس، گراهام، تد کروز و روبیو درباره ترامپ پیش و پس از ریاست جمهوری او
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/678025" target="_blank">📅 13:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678023">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e443f1ab91.mp4?token=QXyQ_0khhRicFZcZIcFbA50oox7mAmQ_DkZcAYUtkwpcL7b25DI_LM_KRNhKMgwU0ugZXnHbO4xmEUCgNGKVty7qCdLBcpRYzopkZne0VxjkzEnlVoqTHLd8mhqFsR6ITrwKo7AChPjR4EQKjhpnakmRXnZ8SVKOO5E_FedTa5c2Lqoig_gkPoPGEeX2NnIECvutSLItQdJqFMMsQcpk95yYosGrDqSG3W3R6O3-b7lp07FgztAVuBUwq2dMzZLibcpR0Nx70A_s9uUfFyJ2wVq82wC0_OKpgPlshwMtGctBIaHJzRSn_LT8dgBuqijKJYYDXjsOirdJAVpcsa8rgK_fbV9cQgkQ1vLj2cU_PThH2v1T9FNwEXRCMx_-2YvpMZL3xRZlKH-oCeEbifIoNo8VbgzzKuV7OCyqnBqZuGIgPJMnweMrdXvIghE0ubnM3ns1f9WVpWcOrTtsDcUAg7BdMP-Wpx1TU2G9Kim05FefSNLL_jx8F5pzhOvgvKsnOHQgfOTsY27Mb0u7SyzzMFl_BiShnnrayWWbV9eocJZeyz8YI5Y1l-XdDx6HLLyGy42LL7Oj8i_Kcl_-nUtWnCRYGK4e7jDjyPLmjzVXnjNMQi-blabYEgUQoJaZ8hHhcoEdpGuYzDmnx8L_Dl59Zr_GmKDnbvooA4fLHwMTptw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e443f1ab91.mp4?token=QXyQ_0khhRicFZcZIcFbA50oox7mAmQ_DkZcAYUtkwpcL7b25DI_LM_KRNhKMgwU0ugZXnHbO4xmEUCgNGKVty7qCdLBcpRYzopkZne0VxjkzEnlVoqTHLd8mhqFsR6ITrwKo7AChPjR4EQKjhpnakmRXnZ8SVKOO5E_FedTa5c2Lqoig_gkPoPGEeX2NnIECvutSLItQdJqFMMsQcpk95yYosGrDqSG3W3R6O3-b7lp07FgztAVuBUwq2dMzZLibcpR0Nx70A_s9uUfFyJ2wVq82wC0_OKpgPlshwMtGctBIaHJzRSn_LT8dgBuqijKJYYDXjsOirdJAVpcsa8rgK_fbV9cQgkQ1vLj2cU_PThH2v1T9FNwEXRCMx_-2YvpMZL3xRZlKH-oCeEbifIoNo8VbgzzKuV7OCyqnBqZuGIgPJMnweMrdXvIghE0ubnM3ns1f9WVpWcOrTtsDcUAg7BdMP-Wpx1TU2G9Kim05FefSNLL_jx8F5pzhOvgvKsnOHQgfOTsY27Mb0u7SyzzMFl_BiShnnrayWWbV9eocJZeyz8YI5Y1l-XdDx6HLLyGy42LL7Oj8i_Kcl_-nUtWnCRYGK4e7jDjyPLmjzVXnjNMQi-blabYEgUQoJaZ8hHhcoEdpGuYzDmnx8L_Dl59Zr_GmKDnbvooA4fLHwMTptw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیاستمدار انگلیسی: وحشت در خلیج فارس از پاسخ ایران/ بار دیگر ایران پیروز شد؛ آمریکا دیگر توان رویارویی با ایران را ندارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/678023" target="_blank">📅 13:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678021">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
ایران ۸۷ میلیونی شد
مرکز آمار ایران:
🔹
جمعیت ایران تا لحظه انتشار این گزارش به ۸۷ میلیون و ۷۷۷۷ نفر رسیده است.
🔹
بر اساس جدول پیش‌بینی جمعیت کشور که مرکز آمار منتشر کرده جمعیت ایران تا سال ۱۴۰۷ به حدود ۸۸ میلیون و ۱۹۰ هزار نفر خواهد رسید که نسبت به ۸۱ میلیون و ۵۳ هزار نفر در سال ۱۳۹۶ حدود هفت میلیون نفر افزایش را نشان می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/678021" target="_blank">📅 13:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678019">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEmsuy9nWxypRPtb2ro_gpogdqyzMfiJK99Nys-PEAI8-F79AVfB9_sLIsvzAXAWOtq-tsPwmj1pUjG26AMnIalSdVxXKp1B-mcwDt4XUhq6ao0Pur1v3Cq5KJGJ-PZVU-xK-9RQ62URbQJJI0GQZkQrYPV-IMUJcHyeh-ACuMWRU3wR7Rm7ZUTZ1QW8qjOtK-3XMsO2vC6JJaYRuHCBLqZ-M5ahSP9mm7ucd1MiKju5ShQpzUzMgDRWmMe58IBWjvrzcvBJZYfdWdXNpCouELk3DbC_XwSuSnl89fhQBOH69lNsSRSi27ZiW1EAReO8qvv5ALyVnwsFwMxz3WWAkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چه طلاهایی برای خرید مناسب هستند!؟
🔹
اگر قصد خرید طلا دارید، این راهنما به شما کمک می‌کند بهترین انتخاب را داشته باشید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/678019" target="_blank">📅 13:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678018">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c223a9b104.mp4?token=d19Gw1H8N6EzBFYB0goq61g1FvxX7z24enhiFqcAqypGsz4u64CfaCiP9UmEMxmB6unIkn4SyP_mOWeVkyLjBvlGUhZbJS38mSnPw6ukwvgVdSMUPVOHTwLii5u2qs-aREX-qZMU6NC3UT2R_UXpKt_2e8j-b0an6l0ODIqJC4DcyvZc1s82gq5Exe-ciSC39ju7_CImCTY1ZqdtFu2o7hNOPzbCp2sUJ1nlM9u557wzbfh1qns-ul-jvavA8Xjl0h7LItdBPKLXlIKGVtRy43QR5bnj4OxFt6ZT__m8cbQH50UAIj1GeAiSJxslhZ28REUWq7lpLOIef1vZbK8sjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c223a9b104.mp4?token=d19Gw1H8N6EzBFYB0goq61g1FvxX7z24enhiFqcAqypGsz4u64CfaCiP9UmEMxmB6unIkn4SyP_mOWeVkyLjBvlGUhZbJS38mSnPw6ukwvgVdSMUPVOHTwLii5u2qs-aREX-qZMU6NC3UT2R_UXpKt_2e8j-b0an6l0ODIqJC4DcyvZc1s82gq5Exe-ciSC39ju7_CImCTY1ZqdtFu2o7hNOPzbCp2sUJ1nlM9u557wzbfh1qns-ul-jvavA8Xjl0h7LItdBPKLXlIKGVtRy43QR5bnj4OxFt6ZT__m8cbQH50UAIj1GeAiSJxslhZ28REUWq7lpLOIef1vZbK8sjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دل‌های بزرگ در قامت‌های کوچک؛ موکب‌دارهای کوچک اربعین
🥹
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/678018" target="_blank">📅 13:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678017">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abc33793d4.mp4?token=AmQD4c39HW9tKluI-6k5vkzZuopRloYrjwnj7kRBpZXWssMo6lHOsyJ_m0dTXLvP2-KDCWzzBXvlpbG7WslXpvQLpW_JrfbRGJE8P_a91gQVYVAuYADs1HH-bDCn9nP8tfcBAfwBT1S9bT6wcL0lQNgljAjiRelMXGiX1anegQzE3W1ek9jYqPCOHtQNt28bKcyBu4td71EcGX0jLqZA-alM15T1kuklNulTSwv6GHSJaXK7lTH0oU0dKJ6bYdQT6HA_ROXnza8U7T6uC66LFGanQJLxqHhWy68jV1JnINYeFL-OZNfrXuO5MFm-_hO4vIvG9RO4o33zr4s8PiHYXSUZv0_i8Q2E68sa7I388cuBBd-IHb4lR_907PYXHo0X__Z7Grd8OYJvl8HrYXVdMJiaHdbvjBZxvglCoqiqlpiPYhNuXYWICmxl-xVpVWpDYUJmYKD5ms8CpmOtK1i7PdEc3dpo2lih7MFsLh0bHdeayNMskluDIe4w8jegbaUhEL-BjEDzsFiEb92wMu4ONtKF2BtADhvPVgwpGNYdYSVsUzDxjvC3Q4YL0RxJ9mfXNw04-zh13jn5US4p8Txx24BfRNiM7_XxJ0epRXf4jXClgHX8DvZpp6XdJrewfaNMNjXqPxo7R5LVyXXWCyVmR7PnQGc6tXZisNlQ9xqssOc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abc33793d4.mp4?token=AmQD4c39HW9tKluI-6k5vkzZuopRloYrjwnj7kRBpZXWssMo6lHOsyJ_m0dTXLvP2-KDCWzzBXvlpbG7WslXpvQLpW_JrfbRGJE8P_a91gQVYVAuYADs1HH-bDCn9nP8tfcBAfwBT1S9bT6wcL0lQNgljAjiRelMXGiX1anegQzE3W1ek9jYqPCOHtQNt28bKcyBu4td71EcGX0jLqZA-alM15T1kuklNulTSwv6GHSJaXK7lTH0oU0dKJ6bYdQT6HA_ROXnza8U7T6uC66LFGanQJLxqHhWy68jV1JnINYeFL-OZNfrXuO5MFm-_hO4vIvG9RO4o33zr4s8PiHYXSUZv0_i8Q2E68sa7I388cuBBd-IHb4lR_907PYXHo0X__Z7Grd8OYJvl8HrYXVdMJiaHdbvjBZxvglCoqiqlpiPYhNuXYWICmxl-xVpVWpDYUJmYKD5ms8CpmOtK1i7PdEc3dpo2lih7MFsLh0bHdeayNMskluDIe4w8jegbaUhEL-BjEDzsFiEb92wMu4ONtKF2BtADhvPVgwpGNYdYSVsUzDxjvC3Q4YL0RxJ9mfXNw04-zh13jn5US4p8Txx24BfRNiM7_XxJ0epRXf4jXClgHX8DvZpp6XdJrewfaNMNjXqPxo7R5LVyXXWCyVmR7PnQGc6tXZisNlQ9xqssOc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احمد الشرع درباره نام پیشین خود: «الجولانی بخشی از تاریخ من است»
🔹
من اصلاً خجالت نمی‌کشم. الجولانی نامی است که بخشی از تاریخ من است.
🔹
تاریخی که من با خود حمل می‌کنم، پر از بار مسئولیت، خونریزی، شهدای فراوان و ناله‌های بسیاری از مردم است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/678017" target="_blank">📅 13:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678016">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l00QK449epvlPN3oozruupEivP4C6m1hkuGF8XXYp0RioYnEsKcirwHFI_dVNbU99y8IoYg3AipzsfA3qufrWiI04bX1y3zC_ulODZ8ceSiDK1eA727ibFvr-frffInFT-a_Tek7G2n4PsY1oZ7vXimkJJb_Ikz8F3gMS6JbdkmXT8aREdODc-uMYTUgjYe1gs61BeMTGgyvLzdkgyjNmQTCWySY1-Znv2Swr_gmoLa_gYq1j0Nk36x8QgsuOpN3d57pEDMy8Y3BbUhSm80bfvAH2BlL-utq1AcA92VqIlNJ2miTQ_ZKaDooizJTbFbFXtD-c8yiBC72fOcdueWiGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعترافی متفاوت درباره جایگاه ایران در معادلات قدرت
آلوهن میزراهی:
🔹
چین و روسیه هر دو از نظر اخلاقی و ایدئولوژیک به‌شدت ضعیف هستند، بدون ایران، ما هیچی نداریم.
🔹
این هم سفیر چین در اسرائیل است لعنت به شما و ربات‌ها و پل‌هایتان
🔹
بدون اخلاق، شما هیچی هستید. دیگر هیچ چیز مثبتی درباره چین منتشر نخواهم کرد، بروید به جهنم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/678016" target="_blank">📅 13:23 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
