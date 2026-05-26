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
<img src="https://cdn4.telesco.pe/file/L52z560azY1ZursWYVgExhucrSVSWcBV_kxTpCgQrmBYV3nV9Iilrvo6P6Pv53Z3PlhdUKCXTAiZCsby3GlKRrssZtTnjgUbAI9L-nQgeuMYT-LiSF_s01wOpnE-nhgKvX4S5BeRL5K0JH3Ls38_nbui-0cK6fyD1orGfWZhvp6ZIWied2HtQlPbQ9uGLsCQYly3UsMGFWmxfqQqWEcTSL5pXFuE_LOhP0kU6RxXOkGG8Vnq8ePi41ZrRmeD6P8JKC71Ymd9uuTI0Ic8Kgvx5l5GxiQzneLRyniJ4IDHqh4LIaP6peD4UDthLtt7XJYRbZFgM-9JXLc8Hp9baSGNCA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 252K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 21:10:54</div>
<hr>

<div class="tg-post" id="msg-76158">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f8e898fc0.mp4?token=mDze-yQ8v_xv8SkwoL_R4gY_uK9-AZKmJrsn1C7zThggrR4MxIrp61Zoxg7EUZCDcso61626GsVVAMaMKaY3G1A1NK1wQ17NiaS4lEY64MHBCgK8OC4ssq4jQJvkSkemwAsY1KLI1on_hSX_PkpnaZMzZYoNweEHVPDJ0Ad98rNFkfnN7M-EGnKsDml25hj6bV-t50UwCaljyMLgcGzqMKKh5nrIIonXNOqX0ejtoB-ZAfQ7Ezur3Pionb2eKvSw8rIheCvXlqrvOkcevqWhHHrn7jkv79zV4G8jKQCFpvfiBqJBFdRf8-2UbhuvvHcyF1bh9YxmwtN2zEhgnP9zXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f8e898fc0.mp4?token=mDze-yQ8v_xv8SkwoL_R4gY_uK9-AZKmJrsn1C7zThggrR4MxIrp61Zoxg7EUZCDcso61626GsVVAMaMKaY3G1A1NK1wQ17NiaS4lEY64MHBCgK8OC4ssq4jQJvkSkemwAsY1KLI1on_hSX_PkpnaZMzZYoNweEHVPDJ0Ad98rNFkfnN7M-EGnKsDml25hj6bV-t50UwCaljyMLgcGzqMKKh5nrIIonXNOqX0ejtoB-ZAfQ7Ezur3Pionb2eKvSw8rIheCvXlqrvOkcevqWhHHrn7jkv79zV4G8jKQCFpvfiBqJBFdRf8-2UbhuvvHcyF1bh9YxmwtN2zEhgnP9zXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار عجلة بين حيفا وتل أبيب ؛ مقتل شخص بداخلها كحصيلة أولية.</div>
<div class="tg-footer">👁️ 412 · <a href="https://t.me/naya_foriraq/76158" target="_blank">📅 21:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76157">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">⭐️
عقب فيضان نهر الفرات.. حكومة الجولاني تدعو لإخلاء فوري للمنازل والمحال القريبة من نهر الفرات في محافظتي دير الزور والرقة.</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/naya_foriraq/76157" target="_blank">📅 21:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76154">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uXOyy1vw6mYHgGByoJCNL0K49qnvFJsdSx20zBJVJwtN1mh3ofl2nNqmoby62PuTPOTSO5xT1p-FZtqsamFt8Kbm6u41tO--57bGZtOM4SuJEQbfkyMqX2GP7e36HknMtXOVjuaD1sjGdtdcKHrkgqSbZHvsjs_RItyyxSKLL12d1vvKOPbcEUYex2DhD5_eY5pxE4JGoi3Xu8CMkz0N00RDmbOAES2hPLMI2p-NrGIJQmRqWEwSKhQh5lVaiXwWBKoX_ddR2bJOu1VUhmWxJAFFL2YfQ1eNt0I3gqJQ7e1Tez-nc-QIEUUuhwJGBVboF-LAr8NVuAoGBGWFRuU9Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rX26-9nuMWO_XDS1TE7nnZAGSZIr5hZDsdno8iIsYCiFZ4E0PBCP-8aLuuKnbmLYO_27Kd9WazKIc2EoC9IqHy6_XGLM7SUU4NIrqnlJ9Zbt8A0WxWax_vrfsWEeu_D8lgOd9lVtPhIkUKPexkt_CLsKuDet_KR5keJHli0NWF6p4PgkxrmNfIrNd64TS427Qi49IgZpfsJEpk4oiR8oORg6hrb_Khx_yFaV29X4DmlFmqo6lkfZjhEO9V1wfhaxsBST1Scd-kCHTjn4Ku2r3efmzTGGQzDhvGMlmGJWbd1RFX-uimWEDmdNK6kZUe0W0jpZxat9_rf2Pn82OtxqpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bk2DYFKsXOgVTC0GJursHVH2y8d6OJcSJTW-rdBZQc7HrwYL2HRqGJAKRIK6QkpTXFWzI6f8pNHUfuXoMi7uRzTAalypFBTiqLexE5bO6HGCWG0rPV6fpgOy23ABVyMJUq62NSfMzjKEMxCLyeHAstP9kYfVJOFt5WavCk0DQfmpva8uKhLKfwjjSet3IIS-ECwgM8MrRMO-p-1KdtGBri9YNuwbIftME3Z2E7P4Gl0dKSkAtSzm5Ik9WeDyq3BdpPa6GEp_VpbdSrEHCQhkBkveV-gS7oYXskFvcDcdV5WtiYxxLj-zGrwyQ2Q3_aSf612c_0hB5lh-syjC4TWUqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
🇮🇶
إيران والعراق لايمكن الفراق..
برای دومین روز متوالی، خدمت رسانی و ایجاد فضایی امن برای زائران ایرانی که برای شرکت در روز عرفه به گذرگاه مرزی مهران مراجعه ميكنن ، توسط فرماندهی عملیات نیروهای حشد الشعبی در استان واسط، ادامه دارد. این کار به دستور مستقیم فرمانده عملیات واسط، آقای احمد خضیر المکصوصی، انجام شده و شامل تهیه غذا، تسهیل مراحل ورود زائران و ارائه پشتیبانی لازم برای انجام زیارت میباشد.</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/naya_foriraq/76154" target="_blank">📅 20:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76153">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇷
الرئيس الإيراني مسعود بزشكيان:
لقد مدت إيران الإسلامية يد الأخوة إلى الدول الإسلامية، وفي الوقت نفسه لا تتردد في حماية أراضيها وسيادتها الوطنية.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/naya_foriraq/76153" target="_blank">📅 20:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76152">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">⭐️
‏
القناة 14 العبرية:
تقديرات في إسرائيل بأن الاتفاق مع إيران سيشمل بشكل شبه مؤكد لبنان.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/naya_foriraq/76152" target="_blank">📅 20:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76151">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWH-FJxI1yw8lVIYCWP4SecUXmymhDPH8ZGrgcmphZwGzWjQjaobHsT4kCOqpiS4px5R-c3qU8g-_1TEq1oKu6wdqfuIAl8RhlYD6UYmUlwONJtoGCSRkRha25C_D7LFl1g-2WUZsnbqwFpybsWZn4zL7SiW3jPJ7sx-dH5XSDs8zJKvwXg5SCBq1WF_p38W00x1uee1BhakLRfe8dSz030CJP27HcpyE0f91z87KOBaGZs1STBfbhV-1-_8WxEyIn8fPxpaosXLyEfVvA1aQEjD33G_CnY5JVYMlQjx2Ij5wqzXaf8yBBLpNF3ZUEFVx8NPIdNiV8LWHAkOqNgX5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
ديدار مشاور امنیت ملی عراق "قاسم الاعرجی" در مسکو با معاون دبیرکل شورای امنیت ملی ایران "علی باقری".
در این دیدار، آخرین تحولات اوضاع منطقه و راه‌های حمایت از گفت‌وگو از طریق کانال‌های دیپلماتیک برای پایان دادن به درگیری‌ها در منطقه بررسی شد، همچنین تقویت روابط تاریخی عمیق بین دو کشور و دو ملت دوست مورد بحث قرار گرفت.
آقای الاعرجی بار دیگر تأکید کرد که قانون اساسی عراق اجازه استفاده از خاک عراق به عنوان نقطه شروع برای حمله به کشورهای همسایه را نمی‌دهد و به نیاز به تشکیل شورای هماهنگی امنیتی بین همه کشورهای منطقه اشاره کرد.</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/naya_foriraq/76151" target="_blank">📅 20:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76150">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a65cbfac7.mp4?token=OPaepMYXAnNu2EZln5XZXIA2LEB5yh1VIAo-WyfDRXCUsAohWDiGdrpEtckJfrkBfN1-o3BEi-Fz6egsOiMDntM6PqfjfSsvXQmH-X4-TW4nDZrfRHORe2BDqmiNVSxVdZFD67gkzA-ukwGGkRqMLgpJpaAwNsVuETTnEuzUr9XLv0Az-h22poxIh9zztb4fxqyYn1NdTM-Jd03SHot_RwNnrGpHHq2bvi0HXEtjWf79pisZoq4jCAqXdBTUhD-yZaeVCoS9yT1HVDmNxZVW862KY_SvZMc9kg0YTGuud18lR14DIa9S5r6nIDE1Z_rXXAFqEB_jJB5GY6V2WHm9lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a65cbfac7.mp4?token=OPaepMYXAnNu2EZln5XZXIA2LEB5yh1VIAo-WyfDRXCUsAohWDiGdrpEtckJfrkBfN1-o3BEi-Fz6egsOiMDntM6PqfjfSsvXQmH-X4-TW4nDZrfRHORe2BDqmiNVSxVdZFD67gkzA-ukwGGkRqMLgpJpaAwNsVuETTnEuzUr9XLv0Az-h22poxIh9zztb4fxqyYn1NdTM-Jd03SHot_RwNnrGpHHq2bvi0HXEtjWf79pisZoq4jCAqXdBTUhD-yZaeVCoS9yT1HVDmNxZVW862KY_SvZMc9kg0YTGuud18lR14DIa9S5r6nIDE1Z_rXXAFqEB_jJB5GY6V2WHm9lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
نتنياهو:
قررنا تعميق العمليات العسكرية في لبنان.</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/naya_foriraq/76150" target="_blank">📅 20:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76149">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jo2CprXpro6MT6z07mj_G7pmEYVjiS8B9_VQD2fH5P07rVZNAAa_EcZfIOUYt3vnVsw_oULLXkAhGs7Pgz59t7F3_ciIydcv87wcsTnUHVR3ce5iHokS2miPXxvi8sxsezWh82-8IDkEnEWOkURB33OB2uPZ7rZUyhWRG0JdNJrs89nsXaiSz3mYj-74tn_GTm0JY5CEYW_BcXtW-ULKhM5unpDaIKK7Glqs6ywOzJh35YHMcN-CCg4ROsYoAMzkG2jiKguZL3uey6JIJbfQbtPfQjprgDT30_eNaelCsZAnr9k7YtTnPear2YqND8pnFSlX5OfEZmWafEFN80iXyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
انتهيت للتو من الفحص الطبي الدوري الذي أجري كل ستة أشهر في المركز الطبي العسكري والتر ريد.كل شيء كان على ما يرام. شكرًا للأطباء والموظفين الرائعين! عائد إلى البيت الأبيض.</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/naya_foriraq/76149" target="_blank">📅 20:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76146">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca0b9345b0.mp4?token=d_Wld_ZaDpdWdaWgK6tE4nZePdB9w-wSUVWDpeJOP8_ikbK2-9zSwxPD_9FhA_nCrk7-vGbhwi0wNPcPKpONLhun9le0c-DMDl_k3r-sKWffDIszw25gGuhya0PlpDc4__q28uS0PFw-HsQGSmNLi56HMsbFU2a4gV6D2Rj_jW2VWKCWtfiSJUFb7aHt0k-kudJTJ-VKEkTftXiK-JUXNZUVonFnTb4h-VhexYkq22xjagzk-UGDbIgRw-brH3fy1iUb7-xhzujN2nLJNlpydG27I0dH8ErnHOX-lRY-tklVDKmKlZ6BFAir-QbpoX9z0ie1vq3nsW-ASkHQKw9HcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca0b9345b0.mp4?token=d_Wld_ZaDpdWdaWgK6tE4nZePdB9w-wSUVWDpeJOP8_ikbK2-9zSwxPD_9FhA_nCrk7-vGbhwi0wNPcPKpONLhun9le0c-DMDl_k3r-sKWffDIszw25gGuhya0PlpDc4__q28uS0PFw-HsQGSmNLi56HMsbFU2a4gV6D2Rj_jW2VWKCWtfiSJUFb7aHt0k-kudJTJ-VKEkTftXiK-JUXNZUVonFnTb4h-VhexYkq22xjagzk-UGDbIgRw-brH3fy1iUb7-xhzujN2nLJNlpydG27I0dH8ErnHOX-lRY-tklVDKmKlZ6BFAir-QbpoX9z0ie1vq3nsW-ASkHQKw9HcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إشتباكات عنيفة بين مشجعي فريقي كرة القدم هبوعيل بئر السبع ومكابي تل أبيب في القدس المحتلة.</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/naya_foriraq/76146" target="_blank">📅 20:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76145">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🌟
🏴‍☠️
أبناء نصرالله يستهدفون دبابتي ميركافا تابعة لجيش الإحتلال الصهيوني في بلدة رشاف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/naya_foriraq/76145" target="_blank">📅 19:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76144">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🌟
🏴‍☠️
أبناء نصرالله يستهدفون دبابتي ميركافا تابعة لجيش الإحتلال الصهيوني في بلدة رشاف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/naya_foriraq/76144" target="_blank">📅 19:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76143">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇷
نائب الرئيس الايراني:‏أُعيد فتح الإنترنت وتوفير خدمات ذكية استجابةً لمطالب الشعب، مع التوجه لإزالة العقبات أمام التنمية والريادة العلمية.</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/naya_foriraq/76143" target="_blank">📅 18:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76142">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">📰
وول ستريت جورنال: البحرية الأمريكية تستأنف توجيه السفن عبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/naya_foriraq/76142" target="_blank">📅 18:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76141">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6nEfyCxmpK2coDCxaj8BMmhQbCVxmpKsUXjTA6GOEeYVEq6lAy4MOR8fLgvkGYy3Y0Se941bcS_aE8FC5evM40ruoqqJA5VNzjhJWFAB0fm1s044SDgdBaQWL1uQA8p7TB_IwPtBa2iT8sOXhVSYBosvUVrtCUrYO8v_iYRprbKZGjr_FZfIyWnbL_svhVDFta1SC8RkbGUJC3nhHcelLhTI09uhZY-Ux1vMGNm_xYTxRjgZvKFLxliPnsnLLfATe_u-MVJ1J-pKUpcIjtA1YSirgReNeD3jyPZabYeIbTBd4402h07X5OMXg21WJQhT8oD9vJeqfjadnRG0lmrrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
ديمتري ميدفيديف:
قال الاتحاد الأوروبي إنه سيحافظ على وجوده الدبلوماسي في كييف دون تغيير، على الرغم من تحذيرات روسيا. حسنًا، يبدو أن لديهم دبلوماسيين فائضين ويحتاجون إلى تقليص عددهم.</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/naya_foriraq/76141" target="_blank">📅 18:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76140">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🌟
‏ترامب يرفع سقف استقبال اللاجئين بمقدار 10 آلاف لاجئ لاستقبال المزيد من البيض من جنوب أفريقيا.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/76140" target="_blank">📅 18:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76139">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e929c95856.mp4?token=bNxOCLneAaG1MLVDriFyW_UdCQE_ULZUc8OO6op9hTeMdiWa93ea3nko0uHteeXWA1Jh3IqV8b2BqOwv1qLOVQCzfmwanmKY9-32G1DJls1isELKUhTrpMsaVQgyYojV9-oTyI6Rl8z0l48CrEl8wasXpiJsfjm2MAVelwonioEFyZGoN6ctmZRlGdEb0rqQKtoZMOx5jpQWLdsZ6bW-w1KUnUjtlgv-149UhBypCDh6D2L6cUCdktR8eifVkZ60cRE022rfy4r3nz9AfcPF54A9DVmVhaOpPNgfXL4dx0mbRSqTHHupnpxDoNZ9CZPfkZhbnkSOsDtUaN14Y2gXKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e929c95856.mp4?token=bNxOCLneAaG1MLVDriFyW_UdCQE_ULZUc8OO6op9hTeMdiWa93ea3nko0uHteeXWA1Jh3IqV8b2BqOwv1qLOVQCzfmwanmKY9-32G1DJls1isELKUhTrpMsaVQgyYojV9-oTyI6Rl8z0l48CrEl8wasXpiJsfjm2MAVelwonioEFyZGoN6ctmZRlGdEb0rqQKtoZMOx5jpQWLdsZ6bW-w1KUnUjtlgv-149UhBypCDh6D2L6cUCdktR8eifVkZ60cRE022rfy4r3nz9AfcPF54A9DVmVhaOpPNgfXL4dx0mbRSqTHHupnpxDoNZ9CZPfkZhbnkSOsDtUaN14Y2gXKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🌟
الاحتلال الصهيوني يستهدف عدة منازل مدنية في محافظة النبطية جنوبي لبنان.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/76139" target="_blank">📅 18:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76137">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbfd9de336.mp4?token=lo9ZwmDq3-OOYqbJi0xL_RVdpzDOsmvSCNenfhtw8o3AtlWWEsM3Syzw-J9H5eW-ehJ-CJpP0N8eehM6vPehk3YDeXKaqqp10cj1YU1ebwe7GeoyRQRMjAEI7_kqxnXyEQTesb4yNEKf0Lmof8zm-ddOdLXnXOvgl41PKSL1bniEAN3dC9X2CX7eW8nMj0MU5hjB2zV7iB2KqVxqWMcKwU_cH8H8-fySWbve-okDDUXxsako6MFhW4Qquo9rhRJ0WHdkZrOnR3EXvCYHh3SqpqKiG-KczHiqVGJdxN-Vxh2xS8LuTfvyuAhgL2t_NOL-OZkBzgEmPQOABqc9FwIjag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbfd9de336.mp4?token=lo9ZwmDq3-OOYqbJi0xL_RVdpzDOsmvSCNenfhtw8o3AtlWWEsM3Syzw-J9H5eW-ehJ-CJpP0N8eehM6vPehk3YDeXKaqqp10cj1YU1ebwe7GeoyRQRMjAEI7_kqxnXyEQTesb4yNEKf0Lmof8zm-ddOdLXnXOvgl41PKSL1bniEAN3dC9X2CX7eW8nMj0MU5hjB2zV7iB2KqVxqWMcKwU_cH8H8-fySWbve-okDDUXxsako6MFhW4Qquo9rhRJ0WHdkZrOnR3EXvCYHh3SqpqKiG-KczHiqVGJdxN-Vxh2xS8LuTfvyuAhgL2t_NOL-OZkBzgEmPQOABqc9FwIjag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
أ ف ب:
رئيس الوزراء الفرنسي يعتزم اللجوء إلى القضاء ضد معاملة إسرائيل "المروعة" لناشطين في أسطول غزة.</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/naya_foriraq/76137" target="_blank">📅 18:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76136">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">📰
وول ستريت جورنال:
البحرية الأمريكية تستأنف توجيه السفن عبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/naya_foriraq/76136" target="_blank">📅 18:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76135">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26b6835677.mp4?token=QTQ8fJibbr8CRtu4KRAiQO8E6zJbeEigEwqStU1tp31jGpw1vTr_DClSkmfYnsnFqQlFMHIbLZe2Hu5ZkuhNT-YN6Rg-qGln2MJI3LhnD7KIXK_38hcVO-Wa1dGmbQ2JvV7APxKWWhODm-Lp7yGdZH56enThl7MbCqePNvGBH1hMtD8dgR37V-IvTPUuFxO_cshmHahnFV_Nk-imLhMl3aFj4xi7tYY565M0oEF8L25WIFz7oTFeTPecXDpLftaU6rBpm2PXD72brIJKOl0zluzoy0tGrEMD0zDjcENHLxetUiGhc1RldHBxwFLMpmQK-MbsU-KMH9-k_wWQpPAeeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26b6835677.mp4?token=QTQ8fJibbr8CRtu4KRAiQO8E6zJbeEigEwqStU1tp31jGpw1vTr_DClSkmfYnsnFqQlFMHIbLZe2Hu5ZkuhNT-YN6Rg-qGln2MJI3LhnD7KIXK_38hcVO-Wa1dGmbQ2JvV7APxKWWhODm-Lp7yGdZH56enThl7MbCqePNvGBH1hMtD8dgR37V-IvTPUuFxO_cshmHahnFV_Nk-imLhMl3aFj4xi7tYY565M0oEF8L25WIFz7oTFeTPecXDpLftaU6rBpm2PXD72brIJKOl0zluzoy0tGrEMD0zDjcENHLxetUiGhc1RldHBxwFLMpmQK-MbsU-KMH9-k_wWQpPAeeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
الصحيفة الالمانية شبيغل: تخطط الولايات المتحدة لتقليص كبير للقوات العسكرية والمعدات التي تلتزم بها تجاه حلف شمال الأطلسي في أوروبا، مما يزيد الضغط على الحلفاء الأوروبيين لملء الفجوات بأنفسهم.  تشمل التخفيضات المقترحة طائرات مقاتلة، وقاذفات استراتيجية، وسفن…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/76135" target="_blank">📅 17:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76134">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🌟
حزب الله ينشر:
أحرارٌ أعزّاءُ لا عبيدٌ أشقياءُ.</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/naya_foriraq/76134" target="_blank">📅 17:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76133">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🌟
رويترز
: العقود الآجلة لخام برنت ترتفع 4 دولارات للبرميل، بعد عدة ضربات وجّهها الحرس الثوري على حاملات النفط بسبب مخالفتها قوانين مرور مضيق هرمز.</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/naya_foriraq/76133" target="_blank">📅 17:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76132">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🌟
‏ رويترز: عراقجي وقاليباف في قطر.</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/naya_foriraq/76132" target="_blank">📅 17:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76131">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🌟
🌟
يديعوت أحرونوت:
حزب الله لديه مسيرات قادرة على الوصول حتى مسافة ٣٠ كلم.</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/naya_foriraq/76131" target="_blank">📅 17:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76130">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇩🇪
الصحيفة الالمانية شبيغل:
تخطط الولايات المتحدة لتقليص كبير للقوات العسكرية والمعدات التي تلتزم بها تجاه حلف شمال الأطلسي في أوروبا، مما يزيد الضغط على الحلفاء الأوروبيين لملء الفجوات بأنفسهم.
تشمل التخفيضات المقترحة طائرات مقاتلة، وقاذفات استراتيجية، وسفن حربية، وغواصات، وطائرات بدون طيار، وطائرات التزود بالوقود جواً.
لا تزال واشنطن تعتزم الحفاظ على الردع النووي في أوروبا، لكنها تريد من الأوروبيين تولي معظم مسؤوليات الدفاع التقليدية.</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/naya_foriraq/76130" target="_blank">📅 17:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76129">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16fda706f6.mp4?token=YLc5k5IxIpxRmxk3rfCi_qnJamc9JogsFh2oslAr80Ugfz26lULxG2Zhe0PHpcfNKR8BP2AtFvPCbB4g3FzBvqpKzTsu9gVbXGmvNp6PmtLx0T0kT8XfESDPWGjEAns_fVJqmmiZzHBYiM1DoDX46SEwx0_g9jtlufYfKDNaX4JgYHoKt9Kmg1EHROmirgTroBU3AKLMxiQ-23MgZVRxQ2xuBWDA2UntJKlBGO-87CYVBhDE7-FzDpw54Z7aQ185VYCrQ2f1Gh_TqLMDr-0nDeGUjCHeWG__alD0izKuisTtn7IOelcZTP_n70HufoI0fFLt1rKmKdWTbCaows_sXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16fda706f6.mp4?token=YLc5k5IxIpxRmxk3rfCi_qnJamc9JogsFh2oslAr80Ugfz26lULxG2Zhe0PHpcfNKR8BP2AtFvPCbB4g3FzBvqpKzTsu9gVbXGmvNp6PmtLx0T0kT8XfESDPWGjEAns_fVJqmmiZzHBYiM1DoDX46SEwx0_g9jtlufYfKDNaX4JgYHoKt9Kmg1EHROmirgTroBU3AKLMxiQ-23MgZVRxQ2xuBWDA2UntJKlBGO-87CYVBhDE7-FzDpw54Z7aQ185VYCrQ2f1Gh_TqLMDr-0nDeGUjCHeWG__alD0izKuisTtn7IOelcZTP_n70HufoI0fFLt1rKmKdWTbCaows_sXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🌟
الاحتلال الصهيوني يستهدف عدة منازل مدنية في محافظة النبطية جنوبي لبنان.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/76129" target="_blank">📅 17:11 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76128">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34378ee6f.mp4?token=ba1Elp9bfyYYOYbd6K9UOavI5PTnsU2rZn37mSYuSO9a1L3RIpMe84g-uy0wfnhF6bgJeQILYmD4J0_scXYA_MXDEDKo6f2HQUF-XcbLaG4zxjJBakGtFhDOqD5hI6D-9SfC27rEAWK0a02wFvP9We8w32O20nWPj_v8wE3t5S15HBWfFZOjDQ6ybFjmcqVRV90Ybru8otBJezupUKXBP2maFE6yTCzwo6SqXJoWfxXA_ug3sa5WHxAtum48dTV0AXkFYKcIUEpZGDxZqXqqcDp6_gqSvBiKr-EBjeEPhiN-Efc_nMlcuKSTmEmaBa_Qutw3U689OEHNvcaibhD__g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34378ee6f.mp4?token=ba1Elp9bfyYYOYbd6K9UOavI5PTnsU2rZn37mSYuSO9a1L3RIpMe84g-uy0wfnhF6bgJeQILYmD4J0_scXYA_MXDEDKo6f2HQUF-XcbLaG4zxjJBakGtFhDOqD5hI6D-9SfC27rEAWK0a02wFvP9We8w32O20nWPj_v8wE3t5S15HBWfFZOjDQ6ybFjmcqVRV90Ybru8otBJezupUKXBP2maFE6yTCzwo6SqXJoWfxXA_ug3sa5WHxAtum48dTV0AXkFYKcIUEpZGDxZqXqqcDp6_gqSvBiKr-EBjeEPhiN-Efc_nMlcuKSTmEmaBa_Qutw3U689OEHNvcaibhD__g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
السيناتور ديف ماكورميك:
"سيتعين علينا استخدام الجيش لفتح المضيق وطمأنة السفن التجارية. لدينا القدرة على القيام بذلك. لن يكون الأمر سهلاً، لكن هذا هو الطريق الأصعب في نهاية المطاف."
خذها ان استطعت
😎
...</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/76128" target="_blank">📅 17:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76127">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPYtE7XE5pNRC_yjA4hMR4kv1VpP9W_DKrIfYUJd7AUwDtxa2SC19OvDuBMRs5YFleBQdnomGWSYUzLMbuHMCkeDm_chx5GxbHnctjZVwi4qyWEPC32A5vcoNg9mk-DuqB_Y5OZgda_T7lZZIkchkuPWOxi719pWKcp4BxdQ82N0HWvjl_jUbHg1O4Xz9KCu4BXuV28v7vHgVGrveSYl1l1KUFw_anCR5I-eVLiNXk3NYai9ZlkI7gezJCxfN06XuRcPdt_mJoX8-aT4VNqc8PjUd57pf7mV_rKgFTyia5Is43aiVaq3yOKbPB2TXhI4MlSaMVVlU4Z-IGjVASoCdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
نائب الرئيس الايراني:
‏أُعيد فتح الإنترنت وتوفير خدمات ذكية استجابةً لمطالب الشعب، مع التوجه لإزالة العقبات أمام التنمية والريادة العلمية.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/76127" target="_blank">📅 16:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76126">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">انفجار يهز سواحل عمان</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/76126" target="_blank">📅 15:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76125">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">انفجار يهز سواحل عمان</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/76125" target="_blank">📅 15:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76124">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d125f4a00.mp4?token=tUwVvDTnheWuwvLdvFgat8yNlov9fs361T7U3yufqKT0xi5Zna5I1dOalhrYpYWULvVR-p93ZNfDT7f4nwFQ743jUMltNrVohmnn0ai-xmlSBeR0vpuvgGXB-bI7bE3pYvFIEaxGTtmLR9j0wD01iku1IsxocGH8d5-eq-2Ks-1JeqFdIpNJW6xg36Vv8lE8g0_-wlIHDOQdmHtatgkSCjB1r8K7KJSCJdCDrQpXSDtFocv4Sxh4aGS0qusk_8I2oe5Q3gigs7Z5mhD9sIswoCUix4ufsqJQuxwRGs-JeWOSyV9drVySueQZZY9Ef6sG7ZIA_xT8vI4KHI9Gla0jsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d125f4a00.mp4?token=tUwVvDTnheWuwvLdvFgat8yNlov9fs361T7U3yufqKT0xi5Zna5I1dOalhrYpYWULvVR-p93ZNfDT7f4nwFQ743jUMltNrVohmnn0ai-xmlSBeR0vpuvgGXB-bI7bE3pYvFIEaxGTtmLR9j0wD01iku1IsxocGH8d5-eq-2Ks-1JeqFdIpNJW6xg36Vv8lE8g0_-wlIHDOQdmHtatgkSCjB1r8K7KJSCJdCDrQpXSDtFocv4Sxh4aGS0qusk_8I2oe5Q3gigs7Z5mhD9sIswoCUix4ufsqJQuxwRGs-JeWOSyV9drVySueQZZY9Ef6sG7ZIA_xT8vI4KHI9Gla0jsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 22-05-2026
دبابة ميركافا تابعة لجيش العدو الإسرائيلي في بلدة مركبا جنوبيّ لبنان بمحلّقة
أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/76124" target="_blank">📅 15:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76123">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJThUTBvEjHI6N2pZtVH1xyB2FuqFXzrtynjfwJQLTiiyiev1OwiqlO02XEV8YR0RjuotoEmSXVA5i6q4_ZMrHaCJKMun48eC2gYLs5PkTftLf2XuuiSioDbcSNnCnbn2P6-q3T5P0yMpIs8J6rltaAZtyiQ2u9prnMMVQhQZDfcQKsJvPeo9EHtQFop3DNAZBLKUHv8m2-wYKduKvUdztM3-TG7j9wuni8P3V0-t6aatHKPtdpVz0jZOeuRKexwugkyiHiJloqPEdghVlmrssIe5TTUSUuHauS8khSWdHkzHHve-59vGA3Dj1FVUsv9nN-w0ujsdf1P_Xb0VkLTIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
‏
الخارجية الإيرانية:
طهران سترد على الخرق الأميركي لوقف النار.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/76123" target="_blank">📅 15:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76122">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇷🇺
مجلس ‏الدوما الروسي:
الهجمات على المدنيين قد تدفع موسكو لاستخدام أسلحة لا تترك أثرا لأي شخص.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76122" target="_blank">📅 14:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76121">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-text">#عاجـــــــــــــــل
⭐️
وفاة أول حاجة عراقية من أهالي محافظة واسط في الديار المقدسة اثناء تأدية مناسك الحج.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/76121" target="_blank">📅 13:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76120">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇶
اندلاع أعمال شغب عنيفة داخل دار تأهيل النساء في منطقة الاعظمية وسط العاصمة بغداد وأنباء عن سقوط عدد من الإصابات</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/76120" target="_blank">📅 12:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76119">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏وكالة أ ب: وساطة قطرية نجحت في تحقيق تفاهم أميركي إيراني بشأن "الأموال المجمدة"  ‏من المرجح أن تعلن الولايات المتحدة وإيران اليوم اتفاقا بشأن "الأموال المجمدة"</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/76119" target="_blank">📅 12:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76118">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال: استهداف قاعدة عسكرية في الجليل الغربي بمسيرات حزب الله</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/76118" target="_blank">📅 12:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76117">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‏وكالة أ ب: وساطة قطرية نجحت في تحقيق تفاهم أميركي إيراني بشأن "الأموال المجمدة"
‏من المرجح أن تعلن الولايات المتحدة وإيران اليوم اتفاقا بشأن "الأموال المجمدة"</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/76117" target="_blank">📅 12:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76116">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">إعلام غربي : يدرس المدعون الإسرائيليون توجيه اتهامات جنائية ضد رئيس ديوان نتنياهو، تساحي برافرمان، بتهم الاحتيال وخيانة الأمانة وعرقلة سير العدالة المرتبطة بالتسريب المزعوم لوثيقة استخباراتية سرية للغاية إلى صحيفة بيلد الألمانية.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/76116" target="_blank">📅 12:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76115">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🌟
حزب الله: سرديّة استهداف قائد لواء المدرّعات 401 في جيش العدو الإسرائيلي العقيد مئير بيدرمان في أطراف بلدة دبل جنوبيّ لبنان بتاريخ 20-05-2026
بعد سلسلة محاولات تقدّم إلى بلدة حدّاثا ومن عدّة محاور، لم ينجح العدوّ في اختراق دفاعات المقاومة عند أطراف البلدة التي تكبّد فيها العديد من الخسائر من جنوده وآليّاته.
خلال مساء يوم 19/05/2026، هاجم العدوّ حدّاثا بشكل عنيف ومن محوري تقدّم بجمع كبير من الآليّات و34 جنديًّا (قوّة من الكتيبة الهندسيّة القتاليّة 601). دارت اشتباكات واسعة عند أطراف البلدة. وعند الفجر انكفأت القوّة المتقدّمة تاركةً خلفها جرّافتين مدمّرتين و4 دبّابات احترقت نتيجة استهدافها بالمحلّقات والقذائف المباشرة. أمّا الجنود فقد شُوهِد خروج 28 جنديًّا و6 الباقون تمّ نقلهم بواسطة آليّة نميرا بعد إصابتهم منهم قائد السرية النقيب م. ومقاتلة التوثيق العملياتي الرقيب الأول ش.، اللذين أصيبا بجروح متوسطة وخطيرة.
كان هذا التقدّم بإشراف قائد اللواء (401) مباشرةً الذي كان يتابع تقدّم القوّات وكذلك انكفاؤها من التموضع المتقدّم للواء في بلدة رشاف.
عند الساعة 05:00 فجرًا، عاد اللواء مئير بيدرمان إلى المقرّ المستحدث لعمليّات اللواء عند أطراف بلدة دبل بعد انكفاء القوّة كليًّا. هذا كلّه كان تحت عين ورصد المقاومة.
عند الساعة 07:50 صباحًا، وصلت أوّل محلّقات أبابيل الإنقضاضيّة إلى المقرّ وقامت بجولة مسح ميداني للمقرّ ودارت حوله، وعندما رصدت تموضع لضباط العدّو خلف تمويه في الطابق الأخير، وبعد فرارهم إلى الداخل لحقتهم المحلّقة التي استطاعت الدخول خلفهم إلى المقرّ وأصابتهم وأصابت غرفة العمليّات مباشرة. ونتيجة الاستهداف هذا أُصيب قائد اللواء مئير بيدرمان في رأسه وضابطان آخران.
عند الساعة 08:10، قام فريق إسعافي بإخلاء الإصابات عبر آليّة هامر إلى مهبط المروحيات. وصلت الهامر إلى المهبط عند الساعة 08:23، حيث اقلّت المروحيّة اثنين من المصابين، بينما نُقل المصاب الثالث بسيارة إسعاف.
عند الساعة 08:45، عاد الفريق إلى المقرّ عند أطراف بلدة دبل، حيث كانت تنتظره محلّقة أخرى قامت باستهداف المقرّ من جديد. وأصابت أخرى شاحنة ذخيرة، ما أدّى إلى انفجارات واندلاع حريق قرب المقرّ.
عند الساعة 09:00، وبينما كانت القوّة تستعدّ لمغادرة المبنى، استهدفت محلّقة أبابيل أخرى آليّة نميرا عند مدخل المقرّ.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/76115" target="_blank">📅 12:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76114">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🌟
حزب الله: مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 20-05-2026 المقر المُستحدَث لقيادة لواء المدرّعات 401 التابع لجيش العدو الإسرائيلي في بلدة دبل جنوبيّ لبنان بسربٍ من محلّقات أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76114" target="_blank">📅 12:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76113">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1060dd6c41.mp4?token=YVx5Jp2FYp_NY5WGLD5jpJx3dAP9D1hSaibLHYl0rqPmq6yT6R_IE9KGRu-TSjj_GnvuLC1k9tdoKTpWZ4C8rpG5MO0BcDAlr00mrTimiqCHRz9usuavw0GSrurz4gnvB51zz7OSmyRy0NI4ZQUH3MaTs1uM_CPwRfAlAPpzBca16GS0ri29qHUcvZ93pPEEO5Af28tP4uj1uYqJlkgh0zvhMJD1_p6053vWPa4QTzlZek5KWuwYYA6oufZaxjVeb35rZ11-eKukZvAvd5i0HGbink_VtkQtjnuVM0M1-Rz055oNrX4QUXdctCAeG8jnZQu2MQ-vs36yA0sC6gQ2OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1060dd6c41.mp4?token=YVx5Jp2FYp_NY5WGLD5jpJx3dAP9D1hSaibLHYl0rqPmq6yT6R_IE9KGRu-TSjj_GnvuLC1k9tdoKTpWZ4C8rpG5MO0BcDAlr00mrTimiqCHRz9usuavw0GSrurz4gnvB51zz7OSmyRy0NI4ZQUH3MaTs1uM_CPwRfAlAPpzBca16GS0ri29qHUcvZ93pPEEO5Af28tP4uj1uYqJlkgh0zvhMJD1_p6053vWPa4QTzlZek5KWuwYYA6oufZaxjVeb35rZ11-eKukZvAvd5i0HGbink_VtkQtjnuVM0M1-Rz055oNrX4QUXdctCAeG8jnZQu2MQ-vs36yA0sC6gQ2OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
مشهد بات مألوفاً في سوريا تحت حكم الجولاني.. حيث أصبح من هواية الأجانب الإرهابيين التجول في الأحياء المسيحية وتحديداً حي باب توما الدمشقي وترديد التكبيرات لإثارة النعرات الدينية.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76113" target="_blank">📅 11:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76112">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: وجّه مجتبى خامنئي، المرشد الأعلى لإيران، رسالة تهديد إلى الولايات المتحدة : "لن تكون أمريكا آمنة في منطقتنا".</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/76112" target="_blank">📅 11:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76111">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇷
التلفزيون الايراني: ما تم تداوله في الإعلام حول البنود الـ14 لمذكرة التفاهم بين إيران والولايات المتحدة لا أساس له من الصحة</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76111" target="_blank">📅 11:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76109">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">إعلام العدو : بدأت إسرائيل تعبئة احتياطية طارئة، بما في ذلك قوات المدفعية التي تم تسريحها مؤخراً من الخدمة، مع تزايد الاستعدادات لعمليات دفاعية موسعة في لبنان وسط استمرار هجمات حزب الله وانتهاكات وقف إطلاق النار</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/76109" target="_blank">📅 10:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76108">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پیام_رهبر_انقلاب_اسلامی_به_مناسبت_برگزاری_حج.pdf</div>
  <div class="tg-doc-extra">415.4 KB</div>
