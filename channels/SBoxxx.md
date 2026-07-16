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
<img src="https://cdn4.telesco.pe/file/kpLs67CG3FXweFN2uRQxenlUNcLNc0nUlccZ3dXpegDflM7GyrzvVjbYE5p-QuJOcoXZqa_LAbUZi_5AVtXnXJUh4tStai0MWPzG5iu8_2VV2sc-dnwfjJs8JX_MgksISnSSEXqmIjSPotd9maY0kDiF321VuKKZN7DwyEKPtAAyGzANuocheYnxMdLwoivqDe52xMYboM5at8UJ2h9Ej3DaJ5IC5Oc3B3GH9c_dc2kHN-V68p3LYK4GUGphGQTRNdstz0AxBswrXreexNhVlsm5UEmvK29OGm4uHj5CPoTl8wlTRn0lrA2ywoSWKpgWxBUyqbAC4LpxV1V7YmHR2A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.3K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 21:14:03</div>
<hr>

<div class="tg-post" id="msg-18834">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwsglzbQvElYB5rVGPR_1ksnscagMjYEykrQ4knzX70RBO9K6RU_acPNJWJ_fb8YOHuMciPzAPEgoGadZ_tUYT2A4shdI-de7P-Pp7UvVrRq6jLCC9dpSI7WQ7_pH0SpyUL57ssMznjqBluhrXqg4Ps5S1nhfVnO0J7J5hEwfD2xqZmQU1FoBomURL1PR-gadTy3sW__jL6IAYhP8kwL6ORxHDsvWiCPLZgxTAtu5G-bYtN1FvPAovho4C-z6wgjUaYXdpaltO9orSX6zSFuImpP0yQ7MphrygeoIO05NKzTABNUhx1nJo9On7zGrm76GH4XtKFUrJ3lccyeB46P-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ را در زمین ونس ترنس انداخت تا خودش را مبرا نشان دهد.  ونس 1405 = مرفاوی 1385</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/SBoxxx/18834" target="_blank">📅 20:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18833">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9y8JLr5TQ-7oSQ9DYVYjXBAyiMAOXn3WN6WIenEHhTmZY6XjHnjSdZEFiztSOc7VXKmN98dvZuQMFlp_AazAbZ1PItzPDkU-h7s3BJzKFPpjvUOaAbNBeV1uDb7zepDuWkSuuoey9YSWMhUC2j3sAk3xat1V1yUb2l9HFDmv1Uh0RmqTBqbYbjeDmQPcHsHP2Wamye84S6Hbwjugeg5VV-gu6PNzPn-ES0j3_hksZnbFDVSoaQIfj804i4VFHSFglGw_cy4Y-ubP_6o_8U78uiO-NJlIquADFPU1arqmef42E86DwgCdoAV9kM2jJM3Q0-nWG0Edem84UX20LvJ-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سل طلا بسته شود.</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SBoxxx/18833" target="_blank">📅 18:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18832">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">موشک‌های آمریکایی به اهدافی در جزیره قشم در جنوب ایران اصابت کرده‌اند.
— خبرگزاری مهر</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SBoxxx/18832" target="_blank">📅 18:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18831">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رهبر یمن سخرانی مهمی را آغاز کرده است</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/18831" target="_blank">📅 18:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18830">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">این دیگر حماقت محض است. شما شاید بتوانید با موشک و پهپاد اهدافی را در یک کشور مرفه ثروتمند مانند قطر یا کویت بزنید و آنها را وادار به دادن امتیازاتی بکنید؛ اما زدن اهداف مربوط به کشوری که مانند صوریه جولانی 15 سال است اساساً در گه فرورفته و مردمش نمی دانند…</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SBoxxx/18830" target="_blank">📅 17:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18829">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مشاور محسن رضایی:   تصمیم مهمی در تهران اتخاذ شده است؛ اگر حکومت جولانی بنا به درخواست ترامپ و فشار آمریکا دست به اقدام علیه حزب‌الله بزند، با حملات موشکی و پهپادی مستقیم ایران مواجه خواهد شد. این هشدار به جولانی داده شده است.  #ژئوپولیتیک</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SBoxxx/18829" target="_blank">📅 17:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18828">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0WK9GzgTyd5FgXZF65PHaeaEfkCxKb3X5kGry44NmzLqy3t6LHS78UJqvvW624gdAkEnuoCPD9ErBDcKysuduJb5Wwuuebs2IAph84UQNj8yMR3Ruqs85mD6zE0KY5rMg4TRpiBKapJR2JLp4rg6Iehy88UjODjENcwCLIxnpbT4YP7nwJMwnQ0sSYAOB3nhvwf858lbFS8tzJgTrrKGOCu0xWcVmzXM8uOys3KCM0ROJq4zv_8CGWFo1zpMq6kHVVZ8RONcYlJGVdNXEfabLjLtg4uT7AGbTwvCwLbwqX3qAmU84vxOIMIhLS7pqJk0nFccxYZ2G-DMpoHyn72og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر شما ترامپ با این سه سگ (اردوغان، فیدان، کالین) چه صحبتی می تواند داشته باشد آن هم وقتی که جولانی هم دارد به اینها می پیوندد؟!</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SBoxxx/18828" target="_blank">📅 17:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18827">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfdMk12v44NFmrhLmzbTiKI440J6YZU8RYigejNxwAbYLWMlipfvd46YMGTRXjSh19yOEAExH1OXiAzPxrLi_1UJ2bTlIZnqrqVtY3032BUBqnwOMpWuR9rbrfdOo5Xqd-FgnfArrDWoJbgD8TXjfxEuLOqOtWgprY6Ws9JcMtAvvlDk6oQhuXXdpC-Qbv802VW-u_qN-pr2e6IZ6A3s1hesni2WS75P3JJFd0B0MP9wzc02uT8WqSw_zRlQrTrB4opKbms5mP_mPzG1ZkTb4EXkbSGUtcn3sacS7DlgnzzxC6rjGg85lLYX2j4I2uQxs4mRdChYrJ8EYcBjsI94Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار: آیا رئیس‌جمهور الشرع (جولانی) برای شما تعهداتی در مورد کمک به حزب‌الله در لبنان داد؟  ترامپ: بله، او این کار را کرد.</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SBoxxx/18827" target="_blank">📅 17:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18826">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رهبر
یمن سخرانی مهمی را آغاز کرده است</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SBoxxx/18826" target="_blank">📅 17:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18825">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SBoxxx/18825" target="_blank">📅 17:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18824">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح بالایی است و پیش بینی می شود شاهد جو ریسک گریزی باشیم.</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SBoxxx/18824" target="_blank">📅 16:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18823">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نایا به نقل از یک منبع مطلع:
امارات در حمله شب گذشته به بندرعباس مشارکت داشته و در این عملیات، به‌طور مشخص از پهپادهای اماراتی علیه این شهر ایران استفاده شده است.</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SBoxxx/18823" target="_blank">📅 16:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18822">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQwBzOWDQ8G7-uKrAwfZV832ulUqmqRjGWvM95t_Rq0079300ij7g9GhGyC1d71ubyAq6USwuydXFI6iA4N7Y0AVTkEAK33hBPl8GY3ksz4GZeqYlMUk3SegR2L73eFEHBPVKyMMM0pnv94c7tXteU0PFeH1Vaq69m_w-ynoLMhTwUf2PCuxSZqbGiUkpfotVDQBZkVPllr0hxb2gigheBo-llXi9XtcbivTAgDtVPIHb6gN6KMopEqWb_b20lQtiIKAbt979zodtXMN50SDq30cDWlgjT6sqH97KiMA3QmSJzZrjDnoo8cKyIYYrNphOtWu6u94nZ5bVpOCjqgdhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با این قیمت های گوشت، همه مان باید بزودی به هیات مذاکره کننده پیوسته و گوشت الاغ مرده بخوریم.
آبش را هم بدهیم میساکی بخورد.</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/18822" target="_blank">📅 15:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18821">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سخنگوی قرارگاه مرکزی خاتم‌الانبیا:   زیرساخت بزنید، هرچه زیرساخت در منطقه باقی‌مانده را می‌زنیم</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/18821" target="_blank">📅 15:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18820">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">یک تانکر نفتی در بندر بصره در عراق مورد اصابت یک پهپاد قرار گرفت و تمامی عملیات بارگیری نفت در این بندر به حالت تعلیق درآمد.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18820" target="_blank">📅 13:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18819">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5Q8PcseMU4I4kvdimKdjfo1rBLB7gSAC6lBb3CTqpk6OhXccwOUtNb_5dr5XutZ8eyBrTeYvc3SeZo4yafD03-UFvh_jjQ-uwDF_oU1MRXzcDPviACLJ6vN9EBj9-GqPL8r0PaiyEvfx6j43eVuynPmVuovXWXdK2wytpZrkOIAbAkAovdwRoGzkxLVofuLuE-xZ744sKK3EHyaLnqk7Iy8vZyFIaFpawP3_dUHwk603JoDlsKyoO9Gcgai5ZVEr_Np79EX7VpMVeZZLLDxc03Z3PI1AYNCwxG67f56NeQouWiWRC5gOwWeAEy6eZUiSsy4iMVim3LOCvZ7BvkJFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح بالایی است و پیش بینی می شود شاهد جو ریسک گریزی باشیم.</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/18819" target="_blank">📅 13:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18818">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اداره کل کشتیرانی هند شامگاه چهارشنبه ۲۴ تیر با صدور دستوری اعلام کرد تا اطلاع ثانوی هیچ دریانورد هندی نباید به کشتی‌هایی اعزام شود که مسیر سفر آن‌ها شامل عبور از تنگه هرمز است.    در این دستور آمده است: «با توجه به تشدید وضعیت امنیتی در منطقه خلیج فارس، اداره…</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/18818" target="_blank">📅 13:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18817">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یعنی وسط کویر لوت هم یک قایق کاغذی کاردستی پنج سانت و ده سانت چپه بشود چند هندی گم می شوند!</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/18817" target="_blank">📅 13:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18816">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">این امر روی بدهد، سپاه گزینه آخرالزمانی نابود کردن تاسیسات نفتی منطقه را فعال خواهدکرد.  البته همزمان ترامپ گفته که ایران خواهان توافق است و این ور هم سیگنالهای سازش می فرستند. روزهای آینده مشخص خواهدشد.</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/18816" target="_blank">📅 11:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18815">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سنتکام:
موج جدید حملات ایالات متحده علیه ایران به پایان رسید
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (CENTCOM) در ساعت ۹ بعد از ظهر به وقت شرقی در ۱۵ ژوئیه، موجی از حملات علیه ایران را به پایان رساند.
نیروهای ایالات متحده به مراکز فرماندهی ایران، سایت‌های پدافند هوایی، توان موشکی و پهپادی و تأسیسات نظارتی ساحلی حمله کردند تا توانایی ایران در تهدید دریانوردان بی‌گناه خدمه‌رانی در کشتی‌های تجاری در حال عبور از تنگه هرمز را بیشتر تضعیف کنند. سنتکام از مهمات دقیق برای هدف قرار دادن اهداف در چندین مکان از جمله بندرعباس استفاده کرد.
اوایل امروز، نیروهای آمریکایی در یک موج ۹۰ دقیقه‌ای به سایت‌های دفاع ساحلی و موشک‌های کروز در جزیره بزرگ تنب حمله کردند.
ارتش ایالات متحده در جهت فرمانده کل قوا، ایران را مسئول می‌داند.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18815" target="_blank">📅 10:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18814">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">آمریکا برای احیای خط لوله نفت عراق-سوریه جهت دور زدن تنگه هرمز فشار می‌آورد  واشنگتن در حال هماهنگی مذاکراتی برای احیای خط لوله نفت متروک عراق-سوریه است تا مسیر صادراتی امنی به سمت مدیترانه ایجاد کند که نفوذ استراتژیک تهران را تضعیف نماید.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/18814" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18813">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">پیشتر گفته بودم که یکی از انگیزه های اسراییل از تعقیب پروژه تغییر رژیم در ایران ایجاد یک کریدور داوود بزرگ است که او را از امتداد آویزان بودن به آمریکا برای تامین امنیت ملی اش بی نیاز کند.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18813" target="_blank">📅 10:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18812">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">چرا درگیری بعدی ایران و آمریکا احتمالاً جهش تاریخی نفت را تکرار نمی‌کند؟   درگیری نظامی میان ایران و آمریکا همواره یکی از بزرگ‌ترین ریسک‌های ژئوپلیتیکی بازار انرژی بوده است. هرگونه تهدید علیه تنگه هرمز، مسیر عبور بخش قابل توجهی از صادرات نفت خلیج فارس، در…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18812" target="_blank">📅 10:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18811">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">منوچهر متکی:  باید برویم پایگاه های آمریکایی ها در منطقه را تصرف کنیم و بعدش صد نفر از سربازان شان را اسیر کنیم بیاوریم ایران!</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/18811" target="_blank">📅 03:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18810">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ: ایران یک شهروند  امریکایی را آزاد کرد، متشکرم!!
«ایران به یک شهروند آمریکایی که در دسامبر ۲۰۲۴ در دوران «ریاست‌جمهوری» جو بایدن خواب‌آلود به‌طور ناعادلانه بازداشت شده بود، اجازه داد تا آن کشور را ترک کند. او اکنون در امنیت خارج از ایران و در شرایط خوبی است. ایالات متحده آمریکا از این اقدامِ مبتنی بر حسن نیت ایران قدردانی می‌کند!»</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18810" target="_blank">📅 02:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18809">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">کما اینکه خراب کردن چیزی خیلی ساده تر از ساختن آن است.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/18809" target="_blank">📅 02:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18808">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ونس :   با توجه به سهولت هدف قرار دادن کشتی ها با پهپادهای ارزان قیمت، امنیت ناوبری به تنهایی با استفاده از ابزار نظامی بسیار دشوار است.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/18808" target="_blank">📅 02:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18807">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ونس :
با توجه به سهولت هدف قرار دادن کشتی ها با پهپادهای ارزان قیمت، امنیت ناوبری به تنهایی با استفاده از ابزار نظامی بسیار دشوار است.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18807" target="_blank">📅 02:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18806">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مجلس نمایندگان ایالات متحده با قاطعیت پیشنهادی مبنی بر قطع ۳.۳ میلیارد دلار کمک نظامی به اسرائیل را رد کرد (۳۱۴ به ۱۰۴).</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18806" target="_blank">📅 02:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18805">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">7 جوان ارتشی پرپر شده در حمله دیشب آمریکا به سیستان و بلوچستان!</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/18805" target="_blank">📅 01:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18804">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIZB2B6Sn9d1s7-wj6HWAmLf1ubraiuuZpOX8KBPdOrhUgEEJfUc4EEi97-16YSiHYuNgVIkpgn2oYPw2MNfVlYyZrzZwsYfggA8sylEcnZ_6gQh62CmMcYlU2mdP0QXTOsoXZ4UV4Z65XPa5i05IiC1ZF_KFss4kPMKagwrZXQCbU85cGCu0BtuhvEHPIUCAwEW9A1j7d159qyu11rM_ATkfEPQwNvQG8t8RI1fnlojl-HO0Y8gbJPdtSRgVz_2dj47izav9K9KpVABTK8Oih7Eha7Fqa0SYtqWL74yaIMZZ86ur5QjYo7McRy310u_mPSrVn_n-Y5YmTTofpvmNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💙
💙
💙</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/18804" target="_blank">📅 00:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18803">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">جی دی ونس:  اگر من یک انسان باشم و با یک روح شرور روبرو شوم، شاید فکر کنم یک دیو است.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/18803" target="_blank">📅 00:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18802">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">جی دی ونس:
اگر من یک انسان باشم و با یک روح شرور روبرو شوم، شاید فکر کنم یک دیو است.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/18802" target="_blank">📅 00:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18801">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ:
ایران به زودی شکست میخورد</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18801" target="_blank">📅 23:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18800">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آمریکا به عنوان «پاداش» حمایت از جنگ علیه ایران، به امارات متحده عربی دسترسی ممتاز به فناوری پیشرفته هوش مصنوعی اعطا کرد.
ابوظبی اکنون می‌تواند فناوری پیشرفته‌ای را خریداری کند که در دسترس هیچ کشور غرب آسیا، از جمله اسرائیل یا عربستان سعودی، نیست.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/18800" target="_blank">📅 23:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18799">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">محمد مرندی:
در همین حال، اردوغان همچنان نفت ارزان قیمت باکو را به شریک تجاری خود، نتانیاهو، منتقل می‌کند.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/18799" target="_blank">📅 23:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18798">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دیدگاه ونس درباره اسرائیل:
من فراتر از کوچک‌ترین شک می‌دانم که افرادی در دولت اسرائیل وجود داشته‌اند که سعی در تغییر آن سیاست داشته‌اند زیرا می‌خواهند عملیات نظامی را ادامه دهند.
برخی افراد در سیستم آن‌ها، فراتر از کوچک‌ترین شک، وجود دارند که دستکاری کرده و سعی در تغییر افکار عمومی آمریکایی دارند تا جنگ را برای همیشه ادامه دهند.
دوباره، نه به سمت هیچ هدفی، بلکه فقط برای همیشه.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18798" target="_blank">📅 23:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18797">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">حملات سنگین به اهواز !</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18797" target="_blank">📅 22:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18796">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سنتکام:
ساعت ۳ بعدازظهر به وقت شرقی، نیروهای ایالات متحده امروز موج دوم حملات خود را علیه ایران آغاز کردند.
این حملات به توانایی‌های نظامی ایران که برای تهدید کشتی‌هایی که آزادانه از تنگه هرمز عبور می‌کنند، استفاده می‌شوند، هدف قرار گرفته‌اند. تنگه هرمز یک آبراه بین‌المللی حیاتی برای تجارت جهانی است.
ارتش ایالات متحده در حال محاسبه مسئولیت ایران است، طبق دستور رئیس ستاد فرماندهی.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18796" target="_blank">📅 22:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18795">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">حمله ایران به اربیل</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18795" target="_blank">📅 22:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18794">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">قبلاً هم گفته ام که پیش‌زمینه سخنان دونالد ترامپ درباره «تهدید کمونیسم» را باید بیش از آنکه در واقعیت سیاسی امروز آمریکا جست‌وجو کرد، در ادبیات سیاسی محافظه‌کاران این کشور و تلاش او برای پیوند زدن خود با میراث رونالد ریگان دید. از منظر علوم سیاسی، کمونیسم…</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18794" target="_blank">📅 22:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18793">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گوستاوو پترو، رئیس‌جمهور کلمبیا، نتایج انتخابات این کشور را به رسمیت نمی‌شناسد و اسرائیل را به دستکاری در نرم‌افزار انتخاباتی کلمبیا متهم کرد</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18793" target="_blank">📅 22:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18792">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">قالیباف: باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم  باید از ابزار دیپلماسی و مذاکره هم استفاده کنیم تا منافع ملی را محقق و تثبیت کنیم  محمدباقر قالیباف در بیاینه تبینی خطاب به مردم عزیز ایران:   این روزها که دوباره آتش…</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/18792" target="_blank">📅 21:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18791">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">قالیباف:
باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم
باید از ابزار دیپلماسی و مذاکره هم استفاده کنیم تا منافع ملی را محقق و تثبیت کنیم
محمدباقر قالیباف در بیاینه تبینی خطاب
به مردم عزیز ایران:
این روزها که دوباره آتش جنگ شعله ورتر شده سوالاتی در بین مردم و گروه‌های مختلف پرسیده می‌شود و هرکس به فراخور نگاه خود به آن پاسخ می‌دهد. آیا ما به دنبال جنگ هستیم؟ آیا جنگ و سایه جنگ پایان می‌یابد؟ آیا با مذاکره می‌توانیم به اهداف خود برسیم؟ وقتی با آمریکای بدعهد طرفیم اساسا مذاکره چه فایده‌ای دارد؟ و در نهایت موضوع مهم این است که چگونه حق خود را بگیریم و پیروز این جنگ باشیم؟
اگر با نگاه منافع ملی، امنیت ملی و به‌دور از نگاه جناحی به این موضوع بنگریم می‌توانیم به پاسخ‌های صریح، روشن و دقیق دست پیدا کنیم. اول باید بدانیم ما در یک جنگ جوهری و وجودی با آمریکا قرار گرفته‌ایم که هدف آن علاوه بر ساقط کردن نظام مقدس جمهوری اسلامی ایران به‌عنوان نهاد اصلی جبهه حق و چندپاره کردن کشور عزیزمان ایران است. این راهبرد دشمن تغییر نکرده است.
دوم، همان‌طور که قبلا نیز بارها گفته‌ام، آمریکا در هر زمان که بتواند به‌دنبال ضربه زدن به ایران و پیش‌برد منافع خود است و این محدود به جنگ،  مذاکره یا فقط این رئیس جمهور فعلی آمریکا نیست. پس نگاه ما هم در جنگ یا مذاکره باید براساس منافع و امنیت ملی، واقع‌بینانه و بلندمدت باشد.
لذا راهی جز تکیه بر توان خود و قوی شدن نداریم.سوم، مقاومت یکپارچه ملت ایران و نیروهای مسلح ما، این نقشه شوم دشمن در جنگ  40روزه را باطل و آن‌ها را مجبور به درخواست آتش‌بس و انجام مذاکره کرد ولی حتماً راهبرد غلط آن‌ها را عوض نکرده است. آمریکا همیشه خوی استکباری دارد و هیچ‌گاه ایران قوی را نمی‌پذیرد.
با این فرض‌ها باید پاسخ سوالات بالا را داد.ما هیچ‌گاه از جنگ استقبال نکرده و نمی‌کنیم اما باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم. در کنار این باید از ابزار دیپلماسی و مذاکره هم استفاده کنیم تا منافع ملی را محقق و تثبیت کنیم.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18791" target="_blank">📅 20:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18790">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyIRqPLVCtiiUQCHmkHPrjpVSznPFxJ1flvSJNvNvlIVFdSqAzDMCK1G2agFiIY0dgqGTkK18bvPBrKh9Evo-QkFqMqGPEc2Hbh4NB4F_TOunzhAhjTdHxN3woHPROGpPRBn7gHP3FTXWcz60VEvhQnvHRdAsswX0mWGpwVcUGquqNTbI7t8qYCK1grzOAO7NrjQLKz8Wm-3UYrxCACGjBZdRZXm5wmqqx05UZKRNH22cOzqX5Vvmk5mA0f4JXZpIe-Z5n-SIC8gKlA_TGT4Z_tiVqlGFG_2mSrCfPJCafrlr2QSWdCeIKLdLkSzko8iXFDMFn7bj5Z8YBwTw927OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در آخرین افشای مالی سالانه خود گزارش داد که در سال ۲۰۲۵ حداقل ۱.۴ میلیارد دلار از کسب‌وکارهای مربوط به ارزهای دیجیتال و میم‌کوین‌ها درآمد داشته است. ارزهای دیجیتال به‌وضوح بزرگ‌ترین منبع درآمد او بوده‌اند.   این گزارش همچنین نشان داد که او ۲۶…</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18790" target="_blank">📅 20:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18789">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">به گزارش یک مقام ایرانی ناشناس، ایران یک پیام خصوصی به جِی. دی. ونس، معاون رئیس‌جمهور، ارسال کرد و در آن، جارد کوشنر و استیو ویتکوف را به سوءاستفاده از اطلاعات محرمانه حاصل از مذاکرات بین آمریکا و ایران برای کسب منافع مالی و انتشار اطلاعات متهم کرد.
دولت ترامپ به صراحت این ادعا را رد کرد و این اتهامات را نادرست خواند.
منبع: Drop Site News</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18789" target="_blank">📅 20:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18788">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIo3MEiHPsS3HU8lxtzhvGZ68T9BQ6hhg-T7y4jo0dMVuvAClgQ-TtXRBIGTFmRhypdcTTL7Oz_AIbsiYYIBQgKtpej46jaJOnBLyDPIsLItWY9AkSsolX-uQju7yx5kHmsoLl9kq7WTygaSA2uMYYdLPnsaH3575mYPIeew2_CPQ2EYVGzh1VK1PjcJQDxFBn3Ao23Pu9e-v5s4UAiYm6yiNyIhnnItfclurRz1ii_oSr_gYGVwUqj2elUntmJYSnGjPbVP9oUWxpRkUI2n0sb6q498e4wgvvceQRg3Ba3gSyJe1TDnfe1GAIkal4G6W7QcHtQzR-45Qm6wSPu76Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس:   چندین انفجار در بمپور و چابهار شنیده شد، علت نامشخص است</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18788" target="_blank">📅 20:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18787">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7NB_PlbvCOB4aAeWnqd1pvcmRULt8UYjSA2PMFAQpUAbZNC0ygdmqJWkzlfIPp0t1--07MbO4QVfUA0sIiVvR7QDBRh_srXzfjaZ98slMgz_Hj4oFdb_h-5HtxRiBoPWM8O4fxwl6zBqUVZEJxgcPkUpEJjMAJf2QsrJ6mz9iWPpAMDl1MU2wEOfvfhT_HCZ_ND5ejpF7QRwx6NTTnRT3rZzThGll-17cakalWTHnOnVfxzeQMqmTU86N0fg9vnt_2noiLBEGzdyDMYgihfUTHRrpoY_3OvS0zHRxjMEQW-xm-nqKeCqeEILaWlLk_rqBBlbeTln3lsLyU_R90rLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#WHEAT — D</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18787" target="_blank">📅 20:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18785">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حمله به کویت</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18785" target="_blank">📅 20:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18784">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یک تبعه ترکیه مبتلا به اسکیزوفرنی در مرکز شهر درسدن تصادف کرد، اما هیچ‌کس را نکشت یا مجروح نکرد. پلیس آلمان به سمت او شلیک کرد و او اکنون در بازداشت به سر می‌برد.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18784" target="_blank">📅 19:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18783">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مثل اینکه یمنی ها در باب المندب فعال شده اند.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/18783" target="_blank">📅 19:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18782">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">و از این جالب تر این است که نسل کشی یهودیان توسط نازیها در جنگ جهانی دوم به کلی الهام گرفته از نسل کشی ارمنی‌ها در جنگ جهانی اول توسط ترکان عثمانی بود.  اسناد بسیاری در این حوزه وجود دارد.  حالا نوه آن خونریزهای نسل کش آمده از خطر نسل کشی می‌گوید!</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/18782" target="_blank">📅 19:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18781">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سخنگوی وزارت امور خارجه ایران:
نیروهای مسلح جمهوری اسلامی ایران نشان داده‌اند که هرگونه تجاوز به خاک ایران، قطعاً با پاسخ متقابل مواجه خواهد شد.
در حال حاضر، برنامه‌ای برای مذاکره نداریم و تمرکز ما بر دفاع است.
موافقت‌نامه همکاری، مجموعه‌ای از تعهدات متقابل است و در صورت نقض این تعهدات توسط طرف دیگر، ما نیز از اجرای تعهدات خود خودداری خواهیم کرد.
این یک اصل است و در آینده نیز از همین مسیر پیروی خواهد شد.
منبع: تسنیم</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/18781" target="_blank">📅 19:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18780">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز هم در سطح بالایی است و تا زمان انتشار گزارش PPI بعید است حرکت صعودی خاصی در طلا و دیگر دارایی های روبروی دلار داشته باشیم.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18780" target="_blank">📅 18:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18779">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نتانیاهو روز یکشنبه به ایالات متحده سفر خواهد کرد و روز دوشنبه با ترامپ دیدار خواهد داشت..
روزنامه "هایوم" اسرائیل
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/18779" target="_blank">📅 18:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18778">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خبرنگار: آیا رئیس‌جمهور الشرع (جولانی) برای شما تعهداتی در مورد کمک به حزب‌الله در لبنان داد؟  ترامپ: بله، او این کار را کرد.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/18778" target="_blank">📅 18:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18777">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کانال ۱۴ اسرائیل مدعی شد ترامپ و مقامات ارشد آمریکایی طرح عملیات گسترده‌ای در تهران و شهرهای بزرگ ایران را بررسی کردند و تصمیم بر گسترش آتش دارند.  تا پیش از این عملیات های نظامی محدود به اهدافی در جنوب ایران بود.  #ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18777" target="_blank">📅 18:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18776">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBBfsDqUs-qBT8C5Z1tIys904fJgxswxyX7_YJfDQmfBB8t0F27hmoe8m5B09HEcU2WRMeisWUH6OoeWiw2eEPZTfjmxDCyC86KAoCQrhCs_vDzzv5jOVTQsNrpzTg_newnWIG-WHWxY1JGjhmfC-XczzNkWi4K7S5YX5-3lhVWQ8UPzoPwME5aT6qFaiAAdIxl4U28g7NuA2G9Nm6vt_2VsWIn7Jz6C5_oawPE7-DCs--h2EedBSgdv2yTgyWa1y8km6vxVQMNJOVvLjsAVPZ4tmzOlp4H2Xpv9ejwB2YbdLKuSY7rtqRE3u5Zk-PsycTo5ooMKIT12V2xmEwrpyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۴ اسرائیل مدعی شد ترامپ و مقامات ارشد آمریکایی طرح عملیات گسترده‌ای در تهران و شهرهای بزرگ ایران را بررسی کردند و تصمیم بر گسترش آتش دارند.
تا پیش از این عملیات های نظامی محدود به اهدافی در جنوب ایران بود.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/18776" target="_blank">📅 18:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18775">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">به نظر می‌رسد حشدالشعبی هم …</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/18775" target="_blank">📅 17:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18774">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وزیر امور خارجه آرژانتین، پابلو کیرنو، ساکنان جزایر فالکلند را "جمعیتی که به طور مصنوعی وارد این منطقه شده‌اند" توصیف کرد و از بریتانیا خواست تا مذاکرات مربوط به حاکمیت این جزایر را آغاز کند.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18774" target="_blank">📅 17:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18773">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ولایتمدار، عضو کمیسیون امنیت ملی:
به‌زودی دولایه از مسئولان آمریکا و اسرائیل را قصاص می‌کنیم
مردم نیز خود را برای تحمل شرایط سخت آماده کنند</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18773" target="_blank">📅 17:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18771">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tEstPWaWQbqXEMmurfJEMWQtb5HybZvdp7yxhNL75mFc-EzJHi95l4S-rp99UFXrQq0C_68tz9GJEqwXF3ZQEmVBt2SxvpMGltXNqqFMvJyKtUyHw1K0Ak5MtpEENYUbV4wwUTZING4FMiWBJweOfO4EqVgqbS1jN4bJstOaqGWSfM3OBzW1hN-5tQmLM1-kozG04Bgf8C1yAHhLX7FLaKWHYq14s6aUG90BNm2e5wv-aoXtRFcvGVla0keDP-75caBWhfldxwuQrfrdK9jirjhG3JElqEWG739-BfzRcgjLLluIrB1eNYsFk9ypip_2rmmqHBag--EBnAuhLiT_wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Clqdbfe5DlvEwYTL-e4DMEHm0uO6DjW5LLx08EEPtvSDnfu5BrlsdYHXDksMdocehRsUWw_BfwskIDGsFlM_ADrO4mF-7M-7vcM6wQ5pRGP5kbUuFxwDizbNBlqmNIpn8UkouqRjoNOTrE_q_xrAZR3qEHE2i9RRbmWp29GulRHAs7Lv-mHYOuQgTXz2EBuibzRLg3gedqIqd79m5qXpDPVFyFOmcJ7Z7tP5qPE_4-GzYHEbTCCT5GxqZTpWaDsvqScs68xLKAET5Kgqnba5ebg9mm16tWo3N5owwPZ2Yitw8apzMI5qJqvPv1GSd1i-xjyWKbs5GyTAbdEOCD1iww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لینک نشست امروز با نیما  #ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18771" target="_blank">📅 15:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18770">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMjzGVjtVgvl1A8vgfPfeHJDHA1_-DO4wsh6NL17rDHArPhCe6H9Hz9-t1FwvfLddaDQiZeJlvhbBua1XXFftbdJ70L-vFeLmS-chKLC8TKW02v3soo_T1Vem9braULSjdLWd_xCeytGbG5_YQNT9nlBKavahJw_KFE1l5LKo9G6VpsqZxNikD7tNQG-cdW6OreEzZWIYyz8KUewYVe-PFtpL-8B2S2JyiJpb6wjCuBzxos1QQo-KNIeG_Kda8TK-XZyTWBdw4cywRGP7WF5-IfKFXjiPmREc23h522riMQQn6bUhe7KvxhcJc-MCpApKT0UFAOGZ5wzpTlcWxzoHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لینک
نشست امروز با نیما
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18770" target="_blank">📅 15:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18769">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvISG5y_-CjhLfK8MbdkHG6fB2Ep987qkrsrR11ZqKWeKWl3LJrHxdlf03Gol8ZBiEF8zA76Ff2wg0dtoDOJfActqrjONPgIxv0pcsPw-68GguSkd3rrAftP1c68oDgsrsWMemsJfkyXAh6vy9PNF8yuCQu-wTF6cyfm02R9N-J_gpH9-7Sgkb7tMk-Z2VU8wRt5ERRBljlnARjMSDXL8b1x3JH3Hd4HraPYeWU4juXUP9y-jROOv_Y7BrzJQgkDa72WR3fwfyPLld1H-K5PDcJpWbxQ25VQ8fgCGbIlomZJbMc27nycAsHovUHX0gYCsgqUJHVjuOpxOKNk0hyAvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خریدهای تسلیحاتی اشتباه ارمنستان — بخش ۱  این تحلیل توسط یک کارشناس نظامی روس نوشته شده و لزوما همه اش مورد تایید من نیست.  گفتن اینکه وضعیت استراتژیک ارمنستان نامطمئن است، دست کم گرفتن مشکل بزرگی است که ارمنستان با آن درگیر است. این کشور کوچک عملاً توسط دشمنان…</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/18769" target="_blank">📅 14:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18768">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">انفجار در شیراز !</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/18768" target="_blank">📅 13:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18767">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c67f12a39a.mp4?token=RwDvTWyIZkLuXaI8H9kv9S8BOQe4hk4YszjZdoyFrEU6KAd1rNv5u1nLx7SEZZQlXltuJ0hqNU_-tQZdCcWnrUjRRUnnM9qlxvPBqU2wFNwAFmTVk1uCXAi1URg84C1lVBaw9pNjnGKFyw42kg3e1020dYTc7600i_ka-Kl_SmP7eTZljQ0-1TkV5MPhG2rHaFT_CmlRuChtNHp88L4iUCF3nFvuPMuDX4ElwaRz56PaePQj-US2lsBIId54DlKdA1jfGvIufE1P2H3e-DX83KoEGGNk3vW1WCwTJvQh8wXFIKoe_Iyy5Ka9kmDLd8eFe_2mANwZ97OcXBt7QdUZxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c67f12a39a.mp4?token=RwDvTWyIZkLuXaI8H9kv9S8BOQe4hk4YszjZdoyFrEU6KAd1rNv5u1nLx7SEZZQlXltuJ0hqNU_-tQZdCcWnrUjRRUnnM9qlxvPBqU2wFNwAFmTVk1uCXAi1URg84C1lVBaw9pNjnGKFyw42kg3e1020dYTc7600i_ka-Kl_SmP7eTZljQ0-1TkV5MPhG2rHaFT_CmlRuChtNHp88L4iUCF3nFvuPMuDX4ElwaRz56PaePQj-US2lsBIId54DlKdA1jfGvIufE1P2H3e-DX83KoEGGNk3vW1WCwTJvQh8wXFIKoe_Iyy5Ka9kmDLd8eFe_2mANwZ97OcXBt7QdUZxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدجواد لاریجانی:  مردم خودشان را برای یه جنگ سه چهار ساله آماده بکنند.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18767" target="_blank">📅 13:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18766">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">منوچهر متکی:  باید برویم پایگاه های آمریکایی ها در منطقه را تصرف کنیم و بعدش صد نفر از سربازان شان را اسیر کنیم بیاوریم ایران!</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/18766" target="_blank">📅 13:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18765">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">محمدجواد لاریجانی:  مردم خودشان را برای یه جنگ سه چهار ساله آماده بکنند.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/18765" target="_blank">📅 13:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18764">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKKSweMfnr1oNzJFcaRz4zwapMmp1eSrNIEUXu6DODohkJYyBECPG1_rzCSOx7nVil6cG-PoeAFv5o7cuB-3jXhbD-cTS3nihVsJBjwpbd9c3b6AqkppojmusmzOVIAny_VtJljauCcjg60ahjGr64GfY_OauX21bzsx5lkU8TMZGYkDNnTlmx4X9xUG4ysHA-p0QWNJljHz3IQP7EJMY4JVqYwHWNyv-eD2lsZyUKNvrUtTtnRCG3aA2Qfvi5TfYcRxPai5t86dRxjff85lhwKZUiXxF-EkRj1jJPUd_T19udFicrzzCl8ibUmeSmIZ3epgS2RE2tTaguQ-_u01cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک جنجال شدید در بالکان به وجود آمده. پس از آنکه وزیر صربستانی، سِنیژانا پاونوویچ، گفت که اگر جای اسلوبودان میلوشوویچ بود، پاکسازی قومی در کوزوو را انجام می‌داد.  وزیر امور اداری و خودگردانی محلی، در یک مصاحبه تلویزیونی روز دوشنبه (شبکه تلویزیونی کوریر)، گفت:…</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18764" target="_blank">📅 13:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18763">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یک جنجال شدید در بالکان به وجود آمده. پس از آنکه وزیر صربستانی، سِنیژانا پاونوویچ، گفت که اگر جای اسلوبودان میلوشوویچ بود، پاکسازی قومی در کوزوو را انجام می‌داد.
وزیر امور اداری و خودگردانی محلی، در یک مصاحبه تلویزیونی روز دوشنبه (شبکه تلویزیونی کوریر)، گفت:
"اگر جای اسلوبودان میلوشوویچ بودم، در سال ۱۹۹۸، پاکسازی قومی را در کوزوو انجام می‌دادم. این سخت‌ترین بیانیه‌ای است که تا به حال بیان کرده‌ام."
وزیر کشور کوزوو، ژلال سوهلا، دیروز گفت:
"من تصمیمی را امضا کرده‌ام که بر اساس آن، سِنیژانا پاونوویچ، شخص ناخوشایند اعلام شده است. ورود او به کوزوو و عبور از خاک جمهوری کوزوو به طور دائم ممنوع خواهد بود."
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18763" target="_blank">📅 12:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18762">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دقیقاً چه مدل آمادگی مدنظر هست لطفاً قید بفرمایید.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/18762" target="_blank">📅 12:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18761">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">محمدجواد لاریجانی:  مردم خودشان را برای یه جنگ سه چهار ساله آماده بکنند.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/18761" target="_blank">📅 12:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18760">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">محمدجواد لاریجانی:
مردم خودشان را برای یه جنگ سه چهار ساله آماده بکنند.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/18760" target="_blank">📅 12:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18759">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqoGMHDw_U2Xar0MP0fX8y8F9XJJ_uDKSP4PgNx7ZQwrHMWXs5aTa_dF8NKs8cEbpH147x-MsfPDPESooGAcYTVg33X-CJrAmQkXG5xr4DUFHR9S1XRVXnzhhcnvziRi7ozEaHZiJoCTfPa5x25ThCFjFk3S8ozRj60Obt-HAiHR0ebZb1VSz8P5ev-dmXNpLOqQ4jT7TaYfHqulmKFP1yMZvk8-JknJFV4WXoiRJ5K0lvk_Sv2XCJTQ114Q-gHwg7HuLiOnD79BHg4PZH6u0JB2oNeVZeQ2TEj1WlFefUehRFiWeG_UDyn83XwyrVzvduLQ2yQTe5m8umiDSoCitA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز هم در سطح بالایی است و تا زمان انتشار گزارش PPI بعید است حرکت صعودی خاصی در طلا و دیگر دارایی های روبروی دلار داشته باشیم.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/18759" target="_blank">📅 11:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18758">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔔
#دلار
تهران =
187,000
#تتر
(تومان) = 186,340</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/18758" target="_blank">📅 11:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18757">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ:
ما امشب به شدت به آن‌ها ضربه خواهیم زد، فردا شب به شدت به آن‌ها ضربه خواهیم زد، و شب بعد نیز به شدت به آن‌ها ضربه خواهیم زد.
و سپس، هفته آینده اوضاع برای آن‌ها واقعاً بد می‌شود زیرا هفته آینده نوبت نیروگاه‌ها و پل‌ها می‌رسد.
ما تمام نیروگاه‌ها و پل‌های آن‌ها را از کار می‌اندازیم.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/18757" target="_blank">📅 02:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18756">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وزارت امور خارجه آمریکا: وظایف مرزی و گمرکی درمسیر TRIPP  تحت کنترل ارمنستان باقی خواهد ماند.   وزارت امور خارجه ایالات متحده در مورد مقررات اتحادیه اقتصادی اوراسیا در مسیر TRIPP اعلام کرد، تمام وظایف امنیتی مرزی و گمرکی تحت کنترل ارمنستان باقی خواهد ماند.…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/18756" target="_blank">📅 00:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18755">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
ارمنستان به اظهارات ترکیه درباره « کریدور زنگزور» واکنش نشان داد و گفت کریدور بنام زنگزور وجود ندارد  وزیر مدیریت سرزمینی و زیرساخت‌های ارمنستان داوید هوداتیان در مصاحبه با «آرمن‌پرس» به اظهارات اخیر وزیر حمل‌ونقل و زیرساخت‌های ترکیه درباره اینکه به اصطلاح…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/18755" target="_blank">📅 00:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18754">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فارس:
چندین انفجار در بمپور و چابهار شنیده شد، علت نامشخص است</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/18754" target="_blank">📅 00:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18753">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدیده‌بان سرمایه</strong></div>
<div class="tg-text">⚠️
۲ مجمع، ۲ شرکت، ۱ آدرس، ۱ سهامدار عمده: آقای زنوزی
📍
آدرس مجمع
#خبنیان
استان آذربایجان شرقی، شهر اسکو، دهستان شورکات جنوبی، روستای سرین‌دیزج، خیابان آزادی، جاده
تبریز - جزیره اسلامی
، پلاک ۰
📍
آدرس مجمع
#درپاد
استان آذربایجان شرقی، شهر اسکو، دهستان شورکات جنوبی، روستای سرین‌دیزج، خیابان آزادی، جاده
تبریز - جزیره اسلامی
، پلاک ۰
این دیگر «محل برگزاری مجمع» نیست؛ این یعنی بردن مجمع به جایی که هرچه کمتر دیده شود، بهتر.
🏛
شرکت بورسی قرار نیست مجمع عمومی را در نقطه‌ای برگزار کند که سهامدار برای رسیدن به آن، از شهر رد شود، به دهستان برسد و آخر سر در روستا دنبال حق مالکیتش بگردد. مجمع عمومی، عمومی است؛ نه جلسه خصوصی سهامدار عمده، نه مراسمی دور از دسترس برای خلوت کردن سالن.
🚧
وقتی آدرس مجمع از شهر عبور می‌کند و به دهستان و روستا می‌رسد، دیگر سخت است کسی باور کند هدف، تسهیل حضور سهامدار بوده. این مدل انتخاب محل، بیشتر از آنکه احترام به حق حضور باشد، شبیه مهندسی غیبت است؛ یعنی مجمع را می‌بری جایی که کمتر کسی برسد، کمتر کسی سؤال بپرسد و کمتر کسی مزاحم تصمیمات از پیش چیده‌شده شود.
📅
آن هم در تاریخ
۳۱ تیر
؛ درست در اوج فصل مجامع. یعنی هم‌زمانیِ شلوغ، آدرسِ دور، و برای
#خبنیان
حتی نبودِ صورت‌های مالی حسابرسی‌شده روی کدال. یعنی محدودسازی سهامدار، هم از مسیر جغرافیا، هم از مسیر اطلاعات.
📉
این دیگر فقط بی‌نظمی نیست؛ بی‌اعتنایی صریح به حق نظارت سهامدار است. سهامدار را هم به نقطه‌ای پرت می‌فرستند که رسیدن به آن سخت باشد، هم گزارش را در مهلت قانونی روی کدال نمی‌گذارند.
🔁
وقتی در
#درپاد
و
#خبنیان
الگو یکی است، آدرس یکی است، مدل رفتار یکی است و سهامدار عمده هم به یک منشأ مشخص یعنی آقای زنوزی برمی‌گردد، دیگر نمی‌شود این شباهت‌ها را تصادفی دید. این بیشتر شبیه یک الگوی حکمرانی است: استفاده از بورس برای پول و اعتبارش، بدون پذیرش شفافیت، پاسخگویی و دسترسی‌پذیری.
⛔
اگر قرار است سهامدار برای حضور در مجمع، هم با آدرس بجنگد، هم با نبود گزارش حسابرسی‌شده، دیگر اسم این را نباید «برگزاری مجمع» گذاشت؛ اسم درستش بی‌اثر کردن حق مالکیت سهامدار است.
🆔
@FinancialmketAnalysis</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/18753" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18752">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">محاصره آمریکا بر ایران دوباره به صورت رسمی آغاز شد.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18752" target="_blank">📅 23:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18751">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سپاه پاسداران :
اگر آمریکا به «اقدامات شرورانه» خود ادامه دهد، «یک قطره» نفت یا گاز از منطقه خارج نخواهد شد.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/18751" target="_blank">📅 22:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18749">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پاسخ چمران به سوالی درباره قطعی برق بدون اطلاع قبلی:   اگر می‌دانستید دو روز پیش چه تعداد تاسیسات برقی را زدند دیگر این سوال را نمی‌کردید</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/18749" target="_blank">📅 22:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18748">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQdLhw3bw9gvtOBRjqQ7i4TEsU5wMrYv3ILyADGPcGCO6ISy39uOsUSwPTGUFrWUDZ0f7qkQYDbMGhmy-8gPV1K9qrxIf6ZATf_OIUj96dcqa2Nz6KB1NJpsdR6ef_BYLPAK-xEl3D1ScIJRUrvfDCKf4NckS-Nk3rTHNIF4bIqYfBwnAPItxG-GplHALzKn9BickdFcLmq7XmktI9u1d9hHPiIYAFTzvVuBM4alD5gDOOlst5JJkBxuDX9HTAav1Yk-0ZtojH2RlEZ3R2tCmdpdKyxaFqUXIg-hgNgtnBYyOIpxg8u9_iSJiUPSOa2dwueLjo5av2ok2yydRKWYpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت جدید مرندی:
برای چند هفته دولت ترامپ در حال تدارک حملات هوایی گسترده و تهاجم زمینی به ایران با حمایت چندین کشور عربی است و  ایران بی‌سروصدا خود را برای یک رویارویی بزرگ آماده کرده است.
در صورت آغاز چنین عملیاتی، آن حکومت های عرب خلیج فارس دوام نخواهند آورد.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/18748" target="_blank">📅 22:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18747">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">موشک ایرانی پر از منور بر فراز بحرین!  این منورها پدافند موشکی را فریب می‌دهند تا با شلیک های پیاپی، ذخایر موشکی شان دچار فرسایش بشود.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18747" target="_blank">📅 21:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18746">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">یک مقام آمریکایی تأیید کرد که نیروهای آمریکایی در حال حاضر در ایران حملات هوایی انجام می‌دهند.
شبکه ABC|</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/18746" target="_blank">📅 21:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18745">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پایگاه شیخ عیسی و ناوگان پنجم آمریکا در بحرین در معرض حملات موشکی شدید قرار گرفته‌اند
خبرگزاری فارس</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/18745" target="_blank">📅 21:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18744">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ به نتانیاهو دستور داد نیروهای خود را از سوریه و لبنان خارج کند - آکسیوس</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/18744" target="_blank">📅 21:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18743">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c52c0b59bc.mp4?token=DO4xsIpoFoOtnxx3X9bjVB9CcCNfloc1ymdJhBRJi4W1R3RzSzqG9g7Es_7VsHc9J18zSQJABwjdCAjt9T7ymNI5cJIbY5ZX_xzNj1Rwqzp-J6qOnIWvJh6mUCppCIehikhG1mTJi19Xt5qjRgFwnIPxr_lD6JcddUc0vK4CDXwFcmfwOtYRUk4gCGRNXCg_hDBZKGvC0ZkjK992U75jpyuFJnqBcwriAQmEH8HBlJxFy32eMktDDizjexF40O3Ksy7OQDnOCGpuJmyToovmxe0yggbYDpdYRp6Fhiw4whKlDmQyJrYToCxrDj7zQ3pyVNaF8BgUc5LAnyhkzBsBKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c52c0b59bc.mp4?token=DO4xsIpoFoOtnxx3X9bjVB9CcCNfloc1ymdJhBRJi4W1R3RzSzqG9g7Es_7VsHc9J18zSQJABwjdCAjt9T7ymNI5cJIbY5ZX_xzNj1Rwqzp-J6qOnIWvJh6mUCppCIehikhG1mTJi19Xt5qjRgFwnIPxr_lD6JcddUc0vK4CDXwFcmfwOtYRUk4gCGRNXCg_hDBZKGvC0ZkjK992U75jpyuFJnqBcwriAQmEH8HBlJxFy32eMktDDizjexF40O3Ksy7OQDnOCGpuJmyToovmxe0yggbYDpdYRp6Fhiw4whKlDmQyJrYToCxrDj7zQ3pyVNaF8BgUc5LAnyhkzBsBKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موشک ایرانی پر از منور بر فراز بحرین!
این منورها پدافند موشکی را فریب می‌دهند تا با شلیک های پیاپی، ذخایر موشکی شان دچار فرسایش بشود.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/18743" target="_blank">📅 21:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18742">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/599f22b724.mp4?token=amsjaPKW8lALvnhTeVvhzliV6iLPC5uM5j21N5020xEjMHJwQHNofejEmdYtoFYVQoYYP5nuQW6wqjkEtPxcyLnVP09xlAT9d7Ta-fPK4eBnoVaeHyfd365LmWBIEkRJ7X7bsVoaF-UYgBv-RLp0LJpJXtll8I-tf4gWDzUPjV4g9-Dbj6MwEwYiZDlMXkiVwzqOp4tkJgf3-KI-SM3_JxqQK7wOv-yO6xrIe_J0p8LikSHdJSIODyB_zSZoyXdVbJt01BmaMhc2PqXzF2LtCD_voQz26VmXJA5pMnrOicxShgPe88V-Vt5VoaeTUSMvYSJDqN0fc_8ezSH5O0POLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/599f22b724.mp4?token=amsjaPKW8lALvnhTeVvhzliV6iLPC5uM5j21N5020xEjMHJwQHNofejEmdYtoFYVQoYYP5nuQW6wqjkEtPxcyLnVP09xlAT9d7Ta-fPK4eBnoVaeHyfd365LmWBIEkRJ7X7bsVoaF-UYgBv-RLp0LJpJXtll8I-tf4gWDzUPjV4g9-Dbj6MwEwYiZDlMXkiVwzqOp4tkJgf3-KI-SM3_JxqQK7wOv-yO6xrIe_J0p8LikSHdJSIODyB_zSZoyXdVbJt01BmaMhc2PqXzF2LtCD_voQz26VmXJA5pMnrOicxShgPe88V-Vt5VoaeTUSMvYSJDqN0fc_8ezSH5O0POLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این دیگر چه کوفتی است در شیراز ؟!</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18742" target="_blank">📅 20:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18741">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">به نظر می‌رسد حشدالشعبی هم …</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/18741" target="_blank">📅 19:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18740">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اظهارات ترامپ درباره ایران:
به نظر من، و این ممکن است برایتان عجیب باشد، اما خاورمیانه در حال متحد شدن است.
ما در حال از بین بردن زورگوی خاورمیانه هستیم.
ایران، زورگوی خاورمیانه بود. آنها به عراق زور می‌گفتند. آنها به هر کشوری زور می‌گفتند. در سراسر خاورمیانه، ترس وجود داشت.
دیگر هیچ ترسی وجود ندارد.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/18740" target="_blank">📅 19:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18739">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مهر نیوز با استناد به منابع خبری گزارش می‌دهد که رژیم اسرائیل حملات خود به جنوب لبنان را ادامه داده و آتش‌بس را نقض کرده است</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/18739" target="_blank">📅 19:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18738">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:  "ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18738" target="_blank">📅 19:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18737">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ در مورد نخست‌وزیر جدید عراق:  او جوان و خوش‌تیپ است.  من این را دوست ندارم. من از این خوشحال نیستم.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/18737" target="_blank">📅 19:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18736">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8fda31b18.mp4?token=HAkhBYnxswhAbSkrC-3_9Y2k0XPbKKMdYUCkC46cVFF7LvWuD04xnB1S6GhlmANHv4t3Far-biAiNgAcAwWVmqIFpE6H2cymNgsriCB8IdvHzp7IpqJPDb14Wdg0yc4b2mrDCuT1M2Ed2fs7rsQF-yxgkfTqJh0DIrGLSiFGhMZryYG3CGSPemHMjvzOXzcOOHtd_w_HwLR7IkhHm_9t4JK3gAmG2nJUQ5nnweUoZnGAXe3FCwpzkD7dbLGY50jQUzCAQk7PJFOIpI1B4A2BXP912UanUAQSnj5ZlqtZuRPIQR05xdBZ7FXu8awt2By61PJ6k2iIL1UYSNjVTCkz2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8fda31b18.mp4?token=HAkhBYnxswhAbSkrC-3_9Y2k0XPbKKMdYUCkC46cVFF7LvWuD04xnB1S6GhlmANHv4t3Far-biAiNgAcAwWVmqIFpE6H2cymNgsriCB8IdvHzp7IpqJPDb14Wdg0yc4b2mrDCuT1M2Ed2fs7rsQF-yxgkfTqJh0DIrGLSiFGhMZryYG3CGSPemHMjvzOXzcOOHtd_w_HwLR7IkhHm_9t4JK3gAmG2nJUQ5nnweUoZnGAXe3FCwpzkD7dbLGY50jQUzCAQk7PJFOIpI1B4A2BXP912UanUAQSnj5ZlqtZuRPIQR05xdBZ7FXu8awt2By61PJ6k2iIL1UYSNjVTCkz2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد نخست‌وزیر جدید عراق:
او جوان و خوش‌تیپ است.
من این را دوست ندارم. من از این خوشحال نیستم.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18736" target="_blank">📅 19:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18735">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">انفجارهای شدید در جنوب ایران و شمال کویت!</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/18735" target="_blank">📅 19:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18734">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">به گزارش‌ها، حداقل چهار موشک بالستیک ایرانی شب گذشته پایگاه هوایی پادشاه فیصل در اردن را هدف قرار دادند.
گزارشهای تصویری نشان می‌دهند که سامانه‌های پدافند هوایی نتوانستند این موشک‌ها را رهگیری کنند.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18734" target="_blank">📅 19:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18733">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">انفجارهای شدید در جنوب ایران و شمال کویت!</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/18733" target="_blank">📅 19:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18732">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ:  نفت مانند گذشته بی‌سابقه‌ای در جریان است. تنگه هرمز به روی همه کشتی‌ها به جز ایران باز است - به دلیل رهبری دروغگو، خشن و بدخواه آنها که آنها را در مسیر نابودی کامل قرار می‌دهد.  ما محاصره کامل خواهیم داشت، اما فقط کشتی‌هایی که به بنادر ایران می‌آیند…</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18732" target="_blank">📅 19:05 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
