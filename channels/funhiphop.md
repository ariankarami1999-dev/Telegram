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
<img src="https://cdn4.telesco.pe/file/sR-SzQqCtzYcj71W3SzNITm0nLbuOq-mShKevBrRCzdvWqqd9lBeMjGp2gSZTpmD8oEdFduwm4XOH7rWZScC-5bagJFBQcJmda7QtlDuIgPBSrU6BKMQS94IqJiy1duOfR4gk-2E6ps4X7RYJ8B6awimcAY3l1w5HpK2sEZFXf6hImzuxmv2-y2ElbAvHSBu5I1J4gOfdcxGlu8QCE_NVP5iAG6O9drlUA0aytDLFh-Ys6HwYhLciK-KKraWqBVx_JxucONUFIjGwwWhr6tkZ23bdvzzWLqM4fh7rgz_IHCpDv93WYAiVWNb8aOdhCqNYf66h2t5jcXuOBOfobf87A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 224K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 03:08:39</div>
<hr>

<div class="tg-post" id="msg-82807">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دلار ۲۱۱
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/funhiphop/82807" target="_blank">📅 01:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82806">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مجید بیدار شد داره از خرم آباد موشک میزنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/funhiphop/82806" target="_blank">📅 00:58 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82804">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مجید بیدار شد داره از خرم آباد موشک میزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/funhiphop/82804" target="_blank">📅 00:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82803">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اسپویل از چند ساعت آینده:
ترامپ توئیت میزنه میگه قرار بود با اسرائیل یه حمله بی سابقه کنیم ولی دقیقه ۹۰ جلوی حمله رو گرفتم و ترجیح دادم مذاکره کنیم
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/funhiphop/82803" target="_blank">📅 00:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82802">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مجددا صدای تحویل ذرت و جو آمریکایی در لارک
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/funhiphop/82802" target="_blank">📅 00:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82801">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">#فوری
سازمان ملل:
این آخرین هشدار ما به تمامی کشورهای درگیر است. اگر دوباره دست به اقدام خصمانه علیه همدیگر بزنید به صورت شدید ترین حالت ممکن نگران خواهیم شد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/82801" target="_blank">📅 00:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82800">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اونایی که میدونن امشبم جنگ نمیشه ولی الکی وانمود میکنن جنگ میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/82800" target="_blank">📅 23:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82799">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تسنیم: حمله آمریکا به لارک ۲ کشته و ۲ زخمی داشته
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/82799" target="_blank">📅 23:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82798">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">پرتابگرهای موشک کروز ضدکشتی سپاه پاسداران انقلاب اسلامی در لارک هدف قرار گرفتند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82798" target="_blank">📅 22:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82797">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">آمریکا پایگاه سپاه جزیره لارکو زده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/82797" target="_blank">📅 22:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82796">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کوروش یه چنل دیلی زده همه رپرا رو توش جمع کرده
بعد یهو یادش اومده عه آرش سرطانو نیاوردم، رفته پیویش لینک بده دیده عه لست سینش لانگ تایم اگو عه باز یادش اومده اصلا زندانه طرف، پیش خودش گفته خب چیکار کنم حالا؟
بعد پاشده زنگ زده به زندان و صداشو ریکورد کرده گذاشته چنل.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/82796" target="_blank">📅 22:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82794">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">می‌خواستیم به ماشین ۲۰۶ برسیم
آخرش به دلار ۲۰۶ تومنی رسیدیم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/82794" target="_blank">📅 21:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82793">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_2hjOrP_jxlcRLl_2tuP1i_pdlBR6w9e53_GWWiKwx4DOR81bv9i5Src8sc66XC70d34zYvL5upLKLyy14TzfWxlfN5UXGNsD_XfY7xd7r2zyXube66uy5p848YScqpc2BSBCdK5zj4RtJt1AYqziicqzRlnOwn-kI4ha2YzAkZRbK1SSU46v1D81hbGyIHgm9GARmokAci63snBYJnrPMjhkwZWCqTjpdJiyPatpkx59d7ceFaVE21tHMAwa1eakkgrhn_SU00SEq9SrSF5lxPB0TufUZxJMOsUTlS7PVSqHFE9htVzt3bDrx9uMQSh3jj1jBlglHx0AfAXsI-vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حافظه تاریخی چرا نمیرسه به قسمت تجاوزا محسن نامجو، بابا خیلی عقبیم بدو.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/82793" target="_blank">📅 21:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82792">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Gharibam Bahat</div>
  <div class="tg-doc-extra">Danial Moghaddam</div>
