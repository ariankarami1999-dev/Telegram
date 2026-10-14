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
<img src="https://cdn4.telesco.pe/file/injPJ0msUHQK2sQJ5CHZdNuy4qxVxr3UZPUw_sZXZdx-rRSCltrl4ZSegl0zLgutHRjM3eTn_xm6QlezEUqiujXkZFn3TnzBTKd3xsDTRNjYvDRT5iQqfY41gUKQfqOpvk3SNisFzLHBtGPAfq9dv4bgMERmW3NIOF_kBp0jo7hCZhbO6UFjT_t1KB7QMrax_AEk5e-EO3geUJkkLwWUMf7sBbdYZi8WB0_flLBRUxJmJHz4CjHpuOec1D54oPYKb_nYbFxJoepylMtumPBc6ZFO30EFz-M1krDSkTEtsa6PJ4U3z0uZq0jgz5sSLqJTuRHRm0Azyqd6yvOGff2HBA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 466K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتارتباط با ما:@ads_Persianaaهماهنگی و رزرو تبلیغات:@adspersianaaa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 21:34:27</div>
<hr>

<div class="tg-post" id="msg-31573">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jg5tBOj1SG9CABWysSSmhBPNf_5p18wd7AivQa0Of6qi2weeNKRmcW1rU0vycptdRsRPks1x909lNjspmmnwAM8SWhTiY1Rrs5fMgKplX56pMTNCoQe7LfpK0CdvNGaQYSUpkNBOihrCv9x7lDXYHilFUxT2xN87iFmNd8zW1uPVErukfn_RYv7XPj9b0HWi0_Q34BwZUbLOjuL6mVZkTjGTaYKVtXfPIWk3qU2DioZmRFX3f51DmrKFeDL5jxi3jlpAj0lMU-0nSH4moTP89fAo2WVPBEV9Sq0HrHNc4fXR21eAgthNxZJVK8_Nx_zHDkc9MrEMwwPUH_hWZgvdLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
ترکیب منتخب تاریخ رقابت های لیگ قهرمانان اروپا از نگاه AI با حضور پر شمار بازیکنان رئال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/persiana_Soccer/31573" target="_blank">📅 21:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31572">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec824b8766.mp4?token=KEo-3U4TwmJJHq-3wtTJbjPJfqDw_XcHYtGNqNqbeUePIl9Udtmb4_ycL4KzwDcGV31TNmsmgUvBF_ihFRcessdbp4i9PM9ulOGzWjWkIwQ7AHx1fRsjQGcq1WZJ4jrI3UdtKRi9w56VP4qESCYk1hZvpyQ2rSgL4zyGK7qSiutCyvhYkV6wynPSS6AqmDOUKtR4OYkfyKAStQftmdYo3XzsdNxsD_koviLlB3QpldNZuipOtQuddQvvOfdXhTqhUvaw_is0YTGFMbgCIdzetDvpxbrp81eAu3xNk2p7pYPt6ucBiZkoSBOziDqeVSApg1TSDRsCmgQuTsHApHOVWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec824b8766.mp4?token=KEo-3U4TwmJJHq-3wtTJbjPJfqDw_XcHYtGNqNqbeUePIl9Udtmb4_ycL4KzwDcGV31TNmsmgUvBF_ihFRcessdbp4i9PM9ulOGzWjWkIwQ7AHx1fRsjQGcq1WZJ4jrI3UdtKRi9w56VP4qESCYk1hZvpyQ2rSgL4zyGK7qSiutCyvhYkV6wynPSS6AqmDOUKtR4OYkfyKAStQftmdYo3XzsdNxsD_koviLlB3QpldNZuipOtQuddQvvOfdXhTqhUvaw_is0YTGFMbgCIdzetDvpxbrp81eAu3xNk2p7pYPt6ucBiZkoSBOziDqeVSApg1TSDRsCmgQuTsHApHOVWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
افتخارات آرین سلیمی و کوثر اساسه دو ملی پوش تکواندو ایران که اخیر باهم ازدواج کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/persiana_Soccer/31572" target="_blank">📅 21:15 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31571">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mquPEYfAFJ_5in1irh7jofU0bPzVJfsRpAy9qxr-J1vcZMzZbiifGG2ynhjRM3pNifupcgL_BQzzOH3BXpFgzNr_VN1S3qwRcyW_aq5UbadlZ3jUaMpTG7WftIKS_y2QU6irtK6-KfoPNRdn1NLhmO4UfWQC5PEH-p8Adalec3it-DfNYSBmf5YOC2gi6Vrxy3aVz717WXMISmO-Tyb-pvJupuwrb6vbEdpgRPgjV8EtVoZthpl5imE9InyCrPunjWh7ZPK2LCT4WbfHM1qhCdiS5C_0HWKVNMSsC4g5zNJsrgUB_BGhFQ_dDURP3Uip-3_P6wg4m5Z6rzKGs8VIJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
وینیسیوس جونیور ستاره‌برزیلی رئال مادرید به دلیل کشیدن موهای سربازیکن ویارئال چهار جلسه از همراهی‌کهکشانی ها محروم شد. بدین ترتیب دیدار حساس سوم آبان ماه با بارسلونا رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/persiana_Soccer/31571" target="_blank">📅 21:15 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31570">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMxttup6aLUhJjZ-NczjvvYtvUPndlYR6_oJFhoVZQDTZcuvto68Jkb-tuZ67NGFQh1U_5xlysGSWqes0NZvgqdFTKnZlbu6HUrRqCxXzpmpVrsPh0gC_5uf-UPhoG16HvsA6en4ZY6ougdIbix3D8trSrOJymu1lXIOtJ1Gb4OIdn6RLiTgsmsoSqfJuDpTDS8FhZxt83bMdw58j8KEitGE8yMp7Zu4bcrc8_R16n1yJ5s1vsCDtVQuOA4dDKUn3fU38BZlVan-p0l8l7PH-hpqGEQLWvxC4wGnoCP5MGpQfpAfHV9KArg06cwBce3qK2YkUeSF5-8OcgcbW1U3Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته دوم لیگ قهرمانان اروپا
🇮🇹
آ.اس.رم
🆚
رئال مادرید
🇪🇸
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🛡
تا ۵ میلیون تومان بیمه شرط
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔹
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/persiana_Soccer/31570" target="_blank">📅 21:15 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31569">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGfnbluMIHsNxRj5oVCLsCROQQ7bLb2fB2ujn9zIaNRKq5X-XRxoP0pPWzIKJh1dgSnd96X5euUV-z2uc2tAE7AGvVLlcsLN9l8kUEV-z39oJcalAq5RC81ILRh3ULrqqRbOeM_o8SCDM15iEngtaxlf-rz0uazaNKffjlyBsSyFoOYU8QafqsRPMnMyl-FQ05PvUDMrlALYJDLEdzyXI3CW-CXb6uEVy3mLVWqajWoHQDkZaKz43oqsqrzg7V3HY_1GzXPDmvo1bTKBgFYY3jFbpcOY4ii0cmefHBsq_ooqbxjB8hkVqRaCTm8BS6fzV3uUjNDRoZckqQ71aM5YJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
#تکمیلی؛ نشریه کوپه: باشگاه رئال مادرید به‌کارت قرمز وینیسیوس جونیور دربازی این هفته با ویارئال اعتراض کرده و امیدواره که محرومیت این بازیکن برای مسابقه الکلاسیکو آبانماه بخشیده بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/31569" target="_blank">📅 20:55 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31568">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuguvMs9MXpigwRnbZGx4aTRRQgOv-vscXcFYMCFeKhvtz_VE_cLYAiItjK0OH9YIBy-XRJXNOsC5cAhtk1D6EuCQg8FpIxWMb2QXEjf396Xiui0WwM-O8U-sSp47H2H0o-Z-F-X0zXK_XLH8gsjcz1Ukv8Njyc-KhIMTmEhL0KZXud_lS0V35mik9JS_w-VcPhSH2h3MAtf75tcZcHZojmyikMzgCZ5DBfioaVYJmEs9B0-AVfIMRUmRcVIznvUOzuSF0g7ieggMMqMG_U_jOXBNdRsqped8Te2p4_YSTf6qSIcKId6CdNshXNVhwHLS-jH7TGhmQ7xiU-O1m531g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
بهترین گلزنان تاریخ‌لیگ نخبگان؛
آسانی بالاتر از رونالدو و فیرمینو:ریاض‌محرز13گل؛ سالم الدوساری 12 گل؛ یاسر آسانی 11 گل؛ روبرتو فیرمینو 10 گل؛ کریستیانو رونالدو 9 گل؛ میلینکوویچ ساویچ 9 گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/persiana_Soccer/31568" target="_blank">📅 20:44 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31567">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFb0tDyheyJGAQnAEk7nW1lTnTJviW9bPjZbJtMrE4Z8YYt7sgQ3DQEkj3br3SexoB14VPTiosm-Le50qJhGlf__FzWy1Gq-Ud_ycEswkFmv-ePa9_JqWf94cm-MQueismG1yzS4ruGdQdV30B3715RMmPJPPiOEwplF7-yCImqWEi9mjopRwlPlz5z3HlPufVQV2U5hT1L7oYGNMHlWeBMLN1pNTxBdW8iSCE96pFOy5pjQFj7tOnkBMLWiei-r-YvIaLJv6sCBwYp03GqS8rVy2EnG5AS5F4Z1_2yBz34BVhgFjjE9BjOAAwILNRaFnW-G1Wf19A7M6MsoF6g9oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرین سلیمی قهرمان ملی پوش تکواندو ایران در روز های اخیر با کوثر اساسه از قهرمانان تکواندوکار ایران که جفت‌شونم کرمانشاهی‌هستند ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/31567" target="_blank">📅 20:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31566">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfzSE39QO6BYjWNyilil9fx6uFIy6uZrQb7zB3yGFkxuAs3Ij2txQaxOzfdiVWZwB1kEwKMj2WOLOEyrZNXRw0reJ3LcSAhpJeSRTI0XOWx3rSmf0fX_9hTHMIY4dmucZ00vFYLedH_GGEL6c2xdewdAUUPA_fIamGRuqIa30xIqWW0_y8o8mO1fc3k6FPsRVKrlQb7GwtgSA0oN0Ug0xOLFsaltsjQUaeFolGYGVgcn9LEBoa29I8xX5ZLDoljO6RocZKiiDZYPcBmJdEoEgJ0J_PfZcR9aTUEJZdvaezUlDM7i5N4ZajcV0j10LOldoe3kIihOGf25K6qfoLF3zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه شش دیدار آینده استقلال و پرسپولیس در تمام مسابقات لیگ برتر و لیگ نخبگان آسیا 2027
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/31566" target="_blank">📅 20:16 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31565">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0UFbi3Xud3buUghAOBjM61aU7RZv1lACiSKusaayb6JWqfNEcNXCVrrveboliOlCS0dD0bLpXwEa04FI8ItnXZMPbjjJHObUri2p6n9QTrdFDe3AogxKVFjmg48F6XdHe3hjyqu2dAnJK0kmZ_1P7Ejx0EjCh6gb_JBoELDhR0ZLi9ZZLapnG1ZT-tn-pD3IWTggvtSIN8gIniYnaCNwIC1pYFaBrsREi5N0xduTTJiN3youoHjhVlV_XETSgjJbvuJrT1iOyAPHRd75iz-4FWt87fE6930WCf6whPh1SyNuQzq1ANnR7BLS5zbYwGIy3JSddM6LGlYi0RaPJ3n8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول لیگ‌برتر فوتبال ایران بعد از برگزاری بازی معوقه هفته هفتم خیبر خرم آباد
🆚
پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/31565" target="_blank">📅 20:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31564">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmATrMNimuNQw0AWlZlSaUq_njv4SXsblu2Gmr2RRKxEjIJVXqGAuRqzuqe6cXMgcjTbyfNoC5psXrFJTtGhQ3MS-Ve0c4ZhA8BeOs8CI_KOfDy5874JpTS_zTpW_DORBFAjxxBQEDJejjdL7MRlXN-zKljMRIB3d2yBD0m0dswbtMMO9cbikLUj2geBux3_ISjyBVaF085pMk4_n74o4PaChZEWBFU2C9SJhOxUTWax4M-IIHxNRRhWRQgBFdJJNrioOJnHx8P0yYEugfiOzlEpJsbWfmDpwm6akw7MVCE4paa2nQv79aBNpUYqtnUFrOJT95ssWu04s3AI-3TzLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول لیگ‌برتر فوتبال ایران بعد از برگزاری بازی معوقه هفته هفتم خیبر خرم آباد
🆚
پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/31564" target="_blank">📅 19:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31563">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TjEtX-0lSpyTDJzajZhw9bWNzkUK8o4YGI2OeLDaY7yMyQQaYPJOBx8wMQWvpetINmBJPpGkwp5ghP8k4EuKRbY0ubk2LVTq6hhr0iFGDr6LtwFFCKjJwv_X3bUzECLQFOF0w5HtS1F9Og_59jyFdSI4VVZ2viIWuFNVTcxjioA-IWArpdTHHp7eStc1w1DOKKMETHLrah5_5adDwiuMqB0BDwwifDwG1fGRMSTLxzIZ8q7xzcHIM5dvwDDm9HAO392txpH69cuj9lm5Y-ChHLHAV-JN6pwfBqA2DnZrGGjo9ewVDM7OAUwL2jStxVlRXJhVH0URFOeAI-JL7lNLTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرین سلیمی قهرمان ملی پوش تکواندو ایران در روز های اخیر با کوثر اساسه از قهرمانان تکواندوکار ایران که جفت‌شونم کرمانشاهی‌هستند ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/31563" target="_blank">📅 19:14 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31562">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfyC7_XE9lmO-MCp1jiFlnZlHD6zBCqZsLajilvG7F_0SrGKUwQeoiVVe1R5AeEOvu_WX9Ra8B3Safk0NQ2WqzF4qSVs4mqpr26l5ckHdDnh6l9wTre09eg6ybMq78fzQdrq0J47_2gXb7tU8V8UXY_dzGVyH6Plpa2808GYg21ZOwGVvudO54cMiOvEWC7-Cb6VH27mqrirONXW_yUzMUaIz1p6wks0KPuUjVnXwjL9f8s8NzhKPYw7W6fU4c00gsVWm6K0ANh-yNLmfOPS672x7HpmJuVUOEyuqDjHElNGNHGP9JeNDymRZaPc9tWht1DbdN0LzK3R403G2U7Afw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
شماتیک ترکیب پرسپولیس برای دیدار امروز مقابل خیبر خرم آباد در دیدار معوقه هفته هفتم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/31562" target="_blank">📅 19:11 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31561">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b787TNN7q01FN3RBS5QKsBFc1ukMfSkWGYAPFktSsjTkrpwM8n-jdu5ENtcG4oDmSSlHM1paEbfriuZwDbWxyo_3AVQEEYWTD-pmCb-A8oPh9flFn_Nf5ORdAsKZlSqdYLqE9On_nyPHvvrrhCb2UAG13OTxcPBGO5idzygKu0rA9iVxpfQBCLi4Cb68HhOSjDIsCgd1Q1RLyaZ8-9m92Kd7WzguwV5ddCUUCRc2KYmvb2CLAESODFYupZms56jyGaMGTdGPDnrE4kKN_3QEK8tF9wK70LsTGvTJ-3yqJuPWV2_rbJDbAUNwaom9OHmelAzc8JDQCmbyw-fBCzf0RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حمید مریخ رسما بعنوان مدیر برنامه محمد جواد حسین نژاد ستاره ماخاچ قلعه روسیه انتخاب شد.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/31561" target="_blank">📅 18:45 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31560">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f16cf41e64.mp4?token=UqkbQc3SttmO0otUjugaQc4Nsb3UUkhpdTu_laWDcLwQ4p8_LCUWqSxqkQ1r3L6KyRD_4OFu5yoyhzMDi2aNrlznznhiFMBy7U_4dlphDSaYIZ7xiHtcSpF3uGC47Ixr4mIfjTMJy-QdsvOBqw6VSu2cJ3uf6ocqXP11HTfgI1U6qDyejAO1-o_5dfDxVWLlCjpnawGcFh5wjF01txsfeiach8gEq2YCGGhfDbr5QuQo7L7Xls_n8OXtbwP1BjBEjPjR6WGcBQ0iPL-qxUJs_KchNeYQWdFCwxXqO3s2piKLNGWpXu1cJA013df38xS3J1UBd_W8xSkWTXt4GHVbfAFC_86e0tV4LFd96-1ssoOi5p27hyP84D_-BXa8ZTfyuJVaG5974Xwgk7BS59Lh7Af03zbcRZDYwn08YypDt5SGi2u6qvg1peRq8KRgI4Cgze6vvPTIpM1jDFTXE7tf_IA-08MU0g59Q7AvXS26STfpwKgQL_tqAdQAtPxeLslvzHAmjKoX7RvqvOTpdPJA7dEeCuVoPEH74ACqOytv_D52xKjIfdLh5GM7Cx1B2Hn71qX9Fk5C3NhJ8wpb1DboVGxJClFv-elZpsi8yfRi32g-tzGoGiJAhq-gTcZESI6yciTAU1dlwljYU7IiJrGH8nlAV8k_4eXDOMfdSXffiVo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f16cf41e64.mp4?token=UqkbQc3SttmO0otUjugaQc4Nsb3UUkhpdTu_laWDcLwQ4p8_LCUWqSxqkQ1r3L6KyRD_4OFu5yoyhzMDi2aNrlznznhiFMBy7U_4dlphDSaYIZ7xiHtcSpF3uGC47Ixr4mIfjTMJy-QdsvOBqw6VSu2cJ3uf6ocqXP11HTfgI1U6qDyejAO1-o_5dfDxVWLlCjpnawGcFh5wjF01txsfeiach8gEq2YCGGhfDbr5QuQo7L7Xls_n8OXtbwP1BjBEjPjR6WGcBQ0iPL-qxUJs_KchNeYQWdFCwxXqO3s2piKLNGWpXu1cJA013df38xS3J1UBd_W8xSkWTXt4GHVbfAFC_86e0tV4LFd96-1ssoOi5p27hyP84D_-BXa8ZTfyuJVaG5974Xwgk7BS59Lh7Af03zbcRZDYwn08YypDt5SGi2u6qvg1peRq8KRgI4Cgze6vvPTIpM1jDFTXE7tf_IA-08MU0g59Q7AvXS26STfpwKgQL_tqAdQAtPxeLslvzHAmjKoX7RvqvOTpdPJA7dEeCuVoPEH74ACqOytv_D52xKjIfdLh5GM7Cx1B2Hn71qX9Fk5C3NhJ8wpb1DboVGxJClFv-elZpsi8yfRi32g-tzGoGiJAhq-gTcZESI6yciTAU1dlwljYU7IiJrGH8nlAV8k_4eXDOMfdSXffiVo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ریاض محرز ستاره 34 ساله سابق منچسترسیتی با عقد قرار دادی دوساله به تیم الشمال قطر پیوست. الشمال یکی از حریفان اصلی استقلال و تراکتوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/31560" target="_blank">📅 17:27 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31559">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KM7jYuaFwOXpQqqBTypw1q0r2A54MWApX5hgjVlZRv25SiE2sAsw3QjHgu0ZyF_5fnUq6hXvTvcIa7p7Z-c-o6cNquenGr-FfeE5qnMSZ1HpX_Q_zrabjuxSw5ot5nz6WSRMQ5Xnbos1Wg8sxXyi_kRTBESl7FNP4Zy56H6ErI16W1uM63fc3ltah7mpC3sGyhnuvC6uG0Vv8QyEklEINFSrwXDCrUey2YbyKQFdiPucLOKVDyqV5Tpj0-JPZkvSXSGtDzHT7dlN8_cRzDdnzvwOqukejDoP7wMZ1Y5uoHUFuZHSmyfr_OFJDrBojkNERNo28qjfql89YCSw2VK5lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
احتمال گران شدن ۴۰ درصدی اینترنت از امشب؛ بر اساس اطلاعات دریافتی از سوی اپراتورها، تعرفه اینترنت از بامداد پنجشنبه، ۲۳ مهرماه، ۴۰ درصد افزایش خواهد یافت. همین رو کم داشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/31559" target="_blank">📅 17:17 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31558">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kh5Otgxr3IhpJVPvqI7fK22WS74n6p8_wjDloFaX5FCCjYmBqumlz62S4WIlZOJfXTP_d3t4VzJcblVFUbmKkbGuDsRGFMSxlWNlG45THRbrF1Ernn52tLWWievkKLS169XpffHlDl31aCf2MEgvblzb84zKXonknX7IrHdVISXp_tCrWowcEePv5tntUTK-f50psRKT-npzG4HoC2SW33uhPzOavbLhb04ruvUDzf0h5WXuAHBnn4WGC2Q_RAzGRCfJ3OanuVb8BjCQ3ZuuoeFHMTbA7eHw4SXAOKhLWHCFS0oIn6cEDArWaAawUhF3_cdSnGYWBLOzukYM073XQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ کنعانی زادگان، ایری و بیفوما 3 غایب پرسپولیس در بازی فردا عصر مقابل خیبر خرم آباد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/31558" target="_blank">📅 16:19 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31557">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjrBJWiRwXJcNigbbIAYn7GWP-3I_rQyAL9IlcwJaulziNA_WBEShiZkp44OlvY33-KzyEpTORMNdcZTKYVAM5wgBwb2vWrOnXT3rQbAHf-gaczec70u8NGBeJX4YYV-JZDDmAN5Z9SOi9a1EnYRD_0xxObK9jzRwXKPXxPwInKRqtwOIa-neI0qwsUEOGFDBlPyQiDRM9l1CzFRNyTWZ60zw3kucg--rZ9kGqiILeoomFkjjsqQDbBfjXWRRk35RmafvUd_U5jGcsFUS8vAFRQIXApeEp0pP1tGp9fUm-hGOpgse5plD7z1rvFDdlMOlOrXjEKTK0NGAO2zGVtkzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
معوقه هفته هفتم لیگ؛ ترکیب پرسپولیس برای دیدار مقابل خیبرخرم‌آباد؛ ساعت 17:00 شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/31557" target="_blank">📅 16:06 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31556">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwV_zY5IDgmIf7GcSb5jlR16iLqmNTiFQavvsXapCkAZG2xTmz43CFLIxtPCzk96gX7sJMCSEcedumrozwERpN41JKx0DjUScDlOmrG9lDxHC4hi-r_dUUhSz5ZTs5OY_HO_7M3MUFSH8Xw6TLloRob_Waydh8KyU4BPRSCoa3BeTrLUupX_GN7Ya36L_A4LYO_sqCvD7gQGbG7j0Zn9P9FJbhKkNBarF25w-UpMXy_9SofzkHLtvEz0yPnONE_nViGFJw1KLT77CmrSY-GLDCKhzHZ7nxxuzjx0lxu8egBjnsO7GaSTJkvF7HulsrGUkpCEuYu8x9Xnz55R8JcnUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی پرسپولیس در بازی فردا با خیبر خرم آباد؛ تیوی بیفوما دچارسرماخوردگی شده و اگه به بازی نرسه به‌احتمال‌زیاد اورونوف جایگزین او در ترکیب‌اصلی‌سرخ‌هاخواهدشد. کنعانی زادگان و ایری نیز دیگر غایبان پرسپولیس در این بازی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/31556" target="_blank">📅 15:59 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31555">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLbx33FXVXtHiWZxaT409qsPVN58o2UfghVFd2Ao1bhyofapzYta7z6DuxWU5VF2nl_ap3lcf7q30klrNo2LD-r9L2r4q-E9FKGPJ69P6hYYem_alNhUxc7LY_sVLwfnd25AgzLRKh-S01ghta4V4J0Q8C3FTnwhWwmpYGvDQGOC9P1jK9ht2-L3doJX2SA-9v92s4Jh2sLQtv1pZrn-EdrDfgCYuDFZ_erSanDApI32TK3g9evTXzpyPSAA1mHoqzX-A8OySBOrWk9pXtAZvSN8p6uIaXpjkpywbkdWJ5zbp7PiJJstH6KksvqAlvLD8bekGev5K3wTqPgIVRdehQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
گالاتاسرایم نتونست نوار پیروزی‌های بارسا فلیک رو پاره کنههه؛ آتش بازی ابی اناری ها در خاک ترکیه با برتری چهار بر یک مقابل یاران رافائل لیائو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/31555" target="_blank">📅 15:58 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31553">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6BfdiSJIXy4iOdrUQMg25H3yxwV8nul_zmUSV4NTS4YMN0c7wkjxWquN76ONf3R0Auc4Ct6yyaGVbjdjc4iJAw3hyhJKYht8auFY7jPlrEpRLcTKlHBjb58vfiPLSatkGiV-ebh6Oui_XcUf-EyT-MPQtmImaS_Y4XQq0GaWkdy6lzlEmz3IdyVQ6foP8j7aHlCDX1WN5damtBwcZZKv1xxg8ge7hMmpwKPsv6lXqkN7RB5RklIdWZPh0V20-uhyJ392kKFfULYMcNtUU61dE6ffO43MpoDjho513U2mxxi1ZNtYNj-H8-Oj3GOgB8bSa2pVIS0aZkKSh7CGz52vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GHXjg9IqyKjJbWm7Y3dCesyxlnhSjQsIi8rZ80O4QQSss6FYpJCSAPgAVQbD5tU0xCrh15GCnm_oE9KaDuZmbugAJP3ghItLBjYPv4KFrj-Qke-3KnepHWcuir-ckiVhvQiJDjtoPNB_J0vrxcPUjaHqOh--5qX6i5Us51vkEq6kmteswScz41zb2HD8YEfJc1kMJS2qgE2XXul1CJYfFF6sL_XDmXJqLPCbcfvynZKKGVCyKaavwmcBcm1bnPKx6IcfLh5eI6fsBwdHzmUWKK10MeShbmN87uzA2Ca9SJc1d6llge1vzeBTmT_cmMixM34IIdLTGYkxT9rBRCnGGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
هانسی‌فلیک: یامال واقعا یه‌نابغه‌ست. بعضی وقتا یامال پاس‌هایی میده و بازیکن هارو تو موقعیت هایی میبینه که حتی منم قادر به دیدنشون نیستم و اون اینکارو حتی توی تمرینات هم انجام میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/31553" target="_blank">📅 15:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31552">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔵
🇳🇴
رسانه‌تلگراف: قرارداد هالند با منچسترسیتی بندفسخ نداره حتی اگه این تیم بره دسته پایین تر باز هم بند فسخ ندارد مگر اینکه سران منچستر سیتی با فروش این بازیکن موافقت کنند. بین رئال و بارسا هر کدوم 200 میلیون‌یورو به سیتی پرداخت‌کنه تمومه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/31552" target="_blank">📅 15:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31551">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIodroVAA3_wdq8qZYP4juvFAF-fIJs3wWKnG3hW9t_-Hg9sXgHYj0G7DNAj-GykNsZQRf0QUu4g1BVbNUKK1f3mQaVuL-YHeMvra2MDGg0x-EzWp13re4d2TxEKIXtMD_9J7ahWZJ_6ukqdU54rlg8da86ycTLKQbfdr5jP9m10mpjv6p7bPG7Ki7hyEprsuYLyMUan2TqsNrL5rDJrxatGVAq3-5FTiwyQWX3QP7gfKMg8gWxE4sGVFuerhwN_jngrZZx_joY9pFf4_XqMqgFWXQlKDUALk4Z16kT0tndCrF7Jd5854oq6nQKN0cQRRtgFIyrXMkYWrJnnz5_QxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درصورتیکه سازمان نظام وظیفه پاسخ مثبت بدهد؛ علیرضا بیرانوند دروازه‌بان 34 ساله تیم ملی با عقد قراردادی تا پایان خدمت سربازی به تیم لیگ یکی نیرو زمینی تهران خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/31551" target="_blank">📅 14:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31550">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bkg6I6YkdpjdRUYjjelJSjmspmtOlSTmk2eu62WQrnTnuNxgBg0wtuKu5WciZT3ih9C1k557GJ4x3-EtkJhvC73WJTf81cIqwJI46wIkO19cefQ9KYnnzLyPCjtyACnuY47aBVm5pkPvOggRgtNJCXb7_I1CkW5AacP8fKemjvCZR_aW2SXY3tTeaUzolexZHj3ifsbWuj-B16KHseSfxiW20IXgzVPqndnZENc7cokFM5N3tcvIPsbyO1aUefnqc9BNToPvWc2hoVKtsgt-UfZ1HVgXjPVNmzWEFwafEr7AtTBdsyPBB4jE2Ie__dmkA7a1LE6sncrTPspiju28GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟢
💰
#تکمیلی؛ بعداز موافقت مهدی گودرزی با درخواست سیدمهدی رحمتی برای پیوستن به گل گهر سیرجان؛ مدیریت این باشگاه 80 میلیارد تومان بابت رضایت نامه گودرزی به تیم خیبر خرم آباد پرداخت خواهد کرد و بزودی این انتقال رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/31550" target="_blank">📅 14:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31549">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNxLO1-iPiBek8Q3H7jgZwNdNVaAKO56TQLPBFUxtjRhqiJSVff7919VcSv73-4-5tDpOFPqGs7u7rGmWdoVMTgzA98uFEuGbG9Ep-2OlxYj0_J3kX7WU63vxSpRlXa0rUxnZhv0UH0uHix5rCbrp9TZONpKn8zAM4M1njkkf-YNBN0I8Mikt48cJtJK-TCttGC0DnItQIi2b-fu2Mjklad8TlM-JTb5dDR-AQvEk3mlQoeocEBS4CCS6gOGSNMjzFd7RImBYHQERL3SdvdQSV6yskeOUwNjNCvHA4DIE_QrNeTz-wHHLWc7phmbpQikwDuwrzpxw-a17zqnvQl6jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
هفته هفتم لیگ برتر ایران
🇮🇷
خیبر خرم آباد
🆚
پرسپولیس
🇮🇷
⏰
ساعت ۱۷:۰۰
🔴
انواع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🛡
تا ۵ میلیون تومان بیمه شرط
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔺
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/31549" target="_blank">📅 14:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31548">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇪🇸
🇪🇸
هانسی‌فلیک: یامال واقعا یه‌نابغه‌ست. بعضی وقتا یامال پاس‌هایی میده و بازیکن هارو تو موقعیت هایی میبینه که حتی منم قادر به دیدنشون نیستم و اون اینکارو حتی توی تمرینات هم انجام میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/31548" target="_blank">📅 13:59 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31547">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwZz-VUb7GbkPpLjcidexRUWltNRKApUq9eV3W9pIKpBfP2qNb9e7RxpG75d9DHkX72tcwWBr7Ly8Y6lW1KU33lUPvmUWiBc_uRQ8_vVHO3yPFigt94--d1i4mi3CXyooRevvm8bH8FCynpFlSuS7-BbA_teSurNJK1EtxD_5uUTjVopj-zPeF4ylFIkfvo6CsCS11gNNQ_PkJ2FPRage-mKx0KGCWp58I-UlopPL9ffyXw3k9YJn-C3lrDk25ThVG0LsKtPEEemm0g5QV22zuEp0qIPH3iop08eSHpl2ia2ZaAagAhjKbS7wcXpbHjsuLurbaWEilFzSiHdF-X1aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
گل‌های دو دیدار امشب بارسلونا
🆚
گالاتاسرای و اتلتیکومادرید
🆚
منچستریونایتد در هفته دوم UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/31547" target="_blank">📅 13:45 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31546">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDdk6Y_viNBjJvLFSjYuhgal3Nbc0iFo1_hprFKdOqavYTIBDVa0aSMKB2R6J3EjUwFGpUbp6JIm0DW702w4Ql6BldYtQDO-1sRSeaRVnNTGqG2emrmKZxZSJtNbuhgfT4gk9Nzlde4b_kLhJM9szZTcjxVfQPykGUOyG_9BR7FnbBMwgZm7wqYo0NEoDhwQP5Ud8H92J1S_CfOOQuN23gbjbFWKVcevNAOX0o11YS5Z1KKi64JDWcDKHP5R_dp9-4nZw7y86_IvaAjc6nwGRHyHBCCLuMg_Y0PuYA91BT6vbaLCazy5u-IKdVLjtZy8UFynsdub1yMa5gyDmn3bfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس‌رونالدو: اگه‌کسی‌مسی، پله یا مارادونا رو ترجیح می‌ده، این سلیقه شخصیشه. بهش احترام میذارم. اما این که بگید کریستیانو یک بازیکن کامل نیست، یک دروغه. من کامل‌ترین بازیکن تاریخم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/31546" target="_blank">📅 13:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31545">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLMD2k-ybmz6BlqbVQIUJKp_gAD0UTyKCmUyqZ8gIaazZAfTUeCDLWPcLp2qguVfk-sVjOh17ggRIALHV9TIwG3SMIQbX1DyMFrfh5ntkmwx2menDcJyweo9dbeyPPnYPZbZRWO74tYuBzrYdEjVeX5KzMiYtlooGaP9IQGl8YWdFjaJ0Ouh2q1-ixX4_EHFn0iP8E7QBK2YmndgYmluBfCNfK3CNfhfSMcQoOhNOAEeBONA-_Uq6LIiCEvcaa8eI6ubjQL5d8Rvt2jFykHhGgPoSXPLUIfBZDJXY6q8PASuzodcf8cBE3lgvrWfgRNiq_McRrw0j2u_50sKJVTPSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛شهاب زاهدی رو هم‌تراکتور میخواد هم استقلال؛ طبق‌پیگیری‌های‌پرشیانا؛ باشگاه استقلال میخواد علاوه بر جذب یک مهاجم خارجی مهاجم 31 ساله سابق‌پرسپولیس روجانشین محمدرضا آزادی کنه. بختیاری زاده به مدیدیت گفته نیازی به آزادی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/31545" target="_blank">📅 13:04 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31543">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cp4l0CrjVf2iA-2Az59aILhWTBQXrXQMxxg4Wd5OH463D1DqFoEU9WbeDNXVwfoLLgJdLxR9kUbMQlXCve2bhRotpoAivqUYZYIPm0_j0cM62Lr_rm9Mr4hfASHxpUn-2MpfzpdBOZGdVVcly3-iolDGY-yMuiBxHcDjBb0k6rk8IBsYMMCXp9VE_bMQXK2_HTkbk6xYo3WajyFIgJLgeVnHPiRnM0WEbCFgqbOm2-Uvlz7kgP8pDlKyciCTSkLisrHRzObBnMSmyqZCCmufEJeIqzJOOqJ9b28vNOg4Bs4-I7NDjoXcC2xlrdvgVqfPjAc1wwczt0JOXhcOZwukNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X_kjvKX_LFV4NoPy69N-jDjq_GQ6pCXf7knLsO2Iue4w-WBmd6TQM-9hMx2C5RZm0qSqDkayfXCZ2moCf9PMd3aw5_IyTGg1YZAvT1AZu2HZl0BAKCOFGvGGkeUwDXZ9ajV56PBVj3BWhmxu5og7L4-bgSZndsUYMr-VJxhg4sGRWjNWkEhQ9qPegztaKHhUt1e1njXYDwkh_-iyGijIjYKjAYK3DwZD7DNpDF6h-dUVZfyHD1tFs-5lIW9Z-jkBTNeuefQLTWpC7Q_4dy9BQWHW7LJdwofh2GBKqsVM3sA0Sqvx4Co-v-DXTn0oYdd4uHOAGf_hgsDku1wTY1PAhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
👤
با گلزنی در بازی دیروز مقابل صنعت نفت؛ اوستون‌اورونوف ازبکستانی باچهارده گل‌زده در کنار گئورگی‌گولسیانی به‌بهترین گلزن خارجی پرسپولیس تبدیل شد. یه گل دیگه‌بزنه به تنهایی به بهترین گلزن خارجی تاریخ سرخپوشان تبدیل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/31543" target="_blank">📅 12:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31542">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHYZg6Ww8Nkf2r7F1VOBwuAJofVPhD3MRLh0LXuA91ra3kHc58Xwwf7jjJABY4wLUyP8fix0yj7Ftp6ZXjXuhBQAamAAa5ltsosZLBV9_SuD2VchNu_lzH3DYXqJs6sw41qkzVdZyBNI3xxhoTkVu-0MLFvgPnLexCcRaRPLgaISP0tWxIidsaXIV8aiLavvPG1Xfk6kKDH6-LOkwtHQ_Ubt43UjaLxrArqG3b0ChHGmgEfphXXTrLsHBUiFdJsAQQGojAS6bcWPayMmzW9kjDY_yDi6ZmixXHWeGg0kTmBn7SWW-pVqUdXH_IGhlnjOVmqDmoprRd1HVVD_YaQhsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
واکنش فلیک وقتی تیمش 8 گل به بارسلونا زد:
‼️
واکنس فلیک وقتی تیمش 4 گل به گالا میزنه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/31542" target="_blank">📅 11:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31541">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52b689cf97.mp4?token=koVjcKdJVLvQbhpj-150EGiq5RtFkS6rHKqoL0JOpQ4lvCTRHINGW1Pq2j0OQG7T3-lxSKo3fLRdip4Pd_1ldR4U8B2n9YoMUZdDsU7RSUYlqi5crpUy0rPXQLEwl574njVpz6OIAGodQqKxC99Q4m1uBSngmvylJw9HZf9ctFmJyAwfVWPfzty_b-sJ88EPdEfalJjuHVX1sOQObGx_GiJSeQT5IXlb5fWrs6quD5FoTdI_XiA734g-3qycUZKJcr7lbODK4iuH2ITMlANJAipNgOxNp2r-tYH7V87ZNhfjfDihN9IA7024I2qylqW0WiDhQ4JsJ1EzTl0DslvmEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52b689cf97.mp4?token=koVjcKdJVLvQbhpj-150EGiq5RtFkS6rHKqoL0JOpQ4lvCTRHINGW1Pq2j0OQG7T3-lxSKo3fLRdip4Pd_1ldR4U8B2n9YoMUZdDsU7RSUYlqi5crpUy0rPXQLEwl574njVpz6OIAGodQqKxC99Q4m1uBSngmvylJw9HZf9ctFmJyAwfVWPfzty_b-sJ88EPdEfalJjuHVX1sOQObGx_GiJSeQT5IXlb5fWrs6quD5FoTdI_XiA734g-3qycUZKJcr7lbODK4iuH2ITMlANJAipNgOxNp2r-tYH7V87ZNhfjfDihN9IA7024I2qylqW0WiDhQ4JsJ1EzTl0DslvmEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌پرشیانا؛وکیل‌علیرضا بیرانوند که رابطه نزدیکی با علی‌تاجرنیا داره در تلاشه که قبل ازرفتن علیرضابیرانوند بخدمت سربازی تمام توافقات لازم رو برای پیوستن بیرو به جمع آبی‌ها انجام بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/31541" target="_blank">📅 11:03 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31540">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDh1kHJlXVmnMU_z5ReVkZqMyYkySpuuoXq0WpBC1duYK5ZSWz6vNesebmFGR_ZDtIkH9vSHFTgVuSyDlkWALu8abFSHC8b8m43MhixOlS0HJBLV0HUmVPiHTsxNi3ypdXrZ7-muGwbHJHBaaqVSiPzLyIk3byZ8d1OivyJ1iYFEeS4LRN0baJi4p7iMffJZ7p95iqkms_xi1-804DQTo6QuReca0fjIMoHkZyOxvKo8U6LSD9m6ckuTc9mAWY-Gh7maS0OxIHaI0D90ine1GEKlPPsvzOgr2pr4IkB-xfoNyLhd0VAQaBO75rRFYePL_r_7vVziJLKhhHbj3RNrAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد استثنایی‌بارسلونا درفصل‌جدید رقابت‌ها: 10 مسابقه، 10 پیروزی، 43 گل زده. شاگردان فلیک سوم آبان ماه به مصاف رئال مادرید خواهند رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/31540" target="_blank">📅 10:50 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31539">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETHaa2GVSu89goRugNh9U4yeAQdJdup5Kp53JhN-Onyi2wkIFqWsimaYMe6dax5Um3bv7WTpsKmJlnj05QY5QZ26NHKJghsCwqcbJsbxGb6OZwF6PX8At-k2R5P8iQ9vzT2XE56VfY9g2nHrYcLfIyLD5KCMaCyDhRpSfQhIRDLwoO1HPUb1ifngh9nvjxlSZ7-YKHPPmRSdvd9HF6yqJ5VNmlFM-gY-5pjYDpTNylrWTHEOLurTFKN8MYaRGClBjnsm08_JFqhFgTHVUWiPPu61GIIgw9XqD7zrMEJdYyiVkehQNiggLayc-cvV1aLnR6DfyG2yIYwAWQDxZtYtjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین تعداد گل زده دریک سال تقدیمی در تاریخ فوتبال؛ ۹۱ گل در یک سال؛ رکوردی که انگار برای شکسته نشدن درمستطیل سبز ثبت شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/31539" target="_blank">📅 10:27 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31538">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvSx1nsiE331kBLqDe5dnuQZd2cpQzZThSPxWwdkk-w30TUkp4wTcYtWm1bUjduxxu92FU1B75_JkLWJ_PoFofPmBmlSIsrRmNEYiQvcKFFQhqrE8KxKbzePoyCwa9Ze4GBr0L4G0T9CYHtWDtbDUfDNQL_sQhSRt8j2zmJB48EUsRxun0CoLZjV_jvNreEZjl_66_wtQp_1YUagXSjicT2PcEO-3cyjPjYhO46ZEH7aTZZEjHYWxIYW8vXifmknpahE5KhgoaN_y8WEHLDj84HRPFZmwp_rAumTbOWN7ptcjeZ3Ep23hq735Iwh_SwFTFE9b1h8LyMWIamYudd6ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
نتایج اسفناک منچستریونایتدِ مایکل کریک در فصل جدید: 9 بازی و تنها 2 پیروزی؛ شیاطین سرخ نیاز به یک شوک از جنس آنتونیو کونته دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/31538" target="_blank">📅 09:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31537">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxYfKrTNIC7Ohfc9SPFtxJ_vr74n_SNJuI6MK7Gs5G2gq_IgLuPcnGm0OKTktZHarBC_vjhYie8xaP8tdLHxZ14xMzH_Qdl5AB-IgX85LWi7lRw0MK97bGBAOYRNeQgunyQwHXWQamp98NoK4zOaD-tLkwrGmUdsqo4hQC2xcbq3vmtTzbKSEK_y_0hkUZ5mpm7tHp_FbE8ccfKcC5-qp0mrZ4cw6pQXmUL2KS_aPT7a04KU7_Mj6eQOozWa8iQpCSBMTupLl24QZpU7ye8y0OTJro3ftbr1Jn4jM1EE-vtmjVzjQy7YEBBC3jcDk66j6vBaxTIjWPDBwida8lkceA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
گالاتاسرایم نتونست نوار پیروزی‌های بارسا فلیک رو پاره کنههه؛ آتش بازی ابی اناری ها در خاک ترکیه با برتری چهار بر یک مقابل یاران رافائل لیائو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/31537" target="_blank">📅 09:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31536">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXzo5uDFR8kqU6wy1mKde3KOM-Ok2VxQD3-1GrHWNLwQSLV6lRPp6YavA1MgVqpwIPSVoJ7o6J8NflBi-Nv8r1fzFtWTYR2UNvEoG3nDjCJ8PQmFwm4IWdYTuNZOQuJIVneJ1PfgWkqg4BiNuFCoUYnzMkJ6AYL6tZf_PZU5KeaRil3bCFqUKhiiJ0PfZ2pviSmEn3GPsLcyWUP4LPTHz6E6Y7x7rsapBQfqdpJUX1hGuangM5hsb2I1ESyPR4sQZ5PWTbTfgAiVIDdZM_8zVrTSYdw-ELiFJN3a_388AIEJL5rcb722FF06fiG2LpmdSdls0oKuijjH4K_bLVbGaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛جدال‌معوقه‌پرسپولیسی‌ها برای صدرنشینی‌لیگ و بازگشت آقای‌خاص به شهر رم
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/31536" target="_blank">📅 08:04 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31535">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfpCI9CKbghREU5ji3rsXg1qYFA2-9OIYO07FNgZNHE-SK7JgwJHpPK_19HHO3IdgGjuR0sB3nVaxQ4JzKx2QlRx0T1V_OKu0Cj19_z3p3WTOVNSAwQVgQX180gEsfW2JdlACQc3baNghyyafOiwIK0T__Z2ctnAxgE-JpvDnQ8SM83uMx6XKvrvLCM5zdn7fQUn8lbIhA1acw9dT9OcSLefMntTtDPFY1Z5lm02eI1w7Lb4qBEVrcg3VQiZZhltkDTYdQghUO8_fuCk5sYxLe3gsyTlx7Hvj_yj-hmq_rmY0JXPGo_RkPJm9a6s-FKasWSvcqyCpPyaDA0-JwcFMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
از برد قاطعانه کاتالان‌ها در ترکیه تا توقف شاگردان کمپانی مقابل تیم نروژی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/31535" target="_blank">📅 07:59 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31534">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHUG7BLX31LxpjzjEYnKKROmFBry8MBJzmBMVaBHd7ZuPvopKpK4VgOnLqJ7_ODybjL8LMK-O9Ya13YZ-gdZcejWgKhygBslpO2VpcX99B092wyZDzXyYqOSFIdPqFxjkGz7pEMe0oFBbpJjQ85nlAvxZNaCrBjfssSXi9d2KdfD1P-3c5XEHDwBeOE5j9JZYw-bhQ_BoFavE82jqpcx1TIcOYIzZ41eR_8_-arnlqYiHc1IFW7aFDrgfhjefnF50Qz22ZE2mbJqgyG8J0u9eAAc04XsPX0oIb7kXJrrAaTAibXLSbEBzkcxFDA412Idaz7eEwqSyQB4SeE3kPuN0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پنج مدعی اصلی دریافت جایزه توپ طلا؛ امباپه بالاتر از همه؛ لامین یامال درتعقیب ستاره فرانسوی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/31534" target="_blank">📅 02:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31533">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zf4hxp2z_lc6dEXz6jvAs4Pk8nv1AhgZQJKUWiaWvneKfpGbGeTPAvxmx_qdYHfls6Qk_Z3VA7wC18RkNE-esCFF1cYg5g3F_OGhOA1xr1jqq7CzsDNLHQFN2WWCJsItF87Xx73PGKDRTAxu3n9tZAZnxNX0IZjoJvp5trZlp6cIU7yK1aRiCfkiDfDqsmytyCYP0kYg4xt7I_FNmAVoNAc1-SJ4KbMM1VZEqZxUL8ldygkukbz-sCE5v6n8vBczqDeZFkzbOolyDq_hkgmSYSBSeXdf3NpKpzsrsqR6B487XhAVij-dOu-yGWFSLokcR8nLfBFpVDxyBTHZTcjPrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ نخبگان آسیا در پایان هفته دوم رقابت‌ها؛ الهلال دوبرصفر السد رو شکست داد؛ شباب الاهلی در شب درخشش سردار الاتحاد رو در عربستان شکست داد. آبی ها با پنجره بسته در رتبه دوم. شاگردان جوادنکونام دوازدهم‌جدول‌رده‌بندی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/31533" target="_blank">📅 02:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31532">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBussiness Account</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afTx45iPeAjzCU_rufbHgR6iXR3G2hKDsFCMbsiecY5jluf6ZQs93YXZdYflW5kA7nOwVI19M-BBG_QEkVENInX903-115jPCift_qzrsxN2AntfICYGksApEXf-8tSdg7wcDYUVQpQTQIC2xjZqXAO-1S9cvR8tdxmCqiACMBZMiSAqhPjixAk2a5YTRely5fu5qDAOE1tqdmTyL-os1m_3xagb8Df9Ke6OMVOGlCKXYptSriZ5W_S7ThGTd2ikKKELJPBeUgSJwtRReI0yDVTS5KgN6RtmAN3SdSXXjmzdIoNeDg7wBya6GqZOrAOSujmhaSC83eLJ7oTHs3ixjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
انقلابی در صنعت هوش مصنوعی
🔥
🔥
‼️
تاحالا شده دلت بخواد وارد بازار ترید بشی ولی علم کافیشو نداشته باشی ؟!
💵
چاره ی کار اینجاست!
یه هوش مصنوعی اومده که خودش بازارو تحلیل میکنه و اتومات برات ترید میکنه، اونم رایگان !
❌
دیگه وقت و پولتو صرف یادگیری علم ترید نکن، ترند دنیا الان هوش مصنوعیه ازش عقب بمونی باختی!
⚠️
بیا تو این کانال نتایج رو ببین خودت:
➡️
https://t.me/+gaXi_cMYHks5MDA0</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/31532" target="_blank">📅 02:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31531">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ku6bIDmsrdzAVHzv7tlonihJFBsR-UWVkzFGvmkid6XqCB6uXLPw4rJWAC3THiEIdHG9fIhK7AV6TFQw5pjrS2cjgZZWBgUfFA479S8IX0dAiAp4QQQhSJsX7tA-BGRFsO64AYi4sCNSMZabuYra-G2eQqQdaKo029sKsA-xxk0vtY-KXscKy9yDuW5hGHWWSxxH_e4-MzQnwO7n1pBzDkzIPcO54iDnRa48KGZx_6oJI1eRJFC0lQ5xhG3uyuhAIdK8_acO5lznGJObFcjdQrB9_9jgcxt0KyHg-XvM2pig-MbVfOEwOwm7_cYXiakn4gNjHiGfS668F3OhsZze4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای امشب هفته دوم لیگ قهرمانان اروپا؛ پیروزی پرگل بارسا مقابل گالاتاسرای در خاک ترکیه و شکست تلخ شیاطین سرخ برابر اتلتیکو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/31531" target="_blank">📅 00:51 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31530">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">📊
نتایج دیدارهای امشب هفته دوم لیگ قهرمانان اروپا؛ پیروزی پرگل بارسا مقابل گالاتاسرای در خاک ترکیه و شکست تلخ شیاطین سرخ برابر اتلتیکو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/31530" target="_blank">📅 00:39 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31529">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-iW8hkz2ZTjJ_gxwzF18OAdHH8K0CecScVN86A1oAqe1vxaK30JLaJUYaHmDEq_VknluJ-r22SvKqeAb7FIH4_018_a6njsDxf_Yvzcrh1PVFtgMGU_bs_gwgoPpQcP0fJ1ptwMol2TiptI3WxqjJ2W6aBbcDmZAgJd4V27alo0qg1HCpPvWyIujJy3jCWSyn4eC52sMhokCgZUMh2sidA227EhhD4VQlam3MH2SLk9PUOGNWD0nAbfeKEgUnLIcnu5zELYk9ySi6TW_39YgCP-o6-gb69k6ccgUt8kJ8UPenHATqUXtULS_bJKRvkKcmCQhnrGVTTS0W804SJhaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌نیمه‌اول‌مسابقات‌امشب‌لیگ قهرمانان اروپا؛ شکست یک نیمه ای یونایتد و بایرن و توقف بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/31529" target="_blank">📅 00:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31528">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTvMWFvoLeDScfaGN6Xxk3atS1yxvWoPRd2fnbL36g96bW8h7j1Dmw4vcQMo63iH9wJr8wNdgvmAf14KKGLMaVLhC91GByxK6Cl9Usdr17yrJ8byUkUJ4GBZQLMI5ZbK1IYpPI6Bc_9jEWcuQtFdiLdGcVwgPT7RkZnBHhLQRy-JgWP8l2ZzN4pN4Z05n7YtbrpC_G6oMV8S61VVu-7I5G433HdxVPF9wcjPvqDHsy3Wycl_HcR23VYjzZAN9wjdht0J02JAIaJc3uKiayPm2onPznU3Vru8PDvPGVLEYxXtcKczzgK9bsZgF9eiTSxBiQRb3Z9esfnYx2xdR7IDTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌قهرمانان‌اروپا؛ شماتیک ترکیب دو تیم گالاتاسرای
🆚
بارسلونا؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/31528" target="_blank">📅 00:26 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31527">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpxiEL1Hrcnzg8YVIyo_Pob9iSvQSvo1srp1CfH5LpufgDb2ZXc633vf3bVBu8SuX6mjLkWxgBuWA7Q8yR1f3nGy9nL8XDx5yB1FZCX2Ny0DsM1R95OxpT1G79VUMY4SPiP1TrXdMTV6oCjzEafZFrH9X4I7AmCH7Q9-kC7w8m457eRBJ9G9kYbj9PhsEMLlV8C2Cwss7QTfSikK3T5Fh79vgpNGAHwRuvwnqHFxbbuhW7S0Dd4uBsPJbqoum22WO1daHPCbynU0CVipzGI84JO8aM09-ucDs2MrzAYsuCmjPaQNO90KXXfHDKxlCoM9yRt33CiQjp9R6JKUGUBv1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قول حمید مریخ ایجنت یاسر آسانی به مدیریت باشگاه استقلال: در نیم‌فصل یک ستاره خارجی دیگر در حد یاسر آسانی برای خط حمله خواهم آورد.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/31527" target="_blank">📅 00:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31526">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMeQuBXZfWVyW6Jj7VDOhS-gUF9wamoA5IF0UzQGwWxa3jH8WpHbhbww68qnf7IkJ6urApVBINx8iu0et-PKcoFUNYKnH4SII4bcVp-feirUQ8CVUXwkNJ0yk9Fy5tpu-5CJdDeG4WUrhzkhOm8FWWz-SjqDMG1e1DQt-wanhadzJHaWAlbJ1Gt5hKAUytb2buy8XbkncckZTl1UXYnEAEmlHuI1QVjiUliDg63lQwtW07rdsL8rgV1QqrAIPiRLor3DkaMlbdwgPX85jJv9Xw_KcOlCS8hH4FQlf4vPlqwMgI3tNaCDWguPqIcEAAKQce-i91csDVXZppJ3EUiW4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
دبل‌ تماشایی‌ سردار آزمون مقابل تیم الاتحاد درخاک‌عربستان روی پاس هوشمندانه رضا غندی‌پور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/31526" target="_blank">📅 23:47 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31525">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEytU-DnwQ3Y58z3DvDzP-85xvivvJU1TtOIW-iwmO03aX5J3cIUfPbAEvp9qamnF2jWkDWgGE_IxfaWITgRy6CiZZS_it5ksHwuC6PvtkCaZK0bb-UqQwLGAzgK_gRY475hnz3kjmhPFarwyIP9QBL2ACrXSalRpebb4cI4ZSYui4dmHc349WtA3U8ce4hNbVSkJJ-3R2aWF7vewHq8kJBzC-JUvZ-3ZSMnrw0GYgwibG3kisxZvQEY3lJL7H7nW1ImJUGKL5j1nr6VG6MO4YfLpDwpuKTox2OZrqv2N2IpwUolG1OV8nUElJq3Iv1BMX84eWfkMYiG3Pc4Adkd5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌قهرمانان‌اروپا؛ شماتیک ترکیب دو تیم گالاتاسرای
🆚
بارسلونا؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/31525" target="_blank">📅 23:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31524">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUq0BcLo7-la-fKogWr35YF3Gey8PUi5A1dEzWhofsk-IUncDFQr3475cSB75lcaW9VyXIF9EP694VWnWCB-irIB1tZtUAq0JLLMwa8pMQzDbLkwNIogitlevOV-vL11DEDfnpawGnFLuB2qQ44KGLP0Lp3EHr08W3xvhXtv9qxefRbHgDDz8y2scZTUG0-YiO2I_UaPC5J8j5xqTx9PUl5jtMeVuVHgXniV6rgrZkyihTKm4kuOoMLWFIh2qdv3mrYKSvY0qKAl1wx1sT9uAb0tRUuRLQvlq-28IWhx3-Wp5kLhxTpRXuTwWgEklGd0BB3Zden8kLUtox2dTnxlTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی پرسپولیس در بازی فردا با خیبر خرم آباد؛ تیوی بیفوما دچارسرماخوردگی شده و اگه به بازی نرسه به‌احتمال‌زیاد اورونوف جایگزین او در ترکیب‌اصلی‌سرخ‌هاخواهدشد. کنعانی زادگان و ایری نیز دیگر غایبان پرسپولیس در این بازی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/31524" target="_blank">📅 23:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31523">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e058158de7.mp4?token=Y2ffKpiUEeoR6r9dG4EWevozD2Vf-TfcrJAmAFpEZCpPR8UbNlG_PyWLBDKAj2BUIo54z37xWHqF6iBu93aNx-ozXY19ZLm6rejNhVWFDX_yP0T2qUAvLHcG6Lpa_O5trRL7jVdt9eICs6o6lIo_z0nntroFZehrzu0pm8_XJ99gN24Y7aQAH5nqnRZ9VnI4epPlBok0U6uOXvhConQOWf-oBt1jlJ4mbano8-djvKwjPMlfQ2rsyXkKoo6vufLo7tOJWF07Rx1zBdLMwuva70vB-9ryEv_Oc14kNbuhQEIvxTLch1Q3yv9lVWnOvZ_Lxfx0zbjxsXP9BhkujSvSpCUG8URv63LemDoXRSm8DRQR3WTTh6iucvSDUhum-YdxsK65LmpIlhf7VDkQIF8D73XLgcA_HToRsmKxNTt7oCZcjy2zEy2_Ho-SJU1wk7Z4_c_TkkeLDoF_2c9zR6TJGyMMHcN98dmQJZUsle5N5DG4gJQT6LrxPHywI9_Vo-fEKocyRQXwX4Y4l51dj0HHnYGCZJ8pUM4ToQOTH3bE6V71L48FEcH4mbHj4eQZHrj96eUG2thN0qO7n_-jQOtCef1-N9TMwmEIED1mc1U-6uSlFAspA0vh66kRTAXLs80T4NqQqXVfM9N8x2z_WckLkoNNVz3zzIb2Tn3wCE-j2Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e058158de7.mp4?token=Y2ffKpiUEeoR6r9dG4EWevozD2Vf-TfcrJAmAFpEZCpPR8UbNlG_PyWLBDKAj2BUIo54z37xWHqF6iBu93aNx-ozXY19ZLm6rejNhVWFDX_yP0T2qUAvLHcG6Lpa_O5trRL7jVdt9eICs6o6lIo_z0nntroFZehrzu0pm8_XJ99gN24Y7aQAH5nqnRZ9VnI4epPlBok0U6uOXvhConQOWf-oBt1jlJ4mbano8-djvKwjPMlfQ2rsyXkKoo6vufLo7tOJWF07Rx1zBdLMwuva70vB-9ryEv_Oc14kNbuhQEIvxTLch1Q3yv9lVWnOvZ_Lxfx0zbjxsXP9BhkujSvSpCUG8URv63LemDoXRSm8DRQR3WTTh6iucvSDUhum-YdxsK65LmpIlhf7VDkQIF8D73XLgcA_HToRsmKxNTt7oCZcjy2zEy2_Ho-SJU1wk7Z4_c_TkkeLDoF_2c9zR6TJGyMMHcN98dmQJZUsle5N5DG4gJQT6LrxPHywI9_Vo-fEKocyRQXwX4Y4l51dj0HHnYGCZJ8pUM4ToQOTH3bE6V71L48FEcH4mbHj4eQZHrj96eUG2thN0qO7n_-jQOtCef1-N9TMwmEIED1mc1U-6uSlFAspA0vh66kRTAXLs80T4NqQqXVfM9N8x2z_WckLkoNNVz3zzIb2Tn3wCE-j2Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شباهت‌برگ‌ریزون‌گل‌تماشایی یاسر آسانی در بازی امشب استقلال‌به‌الغرافه به‌سوپرگل‌خاطره انگیز آرین روبن در دوران حضورش در باشگاه بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/31523" target="_blank">📅 22:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31522">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcBArrInw0KpSAg2I-ZgA9PeHAq5TAswD56B12PtK-eJLCQUbzEbRNXXhkoJs6UWfsh950UI4xhfgF9Lfc3yktl5aQPZPdtQdq028ZxzkVg0xSsZqDXZqcYkDw6lCUB0b_5anZk5iQjCZ95ry3bqoEecKdZntk3jxHeqJ_yUvc7NG9aVfzzlaGqVZnfAURpof0JJQhQwb85Q1KzEl3d0JXfgtn7-Hu6Sei0-135pA1U-X-Dva38FSJenLE6JVtZPr238ROhukHiOpnCQBs9DPpoRAjwuBggORyRc3VZnkIp5Jzna7IW_sifhHKbeHYEZIFmKCAQZy0L4qbu85_CagA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دانیال ایری مدافع جوان تیم پرسپولیس که چند هفته به دلیل مصدومیت دور از میادین بود در فاصله 24 ساعت تا دیدار باخیبرخرم‌آباد به تمرینات گروهی سرخپوشان بازگشت اما به احتمال بسیارزیاد در بازی فردا در ترکیب فیکس حضور نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/31522" target="_blank">📅 22:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31521">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d9d3f2c25.mp4?token=MJHghylW37uDj2kntlgxmdRqC79dIOqkG5peYq2p-x6Vgj_eY_6uUmnj9QIvTOxDaNS2HgVo2pTCnhyH7UgjwhkxDhMVngCLGkjsbzMxENUSeddEnqSs0MDiheBxC1LLKFGA730ium9ySxKWnXcnbZtz0rBkIYNU80vQo0vb-4cXG3ZEInBIyf0OqlZQMWtcJOXsRIvIdgx51jYJjveVGxPh9qQEtXhxukB5pAu_9y8XQZq9r1NIWdZKm59K9vLwCFPrmvzwc5eUHh9Ga8VunrO_88pKDl-sQqOK1otTgzymT2CgE2eHXiMIcUSoSrJvcbZUxvn4u32a3OsTzivrXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d9d3f2c25.mp4?token=MJHghylW37uDj2kntlgxmdRqC79dIOqkG5peYq2p-x6Vgj_eY_6uUmnj9QIvTOxDaNS2HgVo2pTCnhyH7UgjwhkxDhMVngCLGkjsbzMxENUSeddEnqSs0MDiheBxC1LLKFGA730ium9ySxKWnXcnbZtz0rBkIYNU80vQo0vb-4cXG3ZEInBIyf0OqlZQMWtcJOXsRIvIdgx51jYJjveVGxPh9qQEtXhxukB5pAu_9y8XQZq9r1NIWdZKm59K9vLwCFPrmvzwc5eUHh9Ga8VunrO_88pKDl-sQqOK1otTgzymT2CgE2eHXiMIcUSoSrJvcbZUxvn4u32a3OsTzivrXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گلزنی‌سردارآزمون ستاره‌ایرانی شباب الاهلی دربازی امشب‌مقابل الاتحادعربستان در لیگ نخبگان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/31521" target="_blank">📅 22:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31520">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/559d04596c.mp4?token=i9_s0eAY1emu1coqlCCLNY8j0zvT6ZaEuyFCUfiQ-D8fYO-avEdkevVH5sVeCMki_5NIsAwV-JAlveEux-6fSPJ6ZyLwuQVz3A0mRbZORkE-igPMoOXykbvsBjVPSqeHIaLr7KDSne3v3eGujkcgHHM3HHnghIDarhSkBUgyO9N7btXiLsPX0pNwfP0OQfm37zzbGz4nRSAUHGxw7GoLd1Z-emt1TKR6iGBQeHDgrQfoi5Wmx7_hh_1lPRx1VV03oe9FZd8ImB2g6LwkGuSWEMs0yVe-VKTlkd9fQ5TlQ7YDEEDbevV1iQ5ttd1t8n9Qlgq1Njf_bV9qmVHKV0JrUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/559d04596c.mp4?token=i9_s0eAY1emu1coqlCCLNY8j0zvT6ZaEuyFCUfiQ-D8fYO-avEdkevVH5sVeCMki_5NIsAwV-JAlveEux-6fSPJ6ZyLwuQVz3A0mRbZORkE-igPMoOXykbvsBjVPSqeHIaLr7KDSne3v3eGujkcgHHM3HHnghIDarhSkBUgyO9N7btXiLsPX0pNwfP0OQfm37zzbGz4nRSAUHGxw7GoLd1Z-emt1TKR6iGBQeHDgrQfoi5Wmx7_hh_1lPRx1VV03oe9FZd8ImB2g6LwkGuSWEMs0yVe-VKTlkd9fQ5TlQ7YDEEDbevV1iQ5ttd1t8n9Qlgq1Njf_bV9qmVHKV0JrUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتایج و جدول لیگ نخبگان آسیا در پایان دیدارهای امشب؛ دو بازی مونده که السد فردا به مصاف الهلال میره و الاتحاد نیز از شباب الاهلی و یاران سردار و سعیدعزت‌میزبانی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/31520" target="_blank">📅 22:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31519">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UstCZbBGRJ8okgGJokyesX0JT34q6tacF_9jzEJnkTf8bqLedlejHKjG8bN48ic6tdVqC2WBtqYAgnYpOkyAM8Yp52cHwzuVkcVLNbSx00dVynd0tq6JLqotlvaatqMt7f5qKTdChCc-DPvCHxPZAlgJjG-h_9MKsSWA0B7d-Ju2KvPpOFgxHkFjafowqpw8mTb3Gu4_NN3sw0SOF-_qYUkuVbT-jG2WIot7p8kaRk49Ema7dhTEe86pc7ObEjkN4Z78fU1-Od2Z4oSdC_yXKrIoyERWS7C4hH-VbsXlJFVQVXswwP-dPQZWNtPI1beETXmuU_L9Md4CVaFemXzopw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تایید شد؛ با اعلام کمیته انضباطی؛ خداداد عزیزی سرپرست‌تیم تراکتور به‌دلیل فحاشی به امید عالیشاه چهار ماه از همراهی پروشورها محروم شد. عالیشاه هم چهار مسابقه گل گهری‌ها محروم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/31519" target="_blank">📅 21:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31516">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T5I7hLi0eVSJ4XQnJvYBjjYoBG1WIJkvhQzaEDMaS-RskLvk4a8B4YovrGMr7NEI3Dx63aIsbqLs68pXe0k32Oqp_AW6MD-eyV3gp6apg5wn7DRsBBRid2aZMs8BDB0YXCKcZHWqNhX05WyJpOhB1uCZi0iorMAaiNWRtNdZiIZa3XwqGVjXUTf1kK6qcC-LjO-NUSjQ3JonTs_Xvj4O1w0N5tJm0uviX1EZUhC8dERdhz1YFbkARdK6Y8UJxlCCXsV8TiNwFCOO4XQpXRrHyW0w34us2MloYiXIEEuwXtUep9JJxtW6jBm995RDy0IeMIsjKNl7cNcJbn8ur1SXRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uOsVHOfl2m-yDqRhJsNNAwZPciDKm-AvmowWWl-OAslA5hConYp9n-eb5vB96xAwdZzKEs4aTN02nkpMpohcGtimFTMdORI4xZ_EbzdMMqg8PilfkelrwtTHg2Nq89hGpguZmPbBQIcUHNlbnPv0oR5upaT9ExVfXLFZiO-1jTlc32mFoLR2uCouRQY1sq0ZLEWZ7BXwBIB9STFl4uESge_ZJ1hdgi4XIdjw0kzrJVbmKXWOLYR6XatbYr7B2_IvwQhKMTgroMgV6tlCrEwWLOcorEnsKJsfwQYM39UO4W-1utXbA-lx6N6sltu1AVlYAb0DsXGwTwP0Q9dP6uT1QA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌قهرمانان‌اروپا
؛ شماتیک ترکیب دو تیم گالاتاسرای
🆚
بارسلونا؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/31516" target="_blank">📅 21:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31514">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nulGodsZPrJnF3IeBHcVjzb0NpHMIGTWUdil3U5i0aO6JhztBSYPEYrN7hYaHY9yU4geVq3gd1ImSb9M1wiDkXPt4GzxEkrLOXTpWSn9QEgkJRSGNVOFhc0gZreo-x0yqy5ZIcJDY9nlLzcyHePQ7-uU2sAo9mGjaZ5B6vAaSfGkm7oJYynl7z0w1buB1MzSIapfr2YecR3FHeQ1KYpWTTgHnEevinfmWUvcu9aYj9eqvZNPDYJ1DBMtwNvZn79ECyUSgp-3mLKV7j943fU-EDb-1J65nzNmgEPrzO8Q3x3VPslXCjiqAlx0H0eY5SukIDL0VPpnPV7owkk4Q83ZQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aIsbIRU-31FRCHeLqF9oBDZJ9ght-4Etw1IfmL_cxjDL2SxL64NsmCIdMZNqws1_X7_qMXmkCCWagplJ8iPwFAaMO9F9eMPfdUjvJsa_vvOUL7hePW5a5Kq7f704y3GMOVuJxBGfGKNL-4_gqj8_o4Vw-9KIvEDUi5bRbgDM2kKmU6Gi6tkF4ccHfoMGGKMMyD7ZMsH35OCrO3G1RL-N4HVhUvLGyjuypWbhU3P1-QubJTWRC5M-GKLVRu3eYgAtjwxmxvj6ssEGlSfOPz0zk1SirD6Lu9EKZEJXW_TvV1FOA-3hIwpx5OWGgh_J-rNvpxkMqWgkoH5ltQOBwR0fvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
کاکا اسطوره برزیلی باشگاه آث میلان: وقتی همسر سابقم گفت‌که‌میخواد از من جداشه و مجردی زندگی کنه من همه تلاشمو کردم که اون بمونه ولی دیگه لحظه ای فرا رسید که اون گفت: نمیخوام.
‼️
اون روز به درسی از زندگی رسیدم که میخوام به تمامی مردای‌جهان بگم: برای موندن…</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/31514" target="_blank">📅 21:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31513">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y88CYJUn2yrJZv_2bGW-qNFjdlvgkywhVqrmNeTXHnHyRqRLJaea0wzd83J07X_8uFNIOxp9ozCW74VbKWA7TgNd6Zl87JY6WjscTfQD8s6LFAI6sb4SGAn6EdN7ysAulFAKDeZhATbJLwiom3lM8EVKfxtCppWfh4jmANtNH_EIDsAdmaB3gOUAEk9AWSComJLzf6OqNCAt9YEVn3x0mqFSp_DemVsIPHiZEdiXoC1JrpK-tbTn8rGj8B94hJBpHDcunnH9GXV10LAI6KNphXfmK_QdKHOoZg-yyrooPmsByhF9eSburawhRIVraAAlW55AghWLyh4LdKkcn1Lvig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🟢
مهدی رجب ‌زاده نیومده اولین شکست فصل پیروز قربانی رورقم‌زد؛ محمدخلیفه هرتوپی اومد رو خورد؛ درخشش فوق العاده یادگاری رستمی که پایه گذار هر دو گل فجرسپاسی به آلومینیوم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/31513" target="_blank">📅 21:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31512">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00694d1532.mp4?token=FtNeVTdwV5PTHNlRZJXpaJimxCCa4DGXk5mPUPduK5_TFJwx0gYRZXqSIsl2qQvpw62MicsdHUdWuHOguMwKhFq5rG5gfGFztgSJmA-eYACWwRKUGhxlrrpZWV-N4h6dFM6juOwbwLavdiUjSTPVHCcpPc9YNeG4k85jm9zJkNCnLzx1vYKsYhlZlzfiwXGplYLdaKu9cTTt2WD2cMEV6Uc77vo5C9f48WS6mvKwggXbzzI2k53ysKo9s9Rwn59B5cjRD_YC9rNElxHvWLGpAYOdZV7QWlszlmBaSLqiz8xIHHR7mZP4iuuevgclK0u75pftgG9sryUtPj5rI9iNqjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00694d1532.mp4?token=FtNeVTdwV5PTHNlRZJXpaJimxCCa4DGXk5mPUPduK5_TFJwx0gYRZXqSIsl2qQvpw62MicsdHUdWuHOguMwKhFq5rG5gfGFztgSJmA-eYACWwRKUGhxlrrpZWV-N4h6dFM6juOwbwLavdiUjSTPVHCcpPc9YNeG4k85jm9zJkNCnLzx1vYKsYhlZlzfiwXGplYLdaKu9cTTt2WD2cMEV6Uc77vo5C9f48WS6mvKwggXbzzI2k53ysKo9s9Rwn59B5cjRD_YC9rNElxHvWLGpAYOdZV7QWlszlmBaSLqiz8xIHHR7mZP4iuuevgclK0u75pftgG9sryUtPj5rI9iNqjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌امیرقلعه‌نویی‌علیه عادل:
خودشون برنامه‌ دارند و مجوز گرفتن‌ از اسرائیل مجوز گرفتن یا جمهوری اسلامی؟ اسپانسراتونم که مال جمهوری اسلامیه. تا جایی که تونستی تیم ملی رو زدی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/31512" target="_blank">📅 20:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31511">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqAc9VKL8gwI8cnmgTCFV7GEi94D036kVFrv6QNd5Wxlw8gPy2QWsRG2vFXKjJkDN4EIrB9uHi84jYnmna3GpLqGLA9vJBBVCRSEqP3ra0TflxW3deW8S4R83hf2CHoNOUWAm0xF36Sea692lEaiWU3e6hLR2iGBnVYUENMOYJOkbVzajplSVkHPr_ipFfcNncuut60RXCtKNbKqYRh4xjigV7l58eSwvO-sb5fpTixnGcR6gXBiLQ0yfBYLleKZMEYSu85vOboyU-19ErMUnxOTJaKi0aknGNvPmmL9fwDNuOHWVwYSODSRpPUaM0Dz2JPJcHByvcVtqE90oHfbKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درصورتیکه سازمان نظام وظیفه پاسخ مثبت بدهد؛ علیرضا بیرانوند دروازه‌بان 34 ساله تیم ملی با عقد قراردادی تا پایان خدمت سربازی به تیم لیگ یکی نیرو زمینی تهران خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/31511" target="_blank">📅 20:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31510">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c7f86dd8d.mp4?token=hke_NunnOT33YxVLs_jLz0xEV8sjOn4QQckZ749qKhfuUAS4HYooYOZCbqNc1Dvam_AeLVQwCBjOcRY8eoWQSVpkubySDAtEDZBMvVh9shy8SOjXHKS851kZHWx_v3cNAiHDBUiFSVIMAt1veiqx-67V8FSglwQTLOCVMVQEjyQF39vclX9Lnq73-VMFzQwhy2bmZRtlMhaSBmPc7GexOmcW_jdjLUSv2G2eM9E76elR7aMLYx_-rEvU89y8gtV8aKVRQ_3fnOteRMs7HKKZDq59qW2D28cLUmeUTgqj9_ES4hpyfBQUNd894JkAEglcgP-tX6vLqJpH3V0UEu_Ojw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c7f86dd8d.mp4?token=hke_NunnOT33YxVLs_jLz0xEV8sjOn4QQckZ749qKhfuUAS4HYooYOZCbqNc1Dvam_AeLVQwCBjOcRY8eoWQSVpkubySDAtEDZBMvVh9shy8SOjXHKS851kZHWx_v3cNAiHDBUiFSVIMAt1veiqx-67V8FSglwQTLOCVMVQEjyQF39vclX9Lnq73-VMFzQwhy2bmZRtlMhaSBmPc7GexOmcW_jdjLUSv2G2eM9E76elR7aMLYx_-rEvU89y8gtV8aKVRQ_3fnOteRMs7HKKZDq59qW2D28cLUmeUTgqj9_ES4hpyfBQUNd894JkAEglcgP-tX6vLqJpH3V0UEu_Ojw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری‌شبکه‌رسمی‌باشگاه گالاتاسرای ترکیه هستند که گفته‌امشب گالا نوارپیروزی‌های این فصل بارسلوناِ هانسی فلیک رو پاره خواهد کرد و پیروز خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/31510" target="_blank">📅 20:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31509">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jC0azQemvDevqYFuGzO6yy5ptlSOCL1KTBVBFEj-YGMpXaV_sV7Z3jgN4iHoN7xlkCeih4sVUGr9aSNYDrgJ_kTyl6HbY_qN8azdR-iz0UnMIxBB2Om67cI35UsYCGittw9gPoOCjiO355q-GW_zJRLimUaHFlH1_OcaUwyR0GAWW9n-JMTVEuk2buMTDJA0CcYrmOcvCBvYlqFS6IXewczc48ojBUBbki7RiehmOf3NXjLdYgYu8QQpS86I9i0TJOprvJ5T6NzlRERQMKt8GCPKuJwqoQZQ3NMSs3676vuU5d3w6IiXgbVxGf9RqfKo0STRaccBD_KxPdWPToAFRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از نگاه بیشتر بنگاه‌های شرط‌بندی؛ لامین یامال فوق‌ستاره‌اسپانیایی بارسلونا بالاتر از هری کین و لئو مسی بیشترین شانس گرفتن توپ طلا رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/31509" target="_blank">📅 19:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31508">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🟡
🟢
مهدی رجب ‌زاده نیومده اولین شکست فصل پیروز قربانی رورقم‌زد؛ محمدخلیفه هرتوپی اومد رو خورد؛ درخشش فوق العاده یادگاری رستمی که پایه گذار هر دو گل فجرسپاسی به آلومینیوم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/31508" target="_blank">📅 19:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31507">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">📊
جدول‌ آنلاین‌لیگ‌برتر درپایان دیدار معوقه دوتیم سپاهان
🆚
ذوب؛ فردا در صورت پیروزی پرسپولیس مقابل خیبر خرم‌آباد؛ سرخ‌ها صدرنشین خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/31507" target="_blank">📅 19:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31506">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVdtBRAqDie2YJuwHDZ4IOzZkha8UouHXIc_Scpzo3cohsf6a_T4aoSk6GN2KBQhdVBrG_-RYX7i0rNCxhoV4hYkMmFO_x2kXJueWRE3rb59KZ6Dm9tncGVPzkTEspSaeKq2bCa9k-sLTbfvBg4X0gE9w75KdDHBAbCoGeebDBrIS23sj6_ZjJ68qCmgcrOn_Ut7xR0pjuMpcuAr6pLgEQuLjal_OhEvw0i-IdK60vx8Efk1v-m4wA3dWrggjjfXs8NOLMZ1uJKbd51K_HRkUrMbK1LyRKzvg4q8p-7fB2vSnd5ogGwrI1PJjuyEQGXoBiwLaFdTurIM_PYEcFNm7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ یاسر آسانی با گلزنی به الغرافه به آمار ۱۱ گل زده در ۱۲ بازی لیگ نخبگان رسید. او حالا بالاتر ازفیرمینو ۱۰ گله و به تنهایی دررده‌سوم بهترین گلزنان‌لیگ‌نخبگان‌قرار داره. ریاض‌محرز با ۱۳ و سالم الدوساری با ۱۲ گل زده بالاتر از آسانی قرار دارند.
⚪️
…</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/31506" target="_blank">📅 18:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31505">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1CLCr9lFbucsoHkATMTnJ2oS4k9O6J7-oEZqpP5rYEdr_yBpGeU7HI4mt6yqexTsD7k2Mj7ruD6GQ8wRb6Z2N-38KK1vO6QDqcAavOzGa_uwtETqUNIO-4tFbWKb9_862vG7BXUR0Q5iwn5ePqsgtGMGxOx5YfUllnyVUX4-MFz1T3tDPrf3tviUpjHAi8eTzYbUUFxareP0kIhpONnWBC00KCBm2wxCKNA8tyWFMUsMBzNLAptZ81DR9Nm1Yk3QoGUo_FYDRWRQivyHDGTGxaGwbuR4_3JX_2MtlGuPNxiEQXzcOxRhy3qSOH--QLQJnoYhj-uISM2POekvcgU8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در شب برد دو بر یک سپاهان مقابل ذوب آهن در شهرآورد اصفهان؛ سیدحسین‌حسینی بازهم نتوانست برای طلایی‌پوشان‌ موفق به کلین‌شیت شود‌. سپاهانِ محرم نوید کیا شیرین با این پیروزی شانزده امتیازی شد و در رتبه چهارم جدول رده بندی قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/31505" target="_blank">📅 18:19 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31504">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🟢
🟡
گل‌اول‌ودوم سپاهان به ذوب آهن در نیمه اول دیدار امروز دوتیم‌توسط مهدی لطفی و کاوه رضایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/31504" target="_blank">📅 18:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31502">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dACtiJ4SoJajTUSjITRTvxGAppYAKXBSlQhgyc4NBU2vhAv47axI1TJckqS8Y7HycgRWDocTSFybfQw_N8d8gcQ8NgGlsoFIACr0HkJ9xE5RiR2f7TT7VH0CgdRXEyugRoU7Y1A8Az996uc1kaCr8DrcuflbmmsIzlEhc5pObQS1QPP7FdLQHxKsQYYxVJHbWXO8NeHNspPDJlW5JZoHkTqikQ7V836AW8iPPK3M4uqRZCV7Injp1fzlj1wQD2cMHsr6OCJ5uaq8Secnz1EGooWjwKtOp_wPz_U-VJGaxSiCvYSqC39oRrqcJoIbFBpywYDRnVSc-vmTxu-kGb3-Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مجری‌شبکه‌رسمی‌باشگاه گالاتاسرای ترکیه هستند که گفته‌امشب گالا نوارپیروزی‌های این فصل بارسلوناِ هانسی فلیک رو پاره خواهد کرد و پیروز خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/31502" target="_blank">📅 17:47 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31501">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Js9RA66loBXmr9vS0EPiP0Aj8sRMDYj4N5Lpr3YEp27jRJYPa7Eodd6W_7HUqYriaer0QZ6udlZ9S1U6R2WKFOeqze3twbpcBHXlear1DcvUVnbPAR3LcWybQFLoJ2ZPIgLxpIer0-bf2IgMnQSUEB1TiztR5HPvUgouZ8M8WL2xuwbQAThHOhRJQxBs2DJhKBeU-Xb0I7vZShjg3cIop_SEJYc1GOgByrN-xZtcHF0eDVCk-rfySwj-zQyvDpXQoInkYYvjBtahorfQ0UzNG4Y0mUFpne4mZj5l4Yi9KlTcjIhxItIiZ5K5y47XgZP_QHWrGBzFtqL6yoExmOJKCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عملکرد استقلالِ سهراب بختیاری زاده مقابل سه‌تیم‌مطرح قطری: 3 مسابقه، 3 پیروزی، 7 گل زده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/31501" target="_blank">📅 17:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31500">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6451b4b3f5.mp4?token=a1nPBfy9_Sm_tNVrqhlghcDj3CKMh4UynUwFuuftKGtQlnR9C43ewRvFbOS2eeRnnRRiSGfX1qI_tU_OWIOvhRaJW9lggrndBN7I61jk5ghST390QciT35r8VhAnaGvMGBNch_eb22Wzwus3fHWTdDRz-YoOzArlnaD-a00y5RklBN8KW1nAbt0OF44xeLqILSEOAaD0YUQXQo4HtjsVTgGDuvjhDSIFlqWdO3p-Z5iWVRl8OVG_Bt_jty4Kn_PZzordOjaEZhkOOQ2H-3FYvZvZb-jX4E7Dco3EiNaRub3nR5BtLJIjUNKBSgBfav46c55sDYN4q05vr4-9iZy-0S65EPMTtAH5eRqmK5ZH5cEhKNRs7XH4v2iCv-F2jAcp99rqnDPXZX40oh0QTS5L0nJd0tQH-Xrz_6R8ruCg1FhqPT9tFXE9VJALxvjC8nmrc-waVM2I6E070Z6UBgCOD5ZudwYGkN5zDPJws1BWLrSwG6R4Ig5Z4OshmiV6DswTkoAAd0rfbW7_9yRPOPZxAa5thihW8ThnCl0i7W8y9QYoQxBOqZAQ4kP7guTUjzQq3n4EisB5hQSA58q3SX_FtzO6sgTFkewQKBB6Ha-iuOGomYoeLFEnBq-DRSeT7OaCojimmGrC68pHIYOE_CThxuhUFd8B-3OS5S3Kwm_DEgc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6451b4b3f5.mp4?token=a1nPBfy9_Sm_tNVrqhlghcDj3CKMh4UynUwFuuftKGtQlnR9C43ewRvFbOS2eeRnnRRiSGfX1qI_tU_OWIOvhRaJW9lggrndBN7I61jk5ghST390QciT35r8VhAnaGvMGBNch_eb22Wzwus3fHWTdDRz-YoOzArlnaD-a00y5RklBN8KW1nAbt0OF44xeLqILSEOAaD0YUQXQo4HtjsVTgGDuvjhDSIFlqWdO3p-Z5iWVRl8OVG_Bt_jty4Kn_PZzordOjaEZhkOOQ2H-3FYvZvZb-jX4E7Dco3EiNaRub3nR5BtLJIjUNKBSgBfav46c55sDYN4q05vr4-9iZy-0S65EPMTtAH5eRqmK5ZH5cEhKNRs7XH4v2iCv-F2jAcp99rqnDPXZX40oh0QTS5L0nJd0tQH-Xrz_6R8ruCg1FhqPT9tFXE9VJALxvjC8nmrc-waVM2I6E070Z6UBgCOD5ZudwYGkN5zDPJws1BWLrSwG6R4Ig5Z4OshmiV6DswTkoAAd0rfbW7_9yRPOPZxAa5thihW8ThnCl0i7W8y9QYoQxBOqZAQ4kP7guTUjzQq3n4EisB5hQSA58q3SX_FtzO6sgTFkewQKBB6Ha-iuOGomYoeLFEnBq-DRSeT7OaCojimmGrC68pHIYOE_CThxuhUFd8B-3OS5S3Kwm_DEgc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
عملکرد ستاره‌ایرانی جوهور دارالتعظیم؛ شهاب زاهدی از ابتدای فصل تاکنون در پنج بازی سوپر لیگ هفت گل و در دو حضور تعویضی در جام حذفی نیز سه گل زده تا با 10 گل بهترین گلزن این تیم باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/31500" target="_blank">📅 17:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31499">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Le7Jmthsb85_dHleITzRTbnbC5ZHcDyGNjtyN2Md0vP450Jg4qeRkcVvPmiNp7q_eYqkauLItTo8xd4bwT-hF104e98Q6bPvj_BIbaYwtpO1bNBFfwcGNXQ8rmmkTZiohpWicfiJseUB3lXFKDr4KnKuSkEBysIMDzLhIahErIoaRJaPNiVvx-ZEZcuo8dgeA1eDQaMmDJEuMo-aMrBYGI4SnkwTRZ9d0KEyVH4uIQHtPiB6MDCRSseUMDxeB7Ae8Atv2RFM4x-j8WN-crETIuCLR-KX_I0AdNIz6c5mWWdCtIo5s2fd0pz6HIOR1nINtpdVaE_PstaCw9KPGuJopA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
شماتیک‌ترکیب‌بارسلونا دربازی سال 2022 با گالاتاسرای ترکیه در لیگ قهرمانان اروپا که آبی اناری ها موفق شدند اون مسابقه رو دو بر یک ببرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/31499" target="_blank">📅 17:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31498">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بانک تحصیلات ،بانک  مشاوره اخذ مدارک دانشگاهی. واحدهای معتبر ایران. کارشناسی، کارشناسی ارشد، دکترا.‌ پزشکی عمومی،داروسازی،دندانپزشکی
پیراپزشکی. با استعلام.
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
Telegram :
👇
👇
👇
👇
@banketahsilat
⬇️
⬇️
⬇️
⬇️
⬇️
جهت ارتباط با ادمین
@tahsilat_azad
@tahsilat_azad</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/31498" target="_blank">📅 17:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31497">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bh-yaDDABueNcYHFxWLdTqqPT5IuC6FC9sCNbcxu64ti_UNFlD_ieQpdk-36WKHEC92MRToSgY271hbUOhj0FwA585kCPqjRZhL1RyySi5k4bbgZI2Ir_MlmtCUfqKHGxUr_i8vdldY6zLkyELZvI3Aq2Xd_dIU00mwy3LzL2D933wTlZNm21osto_njLeMIqTCLWxS8SNGygEo3OIpRhLMx9tKkPs8ejzrIRsg49FIdEVYulvk_iBh6ZnpG7RtBk9l86YbWFs0nFfliX6V1raAP_mf2tVn-itA3FmcmlglB76a6yqubapTNjHsYCDX-1JT4duMzOmGOlwNOyjUiaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیدارفرداپرسپولیس
🆚
خیبر؛
ششمین تقابل دو تیم‌است. در ۵ دیدار قبلی خیبر سه برد و پرسپولیس دو پیروزی کسب‌کرده.تقابل‌های پرسپولیس و خیبر ۱۳ گل داشته که سهم پرسپولیس شش گل و خیبر هفت گل بثمر رسانده. اسماعیل بابایی، ایگور سرگیف، علی علیپور،اورونوف و عیسی‌مرادی گلزنان تقابل‌های این دو تیم بودند که در دیدار فردا هم حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/31497" target="_blank">📅 16:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31496">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0e5fab635.mp4?token=A-FouDG2vs6XkpYAIcwEmSry4SmyAaWdZ9V1MhvFNySNcI53r2Y_mGsBhxf8Hf2K9oXHE37c0YW3pt1r7q182W-YysP3hsF0hLD2lpA8RWSXXKKgc9SBEsgtZwdOJs61Jfs-IevlU8SIt82zfFxx1Wgz_bixfNJ4o2rxzp9UcXx7GYbQqRIl0tP96HwXzassBGrpIKwzhgTpfc4hKeJKk7bcKqUcnNTQbEU6ZYeHaSM8VQh9ydBZ6OMNH4kbdKP1cSU5PtU0Dh0AdolO3ARqTPRdYUU2TEurgZkWSEjhpe2DN5GTilaUpcO78qp4NZ94VI-Sw4jSuT67GRoYfiYuaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0e5fab635.mp4?token=A-FouDG2vs6XkpYAIcwEmSry4SmyAaWdZ9V1MhvFNySNcI53r2Y_mGsBhxf8Hf2K9oXHE37c0YW3pt1r7q182W-YysP3hsF0hLD2lpA8RWSXXKKgc9SBEsgtZwdOJs61Jfs-IevlU8SIt82zfFxx1Wgz_bixfNJ4o2rxzp9UcXx7GYbQqRIl0tP96HwXzassBGrpIKwzhgTpfc4hKeJKk7bcKqUcnNTQbEU6ZYeHaSM8VQh9ydBZ6OMNH4kbdKP1cSU5PtU0Dh0AdolO3ARqTPRdYUU2TEurgZkWSEjhpe2DN5GTilaUpcO78qp4NZ94VI-Sw4jSuT67GRoYfiYuaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
معوقه هفته هفتم لیگ برتر؛ ترکیب سپاهان برای دیدار مقابل ذوب اهن؛ ساعت 16 از شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/31496" target="_blank">📅 16:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31495">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drCh2JoAdrUp-Yqv4d6aDgj97JQzJHbFWEpJGTIw9fJDXRhWFJU5QuXu9qC6CO641vpIMXr_kPtQuFMsfJRHpEImXowBVuufLZDkADJi-iWbH2lePuxAsOv7ukQHHJRnRweyh2Op_NBuiH4fG3d7kEMs1A9DxZB4q9PhZhOfb6loo7FgubgeCSW2kwIeUUJAUpcA1b9g5m2xAEFwj0WZACbcVIUV0FD_iaDdlbj4frCTbZW_ACNzEf1MUtpMaIWY3XrdW_LQ2DALMGsBm5ohOu0xbfezs8tg11_Y10A9yyPiSfTeAhOwP5nlhDTFnsjgsVRkMX1oWPfGFwwENFAA3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ یاسین جرجانی مدافع‌جوان فصل قبل آلومینیوم با قرار دادی سه ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/31495" target="_blank">📅 15:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31494">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldXSNlmh2w0YLPKqN7LBSLXExnvmSJtCgEbvk4oYWCLV1l2NwKetrehNHnMGlfe92fxWt9qgGL6UHc-FoUdjVMWzUkENHzO3UpcRb0M4xhRIsNiebhaVnK-QGQpvjicnyqDuD-sU6vex-KC3u-iSuuFWsQn2lObTIdqTGBjEA2_EMvikuRJDNrL97FHKvB8iax-o6ZL8rRsyT2n8GFnR7vdjiIn7Rx7E9LYLtIsEn09zeBmvuQdtzVxAe_ZMAV2ByzQSLQ8FioP7DTVPurcbuugJIk2nUWvDkEblNRgx0-4YcjzeoMUl5mrBabpo6RuswQdBfcdIr0kI5tVZdKgq-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
دانیال ایری و حسین کنعانی‌زادگان دو مدافع میانی پرسپولیس به دلیل مصدومیت دیدار روز چهار شنبه مقابل تیم خیبر خرم آباد رو نیز از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/31494" target="_blank">📅 15:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31493">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGgEryRdrtRwKT_qb6qCq3jftwJcew8aMuLFtMlHejUPPyf26ses8mOV5MREyu7eMTn7fWIvbLJirzLDS6T3-xXfAl5uso3v3nvFs0DtxCqCiwQifMO94zV2sLds2XCLtHSpqJbkSHMpQhR5wXackQkvPpK4wghfRcCARaN2DWqPE-cflqRPC7L1CTXphVevdb2-8WTKkJ__hK5hX4htlEAv9Zu4vIPEv1K2zy1_MuoFVHLbbhYz3usSX7nzxUEuaDupxguzGbykC9IW4oReKf_QS8Jc3KD6K3DOjczo6bbPmVi3ycnJltAyp9YtE7OKKsMCWPl4_klUBMEZ87myrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ معوقه‌هفته‌هفتم رقابت‌های لیگ برتر که قراره امروز و فردا برگزار بشه. درصورت برد پرسپولیس در بازی فردا سرخ‌ها صدرنشین میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/31493" target="_blank">📅 15:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31492">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZ0CiKvOUyGda7t4Xv3SKPCKWqR8jqvA2RLIah9RiYjbZUSReYluFVjn9WXbQ0WUaAhJGiHIqMo_kEP8puSf30RQ40heujkDPlgtsGVpmYhsRo6RhmliqeAMezas8IfRL5yrmy0AgeOVpq-e6F31Xe4zNNOqarLj4tyl3HIQZU2q0IbXkNGFPNP3ElPYC8TaV76XJ3Q65FbuQBtRENAwWIpBTShib9lLbgfTCWZnR6nE7WRc1x1iKM7B5ha6jcYb4Qp53k9fQpao79ErPQGK6GQRKjac-yihLu4aFEjKnMNrdnJk0aFLS1QHcqR0hY8Mjvfy4W5VHW1EUGqbHgIE-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیش بینی جالب بازی‌های امشب هفته دوم لیگ قهرمانان اروپا؛ ببینیم‌چندتاش‌درست‌از آب در میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/31492" target="_blank">📅 14:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31491">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKiQdEYjmSMINvZ7ZPVOma0tKgcpaUwQDUxghUdEMJpdTWYV9U9JXEC4pEpIhu9rFeItW2CAzvDuvN29kXUHNwDarMuMzxjtkhh_sBcOAvC3Ha8As1LYMmQoHtd9XS8VuKi5_l8KYIVQmKe5-T0MzcbhGtW8i_GF91SrfdhjEuGdNKaQCDe0gNgoJcf5bKkGO_ekAplfRVKwNDi92W5aofbo2RKnsPNtut6MdTfRKf9ftmlVI2oIhkuq48LeVbM4rGeR2BPtxbbU_D4vopuSJx9dtxNiXYGLWcMqlynrzoJm8WSmGpuMHkdYqaTAO2mqVQYixFFSG36sx8KIa7A4ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادت بدش روترک‌نکرد! جواد نکونام سرمربی تراکتور: شرایط به‌گونه‌ای‌است که همه چیز به سود الشمال است. چالش امروز ما مقابل الشمال شرایط خیلی سختی است که برای ما به وجود آورده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/31491" target="_blank">📅 14:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31490">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipyov-uynQQTkejw1naUPj4O7TjsKTcd48JwfvKPbVm8ynpCxscVEPG34JtrjntQucC4VZ8Lz3erc8BbaVhkQ68cmkELSdwFqsGwF3dU4YmM4FvA3H-oLPWct0s-EQcwexKEgDV-PpJWhWA7Xi8vXKknsGo0lnrsQ4Uyxe7xkd_zf28ng9Rmv2JMue7VtGFH6naVLoxbsUOnGmTY6fOrOPSryZGIaDDgVSXehpWkPXjHl-L_6C0cmqo1AA-R3KoR9UK91YdlYb2zlHb4ztHyEwJZg5Ene63DpKqjD5RgkdrgmmD2KvejHfUM9G6RpdJtAc6h7pXPET0OcnFm4xcI3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تغییر زمان چند دیدار هفته نهم و دهم؛ استقلال و گل گهر بجای یکشنبه روز دوشنبه بازی خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/31490" target="_blank">📅 13:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31489">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBb6TuVxQ5FZQYiECODBswQnwTtbGcLmr607hzuZUbp2eks5uG1p59UDE4nPubtetanDz8_XCBYhQ_9cXbqrltHU0bJHO5wgy0r2tIdLIJ6INRIOVyLhDFEIp3Ha4ifR-aAxI8BF9oYYlGlPrjc4HCtUQknlUiBXAmnaOQ4jHMBsyQFGOvIug_dqpT_nFUvYXuEsESwVMkZ1cj83DSvE7DT_SpctD1BC7-liTsnfODCpUVlNmh4XIIjy2jdktUwNUbq9oxE-IPcONByeqasPd0_yXtIFxlN6B-figFuIp6M3P8M_KpxIPbxdf9aby_zyasp1kQbhA9UsPU6yErIacA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛سخنگوی‌نظام‌وظیفه: باتوجه به کسری‌ هایی که علیرضابیرانوندبخاطرمتاهلی و داشتن‌فرزند خورده سربازی او تیرماه سال آینده به پایان میرسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/31489" target="_blank">📅 13:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31488">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWEA3n0hWAc-z1ikKk3oSOfZztDA7VzhD15B9hocLq-kiVytG19af2oiFO8-98_YdBYuZEqptt_gKThL06_8nxCPvJPE3BIzeIo6AlNtHbvMF6kLuqDJA2ewR7QRkwpiVt7G2h9HDp48_CUKQD7g6NBzCOj4t9qfoiT-jKFfqQ1ujP46_TmKJNIPz5m87deZPEGiH3ViDiOpyf7W0oJ4HbsKr7WRG3tCmAdeNhdw78RKNue5C8aEVujH0Id3EicwOaCWO34PswBoz0gstW8JuwpTTDUEo4IuYIxDBJR-6UUhb1YDivXcQKE_M75L-RDf335DNeKPvMrGlNmwcpaPEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
درهفته‌پنجم‌رقابت‌های‌بوندسلیگا؛ شاگردان نیکو کواچ در دورتموند درحالیکه تا دقیقه 85 دو بر صفر از وردربرمن جلو بود در عرض تنها هفت دقیقه دو گل دریافت کرد و 3 امتیاز شیرین پرید. زنبورها در چهار بازی اخیر خود به پیروزی رسیده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/31488" target="_blank">📅 12:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31487">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ly5NA01lHSrm9sO39acfKgqw69Lz03YWc6L7DusSgjswo85vPmLH6DtQASiPfb16KQMjEFK3KZT6-_ZUhm2Op7FuE8jEEC0P0dR1dw3dQaCTzuSfYMrbguJbHGxLU87eqX_bHNMXqDMg6Sh52QQimERGaSm5T0WIu2eketxcXqWIOiDlwDlfhfRiUbbMf6m2sUnbiSNtIb-fWP4-8bB8mF3-HKhBOh51onmnRtbA1G7kAPCGWFwTaye-PypVMPKE2KbJDBTzf0TkphgWpdjKbr23NCMQDcJ2mYFFfToZgQ_AUoRiWJvyDWkiIdvPGglwvNzptFDhNcpiy4QNUwbbMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکثر مسابقات لیگ برتر مصر رو ایشون گزارش میکنه و برای هرمسابقه 5 هزار دلار دریافت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/31487" target="_blank">📅 12:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31486">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hes2KS0hYLpRf6OvlDKGJbEN1RG5rDW5iaXcwjVC70MbskncggEv-l00dRlwFMHjX9xTcTloCY6trSg1jRQX_hsEfDnq_OJwPBebdEZqc1AbmloDKVzrXCurtbVIAxBUT6IgtgbSjkxDf9DzljyF1zbKwHFGEwtbTs_5qnXt1XrolVLUsAhTQqi2d0CPMDarmliIr5AjUnItrxmIQZPJhcVtwIvEALx7yYvGPsTFPJXCQ97BsmDOo7E7zbAkqNdzEJWMOfn6bv-6EArBBUpZ6XVFmg9wKjoGG6MDlVuQd9yvW3WX9e1rWhi8p3YC-l4AAQQJrX5S8pWBULV-EZRkRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسیرسفر گلگهر از سیرجان تا بحرین را مشاهده میکنید. پرواز از سیرجان به تهران، از تهران به نجف، از نجف به بغداد با اتوبوس، از بغداد به مسقط عمان، از عمان به منامه. به همین دلیل خواستار به تعویق افتادن دیدار با استقلال شدند که مخالفت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/31486" target="_blank">📅 12:28 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31485">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71e001dfa4.mp4?token=qRujffSq9FuMRyyXxVujwDdCZe8wa944SWgO0gAFTlynUBtKpZeYGdl9NeD2ykByELOAwZzlbRaei1EyOuE4WKNZoElfKL_3ncLT4hjxiGMKjFTqIs-e4hir4_fUE9p9JcyYzYrF-pNJawxA9D2BsW5V8WA3cXGB9qrBTsKUJ21G-BUv5Uq6mdR5WpOvKTI6Uf1IhP7wPM1qwTcvXGmiGWdEVKWiiTbwTd2T5fcALhqxJ1EkS4CNCcSruavOhicVH__P6h2Orj27a6WKsJB4p2s5_cWPlBcz2uhR3BIUtRs7t24Q2McBJs2WcAY7Gxo0V4UE5Fhd-SJLZykMYTMGbEYG27qfXjyWZVrpD4lszudY1cKW-LEoK1pP9qme13Fu-gsHD3FnPFUgSYIqFc-GUIgUXBVCmngvMm2fnCQH_BvVWz_b-2ScNld2sTSDTHn6RePblJX861AKXU2JSzz1SibyNnuhdEQ9K1Wa8GHUY5K4ovvaTz2ilKYZWbIRLy8IjQkNJc-5mU6Rl3V26Jh3J_x2rAH-v5vGYsUVVlVzeHdSf8iQw2rAhS4lXEqkVFXgEaa07mYdz_XUUgCAuoMyULRVa0aYQvMR3iyQ4pgfnclYlfgzFxxRyxF9Jq3TDcDvA0C75CFVtb59kqHgD10hyGkA3MVqOvKfsKEK8v0wvLE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71e001dfa4.mp4?token=qRujffSq9FuMRyyXxVujwDdCZe8wa944SWgO0gAFTlynUBtKpZeYGdl9NeD2ykByELOAwZzlbRaei1EyOuE4WKNZoElfKL_3ncLT4hjxiGMKjFTqIs-e4hir4_fUE9p9JcyYzYrF-pNJawxA9D2BsW5V8WA3cXGB9qrBTsKUJ21G-BUv5Uq6mdR5WpOvKTI6Uf1IhP7wPM1qwTcvXGmiGWdEVKWiiTbwTd2T5fcALhqxJ1EkS4CNCcSruavOhicVH__P6h2Orj27a6WKsJB4p2s5_cWPlBcz2uhR3BIUtRs7t24Q2McBJs2WcAY7Gxo0V4UE5Fhd-SJLZykMYTMGbEYG27qfXjyWZVrpD4lszudY1cKW-LEoK1pP9qme13Fu-gsHD3FnPFUgSYIqFc-GUIgUXBVCmngvMm2fnCQH_BvVWz_b-2ScNld2sTSDTHn6RePblJX861AKXU2JSzz1SibyNnuhdEQ9K1Wa8GHUY5K4ovvaTz2ilKYZWbIRLy8IjQkNJc-5mU6Rl3V26Jh3J_x2rAH-v5vGYsUVVlVzeHdSf8iQw2rAhS4lXEqkVFXgEaa07mYdz_XUUgCAuoMyULRVa0aYQvMR3iyQ4pgfnclYlfgzFxxRyxF9Jq3TDcDvA0C75CFVtb59kqHgD10hyGkA3MVqOvKfsKEK8v0wvLE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش بینی جالب بازی‌های امشب هفته دوم لیگ قهرمانان اروپا؛ ببینیم‌چندتاش‌درست‌از آب در میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/31485" target="_blank">📅 12:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31484">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2RulGR5GFMDjWfPv1QUcezkc0UCSylfkNAVh5KLI52nlQggHJWk_FhyD-Y9k3V2z0EgCN2d1oCrg5KYZtxGH01_Jx9tAJE9_IQkDPe3wW6ee6ksC2cZXftDP3HErs11WtLCzDTiuc75mOsIA-zMJha7UNtQyu8zipeSW3jYQhc4TNjDiuB75Qrr34NpyvknDPtRdzvkbbLKZJX2_lK0_XSD_JD95Sgq1zQB8-V42Tn4PunrijRb38LflNRxEoAPoiYU6fKawUmGUAHlEUzWHpULeIx7LgAyL3fKkV733niAnEoUJOcyJH4EOWS1neUBPS1Gp2b77_CGPgMbKocQOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
با اعلام رومانو؛ دنی کارواخال مدافع راست رئال مادرید با قراردادی یک ساله به ختافه پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/31484" target="_blank">📅 11:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31483">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ua-VZkkQperXiDT0lByG41nxmlnLO8T5PXlsHv_4XN8kRPRZpxrhG5Z9qngFYxUA7JVA8C1JmGcU09jxdh4OjJ4Pv0EwqtFsOXOTCEbeIQFYslT_2DbxHkFYJieNp8Xnc541UGJiNpcCRd77BmdOqDWqVJ9e33XEOAHlxSPZPOEueWf1xuA-OVMQhXmyzT3hfezORCRbpyGtbHChgPVuhj_7PjE-m4WoAwiGyI-kBHifDBge6Ebn99V3E2FinvXjc0Z8T0xFFwH2y0dbDPulsH2LBts_3fZPNO2anLiFSc0KiijQby06IhXOjipkjTmdfi5BmUjXySYf48OuoHthkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حمایت‌تمام‌قد کریس‌رونالدو از کشور عربستان در جنگ با حوثی‌های یمن: جنگ هم شود از اینجا نمیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/31483" target="_blank">📅 11:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31482">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Asn_7fEs7aq0gZFWjzDtBDR2M17wwCt536yb4dIJ7EzM0gcbVi0a2XgyrhVMElG_C7POznJFoS0VIbCvlXxvzGhRL2uEDQTORMUAtlL6HTRi8vDRB6UjhLP7r6APOdxWuENvmmghaUiUIn_zWOw8hetmAWaQsnvovG3xLi5xpnkFQu3pVU9kR4XcjI2EsQAIcmr1VKTLhkNIh0Vx1iCPY4zqSgohqnp6BAAfkEHMAM3s_WOesOjGxIESNcZXgBqbooEEizGiSOVV5Kd5OuIlNaOUEW_QiXjXOkJuWnsuPo1dv5Cr1_A8EzaOjfjwWVm7HFCa-WI4ub1qFg8qGUe-jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بوسه کریس‌رونالدو روشمشیر و درخت نخل نماد عربستان سعودی و ناراحتیش از جنگ تو عربستان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/31482" target="_blank">📅 10:52 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31481">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atT91HfW-3Az5GQubddFCuu4RKw3V1eew0mLOgXH_x2GUVkWQsw9QwUG1A79Ktf5wfZXhBsZtIUBazEtZle89G2k6ZSx30hy5U0z2q-FsKO3AHhkcYj2r9NpQ3KIZJTLwzWRHn4riLT9T3D2eZOyCqNXIexUb0oq6ncohDcdrHCrEYNL5eLSexDPf9kViYjcMqWds1WTbNgbC_4Cn3_rYO80GhUkxD_HRN9jMeAVH5xt82rO_XvGgv-3ld3lvgaKluktb6L6KVPC9Yut6ne_e3xeocCvaInJsHpTAmkkNyGv0C3aMfktJIfyG3eXa6LVXxtV9lUNN1ryulP4cGj1kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
برنامه‌مسابقات‌این هفته رقابت‌های لیگ قهرمانان اروپا که قراره فرداشب و پس فرداشب برگزار بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/31481" target="_blank">📅 10:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31480">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmI41aMQfzQmvKTCf2wm0Xxywh4l3jP-Bzs8HZCY7CyoVaj1eGRBpXKbHTVBhDIVVSejk9azeRiS8Ifn-Ojs2QMd1EGFxRaFUrjzjeLJnYmrdkhUkUaxLgRIvQCr614jV8zLuR9NTXGM0I-G8NcLYg83SPWzBMyt-rAnGnLwY8iWdcQ0x1nl7FwA_Ctb-tqx9bwbRS7kIzXdNhfomEzsX5y0z6VHu6cxo-GkNRrfoH0okbFo8Njy5ydi_mLgMAlavRfFqBQtegFKAUWyHsmqIW8_VyaaKbqcV_7x5pNQiOcGs5U2yRiEM_Pfq8aKJM1JMn1OiCMBvkCLU9-4M6zZwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
👤
سعید الهویی دستیار و همه‌کاره کادر فنی امیرقلعه‌نویی رسما گفت که مهدی قایدی بخاطر اون مصاحبه‌اش باامیرحسین قیاسی خط‌خورده است!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/31480" target="_blank">📅 10:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31479">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6DjTkWD6GKU7GiC-JE-f95KVV8sFAAQTcNPsJ9fd9kdRhWASf-xEr5rlspElhTDPe6-EnikL4FF3ZyxADdCFpo2X9grx-u-wTdpSnbksqmSz-LxG2YT8GfNB7s-WjwSXcYQ7D5-xIuUUs6r8AF_wgd4PsNXfPOFxSXhlJ8X9Z5BQ93jmsEL3fq2zzTfX4Y2ACuMLvAzHTBBEPV6b_KFsOT9oSmPjF5VQMWCKF1MLu5-QQ-nKeprkfQxhCraPgqrdIJSnwLbKyov9I_e1544ZDgpd_VsoAOnRn5Ail67Mje7_hG5nAUAsAoSbIWSuVqKDp6U0fHGkKgaM5IlPfDedQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارهای هفته نهم و دهم رقابت های لیگ برتر که قراره از شنبه 25 مهرماه استارت بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/31479" target="_blank">📅 10:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31477">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b74c2dae8.mp4?token=UfDWI8qj9QZq1kF4DUiZENZfE_sL7c0uqb2tTuHkRYCC-llrYcwtMBj14upA2g41W3fgkC5Vu7dVOQNiOplM-PCZNbBHNWX_K7Rta0V59N8s7oqJRJeg3rmFKCDroioWBKo0FxAfSXzrH2yBGLDmBXzKdF7fI18LvYEJF1Lis3G-l0vEOQFDBS3TjNC0K5UacylBbcT9CM5dJYINjEkbfTsmeDOINkY01IYJ8_uFL3Ya64Y-fqdMAKypV-XU5IgUhnrKhy23svHAsgJFnmnvpH6V4SH1gfi-FtSFDL0pnmcPPSL5ZqlafL6e0bvi0vt5XnDrP0h_J0k7u7KpLAFB8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b74c2dae8.mp4?token=UfDWI8qj9QZq1kF4DUiZENZfE_sL7c0uqb2tTuHkRYCC-llrYcwtMBj14upA2g41W3fgkC5Vu7dVOQNiOplM-PCZNbBHNWX_K7Rta0V59N8s7oqJRJeg3rmFKCDroioWBKo0FxAfSXzrH2yBGLDmBXzKdF7fI18LvYEJF1Lis3G-l0vEOQFDBS3TjNC0K5UacylBbcT9CM5dJYINjEkbfTsmeDOINkY01IYJ8_uFL3Ya64Y-fqdMAKypV-XU5IgUhnrKhy23svHAsgJFnmnvpH6V4SH1gfi-FtSFDL0pnmcPPSL5ZqlafL6e0bvi0vt5XnDrP0h_J0k7u7KpLAFB8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دستور محمدرضا زنوزی مالک تراکتور به حجت کریمی: قرارداد علیرضا بیرانوند روفسخ کن. او دیگر به هیچ عنوان جایگاهی در تراکتور نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/31477" target="_blank">📅 09:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31476">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7c8f6c96.mp4?token=UQLr-a05kA5roeFdSlQ-Cb1BPTb3I0JNQ37_6y8_TYB1SV9Dq5fdNL5fN0p3yXYuOdlLC-y9yUKmGlvqwglTAiCmpGtcSo8B-tCoDrEUAKuwrdnsjJoWxdakSUvthRYTu9vdeVk1gGrTJHoHIvpE4MTDGoAqD5RoKJjjXbhf_3jyi-2o7RgEn9uklJvTfk0PPAsYZ8Jbs-CqquDEaDBJnpo90QKALuemWDl9wZuaqcBr2PhfJs8Yz0OPJpk25ia23KJKWsI2SXtxRvEsQ20tD4uXZGr5Jx84yUbrV0cUUbpW2JakCj4Ke7Xs-TZw-lxH2puYY2tW6k-9DsdaRwkqdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7c8f6c96.mp4?token=UQLr-a05kA5roeFdSlQ-Cb1BPTb3I0JNQ37_6y8_TYB1SV9Dq5fdNL5fN0p3yXYuOdlLC-y9yUKmGlvqwglTAiCmpGtcSo8B-tCoDrEUAKuwrdnsjJoWxdakSUvthRYTu9vdeVk1gGrTJHoHIvpE4MTDGoAqD5RoKJjjXbhf_3jyi-2o7RgEn9uklJvTfk0PPAsYZ8Jbs-CqquDEaDBJnpo90QKALuemWDl9wZuaqcBr2PhfJs8Yz0OPJpk25ia23KJKWsI2SXtxRvEsQ20tD4uXZGr5Jx84yUbrV0cUUbpW2JakCj4Ke7Xs-TZw-lxH2puYY2tW6k-9DsdaRwkqdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
واکنش حامد لک به صحبت‌های بیرانوند علیه علی دایی: طوری می‌گوید در نوجوانی کارگری کرده که انگارهمه‌فوتبالیست‌های‌ایران در خانواده میلیاردر متولد شده‌اند. ببند دهنت رو بابا. حرف نزن تو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/31476" target="_blank">📅 09:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31475">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e5884a83c.mp4?token=cvnBtDISTQFcMwGm627BV9Slzd5Vg7zQTCZgYQnOe9q2LpncPxFYXlv3WFK2j4BvDIY3lqIIGesgUoI7vO9223WvkT74-_oZWMGLeT6Bg2D7YLelpdRXw4cc4LRSFyJ3xSN2n8qSMFD-DWd2gwryNCkvHHD6XeK_KWTnhn-ktTwLKXhPpUubSsKLwBU1o4qurMEY91InYyfk5C2DPGJjVsQdsv-Wlq18w8a20GnHkY6lgC1R1o7Xb9eI8LpJW2E9FqaMacsHJ7lm3qqsfq6YrKn4blI5yMwRvy5wZmJ4C_SDkc_zksKENMV1PY3-6eqg7X8uf-kIme-DY-7JKUq8PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e5884a83c.mp4?token=cvnBtDISTQFcMwGm627BV9Slzd5Vg7zQTCZgYQnOe9q2LpncPxFYXlv3WFK2j4BvDIY3lqIIGesgUoI7vO9223WvkT74-_oZWMGLeT6Bg2D7YLelpdRXw4cc4LRSFyJ3xSN2n8qSMFD-DWd2gwryNCkvHHD6XeK_KWTnhn-ktTwLKXhPpUubSsKLwBU1o4qurMEY91InYyfk5C2DPGJjVsQdsv-Wlq18w8a20GnHkY6lgC1R1o7Xb9eI8LpJW2E9FqaMacsHJ7lm3qqsfq6YrKn4blI5yMwRvy5wZmJ4C_SDkc_zksKENMV1PY3-6eqg7X8uf-kIme-DY-7JKUq8PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
گل‌دیدنی‌کریس‌رونالدو در بازی شب گذشته النصر مقابل نفتچی از زاویه‌ای متفاوت؛ CR7 بدون نگاه به دروازه حریف توپ رو وارد دروازه کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/31475" target="_blank">📅 09:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31474">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39e71f827d.mp4?token=Ib8UKInIw_Z_-RAkkKr7c2gn1_x44JeAeK4leF95m4XrQRzgHBjmpaFthMnTQJg698RM_IoVlCOhbEZivBOfma1D9Pw9J_cpKCqiDEdlZgcfxDDq7ryrugss8JuHtOxpBTbp7u5F6HR0rHDvSneV-GDXP3YdFDQTayB0aDwDIKczGspaSu4Tb4UhyIXsS4dUURAfO00T0_jtt2d0Ulw83IVasOuV_3hSyekAOyLGfoNds3VKTtOt27xeAgCLONwXF9l2gi0bbmQ_19U5-z_XZF46pJIT1JPr0rDahMHEywN-uBPQhiE-nClggY1prkYGL-_rwo9xxs8y-9Qzp6gFkn_WgVlhiRjGjTV4IWzxMNW1XOXM32iEt2-Nmzt3RVQ5WHRgNB7gXxJU9gwLqFRzUvwV8kTiy0r5-LuuCRnq_eJ37UV1dtUrG3T-SAMNJa9aAVKaWtELCArK916sh9Ks99FOas3OqHI7VIP3--tBVUxXgZG_ans5ewI08YVPLZiF37gKctfaJrAxtBlbojedVK7LKiNZ-fqpKe_1faSY2txPP7YWPCYxA5hW1EsFpMsp-Tl03bGZjjQ8gEtgBpQ2Nb4cFcm9Ox8uBjkpiEgQfPUMrf3YqPyJi7peXycIG52onbGpOtoao4uWLRH0DbMcffWsIfqonleRz_KhngPuMGY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39e71f827d.mp4?token=Ib8UKInIw_Z_-RAkkKr7c2gn1_x44JeAeK4leF95m4XrQRzgHBjmpaFthMnTQJg698RM_IoVlCOhbEZivBOfma1D9Pw9J_cpKCqiDEdlZgcfxDDq7ryrugss8JuHtOxpBTbp7u5F6HR0rHDvSneV-GDXP3YdFDQTayB0aDwDIKczGspaSu4Tb4UhyIXsS4dUURAfO00T0_jtt2d0Ulw83IVasOuV_3hSyekAOyLGfoNds3VKTtOt27xeAgCLONwXF9l2gi0bbmQ_19U5-z_XZF46pJIT1JPr0rDahMHEywN-uBPQhiE-nClggY1prkYGL-_rwo9xxs8y-9Qzp6gFkn_WgVlhiRjGjTV4IWzxMNW1XOXM32iEt2-Nmzt3RVQ5WHRgNB7gXxJU9gwLqFRzUvwV8kTiy0r5-LuuCRnq_eJ37UV1dtUrG3T-SAMNJa9aAVKaWtELCArK916sh9Ks99FOas3OqHI7VIP3--tBVUxXgZG_ans5ewI08YVPLZiF37gKctfaJrAxtBlbojedVK7LKiNZ-fqpKe_1faSY2txPP7YWPCYxA5hW1EsFpMsp-Tl03bGZjjQ8gEtgBpQ2Nb4cFcm9Ox8uBjkpiEgQfPUMrf3YqPyJi7peXycIG52onbGpOtoao4uWLRH0DbMcffWsIfqonleRz_KhngPuMGY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔵
👤
با اعلام مدیر رسانه‌ای باشگاه استقلال؛ مصدومیت یاسرآسانی‌جدی‌نیست و او به دیدار هفته آینده با گلگهر سیرجان در هفته نهم لیگ برتر میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/31474" target="_blank">📅 02:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31472">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dN0HJYxuhBvr8xY4NdTyOA7rV_znagC6-Flk4SZfvOht-FYdwiupjJRGu2CLbnl19BLb-1Zl1glo2T6NuwMNPkwvnBJxbNGUZIWGvn3tKFmxD-LzHwQTPDgCQTa1SMuOaDBFM-iSigtaYUIGMQItEE2anRzxdUcAX-tMtCQDqRHLUvr9WaYrcF8hztz5pTGeJv21hGEdtVxvvmG012BhKI1yE855ePEmJxsB0MzKJLD9RYTG3zqIJvpQh5cWkMPjFFDO3pt70WhkGTn5Q8r7hPoLfBEvOCnm0_GtDOgeaZ0ryIsHDtul1Ya9lzLbyb4oecR6U0t9HXvTiIdxWvkxJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ نخبگان آسیا؛ دومین پیروزی پیاپی شاگردان بختیای زاده در شب درخشش یاسر آسانی؛ آبی‌ها با پنجره بسته در صدر لیگ نخبگان.
🔸
الغرافه قطر
1️⃣
-
2️⃣
استقلال ایران
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/31472" target="_blank">📅 01:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31470">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4_rg6MHaa54BTtcmXJibdWjjO6VlH0TOMcDXDfKuA0ZU6duwVuo6MJdfNjcjMhQcvwedC90vu__jJIaeQ6tFM6eZooXq0nr6ZOqRaRY4EwxRcg78naPqB9L3VW4FZp9e1N8qKjVFjjnYyguRUMI8N20iP2zGvYBhzgMfD05ccEEbYLP4uLVKjhLhXJyesbbYHMMc-_oVsDwZbARj6__bwLONFK86LMOpj8S2VegWGF5yLWp2ziUJM0ngcqk6ScAHrKcS8vjQ0XxwI_tprVAdrCbNHIh94WC7cwU5DGH3RpYQ8QtiaqesQKGod4zhqMBxwq2jT5EJN6iPMsHLmiSwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛ از دوئل تماشایی شیاطین سرخ با شاگردان سیمئونه تا نبرد بارسا و گالاتاسرای‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/31470" target="_blank">📅 01:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31469">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_NNuq214YZ-p9TOVWN231vuhrK8hN9tvcGy10h7SvHtNw51TkqLaAOX4TCN35wpECto0IPhcSb2e1PcWNz7sPCUxRUUbG0GpOc6oGWz3Wsj0sanTYMJaRqdNcbQJcL9az3FuQvDVJXMR32nLRuR7wuOcdFcaXoljyBj71lvY-4FXOEBXZpyWP50uTNUoE5zS8RfpM7vfSVwHxMzOOFnmyOez6QCJd_AKQQFxjNO82Hst1zgcsT1utMsbk7pAuPnTrmMyWp6rWOQEwBRCmSvHfcJmd9Q04JevN3FBPVgucavd3uoEEwZIbTSyVGy8MQvwBKeQzXL60Iob8mss4d4Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
دومین برد پیاپی استقلالی‌ ها درلیگ‌نخبگان آسیا 2027 با سهراب بختیاری‌زاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/31469" target="_blank">📅 01:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31466">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l_UBA-gjWxoUSQExRHBn8M19L7XVAQYk4CDsnhLtMfTmDIpL7EDnFCezsDnMp5bQhBhPITtluunEbP-oZw0Evz5OEoF4R5fNVKuV2RfAqYRGazeW9Mz5RInJwzssC1qgm6EI4g6_CXks3Wn6_3nmfsRGTr3_f0_nhZIdq8GBIC4ATUbSGLPVOb8ewMoDYQ4XDYfyF131upBbJwJTBoECIvGkMMCPlcv11HPHdR6WuRDEVkfjnfsebS7kefPI6OGJWT_whWYEa8YQ--Th8GdFFx8kWWJ7G4H4D-Iafw1LeqFDwcqlHswGrhi5OZpYXtBq_RK9PI_5XA1DAEhApdNkBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KE3u8HWWgANDppPcUmq-tym2F52gCdKc6JpL5p-1H_pyIwGgNFB_jmmk48zvCeYUMSaexsZA8_RY75jNt-vtw-jjVpQkjHlJJ7h14lWQxWpraXwFeO0MRx8b26gQ4KwBC0DQf0Q_V2MyIRBmRvMuEzAjo57O9UetucNtFUCy2HhuC_mjByq3jHq1_FinsXkkaBIWjhWANbNONAwcOAuQ7hKws3ROfxBf2BNzqxXW4DKZBw9RUFHMo3PmUsYmJGO5gf-viBSEyBl9JTrwPR6G5wyjSpB5jsVqPIEdWj1S5nNMk1GJo352r8H0Pv25fvuF5bPy6v69t88Dwm6fcIEe-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌دوم‌لیگ نخبگان آسیا؛ دومین پیروزی پیاپی شاگردان بختیای زاده در شب درخشش یاسر آسانی؛ آبی‌ها با پنجره بسته در صدر لیگ نخبگان.
🔸
الغرافه قطر
1️⃣
-
2️⃣
استقلال ایران
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/31466" target="_blank">📅 00:57 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31465">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSxMwk4Xtw3YGiSUuo5Kns5b7FT7UpqdFw6aNB1U1UV709sRifQymClQa_lwcF7FWcJqNReV4WhfkkpKFVRNzbX3TSNgIb7DN9G7TXMvrhObVPDHNy7mki798oEl3Y_1i0ynmu8dU5KmaL-1xFuH9rhRQkwGPMXUrt2qDW1OHLn3dfP69Lksb8DZ0vr1735NM-3j5YE0saI9FWnedn9iCU2Bybj4I_mZnBguMgu-jAycCJ69QCxkO24sZr-nzH-OMSwu_W1WWt8lzzHZpckQZhRRXBcltcr8wMEjSWGcB4cyu4XLqUqTpoRvqnUdhJJfYzjwS7Zb-rMqXRkIg1Vp9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
👤
با اعلام مدیر رسانه‌ای باشگاه استقلال؛ مصدومیت یاسرآسانی‌جدی‌نیست و او به دیدار هفته آینده با گلگهر سیرجان در هفته نهم لیگ برتر میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/31465" target="_blank">📅 00:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31463">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZR_oQ6rF1MzlbaVy9R0pjehqjqwX8IA0aL2uOybx5xjsoiC5dMlW_lbudiL2xbI1ECzhVj3qIvLl669azvszMXAhK9hsbwDu8gzsUUBCTdz9-kvG1JWuHyVs1DXfy_lYFvfoS8dEOHn_wlTln5XzoqLWo-4TCfcWvgLOnHROS1-QJkq4IrKpVhmbb4kB9aHWLqn91XJzfMqC53bgzsm3DWZeaTzJi6x8T-Ez5g2h9x_afKdgSBVuU_A5Hw1GUqmbuhzraxG1rPS0PbArsMdPsZWy1ghJandoSOtJJcd8Tf8KcgfjdIEN7YdlYkNE6_a-f27pGIWh6BIRGygL6-NgmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
#تکمیلی؛ یحیی گلمحمدی سرمربی دهوک عراقی توافقی قراردادش رو با این تیم عراقی فسخ کرد و به احتمال فراوان با عقد قراردادی چهار ساله سرمربی تیم امید خواهد شد. فدراسیون با افشین قطبی برای هدایت تیم ملی امید به توافق نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/31463" target="_blank">📅 00:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31462">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgoHZUSO9knG7Utu3uXMWzN1Lkb5ntbDzQO0GI_xHouY26misKe4aL0HVkt0_I1Pq4btcY-qBHDhRKW37eNtdmB1uKmKwQa6tGy350vqvYZ0epBJ9HRKxiPgYMZlOSSZeiTBzl0by6QvUPT7S680YO4fGOgdYqDuYSQCUSo2PxvmiRp3gBO51wj9wLFyjrSkgFtWl2ai2d67d-gK7ErW4cY8nWlo-15qiYIo3pJA5p5JKHRQcuQh9_47mqSx4Q4J35aICNYwK7MFciJddBQUI2RkQsqK2I9-Im6WYLMuz-x1QAow_HqE3eXmYwXs-BVQJrvNt-FdIQCvyyiR_Uktjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگام این چه خبری که منتشر شد؛ آرجی میته، بازیگر نقش پسر والتر وایت در سریال بریکینگ بد، به‌دلیل خودکشی در سن ‌34 سالگی درگذشت.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/31462" target="_blank">📅 00:29 · 21 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
