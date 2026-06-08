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
<img src="https://cdn4.telesco.pe/file/kMA480aO3f68fndHC4hfG6R_FWf5dLBG8Gc3gO4v6jfzcDIhmnQWE4Hb3HdGdWwuXe-NLIsP8dO8zJ2yY07hL8dvPOgFsHTQMcYR86goavRIV4yZEdxbV4b3c1BZKPuYERw7PlZ1-TEYoXFc6rHOpx8KE6EhFB1QYfQVQMrlE0-vKYaQmjsIm0FooRTTuMzsws5dEvkTgUhX9VCqpZu2VFNV8ZtktZKsTmOyPgR8lsC9rjB7sPY7Q8s_o5gdkjF8DDj3vtu9hhHNs53rH_1BFJftUEtTYobIxlGoXH55tAWy_8npmAdarsrfjuo6DoHTRhxRCg7Gcud9kPWnySH9WQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 23:33:16</div>
<hr>

<div class="tg-post" id="msg-440822">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9Pa5wHE7vULHaN6eBrJ63fMPAFB106FxicP0BNQS4Fl-UNMFUk-v5_RXtcXeIp5JYhRdv9mHngo728ac_-nyaPoCSxzAUHqucNJ8KG5iirFoWSJ3S32xDVZKD1DQbzdJk0tsra1EGlo3I05Br0G3jedz1WPxGJBYcn-B1TyP0r5EuW65NfYvQ03HUsMZsNz0QpAcBKNPvVa12xBju_cpqU4JdEcWqdtkXhn7FvxL5W5EhzSh4o_lu1QKGLODSsvo9SCbFgGQlC-xkjvxCCuNTUPPgSjjaNDDg9G3FrRasKg8NPPaKDee6phEuC34Wji1k0ejmisFqlGaeW2s-0JYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام آمریکایی به آکسیوس: نتانیاهو برای بقای سیاسی خود نیاز به جنگ دارد و ترامپ برای زنده‌ماندن در فضای سیاسی نیاز دارد که جنگ پایان یابد
@Farsna</div>
<div class="tg-footer">👁️ 343 · <a href="https://t.me/farsna/440822" target="_blank">📅 23:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440821">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5710e1356c.mp4?token=Ku4pqqzgquD_6DnTT5CZBEQ3aaqmIQjqtvFFTCZQ_OubvzTvhtFgp9XpHql7pzdeXeR1ikcTCbkBDcj_eQV8cQ-DSvZUoGgcrgpKOtSYsotASPqKmfHjdbtsxkAanOeazCGqjMAS7K8_jxj2OvFJzu6OVOCNns46sJc7ngG0rdUWj4GdjLNYRs-voIc2IcAcdIwdrHQWPpYM7MDiN0oR7P-J9_jz9yvalyMqMXV19tK1J9bf-e8etmNAOwnaY1s9Lcb3faK-nyqbG65_njGb4yvP4yuKM8Qw3Zg_2jZw0zFokLXc6sAIZyTmLt4SO-qOuDlLi_Hl0HnuXKAzeYyj_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5710e1356c.mp4?token=Ku4pqqzgquD_6DnTT5CZBEQ3aaqmIQjqtvFFTCZQ_OubvzTvhtFgp9XpHql7pzdeXeR1ikcTCbkBDcj_eQV8cQ-DSvZUoGgcrgpKOtSYsotASPqKmfHjdbtsxkAanOeazCGqjMAS7K8_jxj2OvFJzu6OVOCNns46sJc7ngG0rdUWj4GdjLNYRs-voIc2IcAcdIwdrHQWPpYM7MDiN0oR7P-J9_jz9yvalyMqMXV19tK1J9bf-e8etmNAOwnaY1s9Lcb3faK-nyqbG65_njGb4yvP4yuKM8Qw3Zg_2jZw0zFokLXc6sAIZyTmLt4SO-qOuDlLi_Hl0HnuXKAzeYyj_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سخنگوی نیروهای مسلح یمن:‌ از این لحظه تردد کشتی‌های اسرائیلی در دریای سرخ ممنوع است
🔹
یحیی سریع: در چهارچوب مقابله با تجاوز آمریکایی-صهیونیستی علیه محور جهاد و مقاومت در ایران، فلسطین، لبنان، عراق و یمن و مقابله با پروژهٔ صهیونیستی «اسرائیل بزرگ» و در راستای…</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/farsna/440821" target="_blank">📅 23:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440820">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">Live stream finished (1 hour)</div>
<div class="tg-footer"><a href="https://t.me/farsna/440820" target="_blank">📅 23:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440819">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🎥
۱۰۰ روز نبرد مقدس؛ یک حماسهٔ ماندگار
@Farsna</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/farsna/440819" target="_blank">📅 23:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440818">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43b9e87bfd.mp4?token=aaTvomlpOVe3HKmI5AMrdVi4YiMc7dp5w4C0mDgETscgz_PJwhbH9kwWA5beFv48y5f1zCUQH1yNiQu75SR1hmZVEUIr9sH3lhNIY-jKmXSeqOw9rli7oWrAQ3Mk0d8WyZpdtz0yVMMTAThArW-mC0H8Ig3fFeiJXXRhNFP1o5XyuWtDqdKQMZ5z3PjXi-cM5qq4s65M97NS6ABo1ud2sEYtHBmfzoL4d48JB-9Z8xU2GdntB7SER7ylTwb-Dpappi2A1FRkz4OTO72iRzUVxFS9UK9JJ-a728N4A78tupK8xzl90Ilp4p6svrf1cpOCEsMeiuuFX5lqCNRir_iupDn_z-oUWLlh_obvxeX38oCSWDo2fzJhglW0ZaqT7EHnymdunTPWhxHEdWHQ_Y_Xo10VIDrrpeh3KuCqTzRiYlt1PMYaUYqxB4gP0gVa_5WZOWMgr6W7GttH0ZAUbGJG3biEo8K5eZGOMWIWhwb2dBEDGtC0YtBx72mU-m4Yi-5MZSxFWU57-kbHCZ7vSBRXw24-o8UaGBi9P5AjUYtRDMi7ZizU1RwpgWamugkxKK4nTayRPozlwu2sOm-xWQdVhDa8UVn-ZTK6s14nQzltfxU_2OyeJ_KD2MTlV74vBviKDxpw5ERMw5UtZjlGEu7HQRcB-q36e1F0CYV0AHjHW64" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43b9e87bfd.mp4?token=aaTvomlpOVe3HKmI5AMrdVi4YiMc7dp5w4C0mDgETscgz_PJwhbH9kwWA5beFv48y5f1zCUQH1yNiQu75SR1hmZVEUIr9sH3lhNIY-jKmXSeqOw9rli7oWrAQ3Mk0d8WyZpdtz0yVMMTAThArW-mC0H8Ig3fFeiJXXRhNFP1o5XyuWtDqdKQMZ5z3PjXi-cM5qq4s65M97NS6ABo1ud2sEYtHBmfzoL4d48JB-9Z8xU2GdntB7SER7ylTwb-Dpappi2A1FRkz4OTO72iRzUVxFS9UK9JJ-a728N4A78tupK8xzl90Ilp4p6svrf1cpOCEsMeiuuFX5lqCNRir_iupDn_z-oUWLlh_obvxeX38oCSWDo2fzJhglW0ZaqT7EHnymdunTPWhxHEdWHQ_Y_Xo10VIDrrpeh3KuCqTzRiYlt1PMYaUYqxB4gP0gVa_5WZOWMgr6W7GttH0ZAUbGJG3biEo8K5eZGOMWIWhwb2dBEDGtC0YtBx72mU-m4Yi-5MZSxFWU57-kbHCZ7vSBRXw24-o8UaGBi9P5AjUYtRDMi7ZizU1RwpgWamugkxKK4nTayRPozlwu2sOm-xWQdVhDa8UVn-ZTK6s14nQzltfxU_2OyeJ_KD2MTlV74vBviKDxpw5ERMw5UtZjlGEu7HQRcB-q36e1F0CYV0AHjHW64" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ۱۰۰ تاریخ‌سازی حافظان سنگر خیابان در قزوین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/farsna/440818" target="_blank">📅 23:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440817">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa9f4bca8.mp4?token=QvO1c9AqmdYgveR4dDwmfzo900Xp5Le35iZwsUajdZWaxmgWfmLk4lNxSM_3kuxK_tUPClzoS_Qrvw98-xzFDWouPFQLoepGaR4DkG-6dK7zas2TLoQvlhzjrhJuOiQEp-lS7cXeEhqLh84Rbgw1fblKB3iSVzVYC5rgjasppm-z8lL7cqP74fdHzXR8RJp6ufHtrHC1Izg5-cJYhSIZgRXBE_LMBIGtpFgdNVI3Tha7se55kC2Gzb7T9zJkWsSUoR_gOsbWhjk6Y-rMrejjMbwo3Q_IT_GpKv6BbZaPfwLaNo6OfAZQNMiqXbmRVZcDv97Pl35jFt2i-4Ga5YSjvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa9f4bca8.mp4?token=QvO1c9AqmdYgveR4dDwmfzo900Xp5Le35iZwsUajdZWaxmgWfmLk4lNxSM_3kuxK_tUPClzoS_Qrvw98-xzFDWouPFQLoepGaR4DkG-6dK7zas2TLoQvlhzjrhJuOiQEp-lS7cXeEhqLh84Rbgw1fblKB3iSVzVYC5rgjasppm-z8lL7cqP74fdHzXR8RJp6ufHtrHC1Izg5-cJYhSIZgRXBE_LMBIGtpFgdNVI3Tha7se55kC2Gzb7T9zJkWsSUoR_gOsbWhjk6Y-rMrejjMbwo3Q_IT_GpKv6BbZaPfwLaNo6OfAZQNMiqXbmRVZcDv97Pl35jFt2i-4Ga5YSjvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدمین شب اجتماع مردم اردبیل با این حال‌وهوا برگزار شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/farsna/440817" target="_blank">📅 23:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440816">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGH-bm9lkXRO_hFzA2D-KI0l5MQY3Fjyb4whakd5iba4zT1o5QTnGILFEAsjRcfrjUw6frIAMiaGQ4k-zN-D7xVq-9asC9HOud_kKtDqoSjRUlSy0AQGn31eKZPqG9f0DXKcp1dnxsI5Z5fwpM6Ep2Pht7AR93AxXEUNVRNnCQXZGz9LiURyEIbwZ-Du7246S1MwjO8Bp7KiUF2PNF_N_EGbvqu-pt-D19EUsNqjiE5Z_Mj2eQAEc4xRuJA-k32bE4ZL64hxb7gSNNNE70xqctvCsKtIdl45GJWPMnTVsJ31DXk4u9_csUCnCG9XIECxU5PbA2WxnldmcPci6ae0eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بازخوانی صحبت‌های رهبر انقلاب دربارۀ تهدید به گشودن جبهه‌های جدید به روی دشمن بنابر مصالح
@Farsna</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/farsna/440816" target="_blank">📅 23:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440815">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0569e1cb09.mp4?token=YwjS4imv6WjDBrnUBDbuVCg25cLIBnA3dq4aNzL9vB37quVp0FWAQWA4w9E54pg9Q44sJXjEvLcRA9_SBfLYFtkNtKwg1TJnPWEZDtj6FUZEP6vdOMrSaLUudHvBihJqW3odo1q5X6DFT-QlFwunsApGovLo8GYbKeHYZWpNVdBO4RqcOiZKO7JrHxlvpt2gfXyv9GDbILPlJWscEsg3kHBSdPf1vk1khPGMPoqnGljo5jDkZ8px-OiqPkYcyFjJ8N9t877WIZEXLmZEStdlinybAfAupyT03NqHmhcPdas3n0NY50romEfm8O2pETdStHAUhk-dIYmsSsFnwPWzqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0569e1cb09.mp4?token=YwjS4imv6WjDBrnUBDbuVCg25cLIBnA3dq4aNzL9vB37quVp0FWAQWA4w9E54pg9Q44sJXjEvLcRA9_SBfLYFtkNtKwg1TJnPWEZDtj6FUZEP6vdOMrSaLUudHvBihJqW3odo1q5X6DFT-QlFwunsApGovLo8GYbKeHYZWpNVdBO4RqcOiZKO7JrHxlvpt2gfXyv9GDbILPlJWscEsg3kHBSdPf1vk1khPGMPoqnGljo5jDkZ8px-OiqPkYcyFjJ8N9t877WIZEXLmZEStdlinybAfAupyT03NqHmhcPdas3n0NY50romEfm8O2pETdStHAUhk-dIYmsSsFnwPWzqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جبهه‌های جدید در انتظار تداوم اقدامات خصمانه  آمریکا و رژیم صهیونیستی
🔹
سردار سنایی‌راد، معاون سیاسی دفتر عقیدتی ـ سیاسی فرمانده کل قوا: رژیم صهیونیستی و آمریکا اگر بخواهند دست به اقداماتی بزنند که در جهت توسعه تنش باشد، قطعاً ایران و متحدانش از امکان و اراده لازم برای گشودن جبهه‌های جدید برخوردار هستند.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/farsna/440815" target="_blank">📅 22:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440814">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">تحریم‌های اتحادیه اروپا علیه سپاه پاسداران
🔹
اتحادیه اروپا روز دوشنبه تحریم‌هایی را علیه دو شهروند ایرانی و یک واحد از سپاه پاسداران انقلاب اسلامی اعمال کرد.
🔸
این تحریم‌ها فرماندهی استانی نیروی دریایی سپاه در هرمزگان، همچنین محمد اکبرزاده، معاون سیاسی نیروی دریایی سپاه، و حمید حسینی، نماینده اتحادیه صادرکنندگان نفت، گاز و محصولات پتروشیمی ایران را هدف قرار داده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/farsna/440814" target="_blank">📅 22:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440812">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04e2d911ca.mp4?token=pubeNtJM_u33Bc_r1pCtIE9rEkQavyuM-xfqkvfolwPZXjWq1fRATPl1DZlHBI8Ajxfwatd5BM1OlfyyGpXNy_oSDzX1G9rNDvCLUVlfOT12n4VjLYQssxZNb_CXBbh85tKdkHa-j6yGGUtZroQjNn1yTvyG8o-J2h68KtY6cByEEd6ie1EhrxRtRemKgXu0iup2n902CnKcYF9XwTxB3slzjmvxinj5Wn55b2THbrS2nmITdEbIeOUZy6e6Okx3eq1a30FkFsNfn9l_MIv6cECZ_V0Ef-1FXAAxW1wKGz9RRCfz1GWSKe6L43pDKcVVnFSEVNyhykkbcGD6ZdaFfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04e2d911ca.mp4?token=pubeNtJM_u33Bc_r1pCtIE9rEkQavyuM-xfqkvfolwPZXjWq1fRATPl1DZlHBI8Ajxfwatd5BM1OlfyyGpXNy_oSDzX1G9rNDvCLUVlfOT12n4VjLYQssxZNb_CXBbh85tKdkHa-j6yGGUtZroQjNn1yTvyG8o-J2h68KtY6cByEEd6ie1EhrxRtRemKgXu0iup2n902CnKcYF9XwTxB3slzjmvxinj5Wn55b2THbrS2nmITdEbIeOUZy6e6Okx3eq1a30FkFsNfn9l_MIv6cECZ_V0Ef-1FXAAxW1wKGz9RRCfz1GWSKe6L43pDKcVVnFSEVNyhykkbcGD6ZdaFfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظهٔ اصابت موشک ایران به پایگاه رامات دیوید در اراضی اشغالی   @Farsna</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/farsna/440812" target="_blank">📅 22:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440810">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-text">واکنش قاطع در ۲۴ ساعت؛ روایت ایران از هم‌افزایی میدان، خیابان و دیپلماسی
🔹
درحالی‌که تحولات منطقه همچنان در کانون توجه افکار عمومی قرار دارد، دو رخداد مهم در ۲۴ ساعت گذشته بار دیگر بحث درباره نحوه مواجهه ایران با تحولات جاری و نسبت میان میدان، دیپلماسی و افکار عمومی را پررنگ کرده است.
🔹
نخستین رخداد به واکنش ایران پس از اقدام اخیر رژیم صهیونیستی بازمی‌گردد. پس از آنکه تل‌آویو دست به اقدامی زد که از سوی مقامات ایرانی عبور از خطوط قرمز تلقی شد، پاسخ نظامی ایران در فاصله‌ای کوتاه انجام گرفت.
🔹
این واکنش از سوی برخی ناظران به‌عنوان نشانه‌ای از شناخت دقیق ساختار تصمیم‌گیری کشور نسبت به ماهیت تقابل با رژیم صهیونیستی و حامیان آن ارزیابی می‌شود؛ رویکردی که در آن، تقابل نظامی و دیپلماتیک دو مسیر جداگانه تلقی نمی‌شوند، بلکه در امتداد یک راهبرد واحد تعریف می‌شوند.
🔹
دومین رخداد، انتشار پیام تصویری سید مجید موسوی، فرمانده نیروی هوافضای سپاه بود.
🔹
او در این پیام بر هم‌افزایی سه عرصه «میدان، خیابان و دیپلماسی» تأکید کرد. این موضوع پس از آن نیز از سوی محمدباقر قالیباف تکرار شد. تأکید همزمان مسئولان بر این سه‌گانه، از نگاه برخی تحلیلگران نشان‌دهنده انسجام میان حوزه‌های نظامی، سیاسی و اجتماعی در شرایط کنونی است.
🔹
در این میان، بخشی از افکار عمومی و کارشناسان با توجه به تجربه مذاکرات گذشته و سابقه رفتارهای آمریکا، نگرانی‌هایی درباره روند تحولات دارند.
🔹
کارشناسان معتقدند اصل این نگرانی‌ها، تا زمانی که در چارچوب پرسشگری و مطالبه‌گری مطرح شود، امری طبیعی و قابل فهم است؛ به‌ویژه در شرایطی که افکار عمومی انتظار دریافت توضیحات و اطلاعات به‌هنگام از سوی مسئولان را دارد.
🔹
در عین حال صاحب‌نظران میان «نگرانی و مطالبه‌گری» با «القای بی‌اعتمادی و ناامیدی» تفاوت قائل هستند و معتقدند تضعیف هر یک از اضلاع میدان، دیپلماسی یا پشتوانه اجتماعی می‌تواند بر انسجام ملی در شرایط حساس تأثیر بگذارد.
🔹
به باور تحلیلگران، یکی از مهم‌ترین چالش‌های امروز، مدیریت همزمان دو جبهه دیپلماسی و رسانه‌ای است. در چنین فضایی، اطلاع‌رسانی دقیق و به‌موقع می‌تواند از شکل‌گیری ابهام و گسترش روایت‌های ناامیدکننده جلوگیری کند و در مقابل، تفکیک نقد و نگرانی‌های مشروع از تلاش‌های هدفمند برای تخریب سرمایه اجتماعی، نیازمند دقت و هوشمندی بیشتری از سوی رسانه‌ها و افکار عمومی است.
@Fars_Plus
-
Link</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/farsna/440810" target="_blank">📅 22:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440809">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c54db1a816.mp4?token=d2uwLJW4vjocUojjAaDbST3gv2h28hluyA1pRtSs_BtK4pf7CxhqHgg5HiN6CIa7r4pl7xxCLADIaR7vxKEeZGtbga-eMEJwJkcqtEVPwz6OLvDTmDqdgKfUshegjI8vS45AfZ3WxsWgJS11nyRNwn9o6tFp_OZM8RXGFqB17YfHf4INSEi0ddVpnvJcXmUpqSdEZIQM-32cGDlwwei__u4Tyn4XzRzLWQaaW1cqIoCUC7L7Vk5TvPZUTljcEr1odSDQiBu4KrAdUifFHrK-v_sFq_57gVh2KaJub7HBv1osNSqTyESeX3Qmn2hzj7192g3Lt_h-gxPDFOiZv5_GFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c54db1a816.mp4?token=d2uwLJW4vjocUojjAaDbST3gv2h28hluyA1pRtSs_BtK4pf7CxhqHgg5HiN6CIa7r4pl7xxCLADIaR7vxKEeZGtbga-eMEJwJkcqtEVPwz6OLvDTmDqdgKfUshegjI8vS45AfZ3WxsWgJS11nyRNwn9o6tFp_OZM8RXGFqB17YfHf4INSEi0ddVpnvJcXmUpqSdEZIQM-32cGDlwwei__u4Tyn4XzRzLWQaaW1cqIoCUC7L7Vk5TvPZUTljcEr1odSDQiBu4KrAdUifFHrK-v_sFq_57gVh2KaJub7HBv1osNSqTyESeX3Qmn2hzj7192g3Lt_h-gxPDFOiZv5_GFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار در مقر عناصر ضدایرانی در اربیل
🔹
منابع عراقی از وقوع انفجار در یکی از مقرهای گروه‌های تجزیه‌طلب و ضدایرانی در منطقه «سوران» واقع در منطقه کردستان عراق خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/farsna/440809" target="_blank">📅 22:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440808">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHK_7kmOSXau844wWU2-XgGtrgFJhRz-1eiHd1LcUFgY9c82tzyTj7fPhESy-LIYs4HJoVZkkPaJHqIy1_UA-xY43D2BLA9k6EbbZLapg8z-ymfd_Cqo42_35YudC12y8UMS5QMTfl08rUVp-nGMi9JlY7Hn2U0Aqnx4S6GD34wPPszjN1ISKdDsBa44kUIh8rreMJV_ZCVa2m-feA-y5UMj_1_q4bn4039iSsPzncZe0zk-69NvbkExlMP0loWTQIyKP8cEHInwfDlaiElc9zOLklAJNO0kzxirls-QAp1ktjS2yQAWM_ulUcYQg9gBIXPtnxyNCJOiHRaxCxY8ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور لبنان: فعلاً قصد دیدار با نتانیاهو را ندارم
🔹
رئیس‌جمهور لبنان که در قبال تجاوزات رژیم صهیونیستی از جمله حملهٔ روز گذشته به ضاحیه بیروت مهر سکوت بر لب زده است، گفته که برای امضای توافق عدم حمله با اسرائیل مذاکره می‌کند.
🔹
جوزف عون که به‌دلیل تداوم حملات صهیونیست‌ها همزمان با مذاکرات مستقیم دولت لبنان، تحت فشار و انتقاد داخلی قرار دارد، به شبکهٔ سی‌ان‌ان گفت که پیش از دستیابی به توافق برای پایان دادن به جنگ، با نتانیاهو دیدار نخواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/farsna/440808" target="_blank">📅 22:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440807">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75ba9a2e68.mp4?token=jVVT9oxfFv8kChfiPqvpwSuuPWxjkd19dUTneoRrnlNI_jvD4fIe-WCputqcRLtIm56g1L-Nu9WcOHWCth3Yc222AgDxnr_WfNYd5jcIlxt1Yhe3QvOOXA78EvlxHXO0yuXWodjyHLvHJLPmxVHS5UQOhPF5sQepFbZzO1dP1hSIEeljLHr_rzZvDocjDBExUyWw12c0k5Z48q227ucL5B9XMjc5FUTW0r7NpkgIbLJCfGb7-TJYkfIsC5tMNQr3UKhNFZ_hJ1MzpDCbrMpKAqyAp6-r2paEzKMyXpSm7X-UpjV6J1-W0xE1vHYLynnYbpYAeXc88Wrm7y28lPtfdogD8M_dD5qWm1zolieDyaM_i_TX_mQEvVRUbTPRz0BSoab35B2UZBiClVfN2cuVZ0X3gKPw6C2w6Qmlfs4xaKR3z1S-XxOeicRfKAyoUb2qAQE7goPUlYi4AC8sOg4212IUqeWcRo6ahBdWhagoHfvZd782it6_sZhhjvMoTtYbLtA0zMjkfeOz6R-9g3cnR9e9Kwl6wN6b-2mtvsiiKNVbIcGUNJnJ9ybCibsucLwzeBpmJZ0OL8itHtNSkaF6MOWrmmuVLRS9IJKY9f7-RiI3nzELegKiTiyCnIzTZ4ahL20zyuMaVwBF7jbH9NM2iZTXOc7NqZNTmligupRe7BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75ba9a2e68.mp4?token=jVVT9oxfFv8kChfiPqvpwSuuPWxjkd19dUTneoRrnlNI_jvD4fIe-WCputqcRLtIm56g1L-Nu9WcOHWCth3Yc222AgDxnr_WfNYd5jcIlxt1Yhe3QvOOXA78EvlxHXO0yuXWodjyHLvHJLPmxVHS5UQOhPF5sQepFbZzO1dP1hSIEeljLHr_rzZvDocjDBExUyWw12c0k5Z48q227ucL5B9XMjc5FUTW0r7NpkgIbLJCfGb7-TJYkfIsC5tMNQr3UKhNFZ_hJ1MzpDCbrMpKAqyAp6-r2paEzKMyXpSm7X-UpjV6J1-W0xE1vHYLynnYbpYAeXc88Wrm7y28lPtfdogD8M_dD5qWm1zolieDyaM_i_TX_mQEvVRUbTPRz0BSoab35B2UZBiClVfN2cuVZ0X3gKPw6C2w6Qmlfs4xaKR3z1S-XxOeicRfKAyoUb2qAQE7goPUlYi4AC8sOg4212IUqeWcRo6ahBdWhagoHfvZd782it6_sZhhjvMoTtYbLtA0zMjkfeOz6R-9g3cnR9e9Kwl6wN6b-2mtvsiiKNVbIcGUNJnJ9ybCibsucLwzeBpmJZ0OL8itHtNSkaF6MOWrmmuVLRS9IJKY9f7-RiI3nzELegKiTiyCnIzTZ4ahL20zyuMaVwBF7jbH9NM2iZTXOc7NqZNTmligupRe7BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ حملۀ موشکی یمن به اراضی اشغالی
🔹
ارتش رژیم صهیونیستی: ما شلیک موشکی از یمن به سمت اسرائیل را شناسایی کردیم و سیستم‌های دفاعی در حال رهگیری آن هستند. @Farsna</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/farsna/440807" target="_blank">📅 22:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440806">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">چرا جنگنده‌های اسرائیل وارد آسمان ایران نشدند
🔹
پس از حملات رژیم صهیونیستی به ضاحیۀ جنوبی بیروت و پاسخ موشکی و پهپادی ایران، اسرائیل چند سایت راداری را هدف قرار داد اما به‌گفتۀ منابع مطلع، جنگنده‌های این رژیم در این عملیات‌ها بدون ورود به آسمان ایران و از خارج از مرزهای کشور اقدام به شلیک تسلیحات دورایستا کرده‌اند.
🔹
تحلیلگران نظامی این تغییر الگو را نشانه‌ای از افزایش ریسک ورود مستقیم جنگنده‌های دشمن به حریم هوایی ایران ارزیابی می‌کنند.
🔹
البته این اقدام با پاسخ سریع ایران همراه شد و سپاه پاسداران پایگاه‌های تل‌نوف و نواتیم را هدف حملات موشکی خود قرار داد.
🔹
پس از آتش‌بس ۱۹ فروردین، شبکۀ یکپارچۀ پدافند هوایی کشور با بازسازی، تقویت سامانه‌های راداری و افزایش هماهنگی میان مراکز کشف، فرماندهی و آتش، به سطح بالاتری از آمادگی عملیاتی رسیده است.
🔹
در جریان جنگ ۴۰ روزۀ رمضان نیز پدافند هوایی ایران بیش از ۲۰۰ هدف متخاصم شامل جنگنده، موشک کروز و پهپاد را رهگیری و منهدم کرده است.
🔹
کارشناسان معتقدند علاوه بر توان دفاعی، قابلیت بازسازی سریع سامانه‌های آسیب‌دیده نیز به یکی از مؤلفه‌های مهم بازدارندگی جمهوری اسلامی ایران تبدیل شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/farsna/440806" target="_blank">📅 22:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440805">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8932184e58.mp4?token=pLad6ufV8-YrgSOklIvTkIhQEUGQx-k7ZH2IUxKImkMcY-gVcOQ4cUgNfv5JUham3DjO0lc19Fm5hHIYIoun53LYw-qWaza5NiBLdIGgdtopYnfYMujWImzf31X8hg9wNzrSML_nc30Yln-MKzCZYkuHLSSn1u_LYvU753Nlr9A8zAO0QU53eNS_YM6c8xzFncqgJ6MNgoypQMoybQvPTKVhFuOqid4slk8DL-yRzkiY-5P9uZGPLAdRhlZU6-ALvFkGYbjaJOCTtQVjdfkEkkwCzrPSbFG0yjKOXJW-537U_uu9pC6FulOk4-W1VS1a7YF6V02X8Fzj0xLvjlGtpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8932184e58.mp4?token=pLad6ufV8-YrgSOklIvTkIhQEUGQx-k7ZH2IUxKImkMcY-gVcOQ4cUgNfv5JUham3DjO0lc19Fm5hHIYIoun53LYw-qWaza5NiBLdIGgdtopYnfYMujWImzf31X8hg9wNzrSML_nc30Yln-MKzCZYkuHLSSn1u_LYvU753Nlr9A8zAO0QU53eNS_YM6c8xzFncqgJ6MNgoypQMoybQvPTKVhFuOqid4slk8DL-yRzkiY-5P9uZGPLAdRhlZU6-ALvFkGYbjaJOCTtQVjdfkEkkwCzrPSbFG0yjKOXJW-537U_uu9pC6FulOk4-W1VS1a7YF6V02X8Fzj0xLvjlGtpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازیکن آمریکایی استقلال در ایران ماند و ازدواج کرد
🔹
تاجرنیا، مدیرعامل استقلال: بازیکن آمریکایی ما در تمامی طول جنگ تحمیلی ایران با کشور خودش در ایران ماند و اینجا ازدواج کرد و قرار است همیشه اینجا بماند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/farsna/440805" target="_blank">📅 22:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440799">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f36use2-ROLD4ZwqoZuxd55wudnhxF10XYWS7AKTWkMfOHYbMAEGzag4SA4k93l9aKm7pT8acl1v3GIdFBZy6Jzi6zKjuYGqhz9F2ObTprvyv7fcofKxCsnia256z4TS1aCQQ46HEBRjl8Hiy5Tm21u_43AVOEvFgPcbbH7Tyx3E4YcCDJIcsL2ftxnH4xexKobkhUpcjYxb26yUt7bHVDo4JVrRw_anrQsGw7hZIwfvh7UxiPGD5zIiO6IfsnQAXMLv7iKbJtthAQRQn5yyRkzvd-OKwQXsn5SpqltxqzdngySkaYeeyFF3Tu5BDBYkUZJnj_HSKWVh6699RTX1yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UznnyaQNgML52Z1dv_fWOBPTvvqT5socUVkVtBCtghZApEas0kBzzgwjq05wXd-3trdw5z8U2ptxpfZ8RF58Tm_YArJ_irlMtNc8Ol8uPYEfSbc1pB82Rw67HVwawEsIyDM1iBytvxaHuXW7yNOXof-OaLZ2FAd5jVOSBTgtCXBqB1VJsAFYo7rMVL2AHAVaKOA3aADIruU5v7RoDW0wa9cJKCN2DHgY6QcYEcP9iUqAjMZTV4yiSzT3FPbzdZ8SVJlCns0uKM6vp8oS6g9PvC6qB7xEYYITXXbJNyd6-UyB_hdUQ742xu_4jOCEd3bEXlT6JhMDXQaCT-IzHt7T9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/abLh9jZYzIpdfftzBCyL421yH_Bx7ZUX8UJMIpKnhU5bgqIFszfbESbYuYB0_682_OElgBwJZsFTGkZI0E-kw5doiiZOXudtX5_6D3OetWcNn183fqFpGlSO6MxNFWA43a-SkYnr4QoRiWbluoOTVFTV1m1FfPwdvIrVJAzIVK5H5rE6b_YBdrfkVY5xalZcddudcCAD1gOZeVvPMLnMyp-XO5nj-FEFRip9D9dVSUBuF7nWSs0gMDbnQQc1bwhsPduz3l5zMr5I04hxXFwxCcnQwKMZhrwDChOkkUGuJ3dtNKpj6zODMpzSvA9gScmvwk2RQTH6Mdk39_DskXcusA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UWPTYgJn9B9ARxfYUd0urPiPaoGngHn9b6FmD_3TP_Y1VFouxZLj8bmADiuScIB1rs6lgW9IMx_9tq__leqYHoJ4Y5xhKUxmijjB4tweK4YvKNeY_xo70lqME5Ns0FRyhzQkVrthataGJzF8Oc8jgQjKW5caOT1fAaz9f0LS9c1E3n5GB6rzMpIJtaPqNf1UwA1qR2Ozuo0cCueg-rdiiVSMzplsfPfvLdiGejXR5uekFhg_2oFjbHb1XzLcQ3ivMbSAiFd2gmHkWFv7X0PWBjhsfexiQysOuBAFAAJnkkW_fJL1Wfs4jhdArmB5Rux5eAHA2LdP0X3aroOLH4NeBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C_mzO7nRBZd-0TYtI6vlbJT1RzCEvIiqCggKp6SzfqGdtKZ3CTh67KkKoSiRs662lI6Z2rKU-Cv8hlxbhg63mNb1uWiAMealSaaGWFJ_WFrbRx7H877iFJyTyKxjoTLBjBTPEdWDrjxZF8bzcr6DkDKcQDfijPaOsB9AwbivUrOVICn1sfl8mDh3YiRZsruc6j7G5ixuY9f6CqprPzZzZmkLAmZaMgyuNnjq845jvPO49NgmY_fMSXUPEpWsPE_oUNh5f4f3DgWxUFE9vmqkqHATELh-8sJrDf_0IIGhDTK3GirNHBBvwhl_S40jj4rDZ0hEtwkgt3yoQIEN4LGGOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fFUZxJEhAByJ03a0lUcaPA6ZIU2kbigT5WWbuq0hTQ1fGGmRhNyuQbxr3dauaK--2pmhLQJGX2D9p1vOY-kjgB-qbVSWSz-6Y86-L-PyWaoyqd8QtxnFzKTxponQoODbEDTZ9ZpNzOjqGfGEQ1p9AaFYJGU9cIdL_xZv08Ype6yHj4r_QT03HFpTbItjpHYlZ_Zfj-sPHl4CvOYaM4JeEOicHRAmc0OLUyWFLzJJF73jRZu17BIXVSOL0zawzJC9OJqHox6nEPOLgLWwI5ryvTd33IMmPnayfdpBAeASaJtos2GcZ90v6NjzKyHFWrad-O6CD6U8bxvRxMe1tZJ4hQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نمایشگاه عکس «تهران، خط مقدم مقاومت»
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/farsna/440799" target="_blank">📅 22:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440798">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fef4612464.mp4?token=pyAs-tbbxRdYUqed53CMLeWruNDY59hIVPLM7UxhYm5AbyaEyy9YTBUbvf-dwnrHFbGlJ5j0tkiNSTYGJTB25aYEXsooPr-rrAY0b-NFL6FU8kum0CzVSikh2C5wAez8gMPSS47NyhMmbBN8XIcIiwOpIK9G3XQpgusBuJA7pQy_B7IujxI2mxQQ1d4pW4JWFpZ4VCu26AmZ6kECnVZe64kO8tT1Wnigo965wz3mIpza1bCd-zzB0Vm30WBNpMZDi3K-pLGDWQNXQr8-FY-Nvt8AkwhnehXiTkLf6LkdFY3VpVCxmO6xlxgnm73qaQg6uscwLO7upWQGSu2t0sLMqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fef4612464.mp4?token=pyAs-tbbxRdYUqed53CMLeWruNDY59hIVPLM7UxhYm5AbyaEyy9YTBUbvf-dwnrHFbGlJ5j0tkiNSTYGJTB25aYEXsooPr-rrAY0b-NFL6FU8kum0CzVSikh2C5wAez8gMPSS47NyhMmbBN8XIcIiwOpIK9G3XQpgusBuJA7pQy_B7IujxI2mxQQ1d4pW4JWFpZ4VCu26AmZ6kECnVZe64kO8tT1Wnigo965wz3mIpza1bCd-zzB0Vm30WBNpMZDi3K-pLGDWQNXQr8-FY-Nvt8AkwhnehXiTkLf6LkdFY3VpVCxmO6xlxgnm73qaQg6uscwLO7upWQGSu2t0sLMqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عضو کمیسیون امنیت ملی مجلس: موشک‌های ایرانی به اهدافی اصابت کردند که بتوانند به حزب‌الله در جنگ کمک کنند.  @Farsna</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/440798" target="_blank">📅 22:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440797">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">Live stream started</div>
<div class="tg-footer"><a href="https://t.me/farsna/440797" target="_blank">📅 22:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440796">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f48eb8557.mp4?token=o9fry0RgqgtVybO1oSjGSkxfF63NKlk3CYjCL98DL1h5NLVIw0GVXIn3T69RiUhqhTy41TVxsqxgKD1Vp6IvP_G_Oy0KDKAgVGGqitC50240Vv1Pu43L76327ACMRfXdZ77JW-Yprtl7l6d90A9Lrr1oqjyODnFN0NZWN5leC9hxIespqjr0GqYhJ3i7vExjIWs7G76Gebd2mygjWu_BukBlxSzcq9wKRjSKcBRtO3wZHjdnRvM6GR5O55aX9qbdg9bERud8A6NDmV3al8-MshcLpuJbtonf9NfFN63Wn7TKz_hgfZtqsc5hX5RPKhK1RD-IEgW19ycCYUGculq4YB9Y0vGqQdiSXbhW5fxcJue_JbXPrNvPX85e6vNLElcm6zFJcMYkdA7oLrXgLS-nuBAgt3hH5X65_SDibp4YbolRFDOQepL6vbbndjUnJIXOjh4MrA0RxVNxbhN1tu9RsuozzJkZabvF-CFl1Ya3mZPzNiWT8p5f9t5sT9Pea39m2JuwLwg_VD-UqOcI--c8BPj38YT8ggN0p6tLtMW3QXg5dmLaC_W8VYzfQo9nApe1PgSlHOp58L4WbbrWlHtE6ykVmsHVUUVE5jegeEHQn0f-zC-Epd9RcEu5erbWmWOmn1Yy0EJyBhwB1GlhxLLu_3GKbVxMrjsw0s93zvXsQnY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f48eb8557.mp4?token=o9fry0RgqgtVybO1oSjGSkxfF63NKlk3CYjCL98DL1h5NLVIw0GVXIn3T69RiUhqhTy41TVxsqxgKD1Vp6IvP_G_Oy0KDKAgVGGqitC50240Vv1Pu43L76327ACMRfXdZ77JW-Yprtl7l6d90A9Lrr1oqjyODnFN0NZWN5leC9hxIespqjr0GqYhJ3i7vExjIWs7G76Gebd2mygjWu_BukBlxSzcq9wKRjSKcBRtO3wZHjdnRvM6GR5O55aX9qbdg9bERud8A6NDmV3al8-MshcLpuJbtonf9NfFN63Wn7TKz_hgfZtqsc5hX5RPKhK1RD-IEgW19ycCYUGculq4YB9Y0vGqQdiSXbhW5fxcJue_JbXPrNvPX85e6vNLElcm6zFJcMYkdA7oLrXgLS-nuBAgt3hH5X65_SDibp4YbolRFDOQepL6vbbndjUnJIXOjh4MrA0RxVNxbhN1tu9RsuozzJkZabvF-CFl1Ya3mZPzNiWT8p5f9t5sT9Pea39m2JuwLwg_VD-UqOcI--c8BPj38YT8ggN0p6tLtMW3QXg5dmLaC_W8VYzfQo9nApe1PgSlHOp58L4WbbrWlHtE6ykVmsHVUUVE5jegeEHQn0f-zC-Epd9RcEu5erbWmWOmn1Yy0EJyBhwB1GlhxLLu_3GKbVxMrjsw0s93zvXsQnY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
و باز "وَمَا النَّصْرُ إِلَّا مِنْ عِنْدِاللَّهِ الْعَزِيزِ الْحَكِيمِ" تکرار شد
🔸
این‌بار برای لبنان
@Farsna</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/440796" target="_blank">📅 22:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440795">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3aed63888.mp4?token=H7F8vQzj_K9Ro88fX6r66gB855pHZqb_4g3EE9oSW-aoSruxVDiHDxHiD-P4IYSOUq26EHcqIbnlOZFj7OUeFGIy2WJpjvLTmrPKsoW4j4xtnWpBkJyQOMnCr1RPUiOkkPcBb7xPw3qiqmbExRXNHgnWFstNnEG0S3GMuHhoujCD4cXJix4IBOGnuuyBpOYencS5GVQGh6wZXLOYlhagahv2E4g9wJXxVysGgEZx2DlFs061fAw7gCOfx4v4Mh8cAWH4rJolDUg4yIo30Nwzz_nPj2zFIZhpXMP3Lfu6-xRHCE3E93A5F0sDXYHaQdItiSH4q9y2T9FnC9axo3o4GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3aed63888.mp4?token=H7F8vQzj_K9Ro88fX6r66gB855pHZqb_4g3EE9oSW-aoSruxVDiHDxHiD-P4IYSOUq26EHcqIbnlOZFj7OUeFGIy2WJpjvLTmrPKsoW4j4xtnWpBkJyQOMnCr1RPUiOkkPcBb7xPw3qiqmbExRXNHgnWFstNnEG0S3GMuHhoujCD4cXJix4IBOGnuuyBpOYencS5GVQGh6wZXLOYlhagahv2E4g9wJXxVysGgEZx2DlFs061fAw7gCOfx4v4Mh8cAWH4rJolDUg4yIo30Nwzz_nPj2zFIZhpXMP3Lfu6-xRHCE3E93A5F0sDXYHaQdItiSH4q9y2T9FnC9axo3o4GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مشت‌های گره‌کرده؛ سندِ اقتدارِ لامرد فارس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/farsna/440795" target="_blank">📅 22:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440793">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4345ef7985.mp4?token=DxjAOCHLXq9OT-iHlV6czMItVM3HQcV1D85WlbX8szUXCk6KsmaQArJ4lMvIsJDTUFXheVV0KDn4Ob3kH2SYlUlIb5UWyZwZnRN6yUYHvA4CPbOyUp65rJb4-lVU4E-yeGTK3lZ3q0l2LQyhQwjPzsQ2ZchxICf6wglbOmQLMowCMRYabGv2_UZaHFMVTwf_iwjSjdo-9MStCD8qnY3Ian0RBp2dno1JahKBGoAXDnxFHwb-orDEaAbjZnz4Rbt7G1R3EL_0VXBrqM26eBturAmRkcnk8TR2hZo-YWTmlmyykeKaztlKATrYST2wxerz8s2i8-HWBwVodPsTT4EZiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4345ef7985.mp4?token=DxjAOCHLXq9OT-iHlV6czMItVM3HQcV1D85WlbX8szUXCk6KsmaQArJ4lMvIsJDTUFXheVV0KDn4Ob3kH2SYlUlIb5UWyZwZnRN6yUYHvA4CPbOyUp65rJb4-lVU4E-yeGTK3lZ3q0l2LQyhQwjPzsQ2ZchxICf6wglbOmQLMowCMRYabGv2_UZaHFMVTwf_iwjSjdo-9MStCD8qnY3Ian0RBp2dno1JahKBGoAXDnxFHwb-orDEaAbjZnz4Rbt7G1R3EL_0VXBrqM26eBturAmRkcnk8TR2hZo-YWTmlmyykeKaztlKATrYST2wxerz8s2i8-HWBwVodPsTT4EZiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بالاخره شب ۱۰۰ هم رسید...
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/440793" target="_blank">📅 22:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440792">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0ec953b5f.mp4?token=qsvbSxrxuE-29GafnGRNxJuEDnQqrMVc7zvO_mulyB-9-aNXCxHEE4maYCURH38sxwA4B0UCqWWOYtG7iOqAWdcUvVVN5UUa02n0fnDlkM53uNxH_x1ycr0s_ZVkMqlv1flOt62HpSkjU9u4ZClzv3v_iUABfWVJQhYnpaBf051iuvnPDdWL28BmpqUt_ytMAVTYBOMbtODLrbKwr9iNCLKqXbNEa9V9bq1vvEdIqBbVfSDw2f1q4b9W3HGrSi0Buz8LNhUQjaaWex42g2dhi7SRgpkwsJQJBg7oY50sTu55sUM9SVu5vrZzew3e8ZAaQ02W3aEb4X6Br_oVLsf9mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0ec953b5f.mp4?token=qsvbSxrxuE-29GafnGRNxJuEDnQqrMVc7zvO_mulyB-9-aNXCxHEE4maYCURH38sxwA4B0UCqWWOYtG7iOqAWdcUvVVN5UUa02n0fnDlkM53uNxH_x1ycr0s_ZVkMqlv1flOt62HpSkjU9u4ZClzv3v_iUABfWVJQhYnpaBf051iuvnPDdWL28BmpqUt_ytMAVTYBOMbtODLrbKwr9iNCLKqXbNEa9V9bq1vvEdIqBbVfSDw2f1q4b9W3HGrSi0Buz8LNhUQjaaWex42g2dhi7SRgpkwsJQJBg7oY50sTu55sUM9SVu5vrZzew3e8ZAaQ02W3aEb4X6Br_oVLsf9mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عضو کمیسیون امنیت ملی مجلس: موشک‌های ایرانی به اهدافی اصابت کردند که بتوانند به حزب‌الله در جنگ کمک کنند.
@Farsna</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farsna/440792" target="_blank">📅 22:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440791">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTgyanmnKet8BTiVyg6B2Nslo-T8nFBdkKdky-NxtYbB3yw8BKEuOjCj1uqsGpeQGDcpVDAPjANCZR0Y53hsf2St90nn9qesvwdTy_c5DzkjsGeG90_GRVxFL755H50EsFYhdJL39qchLG30p2uYqXTy38lymolwk9NtjRCPDdV32pcreO4ltDOY8vyDQPK49lDiW0jAEooRAFO8LLQ-Q6_FSyfYo2-P0dWGMgoK4YI8bG3Cb4wYybUEp4ID1GrT8FubwPE8BRPdrWotM1JLDMRT81VI8BHyW5jbB7JBwK3EX2M5aJnHqeaS1-y4DGVmab7tXcQBU0ZnnP_HZFU3fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚙
بانک صادرات به‌عنوان موتور تأمین مالی ایران جدید؛ از دانش‌بنیان تا محصول نهایی
🔹
سرپرست بانک صادرات ایران در بازدید از مجموعه دانش‌بنیان پارسا پلیمر شریف، مشارکت همه‌جانبه در پروژه‌های دانش‌بنیان تا رسیدن به محصول نهایی را محور اصلی همکاری‌های دوجانبه اعلام کرد و بر نقش این بانک به‌عنوان بانک پیشرو در نوسازی و بازسازی اقتصاد ایران و موتور تأمین مالی ایران جدید تأکید ورزید.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/farsna/440791" target="_blank">📅 21:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440790">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromماجرای جنگ؛ رسانه تاریخی سیاسی</strong></div>
<div class="tg-text">🔴
ماجرای جنگ۲
👤
به‌روایت جواد موگویی
📽
روایت هجدهم:
لامرد ۷۲۰k
نسخه باکیفیت را در
آپارات
ماجرا تماشا کنید.
🌐
@majaraa_media</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/farsna/440790" target="_blank">📅 21:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440789">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/farsna/440789" target="_blank">📅 21:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440788">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ba1ff455.mp4?token=RGPFiovhg-QvpD8zBkwUyVVryb9nZB8pI_aeQRhkmzElt6C_ifJU0Z0xyN_Dqi4jqpEnkk5DxLocH5yQc6gQE944uY01lilpBWlNJqo-3jGb-ihrHZ2OT4CHMUB9LFDqrhK6rSMXilVKHNyLru1HpWwkQvQlmNAUAOIMiJDH0-KfvOARGHEvbjj4GIil27goly7pv834eap_tGkJamku6Pe8Wr8o9SmezaWPOdsrGPGTisSL1vDrRP7s9ilR9lA6BvZofx5hcgK0JOA8XSJK_6vlATqot_TFQk-wsv4VBPQbQUtHxqtpExPztBK1b_ALRoerGDL_bJfXFcNc032zzgmiaUCGhgZCbfPiXeN0zSKp_ZxkLRV--xtxHF0fkkNOtHG38sCxCjgG6KPT5YT4l5uYXWG_Mv9MFB6ltWUhWcnjP39ncoqUnB3ACkKZ7gt7iF3qC4N7lLicIfICUbdRymdXeXpAkDtMPwnlaFrniDxVmiJY0LFk8Km90VYi5Q_mzpzBsFLVaZI1MHRnus7geBWBC3rZt0FfsdZIhvP9whWZVOpcUqZbBcnbe_gFDSILK6yuN7_PLw47KRlIz5UZYol9bHFcKAvNuglyTbjL7I5eckRxwYnf7R5kK9PoqMGowy5j6zticfY8XwMTLHm6oYklURYzzhngRgsSzMoMHPI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ba1ff455.mp4?token=RGPFiovhg-QvpD8zBkwUyVVryb9nZB8pI_aeQRhkmzElt6C_ifJU0Z0xyN_Dqi4jqpEnkk5DxLocH5yQc6gQE944uY01lilpBWlNJqo-3jGb-ihrHZ2OT4CHMUB9LFDqrhK6rSMXilVKHNyLru1HpWwkQvQlmNAUAOIMiJDH0-KfvOARGHEvbjj4GIil27goly7pv834eap_tGkJamku6Pe8Wr8o9SmezaWPOdsrGPGTisSL1vDrRP7s9ilR9lA6BvZofx5hcgK0JOA8XSJK_6vlATqot_TFQk-wsv4VBPQbQUtHxqtpExPztBK1b_ALRoerGDL_bJfXFcNc032zzgmiaUCGhgZCbfPiXeN0zSKp_ZxkLRV--xtxHF0fkkNOtHG38sCxCjgG6KPT5YT4l5uYXWG_Mv9MFB6ltWUhWcnjP39ncoqUnB3ACkKZ7gt7iF3qC4N7lLicIfICUbdRymdXeXpAkDtMPwnlaFrniDxVmiJY0LFk8Km90VYi5Q_mzpzBsFLVaZI1MHRnus7geBWBC3rZt0FfsdZIhvP9whWZVOpcUqZbBcnbe_gFDSILK6yuN7_PLw47KRlIz5UZYol9bHFcKAvNuglyTbjL7I5eckRxwYnf7R5kK9PoqMGowy5j6zticfY8XwMTLHm6oYklURYzzhngRgsSzMoMHPI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظه انهدام یک تانک مرکاوای اسرائیلی از دید پهپاد حزب‌الله در ظهر امروز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/farsna/440788" target="_blank">📅 21:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440787">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NkdnVVgKJcHtKyEY-WzWBW5fa8Fy3V5yDTpYhy1kAZPDTVKOZT6ntcZwlw6YczU-1HZip8NNy29-wIXmjD2MzjhJZWkubNNLIAIFR6Ifkq7qh7Sf-MjP8ukIVEUDIhqve8MVD77qPfL1_XGgThP_pSg-A-rLaASj3hoJN7-gCMZpHMTET7yxMlNbYhIJBIELLMvTc-CbwJd4MjIhp004R8TFmoyKCLnY_QY3I8rKsJ-n1n8QCnpKKKq9C1MTbm7t7r1-E9y2buJObb6JrN_V_Nqk5_ZH13fwxFpsRnzwMRYcDXIJxLgMe0LchiDsDggw7pI25byetyP5loM_p78E9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استان یزد فردا تعطیل شد
🔹
مدیرکل مدیریت بحران یزد: باتوجه‌به مصوبات کارگروه مدیریت شرایط اضطرار، غلظت بالای گردوغبار و افزایش شدید آلودگی هوا کلیه ادارات و بانک‌های استان یزد فردا تعطیل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/farsna/440787" target="_blank">📅 21:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440786">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2483b6ad7d.mp4?token=ho8jLyvJPbXZrVS3YyYxZcT4MpJOtEQT1Q56Fr_RfXVq6vlUsNBI0eeAGb6QrFJQ2jXwrznq0O_WHr7RFXy0Oe1jH-eaZ97tsWeZnkLJb_8S7BgJb5FhNXB9uuxFACrFYg2hMLrhUpRq3J0b-Qd2ArOcFogRfU0KgjoCGws1gjLIFaqxaC9hZGk5I5I1Fk1oNmX5IkTsL_N_P-bClhl9sIroULd0jJZpWlTgY_hI7jbRZnLBGLvxu38ZRX0xZf1Qlk4jSwnLvXu7nPKScx-PhNlDK7qB3WmIsauKWrueVK8ammChBydYC8UAYnyxegNtu1UvqjXEz0lX1oH_diVHSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2483b6ad7d.mp4?token=ho8jLyvJPbXZrVS3YyYxZcT4MpJOtEQT1Q56Fr_RfXVq6vlUsNBI0eeAGb6QrFJQ2jXwrznq0O_WHr7RFXy0Oe1jH-eaZ97tsWeZnkLJb_8S7BgJb5FhNXB9uuxFACrFYg2hMLrhUpRq3J0b-Qd2ArOcFogRfU0KgjoCGws1gjLIFaqxaC9hZGk5I5I1Fk1oNmX5IkTsL_N_P-bClhl9sIroULd0jJZpWlTgY_hI7jbRZnLBGLvxu38ZRX0xZf1Qlk4jSwnLvXu7nPKScx-PhNlDK7qB3WmIsauKWrueVK8ammChBydYC8UAYnyxegNtu1UvqjXEz0lX1oH_diVHSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدمین شب ایستادگی و مقاومت اهالی جنت‌آباد تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/440786" target="_blank">📅 21:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440785">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSNuWtjifYN4rWB1BsXq0sB1LHdocJAy5KajRtpL9LppgoQe4W9p_wFgpd25kJuTu8mYostxHVWYeqYmFtKftgihg-YPnRTmtmL8L9zALVg7EGVNv-xCdZoSvMUuHzPaXiG1ImWgZmDu9i_8hZzVbjb9zUPHyj3ZHF72yMA3pAdOLC5VHtQ8371mBCPpGD5rp5eiSi0-lHZ31oqyPlPMciFmL2GTJC-SrtDVfanlg_tqc1GAKutLCeXxBwi8Ukmc6K9kZ9GqbWtezi88Hy8FvgmfVHijBHdCNWbYHXuw2zRUnT8HqmwbbSEEtbqvlWph4_MZXVZmnYaULoDySF9grw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سردار قاآنی: از تنگه هرمز تا باب‌المندب و از خلیج فارس تا دریای سرخ کمربند امنیتی جدید مقاومت خواهد بود
🔹
شرارت‌های رژیم صهیونی و آمریکا در منطقه عکس‌العمل جبهه متحد مقاومت را درپی خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/440785" target="_blank">📅 21:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440784">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06f78a514.mp4?token=Dgnfwf2dRUhlB7NqbmekaU-H_kTBbQ5-bDOLEYjhrUssFEE2g5T532EICDKF81QlwtqFE9KU_utQc18tYDFr7VZANSZgN0j_37RoCpmt4_Wivc7I2lmyrf99lS87R-U2g4lsLUZBpfd7amGaEAkQDHqc5n_ISCpMpjXIHfYCJ80FkMQD4iT78i547WNntTo4WV5KD7jGrBCExxdpBZbGHVUKn7s4_BwdGlPNs11s5sKae0QOWHFqsifbivjuszGSVz9omlMET_kkRY6FYSKsfidT_EPRDDcQetbeYqZ7SHeWqyGK38HX5LrnGVtsvesKsWL5udszvpusno_ywYdMFHSVUOkuWUUdJHqv0NWUkuj_HYAJ-SaBDTdZ97ztqTDDS2FualKKUsvToMu5livkA5ZrZGRy7jgnBX6kj-QDemCm3aGbmzscHDCJ-WH_yFY5c1Bhtxhn9bnpFfrKEYP2iVQ8yL5G2N6xyFxqQhf0Kw5L3_yy2XfUoQ-qq8GxhxkfNpPeBr9OqZ-8ChV_dj3uK_0lDBT3dEeusNVYNoOtlVEHtvEl8NKA9pXFOX7on8Fz1zwKf7Z1r9sQ7lsP7VHAGm0aiPmSqL9JD9Cy1Vm99bbuGEbwXgCuvxzlcwUEV2P7jI4Evh2qgD2Uc40YhcgTiduk4uRuvYFTWK7kKVeIIbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06f78a514.mp4?token=Dgnfwf2dRUhlB7NqbmekaU-H_kTBbQ5-bDOLEYjhrUssFEE2g5T532EICDKF81QlwtqFE9KU_utQc18tYDFr7VZANSZgN0j_37RoCpmt4_Wivc7I2lmyrf99lS87R-U2g4lsLUZBpfd7amGaEAkQDHqc5n_ISCpMpjXIHfYCJ80FkMQD4iT78i547WNntTo4WV5KD7jGrBCExxdpBZbGHVUKn7s4_BwdGlPNs11s5sKae0QOWHFqsifbivjuszGSVz9omlMET_kkRY6FYSKsfidT_EPRDDcQetbeYqZ7SHeWqyGK38HX5LrnGVtsvesKsWL5udszvpusno_ywYdMFHSVUOkuWUUdJHqv0NWUkuj_HYAJ-SaBDTdZ97ztqTDDS2FualKKUsvToMu5livkA5ZrZGRy7jgnBX6kj-QDemCm3aGbmzscHDCJ-WH_yFY5c1Bhtxhn9bnpFfrKEYP2iVQ8yL5G2N6xyFxqQhf0Kw5L3_yy2XfUoQ-qq8GxhxkfNpPeBr9OqZ-8ChV_dj3uK_0lDBT3dEeusNVYNoOtlVEHtvEl8NKA9pXFOX7on8Fz1zwKf7Z1r9sQ7lsP7VHAGm0aiPmSqL9JD9Cy1Vm99bbuGEbwXgCuvxzlcwUEV2P7jI4Evh2qgD2Uc40YhcgTiduk4uRuvYFTWK7kKVeIIbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بعد از ۱۰۰ شب شما مردم بگویید...
@Farsna</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/farsna/440784" target="_blank">📅 21:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440783">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3LWwK49leNsM7ciOc2dptu8EatB4KQT81w2lyc4n1lohlkEJ5q9E0xW8tAvbeni2GJ1sSkJ9UrLPGU6xlN7TXJUXmle1E93PFefRdL8kKTfMaPB_037LWK1fGA-EHUxW1dXSp1SVN1QZwykQG93gYwa0KDv_SFXuqivOxhP4VpQVTZyEWzaOgS4odWx1IQhCG8du3afCyGpIa_QHkPsfwodt4info8GHHyY7LC02fsO4-kEQh4as6GHyYoZ0vYh0KDjLgjynaJ3Xtw8NHkLoMuJe_-YD5R_JdrvfFTLILaY5HuQJT7LdhQSLr6xFCuZoyCp8ddNCiffo6oSHThVQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروازهای حج به‌جای مشهد، مستقیم در تهران
فرود آمد
🔹
درپی بازگشت شرایط پروازی به روند عادی، ۳ پرواز بازگشت حجاج که قرار بود به مشهد منتقل شوند، ساعاتی قبل در فرودگاه امام خمینی(ره) تهران به زمین نشستند.
@Farsn
-
Link</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/440783" target="_blank">📅 21:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440782">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5A5Ntwz9mj3DyLRufMayRDkVJiJKHEKY3QCEckngB_z2LVduyp17LytmCVYyZPR-43bkWz7LfSyRvrOb7Xd2tqWVbwhgmts_8b8ySb-D1x74MnDp40hY1jQGjG90DrL_G4LAipwGmSQlJ701TO2Zg7DSdM22ayXsFdGmsHJgUStGu0sMUjYSLw-F0P28i4cTxE_D38dtwXXYN7ncw_p3Nb8nnAgKhxAiy_pP1HInxlttZQB7yOTUqGd56EZp8GxSj8NIob4R5lIxpjB8I7VF7OND2qxtN7oPsFIhwxj8UdeRcZE3w7JaFePR5hY6aMaSE5SMg6eNow-lf8Udy-PAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منبع امنیتی صهیونیست: تصور نمی‌کردیم ایران تهدیدش را عملی کند
🔹
روزنامهٔ اسرائیل هیوم به‌نقل از منابع امنیتی رژیم صهیونیستی گزارش داد که تل‌آویو انتظار نداشت ایران تهدید خود را عملی کند و به‌سرعت به حمله علیه ضاحیه بیروت پاسخ دهد.
🔹
به‌گفتهٔ این منابع، اکنون نگرانی اصلی اسرائیل شکل‌گیری یک معادله جدید بازدارندگی است؛ معادله‌ای که براساس آن، هر حمله به ضاحیه می‌تواند با شلیک موشک از ایران به سرزمین‌های اشغالی همراه شود.
🔹
این منابع اذعان کرده‌اند که واکنش سریع ایران باعث شد اسرائیل به‌جای گسترش درگیری، عقب‌نشینی کند و در نهایت به سمت آتش‌بس سوق داده شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/440782" target="_blank">📅 21:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440781">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‌
🔴
قالیباف: دست نیروهای مسلح ما هم برای اقدام همیشه باز است و براساس تدبیر و برنامه‌ریزی درست و تصمیم تصویب‌شده عمل می‌کنند. @Farsna</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/440781" target="_blank">📅 21:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440780">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‌ ‌
🔴
قالیباف: برخلاف تصور بعضی‌ها که فکر می‌کنند بین مسئولان هماهنگی نیست، هماهنگی کامل برای رسیدن به اهداف وجود دارد. @Farsna</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/440780" target="_blank">📅 21:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440779">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‌
🔴
قالیباف: ما در مقابل دشمنان ایران، ۴ میدان مبارزه داریم
🔸
۱. میدان مبارزه نظامی
🔸
۲. میدان مبارزه دیپلماسی
🔸
۳. میدان حضور مقاومت مردم
🔸
۴. میدان خدمت
🔹
سه میدان اولی، پشتیبانی می‌کند چهارمین میدان را. @Farsna</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/440779" target="_blank">📅 21:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440778">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‌
🔴
قالیباف: میدان نظامی موتور پیشرانِ قدرت‌ساز است و دشمن را از فکر حمله دور می‌کند
🔹
میدان دیپلماسی نیز باید در زمان مناسب، این اقتدار عینی را به دستاوردهای ملموس حقوقی، سیاسی و اقتصادی تبدیل کند. @Farsna</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/440778" target="_blank">📅 21:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440777">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‌
🔴
قالیباف: قرار نیست یا فقط جنگ کنیم و یا فقط مذاکره؛ بلکه قرار است به وقت خود جنگ کنیم و به وقت خود مذاکره کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/440777" target="_blank">📅 21:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440776">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‌
🔴
قالیباف: پیشرفت مذاکرات در کنار انجام عملیات‌های نظامی در خلیج فارس و موشک‌باران دیشب رژیم صهیونیستی نشان داد که ما باید درک کاملی از هندسهٔ میدان مبارزه داشته باشیم
🔹
ماجرای لبنان ثابت کرد که میدان دیپلماسی در کنار میدان نظامی می‌تواند دشمنان را عقب براند.…</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/440776" target="_blank">📅 21:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440775">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‌
🔴
قالیباف: اگر دیپلماسی را صرفا گفت‌وگو در اتاق‌های دربسته و لبخندهای دیپلماتیک بدانیم، از همان ابتدا شکست می‌خوریم
🔹
از طرف دیگر، اگر صرفاً به عملیات‌های نظامی و جنگ تکیه کنیم نیز نمی‌توانیم از حقوق خود به‌طور کامل دفاع کنیم. @Farsna</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/440775" target="_blank">📅 21:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440774">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‌
🔴
قالیباف: صحبت‌های رئیس‌جمهور آمریکا دربارهٔ یادداشت تفاهم، مخالف بخش‌های توافق شده بود که نشان داد آن‌ها نه دنبال آتش‌بس هستند و نه دنبال گفت‌وگو
🔹
باید برای دفاع از حقوق ملت ایران پاسخ قاطع می‌دادیم که به لطف الهی نیروهای مسلح ما با اقتدار به وظیفه خود…</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/440774" target="_blank">📅 21:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440773">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‌
🔴
قالیباف: ما نه می‌خواهیم با وادادگی پیش برویم و نه با شعارزدگی بلکه باید با اقتدار و عقلانیت ایرانی به‌دنبال یک پیروزی مهندسی شده باشیم. @Farsna</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/440773" target="_blank">📅 21:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440772">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‌
🔴
قالیباف: هدف مذاکرات پایان جنگ و ایجاد امنیت پایدار است، نه عادی‌سازی با آمریکا
🔹
به مردم عزیز اطمینان می دهم که با قدرت از حقوق مردم ایران دفاع می کنیم. @Farsna</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/440772" target="_blank">📅 21:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440771">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‌
🔴
قالیباف: نه دیپلماسی مانع عملیات نظامی است، نه عملیات مانع دیپلماسی
🔹
میدان نظامی، میدان دیپلماسی، میدان حضور مردم و میدان خدمت به مردم تار و پود یک پیکره واحد هستند. @Farsna</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/440771" target="_blank">📅 20:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440770">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7701fd0c2d.mp4?token=HJaRMvq-fFYTDtmhFmwC598fQuATXycLU57XeUcULx8et0rBHzZzlEcgg_9ElLvNG6i7YhmJ6lMfL0nUClPBkIuKLWfDobIjX8anCpGMR1kTkwjywPz9mdJp8D6CQmhg5sT7-FEdaw60CLRic2y1B05udZwp-rn5f1EphRnu4hOwWINeFd37uZURxrG338hevP2aOuEy_3TJ4hBjPNmDw1PJnJxysZ4iPOdsoHzzdyxEDhSnowxGpXJibFOzHyGtMdnzagcZPYtBtAX8i9j85uzTsC2m2s9dLpf8ByXZ5KH-cL2IBLBmFF8DV3oRqq0eENNkvGrQIAJDVAuV8VPwBaII4OqgtpBzRT_RGObuSN5zgMfRHsdvrMgx_z9Gz3p006xqKHWKZ9G8xpvpw2FMxIWiLKWxuTw_jmkVSEfYZnWMy0to52UG-lD62HWO4mO0BbLfTNk0HklW3E_c33-vQ08pfYNabyf6cVcTrhx3gSlkypRhuLOPx-00I8eOnof7WNKXGptPprtpv5TeOsSJ3CYUmZdXKXUqet-yMjNz3Yw4G_a1px0suoVakARmwYxg5Nq-1E9sHciOQUeZTIOliU0kYVKiWIadRn--EzyjT7PezPd9wx9wRaQzRT0y6x66CjQJD28ntL-pVGtsoX0LkYJzWjhVcAutlIiEwGCBnO8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7701fd0c2d.mp4?token=HJaRMvq-fFYTDtmhFmwC598fQuATXycLU57XeUcULx8et0rBHzZzlEcgg_9ElLvNG6i7YhmJ6lMfL0nUClPBkIuKLWfDobIjX8anCpGMR1kTkwjywPz9mdJp8D6CQmhg5sT7-FEdaw60CLRic2y1B05udZwp-rn5f1EphRnu4hOwWINeFd37uZURxrG338hevP2aOuEy_3TJ4hBjPNmDw1PJnJxysZ4iPOdsoHzzdyxEDhSnowxGpXJibFOzHyGtMdnzagcZPYtBtAX8i9j85uzTsC2m2s9dLpf8ByXZ5KH-cL2IBLBmFF8DV3oRqq0eENNkvGrQIAJDVAuV8VPwBaII4OqgtpBzRT_RGObuSN5zgMfRHsdvrMgx_z9Gz3p006xqKHWKZ9G8xpvpw2FMxIWiLKWxuTw_jmkVSEfYZnWMy0to52UG-lD62HWO4mO0BbLfTNk0HklW3E_c33-vQ08pfYNabyf6cVcTrhx3gSlkypRhuLOPx-00I8eOnof7WNKXGptPprtpv5TeOsSJ3CYUmZdXKXUqet-yMjNz3Yw4G_a1px0suoVakARmwYxg5Nq-1E9sHciOQUeZTIOliU0kYVKiWIadRn--EzyjT7PezPd9wx9wRaQzRT0y6x66CjQJD28ntL-pVGtsoX0LkYJzWjhVcAutlIiEwGCBnO8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیشرفته‌ترین سامانه‌ها هم نتوانستند مانع اصابت موشک‌های ایران شوند
@Farsna</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/440770" target="_blank">📅 20:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440769">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
قالیباف: نقض آتش‌بس و محاصرهٔ دریایی، علت تنش‌های اخیر بود.  @Farsna</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/farsna/440769" target="_blank">📅 20:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440768">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
قالیباف: نقض آتش‌بس و محاصرهٔ دریایی، علت تنش‌های اخیر بود.
@Farsna</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/farsna/440768" target="_blank">📅 20:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440767">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DW9ezrNIjojpcE9EqTd92KkTS8LNR6x-ZfXShx_TfzSOUMo95uWSEEPVqT1ERmjZYCymLwAHbMO_Ok4B43RTQ5v5NeUeiV5BeW_jouSgu7HDFtLOkMznARb11om3kgliY_h56IVh1t6YofwbQfXP5YmEWgvMCt-sx1wFehESoMRtmY3KFGEsSHP_HRZfL_GfX1hqo844mNSnjQPR2mW6MOi-HpLtbwvFEHxO3ThgV5c6-1QDKm1e_ZQ2LVrMlxEGicP2vzp0QpHpuX8YjhYTGRxSlG8GVzV4174tx_IqmNgOmjx2M9-y69dP0V0L9MR87XYES-gOJe1qXlO9Ir5gAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکست بزرگ در پروژهٔ نظامی اروپا
🔹
پروژهٔ مشترک ۱۰۰ میلیارد یورویی آلمان و فرانسه برای ساخت جنگندهٔ نسل ششم، پس از ماه‌ها اختلاف بر سر تقسیم کار و حقوق مالکیت فکری، رسماً متوقف شد.
🔹
این جنگنده قرار بود از سال ۲۰۴۰ جایگزین «رافال» و «یوروفایتر» و به نماد استقلال دفاعی اروپا تبدیل شود. با این حال، اختلاف میان شرکت‌های «داسو» و «ایرباس» باعث فروپاشی هستهٔ اصلی این طرح شد.
🔹
هرچند بخش‌هایی از این برنامه مانند توسعه «ابر رزمی» و سامانه‌های هماهنگی پهپادها ادامه خواهد یافت، اما تحلیلگران توقف پروژهٔ جنگنده را یک شکست تاریخی برای همکاری دفاعی اروپا و آرمان خودکفایی نظامی این قاره توصیف می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/440767" target="_blank">📅 20:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440760">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ncmoM78rfx0tXGuZTZqRepETuOiReW630R4V7pWMRlfA5VEgjhfHccDUvvGK1FXkkINFF3QWqfiule60TjDPJ-zai92B5eQB18DbzH-Ah8jpzeuShMCtOXfdTL-Tg4DpHuo0hfbCSI_IjPgyjdtD_CIFqLE6LzSxFbJeYHW_NLdYfeBtn86A61AlzghYM_zq_Ha8ZQnhuZK3lJ4obWqoZgN9rjs65RqM0xm-KJn4j2RLPfTxmJDKT1sblmzyVB9uPxlvkctv9uQDnVz3LRAuclJo0roQeji_UnZVYHP7IaBfkHiO0Q5oDYDiB93ns6OcOSVXoCDi2AwjTmkFC2Atqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oMWETf9Jpx8kFbZlxOmZJ4ZnKiHm4k3gO_gp-MlEOovi7ZpEaWARRw3mr9jK8vTNex8ZVWcFoww9NhoFnowYzd0aUxNw3EQ3WyP0NpM2HzDdkRhX6O981Q1VW_zuAIOIsOIQTWffpzQmhTTR6HKymmmgeTfcPFOR8sRWYCjtv-O161Y7EOmS3WKqH820BrZEhXoIYJB87n0b8I-qBDBiNZ5jc-utqpYiqZ4Rt_z53Nsy-bYCwxQjZWlKGc42IMPuDJDiFJD1FafIEtSgZaTLKloXA6AMrSdz-bICGwKG4KO4qTQf7XN9qIZGr_msf0VfLq3cZ8N1qp8FX4sqwqlnhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YUvKXNKdTJi-fJoR4NS2uwuwRDA2LSFKzujxjpOqx46i-G2o2pHvq64KnFAHnLE1wuqzKMcBmPDrCUIpA0Q_2ZoZ1kgyfIDoz1IVgswnrvtAxe-5MtgAcGPtD-s8GCWQ87IxOTvba8Caj1EI-EZGK6sTo908iXWj0S_opUKvvb0xXL2gkb4YQCMMAB8Gf5JyJfQU9JE567ZP-JYztUG6aFopf5UDIzJJ6EuD3swLKwlmbhBP_ESTJ1FN__uHiV8QHrIh2vDzKvMGob28wIVrEPkomY7AfJO_JC3rc9QXmpKMsz7Hmix41VZSNMs1SFFzVGHB6giVUR7rLOg2Hj7S2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P-JIHsNE5Bbw1wDiYQKR2iRfLrcok7ms40ulYLuOurt13LWTZoT5Y_ESDIxfMcqnF8pQMlZxAKyGfQ-G18hXRIt_FHVU2xMjy9leRdiRyMtl79zAh1z5jcN_9UjQG8HiBxukdf9QtPPwx_9tiqr4hT0BaPyQh7rF4AQ9NtJKi8NrHZQ1EFemV4lTQIJYGk3Cr8laq3kHbHkrPm2PpXW20jkNF20_HTts7_gBrBJAa9A5zZy01WbXKF8SaRkYAA6Z0q9uIz2XEx6zevgrhcUcJ3pwjZsBmhdYBEUOOtasr6DK3uElugau_qHkHRKecUP5wJs4Du0MYU0aBkfesHUIwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uctiMVVngr71-VLRiSj9v7_t-TfkdMEgumzVBr6XJ3eyedoOBfn6pV9eU44LULYWap7shA8_H08vQXNs_9c0X-0GdhhNQY6ON7t_XsqocMEFrzUJRdXwMFmH-e08bppU-xbrbfg83Qg-KHAoXMEZVlsOaNsm3ODAc5NXBPGmbTsce4qCnkQo_r7K_pdxfxXvZsPaXtTOt-c1BDuQ5MOmZX6JKnuAEIKQt3CJjK9fVepe4l5YAMME1bIg4-ksgvm3RFP7aaOnMR8U8VxMwmQGqMaFpWe_IDer_XbslgjI2FuskclX01Y_A6nUi8TXum1sOKvhkD_i0ejSsDdVW0YrXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IuyHb4NjK6oYBXlsklxzE4hq7U8zkHjcIUSJ5dBUIeROgVrRT7u4beGxp_ntqciEoJwZM92cn3RUEFbskMgaHg1b9YqBixxtzeb8Jr1Mpvfc_mvUOPe9rlGa9_brfUtLjylY6jHOfLyRz4GNyuEmZ2_GqwDVr_cE_2rpVw65ia9LJ-2zOw4ztelfymWMLI-DhajzEl3Wbje9lNytCK6RJSviwTl8tkJDW-wP-ztCZbsMsLy1Xz6jsc1l6L2gZXKEZND3NPTbYgxkq4V4Xw1-o4KP3kiEcdcHslqZHv2U-PRmzeNNVEhsowKUWFqpac139DlubeBP6W8p4KUd5cqJMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Moz519lcwLxoFhuWyUFWtcTCTcWTVUbEzVlOQzt0qaeN88qr-rzxqJukroD2UNR_dwzAwn0y-CjJNc6KvN_TH6pxi2gyJn11NNCsK2QDhGURPDhsgRzqg90PtnZnHOenNhzyjhgxNuX9pEWRytRWyxTQVvV2ie0s-f7WvZwBDplhNdS64XIsQA-GQ_1BRq_vE-sSTe0a2H1BpDt0m9a4L7uARLsIu9_IxDpZqT72kH-2Ds_aDYotTGVmpcisnevfN0HkSc2BRlI0jGU5aZyJAng4wc7f94YpJLp3-h51WKSgJsy8f1cd77mi1TmAB-VbRbOOSFhizdJTOhNaExIa0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: جام جهانی قطر بسیار منظم برگزار شد اما حالا به‌خاطر اقدامات آمریکا با یکی از سیاست‌زده‌ترین رویدادهای ورزشی مواجهیم
🔹
از مکزیک بابت میزبانی از تیم ملی فوتبال ایران متشکریم؛ اما تیم ایران هم باید مثل تیم‌های دیگر بدون تبعیض، فشار و استرس…</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/440760" target="_blank">📅 20:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440759">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIwCe4FvR5vnJBdZ7BzJjKLIaAYnuMe7ZPeDRko8XbLAJPUgdgmcwaaBaJ8UrFOWmmGtNwHVYqM3ULhUEKAzXuDfFUsZ6AeyKCPR4lZzq5wqOO8qfnL0nCJ81lu-7kbxNS3WL9NE8QM1NlEuhSwoK9gt7S92rdBxktfCbwmBYttUDdG_79VSsf2eVA-4VAtmtrmq6wt3DH4bc_xGsmKs9nNYzNyBIDrABzQuxbZ1EqitaQQlLYR0SqnsjGbm-oo_u_veoWVnn4qn3cYBAkco03gpVxYzAEjoyb0UvZIKSoB9BLjqM_0OLncF-vHoDoIWoBcFS689BczfjWPmSI4RuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
موشک‌های ایرانی به کدام نقاط اراضی اشغالی خوردند
@Farsna</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/440759" target="_blank">📅 20:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440758">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">هشدار روسیه به شهروندانش دربارهٔ سفر به اراضی اشغالی
🔹
سفارت روسیه در تل‌آویو برای شهروندان خود هشدار سفر صادر کرد و از آن‌ها خواست که به اراضی اشغالی سفر نکنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/440758" target="_blank">📅 20:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440757">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اسرائیل هیوم: آمریکا در حملۀ اسرائیل به ایران مشارکت داشته است
🔹
روزنامۀ صهیونیستی «اسرائیل هیوم» گزارش داد که آمریکا برخلاف برخی گزارش‌های رسانه‌ای، در جریان حملات اسرائیل به ایران و همچنین مقابله با حملات موشکی ایران به اسرائیل نقش پشتیبانی ایفا کرده است.
🔹
پیش‌تر شبکه CBS گزارش داده بود که ارتش آمریکا در حملات اولیه اسرائیل به ایران پس از آتش‌بس مشارکت نداشته و واشنگتن نیز دستوری برای دفاع از اسرائیل در برابر موشک‌های ایرانی صادر نکرده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/440757" target="_blank">📅 20:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440756">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nH9OWzjCU904yR12daVytAoato2ARQvAmYKQPU_yuGwriiUt8Vx_NEaxzS5wLHiuRqV9b-DVwez2i-iL-MlIrNDI8BgPoE9zqOrC247Cug2JPOap-RQd8_xd2xu2yDNktDioJcIzks4tS-vkHGlrMp3UYH4qL1hBBKI9SB4YNeiRtsu9FkJ58ej_fBpf1NG6rkiG33plM7u71sCsvFA6NQ2jYH02RnmaN0GDbIWtDAdVrLhoBHFFUTzvUooNT4sVYF0yxLZRBDIs11_vjNQi4QnpyvvUfyb04Xsyk48fJngEuxHs5yiIMRaXWmjyHhVqdgR7EfFJI8vJeEDkwZAdDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«سوپر ال‌نینو» امسال برای ایران بارش می‌آورد؟
🔹
مهدی زارع، پژوهشگر حوزۀ مخاطرات طبیعی: پدیدۀ «سوپر ال‌نینو» ممکن است اواخر پاییز و آذرماه امسال، شرایط بارشی متفاوتی را برای ایران رقم بزند.
🔹
براساس الگوهای تاریخی، سامانه‌های بارشی سودانی و مدیترانه‌ای همزمان با این پدیده می‌توانند موجب افزایش بارش‌ها در کشور شوند.
🔹
«سوپر ال‌نینو» یکی از قوی‌ترین نوسانات اقلیمی جهان است که با تغییر الگوهای دمایی و جریانات اقیانوس آرام، بر وضعیت آب‌وهوایی مناطق مختلف تأثیر می‌گذارد.
🔹
درحالی‌که این پدیده در برخی دوره‌های تاریخی با خشکسالی‌های شدید همراه بوده، پیش‌بینی‌ها حاکی از آن است که امسال برای ایران می‌تواند به شکل افزایش بارش و حتی بارندگی‌های سنگین ظاهر شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/440756" target="_blank">📅 20:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440755">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
سازمان عملیات تجارت دریایی انگلیس از وقوع حادثه برای یک کشتی در دریای عمان خبر داد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/440755" target="_blank">📅 20:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440754">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G17WZFlvyFhpzlvWqBx_PLvWbbvehCGrcT0LK3gNBN2EDU00iqNI2GWB0P8gZYv_71wO9Vd2c8W3jUgcalhbdB_YNH9ty5wrRqNrsZuJsEUE6Fa5pzL8U9ikmP2wbJFp8-VHgOk7jadQqkaksylF3ubZGpVkOsIWVeW3pD_movFcDOQB7qJhf7_4GJyUqvCINixaqs81tWn_KKLUKrS6Uy5PCWCDlwuj0GHXYMo_X4mvqdSL90pJKhJxhNSwYJh-9E68ePlUQXaNaDtAtBozsPOyJlknrGMkJ0cllAGb0FmoEcdEDX0W5QEncKrQki__4Ua6WYCKlGo5T7OTH2o7RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بهترین داور آفریقا را دیپورت کرد
🔹
در آستانۀ آغاز جام‌جهانی، حواشی مربوط به کارشکنی آمریکایی‌ها دربارۀ ورود برخی چهره‌ها همچنان ادامه دارد و در تازه‌ترین مورد عبدالقادر آرتان، یکی از مطرح‌ترین داوران فوتبال آفریقا، در بدو ورود به آمریکا با ممانعت مقامات مهاجرتی به ترکیه دیپورت شده است.
🔸
این اتفاق درحالی رخ‌داده که آرتان پیش‌تر در صفحه شخصی خود نسبت به کشتار مسلمانان در سومالی موضع‌گیری کرده بود.
🔸
این نخستین حاشیه مهاجرتی مرتبط با جام جهانی ۲۰۲۶ در آمریکا نیست و آمریکا پیش‌از این «ایمن حسین» مهاجم اول تیم ملی عراق را به محض ورود به آمریکا بازداشت کرده و مورد بازجویی قرار داده بود؛ همچنین طلال صلاح، عکاس عراقی هم از پوشش مسابقات منع و دیپورت شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/440754" target="_blank">📅 20:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440753">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‌
🔴
لغو تمامی پروازهای کشور تا اطلاع ثانوی
🔹
شرکت فرودگاه‌ها و ناوبری هوایی ایران در اطلاعیه‌ای از لغو تمامی پروازهای کشور تا اطلاع ثانوی خبر داد و از مسافران خواست که از مراجعه به فرودگاه‌ها خودداری کنند. @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/440753" target="_blank">📅 19:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440752">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGl9Tm9vM8jQFSKEtQ9EO7USmddTTS0l_cX5PBzHF4w9nWL2dPA01PJtDnqnTxW5DfNtuUaCCc-c1KmzX7vjojT_8FihFDBlFDBnJlp-_Q3nLDwziWFPvIdTZ73lPRVD-0OjHVMzfjOxCfmCHotI_YCYDG45thJhVi8TeI66IjI2wpcpax7PE45mzPZ0GXyRbmNPf6Aqeu27BqMUj9ybwRE6A1v8wgpoPqp_OcQdP8beKPdw6rVbJ9XHPn93qKUlevJqbqHirEWYLJo8PLtXupq9Kg-L431Gfbac9pAmRssPPpIADvDiK10VEeerRw2-y3nd92vI0z-XvStB4sFyRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اذعان نتانیاهو به تلاش ایران برای تحمیل معادله جدید بر اسرائیل
🔹
نخست‌وزیر رژیم صهیونیستی امروز دوشنبه با انتشار بیانیه‌ای گفت که جنگ این رژیم با جمهوری اسلامی ایران و حزب الله به پایان نرسیده است.
🔹
نتانیاهو ضمن تکرار ادعای همیشگی خود مبنی بر اینکه ایران نباید سلاح هسته‌ای داشته باشد، به شهرک‌نشینان صهیونیستی ساکن در شمال فلسطین اشغالی، وعده داد که امنیت را به این شهرک‌ها بازخواهد گرداند.
🔹
وی با بیان اینکه ایران و حزب‌الله قصد دارند معادله جدیدی علیه اسرائیل وضع کنند، مدعی شد که مسئولان رژیم اجازه تحقق این کار را نخواهند داد.
🔹
نخست‌وزیر اسرائیل پس از پاسخ کوبنده نیروهای مسلح کشورمان به جنایات این رژیم در لبنان، خبر داد که در حال حاضر، «در جبهه ایران، آتش‌بس برقرار است».
🔹
وی با بیان اینکه اگر ایران به اسرائیل حمله کند، «ما نیز با قدرت پاسخ خواهیم داد»،  مدعی شد که حزب‌الله ضعیف شده است.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/440752" target="_blank">📅 19:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440751">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9d899f7a8.mp4?token=SA86rtq8x97hJYw3EV-IqkOxGr6fjbaQpo7X1WQfgY4aWdxLqjAXPLrqkZjyAjyE6kdsbUPvkK8WfiSUl8_oxnKxxa_TOo-fZfuyhnz8ZT6OOqe8QdcS5dB8fFxPigs9tnmAxE04H0xb9gYPmDqrwKDsJgKr3LmdXrgqJHQ1ZKqxDt1Sir3GVyuv-XrGXi7PbFp3VdC39ehGpKH0xMhtp3beM8FpHNxNcIacruU6EkngesjlYpFsnFVc8AGCaAt3Xm54XiTiOffFvtStIvn8OBCj9JNO9EWuKyIACOsvfJVJTNdsEf2P1OKUpPWpcGxVpNR-8ZR9QRN70pCTnkV0xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9d899f7a8.mp4?token=SA86rtq8x97hJYw3EV-IqkOxGr6fjbaQpo7X1WQfgY4aWdxLqjAXPLrqkZjyAjyE6kdsbUPvkK8WfiSUl8_oxnKxxa_TOo-fZfuyhnz8ZT6OOqe8QdcS5dB8fFxPigs9tnmAxE04H0xb9gYPmDqrwKDsJgKr3LmdXrgqJHQ1ZKqxDt1Sir3GVyuv-XrGXi7PbFp3VdC39ehGpKH0xMhtp3beM8FpHNxNcIacruU6EkngesjlYpFsnFVc8AGCaAt3Xm54XiTiOffFvtStIvn8OBCj9JNO9EWuKyIACOsvfJVJTNdsEf2P1OKUpPWpcGxVpNR-8ZR9QRN70pCTnkV0xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی دولت: احکام جدید مستمری بازنشستگان تامین‌اجتماعی صادر شد
🔹
حداقل رقم مستمری ۶۰ درصد افزایش یافت.
@Farsna</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/440751" target="_blank">📅 19:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440750">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwcmBb5HpMhhv0YujyEa4supbCSyqDZeffmh8EpZcfRHQEIAh5sJQWarsj_l8ai5UfOVwVNztsP83qSUhgujqLunZlYEHJC0vO6c6XO3SjeAMO6YAnQzQPfZEV2HADf_zSdT1sJSn_rlOiZdKGwdOrLovW1pxUdYlWiPTqdPIWzy145x4upOG6xKF8ckATQl8Xn-CdJNI9_nFmOw016z-ufWLpUM9U6vihiKreQqwQcDm89pOJ86cWQ_kBQ3g_1HeAzRT5dC_AoDWXOeT1f550ZEbJWV-tuNJuKJTTOJTKs57FgRxTIOveejANp-UpxGlQwUV49l1a02ns7FMnT85A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
معاون بین‌الملل وزارت خارجه: به اعمال حاکمیت در تنگۀ هرمز ادامه می‌دهیم
🔹
غریب‌آبادی: ایران هیچ ارزشی برای تحریم‌های اتحادیۀ اروپا قائل نیست و به راهبرد خود در حفظ حاکمیت و اعمال حقوق حاکمیتی در تنگۀ هرمز ادامه خواهد داد.
🔹
ایران عضو کنوانسیون حقوق دریاها نیست و رژیم حقوقی مورد تأکید جمهوری اسلامی در تنگه هرمز، «عبور بی‌ضرر» بر پایۀ حقوق بین‌الملل عرفی و با رعایت ملاحظات امنیتی و ایمنی دولت ساحلی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/440750" target="_blank">📅 19:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440749">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط ۶۰.pdf</div>
  <div class="tg-doc-extra">3.5 MB</div>