</div>
<a href="https://t.me/funhiphop/82792" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/82792" target="_blank">📅 21:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82791">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ogzz52SxH-JhILr7r-dyO_eWYdqG4TUURZGkP5kUXnYuG-WODRePBRnP9hQ4myoXjK7heR4302F88iyXnx6vooxBzlF6Uzo9WrDA2grHtxzLjGhn91mJJo9W6gy0Wsejg67ph6722SVLB6ZDcjS8Og8VWDJEUdFbEy7NJY-eNadfDdyT0pRDq32l5W0jE1Zg9Shs5oXp7GhODcE1ZDVzlkdp9saWPxEcS9ztk23xhXgbwT5jeTA2kgIMdyiWK0t8HrHaM-1za37-jBgkDDDsl8euzPdbz_H94tQyBroULsrQq0UBnjzRMjJDKNM0UqYhIdOS4_PUr_sJtPP8TFPL8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آهنگ جدید دانیال مقدم به نام غریبم باهات
از آلبوم خط مقدم منتشر شد
https://t.me/danialmoghadam3</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/82791" target="_blank">📅 21:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82790">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">الان می‌تونم به جفری اپستین برا خودکشیش حق بدم.   @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/82790" target="_blank">📅 20:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82789">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d776d17fe4.mp4?token=me_0QRzGYlPxPFSMwG-T7NA_rCAjSkJzqvb54YZ0YJhfEuUBpq4i6AjgR4liVEzPzfSaBRXeH9b8dM7MW7ctaLj5aHJ-jBtZnSFG9X56CPiLEFstcJoqhNMEOtVrYFMLs4zI_e2VYDAoBRYUoGuX1XvHQ5ZJrpjarrYgIj10lzBxc0ayP3HSaPTKHQAjJFtRRNI9Y6UBObkll78YJewGrO1MaGbTmUHRFhdBNyQL_ohO_X0NR0GmPeVUdJHec_xwnh3erkYVj4H4ANbU1k5rHYmh55QzJJc0GwnDzqmuWqr5D4_2NY4CJCMExobmuMQ2y4y9G8SALc8Ei10pWoEIsg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d776d17fe4.mp4?token=me_0QRzGYlPxPFSMwG-T7NA_rCAjSkJzqvb54YZ0YJhfEuUBpq4i6AjgR4liVEzPzfSaBRXeH9b8dM7MW7ctaLj5aHJ-jBtZnSFG9X56CPiLEFstcJoqhNMEOtVrYFMLs4zI_e2VYDAoBRYUoGuX1XvHQ5ZJrpjarrYgIj10lzBxc0ayP3HSaPTKHQAjJFtRRNI9Y6UBObkll78YJewGrO1MaGbTmUHRFhdBNyQL_ohO_X0NR0GmPeVUdJHec_xwnh3erkYVj4H4ANbU1k5rHYmh55QzJJc0GwnDzqmuWqr5D4_2NY4CJCMExobmuMQ2y4y9G8SALc8Ei10pWoEIsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان می‌تونم به جفری اپستین برا خودکشیش حق بدم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/82789" target="_blank">📅 20:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82788">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e9b9dca48.mp4?token=iEX93fla0inI6BqyMnUBq9TtNhz8rbTersk3YiimiiwKfTbvDLRgJ1N_BrizOZkoC_obLKJOJ3o3TLlGXQgWyNj4N6XQNevPxqhgGgYGKWlOitMKGVBnQuibvEqvX-2Ul4z2huwEDM6nZ4_I-nZYc8LPKPqybADNlgfUhhgsWvO9d0uFlzGpyfkpGHKHwlenBeXUaQP8AOO5vr6vGMezC3DqvvUaAzzHnIclQzRTwxI3OhMvOLOr7iwO4bZ1GVYzQGFvM_wXm6CMhZemdL69Mc3oRTQvGv4bh66Q6yW6SXWXE1dscAHiQgGgz2qNpkEB8IrNU7dca7yyvmbYJjfWPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e9b9dca48.mp4?token=iEX93fla0inI6BqyMnUBq9TtNhz8rbTersk3YiimiiwKfTbvDLRgJ1N_BrizOZkoC_obLKJOJ3o3TLlGXQgWyNj4N6XQNevPxqhgGgYGKWlOitMKGVBnQuibvEqvX-2Ul4z2huwEDM6nZ4_I-nZYc8LPKPqybADNlgfUhhgsWvO9d0uFlzGpyfkpGHKHwlenBeXUaQP8AOO5vr6vGMezC3DqvvUaAzzHnIclQzRTwxI3OhMvOLOr7iwO4bZ1GVYzQGFvM_wXm6CMhZemdL69Mc3oRTQvGv4bh66Q6yW6SXWXE1dscAHiQgGgz2qNpkEB8IrNU7dca7yyvmbYJjfWPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سناتور ارشد و جنایتکار و نادان آمریکایی، تد کروز:
من بارها از ترامپ و دولت او خواسته ام که به معترضان سلاح بدهند، تا مردم ایران بتوانند با کمک سلاح، کردها را مسلح کنند و اجازه دهند معترضان این رژیم را از قدرت برکنار کنند.
هدف این نیست که سربازان آمریکایی وارد عمل شوند، بلکه هدف این است که مردم ایران این کار را انجام دهند.
تصمیم‌گیری درباره اینکه چه کسی در دولت ایران باشد، از وظایف ما نیست، اما وظیفه ما این است که بگوییم دولت ایران نباید توسط یک حاکم مذهبی افراطی اداره شود که از آمریکا متنفر است و تلاش می‌کند آمریکایی‌ها را به قتل برساند.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/82788" target="_blank">📅 20:36 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82787">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBaGpYgNYbzloYa2rEzmIuosj7HMVatB_ezy16LapJUiO3kpVQPK-7rTXC3gM5_0nZuzJoGi3aQORvZRbkMwPwL679JCCuq6LBKCv46kBHSIOIIACcn8O84Ghoa7AfnlNMLcYbzIWSTHdcDLqoGTAp1B1a7DgRDVj7yoj88LS4udC6DeN3HygmunAo3hMhigUnr7LYSrRCvW5RWmZW2wup07mmevFYxukjfffG0gn8-TQ-NKCGA3c1Tnw9geW3akYgT6r3RV2iP6QXOGkn27MIvQDvRBrIjJQAllEVC7HNKpjVndTEgszYwlgFX1WKqxs186GTObsBa-3nW8i8HHJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/82787" target="_blank">📅 20:14 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82786">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKavJN3fDuKr5jG13Rf62VCs6edx4HKvyvDhj61mUVpioCFy7jSJDij9UWUjJ0jYj5Zn6UyGzhC5sUVWvPzEJQhgQh4I09pZKlEdk8Aa13Zt0KfsiHk8ZW4-Jm1WfvU-YjA9kbEARFUUl12t_w5abh0UYNx7US1MW6bTjouxudCGXFdjR-n7Ic00UZTJCmPt6v7NKSSu1bWhUapNk797n2sSkz6UZY2Ktfhjg2FCi4MIfZ5-aUECJ82yiti7eoMmrKuQH8oCcPJNGp6ZQS2CGBqL3g31cJI4Y4SnwKkyP_18e6cH21V2N27pSkIpPYflbUyTGFpamsgH8lYGaMEBTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زن‌نامجو: به بهانه بقالی رفت بیرون ۶ روز گم شد بعد دیدم با چمدون من ایرانه  مشتی حداقل الکی میگفتی میخوام برم مسافرت  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/82786" target="_blank">📅 20:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82784">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OR5Lla2gFtvaVuifLjAybxEENIdJMFnQVIUMnWEMmvdzdowTFfhevxQKxacgyatBb-VWlcw0cbqO-K0csXnwVTh9rk0LT4azLrFJTEt78uPHNnIYvIeoXci1k6ONczNWm16TJskquHwTfhsQOXBgpDwGY9Ti90TrAZTOaPNNB6OF52tdf3OW5S028-PEShxwvuc_8uKxCvB251jJIbOLPAWqkjukTiD5sc2_CEWIcdGRYwNCAF3x61lVYvigrpVGxQ27E93kjCt1yZ1AebxrZhGnWzEAQtSh0fKYD0mN10CYlv4F2CLWGS-Z8b43JXbr4tEaE8UgxAUJxpGH7URJkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q57ZZFOZG1SNTbliRXTuJSGyzkPj0nmCaQTNvI0PbGIyqxBWCJFbKGCxl1BzWwETk263NjT6nTlk4VKsjP7e8ukU8HgbwgZnBZj8NJFr6p8P1Lq5K-PYI-WeJEIUJ3csuAtqJ2-DZ92vhN51fL8AS9rhhbXVbcR5QqlG0c6Nlxyogqme0fRfzk8S4AwsfagTrLP6sBb2OkeiZCRqK3ZfQYaJv4OaHD8eTeiwNQebbWJliudabM5bVPxmPrDK_AkoCLkZQCOcEvoSuqvfUFeE_ABRZKSwk3FCbprBn0DQWG8zfr9ME_kg0V6KV4w0uBPDggNlj0syq-aGv8gpE7VxZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتظارشون اینه مردم فتوسنتز بکنن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/82784" target="_blank">📅 19:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82783">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/my5iw2VYG7vuwJG-xcJ95WlyGmxqRh8wBXuD1b2667ukpLtuRG-LOr-FTQpF8xxuREpu8Vin2cfPFHvAfYRAZ7d6GTxlR5B510cyM3AGEyzM08WC63knmdMKnvb8ziGgg-st4DzzzHbPGIHhd5lbhYOiPngF1kjssUQE8mWs_9qBnPzYWfz6pcEnNxDCA4GtLi0rnyOa9eIJLKmEkl3vgLZUxKoIfJFIv5MnFijLfcd5ITQGXiEctVY7uFNP-24hLkPQOVcoHLRmt0Afua-u4g-NNHu9fY6WRLzK5l4ssbVTbf_qSA43Cd3_cTCxbJlPYRWP8Plky5fN1XlUnoQZOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرگوسن فک کنم تهش تو همون الترافورد بیفته بمیره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/82783" target="_blank">📅 19:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82781">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dATYc39OJbP7DKql9zJb0uIlh8tNHX_zYN7zPbOT65uptMA8qxAoJuNxL7vYfbARi52Wj9AC-_fJodSlmD5SMJPqybywHw3hpNFboWkF3gpSY1ewa-h8LZ-T31T02eTCMVkYZTg5RMcGCuebo33CZvrutoqMkvoOv4IyiV7VaGYF3jgptCjbc-d30CHp4HCpkGEzBBWDjQKihrgQSSFjA8Vnipzz6zsgpWFEMYs7_zTirmpVCEx42pWYznG0jhKo9wYG7C8cGzAkJXed0CLGc68Y8TALPe05jgB380lc8zCj5Cwbwvz8gu-MLPcII4bRqBkZM1yVbovIZ2MER6zf3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v8jIZ7ud2GTRaT8E0LjqzXEFlRPV87XeSjGolXw9Yd45eKHh0dY6IfTOa7w4NphX1LPPie-4VsOjCASYm5V8F72t9uWgYa3kSl4RIqFj4ZlrNFq1IouiLvZTQoND4IDf4NonJyfCC9GdlPWp3yIyxrh10E6TgAMwyX26Np4KAIsGYfJkgkjsRGJIgbRvt_qFoPoC7FTpD56SzF92vU8VPpk_RbcgOm1uw4NmnlsB4egTFqCwcFp2z0k7oqojUUlc7_hawhD8hzpUwnuJEoSE6B58tKgWyONFh6dqFBv-I68cqg9b-nPAVZruZmbnoNykhgR65VP_LSxAiYU3gRbsqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حاجی انگار نه انگار که یه مملکتو بگا داده و الانم تو یکی از امنیتی ترین زندانای آمریکاس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/82781" target="_blank">📅 19:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82778">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">کی میخواد این فصل جلوی رئالو بگیره</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/82778" target="_blank">📅 19:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82775">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">انقدر گفتن تحریما تاثیر نداره
اولین تاثیرو روی رپرا گذاشت، همشون دارن بلاگر میشن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/82775" target="_blank">📅 18:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82774">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmYRpJRX4ZeMsCngFbgxPsq1BGgbY3H48QwwdFYa3964V07SGIwSLEWcp5tndjkGeEHv1vzR80BjE7g1yF3bIsKoftgMxigLquYg2cv-mc3ahmBpu2s5Qod5t14j7keyCcqTK0S_lt2nqKhItlMHCIMoS_CedKz1LZJaJsDwPelJuaoFi5z_DNfIk49x4q2zIsdCQ0_Aoek4-PEz3JSaHo7FDMBERQCJCNNfzXu__ydmQzWnbZQFxdUXK8or5Ak0MQTUuQjJETPDVdeKlaKuZrc_f3Y_UEiqeENP93p1oHIicfYQfMMelKQTkQhcH_Qw2TzSeFFTs_8GBS6ziqcFtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژابی بال و این حرفا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/82774" target="_blank">📅 18:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82773">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJIxUYmkIGbdhX3sgB_Pk9cl_6gW1zTFD3kWLJmKKDZzvb8BrLEY3GZj3ISBljU9EQa5m49iEsq31StN9nuYpU3WUYZcmn-GpKWmuUt2AeabpBADS0ZS3Wv4j5e-Lg73sbdcv4NxDe_G53olGWefdud6l6HfUAES00spwk-T3HWJq1PITfKRZrAPvP8jBlg06rRTegsL10iPFEzyQbZOgfmQS3odUvcmsBpe0FRJfAedWFQ3b6AZKqlYPYuDk2Ae_K6_5-3tFRB9_tKXQlwMxi113xbUgT50FLupEotpyQdnuvKJjjaCaxUPyZNCzbNQBBZMwnuSzrvuTk9sMI2LqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال داره انجام آزمون تافل برای ایرانی ها متوقف بشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/82773" target="_blank">📅 18:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82772">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pj_QtWwwFXhlso35yBpq2m0sb0a-9BJB1NknX3RiN1Ooev9Mfdp-CgaEDTJKMcmZNR_fTgi2b3mINbUCa8qnto5SGY77F325zidqAM0Hon9y8pXLc0nwAN2R0AQ9tfQUEvS6wJu0_0p-10mLyoSOU3185JJqsAljAww4FTAe575JtMCJVQPMH5H8kI0TZaimDAC8zcrmoW6sf5jseSkPlaaP5COgYQiUrSrJnsYejxkq6b-iREk_bw-XUvyfHW6hLU3PCZ94JWoiXzGE-j_r-OIlhjifXDYyPPCPn78mz-5t_jdp4GJVjcWDmr3XFepqVq9bsifhI3IP6SAn2QkPvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
مجموع جوایز نقدی رولت زنده
🔘
🔥
با ثبت پیش‌بینی در بازی‌های رولت زنده جایگاهتان را در تورنمنت ارتقا دهید و سهم بیشتری را از مجموع جوایز ۱۰ میلیارد ریالی بت‌فوروارد دریافت کنید.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/ROU
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g8
💻
@BetForward</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/82772" target="_blank">📅 18:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82771">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بیگ شگی بود خودش ویدیو میگرفت میگفت بیا پستش میکرد، کپشن میزد پول رپ پارت ۷۲۷۱۸
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/82771" target="_blank">📅 17:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82770">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">شاهی به این دختره شماره داده بعد بهش همون روز گفته بیا خونمون  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/82770" target="_blank">📅 17:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82769">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">حاجی چرا خودش ۵۰ دوستاش ۱۵</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/82769" target="_blank">📅 17:38 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82768">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAri</strong></div>
<div class="tg-text">منو ب چشم بیزینسی های کنار خیابون میبینی؟
۵۰ بزن بیام</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/82768" target="_blank">📅 17:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82767">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">شاهی به این دختره شماره داده بعد بهش همون روز گفته بیا خونمون  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/82767" target="_blank">📅 17:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82766">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d882fddf5.mp4?token=Eia3GMsQziFcuYD2WjDFWJkG5-TJr7RZERIvMUfuJ7xWA_8EIX645a6KSfcJ5cT6g5u7VLI1_xIaceFAhz9FHWd2WlWMhfW8MvBmdK_C2rHhjMI1DoZhhxb568qDUlYAQzX0C4hegSntXRKxmzBi_FwMffXk2SH74F62_2XFttyWCzilDSHQL_lVc1-HhpBOltOYHTN7T55ARiUni7FsaCjD7V8ZxmSBx_1Ez8jyam2LTf28fuRO4jCqUEY6zRQXm9foutY-qJcYcZNsvyn-7W3uuJ-XnjK3zPxgwrInKfbtcxP8oAWA1bQiX0ZSKzS-WJOca44QHLlxq4x4c5yGCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d882fddf5.mp4?token=Eia3GMsQziFcuYD2WjDFWJkG5-TJr7RZERIvMUfuJ7xWA_8EIX645a6KSfcJ5cT6g5u7VLI1_xIaceFAhz9FHWd2WlWMhfW8MvBmdK_C2rHhjMI1DoZhhxb568qDUlYAQzX0C4hegSntXRKxmzBi_FwMffXk2SH74F62_2XFttyWCzilDSHQL_lVc1-HhpBOltOYHTN7T55ARiUni7FsaCjD7V8ZxmSBx_1Ez8jyam2LTf28fuRO4jCqUEY6zRQXm9foutY-qJcYcZNsvyn-7W3uuJ-XnjK3zPxgwrInKfbtcxP8oAWA1bQiX0ZSKzS-WJOca44QHLlxq4x4c5yGCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهی به این دختره شماره داده بعد بهش همون روز گفته بیا خونمون
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/82766" target="_blank">📅 17:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82764">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/408e06015a.mp4?token=i5IO9zatR7KayWf5-mHSPnZB8AslIQLVVo5O1WApyQf1jXBgglo0dhVwMO2ZrhQSRu5ZroZZ_G5FyAht5VuHD9B75RfNt_Sy30PDgMybQWeMug52OIlUIJvl6wvIiRvuDVR1yo7fvnxnCg8WV0rJ1iCjAK-pKeledN7xKy0rrkwrKPTCYASicUt-xr49lat7Bc7-oCVqRG6n7tB6FbyzzBhC4NDhip9PENISj9R9s08x3RfgKcd3THd5--NbNA2S7XPrxXQGVzU-GOguZ4G0Evg5g9UGAmj4RMQwWfIcvoxeq2Dg4Zy_YMOeU5L8RGYh4UHjOxpKBK5ZKJiJfnCk2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/408e06015a.mp4?token=i5IO9zatR7KayWf5-mHSPnZB8AslIQLVVo5O1WApyQf1jXBgglo0dhVwMO2ZrhQSRu5ZroZZ_G5FyAht5VuHD9B75RfNt_Sy30PDgMybQWeMug52OIlUIJvl6wvIiRvuDVR1yo7fvnxnCg8WV0rJ1iCjAK-pKeledN7xKy0rrkwrKPTCYASicUt-xr49lat7Bc7-oCVqRG6n7tB6FbyzzBhC4NDhip9PENISj9R9s08x3RfgKcd3THd5--NbNA2S7XPrxXQGVzU-GOguZ4G0Evg5g9UGAmj4RMQwWfIcvoxeq2Dg4Zy_YMOeU5L8RGYh4UHjOxpKBK5ZKJiJfnCk2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقا محمود زد به ناموست
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/82764" target="_blank">📅 17:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82763">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ژسوس زیر دست فیلیک شاهکار میشه
بماند به یادگار
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/82763" target="_blank">📅 16:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82762">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بارسا نگو بگو سطل اشغالی سیتی</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82762" target="_blank">📅 16:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82761">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">الوارز میخواستی بارسایی؟  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/82761" target="_blank">📅 16:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82760">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYNwo1vfg-sQSLVeCkx8mi-O69NtQ99ysJTTZ282ruK5C8HAsOEJOqfUk62A1792F0RV0oBLFoTTSi1KChCE0h-hGZfmTqk_cTwDpfrsMdmkzwhRxALGx9031LRlqhg3YBz4s6oHWMr6G9RhO_Q1Nm9KjGIIf2CcgPBhdQhnMyKSHNg6D_EL_M0HhiwaIcfbLUeyzjRGJ8RCEqPtgmarlcBOGfgfRYWxJirJbd8rUKnqbLcfQsCZ-1mBAHRuVfWw559cQ7LTKCIlpIUimmin_n9yBjmDfzd5o8CcpHlbNEYbzJVzSjSC-HXukDnjR4DyDO3IOlaZJ7KUjrFhiD_Q5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الوارز میخواستی بارسایی؟
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/82760" target="_blank">📅 16:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82759">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2CaFOaf3PoLm_LesKgaSGqjrAIgPK9RJZ7ekNX5Ei_5TlVZVzTvNpzyjCMRsgnbhoFsqAueUfZoQZaXz90I0yVbbdXDIWcCbFIAbMhYTTqUFuLpUJSe9lzCruuaS4CnQyQ0YmJjV3qCCuARJ2OCjLCdj00Toj5t7H4On-AXxhBKalgR21gVy6dPEcBo_PnOk4O9fnwvu4rkuONt8xVc3z_YzE4-a6XkVfoAYD_0bOptst9NwzSQHrvcSbp3CVhHCGQuYFk7Nw-KaXX_l8-9wAUKXnSkyV0_Ev6wZZKVJJi_GkuYYgh49yvNFixwvLYgn3zVcwHglBZvydFSIb8Ltg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ته خنده ای مادرکسه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/82759" target="_blank">📅 16:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82758">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d256a2c699.mp4?token=Ghg4QJLSXwnywFnfz_eVfcOKOnwzsi6Y8z6kdXhvPt39AnKIwrHjvv-33zDk3q5pjgLXsxb02EKTbAeoaklRol2vfr_53lID_zWyfzYq-qhQjAYkNVrwotKsZRTbEXjcMEzGEJSQjQZHETl7M4ilne2s7LbFhTa7R8MJpKJqV8NyLmlsBrPFY7ZMG31_6ZBna9OxLrr1uSO8r-oRFOyrF-SgPrgt1nW029dhogj-LRyb-oJnnLQR1IfxkFIGusCSohRa8H6A8x7ZS5OFo5GOSTgPXsqOGW2wzSxg9Gw91alPGucb6nGQ2KfLpnNwWBUl-BAPxz-v_D7U_UClxkDwBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d256a2c699.mp4?token=Ghg4QJLSXwnywFnfz_eVfcOKOnwzsi6Y8z6kdXhvPt39AnKIwrHjvv-33zDk3q5pjgLXsxb02EKTbAeoaklRol2vfr_53lID_zWyfzYq-qhQjAYkNVrwotKsZRTbEXjcMEzGEJSQjQZHETl7M4ilne2s7LbFhTa7R8MJpKJqV8NyLmlsBrPFY7ZMG31_6ZBna9OxLrr1uSO8r-oRFOyrF-SgPrgt1nW029dhogj-LRyb-oJnnLQR1IfxkFIGusCSohRa8H6A8x7ZS5OFo5GOSTgPXsqOGW2wzSxg9Gw91alPGucb6nGQ2KfLpnNwWBUl-BAPxz-v_D7U_UClxkDwBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به خلسه گفتن چرا تیک تاک پیج نمیزنی مثل بقیه رپرا، گفته دیگه من سنم رفته بالا به من نمیخوره تو یوتوب دنس اینا برم.
حالا عادی ترین محتوایی که خلسه تو یوتوب میزاره:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82758" target="_blank">📅 15:36 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82757">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">حافظه تاریخی چرا نمیرسه به قسمت تجاوزا محسن نامجو، بابا خیلی عقبیم بدو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82757" target="_blank">📅 14:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82756">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-BCYbJv4wrDWmbE4h6Gnh3Q6s-pxaxq39d3q6Xs7LRcL-hnBJLfA7Oh8fAQnCOjgsGzyccvDWcNA_TArH-PkEDG4V3Pb4ReY-WH-C0mXZNqBR31jX6aCk3dljS2muBXLs0luuYbXEf-XwQy1byacfdlJP1pz3hwARglG0fEL2dbaH5OCPpvo1vCMFqIZO7MK1fqDecixg6SERPLgWAZpGlAL3EEZk1JyRSJqp_iz9ZdyDVQPgNoBjLYPaWPmCCbD-1yUbqAALIU0jlFhHaoJI1FpLizI27_9qimsvZH2qZ1UhcQkovU-BRtsUs9Qq8xqWvtf6zK3z47CtA3lxlzow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوریا ادرویت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82756" target="_blank">📅 14:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82755">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مدیونید فکر کنید این که مهران مدیری میاد مرد سه هزار چهره رو برا صدا سیما میسازه و توش عراقچی و دولت مردانی که رفتن مذاکره رو مسخره میکنه اتفاقی نیست
کاملا خودجوش مهران مدیری و نویسنده هاش تصمیم گرفتن اینو بنویسن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82755" target="_blank">📅 13:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82754">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">حکم اعدام برای ۱۰ معترض در اصفهان
شعبه اول دادگاه انقلاب اصفهان، ۱۰ نفر از ۱۶ معترض بازداشت‌شده در پرونده «میدان شهدای اصفهان» رو در مرحله بدوی به اعدام محکوم کرد.
بر اساس این گزارش، ترانه رحیمی، نوید الیاسی، ابوالفضل دادگستر، مهدی منصوری، احمدرضا سعیدی، مهرداد بوئری، محمدمهدی اسدی، آرمین غلامی، پارسا جعفری و مهدی جعفری معروف به مهدی خسروی، به اعدام محکوم شدند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82754" target="_blank">📅 13:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82751">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1de67eb81a.mp4?token=myWOv0w_ASMs_NvJSTq7Hi9zcSXlzagYckVDq8ue0LUSZqseBV-kFVUevUOTpvxs_4m9YeGSQR8W0arZ9GJYlaeFJqIWd5CK5fwn3cvLrLQoeF4tiEy7RxWWXLE-2Xjg-7DCUZ1Y7N5OHZoHVtFkwc2vqWghC69fO16JNyQ62ejKxsNttuNp3ik7m1g7wt-OG-JOEWHxbLdaZFRX3xeDFfKINwcyu6PcSIOxVC068OgFrnEmn-4O8TocwrZ6mykIWLTrvPNeiaUPMmunXwoBlqhqrp1UbG3Cs09-CA7048Dn3g92EFG3PTJDnAbe7bXDxQlsI3DLx1rTUDf7Nj0UUA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1de67eb81a.mp4?token=myWOv0w_ASMs_NvJSTq7Hi9zcSXlzagYckVDq8ue0LUSZqseBV-kFVUevUOTpvxs_4m9YeGSQR8W0arZ9GJYlaeFJqIWd5CK5fwn3cvLrLQoeF4tiEy7RxWWXLE-2Xjg-7DCUZ1Y7N5OHZoHVtFkwc2vqWghC69fO16JNyQ62ejKxsNttuNp3ik7m1g7wt-OG-JOEWHxbLdaZFRX3xeDFfKINwcyu6PcSIOxVC068OgFrnEmn-4O8TocwrZ6mykIWLTrvPNeiaUPMmunXwoBlqhqrp1UbG3Cs09-CA7048Dn3g92EFG3PTJDnAbe7bXDxQlsI3DLx1rTUDf7Nj0UUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سجاد شاهی تو پشت صحنه موزیک ویدیو ترک "تا ناموس"
حتی اینجا هم داره کتک میخوره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82751" target="_blank">📅 12:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82750">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSPEmxlHQ2WK0XM6d-XDwseMTJyc1E_atigkMUTKpAk-Qk5TL2WP0GhWbwPotIXkvFHL5x3wPx4Z-sGJeV2aub_8OUtrdAQWlawFBsxV70nPXC-fzc2_L4kP8zUnMpsHjJkK8spaTCnPK4wvqYOrw4EXgnEufT3yPePMm7LRA0o-z4Jij1UEnUHQQHSRjKYQLyWk57ApxTz3pPuDtmc0-xRqreg9oZ3SV48Fx0tG2K8C8B8wfqs2EhrIyE_pKh5tlkRZQtMSM7BwBXq0kTzmxpcFaVTZgs_rBrGp62Wiif3lASJKwujgsIY0XjBgkTTU7EyYq4sVTPqJqbDqu9Sjiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس پوری و مامانش
حالا سوال اصلی که دارم اینه چرا شلوار پوری جیبای عقبش جلوشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82750" target="_blank">📅 11:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82749">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">زن‌نامجو: به بهانه بقالی رفت بیرون ۶ روز گم شد بعد دیدم با چمدون من ایرانه
مشتی حداقل الکی میگفتی میخوام برم مسافرت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82749" target="_blank">📅 11:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82748">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59a6fa8663.mp4?token=Cu29eHzWS8nS2OYcEXyxrzCiyKAnZDenyXjo9NQi4DYzI0dZ83RpfpO9jb2Y6BLfIBmmfk5XdHf19o2ZSzle-nAo4hPPw-CTDByRScSr_vUgutT5v9TPRGARCEUNaAVBY4YigFVx93g9qjcdmj89VvBHL-UdB90uKWSXm23Wg4TfEmBCD1TpqPKErqcE6v7wRnMIO6HW40jryJIPUK_XjnmgvU0cwFNuRDCym8xAbiXpu0t3ufIdC__DMO7NZvSJL234rY4JkQYOEHVoBDX6uPqw2nFCGjjt-3Rf0NI7HWpWs1HiJu-kuR1lCWf4Wt8pfzyuqN-jsPVtv4wErYqfTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59a6fa8663.mp4?token=Cu29eHzWS8nS2OYcEXyxrzCiyKAnZDenyXjo9NQi4DYzI0dZ83RpfpO9jb2Y6BLfIBmmfk5XdHf19o2ZSzle-nAo4hPPw-CTDByRScSr_vUgutT5v9TPRGARCEUNaAVBY4YigFVx93g9qjcdmj89VvBHL-UdB90uKWSXm23Wg4TfEmBCD1TpqPKErqcE6v7wRnMIO6HW40jryJIPUK_XjnmgvU0cwFNuRDCym8xAbiXpu0t3ufIdC__DMO7NZvSJL234rY4JkQYOEHVoBDX6uPqw2nFCGjjt-3Rf0NI7HWpWs1HiJu-kuR1lCWf4Wt8pfzyuqN-jsPVtv4wErYqfTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخدا این آدم نباید رئیس جمهور آمریکا باشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82748" target="_blank">📅 11:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82747">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mU_HjQIG9-Ydh4-Tm2kHTKxCTiiSAjhVM6TLcx7gJnF6d_9Sn2-V3y9od5mBTbXPHXOS6Y5lgelqY_Eo1skTDF2j52pBC-B5mA-YwH7i8TVXSVn6y8oc4KXKz80Yllo2UdS0dHZqYginK0qSVV1apcRvqdW8pb2R-7NA1nrBhWCK9acuJCEKrgYlv7JcL0StTgLeQKUL1iqu-Q5vEzAcT8fm2Q_xMYeQVXXQQHwc1lox68LFjozRfqUWK5GUONAu6mwJQyMyPUYenShAMtzBzlxbD5efwweqdui4ntU84F4tMCL3C1TFaQchMn1eXKJJDbzAdk71R82ZFNgksKVaBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش این عکس حداقل واسه ۱۵ سال پیشه
از اون موقع هنوز ریشات در نیومده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82747" target="_blank">📅 10:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82746">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEnlzl-Jnl00w2nms88YGYx71xanz3xUbMriNY1kTjaJJZKOfSCIcyRUhOgwVepUNsu3yf9oonnanc2n9Eh4odxTJ62mLaVRTDCWpaw9Y3BrvDF0c_Y8XOmLyF9qCl3Tqx6MfNG1Gqwcc4rhlFbCuRnmfrSOj67H13NUH8-dyCtF6WjDy2vpcyqB_g7zh-vkQ5rc7n4C3PZpvIDxVV5vHxAOZFCGV0u5JWhwXLVui6nCZ7YkyaPk87c90wW5Bv57f3ndUDK2H_bZhz7zMJd9yn2n8YiKgYwV8NlHo2J-KtiXr7YaxW-IDCdigNdl-RI6e0J3806r61fHODv-IXZuHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
مجموع جوایز نقدی رولت زنده
🔘
🔥
با ثبت پیش‌بینی در بازی‌های رولت زنده جایگاهتان را در تورنمنت ارتقا دهید و سهم بیشتری را از مجموع جوایز ۱۰ میلیارد ریالی بت‌فوروارد دریافت کنید.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/ROU
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r8
💻
@BetForward</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82746" target="_blank">📅 10:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82745">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSHMeHJOpk4M01QA6y03nxX_fLhpoS1r4wpr1C6Tzck9L8YM61uspYreq1q0VnOZ0KXvxgnUxN5ZMewvfWyskL4MYFfJc6ffA9F6zhtzPHMjXtF8YmSUcLq5aVLnq06QTvRxpDwbioX_Y7DFD8RnjvD0o4VgVBtBptkda8OTp0yMC0l4T5_GUVlefw3izf5hcrEDgSZv_amYx07MiXF1vw9tWEbxuy5Pd-UAEVKni3ayzUW6crcrYkBwiTCPE7Lc6D19BvgEQ7MX60BQcQ5j-lwMhpIxTi-GdDGY7m1QzlCTr9fg1aH2sOYimMoDBC_SYPEZ6cyA41kQyuye9d2-eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82745" target="_blank">📅 05:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82744">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">جدیدا شات های کصلیسی بیگ شگی هم بیرون نمیاد دیگه، فک کنم دیگه دخترایی که میره دایرکتشون عشق میکنن باهاش پخش نمیکنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82744" target="_blank">📅 01:56 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82743">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_eilJB9luKUuCVEhCeNy4qLkMcS-LLhuemm_PEllkKmdVxpxRPfkCv6gJtSidHVJ20H-yJ4e1fKZ7jEKAgijIVW_YtDsSFWvIsy6IUZqmS8mY6GYdvBC5CoCLASXDTsbyrY_RYFz1QWaxrzy37mBkAR5jq_U8r9-PojmpKhGfpiI-MYEqlEu7M7NAmMLYEE2DIe2MlD_T4VVNNR75hxb9n7aPZCdDs9uQazPDb5piq391QPOCMuatuWCFadFIUx-KJdVcW0PEVsT1fu2B0i3Rb84AKy7pi5fkeiATCGavMq9jvWy4CtPIRJhcsOsvSIMzCC_WSaYbkKGQjZNZJTiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زندگی‌ رو دخترای خوشگل میکنن ما میدیم
یه یوتیوبر(aj king) میاد پیج دختر فیک میزنه با هوش مصنوعی و به نصف یوتیوبرا پیام میده همشون هم روش کراش میزنن و برای اینکه ابروشون نره کل چتا رو نشون نمیده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82743" target="_blank">📅 23:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82742">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11c692bdfd.mp4?token=N4EACDXBaTEeYKnrPQQjudC5d8HezN0-NDPh95lxzKrBTQNbSovZs5wSZ78xpK7-832x9rcdZCReyl4zCUgYoA_IDjMat8ZMA_3bIXA77OhOOstA7p7QMTxgQQOMzkPH1wnkP2R9kOSLpSMZcl-a79EPDV7tPuEGbURZXVreyMuBaQV4GmkPMub1WbFAo4HhnTolQUqEgu1M7_Qh8ymDpXze_J-4FZ48ydwi2mweTrK18I8o4GOP_qhEcstUWbmtf5wsYsHjiNEtN4FxUmTXI5qSh01vNeFO-NqbTWd38ON2EebgzI7ZzbvYNBwKN2Dpn4xu1uuBgqOZ9o0Bqw2PSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11c692bdfd.mp4?token=N4EACDXBaTEeYKnrPQQjudC5d8HezN0-NDPh95lxzKrBTQNbSovZs5wSZ78xpK7-832x9rcdZCReyl4zCUgYoA_IDjMat8ZMA_3bIXA77OhOOstA7p7QMTxgQQOMzkPH1wnkP2R9kOSLpSMZcl-a79EPDV7tPuEGbURZXVreyMuBaQV4GmkPMub1WbFAo4HhnTolQUqEgu1M7_Qh8ymDpXze_J-4FZ48ydwi2mweTrK18I8o4GOP_qhEcstUWbmtf5wsYsHjiNEtN4FxUmTXI5qSh01vNeFO-NqbTWd38ON2EebgzI7ZzbvYNBwKN2Dpn4xu1uuBgqOZ9o0Bqw2PSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فتاح سجادی رپر با استعداد نسل جدید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82742" target="_blank">📅 23:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82741">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cafd847a6.mp4?token=liRF7cEkSkMemfcOQfFuTzhuAw76gT9J7WKrbFphUPBakRVxP9udJNDaEigCT4D9dyFHq1-6cMLgaufn27HSluPCfk9_aRv_y2oNeMJvBt7l58pUaiOZe-mxWYAWIW-1P_usDbuD_qAbMyyPfYpBxi3S6RZWl3wbt4rRHyaZaV68mw3CCZpDY09myrgvV-ZlJtRN8eDQGK5wRq8nnnTTOiK2BcZu7CWFcrtoOKcTy5KiunYtURENROLrn2l_WWIMAKpRB8e197DCRkMTPNLQIGymd0_ldc3OV1exGjCSUhIiuBQCyFAhcZRdfjv0_-pR9XxnvPTvN1v0ttBMaVlSAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cafd847a6.mp4?token=liRF7cEkSkMemfcOQfFuTzhuAw76gT9J7WKrbFphUPBakRVxP9udJNDaEigCT4D9dyFHq1-6cMLgaufn27HSluPCfk9_aRv_y2oNeMJvBt7l58pUaiOZe-mxWYAWIW-1P_usDbuD_qAbMyyPfYpBxi3S6RZWl3wbt4rRHyaZaV68mw3CCZpDY09myrgvV-ZlJtRN8eDQGK5wRq8nnnTTOiK2BcZu7CWFcrtoOKcTy5KiunYtURENROLrn2l_WWIMAKpRB8e197DCRkMTPNLQIGymd0_ldc3OV1exGjCSUhIiuBQCyFAhcZRdfjv0_-pR9XxnvPTvN1v0ttBMaVlSAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارتون عالی بود پیشنهاد میکنم پیج تیک تاک بزنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82741" target="_blank">📅 23:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82740">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uz-ooh1WcB7g3Et1OZg6d1WVkfz670LUh-g7vbsSxmRdDRrG7FCUcqpuRQk2bSL5r_Ecg7o0D2ytAbCSMfb2oIPIpu1pVKQFQm2kA7-VkERx3yizXFj7jyb34KoNQPjRycGpYKv_tBzTbF3OTVTZvf_wHqCee4HYCgpFlOxRFy0YPNV0Ene9-UMQ1oL4GRHO4rlIBTKhvTWosSyXqcXfizSQzZ-a4IpEB-SqQnDMXuRaxqFBtGOLvhG54sUlae2bgt5zmpr6C_IzMGQmOEzw1fiNUK7muYAssW5PxN8A73EaT6In1csjf1-e0cpriBYuTYciylePtjhaDQ4Wch6isA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقیقا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82740" target="_blank">📅 23:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82738">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/732d114172.mp4?token=cvfNZPi78oMylT441tqpERXRQC7YhkoH1hC8Vyj816N0FqgHidjpJt2NSbqIPQSye8O91lQOJp8bJ4LgBeHmqkW4AdzzxTS9CdyxfqmDC0a51_YEkkwW8SeQTRlhZlLN80w-MLLbPJ3wwcQW_6oynyOHyPruCfvInvKH5Fvlo2J0wHqfrTlSfOoZlu5mcNke4LXebWnbCCf3Io5EnRz6jM6-fmrDvWsANfjzhHOsn0hA-t8FbYBfaHwhCQuRtoctZogTNUjRtL9Puuz2tY-NEa-zimUql-4RuATSjPssSHNbi6GpUXR88HAt4fRJcTU4GitYHSH043bHMRIKdvZp0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/732d114172.mp4?token=cvfNZPi78oMylT441tqpERXRQC7YhkoH1hC8Vyj816N0FqgHidjpJt2NSbqIPQSye8O91lQOJp8bJ4LgBeHmqkW4AdzzxTS9CdyxfqmDC0a51_YEkkwW8SeQTRlhZlLN80w-MLLbPJ3wwcQW_6oynyOHyPruCfvInvKH5Fvlo2J0wHqfrTlSfOoZlu5mcNke4LXebWnbCCf3Io5EnRz6jM6-fmrDvWsANfjzhHOsn0hA-t8FbYBfaHwhCQuRtoctZogTNUjRtL9Puuz2tY-NEa-zimUql-4RuATSjPssSHNbi6GpUXR88HAt4fRJcTU4GitYHSH043bHMRIKdvZp0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکار خلق کردی علی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82738" target="_blank">📅 21:55 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82737">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVDJnMCh94h4q5PRKCplmq_v51yuJaX69Z6qwp16rsx0WyPOv1TadRkoLwxngUEPUgNOdfWJz3058i4CV-f7YHTrJ73wvAjgBye3H7f520yNUpsp9w860DM1PfvcfANZQfrKmsg0Lfj9gPaXbrbJdU_BKKft6Sysfsm-Ky_qdQ0NLcYFd5MmmSB_flH_v1Spp803BmfShAyj03-lDGY1ggjBaxjxLgYBSLqlQ2Rvu2HRGjOFdVQoOJSD6qSOqsm6wwN7AFFwIw5jUSIIRWVMWfrcUlbp6_ioe8fNZaFmbiMYPfyapdo_HD2JTCSsVwxS9fGax7kNEbBMqkiT_z61Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نپال قبل و بعد از سیل
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82737" target="_blank">📅 20:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82736">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGLB02MSJ-LhHZUg-wGigB3_hlw7m6xO0yY3LzGGHkRQRaOMVGiq3jl23wPNp430CsmoQeov67sqUwQQReYOY38IqIwwC9-w5VQunUhh5iwRgJfMz7qkeH5Mikj3LXMrJuu8hE6hxEgWT95Cxq5_kOooYkgWFZku967io454CtJMishzEEA91KSjAheRMcaUBnJ2npqsCLjwhUm7x0Wj3pxI23EV5IGd52ILTrjQaRRUrmR0UovwY1PAajnv5Qw8P6w12Y3PPCFZ0gkosZr5i9ND0FmbcrpDwStVUzZzcp_G13qAoCLvKu3G3KaW0aODJepDDPJ-iW7BiT7CgRRVVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسپلور قراره قوروق بشه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82736" target="_blank">📅 20:52 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82735">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0h1o2poSsGHZx0swFDX6JNPsurSaggidIqbN-IYlUea1q8k6dG_jQOqc2j0D12PjhDGHAL9u1QgXXuzaNqBkyYzJSxRnVHbBzTreLNIBhhiVAkA2QSYl6-1ZdUAUfIiozgcKgMJfDbJlAl22PgNcsrGvWFieAk_HcP6H_YS48qQBGNYYweUcRmjrMEJ7la1-3WHKNXyB45AK_aDcShgM00-Kul86ja3NIBgLCJfS6oTvP-k0jYD2s_ONsoci0x5Lz00UdRJBtEUSIMsIhmA77FNA5NJWhlfI6moy9NocV0tR2Hrh3j5uBwfyhjRktwfIGmarmphJKVm8dTRDyjqaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوری ببین کاراتو
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82735" target="_blank">📅 20:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82734">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOul11bEbnvlls-bD4fmSANe8X9KHaWXSBLYbOs_XVPmMyjw0fW0SkcfehtB0iPAgjEpUNmYVTerECC93Mv9EjndBrvP4hLQKCU68EZdcsAFq7rDkjzQ19m1i_TByAoz2xZzqrUrt4h_L63SMJEn6L6OBpTSup8Vhi4NAyQJs4qZ724Za6FUoz4BlQkGc8tJzQscM4kQF8IiDG4NcyzMUvJM_MHhIWTHQeEGnWXWOr2bbJjlc3DrEY7aGIwkP43Ktrh3-FHXe_XXKfY_QTv3zTqPbXYn-0uABhHBCCMmaF8KZHBviXE4a0M0sedgwANqjqgEi7jDNvD67dgiVfJMkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تروخدا وضعیت سلامت عقل شاه مملکتو
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82734" target="_blank">📅 20:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82732">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPbaoRoSQ7I76yC8by4V6U95CZmlXXveQz562GT5ygIn9b2ZQ_N8EekJ2TjkK2ls7a8YdfZGpMi4MaYJKtE98MCL84qoxsaV5w0lhI5j4a7MZl8n6DTg2CvHX-v8DWHW_Jp6Wx0U-buIxlmkFlBC8r_m2M3s_qSrMhRMynhCr2FYOYzhjeEwHNa8SfMiAJJc3Z_rBZwdsy3jvXil89T0HU4EWaIw8fIAfVtA9s8JXt6wt0iTKuX8clyUFSupYFN_o1okz4Cuyb6TTHOMk0ICFrRzqJkShu7USkVlMo_fwiuNm9r3CTyOhHM17yueWV6MB2bsmDCOOgdDZxF__cxzaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53fb725890.mp4?token=LWlLzyUTQG-TnPmxFy6LJNXmTzmuqTWcEV2W8-MTx4Kh7-1x3oLaFxa_yypbRzGxtBFFTgvGjKtwC7okMmwS69UhP0PXKQ_I67HZeP_gzcmHsMWgmpbsSv61LzkRPpFHP-WOpEJwYPbtqzd-ola-NZYjz4xDCpOGnWJvObWFUlrafjEP7V4A5AZyyW1VxLtUwCfXPP8Jrq25KwrTy1V07rCHchwd4Jz4kCWFl6KXe1AKpzdikj2JK8b4UiAAE0fatjcl_M2rM6fxH_yNRksPA-F0fMnx4E52Kfjzd3VZkOgBxAS5pNbNcWqhLeLyl5jVaXipyxW7R0K0mw3Ffowz-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53fb725890.mp4?token=LWlLzyUTQG-TnPmxFy6LJNXmTzmuqTWcEV2W8-MTx4Kh7-1x3oLaFxa_yypbRzGxtBFFTgvGjKtwC7okMmwS69UhP0PXKQ_I67HZeP_gzcmHsMWgmpbsSv61LzkRPpFHP-WOpEJwYPbtqzd-ola-NZYjz4xDCpOGnWJvObWFUlrafjEP7V4A5AZyyW1VxLtUwCfXPP8Jrq25KwrTy1V07rCHchwd4Jz4kCWFl6KXe1AKpzdikj2JK8b4UiAAE0fatjcl_M2rM6fxH_yNRksPA-F0fMnx4E52Kfjzd3VZkOgBxAS5pNbNcWqhLeLyl5jVaXipyxW7R0K0mw3Ffowz-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خارکسه تو خودت تو ساندکلاد ۱۳۰ تا فالور داری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82732" target="_blank">📅 19:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82731">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39afc7af6e.mp4?token=VLgyF6WD5Ql2H9E5j83PE4JkfPw13p220ggQjvIWUPtY6NwvKrSHl8FzYoSsaiu5jVfMP7TeDp3XtU93PmK4q_mRMrH5TfJ7QWzKoxo38S__1YFF6Lkf3C2n2Mg6dGKuK0JqGeTsAHDn1jDxkBvCnt7goQ9NCj50Ydv_OwtUtITPFgfWa8tQ-jUagpbV8ZeS4AQQaWmD_U__X4r3Lu0W3lw8iz6CBUjRGRZAyNEYJMZhhF5mljE6IOTgBhcCxGACs92Jrk0BLO058o1sRQX1kAxMd3rv2fDMe9kZdVW8_jw7T8ydiiG0Ct5Ke6QHh3CCdAUf0rmEj3lOR_5DDQ6MxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39afc7af6e.mp4?token=VLgyF6WD5Ql2H9E5j83PE4JkfPw13p220ggQjvIWUPtY6NwvKrSHl8FzYoSsaiu5jVfMP7TeDp3XtU93PmK4q_mRMrH5TfJ7QWzKoxo38S__1YFF6Lkf3C2n2Mg6dGKuK0JqGeTsAHDn1jDxkBvCnt7goQ9NCj50Ydv_OwtUtITPFgfWa8tQ-jUagpbV8ZeS4AQQaWmD_U__X4r3Lu0W3lw8iz6CBUjRGRZAyNEYJMZhhF5mljE6IOTgBhcCxGACs92Jrk0BLO058o1sRQX1kAxMd3rv2fDMe9kZdVW8_jw7T8ydiiG0Ct5Ke6QHh3CCdAUf0rmEj3lOR_5DDQ6MxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مادر چنتا قانونو با هم گاییدی دلقک.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/82731" target="_blank">📅 19:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82729">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dc982FtMMDvL9f5y6QtkaPFgXu5FOcJkNlhH1vQQ0xgjgc7B9DfQGVvDaqeahT9A6fvY3_vEr8Tc8ptuEVAyMzWtkRwE_Hh8BWsyhkj7V6SoutTJvQ2kj19G9TMecteURKjdKRGMvjjna0Ct2QpC5sQhH32U5GzuKqCuGa4UgVUCKp9tBWJfz9SRkE4wBf1tB_I7FPwka4dXJ4Hj07kpMLMgc9eKmSAWK-w-dp0v5hw6-m3maldns43vci13QE8dNfhKc3xhyzHlH3VFLgXukENZaomQ2nRXeSoD1r1cpfWqZbWdKPVOsjD13qGl95gkbdURrQNcGcD63zH24Oijuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقت پولدار شدنه پسر
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82729" target="_blank">📅 18:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82728">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اون قیصر خواننده که اومده بود ایرانو یادتونه، حالا میخواسته برگرده بره نزاشتن، و الان ممنوع الخروجه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82728" target="_blank">📅 18:07 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82727">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">تنها طلای این تو کشتی بود که اونم بعدن معلوم شد دوپینگ کرده طلاشو گرفتن ازش</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82727" target="_blank">📅 17:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82726">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">میگم پویا رحمانی پتو رو پرت کنه تو کون مادرتا  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82726" target="_blank">📅 17:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82725">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBb3eWGyPbWnsm_dRAY8oL1Oqy4UuW1yossuldVbbgXQOBU2Ffwk63VbMxjXwZSmwMcCZHxXyvQVmlNpMQ2CnfgGMl9i_7zjNjTo7l07ZRPFBL1-Oej3dxv9irq1L5aEdgxf7ktXXGFjm7hxMl47RY6dfNibxbjwqAwb8M3Df4Gr3MxW4gVCtsrIzwzk2cdYriOEfbPfCnf-ofy1j39S0s74UotpmvBZICHtkJFjcdNSEga7EVYPreoAIhY_nz8F-52xAIkPREWcYhgxcbDk-8EXqIrS5SaRNJEHJ1MFV5FGW7-XraWKhkG1ItCUuTtfoCsHGvFsVBIJ-RjP-7y25Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگم پویا رحمانی پتو رو پرت کنه تو کون مادرتا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82725" target="_blank">📅 17:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82724">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irpMI8JgBTsIktuMTG6hkCqaPAkznGObE9BjevUyWZL4AkaYi9E019vsyQ5VAJPr6EYRCu0RU2s_F_0eMIqsr5JxO8X95jIBT0sU6rCaMegTL1YqiJNJM8gMLOdyUeM3yn8oTh65x9q8xQi9h6pvL7J3wmITHhne_SCmfItdE3vlO_dsaMFGmfTma6Gn9Mp_oW0-u703aGdXE6ERHGTSGANVPbipX0Djn-EYvHJFxOkQ-znu-4TN_xzoUnjCBgJLnUIcoakwsui2WiF7TOPsV4owTCQwRwbdFGUYCJ0TTN1BSc6CN-uBsyxhJWE_B0xIzsTgLb3Rhul8rwAYDbIGlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت امروز گوشی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82724" target="_blank">📅 16:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82723">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خاکپو لیورپول چقد استیل خوشگلی داره</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82723" target="_blank">📅 16:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82722">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIjksVOtXd2Lu01GHK1Z-Qnarp6n4QgVD6FCM23z7DYNxpLaIGnHlcbE5hHKq3IQ1xZeAPMWkxuza4nQuRjWwf_E3aPEVbSzJJk8bGlIX4qbD1STxGOrxX4Ams-HLtFSbbRmQ-v6yzFccoe_eWQgFY0BHN3Tk_K-9jHGNsjmwdVX2MJlkVseaHQawG5Qx1kNv1oXGiQLSc_FuOLojZmlzAoSmy5XqFd6fDOcuY0S6JWwL_awJNGp852-nuJLndFeEhySi8qE5s7ySIxLmVUdfBEon3hxM3wWF54b4Om_7Rl-J99xMBkVpf8AKjm_ioFbMf1HIjFKzPisK9tGSeoQVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفسور سید عباس عراقچی:
یه سری اطلاعات کیری خفن و محرمانه بهمون رسیده که نشون می‌ده قیمت نفت و بنزین خیلی بالاتر از ایناست و آمریکا فقط با خبر و اینجور چیزا داره قیمتشون رو کنترل می‌کنه و اسرائیلی‌های بی‌وجدان هم می‌خوان رئیس جمهور ترامپ رو با این خبرا تو جنگ نگه دارن ولی مردم مظلوم آمریکا دارن این فشار اقتصادی و پیامدهاش رو کامل حس می‌کنن.
💔
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82722" target="_blank">📅 15:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82721">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHsFaRkAFE-NgJFuVMfzE9uS34JWKK1mO0WBPWKra6OQqzr9ia0K0B851zYZo8BA8N3VMRwSet7WpQv4O382m4nnqqdkg8nE1oTMFYUNMGtxPqRnl4SIjIU3yUr4LOZcbHPCUxGnfPBo9iNuQX-Gn5TiKwC_U2GnMgsVKWcEoF5rguUl7_UeiLgGw6CqfCLdbgsP7NbuskRopw7-x-oLbPVhVWXZfUyAEH-lKLbIKJ4Kcnt8HvX0pWTm0T5G97-JZaWid4m9V-NBwCSxTPYNtjPAMdEWtC01naonax63hconpByp3MFZTJXnVgfX8pJt1UhgKDOeZ84shGelUdtRmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا نوید یک اصلاح طلبا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82721" target="_blank">📅 14:06 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82718">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">کریر تلخون تا اینجا کلا دوتا نقطه عطف داشته: یکی اونجا که فان هیپ هاپ تصمیم گرفت مسخره‌ش کنه. یکی هم الان که خودش تصمیم گرفته از تیمارستان امین‌آباد تهران دوست دختر بدزده.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82718" target="_blank">📅 13:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82717">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">@FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82717" target="_blank">📅 13:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82716">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUoBuft6yRpAdapsAzFXqfuvMURfwPHY4CbQaUueVEV4cS8M5HujWH6Nw1cdT9tO0PYS7sbjxGF787PKkFqa1vM9dAHCiQ3j7p6CLwQbDCV8UBkULxD8JrLspre9dO3TCYQtuXKYCc9jcRN2-K6WBS2MgHvJHqzq0WT6KVV9IivcoKZBjtxcDD7sfABNzADenXTwZk4-JSVaHHrSeSMD96BzrtY0ZRvGzWRUjltv-x8Mr2CHAob0GiS2JhQDCIOYqddonO8viAt8sgyvQgH_kR7WeddS8XqQzMyQuNMoC5_9fSS1tRTKH1Kynqh5Io4024b8RkGK3ye47I7QolIUTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82716" target="_blank">📅 12:55 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82715">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vr-F6sSJFqPrx4JcFtqLkSVb0UjErFDby3fQ8pGW_cjkfWoOY1kPXkZ65IWKJQrisS5rEGEkacGQFcWsxsglnHo2rKHXpbD91EeLiBBdUaRmOxwHErj_oOJPw5LplPJr1UGER3ZWqIKYZQCcrN58uA4H0LnEEcra6UycLMEbr_l3-x_zkP4obyHY8TkSvg5UWtfb6_hS4WvFInHawPNRycuGQgQ8rTuaSwcNBTxrvd7HlW4zENFGDGJnIGGlrDmgitYSFl6NJJ9kf-YT0MC-XvSSHFzR4KFVzwomPwXwEFG3JcrXWFch9iTyhelfl1kOgsTAinyvW4fQwC5M7t-n-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زن سابق و پسر حصین.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82715" target="_blank">📅 12:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82713">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Va7rBY3yjF1pXfW4tbpjhEP0wOhfUFAZ280Ku_-Iud2nHOL6VtDaYAEUKFAP8gpTzH35lvagaFc6UxmiG2lf4XJLZp3E-MFdY6_l5X0-e9L4BfyOGKys0h2B6jeCqnz4q2jR6lPB-OfnHoBp6bBxFSbyNS55BlLcanTHBA5pyIBruXC95B4QVo_cxvfRdXoZKQBBt7anpzoyzmRiir8PG-0m8AKtuxkjUs3R94nujSgeF6CWAdD8WrN4C15Q6fRLh4tjXHwozwbjZa65B5qQZ-mX1pUGrJ_3_2fv4cG1bSQrWSoFfvy7jv-1n1Gc84K9-okaIAU8MN7tVcbHVs9CQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jamXlkQg7ceFxW0u5z-Tk9vYh3i2ejGyB2ksWh-wfl5VWqzhK2uXvW3rtXVeoYb8rv7M-wW7gSBXRMvr8RHOZzOK9ObNeZLspozPZyW5SxMTF9m_WAOEdWgefQKsmGjZ8NrcMpydRNq4o6Uh9gVvCZv1I1_DT5y5LT2JJvRRh4zoeLtNP0dPi6-ROndoKLktBFu430_Q7_umEJNPBRj-hgcNLos0oSAUa02l4VOdg01VqdDjVZdKx1XAUTArxs5ds259u1Z4hb_IFkuAM3rbfwPOc1AmSV4KRswi8t7Vxewv8PqS960buZbJ5DmU1SEt9vDQV70-QSKtPYuFbscjSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دولینگو معروف ترین برنامه آموزش زبان که آزمون انگلیسی این اپ اعتبار بالایی هم داره و مورد تایید دانشگاه‌هایی مثل استنفورد و هاروارد هست، اعلام کرد آزمون‌های این برنامه از یکم سپتامبر (۱۰ شهریور) برای تمام ایرانی‌ها متوقف خواهد شد؛ این تحریم شامل ایرانی های…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82713" target="_blank">📅 12:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82711">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLV8aBu7YosPnnmwBF0rNZ5U8RgSNw11W0MRifAweqlgr6c12n5cpSjSivnO4_4w7rw6hxT_nO4EzCeGDbqV49DvcP1E5vlCU_yXoh8_0PyFkQvu0zuKpUap6xJPIqVl1EGuboRQt70Djo25HQQ3BT04uBCSJtXvy60EW877VTvTOOiC2GELFP-3ECXqvfUX4Hn2QmV30K9osHuuHbhUK-WfWa6ultQ9_TveQh3bCdHSjzQkHmBznXi955mmEScFO_o2AQZwO_vuVQ9IQju98hsC_hVg9Sfq-G_6fyxO1BsjGt7Zg-PHDXMugYJEnmTnNlJIbJdoTyuZrVBVV2oH7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه فن اکانت انگلیسی چلسی اومده یه ویدیو از ریدمان های گلرشون سانچز درست کرده و گذاشته تو توییتر
چه آهنگی روش گذاشته باشه خوبه؟ پلی کنید بزارید رو ثانیه ۳۰ میفهمید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82711" target="_blank">📅 11:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82709">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یه آمریکا قراره بدنساز بشن
پیت هگست وزیر جنگ آمریکا داره به نامزدی تو ریاست جمهوری فکر میکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82709" target="_blank">📅 10:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82708">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449380bcee.mp4?token=RPLqRdWpMCUrxFiVcH8Igxdu1nAMJM66CnM5xnzd1kAYSfzHaX3tm9957CLUtwm0H_aGtqLJsZqskxv0JC6tvgC4AKeF0LCLSPmpnk7lhv3ZlUnHIwmZwFuCX2V0hD1PEphrxeBMT5MoL0El9qxCRCKq90yeX6kR5Uq6QOxUypg6nLYcs2xroO_411et8U_bKshqXrlgzAceyQt9IPRVW_iuI2rqfYpGfQocKmNxZwc6b_i1l7epdqsh9sAxPSxSEqpOmyUo6O9LAnB-ag7t_vWkgOrjMdMwjG8RDCbc1Deix_7A765DpTouDbRcKICPzC6VzVdJjj4qz08ZjGCm84i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449380bcee.mp4?token=RPLqRdWpMCUrxFiVcH8Igxdu1nAMJM66CnM5xnzd1kAYSfzHaX3tm9957CLUtwm0H_aGtqLJsZqskxv0JC6tvgC4AKeF0LCLSPmpnk7lhv3ZlUnHIwmZwFuCX2V0hD1PEphrxeBMT5MoL0El9qxCRCKq90yeX6kR5Uq6QOxUypg6nLYcs2xroO_411et8U_bKshqXrlgzAceyQt9IPRVW_iuI2rqfYpGfQocKmNxZwc6b_i1l7epdqsh9sAxPSxSEqpOmyUo6O9LAnB-ag7t_vWkgOrjMdMwjG8RDCbc1Deix_7A765DpTouDbRcKICPzC6VzVdJjj4qz08ZjGCm84i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حجم سیلی که تو نپال اومده رو ببینید خایه کنید  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82708" target="_blank">📅 10:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82707">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2fea1138c.mp4?token=KfZ3i7gWqBk9ZF46ueI1AdAM2vu7wa2dFKMXOzuSxNU5qgq1bax_9ckov3ByFde7xuCoZvyxr9z0O9IGa2WjcISxOTRqXraxRGkOFwR8So0-op1fmEUJCwydl8IcOEM1Zgq9WVcn2h41ZyLj01g74cF6-lWzDsGOZVrTDBmlT_JCjORC4LIqfV61fNZLkoFC6oE3MuNDSWQ6RrrZv5pqudWi27RrxpWGQ1tg3eOPm7u55h7T9qxv9aLstsCY0pRxlIGWf0_FVeACTSclLyQ7wQmn8pPOknq5GSyw4kVappQ4-7Y8MCb6TjJ65lGbEj_fTcxpFfVhALOuSqtaow59Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2fea1138c.mp4?token=KfZ3i7gWqBk9ZF46ueI1AdAM2vu7wa2dFKMXOzuSxNU5qgq1bax_9ckov3ByFde7xuCoZvyxr9z0O9IGa2WjcISxOTRqXraxRGkOFwR8So0-op1fmEUJCwydl8IcOEM1Zgq9WVcn2h41ZyLj01g74cF6-lWzDsGOZVrTDBmlT_JCjORC4LIqfV61fNZLkoFC6oE3MuNDSWQ6RrrZv5pqudWi27RrxpWGQ1tg3eOPm7u55h7T9qxv9aLstsCY0pRxlIGWf0_FVeACTSclLyQ7wQmn8pPOknq5GSyw4kVappQ4-7Y8MCb6TjJ65lGbEj_fTcxpFfVhALOuSqtaow59Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حجم سیلی که تو نپال اومده رو ببینید خایه کنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82707" target="_blank">📅 10:08 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82706">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نمیدونم چجوری بهتون ثابت کنم ولی شنبه حتی از جمعه هم تخمی تره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82706" target="_blank">📅 03:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82705">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X50sTp1HUTK2sIOHxw4rX_8Zr_a0Ceo_AnQlsw_lAhKOU_iZ4eNbgsClYfAWGJ2WKInGh682IYQHJfMXeZ3nXUOTieMj__ppyaqF9HwAThbKBPPgK1dS6Y9tiW_MYtcShmgwbAM2ShkQpe3eQamszITQn4iYcSEWNYfLQcB1VvEuYRSzpT8ChbB50yhxFGatXUWDgPbzZplLduqm51MjNhw0WX6o4rDz_3vk7BhZiLmTOveBV0v6ZmQQS_5BkuKlfSdL1keA0RJbQ4ioOxl5j3AiTnLJyORzNYkpFPBSJjTdOGSPzmvq748kQOHkJSFVmQcjIOgezbJWZPWSoFNVBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیلی بازرگان: شاهین نجفی برای پدرم با صوت قران میخوند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82705" target="_blank">📅 00:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82703">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7BNUfjg8bcQXI5wEXSq3GvgHKeFBphuH5tarQz1jFq_lBklvfWwRZahvnAI3HDT96qz0fQSTzF21P09hdOZuvSM5qQiOPpddidSACzzfUNgbR9LnmegBaubbL7IWENx34HJHP0kfiPIkWzq9BPosmoIraM0LlRSqagFjDcjuq3N-OvXbkVHbgt1H-TggkzQgndZ7kLHQIlGziI27GkBaoyPqC37EHa37DAK_4xB1oHXXtVCW3zQaeGwNcIPPtlPXbgi-2A6ghFdA1xp_9D-utmPkLeKheLwRldCp1cS0HjXX6bru9-27JUtfu_kggeZg49HYLVCnxnRNmMFoz-k9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a8b3495ce.mp4?token=BgQpHK5Sy_DrtyUkbTFuBOGqvn1z6XDMz-3zTxTDrILH-zHSdhJBeiNqXrXFgROQgxgTMn8vyyZQaipTVml7xykEfPuuLyTBv98Lri1APit9r7F5lSoHnKmOpDBFH03u_D0ZqOqpnUhYk3MFhSGlFf0z3uob2vrktiDE9IZmvhTmJMTGlBMY5fErznahxfdulTLqkPC9FZqTRgfivjA25hykV5DELVYOrwmhcy1xD-Gz0X5mV4utMryqQnsrI3k5RpcvZv7dQzbnrD5gz9exrrs6aU3QVCs7rPtfmg_KjKrEqtmlfDBwhJAB4ANaHyGR1BCmaFOy5k_vx4Rt04Ex5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a8b3495ce.mp4?token=BgQpHK5Sy_DrtyUkbTFuBOGqvn1z6XDMz-3zTxTDrILH-zHSdhJBeiNqXrXFgROQgxgTMn8vyyZQaipTVml7xykEfPuuLyTBv98Lri1APit9r7F5lSoHnKmOpDBFH03u_D0ZqOqpnUhYk3MFhSGlFf0z3uob2vrktiDE9IZmvhTmJMTGlBMY5fErznahxfdulTLqkPC9FZqTRgfivjA25hykV5DELVYOrwmhcy1xD-Gz0X5mV4utMryqQnsrI3k5RpcvZv7dQzbnrD5gz9exrrs6aU3QVCs7rPtfmg_KjKrEqtmlfDBwhJAB4ANaHyGR1BCmaFOy5k_vx4Rt04Ex5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به هر حال کمی روغن میریزیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82703" target="_blank">📅 23:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82700">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a822db941f.mp4?token=rXUClCaG4vgKWaLpKdtX7lidxoooQ8pN8wHGUZN1-3v-318wbgWYsZA_iea1FVmGhQEKBnuTXZAKd-uwdphiJtMcmDVzpiYDYiEh-KAFMvWJpkhooSehLKN7uz5XtXvlaB5cXabvcjC20SclhMgUmztuI5HnEG6iPA6F76x1oLtucMyeTU29uBvNQ9SdtB6afLbg76SNLYwzfNuH33KygPMUrIxGW4J1FIiOKzCBsy1b0pwpu51EAgbUYZ2kY7QwcpCjvFsJjlFiZ3AVaywzmLnF3Dcg0wDoMLdZ_OKVz04n-Qg_nrWG0yyqJ5eAABER7Zxnpcpt71DKLJCwsYrNjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a822db941f.mp4?token=rXUClCaG4vgKWaLpKdtX7lidxoooQ8pN8wHGUZN1-3v-318wbgWYsZA_iea1FVmGhQEKBnuTXZAKd-uwdphiJtMcmDVzpiYDYiEh-KAFMvWJpkhooSehLKN7uz5XtXvlaB5cXabvcjC20SclhMgUmztuI5HnEG6iPA6F76x1oLtucMyeTU29uBvNQ9SdtB6afLbg76SNLYwzfNuH33KygPMUrIxGW4J1FIiOKzCBsy1b0pwpu51EAgbUYZ2kY7QwcpCjvFsJjlFiZ3AVaywzmLnF3Dcg0wDoMLdZ_OKVz04n-Qg_nrWG0yyqJ5eAABER7Zxnpcpt71DKLJCwsYrNjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکوندی شیر
مسعود پزشکیان:
نرخ سوم بنزین از ۵ هزار تومان قراره بشه ۱۰ هزار تومان ولی زمانشو هنوز خودمونم نمی‌دونیم سورپرایز باشه بهتره.
(احتمالا بلافاصله بعد از پایان شهریور)
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82700" target="_blank">📅 23:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82699">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjCn4qmFCDIVI3fxrDpwdC65qOxbXtzXOKyTqImlypIWV-3yMK5lzEvwfh5GfyodSSZGdQjjr_q-RGZbKKz4qUQE296z5jxfWz6C6wqEVpcRqkiCKxxxG4Jzm1PNHFQ3ljVPZjEVmFppRKi8SuDoqWxbqKWcrpBDRGdVm6-k3ckijBmQL3QK-Z5asp6ypPkoucY4sYh-0wPhVM4O_7lPZX-Vx4xH0wplfW3T7JZ6k06HmY9GEfO94vqMtpU65TFQmaGY_IxmsVk4EA-1_hKV-KO_sz9o10KO3d362lz4PCemHxkwfQCPuFUaVBUefc1nb4x_8wtdT-IQX9UEswxg9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای تکمیل بازی Gta 6 بیش از ۸۰ ساعت زمان نیاز دارید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82699" target="_blank">📅 22:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82698">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzBYpgSy5FLPzfn9gIY57QXqR0EuvTre6kO4H95Sn-nDeEBDdikjkpUyEFjDMBQY2cazjDZYA2tbKINcHNtiBuWe4HvBo-PEN8gX1LIdx3UydtGtWK_3HC_E8CGZUIPTHq8WDiXYy5cT5veHCFEZo7sllr4Wp4CPds62MJx_qWrOxn1toVx3UoLgRU-AhW2wy-UJ_93kXeTWJczAsm5wn4UDuObFIvSir4l_KY9LS_TMWWc-GC4L97ZNPKpRyFUzb6pwyJAexOvu6JsC6dh1aYQCl1E_ZJmx1DCLq-HFKiYbwBG13fKS2AKvUKQJ07RSWstTdPFP3smOdpkCf4ZI5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الکی گرون نخررر
حجم نامحدود واقعی یک ماهه فقط ۵۹
هزارتومن
تست رایگانم داره؛تست کن راضی بودی بعد خرید کن،خلاص
❤️
@VpnRgbot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82698" target="_blank">📅 22:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82697">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">فیت خلسه و هودادکا رندوم ترین چیزی بود که میتونستید امروز بشنوید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82697" target="_blank">📅 21:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82695">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cvyRM-g6ojwl2QkYSdk6Ab2NSbdxRJ2QaFhjFmROQTPsz2erJY7QB-lebGrrmhDC_bqmAbHZh5TJiP8IPdvdxmbliH8I8Njs35Th42QQOEQZOBeH63gRhe1FKwkopMW0uCD1wR_XFhK0RrXEBRwmuUo7X7pX_ci3KGiMcqCpmZtGbJsO6npNnqUH7-Zv25TceresrcQuqw1qcSY0AzcO49GN9VcX1sUNxQZha_15bHfaS-yNdz4SEllfcy7W6iPLB8f2qzfwcuc5qBN0po372OuSAKoV8LvHci-F3cz1Gbd92LTmeCgCyiTbeazEyAHJuGba4cLE5Zfwqjokpypagw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pb-ehEJV866AMrg9wAuUK667bwFnsAEZcPcvL50ajj3MwtFs0z6LIqfMf7_75Rw5HwebMoB1muEBVGWIKQ6SGSJiC8TQ-4iXZK9b1VQmT13MD8A3doSVvhE9hSZY-xZiapQOgZjnP4yeENq4w-r_Bz6OtxFLxI9h86dROpLsPRyAg-KH3arzWrT0f2foUKDd3aSauDy05RI6bVU9wdEmi4QjutiNRv40wiDwmN63Pz0o2DlovPX_CTLbowkET4ftVCNF1kh4i3wE4aeu3fHAonWgWsDpR8TtTHUtoIsax5R924cKgfLIc_jLFk2ajlFNfrGmzZKXoewFd1VbyAOeBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ای کسکش
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82695" target="_blank">📅 21:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82694">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaApOk_rkHDRmR1XQ7At2mVKLoC1GnIihRQoT6dHlM85pPyPPKA4y-3ncbK4aNy4w-Mv4AceXRK7hz7amRCqFFk8rnKHni4PKaWjKAy3cgvqCfLDOW-_GUf4zc60VO4kSrHaH_QLIlBpu_oh02dsEh3VS6XqEAAaaG_Wjv2UZYUtapy3eqUrjWVBE5srEZZnJzuFh8q3pV5AEczjOqtitXgiMnW8YkhkXiHbXOtSyLp5fn6p87MaQDWEUhXZx_EKRKyBwWY0IRKsyz8lijkv24q43x3h1fqCfIh-mKl9WqJiNMgs1u7BSom1j3Yd-eMRbZ6CKd9uHAkwsXIXI3fhxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن نامجو برگشت ایران.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82694" target="_blank">📅 21:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82693">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">مجتبی_خامنه‌ای.pdf</div>
  <div class="tg-doc-extra">250.2 KB</div>
