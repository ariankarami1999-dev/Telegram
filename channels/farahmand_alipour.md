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
<img src="https://cdn4.telesco.pe/file/kAyG8iFHCkRzAq93ck83Zy3JcYaUprpimvrD-o0m5yGf0zooCjBz2my6cx1eCGd-4d27nEgAH_2ZtxM_FIC_SiCCYbt4GuNjgDWA7-Hdxd_s01rTYe5uEOmKMyT3zaXe7KynCG3MAGeOFxscJYztXqCD0kEksRdGC-3cZjbuXfTMm4NB-5tPFkfxWsAfeiZYWBGHUIFHR1QG9Qnk94bzy7O47N4F_89YoVW4UaFnP__gx3Z9AmK2cw2TiHDSgcnW5mkauwEh9dif6eL4JNYlavS4cGePLvEN59vr2Do2HaOkWSp-oz8VJpYR2mIvK3mmqtnM5J56p_AuopbYVYqiIg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.6K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 20:17:37</div>
<hr>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sq936ugl26sbwnyE8iB79fB7noR5SqHorlpTfEf4JWFcR4T8eaoDeYDG48FmljMzDqMRdMtFNeDSPO-OZuF9ZWCiPlunWVwEFQ48jb_HekziTxJDe8_xWOvuAoKcAPb1J_lZ3JmWM3F4ZXLbEccpXTzdxcw3O8Ykkk6FTIjNQ_wNYvvaawlMT0YMXXFwwD2PX-MScveol36gyZ1r1mGap2XVtIqv0MwGzLZvWo7DsOligRE2Af1fL4zaL5yYb37mvqLPOC-y3qfiEdAvsU--D3Wn10-8zc-pgGSo9zt1WJVytyvxbqwwYeia-8BK0elWrmaO8DheQlBRJhAKLBC24g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/5303" target="_blank">📅 15:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrEErn4I8PA5ae7z6EX7OpfecACK_ZIqCfiMArF47makxsbpt4g93RtkpF_w7L6BxKfuur2NYaiEjQlPMs5pAZUZ0mqYjIN8RN07SlcCqMxCXoBxgAXUDQPT0zj4x8XOxO7-_okcLe3DAuOjaeWXxPT7WBGIfOZsh8VgJv9PmZ9lIoVO9O1fRHpeJDZcPcgCSAHdTyFycZ1GlkeV-dAFadQaKkGCv9_4oZ_ZObQUFeBxQ82A8-8xvowmF2ZUPOQjHY97V4vVxbaEjL5XUev72Epo1IPn8QZsXWklHGeW2Q0jIaHdBpQh0sS-kwvUKyCMbw6DrzIdaMHYycn44n0sWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به این بخش از نوشته نادر سلطان پور که نوشته بود : «فقط ایرانی می‌خواهند آن‌قدر ضعیف که هیچ‌گاه تهدیدی برای اسراییل نباشد.»
پاکستان یک قدرت اتمیه! ترکیه ارتش بسیار قدرتمندی داره، مصر هم همینطور،
چرا دنبال تضعیف اونها نیستن؟؟
زمان شاه هم ارتش ایران بسیار قدرتمند بود
ولی مشکلی با قدرت  ایران نداشتن!
بهترین سلاح‌ها رو هم بهش میدادن!
پس موضوع «ایران» نیست! رژیم حاکم بر ایرانه!
چرا با جمهوری اسلامی مشکل دارن؟
چون اونها سیاست شون رو جنگ و نابودی اسرائیل نگذاشتن! افتخار نمی‌کنن
که به گروه‌های تروریستی سلاح و پول میدن!
این چه ناراحتیه که ما میخوایم تهدید باشیم برای اسرائیل و اسرائیل و حامیانش مخالف این هستن؟
بیان کمکتون هم کنن؟؟</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5302" target="_blank">📅 13:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvsN94JSKqsljx9mgbDBRgV_llqF_WAaZnBseHlLELQKKJ3ws65dQqANeVtfIJlnDw9bUkamsXNJMxX4eg__jKNzrsB0NVBfezZhjqJtYhR-RnVEK9Ckf5mA_EDe2PbsO1jc5aPs8PmMOp7tRRFSZ96-ank0yI4ROcmu4mFjI_To5cjVmnd47taemzRA5xmbn_UiuMpRST9nNDkzN5Xvrk5AnGgzG21bPRm0MWUsQeVO7Io2NPo7jATmNBZmLQjg97FZaJOthxu6wfddjrAGzlSlU93BlZwS4XZ0OI1MIJCBBo2EDJ72Ws3dw1s08pVb6fNIhm7-33CJDgroWH2PcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی در ۵۶ سالگی درگذشت.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5301" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تصاویری از فرودگاه کویت
پس از حمله جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5300" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPQwDsb8e5BbH1hHBk83pdT9vAG1x79B7h0LBynwZ8NPcttZT5t3RZopf3hiWBBIv7zpMES_kv-3AWxgm-ma703Uu2nAx4--3HQ5b5KK8QyprJYZ9Ft5P5S97-VAKMwUo-QsunXTOQ7KcmsjlmuzbaVXvSL1sfB4EfGoOvbt6jf_AiZTzFWg1_G0QFq4aDz7AkSXX1ynXd6PIOxsZVA2dbUQrB4xdLPIEoldADTVvkmYTF9u6DhTZmrAR6os34aoVIF3XBtbtST4oRCo3oUSJlUc00N81jLobAJ0zjLd2Nj7V9Xw9yrxeItMrKQxrMm4ynMaC8bhmRAJY5cnOCQO3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5299" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oc7NeffMHacldACBXwHgF5KB9SWjsA0sz6BxNQeeGnJE-jIxQlN9t2ErNgCfzeUItF56PxYjnHLcBuelWVdoGpaz1osWXqIdC7EfeKEE5uwz1T8dONu3kkzI1TBluBsnmvHxLKqmiyauifcRfTzMUhcRTWmaWynDqTor0yBJcRh3JrIXAu8Pc-s0wEi7jxEIWhYsYErpmZwhHuX8CYUWGs8mQdF2qt9y-Oo-5BgiVAFlA6afJTyFra4MDCbMncbOYi8b6pcPSahlaJYSjrN77QaZhCM7H4bMRL8PcC3kVzeH2v7OI9iex9515vHqU-mH0Rvt7oZ0_c_FYX-z5VjIiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کویت ضمن احضار کاردار جمهوری اسلامی، دو دیپلمات جمهوری اسلامی را به عنوان «عنصر نامطلوب» اعلام کرد و از آنها خواست تا ظرف ۲۴ ساعت خاک کویت را ترک کنند.
وزارت دفاع کویت: جمهوری اسلامی امروز ۱۷ پهپاد و ۱۳ موشک بالستیک به سمت کویت شلیک کرد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5298" target="_blank">📅 16:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=jS4xDj_c3i1C68Pcam2LBwfQmnXNDiev2N4uUr6TZiO9H9g08Xq0HEHulBbRBrLUuGmVpEtI9rjZT489BRNPmDGD0eLvnV26JaBhV4w9Sl7RioKil7EISKJw1bAZeBh6ljy9PEfgXepm4syKc0DFh7--qTy4Gv1Uc-uY-h1tPlSyiRAVWE9hP2r_7DnWC1_V5WmMlSAiWhYywhOXNosv4C5W24bQ7qLSEErXltmvqHJ71xPizwMq_K2M0mVYPRRW-dSLrabmpJLo7l0K1NdqTl0qKbPM9Kh-szBLfQ9rvCpYgu1MwOP_vxq5VZ9dgxyApKnq9VwjgBRO1YD6sWmOaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=jS4xDj_c3i1C68Pcam2LBwfQmnXNDiev2N4uUr6TZiO9H9g08Xq0HEHulBbRBrLUuGmVpEtI9rjZT489BRNPmDGD0eLvnV26JaBhV4w9Sl7RioKil7EISKJw1bAZeBh6ljy9PEfgXepm4syKc0DFh7--qTy4Gv1Uc-uY-h1tPlSyiRAVWE9hP2r_7DnWC1_V5WmMlSAiWhYywhOXNosv4C5W24bQ7qLSEErXltmvqHJ71xPizwMq_K2M0mVYPRRW-dSLrabmpJLo7l0K1NdqTl0qKbPM9Kh-szBLfQ9rvCpYgu1MwOP_vxq5VZ9dgxyApKnq9VwjgBRO1YD6sWmOaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«وطن کجاست؟  عقلا منطقا نجف»!
وطن‌ پرست‌هایی که وطن‌شون لبنان و غزه و عراقه
و میگن برای غزه و لبنان حاضرن ایران بمباران بشه!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5297" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کویت : در اثر حمله جمهوری اسلامی به فرودگاه بین‌المللی کویت ۶۳ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5296" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بخش بزرگی از انگیزه جمهوری اسلامی  در حملات پی‌ در پی به دوبی را باید در عقده حقارت جمهوری اسلامی جستجو کرد.  شهری که برای ده‌ها میلیون ایرانی  نماد پیشرفت و توسعه بود، که ظرف ۴۰ سال از هیچ به گوهری درخشان تبدیل شد،  و مردم ایران دائما دوبی  را با ایران  و…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5295" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sB_h4J3ajcoo4MrVzxNnvIjZUBixGq4zulHGegUyYGdHTLtT08E8jz1W3XA4nhedTJXUXZWsKcx-VXtnZDAXFVAJxBdLyXNx1sX-GoNNCS7aYJg2SK-GbIy_JrwSAJWWpce_7UAeuUcH_ostBsPebiMTaL-bTQFd0-rtsV9UaVEgIVjTkdL1MjHlQBbAjxauPIkXTwXeORUX11K_7InXaxp1n9H2GBU1MXU-UflyhuZuQsx_hnAlTOeKCI5negBKzE-2yvdArIk5VOSS4wJL5y2GNByr4qSp2Ers_fLzM9VBrWwJGM7QUW4KM2VdxHnWBGn2LX9fTtRw7zR6G2v7OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/txebbeCzWXayH7eLVE4yIwEMmL7Uh2PuOzRC_NOnMGf7GLsQnq5QBFP4zbgqEmGuDiTVp2I2CuMZ0gDjeyBVblQVx3NanEpZ7KzOP1KpynPUd6QAmVlSi6HpPFVm6YRcxyrSCZLuSRQS7IAYGTOh-570c8kvHdHIKf0NAYCqi9sGg-d2n_va8_CDF5EI6d93VjsT8rRyViWCKv_8vEG3vmaCNiZuaUC4dH7YOPLPJBFL0peL9AprG5iX5Ayj2KH5_5BFvIwye2ekcu51pbWM8nxU3d847DEXziNTFzOWpIa9Znt0S_BjwDDcPPPdAOCPnG_iGIzep-owdqqHiDUgRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XuF6JUawgeSKBR1h4twdsPkVJj_xAbhBdm2oSyebFqXm6cvM-Oui7McAps9oRK5NkNvgGTT2ckO05Vwz3Kq1NIuOzbPHZaXH2njUWyfPUWvgyrH72Nb2WYc2bPv5CXU96nzBOewKFTIbjKTuyGOsqxGQhZbI6D3GggBOKkf4Ht9NSEhUaDG7UlkLXTen2g5E_6BFkeqk9M1oAiTk2OrBi070VYdl_R51vK8YeKTqJl9FAIw1WPenHFMFwTHFvdf22ewuMN_1ytmQsPlEwiO2I3Z0XjoRS2tfY26ltP1IO_pyHt24aRSpvJ1Hrlvs23hJFXyPfPaI-QcnI1BzTOw7ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درست ۲ روز پیش کویت ترمینال شماره یک اش رو دوباره بازسازی و افتتاح کرده بود،
که جمهوری اسلامی دقیقا همین ترمینال رو دیشب با موشک زد!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=qFuhHKhLSnnYEpXE323cfmbGwT2if47uWk4Y-wFLXBN0Z3D2O8DZdYokB8060_r_oaETIVqjq63WTqT-dI7FxbUVNboElcL7v4sGTaeMLjAkrgPH8FzqlLq-niTlyiJUa-WRM09i_nC6A0JiS7HK5SFPeTPM4ZMqPL_d835CJOTU1i2tDJjdut1eCQpwTtUPtlY5lGNmjuJfGjaFnaIcv5BvHZ2h8bFIzNOR4JhP6YictXG6YSiVvFkj-Zu-fAuKufXFAg-Z2dxN11JMLpaxZXYfqKjHS-K62BUrPFevUpz6pFXMKF2e8PLvHC5gS2NgLHf5u28Epx9Toe87GEPORg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=qFuhHKhLSnnYEpXE323cfmbGwT2if47uWk4Y-wFLXBN0Z3D2O8DZdYokB8060_r_oaETIVqjq63WTqT-dI7FxbUVNboElcL7v4sGTaeMLjAkrgPH8FzqlLq-niTlyiJUa-WRM09i_nC6A0JiS7HK5SFPeTPM4ZMqPL_d835CJOTU1i2tDJjdut1eCQpwTtUPtlY5lGNmjuJfGjaFnaIcv5BvHZ2h8bFIzNOR4JhP6YictXG6YSiVvFkj-Zu-fAuKufXFAg-Z2dxN11JMLpaxZXYfqKjHS-K62BUrPFevUpz6pFXMKF2e8PLvHC5gS2NgLHf5u28Epx9Toe87GEPORg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c026494834.mp4?token=SYfe5TGmTxzxBPtHFMaA284xFIDzACzCAeaWMsElGnoc8i0CRaXCxVUYPpAV_-L6Y_k4ht7kRyLTkTJt6B6syU8sVm8WxOKo3xQvtWNmxXp-HdoAdQy9rz2wkcD8j-N49R4_PrQVhc7ro6Q0JaHlfk4g0AuLE_eqJZxuKnxirYTvtITnt9PvkRTNOToZ_UHMouRn0ae43acrHK9RGO234Ryn0UknOJUgJElABgedHqThsssg3m93kGXnt7xRoHdWAqALnSf6TWTcwx00t-wbgVHCd_smEeERMuFXHv2zwoFrjm966lvvQKn5nZZSjPh-_MV93GflC2Z3Cw4dsBKAKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c026494834.mp4?token=SYfe5TGmTxzxBPtHFMaA284xFIDzACzCAeaWMsElGnoc8i0CRaXCxVUYPpAV_-L6Y_k4ht7kRyLTkTJt6B6syU8sVm8WxOKo3xQvtWNmxXp-HdoAdQy9rz2wkcD8j-N49R4_PrQVhc7ro6Q0JaHlfk4g0AuLE_eqJZxuKnxirYTvtITnt9PvkRTNOToZ_UHMouRn0ae43acrHK9RGO234Ryn0UknOJUgJElABgedHqThsssg3m93kGXnt7xRoHdWAqALnSf6TWTcwx00t-wbgVHCd_smEeERMuFXHv2zwoFrjm966lvvQKn5nZZSjPh-_MV93GflC2Z3Cw4dsBKAKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی
حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxKOHkyAEiaCs7V2GZO-RRWzDx3LC-9GXbWPpK-qAOLBuInmp42-qIams4ncYwDzhxR7uvXtcgPpJJoZbIFpa9sV4PanMaAIpgiFOGqTozeLl6yBBVHwE_NJh5k9sZF4jQE5cUQOSUrWjMT0M1h-QD3130EvzZDcqIpuHk7R5b8kOosSk-E03USLxhGmY5wX8iX4renn2KbWtetMte8wQUxuh4Wn45-BuTqe1qFTzELGgdzQ_K5bOd_qnSoutXgwHpwm3C1i6HXgybMSiLua2uCO-2OWEIKjXm3hY1WwZUyvyHl4SJKsgR_5l4aO0msYiwI1Ak17JBLbcGLv8oF7a1FU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxKOHkyAEiaCs7V2GZO-RRWzDx3LC-9GXbWPpK-qAOLBuInmp42-qIams4ncYwDzhxR7uvXtcgPpJJoZbIFpa9sV4PanMaAIpgiFOGqTozeLl6yBBVHwE_NJh5k9sZF4jQE5cUQOSUrWjMT0M1h-QD3130EvzZDcqIpuHk7R5b8kOosSk-E03USLxhGmY5wX8iX4renn2KbWtetMte8wQUxuh4Wn45-BuTqe1qFTzELGgdzQ_K5bOd_qnSoutXgwHpwm3C1i6HXgybMSiLua2uCO-2OWEIKjXm3hY1WwZUyvyHl4SJKsgR_5l4aO0msYiwI1Ak17JBLbcGLv8oF7a1FU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسام الدین آشنا، که قبلا معاون ویژه وزارت اطلاعات بوده، طوری وضعیت رو ترسیم میکنه انگار ترکیه فقط یک فرودگاه خوب در استانبول زده،
بقیه کشور رو رها کرده! اما جمهوری اسلامی
در همه کشور فرودگاه زده!!!
ایران ۹ فرودگاه بین‌المللی داره!
ترکیه ۳۷ تا! چرت و پرت!
یه جوری میگه ما همه جا ریل و قطار داریم
خب پس بیا بگو چرا مردم قم، اصفهان، شیراز  و…..
برای سفر به تهران باید یا اتوبوس بگیرن
یا خودرو؟ چند درصد با قطار میرن؟
۵ درصد مسافران با قطار میرن؟؟</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5289" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fspQNsc5OYvFA62CuA3V6HUzrKr5w4d7OlMNtZ1cGgb4ZQo5nN5LGZAkDa9nFb3tFERQkCO0La9GIdb8IGQnQ2TebATHpQM98gymZsbF67ZRUDLLBsLQOjBbGjHHuzCCyz3ec4i8AU-O-mnh1S_VsjT07wjSZ1UK44WAbs-TcGrWpE_uIKyRRzaa_oIP34ueiyALfetcLwNvjXhQal129fQHBRqoU7wibpjom4LXn77nKmJhnPAa4K2PrsSSkO-3f2OBKEhDOuDp7xl3C_UzEPgkqMulEFSkTZmS9FuLXaLm9RsMpfbux1dYNq3cEnC0HomXc4hJNcf_S9p9EDWHsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت ۸ صبح حمله صورت گرفت
(توی روضه‌هاشون هم‌ میگن رهبرمون گشنه و تشنه بود! ساعت ۸ صبح!)
اینها همون بگیم ساعت ۱۰ صبح فهمیدن! اما دائم تکذیب میکردن!
نیمه شب به وقت ایران تایید کردن،
اونهم زمانی که ترامپ و نتانیاهو با قاطعیت و رسما نوشتن که حذف شده!
اگه این دو نمی‌نوشتن هنوز میگفتن خامنه‌ای زنده است و «کمین» کرده
و داره رهبری میکنه و…..!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5288" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFeDPsRT5NZUqrTUVA6Vfz9rtxtRVDiM6A3gdGyWmjN0ndZmnctFVZuLN1j_1hXm-sp6jJigmg__vXtQz9misQ5VGQOvkCJxrlP6zkgDCt8hFsGlWYaKJ4VA4Fiu66GgC3uVn4ZKVqjx4ALOx5kWeixkqU0aSTos6Ma4TZzNzVsWwupAqmPJlXIj_c8EL4v0qeqUtHvmJAHIeluuM6GYg8BSkaEjsSnt0m6fncOL5Vpa0CH2WFItvP9VQbU7Oeg97fOTx81dpwtsPMD8UX-WTOenHn66eUnF_4Yi4vteueyUmJjw29GY9DymGtLC6U5_TlVnuUtDB3Wjk2ceFgna3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015500535c.mp4?token=WEJ2hfUbnb1CGi_4xA80dLU4NaVnyuruFoVq4pqvSj1_nNzYdkSljy8g41jzcV9HvhivmveBs1jum0oTjQDRSkobwimfu8RFUoHQK8iz-Z81jos9roaffv3Ntp2L9fR95PjbEx8DJL092MWFzqF74_PdR9xpTTJka5qPmfN44GDlDV81dVMhHmeywSN3HvkTIEMIm5bfSjYisIYuGTeQt6kv4dnQKXpQZTWwLOYgh_mo2Fc49u5WXE8eqFMsQTfwFrOS2xZMqV26aJAR5jzPpRQYcXgGcn09r6IkaZT7D6HfZCGW4-t3-w0hJxhcagGiWPmk4XYiFZZlr3EeoWZPwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015500535c.mp4?token=WEJ2hfUbnb1CGi_4xA80dLU4NaVnyuruFoVq4pqvSj1_nNzYdkSljy8g41jzcV9HvhivmveBs1jum0oTjQDRSkobwimfu8RFUoHQK8iz-Z81jos9roaffv3Ntp2L9fR95PjbEx8DJL092MWFzqF74_PdR9xpTTJka5qPmfN44GDlDV81dVMhHmeywSN3HvkTIEMIm5bfSjYisIYuGTeQt6kv4dnQKXpQZTWwLOYgh_mo2Fc49u5WXE8eqFMsQTfwFrOS2xZMqV26aJAR5jzPpRQYcXgGcn09r6IkaZT7D6HfZCGW4-t3-w0hJxhcagGiWPmk4XYiFZZlr3EeoWZPwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت ایران از عراق بهتره؟
این روزنامه جوان متعلق به سپاه !
در خصوص زنان ایرانی بدون سرپرسته،
که مجبورن برای سیر کردن شکم خودشون و بچه‌هاشون روی خط مرزی بین ایران و عراق «کولبری»!! کنن! در کوه و دره!
چون به این پول نیاز دارن، بیا بگو چرا شهروندان عراق، که روی همین خط مرزی هستن،
نیازی پیدا نمیکنن که دست به چنین کاری بزنن؟
اما زن ایرانی بدون سرپرست نیاز پیدا میکنه
که دست به این کار بزنه؟
تازه میگه بهمون گفته بودن به روستاها برق نبرید!
دستتون درد نکنه چه منتی!!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5286" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">وارونه گویی!
به خاطر دشمنی با اسرائیل رفتن دور تا دور اسرائیل گروه‌های مسلح ایجاد کردن، پول و سلاح دادن، حماس، جنبش جهاد اسلامی، حزب‌الله و… تا دائم با اسرائیل در جنگ باشن، خود خامنه‌ای بارها تهدید کرد و گفت «کرانه باختری» رو هم مسلح میکنیم علیه اسرائیل!
حالا که اونها برگشتن حمله کردن، میگن ما اونها رو برای دفاع ساخته بودیم که بهمون حمله نکنن!!
نه خیر! ساخته بودید که حمله کنید! نه دفاع! که هم اونها رو زدن، هم اومدن سراغ خودتون!
و الا اسرائیل زمان حکومت شاه، با ایران دشمنی نداشت! جنگی با ایران نداشت!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5285" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‏روایت سی‌ان‌ان از درگیری شب گذشته ج‌ا و آمریکا در خلیج فارس
‏ایالات متحده و ج‌ا در یکی از سنگین‌ترین شب‌های حملات از زمان آغاز آتش‌بس در آوریل، دست به تبادل حمله زده‌اند
‏به نظر می‌رسد درگیری‌های شب سه‌شنبه زمانی آغاز شد که ارتش آمریکا با استفاده از موشک هلفایر، یک نفت‌کش با پرچم بوتسوانا را که به سمت بندری ایرانی در جزیره خارک در حرکت بود، هدف قرار داد. به گفته فرماندهی مرکزی ایالات متحده (سنتکام)، این کشتی با محاصره دریایی بنادر ایران توسط آمریکا همکاری نکرده بود.
‏در پاسخ، ج‌ا اعلام کرد به یک کشتی با پرچم لیبریا موشک شلیک کرده است.
‏اما تشدید خطرناک‌تر پس از آن رخ داد که آمریکا یک ایستگاه کنترل زمینی نظامی ج‌ا را در جزیره قشم، نزدیک تنگه هرمز، هدف قرار داد و این موضوع باعث شد ج‌ا به کشورهای کویت و بحرین در منطقه خلیج فارس موشک و پهپاد شلیک کند.
‏ج‌ا اعلام کرد که «یک پایگاه هوایی و بالگردی آمریکایی» در منطقه و همچنین مقر ناوگان پنجم ایالات متحده در بحرین را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5284" target="_blank">📅 09:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خبری که ایتالیا رو شوکه کرده:
یک پاکستانی در جنوب ایتالیا،  با ریختن بنزین ۴ نفر (۳ افغانستانی و یک پاکستانی) را در یک خودرو به آتش کشید و کشت!
https://www.instagram.com/reel/DZF42fzqtho/?igsh=aTJocnQzcWw5dWVj</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5283" target="_blank">📅 08:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سنتکام : حملات موشکی جمهوری اسلامی به بحرین و کویت ناکام ماند. موشک‌ها رهگیری و منهدم شدند.
به اهدافی در قشم حمله کردیم.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5282" target="_blank">📅 08:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lclN18-BgnjHlbN3zDaQZwRI7oXYWmiAz-OEKylgNo1Vv5iUb_uqvfI7JoKIaLtEh9TaWmGZLoli_J9KwU9o-e5Dh43brHDo3mHVBNegMn-BUY9I2bTijTrZsV6MVKK8W8mUyenzw2wZOf2ZwSHcKa_M5SHgDIANas0d5O68L6taqpqUjjULxCY9dYfdFF5ULWoic8IM_xCa4OWtsPy1DEXrtBKLNb3lPYf126TrU7boAN-YVgB9A6816jm5VOmhI4C_CvHPf6eCCGEKXSTI0W8A9zn6_kjyk93Ase43JyI5-54qjLskKFQUT88ilEoY2UonxYzeueCA2CqW26T99A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم اعدام برای دو برادر دو قلوی یتیم فقط به اتهام داشتن تصاویر ساختمان‌های تخریب شده در تلفن همراه</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5281" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجارهای تازه در قشم
🚨
فعال شدن ضد هوایی در عربستان</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5280" target="_blank">📅 02:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله ج‌ا به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5279" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
حمله موشکی جمهوری اسلامی به اربیل در عراق و به بحرین!
حمله مجدد موشکی ج‌ا به کویت.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5278" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=Y1GnSZsPcMCFuqssqwr-dZqsFL_nFSJoLU-BAGQv7X6lQB4gPlYdhAXq9It6rCALOQaibblfDWCYA_NT43Az-Rkk0i5DPQu_6Vy2zU1bCr7MSXzRDhpa3boLc0-Gk_zBzYmFA01DfEiflkMU3d7g38F6Mqgl1VIHa9vkGTaf-yAzaXaSii6ByMnhsb2p0bEUGe6rHzIiBTmqeLu2I3aT7BY-3YRtd_dTql9Eo9bHod8mV3mtb4gVAyQo45Q9uKEKlX-6-W2XX23lGnFIYpqPSERrrqtia8H-fn1-32gKkLpRUQNXjC6xV2CMyhs5PUyR_g7xxCkX1xQNtixqjRp-0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=Y1GnSZsPcMCFuqssqwr-dZqsFL_nFSJoLU-BAGQv7X6lQB4gPlYdhAXq9It6rCALOQaibblfDWCYA_NT43Az-Rkk0i5DPQu_6Vy2zU1bCr7MSXzRDhpa3boLc0-Gk_zBzYmFA01DfEiflkMU3d7g38F6Mqgl1VIHa9vkGTaf-yAzaXaSii6ByMnhsb2p0bEUGe6rHzIiBTmqeLu2I3aT7BY-3YRtd_dTql9Eo9bHod8mV3mtb4gVAyQo45Q9uKEKlX-6-W2XX23lGnFIYpqPSERrrqtia8H-fn1-32gKkLpRUQNXjC6xV2CMyhs5PUyR_g7xxCkX1xQNtixqjRp-0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امشب جمهوری اسلامی به کویت
و انهدام موشک‌ها در آسمان کویت</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5277" target="_blank">📅 02:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سنتکام:
نیروهای ما یک نفتکش خالی را در خلیج فارس که به سمت یکی از بنادر ایران در حرکت بود، متوقف کردند.
نفتکش توقیف‌شده توسط نیروهای ما، پرچم بوتسوانا را برافراشته بود و خدمه آن به دستورات داده‌شده تمکین نکردند.
یک هواپیمای آمریکایی با شلیک موشک به موتورخانه نفتکش، آن را از کار انداخت.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5276" target="_blank">📅 01:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ارتش کویت : حملات موشکی و پهپادی به کویت.
برخی از رسانه‌ها از شلیک سه موشک از منطقه‌ای نزدیک شیراز خبر داده‌اند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5275" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
شنیده شدن صدای آژیر خطر در کویت</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5274" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر :
شنیده شدن صدای انفجار در محدوده جزیره قشم
‏بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است.
‏
‏بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست و هیچ‌ یک از نهادهای رسمی  نظامی و انتظامی تا این لحظه درباره علت وقوع این صداها اظهارنظری نکرده‌اند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5273" target="_blank">📅 01:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=F-kMk5ML1eVwtlKNV-WdjRFdWTieeYwpz576IBR63ms2ZgHMpBJt2cbxMl8YdDdfTewyVhnKoGz4AmNIFcl6Kj7bp7PuDTYhokfz5QHCPXn1mtXO9v8wYysrBZTedakN4iaGOatL7L0YRqYqhTbAVFnEjdbwpnyA4F3Hyl3AZtYOh-Z7LyWrMc44bSfREpxuKP1YOYzububIwyNDS2SbhnGr_7_XhBShU69RG6TRtZfHmYjBe-f6z7CnKCCBn857EJnBEBl6Fan_y_pGsgq5J107cPvUK_jMk2-iTKCuymRGsVWoE2qW7H5CApQAx5J4i6g8ehIhQhG8SYpE5DSKWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=F-kMk5ML1eVwtlKNV-WdjRFdWTieeYwpz576IBR63ms2ZgHMpBJt2cbxMl8YdDdfTewyVhnKoGz4AmNIFcl6Kj7bp7PuDTYhokfz5QHCPXn1mtXO9v8wYysrBZTedakN4iaGOatL7L0YRqYqhTbAVFnEjdbwpnyA4F3Hyl3AZtYOh-Z7LyWrMc44bSfREpxuKP1YOYzububIwyNDS2SbhnGr_7_XhBShU69RG6TRtZfHmYjBe-f6z7CnKCCBn857EJnBEBl6Fan_y_pGsgq5J107cPvUK_jMk2-iTKCuymRGsVWoE2qW7H5CApQAx5J4i6g8ehIhQhG8SYpE5DSKWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.  پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5271" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5270">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=oJy6dDCvE_meahkJAU5D8zer41Er_KeRcJzki9XuAwSfqdjZGd7E1fhDyy7tK30jVsZIh3MW7FuRmgOst44bjX7jBfLUi3dXmV2yZfOW7ovvQMNbEzZ_wNwuCIKzpdKdWgsmHN0vTQ5pbyQ4_BE_pdtQi0W4ZvYaq7FT6PtoE3KjQSD8p4m5zCvnqIvy45_UVDvHt9Vb2nDfKvbZGwrTiZSs_igotJ95hkjPJNbAQd4VKyRcvuWKsxb_9TPz-SE_1niNeBk_ff8z9GivjdyEWgnE9PJWPt-etiDgbBbBOxft4NOOcK-4PokXhDeBffGzuQbRcFVzBWQ72RF5BOsDiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=oJy6dDCvE_meahkJAU5D8zer41Er_KeRcJzki9XuAwSfqdjZGd7E1fhDyy7tK30jVsZIh3MW7FuRmgOst44bjX7jBfLUi3dXmV2yZfOW7ovvQMNbEzZ_wNwuCIKzpdKdWgsmHN0vTQ5pbyQ4_BE_pdtQi0W4ZvYaq7FT6PtoE3KjQSD8p4m5zCvnqIvy45_UVDvHt9Vb2nDfKvbZGwrTiZSs_igotJ95hkjPJNbAQd4VKyRcvuWKsxb_9TPz-SE_1niNeBk_ff8z9GivjdyEWgnE9PJWPt-etiDgbBbBOxft4NOOcK-4PokXhDeBffGzuQbRcFVzBWQ72RF5BOsDiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=NoFszqOnS8z--kF4mm-4tMsdpvXJgzA-hkZQE3Xq5IL61njc5pu406OR-cD0nVMYksL-T1eVi_76Pile9zmp1bmIV9pevadA_6WdGJ0PkrwZr_JTbv12Vn3W5q18BFOl9suEtmR3vz24D_fwofVco5JcqiU0jTvZrfxPLy3LUrQeUHKyIaRwxDKid5FAswxAVDNf29JcgY4ztzoxRAMIvIZFvjEzPsF5HPryHZwB1li-d2vZJp6o5WUt3-D0nct7F3i_ME4kfluiQF-0ZJKvAI-dCo4kl68vx0AtsRfr8O6wMm-Sbq9fVkxlZW1jDscogQyGJFDDHMERAqnY4_7Mgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=NoFszqOnS8z--kF4mm-4tMsdpvXJgzA-hkZQE3Xq5IL61njc5pu406OR-cD0nVMYksL-T1eVi_76Pile9zmp1bmIV9pevadA_6WdGJ0PkrwZr_JTbv12Vn3W5q18BFOl9suEtmR3vz24D_fwofVco5JcqiU0jTvZrfxPLy3LUrQeUHKyIaRwxDKid5FAswxAVDNf29JcgY4ztzoxRAMIvIZFvjEzPsF5HPryHZwB1li-d2vZJp6o5WUt3-D0nct7F3i_ME4kfluiQF-0ZJKvAI-dCo4kl68vx0AtsRfr8O6wMm-Sbq9fVkxlZW1jDscogQyGJFDDHMERAqnY4_7Mgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در میدان انقلاب تهران چه شعاری میدادن؟
نحن جنود الدین و العقیده / لبنان لن نترکها وحیده
ما سربازان دین و عقیده هستیم،
لبنان را تنها نمیگذاریم
(همون لبنانی که سفیر جمهوری اسلامی رو اخراج کرده و میگه این جنگ رو جمهوری اسلامی سر لبنان آوار کرده)
فردا که جنگ بشه میان میگن :
موضوع ایرانه! تجزیه ایرانه! برای خاکه!
رستم تهمتن و آرش و شاپور و…..!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5269" target="_blank">📅 17:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">حالا اینها با همین سوابقشون!  بزرگترین حامیان غزه و … هستن!  دوستانه بهتون میگم، روایت فلسطین و مدلی که جمهوری اسلامی  به خورد همه ما داد، و اینهمه براش هزینه کرد و پاش پول میریزه تا همیشه جنگ باشه و خصومت باشه و…..  نه تنها از بزرگ‌ترین دروغ‌های یک طرفه …</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5268" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWTc0SrlGNkT9Vcav7liO3pdh1goudEtPVlpTTwcHfUG9ww-pRLvhU5tjWKhK75f1WWa234oz-0kDIQ4iRU0JgbfFAM0bqgD8txdcRqUpGfmFkwfTUZ2v9Vn6yXlZn5MnLgA0m9CH62cDSzOl20BR1P9HL5lxbdvAD0_5RASzUY8OyBi--c8mjBatiyhkf0ii98L4-HshI6MPTiZ34KqXIHZGX6GtUsReeRJlTG3XVDPXBvqccjY2Yj2pgSsdq6OoPWsUs3EOu9Zr60E4eAarxPi_vtBX3PBhhCpr4UgvDPk3Gpo_K4j1Ut9l7_delrCzzhQ27O0HrMn5G7iBYXqTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIBHq7lGDauf1gAH-ZUGx7Y4iABeAZWy_4UhabZCzRkOUvAmynRndXWcpvF9JcJnCjiDPQk6JX2dAfsuGJBVOUCKf2PQTWJnG9BhLHOdPyLXuq6CgD0XFyvVCbnDw2rjErPzfQ8Vje9DzHed8vu9NrtQiT9sl-74lPP8LS0GSulVnC_toX99xk-vdJfuOyr2BBo1lfD0ZdgRpV8HHBdotZQvZ8RmLgBmJ4O4z0DhkMpVML06oDF1W6DulZ9-CCR2kliGRl67IfSRqyFkuICQWH8N8F5eZpbjm7Rl6iRxAR9IH-RtDhNJmvpCImd3o3XmFUG0JoRck-6Cn0gL_doLUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dymnxyAgC-ErUkJw7KgovxMX2vHtV6ZID75lRsMkydjo6cd7XJCYxdH-8soOOrWiIDR9lpKxuW009OidZIDYnHHUz2jgUk0_AFy2L9syC7M-cEukxb_Ngv2bt-YtKfLyK1E_zWiipUlnI6FrBz5ANERiDSDWl_QEv2qDdsWIHpbycc8cMEjtWsIUDmr50CEnMJ6Cg61qZ_WZHs1jiavrr4uE4YDzyaDMbNG8OFkA6QHmbWLK4BMa6gxpv4blqddUfsERs1Dabn2R-rFZrxPftbxOvGk6B58oGJRABthVg2xTK84CJ6TxNUg0BISE-il1zu-ipA707U_45fu0PMTNVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،
وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.
منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!
یعنی از زمان هخامنشینیان این بخش
یهودی نشین بود! و ربطی به اسرائیل به عنوان یک کشور جدید نداشت!
دولت اردن نه تنها همه یهودیان رو اخراج کرد
بلکه ۵۸ کنیسه یهودیان رو هم با گذاشتن مین
منفجر کرد! فقط و فقط «یک کنیسه» رو نابود نکرد
که البته غارتش کردن و فضای داخلی اش رو نابود کردن ولی دیوارهای ساختمان سالم ماند!
۲۰ سال بعدش چه اتفاقی افتاد؟؟</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5265" target="_blank">📅 15:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNTo6xmhBxtDIXnEMoFSZvINMJmZM_Rh2OmKSFGoute8tKM7ilF1bKCucCM6C74gflaVNZsUyjcAfPw3GgDNwmpbMKlsrCdXwxl-JxdlL95JLaeqPDDp6GFDGMTkKDBpjCLnASDaB_BZJZoQ5djz7t8nnsPh8Iu3GLJCZBzvuMKSAZWdrhH4RLSUXhl-imfsFO4fCCTJxXlHSq-GaT1Bx9wi3vU0ZceR3QM6z__Zn3LS7eZrARUqMzE-0w-58mN7xRoIXdhldT2g-_1i_9wJEMvPcVGzsd0PEIrmAHL7jbNHSiPthBNf4Kxa9ZFmh67CZ67Zl-w0K2feHE1KmheYSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ke02sqhWEEGzcvvurkoha-5WaOMzhXNW1nJ0kZ4l9KpnWyw30n0N6BVG3FscWRk4503_uHpkqzamIkMKsDNO318PDKJlWLbQeD3mNa_fGdmSB8uXf_W0yrsAZ8NVI97a966ifrHnsHM33OOCjUYHvA7sJC5S505s0fEh5-xnEXQteu7iJw3SxRjUiKprkH_xuD3Bz37fcOjxJZWtgg-4LH_edydMoh3fysgUGyW4CPQCNs8Mv0TUYNwawkcFhkKm_aEm3tUYxIT-UaBEGUbkjJM7dIhkcqq1V_SJ3_jHnJX-pA3jsekmwjPhsz2Qt7VNRbIsLn6AbvLHB8aakxsAeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usWEB7rWPgSN_OO-xq3jsWqTTqA_5mlxhZJKGfX9rOvr6ZLgqRKkDnXUFluauNkp1oqmZ15EF8NyEngXBrIdGDVVFk3lCetOI3myraMRayW1jZxLunWfJ9lM-SDXB9e-x0X__bi8sGWol3UhMuhHhZkyTfk2YHnicoYNBiQ_Jmz2BkoQa9FHDEgD-Ae-zKHlQ_lv74JRJGwdouI6TTzr2em6yOO4138FT5Hnz4b-OTDxGmgJ8_H3Gkur9jXjji3lYhrPjnTT6s5aSW9jSWbqD51PbKmjfHAyXcg487s3FzlQNBoz-je7581hsAvlQVGjTwBgEMYvOcPD9J72guzb4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEPoIusN3FrvPBk785ilpDt7tUkf7uGZrDUYqyAbtHx0Hh7m1fDPTu2DL6CS4tZ2M4vOJaa43NsqdBiBZPQgLw2i2cqT0KJl-Eb9LuODntiZab4Kxn5k9PH9JGwYhvjxEkqGyhPipK_i5wGmDwP1eTdz0nFwdBQyFxaZNL3H4wouvgGkOxqIRmoxC5-4EMcw7Nl4WF0VH3kWzKbXwQYCAAVCfSfhS39gAXKaqH0Jpi5TzsgvrOzd1J7xJyCzk2qhxDTa74c9DezWVvoPyKQo_CcX9pAwDiGCzJOBKPzqis5DysBVHhDVkeQQSZI61uRuvFnWOVWXT7X97uyqXFHPSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=tPTPEMsc3wjucFhQnwZF6q6DNldT-jWsUwDflKE8hyR2zNFrCyECy8--EGy02dVjCUE7arAf1zL5UZg78TBjqr_x7UZZCclnELXiIVncVQHHLHSJb-u4VTUKZS4gtVwzlxuXgXThwGfUZV7IeEHOYrlFaXO_cMvno6M0rnXZ-_TvtLDd-XBPBVgW-V8AXeQB-75AopX1ypezZaOHWY2OELCjXjWLxqSBu0B9eG4aT_oRgUcb8c2ntGNSF-Ywwixbq4iB_iXTXdFIL3cNz9Ic2-Z-IxrgcsHeHU3Xokov6AoygQ1yUiu9mYuY_hutb4cAvppX7qe3dkzaagxvFNYK1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=tPTPEMsc3wjucFhQnwZF6q6DNldT-jWsUwDflKE8hyR2zNFrCyECy8--EGy02dVjCUE7arAf1zL5UZg78TBjqr_x7UZZCclnELXiIVncVQHHLHSJb-u4VTUKZS4gtVwzlxuXgXThwGfUZV7IeEHOYrlFaXO_cMvno6M0rnXZ-_TvtLDd-XBPBVgW-V8AXeQB-75AopX1ypezZaOHWY2OELCjXjWLxqSBu0B9eG4aT_oRgUcb8c2ntGNSF-Ywwixbq4iB_iXTXdFIL3cNz9Ic2-Z-IxrgcsHeHU3Xokov6AoygQ1yUiu9mYuY_hutb4cAvppX7qe3dkzaagxvFNYK1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bs8zvn0C7Ug8d0l7p7bl9gyNwM-Vt7L9mmslekhrYXJUgGd1XdF2d1TFc34oJQAO43Ce5-vA_pgbZ2cOqP3m4oUZJ-QHkryTlT2lcMsbuYYek5rj0jVoiRLkej__wMjC40rUl_DBjXNsqXzAmvaqqtNPt8lkHAu2eUemZaKgrI_fQXgP9tItkmh9U8VmFQve_3S-OPN0mA9XztkFqENMqCXXN_PmTWmY-5wQr2-EMmMxooX6GCJTi1wyKfZhGeX2p-kbY7uxlJqQSoAUVfMMxoeJFMMR2-IvW2DNfm_AhFsfrLT7ygTo_H__I7ROC0kY9uHPc4Aj3tBvFHSb5jbPcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZtqpI3ji0RhK9UuHGZQNgIta7xiAnc6-kfokvCmXa5GZ8FlXp8bOEv3twZroOMU_wEq4eN3vqRbBDvb1lZB5l0se05kbPHzmZnRsNBYa3PkF3NQ4tqhKoqIgWOGxj_-Rx-OZktNfbH7TjpJU0Z3nNtR7z3kTjFLwQVCqOkw0-5Xhi4FyHAm1lYY_5f8m_LT6T9tngvgjM3FE3tfXrl9jhtUyeSfE-pWuySPlvLBrTZ4Apd3dg1WFUMttlnGSghdpahmCJRB_wrimJQFeIQvG8eqmakeWVLVHfa8j2mY6PnYYIJbBXmhTib0aD0LDXGspFi681HsZPATcKPq9LuL5Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K6vM6L6hFs4QQquHeB7bz1AV5ydfRFV6ZPPmcRGWR2Zd0Sc0_yVcj5aYtT8-drAsRDPJhZic9qXg0e5FcgRTe4geySGqGcqVFX_Z7FLJU927zf9TEwOFZQUapoA3mAQRZIo4n9_XNBksjdkYN6ghb8pMNVrp8hZm8ONyRu4Cch6z6vHlJyHZ-mnIHXMgyKlophW2ELFX1sWjM_OIEgbYfVwdUDICho_gIL3I1iMEK7hu4AF82Mcl5Sv4SwPW1BuOxbqf2Xr7LNMWujddlkf_GPPb7YnHlhc_1prVvvTtR_YoEMCUpgT87r1Q6bgIIp1SxAqXkPUDYHEu9eMN8vSVPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،
خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!
در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان
رو پذیرفتن،
اما «خسرو پناه»! مخالفت کرده و همه چی قفل شده!
خسرو پناه کیه؟ دبیر شورای عالی انقلاب فرهنگی
که توسط خامنه‌ای انتخاب شده و نهاد به قول خودشون انقلابی است! و قدرت و نفوذش در مدارس و دانشگاه و….. از رئیس جمهور و وزرای آموزش و پرورش و آموزش عالی بالاتره!!!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5257" target="_blank">📅 13:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqcxUGxbaQa6_MDUjQrApv5Yx_Ab0EOS_hOYl2Wx6WMezwGhtglOVhYi0pZHnzyUNGvvUed5U-00hoMgZD01oNBGFVlaamyxeVQ4IEZR9WlkG1846q8kWFaMQ9TNuNNghne2EQY3gwal1lMNH8LUxH33k35mTKAjckK4VmBptFOlZynaB9C23TN-CTtLImHFqh8aHXo6lMZQOsRUqCO0WO9lH_xd5wcv-cbgkRwMejkm6nf6a4mpR8g60bnzfhU_lKxd4bAsw25MMt-8ulZKd9QPQBdPuTOH0aXE3Hc5z33FUcS-Q0xaJFe_i-ETLQv3WT9EjQYvMCrVyAuF5ZIBBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nhaMNa-sZlZndFutUfjJyfsSZkddM5ivKYJ3pft17vIyWKfSksOexbzxIyP7Chfv_ATg_pNBUxTMbkxZpeMvCafkPZ0DPhLcdATbXYg1DO8b9cQvcAshn40k3WTqASGAmFWCu8wUTcCQa2dWfZsx13nBdrKByysYyNjgoZil4CZ1Wlyw_UbTtllZ1SDe54_WkhcZ655GSKXelqf5I1PaobDGdZsi7BFCxvlwyh80awYq7cwa1NdqwUhYyi6MbfGsHGKxfneAondJGrHDH-dHiX3DnGjyUmsfHBpMgNNUmlfzOEyw4wSOub9yHkCFKy_kwzRR2eyV4w8cRnFkdxtMAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i1aAIAYcF9Txin3XSlaJAGqNNblDtYtxYpC5y74_kD8xOAYj2tr8P5CJNxp8Ww7E10L7ahZQHGcD4e93MB2_dZlRT9kJAEmYYjQfDZhj0OlwgAmQxfiKMHrHwgqB7602yXNks-zA9be-0UbI6fwxiUuMiEcMEZTJusIocPhd9IvDhIZ1p21up87hFlsyJNhaTptEZsJFLCD0dc2DMqRZz115TlhMphh41kIRIqusLUdH2xR4O8pe-AJSS3d2pj2NDxewQU6H1ev3AI7ICYIOsWdWLL0MTopAh3IUDObphaSAeVpOG9KsHItznnnbHcnrsG2Fui7VQhl9mwXE-Yhl4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XqEH-foO3gNLScd7J6HkPg00UhhOQ9jm7UywcPKG3ZRSp9l0VnXzdrYBbCsNqMjxyVCUjZo998yvm8X2Dm8_r0pOoyq7fhkidUz0KEZ6abs-LXlGR4HnLw_Q8xMFkl4dM1HhaAsfqXXAxGHMRVCnBQRU18JCvuUkC4M5ZWxFgnhN9xPU71ATK9KXyJ9d5VYPFu9xFZFSSKCxsEkywMZtPF4TqHyfZGZzkRt-mb-8RLykBxBKYIBQ6PWn5HDVbKy_HFmjmJYMqXxT8EsbSYgA2zVMxQcksDsCAqmwVwZTbilGE1T5Cv_e-1XVvvQ3WNKeZdc9sGjFKyii3d-MZtcDuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IDUYCdxqeff6yWm_vJ4PBujDlTw0wIeyWI9uX0wVQZj41pQ6WHHUsf3CnCYtFkroQlKTxtT2FBwgZtfQcbHlFnNSNzHjQP2Ph54cReoFqgSsX6Vj4npBTmP30hh8AwTnm1DdDH0dHnFXK5pMWGJqG8rzNOqS9qQ0ZSuAwQ4wTwLVry0WHwwEmW3zV6fIab_xiZ5i_scrSG46exIuwEOCCI9ZioozxOqHz3jeG6fpT9ucNUW_84vw8BE110gn6xS_y4qOamjwRd8JpdiDYcc5lBRvQ6N_xOD8P4V1MSm13ImMaGWVE8I7a6TYdjWwxwHjZTLBottzPorElok8wGeIRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">و بعله! خامنه‌ای و پسرهاش
خیلی ساده زیست «بودن»!
فقط در زمان رهبری خامنه‌ای، برای خمینی مقبره‌ای ساخته شد که هیچ کدام
از اهرام فرعون‌های مصر،
حتی فرعون‌های مصر!
به این  هزینه و گرانبهایی ساخته نبودن و نیستن!
این فقط و فقط «یک قلم»! از ولخرجی
اینها از اموال ملت ایران بود!
در کشوری که هزاران مدرسه‌اش توالت نداره!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5252" target="_blank">📅 12:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=cRfJ4Lsa9SU5DCMWiRCDM6v_qYcA5kPIf-WwCASi4JbeLlaj3WgbJw5c4F1Y0jENDErk5WH8MGt2J1T4dV_dtj5gGyWfG8eQ3yUuBrTwQZ0XFsdOP44QMXix1Fxwz4ED0oZNLthM2-IGSdHvuMQCJsh8AMU9ipe2tth5j8VoMevRsTdgfgZvNOI4nazx9bNO6T1gfgkNaUkzPeG8yN8wcyZHPxgVMM90lQrh68tS-OBkSJt8tPQDXZXT1KIF7BO8GhNn5Onew4Cq-hFDR9WRe2JNtiKWpsTtZlyQ5GkmJy1aex82-GAxu6udfRkbOyuVTUb0CT52bouPwLljBb5fMWLV-AF0fH1hv9wpHsVb4rZcAnmHvyRVNy_B9wL_ZPWC_JapWSphR_MqCoBB5e4XbwRxKnI2CQlWSfD0CMXf-BFc0KF5C0nNgZZ1gIrtvJ1KvbBjhbp_C0ySoGkhdRFwJMKX7xPKJ9OPKOCrLykAj-Wj3ttRgvRsBMeLPk79nYxXa8WerlT8eVLZy64fAnCNu1KzgOyEiDhiN81QR6bKLCUyCQP_L5c1TpcgIoh_U0s1d6NMgu_-njOhgJO14W26WjU0SB61aM9Q-OY4enwXiZrqquYQZacmkOBzV0gZM4Wn0UZMVaoZXTtGewflnEOmP9cNvGsQsqoVnDFsD-eQ-xc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=cRfJ4Lsa9SU5DCMWiRCDM6v_qYcA5kPIf-WwCASi4JbeLlaj3WgbJw5c4F1Y0jENDErk5WH8MGt2J1T4dV_dtj5gGyWfG8eQ3yUuBrTwQZ0XFsdOP44QMXix1Fxwz4ED0oZNLthM2-IGSdHvuMQCJsh8AMU9ipe2tth5j8VoMevRsTdgfgZvNOI4nazx9bNO6T1gfgkNaUkzPeG8yN8wcyZHPxgVMM90lQrh68tS-OBkSJt8tPQDXZXT1KIF7BO8GhNn5Onew4Cq-hFDR9WRe2JNtiKWpsTtZlyQ5GkmJy1aex82-GAxu6udfRkbOyuVTUb0CT52bouPwLljBb5fMWLV-AF0fH1hv9wpHsVb4rZcAnmHvyRVNy_B9wL_ZPWC_JapWSphR_MqCoBB5e4XbwRxKnI2CQlWSfD0CMXf-BFc0KF5C0nNgZZ1gIrtvJ1KvbBjhbp_C0ySoGkhdRFwJMKX7xPKJ9OPKOCrLykAj-Wj3ttRgvRsBMeLPk79nYxXa8WerlT8eVLZy64fAnCNu1KzgOyEiDhiN81QR6bKLCUyCQP_L5c1TpcgIoh_U0s1d6NMgu_-njOhgJO14W26WjU0SB61aM9Q-OY4enwXiZrqquYQZacmkOBzV0gZM4Wn0UZMVaoZXTtGewflnEOmP9cNvGsQsqoVnDFsD-eQ-xc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=Q5mCnp8wwk4Z5i_3k7e8reomp42eo7n32gvu4Qg2NtpUjBpph9w34T9VrevIdcun6E83yAP_pZScDVuv8pCWakBsf1_woVwa8sveVkQayes5z9wNaZVw85JXaPL4ScKr9RtGCdY3jz13WrjIYobQaxlK6RCPykBB_ietoDd4iLR6VlZv0YDW0sxDVZTBl7J9PS0KUn81MzMV5al1pKcQ-7YKzuOIOOpDs8WF6BIRVvdiCN8a-HEz437xgg9vW0TZTQ9cIjzV6KLPT1fMlzrx7LUq10JGH6_iP5nc8u9xwAmrUotzJV8l1EdXNsS-4bHNkpRA5bzXw67LbomyRMOaQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=Q5mCnp8wwk4Z5i_3k7e8reomp42eo7n32gvu4Qg2NtpUjBpph9w34T9VrevIdcun6E83yAP_pZScDVuv8pCWakBsf1_woVwa8sveVkQayes5z9wNaZVw85JXaPL4ScKr9RtGCdY3jz13WrjIYobQaxlK6RCPykBB_ietoDd4iLR6VlZv0YDW0sxDVZTBl7J9PS0KUn81MzMV5al1pKcQ-7YKzuOIOOpDs8WF6BIRVvdiCN8a-HEz437xgg9vW0TZTQ9cIjzV6KLPT1fMlzrx7LUq10JGH6_iP5nc8u9xwAmrUotzJV8l1EdXNsS-4bHNkpRA5bzXw67LbomyRMOaQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی
از فعل گذشته برای مجتبی خامنه‌ای
استفاده میکنه.
مجری : رهبر جدیدمون آیت الله آقا سید فلان!
حداد عادل :
ایشون از آقا سختگیرتر «
بود
» !</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5250" target="_blank">📅 12:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_7uDFSNJLWxrfa0CV00L5oOfO0kGLCi1z2fgxS1jd_5nPQFTMA8a-tVCQEjP63DInG89RN9K8h9b9DHZRWWrrhhFNa3DHAqqLWg5h2a8bkhql_HtANvgEx6EedHX_egtTRqyLGMozJDHuW4Vge0iF_fnr6TJyxd7mnDwpxzLmKTYsfgY9Fqh3092P2wS8NWEdINg3zx3_SwQt8jbjuJ7-NyJtUT0nGXXkm5LdE6WPqvag1rfN62-J__a6hgZSEcIr2H8_zY3Xa7_dyf17-6OMzsiQjWwAv94Ck6uibNtNie6-frgvXl_21aSxQBuWLenOPl-v2oQiWDnp5buuncEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف گفته که اگر حملات اسرائیل
به لبنان ادامه پیدا کنه، در مقابل
اسرائیل خواهند ایستاد
‌ و «زنده باد دفاع از سرزمین مادری»!!
میخوان وارد جنگ بشن
برای دفاع از سرزمین مادری!
حزب‌الله برای چی وارد جنگ با اسرائیل شد؟
برای خونخواهی خامنه‌ای! که
هیچ ربطی به لبنان و سرزمین لبنان نداشت!
اینها فقط برای فرقه خودشون میجنگن!
نه ایران و نه لبنان!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5249" target="_blank">📅 01:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">قالیباف در گفتگو با نبیه بری (چهره شاخص شیعه لبنان و رئیس پارلمان):
«جان ما و شما یکی است و پیوند ج.ا و لبنان ناگسستنی است.
در دو روز گذشته، ما به طور جدی توقف حملات اسرائیل را دنبال کرده‌ایم. اگر جنایات ادامه یابد، نه تنها روند مذاکرات را متوقف خواهیم کرد، بلکه در مقابل اسرائیل نیز خواهیم ایستاد.
ما مصمم به برقراری آتش‌بس در سراسر لبنان، به ویژه در جنوب این کشور هستیم.
اگر توافقی برای پایان جنگ بین ج.ا و آمریکا حاصل شود، شامل توقف حملات در همه جبهه‌ها، به ویژه لبنان، خواهد بود.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5248" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
به رغم گزارش و خبر ترامپ : حزب‌الله لبنان چند راکت به شمال اسرائیل شلیک کرد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5247" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بیانیه سفارت لبنان در واشنگتن در خصوص توافق
بر
سر
آتش‌بس
متقابل
:
حزب‌الله با پیشنهاد آمریکا برای توقف متقابل حملات موافقت کرده است؛ به این صورت که حملات اسرائیل به ضاحیه بیروت متوقف شود و در مقابل، حزب‌الله نیز حمله‌ای علیه اسرائیل انجام ندهد.
اسرائیل به ضاحیه در بیروت حمله نکنه
حزب‌الله به اسرائیل!
یعنی : اسرائیل می‌تونه به حملاتش در جنوب لبنان ادامه بده، اما حزب‌الله نمی‌تونه به اسرائیل حمله کنه !</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5246" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
ترامپ :
«من تماس بسیار سازنده‌ای با نتانیاهو داشتم.  هیچ نیروی نظامی به بیروت اعزام نخواهد شد و تمام نیروهایی که در راه بودند، همین حالا بازگردانده شده‌اند. همچنین، از طریق نمایندگان عالی‌رتبه، تماس بسیار خوبی با حزب‌الله داشتم و آن‌ها موافقت کردند که تمام تیراندازی‌ها متوقف شود؛ یعنی نه اسرائیل به آن‌ها حمله خواهد کرد و نه آن‌ها به اسرائیل حمله می‌کنند.»
🔺
ادعاهای ترامپ شبیه برخی ادعاهاش در خصوص ایرانه.
اساسا اسرائیل قصدی برای ارسال نیرو به بیروت نداشت! بلکه نیروهاش در جنوب لبنان هستن!
🔺
دوم : بر اساس قرارداد آتش‌بس اسرائیل قرار بود که به بیروت حمله نکنه! ولی داره حمله میکنه
و در نوشته ترامپ هم اشاره نشده
به حملات هوایی اسرائیل به بیروت!
گفته : نیروی زمینی به سمت بیروت نره و برگشت کرده و…!
گویی ترامپ دست اسرائیل رو باز کرده که به‌ حملات هوایی‌اش به بیروت ادامه بده و به پیشروی‌اش در جنوب لبنان ادامه بده.
همزمان گفته بله من مانع شدن‌ نیروی زمینی ارتش اسرائیل به بیروت بره!
🔺
سوم:  ترامپ گفته با نماینده های حزب‌الله در تماس بوده و… عجیبه! بعیده!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5245" target="_blank">📅 21:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwQm8-V2e-CV10b3RrcWwnLlLKOYDJk0py9lvFKB9jhf_bWMYSAS4WeVFQ6A8DKVuO8tHHFXpZVjCcPFHxzfR3-OTFPz7f5CDE-1xluwXV6DmsBoH1wlyKwPHaemID4RrkEdy3Ka9xV4ySfqNN0wuv7Cwms8INlg2lBEzxO1iETuWmx6sNcmKhXTWIFVK3GXHNsRevmvFMwF-dwjbfQ4eIJfQKV7NiaNUg0nqe0huKKeH2DyyCAvC1wI97gag52g4VcNSDjDzehDdqr42fgRMbssCF15Q68cQIScSEDJmRzrh91FkNgchCrXtabBEoy2sY5yMAyxLz1qHQmHtV2b-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه جمهوری اسلامی اسرائیل رو متهم میکنه به «نقض حاکمیت ملی لبنان»
یادآوری :
دولت لبنان سفیر جمهوری اسلامی
رو اخراج کرده و گفته مسبب این جنگ جمهوری اسلامی است اما سفیر ج‌ا
لبنان رو ترک نکرد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5244" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5243" target="_blank">📅 21:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YoeXxBLZGMhYaS7hqhFIUrVZVnkhVaH9lnzWHHmU1QBukw17Nurd6WFfAE-meuFlbgf5F7bnwBggH567-WygMB66wi9Q_TkVdF3kmxWN2Ye8ubzpCQh2tS9PQyaENAkMOZHgBsdtzptc50F_582j1w-zvxsZv1FgD1s8Gl5DhtkfljASG5oT56yP4d5O6pdeYy-e65wUeP-nWAyRv0w4YVU1wPbsSCX-hRz7M7uC5NR8Nt3JuZgMauft61v1ZSV2mrgKpQlV14UxsewQY7nE5mEpp65RK3frPPBEAzoUw3c3RWTx8z0jsyE8NCtF_YQp8M7RyhYta_pjmVXB_7TdSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfU25rB1AoUlV7a1dQNQni3XybJ6OurkiLD3NvbbPzLV4fOAogubee0em7lIyDYjR3U4erdlGyMw7S5Ipfg5AKaEnfcwPFrS9JuFLn8Sz-eYuNL0CpOQVFpe7TvyTDSP-PsBOBH3QET0WtumIIN1CkUUbaUn3fevMqPupzmykHXnnUWw6EGQe1DLifW2rTLzGCXU1AxzX5Gdqa65RY49cqbIEaXS2KtRqeW4BWaXJkKONP55yfPARlSoAtiDOUWMo3rytALvt5VnEG1AkfOQ9ZjhZXxksviAy3yej5X8biyjNtXLTJnvLWbhlF53EPKXipC0Y0OrTiGnIx--Wbv8aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwpR5qpNpBmdOQbg79WhlhgWihIpXiSDunDA466r6DCPnokJ_w4eirVc0vjJ7A0wodzkGY4ri2g3wwqOhj_TEGcQLUq5VuBaaoL80Kn6-307DnHPLmE07p2HlbCjDuYDd6a4K3_E7XyfD5kiMtF4gGc9IQtC7t5LjpnzktEPOmgJGaCZgmBYRv9mojXHl6cSYGBMwVSuwXUN1ATpB6LSb9lhH2pUA63TI8msk8LdvJ1GT5_z9K43ITCscCGlIDIgYitbnjzPdrxrx-59zHOpNB0btjKCwGRrSVsfRJL4MFjm-3I4MgLS76Zj-0Cv7VZnfSEN5jkRPX1yzTc_P4k5cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه خب ! اینها «وطن پرست» هستند
دغدغه‌شون «جمهوری اسلامی» نیست!
حفظ «ایرانه» و بحث «وطنه»!
فقط اولویت نخستشون
گروه تروریستی حزب‌الله لبنانه!
و توی مصاحبه‌هاشون هم میگن حاضریم ایران به خاطر حزب‌الله موشک بخوره!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5240" target="_blank">📅 20:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5239" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVSBPDO8NBGQC7MOfElIPLwfurHJkOhuoRlrgHQxWQFXeNwA_mjqwJ3cGAdOzQXGGKsI8SabDTzLmqoG5lNwe0cpA3twxs3g4AoYPNSbdHkisFh_hCZ9WXRXBBFfn7wrXsQOHaf-n5PC1FUOoL50rTUd4W0dVnEeNeNz1TEvylZxtBZt-ArnWK5BBDrgtDQl0t1PKnIaFXDW3uG6fQoWUPIaJpurYByeajxcBz2Lv076qZ8DFhS5VN8q4G2GC6kLcizugXnEFeqWcCbuxV8sZZ9wC9xiUxG2EXIKIOvgoexZNqAJEYnv7zuG7o6Pohpr1N_zQXl8lCfxZnaD9StFbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتابهای اسلامی برای کودکان
(در مصر و تونس و….)</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5238" target="_blank">📅 17:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">این دو سال رو یک مدلی با ترامپ راه بیاییم و بعدش بزنیم زیر قرارداد!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5237" target="_blank">📅 15:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjInTgxKhsvoNgMx8dC3YRrZAjIn0mqx6km4buR0qVbWIGC28n-_-DCyFiAL-UoUCvwnyWDkLUc5ksX67GYoCufS9PwirRVL6gm19Qiu8nR_lSuxVa3naR255IKOpUkrlHYyI7Cmw9J4yk3OLYFEdzagAPxKUA4cNFB5h4SPe5PXWYXFrrZr5VHTbVy7piqCJ0M1przx1nS0YyCyB6TaAPxqaohcXKXdfqyTof9LE2N9uneJ42YNN16xFhDCmMq3vy0HZFlPvtD0WkSbnVhalWX1OZFxY2SJE-zae9a0Ptz3g6F8vyZx19rHaPN8QF73urjP7spSqQWgSGsci0-z4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نتانیاهو دستور حمله به ضاحیه (بخش شیعه‌نشینِ بیروت) را صادر کرد.
🚨
بلافاصله پس از انتشار بیانیه نتانیاهو، پهپادهای اسرائیلی در ارتفاع پایین بر فراز ضاحیه به پرواز درآمدند و خیابان‌های خروجی این منطقه بند آمد؛ هزاران تن از ساکنان ضاحیه که پس از آتش‌بس نسبی به خانه‌های خود بازگشته بودند، دوباره در حال فرار از منطقه هستند.
🔺
نتانیاهو دیشب نیز در دستوری به ارتش اسرائیل خواستار  عمیق‌تر شدن و گسترده‌تر شدن عملیات زمینی ارتش اسرائیل شده بود.
باید دید واکنش جمهوری اسلامی چه خواهد بود.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5236" target="_blank">📅 15:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NWlSD6cmGK8973K8lWf-ALIW_Z9wjTnt-hmpvOwYJh7lT9KVA9mHlhAqaH9WOjIzUH05PEiQ3WiPAZ-uLHTK9bLG8Xicm1LYLt78zLG5-pf79116M-7PYf0BD_V1GE812ml6lSuPKV26imb5Elj2weWThMu5jypQkOLpIIx5c_jaz97v0gLOjiwaornpgMD3gFpgl_iRCFomSPIdmAbnFJYLkOxHxytgWQ0DnJjvs4fTvDAk8Pokr56eDBAyi27tLi51umf0ribtapEwFKmWaG8dcGbndpC96oEC66pgxzctbFwOhbnPKhbStO3_at5Ew6RGyzUi97YmfprGPdrycw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SDSBnOzeWTke09aWT7c7PngKxjVanMX6EjINxkC3xjYoME6GAV8UF0zZZcVwVEbwEpzyZaqqikJHlvMet-rQc94o7GLkVvQun3NunxxZvCJMDOFr2kvErVN3fVtUfS1hZbQZFQq57jqPmKnugYlE7DfBbYU4BVnTSD2Z9PS-4Cdl1hGfQgbIoSoJRREN8JWphsUJkumytueMO2PrGOmair9QGIF6cuuyCKBXFf8bwXudY0RJQ8Gn4ZgV5--4xT-yQtjJaXH_1dTUhKI_5yl1DZ47MUwiEf9u07osDxDinNkZKGYJvoIsoHsMFWYz0C1VUwUNrgwMHCtKRwhhEcw2Lg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=sNayD6Tt2zj6tzQDGRlfTQEgQ5chFMNbJqUN6Wn4oCh29UCiPNckYh4YBxJJc7-ssXF3bIAAH_cYJY2pWI73LqNxtF43ptGtGQBJ3SLRb-c4WNrxUVdDZX5wxW-0ELv7LuUcuo2X1CliZnlYaqsRtOUJw7iChSMXOySePPMg2ruTFtszR6BIkGI23EKbQqXs_HhkWP8GGqTa-RDiKuwGHxG_SH8PCfg6DJoJREIFdVcVWHC_8rBIPCrXK4alvToxFYugPNNXzwpRcW1mIyPvdlK62nVeMccq1RwVA-JE-ORsywfr_dtqnbQe2OEsJXLXovz0IAzcOyU2deSjeE5uIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=sNayD6Tt2zj6tzQDGRlfTQEgQ5chFMNbJqUN6Wn4oCh29UCiPNckYh4YBxJJc7-ssXF3bIAAH_cYJY2pWI73LqNxtF43ptGtGQBJ3SLRb-c4WNrxUVdDZX5wxW-0ELv7LuUcuo2X1CliZnlYaqsRtOUJw7iChSMXOySePPMg2ruTFtszR6BIkGI23EKbQqXs_HhkWP8GGqTa-RDiKuwGHxG_SH8PCfg6DJoJREIFdVcVWHC_8rBIPCrXK4alvToxFYugPNNXzwpRcW1mIyPvdlK62nVeMccq1RwVA-JE-ORsywfr_dtqnbQe2OEsJXLXovz0IAzcOyU2deSjeE5uIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال «پاریسن ژرمن» قهرمان شد و پاریس و فرانسه رو به آتش کشیدن
قیافه‌هاشون که تابلوئه!
توی یکی از ویدئوها شعار الله اکبر هم‌ میدن!!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5232" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.
پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5231" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZit1U4q4Sra0p9OZMbvYI0FObz27BIn3RfaFh8yjFVcGrLeSquRFgxre8a39XKMH60RvqaTe4oHkGjeLgZ9RmjPC1zShOueuWf4qcX5U6RwEcfvh7hb_EIQetdHEO6A2GsgjpRfvAWjHV3YP6hZ3h2YDopnWudCEWhSxo5tbpou03TmFVkk74bq7RZBJFcJJ5z4UfTaMCMkzExmyj2RwAEULeKYKCEPENDq3kVHBrDL-IlxQpFlqKsF40Cghk0LjdHXvj6GfJrctj_BQ7wU9YZzPmKcTo0DlyCmmhrGU0j23NNalE3gY9vs9aOnv6IIJ1eGMacJK_RrRVwPy_y2lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش آمریکا رسما اعلام کرده
که چند حمله در دو روز اخیر به قشم
و گورک در نزدیکی تنگه هرمز انجام داده!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5230" target="_blank">📅 11:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=Ok2cE9hxoXH61BruzXc3aFAIMaOMl103l_lmKxM2D9WDA-JUhvSNBms0xRRkXzZRqhg-N6SHzFHt9NOCZR4DNNbTSUv4ntfXzSE3Z2sOgUJvDa2DlTXPHGkudxxnSKs0WFZPQCBBNlpw6rgklMYcVfz71G2aPT-E5dbhw8EGFewt7Rj9vb2imSjCHPW9dZMMc6PNKXFCga2WEPbXV2bAfhMMR2vuMP4XH4vHb9Y_07jporcawAvwiZger9yHhxfDt3nHrivFL5fuyCyuK381pmYUs1mbI4_oPw8nGp6Ms8qvewtr_NkKy97jagm2ivQH8p0vwURG6cCc0Rmv3FmTKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=Ok2cE9hxoXH61BruzXc3aFAIMaOMl103l_lmKxM2D9WDA-JUhvSNBms0xRRkXzZRqhg-N6SHzFHt9NOCZR4DNNbTSUv4ntfXzSE3Z2sOgUJvDa2DlTXPHGkudxxnSKs0WFZPQCBBNlpw6rgklMYcVfz71G2aPT-E5dbhw8EGFewt7Rj9vb2imSjCHPW9dZMMc6PNKXFCga2WEPbXV2bAfhMMR2vuMP4XH4vHb9Y_07jporcawAvwiZger9yHhxfDt3nHrivFL5fuyCyuK381pmYUs1mbI4_oPw8nGp6Ms8qvewtr_NkKy97jagm2ivQH8p0vwURG6cCc0Rmv3FmTKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=oAbXmTsykwnb7YMZsLr7PDE5kBHSDHYeLSKjQfNIX6vCaNYTQavKNCL0aHji2ECZsczx-eLmFERmnJ2SPJwQp44tujrCT9o4WRVahqOFaExA_wOOQVdyX61h865Abynr7fAV9hGb3joii2GRjtbXSUALMTrQPe4T8syYT3AhrZcBuAPx5NzUFRZut_qandw7kMo0UqqrndhCbPmk5z_NeteXdZguV7t-yhsVx124xXqBz6y-6ELpxw-veiTEWltMGhvE8p7He2XxDQ3ILJI4VN5wlX-OmU_SCksVR4PBo_3YQfGhDMQY5naoSwLNGiYBnK3H3SZQSg2mpm9pgnswvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=oAbXmTsykwnb7YMZsLr7PDE5kBHSDHYeLSKjQfNIX6vCaNYTQavKNCL0aHji2ECZsczx-eLmFERmnJ2SPJwQp44tujrCT9o4WRVahqOFaExA_wOOQVdyX61h865Abynr7fAV9hGb3joii2GRjtbXSUALMTrQPe4T8syYT3AhrZcBuAPx5NzUFRZut_qandw7kMo0UqqrndhCbPmk5z_NeteXdZguV7t-yhsVx124xXqBz6y-6ELpxw-veiTEWltMGhvE8p7He2XxDQ3ILJI4VN5wlX-OmU_SCksVR4PBo_3YQfGhDMQY5naoSwLNGiYBnK3H3SZQSg2mpm9pgnswvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما  از دولت لبنان خواسته بودن  که برای آتش‌بس، مذاکره نکنه و…..! به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره (که بعد بگن دیدید،…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5228" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxlILNsqResUeESL4-PzC7lzJwqx4vBbthjMoYPyuWbP79FqV6b1eRVhhwaSBTSvifjg53L62fQDij-pPt6IfjjJPq3SZZBa6nKPIMpJrCrz6_h7PUWtqOZgjix5Rg4rBfaU4t1fPe9f2dtS_0jkGCiztDihr_U-Lfe5PKhQu2BSyqIVY73XKYYKGdxDi_N5nqm1og0MIhUoGm9SIHInXtUTnXSa-uAnXBEWmB94cEd-WYR6MtpxBMuclxvFO9xPo3ck1a17O-LutuTtfrtO0xlZ8N1n6uNaaQmPJ3icYpriKIc3uDge__T7I3OS8vxeq9lZZANMFC0GIhum5y2Cwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما
از دولت لبنان خواسته بودن
که برای آتش‌بس، مذاکره نکنه و…..!
به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره
(که بعد بگن دیدید، همون کشوری که به ما پول و اسلحه و….. میده، آتش‌بس رو هم آورد؟)
ولی الان می‌بینن جمهوری اسلامی توان چنین کاری رو نداره!
ترامپ اساسا داره لفتش میده و سرزمین‌های تحت کنترل حزب‌الله هم داره می‌افته دست اسرائیل پ یک میلیون نفرشون هم آواره شدن!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5227" target="_blank">📅 11:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5226">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.  به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.، مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!  یا شهر‌ نجف!  برخی…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5226" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=c2O2J-pvBR5woL1plU8D0fh9AVS80UPFFlGIHbNkqaFkdo4blQZcNAa_3UK2UIji61MvcPM3mlvVSrlRac1BCdHZWJBZpeuNCoAe0lvoTkUAF7r6_LebfHYkNEwpjBX-H-Dj7g-vgPVev0KL8x4lFnwLYGVcskkj25-hD0F8we7tn6XMW51VVP2xO66zRiy_0FilO0ubdij-bLjvl6C_HoIbrNGNNqAPYvtcuXv_lBLk47z7Zu1s_4RVTQIMLA6PJXSy38RdlDb7bt-FXDgiuhb_KZtAa1rimV2rDMzzUUMclp1aiz4pXmxf_-ApEVolan3wDBUyQqVG8CNzImi1jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=c2O2J-pvBR5woL1plU8D0fh9AVS80UPFFlGIHbNkqaFkdo4blQZcNAa_3UK2UIji61MvcPM3mlvVSrlRac1BCdHZWJBZpeuNCoAe0lvoTkUAF7r6_LebfHYkNEwpjBX-H-Dj7g-vgPVev0KL8x4lFnwLYGVcskkj25-hD0F8we7tn6XMW51VVP2xO66zRiy_0FilO0ubdij-bLjvl6C_HoIbrNGNNqAPYvtcuXv_lBLk47z7Zu1s_4RVTQIMLA6PJXSy38RdlDb7bt-FXDgiuhb_KZtAa1rimV2rDMzzUUMclp1aiz4pXmxf_-ApEVolan3wDBUyQqVG8CNzImi1jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.
به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.،
مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!
یا شهر‌ نجف!
برخی از شهرها را اساسا به صورت شهرهای پادگانی عربی در وسط مناطق فارسی زبان و ایرانی ساختند،
پادگان شهرهایی چون : بصره و کوفه!
در قم اینقدر عرب ساکن کردند (از قبایل یمنی اشعری و از کوفه)  که برای چند قرن یک شهر با هویت عربی بود!
اصفهان اغلب یهودی بودند، یک شهر تجاری، عربها حتی بهش میگفتن دارالیهود
عربها شهر «جی» رو کنارش ساختند و اعراب رو ساکن اون کردن. تا نیمی از منطقه شهری اصفهان عرب باشه.
نیمی از قزوین، محلات عربی بود.
این حجم از استقرار قبایل عرب در قم، مرو، قزوین، اصفهان و… اغلب به خاطر قیام مردم در این شهرها علیه حکومت عربها و مسلمین بود. قیام های قم بسیار معروفه، اما اینقدر عرب ساکن قم کردند. که شهر برای قرن‌ها هویت عربی گرفت!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5225" target="_blank">📅 10:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrzkJ1LeTL230Ptsx8qIITW_pi4Odg2kWduIjx4ZRg5Tl8f0WLU_Qd_Bvr22HfyNcGOUemfX7Vnopy6NpvH68c5H9AIbuDV_2IH_BeaEIsVYltEQr0-ewqcDB__LGonPzvrjU0Qy1dCw0BCHROtRZjkvXJ8Fm6zTWCXjS-yy0clLvViY5sblfF2OXYeCaP7Pu09wvoTpMTcWJlKSGP04xFC-7ZHavBYXquuWvbRf9Lq9y6ppO2n2CXRec0h961_G1_K0ZbntRn6F-PJOWQpnbe5XzpmxvDDs3Qg6k7YFN4ZZWMtAdDgbWZskwvTljOW3Ya-1BLR6oyH68sWU3gWd5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطور تریتا پارسی در آمریکا
متوجه یک «طرح پنهانی» برخی نهادهای امنیتی در تهران شده؟!
معلومه یا این طرح رو خودش داده
یا با این نهادهای امنیتی رابطه داره!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5224" target="_blank">📅 02:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
مایک والتز سفیر آمریکا در سازمان ملل : جمهوری اسلامی با حمله به کشورهای عرب همسایه‌اش اشتباه بزرگی مرتکب شد و تاوان آن را خواهد پرداخت.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5223" target="_blank">📅 00:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUUOyie8GxACUALMyPP-4Unq6aTEmT9co-Tixx5tgzq3me2K2mInBV9HKErT0qGQAK2kl4Y0XBZg82Htx-N2gAQDj1M8A4NnCiqUCd8DGsmMjJu6MVYy8AnXbsSdCMHMswdhQW5BtqVg-WyGLZrKEFiviOEWukAGxy8k5_3hxjj7l8NEQCq9bHlwkOHHQckQ3d7a1GWRydsy9C3k8LnDG_W_Fe4EG2X8rml03rMvujHujQT6zPYrZTQsCEj1w_PDWZAjXAv0mGB_rXJgmWmqqo7zKHE69UIjKy-uAODc4U3puwRVFxHqd8n40jg2UN1oAb1kmUirP2Tw_pA30deAwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌های ضد و‌ نقیض از استعفای پزشکیان از ریاست جمهوری</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5222" target="_blank">📅 00:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hUP11SfDWEO9CTchTstsQc9xVEcIVFTBn6E4aoBXcmXoCOOMDNNAHFoMTvUAcJBK6sWCSiTrxlT5a0fYQC3Xg0Li35m1tT7RkCwuYwCUV6QWpeZkJWdL-2nVqHmdNwefrqn4rl8r5osEh4WFjhm5gGS91KEuj66IknThj2Ctb-9eDs6IYv96tA01sMlZ5o4Ws6ZLiDeYD-k49Amt6d1dBCYuiutRpYcUKUoK3hRc73ualGgom4bGj3nFBZ__30ywUeeCl7b8CzICnImtLUoxEu3BxqlXF8XmVtJRS4T2g6rLu0-WPkV_kxRWRHsMUnDg9pKhAIi9t-paVgDSL8zA0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ing-W3rev_ei-gT7cphbplh-7KSTOWE6UlkII_kvqkVo-uF419lXkBqOgLWoQMPDioqGZUZTugARa6TXv7asTnkC4-U_uUCCX0tKaB1zyde4oAC6T0jN0c8jne1O5dWVNFUuMgTgwuXjYjYtxrzvsyE97lGwNFnssr1UgUpHh97kbThAsRlHdrzP0WOgHtctuUxtV2rMiSudTiCqrRLdsE-K8c7FH4EjQuOZCnr2lP6WnW8xWqeEM5SOwBQDuDvzKvPnSATWHYMTUc8oP4SKyFxJz4JdOoabWIugCl30_btaGpzsy0gJ2uUgFgUIU5HEpOWCdGXweSPq4lSl9de55w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kcEsgj_siuwaOkSz93J6U6r5QMbQt1CigaGEsXc2o6XabJL8UEUuc-OIgLBZyFIrAa-Wx1noEL5V4BI4F8L_-Vgjl8lsi2ku8HmG64BDKQhGl2-KkcVtYKDEY2FyMO1OzPM3japKSqXU2jT26UoZF4dCCPP6E0n4T8fGizWeHxSo5rWzuCAQFK_neVDkTGwUAUPMr1zRJ5GPESeiojUaD7Ke5bzvhBwjui1IHfCr5FaRHJsfMWZx11ocnjjSE6eFBAvKSrd0VkL3sGHOXhRCjoIGJuMSBUPztsTA2biNMc4Sf4gtKPx5laHS3jFuP9sOM1_fBDSUAyOELfY4BQkFJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتون رفته میخواستید برید
پشت سر خامنه‌ای در قدس نماز بخونید؟
که شما تاریخ خوندید نه؟
تاریخ جمال عبدالناصر و صدام و قذافی و بشار اسد رو لابد خونده بودید
که همین هوس‌ها رو داشتن!!!
و به همین نتایج هم رسیدن!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5219" target="_blank">📅 18:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5216">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XdqnvpQFDMS4Yl67-tJu5u7bcwmo092xy6NmORJh4XmDtRr3xLIYFFyFmgfoqOhRpypz7aI20pIJt82FavbcdELdNbhMYpKm5ucm1qDMu9cxjp9XdsS7vULrG2wOoxwDj6f_8LBSn72FXanywBBPuBnNUupVIRZ3LU87zfO0qeBJiRVd5o6nfETlMOZ0MFYaWySHGfkvb_ipum8u9dojFWEo7kKv9x8RvbVZ2ugyQYlejSBTPPvQmmGpXMwIjMoakVwg9Rh1AFz7inkhxAHwpr9VrA_Vtm4oyZqDsgvhAJqmi1npVwxFAAxZp6qObOv_pBgAWqPt4hFh6vCvmrOL3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y0Z298ROODPJitCrOhE9Zysdlkx2EPBj5LFuhoGa5EpMgmQql8H19TlzWnB00s87OtNNsx3FNBupzA9fVnfSso6_WmquvfW7BfqhOd-qiXNwW8EQxwGbYBjANkvpR0yfvG-iQkvhioChu7Jg1QR-XvEo4kgtaXd2ZDu6VIezVG8i5zWKRTntDLIE1d_Qt3NFK42knUmDiejXIeyV7Lxn_uzGpr_ayjG5yphVOJULcQNY29Qq8rP38Ng4jCbL4E5-JasPdAJypZICBTaomjujKIy8Xg1X8oBr5RRyVacsA-pt2FZJM0vhw51kRQdMMn_M5G2-L-ix_ijdr0g9BzUizQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G0XS7q7piblBC54t4Do9Sm3jI_CGi0KY-tsSsSAFANxmJ6PXGRm9W2QfTKKy0VG9wtgRloJmRFkNYWrsNZJiZ0mDMoIHXz262WXIqCG4rM9ptwyu_drAVoLa5zD8r6_AxVIa1FE7oY-dhYTD98EmfwUX1vTcn8h-fqo6tIVuK31KApeO8z0GIH3Jzy_96QfLreCMBKZm6jrZS_e5n_Wz-BpPsE1cItrWXfxfc5iNRj1cSR6LM56WS1N-xxZhicqntuTmqR915-hPpb7o18RUGjR_ZFOndpE6SWHMfk_4hbnu0zPOBts_0nG6FX6yK65zSYDD72SF6Gihfl-j6lezuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفسنجانی سالها پیش گفت من به خامنه‌ای گفتم پاسخ این همه ضررها در دشمنی با آمریکا رو شما به عهده میگیرید ؟؟ خامنه‌ای گفت بله! جواب خدا با من!!!  و خب این جنگ‌ها و تحریم‌ها و آسیب‌ها و کودکان میناب و... همه همون مسائلی است که خامنه‌ای گفته جواب خدا با من! یعنی…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5216" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db68225cef.mp4?token=aTnqMlPy_EoGCoVmzQ9c36Y1t6VCG5xOiyD7j7WgOqXuz2B2liX3nJQbznMUjftK0rcWsher-hYwJlLNOzjmkeEpuDUMCIjsb6Pu8RW0OYjdylr3M0N8dlK45IDBjjpgghE5nB6PUPW88yQUGeTbMilHkb-zThQcnU-ML9JvktQ6a5PILyp845Gfa9tf1_0xFxMWhGytpljBOmfD1hSM0Na1Rcw-7XFhKwbn77mYJ20BxB-zUdWGj_VgYQh-Hy8u_30L5IviOMPOt6DY0WsbN5D_Q7gd5ufS2b-IX5ZKVtlu7lnzkE7coPn4-O-JoAkc4MC8eZ0FDc4AhKRY0EoAFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db68225cef.mp4?token=aTnqMlPy_EoGCoVmzQ9c36Y1t6VCG5xOiyD7j7WgOqXuz2B2liX3nJQbznMUjftK0rcWsher-hYwJlLNOzjmkeEpuDUMCIjsb6Pu8RW0OYjdylr3M0N8dlK45IDBjjpgghE5nB6PUPW88yQUGeTbMilHkb-zThQcnU-ML9JvktQ6a5PILyp845Gfa9tf1_0xFxMWhGytpljBOmfD1hSM0Na1Rcw-7XFhKwbn77mYJ20BxB-zUdWGj_VgYQh-Hy8u_30L5IviOMPOt6DY0WsbN5D_Q7gd5ufS2b-IX5ZKVtlu7lnzkE7coPn4-O-JoAkc4MC8eZ0FDc4AhKRY0EoAFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴ در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته «دو گزینه بیشتر نیست» یا جنگ و خونریزی یا مذاکره مستقیم «برای از بین بردن غنی‌سازی و موشکی»  این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5215" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=fpQCqQZoQsPZWd6ri75cY2fpsZitv7Fv5ltaI5FTLCkUjGkWD6UNz9ZawSyuW1EKOSryashsmnySAaaGEk5x9hC0MwSj2LLuLNGYl8pMq8YUbk4R6OfhJiFpY-Zboal3GeYxFnxAsSoKehBcTkQJNCcURmm3ZteTDRmIECHHukFQ4wIG9OSzcpGpTM0KxF70Hknj2f2oac8fIQb7CBAUeXteExSb3o4p_X2IgAMav2HaKIM_yDSwhW5YF24FSPF76PKZBCWWcNaGX5zoGRMCpHdfvjvzOf6JKi2cEe8xpSsyK34ZBcWNKcxQ6lVo2CnVTm6JWGNERwzGXcIvsFG-YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=fpQCqQZoQsPZWd6ri75cY2fpsZitv7Fv5ltaI5FTLCkUjGkWD6UNz9ZawSyuW1EKOSryashsmnySAaaGEk5x9hC0MwSj2LLuLNGYl8pMq8YUbk4R6OfhJiFpY-Zboal3GeYxFnxAsSoKehBcTkQJNCcURmm3ZteTDRmIECHHukFQ4wIG9OSzcpGpTM0KxF70Hknj2f2oac8fIQb7CBAUeXteExSb3o4p_X2IgAMav2HaKIM_yDSwhW5YF24FSPF76PKZBCWWcNaGX5zoGRMCpHdfvjvzOf6JKi2cEe8xpSsyK34ZBcWNKcxQ6lVo2CnVTm6JWGNERwzGXcIvsFG-YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌نشستن و  با نخوت وعده «دردسرها»  میدادن برای آمریکا و دنیا!  «حالا حالا دردسرها» خواهیم داشت!  بعد که جنگ شد تقصیر مردم ایرانه که تاریخ نخوندن!!!  تقصیر تلویزیون اینترنشناله!</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/farahmand_alipour/5214" target="_blank">📅 17:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=EyoHr9hemHTLkUtuH3Onk0aZ-DatZgXQezeN1kNlLL1p9evATnlFBk-WFSPdCJIfbkbgle-LPF0p3ScXbwutm8o6M0D5kAkGBDdvOTiI4qaheWKf_4tK3ZpSfhnfFua7dYbhOr7o_N4XmnXySn8AeDzk15mf319f502NfVUBDqblE69u9LPidxPeMycft5mWlmWS3ulBdks5cSYpXup3TooJV7RH09BfwK9L4k1oJJzpHGhbLDFtaFwbFLOkbww1K4O6u6OiQp9q4D2r6etq66reZ6NoMNQ1_MkvkDPdtl-v3OQZ0ZAdHxUQ6MneqZlCm7d_oYTVucDslh4f4Lox3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=EyoHr9hemHTLkUtuH3Onk0aZ-DatZgXQezeN1kNlLL1p9evATnlFBk-WFSPdCJIfbkbgle-LPF0p3ScXbwutm8o6M0D5kAkGBDdvOTiI4qaheWKf_4tK3ZpSfhnfFua7dYbhOr7o_N4XmnXySn8AeDzk15mf319f502NfVUBDqblE69u9LPidxPeMycft5mWlmWS3ulBdks5cSYpXup3TooJV7RH09BfwK9L4k1oJJzpHGhbLDFtaFwbFLOkbww1K4O6u6OiQp9q4D2r6etq66reZ6NoMNQ1_MkvkDPdtl-v3OQZ0ZAdHxUQ6MneqZlCm7d_oYTVucDslh4f4Lox3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی! جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!  فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ، بی ایراد هستن…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5213" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTe7YN77T49h_Kuy0jXCjhHHuDqOXlhaAH1y1HLO9oYaKy2VQyOioMtGyoHj474Zvv480B1svRrE7w19waMiKEWCrMYUm29kTgxXUc9u7LFOLNLi5aLKnTkM7QAp2D8KyzkHCElVpgfLtl0U4uNZAPU9Y_PFmGZVCjkiXXiFVfXLFotw1RWfks9GrYRDbmFecQMtMlqpebgKrB9yZgIn7mm2WzwDmOEn2bcTRR0lmtikPMcc6SMgoFTH8FSKFaUR_V6oMA07UfcxED4i3yPy_UiHxkMd_e8IPz7UkwznhG_cPnlFyBPhRHLYJntTnHoQ9Y5KX9vrlDzgJozhs5eL_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی!
جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!
فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ،
بی ایراد هستن و مشکلی ندارن!
و همونطور که می‌بینید روی میز مذاکرات هم بحث ایران اینترنشناله و افغانستانی‌های ساکن ایران و دیاسپورا! مشکلات و دعوا سر اینهاست!
خوش به حال آخوند که چون شمایانی رو داره! هر بلایی که سرتون ببره، آغوش گرم آخوند رو رها نمی‌کنید!
شما اگه تاریخ خونده بودید راه شوروی و کره‌شمالی رو نمی‌رفتید! راه
صدام و بشار اسد رو نمی‌رفتید و چندین هزار نفر رو دو شب قتل عام نمی‌کردید! بی‌آبروهای تاریخ!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5212" target="_blank">📅 17:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ve6wZOdkKWiVCObW7MCo58iXlT5fOsUTOpr0MpNjylogucMt88U1G_sKjLfHaLjHJEfmlvDk282P3wQvcNHmn4GAkwqMmlYhjpZxgGAhLv97Gr0ZnSb_6FNzppW49hxLOQ36SJhiPeQlrLQdDfdDs8ETFZPd3juHI69Gz9y7MWhdT4dx4obxf6JMEpH5YbTKYVmMm2THcgh_foa46QJC7A2RXhN8bM_7XU3EkQbn1U1pkMIAQxhwoGvrUsStqOa_IxhmEV_IZldNd0CHf5S39NmHFDVfpqx8wcWCUfIAfWzEl5N28MWWlDytXOjrdUXWm7KJDRmmsFkWZdco1VywlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله جنگ  ۴۰ روزه به خاطر ایران اینترنشال بود و‌ دیاسپورای ایرانی!
جنگ ۱۲ روزه هم تقصیر افغانستانی‌های
ساکن ایران بود!!! یادمون هست!
فقط فعالیت هسته‌ای و موشکی و نیابتی‌های
جمهوری اسلامی  و ۴۷ سال آمریکا ستیزی و دنبال نابودی اسرائیل بودن ،
بی ایراد هستن و مشکلی ندارن!
و همونطور که می‌بینید روی میز مذاکرات
هم بحث ایران اینترنشناله و افغانستانی‌های ساکن ایران و دیاسپورا! مشکلات سر اینهاست!
خوش به حال  آخوند که چون شمایانی رو داره!
هر بلایی که سرتون ببره،
آغوش گرم آخوند رو رها نمی‌کنید!
شما اگه تاریخ خونده بودید راه شوروی
و کره شمالی رو نمی‌رفتید! راه صدام و بشار اسد رو نمی‌رفتید و چندین هزار نفر رو دو شب قتل عام نمی‌کردید! بی‌آبروهای تاریخ!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5211" target="_blank">📅 17:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYWV-Q7dnvJg59hsewCP6Hj-o16xCbE_eEOxxbg5jdKPX0M9vBWJ0kxc28s2EY0AJscFoxfZIlSKlfwdtgimDfFNQPv5_9iJxIO8fBqnjNoUJfWgSEkY2mEQHFqCJQAh_Q9RLZ5FJMJAXSuV84hWkyAO7Q6EPUKe-3lKtyJYYiRBdb5AWKAT8gM3_3ENoqjjJlOJTjdM36qrZznRJFOXkiTzDjAlJUpfu_8_IeLAPyJgb7qZJraLMuTbfOn-XrCYmMR5EXuWh4Eq7PQi0YEGKOfJbUEdDFUOE8ULHl4vZT5xytGn9lUMgW3sOR-i_yzt0zXYFOgkk7wkIOxrDG1dZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5210" target="_blank">📅 15:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMBtouf8rCvAfgLs_FSwOdFHKJBfJVvYnVFS6IY7hspjT_kWsGY8Hcqa2RPEW9o8duUmi6O5G6kRKSs6Rkt1yDOP5gHjeDWL2dNSs4tVgCOY5N5Zea9qXVkczQ6F5GMAF-gWrkTwRuaCEw6azWhFEbts0_Eb8y1fL0KbQymiYavc2onNml0WrLlPaKrbAbU98D035Ym2u0jIYZvj5XZ4h1tTSTFm1KlNQQindiHKPSaqwepK99oK86o2BqLnTEVrxmujzZ2aRUmWJB9mOTWSICUmrBLBmbyKIz5c2IIdJyBNC2HSiM5YfCOHDpd5Y-0wlWHxOP5-FvV1AlQk61a0JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل قلعه شقیق در جنوب لبنان
را تصرف کرد، این مهم‌ترین پیشروی ارتش اسرائیل در جنوب لبنان از سال ۲۰۰۰ میلادی است!
گروه تروریستی حزب‌الله لبنان،
بدون اجازه گرفتن از دولت و مجلس و ارتش لبنان و در خونخواهی خامنه‌ای،
به اسرائیل حمله کردند، اسرائیل نیز در پاسخ دست به حمله گسترده به مناطق شیعه‌نشین لبنان زد، بیش از دو ماه است که حدود یک میلیون شیعه لبنانی آواره شده‌اند! بیش از سه هزار تن کشته شدند!
چند هفته پیش دولت لبنان قصد مداخله داشت و تلاش برای «آتش‌بس» اما این گروه تروریستی و حامیانش مخالفت کردند و گفتند که جمهوری اسلامی باید این آتش‌بس را برای ما بیاورد!
(که بعد تبلیغ کنن قدرت ج‌ا بود)
جمهوری اسلامی نیز توقف در جنگ لبنان را در صدر خواسته‌های خود از دولت ترامپ قرار داده ولی هنوز به تفاهم با آمریکا نرسیده و اسرائیل هم داره کار رو ادامه میده!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5209" target="_blank">📅 12:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=hs-jZiQtSNUkeBNqWiOOlj6cBBz6tNfOBrMQ9HY-kwuizhymyO7ZwHfhYkQoyvzJ-I6YTlb0yuL4Fu3Q7S3bQSsED_SJE7sVyQ76hEMhMdVVHi0w62COvxqTAXwISb_3CbUzXykSbTHnEMzqL4BaeqlVn73xSxODfwzkSjuQhbtb8tT4Ke3GNSdan78rEsiLrBvQiVgfJR1pWkvB7qajsypEi9CBhGpuF0cylTQvio9FENIRRI_sBxpHw6IoUeer41CqA6CCwdJpQa4VSpebOGPr3p9_OAGz2aUD4W5YLYeswUdiOPNYXaTKyz20L3Jcg40gM6GlfBsUX-V1Hmm_pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=hs-jZiQtSNUkeBNqWiOOlj6cBBz6tNfOBrMQ9HY-kwuizhymyO7ZwHfhYkQoyvzJ-I6YTlb0yuL4Fu3Q7S3bQSsED_SJE7sVyQ76hEMhMdVVHi0w62COvxqTAXwISb_3CbUzXykSbTHnEMzqL4BaeqlVn73xSxODfwzkSjuQhbtb8tT4Ke3GNSdan78rEsiLrBvQiVgfJR1pWkvB7qajsypEi9CBhGpuF0cylTQvio9FENIRRI_sBxpHw6IoUeer41CqA6CCwdJpQa4VSpebOGPr3p9_OAGz2aUD4W5YLYeswUdiOPNYXaTKyz20L3Jcg40gM6GlfBsUX-V1Hmm_pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، ۱۸ دی در جریان اعتراضات شهر قدس بازداشت و پس از ۶۰ روز پیکرش تحویل خانواده داده شد.
امیرمحمد ۱۸ دی‌ در اعتراضات ناپدید شد. خانواده‌اش به بیمارستان‌ها، سردخانه‌ها و پزشکی قانونی مراجعه کردند، اما هیچ اثری از او نیافتنند.
پس از دو روز و در ۲۰ دی، تلفن همراهش روشن شد و ماموران حکومتی از این طریق به خانواده اعلام کردند که امیرمحمد زنده است.
خانواده پس از این خبر، پیگیری‌های بیشتری در دادگستری انجام دادند و آنجا نیز به آنها اطمینان داده شد که پسرشان زنده است و حتی برایش حکم صادر شده است.
امیرمحمد دانش‌آموز مقطع هشتم بود و خانواده تلاش کرد از طریق آموزش و پرورش نیز این موضوع را پیگیری کند، اما در آنجا نیز با پاسخ‌هایی مبهم و با برچسب «پرونده محرمانه» روبه‌رو شد.
این بلاتکلیفی و بی‌خبری تا ۶۰ روز ادامه داشت؛ تا اینکه در نهایت پزشکی قانونی با خانواده تماس گرفت و اعلام کرد پیکر امیرمحمد شناسایی شده است.
پیکر این نوجوان با کد «ناشناس ۱۱۷۵۴» به خانواده تحویل داده شد.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5208" target="_blank">📅 10:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=Tek6BUbjez2rvvNO55XRq1df-Qku0k0UwgywRM6wteDpfRRSeIjqgcX7RZ5rJFM4qvJEuDEUgMBrI2V_Nsj1OeaWG1osz5Znhym_5EkkVvHuPsajlLzj8G5OTzhyDlQvc-_aFXq6mM-xFo1zGbvsT7l0tnDCFfOFnLUnaDaF_OF602DpERWmg97K2uOH7-o8OEyCNtbBVtBYTu7IrsJCrIIjB2RxC_XbZ7RSEjGsyQUy4MvJSTHGs8j4Sq8oXje_CuTQE8k3SI9QCLk7KgPoz_OaAGf6xdmMwqW3IRC0XaB_BYyf4fErxq19hL1ecCKwf2o3RtJizHz8z5AZD4xqsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=Tek6BUbjez2rvvNO55XRq1df-Qku0k0UwgywRM6wteDpfRRSeIjqgcX7RZ5rJFM4qvJEuDEUgMBrI2V_Nsj1OeaWG1osz5Znhym_5EkkVvHuPsajlLzj8G5OTzhyDlQvc-_aFXq6mM-xFo1zGbvsT7l0tnDCFfOFnLUnaDaF_OF602DpERWmg97K2uOH7-o8OEyCNtbBVtBYTu7IrsJCrIIjB2RxC_XbZ7RSEjGsyQUy4MvJSTHGs8j4Sq8oXje_CuTQE8k3SI9QCLk7KgPoz_OaAGf6xdmMwqW3IRC0XaB_BYyf4fErxq19hL1ecCKwf2o3RtJizHz8z5AZD4xqsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGXKfCYN5rlAwomX_e4Fp0-7miOkSgiqTN1TehILOGKLLJVDh7XkGzdBELfQTrdPhjZMOCjXAswygJhV3UBeBX0ZkVLe7GSD77fiFGaY4FaKQEKQ0qvehTfZcLUQBz_TKbtOyeiwHZD2j2eCZhoSEj4gtAZ9mGlz7fXy4em1Wgjfzy3QFh7ayJRI37UdomesmsoF0OM4aCutsCN3QsNFeDoMco4Y0WHyqe2H8GwXLYRpe3OK_F2wU2-CKI9luJTG2rnhM6LMO3PazxvCtNnlE96tgKEq_cPYnEqEomwB-00_vvpLh9fXAa6_Vjp2GB7EpElG1zhT0ADQTBXdOpjn6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی با آب و تاب می‌گفت
به امارات حمله موشکی و پهپادی کرده،
حملاتی که ۹۵ درصدشون توسط
سیستم دفاعی امارات خنثی میشدن!
اما امارات در عوض پنهانی با جنگنده‌هاش
حمله می‌کرد و جمهوری اسلامی هیچ سیستم تدافعی نداشت!
یعنی اگه به ایران ۱۰۰ جنگنده، یا ۱۰۰ موشک حمله می‌کرد، میشه با اطمینان گفت ۹۹٪ ماموریتشون
رو انجام میدادن و اهدافشون رو میزدن!
کما اینکه اسرائیل ۸۵۰۰ سورتی پرواز در آسمان ایران انجام داد حتی یک هواپیماش آسیبی ندید.
آمریکا هم ۱۳ هزار سورتی پرواز انجام داد.
آمریکا همچنین ۱۰۰۰ موشک تاهاماک به ایران شلیک کرد، جمهوری اسلامی قادر نبود حتی جلوی یکی از اونها رو بگیره! یک در هزار رو هم‌ نتونست!
جنگ با امارات رو جمهوری اسلامی کلید زد
و هنوز هم کامل مشخص نشده چه آسیب‌هایی
ایران در این جنگ متحمل شده!</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5206" target="_blank">📅 10:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZ0X0vwkGWE82u8CFIVOgKXqn8EGWHOC5kc9EjAtkTvhTbx_gpFTUTI0gFPDBUJMoLu4-cn48I3R1B1D4BNZGEOBvF9xhvvmUokW2sPazfwpdokm5p9f7seLmqnEPsBgdUrCzHeQNxZs2txp6IHIC2EwBKakiHYK_CvpIs18OXYR7228XMNb8WwLM5Zyv7-riCNnLQOit8oX5O4dWelZxVXKv0NZcVtFnc6F1YlIdDkVnRFzRPnYf_14XUVXZLYun8ZFcJun7Tip_DBQp72WpthR6iJ4FUs1qi_Qq7IBV3JaiifMXEmlBN2HZ-eFXq2liN3OniJFxh83eyD_uGsIww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o87ZOdwMotPx4L1i6NDa8qvJRuhnOjf9UPwigDYOBc3HI4dbntUVKiFcwbxSVHpSqqH_PXR0HRaAbLZt2Z8pxOaZOBX8iN84bQPzuM6McfOMDaetA7rHjlikc-v29BJIfJEc4Qh1yH4TTIqjVcvasD616V3HP6bA7-OF4CtB6GBiHKySkShuNByGECgoA3BpTf-9vYO1V8pPDT6_EFM5cUbPnHFdvcZJVqy3wMmCVkvAsP9pB9ji782yH5kR5SKiNMkIVPUXPNGMBr7yVeAmCucIo2ZczElZg2CHHXttR3d_POXBgQXg9kqx9Vl3q5EYnx7HZcserK0lGdnD4Ed6Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFR4YlxQsWZBEnCPeT2XWkRx-mvQ0E1N6u4WlZK4VR74ivzJIcPFrRiMDzCEoORtNyDg8-hBxdBdTGW8VR2XI81kY4vDKAeyHM0PqmUTAxs6tlEQUz_EerupbP7bfrzs83dT9qeepCUFdmguaL8-PIAzpaLNbRlRwLg7I9MIysPo7m5MYWIs8nJfCNOnJ05tidpOK9_CJLHvYsv920-iuzDDU-fGoUoG5G8BQeArj35nRn7xmNEMFaSU6JfOOLNvjo91F4GaS1JH189XB5dZzA0z-cxYbrE364G8JRPe7F6v9esjW5evQfSgndg2h6NJ0VIamPkwRRixytugjUJmcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی بهتر برای جنگ بعدی …</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5202" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : برای اتخاذ تصمیم نهایی اکنون به اتاق وضعیت می‌روم.
«ایران باید موافقت کند که هرگز به سلاح یا بمب هسته‌ای دست نخواهد یافت.
تنگه هرمز باید فوراً باز شود؛ بدون دریافت هیچ‌گونه عوارض یا هزینه‌ای، و رفت‌وآمد کشتی‌ها در هر دو جهت به‌صورت آزاد و بدون محدودیت انجام گیرد.
تمام مین‌های دریایی (بمب‌ها)، در صورت وجود، باید از بین برده شوند. ما با استفاده از تجهیزات پیشرفته مین‌روب زیرآبی خود، تعداد زیادی از این مین‌ها را از طریق انفجار نابود کرده‌ایم. ایران نیز باید فوراً هر مین باقی‌مانده را جمع‌آوری یا منفجر کند؛ البته تعداد آن‌ها زیاد نخواهد بود.
کشتی‌هایی که به دلیل محاصره دریایی بی‌سابقه و فوق‌العاده ما در تنگه متوقف شده‌اند ــ محاصره‌ای که اکنون لغو خواهد شد ــ می‌توانند روند بازگشت به خانه را آغاز کنند!
از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدر و مادرها و خانواده‌هایتان سلام برسانید!
مواد غنی‌شده‌ای که گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌شود و در اعماق زمین دفن شده‌اند ــ زیر کوه‌هایی که تقریباً در نتیجه حمله قدرتمند بمب‌افکن‌های B-2 ما در ۱۱ ماه پیش فروریخته‌اند ــ توسط ایالات متحده از زیر زمین بیرون آورده خواهند شد. (طبق توافق، تنها آمریکا و چین توانایی فنی انجام چنین کاری را دارند.)
این عملیات با هماهنگی نزدیک جمهوری اسلامی ایران و همچنین آژانس بین‌المللی انرژی اتمی انجام خواهد شد و این مواد به طور کامل نابود خواهند شد.
تا اطلاع ثانوی هیچ پولی میان طرف‌ها رد و بدل نخواهد شد.
در مورد سایر موضوعات ــ که اهمیت بسیار کمتری دارند ــ نیز توافق حاصل شده است.
اکنون برای اتخاذ تصمیم نهایی به اتاق وضعیت می‌روم.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5201" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SRQylNdhctVQ41OobG9w9TQFMO5hheilYiip_pTI5YMuVZa22M0dKY180jguyUjzOeWXbJEkJ1msfSHYI6tA42afDWUokFEMV2XuItoThp5GgsobeOEgdeFwqT9mWqJO10j-OChatM8oUeA_64Yz_PBmA4RbewlGBVOm--7SJklIX1bscBlbRyM9P0nlVgQsulfO4oolhAFzwEsu033uBr7fGxCMt2xrRwBf-ZtFMxb92PWonvrpMzR-AiGM3i5CFrJjYl_2fqcaeRtR078sjdkclwxPIbPw8Fg20MENwXomIYil-HnaFuoEbpXq7Ax5CpvlP1gdtImIps05mnStfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LOTagsaurOfoLWvK42AvK6O_XQeECxuK49TwqNO_eqlMEY1qHd6iO2ayDcj-0LsMJeYJweuIg7aiEFKQDsGD1cSkhjwwm6JypS_HbokxEiofyWs4UK8DzdkSAvETEm8npA3mEeqvl-EpOv9I9hwoBYINkgCj97vbbJPMZs1A2j1PwF32HmtxHPxIbZK7H759QSCW343b4LUKpVMu5MjOeKZa1OmXxZwpCFA0DY8LuhbyAwneB7AbAjLEDvKBNx3VOeTwcEeizeqNWtQAM8Q5SnKw4UzbQ2oldalH3ojcXst66yqWFLTm69KzfAy88zKi4eD0CKODnV7OPgmLemhp_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
لبنان سفیر جمهوری اسلامی رو اخراج کرد!
گفت «عنصر نامطلوبه»! گفت که جمهوری اسلامی عامل وقوع جنگ در لبنان شده و جنگ
رو به مردم لبنان تحمیل کرده.
اما سفیر جمهوری اسلامی در درون سفارت خانه موند و گفت برنمیگردم ایران!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5199" target="_blank">📅 18:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TC-UYt5QWnCBrTmIMx8vVx4OF6AwIi8OvWO52FzrWpY4BfT5KwjrmZRptJL6zbiyIAF-petU7hvw7CVb9E5yVEP95RVqAjnSCuk8v__xw2NsBG74svFcTqf9F6gZwOS-9pUHBFDMMEoA40kSENTo4W7fnkcDAwoVTX4gRHM1fR5PvrvEnjth-yNFojuireBMqLcpsN_n7xmL6un2XNwvdVFSD_d88vRwoTw5MTbTEL9qx-ASIixNQ6JKczrkHWhgGq3peGGiWUapgfFjxcpUVF9TJYKrza7k3onWuH1l5Obm6ObpJHf8OdanID0-LwJ-WIue2-lxDbVADkvMByfghA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eepMzVuA0zm4GjdzCVCTExQnxUChPsfZV19K4hxezibm_NtQyOkawz-8xJrb_5h5VAmT-aTMq4mOFgk6CNux28_ZMTQ6SCLtt5hUVROHT-5d3BoeYUDwsDiL5HYfIMznI6ExihYBlBrWISwBvhvd63Q3tz1_Zm1AsGmxOmRKyHLK2UrTCpWsY73-YqbHOPtaHZFA5pXfLL4pT9N20E58PrVU_jfCqL3USkF5kCi0eHk0KmUZLwUa6EyN-9e9yc-hfYfsKAa2hYBbLY6eQIUSVA6ZEUVJfHcCEYPNaMFgloknx6UjPSkMcLPFp4S8dMvZnhCA8X5OFriyiNQv-TFTzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
درسته هر شب توی خیابون‌ها بزن و برقص و عروسی داشتن اما در افغانستان گدایی پول میکردن :)
سفارت جمهوری اسلامی در کابل در اواخر اسفندماه رسما تقاضا کرد که  مردم افغانستان به جمهوری اسلامی کمک مالی کنن!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5197" target="_blank">📅 13:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=Lbs3rYqfPv438112WXskyV2glrjTFXwdiQlbw3sIlO251LGIQQHCkgK38ZSO4cEu_FhN3zJBCH4viE07-A9b2NUjpcpFoajRERP2NFhedclU9b6Hb3Vf_bqklCiFvTMFoICxlQbdRG_3CxCeYtjaS2MR-s4IsiEgKzZK_A3zbbyxwy9V7SWndoNz_7jO6bMerMuAhkjvxI432MLK10msadSoiqv9ot9S5__3ujABoqkE9S8L--GNgUpBJIEhmNa2YC_sH--55UAgBFApiv99kTkYqrnfFx2nBC3otn6maqKl1a2Oc5rlJtPsCR9LvZpDDsMeZuuyLpsPmN0IGhf40g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=Lbs3rYqfPv438112WXskyV2glrjTFXwdiQlbw3sIlO251LGIQQHCkgK38ZSO4cEu_FhN3zJBCH4viE07-A9b2NUjpcpFoajRERP2NFhedclU9b6Hb3Vf_bqklCiFvTMFoICxlQbdRG_3CxCeYtjaS2MR-s4IsiEgKzZK_A3zbbyxwy9V7SWndoNz_7jO6bMerMuAhkjvxI432MLK10msadSoiqv9ot9S5__3ujABoqkE9S8L--GNgUpBJIEhmNa2YC_sH--55UAgBFApiv99kTkYqrnfFx2nBC3otn6maqKl1a2Oc5rlJtPsCR9LvZpDDsMeZuuyLpsPmN0IGhf40g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=NJqnOCQ57PqrR0X_e7FVfU5XJICY5wWH83wCd3NLg-mTlT4Ns0kKaFkwJiDuXp9GfI4cPV0U9Vs8wgByl_BaBW7OyrBEGQOcroSKJfIzyFM31_i4Q2n_-0Wpz67K-ZOOANO6FQNd38DkNPU92BwEDoMO5vhWLsjXjfHleisKNgX64Xr54h3PB-PbmIjCWfbnKSexxCZKLyUro6Ec0BJ1_eLHDu7VDMT6BobFuzH47wl1CUL6m5e7h_1YfCp2o_dvJCq-phMvzCnkeaAfV_bXUCMiiFQnhqhz8j2JKPFIzARu8195NqL6Srm1DkdaA-X2Qn0QV-_Yq98GuaNLDqfCbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=NJqnOCQ57PqrR0X_e7FVfU5XJICY5wWH83wCd3NLg-mTlT4Ns0kKaFkwJiDuXp9GfI4cPV0U9Vs8wgByl_BaBW7OyrBEGQOcroSKJfIzyFM31_i4Q2n_-0Wpz67K-ZOOANO6FQNd38DkNPU92BwEDoMO5vhWLsjXjfHleisKNgX64Xr54h3PB-PbmIjCWfbnKSexxCZKLyUro6Ec0BJ1_eLHDu7VDMT6BobFuzH47wl1CUL6m5e7h_1YfCp2o_dvJCq-phMvzCnkeaAfV_bXUCMiiFQnhqhz8j2JKPFIzARu8195NqL6Srm1DkdaA-X2Qn0QV-_Yq98GuaNLDqfCbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید
در اجتماعات حکومتی شون
هر شب عروسی داشتن!
«صیغه یک ماهه»! در برابر «یک سکه» :)
با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وقتی شما نبودید پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،  پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!  حتی زودتر از پیام‌ شهردار تهران!  حتی زودتر از پیام جوادی آملی :)   پوتین در پیامش نوشته بود :…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5194" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gQrMgGNa7ZcSiwO9iRYxj0lQ2eiBhcM_5v30lRd0mF0hgLktBPKdlSawJ3RnZHBblMi0tpqLW3t0mAQiTPCv5sm0FGrEc-6unVPcma0WwKLB-ErvDBw2lVd2-H47zQLGJrbhWHlhMpUa3VyThimzXhAuvN0zNGP5zh7MHG7qxIvdhRzjgn3noG8i-c0B3-KYpckwrREbvCUzFyF2bbmtPiWUyCVPJJgaOmR25IMSDGhuE4y8FQiXJBN6KXcLAEr14UPj4t2CWu5kAc6JC1lDVQW0demzQKWDiBq0GyV5kHIE_x4L65gRh6X6H5Loantsp6VF74rtCfZ9sej216o-jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NLF3dE5Z0V2D3rkvOqHferZgTmZbR4DtqoWvR4MyGyvUQ4YRCAGRRRuWCTsZ3DmGgkTSjMVSQ1maSMJcHITWVdvZ8UBEJuNvs4_16MdY2eLUvKFskrKY5q8_l4CTM0C2NEBMTxOy5bnfRWZIOfRr8ftJQLVVI-dY2p_wpBX8aa8FG1fG5XwpaVUUGnxNgGEZ--eKVVoa_O4jGot6M5m9i-r8uRtmQnAqA1ep2GABVJ0P1rcgAnOmEs55ZF5igzRUvbWtG3vlBA-fJ6ANRN2H1CChhjYEJBRKn3ugDEseo0f5Fv63EEWWfatYKMZaevsD9E2Jv-BvXb_temsCREUHcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،
پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!
حتی زودتر از پیام‌ شهردار تهران!
حتی زودتر از پیام جوادی آملی :)
پوتین در پیامش نوشته بود :
«اطمینان دارم شما راه پدرتان
را با افتخار ادامه خواهید داد.»
پوتین راه پدر مجتبی خامنه‌ای رو دوست داره :)</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5192" target="_blank">📅 12:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=Gx8QUhk9dpzzVZzc_Uc67FB8nGEg3BPzJi1njtHIUbH1Yc_-RyStelD7MwXCddqBfbvIT5ndXwDMpQAFcFGUDIvsY8w6Hm6Im46xXvhMml3HBff7pS64jJJADIlXilmjhXqRCNhuBnB2mpImAa2OiU9khh544CXqBucjJaERwzlTZwca1IaTFhfKxbw5C6_SmiCbTDmrW6hubgoUZZ70K8BV-l1uW7FxWrvFLmVCXMqEic9yqO7rQsMdaKBhsPSZ_hNL1YOLYwT2AyxSoa-3B4uG1ug-3JAx-JYgANDAf_H0xBC5sRBrplaw4uAIglJ4QoXYMSFIezPAQGSJQni0EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=Gx8QUhk9dpzzVZzc_Uc67FB8nGEg3BPzJi1njtHIUbH1Yc_-RyStelD7MwXCddqBfbvIT5ndXwDMpQAFcFGUDIvsY8w6Hm6Im46xXvhMml3HBff7pS64jJJADIlXilmjhXqRCNhuBnB2mpImAa2OiU9khh544CXqBucjJaERwzlTZwca1IaTFhfKxbw5C6_SmiCbTDmrW6hubgoUZZ70K8BV-l1uW7FxWrvFLmVCXMqEic9yqO7rQsMdaKBhsPSZ_hNL1YOLYwT2AyxSoa-3B4uG1ug-3JAx-JYgANDAf_H0xBC5sRBrplaw4uAIglJ4QoXYMSFIezPAQGSJQni0EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم مشهد از خبر کشته شدن خامنه‌ای</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kh0KSEKnM_2ddziAiG-8uleBjhFJzTbPKwKSPoDNtjaTdUdCVUfaYqh6BYym73YSQBLwcNFr82UAptofIJMbS26avVh1Is5QmuDy4N2EKCFaNzY0SUCE2BKTL4LUgKSkkL3Et6fcy4ZNN-4uKeuM2A3wCUd6TyXwELKP8jz0PL1rl1o5jVLI4LQahswTtKrA89xIC2DRx-39fG4aDYNFXAHyU_RpHqjyDyqln0nJ6X92PW_J6TFHikcX4DByZk75nV0I-DX8V_DKJp8se8OCDr-U7-O7jPgiAU8GtZTgJ1IEhOEc0bofLI8McYQudI4YC9slDv5ClZ8Lv8sZKpIzFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نکته جالب :)  امروز ۲۶ روز پس از کشته شدن خامنه‌ای  در کره شمالی هنوز خبر کشته شدن خامنه‌ای منتشر نشده!  فقط اعلام شد که مجتبی خامنه‌ای،  پسرش جایگزین او شده،  اما اعلام نشده که در طی یک حمله نظامی  خامنه‌ای کشته‌ شده.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5190" target="_blank">📅 11:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‏حالا که تشریف آوردید:
‏از ۵۷ کشور اسلامی، فقط ۸ دولت کشته شدن «ولی امر مسلمین» رو تسلیت گفتن و ۴۹ کشور سکوت کردن!
‏عراق، آذربایجان، تاجیکستان، پاکستان، لبنان، الجزایر، عمان و قطر تنها کشورهایی بودند که تسلیت گفتند.
‏بزرگان جهان اسلام چون‌: ترکیه، عربستان، اندونزی، مصر، مالزی،ازبکستان و… سکوت کردن!
‏تروریست‌های طالبان هم حمله رو محکوم کردن اما تسلیت نگفتن!
دولت فلسطین حتی حمله رو هم‌ محکوم نکرد! سکوت کامل!
فقط تروریست‌های حماس محکوم کردن و تسلیت گفتن!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5189" target="_blank">📅 11:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
امروز : کشته شدن ۱۴ نیر‌وی سپاه زنجان بر اثر انفجار مهمات عمل‌نکرده</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5188" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5187">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های جمهوری اسلامی  از بستن تنگه هرمز خبر می‌دهند.
🚨
🚨
🚨
سخنگوی قرارگاه خاتم : به ۱۴ پایگاه نظامی آمریکا حمله کردیم و «صدها» ‌تن آمریکایی و اسرائیلی را کشته‌ایم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5187" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
