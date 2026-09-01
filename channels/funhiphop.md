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
<img src="https://cdn4.telesco.pe/file/h4bhgIienNEXV9I5gJWEIPBJVWKcIrM4fmybBnBwZL87Pwnd2QZqNKchsKbb56jswrOn46eIV-0zXEo5307VGPMZO0gIQM37c3sPkEETpDRoI2thMZhaxmDheDmuUJXb5soe4fRMC5_R2KH39CE_BukAHcbFFzF_5oU5X20uF7zRzeb198uCpe-w5z9W5EokVt2F_vCxSv8BC7k32Sm11KSPQACGAfovXthDv72GS2E0W29nByp9wA3eo3YZJT-KkLhLdLurXZdjdACZrJLmNma0NeQofFuYueWgHALzjK_TTDopj5_geq2hzTwfDZ0h9kLwxs_PjZ6mSXjh4xda7w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 225K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 04:27:56</div>
<hr>

<div class="tg-post" id="msg-82846">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3tlKKgE6q_beu-zd66zb22PaFVagTnNQAx_SzhbFdUQMzzJJyOsd5MJIm6eIYPF94DzBgh_ziyefP9AtE87NeWXdYIuRtOK5jN6_BeHZt1FddILKkGG8Ccj5CTommQ4DFO2gZhI-gxDhcC9B4VcSh8TWT0S_AD4wgyOqeIe0Z9YThvHQrr6FEA9q8-OVcsHCreRp0wa6wyqjXZ2k-o3KfiASRxKaXuZ4GdeqqxkPvT1SES6Sd6-hzULT52jCxdQA7L1Mg7CS1j6doEh7SI2eXZx7IGp4r9MLU-21oI8Qp7DmTTmOl3_9U9xREiWagSX75sWGwrSamFgrmDZnjWiqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلیپ لام جدید تو اروپا متولد شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/funhiphop/82846" target="_blank">📅 01:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82845">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کصخلیتی ها.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/funhiphop/82845" target="_blank">📅 01:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82843">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChXrU3t3zvr9kD7cvM4kavymleuC0loHSkrfhj7ph2mu3KZbKgKfM22M0X1SmzlhJgmLEd7UgdJoV07j3WReZRtXhxMYJCVeaG7jbCXaaAGyfrq-8Ahp_t3h6WF3TaSUJsbH3O987HsIjoFXFEUXBET1crrQ64kBVfHY_qpL_dxNYy_-9Pu1IrzXksBlg3vFRYytavJWX4xEpQSFiRcBUuTdJgVea8ho1V6F3FIGbz8by4h2_9R5bvMdK6suBQcVgZGgP69-cLzgl_QAMSvcgN3TuYYqJlmUUfiYD1hY62Kop94-M7oXzR5IJ8Egkrr5xrCCm9vDVL2YQP3zbyWANg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6efb1a9258.mp4?token=Gbv4Jn1tH_yo7hV2E2HeOpjIO57Mm6Z89PTolEkjgj51JZ_3hR5OrfBY_UzvIuh8nUqZu8lJDRKceD5ews9EjAnR5TeQWsBz_L3cRzteyC_Sd1NyUM4yQ23iMDMphonOj8lYRfziPdulzfYFsSI3jRPj6Rjy5VAzesEhJUebB2fw44AWIpJit7nSOwCwjTHuY0bYHMFr3t9nEsRlS_7ZycA-LlQ1LlwnVybuTi_zKFydxca-Az5QAEGMppPJgqA25XPHZOavgGs-96UKTsHZZ5YkpLFdEw6HljWCGFLNNNGumpIedfHQY-FrCzU5Ilm6MWar0jH94TWv3AJOc4yctQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6efb1a9258.mp4?token=Gbv4Jn1tH_yo7hV2E2HeOpjIO57Mm6Z89PTolEkjgj51JZ_3hR5OrfBY_UzvIuh8nUqZu8lJDRKceD5ews9EjAnR5TeQWsBz_L3cRzteyC_Sd1NyUM4yQ23iMDMphonOj8lYRfziPdulzfYFsSI3jRPj6Rjy5VAzesEhJUebB2fw44AWIpJit7nSOwCwjTHuY0bYHMFr3t9nEsRlS_7ZycA-LlQ1LlwnVybuTi_zKFydxca-Az5QAEGMppPJgqA25XPHZOavgGs-96UKTsHZZ5YkpLFdEw6HljWCGFLNNNGumpIedfHQY-FrCzU5Ilm6MWar0jH94TWv3AJOc4yctQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضا پیشرو داره غوغا می‌کنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/funhiphop/82843" target="_blank">📅 01:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82842">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">حالا که ما رفتیم ولی ارتتا مادرجنده به این کاری که دارید میکنید فوتبال بازی کردن نمیگن</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/funhiphop/82842" target="_blank">📅 00:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82841">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTemSah Bet(Mehdi)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAo8REfESi0Yz90y7zD0gsT0lPq4LHIPp9RzUxefrcHkg99F2oVaifB3HOU86thXPBB2lXRFkJ5JNQRii5eDUxi9cc4_LZhaRz7irE18iz7Jt4TxjdSIiy7MXdgq4N-pI7snV0XtXeMhOCF4tkgfrOIEFnF-v8sBL9LBrti_-fCun6yF0rJyjiF0p3uJE1af-EbsobIZRI_ZTbwEgI__D91Up-JGj7KNnfd36LFt95G7PxysVrQfcKea2MALn5HWPPl_YGpQ8PVpv-V9pSB2dElY4Erx9FCNgRmr7AymCvdAhtHmR-h6fLIxrH3n7rpkh9kuzKKzfFL2o8PAlL4m8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خایه ام اومد تو گلوم</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/funhiphop/82841" target="_blank">📅 00:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82840">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsQZ-sGFpXwuf19mZvqnrLgkjAOTFfT5ZHfG50QPs_kZSHqKWqV2qir59H14AkEvGFQ-i0gM0JUJJ6EgYJQWDTOFJuyAjchjUkEF_5fCV75bdReJodbBDr-3aSCf_ve2XXzaqAK3RXRIbMD3wAsgVoQj8OeWfhoCa9BNK93GSKS38OLKpWoMmUH6OFBybnZdGQ1uDd5jtGu5ajzTQPVepAKXTFXFHWHUWOOHKS7HzkjT__NMiC2wNHTpCy1mp1KmjuAtBFHBxWmL1R6z_BUiYOCLUrT8PYP-LAIGKDZfZN_ZgGAvWDQigj-_RRG6OtrrrVggzFKdVkDtxr7j1UEJwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشه یه نفر بتونه انقدر اشتباه کنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/82840" target="_blank">📅 23:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82839">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzSR3GaiGjOsBDR6oYB0ECRFRolZqmqvxfzQtKjISpoWetJsvWGlBjOTFuSe7Ge_0p1R_TMD45_m-lNKL5QwajlH3m0yLpi-ap2PfVLEB5hyUPv8SUhW9BXip2Xm81PgrB9wydLpO_2MDAyyWyovvd5a6ztnjpulQAhzfVSc6NJI_kLJDjaYHB4ThGVboHPxew2MOmFEYf77X8lNrQFh1wV5nkE2JVuJ2IUecpHRF9S9izS5f3xRQNukeREDE36rYEy2R0Nowbhwmjr_mU4w_x20oWSD4Z43CU2Geg6qy7uEM_DHGncm9mDpcr2hbbKmYSxtQ5q0M9SkReDyzOm2yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخاطر این چیزا جی تی ای رو پی سی قراره دیر بیاد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/82839" target="_blank">📅 23:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82838">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پزشکیان در واکنش به تذکر رعایت پروتکل‌: بابا ول کن پروتکل رو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/82838" target="_blank">📅 22:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82837">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">پدافند جمهوری اسلامی یک فروند موشک به سمت جنگنده F-35 شلیک کرد، اما موشک توسط جنگنده دفع شد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/82837" target="_blank">📅 22:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82836">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpMylAACAHMd4gLZiV8-GYUtYJI20DYwxvMa8wX19sfh2-ihKvnUj0FdiTUbMNkcb-cEihQfn6wD3LmfGnVUcUWEYtf2Sq79WfP1T9bn0PWsrwuJ2PPw4dSkOOnLtIVqNrGK_2YID_OPXcNawIxogTD_LXjqTawn5snBd56fjXjlTUDokwS1Qjb3VVShhr89JQ7A9TZ2WBjeMJn-1JHZSqtvnXg7Fn1aLzgsJGQaj4Mz48w92oouKsNkLddm8YjinnDolzMQhdMnpgl6KT6Yf3-8V-sFhHsDxjMjr29MbNF3VsQutEImAS8eYTeuOyKSCUYdmpY8cO8i9UhtBsVSjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویناک بیا تو چنلش بگو دکی پولمو بده بخندیم یکم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82836" target="_blank">📅 21:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82835">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ گفته میخواد امشب جنوب رو بزنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82835" target="_blank">📅 20:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82834">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEflZoaAo5sSjQSN53Zmhb0tOw6_Tu58DBQ0N4_PjR8u3zD8cwsHgVp_dkeyg_Ps9yNxTdmDV4U-5SuZIAHyFExbUY8mzIxMD1w583YeZ0MzkfF5N4bL868lsa8ykdyS2532VPCDSQjJR5qfosVPrQlnSI1JRDM-AqU5_d99Ntoss_JT1SjwBmvQmWVz2amgYIuwsS5wKhJ1Z2guBN5Pc3gnslqw-YkF1vxCFe6gxNts_JkyYTMSkDw75pDMhmyUrUD1RcXi-ta5FQk15vQ2mzI0E8w70p4YsbMeWk9DZ0Jg4zXVcM5Z2uxRSiRWjqu9Un9Bk6mb606wPsfsOQQyww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوید محمدزاده از تئاتر "آرش" به دلیل استقبال کم مردم اخراج شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82834" target="_blank">📅 20:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82833">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مسی از بازی های ملی خداحافظی کرد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/82833" target="_blank">📅 19:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82832">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دالر ۲۱۳
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82832" target="_blank">📅 19:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82831">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdHrZMmcaWXX_6DgB0ibtWpT1tdtJf3K8OW_I5aChfR2VEeJcQHvyAwL8aW_53mA2NZDUpKZBrtvCQX6cTU_8hqHXShFlMUCubdoP5PexXSzBbrQCMmvdIuE0RN91uquGRWmqGdr2CwJ37lXXJTrlUG1mdqE0x_ba-mEySaIa9Y02M4e7HgJ3kdYxMvv98h88UwIsfsEwL18ZBFOMhgx2iqDj1rWMFu1Q7NUeBRyH5lN43hVNmYlplVfuAJF7jt8OK3igRf8nBA2RV8mlIrZPDwet_4KJyOiD8QY4Ye7QQQaflKqTwtwvOihDBEoqgvrxA3VGkdPJcHrLf3YwsDBaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی از بازی های ملی خداحافظی کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/82831" target="_blank">📅 18:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82830">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hilHw6BLlKTxNBLFnooO4g9Az9oBhEBDdM0hcNOtIUrG0n1NOmfsL-G0Hf3yhKhejggbOROJ-5ToihyXuOgRajTUhgq73CNq_KtyLBh4KFpLBx-en0GbKA5GwC7-HlBgpPEdYjFfXfCUfrbs5VUdoeIFuxU9M7ZIrb3fdozOYw4Gt4kSmEprgCxc02Ve45v_cQXI4JBYqAh0T9sUu0L9O8QdYLLZBJh4McBdnV0lSYy9Yi_W2bTufuxJ6YpzgzJCKuvapCN2WwvBbgX8wm6da2TiH1jICTuG59s0LNAs1DZpcVK9KQgqzR3f2Qga7g6pMxthpySa2xjLBG6QFcbEWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخندم و رد میشم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/82830" target="_blank">📅 18:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82829">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">شما یادتون نمیاد ولی یه زمانی میگفتن تو ایران شاهین نجفی گوش بدی دستگیرت میکنن یا اعدامت میکنن</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/82829" target="_blank">📅 18:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82828">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">شما یادتون نمیاد ولی یه زمانی میگفتن تو ایران شاهین نجفی گوش بدی دستگیرت میکنن یا اعدامت میکنن</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/82828" target="_blank">📅 18:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82827">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/921c1bee68.mp4?token=FKL7SLNkF7nm9Kr0htTS2PLLjkFAH2UoQP_4bLlpCUki6l2xkdwsgQaux-JP4ezzHxXDJJzEuCETy0IhcBBrSE4VgwWNIJc_QsvKHvI611_0BOyuS1oG6Y7SgHoxxLEApV-HPdWJdOws24yAUqOyhqC8h-LWFd1eVxkpHFyd-qc1K9f9U2ESFFcTNZ5KYZtstfZ_y8_7OZSK080vd2QmYhAV6gFMwp7YKu74hSA2GHHkacNuWpP_blptyTYbGuFMMlWAlyiwmYUiqFbvPQtwVsQn49u60QQgOdE1jtq6Nkf2i7VfdhYsa7wVyMsIVD_rG_GVORCsQYYimRcJJ1jOwIczFoOsYpbXSD_V02xqcMNjv-LSmLi57D6mhlYqqgd-GX6EEbA9fUXPLs36nJHV5TfA8TqdB0mIo7ocmXmyXginCq6iJK4zhXKgxY249xVuoT2Aeks7wcJUUb2RMm0M-0-OXBMVzj8rsjIqGuRPi2lr1M_iqNBVvNbHTVtAOJjM_2VBD93ehodttMew9ZHRI8UgQ_p6Il0Tn8CTGaO8vTh5Q7h_dbeCLYUFZyYeJp4swCME7cyhN09pUOwDG6MS1i-WM5xuUwJJk6wO0BeNGAv0cPJLJ0qix2K6gCSkQICYB4dSzveg0dUDgw5Oy-0OdKu9JBqJ3KZu-AIheZwLMOk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/921c1bee68.mp4?token=FKL7SLNkF7nm9Kr0htTS2PLLjkFAH2UoQP_4bLlpCUki6l2xkdwsgQaux-JP4ezzHxXDJJzEuCETy0IhcBBrSE4VgwWNIJc_QsvKHvI611_0BOyuS1oG6Y7SgHoxxLEApV-HPdWJdOws24yAUqOyhqC8h-LWFd1eVxkpHFyd-qc1K9f9U2ESFFcTNZ5KYZtstfZ_y8_7OZSK080vd2QmYhAV6gFMwp7YKu74hSA2GHHkacNuWpP_blptyTYbGuFMMlWAlyiwmYUiqFbvPQtwVsQn49u60QQgOdE1jtq6Nkf2i7VfdhYsa7wVyMsIVD_rG_GVORCsQYYimRcJJ1jOwIczFoOsYpbXSD_V02xqcMNjv-LSmLi57D6mhlYqqgd-GX6EEbA9fUXPLs36nJHV5TfA8TqdB0mIo7ocmXmyXginCq6iJK4zhXKgxY249xVuoT2Aeks7wcJUUb2RMm0M-0-OXBMVzj8rsjIqGuRPi2lr1M_iqNBVvNbHTVtAOJjM_2VBD93ehodttMew9ZHRI8UgQ_p6Il0Tn8CTGaO8vTh5Q7h_dbeCLYUFZyYeJp4swCME7cyhN09pUOwDG6MS1i-WM5xuUwJJk6wO0BeNGAv0cPJLJ0qix2K6gCSkQICYB4dSzveg0dUDgw5Oy-0OdKu9JBqJ3KZu-AIheZwLMOk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Send him back
🙏
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82827" target="_blank">📅 17:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82826">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgRYHdi3oQc_G_VflZVn3GaJv8vBpPwE05BxBLdFaruNDk4ZbaqllxvpI79wN1hAoxa5akHb4HE-B6aY3jmypHSsJ481UqoS8hD_A3Ppkmruxh8Y8Or5mjnefet3pICG0IN0LMCmDr7Osb7DZsuPlcZ9OYvyCGi6UY4A4JgydFJTTXiS4mV0YVehppIKJhi-nY_CzuyxsaE1BiCSGCp4xKjGao_Y1hrmDLmr41V6Kf0fUj7Bg_YYw7bclvFST_FCNX-gt7jELJXSuwWl3vLtod7_P5YPVcoIXtVJ9Q9Ed2_Ajl8UhG38cdILcoDDOjfSQ94sPrD_RGoBLSt8BOePbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
استون ویلا
🏴
-
🏴
آرسنال
🏆
لیگ برتر انگلیس
🏴
🕔
دوشنبه ساعت ۲۲:۳۰
📍
ورزشگاه ویلا پارک
🎲
با بیش از ۶۰۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
⚽️
نکاتی در مورد بازی‌های رودررو:
در ۱۰ تقابل اخیر، ۶ برد سهم آرسنال و ۳ برد سهم استون ویلا بوده و ۱ دیدار نیز با نتیجه تساوی به پایان رسیده است.
🧠
به ساعت احترام بگذارید، زمان هم بودجه شماست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g9
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/82826" target="_blank">📅 17:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82825">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jc3i-g31bgNetgABN5ccBMZhMorQ8SPvsP900nEHCf4S_Av4dmvn2ejGpLicJViHyGR0j69cRalKsZ6VgKIoeN8XSMgdCozw6Aed5SbyXykmGOFaGN4lzgRYbCOmXB1zIaZnwBuxBMRgUMFid1Lvem4JUA4b_5XdFGr7Ihv2wAzM7i57dhxZSQbU-eAM3m14KSRFm4A0INdeOJv1Ze8axCz0ZBZyV5WFUP4M5UUPl7lea_DTxNpi8UdfKp36FZceSlqnq5-D9fsar_5hejeN2W5yyrguynVkohRjQ_5DkuyfFd_PMtEhTfc3oaQ8MqfrbO5sYQyWxdOaZr9RUSVS1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاش اون گوشیا رو بکنن تو کونتون که انقد تو خیابون از ملت عکس و فیلم نگیرید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/82825" target="_blank">📅 17:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82824">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9062dc2e0d.mp4?token=B11KHidgrtNX62s3SLwb5bAZBAMdX01dcQl0FmD6ZnA22q5Pq1IQMUUQ_mzq0ch5ZMZth2YsSYJZIrDiUOTjmsI_V7gDbZq01Jo_ialxpvsR0savUemZo8NJXmBA79izyZwA6X0DJRzGDuO5BWx3opyxGd9aTFZDltRK4GgEsjDbpXuD4Zd_XsvU5RqqcPmmA_Vc-3eAohQmN0ioVzHQU4qe8ePBWEpB6TBQZHuguBkN-hAlNlZFN2tshtCtsYDDvxSV9TYLWZJXDng_mS3Dec2pbC-ra7ivABG6U_mQrUImgdAJ4ZsAbq2QtrcNPmqZ-PV_Wc52aygC5jNrYNc75g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9062dc2e0d.mp4?token=B11KHidgrtNX62s3SLwb5bAZBAMdX01dcQl0FmD6ZnA22q5Pq1IQMUUQ_mzq0ch5ZMZth2YsSYJZIrDiUOTjmsI_V7gDbZq01Jo_ialxpvsR0savUemZo8NJXmBA79izyZwA6X0DJRzGDuO5BWx3opyxGd9aTFZDltRK4GgEsjDbpXuD4Zd_XsvU5RqqcPmmA_Vc-3eAohQmN0ioVzHQU4qe8ePBWEpB6TBQZHuguBkN-hAlNlZFN2tshtCtsYDDvxSV9TYLWZJXDng_mS3Dec2pbC-ra7ivABG6U_mQrUImgdAJ4ZsAbq2QtrcNPmqZ-PV_Wc52aygC5jNrYNc75g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوشآمد گویی فرشته حسینی به میهمانان شوهرش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/82824" target="_blank">📅 17:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82822">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5f3af0f50.mp4?token=qHFFgnyaL9e59KlAkJs4QocTp3tK3TM6My8cN6ucefEW-mSZIA_u52GCt6smDPQi3iPYo9sbsqSDzx-q2bykXtFFAaqYF4n-gazEidtsHNsQdgow4879j57cBpxbJqoi9IlZm9QcDmuZkkZu2t0eTIIFKPoEUTDc6dzmF7PGXclec5M5jpkqkwY5N7SPxy-pCXGKdKUr-KHymB3m90kdnP3q4tgOwopsQva1SOcLrxBQHsXsg11q7AgDg5VcWi6g54wdHeQMCP4zTtilFGZ0XpVzf8Y__pdtcaRTMzMrzr1SPOJJe39loily9wivrQHZUpFts6ROr8JgjkVGPVeRZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5f3af0f50.mp4?token=qHFFgnyaL9e59KlAkJs4QocTp3tK3TM6My8cN6ucefEW-mSZIA_u52GCt6smDPQi3iPYo9sbsqSDzx-q2bykXtFFAaqYF4n-gazEidtsHNsQdgow4879j57cBpxbJqoi9IlZm9QcDmuZkkZu2t0eTIIFKPoEUTDc6dzmF7PGXclec5M5jpkqkwY5N7SPxy-pCXGKdKUr-KHymB3m90kdnP3q4tgOwopsQva1SOcLrxBQHsXsg11q7AgDg5VcWi6g54wdHeQMCP4zTtilFGZ0XpVzf8Y__pdtcaRTMzMrzr1SPOJJe39loily9wivrQHZUpFts6ROr8JgjkVGPVeRZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه چیزی جدیدا تو اینستاگرام ترند شده که مردم  میان میگن قیمت خریدشون چقدر بالا رفته و آخرش میگن: «من اصلاً ناراضی نیستم، چون اگه ناراضی باشم میشم عامل موساد؛ پس من خوشحالم!» بعد هم شروع میکنن به خندیدن یا رقصیدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82822" target="_blank">📅 15:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82821">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKljnIGm8TrF32E2CCU4E9-EfGcIzgEbImlWZCJ8cMMRnw5dgH-A3dDOIRmyA3WYHvOtI17NJC-bls1Tck0-kNUlRP0rvgVl5pkUVKtXdn6Z2Yr6PbQOXa_1trTeSfZHj351JGOAFcd36HaxbMPORRFoe5UdNSJ1Tvvb66uAgsZs6FBIwaWbySwtWPplxkTSWn_P36oL64UsAqqtu6xAD78w1r6mHsGxgwY9ftjsOhLRIrODHtOqHex98NR2QbIj1uF1AYv4OOFIYmTfdlI3DJMUxYz6_gRGJJkIDwhtLVBa1xt5I8U4ZRp552spQ-93VU8JwbWAy7Qi3loFNPwy_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون لحظه واکنش پی اس جی که تصمیم گرفته امسال بخاطر تنوع سقوط کنه:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82821" target="_blank">📅 14:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82820">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7G-fHtA7Ta72cYSTriGvZQswNonJas5jWxAXbXhUSBSkS3SrLPdnbn6D9nBemnjmFn3qSpd6vlCkJq9y2fGTqWn5exNFzczc15rtJctfDlxyI2KmQGcYcAvhSqCngkBs_mNrZnWbQemuLliLEuLDb5hLBNjXypvXvq78wfUxrJgB4e5rtL9hfsyDRDxxmT3yH-xwK2eVK8zUSjt2ctiH4i1BDTkdKILwoqygHu4IB7TewUewJlrZrG2_yDvtv5GQYtNMlpyViXVe5Ik9xVHkVIBKEZ5A-1sUJ2scPeiMBQaTEzn7g65vccCsxN_NdBwGQ_EpAIg9HEYzqfrswYqzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی دوس دارم بدونم مالک این برند کیه و به کجا وصله.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/82820" target="_blank">📅 14:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82819">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">روبیو و ونس و امثالش کیر بسنت هم نمیشن حاجی، یماه نشده ترامپ ایرانو سپرده بهش فلجمون کرده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82819" target="_blank">📅 14:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82817">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sawTCpPiVpJEiMQPXO53gy0ZLvc2SeV3i8Yn8_a264sUYlDEObXK8bdWvzwgpFGjNVa3jxQYxiJ0ZabY34c3msScPeqXJxBunI58ZkSBuV6WoA6WjG_hufu8O2l7eLmCbKlkrtnpH3hA-GxLnTfUdUeBUpeBPa7tX69fFBiIMeBWnDFGJr4Q-HBP1-aDg_cA5_ofc7nD2XuKfrTpDs8ed-BvmdkafOr9w9o10berzzY1HMRgxLOuYbwQqTMMZ33RONViIs2MBnZzV0_J5U4dN-lMUC_mdf1yFtwO6jtTuJLYH3X9EOlnB9ht3cdSOmQd9I4YW9YuFp_iX8ALo2xbkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J3CtE_j0lwMNQ6bVKZ8nzRJUM_w7odm6r-ePYybiIfaJzNNv1jefa9cOkBqe_hthNcJZFtq46iKuaTlILnswqBZmbKsVPmTo8D_RjCO8GHaz1zsmq9SS-bFXFB0YlruANqvQDFUih03uNrAMmvoZvJr_xzt9I9YmZIDoGIfK8_AZHe4avKQrTqXlvgM2z6xNepTmUyXw5YYI2ErCov_7TeaRe9h_gYWj6-TlUZcS6ZMjEE6rzUvFTrj4GeBsaBb95q6sdN5JP5TADeGDbkYgIYSg0-h4Khp_U8Hv4oNW5xIP61-RUqJzgQRHQSgSBd4kT9pi8ft0qanlU6O89WlN1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کسایی که بیشترین فالور اینستاگرام رو دارن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82817" target="_blank">📅 13:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82816">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">این گربه هایی که صب تا شب تو گپای رندوم میو میو میکنن بیان براشون گپ اختصاصی زدیم فقط اینجا میو کنن
https://t.me/+CAwWLYMxGAU5ODU0</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82816" target="_blank">📅 12:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82815">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ul1Ae_4TGhn4E3q7aWEOeQ98MacVHutJNm7oczXvIajgFVCdCXD1shY8xmE4OdGP_0rnWyS1f8hbx8mruFMObtjPUguqZ7UTzxJ3E9OoQlA0o8Ffnf4pRMIuNHguSSGUjR107F9aiPMT46P0sCqdqKZtrI8Cw7ldSiXe0__353-HJwndWMz4AyEa1NbCsrPaAdiMMykk7QvX6DkSCpYc0T9MLA9zTg5rmwXU9dhFFdKrEBWrNa7oNEve_NBTcMTqIjSaDPjExDbZety5RGs-yO7OgwRcvKYNTSbSyPBNj4Xdb1jjmEljrvEo2JQVKUNDcfD3_7LiEDti69lTNeQi3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من به شما چجوری بگم این سلطان قیمتش با اف ۲۲ رپتور یکیه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82815" target="_blank">📅 12:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82814">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دوستان عزیز جود خیلی هنر کنه میتونه با فرمین مقایسه بشه، انقد با پدری مقایسه اش نکنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82814" target="_blank">📅 12:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82813">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CI6uqKgD5niUtBzX9ZasCb4uu_RnZ0GVoX5ygTtcsaGfBowd4WDyw8vf5KOE1kb3ZzPOynj73omicQQyxGm5HsRPZH1iNFsLKvegsh41boYjb3Toi8dSvtZtAzZw0DXzU-wUQLYeJzrKAFfxu8eA7iAGEbyJ4Wzo1I5AKXDpwY6DdJ7Vt25yY7QaaFZPlaC2O0OeH7ZSZ-xpQ9iP4RqI8RY-zc7lJ-_Hf1jv9Go-ZwizbiMAeSr-YfMVsYq5GJSEji8dbtZybs5RlETjfbYCRPhRotqdxWBKBnUDDoUovxyVV6YG1-CZ_r9_w0eiq0iDHqrltBL08chz7qe7fznTRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میترسم از خونه برم بیرون بیگ شگی بیاد بگیرتم ببره باهام فیت ببنده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82813" target="_blank">📅 12:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82812">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdZCGsQDmuQ9HHlctW5o9RRLytYUv_m4F4lpK413exH0IWSzGGb5-9jValRAVslb_Mu4VFudQfK5WKi-gH5XPrNUSz7fsb_EoRfJkCXQ5esxabH-xUISeWLAz95hT8fkVd_ARFZop337SSQ6SsZ6QQTztb5cDbBnBaeAanMqDABhh2XUyaKAAAYjB0vMFuL5fsnO3uafib2FRiAmh4wg0oxR9XrdyZSKzaxCnPstrJ-0YNX3pOVhb2wfVq04R1p-AWncpKObI9Rf1Lr1smpL-Ccv4vID6Q034MLWtkW3bVGpDTJnleOz_wvlyRRfSY19LFdZfgjNCw0x44q3txJ-MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی این بنده خدا رو از دهه نود بکشه بیرون به زمان حال برگردونه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82812" target="_blank">📅 12:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82811">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geSJB0J84ckm_NIkx1jcKQv2OqOkNMpETlg836GmaR2LV2j2zpCM3QyNP-IBdMG1KtSuRiiTApwWhjyPGjXlcfkWguI2V8S1KBuczmiSWW3Kwj9HLif2Bd2jBkxT1wkCxc0rhWZIRkbx9X5-Oi1DPFyRzPnVuWGNw8bzMroRN_I66Z2ySOTfTFPI-NUQCpxJ1lu1G_r611A0m_3r_wHCiRTJisPiVkj80CV9ix1v3C5ed3wK64kFpu6x2xG8P7yt_LFTDumEsqnASFy3GPJegky9JV4AnaVIYph_b3jppfKFk8duc-qaK6RCRFwgw8-f2Ekes-DW7nFiu8QNNL5PaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
استون ویلا
🏴
-
🏴
آرسنال
🏆
لیگ برتر انگلیس
🏴
🕔
دوشنبه ساعت ۲۲:۳۰
📍
ورزشگاه ویلا پارک
🎲
با بیش از ۶۰۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
⚽️
نکاتی در مورد بازی‌های رودررو:
در ۱۰ تقابل اخیر، ۶ برد سهم آرسنال و ۳ برد سهم استون ویلا بوده و ۱ دیدار نیز با نتیجه تساوی به پایان رسیده است.
🧠
به ساعت احترام بگذارید، زمان هم بودجه شماست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r9
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/82811" target="_blank">📅 12:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82810">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DB8B_gzyhNVyNw3q-HUMEtU6QsZi2N0q6O-fziqXroW44CZqiu5sPNEIvQvtD5uXAWdwE0ZT6zqQqIYVPGAxS0o8pKPeLywo9FMYtZYI0LeWxHPjBAZgUPeh1AtP6oh3_O7zRsiQW4Ah0Ah175Lni2DNNmM2K2mUk5hlOGrDTWGcObLkWi0j7kF_vc2jBFFjBBVRVs-JgeOIy33wagZ5dAejuCXToMK7tFkl_lxa7Z4vlXl5-KYJ9RK9op9rGvPmIsvrwUyIx9s2IcuFrHb5one3Wsesa56FHtTYSojHJ7OIO9Oe6x18TqRs1l7KXh3z4OSnLj-1jQijmgajZV4j_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببخشید خانوم منظوری دارید؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82810" target="_blank">📅 11:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82809">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ii1HZXlK17Hybucx-H4KliL6cVmXkFNAk15ibmET4QAf3p0j9ssubstKUczBstlmKN4qPLPL50NWwbrZMUaX6tGtMFFa9VOxUP5uWcn61_DrDSUpIBg11gjCUOOqp6s1_lwkk2iBaJwcES3rLZu9j9Iz7rSIiDg7Z8gHZSUYxU1Eapubl6d8GTLly-MStAgDMfbLDuNq5dum6Rqy0tcNADzeRgBTJac8e7v0XwkmutARmWD5fiAGlBW0oSCnZLxNQyiyrDtW3B7juTMtrIvjtHljz0qlfgMSEefqIGcz5jOu9HVp3gIUs0Rm1Jfaid0fsV3az3tt-eAjuG5mX7EEug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها دلیلی که باعث میشه بتونم این مدل مو رو از استاد بپذیرم اینه که پسرش اوتیسم داشته باشه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82809" target="_blank">📅 10:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82808">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">میگن تهران زلزله اومده، ما که حس نکردیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82808" target="_blank">📅 07:28 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82807">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دلار ۲۱۱
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/82807" target="_blank">📅 01:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82806">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مجید بیدار شد داره از خرم آباد موشک میزنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/82806" target="_blank">📅 00:58 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82804">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مجید بیدار شد داره از خرم آباد موشک میزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/82804" target="_blank">📅 00:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82803">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اسپویل از چند ساعت آینده:
ترامپ توئیت میزنه میگه قرار بود با اسرائیل یه حمله بی سابقه کنیم ولی دقیقه ۹۰ جلوی حمله رو گرفتم و ترجیح دادم مذاکره کنیم
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/82803" target="_blank">📅 00:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82802">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مجددا صدای تحویل ذرت و جو آمریکایی در لارک
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/82802" target="_blank">📅 00:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82801">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">#فوری
سازمان ملل:
این آخرین هشدار ما به تمامی کشورهای درگیر است. اگر دوباره دست به اقدام خصمانه علیه همدیگر بزنید به صورت شدید ترین حالت ممکن نگران خواهیم شد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/82801" target="_blank">📅 00:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82800">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اونایی که میدونن امشبم جنگ نمیشه ولی الکی وانمود میکنن جنگ میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/82800" target="_blank">📅 23:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82799">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">تسنیم: حمله آمریکا به لارک ۲ کشته و ۲ زخمی داشته
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/82799" target="_blank">📅 23:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82798">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پرتابگرهای موشک کروز ضدکشتی سپاه پاسداران انقلاب اسلامی در لارک هدف قرار گرفتند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/82798" target="_blank">📅 22:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82797">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">آمریکا پایگاه سپاه جزیره لارکو زده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/82797" target="_blank">📅 22:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82796">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">کوروش یه چنل دیلی زده همه رپرا رو توش جمع کرده
بعد یهو یادش اومده عه آرش سرطانو نیاوردم، رفته پیویش لینک بده دیده عه لست سینش لانگ تایم اگو عه باز یادش اومده اصلا زندانه طرف، پیش خودش گفته خب چیکار کنم حالا؟
بعد پاشده زنگ زده به زندان و صداشو ریکورد کرده گذاشته چنل.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82796" target="_blank">📅 22:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82794">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">می‌خواستیم به ماشین ۲۰۶ برسیم
آخرش به دلار ۲۰۶ تومنی رسیدیم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82794" target="_blank">📅 21:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82793">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkW7U-bfhCaMMiYtX30HzmDXk_rY72lLyG3rRRDZRDubb4V92Cj2-68J5XIOGJInOU4EZ8GWkfrVSJp9dcKOFe8xnI6H4T9Ldm-TcWXXG9K6VqedjpjYB3Q_r0ZeoWlGRxwGcNCm4RUMtHArjCRmEc9zvcjsk7xdSxDS-1yWpKr_lbxmOwkZW3FcOMVEYh8lltRAVQy2woRByJooa_HGSdn54xMa_AEmGMCulLbp-rgBXy26gIswddASgL6WMcDTpyO5SxJFbT4P7iTUTn1s9vH6miywHeKb7UkzTbmEE94NBik1eP7eidy3nATxfBkUb1RcC35GyFVJz94uwIKSHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حافظه تاریخی چرا نمیرسه به قسمت تجاوزا محسن نامجو، بابا خیلی عقبیم بدو.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82793" target="_blank">📅 21:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82792">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Gharibam Bahat</div>
  <div class="tg-doc-extra">Danial Moghaddam</div>
