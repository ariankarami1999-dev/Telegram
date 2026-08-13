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
<img src="https://cdn4.telesco.pe/file/aWs6hlkp_fHhylTpVpV51xnFzklpGEyExRMIbHbfl1T7OwWuEFMI7shVEEhtYrQ880nJNoGi1gnqu3BlTt0rm3DFFL50O-l0oH5Mm6PP_KXAj1Sj5pMjXMHOh3VkmyWCZQvxBJIxJc8wbMvcU5giYocnGUwjNhCWKF8_lnmMCRkbCrChrk2CPvutjrpv3BlTRmoUjDjUHdZNJQlxZWaTm99GoHEaj_avdf70Otf2yoJZ5-sAHpaiodE5H4vhMuF6ZEgYgp25nmtzqcOGh3RbQJiddbI1EVWu85zTq02XrnGOfaFoTG5iRrsSDxNkv9sH6ujaWsEVp_KyPROyGuX3yw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 223K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-22 14:24:14</div>
<hr>

<div class="tg-post" id="msg-82160">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سیتی خداست، هر سری که تیما اون پولی که برا رودری میخوادو میدن میگه نه ده تا بیشتر، خلاصه قیمتشو از ۴۰ میل بردن رو ۸۰ میل
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/funhiphop/82160" target="_blank">📅 13:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82159">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFZYeMw8ojjPYt0Z-vzvXnqz8Ct7T-Haw78NTYUcRURdBnmhrGiSLdBQ49wYr2bD4q_BZ4UgqEx-MhxzmDpJ8PzpunG5oFXw1Bt6adHenFpNjBN8KWGESTUlnG1ZhAhQVuVdQsN8W6hAVbsPCUvEReSzlZYq2AHg7KYXCsk3s8J7OuxHhu3KajmvjYjWkmhbvxGkSdQMNPU5CfbDHWwgCf2CGwzAiBoBcuuri2wceV06_m6ipd_4FxkoIrjufJ21coN-3lY9i0iK_dhEKcmCyk64FhIN9AiCobI9titzBSRyQCoOFdyuTPWZg-aD2ZBXRpflZbP9ppkDJj6MHn40Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویرو هربار میبینم جمله "آقایییی محترمممم" میاد تو ذهنم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/funhiphop/82159" target="_blank">📅 12:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82158">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7jwxVAa8WPM-bpDpy3BlvHAer2t8aQtNwpQAn_rty9jMfaLoJLGWX-NJUlnNPq6aa-tANiV6fuWHYm59hNz8H6Df1-4f4Ky9QSD_1BWZZcfUOpFx0-mwNBO-qvwTSYro2G5H29ENenOm9qr0y_0dCh-b1BxGF0HZJl--IDl4YPf85QgakZCtbPEChzdyahiFAb6PHnzWvwIPMHeepgMYPchMBpxh0DxcPZnWNR9JfoFZsdHpAyFzQb6_DBi0M-D7jF4w9PrDwbbcxxvIV8zcTP1yCgpl2Py4SVClEPyrm0f1JPaIAf3FaQts2GqwguMHLDu-JjeqMyxGQAXWXyaiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خفه ریدم تو سلیقت
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/funhiphop/82158" target="_blank">📅 11:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82157">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e23ac6b2e.mp4?token=mdTzEdIRR6lkY1ZPTQhsbMMHrf5CuaFMw4IRdr6U2D9xFIXIbE4OEdmncmqqylohthqHTM5fanQVWidhtymF4UpfhK_U4kD4iAIpnDNBum2dVGbAnRZtdLkw8dQFu7sCHGkEHYkMo08-wN7Yk4S-R6pigwmRyPO8mLS5iKZoPWQFJ4VUhU8MCmcVBcuBrHwuF1jmAw1DVFfzSk8XFfZBrPGqoFUMEj4XVSU5OxMHFEOCNqrpSlz-klYXVlggfW2V72NqtuGYuwbtDulitxun0lO8ZWDGl3a7QlHHaKcnITFoCpC_UhUx4AMykJ29-CMIEcK6CxmMtap0yBRHx_5Bmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e23ac6b2e.mp4?token=mdTzEdIRR6lkY1ZPTQhsbMMHrf5CuaFMw4IRdr6U2D9xFIXIbE4OEdmncmqqylohthqHTM5fanQVWidhtymF4UpfhK_U4kD4iAIpnDNBum2dVGbAnRZtdLkw8dQFu7sCHGkEHYkMo08-wN7Yk4S-R6pigwmRyPO8mLS5iKZoPWQFJ4VUhU8MCmcVBcuBrHwuF1jmAw1DVFfzSk8XFfZBrPGqoFUMEj4XVSU5OxMHFEOCNqrpSlz-klYXVlggfW2V72NqtuGYuwbtDulitxun0lO8ZWDGl3a7QlHHaKcnITFoCpC_UhUx4AMykJ29-CMIEcK6CxmMtap0yBRHx_5Bmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سم آلتمن مدیرعامل OpenAi:
احتمالا تا ۶ ماه آینده، Chat gpt بتونه صفحه نمایش موبایل شمارو ببینه و بخونه!
به این صورته که کارایی که در طول روز با موبایل انجام میدین رو میتونه تحلیل کنه، مثلا وسط چت با پارتنر یا رفیقتون، کمک میکنه چی جواب بدین.
یا اینکه سر کلاس آنلاین، جواب معلم رو چی بدین؟ حتی می‌تونه تماساتونم ضبط کنه و وسط مکالمه کمک‌تون کنه!
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/funhiphop/82157" target="_blank">📅 11:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82156">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pf0OPREOcj1VtZckenoZJg2rS3dkUcZ9vLJPMzbCpvcPtrLxsbLofU_OjiqiXnTbhd4Z2XZjZwqXchVBX5YSyb-Eho9bP81bf6AfN2rrwtpCXZsHNp4-K3jOykYse3mh5wRzsqtHjswD5I_6TyIlpTsEfDRQfSJnlJiNQ4JKdLupogMpIKfGPC2yS_ypw39OqyudAsC1Lrrzoe3dRZGlqyBK0L73n75RbjSOcqUyXQ9tXn9m2m7pQDBOBS3mM7RZIt6NhH7gpBMdoRM9__xHrxFrtIndhvK6uouLIJei-ucCOFb8qtc1RW_Qs3okX7Klcq2B6_P9CnINtYLvuUOzgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
تا صد درصد بیمه ویژه پیش‌بینی لیگ برتر خلیج فارس
🇮🇷
⚽️
با ثبت حداقل ۵ میلیون ریال  پیش‌بینی میکس بر روی رقابت‌‌های جذاب و تماشایی لیگ برتر خلیج فارس ایران، در صورت ناموفق شدن نتیجه، بت‌ فوروارد با توجه به مبلغ پیش‌بینی، در هر روز از رقابت‌های لیگ، تا ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/PERG100
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r22
💻
@BetForward</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/funhiphop/82156" target="_blank">📅 11:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82155">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b33fe099a1.mp4?token=npF-rZfR1YrbW6wciOaRWEnQbDSxJavA-RXFjPsJ1XK6Sa0wOr00dRLx23OIFPhgValswoYGS89tp1M25zQCXxyyAdF1Rvaq8uvhRB_3wIIaLUqcN7nr_cbG7u7rtueI1G84xLLkXXxyLNJNY07PW1WGBx8ApEUeOgK1RzyPC3aA-wsbqEJDiCxK9tNJz_L29fdG0JaARLdBER23FZ9O7uKZzYbLs_fLklQy_EsYNcPW3iSf0ZLlg5dNPXii62aiVMOgMmZOXqh3RGdAGF1mhj0tW8rSOnL_iKUMSwBTfrrRxQeit5fKaqfudyDj8s6_UbRSKfyHNrq1jHx8fnMiPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b33fe099a1.mp4?token=npF-rZfR1YrbW6wciOaRWEnQbDSxJavA-RXFjPsJ1XK6Sa0wOr00dRLx23OIFPhgValswoYGS89tp1M25zQCXxyyAdF1Rvaq8uvhRB_3wIIaLUqcN7nr_cbG7u7rtueI1G84xLLkXXxyLNJNY07PW1WGBx8ApEUeOgK1RzyPC3aA-wsbqEJDiCxK9tNJz_L29fdG0JaARLdBER23FZ9O7uKZzYbLs_fLklQy_EsYNcPW3iSf0ZLlg5dNPXii62aiVMOgMmZOXqh3RGdAGF1mhj0tW8rSOnL_iKUMSwBTfrrRxQeit5fKaqfudyDj8s6_UbRSKfyHNrq1jHx8fnMiPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید براتون سوال شده باشه اگه سندی چت کنه چی میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/funhiphop/82155" target="_blank">📅 09:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82154">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">یعنی نتانیاهو با اونهمه قدرت نفهمیده پوریا زراعتی آدم جمهوری اسلامیه و بردتش اسرائیل و باهاش مصاحبه کرده ولی چارتا کصخل تو توییتر فهمیدن؟</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/82154" target="_blank">📅 08:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82153">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">درکل فیلم قشنگی‌ بود بشینید ببینید بفهمید تو چه کشور گوهی زندگی میکنید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/82153" target="_blank">📅 03:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82152">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe5c5e708.mp4?token=qeCC1zdxunR2yqF6HTMkBRwwa4PSXdwuA4nq3RjNaipqG89LYi3w5Zg9Hg7yXYK2XPbY6TDxZQQFAlsdfEcW4tkw-y9B-djPkdwBtUiFYISR58zmWxPxtRGCFJJc-XxMJAa7A9EupEbBUUmezt-2Fn4WIuO9g-L72T4R0AFdDI-2mYW2lOgHFbS4jcfyoUbdlIvvA4VLZd9muoyUVMhTGrQQc1GOThoRQURWRLs1pXD6yuc9LWoQ4rNDo4j54z3_-hzLIJovSjZfuoBEkB9NMLS3XFe6RHn3kXtklF-jXTKaCjbDFxA6OeNt9DpOVyeEBLFqoUIt6Jp76QCT56bQRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe5c5e708.mp4?token=qeCC1zdxunR2yqF6HTMkBRwwa4PSXdwuA4nq3RjNaipqG89LYi3w5Zg9Hg7yXYK2XPbY6TDxZQQFAlsdfEcW4tkw-y9B-djPkdwBtUiFYISR58zmWxPxtRGCFJJc-XxMJAa7A9EupEbBUUmezt-2Fn4WIuO9g-L72T4R0AFdDI-2mYW2lOgHFbS4jcfyoUbdlIvvA4VLZd9muoyUVMhTGrQQc1GOThoRQURWRLs1pXD6yuc9LWoQ4rNDo4j54z3_-hzLIJovSjZfuoBEkB9NMLS3XFe6RHn3kXtklF-jXTKaCjbDFxA6OeNt9DpOVyeEBLFqoUIt6Jp76QCT56bQRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیداد خوبه یا همین سه چهارتا تیکش تو اینستا خوبه</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82152" target="_blank">📅 02:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82150">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بیداد خوبه یا همین سه چهارتا تیکش تو اینستا خوبه</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82150" target="_blank">📅 02:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82148">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jolq_9EK0qZPmZ1llcNEN-4DDVr1coecSt1lA852sL5poq9aZnc0__Yu5YrP6QiofzI6cz31CY28B9d-LtcKdmIlgJn2KASF5vcSWQNLZt-ZSClU2kymkQhpqIgmceWRemyld4C7vyqqjdY5zeQdbnpe9cmM_nbwlWuXirRj3MTaRxIEeYFjfuP0qOJ_-IOqBLeE0gI633k53F1242oXjWUP220Lt9DeCW1Gs2asfk6HzHtjYTKtkLI_oz4EzvrK9L6UA3DfnZbbx7v3KIHOVcy_nlUVpLH7h7ZCDYLDc--TiY5fHMQU7p9GBlshw7GEW1omidT-vKhlaVQuPQY93A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf0e2ba89a.mp4?token=aMha0yo4jxJPeYPiFjnmKuKS7E-b-tZNLEYv7Ke2rfbqwQegj1ik1NXRsmuw0LTm1SJKmw3_wlZnGo6BsDi07YLY44qLxUOMv3rvsPNQqbbnaq0-HNumL7ttWljmlBnOvFEGlaR7G6XgCCYZhhH1yrmb2Y2Ap2uk2MOO0MyMyo6aB9J6UeSYkU_7bh0OeRRFQWdcb7pRBSvmVbCuW__iw58Nsbx_07Ugt6N0yJyotUTDfabNYZfBJqSt_vTZOUWtFxvzubJ29FQYd6VofyMXQyQ7mTT10ZtCSOdrsqfhLG42cXUgArcqOSuNNbsD7fLNzslEVNlioDPjAmxCDisgtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf0e2ba89a.mp4?token=aMha0yo4jxJPeYPiFjnmKuKS7E-b-tZNLEYv7Ke2rfbqwQegj1ik1NXRsmuw0LTm1SJKmw3_wlZnGo6BsDi07YLY44qLxUOMv3rvsPNQqbbnaq0-HNumL7ttWljmlBnOvFEGlaR7G6XgCCYZhhH1yrmb2Y2Ap2uk2MOO0MyMyo6aB9J6UeSYkU_7bh0OeRRFQWdcb7pRBSvmVbCuW__iw58Nsbx_07Ugt6N0yJyotUTDfabNYZfBJqSt_vTZOUWtFxvzubJ29FQYd6VofyMXQyQ7mTT10ZtCSOdrsqfhLG42cXUgArcqOSuNNbsD7fLNzslEVNlioDPjAmxCDisgtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئال بعد دوسال جام گرفت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82148" target="_blank">📅 00:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82147">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QeKB4SNRhfbHcN8oS9Y1sPKpHtO9_fFD8nR5Uh1SyxxY_lsgPLBXhQZ2S7RmrNhMR9cGoDtQE5wjniO-Nls1hiuNgRKHCTOSLTk3diKc4zNwaeiAekZJLAzzkzY8OOCOPLUqfdn-KhuXY9vBJqTlth0abByz6yrDJu-tJdEkiOpe1nz9M5jEiq0QGPPQPWXZYLhI3Iv3iRrVdt3c5QBpC4_8Y1EceMLU1JMhnP8TZzpNrzD27wLU6fCQnWiP7fe-RQnPT4bJXk97SphpKhIxEKWZFND5uxdtAVc4W7Nd-tKrzVdv70P_x2FP9KKhk_2Ny4ool7el_fwx6mipdFmF9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اوکراین هم عده‌ای از گیمرهایی رو که مأموریت هلی‌کوپتر GTA رو با موفقیت گذروندن استخدام و مأمور کنترل پهپاد‌های انتحاری کرده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82147" target="_blank">📅 00:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82146">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پاول گیفت تدی تروریست داد بیرون
🎁</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82146" target="_blank">📅 23:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82145">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">کیرم تو توپ طلا اگه به کسی جز کوارتسخلیا برسه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82145" target="_blank">📅 22:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82144">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_AsD88la0RPhb756ywGIzCpWVAMRLYSxrpaFP3O1cv_UUnEVNMc3HO3Ja8GXzOIEjh60twEistZt9LPTvbeSMV7wWAitNfXmv5cR-wZ5G5_BU5Fhv4L5_XE-ehyab6p8mMp49ZkJvwpwktH42IzJ0wxWn4uWAbaG4_f8S39fC8X0wn7w23gUoqHl0fF4jyTxoX-iippqdCfA0jwsTPpY3RlYqRHHceywdtbEdkGAnu5pQbaC44IFXUKNeULHPsKTjyhVlmjhkeq6uDKfPW9wOtYZYL5sg_V4FJEY4x28DBdjkgRGOAtBk4r0PLK_iwTFKrG6Ea_SRMhBeMaPoSK2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام به قدرت جدید فوتبال ملی اروپا, هلند
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82144" target="_blank">📅 22:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82143">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82143" target="_blank">📅 22:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82141">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاکوپینگ | EcoPing</strong></div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/82141" target="_blank">📅 22:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82140">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">البته ما کی باشیم نظر بدیم، چین برامون بنزین میخره</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/82140" target="_blank">📅 21:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82139">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">موضوع سادس، نه میتونن بنزین تولید کنن، نه پول خرید بنزین دارن، حتی اگه پولشم داشته باشن بخاطر محاصره دریایی نمیتونن وارد کنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82139" target="_blank">📅 21:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82138">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تورو ناموستون شما دیگه حتی با افغانستانم نجنگید ممنون.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82138" target="_blank">📅 21:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82137">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">داشتم فکر میکردم ماشینو بزارم خونه با مترو رفت و امد کنم یادم اومد کلا ۴ تا استان ایران مترو دارن</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82137" target="_blank">📅 21:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82136">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">قیمتا دقیق:  نرخ اول: ۶۰ لیتر بنزین با نرخ ۱۵۰۰ تومان  نرخ دوم: ۵۰ لیتر با نرخ ۳۰۰۰ تومان  نرخ سوم: ۴۰ لیتر با نرخ ۷۸۰۰۰ تومان  نرخ چهارم: ۸۷,۲۰۰ تومان (نرخ آزاد)  پ.ن: فعلا این تغییر نرخا مربوط به ۲۰۴ جایگاه تو کرمانه، بقیه جاها اعمال نشده  @FunHipHop | چمن…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82136" target="_blank">📅 21:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82135">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">قیمتا دقیق:
نرخ اول: ۶۰ لیتر بنزین با نرخ ۱۵۰۰ تومان
نرخ دوم: ۵۰ لیتر با نرخ ۳۰۰۰ تومان
نرخ سوم: ۴۰ لیتر با نرخ ۷۸۰۰۰ تومان
نرخ چهارم: ۸۷,۲۰۰ تومان (نرخ آزاد)
پ.ن: فعلا این تغییر نرخا مربوط به ۲۰۴ جایگاه تو کرمانه، بقیه جاها اعمال نشده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82135" target="_blank">📅 21:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82134">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">میگن دارن سه تا نرخ بنزین "۱۵۰۰ تومنی ۳۰۰۰ تومنی و ۵۰۰۰ تومنی" رو سهمیه ای میکنن (۱۵۰تا سه تاش) و نرخ آزاد رپ نزدیک ۹۰ تومن میکنن، حالا کاری به این ندارم که ۱۵۰ تا ممکنه برا خیلیا کافی باشه، تکلیف این ماشینایی که از زمستون ۴۰۴ تولید شده و سهمیه ندارن چی میشه؟…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82134" target="_blank">📅 21:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82133">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">میگن دارن سه تا نرخ بنزین "۱۵۰۰ تومنی ۳۰۰۰ تومنی و ۵۰۰۰ تومنی" رو سهمیه ای میکنن (۱۵۰تا سه تاش) و نرخ آزاد رپ نزدیک ۹۰ تومن میکنن، حالا کاری به این ندارم که ۱۵۰ تا ممکنه برا خیلیا کافی باشه، تکلیف این ماشینایی که از زمستون ۴۰۴ تولید شده و سهمیه ندارن چی میشه؟…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82133" target="_blank">📅 21:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82132">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">میگن دارن سه تا نرخ بنزین "۱۵۰۰ تومنی ۳۰۰۰ تومنی و ۵۰۰۰ تومنی" رو سهمیه ای میکنن (۱۵۰تا سه تاش) و نرخ آزاد رپ نزدیک ۹۰ تومن میکنن، حالا کاری به این ندارم که ۱۵۰ تا ممکنه برا خیلیا کافی باشه، تکلیف این ماشینایی که از زمستون ۴۰۴ تولید شده و سهمیه ندارن چی میشه؟ کدوم کصخلی میاد به ماشین ایرانی بنزین لیتری ۹۰‌تومن بزنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82132" target="_blank">📅 21:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82131">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">صبم خلسه اومد این ویسو داد بهش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82131" target="_blank">📅 20:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82130">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مگه دیروز تو البوم فیت نداشتن</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82130" target="_blank">📅 20:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82129">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">کچی میخواد به خلسه دیس بده</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82129" target="_blank">📅 20:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82128">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gxRxaITMWARGjCPQrbUiUVo5sQaFooy1o2t116rRKfswzOXnadhG5dn5wTX6I1tymNqGnn-UA0RKP1A24MDi7KrylrIxpKSs6gjlIV-sR1SlwUxyClPkgIqoTnLw0ahDo0jZ5uL9uXbgSM_cFAi_numvq6Ifp9bkFZZH6NPh4aC_tWwGEtAUvAlp2hEN2VwcfqXQmnYfH1SRXtSw9ZVUkwU2QMlu9LggwP91BXtuLH_iZH8WW0487ygnoNCuYL4MGLvl6gJCl1qY-VZ-lC6BuVSzLNdNPtwkJI7T8W8wLuuovFsddNag-c6IbwGUYhi0CciiQaCHCtXaLG-inHUIrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادت باشه اولین چیزی که توی استایلت باید بدرخشه، موهاته.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82128" target="_blank">📅 19:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82127">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4765f0c41.mp4?token=Gvr8cCVl_-mXb_ClkAg102lqpFKIRhJMyiqp4BHKeiidBQMhB_lxGqLVN2Q-zQShw7aNtKekoVoSgL-zTMGiITzrxBT7RrxPvHn8XLFM7JHxuRq5guZDBSsk8qPWPeSvxzIHlzc-Ryf6EAAHTg8Wkln6yBpb06vskBlbsgJ3hDYdBtTFRsJnjCThX5mbiVnt64yre4MwqehaFdbFecB7o3-ssgphSvm-zQpDayIU7vfJhwvevFGt13BFtmYfEX9cl5hajU4IAQd0yjNU5EGHr-wQ6rR7IykSOuVuVPwcwYic2HbfUMgdaxuIsVL4FsZHyY9EaNO4SaK215nBD7SXNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4765f0c41.mp4?token=Gvr8cCVl_-mXb_ClkAg102lqpFKIRhJMyiqp4BHKeiidBQMhB_lxGqLVN2Q-zQShw7aNtKekoVoSgL-zTMGiITzrxBT7RrxPvHn8XLFM7JHxuRq5guZDBSsk8qPWPeSvxzIHlzc-Ryf6EAAHTg8Wkln6yBpb06vskBlbsgJ3hDYdBtTFRsJnjCThX5mbiVnt64yre4MwqehaFdbFecB7o3-ssgphSvm-zQpDayIU7vfJhwvevFGt13BFtmYfEX9cl5hajU4IAQd0yjNU5EGHr-wQ6rR7IykSOuVuVPwcwYic2HbfUMgdaxuIsVL4FsZHyY9EaNO4SaK215nBD7SXNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
زاکانی، شهردار تهران:
موشک مستقیم به طبقه خونه مجتبی خامنه‌ای خورد!
خانمش (زهرا حدادعادل) اون روز سردرد داشت و نرفت مدرسه، موند کنار همسرش و نهایتا ترور شد.
مجتبی خامنه‌ای خودش هم مجروح شد، ولی تو اون شرایط دائما دغدغه نماز داشت.
با وجود زخم‌هایی که داشت، خیلی مهربون و خوب بود و توکل به خدا داشت.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82127" target="_blank">📅 18:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82126">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYl5neIHSPeCzQJR_-Ay0dM4DympCb5guNHL4aMTRQ_XKDUNr2UXLhHHANm-VoE1ahx47Onbd40bfM6HTgyc4KiQFi0AB7AHp-j7P-lDAiU0eQnZm7XSqTNqHtyW4UQtoJ49QpLwiHCJ7tbCOBXlE753MQq_e7mFFJWchyQO_GBGzH8H-95d-_OXVU5wpSYzBKrHuHBFHZqcJFEsFI8yDV1TTBgNYoxWo2rUFq-jsyeOvLfSvas2GmovzOlxOwS_p2iFknVaIrPBAch06Yon2gK4FOsoAGzejQG8SKnW7FYcGGQfdCRAUXPCuQu8SaMJQQPKntDyE-fmdM3A24B1XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
پاری سن ژرمن
🇫🇷
-
🏴
استون ویلا
🏆
فینال سوپر جام اروپا
🇪🇺
🕔
چهار‌شنبه ساعت ۲۲:۳۰
🏟
ورزشگاه ردبول آرنا، سالزبورگ
🎲
با بیش از ۵۰۰ نوع آپشن پیش‌بینی
👆
با بالاترین ضرایب پیش‌بینی
📊
نگاهی به آمار دو تیم:
✅
پی‌اس‌جی در ۱۰
دیدار اخیر خود، ۴ برد و ۲ تساوی کسب کرده و در ۴ بازی شکست خورده است.
✅
استون ویلا در ۱۰
دیدار اخیر خود، ۶ برد و ۱ تساوی کسب کرده و در ۳ بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر پی‌اس‌جی ۳.۱ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر استون ویلا ۴.۱ گل در هر بازی بوده است.
🧠
آرامش ذهن، دقیق‌ترین ابزار تحلیل است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r21
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/82126" target="_blank">📅 18:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82125">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGdvmO1nVzZZfxHUJSnzNp26UwN8SdI1G1UCfyGclxBFpIoiBigFMVgx06mxZYUDx22nVgDB8xIXezawkxl2LcGCQb4_A9bJCuUScHxHxNxedoOLMFTqIdNemIdXqcTA3Msm9DlngtIaEkERyvzLsONx43_KwQytPr_z3ChXQAXMBB_laRa2KA966wivw0eqoURQ-_T7jGfa8Qh7gmCAQH1rqt9I4Wax7ilnNi9AuHFTFRizIarB5z2TSVHSXDcuYGI4DgGXCHnpifHrE5oAxCxEdz008EUBt2o92Cnv32RR8EClPUtaxbWjqJKTDuX_P9bMwqnXUrkiri_oiQd_9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلنوشته مسی برای پدر:
اینکه دیگه نبینمت و نتونم باهات حرف بزنم، واقعاً برام سخته. میدونستم روزای سختی داشتی و رنج می‌کشیدی، ولی اصلاً فکر نمیکردم اینقدر زود بری. هنوز کلی چیز داشتیم که باید باهم تجربه می‌کردیم.
همیشه دوست داشتی آخرین جام جهانی رو بازی کنم. چند روز قبل شروع مسابقات حالت بدتر شد، ولی من ادامه دادم. رسیدیم به فینال، اما تو دیه نتونستی اونجا کنارمون باشی. دلم می‌خواست قهرمان بشیم و جام رو برات بیارم… ولی نشد.
واقعاً نمیدونم بدون تو چطوری باید ادامه بدم. حتی نمیدونم تا کی قراره فوتبال بازی کنم. تو از همون بچگی همیشه کنارم بودی؛ منو می‌بردی تمرین، بازی هامو میدیدی و هیچ‌وقت تنهام نمی‌ذاشتی.
خیلی دلم برات تنگ میشه، ولی میدونم همیشه یه جایی کنارمی. راحت بخواب بابا… از اون بالا هم مثل همیشه حواست به ما باشه.
ممنونم برای همه‌چی. دوستت دارم بابا
❤
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/82125" target="_blank">📅 18:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82124">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVmriylmSWxWLo6VUkNsk7D5TNAbthu2tDIWaGV3udBsFjDuVCCMfe2cNZVSbRAyY05Ka167vGpQQcQIFitzfKlCCUh34n9QoN0DmHkehwoQCMrI3bRUWC6DBnBYSzRE155Z2s45HsPVXp_jOCT4CXla0-ZwVndKb52YyUd3_kXAcpzGmpl74ak6L6cUV0quyLS_3Ly36H5zUsv4tGLbQqDREz3kXDbgCCQFlZKHX7vbeloh_G1VxrUmNJOu_dePYwPviscVh2QL5qfDOX2Zb4KfEv1uP6A6V8YLS_ddGkwPwfIpXJ2q63mORY0JiTnC_iwWOK6yHMXjzUnzEKczDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی دوس دارم بدونم کی این توهم هارو بهتون تزریق میکنه پسر پوریا ادرویت به سپهر خلسه ویو بده؟  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/82124" target="_blank">📅 18:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82123">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEHCJOQ8hWqYPXB2HUQBuGmeHxpp3_VVAt5Kl2P8Z4vNV0PpRmn6Zd0gDJ9odD2T4Gj1GgILdodqWvdAB1qxYdK71kczEU3Sdigum1dNtsoQNvijJdVikul8biR1P_6Q9cRZ8DNH0f0JvHJ7qlgshiqmQ42Ui4bv8FUJPvzkt1bl8bgBaM7_M8fSzn6uPlTrOLuyEZ3QFW7nX_uREdt2O-6hKGIiwgphYDs5ioOwZloW4VzCMe3Hd7jGiopPi4OFGEhXZ0SUr5200AA_ca6I_-Iwpe221xX-TUtVTc-AmWCLsVyL0f8itZwNGj9IYdL9vAIIl3LNbg5KtnhZkMdaLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی دوس دارم بدونم کی این توهم هارو بهتون تزریق میکنه پسر
پوریا ادرویت به سپهر خلسه ویو بده؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/82123" target="_blank">📅 18:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82122">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_xrH6ILd1jS25tMf2KcwYL9cDp3mISWh5f8CUgByEn3pKtV6aq19DOrrh57-v-hTjd6SES8oi9qL_lU7xj3NsZXyiSpOdqFKBM6HvUVjazsoCWrgdJtPp0N9-D42PRxIlwqZq2g8z-JNgqdQ3PQpHFpBvQWxulZgSsiX0974Nl5y-WokEvhF2jjTyY0-9LSUQCgu6nhOsR_AaghOsEbtRIGqwzMhkoOOES91pUbpsGY5kYc-bxRLvWBJTudQAZsGx0YnFZ7t8iqLvPxOBqbdV0nuAhEZPfxBPvHT3cipC4PToQ8cYRNRNJ1ws5n3EX4BbYDgy-nKTZ6qnK9NKH2Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راستی، این یارو که چتای ملتفت رو پخش کرده یه ریکورد هم از پیوی مهدیار پخش کرد که بهش عکس یهویی داده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/82122" target="_blank">📅 18:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82121">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترک جدید صادق به نام "گواه"  ریلیز شد.   Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/82121" target="_blank">📅 17:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82120">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CW24n0zAUxEML6c_F4Ys9_YgasKuycfw6MVWY-0exmEYHwbgl8Hf0FxERwWn2NaQ1JI8v5BoE1ctWMC1skk_C2FPZY5XkLYt3v_NC8TbeebiIeU7ZJt8ldM9N5vxXX4BKbqgdIqKhn3Ue8rTm5Yh1K1FMl2lSrlOSUsoThyQdCOLjYbSF1rClkM-Y-GerVKl_Wtyga19pAeulQYR_G4tc6SFgQ2XoiUSGurZIH9ZQ6Qn2ui_F-APUjuX6wku78sSyuH0aB_RmykQ2rBBl9cfrIhonlWsCpq9rwDrchdBDBS989h5LZZ_-fXPOk3mHypNljqOaliOv89jg67ggMQ71Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید صادق به نام "گواه"  ریلیز شد.
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82120" target="_blank">📅 17:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82119">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خفه شید عشقم آقای واحدی ترک داده</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/82119" target="_blank">📅 17:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82116">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOjKE4618ers6qPbPazS8jchmhVfbGKlNgOENZlSOVH2798rSF4ix71d3ivokiMqLVz_IwoJBAWUa_S6LhfenY5gPetdsl3KK25JlvRtz3llHRQSHs2ewx-F7m9c5yeoKHnFAEER3nMEc6xjgwUdD0-nAEAGepITXe3--q_SivxWUufJZ08p9EKbvxJwRpqW31PcThIzV_19bqc_WJY2ca31yhp69FA1iohwwGPtCeaYegktNLKakt26m1CK_KpwpEhF-4FhSpA-eHIGiHw6VGQ1ZO2vsn4wfwJSiRGB6p9BMoN1uhNnHCV8sGWeLEiJNX1qkaGX35_HtaaSt_sgtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز ۳ تا اتفاق نجومی قراره همزمان تو آسمون رخ بده:
خورشیدگرفتگی، هم‌نشینی ۶ سیاره و اوج بارش شهابی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82116" target="_blank">📅 17:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82115">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CV6LDqCgLDoeAMHalcpNlXHpFi0eI1yhxEZGyqOTxE99mZngY6P_DyPDiaQcXEB3sZOkZtoKsa0z5FIEE84UJlX2XJh8cim0GtxRP5JzhIIpaiJZtZrUOWymLs1zjuAsMFgr-2NFifmew6y_0kCEYgfqqLRMHs3FPaYcM0pcHUcpjD1TGp6VerLZP5gwPPs2vEGFwhFp5-kKK6HJYotHd_qrqNEpvo7QGcOa4nDSJ-NWdIc4vfV2V90C4Q6Eta97XeP5j4heIT7eH6hJ2MPOI4L3VbMxdULBgqjWcp5gPgwUvss3DpAN09e0CeCq6Mq85l6R0AH7roln5Zd8C9fNnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو فنا و مسی فنا باهم دیگ دوست باشید
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/82115" target="_blank">📅 17:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82114">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBzza6IoL414W1KBbGkg2jsWgYEBC3RC05Q2jQO3rErpCKYwhvUVIsiByiLn-bbZlokix96IpQiCKkQu8Nk6gKYr0fGAPv3-hmm_CGYaVTNrmkMnwdtsnxEW3CYnh75amkcbXWjPj6zC8to-oX-dnvg4V4ou8-heN-rJGDVvkhbGHsKBx-XMqHr1mxAmb_w0jhtAO6WJcn1mkN_E2fk6LKoxBhuJAdbzF93wf6TSX-oVIRioGVeEdN0O2r6opT14eJBVM6XGfz1UXhQCuhZwKojBIqiJ1EibUKDOphxzOaz9chKM7lV7R6bw9n5PjY2B3xmywDGDxkh1xHvaQ4baFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خورخه مسی، پدر لیونل مسی در سن 68 سالگی بعد از یک دوره بیماری سخت درگذشت  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82114" target="_blank">📅 16:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82113">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دیروز دعوا سر این بود که کی کیو فید کرده، تا خلسه اومد و نشون داد دود از کنده بلند میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82113" target="_blank">📅 16:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82112">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">زاکانی، شهردار تهران: موشک مستقیم به طبقه آقا مجتبی خورد؛ همسرشان، شهید و خود ایشان مجروح شدند.
پس از حمله، اطرافیان قصد انجام اقدامات درمانی و بخیه جراحت را داشتند، اما رهبری در همان شرایط نیز دغدغه اقامه نماز داشتند و یکی از حاضران از آرامش، مهربانی و توکل بالای ایشان در لحظات پس از حمله سخن گفته است.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82112" target="_blank">📅 15:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82111">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ویسای خلسه یه جا خطاب به خشی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82111" target="_blank">📅 13:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82108">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">وزارت خارجه پاکستان:
پرونده میانجی‌گری بین واشنگتن و تهران را نبسته‌ایم و امکان تمدید دوره ۶۰ روزه در یادداشت تفاهم وجود دارد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82108" target="_blank">📅 13:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82107">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUBhxiZETAFB1hcS8Tfa4NWJ4Wozq7iJqrn2slf4l3CHYaAwxyqm6eKR9gf2DqrdTxTHDCNOSvK9Qpnk7FbtsgBp-9u7ABJCrph9bTTHAphmjgESMSACxVFQxCI6eazBdILXLOknZiVxGMem5KLlcZjAireRlQvklyAbIYUm6yHZUtD515MTWbfz8M_gYYOScqO9n7p6P9M2Mr7-8S57svB-7cPMBxRQyvINOFl4unXTyW_70QnY0D6HM_hh7eco2OmAy48IGFqJWVQ5LmxE9WFh2-PWzrtmTqynT5hj1TlBwlm95Z47oiSIwBLrrQA3xY1gpaLLndnuNsEUbOlqBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو به مناسبت عروسیش یه قصر چند میلیون دلاری زده به نام خانومش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82107" target="_blank">📅 12:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82106">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thBLR6Z6cdmDhAeGIf6pTAMNiSKsHhXelV49Zv-HTs8tGuIyPzGO-dJ2soGS8oFWcvocsi41HCcfEIc1fy87x1tDCPF7qEM4PjkQto2WxZsp5SiXXFBfpFPPBL7O-i0vbRHRvaG3RJiX-0Lw8H6Qw1AIEYza3kIyvlcZGHEp89RsFMcvhEvr--LHUpS0ss4gLyD8_fV-Lm16TL8A5_O8bVqftqsFh_XXfZ9gABKq-TZQTBWUXVAe4_VqOAoh-4uWfbR80kzVKRO0KqWd8XgXSoDELcTB7XTqUf7zhgCFyfRmnf5kyhR5NIfglcqd0ubC9KG2jg1tpaPPTane0puAPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
پاری سن ژرمن
🇫🇷
-
🏴
استون ویلا
🏆
فینال سوپر جام اروپا
🇪🇺
🕔
چهار‌شنبه ساعت ۲۲:۳۰
🏟
ورزشگاه ردبول آرنا، سالزبورگ
🎲
با بیش از ۵۰۰ نوع آپشن پیش‌بینی
👆
با بالاترین ضرایب پیش‌بینی
📊
نگاهی به آمار دو تیم:
✅
پی‌اس‌جی در ۱۰
دیدار اخیر خود، ۴ برد و ۲ تساوی کسب کرده و در ۴ بازی شکست خورده است.
✅
استون ویلا در ۱۰
دیدار اخیر خود، ۶ برد و ۱ تساوی کسب کرده و در ۳ بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر پی‌اس‌جی ۳.۱ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر استون ویلا ۴.۱ گل در هر بازی بوده است.
🧠
آرامش ذهن، دقیق‌ترین ابزار تحلیل است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r21
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82106" target="_blank">📅 12:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82104">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WPa58iOoOe0zClULuiCjGE6aoCGIt9aHRivnR-Ye5rOhwLopxoZfelJYtkGvrzlZtOq5XibaogzRqEX7KU2rpRtXgySLw13EojQtJ8GFtal4KraGKOsCprmU2GjxktibveKgorNX8Ai1no1mScvfOzc3A0sscHVZ4ZF4OeJtmH5WtYGfvGaclp0RRXMDCUyX0ZTDb2kaMkZsrl6bVoDhEXh3nFvK9T7tNuhDmm4_zdwPcCX3lTZ-jHhtUCIrzWuY9WSVvNQNVT47whtg_ZjCuWY4oqNtUSlqTWKs9RG_PIZPRy3kVOk3Up3EO06MLTg41dHfq4io25uXx4Q-Zx9bng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HaKlOT4vUpl_bzKoGyrYPDI9RgfX2nOtaT0J2FAL20x2G3lNrmhmY1JZ1MeuJMM37NxhxPxyF9O1tgq8fbVrXXrQdhht43Wzd1-dACZoxfAbjXTgkNkXPMt9WYDL6lHRX6zXtcnTF5r230TfHFjEeiB-W-EraqEERN6Psut9wFjAfnzFiMWWEqO2ZoQ3fIh-k7_uhCPD1u-Qw87jZf_TYa1P3RWYov71OFpgUUB61BvqSheCaYAVwAfndTPERnKjo4qlBzUXLTDC9gIaGs4YasEMhkV6jNFW0ZHdIWymeFlkYy1a9VMga0H_3MUF3bIwYiJRZIH2g-yiSNcYRbodRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پسر شایع نسخه مینیمال خودشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82104" target="_blank">📅 10:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82103">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2be999c32f.mp4?token=jxiHeiwSYlcJwQXPEQDW6JOMuZZtha01AMiiaIfv2hjzcC27xPLxKOPNifoplf2tpm7H_r39PhzZTu9xtKcoQo7zdITeMV1u8fkGUBjOK11q3sqtDPbFeztui9m5VzvAq5uZOp0IJAOCeP8NVs12u9Fs_yhuyq1qVu2xHEqj-6NHPkMZ56u7G_wVpeK3EznMdlHX3w1BbI5JQkru2q6YfFReMBteLJAbYT0iRkhKLWjoPl3D_2lWcftfOLfSvNq2SCUOwGcHVL4dgtRVTV3rvP9zCzSuEVgCZ-7aWBB4dDsRZCjQQMV7cSUfOeq1cegsgqBQ4nO9u0TaAM38PHl3ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2be999c32f.mp4?token=jxiHeiwSYlcJwQXPEQDW6JOMuZZtha01AMiiaIfv2hjzcC27xPLxKOPNifoplf2tpm7H_r39PhzZTu9xtKcoQo7zdITeMV1u8fkGUBjOK11q3sqtDPbFeztui9m5VzvAq5uZOp0IJAOCeP8NVs12u9Fs_yhuyq1qVu2xHEqj-6NHPkMZ56u7G_wVpeK3EznMdlHX3w1BbI5JQkru2q6YfFReMBteLJAbYT0iRkhKLWjoPl3D_2lWcftfOLfSvNq2SCUOwGcHVL4dgtRVTV3rvP9zCzSuEVgCZ-7aWBB4dDsRZCjQQMV7cSUfOeq1cegsgqBQ4nO9u0TaAM38PHl3ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تروخدا یکی از دوست آشنا های این ببرتش تیمارستانی جایی درمان بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82103" target="_blank">📅 02:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82102">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کیر تو بارسلونای بدون فران تورس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82102" target="_blank">📅 01:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82101">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">علی گرامی به کدوم قبله قسمت بدم دیگه نخونی؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/82101" target="_blank">📅 00:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82100">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir</strong></div>
<div class="tg-text">چشماش دنیام بودا
دلبر بی ناموس
🤙
🤙</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/82100" target="_blank">📅 23:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82099">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9tA-qqN0SIkD_Sy-FRQiYoyslzaIdbQBPW6_sycpG3BstU7OOpuImMEHKM6FEljIV2tMLRyaGV_5rxDimVWJ_2sdXEgTGZcNlRXsdCVfcFvXWK9QFPdI3FFSrFqKQ8dSKeSHKMgW0QRV14X1GTIDvZVdfvNeLCkWrpjQcVf6wnELgs6C3fUuMLwEUU0ODKaUySf5f2wu1mXrgb8aoeW52OJNZRVpNC7yuZYupPsQNhX2VMEFQpP97EC3M1xrkIq3HCVRfuniqtINJmlQGQP_N8GjAzwJdtymVnutDO6QbGNNHSVPi87PQkGeYQKKOxBqLv_aPQg77RNPXxqCHEy2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس فقط یه کپشن "حسبی الله" کم داره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/82099" target="_blank">📅 23:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82098">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNoah</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xc0tfPF6j-wc-M7wu1RX0I07olqBTB9kVM2tlCceyQwUW-0VJu4bxnWB37aff5eqsRIQjvSdai1NPDDCZW3_3GUHATef9or5RT_R4QXgkDbr9VV_PHTdBpqPLMKSMhdQSKZoyPOLQG0kvN92P3sYLLwnWF0Hq0vcOqdeB-VsqF-YY2xXltPbbWCAVlPLrOctBdyQjJJrKfSB9bdY-jUxXPBtArenbJTdALdU_MFHPQlK0xfuC7v9-ek_MmDwGXH-gVc2Hw94L00WPPe0jS0POiBDkMod5vITLtk79GV-DK2MRo94iFm5sNBh6FGJZEGQPt3ghEOcqo-7FQCH8psWqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو حرومزاده یعنی چی که اسپید رو دعوت نکردی به عروسیت، من بت زده بودم روش</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82098" target="_blank">📅 23:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82097">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o73iE4EhTYrzH7bTVixP7nuXQDmPivZHbuz3WG_f9a1ud8FWyb9JU3NNO__wItdk44mz5-Q4SNuwIi86vpdhN4RVLdvdFlu8YhRnIzEc1GrM-z6-dXjtMTpRL_0Q10C1xQoC6XKJVYAyofZDy23QXxmDrGdZC1GrENznaxXdHn5FPw4esaX_R4WHKvGQZq3Rf8IUs0lJqFRrHLskBUkYhH4D1xdHsrBQuCnWD4nudY5jbRrZKD4PAovI8Ws9iW_mEHOZ6XjfeHJWn1LSzAZlbZ5EF_WJtLcWO50Q5zwKsbQI1JJ31_6oV55t587JFyo9u3wUippd2vWr0ywK43sARA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این رسما دزدیه‌بخدا</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82097" target="_blank">📅 23:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82096">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">رونالدو و جورجینا به قاطی مرغا
هیر وی گو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82096" target="_blank">📅 22:56 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82095">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKVqntB2y2iulQvupylTGXrBMYMm0QbZgOke7Mlb5kMdSJ_2HqJWG6YwyuP0qReKko7rTzPGuIHvEFu8GkvUetbsnlso9I_hWxIWkWsSz1cjzEYixxoqUjhBrBBC6aBGiNNiSncjPbMJUlCHXb1oGOlSopZ2N6u2h14M1YEDncTbY0SzIJO6DDHLLt3Er7WLx1766jxt9hlEfdCdT1yFrW8AtrdW948NOQEWfSUygF-JXp-Ay1hgAjxhu-bcHX1Swu_oXFxJMCffHGC2s0jYTytnzvM6su2EHilqJtA73yAcpRg5Wb0qo16WVkQEz7ZXSZDnCmnIrt11Ow6VcjE62A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داود کیم، خواننده سابق کیپاپ از مسلمان شدن میگوید: صدای اذان در تمام خیابان های کره شنیده خواهد شد و گفت امیدوار است بتواند به ترویج اسلام در کره ادامه دهد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82095" target="_blank">📅 22:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82094">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">آلبوم جدید خلسه به اسم " Margo Zendegi " منتشر شد.   SoundCloud   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82094" target="_blank">📅 21:07 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82093">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">آلبوم جدید خلسه به اسم " Margo Zendegi " منتشر شد.   SoundCloud   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82093" target="_blank">📅 21:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82092">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edsTsVhUiQqV0uaQu0eJ5gDLOedpMfUvc7pF6Rjwd4J07O5TOzmS9NB5sOXpW1G3_dzWfTeempXin0pzN1k6HZqpmeey3RCGDWAE6IGFYacG_qDhZj94HlxmBnjDR1xP0lNF59cKsHM-t5cntCFsvPnPza1l2CbPnsqSLhIY2-jPWGb4EKcipuVdR3F1AaornkyJYzvmgpkMWwupG30fDvo1m4PDFd87lCta6cvNu7Q1GFA061Ih78LvAELciMXv8DQTbexNa5EF181GCT81o_ziCI6wYgt-f_G0LpmzMQwuUkCWTcfRPoZn0udoAikje_2EZaST6Ep1pHcxiIrC7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید خلسه به اسم "
Margo Zendegi
" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82092" target="_blank">📅 21:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82091">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkuaPF3NUuNg0j9NSvHF58B9Ww3Nk48v-cppmZ7Bp5tRq-xx-f5wfjhJfOdPyH7CUCc4yyXKTY_88M_prlOR64wOCQq5DUeNEXkle-C9TKjIycF2lF4JqZzOCjAETJJPuIlSLT04BONDwj-BAPAlWI7Xg_d6mremUWzwBUjcLL4ixAoAWyh3cPOUz-cT6EAOBRu9byHlPlrmCTBxSGJyA4U8AK0VIFrJ2-HuobOL2ovzAQCQnWyEZiWzuEzuxhAw8XiWCwlZQ0dbldpxst_6imuPtsrpoyCLNHPqCXQqEpV-1RaWRzDjKFd0HJzsgpr6RU3VUcksxWuHO3lKW9kAnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#ایده
#تتو
#مهدی
#پسرعمو
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82091" target="_blank">📅 20:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82090">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbK_gODGcVvrlpgPazFu7HR9UmrXmVV-OhLFd-x-xUtZx5v6vv0FClycqxv_9xLMY_Nqa3KzmCPc3cn81ftY9pRUoGMkAiXCpfSnBFaovWquAfOJ_6jmer8B2mgt5rMKgYxAIkB3RuA9PH7Naqfk4cQQX9OEvhTnGhw9468qot2jhCdcrtVUy9FzBoqh_BSYKstSfyp0hqX3PWG6Jwb-PEpqzt4htHcZh0jkOt1M6cYDn5KRsdlZEJnTV3XNksF5fZSQOvoIdjS4fZeLT30SobIVNFndRJ773vHU2inoresjeD1m_7-GJ5b8WwDXTdO9QfUL5a4RGvEppHlcxVXfRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علم‌الهدی : اونایی که داخل کشور میگن جنگ رو تموم کنید، یا بی‌عقل و مریضن یا منافق؛
فکر نکنید اگه جنگ تموم بشه آمریکا دست از سر ما برمی‌داره، حتی اگه همه‌چی رو هم بهش بدیم، باز راضی نمیشه و در نهایت وارد کشور می‌شه و حمله زمینی می‌کنه.
@FuunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82090" target="_blank">📅 19:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82089">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfozuaypOmR7EC5qr2gX_xaDNThcXpfIfiOz1n-1h2IdEJ2A8fzLckLmr44vTj1n1Fsm4NocgtPy-VZuGMpz9WQ3wDr8-kkr-Yo4eAowLN0FwDwpJBmK1g895zf9OpymeLx-mdAQevydjfvDLi6wJJrv5hFHfyQGZrYKak1uqVF-33iPRS_36ryK18GE9aC-WGaytHd2C61IPWjtufgcg_nXYNZ4qaGCMhydY-XLbfU1ArXNpUTPutX4fcbNQH4pJ1eucv4DDfFrQuHrXS7-1TXGcahGK0e2yZdbymiFncvbLULMk164VleN7T3fHHZa98kKj3P-ROKBHIeV8nD5eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دولت لبنان رسما مجازاتِ اعدام توی این کشور رو لغو کرد.
مجلس لبنان با اکثریت آرا به لغو مجازات اعدام رای داد و این مجازات رو با "حبس ابد + اعمال شاقه تشدید شده(احتمالا کارهای سخت و اجباری تو دوران حبس)" جایگزین کرد.
لبنان اولین کشور عرب تو خاورمیانه‌ست که مجازات اعدام رو به طور کامل حذف میکنه.
@FuunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82089" target="_blank">📅 19:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82087">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اوه اوه آریا یوسفی از جنوا و مایورکا پیشنهاد دریافت کرده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82087" target="_blank">📅 18:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82086">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc87bc1a00.mp4?token=EFCtzaGRmyqDlA8xoRgToPBW9Uqs2nyf179EFZWCE0Kw09i03_ORy0Qln3VZznQyth5BwQz2uhgV8wHZvFO1otU7oCVi0l3QBU9xhxf56o-zV9uw2NDB6nH7GZgW1Ifvp0MrRNgAMmRXhCmV7yvaVRd7j32-qhGlcneZNI5FcgxFZwXmG5FkPyQe0Fn6PlpHGeC6xx6oJLbMaqhFZayFVHmHre7p7I70_WhqbGjwDzol4CHEj0Kna3LYGmmzVA61OOJciQL2m8h9TfpPunWtfcn8u5-ngBx1ljY9wvIJ-7SS_gFAHArF55VtBdIU7BCABGFgZA_j9OipRrpSuk7P9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc87bc1a00.mp4?token=EFCtzaGRmyqDlA8xoRgToPBW9Uqs2nyf179EFZWCE0Kw09i03_ORy0Qln3VZznQyth5BwQz2uhgV8wHZvFO1otU7oCVi0l3QBU9xhxf56o-zV9uw2NDB6nH7GZgW1Ifvp0MrRNgAMmRXhCmV7yvaVRd7j32-qhGlcneZNI5FcgxFZwXmG5FkPyQe0Fn6PlpHGeC6xx6oJLbMaqhFZayFVHmHre7p7I70_WhqbGjwDzol4CHEj0Kna3LYGmmzVA61OOJciQL2m8h9TfpPunWtfcn8u5-ngBx1ljY9wvIJ-7SS_gFAHArF55VtBdIU7BCABGFgZA_j9OipRrpSuk7P9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رامین رضاییان: طارمی بخاطر تیم جلو بلژیک  گل نزد که زیر فشار نریم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82086" target="_blank">📅 18:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82085">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d87d048c.mp4?token=ZciqqGvqW5XmLawUOM2kgKTDY2gr1AMBXd10oqegoQhbPqMiQJyZWuKrP_CFrahRxdKguAp_Zn3Io2M9RlmKIENeHu-UYoE2ooJM0254G6mWkq4eEtSCmISTwcpn97Aw9LsU6M6vvTcByjrDy0C6BHbpZYOCKBODfcOaF_v4RncI_A1Yt9cDnyIq1c7PPDe4FFiXeRA8jYMpx2odFcS0cKsIqLCV2gFKKNqCZjXdiZ7bCa-dz_TvrdKN2pplSxKyTrpzsJp4J5ZpnXxZZyL1plXJcqo1oe1iI461hTcVwBeq5aDdrd7s3FkDdtS9FBIY2YUJbo9U18siMM-Hi4IaeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d87d048c.mp4?token=ZciqqGvqW5XmLawUOM2kgKTDY2gr1AMBXd10oqegoQhbPqMiQJyZWuKrP_CFrahRxdKguAp_Zn3Io2M9RlmKIENeHu-UYoE2ooJM0254G6mWkq4eEtSCmISTwcpn97Aw9LsU6M6vvTcByjrDy0C6BHbpZYOCKBODfcOaF_v4RncI_A1Yt9cDnyIq1c7PPDe4FFiXeRA8jYMpx2odFcS0cKsIqLCV2gFKKNqCZjXdiZ7bCa-dz_TvrdKN2pplSxKyTrpzsJp4J5ZpnXxZZyL1plXJcqo1oe1iI461hTcVwBeq5aDdrd7s3FkDdtS9FBIY2YUJbo9U18siMM-Hi4IaeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران چقد عجیب شده، تو دیجی کالا مواد می‌فروشن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82085" target="_blank">📅 17:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82084">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1tGgIJzytYUKNtb5XkShG98bW9_cbIZZl0wAa4JR3mJWofSejdtPS6nGMUtx87RlzM3DbTSpTYEoEXIQBjKZ_JY95ALmcHY2iUjV7JbTKY8Uj-IW9d2AdpsGtanxkpJbReOjnQ1UkroFR60iwDW5P8VjTe5VR1JeuHK01kcNmc7CXOW4qgAODv7PMmE6asTybJ7SfnjXYMYXE29iIGpMlbGXJ23ibJKCd7brDqgK7FK49uz8V3k_WJvu7gwkacbscrydlOIbFY6IKoe0y6C274Vj0qDnZ3X0dKdqGKS0fvwyzD1K6qkACDTAAIMosawH2q6bKR6yjaeDkQ1dLGOjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دورچیو
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82084" target="_blank">📅 17:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82083">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترک جدید متین فتاحی و سجاد شاهی بنام دو سه سال ریلیز شد   YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82083" target="_blank">📅 17:07 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82082">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DT6gYyTDILS9nDzwZmsGjtaSQHf7jBwUQU8NdI5Nr3lWcgobEvzgugZiLHGqh-I83_wXjYwm1i9vkkkF81QFjVaU8hkkbC5m3MbMqKpzloKsWXinn0K8skF4l4NGdkf0zkFAuZVKFT_EfBp8MgjlmJQ_tBhh65ZA6uqftLRPi-zQbmL1rVm1vKgrjsrageL-pObegsMIDV_lbiKgdLeOgVGh-i8GaR7FX5XRRDtXQMYKpE4n0Em4p4WhMvcz7Yr5Ix3hSF4H7vJaYnc8nV9wh85SEf5X1OmPSCjGjm7H11wN3YSG-DU8nWlMkSn7pFv5srjGIy9qaAl3z2ca_RMxBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید متین فتاحی و سجاد شاهی بنام دو سه سال ریلیز شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82082" target="_blank">📅 17:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82080">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترک جدید سجاد شاهی و متین فتاحی یکم دیگه منتشر میشه</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82080" target="_blank">📅 16:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82079">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترک جدید سجاد شاهی و متین فتاحی یکم دیگه منتشر میشه</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82079" target="_blank">📅 16:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82078">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGzjWysZMSmiKR_yclvhubpdTRoUlX2XPRdFJtpyrNYS55R3CackrWQErFPMFbqEutePjkjMwItFLctNG7nXmrftnbkKbOS9e93e0JGvxq00I5uvcIOeGBPklgxzgVM4zxcQVXcBnyOVdpJmfuw4vfTHYyX0pp0BAqZkqu3YUzqY4iozih2EpbJfDOR7gMdgwEPBpqjWxtKRfjqC_AIg8YaYqKGtooTT9nO1MCuJoLWjNJkl551WLMh_Bkn5VnEBrFQBYgnpGZ4RPH3TljVZ_1OiOUqJQl1RmRCOG1q4pG9VItRjlU4mVgpBnERrqvzGbBgPBTZip_JVKXv8XxU0Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیپ استیلر ۲۹ سالش شد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82078" target="_blank">📅 16:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82077">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بوی خداحافظی از فوتبال میاد
مسی بعد فوت پدرش هیچ زمان بازگشت دقیقی به اینترمیامی اعلام نکرده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82077" target="_blank">📅 15:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82076">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-gHW2qERDQwEDLGyoPMGB4LhqgLvBq9XfiJKMrU_l5GBq8qYGKIdt6jOsUOuslGC9SWmLyQMwa6z0zl3d67RowYUXhF9z3W4_OY6TOllPH0fiJke-pKE4mnejqsFYqU90PyemXrtwW6VK6Q96sx6Pr9zsPf8hKrhD7X_z-IG6xNVjFgtk7ExahUlfvKsZUc81DCC4XKKFY4NIa4qRc0QzvzZ1FVSdYWjOcyImJsfTFcSekfW9BTVId_o9GI_Mpe5V1YZo0oS_qEXjVzNTtTfycOTTb6Pddr_EUaA5lZKZnOObJHxzPwIqe4alqFRAIE8DThn7qdFqjJX7M_u0bkmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنجشنبه میخواد بگه دکی بیا بدهیتو بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82076" target="_blank">📅 15:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82074">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QTagDlKKqdNs7lX4_IZa2TDOSDoQva0CmwtpEbXQg_7ZGkmzxx1_aLanmvqz__Bmgm3ZVwbsnTKn1qxrEEpt6IwtlswaumaGtJlDC-b_WeJpHoIz53vSdyBDzfQYPYK0iH_KDKtcD8psIs1tH3RJHO48skbDgWmy7VdUQ9CMhi5c8t_F9iHJzjd78zcsS184TL239FzGJZumTJ9PgVQZk00occMIZBlcYIKTcbefJYFBNv7CUT4E1Nh1uTQRVnEl_K_Hblqz9NmMY9D3H2z5ha-ws78qK2CVhpMNdRO0jAmv3-hijUloMmriaoLTVNWodABFQCN-vKSWWpVmk_uM0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rnmWh_fbAYP2qKoVrehw1g_B13tqSBwnRUfYgmhXpDB81NCfTiGAwprL6b5rnkV2TRo2yNLn2G0CI8_ek6f0pFpT-ha4T_XtlDGxh7-PkZYJkeeRTGPxeB3-fiCs23pq7oQrlHX9CvKre9S1k7OmpG31C01HwCqBKd170IuWytAD9MAkjNAfveoTW27ufl4BE28KppsZB8J4W9L6Hj7-AOSb4qG1US3NiOBdcYOuF73VSXuXRtakzNYTtLyHf_L5R-Njd7cXcWsI_IA6FqO3zND22ttutOc1qmSHnMy6eM_-wTgQpCxDu_XoTIigGqq9RfccF3ccZWQyDABdjKUddQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شیپ استیلر ۲۹ سالش شد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82074" target="_blank">📅 14:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82073">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtUgzPGVhSiz4RkwsDQWvCkMf0AF4tWi1F_2DqNmAkH3oN4c0ewQNzdQmlAivVj7F7WUEGs5DfmkZQZTtpnHd_gMQzIZvd8m4qZHR36OTo9fPNlM5gQ123zJO6APfpdfcgUuJC2WdqthpJWVUJY_RsmSq7l2GxfUSF04cIftZec_tuasQTcQLk3LXR8yXMNpxAH78Np8QeB680sOP_vVfrFuXzyD6ikBLkzux4lTTL2abz_z41hLDquFSizvn5P74cUKNm93bV4-_9gi7IBDfpdRmX6haDq-n7lbmkNEnOe9vJWFfJr6qW0K7sGQzkWuTF1F1DLtG_3j_D9ayDWpFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیپ استیلر ۲۹ سالش شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82073" target="_blank">📅 14:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82072">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا:  گزارش از وقوع یک حادثه میان یک نفتکش و نیروهای نظامی در خلیج عمان   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82072" target="_blank">📅 13:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82071">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا:  گزارش از وقوع یک حادثه میان یک نفتکش و نیروهای نظامی در خلیج عمان
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82071" target="_blank">📅 13:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82070">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrCbbAPQY6S37fy7F_uq1ETJX7TDVg9vPMyPFl5yyGO5RvDjltd2gBtThEj-bBhcwlffTzPClBJzNig1DUk9EZx5_kIZtyMQgSncQEJjRuomGmlzL19IQHrUphmnZw461bbX1UWIw9JcecqSaDn9EsYVi3f4csVEYhqKFGARQUggz2doCU3W2NC3cGTh97OH_useCFOqCRkzAhD8qk6TbzbzppXEUgyEKb1GUTnqxm2SzU5J5xvMW4TSlW_arYLK7WQORsnZZcx0iLDN8EmET_BfmZDk6s0o2eh7qODWUg23ws-5EnU9BEF-hZUtaS3GI8N7IZpiI9S3kDAKA5e1hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویناک پولات به گا رفت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82070" target="_blank">📅 12:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82069">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_9fi1PGQKECEHkdL4KTTGD_W7u_ZaQw_FLvMS9xgcOlEbdURFY-gELjG-ePq6icQOHb3RoNyrpd86OcPAoPra78z06laJZ0sD1dm5C2rlCzpU_LJdjs0ttd1B_V0xjjyuYPsIT3TXQYY3PKB-4qJvBjgoryKObvR_O9WC2qe2I9z5swP2ihHUYyCh5MFlGOWMQOZQeoOTy9_EStGulFS3AkgZueWesY8PmEzYNMIuebdl4Zr1L0CIPMHx7MIDp6nm-sedrPmkxT1Crcw08aU7aLI0H0iUDfn6DHP664R8XdPbBshzcYG6GnB5xPF9eWiPI9YPFza-b2Qnv0BP9knQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82069" target="_blank">📅 12:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82067">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3CltddpaBu4ml9WWhkRdMUUvYn2d1kQnczTKnkSrzmKDfAfOABz9OgxNo5hSiJW3Um0M6yZ8DgN_-ZxWwEdM_qVvBCEc5sbhZL0_JTAiq3O-LGReWhnqm3hl9SZRuFXBf2oOMjOxiwqzuzok20EuH8_VV-nQ1rrlWo3druoDZEapi4es2CoQ15XxsK5amHaA0XA5aZoIEYTS5c1_EY1Fvdl-uL_kE1UGrAnwL3UCNvQ1IsmNGAfr4npgQbknChW9xPPXxb5TTFF8mUpnAptHIHd0wRzBgY88SZ6_6voPQhjX-zlbWsSLrioULVD0Cvd2p1sUqMec2mtTZO_sX45gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری احمد خدایی همسر جاویدنام صالحه اکبری از پیامی مجاهدین خلق بهش داده شدن که در ازای پول علیه خاندان پهلوی استوری بذاره و اعلام برائت کنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/82067" target="_blank">📅 10:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82065">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">داشت یادم میرفتا
کصمادر جی جی و دانیال ددان
کوروش
❤️
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/82065" target="_blank">📅 02:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82064">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrZPUlE2kZfIStRGOklN4fPvjZgPlVehLY_0svf98t90GlKk6tdGFzA0caIVOft17ax6G5xXH2anfOX2NkSEAOpD5dNcpSEreKNgs0snFhNp83zxHGXrHcdGvuHGg6GpO396o6mr7wRTxfIn9kTG8zKnP-NMO6x45v2dIEZASIG8IHxI9SiOry6Ev3LDEYhdsGdnEoqYR8h-vsJzWIbDRBkULFdOwp9Xym-piHOQKZ6az8H_ndPLZv-nc3R9j_ElhSQrpd6JSc7OrfIcep52Z0gs9PHOp4zd3yi10HHwxZEdJftgptYc-6hYHY4f8qYqNi9EA2BMtRal_Vhs9io-2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فریک پنج ستاره از ایران داره تکنیک های مارکتینگ یکی از موفق ترین آرتیست های تاریخ تو این زمینه رو زیر سوال میبره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/82064" target="_blank">📅 01:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82063">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دیگه حتی دکل سیریکو هم نمیزنن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/82063" target="_blank">📅 00:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82062">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ceZf5twYSzpbHT1iTm7qs1SpTAjEsLpEJmIs9Gkoj4qn7EIePdcNazn5A1uNMpnPleyJJtDgwcsiSiiBDyolRsSKYFQChUf36y1myvhA7q22MYVCGFHZtdfQDECy_n37wRj8ZzBtwABcgMqReWWNFySRIQ-3MuHsLZOayOs0R3ETNNNys5VE_kzqub48IjdjBsvgCzdH9TXngZ7nR1FfCUI0dUE5D4CzWqganDhts80uvlg5--dU3coHZcI2eTaNV9apHCeElAoDNNweISYFy0IYA06dxCXOtA-W4W9tKP91U1Str3igQXUGCGc6zxriQXwVLwokoMDcpVsdd_wDMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سطح امیدم به زندگی :
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/82062" target="_blank">📅 00:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82061">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">هنگامی که با یک املاکی مذاکره میکنید، بیش از حد چونه نزنید. _چمن در خاک  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82061" target="_blank">📅 23:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82060">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbkLMhRgs8LX0yiqtSL6QevdbOKwnZf0jDOWuAQ1SnxI868xQdJEHO0XVH0xXfXZG6Y1ifvOldSDQFaQ5Ac7HH8Msxv_jfcU0lUjaSFsvY-d3gWZaXYciHUJ6lFXxqdMTDmrR14k5e1kjKFhem3rFHIvAfKn5Iv7HvN5ZD03d3P0ueTcDN5Uqxny2Few0eD0EY8hEvI-_QEQ9f0sF_tu6eWuCkeXiwn8P26uDprYPNcaz3S0HGtMvqYkR_DFSWW2ZRQre9FehmxkJP514dPNW_eIHKmdOL5lXFOS7vvzJLsCDTjHMG-MMX5IOkWkUdsDxQSf81-zVWrTGgp0HWLThw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید بی‌بال به نام آزادم زمان منتشر شد
YouTube
@FuunHipHop
| فان‌هیپ‌هاپ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82060" target="_blank">📅 23:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82058">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWtsDf-ETc-no7sj-QaOf5RagnjrgN_0EAAfPmHRFcLdc_RgcZFBBsKYiZO-9vRdpbUS0as2a9GM6WcDfqywR1eSBMXWIWE3uDY7tVl0d9d0hyqq0WjWydlEjVtG40rQIRFeyARXGxfHj01nwuE1hUd2Ji7L-Ys-FH1eryO_Jy5wfFAIT0ET9_SMxXZ7HdTRdClFXN8fiYhJ5d3iKI73pL2CbGPLG8EPTLfCrQ913lCSPs8_YKt6n8rczpgqFq32QcHYak3W0pD7Uait2LX9JbJ13N8nyVP7GssM3mb6OcIVMKNe6oRy6Ll7ew-sMt4aQU7x8V4tEyo-PJwLlrs7eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پینترست چرا تبدیل به کرج شده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82058" target="_blank">📅 23:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82057">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ عالیه
گفتن خب تنگه رو میبندیم فشار بیاریم، پاشد رفت یکم اونور تر محاصره دریایی گذاشت گفت اصلا خودم میبندم
گفتن خسارت بده، اومد گفت خب من که خسارت نمیدم هیچ شما باید به ۵ تا کشور خسارت بدید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82057" target="_blank">📅 22:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82056">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">هنگامی که با یک املاکی مذاکره میکنید، بیش از حد چونه نزنید.
_چمن در خاک
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82056" target="_blank">📅 21:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82055">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دختره انتقام رجب زاده رو از قاتلش گرفت  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82055" target="_blank">📅 21:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82054">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bf0cb6c78a.mp4?token=OvSvloeVfxo2U9vx4UmKSCMwHkaPV-1rItyi1RwsXUr1gYHvXUA3Dkx8lxmi_O2RTa92aCBMfvdcDfWZX-NQ-ZA49B13mdsICjAJyKsdCJMmIRhqnpCAQ9HqqnArG7pcXAoP7H97GPrRYTjigDNqgHApHKMdHtxBhQ8Es7vQxLS_2VE3xBU8v4VX-ewc-svr64dwQSupeMZTkMW4QBAad4ToIqq3-jG7_wErUJXzNTz6_PpBmtMo_vUH2rMIKA5IPHQbOZCqCeL5Yg0lYGJswjqLy_NWGzznmSA5JQs9Do9sAXvUIpT_PhsJcCNPySsZ1DeaNHZAq80DvkwkkwvPTg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bf0cb6c78a.mp4?token=OvSvloeVfxo2U9vx4UmKSCMwHkaPV-1rItyi1RwsXUr1gYHvXUA3Dkx8lxmi_O2RTa92aCBMfvdcDfWZX-NQ-ZA49B13mdsICjAJyKsdCJMmIRhqnpCAQ9HqqnArG7pcXAoP7H97GPrRYTjigDNqgHApHKMdHtxBhQ8Es7vQxLS_2VE3xBU8v4VX-ewc-svr64dwQSupeMZTkMW4QBAad4ToIqq3-jG7_wErUJXzNTz6_PpBmtMo_vUH2rMIKA5IPHQbOZCqCeL5Yg0lYGJswjqLy_NWGzznmSA5JQs9Do9sAXvUIpT_PhsJcCNPySsZ1DeaNHZAq80DvkwkkwvPTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختره انتقام رجب زاده رو از قاتلش گرفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/82054" target="_blank">📅 21:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82053">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ:
-
من می‌بینم که نمایندگان جمهوری اسلامی ایران درخواست غرامت برای خساراتی که در طول درگیری نظامی پنج ماهه گذشته به آنها وارد شده است (آغاز شده است زیرا آنها سلاح هسته‌ای نخواهند داشت)، حتی اگر هرگز در هیچ یک از مذاکرات یا جلسات ما ذکر نشده باشد! اما این ایده جالبی است زیرا اکنون من نیز از ایران برای همه افرادی که با بمب‌های کنار جاده‌ای و بسیاری از درگیری‌هایی که به خاطر آنها مشهور هستند، کشته و به شدت زخمی کرده‌اند، از جمله خانواده‌های کشته‌شدگان در ناو یو اس اس کول و هزاران نفر دیگر که در جنگ کشته شده‌اند، غرامت می‌خواهم. علاوه بر این، باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است، غرامت پرداخت شود، و ۵۲۰۰۰ نفری که در پنج ماه گذشته کشته شده‌اند را هم نباید فراموش کرد. من به نمایندگان خود دستور داده‌ام که این موضوع را به طور جدی در هر مذاکره و تمام مذاکرات آینده قرار دهند.
-همچنین، در رابطه با مذاکرات ایران، ایران باید مسئول خسارات و مرگ‌ومیر ایجاد شده برای مردم لبنان، سوریه، یمن و غزه باشد! رئیس‌جمهور دونالد جی. ترامپ.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82053" target="_blank">📅 21:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82052">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgnTIYIUCiqVT6bhRVtJaWDZbNseR2fsuXJnM5sGZ3weJU4k0xalcg8ThF3u0tg6HDbHN0WxvoD-VVVQgjj_voxeA--DJPBkaIT-F_on3M_nqV7jt298iRqfT_aDIJm7QBbpX24Ew9MPnX0iwFHHQG6OR2QubkfD8YDlevjPWjwBa3ueKt9O5VFsZ5aQSkawhzmKEQW3-7Iy5OcO0bDFioWLbVOWQOnBJWICAzwuf-qTgIQ2iyXUNrGy4aeq1Vbph3sNBWOywGfJcdCDnLr8QFoSBswOxMKJz1ckz531mOE4hKVQmhnAH3Cmttps_aK4q6lA3IWeYHe_hG9L7Ak8SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برید امضا کنید لطفا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/82052" target="_blank">📅 20:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82051">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0KEhXlldRHPnwSSbpo941L-c0nMyzIuYcOQVYOCn2F50j-I5frCCw8TX6N6xooOiNNyoq32xA2ICf2C6sz9syw_PngLlqaFuheJD41fxCJHPiiHvRRBf6r7SRoSOqqojFs6KsqVdS0-Alsd8JzkwVqz4Fthh9yqU7DFRs_lAIpOngjsKZhAOKvh99h_NJOn2GJbHrCzGJaQIlMsQk7inj5I6cz9GnjslWaly51Mt1iGC7TSNCXoGoUBEOvPdQ2oRs6GXiY3ivsZ4pheVtZQ_ZrsHcOwdSeenZfuCQoO9fvo_-OZDOZIcPg_-N84MT1pFWTn0bIBwpO2CZ2kmZ2C9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزش سه تیتر زده جهانبخش رفته تیم صدرنشین لیگ هلند، حالا چند هفته از لیگ گذشته؟ یک هفته، و تیمه پارسال ۱۳ ام شده بوده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82051" target="_blank">📅 19:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82050">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5c48QTmQd8wsd8Vv-k_gOAf7yp7nRlZJ5sfDd-smkjY0X9FLU-X-ybIuprSroThFhx-TKgBWqOjTvUY0eYqyYHMN2-creGsZbCnppkuJwroZ_xoTdfnq8yI1boXDyFYeUGzri-yzpi4aGvP8eKkduSlsw8aJvcJ7jeJ0r7a0Jecudy14M7h6aq_VBi0c2KNodAUrUWS81C4-o5FPlyKmKDp4ha0sX8nKhb-m8cqJJ9UCpwRcR6SBUTcXM0F6r7L0c8xsjbByynJ9RxPBwQuZE3R5GFSovAMAVy2Yi1fabmpwGHfAnsgaIUCDKSLsQlT6iBL815Hc4dFtpoXiSFf4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرومزاده
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82050" target="_blank">📅 19:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82048">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7uyuIjXuW7WAUFZWDdZz-TnuyQtHvm7s_HN9hJZlqMrQtEi63JX1Vv89pU18mu1RbP9xIWd2GzxTQJJ9g3i9f1m2fmUL0I6Z40lTudK1MvJB2g5fJetpkWt31xW4lnzD0-OJIg0Ogpo0klKl6CF1bPhNgjG2oiXTFNl7GU_1RWrYjWg_-DUuxNmCyDSM4SZaVestgzv46wm2CunpafQbSEQeK5_6kK_o3ssOJ0GG6NbIIz8xQpxdxa4YYrhO8QAk5PjTXXB9MdT84DGK9Pv7YWzoCgTI74N_K_IwubHhrP7CPxiHjecQENaA6HCpIKBIOmUs81t0MxnwOdVihfnMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید بانو لنا
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82048" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82047">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhtDZN6S42rsnOzN6GC6szpuiwhS339W59I4RSnrg40RIS7J6bY64sCrfMthX7PpXRYcXp8xHy_QkBuf3BXXFuU8jrkjIynBxr305_L7G0AzuSKXYL9q_SNL6U2riyRYB6tyDavpmF7NbGWWultpSdmw5WAXfQS9cyY79N7y9knTJVD-CDVdEfktmz48N586VzhViN4P89NbAZ86rq1ZkyfKRtHtMcFr-B6N3r5rht_fcte4Sm20WLa4rqNlRY30jKR4Qy6wZuGMBBrxwDM_G4xiA2FBGfE1A2Rk7iUK3GAXgW1dMBFYrsWREymBpdgoEAeLdB1ayoDjeyDp1uqKzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوماد‌های سابق و فعلی علم الهدی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/82047" target="_blank">📅 18:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82046">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">زن ابراهیم رئیسی با احمد مروی, تولیت آستان قدس رضوی ازدواج کرد.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/82046" target="_blank">📅 16:44 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
