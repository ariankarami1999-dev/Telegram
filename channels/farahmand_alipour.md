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
<p>@farahmand_alipour • 👥 62.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 11:58:49</div>
<hr>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">« سد طالقان را یک شرکت چینی صفر تا صد ساخت، بعد به دروغ
به مردم گفتن که به دست مهندسان ایرانی ساخته شده .»</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farahmand_alipour/5304" target="_blank">📅 09:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sq936ugl26sbwnyE8iB79fB7noR5SqHorlpTfEf4JWFcR4T8eaoDeYDG48FmljMzDqMRdMtFNeDSPO-OZuF9ZWCiPlunWVwEFQ48jb_HekziTxJDe8_xWOvuAoKcAPb1J_lZ3JmWM3F4ZXLbEccpXTzdxcw3O8Ykkk6FTIjNQ_wNYvvaawlMT0YMXXFwwD2PX-MScveol36gyZ1r1mGap2XVtIqv0MwGzLZvWo7DsOligRE2Af1fL4zaL5yYb37mvqLPOC-y3qfiEdAvsU--D3Wn10-8zc-pgGSo9zt1WJVytyvxbqwwYeia-8BK0elWrmaO8DheQlBRJhAKLBC24g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5303" target="_blank">📅 15:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5302" target="_blank">📅 13:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvsN94JSKqsljx9mgbDBRgV_llqF_WAaZnBseHlLELQKKJ3ws65dQqANeVtfIJlnDw9bUkamsXNJMxX4eg__jKNzrsB0NVBfezZhjqJtYhR-RnVEK9Ckf5mA_EDe2PbsO1jc5aPs8PmMOp7tRRFSZ96-ank0yI4ROcmu4mFjI_To5cjVmnd47taemzRA5xmbn_UiuMpRST9nNDkzN5Xvrk5AnGgzG21bPRm0MWUsQeVO7Io2NPo7jATmNBZmLQjg97FZaJOthxu6wfddjrAGzlSlU93BlZwS4XZ0OI1MIJCBBo2EDJ72Ws3dw1s08pVb6fNIhm7-33CJDgroWH2PcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی در ۵۶ سالگی درگذشت.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5301" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تصاویری از فرودگاه کویت
پس از حمله جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5300" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPQwDsb8e5BbH1hHBk83pdT9vAG1x79B7h0LBynwZ8NPcttZT5t3RZopf3hiWBBIv7zpMES_kv-3AWxgm-ma703Uu2nAx4--3HQ5b5KK8QyprJYZ9Ft5P5S97-VAKMwUo-QsunXTOQ7KcmsjlmuzbaVXvSL1sfB4EfGoOvbt6jf_AiZTzFWg1_G0QFq4aDz7AkSXX1ynXd6PIOxsZVA2dbUQrB4xdLPIEoldADTVvkmYTF9u6DhTZmrAR6os34aoVIF3XBtbtST4oRCo3oUSJlUc00N81jLobAJ0zjLd2Nj7V9Xw9yrxeItMrKQxrMm4ynMaC8bhmRAJY5cnOCQO3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5299" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oc7NeffMHacldACBXwHgF5KB9SWjsA0sz6BxNQeeGnJE-jIxQlN9t2ErNgCfzeUItF56PxYjnHLcBuelWVdoGpaz1osWXqIdC7EfeKEE5uwz1T8dONu3kkzI1TBluBsnmvHxLKqmiyauifcRfTzMUhcRTWmaWynDqTor0yBJcRh3JrIXAu8Pc-s0wEi7jxEIWhYsYErpmZwhHuX8CYUWGs8mQdF2qt9y-Oo-5BgiVAFlA6afJTyFra4MDCbMncbOYi8b6pcPSahlaJYSjrN77QaZhCM7H4bMRL8PcC3kVzeH2v7OI9iex9515vHqU-mH0Rvt7oZ0_c_FYX-z5VjIiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کویت ضمن احضار کاردار جمهوری اسلامی، دو دیپلمات جمهوری اسلامی را به عنوان «عنصر نامطلوب» اعلام کرد و از آنها خواست تا ظرف ۲۴ ساعت خاک کویت را ترک کنند.
وزارت دفاع کویت: جمهوری اسلامی امروز ۱۷ پهپاد و ۱۳ موشک بالستیک به سمت کویت شلیک کرد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5298" target="_blank">📅 16:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5297" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کویت : در اثر حمله جمهوری اسلامی به فرودگاه بین‌المللی کویت ۶۳ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5296" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بخش بزرگی از انگیزه جمهوری اسلامی  در حملات پی‌ در پی به دوبی را باید در عقده حقارت جمهوری اسلامی جستجو کرد.  شهری که برای ده‌ها میلیون ایرانی  نماد پیشرفت و توسعه بود، که ظرف ۴۰ سال از هیچ به گوهری درخشان تبدیل شد،  و مردم ایران دائما دوبی  را با ایران  و…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5295" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sB_h4J3ajcoo4MrVzxNnvIjZUBixGq4zulHGegUyYGdHTLtT08E8jz1W3XA4nhedTJXUXZWsKcx-VXtnZDAXFVAJxBdLyXNx1sX-GoNNCS7aYJg2SK-GbIy_JrwSAJWWpce_7UAeuUcH_ostBsPebiMTaL-bTQFd0-rtsV9UaVEgIVjTkdL1MjHlQBbAjxauPIkXTwXeORUX11K_7InXaxp1n9H2GBU1MXU-UflyhuZuQsx_hnAlTOeKCI5negBKzE-2yvdArIk5VOSS4wJL5y2GNByr4qSp2Ers_fLzM9VBrWwJGM7QUW4KM2VdxHnWBGn2LX9fTtRw7zR6G2v7OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/txebbeCzWXayH7eLVE4yIwEMmL7Uh2PuOzRC_NOnMGf7GLsQnq5QBFP4zbgqEmGuDiTVp2I2CuMZ0gDjeyBVblQVx3NanEpZ7KzOP1KpynPUd6QAmVlSi6HpPFVm6YRcxyrSCZLuSRQS7IAYGTOh-570c8kvHdHIKf0NAYCqi9sGg-d2n_va8_CDF5EI6d93VjsT8rRyViWCKv_8vEG3vmaCNiZuaUC4dH7YOPLPJBFL0peL9AprG5iX5Ayj2KH5_5BFvIwye2ekcu51pbWM8nxU3d847DEXziNTFzOWpIa9Znt0S_BjwDDcPPPdAOCPnG_iGIzep-owdqqHiDUgRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XuF6JUawgeSKBR1h4twdsPkVJj_xAbhBdm2oSyebFqXm6cvM-Oui7McAps9oRK5NkNvgGTT2ckO05Vwz3Kq1NIuOzbPHZaXH2njUWyfPUWvgyrH72Nb2WYc2bPv5CXU96nzBOewKFTIbjKTuyGOsqxGQhZbI6D3GggBOKkf4Ht9NSEhUaDG7UlkLXTen2g5E_6BFkeqk9M1oAiTk2OrBi070VYdl_R51vK8YeKTqJl9FAIw1WPenHFMFwTHFvdf22ewuMN_1ytmQsPlEwiO2I3Z0XjoRS2tfY26ltP1IO_pyHt24aRSpvJ1Hrlvs23hJFXyPfPaI-QcnI1BzTOw7ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درست ۲ روز پیش کویت ترمینال شماره یک اش رو دوباره بازسازی و افتتاح کرده بود،
که جمهوری اسلامی دقیقا همین ترمینال رو دیشب با موشک زد!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=qFuhHKhLSnnYEpXE323cfmbGwT2if47uWk4Y-wFLXBN0Z3D2O8DZdYokB8060_r_oaETIVqjq63WTqT-dI7FxbUVNboElcL7v4sGTaeMLjAkrgPH8FzqlLq-niTlyiJUa-WRM09i_nC6A0JiS7HK5SFPeTPM4ZMqPL_d835CJOTU1i2tDJjdut1eCQpwTtUPtlY5lGNmjuJfGjaFnaIcv5BvHZ2h8bFIzNOR4JhP6YictXG6YSiVvFkj-Zu-fAuKufXFAg-Z2dxN11JMLpaxZXYfqKjHS-K62BUrPFevUpz6pFXMKF2e8PLvHC5gS2NgLHf5u28Epx9Toe87GEPORg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=qFuhHKhLSnnYEpXE323cfmbGwT2if47uWk4Y-wFLXBN0Z3D2O8DZdYokB8060_r_oaETIVqjq63WTqT-dI7FxbUVNboElcL7v4sGTaeMLjAkrgPH8FzqlLq-niTlyiJUa-WRM09i_nC6A0JiS7HK5SFPeTPM4ZMqPL_d835CJOTU1i2tDJjdut1eCQpwTtUPtlY5lGNmjuJfGjaFnaIcv5BvHZ2h8bFIzNOR4JhP6YictXG6YSiVvFkj-Zu-fAuKufXFAg-Z2dxN11JMLpaxZXYfqKjHS-K62BUrPFevUpz6pFXMKF2e8PLvHC5gS2NgLHf5u28Epx9Toe87GEPORg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c026494834.mp4?token=SYfe5TGmTxzxBPtHFMaA284xFIDzACzCAeaWMsElGnoc8i0CRaXCxVUYPpAV_-L6Y_k4ht7kRyLTkTJt6B6syU8sVm8WxOKo3xQvtWNmxXp-HdoAdQy9rz2wkcD8j-N49R4_PrQVhc7ro6Q0JaHlfk4g0AuLE_eqJZxuKnxirYTvtITnt9PvkRTNOToZ_UHMouRn0ae43acrHK9RGO234Ryn0UknOJUgJElABgedHqThsssg3m93kGXnt7xRoHdWAqALnSf6TWTcwx00t-wbgVHCd_smEeERMuFXHv2zwoFrjm966lvvQKn5nZZSjPh-_MV93GflC2Z3Cw4dsBKAKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c026494834.mp4?token=SYfe5TGmTxzxBPtHFMaA284xFIDzACzCAeaWMsElGnoc8i0CRaXCxVUYPpAV_-L6Y_k4ht7kRyLTkTJt6B6syU8sVm8WxOKo3xQvtWNmxXp-HdoAdQy9rz2wkcD8j-N49R4_PrQVhc7ro6Q0JaHlfk4g0AuLE_eqJZxuKnxirYTvtITnt9PvkRTNOToZ_UHMouRn0ae43acrHK9RGO234Ryn0UknOJUgJElABgedHqThsssg3m93kGXnt7xRoHdWAqALnSf6TWTcwx00t-wbgVHCd_smEeERMuFXHv2zwoFrjm966lvvQKn5nZZSjPh-_MV93GflC2Z3Cw4dsBKAKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی
حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxJatbVr9wU8S7RSh7iUAlY03H1-MafY9RulTGe_ER08nppsb2zkslFHsgQ6HEBpwXUe9I4ZRPaPJwLtxJ8rTn03LOWyj41P5dpd0T-RQ6CV_1XYLVzldsck6bDc06CSLE-Uiq8i0hfh7uNZGLhfMdCVfQn8pt_SRxGdtPdIDYtZsK-FtGJUaE0crvgjjn686B9nNF48fkNsqBMLxXQkOZAbHbw4Qob-Q3abic6VzzEatUzZdrLlI_mhHArfbmEZ3LcGLWDHImM3MYtX_Hdk1dEEkJ-i-_I_Al66w8LMuH9WXwbH37VIpGXlfP01N1ZX-9xd0SSMOhNSQ2GnL34sB4QE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxJatbVr9wU8S7RSh7iUAlY03H1-MafY9RulTGe_ER08nppsb2zkslFHsgQ6HEBpwXUe9I4ZRPaPJwLtxJ8rTn03LOWyj41P5dpd0T-RQ6CV_1XYLVzldsck6bDc06CSLE-Uiq8i0hfh7uNZGLhfMdCVfQn8pt_SRxGdtPdIDYtZsK-FtGJUaE0crvgjjn686B9nNF48fkNsqBMLxXQkOZAbHbw4Qob-Q3abic6VzzEatUzZdrLlI_mhHArfbmEZ3LcGLWDHImM3MYtX_Hdk1dEEkJ-i-_I_Al66w8LMuH9WXwbH37VIpGXlfP01N1ZX-9xd0SSMOhNSQ2GnL34sB4QE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5289" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kj2QsYtbUQ9aJM0MvD0I80tY2sDysRMnJTu4SbZEamgZMYNtvWHscRZL5EN70lN2WrfUeM5Lrh0Xd1ufT2YmTh1C_cfMnVab0pms4x8aXa_mZp3iwEoMDtpXRdmdLyysNvPx7QhOOwCen_xxIXQwQ2t5X3Ho3_xy8jnIvH3rhW9e4YwoZPzlegAjRkK-sZ5DnUC4obeDBX_7-vUh8HHFx0zIaDdsygOAYZftpsRUI80UR-zye3-WDGVr2iiqCq0VhzB3LXNtV72EcN3UfdDe_Lw5isY7Th87ZFkvf0tv0FwrL35SZYWvGUc9F382BskIKb8JiitptAxEFmgGJWcdhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت ۸ صبح حمله صورت گرفت
(توی روضه‌هاشون هم‌ میگن رهبرمون گشنه و تشنه بود! ساعت ۸ صبح!)
اینها همون بگیم ساعت ۱۰ صبح فهمیدن! اما دائم تکذیب میکردن!
نیمه شب به وقت ایران تایید کردن،
اونهم زمانی که ترامپ و نتانیاهو با قاطعیت و رسما نوشتن که حذف شده!
اگه این دو نمی‌نوشتن هنوز میگفتن خامنه‌ای زنده است و «کمین» کرده
و داره رهبری میکنه و…..!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5288" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4JrqjdkAKLAzGyDSwTy0rpuTiXkMrBJ46imhkImn6--XE2dz-yw3EVE1Fd5ppRqGOtcfPsa7dgmJt3V6IW_Jhp00NEnPMdrLnjY1cc-4jH3xlH-TVlL8VOslbNGjhn2J1s4bDV8NBym4UJBImmCNI4rVs2wGcihEMsGaIf9x-SBkhB0-Js8MjmIsP8HLfhipv-5vnqBvWjb7cOOCRT-1DhLCkDCezfdIO8tsCe7U-uSrYItT81MGjCHQCwD2MbvAY7PfUQjSI1aMzFqOQ5qHdP_XzebcFEcEwZxed1U1eUTnMXcd9nVT9YZglj4LWBo9G8GGMVoXEFX24xL61MzIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015500535c.mp4?token=dsaliq_6DWYE8KHuih0fQKmYhCROn_ZdOu-i6Rkvh9L7sfMSOJW2umkRaCQU7u2Ef-Snm5xxUp0yTc_Y_-AVzhK42KXumvAFrqrvlBMri-UOnoZXIvI2ZUGHe2ixdX8AEIOQAakWRluypqc7ghnvqXbTsp-iwz16_Lw_TiEb-MrLDPNUD7nNSpdqAqcrQ8R-mZBnsXx_dSNYHz-PWEBDDaVJfk755vGVUbyrw44Dzq2F8FO3_DREDHB3hq9IU9T-Pu85_ymKpnI_N2BAfJ_u8UMgMAUDueJgnQTBoJj0hpW-64YNpvYPR_hkctMnQyHwzB1b7V3k8cuJjrWMBDcHEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015500535c.mp4?token=dsaliq_6DWYE8KHuih0fQKmYhCROn_ZdOu-i6Rkvh9L7sfMSOJW2umkRaCQU7u2Ef-Snm5xxUp0yTc_Y_-AVzhK42KXumvAFrqrvlBMri-UOnoZXIvI2ZUGHe2ixdX8AEIOQAakWRluypqc7ghnvqXbTsp-iwz16_Lw_TiEb-MrLDPNUD7nNSpdqAqcrQ8R-mZBnsXx_dSNYHz-PWEBDDaVJfk755vGVUbyrw44Dzq2F8FO3_DREDHB3hq9IU9T-Pu85_ymKpnI_N2BAfJ_u8UMgMAUDueJgnQTBoJj0hpW-64YNpvYPR_hkctMnQyHwzB1b7V3k8cuJjrWMBDcHEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5286" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">وارونه گویی!
به خاطر دشمنی با اسرائیل رفتن دور تا دور اسرائیل گروه‌های مسلح ایجاد کردن، پول و سلاح دادن، حماس، جنبش جهاد اسلامی، حزب‌الله و… تا دائم با اسرائیل در جنگ باشن، خود خامنه‌ای بارها تهدید کرد و گفت «کرانه باختری» رو هم مسلح میکنیم علیه اسرائیل!
حالا که اونها برگشتن حمله کردن، میگن ما اونها رو برای دفاع ساخته بودیم که بهمون حمله نکنن!!
نه خیر! ساخته بودید که حمله کنید! نه دفاع! که هم اونها رو زدن، هم اومدن سراغ خودتون!
و الا اسرائیل زمان حکومت شاه، با ایران دشمنی نداشت! جنگی با ایران نداشت!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5285" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‏روایت سی‌ان‌ان از درگیری شب گذشته ج‌ا و آمریکا در خلیج فارس
‏ایالات متحده و ج‌ا در یکی از سنگین‌ترین شب‌های حملات از زمان آغاز آتش‌بس در آوریل، دست به تبادل حمله زده‌اند
‏به نظر می‌رسد درگیری‌های شب سه‌شنبه زمانی آغاز شد که ارتش آمریکا با استفاده از موشک هلفایر، یک نفت‌کش با پرچم بوتسوانا را که به سمت بندری ایرانی در جزیره خارک در حرکت بود، هدف قرار داد. به گفته فرماندهی مرکزی ایالات متحده (سنتکام)، این کشتی با محاصره دریایی بنادر ایران توسط آمریکا همکاری نکرده بود.
‏در پاسخ، ج‌ا اعلام کرد به یک کشتی با پرچم لیبریا موشک شلیک کرده است.
‏اما تشدید خطرناک‌تر پس از آن رخ داد که آمریکا یک ایستگاه کنترل زمینی نظامی ج‌ا را در جزیره قشم، نزدیک تنگه هرمز، هدف قرار داد و این موضوع باعث شد ج‌ا به کشورهای کویت و بحرین در منطقه خلیج فارس موشک و پهپاد شلیک کند.
‏ج‌ا اعلام کرد که «یک پایگاه هوایی و بالگردی آمریکایی» در منطقه و همچنین مقر ناوگان پنجم ایالات متحده در بحرین را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5284" target="_blank">📅 09:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خبری که ایتالیا رو شوکه کرده:
یک پاکستانی در جنوب ایتالیا،  با ریختن بنزین ۴ نفر (۳ افغانستانی و یک پاکستانی) را در یک خودرو به آتش کشید و کشت!
https://www.instagram.com/reel/DZF42fzqtho/?igsh=aTJocnQzcWw5dWVj</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5283" target="_blank">📅 08:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سنتکام : حملات موشکی جمهوری اسلامی به بحرین و کویت ناکام ماند. موشک‌ها رهگیری و منهدم شدند.
به اهدافی در قشم حمله کردیم.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5282" target="_blank">📅 08:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSreyKfRdQQ98GrFZoOPc7hPicCwyHOaAgcvcN6_z4mTwUAMcbcQKfGjbJeyED8R-uKy4MEujkxdQxeW_jJ3iu8EKi7uEMpToXbAVuhmM7k55-DUfRYJvCG8ZTGv6IxplEwZ6kxxKKgX94h0xdtx4tDYvitOvkyw_4VOVkyc0cJEmiWO-Win74BdOmrCHZRelPt9zJQcPcyvG4SBsQvsabB9lqUkDbsepvBMXXfFQWXGdaptRK-saT8xvdovydaXVpSzwScuBEjiaXkMVbPRndiqsLea8x6JjTsIhXYIZ7WOOIniThu32ACJC7zQb7FE1QGa6DqEQwh1FIYojUcodg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم اعدام برای دو برادر دو قلوی یتیم فقط به اتهام داشتن تصاویر ساختمان‌های تخریب شده در تلفن همراه</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5281" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجارهای تازه در قشم
🚨
فعال شدن ضد هوایی در عربستان</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5280" target="_blank">📅 02:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله ج‌ا به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5279" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
حمله موشکی جمهوری اسلامی به اربیل در عراق و به بحرین!
حمله مجدد موشکی ج‌ا به کویت.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5278" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=B_qcTRY-A3fz6HZk_5i54tIJQQ4qyE-FujbJpV3ow2PgPDV2clAC9G5-cM_jA1FcecuKSEL-6_rUNoliNcLgFze7c6XehC7Y0xG7G1Kylz--GsLMOr_jGfm65lpZaxjJj1zBoJpWe7f4tAea-ozhhRRzSIP4ZBbcVaOHF2t8jHhhEzKDctdW1zcUgeaOmb5c97U8APS1G4477byriYVJ8CNR4kTa2oAVKa6kqvi8E9S_R7JaQa-SqnieM2-O3sNdeXEShOuhIKyHbV0dpgtHEWcmp8hoIK8cnVTyIyHRrupKL_ezWomSsZoSnS11zLiPO9T4riZCOAiORcZ22qwjDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=B_qcTRY-A3fz6HZk_5i54tIJQQ4qyE-FujbJpV3ow2PgPDV2clAC9G5-cM_jA1FcecuKSEL-6_rUNoliNcLgFze7c6XehC7Y0xG7G1Kylz--GsLMOr_jGfm65lpZaxjJj1zBoJpWe7f4tAea-ozhhRRzSIP4ZBbcVaOHF2t8jHhhEzKDctdW1zcUgeaOmb5c97U8APS1G4477byriYVJ8CNR4kTa2oAVKa6kqvi8E9S_R7JaQa-SqnieM2-O3sNdeXEShOuhIKyHbV0dpgtHEWcmp8hoIK8cnVTyIyHRrupKL_ezWomSsZoSnS11zLiPO9T4riZCOAiORcZ22qwjDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امشب جمهوری اسلامی به کویت
و انهدام موشک‌ها در آسمان کویت</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5277" target="_blank">📅 02:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سنتکام:
نیروهای ما یک نفتکش خالی را در خلیج فارس که به سمت یکی از بنادر ایران در حرکت بود، متوقف کردند.
نفتکش توقیف‌شده توسط نیروهای ما، پرچم بوتسوانا را برافراشته بود و خدمه آن به دستورات داده‌شده تمکین نکردند.
یک هواپیمای آمریکایی با شلیک موشک به موتورخانه نفتکش، آن را از کار انداخت.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5276" target="_blank">📅 01:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ارتش کویت : حملات موشکی و پهپادی به کویت.
برخی از رسانه‌ها از شلیک سه موشک از منطقه‌ای نزدیک شیراز خبر داده‌اند.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5275" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
شنیده شدن صدای آژیر خطر در کویت</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5274" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر :
شنیده شدن صدای انفجار در محدوده جزیره قشم
‏بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است.
‏
‏بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست و هیچ‌ یک از نهادهای رسمی  نظامی و انتظامی تا این لحظه درباره علت وقوع این صداها اظهارنظری نکرده‌اند.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5273" target="_blank">📅 01:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=AqC-_beI_rg1nsO1vXPqs4SiyxNN0Qel4dtiilQfqcThqEnoY-1cPwpuqw8xsWTpY_LD4gdrohqoyqIRyWcme8FDdo6XIOhBpkdw0Lb4dhqo88-gUae3Fyb-Gfj8HkLOSkEOYmF9klfMqhzwnYoTmte7PJvcQi2uJFF0IS-uCnHQ1zkYfNER9lO4vXjqokBgk9mQ5af3fzLgWTKw-XYziCq-cMeqrxGnXTGSaXu_8w2FpzkUCsQdzWjDUFR_c5mxqgVLYi8h2sDNZsyVnAPk2_jgq_QiolyizaxIeUXQLRZJ9rPgBb4L2py-vm-5HMlJaubyXHiu-ayawNEXFsLbzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=AqC-_beI_rg1nsO1vXPqs4SiyxNN0Qel4dtiilQfqcThqEnoY-1cPwpuqw8xsWTpY_LD4gdrohqoyqIRyWcme8FDdo6XIOhBpkdw0Lb4dhqo88-gUae3Fyb-Gfj8HkLOSkEOYmF9klfMqhzwnYoTmte7PJvcQi2uJFF0IS-uCnHQ1zkYfNER9lO4vXjqokBgk9mQ5af3fzLgWTKw-XYziCq-cMeqrxGnXTGSaXu_8w2FpzkUCsQdzWjDUFR_c5mxqgVLYi8h2sDNZsyVnAPk2_jgq_QiolyizaxIeUXQLRZJ9rPgBb4L2py-vm-5HMlJaubyXHiu-ayawNEXFsLbzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.  پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5271" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5270">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=IJYee6O0yfXpcxmky1IHFVHFrT8QC4S2s9JBR1syCtX_FrRcjmz7ckFZAAbO8IIsK06sP8JgmZxVtVGBeYYEBUMl1gn-nEHkJS9Xo33IJ4f9GlHKT0dryUnyiRMG9iyFUJq_Nfjs5jXWpWn6EUWsc461OG-CNh4i3L0Sbb4XRw_8da4zDFFjk-WaGPgSf9YTX3hNjKZ_p6CGYLQadL7Baq8r19FaTU7mkSM3B9qgATB3A_M2f1u_zbdTiUI0TFnHhQ2H-K8ZiyXUUkHptephJrBgHnMf1LuSjQC7Sv1thlkXLxZ80yc_Gl679TVD6n_ezFjv7K-aZ1tcsWcIrgR3_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=IJYee6O0yfXpcxmky1IHFVHFrT8QC4S2s9JBR1syCtX_FrRcjmz7ckFZAAbO8IIsK06sP8JgmZxVtVGBeYYEBUMl1gn-nEHkJS9Xo33IJ4f9GlHKT0dryUnyiRMG9iyFUJq_Nfjs5jXWpWn6EUWsc461OG-CNh4i3L0Sbb4XRw_8da4zDFFjk-WaGPgSf9YTX3hNjKZ_p6CGYLQadL7Baq8r19FaTU7mkSM3B9qgATB3A_M2f1u_zbdTiUI0TFnHhQ2H-K8ZiyXUUkHptephJrBgHnMf1LuSjQC7Sv1thlkXLxZ80yc_Gl679TVD6n_ezFjv7K-aZ1tcsWcIrgR3_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=Uin0h9R-ojsCZB46OOdw8xXyJNP6Uwk8HLc-1U52K8Tol5YxsKq4Wja-1rQWVQN3nn8ICWq29YaZx98K3vL14hmt16pEe4ZyMP5jFHxcLqzpkOKsq8I8yP0jFkU4Oi_WurKgxofZZ1o74gg9KRJIe0pKL1015P87z9Sr4J4wjckXJIuEyTgqxZ-kh_2ZR5kZklBJluun8lpItqVsmPOiZfMtYw96tO2lI5k3aIG0Zt4ze691KhU9zoOE8QkFRa8LrKIliEmDBP4uvD6g5Cm5FO3NVObIQ0DRVqGlhT96Dbnjhd0Fm0xsx6SvCvUtb5iSH41N1y23S5ofhxfnFrzHwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=Uin0h9R-ojsCZB46OOdw8xXyJNP6Uwk8HLc-1U52K8Tol5YxsKq4Wja-1rQWVQN3nn8ICWq29YaZx98K3vL14hmt16pEe4ZyMP5jFHxcLqzpkOKsq8I8yP0jFkU4Oi_WurKgxofZZ1o74gg9KRJIe0pKL1015P87z9Sr4J4wjckXJIuEyTgqxZ-kh_2ZR5kZklBJluun8lpItqVsmPOiZfMtYw96tO2lI5k3aIG0Zt4ze691KhU9zoOE8QkFRa8LrKIliEmDBP4uvD6g5Cm5FO3NVObIQ0DRVqGlhT96Dbnjhd0Fm0xsx6SvCvUtb5iSH41N1y23S5ofhxfnFrzHwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در میدان انقلاب تهران چه شعاری میدادن؟
نحن جنود الدین و العقیده / لبنان لن نترکها وحیده
ما سربازان دین و عقیده هستیم،
لبنان را تنها نمیگذاریم
(همون لبنانی که سفیر جمهوری اسلامی رو اخراج کرده و میگه این جنگ رو جمهوری اسلامی سر لبنان آوار کرده)
فردا که جنگ بشه میان میگن :
موضوع ایرانه! تجزیه ایرانه! برای خاکه!
رستم تهمتن و آرش و شاپور و…..!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5269" target="_blank">📅 17:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">حالا اینها با همین سوابقشون!  بزرگترین حامیان غزه و … هستن!  دوستانه بهتون میگم، روایت فلسطین و مدلی که جمهوری اسلامی  به خورد همه ما داد، و اینهمه براش هزینه کرد و پاش پول میریزه تا همیشه جنگ باشه و خصومت باشه و…..  نه تنها از بزرگ‌ترین دروغ‌های یک طرفه …</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5268" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-Xls6dvkSnorcL_TWPVZA0NOfPs2JEMj0nBuGU28oUPpCkcKNL-bDnuJZ1_gZT1g9FgVRshtcUeQBm11VRhbLOiADWLaSdaGuqgbpmLDutpPldVtYzdA6tKshb7nIqKUWPCbXyD4BJMJkfmbtSwqmiWgC8pqCA-VjqmEjcPKK77Ow5dNv3RW5aDZEnpO8ceKbWd8-MjNnln-pkLF8WXOPRvsA-Upyqyl9g86aPh7TyL_J3oNj4m8Wp80Ajhyr_h6D7XLTk-h5FTmMc0mxSjV48B0-x1lOZevq3NtraGrVgUpabrlZjCPvayrMXqljqC84VYUnXveaoEn45wypNUvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLWAI5r-Qjzh3KQSiz3FEoCiDY0_hgJah3osemO_bMq50AWaqWegsSDizselervlxMHVl_c5T7U1jagzB6Y6xPw2Y6HfrkH3-JF1pL5c-05kbLV-0SYILKzZYEQOUniuqqhEP1Bbftss6ALS_n0tzukhrA-38m0YvgWd3Hu8tzbBAgWgIuH051NkErvM0xBVvA0lTJ5QP_NUDjDB7hctHKgEScE5FX_xmAtllcJad7Q_xYqA7aOfT4wV1PtSxa4HtpC7vNhkGvkDRgLRyGBCtd_gK1zspZ3_IzbSv3PzRWHsK8sW1IC2TLN9eSezXQYxbfGzk-a5nLA6MQehIxOujQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjEjGp4yCYvLVpswlNzbu6pdcA9dL9qCtUef4axnRb56WgGE1EQOvFRJq-ZZ9JAngiXb3HsNC7xVSVzkBAe6xPG2xac78ImbGY_Z1mgkC-LCctgXbr7fYY2JqcPrPFXwzWaD9i8cuygkB0IxCv9lPiEHVnWO4dVAaRDuxdHDzZBwrKaixCIUE62_oQVn1uG8xizcBOM89vC8F7VubMXK_5wsZ36krRagIUpNbNgL-Wo9F2xTcZgLL1vMngrJrNwDY2Ui_pRltPkIzRPqINVi5g0VjZNjWIwuGxXTMkVhe4UmdNWSOPbgYJ5MjVjXnJN_eC-uhA6O5GQucDIOY90bKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5265" target="_blank">📅 15:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brbGVof-emCevhgY8vDpB8avuAq6Cxk_eG-BqHmHjW3q1wRMW34uBR689UJ3H01ivB5CEeQVuUO3BXley4Fywuw_pJoYYAHKd-PkoaUdWECagDOdlZ0Q7xT8YWC3rO5QGhFM2QgvwOzZwk6zWmKA3UcSh39llRRByLx3IK1Bt9Nkn0onYn-dGHuWp5z8aZGABAZvoy_2EXiG6IKFBAybPbEDffZF2Pi6jOtLS0x-Eko52N0d_6F30-Za5twLz7jy56DoaoJLbd1x1XGuNvTy9wqP2AphzyeCshp6ekRgJVgeQZNbQ5Df4dPZYqWm36AfM0z1es3Ba3M_zmEPC-TFDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrG8m-0Xr-5HcZ2o8AuKT-OvCQA8hPLiEmcXVxWqdv6HkydVrAz5nh03SEgqnaI_3s_UXXKXvUmtLTehHrt8H9I31u01glxBYPU46eZOByrphq6sMsSUWrV5shyA6U7oBcPFcL8jjDNHOe00-n2RFXjxWTw80Uj2iek9mWCvD0fq-blfWiy4PDjpHrQCbr0UI-L7en2_r5AAVPHk5OPTer6eXGTk2VP9_sbZ3EK5IXoGcmaapzwjFzoKHZDraPXgbUxrfZm6MvkqdA0jEfc6jJpRUYQ3bTLXlbdqNTJxmOFiHt3yl8MEQzxY0qgzzHMtIN-XR_r4fNWz-C2pWGxRkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUjHG-f0BK-vFVzdbHJiI_gBbBKrqlm-4h5nyUlxDkvYoL884ULK6r4c_wiN_kUxBvGNTQiJXS1nR8fJeJcwFkCP2-OnchoKpWja8ALpyHDTObwDvqs3ipTGdsOZoPYQf0twdF-nuPl0kkeuIrCW_8x3UNhq8rxmadQYHaNxdT5qT90AubeoslV6qY5SVFHna3EQ2sqBbd6kpaMhfFF6IAnfw_g_c268Yw_dAyZ43ZbbRldD2NcN0mB68IPErK3GgdoMeExQb6IQKSajz68Yt-YoN9VYLms02BkVXvz--ut7MI3sxmDUS8jZK5MMkr_x80io6rrqKogx7sR-eotSmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sI5ZMNWUMUM3c86hpt_3cCdlR7GktVcuv2C_lSnd1xnfPj3hMGEAiXwxWZ0Z6T2FWVmchewC7-I5Ck_bbdsoy-ZFg1ssN66L5epWV7XZ1tDuWc9Fb5hAbdlI4bnowFeXrY0Z1xXxqW_4Y9fjnTCjwcRn9yJjmxiC_ouby2LwDh_vyiDFfxk-kTJUCVpq5awN80GAH3c5nXtgcu4pKful9EbxGP0rmJcn7omU0PB885wCULeDoO6s-A20TuS6QchY-1xwUgOGFI87tOuCsLnSTud6xQUCqCoKTOfJkIOr5eYrN-JhQq1TcR9KdkCTdp-OvA7rUGd9TJrqULnbQRpNWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=mRCpwo3A4cMNQZN_dnG98yinn0OhsEIxgiOgc5KGkhNHLa50Odqq_rAmatgQMIch5ELpQ_FP9E-GXv73Ca7PI8KPqCIMhwIPI-2_kjFIAElwJv2UrnSXHwU01IU_NLDRvqLT6Mrit90qrBMt36yTTkOZr7yWnz9oixY5ple8fybqbYFvIGXs_24P6MdnIUtB7ACYGY-v91alQpT4NFKDM3OkNUTQ5TyxJgFVYc02xFAEJ1hnEyHby5N5ktPv0-f0IfTYqISmdQfdQs5YmGC_HpMM1PNgzadG6iSUC7AFpJMZPNogBIKUx6t6oRend4WZkYnQij65tnJYZ7fqfietWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=mRCpwo3A4cMNQZN_dnG98yinn0OhsEIxgiOgc5KGkhNHLa50Odqq_rAmatgQMIch5ELpQ_FP9E-GXv73Ca7PI8KPqCIMhwIPI-2_kjFIAElwJv2UrnSXHwU01IU_NLDRvqLT6Mrit90qrBMt36yTTkOZr7yWnz9oixY5ple8fybqbYFvIGXs_24P6MdnIUtB7ACYGY-v91alQpT4NFKDM3OkNUTQ5TyxJgFVYc02xFAEJ1hnEyHby5N5ktPv0-f0IfTYqISmdQfdQs5YmGC_HpMM1PNgzadG6iSUC7AFpJMZPNogBIKUx6t6oRend4WZkYnQij65tnJYZ7fqfietWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hh-npEdaEwKWREUysMeNV_e8j3VheCdwrajh7yTsvdagyNqUXiLJVecos_xqjDKhkjy35R4LTWZkQPJbfl9BhbTWYFomLl-olGniJk0hMjUkUl23e07WiM2tYnra2mMgNwuNH1S9d3jW9nmJ4XSM_i0g2Qp2zhl3ylDkXnTe6fy6i_8Q5GcTrmMSeRqC_Nn9D0yR6k5RRc6S79RRV8Ii-R5HqdTbN4wtcvMqgOkg2QKCCIQ5S8rZAgISFnYWb6Fg9ZZ416Ir9yh2RCKCwTZ-Jjsue54P9D02OKrruoOYOPyOTUwcyhtBbNFgnEMkirlhZqdJCjGv11ylHFOGJt3Q6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KVGEZ_t16CqTWWghuya_DMAKjDK_fIUjPOS-PecKem4gxKd1ZPtcvPDwcOIBHBqHjI4vWnlBnIoAeJocXqpmfipRRZd0arxvz-4NZVSWGE7Vn6L63V4cTu9dEM9mXcsco_ubp0ETqmcZxjr31MOvIovPL2Y1rqRV01cgCnDcSoGAoY9X1v16oebg6kbln9G5in-NXoaPrjSb_RvV97o0QfKdsv7qa905xg3AapcQ_FX3nJIuO-81NPnDlq8rAwiemdITL1VdPW7BERhUilMLX914MF39WJ3xpWvR4YyXh-wskWrsGB_HTEGKBZ-PksfacjX5A2QThNio2Ic_H_Q7bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qvI0y_x9aO7rAYdUsFoWmoImTpa5PUVLKHsBsGtQcQuHjODqZryqyAvvdmoEfZ16jqck83hQFhBdV9gejoOAfm5xfbQ1nVDuSKHqVw_bhv0HWTufqxS-9Ew8MMNS7eGctblC_868s-0KLqAHyvc58dGqWloZ75PXdQd47ws5ZD-mF3swuxnlwGxZa7IrYMzjYD20qalBWEh6kxR5eQ47uri_iPKQ3zukKC5H7yeuZn_Zb0D4QOnRMJP6Fv1nAUf_4mifSrzgMC4M3W06rU9FT7j21qbdZjLUDQi5P46hTFaksTpPLHe_usndHIGkTJj4Utx2WcnghdrVIi2P-T3NfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،
خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!
در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان
رو پذیرفتن،
اما «خسرو پناه»! مخالفت کرده و همه چی قفل شده!
خسرو پناه کیه؟ دبیر شورای عالی انقلاب فرهنگی
که توسط خامنه‌ای انتخاب شده و نهاد به قول خودشون انقلابی است! و قدرت و نفوذش در مدارس و دانشگاه و….. از رئیس جمهور و وزرای آموزش و پرورش و آموزش عالی بالاتره!!!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5257" target="_blank">📅 13:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fx6IsnKm6jz1LkLtoId7MRcbHYMVzxHUxY-SxZaZGAZxecN0QUlYfUjeVhdnc9FRGem6FlnJeX-lr83r5bZ1E-F60snN_r0D-rukaVvWcI_zqpvUIbs1FclQshxHzdOe7_bWKSjjdLd4dqNTTVQh_eniOV6JmL-o3QjEi6If1ompwhjSZkmmig82v2ujPVkuCC4wy1Nj5S9I_C8UGi-5xUFICwqobcDkbuTdX2tbOmJ6GMXLhX7fhbK16kbgaLA36kEnobX0sXPcbj-nanb6YT-bHbFvSOUYpDTmFLe4vHfBTRNONv_EhrmB9zvN0uPYaD66dRultdOzhijyEuLxKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rnV8ooBisgdU7Kgi5ZAl0F_ytiEFUgLru-KGzyzVzCQK0JTFJ9SQ2pvzTrD8AX2KJfMhqs-8JrlheSCRScQ8aTXH5SJ2oIlDxbh2BniefMZqgXTBUrRAVnqsx_gd2Wft2kjfC8qHh7G3DqTXBIy6PhEO4MB6BZIAVYlF7Jjl4WjnBaTKbzxgyEHE0YyYauiVCLvyceHuQFdZmml59Tu7LYGkScJRRoNdvN0qRf0ASq1hDU_ynNcVi0cAJAMc-MU1-_moXXAYHnYlLwesDSJbzUefJavdZkaigY_YRZ9MCgXJy9I1O9H2RaECKFchV2c4_BhkUfk_ytIuoXk5kSwgZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nkua1Oj_OvCCOE3_1W8s_SdQzUJ7HRTHyaysn57lLgWqxMdKyzR9lH1Jn2dJL4DmUeG3PMobySTe4Wb0w1M2swK4Kbn0R-pD1MRFyW0V3I206MMe9xfnR2U4JHsEOYRfcrdPHrpqiTsPkFMtTkqPYsQydUFyvXM4A0VKoHEsM4sZFQ9hByb9lkBNbrKdcwfzAmzUPGwO945K1LBt7_nXq_wAreCXgpRQ8Fc3oTyNIoEe9JdDRm7_oC881vcbx4s1WPKMmi7H4K70Mlr0S8pzxIr_C_Y1EKzZ5Q9qP898sL6p6Us-v2DLwoqzMK6RWYWAcUUMUhXLM3A4MbeF4yQWuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MvngD39KGyXCPuxOGrciB9fUJDRWJFA10-kDRcf63QXWQ19J_K5CKTzZ0oVbPp-QBGg3ksykSY1vNKU0SKF6D51QQ0qKgmBv6_ZLzC0HGjpaxaM5hOznOVYXMqmm8TEEfycJNRb4aygfb3M8cT0B-cZdSVo_YxYgGjU9_cF6L20Hg9EardStMwQ3Mz5aMNSXfy8uAmR6EqaXwjm4nMxH2Ga49V4i8RdadC4w7uDCMewa_RxGLjYAlvRXLhrLmmGsmyaYVj6jsipNq89CTvMpWje91L1Qio0bEr_iyf0fj_ws4bTuEc_o-65bqCDksp4jm5RahFL8e2BaXL7lhbLEdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GtBrLr74VY5cIReHLiH-lVA6MYaTx1p47whjASyTzRsZC29d6nbJRrVAgX6ibeuB4A1BNeJh0cctbJ5ZYjmbyoEpCfF8ebsNBWqWhlAmhcmOaRmyRL40045eVuCdg18_dlKeeWo49lc_57aSd__QGPeJc4DmX1wFGRtplpHVKhPXG2kJ2yX1ru1_oXOzH7SqKcPQrymPHjyJsiNhJygq2j91WDEKQSG903UmoDKX4s0yOnywJMP2SWq8JJeMTs3k9pDm3bLenGc8mLAruuUovxM5BAU_pSmSfLa0O7sKGhY0rO7R16kMXOyQ0ZmM-XihQck9fIpM537rr6_qwuqAKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5252" target="_blank">📅 12:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=BHFMuRWymgPecEQdLL9vbUc177joZpvg2fMc5szPePtDoq9ZsTi1eLUkWsdxeau9Rk5_8AneHdFtoRaPeRcIL_2le3NgkiIyL8_jiX4-iCJOZnpyHBWHE5bhWkPIRf3pA05flOWE07SZ7eIb3UQ2NbZBsomA1NV_v1tkOgHh2Euaoli8qiwgsFxHhybBaw1h7nxLteW44WbXzVbMjJtvqJ6-633sJbTdhL2F9A_Keuv09doa9qsYRcqsUVe21xgl61mtUGIo-CuHEcxb5etl0aCbTSEOnfnlldrCnO7AJ-PiZy6bGIa4BuHnGd-HCG_LgS9AXqzqpPioWH9dyYIi5DsXmE0dQ3HkMGzKv2r18lrU8XpDLtTeuVNmEmSbEOKaG-4EpN0uUuWH29_vSy0m_B8fpokS5bGizbVADswDTiQTHgFAAk6DWONs4Y-6CGgeKYzih-hJnnWeKI5f4qvxiBCzXMCUj2CxsXNRB0ljZdTktetGgNRBOXTmDAb-TTntSqWWbuYbbytigQHcXI0Ii3Ec5RVv9MgRG5iksrs0LaBEihDXDA5f5SpAOGDTD8wRIAb9VmZ8D2geGUN2OXuWo2eD_kW8XBD2vQtFh2d0A5kluR2ui6navLhU2fqQk5jx1h3uwPnGHSurn_yVE6FKb2mQorLWzgMRf1P02OU8z0Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=BHFMuRWymgPecEQdLL9vbUc177joZpvg2fMc5szPePtDoq9ZsTi1eLUkWsdxeau9Rk5_8AneHdFtoRaPeRcIL_2le3NgkiIyL8_jiX4-iCJOZnpyHBWHE5bhWkPIRf3pA05flOWE07SZ7eIb3UQ2NbZBsomA1NV_v1tkOgHh2Euaoli8qiwgsFxHhybBaw1h7nxLteW44WbXzVbMjJtvqJ6-633sJbTdhL2F9A_Keuv09doa9qsYRcqsUVe21xgl61mtUGIo-CuHEcxb5etl0aCbTSEOnfnlldrCnO7AJ-PiZy6bGIa4BuHnGd-HCG_LgS9AXqzqpPioWH9dyYIi5DsXmE0dQ3HkMGzKv2r18lrU8XpDLtTeuVNmEmSbEOKaG-4EpN0uUuWH29_vSy0m_B8fpokS5bGizbVADswDTiQTHgFAAk6DWONs4Y-6CGgeKYzih-hJnnWeKI5f4qvxiBCzXMCUj2CxsXNRB0ljZdTktetGgNRBOXTmDAb-TTntSqWWbuYbbytigQHcXI0Ii3Ec5RVv9MgRG5iksrs0LaBEihDXDA5f5SpAOGDTD8wRIAb9VmZ8D2geGUN2OXuWo2eD_kW8XBD2vQtFh2d0A5kluR2ui6navLhU2fqQk5jx1h3uwPnGHSurn_yVE6FKb2mQorLWzgMRf1P02OU8z0Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=Pdx1EcmFEY3sbOfwEBdUBTxtfuK0VbcIlWlaxzzjCNrPj7A57dffXUWGxGVnvuJOVGXrDSBoxVe3WOvMdcoT98A_rVSiWYmWg5VuTLmitwHJlCL9XHyL1vAW9cvtHwAQ1mA9kq3JFSdJwRFLU7Qs7n3rgE2J-mzS-oCeRPjkOyb1x8YBcQnyx33sCHWqhRxkW0i3nNRlomfRWhu1ep5ast58bT62l3yBLCuXFwJZNXnogiVSZ6J9aBD3kr33k9n9LSVUMLhYcJXGF7euxoW9dhQIO8QTuZt-aOkT1u45Pv55vhrlqzPliksjGqXDKbhkyhHocGvLAsQ5BXsu24QIJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=Pdx1EcmFEY3sbOfwEBdUBTxtfuK0VbcIlWlaxzzjCNrPj7A57dffXUWGxGVnvuJOVGXrDSBoxVe3WOvMdcoT98A_rVSiWYmWg5VuTLmitwHJlCL9XHyL1vAW9cvtHwAQ1mA9kq3JFSdJwRFLU7Qs7n3rgE2J-mzS-oCeRPjkOyb1x8YBcQnyx33sCHWqhRxkW0i3nNRlomfRWhu1ep5ast58bT62l3yBLCuXFwJZNXnogiVSZ6J9aBD3kr33k9n9LSVUMLhYcJXGF7euxoW9dhQIO8QTuZt-aOkT1u45Pv55vhrlqzPliksjGqXDKbhkyhHocGvLAsQ5BXsu24QIJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی
از فعل گذشته برای مجتبی خامنه‌ای
استفاده میکنه.
مجری : رهبر جدیدمون آیت الله آقا سید فلان!
حداد عادل :
ایشون از آقا سختگیرتر «
بود
» !</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5250" target="_blank">📅 12:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ea7JlKt6cvd6TLaFLvbEJ67An9PEz5QXLtMupzoLK_SmPAehq3jo9HYMS8Ef2bDiA1S6I73IQJIGqQ_pvruzl6c1OM71pm90_OZlzOa6cKLKrVu6OxsTZ4fV7M0S7r1Gp648l-AdI5ILUqkKSwMt2rGTpZblv-3LCCP9M64mdLWuc6UjLe6siJ7QEDOk_ojAXwqGObKXbQD_Ug3bgWlAWmkFfZg1PBWRFy10iukrXLm_l1X2haJeW4wJDtvF1vC5hO6txAlKv1Fo8BEHfgSRnDNFGge1ja7DH_rVD7Xe61prTUULLdBd1_N8hXtdZCNocqwEG6XfeMbQvpMFcNXRww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5249" target="_blank">📅 01:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">قالیباف در گفتگو با نبیه بری (چهره شاخص شیعه لبنان و رئیس پارلمان):
«جان ما و شما یکی است و پیوند ج.ا و لبنان ناگسستنی است.
در دو روز گذشته، ما به طور جدی توقف حملات اسرائیل را دنبال کرده‌ایم. اگر جنایات ادامه یابد، نه تنها روند مذاکرات را متوقف خواهیم کرد، بلکه در مقابل اسرائیل نیز خواهیم ایستاد.
ما مصمم به برقراری آتش‌بس در سراسر لبنان، به ویژه در جنوب این کشور هستیم.
اگر توافقی برای پایان جنگ بین ج.ا و آمریکا حاصل شود، شامل توقف حملات در همه جبهه‌ها، به ویژه لبنان، خواهد بود.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5248" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
به رغم گزارش و خبر ترامپ : حزب‌الله لبنان چند راکت به شمال اسرائیل شلیک کرد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5247" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5246" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5245" target="_blank">📅 21:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOtOBrMycpXFmQioRwp7RJRtZJI0r8kViafEbG_EHEViDzSm4dVSWZh6MJmMaYTbvFcu1l8FQR_Y5WL1CHtxaIyq5-CImOccS16rk18CETqJds7tM11NLBvNneRK1papdY2FPyIeH3RtGoNT6X3XVw-B2G-P-K5IFHyuwhseBrBzCjGL9qrt_RmPZQ9oADd5h-odB0xVutYvsdG2IdDJqg_v1oOjWJHhFRHhzpTOkicp0NNtweMo0Ucj1_LaFcfKOemFZDx1zXzQdbpShZAgr-r-2c7uKNGhdlfWQDvr9dQtTCEnMHJo7BZdGtTKwWcugeFA3mnLXvSOmLBz7Fqr0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه جمهوری اسلامی اسرائیل رو متهم میکنه به «نقض حاکمیت ملی لبنان»
یادآوری :
دولت لبنان سفیر جمهوری اسلامی
رو اخراج کرده و گفته مسبب این جنگ جمهوری اسلامی است اما سفیر ج‌ا
لبنان رو ترک نکرد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5244" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5243" target="_blank">📅 21:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eh6zRhEpiY9z6icpxMNDsoT3oeJAnQ2eLe4b6MzkwlU_UsWDjMGtyiYNYGT7LNDEnUBdVkkIqa3jOvbd-77G0P0iVZ1MCkJCLsj-App-XIrAssru2AQ0RKLY1pujXTqSMNwNDIel7-YwKFfll4cFiNfKIR1Yu_65AznDzBB3b8T44ZgXhfTI-VYhUQnaoIhsv2zQaedx15jfxTcNCcZ9rC-rsDb-Bfo1IQIO8oJ5cC31S_Coe6NYJxvrUmMPNOpXTlEhQPrvNXlW98PYw7xJO4mk_A2UlWJ2bsw18FJZ0JQ2sqCkRkeCoKS3vFmxjgTybGx4JEfAtQnR9NsVqU4TUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjdZH1nY3OUH8az0BXEzihM2o0TxJdOWjqB91ZkCHZbDiZaTxaWsS8oVgkJPygvSH9l5PapEDerBtrF3QvwcfmlPoCEIl7BKtq_NPGOD_ma8ketEr4cj_GJMiP_OV5X-oEkjrE_hnXmpuf9OPaAcEx_6rtsUEHSHRRXhjM378ALKYU2JRLPU2c1l2uCeWSISHjTzuj0IVM6ITghWacR08s_ZAmnfTGEWxexP9IZYCLnqbaPmav4qJJ0EcQr8b5ENlZkbFV3SX64iXw4LdJ6FoHLz6nCWtKur0p3V3rfmS7iwB7hekL54o0e8rnHldjcY0cRY0RkKGBdL2j9E47GAnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dy02754OPL5IhelY1ToejvUMLMP2_vtjweX0HQngoJexbKed6Bs4IN0wRdN3kHoqh1tllTGDSfzIzWcVCBQMpGVo1Xm1skDylv9kboSQYbaSwUR2bp6DG2eKlV21I_rM7NEAukrsmttNUuUmebwrJ-Kd0bGNRxBucm0Oyx8r349ftBt67FDjf1Fhn8DVeN0wgQGuxzY54H6B3Q034OqkGd6YuyoI05fD7sxLteAkd8XZeF1bUoueBlxH9-fQuKRxlBNEd_dYHvvipg6UZYJOYuoaAwqYmhzK0tT6C5WVspfwVAizT036GmB6aZ9GH2FSf3I1xPxClxcTsLv5FObolg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه خب ! اینها «وطن پرست» هستند
دغدغه‌شون «جمهوری اسلامی» نیست!
حفظ «ایرانه» و بحث «وطنه»!
فقط اولویت نخستشون
گروه تروریستی حزب‌الله لبنانه!
و توی مصاحبه‌هاشون هم میگن حاضریم ایران به خاطر حزب‌الله موشک بخوره!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5240" target="_blank">📅 20:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5239" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8muuGtBoedn5TD8kpCXV6Bc6omvPIuuNxk-MdZU14aJpq1JbNQ-0Nq0f6phCThQZwiuVFXvJ1oUFVcxytnHySrUHQ-TEEzdIJtQ79zgexIyY_YJYcy_ZDQhTVZj67agJuBkBnCjSPN51seWnIod9sgji5_A4Mra_eSMKE63-_iSgNjAzdrPfdl_L7VYx2axrd1h-mF4kJU2EwMrNrCavmlhDGQ5jaiT5Dwd8kujTJM3iWz-Dr-ck2rUHdu94zQC9FacQ17TBGa3t82_tcr5KJWCuL7NlpRkVCopCG7u8QJyfPFLrlUHbAlO6LgDv4RDMUlmDVLM6t6pmbeR5nYByQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتابهای اسلامی برای کودکان
(در مصر و تونس و….)</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5238" target="_blank">📅 17:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">این دو سال رو یک مدلی با ترامپ راه بیاییم و بعدش بزنیم زیر قرارداد!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5237" target="_blank">📅 15:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRL2E_qcZUicLVSKp-7K7WbTicH7R5S7uvZ4B4NkT8Lxgozq7gwY9FGhe7lk_ZaCYfzvYBqvnvrmBNJ4EPJ2y0BfTHTyurtOb2zAmARct3yujTcWpYL8xK726P_vFdEgcIvv7qHgRWcS0ILHOBrSTI0RudPIaaC4nmR7hBNd_Yi-ePqN9jAQefB2A_k5fb43WRCNbvJeLIbeN8d7MSvkGKEHcRtuKvzhzqdH5hJJ99MoRWGRC2MPvBQQLrXkF2YWVbsVdVpo0HT18AewxI7xhQ1d0dB-QqWjnLgphy9-ckO3zJY0mOEv2GMM1E7_Kbxg6wN_23M_5dLQxAnHLyNcTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cIE9HLwHCi9d-jddgnPKAgYqXGcmS8pg4esqpmh7vmmL0kIaaLQOkrojrrWZIiB_W026d6z0FjXIEv1SiyMa52gHfemHa3OeNTnjJEsQJz-RUJd2QUcUQANLr4jVt88GfjJ7zCzmnxKF7a36LGbiO_Gp9W9Ht7bKe8NalESnsdSsA_c6hNf8m4h9WJ6WAFQDp6uoVjZYuW8bGx9r0GY-xTaZP8OL_l3IB5VRxwR9HPE3gSSq1bp0uYhiUz61memZr_IHszr6zc2aIVQ37KjWQduJt5CgHXg0xXpWnjS0nyXh7TY_aI7iv3mOLOXTSraORXxYDIYcdyiwtFHaZa65bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WbxdD3GKLnIIn_fW0IUzjwa8GmuRg-9S7w-1vIqPhZUhLQEg_q93jXXeGrQ3XrLPz4oufH0mqIwvCkRlfanGspUtI9lWDpSSo8fqlVoMSGFUkFiuiZ5JQ1cfhN1XnPa-F80X4MEuCtwo2CIyQUSuq0J_FNrZxL3ZaDlX5K5_pIFEUUWAriTcrsNY-sFho4UFF4NPeLr0dPfH_QZTAG4e_uOqU6cFn4Lhb2kRqlfNKVjA4Jfhlq6db1Tv8rHq1b8ZNLtn972pzA0Fe3HeuXEYJAM05ElGrGNFv1NA0Usb1O2zncVFGTbaVZVgDU2bn1GF_6M_oCq61Zmj4KHi8B5DHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=HIcJUrGExxPpBI1LxO0eCIrOa9OC_VQ-lTUhmuyHJjG5gNlj53h-d_IFWIQCYspfbJz61YpqFEtY7qFGTbmioErf0srF97DQdLY1WYW1lsmhFDtAIM2EB5miOMolTkGI14lNDSaDnp20j5NURUlxZ84Ff_5Lw2ycT9bEL7op87uomI_nsW5QkqPv7BZju7cFh4EKJPBlBh5wfj5w3VrUjpQbpMox0u32SjjRhffMwU8LYXIWXDjDeecKSvMfLubVcoUiFRmSgrPXQQo0eqT-HokDq63uy8-V5oRVtEPmmUVS4If_-PLrt56bwKE-tWxHiQoyKUdneU2xDTIy7Sppnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=HIcJUrGExxPpBI1LxO0eCIrOa9OC_VQ-lTUhmuyHJjG5gNlj53h-d_IFWIQCYspfbJz61YpqFEtY7qFGTbmioErf0srF97DQdLY1WYW1lsmhFDtAIM2EB5miOMolTkGI14lNDSaDnp20j5NURUlxZ84Ff_5Lw2ycT9bEL7op87uomI_nsW5QkqPv7BZju7cFh4EKJPBlBh5wfj5w3VrUjpQbpMox0u32SjjRhffMwU8LYXIWXDjDeecKSvMfLubVcoUiFRmSgrPXQQo0eqT-HokDq63uy8-V5oRVtEPmmUVS4If_-PLrt56bwKE-tWxHiQoyKUdneU2xDTIy7Sppnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال «پاریسن ژرمن» قهرمان شد و پاریس و فرانسه رو به آتش کشیدن
قیافه‌هاشون که تابلوئه!
توی یکی از ویدئوها شعار الله اکبر هم‌ میدن!!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5232" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.
پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5231" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9_z-YJEtfeQUA3l--BBErDntrVmj_sc9TADUs4_gxUnHr3FviQBv2j14v-6dfAE7g7b0doNgBlDBsLaazK9x-U_Oul5xNIiidH1vzCFGgsOwYcL4W4fsYOS_hMpVApKCxUtaKpxBUut0-OJsLWhwvzuB7xN8nuIDqzIZwwgG5HMfroCUYuIndWHMur1E2HvhZIpiqYav2uw8gtS7sEu8m5pKltP4N4eGKP6JmR44u3fvnbBWSAAEkCtjp6b7QWydgoli5w2ADRmG1f68gM7Wbc9hlbz5R9QCScPCc60-B0YSTEna7KL9PRnnH0F97N5R0YuUR9_wIgve9rxfoqMOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش آمریکا رسما اعلام کرده
که چند حمله در دو روز اخیر به قشم
و گورک در نزدیکی تنگه هرمز انجام داده!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5230" target="_blank">📅 11:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=GZlQrTwJl-tJUh0hcC-nKQUIES2uC959TKfQ5eNiCW7-QaZ_ybW6366AxJqUgFdoBhg4LPc0EvXIerURhVCda4jIhUOG-OVnfB5se7mog5WHtr6GUXWYw0fk1y1eV_S7kYrCTUUoHotgoCtKOOIom5j9HdQ21yPgSpOR81EA8zVBc5XCh3THtxlfbXiyBFch0Swsl5uiC1Q5WH7kMvc9y7jH27YsDU2h_upTyJCEn8aBnqmbzPTrlAO-r-gGluAE7qRnjA9uEIlQwlArociuu67aPh6zACH4g9_oJNOsjRqi-mSwUs9wDklufXJ6d9riGRk5BkJlbROnAextLq-ADA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=GZlQrTwJl-tJUh0hcC-nKQUIES2uC959TKfQ5eNiCW7-QaZ_ybW6366AxJqUgFdoBhg4LPc0EvXIerURhVCda4jIhUOG-OVnfB5se7mog5WHtr6GUXWYw0fk1y1eV_S7kYrCTUUoHotgoCtKOOIom5j9HdQ21yPgSpOR81EA8zVBc5XCh3THtxlfbXiyBFch0Swsl5uiC1Q5WH7kMvc9y7jH27YsDU2h_upTyJCEn8aBnqmbzPTrlAO-r-gGluAE7qRnjA9uEIlQwlArociuu67aPh6zACH4g9_oJNOsjRqi-mSwUs9wDklufXJ6d9riGRk5BkJlbROnAextLq-ADA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=sLsCIlOks0Li4iALIuet_I6obimFNa1sleGcg8PRyVVcmJbKZ5dYpMItCEIyJ58bJ4yUOM066l81H7iJkXiuu-vhBZqAiOCQVcWJWZzj6ADHmwvirgTxqT0tGxDp10FJpC6PcU_tZXwtC1HZnymVW-HopgyY0g8fh2g-UMSX8362hRGBVIKxNiimC5pe-hfANZiWI4rs8iWFbH--sVeq5HEVDhctOM5i-iHlYchkUTND6HHmQpv2iVfGCcR5GlJlVQgbVR4RYbn8Pnk-Bwp9zt_sKzdru-YpZstne55iW5MSFAvqw1e8P6Q8tg_E6yBX_Lbe7I6CD2w9Ox5vkoo-Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=sLsCIlOks0Li4iALIuet_I6obimFNa1sleGcg8PRyVVcmJbKZ5dYpMItCEIyJ58bJ4yUOM066l81H7iJkXiuu-vhBZqAiOCQVcWJWZzj6ADHmwvirgTxqT0tGxDp10FJpC6PcU_tZXwtC1HZnymVW-HopgyY0g8fh2g-UMSX8362hRGBVIKxNiimC5pe-hfANZiWI4rs8iWFbH--sVeq5HEVDhctOM5i-iHlYchkUTND6HHmQpv2iVfGCcR5GlJlVQgbVR4RYbn8Pnk-Bwp9zt_sKzdru-YpZstne55iW5MSFAvqw1e8P6Q8tg_E6yBX_Lbe7I6CD2w9Ox5vkoo-Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما  از دولت لبنان خواسته بودن  که برای آتش‌بس، مذاکره نکنه و…..! به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره (که بعد بگن دیدید،…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5228" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnlwHwWkt92H-I1ufw5OExJnwFKO7RFLuyyQdIgXFmz9j7XDkoSgglXgOi4aFrop3fffvnRJmisJumnBXIbIYb1qY185RkKxvuSIWaBXQt0DLRbXMtkuamtIBQKpYSLkdh9qe6Z7emPBfk5vBrCr2658A7wNy75uRr8G5ByxKKsluze5Mfr7-za8VoJc6f_mfG48MuHn142pB6_38WayqZNniEduBET2oK4Zf0RHdPFiGia69Yr4q9Yj1DCnXOQoMVP5Edg-p6rz1gPgMUNZwQAsBJUX3i3DSaL5XZZLO45ZOR2qcWRdLzG5NwMto52LiWAPnxJmLIQVF_axmAQ0cQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.  به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.، مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!  یا شهر‌ نجف!  برخی…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5226" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=aDjgrCdOMxQDRcN0RGkoLxrjRNwm51kFCgUKVsB6krSSnmr0cEwE_RP3Wy7KtXeVJYfQQ6a9EpkCVQ3cqT-vmTqq49e21fe9Or_xDIltusDvSjLSP9b_jqcxdrTtNBSjMANhRv-Acphsk9XM4FP52dJ9gfCkgirm9g4JmULFZ3XZ0fttAvMK65lmYoGOtI6mQSzaLTfhGBwdv1v3ZHiGhFWoZuyluzYoHZDaGH0sUL5PMuDHdfL9hEq-AepEym2uyRimcNWe8mZ_wCYdDHE3Z0knIR6po1afKtEmStgXUnnXmKbovTAibKGkFgegPSrCFg-Vvgutl0gOpZ6_yqJ7Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=aDjgrCdOMxQDRcN0RGkoLxrjRNwm51kFCgUKVsB6krSSnmr0cEwE_RP3Wy7KtXeVJYfQQ6a9EpkCVQ3cqT-vmTqq49e21fe9Or_xDIltusDvSjLSP9b_jqcxdrTtNBSjMANhRv-Acphsk9XM4FP52dJ9gfCkgirm9g4JmULFZ3XZ0fttAvMK65lmYoGOtI6mQSzaLTfhGBwdv1v3ZHiGhFWoZuyluzYoHZDaGH0sUL5PMuDHdfL9hEq-AepEym2uyRimcNWe8mZ_wCYdDHE3Z0knIR6po1afKtEmStgXUnnXmKbovTAibKGkFgegPSrCFg-Vvgutl0gOpZ6_yqJ7Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5225" target="_blank">📅 10:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pu8F1sF8gIaajx7-Am66zTCfZo4c7RoCvzjoEjn4wfDecACxpQFD-xOooC_6qDrOIfqnWU4JCtZFjHGbq1M-vffUbgyc6hO46QkkSpZk3QDRmPhz_xw6uNHebc4rxiZ_vrozIsggFB9FvwvRz2bgsB8ioDcnqTTHVTvek2BMizP7QsU0fTDli_CQDQo66dYWH7S5xDZVT9GgJnvhEE9bSsCnrluAdC1kEGJixaAfH3KV-6Ncni2UwkS5xMvXbLUEVwy31AvtcSTf0VX5f8wt0yxr2az22Hb-8cTSlFSAqNO97Fre5RmqWdwOf64xKpcuqgBia9autt_rahSPCB2I5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطور تریتا پارسی در آمریکا
متوجه یک «طرح پنهانی» برخی نهادهای امنیتی در تهران شده؟!
معلومه یا این طرح رو خودش داده
یا با این نهادهای امنیتی رابطه داره!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5224" target="_blank">📅 02:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
مایک والتز سفیر آمریکا در سازمان ملل : جمهوری اسلامی با حمله به کشورهای عرب همسایه‌اش اشتباه بزرگی مرتکب شد و تاوان آن را خواهد پرداخت.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5223" target="_blank">📅 00:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fE26PIS0ptYa5HtrBHBpKVthhIPTzbPeCeXWSOE0gV8IghzXdsZDyy1YwXHgPKZTtIpsO9B1ukGsPMmKSuSiUtgn8TinoSN3UkPljTmQ5xwsryEkCQI_UGZ_lNFORsN3n_gz0Dlh2ODiSe86rncZoGdEapk402xYMKD1WrjI8ngGjbjwtr37Q1srKTHhPtPD0GdZ5Kf4pFLUO3ylCUgykZHDUe6t4dp0F5gzx8pebAcbqZEz1dOhE_IEnHaJ4vuUcBbPElIvg56QKdAKY-hq0ORMv35UXrQKC6Ski_ErVBzCmh3kFg7m0BOuYNXczj1-hydkenubNEWlAaKzAIdg-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌های ضد و‌ نقیض از استعفای پزشکیان از ریاست جمهوری</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5222" target="_blank">📅 00:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oecvDU00KuX47KWEaYDVPqi6q8lzk_Aqrzi-3tSEibU9U2voR0D1D1wSbkrjGTvlf-hlm-wW9CwsMS_nmmo7c9x7J5SkRNCuPUixMZX-7RxUu7ajpAOj2rtv3EwmMd6yuoA8id0eaZkTl456dClnYU1XJRJD3x7rdjpMWcHd0-X0MjaSG_gxOiNBuvbDisTu5dvJvHYcLBZeVcYfHnb4B7wDRS6c-5MTEc8lMvPXASnQkFj5KmLEDwcNluCcxuvxdQreCmhw3IualXZhI1K0wbQPfT97YleYOyz40LCYWxk7uqMvgrGAgv2NUopuRwmRYJs5ZeXXDsToHmINrTCfcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EjkvpcOgHmYblktk7tnQIVKdHHsZzx5OaGl-zGHU6vqPjtmng4nWxOAee5YdTzU8ezLcQ8RIHu_tzPxjMeKAai3OaLBKQG1RFwQhBESxUtvLRZaV-Q5j86HN3Etd2n2gd3FfBfQDrIDYvOUUb_rt7zKgsRVzditahuxgrPgniDaafkiJqkDIIAkI4tB4m6H3qv05-bxj9YHkj6ZlMozYcHTFQbGHJyxIZfmhyM5_GMYbIElbtImGO70IiQ8PO3-Gd-16XFR59PgGWnq05ExfLcOwQFE5fwkUYpvpHFMOLJ5QpvRqdtKhJ3Zv9Qb5s0GsUcpbOkY6sqRwApGAnVN9Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AEYpZqk3e9C15dB_Yvhjn64XqW6f3XvC4n8-qHHYsxgsUhyvdE_7qcZ9dIbGP3RkaXNuTkrU4kpHloGhXBTQx9RqghfttXU0eNaaUM0jgd01VLbugKWah1BHxbsMsz8j96KFHFLNgJmv5lbTtbCut0RfTn3bK64cVzyKpBla3ZqfMV-X8nY-vO3L0TGkH1JRd1of_W06RlnN5NYK-T0f11pgsS4RK-na4CIYgNtUbnb5P8XTJ4feANNHHNwUVpoOO_xvC2K6eI5ezLg1lTZm8R9j_-634M0kLR4T4HbPCbinufs5pJmNa55G-fwClrJivnPo3r-7GmVLPJ_vuCSadg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتون رفته میخواستید برید
پشت سر خامنه‌ای در قدس نماز بخونید؟
که شما تاریخ خوندید نه؟
تاریخ جمال عبدالناصر و صدام و قذافی و بشار اسد رو لابد خونده بودید
که همین هوس‌ها رو داشتن!!!
و به همین نتایج هم رسیدن!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5219" target="_blank">📅 18:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5216">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E0cFGljLjVyTwM6BnSMNc4N3a037Rwab7gxvU1HD6IEWmpUaFeR2pl4CCul0hhPa_T2Bx6rc9L98jVQXPoYWsdAWpKrntVc1LttxJciZwLPdkZt_sJG8lieoQFpfI2zptoDGx3uvEBamw23PwDts-aJcMSymG6Zdy5IfcG0r4VZlOIadocqwldYv4PMxJuVd2D5jNszRIWv3SQM85oQdsHnizWqcGYJsTtijlWEdk0w-KgV57LdGQklRbq1fYUlQgIkHHRQhZeelYSzeb3QDcodiJ_thWPZQ7KOl92YVqQj7CynJU9HjPF0CXnM3nLEQ3DRt_vvwvaxjX5xlFOA_sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G9iBBCS1Rx4crnXn5ENcLCKepMl3fqE-usgMiDxEdt0kL1OOjb945M3zWD69azZII-5lCDmfCNulMIq9bRzOx8hzfFgvrp16BCI52LAZDhgNUYx6aZAdzynipvOf-VJI3JEs38lhNVItZTXC8yqCGcSKorwt3fXo6elsoH1CywgPTEyXtnZ5qX_Zif4NfRpjygy0HytCHDCt47ftnwYMESQnlnW3fTvesBlp-B3DULIA088deMpGAnC9kbZLzQsc5VPQI4eiK_L_cETLRd9kqVtNmvjCAE8LA6IlW8FxcLJySIBzCNBn12lGswuq0YtxP1TeUUGmAxQKhaDoKlAw2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LwzpSH__1PzZ9tdARTFrMSFBo7e4NVmXmlyHaz_mCWJj4w1GXkUgdROKY83RohQRmF9-5g0wGmY3i9_4cVgpqNP_CS4483iy3DJUHscYEJHPF_kU5DURlbqEXXoHY1zyHzGw96k-pqUNgY7tWBOjJwOwAU0t2huMeN4qQo6ZSiKkLwyz6jf8b7wkNOMLQwtmVcMGngkLQTnkjxWqEmOPjlZCjHgVpHvFsxkAMzp7l92212T0XuNVN86rFzYtbIzv1HnFFKNIw8jdqczXprDvqc0cbh9JzuL2CGVlcbMfnwZXuxrd8gkWqp8xW5tlFqPHfYapfNJELL-HPCUK6DGMmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفسنجانی سالها پیش گفت من به خامنه‌ای گفتم پاسخ این همه ضررها در دشمنی با آمریکا رو شما به عهده میگیرید ؟؟ خامنه‌ای گفت بله! جواب خدا با من!!!  و خب این جنگ‌ها و تحریم‌ها و آسیب‌ها و کودکان میناب و... همه همون مسائلی است که خامنه‌ای گفته جواب خدا با من! یعنی…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5216" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db68225cef.mp4?token=I-dX7rfUVIghDOJ7itoQuS1742dQYogcjiGy1_vGI5unqeFK5WwWINHAlo-3AMwDibIGz5YM3P2YnnIxwkAgS0rD9EhjOi7TJ5-0ruG_FOBsuc1QqpzAFTiA4AaXza5uPlsG8_izHY_p6x-VymtUSP0UfmhBbPcOHZVCfGOa3TCEV-uBzohOZzYCBLHJOw5Mas-SajLAF9yUnU8pU6C4z2ZwXuJcDJ2Tr2Dg5OqsOASzxpBXwWt-gyYR-mIiLrrDf8wxBjvFIJjT1p0Bk3twCh1Cu16qDxO27ZXobvKcIDBFncUl1fnGAqU-ZV7V0A93VHXkI6hLXpHgnN0T1baWbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db68225cef.mp4?token=I-dX7rfUVIghDOJ7itoQuS1742dQYogcjiGy1_vGI5unqeFK5WwWINHAlo-3AMwDibIGz5YM3P2YnnIxwkAgS0rD9EhjOi7TJ5-0ruG_FOBsuc1QqpzAFTiA4AaXza5uPlsG8_izHY_p6x-VymtUSP0UfmhBbPcOHZVCfGOa3TCEV-uBzohOZzYCBLHJOw5Mas-SajLAF9yUnU8pU6C4z2ZwXuJcDJ2Tr2Dg5OqsOASzxpBXwWt-gyYR-mIiLrrDf8wxBjvFIJjT1p0Bk3twCh1Cu16qDxO27ZXobvKcIDBFncUl1fnGAqU-ZV7V0A93VHXkI6hLXpHgnN0T1baWbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴ در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته «دو گزینه بیشتر نیست» یا جنگ و خونریزی یا مذاکره مستقیم «برای از بین بردن غنی‌سازی و موشکی»  این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5215" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=nuAJFgla8MZmcvRZVmRnyr3B3l57Iq1q-WP41dDxGMDkBNDk_J_j1XctHvVeP6GV460TKbKq_m1wkmOTPGWnS2R4EU7XU9jknMQ5gN3ZXsgMa3zWvM60u78KYWIfkBgBi0NYU9CDKKTDWR9cISj6ktEj72QeIOOW88XXD903OfYzzcpk4CQjwSihFyDvtyRcq-vS9uBaEeQcPAJNBsFGcfSwaChRaci2MMKAzk1zzQPbGI-ODYsiRPgNWPMZ03DLw3sz51xb_aakTtcIQg--lzHPtzVZaia7bEx5o_zkPRF9zScfKzluZHL9XYEqlPvw4puEE3JpDx6RjRle0wiz2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=nuAJFgla8MZmcvRZVmRnyr3B3l57Iq1q-WP41dDxGMDkBNDk_J_j1XctHvVeP6GV460TKbKq_m1wkmOTPGWnS2R4EU7XU9jknMQ5gN3ZXsgMa3zWvM60u78KYWIfkBgBi0NYU9CDKKTDWR9cISj6ktEj72QeIOOW88XXD903OfYzzcpk4CQjwSihFyDvtyRcq-vS9uBaEeQcPAJNBsFGcfSwaChRaci2MMKAzk1zzQPbGI-ODYsiRPgNWPMZ03DLw3sz51xb_aakTtcIQg--lzHPtzVZaia7bEx5o_zkPRF9zScfKzluZHL9XYEqlPvw4puEE3JpDx6RjRle0wiz2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌نشستن و  با نخوت وعده «دردسرها»  میدادن برای آمریکا و دنیا!  «حالا حالا دردسرها» خواهیم داشت!  بعد که جنگ شد تقصیر مردم ایرانه که تاریخ نخوندن!!!  تقصیر تلویزیون اینترنشناله!</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/farahmand_alipour/5214" target="_blank">📅 17:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=BOyZwJBnGI7F7kQhTzHKtAK_brJ2wq6vNal8q2neJNPk2p1XBHpLbCzZPWzT7IcpNzg0jzwcJ8qiEw_WgxlrxPQF9Xi4qtZ9N_mv2ESjQpN8wMgVTDh644RS_FRbrekf_uBa-aa5L0VP6YPZ9Jpigk-v2QW0elL-E7-SnbmE9rLhnwOpqMtLKWjxJnRaRsR54VkWHbR8hU0XMXlMpGhx5IHR7BFdkVwFrdg5GjnBUIwgxXoClSp9iMHhvHEkZ0L3MeS8muXTYY2mKv2NQwATy9xSPM5IDSg8E1PKB4gtabHCBhDP99XD9Sf4WBe5edpbNmRzDbnfnn9CBSeUViKCeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=BOyZwJBnGI7F7kQhTzHKtAK_brJ2wq6vNal8q2neJNPk2p1XBHpLbCzZPWzT7IcpNzg0jzwcJ8qiEw_WgxlrxPQF9Xi4qtZ9N_mv2ESjQpN8wMgVTDh644RS_FRbrekf_uBa-aa5L0VP6YPZ9Jpigk-v2QW0elL-E7-SnbmE9rLhnwOpqMtLKWjxJnRaRsR54VkWHbR8hU0XMXlMpGhx5IHR7BFdkVwFrdg5GjnBUIwgxXoClSp9iMHhvHEkZ0L3MeS8muXTYY2mKv2NQwATy9xSPM5IDSg8E1PKB4gtabHCBhDP99XD9Sf4WBe5edpbNmRzDbnfnn9CBSeUViKCeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی! جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!  فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ، بی ایراد هستن…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5213" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndh_HHPzG0M-sHxuPN763xu1IhPIOTJKE6W1TF1Ux7K6h8cUApSVBggzChQLDGVKdnycv_TxoA7TFx4m0EfcswdSyk7zONHCQ6gQDxS53Db7iEFJBuUu_4E-F3-KwQac330zVx6BB7bGA9Lt2MmlH6enoTV777sOzqoYHbPRj6FZTaJfk3QQwUaxy_0K7xnbLNPGYpWWR3cHJWGR0YBOIzwGi_WjMmui5PS6lYHsuye99wRh6h-VgXDnrZ2mz_EWEi22AjpoKNIUcyTqvnpvbLMjrvBWS8kMF8J-6710rJklKHuASxZccEfJYIbiQtCVq1UI0HFQOqnX7qyR2ptxtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccOOxi_XpwVRDbeewbj-EzNuXf8Qi7Z6hVD87zz4qks3MIj8kU6kyaeNnH1E07nKvJRF3Wh6Hxt3N4tMEO4xdrnKsK2KCDxpcWCTu54gTKb3gVk44LtUyh5-Dna1-5qd0Sru8VoeK0lpgT6FCSC95vP0HRcVtTncKk8Vj23V0VjdJeKnN55UnkdhFQoZ_rpFiyFK2NO21xcoS-zVTPovsv1lRa3iOLgVlri9sYkeJc-JB7E2tWGBmMcn3GwoOxHwJk95SCJNz-j7rGz26db5TswzZrD7WIoLNXO_vbSF9USuL15EPU0UJTVaXYtGr0KcX3M0p54ZD7Ir-5dfi5_8Yg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5211" target="_blank">📅 17:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzIs1sB9FbP1BmOncLp1F5W4DgKQyT6M5uCKooFNC1HDQA1ilVGfGyAnsvlM7Fe8wUsmPJC_VROAngtGtAOeFLKaElYziGEr5jY6PphNGpdkODCojS8HyFlIa8HTg2InABG2nzAJQUGNyZEdxgFxVUa8sKif0o8QP0FPcoxn2lIoIl9F2SVbgujCRNqiD1QRwF7avovLafSKWD_rbZxcZtdGOl7pRbHjj1ibqCODXuzb2wcja-EbyKgD4ZmSoSXgapbjyJ13K9kXQ3sDvgkbSs-hiIqH8rC_zum4f8TBeuOe6xkQm0B3fNObP7cYN2CDWICfsDKA483RrpFLIlmlsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5210" target="_blank">📅 15:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omfmW4Jhnc9QU8Dm3V4dFriRHvAqtSijw-junkcuDPGULyW6ku3M_VhVuvXHah4tO7AduQT5Hjt8zPf1A1zCX9zOHOujfImbQz_znbmiJtJcfVAjT2_i5PH_V2qbY0pAEQAh7BzC_0vzwEYCw41WaKkQxk_oCEpVPqGrCvat-VpFYSAwpEBBAgvam4N3GXblbv9okBXqbDXR5ZvaC3C3jwXe1LJiPhmzSlkjxkVYMei1PsxPCQAXVG9Xjw7rnjJeR0gZ6HQoafGZ1qCkUzkFHTQG16Dxdd4x0vHL8_9UztDdvZQyIYW5kUeo45rLHUdN8fET0j_RVl_wEGv_B8AtLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=OvobVt2ZT6v359JJhjRAzQluiyI2pSMFCrTNdcimCX4KNAekAeVuRejxM8J9-cCDysdkcOEWA51etKTgjqvl49HUimoF7tc2kcSMPnBC-OTJPyoOoEaVne8ZHKQuFBM4yF1IUOHsgLgHdvqUkr-v-RWNMRW-3Dhv2A6JVHVfdrlei4VadyBl66TAkXj1Hy2RTzZDRC77tFR1KD8va1VcAm4FN-AZCrG8K52aFt7_wcVyRU-TGwn8uUwy8srDgXtlGuKKUgdw1530ptMaxK3oOiiTMXmVXItKJqFYyWrWwyuUFhTeJL2JudI9EILXXFbbq4SF5BH34y-_uECnYkfBGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=OvobVt2ZT6v359JJhjRAzQluiyI2pSMFCrTNdcimCX4KNAekAeVuRejxM8J9-cCDysdkcOEWA51etKTgjqvl49HUimoF7tc2kcSMPnBC-OTJPyoOoEaVne8ZHKQuFBM4yF1IUOHsgLgHdvqUkr-v-RWNMRW-3Dhv2A6JVHVfdrlei4VadyBl66TAkXj1Hy2RTzZDRC77tFR1KD8va1VcAm4FN-AZCrG8K52aFt7_wcVyRU-TGwn8uUwy8srDgXtlGuKKUgdw1530ptMaxK3oOiiTMXmVXItKJqFYyWrWwyuUFhTeJL2JudI9EILXXFbbq4SF5BH34y-_uECnYkfBGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، ۱۸ دی در جریان اعتراضات شهر قدس بازداشت و پس از ۶۰ روز پیکرش تحویل خانواده داده شد.
امیرمحمد ۱۸ دی‌ در اعتراضات ناپدید شد. خانواده‌اش به بیمارستان‌ها، سردخانه‌ها و پزشکی قانونی مراجعه کردند، اما هیچ اثری از او نیافتنند.
پس از دو روز و در ۲۰ دی، تلفن همراهش روشن شد و ماموران حکومتی از این طریق به خانواده اعلام کردند که امیرمحمد زنده است.
خانواده پس از این خبر، پیگیری‌های بیشتری در دادگستری انجام دادند و آنجا نیز به آنها اطمینان داده شد که پسرشان زنده است و حتی برایش حکم صادر شده است.
امیرمحمد دانش‌آموز مقطع هشتم بود و خانواده تلاش کرد از طریق آموزش و پرورش نیز این موضوع را پیگیری کند، اما در آنجا نیز با پاسخ‌هایی مبهم و با برچسب «پرونده محرمانه» روبه‌رو شد.
این بلاتکلیفی و بی‌خبری تا ۶۰ روز ادامه داشت؛ تا اینکه در نهایت پزشکی قانونی با خانواده تماس گرفت و اعلام کرد پیکر امیرمحمد شناسایی شده است.
پیکر این نوجوان با کد «ناشناس ۱۱۷۵۴» به خانواده تحویل داده شد.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5208" target="_blank">📅 10:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=Zh6h5RMQ6IUdyj3WCJQwM8kRcf53BAHAajB--o3EBBKx_eia-7uUfyDMUVPpnop2NbNMAPdORKEkje3kI5cbCRPXuWI6eK0GRBeNkavOxtu3ISaxggSvAfmiqLkmY90R0uU-m3b5iFYlVBSS94-S6qqXK5hOA76-Fb_e_NSZx3lwoYKkBIQlErfj5zm2GLmNBkLvvCg7ao6z9beXjisERgPTZUHZcafLxz1mL0WBfe8YSTP7dAFdDQjSnIe9I1YeQVIo9iED6OdkNziISOF6CvS4gna0MkNqJSWC1OuwlbicENcSkknBP3iNeoH7SLbEgkUAG3a4IGKadiWkBIHbgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=Zh6h5RMQ6IUdyj3WCJQwM8kRcf53BAHAajB--o3EBBKx_eia-7uUfyDMUVPpnop2NbNMAPdORKEkje3kI5cbCRPXuWI6eK0GRBeNkavOxtu3ISaxggSvAfmiqLkmY90R0uU-m3b5iFYlVBSS94-S6qqXK5hOA76-Fb_e_NSZx3lwoYKkBIQlErfj5zm2GLmNBkLvvCg7ao6z9beXjisERgPTZUHZcafLxz1mL0WBfe8YSTP7dAFdDQjSnIe9I1YeQVIo9iED6OdkNziISOF6CvS4gna0MkNqJSWC1OuwlbicENcSkknBP3iNeoH7SLbEgkUAG3a4IGKadiWkBIHbgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0ojAvszJPAgZCFPV59yVO59eNwqU_HdXHl4HPOKV6TtYkTyFBwZAprCoPPJusDNwx6EXznCusBYYr2qGDU5Bx_ZTG1e1I3vsC024BNCAEZCzbNOeMeeVu7T6yF5dmPZ6x07v7Que6ahbM6DAguIJMi8ZTPbhrZot2H6HVdB_2_Qr71aSpZM0miF6SnCxcF04i5DEJMRZsGbBeqeVNiGmzBvop828l1-Bbod56HvL4K7nLnDQZWOv5WVHFDaaQfEKQhNpvja9JInSVoj8hWa77omtPUeLIPAgF018GuUupcu6A4QirJY4EAu7J2d38TzxCEGhaPwRzXjhs0s-xK1zA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6F-LugVpLXiosIhvwAB_Ytcj9o_8-uQn0kPQUwu2ZlSwwZCgOB2nL49ekrX7iBEl9TnRdhky5Y0emR7WcDxEP4xEY_L5DKd3OD4Tv8q6_GeFWeE2j4FGMFaT1jPiZhcoWsz1wN_018QVctJfutvfJYh2BahlYXRkLyb673JPtM1aXOumARE94tNFP2TmV4VxqzYc6VKLKA_d6RlB6dBf_a0gvcf8aw9YGqXVU1DPfJxz5cXygR8vqquOrFdnOZVeUaTQjWqRxsEOTvPvogk1BeunpNVlPcp37CwpvA9cWoI08uOdjKGPJgL2B6Y1cCsePZUb7Skmet-ehyQsGOknQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgL69XLsVYTZqGEnWzfxiiQsdxnf7lMnxnzDpiWOdN_8AAfNrpjyPc5INT3JtV3dBOA1qITJ3a6GTAHF7BJity2s7p3jSulRxWA2K3dphKsYPuJJiOT15esB0SIVvW2fJ17zJYRDgToUH0fvzYyp0_qbGgX9I10avcaie0m0F-5aIo-6EjKa-Btf5isQCwm-iMh8dP6mSzy5kGY-yAz4wauyfU-P5pxxoPCWtDT8Un5L4pR8rpxdevz7vBVcaHTaEJX56h94UQuNbR4p7Zy-DCZblTxTayhMvVIVzjDh9t1XoYuWqrUkrB7HmHJrmXV3AvCgfpIa96lqbFnVlwj-QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psEgrYGHeFplBwz8GuxzikiIl_UqIEZYPSqEdVLAWr0bhdUIjXJC6-TXNLfXUK4G9GfXUW3MtvS76TdJBJfbVplGoBOlS1xKXTkiSa4PlPsbHEZBXaAwiNQi6LB67-GKuNEWE4iDQsZXC9Gr1QO2SWkKBjstA1VKjV5ai_gkc5Z2OBBOPl-R4GiUYZU3U5lYMDJWLHICkDsapFUApc55jRGs1boRuqvcwlDKecXqiHMaBtUQfsTKXiq6UJfneQQ3zzjaBs74s-nGq0Am5VBTBukQVB7KYS_ivqA0LaqVMpzpYhBottPekw64-ZQrAo0yIZZC8UAs0tNGZSyduMTj6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی بهتر برای جنگ بعدی …</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5202" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5201" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BtMiU8ZF4MUBGayQ-uUPFrBONeb64xya-61vTEPAynNDgOwPtKLxMWeR2zb9h7vH8neSuXJcKdH4f0ZhznkLuuGEnzSlR92Mip3KSVcvejR6Ipqshjwxhz1Foh1m-u4tZfpyrZ63LQZKmWAhNGQRTSUgEP6x7fi3AMl88HAjNlEbNgFVURT_VeNRJu-VJWWFyAU_DdZSngs-TIiXag2fMxMPqfCMtfBPEX0YsiHhRkyp9HJ4dELzJ0NpsKsMMwQNBoGahWAiWCh3lrMnw5VyQyFHek0CXu_o_X8CSTAhhozHLhS4femXBw8QEtLTo1BtPrQ7O0uXx9AsiXtUKBZzIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uqgtwTu-088SMUcqsvl3EzjjI7kt-taeWx3IhzJ53jJfjVrB5LPX61Aulm_L8d5BNLsFFRY1ff7pMIPpoWO9z6nadJjAGiXR26VMmtWriA7wkOQ_lW22AivJksvIG3Du8Q_fnuJq_fAHdCveXWusZYS0CGkXIzYlKpAOcYGOrq6-JJ91nT7pzbJf2pbT6UMOjRB8_2coRItjuTl1_2UGW8MhcT49fPiejcak1gx2zQPhb-EbD-YYtsvTQ0ytSEpCLL_G6TNlzZYnlgRGCu0rBXoduho6m4FX3rFN-plEQ6-xUuR7KgJCT7sZk_DeGzoJi9GDI958TwzF15ibnwV9Bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
لبنان سفیر جمهوری اسلامی رو اخراج کرد!
گفت «عنصر نامطلوبه»! گفت که جمهوری اسلامی عامل وقوع جنگ در لبنان شده و جنگ
رو به مردم لبنان تحمیل کرده.
اما سفیر جمهوری اسلامی در درون سفارت خانه موند و گفت برنمیگردم ایران!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5199" target="_blank">📅 18:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i9yxRpXoaP1eeWOgxzIlXmuWjLpYRWDE-f-IoRTBwuvVU66cj0X5H0jIZlCRWjjDyShWhWqfmKFF9NW3Bt9Ioqskjir7OdWBg-Yj7ukRccyixvmstJfYUoVd9ogv1kjQgD-ENgdXn6Yt7VysxtEAu59hOvNSR_Xdk69nCYZHnYXpodrdAt63VYs-m70_fkw2HrxasARKI662lv7R3gWaRVQOCOPF5BF_74QyxlKMCgMh6QdlZlLu7Ovm6S0kc7wpChvJ8gRWU-lTaktJ2xt76A1gh4IAyfBPZbVhxSkI-l9aXsXrjrz0W2GuOphApXSAXBBIXWqXRb4TkMNCdzo7vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WTg6sWNMtbsCdKCD5rvspkkDJQC5sBommNgg5yaCpURAIOzUCgklvbE9BHhI1pgjAOthklCSstdSOxpIDQFxFnqh55n5dfL2tne2GRXbPNeQ2JdJm56TSWzTXRooTwHBAUXGPVYKGr2oMXeMdc1BSkLmSGki2eb194p4MNg41vxX2a2eRS11o3mMTW7hFxRH3QWp1xUuni7CXD5KReuaWObI5dk-kkzNDL64GXeE_D6fwDn2oYMxou7Epuy3uhJBjwiC2M9voZdNUHLh6RvTxCjX7L1wXsTAWoeCw4oCelVZ7iqtWjP8-Er2Dx3pino_Y8D1eP7CAOrNf_dnJV4aXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
درسته هر شب توی خیابون‌ها بزن و برقص و عروسی داشتن اما در افغانستان گدایی پول میکردن :)
سفارت جمهوری اسلامی در کابل در اواخر اسفندماه رسما تقاضا کرد که  مردم افغانستان به جمهوری اسلامی کمک مالی کنن!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5197" target="_blank">📅 13:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=atwt7l4VpnBz9jK-1MjjnsVUGv5B5lhPgjDhS0ueBoZeF2UH7qC_BZ-2mmpjQ-nzWRDuuDE5ep0sQbPDVUjXlmZlDoRG-RUHLifiuzFM4gLzZoje6yga4Ig_65GXk79hnhylMqAc9hd5mNWN9LMH1k2dfKFU2Q_fxu5Zv1kpxQpYppE_c5h8FIyldhgcYqQb7JBDSJ9g_YS9sJ9UQvkE7X4iCqR-E4tN_lpA_K_PHe0Xj1iOozGA-oIEvrucGY5LbDO6g0J6IByp-o0BrwAA_IbF-rJsHFjjLBh9pmK-9Fj_wuhiSDgn3QNuu2Dd8X3IYwXpQqKhRhHyf20tKKiylg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=atwt7l4VpnBz9jK-1MjjnsVUGv5B5lhPgjDhS0ueBoZeF2UH7qC_BZ-2mmpjQ-nzWRDuuDE5ep0sQbPDVUjXlmZlDoRG-RUHLifiuzFM4gLzZoje6yga4Ig_65GXk79hnhylMqAc9hd5mNWN9LMH1k2dfKFU2Q_fxu5Zv1kpxQpYppE_c5h8FIyldhgcYqQb7JBDSJ9g_YS9sJ9UQvkE7X4iCqR-E4tN_lpA_K_PHe0Xj1iOozGA-oIEvrucGY5LbDO6g0J6IByp-o0BrwAA_IbF-rJsHFjjLBh9pmK-9Fj_wuhiSDgn3QNuu2Dd8X3IYwXpQqKhRhHyf20tKKiylg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=C-S5WJHgF4yI3J3fj5515YMQLyzRn3W0TF5g9DW7PGtVxVJRjj4mDLu0OsHRZGsZWsVbo0UbkT1-uC7sXdS-54mMSs_LPWMFyouwFHNJzSisTqfmwAHUQyinPL64YX2IEE041NOBVtRAZEuoyfqKDQcv_AVcalqxvgs1ViesXC_X1ZE7J-KZ2IYo0Iv422HmAfGc1l7DBuxnmia5Ws1P2gRs1UlLdNn7TXutK-6V48mQVCiST23BHu3HBQLA0k_DyYUEft4mTs46dC0CPYXeMzgLx2JSpHmRdTprdK4PRPzmjNiuhV1_PBBBqO0DDsSOQ-2IHjxXAxTSKQCzrCP_lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=C-S5WJHgF4yI3J3fj5515YMQLyzRn3W0TF5g9DW7PGtVxVJRjj4mDLu0OsHRZGsZWsVbo0UbkT1-uC7sXdS-54mMSs_LPWMFyouwFHNJzSisTqfmwAHUQyinPL64YX2IEE041NOBVtRAZEuoyfqKDQcv_AVcalqxvgs1ViesXC_X1ZE7J-KZ2IYo0Iv422HmAfGc1l7DBuxnmia5Ws1P2gRs1UlLdNn7TXutK-6V48mQVCiST23BHu3HBQLA0k_DyYUEft4mTs46dC0CPYXeMzgLx2JSpHmRdTprdK4PRPzmjNiuhV1_PBBBqO0DDsSOQ-2IHjxXAxTSKQCzrCP_lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید
در اجتماعات حکومتی شون
هر شب عروسی داشتن!
«صیغه یک ماهه»! در برابر «یک سکه» :)
با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وقتی شما نبودید پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،  پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!  حتی زودتر از پیام‌ شهردار تهران!  حتی زودتر از پیام جوادی آملی :)   پوتین در پیامش نوشته بود :…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5194" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QvkAirGyjMx0PiMJe4K2dKCN3U2gVISQnRttLxVaU9aY77Rn_lUK6OoXOZ5Zooh1SoLNxMA67x8-ZiKfrH3HbT5eAb29oxRmGKLqmTnslY-fjtcXLIKbbP0FIywlmy7T-YUfttuAJ1mb0-fyLfcd0FKWtGPg3y38PPQ4wiabou4RmpAFNNCZGIursOY8N0gLX422RcBt_pyvem-y77vF9h541nztNbdo6wsyhAQPAFfNFLYROLYR-tXXX4Tkug9miRPMrjK4vi5pjJlyDJiMV0SE7PVAPhDpdcrA-oaQgtMCJl2aXfyX-LNUcoJunJk40_entGl8XZ4_SElhQTxl4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tyOjgY1Uoi-t8A7JiHG19Ojwj-RvTH9RRKFqV_ZNnRESzB7FeFKeZAlPilF6kNFAowPKFQgcu5b0KF_O1EAJ5h6DJOC3c6FbKHsHKa1W201lAoT-_WdAu-Y47r2fD_KM_3yiOsdqWsAKlD83wS6y2Qhob_Puwk5ORacPo9QBzOAiXULZp0AFSslNvpWaEe5c9QePpWJdNkm_dXcLnKT7HrVDd8g4jxTvb6LGM6XWoY_yA0j6jx4lBbT7FlY7kzdV6LUU_woUdPAB4cS2oG0GpA6syAtSGOoW8q8QLyAsx52Gwd6XAR3VIRWOFVzJMjaQunG97dArwQNnYrzbhhn3gQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5192" target="_blank">📅 12:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=j3QmxAnL6Ml2QrzjwwbyOkEzgCHrUZV2z0LGZONIpxh837ORv6wE4J11Bgh3pC-9qV6ja_IfHVRoJTjqoIf3HLWGH0Ol6cc4zMOmYD0RBGmA1UkZCaaNr3Qa12SQrVGuo-KHOjh8cvSyXAGW0yuWZRRnXa0nTswvycr0r_qvomJ2yzi6NFvrxHsoJqi4fGSKKmruxcKjObhn6eYobjiPqjEB_A0dojAm2PD-La7evaiBor-QcODgeH5VPEY_PZXYRVCZg0448GruIER0JtjuuXfFLy-g21qbYepo528huRjW919-1aiyWID5DQUaZuuMwj31In7Wi1AFparAfkaHVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=j3QmxAnL6Ml2QrzjwwbyOkEzgCHrUZV2z0LGZONIpxh837ORv6wE4J11Bgh3pC-9qV6ja_IfHVRoJTjqoIf3HLWGH0Ol6cc4zMOmYD0RBGmA1UkZCaaNr3Qa12SQrVGuo-KHOjh8cvSyXAGW0yuWZRRnXa0nTswvycr0r_qvomJ2yzi6NFvrxHsoJqi4fGSKKmruxcKjObhn6eYobjiPqjEB_A0dojAm2PD-La7evaiBor-QcODgeH5VPEY_PZXYRVCZg0448GruIER0JtjuuXfFLy-g21qbYepo528huRjW919-1aiyWID5DQUaZuuMwj31In7Wi1AFparAfkaHVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم مشهد از خبر کشته شدن خامنه‌ای</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2ZROrKpc6s2F2mf_GFN7CNzZmx5YPDUtJU-i4zIcduWxpNusGHxNZFVtLCDKLcqgHIOlFOHHYDOeNLGO2ehIiCqaNXH26XpDgsCwHnAPAoSyQg69bHszdEUhsb6HNNRGs-p8pxpQpmkhUt3koKQUyK3rRgTs0j9T814qjVduToRT503_mH5QmW7_Emv0RJfjGpq95Jp0Tv5ecQOtn1NPPUJaTc5UZco1JepjmmB8ZIE0FLBDc7bFIWogGtwdcAYRzNpC3SalxYQJX6VTOcUj4mhsTGLn-MqOn18X9r9HmvchJINsEb9VW6ls9fqFhwTGKQAPgCrBmlr82dp0hp9fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نکته جالب :)  امروز ۲۶ روز پس از کشته شدن خامنه‌ای  در کره شمالی هنوز خبر کشته شدن خامنه‌ای منتشر نشده!  فقط اعلام شد که مجتبی خامنه‌ای،  پسرش جایگزین او شده،  اما اعلام نشده که در طی یک حمله نظامی  خامنه‌ای کشته‌ شده.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5190" target="_blank">📅 11:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
امروز : کشته شدن ۱۴ نیر‌وی سپاه زنجان بر اثر انفجار مهمات عمل‌نکرده</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5188" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
