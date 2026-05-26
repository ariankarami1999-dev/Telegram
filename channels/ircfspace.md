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
<img src="https://cdn1.telesco.pe/file/QP_josu7GHfRWkPFXKHMopQvK7Egin5_5Y8p1dP_7X8UpJcJ6D885Ygw1AUr73MIJwgtsJCiEQA3AynR_ljnByl5tf09tP1dD7OwoAPwiqzx9rHCfKD56r-bFF8bmK09k7gbsiRi__FMfFUWEmp6GZ2bLpvQy4JzD_baxXuYK2k5oySak7xtFiqnXik0ZCHGqNE_f7V0pdq4JMt6N2YfUqMTKtSmyBYdSFlB9LN7S-2mPTveaxdXD8UJMBz6Bztait532t0b54dgo6UgtmpAv_Dp7nwXjFrpbcO2w3sWFFoenfb8ZN_UpDsyIRjYQySxpslXCzRlCpurVnIPljokLg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 97K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 03:28:01</div>
<hr>

<div class="tg-post" id="msg-2382">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FnDZowGAQ8wLQ0sRckghIrsJYEYl6c4abB-DK24LNUiI38F_xGRg9s2wG5aqMzqum8TBMp2wmUcxXN9I43fm9SG_m_VF-5P8daqL3QLHzx8gN6-JST2qLy_BbnbDgDUec2wUFFLAfaAwcsuHJI8QAXUIiQVbMpnpgr9SjMXFwSQzdR5shDFhMYUCWZuVnBT1N9AfMNjGaI1bGqlb3wlQK5dSOFk45n53J-pbRPwQakSPUcjhpOdIQnmuRfV1oVBtbEvsLl9ZHoS1KhpeBwfHDpz-Y-B5VeN6SyR0jIZskmnCl_EOdepE0mGb1HsAyipQy7r7eRJFV1TUtXoB1ZNbRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌ها نوشتن که مسعود پزشکیان مصوبه بازگشایی اینترنت رو امضا کرده و بعد از ۸۷ روز، بزودی فرایند اتصال مردم به شرایط پیش از کشتار دی‌ماه برمیگرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/ircfspace/2382" target="_blank">📅 23:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2381">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jngf0wyZFSRFuNkEIP_QYl7_f9CkFDu7NOyYcGkZA5C9U5ZxzuQTpwR8dCgpS6_yDkeHJf4DyunEmybWhrsDRSc6-pR4NzE3BipbaHM0BPjnDo4Pz5C8Qbrp25TTPpsL3wZo2PBAKa6ecU1ILBadwpkW5M5pmEmkUuumehLr0qhg3ZEPNarRvzRoIMxhXBtVaLOzlPTfM0b_qwDN0W2SjnWFZax3ziMJd1veSfzDwFoyRxL8y0SnWKsTqId0OHKUTHAuiDM5y4GiOnpqF10S7a63FKtLD_ALK7zElHerI6ELKFsmk0mxeicbYnkdqJo_6YxAmrzon96B7NAnfG9_sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: اکنون هشتاد و هفتمین روز متوالی قطع سراسری اینترنت در ایران است؛ محدودیتی که بیش از ۲۰۶۴ ساعت ادامه داشته. این اقدام هرگونه شفافیت درباره اعدام‌ها را از بین برده و به شرایط غیرانسانی و بلاتکلیفی روزمره‌ای که منتقدان زندانی، مخالفان و حتی گردشگران بازداشت‌شده با آن روبه‌رو هستند، دامن زده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/ircfspace/2381" target="_blank">📅 11:23 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2380">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g6uzM2bRO5-TXVN3jzMhsfREcLnCN2UV5uXTWGKurEVgU4R8B8Oo2n0c7aBblTtfNjmSLTa0mgGQXSJmGo_D6bs2fl73lBUKAdvGroQi6JQ0enz3lH_rWA61bNq37sHU404AFMCBQBudiMMa0m7qjKBls7li1pGNMboqMve8ODVOz_QpgVQwFuBD6xMegTM2HkrJqc3UzKdnhWUH0I2ucotZgg1UPakiv8h1ElArjGfMZ9EdqyuJyFuDk4Ij4gfGoWeZVQ4FsFy5XwSsqiVnfWHh8GJAJIPKCuNiPxjRIClRydWKtJm9OrgwFIC0cCEV_SoiMIf_d5VX329d-p6FBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی آپدیت جدید از اپ متن‌باز و رایگان
#شیروخورشید
کار خاصی نیاز نیست بکنید! حالت اتصال رو روی CDN FRONTING بذارید، اگر قبلا آی‌پی و SNI ست کرده بودین، پاک کنین؛ بعد روی اتصال بزنین و برای مدتی صبر کنید تا نرم‌افزار خودش آی‌پی تمیز پیدا کنه و وصلتون کنه!
👉
github.com/shirokhorshid/shirokhorshid-android/releases/latest
💡
t.me/PersianGithubMirror/5515
©
yebekhe
آیا این برنامه امنه؟ قبلا
اینجا
توضیح دادم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2380" target="_blank">📅 17:16 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2378">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مامانم دچار آلزایمره، از وقتی اینترنت قطع شده و نتونستیم ویدیوکال کنیم، فراموش کرده من ایران نیستم، فکر می‌کنه باهاش قهرم و نمیرم دیدنش.
©
MaryamA89323145
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/ircfspace/2378" target="_blank">📅 08:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2377">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LAsOeZZXEAXdd795G6GA_s46klVQuwV7GuAPwVAhxHT9o0M45ffv-iEL5lEp_jeaER7gfz_V5o7k7uRKvsO8S6CopXQiY07i0APXk3bZ9Th7GDrd74jyVEefWmDXYPpohFtCbh9Xeq5l3s4zSgOJlag6tiNl2XdygyLnfyDcsdylP4zHZZD9QJrej_s9VhdzPuLYFKH940HIDz3Xa7V2YTupfRgDi66QPR7-A3k4NwyaahZb1KHGAWF3Xj_Quf1bs68mmvkJyU-raPOhk6J0ZaFGhlR4BtseFCWN_Ha5zTC48e3gwYsQjuvzNlSsnDEcHy_XR9vlxnaBV93Ld0jflg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع سراسری اینترنت در ایران به روز ۸۶م رسیده و همزمان توجه رسانه‌های جریان اصلی به این موضوع داره کمتر میشه. انگار دنیا معمولاً به رنج و فاجعه‌های طولانی عادت می‌کنه؛ مخصوصاً وقتی قربانی‌ها صدایی برای دیده شدن نداشته باشن.
Iran’s nationwide internet shutdown has now reached its 86th day, while mainstream media attention to the issue continues to fade. It seems the world gradually gets used to prolonged suffering and ongoing disasters — especially when the victims have no voice powerful enough to keep themselves visible.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2377" target="_blank">📅 08:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2376">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a874f4f669.mp4?token=INNXxogRZfJh07yb4UT_YloHRj8vVYWQII9BIWFyS5P_mFRieisfWzyCpnxQyk875RFpaAYMXlhFVXBK53HJ-XvovcBnvbLBv1a9gkf9-s8d-FXNIgSW0aI1rvu4gdQWL-z5LhpKK3brwD2Sm1p4WoGu6RGM098MZxqEebdrX2DQ_q4fZNXPrTnQ6a40W_zptFYsVk9ld-KZLRqc9LhIJFJYO0YKZMpo0OZ_au-50VldGyFIXQDdz6lM1Qs6v0KmOAwk-_LUHQssao6Vj6GUqGXhpbVQxe0wLdWpItVJ76W8kzlnUNq37jaYJuLzMmnpxMDatZhnx-qXi1pdemXX6A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a874f4f669.mp4?token=INNXxogRZfJh07yb4UT_YloHRj8vVYWQII9BIWFyS5P_mFRieisfWzyCpnxQyk875RFpaAYMXlhFVXBK53HJ-XvovcBnvbLBv1a9gkf9-s8d-FXNIgSW0aI1rvu4gdQWL-z5LhpKK3brwD2Sm1p4WoGu6RGM098MZxqEebdrX2DQ_q4fZNXPrTnQ6a40W_zptFYsVk9ld-KZLRqc9LhIJFJYO0YKZMpo0OZ_au-50VldGyFIXQDdz6lM1Qs6v0KmOAwk-_LUHQssao6Vj6GUqGXhpbVQxe0wLdWpItVJ76W8kzlnUNq37jaYJuLzMmnpxMDatZhnx-qXi1pdemXX6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازم خداروشكر كه الحمدالله، وگرنه والا به خدا
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2376" target="_blank">📅 08:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2375">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">رئیس کمیسیون تولید سازمان نظام صنفی رایانه‌ای استان تهران با انتقاد از تداوم محدودیت اینترنت گفت: پیام‌رسان‌ها و پلتفرم‌های داخلی هنوز نتوانسته‌اند نیاز کسب‌وکارها را تامین کنند و مشکلات فنی و محدودیت‌های ارتباطی همچنان پابرجاست.
حسین ریاضی اضافه کرد: راه‌اندازی اینترنت پرو و اینترنت ویژه برای برخی گروه‌ها، نشان می‌دهد که خود سیاست‌گذاران هم پذیرفته‌اند محدودیت‌های فعلی، فعالیت شرکت‌ها و کسب‌وکارها را مختل کرده است.
او با اشاره به آثار طولانی‌مدت اختلال اینترنت بر فضای کسب‌وکار افزود: ماه‌هاست درباره آسیب‌های ناشی از محدودیت اینترنت صحبت می‌شود اما هنوز مشکل به شکل اساسی حل نشده است. در عین حال، ایجاد این محدودیت برای اینترنت باعث حساسیت و نارضایتی گسترده در جامعه شده و بسیاری این وضعیت را تبعیض‌آمیز می‌دانند. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/ircfspace/2375" target="_blank">📅 08:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2374">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/msG-SxsFJK2c_GWFfzIYegQsf4lLAWEGPUo-tJZGxXr-0Q2EUWn8_i9jSzZSprLMk_iZvTxvGmL4VwY8vcGFYdRh_L6Vmm8cvXHEnvxkx2R5X9z7yfTbYTYTVeIavE5fk04HnG_YH76B843MpdZxq2QWnf-lx-HBMRTp_Cjmu_edfhm0uB_Sw-T7ypbqn7ADjH_fXO_YGsRvc-b_dcGvhJZky3NcY77B7bGnVTkp-FbRSis4LxamrJuNO_cVg7ZyYF3Bh-FF32zvpqVdi2_f40TMjmqHpG8nZZhwWEo0YuCA3GtYHgFBlhJwgaZavoUAiEexXkl_YDyff5stV0haHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۸۵ روز از قطع سراسری اینترنت در ایران گذشت!
قطع اینترنت در ایران، یک پروژه چندوجهی است. قطع شده تا بین "هواداران پهلوی" و "پهلوی" فاصله ایجاد شود و همزمان عده‌ای بتوانند روایت جعلی بسازند.
صدبار دیگر ایران بمباران شود، نظام با بمباران تغییر نمی‌کند؛ چیزی که جمهوری اسلامی را ساقط می‌کند، آن مردمی هستند که شعار دادند "این آخرین نبرده، پهلوی برمی‌گرده" ...
با تمام دشمنی‌ها، سرنوشت محتوم ایران محقق خواهد شد.
©
AmirHadiAnvari
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2374" target="_blank">📅 08:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2373">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aBvV11T771SMZeM4DUtqZ70zip5k--X8OvZOymIMHx_I9YvaGuZmxN-tXJNayix3oCPSiVvvlnRt9O2ZGHSMsyGyUcqABnD4YZuQnQPEiMYk3kuAdu4o3e27QCn81ELk-dBF5AdEM1X9JmOFfOWRH45YHxQ1rwfAtR0lDiQcpkaM7aQ33kHjkE3ASgb3ux5sVzbsyCD-ebzKYSQeWMlB4HPLBZ-LWN47TolvkO8VqMsHxNkKoKmi6Vb7y3noutP_GRiV5r32BNucoITTS5rzUuuOcAv1hkwc30eHX7ofOBFIaSv3xUuAurVRsgH0x7has9laBi7eBmuEN6MLWx-Raw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طی یک عملیات بین‌المللی، سرویس VPN موسوم به First VPN که توسط مجرمان سایبری، گروه‌های باج‌افزاری و هکرها استفاده میشد، از کار افتاده. در این عملیات بیش از ۳۳ سرور توقیف شده، دامنه‌ها و سرویس‌های Onion بسته شدن و یک مظنون در اوکراین هم بازجویی شده.
مقامات میگن این VPN در تقریباً تمام پرونده‌های بزرگ سایبری یوروپل دیده شده بود و برخلاف ادعای بدون لاگ بودن، نیروهای امنیتی به دیتابیس و اطلاعات کاربرانش دسترسی پیدا کردن و هزاران کاربر شناسایی شدن.
©
eurojust
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/ircfspace/2373" target="_blank">📅 08:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2372">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">جمعی از سازمان‌های مردم‌نهاد و فعالان حوزه حقوق کودک، با انتشار بیانیه‌ای نسبت به تداوم محدودسازی و طبقاتی‌سازی اینترنت در ایران هشدار دادند و آن را عاملی در تشدید نابرابری آموزشی و اجتماعی، به‌ویژه برای کودکان و نوجوانان دانستند.
در این بیانیه که به امضای ۱۹ نهاد رسیده، تاکید شده دسترسی آزاد و برابر به اینترنت، بخشی از حقوق بنیادین شهروندان، به‌ویژه در حوزه آموزش، دسترسی به اطلاعات و رشد فردی است. این بیانیه، با اشاره به تعهدات بین‌المللی ایران از جمله پیمان‌نامه حقوق کودک، محدودسازی اینترنت را در تضاد با این تعهدات دانسته و همچنین با اشاره به نقش اینترنت در آموزش و معیشت خانوارها، تاکید می‌کند که اختلال در دسترسی بر شرایط اقتصادی و امنیت روانی خانواده‌ها نیز اثرگذار است.
©
hra_news
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2372" target="_blank">📅 19:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2371">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G4gRdQWlW2-SwBWtwsO9fun3QsXXHXKjF59Z_1JIHDRyoDTV5G1V0YKZYeyLO3Mw0jTVmulJhxPHp2ZVfJotVV1xMQKg4NssjjGwLEsBBTAkvJvFMm8yJpI5fUWiLH_OhjoQ8ZdVKeOfmFk80h1fRGOKG7H2_WfKx2I9iY1Y_M8btOTazNbNbBZStaBB58lDhjBRAiwCkzORZ0OTq_tkH3aV-pR6-VrHwMZwm5aH1JyxoLnbyrdOrR28vQesCo0ziHyqP6Aw6wKmfpFA8ik3sMyMfNEXwdZK6xuWmc_fdHPH9tPZ9mmPL7JjJLwpxTh2nXWQuCYgfUQCBYvpNpvu1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع سراسری اینترنت در ایران با ورود به روز هشتاد و چهارم، از ۲ هزار ساعت عبور کرد. هر ساعتی که می‌گذرد، شکاف‌های اجتماعی و اقتصادی عمیق‌تر می‌شوند؛ به‌طوری‌که هرگونه ارتباط با دنیای خارج به جایگاه، تبعیت و امتیاز وابسته شده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2371" target="_blank">📅 19:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2370">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">خیلی راحت آمارسازی میکنن و میگن ۹۰ درصد مردم با قطع اینترنت مشکلی ندارن؛ به همون راحتی که احتمالا قراره تعداد ثبت‌نامی‌های سامانه
#جانفدا
از کل جمعیت ایران بیشتر بشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2370" target="_blank">📅 20:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2369">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کسانی که قبلاً کانفیگ می‌خریدن، الان ترجیح میدن دیگه نخرن، دلیلش هم تکراری شدن خبرهاست. دنبال کردن مجازی دیگه اون‌قدر براشون ارزش نداره که بخوان بابت هر گیگش خدا تومن پول بدن.
از اون طرف، کسایی هم که سیم‌کارت پرو گرفتن، خیلی‌هاشون توی کسب‌وکار خودشون موندن. چون درسته اونها اینترنت دارن، ولی دیگه کسی نیست که بخواد تبلیغشون رو بخونه. تقریبا اون چرخه‌ای که باید بین محتوا، دیده شدن و فروش می‌چرخید، به بن بست خورده و کل سیستم رو از کار انداخته.
©
NR2OH
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2369" target="_blank">📅 20:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2368">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B5AXCnQn9MVKM-ZHZRKdS5f0QSttCdUBvDzbuKSjFF5i7izlkaYXqBCidlwjcGfZ_ZY3SExAQb5fJo2NAqrkIQZZPZ1dFeeevuRF-o3xpWDDX-u5vh8R1VyHGXkHoN8Hkn0vHgacPkX4JSDFEUEZTHqyvCHbheTtizQqIqZb9_4RfxAXmE4kQHv9yZqYbHyt-c7q9HA0XVvlmwV0LTYr6p0Y9F4zTT2abjHBt1WpNRhwjTg0JuOJ4ItyL6PDdSvlvKe68yR6D8YU9LOr6wJ5RRhUKuqegcI0FSatPreVwWYbhxDrSMpx2sqbb9j_La7lNgjFcujw2znAVFaH1du36A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا فرزانگان، اقتصاددان حوزه خاورمیانه در دانشگاه فیلیپس ماربورگ آلمان، گفته است حدود ۱۰ میلیون شغل در ایران به‌طور مستقیم یا غیرمستقیم به اقتصاد دیجیتال وابسته هستند.
او به وال‌استریت ژورنال گفته محدودیت گسترده اینترنت باعث کاهش بهره‌وری، تضعیف اعتماد کسب‌وکارها و افزایش نابرابری می‌شود؛ زیرا در چنین شرایطی تنها کاربران ثروتمندتر یا افرادی که به ارتباطات بهتر دسترسی دارند، می‌توانند اتصال پایدار و قابل اتکا داشته باشند. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/ircfspace/2368" target="_blank">📅 20:09 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2367">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E8lwMgDV_lgZDZZkaFic_r_gkoNILD13EYeqJn7s3r5QMFGrBvbSJwqd1gSFllChF-ABnn4XyEaR-kYfuLTE22z2s4zzRkQyo7dVAORUv6ciXBgx7_4HiYqtqolTpgf6T9BCdPZKMXZX3g_5NRWaMQpk5XTZb-gjOQ_OXIjfyF926zKZ8XcwK_66sC133LgvQXi5iMR0IdFM4rQGTkHCLtL1A_yV8Wnldq9QkAT6RGsAG0e6UG8EcDWCb7QdMTZKD8BvgUIvmhIkHxK9rSDcXeoEExKwhIhDt3vlvwQgzN0LthHuZNXO74VrVz3ijFb3_R0QdPzP9yDduBge2LRbKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زارع‌پور، وزیر قطع‌ارتباطات دولت قبل گفته "جمع‌بندی رئیسی این بود که اینترنت به خاطر هیچ‌چیز نباید قطع بشه"، ولی یادش رفته که رئیسی با ۶ کلاس سواد حتی جمع و تفریقشم افتضاح بود.
جهت یادآوری واسه
#قوه_عاقله
، اینستاگرام و واتس‌اپ توی دولت سیزدهم فیلتر شدن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2367" target="_blank">📅 20:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2366">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">یزدی‌خواه، نماینده طویله مجلس گفته "در شرایط فعلی تصمیمی برای بازگشایی اینترنت جهانی وجود ندارد" و "با قطع اینترنت، کسب‌وکارهای مردم از جهت ارتباطات بانکی، خرید و فروش و بسیاری از سایت‌ها همچنان در حال خدمت‌رسانی هستند و مردم مشکل عمده‌ای ندارند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/ircfspace/2366" target="_blank">📅 19:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2365">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JIv2hHgFktJ-Qczc7hDwGbdmL2itqJWzk4OavI3ZbciNgqXIDgF9H3ZXocgREFO7Fsb34eyfgxqKq3o_aqMKOgUrTANaD4S0rPKYkuZSZawTEes93nhHBwfCILIH7204QimoTS5dI6YzSyUSUak13jR62zfhN-NnUwBePoq3l8_cpck-aELqYMpGx10XFJ9Phq7aY--eNB9osKoZVC7gg2H0aYQRDDpvX15siTCX_fL6k8pUyDoLWVrqvHc5YAAYtDIev-jCaEjk9im9G5fpVozrpIb-Jax9aUaN1ze2GxiK2UzQYd3vx0Io5rXPIvbyez7bi52rVUBX9dDI4GYhZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه عاقله در همراهی با سایر قوا، قطع سراسری اینترنت در ایران رو به روز هشتاد و سوم کشوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2365" target="_blank">📅 08:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2364">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گیت‌هاب گفته دستگاه یکی از کارمنداش از طریق یک افزونه آلوده VS Code هک شده و مهاجم تونسته به تعدادی از ریپازیتوری‌های داخلی خود GitHub دسترسی پیدا کنه و اطلاعاتشون رو خارج کنه.
فعلاً میگن شواهدی از دسترسی به ریپوهای کاربران یا داده‌های مشتری‌ها پیدا نکردن و موضوع فقط مربوط به ریپوهای داخلی خود گیت‌هابه. البته دارن لاگ‌ها و میزان دسترسی مهاجم رو بررسی می‌کنن و گفتن بعد از کامل شدن تحقیقات، گزارش کامل منتشر میشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/ircfspace/2364" target="_blank">📅 08:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2363">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">عضو هیأت رئیسه مجلس: تصمیمات مربوط به اتصال اینترنت فقط با امضای رئیس‌جمهور انجام می‌شود؛ تشکیل ستادها نمایشی است.
این هم خبری دیگر درباره اینکه مسعود پزشکیان نه‌تنها مخالف قطع اینترنت نیست، بلکه در ساختار سرکوب و محدودسازی اینترنت کاملاً همراه و همسو با حاکمیت عمل می‌کند؛ تمام نمایش‌های رسانه‌ای درباره «بی‌اختیاری دولت» فقط برای فریب افکار عمومی بود.
©
alirezaer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2363" target="_blank">📅 08:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2362">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/csCL_6TSwMywnsQ1SQQWaDLZq-TDO3-zN8x3KcQ1WMNBnH10yWLuu5oEs6IOW3q6ylkyvt9exQpkG-tpWKlywGdLLLPeP_9elXlEoJS8YJwYttMVtyVBEi-iy1HPj2DaLQxrQW5aYMNsL9PeXNvgXwBKi80kHxdX0RxRjIHbYV_2IRA5vhWQYdIGH2ng6mF08IzZ0aqHaIDg5vD7as3_XsvcJ6AapWLOW5BKfF43fZ60IAp1az9rJufRGyVCSE5Pyer62FWHPYGPcwTwajfKBZwh-I0-_YqLeXh7bhYU6X5dbpJsNo_58FI_6VmQXBncJqQjucp2f340ZP9GhvaLRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار نشون میده در ۳ ماه گذشته یک پاکسازی طبقاتی دیجیتال در ایران رخ داده. در این مدت سهم اندروید از ترافیک اینترنت ۲۵٪ افت و آیفون ۱۸۰٪ رشد داشته. این به معنی خروج میلیون‌ها کاربر طبقه متوسط و پایین از فضای آنلاینه. اونی که آیفون داره (احتمالا) از پس هزینه کانفیگ یا اینترنت پرو برمیاد، اونی که نداره، اونقدر دغدغه مالی مختلف داره که عطای اینترنت رو به لقاش می‌بخشه.
©
arashzd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2362" target="_blank">📅 08:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2361">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rwJ23S0BknSSpwHoEi_5ajl-0QpVeW2n-6LrWRjtKMUWp4IdrvWG5lCD_2BRgmg0WXPq34xCyh_0VRnj-CBCqBCKiuwt157-FiwL0D6L6_xQd6ERK0bdEGGQJ5gZcmuCKXd099BYkGonaetAu6dB__LAs3bDJj8--17O5gp76C00BaUpNrxdSqiCdCq5O3AbyHk_UMcAfv0WbrsB_vLBIcRR7yZb4pSAD8hampvfF6sXQr6vncUZhe7T11EnBlEfgtpynsCHlfA3sUddEloYEp3SZm99MbSoAnYfrz1S2b5p7WmcjUmLz5yKTUuJvvSzR0gJ39qc2dPG6e1q-KreHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشتاد و دومین روز از قطع سراسری اینترنت!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2361" target="_blank">📅 09:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2360">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">قطع اینترنت به خاطر تأمین امنیت، یک دروغ بزرگ است
گفته شده قطع اینترنت به خاطر تأمین امنیت زیرساختی، نرم‌افزاری و سخت‌افزاری است تا کمتر مورد حمله‌های سایبری قرار بگیریم، در حالی که این یک دروغ بزرگ است. حمله‌های سایبری و ناامنی زیرساخت هیچ ارتباطی به قطع اینترنت ندارد. متخصصان به این‌گونه دلیل‌تراشی‌ها پوزخند می‌زنند. البته نه به این معنا که زیرساخت مخابراتی ما یا زیرساخت شبکه ملی اطلاعات ما در حال حاضر امن است؛ نه، ناامنی وجود دارد، اما قطع اینترنت کمکی به تأمین امنیت زیرساخت نمی‌کند، بلکه لطمه بسیار جدی‌تری هم به امنیت زیرساخت می‌زند.
در همین مدت دو ماه و نیم گذشته ده‌ها آپدیت امنیتی برای باگ‌های «زیرو دی» یا اصطلاحاً باگ‌های روز صفر داده شده است. این‌ها باگ‌هایی هستند که می‌توانند دسترسی بسیار بالایی برای هکرها ایجاد کنند؛ روی گوشی‌های مردم، روی مودم‌ها، روی شبکه‌های صنعتی داخلی. این‌ها هیچ‌کدام آپدیت‌ها را نگرفته‌اند. آپدیت‌های ضروری‌ای که حتی یک روز به تعویق انداختنشان گاهی باعث ایجاد ناامنی می‌شود، الان بیشتر از دو ماه و نیم است که دریافت نشده‌اند و ما با یک بمب ساعتی در ناامنی زیرساخت شبکه کشور مواجهیم.
من فکر می‌کنم وقتی بحث امنیت مطرح می‌شود، بیشتر از اینکه منظور امنیت شبکه و زیرساخت باشد، منظورشان کنترل افکار عمومی و جریان آزاد اطلاعات است. اگر با این چارچوب امنیت را فهم کنیم، بنظر می‌رسد حق با این آقایان است؛ قطع اینترنت قطعاً باعث جلوگیری از جریان آزاد اطلاعات می‌شود. دلیل اینترنت پرو هم اتفاقاً همین است. اینترنت پرو نهایتاً شاید به یک یا دو میلیون نفر ارائه شود. یک یا دو میلیون نفر با ۵۰ یا ۶۰ میلیون کاربر فعال ایرانی خیلی متفاوت است و باعث می‌شود جلوی جریان آزاد اطلاعات گرفته شود و در واقع کنترل افکار عمومی و کنترل جامعه راحت‌تر شود.
چطور اینستاگرام یک پلتفرم آمریکایی است و ممکن است لوکیشن و اطلاعات مردم را در اختیار مثلاً نهادهای امنیتی آمریکا بگذارد، اما سیستم‌عامل اندروید که متعلق به گوگل است، نمی‌تواند چنین کاری کند؟ اساساً منطقی که مطرح شده، پر از اشکال است. وقتی شما اینترنت را قطع می‌کنید، عملاً یعنی تمام زیرساخت‌های رشد و توسعه یک جامعه را متوقف می‌کنید. به یک معنا، ما با این مسیر داریم گام‌به‌گام به عصر حجری نزدیک می‌شویم که در آن از فناوری اثری نبوده.
©
hamedbd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2360" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2359">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">امروز هشتاد و یکمین روزیه که اینترنت ایران بصورت سراسری قطع شده، ولی پروپاگاندای حکومت بدون لگ داره کار می‌کنه.
امروز هشتاد و یکمین روزیه که جمهوری اسلامی داره
#روز_ارتباطات
رو با قطع اینترنت جشن می‌گیره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/ircfspace/2359" target="_blank">📅 08:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2358">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cY4nSip4BuZ2Vwsqa9hVwcBApSE_MPH1RDn9-yLqrVaZX7tx2BzRCRe3WXiy1WvTsyLup3xLisGMrrjg685yfxZGCpgRLV2XdNpwdU0AmrE9NgRVMzEV1I0nlOLjZiZtqHsPbJQBRqLkxaYG6HjifCY1mTLq3yRFM6M-UeMhkslOCdRKcHy7-REhzqjQabXNhBIsDYhBICjUJ5GaQ6mU5kmwbCE5DLzeyUYARdVtAF90XDdBT-L251ZuC2mpE-677P4CeqV2OHEZKvEaIQkmPV_DveuMweFtnsq_UYnFwGPPSzQLtTerOUHhJ3UhQy_XwFSE6vfza8iNNBtMaFxlkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در بروزرسانی جدید از اپ Network Checker برای اندروید، ویندوز و لینوکس، قابلیت اسکنر آیپی Akamai (جهت استفاده در اپ
#شیروخورشید
) اضافه شده.
👉
github.com/mirarr-app/network-checker/releases/latest
💡
t.me/PersianGithubMirror/5227
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/ircfspace/2358" target="_blank">📅 08:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2357">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RjGTJQnh9XqMFa3MXk3mFHokjDLwVpYyiCEojhrOtgDz6qA-Wl3XhAxUaWj1OQYhHNJBJnhs75YYyFlS1PDGJKjT2FR-A-sJ1kLpFzhuBv3qjWYZcYsJl0bI7UfDfKYdcY_dY6eMZRDKFkajnQSJHPGckTpEsV-sr-CDOikJ-ALCAzPb9ewmB2pC7EADd9S2Uhh6yf2MTgOdmn0IVcYbUkRt545akBJddZQ2RmVCXUygu244-pwePCcU_kcKKwZeIzrvCJXyV7odwFuhE7gWe-I_GaE7B1xpE3MDWMlKD7YhML06rejvXVKCbf9KXFAAmnkvRbMhovVK-wAzW2t3mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ NexaTunnel یک کلاینت رایگان برای مدیریت تانل‌های StormDNS در iOS هست، که به شما اجازه میده کانفیگ‌های مختلف رو وارد و مدیریت کنین، وضعیت اتصال و ترافیک رو بصورت زنده ببینین، DNS Resolverها رو تست کنین و خیلی راحت بین پروفایل‌های مختلف سوییچ کنین.
این برنامه با رابط کاربری ساده طراحی شده تا بتونین وضعیت تانل، سرعت دانلود و آپلود، پینگ، IP عمومی و سلامت اتصال رو بطور لحظه‌ای بررسی کنین و مدیریت بهتری روی اتصال‌هاتون داشته باشین.
👉
apps.apple.com/us/app/nexatunnel/id6766783641
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2357" target="_blank">📅 08:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2355">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">توصیه اکید من اینه که برای وصل شدن به اینترنت سعی نکنید از سرویسهای ایرانی (خصوصا سرویسهای متصل به نهادهای امنیتی) که شمارو قبلا احراز هویت هم کردن، سو استفاده کنید.
به هیچ وجه حتی برای امتحان کردن هم ارزش ریسک کردن نداره. و به هیچ وجه هم روشهای مربوطه رو معرفی یا پروموت نکنید! اگر کردید بهتره همین الان پاکش کنید. از سر دلسوزی میگم، بچه‌هایی که از چندسال پیش در ایکس فعال بودن میدونن دارم در مورد چی حرف میزنم.
©
aleskxyz
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/ircfspace/2355" target="_blank">📅 20:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2354">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gS8cVNC6F8ij3RUvaDJ9MuCYfSbWkPmY6CZmyjR8osY5f2wwt44mGdCyu8I5MTBwdYtjHfbPEiRSR5Hsq546k-2c_3ZOkoWKyUwiXqkAXJ3HimSdKyWJhlxTFNoPD-vOzxL1OxVOd1z5c2_ziH0j9Ls56sWJH59DSfmb_Bna3cZ98aTWvPXDvxiyiK9tFDGHjKpRfSeeNmQaI8G0kirJr85OMwb3NaL2W7151iTQnkVG7QjZFAzY_xK2LM_Oay0L2p5MYQCv5RQSN5hfY3dmaAb9iYTbfJYjswmZXEpKcslYMVlJWOKbaXokSiaVh2h8z6aPgCPwOFCJADHvrR0l_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما در انجمن تجارت الکترونیک تهران تجربه واقعی کسب‌وکارها در زمان اختلالات ارتباطی را مستند کردیم. از میان ۹۴۴ کسب‌وکاری که به نظرسنجی پاسخ دادند، بیش از ۸۰٪ اعلام کردند در زمان قطعی اینترنت، فروششان بیش از ۵۰٪ افت کرده است.
اما یک نکته مهم‌تر در داده‌ها وجود دارد: حدود ۳۳٪ کسب‌وکارها گفته‌اند در زمان بحران، «پیامک» مهم‌ترین ابزار ارتباط با مشتری برای ادامه فعالیت آنهاست. پیامک در زمان اختلال اینترنت، یکی از آخرین مسیرهای باقیمانده برای حفظ ارتباط، اطلاع‌رسانی، پشتیبانی و فروش است.
حالا تصور کنید پیامک هم قطع شود. بیش از نیمی از کسب‌وکارها گفته‌اند با قطعی پیامک، افت فروش جدی (بیش از ۳۰ درصد) خواهند داشت. پیامک بخشی از زیرساخت تداوم اقتصاد دیجیتال است؛ نه یک سرویس فرعی.
©
NimaQazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2354" target="_blank">📅 20:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2353">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rng7jKozhDv5Vkw2_70vV-V6xcPMLaw0hDfs8yMY6M6w5A0uOGL2-AARsPp3DvvdKSqLo3GrMxP5ninlZsnTj7pUGhn2R3_dwZ1QFWpola5amyYSzl-wOjjSGGW-lI-SNaG5y5vPobh-z1oZ9njefFp-CsK5JH03KlkZ8iVepxxJpEpgmclcLSiy4Ni6dlV1ttC57HDnDVuddzoCSpU5_Hq137DXTvQ2I7wFr33g6Q8j1ndtHa6XivkdCwz9es93ICjRcdfom4fgbYvW4TgvNcvklkA72Poubiu5sdssG4PEAYk1sxFRPJQgpLnRaYpjrjglSoHe5z-P82ZbJB5A2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید به افتخار وزارت قطع‌ارتباطات ایستاده
شاشید
!
آیندگان در کتب درسی از تمامی دست‌اندرکاران فیلترینگ و وزارتخونه‌ای که اسمش ارتباطات بود اما ۸۰ روز متولی قطع‌ارتباطات شدن، بعنوان
#قصاب_اینترنت
یاد خواهند کرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/ircfspace/2353" target="_blank">📅 16:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2352">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o9zQJjGxzNEgyoz8uEG1jcn7S-b62NviNL1pMlutPhbI-YMBDbysmGqLjZvIUwTSMGL4LvIDo8ye_nzA-CM7ZCPKq0sNbuyJRKfbq0_9g0ft2Uwwspp9O1cbUvMf2g1baFAJ8BYCQNcJOGNQL1Y-VD32XopReDPYk4MMMEQVcf-YFKScVMimKKSH7CW9bVMER-Zh0JBC9EBBt4kNyjmzP-ID097rtiFou7HBLFgDw7HzKcJsQT53DX57FY09aAwZSONJinAMH8EusMi3HHoWKluUAk8SZVVeM_weNcrKzoDqv3ER15G5fl-v4XdYQYeGirk4eHFBonYs_fnaip-eCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستار هاشمی از پایداری شبکه ملی اطلاعات در دوران جنگ تمجید کرد و گفت: شبکه ملی اطلاعات کارکردهای متفاوتی دارد. در شرایط جنگ شاهد پایداری شبکه داخلی کشور بودیم تا ارتباط بین مردم قطع نشود و خدمات مورد نیاز مردم ارائه شود.
وزیر ارتباطات افزود: در دولت چهاردهم نشان دادیم شبکه ملی اطلاعات ورای یک شعار در میدان عمل کار می‌کند. این اتفاق بی‌نظیر و شاید در دنیا کم‌نظیر است. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2352" target="_blank">📅 16:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2351">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nRnl0PwKVzLo3sFK_jMpe2PG-o-96W32PBxBD6c5orbcljBEyWTeYpe-bkgP1FXYJdHcFLZHJbb9i9JyB6Odi63S7q6RGeXu4bgJsWfTHPWUQQdIDKW5RCQev2a2aqg1zNzI9l8MhO0Tpu0ceQrOadDnEzmGDV2I_3ijEeEsF-TyX3e9b16cG2HiuHPfJXXGQhKL0Pa8KZZgfwWp8gEpJWuAvduJsEoB-LL7wZJOJCOPoKfMvEWVhmX8txtSNShXYQMtUWWitzqyRj9vPX8VEqNmqnA5yIHQ-5Np2NuhZwnctwoRzkWCn60wr4xCxAx1RFFveR9mt8SpWVZh5SMpTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ اندروید
#چشم_عقاب
نه فقط یه خبرخوان، بلکه یه راه آفلاین برای دسترسی آزاد به اطلاعاته، که بدون اینترنت، بدون VPN و حتی بدون داشتن مجوز اینترنت روی گوشی، خبرها و اطلاعات رو مستقیما از ماهواره روی دستگاه شما میاره.
کافیه کانالش رو روی فرکانس 10762/27500V ماهواره ترکمن‌عالم باز کنین و دوربین گوشی رو سمت کدهای QR که روی صفحه نمایش داده میشن بگیرید، تا اپ در چند ثانیه اطلاعات رو بخونه و روی گوشی ذخیره کنه.
اپ فقط به دوربین دسترسی داره تا QR Codeها رو اسکن کنه و هیچ عکس یا ویدئویی ذخیره یا ارسال نمی‌کنه. تمام محتواهایی که دریافت می‌کنین، قبل از پخش با امضای رمزنگاری‌شده Ed25519 تأیید میشن تا اپ فقط اطلاعات واقعی و معتبر رو قبول کنه.
👉
play.google.com/store/apps/details?id=com.filtershekanha.cheshmoghab
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/ircfspace/2351" target="_blank">📅 10:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2350">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">باورم نمیشه قطع اینترنت به ۸۰ روز رسیده!
وقتی حکومتی برای حفظ خودش حاضر میشه یک کشور رو وارد خاموشی دیجیتال کنه، یعنی مردم هیچ اولویتی براش ندارن؛ وگرنه امروز وضعیت اینترنت، اقتصاد، مهاجرت، ناامیدی و زندگی روزمره‌ی مردم این نبود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/ircfspace/2350" target="_blank">📅 09:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2349">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rGt1EWmo-z3iF_Ttw176fdPhIof1_m4SM_ZZJeWLcEzJKEGuAgS-zQY_njrvtH9wDIHVlhv_bXB833jG8jqZqVkuXA51OagMb8ZoIyWTW8sF1orXhtXQroFUtmSIRNPPzAHFQoC0VyrJd2NjD1oepNWjyoErRESZfcqfJHqfvmuJcBzHi1DsH8lxErPbg46ALtX4CigP3Q8XAgBAm_YYrhhzPnBWlnI7b7TS7TMYl0EajqwVey2UnMDNCKflmJ89XApXKuslS7uQmqZemiC_bmPVY-Z8ruBc0zpncZ2I9pd1d0wus-l_VJpzUDQwz1fqalfsuIm75qVJXE5qUc6kRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان بعد از ۷۹ روز قطع سراسری اینترنت در ایران، روز جهانی ارتباطات رو تبریک گفت!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/ircfspace/2349" target="_blank">📅 21:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2348">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CqeY3bKqqXkaHLEszuq5VcpxHCrcriyN4vwcZaiVS9nYNWpzuugUXu7mn2eE5LdXFRSQvPUWA3_a_tvzEsu70H20TC6amXl2UNUvKScxOsIYExLIjZz9J5W3fCLP_nxgqQiiind1x98kI6zIpXm1qiKVRKQ3EjVK-UHVhB3M8hygmBsWemcoEpKITKg0VItjxRElciK352PAXvJbw_9-ceHf853WCKf4Vafi_jkhGR3192FGnwEZVlWs0DMvNcowcULhxrCiUUrCV9CBJQfMRufAO7c8a0RtXqFisrXIeScOhxu1sHWIodEZknghJT9Dk3PAcNH_KmXaPlbUT-a94w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیمکارت‌های بدون فیلتر، حفره‌ی جاسوسی برای مسئولان!
در رابطه با قطع سراسری اینترنت به بهانه امنیت و اعطای
#سیمکارت_سفید
، سیتنا در مطلبی نوشته: طبق منطق فنی، وقتی با سیمکارت سفید و بدون فیلترشکن به اینستاگرام، واتس‌اپ یا سایر پلتفرم‌های خارجی وصل می‌شوید، هیچ لایه واسطه‌ای برای مخفی‌سازی وجود ندارد. یعنی دقیقاً در همان لحظه‌ای که یک مقام مسئول درحال چک کردن دایرکت‌های خود است، اپلیکیشن‌ها لوکیشن دقیق او را با کمترین خطا رصد می‌کنند. اگر نفوذ و ردیابی، خط قرمز امنیت ملی است، پس چطور با دسترسی‌های ویژه، عملاً موقعیت مکانی لحظه‌به‌لحظه خود را تقدیم سرورهای خارجی می‌کنند؟
تناقض وقتی اوج می‌گیرد که می‌بینیم مردم عادی برای اتصال به همان شبکه‌ها، مجبورند از کانفیگ و پروکسی استفاده کنند. این ابزارها با وجود تمام دردسرهایشان، حداقل یک لایه پوششی ایجاد می‌کنند که لوکیشن واقعی کاربر را تغییر می‌دهد. اینجاست که بوی یک تجارت کثیف بلند می‌شود!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2348" target="_blank">📅 08:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2347">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اینترنت برای عده‌ای خاص، محدودیت و خفقان برای بقیه مردم
امروز هفتاد و نهمین روزیه که جمهوری اسلامی اینترنت رو به روی مردم خودش بسته، تا زیر سایه‌ی خاموشی دیجیتال، سرکوب، اعدام و پروپاگاندای خودش رو پیش ببره.
چندماه هست که هزاران کسب‌وکار اینترنتی لطمه دیدن یا نابود شدن، اقتصاد ضربه‌ی سنگینی خورده، تعدیل نیرو و تعطیلی‌ها بیشتر شده و مردم حتی برای ساده‌ترین ارتباطات روزمره هم با مشکل مواجهن. با اینحال هنوز هم بهانه‌ی امنیت رو تکرار می‌کنن!
این قطعی تکان‌دهنده معلوم نیست قراره چندروز یا چندماه دیگه ادامه پیدا کنه؛ اما همزمان جمهوری اسلامی با پروژه‌ی اینترنت‌پرو هم جیب خودش رو پر می‌کنه و هم به رفتارهای متناقضش ادامه میده؛ یعنی اینترنت آزاد برای عده‌ای خاص، محدودیت و خفقان برای بقیه مردم.
در این بین، عده‌ای در شبکه‌های اجتماعی تلاش می‌کنن با فضاسازی‌های ساختگی یا حتی ری‌اکشن‌های فیک، تصویری غیرواقعی و عادی از وضعیت کشور به دنیا نشون بدن؛ رفتاری که علاوه بر نبود بلوغ فکری و ناتوانی در درک عمق بحران و رنج واقعی مردم، برای خیلی‌ها نشانه‌ی هم‌پیالگی با ساختار سرکوب یا فعالیت‌های سازمان‌یافته‌ی سایبریه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2347" target="_blank">📅 08:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2346">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gM_VHXb4-qWvhcRtGjoOcgILbSW7ZLv4Gnv6tIdVL1GYvD9O6OPe5yZ0zmmJc_cMsTG-OXUOF82LtOKSXD3f4wKvDXP-LUWGwmaMyiGAvF2D41mUTjYfFs1Mln8h1dKqDt4GwGgKNeDjtJW4c1HBDBpigzfEB174gmqTOxX1COCYMRn_kf2maAQ6Q_zVO9T3DNzEoYyUK-uegKztZV8UwASm2kZmPCBEoHvNSW1SnLARgTA_GfIzQBqH_m8XXzcRBIBJx3nW6zu4906ppE48HkeELoN8nARWSfWYFOajD87TTqevR9xiJkByNhZIUHjuVxoUervwVXf56c0hWbAuDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱۶ از فیلترشکن
#MahsaNG
برای گوشی‌های اندروید در دسترس قرار گرفت.
در این آپدیت هسته‌های MasterDNS، GooseRelay و FlowDriver اضافه شدن، قابلیت CDN-Fronting سایفون تعبیه شده که میتونه شانس اتصال رو در برخی محدودیت‌های شدید شبکه افزایش بده، امکان وارد کردن دستی HTTP Type لحاظ شده، یه سری از مشکلات رفع شدن و اسکنر DNS حالا IPهارو بصورت تصادفی بررسی می‌کنه تا نتایج بهتری ارائه بده.
👉
github.com/GFW-knocker/MahsaNG/releases/latest
💡
t.me/PersianGithubMirror/5051
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/ircfspace/2346" target="_blank">📅 23:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2345">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اپ
#شیروخورشید
بعنوان یک فورک از اپ رسمی سایفون بصورت متن‌باز ارائه شده و توسط گیت‌هاب اکشنز بیلد میشه.
آپدیت جدید این برنامه تونسته دسترسی هزاران نفر به اینترنت رو در محدودیت‌های شدید فعلی فراهم کنه و همونطور که انتظار می‌رفت، افرادی سعی کردن برنامه رو به حاشیه ببرن و برای کاربران نگرانی ایجاد کنن.
علاوه بر متن‌باز بودن پروژه و امکان بررسی کامل سورس و روند بیلد، متخصصین حوزه امنیت و افراد فنی آشنا با ساختار این نوع ابزارها امکان تحلیل دقیق رفتار، ترافیک و عملکرد برنامه رو دارن؛ نه اینکه صرفاً بر اساس برداشت‌های سطحی، حدس و گمان یا خروجی‌های بدون اعتبار AI، درباره چنین پروژه‌هایی قضاوت بشه.
در رابطه با تفاوت این روش با MITM هم توضیحاتی از طرف توسعه‌دهنده برنامه منتشر شده که پیشنهاد میشه مطالعه کنین.
روش کار کلاینت شیر و خورشید کلا متفاوت هست و اصلا MitM انجام نمیده، که نیازی به سرتیفیکیت داشته باشه! دلیل اون روش این بوده که بیرون هسته سایفون میخواستن ترافیک رو در v2ray تغییر بدن، پس باید از سرتیفیکیت خودشون استفاده میکردن (که در صورت بی احتیاطی نا امن هم میتونست باشه). در شیر و خورشید تغییر تنظیمات SNI و ... که روی ترافیک ایجاد میشه در خود هسته سایفون اضافه شده. در واقع اگه کد رو بررسی کنین میبینید این قابلیت Domain Fronting چیزی هست که خود سایفون در نظر گرفته بود، ولی تنظیمات و قابلیت تغییر درستی رو برای فیلترنت امروز ایران در نظر نگرفته بودن، که الان در شیروخورشید اضافه شده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/ircfspace/2345" target="_blank">📅 23:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2344">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dt-WT2Wt7KEXIGRsxfvPDcpGQVQoKTfP_xINdjcb9QijsCBIToQbDmv5hzcsnPHBdNXOWSS51TVsEN0AlXXr6bBYfTopd31nrp7E2A2EX3H7YIuUmRwJLkb-Nc-2gfFk2ajUuNRmu6JIzbFbRyXPBVqiH-ccXSbjig3_x2Q40G_w2R5xoG64uKLawvK48aGsVYFQMPxO3BXsXQ2ORiMoMLuYlrJoR2F3KBwIu_OOyxAigAKqrqRS6J-eeWFGi-76dSkDh_rTGecSVVGa1ale5dIR5ZIS1gOWNDVeytlxuZbGDx4sOTqMTNLpRrEK8n_FeQiEw74bZju-M39mYXnTWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتن هرچی که تهش Hub داشته فیلتر کردن؛ حتی گیت‌هاب.
قوه عاقله‌س دیگه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/ircfspace/2344" target="_blank">📅 09:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2343">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J8iRXMc26ui1FTFoUgx64osxPXQ7ZP8CzDV1WjRV2xcFQOXYxwwiVH2DssPM9bKGlb-eefLRhU7EXvdbARV67SmtaYJ2f3d2Qr0Sz-zG22F818eb_XqESfknj8n3Cz-UVqs98Xj4U5I9fLYkzOCGzWxFsw5CWQ67jT-HWCf6hDvg3hRkuio9asSVAfV_bm5Zs2xCh61WFwNhwA7f-zFKhGJaDLGm9QsFFjXZpM5i1vuF-tKK99m6QKvNQnGC05asn1ZH6msAPBW1zutD9VA1MzFTlP5AgzdK5xEajKH32wBHR6RUlAZEPE5H-fNYhFfwtZWPP79aa15J5amQCK5oMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ متن‌باز و رایگان TunnelForge یک کلاینت L2TP برای اندروید هست، که از امکاناتی مثل حالت VPN برای کل دستگاه، حالت پروکسی با پشتیبانی از پروتکل‌های HTTP و SOCKS5، مسیریابی، پشتیبانی از چندین پروفایل همراه با ذخیره‌سازی اطلاعات لاگین، بررسی وضعیت اتصال، امکان استفاده از DNS سفارشی و تنظیم مقدار MTU برخورداره.
👉
github.com/evokelektrique/tunnel-forge/releases/latest
💡
t.me/PersianGithubMirror/5008
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2343" target="_blank">📅 09:11 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2342">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nkLWJ8AC5qgVrN9U2z3SDaLl_kwwEAjS5zUQkLo5AQhQdKgAvzvGh0I6N8Wo7zzDJbeXGdSYJ8lLk1ITF8kKF7GhKZuvZrglc-wj0RawpQqHrguWgKwV-XtourbaehktdB_tlGpYyM3zoU9OTGTnljTs-DoxPvXAXgOe1hTBaNgVcNH6md4lQ45qAfxMgJ3oySTka4oRDFOX6JtsVU2RjkYOV3xlFjeKfWBfw_lyH1GKJ2MDTKWCdVdokdK7DBUsPk3PLY6cEUgPMYHfH9GpQ4NLSC5M2PKHgNCc1a1Vxa3HkgawCBQhDyO93tAcDkyDgDxJW7q6tTDF-w5S8LI2Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه آسیب‌پذیری جدید به اسم YellowKey در سیستم‌عامل ویندوز پیدا شده که توی بعضی شرایط میشه BitLocker ویندوز ۱۱ رو با یه فلش USB دور زد؛ البته فقط وقتی مهاجم به خود دستگاه دسترسی فیزیکی داشته باشه. برای کمتر شدن ریسک بهتره ویندوز و BIOS آپدیت باشن، سیستم کامل Shutdown بشه نه Sleep، و برای BitLocker رمز یا PIN قبل از بوت فعال بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2342" target="_blank">📅 09:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2341">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pQF0B5qSsvLxbOjOMWcDDeGMk6ZmDt_dqx3_H4M5ud1yO5l6Jo2mlBfb6LHm8HYVzmGYuDdQqKXbbeEteCjla610ifI4VF0KHypBnONuBg6xE3U93bfFx8oZsZqm0kCybJEoe7s0I8nZO9dOc0z3kFYrd-rHVt5YkvNI4tRFDLFQtx9_th1I9q_vqIoblV9-htwEjFNFUw-ey4SVIiCEu_L6tJC1VcepWD3S0FQ6U1qC3GVhYI0W8mnbFJ-HMU8ko36Wvi2reJ2obPNw0U2H7k-E4GRxXCRKbzlPF-VBS_wO0ZSC-62keBiOlCGej2zQ0qmrTdYqDJkdO_vhwFmKdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استارلینک مینی به ۲۰۰ دلار رسیده که فعلا اشتراکش هم رایگانه. کنترل اینترنت با اینترنت پرو و قیمت‌های کذایی یه توهم زودگذر هست!
©
imanraisii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2341" target="_blank">📅 08:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2340">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dgqIw9a8xAL7-QAReZ84XV2oHQsV89g6R01ngpSw85fvhg6It9meiLk8D9085HCyteE8DWwpBtw60NvWvBfpWn2KzVuMN9ck6DzrlynpUZdOq_KkyT8ar0M9O3pJ7I2DJDfbwoB2aR7ILnjPaihn6e2MvfsapjwLd4JgBnFKeidQPtjpHGxo649FfS1oITRpSX2WGob03D3UghYSWB3axwx1i7XNImGk0v_ZAKnJF4H_lYBKXurWTybEtMjn3uSHpIuu7UaeNJ8tryWzjXSH0azJpP44JXT8L2GJ5moRipB6dQbB3aRPhy5poC9SxPlpppQhtkEAkkr_qvU4sFMwhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در هفتاد و هشتمین روز از قطع سراسری اینترنت، از جدیدترین روش ترکیبی عبور از فیلترینگ با ذکر "لعنت بر جمهوری اسلامی" رونمایی شد.
😁
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2340" target="_blank">📅 08:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2339">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WU2H0qfQQbU3A-FIAj8ZC_sCj32HCoZxbyoWq_cVL1IXhdGn5_ZVk_0MW-_fgwrTO8LscDc2aDfTrVTDPj6EsbqdcFFgjofgKVE2qc2jCeQoc2dsO7tiZyRdv0TM8Hou5t0Duuw-ejilUzj3ZQ6ebtwlFVxuKDNaRojF8YsymN4njW8hI4W-v2oqhXxaPOi0xqpl2UBmB3pWDV8wCUJ88ui4OfhMQM_OudAksG2M2Lg2uC-lk1fiyiNNV7n7_GP230GbXIlQewKTltDafV1k4LUqbrAihVuAsHzFBMblYpHvGlB1asdymHA4PmoWLA9JjXR8Zq6ZzAgVUnJR2snxgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشتگ از تبعیض بگو!
اینترنت غزه که قطع میشه، اتحادیه بین‌المللی مخابرات میاد محکومش می‌کنه، ولی وقتی که اینترنت ایران برای نزدیک ۳ ماه قطع میشه، سکوت مطلق! ۱۰ ساله در مورد ایران توییت نزده!
©
markpash
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2339" target="_blank">📅 08:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2338">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SJRYt0Dp_zHjZtE8MSEfygo0lGtT_TUj1ZR0l7nuTlUbs9QuuYQi1XuW49t4HVX_W4hmbni6PzGJSL7mZ2LotH3YWmjha7x8c2oPonWga89ORZcbKMRjJQo6J4Hylt1B2PTja7U9f4qJ567iqoMdjICB2fjH4s5MCdCY2Ss45K7RroKhibJzr9PBe7i5RlVQMEeF8_zgmaZcwDhBpu-KSjLyaAqkxPiaskZoGENyq1fsZJzgewsrtYUwOnnZ7Xh30T-zIqTemkamjZyZ9_Usv-vjW-dr0_pabkQJnEkbbPppGa6ptJObv3W8-cL_IQJX5sc-3tEPCOjhPqb-dwGmcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد حساب این الاغ [توی ایکس] بسته میشه، داد میزنه که آزادی بیان نیست...
©
AminSabeti
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2338" target="_blank">📅 08:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2337">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">تقابل اینترنت و امنیت یه دروغ بزرگه. مردم نه‌تنها  دسترسی به اینترنت رو به امنیت کذایی شما ترجیح میدن، بلکه هر چیز دیگری که خلاف ترجیحات شما باشه رو هم به انتخاب و تصمیم شما ترجیح میدن. شما هیچوقت جسارت برگزاری همه‌پرسی در هیچ موضوعی رو ندارید.
©
vahidfarid
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2337" target="_blank">📅 08:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2336">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ستاد فضای مجازی با مدیریت دکتر عارف در اولین روز کاری برای افزایش رفاه مردم و تحقق وعده‌های دولت وفاق ملی، گیت‌هابو فیلتر کرد.
©
pey_74
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2336" target="_blank">📅 08:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2335">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z81bbJuLdlTvneY2A8RBw94L0CxfM_dBr4ha6-SkDJtPgVv3QC1ihKBR4uaq1d3gB_4TpeGrEfS0IMhvC2vgXyhXqu_QH4_Qoq5wAtpagUITnTJm0pzkp8AjgMZDM7E6hMRtE2JC7nxP7EpHupTKgaJVRqeBSWDibPug_kYhiG0Mhp8pCKeoN5ICXYiSuEpcMvw1JIt2bavZHTeJw7crgyiKEWGyVxuN3MbH_OOe4CnTUP9aMu5XIKilZy4Zwdwaro0YZW0MxJp4MoZYnoYKEp4NV9DG4eVRx9RTjmH4edsAoojGEcsSgT0PfjB5Z2uRKVTV-QeHljgQBtQ69fuEdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش
MITM
در آپدیت جدید از اپ اندروید
#شیروخورشید
گنجونده شده و می‌تونین بدون دردسر ازش استفاده کنین.
برای استفاده بعد از نصب یا بروزرسانی، باید وارد Options، سپس More Options و بخش Connection Protocol شده و CDN Fronting رو انتخاب کنین.
همینطور در قسمت CDN edge IPs اگر IPهای وایت‌لیست شده
Akamai
رو بذارید، سرعت اتصال بهتر میشه.
👉
github.com/shirokhorshid/shirokhorshid-android/releases/latest
💡
t.me/PersianGithubMirror/4954
©
PawnToPromotion, mahdavi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/ircfspace/2335" target="_blank">📅 16:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2334">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نحوه اتصال رایگان و نامحدود به اینترنت آزاد با متد ترکیبی MITM + Psiphon
👉
github.com/patterniha/MITM-DomainFronting
©
patterniha, MatinSenPaii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/ircfspace/2334" target="_blank">📅 16:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2333">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">روز هفتاد و ششم از قطع اینترنت.
معاون دفتر پزشکیان گفته "درصورت برگزاری همه‌پرسی، مردم امنیت را به اینترنت ترجیح می‌دهند".
وقتی گفته میشه هدف از قطع سراسری اینترنت و خاموشی دیجیتال مسئله امنیت نیست، دقیقا مطرح شدن همین اراجیفه که به جای نظر مردم به افکار عمومی تحمیل میکنن.
زمان زیادی از کشتار دی‌ماه نگذشته. به جای این چیز خوریا، بهتره یه همه‌پرسی بذارن تا وضعیت مشروعیت جمهوری اسلامی دستشون بیاد!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2333" target="_blank">📅 09:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2332">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wl7BtxEP0elGN6RlLuT60-U8Mp3uMaTwz9OZF8yHWAc6E8yPS7FpeTRKbW9pDwP8_bh6F0WgGYH8ifIWHXXigEZTyfIUbOdcPq3u5P-Fox2AWbfxdBUnhkUC5fYHE_gOho5O2Cudda1TlVX8Mpa1qnjiQYEZCFhASA7qaDSVLvLXfqKdnH0jFv9MQafByphky0NLBvz760NR2arZXoaWDtpwU4WVCsjSQ2rNx7cehprdY5vhbbdAQ-LuPlPLK0JaYkIExhRtu6bq_WvCC9VYc-ejHcVnA4p6K952huKI53NzFAQKWKLXlbA2npBC5OiUe8Jo721oXWhaEoC12_tnsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون فرهنگی مجلس: امروز پیامرسان‌های داخلی گوی رقابت را از پیامرسان‌های خارجی گرفتند.
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2332" target="_blank">📅 19:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2331">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fmyqlq50wP3bYjrdOjqNQ0zapgXJgkjxYe_AFSRzSn9EPkGf2Ea9lfQVm-Ap5QTmlgMwC8HbOq_HSolbDVbuaUD6r50JxyD2DX5Ts0U29whIfkDwZwxlSK3YPdHUU7tlukmsK-XlHRnoB2z8FqDUvZYD7LBzNV2wzu7x4z44c0hxsJFYI3S3MlGVCjg9vqhf15UYfc-r3roWaLrwu7EoG43x27_3iWHa9Ki79MasLgRKOTOfPz-vWau9csnOd6KHGsfGdL6BmMO6Qc0SivVZoVWZ1itxi0nSRQLxhR2rxjcknhPgA95dKj0QSjU-se0i-pKrGifJ92wP5MNqVmxQeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷۵ روز از قطع اینترنت گذشت؛ همزمان درآمد یک کانال فروش فیلترشکن از ۱ میلیون دلار گذشت!
©
mosi115
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2331" target="_blank">📅 19:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2330">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/obiM29m0go_WS4ynByr7PypCRU0iYprLNMxAT4f8plcijXty8FKrcQ4JXxJDM2sAkiud_uZ0r0FbEenbS-ZUWgT8M65c93I7LE0ZBIKE-wpcWBr_MoCIU0oPVjTaQqH4HVF3zHxMRRnLLsAwwJyKu1KXkU3EoEgGqgXYFoBH7pvEYF1LzU3ickb7DLayldy5dTTokzSVMd2XBlS_phI3MMJSPwpK_L8ZadLf3p4nqfVVK0TJ-bxPrlSSiHECKO0WLsfND4F6wxJ78IGcRds1RPe4FvEbe88rjWbRH_YJbGV-F01bti18eyUoHt8Elr5Y0E7UMCwrkjPt769dfyMCuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میاد مرحله‌ی جدیدی از
#اینترنت_طبقاتی
شروع شده؛ دیگه خجالت هم نمیکشن. قدم به قدم دسترسی برخی افراد و کسب و کارها وصل میشه، تا عموم مردم به عصر بدون اینترنت و بدون هوش مصنوعی برگردن.
©
vahidfarid
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2330" target="_blank">📅 19:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2329">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سی‌ان‌ان در گزارشی نوشته
#اینترنت_طبقاتی
در ایران خشم و نارضایتی عمومی رو شعله‌ور کرده و به نمادی از نابرابری ساختاری در جمهوری اسلامی تبدیل شده ...
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/ircfspace/2329" target="_blank">📅 19:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2328">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">قوه قضائیه در یک کشور مردم سالار آنجایی که حقوق مردم با تصمیمات دولت یا نهادهای امنیتی نقض می‌شود واکنش نشان میدهد. در ایران رئیس این قوه نه تنها حق مردم در دسترسی به اینترنت و کسب و کار مردم برایش مهم نبوده، بلکه چندبار شاکی شده چرا اینترنت پرو را سختگیرانه نداده‌اید!
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/ircfspace/2328" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2327">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=CoQACARMjeYZZ4zUATklhKoZOaEHnKv_00ZQKVMst7ZdZ9AqwWwxBLkfwmddcoqeC7SU_voZKS1EmGwd3C27yFvrMFj6Hy93e3PF71PfREAAAKT7oLGKX0YdrgV7wh8IxnUeuzqrgUeIQoBmKBJYbsiMWYlffXetoRrQ5hZ4PuXl0tWNlh4LCAWLaTIgPxrKTpy_p-HIWUBPTjslWYRTCy8L3zTZcrLfYLUXTvE6OPcc57fphoTOgggtJB9bnmw-wHEkAoJsO37IVJUNSHJP6Wn_g6iT09pwKT6qVEuILza3BQbkSthD5CxourDQPjvbvM_Y4Ndql_gcBa5Hr5r0BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=CoQACARMjeYZZ4zUATklhKoZOaEHnKv_00ZQKVMst7ZdZ9AqwWwxBLkfwmddcoqeC7SU_voZKS1EmGwd3C27yFvrMFj6Hy93e3PF71PfREAAAKT7oLGKX0YdrgV7wh8IxnUeuzqrgUeIQoBmKBJYbsiMWYlffXetoRrQ5hZ4PuXl0tWNlh4LCAWLaTIgPxrKTpy_p-HIWUBPTjslWYRTCy8L3zTZcrLfYLUXTvE6OPcc57fphoTOgggtJB9bnmw-wHEkAoJsO37IVJUNSHJP6Wn_g6iT09pwKT6qVEuILza3BQbkSthD5CxourDQPjvbvM_Y4Ndql_gcBa5Hr5r0BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگر هکر بودین و میخواستین بانکهای جمهوری اسلامی رو هک کنین، سرورتون رو کجا میذاشتین؟
علی کیافی‌فر، متخصص امنیت اطلاعات: در جنگ دوازده‌روزه، نوبیتکس، بانک پاسارگاد، بانک سپه و بانک مرکزی از داخل خود ایران هک شدند. مثلاً نوبیتکس توسط یک سرور زامبی واقع در یک مدرسه‌ی علمیه خواهران قم هک شد.
قطع اینترنت امنیت رو کمتر میکنه و نه بیشتر. سیستم‌ها نمی‌تونن آپدیت امنیتی بگیرن، سرتیفیکیت‌ها expire میشن، ابزارهای دفاعی (فایروال، آنتی‌ویروس) از کار می‌افتن و هکرها (داخلی یا خارجی) راحت‌تر کار می‌کنن، چون نظارت و لاگ‌گیری مختل میشه.
©
farhad_mottaghi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2327" target="_blank">📅 19:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2326">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c5bCPiPlcf_Dzc1xUnmWNKnI6kPWtah5QrbrXBo90SujqY6dmaIXLSGDmmQOl1Mod4BSJ5m1xLiF-3Rv57hRIB3Ba7djAd7Xm28v-qXvAbySoVBw4bmB3C5xFhQ22Q-fnx6fXx8Y3lFIiuLzpO4d8kcrLLfTEOejT5mR6P3LhGZTIMORJwOYcFK4P7-YR_iW0-3xH-15GHOtv5ctmTXLKTaNadoPZIFI8s4e-meStdedS8Vwek_JYkjVP7H9EEvJwwu-55xWRgyGPue1XHWYPVGDcOT0TNYPP9z2YV61CTdHbhwR9L4RYATQXOaGuJ5ajw27dv5cI9bnoQ7NV9pEPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آگهی یک دفتر پیشخوان دولت برای فروش
#اینترنت_پرو
©
mamlekate
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/ircfspace/2326" target="_blank">📅 19:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2324">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mu5Kc5bL7H3EUUAWykt46Rq-jhhYGRQU_c4QyD9H4U68ZXXhMFBjouCYq5dJUJQLoFkqkdcc-lnCo90WyprwhIb_UoozX1XfGTi0-nrFBLazG7W47tqdyRUJhF93pQF7WSdT-ti1HBvOZ38YA-bmQHAUdN-3n9JhSI5X1C2rlZ175IjjJrRTA4m_ofmmkqwhOQFQ1Om8xByuw6P7TtMjQ3xyAPt9oGyUOuf7m0L1OCtJoPKOxMJ5e9QbsY-8jfKTHW0PFDQkFOa1DJmi_tLQPw5pNxGz4PfiuIEhl6DD7sUhzRlW5Nd1Gd4pWvSaZLXAg81ruPUsp6rwMD5e7K3HDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا دسترسی آزاد به اینترنت در متن سخنرانی‌های رییس‌جمهور و هیات دولت برقرار شده!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2324" target="_blank">📅 10:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2323">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تعداد کاربران اینترنت پرو کمتر از نیم‌میلیون نفر است!
تا امروز یک اپراتور با ارسال بیش از ۴ میلیون پیامک، برای بیش از ۴۵۰ هزار سیمکارت،
#اینترنت_پرو
فعال کرده و اپراتور دیگر با ارسال بیش از ۵۰۰ هزار پیامک، حدود ۴۰ هزار کاربر پرو فعال دارد.
©
aghplt
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2323" target="_blank">📅 08:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2322">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lb4-X0Zy6AcFA-K6Zdgb3m-b-ScCF8XSgp2Az9_dxXoILetePYJIL97W6iDWJLSkzwJI0ryZL01KtOYBfdu3WLv1F5Aya8IsJkIyzlxmtgPGCpk1XYOmmXy-U2vP4HGq08SbiyHKig7jUyfmRnxuqeYsdYywtPALv0B9juDfolPxHy6wdFK_h-cmalcHxyAnY3JAZWf4M7N17vk26bRk40WtjOQy5_5_e8ZdmoBOEXXhgLYgWxavS_hNe0tfxSygI492nxV747pVWsLXBB7yNkGFvKRzoMSR9v8g8854vi_LSmygX4IVwCtCpel7ORYib96UcLzcX1IPgwy6kgnbGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن مهندسان نفت برای دریافت
#اینترنت_پرو
واجد شرایط شد.
۷۵ روزه اینترنت رو به بهانه امنیت به روی میلیون‌ها ایرانی بستن و هرکی که کار و زندگیش به اینترنت وابسته بود به خاک سیاه نشوندن، تا
#اینترنت_طبقاتی
رو اجرا کنن. مدیونین اگر فکر کنین کیسه دوختن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/ircfspace/2322" target="_blank">📅 08:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2321">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بدتر از قطعی اینترنت فکر اینه که سالها درس خوندی، دکتر و مهندس و محقق و پژوهشگر شدی، بعد واسه کار علمی دسترسی به اینترنت بین‌الملل نداری؛ اونوقت حمید رسایی با حول و حوش دو کلاس سواد برات تصمیم میگیره تو اینترنت نداشته باشی، تازه خودشم تو ایکس وله!!!
©
NiHa_Mehr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2321" target="_blank">📅 08:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2320">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZfuJVPvVX_YCsI89fa91Tikv_i9NwHw1zt0_V9P8zPpD8k0oz0OeDaUCfCVHvhSqIn2RzVd4c1IqLAnz8TAjR7jl0plcX8_2J9fHz49MA1gpX3LyeA6KOZxJfkeda1k5XZJ1YV8RWJ0CMmtz3Ev15sEu9QRMNEoEaEJOKrIdOuKoMyrVZsaoBhp3YT4F0r44kShPeeE46X11BcyBd2KgS0NVjlpcghQ-VmXL2-p5lXOOP5RIYjUrwdGg3ehwW4CMbuwrCwrpYZXS8GVr0vXKMmWMOYNBPhnHYGbtoavqFSinAw5S5XAdOKBRiEskEVZrAwTu_AY9edIfHIYUbSPudQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس قوای سه‌گانه کشور در واقع ۴تان، که یکیشون به نام
#قوه_عاقله
نه توان قانون‌گذاری داره، نه زور اجرای قوانین رو، و نه در جایگاه قضاوته. مهم اینه که قوه عاقله قصه ما با
#اینترنت_طبقاتی
مخالفه و قراره نقش اپوزیسیون داخلی رو در این مضحکه بازی کنه!
©
nimaclick
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/ircfspace/2320" target="_blank">📅 18:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2319">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DuhdBr2qZVXs44bFn39W_jcIkVXOElMCn4T4zrjLj7WWoEYZcNQ1bwIBSxgqhaDJTX4Jadbb3fSgFIDO2cXlBrS8KyfPGkaDSAYuOImhJ8zzF4ct11qIUpLfS1QuU5-aoOalbK-ezuY1v0pNPorJl5bg9dQ0NAG7djBvKiws9ojoPwxasAAYwUtXpReUQJtaq87DEoTr1WDNseGeyIFpW5aJ2fAHnrSv68jLyHof9k5FHxcbJBLoyljyXsmPlbjrw-ynxsbcD0Coe_bJhkhkQyW8wzGrVrJtW8ctSNIfuv24Jk8D9lEdnuVxSKO7Y_9Y1IrBjAyvT9Ig9HyjUS1SGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پای
#اینترنت_پرو
به اتحادیه صنف اغذیه‌فروشان و مواد غذایی باز شد و حالا با ارائه پروانه کسب و کارت ملی میتونن از
#اینترنت_طبقاتی
استفاده کنن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2319" target="_blank">📅 17:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2318">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UCH113GoJ-EpGIXsfyxvebT84-8dYW7oVH_K-6wvons4RDh10UWzK2TyznghE-BJi5JPBDycCR3xrItwXcffS7cF-sZwmMhpbIATkVyKBGAcnHSmP9xPLPu2ze1R_1vQ3zDe0vNsJD31fJIgwDl4vEeqlLpOJ47mD5O4ts_ua7-2D5EkA7AMZ8dA5_bmb8Wi8OtPFiy87K5TZkSRixvBfVVrs9hr35VDIhUU07KQuSYRbzO7U9fdL9mN7U-cPv6R3XfuHPqkv0p9FL71f14E4V_mdRQUPGELkwW867PqY1ALFkiV4KBOAT8q3btbP9CruTLuu-pkrD_QA4tp-kORyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ متن‌باز و رایگان TunnelX برای زمانی ساخته شده که کاربر نمیخواد تمام ترافیک در سیستم‌عامل ویندوز از VPN عبور کنه. با این برنامه میشه فقط برنامه‌هایی مثل مرورگر، تلگرام، ابزارهای توسعه یا برنامه‌های مشخص دیگه رو وارد تانل کرد و بقیه ترافیک سیستم رو روی اینترنت عادی نگه داشت.
👉
github.com/MaxiFan/TunnelX/releases/latest
💡
t.me/PersianGithubMirror/4816
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/ircfspace/2318" target="_blank">📅 16:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2316">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/csdE2I_hlQPshqNhHWixfrOYLKXpe0BtKPDC9nvg5wdJlWpZ9AfzwQo03i0zuyL2r9c3a2w6ORgWtZE4yLfwhgtsuJlxgO9D3W3ySykHb2CX-SKFDifH5eoCYw-RKnH2fYlK4PY5SYWgvXK8RSmYkI4Rt58A8bf-RyEczNX-IEhU0OgfURAKFYPy6aBhxhPENyKPeDhQgE6GQ6q0kCo8hU0FMnggLkEP01OFpxV9tEwuLr9BgVzkniJ0l_b3ZTzhBhdhjMoDHpqKS_OtJY3BgJj4-TFFUHUOEEs1Em7fYBj29QsLTuhX4InOn9wR6jx11wrh6lgZ6KOS35P0U-K0ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر اینترنت غزه، اوکراین یا هرجایی که حمایت از آن برای حامی‌نماهای حقوق بشر "ویترین اخلاقی" داشته باشد فقط ۷ روز قطع میشد، دنیا را روی سرشان خراب می‌کردند؛ اما اینترنت ایران ۷۴ روز است عملاً قطع شده و آب از آب تکان نخورده است.
فکر می‌کنید اتفاق خاصی افتاده؟ خیر.
ضریب دسترسی واقعی به اینترنت آزاد در ایران به گواه نت‌بلاکس به حدود ۲ درصد رسیده؛ میلیون‌ها انسان نه ۷ روز، بلکه ۷۴ روز عملاً در یک زندان دیجیتال گروگان گرفته شده‌اند و همزمان که جمهوری اسلامی در پشت پرده به سرکوب، بازداشت و اعدام مشغول است، آشغالی به نام "اینترنت پرو" را به‌عنوان راه‌حل به مردم می‌فروشد، که عقیم‌سازی عمدی دسترسی آزاد به اطلاعات و نقض آشکار حقوق انسانی و حریم خصوصی شهروندان است.
ظاهراً برای جهان مدعی آزادی، فقط آن دسته از رنج‌هایی دیده می‌شوند که موضع‌گیری برایش هزینه‌ای نداشته باشد، یا چشم‌های مردمانش رنگی باشد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/ircfspace/2316" target="_blank">📅 10:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2315">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RI-GAyzY0mie4BLWlelzGTExVIbN1gbM8KREUv8HbznMrHqjm_lhhD1PeW1PcKpIMJCnYT6RZVellvnQWEbM9ndRugDimjhfuuqyB4QmmYJjdDa__COAysIzfDdMQl0CzI6CCypnHifXjEGMKiJF_eO4gtqrg2l4rhAMV6njDUzi0M0oze2e4d4iFHEKalx2bHUAt9Xt3j7mg5hnnkDDVcQG7U3Fzmc3LKFGhINP4PH_MmlP8lND9KNFjeRxIa33HEgTKUkGDoPQI97iO1uKRYzrAUs9DgxZs6keWKKSgktKJMN_AwUMqceZpgtNnsUb05zVnZbe0cU-aP1mY53hGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در روز ۷۴م از قطع سراسری اینترنت هستیم.
وزیر قطع‌ارتباطات گفته "در تلاش برای برقراری اینترنت بین‌الملل در اسرع وقت هستیم".
نتیجه عملکرد و تلاش ۷۴ روز اخیر این فرد از خروجی عملکرد یه مترسک داخل مزرعه هم کمتر بوده و جالبه با اینکه از بی‌خاصیتی خودش آگاهه، حتی بصورت نمادین دست به استعفا نزده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2315" target="_blank">📅 08:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2314">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W-atS88EWb8GqqJLn-6FRkb5uhOjhqMhNcLZsc52GUB0bhRfwkJQk8Pxp9fIJKtDAPwUNynfsXvnqZO-uqk21gcQcKhKo8PWjMBroGKR7SpdXiZ58UB7gtiSL5wqLqRMW_6YIxmhmCia11cV4rl6x2Jlw-XREr6361VqSPn-z1BJOoluM6L8x0VyXUw3qWtQGpy8qCLeoYgBG-KhgBbuYSIJbVrNuF2JOqEOqlFePDaJtdlRvejAiKE19MwEGKL8azDFPJl4clx8oHR9uP9HF4Pn1aXUR2pioJ0oXI7crxgWhgAibcWQxOUEfPX_MuCuaWZeXLNAd0E-Xz4K5nMdBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ادامه روندی که نشان می‌دهد تصمیم‌گیری درباره اینترنت و سطح دسترسی کاربران عملاً از دولت خارج شده، وزیر بهداشت برای رفع محدودیت دسترسی به پایگاه علمی «پاب‌مد» مستقیماً به رئیس مرکز ملی فضای مجازی نامه نوشت؛ اقدامی که بار دیگر نقش کمرنگ وزارت ارتباطات در سیاست‌گذاری اینترنت را پررنگ کرده است. /شرق
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2314" target="_blank">📅 08:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2312">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ouBUZYeWE5wVRDbB0cCbfwAnvcjwsVHnFu1qLXoxhT-LAwiK0fa45FeNtOKTCIu4dP8839ks3r0RQ3jpOpm4bIZflVccdAio4oij6lQLV0nN77FkriXiUlqb_4PU2EeGniUzrKTCtMIOKZzjFaadpHwVrDuyx2VUErHG9elUZpMN8S61NFb52IBPLVHaZfWivNtyz29Rti6PBcoh-wfL3Z5E_8f8Unsm3FLRjclgvaMjyq_ApQrhfKEPMgpXDo4YO3ac1uHw_chdIkWkWVoUPnfW92-7dzkzFVMYgxRm-kTSqyhXQh7Lq2AFj3zHbVD6-ad6RWDKL1a9PjwdgCh1Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت AIO Downloader یه ابزار متن‌باز و کاربردی برای دانلود فایل و محتوا از سرویس‌هایی مثل یوتیوب، گیت‌هاب، اینستاگرام، ایکس، تلگرام، گوگل‌پلی، تیک‌تاک، پینترست، ساندکلود و ... هست، که فرایند دانلود رو از طریق GitHub Actions انجام میده.
این ابزار طوری طراحی شده که در شرایط محدودیت شدید اینترنت و وایت‌لیست فعلی بتونه بسیاری از فایل‌ها و لینک‌ها رو دریافت کنه، بدون اینکه نیاز باشه سیستم یا سرور شخصی برای دانلود داشته باشین.
با توجه به اینکه این پروژه به GitHub Actions متکیه، بهتره برای استفاده ازش از اکانت اصلی گیت‌هاب استفاده نکنین و ترجیحاً یک اکانت جداگانه بسازین.
👉
github.com/ProAlit/aio-downloader
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2312" target="_blank">📅 08:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2311">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XQF1x6jJ6GwGr8GySObqqLvykLoFK7EO-2giavMJW1MQrWAEL7j6IbCcnpeLrJwA4r0av6q74rRsf_VDYu35xKtEO5otuSQNtkE5ZwyOPVOQSbBKd4BRF8x1YpZH95kZCj_geNPooNqITYaQf44-GJSCdJke0jX79GnBZvpBmyXWHu0m61chMYN2-XIGASYItJVpG_6gzhEjCJ8eNH5tBWLQwip88rFwr3_aoXBhepG2i70ndDSf15pcX6C0HhZbuGaelq2uoaFpbLjiCr285NCtithMzJuUwJABGUgzlDD29FEMg5wRkXUB_wKZP-IWesowTUix84Cvl5Se6vmy0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پیامرسان_بومی
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2311" target="_blank">📅 21:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2310">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G7LJyOTE_q7Khxa-dpTZ6EmUIa7gKV4wgbSvNIx0Rq8dBbqIyoT1KD-4t_8Y0lSTivWYUf04baAQ9wTmiEfxBFlPCI7xFVb9YN1YOabRmwAirOaFnL5TvToJ_na-EWOgYbqM0TeKDVenQDZjlSUZ7hxzVhbzCCpmpHTYtiiBcCRYj26gy5X8U9mk1G6y4LAkdLarlImMiuA0VZRaCupWLaMmsYYYvudyf5bssnkN_OA03MZdKuNjYDk56SL4v0xLh1wsDprUDdZ5ec8_oUnvuxVdZ4dcp898ORFbnWbXcML5aqAZUxJf9B3vfjx0A-s5OjiYIMqnV1HFFOOBe_3W0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیگه رودربایستی رو کنار گذاشتن و بدون ثبت‌نام و بدون احرازهویت، بابت پیوستن به پویش جان‌فدا ازت تقدیر میکنن
😁
کی به کیه؛ اگر آمارش به ۳۰۰ میلیون برسه هم تعجب نمی‌کنم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2310" target="_blank">📅 21:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2309">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">تا الان توی هیچ پستی نگفتم که به پروژه‌هام دونیت کنین، چون حس خوبی به مطرح کردنش نداشتم؛ ولی شرایط همینطور پیش بره احتمالا سر چهارراه نشسته باشم
😂
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/ircfspace/2309" target="_blank">📅 21:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2308">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">قبل از شروع جنگ و قطعی اینترنت درخواست فیبر نوری دادم و حالا اومدن نصب و فعالش کردن.
با تشکر از شاتل بابت سرویس خوبشون؛ در واقع قبل از نصب اینترنت نداشتم، ولی الان با سرعت خیلی بیشتری اینترنت ندارم.
©
itsmralii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/ircfspace/2308" target="_blank">📅 11:45 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2307">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TIjmLKpCHzBPx9W4Wsmc-Lgk1iMGWt0vTgPLx4O5JZT2WaW1XlAcgg6Qg9_sGkEmQ2Dg0rk-Gr7vKrls3AM_e7VQKZE_RIDR1k_0mAa6yvlwgVmfh3KJVmpufus3qYjGpH5fLPpSFn_CIWnA6QasSQruOI_BP8cWWaxYvcLFG4U7BugGPOBnAA-MUKaN7_6Po4yuIWbN-EqAjZVDkGjrcZY5lR3JMefdTzFH6NLMRtiN2BQvxJjEhlkwwVbw1J6vQfyd_yCECneEVOGHuAqrMAP2l70cysld_yEUTym4Y5OwNV5vdemxbRdYPrRsLGD1t0Bp3ath7kvJsp4ltvvtBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس‌جمهور از وزیر ارتباطات بابت هیچ و پوچ قدردانی میکنه، بعدش همون وزیر از رئیس‌جمهور قدردانی میکنه، بعدترش همین بدردنخورها دسته‌جمعی از مردم قدردانی میکنن؛ اما تهش می‌بینی ۷۳ روزه که اینترنت قطع هست!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/ircfspace/2307" target="_blank">📅 08:13 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2306">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rRmMt2vC6AW8T9MZ9_FrnXEi_Fffs_-ZJsjZL1btKwSFv52EzazyRQTDCpPgJxSoBpg_-2Wd3vh08pW2pwDX4RwxgHxqTxswvDo3WSvMziCfR-Yy9fwhcMchk8pnTP6qPBj7D5B7R7xIw6EKtwqy36lTOtbGhncBPmRSIs63Gj40KXXxMVxhv4lkJ7FwafiIUG0InT_zdaCj5Bz5idT9vWuxS5SO5R9OAxTk71e0G5qndkhGVp1KmVFQ0Ye1qmF74sSKG-DLHEZdKD9pJ1hii326Dd4dGEw-0wVGngT-oyI7F6aJiLzrSurGh2hcY7RzWvE1-0_0594S0k2RzwdrlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ WhiteDNS یک کلاینت متن‌باز و رایگان برای اندرویده، که امکان اتصال از طریق DNS Tunnel رو با دو حالت Proxy و VPN فراهم می‌کنه. این برنامه با تکیه بر MasterDNS و StormDNS طراحی شده و میتونه بدون نیاز به تنظیمات پیچیده، ارتباط رو از طریق تانل DNS برقرار کنه.
👉
github.com/iampedii/WhiteDNS/releases/latest
💡
t.me/PersianGithubMirror/4637
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2306" target="_blank">📅 16:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2304">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DleO2GzRTWYLWSaFozaI44P-6iJ0hMsDNw5hIJaeL49cjmRINFSfMs5XTHD6AqwSdB_JQq7ctRXlXQArjEorOqMWvluZBDrJ1PV1zBCmwLhiyNb4CiDfR1bhzKQBy-iN96WYdvFxh1xaNVcAqADOJUE5QIQrEpX8T2EPusjPgGQdqH8yVPb_M0iNDato-W-eN5NrsWWLrVKUiwU-k-G6MXwIRNj_ZwVmuWTlNUlhBDgcBazqNy2wxNEBuaZ3n1OFOAcPL0MigES8rroGo8OozxUXrM-MU8DOHIsNOQRfk9SMVQuL03xTt-3T9OdVVhgzQKPm5v0xVWd6L4-zjAhOEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز که نت‌بلاکس عدد روزهای قطع سراسری اینترنت در ایران رو اعلام می‌کنه، یه عده میگن "خب شمردن که کاری نداره، خودمونم بلدیم".
ولی مسئله فقط شمردن نیست؛ مسئله اینه که نباید این قضیه عادی‌سازی و فراموش بشه. اگر فکر می‌کنیم راه مؤثرتری برای اثرگذاری وجود داره، خوبه؛ ولی سوال اینجاست که چرا تماشا می‌کنیم؟
۷۲ روز گذشته و هیچ اقدام جدی‌ای برای کمک جهت اتصال آزاد به اینترنت انجام نشده، کسب‌وکارها نابود شدن، آدم‌ها شغلشون رو از دست دادن و سفره خیلی از خانواده‌ها کوچیک‌تر شده. مردم برای یک اتصال معمولی باید میلیون‌ها تومان از جیب خودشون هزینه کنن و در عین حال بخش بزرگی از نهادها و جوامع حقوق بشری نسبت به تداوم قطع اینترنت، سرکوب، دستگیری‌ها و اعدام‌ها سکوت رو ترجیح میدن.
در فضایی که همه‌چیز خیلی سریع به حاشیه میره، استمرار در اطلاع‌رسانی خودش یک کار مهمه و همین گزارش‌های روزانه امثال نت‌بلاکس حداقل باعث میشه موضوع قطع اینترنت در ایران کامل از توجه‌ها خارج نشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2304" target="_blank">📅 12:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2303">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">این هفت کابل اینترنت جهانی در خلیج فارس رو اگه قطع کنید خیلی خوبه، اونا هم مثل ما اینترنت نداشته باشن، بلکه دکان‌های حقوق حشری صداشون برای اونا دربیاد و یه نگاهی هم اینور بندازن و دل ما هم خنک بشه!
قطع کنید.
©
ehsan_369
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2303" target="_blank">📅 12:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2302">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XEBxVaXtw2LMvC7J8iD7_uo10ROZ8txAuhgYatcy2uOoKgYvwEyKl1Db_1NOXHEkZeCGWIO9B0NqadX69mwyzvRrWUXGu41aeEMQi19RQs3jt3YTJG_9MCeXzSSPAyJ41NWz6DTamp0Y_z_ydalfUd6hTN_pP-flIqXe1qZPRUs5zykp7ZVfSD01EYLZWukjaBTuBu7VQ9tAl60nkjQyiIP2s5jdfk_UD1Aer3lzQ3cnpOFMXZ9-tWbpAIyOgIn-i7TZu-kTteOe2f-YPKpjPqFNTlUv4Fgk8SurOnfiTH4AdUHYei1w9gqbcXaF4NSGnK2mEl-aeVW94xaRvDFG6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسنیم نوشته تنگه هرمز فقط مسیر نفت و کشتی نیست؛ بخش بزرگی از اینترنت و تبادلات مالی دنیا هم از کابل‌های زیردریا رد میشه، که از اونجا عبور می‌کنن. پیشنهاد داده ایران از این مسیر پول و کنترل بیشتری بگیره؛ یعنی برای عبور کابل‌ها مجوز و هزینه تعیین بشه، شرکت‌های بزرگی مثل متا و مایکروسافت مجبور بشن تحت قوانین ایران کار کنن و تعمیر کابل‌ها هم فقط دست شرکت‌های داخلی باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2302" target="_blank">📅 12:17 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2301">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mqb7GlUNmlPs3H7ofGxGFAmk_HJVMsape4_7WiIxOETF_O5YHLmHA_WehxakKz7l1zphyJtoF6jOIVxiryhfkrF1vztUL-LEIARKp3BI7YMkuBP56oRhuQohPC7elWP0pZiOR4W62yi2ov6g1IVczyrF9icF5woGKrfn2OwoP8oYG4KsvuMnw-UzZFr20zZw6lUMJzjj67nbe_Byva71DfgLUh6Sl5yddct41CUws8-_YgnWhRGVEqJ8rUuvSGySJVN8NmzwgE8K5BdXBtccWTdW1a52yl4pB1udHCoR-pls_yss4hmXAVq-Wi9tVR-5iSEUgNcGVOnSUy_tTkWWmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع سراسری اینترنت در ایران وارد هفتادودومین روز خود شده و هیچ نشانه‌ای از بازگشت گسترده اینترنت دیده نمی‌شود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/ircfspace/2301" target="_blank">📅 12:07 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2300">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hsW2yQbFOdTlCBgjoy2XJMugJ4bvDw5NO_lDMFSLxg9ETw7W52bre2DP_j1Qgys1YYFbl9xNdv1-JvBOg10RYWXpCVfyEE6ChaKXsawtZ_y5THuTBkwEgpXtFjh8MagIeNE1Jnr8IuCWquECO9MRPqMQcvA6JRAyH-cnJ8rp53eGiDGGkMaAP7leVIjJICdHdPoKIcAeQp3NNKExTceXoEraqYKp2MaL90PGbm92pMAref5LluX4aNCT2TLj8HaDZSEsILrHcK5cfVRf28QNtX3zXuPz4QKdRhG8H1kZxI9gONDXxb66mMN4pGP8evE2zbCf4BVkvihO70LnJurMTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۳ از اپ متن‌باز و رایگان TeleMirror برای "دریافت آخرین مطالب کانال‌های تلگرام در شرایط محدودیت شدید اینترنت" برای ویندوز، لینوکس و مک منتشر شد.
در این نسخه نمایش پست‌ها بهینه‌تر شده و مشکلات مربوط به کش تا حد زیادی برطرف شده، بخش تنظیمات به برنامه اضافه شده و امکان بازگشت به تنظیمات پیشفرض فراهم اومده. لیست کانال‌های پیشفرض افزایش پیدا کرده و علاوه بر نسخه Lite، یک حالت Normal اضافه شده که تلاش می‌کنه در صورت امکان تصاویر فیلترشده رو هم نمایش بده.
این برنامه فیلترشکن نیست و بر پایه دسترسی‌های فعلی وایت‌لیست اینترنت عمل می‌کنه، بنابراین ممکنه روی برخی از اینترنت‌ها قابل استفاده نباشه.
👉
github.com/ircfspace/teleMirror/releases/latest
💡
t.me/PersianGithubMirror/4599
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/ircfspace/2300" target="_blank">📅 18:57 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2299">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">افغانستان تست خدمات اینترنت 5G رو در کابل استارت زده، عراق تلگرام رو رفع فیلتر کرده؛ اما جمهوری اسلامی تا دقیقه ۹۰ درحال آزار و اذیت میلیون‌ها ایرانیه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2299" target="_blank">📅 17:52 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2298">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QB_aYdbAuLQS0I2FexwGMw7s6FJnTtE6vMxdUkklH3JWVLZGo813EnmWpBSCEfpsjjbCSlK1ApRNj_sSFxHvIl80-AVlVmLWSEhIxyPqtN8YfhCe3DkNPoMOxHnT63E87sdPvOuqZYoMmihgg9nlMAmEXFuUN2YCuQhT1tzPFA8cjDvVLP5cWqg55iGkUrG6RVks5WvJ8u4d6GtZlMaHNmCHPiQjPpIYzwxKCvEYE4MtGT9fmiQNP_WmVJQKsz40FmjHDNr4jTY7Ef-B1IiTONPVLymwYXYdbMQiXpmveioozPfAI1L3Lo9DikJRCbb250VpClETFMGnrJV9fvEbUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی خاک بر سرتون (پیامرسان‌های بومی) که با اینهمه حمایت و در میدانی بدون رقیبِ جدی هم عرضه ندارین کیفیت خدمات دهی، پشتیبانی و توان زیرساختیتون رو ارتقا بدین و بعداز اینهمه سال سابقه، آدم نمیتونه ۸ مگ فیلم ارسال کنه.
بعد از خودروسازی، باید شماها رو هم دومین فرزند لوس و بی‌خاصیت کسب و کارهای داخلی دونست!
©
kamran_falahati
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2298" target="_blank">📅 17:48 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2297">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">جمهوری اسلامی ۷۱ روز هست که اینترنت رو به روی مردم خودش بسته!
روح‌الله مومن‌نسب (تئوریسین بارداری با ۲ گیگ اینترنت) گفته شرایط اینترنت به هیچ وجه نباید به روال گذشته برگرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/ircfspace/2297" target="_blank">📅 17:45 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2296">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dx70QJLyVbPJhyxUaKXEmBgO6CoacPJt_TUdGTuoF50eC6BD61yDCdm_UjLiTAyPwsRGOW-myGT-3FWznMkE61YfA7CrzB8w1lN1bHmEioacls3LzObjsoH1eC_vD7dZbTr5oDnIp7xNoGOUIT3nfhUn-3JxmiKwPQ3hSQQ3fSEC3PKptm3edPTuzsmaXZKPCkvNEeB1SBG1nsMQRkSOnR6qjA4vhI1o1sMEixzHPHxA77gb7U4C7tvE3JELDVSzk5Ss5A-VUlSzpKLmw516Z0jFxSSZixi2c-1KQvKPp1Uwoe1t9XaiGtIugkSlZGfdRHCfMxeuT4H9hKLu25WuEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ متن‌باز و رایگان Pigeon یه فورک از پروژه تله‌میرور برای macOS هست، که از طریق اون میشه بدون نیاز به فیلترشکن یا لاگین در حساب، به محتوای کانال‌های عمومی تلگرام دسترسی پیدا کرد.
👉
github.com/MaroMushii/Pigeon/releases/latest
💡
t.me/PersianGithubMirror/4500
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/ircfspace/2296" target="_blank">📅 17:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2295">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h5YFOTo8UHREFVI_jK9Hx462fK0e4xGfDaOAYijhKzRPnEmvMUAHw4KgLb6Yba9KSNDZeGLZStO61tMTHHaSxacjCsGbRcV_6NsVycG_Jw5kPeJwKdw0IG2t3OlX1CU1MiyvjWU5TTVMQm7R65DU86PREnco3f_DR7hnVWuFLzdCePf1qcfwp1JEpGON8O0zJQvTx2YZ4HELIf4gIigCFwL0EEiQGcn3FacaH1emcxmFYqltBu3mj2Fpt0Docc-HxYseIgb7rF9ixBr26hMou3tW3efGZLR45Cc1w7UeT01ouwzSOYNTsTPVSikTFZIMJ16FbSdcoCiyGuc4d40XbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه Youtube Sandbox با استفاده از GitHub Actions بهمون اجازه میده که فقط با ارسال لینک یوتیوب توی کامیت‌مسیج، فایل ویدیوی موردنظرمون رو توی فولدر Downloads (داخل مخزن) ذخیره کنیم.
👉
github.com/iphoenixon/youtube-sandbox
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2295" target="_blank">📅 17:36 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2294">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ugv6Rr4RFvEt4UnpE-ZFpLUtd1ufaBLcB6Sawhk_b6EvcKpTvdlS5Fqq3nyTI2xTxPC_0LOp_kza2yW-XUac4kNoj47ZeQdv1B8lRfTE-Yb-Khlw6_xtmVMmt03xff2iSSDhGQrSo6E_ujzPKRs4amDN5f537SA07G3QlzYspjtK1YyVLy6NNCfAeJbmStEdVurYRTlsC_E_Wgw_Qc3nVOp_OPEK6_4_Dv57trqlI7JmhPu_A-mVtLnv1ST_vBf9VB1qP8yVPylcn5mzuuC7QU9DzwQHT6cPp6PSxfJEXF7qSY0y93QraFl71uTxHN94oTijyYu60nULKSo6dXlNBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه گوگل براتون باز میشه و در وایت‌لیست اینترنتتون قرار داره، می‌تونین خیلی راحت با نصب این کلاینت اپن‌سورس به گوگل درایو در اندروید دسترسی داشته باشین.
👉
github.com/aleskxyz/Round-Sync/releases/latest
💡
t.me/PersianGithubMirror/4489
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2294" target="_blank">📅 17:26 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2293">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oU12WdEhZhpF4qoXwUhMYggYhKPeX44BT6i0vX4asKmeD9l-rICYDeZU2i1Sgi4a0vMXHzuh1QXN0GTzKr1qS2WoUd5H6sp9Qnep70D5oGxvRWr9_FR850VpgDuqYxkZ9H_S0_qyj9DxPOLPuFk61IfKRgqOGh94-X4SOu3T_JhgB1hd9lWvD38yh-gHzAZMi82iV5m_2NJGDHzWYF4hhMdNiPX_JFj2f1tqlbZIchtN-0r8t_SrGIYdt6_Y4BvjQ-uwgZjlhIQLtgNZRi-g6CFKh93Ufl6k8V92qBstH3pZ8ZyLUz1PO5tZU0DZksFsRDW9uuBVXifKNSrWHO6JoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید کلاینت ZedSecure از طریق گوگل‌پلی در دسترس قرار گرفت.
در بروزرسانی جدید این‌برنامه پشتیبانی از پروتکل DNSTT اضافه شده، هسته ایکس‌ری رو بروزرسانی کردن، بخش تنظیمات تکمیل‌تر شده و یک‌سری از مشکلات برطرف شدن.
👉
play.google.com/store/apps/details?id=com.zedsecure.vpn
💡
t.me/PersianGithubMirror/4496
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2293" target="_blank">📅 17:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2292">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">۷۰ روز است که جمهوری اسلامی با قطع سراسری اینترنت، میلیون‌ها انسان را عملاً گروگان گرفته است.
این یک اختلال اینترنتی نیست؛ حمله‌ای مستقیم به زندگی مردم است. کسب‌وکارها نابود شده‌اند، معیشت خانواده‌ها آسیب دیده و ارتباط مردم با جهان قطع شده است.
در سایه همین خاموشی، بازداشت، سرکوب و اعدام ادامه دارد؛ بی‌آنکه صدای قربانیان شنیده شود.
اما بخش بزرگی از جامعه جهانی همچنان ترجیح می‌دهد چشمش را بر این فجایع ببندد؛ چون واکنش نشان دادن هزینه دارد و سکوت، ساده‌تر است.
For 70 days, the Islamic Republic has effectively held millions of people hostage through a nationwide internet shutdown.
This is not an internet disruption; it is a direct attack on people’s lives. Businesses have been destroyed, families’ livelihoods have been harmed, and people’s connection to the world has been cut off.
Under the cover of this blackout, arrests, repression, and executions continue while the voices of the victims go unheard.
Yet a large part of the international community still chooses to turn a blind eye to these atrocities, because taking a stand comes with a cost — and silence is easier.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/ircfspace/2292" target="_blank">📅 16:29 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2291">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">قطع طولانی اینترنت تحقیر اکثریت بزرگی از افراد کشور، یک‌جا و باهم است. اما این بین، گروهی که شغلشان به‌هرشکل به اینترنت وابسته است، تحقیری عمیقتر و نفس‌گیرتر را تجربه می‌کنند. با آن‌ها طوری رفتار شده که گویا شغلشان "مهم" نيست. حرمت ندارند و می‌شود با زندگی‌، زحمات، اهداف، آینده و برنامه‌هایشان بازی کرد.
©
DevYara
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2291" target="_blank">📅 16:19 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2289">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بر اساس گزارش جاب‌ویژن با عنوان "تاثیر جنگ بر بازار کار"، محدودیت در دسترسی به ابزارهای اینترنتی موجب اختلال یا کاهش فعالیت در بخش قابل توجهی از گروه‌های شغلی وابسته به اینترنت شده و بیشترین کاهش فرصت‌های شغلی در گروه شغلی دیجیتال مارکتینگ و سئو (۸۳ درصد)، طراحی گرافیک (۸۲ درصد) و ترجمه و تولید محتوا (۷۹ درصد) ثبت شده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2289" target="_blank">📅 12:07 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2288">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IiK1lSRFJo6FLhWLpOwfyFH3ZcJGlO3bF7kqcdlOq3M-GUTScXcsKgVhMe74Pyw9tbMXxmDvJnMJmByxAUfE0_dO4AAHKj-rZKVhzcyiglb4tb3KreDSPA_JCghpUwNcP13Pn6NPA6vPeQojL2aNUt1h9UFqzBiWnDbb_4tFTEtIY3cuMnOZ3y-wrjqObxt1KPLXi62Att5mO7G6XJwG42xujSa-LhsDdVtEagEgs0zlnHJqrz5JxtKPhC9Ja45YeFo_qCvsfKRP_sTNrjq1G-PtXX3otui0yrCGgihAC4MMpNCZbX8hTbOZ-tLqypz64f7zHD9kEDVl0scOOIFSig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقایی شاکی است که چرا با وجود اینکه که پول داده، تیک آبی اکانتش حذف شده و ...
در همین حال میلیون‌ها ایرانی پول اینترنت دادند، اما بیش از دو ماه است که یک شبکه داخلی که فاصله زیادی با مفهوم اینترنت دارد بهشون تحویل داده میشه و از دسترسی به هزاران سایت و سرویس محروم شدند. سانسور اینه!
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/ircfspace/2288" target="_blank">📅 12:02 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2287">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وحید فرید، کارشناس اینترنت گفت: ما تجربه قطعی اینترنت را در دولت‌هایی داشتیم که به ظاهر حامی اینترنت بودند. خود پروژه شبکه ملی اطلاعات یک قدم به سمت ناامنی دیجیتال است. کسب‌وکاری که اینترنت می‌گیرد از نظر مردم رانتی است و روی حقوق مردم پا گذاشته. حاکمیت با قطع اینترنت به جامعه سیگنال ناامنی می‌دهد. /کارزار
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/ircfspace/2287" target="_blank">📅 11:58 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2286">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سمیه توحیدلو، عضو انجمن جامعه‌شناسی ایران، قطع اینترنت را از منظر اجتماعی خطرناک توصیف کرد و گفت: در زمینه قطع اینترنت حاکمیت هزینه-فایده انجام نداده و متوجه نیست چه میزان خشم تولید می‌کند. آنچه در این وضعیت تشدید می‌شود، شکاف دیجیتال و محرومیت نسبی و شکاف حاکمیت-ملت است. /کارزار
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/ircfspace/2286" target="_blank">📅 11:37 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2285">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WtwEUv5t0MDZY-OIBxKhdBqOzHgkLPDz6ngvV-pccFPpSQx1J9cAoupu7A6tNi2Tz_xF0daA87C0W7LClBvGyxYMnjWMASRXNXBG-ngwLYl3ZNO8DCZ-PSsw7TvT3O9jSEJSE6rHym92hPOA33mytQGU3VliN5dpygd4NYvYima5WzpyffYvd4iiPMpGqnkrm0gbtVLAWWXhiUzrlF_GbjvVJLDfNVtgvUn-Hu4zCc9NjfVL_0qJfSJ2NZWgVZVs3AHhpIakfe07Ta62tv3b8o50cH-AeN2qs2TTV_p6TSebfETWooo7i9J06RCRiGjND-PZwlzsicbNudxnr4H2aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای شرایط فعلی اینترنت ایران که روش‌های عمومی دورزدن فیلترینگ عملاً کارایی ندارن و اسکمرها و کلاهبردارها زیاد شدن، مدتیه یه مارکت‌پلیس برای خرید و فروش کانفیگ راه‌اندازی شده تا خریدارها و فروشنده‌ها در یک بستر متمرکز و نسبتا شفاف با هم ارتباط بگیرن.
طبق توضیح تیم دیفیکس، خودشون فروشنده نیستن و تمرکزشون همچنان روی ارائه و توسعه سرویس رایگانه. این بخش صرفاً برای وصل کردن فروشنده‌ها و خریدارها از طریق این فیلترشکن و حذف واسطه‌ها ایجاد شده و فعلاً هم برای تراکنش‌های رمزارزی مرتبط با ایران کارمزدی دریافت نمیشه.
در این سیستم، مبلغ پرداختی نگه داشته میشه و برای مدتی بعد از تحویل آزاد میشه، کاربران میتونن به فروشنده‌ها امتیاز بدن و تجربشون رو ثبت کنن و کانفیگ‌ها هم بصورت رمزنگاری‌شده تحویل داده میشن. البته محدودیت‌ها خرید بصورت رمزارز رو دشوار کرده، اما افراد خارج از کشور میتونن برای خانواده یا آشنایانشون داخل ایران خرید انجام بدن و فایل کانفیگ رو براشون بفرستن.
👉
market.defyxvpn.com
💡
defyxvpn.com/download
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2285" target="_blank">📅 11:26 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2284">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb8db45e7.mp4?token=GIWb0vAXCfQ7rPPt4uajDwh-zAPS0XKIa9HmukFq6ZW-LMx0bDUHOMRGQLl5m729gQEwLXoUP0R3frbHVYWgk2aVgFXrHIzgu2n34jpcbcuJXYULnJ7u0Zt3x1X9bph22aQWRfP-3EDmtRRy8ywsCdrLnvwpUsUP2Hd7yZyi3tQ3v6XZ_iul1cWN25Lj20zrya7lcpUjn_wT1hkhKIdgJhZ9EhL0iDWvkUn1zp17U6wxst-Mj6B3_FUUBeQPUq2xPZISSrVCeKcQY-kw7m4Ij-MgOm10uYA0atBM6mCajx15-_vPTTmeKt28rlgLOAjMP2k3keeg0Ru5zSm8NLWepg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb8db45e7.mp4?token=GIWb0vAXCfQ7rPPt4uajDwh-zAPS0XKIa9HmukFq6ZW-LMx0bDUHOMRGQLl5m729gQEwLXoUP0R3frbHVYWgk2aVgFXrHIzgu2n34jpcbcuJXYULnJ7u0Zt3x1X9bph22aQWRfP-3EDmtRRy8ywsCdrLnvwpUsUP2Hd7yZyi3tQ3v6XZ_iul1cWN25Lj20zrya7lcpUjn_wT1hkhKIdgJhZ9EhL0iDWvkUn1zp17U6wxst-Mj6B3_FUUBeQPUq2xPZISSrVCeKcQY-kw7m4Ij-MgOm10uYA0atBM6mCajx15-_vPTTmeKt28rlgLOAjMP2k3keeg0Ru5zSm8NLWepg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبقه اشراف و طبقه رعایا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2284" target="_blank">📅 11:01 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2283">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وارد روز شصت‌ونهم شدیم. میلیون‌ها نفر رو با قطع سراسری اینترنت گروگان گرفتن و بازداشت‌ها و اعدام‌ها در سایه خاموشی دیجیتال ادامه داره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2283" target="_blank">📅 08:16 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2282">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jwjU-yWxz5cKCJ92rOAg0Fkp7EdPOy9pNR633ZoIN50n8_O38Z2Z9entCOPnPzztt4hapBxTREXCjlrZMyCHGQDW6IB_AN8EAv1y6sMZwnK2B3PO_vh86t7DqK-H0saru7iCXHEkq5wED9D9CoeFwpc38zqpvTsevLpzISHfZxClnLIMKP8Gdzixz6oIesAP3ZUZVzBaz_jGHDxf7gINlMyfVZWWeW-l6-o0RYjJpAVDJ9LQI849Q7yLl0fBkmKmjTbyFKlmbmaWXZdbzcuUpdtu4j8NrHt1vaTV2zKyLXFyitxGNpUNc0LUwpRDCxmT03wurOzXIZgKv82fpslP_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در آپدیت جدید از اپ theFeed امکان فراخوانی محتوای کانال‌های عمومی دلخواه فراهم شده و پشتیبانی از اندرویدهای قدیمی‌تر، حل مشکل رندر نکردن نظرسنجی‌ها و ...، بخشی از تغییرات جدید هستن.
👉
github.com/sartoopjj/thefeed/releases/latest
💡
t.me/PersianGithubMirror/4273
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2282" target="_blank">📅 18:20 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2281">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g-WRnkNuWGqzbN0ajwJtdsqHK9Mv-Tn42Lf5pjrTg-wlNArNs9XD_zLLBrlJsLIDfFBVH3KWypeo90Os2EB0fyp03WsfE1jq0as-xbNfrTzeILfUz4B-7f6UtYfWQ2wfWUDfFST2KB0-2IlIvbYecMzLiUYQ-bUZAVSFlz10k8bZfR9YVp0-7kFObzcsRMBVp0qzw1fqq82FU9X-SFPsa_8yfmZmbWGAgUL1wOyGxup3NZB9a1t1RQd16aZEQgG4aJSaeh1PuZIMV3WTRYVvhYV_S-nEY02PGViuBzJce7EgTk0xm-LZDwCOMX34dqUfx0zOgJEPPCXC7XtK44_F4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای آسیب پذیری اخیر کرنل (
Copy Fail
) فارغ از اینکه آسیب پذیر هستید یا نه، آپدیت کردید یا نه و کدوم لینوکس و چه ورژنی هستید، همین دوتا دستور رو واسه محکم کاری بزنید و تمام:
echo "install algif_aead /bin/false" > /etc/modprobe.d/disable-algif.conf
rmmod algif_aead 2>/dev/null
ریبوت لازم نداره، ضرری هم نداره؛ چون به صورت معمول شما به این ماژول کرنل نیازی ندارید.
©
tiosus
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2281" target="_blank">📅 18:11 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2280">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">قطع اینترنت به بهانه امنیت ادعای مزخرفی است.
پشت پرده اینترنت پرو و سود حاصل از این رانت در جیب “ستاداجرایی فرمان امام” و “بنیاد تعاون سپاه” می‌رود.
حدود ۹۰٪ سهام همراه اول در اختیار شرکت مخابرات ایران است و مهم‌ترین سهام‌دار مخابرات هم “کنسرسیوم اعتماد مبین” است. این کنسرسیوم متشکل از “گروه توسعه اقتصادی تدبیر” وابسته به ستاد اجرایی فرمان امام و “شرکت سرمایه‌گذاری مهر اقتصاد ایرانیان” وابسته بنیاد تعاون سپاه است.
در واقع گردانندگان اصلی این مجموعه و به نوعی مخابرات و همراه اول دو نهاد ستاد اجرایی فرمان امام و بنیاد تعاون سپاه هستند.
©
yasharsoltani
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2280" target="_blank">📅 09:22 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2279">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">۶۸ روزه اینترنت بصورت سراسری قطع شده و در همین تاریکی دیجیتال، بازداشت‌ها و اعدام‌ها ادامه دارن.
قطع اینترنت فقط خاموش کردن ارتباط نیست؛ پنهان کردن حقیقته، اما خون با هیچی پاک نمیشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2279" target="_blank">📅 08:21 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2278">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EbEFbtMUSLGMBKsVDIcNAQxctWyOgXfkwwIreygqrfn8HDErXLB3P5ASuz3xYVlhNZNmPiIzVcQffsWywUgnlia3G4p8Z5xIxwIuDB0U-zhWrp6vHAcgBEgbXiRDxBtVnL4GYxo4T3SzTFYpu_c_SfpDJ8Gyg8an4j-oWxWGBvycRsvcg-JdHU8qPX2fiC5xd_zDP4ZG1BYlmIKZwdlvVWYnWEyqX9TFSA5z4NjG0UCzJw3UtBz-xZjwjo-sbuR_3YcfTYnFeVaaneKrFH9vjYLJ_rbgiB2RA5puuix2dlu6Mq6Jp66yQx6IC7LpAi_HrbHIqSVLrev-HDuwRICExA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۲ از اپ متن‌باز و رایگان TeleMirror برای دریافت آخرین مطالب کانال‌های تلگرام در شرایط محدودیت شدید اینترنت منتشر شد.
در این‌نسخه بیلد لینوکس و مک هم در کنار ویندوز اضافه شده، برنامه چندزبانه شده و یه سری از مشکلات برطرف شدن.
این برنامه فیلترشکن نیست و به وایت‌لیست فعلی اینترنت متکیه، بنابراین ممکنه روی یکسری از اینترنت‌ها کار نکنه.
👉
github.com/ircfspace/teleMirror/releases/latest
💡
t.me/PersianGithubMirror/4295
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/ircfspace/2278" target="_blank">📅 20:49 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2277">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s8efQB6todZx2jvrmjkNGjzzXm2wbvUkeixobAhK3nIRvcldUJOlCoT9gNAqztuNLz3oTjLL02q3xM6lPcwaAxIyYlUZZ2PJqctTvZ26v3cZZtkW2poDWhVtbEUhOZGRgY3UmqRUXQOBDAb1VPxi7i64Hd-P__o8dnxnZFBc8tCXPkaAMWggVQoSzL2-_AWOZisa93nUE5EqUBl0Syo2I394aip-w256p8kN8ntVAD6BWvK7typzxOGF1_UjMIcG5dhenQGDyHjByW6tN54ALtfCVScB5tvJROIyWQbB6_Bjd0lYPHfFdLLTPaANMwFamtl1DO1glj8ycPTI9aIk4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک آسیب‌پذیری بسیار خطرناک در هسته لینوکس با نام Copy Fail (CVE-2026-31431) شناسایی شده، که به کاربر عادی (حتی بدون دسترسی sudo) اجازه میده تا کد مخرب رو مستقیماً در حافظه (RAM) فایل‌های سیستمی تزریق کنه، بدون اینکه تغییری روی دیسک ثبت بشه؛ به همین دلیل بسیاری از ابزارهای امنیتی قادر به شناسایی اون نیستن.
این حمله به سادگی و با پایداری بالا اجرا میشه، میتونه برای فرار از کانتینرها (Docker / Kubernetes) استفاده بشه و تقریباً تمام نسخه‌های لینوکس از سال ۲۰۱۷ به بعد (Kernel 4.14+) رو تحت تأثیر قرار میده.
اگرچه با توجه به وضعیت فعلی اینترنت در ایران بروزرسانی کار دشواری هست، اما توصیه میشه در سریعترین زمان ممکن سیستم خودتون بروزرسانی کرده و وصله‌های امنیتی هسته رو نصب کنین.
©
Bamdad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2277" target="_blank">📅 17:02 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2276">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b82lASXbreTB_vIDbZF_5AbByPm8CFa3REz9Vt4AFOhetJz7iQ0cCThVlU4uF-KddNdI-juqPtcC0bcuZqaX1IH5WHiCjQy3STp876sZ1nM5FUnUCZq8Hf5J9BBjl20GxpVZP6w-KqRsY38gXjPEZuCDZmE9-2fXJjfLqdMsUHmpGTKvPYyg_V-uFodp3Hh9bQePfYtyFHqNaIJ1F_HfPRk2tgBJ88XnmfDHNG0gFq8eLEKogLGygO3psrhkJGNO27ECCv8w0oAnY9pCameStLKo2wbZRb_68gj4448m29Yir8UskuuKz7uVg47465Yj0dbViUUTyG23jFTo9JlUkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل آموزش ساخت فیلترشکن شخصی به کمک گوگل و کلودفلر از طریق متد MHR-CFW منتشر شد. اخیرا یک کاربر فورک جدیدی از این پروژه رو به زبان GO بازنویسی کرده که مشکل سرعت پایین، لود نشدن برخی از ویدئوهای یوتیوب و همینطور یکسری از خطاهارو برطرف کرده.
👉
github.com/ThisIsDara/mhr-cfw-go
💡
t.me/ircfspace/2259
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/ircfspace/2276" target="_blank">📅 16:49 · 15 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
