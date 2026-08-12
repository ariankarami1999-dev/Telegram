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
<img src="https://cdn4.telesco.pe/file/Wb5vikQKjnR3R064ZObBTHz1gJJuCo74W78UKpOhVvFS2Map67uxXatO8taB6JER1dNWDdtX0pdhMfysmMZxqgirDg0QiTRwZ67CR8ZHsW_VI-92p5iIsCCAFjG0B6jxrbmA0IVR3STpyV-PDjwTSMvhL2uBUwlv2KoilXLF-LfhntpGDwhks-qwkVJ2OIFOqneekX8pII0Q-D1-C0vPozQxFBzvhKZaI-BC6SqcIZijzwedTv3AwRKEatLyjBaJ1sGn3FQ-bzNd_bghF1vbMkHbnUIPbw1paApMmKXdpQsUJ7rJlDcD2N9ZWLnkW1yh-jUA-oXT2tZSVNLX1Q1OSQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 127K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 13:06:38</div>
<hr>

<div class="tg-post" id="msg-69933">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fae5c53c68.mp4?token=SyfiZdCJhCgKWwVTJ-7Mo9bcpG2BQmhZdhcRTALTO9C5Cev63X9DE9g1VJNBnbXUH4WsmbzxK7WvpZBWGeXqOJdYZjsOSMsQItBKayWKs8T7tGjoaa5p7RM7BwOptjWwDro2Isk1ki-umw_ktv0NAF4fFbq0NPZ4EklVVwNFqk_QHkprNSwvAbqZKFE9lrdOZPBtLpMxmhdF57pa2PLq352szhUSAzhzqs-bGZcvVwyDH8PFLbq8YnT-WOC4Fc4SKTAYSMvTxPRirgg9JoRPaH9uzYomSaJbMvI0wenM4cG17gWmD9zt9S5ONE79RPWSDqJypomexeftmBJxFCykvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fae5c53c68.mp4?token=SyfiZdCJhCgKWwVTJ-7Mo9bcpG2BQmhZdhcRTALTO9C5Cev63X9DE9g1VJNBnbXUH4WsmbzxK7WvpZBWGeXqOJdYZjsOSMsQItBKayWKs8T7tGjoaa5p7RM7BwOptjWwDro2Isk1ki-umw_ktv0NAF4fFbq0NPZ4EklVVwNFqk_QHkprNSwvAbqZKFE9lrdOZPBtLpMxmhdF57pa2PLq352szhUSAzhzqs-bGZcvVwyDH8PFLbq8YnT-WOC4Fc4SKTAYSMvTxPRirgg9JoRPaH9uzYomSaJbMvI0wenM4cG17gWmD9zt9S5ONE79RPWSDqJypomexeftmBJxFCykvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سفره‌ای که واسه عرق‌خوری تو زندان پهن کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/news_hut/69933" target="_blank">📅 12:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69932">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ca7afc613.mp4?token=dNgac9IfY4QDzka5ifP82kXpDwJnsvJVTLqrtdvrGNkyN9edHRIgtzTbOL8o5G50CVnSF0h07wpcbTiDzqhgkJ-QSCkZB6GeEEvkVFTc4WK8DR3BidhwuFgLSShawkpQFhBnCNaZN2p31egKFBpy0zjg4hDjGSlKAcPLx2_DfD0etnnp_dgb532IBjeL2ODk5aRgP3P3hUG_KxYmlLF7WR1Dy-2Nq_RaUYYTnSL0Nby7m6JXP3JcoMcCKSUh903vl_os9M1d6c6tdLkzamL2STT0H1KepNBkQrNxNZ0GrmEYVsacdbH9Pu-4XJ0aiab6Ivb-CaEcdesBceeor1HDfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ca7afc613.mp4?token=dNgac9IfY4QDzka5ifP82kXpDwJnsvJVTLqrtdvrGNkyN9edHRIgtzTbOL8o5G50CVnSF0h07wpcbTiDzqhgkJ-QSCkZB6GeEEvkVFTc4WK8DR3BidhwuFgLSShawkpQFhBnCNaZN2p31egKFBpy0zjg4hDjGSlKAcPLx2_DfD0etnnp_dgb532IBjeL2ODk5aRgP3P3hUG_KxYmlLF7WR1Dy-2Nq_RaUYYTnSL0Nby7m6JXP3JcoMcCKSUh903vl_os9M1d6c6tdLkzamL2STT0H1KepNBkQrNxNZ0GrmEYVsacdbH9Pu-4XJ0aiab6Ivb-CaEcdesBceeor1HDfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
تصاویری جالب ، از تلاش ناموفق یک تیم آتشبار سیار روسی برای رهگیری یک پهپاد انتحاری (کامیکازه) در حال عبور را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/news_hut/69932" target="_blank">📅 12:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69931">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fd2c3a8ef.mp4?token=X7qVTw5loN072RRP6TX4CDdmD-PIKQpamy8XmIft6lPESt4RBhnXXC3IgRuRJOqG2n2YCW4zVmbNZgBqzX-emCDX0ThcNR-hNiSW1OHoV-4OU0IISUATAfLzDvDXCl-kHCUmuczlIOtJEli6yadnWUamEyfAN4ctgEhMNIrkRNrYBxeoM7Jtesz2bZMSWVhUczqBhAsche26XO0kktWSxzrjfcTvwqN0jeL_e5g6JqH26nhBfI4Q2iBM4Pebax2V9N5wYy2BJ4RM7B_X2krYvtICWEhqhbKclxPD97u-vsaEuWVwZAu8gI0Oi1PTJT84KNVrd1aOUYd8crW8ZLWwHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fd2c3a8ef.mp4?token=X7qVTw5loN072RRP6TX4CDdmD-PIKQpamy8XmIft6lPESt4RBhnXXC3IgRuRJOqG2n2YCW4zVmbNZgBqzX-emCDX0ThcNR-hNiSW1OHoV-4OU0IISUATAfLzDvDXCl-kHCUmuczlIOtJEli6yadnWUamEyfAN4ctgEhMNIrkRNrYBxeoM7Jtesz2bZMSWVhUczqBhAsche26XO0kktWSxzrjfcTvwqN0jeL_e5g6JqH26nhBfI4Q2iBM4Pebax2V9N5wYy2BJ4RM7B_X2krYvtICWEhqhbKclxPD97u-vsaEuWVwZAu8gI0Oi1PTJT84KNVrd1aOUYd8crW8ZLWwHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیویی از هجوم انقلابیون به کاباره های تهران و نابودی هزاران لیتر مشروبات الکلی، در سال 1358
@News_Hut</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/news_hut/69931" target="_blank">📅 12:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69930">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/69930" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/news_hut/69930" target="_blank">📅 12:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69929">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ahjHkbDS7PpcszymJ3A_Y45CWJKXVCrGxuQTv1SzWg4qDOk1-Q_3lV4pkk7FLci3YUhKsvUdHMrHLkK_TT6CsBNvUNMWoxxCiiD2zwVT0MPenvgMqL_sFtENVwYBhs-AaZ7MvqLWcorW1EdsvihclyNUiCdMUBmP-bWBb96HPqE4Rz5Sv-Zkpqx4lFhQ5F05xVSRVMqRPSuBsIDiGvZhuCEzdqSbN7Sow_yKjNrbxaqCLCA7I9h1wksvSFvNhmbQOuOHtz-Ph09jDOz_lE9waBCcPl9G-mHXGS15JRlnbbED-77Co0yBosLPmulN-aaODQaerFkvXrx8stebNram4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌     ‌ ‌ ‌ ‌ ‌    ‌‌ ‌‌‌  ‌
💯
‌
فینال سوپر کاپ اروپا
💯
🆕
دیدار فوق حسااااااس
پاری‌سن ژرمن
و
استون ویلا
رو با آپشن های تخصصی در
MelBet
پیشبینی کنید!
💯
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای، مطمئن و در کلاس جهانی پیشبینی کنید!
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/news_hut/69929" target="_blank">📅 12:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69928">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9676b05e8a.mp4?token=KwyWNXKBKxXlG7JbWm_fwHain9JJE7BWEOpr5oQ1xwVX7NTE3d-Wb22BaoFssB8yiqTqUgwh3Rudxe6U9m620A48kaDgsnEWCsXM882o6rFFJLtMOcBcTPog8ToYp6tE-jj91RnCfsZtiwy3w-Zod3yMJBS2OjXkPi65X2VmoM29bZS_QDn1l0zq6XXykg6EDntVCbkYTYlPzR2RAsOHwRvOPze0LsFHQY_PD6M1B9FSSE8bGdS09ITyCh8ZzY9q1E6hhS0jD7Z926N7CxUo5Ae-B4nq_vfwc8PE5dPCTOof93MThu6UYwiFojOqkCmrYkGh72-7NQi_6mdZTAG9yg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9676b05e8a.mp4?token=KwyWNXKBKxXlG7JbWm_fwHain9JJE7BWEOpr5oQ1xwVX7NTE3d-Wb22BaoFssB8yiqTqUgwh3Rudxe6U9m620A48kaDgsnEWCsXM882o6rFFJLtMOcBcTPog8ToYp6tE-jj91RnCfsZtiwy3w-Zod3yMJBS2OjXkPi65X2VmoM29bZS_QDn1l0zq6XXykg6EDntVCbkYTYlPzR2RAsOHwRvOPze0LsFHQY_PD6M1B9FSSE8bGdS09ITyCh8ZzY9q1E6hhS0jD7Z926N7CxUo5Ae-B4nq_vfwc8PE5dPCTOof93MThu6UYwiFojOqkCmrYkGh72-7NQi_6mdZTAG9yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قیمت های پشم افکن خونه و برج توی فرشته تهران بعد از جنگ که به متری 2 میلیارد تومن هم رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/news_hut/69928" target="_blank">📅 11:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69927">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6983998d5.mp4?token=wBla5BbLopaBzQ7kHZweGJrlRe0m3o4shvuMNfdHirhJatWcKE_jFjge-b143T6USt3MSof3DdarHsPprFDwMktlbpDv_OhXW35Rs49rTJileFL9UAhvu2NeqFt_dNI-AJW7DYFMeqoRkbGeLBpyIIWStlkBjKFrCqoPtZQAQVjwswB_rmgXn6kA-FjvVDn7T6EWkhm5IqfKLBGMxtSBf1zH5M9LQp_MWbXvyDCO8oMN1ZzZQeDl2eZ52pDjUgxY7XynVxXV5WE5bMw0RTpSTqD9tUMiXrWPf0uTIzdLjqv0wtBPkty387TGl-NBgS1ini3ZGn_xsfFOGL7_MXA-xCpueMD0e4nN9zAIdyhE42QGSKV0uB3Tgtypxf4q_5h6TGEliLzwl-4x88-rzlsZILiErNCYwjZtL7cPYMiWfVjP5VYCyB0U1ujNgu7M2eJYD60KiF68LWe6wWPQjOdPViAP8m9BrQlCzqOiWnRo0tvuH1VZ9baV5j28vUwFLgM7XLPUmNz5UEZwWGv25IfWRCfaBCBu7uIAky082bNDzuoNDYg48jDjFNJWajItJdniPhaXuUjpoXE3LrBjKjfyX4V8McELNFgRi-eftHT7ZaQBDqQWMUH-3auIWLm0jnSwmdUmnZfrNLNytHiNREQY1mFYEO_J8qI4VQXAC34W0Gs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6983998d5.mp4?token=wBla5BbLopaBzQ7kHZweGJrlRe0m3o4shvuMNfdHirhJatWcKE_jFjge-b143T6USt3MSof3DdarHsPprFDwMktlbpDv_OhXW35Rs49rTJileFL9UAhvu2NeqFt_dNI-AJW7DYFMeqoRkbGeLBpyIIWStlkBjKFrCqoPtZQAQVjwswB_rmgXn6kA-FjvVDn7T6EWkhm5IqfKLBGMxtSBf1zH5M9LQp_MWbXvyDCO8oMN1ZzZQeDl2eZ52pDjUgxY7XynVxXV5WE5bMw0RTpSTqD9tUMiXrWPf0uTIzdLjqv0wtBPkty387TGl-NBgS1ini3ZGn_xsfFOGL7_MXA-xCpueMD0e4nN9zAIdyhE42QGSKV0uB3Tgtypxf4q_5h6TGEliLzwl-4x88-rzlsZILiErNCYwjZtL7cPYMiWfVjP5VYCyB0U1ujNgu7M2eJYD60KiF68LWe6wWPQjOdPViAP8m9BrQlCzqOiWnRo0tvuH1VZ9baV5j28vUwFLgM7XLPUmNz5UEZwWGv25IfWRCfaBCBu7uIAky082bNDzuoNDYg48jDjFNJWajItJdniPhaXuUjpoXE3LrBjKjfyX4V8McELNFgRi-eftHT7ZaQBDqQWMUH-3auIWLm0jnSwmdUmnZfrNLNytHiNREQY1mFYEO_J8qI4VQXAC34W0Gs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداشمون در یک دقیقه به ۱۳ نفر پیشنهاد رابطه داد و  همشون هم ریجکت کردن و تونست رکورد ریجکت شدن زیر یک دقیقه دنیا رو بزنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/news_hut/69927" target="_blank">📅 11:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69926">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
لحظه نابودن شدن خونه های مستحکم و نوساز توی کلمبیا بر اثر زلزله!!
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/69926" target="_blank">📅 10:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69925">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72ecf27139.mp4?token=Stv_mSYYjzR09AzJ4zxfoD76YjPObUDMBueYAJkIo-a6I-yOEsuFLObi-AXrtwT5RlF4Trrk2ayyhXX_VzUfrsOILM_X5jbNTmcbf0-yJXqeTdicWJWi5NPppwJkFs3XBYhZw5UehtyBNBl8KfVZcve88ElhFHQQQ9Kn7X7hWItkdU3yuv0RGX1wOJCNG74sat4i_e6sngam8T8gyQrZgOs9Wzo_gqyp-eNOHrr7k2lIZYqi3FqASps7t9IZOAYOiI0NagPMejHlDQsj09bUqAkW0r8u8p-ue6lpisNmUwyLmfp3bJItj5mMCR-DCbd_gD2rCwJqcWpqu2KNjwlRxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72ecf27139.mp4?token=Stv_mSYYjzR09AzJ4zxfoD76YjPObUDMBueYAJkIo-a6I-yOEsuFLObi-AXrtwT5RlF4Trrk2ayyhXX_VzUfrsOILM_X5jbNTmcbf0-yJXqeTdicWJWi5NPppwJkFs3XBYhZw5UehtyBNBl8KfVZcve88ElhFHQQQ9Kn7X7hWItkdU3yuv0RGX1wOJCNG74sat4i_e6sngam8T8gyQrZgOs9Wzo_gqyp-eNOHrr7k2lIZYqi3FqASps7t9IZOAYOiI0NagPMejHlDQsj09bUqAkW0r8u8p-ue6lpisNmUwyLmfp3bJItj5mMCR-DCbd_gD2rCwJqcWpqu2KNjwlRxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت های یک مقام حکومتی رو ببینید که باخنده درمورد شلیک به سر معترضا صحبت میکنه:
ما به پای معترضین شلیک میکردیم ولی میخوابیدن میخورد به سرشون
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/69925" target="_blank">📅 10:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69924">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a54f6b8d.mp4?token=tZ-F7KlFJ7XScrbeghwjetZMK6GKK95JUkiH1IZm64Y2CrM8uX5WLun2wx59wB1uAnjP1cDqOHgE3eDHmxXCBCwS2KWTIzjUM7094i68nrJyxlgpYiehFLqUp1wE8XWIl7D8GX6yKpBTdtmq5DdlU-B5d7sSNDnPCJsB_5zEuyTd1ZJ-E-moKLnOmODKa8B4Rxhtp9sBeQ1HpHche6ujA1HL7XF5W_lKVg943nSdDfmY-G1_nR-xk4b4bSb_eFO3VWnktxJp-mWp8knAc2f0CPRP81WrRWTttWdH_ero_jpdh61deOV1YLWXNYHAP3BP9lCGT8r53B9prF5kec7dcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a54f6b8d.mp4?token=tZ-F7KlFJ7XScrbeghwjetZMK6GKK95JUkiH1IZm64Y2CrM8uX5WLun2wx59wB1uAnjP1cDqOHgE3eDHmxXCBCwS2KWTIzjUM7094i68nrJyxlgpYiehFLqUp1wE8XWIl7D8GX6yKpBTdtmq5DdlU-B5d7sSNDnPCJsB_5zEuyTd1ZJ-E-moKLnOmODKa8B4Rxhtp9sBeQ1HpHche6ujA1HL7XF5W_lKVg943nSdDfmY-G1_nR-xk4b4bSb_eFO3VWnktxJp-mWp8knAc2f0CPRP81WrRWTttWdH_ero_jpdh61deOV1YLWXNYHAP3BP9lCGT8r53B9prF5kec7dcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی:«بازندگان و برندگان انتصابات جدید در جمهوری اسلامی چه کسانی‌اند و آرایش جدید قدرت چه چیزی به ما می‌گوید؟
🔴
انتصاب محسن رضایی به دبیری شورای عالی امنیت ملی و حسین طائب به فرماندهی بسیج، دو پیام مهم دارد؛
یکی رو به بیرون، درباره مذاکره، جنگ و رویارویی با آمریکا
دیگری رو به داخل، درباره مهم‌ترین نگرانی حکومت: خطر خیزش دوباره مردم ایران.
در حالی که هنوز درباره زنده یا مرده بودن مجتبی خامنه‌ای و میزان سلامت او تردید وجود دارد، سپردن بسیج به حسین طائب، یکی از نزدیک‌ترین افراد به مجتبی، یک پیام روشن دارد:
نگرانی اصلی حکومت، خیابان است.»
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/69924" target="_blank">📅 09:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69923">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa002b9fb9.mp4?token=GDtstVzFlYS9q1WaO1FHSMSEtmEmdd6XW2Hdj-SXQyHrn-T-EUCdowTV4sNmn3iucvYLJEHzpduWA7TGSHq2V53eUlKcpKzHxZas1l6jvJLE49CulJFTRpv-K79hVNBF_IrFux3v7zXLDZwx7HYYwqw3H69Y0y4K8tm1OnLVNA4wB_hR1Y1aaWwOGAQiZnZVdSc5yDwDPCU9KtNXHniBvsMGRLjHBp8qALRwXi3vJZTYIyR7_lQOzZmRGYNGu8YMqOEyMM0t9g_9IpBX2FjFfNcMkvtlUmxBLRiOV0oASuLE9-xQKZoVMlAWWupmlK67VWJwz7I9ANrtsDlGgtrL7ajD1FHe8jVoIzIxfV0uMQAML9xy45c3NZWK-ZN3xCsX7tAoOM6KjVzOYmjFPMzwpPGFf6sx0fJ6GnThiJjyPpW7ZEFRHqwTI5yjP8QLiJqSHR49jpSuhPPznTAOK0s71y2uyOeYqV6U1Pxdb0lGiWqQAt2DSjZUkIrYE6r8vL9qaHRmPlBbHvAGGrCLJj9Im33l-vqI2aD7Mw2RGxm_mFqKMDdZ85adzvVznZtSqP4emD5raxfa757Ht-DmMdAyppzNTKC-yiUqjuwLPvMkUgU9SxbKVDYctAqeE0OJZudMMmVGlpjsRfeNbLda_VAoSq1onw2VaUZg-VZ1iGYCF0I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa002b9fb9.mp4?token=GDtstVzFlYS9q1WaO1FHSMSEtmEmdd6XW2Hdj-SXQyHrn-T-EUCdowTV4sNmn3iucvYLJEHzpduWA7TGSHq2V53eUlKcpKzHxZas1l6jvJLE49CulJFTRpv-K79hVNBF_IrFux3v7zXLDZwx7HYYwqw3H69Y0y4K8tm1OnLVNA4wB_hR1Y1aaWwOGAQiZnZVdSc5yDwDPCU9KtNXHniBvsMGRLjHBp8qALRwXi3vJZTYIyR7_lQOzZmRGYNGu8YMqOEyMM0t9g_9IpBX2FjFfNcMkvtlUmxBLRiOV0oASuLE9-xQKZoVMlAWWupmlK67VWJwz7I9ANrtsDlGgtrL7ajD1FHe8jVoIzIxfV0uMQAML9xy45c3NZWK-ZN3xCsX7tAoOM6KjVzOYmjFPMzwpPGFf6sx0fJ6GnThiJjyPpW7ZEFRHqwTI5yjP8QLiJqSHR49jpSuhPPznTAOK0s71y2uyOeYqV6U1Pxdb0lGiWqQAt2DSjZUkIrYE6r8vL9qaHRmPlBbHvAGGrCLJj9Im33l-vqI2aD7Mw2RGxm_mFqKMDdZ85adzvVznZtSqP4emD5raxfa757Ht-DmMdAyppzNTKC-yiUqjuwLPvMkUgU9SxbKVDYctAqeE0OJZudMMmVGlpjsRfeNbLda_VAoSq1onw2VaUZg-VZ1iGYCF0I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
من به ایران اعتماد ندارم. من آخرین کسی هستم که به ایران اعتماد می‌کند. آن‌ها مدام به من دروغ گفته‌اند.
ما در حال حاضر کنترل کامل تنگه هرمز را در اختیار داریم. آن‌ها کنترلی ندارند؛ ما کنترل کامل داریم. آنجا در اختیار ماست.
و شاید زمانی آن‌ها دست به کاری بزنند و آن‌وقت نابود خواهند شد. اما فعلاً در موقعیت بسیار خوبی قرار داریم.
ما با کشوری سروکار داریم که ۵۰ سال قلدرِ خاورمیانه بوده است. اگر دقیق‌تر حساب کنید، در واقع ۵۱ سال می‌شود، مگر نه؟ ما چهار سال بود که می‌گفتیم ۴۷ سال؛ و حالا دیگر آن‌ها قلدرِ خاورمیانه نیستند.
🔴
ترامپ درباره تغییر هواپیما در آنکارا:
این موضوع صرفاً به «سرویس مخفی» (تیم حفاظت) مربوط می‌شود. من فقط از تصمیم آن‌ها پیروی می‌کنم؛ بنابراین تابع نظر سرویس مخفی و ارتش هستم.
آن‌ها می‌خواستند که من با پروازی دیگر و هواپیمایی متفاوت سفر کنم ــ که از نظر ایمنی تفاوتی نداشت ــ اما چون خواستار انجام این کار بودند، من هم پذیرفتم. من هر چه آن‌ها بگویند را انجام می‌دهم.
گمان می‌کنم تهدیدی وجود داشت؛ البته من خیلی پیگیر جزئیات آن نشدم. من با تهدیدهای زیادی مواجه می‌شوم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/69923" target="_blank">📅 09:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69922">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/69922" target="_blank">📅 01:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69921">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=IMji__YcFJlviLGTI_s5j7bEjpZ5-2ZstFa9XPTpc8mj2gnY_yYHf3lkxbxZXFrex3F5s50PcMX-JgQ9bUJ1h9HFJS2qUbg3IzHOSt343eblKxTMmgP8Mt1LpsQVHQ51iw7S9DTvbvIfXnI2EacAlDOl9mFyp3LljYHywsMCpVtSIsszw4gH2cv7hRjm4DqUR-K-wn0bvKFj3I0I4isu6Mz5TdzTGU1a-b8uCE4Xc68g_LT53MX-EFNCMSwdpXYkZtWX1gpI9xZLhisOrwdFa0_ds4i4ZFpQILrbh8Q9djPen1vFu7Ic0Q2u28bNxYtTKTp6kFkk2RW2rTdi3W7TaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=IMji__YcFJlviLGTI_s5j7bEjpZ5-2ZstFa9XPTpc8mj2gnY_yYHf3lkxbxZXFrex3F5s50PcMX-JgQ9bUJ1h9HFJS2qUbg3IzHOSt343eblKxTMmgP8Mt1LpsQVHQ51iw7S9DTvbvIfXnI2EacAlDOl9mFyp3LljYHywsMCpVtSIsszw4gH2cv7hRjm4DqUR-K-wn0bvKFj3I0I4isu6Mz5TdzTGU1a-b8uCE4Xc68g_LT53MX-EFNCMSwdpXYkZtWX1gpI9xZLhisOrwdFa0_ds4i4ZFpQILrbh8Q9djPen1vFu7Ic0Q2u28bNxYtTKTp6kFkk2RW2rTdi3W7TaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a20
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/69921" target="_blank">📅 01:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69919">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0c53c5d72.mp4?token=CDjHmWIMNl80RjVBGXHog3qk2fHnCf75eCwNoJVMPO-m0enE2_cSRU-eNnBjkxJ49p5v3YHFqlqFbmCuV1pFtKXj19jI_MjuJ6fIYPhlG2GRG3VRKO_3xUkSG_6Ww953IWjDzOI6Wzx17JnMe4ak9S6vxxB5nhq1x-WJw2R88p8MuKF8gp0ZCTyd_qIYBoyfuLZgvZ0Hu6TlYo5Ajn3tV0Mti-ubXYrUzzKOUC7vFDV6t2MrsINWwVzh8djrDB6ZxGeEccGx4II5Fw-vHPEvbiQCxWqr85iJVTP4Enyi4iUFgUaS6f903FVGebJEN0tUs8lETYoGf9TWbClrEWt8nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0c53c5d72.mp4?token=CDjHmWIMNl80RjVBGXHog3qk2fHnCf75eCwNoJVMPO-m0enE2_cSRU-eNnBjkxJ49p5v3YHFqlqFbmCuV1pFtKXj19jI_MjuJ6fIYPhlG2GRG3VRKO_3xUkSG_6Ww953IWjDzOI6Wzx17JnMe4ak9S6vxxB5nhq1x-WJw2R88p8MuKF8gp0ZCTyd_qIYBoyfuLZgvZ0Hu6TlYo5Ajn3tV0Mti-ubXYrUzzKOUC7vFDV6t2MrsINWwVzh8djrDB6ZxGeEccGx4II5Fw-vHPEvbiQCxWqr85iJVTP4Enyi4iUFgUaS6f903FVGebJEN0tUs8lETYoGf9TWbClrEWt8nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی یک مخزن در اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/69919" target="_blank">📅 01:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69918">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c665ef2ed.mp4?token=BGLhLE2EfDQ3At4NXmIT0pJdECfDDvlo32bLKCbPcCl2cW90h2ZbZh0c2Vuo3As_LNQhZQe8LWwSoLhNNJGDj6a7deEFYhNeWASwJH3cF8QBXudOGrf7m3V3NmCcPPyiowZt4nVv5I9yXN2bcrNr0zBqBaFLOIXZAxQL4j7v6P0wmJGn_-nirNDx00OZhTnuRGzGXZ8Mx6k1reRYTxH3owDLNQ-FczLx197y44_A7SFqO4ZX2CQf0tYktrzp-PEw8KAwCOWGS8Ils_-42r3eQVSef8hSMKtGuzTk-0Lb7it7dKtamxZ3kVPdF38YAwDEpZapsEd9MR3fwW0CoOvgfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c665ef2ed.mp4?token=BGLhLE2EfDQ3At4NXmIT0pJdECfDDvlo32bLKCbPcCl2cW90h2ZbZh0c2Vuo3As_LNQhZQe8LWwSoLhNNJGDj6a7deEFYhNeWASwJH3cF8QBXudOGrf7m3V3NmCcPPyiowZt4nVv5I9yXN2bcrNr0zBqBaFLOIXZAxQL4j7v6P0wmJGn_-nirNDx00OZhTnuRGzGXZ8Mx6k1reRYTxH3owDLNQ-FczLx197y44_A7SFqO4ZX2CQf0tYktrzp-PEw8KAwCOWGS8Ils_-42r3eQVSef8hSMKtGuzTk-0Lb7it7dKtamxZ3kVPdF38YAwDEpZapsEd9MR3fwW0CoOvgfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اولین ویدیو منتشر شده از عروسی رونالدو و جورجینا:
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69918" target="_blank">📅 01:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69917">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d80bd3b48d.mp4?token=VJDvgNFKSgOPEGDIMbx6aUoEedqNPCh5ZzAScX9g34BsalSP9aBx0qddY1dQ6iS8965PU8KsOmHztCzy_kq89y0zJ2HRF0RTV4GNWEtMKDNvTJYa1WdWZev4kcmqF_qBfdzY9rgZO218IvtHFM3iF5Nqh_MhqTt_YlUevo-jNrDInWVx5vcPXUibcG5lHU-r_mLNjc6OmDJue-wkQW12Zg7bgiq6Z6jhqAlaB4-drmDMohmqmo55xX_SlkhFufGDJcufuBGvWKTDUI1iHingAD2bCBCdZXnH6fD5xXnHCJGEmVWtmbse8paKml54MXzGSwRUrWEL8Y1aepYuwdu49Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d80bd3b48d.mp4?token=VJDvgNFKSgOPEGDIMbx6aUoEedqNPCh5ZzAScX9g34BsalSP9aBx0qddY1dQ6iS8965PU8KsOmHztCzy_kq89y0zJ2HRF0RTV4GNWEtMKDNvTJYa1WdWZev4kcmqF_qBfdzY9rgZO218IvtHFM3iF5Nqh_MhqTt_YlUevo-jNrDInWVx5vcPXUibcG5lHU-r_mLNjc6OmDJue-wkQW12Zg7bgiq6Z6jhqAlaB4-drmDMohmqmo55xX_SlkhFufGDJcufuBGvWKTDUI1iHingAD2bCBCdZXnH6fD5xXnHCJGEmVWtmbse8paKml54MXzGSwRUrWEL8Y1aepYuwdu49Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نظر محمدرضاشاه پهلوی درباره نفوذ لابی یهود در آمریکا:
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69917" target="_blank">📅 00:21 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69916">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJELHkLyB_FIWXKu2R7vAXTSvb635MgDUc4geghaMkRoQz4Q_hkE8mU52S_Gv7FMgvIhpsKkw-9LpAc-Z69lV7LZOiNtQq8RYPBDtPcTm_EqUGkK1M70DVVmJlIL4lYJfq97A9qaYNTrJk35TwBsBOlDIuI27wN92xi2Z0XwbmVqEanQb1Rm1c3vBZYZAgI06L9jy_8uluMcGpUIeibhtcQha5l7kowrYgJbgPcX6dfv1apC2KnnujlaIxNtJKz1DhrTYMTBKTGnVkBdbeMSiA5c-SVVim-f-dmHtZKvfwUwH4JfVwdtR_O0ZBcmbL0GMy0kkJbHF4jyvBK3Lap63Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رونالدو و بانو جورجینا رسماً ازدواج کردن.
رونالدو هم گردن گرفت بالاخره، دیگه وقتشه تو هم گردن بگیری
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69916" target="_blank">📅 23:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69915">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d1d1d4e3c.mp4?token=UXSce1fnygdLNIyfCs7ho4gKv6JtN76hz45rOhBBOIG4E7yLIfSyyT8MY1LQ8Ydl2PR6uop00_bEj3xgRh31rMlMMYMFZtviS6LXoZbGQXvzudvaysTmNP8Balinw68Wb20-7c1pLJ117V3ubTGR08wtyLIaiLq4DLDfUou5CjArerpicL23jXt87RUImyOSkmm0KDG9wp7WWMCJDpmA98DvNJeDVBMZhNRfQ_BvkyELU-mbtAOQt94YtlNQfx4W5Wfr5aM7muG78qMgiA4yPj-iCjWmO1no7f1_pkWue-1d0C9_DjlGj8_7PtsV3co9LmHuYGKD0JITwTlop6BmFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d1d1d4e3c.mp4?token=UXSce1fnygdLNIyfCs7ho4gKv6JtN76hz45rOhBBOIG4E7yLIfSyyT8MY1LQ8Ydl2PR6uop00_bEj3xgRh31rMlMMYMFZtviS6LXoZbGQXvzudvaysTmNP8Balinw68Wb20-7c1pLJ117V3ubTGR08wtyLIaiLq4DLDfUou5CjArerpicL23jXt87RUImyOSkmm0KDG9wp7WWMCJDpmA98DvNJeDVBMZhNRfQ_BvkyELU-mbtAOQt94YtlNQfx4W5Wfr5aM7muG78qMgiA4yPj-iCjWmO1no7f1_pkWue-1d0C9_DjlGj8_7PtsV3co9LmHuYGKD0JITwTlop6BmFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
روحانی:
صدام پس از کویت به دنبال عربستان و امارات بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69915" target="_blank">📅 23:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69914">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🇺🇸
سنتکام اعلام کرد نیروهای ایالات متحده از زمان تقویت محاصره بنادر ایران، ۵۵ کشتی تجاری را بازگرداندند، ۳ کشتی را غیرفعال کردند و برای اطمینان از رعایت مقررات، ۲ کشتی را بازرسی کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69914" target="_blank">📅 22:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69913">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaTDaFlrweW6jENPOUEmp_UQ1uByyOCbOriYgyxPfrv6_vtLZEEBeDJ_NgMMAOx3q-7rCAk4LKH07P5t3R_ywK0QjG7_nOHmOqlTrp8pN7khskWyPR7s1eyO2o6nMUUDAO22SV-WzLVDSHrTPWKSUrj9pFHVyxx0Gqv6neQgC3CBrSRtgJ7tc-4zbB8oqqLJCMaUCSuYuxEas4EbjWdK8ooemk0yVgP7xchx-mhv4wsbvZCiu6llwp54ELZx975WtEMZutNuCN6T-xV1BLkZCR94zUWYisRK8qipKvezptaYn83i1DuyEtt518r0i1K_jTl0MMG7030VH5OjKQBRjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
📰
وال استریت ژورنال:اسرائیل دولت ترامپ را در جریان اطلاعاتی قرار داد که نشان می‌داد توطئه‌ای احتمالی برای هدف قرار دادن هواپیمای ریاست جمهوری با موشک‌های زمین به هوای دوش‌پرتاب وجود دارد.
مقامات امنیتی ایالات متحده متعاقباً پس از اجلاس ناتو، رئیس جمهور ترامپ را با استفاده از یک کامیون پذیرایی فرودگاهی در آنکارا به یک هواپیمای نظامی جداگانه منتقل کردند، در حالی که مارکو روبیو، وزیر امور خارجه، دیگر مقامات ارشد و خبرنگاران به عنوان بخشی از یک عملیات فریب در هواپیمای ریاست جمهوری باقی ماندند.
در نهایت هیچ موشکی شلیک نشد و هنوز مشخص نیست که تهدید گزارش شده چقدر معتبر بوده است. این عملیات اولین باری بود که چنین اقدام فریب‌آمیزی در دوران ریاست جمهوری ترامپ استفاده می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69913" target="_blank">📅 22:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69912">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f811c57f.mp4?token=DptFxnPWfJlHOGpCqO7KcFw-a_6851Tv6JiuggyYM22atizUhqM4TQW3u70O6gAJR18TWdj3UBCktzT06mp64CgnUB8ZFlWK454mEd8AGBUVxUn_M1ek5bjj1bZ3nVeXNgFFTQ0SiRbcqxwkB-hGt9Yl2s5smFFv_D9iLXvWfNtJa1SlH-fmmpC23ATjprHtf5uBacAenNMYeMGa_7jGNUVPnaq4bTva6k8upxQ7B4F5KJoasB065P83pG6LO641uLSJVkS3LzWQaGinzGRkvTAw8EcnAt-7YLJNw1kwIqbk3Lex6jKrZNHyMp6PyUA1krMXQw2yIJAANpfWek3pRU3J3n3AWUzIswL4vQuBor_KrZ_D9ddw48Zs0idRRVixQbBSYtEclPyiLB2Mu7tcw1Zkx5NgL-YuuJL1tM7oEC8nAqLzTK95_fS8DKB4q1ReH_23qjpx1zndRHyvdeUFSwz4cU8rbnjQGCncL7nxFxOOZDro88j4YBEKQmPmlANdC3SYRjaEfegvPQ9QBgFQztSAskyX0ucXVFQvURLBYfGckatn1fk9UPNdGKWqQXLUp9L7xED5u20ecM2w1Egq8buDvihclF1kMPt72Yp_9_UOFJRFVPqLc4assS30eQlDnKjft8HGB-rYybBzKafQ16d80L5JBUzoOz_OH0xX2Oo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f811c57f.mp4?token=DptFxnPWfJlHOGpCqO7KcFw-a_6851Tv6JiuggyYM22atizUhqM4TQW3u70O6gAJR18TWdj3UBCktzT06mp64CgnUB8ZFlWK454mEd8AGBUVxUn_M1ek5bjj1bZ3nVeXNgFFTQ0SiRbcqxwkB-hGt9Yl2s5smFFv_D9iLXvWfNtJa1SlH-fmmpC23ATjprHtf5uBacAenNMYeMGa_7jGNUVPnaq4bTva6k8upxQ7B4F5KJoasB065P83pG6LO641uLSJVkS3LzWQaGinzGRkvTAw8EcnAt-7YLJNw1kwIqbk3Lex6jKrZNHyMp6PyUA1krMXQw2yIJAANpfWek3pRU3J3n3AWUzIswL4vQuBor_KrZ_D9ddw48Zs0idRRVixQbBSYtEclPyiLB2Mu7tcw1Zkx5NgL-YuuJL1tM7oEC8nAqLzTK95_fS8DKB4q1ReH_23qjpx1zndRHyvdeUFSwz4cU8rbnjQGCncL7nxFxOOZDro88j4YBEKQmPmlANdC3SYRjaEfegvPQ9QBgFQztSAskyX0ucXVFQvURLBYfGckatn1fk9UPNdGKWqQXLUp9L7xED5u20ecM2w1Egq8buDvihclF1kMPt72Yp_9_UOFJRFVPqLc4assS30eQlDnKjft8HGB-rYybBzKafQ16d80L5JBUzoOz_OH0xX2Oo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
پرواز بالگرد آپاچی۶۴ آمریکایی در نزدیکی قشم
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69912" target="_blank">📅 21:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69908">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b1WUNPlFdZkM_HjxFoT4VJwk6WC-nMklk980PxhF44Lp98852B7wOjtg0cyZOXiAPyR96T_4p1CPVTail4-AksO2XzuNN2EMHgnRHrCvUx34ICnDeYXDsjv3CS2ltHbf5Rra_WQlXp2Zvo7uzj4BKaoJaA37dKnx8SEPlEwYutd18X-BEa3ptkkdDkgKlcdij2whV7efqT8Xvl2vMlY5Dyt7hsrq2njy4mR5OAg2WCWzVt3jMvi6GQ7seszFDXjrB0bj-nyXVKXdC9erPSsBjddnXprIP_MTu8hJdz7gN2A5Rd3LO2BWGjSF_ROzmoxj1DWc9FWYG5_ZsOsOL1Va1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qv80zNPmg5Ubj5fh6i04tpv-NWRq7h-daejE0gA7SRMLOS5hiLJ0oao5mqbBxlYogGyd908WCz6YJ9EBjQ6-N1HCEkBL6kS3mQxwFeFiC9jUNMDip8Satn4ed7BsRHBuPccizckY-TUOrhKFWrfnW659FJQe3RItgsWgQ2KXMt_Hn2I_L3g-yNOhTs34VsQ5xmfF-lsUpIayGQ1LxNt7wzYUOmXpMCsJsVF-JqJldJn_TF8_8tIwPZk2G6x1u6KJ_WwiSZs6xCx1ZGJk1tIo3OZTMQkuTQB-KOWDEcN8aPImMc1WHOrv48tmI9LQVX2U_mAuQ-L9473iH9gJMwAvqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RDFYdFDC5tvxqyGFJ4IxEP7CRhvvm8d2QKmWlfewvIk_iNWgdjlEPwRROu8H5RAfHwCic25IGbJmCyR9amklNEvnuaA2cujRaXDHihkVxASUCG_HfWwiz85vA4bGipIiRwexsbhzpprgWCTNYDoiuntbvaR7HQRz0nELOHC_g-6XEfabbpQqz3J4xoKcKr8Op2ichIy4-hiUVg-1ANgoC987Ko01YGxPHI7kv9Fun2AngP-8bOyJmGAX6ABIvCxtfE7X_0QgUEhtFp8fDnnhF7j1IS-UUYNrvqCJRN2ViITW0an-Dw1wpJRk1XkQpM8cBrt-ohIKSw7RODv3djPlLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbbe5c4282.mp4?token=hyjBIDsDZV9N4eP4HsAYvkpjjmFkYKHdfszekCOV9L-PVzysureZnvQVw3ztKUMfUGkK-gcFEeg4IWpqCTLeTn5nQcU9-7HVQ0qlp5-lY2dSLXTIzMRFfe0Bq88Ix0HlkTd8Ntd_cH_RA0hTHVlYDhpzdWc4nTvjbaEKNHto-jF7i3erl09nckZhnB2WOgPhhZw60ETyQvRMJKMZlQ_d8RGEBBXZ4cGyf4bTI7LHq8L09YWfDr6mc1s3WBr_7r_FydAuPf8j8n4r8xcFVRlppCpFPgXJQaoRrnkvYjjIpws2ZghQTX0JhNMDItH6rLEulmI4aGoswp8B3cOM3-uC-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbbe5c4282.mp4?token=hyjBIDsDZV9N4eP4HsAYvkpjjmFkYKHdfszekCOV9L-PVzysureZnvQVw3ztKUMfUGkK-gcFEeg4IWpqCTLeTn5nQcU9-7HVQ0qlp5-lY2dSLXTIzMRFfe0Bq88Ix0HlkTd8Ntd_cH_RA0hTHVlYDhpzdWc4nTvjbaEKNHto-jF7i3erl09nckZhnB2WOgPhhZw60ETyQvRMJKMZlQ_d8RGEBBXZ4cGyf4bTI7LHq8L09YWfDr6mc1s3WBr_7r_FydAuPf8j8n4r8xcFVRlppCpFPgXJQaoRrnkvYjjIpws2ZghQTX0JhNMDItH6rLEulmI4aGoswp8B3cOM3-uC-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دریک، از بزرگترین خواننده‌های دنیا؛  با 140 میلیون فالور و ثروت 250 میلیون دلاری [50 هزار میلیاردی]  وقتی ممه‌های بزرگ یه دخترو دید، نتونست تحمل کنه و براش هاپ هاپ کرد  @News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69908" target="_blank">📅 20:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69907">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bcf8b7227.mp4?token=GDAb3PLrKQW5fhvI-pEU-NyOTkmpnSSoDgVQg1y-TLTw0ZRo3MTsV8QU0gSbsLjpVLPJ9Dxoa-pLs5FVgfpDzSPtdBzkbIHs1Y0TS7UXYBW-Q2lJ58a9wqvTBVByd_K2RtJAgJfjCkclEupTK_qAj1XzVLa1K2kK9CBo6D7Ri8Y1vEXYZMsuPmYmaANi79KFOwtnRph_tTECIRdmCZ6eh3gO9PnP2YFZWC9adb9v6ds48RUtBGrah3Y1dBNmehmr1LHR8FNj5HuKTsXRU_DNVT5A-X_GOBKl1euuEMKssrVnr6ws-dcChlm4_jm9N5yzZO_qv4iD0BPYBku688Pnkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bcf8b7227.mp4?token=GDAb3PLrKQW5fhvI-pEU-NyOTkmpnSSoDgVQg1y-TLTw0ZRo3MTsV8QU0gSbsLjpVLPJ9Dxoa-pLs5FVgfpDzSPtdBzkbIHs1Y0TS7UXYBW-Q2lJ58a9wqvTBVByd_K2RtJAgJfjCkclEupTK_qAj1XzVLa1K2kK9CBo6D7Ri8Y1vEXYZMsuPmYmaANi79KFOwtnRph_tTECIRdmCZ6eh3gO9PnP2YFZWC9adb9v6ds48RUtBGrah3Y1dBNmehmr1LHR8FNj5HuKTsXRU_DNVT5A-X_GOBKl1euuEMKssrVnr6ws-dcChlm4_jm9N5yzZO_qv4iD0BPYBku688Pnkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
رامین رضاییان:ما خودمون از عمد به بلژیک گل نزدیم و تیم بلژیکو نبردیم.
🔴
چرا؟دلیلش:
جلوی بلژیک شما دیدید مهدی طارمی یکاری کرد تیمه ده نفره بشه.
مهدی بخاطر تیم به بلژیک گل نزد.
من باهاش صحبت کردم داداش چرا نزدی گفت داداش اگه گلو میزدیم فشار وحشتناک میاورن و جبران میکردن، حقم داشت مهدی
🧠
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69907" target="_blank">📅 20:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69906">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🇮🇷
فیلد مارشال محسن رضایی دبیر عالی شورای امنیت ملی:
آمریکا باید جنگ رو پایان بده و خسارات رو بپردازه.
به هیچ وجه کوتاه نخواهیم آمد.
تمامی جنگ ها باید در کل جبهه مقاومت پایان یابد چون شرط اصلیه.
شروط دیگر را نیز از طریق میانجی ها گفتیم به اونا ک باید بهش عمل بکنن.
توافق با عمان ربطی به باز شدن تنگه هرمز نداره.
پول های بلوکه شده باید آزاد بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69906" target="_blank">📅 20:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69905">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی We pari همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/69905" target="_blank">📅 20:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69904">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/si5K2npmDngoSkXO-2TisKJqVVaT4L5pFjMwbVHLj8V3xqVYCOMMHfTvgih9AA61O0LaVHJIj2JImoBE4XKuRzqeU7T0RozD_sIPCiim9duSG9ICESNIIx7tCDQlibe3ze6dtS2RzneRNId6ZMxxGAUGNJeitxv5HyWvr8wDLdn3lqFSwqPi0_LVDwK6KEY8CZ63OeogCKwbipCHFg6_I4swszxGX-IZdKAqqu18ovOB9VvzfU3zGS37m7emwAsU-Z1_o7e4TlxI9xsCbV-wgV_7a3uSl186JE1a7ZQmK8MF_XNkVaHzh4l9nVdKwlokVfWww0tKm-5hTzwhK3Qz3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/69904" target="_blank">📅 20:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69903">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e58dcb779.mp4?token=lBV4ToCv3YuwX4SYEqBs8ci3i00nrf4N28m1W5VKRrl9W8kvtCwG7-P5FjmEwmWybXgeWe0zX3xAxZ69RR3bvgja2kG7aoo10R3tx_LXft_4DYA0zT8vtWrQbvaVO9qC9ZJ3RpquQJ-AdpBNgwRVysUrQnEwKUtayVKPlccFcftMCa4-o2Xy3UX97C6ZBwYrMJkzwmvbKLmEZ0LbtNwNqwDkCxfgutpLeivFFFQzpvVNY1ewY3oFiQSGAqNT4BdHSYXbqpjb09TEkzPdyFDLgKa-RuIu-cobGPPS6Tgu5tFmrtBSa5z5TIp4ODZjvodadUP_q1-vx4I_P09qhY_aFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e58dcb779.mp4?token=lBV4ToCv3YuwX4SYEqBs8ci3i00nrf4N28m1W5VKRrl9W8kvtCwG7-P5FjmEwmWybXgeWe0zX3xAxZ69RR3bvgja2kG7aoo10R3tx_LXft_4DYA0zT8vtWrQbvaVO9qC9ZJ3RpquQJ-AdpBNgwRVysUrQnEwKUtayVKPlccFcftMCa4-o2Xy3UX97C6ZBwYrMJkzwmvbKLmEZ0LbtNwNqwDkCxfgutpLeivFFFQzpvVNY1ewY3oFiQSGAqNT4BdHSYXbqpjb09TEkzPdyFDLgKa-RuIu-cobGPPS6Tgu5tFmrtBSa5z5TIp4ODZjvodadUP_q1-vx4I_P09qhY_aFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
روایت تلخ یه فرد نابینا:
اینکه من نابینام به عقیده پدرم کارمایی هست که دارم بخاطر کاراهای اون پس میدم.
پدرم وقتی جوون بود نابیناهارو مسخره میکرد و بهشون میخندید.
مثلا پدرم بهشون میگفت بیاید جلو بیاید جلو و وقتی میومدن میفتادن تو چاه و پدرم مثل خر بهشون میخندید.
پدرم بهم گفت من این کارارو وقتی جوون بودم انجام میدادم.بعدا وقتی تو دنیا اومدی دیدم نابینا شدی و این دلیلش کارمایی هست که من باید پس بدم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/69903" target="_blank">📅 19:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69902">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfb370d6c1.mp4?token=HzYiZY1sqVLIqKjNol8p-jllT7FckJ2lHwXEzmWLcHOLRSOeDaOuczem-opuAtPZ8TDrlBtRgXSW4JOMEDQIez7_a-rIvTaGOo4iuHGsyvRK0Zx9RVzga0dqV2djTaahIRiwSGaZ9YULIgiZCLQ1q_2zxilmTaXiVw0yQj4jD5PaeYX-olWAOXxuLA8D7muVNA6uDBXO1XLcUP3vcfS5TmayBD1ZTXxu0E-nYjxJffXI0j8w8ccFKNnvbSYsNm3me7JFljLQW4fNDLe-PezoViahTyJefPi4FoDxQiwnNXESpqsRz16MM_UMb7ojFaoQAfw7qUAqlxONBJdsPVtA9RNkYmjqyb-EhsrsO5rGUz1hunQ2lSC5JoYMJa9BSvDqRfFmaYV7A-Zm8Mf4FkDJalojnpzJyvR-SHxgGy6HI0S_sKNJYf_Y7MVIynFE8aTe8r3pyZzvdq1v7XuvUpWqQKt9HlU3oKNHU3aKAXUJ3Eho2pfmsmFF6katENitvj2x0NJPMtcEskLzjBFbWNPQvrK5Xpg9_SbOalpUMzQFnhV7rQFkHe9wRkKBw5VPPunrO-JtfenjFTPKX1pwtaq595fnr0OdfQHzmuL6xEfAWW7P0Qrw22nCYm5T-WYD8RkENOv9d-IACPVBTiWslbnWzpwQBKqAKe7R11CNMieIopk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfb370d6c1.mp4?token=HzYiZY1sqVLIqKjNol8p-jllT7FckJ2lHwXEzmWLcHOLRSOeDaOuczem-opuAtPZ8TDrlBtRgXSW4JOMEDQIez7_a-rIvTaGOo4iuHGsyvRK0Zx9RVzga0dqV2djTaahIRiwSGaZ9YULIgiZCLQ1q_2zxilmTaXiVw0yQj4jD5PaeYX-olWAOXxuLA8D7muVNA6uDBXO1XLcUP3vcfS5TmayBD1ZTXxu0E-nYjxJffXI0j8w8ccFKNnvbSYsNm3me7JFljLQW4fNDLe-PezoViahTyJefPi4FoDxQiwnNXESpqsRz16MM_UMb7ojFaoQAfw7qUAqlxONBJdsPVtA9RNkYmjqyb-EhsrsO5rGUz1hunQ2lSC5JoYMJa9BSvDqRfFmaYV7A-Zm8Mf4FkDJalojnpzJyvR-SHxgGy6HI0S_sKNJYf_Y7MVIynFE8aTe8r3pyZzvdq1v7XuvUpWqQKt9HlU3oKNHU3aKAXUJ3Eho2pfmsmFF6katENitvj2x0NJPMtcEskLzjBFbWNPQvrK5Xpg9_SbOalpUMzQFnhV7rQFkHe9wRkKBw5VPPunrO-JtfenjFTPKX1pwtaq595fnr0OdfQHzmuL6xEfAWW7P0Qrw22nCYm5T-WYD8RkENOv9d-IACPVBTiWslbnWzpwQBKqAKe7R11CNMieIopk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو ای از لحظه حمله آمریکا به پل B1 کرج:
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69902" target="_blank">📅 19:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69901">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
🇺🇸
پرزیدنت ترامپ:از شیوه مذاکراتی ایران ناامیدیم.
ایرانی‌ها بازی فریبکارانه‌ای با ما در پیش گرفته‌اند: در اتاق‌های مذاکره موافقت می‌کنند، اما در رسانه‌ها [توافق‌ها را] رد می‌کنند.
ما از هیچ کمبودی در ذخایر موشکی رنج نمی‌بریم.
ما می‌توانیم با نیرویی عظیم به ایران ضربه بزنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69901" target="_blank">📅 18:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69900">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24b53c400c.mp4?token=C5K5dCv8f60ZvPFjTEKnqEsQvziVup1Qdfxq672zG64rnkyLzNVOdMTo9Kn52Ba4AMPckLFFywANo9s6XdbVX11EVgbka0hsG_AWk2mscR1XeK2Hsin2acR9hLdeFS3W5Tzwwu_QeK1FrzUrNosMa4ubBNVIPu_6vYYvH42Cbsoai-AJLDbIhIs5nJGfsht_7I7aSTjVBPUzd3nN_vr-HNEqx5J8uAsaVwUABOJQxiS1y_jpKYbdQsoGwTjbLDQ7eTkRgiG4BN5VVRO85B-bCwmQr5JkHX72PHE1Op_opIbPwopnZ56VrhzxRCKqiq4SgveppQWlD__cuznUL2zAUwvBACeV9sDa4RBP0WxaMpWi4HGvTyywcKcGlUxMfA_lXtGFXpLMUXIwNtexJ659jpFSXD4aN7qUW6nQSHFbOUSESiJH_79__fzBaIOw_vQEVdKwwiVJQjigQf2BdbB8ee4hic7GR6fq4Y2um7-f22v-avIjg1MdL0dxe8sm-N-iiqerwqlFvJNR84wjVThBp8zAxOdy58Qox5KTbFFpkdXnotnFKXuFj0jDtYf-POD1x-LBTSz5n2xt3pLkULV3qHELdEM6VN8tDfOfHW0_hmiMucT0gRLHSYOjdh8Y9hxwbb4701RAjVuhlxFwfLGC16ry2D8VntHD0xMRZTgtGLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24b53c400c.mp4?token=C5K5dCv8f60ZvPFjTEKnqEsQvziVup1Qdfxq672zG64rnkyLzNVOdMTo9Kn52Ba4AMPckLFFywANo9s6XdbVX11EVgbka0hsG_AWk2mscR1XeK2Hsin2acR9hLdeFS3W5Tzwwu_QeK1FrzUrNosMa4ubBNVIPu_6vYYvH42Cbsoai-AJLDbIhIs5nJGfsht_7I7aSTjVBPUzd3nN_vr-HNEqx5J8uAsaVwUABOJQxiS1y_jpKYbdQsoGwTjbLDQ7eTkRgiG4BN5VVRO85B-bCwmQr5JkHX72PHE1Op_opIbPwopnZ56VrhzxRCKqiq4SgveppQWlD__cuznUL2zAUwvBACeV9sDa4RBP0WxaMpWi4HGvTyywcKcGlUxMfA_lXtGFXpLMUXIwNtexJ659jpFSXD4aN7qUW6nQSHFbOUSESiJH_79__fzBaIOw_vQEVdKwwiVJQjigQf2BdbB8ee4hic7GR6fq4Y2um7-f22v-avIjg1MdL0dxe8sm-N-iiqerwqlFvJNR84wjVThBp8zAxOdy58Qox5KTbFFpkdXnotnFKXuFj0jDtYf-POD1x-LBTSz5n2xt3pLkULV3qHELdEM6VN8tDfOfHW0_hmiMucT0gRLHSYOjdh8Y9hxwbb4701RAjVuhlxFwfLGC16ry2D8VntHD0xMRZTgtGLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
رونمایی صداوسیما از «قوی‌ترین سیستم جاسوسی جهان»
تماس با پذیرش هتل عمان برای جاسوسی:
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69900" target="_blank">📅 18:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69899">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736f2f73f3.mp4?token=Fr18eSrt-8ecWO6VQxJWKwEIW8jy13hyTLRHl-e-BMq3rtIrWI47dfo77R77VWYAgTyCsIozQe1Ml260dBQlPPMGLQpAOR7DOX2lEINpk9jiY9-9fw4qdEqvGtPJkUyPFW_fkJylAq4fG4qYIgHQ5anWHrCga5kyBfrNLw3voQYk4KPannwJD1xpnepGBnYauyUS0p-T_oZ6WSi3MtdB76fgdTD_93Y5m7WV2wkWbwd7HEx19CHim9UbLPQEc3hIdUgmDfVtRlW-NohU3rEMjTpnQh01UcWqHVercnIZ3V4DmxjmqPWBXsQweU7ta3BDOPQIE7vjlGhSBa40CU6eyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736f2f73f3.mp4?token=Fr18eSrt-8ecWO6VQxJWKwEIW8jy13hyTLRHl-e-BMq3rtIrWI47dfo77R77VWYAgTyCsIozQe1Ml260dBQlPPMGLQpAOR7DOX2lEINpk9jiY9-9fw4qdEqvGtPJkUyPFW_fkJylAq4fG4qYIgHQ5anWHrCga5kyBfrNLw3voQYk4KPannwJD1xpnepGBnYauyUS0p-T_oZ6WSi3MtdB76fgdTD_93Y5m7WV2wkWbwd7HEx19CHim9UbLPQEc3hIdUgmDfVtRlW-NohU3rEMjTpnQh01UcWqHVercnIZ3V4DmxjmqPWBXsQweU7ta3BDOPQIE7vjlGhSBa40CU6eyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
مشاور قالیباف، مجید شاکری:
هیچ کس نمی‌تواند با ترامپ به توافقی برسد.
این تیم فعلی با هیچ کس به توافقی نرسیده است.
او هم با ما به توافقی نخواهد رسید.
همه فقط در تلاش هستند تا "تحمل کنند و صبر کنند" تا پایان این دوره.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69899" target="_blank">📅 18:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69898">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c85bc1feb.mp4?token=dzUEO3U2pBpEr0vlRc_K1HKdatV-CorGbQzeyoVbr8RilpPXaPXnGW_mbkv79tmQsoryjs5S80u5xgCh0NVcQ69rt8HQXLBF-0WEsAY8mMFWqEsuZwvDSDkrCytXbWtp4GcTUncathZb5ijOq7WME75S2unX-HCrgAsApYTXDVd-OTuMU5ZiypHTEouqTrXi8YJL4ZvstabeBCX3vSreS4YncEfazekfkYigLL9MWi4SZ_jlUwC-ZETcO-Dun5Bnesau45aLPr_lLym8Q0vEgMtTIZyQOBEUmPLGYiBh7UTiwOuvWIATcrUybNfSkKjOPd1bx5NaFiexp123quREvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c85bc1feb.mp4?token=dzUEO3U2pBpEr0vlRc_K1HKdatV-CorGbQzeyoVbr8RilpPXaPXnGW_mbkv79tmQsoryjs5S80u5xgCh0NVcQ69rt8HQXLBF-0WEsAY8mMFWqEsuZwvDSDkrCytXbWtp4GcTUncathZb5ijOq7WME75S2unX-HCrgAsApYTXDVd-OTuMU5ZiypHTEouqTrXi8YJL4ZvstabeBCX3vSreS4YncEfazekfkYigLL9MWi4SZ_jlUwC-ZETcO-Dun5Bnesau45aLPr_lLym8Q0vEgMtTIZyQOBEUmPLGYiBh7UTiwOuvWIATcrUybNfSkKjOPd1bx5NaFiexp123quREvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
نیروهای روسی تلاش کردند تا یک گروه بزرگ از خودروهای سبک را در یک نقطه تجمع، تقریباً 20 کیلومتر پشت خط مقدم در منطقه دونتسک، مستقر کنند.
همانطور که در اینجا مشاهده می‌شود، پهپادهای تهاجمی کوچک اوکراینی این گروه را مورد حمله قرار دادند و ضربات متعددی به آن وارد کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69898" target="_blank">📅 18:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69895">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c9ff38ed.mp4?token=lPu7GUcIFMWRpxRITLehSIKfW6ksi7l0QCk9d3x7ywLp0HZyZtvDyZGLSV_UOzIBoLSOvfwmpoTx0Jw7iCzmYw64IPAow1F8zAwt3_c6yQc25uAMrH5BIJF6ES2d03DOrlvhrmO1fXO-mWXW7JEaOte71uCxV7AEJBlKVQT-j3Y3gBrD6IIyay8J43LhI2chfAW7AWRsJk6p2qFmVKzggv1jEwtNWa5wwYPH7STU5RKRUjhkbk2LTr4AJrAJQMaZqpI1hE2FgJ7O0FuTZNIIlZ8cjN1NdXrSvgDlnONWvpk9ovk4fs1UPhxtSTL7U0rYLC61OGO1lKSpTB23ofjPow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c9ff38ed.mp4?token=lPu7GUcIFMWRpxRITLehSIKfW6ksi7l0QCk9d3x7ywLp0HZyZtvDyZGLSV_UOzIBoLSOvfwmpoTx0Jw7iCzmYw64IPAow1F8zAwt3_c6yQc25uAMrH5BIJF6ES2d03DOrlvhrmO1fXO-mWXW7JEaOte71uCxV7AEJBlKVQT-j3Y3gBrD6IIyay8J43LhI2chfAW7AWRsJk6p2qFmVKzggv1jEwtNWa5wwYPH7STU5RKRUjhkbk2LTr4AJrAJQMaZqpI1hE2FgJ7O0FuTZNIIlZ8cjN1NdXrSvgDlnONWvpk9ovk4fs1UPhxtSTL7U0rYLC61OGO1lKSpTB23ofjPow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سامانه‌های پدافند هوایی «اونجر» (Avenger) و رادارهای «سنتینل» (Sentinel) ارتش ایالات متحده در نزدیکی محل بازی گلف ترامپ مستقر شدند تا پوشش حفاظتی کوتاه‌بردی در برابر پهپادها، هواپیماها و موشک‌های کروز فراهم کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69895" target="_blank">📅 17:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69894">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f4acff5e.mp4?token=gA7iENkfM9tF17WNCrCsyZeITH1stldmNNt1cZv_Uwn_2iB--LfLSqOteNaOdUAuNgawKAGZGcO16qQ42zTXeiB4thzMCOPMhIOcZIuhBM0hSGIJoEmFm30a0wnQUyTUFE_1uVl-uJg5gC-KZgJUVdM_d239PRgf_Smq_c-wrhpMuRWV_Na14LLzopySK6VYkiBD4oazCZMXcnGUTtY0gdoiFC6xv4N-Z6gdNwfEaoxcDfXGRFEHtiaVgL1Q_lzyF16NxqbE7TNC8kg93nyvhqq5qOrjKirQY1dn4k7mm8iQn7EL6v142dvEvuIQq1yOMz6n2mN8jiy0AE7v38XT9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f4acff5e.mp4?token=gA7iENkfM9tF17WNCrCsyZeITH1stldmNNt1cZv_Uwn_2iB--LfLSqOteNaOdUAuNgawKAGZGcO16qQ42zTXeiB4thzMCOPMhIOcZIuhBM0hSGIJoEmFm30a0wnQUyTUFE_1uVl-uJg5gC-KZgJUVdM_d239PRgf_Smq_c-wrhpMuRWV_Na14LLzopySK6VYkiBD4oazCZMXcnGUTtY0gdoiFC6xv4N-Z6gdNwfEaoxcDfXGRFEHtiaVgL1Q_lzyF16NxqbE7TNC8kg93nyvhqq5qOrjKirQY1dn4k7mm8iQn7EL6v142dvEvuIQq1yOMz6n2mN8jiy0AE7v38XT9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
دیشب توی تهران، یه نفر با یه دست رانندگی میکرد و با یه دست فیلم سوپر میدید
😐
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69894" target="_blank">📅 17:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69893">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDNB0EVzqzqMfUgalQ6xd2FlmnlFxdRgd2zmUovzqh8VwvDwOORoxM9PEsN5V_bpgnk1Hp1G5j8wNdGkYqf1NL9oxaejEqYFmZg4WJee2Yc-FB11V139fqA5uMg4yO-VtQ_pFWPPk3uwKFwYhHnjf6YBpgdFu7noyC8hy9MCvNZg8FMJuVAj0EXYb3M7WgBlEEdHASPG_8rCbrh4OHhW01yyGRFtWv7guKdQFKCFcSnOeiT4vbkImNFEV0bxChZVtpjKZzGceTq0e24orGjWhQ7QrAgZpqz8pcxZWYEUYlV7jTBB2S6trNN_6ah5CWvswCvI8P9aArg2uTVDKdUaBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
📰
وال‌استریت ژورنال:نیروهای آمریکایی بامداد سه‌شنبه به سوی شناوری با پرچم پاناما آتش گشودند؛ این اقدام پس از آن صورت گرفت که شناور مذکور ظاهراً تلاش کرد محاصره دریایی بنادر ایران توسط آمریکا را بشکند.
پس از آنکه خدمه این شناور هشدارهای مکرر نیروهای مسئولِ اعمالِ محاصره را نادیده گرفتند، یک بالگرد نظامی آمریکایی سکان کشتی را هدف قرار داد.
خدمه شناور در حال تلاش برای انتقال به یک کشتی غیرنظامی دیگر مشاهده شدند.
در نهایت گزارش شد که هر ۱۷ خدمه کشتی در سلامت هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69893" target="_blank">📅 16:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69892">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VooULoBmfIZORG4nwH6kqwAV7BMpjyAI0FcqeClRoYU3MiUmAjTUnP09jcPlzty2bS2-axH09yTOiAgdMY2VqzJszCKfblukEIaFu33wYQu9b27BwdNNp4isiwCUrpm6xzXhcrfQ65znwd44QjMPAk0lTChhZLqLYCTG3iGai5B5HQZI-20bD-_-YNWS6M1s0tuwjlKE9ANKA0bYwLDec7TPfnfPjbmfYZ49chCkFlHwjhoZ6WqjGXfXPq5Rx13KOYWhpCfUojtxZ7IQY9b3uJ1VgA2-bzwKjP9v4JGZSPM0WAZK-_jGllB3qc_eglqv8DR9lwZUa_zwzA3aKqzNpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📚
#فوری
؛ زمان برگزاری کنکور مشخص شد!
صبح پنجشنبه ۲۹ مرداد : کنکور تجربی
عصر پنجشنبه ۲۹ مرداد : کنکور زبان و هنر
صبح جمعه ۳۰ مرداد : کنکور ریاضی و انسانی
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69892" target="_blank">📅 16:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69891">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62f8b2cd3c.mp4?token=MBjmGItyz1jseoM0JhB4XAZRi-QZqc4p4Z0kAZCT8o2vdQ6cq8VV_STxKeltI9SdMuI9yAFhEHbud3YZmdADpbpvavH0MpY3LZmFGkCJDE68adw-8DWwzUNQaL0xS2NwYHHjHeAEWGT4KVQUgfC7E4NWyWxUE-bfpnyWJSmUKXjE5FOsHLWvZzRktCW5DMEsRXQDKX1fHb4yw1yB1iVn_HTNnUaJCe39hjHazo61_cCcbWdqMIdWq5HYG7SxlMlCphGpSkRTaB8yXHf3azp9alUxLt-Apr0Jd1iqhNdbZK4eoNuB33koF8keVkUGGU8Ktu0bL2AIuubF7_mmgQuZag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62f8b2cd3c.mp4?token=MBjmGItyz1jseoM0JhB4XAZRi-QZqc4p4Z0kAZCT8o2vdQ6cq8VV_STxKeltI9SdMuI9yAFhEHbud3YZmdADpbpvavH0MpY3LZmFGkCJDE68adw-8DWwzUNQaL0xS2NwYHHjHeAEWGT4KVQUgfC7E4NWyWxUE-bfpnyWJSmUKXjE5FOsHLWvZzRktCW5DMEsRXQDKX1fHb4yw1yB1iVn_HTNnUaJCe39hjHazo61_cCcbWdqMIdWq5HYG7SxlMlCphGpSkRTaB8yXHf3azp9alUxLt-Apr0Jd1iqhNdbZK4eoNuB33koF8keVkUGGU8Ktu0bL2AIuubF7_mmgQuZag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
یه آخوند توی برنامه زنده داشت به اجرا نشدن قانون حجاب اعتراض میکرد و میگفت ملت بالای ۴هزار تا پیام دادن برام؛
بعدش گفت بزارید یکیشو رندوم براتون بخونم:
چیزی که خوند
😔
:
«آقای پفیوز احمق بیشعور حرف دهنتو بفهم»
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69891" target="_blank">📅 16:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69888">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/698b90aa95.mp4?token=CgzzAacP698fkkGkk93iAwDWqS1sVXH0xVMdpFFxGjRqtSTstcl87b96nqIeQYzlFj7tTygEUPz4zc4dNUaiFqt_xDb0jkYEgA8gm8NFwjhwZCgLCV3FBZeT0G0MO6xtZ8g3p0Qzn3XC4DZox7QEas9UIzfJ37iIg3d8ysYWdAorJ39N0P6efdkW6pPIrpc7AIC5pdyW1Y46A4EyYkO9f-E7fLIpD6H_nhj8eY3tTlp5jNMRbMct60EoAZcQg7TTYcf8m81kDd3DdJVirxjsn_EcDMekoIEQMOcAnSUSBZ26EvwioSIdyI4c5MKiSX3dQnEHIA68fOvDK2lHgU6kXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/698b90aa95.mp4?token=CgzzAacP698fkkGkk93iAwDWqS1sVXH0xVMdpFFxGjRqtSTstcl87b96nqIeQYzlFj7tTygEUPz4zc4dNUaiFqt_xDb0jkYEgA8gm8NFwjhwZCgLCV3FBZeT0G0MO6xtZ8g3p0Qzn3XC4DZox7QEas9UIzfJ37iIg3d8ysYWdAorJ39N0P6efdkW6pPIrpc7AIC5pdyW1Y46A4EyYkO9f-E7fLIpD6H_nhj8eY3tTlp5jNMRbMct60EoAZcQg7TTYcf8m81kDd3DdJVirxjsn_EcDMekoIEQMOcAnSUSBZ26EvwioSIdyI4c5MKiSX3dQnEHIA68fOvDK2lHgU6kXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترلان پروانه توی آخرین مصاحبه‌ش گفته رابطه‌ش با شروین حاجی‌پور یه اعتماد اشتباه بوده و این رابطه تموم شده.
بعد از این مصاحبه هم شروین یه موزیک منتشر کرده که خیلی‌ها معتقدن حال‌وهوای بعد از جدایی رو داره.
جالب اینجاست که اوایل رابطه‌شون شروین توی یکی از موزیک‌هاش گفته بود قراره تا به دنیا اومدن نوه‌هاشون کنار هم بمونن!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69888" target="_blank">📅 15:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69887">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05e9aa8412.mp4?token=C8moe2I4UqswvFSUvAHcxLZ6lw2_LZx1X3K9-jdyFTnX6-lhsEZ3MW_800dA2f0wKiG9k6MCXnUMM5jwOV-Mk91TQACOLI7gAUNURHuWUOsfSQfxzaW_SQMxx6gGrmlJhmJfXP8CEUNN8EPCOzmgIuKU3c1aSgH7alLkI7M2ie8GxVX_lW9zibOGRVd2OTWmMF-HIYOtyBL2bMiyyrJFX6Wxawx5axF-4J5orRiDj5-ndS-BjlYF8cLajDq68dxqf7OaOTmmW9g-S5dFcO1rukWIOeGXCIe0rwnMqLUR792SqQFsfgjO4rRK2z0ZZlaT2Ex8kb0XFB4gHX-g6kMlyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05e9aa8412.mp4?token=C8moe2I4UqswvFSUvAHcxLZ6lw2_LZx1X3K9-jdyFTnX6-lhsEZ3MW_800dA2f0wKiG9k6MCXnUMM5jwOV-Mk91TQACOLI7gAUNURHuWUOsfSQfxzaW_SQMxx6gGrmlJhmJfXP8CEUNN8EPCOzmgIuKU3c1aSgH7alLkI7M2ie8GxVX_lW9zibOGRVd2OTWmMF-HIYOtyBL2bMiyyrJFX6Wxawx5axF-4J5orRiDj5-ndS-BjlYF8cLajDq68dxqf7OaOTmmW9g-S5dFcO1rukWIOeGXCIe0rwnMqLUR792SqQFsfgjO4rRK2z0ZZlaT2Ex8kb0XFB4gHX-g6kMlyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرود هواپیمای F-18 بر روی ناو هواپیمابر در هوای بارانی.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69887" target="_blank">📅 15:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69886">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e61a50ec6.mp4?token=WKTv2VPSY-jYD6_QhWfmkfequkd1p7Llq7mBve0dJG0yN7lidwzQXXt8waePAqDmxFxhhZ4pdTPo31pITTFQrcP5pgI0vbTZ1OFLLi6S1bTkNjWhpMnOoZpRjSxo3sGxD9pdhWyrzM7eqByGvCVq2_Vwd60DrHqH49gu01CBoUCrzxeSYcQAczYrh5-f05fTrsheQb-e-xPeRraJA3u5WJWYrT6P6QC7IGJNIOQZS7y1vxC0qF1m4nWeu-hsNoy2YR38tzPqXiYniVynDikLvgf197lZEzMsaQ-y_mAnoPLfr02WtPlxk9rTyhy-Qu0ctSJuy9F9GOfrWIR-jSHfug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e61a50ec6.mp4?token=WKTv2VPSY-jYD6_QhWfmkfequkd1p7Llq7mBve0dJG0yN7lidwzQXXt8waePAqDmxFxhhZ4pdTPo31pITTFQrcP5pgI0vbTZ1OFLLi6S1bTkNjWhpMnOoZpRjSxo3sGxD9pdhWyrzM7eqByGvCVq2_Vwd60DrHqH49gu01CBoUCrzxeSYcQAczYrh5-f05fTrsheQb-e-xPeRraJA3u5WJWYrT6P6QC7IGJNIOQZS7y1vxC0qF1m4nWeu-hsNoy2YR38tzPqXiYniVynDikLvgf197lZEzMsaQ-y_mAnoPLfr02WtPlxk9rTyhy-Qu0ctSJuy9F9GOfrWIR-jSHfug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان زیبای زندگی کسی که هممون باهاش خاطره داریم...
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69886" target="_blank">📅 14:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69885">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
🔴
ما سه راهبرد داریم:
ادامه دادن به همین روال فعلی؛ یعنی صرفاً پیش رفتن و نظاره کردنِ وضعیت وخیم آن‌ها، چرا که تورمشان به ۳۰۰ درصد رسیده است. ارزش پول ملی‌شان تقریباً از بین رفته است. آن‌ها حقوق سربازانشان را نمی‌پردازند و سربازانشان در حال ترک خدمت هستند. بنابراین باید همین روند را ادامه داد، چون این وضعیت پایدار نیست.
وارد کردن ضربات بسیار سنگین به آن‌ها، یا... در واقع راهبرد سوم، شکست دادن آن‌ها از طریق اقتصادی است. اما ما به هر حال داریم همین کار را می‌کنیم؛ این [راهبرد] تا حدی بخشی از همان راهبرد اول محسوب می‌شود.
از نظر اقتصادی، وضعیت آن‌ها آشفته و نابسامان است. آن‌ها نمی‌توانند وام بگیرند. ما کنترل منابع مالی‌شان را در دست داریم؛ همان دارایی‌هایی که در اختیار داشتند و رقم بسیار بزرگی هم بود. آن‌ها سرمایه زیادی داشتند و ما اکنون کنترل کامل آن را در اختیار داریم.
من بانکدار آن‌ها هستم. من بانکدار آن‌ها هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69885" target="_blank">📅 13:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69884">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71d56160d7.mp4?token=h_0Py_gcslcw5U9kGT_jUm43hMSIBWEGMDSNyXe6hyQ5uiqAx_A6WhPYShOY7eAbTbSkvbTCpd1EUlRBanQWiuG7hgDByv7wVo3OKAIZb_t1_IkDA_OxyBf48M0__HPasnyFQrS1wr3-5e8wBI_jmDHqfGW_X-N067ES8HmARbqQP1gOstXAgph8-pWXMlb8OGfGHeBEzPAlmKoaG9ty2smC1z2yqE1kFxPVIL1-1EEcBoofpXHcEHh0FnmXDsbfC3dh_n5hmW6JfHYRJS72heuW8qgaO63mA36OeFUU4_YURM_8Q_vwaQMC9fCtQvVKrgDKLvt1xjqssIDDWjUe4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71d56160d7.mp4?token=h_0Py_gcslcw5U9kGT_jUm43hMSIBWEGMDSNyXe6hyQ5uiqAx_A6WhPYShOY7eAbTbSkvbTCpd1EUlRBanQWiuG7hgDByv7wVo3OKAIZb_t1_IkDA_OxyBf48M0__HPasnyFQrS1wr3-5e8wBI_jmDHqfGW_X-N067ES8HmARbqQP1gOstXAgph8-pWXMlb8OGfGHeBEzPAlmKoaG9ty2smC1z2yqE1kFxPVIL1-1EEcBoofpXHcEHh0FnmXDsbfC3dh_n5hmW6JfHYRJS72heuW8qgaO63mA36OeFUU4_YURM_8Q_vwaQMC9fCtQvVKrgDKLvt1xjqssIDDWjUe4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سینا حجازی، خواننده:
اگه زنِ هات میخواین، زن گوشت‌خوار بگیرین، زنایی که گیاه خوارن، سردن!
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69884" target="_blank">📅 13:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69883">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZaD9kI3JTdrX8CvWubqzdMTefOZGppmUWtwd50lSe4SRVPdirxXqcy39nvONAOBW135GQjLIgfFXSDCGlsx0uqyZxYeidxxLhj2VtO7L_NBxiuqGXppXTHPvR1OuANGkNISFmYyWUlhWOsAfCrl0bJSFNqySHJfasSBUXunyn2xZ3i2P-D5afdyzYZe1hgHWzSKhSoaKethyceqKMBxEZqr0l1Xq6tzkobu7cUCUaVHpj2ew_2fvtmV86TN4Nf1A-DyNuuYAGq49zLQyvbWXuahTrN9bVt1eQ4A5z3yPBiWl-bE097_17-RSA8DxMssuVhRM1EzqOeYE9JtJruJzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا:
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از وقوع حادثه‌ای میان یک نفتکش و نیروهای نظامی در دریای عمان خبر می‌دهد.
هویت نفتکش و نیروهای نظامی درگیر در این حادثه هنوز اعلام نشده است.
در حال حاضر جزئیات بیشتری در دسترس نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69883" target="_blank">📅 12:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69882">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b61a921e39.mp4?token=X0YIzbGdn9C3vZkc6xbpLYG8FwT_bR5yXWDMSksnpVtJkXA7YuW_K2dzg9FbCY3X3Nk4T3QdHgvxaaTHObArhnxmSZ1HjlmapVka0h5xcDkQqthGncf5GYYLS4H93PDR1dpEmMwBOJo40gD91dfwg526u6fAIXNiFj9qvtthqXn52uu4kC1jvGvlTU7KfquPGKaNgYWD51WzgrzpeLi3JlJCdrmSFeHwsyGZRiSnVe2R45suLQkgwCrHWi0H5zBKln0dda0rE9Mxduofhinlzn_ysXQyML8uo3gZoVq-ruEfYlzvIViVem2w56Ms6YdvwRT3xekbs2Mz9KKNpq8j5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b61a921e39.mp4?token=X0YIzbGdn9C3vZkc6xbpLYG8FwT_bR5yXWDMSksnpVtJkXA7YuW_K2dzg9FbCY3X3Nk4T3QdHgvxaaTHObArhnxmSZ1HjlmapVka0h5xcDkQqthGncf5GYYLS4H93PDR1dpEmMwBOJo40gD91dfwg526u6fAIXNiFj9qvtthqXn52uu4kC1jvGvlTU7KfquPGKaNgYWD51WzgrzpeLi3JlJCdrmSFeHwsyGZRiSnVe2R45suLQkgwCrHWi0H5zBKln0dda0rE9Mxduofhinlzn_ysXQyML8uo3gZoVq-ruEfYlzvIViVem2w56Ms6YdvwRT3xekbs2Mz9KKNpq8j5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تازگیا به نوع مدیتیشن تو تهران مُد شده که کلمات رو به صورت نفس‌نفس زدن میگن تا انرژی بد ازشون تخلیه بشه
😳
هزینه هر دوره بالای ۴۰ میلیون!!!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69882" target="_blank">📅 12:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69881">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46ae8f31fa.mp4?token=jmlkHgJzuQi-Shmg6mM1HqGSLk_MB8aF-UXPud1lg3rTz2vx_cHlzOpaQJci2taOtQx5wotjHpnSslqJNFkfJfyL2GXlCw0E-Vw6RW5X25iJHlFuOovHaAJ98yG2qa1ZINSwpcRTnk1GHaAwOy6vkGfXudvv0VYnxv04_LqWW8ve6lnWf4WKC37JM8WMJe6Xae2CU8QeKei8vyaAgekVLwlxNysebHRD1wK2ihV7tDC5_THsTWW_73qD0XvpZyPIe1lGcFLWkDqJ59G6IRIt1orELN4ERg3C7lowEJzsod_mWGH0cWNvQyoJkPHdvtyIoD8r1pzgg5h4sKSWy6cSXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46ae8f31fa.mp4?token=jmlkHgJzuQi-Shmg6mM1HqGSLk_MB8aF-UXPud1lg3rTz2vx_cHlzOpaQJci2taOtQx5wotjHpnSslqJNFkfJfyL2GXlCw0E-Vw6RW5X25iJHlFuOovHaAJ98yG2qa1ZINSwpcRTnk1GHaAwOy6vkGfXudvv0VYnxv04_LqWW8ve6lnWf4WKC37JM8WMJe6Xae2CU8QeKei8vyaAgekVLwlxNysebHRD1wK2ihV7tDC5_THsTWW_73qD0XvpZyPIe1lGcFLWkDqJ59G6IRIt1orELN4ERg3C7lowEJzsod_mWGH0cWNvQyoJkPHdvtyIoD8r1pzgg5h4sKSWy6cSXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
استایل ثروتمندترین ورزشکار دنیا
🆚
استایل پسرایرانی با ماهی ۱۵تومن حقوق
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69881" target="_blank">📅 12:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69880">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf27d27808.mp4?token=ajBdTa51AEyToO5VwwXSxoc1aTXdU_fdWqtvxR7BDzqi_Bz2nqfpQFttSmTNyQDEx6jGAx1zxJTCjKa7NGAv7lVxuTYtsG0r7sSxLjKEndNYvoRU2fmX3kg07RlRjCxPYx2pIr2Sy_CdqCK3vXwPx_xEIFpW0GnD9mwgOHshwt7B_D4_ZpGlvEgyFWiG5MfuSfBoC0jk7TnSArMIE4H1qLKObR5UUiuo4tUDo8MQPaZqOno6blqJNk63BbCaKCZrd48TpYmQ35L98M79JVLEJ6W7eRhzT7xJ6WK7RPkFvN-TvYn3NSknBi5kxn189ww9tQ3e_VSOAFY8HneVwl4yPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf27d27808.mp4?token=ajBdTa51AEyToO5VwwXSxoc1aTXdU_fdWqtvxR7BDzqi_Bz2nqfpQFttSmTNyQDEx6jGAx1zxJTCjKa7NGAv7lVxuTYtsG0r7sSxLjKEndNYvoRU2fmX3kg07RlRjCxPYx2pIr2Sy_CdqCK3vXwPx_xEIFpW0GnD9mwgOHshwt7B_D4_ZpGlvEgyFWiG5MfuSfBoC0jk7TnSArMIE4H1qLKObR5UUiuo4tUDo8MQPaZqOno6blqJNk63BbCaKCZrd48TpYmQ35L98M79JVLEJ6W7eRhzT7xJ6WK7RPkFvN-TvYn3NSknBi5kxn189ww9tQ3e_VSOAFY8HneVwl4yPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:درباره گرانی ها هم توضیح بدید؟!
🇮🇷
مهاجرانی سخنگوی دولت:
قبلا توضیح دادیم، گرانی های موجود دلیلش فشار اقتصادیه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69880" target="_blank">📅 11:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69879">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1ee7cbbf.mp4?token=kYRPYqFZB_ruFbkskSLWrWr-JRgSQDijo7CWNANvNvMBMk00sWzDZA5eCVvVhf-yidNEDCOVWugcZx2QSXznRbAnlCAiPFW3Y2tZrDXUPrPkkxvFrIOOCnnRd8IkGyag4emISB4xntSqh2y66zc0TyQUPDq1Zb3vX6EzVTAUf4gLLCQvnnCzuBWopH4itb4TN21ravuWU69ZtBliJnxFAhnmcGe2sxmljSQ0pqtpSP1LLR7QeFT_8-rrVpbgaOh_9GWO_KT6bhuSierfUsxH-7aC8ZJdIbpNSdXw1x9yNxjH1SA0yvqO9tAUqT6zHqypDNT19XgkM36R4RU7hRHIRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1ee7cbbf.mp4?token=kYRPYqFZB_ruFbkskSLWrWr-JRgSQDijo7CWNANvNvMBMk00sWzDZA5eCVvVhf-yidNEDCOVWugcZx2QSXznRbAnlCAiPFW3Y2tZrDXUPrPkkxvFrIOOCnnRd8IkGyag4emISB4xntSqh2y66zc0TyQUPDq1Zb3vX6EzVTAUf4gLLCQvnnCzuBWopH4itb4TN21ravuWU69ZtBliJnxFAhnmcGe2sxmljSQ0pqtpSP1LLR7QeFT_8-rrVpbgaOh_9GWO_KT6bhuSierfUsxH-7aC8ZJdIbpNSdXw1x9yNxjH1SA0yvqO9tAUqT6zHqypDNT19XgkM36R4RU7hRHIRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دکتر مشاور خانواده :
یه مرده اومد بهم گفت زنم عاشق دوستم شده و منم بهش گفتم که تو حق داری باهاش رابطه داشته باشی!
گفت منم با خانمِ اون آقا چندبار رابطه داشتم ولی چون اون خانم خودش پارتنر داشت، زیاد خوشم نیومد و کات کردم...
ولی خب موقع سکسِ اون آقا با زنم، من اونجا هستم و تماشا میکنم!
الانم از اینکه خانمم از اون آقا باردار شده خیلی ناراحتم چون آمادگی داشتن بچه رو ندارم.
ولی خب بازم میخوام شناسنامه اون بچه رو به اسم خودم بگیرم...
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69879" target="_blank">📅 11:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69878">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/69878" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/69878" target="_blank">📅 11:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69877">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_nGH25DPmoy0DQpuQLmlCYtAkWpE46cu91F4cQqT-DYaSsfhUPHJlSnHhnBmyL4QduzdZbP05E2hunvocMe132SZb7wck6R9fKfZaRf1uyypf-thXUZwuMae5SgoIXVvFr_k3Uul6Ua8ra5HbfiYreoRrW6vek11OJ9sLJM7jtQtpf-KzdhywemPo3xINQTpxoMM1CFYsG_eFLYM54hxOaO9UNCbyw-G7IjQRHJa6-T2wElLodi4GkPvPL0qtV2ONOlkAjIyS4OpXtvr-kSyUCxZSBRR1zYJz7qVqlEjqaR8s730TnZYMJ3qjcv-0lYvL0DPXJJBoyFyJF46pc9Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
r20
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/69877" target="_blank">📅 11:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69876">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2435556002.mp4?token=OZ5LuNvtb8E95fZH1FsJfTcGNjti3SRZSGRmoWLgSQihlChHUf-ojwemrXjS_qfV2HvIwkclFzyxGyG_YA4aIGjexw4b8C7RlPVfXXqJZrGIXrg9Plwn0AXb3qyv-Xe4vEIIt78EOaTxUFp-XN9j-qDQlxrq2rP9P-YNJrWgHelk5ep89iPrpSmh4GmLJBtH-KtbaNODXQp6QoTwhGfuflHMDAL4WqQ8RqjtxyXkYTOx7kRMaXkU_oGncWxnbhBLGjqEnI4vmaPjyxO5OCEr_8k_xVNcpxQSTZ8zVGl56fJ83WeBFefoyytnT_v5ypS45MBGi_Hn3Lpq8W1b8u2OBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2435556002.mp4?token=OZ5LuNvtb8E95fZH1FsJfTcGNjti3SRZSGRmoWLgSQihlChHUf-ojwemrXjS_qfV2HvIwkclFzyxGyG_YA4aIGjexw4b8C7RlPVfXXqJZrGIXrg9Plwn0AXb3qyv-Xe4vEIIt78EOaTxUFp-XN9j-qDQlxrq2rP9P-YNJrWgHelk5ep89iPrpSmh4GmLJBtH-KtbaNODXQp6QoTwhGfuflHMDAL4WqQ8RqjtxyXkYTOx7kRMaXkU_oGncWxnbhBLGjqEnI4vmaPjyxO5OCEr_8k_xVNcpxQSTZ8zVGl56fJ83WeBFefoyytnT_v5ypS45MBGi_Hn3Lpq8W1b8u2OBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری و بلاگر طرفدار حکومت:
یعنی چندنفر باهم مشکل داشتن و همدیگه رو به طور کامل میشناختن
این پروژه‌ها از این به بعد قراره زیاد باشه واسه اینکه میدون‌ها و نیروی انتظامی رو ضعیف کنن
قاتل‌ها تو کمتر از 24 ساعت دستگیر شدن و کشور الان تو بالاترین سطح امنیته مخصوصا تو تهران.
متأسفانه قراره خون ریزی های از قبل برنامه ریزی شده شاهد باشیم
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/69876" target="_blank">📅 11:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69875">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/022aef02ab.mp4?token=ITiTpvTpUwhDqTV-o-3OBQpTf0Su7OEfbtXVtwqw7DiUBpWBtQvaJJwu7nYsaePSdhsCDMHi6o3aSmy39EfQabPV6WSQ0ntlCvoinAQUd1xQMPXTdfVz-JG1yrz_gZuEqgcyZc3XndsNVm-Ec12t253ktCAy0aOOXgXTjC8ZrRz5dP88Oc-4GeZpIUOzdYJ2oayJYUj9pRCGoNsHurPYJXt3NLMHQ0epiaLcdrP2mvk5NvA4A6627b9iV9jBUVyzBAxACYHoacicmxkmfs8R50FRD1wzHeoSiLqmNfE6p0SOiSZnoFBHMwp1T1H33cf0XFabLnN0DwdMGM3rG-oxvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/022aef02ab.mp4?token=ITiTpvTpUwhDqTV-o-3OBQpTf0Su7OEfbtXVtwqw7DiUBpWBtQvaJJwu7nYsaePSdhsCDMHi6o3aSmy39EfQabPV6WSQ0ntlCvoinAQUd1xQMPXTdfVz-JG1yrz_gZuEqgcyZc3XndsNVm-Ec12t253ktCAy0aOOXgXTjC8ZrRz5dP88Oc-4GeZpIUOzdYJ2oayJYUj9pRCGoNsHurPYJXt3NLMHQ0epiaLcdrP2mvk5NvA4A6627b9iV9jBUVyzBAxACYHoacicmxkmfs8R50FRD1wzHeoSiLqmNfE6p0SOiSZnoFBHMwp1T1H33cf0XFabLnN0DwdMGM3rG-oxvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇺🇸
واشنگتن پست:پس از تهدید ترور از سوی ایران، ترامپ مخفیانه هنگام ترک اجلاس ناتو در آنکارا با هواپیمای دیگری جایگزین شد.
او با هواپیمای جدید ۷۴۷-۸ اهدایی قطر (اولین سفر بین‌المللی ریاست جمهوری‌اش) به ترکیه رسیده بود.
برای عزیمت، او علناً و جلوی دوربین سوار هواپیمای قدیمی ایر فورس وان شد و گفت که می‌خواهد «به یاد گذشته» با آن پرواز کند.
اما دقایقی پس از سوار شدن، او و چند دستیارش از طریق یک کامیون پذیرایی فرودگاهی که کانتینر آن به صورت هیدرولیکی به دری در کنار و دور از دسترس رسانه‌ها بالا رفته بود، به یک هواپیمای کوچک‌تر C-32A (757 اصلاح‌شده) منتقل شدند که از دید پنهان بود.
سپس هواپیمای قدیمی ۷۴۷ به عنوان طعمه پرواز کرد و همچنان از تابلوی تماس ایر فورس وان استفاده می‌کرد.
روزنامه‌نگاران و برخی از کارکنان کاخ سفید که در هواپیما بودند، اصلاً نمی‌دانستند که ترامپ با آنها نیست.
به آنها گفته شده بود که پرده‌های پنجره را بسته نگه دارند، که امری غیرمعمول است.
هر دو هواپیما با فاصله چند دقیقه در فرودگاه سلطنتی میلدنهال در بریتانیا فرود آمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69875" target="_blank">📅 10:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69874">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ما ۳ استراتژی برای برخورد با ایران داریم
رصد نقاط ضعف این کشور.
وارد کردن ضربات سنگین.
اعمال فشار اقتصادی.
🔴
اکنون ایران در وضعیت آشوب اقتصادی قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69874" target="_blank">📅 10:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69870">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b616d440e1.mp4?token=aGDQeFSQoiqOZMLZYVagqzsMVbAElxCa4iRQOOCpZeEZM_SQiiptLx6H38czrhSLjzXZBAVV3fY9dZy_Mfs1TuVUlZqZsYEAjgGbRJbZ29C5dUwI2_Kpf2PpyaKcP2-7o0xcDudCXSUKslls1mW0sWimIHFcnoul6WonmkZlH3Kk5JrqyJqHkrwldpxn6WX5-rsOZVn41cKByMHfW1AjhRZXmftPbpUN39RP3HVEc5BXheo-nI4XtvasxeYE9zefVmEHb9crcT9Uz8gMP5Tpu2EJSy884g5gUfZKXm6yy1CDaps-QW5RMALxrk9qjOheLTfXNT2yAUg-SBwdGgc5SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b616d440e1.mp4?token=aGDQeFSQoiqOZMLZYVagqzsMVbAElxCa4iRQOOCpZeEZM_SQiiptLx6H38czrhSLjzXZBAVV3fY9dZy_Mfs1TuVUlZqZsYEAjgGbRJbZ29C5dUwI2_Kpf2PpyaKcP2-7o0xcDudCXSUKslls1mW0sWimIHFcnoul6WonmkZlH3Kk5JrqyJqHkrwldpxn6WX5-rsOZVn41cKByMHfW1AjhRZXmftPbpUN39RP3HVEc5BXheo-nI4XtvasxeYE9zefVmEHb9crcT9Uz8gMP5Tpu2EJSy884g5gUfZKXm6yy1CDaps-QW5RMALxrk9qjOheLTfXNT2yAUg-SBwdGgc5SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
دیروز تو کلمبیا، یه زلزله 7.4 ریشتری اومد و اینجوری به ساختمون ها خسارت وارد کرد؛
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69870" target="_blank">📅 09:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69869">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22c07c5ff9.mp4?token=c5hAdVRY1AjoW8XhFaY-JlKPSjHo80_-jY3JKI_JfLGue_rziMXlgooCGjIvVJLruXct-0p46sRSRNTy0MTRWrvN-oVz5cH19K9y-JL7A8rZ1AwVj0MHFSJgdV8leVttPPcVJVJr6GT-twFaIsGyT9hNWaU7_2bxVyEU5ebJf5Nbc9x-xOiJmQ0y7p23lVCwccO6xr1IIrkFkMfkjLrK-4RKKD9C6ClLxH72-rQSRvOUvj61-rOJVF6cyYNNFpmnhZ9TQkq-1rrGeePkP1eMYl1ew1gqW3_Tn7DYV3Qx-kzqYBRAyB-w2_vPyLqWaEU3_XLrbiINL1-ljlLdXwv4fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22c07c5ff9.mp4?token=c5hAdVRY1AjoW8XhFaY-JlKPSjHo80_-jY3JKI_JfLGue_rziMXlgooCGjIvVJLruXct-0p46sRSRNTy0MTRWrvN-oVz5cH19K9y-JL7A8rZ1AwVj0MHFSJgdV8leVttPPcVJVJr6GT-twFaIsGyT9hNWaU7_2bxVyEU5ebJf5Nbc9x-xOiJmQ0y7p23lVCwccO6xr1IIrkFkMfkjLrK-4RKKD9C6ClLxH72-rQSRvOUvj61-rOJVF6cyYNNFpmnhZ9TQkq-1rrGeePkP1eMYl1ew1gqW3_Tn7DYV3Qx-kzqYBRAyB-w2_vPyLqWaEU3_XLrbiINL1-ljlLdXwv4fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
خرازی:
مجتبی خامنه‌ای اگه تو این سه سال از دفتر رهبری طرد نمی‌شد، می‌کشتنش
خود علی خامنه‌ای هم همین‌طوری بود، تو دفتر خمینی هیچ جایی نداشت
از احمد خمینی بگیر تا کروبی و... همه میخواستن مرگ علی خامنه‌ای رو ببینن.
ابراهیم رئیسی هم قصد داشت رهبر بشه که شهیدش کردن
اصلا بحث همینه مجتبی اگه زیاد پیش پدرش دیده می‌شد خودی ها میکشتنش
تو بحث رئیسی هم یکی از اعضای دفتر اومد خونمون گفتش ک دارودسته اینا میخاد رئیسی رهبر بشه ولی شهادت جلوشو میگیره
خیلی حرفا هست ولی خب مطمئن نیستم بشه گفت یا نه
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69869" target="_blank">📅 09:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69868">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
🇺🇸
✈️
پشتیبانی سنگین آپاچی‌ها از نیروهای ویژه آمریکا در افغانستان
⏺
تصاویر نادر و حدود ۱۵ دقیقه‌ای از عملیات دو فروند AH-64 Apache در افغانستان؛
آپاچی‌ها گروهی بیش از ۲۰ نفره از نیروهای طالبان را که در حال آماده‌شدن برای کمین یک گشت نیروهای ویژه آمریکا بودند، شناسایی و درگیر می‌کنند.
در این درگیری، آپاچی‌ها ابتدا با توپ ۳۰ میلی‌متری M230 مواضع طالبان را زیر آتش می‌گیرند و سپس برای درگیری با اهداف مشخص‌تر از موشک‌های AGM-114 Hellfire استفاده می‌کنند.
تصاویر این ویدئو با سامانه تصویربرداری حرارتی FLIR نصب‌شده روی آپاچی ثبت شده؛ به همین دلیل صحنه‌ها به‌صورت تصویر حرارتی دیده می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69868" target="_blank">📅 09:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69867">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/69867" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
a19
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/69867" target="_blank">📅 01:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69866">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UC94Z7b5eE6ZTrog3axeHXD64V09YedgwAtiqLj8WVNewYJJVDL0cRlTkrCuUE1uU-rw30eL7F8j5jnGhWrVysCjyZ-dnmvBrWVz1_45Xxf1YlzBqEWaQ0ppFmmlXJay5xzPMAyFlvOYIdeG0Yp2hgKy9FsAQrnHFMPAQbVE_67UU_dEokkok-sRz2pNAbDumESVRJ22P3PlCB21phNup1zlmsgEIquK1DhwrT1tpKCMpWh2s5b5dqC1_UKkIBgRI33CXQkPY3zfv6qJEqFskNuy_3qOqdgP4T8L2GWus9dFzeDxJoe9ADJ7ZbONXSVYn_saPWvNx2JDei2DjZqTPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
a19
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69866" target="_blank">📅 01:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69865">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/6ad4ea0af6.mp4?token=oU00ZYkiQyRM-sUilZt4TTgFs1eswq9uFwPLas4zlfa_CFx4kbbIDApbtgT5p9Ax9PYNvouOCVlE17CHqevwQv7RN9fYobBwpWUKPvsmrNqR77Y4KKBpaGViA0ah7JDO1MCTaBZt018xdpHWaQhz8JwvMJHCvIhgTYQl8sT3jCwpic3B75p1fb4wtjobaIrrI-7yu5ddMxRT9cpYmutcF-Y2JdJXH31LG4mAYqL6hTt74i246LImL7Uc8aI7FfAwtM8M_GHRVjWX7xG3WzPgs7h0kWHMdas2limW22a1_sIddPtAob_nOcvWHu6VrW5-6yR1eMQ9tP4x_TMzQ8HrdUlCBMyuUbPLXWCMwxIwidBx2fLclXOKBWKhplRydKpYXaWlH3Y-pT3EaeoA0D50YC3o3ZxT0-XYkjWmALqMbKDSBi535BuolzZ2UeCn2chyek3iNbEvypiwaLaP_iTjlK-K6DyR0aQWwhG1xvCRVwsB5s1wRgMyLxo2utkWA7FL13cGYzSr1p4u1X6hzBPs0qQ5yERf5fWuA9RvMV8SNiS4MC4UoVtePsDSSZOfeVTqtZcnOk3r6IUB0gQ2x3hYzjDJwSWtohmQUBkTuresEDySbP8i9HlxAHhusJEpr2tqcZACjAIm9pgeotMfAhqXsw8bcbM8NIWQ_w8OPcSK_wE" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/6ad4ea0af6.mp4?token=oU00ZYkiQyRM-sUilZt4TTgFs1eswq9uFwPLas4zlfa_CFx4kbbIDApbtgT5p9Ax9PYNvouOCVlE17CHqevwQv7RN9fYobBwpWUKPvsmrNqR77Y4KKBpaGViA0ah7JDO1MCTaBZt018xdpHWaQhz8JwvMJHCvIhgTYQl8sT3jCwpic3B75p1fb4wtjobaIrrI-7yu5ddMxRT9cpYmutcF-Y2JdJXH31LG4mAYqL6hTt74i246LImL7Uc8aI7FfAwtM8M_GHRVjWX7xG3WzPgs7h0kWHMdas2limW22a1_sIddPtAob_nOcvWHu6VrW5-6yR1eMQ9tP4x_TMzQ8HrdUlCBMyuUbPLXWCMwxIwidBx2fLclXOKBWKhplRydKpYXaWlH3Y-pT3EaeoA0D50YC3o3ZxT0-XYkjWmALqMbKDSBi535BuolzZ2UeCn2chyek3iNbEvypiwaLaP_iTjlK-K6DyR0aQWwhG1xvCRVwsB5s1wRgMyLxo2utkWA7FL13cGYzSr1p4u1X6hzBPs0qQ5yERf5fWuA9RvMV8SNiS4MC4UoVtePsDSSZOfeVTqtZcnOk3r6IUB0gQ2x3hYzjDJwSWtohmQUBkTuresEDySbP8i9HlxAHhusJEpr2tqcZACjAIm9pgeotMfAhqXsw8bcbM8NIWQ_w8OPcSK_wE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇦
لحظه سقوط یک جنگنده میگ-۲۹ اوکراینی.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69865" target="_blank">📅 01:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69863">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcca7b928e.mp4?token=E274wmZVr0jC8h4XL0Dznu8z3p-WRLSJiAJHLEUhMrJuefAPAK-91tBV4QNtmcXI71bR2oBt97jiyo1MwUplfNPKE7t86yP2lUPkPgvOkDBp1REUxZx1H0YgxyQTz5dxrXxRkQtVdDKClurxXqjwO5ErWWrrdodus9F-Cbxbgy-qBNZYG4nOvWsPJppNZHlgNZInoC1nitOtOs3A_MBM2-U31GIzwG5aPZlzlP-dbqZKZxQXiriK5MnRZ7Up6jVgdHYt0AgC-X179AzLP35jVjMuSca5z7SixZY5VNCmHWia2vU3NdSBOeISqRxgR1r7mlvOUlksn6v9g43vbsDMUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcca7b928e.mp4?token=E274wmZVr0jC8h4XL0Dznu8z3p-WRLSJiAJHLEUhMrJuefAPAK-91tBV4QNtmcXI71bR2oBt97jiyo1MwUplfNPKE7t86yP2lUPkPgvOkDBp1REUxZx1H0YgxyQTz5dxrXxRkQtVdDKClurxXqjwO5ErWWrrdodus9F-Cbxbgy-qBNZYG4nOvWsPJppNZHlgNZInoC1nitOtOs3A_MBM2-U31GIzwG5aPZlzlP-dbqZKZxQXiriK5MnRZ7Up6jVgdHYt0AgC-X179AzLP35jVjMuSca5z7SixZY5VNCmHWia2vU3NdSBOeISqRxgR1r7mlvOUlksn6v9g43vbsDMUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
املاکی رو ببینید؛طرف یه ساعته داره جلوش گوه میخوره بعد این کصخل یجور لم داده رو صندلی که انگار تو تخت بغل ملانیاست
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69863" target="_blank">📅 01:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69862">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d1e744df.mp4?token=HLXZnvGVKRcvIMZsz5T-swuScqd6ILOHZ3e_3zQLk85PEWQWikLGiAzPVnBmWljv11Z-PRv76qzP9L4hXt64uwocRIdmocoxKQCJpVTUuzDk3-WXDVTnJudggPMYIU4IiAjIKJfaK7HUWLmodgGAk2r77V8EikI3rRWWbDue0ID6PRgpLFbqdPPQ_lb886ohVnVPpBOIda7YBYQ8_c6ktiqqj6mIfX8zOxBM4MqxiS2GwrBZbzCneEJhGIW2gXiCdCn3JFjpZWRmojsYO-HWz-9R3czFb332siXiBpYtQazqqRnyQzo9JzPamb-v4q7jZZaJN22RL2itZ35UO6hf9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d1e744df.mp4?token=HLXZnvGVKRcvIMZsz5T-swuScqd6ILOHZ3e_3zQLk85PEWQWikLGiAzPVnBmWljv11Z-PRv76qzP9L4hXt64uwocRIdmocoxKQCJpVTUuzDk3-WXDVTnJudggPMYIU4IiAjIKJfaK7HUWLmodgGAk2r77V8EikI3rRWWbDue0ID6PRgpLFbqdPPQ_lb886ohVnVPpBOIda7YBYQ8_c6ktiqqj6mIfX8zOxBM4MqxiS2GwrBZbzCneEJhGIW2gXiCdCn3JFjpZWRmojsYO-HWz-9R3czFb332siXiBpYtQazqqRnyQzo9JzPamb-v4q7jZZaJN22RL2itZ35UO6hf9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: گفتید این آخرین فرصت ایران هست چیشد؟؟
🇺🇸
ترامپ: به زودی متوجه خواهید شد
ما توانایی افزایش تنش رو داریم
خسارات های جنگ رو از طریق منابعی از ایران جبران خواهیم کرد
خسارتی رو اگه قرار بشه کسی جبران بکنه این ایران هستش
هیچ اتفاق بدی قرار نیس بیوفته
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69862" target="_blank">📅 00:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69861">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10abc62a6.mp4?token=oZobV7hZx3FgkSHjEat8SbbAMKBuya98-Alo_iwNvLgUWDe4te01DIItkeiGWA9ILMS2zeylUiFTgqUz-9IDj3X5mZPwQQmahmSLVIbewJoGQA-ng0ABku6qJhg2h_SbZEal1qv3DhOSMapKQm2O8OW0idqdqiqXfqT0z2jef34XoMlLX73taa-o8uN6rTaUDd0f4lLo4Focb7ksv2SA14vvEKB7kv7c33oLYtO-EUDlNqK7bZHHPPdvE3i1m78cj7kIVmzNr7UObof6PypmILP0h47feePlwgxhoOFHj7C-8hOZZQtsVKcXTcZncXBWMtrrCKCTsRrsA4dE-5jcMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10abc62a6.mp4?token=oZobV7hZx3FgkSHjEat8SbbAMKBuya98-Alo_iwNvLgUWDe4te01DIItkeiGWA9ILMS2zeylUiFTgqUz-9IDj3X5mZPwQQmahmSLVIbewJoGQA-ng0ABku6qJhg2h_SbZEal1qv3DhOSMapKQm2O8OW0idqdqiqXfqT0z2jef34XoMlLX73taa-o8uN6rTaUDd0f4lLo4Focb7ksv2SA14vvEKB7kv7c33oLYtO-EUDlNqK7bZHHPPdvE3i1m78cj7kIVmzNr7UObof6PypmILP0h47feePlwgxhoOFHj7C-8hOZZQtsVKcXTcZncXBWMtrrCKCTsRrsA4dE-5jcMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
پس تنگه هرمز کِی باز میشه؟
🇺🇸
ترامپ : بازه!
ما صددرصد کنترل تنگه رو در اختیار داریم.
همون طور که احتمالاً شنيديد، كل تنگه رو مین روبی کردیم. البته شاید هم نشنیده باشید.
اونا میتونن دردسر درست کنن، ولی ورشکسته‌ان؛ پولی ندارن، ایران کاملاً ورشکسته‌ست. حتى حقوق سربازهاشون رو هم نمیدن، نرخ تورمشون 309 درصده.
ایرانی ها صدها هزار نفر رو کشتن، حالا دارن تاوانش رو پس میدن.
اگه قرار باشه خسارتی پرداخت بشه به نظرم ایران باید اون خسارتها رو پرداخت کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69861" target="_blank">📅 23:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69860">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
گزارشگر: شما گفتید که این آخرین فرصت ایران بود. حالا چه؟
🇺🇸
ترامپ: شما متوجه خواهید شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69860" target="_blank">📅 23:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69859">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8eb808fce.mp4?token=G8hvg50N5Fl9QbZ-va-Ib5vpLYb3pIiHNtPA8N7IpOR2D1QICir8SYfzjiA_SXt0rCh5Fu8YTp00Kh_dTWECALMqEwMbkYgkbrB7zHEcPFKTHMu0J2BpaEdS9YEAatqfbQ2xWZIbfUjhm64VBbjlncNMaWsg5mrZUY66M-NWAMT1UvL1ZqR06QG_Pb13rzNhSX3_hFrmEeNjQ2ujw7rdeegoQOKzTOtr4cbsO25liNjK27wOyAJKjgNqhkE45NHEkN_xtfpad7kmBDtx1HG4ilwxNaE4xhLszTx7MMqhzQVrx46K9MYfKpd2V5cUy70pSipdpNM5QTnh7gbVJcOTHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8eb808fce.mp4?token=G8hvg50N5Fl9QbZ-va-Ib5vpLYb3pIiHNtPA8N7IpOR2D1QICir8SYfzjiA_SXt0rCh5Fu8YTp00Kh_dTWECALMqEwMbkYgkbrB7zHEcPFKTHMu0J2BpaEdS9YEAatqfbQ2xWZIbfUjhm64VBbjlncNMaWsg5mrZUY66M-NWAMT1UvL1ZqR06QG_Pb13rzNhSX3_hFrmEeNjQ2ujw7rdeegoQOKzTOtr4cbsO25liNjK27wOyAJKjgNqhkE45NHEkN_xtfpad7kmBDtx1HG4ilwxNaE4xhLszTx7MMqhzQVrx46K9MYfKpd2V5cUy70pSipdpNM5QTnh7gbVJcOTHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
🇮🇷
عظمایی فرمانده نیروی دریایی سپاه پاسداران انقلاب اسلامی:
«اگر اسرائیل، ایالات متحده، یا هر یک از همدستان آن‌ها حتی جرأت کنند نگاهی خصمانه به جزایر خلیج فارس داشته باشند، با کمک خداوند متعال؛
چشم‌هایشان را کور خواهیم کرد و خلیج فارس را گورستان آن‌ها خواهیم ساخت.
»
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69859" target="_blank">📅 22:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69858">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c15a39d1d6.mp4?token=uLwUcF0tQAAcDuljAeCMsyyadIFaHiMS2wRRQ_SeyJsXGoeFKbN5NMKlCZ9T7EzLnKkVf52L9dVz7zPzC3N0outQLEevWmCtVOlmKAEmJT02u6KeCnENt4MPkHbyZKiKbRvn2-I-xr54qb9C4ZOv1ZJ0hknRTGvy6Xzl-uq32x4352OueL11h0V9-gnxleD-db762Oz7T5K-KRasSOd0inzXegzc1MSgdofGxijF1SqapsjAA1VlHzo_THt44BmpCq3dpegb__cFoBQDiDIAn855IeiMaSSVW-dbL998VVF8oik5BMnGNT8e-WQAclDJh9ikNOGjQnwY4EzA9itgBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c15a39d1d6.mp4?token=uLwUcF0tQAAcDuljAeCMsyyadIFaHiMS2wRRQ_SeyJsXGoeFKbN5NMKlCZ9T7EzLnKkVf52L9dVz7zPzC3N0outQLEevWmCtVOlmKAEmJT02u6KeCnENt4MPkHbyZKiKbRvn2-I-xr54qb9C4ZOv1ZJ0hknRTGvy6Xzl-uq32x4352OueL11h0V9-gnxleD-db762Oz7T5K-KRasSOd0inzXegzc1MSgdofGxijF1SqapsjAA1VlHzo_THt44BmpCq3dpegb__cFoBQDiDIAn855IeiMaSSVW-dbL998VVF8oik5BMnGNT8e-WQAclDJh9ikNOGjQnwY4EzA9itgBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باشگاه مختلط تو قیطریه تهران همراه با استخر جکوزی سالن  ماساژ سالن بیلیارد سالن بولینگ و...
😟
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69858" target="_blank">📅 22:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69857">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uI7OCa3bqAxVhWUDF6-bIqYtFtiIUzmO1suE_Fp5qDN5IqSmiQXI6gbz0CYQt4OArjC7D2SlCoGZV5SmWDpndEyX0Mz87vqJFJctCOuOAKGOY7IX6Aae_t_14ZkGGoHjbj0EYd12wMAI1lO-MQ8i7dM5fq6KbJL9P-4Aa0FJC1qQvHTyzBqJZYLSvgyjIfHvPyan23bOH7MtWgNa7eXj_TYZuE9TGHnRs0qxEuIlMrGiGef4V-tJt0hFL9nZJsmSpOuafO1eAQVhtSSYFofg6JbfhnkHdJ1UliUFhBGBtIPbkd9G0z_1zyrv9YBBoy3-IqXhT6YkE8PnU-P4N0Lp2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
پرزیدنت ترامپ درباره ایران:   می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار غرامت بابت خسارات وارده به خود در جریان درگیری نظامی پنج ماه اخیر هستند (درگیری‌ای که آغاز شد چون آن‌ها نباید به سلاح هسته‌ای دست یابند)؛آن هم در حالی که این موضوع هرگز در…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69857" target="_blank">📅 21:26 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69856">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79470446aa.mp4?token=PP5nntp8Uophg8Gtjz1jahQDy0DVMgWoEHcfGsq8IeqcYbO9dHpazVQCqCZVPYc9EQ8UwhkWP63-6_-N_boir0ZKMzfd0VBfBhDioG0lGC-s0t23f1l5MPCrb0KVFFDDAWGsZd0BBDNVsWxYlysgFho2dQNrdsayrWAXBTuZe2ipEeOOaE0_FYxqDf8IGmByRi88qj6UaV7a8bYfAi5GTAFHvFpeq2B4mXGwecjozXJbVVRiaMwPyZRvOkibhUnP7Qle97nhi2ExJ5tbqs4tjhz1UPZFR6-X8aFBsG_V5UJ2m3p3HcJ3McB3QNdplDKbLtQpCwxRWyDXotmzZPWyEi4LKU4KRicd-hJyV3UF87Texyi_xIitQyiL4hYZhTYX5wbfVPUSkO9Tqx6Uq53u2BizjXv55ZwHKgCSFC3r4iEy57Wb92wlFQKQYAtD90wWESUMZw5_Aon8IH1gH0jKf51dAV6eoxn-pFQ2DRgiOUNvyQSU5XW5g6hVhbD08Rhf10T5tcVrmTk_DhWx0g5G5sKGsyjmjaLoE72a8SQ244PBCmMHVKf_5HwKAXejGDGuTBM88ChcxYVdVoEQW5sWNLrtmCQWoEUoZ0PlocyT7sSXvhhL9YoG-a5gb7G_TEpKfz55ZfTid15pkFG_Yq3BY1uYW_I-gAbc2tqCeFFyzoU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79470446aa.mp4?token=PP5nntp8Uophg8Gtjz1jahQDy0DVMgWoEHcfGsq8IeqcYbO9dHpazVQCqCZVPYc9EQ8UwhkWP63-6_-N_boir0ZKMzfd0VBfBhDioG0lGC-s0t23f1l5MPCrb0KVFFDDAWGsZd0BBDNVsWxYlysgFho2dQNrdsayrWAXBTuZe2ipEeOOaE0_FYxqDf8IGmByRi88qj6UaV7a8bYfAi5GTAFHvFpeq2B4mXGwecjozXJbVVRiaMwPyZRvOkibhUnP7Qle97nhi2ExJ5tbqs4tjhz1UPZFR6-X8aFBsG_V5UJ2m3p3HcJ3McB3QNdplDKbLtQpCwxRWyDXotmzZPWyEi4LKU4KRicd-hJyV3UF87Texyi_xIitQyiL4hYZhTYX5wbfVPUSkO9Tqx6Uq53u2BizjXv55ZwHKgCSFC3r4iEy57Wb92wlFQKQYAtD90wWESUMZw5_Aon8IH1gH0jKf51dAV6eoxn-pFQ2DRgiOUNvyQSU5XW5g6hVhbD08Rhf10T5tcVrmTk_DhWx0g5G5sKGsyjmjaLoE72a8SQ244PBCmMHVKf_5HwKAXejGDGuTBM88ChcxYVdVoEQW5sWNLrtmCQWoEUoZ0PlocyT7sSXvhhL9YoG-a5gb7G_TEpKfz55ZfTid15pkFG_Yq3BY1uYW_I-gAbc2tqCeFFyzoU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله تند مجری صداوسیما به علی دایی:
وقتی جرائت نداری جیگر نداری به دختر اونور آبت چیزی بگی پس اینجا هم خفه شو لال شو
یه گروهی گول میخورن میریزن کف خیابون بعد از این دایی و خاله ها زیاده هشتگ نه به اعدام میزنن
یکی از این آقایون مشهور دخترش مورد دزدی قرار گرفته بود کم مونده بود دزد رو بکشن بعد همینا هشتگ نه به اعدام میزنن
بعد این وحشیا این بیشرفا جوان مردم رو به شهادت میرسونن یه عده یاد حقوق بشر میوفتن
اعدام نفرت نمیاره شماها نفرت انگیزید شماها ترحم انگیزید
ولی یه پلیس یه گلوله شلیک بکنه داد میزنن عای دیکتاتوریه عای خاک خون کشیدن
شماهایی که لال هستید همیشه لال بمونید حتی اون ور آب
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69856" target="_blank">📅 20:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69855">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTv118J3mw8_WBmS6fOEdmQeUeQemXTLQHn1AihsSlVm02jeuvu8zbk3coklGzRL8Nuxysx2iWLfQa8yd6yHHh64ZTk0kZ-C7PVWkj1J8hDEJ_llRFs1_jmsAqFkrOuANPI2qjFBLXiAGyJ51MnfKMMlMHEOcfUGnAg-LmWSEKi7jQm0oVFJXZHDPycECX1ZqCP7_S2fqfCYEjsxqDYY0y-7-9ZRhGJrGKioZuWo1_OTkdwhHo4GU_T9_tUY8Q5UqIKPWynYzUGnQFW0qY7Xxok-ve7I9BWMczB0x7fr7wYvHg6jpCWlNtu_sQBldHl1qYPkVfiuMIBKxj6krj5TAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
پرزیدنت ترامپ درباره ایران:
می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار غرامت بابت خسارات وارده به خود در جریان درگیری نظامی پنج ماه اخیر هستند (درگیری‌ای که آغاز شد چون آن‌ها نباید به سلاح هسته‌ای دست یابند)؛آن هم در حالی که این موضوع هرگز در هیچ‌یک از مذاکرات یا دیدارهای ما مطرح نشده بود!
اما این ایده جالبی است، چرا که من نیز اکنون متقابلاً از ایران درخواست غرامت می‌کنم؛ غرامت بابت تمام کسانی که آن‌ها با بمب‌های کنار جاده‌ای و در درگیری‌های متعدد — که به آن شهرت دارند و در ابتدا تحت هدایت ژنرال سلیمانی انجام می‌شد — به قتل رسانده یا به‌شدت مجروح کرده‌اند؛
از جمله خانواده‌های کشته‌شدگان حادثه ناو «یو‌اس‌اس کول» (USS Cole) و هزاران نفر دیگر که در میدان نبرد جان باخته‌اند. به‌علاوه، باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران طی ۵۰ سال گذشته به قتل رسانده نیز غرامت پرداخت شود، چه رسد به آن ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
من به نمایندگان خود دستور داده‌ام که این موضوع را قاطعانه در تمامی مذاکرات آتی بگنجانند.
از توجه شما به این مسئله سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69855" target="_blank">📅 20:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69854">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvyPzv7pnYcx1ZiBbkpF5SEI9mnFaR6uWMBrTfZwbq8rsSm9Jtfm09FBXpadsGWdFtNVbqyEaRzzBtPf_Yu2mdFHGvgTQ5Ou5oZ_8Ov6nwFVXVKd4ULYyD7VFbfF2JnwFOe9bKA1MSvpYj5rqOG2OIL28DUwwMC1_81DqoqZOOQsIu57Y1shOOIHp5zz4JhyYVKFj3MUXhyEQHe9rcCVkDFaWkaR9QmJ4mIcB8scZ5LmsSgQyaf8km9Irtkwpj8Up2gZKGmt0M3d4v9oWAr-sJ3-Ol7aTB7sw14NlWKnmkPlTZmypvBRDHbk-8z9H8ccnFuD1YVAYhklPUVzG25x5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
مرندی:
‏ایران آگاه است که نیروهای رژیم ترامپ در کویت، امارات متحده عربی، قطر، عربستان سعودی، بحرین و اردن در حال بسیج برای یک حمله برق‌آسای بالقوه - احتمالاً در کنار نیروهای اسرائیلی - علیه مردم ایران هستند. جمهوری اسلامی با پاسخی سریع و کوبنده آماده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69854" target="_blank">📅 19:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69853">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🔴
🇮🇷
لیست فرماندهان جدیدی که مجتبی خامنه‌ای انتخاب کرد:
سرلشکر  علی عبداللهی به عنوان رئیس ستاد کل نیروهای مسلح
امیر کیومرث حیدری به عنوان جانشین رئیس ستاد کل نیروهای مسلح
سرلشکر احمد وحیدی به عنوان فرمانده سپاه
سرلشکر مصطفی ایزدی به عنوان جانشین فرمانده کل سپاه
حجت الاسلام طائب به عنوان رئیس سازمان بسیج مستضعفین
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69853" target="_blank">📅 19:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69852">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f1723f2a3.mp4?token=CNSYpoj525XnZGkOLvak-cdUAVSOOnu1xZ1fWlXdhO57lA1BeAMnEeFUFTILFEZSKkDX8eAoObAAmTP2GWzhw4RMXMJEl7mE-L1UGA8UqpZkPIuJcdYrbfEsQimF-xHrishh6pSQOq1TFv4fX3GcSRL7oPyFJT5B9SuHiWRJ0y0DU0x1llNZ4gc8XkXAyGJiXJUXF15ftVEUllk63Ri_U7gnh17xFnZtSbPI7ilRlyI9aryqidM3nfFd720S9MbCsOax2Qr12BV2kUtrNa58_fLgZJwkG_g3-eR9XJGxVzZyoVG6CMh__S1qr1siF1VdIFZ7FrIZPb1LzE7W_GrTYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f1723f2a3.mp4?token=CNSYpoj525XnZGkOLvak-cdUAVSOOnu1xZ1fWlXdhO57lA1BeAMnEeFUFTILFEZSKkDX8eAoObAAmTP2GWzhw4RMXMJEl7mE-L1UGA8UqpZkPIuJcdYrbfEsQimF-xHrishh6pSQOq1TFv4fX3GcSRL7oPyFJT5B9SuHiWRJ0y0DU0x1llNZ4gc8XkXAyGJiXJUXF15ftVEUllk63Ri_U7gnh17xFnZtSbPI7ilRlyI9aryqidM3nfFd720S9MbCsOax2Qr12BV2kUtrNa58_fLgZJwkG_g3-eR9XJGxVzZyoVG6CMh__S1qr1siF1VdIFZ7FrIZPb1LzE7W_GrTYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇫
طالبان به طور رسمی برده داری جنسی زنان رو قانونی اعلام کرد تا محدودیتی از این لحاظ نداشته باشن!
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69852" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69851">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69851" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🙄
همه بت باز های حرفه ای دنبال
🔞
شکار این بونوس ها هستن
✅
لیگ های معتبر اروپایی شروع شده بهترین فرصت برای جبران ضرر های جام جهانی
💯</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69851" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69850">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4n_tWXjU_8iQ12w-JGmvapUlWAqG2cDF9ZBDnt6qkEvwNI01vxe3Bf3AfN134nCUMADFYVVwG2rc3GOPyRbMqFRoKT507TSGIrpiiRad1G0xSXtGffC19RdoZAg0I5MNTfKPFKoZb-iTy_Mo1gQ4pw3gTWDPxRJ8UsmkNIUHak5z501dt6lqUKPrQn2qHRU7FndlXie1HzhPzw5JXNZi18VWbm5sp6UJURYEF9DK7JfbmudKb0hFskLB2AQe_lb0FsbGO9Y8K_A7WI7IFfNJ6jOxtoAjkHV9vbDviVryZEi1YKJKUEAZP4nqV4NoWSSHWG0aCd22h-aQfuFRHJnjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤔
شروع رسمی لیگ های اروپا
❄️
🆕
بهترین فرصت برای جبران ضرر های جام جهانی با جشنواره رویایی مرداد  ماه
⚠️
هر افزایش شارژ مساوی
2️⃣
1️⃣
🔣
شارژ بیشتر بدون محدودیت
☄️
به همراه
🤩
🤩
🔤
کش بک باخت همه روزه:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
g19
@betinjabet</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69850" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69849">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
⭕️
مجتبی خامنه‌ای تا ساعاتی‌دیگر اسامی فرماندهان جدید نظامی را پس از بیش از ۵ ماه رسما اعلام‌ خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69849" target="_blank">📅 18:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69848">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a2288e087.mp4?token=BHK7lFX7is9HkYVfMhWw16sMhiCKwohc9IBO89yZF12kY-LV9t6N5EhJnZj3Twykw9kwFgva9rHEFz6DEXPLaPvrJ3mCWkDfdFcWXhBdTXFwQU_g0ofnPgHRqz4oQJEb7zkEDYKa6K9lmPVOwCu9b1_iILs0kO1pSiAdacdfNF_9ystgQo4wTNhxRpM94xN0z3lrPlHCC9gGDmJyBHQ_n0CcqXQT3XUu0gvikgzkX2eVoFN50jJ_FAOW9KwUvwCvrL0RVT7DwJHS5M-DDWaEdX6LY35xanwdGag3osUjVOYQ4FszoJX_igfeZhlTftw5xywhfsCdErtR1lCalhClnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a2288e087.mp4?token=BHK7lFX7is9HkYVfMhWw16sMhiCKwohc9IBO89yZF12kY-LV9t6N5EhJnZj3Twykw9kwFgva9rHEFz6DEXPLaPvrJ3mCWkDfdFcWXhBdTXFwQU_g0ofnPgHRqz4oQJEb7zkEDYKa6K9lmPVOwCu9b1_iILs0kO1pSiAdacdfNF_9ystgQo4wTNhxRpM94xN0z3lrPlHCC9gGDmJyBHQ_n0CcqXQT3XUu0gvikgzkX2eVoFN50jJ_FAOW9KwUvwCvrL0RVT7DwJHS5M-DDWaEdX6LY35xanwdGag3osUjVOYQ4FszoJX_igfeZhlTftw5xywhfsCdErtR1lCalhClnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان درباره مجری و کارشناس‌های برنامه به وقت ایران:
این همه علم رو از کجا آوردید؟
چندتا جوون نشستن رو صندلی و درباره اقتصاد، سیاست، جامعه شناسی، کشاورزی و... نظر میدن.
از چهارتا جا یسری اطلاعات ناقص می‌گیرن و بعد درباره‌اش حرف میزنن و نسخه می‌پیچن و جامعه رو منحرف میکنن.
من 18سال تو دانشگاه درس خوندم و استاد تمامم، الان فقط اجازه دارم درباره یه گوشه قلب که تخصصمه نظر بدم نه کلِ قلب، اونوقت اینا...
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69848" target="_blank">📅 18:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69847">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7c4253089.mp4?token=pveA_tmDu3AtLxOhDOctKOs2HM_IbAbfvmEdG7cxmv_oZjNuIKp0hY_Kmi_-qhmdplpLafE9onlbPXnUq0Pf7w1ibnBl9uU8E3JQsCe4oVv00mfztT2KRoiQCqa7S3S4BqG2LwTj4J4xXUoomD0ufrtcwmJR8ILTNrgwkuA8NPCCXs_7UM4Cd_4-2e0kP5N6tNHjMV7dnaWCCiPJu7I6388G1iz_OKvlkjHe3lxjuYmkRk7P-05IGqxTsMVPnYxaEiInq6zinKqlb4SLTsPlipBYNWZAUa5Tg__0SFDeTt64GB_3xiy5Em9LOjB_Id9Hi2H7wSSDCtF5AnO1UV9BeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7c4253089.mp4?token=pveA_tmDu3AtLxOhDOctKOs2HM_IbAbfvmEdG7cxmv_oZjNuIKp0hY_Kmi_-qhmdplpLafE9onlbPXnUq0Pf7w1ibnBl9uU8E3JQsCe4oVv00mfztT2KRoiQCqa7S3S4BqG2LwTj4J4xXUoomD0ufrtcwmJR8ILTNrgwkuA8NPCCXs_7UM4Cd_4-2e0kP5N6tNHjMV7dnaWCCiPJu7I6388G1iz_OKvlkjHe3lxjuYmkRk7P-05IGqxTsMVPnYxaEiInq6zinKqlb4SLTsPlipBYNWZAUa5Tg__0SFDeTt64GB_3xiy5Em9LOjB_Id9Hi2H7wSSDCtF5AnO1UV9BeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
فیلد مارشال محسن رضایی (1392):
اگه آمریکا به ما حمله کنه ما همون هفته اول هزارتا آمریکایی رو اسیر‌ میکنیم و بعد در ازای آزادی هرکدوم چند میلیارد دلار از آمریکا پول میگیریم و اینطوری مشکلات اقتصادیمون هم حل میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69847" target="_blank">📅 17:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69846">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b47958b9.mp4?token=iyQhy-j1SMUKl9El8zrXDZMj2mlX8YZ2d01o6KEeL_2uRoqNIcJIbjLlYYg_54UKQWLT-wdl7n99vK3nxii2TfTkmZNyLqI5GiZ0Mr1SXdFY-o2usDkzTf12vpi-p0ACJI5RST8Lc41VDCvBbjP_GuuHZoxwPLwkwK-QwrnPz8gCA3cuJTkYL3FwOCL1pmqoWXfeycYONSsxgk1JupgGh_9PemG3C2D-msPLFCW8PiNdanRuiKV5QlGIzhRKBOSSAREKMFfbEjjZydLw6KcHsdSeWCcgc7AzSMPJAWEZYvfPHmAYDGgBGz0ZJE2QzIpkGQv2bjPakOgYEYUKjwE2WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b47958b9.mp4?token=iyQhy-j1SMUKl9El8zrXDZMj2mlX8YZ2d01o6KEeL_2uRoqNIcJIbjLlYYg_54UKQWLT-wdl7n99vK3nxii2TfTkmZNyLqI5GiZ0Mr1SXdFY-o2usDkzTf12vpi-p0ACJI5RST8Lc41VDCvBbjP_GuuHZoxwPLwkwK-QwrnPz8gCA3cuJTkYL3FwOCL1pmqoWXfeycYONSsxgk1JupgGh_9PemG3C2D-msPLFCW8PiNdanRuiKV5QlGIzhRKBOSSAREKMFfbEjjZydLw6KcHsdSeWCcgc7AzSMPJAWEZYvfPHmAYDGgBGz0ZJE2QzIpkGQv2bjPakOgYEYUKjwE2WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی سمه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69846" target="_blank">📅 16:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69845">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37165ac1ad.mp4?token=HjQVNgOa_8OOVgm1lB6FSqVRv2TmQMS3HRUP3foxYQK7nyNhRYL-Va-GtIkTxaFHvflir3Ul8ZFO_tuXVTk36wc2YZwieNGOLXoD_j52pOuK_jo5gSb3NrosM0siTqCLqjC20mOPKXtLRqo0GyRNoAb-MRVtfQdwURSuMlT9QVeHr6MKa4DzIru8LwQBMRHfVBIs2_bzXlZerodtIHl_rwa_27khHm5Fj-rJVzCAMYnXvnTpcbiq7FagBvXo3jnWyiENG7PZEBaNpcuef7dXpoKVsXh3VOMHQrLMbCJ99xPnh_ecQR8sKiDpDtL6EwmzyI4Qt7ZezArcPQdin3E_7C4WXG16_Zy8wb0dJ4QuikPXUjRNFMdCSp62NRK76e5QJ8OL11HNy0e1VXAgTyuMHQ063ubmRQysaX9V71SpAk8sahhyEwFHHobZBKo0n9qSfpYDncsQDEw7Gb3ZGR377So5ubsD3tAoEkYUW50KvfTgoOZdSj3AQcRD1Rx101Poxh5GXZTGztq4qqexwuTOmtZL5PztpFj24ZuCZQK3q_9cVMXk0gQ4VKZPaqj42Pea0G6rHA-HkqnI-Vkdsbb3tM1M0XrZIEMjJy0ggBPV0T6TK9uD75QixW3CbqKEELjEKOFWccyYmdLvhcL-9oViG-3CPPc5ZH0HxG3Gg-3rnsI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37165ac1ad.mp4?token=HjQVNgOa_8OOVgm1lB6FSqVRv2TmQMS3HRUP3foxYQK7nyNhRYL-Va-GtIkTxaFHvflir3Ul8ZFO_tuXVTk36wc2YZwieNGOLXoD_j52pOuK_jo5gSb3NrosM0siTqCLqjC20mOPKXtLRqo0GyRNoAb-MRVtfQdwURSuMlT9QVeHr6MKa4DzIru8LwQBMRHfVBIs2_bzXlZerodtIHl_rwa_27khHm5Fj-rJVzCAMYnXvnTpcbiq7FagBvXo3jnWyiENG7PZEBaNpcuef7dXpoKVsXh3VOMHQrLMbCJ99xPnh_ecQR8sKiDpDtL6EwmzyI4Qt7ZezArcPQdin3E_7C4WXG16_Zy8wb0dJ4QuikPXUjRNFMdCSp62NRK76e5QJ8OL11HNy0e1VXAgTyuMHQ063ubmRQysaX9V71SpAk8sahhyEwFHHobZBKo0n9qSfpYDncsQDEw7Gb3ZGR377So5ubsD3tAoEkYUW50KvfTgoOZdSj3AQcRD1Rx101Poxh5GXZTGztq4qqexwuTOmtZL5PztpFj24ZuCZQK3q_9cVMXk0gQ4VKZPaqj42Pea0G6rHA-HkqnI-Vkdsbb3tM1M0XrZIEMjJy0ggBPV0T6TK9uD75QixW3CbqKEELjEKOFWccyYmdLvhcL-9oViG-3CPPc5ZH0HxG3Gg-3rnsI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بقایی سخنگوی وزارت خارجه:
تنگه هرمز از زمان حضرت آدم تا ۹ اسفند برای همه باز بود
ادعای ساخت سلاح هسته‌ای ایران توسط نتانیاهو دروغی بیش نیست
به ترامپ بگم که ایرانیان شطرنج بازان حرفه‌ای در طول تاریخ بودن( ترامپ جنگ ایران رو به شطرنج تشبیه کرده بود)
هیچگونه مذاکره مستقیم با آمریکا نداریم
باز شدن تنگه هرمز منوط به لغو محاصره دریایی هستش
نگرانی بابت پیمان دفاعی مکه نداریم چون همسایگان ما هستن
بحث کنوانسیون دریای خزر به مجلس ختم شد و تصمیم نهایی با اونا هستش
درباره عمان نزدیک به یک تفاهم هستیم و به زودی نهایی میشه
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69845" target="_blank">📅 16:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69844">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c431777b9a.mp4?token=EtkKJfwRKkUrBYiaSXd2ERNKUDSeUubGd0E6n_cprQnZD2nlulqjTgd2S8pQMd4Q2pSWdGo3A8VNpRYhKJdxYeOADbtseNu6UoSs5n1MF8xOnrtIstkD9UwwSY5k7W4vVkZxSIuX6LgNHpf6uxWIUaMuN4DDzrheQ_2PHA5yaMBTQqMmcrZTOV73kZ6ESZkVHHUI79Es-IPNxjIz9-P183oRt8FXUztDOoANR6QecHRDICKpeqCdKaebJUVwDSrs6c0DqLjNsAf7z1zQlNW9lsOC044H5FAuLVgeam7OXTzUHMQCypsMnBv0f_3ttIb_TNZmo2-BTaxqXtZ1P1FM5DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c431777b9a.mp4?token=EtkKJfwRKkUrBYiaSXd2ERNKUDSeUubGd0E6n_cprQnZD2nlulqjTgd2S8pQMd4Q2pSWdGo3A8VNpRYhKJdxYeOADbtseNu6UoSs5n1MF8xOnrtIstkD9UwwSY5k7W4vVkZxSIuX6LgNHpf6uxWIUaMuN4DDzrheQ_2PHA5yaMBTQqMmcrZTOV73kZ6ESZkVHHUI79Es-IPNxjIz9-P183oRt8FXUztDOoANR6QecHRDICKpeqCdKaebJUVwDSrs6c0DqLjNsAf7z1zQlNW9lsOC044H5FAuLVgeam7OXTzUHMQCypsMnBv0f_3ttIb_TNZmo2-BTaxqXtZ1P1FM5DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
پزشکیان:
با رهبر هفت ساعت دیدار داشتم و درباره مسائل مهم کشور باهم گفتگو کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69844" target="_blank">📅 15:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69841">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YeGKBJwuHdUktTveeVZOVRJHup9vsUGtL_9QRwbevv6nYI2vojePFrnbK2SENqHIrNl39SZD0W95XuiA2V5GPIayLyxwlQ4x2L_8HZz2t8zRghhXqF4NMlFfgCsOSr0uRyMtfJUpuOdNxpwZJoXLKx2VGo53PDchx9g1e9dwqgLeI6MDixyNx9dSGQMnheyJ4Wnb41kLPZtOfS1PPuG55NHV6t0z8rSh1-0p5rPbLtjXh1p5UUYmA_tIp6nCRiFqbLKebRL9MSzA2uHFsN9E8ejdIR0Mhx73gfNGHXnqwEhg-DdkLtUe7851mgFROm0150iNoVkgRAtToWQ5UKfXUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vUYsgp7OQ-SBU-xbhAkv1HzVZ4RKd_lpJpgr6zhJzHRVwzISdpOF6UPpQ0dV2FqqNa6iQiPqwcfdgfSjIP8gdijMiRNJjKfrXDvi6QWt3_TKNwb1Rs2-NASNfx8FwODC-S5x2tS1F9HoZzzKCKlRbnrQ5g5Rs7vM6G3JpaYnDOuZzF-6xOhB9s7T-HINGwDarh1ISufR6P9hinK0jnjK2HfOwCgPcM7pFYuUf4bwdZWbT2huLD1vhhkf1iZtDWkfbA6Re-kXPCYcdhn39T8OziBiVU0MYfPO_CxtsL4yKYFLdtzej_8aTQA84gK06NEE5ByConMNzGcZ6xPlWLNI0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92217bf769.mp4?token=ie7lY8kslkGCLXmePrRczoz2KuzsUD0b3SmUjuP5U0H52fCqwq6nyf7dvNPG8uR_-N_sP4QylVxtl2D9wAzOn7safKshMoBOqzG-N4s28MG2VNz4rMi_Q67s4-W2bPuSPq3pBSg4VV9hqSHAJqbIiSYIMnAtoETFfkRYvRZW7xShXh7jkUa6N-Z1fyUUFTbqwrHogJGAYRQSQptZgfghSoMo-IIGKBzdqXESSPfqDx-hKFX2jGQ3uOSI5fihBJ2csGFGuFiVkXm1DHEDNSS7PmjyFpKk1UKbWYvX_ZOeS1OtsFUHoo2WiLqEVkRXwgSj9Afa8jxHqW1EKScLhp3esQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92217bf769.mp4?token=ie7lY8kslkGCLXmePrRczoz2KuzsUD0b3SmUjuP5U0H52fCqwq6nyf7dvNPG8uR_-N_sP4QylVxtl2D9wAzOn7safKshMoBOqzG-N4s28MG2VNz4rMi_Q67s4-W2bPuSPq3pBSg4VV9hqSHAJqbIiSYIMnAtoETFfkRYvRZW7xShXh7jkUa6N-Z1fyUUFTbqwrHogJGAYRQSQptZgfghSoMo-IIGKBzdqXESSPfqDx-hKFX2jGQ3uOSI5fihBJ2csGFGuFiVkXm1DHEDNSS7PmjyFpKk1UKbWYvX_ZOeS1OtsFUHoo2WiLqEVkRXwgSj9Afa8jxHqW1EKScLhp3esQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
دیروز عراقچی برای مهمانان خارجی تو ساختمون وزارت خارجه بساط تعزیه راه انداخت
😳
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69841" target="_blank">📅 15:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69840">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7709b161ed.mp4?token=Q3iOnNkCv1OJd0MaUOBUGCCRV1k2IJ_uCXPNqSk0gByfkUQ-udtgf1J74yd0Rnpm0VTQpT_aoAYloGX_PQUx6E9Rc3qtmSoSXQJvxlJv0TbZaQ7kBEzCS30GgYF1hb9e_dCUljIejiziEi3eDpNzfmlH_kJJ_jd9YcI5V1PYBT1OMPCGJlo-R4ezfm1jhGCe5VMh40K8-NjRzvxyk1jW-nQCvFhhifCOGp1M-STO3D8xPIsQkUaQveSNUYrM1upTprBS28YKMF8xyTq_IJrO6OGkQaVaYU3I7Z6C6stTJILF3lObQSmnoL1dlIv7NOxJ3dGr3HVB50law17tKpUm2A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7709b161ed.mp4?token=Q3iOnNkCv1OJd0MaUOBUGCCRV1k2IJ_uCXPNqSk0gByfkUQ-udtgf1J74yd0Rnpm0VTQpT_aoAYloGX_PQUx6E9Rc3qtmSoSXQJvxlJv0TbZaQ7kBEzCS30GgYF1hb9e_dCUljIejiziEi3eDpNzfmlH_kJJ_jd9YcI5V1PYBT1OMPCGJlo-R4ezfm1jhGCe5VMh40K8-NjRzvxyk1jW-nQCvFhhifCOGp1M-STO3D8xPIsQkUaQveSNUYrM1upTprBS28YKMF8xyTq_IJrO6OGkQaVaYU3I7Z6C6stTJILF3lObQSmnoL1dlIv7NOxJ3dGr3HVB50law17tKpUm2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وایرال شده از قیمت یک پک آرایشی که ناقابل سه میلیارد
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69840" target="_blank">📅 14:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69839">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3Y_sK1_d2M3l3wPB698R-PauBLtSgx20sHMYxaBNUwJ_DA49gvAwPtDSae9w5d9pogPOEl6DAZsTyHA_K9CSLVIlFmaIyQdhfC6Ep2Ll7hwZFaNU8m4FU6AYs79fK1DfqNZ41vDaVB4TqACvTW-LjZeed_RAOgHMO488RzSAPj9qi89CVeqsMYGyFOl-EyrPJTXueKs5SYu4PrWOpRAO1YOe_RpnXiEWY0kmoFIur0qHU-Hwv_XDpAbnetXsTDKxT6_MRDzFx2c_Da8Fjzxct4D0Tm_u2qd1Hp1n_Njj1-vNcyijyT1ysEL8dAkvryQsvdloCYAafyMZO13GCWjjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
یک مقام ارشد آمریکایی به من گفت که کاخ سفید از اظهارات نتانیاهو درباره طرح غزه «ناراحت نیست» و آن را بخشی از فضای انتخاباتی اسرائیل می‌داند.
این مقام آمریکایی گفت: «ما نیازهای سیاسی "بی‌بی" را درک می‌کنیم. تا زمانی که او به انجام آنچه ما می‌خواهیم ادامه دهد - به‌ویژه در خصوص مهار حملات به غزه - مشکلی با این موضوع نداریم.»
به گفته یک مقام آمریکایی، نتانیاهو هفته گذشته در تماسی تلفنی با جرد کوشنر، فرستاده رئیس‌جمهور ترامپ، وعده داد که علی‌رغم تردیدهایش، به این طرح ۱۵ ماده‌ای فرصت دهد و حملات به غزه را محدود کند تا روند خلع‌سلاح این منطقه بتواند آغاز شود.
از آن زمان تاکنون، اسرائیل حملاتی علیه غزه انجام نداده و ارتش اسرائیل (IDF) به‌تدریج در حال عقب‌نشینی به سمت «خط زرد» است. هم‌زمان، آمریکا و میانجی‌گران خواستار آن هستند که حماس روند خلع‌سلاح را آغاز کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69839" target="_blank">📅 14:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69837">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d242d991d.mp4?token=Y7yyJyqoRFQqzgLC5kcA0CvOxVIlFU7BhV-BywhjVcq7BS4xg5iRMIN2tjeGJzIum_MGEF0GJpdX_PeYqYF65sV8MmvLWgEDCwX15Ywaf1UrNv_s6mf-zvhjB3xJ9VSkv0M6EHvaJ9lHuSdaqrDFJa1O8wOyEjm9ItvLHl_-GNps9HE1a7uto9qlgj8fc-bZUDDtUJNVWsmf_pDcrxNsDj8Hn7nu-FdDmCoRplkoKq7s65Ff11djrrnvuwrsCbKVMzX6AiNKeo1uaiu8jTvitCiIfdQBCszbNAC_U_XK1Qq2QOByi4KEiNmnfSy8QuF2uraYq5h_cE7cVUo4K_HXFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d242d991d.mp4?token=Y7yyJyqoRFQqzgLC5kcA0CvOxVIlFU7BhV-BywhjVcq7BS4xg5iRMIN2tjeGJzIum_MGEF0GJpdX_PeYqYF65sV8MmvLWgEDCwX15Ywaf1UrNv_s6mf-zvhjB3xJ9VSkv0M6EHvaJ9lHuSdaqrDFJa1O8wOyEjm9ItvLHl_-GNps9HE1a7uto9qlgj8fc-bZUDDtUJNVWsmf_pDcrxNsDj8Hn7nu-FdDmCoRplkoKq7s65Ff11djrrnvuwrsCbKVMzX6AiNKeo1uaiu8jTvitCiIfdQBCszbNAC_U_XK1Qq2QOByi4KEiNmnfSy8QuF2uraYq5h_cE7cVUo4K_HXFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فوران یک آتشفشان قدرتمند در جنوب غربی کلمبیا
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69837" target="_blank">📅 13:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69836">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81027c9c4b.mp4?token=N3ck2a2KxjiQqTacBgk2jp2Qmp4C1ZZQX1LO8tyA1r7v8V_-lG7HZhPDPqu_BxaSva-kP9NBvbDJyNkWPef2-viwDRqin4fLtQabVDUL4u1J7rtPhjFYcaFzpN1lw3za-DHEqqNJb3AxgO25QNysGhqAGDAnshxuingorzAGs3MPb4Q4I8GUveof1wFvvwf6ax9bWc7ePvPF9Mth0w-WJjaCGj81SLP0_oPwXG5w3YNgG1GAHj_aJNUqNU6Wvd4_pdWveIOQQlJAzXEFWYnuKtretVnBkMDgL1gsKxrJhmGBe33XPUuKF5AmfLFMtKcIDItOUiJgvTbFOjzw-50c6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81027c9c4b.mp4?token=N3ck2a2KxjiQqTacBgk2jp2Qmp4C1ZZQX1LO8tyA1r7v8V_-lG7HZhPDPqu_BxaSva-kP9NBvbDJyNkWPef2-viwDRqin4fLtQabVDUL4u1J7rtPhjFYcaFzpN1lw3za-DHEqqNJb3AxgO25QNysGhqAGDAnshxuingorzAGs3MPb4Q4I8GUveof1wFvvwf6ax9bWc7ePvPF9Mth0w-WJjaCGj81SLP0_oPwXG5w3YNgG1GAHj_aJNUqNU6Wvd4_pdWveIOQQlJAzXEFWYnuKtretVnBkMDgL1gsKxrJhmGBe33XPUuKF5AmfLFMtKcIDItOUiJgvTbFOjzw-50c6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشتیبانی سنگین و فوق العاده از نیروهای زمینی آمریکا در جنگ افغانستان ( طالبان ) توسط بالگرد آپاچی ۶۴ با توپ ۳۰ میلی متری M230 Chain Gun
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69836" target="_blank">📅 12:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69835">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ea33d827b.mp4?token=Vy_oPxA8NrKt8nwRAy7qWWAKCwxSEhWY3gA0-04Aoh7d9NrxdYYEfWgoF6rhfPqDnxfq5o1DmbdEFWOWAT2a_UrIgJnn9MG363qgGWcaLk4e6l6N_7WQ59qOCGiUoG1iNFqdRFADcqwcFunSlU-dCZS7I8L7_bTyCHjCwQLkOnx5vbJ3qVwsZ5GTLFnpOGK6uuGm_wJv9imKxgfLqeaQwAAmmiBK9aeMeswZjQOSRiShEgdOD4vq7TKEo45QURJwvZ2ghYIyF8vu2W256YadRzIt4oJWbnpIn-RCwbTe0ZH_H0UPjmii54uZPVPZC0PxqpfWc-mDvj3SAsl58NJOXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ea33d827b.mp4?token=Vy_oPxA8NrKt8nwRAy7qWWAKCwxSEhWY3gA0-04Aoh7d9NrxdYYEfWgoF6rhfPqDnxfq5o1DmbdEFWOWAT2a_UrIgJnn9MG363qgGWcaLk4e6l6N_7WQ59qOCGiUoG1iNFqdRFADcqwcFunSlU-dCZS7I8L7_bTyCHjCwQLkOnx5vbJ3qVwsZ5GTLFnpOGK6uuGm_wJv9imKxgfLqeaQwAAmmiBK9aeMeswZjQOSRiShEgdOD4vq7TKEo45QURJwvZ2ghYIyF8vu2W256YadRzIt4oJWbnpIn-RCwbTe0ZH_H0UPjmii54uZPVPZC0PxqpfWc-mDvj3SAsl58NJOXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پرستار از اتفاق عجیب شب زفاف یه زوج میگه:
ساعت ۴ صبح یه خانم با خون‌ریزی شدید به اورژانس منتقل شد و اول فکر کردیم
سقط جنین
اتفاق افتاده، اما بعد مشخص شد مربوط به
شب زفاف
بوده.
خون‌ریزی اون‌قدر شدید بوده که مجبور شدن بیمار رو
جراحی
کنن.
⏺
پرستار توصیه کرده زوج‌ها برای اولین رابطه عجله نکنن و با آرامش و احتیاط پیش برن تا به این روز نیافتن
.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69835" target="_blank">📅 11:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69834">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53aa49426e.mp4?token=BaRqAIlDoN4lWY_bglQPmVxPacAGeU4JZgZ1-eI5ErjaaUrPXwrplyC_MEav6RJVN7YZXhI3HhKCLH6VLSnAJeVac3Vgh1nPTQHcjiBEcnhvbYU8LgrVNCzWKQ4h5VkKJplbW7Q8KUKPzQX--CJghHxiEfBD2MR6WIo-qjjZSRMnNYVA6oYbWC7P83xTssBKYW4cjz9o6PocXhHq84AUNQGt7E4B2_Z6QY1dDmesi2swbtc0YKmH_Q8zD8qTEEX_7N6gNqV3i-CpeP1Fqk2557Frn_SuLsv14mQ9o7CRxbDubGi5qJeBfPUNKmmgSZeshJNKm5HkhJVrVrb5N2br_6nxq5zcvutX_aHDu5hKIBe_plhr1sjmJzD9KDsTMzVSjbPanw8Y_P-poe0RRRj4S9ANI6lWToQsZAKxuaaVqhkYqEMslGjF-0qwORwWm-kSxzoNofbClvZsd_nSsnz9TO3q3XbRaeEeW9B35EK4wNSHIFCA536XCtD6cjeoraF-b7soVF-gN5YW8PffJYnbK72bNIEWL4HC7vprpdqL-PJHRja56I0phspS6jY_IXg1q370Uv3Yi-OH_WHYfDzIBM2ODOrGb7vh3pHjcC1w3EgglTK6b8ZyYPkFDS7NPFmhCzVNRcRfGEBUDZzO3wbmKgCkKEmLvvTGTlGh7_A-ijs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53aa49426e.mp4?token=BaRqAIlDoN4lWY_bglQPmVxPacAGeU4JZgZ1-eI5ErjaaUrPXwrplyC_MEav6RJVN7YZXhI3HhKCLH6VLSnAJeVac3Vgh1nPTQHcjiBEcnhvbYU8LgrVNCzWKQ4h5VkKJplbW7Q8KUKPzQX--CJghHxiEfBD2MR6WIo-qjjZSRMnNYVA6oYbWC7P83xTssBKYW4cjz9o6PocXhHq84AUNQGt7E4B2_Z6QY1dDmesi2swbtc0YKmH_Q8zD8qTEEX_7N6gNqV3i-CpeP1Fqk2557Frn_SuLsv14mQ9o7CRxbDubGi5qJeBfPUNKmmgSZeshJNKm5HkhJVrVrb5N2br_6nxq5zcvutX_aHDu5hKIBe_plhr1sjmJzD9KDsTMzVSjbPanw8Y_P-poe0RRRj4S9ANI6lWToQsZAKxuaaVqhkYqEMslGjF-0qwORwWm-kSxzoNofbClvZsd_nSsnz9TO3q3XbRaeEeW9B35EK4wNSHIFCA536XCtD6cjeoraF-b7soVF-gN5YW8PffJYnbK72bNIEWL4HC7vprpdqL-PJHRja56I0phspS6jY_IXg1q370Uv3Yi-OH_WHYfDzIBM2ODOrGb7vh3pHjcC1w3EgglTK6b8ZyYPkFDS7NPFmhCzVNRcRfGEBUDZzO3wbmKgCkKEmLvvTGTlGh7_A-ijs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایشون هم اینطوری انتقام قتل حمیدرضا رجب‌زاده رو گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69834" target="_blank">📅 11:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69833">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48e95fc990.mp4?token=pZEl1hCq3UwpvNHQ-aaPH-x-3eXl0z3ssR_OzXphqpDeABReJCrN2J63Q4suUv5v0JuOD7UMf7Z0viIJqu_kKz27pthhDoH-4jtyML5PkQG1sR0TrfzyX8VovnXWntvey71eVC803XWr8aA6SBJIdaS2wI2l_3fzcE1nQ66YtOetVh2WDxPAHoxO-5yqTC3KZPoOpJOt5dystunHgHjQJJGqB2ocWmlCkuJpBwLyYcyTF9TunR5AENnmny_HoPEvQ5kCmQ8M3FqHC64hZnlzU5VkBshVbnxLUJ-V7_d4W6zQYXAF-4Bw0yZQ56ppIJusVQ9lI5wVt6oZrA75GBvlQw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48e95fc990.mp4?token=pZEl1hCq3UwpvNHQ-aaPH-x-3eXl0z3ssR_OzXphqpDeABReJCrN2J63Q4suUv5v0JuOD7UMf7Z0viIJqu_kKz27pthhDoH-4jtyML5PkQG1sR0TrfzyX8VovnXWntvey71eVC803XWr8aA6SBJIdaS2wI2l_3fzcE1nQ66YtOetVh2WDxPAHoxO-5yqTC3KZPoOpJOt5dystunHgHjQJJGqB2ocWmlCkuJpBwLyYcyTF9TunR5AENnmny_HoPEvQ5kCmQ8M3FqHC64hZnlzU5VkBshVbnxLUJ-V7_d4W6zQYXAF-4Bw0yZQ56ppIJusVQ9lI5wVt6oZrA75GBvlQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دریک، از بزرگترین خواننده‌های دنیا؛
با 140 میلیون فالور و ثروت 250 میلیون دلاری [50 هزار میلیاردی]
وقتی ممه‌های بزرگ یه دخترو دید، نتونست تحمل کنه و براش هاپ هاپ کرد
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69833" target="_blank">📅 11:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69831">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d3c25ee1.mp4?token=BiXl5mK5Iosdd6vfQzXn9ocgNsDH8Sb2-Dox6nQVE0m1KH3tqJrypqWWYmjfXvHZ0fC12kKsha0G_bDUJKwDLgYMlmTx9b1DYA5eQ0n8lvfqatcF7MxWvmX_ZBUsIVSVHcG2aKkL6eTz8E-azXtQPI_Irg45BipEEUWs4rt-LPpBCLl9LBOHVa3GpcEn__4cUCEUJ2to4ZCy5ViPwSkB-H_0V0MKjkns9fys7p_GitcjQHdh0FgYT0MK4eHmqWzXgG2KBtV2yP5NMCmBRpjySoT8owOZHYHbJ6tBm3ud07Di0qXXd7frUGNoPM0s1nrhfuHgIiR6gEWaDs7CiANkWLxYJCsMbmIxIXKHNJWgzksmmiJHDSrs6siG2D6RKVg9Zj9ELy2RVkU9eb46P86duBms0yBgiwdQVtk7Dh-wva8F-gLiCrHJ0yoU_71s53PYozHl13d2D648zajpo4o6UGGweDq47Qz6fJY3WCI-DamH1ZZweJI0hJTkukYjIkG1dAXuF1IcLOTO2F2eOTBeTkAsvvfVkXGKgrqTwW-4qHZ2D7Vufu7MTJJH53vKWZQIbI47CMJRvP7s-OxcCMLsshard7eWZC1ATf7Q48PrBMWYf-WMGmlJEBS77zV7uRqpRYTiBvemn5GPO8lBiH4F1xyFXv3JUNb-KB7qcCtxV7M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d3c25ee1.mp4?token=BiXl5mK5Iosdd6vfQzXn9ocgNsDH8Sb2-Dox6nQVE0m1KH3tqJrypqWWYmjfXvHZ0fC12kKsha0G_bDUJKwDLgYMlmTx9b1DYA5eQ0n8lvfqatcF7MxWvmX_ZBUsIVSVHcG2aKkL6eTz8E-azXtQPI_Irg45BipEEUWs4rt-LPpBCLl9LBOHVa3GpcEn__4cUCEUJ2to4ZCy5ViPwSkB-H_0V0MKjkns9fys7p_GitcjQHdh0FgYT0MK4eHmqWzXgG2KBtV2yP5NMCmBRpjySoT8owOZHYHbJ6tBm3ud07Di0qXXd7frUGNoPM0s1nrhfuHgIiR6gEWaDs7CiANkWLxYJCsMbmIxIXKHNJWgzksmmiJHDSrs6siG2D6RKVg9Zj9ELy2RVkU9eb46P86duBms0yBgiwdQVtk7Dh-wva8F-gLiCrHJ0yoU_71s53PYozHl13d2D648zajpo4o6UGGweDq47Qz6fJY3WCI-DamH1ZZweJI0hJTkukYjIkG1dAXuF1IcLOTO2F2eOTBeTkAsvvfVkXGKgrqTwW-4qHZ2D7Vufu7MTJJH53vKWZQIbI47CMJRvP7s-OxcCMLsshard7eWZC1ATf7Q48PrBMWYf-WMGmlJEBS77zV7uRqpRYTiBvemn5GPO8lBiH4F1xyFXv3JUNb-KB7qcCtxV7M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی شبانه به مجموعه‌ای از اهداف در سراسر روسیه و سرزمین‌های اشغالی حمله کردند.
پهپادها مرکز خرید گالاکتیکا در ماکی‌یوکا، که قبلاً مرکز منطقه‌ای بود و در سال ۲۰۱۴ توسط نیروهای روسی تصرف شده بود، را به آتش کشیدند.
آنها همچنین پالایشگاه نفت در نیژنکامسک، تاتارستان را هدف قرار دادند، در حالی که روسیه ادعا کرد ۱۵ پهپاد در نزدیکی مسکو سرنگون شده و عملیات فرودگاه را مختل کرده است.
طبق گزارش‌ها، حملات پهپادی باعث قطع گسترده برق در ملیتوپول، بردیانسک و دونتسک شده است، در حالی که انفجارها و آتش‌سوزی‌هایی در سواستوپول و کرچ گزارش شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69831" target="_blank">📅 10:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69830">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69830" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پیشنهاد_ویژه
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید بازی ساده و بسیار شیرینی که راحت میشه میشه ازش کلی پول درآورد
👌🏼
دنیای سرگرمی و بازی های جذاب رو در این‌اپلیکیشن تجربه کنید
⭐</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69830" target="_blank">📅 10:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69829">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=TLA6NXnF12n3lNN39ySlx1JBRWTav_fu-pmbqfSUwSc3ErYHRI-9GZeXovmi6k_hXjpWBoYDwW87OF-I09a6xZivHi_adINVh2a_JM0zrxmfw5PmSsJ1hhQEhYDAMUnkM2joakoUglkNt5jOqKYsf0WTb6tuu8xF2s8wwsKzJI9589Qm7y3X0FkL6BBvTLJZU1p03hsazsd5G-FaURoqZXRUyLWuivicbhOpyiVqWfmyERALwYge0qbKESKZvkMjbAvGfU2r-JvdXM71NHg2lEoRsxtdOM292Q-D4cdymoxu86Rl1yIkuzmgR36DbqjCmiEs2_k8AUagyMBNKojHWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=TLA6NXnF12n3lNN39ySlx1JBRWTav_fu-pmbqfSUwSc3ErYHRI-9GZeXovmi6k_hXjpWBoYDwW87OF-I09a6xZivHi_adINVh2a_JM0zrxmfw5PmSsJ1hhQEhYDAMUnkM2joakoUglkNt5jOqKYsf0WTb6tuu8xF2s8wwsKzJI9589Qm7y3X0FkL6BBvTLJZU1p03hsazsd5G-FaURoqZXRUyLWuivicbhOpyiVqWfmyERALwYge0qbKESKZvkMjbAvGfU2r-JvdXM71NHg2lEoRsxtdOM292Q-D4cdymoxu86Rl1yIkuzmgR36DbqjCmiEs2_k8AUagyMBNKojHWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖱
به راحتی کسب درامد کن
💵
💰
🟢
ویدیو
#آموزش
بازی chicky choice رو براتون گذاشتم خیلی راحت و بدون ریسک و میتونی بازی کنی و کلی پول دربیاری
🔥
💖
حتما ویدیو رو تا انتها ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
r19
@betinjabet</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69829" target="_blank">📅 10:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69827">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U065_ShXZTBb9d4R5fUTylTabJVA-l36oPsz2Me9jR7Kq3xI6Pc5Bg7JmXKqL-Qw2O4qkISgLaxdtdykvl87xE0RMN4wkHP6VeY7iS4xFmii20qZ6OjbAyuY1_h8NhRTs_9Ot5O4GGAbkICGCBjvu4GI08olicEtLiY6UC5WyOG5PuW2hRskwC8TVZbaiKXTxK986TnAnTz5Zt92L-1bHdfFSt6i9cFU66ecPUx7AIiFUIqSP9R78YOLYjuQisuDYn8-tU0KjRXvC1l7LJBUBjSL8mqX9PhfZBKDeH7wvlcG6ld00_RaLOQSZPtKFyGKK_3v2UQJOmNE4_M2wzVuPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
شرکت آمریکایی BlackSea از پرتاب یک پهپاد FPV از روی قایق بدون‌سرنشین GARC خود رونمایی کرد
؛
این شرکت اعلام کرده است که با استفاده از تجربیات به‌دست‌آمده از جنگ، استفاده از پهپادهای FPV هدایت‌شونده با فیبر نوری را پیشنهاد می‌کند.
محفظه‌های پرتاب این سامانه قادر به حمل پهپادهای FPV در اندازه‌های ۵، ۷ و ۱۰ اینچی هستند؛ پهپادهایی که از نمونه‌های FPV مورد استفاده فعلی روسیه و اوکراین کوچک‌ترند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69827" target="_blank">📅 10:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69826">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4c36a2172.mp4?token=rt3YpDjW1JYWdjy6fq16DUngc9WcHnC4WGXxfLbEBDmirqFbfxXgzEOUipqwod_OSRwGX6G2cY6zHRBPGEV1lMY715v4bMCQxsf-V7O-6Xcguo5z_7bmvzQQYaSIC6Av3LN56nYftm0zDfQ6Ybm7Q1cWmN0IMlR0A1yHj3IJLrsrh-Yd4ggOeASqm7rQ-gFMp8e7fvPR0DRV-JCQXXPDOPBrurNWbaJ2KXmTiGXH2HcZugKqhOlhkcO0CpjZCUG1eIw6TMUSeqzkv7rRGBbivjK3d8VubYgWSez5THc2ygdTFMWq4XXOFfuKyLIMLo6rzN6MaEuzZlQKXf2qSymqCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4c36a2172.mp4?token=rt3YpDjW1JYWdjy6fq16DUngc9WcHnC4WGXxfLbEBDmirqFbfxXgzEOUipqwod_OSRwGX6G2cY6zHRBPGEV1lMY715v4bMCQxsf-V7O-6Xcguo5z_7bmvzQQYaSIC6Av3LN56nYftm0zDfQ6Ybm7Q1cWmN0IMlR0A1yHj3IJLrsrh-Yd4ggOeASqm7rQ-gFMp8e7fvPR0DRV-JCQXXPDOPBrurNWbaJ2KXmTiGXH2HcZugKqhOlhkcO0CpjZCUG1eIw6TMUSeqzkv7rRGBbivjK3d8VubYgWSez5THc2ygdTFMWq4XXOFfuKyLIMLo6rzN6MaEuzZlQKXf2qSymqCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
جهانگیر، سخنگوی قوه قضائیه:
آخوند خرازی، بابت صحبتاش تحت تعقیب قرار گرفته و به دادگاه ویژه روحانیت احضار شده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69826" target="_blank">📅 10:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69825">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🟡
📰
مراد ویسی تحلیلگر ارشد اینترنشنال: «جنگ بزرگ در خاورمیانه، برای سرنگونی جمهوری اسلامی است.»
⏺
پرسش این نیست که کدام زودتر می‌رسد؛ پاسخ روشن است:
جمهوری اسلامی سرنگون شود، مردم ایران به یک حکومت عادی می‌رسند.
جمهوری اسلامی سرنگون شود، نیابتی‌ها خشک می‌شوند.
صدام رفت، یک کانون تهدید در خلیج فارس از بین رفت — کانون دوم هنوز باقی است.
خلیج فارس می‌شود منطقه‌ی صلح، ثبات و توسعه؛ چون امارات، قطر و عربستان دنبال توسعه‌اند و ما هم دنبال جبران خرابی‌های جمهوری اسلامی.
ثبات منطقه از تهران آغاز می‌شود، نه از میز مذاکره.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69825" target="_blank">📅 09:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69824">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdd241cc6.mp4?token=BoyeR1NH6AVpBcGdoxIznfdlLccQRPKPxMvAL8vcCBADOaEqeMf_i7OIQvlVTi9xfyG_VEMr7T6KBwsfeCFYdsK5jhaV5DpJYTpUNi93e2p441pSPK2N-kqZKOsyO5WiAyC_TlOr1-t5X-uKWpLVbVl8o2h3IxNuAjUB8KgDK3GsMIkVWyjeuErj1jBMhJthYJHsyz3UBdyw5KyzwOx1hyBtqZedYCwwdeFahlWIGTcfnZU9gvcqnsXskp-KMEczmiXXW9PQS_cbKlv9Naee5ShzQ5dq_HiRxfbsqrh66WQWvuuLYvaYM06YCh7XNHCiBJ5mk3LEA-o5ppfEiWKM6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdd241cc6.mp4?token=BoyeR1NH6AVpBcGdoxIznfdlLccQRPKPxMvAL8vcCBADOaEqeMf_i7OIQvlVTi9xfyG_VEMr7T6KBwsfeCFYdsK5jhaV5DpJYTpUNi93e2p441pSPK2N-kqZKOsyO5WiAyC_TlOr1-t5X-uKWpLVbVl8o2h3IxNuAjUB8KgDK3GsMIkVWyjeuErj1jBMhJthYJHsyz3UBdyw5KyzwOx1hyBtqZedYCwwdeFahlWIGTcfnZU9gvcqnsXskp-KMEczmiXXW9PQS_cbKlv9Naee5ShzQ5dq_HiRxfbsqrh66WQWvuuLYvaYM06YCh7XNHCiBJ5mk3LEA-o5ppfEiWKM6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یکی از نفس‌گیرترین ویدیو های منتشر شده از جنگ؛لحظه بمباران شریعتی تهران!
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69824" target="_blank">📅 09:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69823">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69823" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#بازی_پولساز
⚠️
🔥
بلک کارت جدید ترین بازی معروف جهانی هست که فقط کافیه یکمی باهوش باشی تا حریفات رو شکست بدی
👌🏼</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69823" target="_blank">📅 02:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69822">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6c003ee1.mp4?token=lcVtCtEJ4ySuYhVMcCfrltxG_ZFO7qQAdZvPjQh_pEbUZZo9dqn1JaJBaNY3Pufyt2ck7UMWuVulOsaG4h5cPnfvn90RLevRHJPl2r3NTmGgCdCnX3Y172Bs0d5xXqvwGTWYDEP4b5VxpCCLqZuP3Hwm4M5aq1lSyECEuYGnxJ-tZ_q-6HHxKZjWr6rNXrYTKdW6SkDXZQ5dPE2vKwxFLfGCam0z-dQUNDC5NQrH6YW6bh-9DllIWqdlnNenmMwQZxndh20wI5D5O1ilcucV_FBzs9ZhgTJiPQu5HjKqIwP8U3ag787i0VrK92E7EI-XXbjoN7ncsqEOopeKROp-Yoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6c003ee1.mp4?token=lcVtCtEJ4ySuYhVMcCfrltxG_ZFO7qQAdZvPjQh_pEbUZZo9dqn1JaJBaNY3Pufyt2ck7UMWuVulOsaG4h5cPnfvn90RLevRHJPl2r3NTmGgCdCnX3Y172Bs0d5xXqvwGTWYDEP4b5VxpCCLqZuP3Hwm4M5aq1lSyECEuYGnxJ-tZ_q-6HHxKZjWr6rNXrYTKdW6SkDXZQ5dPE2vKwxFLfGCam0z-dQUNDC5NQrH6YW6bh-9DllIWqdlnNenmMwQZxndh20wI5D5O1ilcucV_FBzs9ZhgTJiPQu5HjKqIwP8U3ag787i0VrK92E7EI-XXbjoN7ncsqEOopeKROp-Yoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😯
اگر هوشت بالاست
🗼
:
❌
👍
این ‌ویدیو‌ آموزشی رو‌ ببین و با ‌استفاده از هوش بالایی که داری پول در بیار.
🟢
بازی خیلی حرفه ای و‌
#پولساز
رو‌ از این ویدیو یاد بگیر
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
a18
@betinjabet</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69822" target="_blank">📅 02:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69821">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:  اگه ایران از این به بعد به هر کشتی‌ ای توی تنگه هرمز شلیک کنه، فرقی هم نداره با موشک، پهپاد، راکت یا هر سلاح دیگه‌ای باشه، آمریکا در جوابش یه پل یا نیروگاه برق ایران رو میزنه حتی اگه نزدیک تهران یا داخل خود تهران باشه.  @News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69821" target="_blank">📅 01:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69819">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBqORRXHNHOEkauLUjZN0fK6RdXyJy2_xK6__Tiahb4hLDNcqTfIO529MLNC5DZ_IaP1BnVAhixqicrXl_3HZGmeVb_HovMhW8Q33L61fTM97IwEWyVR1aABPY8QHoORVMXa2E6G8dFQjsUPFtg5n2cPF-osipo97hF-fYAv8fx2Vwwax6Td3CpQGa2xLpQiG26EOFjPX8zXTb-EOTyVzf7eg3XeyW1teFMtGbeuX-uCMmLhSxE6VWY1GcIGAH2lklXkvCq0kT8_9Rm7GrANEg3sZ_uNIOkOLdMq9Z4p6smZPWfNONWzSlPJKp1g8HUTDw0OoMeux1YLoelW7gWgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94eb35c039.mp4?token=lQjPAVqSb4leoIWmzhFF4jrAiSmAQAFJBI3r7naIhW6TEuH3ymOQRELgsCl3xDvfGc2j2_EnGhl6X5zDL1w62t7-Iorl6Y82KJu6CiOCIls47L9-fPRTS2y_9bXLR0_hZtLcdvDMSpkG16MzZyTTJLq7F3L2sfqPntIKNREJp7DGYmPi8aWYsLpTYI8HxqUCZ5I6s0uuarZpZmTDnueR-tT2AWilneQ_vTyraqaUoEvj21ApKd-_y_qpWf4xFIKBDyjUT3iD3XplMfJZzpK8mIUpu72rg_QHRJy7XTq8f3WGansWn6fSA7CCSpgGBkOrm8UksMJU92Rpaj9wnp7feA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94eb35c039.mp4?token=lQjPAVqSb4leoIWmzhFF4jrAiSmAQAFJBI3r7naIhW6TEuH3ymOQRELgsCl3xDvfGc2j2_EnGhl6X5zDL1w62t7-Iorl6Y82KJu6CiOCIls47L9-fPRTS2y_9bXLR0_hZtLcdvDMSpkG16MzZyTTJLq7F3L2sfqPntIKNREJp7DGYmPi8aWYsLpTYI8HxqUCZ5I6s0uuarZpZmTDnueR-tT2AWilneQ_vTyraqaUoEvj21ApKd-_y_qpWf4xFIKBDyjUT3iD3XplMfJZzpK8mIUpu72rg_QHRJy7XTq8f3WGansWn6fSA7CCSpgGBkOrm8UksMJU92Rpaj9wnp7feA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇨🇳
🇸🇦
یک پهباد ساخت چین متعلق به نیروی هوایی عربستان سعودی در آسمان جنوب کشور سرنگون شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69819" target="_blank">📅 01:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69818">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtsqqLQb7rdfNB0dKWC76DNtuh_vrrGDskAmBdb-IQ0MOtHvDruiUJGoqBke09xoCtTkDjuO4Ua5TRJK11vNFRPsy7vw3hLfWm9qiFDJfi4OV979SUrT6FXP5LMyluKQa1lo0t8ZK_-FOx2kfSIwAyqFDo7BtOhc7E75TJZnSfEm1RDcbTX9DweqcZ7YDV7J-yHZyKBeJQcu8cj_z53OhMj0nu_sKsUb1bLGzqSa2O5qWibBdhcoF2ikbGDqvpS69k08xWXb8aojemyE7N8f7qenG4SdDGYVcqjsjmKlgbVsSyS8osQpyENZHLB0dMZkZDLYRAOhXoyA9dtAcJihJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در تروث سوشال:
51سال رفتار نامناسب!
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69818" target="_blank">📅 00:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69817">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dbf391292.mp4?token=HEbB9CSdCwr8doMqf_oP0os0R2wrIIlchkS3qzhGaqf4kwetONzfh0J41RU-NH54O9F5mkzLTAidguox4-wPTtajgxzjmQIEQx5uZhf9WOLZD0fXY8qBiQeSZ0vVE8iwdIbol9NNAYezH6Abxm1nruX9hnfz8_bhlVFQTA1YBUqvGDJXToYXib-kLvnDkagkkaqcpjr9Sb-6UHC_EA2IaW7Xz7Q7wQW9Vw-WnVJoxr5kwPGz_HTCuAjQRKCZaPmWjBk465kBS6mX4MJVbYja5ZuwkulVH87-GQ6bUYamx-ntcj2X7r7M3CbwwJK7C6KPHM-34BUw0hB3TIbpgyjLNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dbf391292.mp4?token=HEbB9CSdCwr8doMqf_oP0os0R2wrIIlchkS3qzhGaqf4kwetONzfh0J41RU-NH54O9F5mkzLTAidguox4-wPTtajgxzjmQIEQx5uZhf9WOLZD0fXY8qBiQeSZ0vVE8iwdIbol9NNAYezH6Abxm1nruX9hnfz8_bhlVFQTA1YBUqvGDJXToYXib-kLvnDkagkkaqcpjr9Sb-6UHC_EA2IaW7Xz7Q7wQW9Vw-WnVJoxr5kwPGz_HTCuAjQRKCZaPmWjBk465kBS6mX4MJVbYja5ZuwkulVH87-GQ6bUYamx-ntcj2X7r7M3CbwwJK7C6KPHM-34BUw0hB3TIbpgyjLNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
آتش‌سوزی یک کشتی در پی حمله سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69817" target="_blank">📅 00:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69816">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🇮🇷
سپاه‌پاسدارن یک کشتی را در تنگه هرمز هدف حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69816" target="_blank">📅 00:45 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
