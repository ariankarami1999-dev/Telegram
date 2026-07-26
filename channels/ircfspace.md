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
<img src="https://cdn1.telesco.pe/file/TBuCxWdGCkXNcoFmkW-hDAMDTQ5WKrhh2ivERe4QjSekQFrXJ6-OJm2fBVQtwRyrEMyy40MGj03Pxa0NdtgEvjtbKEQu2Z-w5AGKCvtmj7ViqhqqZ0sL6o50MWKvgQdY7t5w7LA9f1SvEwrATyHPjZC-QDqLQsdgj2jDBG1SgQz4Xu4NAkuBkYkh-9xQJC9ZvMoKea0zLLbpv5qqZG11sFToVfSiNhag9B_3mlAiAB06D6Oa6NJxN-KdKAzVhB1t3nwOO-HMUfDqf8ztkutDCLnv04YRGA0A4Mk4v53IufVr2ggkpGO3fTllrWI69m1bbsuybkbh3rM5zomgqnV93Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 97.7K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 00:54:15</div>
<hr>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P5fwr29Erpu_u8yHJRE3GF2U4kgkVzMAJ1DW-VkrG534FGfKtCefN1wwphC4tbK-sBXatnI5G1Xz028zQ6ZP-FxduL_7WDbIQnjxbI6W0Eq5sgHFH3pPg4U4_iG1vgo2P--MwPxWkyyDa0HitTpLqkMREQf2o6t1P0c2VWpLz5YxdPJRfbzqg7fYLF2br-ZQfpNAoRYDz3AGi0HdIV6GZAo8M1_eQH9isC4ljzgmNJxZCrWYEgRANMpbaF9QSjIbRybFxHKbd0C9yF4T-I0gP4Dam1TVCJzo2l9Ll2hONpF5IK7e_P4rzVicg5nGOtPX8_edWoQuyMz1-ElYIpaTCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه‌ترین نمودار ترافیک اینترنت ایران بعد از ۲ دوره قطع اینترنت، نشون میده ترافیک هنوز به حالت قبل برنگشته.
الان دیدم یه نفر یادآوری کرده "۴۰+ هزار نفر دیگه نیستن که به اینترنت وصل بشن"!
#دی_ماه_خونین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WhQRHxIpqGAdMFyIssWWXjzBy5Yzn-OS5PA6qtaCD9aazOUn3uulbxOj8rLfs7KiYhIctkzSHGylvQvadJxkaGPvGHBlj287_hoOSt9I1MJL28dnbjY92QkY2G_ILcU_2QzmBwpFcBhQqVmp6RH3s_JxEYsY5IXvsyuo69k2Levh1-hechTM2UQ__m5eqmHqLOZecYtGSIc8ejco1QVKXGKGW1Oi6lJckChEffLeItBiueBMrRPja2_8ES_QBCymYYQIYQEaorYtcS3WTymoR8cNEoPbQbWT6sm6p7NikKiR9nFD7WNeLyY8dxjt2xqPmrTYprK4wD-2VHBpIs3GHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته "سایت‌های ارتباطی در خاموشی‌های بیشتر از ۲ ساعت قطع میشن و راهی برای تامین انرژیشون نداریم".
یعنی از هر زاویه به این مرد و عملکرد درخشانش نگاه می‌کنیم، حل مشکلات و امیدواری به آینده فوران میزنه!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XW5UEp_ud7XhGMANQXFJfbaQcUtb8StLxw1G2QemyFQ9QSrI4Fj_WZnFjHAjYq5V-_O71A1Fw_IyR22ipDYS4GqHV3iL11wfuhWQW7jpblqzP8r1HgE65heFCPfc_hjOghLpGmmf18pi41WXA7aa0xCTMIPvV4XmNUkvDZfEbT4uDFRzlMmKg4WtUgd9w8FpbAZ6fabHtechCFK2MD2IGHPFs1yPVo5lLFNWLZ_-qmK8oBqoYlBJ2ASgVd5AGUaq5UH93AaFi4APmwOot-rCbYWnqYccvM6L1ufQ5C7aZzZkWiaKUMiuMHDlasQvVu2dvDTfVTNslj8EPHOoU-KysA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی هسته ایکس‌ری از نسخه ۲۶.۱.۲۳ به بعد یه سری هشدار برای قابلیت‌های منسوخ‌شده اضافه شده، که شامل allowInsecure و Shadowsocks، VMess، Trojan و VLESS بدون Flow میشن. مثلاً برای Shadowsocks این پیام در لاگ نمایش داده میشه:
"The feature Shadowsocks (with no Forward Secrecy, etc.) is deprecated, not recommended for using and might be removed. Please migrate to VLESS Encryption as soon as possible".
اگر در حال ساخت یا انتشار کانفیگ‌های مبتنی بر Xray هستین، بهتره به جایگزین‌های پیشنهادی مثل VLESS Encryption مهاجرت کنین، تا بعداً با حذفش به مشکل نخورین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j7adO8dloAAcpZ6Mz0HIIpk4aEWlbNiPV1LrrKBmYCYxBkcjU-AWjFoTzP239xe8oGA9hJK0nfEMSLmx64wg0PMAkb1wEjNsz0i0--Q6WwRiPTIiSzAcgk-7z0v95s3HgtE6sMpIZ5VoHmAY1eQtaO-Ak0Ra8shGZ-mGesAaKzTCW4MGxDcTqH_dMDHUrDhu3iMBTSjyYit241FFxYrkPLOGpiddKA8wjhmCtuQLHBHqZbnN9uvIoEiJQf36_ZS4ooDIfx65eBC4S3aWVZDP05YBQ1XnbYqfe7lYyNnXgLx8N3hq1uNj0zh_eCqM2Apz3Kk9M5V1UBjSKxViyqaj7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت دسکتاپ v2rayN یک بروزرسانی امنیتی اضطراری منتشر کرده و از همه کاربرا خواسته هرچه سریع‌تر برنامه رو بروزرسانی کنن. این هشدار در چند ریلیز اخیر هم تکرار شده و توسعه‌دهندگان تأکید کردن که نسخه‌های قدیمی حتماً به آخرین نسخه ارتقا پیدا کنن.
در توضیحات این بروزرسانی اومده که "یک آسیب‌پذیری امنیتی بحرانی در دانلودر داخلی نسخه‌های قدیمی برطرف شده، که می‌تونست به مهاجم اجازه بده فایل دانلودی رو در مسیر انتقال دستکاری کرده و به جای فایل اصلی، فایل مخرب رو بهشون تحویل بده".
👉
github.com/2dust/v2rayN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oUFIGBb7dyKO0JLv0vtNN8X1CS4uOSSRde9meq_IT-aBOrY8DbKtSU4XpgsQ1B0MNVQkSy1s5zLklBqAXLYNSKd7wqQKTaSUZaSmxUPA60BfHbeeJxtH19cRGecVhmxBXi-id5V4esyXKe_OnkAzglguJ0SsvwezBSBTaj_IYcyIySfdCHiuHJI47XDCkc5ILuyhTZhFWWI4rbYzImjZGB31DC7Exs5otyz_c_gvTRZAH7SiJ_LxuELpf8LJXukL-FgZ_t6adc-OfD_ak4AZ5tgKEZTYapEnORepUPOFdqBm7pmHw3-3hu6OosKbdb2CYAN2pWxHRS8Ts79dALOH-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bwlC5PgaJe4yCdN0VqStxSf_TLDyDSAVKNac8UtiM_2xY-XqHSGCk5ZSBHJlDRG5cX3pk0MkOWvOWHCSdWsukcB_1kWi-Ueu8MmysnZVYaNIxOMrEfjVydur6yC3BkTwopohnVzc7ON8PLP1boemOtK7oPgexh73U1gXnQ41_3l_txd3JkAP6BUgPqu3q7x_BR3fU90DAeJS_x3uUU_pkd6bGXKgRC6HbASFADjqjlGmgztm7bw-c0DNGBFHyL4Q46AZW8z_adEBmuwiuoZt_AWd55rZts5l-M2pgYIjYjOZWap9tYu_60BHOaB5lUl2emPye9rGoLxiEOWkFy7y7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vvr6gHCjhih5K3Ppv7pl0l6-q4wPhOk3yfL0M0KLAfwvagj8ppzdd5WYw_cCKuIuFguonP3siOWN7etUpT8PFUvX6xWyuuQ8NHtie6Epb0TjwLlGu3dKohpanQkVlPtmrf58JotK0BY-U79VAaBNzR0jviNdub3kQG3KitJDdwlxOwHZvMCwQTHiT_ljlzcyM6aXL1qmwtPCFa0uckZuo1ehpcpPs6lJ0N2Lj9UDE8cwyY2Apvvy2dZFHAv81kWOOi2lZ7ZU26A0q7AoE8g1ihy2ICeDUu11FF8Ku6sjxWduU-Q1oFIozGoH3t_r8JtZqYAe5NeSdoVqa2_5f3EuMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن تجارت الکترونیک ایران یه بیانیه داده و نسبت به تعلیق دامنه فوتبال ۳۶۰ در رجیستری ‎.ir اعتراض کرده.
اصل بیانیه قابل دفاعه، اما امیدوارم برای کسب‌وکارهای کوچکتر، استارتاپ‌های کمتر شناخته‌شده یا پروژه‌هایی که بدون پشتوانه رسانه‌ای قوی دچار مسدودی دامنه یا محدودیت میشن هم کوپن بسوزونن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2512" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ساترا گفته نقشی در فیلتر شدن فوتبال ۳۶۰ نداشته و قوه قضاییه اعلام کرد مسدود شدن این سایت ارتباطی باهاشون نداره.
وزارت قطع‌ارتباطات هم طبق معمول نقشش فراتر از هویج و سیب‌زمینی نبوده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2511" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2510">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mnBgZ72R1SsmahCa3KwQJRI4FlZC-70InFO6WkW8JT4z8hcvOtFF6EvPkM-4WL_rJZ6t8cWeA7wjp-_zb_yXKFZXQTozPao7CcFg5j0_O9byRdRMBo0He1mjkz-GGPfIC_Ms2vVWAGTtjqLs4VNDjKUuU9GjSjc41e3ZvMc2qxwIIs_-HYlBjz9L8JVAhhY1jEs9bTuzFt1uYK9bB_47l5_1C7oFOthrXWvRp4PEPcnU_owXnkBV_mM2beYvLLbW2wDHVJw2MlQcNVFHXfw4FUqOkF2oMqRKdNUY9wey5ED9Z6BsEFpXJm20zkOhTENpbjHFAVrRmuWSACpVN250jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ ShineNET VPN یک فیلترشکن رایگان و متن‌باز برای اندروید هست، که از امکان انتخاب هوشمند سرور بر پایه هسته‌های Xray و Aether برای دورزدن محدودیت‌ها استفاده می‌کنه.
👉
github.com/shayanheidari01/ShineNETVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N_Ca7l30P3SM-PsjDVweVSHFUVPyO_VhOC2iRNvsQlwjUY7fs97vHO9zeLsrlvisRXquyywz-rZVXBVgRSGbXmdFMmFPgBCH4vislL9WS5X3g0F3M2A566rTTc-uGwvh7tQSAg0X7asFKiWAmoCjL4Kk4Ex3cfxgj2FoMrmGxALhE21hUk5WP5wxxVKYAynDYXfg1CZA7GrR2q-lfrGGrZsLhlDdavDZYd7wjVLljAWqmW9OoX00CE7UJz13344B0Z6M10MMlDoSyDsO8ufgcv1pWE9r06T4SR-PZpU1PJGvvKkRvz0VTMVwvtX02A-is51ymQWZxfQw2Ho_DVDe4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فوتبال ۳۶۰ عادل فردوسی‌پور توسط قوه عاقله فیلتر و دیشب چند دقیقه قبل از شروع برنامه زنده از دسترس خارج شد.
هنوز علتش بطور رسمی اعلام نشده، اما این اتفاق پس از درخواست سرمربی پرافتخار(!) تیم فوتبال جمهوری اسلامی برای برخورد با این برنامه و یک روز پس از جوابیه به امیر قلعه‌نویی صورت گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/ircfspace/2509" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DK2MiGqNvIdoF1SgcqWEWQ_pjrIV2nm8MdXz1v8t7U7i9suOXNW8PUqBxx8nbRr0G1Wi60aFjS3Ns37DE6k5TVPViDKpd5KUhjZDUIA6w8mWMLW1rVwg6SmQceDRPHAqYEkt8IXlEurpsmzFqqW4zuUd94inrLGYb6jNcFjGJbPgAgN5YUy4CUvKFQERLr-cz9nDcCq_OXVkqYj2DrADAhpktAzdS5pwcasev1i7_NuW6Pq5tqT5z-AM42kF1Ey4LAk4Ru0cAPqbIp8dvrUZc9reFhWy9grlpk49ArklAXrQjqY3XxQ6MGJHv-XsaGjSEU7SXi5CJMKl-3PUaj4L0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن Aethery برای اندروید یکساعت قبل به ورژن جدید از هسته Aether بروزرسانی کرده. اپ Aether-GUI برای ویندوز هم کمی عقب‌تره و ۳ روز قبل بروزرسانی کردنش؛ البته احتمالا بزودی براش آپدیت جدیدی ارائه میدن.
👉
github.com/ZethRise/Aethery/releases
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2508" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2507">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qv8s5iJOvbQom-wedEpdBJUU6EOeF8FCbV9LHf4kws-ShF44SNDb2coUyvK48LAmA-ebhOm4QvcMaZSTlbxEcqKHbqJ7SABKfyAp_cuC9UuRGP2zMaEz7CJo0c2RggPespN5440eeGmUGfylkr2SHZQ8HA93s4GFXYgB9U4L5LwrG545zKhXwmoswminB3EOnwDefGQRukN3zoKpK_SyCHcATDCTKUmqO94QOLrB0nsq6qmQ5bcz5AaIjSz9f5tbG0XO8BFZVZk8AyFy7p623KJToLVKIxi-r_IukMl4h0_GafHSqNO4Bj_4Y8cRYjnGP5YVjMBpIKENERl88JGxJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱.۳ از پروژه متن‌باز و رایگان Aether منتشر شده و مهمترین تغییرش اضافه شدن حالت اسکن Ironclad هست. برخلاف حالت‌های قبلی که فقط بررسی می‌کردن یک اندپوینت در دسترسه یا نه، این حالت قبل از اینکه به یه سرور اعتماد کنه، یک تانل واقعی برقرار می‌کنه و یک درخواست HTTP از داخل اون عبور میده تا مطمئن بشه اتصال کار می‌کنه. البته این روش زمان بیشتری می‌بره، اما در عوض احتمال وصل شدن به اندپوینت‌های خراب یا ناپایدار رو تا حد زیادی از بین می‌بره.
توی این آپدیت روند اتصال مجدد هم هوشمندتر شده؛ اگر ارتباط MASQUE یا WireGuard قطع بشه، Aether دیگه برای دور زدن فیلترینگ مستقیم سراغ اسکن کامل همه اندپوینت‌ها نمیره. اول همون اندپوینتی که چند لحظه قبل روی اون متصل بوده رو دوباره امتحان می‌کنه و فقط اگر از دسترس خارج شده باشه، اسکن جدید رو شروع می‌کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/ircfspace/2507" target="_blank">📅 16:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2506">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پژوهشگران امنیتی Insikt Group وابسته به Recorded Future از شناسایی یک کارزار جاسوسی جدید خبر داده‌اند که با استفاده از بدافزار MarkiRAT، کاربران ایرانی را هدف قرار می‌دهد. این عملیات به گروهی با شناسه TAG-182 نسبت داده شده و طبق ارزیابی پژوهشگران، ایرانیان داخل کشور، مخالفان جمهوری اسلامی و فعالان مدنی مرتبط با جنبش‌های ضدحکومتی مقیم اروپا و آمریکای شمالی از اهداف اصلی آن هستند.
مهاجمان برای توزیع بدافزار، نسخه‌های آلوده برنامه‌هایی را منتشر کرده‌اند که برای کاربران ایرانی کاربردی یا جذاب به نظر می‌رسند. از جمله آنها می‌توان به فیلترشکن Pis2ray VPN، نسخه‌ای جعلی از Star VPN، برنامه‌های YESHICA، YEPlayer و YEMPlayer و همچنین یک وب‌سایت جعلی با هویت Starlink اشاره کرد.
بدافزار مذکور پس از اجرا می‌تواند اطلاعات سیستم، فایل‌ها و داده‌های مرورگر را جمع‌آوری کند، اسکرین‌شات بگیرد، دستورات مهاجم را اجرا کرده و ارتباط خود را با سرور فرماندهی و کنترل (C2) حفظ کند. پژوهشگران همچنین زیرساخت‌های جدیدی را شناسایی کرده‌اند که نشان می‌دهد این کارزار همچنان فعال است و احتمال ادامه فعالیت آن وجود دارد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/ircfspace/2506" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2505">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مدیرعامل شرکت آسیاتک با رد شایعات منتشرشده درباره کاهش ظرفیت دیتاسنترها و احتمال قطع اینترنت، اعلام کرد: تاکنون هیچ‌گونه اعلامی در این زمینه به آسیاتک ارائه نشده و خدمات ارتباطی و دیتاسنتری این شرکت مطابق روال معمول در حال ارائه است. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2505" target="_blank">📅 19:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2504">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گزارش‌های زیادی از کاربران در ۴۸ ساعت اخیر در رابطه با کاهش پهنای باند، اختلال یا کندی اینترنت تلفن همراه در مناطق مختلف کشور وجود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2504" target="_blank">📅 19:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2503">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pg0kA5Uqu23uzrSHzGD-4A1R0wG5OEJf090I4gkHNYwIOW8T7HHxI0CtirgDmu1RhSL6Gtw5aPX1oSqqCImVDvFbEsuiqyQCPRV4l07P3sluodDS_wM0x-m2Q9C1uYyfTC_frD58_sJWdOCtl1g-jNAvPTWYK2Fehug5Ss8cq7JPgBDKFDSnzdehTeftbefJMxQX0RNX94GeipNKQK4bqUO26PpeN_ZjoFMX5a16tTkacoVxJK_sFgMdbFNvZyZaLIOHxKOpLTBnlYO8d7gWrGoylJZCPhTndpPeN-VP_uFymMm6cXbi8p3GDqRgYvcZCMAzprbusHyXGZsykkLpZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران امنیتی از شناسایی یک زنجیره آسیب‌پذیری جدید با نام wp2shell در هسته وردپرس خبر دادن، که می‌تونه به مهاجمان اجازه بده بدون نیاز به احراز هویت و حتی بدون نصب هیچ افزونه‌ای، کد دلخواهشون رو روی سرور اجرا کنن.
بدلیل شدت این آسیب‌پذیری، جزئیات فنی و کد اکسپلویت فعلاً منتشر نشده تا مدیران سایت‌ها فرصت کافی برای بروزرسانی داشته باشن. این مشکل در نسخه ۷.۰.۲ وردپرس برطرف شده و برای بسیاری از سایت‌ها بصورت خودکار در دسترس قرار گرفته.
©
slcyber
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2503" target="_blank">📅 18:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2502">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بیش از ۱۱۶ دکل مخابراتی استان هرمزگان در پی حمله آمریکا دچار اختلال جدی شده و خدمات تلفن و اینترنت ثابت و همراه در شمال بندرعباس و بخش‌هایی از استان با قطعی مواجه است. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2502" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2501">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">زهرا مرادی، مدیر اجرایی سامانه پیشگیری از خودکشی طعم گیلاس: در روزهای قطع و اختلال شدید اینترنت، روانه حدود ۷۰۰ فرد بحران‌زده که به کمک فوری نیاز داشتند، امکان برقراری ارتباط با سامانه را از دست دادند. برای تصمیم‌گیران، شاید اینترنت تنها فشردن یک دکمه باشد، اما برای سامانه‌ای مانند ما، این شبکه تنها پل ارتباطی با انسان‌های ناامید است. قطع کردن اینترنت، فاصله میان زندگی و مرگ را کوتاه‌تر می‌کند. وقتی شبکه قطع می‌شود، افراد آسیب‌پذیر دیگر نه تریبونی برای شنیده شدن دارند و نه راهی برای دریافت کمک‌های حیاتی. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/ircfspace/2501" target="_blank">📅 08:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2500">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FuyiKJkd9XHhVLrGcWZBSxx9Y0T3KSKOhn5lZuXekt1XVc61B9rCA5Zg0ycWCTnbGqC6CXqI0qGBrQCSUGO_eHM9DCdnowaioCmC1FPyrbc4DO0X_ZKwjKUFlfc9fm0DQeRz36SnYydIVxnzcgnbelacmR6sMaSYq3t_h2YwcVp5uM7BTegixCmsDt9Rz1DjAqubHKQIw-4BFYfXKvN85q394E_9oKt7x5IOrd9dwTsxEvmsc3SspWx5W18du7gy4IRzroCtBxLZF47k3O623L-2tmSYkS4TFpUdfBu0aQjf8CtjdlVZc9lyWIXGvrBzr3OlZ0jVgzwElNjSEUwYJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگرچه قضیه ترند شدن "لغو عضویت جانفدا" در نتایج گوگل بزرگنمایی شده، اما یه نقل‌قولی هست که میگه "وقتی دیکتاتورها در حال سقوط هستند، فقط دو گروه کنارشان می‌مانند: هم‌پیمانانشان و احمق‌ها".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2500" target="_blank">📅 07:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2499">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gdFohYz2fsLhXHc8Q24Yty_-E5xfCuKG69I4pZdm1TvCmNgS-e2cMzWMMCpcJnISVoLpuhOR8bFRYo0ENISQnYS1l5uXcv7si6X7gITMPNTlocBFPVUkWf2Ie0ST8ZAhbl_DnRtRGO_Wz897mQZOfmrhdyP_8awGSC4WGsbSvuMOuipcCO7CY7HnfCeN9Fqr6g3aEwbOgQSqjoCQDC8ZZJIJgl9gU2WSBiRyQCwbNIs0J6dmEvERzVpYAzhp0v4FyfS_xt1dxIS938ckfztzlaUpxD6vg4hW23SMiRApXNPtCNz5wyMiZj88o_Ouzt6TZ80SH698VMaE_Kw0dErojA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ dicodePing یه کلاینت متن‌باز و رایگان برای اندروید و ویندوزه، که مدیریت و اتصال به کانفیگ‌های مبتنی بر ایکس‌ری رو راحت‌تر می‌کنه. این برنامه از مدیریت سابسکریپشن‌ها پشتیبانی می‌کنه، می‌تونه بصورت خودکار بهترین سرور رو بر اساس latency، jitter و سلامت اتصال انتخاب کنه، از حالت TUN/VPN پشتیبانی می‌کنه، آمار لحظه‌ای اتصال رو نمایش میده و امکان تعریف دامنه‌ها و برنامه‌های خارج از تانل رو هم در اختیارتون قرار میده.
👉
github.com/mcodersir/dicodePing/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2499" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2498">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پژوهشگران دانشگاه میشیگان، دانشگاه نیومکزیکو و مؤسسه فناوری دهلی، ۲۸۱ وی‌پی‌ان رایگان اندرویدی با بیش از ۲.۴ میلیارد نصب رو بررسی کردن و به این نتیجه رسیدن که بخش زیادی از این برنامه‌ها برخلاف ادعاهاشون، امنیت و حریم خصوصی کاربران رو به‌خوبی حفظ نمی‌کنن. توی این بررسی مشخص شد ۶۱ اپلیکیشن بخشی از اطلاعات رو بدون رمزنگاری ارسال می‌کنن، ۲۹ مورد دچار نشت ترافیک یا DNS هستن و بیش از ۸۰ درصدشون هم با سرویس‌های تبلیغاتی و رهگیری در ارتباطن. علاوه بر این، خیلی از اونها هنوز از تنظیمات امنیتی ضعیف یا روش‌های رمزنگاری قدیمی استفاده می‌کنن.
اما نگران‌کننده‌ترین بخش گزارش مربوط به ۵ وی‌پی‌ان بود که فایل تنظیمات اتصال رو از طریق HTTP و بدون رمزنگاری دریافت می‌کردن. این ضعف میتونه به مهاجمی که روی یک شبکه عمومی مثل Wi-Fi رایگان حضور داره اجازه بده تا اتصال VPN رو به سرور خودش هدایت کنه و تمام ترافیک کاربر رو بدون اینکه متوجه بشه زیر نظر بگیره. به گفته پژوهشگران، ۲ مورد از این برنامه‌ها این مشکل رو برطرف کردن، اما BambooVPN، Free VPN و 101 VPN همچنان در برابر این حمله آسیب‌پذیرن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/ircfspace/2498" target="_blank">📅 17:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2497">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X34qTzFdKr5WwOZSfPdDtfT0w4x1-cQFZeM8PAX8SbXa2c5E754-dMGQ7IU3OkUQz_QLVNvZgMWDVCwLCYkMKAVBaGtfRnMpK7PSBsxU2olbtuGeNU1Pf39cxLYrX8NOjo2QDsncx18zmrSN3kkxs2VvZyc5GIvRl-JuZ1YdKT_dOtWyl-3CJ1Zef1Y_3g6A_f9F_50F7SREungv-E0XC-tsSzf9MYxzLTiIRafFljFeg7-RqVC3A1kcoz3wA0-vIwnR4a9l01hQDGbblbhkXrdUzDsEE_ohptg3Egygz9eMNr0RBYJaEVKD1Q8ePLmS4mR_SbJBH4zBMdK6-ghFXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aethery یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که بر پایه هسته Aether ارائه شده.
👉
github.com/ZethRise/Aethery/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/ircfspace/2497" target="_blank">📅 16:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2496">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mgzaP8cRShDu9TT6Gy4O0EK7kac9J0pI867r89PXGphannTXzVJwIiG886GFwKmDJuu74naiWnv5hg95xBuFnParOFt1jGJS5Z5YMKUQvqNpvicQx0zrck-l5xmxjbFLPiNFAhnsqIkC-sJsTrC0HmScjvePmRZf0NAG9SxtmtsuWfWcu_W1wwQXrLiTM4t1yBOT9W7fJllpRng4oRCjRMvyUWgTFtUMGopaboKy6W_732Y50SL1Jb6e2NrZpfJzvCGhtDzFTOWaxp2PU-yL7am5zQZSxtfJayNgVTw3WDMDdBm1vVDXyAxoVlmxWZxBg-Mama9L_V38lTy7vnd7sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت رسمی Sing-box برای سیستم‌عامل ویندوز بصورت پیش‌ازانتشار عرضه شده و طبق اعلام توسعه‌دهنده‌ش، همون تجربه‌ای رو ارائه میده که پیش‌تر در نسخه macOS در دسترس بود.
👉
github.com/SagerNet/sing-box/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2496" target="_blank">📅 08:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2495">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RaUn5Tdw5vYc1qR_MmD0Su11_CgCusooyIhOuNqoLpuve71oPhw-sShSZRZpTVFM6ZB_y2aBcpDRhpgvCrn2HLuWwlRsHghssgbGyU7kE4lFkVAY6CgTHyiWRim3sHqDxo6ul66vs5DqjMvy1eAtTsPsUECOW_c4ut3_R8XVvV6BkR9Xw-I4IDmZ0cy-RIsbpPh9KjYhp-JcN1S6dRvKWRZpOLnRPW3TKYpZiqFi2MqYpq0ZokeXFvEspFvPuaWahz_dwsZRPk7BMc2XIb8JhR8lyaUdrG8XVaB8hYC3uj7M1aegGcCgx_UNhwOHn_TyaT35elsvU3lXqRv0lORWag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aether-GUI یه واسط گرافیکی برای هسته Aether جهت دسترسی به اینترنت آزاد و دور زدن فیلترینگ هست، که دردسر سر و کله زدن با محیط ترمینال رو برای کاربران سیستم‌عامل ویندوز حذف میکنه.
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2495" target="_blank">📅 08:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2494">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Week3rgkjS7Rg7PBLF2D69VtnPzH3O-8ZdCvy11ScTR9APHfJTyZqpi1d9biKpCJDG1LnLe16MiuKYoRrMtSwYP6SNn3l-lRRWHNuW0rJ_UkjldGZfGLpth6ccBjxZXoNciLSd9uwyA_pRpg4CZlYfkvSkpi7MRVyQqoDcD7pq-vcoYs0FInnx7v_hC4tyCl0hEBqHkmaHNjeYz0TMjZNblM9_W-L56LIu38oN9CxecL8G1-QE65_YF89IdxLmGO_hgvtZO8d7KypG5V40bhAectVRw6c6SG96ZqhV5nsCyNqXMvKD3Zl0bGN5zavLsLoRKpOE8p52QmLqEHgXiV8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت در بروزرسانی امنیتی جولای، بزرگترین بسته اصلاحات امنیتی تاریخ خودش رو منتشر کرد؛ بسته‌ای که ۶۲۲ آسیب‌پذیری منحصربه‌فرد رو در Windows، Office، SharePoint، SQL Server، Exchange، Defender و سایر محصولات این شرکت برطرف می‌کنه.
اهمیت این بروزرسانی صرفاً در تعداد خیره‌کننده آسیب‌پذیری‌ها نیست؛ دست‌کم دو Zero-Day Vulnerability پیش از انتشار Patchها، عملاً در حملات سایبری مورد Exploit قرار گرفته بودن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/ircfspace/2494" target="_blank">📅 07:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2493">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jkjFOa0iGWjp7LPPjaeEfyDe4jcSA0eXpV6tedkKo3L2oUh4gzuGnPSLzQltUvgBiAaB2pnyEnRuJ0M3iYLH9iQlg-COOPx5ukFSRVgdoVxgiesir_sNs4nEgfeZV1cNVNLvX1tKpHp2OCMaLyhmfS4Sl4eBEjAQCf2XS0MfG03z4mwK2o5Wz2IXnmMtTIgBBB0vX43x5dJYcX7XZb1bi8P0UrauhpT7xB3mgzcdWAu7rJf1Jw_RkLXi4MiSR0GpZoyfPgvqTMdZlrrYB8XL75gXQUAsFxINTQSIyH3QF-0pC0WcpcEBPZ_n16OlvPAEesZ094YuL8-u17-3RiMd5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه Aether یک ابزار متن‌باز و رایگان برای دسترسی به اینترنت آزاد و عبور از محدودیت‌های شبکه هست، که با تمرکز روی سرعت، پایداری و مقاومت در برابر فیلترینگ توسعه داده شده. این پروژه با ترکیب وایرگارد، MASQUE و WARP-in-WARP، ترافیک رو تا حد زیادی شبیه ارتباطات عادی نشون میده و به همین دلیل روی شبکه‌هایی که از DPI و روش‌های پیشرفته فیلترینگ استفاده می‌کنن میتونه عملکرد خوبی داشته باشه.
یکی از قابلیت‌های کاربردی Aether اینه که خودش بصورت خودکار اندپوینت‌های تمیز رو اسکن و بهترین گزینه رو انتخاب می‌کنه؛ بنابراین نیازی نیست که تنظیمات رو بصورت دستی انجام بدین. بطور پیشفرض هم از HTTP/3 استفاده می‌کنه، اما اگر شبکه‌ای QUIC یا HTTP/3 رو محدود کرده باشن، میتونه اون رو روی HTTP/2 قرار بده تا سازگاری بیشتری داشته باشه.
این پروژه روی ویندوز، لینوکس، مک و اندروید (از طریق Termux) قابل استفاده هست و توسعه‌دهنده‌ش اعلام کرده که بزودی قصد داره هسته Aether رو با زدن Pull Request در فیلترشکن‌های ابلیویون و دیفیکس ادغام کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2493" target="_blank">📅 19:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2492">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s3p1FzUUW3IdShDJTrg8E6SbQuktusiJXj8hVGLtwUAoItszfnwQ5kXKog1IYJAgm-YKOZAiW312YrixLAVSNCHKP7eImwqnt3c8AlmD8MpLmLGl6mhZeAhrl_55WJz5ScB8mSfGJJinhMxhEeoOWNgWosg8NGTbjWc5rfAyfde8SbrsghlGq384zlGNjp8mIErnB954afSVZXBE5I_YBYq1HMDZe3m5fkMnsL6MeWtleR6k5H7oSWsTnv1k1s7FgorTX5ru2ZNP3w8-ccTa1kEVrmOYQwi5PlnYS6wj8Q-uqg_Nt4o3DqfzOauSxUmBl9JgcOixNFcmYUzaTpqOgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دامین
t.me
که بدلیل تحریم‌های وزارت خزانه‌داری امریکا مسدود شده بود، مجدد فعال شد.
©
Linuxmaster14
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2492" target="_blank">📅 19:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2491">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نزدیک به ۵ ماه مجلس تعطیل بود، آب از آب تکون نخورد. ۱۵ ماه وزارت قطع‌ارتباطات هم تعطیل بشه، وضع اینترنت بدتر از این نمیشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2491" target="_blank">📅 19:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2490">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دیروز کاربران گزارش دادن که IPv6 بصورت محدود روی بعضی از سرویس‌دهنده‌های موبایل باز شده. همزمان گزارش‌ها از اختلال شدیدی که روی اینترنت موبایل و ثابت بصورت منطقه‌ای اعمال شده، زیاد بوده.
در مورد اینکه آیا با از سرگیری جنگ ممکنه دشمنان داخلی اینترنت رو قطع کنن یا نه، نمی‌دونم. البته قطع مجدد اینترنت از کسایی که ده‌ها هزار نفر از مردم رو توی ۲ روز قتل‌عام کردن، بعید نیست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2490" target="_blank">📅 08:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2489">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hXbSs0RlodSGZxCOxrgMp5_Jey6BYhXIX2SFJmUrjmu-YQWIUq4FndciMJhsKT2m-gkT95tliiH-biKfzuogda3MFhrBxQ7RCKI3yhVnTZRJgNLnctkU2w9iZ1G_hH-Z8fvUxWEUno_YFzx9nsfRagDoF1idbLv-GM6xvFEirtTpJU6hMhhZQyIjTf8gRl4XexRIMqoFSUiujd2jZjJFYbx8fZdiC0WMrxssnddsj8QREpvT_w1ueD46UkwtO2zxrctNAtJQ2T64S8Oc3XisdJCNKvEWuPAv964dfkdl6_8LhtrRXuOBfgQK6mRYD83bb-vLXYhdxzHLteHjVcv5Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به یکی از شرکت‌هایی که API می‌دهند مشاوره مارکتینگ می‌دادم. چند راهکار برای کاهش هزینه جذب مشتری یا CAC گفتم، ولی تاکید داشتند که باید API‌ رایگان هم بدهند. پرسیدم چرا؟‌ خیلی راحت گفت: چون رایگان است، طبق شرایط Privacy & Policy تمام پرامپت‌ها و داده‌ها و خروجی را می‌خوانیم و ذخیره می‌کنیم. فکر کردم شوخی می‌کنند. بعدا دیدم نه. جدی است.
(...)
مواظب باشید، لااقل اطلاعات حسابداری و مالی و مارکتینگ و اکسل فروش و لیست مشتریانتان را به این API رایگان‌ها یا این سرویس‌های هوش مصنوعی حتی پولی که در ایران هست، نمی‌گویم ندهید، می‌گویم دقت کنید.
©
AdelTalebi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/ircfspace/2489" target="_blank">📅 07:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2488">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jD9k0HeCc7L5ClCASAZQeAjh9PvRSvNi_S4Dxg6uFkhbQ5Te7-wgtWBqmIYd0K7PbWKhZuel2IBUlaaoQMRpqdQTb14sYOXNzyGTDly2GwGls2CnlQ98ybmJcCYDbK7gW_rQGl6zCo1xs7-J_zTHnuqxAbLzJkyTbOtrC2iO_jxRR6jqsvDj6DSF81kASG6jBndJ2HyXLHcxPYmetA-FQsdpTic78DPJ468g2wpqjHJy4Y8mDUnV4C3wIHdaZkNhkZ7fJxGtYl6puIcruGyPzd9ip6DikrV0Ub9K8LHXyVDJguEQFdadvg95PsDHAEbxmgFSKfA4XGr5jLlT6UZoWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروتون در
یک مقاله
جنجالی ادعا کرده ویندوز دارای شناسه‌ای پنهان به نام GlobalDeviceId (GDID) هست که میتونه یک نصب ویندوز رو بصورت پایدار شناسایی کنه. به گفته این شرکت، این شناسه حتی در برخی شرایط با وجود استفاده از VPN هم میتونه برای مرتبط کردن فعالیت‌های یک دستگاه به کار بره و حذف یا تغییر اون برای کاربران ساده نیست.
پروتون با استناد به یک پرونده قضایی معتقده مایکروسافت درباره وجود و نحوه استفاده از این شناسه شفافیت کافی نداره و به همین دلیل از عبارت "ویندوز یک جاسوس‌افزار است" برای انتقاد از سیاست‌های حریم خصوصیشون استفاده کرده. البته این عنوان بیشتر یک موضع انتقادیه و نه یک نتیجه‌گیری فنی قطعی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2488" target="_blank">📅 07:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2487">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بانک ملی اطلاعیه زده که "کلیه خدمات بانکی و مالی این بانک شامل همراه بانک و اینترنت بانک مجددا فعال شده"، اما ایسنا نوشته "اعلام بازگشت خدمات بانکی به شرایط عادی، لزوما به معنای پایان مشکلات برای همه مشتریان نیست و گزارش‌هایی از تراکنش‌های ناتمام، کسر وجه و اعلام زمان انتظار تا ۳۰ روز کاری برای تعیین تکلیف، نشان می‌دهد بخشی از کاربران همچنان با پیامدهای اختلالات اخیر دست‌وپنجه نرم می‌کنند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2487" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2486">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">طبق گزارش‌ها اینترنت در برخی نقاط کشور از ساعات گذشته با اختلال و کاهش سرعت همراه شده و دسترسی به برخی سرویس‌های آنلاین با مشکل مواجه است. همچنین گزارش‌هایی از قطعی‌های مقطعی و افزایش خطا در اتصال به خدمات اینترنتی به گوش می‌رسد.
©
IRRadar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/ircfspace/2486" target="_blank">📅 20:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2485">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tCWfAOep6ojGz4fl-LIrAeHvdkOFNz8-hMo1XuE64NbbhxWprQ7Ib9c8xjZAmrhrNTZyju0DU-PancV1o-4tfhm-G2sfV6UPMOf9PMu8D0ekXstSxwfNvN6UtfhwXeUD960YbORlepvF-3Ds2G3JjV--4fjnkGekGo-9QAlHJgPCWqi06GNWg9iiGndJeYKXAZU0QD3o-ZYmy4H5dhBLpjM4BhECHR_KF89LCVehqLU85HTVYJe9tye36Q9pf0ZznSJteUVEVMPCXEfOip1sOXpKZnWHu2ZOfsCV243jRS9g5X5f7Z3bE5miYGMOXuLbIQMlxVS0TXnQFnFm7Ku5IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که بارها نام اون در گزارش‌ها بعنوان یک اپ ناامن مطرح شده بود، حالا یک محصول پرریسک دیگه با نام SpeedTop VPN منتشر کرده!
این برنامه با وجود چند میلیون دانلود در گوگل‌پلی، طبق بررسی‌های فنی پس‌کوچه دارای موارد نگران‌کننده‌ای مثل وجود تعداد زیادی ردیاب، درخواست دسترسی‌های غیرعادی و کدهای مرتبط با شبکه P2P هست، که می‌تونه دستگاه کاربران رو به بخشی از یک شبکه انتقال ترافیک تبدیل کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/ircfspace/2485" target="_blank">📅 08:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2484">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iGO7HmnkM3fMGOt91f2d3-vjsVVWAL5PcwoDcQavzuQEKXBP4vfqKxs4YHgkSHx_bRbY3DeoL8ZE6O_XDgmRU6ZwZ_piwWnDpBcRWpSAjZMSaYXt_y9_WExqp9BIzqFQrPAM3GZF8UkDrPcqo-c_LixWnbosgrTqjcv5wBxxE6Xq_T1kGugUBaWtFmCLh_lXkttvDhxZccf6xH5xM6uqyK14YwssqlXXjNhNkUDCQPAV7iNdkU6Nsi3hB-pdi-SNZM6G1x8M9G9F-_r_uT5Xvppl-PKkwVP_nI46HqS_qGvFuMfaZFCCSSe_HuYRh_yqA2_fWBjTTl3KEOWRwzZ58A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل زئوس یه ابزار متن‌باز برای ساخت فیلترشکن رایگان روی بستر ورکر کلودفلر هست، که امکاناتی مثل آیپی و لوکیشن ثابت، دریافت خودکار آی‌پی تمیز، لینک ساب و QR Code اختصاصی، فرگمنت، شبیه‌سازی فینگرپرینت، بکاپ‌گیری و ... رو بصورت یکجا در اختیارتون میذاره.
👉
github.com/IR-NETLIFY/zeus
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2484" target="_blank">📅 08:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2483">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TftDoyaEFNnO5iRJAbH0R29t2w7LSxlwl-7yC5jE3dZ9C7rYIxwVjgs_jrNOdDfywXEIDS_z0HnYqKXKtUw4bxCW57EhKsNLnrLoBF9ZkTmBdx-e0QaSYyjIo32QPcNlilCptvsJ6qkA1hyUF1jLgrajOYC3F4ISj7xv0vWnfD6bK1lMttZ5_WYCAX2A5uDhMFbt2Simpl-Cnos8A3uvRAC9ctu8RCWQCc78HcMTksUOjKOG5Mytmrqpk5yxJdvwn8hygoUKMJWDkZmcD-BZW-f8piZriX4sNuh5_UsdeqCGY0bJxZxqLxxP7YU_fg6hspnr6J7or--hnieHAeG13Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت یک آسیب‌پذیری روز صفر در Microsoft Defender با نام RoguePlanet رو برطرف کرده که می‌تونست به مهاجم اجازه بده تا با سوءاستفاده از یک نقص Race Condition، سطح دسترسی خودش رو تا SYSTEM بالا ببره. این مشکل با شناسه CVE-2026-50656 ثبت شده بود و حتی روی ویندوز ۱۰ و ۱۱ کاملاً آپدیت‌شده هم قابل سوءاستفاده بود.
©
bleepingcomputer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2483" target="_blank">📅 08:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2482">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Tz9h7Sx1qSdhGuh4M0_glPpjtzPN3KmTOYegIqPa-ErzGdyCRBTDUO63NqHxqBBVI3M0vwB2zuJKus_vAvdzvuFWDUBqAG5D0aFiJ37P5DQBZRT37DHRTgD3eFHe6xZb1K63JYimZBfNqhNQBx1UWHZMBuLS8B07QNMofr4RyWfnVT-Nvjq9dPKehGeIu9v05z_9EZK1f_yBXltTu0NciOxlBJV9KiF3w9xlhDqYmIA7aXppTvLSwaQRR_wwzGadbwuyA-UzBPFxgvvEo_8Y9hWkqglj6qpPyia8xXbh_cjU8mJka7ozzrw3OfJjhULwbK-FA5IpVuTOfbLTSZDQ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت اندروید NipoVPN که برای اتصال به هسته این پروژه و مخفی کردن درخواست‌های HTTP داخل ترافیک عادی وب طراحی شده، حالا روی گوگل‌پلی در دسترس قرار گرفته.
👉
play.google.com/store/apps/details?id=net.sudoer.nipo
💡
github.com/MortezaBashsiz/nipovpn/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2482" target="_blank">📅 08:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2481">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DghVkFmsYK-Ras_8glPoL28faZUeHQYMBrPortxv39fCMoiV8mjvFD8cRYi31S75hAzrczICt4d-KT1eh1J_2v7_qcEEON8ZG0AOL9MivRkaCA1jFzOnmVH4Hj7JOSYa9Wc7Wtlz_TaRvSKn3uFsRyFh9umYHGshF6Nk-GWVe5ZFeahVWwy6yACi91j_YE1hVP7In9bpt4MNl9w9RL2CZdH9d3pWb7YO0H5xCWSniTMJI77sZizPBtAaCWS7EzTK--rCVZ7TYriquUbnRcZT6EZU14oy0M8CH9_PFJgQy87cXOm8rsnB9JAjiWkyf_HvgxghpQZTIuyX8mynnJnzRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار BG Scan یک اسکنر متن‌باز و رایگان برای پیدا کردن و اعتبارسنجی سرویس‌های شبکه هست، که اجازه میده چند مرحله اسکن رو به هم وصل کنین و عملاً خروجی یک مرحله رو بطور مستقیم وارد مرحله بعد کنین تا فرآیندهای پیچیده راحت‌تر انجام بشن.
این ابزار از پروتکل‌های مختلفی مثل ICMP، TCP، HTTP، TLS، DNS، DNSTT، Slipstream و Xray پشتیبانی می‌کنه و علاوه بر اسکن، امکان اعتبارسنجی و مدیریت نتایج رو در اختیارتون میذاره.
👉
github.com/MohsenBg/bgscan/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/ircfspace/2481" target="_blank">📅 08:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2480">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v-ME3gD6ZeUNkBx6R9DKnSxopAZQ22h4u6ioEwNmmIhjCTTAaqN0pOhf_22sIFq8ueC5fLSRHL17oqpxmqTXoy65FmPAtn1Rg9OFdpAk5nYQ4WxK5cMZHh6wLv7lL2HYkRJpaCOY-T9ERmMsVPrzdUnQT0hoTEEueTw-G-Q6-jXmX59ii0byAn3LfT3RxAEVnijN2gy1hM1arrHuWs7Ol0M6JcjbWh1o7uDAjsfgzurKhqS-u5he3h8l6o4GjkyqqWX-dQTkhNbgG6YUGVDVJbb2GRaPSYBlJXdiBbs9nDIBFVUmKrT--p3iXALknaJYbOMse2HdDXqJUbLPSvzf_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاوه یه ابزار برای اسکن، استخراج و اشتراک‌گذاری کانفیگ‌های فیلترشکن هست، که کار پیدا کردن کانفیگ‌های سالم و به‌روز رو راحت‌تر می‌کنه. این وب‌اپ میتونه چندین کانال تلگرام رو همزمان اسکن کنه، کانفیگ‌هارو بصورت خودکار استخراج کنه و در نهایت یه لینک سابسکریپشن بهتون بده تا مستقیم داخل کلاینت‌هایی مثل v2rayNG، v2rayN، Hiddify, Streisand, v2box و ... وارد کنین.
توی کاوه می‌تونین کانفیگ‌های خودتون رو با بقیه به اشتراک بذارین. علاوه بر این، حذف خودکار کانفیگ‌های منقضی و امکان رأی دادن به کانفیگ‌ها و منابع از جمله قابلیت‌های این ابزار رایگان هستن.
👉
kaveh.yebekhe.workers.dev
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/ircfspace/2480" target="_blank">📅 08:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2479">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qx7gtkxZJ8kq6l8TX4gkJOaKaeX1iMAdApwvZqtKUxw_Fe9IBLY0W5R0BApXQb938R15Cq8OrizE3YLavgimXAWtqvbmFWpnSrYezFsfS11j6I-Z-JSY-0LTSL0Xeu4lfm4139Moo20WyPgS-iRMFpb8VIVMtShjKYQObYoWKxAOPt4TY7Jw9tmx24kTO4sfFY15LthP8ekp-vsm7MAD7v2V-NcUWDTlMMiVbFB-ZMPkHhh3wH-SoOzYDaLRxk2SNchVE-dsaDX1lL-6zx-Bj5-jRQDLJ8M5V7FC1pAwsd58VVVoTAofEaFmgD3r6fv4FFbhszffch3pd0tmS_8aLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ابزار MTProxyMax آپدیت جدیدی منتشر شده که توی اون از بهینه‌سازی‌هایی مثل BBRv3 استفاده شده تا عملکرد سرورها بهتر بشه و مصرف حافظه هم روی VPSهای ضعیف‌تر کاهش پیدا کنه. همینطور در این ابزار که برای مدیریت پروکسی‌های MTProto تلگرام روی سرور شخصی هست، قابلیت‌های جدیدی برای مقابله با DPI و اسکنرهای شناسایی پروکسی اضافه کردن تا شناسایی و مسدود شدن سرورها سخت‌تر بشه.
👉
github.com/SamNet-dev/MTProxyMax/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2479" target="_blank">📅 07:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2478">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JqDQWJGbiqOY8GFGxKDQzYV3p2hQRK-pWcluGG-HqxOAsx0Hcvv7wE12UwVyF1Z6V_zGT0id9SA6yfXKOMI3R4w9_xrO5yeU0B6e7IStOqn9QN9rthMbYcD-Pfzf-2OU72YUPwcR8MTYFihUwdYGsetTs4g4aXa4InCvh_vUvCQApoZjT66JW4MsH-lHMF8cfeiNq0xng6dtjY5EXrsbzTbTydouFqp4OeW4w-RAbDDUaJ_EgXy2LmbcGwL9s49Zs1wImh8t83oDbOPB0qjqFIyz8LuIuGzTFJggccoYqYUlFGiLnb5qTPn3UU-k-z717Bv7ZXPnb6j7g7LYT7r8vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Intra با استفاده از فناوری DNS-over-HTTPS (DoH) درخواست‌های DNS رو رمزنگاری می‌کنه تا اپراتور اینترنت یا هر واسطه‌ای نتونه آدرس سایت‌هایی که باز می‌کنید رو دستکاری، مسدود یا به مسیر اشتباه هدایت کنه.
این برنامه فیلترشکن نیست و آیپی شما رو تغییر نمیده، اما چون جلوی سانسور و دستکاری DNS رو می‌گیره، در شبکه‌هایی که فیلترینگ از این روش استفاده می‌کنن می‌تونه باعث دسترسی به سایت‌های مسدودشده بشه. علاوه بر این، رمزنگاری درخواست‌های DNS تا حدی از کاربران در برابر حملات فیشینگ و برخی بدافزارها هم محافظت می‌کنه.
اینترا توسط Jigsaw (تیم نوآوری گوگل) توسعه داده میشه و سورس اون بصورت متن‌باز روی گیت‌هاب منتشر شده. این اپ از طریق گوگل‌پلی در دسترسه و برای استفاده ازش فقط کافیه یکبار فعالش کنین، تا در پس‌زمینه کار خودش رو انجام بده.
👉
play.google.com/store/apps/details?id=app.intra
💡
github.com/Jigsaw-Code/Intra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/ircfspace/2478" target="_blank">📅 07:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2477">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d-F8bE1aDb_64rWHxVg5L_SCIj-k4WpPMikuxXGzpvfGvS-cPa5FnGfewZBhhSatq9mEDg6829WpwALCpdChptVejRgSg45-Lvf3Bh83gPtHgd85DrHm9y8IZmZlkWP0kGLmOtdptt5TKeXbNf8e6aWgEA_VWVyl8HRXQRiydMpxagJOmpxMjM87IsxzPdKAGUDJ2Yhba2NLRHbX9b0nfC9WfnhhYjr6lFySNc-HXoF8KOj9eD3yYC_J-FcABFXZYXKpIh9PhBloaMD-zxcrnvjGnlVKzyi6uq9q3TEfjASauDinIjcylCO50Jgeuu0JJ-fIOiLNLdJielm3WEcaQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محققان Datadog میگن مهاجمان با استفاده از بیش از ۵۰ حساب قدیمی و غیرفعال گیت‌هاب و توکن‌های دسترسی (PAT) افشاشده، از طریق API گیت‌هاب در حال جمع‌آوری اطلاعات سازمان‌ها هستن تا برای حملات بعدی آماده بشن و ساختار داخلی، اعضا و ریپازیتوری‌های اونهارو شناسایی کنن.
توی بعضی موارد هم تونستن ریپازیتوری‌های خصوصی رو کلون کنن. به گفته Datadog، چون این کارها با حساب‌های واقعی و API رسمی گیت‌هاب انجام میشه، تشخیصش از فعالیت عادی توسعه‌دهنده‌ها کار راحتی نیست.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/ircfspace/2477" target="_blank">📅 07:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2476">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JkHzWzW6YH9PJzRIC-Y63tZ2O0TdkLjkoRtaLeCw-_S9mfqC_uPPxiDPvxIdjcTYrBiV698-5jLyJBztE4Z8ABO41CV1wgcbJqQ-pFzKBnBDvjLyK3i5CEfjfQuZQHUv8xSYYHx8Kf77tiu_fJUHKTORVOkrCC6c5eLTVqYwCFz612JNIPjimBVBUqjhftMqcCTiYLtAfcR8j_MrR0xhf81AblkCwHKXrPpSK5WlfRpg_AvhlmiXZaPKz2xEmh-QQew1I72SLGL9-zWeRVai3uGtRpCR65BQKQXudYW33bfkJD54wXJUynr9vWrgyvZx4VpZH38WogYWopDrGPogZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایک سنتوناس، مدیر ارشد فناوری شرکت CrowdStrike میگه خیلی‌ها دارن روی این تمرکز می‌کنن که "کدوم مدل هوش مصنوعی خطرناک‌تره"، در حالی که تهدید اصلی جای دیگه‌ هست. مشکل واقعی اینه که هکرها حالا با کمک هوش مصنوعی می‌تونن آسیب‌پذیری‌های قدیمی و جدید رو ظرف چند ساعت، و بزودی شاید در چند دقیقه، پیدا و سوء استفاده کنن.
به گفته او، هوش مصنوعی بیشتر از اینکه باگ‌های کاملاً جدید کشف کنه، باعث شده هکرها بتونن تعداد زیادی ضعف امنیتی شناخته‌شده رو خیلی سریع به همدیگه وصل کنن و ازشون برای نفوذ استفاده کنن. یعنی اگر سازمانی هنوز وصله‌های امنیتی رو نصب نکرده باشه، حالا خیلی راحت‌تر از قبل هدف حمله قرار می‌گیره. هوش مصنوعی لزوماً حمله‌های جدید خلق نکرده، ولی سرعت و مقیاس سوء استفاده از ضعف‌های امنیتی موجود رو چند برابر کرده و همین بزرگترین تهدید امروز امنیت سایبریه. /اکسیوس
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/ircfspace/2476" target="_blank">📅 07:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2475">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qvKVNg6Tu2UEV5zdV8YB4Gvu8owFoZXsrv69M3Q3mxAKCqATSbVIwzcqLYOjvqPlDCVBQoYlVfY2k6DEn4OGhF35LDxDA1kaVecvRpjENGb5V3UaovfcTCSfx80FkITGfJVirCtsARTcXUgDGVgT31Ff1kAX4xGJCTJr5bnVKLS31wQcXVxsql69oTh4n5fTBirpXPfw86TPgd8ka95sAgG25Y0b7DoV7MfVL8uqCG7yaCtES9oid8L39N5k0fjEqQQRPZ4ZxThC7myOMT6bzYBzyp4kOdyVosungqJZxV6-kt-o22Vb8xQKOaaJVTuN3K2Ev7ySdx-IuYAOEVloMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ GRoute یک کلاینت متن‌باز و رایگان بر پایه هسته ایکس‌ری هست، که امکان استفاده از پروتکل‌هایی مثل VLESS، VMess، Trojan و Shadowsocks رو در کنار ترنسپورت‌های مختلفی مانند REALITY، TLS، WebSocket، gRPC و XHTTP برای دیوایس‌های اندرویدی فراهم می‌کنه.
این برنامه از قابلیت‌هایی مثل اضافه‌کردن کانفیگ وارپ، مدیریت لینک‌های ساب با بروزرسانی خودکار، مسیریابی تفکیکی، پروکسی برای برنامه‌های انتخابی، فرگمنت، Sniffing، نمایش لاگ‌های Xray، اسکنر آیپی تمیز کلودفلر، امکان تست کیفیت اینترنت، بررسی پینگ واقعی، تاریخچه مصرف دیتا و ... برخورداره.
👉
github.com/SuOracle/GRoute/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/ircfspace/2475" target="_blank">📅 08:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2474">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آموزش راه‌اندازی پروکسی تلگرام بر روی سرور شخصی ...
📽
youtu.be/pyvB6VSPhwg?t=176
💡
github.com/SamNet-dev/MTProxyMax
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/ircfspace/2474" target="_blank">📅 08:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2473">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YB0Wr8T5AU5cR4l-TkFLl_xsKP0F1JQMmkSPxdUMeOSPqOSDHQI6e_lutcnUJj31nRjmkFq74BAxcfF7vAYWv8U31axALBjmSFCU61XIUx4LHZGJZhYg4rDs5k_DgzwOFBuKJulOXDdZ5oVkMRrOOxjsNaRSXd_WOXzFTBBJf0YkhfrjhYj2HHCE6kGhfnoe6GCZkyfgCED83XTWw6KJhkJzVwDKN-GpTED-O8WwQ2VHbAypfYgujCxo917Y7RD1litxun_dNN9-n36yA2U4J2l3UsU7ePX3jTKKWlOHxRZSvpKfTk99WCZKAswWam5f8rYZUL0VUYUWu9qNPEZ4Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر سیمرغ یک ابزار متن‌باز و رایگانه که برای پیدا کردن آیپی‌های تمیز کلودفلر در اندروید و ویندوز ساخته شده. این برنامه میتونه آیپی تکی، رنج‌های CIDR، رنج‌های دستی و لیست‌های آماده ISP رو اسکن کنه و بهترین‌هارو بر اساس سرعت و تأخیر بصورت رتبه‌بندی‌شده برگردونه.
👉
https://github.com/rezakhosh78/SIMORGH-Scanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2473" target="_blank">📅 07:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2472">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PwgyK5yrFvz8BgFPkxISfg7iTfEWGBTFfOa0SiwFgZXxI05fWfOqFzsI6cTgjHd7uOTWSZnaTD6sFQhuIds9YKl5gVVX5VISArqZj2X4phSODTkIbRgRW7xlga4QRG4Yb0xWuh8Am2KUQRWUX-k0hajsajhB-8kzgd-EXEwjeeWSTF5xX2hi0rODWaj_z6kt2K5IR0Q54gUtPPugWmVBJTiKMwXj67xS8pw5B9miMtWUlTtKoetH9kVoE7TFtX_fS5O6aC3T0_vARSsslOlg_3gwtest0X4EH3T5XNr4GbxepSa9TZ7kwrrYKeMw2gHtnGCmCKNI-YHf-VSKdJkIGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر Asha یک اپ متن‌باز و رایگان برای اندرویده، که با تمرکز روی پیدا کردن آیپی‌های تمیز و پایدار کلودفلر ساخته شده و کمک می‌کنه سریعترین و مناسب‌ترین آیپی‌هارو متناسب با شرایط شبکه پیدا کنین.
حالت‌های مختلف اسکن، بررسی لیست دلخواه آیپی، شناسایی دیتاسنترهای قابل دسترس کلودفلر، امکان تست سرعت واقعی از طریق پروکسی و استخراج هوشمند آیپی از وبسایت‌های پشت کلودفلر، از جمله امکانات این اسکنر هستن.
👉
github.com/ashanews9776-eng/asha_scanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2472" target="_blank">📅 07:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2471">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نسخه ۱۷ از اپ
#MahsaNG
منتشر شد و توی این نسخه هسته سایفون بصورت ویژه برای شرایط اینترنت ایران بهینه شده. همینطور امکان ساخت، وارد کردن، خروجی گرفتن و اشتراک‌گذاری کانفیگ‌های
psiphon://
هم اضافه شده و یک اسکنر IP جدید برای CDN Fronting طراحی شده تا پیدا کردن آی‌پی‌های مناسب راحت‌تر انجام بشه.
امکانات جدیدی هم به خود برنامه اضافه شده؛ مثل دریافت کانفیگ‌های ایکس‌ری از طریق نوتیفیکیشن گوگل، قابلیت زنجیره کردن دو کانفیگ و حذف کانفیگ‌هایی که موقع تست پینگ توی ساب فعلی پاسخی دریافت نمی‌کنن. رابط کاربری بطور کامل بازطراحی شده و جابجایی بین ساب‌ها با کشیدن صفحه به چپ و راست انجام میشه، مدیریت ساب‌های بزرگ بهتر شده، شماره کانفیگ در حال تست نمایش داده میشه و از این به بعد خود اپ می‌تونه اعلان‌ها، اخبار و بروزرسانی‌های پروژه رو مستقیم به کاربر نمایش بده.
توی این نسخه مشکلات مربوط به اتصال مجدد و کرش سایفون، ایرادهای ویجت، باگ‌های CDN Fronting، کرش نسخه ARMv7، بازیابی نشدن رمز عبور HTTP، وارد کردن لینک ساب در بعضی شرایط و چندین مشکل دیگه هم برطرف شده، تا تجربه استفاده از این فیلترشکن پایدارتر و روان‌تر باشه.
👉
github.com/GFW-knocker/MahsaNG/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/ircfspace/2471" target="_blank">📅 07:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2470">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یکی از نکات جالب اختلال ادامه‌دار خدمات بانکی اینه که هنوز چک کردن موجودی از اینترنت‌بانک با مشکل مواجهه، ولی پرداخت قسط با قدرت کار میکنه. در کل هرچیزی میخوای از حسابت برداری، به خاطر هک به مشکل خورده، اما هرچیزی میخوای بذاری، میگیره
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/ircfspace/2470" target="_blank">📅 07:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2469">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مخابرات قیمت اینترنت ثابت را سوسکی بیش از ۵۰ درصد افزایش داده و آن را به بدترین شیوه در محدود کردن کاربران و تغییر ویژگی بسته‌ها انجام داده است. مثلا اینترنت ۱۶ مگابیت قیمتش ثابت مانده اما در سرویس سه ماهه، بیش از ۱۰۰ گیگ از ترافیک آن کاسته شده (۳۶۰ گیگ به ۲۵۵ گیگ).
حالا شما اگر بخواهید تقریبا ترافیک همین بسته را که تا ابتدای سال عرضه می شد بگیرید بایستی ۱۰۰ گیگ ترافیک بخرید که قیمت آن بیش از ۲۰۰ هزار تومان است و در واقع همان کلاس ۱۶ مگ سه ماهه با ۳۶۰ گیگ از ۳۰۰ هزار به ۵۰۰ هزار تومان تغییر کرده است. انتخابها هم محدودتره و برای ۱۶ مگ یا همان ۲۵۵ گیگ را باید بگیرید (و بعدا ترافیک جدا بخرید) یا انتخاب دیگر ۸۸۲ گیگ است که قیمتش بیش از ۳ برابر است!
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/ircfspace/2469" target="_blank">📅 07:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2468">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QzU7B1g6K5d96uKY356Is324lElqyIopSyk388wgKvZ5iD05dDW-2pel5JPZ8fIqVY7hHgW9osEQApvoHrCdt91jg6QrdzvcqGylpNeEeyFSa-CUrZ_0hOo3eC5bT6VMUdASYWOU9oqF_DIwCCbMMHzpQ1-Vkw254LLBhomslSoMNwdETLiKtXsjkFS_j81ib-LcE64hUix9j4u9RK-AJchfDPI4pJfyRNiZp8miaG6R9iW5OzHfKj8SXMgSGWrwGAtCO7UVk8hoe_Yvw1UZ5Q29nmIDu92Gl8xfCaEryTVKnXqX_A0z0ySAXIma3KeezkIpZBBJ7LW16m9b7LR0oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات (که به تازگی بابت عملکرد درخشان وزارتخونه در دوران جنگ ازش تقدیر کردن) گفته "لازم است با وزارت نیرو برای خارج شدن سایت‌های ارتباطی از اولویت قطع برق تفاهم شود".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/ircfspace/2468" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2467">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گزارش تحقیقاتی
HalcyonAi
نشون میده شرکت
ابرناک
(مالک جدید دامین ویکی‌تجربه) مستقر در تهران تحت پوشش یک شرکت آمریکایی به اسم Cloudzy مشغول ارائه زیرساخت فنی به هکرهای حکومتی کره شمالی، چین، روسیه، ایران و چند کشور دیگه‌ست. زیرساخت این شرکت برای ۹۰ روز زیر ذره‌بین کارشناس‌ها میره و مشخص می‌شه نه تنها گروه‌های هکری حکومتی، بلکه گروه‌های باج‌افزاری از جمله شرکت تحریم‌شده اسرائیلی Candiru جزو مشتری‌های این شرکتن و بین ۴۰ تا ۶۰ زیرساخت‌هاش به فعالیت‌های مخرب و مجرمانه سایبری اختصاص داره.
آدرس خارج از ایران این شرکت (که قبلا اسمش Router Hosting بوده) به دو کشور قبرس و آمریکا منتهی میشه. نشانی آمریکا به یک مرکز خرید در ایالت وایومینگ می‌رسه که آدرسش با بیش از دو هزار شرکت دیگه مشترکه. ثبت‌کننده کلادزی در آمریکا شرکتیه به اسم Cloud Peak Law که تخصصش ثبت شرکت ناشناسه.
گزارش تاکید کرده بعیده مدیران کلادزی یا همون ابرناک ندونن که بیش از نیمی از زیرساخت شبکه‌شون داره برای کارهای مجرمانه استفاده میشه. این شرکت در واقع به عنوان command-and-control provider به هکرها فعالیت میکنه و برای استفاده ازش فقط داشتن آدرس ایمیل و رمزارز کافیه. ابرناک در ایران در سال ۹۹ با نام «آلان فن آوری ابری» ثبت شده. دانش بنیانه، بسیار هم فعاله و در حال حاضر ۳۴ فرصت شغلی باز در سایت جابینجا داره. مدیر این شرکت محمد حنان نوذری به رویترز گفته فقط ۲ درصد از زیرساخت‌هاشون در اشغال فعالیت‌های مخربه. همینطور گفته نباید چاقو فروش رو مسئول خلاف مشتری دونست.
دور از انتظار نیست اگر اسم این شرکت و عوامل اصلیش رو توی فهرست تحریم‌های آینده ببینیم. ابرناک حساب‌های توییتر، اینستاگرام و لینکدین خودش رو غیرفعال کرده. نکته آخر اینکه غلامعباس نوذری که در شرکت ابرناک شریک محمد حنان (احتمالا پدرش) هست، دیپلمات ایران در نیوزلند بوده. حنان هم در پروفایل لینکدینش به تحصیلات در نیوزلند و در پروفایل کوچ‌سرفینگ به ۱۵ سال زندگی در این کشور اشاره کرده.
©
arashzd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/ircfspace/2467" target="_blank">📅 08:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2466">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kMhof7HQ5sV8c4Qzsp__eJQJc6OPpe_ab5pCJxviclzCPCDr61opWag9knAWbZSHfW3HENQsTZ0_ipyNuc5B9-Pffh5Nw3-u0kbRYqP2aYNIreaXIELGrJ6gsQTA5goInzQq286wBtY0l81VSEilwyvOEgf9NP6ReA39z_FYtLahd-3Vj249L3mKX9I_qDt628_RCR7iQw72pteQ6uXtrZf42o5jn1pZhGrM5LTML2hDiLFNvxPqVtT3lHZG8hB6PwJLB0FGJHCmQchfYQAd0_B37LsF29czcUk98_6pIzqMYpYslL5vVk0zALgenYWDJ_9nPp_z1ztPMNX8cis9eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران از رتبه‌بندی جهانی اسپیدتست حذف شده. شاید فکر کنید چون دیگه حتی ته جدوله، رتبه بدترین اینترنت هم توصیف مناسبی نیست، یا دیگه زیر ۰ و منفی جوابگو نیست.
نه، چون چیزی که داره ارائه میشه اسمش اینترنت نیست!
👉
speedtest.net/global-index
©
Mehrdadlinux
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2466" target="_blank">📅 08:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2465">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rzZvtjzDiXE7GXnvArRkxWMaQTE39mTytzIGqhgsp1bHJ-5zo_xuNEpe-suDFcG5tVeoNxyRZ6TMx2M9dd66MgkWUymfCXVFHpO1T2YPlphQb4JdbdZpRqdMjT314qJfUJePVcAuImTpdshtfQN4_RSZhg7-oVCALYq8k4R7-91-WMUjnj3U2OgEvh_N_BMiqbCmqtPwwh46mowDFxs7PaQ5nPPMlC_RocPYCQ34W4s4Z1zaOCT2G47YCHXzxXyUBt4_WOvs4HfbIH8-I7XSyZUfgm_Hfx2UChyy1oq6UeUAsFrHHjZA7RqKidsND5q6iAkuTOKLtLjOGrs-Jynyvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این چندروز احتمالا در مورد اکانت ویکی‌تجربه و سرنوشت نامشخصی که برای مالک ناشناسش رقم خورده چیزهایی شنیده باشین. متاسفانه دامینشون رو در ایام جنگ و قطع سراسری اینترنت نتونستن تمدید کنن. بعدش این دامین توسط ابرناک ثبت شده و با یک پیام مسخره و کینه‌توزانه، صفحات سایت تغییر پیدا کرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/ircfspace/2465" target="_blank">📅 08:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2464">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F1_iMSomY244P0Avq6aNDT2bAkW1oVWNbPpFRVcYC4y-Pq9sHVhT2hG_LVxkJVEdRERuuXkbTt8u7WYKmdScX6v3ldZ89qOW5wOCTSxcRxVueSZAquK4CrorJWOPgqzD6dlOZ9U5D_zGU4nL56Nst5Pj1B3wj4kcfnvRofN8sKSlQ75NGkn7QHzmsVz9SLYk5Z7S9GiJs9bz7itACSU4sHl_At1j8g7i9_LSsT0c2veqGpT2_5IAXqVZTy53AcEDqUgAg63JhLTgRrTe7Bv3CpUK17Ugzutscfjnq9x3yhBwrce-i9ZjkDPlIVBoLWviKcofTgoA8emPsShgP8pmLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از
#لینوکس
استفاده می‌کنین، فیلترشکن دیفیکس در جدیدترین بروزرسانی خودش پشتیبانی از این سیستم‌عامل رو اضافه کرده.
👉
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/ircfspace/2464" target="_blank">📅 12:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2463">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oHleLi7q49vCA7E3k2x73G42Cye2OaZ2BAuxikpqXuxPyI2VCRLZ2KKqdVXEfBEhr81NTR6BFLT1ok4n0diCeBislneJwgf45yiRDXfTpW6Uaseuwsb6TGkarX-UCsdx4YXug-iV-w7eRpLnzTtOv8iprBZ6Q6MI4H3Mwww7pi8qp_MGSL4jhv2tvI7SrGVPV583Eh3nXJj_o311S5V2XnQjHWNGO4z0hVUV7BvtsauhoeFXqiK2tYso5ukTU7qsmN1y63MndGzMGYvF03thdmXt8mf-4FiT_Fym8gfvaqa_te4zHYXVmA-pGWIUCbqFJSfrpFi7ttBxR38j7501Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ RedCloud VPN یک کلاینت متن‌باز و رایگان برای ویندوز و اندروید هست، که با استفاده از هسته Xray توسعه داده شده و امکان اتصال از طریق کانفیگ‌های VLESS، VMess، Trojan و Shadowsocks رو فراهم می‌کنه.
این برنامه تمام ترافیک دستگاه رو از طریق تانل‌های رمزنگاری‌شده هدایت می‌کنه، از قابلیت اسکن و سنجش همزمان IPهای کلودفلر هنگام اتصال بهره می‌بره و همچنین با استفاده از قابلیت Sniffing، ترافیک HTTP، TLS و QUIC رو شناسایی می‌کنه تا عملکرد اتصال بهبود پیدا کنه.
👉
github.com/Devtahas/RedCloud-windows/releases
👉
github.com/Devtahas/RedCloud-Android/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/ircfspace/2463" target="_blank">📅 07:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2462">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بانک ملی از اختلال مجدد در خدمات کارتی خودش واسه ساعت ۲۲ تا ۲۴ روز جمعه خبر داده بود، که گزارش کاربران نشون میده این اختلال در روز شنبه هم همچنان وجود داره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2462" target="_blank">📅 07:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2461">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">الان خرید کردن با کارت بانکی مثل دستشویی رفتن شده. اول باید چک کنی آب وصله، بعد کارتو بکنی؛ وگرنه ممکنه گیر کنی.
©
shokhmatic
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/ircfspace/2461" target="_blank">📅 18:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2460">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">در حالی که با اعلام شرکت خدمات انفورماتیک اختلال خدمات کارت محور بانک‌های کشور برطرف شده‌اند، بررسی‌های کاربران نشان می‌دهد که همچنان بخشی از اختلال‌ها در خدمات‌دهی بانک‌ها برجاست. اغلب اختلال‌های موجود در بستر نرم‌افزارها و همراه‌ بانک‌ها برجاست و این موضوع کاربران را در برطرف کردن نیازها روزمره دچار مشکل کرده است. /ایسنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/ircfspace/2460" target="_blank">📅 18:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2459">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pl8Z3kOyvnMsFx4M-Kq2nFUqLuwhY_5-KN3WkJVoGsQatUEp_RXmobNrwBzUiaMV5E-PWR6h55TPBujYXkvaWAKsNJs8DQZhYssQW-y_UUGJYUcCq-KP08E5trM00qH5kNoeZkJB1YoYspelkWyAV5Rv-s5y9o17DH1c5R0WtK8Qag23aVlj51WoNJ84cB7U_CfS3Y4q_Tm-99w_QyAqN_cLwbmoOCRmZ7wCR6rt-ohyAECkyzWm6zsAqi5FZs9Rw1DeHc4nfV8dYMt-s_I_RUW1fXx8ov0kW1wgiOmOO1FZyg57xLLqX7XfamEk8MH0OclVGN7f8IkeuvgHEdsBEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمیسیون اقتصادی مجلس طی نشستی با ستار هاشمی، وزیر ارتباطات و فناوری اطلاعات، از عملکرد این وزارتخانه در دوران جنگ تقدیر کرد. /دیجیاتو
بابت تقدیر یه کاسه دادن دست وزیر قطع‌ارتباطات؛ اما بابت ۸۸ روز
ریدن
به اینترنت باید یه لگن بهش تقدیم میشد!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/ircfspace/2459" target="_blank">📅 20:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2458">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">خدمات‌دهی دست‌کم ۸ بانک کشور با اختلال مواجه شده. شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، حملات سایبری را تایید کرد و نوشت "شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه خدمات مبتنی بر کارت را به صورت موقت از دسترس خارج کرده است". /iranintl
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/ircfspace/2458" target="_blank">📅 16:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2456">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اختلال خدمات بانک ملی بعد از چندروز نه‌تنها برطرف نشده، بلکه این اختلال فقط محدود به همین بانک نمیشه و خیلی‌هارو گرفتار کرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/ircfspace/2456" target="_blank">📅 13:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2455">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">جنگ شد، اینترنت رو بستن، تنگه رو بستن، آتش‌بس شد، توافق کردن، تنگه رو باز کردن، اینترنت رو بصورت تدریجی برگردوندن، گشایش شد، مسابقات جام جهانی سر رسید یا هر نمایش و کوفت دیگه‌ای؛ ۸۸ روز قطع سراسری اینترنت، سرکوب، اعدام، زندان، شکنجه و کشتار ده‌ها هزار نفر معترض دی‌ماه رو به فراموشی نمی‌سپریم.
خون‌هایی که روی این خاک ریخته شد و نسلی که هزینه آزادی رو با جون خودش پرداخت، از حافظه ما حذف نمیشن. بین ما و شما دریایی از خون فاصله هست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/ircfspace/2455" target="_blank">📅 09:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2454">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cHTW3MGanzbzNCiiAEMkUDhc6FPpHXxkvUzSPERyVwgUnVDgdWsFpQSIkH9QNFzsn7AXawXBWvOLsOKl-IeYW9ah4M0tp_nyG1Ywnaj2C3s5aVh7FnYC-9VH9QnZuJPlB6M0FPyli2806xeF-GbOhj1sCxZS00sKsvE1QV-VGXV9mqlj5Bbm4N5ZLGp_nREixYKCNI6SIVFsyPfSGNCjWhVqKiT05_0sXSRuZpO3O3QIeTEUSTG0HXW9cvDsLUtnmjRwCr4AH4vAlt_0CuwNXj4kcsK_ribQ4ZBjHVulc_D0GO_ACzpatQy9-_qI3iXREKe2TqWrne_Oba_CMDMT1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل V2X یک ابزار مدیریت اشتراک سبک و متن‌باز برای VLESS روی WebSocket + TLS هست، که به شما اجازه میده با دیپلوی پروژه روی سرویس‌هایی مثل Render، Railway یا DockFly، برای خودتون و خانوادتون اشتراک اختصاصی با قابلیت بروزرسانی خودکار ایجاد کنین.
این پنل امکاناتی مثل مدیریت کاربران و کانفیگ‌ها، تعیین حجم و تاریخ انقضا، نمایش آمار مصرف، مدیریت IPها، اسکنر داخلی و ارسال گزارش و هشدار به تلگرام رو در اختیار شما قرار میده.
👉
github.com/SulgX/SulgX-Panel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/ircfspace/2454" target="_blank">📅 09:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2453">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZNmk62hV36UT3macwWcAOcBdtCL-7Wz6bmvgLdBe53dxXtdUo19JkY1LVokIQy1aS9XYMcl-hU_MxG5NKurhRW428edFjR-hlF8AQ8--7_FaWo4jSCiFTFITLVGWRxKOlZpVIaSFmiUiGItHJE0H4oc2Fo-tE6A-p5NRDUzK5zBIQ9Av9hY_JsQ4Huu_7EKJdqgAiv7SgaJ8LOYI3-56R0QKkLY-i7yb_4dtjesrh4zzcLLO6UcrDqjbXOt00ScnKkELJdRARDBzCoyzWIsc8nz5Rt1bln3nwGPADe4CVww5hUSmj049eEUDAhwW6HRXTq7VZniI4qpFHeByqtRIlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از کاربران ایرانی به نام MrArrow دو مشکل مرتبط با فرگمنت در v2rayNG رو برطرف کرده، که از نسخه ۲.۲.۵ به بعد این اپ اندروید در دسترس هستن.
این کاربر توضیح داده که "چون تو شرایط فعلی اینترنت ایران Fragment نوع
tlshello
روی خیلی از اپراتورها دیگه مثل قبل جواب نمیده و بین حالت‌های مختلف،
1-1
معمولاً عملکرد بهتری داره و حتی با مقادیر پایین Length و Interval هم میتونه از فیلترینگ مبتنی بر SNI عبور کنه، یه سری مشکل در برنامه وجود داشت".
مشکل اول این بود که با وجود اینکه هسته Xray از Fragment نوع
1-1
پشتیبانی می‌کرد، اصلاً گزینه‌ای برای انتخابش توی رابط کاربری v2rayNG وجود نداشت. مشکل دوم هم این بود که v2rayNG عملاً فقط
tlshello
رو استفاده می‌کرد. یعنی حتی اگر توی تنظیمات نوع دیگه‌ای از Fragment انتخاب میکردی، موقع اجرای کانفیگ دوباره مقدارش به
tlshello
تغییر می‌کرد و انتخاب کاربر نادیده گرفته میشد.
👉
github.com/2dust/v2rayNG/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/ircfspace/2453" target="_blank">📅 09:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2452">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CVadXTrisoc3Y20twJ9oE0RtC-PvnDhgLyNpZPnOT-xxub5pMCDmUGEKmnjWhKDQVVdzeg60wndAZ1mGHkvpienqfSViipJwvJf9xIv9y7KrLvaaDS9FWjC6pqsTrq-sIkvalA0UzYBRBmnx_5XTOjLymbSuFr-3vp8nq2pe21K7h9XG4BWUAPcT3jhRjK0O6WjfH3V5v9cEr2xaJsv9GLiI2FkUEzBZanFUTtPKsNMpmHqq5e7IthhqOCYtXLiJH3uj4Iqzkhp54fxu9dK4HXqJ9bAqRX-0Npr8JbcmHo0g8H1A7w_7CWcpv9Jf1WC293o740aMo4mqFNtQ6EHdqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکت اندروید F-Droid (که کاربران میتونن بدون وابستگی به گوگل‌پلی، اپلیکیشن‌های آزاد و متن‌باز رو ازش دریافت و نصب کنن) هشدار داده که گوگل قراره از سپتامبر ۲۰۲۶ قوانین جدیدی رو روی اندروید اعمال کنه.
طبق این ادعا، توسعه‌دهندگان برای اینکه برنامه‌هاشون روی دستگاه‌های اندرویدی قابل نصب باشه باید در گوگل ثبت‌نام کنن، هزینه بپردازن، مدارک هویتی ارائه بدن و اطلاعات مربوط به برنامه‌ها در اختیار گوگل قرار بگیره.
منتقدان میگن این تغییر میتونه نصب برنامه‌های مستقل، پروژه‌های متن‌باز، نرم‌افزارهای شخصی و حتی برنامه‌هایی که خارج از گوگل‌پلی منتشر میشن رو با محدودیت جدی روبرو کنه. به همین دلیل F-Droid و برخی فعالان حوزه آزادی نرم‌افزار معتقدن اندروید بتدریج از یک پلتفرم باز فاصله میگیره و کنترل بیشتری روی اینکه چه نرم‌افزاری روی گوشی کاربران نصب بشه، در اختیار گوگل قرار میگیره. به همین خاطر کمپینی با عنوان Keep Android Open راه افتاده تا کاربران و توسعه‌دهندگان نسبت به این تغییرات آگاه بشن و به اون اعتراض کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/ircfspace/2452" target="_blank">📅 08:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2451">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کاربران میگن "ظاهرا" دسترسی دیتاسنترهای داخلی به اینترنت داره برقرار میشه. فکر کنم هنوز از اون زمانبندی که نامسئولان قطع‌ارتباطات گفته بودن "بازگشت اینترنت درحال تکمیل شدنه" چند دقیقه باقیمونده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2451" target="_blank">📅 08:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2450">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oNEMeoHXtgc-LzoSNa7BxMQmF03IYlTN12623EAuCjQSO1pgPKH221rEQgyY8hSKZ0QK-S5wJMvUv0K9v5_qVDhaMwcQUllDG2ltZS6y4c7X2AyZPVz7R90H1biW8iCYwr4NluVNylvPBtbw3PkkzeUohqXvihqnS35etGYsov9n7LJge0RLDy6GxESSf3iTmNrAqXBWXx2HYTxE14AKlWp4NXqHH1txo-MRtooHsn-TkGehqkESMMfx0aFLPLpwHvvdxh-wCJuzjBPNCenyOIebvRpbCB_LND0CFn2-NYNLdmeCeWjeZQItSoz3etEF4QyrMLqzfpgl_b4PUSjz7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما تنگه را مفت ندادیم، زندگی یک ملت را مفت دادیم. سال‌هاست حرص و ناکارآمدی‌تان را «سیاست‌گذاری» نامیدید، ماشین قراضه را ده برابر فروختید و گفتید حمایت از تولیدملی، اینترنت را خفه کردید و گفتید «مدیریت»، فقر را گردن تحریم انداختید در حالی که رانت و انحصار رگ‌های مردم را بریده بود. جوانی را به مهاجرت، کسب‌وکار را به «تاب‌آوری»، آینده را به سکوت فروختید. اگر چیزی واقعاً مفت رفته، نه تنگه هرمز، نه یک وجب خاک؛ عمر مردم، آرزوهایشان و فردای سوخته‌شان بوده. این صورت‌حساب واقعی است.
©
rassssoo
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2450" target="_blank">📅 08:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2449">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">این اختلال GPS بخصوص در مناطق مرکزی شهر تهران برای چیست؟
داداش طرف اومد نقطه زنی کرد و رفت و تمام شد. الان GPS رو مختل کردید که چی بشه؟ ملت اونجا سرگردون و گم بشن؟
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/ircfspace/2449" target="_blank">📅 08:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2448">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j6aeQr9c3ddVkpBLenaS6U_2lH8OoeEJgmWJX4OHZR70tu8rPy3Q7YoraDg8nHFLPgQG3EK4AlNHG82lQNRTf8plJmNPD5i3AHuNmHpaAuKs2VvTQq0t51Y8IwuIs6LUKg4kRQ053F2ymbYj695OVAY63cXtFrYzG1bNSQJwGBTJ8lBdhH3ZSkrS8oQQVKo14x0k2vY385gVe1XZXdtT6yIJ-1EPJ7BeLXCufAVsYI173q2ZYQdxcHl7h-jEezUDVGwgqE7_UMGtiuNC1jbAxJhgffDHnKqugSrs-UQwpIF1CAF54OeZRTlBXREloyICpNgdfo_WUssp2zuzp7pTdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه CandyTunnel یک ابزار متن‌باز و رایگان برای ایجاد تانل روی سرورهای لینوکسی هست، که با استفاده از تکنیک‌هایی مثل تغییر و پنهان‌سازی آدرس IP، رمزنگاری ترافیک، بازیابی بسته‌های ازدست‌رفته و روش‌های مختلف عبور از فیلترینگ، تلاش می‌کنه ارتباط کاربران رو شبیه ترافیک عادی شبکه جلوه بده.
این ابزار از پروتکل‌های انتقال مختلفی مثل UDP، ICMP، Proto58، TCP، QUIC، IPIP و GRE پشتیبانی می‌کنه.
👉
github.com/AmiRCandy/CandyTunnel/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2448" target="_blank">📅 08:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2447">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Iz0iJ-mRUhHhnMqJmV_uPNsm7EH_6W4qw8D2J00hDlVjYB2bXl5qgatVi6glwDZOmRXPvGKfdNHPbLVC8FNIF4NF1-9bgdc86NOJ84nW_mRskghOmJtN2dBuRC9eNcapCR8fi5ibOlgjsGRC31MbH-w-sTrXVlVO-dvtpaEFrSqGtNibLSHfgl6EO5iqSQ6KBL5HHPzZMo4booUHpYUahAB1Wt52hZNSmCbySmCd5V54iGwO4Iokw7oC-AUE4E43xS5Jb7TRR3UFOHHAPAE191Q9WG-Dj3e3QtLVy2VgidXiPkPEkWr00zJdjmfLMvRLU0S37Ku1DyuSpHE-YW6xwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار Config Converter یک وب‌اپلیکیشن متن‌باز هست، که ۳ ابزار پرکاربرد مبدل V2Ray، مبدل WireGuard و مبدل Clash/Sing-box رو در یک محیط یکپارچه گردآوری کرده.
این ابزار امکان دریافت مستقیم کانفیگ‌ها از لینک‌های سابسکریپشن رو فراهم می‌کنه و ورودی‌های Raw، Base64 و JSON رو با تشخیص خودکار فرمت، پشتیبانی کرده. همینطور کاربران میتونن بصورت گروهی آی‌پی، دامنه یا پورت تمامی کانفیگ‌هارو ویرایش بزنن.
👉
darknessshade.github.io/Config-Converter
💡
github.com/DarknessShade/Config-Converter
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2447" target="_blank">📅 08:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2446">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HePyH1SUPYlRVFoz_l9ke3zyeaZwpu10FPti91zuD-1n8G2rtejSI17AfbYdwE4aZ4vq2CRE_1fYXxEN2gUdycZqO9OaCZjV5sbK8tp7gKXlJjiw1xGrZRyWMcl5HM0-qEg0OWwvMSdVCzOBOg3oJVKgRVTw7F-TLnCDUit6I7zGtCUudLgeeQbjQWWYPPHFYbIkrCGrH6Ye6XsobrfBICUnqtpVU_Brs9jt-ls4ho5sUJ6mp-fB_Vo_wsL2r550xJvzx90brTjtIzAKxnKyIXglGcUj9AFzp_hLa7oof3pH4Lc9rOmTlEVX2Q8toIsSylqGHU7TCvxgSNHnsZdZhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان بازرسی کل کشور از توقف اینترنت پرو خبر داده و گفته اپراتورها اقدام به ثبت‌نام گروه‌هایی از جمله وکلا، مدیران و اعضای هیئت‌مدیره شرکت‌ها برای دریافت اینترنت با شرایط ویژه کرده بودند. در اجرای این طرح، هماهنگی‌های لازم با رگولاتوری و وزارت ارتباطات به‌طور کامل انجام نشده یا در برخی موارد محل اختلاف بوده. بنابراین مقرر شده از ادامه اجرای بخش‌های دارای اشکال جلوگیری بشه و مبالغ اضافی دریافت‌شده از مردم رو بهشون برگردونن. /فارس
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/ircfspace/2446" target="_blank">📅 18:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2445">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ufRQwdP5C4p595WfG__FaY9oGo8OKz6ReK6mRuy5kXi_EspHlllu0snRcb4FO94Hb_9-zoMGkZ_mLpKsIwMun8t_TLoygMxR3-kVF5ULGc-Ads7gIJWFMTrFnTrfmpe3DGqqXBG3jLY_Axy3gPUGQRbbEPNbnQqbUasmIUr4cjuzQXPxYSS81gXIp8AbTaXMUiMq7_7oFGgTp-8bORLvVZYUwY9Cn2PpUVU6ExWhDUPaTijGtiGejmVQ-KdPQAqVWOVL8sv6AShhq05GVWh_7l-NEQgy2L16y3RXbrju9eIp5WtpSYO_Y3H4j0ONvbWFOJJNGN039vxIDYUMoaZMCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه NipoVPN یه ابزار پروکسی سبک و قدرتمنده که درخواست‌های واقعی HTTP رو بین ترافیک عادی وب مخفی می‌کنه. این پروژه با معماری Agent-Server کار می‌کنه؛ یعنی برای استفاده ازش، اول باید هسته رو روی یه سرور راه‌اندازی کنین و بعد کلاینت‌ها به اون وصل بشن. در حال حاضر هم کلاینت رسمی اندرویدش به‌صورت متن‌باز و رایگان منتشر شده.
👉
github.com/MortezaBashsiz/nipovpn/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/ircfspace/2445" target="_blank">📅 08:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2444">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jrcVSpsewHmNMyqRckJvG-yb5XWk0rr2KsQpT8h9YO30tpZgbh-74O9tmSk_sSF7S1kd07GE63LV1n9c1paXCjiAOjJfBLxTB3pu-K2Cdx3VMFS__aC7yBXvykYtM9xz7unE3hdqAd0KVoIIt__1e96xR5Ct9j7JLKaiSbQuybykp3cDEbDmOG3uDFefQJvXxwQF6JCmQ0F6y34q6Ec1QW4PNAsq8vZJ1JYbWzFYPshjy3M6GpFl6zXXbUaySI61rRGrQy3aUVHig4LHnsCV-bQyrueOk0sINhiq9uMbDAmj-LunfAh7bJcJuOeixbLXhm0rXsL7Qx1NqnqTpyIbaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ InviZible Pro در بروزرسانی‌های اخیر نسخه بتا، با اضافه کردن Tor Snowflake و پشتیبانی از پل‌های DNSTT، قابلیت‌های ضد سانسور خودش رو برای عبور از محدودیت‌های اینترنت گسترش داده ...
👉
github.com/Gedsh/InviZible/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/ircfspace/2444" target="_blank">📅 08:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2443">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پاول دورف، مدیرعامل تلگرام در واکنش به محدودسازی استفاده از شبکه‌های اجتماعی برای افراد زیر ۱۶ سال در بریتانیا گفته: این ممنوعیت فقط اونهارو بیشتر در معرض خطر قرار میده و کودکان به استفاده از VPNها روی میارن، که در نتیجه به محتوای غیرقانونی و به‌مراتب خطرناک‌تری دسترسی پیدا می‌کنن. برای مثال هم به استفاده بالای فیلترشکن در روسیه و ایران اشاره کرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/ircfspace/2443" target="_blank">📅 08:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2442">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">از میان ۴ بانکی که اختلال برایشان پیش آمده، ۳ بانک در بستر ایران‌اکسس فعالیت می‌کنند و دسترسی مستقیم به اینترنت ندارند. یعنی هیچ ارتباطی بین آن اختلال‌ها و وصل شدن اینترنت نیست.
©
emirhussein_rz
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/ircfspace/2442" target="_blank">📅 08:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2441">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WWmWY6b42RvEZqN1DE-fzmfurmoZn0JzZIkgN0S5Gn0l580h2cga87NeZie38Ubt2bmQu5enz40vmSYl7Pmyfp9uauC9IO1qxDWS8dE88cP9A4yGGIXvB9CJePCvbZGsRwtRe3i0pyqLDQOG_2c3KRDrOhi8wN8IBvbPu19VDKHey0omkgp8h-6MCYM7ljw3y1pWEgQTtvE3SMurgouO_w8k6iOmgOgumXw1DHthM98ks6AbfTQW6YB1W3_Tjucfj25WBBTpS4OaaMonzWizQAAEx_99PN7iLxX3fKfRSItUhhtHCOt3lUQjR50Da3uHFmCOQdZAavbnSZZ8q4Meig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویروس زارع‌پور به هندوستان رسید؟
دولت هند اعلام کرد که دسترسی به تلگرام رو در هند تا اول تیر مسدود کرده، چون از این پلتفرم برای کلاهبرداری از داوطلبان شرکت‌کننده در آزمون ورودی پزشکی استفاده شده. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/ircfspace/2441" target="_blank">📅 08:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2440">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NXzfyADm8oB-uii1LBhPHemPI79-KLVGbqETaRZpnbpAFG1LS1QpfbBJSP2E1zmhxnxvu5qG_cZprdKVOuFf05rEjpoRlLA1NFhfy5_lIE6Z3iV3AYmABJ6mA2XT3D3_cMiAMZw3QUKUjI3hyV602H9Ogqg04lB2xzOd32ye-otB6OSHfOTfT4LMUIO1TKvNYkm9AAM704fHFndv1LHLMQBFEwPPcfZQL3PFXUtZT87Ux-mRU4rA5vtrcOKGI0gDpv-mg_cLMd9MQUZeZiFi-7CHDFRIVBxwQC4A9kx3Be6IoAbxqaBuLwW4RZFvizgK_cCyWIAf_0ZUoYbVV2WUPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ سیمرغ یک کلاینت VPN متن‌باز و رایگان برای اندروید هست، که با پشتیبانی از کانفیگ‌های XRAY، پروفایل‌های NipoVPN و موتور اختصاصی MSP، تلاش می‌کنه بهترین مسیر اتصال رو با کمترین پیچیدگی در اختیار کاربر قرار بده.
اسکن هوشمند آیپی، انتخاب خودکار کانفیگ سالم، پشتیبانی از کانفیگ‌های ServerLess، پروکسی محلی، ذخیره IPهای تمیز، بررسی سلامت کانفیگ‌ها و ... از جمله امکانات این برنامه هستند.
👉
github.com/rezakhosh78/SIMORGH/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/ircfspace/2440" target="_blank">📅 20:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2439">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">با وجود ادعای رفع مشکل قطعی و اختلال در خدمات ۴ بانک بزرگ دولتی، این اختلال‌ها برای سومین روز متوالی ادامه دارد. نیما اکبرپور، کارشناس فناوری، معتقد است طولانی شدن روند بازیابی، نشان‌دهنده ناکارآمدی سامانه‌های پشتیبان است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/ircfspace/2439" target="_blank">📅 19:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2438">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/672c6641f0.mp4?token=NyTD1_AUX9I3dC61DvaC2vmjUIvSvLc2HgMs6wshTCl4vQT41JQvhZCUzLYagoqK8P5QlG3gApAU3SAUJZ6WtnKqFh5A3FaCFpTKr2DI7oTZg6GTFb9-zCvJvnXNCO6Qva81fmRpEn33na_d_IeaiJg1Y3hKucn7Vuc09BlxvtAf_YE972F5ED1P4Ce0GWH6I5n3_eiN8lwx3NN0a7HdDHSKy6tkCOIQEHwEXQlPHrIoEcl5-1LldWbRKlgYslSKJTBfpG2jK_FPH9hQ7h5O7EFtfvq7xnbJxaXBnuLHXlUGTAvWjNUWqEbL3sfE3AbC_1FQ-uJ-mWlixAiYBr6Fwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/672c6641f0.mp4?token=NyTD1_AUX9I3dC61DvaC2vmjUIvSvLc2HgMs6wshTCl4vQT41JQvhZCUzLYagoqK8P5QlG3gApAU3SAUJZ6WtnKqFh5A3FaCFpTKr2DI7oTZg6GTFb9-zCvJvnXNCO6Qva81fmRpEn33na_d_IeaiJg1Y3hKucn7Vuc09BlxvtAf_YE972F5ED1P4Ce0GWH6I5n3_eiN8lwx3NN0a7HdDHSKy6tkCOIQEHwEXQlPHrIoEcl5-1LldWbRKlgYslSKJTBfpG2jK_FPH9hQ7h5O7EFtfvq7xnbJxaXBnuLHXlUGTAvWjNUWqEbL3sfE3AbC_1FQ-uJ-mWlixAiYBr6Fwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانفینگ
😄
©
miladiels
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/ircfspace/2438" target="_blank">📅 19:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2437">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">در پی تجمع مخالفان توافق ایران و آمریکا، خبرهایی از اختلال در
#ملانت
و پیامرسان‌های رانتی منتشر شد. خواهشاً اینترانت ملی رو قطع نکنین؛ عده‌ای اگر مدت کوتاهی از پروپاگاندا و خوراک تبلیغاتی حکومت محروم بشن، ممکنه ناخواسته شروع کنن به فکر کردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/ircfspace/2437" target="_blank">📅 08:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2436">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">فاجعه یعنی اینکه اول حمله سایبری رو تکذیب کردن، اما بعدش بصورت رسمی تایید شد. الانم نشت اطلاعات مشتریان رو تکذیب کردن، احتمالا چون قبلا هرچی بوده و نبوده پابلیک شده!
شورای هماهنگی بانک‌های دولتی، اعلام کرد: به پیرو اختلال پیش‌آمده در سامانه‌های ۴ بانک ملی، تجارت، صادرات و توسعه صادرات، تیم‌های فنی بلافاصله پس از شناسایی نشانه‌های غیرعادی، اقدامات پیشگیرانه و حفاظتی لازم را برای صیانت از داده‌های مشتریان و زیرساخت‌های بانکی کشور به اجرا گذاشتند. بررسی‌ها نشان می‌دهد حمله سایبری محدود به چهار بانک بوده و هیچ نشت اطلاعاتی رخ نداده است./ انتخاب
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/ircfspace/2436" target="_blank">📅 23:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2435">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ایرانسل و همراه‌اول با گذاشتن ضریب روی بسته‌های بین‌الملل قشنگ
عَنِ
دزدی رو در آوردن. گِل بگیرن در اون وزارت ارتباطات و سازمان حمایت از مصرف‌کننده رو، که دزدی اینقدر راحت و علنی شده. البته چیز دیگه‌ای هم نباید انتظار داشت، یه مشت دزد دور هم جمع شدین!
©
Mohsen_935
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/ircfspace/2435" target="_blank">📅 17:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2434">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Texi4ku03I19Lt0RS0lqoR3-tKlhl6im6rrkvVW6fxjYfhvGTePIFRbEgmfhSYdpeIU10bxrnuWZFzXEKQstGBuD3t_WCvhWzkOk63uuPPctBNyU3l3HWLdSX86gwzlXnPKo-_cekDMoxgeCCQk_Z_RKP_Bkt7yiZQvkeFdqzMhR8owlzOiW_wqStCw9nYYVGWAe-1uwo2M1fS36IbbjEpEXT_wJojZGpzm-a1Ln18Hf871NXvGKcIVWT2wJAs9_FrD6rj4itntqLk1o0FwrP55-39Z_9WyMGeNL35G8Z93gP9uw7ptlu-W89BsdA1C2ubMRMxqozDqtqjvtSZKdxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به دنبال بروز مشکل در ارائه خدمات بانک‌های ملی، صادرات، تجارت و توسعه صادرات از صبح امروز، پیگیری‌ها نشان می‌دهد عامل اختلال بروز مشکلات زیرساختی در شرکت ملی خدمات انفورماتیک بوده و ارتباطی با حمله سایبری ندارد.
البته تاکنون زمان دقیقی برای رفع کامل اختلال اعلام نشده است. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/ircfspace/2434" target="_blank">📅 17:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2433">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/drEuAeFfZn32h278J-wA3IY3HJX1QbzCxhiJAv8qhjr798Bd2baB_Z2vSqZ6a9roEt77olqsFl24HlQ6P4n5_njSN0aKMfl404bQjO7LgGuhktZN-CAWhJ2izr6mLdQUFmfs5UC17iIxPFkvkOXxHiWLcG1O-TG9Ph7PBtu50Df03kTC1xYa2QfxLByfANMQHuUIRB0xj9HDjod2L6QojreYJ0o-8WHeumCJaOQMKdDX_KEdWQ0_ZhzZd5ZEQmxBphsRMXkdS6Y2gQqSot5mxPIy9d4ZyBea41CXJeoM8sgncdarERP_zV7cB628AhxVkuU6-qcFGMB7d2akmtIB9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل اعلام کرد پس از دریافت گزارشی درباره فعالیت ده‌ها کانال یوتیوب مرتبط با اشخاص و نهادهای تحریم‌شده ایرانی، علیه برخی از حساب‌های ناقض سیاست‌های خود اقدام اجرایی انجام داده است. این شرکت جزئیاتی درباره تعداد کانال‌های مشمول این اقدام یا نوع محدودیت اعمال‌شده منتشر نکرده است. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/ircfspace/2433" target="_blank">📅 17:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2432">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gkPIKOYC6KzgTNJhA0iR2eV8dji1u90lJ4JkVl699Qy6sabcB3xraeiKoUEjUtbaY8XrDu0IerxNUQN9xaUt_ZBID6EIkvS1zTI_BVglRCj8qP6Z4brKCLSf8I9t99ZW9jWiABG5kk6sJVyc_xfv9bkenm7WzNQRlArKTlqR-k4JUQZ9JSv7_uNMgt42TH2qcvQysQageY-fDvEUe4aujJ4s5i8NgR9IRWQHTWSolBv5vcykhK0_iqWwEoXi4NY1DWkg5ul9YEK6X5v4XEHW7LPQqSy3pQzm0V8rmRHFIjJl0MNloIaAcaaFpXYke1cldpxXg278Yzq71XGeAaRsXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستار هاشمی، وزیر قطع‌ارتباطات اعلام کرد پیش از بازگشایی اینترنت حجم ترافیک استارلینک با کل ترافیک اینترنت کشور برابری می‌کرد. او همچنین طرح وایت‌لیست اینترنت را برای جمعیت ۹۰ میلیونی ایران غیرعملی و غیرقابل اجرا دانست و گفت به آنکه ایده‌اش را مطرح کرده بود گفتم ماستت را بخور. /یورونیوز
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/ircfspace/2432" target="_blank">📅 08:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2430">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KNA7_8ZaBvkUF7SSc1uSleQi9IHjnh5YyXEWjgXJhBYpN8I9caZ6Wyo94XCdyasQC0rrIHMfPXng2PkLs1HyycaN-IviDQpVK4905w2U-AW1W5vfu0P0sfZCWigBQ2JECyqCkUvKeeYLOg9XW-vv3kKrZnMcL2VXCM5FiZgUSVfPz2gU_4pCoF8jGYI5jg22KdeFxmxKTA-sjP_PnbjxR45-wDs50EdL7MM7vj8R2nIksrLLN14BySYr-R-G2LaNEzGJHsy8H7n5PeCdlAlH8mAUM3Rh08k7K4fkDlkEj5C_Bts6FRs1ALZRjrpFjbza2_R0OvWU-rweJJ0blnL7_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌دنبال توافق‌نامه‌ای که در اردیبهشت میان شرکت ارتباطات زیرساخت ایران و آذربایجان برای توسعه ترانزیت داده و زیرساخت ارتباطی به امضا رسید، بخشی از داده‌های ترافیک اینترنت ایران به اپراتور Delta Telecom در آذربایجان منتقل شد.
داده‌های موجود نشان می‌دهد که آذربایجان در مدتی کوتاه از رده چهل‌وچهارم مصرف ChatGPT در جهان به رده سوم رسیده، که انتقال ترافیک اینترنت ایران از مسیر یک اپراتور آذربایجانی این اتفاق را رقم زده است. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/ircfspace/2430" target="_blank">📅 07:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2429">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور گفته "نگرانی برای قطع اینترنت وجود نداره و اینترنت قطع نمیشه".
از اونجایی که دولت کلاً هیچ‌کاره هست، نگرانیم بیشتر شد!
😒
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/ircfspace/2429" target="_blank">📅 14:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2428">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VAKY8wvaQcftgiXlGTqz7sChva2-DN1HZ2TnO-XeycoeDnmQU1Dqpy6FS3NyClrBt-UJej4ZE9aIUpVCqJPbGMYJA2YnRwuDYDwIzm7hbQtCeNyvh6cacj8NtVGtfXiSsX8_FPw1StAeLvm_NjxjFZ35_T96QwwQHDsCOQptDdlupp9q5tkbNUDcyUBas4X0RA_sGUcKR-y6p4QtCkAQ6fR5gZa8mOH2aaGMMQbYvp8otouhLSV1mhmxsdStJo0jkaKibItv0AX4P-XKclsP9jpgHIiEIOO36_n1HjUCVG8ePgVkUw861mWOQlmFrGZyJhSm9IeqJrah4ngG9ZTOFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در آپدیت جدید از فیلترشکن متن‌باز و رایگان pyWarp که برای ویندوز، لینوکس و مک ارائه شده، ۹ مسیر اتصال به وارپ (با انتخاب گزینه Auto در Protocol) چک میشه و در نهایت اگر اتصال امکان‌پذیر باشه، بهترین رو انتخاب میکنه.
👉
github.com/saeedmasoudie/pywarp/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/ircfspace/2428" target="_blank">📅 08:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2427">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">هنوز موشک‌ها توی آسمونن و به زمین اصابت نکردن، پهنای باند رو کاهش دادن و گزارش کاربران از کندی اینترنت و افزایش اختلال‌ها حکایت داره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/ircfspace/2427" target="_blank">📅 23:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2426">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بعد از ۸۸ روز قطع سراسری اینترنت و برگشتن دسترسی‌ها، هنوز اوضاع اینترنت به قبل از دی‌ماه برنگشته که دوباره دارن واسه همدیگه خط و نشون می‌کشن. انگار باید خودمون رو برای یه قطع سراسری دیگه آماده کنیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/ircfspace/2426" target="_blank">📅 20:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2425">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cyohUctx8Bwy0RTYyTfd5RHCXpFZ6MmfTUAqmllQsuwhIF2_XH9VkA2DsWBQZ5Ow7wqXQIpVvnhy3QHuxsAHU9bHKoFOosAgHikYxBW2wnW3uVxroav4DzlS-SHHLATbYisJc7W18mufsW7OvH9BpJpyJaEHuiAa1BybBDR28iyq2OVo8YJXuX_MOIQa3Gd2wF9oyAv6L2qxEB_5oSaxsJf3U1T2V8xm4YSM7FdKZ_yGWc8NSoL_Mvh8YsRBbF7l-LfnVxE7OOhlIOcSYobVV4EU1n2oweAXLNkkb6HzYbZZ1E1CQByerC25jJMjIvEiaLyxK-BmhK401mu1j91zJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه
#نهان
یک راهکار متن‌باز مبتنی بر Workers کلودفلر هست، که امکان راه‌اندازی کانفیگ رایگان Vless و Trojan رو بدون نیاز به سرور مجازی فراهم می‌کنه. این اسکریپت از داشبورد مدیریتی، امکان پشتیبانی از چند کاربر، ربات تلگرام، قابلیت مخفی‌سازی ترافیک و قابلیت تغییر آیپی تمیز از داخل پنل برخورداره.
👉
github.com/itsyebekhe/nahan/blob/main/README_FA.md
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/ircfspace/2425" target="_blank">📅 08:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2424">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lHRymGFTf_I8zLork18Jx7hcf_mdN7vW738FNBlWW24kVWWKufUsibCcwm0MWnG72jv6I6mRd5yaNW0yaEhIkN7ZSe92A_XHlRKAEUpnxoVashlDY1JhoQFlHVt6cP_G9M_EulE4SpIh1dWcObnfkrXsaJaX2jZcTMu_mFsdRcyIF_sFYx55BCuYc3QOscmEbyGfYPFjCNboJ6ulbgWbwKEAynrVKov1PX8MEvoI5hfi7tHOS5_XMdHVjpLs7Ik50HMgW-VQI7zVb6LiUPx1-v4qQ8L8guKwiQ_IE9V5ukbcc4xd_RaSdybxZ0DT_PcFoMg-th_3zljh7ITTSNg9dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه موضوع حادتر از دستکاری DNSها هستش و هر روز ابعاد جدیدی ازش کشف میشه، هرچند سرقت ترافیک تعبیر درستیه. همینقدر بگم که این مساله اصلا درایت/اراده‌ی زیرساخت برای کمک به کاربران یا چیزی مثل تحریم‌شکن نیست بلکه بخشی از پروژه‌ی وایت‌لیسته، با هدف قطع مجدد اینترنت در آینده‌.
©
vahidfarid
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/ircfspace/2424" target="_blank">📅 07:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2423">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UO7wsKbLQM8hIfpQ8mz4PgKl_VRQiYLUc5_15ZoAWEym_iZIEAxfu6Ru_BZWuSReRXDKqkbLMIYxuSbrs9TVC_Z-r0qKxD1kPgvBGG0P0Fy8UeS_WNU28B8KmO4QrryKZn0IU0pLyCV8TqoRxBGlPT4DlUh9SmVZ1ktYySxsw57Dd9RRE5qdXfJyBt0TKOe9f4W9xkqfTj-4NQDS9O_qQZSW59VET7udAeqxJo0seIkw63PKndQsgE3_n0E2_Ng62rk4_tBh8IkMjiPAmKaaLrvVkB7NWg-cOM5FZm6G6b7KmjApWAVU0M8mUPUpNxK1bWxWSkN5YYUeULFPKjNUwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ GenyConnect یک کلاینت متن‌باز و رایگان برای شبکه‌های خصوصی و ارتباطات رمزنگاری‌شده هست، که با تمرکز بر کارایی، حفظ حریم خصوصی و مدیریت دقیق ترافیک شبکه طراحی شده و ضمن پشتیبانی از هسته ایکس‌ری، برای اندروید، ویندوز، لینوکس و مک در دسترسه.
👉
github.com/genyleap/GenyConnect/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/ircfspace/2423" target="_blank">📅 19:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2422">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h9mWNqNCQk0CwY1aLWoIMTTGqbstuhqe9CAfQJuO4aawGhyWG1_t0ZF1PXNXaXxN3xQvuO9tKTt8RgXOSc5ejHXjb7OxkVkbX91fYyKDZxvQGOWmkkbco2_CgPmnIKAdHgNQuz-s7oU0HZQD8Yl2DU1qCUAvLjRzPocU5ZW9hXlbXb9Cdgv1D_taNxV_79_T41XPNJBmRPbweuOccLJGI1VVI0QeCkZCCegkH49FDs6aF77a-NtfFilIsp20X_pOKmDzbM3nWs6JUI2UJ6xY5k4mbCD-84eSpUj4VKq-viK-HeBmMuhN9TJ3YMZ_g1Wxt3V3sPHIxUbvlIL0Us-8kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه آیفون از فیلترشکن
#شیروخورشید
با نام AzadiTunnel در اپ‌استور منتشر شد.
👉
apps.apple.com/ca/app/azaditunnel/id6776486891
💡
github.com/polamgh/AzadiTunnel/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/ircfspace/2422" target="_blank">📅 18:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2421">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kNrqouKvR92kXBJ1--AxiJaaNrED2Xtpo_vv8nPzNAtsiGFZJM-JeVTt-L4_Di9F-sDVJ-ys38NOHm76zEMK3874gMrzBSy9QkPcYL4oQGi9600kgIBOula0ErL5maV1oAeRvhDJEqyloFGAlLQFwiuxgODLJ6JkYc58uQ4To4_CQm_PtmUbKwmE675l6E1vgiaIx4HfuiJ8OBB34nnAl_upQ4t7bkLeLbe8nxIC8klT-24FXivKrIjgP3MIaWdN0sbsd5FMTFQ5zJoqC_RSzuznv1nJKix0c0iPYrYu_fHIRdMQgcuqulkdFnSsPs5EM2eJQk-DxXEPcFIiX6JN6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در آپدیت جدید از فیلترشکن
#دیفیکس
که برای اندروید، آیفون و ویندوز روی استورها در دسترسه، قابلیت Health Monitor به بخش ترجیحات اضافه شده. این قابلیت بصورت دوره‌ای وضعیت اتصال رو بررسی می‌کنه و اگر کانفیگ فعلی از دسترس خارج بشه یا کیفیت مناسبی نداشته باشه، برای اتصال به یک کانفیگ جدید تلاش می‌کنه.
اینطور که تیم توسعه‌ش گفتن این ویژگی از قبل در هسته برنامه وجود داشته، اما به‌دلیل اختلال‌های شدید و ناپایداری اینترنت در ایران، گاهی قطعی‌های موقت شبکه رو به اشتباه به‌عنوان خرابی کانفیگ تشخیص می‌داد و باعث میشد اتصال کاربران پس از مدت‌ها تلاش، مدام قطع و وصل بشه. الان استفاده ازش اختیاری شده و میشه فقط درصورت نیاز فعالش کرد.
👉
defyxvpn.com/download
💡
t.me/PersianGithubMirror/5927
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/ircfspace/2421" target="_blank">📅 23:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2420">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مرکز ملی فضای مجازی اعتراف کرده که "از منظر فنی، قطع یا محدودسازی دسترسی عمومی به اینترنت، به‌تنهایی مانع اجرای عملیات سایبری پیشرفته از سوی بازیگران دارای توان تخصصی، زیرساخت مستقل و سطح دسترسی بالا نمی‌شود. این دسته از بازیگران، با بهره‌گیری از مسیرهای ارتباطی اختصاصی، لینک‌های مستقل و زیرساخت‌های غیرمتعارف، قابلیت تداوم عملیات خود را حفظ می‌کنند".
این مرکز اضافه کرده "به‌عنوان نمونه، حملات مشاهده‌شده علیه برخی سامانه‌های بانکی نشان داد که محدودیت دسترسی عمومی، لزوماً به معنای انسداد کامل مسیرهای نفوذ به زیرساخت‌های حساس نیست. بر اساس بررسی‌های فنی و ارزیابی‌های عملیاتی انجام‌شده، تأکید می‌شود که اقدام قطع یا محدودسازی دسترسی عمومی به اینترنت در شکل اجرایی اخیر، تأثیر معناداری بر خنثی‌سازی حملات سایبری پیشرفته نداشته است".
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/ircfspace/2420" target="_blank">📅 23:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2419">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دسترسی به چند سرویس تحریمی مثل اسپاتیفای، گراک، کلاد و ... ربطی به آتش‌بس، توافق و رفع تحریم‌ها نداره و مربوط میشه به دستکاری شبکه توسط فیلترچی و عبور ترافیک از شبکه آذربایجان!
©
DigiHubAI
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/ircfspace/2419" target="_blank">📅 22:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2418">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">محققان امنیت سایبری یک آسیب‌پذیری در Visual Studio Code کشف کرده‌اند که به مهاجمان امکان می‌دهد توکن احراز هویت گیت‌هاب (GitHub OAuth token) کاربران را به سرقت ببرند. تنها با کلیک روی یک لینک، مهاجم می‌تواند توکنی را بدزدد که دسترسی کامل به تمام مخازن کد کاربر، از جمله مخازن خصوصی، را فراهم می‌کند. این آسیب‌پذیری از طریق سوءاستفاده از مکانیزم انتقال پیام میان پنجره اصلی VS Code و نماهای وب عمل می‌کند و به مهاجم اجازه می‌دهد افزونه‌های مخرب نصب کرده و توکن OAuth ارسال‌شده به سرویس
GitHub.dev
را استخراج نماید.
این حمله همچنین از قابلیتی به نام «افزونه‌های محلی فضای کاری» در VS Code بهره می‌برد که نصب افزونه را بدون نمایش هیچ هشدار اعتماد اضافی ممکن می‌سازد و بدین ترتیب بررسی اعتماد ناشر را دور می‌زند. گفتنی است این آسیب‌پذیری در دوم ژوئن ۲۰۲۶ به گیت‌هاب گزارش شد و تنها یک ساعت پس از آن جزئیاتش به‌صورت عمومی منتشر گردید. مایکروسافت این آسیب‌پذیری را تأیید کرده و اعلام نموده در حال توسعه یک وصله امنیتی (fix) است، همچنین تصریح کرد که این مشکل نسخه دسکتاپ VS Code را تحت تأثیر قرار نمی‌دهد.
©
Teeegra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/ircfspace/2418" target="_blank">📅 22:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2417">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/locX-CvQH0a0gklixMxZ0Gd2uLGYB90e0tAHlgi-wuucofsct0S7B7CxKMVzrh_84Gb4MukcN7n3nvS2N0C525UiZyvmnZ7Yq49kFK2ZPKtJKQlFwL4CUx_CDTRQQzDT6uNo6QY4uAExuVqZ7lNQAhNH2Hdsy0a1EG9x2O3RqiVoFxJa27vj1N1l1dfIMx6gOBL2JmnVzcVhcZ9mwvab5N3xYHmU-vQ5ZIQ2nDH3pN8lNlmBY4FM3y5eGwJYql8Y8IGP1x4Az0yB6qRWxv4O_FFLbp8Xf_8kr0UHgrTSPyt7JCsVclLPYKWW4HB9qhnmbE94C_4UxOoN0raKr-C4Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر RKh CFS یک ابزار رایگان و متن‌باز برای پیدا کردن آیپی‌های تمیز کلودفلر هست، که از IP تکی و CIDR پشتیبانی می‌کنه و در نهایت نتایج رو بصورت رتبه‌بندی‌شده برمیگردونه.
👉
github.com/rezakhosh78/RKh-CF-Scanner/releases/tag/v0.1.4
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/ircfspace/2417" target="_blank">📅 08:21 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
