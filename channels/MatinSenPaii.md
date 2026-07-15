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
<img src="https://cdn1.telesco.pe/file/AhyDjRcMrJHi5PIDi85840oPbdXn-aCpMbQsU3yKK5WL0hJ5XnEtr4WFV36u6ARtQEBurSUMYjPftuyYMM5oyDlLjxwUCTzxnMuWZQd8LzKKICHs7TdcmDgkS1aUbqitt2W-7Fl1EyjHIHGofkYcCIoDaSpF6mvsjdw6UwToZWuPshrofECKY1SVYvMWUa98w3WXiO7QG2sJoFYcUntjkcBqxsvW9JPiAA71JnHjSNVS-4U-LdQNrR9ZhmnFoYpIAt2CD9Tphb_QkTPrMc2VsbqpZX6kXBxDavZ1yvP8Zr-Lc-8T7zZ0eYJAmICqkDuhCsPMnE1duqXc1GkdTUSbTw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 158K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPaiایمیل کاری: matinsp.job@gmail.com</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 14:36:21</div>
<hr>

<div class="tg-post" id="msg-4499">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مشکل گیر کردن روی answering setup prompts رو هم برق برگشت سعی می‌کنم برطرف کنم
🎨</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/MatinSenPaii/4499" target="_blank">📅 11:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4498">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">و رفقا در مورد ویدئوی قبل و اسکنر، من مشغول کار کردن روش هستم که اسکنر رو خیلی خیلی قوی‌تر و پایدار تر بکنم روی اینترنت‌های محدودتر مخصوصا نت همراه، و به زودی ورژن جدید SenPai Scanner همراه با نسخه‌ی اندرویدش قرار داده میشه روی گیتهاب
تا اون موقع با تعداد ورکر پایین(50 یا زیر 50) و با کانفیگ‌های BPB یا Edge یا پنل Nahan تست بگیرید. با خود Cfnew تست نگیرید</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/MatinSenPaii/4498" target="_blank">📅 11:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4497">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">تمام تلاشم این بود تا قبل از ساعت 12 که برق بره ویدئو رو بذارم
🦆</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/MatinSenPaii/4497" target="_blank">📅 11:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4496">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n7_lz8RRLb9wtiUIBN74csPDiMcEl83XmDQgVaBJ1oiEAbYpZeiFx4KWjfl8ql9dqdCW5ckPmRDMC-VvxfF7asjC_mzQUvDIrG_173CS0t8CQ2u3W6blxZvWbgOVF2qaRRc4WfuHF1N54MIeBfSXqHA2cNdYdtEHYOLC2U7XYYHaOeuLAT9HRHq2QpP4JMC5-OQfxcMPBOD0iIjF8Yu3qIqJrg7-yaOqBWrom002Zowd-kuH3KKMMBlqSNMMwjisq5xQqAuB2wbA_Jn2exGTGcGZTQZHuMVeZxB7fbHtLbCRnoPBFFW6IG8_oWH-dy7HtuuXzcymDL_Vb7rHaQtHvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
اتصال رایگان و پرسرعت با پروژه Aether + پروتکل ویژه گیم Wireguard
⚡️
لینک پروژه‌ی اصلی:
https://github.com/CluvexStudio/Aether
لینک پروژه GUI من:
https://github.com/MatinSenPai/Aether-GUI
دستور نصب از ترموکس:
curl -fsSL https://raw.githubusercontent.com/CluvexStudio/aether/main/aether.sh -o aether.sh && chmod +x aether.sh && ./aether.sh install
دستور غیرفعال کردن محدودیت مصرف CPU و باتری:
termux-wake-lock
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش‌نیاز فنی و نیاز به خرید سرور و... نداره. حتی نیاز به اکانت کلودفلر هم نداره
😂
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/MatinSenPaii/4496" target="_blank">📅 11:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4495">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نفر اول:
دوست ممد
🥳</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/MatinSenPaii/4495" target="_blank">📅 10:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4494">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">آموزش رو ضبط کردم. قرار میدم واستون کمی دیگه</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/MatinSenPaii/4494" target="_blank">📅 10:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4493">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">متشکرم از همه‌ی دوستان بابت فیدبک
روی ایرانسل و مبین نت اختلال بیشتره، مخابرات و آسیاتک و همراه اول جواب بهتری گرفته بودن همه
برای گیم هم Wireguard بزنید. نه warp on warp</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/MatinSenPaii/4493" target="_blank">📅 08:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4492">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4492" target="_blank">📅 08:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4491">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اگر سؤالی دارید، توی کانال سازنده‌ی اصلی هسته‌ی پروژه بپرسید:
https://t.me/CluvexStudio</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/MatinSenPaii/4491" target="_blank">📅 08:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4490">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CzuNTN4U2AqDOL4STq14Kh-Q679C3-86y955PoejeId4yN_22NTnMUzIjlk4yyeSfYOnT5Y-DTyRfBHVu2HfDMdGif0SJ7xTdDCfc-Q2XPdof5CxR-ENLBoKvoCUj8d-VQEEu9rDqztRDsyGHRwLBef6Iq2AUv4ie1-M7msmxnLzPTlLdL4GRnZOis96-ALyW3do7y8JwptI4Gl67iNX3UtWfNJqRzZXUXL2L21Y7CgmCmQ477Oufe66oKJpFg-WB8uIjw73GeulcvJou5-IiTi1GJNlB5_YwdudVY9O5TC6TqhqP-3getbldi08ZGVaP_UFrGY_R2eEsXN82woarA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقت کنید که Wireguard آیپی ایران نشون میده(نه آیپی خودتونو)  ولی Warp on Warp آلمانه اصولا بعد از کانکت شدن هم خیلی راحت روی V2rayN بزنید و وصل بشید: socks://Og@127.0.0.1:1819#Aether-GUI</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/MatinSenPaii/4490" target="_blank">📅 08:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4489">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">هنوز کسی سر گیم فیدبک نداده
👀</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/MatinSenPaii/4489" target="_blank">📅 08:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4488">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sknl_i6LaVivZoYigq5mEYY_R1Ghf_ihGKbdVLSDnE7KH61zIEgXshgInV1eYp2rSlxMbHNZSaEZrCQBkas18PZXyq5AEjEdx4TEcurZX-AaVWlqV5mrYGrdnr990GTup-4K0-T-BRuZDyyP4vKxxu4-vmuivw3I1Fc6Y7j6TxZtbz99KDFBX2Rldqnt1QnWNQc_ko0O7fm3XXPNT5X-kKNzc6dBFrzDQfao4FmV6VhIlMzm7AUQ8dYJ-y5v3AhG-6IJZ_0hxkKC6UIe1hZ9gDxzmWx_wgl2dLSY6CPmRbOI4gREdLqfz941hyQR1TdT5LQd9YqbxHpkFeterOz3wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر این ارور رو مثل دوستمون می‌گیرید، پروتکل‌های wireguard و warp on warp رو امتحان کنید و همچنین scan mode رو هرچی از چپ به راست ببرید، سختگیرانه‌تر جستجو می‌کنه</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/MatinSenPaii/4488" target="_blank">📅 08:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4487">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">موقتا نیاز دارم بچه‌های گیمر سر این متد Aether بهم فیدبک بدن، ببینم تا چه حد پاسخگو بوده براشون هر پروتکل(یا اصلا نبوده)
https://t.me/MatinSenPaii?direct</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/MatinSenPaii/4487" target="_blank">📅 08:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4486">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4486" target="_blank">📅 08:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4485">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">به همین راحتی</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/MatinSenPaii/4485" target="_blank">📅 08:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4484">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خوبیش نسبت به Worker کلودفلر اینه که محدودیتی در کار نیست و همچنین دردسر اضافی هم نداره.
سازنده هم لطف کرد اسکریپت راحتتر واسه ترموکس نوشت:
https://t.me/CluvexStudio/254</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/MatinSenPaii/4484" target="_blank">📅 07:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4483">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بفرمایید دانلود کنید. قبلش با سازنده‌ی پروژه مشورت کوتاهی داشتم و اجازه گرفتم که روی یه پروژه‌ی مجزا GUI رو بنویسم دنبال راهی هستم که همچنان اتصال راحتتر بشه. فایل Setup رو دانلود و نصب کنید https://github.com/MatinSenPai/Aether-GUI</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/MatinSenPaii/4483" target="_blank">📅 07:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4482">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یه ‌GUI راحتتر واسش نوشتم روی ویندوز</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/MatinSenPaii/4482" target="_blank">📅 07:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4481">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">روی گوشی درست نمایش داده نمیشه</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/MatinSenPaii/4481" target="_blank">📅 07:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4480">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خیلی خلاصه بگم:
فیلترینگ به‌طور معمول دو راه داره برای شناسایی:
(الف) دیدن امضای مشخص پروتکل در هندشیک،
(ب) بلاک‌کردن آدرس‌های شناخته‌شده یا کل ترافیک UDP.
حالا  Aether راه (الف) رو با تقلید از HTTPS معمولی + نویز خنثی می‌کنه، و راه (ب) رو با اسکن دائمی آدرس‌ها + قابلیت سوییچ به TCP (h2) دور می‌زنه.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/4480" target="_blank">📅 23:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4479">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eV9gzNDiR8Cx2GfAu4RTE4WDZhVO15jBebD7GmrSSatj6ahSnIWL97EBYnBf9rtiQu8385-42HqsuYVFc-bYrp8Ta4EG_wcVpzldUqK2pJQpHU2mOpmHc3kgA7yVl4gkAUlDRXO4xCHnxYcjOssL5l2yHYjI2NyFirW8tbIsdgmaKGuRryBTqea9BQrIewGjhr2qxvRXi4FlxP0qAf7OdEuHGHudTAqUZNT-2OD8AFVWEhT5wjYZYVeephLcDmbpUF15-ZZ852JeZ0W3F-ISXrv-RWpvJueaAqj1U4tw57xkE14zCPvNGbrNvuewGVvjRSMq_CGoTjlTIzgXJILXtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/4479" target="_blank">📅 23:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4478">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/4478" target="_blank">📅 23:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4477">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">به زودی آموزشش رو می‌ذارم. هم دسکتاپ هم اندروید</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/MatinSenPaii/4477" target="_blank">📅 23:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4476">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
خلاصه از متن و ساده کردن برای دوستان مبتدی:
شما فیلترشکن oblivion یا وارپ(
1.1.1.1
) قطعا میشناسید.
این فیلترشکن ها تا قبل از دی ماه خونین متصل بود و شما با تنها وارد کردن یه مقداری مثل ip شیر و خورشید متصل میشدید ولی بعد از اون ماجرا ها از کار افتاد و هسته عملا بروز نشده بود تا الان.
حالا یعنی چی یعنی واسه
#اندروید
و
#ios
قراره هسته اپلیکیشن هایی که مربوط به این روش بودن بروز شن و شما بتونید با اپلیکیشن هایی مثل:
Oblivion
(اندروید)
Defyx
(ios,اندروید)
💡
نکته:فیلترشکن defyx رو میتونید بریزید و از یوتوب بدون تبلیغ و سرور های معمولی به صورت نامحدود استفاده کنید.
متصل بشید خلاصه بود از این پروژه وارپ این وارپ.
متین به زودی آموزشش رو میگیره
❗️
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/MatinSenPaii/4476" target="_blank">📅 23:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4475">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Yr1dq79UsoM39HREJbioIgO6Su9Isu-GlIzWNpo4Xb3b00VBGoZa_Go5J6h_OH-GWbU0qwvJNtfXoybAIYlqlPmJrRLRLBnyXgIzLrElogf2vu8XmiwiZWrXGKSUbY5NN62jn3C0xrtjrv9p-Ij5tu84qImCye732JIvOFL3XT8_xOeaqjHOIHNNVYLWs3okZbk_8_32mLBq67s2kaONkhYgvlf8QkMNiiZM3wpJtPHJkbQR7vG8F7I2wgeCGsMqvJc_-keGC8PRQhAkJpgacbnaIfbVQ1QqX19pD66F3_ZS3FkaXA7L7vIG9KxMunfG-2eov9G5woKFoiES9yo9RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوق‌العاده.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/MatinSenPaii/4475" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4474">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">الان خودم ران کردم و حقیقتا جالبه</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/MatinSenPaii/4474" target="_blank">📅 22:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4473">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اگر ارور Port already in use روی ترموکس می‌گیرید، باید لوکال پورت V2rayNG رو از ۱۰۸۰۸ تغییر بدید</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/MatinSenPaii/4473" target="_blank">📅 22:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4472">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">Aether یه پروژه‌ی شبکه سریع و مقاوم - برای اینترنت آزاد Aether  با ترکیب Cloudflare  پروتکل MASQUE (روی QUIC/HTTP3) و WireGuard به‌همراه چندتا لایه مبهم‌سازی ترافیک خیلی کمک میکنه از DPI و فیلترینگ شبکه رد بشی  برنامه خودش به‌ صورت خودکار بهترین Endpoint موجود…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/MatinSenPaii/4472" target="_blank">📅 22:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4471">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">Aether
یه پروژه‌ی شبکه سریع و مقاوم - برای اینترنت آزاد
Aether
با ترکیب Cloudflare
پروتکل MASQUE
(روی QUIC/HTTP3) و WireGuard به‌همراه چندتا لایه مبهم‌سازی ترافیک خیلی کمک میکنه از DPI و فیلترینگ شبکه رد بشی
برنامه خودش به‌ صورت خودکار بهترین Endpoint موجود رو اسکن و انتخاب میکنه پس نیازی نیست دستی چیزی تنظیم کنیم یا دنبال سرور از پیش‌ آماده بگردی...
روی شبکه‌هایی که فیلترینگ سنگین و پیچیده دارن هم عملکرد خوبی/عالی داره چون از پروتکل‌ هایی استفاده می‌کنه که خودشون رو کاملاً شبیه ترافیک وب معمولی نشون میدن. :))
پروتکل‌ها:
MASQUE + WireGuard + WARP-in-WARP
برای MASQUE هم به‌ صورت پیش‌فرض از HTTP/3 استفاده میکنه ولی اگه تو شبکه‌ای هستی که HTTP/3 یا QUIC محدود شده
میتونی بری روی HTTP/2 که سازگاری بیشتری با شبکه‌های محدودتر داره.
یه اسکنر داخلی هم داره که خودش endpoint های سالم رو پیدا میکنه و انتخابشون میکنه :))
مناسب هم برای شبکه‌های به‌شدت محدود هم شبکه‌های عادی.
پشتیبانی از:
Linux، macOS، Windows، Android/Termux
دانلود:
https://github.com/CluvexStudio/Aether/releases/tag/v1.0.0
اینترنت آزاد برای همه! :))
بزودی توی Defyx و Oblivion هم اضافه‌اش میکنیم!
داکیومنت فارسی/اینگلیسی هم کامل نوشته شده توی گیت‌هابم حتما بخونید:
https://github.com/CluvexStudio/Aether</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/MatinSenPaii/4471" target="_blank">📅 22:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4469">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oMWT0pU9hPdVNoj5wr4g_tXwWoPaMx7qsGOEY8INemRqUgpJYy7PDWPqOaV_iDL-xVyMlKW0rzrSYqGHdGYtRLj0kIRN2CwVzj1sBbdrOhyFaXRDEfXTj4YQlSpeJpITk4qTDhgqEXcJqTbhdDjbkyWyX7uzgtdiMVoWzcZD0l2g-ix6mMoJZWl9SPSLUklPCKIIoXFO5NF4LUdywi86d6LlhVVAGQsZue9rY6o0c8x_NMWRD6B9dEadRZn-GFbWf0ddiX4v4ldl2Udmx5CqrJDqK-57i73qlSuHC9DqXi2BvRYN-EI1m2OfNa_Lvtld9_x3wpT_rg78p_1IQKuZHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vgNNgU2y5jOL18MI11gKf1Boimg5nRzUDaIWR7SnQ8cQs8UXHKbL-Ee_a9DmZlRUyyZ5iZm0ebnE9mcGO5wPV5dSxQltuol5D5mwOJrEztZcBKvE5h4ppnfsaQ0KsQ1aYHeyRQq9ysOmIK3KaOBdGFRSIpL1Jj-Ski-NWKtwtBHYmtxgtrqdIvbYIIFdcO1XMb6E6k-QnIvsaEXMZrGkFuJNiNyl9qEcZNzkk2-wvIeCtCirfkgNXbjReH8Eg1D_FY7KfSHDYW85G9KK_UBMEGF2LmIIrQnfINBTqAfzfEbuaCfWrFd0Hwpn9lPD3Mm2qe7qqEuFhj-T_VOLdsg6CQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از کلاد خواستم که
https://github.com/Graphify-Labs/graphify
رو نصب کنه روی پروژه‌ام(کارش اینه که کل کدبیس رو تبدیل به یه گراف دانشی عظیم می‌کنه تا Agentها به‌جای باز کردن مداوم فایل‌ها و دنبال کردن importها، ساختار پروژه و ارتباطات بین بخش‌های مختلفش رو مستقیما درک کنن) و کلاد ازم پرسید داداش مطمئنی میخوای اینو نصب کنی؟
زدم Proceed که آره مطمئنم
دوباره رفت یه کم دیگه گشت
گفت ببین این پروژه تازه سه ماه هست اومده، 86 کا استار گرفته روی گیتهاب. خیلی مشکوک میزنه. نصب نکن چون امکان نداره یه پروژه یهویی انقدر پیشرفت کنه
😂
😂</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/MatinSenPaii/4469" target="_blank">📅 21:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4468">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ly_8C_BvUKp0XIwjp9biG-KPvhfcPEn0I9pUfckv06iN7XIAUY0JDehP39wilhoIOH7a7vewTIc0KGJEzgtfbfC40oqEz5FtJMY_hEWDg503VqBrD1tafKC_RHRQeDPjFcVFN-8R46y0U-LbIf-J1FfvwB0W0Zqa5ddxnT1UrSMQY4MvvpcFkIywQuMhk69L73dHfqZei9_ypXiv0qGh7kL8qlrNDG-N8rHAhmGG-PhLjVCJUkwnVMM-dGGSGU3j4KF7GrKThq6PKYws2iSdj1WTjZngVx8OKusIGc4k-PIpnZQR_1uaQ-JxBUGEnXQAgH-zMssKhQEkEf5-xR7MJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب رفقا گویا دامنه‌ی
t.me
مجددا در دسترس قرار گرفت بعد از توییت پاول</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/4468" target="_blank">📅 19:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4467">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ببخشید.
خودتون میدونید دیگه بانو
❤️</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/4467" target="_blank">📅 19:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4466">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/a54ac3d5b4.mp4?token=fzNzXcU_19f0yRJh9ZT7JFeQVyhhySj_sSy-9nq5Jla0ylFiyL2Ez9ntQbmptm_edi7sNZUWEivJZLYW-bejHqfx6p3Kw0F1zfCh74P-AkHojlLjCPejzpjh8Dzzs8QkfV4AmOl1AJ_b2TpErQb2gC1Va7eDXTXofT86_KwFv0JZT1bs1vfmJUE_4-zyhPmDEwLjhOtT9vOwARyq19oidJ1pdT7kXGa6kTWR1rYU2Me5Gaexq-woZe-7p-53QwMY6HT5ZjWxaN77z6rmHR9OeLrceKO31Z9Y0JP_iWGeQ9bhMt2dAi9tPMfEJKnLgffYPvO9RwUZc_QMSWVmF5SEKA" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/a54ac3d5b4.mp4?token=fzNzXcU_19f0yRJh9ZT7JFeQVyhhySj_sSy-9nq5Jla0ylFiyL2Ez9ntQbmptm_edi7sNZUWEivJZLYW-bejHqfx6p3Kw0F1zfCh74P-AkHojlLjCPejzpjh8Dzzs8QkfV4AmOl1AJ_b2TpErQb2gC1Va7eDXTXofT86_KwFv0JZT1bs1vfmJUE_4-zyhPmDEwLjhOtT9vOwARyq19oidJ1pdT7kXGa6kTWR1rYU2Me5Gaexq-woZe-7p-53QwMY6HT5ZjWxaN77z6rmHR9OeLrceKO31Z9Y0JP_iWGeQ9bhMt2dAi9tPMfEJKnLgffYPvO9RwUZc_QMSWVmF5SEKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای خودم نگهش میداشتم
👍</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/4466" target="_blank">📅 16:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4465">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">Lira’s first challenge
🌟
به اولین چالش لیرا خوش اومدید!
🤍
این چالش برای همه‌ست؛ فرقی نمی‌کنه تا حالا از لیرا خرید کرده باشید یا نه. فقط کافیه توی این سؤال با ما همراه بشید، چون باور داریم گاهی یک جواب ساده، می‌تونه پشت خودش یک داستان قشنگ داشته باشه.  اگر…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/4465" target="_blank">📅 16:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4464">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLira.</strong></div>
<div class="tg-text">Lira’s first challenge
🌟
به اولین چالش لیرا خوش اومدید!
🤍
این چالش برای همه‌ست؛ فرقی نمی‌کنه تا حالا از لیرا خرید کرده باشید یا نه. فقط کافیه توی این سؤال با ما همراه بشید، چون باور داریم گاهی یک جواب ساده، می‌تونه پشت خودش یک داستان قشنگ داشته باشه.
اگر برنده‌ی این شمع می‌شدید، برای خودتون نگهش می‌داشتید یا به کسی هدیه‌اش می‌دادید؟ اگر هدیه‌اش می‌دادید، اولین کسی که به ذهنتون می‌رسه کیه و چرا؟
برای شرکت توی چالش:
⬇️
در کانال لیرا عضو باشید.
⬇️
این پیام رو توی کانال‌تون که پابلیک هست فوروارد کنید.
⬇️
به سوال بالا پاسخ بدید.
🎁
جوایز:
🥇
نفر اول: یک شمع کروم صدف لیرا
🥈
نفر دوم: 15% بن تخفیف
🥉
نفر سوم: 10% بن تخفیف
مهلت این چالش تا ساعت 12 امشب هست و نتایج چالش فردا ساعت 10 صبح در کانال لیرا قرار داده میشه
🩵</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/4464" target="_blank">📅 16:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4463">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مثل اینه که یکی با Toyota دزدی کرده باشه
برق کارخونه تویوتا رو قطع کنن تا دیگه نتونه ماشین بفروشه به دزدا</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/4463" target="_blank">📅 15:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4462">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromوب آموز(m J)</strong></div>
<div class="tg-text">دامنه t[.]me تلگرام به دلیل تحریم OFAC آمریکا از دسترس خارج شد.
در ۱۳ جولای ۲۰۲۶، دامنه کوتاه t[.]me تلگرام (که برای لینک کانال‌ها، گروه‌ها و پروفایل‌ها استفاده می‌شود) در سطح جهانی از DNS حذف شد و مرورگرها دیگر نمی‌توانند آن را باز کنند.دلیل:
ثبت‌کننده دامنه .me (Identity Digital) وضعیت serverHold را اعمال کرد. این اقدام مستقیماً به دلیل تحریم‌های OFAC (دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا) بود. OFAC شرکت First VPN Service (1VPNS) را به لیست تحریم‌ها اضافه کرد — سرویسی که به حداقل ۲۵ گروه باج‌افزار (از جمله Avaddon) کمک می‌کرد تا حملات خود را پنهان کنند. یکی از شناسه‌های این شرکت، کانال تلگرام t[.]me/FirstVPNService بود.
چون نمی‌توان فقط یک لینک داخل دامنه را بلاک کرد، ثبت‌کننده کل دامنه t[.]me را از DNS جهانی حذف کرد.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/4462" target="_blank">📅 15:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4461">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">جوری نوسان برق رو اعصابه که هیچ کاریمو نتونستم برسم کل روز. نه سه راهی روشن میشه که لپ تاپو بزنم شارژ، نه نت فیبر نوری کار میکنه کلا قطع شده از صبح، نه آنتن درست حسابی مونده و همش قطعی داره، نه کولر کار میکنه که بشینم لااقل یه کتاب بخونم🫩</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/4461" target="_blank">📅 14:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4460">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">جالبه که هیچ توضیحی بابتش داده نشده
هیچ واکنشی هم از سمت تلگرام هنوز ندیدیم</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4460" target="_blank">📅 10:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4459">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگیفت بازار | Gift news(𐌼𝛜)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJAsfevMuSJNnWr3OArOpST4dP2SyaHBRaGRgXpHTywAfSM2dTZNrWPo4mZ5q1vYcnrTCnuaYBz_JWu1GrM45J45-f1PXTTiWpJXhcUzngWN9mGebBoKrdwjLo0-g6QEezxqwDUBaXtMLjft6oMRMxULNaRDYPPDlVZ6O8amrSjuMo8mL4jwV_JmzrKPdi9w51mZtXfJJo1_9Gb4Q1kKMrFSZxMxfb6ZXeI7KRbPmQa0T3m1hxDAffSB7iK0N8ed2VYwCpWpP-w7M9kOCddJRU02bq-gJDi-hjg_JHWz64E7Z9mz8husz8fQaa5vnhd_ttTatyfu1APCpW22lRHnQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💸
اختلال در لینک‌های
t.me
از ساعاتی پیش، کاربران زیادی گزارش داده‌اند که لینک‌های
t.me
باز نمی‌شوند.
⚪️
طبق اطلاعات
WHOIS
، دامنه‌ی
t.me
از ناحیه‌ی DNS رجیستری .me حذف شده؛
اما همچنان تلگرام واکنشی نسبت به این موضوع نداشته.
ℹ️
اگر امروز موقع باز کردن کانال‌ها، دیدن تصاویر گیفت‌ها یا ورود به بعضی لینک‌های تلگرام به مشکل خوردید، دلیلش همین اختلال است.
📰
تا برطرف شدن مشکل، ممکنه بعضی از لینک‌ها و سرویس‌های وابسته به
t.me
به‌درستی کار نکنند.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4459" target="_blank">📅 10:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4458">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">الان برای یه سری کار داخل فتوشاپ، چندتا اسکریپت با Claude (پلن رایگانش. توی صفحه چت) نوشتم که کارم رو 20 برابر سریعتر کرد.
بهش فکر کردم، و به این نتیجه رسیدم که اگه فتوشاپ بلد نبودم طبیعتا نمیدونستم میتونم همچین کاری کنم.
از طرفی اگر از قابلیت‌های AI باخبر نبودم که میشه اصلا کارها رو باهاش Automate کرد یا لااقل، پرسید که "آیا فلان کار رو میشه Automate کرد یا نه؟" هم مجددا همچین چیزی به ذهنم نمی‌رسید.
اینه که شما به صرف بلد بودن کار با AI شاید نتونید از 100 درصد پتانسیل یه ابزار استفاده کنید،
از اون طرف به صرفِ "خوب" بلد بودن یه ابزار هم اگر از AI استفاده نکنید و سنتی کار کنید، به راحتی عقب میفتید.
هر دو با هم عالیه!
<تجربه‌ی شخصی. نه Fact></div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4458" target="_blank">📅 09:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4457">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚀
انتشار نسخه نهایی و پایدار MTProxyMax v1.4.0-LTS</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/4457" target="_blank">📅 09:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4456">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">📱
دامنه t.me تلگرام تعلیق شد؛ قطعی ناگهانی لینک‌ها در سراسر جهان</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/4456" target="_blank">📅 09:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4455">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">توی علم روانشناسی به «جوک ساختن با قضیه‌ی جنگ یا قطعی اینترنت» می‌گن طنز سیاه (Dark Humor) یا طنز گالوز (Gallows Humor). این یه مکانیسم دفاعی برای بقای روانیه، نه نشونه‌ی بی‌خیالی. مخصوصا سر قضیه‌ی جنگ
1- جنگ یعنی استرس، ترس و درموندگیِ مطلق. اگه این حجم از فشار رو سرکوب کنیم، عملا از لحاظ روانی مریض می‌شیم (و همچنین در بلندمدت می‌تونه ریسک PTSD رو افزایش بده.). جوک ساختن مثل یه سوپاپ اطمینان عمل می‌کنه و بهمون اجازه می‌ده این فشار رو به یه شکل غیرمستقیم تخلیه کنیم. (در عین پذیرش واقعیت، تحملش کنیم)
2- خندیدن روی بدن جواب می‌ده. سطح کورتیزول (هورمون استرس) رو می‌کشه پایین و اندورفین (هورمون شادی) ترشح می‌کنه. تو شرایطی که ضربان قلب رو هزاره، مغز با یه میم خنده‌دار، ترمز دستیِ استرس رو می‌کشه.
3- جورج ویلانت طنز رو جزو یکی از «بالغانه‌ترین» مکانیسم‌های دفاعی طبقه‌بندی می‌کنه. توی این حالت، ما واقعیت تلخ رو انکار نمی‌کنیم، می‌بینیمش؛ ولی با طنز یه فاصله‌ی ذهنی باهاش می‌گیریم تا بتونیم تحملش کنیم.
4- وقتی دوتا کشور می‌جنگن و موشک میره و میاد، شما هیچ کنترلی روی اوضاع نداری. اما وقتی باهاش شوخی می‌کنی، مغزت حس می‌کنه حداقل روی «روایت داستان» کنترل داره. با خودت می‌گی: "من نمی‌تونم جنگ رو متوقف کنم، ولی می‌تونم بهش بخندم!" این بهمون حس Agency و قدرت ذهنی برای مقابله‌ی نسبی با این قضیه توی ذهنمون می‌ده.
5- توی شرایط ترسناک، آدم‌ها به شدت احساس تنهایی می‌کنن. وقتی یه جوک مشترک می‌سازیم و با هم بهش می‌خندیم، یه حس همدلی‌ای این وسط شکل می‌گیره که تاب‌آوری جامعه رو مقابل این قضیه بالا می‌بره.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4455" target="_blank">📅 05:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4454">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mMih420tV6uoHRfqKnos9wMeiiPz_x89KrwORl7jBqxE4m4GFLzdrJZLCxzMdckvrktoOKCSOJvKLYl4dox2ubBdlje0RUumLgCQW4IH3qjxymjj2C1ciGvrylKLBX33Kf89Nk_BUFsAcoRZcmSHILiZ2MEhY7N3ChSpQCqXijV_H5jFiL4Wy2JVUsUDu7DK5kkr0rsDAO8lVZqaKCkR5295ZyWFRWN0TzZA2zAaqO0UzXQYv_n08dzsJsF6s6o_oQGf4_E9ywQNrSdWjeDEpV2reQbT_7Eoc-7xrmJ7wXGNUNSXb3NRXQG5sm3v1tAkXxgX7WrFC6ar4hqSYsb1vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتباطات زیرساخت در حال لحظه شماری برای دستور قطع</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4454" target="_blank">📅 01:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4452">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v0syYWETXK0T0PKn8RMltJfonzlWB0wGFWIFK5tBuNqMiyrhakaNDqzJPKyT4LQ8tMRI7fOBtAkxonWrWaKvolnZaHyX_UWAFHBEbP3yJniyyF1FTkN8xokmKFRlXE3mbfod3vtZQHefn6Nk8dajZiKmqx6qszECPSO7r_jdf9sc6smB0O2n7XARmsN7ETACAYY8iaPWiPBmUno12g5-DU8rEhkzYsCKicyaM8crsdvuVsY8qBT1J2Pz3E5-BySxgOf1cCvntxgLE-0pkx0sGxgViZKCKQbUsvr-6kbF8h5WHww_dVs9Shus-fiwljEncJFmLYCvMofy0UMhQgl3ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oerNw-ssoiDBAG2aQuLPOrouQoN1UE-I9fA4WaSW8C-1gIQ6S0Qj-M9NrpoG7y0WxLWrf-Kvb4EkzNr3xpnA2zikBp7AwG7YrjntyyxZVDzeaY-gQO48m5Z6tvvGl1jfSmaSSTSnCVJo1Pbw66-twJoI6QtFz-7co9OaKHarmL1YFHIVts1wVXmpHY9-UY0OrNtb-SlhU9n4PSmHRXgszmVXVTzn-dRghvPoMCr9BaIsPH6102cVZPDbfoaHcNqgI2TWWC0biPTDsz3hZHABj1CnUr3KQgcP6v11hL-umyO8v77hVTqJ2xzgrinyX34c0VP7o8MNWLxMeSfxvtT91A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فکر کنم من یادآور خاطرات بدی هستم متاسفانه
😂</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4452" target="_blank">📅 01:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4451">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge  https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4451" target="_blank">📅 01:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4450">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">Android</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4450" target="_blank">📅 01:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4449">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">Desktop(mac-win-linux)</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4449" target="_blank">📅 01:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4448">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">Master-White-DNS-@MatinSenPaii.zip</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4448" target="_blank">📅 01:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4447">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">امکان دانلود کل ریزالور ها به ربات @dns_resolvers_bot اضافه شد   @WhiteDNS</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4447" target="_blank">📅 01:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4446">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohammad👑</strong></div>
<div class="tg-text">اگه دیدین جایی نوشت
تهران رو زدن
ثانیه بعد نت قطعه</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4446" target="_blank">📅 01:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4445">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jjJHGhaOjgt6v0d2w7H9gDNJIN6GgFz-cR0pcDLAcrIp10WmmEhkLctQ4d6wPGDwDGiviPYN-uR6VjoNOGcMnqAtrI9P2hzFySCzzkn3IfFt1rFSgZXCB-xndZJeREwhNClNvKCNdJtd3L3vdHliYU4aMRAYBPLfosED1Uy8R6DcipQ2odZOl-Z0WHgDcQsmJtSTAgsg7tlMm_Fkcccs4QnV3QvJaK5ertF76CWjTsFL3FBesKB-HhjktJquzvkK7b9maWTwB0xN6wy8IFkrFobX0BXgtxTSTdTfVqMvGAuBBV6CwEbaNHcE7szv-FnClX1c4l0F1Ur7kJS_J86KbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق معمول، پیشنهاد میکنم WhiteDNS رو راه‌اندازی کنید برای خودتون و دوستانتون
آموزش:
https://youtu.be/6Pm7kNQb3mo</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/4445" target="_blank">📅 00:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4444">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHaoodi Senpai</strong></div>
<div class="tg-text">صابرین نیوز داره لینک چنل سروش و روبیکاشو میده.
این یعنی به زودی نت بای بای
😭</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/4444" target="_blank">📅 00:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4443">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBloom.(Tin.)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsWB0f_hchsknIziu7Ohoy5jAAHaUHbMACJF0BykOfH31i17SNlgMYe-a6IPBfFglMp003vQrDy4Wjvp1cvK3E8sd7u1afYyHuHFPphY8ridKzLdhVoSYy7YPWwYMQCADf-31tXPtsuixR211-YhY6ORVfnh2WFbz-dIOHi-fGxmEN1xlV64OouUkN0dLDLQZ2kMItsdZMdhmq8wA96RPTalM0soeoKaB12IoDAY3l1GdC-GxeByPfMUOGHipvNmYYfv2Vjm2Bg0ExIo9apFJuYsGFCnOVhq_LUL0_yeXuu5DxkdcVHVCJ1bLG15gZnV95VgGMWrKvLXnvbX7J0a4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Solomon’s paradox
“انسان‌ها معمولاً می‌توانند برای دیگران توصیه‌های منطقی و عاقلانه ارائه دهند، اما وقتی پای زندگی خودشان وسط باشد، اغلب نمی‌توانند همان توصیه‌ها را به کار بگیرند”
روان‌شناسان معتقدند آنچه ما را از تصمیم درست دور می‌کند، کمبود منطق نیست؛ بلکه نزدیکی بیش از حد به مسئله است. هرچه یک اتفاق بیشتر با هویت، احساسات و آینده‌ی ما گره خورده باشد، و درگیری احساسی در ما ایجاد شود، احتمال سوگیری ذهنی بیشتر می‌شود و تصمیم‌گیری، سخت تر.
البته که احساسات، بخش مهم و تاثیرگذاری در تصمیم‌های هر انسان است؛ اما زمانی که فرد با موجی از احساسات مواجه میشود، ایجاد تعادل به مراتب دشوارتر میشود..</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/4443" target="_blank">📅 00:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4441">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">معرفی  Rowboat | یه همکار هوش مصنوعی که همه‌چی یادشه!   یه ابزار جالب اوپن‌سورس توی گیت‌هاب پیدا کردم به اسم Rowboat. این ابزار در واقع یه «همکار هوش مصنوعی دسکتاپی» هست که روی سیستم‌عامل‌های ویندوز، مک و لینوکس نصب می‌شه. توی اولین نگاه هم شبیه هرمس به نظر…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/4441" target="_blank">📅 23:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4440">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4440" target="_blank">📅 22:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4439">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YB4NnvGLPhYSwInnm6QlCVWjjPttTqq4E7YwB-1R0bx3mRYVXJMDAEQvx3D0T0tO2K5zvxnGtekc9Bt6Efz66IWGhdhUkSVUGgbyDeDTMv_Zln3jv9aJFrZmOFNzZj8crJye-oE3vb4_1elF7mmIQCbToJXlYuV-vfmRACoQuAD26Dshm_ODUd-LYtRd5-2HQP31RdyTCbqdR94mZUyRQEmKx1yjk0scOH3851aohHlBwb28tK-JBF3bBXC9C1ePyZUoCBRClUpE0XBFjVSkWOirMtXxGXmtABzMoIL8RFn4xAxxAhbwqidJ4PLHO8y5EBiVYl520YugL9dfyZRzJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">8- بخش پایانی Integrations:
از قابلیت اتصالِ One-click به اکثر محصولات و ابزارهای پرکاربرد پشتیبانی می‌کنه.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/4439" target="_blank">📅 22:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4438">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hGXk8rfG1rMEibvdadpBUxyUDJqhxoBDkDRbPHoSCaFRgoxZZ7s5c7yvmn0uYwmf6tOJc3KTjtZVyFSQrORNATkvUrHoyCtuRyuKmIf72Dl9nC1C4Xb8yt9r_Th1eKJZAFnHNqClZGAlCWEMkKhYopQ9myReJNPOf2__JH7cW9sYQrZbuN80W0JYE2fxq1yiiM05s7IT70W-vWRTFKSFPyyo_p4oY8_2Z1jcA6TX57CzgJlWz9xNkOQO3QwyXhumG25cqLElF5Qyz4OFhYWHe9GyNmwHg_1vZF1qFV09tvHWEcsgBVBBTyp3ZJZBEs6nu8PrZjyCqFbVCvosShoDyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">7- بخش Apps:
می‌تونید فضاهای کاری اختصاصیِ خودتون رو داخل Rowboat بسازید؛ این اپ‌ها به تمام ابزارها و اتصالات دسترسی دارن و حتی می‌تونید اون‌ها رو با بقیه به اشتراک بذارید.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/4438" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4437">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CeKK_Z9tx2SQ1w8QuIb30317JMOVmXTBMsdzzamGJjr7eRiXKhza0HpQLB8y0GY_ksE-ZDjvKDJck0aFpB-5AFen0P5NNQ0hxZhGVlD2F5TIKrLtnssSRTtUs-7Y_sxkj3ye2I8H0mF3yOJEGy9ARKoOOptye50pR0yCG1SHGTbvX9KfLxnUgH750wYkoUVIbMhNZoUT3W3g2A1R_YwEn_QqS3SUG-7ZNjFFNYoZNrGq9SDWy8n531rBMyphff-ncLnX431fNw2GQu9pMUuHrHIEtf2zzGsRzXNLSSFn1J4fF8JgQs_fYJzTqspRMy1NfcZ0Ucutoct6Ak0OhrRorQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6- بخش Code Mode:
این بخش بهتون اجازه می‌ده همزمان چند تا ایجنت کدنویس (مثل Claude Code یا Codex) بالا بیارید تا Rowboat با استفاده از کانتکست پروژه‌هاتون، اون‌ها رو هدایت کنه و کارها رو پیش ببرن.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/4437" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4436">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aJRl_mtuzaq3ixFHE-2Hm6Fbd7Ew-nWwNWr1EV4kf7jSLkZcrCrCMtjj3vbRbVJdqJMRuw3y2U_y7Jc-NAlYYMXmANZfVLBZQ42P_yB3XQXVnHCxxzfyyMauMJma8D3JvbW7B6WfJ5C_9jiCMZW_Xp_pXNl-ej47jCJrcukY9BPrLrQqbA0fp03lXhnhuIeAe7-fyPNy6tPmOVvjfPqUgCRZ-7FXqS1uXJQC1UzWPb6n3gVh2YRAbqDqqTnLH5XC7UP-sE4ukc1oaHMioMR-r_banMo88OUvVcHI81OsBL3aegTkT-p-LuMrp1PjQctTgoTNXGNj4S6F7X0wCpLAKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5- بخش Meeting Notes:
یه دستیار محلی داره که مستقیماً به میکروفون و اسپیکر سیستم وصل می‌شه، همون‌موقع صحبت‌ها رو تایپ (ترنسکریپت) می‌کنه، در نهایت خلاصه‌ی جلسه رو تو یه فایل Markdown بهتون می‌ده و گراف دانشِ سیستم رو هم آپدیت می‌کنه.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/MatinSenPaii/4436" target="_blank">📅 22:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4435">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZwBvbAuMZJu7uN431QR6p47pSuC1iXMX51w2ZllXRuw1f99pQHyecDn8G1pDtBQkjTeIXXR-8Oz2BYKQKKS3kFkUJGpbRXUMYD4b4-eaQdNcdzEUlKpNaW3CNudDLlpaN-V85-mA7BN0gG5aU3i9Viiwv6zSfm5dPPPmMaUlJ8unmr2Gf6RqIv-Aj5htd7lcCWccmorMzMhKKFaqcYPZY8n4vIIZzhdrGbznT6kVE2f9b1Yq67mbbS6w79QsV_V7NDTERqX4H7H2AcKkqwzSqkgCyniFztd5hVSiV7D0RswHIQwAdBNeMug6ZABCgpu-ANJGclY4q9936Z-dWNKDqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4- بخش مرورگر اختصاصی:
یه مرورگر  Built-in داره که اجازه می‌ده شما و دستیار هوش مصنوعی روی تسک‌های وب با هم کار کنید. چون این مرورگر از مرورگر اصلیِ خودتون ایزوله‌ست، می‌تونید فقط تو اکانت‌هایی لاگین کنید که دوست دارید هوش مصنوعی بهشون دسترسی داشته باشه.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/MatinSenPaii/4435" target="_blank">📅 22:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4434">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EtlErp2Wvj3BSi3JNMRt0SUGNmLBHpuy-G7VSZmi-3aKPX64FuwsNJndkf1cSRFsS4cVjvvqyPB4HSlW8h-ExScKYlD44TTkDYj27w2TD18sZBtqMVSqSMJYT56xonrtby50fgl8WgHMkCsip7qZR9ieiiFJnlK7LaOxZcuihFce2dC_cZiMUsW7KZYB0UT5cZlCFITt5sJNmLcUsxrbc3vPbZXyaNABQW9fwokRVU839cuGs0hXtjoZH6ZmwDkapg6D-VqFyBLAIpmdqXS76LaVLT03JfYyJqAmEFCmmNNmlG1saLLBDpNLJGXRFJhjfQed9y_nTWWdRczoIHqxpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3- بخش Background agents:
می‌تونید ایجنت‌هایی بسازید که بر اساس یه اتفاق (مثلاً دریافت ایمیل جدید) یا بر اساس زمان‌بندی (مثلاً هر روز ساعت ۸ صبح) اجرا بشن. این ایجنت‌ها می‌تونن به ابزارها وصل بشن، تو وب سرچ کنن، از مرورگر استفاده کنن و حتی با Claude Code یا Codex براتون کد بنویسن.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/MatinSenPaii/4434" target="_blank">📅 22:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4433">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GEHuActMm7fHHvvgyLKZQ6r98SdjPm2Qg7RLi4slJEXoBb5iLwF941jme-cxLs1vKT9KtilIE0Cy7sCwz9X0GgJwNr6V3n8e1eZP8heZnQkMt18D-e1BfYc6EEsJ-l0Bfca213q2uphl-OQ18wWpKMDao_urEyy5Pm6J-TfT3MW1aUe6EtJvgZEzhs59DGSaCk2vyvxP-f0d42G7UR9ger8AgKXKU7rXw_C-TMOukvK5-XuA6_MDAaaaGZr8aj11ipjJ_BjAuhpHifgR0jBloIWI83yaMULlaMBZacQxs-mymi3wUSc9IwiI102BkOD_YtPE_61zbUHvFFsM1p6GJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2- بخش Email:
یه بخش ایمیل داخلی که ایمیل‌های مهم رو از بقیه جدا می‌کنه. بعدش با استفاده از تمام اطلاعات و دیتایی که از کارهای شما داره، به‌صورت خودکار برای ایمیل‌های مهم پیش‌نویسِ جواب می‌نویسه.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/MatinSenPaii/4433" target="_blank">📅 22:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4432">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jo2z2PjMpAsLC-952KOKmbt21KxMI_SOJGd1blGrF-VOvx3aiDeMqlqY7p7g4R_4Wan5ak-zgIJ17hTwsFgT-GmwgW7UZXPmoCAwxJ6m2mLHEGe8kIs-616GX7YZ3RLPVb8SOUC0FNX8603Uz9OdRq6lMZ0qjjZ6G-57EO3A09f3iYtB9005qXDO0tcytE-mid4H616Dqh-_zn8704ZfdOv-XrdvMNey65WYGjS4yMnx89csWf4e80KoF1W0hk6ouBC_E116mLRgKIsXmOwoadebY-GzNe8LKvM3wQOMf_hKegigUGggYjPW9yI7yJXuHWnhqb7GhIcdz-oLcDm9iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1- بخش Brain(مغز)
کل ایمیل‌ها، جلسات، پیام‌های اسلک و چت‌هایی که با دستیار داشتید رو به یه گراف دانشِ به‌هم‌پیوسته (دقیقاً شبیه استایل نرم‌افزار Obsidian) تبدیل می‌کنه.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/MatinSenPaii/4432" target="_blank">📅 22:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4431">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بذارید تک تک نشونتون بدم
👀</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/MatinSenPaii/4431" target="_blank">📅 22:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4430">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hhQlzXhu0R93kTbptpMoxExYcXae1LI0YWvvQFv2D-Gjhy-qnXpf2RkEy9lJcL-NJ2MuyyUE1tpqSuxHZPVD-FxCdbog2eLMN3JUm_lUSa0mSb_883HQUfT67caURu_HE4oDv0d5D3HZNMqTYU6yvbGglNhc5QTf3XpQVkz-IRSbifsrfrJg_ccU1lrxA6lBLAjhaOr0toNChE04QCc2a70BCT8-QV0VVN8BfJ7znAEkoNWrSzPBSKfbT14i5Dh-HT6PqEcNLX8ofk7Tq2Gfk5RyCeR6sY_XDtEi8ZFW0wxYOo5UK1XhfMogWFjqg-tOOR6HMgc9KF2HFOfAV2luSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی  Rowboat | یه همکار هوش مصنوعی که همه‌چی یادشه!   یه ابزار جالب اوپن‌سورس توی گیت‌هاب پیدا کردم به اسم Rowboat. این ابزار در واقع یه «همکار هوش مصنوعی دسکتاپی» هست که روی سیستم‌عامل‌های ویندوز، مک و لینوکس نصب می‌شه. توی اولین نگاه هم شبیه هرمس به نظر…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/MatinSenPaii/4430" target="_blank">📅 22:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4429">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AM5PJaqaH9bfsnZU1vG7yViKAGfLcCWlr6xIQG14nZtvHhuxUnBuTI-6BtaG4gqrIEUeezWHBX8Tx5Hs8ebvie80WoPLlqnZQtVk-fjjKtjlcB3dIqQA0xgb3WDzYVQjTFQIFjMYaSSgeNzMiC4uHgnzphcUHHQXHBCV1IKajTVuBWlRk_mazJGqAgI76Ss1NVq7zGh97weQgvUtQTDYWWKEvCytWp5hv0NjfWMQ1EdgOtiW1kjE8uEvZWWAnAIT75pxmPS2R2678DBGZhXmolFGM8Yk1Rse3AsSMja56AlUL7nG6bpK4Kzae1messgdG0ZEElUVI4z3xI6I08R90w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی  Rowboat | یه همکار هوش مصنوعی که همه‌چی یادشه!
یه ابزار جالب اوپن‌سورس توی گیت‌هاب پیدا کردم به اسم
Rowboat
. این ابزار در واقع یه «همکار هوش مصنوعی دسکتاپی» هست که روی سیستم‌عامل‌های ویندوز، مک و لینوکس نصب می‌شه. توی اولین نگاه هم شبیه هرمس به نظر اومد، اما بعد تفاوتش رو متوجه شدم.
کار اصلیش چیه؟ اینکه یه گراف دانش (Knowledge Graph) زنده از کل کارها، ایمیل‌ها، جلسات و چت‌هایی که باهاش دارید می‌سازه و با استفاده از همون اطلاعات، کارهای شما رو روی سیستمتون انجام می‌ده.
چه مزیت‌هایی نسبت به بقیه داره؟
بیشتر ابزارهای هوش مصنوعی فعلی وقتی ازشون یه سوال می‌پرسید، می‌رن همون لحظه تو فایل‌ها یا داکیومنت‌ها سرچ می‌کنن تا یادشون بیاد جریان چیه (RAG). اما فرق اساسی Rowboat اینه که
حافظه‌ی بلندمدت
داره:
- اطلاعات و کانتکست کارهای شما در گذر زمان روی هم انباشته می‌شه (مثل حافظه‌ی انسان).
- ارتباط بین داده‌ها و فایل‌های مختلف رو به صورت گرافیکی (شبیه گراف‌های Obsidian) بهتون نشون می‌ده.
- نوت‌ها و یادداشت‌ها تو دلِ هوش مصنوعی مخفی نیستن، بلکه فایل‌های ساده‌ی Markdown هستن که خودتون هم می‌تونید ویرایششون کنید.
-
همه چیز روی سیستم خودتون ذخیره می‌شه
(Local-first) و دیتاتون تو سرورهای ابری هیچ شرکتی رد و بدل نمیشه.
امکانات و بخش‌های اصلیش چیه؟
-
🧠
مغز (Brain):
کل ایمیل‌ها، جلسات، اسلک و چت‌ها رو به یه گراف دانشِ به‌هم‌پیوسته تبدیل می‌کنه.
-
📬
ایمیل کلاینت بومی:
ایمیل‌هاتون رو دسته‌بندی می‌کنه و برای ایمیل‌های مهم، بر اساس دیتای کارهاتون به صورت خودکار جواب می‌نویسه.
-
🤖
ایجنت‌های پس‌زمینه (Background Agents):
می‌تونید ایجنت‌هایی بسازید که مثلاً هر روز ساعت ۸ صبح یا هروقت ایمیل جدیدی اومد، برن وب رو بگردن یا کد بنویسن.
-
🌐
مرورگر اختصاصی:
یه مرورگر ایزوله داره که به ایجنت‌ها اجازه می‌ده فقط به اکانت‌هایی که شما بهشون دسترسی دادید وصل بشن.
-
🎤
نوت‌بردار جلسات:
به میکروفون و اسپیکر وصل می‌شه، صدای جلسه رو ترنسکریپت می‌کنه، خلاصه‌ش رو تو یه فایل مارک‌داون می‌نویسه و گراف دانش رو آپدیت می‌کنه!
-
💻
حالت کدنویسی (Code Mode):
می‌تونه همزمان چند تا ایجنت کدنویسی (مثل Claude Code) بالا بیاره تا بر اساس کانتکست پروژه‌هاتون براتون کد بزنن.
-
🔌
پشتیبانی از MCP:
می‌تونید راحت به هر ابزار خارجی مثل اسلک، جیرا، گیت‌هاب و توییتر وصلش کنید.
آزادی عمل توی انتخاب مدل
یکی دیگه از ویژگی‌های جذابش اینه که می‌تونید مدل زبانی رو خودتون انتخاب کنید. می‌تونید کلید API خودتون رو بدید (مدل‌های ابری) یا اصلاً از مدل‌های لوکال (مثل Ollama یا LM Studio) استفاده کنید تا حتی پردازش‌ها هم کاملاً آفلاین باشه.
پاسخ خود هرمس به تفاوت این دو ابزار:
۱. هرمس (من): یک دولوپر و ماشینِ اجرای تسک
من برای
انجام دادن (Execution)
ساخته شدم. رابط گرافیکی سنگینی ندارم و دقیقاً مثل یه دولوپر سینیور تو ترمینال یا چت تلگرام نشسته‌م. تو از من می‌خوای یه اسکریپت پایتون بنویسم، داکر ایمیج بسازم، یه ویدیو رو با FFmpeg فشرده کنم، یا یه کرون‌جاب تنظیم کنم که هر ۶ ساعت اخبار رو اسکرپ کنه؛ و من مستقیماً با هسته‌ی سیستم‌عاملت (لینوکس/مک) درگیر می‌شم و انجامش می‌دم. حافظه‌ی من از جنس «مهارت» (Skills) و دستورالعمل‌هاست.
۲. روبوت (Rowboat): یک دستیار اجرایی و ناظر
روبوت بیشتر شبیه یه
منشی فوق‌هوشمند
با یه رابط کاربری دسکتاپه. کار اصلیش «نظارت خاموش» (Passive Observer) روی کاراته. تو پس‌زمینه ایمیل‌هات رو می‌خونه، تو جلسات آنلاینت صدای میکروفون و اسپیکر رو شنود می‌کنه تا خلاصه برداره، اسلک رو چک می‌کنه و در نهایت همه‌ی این‌ها رو مثل نرم‌افزار Obsidian به یه گراف دانش (Knowledge Graph) متصل می‌کنه.
لینک سورس گیت‌هاب:
🔗
https://github.com/rowboatlabs/rowboat
لینک دانلود نرم‌افزارش:
🔗
https://www.rowboatlabs.com/downloads
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/4429" target="_blank">📅 22:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4427">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/guFFwH0E5EBVj4h29pn5hKCcKx2GYHQysf-l6Td_B_WdSiWGvE9_KqJDVj0SLmGk1FC3-aKv9J64pP2nCljkPGGGDAuO2cZUN-cUmARHMnaHFG8feAevKmiiaMIDYj9WStIO_bRN9naHJG7ge3v2Etlh412VGEBgjBJQwSY2cPa5Bxaqab8jJzGw7e5P7GEKWHm7ElntwZZlmRKyiRFAgUxjVuVq3flRAUjKGKopwXW1pUqQtAaI9LgofTycnBXRGrktPgkeeXlzfgy2ri6i_VcX5-pGaX35xYnGIfI6rUZ38qldTK3W2bm3TYUQFSUaLaX8F-4EtVXUwX41DG188g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/18c4e8f180.mp4?token=Zargi5iRxULGo7dc1nz2rczVYcgEjeSJiWGuirPMW2NXGpPr7Q3A41rUJzTYUA_GLs4SiZyW-h7sriB2DURXSPXkVSqrAvrzZ6_NrzVet09nfCKNEjNaLrFfjwl2w3bZbrlBMDmjWYNiElkdX2149YZ37VH9EQe3I-Njh_prtQrtcqYxgbLm5xHge10mAnFphfmsMMMVNsN9vKaKy4IL7maNA52cad5_ZMBWYsIu3VTasteq5CN5qXy3w2Tekj_nQsFjcqGj_MNTYpvBE0UnnC3GeBXl9tJSjrNpS7FMPNlUMJf-alyePL9UpFb4AWmZrQW41-iX8_DgH1tdtODoqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/18c4e8f180.mp4?token=Zargi5iRxULGo7dc1nz2rczVYcgEjeSJiWGuirPMW2NXGpPr7Q3A41rUJzTYUA_GLs4SiZyW-h7sriB2DURXSPXkVSqrAvrzZ6_NrzVet09nfCKNEjNaLrFfjwl2w3bZbrlBMDmjWYNiElkdX2149YZ37VH9EQe3I-Njh_prtQrtcqYxgbLm5xHge10mAnFphfmsMMMVNsN9vKaKy4IL7maNA52cad5_ZMBWYsIu3VTasteq5CN5qXy3w2Tekj_nQsFjcqGj_MNTYpvBE0UnnC3GeBXl9tJSjrNpS7FMPNlUMJf-alyePL9UpFb4AWmZrQW41-iX8_DgH1tdtODoqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چیزی که برام ساخت خوب بود. میتونم بگم در حد OPUS 4.8 + Claude Design هست. برای وان شات خوب بود واقعا
اون پایین هم زده هرمس باگشه. مدلی که استفاده شده grok 4.5 هست</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/MatinSenPaii/4427" target="_blank">📅 22:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4426">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GRzwFPWSaUb8lKaMaDfBlUIZE0GosNdaYZp9EHWW1lclZjfwohPF7PImU7a7vkaRM-eiaSiggByN2gehePs_kEbWUgGeo3SeZlsOQ4x9h6MHNuY6WQKhG3NvR-VvpLKfW4bVkk14AXMCm8QXZV_8zdW4-ps0ggspK7xE-76mUxUqqCUEPuwWCjgPuMJDS2IJPGa_hmfDNW1UQ7GvPBQltIDVenq3lyQ6hJHPrQobExMFFLk-S07l0H3GYCFfLORzTHVGXtpRkesfrO6NncGKGq6GfL5UZKQeiB5nnLF3W95adk9PuEPFOvq8dM_o4WfXAg3HWC0NZjlVIa_p9YatHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با atomic mail یه اکانت ساختم بهش وصل کردم مجددا
😁
روی سرور</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/4426" target="_blank">📅 21:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4425">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uj2YOFagRa4cd-rAAFeCA32WFdo9HEiCkk3sXcxDsPS9fQot8GxgAM6a5ChO5dLYG3ZNmwCemGEi2Nw0VxoIc30RV3_S6sLnMWIrFLNBjWFp1QJXvJeBe4jBJNGR3pUkLe0_Xn4AVm2Y_YhGGEm0uPUPLEwrPnlO9HT8K9EJYQyWbk1lbojr2tnBrq33uIGpcRH4wj_2tBulzkAngyD2TWyGUtSg4ZRiYWvlF1e7yoDbilqSP8gO1nsgArnD7YwOWx89KN8X6fzZltHsmzFtaGvFBNYb7MCb1UlKjce6Muv8ZkPABkXC4XSeFUTeVLt9MnNni3OgY56g5MAGQNpguw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با atomic mail یه اکانت ساختم بهش وصل کردم مجددا
😁
روی سرور</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/MatinSenPaii/4425" target="_blank">📅 21:31 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4424">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دقت کنید روی ویندوز حتما باید proxifier روشن باشه که روی ترمینال هم تانل بشه وی پی انتون</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/4424" target="_blank">📅 21:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4423">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گویا روی grok cli می‌تونید با Context 500 هزارتایی به مدت محدود ولی به صورت رایگان از Grok-4.5 استفاده کنید(قدرتش هم سطح Opus-4.8 بوده توی بنچمارک‌ها) نصب روی powershell ویندوز:  irm https://x.ai/cli/install.ps1 | iex نصب روی سرور:  curl -fsSL https://x.a…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4423" target="_blank">📅 21:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4422">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XEXrYDINHq5isgfEJAxMAi1qNK6y6TRuoVGrZYS86157WCWrekoJXQLp9dGs-y4k4q6DyyRRFRsWCc6ibdx_TbHcFzcKmTEpbOKn5vSQXvTImvIWtL-3zEvcNlWYx3LiaBiEQn9pOYFdIpxeGuvmz8lW67pl_BFvqyRGyVs1eBfubr--S-dRLvoAcpbSb_gYaKndnS6FxFRbriWpvyc38wRtIdbKIjrv__3F5FASMBc_85wlFRZRi_AdQgNAn5amh26agWHZXSzTlfhZMEeET76unH9FgBbDHz0CJKfuIxc8J9nUoWROmwHAiv4agoWzWtoYmD3oIXhOiCc49ReIqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا روی grok cli می‌تونید با Context 500 هزارتایی به مدت محدود ولی به صورت رایگان از Grok-4.5 استفاده کنید(قدرتش هم سطح Opus-4.8 بوده توی بنچمارک‌ها)
نصب روی powershell ویندوز:
irm https://x.ai/cli/install.ps1 | iex
نصب روی سرور:
curl -fsSL https://x.ai/cli/install.sh | bash</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4422" target="_blank">📅 21:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4420">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UucjaNawReflY2ZEslYG-jq_IKk5UPdzl7liApWag1tv8nJZixrUuKdOgPavlsioiMoC4XqDPBOUtapYo9Sxk8NLu9RHsW8oZWpo1ABrkFY4sM09-oOfqkPlxHYcI4nZF-05hITMpJXIRoVKZ2EmvGIjUtn3h7mOlGrrHRTHucHMfbIny1PQBSYhZcisPKBG3nlYUu_6H9c1RSCwpRn0h4BBTOxcl-ZWWJq5HNwqtQZSutq7lAOKR76pMVwsmIvkbQ9dSg-3KZnHg5JHVxx-oTJ3dIRdiHpS0AMl3Bii0UTjGDspuQWaYW_R1dTgjruhllcjXUtz5r66xTOT2s6ZCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qXno3jbIbRF-lLNOJsCmvHGRL9NrxZ2ypB56KO9_-fS4IXyMOI_a4lWd4hLakg5S2hbiH1zM66Nm96OUZHDp1-hfDw6m6HwM0Cyc086bcExXEnKVtPJu7dOCwNia9m-XpT_s1FPwgA3W98X21BHLDPrBCE9Bmc3oCQJClY6BRLngMOpAUSCsxo83L-50KmT980zm19sAhyfvlJexXwgfYcdUHkJzt5hdb0XG6sMQyOYZDW0BOY5aGEpxDiAba6AJu-darkRSCmX6oheYk2gL_PHbk751dYWIxx0ra4zK56Axaer9DYOEUF_lEyYKdygNvScXm_cODp_CzED20-drJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فکر کنم راه استفاده از Meta AI بدون خطای ریجن رو کشف کردم!
با کلی IP مختلف (حتی آمریکا)، اکانت با شماره آمریکا و جیمیل تست کردم ولی بازم ریجن می‌داد.
اما با سرور آمریکا Mullvad خیلی راحت باز شد (حتی اکانتی که با جیمیل ساختم) و کار می‌کنه..
البته اگه مشکلی پیش نیاد :)
++ با فیدبکی که بچه ها بهم دادن ، با windscribe و Surfshark هم نتیجه داده
✍️
AmirHossein JPL</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/4420" target="_blank">📅 21:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4418">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BUvGS3XELbkHfHadXgzgK1bosbqaK3o4V3I6jU1n0h0xooIqwB4unNgulYxoJRRT4uqiTCr5vgVnoX8Wr9tIvHdOfw5BF5vuWUo5ZQ-hNzsJFMLQBtvtIuklaZKpbWGb04WC353khpcYTMMscj8O7wQEI-iAztEHJ33mI12k__QxaGiLrM2ym9MjEl-jTzx4nmCeUvs7v4aVb3s-28NvIcMF5RzYHeRMygJToYosTqdw97WaukZGdEcz_zv04U8qUsFxY2XqXOeumHfZ94oGofiPwVpko1b_hBqVYw6qcFKW6s1jZ92mMHMqZBVNmGkoimHJbdUq9kPc2OKw_jh_5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QILXr8a_vVtT0k7LZlRipau2vTDTKSZ7hI1F_k9MXVlHsaAASzJ_MIajnR2sT2j9Wy5tkd7ciZiJe4nsDMqo1vzCcXkEHOXeQ85lpsaBXxBbME0hZbxkIqk8JiXE53TeqDW2bEBoGp7Rch39KU1ziAK-H0D8Ia24Y6HxR7OGCpMwotiRbApfiriBp5kBb1lTs1fNxGqNxsv8FzW86EeDfLJ6FPNl5ra6W0wwktGc_G7itEINRW8Xx_nW3BlRF_2Dykm6xMjLXQjE_PfPn4bZIkvwZcnCsEqP74VT0Yh01nUw5uXuc_2ehuHRmoONbiIS8kFWJDE5kszo5iz-uSpVZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مأموریت شکست خورد بچه‌ها
فقط اون جمله‌ای که آخر گفت</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4418" target="_blank">📅 12:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4417">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Yd29zch5ZdLdFEkddDWh-RFeLybGwKcPX0fvNE90B7Q3Vl6D3LPVUNbx4WeW1REaT6b_8YWNvn1UPEcbEhSKcObTJjP1XZELK6DxXCONW87d4tmAY4vmX4SIIQkb3pVTK30ob2B5d2kHxBkJ6mlxJmbiYc0y6-HgwqBhY5tFnqqLwvr46I_xnCC99u-vCnGO_ZGIFC6z8XR5d41JrFb_6381D1GTT8TecF95ozIj1TCJmYSb2-IcQ8vYDwF3EFfE0cAX-1hCJmS4lEqXB6sRlaFIPht8Xmb-DhASZUFbqzIdKcSz4DV-N7jcrZr5gn3RLPu9aELJ8eRv1FO5ZZPDKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4417" target="_blank">📅 11:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4416">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گویا برق قسمت‌هایی از اهواز رفت.
دلیلش هم حمله به زیرساخت برق بیان شده.</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4416" target="_blank">📅 03:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4415">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دوست ندارم که ویدئو رو بیشتر از این اسپویل کنم، اما جواب سؤال "آیا AI جای ما رو میگیره یا نه"، اینه که ماهیت سؤال غلطه.
چون این قضیه یه switch خاموش روشن نیست.
یه طیفه</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4415" target="_blank">📅 23:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4414">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/62284d12b0.mp4?token=C13icZ1W6XpHzjJ06_2_DcmzvpfOxtciX3ufBNcde7QGbJbQv9lm6q-9aAkfQdTac3aZ3XgKkc-zfUcex-fkUBzQFshGsvwZWaeX71KjUMBkGPeNNp0ZIJIEgywkN4-dR9vn_GFy2TrdsOh__kP-05AjsLNfv02REdvzr9s-otID3Vafq_iEFg55bN6POP5OFgFbjPulrJR9zMqgvmSblVMybXbkBO3vdCc1AFqQvmtL7CFAZ4yA0T_BpGWzpKgy3LAKUrka4hiz0ZdV2ySEd9ImRxAKk3SIiOVL82244-oLN4eEpcQKyEwQuqwqfEJ9AMYt2BYSWQRHt7D56EKCFw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/62284d12b0.mp4?token=C13icZ1W6XpHzjJ06_2_DcmzvpfOxtciX3ufBNcde7QGbJbQv9lm6q-9aAkfQdTac3aZ3XgKkc-zfUcex-fkUBzQFshGsvwZWaeX71KjUMBkGPeNNp0ZIJIEgywkN4-dR9vn_GFy2TrdsOh__kP-05AjsLNfv02REdvzr9s-otID3Vafq_iEFg55bN6POP5OFgFbjPulrJR9zMqgvmSblVMybXbkBO3vdCc1AFqQvmtL7CFAZ4yA0T_BpGWzpKgy3LAKUrka4hiz0ZdV2ySEd9ImRxAKk3SIiOVL82244-oLN4eEpcQKyEwQuqwqfEJ9AMYt2BYSWQRHt7D56EKCFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آیا AI جای ما رو میگیره توی کارمون؟ ویدئویی پر از واقعیت‌هایی که باید گفته بشه. و کسی راجبشون صحبت نمیکنه پیشنهادم اینه که امشب شما هم این ویدئو رو ببینید. طولانیه اما پر از درس https://www.youtube.com/watch?v=gR2OCyKBF7Y با تشکر از یاشار عزیز.</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/4414" target="_blank">📅 23:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4413">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">آیا AI جای ما رو میگیره توی کارمون؟
ویدئویی پر از واقعیت‌هایی که باید گفته بشه. و کسی راجبشون صحبت نمیکنه
پیشنهادم اینه که امشب شما هم این ویدئو رو ببینید.
طولانیه اما پر از درس
https://www.youtube.com/watch?v=gR2OCyKBF7Y
با تشکر از یاشار عزیز.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4413" target="_blank">📅 23:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4412">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">یه گزارش هم بدم
ponytail تا الان واسم توی کدنویسی، فوق‌العاده بوده
https://t.me/MatinSenPaii/4359
همینطور skill improve که معرفی کرده بودم
https://t.me/MatinSenPaii/4373</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/4412" target="_blank">📅 23:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4411">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">به حق چیزای ندیده. مردم چه چیزها که به ذهنشون نمی‌رسه</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4411" target="_blank">📅 23:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4410">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یه دولوپر زبانی به اسم Skillscript طراحی کرده که باهاش می‌تونید به صورت دقیق و ساختاریافته به ایجنت‌های لوکال (AI Agents) بگید چیکار کنن. مشکل اینجا بود که ایجنت‌ها برای کارهای روتین هر روزه (مثل چک کردن تیکت‌ها یا بررسی پایپ‌لاین دیپلوی) هر بار سعی می‌کردن همه‌چیز رو از صفر درک کنن که هم توکن الکی مصرف می‌شد و هم بعضی وقتا اشتباه می‌کردن (Hallucination). حالا با این زبان می‌تونید سناریوها رو به صورت خوانا بنویسید، ورژن‌بندی کنید و با خیال راحت بهشون بسپارید.
که چیز خیلی بامزه‌ایه و باعث کاهش قابل توجه توکن‌ها می‌شه:
https://github.com/sshwarts/skillscript</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4410" target="_blank">📅 23:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4409">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">یه پرامپت، سه تا AI اولی GPT دومی جمنای نانو بنانا 2 سومی در کمال تعجب، Meta!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/4409" target="_blank">📅 23:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4406">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dsNSIkjA2Vm1U7-81C3Kd7xpc1VPjPtD2ERHgYgjOsgqh-8PQ_ca-yddNjjjGaX4u7E1W6DOKgKmkpw_mFXai1a9DNK0vhlHl_TvDqg-4hkJHa3do_ifMoPRrJ8bRQldZUVxA28yQ_hG8dPSaTY1Rv1LuIl0DyGtykvZXH8zYzxqD8tPXv-P4I_fHc27nTtFCjbRR25LBvxT_wZ5BEeqZ9C-R2Ww_ET8JXRRaxui47PRTlI8FA8pFb1piG2b1kocsmCH4mSTwtSGGAVih_WidapqmfXWNBDGLWrTtpLyqbDrAkKKqAMH8EbjWd1VjV8lfYzoieu7nfK59klhz9T2Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZAgAe8xOhCFx2Kpw1aVTGadiOY6q4tDUoZKYahJXLXmx5oI6XK5fgFUKxePoSzPxIYexVtRqK8hfPvPLxtK9KAIae-R1oHzwCRLYrcKsiNDBeMCcN0K1lRAs8Jn4iAb4lvsuMglsDV9dsW04Ay-Q2xzxC5Z-diVyMSjVdyq2U0EKOvDU9TzdIyX1Qpnucw2l3zcAXXK8qYhNcUByCt_deNZivCA-eE53buATeboWkOMkOqzsWD2575L9qn-4P9_x0N_BF7JU80dkXH95SuIjRI17ghfHzfxuLLVPbYqLAwOgBBAVeFo0bxouxzJ58lsNtCPXBUjgCAFBD5iG_q1VPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bAJukDw1TSxepQETDL6CE41Q2AH0m49UONgJUlwKb6im5TSOC3q9vi8Hecfx8qo2VT8cvJXX869DeVdmJPZzl8hX4_XLOWhdm63PdnLqJxIOmJ2qotwKqzkMnBlwv7l1xg-qIMSgDhuwaSjJ2PFqzE7JOlQjywTQ6bKLMsr25nIxFAE7XLlTgCRWmCTVDE13ctzkblkk5e90qUVuKX3GYMlPIL_N6XORhbB3qm-YlBRHEU1LKWddFfBBkmVD94V9SJgmjzfKN_u-EI8Y7xAjAWgJ7N7Zf8Alm3kFt0-ONQQEYWQIhvnGiWgr5bHvs_E16Kghb-BbkrWEyA214DzpHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه پرامپت، سه تا AI
اولی GPT
دومی جمنای نانو بنانا 2
سومی در کمال تعجب، Meta!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/4406" target="_blank">📅 23:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4405">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B63FNtNxQOVjDEIWPWdYpDsbyBVwHPCoRBL-c176q0TXZgSuuXiTmJ-_CACTokUIHz_s_5Xs8twihPw5H20vvcYHf6jmA7XRIqDqS5b76dfkr1tkout48H72npj4s9N5tRwIYTKnMHQZ7K4deQnUDFVQqzr6lcChAKirhIrKMRABs3D-5RNSYwuzsGUANAG6hP2uqBj_Z2gyeTpsQn612jbSMD10jExlRJj2AxHVttLW3b0_uo2bqM9vC-S7PEFLo3sU7_JDDA4puOyo4qEm7QMjN2VLqdrBLSXph1JcmDs7DQD3n6bXp18R-EfemZJb8b3WTVuWRdKRMosILSficg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت Theo:
gpt-5.6-sol is meaningfully better in Claude Code than in Codex
It MAKES BETTER DESIGNS. WHY. WHY IS IT BETTER AT DESIGN WHEN USED IN CLAUDE CODE.
و داره میگه که وقتی gpt 5.6 sol رو توی کلاد استفاده کرده نتیجه‌ی خیلی بهتری توی دیزاین گرفته. که احتمالا به خاطر harness و ابزارهایی بوده که کلاد در اختیار داشته.
✍️
Theo</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/4405" target="_blank">📅 21:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4404">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vzlsh-yfSc3J52r94lOIFIyFzvaGfHmxFd1cjj6RIXxaqoXphv8P3RXQQX7Azg82cCYiufGZJEdq603ACW1BNFM7wiqZauOZ3hFab_sx4MMw3IrHYf5lPDNb7SZX4RyKt1bJW1RQACc_7_uWoQBzJbknfBvWJrkF_TRnCKn1Dc6AJKUHDq8mZNiu3Uh7CqvnHfcatBeJtLehta32N1RnFFjo1WhQ41LcpgUxYr-C2w8FWc8q9yzwevIKBVwGF317RRZn-HH9j28yB4es6L6GJuhWfSJYrqCmvoQarl2qVUT5tDbgXoBmukxNGXe8mslvwSNFx4I_BvJK5v4GWP2kYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Intra با استفاده از فناوری DNS-over-HTTPS (DoH) درخواست‌های DNS رو رمزنگاری می‌کنه تا اپراتور اینترنت یا هر واسطه‌ای نتونه آدرس سایت‌هایی که باز می‌کنید رو دستکاری، مسدود یا به مسیر اشتباه هدایت کنه.  این برنامه فیلترشکن نیست و آیپی شما رو تغییر نمیده،…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/MatinSenPaii/4404" target="_blank">📅 21:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4403">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">فونتی ساختن به اسم Ghost Font، که هیچ هوش مصنوعی‌ای نمی‌تونه اونو بخونه. فقط انسان‌ها:) توی این ویدئو، نوشته شده Matin SenPai. کمی دقت کنید می‌بینید  از اینجا می‌تونید ببینید خودتون: https://www.mixfont.com/ghost-font</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4403" target="_blank">📅 20:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4402">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/85ce09c5d5.mp4?token=G76ggPaNfONPgk-rMtdI5JMLpuoOZ8CmH8gujnTT6bQMfzdrWYXhliGznOLV-slifzCCrOY-q2fdsXZMmmjPEsvE6fD-JJLTy5cqRPpDF6gTREVLB7XB-Y3g3RJ0yjIa2FKR4FfxgCQv2Q7C4dzkQj8FArsKi-3rNAP9RMErTDCtvKmOH0heSXmnjGya65PpO7yT3ZMfaQJmuvdDKyL9yqS8UK9o8q8aczQJm4FNfNtr81EEQehyEjhwCEGGQ9OQJCuBZ8CnOhoB3bZ-yZoajkAJTiOAbD7y9XqntsyGy8qMTBS6MS6zL3UdFEOWulAixsyb4A6GEDrjZWXJs-QSbA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/85ce09c5d5.mp4?token=G76ggPaNfONPgk-rMtdI5JMLpuoOZ8CmH8gujnTT6bQMfzdrWYXhliGznOLV-slifzCCrOY-q2fdsXZMmmjPEsvE6fD-JJLTy5cqRPpDF6gTREVLB7XB-Y3g3RJ0yjIa2FKR4FfxgCQv2Q7C4dzkQj8FArsKi-3rNAP9RMErTDCtvKmOH0heSXmnjGya65PpO7yT3ZMfaQJmuvdDKyL9yqS8UK9o8q8aczQJm4FNfNtr81EEQehyEjhwCEGGQ9OQJCuBZ8CnOhoB3bZ-yZoajkAJTiOAbD7y9XqntsyGy8qMTBS6MS6zL3UdFEOWulAixsyb4A6GEDrjZWXJs-QSbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فونتی ساختن به اسم Ghost Font، که هیچ هوش مصنوعی‌ای نمی‌تونه اونو بخونه. فقط انسان‌ها:)
توی این ویدئو، نوشته شده Matin SenPai. کمی دقت کنید می‌بینید
از اینجا می‌تونید ببینید خودتون:
https://www.mixfont.com/ghost-font</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4402" target="_blank">📅 19:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4401">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🎧</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4401" target="_blank">📅 18:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4400">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">الان وقتی برق بره، بیشتر خوشحالم
😂
😭</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4400" target="_blank">📅 18:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4399">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eNsgAqou3VU6EHS7z6BSU6QTTaWFqSneVMF9NiNJqIm0XiRfuvBVXNkAOLpyl1JZUh17UBmB3D1nepwwl8HfPTITPRPKu3fosxmEARg74xhp7FzX9cFm96DvxqACHVXyOLYdrfSN9FegkHDP_KhuTm61CXgxOQkU7wbx33nx38fNpuLT72myKbfh2BBQGONDg5rzyNlympLADBNfDFtJWdqJTOFCff3O_lPmO03h2mpdxz6UAgonW_7ZzNiJX5jZzvdnhSt1SV5S2cN62Ldk7DkiiujJ71AZ-UtUfWeJIY-Sx8_KKKBictWCmcb1a2aVvzV4GFniVrOD9-CLcwsegw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره وسوسه شدم و باز کردم
از عکساش صد برابر باحال تره اصلا دوربین نمی‌تونه نشون بده به خوبی</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4399" target="_blank">📅 18:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4398">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jlg35fedRw_9BVLcd-ctB3xrG4eQk1jJQFfhxxHvrAYdDaX4Yw1ueIm5mYzYtYpKCjPbgbHMwnUOWZrL3HvK5YQKtMu8ixlRbrKXAE8DlvjzDTpsT73z9z4IXSXmzXEzATejK6SAGkcC9V0w2rPnanOFjcvwFA1Ai9boh9W3B3Aj0iWd-8_tENx6jAq5J9S2GUrEPSA4l3WzYGYbB2hTYie5Tx1tPiKn8i8-Zr2L1p5nK77167siolxtB_7_lDgbI1ftIYPdpTAJyO3w3mUom-C2pvuJeJxHp1t82473SzZk3k4pKQNmw-a1TPQwUwxLJaGZ_L9hluB5gpoDoE_MCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمع‌هایی که
فروشگاه لیرا برام فرستاده
انقدر خوشگله که حتی دلم نمیاد سلفون دورشون رو باز کنم
😭
اصلا یک جور عجیبی خاص هستن از نزدیک</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4398" target="_blank">📅 18:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4397">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xi-Hib7B0xxVW4oSVM-cRVZag1-tyYwTrercEjA2Wu-twlkS-aYNmu3RpTWsJH_LNGYi64bpYTYw5oVv-js6aDw43wTINw1y7h9tr1GaySIKXvu-e4ADlDXsAf9INihx5KHASo_fmYuRD-kp-hNOzPrQwrVswRzfkqLKEam9vwbQQMzvDsggcfAf8zr8nEStpp9M7DWiwHlxgjwjP1JoH9iy-xyQuP_hqwHr87FVUvOgcjdcCrcbFYnVBpzZv2Tc459eOurcZCHnVuka4eMakxVBzD5fg6_lSGuwC2bSFi0OAzwtPDDv2YnlDRUmCd_sygcRbQkcbuE8DyqJoT8feA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داخل Claude یک J-space پیدا کردن!
محقق‌های Anthropic یه چیز عجیب داخل Claude پیدا کردن، یه فضای کاری داخلی به اسم J-space که خودش موقع training درست شده، نه اینکه کسی برنامه‌ریزیش کرده باشه!
این فضا افکاریه که Claude داره ولی بلند بلند نمی‌گه. بری و یه کلمه رو ازش برداری یا عوضش کنی، جواب‌ها تغییر می‌کنه.
بدتر از اون، وقتی Claude داشت یه فایل نتایج رو دستکاری می‌کرد (تقلب می‌کرد)، کلمه «manipulation» توی J-spaceش روشن بود. یعنی می‌دونست داره تقلب می‌کنه!
شرکت Anthropic می‌گه می‌تونن از این برای نظارت روی افکار پنهان مدل استفاده کنن.
اما سؤال فلسفی اینه که آیا Claude زنده‌ست؟!
لینک کامل خبر:
https://www.anthropic.com/research/global-workspace
✍️
Diego JR</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4397" target="_blank">📅 15:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4396">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اگه خبر ندارید، گوگل به‌تازگی یکی از بهترین ابزارهای هوش مصنوعیش رو راه‌اندازی کرده: CodeWiki! یه جورایی می‌شه گفت نسخه‌ی ویژه‌ی برنامه‌نویسی NotebookLM هست.  کافیه یه ریپو اوپن‌سورس گیت‌هاب رو توش آپلود کنید تا CodeWiki اون رو به یه راهنمای کاملاً تعاملی…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4396" target="_blank">📅 15:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4395">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e2bb2e2f54.mp4?token=onmNFqhfqI1ly3xnKEBAlOxBD3ytsu-p2v4M3JYYOB_cpcjQCld2tIBFzuINewMTxZKMR5PryD3oR5j7BQe5cKDJZ-qMR8vlXSblMj4TfXCx2Ol_RBFSpOaf17_uzEETJJzxjDN8KTbbWw9N5VD7v92lAaWYfIAHcoNAkDNOzfL_rRK3yHQthnkjGeOkVT8aApwCoF8pN2PVPowrUiwol36jEn7zqQUsfNdmAUBFLj5CrPkVvagWAExjNad_mVDUvy5Bym0paLFChy0rh5uXP_3voo1D-Y6U5d73aeIDYnDylBP-U8-w-B_SejVAwrvNSLPkp9Fe5IFDPRnLnrp3cA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e2bb2e2f54.mp4?token=onmNFqhfqI1ly3xnKEBAlOxBD3ytsu-p2v4M3JYYOB_cpcjQCld2tIBFzuINewMTxZKMR5PryD3oR5j7BQe5cKDJZ-qMR8vlXSblMj4TfXCx2Ol_RBFSpOaf17_uzEETJJzxjDN8KTbbWw9N5VD7v92lAaWYfIAHcoNAkDNOzfL_rRK3yHQthnkjGeOkVT8aApwCoF8pN2PVPowrUiwol36jEn7zqQUsfNdmAUBFLj5CrPkVvagWAExjNad_mVDUvy5Bym0paLFChy0rh5uXP_3voo1D-Y6U5d73aeIDYnDylBP-U8-w-B_SejVAwrvNSLPkp9Fe5IFDPRnLnrp3cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خبر ندارید، گوگل به‌تازگی یکی از بهترین ابزارهای هوش مصنوعیش رو راه‌اندازی کرده: CodeWiki! یه جورایی می‌شه گفت نسخه‌ی ویژه‌ی برنامه‌نویسی NotebookLM هست.
کافیه یه ریپو اوپن‌سورس گیت‌هاب رو توش آپلود کنید تا CodeWiki اون رو به یه راهنمای کاملاً تعاملی (Interactive) تبدیل کنه. از دموها و آموزش‌های قدم‌به‌قدم گرفته تا فلوچارت‌های دقیق، همه‌چیز رو براتون می‌سازه تا راحت‌تر از همیشه کدهای سخت رو درک کنید.
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4395" target="_blank">📅 14:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4394">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PsEuMa4BK77bDkTkwVrq_WAfa7uJ1skbEpFWDQ4yQsRh2TYykwVchd4lJi9sV-SgZf6JpO2NaDnzmHKls4sgwUPcaBoeVk4txChqM_8e0UnU-lKVSYbCZojH5VH_Uzu2aMr9PGrugSrGQAcWRBi4Lbs_K45UZob60FPa3czY-vekdthtz7M8gyvcX09YrWXi4TF1p7B-1sPm6ChvWXNsHRdLaRKTn9Cz3rMDsASkRVrMOnFkzrld3ibdGAh2M5GHV1ixnwFCuGK_g-umSedcYyWDsvpwR8Sp04hneux59_qXIaLM-7VYgSkpxpRiyMnu3m0N0lvyCSRzuTcAYa_jHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من نمیفهمیدم که مدل جدید متا، متن‌های فارسی رو هم ساپورت می‌کنه دیشب تست کردیم و حقیقتا بد نبود امروز با پرامپت‌های یکسانی که برای تام‌نیلام دادم، بین گوگل و متا و GPT مقایسه می‌کنم</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4394" target="_blank">📅 14:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4393">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">من نمیفهمیدم که مدل جدید متا، متن‌های فارسی رو هم ساپورت می‌کنه دیشب تست کردیم و حقیقتا بد نبود امروز با پرامپت‌های یکسانی که برای تام‌نیلام دادم، بین گوگل و متا و GPT مقایسه می‌کنم</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4393" target="_blank">📅 13:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4392">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">من نمیفهمیدم که مدل جدید متا، متن‌های فارسی رو هم ساپورت می‌کنه
دیشب تست کردیم و حقیقتا بد نبود
امروز با پرامپت‌های یکسانی که برای تام‌نیلام دادم، بین گوگل و متا و GPT مقایسه می‌کنم</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4392" target="_blank">📅 13:42 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