</div>
<a href="https://t.me/funhiphop/82792" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82792" target="_blank">📅 21:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82791">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrwPZ5mIRNPbObs1KPddqKS4ygyNc_qbz8ZNZa7-FOftGAe-G9gkepNATreh4w3SapyuWWLC1XS_P8F4jk7ZKb2nYuufhpEpuxPHR6bHOizz3uheIsE87nIE79rm9MEJHA4LouRuF7X_aKrrdQKKQxwph_Kb_ralhJS9QHe6Q24pLBs8WxWSlRLWt_kAwByG4uz8DS1tlZhkuBgS7P5P6026wB9Q1Sa7KLSnxC0dGtr4PUb0043nZBw5MmqAXRw_xKJPhpQszWi8Th9PZjx_GaEiXegsIvdgmWXXvCdxd6MmBbzknlqxZPfGxzzfIC_RnvQ8_6oWoo5pfWYaKYgkmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آهنگ جدید دانیال مقدم به نام غریبم باهات
از آلبوم خط مقدم منتشر شد
https://t.me/danialmoghadam3</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82791" target="_blank">📅 21:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82790">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">الان می‌تونم به جفری اپستین برا خودکشیش حق بدم.   @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/82790" target="_blank">📅 20:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82789">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d776d17fe4.mp4?token=ikZQrqZblM37svNzcumSBdD45EbELDy4pZPGxDdMaQEHtqzEpdfYa95m0zC0-Y2Q8khkaenJp3zMuFLDz03D4z976ee4R1cmaTxuoxvZbZLZvYDTmm7_C396mrclb-tkRDklgZhIUVjT89_6x7di_gSMqCrKiUXbmbl8EXihS4rd_oJNCDjbpZOVFQuRf97KN1Lz8pOFKhPK4GOS9TzL0HgQIjxrwpma03wkigBlQh0eLFclyewUtrQpZYEcWC9LX5DXys0une5h8UhQtwMkAlYkv88b6J7uCx98Jyu6t54UDJfVHbIoXSDSXbQN6zK1kXmnMkqKPvcCrjGfHbdjQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d776d17fe4.mp4?token=ikZQrqZblM37svNzcumSBdD45EbELDy4pZPGxDdMaQEHtqzEpdfYa95m0zC0-Y2Q8khkaenJp3zMuFLDz03D4z976ee4R1cmaTxuoxvZbZLZvYDTmm7_C396mrclb-tkRDklgZhIUVjT89_6x7di_gSMqCrKiUXbmbl8EXihS4rd_oJNCDjbpZOVFQuRf97KN1Lz8pOFKhPK4GOS9TzL0HgQIjxrwpma03wkigBlQh0eLFclyewUtrQpZYEcWC9LX5DXys0une5h8UhQtwMkAlYkv88b6J7uCx98Jyu6t54UDJfVHbIoXSDSXbQN6zK1kXmnMkqKPvcCrjGfHbdjQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان می‌تونم به جفری اپستین برا خودکشیش حق بدم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/82789" target="_blank">📅 20:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82788">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e9b9dca48.mp4?token=dAJu1Ha8DDazgjMfYSK9dKincRDJFF2CsV99IchGoZPECZOV1vhKva8W1NVT4o81l6lKxIjvb1kGFWXxdIP0oj2oYMea6Ns_mOZ795ASugx7v66apJhpymHs1EGrNjcnDBE8aPocijXJi5mU09uid9O-062HBrjywnGEiJ2RhOHQ6R6qR7F3A40jlEQ9cBYzS7v8NBf9MW-adUo7HrFl4jA7kEnkcDlOj7HN3u2ouwJD18i1eNfNiKd2bfVcmWqkpWu3avDX23MUfOU0VyDr4DJSycK4wS7GOZZyixQSo4vRcBZ1uqw-0d-cUK6ZhjFQq50ruFOs2N3gkAmmm2-orA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e9b9dca48.mp4?token=dAJu1Ha8DDazgjMfYSK9dKincRDJFF2CsV99IchGoZPECZOV1vhKva8W1NVT4o81l6lKxIjvb1kGFWXxdIP0oj2oYMea6Ns_mOZ795ASugx7v66apJhpymHs1EGrNjcnDBE8aPocijXJi5mU09uid9O-062HBrjywnGEiJ2RhOHQ6R6qR7F3A40jlEQ9cBYzS7v8NBf9MW-adUo7HrFl4jA7kEnkcDlOj7HN3u2ouwJD18i1eNfNiKd2bfVcmWqkpWu3avDX23MUfOU0VyDr4DJSycK4wS7GOZZyixQSo4vRcBZ1uqw-0d-cUK6ZhjFQq50ruFOs2N3gkAmmm2-orA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سناتور ارشد و جنایتکار و نادان آمریکایی، تد کروز:
من بارها از ترامپ و دولت او خواسته ام که به معترضان سلاح بدهند، تا مردم ایران بتوانند با کمک سلاح، کردها را مسلح کنند و اجازه دهند معترضان این رژیم را از قدرت برکنار کنند.
هدف این نیست که سربازان آمریکایی وارد عمل شوند، بلکه هدف این است که مردم ایران این کار را انجام دهند.
تصمیم‌گیری درباره اینکه چه کسی در دولت ایران باشد، از وظایف ما نیست، اما وظیفه ما این است که بگوییم دولت ایران نباید توسط یک حاکم مذهبی افراطی اداره شود که از آمریکا متنفر است و تلاش می‌کند آمریکایی‌ها را به قتل برساند.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/82788" target="_blank">📅 20:36 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82787">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqWGScJkH9PdMLp0HBqpgYcCQvOcS-ZpLXu1fRgX-xxhc8dTuytRLABXIH8BOfZK7dSq5pkLuQah1LWjhSTUnt9gdrTuTGb2W8BgLYNvopqOedugleBKQUd-XjbqcUYSY71lWQXU4tfh0_ei7iMRY58K-48jz4WjE6W-HqmHEA5JnGMwQzmfXtgc9nOBf_0QD5MQc4OAg_aRcHMPE4QqKBx5PIZQYGVghmY218jMtEH-AAWNhOMQBwNR1o28KD380LwTnmCJoS2AK0hyFn9iXPSIKJLpNCenAXNDxqdXuIaizo1jzGkvKn2FC3DEu4i5JMSgrEMqx77TGJI8_3-79A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/82787" target="_blank">📅 20:14 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82786">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvB_knmrp3qX-EGD7qAvuvjutFFKPTC7o3TGQnGbG66CTILgaAtCigF3kQPiGAeW9lzDaylEVyNlU5EDmo1-ZQPNhngACuBVUPosrq5_J6cjHX1I22Hw9AB3Ku3CUxuefw7dm1oPvnjb0EgNwcXwVzsXidNbdRxmG_n1jRZP1BIUlUXTmmwpBUHOJVxRiigApVXuGq5_MabvuZqySx5JMu4Iuxl1RBPYLYexJu6gJG9fLpynVyNVqS76-hq-2npC7H7ZVPBiI1CZM-a_5X0u7Dv3lh6PVkYx_-IMh1C8txEaY2arLPk77Lr1ioDHAiCzbVvQAR1dqnp8fmgBA63mog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زن‌نامجو: به بهانه بقالی رفت بیرون ۶ روز گم شد بعد دیدم با چمدون من ایرانه  مشتی حداقل الکی میگفتی میخوام برم مسافرت  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/82786" target="_blank">📅 20:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82784">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B7bTlcK64VlIcTZXsU165Ls9SsIDY60Vyf1o_awNaGwB31GKdIqT1nln2rrXhQs3MZAOiJ3cOkRtzdmx_xLeOvPxDTcvF7bmSPTXYnbmWQPoH58WhjR0Vg2jZWVUD9EHPgLltbpT0PDd04zuORNfmCOD_CZtoenBBVJizw4x-GByiY9_1KR-SeXpr69Me0PhJvT-GM6J7JGWO7tXivkfAUe6AEoxczXOZnMe0T5vJrMPOCL_5FqJ2jOZSJkO9WRZWImccLy9bYzeaH_xvk3nqBtzjuw8wyDHCe90Y-knie5nW0OJt0QkI88MGTFK8CqO7AE7pONeKBOAnki5V0CZag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DmeZ8TlyVYHZlsg2d4Iomcm2_sX7059Caojcb7qbndoA-MNT-fJ0MVkf4XPW4H2XjzEQO4HbSxKjIbvS4OUt9N6emvppJHnXLBMXT_AgJgHy_JuKL9fXesPBHP3liCg2rOsVFeRaFpT4oJCf8A95n8tsohS_3FAiOHfTjZ7eeaJGzQAO8L0TbK72FDvJjlevxwUGwxF2XOpUr1CNW2SSt1eN-BZnFFBzPXDS_v9ljK1LHoxoqrNYE7W5MzU007uHFe7PCPhgSnjTy7P16N9AEeI0Nqqp0d7ZrbHnwfkSzGAUjIGfoQNfRAuDlWjm14CfCQT5j65IpDQygOu6QjggUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتظارشون اینه مردم فتوسنتز بکنن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/82784" target="_blank">📅 19:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82783">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcoHhEbyVspfvhym7EC0itHSsXOwI9CV8DMLpJwvYeYD1jEbpUYzZXpKnst-1jlkEngtSdh6oUHiwqBfc5hveKoQ5U7KsVV-qSSfiBFMbXCZIwEF_KR441IhurZBckdu-M6Or1_W_ZgpC5LRgB-M8cgirPtHf5UBiupki5xWwsDnHVgGHY4jNTMk2DUVx6sSrQ5t5i_YgfJyyRjQqj_U0o8VndCb9Edy8u2IuRYthuYFO_FHcpc6aDFiMYZOR6AcYLGShDiQjEDvPcTW48dzd32N9qYbQLkutJ_s1xvgguj8RAjrlK7fLSbtjuObvDjK_IjUGTqiDz4ttpyHwu4j1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرگوسن فک کنم تهش تو همون الترافورد بیفته بمیره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/82783" target="_blank">📅 19:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82781">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OPTBCyxsGLFjlSOVo8igAlyqngWscMsYNAAeFP4dSkkqLB_xpeZFEAVl6a5oai0HKH-GLAUfSzXyuUVOwL7pNTki8kLJY60RF9qkuqu-6MxgnPHpfi3BHzguxNXXFI7uyuusPjiTnijD9lau4LHpTUdmacNarTdqTH1NeVsnxVDzLimgpYddrMTN1hi3d-dS7_hospkUS4akjI6GrCIc4SixSOlIUnv26Wl5BnvkynTXz_RsiSkx_90ETZgrBB_Z4BClAYojVAO_tzepfWEf2zxhNO99Pc95SDx3uJxh0HeXBPBgxrpgil5btImDVA1ny0h0SvsXGxI6wxAwmOeGig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jL9T5feTMzBbRIjIV5aBb2JoyajEm93ewEGUSjcMulL4MTMVxOc4Te4-ud6hg5e34pW844_rDtmrONPGShHfisnDDsjPbDLf2dsvs6A-rq3bb7Z5pi1C6mYiFm-ffgGCITQDOBM_cI-LHghblIxIdP1bJwnllbGquLOAhBj_FKJuQUqrP49und9c4mqmANq05MP5tXJGvGKTuzo_zFQWn-ThfN1A81_dUZHFw6L5bypwKDHUyKJEiGx0qJd-PCG5jPrxPvqxMD5XNKorWjpSspNhjtn-L0wmnxeYgVjuMdxulztjDcBBn6_pGflAeCSem0A9MgF-9WzOI-lm-lofyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حاجی انگار نه انگار که یه مملکتو بگا داده و الانم تو یکی از امنیتی ترین زندانای آمریکاس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/82781" target="_blank">📅 19:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82778">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کی میخواد این فصل جلوی رئالو بگیره</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/82778" target="_blank">📅 19:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82775">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">انقدر گفتن تحریما تاثیر نداره
اولین تاثیرو روی رپرا گذاشت، همشون دارن بلاگر میشن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/82775" target="_blank">📅 18:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82774">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5T6ly2E-BpTQJjhE7gAC0KJKsW3DRlgBit3jpmJL2ktmeOObnbhjcyrvQXnf5X9eZq5EELZgGDsYeSgFWgGB0hDM95ZiOxUGninysX9WMgJrxdoBny0Hk2PvENeXQii3iznw3ZMUtbiKAgO-MJ_jbQyaQLfahJGUKheGyRheFpN3KhQ0RVESRqOQoAOxSMSNXfmMFX7TGXYslKDKTqst21gNchMV56GrufIx0TQvZjgkny2o4g4JK1PuUMS75w5oUN3y8gEj0F7Rs7_96TT6ZOSGxilxX3mQsxto-Phh4m0dYrHuy7HNecnkgp6GUN2lZHGBMgL95rC8fRhEttAuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژابی بال و این حرفا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82774" target="_blank">📅 18:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82773">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tjs941IOhimWXigl9I-JBngfp5Wf1p9BYoswkJOfpctgVofzFGipPIX7NnJUV69SFGvtdBPomkxCwx7s2DxfPSTBjnTAdZSE80n-UZDfuGiu_-nqmpqWb0Nr938Lb9JFbwGJeJo0tJm-TWAvGo4O5Qz9kKkGoqB53O78Not-JJhj1rEJXRIuOjMvMYXRRcnI_QVTwilX-t7_t6UW1m5-s4USRR9nztyzsfwsH-SIY65i1H-Nz7mkSu4yQ6lF8Ap17_tTzdG-Iz00xGxOzirpngp2WV7uOsE0mb8oOwiuG2-H84m0-D7KqlY3J1ePktcJ6sH_tbVt1ZqGcGRr68HkGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال داره انجام آزمون تافل برای ایرانی ها متوقف بشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/82773" target="_blank">📅 18:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82772">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAt1xa5AyEAsfM_9GFtrNLrxfL7L-w7nOpzB_HmtXjM15KbKeCPnLlLqMXXaUts2n3Xr49CvCeyoWXyW_zb8Qvfg9utJe_a43JvduTgExMjaqX2njGDl8yxexfvlCVzBPcBMAe-04-5ShXbzJvXkB59uk6Uqke6cTlrXnYoBUPFgWi8yYDsCOw7agpE9Km1H-_szYLfFn0A2JSz3NtFPNhofN7NOd4r2wUtUg9NI6uo8h3lJYgQTdvibJyr2zuQndrAtzTfSnSIbdHOFLjkGBYPo4CKyxh4aSFrb1jOkLUPfcy0Ss6bJ_FGLcEuoQcr_8XW55cthJA_P6UzGCJ67ZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/82772" target="_blank">📅 18:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82771">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بیگ شگی بود خودش ویدیو میگرفت میگفت بیا پستش میکرد، کپشن میزد پول رپ پارت ۷۲۷۱۸
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/82771" target="_blank">📅 17:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82770">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">شاهی به این دختره شماره داده بعد بهش همون روز گفته بیا خونمون  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/82770" target="_blank">📅 17:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82769">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حاجی چرا خودش ۵۰ دوستاش ۱۵</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82769" target="_blank">📅 17:38 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82768">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAri</strong></div>
<div class="tg-text">منو ب چشم بیزینسی های کنار خیابون میبینی؟
۵۰ بزن بیام</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82768" target="_blank">📅 17:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82767">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">شاهی به این دختره شماره داده بعد بهش همون روز گفته بیا خونمون  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82767" target="_blank">📅 17:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82766">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d882fddf5.mp4?token=SuCXH66QLrgzGMs4p4J7oOJ2xG9jQsmN2wIbf64lEDnZ6UarA2edLFWh9KHMoEgTyP3n6mDHtdliUrnMopq8IzJvatGjcG4uhyrCUD4zHMvvE-5b9BZ38cqngZjwECGFYhhN7lVoeHWSfiO2woPca4V9zKfKInZsfOjTwnXBPwHn_mvZxMWal4RdHwprbf0xEmnF6AW3_UROJZdk_B6EIMcIky0r0dg3iRColM0vVq2veZiyXKnP6gBH7TJoXDRi8WGsrg4sQcq0OGVObPrjZO3Zji32qSlTXnXBE3_dtbCQMApAx1WmHCGI7zwNolrfCFpmHcQQhE8RtLuPom61Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d882fddf5.mp4?token=SuCXH66QLrgzGMs4p4J7oOJ2xG9jQsmN2wIbf64lEDnZ6UarA2edLFWh9KHMoEgTyP3n6mDHtdliUrnMopq8IzJvatGjcG4uhyrCUD4zHMvvE-5b9BZ38cqngZjwECGFYhhN7lVoeHWSfiO2woPca4V9zKfKInZsfOjTwnXBPwHn_mvZxMWal4RdHwprbf0xEmnF6AW3_UROJZdk_B6EIMcIky0r0dg3iRColM0vVq2veZiyXKnP6gBH7TJoXDRi8WGsrg4sQcq0OGVObPrjZO3Zji32qSlTXnXBE3_dtbCQMApAx1WmHCGI7zwNolrfCFpmHcQQhE8RtLuPom61Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهی به این دختره شماره داده بعد بهش همون روز گفته بیا خونمون
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82766" target="_blank">📅 17:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82764">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/408e06015a.mp4?token=uW4_NbpULSHOkPV_ou9Jltg_rrGvwFCJ3sTYssbNlGBBRIgcl1E6b4NcWDQyVOBpgokgLrau3qRW4fKv4cDCQsxFl4GMr8iFC1WCGXIhsPWGFeJsgRJfT-m_cQ41nsuiVQOF-2iz8xHJ5uuS-dvtUklIMlN77f3UG6t2TG6tPAcm_vZ7oGJokhfvNEgm7Mq-HyUHTrg2MUDTAWFKz3jPdqAuKFglPa3AXwpuNiorYYkqV2Nx4yrQR4MtFzH814B4zYTjzIxEiR182Lea3d1Zhd64odWRJAsEmSxzWUeXUNzI6t5lbHLLLK0Rn69SBnn6A9dDbra9RQEWRAwdYHbEsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/408e06015a.mp4?token=uW4_NbpULSHOkPV_ou9Jltg_rrGvwFCJ3sTYssbNlGBBRIgcl1E6b4NcWDQyVOBpgokgLrau3qRW4fKv4cDCQsxFl4GMr8iFC1WCGXIhsPWGFeJsgRJfT-m_cQ41nsuiVQOF-2iz8xHJ5uuS-dvtUklIMlN77f3UG6t2TG6tPAcm_vZ7oGJokhfvNEgm7Mq-HyUHTrg2MUDTAWFKz3jPdqAuKFglPa3AXwpuNiorYYkqV2Nx4yrQR4MtFzH814B4zYTjzIxEiR182Lea3d1Zhd64odWRJAsEmSxzWUeXUNzI6t5lbHLLLK0Rn69SBnn6A9dDbra9RQEWRAwdYHbEsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقا محمود زد به ناموست
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82764" target="_blank">📅 17:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82763">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ژسوس زیر دست فیلیک شاهکار میشه
بماند به یادگار
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82763" target="_blank">📅 16:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82762">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بارسا نگو بگو سطل اشغالی سیتی</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82762" target="_blank">📅 16:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82761">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">الوارز میخواستی بارسایی؟  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82761" target="_blank">📅 16:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82760">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DziPIJ-tNn7Y71EuixLzI90eRdvD7uljG6kW40XKOp9YslNFlz7m4BY7SsgBqNVPitLWDLj2YSJgfnwpQyu8nStYiUhXMBXySaWG3vIedV8OiFXEw5f6pnnEN42Xoz6me-Fqes0YoV1bFxRn3R85PaY0rfK_gbZLokds6MWhxssuy8QDnKEk4qPVI7xxCSkfuEFnV7pLsP0z7vdDemL7beUQkFyxSZ9RD1iIgoZN0_aMMwt_je6o17pkrTJ8zbbhS57v8mkmriupWTazz0kqjHITsDO66r1-0pWcOfthz0w1J8fQEM_nLeEwCdWENqK32jRH3rGsFToVrbunKcgIaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الوارز میخواستی بارسایی؟
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82760" target="_blank">📅 16:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82759">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUFfZr9RBiHjTB9Zz1sI2Eo8auR2cKIo3Fc8kwl6-4Gc77EyDL_naiz5mQGW-Ia1SEUIpH1i_2-h_VYlVRkO31zFh-mc14FXKiZ-N4v4oTxPKnHvcnNZ194AojcpThFsjaWrOiRDnUrM3d_6nMfPg5Ia9n_p_0WR7pBHmdVGEGFbX6dOX-aTpuIs6kuEX2pbtGSyGa7Y_tmvjFaNxly8R_mHA3ziFBlMfbUOkednNxei2_enSxkxyhGY7UoLLCmk7Xo5tGSO6NEF5Wc5K7dhWFcnR9vW_S0EGu5Xdc_2dWAQywijunENnP59aGZkZdQuMxspnfTQGpnM1AcYZ_iUKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ته خنده ای مادرکسه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82759" target="_blank">📅 16:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82758">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d256a2c699.mp4?token=tee10gfycY1I-PKdn2o4fewmcxpAIDPR6sjN7cbh6_2PyH8ZBOk2n0Hd5SwGwcIxo4uYrPKH14ac9ZUumc-oGKkZ_gYrnXjaDFXpfGvIMidoDUbD853s4GoRrGFoKh8r14cFABMHFqfkcqbNZQmLwiPDcIRbf_JuXy9XHZotvhoZzTcvT9UUDaEj_4d539xsNKLeLMUG_Ge_vhQlyE2Jm9nKy9N-y2SMYHBH6WT2Mog7ywM8-z_qd7AqudCw14xvkBmBoSnpDBO7UfgfNn4NE2yWo_NymOK5__aTZgNGHR3mo2go-gQ-gQ5ypI4lyYNrTUp04-4_7qOGcQsKae056A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d256a2c699.mp4?token=tee10gfycY1I-PKdn2o4fewmcxpAIDPR6sjN7cbh6_2PyH8ZBOk2n0Hd5SwGwcIxo4uYrPKH14ac9ZUumc-oGKkZ_gYrnXjaDFXpfGvIMidoDUbD853s4GoRrGFoKh8r14cFABMHFqfkcqbNZQmLwiPDcIRbf_JuXy9XHZotvhoZzTcvT9UUDaEj_4d539xsNKLeLMUG_Ge_vhQlyE2Jm9nKy9N-y2SMYHBH6WT2Mog7ywM8-z_qd7AqudCw14xvkBmBoSnpDBO7UfgfNn4NE2yWo_NymOK5__aTZgNGHR3mo2go-gQ-gQ5ypI4lyYNrTUp04-4_7qOGcQsKae056A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به خلسه گفتن چرا تیک تاک پیج نمیزنی مثل بقیه رپرا، گفته دیگه من سنم رفته بالا به من نمیخوره تو یوتوب دنس اینا برم.
حالا عادی ترین محتوایی که خلسه تو یوتوب میزاره:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82758" target="_blank">📅 15:36 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82757">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">حافظه تاریخی چرا نمیرسه به قسمت تجاوزا محسن نامجو، بابا خیلی عقبیم بدو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82757" target="_blank">📅 14:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82756">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLFJSJF8X_CIA-sFz3PJqQ_eH0xccHFTNXvuZSYBlox15XB5E6vQByN1Xih8Ot0zu6a1bBvSbkY7WeNEFg3WLEL1HwN6C6E1Hvjp_hbVmyf9x3LciBB9gtnihMbHzTfnKogLyX5i_Lo6_0Rx4lhTjo5bU4TYwTuoJMOrr9crkO_JgjtuXD07t0Fi5x2QXBYFD_lNe4964DpoKk6HUkVziZfFNNXvNkcxn9CRIRyzBA5gzTvjh2g3GAWL1-T7dhNi1N0awsSG9eTnzJTYa4RtMoiL2YIazNgJEsQIDFAtyFXVCdOF5cixpFtHLdzL-cFJXBVF_SvWAAZecfAc6hkAZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوریا ادرویت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82756" target="_blank">📅 14:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82755">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مدیونید فکر کنید این که مهران مدیری میاد مرد سه هزار چهره رو برا صدا سیما میسازه و توش عراقچی و دولت مردانی که رفتن مذاکره رو مسخره میکنه اتفاقی نیست
کاملا خودجوش مهران مدیری و نویسنده هاش تصمیم گرفتن اینو بنویسن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82755" target="_blank">📅 13:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82754">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">حکم اعدام برای ۱۰ معترض در اصفهان
شعبه اول دادگاه انقلاب اصفهان، ۱۰ نفر از ۱۶ معترض بازداشت‌شده در پرونده «میدان شهدای اصفهان» رو در مرحله بدوی به اعدام محکوم کرد.
بر اساس این گزارش، ترانه رحیمی، نوید الیاسی، ابوالفضل دادگستر، مهدی منصوری، احمدرضا سعیدی، مهرداد بوئری، محمدمهدی اسدی، آرمین غلامی، پارسا جعفری و مهدی جعفری معروف به مهدی خسروی، به اعدام محکوم شدند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82754" target="_blank">📅 13:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82751">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1de67eb81a.mp4?token=FaN_r-YEnMgt647c_8zYMArAqInmeNm_Z9Z7Dc_LDSIPe1rAWMKS0NBqL110NhUHTRbQFP14NZYSk7VtotSoRx08Qf_LYap0jLFNwZtFZ0ggT0XA4KEGmwdQ8x22Ojdqq2GQp4cCZjbznxWlSmmzKfEbWV2f1djxcSprB6FRS9WcFSRrJq8ulX_EdXzZ8Y8iKFVuYVQ4TnkS6NWGi_YuiSgtPJ5milMwRPiotk8fhXAkKcAqabmk5b5adWkIJd9zNwDCRue7N-Kv1gjeIokUxDPU39JvsMeo3VbHdPmy6AQzMjA1xLEPl36z2L1pI_MQA1KuDyuLEbmOQjFFH7NIuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1de67eb81a.mp4?token=FaN_r-YEnMgt647c_8zYMArAqInmeNm_Z9Z7Dc_LDSIPe1rAWMKS0NBqL110NhUHTRbQFP14NZYSk7VtotSoRx08Qf_LYap0jLFNwZtFZ0ggT0XA4KEGmwdQ8x22Ojdqq2GQp4cCZjbznxWlSmmzKfEbWV2f1djxcSprB6FRS9WcFSRrJq8ulX_EdXzZ8Y8iKFVuYVQ4TnkS6NWGi_YuiSgtPJ5milMwRPiotk8fhXAkKcAqabmk5b5adWkIJd9zNwDCRue7N-Kv1gjeIokUxDPU39JvsMeo3VbHdPmy6AQzMjA1xLEPl36z2L1pI_MQA1KuDyuLEbmOQjFFH7NIuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سجاد شاهی تو پشت صحنه موزیک ویدیو ترک "تا ناموس"
حتی اینجا هم داره کتک میخوره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82751" target="_blank">📅 12:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82750">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqRy_YqNuHeZDW1cG_ECSI4_H68mg9hg1BN55uU-j1c0iqSGlFvxJwi8xIcl067Ub_7wzSEvXNuFyCG83_SaVFgR2YUdHaB5_9opd8q9WhlFI22rakuvzHNGpDShHzC5R1bRcBI4YmrBImxF1604MuZ1hb8OqXaWP628PryJJZqzUtdSp1Lbdvk-pXkDPiJEBKrZOKo_MnfIDk-R1Rbr_vzkWT7QWdtbt-XjBENplZLidMdxclpQLz17dcho9Ku9wRnOFBEbAvJg0YRrt3nlOSxgKH5b6ljyEKPU0QTO1sCjcl-OqVHuOfrAYhlYrvj3cMTj5o9uOG0xDJUOybTHxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس پوری و مامانش
حالا سوال اصلی که دارم اینه چرا شلوار پوری جیبای عقبش جلوشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82750" target="_blank">📅 11:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82749">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">زن‌نامجو: به بهانه بقالی رفت بیرون ۶ روز گم شد بعد دیدم با چمدون من ایرانه
مشتی حداقل الکی میگفتی میخوام برم مسافرت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82749" target="_blank">📅 11:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82748">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59a6fa8663.mp4?token=WlvuSfGc6mz3qnFnSK78bbpET1mYDeBZsX_075BbXLnP68lhhzzkeojUYNWS7tzxlxg-jJlj1o80wMlV36YmO_N4rjr5XhD0HWWAP6R6AtenjovC9h6MysP9kRSYSBNGc4xuw7MeSZlfrOCPHiZGTid_QlQKl7kKvrQNTooJP4pPbRabIcljMQ2GCm7QNd6fmUYydpAS2uGFbG483-xBHcv3Jat-bZCvhVIzErgnMQarGnIOWMSQBgN9mquXNwamenGe_kJ8gdIFQ563uT0z2AZlDaFwAa4jVZAwaPIJimzwHQ-YkqsDi4-k2VIbB02jCxAUx0VVoSOMe8gSmbscBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59a6fa8663.mp4?token=WlvuSfGc6mz3qnFnSK78bbpET1mYDeBZsX_075BbXLnP68lhhzzkeojUYNWS7tzxlxg-jJlj1o80wMlV36YmO_N4rjr5XhD0HWWAP6R6AtenjovC9h6MysP9kRSYSBNGc4xuw7MeSZlfrOCPHiZGTid_QlQKl7kKvrQNTooJP4pPbRabIcljMQ2GCm7QNd6fmUYydpAS2uGFbG483-xBHcv3Jat-bZCvhVIzErgnMQarGnIOWMSQBgN9mquXNwamenGe_kJ8gdIFQ563uT0z2AZlDaFwAa4jVZAwaPIJimzwHQ-YkqsDi4-k2VIbB02jCxAUx0VVoSOMe8gSmbscBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخدا این آدم نباید رئیس جمهور آمریکا باشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82748" target="_blank">📅 11:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82747">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3fDRBRq3S8zZHuo7DeCTVR1XEz1C7-RIHZtfhwQ4s9IOZsxvjF1Bz2TFWu8LFF9Ps5b33Wnqbe_2HoSgviAdebNVK4W66IbGuha5Ri9uKv6WhfXK8_aEC7iJK9jc1AkcktMrl8nRw1FRdd8D3wPY7eMvOCdgszpHg8Zt-wnbHVglegeFWUbcTH4toJbiJhZhFwPCR4H26QqgrT8AuTTKRN8zPJR0HprkQsXGrKAsSJVaL5rNc57OMvVvrSz8T9qlewGXRypTsGnvnttk9UfCx4ryX51ZMagj1w3nqmmspyh7jA8z38R4hFK3v_rAmwanVx58tR91U5fCFcbIN62bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش این عکس حداقل واسه ۱۵ سال پیشه
از اون موقع هنوز ریشات در نیومده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82747" target="_blank">📅 10:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82746">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LL3ffCZhdtVTiUxNtSULHvA7N6K4wFISHyhwKXdjBAiEV_GQ_qW1FEQEetrXIxb3mslswRVujK_opUY8d6h-7ykdraHP9qz18jc_qew2m_0LNkyqPKD8makEPRDCUVQ8DZo5SnKA5bCbRFvS1Wp3n7Cxb_U5Q4HFAN_8b5VybaXP9AppHXAmMtqclbqJAXdpjy-WzgiIZ0QfAo88kfi8JCuuZ1DGpQB87qTAzmKmOCtZiU7_LBtycLN6BotEbXH3Q95Ybvq0mYhx7pftmR5q-JtAqi27gq81X0h_93T7a8OeMt66SSqKNJgODAuI9pzhswR7NbFMlQBsWRqUa5KRrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82746" target="_blank">📅 10:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82745">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGOCOy0vCP7iVw97b9LLh5S8h7OakkbThCMPV8Ai6ahEhKT9v_BBAwvzDz-NiYPQmGGEf6VasTCZ_zOO66ZrtDnPbmQHT5sfezIPSBeryv10Ts_v74FwY-QnzwfMJsdYCpMp1zs9FfP3kCKDO6kXqeuI2en3zn5YkSHiTqYnPonWhoMnZgheD1Ar0bDt4U9r08pJPpYtSuTIKu-mwWMlLa4g7Zl7Kli1XosjwAN-oCJwpLSJzczJ5fqy45oBIpQl2a0JXP6nzEBuQpJm35NMpeKMiSf96EYmbpm3DavBJVkZJpWL2U0ppPiWU6qo9L3nfOO55rQub3Y6vkb8aYh8BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82745" target="_blank">📅 05:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82744">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">جدیدا شات های کصلیسی بیگ شگی هم بیرون نمیاد دیگه، فک کنم دیگه دخترایی که میره دایرکتشون عشق میکنن باهاش پخش نمیکنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82744" target="_blank">📅 01:56 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82743">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGxRfAuVcFVZ7RSea-Hue4yHKmJoyPVj8ZQn79hJxyINH4e0N_9A38990VpZbcoAmKZxv1X8gViHwqthqeJEJWCy2IbqgGpbQnBAnGP6IJtMpd1Ex9uLVBgwS3atgQV2PbtviRBBdsSfY54wrBxrk9FWAMc7-GWPqgWBWIy-Vzj592bpZ9f8rBEvUnYUrvRsKbEqryTCKWljVuG_ES9oJn30ks_CZvcbxQ4nXkXUCsUucmeIITWUlZEnfmxLePgc7Qqv-VLPpSzSwePFmdokJ9WEbmwIP24_MFhH-ZBormicCfVuoUN5zd39GwnS_wrHqRL3cXLka4ImLMgcBJv80Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زندگی‌ رو دخترای خوشگل میکنن ما میدیم
یه یوتیوبر(aj king) میاد پیج دختر فیک میزنه با هوش مصنوعی و به نصف یوتیوبرا پیام میده همشون هم روش کراش میزنن و برای اینکه ابروشون نره کل چتا رو نشون نمیده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82743" target="_blank">📅 23:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82742">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11c692bdfd.mp4?token=sNOpj3AZsU1NcMnBNnQ3KqQMPNbqv3I-pDHWewMgPZBm5mNsDMmN9C6_uSYFt-eT0zvZ6H4XLPUlhJCm4zkQjiWDawrwbZu8-ae9GKTuYjvBZjtQviZkhF8K00M7ahugpieVG4y68rfWtRbmXhVhGZrHlGuZxP7exmZ1Ws5T7gBL8yt-U_Ho7at2yKR8yMx4fuNfXnYh4FlxXT8y22I9TwXVYY2Z7oOcvGY2xxxIzUYSVuvab04HjJF7-M7K6Rdr8rqXCr5ujDo-jf3KpdohjE3GZ_maazZIZZ62P5XSZ05veDSMZcYPF952b1i0AcgYq5FyViii5_zUw61YtZZ1Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11c692bdfd.mp4?token=sNOpj3AZsU1NcMnBNnQ3KqQMPNbqv3I-pDHWewMgPZBm5mNsDMmN9C6_uSYFt-eT0zvZ6H4XLPUlhJCm4zkQjiWDawrwbZu8-ae9GKTuYjvBZjtQviZkhF8K00M7ahugpieVG4y68rfWtRbmXhVhGZrHlGuZxP7exmZ1Ws5T7gBL8yt-U_Ho7at2yKR8yMx4fuNfXnYh4FlxXT8y22I9TwXVYY2Z7oOcvGY2xxxIzUYSVuvab04HjJF7-M7K6Rdr8rqXCr5ujDo-jf3KpdohjE3GZ_maazZIZZ62P5XSZ05veDSMZcYPF952b1i0AcgYq5FyViii5_zUw61YtZZ1Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فتاح سجادی رپر با استعداد نسل جدید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82742" target="_blank">📅 23:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82741">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cafd847a6.mp4?token=ZN7l-UxfPai0-0RtwSzKTSPzkVwHYAg8tlE7f6awqcB7Hv2Usn0NmVBRXkwnMzELHEbwY2QH8eRsMlSlQ-Pi2zqKrz7vkOwz6PX_-53Yx6CP7vcn8OzMjM6uWJ1Mcw_5jq96dOMTnBPHZVXPWhKshWQNFpSsmnt4oDHDflEDab9b0mGJz0LBWiaJ5xwMncbUbhHMcSMC66jm_x07yie9NIH1fuySvlB3GGKO3TPRt7yOUDc6TOxRkm_rNijkJfcnLprDeD-AUqszvCISYC2kmG_durM7jW8tCiYd4rnJwOHhk5Z_OA7UETazTNjy-bCSKnIzOvqRzvAHZXEWREgvrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cafd847a6.mp4?token=ZN7l-UxfPai0-0RtwSzKTSPzkVwHYAg8tlE7f6awqcB7Hv2Usn0NmVBRXkwnMzELHEbwY2QH8eRsMlSlQ-Pi2zqKrz7vkOwz6PX_-53Yx6CP7vcn8OzMjM6uWJ1Mcw_5jq96dOMTnBPHZVXPWhKshWQNFpSsmnt4oDHDflEDab9b0mGJz0LBWiaJ5xwMncbUbhHMcSMC66jm_x07yie9NIH1fuySvlB3GGKO3TPRt7yOUDc6TOxRkm_rNijkJfcnLprDeD-AUqszvCISYC2kmG_durM7jW8tCiYd4rnJwOHhk5Z_OA7UETazTNjy-bCSKnIzOvqRzvAHZXEWREgvrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارتون عالی بود پیشنهاد میکنم پیج تیک تاک بزنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82741" target="_blank">📅 23:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82740">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-BZfjh2UfP-SOb5wAIz8kmmubWnc-KxJ8Dheot6AgU8IvT8Mvor2WTmCpo5A4iUNNR8btrP9Z2r8-dKf1_f6utavtPUdRxjxGz8tX0g0wzHAKG_6cEScE-k_5D5NUto8YIYyInbDkFkYAUaqiTtZHJPNozqsSVt52nnGcvsKWsIJuSZ1_TgI7kq6xV6s2yqz-fhXzHr_zPpZb2Np6gb71JvhUTkS0PkadU69_Z47f19DEcuoFoyLGp6z7MmEmbZUFYrHq2WsKSMteoWsliQBYLA3J5bca7GvvQwSblP_7836k5bpfIwbPCvCgaoyWIVaaltXWulGG7jPZTdw-Blpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقیقا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82740" target="_blank">📅 23:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82738">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/732d114172.mp4?token=NPeNYvvn0hVyFuh2iatRBsFy23V4o1dmjdcQB4k-kIfenvfQPj5F3lGja6Fney71DWleli0EKAYivvakL7mXpalboCnEL2Vt9I9x8SXz4QzAsV1JsgyItslktEtjoORaQQrlw9gtqL-8V86PUFbdZvobmW9KGyqDSEKwBQW5HZ_4MV_c3NS0sDlecwRBQrjtkrRuoGT8A0a080HhWTllEXyLW_VVE6yhXJWTjN-fYUjwTFL0zMPXsuo3ml20VCc3hZDoFoYCCr7WejqEw_Sy_nMQ2Ej1UhNj4Hk9UcKRvUpdq-xSsrffry4w1SGxpW111bd0heOyZLPGDCPYH1QJiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/732d114172.mp4?token=NPeNYvvn0hVyFuh2iatRBsFy23V4o1dmjdcQB4k-kIfenvfQPj5F3lGja6Fney71DWleli0EKAYivvakL7mXpalboCnEL2Vt9I9x8SXz4QzAsV1JsgyItslktEtjoORaQQrlw9gtqL-8V86PUFbdZvobmW9KGyqDSEKwBQW5HZ_4MV_c3NS0sDlecwRBQrjtkrRuoGT8A0a080HhWTllEXyLW_VVE6yhXJWTjN-fYUjwTFL0zMPXsuo3ml20VCc3hZDoFoYCCr7WejqEw_Sy_nMQ2Ej1UhNj4Hk9UcKRvUpdq-xSsrffry4w1SGxpW111bd0heOyZLPGDCPYH1QJiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکار خلق کردی علی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82738" target="_blank">📅 21:55 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82737">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWlNLJtAeuIrFAI68xa_DV--Q9BD7fcolId1lLbh1iyFGlb3InnJ5GifS_xJHHvksIjhtml7Ir757TA9R-hTuNcuoawESNrMqhvTgzjaovGYCLRtlVomY5jA2Jbjqj0CXO0LMVYGjEDzTrgaZ9uXiuRkBqUHZ4zVT0pbOulC4flU6iryV-nLTIueyO0wBNgJxkwDkgIqArC4Fwh_ON5jVcVxTaTaBmEIUsSdAYTTINnCPcaT-81KmcFBXVPlXHHi-PXlRvPUD4Aicro3VcNk_uW2ufx9UZ6sX0qCDo3EcLWAg8rGMFmSIu0HMwDTb-wD2x1WVn1ie2i6T7cS-9CgHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نپال قبل و بعد از سیل
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82737" target="_blank">📅 20:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82736">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDl4BqSl-b-8VSwUQKb4o8xK1RPcTOBm2d8rZRkQqRQwdb4vbiaJFvJrRJdUbeA1IprkU-3XB-F5MJi95MGQSBx9wmrCNOISafqajXA-0mj1ySL3lglEM9JrI3weyw4aDtCf3gIYlnME0PmYU_z4qCm4VECoxrqDwMm4GBKiDH8jvnfNYQpODvGSHzjxMfCm2WxBaoBK_ZKBr-Il_tQ1CGBIk86yk2K3P62ZbbzbVkip0VEE_Uf7K5DOWSpnW6nHXet6ddmGNIkYEHDGglfaQ-6gug92aH5NFOtF-U-s22eLYuGXArzxFNc4VX8VdI4q_pf3AlggB0EfX9ACNrAgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسپلور قراره قوروق بشه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82736" target="_blank">📅 20:52 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82735">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7brLgj18rrUDc6a9mk7YZdRY18Blsf-jD7zgct2IHzG4huzTAHqGnhvrr_OsrMIIlx1RdKj8uLE-OM8OMF6OPj-Z1F3oLN0EW8B2NiEhMC-D5uTBr1OT8y_t44xCOCxNCGS9sRMHqqOdi6u1kJHqdlb8IlxYGSF-6D8GjioDdimo48y0_cmSuwSGvmQpE39z1Ozbr9o8P24Vl4Wlh_SY8nxUnQ74mUJ8__ewqojh9FjnhpG2aOd9j4Q9pu-fZ9ckRao-a1ETFKJWBE0SSOe1dVQf2w8hf__0Hix_cH1CTVJBtz11ZIzJhDznQmPHdvTRAfqF3V8z34voUCAyrc_rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوری ببین کاراتو
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82735" target="_blank">📅 20:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82734">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pN9jgZ4GHPW0p7oqO2gTQ9LqVNEzCzcjfDziUgLrga8n1owKpJXYaY6SAq10bMQF8xpRpFkb8kmJ1oHS2r59KF9cYG0m4yUYigdIlmTz8E3gF66D523mveMX7fSUKM8E5iA_O0nkcPDTl8mIxh0c7Cf8meHvq7A2a8wCnc1z6Rs05cmXM80WoEuJ4SYwXDCfQEUeoJrn-kKGn021n9kblDSAkZagCHQayvtWFdLvZslPo5CC_WSwRaH462cRKOgJ2fSwl6T9ObrG47n6LMfuTirBpUBvnI8hdRLr9xaEt-yMGG9tE2BbRP6TJmhlNOAQzK4h3exQZ4ldEljGpLhcew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تروخدا وضعیت سلامت عقل شاه مملکتو
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82734" target="_blank">📅 20:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82732">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prcgAwb9At-W6wWp9KJnHKK4pACZQJKC1uZzwT65BLH7UuIL_2DiLibatCDf84RZL56_z4rRDf2zqQzO7hK0qhX5RIa3Hz2kU4KaO1n3IjZ1dmRGw7kJaXKmPPlzAKB3kjtaH7J3HMmv81r1kdRf-QTUGzgztvSAZC33bfZOaUQ6Rvis6BgUsZ1gTEomqitMeEdpJtxwWW8HYFw0Ls8Lr_bPM2IciUSrPIDwWB6iRthk7PDdlQW9XeTOULp_uTvfMrViqmz4RzLFYB36whR4xaRV-K-Z4tvzoSgi8uGRXd8X46a1shvMe5uon-t5-UcGhrv3Vvc1g3O1OYi40KvIxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53fb725890.mp4?token=gLRTijiyGrdmq7jnsaKN9yQ_yI5s7uh-lAdH9lGpM0kLUzAWZOH0O9dXVaYE5nsoc-WXOwbnoBarKaoNIh40UlQl0GW8EwlhA4ZbKHXsHX0JU3jXLfDoWigJtzVbyCnptDRU7ZBk0JKe5lflsW-B1zJny9RX1Qtaa6WIzWNK0ZpcY2kCekH2l07Yt_g3ZRCH5_6e_rNlz8cJoTHQX9nVnYpqXLd9f6fCVvMwptseQ5IYb96Gl4QcVF7E_EBydVN9aV4Zo9pSTivKJR0-3bI8mMmIYP7XbJxcjQzfv09fDnUoSEZ31YO2Bo4THHztoxXvfQ_EfCUgVK_aef3kBBFRrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53fb725890.mp4?token=gLRTijiyGrdmq7jnsaKN9yQ_yI5s7uh-lAdH9lGpM0kLUzAWZOH0O9dXVaYE5nsoc-WXOwbnoBarKaoNIh40UlQl0GW8EwlhA4ZbKHXsHX0JU3jXLfDoWigJtzVbyCnptDRU7ZBk0JKe5lflsW-B1zJny9RX1Qtaa6WIzWNK0ZpcY2kCekH2l07Yt_g3ZRCH5_6e_rNlz8cJoTHQX9nVnYpqXLd9f6fCVvMwptseQ5IYb96Gl4QcVF7E_EBydVN9aV4Zo9pSTivKJR0-3bI8mMmIYP7XbJxcjQzfv09fDnUoSEZ31YO2Bo4THHztoxXvfQ_EfCUgVK_aef3kBBFRrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خارکسه تو خودت تو ساندکلاد ۱۳۰ تا فالور داری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82732" target="_blank">📅 19:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82731">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39afc7af6e.mp4?token=hhEQgwuXATtV83dLFVjEdRtBReLrBkl16cXrqs-Cj7CcexLeGNj2sVHRm8pG0hSCgQQJH-fEY1ynaDpxtMKKrdB-tFeHikqTnNssiNjfdGcVPTL5tkqQ5FwpyLgbFl0mNUg8iW0lPKgkPo84-mpBrMe-1fQgkOmlEyZWYOzSKq8-xFY4FnPFpaeOiru-fxzHO8Gxq849wIAo3PEP7lN3gcLjSeRPaQOfnceyG4UeBZpsh3pFEICA648j-iDxMCQHm1YiPpfl-5tdYRfvOGle_MwuKJRRsVPC23P1xrrM36CRQQyGpU9znZ1NLQ-hI7it1mlRor1xrfId3yeSWJCrOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39afc7af6e.mp4?token=hhEQgwuXATtV83dLFVjEdRtBReLrBkl16cXrqs-Cj7CcexLeGNj2sVHRm8pG0hSCgQQJH-fEY1ynaDpxtMKKrdB-tFeHikqTnNssiNjfdGcVPTL5tkqQ5FwpyLgbFl0mNUg8iW0lPKgkPo84-mpBrMe-1fQgkOmlEyZWYOzSKq8-xFY4FnPFpaeOiru-fxzHO8Gxq849wIAo3PEP7lN3gcLjSeRPaQOfnceyG4UeBZpsh3pFEICA648j-iDxMCQHm1YiPpfl-5tdYRfvOGle_MwuKJRRsVPC23P1xrrM36CRQQyGpU9znZ1NLQ-hI7it1mlRor1xrfId3yeSWJCrOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مادر چنتا قانونو با هم گاییدی دلقک.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82731" target="_blank">📅 19:33 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