</div>
<a href="https://t.me/funhiphop/82693" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">مجتبی خامنه‌ای: به طور جدی اعلام می‌کنیم که هر چیزی که به همبستگی مردم ضربه بزنه، ممنوعه؛ مسئولان هم باید حواسشون باشه حرفی نزنن که روحیه مردم رو تضعیف کنه یا باعث دودستگی و اختلاف الکی تو جامعه بشه. دولت باید قدرت و مقاومت ایران رو به مردم نشون بده، چون اگه…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/82693" target="_blank">📅 21:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82692">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مجتبی خامنه‌ای:
به طور جدی اعلام می‌کنیم که هر چیزی که به همبستگی مردم ضربه بزنه، ممنوعه؛
مسئولان هم باید حواسشون باشه حرفی نزنن که روحیه مردم رو تضعیف کنه یا باعث دودستگی و اختلاف الکی تو جامعه بشه.
دولت باید قدرت و مقاومت ایران رو به مردم نشون بده، چون اگه خودمون بیایم ضعف‌هامون رو علنی و پررنگ کنیم، عملاً داریم به دشمن کمک می‌کنیم.
مشکلات و ضعف‌ها هم باید با تصمیم و عمل درست برطرف بشن، نه اینکه مدام درباره‌شون حرف بزنیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82692" target="_blank">📅 20:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82691">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a618ede86e.mp4?token=G0UNwUkREKREQ-_ds_KG9BXdz2eNxKcfMT8avicXm21GH3JixhuT5ii7cYgwg3aCOjiga9KfPQVT3JKnrcDmas3F5Y0CVZNpgImzmqQlJ1pFhhwO18b8FrtpJj_gHgQNiC4TpfL4jcH2IsSkWcHdL3N1z-QPzyveJKezFELvB5n0NvOAM0kprAwS0Ufm_d7PJbQ6dv-YFIelQCxeYWVXLZh6vrIuDYFEm63JkXKCbP_G21E1Z3KdVYQbInXBkHsIbDVwVmasSnjGz9AcZScNr7w9Y3xyiDkUYmmFxhn6bU4IumwedQK9gzgnsBlzk06VEwsw3t2wpCZPZwcGzRR8Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a618ede86e.mp4?token=G0UNwUkREKREQ-_ds_KG9BXdz2eNxKcfMT8avicXm21GH3JixhuT5ii7cYgwg3aCOjiga9KfPQVT3JKnrcDmas3F5Y0CVZNpgImzmqQlJ1pFhhwO18b8FrtpJj_gHgQNiC4TpfL4jcH2IsSkWcHdL3N1z-QPzyveJKezFELvB5n0NvOAM0kprAwS0Ufm_d7PJbQ6dv-YFIelQCxeYWVXLZh6vrIuDYFEm63JkXKCbP_G21E1Z3KdVYQbInXBkHsIbDVwVmasSnjGz9AcZScNr7w9Y3xyiDkUYmmFxhn6bU4IumwedQK9gzgnsBlzk06VEwsw3t2wpCZPZwcGzRR8Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر کلمه‌ای که اینجا تایپ کنم فقط از شاهکار بودن این محتوا کم می‌کنه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82691" target="_blank">📅 20:26 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82688">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkEjFzkXjqF8QLm-XRgJ_xtUXyN9TkuMn9h-LjCRlCzdHVrZGQbw-JJvoFI5dMAaTYRjbARERa5z40bCd72l5stPIvknND2DuhHW4bGo3bqJfb5WqujrS5wSv9_mtVWQfzR-L0abADLXx9kxCjniiVJNaIXZYeuhQLSyxfjsjgCd8gPiYEssJq9K0caN-yw8dZ5Sj5_4hxHPmNEdTEfpgk2blEvc9nc3IUTGoWh93WJpOLxJLOQVnNFNGC6GkgD4j6LDxytjWxm2jH56F9Po6MCu1SLrEVFV7gH-60XIZ5JznZQiDGvR7qrgd0w29uvcYKpvVR03K8y4w3jxUyovHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولینگو معروف ترین برنامه آموزش زبان که آزمون انگلیسی این اپ اعتبار بالایی هم داره و مورد تایید دانشگاه‌هایی مثل استنفورد و هاروارد هست، اعلام کرد آزمون‌های این برنامه از یکم سپتامبر (۱۰ شهریور) برای تمام ایرانی‌ها متوقف خواهد شد؛ این تحریم شامل ایرانی های خارج از کشور هم میشه.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82688" target="_blank">📅 19:56 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82687">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jdp2DW0OPOzOVKFGKRRRYP5kvFvvhutWnC9ZaOMb6l1v0O-l3nHjaSEIYcl6fsyxaHtcRFZPtX324WLIhvADpKD85wngktkLrQmVnRSmSs9LWCyI3RCY5y5XVfmHaOOkaSL_dItF_boxzJUP43Fk4pUc0XaoXSAp7uv3fhNsIbHRBGvqTtUveCngbdtCk-DejF8fTWGxmwI7ylhR-rZcC5lWrqZ_0ZCoq63NIEbbPU_fiG0MHQoBFFXgNZHqM4m6o1cQEzM_4Qe9zyApY963zwKTI_YiQEKQODbYClCB7R1YkQ7GcksL8GtSbkpRYKkIhSPSAv53TZ0-8AipyvGc8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یا راهی میابم یا راهی میسازم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82687" target="_blank">📅 18:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82686">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐍𝐢𝐦𝐚</strong></div>
<div class="tg-text">حیف بازیو نمیتونم بخرم وگرنه  تمام کاراکتر ها رو میگاییدم زن و مرد فرقی نداشت کل شهر رو می‌کردم</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82686" target="_blank">📅 17:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82685">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-qucPVG0-py66nhzQJuJVF1nfa2NvqViR_4AoDipRUJwd4L34enLKlTpO_ebHecbfeYAbuxEE6f1_iLhYpownK4P3Nt0q-QGLvSfhlKbrsmi5EbG2du9EUY5WthtALWkdA-auQD-Je_0HuHMenjc94PgTFqU1eEX3JK_zIVIiAqEq3k0uQYwff-LK66DJQs3FDtD9ffeRPRMvH62xysm5TwPYSUHYFnSydzzfwLAlWhDtTwkvxQpj339D6Eptjw1Hh0C9Y1OMTguWD8G6cNC_rDRuzS9AKOKdDFMILnWXK5S2L9qoSpE41KLjWpXM7YXB4nTl4LYNEK2YQR_sk1Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیم ساعت کسشر خالص بود</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82685" target="_blank">📅 16:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82684">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پوتک آلبوم داد  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82684" target="_blank">📅 16:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82683">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پوتک آلبوم داد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82683" target="_blank">📅 16:05 · 06 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