</div>
<a href="https://t.me/farsna/440749" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📎
دستِ پُر به میدان بروید
🔸
اگر برای اجتماعات انقلابی به‌دنبال شعر، شعار یا تک‌بیت‌های روز هستید، ویژه‌نامهٔ «خط» پاسخگوی نیاز شماست.
@Farsna</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/440749" target="_blank">📅 19:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440748">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBqV-tb9D7hlmu9MQnjZlqBFofqEWFsU7UcoYjj7dHC07Bik59IWAYX4PwfZBq7GSozR_Bz_zMY5hEf6omrqWMLMO7SuY_9yjdjIsW4miDcXKKHW6BkxSGx-r_A1TyLKVGZjV7yJJXbBf1xCr5zUqv9UuqRc3C2fRJ24vhlwpzKmXQlDpIuazvobmEC2Jq8O3BXF_DhYLtbzuPhKAvQPGrWNa3g7y-6gj8QbnU4KFDC-hC7Hv7UXmjoD37ch_8QCkP_PeACdLrnzFdt0_hvC1F8TResjRWj6kg1YlIYG5Z3UrLolQxkyVHH_d25r3ddU588r3wpAVwvKkeoC0Fbjaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گروسی: جنگ، بازرسی‌های آژانس در ایران را متوقف کرد
🔹
مدیرکل آژانس انرژی اتمی: آغاز جنگ علیه ایران در فوریه ۲۰۲۶ باعث توقف تمامی فعالیت‌های راستی‌آزمایی میدانی آژانس در ایران شد.
🔹
آژانس نزدیک به یک سال است به تأسیسات هسته‌ای آسیب‌دیده در جریان جنگ ۱۲ روزه دسترسی ندارد.
🔹
حدود ۴۴۰ کیلوگرم اورانیوم غنی‌شدۀ ایران از زمان جنگ ۱۲ روزه تاکنون تحت راستی‌آزمایی آژانس قرار نگرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/440748" target="_blank">📅 19:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440746">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pteyT3hkEjli_FPWS1QnBM9TizA8D-AUDyCQTIMWSP_sGdm3rDQsGkNDPnXkrRfbhGqKA6I-o4Q5x79OihqSR43dzeIkavqtdJzHB5Rik4zU2Lzln3KHsvowjPLf4_4O4APqEOgb0h-7k6mQJdmQ6KdbuRRiwtXHqlXM-poNseYoeNvM45u8Ck2f9ff4JMLUG5s--Ngqlt-MM0rBllqbTOWefHMn7Z4uFy1K2FQVuCOQU5dDyzt4kb6lohDkZctkzpzfV8deaE22BiXBSvu4KRfC9q-D2SnxBSXG1o93Om5Dw0E3FKXubDc2CB-LURvvLzKkCNa83hiwOkTYY2kvzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازوکار قیمت‌گذاری لوازم خانگی اعلام شد
🔹
براساس اعلام سازمان حمایت، قیمت ۴ قلم اصلی لوازم خانگی با هماهنگی انجمن تولیدکنندگان، کارگروه تنظیم بازار و سازمان حمایت بررسی و تعیین می‌شود.
کدام اقلام؟
🔹
ماشین لباسشویی
🔹
یخچال
🔹
یخچال‌فریزر
🔹
تلویزیون
🔹
سایر لوازم خانگی مشمول قیمت‌گذاری مستقیم نیستند، اما باید ضوابط و مقررات تعیین‌شده از سوی کارگروه تنظیم بازار و سازمان حمایت را رعایت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/440746" target="_blank">📅 18:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440745">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
سازمان عملیات تجارت دریایی انگلیس از وقوع حادثه برای یک کشتی در دریای عمان خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/440745" target="_blank">📅 18:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440742">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBLWCQns42AnN2Z0b-JKhPhNXExxCw3vpF3QqLQxl37DgvMer6dUMmq6_ngh3ilvirbIqojgWGNo4VkTsmNmZJOa5sMZo-yWF0UVNV_7EDUDoQ2paWaQ-blNjSY1lF-THKy_ZsqhtdK-WNkbju-5DFR1WVpW_IUr0H7RQ3neL5nv7Bs9VIfXfVpGzVQDa6EvWh-ryQHZPH05SczkAZeuHdXex6o__0Jk-923UeBigZi6LHUVW1yePjRSPEZuVCDYFBT4RQfjhINumo4rGKDLS4OOioS5NoA7gje1wTqO5xVh2Bo6p36GhPxNYhH9HhyFdA8EPTZ-V632sceOCgSn2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قالیباف: معادلهٔ آتش‌‌بس روی کاغذ و نقض مکرر آن در میدان را برهم زدیم
🔹
تا زمانی که ارادهٔ واقعی برای اعتمادسازی نداشته باشید، پاسخ ایران همین خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/440742" target="_blank">📅 18:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440741">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EW_KwSCpOnUr7opWIaSD-e6bTnW1x2KvNH1sUmNnd0HTmaE8T8S43dCjcujQE1Fj8LVeC8Xzcudl1MQ2hh047mzHv40uwyt1TTn-03C7Rty1650So2d5ytz0IvxlQDsSPLvH4r884BSqWXZk7L3PDac-n5gedLWiMu9qzFlR9oQQsFJAmu5a-Qc4G4p26qljQ4e-M9_naPHyHy5AgauKUuPQBSmn4gbLCWlyLAaPg366gT2i_O0_bvwp6-vTgKzpUHg7NT2z5lyndplU8Ona58GdmMm0CCV4MpUgs0xYd2IuMfIs-sKtwStzG87WOJbH2zB9kL4Jm6jcKWfYrdMltg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مراسم سالگرد شهید سپهبد محمد باقری و همسر و دختر شهیدش
🔸
پنجشنبه ۲۱ خرداد، ساعت ۱۷ الی ۱۸:۳۰
🔸
مسجد امام صادق (ع) واقع در میدان فلسطین
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/440741" target="_blank">📅 18:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440740">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6f1a255f8.mp4?token=ao2MWX5g8W19_0KFJ_MZUT5jTpQkTUowZBjB5w67JhmcupVAbYZgLpw1_ioALT_4YjsHAgRl0YVCDPG_IJoiSnUXDKjX-aA9s9nATEhc7xLpp7XWfrB7z-nImGJdCcmlJq4Caa-aBz7tl-GmcfIP1eKcjzwM8f2Sw91mSyb0O_oGUA5oE82pzak396u91lA3jk173yNfY1qQzuvzcEiyinEzLv64A3MGh7a2WPvlsnFUuHzX3ktFWuV3s7mcWgn4PA9uuCDE7Oq9hb_noaWU0tChyfCxMiNQn0pu0pJeiTBadj4543Ocot6qWt7XHjNoEu25t8GDWCQatJXUiDMJ_4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6f1a255f8.mp4?token=ao2MWX5g8W19_0KFJ_MZUT5jTpQkTUowZBjB5w67JhmcupVAbYZgLpw1_ioALT_4YjsHAgRl0YVCDPG_IJoiSnUXDKjX-aA9s9nATEhc7xLpp7XWfrB7z-nImGJdCcmlJq4Caa-aBz7tl-GmcfIP1eKcjzwM8f2Sw91mSyb0O_oGUA5oE82pzak396u91lA3jk173yNfY1qQzuvzcEiyinEzLv64A3MGh7a2WPvlsnFUuHzX3ktFWuV3s7mcWgn4PA9uuCDE7Oq9hb_noaWU0tChyfCxMiNQn0pu0pJeiTBadj4543Ocot6qWt7XHjNoEu25t8GDWCQatJXUiDMJ_4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حزب‌الله یک تانک مرکاوا در جنوب لبنان شکار کرد
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/440740" target="_blank">📅 18:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440738">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ybr3gt0iMrFSc8Hb4f_N5rF0EWxQp4CcvMC74tdIaR8JWRtQ0YDsxnmPv2fqnL1UKmsmR5I4bc7s0inLyygPLtmXyYLQd14GjJM7UCR8vNBGyWZ5qqcqm-egQx1TSaQfohwIJ4nqYuRLOTu9qKuJgY3mnKP0UblOMwvU5l8a1JU3OwF3H7grcoQCNqW5SazUaCML3hGN8XFIxVddZtrgAJk7_WG1ooJ3JusGP-cMDbdGQm8sqGVpFbdAk63Ie2j9ZKvTop9rTA6N9tfMsglzdqf3ptWoeOLQufNb6sIYKMOiZPSKcZHxcJyfuGzse-JtVEgBsYG0bGsRc2FtiefVZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دبیر شورای‌عالی امنیت ملی: اگر ائتلاف آمریکایی-صهیونی بار دیگر دست از پا خطا کند، منطقه برایش جهنم خواهد شد
.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/440738" target="_blank">📅 17:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440737">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‌‎‌ آخرین وضعیت فرودگاه‌های کشور
🔹
روابط‌عمومی سازمان هواپیمایی ایران: تمام فرودگاه‌های غرب کشور تا اطلاع ثانوی بسته شده است.
🔹
درپی حملهٔ رژیم صهیونیستی در شب گذشته به فرودگاه‌های تهران، فرودگاه‌های مهرآباد و امام خمینی(ره) نیز بسته شده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/440737" target="_blank">📅 17:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440736">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حزب‌الله: با یک اسکادران از پهپادها، محل تجمع خودروها و نظامیان «ارتش» دشمن اسرائیلی را در شهرک «الناقوره» هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/440736" target="_blank">📅 17:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440735">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFwnfoMKOWKB5br_Kjv9UkhMWSgCiAQN71WzwgC7rINeuOiYbImBzu_2JH59wr4TgOU9fdguwL8SFYAxCjYELh3YarqBHQmgO8N1MVvqBygWkk9XGajUIqo4_u-Yp7iEb7tnzbA0zsv6rUIekkjmiyx3c-Ix4fNJUbb6UI0qcHmG1FXYHEeKcE8ZPuQ9C0mj62EnPMSdoz_-wjB54IIZhiCwok1SHEnnFtbdmk4qXVfz9NsMaK30kez2iNNAbDTE0Xzf5S4jM14Me7pZIdnNTy7iTIGWZ_2dDUnQVmMZSGokcu1NWh_aRPYdaanqP2tDQ-ROUDU3aDcEbjGe8VeBKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مراسم اولین سالگرد سردار سپهبد شهید حسین سلامی
🔸
این مراسم پنجشنبه ۲۱ خردادماه، از ساعت ۹:۳۰ صبح در حرم مطهر حضرت عبدالعظیم حسنی(ع) برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/440735" target="_blank">📅 17:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440734">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پشت‌پردۀ شایعات ترور مقامات نظامی و سیاسی چیست؟
🔹
همزمان با آغاز حملات اسرائیل به برخی نقاط کشور، موجی از اخبار و شایعات درباره ترور، مجروح شدن یا هدف قرار گرفتن مقامات سیاسی و نظامی در فضای مجازی منتشر شد.
🔹
تجربۀ درگیری‌های اخیر نشان می‌دهد که این اخبار صرفاً با هدف ایجاد هیجان رسانه‌ای منتشر نمی‌شود و یکی از مهم‌ترین هدف آن‌ها تحریک جامعه به تولید داده‌های ارتباطی است.
🔹
انتشار خبرهای تأییدنشده دربارۀ مقامات سیاسی و نظامی، معمولاً موجی از تماس‌ها، پیام‌ها، جست‌وجوها و پرس‌وجوهای غیررسمی را به‌دنبال دارد.
🔹
این حجم از ارتباطات می‌تواند برای سامانه‌های تحلیل داده و هوش مصنوعی، اطلاعات ارزشمندی درباره ارتباطات افراد، حلقه‌های نزدیک و مسیرهای تبادل اطلاعات ایجاد کند.
🔹
همچنین انتشار چنین شایعاتی، نهادهای مسئول را ناچار به واکنش و تکذیب می‌کند و در برخی موارد می‌تواند به ایجاد فضای ابهام، نااطمینانی و جنگ روانی در افکار عمومی منجر شود.
🔸
کارشناسان امنیتی معتقدند شایعات ترور فقط برای ایجاد فضای روانی و التهاب رسانه‌ای نیست، بلکه می‌تواند با هدف جمع‌آوری داده‌های ارتباطی و شناسایی شبکه‌های انسانی منتشر شود.
🔸
در چنین شرایطی، مهم‌ترین راهکار، پرهیز از بازنشر اخبار تأییدنشده و خودداری از ورود به زنجیره گسترده تماس‌ها و پیام‌هایی است که حول این شایعات شکل می‌گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/440734" target="_blank">📅 17:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440733">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb9ad04539.mp4?token=Op4ouAgQXruCF9fXENTl_3oXuvpwO_la2G53MMI1CdC3vzpFE5Z-Ol4kDFzbwXIQ-P-0gpqy-uVOcBKCWQZ78j3x_x9HZLwzHyB0GrNdccA7ly4QBNNc7y2WoLt6fmDG_GaDlCgjz0Du_QLSKXz8DPt0Yaxn9VvWkCW1I0QEvQCYyk0xFLkppGSnJJl1_hbc5m4FILMmggLgo4cj9Du0SKNjowfgCpWeL0I6q0m38TqImJFeVoOrDGX6UnSDuL1eDrGwpFuP_ju_6QZvZo68XHga6ICmL3_e1jg_49A91CabGFRqgTQqthppwd6ryTVYQWBq9HlMOBI8ApiHF8yBCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb9ad04539.mp4?token=Op4ouAgQXruCF9fXENTl_3oXuvpwO_la2G53MMI1CdC3vzpFE5Z-Ol4kDFzbwXIQ-P-0gpqy-uVOcBKCWQZ78j3x_x9HZLwzHyB0GrNdccA7ly4QBNNc7y2WoLt6fmDG_GaDlCgjz0Du_QLSKXz8DPt0Yaxn9VvWkCW1I0QEvQCYyk0xFLkppGSnJJl1_hbc5m4FILMmggLgo4cj9Du0SKNjowfgCpWeL0I6q0m38TqImJFeVoOrDGX6UnSDuL1eDrGwpFuP_ju_6QZvZo68XHga6ICmL3_e1jg_49A91CabGFRqgTQqthppwd6ryTVYQWBq9HlMOBI8ApiHF8yBCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرواز همای: اجازه نمی‌دهم با من مثل استاد علیرضا افتخاری رفتار کنند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/440733" target="_blank">📅 17:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440732">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71155f3d2c.mp4?token=UotjDACJoPa4MOLlkZvypf8ZFk7sIgtFyjmGrLKVnJIF1udLNeh9lgaPtJOR7nFmQCOTvaLDsW2uNFZIWA9PfyvW4XFRz2Pgf_r3C_EqydktaLEXgdta4FapUhwdOEOGb-LaOkKmeZSQN_H02IzwSc7g9btgidQBLHIcSQSeqa9WYYtHRf14uzpNmjNT4Xg2CMRNHbnz1w_yIpRHFqkBpFBRYiO4clvyPW2hu7nt1xC4PfrhDtiVvhy_N1lKvvWRT75e3pqPuNicAUySPvhdioqzCoIDZeTQt28qx46_71HKzsr8ROhDmfW-C0kkh6db7Uu0al7b-yHX8DbhmOWFlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71155f3d2c.mp4?token=UotjDACJoPa4MOLlkZvypf8ZFk7sIgtFyjmGrLKVnJIF1udLNeh9lgaPtJOR7nFmQCOTvaLDsW2uNFZIWA9PfyvW4XFRz2Pgf_r3C_EqydktaLEXgdta4FapUhwdOEOGb-LaOkKmeZSQN_H02IzwSc7g9btgidQBLHIcSQSeqa9WYYtHRf14uzpNmjNT4Xg2CMRNHbnz1w_yIpRHFqkBpFBRYiO4clvyPW2hu7nt1xC4PfrhDtiVvhy_N1lKvvWRT75e3pqPuNicAUySPvhdioqzCoIDZeTQt28qx46_71HKzsr8ROhDmfW-C0kkh6db7Uu0al7b-yHX8DbhmOWFlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بالگرد اسرائیلی یک ساختمان مسکونی را در غزه هدف قرار داد
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/440732" target="_blank">📅 17:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440731">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f601e1d28.mp4?token=O0RumWm7ZMenfX1Rx7_txrd8-q3qirbzp7g13FPDvk6cB_adjUbXHkN4v20p3_GFXsCk6BUx6_aNBN3kjB6HS3C1w3aF6CJOwl-ZkLEdUSEguRbvSSj7WOOti-N6zLKzYHFMZc17dN8s14r0Zhsn-0pO7hlHkOMY7ooqqUxSl117zpiX6rbKTqPTW84YskVb6FWTU5ySG_V3v2HtYS5C0DwNpggkezvjSjFAE18Gxhc6_EYf-jKOPmwiV1kbphHvQcdJTh3bZwjM2CDuB8YNc30zAchSq9T45uOqH9NMeyjxQJApBI2msTnfcvFqB9Cj5bMMx13DxoPwkKI684kMpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f601e1d28.mp4?token=O0RumWm7ZMenfX1Rx7_txrd8-q3qirbzp7g13FPDvk6cB_adjUbXHkN4v20p3_GFXsCk6BUx6_aNBN3kjB6HS3C1w3aF6CJOwl-ZkLEdUSEguRbvSSj7WOOti-N6zLKzYHFMZc17dN8s14r0Zhsn-0pO7hlHkOMY7ooqqUxSl117zpiX6rbKTqPTW84YskVb6FWTU5ySG_V3v2HtYS5C0DwNpggkezvjSjFAE18Gxhc6_EYf-jKOPmwiV1kbphHvQcdJTh3bZwjM2CDuB8YNc30zAchSq9T45uOqH9NMeyjxQJApBI2msTnfcvFqB9Cj5bMMx13DxoPwkKI684kMpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: تنگهٔ هرمز مال ایران و کشور عمان هست، به هیچ قدرتی اجازهٔ دخالت نمی‌دهیم.
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/440731" target="_blank">📅 16:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440730">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63423f1479.mp4?token=V687PabyQIyJ5DzzTBaXSgXH9Qjzxx1uDig9xi-z4DujuyKectaC8OEXyyyHcMmp-Iuos8-UQiwf_5EBh6WiTD3XJG-3WasGhqKQ5xu0kbqvI15rpHt9zKnl6qCjV_5fIR9QB342FItg5PvH2udbumwNmGHTi5R5OJhH05Afn_4_jv3EMaR64Ae6PzM3KpmDjCC8Yfzq0YhbvM9JYzwtGv_qJVsiS9IR5ndZ4M1sUx1egPez1xcMYgW2kHTwJXhk878wyrmO65sI8zSbf72JwdoNGCPO0nmVa4jZORmG-j9A0foQE8kcNrZ_jaBEcR2bjhpQzSOUkMguUfeqWWakow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63423f1479.mp4?token=V687PabyQIyJ5DzzTBaXSgXH9Qjzxx1uDig9xi-z4DujuyKectaC8OEXyyyHcMmp-Iuos8-UQiwf_5EBh6WiTD3XJG-3WasGhqKQ5xu0kbqvI15rpHt9zKnl6qCjV_5fIR9QB342FItg5PvH2udbumwNmGHTi5R5OJhH05Afn_4_jv3EMaR64Ae6PzM3KpmDjCC8Yfzq0YhbvM9JYzwtGv_qJVsiS9IR5ndZ4M1sUx1egPez1xcMYgW2kHTwJXhk878wyrmO65sI8zSbf72JwdoNGCPO0nmVa4jZORmG-j9A0foQE8kcNrZ_jaBEcR2bjhpQzSOUkMguUfeqWWakow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس‌جمهور چین وارد کره‌شمالی شد
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/440730" target="_blank">📅 16:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440729">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLhy7YQbI4ZboSVFVCeaEC4cvHKrlyvBY8lncieKsW_wwbM4klxcM9JXVwnuW390sNo2S3O61SbYEVshz0OMJBVWHtbIL2_RE7zeh8O5lmYJKuYorzeknMvD16lRT-nl8ttaieCkxsam7Is9IzHyiP6OcNu5ZLRt7-nCQUNAaI3rTS3D1eYc73qOBTgGq-GSYJTUkYxdTWC6Y3gh9-VvfX6Vm23jzBjx65Os-bXHy72-8yQM4Qx4aesw4NAyhzBYZqOiilfOb7HNrZw5JmH6eCaXWVxD_IfM2NuoNXOVaMM8mzR-C3O8ADjElLnWVxz0_y-xQ5BGiq0qY7GFQ1ZTTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوتبال سیاسی به FC26 رسید
🔹
سال‌ها پیش، زمانی که در برخی بازی‌ها تصویری خاص از ایران ارائه می‌شد و حتی حمله به ایران به شکلی عادی‌سازی می‌شد، کمتر کسی به تأثیرات فرهنگی و رسانه‌ای این محصولات توجه می‌کرد. برای نمونه، در بازی‌هایی مانند بتلفیلد، این رویکرد با فضایی کاملاً جدی دنبال می‌شد.
🔹
امروز نیز نمونه‌های دیگری دیده می‌شود. در نسخه جدید بازی فوتبال EA Sports، اطلاعات و ترکیب بسیاری از تیم‌های حاضر در جام جهانی ۲۰۲۶ با جزئیات کامل ثبت شده است، اما تیم ملی ایران با اسامی متفاوت و غیرواقعی معرفی شده؛ نام‌هایی مانند «شا‌کرمی»، «افکاری» و دیگر اسامی.
🔹
حذف نام و تصویر واقعی برخی بازیکنان در بازی‌های ورزشی اغلب با بهانه‌هایی چون محدودیت‌های تجاری، حقوقی یا تحریم‌ها توضیح داده می‌شود؛ اما نتیجه نهایی چیزی جز اعمال نوعی سیاست فرهنگی و رسانه‌ای علیه ایران نیست.
🔹
از سوی دیگر، وقتی یک کشور یا یک هویت ملی به‌طور مداوم در محصولات فرهنگی جهانی با تصویر ناقص، تحریف‌شده یا غایب نمایش داده شود، این مسئله می‌تواند آثار فرهنگی و هویتی قابل توجهی بر جای بگذارد.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/440729" target="_blank">📅 16:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440728">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f18b8d73f.mp4?token=Cl182jroFH_uF_0YFSBSZK2gUaG6TXAQHKnX2_RQCEl28W6hK4km9-EUIPNi1vYyhT071L5o2Zjb9-eLBl-XNOh0wplaN2E8DJGigUD0Y3dpdEenqhGsZGN3DbG1Ybh6Z1J1CpLWVo58xEi8fGv5XYd2hP43RworIA_iwFimyO4QIFP5alO8Y6jaCtYNNz7VmpB1TNPAjUi0wFBrQ1nkBiTYDmHE3JFzCT8M9Fee3YDG3Y9YewI9mZNhPcl2CePC9KpHMrqO-X-JIrHVawa309iVsdDRuq0CKf3al4beRtf7g6yf2EV0xeb9vW7pKOQVH3hmQI4S9Ypr0S9nt84fmjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f18b8d73f.mp4?token=Cl182jroFH_uF_0YFSBSZK2gUaG6TXAQHKnX2_RQCEl28W6hK4km9-EUIPNi1vYyhT071L5o2Zjb9-eLBl-XNOh0wplaN2E8DJGigUD0Y3dpdEenqhGsZGN3DbG1Ybh6Z1J1CpLWVo58xEi8fGv5XYd2hP43RworIA_iwFimyO4QIFP5alO8Y6jaCtYNNz7VmpB1TNPAjUi0wFBrQ1nkBiTYDmHE3JFzCT8M9Fee3YDG3Y9YewI9mZNhPcl2CePC9KpHMrqO-X-JIrHVawa309iVsdDRuq0CKf3al4beRtf7g6yf2EV0xeb9vW7pKOQVH3hmQI4S9Ypr0S9nt84fmjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امنیت تل‌آویو به بیروت گره خورد!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/440728" target="_blank">📅 16:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440727">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/831f3f3a87.mp4?token=hZm5klNVBX2LQonmGgTlY2zWhCEcfWCb-aZDu1iTZ3G8R5NRWP9Q2N7fWlXvRaG81w6NTo6UQOBq4d3XKyl1nhCjIDFl5i47GsAFFVBGt-05fGZguUh2AHiUu5QE23UUeWoHHREnenpv8EXtqUnaBEEBQaX5nCaZlN2kGrYdTHQ8tVKgvIL-vp1yGYl1Uz0TDcEChjx9DXg4ZgIzDbVqGoEZDUcNUU8HsZsIsP9RjLoOkYJjxFluvYBYfDWVzA-rZvDAJPd8y7LOEn-D26wOESGOytoDLJxBDidHcq4NyaBpX9OWnKEpdqYefe2xkKQPgw-QhIWB-l0lpx1vhLuSyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/831f3f3a87.mp4?token=hZm5klNVBX2LQonmGgTlY2zWhCEcfWCb-aZDu1iTZ3G8R5NRWP9Q2N7fWlXvRaG81w6NTo6UQOBq4d3XKyl1nhCjIDFl5i47GsAFFVBGt-05fGZguUh2AHiUu5QE23UUeWoHHREnenpv8EXtqUnaBEEBQaX5nCaZlN2kGrYdTHQ8tVKgvIL-vp1yGYl1Uz0TDcEChjx9DXg4ZgIzDbVqGoEZDUcNUU8HsZsIsP9RjLoOkYJjxFluvYBYfDWVzA-rZvDAJPd8y7LOEn-D26wOESGOytoDLJxBDidHcq4NyaBpX9OWnKEpdqYefe2xkKQPgw-QhIWB-l0lpx1vhLuSyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اشک‌های بی‌اختیار یک دختر بچه‌ برای رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/440727" target="_blank">📅 16:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440726">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): پاسخی دردناک به رژیم داده شد و توقف عملیات اعلام می‌گردد
🔹
درپی تجاوزات و شرارت‌های رژیم سفاک صهیونیستی در جنوب لبنان و منطقه ضاحیه که با حمایت آمریکای جنایتکار صورت گرفت، نیروهای مسلح مقتدر جمهوری اسلامی ایران در راستای…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/440726" target="_blank">📅 16:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440723">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EhEJtlERNOLqVldSD8-565aKb6hglPlDxCWFJAPjNP5-ywHNG_9M4qqfZn-7DhCu5q27SdQImAsE2lmrX58SgofPKR-qR5ocIVuzY-yjGpyyVXxySGX0OqGyOsteCQi6CUmzFH6uC7cwDSZNemt0VZSbi-hLDKc-oDA1xb6jxfSp2RQ_b2kGZO9zuU-duGqSTTJLm_TvI64y40Rt8BdAZgw2II_vyrjlUnJa2Ju47y9p-vxq8Rg6mcxauElpsJ9gTWZh8K8IQ47_Rv9BOSIw5g1CYKbjzFohjA5VYqkkJFPT_1Q_dzlR_qT3zOQVyOB7xPsZmcbixnUfH5dteHYdcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JAAnR9SPlFakpUmNZxbiIajL7H4ys3Y1tgnjdU2HYT2wNFlc_lmyOiNAogQSIEpGj_WBQEhgtp6o3dBOFPVYoFDpsy1XwsNxLr0bruma0TI_ozFdvWt2HW8Mbiev5telQCyhLKgvu5NZvEEOp61XFGv8VgEP__mYnR9jRQjDgrTdjX-tS64oXicLX884qsbHdBPoTtfX_Q1yPoTAwmxrgLF2KU4u2bwTftuUTJUFjKC6owR2SRQvyJx1NDshtRuPKEJE5oe1MruyOb5Pv8wveW6DpDJtwOMH6vSdRX4U_8syGs37ANUr-rXJY-fpsWQCIkYTAfx6v5ILKynsGy7fug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9ecefb81.mp4?token=rx-ulupRQTzV0blGA0uvcGXRAzPnGCfaQdQHXAlN4uqg_1sbdtfHvXIJqRTybsXtqdj1S_2FvxF3LRfp4ruQW9mQmqtDXxY2al_ejVeNasXBPh4NGoSEUnPF69nNYBpEeVPIecS5QFNziObxjkr6_F-NDHdKkmQWBEalqhf_EJA0AFx9Iqtbagwrgh9Dica2HkBtFyL-d-ft5Ww2dBVzudwq1L5g89WsWRRukh_YkV08-Rz-3OxJwz85zHX1lPGDOxRskwq9DwHeSercJUJSfjuI8gRVGXutHg-ImzHJP9s45hb2ysr6_tf7pcLg46mnv03j33YJYMKqbaLdvHHItQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9ecefb81.mp4?token=rx-ulupRQTzV0blGA0uvcGXRAzPnGCfaQdQHXAlN4uqg_1sbdtfHvXIJqRTybsXtqdj1S_2FvxF3LRfp4ruQW9mQmqtDXxY2al_ejVeNasXBPh4NGoSEUnPF69nNYBpEeVPIecS5QFNziObxjkr6_F-NDHdKkmQWBEalqhf_EJA0AFx9Iqtbagwrgh9Dica2HkBtFyL-d-ft5Ww2dBVzudwq1L5g89WsWRRukh_YkV08-Rz-3OxJwz85zHX1lPGDOxRskwq9DwHeSercJUJSfjuI8gRVGXutHg-ImzHJP9s45hb2ysr6_tf7pcLg46mnv03j33YJYMKqbaLdvHHItQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات شدید هوایی رژیم صهیونیستی به جنوب لبنان
🔹
منابع لبنانی از حمله هوایی رژیم صهیونیستی به  محله «المساکن» در شهر صور و همچنین شهرک‌های  الخرايب و كوثرية الرز در جنوب لبنان خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/440723" target="_blank">📅 15:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440722">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c159decf7.mp4?token=tXX-lB6bciEb0qsP9C3VgcmbyYUypTxuZmlgT8o5FO-qyTgKj4OpUhk1a6DwzuS32EaWGNAPkvtMrcrBiTelr0VmU-tmZcKJQSuFECLouq7JzfAdM3V1zir61HiB7a5r_hPWn6LnwPX6VEy9_2oru9XS-54ozEGhaqS4RRfOWT_kKXnJaFr_PwhPJdb4HqRBzhUuDhYvzZld7SCdhQ9p--YjFht6qQikqtw_bVB8ywEp6YXFh8Ea-jol-N4--E7kn776CszKjA7FkajeR6dlYwuXUEwsxZlfMi-1t2ZAANXr7c-_Hue6Zpg3nTNzMPoOdRAJQBSHVfz-D2g_VP1QlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c159decf7.mp4?token=tXX-lB6bciEb0qsP9C3VgcmbyYUypTxuZmlgT8o5FO-qyTgKj4OpUhk1a6DwzuS32EaWGNAPkvtMrcrBiTelr0VmU-tmZcKJQSuFECLouq7JzfAdM3V1zir61HiB7a5r_hPWn6LnwPX6VEy9_2oru9XS-54ozEGhaqS4RRfOWT_kKXnJaFr_PwhPJdb4HqRBzhUuDhYvzZld7SCdhQ9p--YjFht6qQikqtw_bVB8ywEp6YXFh8Ea-jol-N4--E7kn776CszKjA7FkajeR6dlYwuXUEwsxZlfMi-1t2ZAANXr7c-_Hue6Zpg3nTNzMPoOdRAJQBSHVfz-D2g_VP1QlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حمله پهپادی به مقر تروریست‌های تجزیه‌طلب کرد در منطقه «کویه» در استان اربیل عراق
@FarsNewsInt</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/440722" target="_blank">📅 15:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440719">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RzDwMNoL9qR_P_LsF_5efti1LxXX3ocjqH7fWGQVXYLfwiwMRLp5ORCBKriNgI3o_Lk-ZIRp3-LGiG_nj_6-2ARxDbDKWGOCdTfEDAsdM5OXaWsLkwV8tAhc8zttg9ZRXaMc19-U9mHB1LrTMp1Vi1V0rtglrrjrCGOvMcwd2vEDouUc0IUXRtiaZTgOce_Syd4FD8ocZlr_JMwNJ5CQthUkXejvFFdB72_My2EP-ktIhHKt8FC2rvarO2oPW20-FuejN3rhyGzY26V1WuNMQVbwGcaQlVdsY0HJVWaqtH6-8Guqn-iv7K7XuTlJCK8PJNxid6Yq988YLK6Qh9W_BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/USUDrpMxdJX58EJ2L1Gq7VnyWH_MeeCcSLH7P8bGtVET7L9pMDs4nrmhxrEXRd7gUJAgk5Ph7UZv4wlJ2jyoDMP2Q3QReS9vdSaeWw6fawb3BQ_yYNc5Oz_1grF2wObJhNBseV5pnW7F24fMOs8noNwkSP3kJsvQrJCCvZJasLcqZM35-gqZn0fIUrbyRxPZXNfiM7UXWrqqRQT3Ttdhvk9Aw-47J84bOLkRJqPeNl89xU1p7OikK9l4U-B5jFr6_vc1K0bP2o8GxYsaiHZQ-FG6S1lwiMcToMPy2U9UZc5RtuxdLmmM8guCxYkrhTei9Dk4EpuN7jT4cVk1nWV6rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JROymc-lZTOJ_-awrx56ewtpQY3ExC9-T5zMFUzZZVc6uwKah4uTc5F1hEBOLDDrb6sqpbh9VVirB7FSekSFn7OuBSdq6OJqbCs0b2j8z7DYvnZ_mKF11qzsiIOU9HerBVXsHYVpwJqoWO_x51Mf4k1JHGBkixVLLt9ixwBBcol-a9cQxdE3w7xqR8HodSLMZQIqnbjZNizCT6y0t6iLcb7H6F5MFtNo5WFWZKH2_WosIKniej_6fQeu5739oN0BLOx6ziPZsHBAwW6E72i3hq1xqHHVjnjvmPwxEOSFnUJZ_c8amPtpHVE_m3eRZ_Abm5z4BGDn1J4g7QbkqK2ENA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هشدار هجوم مارها در آستانۀ جام جهانی ۲۰۲۶
🔹
فدراسیون فوتبال سوئیس با نصب تابلوهای هشدار «منطقۀ مارهای سمی» در اطراف کمپ تمرینی خود در کالیفرنیا، به بازیکنان و اعضای کاروان این تیم نسبت به خطر حضور مارهای جرس هشدار داد.
🔹
کمپ تمرینی سوئیس در منطقۀ کارمل ولیِ سان‌دیگو قرار دارد؛ منطقه‌ای که زیستگاه طبیعی مارهای جرس است.
🔹
فدراسیون سوئیس اعلام کرده برای جلوگیری از هرگونه حادثه، از بازیکنان، مربیان و کارکنان خواسته شده از ورود به مناطق طبیعی اطراف کمپ خودداری کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/440719" target="_blank">📅 15:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440718">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlR-Qh9o5MAYGiqGFFDg8zYWfMxWw0BeMLYpbZAHfwVjtgkdfLuhC20Uz2MtMjhtLaz-VAfNKZYCMtZemb7DPWMILv1_8-qKQW_BuM1yLKKPm9mzYXOtzdNC38GTEYjSTgMjmsrlr8fEh7v-Mulx5MTuMyUEv5ByIJL4Rjj9-Xka3bmu1ANvOmnSdyGtPM85a8Sq7a9OJiRcpPhb-hsniUEAArih4iVJ5d6m5tb5mL2pbrJL_oqR5NrgrGcXU-uj0yG3wRp2pTYMGOn0YaW8zl1O1vWSz0ws6sNqrmb-ujcHhf3-cGlrJ1Wpoq4cy-IGV6hj6HP_LCGDQsNEqfSdfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملهٔ موشکی حزب‌الله به شمال فلسطین اشغالی
🔹
منابع اسرائیلی از به‌صدا درآمدن آژیرهای هشدار در شهرک‌های شمال فلسطین اشغالی از جمله کریات شمونا درپی شلیک چندین موشک از سمت لبنان خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/440718" target="_blank">📅 15:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440717">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hr_lK_nLjfNbWMwLR4f-ZVljaOpsm8QmqWNf30oGSxyqrsGC-zVOo4wtJb_QZ80Y54lo9LI9EhQoDdl9bMKiUUuV55E0f5gDTPNZIoBsbJNRzUDbtVaiR5Y9lAaXKNLIwuHq-iPBGOX8y8A7Efo3M0UhK8AHZ3e98LvV9B1U9LJb7-Q4bVDUcgeo_h4GbLbtLZZW7r0vfKXTjz1s8Mr5ZQvdagh-nNlPbVXlLldhBMe9k9ARIhiivfuD4cDPn2NHCDsu1jMX9CNrsAuGTsKxgKHCT48n_ELGV6XMMEcO2vC-zcNqxflH-tD70OeucKNaayo46tMf8UrOhtHbgoWMdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده ارتش: در صورت تکرار شرارت‌های دشمن، اقدامات ما شدیدتر خواهد شد
🔹
سرلشکر حاتمی: ملتِ کشور دوست و مبعوث شده ایران عزیز!
دشمن در حالی که میانجی گفت‌و‌گوها در ایران حضور داشت بار دیگر با عهدشکنی و نقض تمامیت آتش‌بس ثابت کرد به‌هیچ‌وجه به آتش‌بس و توافق پایبند نیست.
🔹
صد شبانه‌روز مقاومت و ایستادگی‌تان، تجلی اراده ملی، اتحاد یک ایران منسجم، فتح قله‌های تاب‌آوری و پیام روشن همدلی و اتحاد مقدس، تحت رهبری و فرماندهی امام خامنه ای ( مدظله العالی) و پاسخ قاطع ایران یکپارچه به دشمنان غداری است که استقلال و تمامیت ارضی این سرزمینِ پاک و عزت و امنیت مردم شریفمان را نشانه رفته‌اند.
🔹
به پشتوانۀ شما مردم همیشه در صحنه، بار دیگر با اعلام آمادگی کامل ارتش جمهوری اسلامی ایران، هشدار می‌دهیم مسئولیت تجاوز رژیم صهیونیستی برعهده آمریکاست و در صورت تکرار شرارت‌های دشمن، اقدامات ما شدیدتر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/440717" target="_blank">📅 15:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440716">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_0n8qYNnSuwlcBTjPMbLe01nR2ABSQG1wLf9u27z-6C3HKzJ7qnmAP6E-wHqaj_PtfaUsHHZCD4-6u7HHB_06HhUiD-Rcs_kfZyWMFTkjMI8L9ADhfZ5D_Z9H-aekHsKLERwjptLr6ILJUNdklM7fisIqP6JScpq0nNfTQcb3E9o7_uBnbSRMc99QzmziyNze0rgjQ1lvnKwoXBLGxD05cs8AIvpQCZNJMz0DAS_vmShBChh0hpl52ZG1QMwKw5B9Cwcto9OghoxCw1ucdzR8-XeBzLR5sU7DgNfPGgFVpn3aBSbzx801C1Z1v5gJ8oEmgO1DYdfprmVYQfD2Uq5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: در برابر هیچ تهدیدی عقب‌نشینی نمی‌کنیم
🔹
دیپلماسی و دفاع ۲ بال قدرت ملی‌اند؛ نه میدان را ترک کرده‌ایم و نه میز مذاکره را.
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/440716" target="_blank">📅 15:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440715">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFiIR4I3zJWFXXmbOZOPNKlK9wAVpKI6ad_krgCtIaNzM7WYZffC-osEvRg6LxKy2d6sCHq_sJ0NZJIbtQ3BkNUeC2vOz2R9KF1IQxI8mHp1cbcQ8xFgiOp9qNLoZ-UFLPNlrw0p9ud0vddu0bQPhF_N6BGex2VOR9ZNCFEnwZSnqED6UYmLzKlkXdzRCo_nS7qqL6zk-lvDm4UuY1IZce6kiNKGASauJgWS6t6oF8bcSFbqnvk9Tdcm04cdbXwLUYOcGNT1l5O9CG0hNFhCwyU1tEAkm4eTgm5KRql3rt6svKT3MJd4kdCvCm5Hqr1QW_lLmm_8H8ESGf8iz7cyQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای اماراتی در مهر‌آباد فرود آمد
🔹
داده‌های ناوبری پروازها، تردد یک فروند هواپیما از مبدا امارات به مقصد تهران را در آسمان ایران رصد کرده‌اند.
🔹
۲ فرودگاه‌ بزرگ تهران از صبح امروز تمامی پروازهای خود را متوقف کرده‌اند.
🔹
روابط‌عمومی سازمان هواپیمایی به فارس اعلام کرد، این پرواز با اجازهٔ ایران انجام شده و این هواپیما با عبور از فضای شرقی کشور به تهران رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/440715" target="_blank">📅 15:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440713">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): پاسخی دردناک به رژیم داده شد و توقف عملیات اعلام می‌گردد
🔹
درپی تجاوزات و شرارت‌های رژیم سفاک صهیونیستی در جنوب لبنان و منطقه ضاحیه که با حمایت آمریکای جنایتکار صورت گرفت، نیروهای مسلح مقتدر جمهوری اسلامی ایران در راستای حمایت از مردم مظلوم لبنان، پاسخی دردناک به این رژیم دادند.
🔹
پاسخی که رژیم جعلی صهیونیستی و حامیان آن باید از آن درس عبرت گرفته باشند.
🔹
بر این اساس، توقف عملیات نیروهای مسلح اعلام می‌گردد؛ اما تاکید می‌شود که در صورت تداوم تجاوزات و شرارت‌ها، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farsna/440713" target="_blank">📅 14:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440712">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
حزب‌الله: یک خودروی لجستیکی حامل مهمات و یک دستگاه ارتباطات متعلق به ارتش دشمن اسرائیلی در الشقیف با پهپادهای انتحاری مورد اصابت قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/440712" target="_blank">📅 14:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440711">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7c1768271.mp4?token=sMw63B0iVRDrdYEP0d96CU5gfZB3JDnTYiptk4a5ZRzR6TWF-R59fKrzq26UYF8WABGpF77KLOsIDUECjDT2Ml7dm2U2zohJwO0mTeF8-oYPLg6fxkOtDdYjj0CWWINd67OgOrPky921zm2FHoInFoMhhE6-iXERimTvFG8EbTHNeeCFG3YoV6q4vfVQOAfZqEb_-fW3lBJrJDrgZMW9-YaUbHaiRLmTORLW7wA9H7uIqaKTQn2rR-3Tf45IR1lRuxzYuwGhNaDBG5JoVufWE0UeLDwhs3BKQEqygTBnDw4pRrGl53e8CgZaFozgd8prI0gq_jl_e0c9J_TLGFzqcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7c1768271.mp4?token=sMw63B0iVRDrdYEP0d96CU5gfZB3JDnTYiptk4a5ZRzR6TWF-R59fKrzq26UYF8WABGpF77KLOsIDUECjDT2Ml7dm2U2zohJwO0mTeF8-oYPLg6fxkOtDdYjj0CWWINd67OgOrPky921zm2FHoInFoMhhE6-iXERimTvFG8EbTHNeeCFG3YoV6q4vfVQOAfZqEb_-fW3lBJrJDrgZMW9-YaUbHaiRLmTORLW7wA9H7uIqaKTQn2rR-3Tf45IR1lRuxzYuwGhNaDBG5JoVufWE0UeLDwhs3BKQEqygTBnDw4pRrGl53e8CgZaFozgd8prI0gq_jl_e0c9J_TLGFzqcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تازه‌ترین تصاویر از تنگهٔ هرمز و کنترل ایران بر این آبراهه  @Farsna - Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/440711" target="_blank">📅 14:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440710">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce31a395bf.mp4?token=Ie9cFlsyJCh5pILdeiWQlzfu-thtttWQ0gN7QzL-XTUOgZvUblHBRYFZ0jjtTMw172YM23T2vMCYMoxdkNmgzdAEFmv2BsjkyZS9tPjnvi1VeMVGFQSJjTZXe7OGOMsmxbXaC_fBlGfj6SV1C8pAePPSgBIdhr15Z05wJHOoqIZaoEFhjecmFhZLYWrTBTNjcGLCN3FOROZhc9soNVW7fw4TPpohOtOANShQOP4MBwKH-S2BTIQASZmcwI6TP2yX0QNBG4R5HFpMtt_hiaIsOnOq9UAYyfL_bU7xY7hImvm00yUiqcbn3OMTuoOy2_kOhjUfWr_FYlqDhWsdkP0GyjEcxFRH5IWCnGpAJMVsWJ8tPQtOqPP6Kr8hNloodJg15QOX0EbBrtFW33m29s-zwenbn0i28HX1CQzghqQ7LdgOPrrTZXjd7nYes4MCQvNqhzYzSKu3IXeGLglfarUFVnsZJPyKxXZnIDAzScKugnP4xHSEveEAbAUowhnxW8GxuTbsz3O55_GcZs4pY-OEq91sx8pLvTeQ_hkYkV4G2Y6NzIbVY6FQA5BpSUfH2GvBdZRt3LRVgzb69EXL44BWMg9lfUf2n9oDxgjQ6QAquwa896mUyDOfyUI8arSx0x_lxAdcOkGtz9HTjOzzcwbJ1N422_K660ejiNwHpASj0IU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce31a395bf.mp4?token=Ie9cFlsyJCh5pILdeiWQlzfu-thtttWQ0gN7QzL-XTUOgZvUblHBRYFZ0jjtTMw172YM23T2vMCYMoxdkNmgzdAEFmv2BsjkyZS9tPjnvi1VeMVGFQSJjTZXe7OGOMsmxbXaC_fBlGfj6SV1C8pAePPSgBIdhr15Z05wJHOoqIZaoEFhjecmFhZLYWrTBTNjcGLCN3FOROZhc9soNVW7fw4TPpohOtOANShQOP4MBwKH-S2BTIQASZmcwI6TP2yX0QNBG4R5HFpMtt_hiaIsOnOq9UAYyfL_bU7xY7hImvm00yUiqcbn3OMTuoOy2_kOhjUfWr_FYlqDhWsdkP0GyjEcxFRH5IWCnGpAJMVsWJ8tPQtOqPP6Kr8hNloodJg15QOX0EbBrtFW33m29s-zwenbn0i28HX1CQzghqQ7LdgOPrrTZXjd7nYes4MCQvNqhzYzSKu3IXeGLglfarUFVnsZJPyKxXZnIDAzScKugnP4xHSEveEAbAUowhnxW8GxuTbsz3O55_GcZs4pY-OEq91sx8pLvTeQ_hkYkV4G2Y6NzIbVY6FQA5BpSUfH2GvBdZRt3LRVgzb69EXL44BWMg9lfUf2n9oDxgjQ6QAquwa896mUyDOfyUI8arSx0x_lxAdcOkGtz9HTjOzzcwbJ1N422_K660ejiNwHpASj0IU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
ایران در حملات خود به اسرائیل از چه موشک‌هایی استفاده کرد؟
🔹
یک منبع آگاه نظامی به فارس خبر داد ایران در حملات شب گذشته به شمال اراضی اشغالی از موشک‌های نسل آخر خیبرشکن استفاده کرده است.
🔹
سرعت این نوع موشک‌های بالستیک در هنگام شیرجه به حدود ۹ ماخ می‌رسد…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/440710" target="_blank">📅 14:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440709">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKmtBS7iErYP1zZWNQzcmdxauQdXf1umflnnW0uFQhQ5ZtcCN5YRPvhECTTEPcV_gQ7IdfAjSAi_U7Ue7qg_pRu0AT0BQD_B4dXV4B4EGLkQCRIBk-dsTC2mjdSRqMkvrGZWXvK402_fIvPWJO0Xir897P7ri06cRtg-o_61HmWa2VdqNvJ7JkosknGT--fpehOgSiY6j38u61Lze8M6UPPzdpwpvvzgwpo4FFP_iD2DO9IAZXj3Gul8I6_92XR_2-APMe3tnSiPK0Vmeg8gl8RFBHpjj3ngkO-qXdq1nMEVVBJUR57fw8waFKxVr9BrlWFioWPZESz45u783AZRlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اسرائیل و ایران باید فوراً «شلیک به‌سمت همدیگر» را متوقف کنند.   @Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/440709" target="_blank">📅 14:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440708">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2cc8dba14.mp4?token=jXpTaj-05Dhx55eGSVQa9atFMQHXfV8Pb-lGymbrn8efWN9pj0IMqfvVbG3-K4yFhir8sEUzuRRGwFncDfuVXetDWGmOrjpFgiqi5w4Uta8vdqgTqu6oH6B6KNdvlaIXnEpVXLs9MqbtGOSxJpA5Sm8reDnVElTDGLMf48R0bx8RO95YZWW4THXRKJdkQ3Qo_x2KDmJrdnL7X3GY8CMJ2E0jguLaF_WtlJQ_mZvfoOIahbV7ybP5vMpe0BYvKIaI1nemJBh-130YXzhBnu3FH5PCWR80bk6r7eorcIrZ34EBYDEyaqiDGB7jVi8iMNKrcZ3CX_3Nt9oMj1UfyG_cd2BTWS0_aFSg_dl6-eGIrVu3mhUJSMtor6rlYVN-MwKMeF8-9uVuv1TKGRe6djSDOCPkpkm0JzsdOyt82AZOABQ8sJidmnsuunxfP75xuHk8H-SdNlDqCck18fSzfMiVO1977rkOQoR080XFPrp-7d5Wc-GYNabWw_MKkcX8GjpTyu0VveH-ZTpBVCXWTVuao4MPXekO99cXS0dByktI4ah03SR9VSAjWmBomi_ZKsVId3rR9rYEkTUN9w42rF8uERUFvDEm0khT8wOrdd8soF-6b5ltrbbA3e-deq4UGK44zFg_7ryFqkIPs9tHu17Lnq4uHrgk95nE5Ha7m4dA6Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2cc8dba14.mp4?token=jXpTaj-05Dhx55eGSVQa9atFMQHXfV8Pb-lGymbrn8efWN9pj0IMqfvVbG3-K4yFhir8sEUzuRRGwFncDfuVXetDWGmOrjpFgiqi5w4Uta8vdqgTqu6oH6B6KNdvlaIXnEpVXLs9MqbtGOSxJpA5Sm8reDnVElTDGLMf48R0bx8RO95YZWW4THXRKJdkQ3Qo_x2KDmJrdnL7X3GY8CMJ2E0jguLaF_WtlJQ_mZvfoOIahbV7ybP5vMpe0BYvKIaI1nemJBh-130YXzhBnu3FH5PCWR80bk6r7eorcIrZ34EBYDEyaqiDGB7jVi8iMNKrcZ3CX_3Nt9oMj1UfyG_cd2BTWS0_aFSg_dl6-eGIrVu3mhUJSMtor6rlYVN-MwKMeF8-9uVuv1TKGRe6djSDOCPkpkm0JzsdOyt82AZOABQ8sJidmnsuunxfP75xuHk8H-SdNlDqCck18fSzfMiVO1977rkOQoR080XFPrp-7d5Wc-GYNabWw_MKkcX8GjpTyu0VveH-ZTpBVCXWTVuao4MPXekO99cXS0dByktI4ah03SR9VSAjWmBomi_ZKsVId3rR9rYEkTUN9w42rF8uERUFvDEm0khT8wOrdd8soF-6b5ltrbbA3e-deq4UGK44zFg_7ryFqkIPs9tHu17Lnq4uHrgk95nE5Ha7m4dA6Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انهدام ۴ هستۀ عملیاتی گروهک‌های تروریستی تکفیری
🔹
وزارت اطلاعات: سربازان گمنام امام زمان (عج) در اداره کل اطلاعات سیستان‌وبلوچستان در چند عملیات مقتدرانه ۵ تروریست این ۴ هسته را به هلاکت رساندند و ۱۹ تروریست دیگر را پیش از عملیات انتحاری، ترور و ایجاد ناامنی…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/440708" target="_blank">📅 14:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440707">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9M9YNgTtSHtR5hyc4Y3nDAT9VG2LaeW58fhFDca-b2V_j500KnGlJCfygS3xmcbTZB7TVvel9hnncl4rDXJpwvrDS2p6fMkMVBNmXOBCaRVO_1-w8pXBXdnxqtao1csiVPnxYAOEHG5vlQez4JP-pU2myrTeDzmmwPk8xLTi92HXUsXrR_OfEuaLwSnTJpnKS531j2-C-YofMZfULzPIZXKA3DPmiOm_8_KYtskXgb-syCGiYxiufMq7Fjj8G9PizeN_kaS-iwk3rJMVKt_ONK1VLD-zCOKtqxbR2x8AqEgZ1DtPC8ZoF0SMvGHM0-r-cgZ67vWXwjMQ35HB5ydZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ای به بزرگی ۴ ریشتر در عمق ۱۰ کیلومتری زمین، مهرانِ ایلام را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/440707" target="_blank">📅 14:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440706">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84c4a04703.mp4?token=gwHwgwIK_RlO1fDZqzhcwg6losYjSJlfNSQ0VivsQ3mMORvVLXWeqc-8qr-AxhTk5F9PA_1hoGk6WB69u5qB6ywG-11TiasUzs6FUbmytw2Bj6Pbjxqrwf4QA7fii1p14uKDOdTBnSLbC6TyEzdJsOloCALNaxo6L8lWuK4H4UEIXGBIWfZKLwepjdn6kxaJCMPCRBxIDUklGDvnA0GCNr-HnVo26U-_mKfqByV0IlC86H8DThi7eaitVnUnfhic1g2_YOR3Qrgu9jK5VqSssDDRNEXBeBhzbTrqppZIOKNnqL0p6vlU3BDpE8jKIuziSruhriOk5sbF8lemOL9tog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84c4a04703.mp4?token=gwHwgwIK_RlO1fDZqzhcwg6losYjSJlfNSQ0VivsQ3mMORvVLXWeqc-8qr-AxhTk5F9PA_1hoGk6WB69u5qB6ywG-11TiasUzs6FUbmytw2Bj6Pbjxqrwf4QA7fii1p14uKDOdTBnSLbC6TyEzdJsOloCALNaxo6L8lWuK4H4UEIXGBIWfZKLwepjdn6kxaJCMPCRBxIDUklGDvnA0GCNr-HnVo26U-_mKfqByV0IlC86H8DThi7eaitVnUnfhic1g2_YOR3Qrgu9jK5VqSssDDRNEXBeBhzbTrqppZIOKNnqL0p6vlU3BDpE8jKIuziSruhriOk5sbF8lemOL9tog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی در نفتکش هندی در سواحل عمان
🔹
مرکز امنیت دریایی عمان از وقوع آتش‌سوزی در یک نفتکش حامل ۲۴ ملوان هندی در ۵۲ مایلی سواحل عمان بر اثر اصابت یک شناور بدون سرنشین خبر داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/440706" target="_blank">📅 14:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440705">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">انهدام ۴ هستۀ عملیاتی گروهک‌های تروریستی تکفیری
🔹
وزارت اطلاعات: سربازان گمنام امام زمان (عج) در اداره کل اطلاعات سیستان‌وبلوچستان در چند عملیات مقتدرانه ۵ تروریست این ۴ هسته را به هلاکت رساندند و ۱۹ تروریست دیگر را پیش از عملیات انتحاری، ترور و ایجاد ناامنی بازداشت کردند.
🔹
در جریان این عملیات‌ها یک سرباز گمنام امام زمان با انفجار انتحاری یکی از تروریست‌ها به شهادت رسید و یک نفر دیگر هم مجروح شد.
🔹
از مخفیگاه این تروریست‌ها شمار قابل توجهی سازۀ انفجاری، سلاح کلاشینکف، سلاح‌های سبک مثل انواع کلت کمری و نیمه‌سنگین مثل دوشکا، نارنجک‌انداز ، سلاح‌ M16 با دوربین دید در شب و سلاح M4 کشف و ضبط شده.
🔹
وزارت اطلاعات از مردم خواسته هرگونه موارد مشکوک را به ستاد خبری وزارت اطلاعات به شماره ۱۱۳ یا درگاه‌های رسمی ستادخبری این وزارت‌خانه در پیام رسان‌های ایتا، بله، روبیکا و سروش‌پلاس به آدرس vaja113@ با تیک آبی گزارش کنند.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/440705" target="_blank">📅 14:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440704">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">واکنش تحلیل‌گران به چالش‌های اسرائیل و آمریکا در حمله به ایران
🔹
دنی سیترونوویچ، رئیس سابق میز ایران در موساد: اسرائیل با دوراهی سختی روبه‌روست؛ یا واکنش نشان دهد و خطر درگیری مستقیم با آمریکا را بپذیرد یا عقب‌نشینی کند و به ایران اجازه دهد معادلهٔ جدیدی شکل دهد
🔹
رابرت پیپ، استاد دانشگاه شیکاگو: آمریکا و اسرائیل بدترین دام تشدید تنش از زمان ویتنام را راه انداختند؛ ایران قوی‌تر شده و این یک شکست بزرگ برای آنهاست.
🔹
هری سیسون، فعال رسانه‌ای آمریکایی: ترامپ دوباره در صحنهٔ جهانی تحقیر شد؛ او ضعیف است و نتوانست مانع اقدامات اسرائیل شود.
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/440704" target="_blank">📅 13:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440703">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de135c17d6.mp4?token=Og_HlXV-LiZjc2HYbD7r8h-vDlsQat9Me-Xg_OK3R1hgka1PvpxfoXCux4tEITJYcjNZH4nt5RjgAQ01Krc65cpU1c1ji4N6wANN_IF95xegFTk1NVxX6olFdqOHdbdyNlrT71vLvuZ8lcYzuI0Ch4ThFGtzng7vj1OCF8hhwgpWyokcr3w1uUMczndXjRWK3SXvDqYr7cnBehp_bJl5_u2ucxTsCNJPKNgXONK2SWsKjiweFd7qm8hXgKZ-lp7ERNbWuQ0fV2ggJob-VT-YKr3ZSSpS-PETr9P_p7EopT4iQSz4KRwmUu1Aikzmdh2RCDhzqjEud890Xy8HPd5HOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de135c17d6.mp4?token=Og_HlXV-LiZjc2HYbD7r8h-vDlsQat9Me-Xg_OK3R1hgka1PvpxfoXCux4tEITJYcjNZH4nt5RjgAQ01Krc65cpU1c1ji4N6wANN_IF95xegFTk1NVxX6olFdqOHdbdyNlrT71vLvuZ8lcYzuI0Ch4ThFGtzng7vj1OCF8hhwgpWyokcr3w1uUMczndXjRWK3SXvDqYr7cnBehp_bJl5_u2ucxTsCNJPKNgXONK2SWsKjiweFd7qm8hXgKZ-lp7ERNbWuQ0fV2ggJob-VT-YKr3ZSSpS-PETr9P_p7EopT4iQSz4KRwmUu1Aikzmdh2RCDhzqjEud890Xy8HPd5HOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
ایران در حملات خود به اسرائیل از چه موشک‌هایی استفاده کرد؟
🔹
یک منبع آگاه نظامی به فارس خبر داد ایران در حملات شب گذشته به شمال اراضی اشغالی از موشک‌های نسل آخر خیبرشکن استفاده کرده است.
🔹
سرعت این نوع موشک‌های بالستیک در هنگام شیرجه به حدود ۹ ماخ می‌رسد…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/440703" target="_blank">📅 13:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440702">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FU0rpkZmYssXr9cvdhCD_n4ZkHrdmZ4fwF_jvoxyw-wq9BIVmrokyrbz6FIY3HTUOoqkiH-TiP0nrOx6KalPw-G29hn7O8XdO1y0YCrJQ76-bTDl-2kqRqluXTye7o8LbZTTB8jW2uMJPiIU7VfBMAroku9l-BiOLC6tYR3Lziir0sJXQEI7hbABciUE2UtWswyKffkJaynwgKPitopaaSpBOaefbHdiH8fpAbuZA3tk4dFVkuHnH5bUTkcXDeBd2y0h2cxYbHYMXcPAB0G2H6N7mzPmMIp2P8WwFbJgNXJRtlBxV0A-32uvuJWPHiew7tRfDGwV508aja6ZU26oKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی کمیسیون امنیت ملی مجلس: تا لحظهٔ پشیمانی دشمن سکوت نخواهیم کرد
🔹
نباید دچار ‎خطای محاسباتی شد. راه آرامش و ثبات از درون جنگ می‌گذرد. اگر خودتان را برای پاسخ قاطع به دشمن آماده نکنید جنگ درب خانه‌تان را خواهد زد.
🔹
نیروهای مسلح ما پس از سکوت صحنه نبرد، بر قوت‌هایشان افزوده و آسیب‌هایشان را هم برطرف کرده‌اند.
🔹
ما قوی‌تر از نهم اسفند آماده پاسخ هستیم و تا لحظهٔ پشیمانی و تغییر محاسبات ذهنی و ادراکی دشمن سکوت نخواهیم کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/440702" target="_blank">📅 13:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440701">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWP7v6P8zxWiOIA4TSMu1KwCV7aE-1xtrWa0agxVkRQPOoV-l8YVcYTNsWcBaHS6QztjUBQ2yYh1Keexds7Z2v-XVfulgCIMH7AWVAeW__DiBD3roOnE4VBr-KGVV7PNk-355gEPiMyv0sMCbUdK6GN_GFNeXmoGAVDUeirHts9itJXYVmbMeKyyB2-z6K3wdYbXC2ZITJUQ-vnIF1IL40vQQVaGf2I_DOkAVyfDrmPHQajdBFFMFED6apCO0Ebkd58SCj4p0yPbNckI6OIEhzctld6MKG3xFP2uaJHVg6LJwWIPEBuGPgFU3ca3ekt8kS-UPKXU0gqddyj_YEqO9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرپرست وزارت دفاع: پشتیبانی از نیروهای مسلح با قدرت ادامه دارد
🔹
سردار ابن‌الرضا: رژیم کودک‌کش صهیونیستی امروز بیش از هر زمان دیگری به افول و فروپاشی نزدیک شده است.
🔹
تا زمان تنبیه متجاوز، لحظه‌ای از مسیر دفاع از منافع و امنیت کشور عقب نخواهیم نشست و تمامی ظرفیت‌های دفاعی و پشتیبانی در خدمت نیروهای مسلح قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/440701" target="_blank">📅 13:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440699">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/837911a19e.mp4?token=ZxIuwbe6UIlzbInrkaLpGTFjc_757bU3w-5ciPScrdHLhctyWRdQeCqfHxgrerDWDXjihpODsQpXhaoeLc1gLj_mxtYqcakXAYI-8Ws0gQ-0TNNdMBRCBdv8tTmKSN2KCnUiUIoTLfN81nA-86e6gy6JuG0V1FL9Rmu4M5tpWmdFGWG9hrUj4g9leBT9GO_HoqSkUCzrjDwD9dR-0fNqlBLO9L1IUr9RNYBK7WevRPTEIikIr7A8qDyNBetdhOJxmkfpYZ0VILUTWMXsEYpD0CxaLzTyqHbK2yBZiBkgQRZ9e17YfiZ1rRfZxaHGA0hsJJPzG1B8BsQ2txiEXDhMdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/837911a19e.mp4?token=ZxIuwbe6UIlzbInrkaLpGTFjc_757bU3w-5ciPScrdHLhctyWRdQeCqfHxgrerDWDXjihpODsQpXhaoeLc1gLj_mxtYqcakXAYI-8Ws0gQ-0TNNdMBRCBdv8tTmKSN2KCnUiUIoTLfN81nA-86e6gy6JuG0V1FL9Rmu4M5tpWmdFGWG9hrUj4g9leBT9GO_HoqSkUCzrjDwD9dR-0fNqlBLO9L1IUr9RNYBK7WevRPTEIikIr7A8qDyNBetdhOJxmkfpYZ0VILUTWMXsEYpD0CxaLzTyqHbK2yBZiBkgQRZ9e17YfiZ1rRfZxaHGA0hsJJPzG1B8BsQ2txiEXDhMdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
ایران در حملات خود به اسرائیل از چه موشک‌هایی استفاده کرد؟
🔹
یک منبع آگاه نظامی به فارس خبر داد ایران در حملات شب گذشته به شمال اراضی اشغالی از موشک‌های نسل آخر خیبرشکن استفاده کرده است.
🔹
سرعت این نوع موشک‌های بالستیک در هنگام شیرجه به حدود ۹ ماخ می‌رسد…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/440699" target="_blank">📅 13:35 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
