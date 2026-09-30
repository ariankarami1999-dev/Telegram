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
<img src="https://cdn4.telesco.pe/file/qUbg_NQRHjPEsrj-I_y_DA3bPo_qpmWkhU6JpUDt4EbqnoegZT3p3LwMFBxg7UX80rcHLDEC1ifps5UTo3LbLizTg97BZkbvs9PGFz4VJu6HGErsi5JLyZzzVh4S33yXLeGcxkNBI67wXkq5t6-3woGaNKMEYAONocA6C0VQUcLqe82oa5fsJwkEmHHn0sr_YkcyMcL4UDSZCgQZt5AKuPT2w-TcqYva3DPO-FQJ_8FuXkrybH5szuU3Io_iiUjNTbLQ11Q9kUGbcXLMA2e_lU3qq79gWsNL8tV-KCqu01fDWRZiWzKgmNbA9ClB5wgjDZs8lCy-27dD8M_-wIfXnw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-08 13:22:45</div>
<hr>

<div class="tg-post" id="msg-465468">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mO6GPm2onqp1WyF1HGcsT9Em_W5n7Tq1eJQUp-xVk_gvGudfs0LCMuARRWq5HO17cTFrMUZJ7wqNz-QpqxmT37MZnAe_wo2A8RNOpzk2vcIgdGFTjlpm1j2MtCB8ulgt4Lwu2bJWX6BEOh4Hm5qVSG5x4DFnH62IX07ttVeWF8CEbKL0QyhVMFlX6EI3Pmq2Qpmit2mmalxCeLpDX_0QxQCV0s2NalhwINsecRaWmbQ1jIxUykGercpSGlf59TLul1SC7zZkLaZ_cl1Otcqxx-l_uoaHSHsuuUrAwry4Eo1Sy47Udn8jvd1bZ_hCFZDtOaB4VMPKaKLk_QRDJlQ41Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعام هنوز درباره انتخابات شوراها نظر نداده است
🔹
علی‌رغم انتشار برخی شایعات درباره تأیید شعام برای برگزاری انتخابات شوراهای اسلامی شهر و روستا در ۲۴ مهرماه، پیگیری‌های خبرنگار فارس از وزارت کشور و هیئت مرکزی نظارت بر انتخابات شوراهای اسلامی کشور نشان می‌دهد…</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/farsna/465468" target="_blank">📅 13:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465467">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzwUzMcbgslW69XXVfcuRob28AqYo6gsBYxn6pEH-8zVmQaYgIQDIhjp97Z_RA8de5TNTJtVq2NpuAtl3J5XtEgay3cvctB1n5XTRftbagSIv5rncg-6Xq5GqQ51YXfPIbwnI3fUly5J04G3sZ0fvYEIo3fgITDwb-YRWl6IOZ1N2D3pYxV-l0V1uKIK-hWR7xjPK1Tf3EQgf7t-0fclniLA6I8Mst2f9PtXZtAD17mXEO-juOVFBdC6rXxJMJkt-JeLGAlJjbDNKH--1Y_nhYFcRQKFQNqlRpAk794_KjuoTgqsjU6GzrRq_gm8vf3lp-4_opK5YFL5xRGoH5jHGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سازمان عملیات تجارت دریایی انگلیس: یک نفتکش در تنگهٔ هرمز هدف اصابت یک پرتابهٔ ناشناخته قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/farsna/465467" target="_blank">📅 13:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465466">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HF-tqikOshohQLbP4k8UP1eBKvsL-f8td3x5ssTJne5_C9T-9VgTnRZrIPmsCxeLWiPkAIkPS54Kh2rXl8IQN0U9GUxBrqSMfNdVkRHqC2PAKwISh-cEYS37L-2Tqxw3KRSztJFOx4ilL7HfmyFnu7YKBME44b1na1J8_MaQ_W5K6n5k3zghuRCys2KewKeaJAn5w0OlsQuCQ_t78HPbW6unfaLh7OSt5UbUz5hbtDEW6Loo9_F_cxYkB-XaDz0kN11PfJrQ_Kz2_xQkIX6MiMyoAdFNg-Q_m57QciC78U3rL79FtJwL93-1ceby7XXD9MS4S2-NK01xZ6tpetG-KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروازهای فرودگاه ریاض باز هم متوقف شد
🔹
منابع خبری از توقف مجدد ترافیک هوایی در فرودگاه بین‌المللی ملک خالد در ریاض خبر می‌دهند. این سومین بار در هفتهٔ جاری است که پروازهای این فرودگاه متوقف می‌شود.
🔹
به هواپیماها دستور داده شده تا در حالت انتظار باقی بمانند و هنوز دلیل این توقف مشخص نیست و مقامات سعودی درباره آن توضیحی ارائه نکرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/farsna/465466" target="_blank">📅 13:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465465">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">افشای عملیات جدید موساد برای اجماع‌سازی علیه ایران
🔹
اطلاعات دستگاه‌های امنیتی ایران نشان می‌دهد رژیم صهیونیستی قصد دارد با اجرای یک عملیات تروریستی در منطقه، مانند حمله به هواپیماها یا فرودگاه‌ها و قربانی‌کردن غیرنظامیان، مسئولیت آن را متوجه ایران کند تا موج جدیدی از فشار و اجماع بین‌المللی علیه کشورمان شکل بگیرد.
🔹
دستگاه‌های اطلاعاتی ایران اکنون روی خنثی‌سازی این سناریو تمرکز کرده‌اند.
🔹
هم‌زمان با تشدید تحریم‌های آمریکا، برخی کشورهای همسایه پروازهای ایرلاین‌های ایرانی را محدود کرده‌اند؛ با این حال، پروازها به چین، روسیه، ترکیه، ارمنستان و پاکستان برقرار است.
🔹
در عراق نیز با وجود فشار سنگین علما و اقشار مختلف بر دولت برای برقراری پروازهای ایران، مسئولان عراقی فعلاً درحال مدیریت زیرکانهٔ افکار عمومی هستند.
🔹
در ادامه این تحولات، ساعتی پیش خبر ربایش یک هواپیمای دبی-تل‌آویو با حدود ۱۰۰ صهیونیست منتشر شد. برخی وبگاه‌های صهیونیستی مدعی شدند که پس از درگیری داخلی و تلاش نافرجام یکی از خلبانان برای سقوط هواپیما، این پرواز با فعال‌سازی کد ربایش توسط خلبان دیگر در عربستان فرود اضطراری داشت.
🔹
چند روز پیش از آن نیز رسانه‌های انگلیسی در ادعایی ساختگی، حمله به یک پایگاه آمریکایی در خاک انگلیس را به ایران نسبت داده بودند. محمد محمدی کارشناس رسانه، معتقد است این اقدامات می‌تواند در راستای آماده‌سازی ذهنی مخاطبان طراحی شده باشد.
🔹
پیش‌تر در اواسط سپتامبر نیز سناریوی مشترک عربستان، آمریکا و اسرائیل برای نمایش حملهٔ یمن به خانه خدا با هدف فضاسازی علیه انصارالله با شکست مواجه شده بود.
🖼
اما چه موضوعی باعث‌شده آمریکا و صهیونیست‌ها سراغ عملیات پرچم دروغین بروند؟
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/farsna/465465" target="_blank">📅 12:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465464">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8642079dec.mp4?token=LaTpOaNl04Gn9jy4uSVSfmRj3DfFBBZUWqg77iWmlVWtySkO8aPiAbdmFJ3F1UwYc_kGlzcxIFDlQ-5SWc8aiUeBTfY_JBmgEkTig5oIbUE54j6nYwPPp4KwkjIOh8JyykQt-1agygwvPGdaInMvNivG5MBO50CamD9Ge4jlVIcCMb8otWY8CySHfk_47TBZ2uLGXRgxqR5Jqp9W4Zo867QiyY-lCmPMnadcdWwlhxdmZGgL4fwSCypgPbZOATWRRiZRWTgXV61wKcTADVKMmCKr--nXmUteE4fxFLMfw4egNOlhijFWgw6HH72HfjepQ-do8RR38FqXz5Ub3fKLxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8642079dec.mp4?token=LaTpOaNl04Gn9jy4uSVSfmRj3DfFBBZUWqg77iWmlVWtySkO8aPiAbdmFJ3F1UwYc_kGlzcxIFDlQ-5SWc8aiUeBTfY_JBmgEkTig5oIbUE54j6nYwPPp4KwkjIOh8JyykQt-1agygwvPGdaInMvNivG5MBO50CamD9Ge4jlVIcCMb8otWY8CySHfk_47TBZ2uLGXRgxqR5Jqp9W4Zo867QiyY-lCmPMnadcdWwlhxdmZGgL4fwSCypgPbZOATWRRiZRWTgXV61wKcTADVKMmCKr--nXmUteE4fxFLMfw4egNOlhijFWgw6HH72HfjepQ-do8RR38FqXz5Ub3fKLxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیر آراسته: نسل جوان شاهد افول سلطۀ آمریکا خواهد بود
🔹
جانشین رئیس گروه مشاورین نظامی فرماندهی معظم کل قوا: فروپاشی رژیم اسرائیل را من هم با این سن‌وسال خواهم دید.  @Farsna - Link</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/farsna/465464" target="_blank">📅 12:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465463">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wjdn7uUIFHptqi18QV_JjZXfIUX95ZPdGLmAeodmDPhrj6TFpXBAckls0KUVi9hYqSXC2KmdkoLJEX5q2ygiDP66HEGUOAltPpUdoZpXXr-pb9sC2I7UxI5zqN8McD5j48c1Vk6tMEiiorBNF_Eig-Sf4UOzCJvXm9_KbdWubrdQHr1YFIZclRJmglwCS3VSsiTtVvvC50wjSMunUJA4HKpuR2PIdKlzwMqNgupWCNTge5RcNVS-6GRbEKw-LKbFQWqiLxsyydKQB6Zhl6XpGlIEq5bQuWSFfMw6QE2wwRc2MfSu2emTb-YHF-1moXD9Hvn__ZoK0akexxB1f6rjTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردشکنی صبحانهٔ بورس
🔹
شاخص کل بورس در آغاز معاملات امروز با جهش ۲ درصدی به ۷ میلیون و ۷۴۶ هزار واحد رسید و رکورد تاریخی تازه‌ای را ثبت کرد. @Farsna</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/farsna/465463" target="_blank">📅 12:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465462">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00999b14b5.mp4?token=sWu-QyPz0vPujwFzTqiBasvDNgCl5vlUJIss-Y_Wk65dasmyraeQcDA0a74I4dJF3JpT2FjacjK0EVq2qytJD_xGluJ-NdM1-70MAIP_5mmd2LRO9dkiPHzHqAql22PZpHHpTVWG6anKFHna1KnbGjD298jpZm8TqnN7tOLMdBOkV5kQtPvFAuQH5kIePkwivU7mWQmYye-ialp7DLs9g690157vCOOvGT6_3BQZ2UYzmTNK6-dINisjWjyYREVNlU_Nj41eQAcs7UHvBL5aUjUxaGqbz5HMZ8L8DVo_QJkYOFwvafaNyPBBe2cR0RSUiqKZtxqxztqd2IHPhN-zkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00999b14b5.mp4?token=sWu-QyPz0vPujwFzTqiBasvDNgCl5vlUJIss-Y_Wk65dasmyraeQcDA0a74I4dJF3JpT2FjacjK0EVq2qytJD_xGluJ-NdM1-70MAIP_5mmd2LRO9dkiPHzHqAql22PZpHHpTVWG6anKFHna1KnbGjD298jpZm8TqnN7tOLMdBOkV5kQtPvFAuQH5kIePkwivU7mWQmYye-ialp7DLs9g690157vCOOvGT6_3BQZ2UYzmTNK6-dINisjWjyYREVNlU_Nj41eQAcs7UHvBL5aUjUxaGqbz5HMZ8L8DVo_QJkYOFwvafaNyPBBe2cR0RSUiqKZtxqxztqd2IHPhN-zkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بزرگ‌ترین سوال مردم: آیا دوباره جنگ می‌شود یا نه؟
🔹
سخنگوی سپاه: ما الان در جنگ هستیم. به اعتقاد ما الان آمریکا شرایط قبلی را ندارد اما در دنیای جنگ همه چیز محتمل است.
🔹
آن چیزی که مسلم است اینکه دشمن با توان ایران و ارادۀ قوی ملت ایران برای ایستادگی آشنا شد.
@Farsna</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/farsna/465462" target="_blank">📅 12:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465461">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcztMYnpsbTAAr9WQ_-iMay7bkIbZGtk5_mHmhj_ontAOw2bBbqNdyFzhMp9lCWhTygO1w2rY6fCaapO-W7ivrVHfYYwBKZU9XYkvfIP5NO8z22R2D2cfVaFvXB9uXjq4t6jZGyZ2yHk1JqWZm8fjFIffrNq5r53ylAEScUYUF2X41RqNVExFZ5uYqNUKjeMluB5OiPavXprGZ2x5MrzTF-wqJxpOoyorNSyIFOAfX7kzVfVrWyDCEh_HxEbCZ70Ky5appjz3C6mugvMySAWOKkNv4OMcbCeJSA31XK7ecoIUJzprx7Ks0mD8QMDrTAjGmDdJTMBxrnW9wl2V4k4Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محاصرهٔ دریایی حریف تامین کالاهای اساسی نشد
🔹
با وجود اینکه دشمن با جنگ اقتصادی و محاصرهٔ دریایی به‌دنبال تحت‌تاثیر قراردادن ذخایر کالای اساسی کشور است، اما بررسی‌ها نشان می‌دهد این فشارها تاثیری در زنجیرهٔ تأمین غذا در کشور نداشته است.
🔹
در این راستا وزیر کشاورزی اعلام کرده است:‌ «امروز میزان ذخایر بسیاری از کالاهای اساسی بالاتر از کفایت تعیین‌شده در مصوبات است و جنگ نتوانسته زنجیرهٔ تأمین غذا را متوقف کند؛ اگرچه هزینه را بالا برده است.»
🔹
معاون توسعهٔ بازرگانی وزارت کشاورزی نیز گفته: «ذخایر برنج، روغن، نهاده‌های دامی و گندم در وضعیت مطلوبی قرار دارند و تأمین کالاهای اساسی بدون وقفه ادامه دارد.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/farsna/465461" target="_blank">📅 12:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465460">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhS8RLdF-zu9gPaPAXB7L2-YbYXC1MeKZpd_dgt2h_TOFCYjjKkffLV8un4LMdfZpVBH1dyzicoqmhAuixn60n5RNZKhXQ9k7ygKDkPZczXEfqfBaoQnET-sR7J62w0hwCgBkk8qlOpelUXCEoHrb6RA7L1M6RGII7yqLkkMt0fyenW3fSh8qHbsBKxKktmlof2B5XQ1hP6vj3GgjpcJkkdmQhgGQGvwgHVDPXZaFq0Tz3jKWH3SKxQ2mVfbY8Vh_GeF6g4FvwM5JRKlE2u_zfsMgmb-Jj4Bat_JfSYdbLYmbD4-6tRCzZ8LZQOHrmJ_dnMgBDyGKvuwd6SEGr6Mdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌‌ حمایت مجلس از طرح «تورم صفر» شهرداری تهران
🔹
سخنگوی کمیسیون اقتصادی مجلس: این‌که شهرداری بتواند کالاهای اساسی را با قیمت مناسب و بدون افزایش قیمت در اختیار مردم قرار دهد، شایسته تقدیر است.
🔹
اگر کمکی از دست ما در مجلس و کمیسیون اقتصادی برآید، حتماً کمک…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/farsna/465460" target="_blank">📅 12:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465459">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841242913b.mp4?token=pAAG8hpfPliwbDoeWQ8QQVaLdwzb7hFBr-60_DE5H4wt0OioQ2g4jLe1ZuVBSgtSlJ-tcrbi8BGu0UT2_evczhuHytG_M38eML28xprVlz38Iqre_rnnPhXUuS2hJozmwLInuzepTLByNMnpxB6eb5m1YbyIu3nFwljIgcox-CxJcx1hffC87z1e2KvOd1iYrw87a1HRGN_8vC-LER1qNfZhMI_RSd4fWpwmJ63CmLs_wpNv-Dk9y3TPrMbT01EhQbsxfKWwpKtcSkBbkPERmVWDJFtghqm5T6m2ftX9OVcAalXQn99ZzVt6qa76mCwVXNJslP1jJ7coRb9dO5UhiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841242913b.mp4?token=pAAG8hpfPliwbDoeWQ8QQVaLdwzb7hFBr-60_DE5H4wt0OioQ2g4jLe1ZuVBSgtSlJ-tcrbi8BGu0UT2_evczhuHytG_M38eML28xprVlz38Iqre_rnnPhXUuS2hJozmwLInuzepTLByNMnpxB6eb5m1YbyIu3nFwljIgcox-CxJcx1hffC87z1e2KvOd1iYrw87a1HRGN_8vC-LER1qNfZhMI_RSd4fWpwmJ63CmLs_wpNv-Dk9y3TPrMbT01EhQbsxfKWwpKtcSkBbkPERmVWDJFtghqm5T6m2ftX9OVcAalXQn99ZzVt6qa76mCwVXNJslP1jJ7coRb9dO5UhiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیر آراسته: نسل جوان شاهد افول سلطۀ آمریکا خواهد بود
🔹
جانشین رئیس گروه مشاورین نظامی فرماندهی معظم کل قوا: فروپاشی رژیم اسرائیل را من هم با این سن‌وسال خواهم دید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/farsna/465459" target="_blank">📅 12:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465458">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6b8d09462.mp4?token=cxg3hyDNG4B1AMAmXFZEyHXw1iAjTYCHSWkwwXXh0F02vieUdlm1UCCxJwv9IiB2y4xnPsxI8mT8yblWVB6P5ohBj-gD5ANv6c-yXU49FSSrW52VkUCXOtIvoZIjHKI-9GLNFWgsyq-Al3CPWfMcaNiT2DUQ7db8mo9cHU4jM_TfNxAwg8MjSr3CgAGIcZOVfz3_yi0cQ3vm_K4x4sw8rt3C13JE8kSmWRCvPCFxqlK1LwRQsJl6tWewRKShK0pVyPCK8w1C1hegoPJlWSktyDFmJ_OfWIW-Zvg6SdMYhpfLlDdD5Ji9GzC64aJCJCRXlORETU8Br4GIiyMC5pcvxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6b8d09462.mp4?token=cxg3hyDNG4B1AMAmXFZEyHXw1iAjTYCHSWkwwXXh0F02vieUdlm1UCCxJwv9IiB2y4xnPsxI8mT8yblWVB6P5ohBj-gD5ANv6c-yXU49FSSrW52VkUCXOtIvoZIjHKI-9GLNFWgsyq-Al3CPWfMcaNiT2DUQ7db8mo9cHU4jM_TfNxAwg8MjSr3CgAGIcZOVfz3_yi0cQ3vm_K4x4sw8rt3C13JE8kSmWRCvPCFxqlK1LwRQsJl6tWewRKShK0pVyPCK8w1C1hegoPJlWSktyDFmJ_OfWIW-Zvg6SdMYhpfLlDdD5Ji9GzC64aJCJCRXlORETU8Br4GIiyMC5pcvxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس‌دفتر رئیس‌جمهور: شایعۀ موافقت دولت با استیضاح میدری تکذیب می‌شود
🔹
در فضای مجلس شایع شده که دولت با استیضاح وزیر کار موافق است و خود دولت این را گفته.
🔹
شأن دولت قطعا این نیست. رئیس‌جمهور از همۀ وزرا با تمام وجود حمایت می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/farsna/465458" target="_blank">📅 12:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465457">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bb34abe68.mp4?token=opT81etFWU6cS5l0_GZAZQ5d_RMXWsGCH4djpGUcAUBx-S-uDb1bsmmuUAxDrfLmCKLcjNvfou2vvnCJ1HCTsGjygaKMogqWWiwllau-3ZQEpA90yqBS-AbeHMxukUaHfQonNT8bjEAMXBno58t0jcwJUfB_rlGiygpVlc6fsRtg4A00lp1IuI_KSMY7hxuWx9518fntWAdYXdfoGymqBYoltkrSP3RCK53OWHyxJJX7VfF8YLd0z5ztrAPJ_iMcjSdd89a-gnD8tu5_e_A5IJ5CqsFTXD3bal_MNy9lMRNamoyH-3ZfFOlISCAQgm0-JJV9ggFsHbjAPzgTEkf25w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bb34abe68.mp4?token=opT81etFWU6cS5l0_GZAZQ5d_RMXWsGCH4djpGUcAUBx-S-uDb1bsmmuUAxDrfLmCKLcjNvfou2vvnCJ1HCTsGjygaKMogqWWiwllau-3ZQEpA90yqBS-AbeHMxukUaHfQonNT8bjEAMXBno58t0jcwJUfB_rlGiygpVlc6fsRtg4A00lp1IuI_KSMY7hxuWx9518fntWAdYXdfoGymqBYoltkrSP3RCK53OWHyxJJX7VfF8YLd0z5ztrAPJ_iMcjSdd89a-gnD8tu5_e_A5IJ5CqsFTXD3bal_MNy9lMRNamoyH-3ZfFOlISCAQgm0-JJV9ggFsHbjAPzgTEkf25w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس‌دفتر رئیس‌جمهور: شایعۀ موافقت دولت با استیضاح میدری تکذیب می‌شود
🔹
در فضای مجلس شایع شده که دولت با استیضاح وزیر کار موافق است و خود دولت این را گفته.
🔹
شأن دولت قطعا این نیست. رئیس‌جمهور از همۀ وزرا با تمام وجود حمایت می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farsna/465457" target="_blank">📅 11:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465456">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dj6jaKX25oS4GbUJpYNNSt1RZeay7S2h12qh6X4n5PbXF1oY5Vck8srqnyuTgHYqhePYeJ3mfsN9IDChJbzQGYc0vusLXglBGbkHWZo1-MifY3LUGZ5CTAMRaxmhK1sW2CnY3EFJ72f1ODK0PM_KsoSyuyvM95SacqzRqRCcAgUHJfqt0V1KBPDvL8YiMfIFVbwgYOGUDn5wDoQJX8F0SFa9N-6YtglptgIyeNEkFUZJD0c8FYTof7xcwtohuuSpIQ0qARLyrQt1oD3HqwUyGf_kgVVcsj7WsJbkTmNaqTF2fK8wQpZ0kdoGAkNalaoDCpht5tarTQfvRxvFWYyl7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
عراقچی: طرح ۷ ماده‌ای از طریق واسطهٔ قطری به آمریکا منتقل شده است
🔹
امروز یکی از واسطه‌های قطری دیدار مجددی با ما داشت و دربارهٔ اینکه چگونه می‌توان برای تحقق شروط ایران راهگشایی کرد، ایده‌هایی داشتند.
🔹
آن‌ها این ایده‌ها را با طرف آمریکایی هم مطرح خواهند…</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/465456" target="_blank">📅 11:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465452">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IId7nFNTG1ryFgIeRDn33MJcpPVXJ0zL9rc2RRoO4qi41zs0NGP05rSlN-Eqxg3Skh2fjw538d4K2BL4gVfDJymqRQGwEcYVE8RPiz7xzsaUwQ6un3d8YRv9ZB4TJDn2HpeW-SsNMYQSmtX8espz2j7fSSXlkDEtw0rc5ZvIqPuMDNksENWnR15U4ETSyyE_ZBDYNNXVYCOlCm2pvDfxwZDBUv_G3it5X1gRPV6DX9TDQi_NJE2S5mCXfz5ihG-NrCnmTPleksq0v4Q4AroShdMqhS5E7tIVJeoNLOybGOh4xmdGyJo3q85DXGvjL7nnZuMBe3vtU-mZh3t0LH2WVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QapKlXAfXj__d-toRR9u0PXzzaYNzaiTEGPvjIEZg2hVKGGCd7W7R7Zrkuapjl6doLxiThNzGwVafSdce9cS6VaamHDRqT44J0Ys2SOextiC6PjlrtXcnpVboVv9jJTxZ0ZtdnuyRR9b4SIXT6Xj0MSJTTI5ea8_SriAUb2VCQhPQTJ4Hx71g2nkGCVbSjaJjcZvspKP_MCHeBrVPtoScfPLDKfi8LloW_V94flN70onK42vNbvWt_Kv8KGYaIqqOOZ8woDs471khsJrJQBIEQoe13rJ0rBmXiBU6YUPfJkzT4fzdbAZ9MDbkgoVsW1k5AFU7qd5V2ti96GNmZu9VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u0jW6nqrN1g_2EUSKRg9SKA3XudPOXBxutphg60_sXn5lsf4mNrdDpudCLBT6ds_VXSq0Tm0yw2AzMz9NfZ56OG-vWClfX0z6fYj_GNmso0xXY5LKIx4R8b61_E9GoDzB3JtLFMswKI1jb1cOrDhpel0LHe2l3eJuI4SdhNmWkRZBKSz537ksRuYaaLeHBm8hRCqBHfeZQFudYcgs3zcrpX9t5GjKMcIK6dzS-TMuAJg-Ty6YCUcpH7_J91ZeXRP6laKJc8fhT1RNXxjYUbdEOIqjIw6ltE10EIbYCxgUnOmbKZboPZey3Pj4tqpAtnE6ScwTLdSnMIwN379zYJsRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QZUOdUm7cxmYGykq1k70UDM20a3pDkPplTvUliAzOHVK5tV8hzKfhUsOJsuyykVjNG2BaZmm-Lgl7-yR5uTYGY-SeY6oROVzlipomz7V01S7EXnblR3loSanJU_NHEUeaJiwN5RlIPHi_OJG9AgbAijlZ5RLN9lQCz6cbNPR3DRpqD22jQzk-aC1wEGzh1HjtapXo3RFN_kQJSOJlDGg4-XtNmSeJQFIP-q6I54HrhFDpoOGLc3vI7CeOKbznmKlpBNAR12VVhr3VHobC3lmRH5g9Ox0ta0OS0MbWuWPclu9uZ6ROc2KCdNWSSxAQBO-hAwVwrCS-xTc24tnmcSsGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان: اساس و پایۀ اصلاح‌طلبی، انعطاف‌پذیری در خود است، نه طرف مقابل
🔹
رئیس‌جمهور در دیدار با فعالان و کنشگران سیاسی اجتماعی احزاب اصلاح‌طلب: پیرامون مسائل جاری کشور و به‌طور خاص موضوع مذاکرات و روند آن، طبیعتاً باید با جامعه گفت‌وگو و از ضرورت مذاکرات دفاع کرد.
🔹
بیان مزایا و دستاوردهای مذاکرات، نشانه آن نیست که ما در مقابل دشمنان سر خم می‌کنیم، بلکه نمودی از شفاف‌سازی است. نکتۀ قابل توجه در روند گفت‌وگوهای اجتماعی، پرهیز از دعوا، ایجاد اختلاف و شکاف اجتماعی است.
🔹
اساس و پایۀ اصلاح‌طلبی، انعطاف‌پذیری در خود است، نه طرف مقابل؛ لذا تا جای ممکن ضرورت دارد میان تمام ظرفیت‌های سیاسی موجود در کشور، همدلی را افزایش داد و هماهنگی و انسجام ایجاد و آن را تقویت کرد، زیرا چنددستگی باعث ضعف جامعه می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/465452" target="_blank">📅 11:46 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465445">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rTOYd6RtOlCxb4NwIOoYcmrRLWccAOQQrux5sF-iTZsxI3fLMYRj3qyOi8fCPEhn4p3PZCIuNlNr4nMn4z_vCv0wmAnbuOoYOgymL5m9XZZVf8TfxJPAUuwV98mbUJiADDDFlU1JQ6S4BLwRuDbh4py7a_ARZyVAsbLMzRAtqNq-wPzKb2wqd-LD6M-20v9u_GWNdKfcqAP0PCYGZhxLVuIxu20-wRBTmbpyOIAVEjLq6Bo9OjCTGuivfG8-kUhDZ3YgonC8ML_jbGGYogqIO--7Cb1KQ3wETTux4yl18DyPgZCeJ7n8gujURLusFqv1UYXDysu3_OtdoGOkkFWu7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a1oYxsSLDj_pkz1WcMJscUnNZhN2Shry0clZNAw_eB1vxMy3tnSnAirKHFUDUtAokS_lI4T1fF738QnWCZCvtvhz4lRqXBskJtBG5I6mf7LDfm1FtgZaFK3H405j_Ljqpx8YoDU6IcVPiB49GVUbi3WO225LQdT05oWIAv8LcFcmVgpXJETdXWvonBViJaHxV_UvL97r0pcEuq2_cUQtm7gO8RmN_iGiuPyYBhJJ90s8PSHIflBJpY2Fy2EaLkbephxTaa0DWvwXLzwJ67RRf_Ggi73lo_-8F1iU2_cCqVRwpJkz0oexZBbpt8eE-49Ax9gBw_5wNLDij-vKWrTCng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QpLfgThHfLNhuasaSegN4Uzinl_UOrc8gj8n6YWGiASjoYDWxYs4e8LRs3L5NpNbiRg8bdDkD52UbKFVLoC9ahsGXf7iL-sEvGAd5NKATeW4C5teGLIdAWfnjPmEU9uCZxcdr7MUHMUPDPgWZnX-V2oWbhwq0B_JXQDBmlxf5fXtYy4GA6mEPp3-o4efC_fORXV8fRHFjxvEgudM_iERSCkUxb1ISFomRRo_cKfIBl2xaVmLJNePlm7umRnFoBade5VxKUuKYhJkzAleTPbR0C5kLpqWakw3YOuAc8gowidOi1yx7Wt5YY5-QZDApDtqpA9DVd_FO-vMCMQeAANUNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BxV2VwrCm2PhuSdyDfAwSVe7kBn_cHPFzTyRk_jzVmwgeNb4HzJADMClP3RVsGMOtyMDI0tp4u8FgytnQnEtA-kADVGkzMgjcnpHOOkCnrYdqZscrVmCBdJ91bslc7Omk_zuEh6TCEElCQrfMG2w0bATniuvGgQO4dI_KXY4j2mdk5Ta4bH8gP7oVhQv0u-M-xjDxgXRbcW3CKT16_Y4UnqyWJv3sbwV4h9DkKJQcjiiwvkugV0kPjqTsKynzdhKvvocWED2BqKsJ1NxaNcuRx1cSimIh0UrBswvv0soBOLNHuKo47XVb_6rOFl46BWyUcxcLXZrSNeQdpVV4IEf3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TeX11JKX9c90a6DN_Vk7tnvYe4YQ2BQokIFy1Im8LbL-a6mZmjsI9ALe_v_feO_y2EVmqXDsDmsOAULyqMtwAuvKYENrol5nGgoP-YQlnhAjDHDvYZV3klSsk-NE-h8ZdR32ITvZ122gQGgEHjmYaUN2wXAGWc2PQty9oeWfUF3cIl-fj4LS8p6OBGcis97Pe2hrosq4q2hXGQEP67J1PEGlUo0K7wFFQJ4z4PESiRnSP9Ty6FwEOVf3p1tA4ILlEcQ7MuChNJ8j9HRvmL-R1hFIaThPmBtL6sn5_poSafI9cUtkdhGiwg2i4htTBHw1cXQMaEUYhI1tm4ulOFQwWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YPFe7F4gbOJ6jxMIqGS86CCFz1PnO_od6YGm13mh-CphvCKaoBEEIRrfUJF4rpsHuaL46dCDsz_kInFV8CdnAh8CXTci9R4h4Hvb6OaLV_9MMIg6fZt5RtYeiM4FMVkH8_M70_AAhQh0wJcuIQiY7wrnMbRbnxeUktrowgoWW__2cottfhH6zOZ9Ev0oUJnEWdA_XYRKtbjmDzi3wuuUhUxKe99eH2j6gR0NW6Q-DYvYC5ihcI5b8OLwMt3Vy2tB9yLNWuOJyJvYIUXA4Df6LOMmxSqxGXPjhvzr_KRl79635QXg2C78ZPOCrdw1vJJpGeDko7MzkMHnFCdO1b3P4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oo0rxAqCm2NYuDDt-TohRSVbzw-2ssTE3kC4hhr_dEdUdveBImJX3eLHx0KE6LuaWhZFhOgHBqMsZP2lRvwxXws8xhpe7Qpl-nrQh42MBpV8FoK08IvioiHZdzL5EcOGsjOz1f58VLTMroPs3zUXdaP6laV56ynbsR_vGHNM5Vs6Hgq7ZzvJH0JoHY0OB3COl2Z56Dg5uSP4X1jkXcZSaVFs8X2uN8b5rnC4jFXoFIdyCwjTWm0Pcn7lTPzqK6gN1ZBvhrlycqZszPF385u-_wqaSjv1Q4DBs-fZrCesLOX-Z7MikDvaGKT7llzr34Tw-kJOebNM4-1iZ5988U-Dsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشن برداشت انگور در دامنۀ زاگرس
🔹
براساس اعلام جهاد کشاورزی، امسال پیش‌بینی می‌شود ۵۴ هزار تن انگور از تاکستان‌های چهارمحال‌وبختیاری برداشت شود که شهرستان کیار با حدود ۲۷ هزار تن تولید سالانه، سهم قابل‌توجهی از این محصول را به خود اختصاص داده.
عکس:
عاطفه گنجی
@Farsna</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/farsna/465445" target="_blank">📅 11:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465444">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc3624d64f.mp4?token=HBaQyFqiFan8Ub_Wy_v6bOeyAIaEapF0VZymxNlfcNjsqVOe96uHPjAELdrHaBJZJQmXGk045uJ7qsP5Jovz_BtC0DNcjI5n6Z8isFagokqoDorfmoo1vsKca0rQkZRFxdOLs2M6-2kBLq3jfx0p-pvp-6JqjlviFYw1VSPxiiWP3OIzInh3OjNY9lgdqeewGpQTjbdc4izIkjY9UW1HCDcJgm079ipQnN_EN0GE1vViD0I_GCJpZVIR2xiivOjQeR9Xy8IGrmPvajeesF3ywmO4PvMHCzdaReQ3_JU8_p7ZmA8esdLTah8BSF0KhfA0qJ-noY8lH2VOAzLntt2XTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc3624d64f.mp4?token=HBaQyFqiFan8Ub_Wy_v6bOeyAIaEapF0VZymxNlfcNjsqVOe96uHPjAELdrHaBJZJQmXGk045uJ7qsP5Jovz_BtC0DNcjI5n6Z8isFagokqoDorfmoo1vsKca0rQkZRFxdOLs2M6-2kBLq3jfx0p-pvp-6JqjlviFYw1VSPxiiWP3OIzInh3OjNY9lgdqeewGpQTjbdc4izIkjY9UW1HCDcJgm079ipQnN_EN0GE1vViD0I_GCJpZVIR2xiivOjQeR9Xy8IGrmPvajeesF3ywmO4PvMHCzdaReQ3_JU8_p7ZmA8esdLTah8BSF0KhfA0qJ-noY8lH2VOAzLntt2XTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آقامحمدی: «گروه‌های مسلح آموزش‌دیده در امارات و اسرائیل» وارد کشور شده‌اند، مردم در محلات مراقب باشند و تحرکات مشکوک را به شماره‌های ۱۱۳ و ۱۱۴ گزارش دهند
🔹
عضو مجمع تشخیص مصلحت نظام: جریاناتی در محلات استقرار پیدا کرده‌اند تا عملیات‌های ترور انجام دهند.
🔹
آمدن نتانیاهو به امارات را جدی بگیریم. طرح نتانیاهو این است که به‌جای اسرائیل از امارات بجنگد.
@Farsna</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/465444" target="_blank">📅 10:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465443">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HW7dxSzC_r-ZFu-iSIx3kSs5XyLyTRler_XOnZQvAORKCB_9hUGZjjHTO2UHHxE1_vNfHeVx7I__ue62ItGSDuF5ZIChtLDDE9iGh1zEMdipOIhuIKfRl-XtYm8lKhvuU5YMDku-bq5-ArUlrgr8bMvWayKxoxI2PVdUAUzvc9rmwWMPXCOVtQ2u9zc9AZ1h_dgCqVukoKzNrz3h--WX7g64kxBOSqgvt5fv2EPDahlp6oKPWvqWWMY515aagQkK1o4WdZL8E9xue-nVe04YLHtt_PpSicqkYTKoFmh-FCmjrbivNXpT4cpjzwr-KNnZ86azNIao1at4DWd0ot7p1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر اقتصاد: دلیل جهش آمار واردات خودروهای لوکس، تخلیۀ اضطراری انبارها در شرایط جنگی است
🔹
به‌دلیل شرایط جنگی کالاهایی که ترخیص آن‌ها ماه‌ها زمان می‌برد، ناگهان ترخیص شدند و آمار افزایش یافت. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/465443" target="_blank">📅 10:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465442">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYGkcFM9B-ckDgs8HtgnF-1QHgDCy9R-W5nC-X-yD3gjB7Kh_kuI_QFdrYZ2FTPu1Am8watg6Ob0PegIIKnis0nze64VmbtVbq64LPGlrKK84vEM59IaZh6wFHBdrVy7UX0qlosuUQTR1jc4U0-j9Bb2R_6CItoXP_Hl-v5aGAJo6_RS7mSoGhCkqQBjqGfqFxl1QKlc46oL3MJnx3LrhuGTjKdQO5HVLpUbm7SraBaX1_Op-FvHSxv1v88EyU_yo3sg2j6Mp3EATCHBwspZDUHG5CnDp0qN4KK2dpR6KNxQZH1bJLG9mY59YcYSisF0NSLWsRE7aecpnCYwRFnLkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت دفاع: ایران از وابستگی به توانمندی بومی رسیده
🔹
پیش‌از انقلاب، ایران در بسیاری از حوزه‌ها وابستگی جدی به خارج داشت، اما پس از ۴۸ سال مواجهه با تحریم‌ها و فشارهای خارجی، در حوزه‌های مختلف توانسته روی پای خود بایستد.
🔹
امروز بیش از هزار نوع محصول و خدمت بومی در کشور تولید می‌شود و بخشی از این محصولات و فناوری‌ها نیز قابلیت صادرات پیدا کرده‌اند.
🔹
این دستاوردها حاصل سرمایه‌گذاری بر نیروی انسانی، دانش، تجربه و ارادۀ ملی است و نشان می‌دهد تحریم و فشار خارجی نتوانسته مسیر پیشرفت علمی و فناورانۀ کشور را متوقف کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/465442" target="_blank">📅 10:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465441">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🎥
چطور پهلوی را در ذهن دهه‌هشتادی‌ها سفیدشویی کرده‌اند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/465441" target="_blank">📅 10:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465440">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJyjSCTyhOhE2c4DFqlJJcChZZfig4qB6vPbVvad4xj2NrbksDw3RMCG_JsuY4r88IjVB5bQEquIpU7TzkmV2bQPMuiR0uhfUE6UP4UVMjhK5aW72demi2FSlbWNEccpjyMlvYvTzqWcyZDSScyO08WlzTNGKPlvYkW8BNL11EMCrF88UzKElbx7c45YmeaUi36TbPZh-HRWblJMkAaS0fw8isgPHFZHJKUsd_caigtDPrTG2-PQ1gXMh2Gk-PDiwTS8qIj7N-cQmgAPoLYdTkzDoAsKLEAG9aojvsOITZuBz-xCOiXw1zDS31JR2qo1Kbe_v4JcBEb3Tu4Dqahh2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دعوای دو خلبان پرواز امارات به اسرائیل را نیمه‌تمام گذاشت!
🔹
رسانه‌های صهیونیستی گزارش کردند که پرواز امارات به‌مقصد تل‌آویو در میانهٔ مسیر کد اضطراری ارسال کرده و در فرودگاه تبوک عربستان به‌زمین نشسته است.
🔹
به‌ادعای کانال ۱۲ رژیم صهیونیستی، علت این حادثه «درگیری بین خلبان‌ها در کابین» بوده است!
@Farsna</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/465440" target="_blank">📅 10:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465438">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2hwd6dsq-XxM9sPF2LkTaJ76nAXHGFY8l7AGCjUJTbDGfgom0x7oSYcbGV-gJdgiRjgFUyFXtNkEos-qdNu17Ctf9p0IKjywWxSVRccowoM5JlEeJW3JYgji-AIyYKwrOOviwEQ-DrLz9EvmmnHBEoCQ424Z_KdqyGzoxXYNIZ0OA8kTOua1vN-83I4SiUf5XCS0ipsxIsv0vykcngWgNPWBmu-C8--9caMziUoD6yI9EzGhBOBLoD2Q9O9AJZWBzp3sKqv0sG7KagIyMSn0VnQRVYifkYiCcZYsqSBWKXy_5-TXfBURiwti_1Id_CjO_SZKNxTzGRN0inj_oTVsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرضهٔ ۲ میلیارد دلار اسکناس به بازار ارز
🔹
بانک مرکزی: عرضهٔ ۲ میلیارد دلار اسکناس برنامه‌ریزی شده که فروش یک میلیارد دلار آن از امروز از طریق شعب منتخب بانک‌ها و صرافی‌های بانکی آغاز می‌شود.
🔹
تمامی افراد بالای ۱۸ سال می‌توانند با ارائهٔ کارت ملی، تا سقف ۱۰ هزار دلار ارز خریداری کنند.
@Farsna</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/465438" target="_blank">📅 10:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465437">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7Ppjb3C03Vsq1BQqOK1_Rw7l7j8OkoK3Yl_CPlXe3Xb8I-qwwbXpcBZU3kmOQo1PsUnRol5H4w-HiUiyeYe1spC6ceJgp6QZNa1N2lZ6xXcSnpIo9FTr1tk-5wrw-t0l-0p_7omf2z86ZcTCqg5SAouD-wxwITNQMHPV6Kk286zmYUrwC59qI2qBEflpl8H9TFAZG51_ZwCYNNyb2-UKluGTMxoMG6WfBbRQx6Rxy_aSa60QUvHI2R2SdV98KJ-Jha4zTcUcGzbiN3truuyLUIYJy2H14ir1_OSaCoXVnTHC4Hrnq9H2HqiVrQDWp8aiafDJ7h8_5PtpQQ_53tOBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۶۰۰ کیلوگرم مخدر در آذربایجان‌غربی
🔹
فرمانده انتظامی آذربایجان‌غربی: در طرحی ۴ روزه، ۷ قاچاقچی مخدر دستگیر، ۶۱۶ کیلوگرم مواد مخدر و بیش‌از ۷ هزار قرص غیرمجاز کشف و همچنین ۱۵ خودرو توقیف شدند.
🔹
همچنین ۱۵۶ خرده‌فروش و ۲۸۶ معتاد متجاهر دستگیر و تحویل مراکز درمانی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/465437" target="_blank">📅 09:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465436">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2Qt1RAAS78nf8NPwrs4EU7ZYBh7kP7fI3n5N8SjhLWcemI_McJDpuVQ3ZZX4NsgiNCQd4Igf06wPsqsOGR9ADMumBO-jX2zjcz9gLka3dHzLw7BqdUaSxAy3AbTh7opATc0WJj-KbjDNLCIZfMbN5sJpyK4Yj3WkOI_TxSLKJ5G1gkwzOhZksHATREEsd72Uf9RKb67htZcF46ixYNb3_EBPRSmcC5vqOc4iPJxxRArtTMCPy57Yq695icq-oRqsRraisU1-rBQNJ8TxdAgOQ11xqE6Fo8SBA0b511MKxsQyojWlMRo4WF8u4VdUSGSoDzUbZQaWpTk5sUxQpVHkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردشکنی صبحانهٔ بورس
🔹
شاخص کل بورس در آغاز معاملات امروز با جهش ۲ درصدی به ۷ میلیون و ۷۴۶ هزار واحد رسید و رکورد تاریخی تازه‌ای را ثبت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/465436" target="_blank">📅 09:51 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465435">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/617adbbdfc.mp4?token=AjmBhtRgyA75aydlclR99T24bg79vrTGwTvaba7Nr7DpdqF9uWd8nKglmx1w2gctg4bRTPiBYJ2P_3Xz6tYKw662cM7EuvdsF82ZLaqk5V03DBAwvTsMS4patUnFXvT70dZfqXziFJyAOWLmY8JvYLHhK_VK-kMjnuKS-C8qYg1_7Ipdokc1pZvY9ItNSTa6UllSAgr6b0LP9Tl9oR6NAAQEM3YHyC-dpP1EAHSQs46oWR76cr2NMBtW6KRC2lTacghk3z6pRzQhmyNDtniz2D2LGGhQa9n7ra7u0dXije7aQ6NRip8CwH7sGT4tv-3RcMCs06BLw2rHHAM1kGcrwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/617adbbdfc.mp4?token=AjmBhtRgyA75aydlclR99T24bg79vrTGwTvaba7Nr7DpdqF9uWd8nKglmx1w2gctg4bRTPiBYJ2P_3Xz6tYKw662cM7EuvdsF82ZLaqk5V03DBAwvTsMS4patUnFXvT70dZfqXziFJyAOWLmY8JvYLHhK_VK-kMjnuKS-C8qYg1_7Ipdokc1pZvY9ItNSTa6UllSAgr6b0LP9Tl9oR6NAAQEM3YHyC-dpP1EAHSQs46oWR76cr2NMBtW6KRC2lTacghk3z6pRzQhmyNDtniz2D2LGGhQa9n7ra7u0dXije7aQ6NRip8CwH7sGT4tv-3RcMCs06BLw2rHHAM1kGcrwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای ساخت شهرهای موشکی به‌روایت مشاور فرمانده هوافضای سپاه  @Farsna</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/465435" target="_blank">📅 09:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465434">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba522c47ba.mp4?token=dNIQx7wqOfI9eL1TeRMK4KSZ-8qyDmDJecXmBpY2s7-FjQ_HERPuZR-9Ne__zo_kkwf5Vzu0EkVOO1WU-MBZiEwmZHPGJv_M6Tiz0NpDrr-rtRA-NumkIChRkz1T5CWB-85WONkbzR_pmxVT7aV56W28P2JUPuNu4GFrsWbxSDYcNM9lAEllBkzt7gnkVQl_VNLS1bO8InIS1R8Z6hPYJVn-eLwJxj969ZD1_6VK3tocBW1axMw6vDoLlDIvyLL-E12Gq2NiUUSxTxbIv3af5lcVOqkCLZ9BKaeKgu0QIRiDyTgCH913pM3oWz312oJFj-1TawfXVgrmT-u8rrwUtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba522c47ba.mp4?token=dNIQx7wqOfI9eL1TeRMK4KSZ-8qyDmDJecXmBpY2s7-FjQ_HERPuZR-9Ne__zo_kkwf5Vzu0EkVOO1WU-MBZiEwmZHPGJv_M6Tiz0NpDrr-rtRA-NumkIChRkz1T5CWB-85WONkbzR_pmxVT7aV56W28P2JUPuNu4GFrsWbxSDYcNM9lAEllBkzt7gnkVQl_VNLS1bO8InIS1R8Z6hPYJVn-eLwJxj969ZD1_6VK3tocBW1axMw6vDoLlDIvyLL-E12Gq2NiUUSxTxbIv3af5lcVOqkCLZ9BKaeKgu0QIRiDyTgCH913pM3oWz312oJFj-1TawfXVgrmT-u8rrwUtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعدام ۲ عامل شهادت نیروهای امنیتی در مشهد
🔹
علی همتی و مجید نیک‌اندیش، از عوامل میدانی اغتشاشات ۱۸ دی‌ماه ۱۴۰۴ در منطقه طبرسی مشهد که به شهادت ۴ نفر از نیروهای حافظ امنیت منجر شد، پس از تأیید حکم در دیوان عالی کشور و طی روال قانونی، بامداد امروز اعدام شدند.…</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/465434" target="_blank">📅 09:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465433">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6599761a6d.mp4?token=hYL8msnNBD0fIM9fGsZHe2SqSv-IK893oRp998TY-zIyH-1N5F1E_jheN3ggboT6qVOr9Wfef89quVNQybBp0lSlQ0rseNGWeerWGEd7txcZ6JbdVR0zuEGo7GVskuCx69XeXW2GdcMgVmIY_rKm52p-9ien3gXe9uOnkmvSG-JBTzQUKVM5BlQ_XqwAfzGm0MMiP1XYfyG1Wv7bjnNmdpNVnUnmoeWGvWJLQ2hD8DD924Gh-S9Zlapgh2urxV5WOxBw_w8oyWJ5KcjZPca9atbAQb3yOF22x-MPdxNGvMF4G33GDqVMBb15grpV7EiwzrfIFI1BD5KjmioTi0a6qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6599761a6d.mp4?token=hYL8msnNBD0fIM9fGsZHe2SqSv-IK893oRp998TY-zIyH-1N5F1E_jheN3ggboT6qVOr9Wfef89quVNQybBp0lSlQ0rseNGWeerWGEd7txcZ6JbdVR0zuEGo7GVskuCx69XeXW2GdcMgVmIY_rKm52p-9ien3gXe9uOnkmvSG-JBTzQUKVM5BlQ_XqwAfzGm0MMiP1XYfyG1Wv7bjnNmdpNVnUnmoeWGvWJLQ2hD8DD924Gh-S9Zlapgh2urxV5WOxBw_w8oyWJ5KcjZPca9atbAQb3yOF22x-MPdxNGvMF4G33GDqVMBb15grpV7EiwzrfIFI1BD5KjmioTi0a6qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منظور: امسال ۲۵۰۰ همت کسری بودجه پنهان داریم
🔹
رئیس سابق سازمان برنامه‌وبودجه: از حدود ۶۰۰۰ همت منابع پیش‌بینی‌شده در بودجۀ امسال، حداقل ۲۵۰۰ همت کسری وجود دارد و برآورد می‌شود ۳۵ تا ۴۰ درصد منابع بودجه محقق نشود.
🔹
برای بودجه حدود ۱۰۰۰ همت اوراق پیش‌بینی…</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/465433" target="_blank">📅 09:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465432">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOOTvqJ1nHdnQI179-ys5qpbIvRerRgVq4WRshbH0hDnM6C77XbUfSTg-h3tl9VEBaKf5UlgXrxtJBw2v5ylukWEs0Y0t0uRqa9a4BUDJN-8BDoQe5oZrWSy3FNoWpdnqQu6w37IFPvE7gtYSyQD8fBzSfNRDc_yrHgoCK9Cp2Yk59KU3pUvNMF2rheDT_4AYqMaws9p0c7pLmc6jmeJZMOybDL65noD-X5JDsMEjElx_RcoWgJgq8S3CFKuXzkfANVMFBqmtdrgE11Hj6UiV_6AH2vbXVnA2IBg9-OmRs-jcy-z4n34qU3Gx9Q1z8t6OiRXCnysMNHwFtR7KS3xsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نبض حساس اینترنت در عمق هرمز
!
🔹
کابل‌های زیردریایی، بخش اصلی انتقال داده میان قاره‌ها هستند و بخش بزرگی از ترافیک بین‌المللی اینترنت از همین مسیرها عبور می‌کند.
🔹
آسیب به یک کابل فقط به معنای قطع یک مسیر ارتباطی نیست؛ تعمیر آن می‌تواند هفته‌ها زمان ببرد و میلیون‌ها دلار هزینه داشته باشد.
🔹
در منطقه‌ای مانند هرمز، محدودیت تعداد کشتی‌های تعمیراتی و شرایط امنیتی می‌تواند روند بازگرداندن کابل به مدار را پیچیده‌تر و طولانی‌تر کند.
🔹
همین وابستگی باعث شده کابل‌های زیردریایی از یک زیرساخت ارتباطی ساده به بخشی از زیرساخت راهبردی اینترنت جهان تبدیل شوند.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/465432" target="_blank">📅 08:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465431">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7ejGby8qnxVArRXPWyZNKWui0E61PZe6FT0JR66OUFOMFQCxocrTOFaup3CXPJ9VhBinffGpJyJfKTfupVhChvAeN4h_PLFgEl8zcFnc4xs-BZCHnaVbkfJ2WufV-BZLglgepAi1zutOFba5KN9T2uUtCdCXvgMAId4ors0Cmt1RYk0R4OvwANqn27n4S-g8fw1fOvsE6iCMIUMcD17UdDcGlaHkfEkqhGLH19-tTCH90rMHSdg_71FtPkDmGMgHv8r-ZKxzerC0ezl1qAoXBSP6gZH4kGUtjFIRUnG6vYJr--MFHilYs5p5TBYTb0ibkjYSwUk3ecIF5ACnPGT6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ برای پایین‌آوردن قیمت نفت باز هم دست به ذخایر برد!
🔹
قیمت نفت برنت بامداد امروز به کمتر از ۹۷ دلار ریزش کرد. این ریزش پس‌از آن اتفاق افتاد که آمریکا اعلام کرد ۴۰ میلیون بشکهٔ دیگر از ذخایر راهبردی نفت خود را آزاد خواهد کرد.
🔹
پیش‌تر اعلام‌شده بود که ذخایر راهبردی آمریکا از ۲۸۴ میلیون بشکه کمتر شده؛ این رقم در ذخایر تنها وقتی ثبت شده که ذخایر آمریکا برای اولین‌بار در حال پرشدن بود و چنین رقمی هیچ سابقهٔ دیگری در تاریخ ندارد.
🔹
کارشناسان اقتصادی این اقدام را «انتحار» خواندند؛ چون میزان ذخایر ممکن است از توان عملیاتی رهاسازی کمتر بشود و زیرساخت ذخیرهٔ نفت آمریکا آسیب ببیند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/465431" target="_blank">📅 08:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465430">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/098d751445.mp4?token=YK89CkNpEMye7LTSMR62D3kJmNEidpHHLmEyFODqKAhikOmsrW3xjwfPs7x-XTz0iK5V2byc6_GpDNHhUcmHvNMt8MWT6icp5bIRX34ogaAC6dq7sh3SGcGJoNO6jC20UvlN9VqBtRXp8z9F8bv-u3WL0KtTrkTkhxotqHwN3_7LwzCwmR6k16FbMYP_drsh3n06MyD_SY9pXDlvhiA8e7JIAUghKnvDtPBNBAFj2AgVoUywy8e3wb1-z-9dTlU7DoUSnHaJ93uGlSWJJi-_Wdz5J4L0WGkl-U5be6qpweOU4peSFZYSlLxtxhnzFe4CaTWNk_jUhTLr-kR8ccDDnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/098d751445.mp4?token=YK89CkNpEMye7LTSMR62D3kJmNEidpHHLmEyFODqKAhikOmsrW3xjwfPs7x-XTz0iK5V2byc6_GpDNHhUcmHvNMt8MWT6icp5bIRX34ogaAC6dq7sh3SGcGJoNO6jC20UvlN9VqBtRXp8z9F8bv-u3WL0KtTrkTkhxotqHwN3_7LwzCwmR6k16FbMYP_drsh3n06MyD_SY9pXDlvhiA8e7JIAUghKnvDtPBNBAFj2AgVoUywy8e3wb1-z-9dTlU7DoUSnHaJ93uGlSWJJi-_Wdz5J4L0WGkl-U5be6qpweOU4peSFZYSlLxtxhnzFe4CaTWNk_jUhTLr-kR8ccDDnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: بارش باران در شمال کشور ادامه دارد
🔹
طی ۵ روز آینده در جنوب‌شرق کشور بارش پراکنده داریم.
@Farsna</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/465430" target="_blank">📅 08:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465429">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gA4pMCQljynDVo5c5l-Xo6lzt1qFs99te-qlAc5bv4QJTlpQQa79D2qBQSgzCXiyVjZqbFHrfV_q2xS8YIkNZ_zqaKrHu-la8t8Sgv1xsckSCLXkZdYvWo6lrNE1ayXejb-HFZpzlr1o61yqbXLfPzHu-m0M19_8k6n0ZP5fbccAE-wHHtPHM8wRRdzK7rMTcY5VNw9FBUhIJei3b7APDGAK-jxOn1ArwDS98Q62-jwF8xySrt9ra9YIoi1yLTS9mI3GjAzQZqo3HfS4J0fdSdk6UwAImURQiosLy7az66rNXYrJkCurSptYJqDAeNQMYNQC9zywfqUjHclYm8pc3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیاده‌نظام بسنت، کف بازار دلار ایران
🔹
درحالی‌که نرخ دلار در بازار غیررسمی حدود ۲۳۳ هزار تومان بود، امروز قیمت دلار در کانال‌های غیررسمی به محدوده ۲۴۲ هزار تومان رسید.
🔹
این افزایش قیمت یک روز پس از تهدید اقتصادی وزیر خزانه‌داری آمریکا رخ داده؛ همزمان، فعالیت…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/465429" target="_blank">📅 07:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465427">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZO5vPkaT5SV9dq8TBBoTK5TFJmbU4VwWK3Xuh7omNeg1Mr1Bje8l85nseuVMv-s5VXORa_qbvyS02dX_b1ksIHRe1AF70ywbQqTaFIIXJ6eGNot9bd091l4-w4sVkw47XHEhOU8cvTXK_oJj-X6xlVVuhLUU4DAjR_7cwM2_I0i1lC8ylVbndCCRNtVAat8u8gkZBGGl17dlh4NGQXt9tp7_oEvxVck87pFFfwgK9W8XgGnKe8B62CcWThOrgxb1FLDhMHOWkCy6xY4CX4GqiziR4I_bWY7bySnrEsDRFWlG8gw8vi4zTSk-dcUOcfZ3O_hR4IffZr9QZc6pu0KZyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعدام ۲ عامل شهادت نیروهای امنیتی در مشهد
🔹
علی همتی و مجید نیک‌اندیش، از عوامل میدانی اغتشاشات ۱۸ دی‌ماه ۱۴۰۴ در منطقه طبرسی مشهد که به شهادت ۴ نفر از نیروهای حافظ امنیت منجر شد، پس از تأیید حکم در دیوان عالی کشور و طی روال قانونی، بامداد امروز اعدام شدند.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/465427" target="_blank">📅 07:48 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465426">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOXChPFMpjllbZ-eQ7lNYskYMWBUEp5P8YG_AhJfv4_lRvI443eRviuf45e8D6wCfe1tjqkHOZTaM1JW9ZsCYYJLFici1_UIo7-2XuGAHQkF63HXTzz2FOxei1PoLPXXir8KrfnGSqnk7vp5ouhat6NSn3eYHWxykKTD2kwMIEaTMytXsrFfvX0bKbKCvVVGVQ8rSqsz5aUGPF0yD6JPufdBmbwy7QIkOg6JqCM9z113nWETkNbvEgO3iHy83whVOdVERk_EABqtavuVl9cijd5pv_B4n8K5WryJL-xk8ZUztPam5ESUzoWKmIlanO_1YzelJ9DEJuT9uGFpSOGZGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت نامشخص مدافع پرسپولیس برای بازی با نفت
🔹
دانیال ایری، مدافع جوان پرسپولیس که به‌همراه تیم ملی امید در مسابقات آسیایی ناگویا حضور داشت، پس از بازگشت به ایران به‌دلیل مصدومیت در تمرینات اخیر سرخپوشان غایب بوده و وضعیت او برای دیدار پیش‌روی این تیم مقابل نفت آبادان مشخص نیست.
🔹
با این‌حال کادر پزشکی پرسپولیس در تلاش است تا این بازیکن را به شرایط حضور در مسابقه برساند. قرار است وضعیت نهایی ایری طی یکی دو روز آینده مشخص شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/465426" target="_blank">📅 07:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465425">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔹
فردا او و محمد بیرانوند در تراپ میکس رقابت می‌کنند.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/465425" target="_blank">📅 07:30 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465424">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5673b02594.mp4?token=HHEK6_SlEbXR7qnqm0xDjyG8PbTE9kd6uXpzWpLnBDCx5urFI6cPcoFnEBMrHcNtfbMNP-kzcgWG9R9uFphnuRxzi3M0f4EvLu9M6UiUCP6_FnywLsOUjDMgYkwgBwr4n8eRxycuHYOcHPF6E50puCCnG2PJ6QBqC5qPh7XO_1tmUo_ZtmB6hlRmw4HmltqQgJiB_OuCbQVmRaAWfGkJe7vLZldVWFzpg_Ztp2OumKVodkgUNkKEjMSMhoXjx-HD_GkKkw9GZok-g2P00y9BsXXuwQVxTkbOxEFdQ0_ZxYWQQrRRtU-3sabKc9R6CKWQDhsXxVxb-fuwTwZzvtJCfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5673b02594.mp4?token=HHEK6_SlEbXR7qnqm0xDjyG8PbTE9kd6uXpzWpLnBDCx5urFI6cPcoFnEBMrHcNtfbMNP-kzcgWG9R9uFphnuRxzi3M0f4EvLu9M6UiUCP6_FnywLsOUjDMgYkwgBwr4n8eRxycuHYOcHPF6E50puCCnG2PJ6QBqC5qPh7XO_1tmUo_ZtmB6hlRmw4HmltqQgJiB_OuCbQVmRaAWfGkJe7vLZldVWFzpg_Ztp2OumKVodkgUNkKEjMSMhoXjx-HD_GkKkw9GZok-g2P00y9BsXXuwQVxTkbOxEFdQ0_ZxYWQQrRRtU-3sabKc9R6CKWQDhsXxVxb-fuwTwZzvtJCfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کشف ۵۲ کیلوگرم شیشه در گنبدکاووس
🔹
جانشین فرماندۀ انتظامی استان گلستان از دستگیری یکی از قاچاقچیان مواد مخدر، و کشف ۵۲ کیلوگرم شیشه خبر داد‌.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/465424" target="_blank">📅 07:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465423">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">صعود بانوان پدلیست به یک‌چهارم
🔹
صبا نجفی‌دهقلی و ندا محمدتقی‌پور از ایران در دور دوم مسابقات بخش دو نفرۀ بانوان به مصاف حریفان‌شان از مالزی رفتند و با نتیجۀ ۲ بر یک به پیروزی رسیدند.
@Farsna</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/465423" target="_blank">📅 07:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465422">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15641850b5.mp4?token=vhhV6tmOuuDBCHe69HRY_vVGhnPobRdpO95gkND4NMRHFaq2ygj66ydpu3iTWoQ1yeZuPCg321bTjhFP9w1XTIrOThy0OophtZQz9UtIoy0vnBaykXtE3b8meFOPhxdVrPkO0wKkVac5m8cAI6Eu1zKC_IBConfrFQBTq79lcRhfks_jCuM0Tno4bKfhb85g1K3MTVRdE3eH3cq3_ybTP9E2TUfzUmoKQujlGDqlB4ee7yHRkL6ADL6_Reg__0illFYAydI4W0MQs3WXFGDpanc7QoTs6ib8tJCARgGt4gMIlBn0LRNY8Sw8xN7s3FLrJJyMY-eOo9Au0X7ebBqdq4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15641850b5.mp4?token=vhhV6tmOuuDBCHe69HRY_vVGhnPobRdpO95gkND4NMRHFaq2ygj66ydpu3iTWoQ1yeZuPCg321bTjhFP9w1XTIrOThy0OophtZQz9UtIoy0vnBaykXtE3b8meFOPhxdVrPkO0wKkVac5m8cAI6Eu1zKC_IBConfrFQBTq79lcRhfks_jCuM0Tno4bKfhb85g1K3MTVRdE3eH3cq3_ybTP9E2TUfzUmoKQujlGDqlB4ee7yHRkL6ADL6_Reg__0illFYAydI4W0MQs3WXFGDpanc7QoTs6ib8tJCARgGt4gMIlBn0LRNY8Sw8xN7s3FLrJJyMY-eOo9Au0X7ebBqdq4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی‌های آسیایی ناگویا
میرزازاده اولین کشتی‌گیر فینالیست شد
امین میرزازاده در نیمه‌نهایی وزن ۱۳۰ کیلوگرم کشتی فرنگی با نتیجه ۱-۱ مقابل منگ از چین به پیروزی رسید و فینالیست شد.
@Sportfars</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/465422" target="_blank">📅 07:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465421">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKRkBzW9gH05XooY1C3uXbht_lzLf46yfA75WJJYE_5ql2TAHc2mF9wHr-eQWf3OKXP9srR0-JNcD8tok7qhWPV6c64Jf3rBnRdfpu4LYiZPYefbFYBBigm9Az-aufTJaf3f761UVCEiuFSjdfuHRR62n4HZrxSir3MT7qCwKCnTizlEWkN6p369O54s_8rDDJz0a98fhXGYQA6WdWZBKcXO5U4_cAdHk4V2P-CyaIlNnyW9CoKLvyYq2Fxt0l2qh1YnFHUC3PH6Jf1nRpRfNLT2MOjofPC0NGxC4n3oZQxTlJCYB40FXDLcYy8gucLImdjVUrGq36nOOIip5EFALg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرط جدید خرید کارت مترو: ثبت کدملی و تأیید شمارۀ همراه مسافر
🔹
شرکت بهره‌برداری متروی تهران و حومه: شهروندان پس از ثبت کد ملی مسافر در سامانۀ فروش، کد تأیید را روی تلفن همراه دریافت می‌کنند و پس از تأیید نهایی، کارت به نام فرد صادر و شخصی‌سازی می‌شود.
🔹
کارت‌های جدید از زمان خرید به اطلاعات مالک متصل خواهند بود و خرید بدون ثبت اطلاعات امکان‌پذیر نیست.
🔸
دارندگان کارت‌های قبلی نیز نیازی به خرید کارت جدید ندارند و می‌توانند کارت خود را از طریق اپلیکیشن «شهرزاد» یا باجه‌های منتخب، رایگان به کد ملی و شماره همراه خود متصل و شخصی‌سازی کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/465421" target="_blank">📅 07:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465420">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تیم دونفرۀ تنیس زنان حذف شد
🔹
ماندگار فرزامی و مشکات‌الزهرا صفی در رقابت‌های دونفرۀ تنیس زنان، مقابل نمایندگان ژاپن هر دو دور را با نتیجۀ ۶ بر صفر واگذار کردند.
@Farsna</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/465420" target="_blank">📅 07:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465419">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نمایندۀ ایران از صعود به فینال سنگ‌نوردی بازماند
🔹
در دور مقدماتی مادۀ بولدرینگ بانوان ۱۴ نفر به رقابت پرداختند که سارینا غفاری نمایندۀ ایران با ثبت امتیاز ۶۹.۲ در پایان تلاش خود روی چهار دیواره در جایگاه نهم قرار گرفت و از صعود به فینال بازماند.
@Farsna</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/465419" target="_blank">📅 06:51 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465418">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">هشدار روسیه به ناتو دربارۀ احتمال درگیری مستقیم
🔹
سفارت مسکو در بروکسل شامگاه دوشنبه هشدار داد که هرگونه اقدام کشورهای عضو ناتو برای محاصرۀ منطقۀ «کالینینگراد»، خطر درگیری مستقیم با روسیه را در پی دارد.  @FarsNewsInt - Link</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/465418" target="_blank">📅 06:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465417">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8NgK7m5w5s6XlVze3Wx1FvWIt8gYGpDk0hVsfWuuFwlRpl_30JDUzVLeFHeLDVO4ZUqHmRrwTOIWB9GgTjSgI5daFO31mGcUICjbCrdP7pEHHYLJoMbwT6koKqLXgNWmVw47YE-zHffTXypA0z_XF9NapQUg3EDoMgtVTNPwmteDK2i6b3X9X1sW4KJjcGSTyy-xhGAuz6zVCoUQN_OooxGMOQvFnZhatBpxsgVhGPvCLteaM94HDdMg-YP-xihIhInJ-Cik2ZfisWH8IofAs9lbxuuY91-9oB4B9fTNGCMIZGbLL7REeYCU9V3zwOdh6MjgTYTRCdImhhzR-5IVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتی فرنگی‌کار ایران طلسم برد امروز را شکست
🔹
امین میرزازاده پس از استراحت در دور اول، در دور دوم وزن ۱۳۰ کیلوگرم کشتی فرنگی با نتیجۀ ۷ بر صفر مقابل حریف قزاقستانی به پیروزی رسید و راهی دور بعد شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/465417" target="_blank">📅 06:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465416">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">زیر میزی گرفتن پزشکان را گزارش کنید
🔹
مرکز نظارت بر درمان وزارت بهداشت: هموطنان موارد درخواست زیرمیزی و مستندات خود را از طریق سامانۀ تلفنی ۱۹۰ یا مراجعۀ حضوری به ادارات نظارت بر درمان دانشگاه‌های علوم پزشکی گزارش کنند.
🔸
جریمۀ ۲ تا ۵۰ برابری مبلغ زیرمیزی در انتظار پزشکان متخلف است‌.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/465416" target="_blank">📅 06:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465415">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">جودو هم با باخت شروع کرد
🔹
مهسا شکیبایی، بانوی جودوکار کشورمان با شکست برابر حریف تاجیکستانی از دور مسابقات باز‌ی‌های آسیایی ناگویا کنار رفت. @Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/465415" target="_blank">📅 06:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465414">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">جودو هم با باخت شروع کرد
🔹
مهسا شکیبایی، بانوی جودوکار کشورمان با شکست برابر حریف تاجیکستانی از دور مسابقات باز‌ی‌های آسیایی ناگویا کنار رفت.
@Farsna</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/465414" target="_blank">📅 06:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465413">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت دفاع عراق: اکنون دیگر هیچ نیروی نظامی از ائتلاف بین‌المللی در خاک عراق حضور ندارد. @Farsna</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/465413" target="_blank">📅 06:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465412">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b89978570f.mp4?token=FZLZB1cAdZDlqryjd5wrnHCpwHm2U0uUp3CS47JYsmQCHLpwPIL5-iQ7EXmwd9zSpEUWG_FxD5phB3kNRA_M1uBQA40D6f8bu0kqoSINCKS0ifk6531GFlL0zxls-reJOAIJK_8bmgNALoOn5wIkSTETfCccG5x1fyRYqKMyxfW0u1OcTZEfOPw29rS6MBM0fWOY73tWZqJXk8ChAndix5DCszjJZ5zLmlI3ovfS_1q8XXHPZ_rrW5e-_7ViZ8Ma7ejBrStQECJDo4OIUvbuh7qKRDvBT4xUU-Zr48BsdxBzi1SFOL8cuS-IpdrNfovW4eklupzeggdtJO9hGoLojw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b89978570f.mp4?token=FZLZB1cAdZDlqryjd5wrnHCpwHm2U0uUp3CS47JYsmQCHLpwPIL5-iQ7EXmwd9zSpEUWG_FxD5phB3kNRA_M1uBQA40D6f8bu0kqoSINCKS0ifk6531GFlL0zxls-reJOAIJK_8bmgNALoOn5wIkSTETfCccG5x1fyRYqKMyxfW0u1OcTZEfOPw29rS6MBM0fWOY73tWZqJXk8ChAndix5DCszjJZ5zLmlI3ovfS_1q8XXHPZ_rrW5e-_7ViZ8Ma7ejBrStQECJDo4OIUvbuh7qKRDvBT4xUU-Zr48BsdxBzi1SFOL8cuS-IpdrNfovW4eklupzeggdtJO9hGoLojw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی‌های آسیایی ناگویا
باخت غیرمنتظره فرخی در کشتی اول
🔹
غلامرضا فرخی در دور نخست وزن ۸۷ کیلوگرم کشتی فرنگی بازی‌های آسیایی ناگویا با نتیجه ۶-۶ مقابل شمیل اوژایف از قزاقستان شکست خورد.
🔹
در صورت صعود فرنگی‌کار قزاقستانی به فینال، فرخی در شانس مجدد برای کسب مدال برنز روی تشک خواهد رفت.
@Sportfars</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/465412" target="_blank">📅 05:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465411">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فرنگی‌کاران با شکست شروع کردند
🔹
محمدجواد رضایی در دور نخست وزن ۶۷ کیلوگرم کشتی فرنگی بازی‌های آسیایی ناگویا با نتیجۀ ۵-۱۴ مقابل حریف قزاقستانی شکست خورد.
🔹
در صورت صعود فرنگی‌کار قزاقستانی به فینال، رضایی در شانس مجدد برای کسب مدال برنز روی تشک خواهد رفت.
@Farsna</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/465411" target="_blank">📅 05:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465410">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uX_C98E2G68SPwo7m2BIxhfFvxUcoFuGss2WIQwhmG9Sd_NOC1E6SYyTMbvgyPwDFaf4Ux-LmRzr9eDlrXGYArSxFlr3w8wkStrwK7ohwWYXfL2u4_X2XNq2rncx12hAeb2CWihkgq-jh9JSV7sfh7csdq-NaQMSc4II76QlX-4DtHIH3qGTDz0FQLkpWs_QnIHIkHwxTVnsncRN3-da9pzSM-5T2R7q1NyFB40qQIJ0dhOg2tuJUYW_O-rHjhjC_dcRh09tn09jQnT7SMBjwoC6QpryEIuk2KSXxfgeKpiQj9CI3LMwuKCiS6hVnkgKqxY_NLXtNTYTMZwvE-TKkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گروسی دوباره خواستار بازگشت بازرسی‌ها به تأسیسات هسته‌ای ایران شد
🔹
گروسی بار دیگر گفت که آژانس اتمی آماده است تا فوراً بازرسان خود را برای ازسرگیری فعالیت به ایران بفرستد.
🔹
او ادعا کرد ما دقیقاً می‌دانیم کجا برویم و چه کار کنیم. تیم‌های ما آماده‌اند تا فوراً عازم شوند.
🔹
وی در خصوص زمان احتمالی از سرگیری کامل کار متخصصان آژانس اتمی در ایران، گفت: فوراً. اگر از ما خواسته شود، حتی فردا.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/465410" target="_blank">📅 05:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465409">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">انهدام مهمات عمل‌نکردۀ دشمن در شرق استان هرمزگان
🔹
سپاه هرمزگان: انهدام مهمات به‌جامانده از تجاوز آمریکایی صهیونی در محدودۀ هشت‌بندی تا شهرستان رودان از ساعت ۶ صبح امروز به‌مدت ۷۲ ساعت صورت می‌گیرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farsna/465409" target="_blank">📅 05:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465408">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گواهینامۀ دوزبانه جای گواهینامه بین‌المللی را نمی‌گیرد
🔹
پلیس راهور: گواهینامۀ ملی دوزبانۀ ایران جایگزین گواهینامۀ بین‌المللی نیست و در کشورهایی که ارائه گواهینامۀ بین‌المللی الزامی است، شهروندان باید علاوه بر گواهینامۀ ملی معتبر، گواهینامۀ بین‌المللی نیز دریافت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/465408" target="_blank">📅 04:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465407">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIGBs6XnvVdDJDgMdrslGPOKa-9kT9G16f7IhAQpy4R9WiC76ze-MhJym1xeFr_nnfvni2O57OqWPkiE1xYRA70uUHtJIh8ZWimPGabB1wXlEKYKhVt6N-fwm8Cn3SODkzUAlwEigSEgwBkO7p8rdO-9U__sn5UOqE2puimG9nd-Dya3otH_iamtAWMfo9i89YzG4K-JfncZmt-qVvDEk-MH11Mdlbs2hoE1QzSWtEIo83D3ttKJXGQiwnMZnkV6RSFIzkf8XQJtjRI0GcISZxwmUkVk-Njyf4NVb7CqgI60EU84q1UwwespZMLL91JqKS9v-kcDnK-LT6Uzlezpzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارشناس بلومبرگ: تنگۀ هرمز، ریسک آخرالزمانی بازار نفت است
🔹
فرانک مانکام استراتژیست و تحلیلگر باسابقۀ بازارهای نفتی، در مصاحبه با بلومبرگ: واشنگتن معامله‌گران بازار نفت برنت را با سیاست‌های کلامی از پذیرش ریسک می‌ترساند و پول‌های سفته‌بازانه را از بازار خارج می‌کند تا قیمت نفت را کنترل کند؛ اما این اقدام در بازار فرآورده‌های نفتی جواب نمی‌دهد.
🔹
در بازار فرآورده‌های نفتی، پول‌های سفته‌بازانه یا اصطلاحا «پول توریستی» چندان وجود ندارند. بنابراین می‌بینید که بازار فرآورده‌ها واقعا منفجر شده و جهش شدیدی کرده تا تنگنای واقعی بازار را نشان دهد.
🔹
واضح است که این «بدترین بحران تاریخ بازارهای انرژی» است. من تقریبا تمام دوران حرفه‌ای‌ام را در این بازار بوده‌ام و اولین چیزی که وقتی وارد این حوزه می‌شوید یاد می‌گیرید این است که «ریسک آخرالزمانی بازار، تنگۀ هرمز است».
🔹
امروز دقیقا در همان شرایط قرار داریم. نفت برنت زیر ۱۰۰ دلار معامله می‌شود، اما این قیمت منعکس‌کنندۀ بحرانی نیست که در بازار می‌بینیم؛ بازار فرآورده‌های نفتی است که این بحران را منعکس می‌کند. برای مثال گازوئیل الان در بالاترین سطح تاریخی خود معامله می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/465407" target="_blank">📅 04:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465406">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnM9QoVNFGDnb9Tz8JjSxCazSq3vdtXRvYP5c_FHiarbpxliWIaNCRZmcZyKryPin5KQdlQHzUi-V3pVkav5t_-Ls_G2NEl0QRGJQR6Ar5q8o4KaDlwhO--zamxfFTcUZyLsegO0oluHKbCDktO5vlWMc01mxUanP7-ZDux_09h2SWxfW05kq6z7KDaqQedVayOSQw6mWGR2-_AAQ6ecVispyPaws4ikrc0snt9dS7B5CJSeZMDJVq7PDgRLvBVZKPOLHC92GbXvK3N98cDPcUYPpG1UVloqPrbFEBnHnFj712xANQJnvnvUSO1VGxHTy9-OmwJsHwwuv4Cy6wYhQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جانشین فرماندۀ کل سپاه: توان موشکی، پهپادی و پدافند هوایی‌‌مان با سرعت درحال گسترش است.
🔸
با صلابت در تنگۀ هرمز حضور داریم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/465406" target="_blank">📅 03:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465405">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c2be7ddca.mp4?token=fTw4k9NmUhwlNhBqybIqZ7rTWLDpFFFBepB9vqW1_GPwyatIYFes0GNmG_36mCnCRf75JZ97zMPs28NPpU30_bZltJ47GDfE5CeYyhbSdZCUk9S3lLJ19HagFNP2aGjnk6-qdElC3Ww9_fp1_JoxDnLEyOqYUURGVpeOu_RZCPPXQUE1Ms9nPPu-4o_irn0Sw4Vvln41grErc3G0aDxnjRhBIkjx-5WGyCp2KUVp1SC-Nk8dPaf4DjNSMVZLLRQXPeKnsYtVoNxecWQCWxK3tfAG201Klr61usnLuWsuNndgXlSso4gGZ6qMqonai1z-b3hS70lmFCBQ9VeL8DG9Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c2be7ddca.mp4?token=fTw4k9NmUhwlNhBqybIqZ7rTWLDpFFFBepB9vqW1_GPwyatIYFes0GNmG_36mCnCRf75JZ97zMPs28NPpU30_bZltJ47GDfE5CeYyhbSdZCUk9S3lLJ19HagFNP2aGjnk6-qdElC3Ww9_fp1_JoxDnLEyOqYUURGVpeOu_RZCPPXQUE1Ms9nPPu-4o_irn0Sw4Vvln41grErc3G0aDxnjRhBIkjx-5WGyCp2KUVp1SC-Nk8dPaf4DjNSMVZLLRQXPeKnsYtVoNxecWQCWxK3tfAG201Klr61usnLuWsuNndgXlSso4gGZ6qMqonai1z-b3hS70lmFCBQ9VeL8DG9Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خدا از تکیه‌کردن بنده به جز خودش بدش می‌آید
🎙
حجت‌الاسلام رمضانی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/465405" target="_blank">📅 03:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465404">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RN1_WG1rG5jKoCHEziY49eci1FhEepXIVKRnMPZIb_XbtkXdpwo-164UuqXNJQO0hDQvizUOyyWeAn3Sq8eBChg939GIY8ge-bt1h4yIn0P-XQ85nBJu_Q_p1MLsS3uNSjVPXzU97VdfpyYrrfFmpJD7Zub84_3DQOt41B3Qpa5D99HgRsRY8f8Gk-LzkSlApBSdfWUh-73WoczyKC6rPg6XKA_aet0E5H4qV1Ey_XsxQRZ13p7lRheOUmvy2i04q_jrCD354zCnCVh_a0RI9tihL4IHitWEUDcafUeMvk4vxkIwn9mfqvACihto1T1vluf76KsaJtbWdlBMLmOAXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کابل ارتباطی قاره‌ها از کوچه ما می‌گذرد!
🔹
بیش از ۹۷ درصد ترافیک دادۀ جهان از طریق کابل‌های فیبر نوری زیردریایی منتقل می‌شود؛ شبکه‌ای عظیم که از مسیر دریاها و آب‌های منطقه‌ای کشورها عبور می‌کند.
🔹
ایران نیز در مسیرهای ارتباطی خلیج فارس، تنگۀهرمز و دریای عمان قرار دارد؛ مناطقی که برای اتصال شبکه‌های ارتباطی میان آسیا، اروپا و دیگر نقاط جهان اهمیت دارند.
🔹
اعمال حق حاکمیت بر کابل‌های بین‌المللی عبوری از حوزۀ قلمروی ایران، اعم از دریافت تعرفه‌های ترانزیتی، صیانت حقوقی، تنظیم‌گری زیرساختی و مشروط‌سازی ترانزیت به بهره‌مندی متقابل از شبکۀ جهانی، نه یک انتخاب، بلکه حق قانونی، مشروع و انکارناپذیر جمهوری اسلامی ایران است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/465404" target="_blank">📅 02:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465403">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBDuhCmX463xa6qffCtdhAgCALSd3DSylBEExuf5eM0cY4T1rIRuB2hnjUd9t75zZYJsPTWAb_kDsqIGs18VUc3P_iOt2YXVPnL7B-SkMTpNxdAQGW3ZZ1CIQCpblFmppQBq0IkbfekROCDb-jn2y3VBSiHo43o_09jwx2f-uaBJSNff11tnrekQGv0gNUvRvaE7_s1VvKk2lUMNw7OtERDt_drpDEpY3fAsUrxn5aq6jZScBJIoXE9tzQIo9dDdUYjD5jCh6pB5tGrwPsfB5LDCwNVbvjpLTsTy8Ki-wK3mRCoLF5tqZ9JBFePc-c44Foogxq5xL2kaJ-eH2mD9zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس این کشور در حال بررسی ارتباط ادعایی این حادثه با ایران است.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/465403" target="_blank">📅 02:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465402">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52c3e03c58.mp4?token=oFDO8KRmF6mWj_VyXvt9vay_WRSDPFnczPmvIkLIwSGAtN-kXxzlfGVltNdt2BjUKzKl_o3aHaWXsm09V5dCzBh8LpvqdtGYOR1aQExuSNOuTQ3AktTSxLizoUQGgPiflm8329a-yu2wiOncx8SxvDYIWPnM8rL9TQhQ6jVda8mNUCoDCPyEzATHSiOStGQL3SWO46MCFIrCAtn7HdSEwjBeu11WpGXhJBqXHcDtYHsWri5AztasjnND4tto2HZi_3pQ_Av4_Iw4K5I3mg4KL8Ao-fkMcPtCxQBxF-zo3d9MTx8gZsYIbTUHh7UpDAHqoSQPkW3bN4Pq5MrIGylR6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52c3e03c58.mp4?token=oFDO8KRmF6mWj_VyXvt9vay_WRSDPFnczPmvIkLIwSGAtN-kXxzlfGVltNdt2BjUKzKl_o3aHaWXsm09V5dCzBh8LpvqdtGYOR1aQExuSNOuTQ3AktTSxLizoUQGgPiflm8329a-yu2wiOncx8SxvDYIWPnM8rL9TQhQ6jVda8mNUCoDCPyEzATHSiOStGQL3SWO46MCFIrCAtn7HdSEwjBeu11WpGXhJBqXHcDtYHsWri5AztasjnND4tto2HZi_3pQ_Av4_Iw4K5I3mg4KL8Ao-fkMcPtCxQBxF-zo3d9MTx8gZsYIbTUHh7UpDAHqoSQPkW3bN4Pq5MrIGylR6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعای مضحک ترامپ دربارۀ تسلیحات اتمی کرۀشمالی
🔸
خبرنگار: شما گفتید که ایران نمی‌تواند هسته‌ای داشته باشد. چطور کرۀشمالی می‌تواند سلاح هسته‌ای داشته باشد؟
🔹
ترامپ: چون کیم‌جونگ‌اون ترامپ را دوست دارد؛ او از افراد زیادی در جهان خوشش نمی‌آید اما من تقریباً تنها کسی در کل جهان هستم که او دوست دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/465402" target="_blank">📅 01:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465401">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eX_6IREbc8HdpoIVEIDcZzXrP2f1BtUy0E97e07DtGuNKAIYJNfcWDP8mnWveV_fLYsFjEaFCramD2YdePvJ2ghNc1BFgZfYogGSoffTqflgedsA4ANhI797j0nNRmNjaBFPNvoH3Ej-puPOvPxSIDJbCa4hjaD773e3Lp6BPMJNWaO8El85bDO5YY4tYmCdjdA6GgGnGQDObn8IjDDFHkpePH1_yPKx1tMKfMXvQxWwlpUiBQcM3PXNRNsVEax_AP9EswNdg9oZjKosZ6AFtwX0buuEJ_iFtxA_-6iemVteJdqWmFUXMkrTXjAslkMdQYplvk-6SEZZY7Nr1-Pmdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میراثی که با این سبک قلعه‌‌نویی نابود می‌شود
🔹
۲ بازی، ۲ باخت. پنج گل خورده و فقط یک گل زده. این آمار تیمی است که با شکست ۳ بر یک از ازبکستان و ۲ بر صفر مقابل روسیه در نخستین دیدارهای تدارکاتی پیش از جام ملت‌های عربستان، هیچ شباهتی به تیمی ندارد که در جام‌جهانی ۲۰۲۶ با وجود تمام حواشی و مشکلات عجیب‌وغریب، تا آخرین ثانیه‌های مرحلۀ گروهی برای صعود تلاش می‌کرد.
🔹
این تفاوت، شاید مهم‌ترین سؤال امروز فوتبال ایران باشد: چه اتفاقی در این سه ماه افتاده است؟
🔹
امیر قلعه‌نویی باید بپذیرد که تیم ملی نیاز به تغییر جدی دارد. نه تغییر نمایشی، نه عوض کردن بازیکنان و نه پناه بردن به آمار. تغییر باید از تفکر تاکتیکی شروع شود.
🔹
او می‌تواند بگوید این دو بازی برای شناخت نقاط ضعف بوده‌اند، اما بازی تدارکاتی زمانی ارزش دارد که از دل شکست، اصلاح بیرون بیاید. اگر در مسابقه بعدی همان مشکلات تکرار شود، این دیگر تبدیل شدن ضعف به عادت است.
🔹
اگر این تیم با همین کیفیت به جام ملت‌ها برود، دورۀ حضور قلعه‌نویی در تیم ملی می‌تواند بخش بسیار مهمی از اعتبار سال‌های کاری‌اش را زیر سؤال ببرد.
🔸
قلعه‌نویی هنوز فرصت دارد. همین شکست‌ها می‌توانند نقطۀ شروع اصلاح باشند. اما از اینجا به بعد دیگر شناخت نقاط ضعف کافی نیست؛ وقت برطرف کردن آنهاست.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/465401" target="_blank">📅 01:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465400">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f638ca38c8.mp4?token=lOp9X1YI4DOw-jn6_Dz6RxE-PSX3wWnBa87ZqvPGWlJy8vuiB464DvagpaN6yPttAo1ESXeaFNryqDq8ag2RaKol116MCM-LuzCCtWAvYnRbMHtwn7x8WpkbMDWRKWkvH-06DBk7yC91cHvzn194TuK0b0H8xu4eVwNI72dbt0Kr8m2aTl2vHOTVySQpy3s_QspYz0-ED5lP3O4-FmdnYN46mRngTjQZG8CFMXAMOlzxzHO4t8Bsxv5zJChI-N7_gF_tCXu2tg1Y_Lx2Zr15UmSxQCIpP_zMWFRyVsZk5ONNpBgE0zZyOA_P57tNUP88lEtEKmBvylAC99uGMf7NNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f638ca38c8.mp4?token=lOp9X1YI4DOw-jn6_Dz6RxE-PSX3wWnBa87ZqvPGWlJy8vuiB464DvagpaN6yPttAo1ESXeaFNryqDq8ag2RaKol116MCM-LuzCCtWAvYnRbMHtwn7x8WpkbMDWRKWkvH-06DBk7yC91cHvzn194TuK0b0H8xu4eVwNI72dbt0Kr8m2aTl2vHOTVySQpy3s_QspYz0-ED5lP3O4-FmdnYN46mRngTjQZG8CFMXAMOlzxzHO4t8Bsxv5zJChI-N7_gF_tCXu2tg1Y_Lx2Zr15UmSxQCIpP_zMWFRyVsZk5ONNpBgE0zZyOA_P57tNUP88lEtEKmBvylAC99uGMf7NNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس دفتر رئیس‌جمهور: آمریکا از ما خواست که هیئت همراه رئیس‌جمهور برای سفر نیویورک، در سوئیس مصاحبه، و بعد ویزای آن‌ها صادر شود که ما قبول نکردیم.  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/465400" target="_blank">📅 01:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465399">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">حملات رژیم صهیونیستی به نوار غزه
🔹
المیادین: مناطق شرقی شهر غزه هدف حملات توپخانه‌ای و جنگنده‌های رژیم صهیونیستی قرار گرفت.
🔹
همچنین خودروهای نظامی اشغالگران به سمت مناطقی در غرب شهر «رفح» در جنوب نوار غزه آتش گشودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/465399" target="_blank">📅 01:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465398">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d3f16facc.mp4?token=V3a78C_jRy43l9vC0VAkFOSgRX3vJh-DI5AzpCVt0EXE5r9WBVo8hHLB8lvb0_dxajbhQ-M8QZQQWxMPxlE7oIsP0CTxds-dLuN8U6a-K9eHbrQp-A_TIvaCiX5bbQ6H6olTnGDLhuScb8Cw82wx5LpaTTrQam2GFurSbedfgdmSw1qK1Smh0Zothdr5Tle2_71l6TrIQY4YZRH8wYmweOHCBWRDFpv8kYAosBwa1hUBTQPvb2kVmvXqQ0_moNrEExpaTMOnknec4P8y3yRDNtx7MOPp4CBuNAnFmQw3zoEfSrjl1r2MHLAh5vvbPtE4-1p9aig7jmJm8BddEk17zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d3f16facc.mp4?token=V3a78C_jRy43l9vC0VAkFOSgRX3vJh-DI5AzpCVt0EXE5r9WBVo8hHLB8lvb0_dxajbhQ-M8QZQQWxMPxlE7oIsP0CTxds-dLuN8U6a-K9eHbrQp-A_TIvaCiX5bbQ6H6olTnGDLhuScb8Cw82wx5LpaTTrQam2GFurSbedfgdmSw1qK1Smh0Zothdr5Tle2_71l6TrIQY4YZRH8wYmweOHCBWRDFpv8kYAosBwa1hUBTQPvb2kVmvXqQ0_moNrEExpaTMOnknec4P8y3yRDNtx7MOPp4CBuNAnFmQw3zoEfSrjl1r2MHLAh5vvbPtE4-1p9aig7jmJm8BddEk17zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس دفتر رئیس‌جمهور: هیئت ایرانی در نیویورک به جای هتل، در محل اقامت سفارتخانه مستقر شدند که باعث کاهش ۵۰ درصدی هزینه‌ها شد. @Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/465398" target="_blank">📅 01:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465397">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/465397" target="_blank">📅 01:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465396">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f64975f37a.mp4?token=dJyEYy-VVUl4y22fQlM1eQ_ykEBD2GApJ3ih0g-7IR-A_Iw2S25KM_KBk3CgBh_MtO-JXHTcB0Bau88RfIeUkRqwiMdQl0igxdzUvGDyK-gi57Wbaxc8SQyFcFztbtwtK0lk-JKYFVu-ba4xaEwc1iZlhX0Eq7pLTnt3GbETzBYw0PTbrovPonLIYiBr3Rxkb3Z7XOHsDKXBKhQ5akDuJ1YQjLDdU0o9agkms9uDHvf4y9lheJUdRdI3zt3mE9fgIBHkGk2rkKWJLPkK7SzImF1B4MVV-Po3_Xg1iHsZ60c3FbKN4zdsz2VWhYs89dfpdzKnzTdqE2OiPtdXzaOPCBG-rrkA4Gitw_PPYzXKXauicA_ZA57NyEQudJQ3nK4jj4xGDZ16T5-XUMkW9PWLk31zHZnj5woIONXGefP-FRuOEggSo3Sv1zu7y-6EXSVNQaKUuIqotcWAjfl90SVegFG96i5Sg86iOdsGO3UoTiB9JNez2puLDZiPjgXfqg6VyKje8LA80X7PcIO1HUDghxncI7Irnzetu45kSA-jqLcrssSEtWc-W1pbYESHG2WSCNl_6DsrVXO9wgCrCSXg-KUnBMsetCYKUAY8k1-_xY-pQE02QV8ATwq2bw6bOvYbL7DCyAUASMMO97DDt-P3iN1-fout6I2vvT6TqVhTmr0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f64975f37a.mp4?token=dJyEYy-VVUl4y22fQlM1eQ_ykEBD2GApJ3ih0g-7IR-A_Iw2S25KM_KBk3CgBh_MtO-JXHTcB0Bau88RfIeUkRqwiMdQl0igxdzUvGDyK-gi57Wbaxc8SQyFcFztbtwtK0lk-JKYFVu-ba4xaEwc1iZlhX0Eq7pLTnt3GbETzBYw0PTbrovPonLIYiBr3Rxkb3Z7XOHsDKXBKhQ5akDuJ1YQjLDdU0o9agkms9uDHvf4y9lheJUdRdI3zt3mE9fgIBHkGk2rkKWJLPkK7SzImF1B4MVV-Po3_Xg1iHsZ60c3FbKN4zdsz2VWhYs89dfpdzKnzTdqE2OiPtdXzaOPCBG-rrkA4Gitw_PPYzXKXauicA_ZA57NyEQudJQ3nK4jj4xGDZ16T5-XUMkW9PWLk31zHZnj5woIONXGefP-FRuOEggSo3Sv1zu7y-6EXSVNQaKUuIqotcWAjfl90SVegFG96i5Sg86iOdsGO3UoTiB9JNez2puLDZiPjgXfqg6VyKje8LA80X7PcIO1HUDghxncI7Irnzetu45kSA-jqLcrssSEtWc-W1pbYESHG2WSCNl_6DsrVXO9wgCrCSXg-KUnBMsetCYKUAY8k1-_xY-pQE02QV8ATwq2bw6bOvYbL7DCyAUASMMO97DDt-P3iN1-fout6I2vvT6TqVhTmr0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان کتاب «کمک‌های آمریکا به مردم ایران» را به رئیس‌جمهور سوئیس هدیه داد
🔹
در این کتاب جنایات آمریکا علیه مردم ایران، تحریم‌ها، حملات نظامی و ترور دانشمندان و فرماندهان ایرانی تشریح شده است. @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/465396" target="_blank">📅 01:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465395">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTN9eZeg1SS_MDdl6-7Gn6Pe_7B15N_Fp8p1ydUyqfsyZ41THXklCWDtXDouWPPobVydFCJT3G1O7OMSUq4arAEAWbSKK6VO7bfYShyG6kbuesUYqxfRKcZVOp29Vi0UdUUjxZ6ArhhsE9vwGT0v86k048G1Jm8UBaMMDGSv9BnSss9sQq_DAGBA0dv4uUraZ1C0D-oLWS8iWRoxV60yZqplOidIf1dNT3yilZzqHfgnkD3VlvhYF_oAVqVqeBVGd8rbUT_UoaZRofrrqKR5fj-1J_sKhg_bQ2BZgWBfvc03N9BsGEwZERFtuj0X8nGR5xiJ95fXY0E1JX1H21vUGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صورتحساب سنگین جنگ با ایران برای مردم آمریکا
🔹
سپاه در نامۀ اخیر خود به مردم آمریکا از انهدام بیش از ۲۰۰ پهپاد، ۳۰ جنگنده، ۱۲ هواپیمای سوخت‌رسان و ترابری و یک آواکس خبر داد.
🔹
به گفتۀ سپاه، بیش از ۳۵۰ تأسیسات و زیرساخت نظامی هدف قرار گرفت و توان عملیاتی ۱۸ پایگاه آمریکا در منطقه به صفر نزدیک شد.
🔹
این گزارش در حالی است که واشنگتن‌پست نیز با بررسی تصاویر ماهواره‌ای، خسارت به ۲۲۸ سازه و تجهیزات در سایت‌های نظامی را شناسایی کرده بود. بی‌بی‌سی نیز از آسیب به دست‌کم ۲۰ پایگاه آمریکا در ۸ کشور خبر داده بود.
🔹
گزارش‌های پنتاگون، کنگرۀ آمریکا و رویترز نیز از خسارت به جنگنده‌های F-15، F-35 و A-10، هواپیماهای سوخت‌رسان و ده‌ها پهپاد MQ-9 حکایت دارد.
🔸
این خسارت‌ها علاوه بر هزینۀ سنگین نظامی، آسیب‌پذیری پایگاه‌های آمریکا را آشکار کرد؛ حالا مردم آمریکا حق دارند بپرسند هزینۀ این جنگ چه دستاوردی برایشان داشته است؟
🔗
متن کامل گزارش را
اینجا
بخوانید.
@Farspolitics</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/465395" target="_blank">📅 00:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465394">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32e208aa3f.mp4?token=XcLK2YnjV1QMt1-p97MMLqpCGziL76Ujbc-34v46CUJqRH4AEo4ZIpcs4jYmqdwYnPfo_tma_FvrkGjSuinovGRFcqNGHkQwehaKGFl3Pgi5F41mO_p81ZLD5AWoMg_yIGYPuHWpXHySC5KzuDzdBdJlo6_7dYGxnh1mElmnAHXT5ThW39LzEh1FKgrFDf0sh1W5I2oO-tjw1lnTOxaIdMRVUYSme7z9x9utsRVN8wFN1mTPobrk0D_xtcOmzm5y1pIaQ2xQRKp1BvyYt2T3JUP8QckFQkBZEw45oXcXwK3gMW4gcLYzJGf3muvxA0U6k9VEvwM1LNSRiMWznbP_xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32e208aa3f.mp4?token=XcLK2YnjV1QMt1-p97MMLqpCGziL76Ujbc-34v46CUJqRH4AEo4ZIpcs4jYmqdwYnPfo_tma_FvrkGjSuinovGRFcqNGHkQwehaKGFl3Pgi5F41mO_p81ZLD5AWoMg_yIGYPuHWpXHySC5KzuDzdBdJlo6_7dYGxnh1mElmnAHXT5ThW39LzEh1FKgrFDf0sh1W5I2oO-tjw1lnTOxaIdMRVUYSme7z9x9utsRVN8wFN1mTPobrk0D_xtcOmzm5y1pIaQ2xQRKp1BvyYt2T3JUP8QckFQkBZEw45oXcXwK3gMW4gcLYzJGf3muvxA0U6k9VEvwM1LNSRiMWznbP_xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس دفتر رئیس‌جمهور: دلیل سفر پزشکیان به نیویورک پاسخ دادن به اظهارات ترامپ و نتانیاهو علیه ایران بود  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/465394" target="_blank">📅 00:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465393">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سفرهای گالیور</div>
  <div class="tg-doc-extra">قسمت ۲</div>
