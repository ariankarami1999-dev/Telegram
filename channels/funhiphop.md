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
<img src="https://cdn4.telesco.pe/file/EPE49LvCbpzSSH_H9WhCeNlNkLd4VTq2mzE2MpD1lcBGk9PP9nwpg6oaIoat6scIXEg9iXfI7Am16jhUBQEsI2Rpr7XGb3q7Cr2XxC5aCTsgt8NmdZkP-cuGVEQ6iQnvFmh71QQqfS_zpcOVDtjw1lUXtbMBMpSRmuvQSZ_E7uye0shNY3-hskqTFWN7Lu_Wyu1LDZ61bcjTl9FtVnzt4AF6nN1-1SPp_5dkJnwdeKiSydE_mAAZIxvcvS41RPPQ58OKn-0rR3vBMbEuULQV6m-CeZd16mzp_fL23wZxq0KmtxnaW-T2Fi-dbhZSUBoO6AKPyWL4q3tx022t1LgOjQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 180K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 01:45:09</div>
<hr>

<div class="tg-post" id="msg-76215">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اینم گذاشت چنلش گفت بگم اینایی که باهاشون عکس گرفتی شغلشون چیه؟  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/funhiphop/76215" target="_blank">📅 01:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76214">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">۹۰ روز از تـرور سید علی خامنه ای توسط اسرائیل و آمریکا گذشت
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/funhiphop/76214" target="_blank">📅 00:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76212">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">امشب وحید جان خبر از چند انفجار مهیب و لانچ موشک تو جنوب کشور مخصوصا بندرعباس داد و تسنیم هم الان گفته به سمت ناوهای آمریکا و کشتی‌های تجاری‌ای می‌خواستن از تنگه رد شن چندتا موشک و پهپاد شلیک کردیم که خب چیز خاصی نیست خاورمیانه‌ست دیگه.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/funhiphop/76212" target="_blank">📅 23:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76211">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=L52u1P65q_Tanr0tD32-HvUwpJngUlNrmLI_OWrJ7CbSlMv_rq_TsBMvgCb6SXFrK8cj7A1XE5YBM5dFDwf2T_mRRYuu-RmrvRQjWGwF3zdIqOfiWRBG3DGedxgwpqFp5EDwR_rPYQCeN_g4-uWRyRzX21gBc4JfV0Liwy7edu_D_ZsFYZ-1syltAZyJwM7vtu6cgBHH73TD6-KkoOIhhKUYXkvGgGFo04cfWSdu0YOYRHsJUEyE2ZnqLZzlvgrGccCRpRZa7xvcMI3wDNkPj3quUFVkMpMHmtI9JFEMA2ro_oucY2lB_wD4390rIdIeChoj2GhbYmXPLwBYBtoFyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=L52u1P65q_Tanr0tD32-HvUwpJngUlNrmLI_OWrJ7CbSlMv_rq_TsBMvgCb6SXFrK8cj7A1XE5YBM5dFDwf2T_mRRYuu-RmrvRQjWGwF3zdIqOfiWRBG3DGedxgwpqFp5EDwR_rPYQCeN_g4-uWRyRzX21gBc4JfV0Liwy7edu_D_ZsFYZ-1syltAZyJwM7vtu6cgBHH73TD6-KkoOIhhKUYXkvGgGFo04cfWSdu0YOYRHsJUEyE2ZnqLZzlvgrGccCRpRZa7xvcMI3wDNkPj3quUFVkMpMHmtI9JFEMA2ro_oucY2lB_wD4390rIdIeChoj2GhbYmXPLwBYBtoFyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر:
هنوز مطمئن نیستیما ولی فکر می‌کنیم یه پهپاد MQ9 دیگه از آمریکا رو امشب نابود کردیم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/funhiphop/76211" target="_blank">📅 23:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76210">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">میدونم برای وصل شدن داری سرویس میشی، منم همینطور  ولی دیگ بسه بیاید یه چنل آوردم براتون سوپره کانفیگاش، کانفیگای رایگان میزاره که وصله همه کانفیگاشونم از قبل تست میکنن رو همه اپراتور ها، خیالتون راحت. کانفیگای اختصاصی خودشونو هم میزارن  خودم تست کردم عالیه
👌🏾
🤌🏽
…</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/funhiphop/76210" target="_blank">📅 23:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76209">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">میدونم برای وصل شدن داری سرویس میشی،
منم همینطور
ولی دیگ بسه
بیاید یه چنل آوردم براتون سوپره کانفیگاش، کانفیگای رایگان میزاره که وصله
همه کانفیگاشونم از قبل تست میکنن رو همه اپراتور ها، خیالتون راحت.
کانفیگای اختصاصی خودشونو هم میزارن
خودم تست کردم عالیه
👌🏾
🤌🏽
اینم آدرسش
👉🏽
📡
@VPNir404
👉🏽
📡
@VPNir404
👉🏽
📡
@VPNir404</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/funhiphop/76209" target="_blank">📅 23:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76207">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">امشب وحید جان خبر از چند انفجار مهیب و لانچ موشک تو جنوب کشور مخصوصا بندرعباس داد و تسنیم هم الان گفته به سمت ناوهای آمریکا و کشتی‌های تجاری‌ای می‌خواستن از تنگه رد شن چندتا موشک و پهپاد شلیک کردیم که خب چیز خاصی نیست خاورمیانه‌ست دیگه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/funhiphop/76207" target="_blank">📅 23:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76206">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcHqkIZPL5AmHMwvWLE1aGp1TfH7UpJv1W14Nuq7_XP3veM7GJy0URR1WRDCa0UnELf21tV1skm-2qu-34xgNCh5mTTDNkA9J6GowGkCLB0ihu6U1CXyVZ5evfUZZzZrnZf6DndIzwV5nkx-E5JeC4ZWbLOdJ9nWYcWanWRSR7epn1xYg3oXRIVocHSeswt8BaNFLGvbpg18Yk4o4Dfs4gJXbOzOxhYn7xFr1IrxohZuqLfS6dBFPU4rJ5mnpHv-Q9sPGxFXOJ9grY1zhU4b8xc5j1ELt6hHItzq3gmD7NiihVof5fTwW4gWCRajUE2yWEi5BUBbbyXd_fN0CZ45MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه داداش بخدا من خوشحالم از این که اینترنت برگشته و مردم میتونن وصل شن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/funhiphop/76206" target="_blank">📅 23:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76205">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">این گروهو زدیم که فقط میشه موزیک فرستاد
بیاید موزیکاتونو ول بدید و ی پلی لیست خفن درست کنیم
(فقط میشه موزیک فرستاد نمیشه پیام داد)
@Hiphopiplaylist</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/funhiphop/76205" target="_blank">📅 23:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76204">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نیمار:
حتی اگه جام جهانی رو از دست بدم خیالم راحته چون برزیل وینیسیوس رو داره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/funhiphop/76204" target="_blank">📅 22:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76203">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfibP6Saley513Ut3aCrcQcPxmXPvw8W4_mmMY_YDXBD3VQ2oXHsLRpF9tAhtEpfjwZ9aRo1ggPnbps9NIARYx0qmh2iavGki1YiPagzqX_onsKqnUZFvLjk2lEi1jOiNF4CcTENwPTRefDxjw3s7G9PNBCExwVfC-gWSUnHwJGGQTxk_EQuJWkgHSnQTF0ihdZwxcADq-F9c_5H4pKFcplhsnSngv6BCoxcHIVpCnG3qn4r3_gWcvMochhtR6fJLt-vsZcRuDriswwl0iZBbx25yXPCBNvjqeg1CD6Zcd-emSPHuYGU0wL5oDkVB0vg8FGSzeiyLE_a1d2gOb5L6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی انقد کصخلید یه توییتی رو باور میکنید حتی بدون این که به تاریخش نگاه کنید یا ادا در میارید
یا واقعا با این شوخی کصشر خندتون میگیره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/76203" target="_blank">📅 22:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76202">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نیمار تو تمرینات برزیل مصدوم شده و معلوم نیست به جام جهانی میرسه یا نه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/funhiphop/76202" target="_blank">📅 22:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76201">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مجتبی جان ،بخدا نیاز نیست برای هر مناسبتی یه پی دی اف ده صفحه ای بدی بیرون، ما خودمون میدونیم در صحت وسلامت کاملی
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/76201" target="_blank">📅 21:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76200">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">پرزیدنت پزشکیان:
ما مذاکرات را برای تحقیر و تسلیم انجام نمی‌دهیم، برای این انجام می‌دهیم که از اول هم گفته‌ایم که به دنبال داشتن سلاح هسته‌ای نیستیم.
ناآرامی‌ها در منطقه تقصیر اسرائیل است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76200" target="_blank">📅 20:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76198">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فرید رومانو:
برناردو سیلوا به بارسلونا
هیر وی گووووو
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76198" target="_blank">📅 20:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76197">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">من کاری به این که ویناک قبلا چیکار کرده ندارم، ولی تمام این فشارا بهش سر موزیکاییه که داره میده و اینه که سر پرونده هاش بهشون باج نداده و زده بیرون از ایران
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76197" target="_blank">📅 20:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76195">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-fJz5UK49PUF-EnLP8b4NXknuNDm1W6FcdGCdkiy5agM-gbcuzH23CJnFfQIPGlFJibWAMID5QrjOZ3L7ycqgErC0yUVVC8FzVI6xw2t7Qxjavm5ZtDCs4PRKErDgnRnxX7ljbXnJU2WsbHou4ORjsQDKSBHI_zzQ_Y4A7KygL5IXA7LMs6q0AoUJw6U_jSuw86zYcbq4MlGMmr92YmEpG19ftsUhqXawJ8OS1UEgkfjeqpEdhZf-gG9rLCIFCDE3ZDt7YfRmxrjh0k1eaE2t5bQN2s3nmfLUDUzua0X_hT9_X_EKJdKXOtVaxOCodNrXhpX1-ZFyO1vTBzoPeODQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76195" target="_blank">📅 20:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76194">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">امین منیجر سر کیری که ویناک بهشون زده و از ایران فرار کرده فشاری شده و داره میگه تو ایران بودی خایمالی مارو میکردی الان رفتی بیرون بهمون دیس میدی.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/76194" target="_blank">📅 20:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76193">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دوستان من تازه آنلاین شدم، ترک هایی که سورنا و بهرام بخاطر اعتراضات و حمایت از شاهزاده دادن رو بفرستید گوش کنم.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/76193" target="_blank">📅 20:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76192">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">یک دیپلمات ارشد اسرائیلی به شبکه ۱۴ اسرائیل: تا جایی که می‌دانیم، این توافق توسط رئیس‌جمهور ترامپ یا مجتبی خامنه‌ای تأیید نشده است. اگر توافقی وجود داشته باشد، در حال حاضر هنوز در سطوح پایین‌تر قرار دارد.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/76192" target="_blank">📅 19:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76191">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یک دیپلمات ارشد اسرائیلی به شبکه ۱۴ اسرائیل:
تا جایی که می‌دانیم، این توافق توسط رئیس‌جمهور ترامپ یا مجتبی خامنه‌ای تأیید نشده است.
اگر توافقی وجود داشته باشد، در حال حاضر هنوز در سطوح پایین‌تر قرار دارد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/76191" target="_blank">📅 19:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76190">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ek7TQK_FUOIlrzN2h-tOVZujV1nWGDisup4hAx2eOrZxHvQv1KbUm3MCjOiBh5XFVFAvGhEk6-zWAKSQfKWpI2R7nb8TP0Yop7hWERpa4qZPyt6iItCJ33S_gm2_72w71FhI1aPtrrBqlhEg0K5fkr9T-KSe3qdeFXJ_q5zsmPRUdsjVuQKusDNg6GjCUG1WkliSkjIwI8QIYSL0SzBe-OjweYqoXeRLr15X1OZjoJtCXTjMEOre7vyb3JDXsTYVhPanLBe4VPgM5eZF4OiEAy5-IK8V8X-SahHZtyUw_OlxzPIxcnlzt3N7ZgB0OosdMN6iLVuAg8W4eM17RcJjSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوری از آکسیوس: ایران و آمریکا در حال حاضر به توافق رسیدن و فقط تأیید نهایی ترامپ باقی مونده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/76190" target="_blank">📅 18:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76189">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">خبرگزاری i24NEWS اسرائیل: مجتبی خامنه‌ای، رهبر معظم ایران، یادداشت تفاهم با آمریکا را نپذیرفته است.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/76189" target="_blank">📅 18:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76187">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">خبرگزاری i24NEWS اسرائیل: مجتبی خامنه‌ای، رهبر معظم ایران، یادداشت تفاهم با آمریکا را نپذیرفته است.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/76187" target="_blank">📅 18:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76186">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">خبرگزاری i24NEWS اسرائیل:
مجتبی خامنه‌ای، رهبر معظم ایران، یادداشت تفاهم با آمریکا را نپذیرفته است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/76186" target="_blank">📅 18:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76185">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا: ایالات متحده قصد دارد دسترسی خطوط هوایی ایران به حقوق فرود هواپیما، خدمات سوخت‌گیری و فروش بلیت را مسدود کند. سازمان مدیریت تنگه هرمز که توسط سپاه پاسداران تاسیس شده، مضحک و خنده‌دار است. دولت ایالات متحده هیچ تلاشی برای تحمیل سیستم…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/76185" target="_blank">📅 18:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76184">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا:
ایالات متحده قصد دارد دسترسی خطوط هوایی ایران به حقوق فرود هواپیما، خدمات سوخت‌گیری و فروش بلیت را مسدود کند.
سازمان مدیریت تنگه هرمز که توسط سپاه پاسداران تاسیس شده، مضحک و خنده‌دار است.
دولت ایالات متحده هیچ تلاشی برای تحمیل سیستم عوارض در تنگه هرمز را تحمل نخواهد کرد.
روزهای ترساندن منطقه و جهان توسط تهران به پایان رسیده است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/76184" target="_blank">📅 18:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76183">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">آکسیوس: توافق در واقع همون سه‌شنبه به دست اومد؛ حالا فقط تأیید ترامپ باقی مونده تا همه‌چیز نهایی شه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/funhiphop/76183" target="_blank">📅 18:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76182">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">واسم سواله سود این تفاهم نامه واسه ایران چیه دقیقا؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/funhiphop/76182" target="_blank">📅 18:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76181">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">جدی جدی حزب‌الله و مثل آب خوردن فروختن</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/76181" target="_blank">📅 18:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76180">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">فوری از آکسیوس: ایران و آمریکا در حال حاضر به توافق رسیدن و فقط تأیید نهایی ترامپ باقی مونده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/76180" target="_blank">📅 18:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76179">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فوری از آکسیوس: ایران و آمریکا در حال حاضر به توافق رسیدن و فقط تأیید نهایی ترامپ باقی مونده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/76179" target="_blank">📅 18:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76178">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">فوری از آکسیوس: ایران و آمریکا در حال حاضر به توافق رسیدن و فقط تأیید نهایی ترامپ باقی مونده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/76178" target="_blank">📅 17:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76177">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فوری از آکسیوس: ایران و آمریکا در حال حاضر به توافق رسیدن و فقط تأیید نهایی ترامپ باقی مونده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/76177" target="_blank">📅 17:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76176">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بنیامین نتانیاهو، نخست وزیر اسرائیل:
ما باید ماموریتمان را در ایران را کامل کنیم و من هر روز در این خصوص با دونالد ترامپ صحبت می‌کنم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/76176" target="_blank">📅 17:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76175">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">روسیه:
ترامپ با انتقال اورانیوم غنی‌شده ایران به مسکو موافقت نکرد
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/76175" target="_blank">📅 17:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76174">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5XLEkM-AnSrq3Gz8SvOlrq1lDIvl80IpYxmR1iJi0yhf5NskbWl6l8LZ7JMTG3i0Cf-lzbjkuG7fSMpFMDeDzOdeIEyr1tl9LFkOywmPUXqdph2auhgMcIDAj9DDJ3cigWOkRASCqlQ-bhguCGTH9PXEp6KxPZnBoKSfvPpPz32Ym8HJrJFp56eNoP5CNYh-sSVOcoZEjgL_jsyZzDBjQX9GUfpElbea0qmWGHPf1_Nl5_eFkE99gQVzKT_nB7vai4YCXdt-Gtq6tLHIRGiSZvH20oBBK6Ff1aOuCY35FSCSE4VkeaHfoH1V9N_AhXhqEbeDFaqVeQthD1JicEc9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و اما مسعود که بود و چیکار کرد.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/76174" target="_blank">📅 17:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76173">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bL-Uv9O-uhTIwi2s0Lwtxh0IPQlsIWIivBPP8FXKBHrJju4tXmsPIDPiqSrEt7a70KjVfnFL8f6SyJpwDi0siZTnSpwtWfUXsn5bBvnGa6CavwXbUTmv3SHhxsCi9uLywidZp8CvOuBXax6q2zR43iMIvFZD_mKgGtsPVvU5zia-RvyhoBpnN1c-TUI1RdlvlQ4dpH_Mlcf7npBv38_dKQcNOEwdxEQ8c5NnixREahSOms-NGWt0vsmPtqpsYmpgQfmnTkelR_yhKQYQKhcuZAtK5CzEt5vzIgHSDxcdOHKy5oEvdAnGlhToC4pEVNw3co7I0fvDexoTEyo3z4JHBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
سایت بین المللی
bet120x
✖️
👍
دارای مجوز رسمی Gambling Judge سوئد
👍
💳
شارژ حساب از طریق ارز و
یووچر
و پرمیوم ووچر
💳
تسویه حساب دلاری سریع
💊
بیمه شرط میکس
⚠️
فروش شرط
🔔
ویرایش شرط
3️⃣
2️⃣
🎁
20%هدیه واریز از طریق ارز و ووچر
┅━━━━━━━━━━━
🎁
10%برگشت باخت به صورت روزانه
🎁
10%برگشت باخت به صورت هفتگی
🎁
10%برگشت باخت به صورت ماهانه
💻
ادرس ورود به سایت:
https://bet120x.com/fa/?btag=971470
➖
➖
➖
➖
➖
👈
آموزش واریز و برداشت دلاری
👉
🔪
کانال اطلاع رسانی:
👇
g7
🅰
✈️
https://t.me/+RvVnWMHCqUc4YzFk</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/76173" target="_blank">📅 17:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76172">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گزارش های تایید نشده: فرمانده توپخانه حزب الله توسط ارتش دفاعی اسرائیل ترور شده.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/76172" target="_blank">📅 17:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76171">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AyDFdV8myp-VC1bPbiHZ_k8j5E83Nd6elP_f8LxbyjV7fSkVNKiJcfgB59vqCmngycSgoW3PlS1j3TZxs5bq6v8InxvsYO4JbeQzUwAAUnKzFeh9j1nZi8eqh_FGzcBahlAN5tiyQMBlX52jw16Pp85JGrJEqXB5uwkup-z34Zn4RHp110uJxOeatncAgQO5vaQJRfuS_Hzv2kdUppA1Kdz4K37n4umQ2J0pV1YrPua7HPHpZIOE5s42oeGq7qqjAynIt9Ah95VBV1x6uHuLkxYnM2cfE_fGsKyVhI52e3KGu7eWPmO0tsqpw-EkAd2S2Haq6M3BZX8Onxq7t0k1-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون همیشگی  @funhiphop | reza</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/76171" target="_blank">📅 17:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76168">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">الان وضعیت جوری شده نه دیتا سنترا کامل باز شده کانفیگ فروشا بتونن تانل بزنن ارزون بفروشن نه دیگه مردم کانفیگ گرون میخرن، همه به یه استوپی خوردن که معلوم نیست چخبره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76168" target="_blank">📅 15:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76167">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">من الان دقت کردم موزیک یه رپر نو نیم به نام مارسلو تو چنل ارشیو بیشتر از ترک جی جی فوروارد خورده، بعد این پلشت میگه دیگه کسی ابی داریوش گوش نمیده مارو گوش میدن</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76167" target="_blank">📅 15:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76166">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQFuGvWNJZpKJPHynrKRW78Pqz_RxalefGyCp_deko-CpDlWbwGMqHeO1r9nOU46KzORkK1oU42FjU1aNDFO98c75JDoBkEZ1yNgjBTWty4NDXnaDMW9LHYApLK-4EpjZsbOeSz_7CLU-pLLcG5G9PA1fw1ijEDDMUKlA9AuPWFowrDX9lvNDlJYkCrE9AVG4LDcnTbeP7PZhNCTfcTloXeYFwrcLeg95-wQ6AjF6jAS-NQ6CK6lQTto_ullS7cYLUalW1eo5F1UijagiA9PEFnJGrc7UZoOZgfigo9iGFfCYKD3SDc0qgPCqDjBLtzYgazwKmGrS_KA7Z4Lf7xkCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به اسم پس میگیریم منتشر شد
Youtube
Download
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76166" target="_blank">📅 15:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76165">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ویناک ترک داد
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76165" target="_blank">📅 15:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76164">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سنتکام: حمله صبح امروز سپاه با یک موشک بالستیک به کویت، نقض فاحش آتش‌بس بود.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76164" target="_blank">📅 14:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76163">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">با شرفی ازمون تمدید شد
سردار آزمون از لیست بلند مدت تیم‌ ملی ایران هم خط خورد و دیگه به جام‌جهانی دعوت نمیشه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76163" target="_blank">📅 14:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76162">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">کانال ۱۲ عبری:
منابع آگاه از مذاکرات خبر دادن که طی ساعات اخیر پیشرفت نسبتاً چشمگیری از لحاظ رفع اختلافات میان ایران و آمریکا صورت گرفته هرچند که چندین اختلاف همچنان بین دو طرف وجود داره.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76162" target="_blank">📅 14:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76161">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بارسا که دیشب گوردونو خرید امروز هم برا آلوارز پیشنهاد رسمی فرستاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76161" target="_blank">📅 12:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76160">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بنازم پرزیدنت پزشکیان
جوری اینترنت رو باز کرده که آدمایی که موقع نت ملی وصل بودن الان قطع شدن
@FunHopHop
| ALI</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/76160" target="_blank">📅 12:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76159">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یه لحظه یادم افتاد قبل جنگ یسری جوک ترند شده بود که میگفتن "کشورو بدین دست وی پی ان فروشا چهار ساله دارن یه قیمت می‌فروشن و گرون نکردن"
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76159" target="_blank">📅 11:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76157">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">صداوسیما رو باز میکنی حالت بهم میخوره، هر اوب زاده ای رو آوردن تو هرشبکه ای داره تحلیل جنگ رو میکنه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76157" target="_blank">📅 11:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76156">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBJGO-s8eCCqidgwAyUhdfO7XbjbBd5oNDgze4Mcfnd2AOzoE5uBzNU0hMowq2Aug7-zs7TeeiNCwvbRGeQm39-Lbl0jZfOZc6P9CMstl6hWlMv9ozY6YqrXHY2yEwBiCAlXXpU6Mdl5hmoZhPE03xAXARVl0Z_gs0jMAg6kpTukRzNxzvapCmsx-2kMKMAuaeLG1--OTEYfa5ejUDfmvp9InRiiyW-hQhpxrQwwYJUClWTZptXAMWqEP5u5R_Tgbu034ezZa6rc-8isqlg54nn3tg1TJwZUUcfqiLdnpsHq-LD5bShYmHo4NWQSwp-QF8VKc1uf9zZAOsDGLRVhqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکایت وصل شدن اینترنت
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/76156" target="_blank">📅 11:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76155">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVwvpMLi8V0oxG8we2_Zz01qCjwDqhCnyJQisRz9dTwdEjNEgUv6S3whNJeTVLVzv4-amEyO7SJunnLG-dMRwqT18Dzo9Hc_cCd9xwld9hb4TE7WCkxYhUXmWEFCh1exzHK-CMj0JLbktf4G0zkJXjkF6NbYx5W8c64QY9K8ZnhL6I9Blz2aFF64VD5L3tBEUB0AsmzmEebH3byxvfVZDJIp007daCRU63J5ympyni_ZR44xocME6-44UvHcZ9FZvQOF42Psi-V9jXSnNT7Jif2DjNTpT4GA2KIRZoRptjT8Ukp8qNg0Fyl8fdZu8cPu2g3KUm9Oy_N3VRCdKxS4Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امسال عجب کیتای شاهکاری داریم.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76155" target="_blank">📅 10:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76154">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بامداد امروز بعد از شلیک موشک از امیدیه خوزستان به سمت کویت ، صدای انفجار شنیده شده و ستون دود دیده شده که ظاهراً لانچری که موشک ازش شلیک شده بلافاصله توسط ارتش آمریکا مورد هدف قرار گرفته
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76154" target="_blank">📅 10:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76152">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Krz1DplrVWMBfh3uV6YREtnF80DK33dYRT8kl7G2yRIi4uE-CF4YW4AL_uEyMXRpqbyNsYhHxC_oWTwd0EHj-m5_17ydTgpRDkQcPMMV_pkuPRwZdseAVqo-yBQKd-ZVzPoS5iiq1_5McVMRW77C_PmuwMykDMqG4UIr9klP3KuYKAnX1-ZTfnyLmAmW137JVlYXu3Y0PstOdzLQjQG9iHPRTKBAlkb-4_DbvEsTXQBE8gxn2c-uJaBxzg4nzSGO3eBgd0wEiFa0v0h4aAsyy4tXhRIzedF2IYk-Qy8X2VwUteNvQYkoo57hQieUWCv7Ye6vqoiFYBLMg15r3ujKHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S21rO_z-LY8bGTmHx1yp0sWkcLYvNploTbBlEccH4Ojpsr-7KLq_1ueU6IEKZIqDRC92rYwxkHE9j7RM2d056at1IMlOiY2cIkEuoqkdnNC5E6WjqUu53bhECVtYFVjIyHAgzoVbeQnrqldc1tFiQHWB6S_ruXhTScKJ8G7-IURe0BzU8mQe0AE1kAsTWGSy8IBORT9mTnReNg8nGq3JPl14IcbFZ-AL3GXqMOD8lG2eTjUIv1XHT8T3PLK9azFtG1ftZn4BG2tcKt8_EFcXasy_1wUPp1k3DOc7ijrdkGjgZ9-mZJezuuMx1MJH-fAJQIUqtVaFQjTZU5hDXkpBSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از سایز پات معلومه اوب داری پسرجان.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76152" target="_blank">📅 10:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76151">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTmrK7EBu9q_wqJSufaEz5Hdmcm0n8bTV1yrLjgJW7xGj5CL_afeK-2qImFVBgF6Ez9dWp6UKnUHKePb_Kj43ZSAewC_o-SMEWcXHbZC9BBcYlU7iX4FD1OTDgH3IrB43agsUYrzLzrdyeH-myO4U4ngFlm5BLsHYz-rFqUSG7Enrb4HEynfxDnug19v9mIG1Zq6amd7TWs6NoMIXj2Ra0JtyhAtWUT6dmmKp3poNJRkI-tK3y-oYEzPM0quLeSBgGw4JTO-kRfcir1V-wJq8bPgcwdXiffJzkh4q1dqxvWgPQoIZU3Ju2RopxT2XgpyenQX5Muko_cBbvVSTljhRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این توییت هیچوقت قدیمی نمیشه.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76151" target="_blank">📅 10:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76150">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtRbpfpO9sWhSnP1tw8L09zLi0GmB1MDgfQfi-6HY5Mb1ms0nY4Cg4wIinRqEIiCABoQ-5suB3WBY3jmRODxWligbCIQjNDA3sFMtjEUdZqJpbp3Gq_SlrRLW6TH4k0B4Aixo5xscwWHuEkNVCCgnJbGRS8jhQi8ydfwPEloaNvvdY4vUwqGiCxhlWuCY5vbvHTCERfVUNy3GAWKMYqD3KDge_yAV5azwmCFyVjo3iL_8y1FZJUxFIHVVOIbXXmvm3Z8uFdT6fpY2WR1lUbi8RZAOe1d1UBkTz640k9cNDF0fPuar33w5AsZJJiHhaQsmSCtKYTUybMLcI_9CIAtow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیمی نام ببرید که توان مقابله با این طوفان را داشته باشد.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76150" target="_blank">📅 10:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76149">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/76149" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
💰
اولین سایت جهانی با امکان شارژ و برداشت با کارت بانکی
🔹
برای ورود فیلترشکن خاموش کنید
😀
Telegram Channel
👇
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/76149" target="_blank">📅 10:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76148">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdGT3ntjICOI3aJs_qzdbafsdmGlhXw15NS0CCnKwidGmchxn4i2TZvNjnbN0NG0LF2O91lp_Bd9oFiBfzEvKqbOxY0JC3AtqPAqeqEID7eB2P5hjIl9BP28C-kewG3cZHBYoBpotJ1rueAAg6zJdWRwC3e6cGKUBdGFqgTnaJeugRjdYSAdZxt8mEeQHgHtSrsB5XMMtNLvlt4GGq-AibN4c736RfW_MIiztNZuD-zez3MsSclKWuur2f8bJGA3_aUngfOI4ZZFKSEva3MAA5tkD0QMHfwZaBXLhuJfFNZ2tRvfRuHu2emJIs0_CH92C7FK2sDwKsB5Ht0D8nsgew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت :
👇
r7
🅰
✅
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/76148" target="_blank">📅 10:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76147">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPUgTj_yL29KQFlK4jeMcCUOKEvgFPTni3RcZtP-ihN3ZtVnLibjus6PwroIxlpV4Zuamn24h3WUAcwK0Cmg5K5ZvdZqzkpQKHUVSEvjx6z86zh8JrVeai8dDSVMfrwEi2-Ylc57W_8dAjCiq16NXbiotlyQDNRqdTdhbP-DhsKw3w0ZyYHgcz7qdzgNq11q5rMq2QD6Ya0EDbt7lGtY2KWoo6x0SQ2RsTIny5Ufxlzn4hWh9y6TZXNo8hl1LuTaee306pXY_KpujJMRoQVeepgBrd7CIARyN1aJarDX4acfNFJvBiBvV3mVEzc3D8jICO52iP4QUmWGCbTygNN1bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با شرف
🇮🇷
🙏🏼
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76147" target="_blank">📅 10:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76146">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=uPDzlW0P7Npr2-mdW_CYrqXyFk1zYszRYfkAa1bkAiASZIESgPkuucYQ6Oow_RJBmv6hdwJFRWhNWkbLajuJ8y6olecZhaeqxgEwFRC6Di3EFDn1ukYanVDLNQOz5z0ZIJyF8UUy9rqsyMncQGiJ_fHmTQoPiljh2h6pqdKSCZO21wUXk0NsJ88Vo8388UfxatXkcMqsyVIbA_wszuI06v9Sr_CkiQ3bg8BSdiQo13icvGT95nJ9FdwRLfM602cITvTMpLh4VfAZfFO0FwxFN02DmXXnUjYj_QrFmnxX7N1XZobT8tUdYlK-sj5mP0eMaCeQrlLeRrA1wshJOS45jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=uPDzlW0P7Npr2-mdW_CYrqXyFk1zYszRYfkAa1bkAiASZIESgPkuucYQ6Oow_RJBmv6hdwJFRWhNWkbLajuJ8y6olecZhaeqxgEwFRC6Di3EFDn1ukYanVDLNQOz5z0ZIJyF8UUy9rqsyMncQGiJ_fHmTQoPiljh2h6pqdKSCZO21wUXk0NsJ88Vo8388UfxatXkcMqsyVIbA_wszuI06v9Sr_CkiQ3bg8BSdiQo13icvGT95nJ9FdwRLfM602cITvTMpLh4VfAZfFO0FwxFN02DmXXnUjYj_QrFmnxX7N1XZobT8tUdYlK-sj5mP0eMaCeQrlLeRrA1wshJOS45jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیانیه‌ی سپاه که توش حرفی از نقض شدن آتش‌بس نزد:
بسم الله القاسم الجبارین
فمن اعتدی علیکم فاعتدوا علیه بمثل ما اعتدی علیکم
به دنبال تعرض سحرگاه امروز ارتش متجاوز آمریکا به نقطه ای در حاشیه فرودگاه بندر عباس با پرتابه های هوایی (گفته می‌شه تلاش برای ترور یک مقام بلند پایه تو ماشینش بوده)، پایگاه هوایی آمریکایی مبدا تجاوز، در ساعت ۴/۵۰ دقیقه هدف قرار گرفت.
این پاسخ یک اخطار جدی است تا دشمن بداند، تجاوز بدون پاسخ نخواهد ماند و در صورت تکرار، پاسخ ما قاطع تر خواهد بود.
مسئولیت عواقب آن با متجاوز است.
و ما النصر الا من عندالله العزیز الحکیم
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76146" target="_blank">📅 06:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76145">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">فان‌هیپ‌هاپ نیوز:
بازکردن اینترنت نشون دهنده پایان جنگ نیست/ تقی به توقی بخوره باز قراره ببندن و همین الانشم درست حسابی باز نشده. وآماده قطع کردنش هستن
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76145" target="_blank">📅 06:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76144">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نمی‌دونم چرا و چطوری ولی همین الان آژیرهای خطر حمله‌ی هوایی تو کویت روشن شدن.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76144" target="_blank">📅 06:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76143">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmsBqz5o0567dOrFcyzzs-JhdLK5VFN__-tk8pFT3nfn-Hr_LOa6ADGvUSbzK6pAh2mxG-hF7renR_SC1nLGdG7ANzCqiKvLTXHq1zLeT4cYMF_vx49sePRZBIYOxuRh6uWCC8SamBHzhjxFHxSS17WiivjoiXb_3--ewXVdRU0fbHmzwzV8r2BKS2ll8lt_cgh6pnkpcHKEO0CTqAkHu1kgMm-_UiQIG-SmM5p8f83T8054yeHJXxqlmLN6XPJcmL2jCWmN_99f2ja_1Rh_Y9DAqykHLvUQ8iMECXJStrfZH-S5M05as_OqTNeE-NfqDcyjGVAo-gJqlRNiEa44dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمی‌دونم چرا و چطوری ولی همین الان آژیرهای خطر حمله‌ی هوایی تو کویت روشن شدن.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76143" target="_blank">📅 05:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76142">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اشتباه برداشت نکنید، قطر داره پولارو با جنگنده جابجا میکنه</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76142" target="_blank">📅 03:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76141">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">به گزارش رویترز، ارتش ایالات متحده حملات جدیدی را به یک پایگاه نظامی ایرانی که تهدیدی برای نیروهای آمریکایی و کشتی‌های تجاری در تنگه هرمز بود، انجام داد.
ارتش آمریکا همچنین در جریان این حملات چندین پهپاد ایرانی را رهگیری و سرنگون کرد.
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/76141" target="_blank">📅 02:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76140">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">فارس: سه انفجار در بندرعباس  @funhiphop | reza</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/76140" target="_blank">📅 02:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76139">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYashar</strong></div>
<div class="tg-text">کانفیگ فروشان با پول کانفیگاb2 خریدن میخوان نتو قطع کنن</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/funhiphop/76139" target="_blank">📅 02:18 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76138">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">فارس: سه انفجار در بندرعباس
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/76138" target="_blank">📅 02:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76135">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سلام فرید جان بندرعباس صدای انفجار میاد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/76135" target="_blank">📅 01:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76134">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMmAtw3mMkByipdLsoPE2wvxjFc0n6h96wOCDBQsgJtbfK-nd94e88P8Ku-bh3gPWDnFshM864QI1HLjgpEtLHk4dYx-XETDpN6-a6JtW8rvNVs1KE8NE9etMB_p4JlzS6v4iN1klLr__rXNcNYUk5Rgnk_jUeyh2rpjzuBZ1PHRAFaeVbkKgFAGt0vVF0g-9qnS_ijLTzyL_Tn3W8PjOWXnubxPDQ1qgzI3_p3mXn578sUXUVD2lIdnsznxEgiWrOVT5EWRaxSfLVc07L_wygKJ9Ly7vDCE4yunP7xK_034gAi4J0fkTo_YlD1-Pk8Ul0jQHNgqQ3683dAhXY4yRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفسور ابراهیم عزیزی، رئیس کمیسیون امنیت ملی مجلس:
ایران با سخنان تهدیدآمیز ترامپ از خطوط قرمز خود عقب‌نشینی نخواهد کرد:
حق غنی‌سازی اورانیوم، مالکیت اورانیوم غنی‌شده، اختیار بر تنگه هرمز و رفع تحریم‌ها.
واضح است که ترامپ، در جستجوی راهی برای خروج از این بن‌بست استراتژیک، بین صدور تهدید و درخواست توافق در نوسان است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/76134" target="_blank">📅 00:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76133">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گوگل پلی مثکه رفع فیلتر شده
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76133" target="_blank">📅 00:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76131">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">این مشکل سامسونگ که بعد چند ساعت استفاده از تلگرام تلگرام هنگ می‌کنه رو شمام دارید؟</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76131" target="_blank">📅 23:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76130">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JR5yKJFO1Z6geQpOwviiQV2CFM4LM0bkLoTu02DzakeyMPwFPFTWLdvNbfspi_L6_UGx8MnSSysppLFHnAGpP2-oswMA6GugOTUGDnA6dafuMo-fTlHX0KjPZBkxCkyv1UfO2d9ALl3EEbjekOlGdVkwIUT1Y0i2gkLnw8snNIAdirSRhVdsz0g315FBHs3mDXxwxx9SHTfuE5VEIdd3LRGQQh1AIFZFRAWM2MBwk2s6c1ea2o56g78FlTJiIaA-lyhWr59-92CPKujUokDpi3ONWwHj2y0St2aamrls8a2OjvkzA78UA31gitQKwD2PTTVonjXa8KHathEACWxjjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
1.00 ton = $1.904
💶
327,221 toman
💰
درصد تغییرات: 5.98%
🔴
مقدار ضرر: 0.113859 $ / 19,568 toman  1405/03/06 | 23:41:05   @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76130" target="_blank">📅 23:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76129">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0mOpH_gqPK1aJydB46BV0r9dcir8pK7gLeTD6_WX96n7FMivJz-aUD-fKZNJp_kgugBn9I-WZkAT-Gt2rQYqb-0BPRhEL5KxxKpDoiUFegeo8fTuZPiWxMTHaHGHDUMBbo1KUoiDRVgescxd9acVt7I-pzbnc4I7PPWjn3tch3pG2JTJkR3Y2sw5rP4cvDsSP-VhQyaCbRLVT3rA1237bDffoIZ0NMixUVRV6FRq6xxhuCVZRh0ctY4klx_b7Tpj6F9QhJGTlTX0ypK9NcMkPet-hY3jo39f1D7eO9bzNXYHWP1V-UjBaRASSj__B1vBGjBmA5JtfQU6yVm0f_IhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
1.00 ton
= $1.904
💶
327,221
toman
💰
درصد تغییرات
: 5.98%
🔴
مقدار ضرر
: 0.113859
$
/ 19,568
toman
1405/03/06 | 23:41:05
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76129" target="_blank">📅 23:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76128">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سخنگوی ارتش اسرائیل:
ارتش اسرائیل دقایقی پیش دو تروریست ارشد سازمان حماس را در شمال نوار غزه هدف قرار داد، جزئیات بیشتر بعداً اعلام خواهد شد.
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76128" target="_blank">📅 23:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76127">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اسرائیل هیوم:
ترامپ پیش‌نویس یادداشت تفاهم با ایران را به نتانیاهو و رهبران منطقه تحویل داد تا نظرات خود را اعلام کنند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76127" target="_blank">📅 22:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76126">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izZgb9aBhsJ9wvm0KDP85y1954UNcDOpwtabey-_ykt-7bd8d6LiKkPvdrvC_qIBe1IFuPmdwnwLuutnJC7uTK519BwqxtZ0SIPdrYjpADpBJFEkkNVC4qnq23BpoRdWuarWXOv13eIlX9YQzykwMpRmMmd_0jYOt39kADMwmjuiTrk3fJYD6SVyOze1Bt6MoR7mAl1gos17uN_3vujokwPYM1hkAFKJo_WgEDiZBUoLgOzZx1lCUv3LmowLMflwyhn7luaQNO72mlOALZ2u03Y54JIE-CJPOlTPFBq5fXKBOTFFCHixXlFrzEm8ox8TV7OBP99cyTq53wIm7eOejQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکنه رئیس باند فروش کانفیگ ایران لاپورتا بوده</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76126" target="_blank">📅 22:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76125">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اسرائیل همچنان داره لبنانو میکوبه
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76125" target="_blank">📅 21:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76124">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نکنه رئیس باند فروش کانفیگ ایران لاپورتا بوده</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76124" target="_blank">📅 21:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76123">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ:
عربستان و سایر کشورهای عربی به ما بدهکارند، اگر آنها به پیمان ابراهیم (عادی سازی روابط با اسرائیل) نپیوندند، من فکر نمی‌کنم اصلا مذاکره و توافق صلحی با ایران انجام بدهم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76123" target="_blank">📅 21:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76122">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">با تایید رومانو آنتونی گوردون به بارسلونا پیوست تا درصد اوب بازیکناش از میانگین ۹۰ درصد به ۹۵ درصد برسه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76122" target="_blank">📅 20:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76121">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامفض:
این کاملا رژیم چنج است. ما یک رژیم را از بین بردیم، سپس رژیم دیگری را هم از بین بردیم، و ما الان درحال مذاکره با رژیم سوم هستیم و خواهیم دید.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76121" target="_blank">📅 20:52 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76120">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ:
به خدا من می‌خواستم بزنم ولی فقط به خاطر روی گل عاصم منیر که خیلی دوستش دارم و درخواستی که کرد به ایران یه فرصت دیگه دادم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76120" target="_blank">📅 20:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76119">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db6012f650.mp4?token=NGBTLdVazMnK_vfcF2NZRz1YRiQ-EnRyFoSZxG0jOUCX6MwDMvAqLUaDw7V7fJG7GeD9u2odLpFRbnU3SuDJ_VzEbxNkNxn9LPAsFZbtBxpS7LPTDeQBH7yF44tzJ7O2kKDUKes5Dbm56b0lgok4vIvzUBqxgZS4XwOr8DNHNtIQBPKxCL53Xepv2K4ds2GVuG348KIw5M618yv4YuNsELtrItUbu5_Iu23VtT_oA-PfJ-yKG5V9ZHdv6-qaPFQr5W189DqyjIu4Qv_XDIj22we9l9M2mdxFfWwfd4_dljyIHnUUTuBSBYjL1mpJhNrxDnzfiuJ226BrkX6mwdrKLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db6012f650.mp4?token=NGBTLdVazMnK_vfcF2NZRz1YRiQ-EnRyFoSZxG0jOUCX6MwDMvAqLUaDw7V7fJG7GeD9u2odLpFRbnU3SuDJ_VzEbxNkNxn9LPAsFZbtBxpS7LPTDeQBH7yF44tzJ7O2kKDUKes5Dbm56b0lgok4vIvzUBqxgZS4XwOr8DNHNtIQBPKxCL53Xepv2K4ds2GVuG348KIw5M618yv4YuNsELtrItUbu5_Iu23VtT_oA-PfJ-yKG5V9ZHdv6-qaPFQr5W189DqyjIu4Qv_XDIj22we9l9M2mdxFfWwfd4_dljyIHnUUTuBSBYjL1mpJhNrxDnzfiuJ226BrkX6mwdrKLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
ما اکنون درباره هیچ گونه کاهش تحریم‌ها یا پرداخت پولی صحبت نمی‌کنیم.
ما کنترل پولی را که آنها ادعا می‌کنند مال خودشان است، در دست داریم. ما کنترل آن پول را حفظ خواهیم کرد.
وقتی آنها به درستی رفتار کنند و کار درست را انجام دهند، اجازه خواهیم داد پولشان را داشته باشند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76119" target="_blank">📅 20:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76118">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ درباره ایران:
آنها شروع به دادن چیزهایی که باید به ما بدهند کرده‌اند. اگر این کار را بکنند، عالی است.
اگر ایکار را نکنند، هگست (وزیر جنگ) ادامه مذاکرات با آنها را برعهده خواهد گرفت و کار را تمام خواهد کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/76118" target="_blank">📅 20:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76117">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6a042bbf.mp4?token=uggneO_uO7jwl7tOC6zMd6NgU0ufyW7ca4EdZ6tost-rt9BHMe55ISYqmFsqxvnNNVtathHyT28e2qOA9NCddvsKjDJbLJM2B4-mnW6iXI8bLzHXt3xgDqCSzAvljFAeac455UJ6P3DPv4IdfnFURLIVbJ5tWqrj31foymuC28uFqKkKPFyDz5r5-VIqhJeD3dMafyPC5DRiRXFBD8cLsf8_lxIBwUex3XPhIKhABqnJ2QhwrwkVNU2oZNNt3vSVhzNapQKyjSC4V6nf1Do3gVi7l8Ef2l2SSzf8y1R8UUiAxUhNCYTVzo2XWSN7pgb3UtT_kw5o35wZuHKR-04x6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6a042bbf.mp4?token=uggneO_uO7jwl7tOC6zMd6NgU0ufyW7ca4EdZ6tost-rt9BHMe55ISYqmFsqxvnNNVtathHyT28e2qOA9NCddvsKjDJbLJM2B4-mnW6iXI8bLzHXt3xgDqCSzAvljFAeac455UJ6P3DPv4IdfnFURLIVbJ5tWqrj31foymuC28uFqKkKPFyDz5r5-VIqhJeD3dMafyPC5DRiRXFBD8cLsf8_lxIBwUex3XPhIKhABqnJ2QhwrwkVNU2oZNNt3vSVhzNapQKyjSC4V6nf1Do3gVi7l8Ef2l2SSzf8y1R8UUiAxUhNCYTVzo2XWSN7pgb3UtT_kw5o35wZuHKR-04x6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
آیا از این موضوع راضی خواهید بود که روسیه یا چین اورانیوم غنی‌شده ایران را بگیرند؟
ترامپ:
نه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/76117" target="_blank">📅 20:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76116">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ درمورد خبر صدا سیما مبنی بر اینکه تو پیش‌نویس توافق گفته شده تنگه توسط ایران و عمان کنترل خواهد شد:
تنگه‌ برای همه باز خواهد بود و
تحت کنترل هیچ‌کس نخواهند بود صرف نظر اینکه ایران چه می‌گوید؛ ما مراقب آن‌ها خواهیم بود.
عمان هم باید مثل همه رفتار کند و اینکار را نکند، وگرنه مجبوریم آن‌ها را منفجر کنیم.
🙏
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/76116" target="_blank">📅 20:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76115">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEjXWQ2FSRH3_YknWDSyRLCO6xfYfjcGrnoij5RbjLnZercEH3O3YaVU1Bqihit1F3KGAOyHwEyVlwz3yPj3e36FuK-JbtAVYysg4nKvIAcH0NSclxbGtRI6cyZ5cLCWYRA5RjXddHx6U1ur_4b4D4D4i9hQlEIQzJT4RkD7yAM6XQZccf2H352knCSabTpXPQgetE8OZh9gimDAGfIQciz9u0TYSEuzU8kKYkX8LQ5T6V48fq-ARFzsTqZiOPy2EIuGbKOV6_RVTvZhPtcmDi2JmLYed8vSjM_wFHUmkKCdgzGO10PjobbA3EilFIAuu9wc81IV8quNfx7aeZ2uKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/76115" target="_blank">📅 20:18 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76114">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c4635a829.mp4?token=cu-jfVeiCfPsORFFiKJwHqCZh_tODle0LE0rsS0vscMLHGQBuGCcRJuTPKOZ-02sLHyybPjMI3X2c5lSj69Ec12soqzYEP833TkVi189YaeJL_NVsGasGSbek3aWeVNcgkmqo6nVjysKAU8aq0vw4_gD3FdwIbh4QTqBYl6UlWMMmC1x4Br1vigQDOCiTa5K9g_P3QRSxy8dOgqlSkJzgc8B94DBZ9Vn3B3UEc1B0LjMj6o9stkPQDioPRzGPmg6u0fX7KliNO7C_5VRqVP71n8KCxDpNtqPE0GJd-qhnzEHexIAm_vTvUcKNuod_ocYa540gnq_TOPkrql3jBLzbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c4635a829.mp4?token=cu-jfVeiCfPsORFFiKJwHqCZh_tODle0LE0rsS0vscMLHGQBuGCcRJuTPKOZ-02sLHyybPjMI3X2c5lSj69Ec12soqzYEP833TkVi189YaeJL_NVsGasGSbek3aWeVNcgkmqo6nVjysKAU8aq0vw4_gD3FdwIbh4QTqBYl6UlWMMmC1x4Br1vigQDOCiTa5K9g_P3QRSxy8dOgqlSkJzgc8B94DBZ9Vn3B3UEc1B0LjMj6o9stkPQDioPRzGPmg6u0fX7KliNO7C_5VRqVP71n8KCxDpNtqPE0GJd-qhnzEHexIAm_vTvUcKNuod_ocYa540gnq_TOPkrql3jBLzbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا جی جی مصاحبه کرده گفته پشمام ریخته که جوونا هنوز ابی و داریوش گوش میکنن چون ریتم آهنگاشون خیلی چرته   @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/76114" target="_blank">📅 20:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76113">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">خبرگزاری مهر:
آتش‌سوزی در یک ساختمان اداری در فرودگاه بین‌المللی امام خمینی در نزدیکی تهران، پایتخت ایران، رخ داده است.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/76113" target="_blank">📅 20:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76112">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مارکو روبیو:
دیپلماسی گزینه اول ماست اما گزینه‌های دیگری هم درمورد ایران وجود دارد.
ما معتقدیم که پیشرفتی در جهت رسیدن به توافق با ایران حاصل شده و در روزهای آینده خواهیم دید چه خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/76112" target="_blank">📅 19:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76111">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afe37ba190.mp4?token=Ufp3hTn4OqxF4AQMjhRq2pfyjaxv9Yivndh1zEzavP5Hukm5R0dzMRYuHSjzid1TEiOM3SjZSxJfh8Z_QmtMrd5ZQD47M_4kdVijp32WK0MS_WyBR4s4n1bdXQF6_tmTyRPqjaQBEGrfaVeL92Qx5onQPUXNz_hg_WMo-AniApKMSpcmafHoY9GNfeIVhcdB_rE5FN4zVSTZ07Xcj5PFOsCua2cTo-WovdaTczmXYYYuz4IEsG9WcRK19H9D9IfLaCDfgNAwLmtmPVUGneaZynThvs9I9AGC0nL7yqrhP_ROBn5wZIm7IFLbR7uiJufLor8RQzWaWzpXl61YUZMyyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afe37ba190.mp4?token=Ufp3hTn4OqxF4AQMjhRq2pfyjaxv9Yivndh1zEzavP5Hukm5R0dzMRYuHSjzid1TEiOM3SjZSxJfh8Z_QmtMrd5ZQD47M_4kdVijp32WK0MS_WyBR4s4n1bdXQF6_tmTyRPqjaQBEGrfaVeL92Qx5onQPUXNz_hg_WMo-AniApKMSpcmafHoY9GNfeIVhcdB_rE5FN4zVSTZ07Xcj5PFOsCua2cTo-WovdaTczmXYYYuz4IEsG9WcRK19H9D9IfLaCDfgNAwLmtmPVUGneaZynThvs9I9AGC0nL7yqrhP_ROBn5wZIm7IFLbR7uiJufLor8RQzWaWzpXl61YUZMyyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نه داداش ببین طرف خیلی باهوشه حواسش جمعه به خدا داره شطرنج ۱۶ بعدی بازی می‌کنه:
با وجود درگیری با
ونزوئلا
، کشوری که دیگر نیروی دریایی ندارد، دیگر نیروی هوایی ندارد، دیگر افراد زیادی که کشور را به سمت مکان‌های بسیار بد هدایت می‌کردند را ندارد و رهبری آن از بین رفته است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/76111" target="_blank">📅 19:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76110">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4df9e7ea0.mp4?token=ULCMxRqbBv2x8SkVg4MxLqEJjwukX0KOr5OFzRcmjScY8qfE6G1o-SkVmM3FfWjvlURldiKt0VKBG6as9dVOG7jzyZGnEmnQZENetUpUsKdPjGyWcMWzFW8lsvNl5O9f1uvwtZCvWlKXDrEwEj4SsOdE1KICanUj_BjKaLW6n7rJKiKGxUaJXpigekHAiRhWu2IbplGl72SvTVYwcb7EB0JSMJFHuF75ZKB8Ae33B9-owpeHlgJDNtJzKWbWjvQLJDmz60_7S9uIYo8YRgek7CiW6iuaiIxmgZDIVeD44XSvd3y6cD5dszQXRN-C3Qq-U9K3qn3UM0T1lMfvT4ezAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4df9e7ea0.mp4?token=ULCMxRqbBv2x8SkVg4MxLqEJjwukX0KOr5OFzRcmjScY8qfE6G1o-SkVmM3FfWjvlURldiKt0VKBG6as9dVOG7jzyZGnEmnQZENetUpUsKdPjGyWcMWzFW8lsvNl5O9f1uvwtZCvWlKXDrEwEj4SsOdE1KICanUj_BjKaLW6n7rJKiKGxUaJXpigekHAiRhWu2IbplGl72SvTVYwcb7EB0JSMJFHuF75ZKB8Ae33B9-owpeHlgJDNtJzKWbWjvQLJDmz60_7S9uIYo8YRgek7CiW6iuaiIxmgZDIVeD44XSvd3y6cD5dszQXRN-C3Qq-U9K3qn3UM0T1lMfvT4ezAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
ایران بسیار مصمم است. آنها بسیار مایل به انجام یک توافق هستند.
تا کنون به آن نرسیده‌اند. ما از این موضوع راضی نیستیم، اما یا راضی خواهیم شد، یا اینکه باید کار را تمام کنیم.
آنها در حال مذاکره با توان کم هستند. شاید مجبور شویم برگردیم و کار را تمام کنیم؛ شاید هم نه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/funhiphop/76110" target="_blank">📅 19:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76108">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⚠️
پیشنهاد استثنایی به مناسبت باز شدن اینترنت ، زیر قیمت کل ایران
🛍
🚀
100 گیگ پر سرعت +ساب
1,000,000
🚀
80 گیگ پرسرعت + ساب
800,000
🚀
50 گیگ پر سرعت + ساب
550,000
بدون محدودیت تایم و محدودیت کاربر
⏰
🔴
بدون قطعی و افت سرعت
🟡
بدون ضریب
🥇
پشتیبانی واقعی ۲۴ ساعته
💸
ضمانت عودت وجه
❗️
این قیمت تکرار نمیشه، از
دستش نده
ثبت سفارش
👇
:
🎙
@Mohammad_vpn2</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/76108" target="_blank">📅 19:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76107">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یکی از منابع فان هیپ هاپ تو نظام امریکا
‏آمریکا به هواپیماهای مستقر در اسرائیل دستور داد ظرف ۷۲ ساعت به پایگاه‌های خود در اروپا بازگردند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/76107" target="_blank">📅 19:29 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76106">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ کاملا از حیطه منطق و عقل خارج شد و به PBS گفت:
ایران در ازای خارج کردم اورانیوم غنی شده خود هم رفع تحریمی دریافت نخواهد کرد و به طور مستقیم اظهار داشت: «آنها اورانیوم غنی شده‌ی خود را کنار خواهند گذاشت اما نه، نه، اصلاً. هیچ تسهیلات تحریمی‌ای درکار نخواهد بود، نه.»
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76106" target="_blank">📅 19:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76105">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">بمببببب فارس:
ا
حتمال اعلام یک‌طرفه نهایی‌شدن توافق توسط ترامپ برای فشار به ایران
منابع آگاه می‌گویند دونالد ترامپ، رئیس‌جمهور آمریکا، احتمال دارد طی ساعات آینده به صورت یک‌طرفه اعلام کند که توافق ایران و آمریکا نهایی شده است.
این اقدام از سوی ترامپ با هدف اعمال فشار و القای توافق به افکار عمومی، پیش از رفع کامل اختلافات، ارزیابی می‌شود.
بااین حال، یک عضو تیم مذاکره‌کننده ایرانی در گفت‌وگو با فارس تأکید کرده که هنوز برخی موارد حل نشده باقی مانده و تا زمانی که همه موضوعات مدنظر ایران حل نشود، هیچ توافقی در کار نخواهد بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76105" target="_blank">📅 19:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76104">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">علیرضا جی جی مصاحبه کرده گفته پشمام ریخته که جوونا هنوز ابی و داریوش گوش میکنن چون ریتم آهنگاشون خیلی چرته
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76104" target="_blank">📅 19:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76103">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بارسا تو ۲۴ ساعت گوردونو خرید، بعد میگن پول نداره</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76103" target="_blank">📅 18:43 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
