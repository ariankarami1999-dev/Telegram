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
<img src="https://cdn4.telesco.pe/file/rbPGknbRdlXdLSZ2BQX0xP_IHZ1WdynCiMUtgv0oVGdE2m3g2iuQ0oEaqfjWm1NzJErwKEsrX3b3itLmkHU3Eri96G4ZhDU06X4GpAXirPI0G2dHD0-mspK1VXCjvwOAZCpy_goSUyXNNWizai1-f1pdpsFTVPlfNbpDNH7wK9_h7cgxQIE-DTA4v0DVAtoP6lxBOa6kWYZoBRZnMEyCwb3_pY2y1umWpbiW_oGBC-S3M-9awsalzi5dCSFDaHJCOF7M3_XnyiZ2Xvjq7FQXND8WCnLBEo6aeMjLR0GgNlaYD-OcJM1BvpHiCpAsrb9ED-g8mg_8XpEiHHe41JPTsw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.07M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 20:19:53</div>
<hr>

<div class="tg-post" id="msg-690980">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdw7DCuWa-EIu2ijSypHDgEMpQwyWfTcT9bn_5VIUVlf1vfdHJf6QbotaplvPIuYitdOiYjOHkNB1JnVLZD1hMWNYeEaeWZTMZ2sFLWEBxxAl7dJMg5a0ySqe8uZH14Iivrc2mB7CDLk_KbBzuoAGjI7VnDtXwoESXg7q2su1BCBIJVziq6G5awn-3h6vqG1rkS4fuLqH06BrKvsVUkRnl3JvmSS9QqCzUsRUIZGpz1c7haXbym-PNZrPOJ9cEnMBPsk0LtnPqm7ewVcnJ6-5lDii0rtDdZJxodNgZUwXGzDsdfabLG_DPs5otpfQSUfKvc6udnchltZv23YZmmLFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
احمد الشرع،رئيس جمهور سوریه درخواست عربستان سعودی برای اعزام جنگجویان سوری به یمن برای جنگ علیه انصارالله را رد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/akhbarefori/690980" target="_blank">📅 20:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690978">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LUMiOx93j5VQ42-6zgZEJnmtuXJAUmoHqfsGlotkMZoqTzWdybaiEJkjppQ6DcNX0WwzHAI_bDXpJXv_yWihpXW_bwhdZaav4f1Wxbj0swLfxhtx6AjslFXzMzJpYD5xMv3Xe1dAPSWbO912zBI5LCAQN2SYdFg5QAKT2TSZ0trRH41rHw0YuT6eIA2vulX2MKSezDKAOkG8j8H6qpEcnGxcCw2kDZq48wvSGFTVDAclgxV64SVlRfZbMuVr8y2LXrbz5VIQAjHpe5IjeF9Ld9XZNMxMPMcTecJzCz6MVTMdeFr9Ugm5ESqiSzJEZaHgMYrV85CQp3quDzPYQoNSVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iquFqaLPjy2yCa7f8WIG7cea9Q2VnpWfsIDKr0JJhqEECxgUNwznL0IpIIKjMdq32acBmkcFOkx_DW3znWyuuSjw0k0j77SsBjMgCn_N91k_1_O5idLH4hVfIrll5c6Fie_5kY4dSoq4wJpjDNIVJMG7M0hBpRs7KZGrWHZIjmNx84FNViK9yPrFnKISnYNOntPZ9X5b5cdHSuJnyxaI76kHUlCNqWTIplzdagkI6C0Ye-Hvf5xUfGcakFmBqW8A01rpHYhpJJAQFDqJhYs6xWVBQccjfHxfol0Ch_J5AnrwYXzS6gG7jA92huB_THdHQuaEIdY03BajHM4zazWXrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مراسم دو ماراتون در بوستان ولایت با تایید مجوز استانداری تهران برگزار شد
🔹
درحالی‌که از ظهر امروز تصاویری از همایش دوومیدانی در بوستان ولایت در فضای مجازی منتشر شد، پیگیری‌ها حاکی از آن است که این مجوز یک ماه قبل به درخواست اداره کل ورزش و جوانان استان تهران و با تایید استانداری تهران صادر شده است.
🔹
در سایت رسمی این رویداد نیز، «تهران کلاب» و «هیات دوومیدانی استان تهران» به عنوان برگزارکنندگان معرفی شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/akhbarefori/690978" target="_blank">📅 20:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690977">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
هانتر بایدن، پسر جو بایدن: اسرائیل از حمله ۷ اکتبر اطلاع داشت، اما برای جلوگیری از آن اقدامی نکرد؛ جنگ غزه شبیه «نسل‌کشی» است
🔹
۷اکتبر ۲۰۲۳ روز آغاز عملیات طوفان الاقصی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/akhbarefori/690977" target="_blank">📅 20:13 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690976">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDYJZTCsVJS6XRZzAAfyWoGP2U0SBWPq-b2NJi2SnqEHkOsX3A75vRJihLk8s1SvruhyIMZ2rnEB2bjlKzaCM2FUuOzCMBYkvY0x88_lMbplB8ozBk1aVLZaEMVCNQoSWufWsdHQzUye92_0NVmrugxd0bVH8kRq5E1r1hs461TTo0uEEaEpI4QEDqynCFxEZAKr9NjgTWUiRexzFzKVT72HIGcEYyUOOV4Fb_-5WTrzXBz57x7mJq8PmwCIbE-94vPclr40MCrcz0i6iDaUufzulRMtqYDL8v3m-CBMOqQ4oBbEZ05JDrioLqex114bn4_EbBMlsp3j0DmME3iMnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۱ کشور به‌عنوان اعضای جدید در شورای حکام آژانس بین‌المللی انرژی اتمی انتخاب شدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/akhbarefori/690976" target="_blank">📅 20:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690975">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
ادعای ترامپ: با حوثی‌ها در حال گفتگو هستیم؛ حوثی‌ها نیز تمایل دارند به توافقی برسند #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/akhbarefori/690975" target="_blank">📅 20:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690974">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
ادعای ترامپ: با حوثی‌ها در حال گفتگو هستیم؛ حوثی‌ها نیز تمایل دارند به توافقی برسند
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/akhbarefori/690974" target="_blank">📅 20:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690973">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c989965e.mp4?token=qizsSyo5NCElKBkGySsH49CP6DQTKP_3c-aU_wcbZPw9EkjMq5fe_ElGqLbVD-tTKT7i728el7Doz2hvws_ct1tUR3tXsveTMxkbOpKTcFBimkDAUyidq0zZmabfK2NlGZ8dX2JldG8uwR60rTYdvJ9E_6dE-xwrLvt8Q3k1wxwyk_bbxgXQtbDCxQ2b3nFPHYowcGfTz7OgFbhbWIREgu0oGx5YFNuERkio3DrrT_xvaU718CiXOmxRcjz2T1KPEU4WR1UGqjyrsbd_AmmITZIKUzxirFjnpyCC78WjsCwtVez1DEBAEdtxyTsK5LiOzVil9OwE-tElOxzt0hHm5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c989965e.mp4?token=qizsSyo5NCElKBkGySsH49CP6DQTKP_3c-aU_wcbZPw9EkjMq5fe_ElGqLbVD-tTKT7i728el7Doz2hvws_ct1tUR3tXsveTMxkbOpKTcFBimkDAUyidq0zZmabfK2NlGZ8dX2JldG8uwR60rTYdvJ9E_6dE-xwrLvt8Q3k1wxwyk_bbxgXQtbDCxQ2b3nFPHYowcGfTz7OgFbhbWIREgu0oGx5YFNuERkio3DrrT_xvaU718CiXOmxRcjz2T1KPEU4WR1UGqjyrsbd_AmmITZIKUzxirFjnpyCC78WjsCwtVez1DEBAEdtxyTsK5LiOzVil9OwE-tElOxzt0hHm5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تانکرها چطور کار می‌کنند؟ چگونه هزاران لیتر مایع بدون واژگونی حمل می‌شود؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/akhbarefori/690973" target="_blank">📅 20:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690965">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vyzPLkxyVN0cjSU7f1RRWRxi4IUJ4HFttkzhp1hxZwIH-qGbEu0IxghTM5A3d2GC5tuhyvGQ-bgAmL99V1Js-sCxd7EWLEILJYRotF-IOvSDyolmZ1GXq5YdrU7WGT4IHck2kMMc5b0y1UufE0Ee66Qf9A6XHx_pPOHhnKiaVoQhz2GD75U1i_RbUSl1zdAXG2ImQAQ5MrRdwaQsuM_KsjLTOtJk7wQknylqMogO12ijwDVe-g_t_E-fYG9JgVZHu1iVmD5Kq9zUVLJAXb716lcTnOD4FX-n9QD-MXcw8dpvv-VNkPhh5KNGOhHIXU_toSF4nMz8oCVEyD_feWqNrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q77HhC3RGXvkCfy91D0znN9OIAI64xmNWszAVy3gzVxz8qLeQWvd26ZzEYS5R5AHlarZ177IheaI-Q2asZL63bNOKsIeaSPk9wqTTQFnJvr8QezNyO4kbZo2iUnHdat8FmBj8nM0S1rT3I74s2Ko3qq6CKS54TUYlEKJubTzywiVv8LD-QYxD3zXY4fXfROfZvLszW4sazz96DQgFPPERy0Ns7KtQM9pJghHMwrCx60f6psRjrzlf531555vNCE1mVJt8ETLKpHpriv9a6FhgOFHcqEYFv-Euu_Vmod6lNgs0Al7XfHTtt1bXhtJlyYWdO6jee-DDztlrxfSewqtwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oha1pRyOwlEzwMIuPMBjPUbNPLwmzWeuXh54MP0Pd9iYQAbQCjT9_NPP6AIoLWoV9xj8b1v92pMFHS6qAQeKJ7rDe6vY8ZqPrxjQPPGyXQbEbcRNmA9XNDegsMxjCyYNkU0LW5ozfs2XtIBYSll78WnEbg90wnZTyv1ZLZvU6p9YImnU9A3RVTr2QCVl0fEdbUJN_lhvs7uqF4i9tEs50vQqy0CSfCtZQJnpOFsFzjgEqvtxxYGTNPS8ZtFUHu1LxcVRGeZ-chjP1Mc9fGIVevMxuSIZ3IoL1XcnvkQV8JmBJmJZKsce1b4QdtEN2k3eWh7G9Ty-kg95hzZI9S9BLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hQNZB6EQ3DgX6Oz2eFa0MtIIXl5Ci5gJUMskMQyBRKlCB9YJSEyWb0acXeYHl2Q--lB7zu5EbjyIbt_984Wsgxu80MPKaH-Tvc_tYm800WJ6I7SCNt5aSYQb7eukNVBOmendIR2KynuF9dL9aILqdd_PPBoa15ue1R69hxye69K_OhyrQc4zgrFee9hYkES8CkJj_PGWTwJ90_qqkwS-A3ydp8oiNHlDsKvC9zRvsiC9s1C-TXWWVJzlvbCLpiu_ygUB4ZX2fIioodFhy0gcefPJzmRBDqHxID1UbdcSNxHerzKe4glQ12Y8n9xVENe3Tu1R0j8WU4m1aN82KdWOfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RVtEWlyPO3FC5A3JQ2uPWG4vdma9UILPllXoYSNiARmtKywXbEJS6xz53OHm_a0zn4FL6w5--YXUra5_cHtUPCsr_xcRN8r7pSvvyCXQAKalviOKjGcr5fdEoE0kCG-OsLBhP8qXOycV3uJfFlF5-5JWf_s8ASmOiTxsH7AtUTxQBS2bsL4wxRXESnnK3RCaG7blJrUgFnsvoo5NtALAgMxLia9UsSXKMFtwWHOqfonFqETj2C_Cv9fK5RZlFqcY2kksFpjbvHEYTknLKBD_bHkrjlFyYIVyOJort1YWPdS93HjsakfqPlhxeolxUWKodgMUFCKbpV7FpRyyeQXv1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SjAc7FKDI_pcC6ArL_KZ3gcm0lr01e8NVULj86wJKB3Z6KRl5I9Hwsz6kd37LemgiHmSjsHba6Fyyhvg6kNWvdgH2rr_VDYMz4E_yCiEIqDRqHjAyAOvkhcd-jfrNb11peDccWNiGVQy0-xjCSrkgD8uxbilu0Gf2fNeRvlw29UDswCkm9swcwHHm4r9XNqhNKcz3AEzj8e6VBZeSAltn1-w3hpgtnJxbPgiW2T1dcsqd_alE7w9tHggLApF3PAND7dVDQF4FZKryMMgu8Pvy-8yZ-_vhLf7ppJDAratv_4qeDzA_xdya48xjwL43E20vSNDlExlOfb5ot_M9H_hRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aNg3GKRSHUJIMeqVU9ZDIVcMmWrY6TBMUZ0UF9o5sNdTPkSv-tzmG-Z8-bGp1Zj75HA5Dbnn0Rldoqo5cPkAPjYbxwCr2l7sbT5uwsgkuE-nw518hrU2qE55QXzF5OLarYYHHeIpFj5-i6VaQ2Obo9WmwpWmNA3AKAuhKV3AQz29g653pbuv3oZFs3Yd6F4Adp1gqo5ODH8BiOFgHROZnUWLBHya0wjfyJuIiexZoQx1rNQR-1BfUrIDQc7m0L0QVYQgaRGOPNQQvT86lWGyLJflNjNVUMcVa6VP43Q-A5N5ux-HDkolFsDle8un8w_dmbFykjM7LLsjvm-XwCBW1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PSmFCdg8Qv3fH_4vsR1Oj-EEwdEwqrpBaMFXeBnX5ipvv9gFEDj_-bltrXJWan8b704K5wD62Pi6nml91rste_MoyBqVVnEIV3m4xRye7NwN85mH2ZOLbjd-zi5P7GIfjbRdzo8NCL_6fZAmHZR1bXkLolr9qp2zoOOLrf-LQqRrXV584ARVE2v7Ga4PvOobBVXosa4sCBP2cV8BVv7wQg3kH19zXDbz9K3W5Mf9RvMl7Zi2qNdOdTMAUTTJINcutzgsgY4ZTvT3sXd0Gf1HnlQ4i107YcZMhJhA-GQXsIUzZA74RXSrXCPqizjje0mXGeNpFMha4CAHOsM9wujBsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور خانوادگی اقشار مختلف مردم در رزمایش بزرگ جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/akhbarefori/690965" target="_blank">📅 20:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690963">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZ-7a3_jUNRQ8ecfjgGIazmmyfZ-JkDkB4cAOegrG5mwgkdEDZpmQxTWJo--s11MZTVDCaWCFtO0Ydpt_pANVoRFgWyW7j7m1_5IHEU-6OFtRGqmgsptQByQ1XV6MSmc1W1RitLg1e4XHnnaHqJ9cfCAU2KzWp6rLh4YV8dNA4hmG61sw_1LHv9kg61uooAm9TpYmyjfn-i-7e7ChCmIn4jpn9SXSCNxe25EKvvhHBr-8FMnhgwa6C9PDtQ7PedmNwBZI9S7aMJFivC-9tkGQ5oSIQf8SF5XJOUYUA_1MrnMPRJ0ePhA_J4VUo0Zos01NqMDPZIQqwF0UzOXbG7KAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قطعات حساس F-35 سر از هنگ‌کنگ درآوردند
پولیتیکو:
🔹
قطعات حساس جنگنده F-35 که از استرالیا به آمریکا منتقل می‌شدند، به‌اشتباه به هنگ‌کنگ رسیدند و این موضوع به بررسی کنگره آمریکا منجر شده است.
🔹
گفته می‌شود محموله شامل کانوپی مجهز به فناوری پنهان‌کاری بوده و پنتاگون و لاکهید مارتین در تلاش برای بازیابی آن هستند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/akhbarefori/690963" target="_blank">📅 19:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690962">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe19ff3eb5.mp4?token=qpHK8kgIifzMdWdXgYbh8YDPfH9V2qoj8Ja2TCFoCxmpV_l1b0tG9I9BTQEUD8Gp0cMOmRRNDRnqVAQDl1CbsTik9_aujC74IZlWBBstmfELEog8A29GRdEAYk9fI7TOJnYO79BRAj-AJHo-Rvkb7mODbeOFh1E3ASc21Jw1YUgn7ttjZu8XOdbeo5H3CncM1fJL98x4yfamzJd2OK7EWesPgz_ykm45f14ozHv25DmvJSDy5-55sS2UnizJrRt7SorhpGOBr3UZAvjDgQb4JTZlCi0pnWiQyJmyxbBZ9-UKL6TGz5-GdOG82VktbqUdtmc8LnNQf3SJ9Bv3GVxxyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe19ff3eb5.mp4?token=qpHK8kgIifzMdWdXgYbh8YDPfH9V2qoj8Ja2TCFoCxmpV_l1b0tG9I9BTQEUD8Gp0cMOmRRNDRnqVAQDl1CbsTik9_aujC74IZlWBBstmfELEog8A29GRdEAYk9fI7TOJnYO79BRAj-AJHo-Rvkb7mODbeOFh1E3ASc21Jw1YUgn7ttjZu8XOdbeo5H3CncM1fJL98x4yfamzJd2OK7EWesPgz_ykm45f14ozHv25DmvJSDy5-55sS2UnizJrRt7SorhpGOBr3UZAvjDgQb4JTZlCi0pnWiQyJmyxbBZ9-UKL6TGz5-GdOG82VktbqUdtmc8LnNQf3SJ9Bv3GVxxyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماده‌ای کمیاب از نهنگ عنبر که ارزشش به ده‌ها هزار دلار می‌رسد؛ چیزی شبیه مدفوع و استفراغ که در ساخت عطرهای لوکس استفاده می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/690962" target="_blank">📅 19:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690961">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
یحیی سریع از ناکامی توطئه سعودی‌ها در صنعا خبر داد
سخنگوی نیروهای مسلح یمن:
🔹
تلاش‌های جنایتکارانه دشمن سعودی در صنعا (پایتخت یمن) که با رنگ‌وبوی داعشی انجام شد، ناکام ماند و بدون پاسخ نخواهد ماند.
🔹
هنوز مشخص نیست که منظور یحیی سریع از طرح داعشی عربستان سعودی در صنعاء چیست، هرچند برخی کاربران عربی از کشف و خنثی سازی یک عامل انتحاری در تجمع امروز میدان السبعین در صنعاء خبر می‌دهند که این موضوع هنوز هیچ قطعیتی ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/690961" target="_blank">📅 19:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690952">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hvMoEHFCSqkaaRL6iYBvcIAFSpov7_yb5P6uJdgz5dq_Bko4lIAAOqSu9PZiP2TwaVSLAWqBEz7E3BrfW4VrtcRaLf30egka92KYv-LAX91HC8xDCvB-dYTG3me3BvM2lhgHPVnXL5ZP73-iS3kvewzfLmgnSrlOfrb_7AC5MbnfWE0gIdaX0B0s_EcmbZ43JFaY0KsIssYSct18F0av17fwpG7EoXdBfSFsaUyKi8wY0NsuUAGxE6eWQfg2dFQDb6v2ZGZdAOblzaVXKjlHoSu_2EC8huesUofsm9bI6W7Qa0QL7hQOAifaPpMHTCrBILXdd_dYwkZvKQ7UfJgKZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ztb1CdKhacWljUUBPhc6bBk92A_D8w4Jby1CQP_WzRyQGzQ5RPtczshaa56gT-CfsYnxTsbAu45yFzmI0bw0RS6VMz8Ex7rbEDJfybFOR6lqDc-DsOAEhXRy-vpKEbk1M3yYvIku0WAps_MA65GtDkkSN7BZKK_o0szAX0lBslNgMCUDNhywifYgMkWAOV2VEmHqO8ZgzIephskYgKTjv6hvuogMJ0ZBHXERJ5zv7kDJ4yLLJb-BvI-UOW3w5V03bI_v63QvqchndGmLrlF3WxlPhHHSN1k3GHeXbuhrFBfnMwTglzY3tdJ8oMJBPOh8Q_zN077XESKr6e6fczRbDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QJeIagX-BhuSbIO3ixABZTWrAjz_X0CAoD2hQVxPVW_nTyPDsRd--Zp6Ojn8uhY9LnWq9Ae4ufIdIOYM7AYbFLTYewxK50msBPkcWSxGSpcB3qGPASg-2xU2fi2PnfLlO8jdWs9tlz99XLVNrC8DRPO_vu8K-QiA7lOIvimjtpazQlD-jpwrQ7vQ1tvVPuRVGuW4M6QxTeu53s8aDxPA53OejfYvxXqFONlJ7eWQvXRk365vWYeexQq1HNlEZ1NZpt893mwLR0iiCveVuI6SV_fw2wxZBnW2VeLmb7I8Jd8X1zDWKNOvDvd_nqcD1W3dz0ipMc-v5G4YkCeDXXZu9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sFNVsGZkND6brNTAWsfKAm1SsMZyXagZn0-VfmU9SpkefcPRxWVQsPQN1JbsJu-j9w_u_wyxKwcqdzEkmcWvz4l1jjCak6hY2qGro1JMkOjecsDrmsgZDQVL63ZF0isSuhFBh_7E6kfNxIgmXuePLL-VVZ6uvLri93cbixOWRSwuuCu9FxTr6gt_QLngFwqhffq6uH5hQnhjja47k0yAab-xSTgVGWQ82W6b2FJSNZp2ZuFVRferhGkCsD_XoQRmoTprfaUVaDtdAd2qhxA7hlDBTv0T0MwaLQ22SyvpWDPNWP2oQQ1uvHo0QBUTZ1yYmx7BJGr4uTxHdv86zQ1_mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XExpUCRxEhLaBk19EYkUCm4NnEHE11Usq0zmnTCyaTFxhnLWT_PbmskjsasqWD7eeCWyAe8h-FbnXu7v6E4hLTm4Je4qvNvkmUeBaaz3lO7Qjcv_nHA3TP6gPjrVvNY_cCK_HIXrNrJMQmwaYGxO-fy2Lsmf99wMgTEauzRjIioNCkKA2v59WGB9SsHjobUBdvzdkWOr5nGALSAqY5LqwV5GfSMpcD0EVsnUswBVYP_EhNnrkdPjd7EyHlolHO8yZrfRHqwRxt-YFpDvDIvKuW8_rWtvMHXfO2tsk_QhGZiHU_DWYIbwzUCxPSL-cVllm2_hgzbV3DLxb1zoUIAmLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GH6oi7liP_5ASP0mhLYsX7dr6Eow0QndsAbMKlEA7PaOvVELBhwnqMxNPL9lPexmvIIrvM4a94bXZVFH7A6Vwuh43coVAAUnpp9dfnK4CW1el8kAxZ3oGbj-7x3jSGCEQk8WZCuoeBow0EP6Ng6X4E7lUAMu_56w1LBk4NmBGQDU-maEcLPAhw048Y033Uc-3u1BHI9Q2JjdwGTzC4b4cHtytjwaokh046zoXZA81HMlqLZJD4rnRlMO3Z2xfREWWgZbrUgtlhFBEZJz6a8Bzst2P5PFx8zsht1vdwkpfe0SYsq8Fleq0Jrp1b3b6JDdULeZvffnsGEmvSgfAaOrIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nYyY4gquvwEOlkGFhjd1XcOPp3TO-ry4y2WOhR-yFnYK9Vfo53XOmUefCV3ge7bp1xmugd1af5BqPac-7YkzO_8nr3MaYqhC3paEjt3XgrXbIrY0nooshGLPS_GcR5pNAGrohySC6ad9aGAizQwTOyU7YIzxIyEqObHWLyq49_hzLS3ScwZanwsBYd6z0zv8ZPtmrjI6lk88gj08VBcqWNa4K3UuH_82PKo6joOKQlX6C9oRsKP6NFa3UC1hKlmLCWbttQ23IzC6n2Yv7DBFcbLcbRox8qKKtpVlyOGuA2N8A2YusfEyHGNrwKj-nM_aRzpPxQ7uYGBkgCx-Zpa12Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q4vCLCpV_Mud1n_1C6srJDsGjqTSzceuQD8B9Wo84b_wBv7v7Abpq9uiiiuOoelhn9uBSkhV0OpYjYs_4sXV-jjhKWJtBVrXPQFb27w_ZOt_oCtCX4Ky3nVZNH4QBG3dqG-ee-agJzXIalKBdhYCvKD5LAKCDmURzTgwrw5He_FA393yGA-srYWmjWW6hKGHoVuN3ADDTIAZm3kBWpAJ_ESWfxACBxaAGs59xgLiaMEKBPNhJyNzsprnWUcpOdp2hZKB4pmRJuUAA05WsLg4dtoGYXUn-qAa9YfmuYnxP4ki2S_D6JuTT_sNnE3Y25iQvgn0LtUcyY0qxH3RCZgIuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07146f6366.mp4?token=iEzLA0_iq0Vz-Q2D1Phv3xSJfFLSJ_UFJRhkO8YJKT7k0pi-zdFxzS8JdBbZZcjL5cF55VFw8l2e8uVnYPY8guXstwZAu6diG5HnT_6RA4PKtH5FAMVunR--olWB3zWSfCCa1GmwTtBqTvGKjsmN5evLZuogM-d3vieLyPOZopI51h-3OFCkqf38NHrDDBMjiy-ijlHKOupG-NuuwTr2Yxnpo2aiYOW_T4cwrZNb6Cg9kmTQ0mDLk-0VZphC3NJJWVcu9CMEZlYTHc04k1gAcAars6nRw7JClf3LrJqgLke-o076VFxTfpRLjL3YtaGclmgg2XYP41-OlJtYNNnzog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07146f6366.mp4?token=iEzLA0_iq0Vz-Q2D1Phv3xSJfFLSJ_UFJRhkO8YJKT7k0pi-zdFxzS8JdBbZZcjL5cF55VFw8l2e8uVnYPY8guXstwZAu6diG5HnT_6RA4PKtH5FAMVunR--olWB3zWSfCCa1GmwTtBqTvGKjsmN5evLZuogM-d3vieLyPOZopI51h-3OFCkqf38NHrDDBMjiy-ijlHKOupG-NuuwTr2Yxnpo2aiYOW_T4cwrZNb6Cg9kmTQ0mDLk-0VZphC3NJJWVcu9CMEZlYTHc04k1gAcAars6nRw7JClf3LrJqgLke-o076VFxTfpRLjL3YtaGclmgg2XYP41-OlJtYNNnzog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرچم، سربند و دوش انداز جانفدای ایران بر روی شانه و سر و در دستان زنان با غیرت ایرانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/690952" target="_blank">📅 19:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690951">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
هزار دلار پول یه باک گازوییل در ایالت فلوریدا!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/690951" target="_blank">📅 19:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690950">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
پرواز استاد دانشگاه با جت‌پک در چین
🚀
🔹
یکی از استادان دانشگاه ژجیانگ چین در جریان روز بازدید عمومی، با استفاده از جت‌پک به پرواز درآمد و توانایی این فناوری را به نمایش گذاشت؛ صحنه‌ای شبیه فیلم‌های علمی‌تخیلی!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/690950" target="_blank">📅 19:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690949">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
هشدار تب کریمه کنگو/ رئیس مرکز بهداشت یزد : با شناسایی ۷ مورد قطعی ابتلا به تب کریمه کنگو و فوت یک بیمار بر اثر این بیماری، شهروندان گوشت مورد نیاز خود را از مراکز مجاز تهیه کنند و از کشتار خارج از کشتارگاه خودداری کنند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/690949" target="_blank">📅 19:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690948">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caae7d32e1.mp4?token=FyZUZFqTvqDl4wH6FX23cLIpPmbaFPpHpKV5FgfNj0SUlbW8Zpvtf-2qmnWmCZcLvdN1yDvq6bCv_Ts2aAE_sI__fksNOCmcfZ-OZGS79wvvuAoLFyty7T_6PM8bthwW319oSaqqLgx99zMMYV8yr9R8qIriyvGyjeVzgAjCUspGb6pm0uawi2DYYprUMxke9nVJ8e9f3-yPEsMcwCHHhSNww8CT7H_He6PlqmITIKMvHUSGXLQoJrKy0MM6ixTTU9_8rqN2eqtI0-K6yAHn4ADWxG2WsB6an7SkO61FAl8EFuZ2OngCMIFQHzotrgHdDpvZCOQn31Xlez24gRU97Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caae7d32e1.mp4?token=FyZUZFqTvqDl4wH6FX23cLIpPmbaFPpHpKV5FgfNj0SUlbW8Zpvtf-2qmnWmCZcLvdN1yDvq6bCv_Ts2aAE_sI__fksNOCmcfZ-OZGS79wvvuAoLFyty7T_6PM8bthwW319oSaqqLgx99zMMYV8yr9R8qIriyvGyjeVzgAjCUspGb6pm0uawi2DYYprUMxke9nVJ8e9f3-yPEsMcwCHHhSNww8CT7H_He6PlqmITIKMvHUSGXLQoJrKy0MM6ixTTU9_8rqN2eqtI0-K6yAHn4ADWxG2WsB6an7SkO61FAl8EFuZ2OngCMIFQHzotrgHdDpvZCOQn31Xlez24gRU97Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تخم‌مرغ خام چقدر وزن تحمل می‌کند؟
🥚
🔹
در این آزمایش، میزان تحمل وزن حلقه‌ای از تخم‌مرغ‌های خام پیش از شکستن بررسی می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/690948" target="_blank">📅 19:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690947">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
پرچم ایران روی سرهای جانفدایان ایران در رزمایش ۳۱۳ هزارنفری جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/690947" target="_blank">📅 19:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690944">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aa588871d.mp4?token=pcF-aFGnPCJyRpA2fVhtjKvcy6Ii_ILJtbu7GDn_kw5E-1VUy-wGT7mgaQYSWQca1im-cY1R9a1BtfmR8Lev-bOFgOikHpyRoKnb1lZuW5y6LgCvnwhHS49xMrVzJD9qU73iZnfC9o8pe9uaqPQf0HmZ9XqnQUpxoX9498zEOU_2HRoHOH3GchmGo7TqVquHOB2OBvYsNJ2VZfXP_TI233mZU4jrHPHOCr2ZT2Aablhv32JNWnIw0K5PYzXzwKzpNYE9kySYAElSs2IMs5xZVBLmqCJXZ9Jhfn5shgos7Ay3I3pzHUMNwIBln_gRQqgM4FSupk6onMLOAc57of_jyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aa588871d.mp4?token=pcF-aFGnPCJyRpA2fVhtjKvcy6Ii_ILJtbu7GDn_kw5E-1VUy-wGT7mgaQYSWQca1im-cY1R9a1BtfmR8Lev-bOFgOikHpyRoKnb1lZuW5y6LgCvnwhHS49xMrVzJD9qU73iZnfC9o8pe9uaqPQf0HmZ9XqnQUpxoX9498zEOU_2HRoHOH3GchmGo7TqVquHOB2OBvYsNJ2VZfXP_TI233mZU4jrHPHOCr2ZT2Aablhv32JNWnIw0K5PYzXzwKzpNYE9kySYAElSs2IMs5xZVBLmqCJXZ9Jhfn5shgos7Ay3I3pzHUMNwIBln_gRQqgM4FSupk6onMLOAc57of_jyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به یاد "مهدیس نظری" فرشته مینابی...
🥀
💔
به مناسبت بازگشایی مدارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/690944" target="_blank">📅 19:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690943">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d3b7367f3.mp4?token=b_lCgFkc7Xe5JQEJIkukclEMKmDWr9grvlJTJ-FxHmHsFDgksSJrKXt02DlkrABCVbEpotwwKatUwcfLQfr_NmAw0DW-ID0q0KVjJdksn2AXXeYW3hRGtjRsQnhVJg96lSqLzBcCNWI55Z1QAXE5F2z9eQQFLajasW9Hj00w-McgTUHujd2a03Kc4Pvw1TupEKBgp7Pbzp8om4C3Iwzm9C6-A0zDDu0zH_BRyU7H1oiPXOK5cp0hkI2ctPnqbHiAXyUIxghM3qrAUaVZ-0hbhQx4gI_QaS8UFKKSj5YbAPAPNIlpghrer4SPzMrMictK1oospho6MyZcLRsUhDK_-zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d3b7367f3.mp4?token=b_lCgFkc7Xe5JQEJIkukclEMKmDWr9grvlJTJ-FxHmHsFDgksSJrKXt02DlkrABCVbEpotwwKatUwcfLQfr_NmAw0DW-ID0q0KVjJdksn2AXXeYW3hRGtjRsQnhVJg96lSqLzBcCNWI55Z1QAXE5F2z9eQQFLajasW9Hj00w-McgTUHujd2a03Kc4Pvw1TupEKBgp7Pbzp8om4C3Iwzm9C6-A0zDDu0zH_BRyU7H1oiPXOK5cp0hkI2ctPnqbHiAXyUIxghM3qrAUaVZ-0hbhQx4gI_QaS8UFKKSj5YbAPAPNIlpghrer4SPzMrMictK1oospho6MyZcLRsUhDK_-zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یاشار سلطانی، خبرنگار: هنوز مشخص نشده که موشک رو کی شلیک کرد (به کشتی‌های عربستان و قطر) و توافق رو بهم زد!
🔹
یه عده خودسرانه موشک زدن؛ کشور داشت آزادانه نفت می‌فروخت و پولش رو می‌گرفت ولی یه عده بی‌دلیل به دوتا کشتی تجاری موشک زدن.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/690943" target="_blank">📅 19:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690942">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/081e9989db.mp4?token=OxVLJks-DActSNHwkLJJwjRupRcrjqpl8AjIVef4dKxpKzM5HJVPOfPl2TIxqjZg4zmTluEvzGuptqofCLHBgk1Ms-8IBozwGkqGmOLDopRWwWEq3BV7D2HNdGbgKvdWgNyNySc57EfsHOXRvd5nAIl9LwABbsGMWbxOt00rbF6in_BpIaUlY0fpXaGGdRl5-T7N2C3KmvoJDL_JcMSKdfFXH1xNSCLE1iy4Wk_J_03maXtgTLa3dwlWreJzjgBfcSRl41x8V0u6yFUVORKjvJNX2kclioNjJA_mUn4rx_RmAkmwslOQVshd3JbAbw3x95WZL12bXzl-I_vL69r4nFYQVZhfiDyR4hzWGeW0yZoGyTQ30hDzBiqL9qsMzme7OHRvIxa4gVXFkHkSuTyK5Dxz_xYlYaN5m9G3mV1vRUxhklhZaY1Yh03yMPZ-vL5YZld9PmY_tjkDZ-Hfgmsziu3DHHKnqJS1sxTJEST7AC925no0Fgd4GmWabI7U2GKp18r69r9iNxbASvgBAVbzoB3_6Te_jmFsguXnTF_gGfuzxc430CY6LZBMXJlLjOCGzvqyBDC8zoRZ4wP1SX3LgWL2BloaiCWJzZzzBcSa94BA4HNmoZhNuSkdDvgTcLIwo_r24edR_OsX4mWNnFPBNJUV-NPTjARjSPOgTZUXOvc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/081e9989db.mp4?token=OxVLJks-DActSNHwkLJJwjRupRcrjqpl8AjIVef4dKxpKzM5HJVPOfPl2TIxqjZg4zmTluEvzGuptqofCLHBgk1Ms-8IBozwGkqGmOLDopRWwWEq3BV7D2HNdGbgKvdWgNyNySc57EfsHOXRvd5nAIl9LwABbsGMWbxOt00rbF6in_BpIaUlY0fpXaGGdRl5-T7N2C3KmvoJDL_JcMSKdfFXH1xNSCLE1iy4Wk_J_03maXtgTLa3dwlWreJzjgBfcSRl41x8V0u6yFUVORKjvJNX2kclioNjJA_mUn4rx_RmAkmwslOQVshd3JbAbw3x95WZL12bXzl-I_vL69r4nFYQVZhfiDyR4hzWGeW0yZoGyTQ30hDzBiqL9qsMzme7OHRvIxa4gVXFkHkSuTyK5Dxz_xYlYaN5m9G3mV1vRUxhklhZaY1Yh03yMPZ-vL5YZld9PmY_tjkDZ-Hfgmsziu3DHHKnqJS1sxTJEST7AC925no0Fgd4GmWabI7U2GKp18r69r9iNxbASvgBAVbzoB3_6Te_jmFsguXnTF_gGfuzxc430CY6LZBMXJlLjOCGzvqyBDC8zoRZ4wP1SX3LgWL2BloaiCWJzZzzBcSa94BA4HNmoZhNuSkdDvgTcLIwo_r24edR_OsX4mWNnFPBNJUV-NPTjARjSPOgTZUXOvc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بحران سوخت به ترکیه رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/690942" target="_blank">📅 19:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690941">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
نوسان قیمت نفت برنت در ساعات اخیر
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/690941" target="_blank">📅 18:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690940">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
ادعای مشاور ترامپ در امور کشورهای عربی و خاورمیانه: رئیس‌جمهور آمریکا برای پایان دادن به درگیری با ایران در نزدیک‌ترین زمان ممکن تلاش می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/690940" target="_blank">📅 18:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690939">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc98ee2c9.mp4?token=Qnr0N0jhaEsiytTNUm3HgyFmwooT5wroGJkuVDq_g9xEoSOD_KVHmu0qrRxPAY0P8D-PXSjONjcy52039pdA597JVLsGOff7BgKESNprXvN6G46kypM-V6H8n3TVZstS9W0aB8V9S9L1pBt9NUX49ibrAUnrUvowrbQDOWTLbwc0Fcj_Y6d1GAvM22pT5RQIljrjNnBuDnkBiLSqIfN_qfImMewojc2Ncr5ow6nkpiYze0oWvjhnc2tSGE6Vnio4iGniWG5RnAOrS2zX_H9V2SYFRwlc5VEOKEMwYbIDaiaTBOC8kM02gaxNyiBGgHY7kqECLeNz6kvUT2V9YkmDAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc98ee2c9.mp4?token=Qnr0N0jhaEsiytTNUm3HgyFmwooT5wroGJkuVDq_g9xEoSOD_KVHmu0qrRxPAY0P8D-PXSjONjcy52039pdA597JVLsGOff7BgKESNprXvN6G46kypM-V6H8n3TVZstS9W0aB8V9S9L1pBt9NUX49ibrAUnrUvowrbQDOWTLbwc0Fcj_Y6d1GAvM22pT5RQIljrjNnBuDnkBiLSqIfN_qfImMewojc2Ncr5ow6nkpiYze0oWvjhnc2tSGE6Vnio4iGniWG5RnAOrS2zX_H9V2SYFRwlc5VEOKEMwYbIDaiaTBOC8kM02gaxNyiBGgHY7kqECLeNz6kvUT2V9YkmDAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور رئیس‌جمهور در رزمایش بزرگ و مردمی جانفدا در تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/690939" target="_blank">📅 18:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690938">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ادعای یک مقام دولت تروریست آمریکا: عملیات عقب نشینی نظامیان آمریکایی از عراق ۳۰ سپتامبر(چهارشنبه هشتم مهر ۱۴۰۵) تکمیل خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/690938" target="_blank">📅 18:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690937">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
رسانه‌های رژیم صهیونسیتی: پرونده‌ای جدی مربوط به جاسوسی برای ایران از درون ارتش اسرائیل، هم‌اکنون تحت بررسی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/690937" target="_blank">📅 18:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690936">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8531e9c2a5.mp4?token=RZ1PMrE52K7IS635Dkya-VGh4jE7KVTTOagouUxXaKG0AkH_uzMqTMTDJ6-lRdSGdrPUUUIIFq8TJSviHMwBkPq63ygVUgpmAAOOmP3u23uZkQGNQYbZK5YivjZS0VSpMngbrju98KQoeyXDJUY9y_o0USrHlo5C_aflW9gP3fKrGSXysBAXbwz6NUp6M2cPn2q_y1tN7cI6LByDSi1t7xwoh3NkMdcZBIdeYaJ_6Yh55jzVRTu-VjhtFW1yKoHh5qqI6oxaSVV_OydzqbSjgQMiw229JFsnAg8VxKr-_TNBx_3-WchtuHzzxm-mOC7gXzVwVZxo1uVgcHknEQbvCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8531e9c2a5.mp4?token=RZ1PMrE52K7IS635Dkya-VGh4jE7KVTTOagouUxXaKG0AkH_uzMqTMTDJ6-lRdSGdrPUUUIIFq8TJSviHMwBkPq63ygVUgpmAAOOmP3u23uZkQGNQYbZK5YivjZS0VSpMngbrju98KQoeyXDJUY9y_o0USrHlo5C_aflW9gP3fKrGSXysBAXbwz6NUp6M2cPn2q_y1tN7cI6LByDSi1t7xwoh3NkMdcZBIdeYaJ_6Yh55jzVRTu-VjhtFW1yKoHh5qqI6oxaSVV_OydzqbSjgQMiw229JFsnAg8VxKr-_TNBx_3-WchtuHzzxm-mOC7gXzVwVZxo1uVgcHknEQbvCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا حالا مار تازه‌ به‌ دنیا اومده دیدین؟
👀
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/690936" target="_blank">📅 18:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690935">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HaTVNlTdHw_D6ZqloAWTrYAc1RWJVE32YLjc5QQbVTBQueUFjWQ8C7R5t2jcWfvhrmGQ-suD9UJSyX3hI_osUBfvbUPtqlruhJuMM84P1oQuFsgyVECvA5ltJ2n3LzuiLuNEsnx2VbrWDy5REOPmwbwMxHu9DFSy0zHq_QvrYtVVjPse_iJixrEqmw4U5CDNSEwc0Ry__zGQdJxOpEhJEXWiQzipoO4-9OJHAjp4gfMldbuI7vOc4fT_xcGVwgRskEn12mhqgm2dwzOOvWL_jlQtFqnouwKURnPYPjOcpnqwzracNUWWpa9jRk7n1Jozd574GpBvMZJuJ4bGkYTcYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیت‌کوین از ۸۰,۰۰۰ دلار عبور کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/690935" target="_blank">📅 18:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690934">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
از گذشته تا آینده…
🗞️
➡️
💡
🔹
دکه‌های مطبوعاتی قدیمی، با چهره‌ای نو و هوشمند، دوباره به قلب شهر بازمی‌گردند.
🔹
این‌بار نه فقط برای خبر، بلکه برای ارتباط، راهنمایی و زندگی شهری هوشمند.
🌐
🏙️
✨
طراحی زیبا و هماهنگ با مبلمان شهری
📍
راهنمای زائران و گردشگران
💳
خدمات شهروندی در چند ثانیه
📺
بستر نوین تبلیغات شهری و محتوای دیجیتال
ما گذشته را حفظ کرده‌ایم، اما آن را با آینده پیوند زدیم.
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🌐
https://samesh.mashhad.ir
🔸
http://Instagram.com/mashhadsamesh
🔸
http://eitaa.com/mashhadsaman
🔶
https://rubika.ir/mashhadsamesh
🔸
https://ble.ir/mashhadsamesh
🔸
https://gap.im/mashhadsamesh</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/690934" target="_blank">📅 18:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690933">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
طرز تهیه رشته و ماکارونی در هند
🇮🇳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/690933" target="_blank">📅 18:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690932">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
العربیه به نقل از منبع آگاه: وزیر کشور پاکستان طی ساعات آینده به ایران سفر خواهد کرد
🔹
او در تهران درباره تشدید اقدامات انصارالله در یمن گفتگو خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/690932" target="_blank">📅 18:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690931">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/974fee3d52.mp4?token=fOrjyBTmgoeWdxchsl98oZ7OmEh4grvDUJqktr8IzE9yq34FfkpFeADD43TsWxzXtNcrqr1tN2d0C2VZIihwngaV8AQH2vuo90Rta375E2pAoMd2zN8iWa3Z7EIgxvEI9NcLekQDP-FI_NtO51NiIbSD8H5wFMRl0shlL_VEcrPRLKtZh5w_dr64-1TjHlJyhMN1ZkFlmnXLhORL6X6rZmtcn8j3HspXsaWuKxVhDQ12bGUBpXWsii6Nm8U7NloiSdGBmc_IBDrss08aKSay67aySWjQlvhCD5XnhLwUXdjHs2xjJcVsVIZ_zf-S8kt5kAaGP4775QHztFnaq0qslw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/974fee3d52.mp4?token=fOrjyBTmgoeWdxchsl98oZ7OmEh4grvDUJqktr8IzE9yq34FfkpFeADD43TsWxzXtNcrqr1tN2d0C2VZIihwngaV8AQH2vuo90Rta375E2pAoMd2zN8iWa3Z7EIgxvEI9NcLekQDP-FI_NtO51NiIbSD8H5wFMRl0shlL_VEcrPRLKtZh5w_dr64-1TjHlJyhMN1ZkFlmnXLhORL6X6rZmtcn8j3HspXsaWuKxVhDQ12bGUBpXWsii6Nm8U7NloiSdGBmc_IBDrss08aKSay67aySWjQlvhCD5XnhLwUXdjHs2xjJcVsVIZ_zf-S8kt5kAaGP4775QHztFnaq0qslw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برافراشتن پرچم خونخواهی و انتقام در مراسم رژه جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/690931" target="_blank">📅 18:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690930">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d717437bb3.mp4?token=szyKb-TNd9j9h_M7gUk2qpCmFVeLjNDdqZcwCQW8SGVJTT7ftu9GfOfVbweKtJYqR0bX_RR4-MhgRcT7QNbIBdRHZFV-3omw4mDcRA9syuFOqMzYRe0x1im5xH4QTa_wNeT-QjEMibssNorkV8yVpN8ZeoNi-_yGQ0HHpQa1feKT15H56z8EAZWYxrvdP8S0LBSNxGFlavZG-YsP7uV0T9gxpiYvL4SHsvtQvfR-SnlFEOzAPK3e7qwb4DptvR8CcOmAJSiad4GOeh_Qnl3EqFZnc9EPHT7_4IZDEktbdkBXwgfyW6fkL-3_X3t09x2zmQm1QPL0J-xLh-CzluhbMUCNOoX3O9fh0f0x0wWCGlilgYh7BUWAPsJ59LxjwYLQ4zkosjmFf1dswvV2UrcZlcQDVg9DPizljQPTriTmU7x9oEpzBHYuMbY7K1oOu7rklNcqH2rdlnW7mPeljzy7I3hPEmddDJ4c-_UifeGqvIfraokFhvB4Vp9ztV2ut5H28FdllTomIG_l5-8GWHbrD63kTvXx2JlaILhAAHWNINbEhOxCVUrCqmfBDCh0Z8w1-UARZ6QWKsS8ZH8Cz1iNISqYnNY6rLVuczHwz6-bsRiH5pDvZ9w_7b5gJ33BOekndptVlc6mzr7cUTwL9yeSY0x4HO3wiCHQ9jz7wvwPARg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d717437bb3.mp4?token=szyKb-TNd9j9h_M7gUk2qpCmFVeLjNDdqZcwCQW8SGVJTT7ftu9GfOfVbweKtJYqR0bX_RR4-MhgRcT7QNbIBdRHZFV-3omw4mDcRA9syuFOqMzYRe0x1im5xH4QTa_wNeT-QjEMibssNorkV8yVpN8ZeoNi-_yGQ0HHpQa1feKT15H56z8EAZWYxrvdP8S0LBSNxGFlavZG-YsP7uV0T9gxpiYvL4SHsvtQvfR-SnlFEOzAPK3e7qwb4DptvR8CcOmAJSiad4GOeh_Qnl3EqFZnc9EPHT7_4IZDEktbdkBXwgfyW6fkL-3_X3t09x2zmQm1QPL0J-xLh-CzluhbMUCNOoX3O9fh0f0x0wWCGlilgYh7BUWAPsJ59LxjwYLQ4zkosjmFf1dswvV2UrcZlcQDVg9DPizljQPTriTmU7x9oEpzBHYuMbY7K1oOu7rklNcqH2rdlnW7mPeljzy7I3hPEmddDJ4c-_UifeGqvIfraokFhvB4Vp9ztV2ut5H28FdllTomIG_l5-8GWHbrD63kTvXx2JlaILhAAHWNINbEhOxCVUrCqmfBDCh0Z8w1-UARZ6QWKsS8ZH8Cz1iNISqYnNY6rLVuczHwz6-bsRiH5pDvZ9w_7b5gJ33BOekndptVlc6mzr7cUTwL9yeSY0x4HO3wiCHQ9jz7wvwPARg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آکسیوس: جنگ در ایران باعث افزایش تقریبی ۱٠٠ میلیارد دلار هزینه برای مصرف‌کنندگان آمریکایی از طریق افزایش قیمت سوخت، از تاریخ ۲۸ فوریه تاکنون شده است
🔹
ایالت تگزاس بیشترین میزان خسارت را متحمل شده است پس از آن ایالت‌های کالیفرنیا و فلوریدا
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/690930" target="_blank">📅 18:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690929">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دعای خاص امام زمان علیه‌السلام در عصر جمعه
✨
گفته شده هرکس صلوات ابوالحسن ضراب اصفهانی را بفرستد، حضرت حجت ارواحنافداه برای او دعا می‌کند.
✨
بیایید در این جمعه‌ نورانی، با فرستادن این صلوات، دل‌های‌مان را به عطر یاد امام زمان ارواحنافداه معطر کنیم و مشمول دعای حضرت شویم.
#گنج_پنهان
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/690929" target="_blank">📅 18:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690928">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzQx-lTpDQRdmLYg3xejZIG3F_Ls9AoS82K6XOT9hftDXxd6_vXC96977terrCimFFVcjQpuXimxodApqhTZh8qV4mB9RWcMZVTwG5haAo-JjXMgfT3X5qxqX7Ng1rdyvVs6RU7KuQGKXCMaG1bAEx-TSdUggKeTGM5AnXZJRuvHgYtxDENQ8BRVwYIBoOfLtL3GxvS9iSpK1yUnjCpuUymezafMaTBROY8necGfrrnIplnRUVlGnyMFxBESrjTxL-6BQ1KR8nCgaz5Qr9QUgbfgx98mrCKELyYjDx8j0mPCSBQcBwE95wX3GGmp40du1LvbhNa-T6TRxTlDi_E75Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زبان و ادب فارسی یکی از بزرگترین ظرفیت‌ها برای ترویج فرهنگ و تمدّن غنی ایرانِ اسلامی در گستره‌‌ی جهانی است
🔹
برگرفته از پیام رهبر معظّم انقلاب به مناسبت روز پاسداشت زبان فارسی و بزرگداشت حکیم ابوالقاسم فردوسی  ۲۵/اردیبهشت/۱۴۰۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/690928" target="_blank">📅 18:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690926">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wd5ZRLcbFLfJyqaIz5x2euLRrNyzXDeYJYckwrly7bi7pc5UUDBbxU7DBdsJDrFK2y3aaSrwJz8uSneX2La3afaGVmaGOWt-sbNq5QIk4E6TKb1R_3xH79I0nI8muKfDu7kHq-M7XSxSknL7bAxjH-xOaYxF2Culu4DZs8s60fkA4ORVN-hSsKf7CuHXc-GPkXl4O_ZlLQ53QGqMaCMIuOvshrMRNXWFSiLL7-kZL8vM_uxSEemyWLUTkmGV5vpx2xvLgP9E_AaGVZgynA8dcNd67XSadVWfiFqRhvY84ij3AXsfVatYNUu2qnO3H6k0ZxIhgjNQBrzs-Nblv7A7qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd18f3e035.mp4?token=tW5z4snSi1fUB-2kQH7cWpAZxpFTIsMsq3jbT5Iwex5geH1dLsLpAcmrDsWOqKt09hpA0whTAh39UMiGZj2lNFCC4s4bIA02282UZUXhfG3Ad5Gz2yHKvXSdFX-F-p0F911BI5PwXXIeEzvkBdzPQbJu-P06LwhmDAKT5uhJriVLRvaisoIWy4XSUJdrN2mWVuY0rP93IDBHWzbOpoNGyGtFGl1eBrbqqJ1VKPm3epCeo68JbtfX53V1IVI7VR6YfLHvJhULVnQFkDS2PhVMRsbURq7kDk6kIL3IwnBEZzv6w3IHFWJ2b8ZsHiqjctbTjz7yJBWYG6bXuU-qDYg-dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd18f3e035.mp4?token=tW5z4snSi1fUB-2kQH7cWpAZxpFTIsMsq3jbT5Iwex5geH1dLsLpAcmrDsWOqKt09hpA0whTAh39UMiGZj2lNFCC4s4bIA02282UZUXhfG3Ad5Gz2yHKvXSdFX-F-p0F911BI5PwXXIeEzvkBdzPQbJu-P06LwhmDAKT5uhJriVLRvaisoIWy4XSUJdrN2mWVuY0rP93IDBHWzbOpoNGyGtFGl1eBrbqqJ1VKPm3epCeo68JbtfX53V1IVI7VR6YfLHvJhULVnQFkDS2PhVMRsbURq7kDk6kIL3IwnBEZzv6w3IHFWJ2b8ZsHiqjctbTjz7yJBWYG6bXuU-qDYg-dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور مقتدرانه بانوان کلاه‌کج‌ در رزمایش جان‌فدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/690926" target="_blank">📅 17:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690925">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKWhy270Sbfv6up2H0uJerCqLwzdVKyTFiUXhWegYkBf-OSK5rAc5Dlu8LFppEJyNiKazoe9Xmyto2IK7K3YqW3XC1tMBVpQ8crMvDHQlGgdRKJ7xujCQbCnaKxL2705SwKrnUD2GKiTwspFh3FpS8a70DmDjn-TSEj0VRXooaYubOirzTcyubSH7Tv0HrhNteTfNSbctsPAXCicynZTGyrVDql6Vj6sEvHLDXDNXGwGyAc8ZGQprFieRINguXDH_K1euOCAAHQHyYYRVSAe2CMgzLoS1xjHpm0S9dP5NHuvYAFhE9iCru444D219UL4S8aLviGHb2sSdJTQzRsT4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هزینه جنگ ایران و آمریکا؛ ۴۳.۶ میلیارد دلار
بن فیری‌من، عضو ارشد مؤسسه کوئینسی، به نقل از برآورد سنتکام:
🔹
هزینه جنگ جاری با ایران حدود ۴۳.۶ میلیارد دلار بوده که معادل حدود ۵ میلیارد دلار در ماه برآورد می‌شود؛ رقمی بیشتر از برآورد قبلی بازرس کل وزارت دفاع آمریکا./ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/690925" target="_blank">📅 17:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690924">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f327cc1ca.mp4?token=rMFleqE6pq_Z_ctIihPqEBLJYfvf_ac2q_VpKH8wU47rUxMM2IfVnlwvWBBCRgH3J2MTjm1TW3VkRAGERJnhUzqVqwxxxuKBIzycp4mH0yRYRVoiKwuQJU0d60JXWnSAHL0GUB63W8gEaVVhOBfuf0M6ajr9UjdCdaSr3Uk2avwS-jytRfNeFpXJRcj3gpG4f_H8mOa2KrKbXgmMOZvZvXtmOwEG9LuelOHaTI28HEAT4STUdztKVVI7lj1_SgumUZCMEvbMXXSqmqAthaFkazCnBL1RRS1wEARJWgAopuZqZzQcaTVDpX5-v7szsmfo4H65pm3DrRrg85l9y29qOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f327cc1ca.mp4?token=rMFleqE6pq_Z_ctIihPqEBLJYfvf_ac2q_VpKH8wU47rUxMM2IfVnlwvWBBCRgH3J2MTjm1TW3VkRAGERJnhUzqVqwxxxuKBIzycp4mH0yRYRVoiKwuQJU0d60JXWnSAHL0GUB63W8gEaVVhOBfuf0M6ajr9UjdCdaSr3Uk2avwS-jytRfNeFpXJRcj3gpG4f_H8mOa2KrKbXgmMOZvZvXtmOwEG9LuelOHaTI28HEAT4STUdztKVVI7lj1_SgumUZCMEvbMXXSqmqAthaFkazCnBL1RRS1wEARJWgAopuZqZzQcaTVDpX5-v7szsmfo4H65pm3DrRrg85l9y29qOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو وایرال‌ شده از صحنه وحشتناک یک تصادف
🔹
هشدار: دیدن این ویدئو برای همه توصیه نمی‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/690924" target="_blank">📅 17:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690923">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
پیشروی بیشتر انصارالله به سمت غرب یمن
🔹
نیروهای مسلح یمن وابسته به جنبش انصارالله، رشته کوه‌های «الأغبرة» در منطقه «المضاربة» واقع در استان «لحج» مشرف به تنگه راهبردی باب المندب در دریای سرخ را از اشغال نیروهای وابسته به عربستان آزاد کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/690923" target="_blank">📅 17:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690922">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
بحران سوخت در پاکستان و روش‌های عجیب مقابله با آن!
🔹
پاکستان برای صرفه‌جویی در مصرف سوخت، ساعت فعالیت بازارها و مراکز خرید را تا ۹ شب و رستوران‌ها را تا ۱۱ شب محدود کرد.
🔹
دولت همچنین مصرف بنزین خودروهای دولتی را ۵۰ درصد کاهش داده و هزینه‌های غیرحقوقی و سفرهای خارجی دولتی را محدود می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/690922" target="_blank">📅 17:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690921">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aad723577.mp4?token=p6-jzAiCDblgEywWIR4sbRZO4yYgWGT9L3gGagOrfq3uKUR93k3xsPJamiLX6fclGnUY1vMDFns6YmaET6Rmxwi3a-WRns5XP1oqZccu6kbidPkUv_AceVud-Ho-OVL4QCXOo3ATFIU2al5fuFEc5OrCK6Sk9uCHaQzswdzdwCEseutTuUk7lsion8E-4Oy_TM4sQ61aceQjbXoxSgDBo8ym466DqBWtDctbVUqfc9IFL3lHbzn9Wv8S8wLMs2OVpz7VrsYyS0oUwPODB_rSzWhcf4K-4y8hpGDFQqsn-HHSYy0bRWGDEocTKGZ2gMxNGs0wpHwjwXlSw0CsrsH2H1r-ecHzkcesaxdlrZ_wUIwyJHjKJ-yKGBvqgxUlwLJ1o6cqc0SH4u9KkdMKHmUetp0aDdfZy4yfIedXSg1H-qbaZ9I-cPjkNVsc82fb_s0_RSYvru6oqfeRqnRlp6QrSAbDMX3GLpHlP9TB-yJqpm_vCEtlLVsXHlcymWqV5H8IcDhIsyumyLyq0lOwYF3lKWcl5rfva34uVG1fL8iPc4t6dWEutPjsdFfqqkrliYAMj1-fvES_BaRbNmCnEOH2RwqeovmlKPn4YliW2LRvKN0Z8hwx9-PFFoUTD1JG6zSMQ5elrUPO9RgYZcsA7yMW-jg2-usj4A3-NOxN0LRpCWI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aad723577.mp4?token=p6-jzAiCDblgEywWIR4sbRZO4yYgWGT9L3gGagOrfq3uKUR93k3xsPJamiLX6fclGnUY1vMDFns6YmaET6Rmxwi3a-WRns5XP1oqZccu6kbidPkUv_AceVud-Ho-OVL4QCXOo3ATFIU2al5fuFEc5OrCK6Sk9uCHaQzswdzdwCEseutTuUk7lsion8E-4Oy_TM4sQ61aceQjbXoxSgDBo8ym466DqBWtDctbVUqfc9IFL3lHbzn9Wv8S8wLMs2OVpz7VrsYyS0oUwPODB_rSzWhcf4K-4y8hpGDFQqsn-HHSYy0bRWGDEocTKGZ2gMxNGs0wpHwjwXlSw0CsrsH2H1r-ecHzkcesaxdlrZ_wUIwyJHjKJ-yKGBvqgxUlwLJ1o6cqc0SH4u9KkdMKHmUetp0aDdfZy4yfIedXSg1H-qbaZ9I-cPjkNVsc82fb_s0_RSYvru6oqfeRqnRlp6QrSAbDMX3GLpHlP9TB-yJqpm_vCEtlLVsXHlcymWqV5H8IcDhIsyumyLyq0lOwYF3lKWcl5rfva34uVG1fL8iPc4t6dWEutPjsdFfqqkrliYAMj1-fvES_BaRbNmCnEOH2RwqeovmlKPn4YliW2LRvKN0Z8hwx9-PFFoUTD1JG6zSMQ5elrUPO9RgYZcsA7yMW-jg2-usj4A3-NOxN0LRpCWI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصادف دریایی
🚤
🔹
برخورد کشتی گارد ساحلی چین با شناور فیلیپین.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/690921" target="_blank">📅 17:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690920">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c81627115.mp4?token=lIp9auQzh6qwu0wHG65KAbP2wY38vDbOggxo6h-37PwRQesTFt5FzMybTZuOaMWl9WIGv2c4jDSb9p8aXa1Ptd1LeOhxmeE6Vwwi-05E2Iy24G3leYjsMxkPYnHosot79_uErvRWXvS443Yg26CS9UBtMKdW__nyoS10egF_7p5hgotmqFDLms0-gXy5XIU63NaPgxmN-uE2JHOWMOlq7czt_Rh5mmcPIH_HCiOj6G_kzEQZ4c8CdnKeqjpehOhBzByfaeZzZNmO9F1c8LUMKhNCwXYt8q4NzCKnNyv3E84pCHnxXVvqNah7mikWkBADNzaqUfHGhfGddJ76CnQIQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c81627115.mp4?token=lIp9auQzh6qwu0wHG65KAbP2wY38vDbOggxo6h-37PwRQesTFt5FzMybTZuOaMWl9WIGv2c4jDSb9p8aXa1Ptd1LeOhxmeE6Vwwi-05E2Iy24G3leYjsMxkPYnHosot79_uErvRWXvS443Yg26CS9UBtMKdW__nyoS10egF_7p5hgotmqFDLms0-gXy5XIU63NaPgxmN-uE2JHOWMOlq7czt_Rh5mmcPIH_HCiOj6G_kzEQZ4c8CdnKeqjpehOhBzByfaeZzZNmO9F1c8LUMKhNCwXYt8q4NzCKnNyv3E84pCHnxXVvqNah7mikWkBADNzaqUfHGhfGddJ76CnQIQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ابتکار جالب سوپر‌مارکتی‌ها برای مقابله با رسید جعلی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/690920" target="_blank">📅 17:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690919">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
جزئیات جدید از موشک قاسم بصیر، کابوس ناوهای آمریکایی
/
روایت کارشناس نظامی از موشک «قاسم بصیر»؛ ارتقای دقت موشک حاج قاسم با جستجوگر اپتیکی و قابلیت درگیری با اهداف متحرک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/690919" target="_blank">📅 17:30 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690918">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04ebf0623b.mp4?token=EojJPsb_mDIcN2mn4NybAu0SNDz5Obbk35PNVn5dP29E-5FLXFkzA8FOvvUl-uF8kSb0k3epRdkWFQwRQPayYacQJUE7B5AJ2HZFVZakeTvnyykk-AckZltWHmOALce69WamB4AfH5KPFbVB05LkgBs5EXmK0hkNLNU9s3SEssTAwTBDFJgdVjCv3PywfegSMK5kjWRkjRCwZ52orf4kQuyVXfHfIsDsviEBaqh96EurMwMHStVp4Z1WFBTvROmZvmiSpLy5j83uFH8fxnbLPYwYpSsJEzNUVk_BmEPm2E-GcGJWs8xaYt5bMlRSzJueuFIZf6Uk1J5Oq9nOZcDpUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04ebf0623b.mp4?token=EojJPsb_mDIcN2mn4NybAu0SNDz5Obbk35PNVn5dP29E-5FLXFkzA8FOvvUl-uF8kSb0k3epRdkWFQwRQPayYacQJUE7B5AJ2HZFVZakeTvnyykk-AckZltWHmOALce69WamB4AfH5KPFbVB05LkgBs5EXmK0hkNLNU9s3SEssTAwTBDFJgdVjCv3PywfegSMK5kjWRkjRCwZ52orf4kQuyVXfHfIsDsviEBaqh96EurMwMHStVp4Z1WFBTvROmZvmiSpLy5j83uFH8fxnbLPYwYpSsJEzNUVk_BmEPm2E-GcGJWs8xaYt5bMlRSzJueuFIZf6Uk1J5Oq9nOZcDpUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نودا یوشیهیکو نخست وزیر سابق ژاپن در سال‌ ۲۰۱۲‌ درحال پخش تراکت کنار ایستگاه مترو
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/690918" target="_blank">📅 17:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690917">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuy0GuL_MhVc_jUKfctUOYVOsQlXeeFhn_O0NbUyPmrMxW1qp1IfvHmqybWUUXAyG0TIR-yoz-JG6awosJg2cZSibjqGkeVPQozyW_wP6Q--v8wEL6YAK1AAscNNvH9sWZ2r_EwrgSrDS687etNoIOl2ypzZ53POcgcidb8zQV2AI8g828kEMfxKp2zEpkngxlHv82f6o2Nrnw7_yZs03hgERro1gkjQd87yqMVDn_aeil6SOFg-XNIejouySwxQOZ6Ou-8fTXlgYyk0alcBXeEMtLNK7oRdt88MYG_tNMQgB9YVYz7ZErcqcPscZd19GgAraX2Tw2FFGkQEXA1x_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
منابع عربی خبر از صدای انفجار در شهر طائف عربستان می‌دهند/ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/690917" target="_blank">📅 17:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690916">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adce80df20.mp4?token=G9d7uQHvoOLOEP9HM72SxRJe-Sqz1KZ-9vl-cVDK68tsMDTSjsm_MMhhD3eHXC6w8MMfReRhjDZ_PT4fazFtYph85nbAYuXYAt4X0ewWPAoqq_2meIKDM6U8bKpAv8o3vDw0EGzXZicUv8fYoAH9TCVKV6uHC5WAOTJO9rxgs7kEkTZnCNsknml4-FhXQFNnwqQ42zxE9-lic0lMBPl_kMxA1oXJwmGVR1F75CHYhoP3u0h55-wDkJwOMp8MXAD9P1KNOfcDqdThjsfMkNwviHRnu6ssYiwRfAZzYkmEnL_hcEVRiCCxLbwLRc2S2GDP1HU7YEj7mBuCFUeLcEnxOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adce80df20.mp4?token=G9d7uQHvoOLOEP9HM72SxRJe-Sqz1KZ-9vl-cVDK68tsMDTSjsm_MMhhD3eHXC6w8MMfReRhjDZ_PT4fazFtYph85nbAYuXYAt4X0ewWPAoqq_2meIKDM6U8bKpAv8o3vDw0EGzXZicUv8fYoAH9TCVKV6uHC5WAOTJO9rxgs7kEkTZnCNsknml4-FhXQFNnwqQ42zxE9-lic0lMBPl_kMxA1oXJwmGVR1F75CHYhoP3u0h55-wDkJwOMp8MXAD9P1KNOfcDqdThjsfMkNwviHRnu6ssYiwRfAZzYkmEnL_hcEVRiCCxLbwLRc2S2GDP1HU7YEj7mBuCFUeLcEnxOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا بهتر است آب را نشسته بنوشیم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/690916" target="_blank">📅 17:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690915">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4HMjKZWcY9ynhcoPFz_ly0rm_gzT_GLCZVN3FE5nLKnE6ctQCJmrwvLPmJ45JLKXnvunNIbG9wJ46YT9I1qWadjYVUuNh1U-Leh_2_3ztQFDQGDPsNOZO-GVzBg0t5zCOe3YSNQzCAOWdFwVUPhfIEr_4zcflh5SL8w8r-SlsAwXFqQUyYqwn21-ehbUP3_4eixXxSlNhD02b8z7OrePxOK-fnGbI6jL7NUWMSkS6ksHugX0dQMPOztGRrujInOzmqQHCo6aO4ijbhAuSrQCu7Mc_Sh3Zp4wN_K3Kpc9NAmewupJtNjhkX45p1G3TYudqwUmQ073tjektHE1HFdew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷۵۰ هزار دانشجوی جدید راهی دانشگاه‌ها می‌شوند
🔹
بیش از ۷۵۰ هزار دانشجوی جدید در سال تحصیلی جدید وارد دانشگاه‌ها می‌شوند.
🔹
از این تعداد، ۴۵۰ هزار نفر کارشناسی، ۱۵۰ هزار نفر کاردانی، ۱۳۶ هزار نفر ارشد و ۱۴ هزار نفر دکتری هستند.
@amarfact</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/690915" target="_blank">📅 17:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690912">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IaJdjp6Y2KGEK2YOe5ditScZy3kSaNXbEyU8DF6L5t__mUutOP8QXdUPERPuo214wWEqWy-gMM3Trso3nvnor98WkLkogTKIUz_XA3R1MCkUeBkNK9fln2iHMhDlk0jBkafb33wi7rUWGaEIOONQRoOtYtT2dmKfxFKVhgP0Bhdq23GcecTib_kKJjmG-TFPCmlfBqtUtvXH0bH0mi5ZFO_qTpox6MIp1fJ8r1gQtNFkGZEirWW-FhTQf5645BZLvWVsU_GYf6oCY450m6eOey-LTQqzBEVOABisaFMwbrTeQClMjS7QkLJ7SsIZs7eQJOR1EAmMhKLtm_NtzWJovA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M2YOd7bmxSXX9qYWs3kYzSXenHCrsWCRsfPZMpCOYFsPnFwAGVMBbyfisAm0z-zKbyVsXj7EvsRNzbcOzUowlQ_ikPWW_dkrsvJCjSM8rBReQP9cqtY1MaSDEk7QMnf4d3mVw7IhwSZptck_fKpsv8VwWLgd4lGx4FHGSq9RoJ8bO2GwqItrWt5EteToI7-GSMrRAeRJf-1IeMWYOfrYEya8xBdjFTfEfY6nfi5LQoflQsixGhxmFzc55pJJXUkFIsVUUfB9VUpDuMbQt5ShEKye85RxOy6eiA_HC0modvQHRazCMQjqHH8TQIO2cFcoMy0REhGWgBe22plLtWQMAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KQWMU4LNlbqVx13vgBrPrVgP6S1ju8tRBJne0owXRM9j36NqKdn9Lk2YFhEFBu_k26kxVH5K50l261YkoiDt15-A6-iIDp9qDNgItGZkMt9V6ZkT5N4pOUOsC5aQ7JaDjiWXqRiMaRkzrilaCMuBZJ1FkxxB9HAMBYLiktNw_J_c7xL5gaM7BMvircfWRSD_8D7_HV3j-fjxzrshap1tIgpFxXBzYXfT_e8MKX3Dito8XSKgTrgxHr29B_ffnPTyhqOABEEBkcJrxkvsgMpSuukGMFICjPTeEulSyrS3tjcoIvTfFOuDVi_Dy27ZH0Nu4h9vnTDa3tl586zzNOO6Ug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
عروس رفته گل بچینه
🔹
حضور نمادین کاروان مراسم عروسی سیریک در رزمایش جان‌فدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/690912" target="_blank">📅 17:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690911">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cd8152537.mp4?token=dQKaAvM7xXRdJbPga1iHJomP6ac311W04uNEr6gIwi9LmnBmk82eswbyyholSUnBoQNButnj-TjOZTfLJ-LvvcK9S3d8Ie274g7HRSb1Q4O69bMxcvePpTGpYaLBvwsS4kCVApbz4Xu_0tKJ1W-diHZVMh0svbx7kWyrGB8IP_sbARjII9Uo2pjwcpBJuL-3nSYYvqie1Jfr3cbLly6MxK-09_EOyS5lXx2Pk3ZynhZ-iXa2XcaHCZovT7TRENJZSHsXMpRcf1_b5efVebWNvKR5bQsqhi8xmrutkbuVgNkFwCDNOHvrZBPjF-uknaN1Mh8ZQFr3yefyVU95Ugx8n6xCk4jtuJ8eMVNEfwshJ78K3HHmt7eUgriTZ0ofv6T186GbQEkuCdt4jzIoFKPI1D1vuE0AbOJCeNG6RjfQUqIKgI20DcAc-upaOg3tLa0yitL6g2gf7fWJ6xqip_PJ6FZJ-aSDbtHOqUG86uQEirH3vTW0AD8FLQgIfA5epTaQS0lyExGFa9XvrPiuv7G9ngNDEzLPMbbGZX9W2njeIvqCijq1UajGcmgoFn0qGO7Uqxt0M6L9jGzRqr8H5HeC0sS8_ENL5NqIaSsowtAbEglrzULN8OlY18uwDLhSt_pwZvl3Nxk8aWuWkuxneabBHjCN7weDuJGKkruarxOPmII" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cd8152537.mp4?token=dQKaAvM7xXRdJbPga1iHJomP6ac311W04uNEr6gIwi9LmnBmk82eswbyyholSUnBoQNButnj-TjOZTfLJ-LvvcK9S3d8Ie274g7HRSb1Q4O69bMxcvePpTGpYaLBvwsS4kCVApbz4Xu_0tKJ1W-diHZVMh0svbx7kWyrGB8IP_sbARjII9Uo2pjwcpBJuL-3nSYYvqie1Jfr3cbLly6MxK-09_EOyS5lXx2Pk3ZynhZ-iXa2XcaHCZovT7TRENJZSHsXMpRcf1_b5efVebWNvKR5bQsqhi8xmrutkbuVgNkFwCDNOHvrZBPjF-uknaN1Mh8ZQFr3yefyVU95Ugx8n6xCk4jtuJ8eMVNEfwshJ78K3HHmt7eUgriTZ0ofv6T186GbQEkuCdt4jzIoFKPI1D1vuE0AbOJCeNG6RjfQUqIKgI20DcAc-upaOg3tLa0yitL6g2gf7fWJ6xqip_PJ6FZJ-aSDbtHOqUG86uQEirH3vTW0AD8FLQgIfA5epTaQS0lyExGFa9XvrPiuv7G9ngNDEzLPMbbGZX9W2njeIvqCijq1UajGcmgoFn0qGO7Uqxt0M6L9jGzRqr8H5HeC0sS8_ENL5NqIaSsowtAbEglrzULN8OlY18uwDLhSt_pwZvl3Nxk8aWuWkuxneabBHjCN7weDuJGKkruarxOPmII" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جشن تولد ۳سالگی؛ برای مرغ!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/690911" target="_blank">📅 17:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690909">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
ایتالیا ناو جنگی به باب‌المندب اعزام می‌کند
🔹
وزیر دفاع ایتالیا اعلام کرد رم برای تأمین امنیت عبور کشتی‌های تجاری خود، بدون انتظار برای تصمیم اتحادیه اروپا، ناو جنگی به باب‌المندب اعزام خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/690909" target="_blank">📅 17:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690908">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0278da7f4.mp4?token=p68iGRy9qVYWpqy0H8Avwh9i4vlnq9GANTvc-YOjddUn9d_tWCoyA0rCrN6YmPaUjcNReXh3kPvAhJZIJ2-bddidM52SbYZCgwFry1vzGdu4U2sG2ICORCxv7cNY_Md-nrdb4xmXLmACekj-meyStOKiubMiqc3NRWnr56wNBcdWHMaOeijbNno4GlOYy5ImoEP5R_Y4xJy8pRjm3UyKgRQIRsab6MmsrB2jx0OD1bPJcLGR3GWRn9VRcY965cXtTaYe6bf0kzDftlTTOxNHEKs-4Or-ReJA3RwNS_FqiVNQHvfsZqxULQFjp4H3WGD--NW8m0pjZEHL3B5JLQoFDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0278da7f4.mp4?token=p68iGRy9qVYWpqy0H8Avwh9i4vlnq9GANTvc-YOjddUn9d_tWCoyA0rCrN6YmPaUjcNReXh3kPvAhJZIJ2-bddidM52SbYZCgwFry1vzGdu4U2sG2ICORCxv7cNY_Md-nrdb4xmXLmACekj-meyStOKiubMiqc3NRWnr56wNBcdWHMaOeijbNno4GlOYy5ImoEP5R_Y4xJy8pRjm3UyKgRQIRsab6MmsrB2jx0OD1bPJcLGR3GWRn9VRcY965cXtTaYe6bf0kzDftlTTOxNHEKs-4Or-ReJA3RwNS_FqiVNQHvfsZqxULQFjp4H3WGD--NW8m0pjZEHL3B5JLQoFDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی تغییر چهره رویا نونهالی صحیح نیست و مربوط به مصاحبه خواهر اوست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/690908" target="_blank">📅 17:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690907">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5Ufkit4w0JlmxYgrqehkwq0RjzFgQnG4Mp0u_47O0AcyKFfqSK07ahZ31CE-SIrVaimWToQVO0XcZU-s_JpbKPLhHHGLX0-YfQca6Onw3kpdS-5eQBkkO7SzhvhTRGLmIOIth2q-5tYPE1YMslrZab7KqccZdLCUOrEVWxQUMKwCnx7eIEiMS-afOvoxxQ5gc9KCZjtSCU0mhzbiVnp_i3sWvA4tUctB-Z_0bvfYifc0BXTkzz4WfCRyCrVC15hpcIsaUVtzpND39gV3umIsOrJdWvnrrXfOwKAgiywzMyVJjdJ_bWjnJS95WaoI4TS5vP23gnr0X04U7kMrue4PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از ۹ نفر تراستی که طبق ادعای روزنامه کیهان ۱۱ میلیارد دلار نفت ایران را فروخته‌اند ولی پول آن را برنگردانده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/690907" target="_blank">📅 16:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690906">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c705d1f9e.mp4?token=QwERncah59u87AfWuQL6PEu9tm-3Gakjzd8EXvTftMQ60Fmk-D1yts_VF8_aJGxQ4ocJu3X8TkXS12KCJkAhG57gI2JgRHlj6Xo3BL3ZORIiCCxMZhEempWamwUC9yw-eKfnqGaT4GDNXGOnB9nCPI3TpGeY5VQvc36icVrc4ecNXQqG4FuqJt1ZQgTupBTZ0PiWn0Jyynssju2Da-gT9IqQBwxZQoAIEw0XBTCn9_kzGbS6INq7iZTS9u75mKRpTOm9KlK5vgWV3X4rWCyACKSFY94Jxho9eIIA2ww0ZNKFwkPwV0ze2nXoKPBXUe-7D-P0lBQh9d1yNhYyTWOTHQi5YMJt5ZY1v-Nw3FTqbNI03YCnw82NzX5MfqK9kL4RBmAwNcza98tiDiPcd_DrUQ0BgKl6hxp6qFsv2Q-TFqPxbRKBC4W-Vn7IQIIq5P7L1oxcKeI3AqrqImkZ-21xiZuI6p8k5ABT3hbK5xvybLtYJ2xdriUnHU-c877Xwd-LpWxqZI1rIjEaA1jSLxllUuh6m6pUxKp5XqUJHD3wg-9eDxoGG1nHoHRqz2mbX0-CMkAB-SP3QlRO8qQHsfPpfL6OSXaFUghqoWSOjbHo2JEaXfH4Kcz7rd-I2eUxLbcN4gpugxynbX8G1b4gglcpRI-vgZRgGEGczp_a-hS45mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c705d1f9e.mp4?token=QwERncah59u87AfWuQL6PEu9tm-3Gakjzd8EXvTftMQ60Fmk-D1yts_VF8_aJGxQ4ocJu3X8TkXS12KCJkAhG57gI2JgRHlj6Xo3BL3ZORIiCCxMZhEempWamwUC9yw-eKfnqGaT4GDNXGOnB9nCPI3TpGeY5VQvc36icVrc4ecNXQqG4FuqJt1ZQgTupBTZ0PiWn0Jyynssju2Da-gT9IqQBwxZQoAIEw0XBTCn9_kzGbS6INq7iZTS9u75mKRpTOm9KlK5vgWV3X4rWCyACKSFY94Jxho9eIIA2ww0ZNKFwkPwV0ze2nXoKPBXUe-7D-P0lBQh9d1yNhYyTWOTHQi5YMJt5ZY1v-Nw3FTqbNI03YCnw82NzX5MfqK9kL4RBmAwNcza98tiDiPcd_DrUQ0BgKl6hxp6qFsv2Q-TFqPxbRKBC4W-Vn7IQIIq5P7L1oxcKeI3AqrqImkZ-21xiZuI6p8k5ABT3hbK5xvybLtYJ2xdriUnHU-c877Xwd-LpWxqZI1rIjEaA1jSLxllUuh6m6pUxKp5XqUJHD3wg-9eDxoGG1nHoHRqz2mbX0-CMkAB-SP3QlRO8qQHsfPpfL6OSXaFUghqoWSOjbHo2JEaXfH4Kcz7rd-I2eUxLbcN4gpugxynbX8G1b4gglcpRI-vgZRgGEGczp_a-hS45mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت یک توریست آمریکایی از پدیده «دور دور» در ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/690906" target="_blank">📅 16:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690897">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZo4qj9m_J0f5_UezuAwHNXyvtyLJ8_bNeSL4zkMAZQggN6Adv4LxZ1bG3XmW3BmaXrD2DGPuV_loznkHsCzpLLMzpk8HekilIWmnOJiDQcTkuozef2Oxqv7SZfJSvwB-gR9z_z8DdpWS1PC0khzU5HiRImrX2v2z9-VTgTl7LZmXOZVl_okpMf61q3GU8HSqMWUOM1JARdv68U61gD1g_2RqhjAvL0Xu0zbjWhc-nVzE0DmG7KcwIsePg7U6KZHNBFizYHJ95UPE7CPooW2uiPBtNTRTZvuLnVMAkcccELsqBP9GNKRkxLBvEQLhV4-IzB4etqMmCVTSHj1SUWShA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P6fzwc87MXOxc6RQKR_CFkA47e_i9eCcyHADefRHniT9Titnqps8P4HeFCzcBCrIlbeTQ4aRLyedmdJ1ojlroGpdvbWnfa0OLy9zrRQJo_rqqjzH-gXdshc3pf2btp1TTay193Brlbffs80Bzx8vKcJhWb3UWowGkOTOITabUzAkAHW2Dd7Xadby7qAniRIcvBvhIFZmsRgFjw785LniszYNd1ekAbZFj8I_WaM3iHIwuYjT0C8PiZOMEOMX7BlxAUkh3IomJ6n2H8ZEmB1d_qJ-KcvvLWmG4hs2Sdjays5eShqZTnhAF-p4S8gmshzJpr8H8Jqva0Gv8UEcq6i_Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GdzOTYQZFD3gqXbeeSN9fyyZZckDsozWdA_yWjbBe1Ydfy3Kv8tc19tJM9IDXwMLSuGWar194LYSYnzaOr3upeivm_kSlRCmuu8dLzvE_t4mZMOkms4Szdp1KVrCdpePgsZUOltDbf5O0uxYLFVbTxuMP2e9RVs4uUmHVY3X0mXJ_lf05nBFgjOeigP7oZIGAYXiwt15b93Q5Hx2w3niEJRcPYZ75ofXTRHqfk2qxECt8q5jSqUqG_1MBoqgj-Lhv4smun117WDpD2Y1uSg1bIxiAL0y2-GdXkqdwsxWEEYoW0fudUBw_X2ojb3AkBq-9GWU7jeoymctnaS6VYg8dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eQsWcgKRF2aNa1OhLjxK4hlFjJb1EmaB0kcEY-VPCH0GfcsaegSyG0U9JT_umhfGboS4mbeRbpYrETT5iFXKaA1Ve5_G-PUvvS-serZnb2rcNzunGbgB7t-BgrdfnvqjhjDP0Av-XSsvLzq2o3RlGT7Ndd0GCvUhlMo_2XKgoE9VR0MB3r-Vtfj5EBGPm-4Wvd1hbrXgZK1_VO3p3q8Eslcy8B5WOfAbXhfvYSgMaMcXqYnlPeJx5K0AB3eEKi0PfRNJ-aG32lpXcRXHd-sNWwFYnw--XVJC62sFSutnfEdidBzJSyqHeJDma6tOZWUm_6SCktGjDTslOgxXXFVx6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jc-zBoZnJ39z85sELhFTPHejLlJYjvDBeM0YhQk8cgoZA27VLusZRT2PlQkBh489T73Pbo7PEWl8uiCJaeTwhOSJNSN2yjkki315Hd6O2gBgxZiMxOlXbrIuVw-r8UPIQ1qOlC_cJaWxBLF6psUnrjUlZ_6ov0zlVW4hQiS9YFF4vuCBLWFJkItmQ9NQBCrDsadCXBgxibI_J2WRNyV26SOJlyiOh0dW0McmAe3_FpGQYYwKQlq73eH7TGGrbMVzyYcrmWUzDSl3puJdulgpzZnb5W2QSh0L3k6nXVJaYSi9UKO81ekj6K1EGQxt7xFOM4Va8sXNByW_dmAGuTVE5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pkFmhHbtquIEhQZIHmk9WKSNyDroPxdyktf9x3150SPSgvZkFoUOJkjP63ErhKFdinQM6Crs3F7fIZmLZpYDHJJx959vDQLH1xGLsRX6FTLo60CIuSbx_YI0HV1hANX68UuoNLfId3a5Hu4ZBqv-wMZUpjt00Km3Mg8-uqErHksi0bLPumVxbwOTegp4Mx-HlyBhbckDGHQtKaQW2zSwgLuV5UUZGcJPZcG3NJW40nLOxN03wUnblsPFXvFXCmgpX8TjXzOikgn1tGFs-4DKxF__fanFOsFy5w08PwivgtDMNTua_G8gLEsQFvITxr-5EQ8Pd5kVxfYCTl-2xe2huw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M73GjLt2cD-Iq64gRbPsoIpMvs_EEmD4A_roisQdA12QKvKs941ThrE4Fe5HfDlOrNpA_NVrrdksHcxPRBscfxiMcFAWqz-XFpWCh3ud2N5Ld3ZB3jEVvA5k48F1XoumTzJAvzrANOCNIyMUMRRblaqUuIS7EKjOr4ipbcy5aVkTvk1BLhRbFpZ_DSp0kVCl88YFeZ8IuGy9rubED_M9pObzJS9j54mN1PX2Lj_y6LedLqAv2gE2k7IsHyluUAW5YF0FyRbqbwyoG4_ATPhVUVZEvZ1Xc5dygNwVv4sSjAdu-snqYypMDTaYbWuy7W1hqUOqOeGcpK0bbTEDw1RR5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G2XBHXZ4Dunk42azIQhUVryu9wVxLWRxNb71XRir7MUiG8UezSGHRqLWxne_PMJ9JaMdVtJ9KJ5TPVIUVXuEdKFEVblwapq4kD3IwQq_Jm22iZrZKYhO6DNA9SGx0jkpmuJZsVeeZ_dFsTkrANBaAY21BRRl5vzmouKEm9S5BT3ujmAk35LN6cpZzHTH4C-t2COrq7_dGXMrj98lJKUXgVZ25h5r75pGSRXWxJFl40FmCVoxtIKnrOmPHKs0o9SED0qVVTmIP31sHO9lPqS188fKfjRTApyCF66XF4DmnE58ENYcfJfcTEK2qznEqpr5AbrY9sb3yK2Uk8Vt5HoUmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lG6fW2GbM5VRcIDEAOk8BA5kh6PZl4aoQy6WFtUV5dX6E0iTLWqBjGceB3kqJoRBpyvcZKYADHFX9y8AvVJha7-Ur-0ljIHi-nCm4ck44Y4ZSGmX96BWaWRhi4Z5HWInwpgE347XjSLBPEtOlW5JZqTcZyS6TDrSYJb5ALYlLPu0aKbwM7qypHkACI-clqIb2ctgmWlFYxxttnSOlkdNIiGYsv0mAwXDJKOuXrY0EPOoGrsw5aGdx81yC6CQAd-RpQqJSxOHs5hT-NRYn-GfflCS9jyEWkpD3tK_o1OYh4Gz9jFZqee2c7NjnYKW1CKG2No9pUtsSpxl_UOSGgixJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور ویژه زنان با پوشش‌های مختلف در رزمایش مردمی جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/690897" target="_blank">📅 16:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690896">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
ادعای چاینا نیوزویک: تیم سعید جلیلی به ترامپ بهانه‌هایی برای بهره‌برداری سیاسی داد تا دور دوم مذاکرات اسلام‌آباد را متوقف کند!
🔹
انتقادهای تیم سعید جلیلی از تیم مذاکره‌کننده بهانه‌ای برای ترامپ ایجاد کرد و در توقف دور دوم مذاکرات اسلام‌آباد مؤثر بود.
🔹
این رسانه با اشاره به مخالفت جلیلی با مذاکرات منتهی به توافق هسته‌ای ۲۰۱۵، بر ادامه گفت‌وگو میان ایران و آمریکا تأکید کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/690896" target="_blank">📅 16:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690894">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f234919aa6.mp4?token=YyRaybkVt5oGFAC6OOLRJuzWWvV6TKartK09ETJ0h-QZ-FVEMoYGUb3Y6CGdNZWsUj0DG56fuOS3iXqZbqZNEDnZHHV3d7OlA1lK9AgZyltcZBcDIDUwnRv0HiVEIQTHrpcOFPLvpOxdxQqkAt-xnIIJ37FCONmqRH1-kuYF0DU3O5Xe5qqHfXo8UFmvyE-4iKjl0AZY9zLZd55N2vhu4fs0ERKOOxwPzE8LIUUNsoFczRKeZ5pd01lDBNy77Q-pXSZw3jxSLhwE-j89DxkPTC-5bD69v14HX568lJ3PuW-Dm_cKKl9HocSk-cI-CACF0W0vUfq9aP54wg08UPvRMoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f234919aa6.mp4?token=YyRaybkVt5oGFAC6OOLRJuzWWvV6TKartK09ETJ0h-QZ-FVEMoYGUb3Y6CGdNZWsUj0DG56fuOS3iXqZbqZNEDnZHHV3d7OlA1lK9AgZyltcZBcDIDUwnRv0HiVEIQTHrpcOFPLvpOxdxQqkAt-xnIIJ37FCONmqRH1-kuYF0DU3O5Xe5qqHfXo8UFmvyE-4iKjl0AZY9zLZd55N2vhu4fs0ERKOOxwPzE8LIUUNsoFczRKeZ5pd01lDBNy77Q-pXSZw3jxSLhwE-j89DxkPTC-5bD69v14HX568lJ3PuW-Dm_cKKl9HocSk-cI-CACF0W0vUfq9aP54wg08UPvRMoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل جمعیت در شهرهای یمن به خیابان‌ها آمدند
🔹
جمعیت زیادی در ده‌ها شهر یمن از جمله میدان السبعین صنعا تجمع کردند و حمایت خود را از نیروهای مسلح یمن اعلام کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/690894" target="_blank">📅 16:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690893">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3785fb895a.mp4?token=EHixS4QVoruVKqunkiIyN_ZBuDHR9vzhSNaysCyV_hDVWanmmieu6WPG6eIwI00iYClLd4SkqxNjh-WF5p8getr6ad-kQOKiUaTQH5vdwR375SK6c1uPpPoz6BD68hri0QoY_G0K6V-nA4YT0lgoVtTG_JpZ0_5T3BT6MA5fXtdGOr8itvjj2SNBUQkM0nNgBtIcqYmsUXbWit-g9Tp1AvqLdp0W-Ixw-QcZQ9ucDDC3mr-oAU3CgJWIM3NC1m2ky_Jtl9CrfoSaTrWfUUS49pren6ACwlLPNvtWzCUpCG8_lGDiOyZeXCABMi8QXgAP5wKXuAd-uck0V95lnmIC0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3785fb895a.mp4?token=EHixS4QVoruVKqunkiIyN_ZBuDHR9vzhSNaysCyV_hDVWanmmieu6WPG6eIwI00iYClLd4SkqxNjh-WF5p8getr6ad-kQOKiUaTQH5vdwR375SK6c1uPpPoz6BD68hri0QoY_G0K6V-nA4YT0lgoVtTG_JpZ0_5T3BT6MA5fXtdGOr8itvjj2SNBUQkM0nNgBtIcqYmsUXbWit-g9Tp1AvqLdp0W-Ixw-QcZQ9ucDDC3mr-oAU3CgJWIM3NC1m2ky_Jtl9CrfoSaTrWfUUS49pren6ACwlLPNvtWzCUpCG8_lGDiOyZeXCABMi8QXgAP5wKXuAd-uck0V95lnmIC0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شغل عجیب در کانادا؛ زندگی در ارتفاعات برای رصد و گزارش آتش‌سوزی‌های جنگلی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/690893" target="_blank">📅 16:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690892">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f46e85377.mp4?token=ZVVhuMaolvmXXJFZghvOrGnEdcPYMsNG5wUgByRmSbG9C_jnc_UukFYSxb4yRIkJLHEkrsao1qMsF0_fEZf1jBGUEvW7DebFojLWVIWtzTADHYAMimgqB2DaqDpyMWEXk5HRmcq1-BIF6Gy-Alp9djpEu5uE1Vh0Jqb6-cCQU594DfxtlH9IXN8R-lydqkt6hc8tCz_W_S4cXWDpc21Q4UIaSXRfQzUHQwPI3CtebdqGopF3_fQml1mUgaXSL6JYIBKAkqZqwC0KwyyJhI8ygc5E_fN3X6tYfwqWrOzFIC5xLAyorWtgBGBd6Td5j-5nbjZXnC8N9gbvDjesJvoZxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f46e85377.mp4?token=ZVVhuMaolvmXXJFZghvOrGnEdcPYMsNG5wUgByRmSbG9C_jnc_UukFYSxb4yRIkJLHEkrsao1qMsF0_fEZf1jBGUEvW7DebFojLWVIWtzTADHYAMimgqB2DaqDpyMWEXk5HRmcq1-BIF6Gy-Alp9djpEu5uE1Vh0Jqb6-cCQU594DfxtlH9IXN8R-lydqkt6hc8tCz_W_S4cXWDpc21Q4UIaSXRfQzUHQwPI3CtebdqGopF3_fQml1mUgaXSL6JYIBKAkqZqwC0KwyyJhI8ygc5E_fN3X6tYfwqWrOzFIC5xLAyorWtgBGBd6Td5j-5nbjZXnC8N9gbvDjesJvoZxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همزمان با برگزاری رزمایش، دوی ماراتن ۱۰ کیلومتری امروز در بوستان ولایت برگزار شد
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/690892" target="_blank">📅 16:36 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690891">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ced362324c.mp4?token=I9mmBkGloMEA8_17W9RIfZHWZnPI9Ix2xkR1K-JLtlXXeAicDqc-kDCGOBJP6ZyicG-pz-_jCxppa6aZZLMmP18Gc7fW7TigPNZCMzUpIaJNV783F-SpEruPCX9blTqdNpux5lCWT6RA0x2pTicihKm9O0KHr3H2ntoyCKAl-0ZxyMLGB4YMLAJCRZ9b5ZXXXT30-HvWm3W26_egOo1IT8JcTTKeaDydLdjIHYGe6To0h2pE2P7gG0soJs-yFU6z972lEL_Ae5T26pin_1pgoCGGZraYufQIwo6hvtHhq0dSXkeBq6QSI3np_wMGYvqqtmhfIb8eQ7c1AwPjVhtfqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ced362324c.mp4?token=I9mmBkGloMEA8_17W9RIfZHWZnPI9Ix2xkR1K-JLtlXXeAicDqc-kDCGOBJP6ZyicG-pz-_jCxppa6aZZLMmP18Gc7fW7TigPNZCMzUpIaJNV783F-SpEruPCX9blTqdNpux5lCWT6RA0x2pTicihKm9O0KHr3H2ntoyCKAl-0ZxyMLGB4YMLAJCRZ9b5ZXXXT30-HvWm3W26_egOo1IT8JcTTKeaDydLdjIHYGe6To0h2pE2P7gG0soJs-yFU6z972lEL_Ae5T26pin_1pgoCGGZraYufQIwo6hvtHhq0dSXkeBq6QSI3np_wMGYvqqtmhfIb8eQ7c1AwPjVhtfqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زابلی حرف زدن محمدرضا هدایتی و ادای احترام به سیستان و بلوچستان
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/690891" target="_blank">📅 16:36 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690889">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
اعتراف صریح ماکرون: تنگه هرمز اساساً مسدود است و هیچ توافقی برای بازگشایی آن وجود ندارد
رئیس‌جمهور فرانسه:
🔹
در درگیری منجر به بسته‌شدن تنگه هرمز نقشی نداشتیم، اما با پیامدهای آن زندگی می‌کنیم و خواستار راهکار دیپلماتیک برای تنگه هرمز هستیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/690889" target="_blank">📅 16:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690888">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sl8WaPTSqPy2eJK09jL-9rnwRViP4j1LUY9FkEnp-Q2XOr8AQ9Eq19Njlgphw43jQIRhF6-KY-NaEMarW03poo64nRRrU2dfSkgCcatohkOsFK-mpDfkXKIJP9DAVOprID4RNKKWp1GMfXAx_4TwyFpvE_yjBkqGHf9QkbAQ9JY7OLf_t2VV0ttngvEvU_7F8WIDl2vAerzRFwmXgatuEQPHZnl-CL9XlxTdsKEmcfIHHV_cTfD6CEZaf5hpQFcvEiS9PtNTPK_TiD8JulN_5O-2wPgSVicOyhVac7VftKDvbYmaJ6PFxbCdG4Qk9eL9jrYr2DHNyTfhnV1goMjEmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#دیوارنگاره
| تصویر استاد شفیعی کدکنی روی دیوارنگاره میدان جهاد
🔹
به مناسبت روز شعر و ادب پارسی و به پاس بیش از ۶۰ سال تلاش استاد شفیعی کدکنی برای ادبیات فارسی، از جدیدترین دیوارنگاره میدان جهاد رونمایی شد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/690888" target="_blank">📅 16:30 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690887">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nm4UvBFhMmlC90g7agKovfhoRThSXqXirngDdq7PyieqhkgNcYUwSkTPP6V9Zv8cYz0xwe26CWR29N1muC_cnZtnLTMcg9idaTJ3JdlRdBcIr1-Wa6p8pWDhp4t03isuGUBbB-PMoNml5GeOrpR8w3RrqmHtMsaUR1pdyIwYHeP7O8BWyUL-IzU1liO43tf4k4Hi1ufV0kHlnxZ4b6VCwiW2gUrm77OEC7Ule6RNFEf9E2RPXQ6yXKSHhYaDO4mfZTdoQFT9LV45br3bR9d5zhrWJp70QdnulOgdZtsmTj1f91vbJCN8KGzYrdIKhi6f7n0g9VcRS35uCNgOVDRWJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشکل اصلی مدارس دولتی از نگاه افکار عمومی
🔸
در این نظرسنجی بیش از ۲۶ هزار نفر شرکت کردند که سهم روبیکا حدود ۵۴ درصد، بله ۲۸ درصد و تلگرام حدود ۱۸ درصد بوده است.
🔸
بیش از ۳۵ درصد شرکت‌کنندگان کیفیت پایین آموزش و روش‌های تدریس و حدود ۲۴ درصد هم کمبود امکانات و تجهیزات آموزشی را مهم‌ترین مشکل مدارس دولتی دانسته‌اند.
🔸
کیفیت آموزش و شیوه تدریس، در کنار کمبود امکانات، از چالش‌های اصلی مدارس دولتی است؛ مسائلی که مستقیماً بر کیفیت یادگیری دانش‌آموزان اثر می‌گذارند.
@amarfact</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/690887" target="_blank">📅 16:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690886">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b17ebd898f.mp4?token=rsptvKZFaalfwXjXZHN4Y2ccz5Mle4w_Ol33JnmjRm7A2_5EVSU-mr_usq4V5qSWZiKIhAgZcg8bBSyL4J01bait21cUNvwN4ub8w7QEb_53NE8-EhoypJtJeJZQP1lOWKFhkoqWmU74zOHCUo_NsVvKGwVYhyeVkg9RL8zmMhr4a2jfIJJqQMx18hlW-HykBurxNYHTo8ZhQFlrlSmdzK_W6I8lSMEKG76g2hjGlMLaxIqG6Nqp3oEv-36sBENiXsdR5MobqLgn22eHnEBjdiVB-l5MVPHPzBwCtseUF-UFboLnWPxdMsaS1T94Gf6UMzc3bMvPEJRwIcqe4X6m-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b17ebd898f.mp4?token=rsptvKZFaalfwXjXZHN4Y2ccz5Mle4w_Ol33JnmjRm7A2_5EVSU-mr_usq4V5qSWZiKIhAgZcg8bBSyL4J01bait21cUNvwN4ub8w7QEb_53NE8-EhoypJtJeJZQP1lOWKFhkoqWmU74zOHCUo_NsVvKGwVYhyeVkg9RL8zmMhr4a2jfIJJqQMx18hlW-HykBurxNYHTo8ZhQFlrlSmdzK_W6I8lSMEKG76g2hjGlMLaxIqG6Nqp3oEv-36sBENiXsdR5MobqLgn22eHnEBjdiVB-l5MVPHPzBwCtseUF-UFboLnWPxdMsaS1T94Gf6UMzc3bMvPEJRwIcqe4X6m-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سفر خارجی بدون مطالعه قوانین/ جریمه شیشه دودی برای ایرانی‌ها ۴۰ میلیون آب خورد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/690886" target="_blank">📅 16:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690885">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f7ca0163c.mp4?token=tH9Gt64w4WnEr3vEUhGcZRWHiBx7UiCb9-qAetfIQyzB84KG3AlZ4W-mZxcS6CEaSYxdGge8ufaJzeSXQb6_D749Zztb8xdQVa4fKhmz5fMytPZjKpTtzxk0fFKbbWKitfctkD4aMIObjlIshjK-fCxbEM6h58TgBih-4GgZkodCKRutoOKAJC3ulg5YiGw7kfiTpH224VwWpgD6Zyef_9KcRfNElLV99p_aE4Y9NIfTLZnLVTuyVsv_yYIJM2xjKrUzO0-sXNLj2oTNHl7lEQdvrj54Jr1pz_BKBFoJJaZa392BHs9kj1p-AVTvNVpr0VCvjEnbNwuRQPEtK2Y25joLcQK8n-h2Taw-H_6S7K0LJaup4jBnPqtUMHnrGpjolXz_f5F6XZtM8KJzz0_z0AwTJXzBhZfHYyTNnIhudTJb8IgbzHzRs8wvOPE9YKjETxO63GQoQ3hvFh78G0yylsoagpYOv6ztL8lQjVxJbfzgeH8qLmcjLRFvxqLsmb3emVcrjkjfgn0IV41VjvkiRSoejjY46C-6op-Nh_PFf0INBZ1uKyN1RTz2jD61_SWjuoMyY0zpVDlWfT_5LO0XvaXHxsxKssmywvUsgOc3ltAh3Dds-F28JxsWOe44tGLWwT5suJIj1jLY3pPyDcjRK9iKahbZqdgzNvaMCcflK9Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f7ca0163c.mp4?token=tH9Gt64w4WnEr3vEUhGcZRWHiBx7UiCb9-qAetfIQyzB84KG3AlZ4W-mZxcS6CEaSYxdGge8ufaJzeSXQb6_D749Zztb8xdQVa4fKhmz5fMytPZjKpTtzxk0fFKbbWKitfctkD4aMIObjlIshjK-fCxbEM6h58TgBih-4GgZkodCKRutoOKAJC3ulg5YiGw7kfiTpH224VwWpgD6Zyef_9KcRfNElLV99p_aE4Y9NIfTLZnLVTuyVsv_yYIJM2xjKrUzO0-sXNLj2oTNHl7lEQdvrj54Jr1pz_BKBFoJJaZa392BHs9kj1p-AVTvNVpr0VCvjEnbNwuRQPEtK2Y25joLcQK8n-h2Taw-H_6S7K0LJaup4jBnPqtUMHnrGpjolXz_f5F6XZtM8KJzz0_z0AwTJXzBhZfHYyTNnIhudTJb8IgbzHzRs8wvOPE9YKjETxO63GQoQ3hvFh78G0yylsoagpYOv6ztL8lQjVxJbfzgeH8qLmcjLRFvxqLsmb3emVcrjkjfgn0IV41VjvkiRSoejjY46C-6op-Nh_PFf0INBZ1uKyN1RTz2jD61_SWjuoMyY0zpVDlWfT_5LO0XvaXHxsxKssmywvUsgOc3ltAh3Dds-F28JxsWOe44tGLWwT5suJIj1jLY3pPyDcjRK9iKahbZqdgzNvaMCcflK9Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توهم ازدواج با گلزار؛ روایتی تلخ از اعتیاد و اسکیزوفرنی
🔹
فیلمی وایرال شده از دختری که با مصرف شیشه به اسکیزوفرنی مبتلا شده و فکر می‌کند با محمدرضا گلزار ازدواج کرده و دو بچه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/690885" target="_blank">📅 16:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690880">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/msva9Mo-N3mL8U1DXpahADRJshoprhXumrpuI0vi9UBM_9LlOPzgHaakuETouCxjHMDlp40Vv713hHA3UoC4x4B_0GmciP7Jk6thYuQPEwV9uhbTJ0zINdXzHutftN1D1hl07d-084Qp6I8ICg0YXP3yG8mOQ-Zj031LT7K5jvuTbTnej4-TFgRRWe7JemywFbTlPz9DYN3Rsv8bcpSzoMRBqmTtDg8UokdrK6ngd0rvH_HRZK5caA6PRr0vpvGs0a9wylxyX8BcklQW8AqLcuHPvJCTYXrTp-_ZsgT8NOY0jW3zdWdimUH9h5sisDUc-OL0QlwaXaq4mz_QK0iXew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sx7DXpFGZpWUT85XBZYmnUSW6fZcCO5iM-TFO7rTnU3ZGNxNMJSTpLT9fWasnOwtD8xa-ecF2CucskF9jnQtjOdZURLy20kTR6z8ypmB2io362PwdXU0vfbUIbcG_AFF7X912pfJGKb7plCsJLL7IKOtEl0qzVzKnibvxQvU4Zjc_pjeT4uo_g0DyseWoBHlWSiJQ8PyAUIgc6_Lv8z5sGMwttk-inIS9NKnz5wm-KYMT3NgVBV5b0JjdJW5R6Rww3XKqWCvYiBgeJ8WXV7AfQBG2h_Vrd5RZMb1e-hrgbviOuMbl7wA6LaOc7uNvL_MIQRGIA1Q-ot4kdqwGa8ejQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PoU2vBsb9FzAOOT8RJ96S64Aj2Iq2krxSpn_skO67_KuQeDeRTurpaidSpu-C7e5f8rdRpwuq6raaku6Ug-KCQYxIyD3cJVraTYsI1wmfvDDUMs3TMB4N7Yy87IjkxQz7os6NLpQqUbs4lSsnXkfYylrGaqR21j4Wi_uGSmyuDiZdKFKGNw-mb2rqS6ZtuurG4VE3NgwFV7LQGxhx94M9RGJQQV19ITBzpKAV1k9c_ceN8AdOtLrrXPtbdf39CkWODDbBElA-EBMITdt7x2SbD_yImEiXuegQaoqd0jiuWp9jUjRymAjbeYIISiOK6KLl5vgacfphtDOVf_GSZuNQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FiQ1aNO0HlzSx_o8SRgRkPHkp0aF4pEORIBLwK08PAK8xO1iqqsKmmA3b7jbIdEPmks5MFr29ftMRe-J2KdbVbq-y6CxOMPpIotjkJpCb8h7FeL5lNZ7QTEi5o2Ms6euqvtSjusr0yzEMJNUHuookhtFUzkFSfBMU2j-x1aMcPAjscPNJRqM-XrHnul26hZrLQUXSxOm_MTDYhR5JB8uRr5uzhiFcU7-8NmlbEgC-dIYQcTzPM_XvOMeNgiUP-beIIUrlc240o_XeToJfioSDriJa85BKcOTyrPBiH6vannB3Fgdn2Jj3M_eXtMMGpz4FDRY27-ckZLrMUlxZoKdNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uFv7uB1MQFhHB1hPDu6PSDiUzuvwDXvcodAUBmU2uLG0dtt15ilwGjTypJTKNAy6IrruL_NbsTkTeNdUf-IwbVYgwY_PfwvJYbhPwZ-LCEDOrFC2szjL58lsW6MWIiIXpcE7E5Xc6Y2UZhp4qLGwxlpEFBkcy98tVrfoQJ6D4fYM_rv1VA93N0yMtO_cLadnUvcsZDGOeTK5x8WT4-zLkVgUOnL__GqyHwLTto3JGU5Mlhol6GcCxxZenigq0snZlkIrpr_9hFTlNBbWaRbx95CifgwEpNWCxjkupWtz5zC3cOUEovZikK4HN4ISxzZ5d9cip5MNFpt6DDtKjkpbzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تا پای جان برای ایران
🔹
حضور مقتدرانه زنان و مردان سالخورده در رژه ۳۱۳ هزار نفری جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/690880" target="_blank">📅 16:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690879">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
علم‌الهدی: در دانشگاه نباید اجازه داد زن بی‌حجاب یا دختر بی‌حجاب وارد شود
امام جمعه مشهد:
🔹
در دانشگاه نباید اجازه داد زن یا دختر بی‌حجاب وارد شود، چون دانشگاه معبد و جای عبادت است.
🔹
جوانان متدین و بسیجی برنامه‌های مبتذل را تحمل نمی‌کنند و مدیریت دانشگاه باید با هرزگی و حرکت‌های ناهنجار مقابله کند، زیرا دشمن می‌خواهد دانشگاه‌ها را به اغتشاش بکشد.
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/690879" target="_blank">📅 16:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690878">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
امام جمعه تهران: جاهلیت مدرن با برافراشتن پرچم بی‌حیایی، بی‌عفتی و هرزگی و با عبور از خطوط وحیانی و زیر پا گذاشتن مرزهای اخلاقی، با اصالت بخشیدن به لذت و هوسرانی، یکی از بزرگ‌ترین جنایت‌ها علیه بشریت را با آسیب زدن به بنیان خانواده مرتکب شده است
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/690878" target="_blank">📅 16:21 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690877">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
انتقاد نماینده مجلس از سامانه علاج: نباید مردم را به جاسوسی علیه یکدیگر دعوت کرد
احمد بخشایش اردستانی:
🔹
نباید مردم را به جاسوسی علیه یکدیگر دعوت کرد، چون مردم را به جان هم می‌اندازد. صرف حضور در خارج و شرکت در تظاهرات علیه جمهوری اسلامی، به خودی خود جرم نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/690877" target="_blank">📅 16:21 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690874">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b050880355.mp4?token=Wqsf_RWe2CGDUb9gDTlwPyMuYMBGiW5ukeDljqvJ34DMBULRBUEyAOqKRCJ6Jzn9Evux1HR3gwbTtN5Nm59JlrMcRvdD5V6PJYkphu1ABOZB32U_IrNCkkMh9aEvv4mTIcCe2PT47SYHVfo6wA0MgkN5KHqKl-ArnK-2RQ1gzKVL9StLUEsx1DCeDRsK82EqGeWymwTShjqJ1zeWta6kerNnvEwPnNoI1TTzUj3YwQKNj-26BV6i9OK4x6SCDiDIC0Y4fnIwoUwvvcvD_gfVGYVREzQQHquVaZzW9dcq1fRft3eX0iSZKry9azvJHAb2oGx57znNuHrWmz_d3LehopinGqRFB2-bsg9wAtUTAA828ztzEK9QbSsIk_Gq21wOHFOa1-7Oc_7N_79auIY8IseUne9-9-Q42kSNZtz1IR0cqx2dOMMLYynZdwhOwHuue_iW8S0o_mAOgpXts2tONMAqQRkYWAn0XeLSJqUXkMHY4cGnz8C44KaEeWOOgXlk-H7vPAvGj9DCR2koG0mPXds-6QNNHJqcXywoGzvFv1NUnq3d2D3QIh18YWFHPqIHqGOAe-He5OmqGtdM803aml0GBR1OYgEY_lt6lAWewoiMxkF6Rs9B5-_rzk8rXIil7egY9RtOqnf0wFWSUZ7P5D5jUAVbwYcgrt3c3-KC3t0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b050880355.mp4?token=Wqsf_RWe2CGDUb9gDTlwPyMuYMBGiW5ukeDljqvJ34DMBULRBUEyAOqKRCJ6Jzn9Evux1HR3gwbTtN5Nm59JlrMcRvdD5V6PJYkphu1ABOZB32U_IrNCkkMh9aEvv4mTIcCe2PT47SYHVfo6wA0MgkN5KHqKl-ArnK-2RQ1gzKVL9StLUEsx1DCeDRsK82EqGeWymwTShjqJ1zeWta6kerNnvEwPnNoI1TTzUj3YwQKNj-26BV6i9OK4x6SCDiDIC0Y4fnIwoUwvvcvD_gfVGYVREzQQHquVaZzW9dcq1fRft3eX0iSZKry9azvJHAb2oGx57znNuHrWmz_d3LehopinGqRFB2-bsg9wAtUTAA828ztzEK9QbSsIk_Gq21wOHFOa1-7Oc_7N_79auIY8IseUne9-9-Q42kSNZtz1IR0cqx2dOMMLYynZdwhOwHuue_iW8S0o_mAOgpXts2tONMAqQRkYWAn0XeLSJqUXkMHY4cGnz8C44KaEeWOOgXlk-H7vPAvGj9DCR2koG0mPXds-6QNNHJqcXywoGzvFv1NUnq3d2D3QIh18YWFHPqIHqGOAe-He5OmqGtdM803aml0GBR1OYgEY_lt6lAWewoiMxkF6Rs9B5-_rzk8rXIil7egY9RtOqnf0wFWSUZ7P5D5jUAVbwYcgrt3c3-KC3t0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نجات دختربچه از حمله زنبورها
🔹
یک پیک موتوری در برزیل با وجود ۴۰ نیش زنبور، دختربچه‌ای را از حمله زنبورها نجات داد و به‌عنوان قهرمان مورد تقدیر قرار گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/690874" target="_blank">📅 16:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690873">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ادعای دراپ‌سایت: تحریم‌های هوایی جدید، زنجیره تأمین دارو و تجهیزات پزشکی ایران را با تهدید جدی روبه‌رو کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/690873" target="_blank">📅 16:13 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690872">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
ادعای خبرگزاری فرانسه به نقل از یک منبع اگاه: پزشکیان، رئیس جمهور ایران به نیویورک سفر خواهد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/690872" target="_blank">📅 16:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690871">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a47bed94a2.mp4?token=Dsbtr3NgBgCGewAjHQ6DUUAa7CnhorsNHVrzzAZfNtdAmgPJS8Ngn2IR5OM3hDgpN-TUs_JyyIoopsDBVqhdyidxaQu0szemHsUcoWJmezuiVr8KYFkS7PiDtF5jdgiUOEO0-yhfWmbqOB2ACfpmpG_t7hwiIekTD3loTE-EyOMTxMnW6qGzfPBXlwbybjkEPm4LUD4c9s7kPo7bctYpZf3xer6cZ3O2rRTgF3J12WeWntnvjLfSkaGwrSWFdI49li6EOcLOoHUnlnAXAyHGzpaRKwUJvh4y4Q7P_pMhha_X4EaXpw4fTTpN7YikAaUS-gx5JOdVXDAUM0UznofD5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a47bed94a2.mp4?token=Dsbtr3NgBgCGewAjHQ6DUUAa7CnhorsNHVrzzAZfNtdAmgPJS8Ngn2IR5OM3hDgpN-TUs_JyyIoopsDBVqhdyidxaQu0szemHsUcoWJmezuiVr8KYFkS7PiDtF5jdgiUOEO0-yhfWmbqOB2ACfpmpG_t7hwiIekTD3loTE-EyOMTxMnW6qGzfPBXlwbybjkEPm4LUD4c9s7kPo7bctYpZf3xer6cZ3O2rRTgF3J12WeWntnvjLfSkaGwrSWFdI49li6EOcLOoHUnlnAXAyHGzpaRKwUJvh4y4Q7P_pMhha_X4EaXpw4fTTpN7YikAaUS-gx5JOdVXDAUM0UznofD5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور عروس ‌‌و دامادهای جوان در رژه بزرگ جان‌فدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/690871" target="_blank">📅 16:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690869">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
کنایه مجری تلویزیون به ادعای ۷۰ درصدی مخاطبان صداوسیما
🔹
پس از ادعای رئیس صداوسیما درباره بیش از ۷۰ درصد مخاطب رسانه ملی، یکی از مجریان تلویزیون با اشاره به تجربه خودش گفت: «۴-۵ سال هر روز در شبکه یک برنامه زنده داشتم، هیشکی منو نمی‌شناخت!»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/690869" target="_blank">📅 16:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690868">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOtDuTgRArubKH1QkYaWcHQ_X9me1F88X7FiWJBiLYok9WQjWACLwI-r1HU8NLeppwe6GCN6muMsCpB7ciQTGHdKTai8gzItDDhQOoLgiwX-E_T0sd3MtOHNwLotMn04b_IlyreE_l_dvy0cYm-SpopgRDvAYQA5Kxw9lAz-_ci8aQ9rmrmS5h3NEHTHVzrs7WjMvCVJ5i9i3y-OEuznqdfsdrTJ0JvaqlwuioOFf2GYc2taxnOCJ4O7BpUMaRwRQMEP4g5BTEcrrwSrH1MnUsuQxW6sgqHrORn7uuAvvnQCkzUPjIe_P1JT_x7dsne7UicKWiGo-AUDJ27Mo3BiYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ضرغامی: امروز همه‌ تصمیم‌گیران و تصمیم‌سازان بر اشتباه بودن روش گشت ارشاد، اتفاق نظر دارند
🔹
ظاهراً همیشه باید مصیبت‌ها و مقاومت‌ها، ما را به راه و روش درست هدایت کند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/690868" target="_blank">📅 16:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690867">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6427a9e1cb.mp4?token=slbrhb21gFCybd_XTon3Z2z3Q3z3A5fJHPtkJ7MN6cw6gmYBh7Fg78ei_z4-IeAuirhPNxsojtkWi41XwKOVHKPy-kQiVx_NpdMtHSPVsMU1c4wARvP8GsfgjGeOlTIoEx1HbZmDRyNHnWilO4JAgw1mjtfyoPJmoSrh7hkDErhmyoFlTOoJecg7KLhVztkWiqDIdp_69mO3VQn7GFTTNE8mdZFOrpn7ABk0Y9u4bLIbzKOmhmUlwps-Bvwz5VFBUuKfda2lWeWMENhqO0wh-McGgDUn33Jd_HXgZZ3TMwbHQyzs3BbKokrN_MFbn2IIAZ9Q7vysiMpfYUohjgaJbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6427a9e1cb.mp4?token=slbrhb21gFCybd_XTon3Z2z3Q3z3A5fJHPtkJ7MN6cw6gmYBh7Fg78ei_z4-IeAuirhPNxsojtkWi41XwKOVHKPy-kQiVx_NpdMtHSPVsMU1c4wARvP8GsfgjGeOlTIoEx1HbZmDRyNHnWilO4JAgw1mjtfyoPJmoSrh7hkDErhmyoFlTOoJecg7KLhVztkWiqDIdp_69mO3VQn7GFTTNE8mdZFOrpn7ABk0Y9u4bLIbzKOmhmUlwps-Bvwz5VFBUuKfda2lWeWMENhqO0wh-McGgDUn33Jd_HXgZZ3TMwbHQyzs3BbKokrN_MFbn2IIAZ9Q7vysiMpfYUohjgaJbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت ساحل دریای خزر در روزهای آخر تابستان
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/690867" target="_blank">📅 16:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690866">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromزی‌ ویژن | zeevision</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfEbYWFP4jB8ORHMAra1EXkYloZrzMt4XRfF6KcVbrtEXi5S6ulhudC2XFSBx7SGZmaH4DyMwdFLKmdz1Zx-JBJePeMo1LXyZHnE-PSKtz-jESE81D7ApDsl3g0xNENK0UuJfa4lRhRnjcbSIKp-SKyMB9ocN-G7XI3TchfsG8_KaRC9uYQxUTAvdfHdljXi1jZXosTL4nr8sWtcJVO_FRmVB9DskUm0L970szZwSuvFklkEbOnOeBDXcMPymUedTkqttXoQRm_BFIp-F-mFVxzbRLPsodO9eY10L-os_r5xkfuEkTLZzttYxQ_Q_FSqxqk5T8siLxllsePmHRjG3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«یه بار دیگه ببینم بشنوم دور و بر اون میچرخی…»
هم اکنون تماشای قسمت سوم سریال «نیم رخ» در پلتفرم
#زی_ویژن
تهیه‌کننده: علی طلوعی
کارگردان: رضا شریفی
نویسنده:مهرداد نیکنام
محصولی از
#نبراس_پیکچرز
تماشای قسمت سوم از زی ویژن
📣
@zeevision
🌐
www.zeevision.ir</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/690866" target="_blank">📅 16:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690865">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه آمریکا به الجزیره: هیئت ایران طبق تعهدات کشور میزبان در مجمع عمومی سازمان ملل حضور خواهد یافت
🔹
هیئت ایرانی نسبت به سال‌های گذشته کوچک‌تر خواهد بود و محدودیت‌هایی برای آنها در نظر گرفته شده.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/690865" target="_blank">📅 15:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690864">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae6039264e.mp4?token=RZsf9PT4IrKF3j4JkTe_nmLtkkST6O0oe6-kYteZ7Apvg80CzyvzxfpqotAqY9X3UCOHchzEG9TUBj4p8kCdYsuFW2-5dfnTiqSQ5gzcITUZ0gDPPljZcIgUCPTR-xZEriRQYvoz73FxSDSrtKY5PxHqZU49uO-QjVVdn2hv4bgaoPPeg02sMJR2gFT3IQ_Y7d_5AxyzsLqcx6eW-Koiv2M9NTjuxW-wUhvgWAVSZnyEA-U9-7ghKahnodIYJU7sh5bjqEZ_8URgcKCVMLOtedpmffp0jV0OGaqX0PzQQcbU50rKqelWPQnxGqSQy8VgvYng5u4MrsMWusx7W5QiUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae6039264e.mp4?token=RZsf9PT4IrKF3j4JkTe_nmLtkkST6O0oe6-kYteZ7Apvg80CzyvzxfpqotAqY9X3UCOHchzEG9TUBj4p8kCdYsuFW2-5dfnTiqSQ5gzcITUZ0gDPPljZcIgUCPTR-xZEriRQYvoz73FxSDSrtKY5PxHqZU49uO-QjVVdn2hv4bgaoPPeg02sMJR2gFT3IQ_Y7d_5AxyzsLqcx6eW-Koiv2M9NTjuxW-wUhvgWAVSZnyEA-U9-7ghKahnodIYJU7sh5bjqEZ_8URgcKCVMLOtedpmffp0jV0OGaqX0PzQQcbU50rKqelWPQnxGqSQy8VgvYng5u4MrsMWusx7W5QiUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شروط جالب عمو فروتن(فیتیله‌ها)برای فرزندانش وقتی می‌خواهند خانه مستقل داشته باشند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/690864" target="_blank">📅 15:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690863">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
عربستان صادرات نفت به اروپا را قطع می‌کند
بلومبرگ:
🔹
آرامکوی عربستان به دست‌کم دو پالایشگاه اروپایی اعلام کرده ماه آینده نفت خام دریافت نخواهند کرد؛ این تصمیم پس از حمله به خط لوله اصلی عربستان به سمت دریای سرخ اتخاذ شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/690863" target="_blank">📅 15:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690859">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UnGzw0Tsgx_qvNEwwadguvkJbq--1vD5Xe3Xas6WxHFuldvoxOo6Ueimhtc1SepLVklP9Tj-nMDALm-git9U7pXFNcCr6kKOffsZNA3ZK0AKmBc1MjrVZI0NigYzYRpRL9zgQTfVl2m2I3VNa-J3T_REpnoXlZ5YfCU-LG8aQgXVYzu1pra7pbGF8QO9ukY3HZiZWhTEM-8enx95TycMGesTq7hC-tMeAFYEawMEmHQEu9xMnPqnFX5Wp5dSeBVyUpIJDp1TBOOroEvIzYWmdQXB_gfdqhPj3ZmdQ4_dELCaaF100l0Bgq6WVGAWF8XA2f1ov9Kwu4oEw5711c8Plg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DOAKLykrlRQW0mxcH5F7uf7KoY-3PS4gqnIOCwavXp51TSXSVk4mF7kGplPLWhvB3yf1ZZN2DoXslrMdCY8RsSnVo4fUywPpMrQ0gecllBU0ShGN3jM-LIUDyKOiRMh5JocP9hz2nSaFpMLG2arWrvGfVd--qZv1Rm4oXghw2Gja2KwithfOLmvCSWNOK4FAKLuodGSyoEl2KNrzxpNsBDwGSWzQXthOg5fU6JzmrjZjFm6vL49ubs27pXl4fNM8UDeicr381sd_sCYgmA2qwjx4Fe9ScXMms0htPk3c1DNm0ZiO4G3X8oSA7JznsUM1cA30bgPT3aZQQffpw7C9zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DRQnH42iyIKMhXIBjlM89wikNpkwF_I6badVzlrj20jf6tXOkJcJeiabKdxsmAazj3Sdwk44WLlr5A6LIbQX8xUSUvJEs9ZwVT4pYbS3-vrVL0_EL014OUB3tNKaL-p8UCmVPxIeEJuEiB2CtQk3rokxAM_cz4B3flEA3neeAGlGQ959J375DrCzyX8ETKWYveugYfrIWMo8cZjHGAvsWwU96YjBkcQVUvmmr6hDAJX4BIFO2mDRqBNFB9E2YpJBhsN8Nzd-lHg6yw4E_yOsv0O0FVVTTnWk_fghTEpYCI-DkgKorOElj_WNK_1-2EMm0sQHJoYsIqTQCHUD9gKGWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rcCw18TdAb9d12EexMbLIHEmwNwKgQrafmy2bWu93JdtdLhntHl2KN2vTGBLPNSlGOIF5Tn-MricqFnxz9vn2fgPqjMBO-3QXgGH4gkaaion4Qn4gC85khKE0czmGer7yGujzJIWoerSWDb5VwJTxs6Lhqmg-rV2CwJsjFkXgWUADJ7jz7QLN3jVG9EPMicOryNRcPlizEmUTC8As733Hg5O_Hov_RKI71FAgrlU4-8gPpq4261yuLT39I_ct3qAaRFH_CcB4hYBoa8Uu4aCnL15K5r2noCjQ8pK4uuNdvbPzqxC4iDKa7eXmmQPCNCqvMbK_wy6Rfkafoacg8_DoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور زنان جامعه مهندسین کشور در رزمایش مقتدرانه جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/690859" target="_blank">📅 15:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690858">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
پز دادن با برندهای غربی؛ خیانتِ نادیدنی به سفره کارگران ایرانی | لوازم خانگی ایرانی چگونه ورق را برگرداند؟
🔹
در دنیای مدرن امروز، هیچ کشوری پایداری و رشد اقتصادی خود را بر پایه واردات بی‌رویه و وابستگی مطلق به برندهای خارجی بنا نکرده است. نگاهی به استراتژی‌های کلان اقتصادی از شرق آسیا تا قلب اروپا و آمریکا نشان می‌دهد که دفاع از «تولید داخل» و تقویت زیرساخت‌های صنعتی، خط قرمز و شریان حیاتی توسعه اقتصادی در تمامی دولتمردی‌های هوشمندانه است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3245912</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/690858" target="_blank">📅 15:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690857">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSuma0DW4kL1WCX0UgawX7ISIP0UuNBHR79mCDktjjRqnvlsuAOagUN6uvfv_6jCxBEDSWS8SDzuhgAHpG42mIlnjAFch82ma0bc2qxVPQ1qDRJoGVb_Pvtoxu0AE4TaAFjN4nDE-1dJxh5quHcalbgY22YEg3W7rp6j-EdcYVaL78BxyHAbRSvhrsHsxh-TrQtZI_vzhQ-LCVrqXYap8BweurXPsVKaDYRlTK5GNzUYxbddvZqSTE8YvGdFRhak7ldF0xMtb7i2hpXUdHCrpW2utzyR2Q8AAEJ4s_8kyvcMWxo2MVUewL_W7immM94Q6BT-sW8PjRmlYbmuNYnIhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازنشستگی رونالدو کنسل شد؟!
🔹
نام کریستیانو رونالدو در فهرست جدید پرتغال برای بازی‌های پیش‌رو قرار گرفت؛ این در حالی است که شایعاتی درباره خداحافظی او از تیم ملی مطرح شده بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/690857" target="_blank">📅 15:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690856">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
انصارالله: همه حق عبور از باب‌المندب را دارند جز عربستان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/690856" target="_blank">📅 15:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690855">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f19a150198.mp4?token=vfcLPZ4n5FYWj_vZkW9AI2oMxCfybSQ-QZ7sysBsp7NPFp7cMXwjM3RPIRr3F2LThYq9yUgwTGHb_Se4CyB9eef6GJAXRLKv8FjCK13mDLLtXJ2CVl1y3lSvB7x-No2uylaRIb89lqQQvXZ9a2aarhE4cHxz7VbQpscCb2zxUSyaASJ5zJEEz-l_8SlZHVU-PQF4Q626k7ZFlXZpH6y9xpCRhnPYMio9wtFCAUN_U8OcYeyamDobW4ZFuHG0z4_T0htevNRzUwVdKt-HOHP3wW5SiNTUHiNVP6-lnJF_3MbtpJ5_qVEko1Khcwj_56XV4ekghSReqhgoKuZqP2GpcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f19a150198.mp4?token=vfcLPZ4n5FYWj_vZkW9AI2oMxCfybSQ-QZ7sysBsp7NPFp7cMXwjM3RPIRr3F2LThYq9yUgwTGHb_Se4CyB9eef6GJAXRLKv8FjCK13mDLLtXJ2CVl1y3lSvB7x-No2uylaRIb89lqQQvXZ9a2aarhE4cHxz7VbQpscCb2zxUSyaASJ5zJEEz-l_8SlZHVU-PQF4Q626k7ZFlXZpH6y9xpCRhnPYMio9wtFCAUN_U8OcYeyamDobW4ZFuHG0z4_T0htevNRzUwVdKt-HOHP3wW5SiNTUHiNVP6-lnJF_3MbtpJ5_qVEko1Khcwj_56XV4ekghSReqhgoKuZqP2GpcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تحلیلگر مشهور عرب: جنگ ایران و کشورهای منطقه، معادلات امنیتی خلیج فارس را تغییر داده است و آسیب‌پذیری کشورهای منطقه را آشکار کرد
دکتر خالد بیدون، تحلیلگر مشهور عرب و استاد حقوق دانشگاه ایالتی آریزونا در
#گفتگو
با خبرفوری:
🔹
ایران مزیت جغرافیایی دارد، اما کشورهای منطقه به پیشرفته‌ترین تسلیحات نظامی دسترسی دارند.
🔹
به گفته بیدون، کشورهای منطقه در حال بازنگری در میزان اتکای خود به اتحاد با آمریکا هستند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/690855" target="_blank">📅 15:30 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690853">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O2vu_2TUEiMyTndsviCnZGyR3CQ77_bIFii1kxVzZcPJBUGjPlncebsZLCdpeakEY2rBRAIK4BLII4DbqwiIIzMxM9ykmdlFm0-RQ7WNUOZOYiXOciBQd6Lex9j4c30V9RyznRk1ndtv4PgmrKdBcVlsMSVRmubOuwPJ5X7bzWglpn9obaTubfOqeNXqltAmEKx1V4sn8HA4wZPKtWYsuJKs7ctRSA44FJsAWJ0YSD34Bg5vS1RRC_3RyCsMNdIrdWdZzHtD99L1ZjUwJOyhSje9g6Bx4u36zULojwg3a87KpvORLhBf7-GWqcIZp_5g51Zi9FHSFP8xyKitXu2Nwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tm4c4qQ1Wd-Ge3EEl-nrEOpYuBm9Nuce0QGtCF1M2s4D2xw_tIRetqcuI1Hwi5ZiNn4AFgrfb0bdgzY4jvNXfHIGVLXw1k7tJCj5NwuEL0qKvkDKqaajyMDFUY7a2BFHHJ5TCAwDipuZAXwZTQsNWvmBueJduJRhZRZb9YCDUvHFzw-1GqEj4Yej6-a-manfv-yPFCNUPrWZ8sb4cPiiadqZt9BK0o7K4QwqQlZnhJiyYP9WKicJt7X3aQ7awWeeY9EFSjBAPLVh6w-wclKGtM3X5bsGkAKp1UOV1Vbnjhm0woI9IBYudplhbr7egDuSf-K62ZIb_FuuFDPcL9rVsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور دانشجویان علوم پزشکی تهران و مدافعان سلامت در رزمایش جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/690853" target="_blank">📅 15:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690852">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krUcdVB3Hhhfg1w7owXad4XIyiDVuvPFoxUQiTOx4HOV3AW4RJFc5WIFmwzmlZpzxZ6dd-vmgxj4GuONw3fcTS8TYP6M3kuNF7nrOhRovDQXamabPkKV5AAfZSHcpBihn1co6CM4FREpLdF28fhaWKS4UnBbGWXVmsvIzhOAIhxZ87GNBUA8nb9XnuoduMAwjmtbH_egnDEzSlOmOsg9bcjrD-chNGiyUoAwPDiBwjA-AYO2d146XEuJI6NkjSVujkkd9HaaXqnpIwxmzoklO7I9coQFaol0Ptqx7vrTJtz9k855qPCGKtBnUKkneLOmr89fLoqG43kcHwkn_5LN3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نوسان قیمت نفت برنت در ساعات اخیر
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/690852" target="_blank">📅 15:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690851">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ade4a47c6.mp4?token=IyMIf0CqoBwVEosymX4SfdolxqmM2OmyfjmGthXKLO3qHr_kSdZkUkWfB9Io4n6hMtVDWPGOlX-qtVkfHfjbJX8lUvcHi1ZVmZIkNpaYpzloMVqT8IP8x_woHp8R48Q042_CV4p_DnkDO6Hxz7qJ1LDYMwEAPz2zBk7N210USK1TYcjwAnz6amG2QVBSeaiWxPTCuqDAGcwaGdrBI4QQroVJSiiSpTinPsGbWggwj5Eab3YUPro7OfgT1nKx0JdeIqWfVfNXf3CH2EyHYoIe7NjLGytVlUAG19_3nAoByc9OBOS0FDoqBMzz63q0szoe0jXI7pRuAOaR9uZO5m9sMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ade4a47c6.mp4?token=IyMIf0CqoBwVEosymX4SfdolxqmM2OmyfjmGthXKLO3qHr_kSdZkUkWfB9Io4n6hMtVDWPGOlX-qtVkfHfjbJX8lUvcHi1ZVmZIkNpaYpzloMVqT8IP8x_woHp8R48Q042_CV4p_DnkDO6Hxz7qJ1LDYMwEAPz2zBk7N210USK1TYcjwAnz6amG2QVBSeaiWxPTCuqDAGcwaGdrBI4QQroVJSiiSpTinPsGbWggwj5Eab3YUPro7OfgT1nKx0JdeIqWfVfNXf3CH2EyHYoIe7NjLGytVlUAG19_3nAoByc9OBOS0FDoqBMzz63q0szoe0jXI7pRuAOaR9uZO5m9sMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خلبان آمریکایی که در ایران نجات داده شد: چتر نجاتم در حمله اولیه آسیب دید و به طور کامل باز نشد
🔹
با سرعت ۱۶۰ کیلومتر در ساعت به زمین برخورد کردم و در این حادثه، ستون فقرات، بازو و شانه‌ام شکست. با وجود این جراحات، از دره‌ای که فرود آمده بودم، یک مسیر کوهستانی…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/690851" target="_blank">📅 15:13 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690850">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a3617254b.mp4?token=lGsGaar0IKf8ZHyvJR_WYIui5mn5wVt5B5rr3_VIpE4KQOAGygkbv74jFfsSUOEObJbnmKOzyreivwpZ_GkJvoH1e4K8r8a62A8tAPmAHQK6sfb2FN9tZafCfmzYhPn2tN_ySIezZdd3qoTsaMDYVoE5WaGvSCAXNMtxiI7Rg2Y64pHGBaz2G_EQ5yohnHFDqLYxgGnV4T3JI4rQqi194rnvwP8TkVv6ahhtP5Kx5o7gobOVxs5CjVx6o-3k_fkgTU5cnswSWbUwmGLQMYH5_4exp3O9zsbSaLrOX9gtZWhuR3fNItF7g9E5sngfNPSKAxw6TjaHnV5eh_vFDiqVBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a3617254b.mp4?token=lGsGaar0IKf8ZHyvJR_WYIui5mn5wVt5B5rr3_VIpE4KQOAGygkbv74jFfsSUOEObJbnmKOzyreivwpZ_GkJvoH1e4K8r8a62A8tAPmAHQK6sfb2FN9tZafCfmzYhPn2tN_ySIezZdd3qoTsaMDYVoE5WaGvSCAXNMtxiI7Rg2Y64pHGBaz2G_EQ5yohnHFDqLYxgGnV4T3JI4rQqi194rnvwP8TkVv6ahhtP5Kx5o7gobOVxs5CjVx6o-3k_fkgTU5cnswSWbUwmGLQMYH5_4exp3O9zsbSaLrOX9gtZWhuR3fNItF7g9E5sngfNPSKAxw6TjaHnV5eh_vFDiqVBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایش پهپادهای سپاه پاسداران انقلاب اسلامی در رزمایش بزرگ جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/690850" target="_blank">📅 15:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690849">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b1dd8dd6f.mp4?token=dKnmLTqcLn-IuVrBb9F44O9j07Je3guvO5Cgc-pOT1UUkR7iX9hJS4HEMkoyLmrHsrIV8EDEo2ZTpICxcqmKu7xXpzRVkP8zLmyQw3u6daiRZSoFgVjqlCOSdFmRuXrhKDstA5I3WT5k_NRMzfB3u5AzgCUegCb_vNSvZ9F2mmViHtrRkN-KnwpVGrTsjG2yKl-4rene7wdoeReLRYKMkA8ujtiFH4-un9cQo4tv3Gt0lEAcn25QxIbW3-QtgwLnmJlFcidsLQp2Kr6RrnjYXljR2sZpLw7hd-LQWNFkNF9Rb4Z7DCoYu1GSXELEIMrWskRnH5A48dGj5rvacYDIpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b1dd8dd6f.mp4?token=dKnmLTqcLn-IuVrBb9F44O9j07Je3guvO5Cgc-pOT1UUkR7iX9hJS4HEMkoyLmrHsrIV8EDEo2ZTpICxcqmKu7xXpzRVkP8zLmyQw3u6daiRZSoFgVjqlCOSdFmRuXrhKDstA5I3WT5k_NRMzfB3u5AzgCUegCb_vNSvZ9F2mmViHtrRkN-KnwpVGrTsjG2yKl-4rene7wdoeReLRYKMkA8ujtiFH4-un9cQo4tv3Gt0lEAcn25QxIbW3-QtgwLnmJlFcidsLQp2Kr6RrnjYXljR2sZpLw7hd-LQWNFkNF9Rb4Z7DCoYu1GSXELEIMrWskRnH5A48dGj5rvacYDIpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هند سرزمین عجایب
؛
پنچری چرخ کامیون با یک اسکیت‌برد جبران شد!
🛹
🚛
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/690849" target="_blank">📅 15:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690848">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmA563LoXfLc6tddlNWDFqt_MSaIBu1L4zTVLr5aL9j-ODiLd0si6eUPW5tDq7S6MiLxol7tYim3LQFb2X-_NL_yb_T_Bo9qGGXO96xGmqD_8LFXhXXUNk5gtFnyvbi0eNaxxD-987p1dOuu18mUds5ShdXGx8J8UYFWjvJ86wgC8gusL6OkrpBI-LsrusbWdRoI9GZRgLiSJ0PZLaBoTL_GafbeD3AwiWzosLZuD487Sq1ShSF63jI0MiaQ1a9ySb9TD2iR8JT5N9B5iad6YEbe_9Zob0QSjgo1PZEmyB9HAIQjMd8waYaUgP_zhNSzCtRmXNbkSuzjWTo7-zEoGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زخم‌کاری چین به آمریکا در میانۀ جنگ با ایران
فایننشال‌تایمز:
🔹
چین دارایی‌هایش در اوراق قرضه آمریکا را به پایین‌ترین سطح از سال ۲۰۰۸ رساند.
🔹
پکن با کاهش ذخایر دلاری خود به‌دنبال کاهش ریسک‌های ژئوپلیتیکی و تحریم‌های احتمالی است؛ اقدامی که می‌تواند فشار اقتصادی بر واشنگتن را افزایش دهد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/690848" target="_blank">📅 14:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690847">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMtKzpF4VbJU4mGf-yVXDOMjLSf8sohrKDzcWLMKxyz2i9upuJMn8b_p0_Cm2TT_CcyqEjvweoOE_fzC173IxYkZw7AQ9AQrYRWVWzJO58V23zigdZja_TemAesmjw7EimRzA4S9dcaHdnc-1z7R4DY8QWNCGZevDiaWjFj8xv2BJTv-Ub3gvKaV5TPH2AvTxRMLz4d2iZ3XXx7uPmT4L1ZRTnYOXDoDmAkU-4f02yoekrpXYz18fV4I57ckpexPYmvMA6vxRufG9tKQVK2oaNBIkxJ9690MA5FzQksK8exBzFAd9jiFXhtvpCpcIJf2FUuztfgGNOD-YTfwe_21-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویری از رهبر انقلاب، حضرت آیت‌الله سیدمجتبی خامنه‌ای در جریان عیادت سال گذشته فرزندان رهبر شهید انقلاب اسلامی از جانبازان پیجری حزب‌الله لبنان
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/690847" target="_blank">📅 14:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690843">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65d34c6fa0.mp4?token=qvQROGwFKUxPMlk-meJdtR5F6JhjslmRB76ZysbEpYypQqfflyV05OEbMEh1wjegj1j1bLaWuImSRPP45Smpud51eO3a0pLNbZTjv9aYS9oiMOpPksetC0tw1lS5k0PRrAYHWt4Cew_-kAgPlpJGXjep8rlFa_JtqO48aBWU4x8cw-nt8NpetKfS6oa4ztvWuWc_h5wndDpmemps05ihDOxvLAPyx1MnhMpmmakxLDBfrC4V7UQggUBAkU2wd8JwsBrNhHSTza1RcKBrjmI_ITvu6jxvuoXjZBIbcLlZ9xEwtmEBkKcpVK7yswy8AFft6yKz_mn7ldA1kIZGNrJbGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65d34c6fa0.mp4?token=qvQROGwFKUxPMlk-meJdtR5F6JhjslmRB76ZysbEpYypQqfflyV05OEbMEh1wjegj1j1bLaWuImSRPP45Smpud51eO3a0pLNbZTjv9aYS9oiMOpPksetC0tw1lS5k0PRrAYHWt4Cew_-kAgPlpJGXjep8rlFa_JtqO48aBWU4x8cw-nt8NpetKfS6oa4ztvWuWc_h5wndDpmemps05ihDOxvLAPyx1MnhMpmmakxLDBfrC4V7UQggUBAkU2wd8JwsBrNhHSTza1RcKBrjmI_ITvu6jxvuoXjZBIbcLlZ9xEwtmEBkKcpVK7yswy8AFft6yKz_mn7ldA1kIZGNrJbGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور ویژه زنان و دختران جانفدای ایران در رزمایش مردمی جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/690843" target="_blank">📅 14:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690842">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/246c8f53f5.mp4?token=nfghIHuluZwsaOcWr5F7nfuS9RMVTJUGec9fz3zVHX0xSVlqLJnW8pOheN4qfZ3P5n9BF3rSbrXduiWg1ALU3aNuQCY0nA8KWMdUVfk44iAoQzsHUka0upbIMVL8rEhEsujzM7mniTGEyVZAYHvXwr4z_T0dsiiSFT7DEm23eziXrT-fXEY1IzaICmjSEgCllMHvkhDgepELN0LeQLajiEFE_xFaXruH8vyAFiK0aq6lIoH3UD-UfeePzfBEskMHabSsYue_UJOdB9Or-k3nxP6RRBkAHwUMYqgE1aqKz82GRLv9dpQK66U5V7N7viCVfRaGvqlLizjF5w9j_gKwvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/246c8f53f5.mp4?token=nfghIHuluZwsaOcWr5F7nfuS9RMVTJUGec9fz3zVHX0xSVlqLJnW8pOheN4qfZ3P5n9BF3rSbrXduiWg1ALU3aNuQCY0nA8KWMdUVfk44iAoQzsHUka0upbIMVL8rEhEsujzM7mniTGEyVZAYHvXwr4z_T0dsiiSFT7DEm23eziXrT-fXEY1IzaICmjSEgCllMHvkhDgepELN0LeQLajiEFE_xFaXruH8vyAFiK0aq6lIoH3UD-UfeePzfBEskMHabSsYue_UJOdB9Or-k3nxP6RRBkAHwUMYqgE1aqKz82GRLv9dpQK66U5V7N7viCVfRaGvqlLizjF5w9j_gKwvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای نماینده کنگره آمریکا: عربستان از ترامپ خواسته جنگ علیه ایران را طولانی‌تر کند!
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/690842" target="_blank">📅 14:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690841">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
انجمن خودروی آمریکا: میانگین قیمت هر گالن گازوئیل در آمریکا به رکورد جدیدی دست یافت و به ۶.۳۹ دلار رسید
🔹
قیمت هر گالن در ایالت کالیفرنیا برای نخستین بار در تاریخ، به ۹ دلار رسید.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/690841" target="_blank">📅 14:30 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690840">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c6781ae07.mp4?token=lRAVP8Mj8o8xwWfBs_qXd8YmYLdqsWEP_Ja_la3tlVQCkolHn5wz72cfUOT7Jdu-MJY-eInzSyUiraiBlQuUD7b_wJ7n7t100US4W9V08b1cSib5TCCahSUvCfjoiNmBme6LhmYbwhU1TO5Aa8FbrV0VhxS1krhRFgRmLzXMBgSp9zhMHi9NyIDpGoHUkWkwDDHLoUeXFnJMQQPnJ0KqhaSlBLtlc2_nwfueqX0UbDzwtHRKoMyZTMncnd3FmQbTiJb5w2P5wo8d-rjW3DNkymVkO78W0yAKcuBQQwdjLJ_dkt2nKelH2QYXjwI6YP0ZdI-TwBxYaZEn7jZgglU4uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c6781ae07.mp4?token=lRAVP8Mj8o8xwWfBs_qXd8YmYLdqsWEP_Ja_la3tlVQCkolHn5wz72cfUOT7Jdu-MJY-eInzSyUiraiBlQuUD7b_wJ7n7t100US4W9V08b1cSib5TCCahSUvCfjoiNmBme6LhmYbwhU1TO5Aa8FbrV0VhxS1krhRFgRmLzXMBgSp9zhMHi9NyIDpGoHUkWkwDDHLoUeXFnJMQQPnJ0KqhaSlBLtlc2_nwfueqX0UbDzwtHRKoMyZTMncnd3FmQbTiJb5w2P5wo8d-rjW3DNkymVkO78W0yAKcuBQQwdjLJ_dkt2nKelH2QYXjwI6YP0ZdI-TwBxYaZEn7jZgglU4uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیمار فلج توانست با تراشه مغزی نورالینک پس از مدت‌ها صحبت کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/690840" target="_blank">📅 14:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690839">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3335bbf6c.mp4?token=EcvVsMu_o3nDm-j7DyduZoIgRl9GY4TuiIGTH2IkUwf2J2G5lWOe7mdqlA8Uz2kaML703KUhgFgQ5bgbVDXnDAKAd0hc9nBHGLuGMKKMGyZVO-gUA5Mh8IkgZ735_zdU_AtrfO1lkUzGeWZ5iTt-UZpxyefOnB1PaS808cdx8IKTKm70BuvX9zwWS_dOVeEbtBIkM3fe52nZWZzWxG9mj72kh7GfPfEvL-_eAKzSroHe11mcVjgI5D5qnMmkoghZKBEa5mxupRvC3W0CfipiP4IgEWIr7IuBGs3OK5pkn_RXM3iY35HM9d3CEBBP3sDBcaAsorqx7l5wxrzqd0f1Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3335bbf6c.mp4?token=EcvVsMu_o3nDm-j7DyduZoIgRl9GY4TuiIGTH2IkUwf2J2G5lWOe7mdqlA8Uz2kaML703KUhgFgQ5bgbVDXnDAKAd0hc9nBHGLuGMKKMGyZVO-gUA5Mh8IkgZ735_zdU_AtrfO1lkUzGeWZ5iTt-UZpxyefOnB1PaS808cdx8IKTKm70BuvX9zwWS_dOVeEbtBIkM3fe52nZWZzWxG9mj72kh7GfPfEvL-_eAKzSroHe11mcVjgI5D5qnMmkoghZKBEa5mxupRvC3W0CfipiP4IgEWIr7IuBGs3OK5pkn_RXM3iY35HM9d3CEBBP3sDBcaAsorqx7l5wxrzqd0f1Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور اقوام و اقشار مختلف مردم در رژه با شکوه جانفدای ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/690839" target="_blank">📅 14:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690838">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
الجزیره: روسیه و چین پیش‌نویس قطعنامه آمریکا در شورای امنیت سازمان ملل متحد برای تمدید ماموریت کمیته تحریم‌های ایران را وتو کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/690838" target="_blank">📅 14:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690837">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gu2pnl5G47jxJOtCz0rDAbLMGLPcnqObu8svdh0_cmK2SzSXd1_hUsj3IGBYeQdn7pvqoslCaTFOm9Zcg6NCMhMu0n1V_OPCkKCFu5XdClfFbSrrFPWa6xtM9IXF4hYKA4ws_JzPTfgfWD8YZmQUe2VEsmkrme7i_dO0SIa1eyM8TkJwEY2ybCC5KOLg1IkUfVGBJzKHWYgzY2ma6rQO5y3ZI75rM1k8PZsdy74rPtTygBulsW58YxICGem4SzO5AIiRUfq9JZXHLObQzW8oAh6RV37qavnT2Sdu_xuAfpYwZNhBu8YbkO9UAhK5QNRpDoXjnW_ODBLepcnIe7hKzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: ریسک تنگه هرمز بر نرخ تورم آمریکا اثرگذار است   قالیباف با اشاره به تصمیم فدرال رزرو:
🔹
افزایش یا کاهش نرخ بهره به‌تنهایی نمی‌تواند تورم آمریکا را مهار کند؛ زیرا انتظارات تورمی تحت تأثیر بسته بودن گلوگاه‌های انرژی، به‌ویژه تنگه هرمز و باب‌المندب،…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/690837" target="_blank">📅 13:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690836">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
وزیر دفاع پاکستان یک روز پس از ادعای عربستان درباره حمله پهپادی به مکه: زمان اجرای پیمان دفاعی اسلام‌آباد با عربستان سعودی و ترکیه فرا رسیده است/ ما وظیفه خود را انجام خواهیم داد/ پاکستان کاملاً آماده است تا به تعهدات خود عمل کند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/690836" target="_blank">📅 13:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690832">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VyFZiOgAXBIXZughgAt3_LjMDhtLK099LL1WMPOx9nUXb-o2MyV4uUQN2gzvg9nkL5FW9fdzm509VPiFzKmVMcQHZaWzGiuZpc0fBBk8VZVGRCnCgNnbjYrOYEN9oVALGhwKj_ippXqAQSN3tUq8sYCFPH96NvOqDq7YAFDsF76YsuCQM8wNSTJy1yq6W7JKDLYH9A47ZgbJ_iNNJ37nByQB9nAI9AOaU-EKzncIlEW-o78fcG0wDMDHe4hFRP7v1AZaFjTgdQ-owj74YW_5WDjzFHfTZDRXw5RUu0Jsmsm-6khXxOUE6Q2PSD9GZvncJm3zvfYXUkhhnHZg3bEzAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e6VAmPJgeE__DqjeHAZ0jTEOnCFrf4EVWWCYB2FCV4Kgeb-1NnxTT7t5aTDq23zcG2DI4hFynhCHVUOP7fmS89xRsMcv-hCVG4y8VdiM9Qfde1UGOGj1uia7AI0iXApcITBw8ERN5JCWO7LhrJp-a2QF1uAut5xnHg3c_ccT96il1Cp4QUTlgJM3W9Qr_AcRfGd1wQIwwMPALC8Qq5FUAkd4T9bGkaKAmCjKd1EH782u762HE8BeW4iOdS6ytebVTEIKc8619O2hY1ltQIYxXLUfRWTEbV-wRF8DEirUmNMDZFsJ9gSdZhwN9XTbeeM6pqluaQYP0Wbb027SHKsW_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tiHrjlA2DjxSCb3fUSyWCI-YV3i66mtVmOlL_vXcGqATu04nHTH_q36pCjB4CKaYdkrNiUc5XqfUdhLRQGtI27S_v46HHKLoQmAvPD7tYWgHY14fgtsvpwf11oyuL3JrY7xtRjvlOfXqc2biSrlkx_ynslxPWaTDosl2dnVFqdA8DvPo0XxlxcYV_nsOFtHWLfuySOy4mfhhWugq1sBaBPEcIIUPnBKvahrw1ML100O3MSJ9N4pSKgzYflK6K9gBb0mkHM0NM-KQ_2XLHQ0U0Lsn7YHHNXZn2OLZFDG4hqReM30hBkioWiGyxxSpiXnuZJLF41v5OJBva-1XleY9Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B1cuNKUoCDw3yyi5qXT_ArM1Kx0sZonvv8j41KrTer0j07q140vbhrRXXwRt4pVnBNvxkUiRXC8vwCzeEZ1iXHzmzoRA777Z7iwVtkyDaH5EHMZZhIfxjhbRNs0udDHZ18q17ddYCXUavaci7YSvgZ3cz8gdwQkwjVggeXs_UT-PhSmIiaFpWVoH6OMLeOL8NWDWq8ZXMkTQoiQT5xL8yibvx_xIvAsPz9eX9OPTtyaPZAEW5y8uCxvgPDQrW1dlkcpV3ocPZAbZ5yNk_V2rZ6jN9WqVYMul8ahFc56G9kMHd2egkuNpDenSmyE8T5-ZK-9q2fTDEDu_9naAPNcvvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور جامعه بسیج ورزشکاران و جوانان ورزشکار در رزمایش مردمی جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/690832" target="_blank">📅 13:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690831">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f6cb7a77d.mp4?token=Otl04xR4r3x5sMgBolj99kGkijuXYFqVnEblO5AFUYNryiQOsSc-RVyFxqEYTYMKmELl8ts6YRKt-6Ko48pqbwQUveorZbRdt1DX3OtjmawVRpOH6PPhjBgJzs1mIWCVR8-LmyGGPz2keghV6kq3VIiTrTAMuZ0Y8CZCDBafUsdQeLgz_NfS0gwl5pOVjRTi68Av69nedVL0JCba-tcICWQZzFiF1riKcv4TG6XHdvzFY6xXg_cDB-Ri0TX0PtK5ItyZN8DFHFJDO9WCt8-XbEmpcneRyZEp8cVDxQVKD66kn09qPknvxrP9LoTTItQMPbC1obwGFg6XNewOvb9mUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f6cb7a77d.mp4?token=Otl04xR4r3x5sMgBolj99kGkijuXYFqVnEblO5AFUYNryiQOsSc-RVyFxqEYTYMKmELl8ts6YRKt-6Ko48pqbwQUveorZbRdt1DX3OtjmawVRpOH6PPhjBgJzs1mIWCVR8-LmyGGPz2keghV6kq3VIiTrTAMuZ0Y8CZCDBafUsdQeLgz_NfS0gwl5pOVjRTi68Av69nedVL0JCba-tcICWQZzFiF1riKcv4TG6XHdvzFY6xXg_cDB-Ri0TX0PtK5ItyZN8DFHFJDO9WCt8-XbEmpcneRyZEp8cVDxQVKD66kn09qPknvxrP9LoTTItQMPbC1obwGFg6XNewOvb9mUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری عجیب از ایستادن بتمن بر فراز نماد شهر سیدنی استرالیا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/690831" target="_blank">📅 13:39 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