</div>
<a href="https://t.me/naya_foriraq/76108" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">النص الكامل لرسالة قائد الثورة الإسلامية بمناسبة موسم الحج | 5 خرداد 1405</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/76108" target="_blank">📅 10:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76107">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">الجيش الإسرائيلي: لم نشارك في الضربات ضد إيران إلى جانب الولايات المتحدة.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/76107" target="_blank">📅 10:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76106">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">⭐️
هجوم بالطيران المسير الانتحاري وعدة صواريخ يستهدف مقر تابع للمعارضة الكردية الإيرانية في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/76106" target="_blank">📅 10:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76105">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">📰
‏القناة 12 الصهيونية عن مصادر:  مجتبى خامنئي لم يصادق بعد على التفاهمات المتبلورة</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/76105" target="_blank">📅 10:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76104">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AO5k7mXLMtKNjp4q_61SAnyhILI-RZaitHfKjrb89nv2eXkO2MkMmy_AXHe6_BOu4Rsu8A2Xbxc4DzmI7NC25VEdK6DGvVHz12dshL18r1AIBfGDOVVxbSijAE5d6BImx7DulkWdXuzBD_2CRsDOww6hQlMKAnpyWr9FIpP0Oqxz4IpxuoeBKWqS8b2FDvebvSVncP6FIJWPdfUTN4xFDoPJMgFyfdO-4uR1-_Eoky6nKtHlzsXtd93ItNPBHOP82KUHkeRvtcvp3LD0PN0sdb3W0YdnGU9N8ySMkK2oY9RaVqutYwKK5XBBQOg5YdNzefaSYaWQBwftT4vML2yacw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو: حدث أمني في الشارع الرئيسي بمدينة العفولة نتيجة انفجار سيارة ووجود جريح في موقع الحادث.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/76104" target="_blank">📅 09:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76103">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🏴‍☠️
انفجارات داخل مستوطنة بيرنيت شمال الكيان نتيجة هجوم بمسيرات حزب الله.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/76103" target="_blank">📅 09:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76102">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي: إيران حاولت مهاجمة القوات الأمريكية على مدى الساعات الـ٢٤ الماضية.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/76102" target="_blank">📅 02:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76101">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي:
إيران حاولت مهاجمة القوات الأمريكية على مدى الساعات الـ٢٤ الماضية.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/76101" target="_blank">📅 02:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76100">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇺🇸
القيادة المركزية الأمريكية: ‏القوات الأمريكية تصيب أهدافاً تشمل إطلاق صواريخ و‏مواقع وسفن إيرانية تحاول زرع ألغام.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/76100" target="_blank">📅 02:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76099">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇺🇸
القيادة المركزية الأمريكية: نفذت القوات الأمريكية ضربات دفاعية في جنوب إيران يوم الاثنين.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/76099" target="_blank">📅 02:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76098">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">⭐️
الإعلام الإيراني: دوي انفجارات في بندرعباس.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/76098" target="_blank">📅 02:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76097">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مصدر إيراني:
ماتم تدوله حول تفعيل الدفاعات الجوية في مدينة قم المقدسة لا صحة له.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/76097" target="_blank">📅 01:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76096">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نقل النتن ياهو لمستشفى في القدس</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/76096" target="_blank">📅 01:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76095">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تفعيل الدفاعات الجوية في بندرعباس.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/76095" target="_blank">📅 01:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76094">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03326bd1d2.mp4?token=Jki8pj0MBzgGhFgGvAqkbGfBn23ABRazQlHgrCIzbKbALaJgjYcuwdTyKhA5R9-6D-bYrv4e3RmtKsvrf5HLkqvt5rGEYT9g826Ey0woTi7d5IHW5gQ_DiSENUptpzHBCBTHof24F8xMUZSdnXhVrdDcf11FoZIy6l6TsYqiK9iXGSAwvawZJgTIAUIWLAJ7WHBtiv5ZejlHTpfKlzZO5qU3aLVcNjXzZMk-obuwpx22mJwf-EqMPmjYqGjQFV_7rVVSsiMQOPQzOMKYbbYuezihJRoIvYIa1Nk-eb-OJDdBKf0AmqUG4VAmKuay02FF4gaCJjQQ4LYi2mbsQAMKWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03326bd1d2.mp4?token=Jki8pj0MBzgGhFgGvAqkbGfBn23ABRazQlHgrCIzbKbALaJgjYcuwdTyKhA5R9-6D-bYrv4e3RmtKsvrf5HLkqvt5rGEYT9g826Ey0woTi7d5IHW5gQ_DiSENUptpzHBCBTHof24F8xMUZSdnXhVrdDcf11FoZIy6l6TsYqiK9iXGSAwvawZJgTIAUIWLAJ7WHBtiv5ZejlHTpfKlzZO5qU3aLVcNjXzZMk-obuwpx22mJwf-EqMPmjYqGjQFV_7rVVSsiMQOPQzOMKYbbYuezihJRoIvYIa1Nk-eb-OJDdBKf0AmqUG4VAmKuay02FF4gaCJjQQ4LYi2mbsQAMKWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇬🇧
السفير البريطاني في بغداد : الأمريكان لم يعلموا أن السيد الخامنئي مرجع شيعي وأفهم تعاطف الشيعة</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/76094" target="_blank">📅 01:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76093">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نقل النتن ياهو لمستشفى في القدس</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/76093" target="_blank">📅 01:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76092">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGmFeJPzPDyPP0FzEEsn5DX2eMQsxMVEQJDr3tzbdSbnv1hk7YaE1ju_AaZ-1BR6dcB96pegz5N-nuNkIHgoTXS5h35k7TekaKulMvKwzA0hjGcENdVJ4GY99SSP3dHNsyQdEY0R4l6MllKkI04JRbSVp3qWZn6oWsIOJzWxVaQoycJaYss-FWX3zxgYLORA2Ps3_XQL6FVoKl59uC6he4iDReT4w9H0CPcASf53TlFFI1ukcpnxfWtl4rhI_tAxy0FmDNGgJbHyptTs5UbxiXXTdX6gsL5xdkKeYJYEL-7g_701z-00LSsZVxHWLLy83fF0pnfJoRfOlyGZG_qeSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
سيتم تسليم اليورانيوم المُثري (الغبار النووي!) فورًا إلى الولايات المتحدة لإعادته إلى الوطن وتدميره، أو، من الأفضل، بالتعاون والتنسيق مع جمهورية إيران الإسلامية، تدميره في المكان أو في موقع مقبول آخر، مع لجنة الطاقة الذرية، أو ما يعادلها، كشاهد على هذه العملية والحدث. شكرًا لكم على اهتمامكم بهذه المسألة!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/76092" target="_blank">📅 01:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76091">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⭐️
الإعلام الإيراني: دوي انفجارات في بندرعباس.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/76091" target="_blank">📅 01:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76090">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">هجوم صهيوأمريكي طال عدد من القوارب في جزيرة لارك جنوبي إيران</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/76090" target="_blank">📅 01:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76089">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">هجوم صهيوأمريكي طال عدد من القوارب في جزيرة لارك جنوبي إيران</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/76089" target="_blank">📅 01:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76088">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⭐️
الإعلام الإيراني: دوي انفجارات في بندرعباس.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/76088" target="_blank">📅 01:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76087">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">⭐️
الإعلام الإيراني: دوي انفجارات في بندرعباس.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/76087" target="_blank">📅 00:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76086">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d6e89360b.mp4?token=QybNEY3dIR-DMSZPq_a0PzRhg0z5EGYqKlmcgdHzga5IYTbJn-12H9Ut5wGPUtuCvstsFRgHmLfr58tkntLvOFBEnk3JmqOsH4swkv8hWqrne0jj6KsOmPoJmg9GWycmk_sJYzULpeG0A-jfOUiP0hQ2WUdMC3TYI1il8dcuZQEBt7CA7pQeKUCTCuGXoLtAGdCGOplM9MgT-aZzvd7PiCjiQsJBH9EFLY3UtKQJsnOoi4QW4armE93kknhf-JEA3_lfmnFdSjO4g-9tsSngW6d8LBOabfVrC5s5HfyfoVyJ4OhJL4pAKng1ftZ-cABDVPmk2UoX13TkJlhLmZzaFQkMQ2AepefeWLUzvMF-HWxEATpWO9LnXXfE5fTXtYIwAKB4053I11gN4R9W7OtJ8kxb9MaojVZ5yd2XVxqicEakWUXzD42UPB55F5OiZm_ARDKxbk7EL15OpHUKwYnQzX4UY8S04f4yKRFoiu9wpjGCRmFPrzKzMwfhoRxijW_jA5oRQE_FuwuKkTCRl1nI1F3yYNvR7JQGsZ5e6gkQXg6SawHI7UObdWLX_b363kmo_-xxM9-hmr0jbRRx-VQQLmkgmsWn0LOhkj42AEDXYULXFs6StsRpEDjArFidGVAPmgDtHzPNStydkcYM8msgasnl1BfgTJhrsCEu-VssOFU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d6e89360b.mp4?token=QybNEY3dIR-DMSZPq_a0PzRhg0z5EGYqKlmcgdHzga5IYTbJn-12H9Ut5wGPUtuCvstsFRgHmLfr58tkntLvOFBEnk3JmqOsH4swkv8hWqrne0jj6KsOmPoJmg9GWycmk_sJYzULpeG0A-jfOUiP0hQ2WUdMC3TYI1il8dcuZQEBt7CA7pQeKUCTCuGXoLtAGdCGOplM9MgT-aZzvd7PiCjiQsJBH9EFLY3UtKQJsnOoi4QW4armE93kknhf-JEA3_lfmnFdSjO4g-9tsSngW6d8LBOabfVrC5s5HfyfoVyJ4OhJL4pAKng1ftZ-cABDVPmk2UoX13TkJlhLmZzaFQkMQ2AepefeWLUzvMF-HWxEATpWO9LnXXfE5fTXtYIwAKB4053I11gN4R9W7OtJ8kxb9MaojVZ5yd2XVxqicEakWUXzD42UPB55F5OiZm_ARDKxbk7EL15OpHUKwYnQzX4UY8S04f4yKRFoiu9wpjGCRmFPrzKzMwfhoRxijW_jA5oRQE_FuwuKkTCRl1nI1F3yYNvR7JQGsZ5e6gkQXg6SawHI7UObdWLX_b363kmo_-xxM9-hmr0jbRRx-VQQLmkgmsWn0LOhkj42AEDXYULXFs6StsRpEDjArFidGVAPmgDtHzPNStydkcYM8msgasnl1BfgTJhrsCEu-VssOFU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇬🇧
السفير البريطاني في بغداد : الأمريكان لم يعلموا أن السيد الخامنئي مرجع شيعي وأفهم تعاطف الشيعة</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/76086" target="_blank">📅 00:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76085">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🏴‍☠️
إعلام العدو : انتحار جنديين اثنين هذا اليوم ، أحدهما في معسكر للتدريب.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/76085" target="_blank">📅 00:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76084">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اصوات انفجارات سمعت في الخليج الفارسي قبالة سيريك وجاسك</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/76084" target="_blank">📅 00:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76083">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">⭐️
الإعلام الإيراني: دوي انفجارات في بندرعباس.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/76083" target="_blank">📅 00:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76082">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⭐️
الإعلام الإيراني:
دوي انفجارات في بندرعباس.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/76082" target="_blank">📅 23:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76081">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇷
مصدر عسكري إيراني:
التحقيقات الفنية تؤكد هجومًا إسرائيليًا بطائرة مسيرة على الإمارات.
تُظهر التحقيقات الفنية التي أجرتها القوات المسلحة أن إسرائيل نفّذت عدة هجمات بطائرات مسيرة خلال الأسابيع القليلة الماضية في عملية "علم زائف" ضد الإمارات. أن هذا العمل الإسرائيلي جاء "لاستفزاز" الإماراتيين. لقد أظهر الكيان الصهيوني أنه لا يُفكّر إلا في مصالحه الخاصة، حيث يتواصل مع بعض دول الخليج، فيجرّها إلى هاوية خطيرة، وفي الوقت نفسه يشنّ عمليات ضدها.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/76081" target="_blank">📅 23:33 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76080">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇶
إبطال مفعول عبوة ناسفة في منطقة حزام بغداد بالعاصمة العراقية " جسر الرفرش " ؛ المنطقة نشطت بها خلايا عصابات داعش أعوام ٢٠١٣ - ٢٠١٦ .</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/76080" target="_blank">📅 23:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76079">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🌟
🏴‍☠️
إطلاق صواريخ دفاع جوي من جنوب لبنان نحو طائرات حربية إسرائيلية.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/76079" target="_blank">📅 23:17 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76078">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇷
رئيس لجنة الأمن القومي في البرلمان الإيراني:
ما لم تتخذ الولايات المتحدة خمسة إجراءات لبناء الثقة، فلا جدوى من التفاهم والتفاوض معها. وتشمل هذه الإجراءات ما يلي:
▪️
إنهاء الحرب على جميع الجبهات، وخاصة لبنان
▪️
رفع الحصار الأمريكي ومكافحة القرصنة
▪️
السماح بمرور السفن المدنية عبر مضيق هرمز بتنسيق إيراني
▪️
تعليق العقوبات النفطية لمدة 30 أو 60 يومًا
▪️
الإفراج عن الأموال الإيرانية المجمدة</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/76078" target="_blank">📅 23:05 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76077">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55cc8092e1.mp4?token=bhmRyXVZMWwclJAKRHOCC5yifU3hzeXh6PE0jk_nSOpFW_nIVlaCoT9yjEi1u5JSx5Cg-sSKQHxJhBlzlLtC2LNixHDwY3p2ikO7TVTuCGARSp31LRuBhrHfN8_i_-6kbDxqZp3A9CauxUuBhoa_lr1VF7II4s0_5orRMQg6YlmxcxuVLFHMq66_PfSXpXVe24XOm4B75AgTzeq5StvKtg1X3p6qE9MdwSVs1Ris6WnWujAUri82iTVjb65j9XrX-duZopgZ0OjubW8vnvhJmzcEZ6CQeJ4wUzbkvQl5fMkqvT5SyIRtFpIyabIAg2FgJpJ9LlF2HUVCbACsMabLnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55cc8092e1.mp4?token=bhmRyXVZMWwclJAKRHOCC5yifU3hzeXh6PE0jk_nSOpFW_nIVlaCoT9yjEi1u5JSx5Cg-sSKQHxJhBlzlLtC2LNixHDwY3p2ikO7TVTuCGARSp31LRuBhrHfN8_i_-6kbDxqZp3A9CauxUuBhoa_lr1VF7II4s0_5orRMQg6YlmxcxuVLFHMq66_PfSXpXVe24XOm4B75AgTzeq5StvKtg1X3p6qE9MdwSVs1Ris6WnWujAUri82iTVjb65j9XrX-duZopgZ0OjubW8vnvhJmzcEZ6CQeJ4wUzbkvQl5fMkqvT5SyIRtFpIyabIAg2FgJpJ9LlF2HUVCbACsMabLnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
هجوم بالطيران المسير الانتحاري وعدة صواريخ يستهدف مقر تابع للمعارضة الكردية الإيرانية في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/76077" target="_blank">📅 22:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76076">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
تخشى "إسرائيل" من إطلاق حزب الله النار على الشمال، في أعقاب الهجمات الكبيرة التي يخطط لها الجيش الإسرائيلي في لبنان.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/76076" target="_blank">📅 22:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76075">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ac03e8b15.mp4?token=qItn6sf8Nq1qz-YW28xl99BFgrzTzdGNvcetHaIkzsCirGlhPbI-A3WirHuIhar0BqewEfwazxVLghzBErQIOUDML901ZihSsOjMvRIcOCYL4s-YPGV03g1azkI8Vdn9AI-W2jccJKzR-7E-nQuyEdaHdbofKBS0uA_CjN8sao7EtYSUBDtlyM_vqTKLnWeGEEuG7NPeJ4YEY2GUsa15c3B3FMTVbOq7w6X0Edf_vMX3pdrCs27sz-6jjrNKbTp5c0wA3IZw7ViF5d96Z-ST2kuqYWv68PFnPpLwN36MQvnx2L4SzSxrCqhORwtuce1jlCdGq4YSg7_OSu1MoIxUWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ac03e8b15.mp4?token=qItn6sf8Nq1qz-YW28xl99BFgrzTzdGNvcetHaIkzsCirGlhPbI-A3WirHuIhar0BqewEfwazxVLghzBErQIOUDML901ZihSsOjMvRIcOCYL4s-YPGV03g1azkI8Vdn9AI-W2jccJKzR-7E-nQuyEdaHdbofKBS0uA_CjN8sao7EtYSUBDtlyM_vqTKLnWeGEEuG7NPeJ4YEY2GUsa15c3B3FMTVbOq7w6X0Edf_vMX3pdrCs27sz-6jjrNKbTp5c0wA3IZw7ViF5d96Z-ST2kuqYWv68PFnPpLwN36MQvnx2L4SzSxrCqhORwtuce1jlCdGq4YSg7_OSu1MoIxUWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
وكما قال الشهيد الأقدس:
بتوسّع منوسّع...بتعلّي منعلّي</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/76075" target="_blank">📅 22:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76074">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🤙
🔥
الخارجية الروسية : على الجاليات الأجنبية مغادرة كييف فورا</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/76074" target="_blank">📅 22:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76073">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0cJsR07UNFKOHdKSfbyMzLphT8lh7osjIJF11vfoGkilGliVPTyu9fB2obNDTtRt3UfoQY1c4z9uIuOpySAYcAMGfkMOONO7GH__oLdWHycuCuwaUsdr1JKKn9qqG5HRMXXpCeeNrQejv-p4j_T12qmfY7esh_C7oukO4PbX3PvT4CcqaqzcgbCNzMKHyNgtnGLnOGxCD4GsdZg06V4-4OxT5CqJIgmTmkCzxPImJoLDDDCaZRfWmF4ywk5erP-vaSZ2XOzOBJ4UE7WMt4h9Rxc26hmq82mNR5h04FXFY_VLgZ_dZjJhisImWlj8r6MmUqvcXdy1wl8knUb7X-FCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو يطلق حملة تبرعات للجنود والعوائل المهجرة في شمال فلسطين المحتلة بسبب ضربات حزب الله.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/76073" target="_blank">📅 22:08 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76072">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/126245a760.mp4?token=UDvNdZp6Bh7l7iioQeygIu-3rjjZGYbQ7N5cgNaeUZVKNw6QDTVbWj8dw6lfAysJa9O4-itXOLG16Bg-1vFhbJ-ckwNj26qCKaDhDSBBJUtXzke6qEjkR9pqNquczY2C61UUHxfIyrje9tXCSkNyHLJAB40gRji8P1jjq56joACjI9RjYDNfd2yBeQ5AZXt1NbZ5fKy0TiAokL3s-F4ghgT5DlYXmg3IDCV3NF5SA5g1afrOBbTnOa0hkHDCs65wc7EEC78jc3t0riJeVNuKfBZLKSIjD51_kUghpRtjBeAmKmDv-GeozeYAOAR_S_N4tIuxTJSm2c26bVOmuoP6u4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/126245a760.mp4?token=UDvNdZp6Bh7l7iioQeygIu-3rjjZGYbQ7N5cgNaeUZVKNw6QDTVbWj8dw6lfAysJa9O4-itXOLG16Bg-1vFhbJ-ckwNj26qCKaDhDSBBJUtXzke6qEjkR9pqNquczY2C61UUHxfIyrje9tXCSkNyHLJAB40gRji8P1jjq56joACjI9RjYDNfd2yBeQ5AZXt1NbZ5fKy0TiAokL3s-F4ghgT5DlYXmg3IDCV3NF5SA5g1afrOBbTnOa0hkHDCs65wc7EEC78jc3t0riJeVNuKfBZLKSIjD51_kUghpRtjBeAmKmDv-GeozeYAOAR_S_N4tIuxTJSm2c26bVOmuoP6u4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: أعدّ الجيش الإسرائيلي خطة واسعة النطاق وهامة تنتظر موافقة القيادة السياسية.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/76072" target="_blank">📅 21:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76071">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: أعدّ الجيش الإسرائيلي خطة واسعة النطاق وهامة تنتظر موافقة القيادة السياسية.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/76071" target="_blank">📅 21:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76070">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🏴‍☠️
استطلاع رأي أجرته القناة 13 العبرية:
يعتقد 58% أن الاتفاق المُبرم مع إيران، وفقًا لما نُشر، يضر "بإسرائيل". ويعارض 51% هذا الاتفاق. ويرى 39% أن الوضع الأمني ​​"لإسرائيل" لم يتغير بسبب الحرب، بينما يرى 34% أنه ازداد سوءًا. ويؤيد 49% استمرار الحرب في الشمال.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/76070" target="_blank">📅 21:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76069">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
أعدّ الجيش الإسرائيلي خطة واسعة النطاق وهامة تنتظر موافقة القيادة السياسية.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/76069" target="_blank">📅 20:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76068">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f73557bac.mp4?token=uWkXYaECm6Zk9f-TwecVVZv4L7W66dMDvZPExAv0UiwqQNCJT6eYNTqdKnPEbG7n5qZupk8WYMR80uK5nF5t33zlJc-MeVD18jWbBWa6lp37B8Vzg_Ma9R3SFXj0TlYAPQ3cz86-RjLP2VJk0Uh2p0Td_1mkPj-TXrc8eA__k8sjCD2Z30bXjj_VVmjuD2EFL0k8RuJy1w9293xe06euyPSaIPyqZzz4HR4RkHBrMMDKShFkFetmqKQS-o5tkWOs0UHhrsa40eHn8LDTYKcTfxuqYFc7mpgQbqLSmrTrLWJTMtKTKnE6bXq2tGX7aH-v9yIazezcRWagt1oEIYptLh-f9EQmDZubsz6zfx6sM6ln-u6zmrElvk_8mriEDQmYFQtbveK3zZ6PzrZS6pxPJ-e6eQKmmh5Zhbc1JksiH6NKB9ysdNxmHvhRsoPXS5EsxhHSOysUtFYSBycz1zg-yGM3m1_YkOCLkq4WG_kc6Jlyrb3B8RCHncBzAyKl0JeK_kAKzbMZM_e9OnhJLT9YFgP9nw1YBa66aaaw2EYo5U1UXXc38cpxCl4-eF1vLyuLv6QbjoATdVPahoPyZ6ibX0X_WvRtRCzM4ZHiyDAknF4fPBNrVvxu0WrS0jR4Ow_QIGAvRTt1N4lKkgi8GcJXDo2bQ4SlcmbC7-hIl4RdGXE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f73557bac.mp4?token=uWkXYaECm6Zk9f-TwecVVZv4L7W66dMDvZPExAv0UiwqQNCJT6eYNTqdKnPEbG7n5qZupk8WYMR80uK5nF5t33zlJc-MeVD18jWbBWa6lp37B8Vzg_Ma9R3SFXj0TlYAPQ3cz86-RjLP2VJk0Uh2p0Td_1mkPj-TXrc8eA__k8sjCD2Z30bXjj_VVmjuD2EFL0k8RuJy1w9293xe06euyPSaIPyqZzz4HR4RkHBrMMDKShFkFetmqKQS-o5tkWOs0UHhrsa40eHn8LDTYKcTfxuqYFc7mpgQbqLSmrTrLWJTMtKTKnE6bXq2tGX7aH-v9yIazezcRWagt1oEIYptLh-f9EQmDZubsz6zfx6sM6ln-u6zmrElvk_8mriEDQmYFQtbveK3zZ6PzrZS6pxPJ-e6eQKmmh5Zhbc1JksiH6NKB9ysdNxmHvhRsoPXS5EsxhHSOysUtFYSBycz1zg-yGM3m1_YkOCLkq4WG_kc6Jlyrb3B8RCHncBzAyKl0JeK_kAKzbMZM_e9OnhJLT9YFgP9nw1YBa66aaaw2EYo5U1UXXc38cpxCl4-eF1vLyuLv6QbjoATdVPahoPyZ6ibX0X_WvRtRCzM4ZHiyDAknF4fPBNrVvxu0WrS0jR4Ow_QIGAvRTt1N4lKkgi8GcJXDo2bQ4SlcmbC7-hIl4RdGXE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب:
فقدنا في عملية الغضب الملحمي 13 جنديا لضمان ألا تحصل الدولة الأولى الراعية للإرهاب على سلاح نووي.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/76068" target="_blank">📅 20:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76067">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⭐️
رويترز:
تمديد وقف إطلاق النار المتفق عليه بين الولايات المتحدة وإيران في أوائل أبريل 60 يومًا.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/76067" target="_blank">📅 20:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76066">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇷
رئيس مجلس تنسيق الدعاية الإسلامية في طهران:
لم يتم بعد تحديد وقت محدد لتشييع سيد شهداء الثورة الإسلامية سماحة آية الله السيد علي الخامنئي ويجب على الناس عدم الانتباه للشائعات.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/76066" target="_blank">📅 20:38 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76065">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇷
الإعلام الإيراني:
خبر الإعلام السعودي حول تفاصيل تفاهم وإتفاق محتمل كاذب وغير صحيح. أن هذا الخبر في الإعلامي السعودي، مثل العديد من أخبارها حول تفاصيل المفاوضات، كاذب ويأتي في إطار العمليات النفسية الأمريكية.
في نص التفاهم الموجود حتى اليوم، لا توجد أي جملة تفيد الاستعداد لنقل المواد النووية، وبشكل أساسي لم تقدم إيران أي التزام بشأن الإجراءات النووية في هذا التفاهم.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/76065" target="_blank">📅 20:25 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76064">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e9c91c53a.mp4?token=vjR0kmqR0XnZ7YTPhGi6bOFvXufvkhwVq4whKiMw-rG3yjuJeI2JWfPBwPOmyBp3VZt_uy7WdkII_zaE6XVBsJ7GzRUdDNYO6GAb2TSOZz1KjVy5224R4UED-0QhyGqVFlFI8KOqcdxEDdd8H2aP1oQiQbfB_o6SvZnw5L4-J1-OC7vqYVT3NTMXLNbJvYvQsjss3knPEEuR3nAvTWmfx9rKf6Ouaobw91K_u57Vw-j8c51fLePMx9m2G2eT0bR1-bShvconUThZRlTi4Dv26geBTgxNM6XYg3Vg_BVn62KoP_mhzdgs1M6FIilwzcMsKHkIbzswJrodqhjyY9yy9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e9c91c53a.mp4?token=vjR0kmqR0XnZ7YTPhGi6bOFvXufvkhwVq4whKiMw-rG3yjuJeI2JWfPBwPOmyBp3VZt_uy7WdkII_zaE6XVBsJ7GzRUdDNYO6GAb2TSOZz1KjVy5224R4UED-0QhyGqVFlFI8KOqcdxEDdd8H2aP1oQiQbfB_o6SvZnw5L4-J1-OC7vqYVT3NTMXLNbJvYvQsjss3knPEEuR3nAvTWmfx9rKf6Ouaobw91K_u57Vw-j8c51fLePMx9m2G2eT0bR1-bShvconUThZRlTi4Dv26geBTgxNM6XYg3Vg_BVn62KoP_mhzdgs1M6FIilwzcMsKHkIbzswJrodqhjyY9yy9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
طيران مسير يحلق في سماء قضاء سوران بمحافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/76064" target="_blank">📅 19:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76063">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cff5fa941.mp4?token=L93fTyiSgnMz_KhL6qI6k63W0h4JYbBcyeUiy-ZM2lc9PcDJSF24V8jclIEolnsllUnIK-I6YUApS5cDOBXYR68V2BEf7Vx_4gegSdvDcP4TJ9-PZCnPf8xVDAz5tbHEkDU9cWVBcRYwz4y6L5MiI4fqzxWBqOV4WNoVP7jVVXySicWO0OPYRjaqEc8RX2pjp0bGImYLzx_tGXu4W7xOpOZTHUOtCjtF_WsIQ04erhrSquT5rb3L1qf5dTNu0PYteMHOsXlnZjVp4F-fY6_bfW7lCTxffRVdWnD31uwqjNYFTa1FhuLBQfGt4QNqU7TavRIxEP0xxii4kFE9waCr5U27PJdMQd_1cewH_b9-5PNxdLzNBcBZmxIkBw6eY3TBvmbkrDHA0K7BO1NHaUhuEP7R8f_RC75RHIJVVqPkurJfgOKyhXOLOgVlHleZRqaqaqvYgWvfOCadQoF4RQGtgO_yXbS1b_RJULA6j32HpvJRicNe-BlHWWt_0nQfRL_zNsAPfAbphoxXdPU9szWMHC_yC4dlR57uwhOFLcHqs8PAkepXiCEByCqUTV6Hk7OKF5PrrBOkaVnIlczoIeKyt4aNFLGPgy-56tBjfva5kj_GRY5-vwi6ULhfgbJoVV_pkouxQtEFEjG1ai9-S6aiin-px34FkUSLLFZNOE7qhf0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cff5fa941.mp4?token=L93fTyiSgnMz_KhL6qI6k63W0h4JYbBcyeUiy-ZM2lc9PcDJSF24V8jclIEolnsllUnIK-I6YUApS5cDOBXYR68V2BEf7Vx_4gegSdvDcP4TJ9-PZCnPf8xVDAz5tbHEkDU9cWVBcRYwz4y6L5MiI4fqzxWBqOV4WNoVP7jVVXySicWO0OPYRjaqEc8RX2pjp0bGImYLzx_tGXu4W7xOpOZTHUOtCjtF_WsIQ04erhrSquT5rb3L1qf5dTNu0PYteMHOsXlnZjVp4F-fY6_bfW7lCTxffRVdWnD31uwqjNYFTa1FhuLBQfGt4QNqU7TavRIxEP0xxii4kFE9waCr5U27PJdMQd_1cewH_b9-5PNxdLzNBcBZmxIkBw6eY3TBvmbkrDHA0K7BO1NHaUhuEP7R8f_RC75RHIJVVqPkurJfgOKyhXOLOgVlHleZRqaqaqvYgWvfOCadQoF4RQGtgO_yXbS1b_RJULA6j32HpvJRicNe-BlHWWt_0nQfRL_zNsAPfAbphoxXdPU9szWMHC_yC4dlR57uwhOFLcHqs8PAkepXiCEByCqUTV6Hk7OKF5PrrBOkaVnIlczoIeKyt4aNFLGPgy-56tBjfva5kj_GRY5-vwi6ULhfgbJoVV_pkouxQtEFEjG1ai9-S6aiin-px34FkUSLLFZNOE7qhf0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
19-05-2026
آلية عسكرية تابعة لجيش العدو الإسرائيلي في مستوطنة مسغاف عام شمال فلسطين المحتلة بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/76063" target="_blank">📅 19:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76062">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19805be467.mp4?token=JQxVl7iDfwBFO8um8CngDJ_Nws7rDlVlszhkB3WOE9tqK_VmY5sc4GIv3YT4nRuRyf5V6DUDUN9YAXadsel1iCw__cX8TQNkRAbMDO2WKlTjAM5pVNPZ_hOdtF-DbXoCDAaeSrrN0D5uKVl6nS2LVozwHmwXeVfAecFFsqoZyoGJFXC4INOIrZKxd6QvftWd1dAALi6NxdsnwEtdUjt4MJ0o3hodOky9HwXdV_xSmaHzQDvtiMQiMx45XSfRQJ-GtC_DYPruWtk1PRxXjaIdHeuWIIu8CtoEiXQ_kJf84gfqUvc953ZW9NroLgQ8N2NYp6qzWsxuDi7LAg6ht69Keg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19805be467.mp4?token=JQxVl7iDfwBFO8um8CngDJ_Nws7rDlVlszhkB3WOE9tqK_VmY5sc4GIv3YT4nRuRyf5V6DUDUN9YAXadsel1iCw__cX8TQNkRAbMDO2WKlTjAM5pVNPZ_hOdtF-DbXoCDAaeSrrN0D5uKVl6nS2LVozwHmwXeVfAecFFsqoZyoGJFXC4INOIrZKxd6QvftWd1dAALi6NxdsnwEtdUjt4MJ0o3hodOky9HwXdV_xSmaHzQDvtiMQiMx45XSfRQJ-GtC_DYPruWtk1PRxXjaIdHeuWIIu8CtoEiXQ_kJf84gfqUvc953ZW9NroLgQ8N2NYp6qzWsxuDi7LAg6ht69Keg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
إنفجارات عنيفة وتصاعد اعمدة الدخان في رأس الناقورة بالشمال الفلسطيني المحتل عقب هجوم مزدوج لحزب الله بالصواريخ والمسيرات الأنقضاضية.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76062" target="_blank">📅 19:33 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76061">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcfe153a8f.mp4?token=IWGlofNprsex6-vjlgvLlPFQjgZ6HEWxxj5APkBr_dHD49y-PiF38piptOQS6VaEWjl3NbHZlZpnWKKiuvktPq8o9wzEyTzuPy54YkOX8bt71zE_qkAcaQKVyFjBatEOXGGtEPhKUF8Pw_MhqgDbRG_EOo0vJ2h3nmOar9sn6mDhZrrBoJ9RbTgcnBXEjazu2kRrAgpSnkJVmgqualwaUw7Ai4eH2g8d8roYR1dCW9gMTvwo_Ofm9itQl4bM-VcjYoJJgK0IPlY_R0tASLhpPQbF5DgRsnyHfZVgXfxK1SoWk_v2a9QlGo5MV-YZ8KgR5YtaKdRQFuAhrYjUbZc94g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcfe153a8f.mp4?token=IWGlofNprsex6-vjlgvLlPFQjgZ6HEWxxj5APkBr_dHD49y-PiF38piptOQS6VaEWjl3NbHZlZpnWKKiuvktPq8o9wzEyTzuPy54YkOX8bt71zE_qkAcaQKVyFjBatEOXGGtEPhKUF8Pw_MhqgDbRG_EOo0vJ2h3nmOar9sn6mDhZrrBoJ9RbTgcnBXEjazu2kRrAgpSnkJVmgqualwaUw7Ai4eH2g8d8roYR1dCW9gMTvwo_Ofm9itQl4bM-VcjYoJJgK0IPlY_R0tASLhpPQbF5DgRsnyHfZVgXfxK1SoWk_v2a9QlGo5MV-YZ8KgR5YtaKdRQFuAhrYjUbZc94g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
عقب فيضان نهر الفرات..
حكومة الجولاني تدعو لإخلاء فوري للمنازل والمحال القريبة من نهر الفرات في محافظتي دير الزور والرقة.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/76061" target="_blank">📅 19:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76060">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3c4d237e.mp4?token=uxFjhQBVxA2CIwh0OY8nOUwuwlGsqHQtPELLc-t_vNHo2I27o9W5x5mPd7clnqDDYfeT10sA6JsOolwacevcD79HS_fWOptn1IsLMDJs_kj7yYN4o7yBf1LX6UyTriWXqyGoHpGHiWdy1XNACT8MIGvwHg72j_7mFoQLs5EzG5juMICtJUzGYla2gTZl4eOvL-x2EgqGCFyOzvfhalTzK6T3YWJwgc4ET5n7hdAolTMhU04UX4GyAszRq-F0XYo2Vm_bUV4p5gRxG9laCJf0GICsRp91v3rocatZl2pPDGtbwv1l1VniEEVZQ-DnLdVIPbsxpjHfhesFqhJ2qPORxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3c4d237e.mp4?token=uxFjhQBVxA2CIwh0OY8nOUwuwlGsqHQtPELLc-t_vNHo2I27o9W5x5mPd7clnqDDYfeT10sA6JsOolwacevcD79HS_fWOptn1IsLMDJs_kj7yYN4o7yBf1LX6UyTriWXqyGoHpGHiWdy1XNACT8MIGvwHg72j_7mFoQLs5EzG5juMICtJUzGYla2gTZl4eOvL-x2EgqGCFyOzvfhalTzK6T3YWJwgc4ET5n7hdAolTMhU04UX4GyAszRq-F0XYo2Vm_bUV4p5gRxG9laCJf0GICsRp91v3rocatZl2pPDGtbwv1l1VniEEVZQ-DnLdVIPbsxpjHfhesFqhJ2qPORxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
إنفجارات عنيفة وتصاعد اعمدة الدخان في رأس الناقورة بالشمال الفلسطيني المحتل عقب هجوم مزدوج لحزب الله بالصواريخ والمسيرات الأنقضاضية.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/76060" target="_blank">📅 19:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76059">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcpy2FiuKe4d2cMt8OLcJMQ9Nlt29g0aDTl1BngQlsdPVEaOd-ZOgsKtsRnMv1NabMps0PUHnLeUh_5QfDoXMxTE3bi2Y8ZvwCkq9HpzPtiSY0MpyCi8T4vxNgkMEwtI7eR0mLkbEizxtE4KGHQJQ9uOPWKvl22JYcV7Cl7C7AAb6n8LIrGL0yX_eqs9lWTpNUb73cGAsuW97og0quNp6dhYZ5qlxqoq8akyp7_O9YijGfWKpcqkW2j1YLnUSl4gd0vmsHPxQgW9gILK9GaE7RacLSOSwZGuqaV75-2M7rJ6myao1jtPddXKKyhp1Boncq0EOJLKoK1rcd85KD5JyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
أمين المجلس الأعلى للأمن القومي الأيراني:
"لن يكون هناك استسلام أو تراجع"
لقد أظهر الميدان العسكري، والميدان الدبلوماسي، والشعب في الشوارع هذا الأمر بمقاومتهم الشديدة، وأجبروا العدو على التراجع. الآن أكثر من أي وقت مضى، يحتاج الوطن إلى الوحدة والتضامن، حتى يخيب أمل الأمريكيين والصهاينة في هذا الشأن. ميدان الوحدة والتضامن ميدانٌ آخر في النضال. إن تضافر الجهود لمنع أي أقوال أو أفعال تُزعزع الوحدة سيقود إيران العزيزة إلى النصر النهائي، بإذن الله.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/76059" target="_blank">📅 19:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76058">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ السبت 23-05-2026 تجمّع لجنود جيش العدو الإسرائيلي في بلدة البيّاضة جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/76058" target="_blank">📅 18:57 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76057">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c703c1c6bd.mp4?token=EOtaxaQGFIuLO6D4irAhlP0bCfW3D2J3TCIwfS97E2JRqh-0zWb598M_Rn-8icuQ_198Nc2Cuy_FWdr8W8WmtMuNduIutw0dhsNJ1VY-omBEdxxIC_frSrGHQmj_coJsNK_zn3dxq54HE7O3NkcP4YNiitkVU6oK1rAgIjs_yGS3m0UdD41jUJ_DSy7CEpIxM2iCxwiwTZmWDT_xaiG2GuhpiVorq3ghICmq441SxH838HpenvUXWD5ZX9XReEqzEOJ6k8d5GwRSIG2PTIXHfx8AatINydXPQ5_d_3n5l0HcYVh_XNXPSev_lq7COW0I7LyPKJztahH05l1ggtVQjnBHj9_1QMANYRuIBJKr2_Gf7ZOakHIzcX0d0vJqypXdyZQtzrK32J29s23_oz0xhAef9cc0Z6wxKeNbj9QAWAaNCprqkNGgGBiKYXmfXtTH2_GKCeJ0_JHSqvJUF-OX_ufhT0XFLwLQquqkvp9_uPe4BsMHR0MmCWrUyG8NPGISrHtByyRZdPF6jz3GvPvfCP-PVAeDC2hXnQDtl9552NkE4Cg4Tq_N34qgwretk0kN1lTCWhitjSOUtmk_pgIu0dLe-8x21Gz0TxQkRHnB9gxVpHT2hnHW3RrvNiv6xLgb7JDxZG5Is_g58LfHFxRrEKF73lt6odEdikQduv0NBdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c703c1c6bd.mp4?token=EOtaxaQGFIuLO6D4irAhlP0bCfW3D2J3TCIwfS97E2JRqh-0zWb598M_Rn-8icuQ_198Nc2Cuy_FWdr8W8WmtMuNduIutw0dhsNJ1VY-omBEdxxIC_frSrGHQmj_coJsNK_zn3dxq54HE7O3NkcP4YNiitkVU6oK1rAgIjs_yGS3m0UdD41jUJ_DSy7CEpIxM2iCxwiwTZmWDT_xaiG2GuhpiVorq3ghICmq441SxH838HpenvUXWD5ZX9XReEqzEOJ6k8d5GwRSIG2PTIXHfx8AatINydXPQ5_d_3n5l0HcYVh_XNXPSev_lq7COW0I7LyPKJztahH05l1ggtVQjnBHj9_1QMANYRuIBJKr2_Gf7ZOakHIzcX0d0vJqypXdyZQtzrK32J29s23_oz0xhAef9cc0Z6wxKeNbj9QAWAaNCprqkNGgGBiKYXmfXtTH2_GKCeJ0_JHSqvJUF-OX_ufhT0XFLwLQquqkvp9_uPe4BsMHR0MmCWrUyG8NPGISrHtByyRZdPF6jz3GvPvfCP-PVAeDC2hXnQDtl9552NkE4Cg4Tq_N34qgwretk0kN1lTCWhitjSOUtmk_pgIu0dLe-8x21Gz0TxQkRHnB9gxVpHT2hnHW3RrvNiv6xLgb7JDxZG5Is_g58LfHFxRrEKF73lt6odEdikQduv0NBdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ السبت 23-05-2026 تجمّع لجنود جيش العدو الإسرائيلي في بلدة البيّاضة جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76057" target="_blank">📅 18:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76056">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇷
‏
🌟
أعلنت الرئيسة المكسيكية شينباوم موافقة حكومتها على بقاء المنتخب الإيراني في المكسيك خلال كأس العالم، بعد رفض أمريكي لاستضافته.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76056" target="_blank">📅 18:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76055">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FckmnuJheV22EFpjVqB9Ydx3lQTdX-7x-wSfBipcSQadYThsNSUIXVjgllDRl5-Xo2Gheq-mdLN2Z00Pa7nkMRes70s9x-IonMzdXXBFW_Pl_J7P5F6-8wRhZITC6GALgiv5AllaUErdUPZ8-OkM3q2O3gFt0YMeZqYYsQo_2a8Gicr0Ya9y6mz2nZYKDyH-K6TKMEIf35IPQKyFCR1zxPkziFkZTOhsgblKK5-R7o6DlzHvq4IRsy3p876V_2JOsNpYkYzRfB_uqhKRNbvlc4KLb6umoevca8qZMWepGxc1SDJh6-Wa3rFNu4qExTBHf3UearH2bchhcFRuvw6IYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
حزب الله:
بعد قليل...
تركضلي تركضلي
😄</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76055" target="_blank">📅 18:20 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76054">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🐦
سي ان ان:
تقول المملكة العربية السعودية إنها لن تطبع العلاقات مع إسرائيل إلا إذا كان هناك مسار لا رجعة فيه نحو إقامة دولة فلسطينية.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76054" target="_blank">📅 18:17 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76053">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🌟
حزب الله ينشر:
وَكُلّ عيد مُقَاومَة وَأَنتُم في نَصر.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/76053" target="_blank">📅 17:40 · 04 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
