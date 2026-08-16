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
<img src="https://cdn4.telesco.pe/file/djbIAeR2SgH0QLY90ep8InQ7S2x7dTt7vaf_Hd-HMmhSscdnBW5BfC4NoNUSKPvBdhwvqIILWFpVpype44retZSXUP-l0ki5J8aLZjlzHvcDk2t7Bcwy656O9lFQJT4hzJP96DDam0LdYPoV5GVhFQHrQtqI9CTL9OC8Jxy6XBQZf6O4wWLLdBsFxWUpTrbihJ8TY_6Dvt28k5uFD81sGVsSmK19bIdlDuDuaAQ3GA640CBurIiBkQjllf7pU-6GkdusZiEGhfFyDeX491J7XFkfugg_6ntBAuIu-LoDR9ftQ6v7bi8nWt2PhsCmw6kc_k1edCcizgizQ7QSnYfQNg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.14M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-25 20:17:33</div>
<hr>

<div class="tg-post" id="msg-681749">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ggniwys4WWKrz3RsRzaQfSLRkF0sSJoww0q0LBIuaEno2v_EK40G1vSffAsVnMpOfq44tf-bXkqFfSIkjkgZiqn8rcgy2S3Yb07xt8csRRAU3CnyPizgBIKdMfnFtfe3vOHF0MWxxQzbHljYT6J5Kk7n5edN4c9NQw1YkzLo4XKSiLtug-tFXPR4BJGQXaXjNTH8YwMZRPkfgc3GGn07OqmrOZGa0HBcyIr6XUMpMuTrUUbysjxL9nBpzHyO42jpfy57XGc9tQVTQhHKsYZG8uX1tp84NF3UaUzl8hqOuEJcpMVpqcxvRzVTcSLsgB0M3UZvvRqe_bKNubBWRzh8xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«به وقت ایران» همچنان پربیننده است/ محصول سازمان اوج در صدر مخاطبان تلویزیون
🔹
بر اساس آمار مرکز متا، «به وقت ایران» با ۲۰.۵ درصد مخاطب در تیرماه در صدر پنج برنامه پرمخاطب تلویزیون قرار گرفته است. این برنامه در آمار مرکز تحقیقات صداوسیما نیز ۲۴.۵ درصد مخاطب داشته و در تلوبیون، در روز ۳۰ تیرماه، به ۱۳ میلیون بازدید رسیده است.
🔹
«حسینیه معلی» با ۱۹ درصد، «جام ۲۶» با ۱۸ درصد و «پدر امت» و «سمت خدا» هرکدام با ۱۷ درصد در رتبه‌های بعدی قرار گرفته‌اند.
🔹
در کنار این آمار، یکی از نکات قابل توجه درباره موفقیت «به وقت ایران»، این است که این برنامه از تولیدات خارج از سازمان صداوسیما است و به همت سازمان هنری رسانه‌ای اوج تولید شده است./ فرهیختگان</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/akhbarefori/681749" target="_blank">📅 20:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681742">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cEY5Jia4I-0bZZUWy-F5e2b6Tg4Zh1aiUDTwDB6KFxoL_8pienc33_5s0kYEBHIplHdzFry1ZyLRZFi784BKbbTUZG4CKPJmPHxXcpBbFN_QQcEJsg4bkFxo-UvltSLjsHeItb1wQXGnRiOmJbsqEbdTTlpVFcGefuPMRFGldtZ2ZHtrQJyDXcUnpwhBAbeXXaeijEEoGtu-Wf_d9zgnh3_Xq5W_huWZEQjpYcFD_dkuKjGtcynNQObFDlEpmI7JZe6IgUrgNwEecD4haYh_T0UKOWD0Oej64RSy_s4Ee72dnbjpuk-KY7FBl1ltGZbUDPRiJc5FlYwTndievWlQnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J4Fman0y--WdA1kuTpsv0AUb3MxYNNYYkiNInABvEUPaTDZEvBZCIVTmICPnjZIn8TbCkQ4b-bJYkqlZtnmJr-4wM5QA7IAmeSJTK1HgaYJO8dMciju8jIWDz1x3A4uIC_ViMA1ql_bfGumjx0xGQmiySgrL_KdDp41hfK2zuCMg5n0qbkCCOsNxgbI5uAmqngBCEs2NLRG3wfwB8MAGaP3-mNKElR_V7_exp9CPz-169JHWz8HuKTdQGAB_Ogws83Rp9_fY2jLf4NPY1yh2V4zkhm2Y2n-WZIxAP4fi0sg5M9NBM-4VXLykfAM94MGm3fz_yh5OE2MUgwvcEpYCig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lRwwtFyx9SeAPlH58nHklCO6qR4XB7XlDyN5hgPL3pBnkV2aifiHOhcImgaCZ5ZV-3AZuC-Kh_mevLjaDgTx97Ug5E2pC79u6tjPGxj6fUUTRECZSAS4rFSHejBUjntEVmn55lIQZ54v8C7mSBZmOAnfnjIP_oxnSBH6SHflE51iIDw-pyvZybKAH5J5oDlbU_02w18263p1wY-mNrzT5eGtvmHbQpkNZUlna8EhoqVaPiUA--dibN_VX6tvOs8mcy2EVZz8fui6NgbDRyAhbqoXhFxl29Ex01HVAyKgHpqgwKPCbhdjtYoq6gNDsPuQd_e2u0UYp6GdN3e92Ac8mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OsBj_Rga1uNtTgttyG7tHJRdRX6RqKjhLMmUdVobydAoCiegag4vorZTX0OJXgTLMgxHjWQ9GBFvYt3tyWZzyRFGNHMcSQKPpdXjBQGemA_5Vc3CIU_c-wT6LVY4znQXg-fAYmcEHK-3pRahKXXwh6srHJwTN1k-_nS2s6pHcwv-qA3YToNJEsUx8l3tSuLksPf0X1kYYhM4yqqQdIEtFvhmKurDChU0lisFkmtAq4XJI8a153zzi9UhtfjWtkcRXQTaJ7D1kuMmzRQQiuXebjJqiIhG-VEjkAKH5mNQLs9dqkk-3bCQHiQ4tlBhnktD5hnDqxQ5wzqmQORR0HeuMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QAX5ePkmEZSe3KLAH4d7Ub7Pt7JVOInCP2lNi8MYyirty7jN9jZ0hzOfiakAuc1NpjWSr5XE6XfkU5yfom_A3-_DSJQbRTTZ96Lxi0t1gFeAMTdPLIyfBerrX2P2N1h_slHBaUwpl9mHY4wjmILgBbXu6dtI5_HpI87riGxuNVoSFtVySjyTarRLiFTEOcZGxMYD6hutI4s6Idg4IgMK9qoxyz-U2UJKGPbWKmFE7-iOr8XjkSEVtFGPW4OSv-1i2n1Uw9vN5-oi0khKmQkR9G0Tq5JqyNm5kdOjRfhJywIrDhfZkEaXFzQGHz3IZBfaIn8FQ0slOugip_njyr4eYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YgogEnUd7e_pWud_izbpGQ02zGI67v0tZNcErpbRZd705YLI_pu-sQPk1yNyRMmVbvDACLWwZwbyv4uspgB9MtFrQkbyBchk3U3GYkZStKjOkW2DsVHbY9VOCX_KySCzAdP0eGbryU30UzQ-OLd76ScSjAxZnuIOmuhJGC_AlmyCT5o6YlfmeFkzIZsNGX0iRXm0sLZS5VBTjahs-NLccE3JGmopZ6N_Nr5c3KYPzJ8kFzJthS9joPJJTWtN_Vw7YkHLLO71C3SA1mdCRTl5U4UnJLpouZXU7DdmrdbEZc8wIopu1yljtMWyxAVs6zRWLYZIETYYsBbKzW6TxCKqOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bNU4BFL8tY24F852qp7ZHauGeSPc-Eqb5Pple-jgTHZgFZfSINJoAOguDa3dsI6XXDpl-MJYywciIRoHuCstJeyIxo8ezSsZ2rQ84viYxbkPuiwWO2JRaKGujX_NA9vXVg01nTJWtZfHHPcplLMfnAqhGBFozJz53Ubb5bIoqfOgNF6lKHy-uzP-uHWp436UWmdigOtyUXa1_mlFBwW8e8x9Caf87naJ50kUfVA6BLX15iPx5IChJN4qb2fXFJkFqkvG1sxIhccIvN_aruOfL9kCGyMn-cmcT2aDa8yCANx4TXyL7EHkwlxsj83_4F4YryE2cuppw9ks6v8bIIUcXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از جلسه هیات دولت که بعدازظهر امروز یکشنبه به ریاست مسعود پزشکیان و با حضور اعضای هیات دولت در نهاد ریاست جمهوری برگزار شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/akhbarefori/681742" target="_blank">📅 20:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681740">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MR1RVyzGc9EMiSR0l2T35Eagl1QiOgrKyqQ4SsG4z7uGnfysZ1XnfcBEsaV48YvWO7oS0HxiUWAWUms-gVZdLYxGpZQFkhg2k5Vz5zUGL75965s1HwSgC0399GsSgVVaz0Y3ETnKzlYAh9NStoMMPPfrWY7seggDN4Fn8HfLxEYr-vKdaU1S3jJtafGKAYN5iSSw9mMrEjS8Tlnj11WkOQoXWTzjAytwGibVkv9TW2UVfomViqiKn1KWx2bO-3Giv1eNkc8KnrquyvYSmJaPEooq9nNPdjGCcCJb3BGX7ZCn4eqhXggWMBTj22KWAwdNb_IS7D48rFgcFpVONkkR1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jfFWjSH9SJbWAoAP-aqSLYVADtSO1GwfUL42mFGlnF27HqXoP-GLRsg4jMQRHX153pe6TprEsZFnynnF8Vtf0ollonVxfUdCY_YR4TXOn0MljikcnCilKGwpNqvELT6OKs0MvF0yJ--abYPGauTO0BmT87EiuMtXI0HQkEknmU_LcGNWdhnjI9DW012aD_0LrGlZ6KREzIhs0Qxo2CjkpDIoeVwf9HvZHAsDchrg3Gu7lKWD0fyyjwOwTVQ3agWfB-cFSH9ctqT10AEyIIG_1BfXpEsiSLSuvl0-ugeeePd9FEZEzFjOGC8bpC2kI1nB_O2FUutz8m78nU2XKXLXFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کشورهایی که بیشترین فرصت‌های فریلنسری را ایجاد می‌کنند
🔸
آمریکا با اختصاص ۳۶.۸ درصد از سهم بازار، بزرگ‌ترین ایجادکننده فرصت‌های شغلی برای فریلنسرهاست و پس از آن بریتانیا، کانادا، استرالیا و آلمان قرار دارند.
🔸
اکثریت قاطع فریلنسرهای آنلاین در سراسر جهان را جوانان زیر ۳۰ سال تشکیل می‌دهند و «توسعه نرم‌افزار و فناوری» و «خدمات حرفه‌ای» اصلی‌ترین حوزه‌های فعالیت فریلنسرها جهان هستند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/akhbarefori/681740" target="_blank">📅 20:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681739">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BU5bKugYiUHpl3muy4wSVhAtDPxBKGdjZvRY0EE6Oj5pHfHiUo4XjyUzyJpU8aJBYWlpJ01JGyW_52AO6rHE1yRxO4QPH6fkmtzg1adKDqhDdL_7KdEOKth9kBo2-MjyMs3aI7v5u9M9oFLwHVCiGJyMpUx7g8HyqGIOj2dS_da08LjgSApe0m4xyzVLB_R_xFuqnaEgA7pff0hMtg1P3yL9U31Uch1gfMfz59WjdNuOvl8qNGe0FGoM2ToRtZzG5m53zWr9c-4tz0_bQX5ZDKXWDdWXMosftxKaAmRxeZOw_c9kgJv5FpiJag8141Wb6_puUG-IF9Up3oJNBeIcBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غذات شور، ترش یا بیش از حد تند شده؟ هنوز برای نجات طعمش دیر نیست؛ با چند ترفند ساده، تعادل را به غذا برگردون
👌
🍲
#ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/akhbarefori/681739" target="_blank">📅 20:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681738">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkGyb8Jk-qogAyYOOC3xn6xxGYoFCx4UheRwnZ3vPGrsqUMF39kilTkTbZi01UEQ8aOBjf3LnOFshayn6qQKraHQKZgVcjyzxePlE0H6YP91Hw3mVXRs0ChgyiKCnsSPfdIbXg4MRqsuorV_3c8wRQfqpllwX-0y6_ocr4eqeEb8je7GF6R837aW3QRvM4Otl0JIp4caG8iguvar1Y2cKqcr1Youj2y_Bfp3eIaHZjHwGzv1cMjSxgXP557O11Rxr40d8pMKr68jKaReGdlvlWIUhK7DH1a6yQf3bbI1o3Wa4qf6Sq9GxWUEn3laKfccMElLxBqUSahSlWVqpkR4ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خیابان‌های اسرائیل در سایه انتخابات
🔹
بنر تبلیغاتی حزب لیکود، حزب سیاسی نتانیاهو، با تصویری از رهبر معظم انقلاب اسلامی، زهران ممدانی، رجب طیب اردوغان و شیخ نعیم قاسم و این نوشته در خیابان‌های اسرائیل مورد توجه کاربران قرار گرفته است: «آن‌ها می‌خواهند نتانیاهو شکست بخورد؛ پیروزی را به آن‌ها ندهید.»/ خبرفوری
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عبری دنبال کنید
👇
@AkhbareFori_HE</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/akhbarefori/681738" target="_blank">📅 20:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681735">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlmfdOU60K7mpHl9KKbFvFdtL-fXYowJjoUuLPVTy2Uc8LkBM4Lz7XuDeaXp4raV4OR-5QE__ZRebZnxkknA4r7aPpIvYeW-A--iwf3QOpdWHBunuJDfZNWuIF1aK0K1hiH_3h70Wrg7DKJXjTWN1IYv3Of_kfPgav1fXjhLIVOrq0a2tJjhmJh_JWw-2x7Pjo-47c4lgMr4jlI29e2nVXEAfELEY2F32kVrDWm-ExOKOeXMXb6nCTj2tI4g-BxxxkVbQA7kL3YnKwtRBfXBeUahIx8xYRvr-i7m2v2RU6Ncwg7yWRF3RmUhJ3bpQPxA5lX6jXmB_eHIIEIZUECf2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ae368fe54.mp4?token=AIagbqTDEMBWihVPKRNXv6b1wsiN0FGRJWwyszjz_aIHuWZgmwU135-as9d3DX-3NVcj-VN6PZt4h8zV2Hjbsfd7D-_TyoRAemG3aBB3gkBkm8VjFeNMJsh7gPQGOtEfKIqX43IsvrYEsjAmEiU8n9OSNHaakEm1mqzPbCYtVsf8axIl2paTOcTYWasrD0ETG4y-1WJgwo-9kg1Hh1h-XMtljuQPxS1xB2R-BM1Iz6LnxfUZl_ex_yTe5yliTLV2CTt99G9BZAuVnih5e3yYu6MRznf01QWytXW623aebDPbgT4jB1ZOxYjNrwbP-Rtisr-zWWFth7bCIKXAAqR1UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ae368fe54.mp4?token=AIagbqTDEMBWihVPKRNXv6b1wsiN0FGRJWwyszjz_aIHuWZgmwU135-as9d3DX-3NVcj-VN6PZt4h8zV2Hjbsfd7D-_TyoRAemG3aBB3gkBkm8VjFeNMJsh7gPQGOtEfKIqX43IsvrYEsjAmEiU8n9OSNHaakEm1mqzPbCYtVsf8axIl2paTOcTYWasrD0ETG4y-1WJgwo-9kg1Hh1h-XMtljuQPxS1xB2R-BM1Iz6LnxfUZl_ex_yTe5yliTLV2CTt99G9BZAuVnih5e3yYu6MRznf01QWytXW623aebDPbgT4jB1ZOxYjNrwbP-Rtisr-zWWFth7bCIKXAAqR1UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره ای از آثار حملات یمن به تاسیسات نفتی جازان عربستان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/akhbarefori/681735" target="_blank">📅 20:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681734">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
پزشکیان: کسانی که در داخل کشور ما اختلاف ایجاد می‌کنند باید بدانند که این کار فقط به نفع آمریکا و اسرائیل است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/akhbarefori/681734" target="_blank">📅 20:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681733">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aShMGDEj0sMHzU3TplYjCGQfXhzjnumfpe0YPFVz4dEUiAuJxz6DAgnX6CDnsbtES8J1FnXImPgGO5QnrO7g8I7HVXfEhMHUH9XtVBy6t8B9wKkQNdJbFoeQa24-8YGehstPF2-RLdKgzTVzQOwliskERRaCO9NONusAUVsqCCE3VnLW0WYtQwOaxgh6zaJV-mICWOAjIhpltktbWc4l_dldGJL5X71AeO59Li8VxJJIu3SZONjkgdn-5cao3qxHTuqz7JYJna8BhrlaJ4K5QO9202yfJqB6OWbl9Ux-k1NDhUbZYvlsfLc-mrV2QBYeH1WxI1QsEl5qK7ZU0kB7LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصمیم ملی
🔹
مسئله بنزین دیگر با تصمیم‌های مقطعی و ملاحظات کوتاه‌مدت حل نمی‌شود و به یک اجماع و تصمیم ملی نیاز دارد. هر تصمیمی که گرفته می‌شود، نباید بار آن ناعادلانه بر دوش مردم باشد. اصلاح قیمت، اگر ضرورت دارد، باید همزمان با اصلاحات اساسی در نظام مصرف و تولید سوخت انجام شود. خودروسازی ناکارآمد، خودروهای پرمصرف، ناوگان فرسوده و سیاست‌های نادرست، سهم بزرگی در افزایش مصرف دارند و باید اصلاح شوند. همچنین لازم است توزیع یارانه سوخت شفاف‌تر و عادلانه‌تر شود. مردم با یک تصمیم سخت همراه می‌شوند، اگر ببینند همه در هزینه و مسئولیت اصلاح شریک‌اند. بنزین نیازمند تصمیمی ملی است، تصمیمی همراه با انصاف، شفافیت و اصلاح واقعی.
🔹
هشتصدوسی‌‌وپنجمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/akhbarefori/681733" target="_blank">📅 19:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681726">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
پزشکیان: کسانی که در داخل کشور ما اختلاف ایجاد می‌کنند باید بدانند که این کار فقط به نفع آمریکا و اسرائیل است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/akhbarefori/681726" target="_blank">📅 19:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681725">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
حمله روسیه به تاسیسات تولید شهپاد اوکراین
خبرگزاری تاس:
🔹
وزارت دفاع روسیه اعلام کرد که پهپادهای روسی به تأسیسات تولید و انبار قطعات مربوط به شهپاد‌هایی حمله کرده‌اند که اوکراین از آنها برای حمله به شهرهای ساحلی روسیه، کشتی‌ها و زیرساخت‌های دریای سیاه استفاده می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/681725" target="_blank">📅 19:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681724">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tO1G7LA46oLlBGR-l47h8vNB4sVXZnPGEryFwX8de8FaPRzbEiH8i55wRoQIwP4bjErg7LV8n7qC7B5265onjmADcX7p09vjmJqUdr8YdQJHY3lyOvgURKXMfB3yqG5KSsmmdYv5KwLxp8EuJNkCAxr2462qDu785mA56gJdfR3-P51DkBipyyzNAqzVIWDaTOculcBIEUts077E411pQdahPbp-FpxUkB8q0KL7-p-zk2RHE-SwSlxwU4LUoCWvBCAJfNo2NZF3wqsyiP_SGLuF2CbLNcESU_gnKxvQk6sKmX3l7gw1a4OH1dbaJHcD5LDvgk2D01teT5KoAHUJIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مصوّبات مجلس براساس نیازهای مردم و معطوف به امیدآفرینی و آینده‌سازی کشور باشد
🔹
لازم است مصوّبات مجلس با مسائل اصلی کشور و نیازهای مردم نسبتی مستقیم و مشهود داشته باشد و معطوف به امیدآفرینی و آینده‌سازی کشور باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/681724" target="_blank">📅 19:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681723">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
بلاگری که به مقدسات توهین کرده بود  دستگیر شد
🔹
در پی انتشار ویدیویی توهین‌آمیز در فضای مجازی از سوی یک زن بلاگر، با دستور مقام قضایی متهم شناسایی و دستگیر شد.
🔹
برای این فرد پروندۀ قضایی تشکیل شده و درحال رسیدگی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/681723" target="_blank">📅 19:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681722">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
کالابرگ مردادماه برای ۳ گروه حذف شد
🔹
از مردادماه زمان شارژ کالابرگ تغییر کرده؛ گروه اول پانزدهم، گروه دوم بیست‌وپنجم و گروه سوم پنجم ماه بعد می‌توانند از یارانه غیرنقدی استفاده کنند.
🔹
در نتیجه، سرپرستان خانواری با رقم پایانی کد ملی ۷، ۸ و ۹ کالابرگ مردادماه را دریافت نمی‌کنند./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/681722" target="_blank">📅 19:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681721">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رکود شدید بازار لوازم خانگی؛ مردم به جای خریدن تعمیر می‌‌کنند!
اکبر پازوکی، رئیس اتحادیه فروشندگان لوازم خانگی در
#گفتگو
با خبرفوری:
🔹
افزایش قیمت کالا، کاهش قدرت خرید مردم و شرایط اقتصادی باعث شده بازار لوازم خانگی با رکود شدیدی مواجه شود و مردم به جای خرید کالای جدید، بیشتر به سمت تعمیر وسایل خود بروند.
🔹
فروش مستقیم کالا توسط تولیدکنندگان و کارخانه‌ها در فضای مجازی و همچنین گسترش فروش اقساطی توسط فروشگاه‌های بزرگ، سهم کسبه را در بازار کاهش داده و فعالیت واحدهای صنفی را دشوار کرده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/681721" target="_blank">📅 19:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681720">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c80afa8283.mp4?token=OcM_4FKqZvPy0HmwSUhnDIMOQkfHYgekO1tv02T3-5d01AVXWCFXtwvpexPdyhwVAwfK-rR5goFM-zAbn0K9356vAaAMbNjtonLEEFvtU0Xf_0Mpdqnq4qaoXIFgLkJz4fVHRj3OmBZC_JkiMyVup1oqY43Og0wWJZaUO76EuDPQKmlL9ExwqyMfMx-C4JmvJFb78ggY8L-ANrqFZovkdgNXGrqjR6_ZcX0XobwQfaLFtzYvtpEqmnjMrWiF_cmHwFa9ud6oCD7nDSD9bZcah52Ui4MYkjlltKqpNYamzD1X-e9ZSCwyDshOSKpSWrq5V9dC-IwStzuw71DMMwWmXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c80afa8283.mp4?token=OcM_4FKqZvPy0HmwSUhnDIMOQkfHYgekO1tv02T3-5d01AVXWCFXtwvpexPdyhwVAwfK-rR5goFM-zAbn0K9356vAaAMbNjtonLEEFvtU0Xf_0Mpdqnq4qaoXIFgLkJz4fVHRj3OmBZC_JkiMyVup1oqY43Og0wWJZaUO76EuDPQKmlL9ExwqyMfMx-C4JmvJFb78ggY8L-ANrqFZovkdgNXGrqjR6_ZcX0XobwQfaLFtzYvtpEqmnjMrWiF_cmHwFa9ud6oCD7nDSD9bZcah52Ui4MYkjlltKqpNYamzD1X-e9ZSCwyDshOSKpSWrq5V9dC-IwStzuw71DMMwWmXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران؛ دلبر سه‌رنگ من
🇮🇷
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/681720" target="_blank">📅 19:17 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681719">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
واشنگتن‌پست: کشورهای حوزه خلیج‌فارس در پی اخراج پایگاه‌های نظامی آمریکا هستند
روزنامه واشنگتن‌پست:
🔹
کشورهای حاشیه خلیج‌فارس به دلیل بی‌اعتمادی به راهبرد جنگی دونالد ترامپ در قبال ایران، در حال بررسی درخواست برای تخلیه پایگاه‌های نظامی آمریکا از خاک خود هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/681719" target="_blank">📅 19:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681718">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
رئیس سازمان غذا و دارو: در سال جاری دو سوم داروها در دو مرحله گران شدند
🔹
دارویی که با کشتی به صورت کانتینری ۳ هزار دلار حمل می‌شده در شرایط فعلی با ۳۰ هزار دلار به صورت هوایی وارد می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/681718" target="_blank">📅 19:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681717">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-ml31d9E7wSy0jR4x3tnl-HtTIpcg1nSN4GedpTr7ZJYr9xo1e9gt4ZCBFbPiHYPvNygCoob1zJUHyYO-fL7j9h9T9LSwrQUMVaGGCiU0IQbIzmcixLf0iPRPF5gLqi2q_tfuhF2C5m39kJDXkM-91e_V97VO-EZFdjg8sCcq7MnEnIo-pbCyc3lUaWXdfxnY2sZfemBjCk2TbBO4JZj7lgJqUNLYN3MZ3l-NO-NTeo9odZaFOlz8rCDaL1WTHkqbCLETvSSJouufLBuQA3hOLD0QOhZk4XgufD0P0wOWqIkWQBzeYCFUEyRC8AQwtabeneSx9THGNDuOhr2gIeHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری؛ چرخ زندگی
🔹
همراهان گرامی؛ اگر با کمترین بودجه، کسب‌وکاری را در منزل راه‌اندازی کرده‌اید، روایتگر مسیر خود باشید.
🔸
یک پیام صوتی حداکثر ۳۰ ثانیه‌ای شامل نام، شهر، نحوه شروع و نتیجه کسب‌وکارتان، به همراه عکس کسب‌وکار برای ما ارسال کنید.
🔸
روایت شما می‌تواند الهام‌بخش کسانی باشد که می‌خواهند از صفر شروع کنند؛ بهترین ایده‌ها و محصولات نیز فرصت معرفی و تبلیغ در خبرفوری و کانال‌های زیرمجموعه آن را خواهند داشت.
👇
#چرخ_زندگی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/681717" target="_blank">📅 19:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681715">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bi2yoe8SCxwFKh7sE08GSoOicvwB4NHVLQTfguHK-VqlTpXSTAwi2Dhu9wqdmnlY7FcMqQH-Z0V20MKfTtQVpyG66nYwP8aWTsozpR-LO2jGnulSz0e1Xk8yHRNTBYaf6N-YvHL6hiGQ-PqzAp87FgHEc8YUAgD8nmcK34-ABjHPF8OtaAQnryZraKICTO6whBB8TDNu91DbhR8FoTtPNM8uUQyJrPXGgGnFftopJV_LKvqw8rwBsOYdfLTtA1-LYw6o9h5Dydr4H8v74bFyS8AnJnEMogkaVqPTuGJdMmhEIAofw-msk5khIABtUw7SEUowTZeUXsAz3mkIi2LyAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاعری که نامش با نوگرایی، طبیعت و دگرگونی شعر فارسی درآمیخته است؛ نیما یوشیج
🔹
نیما یوشیج، از برجسته‌ترین شاعران معاصر ایران، تنها یک شاعر نبود؛ او آغازگر جریانی تازه در ادبیات فارسی شد و با شکستن قالب‌های سنتی، راهی نو برای بیان احساس، اندیشه و تجربه‌های…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/681715" target="_blank">📅 19:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681714">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
دریا همینطور که بخشنده است بی رحم هم هست
🔹
این دو جوان هرمزگانی ۵ روز در دریا سرگردان بودند و بنزین تمام کردند که صیادان بحرینی آنها را پیدا می‌کنند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/681714" target="_blank">📅 18:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681713">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فاکس نیوز: تفاهم‌نامه ۶٠ روزه بین آمریکا و ایران فردا منقضی می‌شود.
🔹
تاکنون درخواست‌های بیش از ۶ میلیون نفر برای مطالبه خسارات مادی و معنوی جنگ ثبت شده است.
🔹
جنگنده‌های اف-۱۸ اسپانیا یک پهپاد مشکوک را در حریم هوایی رومانی سرنگون کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/681713" target="_blank">📅 18:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681712">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WN7FKgRj767mJUVm8ssPNWuy5gyUB3oOcqsLO-htAtpRe9SQZDt5muWiDafjNaX0-w__ZJHm-3Ng2gToPO3P8t5uSdgnJrqsjG3wan5tNh4oRXe2MlHCVIo5a8zXOWSPdCTvu1W5jpxz7ArvUWkwTIlpzhKQCRui6XTJJDE2bSKX_JS93ljoB_ImG1D41OyniyhuyhpQWbCfFnrQVEb86nqZCB6MlKTlPNvb4GHSrI20czqPhr6ACfKz8igXHsxzc26YlL3iEwlm1V5GTIiLysZfriGK622SCdmPX7ZeTaid_qqJYcLWkpLbnmF3nH03irYT3jR9eiyHkVLJIH4sjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کریستیانو رونالدو ممکن است در پایان فصل از فوتبال خداحافظی کند
رونالدو در مصاحبه‌ای با مجله ووگ:
🔹
احتمالاً این آخرین سال من در فوتبال خواهد بود؛ بعد از آن، زمان زیادی برای استراحت، سفر، تماشا و بازی کردن پدل خواهم داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/681712" target="_blank">📅 18:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681711">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c0c01f9ac.mp4?token=krzeURJASihaxrItFhxxBzeQx_dzb3tpvkIfSZQYlCtKLkJCzVk2e3TLMkepe3bzFpZrZ4AUGHX3UNUGG4b1sgPBMMcNreheES67lQMzEhRTXvD1-fNBCQZsRkLwfWe_oHuKo8XiBng8q-si94CAJU6wVWP8WyBxduIlltdsPjqqWx_XAwD2EIQ-lx_HD2wDiCcpgD74szK8PUqnr-wmLEy0DUDd6fdrRbGQK4s2NZE_t_Fy1KBz2W52LWQjx9L0ALZ3xHOuzjZSAti6yZudEJpDHgWq07zWMaPodp99SGvDFMYbpNV3dFrI9g9SOiLHPb3MTWzNXfw6Aq5u_4wbUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c0c01f9ac.mp4?token=krzeURJASihaxrItFhxxBzeQx_dzb3tpvkIfSZQYlCtKLkJCzVk2e3TLMkepe3bzFpZrZ4AUGHX3UNUGG4b1sgPBMMcNreheES67lQMzEhRTXvD1-fNBCQZsRkLwfWe_oHuKo8XiBng8q-si94CAJU6wVWP8WyBxduIlltdsPjqqWx_XAwD2EIQ-lx_HD2wDiCcpgD74szK8PUqnr-wmLEy0DUDd6fdrRbGQK4s2NZE_t_Fy1KBz2W52LWQjx9L0ALZ3xHOuzjZSAti6yZudEJpDHgWq07zWMaPodp99SGvDFMYbpNV3dFrI9g9SOiLHPb3MTWzNXfw6Aq5u_4wbUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی وسیله‌ای برای باز کردن درب کنسرو نداریم چیکار کنیم!؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/681711" target="_blank">📅 18:39 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681710">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
یارانۀ ۴۰۰ هزار تومانی دهک‌های ۱ تا ۳ به حساب سرپرستان خانوار واریز شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/681710" target="_blank">📅 18:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681709">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
هاآرتص: هزینه جنگ غزه برای اسرائیل به ۱۴۲ میلیارد دلار رسید
هاآرتص:
🔹
جنگ غزه که از ۷ اکتبر ۲۰۲۳ آغاز شده، به طولانی‌ترین و پرهزینه‌ترین جنگ تاریخ اسرائیل تبدیل شده و هزینه آن به حدود ۴۲۰ میلیارد شِکِل معادل ۱۴۲ میلیارد دلار رسیده است؛ همچنین بدهی ملی اسرائیل حدود ۴۰۰ میلیارد شِکِل (۱۳۵ میلیارد دلار) افزایش یافته است.
🔹
رژیم صهیونسیتی در ابتدا انتظار داشت جنگ حدود سه ماه طول بکشد، اما ذخایر مهمات برای جنگی کوتاه‌تر آماده شده بود و مصرف برخی مهمات به دو برابر پیش‌بینی اولیه رسید.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عبری دنبال کنید
👇
@AkhbareFori_HE</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/681709" target="_blank">📅 18:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681708">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ua5XyGhl3kRPHO7WJhxifCLWrauYpe8H1E1aMw26F37eUoLfAoIMzNWW2dgmuoY7hlHNblpD-bTmNzoAP1LQzTmem2nl9q5BslCTYTVVOeryEgQmrKuVU3g3_6BS6vvag_rvmz8FyZu5KqStIf0pgD2y86eUMx1XvJbUrgHxc-pC5KDiPXW5t5901U2uNskJcbKh2mv72GF-GSFnH5zlOCdSvs3AfOwVFJxy8xfLlesBT5sKezXXx3vboQ7tnBV7TMN57DcjVefAu9NZXl2RGnd2no5UPt4qMqgZNoKPDdvh8urYSmfrz8DCzASn2-EvtacrT-yK_C5WYhXumeIv2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بارگیری روزانه گازوئیل از خاورمیانه و روسیه نصف شد
🔹
از حدود ۳.۱ میلیون بشکه در ابتدای سال به ۱.۵۵ میلیون بشکه در ۱۲ اوت رسید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/681708" target="_blank">📅 18:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681707">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
خاتمی:یادداشت تفاهم فرصتی فوق‌العاده برای کشور است؛ امیدوارم این بار فرصت فراهم آمده از دست نرود.
🔹
سخنگوی ستاد انتخابات: شعام تصمیم گیرندهٔ نهایی دربارهٔ زمان برگزاری انتخابات شوراها است.
🔹
پاپ لئو خواستار پایان خشونت علیه فلسطینیان در کرانه باختری شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/681707" target="_blank">📅 18:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681706">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/026aec7222.mp4?token=ZeVhdZ8C0uSwLiAllvnikd21GFViupSNfVyRv3QE_IYPRSDpWqEIrJZ8_jYIH_HQhTc4M74MHmEH1DJiwVbHNw6DtSRCWks31VddVZaguld5y6ce4wI94BhWYxVRB2etJZ7pV72wlbfMMUUJRjEwfqqsTSEdjxgSYIprSmOTz6aJTQEqNQ2aZiv0U_W5q6A2CZ6h0IFoVO1ljsH-PKR_2hMyAfEvfwAlG0qslQeHamNCajspXElCy-TYy7uaiFaWzvoIlTocfAClFTYqaScYKDENWyl4kPy3Xxky0wZ3NjQkzQ8n8pGBqFh37KmbvWBqNil9ApmtM5r6RQsO9d578Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/026aec7222.mp4?token=ZeVhdZ8C0uSwLiAllvnikd21GFViupSNfVyRv3QE_IYPRSDpWqEIrJZ8_jYIH_HQhTc4M74MHmEH1DJiwVbHNw6DtSRCWks31VddVZaguld5y6ce4wI94BhWYxVRB2etJZ7pV72wlbfMMUUJRjEwfqqsTSEdjxgSYIprSmOTz6aJTQEqNQ2aZiv0U_W5q6A2CZ6h0IFoVO1ljsH-PKR_2hMyAfEvfwAlG0qslQeHamNCajspXElCy-TYy7uaiFaWzvoIlTocfAClFTYqaScYKDENWyl4kPy3Xxky0wZ3NjQkzQ8n8pGBqFh37KmbvWBqNil9ApmtM5r6RQsO9d578Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس پدافند هوایی سپاه: در روزهای اول جنگ ۶ تا ۷ پهپاد هرمس و هرون رژیم صهیونیستی همزمان بر فراز جنوب لبنان گشت‌زنی می‌کردند
🔹
با هدف‌قرارگرفتن این پهپادها در ایران، تعدادشان در جنوب لبنان به یک فروند رسید و حزب‌الله آزادی عمل بیشتری برای عملیات پیدا کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/681706" target="_blank">📅 18:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681705">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
پایان جهان شاید زودتر از تصور باشد!
🔹
جهان حدود ۱۳.۸ میلیارد سال پیش با رویدادی موسوم به مه‌بانگ (Big Bang) آغاز شد. از آن زمان تاکنون، بشر توانسته مسیر تحول کیهان را تا حد زیادی درک کند، اما همچنان نمی‌دانیم که چه پایانی در انتظارش است.
🔹
پژوهشی جدید که هنوز در حال داوری علمی است، احتمال می‌دهد جهان حدود ۳۳ میلیارد سال دیگر به پایان برسد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/681705" target="_blank">📅 18:09 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681704">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qW179nJD6dYaucU4cindA_6QCHM5Mi2As4rQ5ce7VNZpr12yQycryctGFEGf4DRapaEk5nUQYmNudWWRSyDSpWsZ6qpTc32A6-Snsj6uejH6X8vQENlK2_MjUD-bK1OXHFJ1WdGTZzs7WiAAcHLPQgXA2YiPxYV3jsObrax-pDjzF-Q9UwWOmoXsoWDZ7cMkKWyhOgPTtu4Wik-qX1B8xGqJ0U5odr5wH2hZI6fve20efELjt54BYicwy2JG50d7KlAoo3N_nkEmZ4T4ByMeAylKj6Nyb26qqIe4TQ4mzxy6uACE4EK67e-6yrsc0B3DqBxFxSvEYacmYaFanRpoiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در ۷۲ ساعت گذشته سه کشتی در تنگه هرمز مورد اصابت قرار گرفتند
🔹
طبق آخرین ادعای مرکز اطلاعات دریایی مشترک (JMIC)، از زمان گزارش قبلی آن در ۷۲ ساعت پیش، سه کشتی هنگام عبور از تنگه هرمز مورد اصابت قرار گرفته‌اند.
🔹
دو فروند از آنها در آب‌های سرزمینی عمان در حال حرکت بودند، در حالی که فروند سوم در مکانی نامعلوم هنگام حرکت به سمت تنگه مورد اصابت قرار گرفت.
🔹
هیچ آسیبی گزارش نشده است و در هر سه کشتی به سفر خود ادامه داده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/681704" target="_blank">📅 18:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681703">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
حمله خونین با چاقو به نگهبانان بیمارستان مدنی کرج!
🔹
فاجعه در ساعات غیرملاقات؛ همراهان یک بیمار که قصد ورود با زور و خارج از وقت قانونی به بیمارستان مدنی کرج را داشتند، پس از ممانعت نیروهای حراست، با چاقو به نگهبانان بی‌دفاع حمله کرده و آن‌ها را شدیداً مورد…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/681703" target="_blank">📅 17:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681702">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8LpCN5lYnm7ttnvsLWj3JmfO2gsZN-iTCVyGJlOkuLbpWaQrLNpNDYYL3aBpxCHwBsz0Pgys6wG8kqpJaDWl0aXMv3oOsRv3RROy4QnMWY7GI_oyvDmWRGB0F-TZniqC2ch-QFspQ3LGnWKnG7LC2pnIWsnNkGHO8fVwBs6YqfFPoyQdO_mURG0M1SEQw1OybdatyaN1VDjGd-F4-GkqDd--nd5aEXjSEF1fciH5Qc5DEmYN69El_2ilUH3nocBK6qa9YzaMlFTECb8eoWRRu7AWhGUFDUOBq4fHHvF8iSbkV7j8ysW4J24hGtOTmdlINAo3bY1YFP1O87tZRhrHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مخمل کوه زیبای لرستان
🤩
#ایران_زیبا
#اخبار_لرستان
در فضای مجازی
👇
@akhbarlorestan</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/681702" target="_blank">📅 17:51 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681701">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
نوجوانان ایرانی روزانه بیش از ۹ ساعت به صفحه نمایش نگاه می‌کنند
مدیرکل حوزه ریاست مرکز ملی فضای مجازی:
🔹
در حال حاضر مردم در فضای مجازی زیست دارند و در کشور خودمان شاخص زمان نگاه به صفحه نمایش (اسکرین تایم) در روز، بیش از ۷ ساعت تخمین زده شده که این عدد در نوجوانان نیز بیش از ۹ ساعت است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/681701" target="_blank">📅 17:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681700">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3056fea164.mp4?token=KCMQWUQR5QRO6rBpob79hHJAehw4Wrh1OtkxkhGha3qu2u8lTGJ4aZdC6aAT3lImRObu2jLMpDZE_Kxwid3fkn5rhJdcD6-tDPvncEoTbFk2FwJN9aNkH3ByFpuK6gk1tx_MsGhgA5yYbS7wZbIewbnzZUusG-UBo3tXb7mBkySQt0_qJoZYy71NJYsEa2TEHxPSwZZzZq_-ronn92v3K5vnhBvWZfVEfT3e0v9ucr2FgualjFsvPB2IVyikN_Wb-abfGhYTFWluAPagJlw-Etp7L9_TGHcQCXgt-CzCTBbcbWalv5xvFFCQ3XC6vbYB16yOv7cQO-1tTCmuDB9D0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3056fea164.mp4?token=KCMQWUQR5QRO6rBpob79hHJAehw4Wrh1OtkxkhGha3qu2u8lTGJ4aZdC6aAT3lImRObu2jLMpDZE_Kxwid3fkn5rhJdcD6-tDPvncEoTbFk2FwJN9aNkH3ByFpuK6gk1tx_MsGhgA5yYbS7wZbIewbnzZUusG-UBo3tXb7mBkySQt0_qJoZYy71NJYsEa2TEHxPSwZZzZq_-ronn92v3K5vnhBvWZfVEfT3e0v9ucr2FgualjFsvPB2IVyikN_Wb-abfGhYTFWluAPagJlw-Etp7L9_TGHcQCXgt-CzCTBbcbWalv5xvFFCQ3XC6vbYB16yOv7cQO-1tTCmuDB9D0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هزاران مهاجر مراکشی تنها دو هفته پس از هجوم گسترده قبلی، دوباره تلاش می‌کنند وارد منطقه سئوتا اسپانیا شوند
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عربی دنبال کنید
👇
@AkhbareFori_Ar</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/681700" target="_blank">📅 17:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681699">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
آکسیوس: میانجی‌ها همچنان پیام‌ها را میان واشنگتن و تهران منتقل می‌کنند، اما پیشرفتی نیست
آکسیوس به نقل از منابع آگاه منطقه‌ای:
🔹
میانجی‌های پاکستان و قطر همچنان پیام‌ها را میان واشنگتن و تهران منتقل می‌کنند، اما پیشرفت ملموسی حاصل نشده است.
🔹
پاکستان ارزیابی‌هایی خوش‌بینانه‌تر از واقعیت ارائه می‌دهد تا این تصور را ایجاد کند که روندی رو به پیشرفت وجود دارد؛ تصوری که می‌تواند به شکستن بن‌بست کمک کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/681699" target="_blank">📅 17:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681698">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9stw2HyypcjOkY1UwUk-wRj3jYeaQAj5_iREQcW7yZ8hFk9x_AHeTZRU482Myk2hxHFH1o9_0CFFqmSRyvXxxsNH3he53sksnKOo1OEHgY7QcFze23qDEHzStvrNBYvsGefAlGtgWAE7nIS9Zq5nr6M9Qimy3Kg30sLaTUeiK_9w_5oP04D83SHeR8Q8A_hMi5Bd1IRT7sl2d0B0XgTY3U206X5DwGqZ1z031TQyHdDMq8Yu56DiA7BOUxhac1NHJymNh6JD_EWVbzNM13PfYIVkjC12OzDSBfTtNty04VuzJTaTIL543ayAtiNK-bXQqbC0FkwMYS1gThodJQbEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پای کار «خاک ایران» / ۱۰
🔹
رکوردشکنی بانک کشاورزی در پرداخت قرض‌الحسنه؛ رشد ۶ برابری در سه سال اخیر
🔻
مبلغ تسهیلات قرض الحسنه پرداختی بانک کشاورزی با جهشی چشمگیر از ۷۰ هزار و ۵۴۶ میلیارد ریال در سال ۱۴۰۱ به ۴۱۳ هزار و ۸۸۳ میلیارد ریال در پایان سال ۱۴۰۴ افزایش یافته که نشان‌دهنده رشدی ۶ برابری در سه سال اخیر است.
🔻
این بانک در چهار ماهه نخست سال ۱۴۰۵ نیز با پرداخت ۱۷۱ هزار و ۲۲۶ میلیارد ریال تسهیلات قرض‌الحسنه، روند رو به رشد حمایت از متقاضیان این تسهیلات را تداوم بخشیده و ۶ برابر نسبت به مقطع چهارماهه ۱۴۰۲ افزایش عملکرد داشته است.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/681698" target="_blank">📅 17:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681697">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bybh-GGMrqUD_nqIWDUqQeoqtYEAyRvrgYiWgqwojGte5o_ZHw-QBzh7O2NdaRDq2J-o_-g8Syq7VqO_b-OjW5PGwUHgB4NOv5vl-PYuewv2w2xG0YvF_TosfTZ8yodQEAyAuU8sMareLtsgL1osXYqkS0FteU5WJIqwMPu-Ltc2V9K1MglbqkOWaIvbPntJfK2-ZlmIamhO0GJs7mUgeesyuD1TC50wv50cWff7toQLD0kRJJx1JPSZCibHW-9zeSHGQqyWMAVCx8hhSzNFdcFFH2TXVjqB-IjtSQNZBJPkR4YaSH0mtxXWibJZN5coZlgBmYEEozH7VF2w5381mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از گوشی جدید ۶۶۰۰ نوکیا که از سری کلاسیک خود الهام گرفته
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/681697" target="_blank">📅 17:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681696">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
بیداد کارت‌های بازرگانی اجاره‌ای؛ ۲ میلیارد دلار ارزی که تبخیر شد!
«سلیمی» عضو هیئت رئیسه مجلس:
🔹
کارت‌های اجاره‌ای بازرگانی بیداد می‌کند و ۳۵ درصد تعهدات واصل نشده ارزی مربوطه به دلیل همین کارت‌های اجاره‌ای است؛ سؤال این است که چرا دولت برای اجرای این قانون ورود نکرده است؟
🔹
قوه قضائیه حدود ۳۰۰ کارت اجاره‌ای را کشف کرده که به میزان ۲ میلیارد دلار است و این مسائل نیازمند توجه جدی است و باید با این مسئله برخورد شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/681696" target="_blank">📅 17:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681694">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCCfeS0YsNBzyqOowkU2QWFaAGH1dhvwWWI1Y6r8d2qDgY0hqBFSvb1DAtQfnVkN8Sb00FHWUXOy1z4gJ80PMUTPKWjYy1IdJQS2U0ghdOzRlj627l8q-UaYqTMrsJlJHoBym2D8ZjD-34Fa9NzLJuCApMchWKvq_shUWF-ZkADeZqeZzawsAtBoy44FIFzIP2nL9kVO-V5UnKKEAX0uOVQHar06d3q8RvSPiaxd_WY_sOhFjljlgYdTgYyXB0Kb7dTnrjrjreSxlQu3eK72aZP_nGOvfdbY2eKxyFEW1MozmNIJtbniQGLoFp8qGUHDhB4wgCZKiDzC9BFdl6b8aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگ‌ترین بازارهای سهام جهان
🔸
آمریکا با ارزش بازار ۶۹.۸ تریلیون دلار، با فاصله‌ای چشمگیر صدرنشین بازارهای سهام جهان است.
🔸
پس از آمریکا، چین با ۱۱ تریلیون دلار و ژاپن با ۶.۷ تریلیون دلار در رتبه‌های دوم و سوم قرار دارند.
🔸
نکته قابل توجه این است که از ۱۲ بورس برتر جهان، ۶ مورد آن در آسیا قرار دارند که نشان‌دهنده سهم بالای این قاره در اقتصاد جهانی است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/681694" target="_blank">📅 17:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681693">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
ادعای رادیو ارتش رژیم صهیونیستی: ارتش در حمله‌ای در خان یونس، یک فرمانده گروهان حماس و در نصیرات، یک فرمانده جهاد اسلامی را هدف قرار داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/681693" target="_blank">📅 17:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681692">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/101ad9a6f4.mp4?token=WQFKA3FuZ0LIqTCCiRr30vECHRNcA1J3y5Ewv7303CYZVwHtgXd7iV6tKZyG2qRxpNlgHijYQOgk5jx1o8ciCtYcL74uKsHB6mPIA2iZVGsHNFsFK5srZJsQ1L39bBEApHNpeOfE2Ui8pLBQjXC3RJq_6vmQ1RdwJeRELiKPSvuIe3BAQR4uwLK3fDEdulSrUKrEOrkcrFy_oJszbRa6SJXmIFeI0ug1TnjrmNn16llpXl3wrYQdR6rv7baa0sPUHOHv-mu38TCEtxTQfeI3cNKKT88E1uXmXu6ISC7GP8nGcLRXJk5tzTeapKLvKE-26bB4gbdBNnRjFLc6di4vng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/101ad9a6f4.mp4?token=WQFKA3FuZ0LIqTCCiRr30vECHRNcA1J3y5Ewv7303CYZVwHtgXd7iV6tKZyG2qRxpNlgHijYQOgk5jx1o8ciCtYcL74uKsHB6mPIA2iZVGsHNFsFK5srZJsQ1L39bBEApHNpeOfE2Ui8pLBQjXC3RJq_6vmQ1RdwJeRELiKPSvuIe3BAQR4uwLK3fDEdulSrUKrEOrkcrFy_oJszbRa6SJXmIFeI0ug1TnjrmNn16llpXl3wrYQdR6rv7baa0sPUHOHv-mu38TCEtxTQfeI3cNKKT88E1uXmXu6ISC7GP8nGcLRXJk5tzTeapKLvKE-26bB4gbdBNnRjFLc6di4vng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ثبت تصویر پلنگ ایرانی و توله‌اش در پناهگاه حیات‌وحش «کم‌کی» بهاباد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/681692" target="_blank">📅 17:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681691">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-r1drCl_2veJOrMZFAW7Iy-d1BePSyuzJI0IR8YuP0hhZzA51Y7-5zBgeVdnLKclGYbW3lYQ1dSL_VKnTL2XRMFko4JidHniaKPkCrCa72QdMJlm24cIDHZbkAv1b1Myz1smIsJO5II1gX4U4zJgi-2sgS9IoPzOG0QOG_xOApiFFoZYZyCV2wgGccnOlJPtlnvCRxjfJLuxjxjDpRbYJ5Z-DYrKk2LXJERo91RyXfSeq_u648Z8CrXxG6IvZE_1gvJCmTV3xtpi88794BymsGF48F0vwGLZ_1ojbKyExoSAyymaraMSLR2i0kH4A_susU2WzyKhTQ0xaWopTyGug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
داماد ترامپ با سران حماس دیدار می‌کند
🔹
جرد کوشنر داماد ترامپ با حضور میانجی گرانی از مصر، قطر و ترکیه، با نمایندگان حماس در قاهره دیدار خواهد کرد.
🔹
در همین رابطه، شبکه تلویزیونی سعودی «الحدث» مدعی شد که جرد کوشنر داماد و فرستاده دونالد ترامپ رئیس‌ جمهور آمریکا، با نمایندگان حماس و با حضور میانجی گرانی از مصر، ترکیه و قطر دیدار خواهد کرد./ مهر
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/681691" target="_blank">📅 16:54 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681690">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c1975151.mp4?token=imgW3RoHBOTXdDhYa4F-jgNabKbVgmEl2D1ZhSkDoDa_28_GsKdjs62k9i1KcXG37joqLIkKY0KoPoOH84tcvhzj9Cmjsm72VmlKioycxgjUl7MwUP6DIYSj7INAIa4lUqBV2B6uS2w39ulUvKYVk0OAope8QiuyqY2rVo4m36bGaKxC3TF-5VyNql29GUJRVvsQ-jpB_3DIcx7BVmXi9Hdf6iRmxzI7li2v9-NOaw36wWBvpjlSaqsdREQ6HcNypkCm75k60WD1JaUYDH3J9wsFWpPwPtpxvjEniHrXPvQNwXIFMxoDZyXiGoDYSqamC8c6wssAgS1S9PBe9AffUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c1975151.mp4?token=imgW3RoHBOTXdDhYa4F-jgNabKbVgmEl2D1ZhSkDoDa_28_GsKdjs62k9i1KcXG37joqLIkKY0KoPoOH84tcvhzj9Cmjsm72VmlKioycxgjUl7MwUP6DIYSj7INAIa4lUqBV2B6uS2w39ulUvKYVk0OAope8QiuyqY2rVo4m36bGaKxC3TF-5VyNql29GUJRVvsQ-jpB_3DIcx7BVmXi9Hdf6iRmxzI7li2v9-NOaw36wWBvpjlSaqsdREQ6HcNypkCm75k60WD1JaUYDH3J9wsFWpPwPtpxvjEniHrXPvQNwXIFMxoDZyXiGoDYSqamC8c6wssAgS1S9PBe9AffUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دردسرهای تسلا در هندوستان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/681690" target="_blank">📅 16:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681689">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
تیزر قسمت سی‌ودوم از فصل پنجم
🔹
در این قسمت تجربه‌ نزدیک به مرگ دو خانم نوجوان با محدوده سنی ۱۰ سال به نام رضوانه که در حین تمرین سرود بر مزار شهدا روح از بدن جدا و توسط ۴ فرشته به آسمان عروج کرده و با رؤیت و دعای فرد سبزپوش با شکافی بر فرق سر، به جسم باز می‌گردد و خانم ریحانه که بخاطر سرماخوردگی شدید در حین استراحت در منزل، روح از جسم ایشان جدا و تجربیات جدید و شنیدنی را درک می کند؛ نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گران
: رضوانه عرب نظرگاه/ ریحانه رشیدی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/681689" target="_blank">📅 16:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681688">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس مرکز رسانه مجلس: جزئیات طرح مقابله با نفوذ بیگانگان هنوز تصویب نشده است.
🔹
دادستان فیروزآباد: اخبار ربایش کودکان صحت ندارد/ تشکیل پرونده قضایی برای منتشرکنندگان اخبار کذب
🔹
خبرگزاری رسمی عربستان: هشدارهای حملهٔ هوایی در جازان فعال شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/681688" target="_blank">📅 16:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681687">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/220b7dc3df.mp4?token=W_FNeq9GOQ7hAgSlgT9foVC2zcAUKTDHpPTRNEhPGNdjLnA9D-0mzmmLyHHzxH6XB4S5dJUM1Pymfu31krh6xz7iOQutumNkAj7iIqe45jYcCa2CfNlFRIvSZWUlvsxytHqNu-vmIEwZjDyXPs6wAWtsCjlxS3Ymj9K0CR39HMwbCHo5t5jV8NLAI63-71O_JnB5LpaPeoAcc5Q6GFhJsewxJnY_KGl0BzpELj4DOWDvtAvkRVVJwp8vH57z9yL2qu_c1bzB9IziymjET4xDCPwVAS8f4URtL97US5Ke2C7Cl4fTHSWofvf1khGslXGtCkh7BIRZko9KsNLfeiYDlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/220b7dc3df.mp4?token=W_FNeq9GOQ7hAgSlgT9foVC2zcAUKTDHpPTRNEhPGNdjLnA9D-0mzmmLyHHzxH6XB4S5dJUM1Pymfu31krh6xz7iOQutumNkAj7iIqe45jYcCa2CfNlFRIvSZWUlvsxytHqNu-vmIEwZjDyXPs6wAWtsCjlxS3Ymj9K0CR39HMwbCHo5t5jV8NLAI63-71O_JnB5LpaPeoAcc5Q6GFhJsewxJnY_KGl0BzpELj4DOWDvtAvkRVVJwp8vH57z9yL2qu_c1bzB9IziymjET4xDCPwVAS8f4URtL97US5Ke2C7Cl4fTHSWofvf1khGslXGtCkh7BIRZko9KsNLfeiYDlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مراحل ترمیم و پرکردن مجدد دندان آسیاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/681687" target="_blank">📅 16:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681686">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a78839f85b.mp4?token=Y-HR6-1QuykEcA9y992bvr2udcL79dTKCgqvS5yQ1Rl1mCRRlZaJ_y9IFtPt38VvftDKykC9ksN0g6G0cVcxrmmnkZCwUEYzx7485ArB2mDM1GmZhMw-kowDYUcHFRrlrbFLkXAOBT34NOT7pblEqt4YoVtSbtrHux3rrh2COuC0vNQxSZGXACTgTu7OY0g1LP3i7cDeQYB7sVklyeo1aO3IQIiQKUUUGGpGnbFyivog6w0VnvH-ulX3ZdZ0cFz8so7SmU_ES_9SBNBDWmh2W31yHK2fDk9-iHmEC36WpnjMtI70qMKq0Bnc51dJ7RJeTO_bB2rMymv1y4L26Df5wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a78839f85b.mp4?token=Y-HR6-1QuykEcA9y992bvr2udcL79dTKCgqvS5yQ1Rl1mCRRlZaJ_y9IFtPt38VvftDKykC9ksN0g6G0cVcxrmmnkZCwUEYzx7485ArB2mDM1GmZhMw-kowDYUcHFRrlrbFLkXAOBT34NOT7pblEqt4YoVtSbtrHux3rrh2COuC0vNQxSZGXACTgTu7OY0g1LP3i7cDeQYB7sVklyeo1aO3IQIiQKUUUGGpGnbFyivog6w0VnvH-ulX3ZdZ0cFz8so7SmU_ES_9SBNBDWmh2W31yHK2fDk9-iHmEC36WpnjMtI70qMKq0Bnc51dJ7RJeTO_bB2rMymv1y4L26Df5wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وام گرفتن همیشه راه نجات نیست، اگر می‌خوای وام هوشمندانه بگیری این ترفندها رو از دست نده #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/681686" target="_blank">📅 16:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681685">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس هیئت نظارت بر انتخابات شوراها: انتخابات شوراها ۲۴ مهر برگزار می‌شود.
🔹
دانشگاه شریف: حکم اخراج رضا دالمن، دانشجوی اخراجی برای اجرا به دانشگاه ابلاغ شد.
🔹
یکصد و پنجاه و سومین حراج شمش طلا ۲۷ مردادماه برگزار می شود.
🔹
احتمال شنیده‌شدن صدای انفجارهای کنترل‌شده در خمین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/681685" target="_blank">📅 15:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681684">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
تداوم حملات موشکی و پهپادی یمن به محل تجمع مزدوران عربستان
🔹
خبرگزاری رسمی یمن (سبأ) امروز به نقل از یک منبع نظامی خبر داد نیروهای مسلح این کشور باز هم خسارات سنگینی به مزدوران عربستان سعودی وارد کردند.
🔹
این منبع می‌گوید نیروهای مسلح یمن در جریان حملات پهپادی و موشکی، محل تجمع مزدوران سعودی را در منطقه «المخا»‌ و استان «مأرب» هدف قرار دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/681684" target="_blank">📅 15:47 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681683">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2feda353eb.mp4?token=gZant8ZYvcAXIk-rNwTaFd0iVwgV3NAFUfO7hY_g3Bsa7cMKpneFZvBcNIT6ndliGYdiD1hpTjHONUAvzrY8ynLFcYvKwySIupkv-iR_u_jjtEUSkrQDiqz9wZ5VoqZtxNFAJPEhk9onA8Z80s0R7tpFh7xeVCNJq6BvxlT6squakBnrpApN6OXE_eIeiNquXRxWfunM33J42PTVckM4QGSKwnVSTaiO95SKsvcIY_9p5Xk94OLxEQNoTST2TswfxMcmczZfnUe1OgvwYouVnjUWYMoKPrhB02fF6kWvuUP282nfB8hOWn47vOOeA6gKR-G0UPUEbyYHeJkfvDKtGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2feda353eb.mp4?token=gZant8ZYvcAXIk-rNwTaFd0iVwgV3NAFUfO7hY_g3Bsa7cMKpneFZvBcNIT6ndliGYdiD1hpTjHONUAvzrY8ynLFcYvKwySIupkv-iR_u_jjtEUSkrQDiqz9wZ5VoqZtxNFAJPEhk9onA8Z80s0R7tpFh7xeVCNJq6BvxlT6squakBnrpApN6OXE_eIeiNquXRxWfunM33J42PTVckM4QGSKwnVSTaiO95SKsvcIY_9p5Xk94OLxEQNoTST2TswfxMcmczZfnUe1OgvwYouVnjUWYMoKPrhB02fF6kWvuUP282nfB8hOWn47vOOeA6gKR-G0UPUEbyYHeJkfvDKtGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرمانده کل ارتش خطاب به ترامپ جنایتکار: غلط میکنی می‌گویی تنگه هرمز برای آمریکاست
سرلشکر حاتمی:
🔹
رئیس جمهور جنایتکار آمریکا می‌گوید که میخواهد تنگه هرمز را بخشی از سرزمین جنایت، اعلام کند، شما خیلی غلط می‌کنی! او بعد از آنکه واکنش‌ها را دید، اعلام کرد که شوخی کرده است.
🔹
شوخی این حرف هم، غلط زیادی است چراکه اینجا ایران است و حافظانی دارد که قلم پای شما را خواهند شکست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/681683" target="_blank">📅 15:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681682">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8ab5c22b7.mp4?token=IO_nQRYZq-czv9Q3Z9YBNr96n1EXYNIlYmttDpVx11TASMGa4IbX_OdnNyBb6PiMRptmf47sM68S6tIzGF5WC8oikoBNhMziamP8VxwJWTu_lJL6PrAamjbMqU0rpsrTKL0z9yPZ3KU8QuzJADNFWN22Gh0hQTR08vGF2OyeC_Tev7HqQctW14qT32NPTNJz8Z_IwxHPWlZ4bTUj2lcVyfcq6_RPDl1iRxYTN2dvnvriv2W5jb5WAwFEq39_1TjggMpczejIGiKQbYAH6Ay-Kb3NldivML8lnUVXmUZB9FNOOe08zrWhSeAsJ0NDSDKn2_LxcR6bTttZqUh6jvAdtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8ab5c22b7.mp4?token=IO_nQRYZq-czv9Q3Z9YBNr96n1EXYNIlYmttDpVx11TASMGa4IbX_OdnNyBb6PiMRptmf47sM68S6tIzGF5WC8oikoBNhMziamP8VxwJWTu_lJL6PrAamjbMqU0rpsrTKL0z9yPZ3KU8QuzJADNFWN22Gh0hQTR08vGF2OyeC_Tev7HqQctW14qT32NPTNJz8Z_IwxHPWlZ4bTUj2lcVyfcq6_RPDl1iRxYTN2dvnvriv2W5jb5WAwFEq39_1TjggMpczejIGiKQbYAH6Ay-Kb3NldivML8lnUVXmUZB9FNOOe08zrWhSeAsJ0NDSDKn2_LxcR6bTttZqUh6jvAdtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله خونین با چاقو به نگهبانان بیمارستان مدنی کرج!
🔹
فاجعه در ساعات غیرملاقات؛ همراهان یک بیمار که قصد ورود با زور و خارج از وقت قانونی به بیمارستان مدنی کرج را داشتند، پس از ممانعت نیروهای حراست، با چاقو به نگهبانان بی‌دفاع حمله کرده و آن‌ها را شدیداً مورد ضرب و شتم قرار دادند!
#اخبار_البرز
در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/681682" target="_blank">📅 15:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681681">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guaUGByhkayXSkNUR9bCeZXWE4xmIQytPoglNkr_5iVTdjzcB3SJn78TG5kuVnwKIzNnsDmDY-FsZQ6tEW3KUKF3DQNdPwMKFR1aHREgKRxHoXcNuQgokA9uP2AsnF3tCZMDwq2ZvwFugWIas6SemllsmDQWrtD9yMr_LtbpU9p0FC6JBaRQwG_4gH0C_Ck4fxR5CdGZJJegz1gE64h3mYPOgQQx8kxwDZizK8d6HncL8YJpT4dRSeTVuCAw-rKw9q_if07og8d4osvJHEZjvMgDA0tw-3k-kpo2od3VxLmv2l9dywOXnODHw21B8WK3RfLWkP7L4bsJyDvDxKBrIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاوش ماه بدون دخالت انسان ممکن می‌شود
🔹
ناسا قصد دارد سه ماه‌نورد کوچک را به ماه بفرستد که تنها یک دستور دریافت خواهند کرد: خودتان بین یکدیگر تصمیم بگیرید که چگونه یک منطقه از سطح ماه را کاوش کنید.
🔹
این سه ماه‌نورد حدود دو هفته را صرف نقشه‌برداری از سطح ماه به ‌عنوان یک گروه خودهدایت‌شونده خواهند کرد.
🔹
هیچ انسانی نیز قرار نیست هر حرکت آنها را تایید کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/681681" target="_blank">📅 15:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681680">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
چرا خاموشی‌ها دقیقاً مطابق جدول زمانبندی اعمال نمی‌شود؟
معاون برق و انرژی وزارت نیرو:
🔹
برنامه اعلام شده از طریق سامانه برق من یک برنامه احتمالی است و در صورت بهبود شرایط شبکه، خاموشی پیش‌بینی شده اعمال نمی‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/681680" target="_blank">📅 15:21 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681679">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFwV-n9tVSM3TZSZZzZmHxSoAjg7iKAuAJ7181zIKy2Pn_7s-3nc_sO6_9AbPtVgtxyouDpN2ew3UJMBCujDrcjwHHgx4qAv_jLXVWjGerHP4uZx-tK9FAxLf9acPN-Clm_dQ284uB1_k4Ied5SerqFuWnJS43NzON_Dff-WHnoIpPuaAp79wDp5iQo6v_HEches4pMq-wQmdQaADWmSARZ8SS0oyFCZIHppoMDGgWPDRx2zGEP0XPCzH1F12Rp_pGo97mRW4B3muN2Yh-XZn1xLnIjE3bOlXZH0-Upa4TJsO0F6BDBjNvwb8UKD_ZOfJ1iU7oyz9Jmxi72w7zWmaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ویژگی مشترک ۱۵ میلیون ساله؛ میمون‌های بزرگ همگی مثل انسان می‌خندند
🔹
پژوهش‌های جدید نشان می‌دهند که میمون‌های بزرگ مانند انسان‌ها از شدت خنده کنترل صوتی خود را از دست می‌دهند. تحلیل خنده‌ی اورانگوتان‌ها، بونوبوها، گوریل‌ها و شامپانزه‌ها حاکی از وجود ریتمی منظم و هم‌فاصله در انفجارهای صوتی آن‌هاست. این ویژگی مشترک احتمالا از نیای مشترک انسان و این گونه‌ها که ۱۵ میلیون سال پیش می‌زیست، به ارث رسیده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/681679" target="_blank">📅 15:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681678">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما مهم‌ترین عامل گرانی مسکن در ایران چیست؟</h4>
<ul>
<li>✓ تورم</li>
<li>✓ دلالی و سوداگری</li>
<li>✓ عدم نظارت جدی بر بازار</li>
<li>✓ افزایش تقاضا و رشد جمعیت</li>
<li>✓ کمبود ساخت‌وساز</li>
<li>✓ نگاه سرمایه‌ای به مسکن</li>
<li>✓ افزایش قیمت مصالح</li>
<li>✓ سایر موارد</li>
</ul>
</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/681678" target="_blank">📅 15:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681677">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
بورس انرژی از عرضه بنزین سوپر در معاملات ۲۸ مرداد با قیمت هر لیتر ۸۹ هزار و ۷۰۰ تومان خبر داد.
🔹
پزشکیان: در روش‌های آموزشی باید به معلمان و مدیران مدارس اختیار و آزادی عمل بیشتری داده شود.
🔹
سوریه پروازها به مسکو را از سر گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/681677" target="_blank">📅 15:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681676">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f46c059e4f.mp4?token=mxKyNGVuD4AC4DMxDpJnk4sxQEB0sDh0wGcUr6XpsWOcuBGehn8zjwZR5LIWW-OKTCbydUCbSzDTlJELfgrBVCS62p3gZZR_8Kss-tJhcsAvZz3VCFak5sXLPP16qFKX6Itmls3JoDc5LiMD59oG8v958Gzms-dpf_TScSlz0lgsdYz67-8eANmnI8ApNTJTZ3RxfE2h9kI0ppFmR8Vhi4p2jNaj0BNzTwHXqEgGofyOjNMOyMAcga8VRBoREiyotov4tRBOB0N4v1Gm3BUJvKpk0TGdt-9993H0C9KnXkgMeTdw0mUT090c6HH9XVCC58dGGujxozLlILEcTVThGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f46c059e4f.mp4?token=mxKyNGVuD4AC4DMxDpJnk4sxQEB0sDh0wGcUr6XpsWOcuBGehn8zjwZR5LIWW-OKTCbydUCbSzDTlJELfgrBVCS62p3gZZR_8Kss-tJhcsAvZz3VCFak5sXLPP16qFKX6Itmls3JoDc5LiMD59oG8v958Gzms-dpf_TScSlz0lgsdYz67-8eANmnI8ApNTJTZ3RxfE2h9kI0ppFmR8Vhi4p2jNaj0BNzTwHXqEgGofyOjNMOyMAcga8VRBoREiyotov4tRBOB0N4v1Gm3BUJvKpk0TGdt-9993H0C9KnXkgMeTdw0mUT090c6HH9XVCC58dGGujxozLlILEcTVThGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون وزیر نیرو: به دلیل سنگین شدن بهای برق در بازه‌های دوماهه، در دستور کار است تا دوره صدور قبض‌های برق به یک ماه برسد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/681676" target="_blank">📅 15:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681675">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/325c72fcbd.mp4?token=gFV5WOFpaROccu37vjJ6tA2lmWBbOHrEqpOCKurarDHwgyvkg91B_fHMEG7UBE6L0IawsyW1CyM9O4OrhXkRUMG3SLbXZlaS1PXkd5rKXpqFWHXTEYOOmXUKu22NCNGyijLeobx6mDykDlubWiJA8D9Z6fX7lvgEEvSqeqebmH_XYa0l0Pf2leFZPBJLZ8kYRCjTBOCDX1f0G0vY_DHE9BZEj98PXKUnigyoF-GzNSn0V12bc6l9GhqrUUCN4OaSDR8VHNCDf9NwK_gyy9v0u5Yllk-bEpFaM940Z2HnIF0HrzYYnxIp1AZw3d61fUPUuqv4aufM66fAmNgHdXl5LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/325c72fcbd.mp4?token=gFV5WOFpaROccu37vjJ6tA2lmWBbOHrEqpOCKurarDHwgyvkg91B_fHMEG7UBE6L0IawsyW1CyM9O4OrhXkRUMG3SLbXZlaS1PXkd5rKXpqFWHXTEYOOmXUKu22NCNGyijLeobx6mDykDlubWiJA8D9Z6fX7lvgEEvSqeqebmH_XYa0l0Pf2leFZPBJLZ8kYRCjTBOCDX1f0G0vY_DHE9BZEj98PXKUnigyoF-GzNSn0V12bc6l9GhqrUUCN4OaSDR8VHNCDf9NwK_gyy9v0u5Yllk-bEpFaM940Z2HnIF0HrzYYnxIp1AZw3d61fUPUuqv4aufM66fAmNgHdXl5LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برای چین‌های یکدست این ترفند رو یاد بگیر
🔹
یک‌ترفند کاربردی برای علاقه‌مندان به خیاطی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/681675" target="_blank">📅 15:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681674">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeYsuUd8gxym14whn0amBGLbkKfN7ud7j1oFyFGNNYeoZeoWzW0nJ_w0bnCJNf7qznhEAVePu6d6aCMoBlvrFw4Fy5Tde9zhMtjHNDRFAZwBalMHQdcrB_uDnTb3ECXDSnAoKGPafbMvBBD2S05VwkXuihiGvsyD1EsDk4DbpsTIfiFypn4ENSuz87rNNVoc1n1rFSzPaYxzqXqBrUJ-Z5I3yBh6w6shLEqBOZos3WrqFz05BO9QDYlS3rJ5JdVfObcdc7fMjOEL1WhsiddvjpBQRzMPrDylssWo5axFr2lhRDDYic57ZpHYpXWJzQpFyWacLarT5ZVLtN-tzO28WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نماینده مردم قروه و دهگلان در مجلس:
زمان بازنگری در ممنوعیت واردات ۴ قلم لوازم خانگی رسیده است
🔹
محمدرسول شیخی‌زاده، نماینده مردم قروه و دهگلان و عضو مجمع نمایندگان استان کردستان، با انتقاد از ممنوعیت واردات چهار قلم لوازم خانگی، این سیاست را شکست‌خورده دانست و گفت ادامه آن علاوه بر محدود کردن بازار و افزایش فشار بر مصرف‌کنندگان، درآمد رسمی مرزنشینان را کاهش داده، قاچاق را گسترش داده و درآمدهای گمرکی و مالیاتی دولت را نیز کاهش داده است.
🔹
ممنوعیت واردات لزوماً مانع ورود کالا نمی‌شود؛ بلکه مسیر ورود غیررسمی و قاچاق را هموار می‌کند.
🔹
از نیمه اردیبهشت، میزان واردات رسمی چهار قلم لوازم خانگی حتی از مسیر کولبری، ملوانی و ته‌لنجی صفر شده است.
🔹
محدود شدن تجارت قانونی مرزی، بخشی از درآمد رسمی مرزنشینان را کاهش داده و فشار مضاعفی بر معیشت آنها وارد کرده است.
🔹
ممنوعیت واردات باعث شده مردم به کالای باکیفیت و متنوع دسترسی کمتری داشته باشند و هزینه تأمین کالا برای خانوارها افزایش یابد.
🔹
وقتی واردات از مسیر رسمی انجام نشود، دولت از درآمدهای گمرکی و مالیاتی محروم می‌شود.
🔹
ادامه ممنوعیت واردات، بیش از آنکه به نفع تولید و مصرف‌کننده باشد، در عمل به ضرر هر دو تمام شده است.
🔹
زمان آن رسیده است که ممنوعیت واردات لوازم خانگی جای خود را به یک سازوکار شفاف، هدفمند و مدیریت‌شده بدهد.
🔹
این سازوکار باید ضمن حمایت واقعی از تولید داخلی، مسیر قاچاق را محدود کند، درآمدهای رسمی دولت را افزایش دهد و امکان استفاده مرزنشینان از ظرفیت‌های قانونی تجارت را فراهم آورد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/681674" target="_blank">📅 14:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681672">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjSfyY17bJQYk8nCGuBcKCgtxxkqPNrd4kckhVG8EqWPxHd4SJChYCQ4ZMD6Pl6VaAzuLrYydfl9yuIAngEiTFpY-dRY8af6xUuzJPTm9DxM1exI64lCAqhg2dLT98xnNWAgaecZRgdb5Krt_XIXD8lO5ep-K-bfKagtazpTexPiiY3I9M3PWwtRp-QdAzmj-QmGj9w8u-VHWng_oxDVPPsx0rctDWB9k5Viweb33exHQNHhMJemibZQjR7H6TvUJ86cQDE7jn_hRoEHI7Y2TAzNkGeOK364VLLVtB1F2AWXY8H9QxMe7G_Uv1WlpxACVFMSrMdppjh9GHZtQSUMfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسلح‌ترین ارتش تاریخ جهان را به زانو در آوردید
فرماندهی سپاه پاسداران انقلاب اسلامی:
🔹
فرمانده کل سپاه با تقدیر از شش ماه جهاد رزمندگان اسلام تاکید کرد: شما در گرمای سوزان جنوب، سرمای ارتفاعات شمال و زیر آتش سنگین دشمن با عملیات موفق آفندی و پدافندی، مسلح‌ترین ارتش تاریخ جهان را به زانو درآوردید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/681672" target="_blank">📅 14:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681670">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
اولین تصاویر از جانی بی‌رحم چهارراه گلزار کرج  #اخبار_البرز در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/681670" target="_blank">📅 14:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681669">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e6f2d67a9.mp4?token=nzAt14TgpLugKHdjxIXHjJcan3xHbxWyJ4Ur8m1KkhRF3XwqLKyN1ZYr6zwFPEfXDtHq_F561VleMQIOCzW34uGhJQv0huXWWzavKejbW3ry3kOxjIGR_w-3QkHdEy3khQ0sSFHH5WccMZGvfOTb1hWrRS00ltZ1ePN7-UbImRCwO-ev7sFFyqb89hDPbdPbjSbzxsT_QlknBSvBa9q4a6vQ1_0ngk7Pk0eU_xwYfgEqoM5SHEarUwozavVfdUpMIDx1fzN7WT4a_eApit4ZusQ_HcVnC9jpl5K3hoiqCA6gUC9ArcfzqyaF6c353CAoZfcejC7xTNWTaPgYjwskEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e6f2d67a9.mp4?token=nzAt14TgpLugKHdjxIXHjJcan3xHbxWyJ4Ur8m1KkhRF3XwqLKyN1ZYr6zwFPEfXDtHq_F561VleMQIOCzW34uGhJQv0huXWWzavKejbW3ry3kOxjIGR_w-3QkHdEy3khQ0sSFHH5WccMZGvfOTb1hWrRS00ltZ1ePN7-UbImRCwO-ev7sFFyqb89hDPbdPbjSbzxsT_QlknBSvBa9q4a6vQ1_0ngk7Pk0eU_xwYfgEqoM5SHEarUwozavVfdUpMIDx1fzN7WT4a_eApit4ZusQ_HcVnC9jpl5K3hoiqCA6gUC9ArcfzqyaF6c353CAoZfcejC7xTNWTaPgYjwskEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استانداردهای دوگانه برای «حقوق زنان»
🔹
برای ایران: تحریم، فشار، تیترهای داغ
🔹
برای صهیونیست‌ها: سکوت مطلق
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/681669" target="_blank">📅 14:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681668">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
هر آمریکایی متجاوز به ایران را بکشید یا تحویل دهید، ۵ میلیارد تومان پاداش می‌گیرید
طرح جدید ارتش که توسط سرلشکر حاتمی فرمانده کل ارتش اعلام شد:
🔹
پنج میلیارد تومان پاداش برای کسی که هر آمریکایی متجاوز به خاک و آب ایران عزیز را بکشد یا به واحدهای ارتش تسلیم کند.
🔹
همینطور اگر هر زن ایرانی، یک آمریکایی متجاوز را بکشد یا دستگیر کند، مبلغ پاداش دو برابر یعنی ده میلیارد تومان خواهد بود./آوش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/681668" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681667">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
مصوبه مجلس: ۳۰ سال زندان برای پیشنهادات سیاستی یا تقنینی یا اجرایی به نهادهای حاکمیتی و دولتی که برخلاف مصالح اساسی نظام است یا آرای مردم را ‌به نفع گروه یا جریان خاصی جهت‌دهی کند/ انتخاب
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/681667" target="_blank">📅 14:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681666">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f83e2233c4.mp4?token=Rz1-3PGQUFhlfAF0Qv2Io3uFMDrCVna4v8JQAIPByR_47VL06imxaHo2niq2kaGUMKIbpeh-FXueWPvL1K0EedDHU781urO5JUlFid6Bwy29JeBpJ2JubJqUFPdLsntYY-_3GTQrDuXbJ3AJ_6OT1AMCkqn6fg2SkWdFgR7GnPlMrjVHyk3rhx9Lv2hQpQ6eKsfIsAV1PvTLRcJ1NsgZkR_69JYbpjgfKlu7D17lPlHfxfXFAJWhYzdukzYLoH_xEZ8itdy0aesHzvuP6JAac71hP3VQoSZ2e9MoQT1xJiHv-ew_8e0J6huXCGymmL6gqu-zKj9LKab6rvN1ZkP6CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f83e2233c4.mp4?token=Rz1-3PGQUFhlfAF0Qv2Io3uFMDrCVna4v8JQAIPByR_47VL06imxaHo2niq2kaGUMKIbpeh-FXueWPvL1K0EedDHU781urO5JUlFid6Bwy29JeBpJ2JubJqUFPdLsntYY-_3GTQrDuXbJ3AJ_6OT1AMCkqn6fg2SkWdFgR7GnPlMrjVHyk3rhx9Lv2hQpQ6eKsfIsAV1PvTLRcJ1NsgZkR_69JYbpjgfKlu7D17lPlHfxfXFAJWhYzdukzYLoH_xEZ8itdy0aesHzvuP6JAac71hP3VQoSZ2e9MoQT1xJiHv-ew_8e0J6huXCGymmL6gqu-zKj9LKab6rvN1ZkP6CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بحران کشتیرانی در راین آلمان به دلیل کاهش شدید سطح آب
🔹
سطح آب رودخانه راین در آلمان به دلیل خشکسالی طولانی در اروپا به شدت کاهش یافته و کشتیرانی را در آستانه فروپاشی کامل قرار داده است. در برخی نقاط، سطح آب به تنها ۸ سانتی‌متر (و حتی در شب به ۶ سانتی‌متر) رسیده است، در حالی که عبور کشتی‌های باری نیازمند حداقل ۴۰ سانتی‌متر آب است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/681666" target="_blank">📅 14:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681665">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd2127aec.mp4?token=lTKPB9sbhSNQXX112g5yDwykmSlcnP7G3_DomL-zFkA9SPG6O_T43PIPoIMOehBdRPjWJJqOifg-NoJ2ulpvX98fGcrmN8_6oUk7Z-mr-u4YI1zXl2AxStk87SnEeUR-BVlFes5V5GvITPjoD-2FoK2whC0zz-z1LbvaJbglVGLjn9q0x_RSzv4iVgID_85__6H9UKVLkhaRYjgt9wx4d7endtcT6ZWpKhRIxi92yUJzNhgSPNF1dn2wOMPEM-I0iDAxkXt3uIr7xk-iHbT0U0TG3wR0v7_Kba6-VSLxiSf40bxgPIIk_BAgS-3dIQffgG59RbnE8365U-jRkQTSgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd2127aec.mp4?token=lTKPB9sbhSNQXX112g5yDwykmSlcnP7G3_DomL-zFkA9SPG6O_T43PIPoIMOehBdRPjWJJqOifg-NoJ2ulpvX98fGcrmN8_6oUk7Z-mr-u4YI1zXl2AxStk87SnEeUR-BVlFes5V5GvITPjoD-2FoK2whC0zz-z1LbvaJbglVGLjn9q0x_RSzv4iVgID_85__6H9UKVLkhaRYjgt9wx4d7endtcT6ZWpKhRIxi92yUJzNhgSPNF1dn2wOMPEM-I0iDAxkXt3uIr7xk-iHbT0U0TG3wR0v7_Kba6-VSLxiSf40bxgPIIk_BAgS-3dIQffgG59RbnE8365U-jRkQTSgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سوال عجیب خبرنگار از رئیس‌جمهور: نوه‌هایتان به شما نمی‌گویند کاری کنید که مدارس مجازی شوند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/681665" target="_blank">📅 14:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681664">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
قالیباف: ما در بُعد نظامی و سیاسی جنگ پیروز شدیم
🔹
امروز ما در یک جنگ ناجوانمردانه‌ هستیم که در رأس آن آمریکا و رژیم صهیونیستی قرار دارند، اما ملت ما شجاعانه، مردانه و خالصانه ایستاد و جنگید.
🔹
بنده به‌عنوان برادری که به جزئیات کار آشنا هستم با همۀ وجودم می‌گویم که ما در این جنگ هم در بعد نظامی و هم بعد سیاسی به معنای واقعی پیروز شدیم.
🔹
تفاهم‌نامۀ بین ایران و آمریکا سند افتخار و پیروزی در راستای تثبیت پیروزی در میدان دیپلماسی است.
🔹
البته معتقدم که مردم ما حس این پیروزی را به گونه‌ای که اتفاق افتاده، حس نکردند و در برخی موارد نتوانستیم این حقی که مردم داشتند را به درستی ادا کنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/681664" target="_blank">📅 14:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681661">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316b3b1377.mp4?token=DPyDJIJzvBeukyZZNoHgPw3DOFtgzAFbovbdPXGNkDxX4hkh85g_mWF89O5l3xobtNF80L84AGCEcZRHMF22_dFp-j99wbQqi7KHXbrlSDA46qwoQpxnwFTHdZ8Q1lmKSF51RGcKAgA_uDkW59U24jAyCQXmijgwPPJRTZ6RgY2E9PbTS8aReIjI5oE6Fg3bcegydrhhGx65hwWT0JFG2U5G8F_g37PNGhjJhlRsQpN4HIXxAuULBlfRwzkgJP2L-6gghZfJSljTVrKryuKASNFjxV9H4rD2dsBTs8nNQIEex_PQeciMcgIPoTRgXSNJOOxX-Af1DxGZXX4i5DRWGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316b3b1377.mp4?token=DPyDJIJzvBeukyZZNoHgPw3DOFtgzAFbovbdPXGNkDxX4hkh85g_mWF89O5l3xobtNF80L84AGCEcZRHMF22_dFp-j99wbQqi7KHXbrlSDA46qwoQpxnwFTHdZ8Q1lmKSF51RGcKAgA_uDkW59U24jAyCQXmijgwPPJRTZ6RgY2E9PbTS8aReIjI5oE6Fg3bcegydrhhGx65hwWT0JFG2U5G8F_g37PNGhjJhlRsQpN4HIXxAuULBlfRwzkgJP2L-6gghZfJSljTVrKryuKASNFjxV9H4rD2dsBTs8nNQIEex_PQeciMcgIPoTRgXSNJOOxX-Af1DxGZXX4i5DRWGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند ایده استایل شیک برای خانم‌های محجبه و خوش‌پوش #فوری_استایل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/681661" target="_blank">📅 14:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681659">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
امید به‌ زندگی در ایران به ۸۰ سال رسید
وزارت بهداشت:
🔹
امیدبه‌زندگی کشور به ۸۰ سال رسیده درحالی‌که سال ۱۳۵۷، ۵۵ سال بوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/681659" target="_blank">📅 13:51 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681658">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
مصوبه مجلس: ۳۰ سال زندان برای پیشنهادات سیاستی یا تقنینی یا اجرایی به نهادهای حاکمیتی و دولتی که برخلاف مصالح اساسی نظام است یا آرای مردم را ‌به نفع گروه یا جریان خاصی جهت‌دهی کند/ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/681658" target="_blank">📅 13:47 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681657">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfae86d8e4.mp4?token=uqsh7FTCgkTee_VErxSBJ0qQoxYRybFsu_IfZRdOHi8K18lKVc7skpfU5bV4da9EfgIOGZKUn73ut5_bzV7yAIBRfAix14SQExoBEWyIJvRhrAKKRFbzGcECa6qmbOMWuwaZ5M2bFqjDn7jc9dzZ2AY4dNDUN62GPZgx6ST_11Dl1LJQR0Dv4Iht9gv-02ML9yi1NQ406le2n1kT-Q58WALNxUWP-nwLKTclxambTw7zUcHrZz72t0CssUiW7TQ4ZRbMvHd4xoqbNvLdrDbcEOf0LPEDdyJhIB-dpQOy96cfRwL_lkzxZ8fGerJO_nnvUknyB86yxx2B1OmBUT6jOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfae86d8e4.mp4?token=uqsh7FTCgkTee_VErxSBJ0qQoxYRybFsu_IfZRdOHi8K18lKVc7skpfU5bV4da9EfgIOGZKUn73ut5_bzV7yAIBRfAix14SQExoBEWyIJvRhrAKKRFbzGcECa6qmbOMWuwaZ5M2bFqjDn7jc9dzZ2AY4dNDUN62GPZgx6ST_11Dl1LJQR0Dv4Iht9gv-02ML9yi1NQ406le2n1kT-Q58WALNxUWP-nwLKTclxambTw7zUcHrZz72t0CssUiW7TQ4ZRbMvHd4xoqbNvLdrDbcEOf0LPEDdyJhIB-dpQOy96cfRwL_lkzxZ8fGerJO_nnvUknyB86yxx2B1OmBUT6jOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراض سرباز نیروی دریایی آمریکا به شرایط ناوها
🔹
یکی از سربازان نیروی دریایی آمریکا با انتشار ویدیویی، از شرایط ناوها انتقاد کرده و با لحنی طعنه‌آمیز می‌گوید: «بیایید عضو نیروی دریایی شوید!»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/681657" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681656">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf64a1bb97.mp4?token=MMH1qs8c3EHqUks-l4TEnwmz7NI0ruJNlgNNKG3EjhDSBaQn7VXgEcWi8q78ajkKDNTzL9fpb9d9nWyMcwQuPO6i00KTwnT4TRaKKYkImFvH0nk84auttPsj81Szd12wUjzYak_3MRx7ugFU94pJT-5hM0WJdul6I4twtCPHV85dbfBjoCINXIYlDk75EwyceSRarNYGdGkCgfPlepkE8fUWSD-qaiA2i1POVAoIOWZFhr66tW1G8jCrf5c50Vwe8cSm9evSEeVTyA9VW3tD4hi6vQwWagJkkHlfW5c0WLMr1Nuon2YFojKTiF2efY0-zt5XdrFVXWy3NpL41Li3PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf64a1bb97.mp4?token=MMH1qs8c3EHqUks-l4TEnwmz7NI0ruJNlgNNKG3EjhDSBaQn7VXgEcWi8q78ajkKDNTzL9fpb9d9nWyMcwQuPO6i00KTwnT4TRaKKYkImFvH0nk84auttPsj81Szd12wUjzYak_3MRx7ugFU94pJT-5hM0WJdul6I4twtCPHV85dbfBjoCINXIYlDk75EwyceSRarNYGdGkCgfPlepkE8fUWSD-qaiA2i1POVAoIOWZFhr66tW1G8jCrf5c50Vwe8cSm9evSEeVTyA9VW3tD4hi6vQwWagJkkHlfW5c0WLMr1Nuon2YFojKTiF2efY0-zt5XdrFVXWy3NpL41Li3PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متیو مک‌کانهی ۴۰ دقیقه ملکه زنبور را در دست گرفت
🤯
🔹
متیو مک‌کانهی برای فیلم جدیدش، ۴۰ دقیقه ملکه زنبور را بدون آسیب زدن به آن در دست نگه داشت تا هزاران زنبور دورش جمع شوند و این صحنه بدون جلوه‌های ویژه ضبط شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/681656" target="_blank">📅 13:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681655">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81159e939.mp4?token=PfY3ybtddM_L0iEzzKapkFXVrkYtFLz89khHsAGuMJuBgSeN6bIGV2rU2Bw4q98mM7oVOkq6IMg7DZRrLp7AxJArBXWSHFo96MYPz0hl3ZNVnyJ-9TjfgJNF8mBQo3y-dUL8ebTkmQCPwSsgeBwCHii51asPumXyhD1OBdjVwUKGN3BC08TJQglyBOu1mSeIhJzGqI5XEw4SPlwsOSaJdQ9hAHqGhnT7g_9AHNjtdMVGB4a6bSWecs6ojf0tqoAxQYNPCUTZB7qbD10Br7lMLd7wCtnlRwEr1hrcBA5eXP50m6FA_X1IL7JIwFh60qzv-mhHoG77d-Id7MIyf0qfIDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81159e939.mp4?token=PfY3ybtddM_L0iEzzKapkFXVrkYtFLz89khHsAGuMJuBgSeN6bIGV2rU2Bw4q98mM7oVOkq6IMg7DZRrLp7AxJArBXWSHFo96MYPz0hl3ZNVnyJ-9TjfgJNF8mBQo3y-dUL8ebTkmQCPwSsgeBwCHii51asPumXyhD1OBdjVwUKGN3BC08TJQglyBOu1mSeIhJzGqI5XEw4SPlwsOSaJdQ9hAHqGhnT7g_9AHNjtdMVGB4a6bSWecs6ojf0tqoAxQYNPCUTZB7qbD10Br7lMLd7wCtnlRwEr1hrcBA5eXP50m6FA_X1IL7JIwFh60qzv-mhHoG77d-Id7MIyf0qfIDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت اندیشمند برجسته آمریکایی از ۳۰ سال نیرنگ و عملیات آمریکا علیه ایران؛ از ترور تا جنگ اقتصادی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/681655" target="_blank">📅 13:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681654">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
ادعای اکسیوس: ترامپ از طریق بارزانی با سپاه تماس می‌گرفت
ادعای اکسیوس:
🔹
مقامات دولت ترامپ کاری غیرمتعارف انجام دادند؛ آنها مذاکره‌کنندگان ایران را دور زدند و مستقیماً با رهبری سپاه تماس گرفتند.
🔹
فردی که آنها برای کانال ارتباطی انتخاب کردند، نچیروان بارزانی، رئیس منطقه کردستان عراق بود که چیزی داشت که کمتر کسی دارد؛ اعتماد رهبران ایالات متحده و سپاه.
🔹
بارزانی در طول جنگ ایران و عراق در ایران زندگی می‌کرد و در دانشگاه تهران تحصیل می‌کرد؛ او به زبان فارسی مسلط است و روابط شخصی با بسیاری از اعضای ارشد ایران، از جمله اعضای ارشد سپاه پاسداران دارد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/681654" target="_blank">📅 13:09 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681653">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e64d209d9f.mp4?token=jmUQioUHzSF5mP9kTmfeux5LiNBhzB5n7hLfRQbgf0f6t_nnyC__JhvRPsd4SyzzMUd1w1vZ0SmytWji6Jkzkj3Lkkd3-MRo1DmFaVMeoEXUHjS8HXSYfHnaPsIag9kFOwJoxlFuw5OIHfv2oXLmjz8zwudXB9aoGa_9cXdd-HAQGnmyhpSS15GcFwfwenOxBGGGO7bpv0LdV8wfoqC7N5P2hxWobl-2BiZqBhzLx4Iu2IabQuFbr48APr20kDKPQDIphjNR22hZCLxz4BNLNdCzfzU7v7GBTIMWmgZz_KVWdvibPIIj5q0TFCsYRinDlY9S0cvcOum5z1ZJSq8fvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e64d209d9f.mp4?token=jmUQioUHzSF5mP9kTmfeux5LiNBhzB5n7hLfRQbgf0f6t_nnyC__JhvRPsd4SyzzMUd1w1vZ0SmytWji6Jkzkj3Lkkd3-MRo1DmFaVMeoEXUHjS8HXSYfHnaPsIag9kFOwJoxlFuw5OIHfv2oXLmjz8zwudXB9aoGa_9cXdd-HAQGnmyhpSS15GcFwfwenOxBGGGO7bpv0LdV8wfoqC7N5P2hxWobl-2BiZqBhzLx4Iu2IabQuFbr48APr20kDKPQDIphjNR22hZCLxz4BNLNdCzfzU7v7GBTIMWmgZz_KVWdvibPIIj5q0TFCsYRinDlY9S0cvcOum5z1ZJSq8fvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنجال در اوگاندا؛ بازسازی دوران استعمار
🔹
برخی از گردشگران سفیدپوست در اوگاندا با پرداخت پول به افراد محلی، خود را روی تخت‌های آهنی حمل می‌کنند؛ اقدامی که یادآور دوران استعمار است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/681653" target="_blank">📅 13:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681652">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
مصوبه تازه مجلس؛ حبس برای ارتباط با رسانه‌ها و نهادهای خارجی
🔹
مجلس با ۱۸۳ رأی موافق طرح مقابله با نفوذ سرویس‌های اطلاعاتی و نهادهای بیگانه را تصویب کرد.
🔹
طبق این طرح، مصاحبه یا ارتباط با رسانه‌های آمریکایی و صهیونیستی یا رسانه‌های تأمین‌شده توسط آنها می‌تواند مجازات ۶ ماه تا ۲ سال حبس داشته باشد. ارتباط با سفارتخانه‌ها و نهادهای غیرایرانی نیز بدون اطلاع‌رسانی و مجوز کتبی وزارت خارجه ممنوع شده است.
🔹
این طرح همچنین برای برخی اقدامات تحت اشراف سرویس‌های بیگانه، مجازات‌هایی تا ۳۰ سال حبس در نظر گرفته و رسیدگی به جرایم آن را در صلاحیت دادگاه انقلاب قرار داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/681652" target="_blank">📅 12:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681651">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21c4c920b9.mp4?token=EN51qq6RTdJMbDZdB0c51hGkXAC0JQhYjEJyT2SB2Hs4Qzign1uT1FnsNWHVyxIPvcsTZw2QPnLNWSX8mIUa687Rh3qgBlTgpCLKjemXssL-zFPukvTX6k1bm4_L2b6SmkjyZuVYot1jQsnh3kmiKaFnF0-_cMn9107SpDU4d0KfRlPlZsPAyVi8vsXCgi8TjrExZ4VbKk14c_YjLLNmOcH6Y9lp8RJPFEuqGzz7Xni3DUct-iIFiQMQGs31PKCZFA8r81izQBmch6F9cYRs3zgV75bkCfn1ceyHewLhzxFdtXK05DdOKnX_gfoSBKwND3aoGjHn3tJq2RUWptEpUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21c4c920b9.mp4?token=EN51qq6RTdJMbDZdB0c51hGkXAC0JQhYjEJyT2SB2Hs4Qzign1uT1FnsNWHVyxIPvcsTZw2QPnLNWSX8mIUa687Rh3qgBlTgpCLKjemXssL-zFPukvTX6k1bm4_L2b6SmkjyZuVYot1jQsnh3kmiKaFnF0-_cMn9107SpDU4d0KfRlPlZsPAyVi8vsXCgi8TjrExZ4VbKk14c_YjLLNmOcH6Y9lp8RJPFEuqGzz7Xni3DUct-iIFiQMQGs31PKCZFA8r81izQBmch6F9cYRs3zgV75bkCfn1ceyHewLhzxFdtXK05DdOKnX_gfoSBKwND3aoGjHn3tJq2RUWptEpUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۴ مدل گره با طناب که می‌تونه به کارتون بیاد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/681651" target="_blank">📅 12:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681650">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crScds7K8kVjul8dksYGSXikdN5atQYi2wfOJysp5mJCi4QPWNrCJBy6DiFQ_YyIsQZ38EgKX7ZT2_KRG7w9WUsKgE4yXaprKksLHq4pL-pE-k1KwMAPXbiepwgInyM3-cfjtHSYtSs2AJIqUjf2uYN8ulDimNS-VBD0heTHHCzTppJFywz6_AeT9lht9ro7WGYF78l9bTci9OE3PuS9DGpBa3f6zSSlmab7yb0b3eFKto5ibD2kE2wESQyTXhylSVI9PdgwrOGSzv4wS3RZT0h90kCx-edNJ5hLAiBN8gwQO7aw5XYDyNS8AXvUoWPYqPU5xwfYjJ6NhFhB4u9eWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_خودرو
| قیمت روز خودرو های بازار کشور؛ امروز ۲۵ مرداد ۱۴۰۵
🔹
بازار خودرو ۲۵ مرداد را صعودی آغاز کرد و بیشتر خودروها گران شدند، اما رشد محدود قیمت‌ها نشان می‌دهد بازار هنوز با یک روند صعودی قدرتمند فاصله دارد./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/681650" target="_blank">📅 12:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681647">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gASj4qe2PWCfYgAOhMQCQyrEmvMW8WlHgLF3mnqp9HRn6WND_z7xcqVZqWRx2Ql2GBpaJHxX2PbExKbJd52NjT_ZVLPQ7ixOzNzJX5PCxxYtiDFWojj89UNUQQZLxLjVHU3TqrGBP9dfMTI1Z2Jml2Lq8AFAbQx95XHB-wMpAS-Nlar6JXV6umRCAVUaK-3BGWGexU-JIZpvMxVQMQ_EUhgCZO761rk8nOZb9hegrudsUlLuKh3dD4U7QpQlJd1ig07I3m5p3M4VfgR0i2BuIDblElv7NGBUHhqafbr651XI4Wx_wF7-Q0BXNTm6Pvyle-a_0MMx7LhvfaUS8TEb5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امارات برای حمله زمینی آگهی استخدام سرباز داد | کشوری که یک تیم فوتبال نمی‌تواند جمع کند چگونه می‌خواهد بجنگد؟ | ماجرای «سربازگیری» ارتش‌ شیشه‌ای
🔹
وزارت دفاع امارات متحده عربی اخیرا با انتشار فراخوانی گسترده، از نیاز خود به جذب نیروهای تازه برای پیوستن به نیروی زمینی ارتش خبر داده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3237916</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/681647" target="_blank">📅 12:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681644">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MA-mZjex3CkQbHbDlf5q4bimuVRhjfqegDhRf-MeA3fWDHgbGQ-jqyLw6GWOj__AKRRJ_2Zgb_wJ1_ONumSBHLifGwHcNo8RGOjzakP5JxIJGXL7d6U9fwn6lF6XTcGyhhDLIJOt7vLbCEmp8lmaFyFMBNzMgISvFnzj0AGjCrMHE2YmUrEAXMU12LL0Hz-7aYP-NJPD9UGtB8fkuUh8ibB5wP3FPQ47ade7EYWHhlyBaHHUT4752JF6fr4iVkNBber6EfeLU1mL8hXXx3_BF5ynUBUneA5N-EJu6nnbATuJaNOYqoUlCbmPRyNdqPOeUUcPkLq4oTdnURo1ODSo1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jogdAYpvk_5T1X2vRUJ3aY0qNHI2BkDpn2PYnyqgGKQ6s8dHLp4bDRcqxDiZxSIDm9cu1if8owo7uttB7RWtHcQh6XKQBS4y3MAS1rPNPoh_j45XoTacH0YrpxDeKz3t_OnYPxDZKKNdR3Q13KMpMVPcuMRnz8hcb0ktUbhQdD1KzxZ8mxsQb34eKDUQu3d0fj-4oibDFuuXtAfA3v1eUqThxs1qWnbzAa2DVGjDjaBT1iF8kYUANLsdZtKH9FZpYiO6f33Xb-rtay6gMIUCmctLOD4cTZHiuGRRkXCmdICsRRHeN-Ak-FvGLAC4UVW7vJCTb6x07L1mg3Gnt2IM3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LFmXE5End3GrHvY2TYN8OkDhuAl9-1e8jJQ4JA_v_oSK8hp33CCPR-DMQ1TIbaBf_DutMCS1lX6aJqenSmqTIxEVlB_Qpyx8RM0Z2aatNwwm03IxthYy9-B--0FeGhUowgaezekWwu5zTBmpUgk4ghGtaxb05UOotiCQFSIsLVveApW-CtTCem8wQiT8OCKxfvqQffW-EHBd32b6iPuCtUvh4jGYF0hbO6L9fHhgsdK1sQb9Zn1597n8MKALa4XNT3olIi2TbY526Wvc8BprEBa18tZ63QRF4iBO6NEXS3KejKoOQdPg7HwDtp3SOqR4P6BmGvEymnbn3Mio0Cmimg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
انفجار گلکسی S26 در جیب صاحبش؛ کاربر راهی بیمارستان شد
🔹
یک کاربر در هند مدعی شد گوشی سامسونگش پس از داغ شدن شدید در جیبش منفجر شده و باعث سوختگی شدید و آتش گرفتن لباسش شده است.
🔹
مدل دقیق گوشی هنوز تأیید نشده، اما تصاویر باقی‌مانده احتمال گلکسی S26 را مطرح می‌کند؛ سامسونگ هند تاکنون واکنش رسمی نشان نداده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/681644" target="_blank">📅 12:39 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681643">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک اقتصادنوین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNlZmEhp6jMzY0RKEKeeXRJ9rSWPnoV8E3tf2i4u_LBOeSyOJ4bgPBjGV11PTAEKhvL-Bex7HC9nkdtshMfiEmTMnUr8MLSaE3uybgEcvNu2UGj96_KqjUHbjWZL_TYulyAAnVfqKNkHG1KGcHdt5rbEa2sLTq-8x7DMacrANUrCZctfxEeCP5NoLx1jo_5SEP8xc4HaMyPQhV3q-mTj10QD7-J1306E_QSe6OyomY_ei5HLQ-Z5I8888WW_EL9_pJnpytOTpnnICwndGBVojmxnTr5CQBVZRLgy0a2yvGz2X1uyzKjbGenAA6iPCdfqtoN92N_-UsCcsJv1DwNTQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
«هم‌پی» اقدام پیشتازانه بانک اقتصادنوین برای رفع موانع تولید
🔹
بانک اقتصادنوین همزمان با بیست‌وپنجمین سالگرد تاسیس و با هدف تامین حقوق، تامین مواد اولیه، تامین برق و کمک به فروش اعتباری تولیدکنندگان و فعالان اقتصادی، از طرح پیشتازانه «هم‌پی» رونمایی کرد.
🔻
اطلاعات بیشتر :
https://enbank.ir/s/mfa9aC
☎️
02162740
🌐
www.enbank.ir</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/681643" target="_blank">📅 12:38 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681641">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e240d557c.mp4?token=PgddS8GS3lbpmXkm6siq9ioVSWCSPRu9NpERVBtYJzCrPfvvP3WV7rR8zlQaD_jVp2iKGW9ucixjeJKCSED0kmxUqh2dKntZj8eU4afC3Ry8DxQkOp_uCTfTKlqsfq9RUEz6VgqwOgaJFpoF4V6vy4gL8nRpgakNvvBRTy00M2vYvVVTzCOuQJKDbWQNPCJS4LbfAer3ToSjoTz7_4hpIwUAMAGGeJ6VO_nfyjC69HFTyS9-Ko3Vdh6FX34Wd6HwDUIOzMkmpieXujjcI8tAR9R0rupaOI2K5VnRGvaVpzhbrzSdBZJBrRWKdAagwc8SmlfQCfVWmzBZHVvbuv7axnLMrvnjheerTo5Q-8cpyqd7wRrlI34Hj1Wyhlh2XjkEx9CpUMBKRDdGtTR6NRJ6a9hcRuqiF3l7blmKXIKW6akweqgFdDzLqKetpCO-0sjIFDjIt79QJ3rLrzThRGHGaaRC7FNceClMLuAQ9piUIR4hco5nc3DJjdnTMlro20glOVSZsBhKndPSZBv_O6vJ8QHaJiHhOqvvDRZs46087-e0ZM43o1-n0FX0JCG1ap14AF_1V2RM6rXpzoNLZRR14UcS5YS0MQS89_WQvqN22QJEtW3KaACbu8gnPNraCZxREEdVHLR3UsolO5F8eaYH56DItJ9-tDVF_TUr-mSpaYM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e240d557c.mp4?token=PgddS8GS3lbpmXkm6siq9ioVSWCSPRu9NpERVBtYJzCrPfvvP3WV7rR8zlQaD_jVp2iKGW9ucixjeJKCSED0kmxUqh2dKntZj8eU4afC3Ry8DxQkOp_uCTfTKlqsfq9RUEz6VgqwOgaJFpoF4V6vy4gL8nRpgakNvvBRTy00M2vYvVVTzCOuQJKDbWQNPCJS4LbfAer3ToSjoTz7_4hpIwUAMAGGeJ6VO_nfyjC69HFTyS9-Ko3Vdh6FX34Wd6HwDUIOzMkmpieXujjcI8tAR9R0rupaOI2K5VnRGvaVpzhbrzSdBZJBrRWKdAagwc8SmlfQCfVWmzBZHVvbuv7axnLMrvnjheerTo5Q-8cpyqd7wRrlI34Hj1Wyhlh2XjkEx9CpUMBKRDdGtTR6NRJ6a9hcRuqiF3l7blmKXIKW6akweqgFdDzLqKetpCO-0sjIFDjIt79QJ3rLrzThRGHGaaRC7FNceClMLuAQ9piUIR4hco5nc3DJjdnTMlro20glOVSZsBhKndPSZBv_O6vJ8QHaJiHhOqvvDRZs46087-e0ZM43o1-n0FX0JCG1ap14AF_1V2RM6rXpzoNLZRR14UcS5YS0MQS89_WQvqN22QJEtW3KaACbu8gnPNraCZxREEdVHLR3UsolO5F8eaYH56DItJ9-tDVF_TUr-mSpaYM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دریا همینطور که بخشنده است بی رحم هم هست
🔹
این دو جوان هرمزگانی ۵ روز در دریا سرگردان بودند و بنزین تمام کردند که صیادان بحرینی آنها را پیدا می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/681641" target="_blank">📅 12:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681640">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
برداشت وجه از خودپردازها رایگان نیست
🔹
با بخشنامه بانک مرکزی برداشت وجه نقد از خودپرداز بانک‌ها به میزان نیم درصد مبلغ برداشت کارمزد خواهد داشت.
🔹
حداقل کارمزد پرداختی برای برداشت وجه نقد ۳۰۰ تومان خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/681640" target="_blank">📅 12:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681637">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f2-C5YOgFbaydNapVETho3elUP2Pe0HDlic3lt_7u-3lV7X58-s3RTSks-7PSgDwFB-iyVA86AJeQ2yHpwh_P0naei5hNz4U_abQx0Slm1SbqR2OoUkvDC0HNKVA_N5snLIi0t_2C9Kh1BwbUVsVJ7nbYB1iOYFGkwIBpsqE-JNUJ5yM5yKPfiPLtR4AzmJn9oipP4j8-5RW_Q0rakV3Q1H5BK1TDOY41nN8PP_CAzwLDCtmvO--gM87KeIi7K2Sn2CXbY_w71fCoT8E7T_kUjZEdkS0YsW47bSdNT9iwFff4ENL63ipEsgpgn2ElA4ZXBFvkgjMcMaATHaoP1KIXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ksyTorQbzj2A42CBTnt82BA9jj-RHanim3wDmWdWD1dChHo5lXJ6VNLU3Rdu_4e3RFSEriD0-5pqTgsgKUmlt5uQWyTkgS6hU6yLZOZ0SsH8deq1rz2Hs22AR0teyZ-oGTwbcNzhR2msvYII-M4XSWdpQwmurZG13vXzE__XOZx4B1wF8lyEN35hmSmhu5CrS93rmWG8Yogny8ChZ_TfPs7WETJpRg8cxsDCaAFl3l31r_SVL-QAe5WMxKj8Mbx8fWKo0Hrs6ao-KF2TI9kegCRK8Gsb3YMcx-pmV9B8XdKywhZLqD1XJYF_IPcU8OKOpoHcRwfUGEZmx7wqC5AWYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بینی‌مو عمل کنم، خیلی کیوت میشم!
🔹
فقط بینی نیست، وقتی عمل زیبایی از سن کم شروع میشه، خیلی وقت‌ها بعدش یه ایراد جدید پیدا میشه و دوباره نوبت تغییر دادن یه جای دیگه‌ست.
🔹
انگار این روزا بعضیا تا وقتی چند جای صورتشون رو عوض نکنن، باور نمی‌کنن خوشگلن!
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/681637" target="_blank">📅 12:23 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681636">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bb740b035.mp4?token=aAUDJLOOie-sQmKohDrv3phd-agO7noQs8GoySrVuDMhf3RhMBANQakvfVp8U3j-8AyOn3V1lsKtBoiXJarmyOd1RiBF4ul9m6x6JyqOe7AKkgOCbsV4WrLDKNDapcKEF0JvEQ7cQQOB6spyg6OBE1mdseqhAkY-0N4QaGb-3JdObnAEqVG2eLELIlCInmS3nBXcJjG3C0qciiBY_BVL3eGwmhduC7AtqFp6P5lfky4zKXm9wZDFkOjS1quxlI2O9lXMNoZ3eec-33hKKHDGRTfCKWVbAcq1CwKR8t7FGAlEtbcs5G9aY2VaLyiRDdTMLKhDgzgrYmoyyVCoNEtL0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bb740b035.mp4?token=aAUDJLOOie-sQmKohDrv3phd-agO7noQs8GoySrVuDMhf3RhMBANQakvfVp8U3j-8AyOn3V1lsKtBoiXJarmyOd1RiBF4ul9m6x6JyqOe7AKkgOCbsV4WrLDKNDapcKEF0JvEQ7cQQOB6spyg6OBE1mdseqhAkY-0N4QaGb-3JdObnAEqVG2eLELIlCInmS3nBXcJjG3C0qciiBY_BVL3eGwmhduC7AtqFp6P5lfky4zKXm9wZDFkOjS1quxlI2O9lXMNoZ3eec-33hKKHDGRTfCKWVbAcq1CwKR8t7FGAlEtbcs5G9aY2VaLyiRDdTMLKhDgzgrYmoyyVCoNEtL0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خداداد عزیزی: علی دایی خیلی خودخواه است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/681636" target="_blank">📅 12:17 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681634">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
این دفعه اگر دچار اضطراب شدین، کارهایی که همیشه انجام می‌دین رو برای یک لحظه رها کنین #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/681634" target="_blank">📅 12:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681633">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84417c6223.mp4?token=O9TNNfdh8hqaJi-jEM5FAMV5-hGqJu4OFktTDCMJK7mhsM-jGYCc0ADDf_QLejo-oxQsiEBXU9aagOGxLCiAJfFE1n6qy5aov7omN7mQeOjS3Tn9NkaFrYgq2IKF8O23_-xW0BlfkIIWnTBSWTVCabsSb5jI6-udesN5xRTQQdbU2k9kcJw9fFueFD2x92vwRlxvc6-5qPCLClTUuyDsKFY8AFNOwTPqFv8aiKERtHwmW3GqxAihP_5q5YnRxJZXo_BVKZuwgdrOi2mRqgB5jiLEOXR9GI0tc8-ghoJKB2qo1MK05nlPF95oLSmgT_nyXqZE0e45ox1wj3kCaUTOQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84417c6223.mp4?token=O9TNNfdh8hqaJi-jEM5FAMV5-hGqJu4OFktTDCMJK7mhsM-jGYCc0ADDf_QLejo-oxQsiEBXU9aagOGxLCiAJfFE1n6qy5aov7omN7mQeOjS3Tn9NkaFrYgq2IKF8O23_-xW0BlfkIIWnTBSWTVCabsSb5jI6-udesN5xRTQQdbU2k9kcJw9fFueFD2x92vwRlxvc6-5qPCLClTUuyDsKFY8AFNOwTPqFv8aiKERtHwmW3GqxAihP_5q5YnRxJZXo_BVKZuwgdrOi2mRqgB5jiLEOXR9GI0tc8-ghoJKB2qo1MK05nlPF95oLSmgT_nyXqZE0e45ox1wj3kCaUTOQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔧
دیگه برای هر کار کوچیکی دنبال تعمیرکار نگرد!
دریل و پیچ‌گوشتی شارژی ۴۷ تکه؛ همه ابزارهای ضروری رو یکجا داشته باش!
💪
✅
موتور قدرتمند و شارژی
✅
مناسب باز و بسته کردن انواع پیچ
✅
ایده‌آل برای سوراخ‌کاری چوب، پلاستیک و فلزات سبک
✅
همراه با ۴۷ قطعه کاربردی
✅
سبک، خوش‌دست و قابل حمل
✅
مناسب منزل، محل کار و کارهای فنی
🔥
قیمت قبل: ۲,۲۹۸,۰۰۰ تومان
💥
قیمت ویژه: ۱,۸۹۸,۰۰۰ تومان
🚚
ارسال سریع به سراسر کشور
💳
پرداخت درب منزل
🎯
ارسال رایگان در صورت پرداخت آنلاین
👇
برای سفارش و مشاهده جزئیات، روی لینک زیر کلیک کنید.
https://memarket24.ir/product/fast/35160/180124/</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/681633" target="_blank">📅 12:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681627">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1278d5aaa1.mp4?token=Zw73ruFppjQ3cFbjgdkIRe1DsaMrbqeaJKKrOeEGMNkkbxO5cd7ASJGIT_8eN2E7zWeJJ7gzQUpmrO0r2oBBmdI1sIQoTRkepIA9BfkthaGcnzfHhmL6KfQ7MDTfgVC3LYE2JMbNED9brQOGzPQ83oP6ODVQBLX2xThMxvn1pmG77Kiim5aU6mLybm9ZWr1u6jEWfiKJLgHvVB0850IM7EZ3ZNzlobS8F_CUgL4DrtmvO0TjafqgPwjtAnQEm2jX-WLcWCiSZw3xvo0rBCMbey2XV7lncTZ2vz4NCJgJ5gRM3REGzeWhvde-ZxXkkxh5U3bW6ZqSlKm1dwC2RYI6ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1278d5aaa1.mp4?token=Zw73ruFppjQ3cFbjgdkIRe1DsaMrbqeaJKKrOeEGMNkkbxO5cd7ASJGIT_8eN2E7zWeJJ7gzQUpmrO0r2oBBmdI1sIQoTRkepIA9BfkthaGcnzfHhmL6KfQ7MDTfgVC3LYE2JMbNED9brQOGzPQ83oP6ODVQBLX2xThMxvn1pmG77Kiim5aU6mLybm9ZWr1u6jEWfiKJLgHvVB0850IM7EZ3ZNzlobS8F_CUgL4DrtmvO0TjafqgPwjtAnQEm2jX-WLcWCiSZw3xvo0rBCMbey2XV7lncTZ2vz4NCJgJ5gRM3REGzeWhvde-ZxXkkxh5U3bW6ZqSlKm1dwC2RYI6ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
من تاریخ سرزمینی هستم که بسیار کوشیده‌اند راز پایداری‌اش را دریابند #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/681627" target="_blank">📅 11:36 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681626">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWeImGOewfM4I4nXEMlRQJs7YXN_9oBTUvSoixxzKzQiHt2tiTa2lzRZGEvXzhe4tMgGpKkmPZp5a2PCL5TMokJ33vK_Aja3U5hh90iLyt-jrC3Tp3N1fp4hbRiODhiWN97dOgPu3R2lpoR2s4MSE104stYniMDXMGjIojVEA6b-87u5esyhyycfhrNBvCINiUo0w5uP2HZlWqvvQ2YszERLX5O4lUyFLVGr_pt-heLWPyEp_gvsZhr2DgryHpNCLPEex6QmjtVZGGqlcZMNmLPIBhzHDMJS04WVb_b41qp6YTSXlDJJnapW02uwdc1N52w2Zp2sy_42KWsJVqkMqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۴میلیون نفر در سنین فعال ازدواج مجرد هستند
🔹
همراهان گرامی خبرفوری؛ برای شرکت در این پویش کافی‌ست یک پیام صوتی حداکثر ۱۵ ثانیه‌ای ارسال کرده و از دلیل تجرد خود برایمان بگویید.
🔹
برای حفظ حریم خصوصی، صدای شما تغییر داده می‌شود و هویت‌تان به‌صورت ناشناس باقی می‌ماند.
🔸
روایت کوتاه شما می‌تواند بازتابی از تجربه‌های متفاوت مخاطبان در این زمینه باشد
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/681626" target="_blank">📅 11:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681624">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
کارمزد ساتنا و پایا هم با دلار بالا رفت
🔹
کارمزد پایا ۳۳ تا ۶۰ درصد افزایش یافته و به ۴۰۰ تا ۱۲ هزار تومان رسیده؛ سقف کارمزد ساتنا نیز ۵۰ هزار تومان شده است.
🔹
کارمزد کارت‌به‌کارت تا یک میلیون تومان ۱۱۰۰ تومان و برای هر میلیون اضافه، ۳۵۰ تومان بیشتر محاسبه می‌شود.
🔹
پیشتر رئیس‌مجلس گفته بود که افزایش نرخ ارز نباید بر بسیاری از کالاها و خدمات اثرگذار باشد؛ چرا که اساساً ارتباطی با ارز ندارند./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/681624" target="_blank">📅 11:27 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681620">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4ti4o1szYVrgNiWHn6KLVyPkufnRfXIHKf9VzrH8Muap1FyK7rxfVp8sNZob_oYS_wo3UwiuQOLcdwtlaLWtOht_NXHGxcKDtUQJpPZ0bj8An4bMLv9ywKc5-igcRkGghA8rm7m9zDNJIcGGu6-ChkeQA4GxkXMqzM-q4YYPQi--5OH-pHKEkJv2rJo1w_rxfkREuPuvY3W8sOG4m3XFwkeQWVF2oIDDw1_2oA5br7kFFd5AIOw5I0ACdW9DbQGRm0kDZth1rX4tU_JlF9Td-KSOl0FClP-7CNGPZEbdAxgnVyVauQoU4lL-csJvTpm-FRhAmw8MRqZx0MUkqQxpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا بیشتر از غرامت متفقین از آلمان، از ثروت ونزوئلا اخذ می‌کند!
فرانسیسکو رودریگز، اقتصاددان سرشناس ونزوئلایی-آمریکایی:
🔹
به گفته یکی از اعضای کمیسیون دولتی ونزوئلا، آمریکا تاکنون در سال جاری، ۴.۷ میلیارد دلار از ونزوئلا بابت هزینه حمله به این کشور دریافت کرده!
🔹
که معادل ۳۲٪ از صادرات نفتی ونزوئلا در همین مدت است؛ برای مقایسه، آلمان بین سال‌های ۱۹۲۴ تا ۱۹۳۱، ۱۳٪ از صادرات خود را به‌عنوان غرامت به متفقین پرداخت کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/681620" target="_blank">📅 11:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681619">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e99e81e0.mp4?token=HN97xzxZCf85gD2dxVYqvcxCELV8DGM2raN9kvv47kagqsxd_kOGnPyb_TlTVqmog2EUI74MfQez_MNU5swsIBIfzVZ-rKJZY0NEqdspxpJq3Dr9UGKBhgjaIbXLRbVMSKvv40aMq-azNrzzRmxRKjLh2SPUhrBCDmNcdT59ZgAnCKE2Gp-YrTNOFqFesRu_VmDIfo2C5sY4vDxvJSULBn4YjCBchNq1TSUR7lB4znts8QOuhMdj39L4S2GHFYwQG-UfqTDIvhAMBKQXBbmZlfAT6_tdRqP913ZQbM8VkaR5LYQD4KGJUq3rvH4LA7uNr3aoCYZtlgi0OwjIGn_MB4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e99e81e0.mp4?token=HN97xzxZCf85gD2dxVYqvcxCELV8DGM2raN9kvv47kagqsxd_kOGnPyb_TlTVqmog2EUI74MfQez_MNU5swsIBIfzVZ-rKJZY0NEqdspxpJq3Dr9UGKBhgjaIbXLRbVMSKvv40aMq-azNrzzRmxRKjLh2SPUhrBCDmNcdT59ZgAnCKE2Gp-YrTNOFqFesRu_VmDIfo2C5sY4vDxvJSULBn4YjCBchNq1TSUR7lB4znts8QOuhMdj39L4S2GHFYwQG-UfqTDIvhAMBKQXBbmZlfAT6_tdRqP913ZQbM8VkaR5LYQD4KGJUq3rvH4LA7uNr3aoCYZtlgi0OwjIGn_MB4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوشی جدید Honor با دوربین رباتیک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/681619" target="_blank">📅 10:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681618">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UW1-dD9v9zlz-jWnAzUIYvNsEds2DGR_qXMAZitiLOBvd6xNC-B7yPvMlK15MLfMWBvkzYkzU8btynY9LC63ECKtDUKLS5tRcmZlSFVd38mWH_qOTrtSNKiiZUBPtP_bEIpbrRSiusjQzIDDTOShAWHQpFE8InUwnTYUno5yKy8gWM5t4FtMU1l1lDdo0fSePKSvRFL5FvETQzz0-tqX8MX95EXkXtODWUiN4DEouazOmF_LC6gYsiEzJd7L_t3mKiOIfNK_dp2FDIPTH0p1jvdeCgQdK4fqARodrwymRg0soQ_A9CeYf5G3fyX5hPrRQnS6AZoxxJ0b6thOCjC2Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری متفاوت از کودکی رهبر معظم انقلاب اسلامی در آغوش رهبر شهید ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/681618" target="_blank">📅 10:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681615">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6702fd240b.mp4?token=i88V5ZHyfXEiTvUGmBKoRha3hySTCmUYONZGqb6optyiw-tLtNaERXEYlk7IqorYRDjfp7ibh20uaaN77nTrg0Us9z1SJbPFmZ79EqmfTHJQmMF_zKWj3jhlQxGHy_n0zWxnz_ZfePugQkVteoYNTWUpzJgD7GFFSC1Dm8k2Mqo4koH-o8t5xPcjHdmurs5zoqBpxy0NuBREVDZBvIDqjgs3j_IkPp2zssOwrL6wVKejrJ7v5CBcZFOF5KuNMSvNr6t1hMeAajPybgyqaH_ZN7-s3TgTjIiB9LEe14j2ud8_aXuY5FawIXtfgXH1U-QyZ4dAiFD3NKM_vqupYpu26Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6702fd240b.mp4?token=i88V5ZHyfXEiTvUGmBKoRha3hySTCmUYONZGqb6optyiw-tLtNaERXEYlk7IqorYRDjfp7ibh20uaaN77nTrg0Us9z1SJbPFmZ79EqmfTHJQmMF_zKWj3jhlQxGHy_n0zWxnz_ZfePugQkVteoYNTWUpzJgD7GFFSC1Dm8k2Mqo4koH-o8t5xPcjHdmurs5zoqBpxy0NuBREVDZBvIDqjgs3j_IkPp2zssOwrL6wVKejrJ7v5CBcZFOF5KuNMSvNr6t1hMeAajPybgyqaH_ZN7-s3TgTjIiB9LEe14j2ud8_aXuY5FawIXtfgXH1U-QyZ4dAiFD3NKM_vqupYpu26Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوشمزه‌تر از این لقمه پیتزایی برای  دورهمی و‌ مهمونی‌ها نداریم
🤌🏻
😋
مواد لازم برای ۱۰عدد لقمه:
🔹
هات‌داگ ۳ عدد
🔹
قارچ ۸ عدد
🔹
نصف یک عدد فلفل دلمه ای
🔹
پنیر پیتزا به مقدار لازم
🔹
نون لواش دو تا سه عدد
🔹
نمک/زردچوبه/پاپریکا/فلفل‌سیاه/آویشن به مقدار لازم #آشپزی
🇮🇷
…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/681615" target="_blank">📅 10:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681614">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCCd995w6KfBL8GR8sHKl1guUZ6mcMjURfDnwxWhGLYCalKk-i8kiEm8l5dBjYKEhBcDNCgLYExBTLyvAzrPk4D6KwlAKrfjbVxp18yUHR8gsunv6GDwuevlYh6f7thfv5IzlngysvmVCS16FLyzD58wB5xscYYLLfog3SAXy49ysRVWP_UmXVJspuqR4zx978cW5Y3JOy44Yo5xfOEhpw8uXdqJnir6DPv-IchsHDH7kWwQ989drX2etrXmj71s2SquzmmgERBsHv6gX9msOA_uQHSqBh_lICKYRpSlvzr9DG4zqnL67SasgYX-wBFXNFr395gToVB2qWprI-NKvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طراحی زیست‌بوم جدید تأمین مالی برای اقتصاد فرهنگ و هنر
🔹
صندوق پژوهش و فناوری توسعه فرهنگ و هنر با دریافت مجوز از صندوق نوآوری و شکوفایی، با هدف تأمین مالی، سرمایه‌گذاری و تجاری‌سازی کسب‌وکارهای فرهنگ، هنر، رسانه دیجیتال و صنایع خلاق راه‌اندازی شد.
🔹
این صندوق با سرمایه پایه ۱۰۰ میلیارد تومان و مشارکت نهادهای دولتی و بخش خصوصی، قرار است حلقه اتصال میان ایده، سرمایه و بازار باشد و کسب‌وکارهای خلاق را از مرحله شکل‌گیری ایده تا توسعه و ورود به بازار همراهی کند.
تولید محتوای دیجیتال، بازی‌های رایانه‌ای، انیمیشن و توسعه پلتفرم‌های نوآورانه و فناورانه مرتبط با فرهنگ، هنر و رسانه دیجیتال از جمله حوزه‌های مورد توجه این صندوق هستند. همچنین کاربرد فناوری‌های نوین، از جمله هوش مصنوعی، در توسعه کسب‌وکارها و محصولات فرهنگی، هنری و رسانه دیجیتال  مورد توجه قرار دارد.
🔹
سیدصادق پژمان تصریح کرد: این اقدام با هدف حرکت از حمایت‌های بلاعوض به سمت تأمین مالی مولد و پایدار و تقویت نگاه اقتصادی به ظرفیت‌های فرهنگ و هنر شکل گرفته است.
#صنایع_خلاق
#اقتصاد_فرهنگ
#فرهنگ_و_هنر
#اقتصاد_خلاق
#سرمایه_گذاری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/681614" target="_blank">📅 10:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681611">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1efd2fb41c.mp4?token=o2uoYI3ZsA4RdudLb1odCvjciOEXYCGKp7QPfhQKPEHMcuW_wKXo6wywm9pT6oQlIcrGdeoI75PDrh6QlM2Mp7smXWXSfFYBmk-Z29VOHFkFrUzMhzB8OVeBivWFXYNC2zMh9pvvX5_7c5tm3u-cveeeC1axy32CWW39e-ItqBl10sGC-2qJ2ClL3u-osgi7r6IuMxPNxxf8P902p8o9YccIvsjZwqyPKBO2p4uOXRWShXFuukfmxgP3jkYe5oInv8x2fwWl8do4ZcN1x9iNNFKQ1ytyWOQr8OON9_r_yb0ZvcIPVvzDssQmIqfMtE6O11PtK-_awebRu5ZqCJzhpXVb_Ap2eXVG-gY4i8AUtvgbIcdXIaRErdAdqJMs8pxWamcPutltmNq7feE_hY2jrYWqZwKi5rB9xsyYzbnBBbGX8EqAD9gGZR3oL4UuErz7iufM0Tqjs0Nf2RoWD5GkIkecnUfesr5wEgNJ6vgHO2eTsg6IZvy1HdZfcTs_ZGN5dRjTrd0ghvG1D4suLG6MJe5vWEDsVmRJ0JJbx0LtW4YjxPB0BCpTmjUts2ZMI4UC8KHjShVNDi8SIzCh21GGkaoDdVuM9s1GwvMlGMuEMSx0fLDp-Kz6xthkKSiwr78DKvINXgTnH_-hEVJRyrBCrja5-OnVzBojXYp4L-LAQkY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1efd2fb41c.mp4?token=o2uoYI3ZsA4RdudLb1odCvjciOEXYCGKp7QPfhQKPEHMcuW_wKXo6wywm9pT6oQlIcrGdeoI75PDrh6QlM2Mp7smXWXSfFYBmk-Z29VOHFkFrUzMhzB8OVeBivWFXYNC2zMh9pvvX5_7c5tm3u-cveeeC1axy32CWW39e-ItqBl10sGC-2qJ2ClL3u-osgi7r6IuMxPNxxf8P902p8o9YccIvsjZwqyPKBO2p4uOXRWShXFuukfmxgP3jkYe5oInv8x2fwWl8do4ZcN1x9iNNFKQ1ytyWOQr8OON9_r_yb0ZvcIPVvzDssQmIqfMtE6O11PtK-_awebRu5ZqCJzhpXVb_Ap2eXVG-gY4i8AUtvgbIcdXIaRErdAdqJMs8pxWamcPutltmNq7feE_hY2jrYWqZwKi5rB9xsyYzbnBBbGX8EqAD9gGZR3oL4UuErz7iufM0Tqjs0Nf2RoWD5GkIkecnUfesr5wEgNJ6vgHO2eTsg6IZvy1HdZfcTs_ZGN5dRjTrd0ghvG1D4suLG6MJe5vWEDsVmRJ0JJbx0LtW4YjxPB0BCpTmjUts2ZMI4UC8KHjShVNDi8SIzCh21GGkaoDdVuM9s1GwvMlGMuEMSx0fLDp-Kz6xthkKSiwr78DKvINXgTnH_-hEVJRyrBCrja5-OnVzBojXYp4L-LAQkY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت خداداد عزیزی از روزهای سخت زندگی‌اش!
🔹
ساندویچ نان و رب خالی می‌خوردم؛ به‌همراه پدرم دم حرم دستفروشی و گچکاری کردم..
🔹
برنج و مرغ تنها یک بار در سال و دم عید می‌خوردیم!
🔹
چلوکباب نخورده بودم و نمی‌دونستم چیه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/681611" target="_blank">📅 10:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681610">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-text">از سوی رهبر معظم انقلاب برگزار می‌شود
📢
مراسم بزرگداشت چهلم «آقای شهید ایران» در تهران، قم و مشهد
🗒
دفتر رهبر انقلاب اسلامی به مناسبت چهلمین روز تشییع و تدفین پیکر آقای شهید ایران، با صدور اطلاعیه‌ای از برگزاری مراسم بزرگداشت رهبر شهید حضرت آیت‌الله‌العظمی سیّدعلی حسینی خامنه‌ای در تهران، قم و مشهد خبر داد.
متن کامل اطلاعیه دفتر رهبر انقلاب اسلامی:
🏴
بسمه‌تعالی
▪️
هم‌زمان با ایام چهلمین روز تشییع تاریخی و تدفین پیکر مطهر آقای شهید ایران، مراسم بزرگداشت آن رهبر عظیم‌الشأن و خانواده ایشان از سوی حضرت آیت‌الله سیّدمجتبی حسینی خامنه‌ای، رهبر معظم انقلاب اسلامی، در تهران، قم و مشهد برگزار می‌شود.
▪️
مراسم‌های بزرگداشت قائد شهید حضرت آیت‌الله‌العظمی سیّدعلی حسینی خامنه‌ای به این شرح برگزار خواهد شد:
📍
تهران؛
🗓
سه‌شنبه ۲۷ مرداد، از ساعت ۱۷ تا ۱۹، در شبستان مصلای امام خمینی(ره).
📍
قم؛
🗓
چهارشنبه ۲۸ مرداد، پس از نماز مغرب و عشاء، در حرم حضرت فاطمه معصومه سلام‌الله‌علیها.
📍
مشهد مقدس؛
🗓
پنجشنبه ۲۹ مرداد، همزمان با شب شهادت امام حسن عسکری(ع)، بعد از نماز مغرب و عشاء، در حرم مطهر رضوی.
👤
از مردم قدرشناس ایران برای حضور در مراسم بزرگداشت رهبر شهید دعوت به‌عمل می‌آید.
🔻
حضور پرشور و گسترده عموم ایرانیان و دلدادگان امامَین انقلاب در مراسم بزرگداشت چهلم قائد شهید، بیعتی دوباره با رهبری معظم انقلاب اسلامی و تأکیدی مجدد بر ادامه راه آقای شهید ایران خواهد بود.
🇮🇷
دفتر رهبر انقلاب اسلامی
💻
Rahbar.ir
|
📲
@Rahbar_ir</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/681610" target="_blank">📅 10:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681606">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a82e403547.mp4?token=q86v07cfONIWkbHUB43PK4hXPsN6ly3upUHgNKYJjZuI5Kh34K2vG59skejMqWDDMFGRNKbzCT6PfrBS4BVro5l9fkZVUvDaMbb4ooxA9v4cA9E9XUKISyixzMxSqalY0oOg1QAAnD6cXc38oBzQwL08SGtg606gyr_u7bNT136pJdD_ktg6w1VsN-BbT756y3UqIUUpQjU2PYHb86OXh1191dWnfCGM1E2TfeWm4I6kSb4OjagaeAwTx40ChDuTmQFdk48jIcWgh1XGOgp3fJBno8MXb6zdg4VPotWJwuCmFfTNkwX-LbWk75As1AhVd8k88bwsfVdwmrkvI5M-cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a82e403547.mp4?token=q86v07cfONIWkbHUB43PK4hXPsN6ly3upUHgNKYJjZuI5Kh34K2vG59skejMqWDDMFGRNKbzCT6PfrBS4BVro5l9fkZVUvDaMbb4ooxA9v4cA9E9XUKISyixzMxSqalY0oOg1QAAnD6cXc38oBzQwL08SGtg606gyr_u7bNT136pJdD_ktg6w1VsN-BbT756y3UqIUUpQjU2PYHb86OXh1191dWnfCGM1E2TfeWm4I6kSb4OjagaeAwTx40ChDuTmQFdk48jIcWgh1XGOgp3fJBno8MXb6zdg4VPotWJwuCmFfTNkwX-LbWk75As1AhVd8k88bwsfVdwmrkvI5M-cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راننده خودروی مرگ چهارراه گلزار کرج اعدام شد
🔹
«شهرام صادقی» که در جریان کودتای آمریکایی-صهیونی دی‌ماه پارسال با خودروی پراید ۷ مأمور فراجا را زیر گرفته بود، پس از شناسایی، دستگیری و محاکمه، سحرگاه امروز اعدام شد.  #اخبار_البرز در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/681606" target="_blank">📅 09:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681604">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b569333b1b.mp4?token=JZyg-u5B2IF3FgLwm1SMY2Tsd-56uZl3MPH_o7IbNPwkRkz4vt86KrZwYDhUsl5w_t-7X4XAL2y2e0_FTAKzdp3V-kCb7PaDYwQ4m2F657qDxss6Ctp8W4wC5eIhpwxn322rj0pJ_5Di4HTFx4EQfhDR5Wu3niFMotwMYHitxqoOeHYfwtk3LaOQDiEvmIspIruP6bsiLV_LOHVstcL1DHyj0rpg5rniwgveOtZ2ULSssOjLvIYz-f6tt6W4dedEn2KL49EuX-PLn8H7Y4XdXl2TE6djI-s9580SO5YydUZ_yBvwMENgUHhnBMZ-ZduFEbYEdlAKme2U446iBgVBrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b569333b1b.mp4?token=JZyg-u5B2IF3FgLwm1SMY2Tsd-56uZl3MPH_o7IbNPwkRkz4vt86KrZwYDhUsl5w_t-7X4XAL2y2e0_FTAKzdp3V-kCb7PaDYwQ4m2F657qDxss6Ctp8W4wC5eIhpwxn322rj0pJ_5Di4HTFx4EQfhDR5Wu3niFMotwMYHitxqoOeHYfwtk3LaOQDiEvmIspIruP6bsiLV_LOHVstcL1DHyj0rpg5rniwgveOtZ2ULSssOjLvIYz-f6tt6W4dedEn2KL49EuX-PLn8H7Y4XdXl2TE6djI-s9580SO5YydUZ_yBvwMENgUHhnBMZ-ZduFEbYEdlAKme2U446iBgVBrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ثبت تصویر گربه پالاس؛ یکی از کمیاب‌ترین گربه‌سانان ایران
🔹
تصویر گربه پالاس، یکی از کمیاب‌ترین و ناشناخته‌ترین گربه‌سانان ایران ثبت شد؛ گونه‌ای که هنوز اطلاعات دقیقی از پراکنش و وضعیت جمعیت آن در کشور وجود ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/681604" target="_blank">📅 09:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681602">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
امتحانات دروس تابستانی دانشگاه‌ها حضوری شد
وزارت علوم:
🔹
امتحانات دروس ارائه‌شده در تابستان ۱۴۰۵ دانشگاه‌ها و مراکز آموزش عالی باید به صورت حضوری برگزار شود و برگزاری این امتحانات به شکل مجازی ممنوع است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/681602" target="_blank">📅 09:31 · 25 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