</div>
<a href="https://t.me/farsna/465393" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۱ – سفرهای گالیور</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/465393" target="_blank">📅 00:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465391">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKYUioRC1beQHpJ8FEom_SwrFCriGJoPV5ZNvxP1Nhfb0b06bUAuJZJ1ATIro8nw9KIwl161SBEJ08Ip6JZgUaCXz-JTVkODjnpSH3s4yL5STBiTnJDcRjJLk18T-PxEsuALxAVgyWyxR_kfSr7AHpcYVOQT02ThOhMp6hSBIVajju7saDhfWh2Z3LckbnQ1lsSMEkGjsueJeEGz91TRLyr29gsuXfYCCNn9boFPVj5nBukIO4muO85auhzLlKGaHEMjDqUI-GmwVcYw6jP5M5bfvfvxJb1Tzb0w5u2Uir29hNf9mfXPd2MkSum0lXya-j4TKVBcD03Y2EbSQdJXCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس را بدون اختلال دنبال کنید
🔸
به‌دلیل محدودیت‌های ناشی از تحریم‌های آمریکا و عدم ارائهٔ برخی خدمات زیرساختی به خبرگزاری فارس، دسترسی به وب‌سایت فارس برای برخی کاربران با اختلال مواجه شده است.
🔸
برای دسترسی پایدار به اخبار فارس، آخرین نسخهٔ اپلیکیشن فارس را
به‌صورت مستقیم
یا از
کافه‌بازار
و
مایکت
دانلود کنید.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/465391" target="_blank">📅 00:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465390">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/400bc7c6df.mp4?token=eWg0CD8Ybde8sE_usAwQocLfwWsL1HaqEA6KMFpqZM4YUPALhRw8_JZvW8lDUff948YgCuULSpSTeje7bdIz8RYKf_Wk54obpnpD4PscEO8k80asmvy3FObZhA2HWnMcqonTfBHv8SPE-47nqXyIASeomevA2FtsE9KFUXeuUIL2DSfr5tJQb5ZULb5RQIVGXY2Aco1IF_N9Kao5Wvp2RSNFq9nWNSKPZjpqJ5uJTl_jIe7Pbbs7GqJBZTWO50QbLTBGXjm_gThpCdJI5tR7XBYDcfCOltFmq-_07xYY4L45PAQhBWf6vdsVjH-L-pJqhqlrMlNEKp4FS_XbASKx9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/400bc7c6df.mp4?token=eWg0CD8Ybde8sE_usAwQocLfwWsL1HaqEA6KMFpqZM4YUPALhRw8_JZvW8lDUff948YgCuULSpSTeje7bdIz8RYKf_Wk54obpnpD4PscEO8k80asmvy3FObZhA2HWnMcqonTfBHv8SPE-47nqXyIASeomevA2FtsE9KFUXeuUIL2DSfr5tJQb5ZULb5RQIVGXY2Aco1IF_N9Kao5Wvp2RSNFq9nWNSKPZjpqJ5uJTl_jIe7Pbbs7GqJBZTWO50QbLTBGXjm_gThpCdJI5tR7XBYDcfCOltFmq-_07xYY4L45PAQhBWf6vdsVjH-L-pJqhqlrMlNEKp4FS_XbASKx9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: نمی‌دانم که آیا ایرانی‌ها حالا حالاها تسلیم خواهند شد یا نه.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/465390" target="_blank">📅 23:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465382">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DDYBA1XeHRsOLxQEF3sSk7bYjbmDISJJwgn_7ueXYhH-D9_O2UDBrEG80O0ptmgKBrRljaSMxRrV6D90heT-KSGfi8U3oMJYI3hddJPXWBCGJUPNM6kDJetKIyY0KNMNDKmHkzZy_Mos79-v7if8bCZKDljGhh7kD_mmTndFM7CIPPft18fSYF5d5rtsqL5x0TWV6xK_VH_jgBJyH9evzZq8nYe-qyma-x-NH_fbB_1tj9YCnTwxrcU0JsQjRThmN4pusgeqWqHSSGbLKjBrha2F8vDa_i3eR8_q543kbDXEjy47ERC6yxVR2sB_lKnuEd_dS2sKxes4fI5TKUCpcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ivKqKi--ciyNF2tAK9M-D77sZaowe26ywoo-LsyQSei0jZVn9kBn0meUzNW-GFKXv7cKtte5MDspflgoYJkchEVOkJB6Wr_qwpJ0IiXaMEVXV0YgjIrT5IjAHUNlCiM4DuazRVhHs_ixP2gwm1xnfu0ukMGTA4dklMGy55X3NCpBci0V4qIOH-fYidMEojgublyq8D3w0mn_3YNnTcJzmGt1f8IzFwQY4qkN18JiyjE_BD3bPoZf4W9AiWdj7Ri_RoGrP_sRFwfUgc2L5YmhrUozgC06ddPkcFG1DI7JaZU40vFjparFnbTqLNgqyVxhO67USR1e_9JyclnnMkUDbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rrNVYEXBN2X78JYmRx4B6hcfcQk8n0hCpPuHIrNkaT7Q-W6JR84_Dz1sa-5Sp1yPEUtn_6bdlqb_th-IwaXuO9kNaQoX7bj6SsuQlPxi5MmSeBWo2O49qrqeEZWjp8sv4NfUog5algH1gcE_QsPNy-MOfcn2zr4qTY9zWbO2VYcPTC8NtOrb3LSxDpzhxVfWGhFTzYa9NLdY-Ifv7YKf8I9BnXfnspxnEW3YYS2vNfBuK77B513JtMbBZqz50LZnttJy50GGypqbGPG2ZZKc4-XWtWYaVkbWDu_M94TW71UBkEtQabbovsDQG8XwQKPqt-uQdr86iEaDxziF5SmuYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XEcbnTTD1BH98kDRZjLBLjWiwX7wac4_QcQQp57INbX6g8wZKflHI3UxnRTomM12poMMJeClQcfdE5CYKcuMAOoYrmNOaDhfnriiWB-cc3R8LzendiL61LCn4mAbOsl3PHCYCQkVP9g6biVinVk2zPRzJ1iWtBwAvrpe10957jHt6gf68dXTCUkA-tOO48_GRYItGkEXnviar4B8TcvraWOiCBMNow97njIR5aoA7SHB4Qnkmrm1boSp6hgElUHLFlZx_VgU_1-m7-XLVTs7H4V61pCTCKQTvOINAdZWXHuHmXbiJQjTam4l2cnePBy-SLnz4heUmZB_dg0G1VEBDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DP92RrnRO3zYoxY8I0HihF7eW8CSBcQqiVmyLjRnAEPJAC6axYifrhGxaSOQL9dLqR_5DZZpqYq6pqhtlyi4Disvj2TqCAvAn_LW1xIReMgz3nB47pyPtK0THUJogr8_jxN6eH4M7i_3uN_HENxej660u1JIhkTj7iztGaZOWArfzQK1jDE6COG2mQ2ToQWxWkc86mh3jqkVnuyf3cBRzkEPyAemDmFZz5TLbnzCCKBQFzJrG4Jt6obqDxuerlQbrZQue7iP7WCPdfEmchFaMuyX4YhJ4nOB5QuORdBQq0sMRmczPJu3syEeUOEZBs9FdlrRM3scHqABkDVFmRtyyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jy5bfgLylpIluH43OxFwRHfU4AY1ClrzDYAcy0wK0c96vzM5LUxu4nO1ywsK2bsfimLgMMN4hnrEtLlW7ZiHx1p8VnZoOyfj0oNVaMaXFxNiXOv0jI8GypUq3q9HdJct4uLUJkLl_z4COHOTHRUmCAhmiU-BtHKUZb4GvAk0J-E_IhOVJubksNzMoClPoAfBWYaTMY_oyaKwixT0CDp33SUxnRor5C0Xt2F9-bKYKnflVNjCq6RIlegik457nDh9vvGvSlU5xkDLXpJUQGyiUziUzITmz0_NW3GRX4bYAeXu4vG0AL-MxzZ2QhdjEbNO9-DPKhaBL2Ni4-vVDp4iIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tPRSulIwsWrKSBL9Eb9ijjT5URIoYQlbgvGcpV3a5B2IiQSk--gNPVSZ1MGMzaVStyKypnAdYKOG8tv4uHxtV33MyHelgjnTV1l9-jHdgng1PsH8-jp0LZrFOAezS4mShmP2n1jTdXFJs8AZ0hCHi5mplUfRoSjPvYOL_Mto9XjBDOQo3Gt0B9Bbsmi8LV_tjvUz1te_OJsGlIgG3dpbaApbuDM9vrQkMLg6F5lCgoGcf6jXWZXR6f28kkSi9aioj2-5P56dKkB0zuPJ3bEgGFid-q57vLbpRCmi0JRaPiDFCddJo23ynik7r3naoxGXPxEJtvasduD4HsHJJBD6pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QiXtUackubAgy_JzESVYJSktDrLjm6F2Zi9j5n7N7rO0tZ6bJsd27SgaYuWDsKE_pzCAeimKxcBi21vQr5LNbB7obQaA_0a771a4YA07h1dNq4Frw2fNw-Dh4_dHxtK_BJa6JsyYqfAc2HEFcWUWRkrHlwzLyGlGZGZ4bksp9_Q3kvDh1aqdO_FeRkSGIIy4h41Kbmchi8Qme0bKImTB9DvdslRB2hwVgtxrXQEJFv051_kx3tEX1i4JyagVNXLj9eGBngc356WOHJKZOI_k3FAtWY-NuBs80L-JBX391vkJ3DY12OCoCvqQJ1mzk_j-zVxHsk66wb_gPXmzCyACew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم روز آتش‌نشان و رونمایی از خودروهای جدید آتش‌نشانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/465382" target="_blank">📅 23:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465381">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9_4viJ-7NuuOUsVhOo4a4Y4Uy0F-QQOdEf2Hg0pVp35cU3oYNgp0ax4z6RAz_mXxijQ1DyLzfPD_UuTFBWjgUeev_Pf24iFBrNWNencG5xQpCvNUV3qEchwLM90VZOY6W5BInK5pTEz75OSwU37QuhRUccgV57CNdd4V9oaLomUyLZHxXQqV-fh7JvfdZW4D661zvKLTBlj54alOquM1wQVtm7-W_Coe0T9fPWIfdQmGHRh0TK7p_wqm74f2Ajxww72CVfvECZgOo8Ol6-hUHr3dFa3IS8rUooxJrXgrlaOxF64DbkA_5wnSlkYC1WITlK0VhnTMpx0fxXGdUU-vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
امیر قهرمان عرب
🔹
رهبر انقلاب: بی‌تردید در طول کل تاریخ شامات تاکنون، پس از انبیاء و اوصیاء ایشان، رَجُلی به عظمت سیدحسن نصرالله در آن خطّه کهن سر بلند نکرده بود. @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/465381" target="_blank">📅 23:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465380">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxN8JuUTirW_hxtnggQlO3GIlxp0ikulclpR3szYRhZq_m3fP6WTn-G2MavQ35rngI491EN90EMHGc36oZdenaa7FGEHmzWyeNt3AoVJwO2NnBuy2NuSZcJedcTXLuih3q2mT-_VCZBbTqScTjHGhA9lc3KzaaEGSgrGNc2isiOuwo3EBKCt9rpD12QVqJA_qAoZXhVpvnp4JY9NWPlql3aJznMV9EnYTa3Jj1bxrqypniGM1Lpt9eRvI19ud1kor_B6YRtXjdqEURTVkbtXdbXjrVNHehi49SJDtkvQALD7a_jnv5KCSGeUK2y5Lp2Dxt_kFtWX2Q7B_qEyF0zutg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌تیم قلعه‌نویی حریف روسیه نشد
⚽️
روسیه ۲ - ۰ ایران @Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/465380" target="_blank">📅 23:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465379">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار در اربیل عراق خبر می‌دهند
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/465379" target="_blank">📅 23:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465378">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">هشداری برای تخلیۀ شهروندان اروپایی از ایران صادر نشده است
🔹
برخی کانال‌های تلگرامی در حال انتشار خبری مبنی بر این هستند که فرانسه، آلمان، ایتالیا، سوئد، نروژ، دانمارک و فنلاند هشدارهای سفر خودشان به ایران را تمدید کرده و از شهروندانشان خواسته‌اند هرچه سریع‌تر این کشور را ترک کنند.
🔹
بااین‌حال، این کشورها هشدار جدیدی صادر نکرده‌اند و به نظر می‌رسد که این خبر قدیمی و مربوط به چند ماه پیش است.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/465378" target="_blank">📅 23:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465377">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGtKHM4tIjcabotlZ2S6r_UMtDUw-w-SilT8jYQHL6-L7ftNO6XCoKEQTMgbMyms09H0N9NQjeM0_27tso4wP4y_MbncyRP7AwilLK5aPC0R3VGMHJDEI0GAAh0OSmg7gvynDszRyUA3F6ljImSQxHypF_3UDPoXD1A_K4smAQmrj7A5kXfWw132NHrL5UuVs0PuQGmf4r0q9f9iR1vH78VaYogscpaGC-rX71cNo0rABEjMm_Huu8Ts01hJ1Ck_LjG-EMKfwhcdkM4kYE_-NpvhnE6th01oAGhCmQ8C1Qslw3O7RQPHxGRXto7gQreWChp8xt1i2IcC39iTnBtTug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
📝
چرا سپاه به مردم آمریکا نامه نوشت؟
🔴
محسن مهدیان
✏️
نامه سپاه به مردم آمریکا را دقیق ببینید. نهادنظامی ما با این نامه وارد عرصه دیپلماسی عمومی شده است. اما چرا؟ چرا این نامه را باید سپاه بنویسد؟ چرا وزارت خارجه نه؟
چون ایده نامه قطعه تکمیل‌کننده یک پازل متفاوت جنگی است.
✏️
جمهوری اسلامی در این جنگ به شکل بی سابقه ای یک جنگ ترکیبی تمام عیار را علیه دشمن به کار بست. میدان نظامی، دیپلماسی، پشتوانه اجتماعی در داخل و جنگ ادراکی در دنیا.
خروجی این جنگ باید چه شود؟ بازدارندگی.
✏️
ایران برای رسیدن به این هدف برای اولین بار جنگی که ترامپ راه انداخت را سر سفره مردم آمریکا برد تا هزینه این جنگ را حساس کنند.
اما این برای بازدارندگی کافیست؟ نه
گام بعدی اینست که بفهمند علت کوچک شدن سفره شان چیست. اگر بفهمند چه میشود؟ تحمیل هزینه به فهم علت هزینه تبدیل می‌شود و در نهایت این فهم به اراده سیاسی منتهی می شود. بازدارندگی دقیقا در این نقطه است.
اینجاست که نامه سپاه معنا پیدا می‌کند.
💡
برای خواندن جزئیات
اینجا
را کلیک کنید.
@Fars_plus</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/465377" target="_blank">📅 23:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465376">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb04cf477d.mp4?token=Wrup-2C1-kNuLxure-NC7GQOXqMN3K6M7hkRRpD-8VS9M1bH8M4d30wwJjEq5OPhnuNQMu53p4x4ZPXRMdI-kIi5-BvWHfO4r84SE34tNXXDyHGhw5TioX1And0k_aDzVwQxSx-4tfwvc0SdTokotFrifrQHF70YpGp1qFl0j3u9NoPYn5xeZyA-LW_5qgqpgsrLvGJS2OxXAXRN7swYJm1fOvVBjBWnDaxrJTGHQm7yYXeJWOfGddT-yODa2p9VdXz1e1ngLSNcKannGvHvmLMj70bbIEGUPYdlosxog8-Ibfzo-rXY5ey5M2FGwL2hcHOiZdVinLwvGz0GTRIilw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb04cf477d.mp4?token=Wrup-2C1-kNuLxure-NC7GQOXqMN3K6M7hkRRpD-8VS9M1bH8M4d30wwJjEq5OPhnuNQMu53p4x4ZPXRMdI-kIi5-BvWHfO4r84SE34tNXXDyHGhw5TioX1And0k_aDzVwQxSx-4tfwvc0SdTokotFrifrQHF70YpGp1qFl0j3u9NoPYn5xeZyA-LW_5qgqpgsrLvGJS2OxXAXRN7swYJm1fOvVBjBWnDaxrJTGHQm7yYXeJWOfGddT-yODa2p9VdXz1e1ngLSNcKannGvHvmLMj70bbIEGUPYdlosxog8-Ibfzo-rXY5ey5M2FGwL2hcHOiZdVinLwvGz0GTRIilw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس دفتر رئیس‌جمهور: فاکس‌نیوز را به‌دلیل این انتخاب کردیم که نزدیک‌ترین رسانه به ترامپ است
🔹
بیش از ۱۰ رسانۀ بین‌المللی درخواست مصاحبه با رئیس‌جمهور را داشتند و ما ۳ تا را انتخاب کردیم.
🔹
فاکس‌نیوز سخنگوی جریان راست‌گرای آمریکاست و مخاطبان آن از نگاه ترامپ…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/465376" target="_blank">📅 22:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465375">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">شرور مسلح ایرانشهر به پایان خط رسید
🔹
فرماندهی انتظامی سیستان‌وبلوچستان:  یکی از اشرار و سارقان مسلح تحت تعقیب در درگیری مسلحانه با مأموران پلیس ایرانشهر به هلاکت رسید.
🔹
این شرور مسلح که سابقه چندین فقره قتل، سرقت به عنف، زورگیری مسلحانه را داشت، با فعالیت در فضای مجازی نیز اقدام به قدرت‌نمایی و ایجاد رعب و وحشت می‌کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/465375" target="_blank">📅 22:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465374">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAjnks3c3AHSJhPWy30BHnSkGoLFE6ki2pb2VMUqojS7_jDUEH4fkuVf1K7PAHYlq0TjB7rAsCDSsLpNjd_MOExdYRUshuRisTBBt0Grsgwcuy4vnbJnkCrKt0qCFEzHR1DbBVvtV-ilNwXC1abAtTf3cp8hFRkzyeklOLjBXjVw95A5mYJHFi2l4Zt5gBpopTICTXJcjeHq5IJ8Ua0A8fSBHdCaTB44L63mWQg8gHUaHSyFzISxOqSLPQbhou0wMjVFDzV62sW2U_Eh0OkaAmBgSGBjqvY3H2bYt2Ux166eLZq4IfSJU_R9xC0aC3mhqYVLmAKxBo0U_82_K0chKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو با دعوت رئیس امارات به این کشور سفر کرده بود
🔸
دفتر نخست‌وزیری رژیم صهیونیستی در بیانیه‌ای گفت که نتانیاهو به دعوت رئیس امارات، به این کشور رفته بود.
🔹
در این بیانیه آمده، این دیدار بر تقویت روابط دوجانبه و چالش‌های منطقه‌ای متمرکز بود. رئیس شورای…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/465374" target="_blank">📅 22:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465373">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a05abcb121.mp4?token=ucI82pO3O9nTefP-ieaSkqVNyEI1bMcJ3NOnMMuQIFR2jImTf7afeDhOtRe8BI4GfLJ9ERyxujcBaM_o1tbOjm82K22CQr9PZFXvhE0LwBn3IvvfZmpz-bZk6OFHJdJJnSduhyOzBZjbTbTGIaupNV2V-s0YbywCowEKIijhYZQCCyzmnh8mXGwg-f8t17-cy4pybx-AKTe59Udg5ojsWy0zJWjJ1UELDv59v1SdP_PIXQpDtl4Bru6aPwEn2QIp0jU0vfIB44fnJpYfI8D7szEnQ0pwFbL4OC5e3NFH6CdQT0dOYnx7t7clD4RH8_rRLIsrzG_E5HodhuSB7jOnEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a05abcb121.mp4?token=ucI82pO3O9nTefP-ieaSkqVNyEI1bMcJ3NOnMMuQIFR2jImTf7afeDhOtRe8BI4GfLJ9ERyxujcBaM_o1tbOjm82K22CQr9PZFXvhE0LwBn3IvvfZmpz-bZk6OFHJdJJnSduhyOzBZjbTbTGIaupNV2V-s0YbywCowEKIijhYZQCCyzmnh8mXGwg-f8t17-cy4pybx-AKTe59Udg5ojsWy0zJWjJ1UELDv59v1SdP_PIXQpDtl4Bru6aPwEn2QIp0jU0vfIB44fnJpYfI8D7szEnQ0pwFbL4OC5e3NFH6CdQT0dOYnx7t7clD4RH8_rRLIsrzG_E5HodhuSB7jOnEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: ما آغازگر جنگ نبودیم، اما اگر بخواهند به جنگ با ما ادامه دهند، پاسخی قاطع خواهیم داد
🔹
رئیس‌جمهور در گفت‌وگو با شبکۀ آمریکایی فاکس‌نیوز: ما به توافق رسیده بودیم و چارچوب تفاهم امضا و مورد توافق قرار گرفته بود. همچنان مایل به پیشبرد توافق با آمریکا…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/465373" target="_blank">📅 22:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465372">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIReJkbeU9zCSRxv8Xvd5UXQ3KLYxCuRsVpbsB7LACKtCfHVBfT0pSmaJUlENInCtNI_gT1XXfJly7yvmBD0GPdw3P7hWsqEfD0kF4srfYPH5BMoD5-v1u2O__PD3f0sv9LvmZv8X9_DMFNQElA5Z0kZoMOe-zE4nXoKVmTLa0ecpsYm4bJKuh0lKUmMCbjVDGTBiBAroxELNPz0duDEgI1U2hboFdIeB9RDJ3j80VvlPF3PA-6NLxkI68uBG683Th1HOFEynExkIJUqS5Q6uypcvgD1d_xJMi89qbzBOcHcfP3C4cz6gh3ZtsUaae0V8iXF6WIdbG5ne5WWyQM4XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌اصلاح‌طلبان از تسلیم‌طلبی صحبت می‌کنند یا توافق؟
🔹
مرز میان «مذاکره» و «تسلیم» را باید در یک نقطه جست‌وجو کرد؛ نسبت میان امتیازهای داده‌شده و امتیازهای گرفته‌شده. مذاکره، فرایندی متقابل است؛ هر طرف بخشی از خواسته‌های خود را روی میز می‌گذارد و در برابر آن،…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/465372" target="_blank">📅 22:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465371">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">انهدام مهمات عمل‌نکرده در ملارد
🔹
سپاه حضرت سیدالشهدای استان تهران اعلام کرد صدای انفجارهای امشب در شهرستان ملارد، مربوط به عملیات فنی و کنترل‌شدهٔ انهدام مهمات عمل‌نکردهٔ باقی‌مانده از جنگ آمریکایی-صهیونی بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/465371" target="_blank">📅 22:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465370">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkXqVmEn5_LviFweuYOHfXOJ-1exQBbYLrY7SLgrfnexHKKC_tpEs_rhislflvCV5GKq7Rz7DDU09RoJbXc716r0Zo4QpD5qs2jqdGAO3Y8i1_Ylu0wL-cehtpZUZQFgjkAob1Tl9Ssw44TE98xMswwvuOtE7nUasxGxG5VJsij0tDk19NfPjid4EFHTG_FcRx9L27DSZBBI1eGYN46UT8c6S7e46AJpR1n9196pFdBTFd04nis6QHObLrNd-flnivdjgQqCcVbacjix7FWNE4mSo6eDtq_1T0vaa17Hxl-M4H0WwDl1wCjegT-EdSd7MfTsZuDrCSbEKhFa8jnGBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
اخبار امیدآفرین امروز را یک‌جا بخوانید
@Farsan</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/465370" target="_blank">📅 22:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465363">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ftGBSg82TZdc4wd0Xu6X-GsQE_SXSDXvDmMytdNmwTo9hsLpZSOJKlxWQ0htXY2y6WvgcT-7Jk6bQu2sfZtFUvULstifXrIOxFQWBLmcVDFfuLNrN7f-SHWu9oEcsdyLEVuwL2zXZ-U8vWKghMeO0UOT5rV2GDyaw2PgAXfOwM4L7eVs96ise9XBzJddCTNQ5lNEp_1_mp99LBo38TfQrWT91zR1cwXQ_nkx1cNwBgCQTN0TDgc0QO-pFpJTEVCS3yCLz9AKBeCzUqjPREQLelbRYP28kGzd6-H6zae52EKvyUwJMQ-QGacP6nUVxZEgXCMznGdEum9tek5bCXXPzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aiwAoY2DRr-qFUaag8JLkuvexjKxqvVSebDoQovVMBA-czsY0jF6ohIQ-qim1CLVe47bPp5UvVSfdkumjIHw8TaWYDZyhEnIMQaB8iNjWtcv7-_0Vp80WNdXjPlfvQ_nA4Si-4gsOsnnmlRM3e3GWthCmDQhkepLX9DAHDyph4s_cYIpbQrVFMOGBq7N5SYbl_MeT45vhFzYXdf23ZVfRJy2hdvAHuXMXNjM_lpJgejHhdV9IMeHnyqeETiUzeXjQ0Nx8z4bislB8gY2SXccH8k7_cMC072QKvLQeAxQEe_JSfr2cKYCvPHnd2rOK9nfY8Pp1mqJcAmVbnV0b8Mm5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r28Ke_dWRHuOUqMVB2WP4ymOd5RDdqg29FV3G88neDaXM1YI3htth7kw31xNnyKEyRgaCLeSVlDse2i7jACbN6Oa8qlrQj2GBQMykdlM94UvkCpS1jE6atzsqkyQs-sBMxIyqZFkHls43dnjpQHFnc-JRga90vdYrXZ2RzEHsGG_F_ZxnV4B0shbbZMyYO1haPLtsWKuRuH7MRXjr_gNCT-nli4oBUYFlB9q4MDrW055KuTt9q2LCFZf65zDWkJs8Fx5Sil0WAyb2-nyESNn3nGgLLJwfgWCTCFBVlUV1NDx7NxEgwSxLRl6HeEgtFZ9v4OAlEY7VlUzhSXJ0Qhrbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oMmi0NyMYjQ117uI4WY1tKq0RgKfwXnYeRp_1aGHkPVBnZIsHdUiI5AcOrIvinXWg67xn-YjVX0b1havJXFrG_Ofj_iVTX77GlU-I0C90SF1ut8VoHaHavWx1wmck47L4y7FjvjMk3_DwLsfL591z7GFXiM2hrMAPmfP-Rzgiwd2UJsec9ibdcS-FgFwHZAJcrSNAeq9xOIPCq5B3nGwe8_ZZU_Tq5U882tqyn98iKr0yNZ6_EAPm3EDBMDxXgGIzzSQaRDzyrlIsPua8pSeqf2BB1aRfZu3q15S1Ncm92tlfUqSrZ0wKv0O9SoWqI0wJCzaMYAwKaRioJ6poQFQUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nwKAcHSZkMtNaMFeI4m0eNdsYtRd2kXB7soiuNvehpa7_82xRM44EHY781tEaWOL2aa3d6LhD_ZpsmFe9FuZ-2rD8PV4pJG6bF5J804fUJyXIZ1dKEL2TlJ5okiRGISscTvurNYJAoepDfveWEoRqH_56gpnjw4BCa6Ozc8qtwRp8ZkG88nWzubc1Kn0RWSdGtddtJ7YKSKDGvyC1_TQTzPQXf4Txtws0wCwYTyWzGrJwjw4GQ-XrdOkEsHze1-vjrJe38dxtHRmi4GC883WY9UAOw5pftum6AHq1TKi-LHJJ7D71X0xCNpim5_LDNTyAFusnjQ7ULRQoa8xHgiNOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DpSFwzJMVBp9JTe13Dn7LGv1LFrCy_QBiLkITEa2jPNbd-5vd0T0HGMNEGBQEY1eepLY6WOPu0RaYDHDQ8flaC_kjBsAyPQPmM0M-43JZS6DsR8lsBatwwmNRLTho4kM0G7tUyqoBt1GMD7pnC1RPGIb6mupV417CkHl8z8TRt4bPTF-7ZE_G_gnHQL5qPtplWeBxkXkuxATMNZH5NjW6CiEDExoDT2xIE3mZvIjAF17q6uvYOFGNJmJy2eG10Po8v8XXFLq7Ahk_Q9kJTSVNWHLeu8v2QmWghVRDtQ51DVKSuoHN7V5oejWDidbZEW2R58-ROpWyMnkDzhPi7fk_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FfQaNL47UJW0mNUnRi3vhOYpPVCbtc1d_oLttczd8fgxEWzo5n5jo9HsU-OWp6wSBHH7Tn1YAyIgRsuqOgZWz7kjYHs6NWP_Pe3qSCsMy2ArNG9F1nnmPCRui8QExb2q3y9vwoWq8wq7SWPJYMOmMKns8w4n_AqjzmR1pSH7BLDkV2sAm6WzfelzB39BuQ4jHniIPeW51r8m24AtsPZn5YfiwoK8MX0ZqjtUbCMO3iY6vcfYstNvky9P3L5e4k7toZZLIAjFnrKp89_9yRgqYkMsixrQshOWQl4lSBTEymx75SM19i-rq3KN4dLshSfvOtIg2AieuGdK-LJsWiu5aA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📸
نشست خبری کنترل پروژه فیبرنوری
عکس:
زینب حمزه لویی
@farsimages</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/465363" target="_blank">📅 22:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465362">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔸
از ساکنان
منطقۀ ۱۲ تهران
، میدان قیام تهران هستیم. حدود یک ماه است
کابل تلفن خانه ما به سرقت رفته
. با تلفن گویای مخابرات درخواست تعمیر کردیم،
مخابرات اعلام کرد کابل ندارد و باید خودمان آن را تهیه کنیم
. هزینه حدود ۲۰ متر کابل نزدیک به ۵ میلیون تومان شده است. سؤال ما این است که مخابرات در حالی که آبونمان، هزینه تلفن و اینترنت را از مشترکان دریافت می‌کند، چرا باید تأمین کابل و تعمیر خط را بر عهده خود مردم بگذارد؟
🔹
ما
رانندگان تاکسی‌های اینترنتی
اسنپ و تپسی نسبت
به پایین بودن کرایه‌ها
در مقابل افزایش شدید هزینه قطعات یدکی، تعمیرات، سوخت و سایر مخارج
اعتراض داریم
. بسیاری از رانندگان از بیمه و حداقل حقوق و مزایای کارگری نیز برخوردار نیستند. خواهشاً مربوطه رسیدگی کنند.
🔸
از شهرستان خاتم استان یزد پیام می‌دهم. خودروی من دوگانه‌سوز است اما در طول ماه فقط ۳۰ لیتر بنزین ۱۵۰۰ تومانی و ۲۵ لیتر بنزین ۳۰۰۰ تومانی سهمیه دارم.
در مسیر مهریز تا خاتم نیز با وجود دو جایگاه CNG، هیچ‌کدام فعال نیستند
. با این شرایط، تکلیف مالکان خودروهای دوگانه‌سوز چیست؟
🔹
بنده ساکن
نی‌ریز فارس
و سرپرست خانواده‌ای هفت‌نفره با پنج فرزند هستم و نزدیک به چهار سال است برای
دریافت زمین در طرح حمایت از خانواده و جوانی جمعیت
ثبت‌نام کرده‌ام. در حال حاضر در منزلی یک‌خوابه، قدیمی و نامناسب زندگی می‌کنیم که مشکلات بهداشتی و خطر جانوران گزنده دارد. با وجود مراجعه‌های مکرر به فرمانداری و ارسال چندین نامه برای قرار گرفتن خانواده ما در اولویت، تاکنون
هیچ اقدامی برای واگذاری زمین انجام نشده
است.
🔸
با توجه به شروع مهرماه و زودتر شدن ساعت آغاز به کار ادارات و مراکز آموزشی، از شرکت بهره‌برداری
مترو تهران
و حومه خواهش کنید زمان
شروع فعالیت مترو کرج را نیز مجدداً به روال سابق برگرداند
. در حال حاضر ساعت آغاز به کار مترو کرج از ۵ صبح به ۵:۲۰ تغییر کرده و این موضوع برای بسیاری از کارکنان و دانش‌آموزانی که باید صبح زود تردد کنند، مشکل ایجاد کرده است.
🔹
بنده از شهروندان
زابل در سیستان‌وبلوچستان
هستم. وضعیت شهر از نظر قطعی و نوسانات برق، کیفیت نان، معابر، فاضلاب و زیرساخت‌های شهری بسیار نامناسب است. حفاری‌های مربوط به لوله‌گذاری گاز نیز در بسیاری از نقاط ترمیم نشده و چاله‌ها و نشست معابر باعث آسیب به خودروهای مردم شده است. با کمترین بارندگی، خیابان‌ها دچار آب‌گرفتگی می‌شوند و طوفان و ریزگردها نیز زندگی مردم را دشوار کرده است. لطفا
مسئولان استانی و کشوری وضعیت زابل را جدی‌تر بررسی کنند
و برای بهبود شرایط زندگی مردم این شهر اقدام فوری انجام دهند.
🔸
معاونت آموزش وزارت بهداشت پاسخ دهد؛ در
فراخوان جذب ۲۲ هیئت علمی
، برخی
دانشگاه‌ها داوطلبانی
را که هنوز تعهد قانونی خدمت خود را آغاز نکرده‌اند،
از فراخوان حذف می‌کنند
؛ درحالی‌که در متن فراخوان صراحتاً فقط افرادی که از انجام تعهدات قانونی خودداری کرده‌اند، مجاز به شرکت نیستند. بسیاری از داوطلبان هنوز امکان شروع تعهد خدمت برایشان فراهم نشده است. اگر این افراد امکان ثبت‌نام ندارند، چرا سامانه از ابتدا اجازۀ ثبت‌نام و پرداخت هزینه را به آنان داده و حتی درباره شروع تعهد خدمت از داوطلب سؤال کرده است؟
🔹
ما از
پلتفرم «میلی» طلا
خریداری کرده‌ایم، اما اکنون به‌دلیل مشکلات به‌وجودآمده، بسیاری از خریداران قصد فروش دارند و قیمت اعلامی پلتفرم برای معاملات فروش به گفته کاربران، پایین‌تر از قیمت متعارف بازار است. با توجه به نگرانی و ریسک بالای کاربران، انتظار داریم مسئولان و
نهادهای ناظر نحوۀ قیمت‌گذاری و معاملات این پلتفرم را بررسی
و از تضییع حقوق خریداران جلوگیری
کنند
.
🔸
ساکن
مسکن ویژه تهران
هستم.
واحد مسکونی ما در جریان موشک‌باران به‌شدت آسیب دید
و خسارت هر واحد بیش از ۸۰۰ میلیون تومان بود، اما
شهرداری فقط ۵۰ میلیون تومان پرداخت کرده
است. با وجود مراجعه به شهرداری مرکزی و بازرسی شهرداری، نتیجه‌ای نگرفته‌ایم. من بازنشسته‌ام و دو فرزند دانشجو و دانش‌آموز دارم؛ با این مبلغ چگونه باید خسارت خانه را جبران کنم؟
🔹
پس از افتتاح
اتوبان شهید شوشتری
،
ترافیک حوالی میدان مطهری به‌شدت افزایش یافته
و عبور و مرور برای شهروندان بسیار دشوار شده است. به نظر می‌رسد تبدیل میدان به چهارراه می‌تواند به بهبود وضعیت ترافیکی کمک کند.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/465362" target="_blank">📅 22:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465361">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9C-an_YElliyxmlW2DwojOqoWLqtyq_7GWCD_l5fUtEVqPepca2RjPbMEeyUTjAsbc-YUkfGaBqA_jfkBte7Qzgwhh7llPWnEb5WmvZoMfVDVFJRUop8ARu56YWMk7jfpwnbEzeQOlTgbsqmZaUaaheoe5x70Hab1nRVf15Lwqvurr7A4seiuVMEufFtKE2XvtfPic7ucb9QilrExfcKV6Oupwxxy4XfiTmlT5PG8Ac3_Hl2rbqt6SuUg-degNloZvc3wR03WUrRAn0WceZ6msHzAR04tbSaNv_zLUvXl2WF_W9r35h_MnUqjuj-8oUPw-GgzxMtty_war_3o90Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندۀ قرارگاه نجف سپاه: پیشمرگان کُرد مسلمان حافظ امنیت غرب کشور هستند
🔹
سردار کریمی: تداوم امنیت پایدار در استان‌های غربی، مرهون تفکری است که سازمان پیشمرگان مسلمان کُرد بر پایه آن شکل گرفت.
🔹
ما وظیفه داریم با خدمت‌رسانی صادقانه به مردم این مناطق و زنده نگه‌داشتن یاد شهدای والامقام پیشمرگ، راه آنان را با قدرت ادامه دهیم.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/465361" target="_blank">📅 22:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465360">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d872812b7f.mp4?token=Dw-1Y7BVgcHyGNBW94RhdTzcgXy2YqNh6lNmaiGfis30NImvBsXiI_3sJEVQhKUkX40wOEFqOdf55p0IiYRc44Xe4RY4JEWdTAhKF1N2pVg3pcOPkmYV9QAmlByvGAXwtIMqG_X2sBdnL6dYDwqcKmuPtoMkzVx1J9v6UcV_NQH1E2YBN89ZdehoOvah-osd_fc_R4jYAz7nZF-ROEX1JULj8eq3sF2ypUYISp0j8AAOcoT6iGijE2K8QT9U1eVncrlNrYMmrhfRupq6pcPo_yibf4pGEpBVamsW_aZ0rK7P_Wq_EjZ2O0ZvqesLFz1-t9B4fY_QyGsfTkW380MkMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d872812b7f.mp4?token=Dw-1Y7BVgcHyGNBW94RhdTzcgXy2YqNh6lNmaiGfis30NImvBsXiI_3sJEVQhKUkX40wOEFqOdf55p0IiYRc44Xe4RY4JEWdTAhKF1N2pVg3pcOPkmYV9QAmlByvGAXwtIMqG_X2sBdnL6dYDwqcKmuPtoMkzVx1J9v6UcV_NQH1E2YBN89ZdehoOvah-osd_fc_R4jYAz7nZF-ROEX1JULj8eq3sF2ypUYISp0j8AAOcoT6iGijE2K8QT9U1eVncrlNrYMmrhfRupq6pcPo_yibf4pGEpBVamsW_aZ0rK7P_Wq_EjZ2O0ZvqesLFz1-t9B4fY_QyGsfTkW380MkMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ۲۱۳ میدان‌داری مردم ایران هم فرا رسید
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/465360" target="_blank">📅 21:58 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465359">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAkQ9vAtX1CA74-Y8USK0d58mau6S1vbOJUNtR4hIA8mfMmlz1KP_TQ9m35QP7yp5MG0sNGrBsG1W53tw9KuN_m9tFSfdohIGidpFVgIRrQ23sMtYjlL1NT0DqTmDyyoGkI0Y8leZgRuUXnUAPcQnkm2__axHz0X6BYEOaQJzK6wc4poioKn1tgc8eQdEXzADagQvLvjRxNhLar05fvkqCKEgn2XJkJpqdG7pTQqRhVmeFw2H1TjpGuLnEA4m-JJAMrSiRMFtpEbH3YeiOi378wrQcS9tbWA_mmpKvxWkadXv7B2xNk8YkegBiQ5Udg5s2n8VPEx5Ig9FiG-l58e4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌تیم قلعه‌نویی حریف روسیه نشد
⚽️
روسیه ۲ - ۰ ایران @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/465359" target="_blank">📅 21:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465358">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">زاکانی: طرح «تورم صفر» با ۱۲ قلم کالا آغاز شده و قیمت این کالاها ۶ ماه ثابت خواهد ماند
🔹
برای هر قلم کالا متناسب با بُعد خانوارهای تهرانی سهم مشخصی تعیین شده؛ برای نمونه، هر فرد می‌تواند ماهانه ۲ کیلوگرم برنج با قیمت ثابت خریداری کند و خانوار می‌تواند از میان…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/465358" target="_blank">📅 21:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465357">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhYYrpJQh_esvW48x1GI-C-sPHuhPnEpRm8Ows47VJDncq1ylVJVDkiI8NylfcHhCm2u8uuxLnJogGq0vfp-37nOGhCBjMBEKWJElK0kXd1-K657JGzIRlXk6Z-h71M4iA6lQbs6o67aVdhH4F_Br7D37vD9fsQicQKeb2u5ZDD7J9dlyslJccHf1ZMYUk1RICOdje3j3VenIdv8U64bU-eJMiOCRN3fOYQlwttf_E5Kja-KmTakXmNLAl8SGBrb0BU2o8TRNfokd1Ho-a0SC0M84NZy80cJFPxbj7d0R-uTP4GceBRgmhxFMsAzLkCfcruOAViKUGX_Obm2ewl8nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
۲ واکنش خوب دیگر از نیازمند که دروازۀ ایران را نجات داد  @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/465357" target="_blank">📅 21:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465355">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af299db612.mp4?token=AT0joubvvU89nJKYGPV4xI4aJ_ce53zYTTZ1PR1yB65uvY-k9Yr-AuiPywe2DGo-NelELpgU7684W0k8fYZ841P47RXFqy-rkepvxNgqB4TDyWIKNhzl6NCsixgl-LMBwSxzfK0ZEeAVEKgQfaGhbEUl053czvFpCnTtOAnWe0gC9iZLfp2DnIMijH3GdEys8ilchG4nHl4ugT-BoD6bO9nuwPXIQjbvvM2bkLMBCM5B3cqYpdWEFBURbX1jy3hxVo-J3hsx10CefWlkydb3hG9LS2HpwHd1xrYDylv9YyQtIjqqZegILmUW2EAKI7bWOw_QWY9yOB3PMpWhBtUL1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af299db612.mp4?token=AT0joubvvU89nJKYGPV4xI4aJ_ce53zYTTZ1PR1yB65uvY-k9Yr-AuiPywe2DGo-NelELpgU7684W0k8fYZ841P47RXFqy-rkepvxNgqB4TDyWIKNhzl6NCsixgl-LMBwSxzfK0ZEeAVEKgQfaGhbEUl053czvFpCnTtOAnWe0gC9iZLfp2DnIMijH3GdEys8ilchG4nHl4ugT-BoD6bO9nuwPXIQjbvvM2bkLMBCM5B3cqYpdWEFBURbX1jy3hxVo-J3hsx10CefWlkydb3hG9LS2HpwHd1xrYDylv9YyQtIjqqZegILmUW2EAKI7bWOw_QWY9yOB3PMpWhBtUL1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش تماشایی نیازمند مانع سومین گل روسیه شد  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/465355" target="_blank">📅 21:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465354">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80bd57de5c.mp4?token=AGkYTGdr7r2iNKYLGNyETmE1uupplGm1Fz49IS1lRJcGkspSUOxMMyaH2yzPfY_8YMQ6lgfIh1YgjWvrDp5mIXWYZ1mSApUi01FZ3fAJUIxd0Aui1cPkXwnjMy8UA0fIgkuzIMTgHS4eDSFWMqt9IqNzV-CslaZz70fpoPJi7OVd_-6vsSJxcBCQaRrWehWmDg3whf3KupRjlf4dX1TxhbluV5MIVWJr7yjZz72165424AuH9e6_J92A4-9I0eKZRxwt_DDnaMQqXvjyaxSZdjHue8_1mFAd0KmkVWk6L2NJ-Z1zu8PsC0TUuJq5YbqGqabcBAoULZftw2OmwpwZAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80bd57de5c.mp4?token=AGkYTGdr7r2iNKYLGNyETmE1uupplGm1Fz49IS1lRJcGkspSUOxMMyaH2yzPfY_8YMQ6lgfIh1YgjWvrDp5mIXWYZ1mSApUi01FZ3fAJUIxd0Aui1cPkXwnjMy8UA0fIgkuzIMTgHS4eDSFWMqt9IqNzV-CslaZz70fpoPJi7OVd_-6vsSJxcBCQaRrWehWmDg3whf3KupRjlf4dX1TxhbluV5MIVWJr7yjZz72165424AuH9e6_J92A4-9I0eKZRxwt_DDnaMQqXvjyaxSZdjHue8_1mFAd0KmkVWk6L2NJ-Z1zu8PsC0TUuJq5YbqGqabcBAoULZftw2OmwpwZAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صحنۀ مشکوک به پنالتی روی دنیس درگاهی که داور اعتقادی به خطا نداشت  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/465354" target="_blank">📅 21:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465353">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745688ee9b.mp4?token=qGpoM0ypPCz4HggjUkB3l4VrYZKPAZnMBPLyZiyZUJP_iLNYFOBZcn4OQO1tUEJbvnnAJzXd5soojCXfJKedAO8QzuBsvDJBpsNULAD636YovBIcpoCdl8ChfcUC45HQZo4NHpRaQh_KoL7a8BD5uC51Jgk1oft3N8wZvh-u73_5aa0pcBM3HsJYJuyCBKJKHmxdN4YenG4IHPGJbTUitiEhicoQwqeKmvgkLYzs5yzmicchIv38y5eHQ5zv5HbvkrKjPjXBnsuw83QG1P1soQHhEn-uy1F5lLATQjLjU_PMN1tAEbs8U-BB3B1jLV28OffJ_lAJwQ6kCO2Q_kRa9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745688ee9b.mp4?token=qGpoM0ypPCz4HggjUkB3l4VrYZKPAZnMBPLyZiyZUJP_iLNYFOBZcn4OQO1tUEJbvnnAJzXd5soojCXfJKedAO8QzuBsvDJBpsNULAD636YovBIcpoCdl8ChfcUC45HQZo4NHpRaQh_KoL7a8BD5uC51Jgk1oft3N8wZvh-u73_5aa0pcBM3HsJYJuyCBKJKHmxdN4YenG4IHPGJbTUitiEhicoQwqeKmvgkLYzs5yzmicchIv38y5eHQ5zv5HbvkrKjPjXBnsuw83QG1P1soQHhEn-uy1F5lLATQjLjU_PMN1tAEbs8U-BB3B1jLV28OffJ_lAJwQ6kCO2Q_kRa9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ رهبر شهید به توهم تاریخی ترامپ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/465353" target="_blank">📅 21:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465352">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a9d2ed720.mp4?token=hP8CJFXeQetsfctT5XSg-Cw56YNPCEj4bzY7uhmVHxqj7nMlY_17b4G2XDgsJyoRTKbyNwbwc4YeqLksC4w91v26wqahmNU5V0rWwBmfvvtkz7EvMLonWlSSFo4KpLwOsDXd6Dlx9_dBmew8TNo1Ig7ktbJ8Uc3Z2q7gAX9OlLiNh5ZZ65b65SgiBErMHNRSHFP8SNH115fyKbDBHIeH2NS5mHyfF56pT4oYvShPx19I6vd8JXS4zKxN_o_-qFIOqiHaz2EHitllhXyJyTr43mOyHTaBzZsMWefYUSCQJ5HSvY_IY0EqoseM1QInP0sRNDbV-HSLgZa9IJkf5S2DXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a9d2ed720.mp4?token=hP8CJFXeQetsfctT5XSg-Cw56YNPCEj4bzY7uhmVHxqj7nMlY_17b4G2XDgsJyoRTKbyNwbwc4YeqLksC4w91v26wqahmNU5V0rWwBmfvvtkz7EvMLonWlSSFo4KpLwOsDXd6Dlx9_dBmew8TNo1Ig7ktbJ8Uc3Z2q7gAX9OlLiNh5ZZ65b65SgiBErMHNRSHFP8SNH115fyKbDBHIeH2NS5mHyfF56pT4oYvShPx19I6vd8JXS4zKxN_o_-qFIOqiHaz2EHitllhXyJyTr43mOyHTaBzZsMWefYUSCQJ5HSvY_IY0EqoseM1QInP0sRNDbV-HSLgZa9IJkf5S2DXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چهرۀ درهم امیر قلعه‌نویی در جریان دیدار ایران-روسیه  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/465352" target="_blank">📅 21:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465350">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SeKpf-x4MC2rnv8_-5KvnYPTIVfFjMf-FrQ3uCCG7LNfLyOEGv2aPQRiR-R3r7BkMYOPpf2eAdMJD1sTlaOyTyO9sPRUlgPcwqzJOpgrGqKW-X_7te343nTQekGTnt5eyMlK4B9Bw0jAPh0PSJYKyU_ik4Mi2jt5O0dHQBhPBDDEduFSJcIUjHhHq50Y1Hv_VuT-zXqYA_zHcvfCHd6re7LCr5RZxjbTMCjotG3JrYxg72bJQiNJPA_3TSqz6bdxUojzbbXMTMJQLGJ3i_3slSe8F62Sx5yD-0YSyN6cen33QCgk43b3vQHlsQaHxrSfmo-0Kp3RO5gmKfn-cKxAqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qPyTWHyYIFwjCovBETlXksOGgM4NN8YRMFbZpiKTlS-myLcrPpXNb16cEMrhanBgeSyqZVFWjskit8z0tFTBh93eIAM7QU28J2wjAY15OVxBVQWGBa35HLbR2K6d9x5soapVGLizhHnjH6mufQMTw1ZSh6Jriyk8BHWrXT1Ps79inJMC93s2cLB2L1fpJbtwP8GbBZfMJaLcoGWCBzkhrO9kUbXBEN1Pze7YIpbrrydk2rm7J1ro2gOITBWrxwejEwcpob7NvOMLmSVpq0CJckFTkRIDYZ2ROcBVuXU0mImk5_KZYXEuJPkB3kgJJZgzjAU7oT4_nNGFywHm3kR2zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایران با ۸ طلا در ردۀ هشتم بازی‌های آسیایی
🔹
در پایان روز نهم بازی‌های آسیایی ناگویا، کاروان ایران با ۸ طلا، ۱۵ نقره و ۹ برنز و مجموع ۳۲ مدال در ردۀ هشتم قرار دارد.
🔸
رقابت‌های کشتی از ۸ مهر آغاز می‌شود و با مدال‌آوری کشتی‌گیران جایگاه ایران بهبود خواهد یافت.…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/465350" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465349">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdOYFLXpo3xLH35JZ3VyDUtlnh360R__Qtv8J7SKTmXVioCjZLusL5-fqYiKU5Bm09JEyddOZDsPHaVqGWxQAmV3j8kAJgQhbwrFZeryUZyWIKDc6_RvJjB-kxMeM0RctYivuTsd-dF7lAabcU7zl7lbSGvTtyFl024YojTV9WwftnoWWRBsbC27W9qxrARxPGP6qLhwFBIKXppVGfURDT98brPFGAgl_HQFeA7wrAH9-7hBEIo2liq8AEGPty5X0R4Dojd9DY3gwUqTRYOyTvM6doQcz7_4qEVInpUtxVCf4gGcvf3s5C4F9iOpPB9UiR82_iqTntDXs6_4raRjDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا ۱۰ فرد و نهاد را تحریم کرد
🔹
خزانه‌داری آمریکا ۱۰ فرد و نهاد جدید را به فهرست تحریم‌های آمریکا علیه ایران افزود.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/465349" target="_blank">📅 21:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465348">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52bcd44b72.mp4?token=UJQnFtmqAzTQt31Q9KmiyQewt7wBF9XPEEVwWRy1KGLm6NSsk6n7GVloyhl8P7tYy6Sm7gGGzS1leGdc0memweTV0hdoOZWGECNCykCXXY8zjx-I4pnqpkw7Za5puAwFjpp-gPXkp1AQs-s6JUjDcAdFx9fIBjBYyBOAh06u38YBqKfVpQ60hmz77JYmyuKBA1S9yLLeKBGHmeFXULbxAnHzFPzYzOWl8HbFsZZttqbUmwAdyDlxb5UpTRwAsWPfa2E-kVu1_FSEc8Im-iYqKpxvgHf9sbXJ9Fc6UmiEzrfle5et19JKM_q7dll2Ja0OXErReZZwJUwuK-DFF4Jm1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52bcd44b72.mp4?token=UJQnFtmqAzTQt31Q9KmiyQewt7wBF9XPEEVwWRy1KGLm6NSsk6n7GVloyhl8P7tYy6Sm7gGGzS1leGdc0memweTV0hdoOZWGECNCykCXXY8zjx-I4pnqpkw7Za5puAwFjpp-gPXkp1AQs-s6JUjDcAdFx9fIBjBYyBOAh06u38YBqKfVpQ60hmz77JYmyuKBA1S9yLLeKBGHmeFXULbxAnHzFPzYzOWl8HbFsZZttqbUmwAdyDlxb5UpTRwAsWPfa2E-kVu1_FSEc8Im-iYqKpxvgHf9sbXJ9Fc6UmiEzrfle5et19JKM_q7dll2Ja0OXErReZZwJUwuK-DFF4Jm1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل دوم روسیه به ایران توسط گلووین در دقیقۀ ۳۶
⚽️
روسیه ۲ - ۰ ایران @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/465348" target="_blank">📅 20:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465347">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9MXUuiPNFO-GeNyLHYbcaoFcIYSx8p_yJHsrt_MWyh4pf3SLkKRkEKxOnQ1zzTvfbjHL-6-txDA37r_fu6k0yWbiTQRUEXbOOItbfB-MZO1dIcyBsUkvbitQSEfY-qYZTKmVcYI2BK6ZecLAwBrReQw1d1ttdIYqfvzmKplWY5UUAryUHaqdg8C_SvC0ab5k0162ZtJmGhpAq7VDrtxEhjqNYy_hgUnCqdEaewaMPGRPVCHwpRBO7mEjZmxD7aKM2QX8_bEAKCWYk-Wre3HIEg7c7H47JiJ2ySlM_KA1PlGJyFVfFcjIC2_8FSn-C4_hEj27MTPX7SBeW-BvtfR2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک نفت‌کش در تنگۀ هرمز منفجر شد
🔹
همزمان که ترامپ می‌گوید که «قیمت نفت به‌زودی کاهش پیدا می‌کند»، یک یدک‌کش در مسیر جنوبی تنگۀ هرمز برای انتقال نفت‌کش منفجرشده هرمز درحال حرکت است.
🔹
بامداد امروز داده‌های امنیت دریانوردی نیز از انفجار یک نفت‌کش در تنگۀ هرمز خبر داده بودند.
🔹
این نفت‌کش به‌دلیل تخلف و عبور بدون اجازۀ ایران از تنگۀ هرمز هدف قرار گرفت.
🔹
هم‌اکنون قیمت نفت در محدودۀ ۱۰۴ دلار نوسان می‌کند و گریگوری بروی، تحلیل‌گر ژئوپلیتیک انرژی، معتقد است که بازار نفت با حرف درمان نمی‌شود و تداوم وضع فعلی می‌توان قیمت نفت را تا ۱۳۰ دلار بالا ببرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/465347" target="_blank">📅 20:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465343">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd358d0da.mp4?token=lCG4DkHF68WGMhzsq50TpFkvXuXe-3e_Kd8b5ci11RV-2O_nseJmkeEGzWvbBb6-S5uDq9rhc2fuQ0Dqd9qTo_FDOFxUAF6-GQZj-eklBcg0A7ua4Z4-GhLRjTWPKAf2P4zXxpl_kBUpGK7SEYgoLGRYZkuTwMRJhLbiHiuvU9z12BhyWeSBk8SJyxzcbxfYYA1uLvL-BaCpF73o9Gv3-IZG-4PUa4udx-5Eau-N63bfKLakoEhm-iSbulKzQpr6RQISNU7nVeEo6ZeHb_eTixOnUfU7Mrz53ApvnY2iWYt5304P7X_jNedSXb-5ogPqyCtxyPXp1DWwUOPU2hRGIzgOKlkBOjuA9Dtw-Qc2SMj9keNQCXrjfBzyo02FumTXqRiTGt6ROgrmkvm3kK4lym79UOomYPxAMEpmU6gbHlgM5y6NkesLyPEWmVvDjA4N6KBU_l5VSiVdqibbG2lqfCHvdUb1q7a703gJDIdxi79X-Kh-lH5x0b0CEnX4v6N-LzVJ4vZZK_6HM2scD_UK12lET38TzgE2h1frSTxDWNctiBsCVQWwAyFndxMMzXTHWv-6CGATMqOUULex1MWu9yB93Ip7r42OOFrqySwbyIUR4QvAE-XNSxS7B-yWCLhLlwbPZXuRyRDowIiOqjDqVHz0XS4TffGrssAVR3LIA4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd358d0da.mp4?token=lCG4DkHF68WGMhzsq50TpFkvXuXe-3e_Kd8b5ci11RV-2O_nseJmkeEGzWvbBb6-S5uDq9rhc2fuQ0Dqd9qTo_FDOFxUAF6-GQZj-eklBcg0A7ua4Z4-GhLRjTWPKAf2P4zXxpl_kBUpGK7SEYgoLGRYZkuTwMRJhLbiHiuvU9z12BhyWeSBk8SJyxzcbxfYYA1uLvL-BaCpF73o9Gv3-IZG-4PUa4udx-5Eau-N63bfKLakoEhm-iSbulKzQpr6RQISNU7nVeEo6ZeHb_eTixOnUfU7Mrz53ApvnY2iWYt5304P7X_jNedSXb-5ogPqyCtxyPXp1DWwUOPU2hRGIzgOKlkBOjuA9Dtw-Qc2SMj9keNQCXrjfBzyo02FumTXqRiTGt6ROgrmkvm3kK4lym79UOomYPxAMEpmU6gbHlgM5y6NkesLyPEWmVvDjA4N6KBU_l5VSiVdqibbG2lqfCHvdUb1q7a703gJDIdxi79X-Kh-lH5x0b0CEnX4v6N-LzVJ4vZZK_6HM2scD_UK12lET38TzgE2h1frSTxDWNctiBsCVQWwAyFndxMMzXTHWv-6CGATMqOUULex1MWu9yB93Ip7r42OOFrqySwbyIUR4QvAE-XNSxS7B-yWCLhLlwbPZXuRyRDowIiOqjDqVHz0XS4TffGrssAVR3LIA4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایستادگی و انتقام، شعار رزمایش جان‌فدا در مهران استان ایلام
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/465343" target="_blank">📅 20:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465342">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSZ56kJ2MaatbqRHTnPfh7txOL3P9u83bnx_l8ylTJzfDg5W7IQwfYoo8osYlaRhUwgghmmRGqINgx855ahmIHrIvQ6UJpo-_9WZ4ShdLKoobW4y7elagG_mmYAvZaItqHs8P3h8lLigsWWdTBdb4GHiiRL05QfI_xOg89GjyJpcwCEJ5uoWSchmUod4t1MEFvxIdhYO5Fk0dGj4ZWlonAZZwtBiqjERD-_8tinRQF04hUCUx2ir2jvKVvh5PBT2hLOc04tTPbQsGQuE_cE7s9QMivbl1ae_C8rKH6mdf3HJSdPG0EjYN00St1t7-9JKfZ1etP0n7AoBuRxlwMJpTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای‌عالی امنیت ملی: ما شروطمان را گفته‌ایم اما ترامپ قادر به تصمیم‌گیری نیست
🔹
ترامپ در باتلاقی گرفتار شده که نه می‌تواند مذاکره کند و نه می‌تواند بجنگد.
🔹
شروط ایران به آمریکا اعلام شده، اما ترامپ قادر به تصمیم‌گیری نیست و آمریکا از سر استیصال در…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/465342" target="_blank">📅 20:39 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465341">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f59ca0cf8.mp4?token=JRFw75VIPHGOtRnW_mFKxL8OlKq37Fp73je6pT_DX5VtsnTWCdiqXtCU-NjdEjIveUE2Dly3LmqqVppbalyO7JTXxJplQsyk2LJin9ElrpqzdpGNo9jphNRMa-sh0SUMVXE5jfLR55DxH2dgMk-OE6ko0TjjPOs32gRXSXuwJBn7vqcwhx2ld5IhCTo4EY5ruFijQJ6PSpaeY98fEOXYF5xhiksDyMnuPwbCfapCVTy-xns3Zbrr_FMNLqv3-H8t_N-yWdUsV0cSSOo7k7VPCmDiwWHWS1yRuKPt4-xkEHBi3ETtVjXnctW36L0tU34I_G_zZJV_Nxe8-7tTti7G5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f59ca0cf8.mp4?token=JRFw75VIPHGOtRnW_mFKxL8OlKq37Fp73je6pT_DX5VtsnTWCdiqXtCU-NjdEjIveUE2Dly3LmqqVppbalyO7JTXxJplQsyk2LJin9ElrpqzdpGNo9jphNRMa-sh0SUMVXE5jfLR55DxH2dgMk-OE6ko0TjjPOs32gRXSXuwJBn7vqcwhx2ld5IhCTo4EY5ruFijQJ6PSpaeY98fEOXYF5xhiksDyMnuPwbCfapCVTy-xns3Zbrr_FMNLqv3-H8t_N-yWdUsV0cSSOo7k7VPCmDiwWHWS1yRuKPt4-xkEHBi3ETtVjXnctW36L0tU34I_G_zZJV_Nxe8-7tTti7G5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر آموزش‌وپرورش: شرمند‌ۀ معلمان هستیم
🔹
به‌طور جدی پیگیر دغدغه‌های معیشتی معلمان هستیم و تلاش می‌کنیم رفاهیات آن‌ها را هم پایدار کنیم و هم افزایش بدهیم.
🔹
دولت در ۲ سال گذشته ۱۸ همت برای نیازهای رفاهی معلمان تخصیص داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/465341" target="_blank">📅 20:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465340">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سارقان مسلح ایرانشهر در محاصرهٔ نیروهای پلیس
🔹
یک منبع مطلع به خبرنگار فارس در زاهدان گفت: از ساعتی پیش چند سارق مسلح در محاصرهٔ نیروهای پلیس در ایرانشهر سیستان‌وبلوچستان گرفتار شده‌اند و صدای تیرانداز‌ی‌های شنیده‌شده در شهر مربوط به این عملیات دستگیری پلیس است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/465340" target="_blank">📅 20:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465339">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYd_QTE1MQUtk2tT-8imV7ckWVQ6ftmok5ynwHHzSZ0l05s2cxsosvw501GkWYSokezpAQj-ocxRpWJELOw_OmldDAjAMon7ELm97WVc0BDY3EBwpqhGb6wZGjK6XFYyLTMPJh6vd2qn1wq4DAofO4obqPaWgS0OsfEPddXFz4Gcq_eZUjk_Dac1EAcl-SIqdkCv-CFF_26JC1JEwdF0y6glSUoX2VSbvHOiLIkhOR8K98R5Ky9EnTzRKVIrext_q5Zpca0f6UD3a17SXkeH5E4b5mJWAoJLYCGDSsGgDzDdpBhDsDP-lMiv8PJQN6urkm6MFpjGssHycSvTCr5QYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مذاکره با روسیه؛ آخرین تلاش واشنگتن برای کنترل بحران انرژی
🔹
در حالی که قیمت سوخت در آمریکا سر‌به‌فلک کشیده، واشنگتن و مسکو دور جدیدی از مذاکرات را با محوریت همکاری در حوزه انرژی آغاز کرده‌اند.
🔹
کاخ‌سفید اعلام کرد که کریل دمیتریف، نماینده ویژه رئیس‌جمهور روسیه، روز دوشنبه در واشنگتن حضور داشت و با مقامات آمریکایی درباره پایان دادن به جنگ اوکراین و توافق‌های احتمالی با آمریکا در زمینه انرژی گفت‌وگو کرده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/465339" target="_blank">📅 20:23 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
