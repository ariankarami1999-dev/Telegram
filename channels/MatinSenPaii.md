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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 21:13:29</div>
<hr>

<div class="tg-post" id="msg-4503">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBloom.(Tin.)</strong></div>
<div class="tg-text">این‌روزا تماما بغضم. از دیدن این وضع زندگی و اینهمه فشاری که به مردمم میاد
از اینکه حتی نمیتونن یه زندگی معمولی داشته باشن
از اینکه نه نونی هست برای خوردن، نه آینده ای برای امیدوار بودن..
هر روز میبینم که قطعی برق چه ضرر‌هایی داره به مردم جنوب میزنه..یکی رو خودش بنزین خالی میکنه، یکی از شدت فشار جلوی دوربین گریه میکنه..یکی گوسفند مرده رو میذاره رو کولش که ببره برای زن و بچه‌ای که دوساله گوشت نخوردن..
چی میتونم بگم، فقط اینکه پا به پاشون من هم غمگینم..</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/MatinSenPaii/4503" target="_blank">📅 21:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4502">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">همراه اول Masque + Balanced ترکیب خیلی خوبیه</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/MatinSenPaii/4502" target="_blank">📅 19:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4501">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">☠️
اتصال رایگان و پرسرعت با پروژه Aether + پروتکل ویژه گیم Wireguard
⚡️
لینک پروژه‌ی اصلی: https://github.com/CluvexStudio/Aether لینک پروژه GUI من: https://github.com/MatinSenPai/Aether-GUI دستور نصب از ترموکس:  curl -fsSL https://raw.githubusercontent.co…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/MatinSenPaii/4501" target="_blank">📅 18:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4500">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">خیلیا سر ویدئوها از من می‌پرسید که کدوم روش برای نت ملی جوابه؟ و آیا «اینم زمان نت ملی قطع میشه»؟
جوابش اینجاست که کامل توضیح دادم:
https://t.me/MatinSenPaii/3680
اما خلاصه بخوام بهتون بگم نه این متد ویدئوی آخری نه پنل‌های کلودفلر هیچکدوم وصل نمی‌مونن طبیعتا. اگه اینا وصل می‌موند که دنیا گلستان می‌شد. قطعی اینترنت معنایی نداشت دیگه.
با بسته شدن
cloudflare.com
و آیپی‌هاش، اکثرا از کار میفتن(sni کمی سختتر)</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/MatinSenPaii/4500" target="_blank">📅 18:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4499">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مشکل گیر کردن روی answering setup prompts رو هم برق برگشت سعی می‌کنم برطرف کنم
🎨</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/MatinSenPaii/4499" target="_blank">📅 11:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4498">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">و رفقا در مورد ویدئوی قبل و اسکنر، من مشغول کار کردن روش هستم که اسکنر رو خیلی خیلی قوی‌تر و پایدار تر بکنم روی اینترنت‌های محدودتر مخصوصا نت همراه، و به زودی ورژن جدید SenPai Scanner همراه با نسخه‌ی اندرویدش قرار داده میشه روی گیتهاب
تا اون موقع با تعداد ورکر پایین(50 یا زیر 50) و با کانفیگ‌های BPB یا Edge یا پنل Nahan تست بگیرید. با خود Cfnew تست نگیرید</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/MatinSenPaii/4498" target="_blank">📅 11:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4497">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تمام تلاشم این بود تا قبل از ساعت 12 که برق بره ویدئو رو بذارم
🦆</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/MatinSenPaii/4497" target="_blank">📅 11:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4496">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4496" target="_blank">📅 11:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4495">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نفر اول:
دوست ممد
🥳</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/MatinSenPaii/4495" target="_blank">📅 10:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4494">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">آموزش رو ضبط کردم. قرار میدم واستون کمی دیگه</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/MatinSenPaii/4494" target="_blank">📅 10:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4493">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">متشکرم از همه‌ی دوستان بابت فیدبک
روی ایرانسل و مبین نت اختلال بیشتره، مخابرات و آسیاتک و همراه اول جواب بهتری گرفته بودن همه
برای گیم هم Wireguard بزنید. نه warp on warp</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/4493" target="_blank">📅 08:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4492">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4492" target="_blank">📅 08:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4491">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اگر سؤالی دارید، توی کانال سازنده‌ی اصلی هسته‌ی پروژه بپرسید:
https://t.me/CluvexStudio</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/MatinSenPaii/4491" target="_blank">📅 08:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4490">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CzuNTN4U2AqDOL4STq14Kh-Q679C3-86y955PoejeId4yN_22NTnMUzIjlk4yyeSfYOnT5Y-DTyRfBHVu2HfDMdGif0SJ7xTdDCfc-Q2XPdof5CxR-ENLBoKvoCUj8d-VQEEu9rDqztRDsyGHRwLBef6Iq2AUv4ie1-M7msmxnLzPTlLdL4GRnZOis96-ALyW3do7y8JwptI4Gl67iNX3UtWfNJqRzZXUXL2L21Y7CgmCmQ477Oufe66oKJpFg-WB8uIjw73GeulcvJou5-IiTi1GJNlB5_YwdudVY9O5TC6TqhqP-3getbldi08ZGVaP_UFrGY_R2eEsXN82woarA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقت کنید که Wireguard آیپی ایران نشون میده(نه آیپی خودتونو)  ولی Warp on Warp آلمانه اصولا بعد از کانکت شدن هم خیلی راحت روی V2rayN بزنید و وصل بشید: socks://Og@127.0.0.1:1819#Aether-GUI</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/MatinSenPaii/4490" target="_blank">📅 08:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4489">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">هنوز کسی سر گیم فیدبک نداده
👀</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/MatinSenPaii/4489" target="_blank">📅 08:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4488">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sknl_i6LaVivZoYigq5mEYY_R1Ghf_ihGKbdVLSDnE7KH61zIEgXshgInV1eYp2rSlxMbHNZSaEZrCQBkas18PZXyq5AEjEdx4TEcurZX-AaVWlqV5mrYGrdnr990GTup-4K0-T-BRuZDyyP4vKxxu4-vmuivw3I1Fc6Y7j6TxZtbz99KDFBX2Rldqnt1QnWNQc_ko0O7fm3XXPNT5X-kKNzc6dBFrzDQfao4FmV6VhIlMzm7AUQ8dYJ-y5v3AhG-6IJZ_0hxkKC6UIe1hZ9gDxzmWx_wgl2dLSY6CPmRbOI4gREdLqfz941hyQR1TdT5LQd9YqbxHpkFeterOz3wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر این ارور رو مثل دوستمون می‌گیرید، پروتکل‌های wireguard و warp on warp رو امتحان کنید و همچنین scan mode رو هرچی از چپ به راست ببرید، سختگیرانه‌تر جستجو می‌کنه</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/MatinSenPaii/4488" target="_blank">📅 08:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4487">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">موقتا نیاز دارم بچه‌های گیمر سر این متد Aether بهم فیدبک بدن، ببینم تا چه حد پاسخگو بوده براشون هر پروتکل(یا اصلا نبوده)
https://t.me/MatinSenPaii?direct</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/MatinSenPaii/4487" target="_blank">📅 08:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4486">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4486" target="_blank">📅 08:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4485">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">به همین راحتی</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/MatinSenPaii/4485" target="_blank">📅 08:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4484">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خوبیش نسبت به Worker کلودفلر اینه که محدودیتی در کار نیست و همچنین دردسر اضافی هم نداره.
سازنده هم لطف کرد اسکریپت راحتتر واسه ترموکس نوشت:
https://t.me/CluvexStudio/254</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/MatinSenPaii/4484" target="_blank">📅 07:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4483">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">بفرمایید دانلود کنید. قبلش با سازنده‌ی پروژه مشورت کوتاهی داشتم و اجازه گرفتم که روی یه پروژه‌ی مجزا GUI رو بنویسم دنبال راهی هستم که همچنان اتصال راحتتر بشه. فایل Setup رو دانلود و نصب کنید https://github.com/MatinSenPai/Aether-GUI</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/MatinSenPaii/4483" target="_blank">📅 07:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4482">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یه ‌GUI راحتتر واسش نوشتم روی ویندوز</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/MatinSenPaii/4482" target="_blank">📅 07:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4481">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">روی گوشی درست نمایش داده نمیشه</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/MatinSenPaii/4481" target="_blank">📅 07:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4480">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">خیلی خلاصه بگم:
فیلترینگ به‌طور معمول دو راه داره برای شناسایی:
(الف) دیدن امضای مشخص پروتکل در هندشیک،
(ب) بلاک‌کردن آدرس‌های شناخته‌شده یا کل ترافیک UDP.
حالا  Aether راه (الف) رو با تقلید از HTTPS معمولی + نویز خنثی می‌کنه، و راه (ب) رو با اسکن دائمی آدرس‌ها + قابلیت سوییچ به TCP (h2) دور می‌زنه.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/4480" target="_blank">📅 23:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4479">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eV9gzNDiR8Cx2GfAu4RTE4WDZhVO15jBebD7GmrSSatj6ahSnIWL97EBYnBf9rtiQu8385-42HqsuYVFc-bYrp8Ta4EG_wcVpzldUqK2pJQpHU2mOpmHc3kgA7yVl4gkAUlDRXO4xCHnxYcjOssL5l2yHYjI2NyFirW8tbIsdgmaKGuRryBTqea9BQrIewGjhr2qxvRXi4FlxP0qAf7OdEuHGHudTAqUZNT-2OD8AFVWEhT5wjYZYVeephLcDmbpUF15-ZZ852JeZ0W3F-ISXrv-RWpvJueaAqj1U4tw57xkE14zCPvNGbrNvuewGVvjRSMq_CGoTjlTIzgXJILXtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/4479" target="_blank">📅 23:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4478">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/4478" target="_blank">📅 23:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4477">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">به زودی آموزشش رو می‌ذارم. هم دسکتاپ هم اندروید</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/MatinSenPaii/4477" target="_blank">📅 23:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4476">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/MatinSenPaii/4476" target="_blank">📅 23:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4475">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Yr1dq79UsoM39HREJbioIgO6Su9Isu-GlIzWNpo4Xb3b00VBGoZa_Go5J6h_OH-GWbU0qwvJNtfXoybAIYlqlPmJrRLRLBnyXgIzLrElogf2vu8XmiwiZWrXGKSUbY5NN62jn3C0xrtjrv9p-Ij5tu84qImCye732JIvOFL3XT8_xOeaqjHOIHNNVYLWs3okZbk_8_32mLBq67s2kaONkhYgvlf8QkMNiiZM3wpJtPHJkbQR7vG8F7I2wgeCGsMqvJc_-keGC8PRQhAkJpgacbnaIfbVQ1QqX19pD66F3_ZS3FkaXA7L7vIG9KxMunfG-2eov9G5woKFoiES9yo9RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوق‌العاده.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/MatinSenPaii/4475" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4474">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">الان خودم ران کردم و حقیقتا جالبه</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/MatinSenPaii/4474" target="_blank">📅 22:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4473">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اگر ارور Port already in use روی ترموکس می‌گیرید، باید لوکال پورت V2rayNG رو از ۱۰۸۰۸ تغییر بدید</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/MatinSenPaii/4473" target="_blank">📅 22:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4472">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">Aether یه پروژه‌ی شبکه سریع و مقاوم - برای اینترنت آزاد Aether  با ترکیب Cloudflare  پروتکل MASQUE (روی QUIC/HTTP3) و WireGuard به‌همراه چندتا لایه مبهم‌سازی ترافیک خیلی کمک میکنه از DPI و فیلترینگ شبکه رد بشی  برنامه خودش به‌ صورت خودکار بهترین Endpoint موجود…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/MatinSenPaii/4472" target="_blank">📅 22:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4471">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/MatinSenPaii/4471" target="_blank">📅 22:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4469">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/MatinSenPaii/4469" target="_blank">📅 21:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4468">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J1TKmokduAzulB83GkX0UpwnJzM4ufIFtjorZZD2jXTmcu4NE6K567m6LQEvph80fvigTW0gNRA3vn3UXW1svva3qSd9qpD-ZNjqufmHphkZ9gWpWy_HxG68RqFyvzjxg_StjyVjl2RHhA236AE_UF993F5YihZ-mZJHO3-jRc32GYwEmfXyAjfkBS7KBQrTTFFY_P0-gcsHUp3Dcl__1ThvossO_kygN_YP3pgSkoH_ZWGAvQmmghoasMfHNaLBbPtOAKietq-LdJSHDOQyuDU3mCI9XLiMVVSSStji_gSsseqXf-LVbn9zn-ySp4L3GRgZDA3Dth052WAPNmL4DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب رفقا گویا دامنه‌ی
t.me
مجددا در دسترس قرار گرفت بعد از توییت پاول</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/4468" target="_blank">📅 19:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4467">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ببخشید.
خودتون میدونید دیگه بانو
❤️</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/4467" target="_blank">📅 19:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4466">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/a54ac3d5b4.mp4?token=eg1K73pgFBz_CcIFCTUWFgoQwm3Ck4eacEFQpA18lEmvHYZS-wmg6ZSJ3jmouSKadxFvN1lFkQCeiW7tlFVnwI5D1FsGq0FHPus7UOD60Gqgb8yg5qj-Zv8W2iSR2JQ73S5_-p1T7vSLrhiQGtiz4V_llC6m5qZo9APAe_2yYa4ulClu2ubpaMqWZzfoxI_6JwucwfDQetzgwJhlroBcm2-XrVajzD4ZrHkqydGh5er_Nc8OOiKYL7o8zKUe_uzRY8upaJ01L25SDVbEnGSlF2CoH_G9b2-i1OI-JSa2ASNHw8OZvzJNqphldmzFb6DRQkIe6i9A9egwuFQM50pPMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/a54ac3d5b4.mp4?token=eg1K73pgFBz_CcIFCTUWFgoQwm3Ck4eacEFQpA18lEmvHYZS-wmg6ZSJ3jmouSKadxFvN1lFkQCeiW7tlFVnwI5D1FsGq0FHPus7UOD60Gqgb8yg5qj-Zv8W2iSR2JQ73S5_-p1T7vSLrhiQGtiz4V_llC6m5qZo9APAe_2yYa4ulClu2ubpaMqWZzfoxI_6JwucwfDQetzgwJhlroBcm2-XrVajzD4ZrHkqydGh5er_Nc8OOiKYL7o8zKUe_uzRY8upaJ01L25SDVbEnGSlF2CoH_G9b2-i1OI-JSa2ASNHw8OZvzJNqphldmzFb6DRQkIe6i9A9egwuFQM50pPMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای خودم نگهش میداشتم
👍</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/4466" target="_blank">📅 16:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4465">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">Lira’s first challenge
🌟
به اولین چالش لیرا خوش اومدید!
🤍
این چالش برای همه‌ست؛ فرقی نمی‌کنه تا حالا از لیرا خرید کرده باشید یا نه. فقط کافیه توی این سؤال با ما همراه بشید، چون باور داریم گاهی یک جواب ساده، می‌تونه پشت خودش یک داستان قشنگ داشته باشه.  اگر…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/4465" target="_blank">📅 16:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4464">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4464" target="_blank">📅 16:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4463">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مثل اینه که یکی با Toyota دزدی کرده باشه
برق کارخونه تویوتا رو قطع کنن تا دیگه نتونه ماشین بفروشه به دزدا</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4463" target="_blank">📅 15:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4462">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromوب آموز(m J)</strong></div>
<div class="tg-text">دامنه t[.]me تلگرام به دلیل تحریم OFAC آمریکا از دسترس خارج شد.
در ۱۳ جولای ۲۰۲۶، دامنه کوتاه t[.]me تلگرام (که برای لینک کانال‌ها، گروه‌ها و پروفایل‌ها استفاده می‌شود) در سطح جهانی از DNS حذف شد و مرورگرها دیگر نمی‌توانند آن را باز کنند.دلیل:
ثبت‌کننده دامنه .me (Identity Digital) وضعیت serverHold را اعمال کرد. این اقدام مستقیماً به دلیل تحریم‌های OFAC (دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا) بود. OFAC شرکت First VPN Service (1VPNS) را به لیست تحریم‌ها اضافه کرد — سرویسی که به حداقل ۲۵ گروه باج‌افزار (از جمله Avaddon) کمک می‌کرد تا حملات خود را پنهان کنند. یکی از شناسه‌های این شرکت، کانال تلگرام t[.]me/FirstVPNService بود.
چون نمی‌توان فقط یک لینک داخل دامنه را بلاک کرد، ثبت‌کننده کل دامنه t[.]me را از DNS جهانی حذف کرد.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/4462" target="_blank">📅 15:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4461">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">جوری نوسان برق رو اعصابه که هیچ کاریمو نتونستم برسم کل روز. نه سه راهی روشن میشه که لپ تاپو بزنم شارژ، نه نت فیبر نوری کار میکنه کلا قطع شده از صبح، نه آنتن درست حسابی مونده و همش قطعی داره، نه کولر کار میکنه که بشینم لااقل یه کتاب بخونم🫩</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/4461" target="_blank">📅 14:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4460">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">جالبه که هیچ توضیحی بابتش داده نشده
هیچ واکنشی هم از سمت تلگرام هنوز ندیدیم</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4460" target="_blank">📅 10:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4459">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگیفت بازار | Gift news(𐌼𝛜)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vT72uMLyuaQi7x8dY5DhddRW96n3NvdtAiHGz5Rk4u8RVDUVcb5XWr14T4nG8nM6_dAC-bJW-dPBo8Z8DOpqNZG_Rel6Z9cw232NKpuOx0a4BQsZ_PUaqz5-KPiLluQ_SgleAr9K9H9BWjHL6l3pXWVMKBY5eHmIHKc4D6_dM2wAmiAt8TmOhcP12pH7tO6ZOxMVnTh-13NA1dLyKtImOCKKujwX0uL97aeU2cqU2n2cuaaKKKO3UCp89sqwF7u-7gfvh2LTCoIdyexye05Zb2FHrEQQY6bdDAcZZaWAVD6uMXdv6J6pmC2qUnkHvzOneAE9r7ufggp43TmPKzX-QQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4459" target="_blank">📅 10:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4458">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">الان برای یه سری کار داخل فتوشاپ، چندتا اسکریپت با Claude (پلن رایگانش. توی صفحه چت) نوشتم که کارم رو 20 برابر سریعتر کرد.
بهش فکر کردم، و به این نتیجه رسیدم که اگه فتوشاپ بلد نبودم طبیعتا نمیدونستم میتونم همچین کاری کنم.
از طرفی اگر از قابلیت‌های AI باخبر نبودم که میشه اصلا کارها رو باهاش Automate کرد یا لااقل، پرسید که "آیا فلان کار رو میشه Automate کرد یا نه؟" هم مجددا همچین چیزی به ذهنم نمی‌رسید.
اینه که شما به صرف بلد بودن کار با AI شاید نتونید از 100 درصد پتانسیل یه ابزار استفاده کنید،
از اون طرف به صرفِ "خوب" بلد بودن یه ابزار هم اگر از AI استفاده نکنید و سنتی کار کنید، به راحتی عقب میفتید.
هر دو با هم عالیه!
<تجربه‌ی شخصی. نه Fact></div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4458" target="_blank">📅 09:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4457">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚀
انتشار نسخه نهایی و پایدار MTProxyMax v1.4.0-LTS</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4457" target="_blank">📅 09:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4456">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">📱
دامنه t.me تلگرام تعلیق شد؛ قطعی ناگهانی لینک‌ها در سراسر جهان</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4456" target="_blank">📅 09:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4455">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">توی علم روانشناسی به «جوک ساختن با قضیه‌ی جنگ یا قطعی اینترنت» می‌گن طنز سیاه (Dark Humor) یا طنز گالوز (Gallows Humor). این یه مکانیسم دفاعی برای بقای روانیه، نه نشونه‌ی بی‌خیالی. مخصوصا سر قضیه‌ی جنگ
1- جنگ یعنی استرس، ترس و درموندگیِ مطلق. اگه این حجم از فشار رو سرکوب کنیم، عملا از لحاظ روانی مریض می‌شیم (و همچنین در بلندمدت می‌تونه ریسک PTSD رو افزایش بده.). جوک ساختن مثل یه سوپاپ اطمینان عمل می‌کنه و بهمون اجازه می‌ده این فشار رو به یه شکل غیرمستقیم تخلیه کنیم. (در عین پذیرش واقعیت، تحملش کنیم)
2- خندیدن روی بدن جواب می‌ده. سطح کورتیزول (هورمون استرس) رو می‌کشه پایین و اندورفین (هورمون شادی) ترشح می‌کنه. تو شرایطی که ضربان قلب رو هزاره، مغز با یه میم خنده‌دار، ترمز دستیِ استرس رو می‌کشه.
3- جورج ویلانت طنز رو جزو یکی از «بالغانه‌ترین» مکانیسم‌های دفاعی طبقه‌بندی می‌کنه. توی این حالت، ما واقعیت تلخ رو انکار نمی‌کنیم، می‌بینیمش؛ ولی با طنز یه فاصله‌ی ذهنی باهاش می‌گیریم تا بتونیم تحملش کنیم.
4- وقتی دوتا کشور می‌جنگن و موشک میره و میاد، شما هیچ کنترلی روی اوضاع نداری. اما وقتی باهاش شوخی می‌کنی، مغزت حس می‌کنه حداقل روی «روایت داستان» کنترل داره. با خودت می‌گی: "من نمی‌تونم جنگ رو متوقف کنم، ولی می‌تونم بهش بخندم!" این بهمون حس Agency و قدرت ذهنی برای مقابله‌ی نسبی با این قضیه توی ذهنمون می‌ده.
5- توی شرایط ترسناک، آدم‌ها به شدت احساس تنهایی می‌کنن. وقتی یه جوک مشترک می‌سازیم و با هم بهش می‌خندیم، یه حس همدلی‌ای این وسط شکل می‌گیره که تاب‌آوری جامعه رو مقابل این قضیه بالا می‌بره.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4455" target="_blank">📅 05:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4454">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NhoKMSai92xWmuGLmnU9yhfJtd3AZ6x_Z7Ql7nKVJe-uplqOioAJrdtnH_qzTN_Lue-85_SitbNN3wCXvLnSEVGsoukA5qMR1c8Si8FvSwCTtnFEYAM0RCUnWfE-PXtUUY4VoT6xpCM7rO5fj4P7Gisp40tqPL5KZnB6MiXxIdJBFvsmMyDtdsT-XGawgPJl8X_gYZCw1hjcGkObytzedXuIv6kCs-CisKzFGFWtT3cx2NwjgNKrQYNFLCoMK59Ui2400n5CuxscbhZon6zbxV-kisgazFbVj9vcQ4UOn2Co7fnKH6SsFl1Iuque4bcdKljiPAKHqKWCSlbdzjj3RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتباطات زیرساخت در حال لحظه شماری برای دستور قطع</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4454" target="_blank">📅 01:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4452">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uJOJld_HkWYy5hrZ7N5Si8-lgcDBuwxLXxudLxR7CrFKhfMs3NTtCsvForjfPr7qrNRjLxi6yu9I3kXSptcmWVXk5-JlNwYSms2hsHbmKWI3a7Da48MRy_CnEqS7vqZhVKhdwoTjiQEyPnI9b3bTOyIL0rmXPR1sk6rOehXuh2erE_LFmb13NXBMnUBbeNchRdHiQp-aQ1ZMz4QF6cSnPX5q68W1Xq2GRTww2gmRObn5OMLshCDoN_QyJwdmllEUuLk4_Y8b0D1ew_KpFSvgMPUJgVFdklySDO6_jQVG4iXkmHgJZz62hhh9FxpBq2kdIYN_bQf6gJ_HXM7TnG3suQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kOasbukxdGMLUEKkqnFWy-kY8FsK1QsIG8b9ZDF9HScCl5pIDfMPrJ-sDcpJTQxo1OGI2YS5W8bMtsnh199Yaq7bkLZ0FA09XqWaiUnrcf23NhfJ6XdEk91mxOfaGMEJwnFyFl7elzSHP_YqnlSXrD8ARRCKoflZwFhw5sjWP6odi1oi8lyLgi0FvwMuCIEQplvZehsNIVp_XJXb4T8Fymt4mmtgUP53e5aE4q5WZL69BM4JIIudZ26fOD4dPQrUBRw50gcivsJ_t9yELZz6pZYue0gaXskHoTntAJD9EhNcyOD1qJodmGNRtz4LM5pKE_sbu3hkrohYT_gv-xt7mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فکر کنم من یادآور خاطرات بدی هستم متاسفانه
😂</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4452" target="_blank">📅 01:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4451">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge  https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4451" target="_blank">📅 01:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4450">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">Android</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4450" target="_blank">📅 01:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4449">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">Desktop(mac-win-linux)</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4449" target="_blank">📅 01:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4448">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">Master-White-DNS-@MatinSenPaii.zip</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4448" target="_blank">📅 01:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4447">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">امکان دانلود کل ریزالور ها به ربات @dns_resolvers_bot اضافه شد   @WhiteDNS</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4447" target="_blank">📅 01:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4446">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohammad👑</strong></div>
<div class="tg-text">اگه دیدین جایی نوشت
تهران رو زدن
ثانیه بعد نت قطعه</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/4446" target="_blank">📅 01:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4445">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cDfN9WA4thytaxFGTh_AXXm57QZnhqfUBhmyOJ034nRU4waZUkgvYfo0A8M3CrKmK9F3vgG2XVN3OEzKfSdO8p8VSJcOozZYknVs_aEd-EhgtgQV-KbVbLVDsTnMKI0gTt-y3VjjDfU9vw0ARwMaKim3Uu1kaqM8h8lkuwQDCvr5K49RhxifCV9PA8fehKnVIrmAJ-4BSaqMh8n5LyEtJNV0t5ptVgQpyEO98g5oF-VRwvYLu9TaDB9BVvK9Tks-TBrxoAQzhxea5pqg1B1i8s-NK0k1qQFpo9iQvtVU5O4TwlNfSOMjGnnJEbAXLN058x2sSo4EfpRTjT87EY7mrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق معمول، پیشنهاد میکنم WhiteDNS رو راه‌اندازی کنید برای خودتون و دوستانتون
آموزش:
https://youtu.be/6Pm7kNQb3mo</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/4445" target="_blank">📅 00:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4444">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHaoodi Senpai</strong></div>
<div class="tg-text">صابرین نیوز داره لینک چنل سروش و روبیکاشو میده.
این یعنی به زودی نت بای بای
😭</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/4444" target="_blank">📅 00:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4443">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBloom.(Tin.)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBH9cm1K2c9FO4LiFH-0qb6eDQrAC_WRZFfTljWiu38np-4fl5yd9gOqFcixJIlj7uzZqhSzYBX66tDLnBwPy8Lz30imY6xDZk0AhquUq089_ECYNgjHM-KyMWLpnsG4Yu5_ANTJcQvhOzXVN0jJVbBzfecHhYiidDGnHh6YqYkIB0E3omCVtPIptcWr1jwmtj5OWrCLecM7C1OtNPkQ56BvlysuBeOUSelAzq3ZG6T0xQ84Mbz_olm76VQ7z3EkvpYFAnxVLOQWBmRc81fZnuzmsJa5OlSNRA9WfKpG5YAuvcmRYOw3si8L7QlDc-RlbPEZmb948_FXNfNOJQV67w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Solomon’s paradox
“انسان‌ها معمولاً می‌توانند برای دیگران توصیه‌های منطقی و عاقلانه ارائه دهند، اما وقتی پای زندگی خودشان وسط باشد، اغلب نمی‌توانند همان توصیه‌ها را به کار بگیرند”
روان‌شناسان معتقدند آنچه ما را از تصمیم درست دور می‌کند، کمبود منطق نیست؛ بلکه نزدیکی بیش از حد به مسئله است. هرچه یک اتفاق بیشتر با هویت، احساسات و آینده‌ی ما گره خورده باشد، و درگیری احساسی در ما ایجاد شود، احتمال سوگیری ذهنی بیشتر می‌شود و تصمیم‌گیری، سخت تر.
البته که احساسات، بخش مهم و تاثیرگذاری در تصمیم‌های هر انسان است؛ اما زمانی که فرد با موجی از احساسات مواجه میشود، ایجاد تعادل به مراتب دشوارتر میشود..</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/4443" target="_blank">📅 00:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4441">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">معرفی  Rowboat | یه همکار هوش مصنوعی که همه‌چی یادشه!   یه ابزار جالب اوپن‌سورس توی گیت‌هاب پیدا کردم به اسم Rowboat. این ابزار در واقع یه «همکار هوش مصنوعی دسکتاپی» هست که روی سیستم‌عامل‌های ویندوز، مک و لینوکس نصب می‌شه. توی اولین نگاه هم شبیه هرمس به نظر…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/4441" target="_blank">📅 23:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4440">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4440" target="_blank">📅 22:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4439">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/htCnaETETLfC-jzoXM3X6M1qGsbQ5W_OHo-UpAxZcY4fqPK9atNs00roZrIkr_lTKDMx5cUmgYoayNGJix2ryh0o9ssmClltamcNeU3MMKlAll5yNBTZgwM7Z7r5NQHZCVF_pqW8Rr4qk1EQArs_r9N0fiwL219zXqyM4rdeOcPqnh46DouRRnPYxm9HU5ELzLNdQs9cz-VoHxN7KUwOHex_AHF4Rc0gDudUzRu2Ih8AYRL8M6a0kzXg4nNLmvpGtTpMCXZGt8srMa8S73jRQfCV1IeNMwtPv5OManwsvOVPUSMiVzTI9Mz6ZmWzX7nZx3H3wwyMIOvTRv0UBTVtCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">8- بخش پایانی Integrations:
از قابلیت اتصالِ One-click به اکثر محصولات و ابزارهای پرکاربرد پشتیبانی می‌کنه.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/4439" target="_blank">📅 22:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4438">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WWIm2pJfjus_DGwM5PwVjdcrHpBIPv2v5h-bTkWoxlNrJTAL4dsEAQZRusIhzBZk_9Xju6PwfVaQ_fAnpH4EftavscE3m3xehG2whOMIyXRPUWb6MC1htYmvGc4_dtC12IFEbS-UhJ8-muZhV9BwyVlfZb6aHt-nlrZkRfHa_yPemmoWOz9MnpE9Lln2GDUN91xCYDpHjCQ6r_flgWpT5B1MBnh9od_3rdGpdlvi1nHHkKUMDgryKsW4P-fbtQbOuAUAgJuKWr_0jKKnQAor48DbSOVmcx6ZE1TewnTrCLy0hN8d72VKsiFE03cOjdZ4MYAO82fV2hM86nIJG0wdKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">7- بخش Apps:
می‌تونید فضاهای کاری اختصاصیِ خودتون رو داخل Rowboat بسازید؛ این اپ‌ها به تمام ابزارها و اتصالات دسترسی دارن و حتی می‌تونید اون‌ها رو با بقیه به اشتراک بذارید.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/4438" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4437">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uX9rYXZ-zCQdRdqyLhgvfy5YcaEKhS__fuOrFIjH5ixhYXtDKNdE79oOiKpDQtZ2_lbUH_n3i0TGIt964kyPA9IlEi16-JE_MxyUlWpF2XhuJ0wNNoDuaNIbkJ03N0mxkIl3G0h7kx6ktDFCA43Am-ejAIISDbpFsi-XV9GH-9h9ugI96ugbkZkUaz_xftlYlH5bzGqwuU0ICou5SLP0TqVL1sfb5BHUbzvxRRsY2i8HAcd4dwsCfSzENe253C0k2gpDvpn37zJoKzxguHWA3Zhn-F6EbZI_DsFbQc9hgsAhIKzyRFa1NflFIrbcGkPZHO1T1iD_YCqLuvw2sXGcHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6- بخش Code Mode:
این بخش بهتون اجازه می‌ده همزمان چند تا ایجنت کدنویس (مثل Claude Code یا Codex) بالا بیارید تا Rowboat با استفاده از کانتکست پروژه‌هاتون، اون‌ها رو هدایت کنه و کارها رو پیش ببرن.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/MatinSenPaii/4437" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4436">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R6xXJk67Ukqaq8q09MSCrr1h2rchSSRljNYhyTN4r7k0OIYdIPDXqvk62rxLfPYoevQPsa5SVhNzIkM5ZWpFcQdX7O5NDPeQvceUBQcXZ9T7qlyMX-xKmWV43hreNTjRDaUl-wkdrS4WS14m6TfmmmZVh1QCNyfv93zvpwJqEjFVAWfHQJHKiT6AscshdFW0HRBbbl--P1UpmAOKPE3OX2KnpzoDiX0B4nDQdhN56qukEPNzTwKegBYzM78uBkimXyHw8frYjr5PChkO5cZ1dyeqdizZImfQAPybVjdB7MyR-WPND9i6QPY77px37MN4YMFkbJsETygxVxjADz7T4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5- بخش Meeting Notes:
یه دستیار محلی داره که مستقیماً به میکروفون و اسپیکر سیستم وصل می‌شه، همون‌موقع صحبت‌ها رو تایپ (ترنسکریپت) می‌کنه، در نهایت خلاصه‌ی جلسه رو تو یه فایل Markdown بهتون می‌ده و گراف دانشِ سیستم رو هم آپدیت می‌کنه.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/MatinSenPaii/4436" target="_blank">📅 22:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4435">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mH9S01u8W1_SiZe1wwpDEZBAI7xbnNVoX8mjg5HC_Uufuj3lIHbSC-2VYW1UFLxBWE51YqsUdhjO4JYyloZWC_PfoSvV2LdfIFtvHolItuLJeEotP6mI_5ufcQoa-fYFQ3GBV8nDAk_QP2vIA7WLWM_4pNI8xXHms6TwmGblSEWnQmhTTW-UXaDv4h2BTsL625azPlzTXgVF70mswyiDS3ufzPC5Vnd2eThJuZ1dOh17-citK45LhBAwJdpZJQcJ5F_2BBkAWvnH8Z4IVeloiMRFT3DbCVk0uOB8SNha6U5fgwu0_iDcN9wc5v_Afx6KvCZ2b8LQasfJKQzkn9UsYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4- بخش مرورگر اختصاصی:
یه مرورگر  Built-in داره که اجازه می‌ده شما و دستیار هوش مصنوعی روی تسک‌های وب با هم کار کنید. چون این مرورگر از مرورگر اصلیِ خودتون ایزوله‌ست، می‌تونید فقط تو اکانت‌هایی لاگین کنید که دوست دارید هوش مصنوعی بهشون دسترسی داشته باشه.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/MatinSenPaii/4435" target="_blank">📅 22:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4434">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PN1-n-ePv27kNgfOaU2OOU5DIcXUXdqqi8wJr8nx_GgsVMM4IJAEhuFKCXJJzJxb_QANGMBISWTA3ijyVXnWEPbqO6TCXiO6zSamwfTzeAHA512UZZIsiMbnYgezts4ziIOaj1ThS8yEjsFSCdP08Y-Owb69TuE38tenNHYnId3PegNxm4l2JGJtkb7Z5fR9uwU_1cjLHV6oL0OO700pB-CTRcKLVDw5xmO6ceEfeU9eMNHgfyA8Pb5yKxIvDFQyGh18QaxfKWBQTlBJ6t8HIHAAMrlRzylVdjp4SiuzMZChIPxlFk9EngBH_5GAF1d6pc95JXzTyl0SvI81uYiAGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3- بخش Background agents:
می‌تونید ایجنت‌هایی بسازید که بر اساس یه اتفاق (مثلاً دریافت ایمیل جدید) یا بر اساس زمان‌بندی (مثلاً هر روز ساعت ۸ صبح) اجرا بشن. این ایجنت‌ها می‌تونن به ابزارها وصل بشن، تو وب سرچ کنن، از مرورگر استفاده کنن و حتی با Claude Code یا Codex براتون کد بنویسن.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/MatinSenPaii/4434" target="_blank">📅 22:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4433">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lpBk_QW1h8Lr-Pg7p4xvRGj48d6A_tV4l-nwLEu-KVJGCFnHnwbUMkX833jeAPjvIArtj81yPc2ahh7TGPVj9nqCF9SjNdNUS5JDPjHt5gCEJwJxamxYP0N2eVYDrXgzINH9GC9_QngqmDu73_beRLWhBulh48XlWTmDv7xqGhsAFxvKPcJg4ae9zmShgrIf68x0wflInjjN27U-a2G3oRan9rJSylvv8HBRZnzc3HGZ78df3GcZ6msCzBCc8Rklk7F32Ef1zEui89txwPijT07Ium_F6Xo7B6WoIgfpcKR1Tv9CslpYalTWdsXAb2M54u7lQIOtRsvCfjG-vD0zjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2- بخش Email:
یه بخش ایمیل داخلی که ایمیل‌های مهم رو از بقیه جدا می‌کنه. بعدش با استفاده از تمام اطلاعات و دیتایی که از کارهای شما داره، به‌صورت خودکار برای ایمیل‌های مهم پیش‌نویسِ جواب می‌نویسه.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/MatinSenPaii/4433" target="_blank">📅 22:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4432">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eo0mdg93mfgwZlq3w15SvqSx4SluHLrFSpJP8eipAOE2Mf3uB-EEmm1QOiawVnIRRVd7WSaQ-15RiX1xomwOGJ9EGl9WvmGWvc2f1-IJa2jRqSippRYYNrVyxFklz4uyddVHt8WOW5_0S75jpkY0-lGL8QspheOR-BGcMnMDdDOjCIB4ryBgDv37gI2WBz8xBV5crkKdcWWu6Pmj9tp1-9nqg2YZDkzLkD_kOLqUM3jVBl7o5srfxrqkfXVpMTIUXZGszrbw94dFDxKRMa_2XL7kZ-Pp3Wp3Lbvh4zSfv5zBoDstFfeYuj-zij7n_3CtgbwQFJzp1MCnrK0jJIro0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1- بخش Brain(مغز)
کل ایمیل‌ها، جلسات، پیام‌های اسلک و چت‌هایی که با دستیار داشتید رو به یه گراف دانشِ به‌هم‌پیوسته (دقیقاً شبیه استایل نرم‌افزار Obsidian) تبدیل می‌کنه.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/MatinSenPaii/4432" target="_blank">📅 22:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4431">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بذارید تک تک نشونتون بدم
👀</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/MatinSenPaii/4431" target="_blank">📅 22:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4430">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uY8EsFqZbffD1OkpQeuRzM6kBEr3NB5RW8Oq_V5VJVVtSeL3Tw1X47WVYAEMdjUToVM9d_ZHI5emBPxQn930zkts2L-22MsdGWYoTCycTEQZDp0LlKdkBGCg53pf6cCCdAuduL8O9gHmr7oojTk5l65Az1F24LiIyeObSvVfXxiDHrix8TCF5ymwqgTA5i3JKguh0uMkVD1oXAlJuyZ6-d3KU-FrQKWYu3adJIzn1gRHUF2KcjuWtrMlKlEh5QijyUgy2pDFlJvHzs0WlIgEQeby8DbWWNpZXCTQ0zAiETJlU_nd8FX55l48ATqv9wB1f7-ujcJ_MQrhbHbcIAf9Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی  Rowboat | یه همکار هوش مصنوعی که همه‌چی یادشه!   یه ابزار جالب اوپن‌سورس توی گیت‌هاب پیدا کردم به اسم Rowboat. این ابزار در واقع یه «همکار هوش مصنوعی دسکتاپی» هست که روی سیستم‌عامل‌های ویندوز، مک و لینوکس نصب می‌شه. توی اولین نگاه هم شبیه هرمس به نظر…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/MatinSenPaii/4430" target="_blank">📅 22:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4429">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pIrjRqNjb935RZfaM5sJQLyuT33o6nVnC9BbaaJJ0P92XKEORgatoH_mMpE7ok2Xis6quO6eLJIjvNOJrdX9wKLmWO1yGocmiUG73KFCbQUkJ_6NNPu6_xsgVKXWCcv-AztUdFBhs8kxOsZWlh8D9yvEHSGOmOBPVKGvYAlz5oKSJLLz0dbNVSXB4KNd2WCM41tYQnDFCayPYoA57PuRSegEMHBO1AGUzxECeYZFr005SHSWFoITRyTB3eh2qK0lXLLWjMgOICdMmfYHiWKtnqQArIoTgEn2UVMWQ5Twk2MkgLR6Az3M_4ckapeqZMduu6XtZLVf0-KNFG-jWLwpSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/4429" target="_blank">📅 22:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4427">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rHfWTGclQtRr-dL4BE1GHwV7ok_wASriaNgn2jii9SSeBS7ROGYRmxXsIkcmvMxCdUGp7CRYq3nscWYh9jM-Lmx4LRbk1AUz51eJP28HMNxb1koeFkvXbk7HL9bT5xe1XYnJYYmPHhx8C0blZyGtRgcARp9iMqmiYhV39Wfs2ggBMuDeURXJzFqO28-qoZd2w2Dd3ilabDCArPLBYO1aOMxGwuQdFdeMSNC8GlSq4gvIeXEFfsRctBMgwdfFxDvOxST75g7YUq6YLJ4yiZlzDF_Fe1saEcaNVs88r-Bf6csv1oxtdzlMAF06AXGCJMIaY7HndBqxkUhO04jRrUZYlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/18c4e8f180.mp4?token=Wp1eW4lpAdk6MNm26wElB1iHRSAFhhsm5lwNh9mtxaMvf0UuLIvNmlu-GKEwH_-UT4X91b71jRA0i9UsnbD5QXwBJ1OaHFZRZavmD0uGTX2g73frOS1ydm8T8zFsFVAXSi-Uq8HKDquzAEO9WKqtZ_TcExGy0OYT-VGIOaD_N2_udB-KybIhxMtgF8aQkHNqJfgGRLNtZoc5A_JcjM88q_R3KDLLpuhjhge-y6DttOmVvlFAcOraeuj9aWZ1UMrx-yhZrjXtII_vMlI9OB_WmUuhuj2-8jM6JI-YYIlUkYl9suUFS4B78G3hax4O6pqRsYwpOfKjLWzlhEewLUtD-g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/18c4e8f180.mp4?token=Wp1eW4lpAdk6MNm26wElB1iHRSAFhhsm5lwNh9mtxaMvf0UuLIvNmlu-GKEwH_-UT4X91b71jRA0i9UsnbD5QXwBJ1OaHFZRZavmD0uGTX2g73frOS1ydm8T8zFsFVAXSi-Uq8HKDquzAEO9WKqtZ_TcExGy0OYT-VGIOaD_N2_udB-KybIhxMtgF8aQkHNqJfgGRLNtZoc5A_JcjM88q_R3KDLLpuhjhge-y6DttOmVvlFAcOraeuj9aWZ1UMrx-yhZrjXtII_vMlI9OB_WmUuhuj2-8jM6JI-YYIlUkYl9suUFS4B78G3hax4O6pqRsYwpOfKjLWzlhEewLUtD-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چیزی که برام ساخت خوب بود. میتونم بگم در حد OPUS 4.8 + Claude Design هست. برای وان شات خوب بود واقعا
اون پایین هم زده هرمس باگشه. مدلی که استفاده شده grok 4.5 هست</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/MatinSenPaii/4427" target="_blank">📅 22:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4426">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EyM02ZIYlAWr4PNlQXWdFhmir0z5QBTkoPqOZTqgM088qkSiLlc8pc0fJHJQsAKq8IAz8C_WyQ0IFRf1UWEM5qbTdFAo85d0-RYzLN3ZCIXXU3KRJGo3M0gOINzrzlD6HxEKAbPuFj-uuuziAxlKNKJ6W43Ox9S6fwN96ESgC3nAyRJTEkxzIIn_BrpqNcqqpj1MAf-SkLAT4D0OW8tfRxhCdp08CWu8m2xtijHicv90pqxZDZcxgI0RmRwIrdzSd2ubolQinSMm9HfC1WHZNVcMpySFFUkOltAk-IYXi_LF7UM-3OyO_VzVH1e5nAt_NWW1dLf4e0FiKpTkUMCT6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با atomic mail یه اکانت ساختم بهش وصل کردم مجددا
😁
روی سرور</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/MatinSenPaii/4426" target="_blank">📅 21:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4425">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X8W0oTPVo9shVAZVcZAJIoQSaz6-Hi0_rgXZx4992VH3MgCmKXavsoLIKVFxEg8h5Yd9cQ4amYskZPE8qF4JPGVXeDhhrzFVql48-hecIE0FqXaoteLEN0DH1gEQZJwMEE6C2uXwxSdHZGfBwaOb4pY9PO4N0yhZG5Nn-sk33ezJCnwuglrUjOSN8ocT5JOve8P8vvcdNMBYIoUlkkMtMvXzKaGtKaZpbZovGi-NMkWb_TS08plNqf3010cqjhuUQKXGsBfr7L7dDG5QuVUuhaCzmBm1--ezZu_vqzf_NwaJqYO8loQzEQuuLN2_2ISZa7mq6DEZS0i_iQhng6y_BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با atomic mail یه اکانت ساختم بهش وصل کردم مجددا
😁
روی سرور</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/MatinSenPaii/4425" target="_blank">📅 21:31 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4424">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دقت کنید روی ویندوز حتما باید proxifier روشن باشه که روی ترمینال هم تانل بشه وی پی انتون</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/4424" target="_blank">📅 21:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4423">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گویا روی grok cli می‌تونید با Context 500 هزارتایی به مدت محدود ولی به صورت رایگان از Grok-4.5 استفاده کنید(قدرتش هم سطح Opus-4.8 بوده توی بنچمارک‌ها) نصب روی powershell ویندوز:  irm https://x.ai/cli/install.ps1 | iex نصب روی سرور:  curl -fsSL https://x.a…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/4423" target="_blank">📅 21:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4422">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X5Cc3zQZoBZO1IikNFlvg1ONTZ4RRSTKSLMa7y1E3wAzYW9SmpPcBTKDMMulmLb_x7Z7l2GhQrN-UbywKvSOtmD40Rmb4txb8K8blhI6qP5w9uu8MSiySJkkoQ_Z_15ELG7yls-9Q6WJX6ZSqCUomNYs5gHEX29EixKaWeO33w7eRckFApWy0ZxvGX35QOormFLG5h5voGn6Z4CoJYyLvM3ew-pdZl8l7Y0NSdL-fgLdtK8jnvETpZhCIZ5TbzzDM6VFysvJVKXc31SD0HXLfYVX0zwM3ZbZ4Xv_i-JUyH2WVO0wIcAr0v2WQzNMI8bvP4JDB93kpK-nk6YLhIEKYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا روی grok cli می‌تونید با Context 500 هزارتایی به مدت محدود ولی به صورت رایگان از Grok-4.5 استفاده کنید(قدرتش هم سطح Opus-4.8 بوده توی بنچمارک‌ها)
نصب روی powershell ویندوز:
irm https://x.ai/cli/install.ps1 | iex
نصب روی سرور:
curl -fsSL https://x.ai/cli/install.sh | bash</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4422" target="_blank">📅 21:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4420">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WQI4-gAZVr_eGAsJ972BjJXv0fmRI2FGajSLkgZ6etoeM0sqXpp1Dx815KsKD3oSiGA9jSjiuvS4RPOhWeBrm8TQ8J_1e2Dt-F--4pNF_Gr3y8llTULTDJ6YlJSDUZ5Wii6Fo6fo1ocMsq5w3GkKrTT01theOwweFRqWjWT8uGRuzzaabR3fqjHZdpZpzXR-TAYBaf7FFwLtSkP3SQXC19HoB8bxtg910tNgPsiIA9g6b0FYIhJE5BscTb0GhpJjFMYoxnveSHZ1vvvbLvJLt3EGj5YqRivwiweu98IA5V2yhSC42VONVzE9pjMl_fZ95oiqdCjW2_hganYDbblkuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BAqLk-NrXmmQ_bZtkobvKCPo9hLONMPSKt4udI_XwP8H2SKLSm3MdJRbh8xZIzP8lHXNPcIBf7IyfW8lLR3S0gMH7DKA_Oe1X7RZircFWzbZw86ogNA0o61cyivuJxqLcweqT7pKPNJrQUWsWNSXOTyFhHX48bPocHkiuclD5ErhSIaZUicoHQ1aTanjRjR3w9M-IUFblnkdf4C5ezasAAFPV4A2SibJUKpuxgR-dYb3apvvWWA4mkRW5CHM0vfOtMx2C-BV9mxXVd0zBqysMcdjPm2T5UKX3MkVfQzrGYfoL1kPbslLSqO-d_-tICm-uwhf6UWvF1BJSZM6CrgKGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فکر کنم راه استفاده از Meta AI بدون خطای ریجن رو کشف کردم!
با کلی IP مختلف (حتی آمریکا)، اکانت با شماره آمریکا و جیمیل تست کردم ولی بازم ریجن می‌داد.
اما با سرور آمریکا Mullvad خیلی راحت باز شد (حتی اکانتی که با جیمیل ساختم) و کار می‌کنه..
البته اگه مشکلی پیش نیاد :)
++ با فیدبکی که بچه ها بهم دادن ، با windscribe و Surfshark هم نتیجه داده
✍️
AmirHossein JPL</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4420" target="_blank">📅 21:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4418">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AQN4t-ArOgVctFkdsFM2H1_lfwDjpXOsZdprBITuVBFzO7bhhUTgKj72vlXOiHWcw_OAeMo1d7f0RGiYfWA7hxzcpCc78o1bA4FKjvyrJM-rb-283EvpPNNJE7ZXhAtEkgU9uaHDmBU20gBbph2rPDAM7lkkqgWLa9HXmEuf2-OBe_IP-7dMmpuGDlDuG95Hq_FnqZlYBwWKV1WTIyuYXuRM3yJYyuUF5GOH-EdXoMatQQZYNTmePQ1Cy3h9Xi380tlKpRvBUwsoT22NS740mTRLTvDpKX7JtI2AW5cbYg9fdtkY8De1uM4MHHapRaWFL6eSDr1hNb6fY-hZXTM_5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kUy2gDQOI1LZzpNHpzOqctCdOqaltwKUKqanPe8OSlo6Xfp_3huqVBFpnmtovVk2eVH7eHGCFWqqdVn_yucBe1MsFVTzRyHIVODNJTlD__GLISIwix5hvuoDiWY0i1NwMP_DLX2igZgCO0OGyFP7o1BCOFXM6gUyaXiP45Bsa5kxJmqkNYueTFwNxSrXllum5bM6E3TLc4qbGcBEFwDIg8gmcUYLsqLqDrAljvprZi46dGtcCCNoTnSW5XFqbqxbkSKNGzk-EUweYJ333m4hjKrliM9b-6i4CDLZxah52ms0xZWd5gSPF7jZ_TfAG-pW-bsTGxuU_epdFG76kSUz5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مأموریت شکست خورد بچه‌ها
فقط اون جمله‌ای که آخر گفت</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4418" target="_blank">📅 12:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4417">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i5xKeyICTLUPWBa695vUF2a1Hnih9--6VH7tbZCiXj4IM8jHPkPsOLLS4vE8r7WMtkYtnLCeruOxFm7EyPXsPC6ia3xE5opcsLHm6Uw8HnKTYVDjTvbYQhDxLeQCu6qw4W3MgOburfa4rtiMnLH4sbjXf48zr8pqzzRc-XbRNINgjm46-zW-WN-t3ZBiUdx0q-4N-BnW8gtMm-6bxkuPS3D_k3gxPeIepWdQ8eOEpPHGn3DU8hU03QHtS99pZumjqUByNgj0lk1xrdMIIaJD5tp17XgGnh94389yDdiljA73b5yp22411NzXqlP2nE82-9M_qnHYJFyQqY0n63OOsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4417" target="_blank">📅 11:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4416">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گویا برق قسمت‌هایی از اهواز رفت.
دلیلش هم حمله به زیرساخت برق بیان شده.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4416" target="_blank">📅 03:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4415">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دوست ندارم که ویدئو رو بیشتر از این اسپویل کنم، اما جواب سؤال "آیا AI جای ما رو میگیره یا نه"، اینه که ماهیت سؤال غلطه.
چون این قضیه یه switch خاموش روشن نیست.
یه طیفه</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4415" target="_blank">📅 23:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4414">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/62284d12b0.mp4?token=NEQVpgkY-73yGYaZ9tH72WGX0sQSH_18hg-F3CQZWH_WTArDOP7CQDEpYUZbvRehSGeSm09YBJJ3z88IuJREjOy7JBYkFnsZtDg9eELJd0MmYKFtnHdILZijCXa01k9mCgDLBk0JRp3q8WdW5s0Amklgs_nFrn-0tHarGbvDUM6tVfTdNM5FYPFw70rd4pDSl3Y6WOgGZbM3goWx0CR9AP9DdN9If3pVE_mNCvKMWrsCl2WV3z-15YXUc0SU17y_Rlldttja4tEphQNicTWC1keDHPcq_lylBk4X4OEqn8LFzy_9GjGSCI_JY2CB3JszuYO9wy65BPGvziYQLvjRmg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/62284d12b0.mp4?token=NEQVpgkY-73yGYaZ9tH72WGX0sQSH_18hg-F3CQZWH_WTArDOP7CQDEpYUZbvRehSGeSm09YBJJ3z88IuJREjOy7JBYkFnsZtDg9eELJd0MmYKFtnHdILZijCXa01k9mCgDLBk0JRp3q8WdW5s0Amklgs_nFrn-0tHarGbvDUM6tVfTdNM5FYPFw70rd4pDSl3Y6WOgGZbM3goWx0CR9AP9DdN9If3pVE_mNCvKMWrsCl2WV3z-15YXUc0SU17y_Rlldttja4tEphQNicTWC1keDHPcq_lylBk4X4OEqn8LFzy_9GjGSCI_JY2CB3JszuYO9wy65BPGvziYQLvjRmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آیا AI جای ما رو میگیره توی کارمون؟ ویدئویی پر از واقعیت‌هایی که باید گفته بشه. و کسی راجبشون صحبت نمیکنه پیشنهادم اینه که امشب شما هم این ویدئو رو ببینید. طولانیه اما پر از درس https://www.youtube.com/watch?v=gR2OCyKBF7Y با تشکر از یاشار عزیز.</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4414" target="_blank">📅 23:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4413">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">آیا AI جای ما رو میگیره توی کارمون؟
ویدئویی پر از واقعیت‌هایی که باید گفته بشه. و کسی راجبشون صحبت نمیکنه
پیشنهادم اینه که امشب شما هم این ویدئو رو ببینید.
طولانیه اما پر از درس
https://www.youtube.com/watch?v=gR2OCyKBF7Y
با تشکر از یاشار عزیز.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4413" target="_blank">📅 23:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4412">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">یه گزارش هم بدم
ponytail تا الان واسم توی کدنویسی، فوق‌العاده بوده
https://t.me/MatinSenPaii/4359
همینطور skill improve که معرفی کرده بودم
https://t.me/MatinSenPaii/4373</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4412" target="_blank">📅 23:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4411">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">به حق چیزای ندیده. مردم چه چیزها که به ذهنشون نمی‌رسه</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/4411" target="_blank">📅 23:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4410">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یه دولوپر زبانی به اسم Skillscript طراحی کرده که باهاش می‌تونید به صورت دقیق و ساختاریافته به ایجنت‌های لوکال (AI Agents) بگید چیکار کنن. مشکل اینجا بود که ایجنت‌ها برای کارهای روتین هر روزه (مثل چک کردن تیکت‌ها یا بررسی پایپ‌لاین دیپلوی) هر بار سعی می‌کردن همه‌چیز رو از صفر درک کنن که هم توکن الکی مصرف می‌شد و هم بعضی وقتا اشتباه می‌کردن (Hallucination). حالا با این زبان می‌تونید سناریوها رو به صورت خوانا بنویسید، ورژن‌بندی کنید و با خیال راحت بهشون بسپارید.
که چیز خیلی بامزه‌ایه و باعث کاهش قابل توجه توکن‌ها می‌شه:
https://github.com/sshwarts/skillscript</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4410" target="_blank">📅 23:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4409">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یه پرامپت، سه تا AI اولی GPT دومی جمنای نانو بنانا 2 سومی در کمال تعجب، Meta!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/4409" target="_blank">📅 23:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4406">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iYS5x0LPJGWinZAA2kvOkX7S3uAFclYuoaRl1ZSzKPMRCOG7KYzz8YvILUkLnATynirwTHkucS__tRzdms-XsQCvZXmGr-a7dmaYg_R-_g8VPkaDef-3qaf-BnezKRmezjS7v58UBKyVbI47obxmOTXIDqhIHlCTx0zSA2IqFqTRAgLo3qQu7_Gihlc21OhGWwLq-dBFkywLxk3DmDtDFZ9dCoIbTQVs70-QeP-ZWByiWTFnZlwMQNTFYiTScbLzQSUs7Q3GNpqgHGEaPMHQZM-JNIerfz67Cj1oJMHYeVTWID5_dsQMIHVUqALRYRYfAf3Iq6OMGv6kMVAL2lGgiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hME2A6dU1hEzvckeNoKRUKwMAagIFyqNhmmRxBVUKWHzCb79anBBmD3BdG5ZJAL7_BrDMhHfdq7V3gBAz61io7DA3Q6ocIrRBDZMMqu-2zyBjPODbg3JBMyEI9Xp8lKe6dCJcmaGa-z64i2NJohy0Ge20dSTH5kKkTYdP1LRU8gEVLfgNWhEzSwQ4hmMbraMAFL2lwS5QA0Ew6bwc-UQ1rBwIc8X-r-DZ7lAL_d6IwtE2plFOG8YYV-o6cHGsdje7sRh3hFYgZwt85jqix085f5WdZ2U88XofVereaWe-bujsPa9jG5yFCXI7qnbYs5SKOc7qUkFjug672IlMeo98w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/n0yQoO6sIsQFXtUYhnL4K0eoJjU-8xJTpqJY6v-vGGhL7KB5VVyafL6rZb1F2dDMkf4ppj8YxLHNiGC7OTKwGHIQDLtRTdehHRGR-oMZ0ObDdUdkXNlu-VkOvc5_6cg-lq9LDwIb2nlAWkgkpsHFq75yeaLK0QeSdYerwjlNRV9MeGbTswflFAOHdrAdXWlRLI_2RH8w4RRi-Ga36Z9U3CdJzLNuL11a_w85-eUnW7Aexy7jwUbMtYUuyyxKEqFnZ9dJ8DMBEub_ib9juJFNtg00ev3SKsuFZucJkkQnFESYjQ4zy_EGlRflbwHsPTCNWKGiKk7S-3HS8Tpjf9Sgog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه پرامپت، سه تا AI
اولی GPT
دومی جمنای نانو بنانا 2
سومی در کمال تعجب، Meta!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/4406" target="_blank">📅 23:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4405">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k4kTQpV046Zye_kLZ_YT0SxEZbz668CesE7hGJvQpLNjrki3WTv_9Zoiov-4UZ5Bpg-5d5WDIhvhCV_xBDXz69vW5JwXQfsBbjVchlyxySD7y00UDrpPVLi-b-8H36fwl-yNX5Pt70ITdiooqpeUQBTlaqdwoh0ZBpbTSmHCvckFYIhCaE-xD6fSFcgH82aIcL7Pkiwb50Oum8OznTcZaGRsevNW89OEv2CGPjMq4hqXGzxGDNZHx9NtQ08qkAC3QnmTCXqCf_ROFx7enNBpZrjANAj0qptw17gZw1Mq4y9KycuEoEpz8W710v5lAtASZGzHUCym_pNOfvYntnbsTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت Theo:
gpt-5.6-sol is meaningfully better in Claude Code than in Codex
It MAKES BETTER DESIGNS. WHY. WHY IS IT BETTER AT DESIGN WHEN USED IN CLAUDE CODE.
و داره میگه که وقتی gpt 5.6 sol رو توی کلاد استفاده کرده نتیجه‌ی خیلی بهتری توی دیزاین گرفته. که احتمالا به خاطر harness و ابزارهایی بوده که کلاد در اختیار داشته.
✍️
Theo</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4405" target="_blank">📅 21:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4404">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXbYXCWTMHRMMyBCMcOXKVNLZNhILn5TD2xQ8n7JlehwIoX2metxv5O1xbmuvxWbQ1FmRW78dq4nIIgNKtR3lqZ_Asi35hrXplGwkJoqW239nMia06CzQf7gAOwRFmnrNxHOyAOoQun6wsLo7bRI1EThEexwvx1iFpRzb1h4IRCs8n_FvwCqnaqZCUaCLsGyevGT8JHPXCB5dKBiowCi45VVp-xR58dIZxHt0mmdYcM-aoobISP7TjxAAJA3R8e8BxZ9nJyOMHTmZgo-snJXeUTi7d4XqqLcAj4xHT7ieVidEYsFBelXTaMfW956vTkWqJC8pG5-r1-RRZiIAcJzyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Intra با استفاده از فناوری DNS-over-HTTPS (DoH) درخواست‌های DNS رو رمزنگاری می‌کنه تا اپراتور اینترنت یا هر واسطه‌ای نتونه آدرس سایت‌هایی که باز می‌کنید رو دستکاری، مسدود یا به مسیر اشتباه هدایت کنه.  این برنامه فیلترشکن نیست و آیپی شما رو تغییر نمیده،…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/MatinSenPaii/4404" target="_blank">📅 21:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4403">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فونتی ساختن به اسم Ghost Font، که هیچ هوش مصنوعی‌ای نمی‌تونه اونو بخونه. فقط انسان‌ها:) توی این ویدئو، نوشته شده Matin SenPai. کمی دقت کنید می‌بینید  از اینجا می‌تونید ببینید خودتون: https://www.mixfont.com/ghost-font</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/4403" target="_blank">📅 20:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4402">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/85ce09c5d5.mp4?token=bGUS9dAgIr--PmWfsCEa_NB3hXaCn_BnrQ4W_GAcSbHJqFlm5sa_kDcibTqXqG1iniufzKw5RvFTdhwvuzH1PAQeRQGDyvBtw8M2XJGMzv5yIGWwQeQgoQnqCAik95V26pKzoa9XpwXu3ZOZVRsC2KGGoyqrZ62fEQBqU5e0P2gFsdwpKfEpJo49dUdG0FwVT6P_pyPVIeuAnguDhGC6dw2DSggR5sgFdUa3hvJYRMIBgAxe-shPg_ChBZC_UTsLX52PWH0_RowCrrun8Tqao7XQ58j3z-f3FERgvaLmtqjrKRBZocpNN9uG7tsLE7kiszpd7_F5ymcEwAOJBYW5ng" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/85ce09c5d5.mp4?token=bGUS9dAgIr--PmWfsCEa_NB3hXaCn_BnrQ4W_GAcSbHJqFlm5sa_kDcibTqXqG1iniufzKw5RvFTdhwvuzH1PAQeRQGDyvBtw8M2XJGMzv5yIGWwQeQgoQnqCAik95V26pKzoa9XpwXu3ZOZVRsC2KGGoyqrZ62fEQBqU5e0P2gFsdwpKfEpJo49dUdG0FwVT6P_pyPVIeuAnguDhGC6dw2DSggR5sgFdUa3hvJYRMIBgAxe-shPg_ChBZC_UTsLX52PWH0_RowCrrun8Tqao7XQ58j3z-f3FERgvaLmtqjrKRBZocpNN9uG7tsLE7kiszpd7_F5ymcEwAOJBYW5ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فونتی ساختن به اسم Ghost Font، که هیچ هوش مصنوعی‌ای نمی‌تونه اونو بخونه. فقط انسان‌ها:)
توی این ویدئو، نوشته شده Matin SenPai. کمی دقت کنید می‌بینید
از اینجا می‌تونید ببینید خودتون:
https://www.mixfont.com/ghost-font</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4402" target="_blank">📅 19:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4401">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🎧</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4401" target="_blank">📅 18:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4400">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">الان وقتی برق بره، بیشتر خوشحالم
😂
😭</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4400" target="_blank">📅 18:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4399">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/du977pEhg-lhgt98lWTaKnqwxF2dKuXfEC-es_ezsUkYBqkDVbcKyKnyp7UmSvKKZwOeHjkqxIOMzFvueDxD1PgNlClVo_3ih1eI7rMWZsO9oJa47hvWYsa_85OZ75psjelwsLlsGjGGzQoEMGc-xbrFuKKNhDP7H2JhfEEyutNiGu_lT49z8MvG-cpo3ZvYGb7PY5kbkOK2gebEj4nPkaWt_1rmBquIUBKzWXAsPiI1uUPPJ_FIJqnbFf2YRnJp5i5RUN3huJgeDgGAQfZFTmPg5SPCQvWY24T4Ho19Ch0JZ9AZmlWwMb3oZTKIk_GmxN-gLrrttg46O_HwcZkP2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره وسوسه شدم و باز کردم
از عکساش صد برابر باحال تره اصلا دوربین نمی‌تونه نشون بده به خوبی</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4399" target="_blank">📅 18:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4398">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PjTTvevbWeHaNxX5r_MSPi07gEmNKuGkN5UUCY9rW11Cs10fooWHMPOtmgAy5sb4an5_uTzaVcBl0k2SklcJKZxfzQWu4SUVWybC0rIgX5j5_tHt2RUAMnMQ11DNjv1-8WndgbHYtR0W3SkwM6IJ53eg89EfGFImY3Q6_zeVjc6QJjZnzUyaQViuqLGlJKglcNs8VYLtzefY4KRdNExzk8hMdzVtwg34gdF3zlXWywyIAl35B1qGE-wIC_9jzF_MAZWWOIB8G8KuYTtQ_V5XsnVmfinPW12525Cu9PvEZD_QjPxNHTzIM0LiMJSptlqBQnf_Y04_t9TTJcRLF3kYPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمع‌هایی که
فروشگاه لیرا برام فرستاده
انقدر خوشگله که حتی دلم نمیاد سلفون دورشون رو باز کنم
😭
اصلا یک جور عجیبی خاص هستن از نزدیک</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/4398" target="_blank">📅 18:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4397">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NQTv-YMsgXpRVcYPOitiyEPTaBQ5OZMJmoK_sge56YTjtpdYnFZ_hgik7o8B2GcP4ruBaKaufFt9734M8Fhu0mi8228zGUiiQTvsQWE59Z6zdgX2wep9fG8wSzOZANnlR9jOKQd-FSE3rQEX3ysuVk1HtbrBC9K0eoM_qk_cpcH-r412NA_N56XQqxP_gdHzMqL8p6uX40AR34d5ws0S57b92oIZWiJXxYLJiciQYQdopvj5TOQXwXwN4uliJgvwEJ8ITAS3rkU2D6l09VAEpntnY0p8Z_zT7GRT2kiMiNjxzuksNoOM70g9jAcSabgDN3Usnb3TQhbQ33d7yKW9qg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4397" target="_blank">📅 15:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4396">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اگه خبر ندارید، گوگل به‌تازگی یکی از بهترین ابزارهای هوش مصنوعیش رو راه‌اندازی کرده: CodeWiki! یه جورایی می‌شه گفت نسخه‌ی ویژه‌ی برنامه‌نویسی NotebookLM هست.  کافیه یه ریپو اوپن‌سورس گیت‌هاب رو توش آپلود کنید تا CodeWiki اون رو به یه راهنمای کاملاً تعاملی…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4396" target="_blank">📅 15:16 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
