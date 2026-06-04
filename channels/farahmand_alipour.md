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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 22:44:21</div>
<hr>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sq936ugl26sbwnyE8iB79fB7noR5SqHorlpTfEf4JWFcR4T8eaoDeYDG48FmljMzDqMRdMtFNeDSPO-OZuF9ZWCiPlunWVwEFQ48jb_HekziTxJDe8_xWOvuAoKcAPb1J_lZ3JmWM3F4ZXLbEccpXTzdxcw3O8Ykkk6FTIjNQ_wNYvvaawlMT0YMXXFwwD2PX-MScveol36gyZ1r1mGap2XVtIqv0MwGzLZvWo7DsOligRE2Af1fL4zaL5yYb37mvqLPOC-y3qfiEdAvsU--D3Wn10-8zc-pgGSo9zt1WJVytyvxbqwwYeia-8BK0elWrmaO8DheQlBRJhAKLBC24g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/5303" target="_blank">📅 15:50 · 14 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5302" target="_blank">📅 13:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvsN94JSKqsljx9mgbDBRgV_llqF_WAaZnBseHlLELQKKJ3ws65dQqANeVtfIJlnDw9bUkamsXNJMxX4eg__jKNzrsB0NVBfezZhjqJtYhR-RnVEK9Ckf5mA_EDe2PbsO1jc5aPs8PmMOp7tRRFSZ96-ank0yI4ROcmu4mFjI_To5cjVmnd47taemzRA5xmbn_UiuMpRST9nNDkzN5Xvrk5AnGgzG21bPRm0MWUsQeVO7Io2NPo7jATmNBZmLQjg97FZaJOthxu6wfddjrAGzlSlU93BlZwS4XZ0OI1MIJCBBo2EDJ72Ws3dw1s08pVb6fNIhm7-33CJDgroWH2PcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی در ۵۶ سالگی درگذشت.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5301" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تصاویری از فرودگاه کویت
پس از حمله جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5300" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPQwDsb8e5BbH1hHBk83pdT9vAG1x79B7h0LBynwZ8NPcttZT5t3RZopf3hiWBBIv7zpMES_kv-3AWxgm-ma703Uu2nAx4--3HQ5b5KK8QyprJYZ9Ft5P5S97-VAKMwUo-QsunXTOQ7KcmsjlmuzbaVXvSL1sfB4EfGoOvbt6jf_AiZTzFWg1_G0QFq4aDz7AkSXX1ynXd6PIOxsZVA2dbUQrB4xdLPIEoldADTVvkmYTF9u6DhTZmrAR6os34aoVIF3XBtbtST4oRCo3oUSJlUc00N81jLobAJ0zjLd2Nj7V9Xw9yrxeItMrKQxrMm4ynMaC8bhmRAJY5cnOCQO3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5299" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oc7NeffMHacldACBXwHgF5KB9SWjsA0sz6BxNQeeGnJE-jIxQlN9t2ErNgCfzeUItF56PxYjnHLcBuelWVdoGpaz1osWXqIdC7EfeKEE5uwz1T8dONu3kkzI1TBluBsnmvHxLKqmiyauifcRfTzMUhcRTWmaWynDqTor0yBJcRh3JrIXAu8Pc-s0wEi7jxEIWhYsYErpmZwhHuX8CYUWGs8mQdF2qt9y-Oo-5BgiVAFlA6afJTyFra4MDCbMncbOYi8b6pcPSahlaJYSjrN77QaZhCM7H4bMRL8PcC3kVzeH2v7OI9iex9515vHqU-mH0Rvt7oZ0_c_FYX-z5VjIiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کویت ضمن احضار کاردار جمهوری اسلامی، دو دیپلمات جمهوری اسلامی را به عنوان «عنصر نامطلوب» اعلام کرد و از آنها خواست تا ظرف ۲۴ ساعت خاک کویت را ترک کنند.
وزارت دفاع کویت: جمهوری اسلامی امروز ۱۷ پهپاد و ۱۳ موشک بالستیک به سمت کویت شلیک کرد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5298" target="_blank">📅 16:51 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5297" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کویت : در اثر حمله جمهوری اسلامی به فرودگاه بین‌المللی کویت ۶۳ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5296" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بخش بزرگی از انگیزه جمهوری اسلامی  در حملات پی‌ در پی به دوبی را باید در عقده حقارت جمهوری اسلامی جستجو کرد.  شهری که برای ده‌ها میلیون ایرانی  نماد پیشرفت و توسعه بود، که ظرف ۴۰ سال از هیچ به گوهری درخشان تبدیل شد،  و مردم ایران دائما دوبی  را با ایران  و…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5295" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5289" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5288" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5286" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">وارونه گویی!
به خاطر دشمنی با اسرائیل رفتن دور تا دور اسرائیل گروه‌های مسلح ایجاد کردن، پول و سلاح دادن، حماس، جنبش جهاد اسلامی، حزب‌الله و… تا دائم با اسرائیل در جنگ باشن، خود خامنه‌ای بارها تهدید کرد و گفت «کرانه باختری» رو هم مسلح میکنیم علیه اسرائیل!
حالا که اونها برگشتن حمله کردن، میگن ما اونها رو برای دفاع ساخته بودیم که بهمون حمله نکنن!!
نه خیر! ساخته بودید که حمله کنید! نه دفاع! که هم اونها رو زدن، هم اومدن سراغ خودتون!
و الا اسرائیل زمان حکومت شاه، با ایران دشمنی نداشت! جنگی با ایران نداشت!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5285" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‏روایت سی‌ان‌ان از درگیری شب گذشته ج‌ا و آمریکا در خلیج فارس
‏ایالات متحده و ج‌ا در یکی از سنگین‌ترین شب‌های حملات از زمان آغاز آتش‌بس در آوریل، دست به تبادل حمله زده‌اند
‏به نظر می‌رسد درگیری‌های شب سه‌شنبه زمانی آغاز شد که ارتش آمریکا با استفاده از موشک هلفایر، یک نفت‌کش با پرچم بوتسوانا را که به سمت بندری ایرانی در جزیره خارک در حرکت بود، هدف قرار داد. به گفته فرماندهی مرکزی ایالات متحده (سنتکام)، این کشتی با محاصره دریایی بنادر ایران توسط آمریکا همکاری نکرده بود.
‏در پاسخ، ج‌ا اعلام کرد به یک کشتی با پرچم لیبریا موشک شلیک کرده است.
‏اما تشدید خطرناک‌تر پس از آن رخ داد که آمریکا یک ایستگاه کنترل زمینی نظامی ج‌ا را در جزیره قشم، نزدیک تنگه هرمز، هدف قرار داد و این موضوع باعث شد ج‌ا به کشورهای کویت و بحرین در منطقه خلیج فارس موشک و پهپاد شلیک کند.
‏ج‌ا اعلام کرد که «یک پایگاه هوایی و بالگردی آمریکایی» در منطقه و همچنین مقر ناوگان پنجم ایالات متحده در بحرین را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5284" target="_blank">📅 09:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خبری که ایتالیا رو شوکه کرده:
یک پاکستانی در جنوب ایتالیا،  با ریختن بنزین ۴ نفر (۳ افغانستانی و یک پاکستانی) را در یک خودرو به آتش کشید و کشت!
https://www.instagram.com/reel/DZF42fzqtho/?igsh=aTJocnQzcWw5dWVj</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5283" target="_blank">📅 08:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سنتکام : حملات موشکی جمهوری اسلامی به بحرین و کویت ناکام ماند. موشک‌ها رهگیری و منهدم شدند.
به اهدافی در قشم حمله کردیم.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5282" target="_blank">📅 08:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RT9kBh34RMxPHNtKaoY8_4loGPxBI_uWhuDiwPi_0tNJjnAxVhOS4SCI3mJ_v8H3InwbgRmQ9Aw_GD5omtYHVw0fv-G5wJ0eE3f9q8HSfeY-6sL-P_P_H5Cez7kV4Iam0y-aZ9-9tTZQNpDb_UcyWUbxPToynB3RoDJGmB_yvV0jaUwMzrgAB1ud6zg59NE9VjsLqF2rrk44UJ0FiF6BE_GwPeAAZTxexwbiR4gHRp8nk4ZO3VWsbh9Otqxy_mo9Ow3h9RFCaaLAjm3EcdmGTfk0j8eelLQlmDcyu3T6WJjXh9gLnx5G-IT4s8zwVajAAkrYJxfF7dZ4lwZTMEF_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم اعدام برای دو برادر دو قلوی یتیم فقط به اتهام داشتن تصاویر ساختمان‌های تخریب شده در تلفن همراه</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5281" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5279" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=AhyPt0rY1hCobB65H5RGkFCfdundQr3-GweiHyFjMCr9wN9Tchq8dcHMl0mbEY7Mfu5AIFGMHqA3TAPtEkO3ABE6-8zkeLJMszCwBNXk3i6BHadxXVSc4ci-_9Y8WgNw6H_Ekkym5lnf6SjiyoF6WbTH52sD-5eYJPvZl36IPkrkiur2P9Ic_tgbyWHUwI3xWD2uqCT4YDmI1yC3J18GMBugloL-gNlMYcXGPuZGO9K72i4KIGlKYlXGP2QgJgb8V53lyeDDVDpUhek9bT39okPXqrN8blFjm6SiT5IJDd5oBbJtg-fSTozlghEOoiSWCZlJwEKnlUgyXFxSePvNGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=AhyPt0rY1hCobB65H5RGkFCfdundQr3-GweiHyFjMCr9wN9Tchq8dcHMl0mbEY7Mfu5AIFGMHqA3TAPtEkO3ABE6-8zkeLJMszCwBNXk3i6BHadxXVSc4ci-_9Y8WgNw6H_Ekkym5lnf6SjiyoF6WbTH52sD-5eYJPvZl36IPkrkiur2P9Ic_tgbyWHUwI3xWD2uqCT4YDmI1yC3J18GMBugloL-gNlMYcXGPuZGO9K72i4KIGlKYlXGP2QgJgb8V53lyeDDVDpUhek9bT39okPXqrN8blFjm6SiT5IJDd5oBbJtg-fSTozlghEOoiSWCZlJwEKnlUgyXFxSePvNGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امشب جمهوری اسلامی به کویت
و انهدام موشک‌ها در آسمان کویت</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5277" target="_blank">📅 02:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سنتکام:
نیروهای ما یک نفتکش خالی را در خلیج فارس که به سمت یکی از بنادر ایران در حرکت بود، متوقف کردند.
نفتکش توقیف‌شده توسط نیروهای ما، پرچم بوتسوانا را برافراشته بود و خدمه آن به دستورات داده‌شده تمکین نکردند.
یک هواپیمای آمریکایی با شلیک موشک به موتورخانه نفتکش، آن را از کار انداخت.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5276" target="_blank">📅 01:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ارتش کویت : حملات موشکی و پهپادی به کویت.
برخی از رسانه‌ها از شلیک سه موشک از منطقه‌ای نزدیک شیراز خبر داده‌اند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5275" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
شنیده شدن صدای آژیر خطر در کویت</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5274" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5273" target="_blank">📅 01:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=Z5hj0h_OaT88mjg2hW4g_0VnkdSJjDdSLXGOt4GPMpoiYxwaFc-O0kpdEIibhLlSpQzm3INMQRBnC9HXkeijfxF8iHGzlb7IH8j9sEFDUC57DdqW6hTvFLt5tzwV25BRrjIqvtcn_IuuCuW3JDR-cM8yYEP4tgkm4dtDFdpxDUrm0MINIIPs8RurOFyM9LubTtu337wDMAHb_uoM7SBSzE_J075eWEpZ2JRc46gO7_CqEIjE2Mfn9wWfQzq5Ll6mj3kviaLL0Hkn28XmyqO2lkqYh_Nsurqazg8QEp6r3JT1RhxDTyYw76CSoL8fXEddtxQ8XwGfKM_bbD6Rfp8YBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=Z5hj0h_OaT88mjg2hW4g_0VnkdSJjDdSLXGOt4GPMpoiYxwaFc-O0kpdEIibhLlSpQzm3INMQRBnC9HXkeijfxF8iHGzlb7IH8j9sEFDUC57DdqW6hTvFLt5tzwV25BRrjIqvtcn_IuuCuW3JDR-cM8yYEP4tgkm4dtDFdpxDUrm0MINIIPs8RurOFyM9LubTtu337wDMAHb_uoM7SBSzE_J075eWEpZ2JRc46gO7_CqEIjE2Mfn9wWfQzq5Ll6mj3kviaLL0Hkn28XmyqO2lkqYh_Nsurqazg8QEp6r3JT1RhxDTyYw76CSoL8fXEddtxQ8XwGfKM_bbD6Rfp8YBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.  پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5271" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5270">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=LU--LwDnpgGzjjIHOr2MelqnMuXHfqvZZqlNNOVP-p6WgQy694aMNVPGglKbO7YBMioRdtRmQ8KuKymz47T3bG-sUjgCI8jpCuY6sSr905Gzw1ZmS8Le1DKliMmNbl6igfyeJCc0SfYq7rRSr-PvzlDMgnDJ1s3bEnxcOTpsInCN_FkGI-MCFBNvhL-SV9GgbQNUh6dbZ4veo6ej-t4Z791e2UvYqkcL-57RjVUpgDtMFbG6Jv_TlQywkDr6g4tsW2ULd-PpZRZzNCXPbhDRe9TQsnBiy3qodD5-dgLKOi3aK8GfLM2sznxdzgM94zzHBKvv-qfLyUJ8Ugkcai9ZNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=LU--LwDnpgGzjjIHOr2MelqnMuXHfqvZZqlNNOVP-p6WgQy694aMNVPGglKbO7YBMioRdtRmQ8KuKymz47T3bG-sUjgCI8jpCuY6sSr905Gzw1ZmS8Le1DKliMmNbl6igfyeJCc0SfYq7rRSr-PvzlDMgnDJ1s3bEnxcOTpsInCN_FkGI-MCFBNvhL-SV9GgbQNUh6dbZ4veo6ej-t4Z791e2UvYqkcL-57RjVUpgDtMFbG6Jv_TlQywkDr6g4tsW2ULd-PpZRZzNCXPbhDRe9TQsnBiy3qodD5-dgLKOi3aK8GfLM2sznxdzgM94zzHBKvv-qfLyUJ8Ugkcai9ZNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=VJzVcXZjb8Wb-44bRzCIjkhQ0748qouYkN4XW1BfbgdnsFjUXfiX825uMSZUyAceqE6-cNj6jCCmpmAUqsp_IQUzQBV5Mq5iZ4tqq-T6bpvWZ3XkkoRVUAojy8GwGfXxNG9LMMViGEmAGk6VXkWga5DBXPFKUbGaTswZa_zhqd-bLOu8JA_a3kOgD8D2JMKUm_KQ50zU8DQoIbrg7pTlucBA_66TbUQZtebjH6MIwtN49m_j_EaPIy1hjEBweKDUxfO6DXXetfKusHwUT370lqS4oxaqcThcLfTF4sHzy6qvJPtFkIwiD3NGmew0TqYPikrkOTVGCmv3y7QJuWSVvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=VJzVcXZjb8Wb-44bRzCIjkhQ0748qouYkN4XW1BfbgdnsFjUXfiX825uMSZUyAceqE6-cNj6jCCmpmAUqsp_IQUzQBV5Mq5iZ4tqq-T6bpvWZ3XkkoRVUAojy8GwGfXxNG9LMMViGEmAGk6VXkWga5DBXPFKUbGaTswZa_zhqd-bLOu8JA_a3kOgD8D2JMKUm_KQ50zU8DQoIbrg7pTlucBA_66TbUQZtebjH6MIwtN49m_j_EaPIy1hjEBweKDUxfO6DXXetfKusHwUT370lqS4oxaqcThcLfTF4sHzy6qvJPtFkIwiD3NGmew0TqYPikrkOTVGCmv3y7QJuWSVvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXVGVHdRby6mJR6TnRo4TK4fYN31zZmlahVlvPACh7MxKc_tHGiNLWvUahIuMQi3jQDf4Yc5akHsMwAuI8w5yPSdD9AUtiQCbpXNbJgKg6Gf61wz4I81RNYcJU9q3ktqGohSF6DJongT0OXp6XTR-zP70iRnhjaTo8H7IN0uMJlBgn8xMfT4pNpdI_q0n3JViqzRPrvPlFC0x-aX2r_A4ii4Lp8uMN_iAuZ4Y7LOz1FTG2NVXGmlVAn_xlE68AWaqavEj1AyLPKHvtMsLgxOobW8E99ormDJ8epF837jjfVwISTDtU6UjkSnKC7dy_Mgkgf5QnGdPE-l4Cl5uU-f_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPbh-1F3y_zBvY5f9KEUu3nSbsPRg_PNRZpywcOL_a8Ln4DHf-B_lhU8eInmH9u9g7aDzXam2nPe2VbOE1RDZe9nuADktO4C-Sn9wvLJEvhmZANuJi1y5JrnpKv170YwuZD_tn58jQaz5omg3y-eCaogmPtb6Abha4Tg8KpwGvGLq0J44DuhuEVRB30JzpUTXKmbJelmbzYgMtzd1nwv5g6Unbmawxccj_Q9xLQCG2GE0HFdSCu3rGFZIUxq_ADfYIIElcZUUBriI8hj_JR_Zf4W8hD5x8cKoRnPlZ_kHwW9abkJEtwThAORWoIi_UJOq4QCdOKebrRPK8CJi6ThIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sS5Abrr47o6AuzW9QVDJPJJuw2YJrsH76_xk_TgXsJbJ-cZfYN5qrIMY5iFayn5tUwL7u-uDiI6kp_PbEc1lEb_dxubL74UKjulCSEOJ5i5dLGuZOX1k5UatC1PeB7Tt5Nl3l4bCEEkv0OQx1K-A6NnyUddL1l58gUTZpk_PYdBZksQoXG_F97I1AYCd2fF2kDDEadsKCDGpuK4PCMuZjbM7wIrb1YxOGPCAEmbVKvmm3iSYw9RQsLtRkVIe_TEFFg-R7OkoWN3UjHnrYiflnGYtCRDWTi4DgL4jQlqt_l6OV0HEiSjGMbNLmGbDxCgxmBwVN-hfJoiypfX2yAAfQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTRd4lEFhpw8_suU95Eoq8fzZ_IWjN67VSr22UGs9rLfPxkRAYgEr8t8WTsMZvnf9n6fTpg-gnAtBTN0Pi8IdZMnMohGm-sh3Pv8dGdsN9ct2yfledwvpl1a5ixFtmIz-puuuHZlkQzaNBy9Bf1x6kthWgPLCQnNLMBc3kGhSdpUkmPOlBpOullmYAOiIcCLey9RJ0OOYmxWuBixrOXuzhJP_bCOgKWExl3SR_pNG4upwD_cW2qpQofy2Jv063FVJ-MuI8JJk7ANsyIb7ezC-pseVerlKoIYPTEgY3scl_4dERQ_mKH0QgFTOQHhmhAHiwaFbaD3dA83bNOyoh_DuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-YJ5gCaGHzll7d-gUAqEWn2T2QtnS2adbIcHLx6hPCw2-KkvKglFYDa1KXtzrJfokJjhFcf_mXDSp9XLeKdUxO2kQH8QGravRm6iLnw44PMe5x0mkqY5H6GXE4MK5RxVqGoLdUq_FLbgLVYuh9xbyMEgn0ebuPd52VAhlgbwbM_S9MLEKUuuCJ-62Kxolw68TWQdikjSSg2ny47aGRl5IRU8anHsXsspu8SDlD6utwqF_GvBwdUwX1VCjwffeOESw3sh4x4OQKFZEWfNaFzvTbWD5TpyjAfBfOhY4FmFWOWRCeo19kE4vZVdEc_MdPaOB2p4ZYOVgqckrp9jtp10w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjqizSMX7llc2y4qLCO2Q2K68WHa5AkLwkWPFlfTsKjOOlBQU15zb3hqIFlJysxlWYkKzWsCtU1ULC1dlovReCvNPfYMjEGU_WKI1t6sMItwqj_XbyHuIlS0d3RA-opAV2P5LHdvVTu2vwBWUM1iD7lS3CoJFJa3y74ALo2xV2TqevMHVrhZ7wi3OAWgJmlWHmxRBTJAwMj5fRbWDkx87l2yjM20c5Cd7yH2Wmg9iodZC62e5PJ5rMAoCdiEKtLqxzBktZ4m9vPIf3BBnWWAlFIZgHvjrUHts9K8dWoxrhFWhnOrRSKclAWgfSD_M-SHHXjItCe7v544pkKrcM7zrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vf3sAJ6xq_vfixCkCaHYEHoxzCW2A3oQ3SAnLFFfi82J364x7WcQYcAVNCqoPxaUAdUsbknyLkS2KIcI8pyeUQF8SHDrWBsXY78a18KcWVUWU_G5cuW9WjZTH4co_tdVAytx0v4UsstZnA254noZk6Tl8XecTJsYjHfVFlULTYTjSogxmKx4QXh9Ae1r_ptR4Fw0vsrem9rp3Zm7BZynrqOJX-YCztPR8yMN3XEixNfJMA4y2x8U3Xt4KUIY2IsG-aR35Lp4rqmFKHn_xIAMNez2Se7qCzPZjhIRHq-SVUICzYu0vB4GSh1G31CLo2BLR-PtjjoFKO2bP2OfrGW2WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=vb7Qst7bpIKAz7kiNgLaudmmXcaPmsTFVdSMLimimTMUM3dsaOHYkYfwdFM4SvtEzQ9xLdY7XSQGDanbmM5Urkfi4EcrpZv5CNOYG3ykv2VpYK8JXwaujBoJuN-15RoSt2qNDh-j4uIvxLc3g7UYklzkWDhNM1jLDY7PZFkgNmkBNhmXggyWzhtqfSJ1hFp_t0ffsCjX_m5SsT0y4uqdz_HmMk8ygsDPUIT0o53H20CDv4YF1flRwBQMAg2kvJS-YBflhdbqcnU0dFSYcTs0hhikZbP5mDDRp8KSlAu_fEbYmikxxPSxTnW1R06B4rRTiCpjsvufz8Q_KjrwOHCMqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=vb7Qst7bpIKAz7kiNgLaudmmXcaPmsTFVdSMLimimTMUM3dsaOHYkYfwdFM4SvtEzQ9xLdY7XSQGDanbmM5Urkfi4EcrpZv5CNOYG3ykv2VpYK8JXwaujBoJuN-15RoSt2qNDh-j4uIvxLc3g7UYklzkWDhNM1jLDY7PZFkgNmkBNhmXggyWzhtqfSJ1hFp_t0ffsCjX_m5SsT0y4uqdz_HmMk8ygsDPUIT0o53H20CDv4YF1flRwBQMAg2kvJS-YBflhdbqcnU0dFSYcTs0hhikZbP5mDDRp8KSlAu_fEbYmikxxPSxTnW1R06B4rRTiCpjsvufz8Q_KjrwOHCMqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bp6pqh91uwQZVlDhYrfLU04XIBXzoq2i84W6ojaOEL-k5mJfCVq8GDX0lwAHR5Y9tMGR1RZPYfUGu6JU1W8wr8fs3DcemZkT4iFvFJi9TLVgaA2uoU-4qPNj6X0dKODp7Xc-TxgRDZBG47Nq1IJZWtc5xmSWd_pZYyI3NVy9Hy987DuiO4iFo0Ze39obxsx6VJ0H-QteFyxNXAQAHzXOPab3Ffkl6SKarWe2O7RtsgLHeY_dwEofysWHnEttxppmiTg0dVlyakU0lGsVnejzxHAHqmzsRxTwex_zzP1zmdY0Rlvn2wpa8WsGSAY8FtklRzP8KZQljAzzyRkK8-53Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yh9srs23HjN7ZZmjucfdCsxbntngF0f6bqGfHHtOVSirzTqAHavEba9FZ9wGyouE4J3e3gf3ntfVAvxZcR_vzC5lXFCs-g68GrsD5AtkBizrQyrnYw7vklTQ0fkROFQ_-C_T30IeloGRhlNNPGIo_i8SNsApFluov7aqPNPcQYR8u2q1AsbR0C0vbrSDnfO_xc8QgYSffbjBU50yIElHFYiELCXxRWJsfn-AfLXBYNx2SzNXAwBQodtr2sApM__7xvoxlpVft_NEWtulkBQd8UzcKCdBW2bSgtHZ6fm19Lw4G6egfUc8fxxbtznvLzHceAAOzU-CNC08zbAuduf82w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qrx4s2xHCc3JTB6hYDIZZklFHfJ6YzcK6kDGu5JqeXgc9RSsHEI9MscqK2ONsfUVVhoCBIG627z710ljO8tHaSa7eTGDmtfMvMJgRow27PqKZdqFf4efRruCiW00gj8WzPIvoUke9wTOCJp1ZRUavQH7GGm_jTeil83ILO1_5iAJlT_27t76jOoiwY6Gw3eQVNDElg8ac5RUbz8Cz6KH2XjB8fuXYO0t93EH4Ey3JW2t_qssNWKA5gXuyHDynsnqOsZonIX-Ict7SZnn6DL0l8es-qrMJ0NPp9XoVo-NprWkOlPWX_DLVrGq8oQ0DHy_pdr1-GwnyrmG9d5Z83xeYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6Zu5M0aH2z05mHXp73RINWfnqBirK6PZZbPiLZN5odeUXk9eKeke5wrx1MZih0HibbeuojGDFQPG0oXoylx_8vBJPKksVD-jcE94jkfipoXOB3Wy1N_lK2WOnrO0-pFBRdaVXfWA1mEr4LpIM-ELtUCl8XkZnItNDR59bnZSbDfcs6882pn9cbbuuYQB-DdSPU2blJYyRoLkenPxH6KPgDSBHdqPuhGdOv_Pg-hbtfBYGXl_8r25d5qOBudxJwXBQWYJK4XFz7TJatCRztivmmkqXPUbVENaTFa45qQNJ8ru6cvCNDXn0DnO7hch1Ss0fvNXEe0WLNoDfxgxkaz9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UbTiFdHOURcCdn_FoHACqnQSCb66wsNT4Ss2-X5xj79K3Fw0YN0nEwJlMBXQD3A2E1eJHrif5yg7LPihyjzs3VFRfyMytTMZOaRFcZpQRbzFr2E_9Alv7L0NyZsMPlvntnbPv6U5CGgZlnjngaYDCXra3t8YzR6-TEsnY6UHE29JMrADNUBhrd3IY7mGYeWyqEP9XfD8Iwe3wCEF1HfozkedzBFjWcAEmsPgX8_38MQqMoQ6xNbD1JYcMoDNro7lot-b8-jj-ifftvFcIB6Xp3642qrGfpp_OqDXyz7ckzNDJl8c7BkjjbTSG49496-c0-GCANLIff8Ac0pQiOyJ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f58B1o7FLg7bZxYeV8ayUKGoNWoVnBShTyIYF-EF5F7bUWhjN-Nd3uuXRzcYsxFaPBKbrTwCnuKNd84OT1lEiS2LU-5ceju_ZaAVF993IbdeX8or9CH7j96aaCWEWJGsHMhgqotuyXoiawMed3-CKwEUJaDJrRv3aZ-lJ-_ShZEca-grjSYWyz9F3bBw9icl0dsVGuse9iVF6QZlTVvuOCLIyRTBwGKAgeOE82pS3vkRY9K9dCVVb0epLe6fv_Q5QTGT5Z_FkGyKQFfYiSzIH8vIcvj3HeNacNVqLLsWpUt_FIQmLGs9_CeO3BG6i-T9koM8dF63A0uZGfCoWMw6lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MacqZl-XcvnenmJiIt8kQVJSuTmaF4Y3tbi9vFYExO8KLfW6HKwrcrT9hzI7EfaDb4wMuE5f_eXJzu-pZ204qLYKeImFks8rI8xX9MXPwz9KGMZzOgFVGTbBFptH3yYi9S9g06MoYWVZ6mxOgA5Lew0Pt-FBzRKpof2qDRsVeLMMNFHJtfeBUSXhwEDZVIwl1gLhnNRkwhpnFVCXNF4rJ9Bv-PejwpcUhGG9KTnKBg0qiZhpHDHU0rsyf88InpcS3HFL0TfwjsR0vA1qVio9zImH-H1-KG4h0DnYWbVVeIm9PySs8HNF8iqDB6FUZilmk91sGg-745P0qLFQCpNiVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b_0pOfarZmtSYLdaLI8onUZltc_eCDmhGKID6OZIA-Y7JfmqQk4PjH4ECIVAuD6Gi4wPLQ5qCHZHXtndivdl5JAnto-NMQvLYJh2CbM1tYW47PPwkV4qH9U45Hb1Z_2G5Se1yWUZBwcVDRVtDddqGOMm5NYkavyLPum3IFZha-qZ6Tg7z1gf7cP0awBwMqGFWTXQI413gHY2-9U2oTF42mqL2X_6k83mMecXSiEGimJuhElA526mgRoCJRuCCJI8yHu3DvrDUJYpFKPIlXThd7FuX0aa4Kg_k4lGC8uojCCVWx7Zu4SH0Ij4EP2hlTRYi7sqEuB6SyQkPXifhTv-Ag.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=QgGDvdlC6UdPGV7UGlnebbN3g8EI0f0Dq-t8TXCWiHOGH30uLbQwL_dWWVFndx4ZwBJr9oLr0wvF2YzsMp_H9IyIrXeIMXGQ27OXNCUVs8pyIhwSX-dsQxsYOJOYLd0rDT96fFWNi1zGXtysCs2C6RkB92ld-gnSzU8ohp8AogE-mjnZiuvhRTxA6Kl5hSwanIG7n2TM9avEuflz0YQYMrPAk3EO_3_q-ZgNBgMoena7iiddxyR5I-8y_eYcLDMQS3l-9lUGFLgs1EDUJ0YKGXqwplcxMchJeJITtcUkjVn8fP61PEc8ij8g-xgSx1ICxHzbPl88oLZNfG_cyC8cSgHVbzzMiVxhD-19NFWcGSlAJWFwuIVrwydsA3cnbnpKgy3uYggXoItKgKjoB1TSvX9jugPzqSwBRE6t3Zj2i6J8AEspLW3KZ29WPjgDt5GoXzU_0WkVdoO9H3Tn6o9Zq1-pHWCAvdi3PwKcVSzNuxoFqx_5xVxfm_ODGLs-Qon8InYSRa253Qu8Q3-zgtSLGELvQCgVtTqbfpGOca1nLO-N395DlaoOpCdj1vZeX1RhrVmG24kpvbld1oX6X7AmdRl1m-5IhPBMo9-Bu41odelj7zBlr1pt7fCk6aL7Z6BGtoix9V_YLUceK8lB27onLaOgDhvmiZVdDdIlzboMjAs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=QgGDvdlC6UdPGV7UGlnebbN3g8EI0f0Dq-t8TXCWiHOGH30uLbQwL_dWWVFndx4ZwBJr9oLr0wvF2YzsMp_H9IyIrXeIMXGQ27OXNCUVs8pyIhwSX-dsQxsYOJOYLd0rDT96fFWNi1zGXtysCs2C6RkB92ld-gnSzU8ohp8AogE-mjnZiuvhRTxA6Kl5hSwanIG7n2TM9avEuflz0YQYMrPAk3EO_3_q-ZgNBgMoena7iiddxyR5I-8y_eYcLDMQS3l-9lUGFLgs1EDUJ0YKGXqwplcxMchJeJITtcUkjVn8fP61PEc8ij8g-xgSx1ICxHzbPl88oLZNfG_cyC8cSgHVbzzMiVxhD-19NFWcGSlAJWFwuIVrwydsA3cnbnpKgy3uYggXoItKgKjoB1TSvX9jugPzqSwBRE6t3Zj2i6J8AEspLW3KZ29WPjgDt5GoXzU_0WkVdoO9H3Tn6o9Zq1-pHWCAvdi3PwKcVSzNuxoFqx_5xVxfm_ODGLs-Qon8InYSRa253Qu8Q3-zgtSLGELvQCgVtTqbfpGOca1nLO-N395DlaoOpCdj1vZeX1RhrVmG24kpvbld1oX6X7AmdRl1m-5IhPBMo9-Bu41odelj7zBlr1pt7fCk6aL7Z6BGtoix9V_YLUceK8lB27onLaOgDhvmiZVdDdIlzboMjAs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=DLrRc__ETMZrlLXyVzB3O4HmlP9SI6AN26KtNnfxVKRkpKh8jk7k2un7u6y-Co0OnuyOvoaCQnFfTf7H2e8p6dMbkfqY99vXQer5WQlKFbqNTm-wndd2s1eTTpBJz-DN_oRUFcZlBMCJn-NFUNJqd-j3VoytALFEFwA_yRt5bcyzFbdMgjVgLU5gUAGlyY-jCT0wLZK_KhOxcrSUOGN7qpnf0pYB02CQ6e7WVBfZWOkjsZtshfD6ApeA1dc7TdLxgIM_uPVEQf9qLRRPUUC79H5pic5Ba1KeHT4yQScT15ZDAfk-AV7OipQu2OUAIKnuBPHSr8EYm_a12JgNQa4KEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=DLrRc__ETMZrlLXyVzB3O4HmlP9SI6AN26KtNnfxVKRkpKh8jk7k2un7u6y-Co0OnuyOvoaCQnFfTf7H2e8p6dMbkfqY99vXQer5WQlKFbqNTm-wndd2s1eTTpBJz-DN_oRUFcZlBMCJn-NFUNJqd-j3VoytALFEFwA_yRt5bcyzFbdMgjVgLU5gUAGlyY-jCT0wLZK_KhOxcrSUOGN7qpnf0pYB02CQ6e7WVBfZWOkjsZtshfD6ApeA1dc7TdLxgIM_uPVEQf9qLRRPUUC79H5pic5Ba1KeHT4yQScT15ZDAfk-AV7OipQu2OUAIKnuBPHSr8EYm_a12JgNQa4KEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی
از فعل گذشته برای مجتبی خامنه‌ای
استفاده میکنه.
مجری : رهبر جدیدمون آیت الله آقا سید فلان!
حداد عادل :
ایشون از آقا سختگیرتر «
بود
» !</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5250" target="_blank">📅 12:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElBeCIAAUyrcbpGimQYjoCqobORldiTU6aXT3Y-NFBtlczdYNWfHIRCdy4AQXROiV5wbXJ5i5wJzEeGc-pDOOdKrpFLtIMA0vXXGbW8vhzkFRADOCQRc4moygcZa_9mdpqHcslQmcLZJZZvZMLUbfoCFAFZsnzZ8oB9HELJzUwRMM_pHGBkGcCg0h5MIpGoX-jHvKiUQrN3ilCEWZv6ZXS73t5PghGjxtYna51Z2egzXXFs5IFkdJiv_j5TAUY-DdeA_1QAF_ce7nFCaaByptECgyR_bLjGvFT2i59AY-yCjXrgmKGnANY3rUKTuEnRvzMYn230qjfUXWTzmQ23pZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5249" target="_blank">📅 01:46 · 12 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5245" target="_blank">📅 21:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nquS66pQJpQ8GLGrZghNQxeyFinTOlq6WZdiI75StOcZ9J76p4yuHwjJIeDFXhCrIVy7d3xmJzidP3BiqJrndSJg2XrilkeLhubDtheqS5Zq2Iq24_pLbRSvQPgTp24K4lXzNTg8_iU3pgQsQV3NgQYfi2qOIzoCg2TNKFzAUZkNzkgCFm6lDxshzHi33j55jmiYaA35Py01Uyg5SVc3p9tZDBgU0EQGnNi9-jlJhsYTAeMJ2MiVOxrncHOIe0hWc1LboWDhTgaZC1hOjrXNwMPjCbMRB3iyQiHlDzj_EJ-V43ldIM1ygKVDTK8Z50ggE9UHmjn7beCGl928-bqvGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXvjNxd6EO6IaO3N7cxWZOBnAW5DLu6EswrFFQsUWp1NSIfbcJ1eT26Vp_7HTp9TRtcvSejz_YXazyRbi4NqqfQw7FWC7ab9KGPeRkOt4aE9BkftVA59QCH4_lbEZOZFu6rmyrUasl3eFD0B9DGuK0ZjNErqqeyerqbmGSOUBZq6WORBzh5-CdGKOfe33_GBHodiYn2nyoUdGyax7OYdlJwnqKzRVEmK1_A-ANqMIq7Bkgsi4gT8djkOq30Q69SrSQeqvmSWVxAYLown3SdpMwk3P7heQ3YVYgtn6qshC4eoRw8FaRGRR73tdCGJeCfm4UP9xozF_lKTUVNrRzWKLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dC95y-dVnNQCE9ATPXp5k3HVsD_Y--QPS_cC6z6IVMRKKkb_qC2Gm_OaTI93I1N2O4rzG8HyKVT6KmIugj9zdWYWVGUidqn2PWqvzG0L4ryvQj0lVfbsYheB-nwVUphaLw7EyBTdQGtVafYG0jKu0Y02KY49uOD81zSOr5Vt-5S25w42Eeut4oZGHP2EjwHWWa8VODNNhYZ2Te7SwEtdSFHDkxRAT_5nHXcjmoW8emn6J6lZSW09XoPRSbIXc29LjnbM73Ocv5XGgGzuiVtT3jP4oQkD-BaU0eoFd3MB3Wad8FGGoeGc9xA2rweEfsFA5M29TMEi3FXZi10josHOtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wjzd4_fLoy_y5U10YplgaxhFH-iU72HcayKyPcQhRttU6Za1Hrz7NI9Z9xYXjnS7_UHwt36UqzAL1eg90mz_y4H3PJFmwqrsqbhz3Kv9rZi_aueFgXUV5ae35iaBdlFD8agmGJ2YGEjKI3o-kMbiIOZQPwiYq7WcFEEc-_Lj7WpGaku1aUzXpcDscrVt98H4ngPf6mFHzeD41Y1Dlj_llx7bpZg9z8PbPI5IWKSVTyAFNbaH0_IA7FUubr1a6kW28tOIy8CJAF8oSq5_dtXITGAkj8iK_nhbokp4eY0Ra2Pg8Kd9UbYYSPpO34iJ2m2kmgv5zRFVfkmC6GY100ispw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sg-3T_gztCO5MiFHoAfYnlBPwDKI5FP3eFwFViLYBjarxJSYhRFq1xgmbcGv8GGYqDssZU87gaz1dKEKtyGK_PKwfIPrU-YE6gzpx7-vmNIJxhYdAepWeF2GR2KEbx6lAkGAGNvyDtac8_ULMNIu21U7g7qRz9Xp-mF5CGC8NGMBr5aKi593Vem0srIt1I3dTjfGeG1IeXGaHC07LO3lOqWSzpDTpzxRZ-vg0esF4DX-_5VAJVbiG6WybrxlMa0jmM31hjFHz3hc3SNR3m2Hrp2F5GgQsdelZjCNtl0bIGb_GrpcTRuA0YyVXgN0TlKszjbwhNQmaFgHmScohtd6Uw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBg7W-ucHrQI9uVNNowEAq7MXIUk9GlIf6FvpcGS7y57S8HmnedNKljdHyu_e-sarPu038VtrXwxksFaOtdYIbB3KdK8oPh4e_bqD85NfwSfkIzFJOiq8N0CxQRx62tuetXnLekNT7GAmOBBBj3B_BfwUHIRVY9caMQA2KP7VY4PijuYu-06Cvgc0Mrxt-O_B25Qv9y6hz6aROfWMcLOAd6fd0v4i0nckiI5aoNWTUMAfXp7q1z0D6XSqyysftvkLxZNDek0PcisSaeT5WCqYS_3XE6acd-MYDm5B2DSQYjknP9TpFQrHjEEfZYCj-tBy2ENpRD6th2YpwWqIYw_TA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QxsGaThi_qtNSYuE-PP2EPjU68sbxuc_cSGeyrYhCNpP7dqbZO44R8GjbMfw6lHKC9aqJXNar2YDKDICHaAJDLix0EroZeYVUGi6Qr9Lk7Z0RKSvahxvz3TWW_N7P6RR-dZH-8lQAC4ZV2dIbtGCTXa0zKOdxs3CrLl77uSmzxLQ5ebEkfqy9bFny3WDHgz4y5Ex7NFaPtwgPtgcKoD-HE8JlkphokBlGprc9MLCBzd4DxUWP3OoGUbfYBo9XuD_0irjWcZ8HI8BMZhtQ8hHRbBVyr_d61wNviokAEaAnSqjxLIQk6rzMcI8LMEzuNtCBZnwHjjxz4xT7RQ7DAVCpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/krEIjgEStD4doPalkvIUXLKSyj8NX_anXcuF6-unNrqWiYmHw4wgvDSfquVUt7dxUD39vItBHadokllbDvXxaT1jyJvdlmVHCUV2X9dI9nBKp2cc9gJY0NqyQ9g7FOigAIKQiB-yIP5TWo0lZ5dXOFzqHiTG3OG3f_6HGYVJq4cvAhIb4MO8ajvt2PFlBYxLMVMUV-TRPGmLnE9A9IJkqsYv8bzjbqRWGeHEYm-Edb58LHu-QX7zwAMzPumWegI7AymmjqL5kfbHyc85FbBbo8dSs-CY_MoBCR5rYdRNFdy8axYA4pCkfYnGtX_r81wxaNmGk2HtSJP7gwbpg8DM4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=UAWGYhDWS1bw-5Sf_udz4NMcWguIxcW5KJ1XqpPwPDJA7v36GZNfMqggXNlL4q53Rf--tZiikgNx1KU1N6jmODt_FVb_hPIUq4Rkq5clq8VS5ryCErH9AdfDpyUKc5KVCq0ZxVI6uwlKWXLnRFNQMmkpgnxDAHpA9ImO1KdurBe2oARJTASYBbW7bR8uTavrGoi_kHVr4AuDZOA6Bq1elbN9-CCmTUtZZG6iA-x6NK_WweE1BuGPWtrHtazRpm4MP-vPkfEzvzFhUN5szXXSMqbaRi_8VGkVxtWhzU-Aj4lEL_nA5NaURUxsaL8QY243Y8op4A82aRAWoaW49l7Abw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=UAWGYhDWS1bw-5Sf_udz4NMcWguIxcW5KJ1XqpPwPDJA7v36GZNfMqggXNlL4q53Rf--tZiikgNx1KU1N6jmODt_FVb_hPIUq4Rkq5clq8VS5ryCErH9AdfDpyUKc5KVCq0ZxVI6uwlKWXLnRFNQMmkpgnxDAHpA9ImO1KdurBe2oARJTASYBbW7bR8uTavrGoi_kHVr4AuDZOA6Bq1elbN9-CCmTUtZZG6iA-x6NK_WweE1BuGPWtrHtazRpm4MP-vPkfEzvzFhUN5szXXSMqbaRi_8VGkVxtWhzU-Aj4lEL_nA5NaURUxsaL8QY243Y8op4A82aRAWoaW49l7Abw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال «پاریسن ژرمن» قهرمان شد و پاریس و فرانسه رو به آتش کشیدن
قیافه‌هاشون که تابلوئه!
توی یکی از ویدئوها شعار الله اکبر هم‌ میدن!!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5232" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.
پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5231" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPxzJkvpE8BE9-2U8r9_GApnury-HdFdC6xS0SIf4ylpmDdhyyb8NHUQpxZVzmRQqrl74wCrcEeXSq7s9YvY73eesMJ2AlVx3o5ovxXLQe4raylbbFUMCbL5sRFGPkE2D9NgskGYVQagG6JuO_Pb8yThbFBEm_pQCeoiNeW75CL2zJFCZrIBPzXbgMQ711ob82xOsTLxLMWQi_awocOso7ff8fFbvyNAkagcjpBfeBUuvboDENAY3mS2AyFCPMhfZGHd6uMdVWpqaN5zEasMFOmsUtCl7cFiQ3-3Ti1B91jXMQcyS3Ljb1gy2PUYDeQUtylkDsPCN7OtZ6evrNt_rw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=Ij7g_WiU3HURh7-NQ8QYCyy1faN6wqE8CV-Obr8ikF6JH3g8W2SC4BmkdA8y5LRM9_jMaDx3I6bRkgcmB_WO9UFV00APfJqA5NguPc9EXScuD_k5_ZKWoYXxaNR5WNlkoYGHti9VhlC0nA9VqrpdMUMr_boFeJavR5LuF9Z2RbyX8L0q2xJtslb7GFKUgBF-Rf7OZFQZxR_16zK62EOPFSkH-UlBpmfl9Wz617SOoJXe4JcplrY7eu0Ez6xmiHoZQIN5TJI5vhAlE0fr5gGfM98zI4_rF4hB5UdZo8hkMSIi7qOpG1j3k4kw6xI2knMVoYP2Tfg8c44cwaugOqYhZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=Ij7g_WiU3HURh7-NQ8QYCyy1faN6wqE8CV-Obr8ikF6JH3g8W2SC4BmkdA8y5LRM9_jMaDx3I6bRkgcmB_WO9UFV00APfJqA5NguPc9EXScuD_k5_ZKWoYXxaNR5WNlkoYGHti9VhlC0nA9VqrpdMUMr_boFeJavR5LuF9Z2RbyX8L0q2xJtslb7GFKUgBF-Rf7OZFQZxR_16zK62EOPFSkH-UlBpmfl9Wz617SOoJXe4JcplrY7eu0Ez6xmiHoZQIN5TJI5vhAlE0fr5gGfM98zI4_rF4hB5UdZo8hkMSIi7qOpG1j3k4kw6xI2knMVoYP2Tfg8c44cwaugOqYhZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=vAYWcv-fRbqFsAKHfiRu8maaOohxDkBGDZv9rdPd1jRW4GdBQ-0pTBzveGd30kb_BL7X1aKa_F7nwOMoJGb5BRWIprgeEREUr3_zf1nQonCsJNuK3ID0dnTZeAxqqb9gac5x5yTDukvcpHWi_xg0K_fLi6Et7G4JRzCQ-sE7EbJsEzKKKBoz2x-abEfkkeX8u4vvjU1ga7d_b_ujDbND8XzJRJTNqLoN5AX_vbHCfavpO9u2JaXwoHF8OcHRr4ZLAjrP8MGRLW4yzckHHhGDsa5nqDXb1jGWQ013TMSUEFkGaubRM2bx98yBcw_iQm5sN6LfeCEjZnUucM9wkcBMjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=vAYWcv-fRbqFsAKHfiRu8maaOohxDkBGDZv9rdPd1jRW4GdBQ-0pTBzveGd30kb_BL7X1aKa_F7nwOMoJGb5BRWIprgeEREUr3_zf1nQonCsJNuK3ID0dnTZeAxqqb9gac5x5yTDukvcpHWi_xg0K_fLi6Et7G4JRzCQ-sE7EbJsEzKKKBoz2x-abEfkkeX8u4vvjU1ga7d_b_ujDbND8XzJRJTNqLoN5AX_vbHCfavpO9u2JaXwoHF8OcHRr4ZLAjrP8MGRLW4yzckHHhGDsa5nqDXb1jGWQ013TMSUEFkGaubRM2bx98yBcw_iQm5sN6LfeCEjZnUucM9wkcBMjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما  از دولت لبنان خواسته بودن  که برای آتش‌بس، مذاکره نکنه و…..! به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره (که بعد بگن دیدید،…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5228" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrkaUqB63jt91Xkcr_FuiTFqnHaJ03iiA9hZduNyntYt0Xvg-X-yX6oPW0v9RDyrxHLgw_Pj48Gq5zG46e1b-iZEUOM376ZZA3kGi93JlHXTIC9mYNm8Qyl-jiUpt5Ypaqrur_bS4qV7RCmYOeB2rk_5rwlA-sGIMl6COlG7BtxASG63qxF2KlGdxl4rZ-Say5devs2IAhJTMdNgxyVOYWGeuXIE1DT-vSYYbTaPDyhA3FJw957v_OJLKK5QpSivaWncSYoeTSETTjGxnOe2A1azkktF6GKwEoBTTfFLIGkP3Ftevp6-MrQCfYvm1Jq11HzOj9js7YSRPJQ45u5idw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=Jjm7hTkfV1nw-fx_pIR9lGQQJhYLGnlaEH1grRODGUCH12psNDkL8gF83qKgiBYIGJQ2VSvTMsEt-knm9V4871WC86WINsB1eIjOtwrWgYQnfZ4jQ82y3HAiukdXsfSzCGGxNWi9dZUryidF4SuXWjUZOzkQwhDLwX00KmOXN-aEpLUWijn4YdFkmdfHr8EoqOCp2Wj1OYPtEp9h-DUl2tyrM1SIAzwnyjjhZl84WGrpw7-42_AQjJARo9oAvmUM8_8XMHqSgRK5YQlg36nOFBEeFiTnj6N4lC9WFdwQcSzB1Sk20itGjugVGAlSxu3GE-NMpKjNqIxpEdv7-MyDPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=Jjm7hTkfV1nw-fx_pIR9lGQQJhYLGnlaEH1grRODGUCH12psNDkL8gF83qKgiBYIGJQ2VSvTMsEt-knm9V4871WC86WINsB1eIjOtwrWgYQnfZ4jQ82y3HAiukdXsfSzCGGxNWi9dZUryidF4SuXWjUZOzkQwhDLwX00KmOXN-aEpLUWijn4YdFkmdfHr8EoqOCp2Wj1OYPtEp9h-DUl2tyrM1SIAzwnyjjhZl84WGrpw7-42_AQjJARo9oAvmUM8_8XMHqSgRK5YQlg36nOFBEeFiTnj6N4lC9WFdwQcSzB1Sk20itGjugVGAlSxu3GE-NMpKjNqIxpEdv7-MyDPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iiKg5Rw1iygFszNJXlmAkIJVnUk6fbaDvP5bpP2HNrrE7BP-7o8E_iKDzoucfajZ7FiWdGsRIDDVxOFM8OXNvqDUgdgVAFJo3B5zEAfy3hmUp2K0PBqRmjUE9C2qDH7p-OZn0s24Nouddn-r695B7yjsW4TqdVnYrkpDGnN8Lzl-0LeX5wt-Xfxvo-aQW3SCyc9keqAeiRlu8IyxqyCGHb9BfDPAwv8YM6vWfoIv5SgRvYIkB_3fGtwsiHSWIzkBVerGsY5gS0k2JAG5cltEcf72ULHkUSXh51_3OAvbsygjr6Ieam94AgUwECyspQ-1iwK4H-nR1BcKr8Fbcc3shg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSy0FQJcAmBAR1RYRWvM11cdVhjZcBezMPFK6a1yS-BfiqKuaZrB5FVpH2ul1TWQMXuFcMEaYp_to5gBI9hsDGg60qJmSKGeLhEgAWyt6y0fUOfPBt0WRNgNKOGP2pagJq_TTjc-d342u1t1tsAVv6N1liI5bx2_DAmz1MPJtt46TwP98U8oUl6HbgymjrCSMKu3A4YHYHAkJGj3hzY-9tLQhNWA4c98cSLkaCZyeACt45fjPXcxV8MEfX_BII-q2up4DOj86x2JtXxYRNQ56vdf9qRZh6Xp8hL1AIEB_ocj4_kpbDyAa8EMZ5NyjrSx6IXrPuqN-9zUz0m0YFFPkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌های ضد و‌ نقیض از استعفای پزشکیان از ریاست جمهوری</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5222" target="_blank">📅 00:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FxoJNlCaa2cNsnSzoA8-_vOwPUDcXbnoWMXuC7Me-xb9M7aA0Nt-_HgD3CYpHMI6jIJtemWlB_mtUqcU_FSILVZJVcGg3pRVYXDJ2tqW3fXGHmdUOQycfQnJqVPz2gOHOI7HKthcyaZHtTlN01fuy9ThZMgeSGPov94q2WpKlDWBGZ80xgPmGez02393W2FWbkoi6OK1KlbhGej4zOLSn26cZLsTxtKvCUeaXNLMwdFhjcdEo5pxlSA6TK84gkViCEUZ_zuXK34KqZxQhnaKjSNW2s_0h2LUMQrAS2-9vNtGnoLaUvzgCsb6lClOnGjfPCn6TVeKml0JQZFuV8DglQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bD723dwAUBcMc4py0Tir-0jz-cu-FrM7k9CUyGeNnqrofGRjN7LVK-JTbFnSMrOPwJao66v4JIa-6l2ddkyODENFPG6E7nvUQbLs4e4slfhv1uzq90S5GqEVn_1EjvFaFdRY-hWkqj991M70yJsYjmeLPGGGFSuBrFPMFnzNGCDIZvq7DnVC0GeOV34UX6zE7mqjRmfedqOwYwmq436oi_LZteoEswE9TZF2SYJ-w-Oxx1y80PSNfvEXQoZG6LZXdz0v7HDnnGdjt_pmbVbHEHNTqS7-GasElCtzgxQjB2Lg0WXLTnpxRJZlpCs_q-3Jj6CrHGLbyd0dcLQ5sZTBZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qI-HBC8q8MtC66u5qpsmfyoo2mSx0hVtzQojXBsIP0doRYPUHJ89Z_z1jqV55MCvFrlXyh4zJodDH0YELKxvfGBrUY-Q7Lu3JfselYeaAAQIQSzh9hMwQ5chPxoFdNiuX05R-z2NDgoWdEN7ibLwSce5VZGc3ARo-U37fLe9K1PINq_pDB9htwiaMOh88y8_oSNIg1nVr9BevsX3-3vtDAUxr_A7XVkfCRjyIuq6LE3WGlD2wFBe_v-_0CmyxiCLijrwlfIsl8XoPn5Sk5_EVCG6wQahgZWrCgmF-XeTfqasKqRsEjPkTtb3nn_wKng5t-E7JuSbLc7N-D16pF7ojw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eGiwKqQraQjzL1QKL6rTwEL289Z4RSYjTPOSyVAW08OcPgX8t6L4H-i0AQBFUq21fje804YUB9DVSHOuy6R1527tVLlE5VKMlVvuTIp_gPioIlfNXgheB71TVy1xhLXcCzVqsh3FKt_9Liar4nVbjjjGgGB6mE_B_V4-aQ_vrB47q9LEkDJR6vKDZUkjhNCmHi3cpEUAWIumj0RZq91-Ce4opjepl1pT7QigR3KMcU1NDkCvc-CyzqeyTKkCVcr-rXXnpk1G1Qbs9JestuxQoUvAAHxjRLAompncAzAMJFQapGU-cqwibLdlv-UQDcSiZBv_l-FJVhIMaCCheReU6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s3uIefKVYX_Y859rug3Kxt5sm8U6k28OyWdywYc2P5DnhcEXXtAtke6OWHeA7qxMtgkrrJFNBpP616OUjeNgr1lpIuGV50hM3tS5cpwt_5eOtD_ZmHDS_LTzoQfbKQM4V7UhMAieeub-ApUI4dcZgRKImw5g5Y2sT1eeT35dj9AVNx2aFaAjLeB6DinWHtFdCH-d2mNyfgDSFniUhJgl_mR1cjuTu9xQ7VROFfoEG18oRsP7EE6ub6WaXFKZtV15_fTJR59oJVnGJBmVSQDJmQbjP3oEtN-vcVsOfDA-XlYUisp3RP32laDPaJwXWmkPlC0484ObClLFejlsoKX8mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eSkZqqKmGdxGGsDoqq09inoD4EtdgcKtOKCELpXUYVpdXP03yy1VSfQBQ_7eZSF9QhRhcFcVE60o51ohvsfjvzIhBw8kceXTdOYI9P8yFlSb_e_F4wg6UuXe5gHCGezR5dgGse2od6h2A1u3XcQs4f82ktcM4yTzE05oTgKK89hI2Q8P2o8pIww1IpcI9BAK7olCWT4XswIN7h7eOiR24t7dSzNHQpJ1xll2O4QMSJ3FLZmbdyD4gaYrDWGvIb2H4n8F7rYlnXI27DSXUwdy6t86t00yZzV3_TzCtqwEbhQjnDdtJCI5aznfZ9M63uiYBLUGmLDXEWzHAIHEpzNuxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفسنجانی سالها پیش گفت من به خامنه‌ای گفتم پاسخ این همه ضررها در دشمنی با آمریکا رو شما به عهده میگیرید ؟؟ خامنه‌ای گفت بله! جواب خدا با من!!!  و خب این جنگ‌ها و تحریم‌ها و آسیب‌ها و کودکان میناب و... همه همون مسائلی است که خامنه‌ای گفته جواب خدا با من! یعنی…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5216" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db68225cef.mp4?token=lagCy3egcfjXXPUvDGcH_N2Dz0sbbWwN8W8XzbXGB28w-aF9LNmFhzQg2qDBtJihBP3N0BgH5EyW4Td_fRKlwAui8X1HC6VlsItz9thAWqKTOF-IVn9_xwOLW1CVI0yUff-qOKPcM-L_I2g242AQ_LmuPqmtVOxHHPo-eAZi_4QtogyxQ9h3P6-rBEO83wY42eRhTYEng8tJ--22lxzLr4p-PW69SZjtWzOl2pTSOyYxewTjhTNeHSP9aW7BJ12QcToggKd7mynQEebePCP6hpeb-d8wCLgIfShxAJvTKosr1YCaRORgsspXlhoIV8WCrpVCoudsfqyU4DfqRIg5fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db68225cef.mp4?token=lagCy3egcfjXXPUvDGcH_N2Dz0sbbWwN8W8XzbXGB28w-aF9LNmFhzQg2qDBtJihBP3N0BgH5EyW4Td_fRKlwAui8X1HC6VlsItz9thAWqKTOF-IVn9_xwOLW1CVI0yUff-qOKPcM-L_I2g242AQ_LmuPqmtVOxHHPo-eAZi_4QtogyxQ9h3P6-rBEO83wY42eRhTYEng8tJ--22lxzLr4p-PW69SZjtWzOl2pTSOyYxewTjhTNeHSP9aW7BJ12QcToggKd7mynQEebePCP6hpeb-d8wCLgIfShxAJvTKosr1YCaRORgsspXlhoIV8WCrpVCoudsfqyU4DfqRIg5fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴ در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته «دو گزینه بیشتر نیست» یا جنگ و خونریزی یا مذاکره مستقیم «برای از بین بردن غنی‌سازی و موشکی»  این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5215" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=pwp3uwhe30VmMBz6mMVBgFfWZ_84M1N73FiVALNa6eGRXdN-_yoQ6BdAa7WW4BoOR9WKD2s6vfQnPQAyXaOoGNv8bQdVBvbMOwkKlIBCX6xOHR0ZM03VUcUOdWHv67nVIwNTATAnktVmVIiKZBGxp2KjocZVshERavOax-qDrdHIF1yWQwNRT5nfXgXAlcnFwgOSKkKRRXjp0KlLwlkoe58HWnLYdlhjM_fWU8vGBwXEnioX0uUpaZgvLgKL3qvHBVq-H3Nu3DkHIQuaf8OzTKCUP2MTwHOBuIDWNMVbKccDBFNjm9hqD5vWVyq5iSuczCFDMMTFAGnA6FrqAfPBhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=pwp3uwhe30VmMBz6mMVBgFfWZ_84M1N73FiVALNa6eGRXdN-_yoQ6BdAa7WW4BoOR9WKD2s6vfQnPQAyXaOoGNv8bQdVBvbMOwkKlIBCX6xOHR0ZM03VUcUOdWHv67nVIwNTATAnktVmVIiKZBGxp2KjocZVshERavOax-qDrdHIF1yWQwNRT5nfXgXAlcnFwgOSKkKRRXjp0KlLwlkoe58HWnLYdlhjM_fWU8vGBwXEnioX0uUpaZgvLgKL3qvHBVq-H3Nu3DkHIQuaf8OzTKCUP2MTwHOBuIDWNMVbKccDBFNjm9hqD5vWVyq5iSuczCFDMMTFAGnA6FrqAfPBhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌نشستن و  با نخوت وعده «دردسرها»  میدادن برای آمریکا و دنیا!  «حالا حالا دردسرها» خواهیم داشت!  بعد که جنگ شد تقصیر مردم ایرانه که تاریخ نخوندن!!!  تقصیر تلویزیون اینترنشناله!</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/farahmand_alipour/5214" target="_blank">📅 17:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=TNruJWVQnnG38LYGvTx11E4Q7afSzYUFxPFmS3SOKkpFYiLoNxKeni41bx6dSsX67yAHtt45S_ABUcNUv-NEBNWtKpNeCHL3-T8fLqHckUz17Hg0Urp0E1mErxjVJeT1hrGnaM6ch2gtd-d2ysewEl98Cx3jh9Hj74BPQupFRCffl9Ths9uOXOeM0q14cVFBiWG3OVUh-eRA_0KeUy3x8l9n1T4FTb7ay8oxaMZwIe1tZbLRru8WzzJnNpNDp4HPJQX_9-hGK7A-4d9DQawyYDfBxt3kDLmGTp-MyeVplfu1d_mQiPOb0QY6ZSLWJVzbgc6curqtW_GQPDKLwFch-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=TNruJWVQnnG38LYGvTx11E4Q7afSzYUFxPFmS3SOKkpFYiLoNxKeni41bx6dSsX67yAHtt45S_ABUcNUv-NEBNWtKpNeCHL3-T8fLqHckUz17Hg0Urp0E1mErxjVJeT1hrGnaM6ch2gtd-d2ysewEl98Cx3jh9Hj74BPQupFRCffl9Ths9uOXOeM0q14cVFBiWG3OVUh-eRA_0KeUy3x8l9n1T4FTb7ay8oxaMZwIe1tZbLRru8WzzJnNpNDp4HPJQX_9-hGK7A-4d9DQawyYDfBxt3kDLmGTp-MyeVplfu1d_mQiPOb0QY6ZSLWJVzbgc6curqtW_GQPDKLwFch-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی! جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!  فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ، بی ایراد هستن…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5213" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mw-EdHGwy7M-O7lzLfpFQPu8Ta7XNKm9uTsyvMCnXz68ujzYZrWnsAF-W7Bp2BHM6jTlRmpPZJzno8FiVy5paHe1SK6GqWHTxmmn2HRZ8kYSW2Vg_CtW2OEDMq81W6ZMG0KETdFOQBblw_-myeBO4V1pUjxmW08Kij8vwnioUL9Vr-38BgBuE1OkCHbGXEva8GhpSRhqnYnqTL1lrTcLs6e1z-w5_y0HDeda6aIUQAf5RM79Q8kuTogl7GHxfK9TsnggOB-WIGMqNqt-0MxphR9cSqbMAUw2Fy4OEr_qq-H9anxbVdvFKiCR2wGvTlo-OP94a9n93bu57IislyDpDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAyJh4Kmi0RZ-MQhlSluNVBpRGV7I35-EamsYuxiBEoU_2zp4K8X0CDpZ1M_BgFuO9hihuqPMp3fz86C3BQLelstByef-JeLVT0NjDMYNV4B8HQBFomy9YBNj9D0nV2a6go9w2LK5caZhzPwTle3UaQlWDJ0Q38oMwwdPd8onQILJoQZE839NYDVx6YrQ_dZegpvQW6AG5Dctqb5Vdux9RfEwslDIa6XuKMC0uPjmTuENfyY2E4nfHMiji6F4sFSHAeZba94pYmsglhZ6TOf7QWRuzxNl8bGeBWYyflC_E8KWMxdgdlaMY76IGnmRNY7y0Va9Wj6mnTfY4qf55PgMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dL3YG6WzlEgDWrfi2B5DRo0jUkO1XnNgi3BDhBDih2CRug2Z3lzY6eJzcEcg6rMbAEWpdnLnfVniZH2F_MkwQf6Yw7g9PyL4zIqylPqdQuUuydM_p_VjyZp3kSynpfmIxTZvCkY1jHeEtX95AXIP0hmYDGJ4a1UhMrhXJ0K3iblGbVxvPyW51cDb_uoR43FSQwFk9kr3-_NRjWjzTeu3n8pZKkprhFZZq91C8_u6c3iwBmlWz2nVyJZ90V5lXAZv86UfhE9ML2bE-zMRpQKquU1EEbjga58jYshPHyMVG7U6BXqz-YdZmLlHpCpL1KF27AxXHbdc45JKh4tej9DDUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5210" target="_blank">📅 15:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzObZgGC0aDe5Z2PTxXhV5DoO7N5TYjJd_R0BJm961GlNU_0CAr2ElA-WxAPfTwZKAadS6KorD8_vQw1SNtVmr49AE40ODye8J_PZPi4ud4NqwFltOQbheWS84TBDDn-nSZBdD5kD4101-LhG2SURoDiAKwCqAsNb8Pct0nW1LNTmqPDZxAq3ngWphtRZuRyHCpNghAaGOFDThwE0i2wgq3t7I7QjCsMs1VymN-n4Wrdv4rsNOSrZhuR49suGqSSQl4dh2FI940iELBQjBR8Q-YwwZkhNljteCKN-79YZ1VqGoWctABFS8ug-2_24Is77brw34L8e31oSqesG8Myqg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=e0X3IiDkmuLqG_Tw6-M5cuUpsIkw7DW6zT0bxkTGm1N6wtqDbAZLh7hBfv3eEBR4DO1vM7OqD-piLwJWq0XRtTnwZZQ4ge6T1-T4NFvrnKsindVcumMTDK6QoU-oKHVK3H8DLxpW0EyqGL_34-6QOT4kjV9FyXbF0osbJaP70cHETV4lqh_wMRGY7V7E6NOFyBVRZPy2j92JVkUfMfzAshC0wzZwv5bbDIctr4i5dqYHReAuSLltsrhOnqtLppWfl3MaHMzWyY0x_IB2MLiKKpg4m5GdLA2iXocGd7KLYbJtORP7po97QM_BpOOCko4t7qKJG7vTuVNF61vlJm_0eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=e0X3IiDkmuLqG_Tw6-M5cuUpsIkw7DW6zT0bxkTGm1N6wtqDbAZLh7hBfv3eEBR4DO1vM7OqD-piLwJWq0XRtTnwZZQ4ge6T1-T4NFvrnKsindVcumMTDK6QoU-oKHVK3H8DLxpW0EyqGL_34-6QOT4kjV9FyXbF0osbJaP70cHETV4lqh_wMRGY7V7E6NOFyBVRZPy2j92JVkUfMfzAshC0wzZwv5bbDIctr4i5dqYHReAuSLltsrhOnqtLppWfl3MaHMzWyY0x_IB2MLiKKpg4m5GdLA2iXocGd7KLYbJtORP7po97QM_BpOOCko4t7qKJG7vTuVNF61vlJm_0eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=ejmVMUKLmjrN57RBRi0UrY7SwVop2fMdpXxwJZBcnB_obBIzmypFpcxf8ZbTnpzVarNs0XilLowJ5VXhTfDzZnwRZgkfXfZFLKGVVaZMwR3JAhd3T-pZA-KnJYesuZMdqFuPJu1fnzOV7yoJi1SPHwBjJ3RAT1QYyXU9lJKRbQ0Uy1pNxHNI2AoWQknNqO-wdb9u0Ny62N8pvDOzSIN0WdHckZ5A8PGZ_spIxO33Gqa-cX0yO_AJ_6WmP_L5scQddx-zTMj0-_T_MXx-OyNYJCMvlqJUIOf60eI42oPPWEmi2i3AozM4POLJVcCVtDx_4L8vmVSMEyKIMRt9TqXRXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=ejmVMUKLmjrN57RBRi0UrY7SwVop2fMdpXxwJZBcnB_obBIzmypFpcxf8ZbTnpzVarNs0XilLowJ5VXhTfDzZnwRZgkfXfZFLKGVVaZMwR3JAhd3T-pZA-KnJYesuZMdqFuPJu1fnzOV7yoJi1SPHwBjJ3RAT1QYyXU9lJKRbQ0Uy1pNxHNI2AoWQknNqO-wdb9u0Ny62N8pvDOzSIN0WdHckZ5A8PGZ_spIxO33Gqa-cX0yO_AJ_6WmP_L5scQddx-zTMj0-_T_MXx-OyNYJCMvlqJUIOf60eI42oPPWEmi2i3AozM4POLJVcCVtDx_4L8vmVSMEyKIMRt9TqXRXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyd9-FvgInwY5APuroUYKNea2UTy6DbRrDW1flJsQ9gPsEiUXTSEpcWyfvfJ4imbpeg6Vos6PTM75gwyXsDG0qZYTmRAM1Ar-LBhTa7zlm3qPwSAIRpYO8onf0UT_Wm0RjctAK5a3C4DFmoWR-U4TcmXoNRs3p4lE87YEav7qYtNCRN9IchTmx1pNRF8OyZ0ALfoRjogESs7gpC5M0v7tvZeuJ05XvUCPD1rEDoOgvND6rkvdfXCTRvSn-ljpcVdcsiZJKz3YH54JLiIobGC9DuDRp7ISihQcatTbc6EqffH0gcgQX8bP_v-V-K-_qDMsiTgyA2_MmYq1BSxOSjmPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5206" target="_blank">📅 10:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_aaBnGtNvXQ9CohA368PM7AOukZDuwGBvN1ilAnHwQwsYvOgh-G5hWSPflthmk39MjqQqLi6FgPl2eX8U5vEwcwBtRjr7Qw3nLacHhHnqv0VVB3WSj0iL6-Ms-4emuuzG9TrrP3m9uq3_FOSCmuKR628NE7JDfEwVRhah6f5h5D8AlpUBgAyCUU8uol0X3zE2Syrz7bOnW9cMGQjI9Z0Gnq25nrI3ESOPuWzZ1O0mHa9ivVMJJQTFoyPOWbLbo_x3Ot8rCYbzkt_I5Stt6N1WDnA7g4wm4am3Kg-dTWFl420Er84cpkJGt4PNjcT0t5Wwx2_pb7upfs-Z-cr5IS5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLhP-Bfmx6ruZmDB_r0wM11YUkK-x-Sm-Ppmdr-kD1x1ynOH4fb1Qm7JIAlg0Tr1_HxFAUs6NgDcTO1oULRvQv-OPwBpvmWbBTKgz7iteny1P-SJX4IP8FW1Xl1OZEO-bhiyM6ngj4McvB-LNm-UCQ0UD0F7RebmFE7yhnCliCy2tCf7l4RCtC7tOF_eUwYDocG77EqLTGcpdAU0VvfQRl7Fv4TtzdCkwEM0mJrKwQBvoqvWqB67oMWzeIsuTiEdc1uyqQ0pSn73ufXRaACeO2hHpL60wk_Ku2xBdCwUvZS4HbyE77pRapznJXN2Q4IdKEc_SbFHTzfPjlOxUvTaRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwxwVBeZ4IvmJYMBwKQB8GTv_dyE4cTNF-SydyuyGS_QQgb40ynzK-tHm95UYiP7mrxn_losvPJkWhkxKrcJRJdcVptYoIIvIVWVQyJmVuKU7iRgxgfd8OiP10nJpq9pOKs01r47n7tF1HVCT4XfTN626MMySR9k9_m7zaNKnAMbmgKTjSaJxkVLYSzH_NgP-Ocsqs3IRqHsbCoYMOxlJhOhadkeSFNkijXjyHW4HKMJHJOeRgmFUEbQsBT7LrmB7zqEdeX6_dIdSJslT4zolU5AovDnP8Z0cIG30lO8k-VnvfidTAs-HkhF_O5pCzlleA4T5_qnf3_Zt4K1nJzOlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/la6C5XS_nxYkZYYTUWw696DRxYflwLBqvGQxPVSJDlPCz2V4twiZHh28jXXTHcQrKlcmDRTgFOJi5y3F8u76PXvI0tt7EfmqjMOe2GG0rLRhxUFSjjl3r0KvLDJfIdh-0_eylwY1EpnDfwIvoI_f5crzRpfoFpHVhlO8NWPjUx7046K1pHnFdnZ06ffkg7rEitH7p0iJYoVAisjK5c0Xh7RqhZc11re7_7ne0C1xo8F6gTLfiYNlqv7xmFGR4JRBpSr28mQwFqoAfjMDQPxjpkoRWnTotGwCF3dZEJUHigpPW8iGNeJ5ft8gKJwarWBqqgDv75nOjxX_9J2MF6x-QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kKxek5zk5zEB3zPtBIfbVibNTf3hO7QoM2fiwLiOfrfH8yNS4t-X42r5qeLUh572vvhja79Qd5zZ0eJqYdp66x0YKYES16W5k-K8qwaHcViE5ojXE2cRhONu_Gcid4PSkSVwn5VWigHWawHKQahZOYKIVcwAeXfmjr-51CiJYbSZhv5ovt3pd-7FyjMeVv3LyqL9WkKDo4Ddo8deRrZTlBExvWDvVs0hYDYONnYs8m5nRAlNZuwtDhvfHtQIGjP7XfQPs9lXEPMbQNynMje_wa3X2g4EmMmVNhbiXa1-bd1yRXSjCXEGIvIaPgq3Fb3TLd28ItXMyKFWaUBfW3WWLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FrexpplZqnsCmfLs8d83f6gsyWbH8LzwU-01yJymUx9y9KqdxnJq6zhIkotOS7KvUbN8f3ygaeTYoZjn7R8cXCq_upnhdSIewIFr5ubAOY42VI6LmYRp_PZ63NKlLks51_6yzvwkM3t4-gawEQ1EhRyPda1WUwJP3aPDAUoHurC3i_P4fCYztjun-EUZ1NbxpfHBENW6pctkb5n5fUoxl8XUUc3ZWzHI8q2dnxgxfMRFdHZ_Xkkgo6f9DeKckfIGxlvcYqnY9hXOu0WzFeJJLI5IDl0R52O1cm-WpfhDxi6qqD_qLdqxovpBLreGfJh3iVu2vxtIpdwC4eMProGx3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oBws6UDBV8ZHXbeio5AAMd3TrsB8qyh1T4o94RHHqCy8tvwTxxl19-iXaZvfv3V2ik1y_xRcdiRioWl1Oikqg5fQ1Lt4IBV6ldIujC0U5MsWRiBR8wjFiG4SXDao7vPEZGEYhN02Y_WpoHlmiegChU6TL0C1RriStK_C4D03F5XzHWfb2Re9HHaUwT1vbd480qd3YlC6EaP3K3asXb9jdLn_4ygFoSLGcF-oYz7eC-elolM1xWhmcpTb95Vjf2eHILYWzrbgrR4yND7j3pZK43tZIpnD3EjMNX11FSe5gjwuo7ysqL7NR9_W1cwILreee_BKOMZ-_Ufq0HeKh1am6Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=pB77luQ8TtWbBBLvReXEZ9wMIKwLsRGWg3IM3CvP-3h4h-89y0X2l2apyBa4nMDBk3QQVJg45cLHwvG0KcXJU9ayw2A5U2sNYQU0Nw5Egc49btnEPNDfwV7JajgwrDF3XaFJmaadybbWvZ5bA9B4ZAWBqxKc8sR83TH1sW0qIvY6VGAsZKGnPkMsQz-smeSF3FU3EDVrLe3VKLqJJUEqHIUWhTOEPMe13pEOmcpuos4KU17eARrmw2F_RLbKqflxTI_XTGst18MYoydpMk0nfr12fAqEeizW4V7-kUQYksRyqeeuL2N64634dNL0eUzJbzLwwYnS_v1zd8C3lMa2qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=pB77luQ8TtWbBBLvReXEZ9wMIKwLsRGWg3IM3CvP-3h4h-89y0X2l2apyBa4nMDBk3QQVJg45cLHwvG0KcXJU9ayw2A5U2sNYQU0Nw5Egc49btnEPNDfwV7JajgwrDF3XaFJmaadybbWvZ5bA9B4ZAWBqxKc8sR83TH1sW0qIvY6VGAsZKGnPkMsQz-smeSF3FU3EDVrLe3VKLqJJUEqHIUWhTOEPMe13pEOmcpuos4KU17eARrmw2F_RLbKqflxTI_XTGst18MYoydpMk0nfr12fAqEeizW4V7-kUQYksRyqeeuL2N64634dNL0eUzJbzLwwYnS_v1zd8C3lMa2qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=Mx2IDTN7fXUL3FCtEFWwlTTKUNqJIpgzSrVfwSDrGBdSRdL2oaoyNcEmxbDxq8T9ElrjPpVhumOy7cLGuPm0rIxxtu2BcHjDPm-wArZ5ab0c8CNgjxzjKEV-vbA1zWOhe7SaxOPcVtfS5bhITu21LWjIOfKNrQ4QRc9SDZLwZsrI2zi1Wy9pnPwEuLPmQNXuHrgAhftbgY3ui4SZUNdXGmJ-yc402OZcXoO3YjXR6-LQobH5QoSbNVdpGUw2Br-khsJ1rsan_mSQhYqG2gz_WCN_194-KWMM_iXZovB9Zkfukai2yTItoJRbzn-7hdLsd8m4-rkbtqebLBWVlmEQjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=Mx2IDTN7fXUL3FCtEFWwlTTKUNqJIpgzSrVfwSDrGBdSRdL2oaoyNcEmxbDxq8T9ElrjPpVhumOy7cLGuPm0rIxxtu2BcHjDPm-wArZ5ab0c8CNgjxzjKEV-vbA1zWOhe7SaxOPcVtfS5bhITu21LWjIOfKNrQ4QRc9SDZLwZsrI2zi1Wy9pnPwEuLPmQNXuHrgAhftbgY3ui4SZUNdXGmJ-yc402OZcXoO3YjXR6-LQobH5QoSbNVdpGUw2Br-khsJ1rsan_mSQhYqG2gz_WCN_194-KWMM_iXZovB9Zkfukai2yTItoJRbzn-7hdLsd8m4-rkbtqebLBWVlmEQjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aO1m3CZvfUr-7D4uQComv0LCTUDZY4u-OGDSfS4XZJpmJaETHz7NW7AxqYeffkTQdgeCdVYhkzc-A_otZjoTeunb4VJHvMYQFSIsvZBmuzxenZrRUhZx5mOzr57WAmiueo7xkCx8zbOjwaEn7XTkThYAZi53XlepcX0l66YWqH65TC7I2y1KKIv1jOLDVZyVsBrpfdA22XxiYVziiVpBNGAcFaTYE7dzi2NG-SqX1h_MdsxtYyiiudPrUP-bM7R9gFzHYRDqZcWk5ADL88h0zIUWSEsdyB6DrLN8qIDxSdQcGSUCI3W6y6DVIYHISZAuxq8oQ6DEL4Ja0fxlTly-oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mBdE2q90u7bD0A1uISp8JhJYsamPdEj6ep-U6iKlVH0aoijBd-6XU_dR7PtHwOPRXXkcUdCIo_sDquqcMeE6Zn-pwWCz4UvtMYiEPW_cP0Q0Y5nVJGhfzFHokjZCqA5e1ujXqoR-lXRFBQUHXQlgaMYmKXYyD0CkWvMygQS8CrRq9FRkpu0MJP1nTyZSI_gzrgdCWxO6yhE8T40gCwGJLIjw_uJtyLeJT8HkYJbGZbqkebT3j7LS6lAWhJSgzcHzMW2WIR67NOuhUJ-qSrCq3wlqwGckOenrgC1XRkdcoQBrwKj2TNWAbsT6n5XP-xqGaXzl7MdBzho517wOGM-EPA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=iee8vriUZznLjaEeOHPNerrZNAM81nSZG1mxtMkPlYQ5i16rLyW_Qa9jMg1x15SHVu_jkhr1dYeSqV1bSOTuA0vmE39kIAbmxRsIMoMg092x9Eo_gDqrJiUsDwlvQRzauKuusRhvXHhmkrtA6WHSkoSC-WEOktHNOnqs-TyW92SmN-vrklGKyOsfSaJCuFWm0d58e7jVZKpZ4Ks98TkZYB-4CjJP6gE3Khmqnlf0ndEeVZaKJ9OuqX6NCfJFkdKm3imKYgHdZoK-lyk5z6LBvG-tHgyX4UujZBXX04QqRiM_kgZi9WvPqfGd7y3qbmXnZPc0rrFK840dsBVyxHIM_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=iee8vriUZznLjaEeOHPNerrZNAM81nSZG1mxtMkPlYQ5i16rLyW_Qa9jMg1x15SHVu_jkhr1dYeSqV1bSOTuA0vmE39kIAbmxRsIMoMg092x9Eo_gDqrJiUsDwlvQRzauKuusRhvXHhmkrtA6WHSkoSC-WEOktHNOnqs-TyW92SmN-vrklGKyOsfSaJCuFWm0d58e7jVZKpZ4Ks98TkZYB-4CjJP6gE3Khmqnlf0ndEeVZaKJ9OuqX6NCfJFkdKm3imKYgHdZoK-lyk5z6LBvG-tHgyX4UujZBXX04QqRiM_kgZi9WvPqfGd7y3qbmXnZPc0rrFK840dsBVyxHIM_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم مشهد از خبر کشته شدن خامنه‌ای</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAALdLUm-Z8nQ1dxXGMelMKMeNyPIJIdR5CHj2qaQcNc5kWQ-wjS5ExSCtA9pESCZz-2AleMdFCmWDLWwxAIZBl6NkSE9_ZHBAiMOAKLoXAgILl68jDNjk-6S5gOT7h_FJBhtgqqnxW2hXi5y7UC7ivwv2XxIRLEbSDyaQ4uayLMuSA3GIIkALnQPgGyCzCcaRi33cD5R8RUQYSZhUbETvBkFuIFTMcYGtlrmd_M8288znMlXZFtC55_Te2MFj5c7oJHpCSu-5m_FaO24r2Aal4YXThedBJTpjTVa3ofGqKz2nC7diLvgXjIav7f8E6EcJFeQocJdq75zS32TExfRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5189" target="_blank">📅 11:02 · 08 Khordad 1405</a></div>
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
