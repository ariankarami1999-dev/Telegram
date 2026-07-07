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
<img src="https://cdn4.telesco.pe/file/osdWt1GLC7NyW_x5VFgBwooyo6rUnF4bJBGE1lSt8yaqkk6BKtJolol1lI9i1kG7WeTmX8XWljmYa-KpL3jSyaNLhhuh5CmDIFMJwOHf-gD_A2r0ZprT7MEiRCGtX6KVubnCivqRF4xpLOI0nFBtVVu5F7_1NYAf36t1E14Xed-7-uyyTD9CLVtFjwHYMnOMgU3vqi3nPutrGcxPpcoKAffnIzn2Lu93C_kyJiu6ro5bNQm6J0n1rCF9guBQOQrHYE1XHxWJI4UdMCnm2jLnP8-X2b_vEORvuaVG06XtwoOPWdYW10UAXRf923PCYBK6M-EftC36TwPbqKerLh7Rjw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 340K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 03:19:19</div>
<hr>

<div class="tg-post" id="msg-16773">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نیکلاس کریستوف ستون‌نویس نیویورک‌تایمز: به نظر می‌رسد جنگ ترامپ با ایران دوباره در حال ازسرگیری است
علاوه بر حملات هوایی، آمریکا لغو تحریم‌های نفتی علیه ایران را نیز پس گرفته است. این موضوع صرفاً یک نوسان یا اتفاق گذرا نیست، اما دست‌کم برای من هنوز مشخص نیست که آیا ما به سمت یک جنگ تمام‌عیار بازمی‌گردیم یا وارد سایه‌ای تیره‌تر از منطقه خاکستریِ میان جنگ و صلح خواهیم شد.
@withyashar</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/withyashar/16773" target="_blank">📅 03:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16772">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">لحظه سقوط هواپیما باری پاکستان @withyashar</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/withyashar/16772" target="_blank">📅 03:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16770">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eed44ca638.mp4?token=rNi3ouoByEHYcxOSq_5Cssseyi0cMAlgQX5fNLWkENVaGeB9ZNUVR3NCKqn2xeaL_9a0tlnp4w4HDV0sXlHDeaDcryfiDE4YIyh2RoI1duh9lcMawB2WH99Lvl1wVqaDLvMwpfCfzodVYd6hVuFWMuWCnRd-XUoXKV3KHX4kNtkBikikH6hTtArE9hKR6Eep-bgV-n5Re6n0hkM6vaTrPAO_8Y5B1QmQiInSkNIdDoyd-JgY6fN211sNyOt1PAsZ5wmNQhzLZhU1dV_kZdo28D5RKicxOMCXvYzITZHCM3VJUf0vSPRep032iOb9feKEOUYdeaWaq5UnerZOq-kgyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eed44ca638.mp4?token=rNi3ouoByEHYcxOSq_5Cssseyi0cMAlgQX5fNLWkENVaGeB9ZNUVR3NCKqn2xeaL_9a0tlnp4w4HDV0sXlHDeaDcryfiDE4YIyh2RoI1duh9lcMawB2WH99Lvl1wVqaDLvMwpfCfzodVYd6hVuFWMuWCnRd-XUoXKV3KHX4kNtkBikikH6hTtArE9hKR6Eep-bgV-n5Re6n0hkM6vaTrPAO_8Y5B1QmQiInSkNIdDoyd-JgY6fN211sNyOt1PAsZ5wmNQhzLZhU1dV_kZdo28D5RKicxOMCXvYzITZHCM3VJUf0vSPRep032iOb9feKEOUYdeaWaq5UnerZOq-kgyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این این این تحلیل ممباقر‌ الان میچسبه
@withyashar
🤣
✌🏾</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/withyashar/16770" target="_blank">📅 03:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16769">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
طی ساعات آتی احتمال شعله‌ور شون جنگ بزرگ وجود دارد
@withyashar</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/withyashar/16769" target="_blank">📅 02:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16768">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اینترنتها به شدت ضعیف شده و ممکنه قطع بشه. حتما اگر پیج اینستاگرام رو فالو ندارید، فالو کنید و چنل تلگرام هم داشته باشید تا من رو گم نکنید به دوستاتونم بگین این تنها کمک شماست
🙌🏾
🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/withyashar/16768" target="_blank">📅 02:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16767">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سی‌ان‌ان: وزیر جنگ آمریکا روز چهارشنبه به اسرائیل سفر می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/withyashar/16767" target="_blank">📅 02:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16766">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMf78tnfnByV_QB4n5oL4ediMntVuds8LjmqKjp7Xt-t_dRJonFM_IMTsv5rVLTNS6Ik4fcz8eOmHbdp6VxOwxIrDX4C9R7JTRnoSOdTbp4GG9nr9ZwsrJdbpOSJNDYdHR2gcF5nmJo9crITEgmbErjDmOy4u2tq9x3f17ogOnH6AGuzVxob39p9EGLvUtGAbI32Jb_mfWWfoWArGsBhdbL4uZ5L3vYAdNH8qe2MqFzW2w3ZOdh0D-nIK4SYJNGui7qEkSpVqkmvh1tGMfFkIkpOxx8CEcwCE4f42BmPyhFY8De3bXer5CiyfcVF6bLiqyf1GPzzGR6RMRq5HAKMZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این صحنه هم باید تو تاریخ ثبت بشه ! کالکشن تمام هواپیما های آمریکا یکجا
🤣
@withyashar</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/withyashar/16766" target="_blank">📅 02:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16765">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiSOakPv4IOVXo9_wmLoEDIpn3m4bZE0-axdEfxkr8SvHH4K--siNpvYamX18JWSoRh0qge_xYrd3LhE2fnPJl0gKVaQ-0IolagAmkwJAeb-QmdFHf-VJnTSGJL-sLybULZCd2HDihdV13-A3DftwvLo83ghUlD9qykP56jSVQVyMcKA0BwvDBEKDzcxSiY_27BbwWnm4nqQGZhTi7zkHdi5qfXgt8JLU0WnObvkHKvhCcqxlRM43qSkwlzhKp9zhAHiEKb5xrO7vuVsOBQlVXzr7q5zrxMo2fjHzdT4Y_3xGEWbq3ymDk7_mIAKhaYIwERmOsTickrB5FvZwRZYLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان بعد از شنیدن خبر حمله، سریع شال و کلاه کرد و فلنگ رو بست تا مجبور نشه با اتوبوس برگرده تهران. هواپیمای مراج وی هم اکنون وارد حریم هوایی ایران شد.
@withyashar</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/withyashar/16765" target="_blank">📅 02:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16764">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اتاق جنگ با یاشار : ایران و آمریکا رفتن فینال لیگ خلیج فارس برای تصاحب تنگه طلایی
@withyashar</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/withyashar/16764" target="_blank">📅 02:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16763">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">قشم ، حاوی الفاظ رکیک
🔞
@withyashar</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/withyashar/16763" target="_blank">📅 02:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16762">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اینترنتها به شدت ضعیف شده و ممکنه قطع بشه. حتما اگر پیج اینستاگرام رو فالو ندارید، فالو کنید و چنل تلگرام هم داشته باشید تا من رو گم نکنید به دوستاتونم بگین این تنها کمک شماست
🙌🏾
🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/withyashar/16762" target="_blank">📅 02:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16761">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKU7WhVvO_8O1WWTsY1gIl2mrG7LaiXKLnlR-KLxmxpBw8BovcD86kYR55lQdE4varFr_2PghIQpPf4JsPdF3RMzBO5YKJJHjxqL__KjZ4dTwskZj71nye591Nw-a2YLLwuaWwttmZ51CpoF6DonuPRSp6OnX_jZjGiaIsAcAKG-z9UF5jHtIfJmTw3uk_y4n0-skvPMhR8nPQ5fkJSUAhgsMg4-g9XAL84sdaUh7Jvd7SOjYHCa62QIDhiauOU9taUqXJy1n1pfWkijdCJ_RB5lImsQek047RHWGY1egv-hc6tcKDcd2eV3J3RgDGt2OSnKFErh5eUvL293TYlWeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون دو انفجار دیگر در بندرعباس شنیده شد @withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/withyashar/16761" target="_blank">📅 02:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16760">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">هم اکنون دو انفجار دیگر در بندرعباس شنیده شد
@withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/withyashar/16760" target="_blank">📅 02:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16759">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اسرائیل قشنگ داره لبنان رو می‌کوبه تا جمهوری اسلامی جواب بده، اونم بیاد ملحق شه
@withyashar</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/withyashar/16759" target="_blank">📅 02:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16758">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دوباره از اصفهان جنگنده بلند شد
@withyashar</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/withyashar/16758" target="_blank">📅 02:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16757">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">الان وقت مسخره بازی نیست !</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/withyashar/16757" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16756">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خبرگزاری‌ های رژیم : چیزی‌نیست بازار ماهی فروش ها و چنتا کشتی ماهیگیری رو زدن
@withyashar
😳
🤣</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/withyashar/16756" target="_blank">📅 02:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16755">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">منابع غربی : حضور ترامپ در ترکیه خطری نخواهد داشت زیرا آنها متقابلا میدانند مراسم تشییع  خامنه‌ای به حاشیه و اختلال کشیده خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/withyashar/16755" target="_blank">📅 02:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16754">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">صدای جنگنده در ‌آسمان بندر عباس
@withyashar</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/withyashar/16754" target="_blank">📅 02:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16753">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بندر عباسسسس دوباره االان
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/withyashar/16753" target="_blank">📅 02:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16752">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKEqOv_luT39Njfd7POGCvVAWLCOAKx-96_B8ZARkJ5g8fsctNFnWxe9TCys7LeDEjUE8PX1FIXRxb1MPWnXMHxbNT1Fmi0K_rS9T1SP7P3rkK6_WAsGaMmHzfExYzktlGFZ4146AgCwCixLfjZuNcoZrIAWE2wjRaNpJVqkGWdIqz4IMEoMQ4GE5f5XyxSV7nz2QSFoDGuawIzG_hDTcqo47qM3vFcR9DqkQbFfRbRa_Z5Dirs_Csqj6ar_8NzyZUzmJMnyv0Mi7ndD2CPgVpJ7E5GCTPk2BTY5cWn6OZZk7jZCm411h4Lf-2R-nytXyY9k7K-2wuBRXRl4x7sZSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیریک الان دوباره زدن
@withyashar
حملات ادامه دارد..</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/withyashar/16752" target="_blank">📅 02:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16751">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گزارش از بسته شدن تنگه هرمز @withyashar</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/withyashar/16751" target="_blank">📅 02:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16750">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">مقام آمریکایی : حملات  امشب ۵ برابر بزرگتر از ۱۰ روز پیش است
@withyashar</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/withyashar/16750" target="_blank">📅 02:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16749">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">گزارش از بسته شدن تنگه هرمز
@withyashar</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/withyashar/16749" target="_blank">📅 01:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16748">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دوبار سیریک رو زدن
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/withyashar/16748" target="_blank">📅 01:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16747">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f5c9f2899.mp4?token=ILLaUCkX28xMqkYUt_p_0rv71N3jWgnU7rrt84rLnlar25aUA4aR2IXPAvfjQWqbTyeElqdKco_lRuRdUB2NUNp3taxWPjqkXMvE9u0OTk6pUnqf71GBgKPH1yUA89SHdPng4vui6q723UxsypU3ZaBeqSJsQnKKnoQ2Kkd48hJZZCOa-mTcPHtZDeYhIlogSNzEQBoowaSRrnZ-hl7Ocvv4AAewT4FYyu4QXVU9ryayVy_L6oRUm9xT4Yw8xbAgFFIrLv3ZpPcyg53E2TDlat5dJMNubN692x5N7aP4n_SLsWch3V90_hL3hh8mMr7Sw9BBqeQ-C4E3Xn43aOrmrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f5c9f2899.mp4?token=ILLaUCkX28xMqkYUt_p_0rv71N3jWgnU7rrt84rLnlar25aUA4aR2IXPAvfjQWqbTyeElqdKco_lRuRdUB2NUNp3taxWPjqkXMvE9u0OTk6pUnqf71GBgKPH1yUA89SHdPng4vui6q723UxsypU3ZaBeqSJsQnKKnoQ2Kkd48hJZZCOa-mTcPHtZDeYhIlogSNzEQBoowaSRrnZ-hl7Ocvv4AAewT4FYyu4QXVU9ryayVy_L6oRUm9xT4Yw8xbAgFFIrLv3ZpPcyg53E2TDlat5dJMNubN692x5N7aP4n_SLsWch3V90_hL3hh8mMr7Sw9BBqeQ-C4E3Xn43aOrmrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قشم ، حاوی الفاظ رکیک
🔞
@withyashar</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/withyashar/16747" target="_blank">📅 01:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16746">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ناصری،عضو مجلس : دقایقی دیگه موج جدید و بی پایان حملات سپاه آغاز میشه این بار شدیدتر و ویرانگر تر.
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/withyashar/16746" target="_blank">📅 01:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16745">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کویت و بحرین دچار قطعی سراسری برق شدند!
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/withyashar/16745" target="_blank">📅 01:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16744">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9748bcf07b.mp4?token=FuKiHAh085G9nkuiMMqdYuRXJHl1VayAruexYfb0ys3sG3g8_qyniWHLWdnTYiZzUbWhlpd9Wwa1cLYwqJ_5hJUNUMtfrg4Uv8y8yfhpxmr6e5mqSwsKebEWEmXxsIONEllwmY7noX1u95a17cxeIpHIwx4odmXMSDa6p4OiWSUBqhLUDEA4CzEbOM5JaiEgzi5-609b4DW2znTwv84IIgTJGuZ0sneSGmIBhf47htW6dmYCCx7ykOQQu5YBFawCy8Ow4cFto4U6mCyRvWtVNn--X8W1cCEdF2DG6R7L1h12QOX3daVQ10AKCjKiNUjE316HYfr9D7QVvY3SLN0_zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9748bcf07b.mp4?token=FuKiHAh085G9nkuiMMqdYuRXJHl1VayAruexYfb0ys3sG3g8_qyniWHLWdnTYiZzUbWhlpd9Wwa1cLYwqJ_5hJUNUMtfrg4Uv8y8yfhpxmr6e5mqSwsKebEWEmXxsIONEllwmY7noX1u95a17cxeIpHIwx4odmXMSDa6p4OiWSUBqhLUDEA4CzEbOM5JaiEgzi5-609b4DW2znTwv84IIgTJGuZ0sneSGmIBhf47htW6dmYCCx7ykOQQu5YBFawCy8Ow4cFto4U6mCyRvWtVNn--X8W1cCEdF2DG6R7L1h12QOX3daVQ10AKCjKiNUjE316HYfr9D7QVvY3SLN0_zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه انفجار ها در بندرعباس
@withyashar</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/withyashar/16744" target="_blank">📅 01:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16743">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwUohaVqrHEVNt2EmUSsk-MlFdm1r5flb5SWsysWYBiBPiNo3YOJeth2fTwEXYu7t2rq3cZ_I6xLmqipKcDXg2_pJ9F624fY69CMslSkliXrKvTQavX4rad3uQIcE0sgqYoLC21sr49L5SeS02xJ-ImTikvD4IYdioxw7BxstpjB42_MGlc1RuN0lj1Pc1_1E8hlM5oStf0yNjhtvrjSZdxZaTtdThqR5AkI4rJ0Ys79Fx3DChP5cBioKplsP111oXlKrH3twp2yHCrh1N43C8tZzNnd-FEi9B3HBy3miE7dERB2x5yKizW6E6CgZwF1sYZZa9vZKZ5FWZUYb5Dbzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسمان سرخ بندرعباس
@withyashar</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/withyashar/16743" target="_blank">📅 01:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16742">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دستگاه های اخلال گر GPS در سراسر خلیج فارس و تنگه هرمز فعال شدند  حتی تا کیش‌ کاملا در سیگنال قرمز فرورفته @withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/withyashar/16742" target="_blank">📅 01:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16741">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">کان نیوز: در آمریکا برای احتمال چند روز نبرد با ایران آماده میشوند؛ این موضوع با کشور های عربی خلیج‌فارس نیز درمیان گذاشته شده است!
@withyashar</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/withyashar/16741" target="_blank">📅 01:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16740">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خبرگزاری بین المللی وابسته به سپاه:
پرسنل نیروی دریایی سپاه دستورالعمل‌های اولیه را دریافت کرده‌اند تا از تردد تمامی کشتی ها از تنگه هرمز تا اطلاع ثانوی جلوگیری کنند.
@withyashar</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/withyashar/16740" target="_blank">📅 01:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16739">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAW2QHkYgAHv0BEE4XpJQ7Sf6Tg5aEWUvEIegRTnk1_jtnKrNeHWck28Bg13rhjmcTj08ZfgGlEDECRawaF-8YJJ1XhO37srVk0i4Pk3dAyMQpXXHYplIypBEy1P3qbwZuIR_6T31GVGoo3odtU6Pyqwj3sfXpDjN43bLbNR6521yw_phEKw6kBGk1OIG2thMr1vI18QKX0EC3cXI3Aq6RbnDjZ8JHsOPVRUyz0aWl0z3D_iniErnsCpHuyQfAkNJY-NkHehdBEvlUf4hxMEiwYp6PXKAfuPaFFOlHB2H39wGdgltzyKaDX_A-XCfH9HVlqVqyzygvrzgNGSa7tgrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندر عباس
@withyashar</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/withyashar/16739" target="_blank">📅 01:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16738">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سی‌ان ان : شدیدترین تبادل آتش از زمان آتش‌بس!  هم‌زمان با دور تازه حملات آمریکا، ایران کویت و بحرین را هدف قرار داد. یکی از شدیدترین تبادل‌های آتش از زمان آغاز آتش‌بس در شرایطی رخ داده که مذاکرات همچنان شکننده و ناپایدار توصیف می‌شود. ۹۴ روز بن‌بست؛ تنگه هرمز…</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/withyashar/16738" target="_blank">📅 01:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16737">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مقام آمریکایی به سی ان ان :
حملات هوایی امشب آمریکا به ایران مجازات آنها است، نه متناسب با کار آنها
@withyashar</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/withyashar/16737" target="_blank">📅 01:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16736">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56eee461b5.mp4?token=PczE4c08HrLo2umptJFay6SfMasGY7qnTmBuvDJlEDdE3DTz8PLR6LIjZncgGxovpk9Q65wwM5AKes50XM3mTv4ROBXfOdS_6MbHiDMd4ZWvDE-WDh6JN0XdjeVRABZbpktkb8Rv72H9f-QE6VOYJRcbXuzcLX35UJ-7Y7ZLJsgtJSM16aS8IVL8eWvu9RxmSMKJseb48mLV0O9mfQizsW-dDlcjEExYF1LOzVE3dEMRjlvLbSAPac3Tfy0eut3bjGCC3sSbmHj5dzYJDLQoltMD0Tc31wew2kwnjGKHqaFDPURzZXUP8cz-3bIzJoV6BUXiekJ_LO4i91aQDYNmrheSj5IBeuFuZdQR_Ow6hQyeHgSuFC82baNTaFtCkWPMSCcBlYBDENT72nPlTgjCxuxJBxVoAyRavgoDrohb__PA04-HZGIdnLMTOBt86VMftWdjo6S_PN0VW9Zu2V9NP8kL42_zbahcq4fOsvh6RU9m1bbubtxkrIMYT0RE6N7tftQwmkgHT28-FqN-8ypx37ajunMskk0NFKp38Llq4IUMVxUqrdPgzmN67fDBhrSn6dbguJZh1pF8Ma4KSu4QPQn_qWbHuWuAdKqcfXazdhnqChGVfCTZkSrBtOIpWTDMNcnAA0UreLFsxOljTciOeXtMJgVEmXDFOfA3TghScF0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56eee461b5.mp4?token=PczE4c08HrLo2umptJFay6SfMasGY7qnTmBuvDJlEDdE3DTz8PLR6LIjZncgGxovpk9Q65wwM5AKes50XM3mTv4ROBXfOdS_6MbHiDMd4ZWvDE-WDh6JN0XdjeVRABZbpktkb8Rv72H9f-QE6VOYJRcbXuzcLX35UJ-7Y7ZLJsgtJSM16aS8IVL8eWvu9RxmSMKJseb48mLV0O9mfQizsW-dDlcjEExYF1LOzVE3dEMRjlvLbSAPac3Tfy0eut3bjGCC3sSbmHj5dzYJDLQoltMD0Tc31wew2kwnjGKHqaFDPURzZXUP8cz-3bIzJoV6BUXiekJ_LO4i91aQDYNmrheSj5IBeuFuZdQR_Ow6hQyeHgSuFC82baNTaFtCkWPMSCcBlYBDENT72nPlTgjCxuxJBxVoAyRavgoDrohb__PA04-HZGIdnLMTOBt86VMftWdjo6S_PN0VW9Zu2V9NP8kL42_zbahcq4fOsvh6RU9m1bbubtxkrIMYT0RE6N7tftQwmkgHT28-FqN-8ypx37ajunMskk0NFKp38Llq4IUMVxUqrdPgzmN67fDBhrSn6dbguJZh1pF8Ma4KSu4QPQn_qWbHuWuAdKqcfXazdhnqChGVfCTZkSrBtOIpWTDMNcnAA0UreLFsxOljTciOeXtMJgVEmXDFOfA3TghScF0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه آغاز حمله
@withyashar</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/withyashar/16736" target="_blank">📅 01:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16735">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گزارش ترور هدفمند در بندرعباس @withyashar</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/withyashar/16735" target="_blank">📅 01:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16734">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmtTz6Hx7zof_ZOfHX1rWcf-qVU_qLS8FU_0Hbh4_Ixzu6mCdNK1T64h6LVA6HNaj_pjOdqfxIt0ylEO0JWAOQsL8fAg0N43DgcvcCVtve1WqSnQPCpR-DM7uf4NFx-jQOeLP4f17nGPwoGPKkDvA0XrgyaJimx1B_FY6bCr_moyZ6ZNWRkftFu-IJPWkG3V3ljBzxvESJU5TgFl0kwivyb0IPJrNMWq8Kp7DUKb770-qfx2i5FO3E-V_hLvWx6gLjYuKb5NfdmvhQyRFrVKisJiCXEReIVdukMHp415Dcp2QnYv37iI2iqccS81G-IgAaYjMorOqK87OKjK4ImXJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله بندر عباس
@withyashar</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/withyashar/16734" target="_blank">📅 01:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16733">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDpozonp5eXl6DsETY6RjtVeoQQdsgAaB43tPRf2GZlrrqGtEPz0FVcn2W9rD62wEkbbFNkbpACbZpXDvJDE_NtWqiGFlV2L24aDugCj8ElzAzQFyOqTWdrzk4usczuG8MSap6F1wM2NsUKRjKoKzq37hV0rUD5rjJUo2WJdHlR4QoXOl7ezrwh-FvyoV4ImRzn5riJpgylZP0FgPmJcMhZn44wTeB_2izeID8ZVO-TdCkunTl--MVoyNIYfCYKsyAYT06p5JjNw8VaUooJii-3_AXMrzBJ8vJRGiKmTUOAyLw7KPxdh0YnazukkEoHr8JLgJRmRh_2iFC-4ysjm9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش ترور هدفمند در بندرعباس
@withyashar</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/withyashar/16733" target="_blank">📅 01:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16732">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgDR7m5IvdqauN5uvjo1b-jZsS7pZhXrAF-nNPn-oyYAVt0JuBqur8RaI7Cyr_cRSpCsw0lReUv19n1a-BI7xOksYJ29SYrgElGpOScQG5488QeqvAfBIqUIT7tJIi42PC8Zu2gHRtTSHwxCt9htRfOx3tjkY1zsY-ERg8JHBDcOgwqxfe3BmF-d2CUY6d8Wa-URD988GHwMWg-8rcgvgd64uW63wgLbx79lUUJh53eAsgtNHSb8uRez9lXzhOvqpc0ifXtcvPUl8DWq5Kt9vbf67TOP7nYOZ625EK6AwXwrcnL8kWkzhiVnPYnythRDar5PuQy4K34jafxYK7gCsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله بندر عباس
@withyashar</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/withyashar/16732" target="_blank">📅 01:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16731">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/496c7aa925.mp4?token=vkL8BlAF25LtqCiJosBtdusscMpVxPCdFLbLL5u2FR0LH-nfpKxPNbFi0FUWAwz1mrAsfYMhJRxrBcWGhW20Y-0yUCXf49AlsCB2O1-OgoryrsiQeQVe30EqQ_ELQYwMenI6i5Qqa1EXJfNx89ImhRLl2Tewz2IrV2x87D8KQcBH7FIlGyTnSfGFSe152xOAQklJTi1zZ0KoP8scxMcbD6tDukZQnGrrMvJhMsPZm90SuunLvoNszIYaJdiJwTL-S9tfS7UxSNIzxH0GWwc3XvuIGaxikIpeUacVjmgkr0AkEiJ2u4R_U39KgIXc_4uIn1z6m6T7ZB1v6RVSFbWa3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/496c7aa925.mp4?token=vkL8BlAF25LtqCiJosBtdusscMpVxPCdFLbLL5u2FR0LH-nfpKxPNbFi0FUWAwz1mrAsfYMhJRxrBcWGhW20Y-0yUCXf49AlsCB2O1-OgoryrsiQeQVe30EqQ_ELQYwMenI6i5Qqa1EXJfNx89ImhRLl2Tewz2IrV2x87D8KQcBH7FIlGyTnSfGFSe152xOAQklJTi1zZ0KoP8scxMcbD6tDukZQnGrrMvJhMsPZm90SuunLvoNszIYaJdiJwTL-S9tfS7UxSNIzxH0GWwc3XvuIGaxikIpeUacVjmgkr0AkEiJ2u4R_U39KgIXc_4uIn1z6m6T7ZB1v6RVSFbWa3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه انفجار بندر شهید حقانی
@withyashar</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/withyashar/16731" target="_blank">📅 01:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16730">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28bfa928a.mp4?token=NZSLgRueSRY_K7hw8Ptty55udU8OIhUm0A1FRZdRVSodmJ04J84eTc_ax7ByZrRltUzkLDbiS-URVAw6RJ7mr6Wcsuz1b3sTz89iclf426gVDj6yEjPM0VTDrf29WtzzKtdJT9JIjtdFWrwfbF7MSccPxvGj6v-cBpWFy6X_ug3nzwCWCPjIu22l0Orz0OlPErzD3YL3veJpyL1lr9EYRKK_2Ohe48YqgQ5ccVy1Kqa_5ZF3Z0CWWf0a4xchx_9fZqtWrMKtpqxjGMJU3L2024giaNMT8iPeoboV1_KXBRZngRYDi4OFHZSs3IkT8owpOFjuSWP_oh3pLIFVSw_u9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28bfa928a.mp4?token=NZSLgRueSRY_K7hw8Ptty55udU8OIhUm0A1FRZdRVSodmJ04J84eTc_ax7ByZrRltUzkLDbiS-URVAw6RJ7mr6Wcsuz1b3sTz89iclf426gVDj6yEjPM0VTDrf29WtzzKtdJT9JIjtdFWrwfbF7MSccPxvGj6v-cBpWFy6X_ug3nzwCWCPjIu22l0Orz0OlPErzD3YL3veJpyL1lr9EYRKK_2Ohe48YqgQ5ccVy1Kqa_5ZF3Z0CWWf0a4xchx_9fZqtWrMKtpqxjGMJU3L2024giaNMT8iPeoboV1_KXBRZngRYDi4OFHZSs3IkT8owpOFjuSWP_oh3pLIFVSw_u9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون
بندر شهید حقانی
@withyashar</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/withyashar/16730" target="_blank">📅 01:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16729">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1da252b259.mp4?token=uXElUErpvC_HKgvE_jv3Vcnpg7gh1HJYt7iFmbUZSRcfaV25t8Uu6EN9y-XcqBRVFDTi38WxU78wtBsOt_AHpbh6lXCAEUiB5flyzjrlUHy-bCEJqODAVhAGnkXPKE_MGT86QUX4C7HUgPzpHxfuTRYUX5Hp2ZVWDyI_3wrrdRuCzCVlb21xy6JkIyhbQO_Q4SafoJMxP5euK4ZdvyPAxsiZc4i1WrEJtnFzr0tgOgVRnixVA5uwMw9-xQI_470OQxZgwmsV_Uh_ozCwxjmApPYK5uC1DGhvaAVWj4py8qcM4wd5NmAQ1LelT_Px6tu_QgMmyHn66iCiDf5ysJmovQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1da252b259.mp4?token=uXElUErpvC_HKgvE_jv3Vcnpg7gh1HJYt7iFmbUZSRcfaV25t8Uu6EN9y-XcqBRVFDTi38WxU78wtBsOt_AHpbh6lXCAEUiB5flyzjrlUHy-bCEJqODAVhAGnkXPKE_MGT86QUX4C7HUgPzpHxfuTRYUX5Hp2ZVWDyI_3wrrdRuCzCVlb21xy6JkIyhbQO_Q4SafoJMxP5euK4ZdvyPAxsiZc4i1WrEJtnFzr0tgOgVRnixVA5uwMw9-xQI_470OQxZgwmsV_Uh_ozCwxjmApPYK5uC1DGhvaAVWj4py8qcM4wd5NmAQ1LelT_Px6tu_QgMmyHn66iCiDf5ysJmovQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون
@withyashar</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/withyashar/16729" target="_blank">📅 01:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16728">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cda8d61e99.mp4?token=rhR1C_RB0nRqsGaubgGm3cn_cf0YCVyLck9O0xfd5qdpArZP3EE5Zg0cfbIQW_EToYT1IRwr02pdUu1uGEAKI33H9g0jk0RQjeQ6lXvM0nOSWB2YY4dg9_bY8dI7wngk9uZWQ0G6CpS2eS0saaVeMAWAbdsgDh_cqbqU3Y0FW2XMF5m0L9SsVUWmntsrQglaANIFbx1FJ9mlz8B7OpOhGmsuQzhcHzRnErTfi18pA5_5Jk__msXBH70rzsgPm2b5cG05BaMpRgG0CIyLHWdt0SMvwJpbjPVakJfMyVGxm3RWIWwfVaoxKc_Sdjj3KtyXTF5LqErHlbwO78cbvQl9RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cda8d61e99.mp4?token=rhR1C_RB0nRqsGaubgGm3cn_cf0YCVyLck9O0xfd5qdpArZP3EE5Zg0cfbIQW_EToYT1IRwr02pdUu1uGEAKI33H9g0jk0RQjeQ6lXvM0nOSWB2YY4dg9_bY8dI7wngk9uZWQ0G6CpS2eS0saaVeMAWAbdsgDh_cqbqU3Y0FW2XMF5m0L9SsVUWmntsrQglaANIFbx1FJ9mlz8B7OpOhGmsuQzhcHzRnErTfi18pA5_5Jk__msXBH70rzsgPm2b5cG05BaMpRgG0CIyLHWdt0SMvwJpbjPVakJfMyVGxm3RWIWwfVaoxKc_Sdjj3KtyXTF5LqErHlbwO78cbvQl9RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون بندر
@withyashar</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/withyashar/16728" target="_blank">📅 01:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16727">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/withyashar/16727" target="_blank">📅 01:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16726">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">وال استریت ژورنال: کشتی های جنگی آمریکا در حالت آماده باش برای احتمال شروع احتمالی محاصره دریایی با دستور ترامپ  تا ساعات آینده هستند
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/withyashar/16726" target="_blank">📅 01:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16725">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رسانه های داخلی میگن سپاه قصد داره همین امشب پاسخ بده
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/withyashar/16725" target="_blank">📅 01:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16724">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0RVVyKIVEmzZW_EPOxhJ0mLTI1ogycz-Q6ntWZzljqOs9Eqo6fguPDz0QOa9t895SZVt5ISK85f7lytpvEf8VhhNiyNrgT6_no7HBkTqqPn59ybypOIA-wuGLmIJYiBTCCmjCd_99THUiTHngZxajHmciaouZaX9BCcsujoMIKtCSaFFbsHCBV2718gH0RhqwJ5nDwfVoD0fS75DNGAtIYooE9RLYAxF_RexddZbUruiuhOfpKPgUKHjzAvXuyM-zElQLBsLR8dRVVhJ0elA1mShgI0Y5Avwinj5XtAQaOgd-IheQPDd_j6pGrFPoI2uu2FGExzEtNkR_MlI45u4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظه انفجار سیریک
😳
@withyashar</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/16724" target="_blank">📅 01:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16723">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">😞</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/withyashar/16723" target="_blank">📅 01:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16722">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گزارش ها از حملات هوایی به قایق های تندرو نیروی دریایی سپاه در اسکله بندر سیریک.
@withyashar</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/withyashar/16722" target="_blank">📅 01:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16721">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HiIDVtQdNTKnxfzESNc_ApQAZSXsSYlEk1Q-PB-6-2miuSfuMdo6ycMnaLfQM2gOhYgGSshU-oJGC5ClczLeQjjuJPXwb2UwaYbBeaMfhLaWu9iNfERVhnAKxRDR4dv1H33RCv3if9MpQ1t8fpZodNcKHPvaTmKvnM1HiqzdBO0fI8TAsiTiyWqwTecacM4cgZ2UUiJM89FZAUvEjzdUlUVTlY2Snf_T-iwrG9rz0CAgNbScopMlnkUuTaY2yQvOwrtt7CfVkR2hVonfwkm1zy8qYGtAEML60oifSzFFJOEYGprYsPEyPZQHCDvNFrdI6zV32XS_eVOdV5gxUoGC1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار مهیب در
اسکله سپاه
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/16721" target="_blank">📅 01:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16720">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">شنیده شدن صدای ۲ انفجار دیگر در بندرعباس
@withyashar</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/withyashar/16720" target="_blank">📅 01:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16719">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHo2GCDW58CLWN0bcRhaxuvutx0eSqoLsEkSmBtrDdC42CTfQrbvcnMZkGT0_meGqf5K-Fz1OO5TKPV4qytNrzICgVhF8Llm4xMku6E3ejN94FeZeeYk05F9PfB4HL5TylihuOvbw1V8lkgaaM74aawGctR9n6vHz8nkOSUcdk5oPZ-LRGYH8aid2vZWEZaJn-GEEjtdI_Dwf3R4U3fuuh8Rqq5bhXbDw-rzpq6043CNvjqZAWz-9SjYRoDNkFK_zgh1t_dx_gXwcwnQnM2heK8LvSWeMsLWM-e7n4RJQ4-yYyVspkUlFrAVt5tTeD__qb72ocjkoMwUbDCfnb3mKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس هم اکنون
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/withyashar/16719" target="_blank">📅 01:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16718">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b07c5ad9e.mp4?token=IebQeDvIFDVTexYiDi_eQ0hArQFeeXi4p23vWM7tVYVLsZjafD6ZOD51z_IE1ppDYeyZIPrNzGoE0RJUAImi1cwEQ9e_WHyQgF0dsv0dox-r539KUY0Gj2WglIm4scL7ri0ClbVe4O6U0RkmwXfzmZhkgISJ9AzgItpSW3UzHaOg4rfKNu067mUHkWTY8r5U8vj16khAEQyUMSDUE5CHo8-7OMTVHhHk9_Rj-OWD-qs5lLXg1DZmyWhpa2AgbRmLW9gq3VB1t9qm4CS7QS45v8GH_dXJolJaiSW-trYX-ldX41wB4eOnrpFnqwtsq7eN5mhv_SwK2nY8pgjdWYBTSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b07c5ad9e.mp4?token=IebQeDvIFDVTexYiDi_eQ0hArQFeeXi4p23vWM7tVYVLsZjafD6ZOD51z_IE1ppDYeyZIPrNzGoE0RJUAImi1cwEQ9e_WHyQgF0dsv0dox-r539KUY0Gj2WglIm4scL7ri0ClbVe4O6U0RkmwXfzmZhkgISJ9AzgItpSW3UzHaOg4rfKNu067mUHkWTY8r5U8vj16khAEQyUMSDUE5CHo8-7OMTVHhHk9_Rj-OWD-qs5lLXg1DZmyWhpa2AgbRmLW9gq3VB1t9qm4CS7QS45v8GH_dXJolJaiSW-trYX-ldX41wB4eOnrpFnqwtsq7eN5mhv_SwK2nY8pgjdWYBTSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روشن شدن آسمان به علت انفجارها در پایگاه هوایی بندرعباس.
@withyashar</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/withyashar/16718" target="_blank">📅 01:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16717">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پرواز جنگنده های شیفت آلرت نیروی هوایی ارتش از اصفهان به سمت جنوب
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/16717" target="_blank">📅 01:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16716">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idLGvhhMl6VPTJng1M_iCnO2RbpbhYbdWbv5mVGhkhXzy44iDOW06IbE8zQ2lWkmRFeu93U7Cm9IbyBFL1Go4SNsSlO5DTU1dL0IP_EkxbXhO7iUPoP9AWXVDlMKRytQCFa5-uspjJjul_3tUP1Wywtr9QGIytQEByvc_bS1y7QL1uCMwkETna12IYeMYYOaDdW-7bmsTdOrtgBff5cyxgqqxMECJCgx2SIsjfqR_1DzlEd8h7L7YdV_bNeW8f3SJyI2dVP_i5uZ5Vma48E6_djAiTW63zwbIFlmk06rT09y1C1USOKTZFb6NztIDJ02uNuI51JbFdr1aDs7_Zpmkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون اسکله سیریک
@withyashar</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/16716" target="_blank">📅 00:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16715">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">فرودگاه بندرعباس که روز گذشته پس از چند ماه شروع به کار کرد، دقایقی پیش مورد حمله قرار گرفت
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/16715" target="_blank">📅 00:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16714">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">انفجارهای جدیدی در نزدیکی جزیره قشم گزارش شده
@withyashar</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/16714" target="_blank">📅 00:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16713">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">انفجارهای بندر عباس به قدری شدید است که پیامهای بسیار زیادی از شهرهای اطراف دریافت میکنم که این موضوع را تأکید‌ و تایید میکنند.
@withyashar</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/withyashar/16713" target="_blank">📅 00:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16712">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">همین الان بندرعباس رو 6 تا صدای انفجار بلند فجیح اومد
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/16712" target="_blank">📅 00:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16711">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">یاشار بندرعباس 11 انفجار رادار های دریایی اسکله رجاییی
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar
🚨</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/withyashar/16711" target="_blank">📅 00:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16710">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سنتکام:نیروهای فرماندهی مرکزی ایالات متحده، سلسله حملات قدرتمندی را علیه ایران آغاز کرده‌اند تا هزینه‌های سنگینی را برای هدف قرار دادن و حمله به کشتی‌های تجاری که توسط افراد غیرنظامی بی‌گناه در یک آبراه بین‌المللی اداره می‌شوند، تحمیل کنن
این حملات آمریکا در پاسخ به حملات ایران به سه کشتی تجاری است که در تنگه هرمز در حال عبور بودند. این اقدامات تهاجمی ایران غیرضروری، خطرناک و نقض آشکار آتش‌بس بود
@withyashar</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/withyashar/16710" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16709">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/16709" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16708">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سامانه های پدافندی در بندرعباس فعال شدند.
@withyashar</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/16708" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16707">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دکل زبون وا کرد
😩
@withyashar</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/16707" target="_blank">📅 00:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16706">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خبرگزاری اینتل : هشت بمب به یک پایگاه دریایی متعلق به سپاه پاسداران انقلاب اسلامی در سیریک اصابت کرد
@withyashar</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/withyashar/16706" target="_blank">📅 00:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16705">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">هم زمان حملات هوایی اسرائیل به جنوب لبنان
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/16705" target="_blank">📅 00:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16704">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">صدا و سیما: برخی منابع خبری از شنیده شدن صدای چند انفجار طی دقایق اخیر از محدوده قشم و بندرعباس خبر می دهند.
@withyashar</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/16704" target="_blank">📅 00:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16703">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">انفجار در جزیره‌ی هنگام
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/16703" target="_blank">📅 00:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16702">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بندر عباسسسسسس بدد زدن
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/withyashar/16702" target="_blank">📅 00:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16701">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مهر: صدای انفجار در قشم و بندرعباس هم شنیده شد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/withyashar/16701" target="_blank">📅 00:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16700">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سیریک زارتان زورتان شدیدددد
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/16700" target="_blank">📅 00:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16699">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گزارش ۶-۸ انفجاااارررررر
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/withyashar/16699" target="_blank">📅 00:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16698">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">تتر پروازززز  داره میکنه  ۱۷۸۰۰۰
1$ Tether = 178,000
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/16698" target="_blank">📅 00:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16697">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گزارش های بسیارررر از صدای انفجار در قشم و سیریک
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/withyashar/16697" target="_blank">📅 00:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16696">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">شروع شددددد
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/16696" target="_blank">📅 00:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16695">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">باراک راوید خبرنگار آکسیوس : امشب بیدار بمانید
@withyashar
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/withyashar/16695" target="_blank">📅 00:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16694">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/494c1afd8f.mp4?token=pI4Qm0-0-cR8qOCQ5qbU_9GuVJJEJcWu2iFRy72Vx8z3gFKfzjLl7fUqKEUd3-fucE2-KdJ_STscyrsP4LhlTeb0puC3WLWCr5EZbRYQawxtXiMo4rIFacOdIU9PvEkD-xYvn75ql7vUD8zHE2ojgcNUB9e2qLuKOGNxFV0w80yoieHh9Has690gMYYmLxXj1_2euIU4vSUpaUwdKHwWtPRnUxlYDRgPUkUY1xPSoyiiHsRe6OSQl8ZgRtb1JEn8ln3hWqG6F3caJOoYpp8lV-4246PFnUDEsNpy3CvWLUgxTnYhK2_fz963KJ88IJ6Pu_5G2F1rnYCwqv1VRLBhOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/494c1afd8f.mp4?token=pI4Qm0-0-cR8qOCQ5qbU_9GuVJJEJcWu2iFRy72Vx8z3gFKfzjLl7fUqKEUd3-fucE2-KdJ_STscyrsP4LhlTeb0puC3WLWCr5EZbRYQawxtXiMo4rIFacOdIU9PvEkD-xYvn75ql7vUD8zHE2ojgcNUB9e2qLuKOGNxFV0w80yoieHh9Has690gMYYmLxXj1_2euIU4vSUpaUwdKHwWtPRnUxlYDRgPUkUY1xPSoyiiHsRe6OSQl8ZgRtb1JEn8ln3hWqG6F3caJOoYpp8lV-4246PFnUDEsNpy3CvWLUgxTnYhK2_fz963KJ88IJ6Pu_5G2F1rnYCwqv1VRLBhOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک هواپیمای باری بوئینگ ۷۳۷-۴۰۰ متعلق به شرکت هواپیمایی کی ۲ ایرویز پس از پرواز از شارجه امارات متحده عربی در مسیر کراچی پاکستان مفقود شده است.  هواپیمای باری با شماره ثبت AP-BOI ظاهراً پس از یک سقوط بسیار سريع از صفحه رادار در دریای عمان ناپدید شده است.مقامات…</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/16694" target="_blank">📅 00:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16693">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">به ادعای رسانه ها دولت مصر با یک تصمیم سیاسی، تمام برنامه‌های سالگرد درگذشت محمدرضا شاه پهلوی شاهنشاه فقید ایران را که همه ساله در مسجد الرفاعی برگزار می‌شد لغو کرده است. ‏همچنین گزارش شد که از سوی مقام‌های مصری به وزارت خارجه این کشور ابلاغ شده اجازه ورود…</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/withyashar/16693" target="_blank">📅 00:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16692">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یک هواپیمای باری بوئینگ ۷۳۷-۴۰۰ متعلق به شرکت هواپیمایی کی ۲ ایرویز پس از پرواز از شارجه امارات متحده عربی در مسیر کراچی پاکستان مفقود شده است.
هواپیمای باری با شماره ثبت AP-BOI ظاهراً پس از یک سقوط بسیار سريع از صفحه رادار در دریای عمان ناپدید شده است.مقامات هنوز تأیید نکرده اند که چه چیزی باعث سقوط هواپیما شده است اما
برخی منابع تایید نشده میگویند پدافند آمریکا به اشتباه هواپیما را مورد هدف قرار داده است
@withyashar
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/withyashar/16692" target="_blank">📅 00:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16691">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گزارشات از پرواز جنگنده‌های آمریکایی در مرز ایران
@withyashar
🚨
🚨
🚨
کانال اگه میوت هست دربیارید و نتفیکیشن های پین اینستاگرام رو کاملا روشن کنید</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/withyashar/16691" target="_blank">📅 00:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16690">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCHOaivG352aoQJwV3O6ydmO7bdPePW6xQeHRFofyHEtdOl-Ci7J8K79Ou0zoHwJSPkEsJUdVn10QW112CxRx0q8PIjc5sz7-mdnHhwrZxV-0r69Do1WCjddLumhsVwN2tQp5kyyKqUwYU6fA9OZk5kqARKwaC3HwBbSg2gX_JjnBK2ROeeCHcGECM1uRMxuFOoy5hWlF0yMi95SOW8LPDMv7tX54xX1ZClXagNpusIrcrkctmBjSh1WGB-i1_GXpcKh7FiFJ5UCoSuANjWvX6ZGyXW7Rpqtn1T-QNCOmXiOTXIEFxPTn7SH2n7mvFxrdeNuC1llFI8Jf9XhOn5aIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از رسانه های رژیم در کانال تلگرامش اومده، آدرس محل اقامت ترامپ در آنکارا را اعلام کرده، که مثلا حمله بشه.
@withyashar
🤣</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/16690" target="_blank">📅 23:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16689">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گزارش ها از فعالیت گسترده ارتباطات رادیویی نظامی در سراسر خلیج فارس و تنگه هرمز.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/withyashar/16689" target="_blank">📅 23:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16688">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">رضایی:  دوستانی که مخالف مذاکره هستند صبر کنند؛ خود آمریکایی‌ها این مذاکرات را ازبین می‌برند
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/withyashar/16688" target="_blank">📅 23:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16687">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">فرصت ۱۰ روزه آمریکا به مشتریان نفتی ایران
در مجوز جدید وزارت خزانه‌داری آمریکا به طرف‌ها اجازه داده ظرف حداکثر ۱۰ روز به تمامی‌معاملاتی که قبلا فروش تحویل و فروش نفت خام، محصولات پتروشیمی‌و فراورده‌های نفتی با منشا ایرانی را مجاز می‌کرد پایان دهند.
در مجوز جدید همچنین تأکید شده است که ایالات متحده آمریکا از امروز (۷ ژوئیه ۲۰۲۶) هیچ‌گونه معامله جدید از جمله خرید یا بارگیری نفت خام، محصولات پتروشیمی‌ یا فرآورده‌های نفتی با منشا ایرانی را مجاز نمی‌شمارد
@withyashar</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/16687" target="_blank">📅 23:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16686">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نیروی هوایی اسرائیل برای مشارکت برای حمله به ایران اعلام آمادگی کرد
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/16686" target="_blank">📅 23:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16685">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e75ced6192.mp4?token=QYemZObaQLy-ySS67wP3LgDIE8I5O4WDTbxuwWi2U4aElTo3DIVq4U7jOLLkOxAHWP5ntOHyI7EioaoZ7iRMvxP3-WzMQw_2TNEqoo8FJ5CmxHx2BmBn1V_ERxsaxB57WKOtkhW0FugZntwssJQgzCKg57_ZC7ZYVj9oeC84M6uSZpJTxwhMW83WYheLYCFRk8An_WKI8pXyp9ZA9emLkHX7GIbzPOxMT-79ZGwQ3FJtKQpLVGsuZA0NjcgZbBD2g2OF32Te3IWqnAQ_iV1nKs-WnIXMnbDE6dpuKOtyMyqI2DdG8gsJ6rdmURF0qCiYSNYjyl6stI4BbuRHsvgxrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e75ced6192.mp4?token=QYemZObaQLy-ySS67wP3LgDIE8I5O4WDTbxuwWi2U4aElTo3DIVq4U7jOLLkOxAHWP5ntOHyI7EioaoZ7iRMvxP3-WzMQw_2TNEqoo8FJ5CmxHx2BmBn1V_ERxsaxB57WKOtkhW0FugZntwssJQgzCKg57_ZC7ZYVj9oeC84M6uSZpJTxwhMW83WYheLYCFRk8An_WKI8pXyp9ZA9emLkHX7GIbzPOxMT-79ZGwQ3FJtKQpLVGsuZA0NjcgZbBD2g2OF32Te3IWqnAQ_iV1nKs-WnIXMnbDE6dpuKOtyMyqI2DdG8gsJ6rdmURF0qCiYSNYjyl6stI4BbuRHsvgxrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضایی: آمریکا به دنبال عبور دادن ناوهای خودش از تنگه هرمز است
آمریکا در عمل زیر تفاهم می‌زند.
@withyashar</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/16685" target="_blank">📅 23:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16684">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دستگاه های اخلال گر GPS در سراسر خلیج فارس و تنگه هرمز فعال شدند  حتی تا کیش‌ کاملا در سیگنال قرمز فرورفته
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/16684" target="_blank">📅 23:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16683">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">خبرگزاری آکسیوس : آمریکا امشب در جواب نقض تفاهم نامه توسط ایران و حمله به کشتی های باری،حمله ی گسترده ای انجام میده.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/16683" target="_blank">📅 23:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16682">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بعد از ۳۷ سال و دو ماه از آخرین سفر خارجی علی خامنه‌ای که در تاریخ ۱۹ اردیبهشت ۱۳۶۸ (۹ مه ۱۹۸۹ میلادی) به کشور چین انجام شد، در زمانی که وی در دوران ریاست‌جمهوری خود بود… و همان طور که نشان دادم با پرواز بوینگ ۷۷۷ ماهان در همین لحظه لشش از ایران خارج شد و…</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/16682" target="_blank">📅 22:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16681">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a4d715020.mp4?token=MzeBzCp9FoTNwq6TevzPRTH4_ghOWSWpC9iLWG7tHBpfkT0S4duF2otiXdYMKofVfUaU9Jh1RsBjGiiUweU7UsD45ZuZq89JeggjbSBln9Qv8NvtWw1NPEGmgvxVxSA3yQXmurnHasGbnqsjcQw-wJEeGd3G30K6ZxPhFWw6F0v-uitB4087orqsnWKn8mllph_RjqfvtLmXiGQiWnApIsaY_HmIFqAvJp1TIfK9G9lUjuGfMaIDEpsGQhm54AX27XRffAeRZZReXqp6vOZpcVgNbMqJNvtjLDj58YemzLP6GUd1QWzd2wCd8D2edXyJCjIJ8PwkQ0Y18aTtmKAwkwRRS3p-aFq383egHhEVgupQL7tPKurjikIUI29OdLU-RcW0EYmSkgvBM5bd9koIeiAu9LQ5Hdxj1v_NDwoHNSlbgvBnK8vts8mxU9G59sCAj5NUliKU2xMJfPXZ9vqNDVwTcsLeipgUifCLFUg-X4t_B4eRa08TUjDOQXyosk8ZKnBXd-gP1SGa9w--RhHWPmOYK-k73QInts1oHA_aWTdIirSLhEaRC4F3NjxhIn-SlWbCDH4jvaVudsLicsxnf6MZ06YYd3UfhigzLRjVkI7ud06X3eY9TzYtJJFht5EbgncMv0lArQ4_HlQG6icR85h56M3T7VId_iRSokmRwRE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a4d715020.mp4?token=MzeBzCp9FoTNwq6TevzPRTH4_ghOWSWpC9iLWG7tHBpfkT0S4duF2otiXdYMKofVfUaU9Jh1RsBjGiiUweU7UsD45ZuZq89JeggjbSBln9Qv8NvtWw1NPEGmgvxVxSA3yQXmurnHasGbnqsjcQw-wJEeGd3G30K6ZxPhFWw6F0v-uitB4087orqsnWKn8mllph_RjqfvtLmXiGQiWnApIsaY_HmIFqAvJp1TIfK9G9lUjuGfMaIDEpsGQhm54AX27XRffAeRZZReXqp6vOZpcVgNbMqJNvtjLDj58YemzLP6GUd1QWzd2wCd8D2edXyJCjIJ8PwkQ0Y18aTtmKAwkwRRS3p-aFq383egHhEVgupQL7tPKurjikIUI29OdLU-RcW0EYmSkgvBM5bd9koIeiAu9LQ5Hdxj1v_NDwoHNSlbgvBnK8vts8mxU9G59sCAj5NUliKU2xMJfPXZ9vqNDVwTcsLeipgUifCLFUg-X4t_B4eRa08TUjDOQXyosk8ZKnBXd-gP1SGa9w--RhHWPmOYK-k73QInts1oHA_aWTdIirSLhEaRC4F3NjxhIn-SlWbCDH4jvaVudsLicsxnf6MZ06YYd3UfhigzLRjVkI7ud06X3eY9TzYtJJFht5EbgncMv0lArQ4_HlQG6icR85h56M3T7VId_iRSokmRwRE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از ۳۷ سال و دو ماه از آخرین سفر خارجی علی خامنه‌ای که در تاریخ ۱۹ اردیبهشت ۱۳۶۸ (۹ مه ۱۹۸۹ میلادی) به کشور چین انجام شد، در زمانی که وی در دوران ریاست‌جمهوری خود بود… و همان طور که نشان دادم با پرواز بوینگ ۷۷۷ ماهان در همین لحظه لشش از ایران خارج شد و به نجف رسید
@withyashar</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/16681" target="_blank">📅 22:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16680">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خبرگزاری وای نت وابسته به ناتنیاهو از قول
یک مقام رسمی آمریکایی: آمریکا مجوز فروش نفت ایران را لغو کرد.
@withyashar</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/withyashar/16680" target="_blank">📅 22:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16679">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/withyashar/16679" target="_blank">📅 22:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16678">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رسانه های عبری : به تازگی، شناورهای نیروی دریایی ترکیه به تمرینات نیروی دریایی اسرائیل در دریای مدیترانه نزدیک شده بودند، مانع از پیشرفت آن شدند و به گزارش‌ها، تلاش کردند نیروها را به سمت درگیری سوق دهند.
بر اساس گزارش "اسرائیل الیوم"، با دستور فرماندهی، شناورهای اسرائیلی مسیر خود را تغییر دادند و از رویارویی مستقیم با نیروی دریایی ترکیه اجتناب کردند.
@withyashar</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/16678" target="_blank">📅 22:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16677">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/022cfc7780.mp4?token=Ndn1rWW46GVeSSOR5d1340Y41QIwWqSWpMjw2I_BW_jovkqp_wokNXayHNCMwXS-5izeSelIBGfPbhh6T-iLep0YmitBnr7razqKvbrnk-e_WiGPQMEf5aREFqNuLUPjtACJjflglzwzHONoWt6q8fCLA7DlCqiC5aW711hDjhUoXhxcqYputeHKtHxi9W3efi5G76BAHZTXNCosIym_tO87Atjnk3A7XdTScawg5qqDyKQbFwUyuWVvR3Iej9JbTCn5DbjRNuccfdZUTFU9Gw3e5gEdp1ayPHBpKdCxDltNe-y87uDybrvaTDHP9INYcJt4w0bkqu70pFbWdeAqPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/022cfc7780.mp4?token=Ndn1rWW46GVeSSOR5d1340Y41QIwWqSWpMjw2I_BW_jovkqp_wokNXayHNCMwXS-5izeSelIBGfPbhh6T-iLep0YmitBnr7razqKvbrnk-e_WiGPQMEf5aREFqNuLUPjtACJjflglzwzHONoWt6q8fCLA7DlCqiC5aW711hDjhUoXhxcqYputeHKtHxi9W3efi5G76BAHZTXNCosIym_tO87Atjnk3A7XdTScawg5qqDyKQbFwUyuWVvR3Iej9JbTCn5DbjRNuccfdZUTFU9Gw3e5gEdp1ayPHBpKdCxDltNe-y87uDybrvaTDHP9INYcJt4w0bkqu70pFbWdeAqPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین
تصویر از خودروی
ن
ع
ش
کش که فردا قرار است در عراق تابوت خامنه ای را حمل کند
@withyashar</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/withyashar/16677" target="_blank">📅 22:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16676">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">طبق گزارش ها یک نفتکش بزرگ دیگر  نیز مورد اصابت موشک در تنگه هرمز قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/16676" target="_blank">📅 22:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16675">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">قطر معاون سفیر ایران را احضار کرد
دولت قطر در پی حمله به یک نفتکش قطری در تنگه هرمز، معاون سفیر ایران در دوحه را احضار کرد.
بر اساس این گزارش، قطر از تهران خواسته است فوراً به تمامی اقداماتی که امنیت منطقه و آزادی کشتیرانی را تهدید می‌کند، پایان دهد.
@withyashar</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/16675" target="_blank">📅 22:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16674">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/16674" target="_blank">📅 22:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16673">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">داریم به این لحظه نزدیک میشیم. گفتم از الان داشته باشین، سیو کنین، چون اون موقع ممکنه اینترنتتون قطع باشه و نفهمین چی شده.
@withyashar</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/16673" target="_blank">📅 21:54 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
