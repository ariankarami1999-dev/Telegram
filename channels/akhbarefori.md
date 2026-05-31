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
<img src="https://cdn4.telesco.pe/file/ODSb7qYGPBSP8CPij_bTJauttfoMmkYDajAkfCyexnIg6cXBE-3-SKgtMVwmtq6QYOj8DuOGWRyPrHREQQwXk5d8zT0StXV2y2NLf6nXKmHVZ8JIq7_KIS2U5AalaerSoht-r9jL8SuhGdP6Kp_FMDZKzpebEHWE3bs5TWLd-WY_pH4suARqj3cfLuWjzTTcc0HV3OR_TkqZ_KnC88byIsmhxUUKqYtoZYLj7rYlaCE_AFqPqmclqj0_srzQCK0lg8_jkLgq_eWl_e3waIbz_4kW9wg4oMz0lWSnbZb-e7KblN82BmO5oOVF0YlIbI2dormFLM52d3U70TsjZfq5Lw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.08M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 10:21:56</div>
<hr>

<div class="tg-post" id="msg-654953">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTvFYkaDFwi680dyGbtKC6Ye6D__n3kzglDRQ2hPS8RgYwJXeLr_f0QUjnaKq4xNtblw9S3mMmK2iMYaV-gPsimGO4QyKF4n1g89De0V4RaMEKtfy_2dtYysln5F2ZOvP94aSUswmnquk4WUmkHYAsJ1jt4umiP8cMke7MziFIipcN2EI1fMrDrYm1_ir6X7obt6VW9EZvaRYyi1JqPTaHCCUaSGQiM-kIow_vGt5KaiXrZ_ekmTIwl5fskgkzAgFrB-Rn1BrSWHY5K7EGxESw6bqF-LQXjqz5Tq0cPmotZQKvsyltgifO2M9s_t58CnAlqb2cNHJm1WUsBPnc-z8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نماد بازی‌های جام جهانی از ۱۹۶۶ تاکنون
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/akhbarefori/654953" target="_blank">📅 10:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654952">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSz-wrQsIkmSKuVryDpv2kxplyCa-VLPs1bp2MEdDPRQkBsokI636I07FwBvOTJvT9KK4AYAGaeazCvcMjXo3cPARApvJyOrwkSi_CJodOFXw69ohabfP1OCtAhrfjFKTudOXjNjmaKzOR2u43HLwn4bL04vrkek-DaGxg4HJW1d1FQOFy5hGT1aTONd4GzXZuNme8tghx7dnpVATmSDU0sVtJwpaLmgFnmqyNrqRuzZmVJ2a179JJoRaTokK058vn7wlu2a7LB1pjIy6XT6nHNVAS5lch3cVt6CGq4YXylYQjt-At3jqJ8LM_WPPKZgLbMq7BzA6fKydYMbLcPhXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هزینه ۶۰ میلیارد دلاری جنگ برای مصرف کنندگان آمریکایی
نشریه میدل ایست:
🔹
جنگ آمریکا و اسرائیل علیه ایران تاکنون ۶۰ میلیارد دلار هزینه مستقیم برای مصرف‌کنندگان آمریکایی داشته است. از ۹ اسفند تا کنون، هر خانوار آمریکایی به‌طور متوسط ۴۴۷ دلار اضافی فقط برای سوخت پرداخت کرده.
🔹
مودیز هشدار داده در صورت تداوم قیمت‌های فعلی انرژی، این رقم تا اولین سالگرد جنگ به نزدیک ۲۰۰۰ دلار برای هر خانوار می‌رسد. اقتصاددانان آمریکایی تأکید دارند ادامه درگیری‌ها هزینه‌های بیشتری به زنجیره تأمین و سفره مردم تحمیل خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/akhbarefori/654952" target="_blank">📅 10:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654942">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/loL-rsGD-A_N4UJYH5JqRD1gEnOD4H-msW4H1G7VnxEicXMLpfNUo4wwOfTqWulq0wqAlGz1spz2zWX-5wfevjjZunyXdQFuFQvcQLVTuS313w9oVIHozhedQ-sbe4MNCJyTv6xkg3HhlOuLcHh7e8M-Lr4lcgs-a0qPpBthdbisXHnN7YSRAP7geD787kvlSlTDIJYf4FGgePwYLebi0XGAb3U2M8qcclVg4fpJtJe_xwwbd5BZW-wwWUKqxPV34ubaDZd3p8F0Ul4r3z74-sd7zCMuJJJx3UvrJHIttSyy3jSDOoVY5JRpPNRbkc_mMYa5TRdXVwSYTncfFiw8EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/e9igSd6b_ls4OPBftRrIBsZW8BkLRT62RtZTSS3xTNaPVjl2hV_fTh3dx4Hv12Ao_HOUgkVibHH20gUGbTI95-kKL_c4Zx6aqiXs72ElsQ8m4nhLI-QS4ltvYtnZP-PxgtAFXzMQbULZL_3EvEGAzuHRms31aflPTbux1hVhfC3ScW8NenOB5IZaJiRfV4nObmkL1B3sDRH7Td2QYIv4WuPcYLqqmz6L-sHVK_9K7nWQS3NDEGwm87C8xEnVLcC2GLeyjdSOQ-kkXWPMR50jjuFf9sJTAi9tU0G1MFhdzEzsKDPwiUWe2VCmonxDMFD1lZ1rEioIfsu1VHSTv2eiVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jlTAGcQ2ijIH-PWVpHLiKur0ikgwrpAJR23dZvLQ_XSlVKfwynWSfK6opPcPafm8Cjd92nxDQbaZdKWn0SWOj61hCH_Mg1SlkQgSnjt_I5vPJiO73kz1WNVE-NWnAT_aJHp9Fc_yIDP9BwvgERmjm87-m6uJ22SYJ2x-r180CQRLqracgBB8xHQKIQmx3n1DAzyYBNRpk8xOEQA2bmbIN9XnmTBsrWS7bmI0aIaUT8CAX6j_M-y3m_yIRq6GxBioeLZ6v7RudC1Fb9wmQirhu-1zd0Eq6anyaoVz9Aw9DtsxYtYCFnlq65Dwfs4A3NHNA2FKn2qkYv4eSmXkaRUBcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Sfdc866yFuOHopORtvyIOKANw6V4oR3KtuuexByRY1A6xEGhcHBTczgbKKnczbPpOvcn0ijPkMdbc5iHnz5ppqxTMOFQptdqzjWbvfu9n0TbY2JLR1i2h8SkkExM-U-MlXQ2lfdixGT9TQvLadCYYyuPLdTsQPZYHu098oHWeNbqnHdLrgVzfBrkgrSoAebx55KsNZ2ib4jjtHDJiz5Yic_jdHp0jG2DwACom7bt8rsrMsJWQZYm-Tp2LJw6rXqrcjU14s7jEFRjqjZsHiMdpRH2OlCRU_jEbFu4cxi-V41QyfEmWxmWX5eTXLuHEf9sg1wAR4aX9dg5lXYAsn5KFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B9J_C-CdVK6dRC2NpFr2zMpbNa0kMjjHVJGlnwP5g1AfSr_DMG-F6nbOhQxOytyiGrIajVZgTLtd3yajyJvFPTJH2O9sZNT55dvaOQ3JagiZm7Rv0rBs8_NZJksymD3R4yOu9Udd2hcngBqqHWWjt65BRyPrpOlzCVOC4TF3tOcWdCJNhkJgrTDbJadMG48wbQ66tHzGv-v5xbdS3NkXmMr_EgZxVPMIi6QaVgsIeyF030QpwRLmDZHF2VQp-LzTwFXmv76CZRaRr0fsmIb7fLyvk7mlSL-YN7ee7wqdiz0IucisgKDlhp4sjH0Z2i99DjYJ7hFb-UUhoJxicexKSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hIf7yOGzywnrE29o66j-PbEJbcLRIBqlj1E_IuDhDSdrxz_BFE_g6RjWvS20CsX1b7PG9vuoEBiqaIMcQfFg5DsYpgm4QXAQe0A6O6kkqzzoqn191GhXR-9_d5qBwep0gFR2UxTsMSBY56C1hokEZkPP-j1hVl7Y4nbahaepmYS7_KxsqvaOzB9Pqd5kniouE0tP2f-kYzozgG2Y7paQJ-QkcuuvFgE1-ksMdQk2rhHe4B9FBkD9XJlZVIA3nPxsGu88GMuptUeXyU7kDZ9G0DOTWV40El-CK9bNEChXxRpRSDymc7W74ANlGeFypA_CoSnwA_3htJFjbf5e0mEZ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tIzXfkCkH1T_azG-cx0OUSkb5Bs-VO-PwnFDR3tXxGEGoPazkPVXy1Usdu1hiKG8fd4G37W9pIv9zZK53Q1tTqyeIdPGhJqGqCfMVsTqQ_WAvn3POSs96rBSB0xhyuCU1-mOsyTHKqtUZZvPV3nNEjBdyRnznQpLRXgPZ_cvyKAIRvx9466Zq62g_4KfbgsadJ3UepUZYk9yyYCSKmQK-o43CQ7M9opqjbQFRfQ-Ebwrm1oEujOSATCEQisbR5mr-KI3AiPoXEV0nkD75NB34qEpzGhrP3LQxb6G_37tj8-uUUxFUUkZCopyJB5_LeVt198eKdPJY2E-dvET-LIU7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mRDhn5FuBMYyOcSJtw1ZiroVpQN1JQFKbXC-64mqF4tCItLWlUKWd2SDTEoAAsq0DOSIUbUfkg0tV7nXry9AdsCQvDWUPOLUcrw--BkiKZSeCM8keqAc6LiR55dUN9P_bLDo9IYu0rq0pavIg7iXyva4cRcSiDPhrQoLy8SDHfa1l69xRNC5JGUuhLjFwH1x9WiPlJjMR8neiY_L8-zdK5wxmU10adhbefFqWG3wPbKHGELoNdUUqyNpA0TL9lc46v2yBQ054G1Hahg3o5iEV0IQhe4q8tN6pqPkkPfUmY5c7Rn5VU_Fp4l9ola-KPddr0lLHSR6CKi1QTkJ2viSzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gkap1jbcCfhxGDbd6ldJLIKxyGK8wrkuO5czU_pyM12jx7n2LG-cr4Kej0lKfxo9yJVpdc1cgdfD3cWBHqv_1WpgruBgIBoubp3LV9_PJ7JXK1EStRQpmwzqE3ESWac1VoJy8tvJwyyoAYhZo9HEqv_iWm-WN9lOH2gZxCUBbbOoq1-zVNC2wvhXp27tRCeaoyhBfVv4CdUgD3IxB8KAkaQRudo9E757o7ocQ9zR4qtubz4wfRj1ykOCtHuETEhmFuEFjyYICJFnjEIzmqUZK5cDxdov_q71-j0I5mt8a0yQOG3-0rlgeyHPMWqgF3PnwCckPougxPvquev_NbysJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/grBu0J643A8kIP5TlqBeHiQWeTZnbNEc4f75NmCm-LrFodU9FMDSDDDj8SC7UFbopCnfl6-Zjqv1MIV0FKI64aCgk_iCoVEXz13dVUXNqafHgcSV-vHQ7zD2xrbLY2211EfHPAIOdM_BUYo5W0appktVpp62r3mQKsHXDECY0zWagiO588MH2kbj4MfvQLWL-jXa2zsR0GtxEDCNM1eY2LY6cfmQmpT0yjLjntTp25KPgj_DGcwJvurHIHm4x2S6_fMXRWJE-c20ucbx7aKhFN8uVUDIez1pgj5zqcvwvQ_jzzlE07ee2gFv6GBjxJK3hsEc_Bydsn3acD4fkwEPvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نفوذ حنظله به مرکز پشتیبانی از قربانیان هولوکاست و انتشار ۲ میلیون سند محرمانه
🔹
در یک عملیات سایبری بی‌سابقه و چندلایه، به‌اصطلاح «مرکز ملی حمایت از قربانیان هولوکاست» (
k-shoa.org
)، که مدت‌ها نماد قربانی‌نمایی صهیونیستی، جعل و تحریف تاریخ بوده است، به‌طور کامل توسط تیم هکری حنظله مورد نفوذ قرار گرفت.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/akhbarefori/654942" target="_blank">📅 09:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654940">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQCyv1q6XO6VVJYQUFmjMk83eqEpG5LRtLz5Q8CE7kLwqTVClZ7vwoKE_bVa4mh8C9mzLStYZ40YgnLucxq0hPsUieVB1Bbaok2j9E_rj4iScHdJygywCf3JSfGMBoBrhFbwRZ4eXCBPDu7iDqymOur7rCHGxroXC6h9npRgKZYeLVkjNYpDx3aSiGSztDqM2nIUMWev9TQlgzHsql6XmVYYMfxOuOF34ugNfhVR2Bctkw2NuCcgsyeFJc7Cm80l0gWUZqIIAZEHHgQ1H5uai-fG0_fHe0BokYH9K_e0ksJPFgr7_QnE2Q41JILtj0pi9QkioJvFennkB6LKgt2Pig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت سرکنسولگری جمهوری اسلامی ایران در استانبول: “پیت هگست: آمریکا توانایی از سرگیری جنگ با ایران را دارد.”
🔹
اگر شما توانایی جنگ داشتید، برای آتش بس التماس نمی کردید.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/akhbarefori/654940" target="_blank">📅 09:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654939">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89138cf928.mp4?token=jw4vhQLp9stp2ERESpfVmLgdeAwx_AxUtHQZeD9FvYJFyhxFukjRqXSU2LMlNrSwfArT3gMEG_29eiLE69OogDQANT7Z7-IUI1fGWVtxr_ni4UDtSkRyr8gK_252DeTJQ6_lPThWX1APXzt7u1_nY35077Rb4MwBV1gLPUF4OXqmUNOgU49g9tYHQ8gL_XvgaMN8AzeWSmzFDKp3GkyLa7CxovJD3dLitYGw-MRq0I6-yujUAyrL4tWH6VNfOfHrKV4vHOH762wrYHnq6bgXb-970Cc4tZd_Y41i5a4Qcp28fOvJRkE3vAwYoVfysjkfYEBGlyVJ7oHuwmGM-n0geQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89138cf928.mp4?token=jw4vhQLp9stp2ERESpfVmLgdeAwx_AxUtHQZeD9FvYJFyhxFukjRqXSU2LMlNrSwfArT3gMEG_29eiLE69OogDQANT7Z7-IUI1fGWVtxr_ni4UDtSkRyr8gK_252DeTJQ6_lPThWX1APXzt7u1_nY35077Rb4MwBV1gLPUF4OXqmUNOgU49g9tYHQ8gL_XvgaMN8AzeWSmzFDKp3GkyLa7CxovJD3dLitYGw-MRq0I6-yujUAyrL4tWH6VNfOfHrKV4vHOH762wrYHnq6bgXb-970Cc4tZd_Y41i5a4Qcp28fOvJRkE3vAwYoVfysjkfYEBGlyVJ7oHuwmGM-n0geQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحنه ای زیبا از مراسم حج امسال
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/akhbarefori/654939" target="_blank">📅 09:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654938">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
العربی الجدید: همکاری نظامی بین مسکو و کابل؛ روسیه از طالبان در زمینه سیستم‌های دفاع هوایی و سلاح‌ها پشتیبانی می‌کند
‌
🔹
پاکستان انتظار نداشت مسکو اقدامی انجام دهد که مغایر با منافع اسلام‌آباد تلقی شود، اما این اتفاق افتاد.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/akhbarefori/654938" target="_blank">📅 09:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654937">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e4d7ccf7f.mp4?token=SgmD-VzvKBvqpArb0MNdZMtlVAA8gAcZ-EG53hp1oKe3gW2vE43F92agzoefqi3HLTtpNqoadNez9U9hKVa13NQnFEa9JH6fHyg4rXQdsMvN6KgviMyisw0-Mq06sar07ZMln0bQsxUTkZHJ4cP9x-RmgG-mlY2ZRESnwSSrSEhEAUho2ySeRhXGB2u_Z2pEB2BOFqhuLP8zcBxRV0fvUgviZYPJ41YYBaLzImmfuyW_-pfZAVB9G6aTmXI9UBvnHS7Cg32vhgvn_GcxRGIsxoTSkR72HXUu_88kOn_WN73Fjhxj2JeMOIrFOucE1U6zs0mN0nzTUvChQXgcOTVobIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e4d7ccf7f.mp4?token=SgmD-VzvKBvqpArb0MNdZMtlVAA8gAcZ-EG53hp1oKe3gW2vE43F92agzoefqi3HLTtpNqoadNez9U9hKVa13NQnFEa9JH6fHyg4rXQdsMvN6KgviMyisw0-Mq06sar07ZMln0bQsxUTkZHJ4cP9x-RmgG-mlY2ZRESnwSSrSEhEAUho2ySeRhXGB2u_Z2pEB2BOFqhuLP8zcBxRV0fvUgviZYPJ41YYBaLzImmfuyW_-pfZAVB9G6aTmXI9UBvnHS7Cg32vhgvn_GcxRGIsxoTSkR72HXUu_88kOn_WN73Fjhxj2JeMOIrFOucE1U6zs0mN0nzTUvChQXgcOTVobIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسرائیل‌اینترنشنال و تناقض و رسوایی و وقاحت
🔹
دیروز: تکذیب و انکار حضور موساد در ایران
🔹
امروز: تحلیل عملیات موساد!
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/akhbarefori/654937" target="_blank">📅 09:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654936">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbueMNkypG1NjNe-pa4w9PEh6eBoY9O4ThqIWHF3lY1oSdJot3MaNQQV-P41oTVHkeNSVlBE--WcL1sZP6XR8OYB1R_0jGyBa8LcbQ_JJB0oQiAdRbTGmztWuJOnFC78FfS_R43TSvvyyW1o_9MzUIVBCZmDjfWlzr5X_zqxMKTQ6P1Ad9xX0QWkis-_q_2zWO0qKP0klT0yjBOGrvAaE2z5sk2TORNN3S2j6ekJop0aiFMXQvx3GP8t9HmmdaQDNVatDUgB03jcUjgwMpt-5tncV3NxTTYIh-KpPs5cbvcFZWzyiTi0gjzsHI2k_HHJVO8ZuEYy41U9u0tHO7lXfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدارهای حملهٔ پهپادی در نزدیکی نهاریا در شمال فلسطین اشغالی فعال شد
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/654936" target="_blank">📅 09:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654935">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/333fb34799.mp4?token=sI3BfbOjKfW0v78vZa62mufOO9B3LOrTZKQQWpao3rc4qB6GdxHj26oE_gZIVpHeMXNiK_Ds_GfFlkT2eytbrAUu0YdWYhZK-B5EiQBFbhXYQ7yIUwhlUXuqEFqH4kicpW_-LB8B6B49IXoAEFeyn_y7wB7fwrqpqu5qRNHaOaZTl8iqxHlEydBlJpgQmumKwIZf3iiVuesdW6gooZc8ts1hYBUNunfit-5zqVCNrcu75Xxp8N-tmtz_KOXLMOV4_UTESbgveMRXsPhuCJtpcC2MCaii6WNKcSNV3gUjdlCXSdcpGDsHrUtM1a_aFtG8qN6FP_catngC6JwrO9sTpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/333fb34799.mp4?token=sI3BfbOjKfW0v78vZa62mufOO9B3LOrTZKQQWpao3rc4qB6GdxHj26oE_gZIVpHeMXNiK_Ds_GfFlkT2eytbrAUu0YdWYhZK-B5EiQBFbhXYQ7yIUwhlUXuqEFqH4kicpW_-LB8B6B49IXoAEFeyn_y7wB7fwrqpqu5qRNHaOaZTl8iqxHlEydBlJpgQmumKwIZf3iiVuesdW6gooZc8ts1hYBUNunfit-5zqVCNrcu75Xxp8N-tmtz_KOXLMOV4_UTESbgveMRXsPhuCJtpcC2MCaii6WNKcSNV3gUjdlCXSdcpGDsHrUtM1a_aFtG8qN6FP_catngC6JwrO9sTpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتقاد معاون وزیر بهداشت به نمایش بی حد و مرز سیگار و سیگار کشیدن در سینمای خانگی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/654935" target="_blank">📅 09:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654934">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQj_Yt2a-BXN2fifXHzQ1fdOEg0rl7Ppz-YNN4Y4JjBa6LlBl4ofKinRljdVoKwvewkV3fQEk7mT9L7AxkI7nb94loSNHbwGrR3ctVoYeJp8lokqEGjGvx7cvenKW4R0z9n8b6b2ArvipxQJKjzsNgFFCGF_jh8lDpPArjOygnsHKBTA9QE0driIjezvOF7QFusIJEYZSb7MBmm4UyA590XcYLibs5tlnZ-gxjz-ol-l0vCnTgczdVZCI8ZAVyO1yBNd8T3kGJfa5wxD9MzaI2n6s9Ikz0n57lwRJB-St2Xo1k6QA8HoLuTX4-8Ty8XocIxpanyCEElB_Q8CgoY4Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک تایمز:  تمام شد و جمع شد؟ روایت ترامپ از جنگ ایران با واقعیت همخوانی ندارد
🔹
دونالد ترامپ تلاش می‌کند جنگ ایران را تقریباً پایان‌یافته و یک موفقیت کامل جلوه دهد. اما پس از سال‌ها تلاش برای تحمیل روایت خود بر واقعیت، اکنون با بحرانی روبه‌رو شده که با داستان او همخوانی ندارد.
🔹
در خوش‌بینانه‌ترین حالت می‌توان گفت که یک تغییر در رهبری رخ داده است؛ اما اینکه حامیان جنگ آن را به عنوان تغییری مثبت معرفی کنند، نادرست است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/654934" target="_blank">📅 09:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654933">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uC837SbCzyq4RzUBr9ep3sdQmb48GiEdroj8moagey66j6OHdce1opZGtUf0zbrRpaNqQXgjF0L66UXR7BAx6h63W93Y7vRgTP-pMniGYQUKcwahhGKIyis0yES7_d7C488EvgkqVMBN_AqJBbNgdVS8eDgbR2Qqz-i5WSLwpAlDHru8lcQdPlHOC2rL0vArhxoYSVVnOKmJsqh6sFRvb-iciMXoWvRsPMR6XmAMhfOT_7i67dhsEuRWH8m-N1V9YV9aXe2CwU76tP6nOKgqyJchcakQY1bm-yHzIwZrB6n8yVsejVHbajmNit3X2f0U5zkB27fCPjrXIMURp12yZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخص کل بورس تهران در دومین روز هفته فعالیت خود را با رشد ۸۱ هزار واحدی آغاز کرد و به تراز ۴ میلیون و ۲۳۴ هزار واحد رسید
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/654933" target="_blank">📅 09:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654932">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14cc54b6c5.mp4?token=VvdptB5-JcEuFrkGVPHD5kF0lX9tGPjUaK7ClhJxO8eo7dlSjthZCHFPeDkzqcrzmUdb_Ps3YEyQ05ZdiJ0FYCUuSPdaqaBeSOV_g3ahWoOdRGgrlNnvz4_hhB4C3ytYv0QmW2Xo11dbqfQNL7LIPGfRPQq4GRpr6uV7VhgGUmnnBL1fhCpPFniwlJZVfdqh_vIA9mkyU5VqZn_tNr7Tf7UNUbZAbZi_PMAexGo1TJpfhU1cAJLAjVmUCWZNGAoF02jwBgZ6eBmrRy5SeFJU--6Aw1beNvnMGqUdIuKuaRG4sxVH3FBfSh4_-D6ZL-pNrAGkOVuhTlKS7bM5-ebLRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14cc54b6c5.mp4?token=VvdptB5-JcEuFrkGVPHD5kF0lX9tGPjUaK7ClhJxO8eo7dlSjthZCHFPeDkzqcrzmUdb_Ps3YEyQ05ZdiJ0FYCUuSPdaqaBeSOV_g3ahWoOdRGgrlNnvz4_hhB4C3ytYv0QmW2Xo11dbqfQNL7LIPGfRPQq4GRpr6uV7VhgGUmnnBL1fhCpPFniwlJZVfdqh_vIA9mkyU5VqZn_tNr7Tf7UNUbZAbZi_PMAexGo1TJpfhU1cAJLAjVmUCWZNGAoF02jwBgZ6eBmrRy5SeFJU--6Aw1beNvnMGqUdIuKuaRG4sxVH3FBfSh4_-D6ZL-pNrAGkOVuhTlKS7bM5-ebLRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط پرچم اسپانیا جلوی چشمان پادشاه؛ واکنش سرد و سلطنتی فلیپه ششم سوژه شد
🔹
در جریان مراسم روز نیروهای مسلح اسپانیا، یک اتفاق غیرمنتظره توجه‌ها را به خود جلب کرد؛ پرچم اسپانیا در حین اجرای مراسم دچار اختلال شد و به‌طور ناگهانی سقوط کرد
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/654932" target="_blank">📅 09:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654931">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
دختران میناب زنده بودند اگر بوش مجازات می‌شد
‌
نشریه آمریکایی Current Affairs:
🔹
مصونیت رؤسای‌جمهور آمریکا از پیگرد بابت جنایات جنگی، باعث تکرار این جنایت‌ها شده است.
🔹
اگر «حقوق بین‌الملل» قرار است معنای واقعی داشته باشد، باید دونالد ترامپ و برخی مقام‌های دولت او به اتهام جنایات جنگی تحت پیگرد قرار گیرند که اثبات این اتهام‌ها نیز دشوار نیست./ ایرنا
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/akhbarefori/654931" target="_blank">📅 09:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654930">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HitltUUp145hidHGCy_BlmDpaRx_GVQpe7iW7JJ1tm3uf0dxZoW1Tsw4XMEeC_iyPhNSplBwjTMEHjimkk7-BSBT5o6gZ3RZRxksQ1HliEG8K2OI3MamTP98GimZNBxu3qFdFYzejA7y0zi8e79inCX1o493IBk7tcbRKkShYcw9QnAeTCgzK1wGku63TBeLI5CfKOSJukquLA86FRqW5c5-CxIusw_aosrH0FbfyIuHdffsB_WqLnxXoBjzqsNTOHirkEvpX6AkEYf1SImXyX15OpkJgC1x-2YkbHcCAanR0dyXWJ3ipR6uxiahlD5K9sANnlV6v1ZzgbHY4tNTBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گوشی را از دست ترامپ بگیرید!  آرون روپار، خبرنگار مطرح آمریکایی:
🔹
پست‌های دونالد ترامپ در شبکه تروث سوشال طی حدود یک ساعت گذشته کاملاً دیوانه‌وار بوده است؛ این حجم از چرندیات و رفتارهای عجیبِ پشت‌سرهم را ببینید.
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/654930" target="_blank">📅 08:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654929">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEAvuI4vlCTyW7istB-J6A31I8HLRy0JsQCv1jp2WH4yfUn5L839aHOC_w_vnguht-pZR7hrwVQTJ-XRQ9N7hRK29TwZSb2fM052jwvhJD3snyuI03fVhvbGxlY9Yr4G47vq0LuK3H9k-F1RzaSyZ-sqFpklVjs5Cj_zUVPkDZrklNYkrD2AUFNaGnjjaKygtVwYsMbU-eVGf-5Waq28FAL3foxNbW8baDe5h0kon8MxJgJ9BXPSf-Kf5EX9icQ67tVDQC4paMSmCDnoBh72cFZEpYOe0t_ScpHuJNvz59F2ynx0t6LumvP0JQnKCOVJ67qYrxi5RjFr65IsT-oXHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حذف صبحانه با افسردگی در ارتباط است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/654929" target="_blank">📅 08:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654928">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7c74b0d35.mp4?token=rIAlA_q3Eo5v46FvT8uAd0VEnU49u27zYU4P8q3RDiaVvHHGCSKJmU_G2rtVn-IZEBE-0iT9ImuUfqhfT8E364Cng5aSTWfzDLMX0A4MCZ_PO47nGMJlTgiCvOJmKjrAoFvu3FaGX9nLBDR2e2OOsxr6zvpKPaHG6_TCe_x7lX97kscUGAbk2TVS_u8OVhzEZBu1GersnUkZD82LMUJfkSDYvhoaX2sIIXic1kC-aOTa9z5eGY1Da60kIgXPFtbQGESDU90qG3Ec-H_NYUaFapv-ZI0JFZmfOUlyqR4sjjs435dZu-x346Uw6n_LfTJZYyx__iCKe1CAmxEl7XbX9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7c74b0d35.mp4?token=rIAlA_q3Eo5v46FvT8uAd0VEnU49u27zYU4P8q3RDiaVvHHGCSKJmU_G2rtVn-IZEBE-0iT9ImuUfqhfT8E364Cng5aSTWfzDLMX0A4MCZ_PO47nGMJlTgiCvOJmKjrAoFvu3FaGX9nLBDR2e2OOsxr6zvpKPaHG6_TCe_x7lX97kscUGAbk2TVS_u8OVhzEZBu1GersnUkZD82LMUJfkSDYvhoaX2sIIXic1kC-aOTa9z5eGY1Da60kIgXPFtbQGESDU90qG3Ec-H_NYUaFapv-ZI0JFZmfOUlyqR4sjjs435dZu-x346Uw6n_LfTJZYyx__iCKe1CAmxEl7XbX9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تناقض‌گویی مضحک ترامپ
‌
دو جمله‌ رئیس‌جمهور آمریکا در مصاحبه با فاکس‌نیوز با فاصله چند دقیقه دربارهٔ ایران:
🔹
ترامپ: ما در واقع ارتش آنها را دست‌نخورده رها کردیم.
🔹
ترامپ لحظاتی بعد: ایران در موقعیت بسیار بدی قرار دارد آنها هیچ نیروی نظامی‌ ندارند!
#Devil
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/654928" target="_blank">📅 08:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654927">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
پلمب کافه مروج شیطان‌پرستی در خیابان ولیعصر تهران
🔹
این کافه با برنامه‌هایی با ظاهر موسیقی غربی، بستری برای حرکات نابهنجار و «تحرکات شیطانی» فراهم کرده بود.
🔹
مشتریان (دختران و پسران جوان) در وضعیت غیرطبیعی و با حرکاتی عجیب و «شیطانی» دیده شدند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/654927" target="_blank">📅 08:43 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654926">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
کاهش سن مصرف دخانیات در میان دختران نوجوان
دبیرکل جمعیت مبارزه با استعمال دخانیات:
🔹
حدود ۲۰ تا ۲۴ درصد جمعیت کشور مصرف‌کننده دخانیات هستند.
🔹
مصرف دخانیات در دختران ۱۳ تا ۱۵ ساله نسبت به ۱۳۹۵ حدود ۱۳۵ درصد افزایش یافته؛ صنعت دخانیات به دنبال جذب نسل جدید است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/654926" target="_blank">📅 08:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654925">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
آکسیوس به نقل از یک مقام آمریکایی: توافقی با ایران حاصل خواهد شد، اما زمان نهایی شدن آن هنوز مشخص نیست
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/654925" target="_blank">📅 08:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654924">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KS2BP-8C-Ma5YhPFDK5SwP3xMs0_ramrXvXprRrAWyuyVueK5AH2naHxIAoXPLQIuxiUo9X8Rk53aSwNpB0EsvAJxpBsW0o4CbUbwgHbzc2wxzWYgCEP3j69-TbamjcjGVG4E8cvseenrIzyC9px85a6zPcCNlVa9Sht6LDQgMKpdJJw4oJx5BvBUlS51XAd763wvrSZFqWvNqjB_yMTUykMOnOnxalMn0b6eG4wzxJXQ2uafhmmqfqzRtVBagTtoVus5vz5juurB2wrJxNkdC4ZSRw-bMCrgikafgR_KppNmdQQnU1n1HfefEYCDrkeo2oX5r6ifTM2of-IeftFQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فاجعه در دنیای علم؛ ۱۴۷ هزار ارجاع جعلی و تقلبی فقط در یک سال
🔹
دنیای علم در سکوت خبری، بدترین بحران اعتبار خود را تجربه می‌کند. بررسی ۲.۵ میلیون مقاله نشان می‌دهد فقط در سال ۲۰۲۵، نزدیک به ۱۴۷ هزار ارجاع به منابعی کاملاً خیالی و ساخته‌شده توسط هوش مصنوعی در مجلات معتبر منتشر شده است.
🔹
نکته هشدارآمیز این است که در حوزه پزشکی، این تقلب می‌تواند معنای ساده‌ای داشته باشد؛ مرگ بیماران!/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/654924" target="_blank">📅 08:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654923">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8db579356c.mp4?token=owC04zbJHTipoAVpf-KOXMQkF4hJ-UnBQPP5DGPEWES_AsfeWxcY6yxjdHrxJGoSWRp7P9OlmdQ2IwrIUQazM7MsTUjTrxZ8ygeUVqZ5VT880v3SDQHONvn66Bif8mdIeFA1Z_08i877FoUJG84yfr_3cnbGAg17JmmcdiSVMKhXMMffKPV0dvpBwHiLu8ofjK5QpxCj9QGUuAy8REtI-73FbI5wrRoTtIjyJjMk7TSbAnQ2KXE6HlWuQMrIoIU5MrKVgupGDfr-4Qbtk6cZf0CP02gIKkXI_bhuVQ8Ha-Y-mteOB-f1Lv5X068pbs3e9PTOAuoolcUkgN_UOwn-u7m8Lk8U2hOi-_LeJjeX0o9l0KBT6hL14yQE1MqgSgy3_J7FoGLFGId9jUNWCSnTXLLqEY8hDmMSkNpXXEQQcWE8s5mYNL2niXuFhD280jGxbLUDYcbRc5OpGEyRF6ZwWXu-tVmhPfdMWiABNp-C1Yzp1vCukjVvQKNASUmWDqiHMhf4rtnNP8SvEsy7zV_OcF3LH5QQS5T03EIpnF_t-r5qj6xHVVKyU0cuIgb_9A1A577ozFB2fZKxIDF7iakSrVA4avMfjnWiB9BncnpsJ2KR_DgjE93Q5d737mWA3Ml2q_g47DWQR5g2MWV0L3XiqweYFi0LpMIjK6AGiakeODk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8db579356c.mp4?token=owC04zbJHTipoAVpf-KOXMQkF4hJ-UnBQPP5DGPEWES_AsfeWxcY6yxjdHrxJGoSWRp7P9OlmdQ2IwrIUQazM7MsTUjTrxZ8ygeUVqZ5VT880v3SDQHONvn66Bif8mdIeFA1Z_08i877FoUJG84yfr_3cnbGAg17JmmcdiSVMKhXMMffKPV0dvpBwHiLu8ofjK5QpxCj9QGUuAy8REtI-73FbI5wrRoTtIjyJjMk7TSbAnQ2KXE6HlWuQMrIoIU5MrKVgupGDfr-4Qbtk6cZf0CP02gIKkXI_bhuVQ8Ha-Y-mteOB-f1Lv5X068pbs3e9PTOAuoolcUkgN_UOwn-u7m8Lk8U2hOi-_LeJjeX0o9l0KBT6hL14yQE1MqgSgy3_J7FoGLFGId9jUNWCSnTXLLqEY8hDmMSkNpXXEQQcWE8s5mYNL2niXuFhD280jGxbLUDYcbRc5OpGEyRF6ZwWXu-tVmhPfdMWiABNp-C1Yzp1vCukjVvQKNASUmWDqiHMhf4rtnNP8SvEsy7zV_OcF3LH5QQS5T03EIpnF_t-r5qj6xHVVKyU0cuIgb_9A1A577ozFB2fZKxIDF7iakSrVA4avMfjnWiB9BncnpsJ2KR_DgjE93Q5d737mWA3Ml2q_g47DWQR5g2MWV0L3XiqweYFi0LpMIjK6AGiakeODk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوشی را از دست ترامپ بگیرید!
آرون روپار، خبرنگار مطرح آمریکایی:
🔹
پست‌های دونالد ترامپ در شبکه تروث سوشال طی حدود یک ساعت گذشته کاملاً دیوانه‌وار بوده است؛ این حجم از چرندیات و رفتارهای عجیبِ پشت‌سرهم را ببینید.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/654923" target="_blank">📅 08:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654922">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4971def66.mp4?token=FlK2H7gQHFpWjyd_sWgKyuSTDkdYWG5-b9oCdqjMhMFZU7grbmHeaucpbMaVrrDrmEBf8O6MgdJSSsT9veaVZk7UPoJ2JF_JH2_XNj-izrf1HhJTRUoIIiXoKbCMTWLSCgUGJQMRxSy21z4_uaNiUsYuuRBmxmUUxkeYv-mGGGDp1HUZ5jtKVGd7Kpi9DqrpgCjkZo8mNeKsynJIv7v92IebZWLbDFxIKtdiaJGfm8p57UOCw-W8Zu9tLpgTH0RyikSgnZxqfxOJ01mMt4e51QZwKi5lnfs32BhorOCgqzIPwKqCp3WrVhlqZUN23whuV5StTSkmVIYAwZgAnuT9DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4971def66.mp4?token=FlK2H7gQHFpWjyd_sWgKyuSTDkdYWG5-b9oCdqjMhMFZU7grbmHeaucpbMaVrrDrmEBf8O6MgdJSSsT9veaVZk7UPoJ2JF_JH2_XNj-izrf1HhJTRUoIIiXoKbCMTWLSCgUGJQMRxSy21z4_uaNiUsYuuRBmxmUUxkeYv-mGGGDp1HUZ5jtKVGd7Kpi9DqrpgCjkZo8mNeKsynJIv7v92IebZWLbDFxIKtdiaJGfm8p57UOCw-W8Zu9tLpgTH0RyikSgnZxqfxOJ01mMt4e51QZwKi5lnfs32BhorOCgqzIPwKqCp3WrVhlqZUN23whuV5StTSkmVIYAwZgAnuT9DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نخست‌وزیر لبنان بالاخره از خواب بیدار شد؛ نواف سلام: اسرائیل دیگر فقط مواضع نظامی را هدف قرار نمی‌دهد / کوچ اجباری جمعی بخشی از راهبرد جدید اسرائیل است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/654922" target="_blank">📅 08:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654921">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUUdzXT_4przSkFbyZmH-ZG6K4BejmH64cFu0kn8gPrtEZLJi41wzP298_rT31_betr4zgvdLjCqgqAOuBjS5vU4V0kquySgmdfOAasN0NTZLBr87sNRKeMmuQlz5duscosWSsDXj62K-K-u-dGDGTJotk7rowZ5U3IzwUhSYdqr1rz19GSuX-hzC4et7naicQKYGLHsB9urJ3eDXsl-KVaAchTfvoCoDmLb67X-G17vFz6BO7pPAFks1dfT3ULaAneyzI-MwK5zBKvxEkHhzmIUtsXqR-B_kevp522v6Vceg7aODx_qcyIBzBJKTzioeTpo-pY6Oet29uC4z15Igg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخه جدید براندازی نظام ایران در موساد
اسرائیل هیوم:
🔹
موساد در سال ۲۰۲۱ شاخه‌ای مخفی با هدف تغییر نظام ایران تأسیس کرد که رویکرد ترور فیزیکی را به نفوذ روانی و سایبری تغییر داده است.
🔹
این شاخه با ماشین مسمومیت (هزاران حساب جعلی) بی‌اعتمادی مردم به حکومت را افزایش می‌دهد.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/654921" target="_blank">📅 08:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654920">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2ImM4T0DUOz1AakhaS11rXiFFa0VHOmkgDCAkH1Wibl7wpMeHeyeejYBt52PUvzVq9PBprSss4siwTquJDfNa4aPQFLpK2aIFNCZdefpiXgSwirW8NxAvZmcuN9waWobOZ4OhG_kwS8QetmUeTKeZUVgLIeyIMy68cfjl84xPFSr6BnVcdV0WW5-vga79y_XTmOEdt7zSY1kpnuV4RRf6KIadGGCthnWo8bGAhW50MVJaOON2jcGgkFWL2PJM6cuS32lkbt4DH0QjiboJeSxaFqJTPJzTM3-6RzpIfLiOvxQy0zlotc9lglrkU-uNi3THa8eJqCblFsaJq8-MWF3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حرکات اصلاحی برای افتادگی شانه #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/654920" target="_blank">📅 08:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654919">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
آکسیوس به نقل از یک مقام آمریکایی: توافقی با ایران حاصل خواهد شد، اما زمان نهایی شدن آن هنوز مشخص نیست
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/654919" target="_blank">📅 07:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654918">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30655bc731.mp4?token=cemvZKozWXK_6x4yfw5swf4gY_cbf-T8J0erJ_2TZu2jGhKP-pTWjNxhTHDLGxdp29Pzl2aJ88DrWd4P_sDSQbTDsCxsj9SJ8oP0Ml86TXRjp2mkV63w3tAzXhOTxslItYJxBHMC2UVQyeHekzauOSY7eOcmB_wxWguF7Cfd9ozy7SytJ65WLD9s6mU2B1k9XT9hZFtLyawPZhxj_kWJGxOYe5Qgo6AOeq7NkTR7yVIAVYgpLbcFr_HedufZ3S6SgQGU8lPnU-9fs5MFa93qD6SBn2OiMXL5hLU0_MAmfFHDRkH2sLITlOyVl8d-95mU67TS3hNdu1YqOVeK11fLPTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30655bc731.mp4?token=cemvZKozWXK_6x4yfw5swf4gY_cbf-T8J0erJ_2TZu2jGhKP-pTWjNxhTHDLGxdp29Pzl2aJ88DrWd4P_sDSQbTDsCxsj9SJ8oP0Ml86TXRjp2mkV63w3tAzXhOTxslItYJxBHMC2UVQyeHekzauOSY7eOcmB_wxWguF7Cfd9ozy7SytJ65WLD9s6mU2B1k9XT9hZFtLyawPZhxj_kWJGxOYe5Qgo6AOeq7NkTR7yVIAVYgpLbcFr_HedufZ3S6SgQGU8lPnU-9fs5MFa93qD6SBn2OiMXL5hLU0_MAmfFHDRkH2sLITlOyVl8d-95mU67TS3hNdu1YqOVeK11fLPTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف رسمی راب مالی «دیپلمات پیشین آمریکا» در گفتگو با بی‌بی‌سی؛ جنگ علیه ایران، غیرقانونی بود و موجب کشتار صدها ایرانی بی‌گناه
گردید!
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/654918" target="_blank">📅 07:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654917">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
رهگیری و انهدام یک فروند پهپاد دشمن در آب‌های سرزمینی ایران
سپاه پاسداران:
🔹
بامداد امروز یک فروند پهپاد MQ1 ارتش متجاوز آمریکا که با ورود به آب‌های سرزمینی ایران قصد انجام عملیات خصمانه داشت، بلافاصله در رصد و هدف موشک‌های پدافند سپاه قرار گرفت و سرنگون شد.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/654917" target="_blank">📅 07:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654916">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
اجازه آمریکا به کشتی‌های قطر برای ترک تنگه هرمز پس از پرداخت پول به ایران
اسرائیل هیوم:
🔹
ایالات متحده به نفتکش‌ها و کشتی‌های حمل گاز مایع قطر اجازه داده است پس از پرداخت پول به ایران، تنگه هرمز را ترک کنند
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/654916" target="_blank">📅 07:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654915">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bc563da99.mp4?token=ecjZIAYumnSiBs1Gz0GUUaEv42DRLevIAwSBXhKGl_Y7QOvNfNH6f68-eQxeW8SA-hfobDRQ_gYP2XCeCRykdFn17VwI1okWlsaz39z2pVoN5uEC6GDynXbeSfDnYhdhMY4EFkNNJzvuPCVI5wDqYXkVyqs9cLQmpNaUNcRIAmOUEyAT37iJq8dkyIObzQhRZIVtWZNfFbYkDFYiGzcNQfmOjY63_JhGeJ8gMPwMkPBWCcBpQXOHA-_mRlp-D4i4wjHYSzNgSA8tYG4ZF9otUxh-GNqpMKZ_Ma0DHLrMEGoOTBCM75h6A8gSQKn9oyxFxm2cCgicE7CgX-pDkojeJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bc563da99.mp4?token=ecjZIAYumnSiBs1Gz0GUUaEv42DRLevIAwSBXhKGl_Y7QOvNfNH6f68-eQxeW8SA-hfobDRQ_gYP2XCeCRykdFn17VwI1okWlsaz39z2pVoN5uEC6GDynXbeSfDnYhdhMY4EFkNNJzvuPCVI5wDqYXkVyqs9cLQmpNaUNcRIAmOUEyAT37iJq8dkyIObzQhRZIVtWZNfFbYkDFYiGzcNQfmOjY63_JhGeJ8gMPwMkPBWCcBpQXOHA-_mRlp-D4i4wjHYSzNgSA8tYG4ZF9otUxh-GNqpMKZ_Ma0DHLrMEGoOTBCM75h6A8gSQKn9oyxFxm2cCgicE7CgX-pDkojeJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه بالا بردن جام قهرمانی لیگ قهرمانان اروپا توسط مارکینیوش، کاپیتان پاری‌سن‌ژرمن
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/654915" target="_blank">📅 07:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654914">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
جزئیات ثبت‌نام دانش‌آموزان در مدارس سراسر کشور
🔹
پایۀ اول ابتدایی: اول خرداد تا ۱۰ تیر
🔹
پایۀ هفتم: اول تیر تا ۷ تیر
پیش‌ثبت‌نام مدارس شاهد:
🔹
پایۀ هفتم: اول تیر تا ۲۰ تیر
🔹
پایۀ دهم: ۲۵ تیر تا ۱۵ مرداد
🔹
ثبت‌نام پایۀ دهم (عادی): اولویت الف ۲۷ تیر تا ۱۰ مرداد، اولویت ب ۱۱ مرداد تا ۳۱ شهریور
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/654914" target="_blank">📅 07:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654913">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
ادعای تکراری ترامپ کودک‌کش: به توافق با ایران نزدیکیم؛ آن‌ها نباید سلاح هسته‌ای داشته باشند
ترامپ:
🔹
واشنگتن به «توافق بسیار خوب» با ایران نزدیک شده است.
🔹
«اگر منصفانه نباشد، آمریکا به وزارت جنگ متوسل می‌شود»
🔹
«طرف ایرانی با عدم توسعه یا خرید سلاح هسته‌ای موافقت کرده است»
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/654913" target="_blank">📅 07:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654912">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpfrfSYV5NHDhgMtRXGkeiSJNTh1QogHc23MIzbTAKrOu89Cej3f4qlj1Hu2BRl9Ko5EkbEEvXi9dGG8aPgruUz1-6Qswh-fa1iN5Xrs1yFw-laotrhU67RvqHm7JP7bdFNUNzEBZxf0z5SFALce-Pg58vSyCGnxyxQDrxRuKWK6wEpH9eOjIxccAfhFDTBoD8aKbAIAjzcwszxxtp5nHbhIJwZjx9eyFdTLMMWpjBAwFasCMBFlM9ThEhfurkt8KT66uymf2YxooOl2INpKIyOPeO7IwIgvX1HcjWK3gz5EP274Srt9nADRyP69F42eJAI5KYmcf8Xy5LP2K_Y9cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۱۰ خرداد ماه
۱۷ ذی‌الحجه ۱۴۴۷
۳۱ می ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/654912" target="_blank">📅 07:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654911">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0Eyw3H4W5qJ_d8GRWu84bK45ZvI4s5XHx5f8hO1Wn8FHqbkO4BbvK5g5ae4ky0OW-N9mItbWX0WPWeSt6NifQ8WDG7clM_JK1ckgWhpQ9O0qJIzKLcQV5pQ_Wk01G05gpCSxRwvF0ad53AzsDRce3LLAxU90jAuEd_09CjxPhHD7VGwpk5VBdN46cUr0deyD1zFl6WA41afiqML_NEImH9czQaTzlLY9b5Wq-OTPpSGvKEd0bwhIKDvUjuw5-AW-VvuNAO-Lqhq7MGdqArk2XSu2R-rzUHcDQNrYU-vvJlPxW6Wjt2d4_op4VgHTgokCwpgDpCdit3kofEAe49UnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/654911" target="_blank">📅 00:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654910">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9A755W2WF6NrkQZL_QsqK5RV_QSCGEZ7ZYNZPqruabpVYzE4BmvwRKwbpzWft8ktHK6hjoZI30tg4iEYV131wArsHojjMc0gRIAcxH7xJGTrFGYeKHdYGmFf9SctW7WKI2KkIG6QcgT_Z4tEEId_fTjf-ILqssLSxbLV9WSxUT-zCGfre5T4WjMYQYUe6qIzGnYVVhlxRG63GEqvqa6iwtohcMpSA2R68Jt49jubEBSpoALPnr_0zOwsZAuSOn_I0parGUrx66Xzv4GXXyn1ulZpl92bVm1U-VSfiEMl1Kd8l9iVuMMxuNUzGRAoGWwNDRR3HaEcHiEssWulAISUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اجاره کشی
🔹
شرایط کشور باعث نابسامان شدن بازار مسکن شد به طوری که بعضی صاحبخانه ها غیر منطقی نرخ اجاره خانه را افزایش دادند و از شرایط موجود سو استفاده کردند. در خصوص وضعیت به وجود آمده وزیر راه و شهرسازی: تعیین سقف افزایش اجاره بها به میزان ۲۵ درصد و تمدید خودکار قراردادهای اجاره به سران ۳ قوه پیشنهاد شده و پس از تصویب ابلاغ می شود. در حال حاضر بیش از هر زمان دیگری نیازمند همدلی مردم در تمام امور مخصوصاً در بازار مسکن هستیم
🔹
هفتصدوشصت‌ودومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/654910" target="_blank">📅 00:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654908">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfqtxKm7316yTeZOzwWxxgIDK0OcGhxzBDUPaTX4cklZ7lMEfoWBugM_B9I6ZlVNiinj7ZhWiEpsX0o8Bl2C39DbAkZIFsqLTYh-BLeKoODpyWEjKaSXlm_aMT4Ge59mRD4zb_aHWD64QcZGWrGDDeFdcEUOBbc-_I_AhZhXNC7aXk_VdnVno1pT935PUdkXc_SdBw52aIJp0dP43fJ05uRuyLovPCH9Thx68fDV34840g9DAo_N934YTbeJwgHJD70lrd0fXHiuPM3JPc2KaOKkH7ZToMmfqInInY_WAwS6iZqmJw_S_8CW85qg4WsIfaCLcUgTL-3CUQt9CxMiVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر دیده نشده از شهیدان: سپهبد محمد باقری، سید حسن نصرالله، سپهبد محمد پاکپور و سپهبد حسین سلامی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/654908" target="_blank">📅 23:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654907">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8n2TlvxH_vU78-wYzjMnAqCoZjdaDh6XyWKMUbm5qruMD1nbgETck8URoa7bb_6Olm77_EsJ6CiyUENk4BhUeAWrc8RhOlwMy1T5YFvNbTLn5B8hqZ4h9GyXjL4I-2VolwrnsgBgVF5uNjC0rnftfYdUYLmxEBrq2MAq2OHtNEQjlRY4J3RGrkP_poLF6JxzqpYM0E2p3FySnXYKdt6gBAJp6HSNE2VzWKX33zRbzyeRKyk4Yoj2-I1qhDIbTcoL72ZPotH_4fcH3pZOQYmoi1w7gYInnd6smA3IIB3oTqwsy8BtRNR5O9URlS93J43IQUctCQwwBVX35TgdFTj5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۷ چیزی که هیچ‌وقت نباید دور بیندازید
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/654907" target="_blank">📅 23:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654906">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac963e4575.mp4?token=XKp_bLQhQ_5yZ_iYpDLEYWKEBzLkAapBPKTjAwauI-zW4XvO_KHI5Byy44-SOdEP-hnfB9qcwvKbJ-RckjFHcojRq0LKhs9_-gwb0spIoy9i7kFkxMXJKW1V2XhihXZK8BLvpHJqnooEiATSXHowsJmGChmI76u-n496Qq_HdiNCcGJpDvmTQCcYRwMWaNhaaMgevJccFI2z_dQgZvcosRUiu9V4E6jAT4qVxs74lAskDqZ2XbI0GWFZRBgjzXCfdbffBqZxbIFyYHIlPzQrGaX-X4GTWDe5ILcqRtjfZvbJWhlRNOyT7_31OjZCK0PdtPwgZ67KSBfFEtq94DA0ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac963e4575.mp4?token=XKp_bLQhQ_5yZ_iYpDLEYWKEBzLkAapBPKTjAwauI-zW4XvO_KHI5Byy44-SOdEP-hnfB9qcwvKbJ-RckjFHcojRq0LKhs9_-gwb0spIoy9i7kFkxMXJKW1V2XhihXZK8BLvpHJqnooEiATSXHowsJmGChmI76u-n496Qq_HdiNCcGJpDvmTQCcYRwMWaNhaaMgevJccFI2z_dQgZvcosRUiu9V4E6jAT4qVxs74lAskDqZ2XbI0GWFZRBgjzXCfdbffBqZxbIFyYHIlPzQrGaX-X4GTWDe5ILcqRtjfZvbJWhlRNOyT7_31OjZCK0PdtPwgZ67KSBfFEtq94DA0ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار مستقر در بیروت: اسرائیل خیز بلندی برای اشغال شهر نبطیه برداشته است/ دشمن در ۵ محور در حال تلاش برای نفوذ به شهر نبطیه است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/654906" target="_blank">📅 23:54 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654905">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoSoTQ3or2SRD-IgFJMs8JK4N9DKIAWORiVuVVm2Finau2ska8DWTbKCZcWcvFeyc3cvS4O3qVdL-mAb-qFWJ8irCOYyxYwZtGXVBtsPT72_6JIAYcO5XK1F7a5VyHi1KDyJJ0ZuI-24wcys4d229vXu0lbCwD4G5M4g1JHYF8TuAKlW5q7MT1_mEz0KIfAEX91Jq2Lw55rYpPimayjdmgKBS5xpewvNdGGTJP7_eTSuFfsLfQiCEWCYBtI3FUhXFmi3gVn-dcVXojqX3X8K4uUMIOny5u7J2Da0SWe9rMXfgbQz1rO7SivwxzXg975cO4hR6U-bAjmBAguNTuYtag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران بعد از جنگ برای سلاح‌های خود مشتری پیدا کرد
ادعای دنفس اکسپرس:
🔹
ارمنستان برای اولین بار سامانه پدافند هوایی کوتاه‌برد مجید AD-08 ساخته ایران را در رژه نظامی ۲۹ مه ۲۰۲۶ به نمایش گذاشت. این اتفاق نشانه روشنی از فاصله‌ گرفتن ایروان از مسکو و روی آوردن به تهران است.
🔹
سامانه AD-08 این بار روی شاسی ایوکو دیده شد، نه روی شاسی معروف ARAS-2. موشک این سامانه با هدایت فروسرخ غیرفعال، از رادار یا سامانه الکترواپتیکی تغذیه می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/654905" target="_blank">📅 23:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654904">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار مستقر در بیروت: اسرائیل قصد دارد شهر نبطیه و صور را در لبنان اشغال کند تا دست آمریکا در مذاکرات با ایران پر شود
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/654904" target="_blank">📅 23:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654903">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‌
♦️
سخنگوی وزارت خارجه: قدرت و اقتدار نیروهای مسلح پشتوانه محکم وزارت خارجه در صیانت از منافع ملی ایران در عرصه دیپلماسی است
🔹
فداکاری‌ و رشادت نیروهای مسلح جمهوری اسلامی ایران در دفاع از کیان ایران مایه افتخار هر ایرانی است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/654903" target="_blank">📅 23:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654902">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔹
خبرهای داغ امروز و امشب را از دست ندهید
🔹
🔹
انتشار جزئیات غیررسمی از یادداشت تفاهم ایران و آمریکا
👇
khabarfoori.com/fa/tiny/news-3219059
🔹
تاریخ برگزاری کنکور سراسری و ارشد مشخص شد/ سهم سوابق تحصیلی و سهمیه جنگ زدگان
👇
khabarfoori.com/fa/tiny/news-3218868
🔹
ماجرای حضور رئیس‌جمهور با تی‌شرت آستین کوتاه در یک جلسه رسمی چیست؟
👇
khabarfoori.com/fa/tiny/news-3219063
🔹
عکس عجیب نابغه ایرانی که نفر اول جهان را شکست داد
👇
khabarfoori.com/fa/tiny/news-3218974
🔹
گنج پنهان در کشوی خانه‌ها؛ موبایل‌های قدیمی از معدن طلا ارزشمندترند | یک موبایل چقدر طلا دارد؟
👇
khabarfoori.com/fa/tiny/news-3218959
🔹
ویدئو‌های جذاب را در آپارات ما ببینید
🔹
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/654902" target="_blank">📅 23:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654901">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
داروهای افسردگی به کمبود خورد!
وحید شریعت، رئیس انجمن روانپزشکی ایران در
#گفتگو
با خبرفوری:
🔹
داروهای روانپزشکی، از افسردگی تا دوقطبی و اسکیزوفرنی، با کمبود مواجه شده‌اند. نگرانی اصلی این است که این لیست در ماه‌های آینده، بزرگتر شود و داروهای فعلی هم قابل تأمین نباشند.
🔹
سرچشمه بحران روانی امروز یک چیز واحد نیست، بلکه تصمیمات کلان حاکمیت و نوع نگاه به مسائل است که روی همه چیز سایه انداخته و رسانه‌ها باید با دیدن واقع‌گرایانه یعنی نه بدبینانه کاذب و نه خوشبینانه کاذب به اصلاح شرایط کمک کنند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/654901" target="_blank">📅 23:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654900">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🎬
#تماشا_کنید
💫
دکتراخلاقی در نشست بررسی راهکارهای گسترش تأمین مالی غیرنقد عنوان کرد:
✨
بانک تجارت با تکیه بر تأمین مالی زنجیره‌ای و به‌کارگیری ترکیب ابزارهای نوین، آماده همراهی با مسیر جدید تأمین مالی کشور است
💠
دکتر اخلاقی با تأکید بر ضرورت عبور از الگوهای سنتی و حرکت به سمت ابزارهای نوین مالی، گفت: بانک تجارت با ظرفیت بالای تأمین مالی گسترده و بهره‌گیری هم‌زمان از ترکیب ابزارها، می‌تواند نقش مؤثری در هدایت منابع به سمت تولید و پایداری بنگاه‌های اقتصادی ایفا کند.
مشروح خبر
👇
www.tejaratbank.ir/news/2417055-bt.html</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/654900" target="_blank">📅 23:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654899">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f7bfc0ac.mp4?token=oU72IQjFaJow7rjx731Tt07HM0DcMgMBwzm_QlnrH-E2ga69TnHYZxrSkCE2wiwjH6-zB_jygigqrNs765gJ85xiJPkc2iF7W-I-DjrRKUME2iVaBa7wQAz57bI_l-f6QnSWHg6n_tSOewGHiLKhvCPVKT1QqsQCZ1BEYhs8NnAdOcBwq7X4439vosPhPbyDeET7qf6jCz9Scu7V7gcABqRSkOXMILdGOXIMoXRBNSKW8ERI833l-rfTkz5IeDMLRTFgYwSwbGrxCWfSom7qmf6cit-DutxRCTaWnOAL6U03TJZx7FLjm0JXMeGAGMZ4Br2mmsQwSKNfW61A0AEavgutSJw7Lhg8dvRBu98o1luqwLkpZLRlk5TbXi2hWfLpOPCuVU8Nrzfys6IU_vGn0Z2yw0pJr0E3KHFjfRltSF-qqSGHnRVf8l396UDbGXuRyGABRp9KfNjnMsgFwzvmTXGnHXHLGD4oLmJBZY6HSTkWBIqHtp-q9wT1Uwp2BNmc1zr2v4w5S9BrYrCWRrpp9XkQm-z42NfcWl3jI8mHQ8pEWEJvUzIvWsy6m_bG7-ZCDL_8foSK_CHP3aLcfRWauy3BHjNWMZS8yK48j9ETlq5ISbxsZwG5VowRrWH9HCNLkX94hdyRWN76tjO2LtFCcWIDjln1lWeFnB29bGlpDnM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f7bfc0ac.mp4?token=oU72IQjFaJow7rjx731Tt07HM0DcMgMBwzm_QlnrH-E2ga69TnHYZxrSkCE2wiwjH6-zB_jygigqrNs765gJ85xiJPkc2iF7W-I-DjrRKUME2iVaBa7wQAz57bI_l-f6QnSWHg6n_tSOewGHiLKhvCPVKT1QqsQCZ1BEYhs8NnAdOcBwq7X4439vosPhPbyDeET7qf6jCz9Scu7V7gcABqRSkOXMILdGOXIMoXRBNSKW8ERI833l-rfTkz5IeDMLRTFgYwSwbGrxCWfSom7qmf6cit-DutxRCTaWnOAL6U03TJZx7FLjm0JXMeGAGMZ4Br2mmsQwSKNfW61A0AEavgutSJw7Lhg8dvRBu98o1luqwLkpZLRlk5TbXi2hWfLpOPCuVU8Nrzfys6IU_vGn0Z2yw0pJr0E3KHFjfRltSF-qqSGHnRVf8l396UDbGXuRyGABRp9KfNjnMsgFwzvmTXGnHXHLGD4oLmJBZY6HSTkWBIqHtp-q9wT1Uwp2BNmc1zr2v4w5S9BrYrCWRrpp9XkQm-z42NfcWl3jI8mHQ8pEWEJvUzIvWsy6m_bG7-ZCDL_8foSK_CHP3aLcfRWauy3BHjNWMZS8yK48j9ETlq5ISbxsZwG5VowRrWH9HCNLkX94hdyRWN76tjO2LtFCcWIDjln1lWeFnB29bGlpDnM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روزگاری که سهم زنان در بهترین حالت زاییدن نوزاد پسر بود، شیرزن بی تکرار تاریخ ایران پناهگاه آزادگان بود ...
ویدئو کامل
👇
https://youtube.com/@caffeinepodcast2025?si=nNwcikUeYdjW2ckV
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/654899" target="_blank">📅 23:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654898">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
رضایی: محاصره دریایی یا با مذاکره و یا زور پایان می‌یابد
🔹
سخنگوی کمیسیون امنیت ملی مجلس تصریح کرد که محاصره دریایی ایران یا از طریق مذاکره یا با اقدام نظامی پایان خواهد یافت.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/654898" target="_blank">📅 23:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654897">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jx-Kz5AGj7HqbEgKbSwc6XDJLDZqmQiDKhQ3saWGrbJqXlYqqaavSC8Xs4DVil046GuST6C52z3nkJIq62ikQO9LZK_qFjFqtW4WeOCXXz_tAv01YHcopowvEc_7zdeARskB5af8DaVjb-poc7Y4qibrg2eUAO8tYmoINsZ9JCHSzgh2gLdvTazKkUWaRdTMjvM88v8rGX1VFZdYXF8Pc4ahxvrjP7TL4nin_uWhdF7PChyGkWcjZ_gvHOXd6rOv0_TYls_DcNFA8W313wjKjTd11-mct6O-pXg6Kjy-LxHk-ey44OkhqhLOyc1xJnOCMXfq9J3hkz5IPnWrpkwBFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگ با ایران چه بر سر بورس کشورهای منطقه آورد؟
🔹
بورس‌های ابوظبی و دبی به‌ دلیل وابستگی بالا به گردشگران و سرمایه‌گذاران خارجی، افت‌های دورقمی را تجربه کرده‌اند.
🔹
بورس بحرین هم با توجه به اقتصاد بدهی‌زده و تاب‌آوری پایین، منفی شده است. در مقابل، بورس مسقط با حفظ مسیر تجاری عمان، بیش از ۱۰٪ رشد کرده و تنها بازار سبزپوش منطقه است.
🔹
بورس‌های عربستان، کویت و قطر نیز به‌دلیل درگیری کمتر و تاب‌آوری بالاتر، زیان‌های ابتدایی را جبران کرده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/654897" target="_blank">📅 22:54 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654896">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/051195522a.mp4?token=DA3Pd1BKN7mPGHlLyTFzXc6PD0GE086Z9Hi_xpxvie-b2Q7JWkthQkJIavAGYmWVdlUAxr2NeLxfPYGlpMMmKAKXH2mZUgiRN3hNQOH6BHSMN8_E7DAFcgPZPXQ6dBDiVQNAedoF_4mDTj3rHNMRnwQyW7fvJsRqhUHe_xiSlE_o9JfIOePyWH5vWH7tck9CGgTfG5Y5FmCkSy_ZLePocv3CLu_lklVL_kLWXSSM9w5Q38ARZwT5kpGqM8sKqraaFN60uOfiOYQL4MJ6Bnju9jrVnKUatpXXpuRI8OU8uKmYdBQLyN4OHpWfZViiNV4_C_Q3jagBYLEmFJsH_YNOSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/051195522a.mp4?token=DA3Pd1BKN7mPGHlLyTFzXc6PD0GE086Z9Hi_xpxvie-b2Q7JWkthQkJIavAGYmWVdlUAxr2NeLxfPYGlpMMmKAKXH2mZUgiRN3hNQOH6BHSMN8_E7DAFcgPZPXQ6dBDiVQNAedoF_4mDTj3rHNMRnwQyW7fvJsRqhUHe_xiSlE_o9JfIOePyWH5vWH7tck9CGgTfG5Y5FmCkSy_ZLePocv3CLu_lklVL_kLWXSSM9w5Q38ARZwT5kpGqM8sKqraaFN60uOfiOYQL4MJ6Bnju9jrVnKUatpXXpuRI8OU8uKmYdBQLyN4OHpWfZViiNV4_C_Q3jagBYLEmFJsH_YNOSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه بالا بردن جام قهرمانی لیگ قهرمانان اروپا توسط مارکینیوش، کاپیتان پاری‌سن‌ژرمن
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/654896" target="_blank">📅 22:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654894">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d00b4012d.mp4?token=mVvBJqhVakH1NPUgGGfadmGsAQPSTGk3gjQ4p1yHPFGsbnha132iI0D50DHxHSqFHbBLGMSMblUSyUvR3QxpoCNhgkpuXZ2WwQksandm97megummKtUmdoFqfZ_Z9N2_HUhowWCFbFWQ688cqEhs2domfzzNOghe2IegrfyaOtKy6Nhc-qRkRLR4zgN4LAIVL-LYNuLyymxTs242aiLtai_HiUxGht2v_Sxz1xxTUdiHA3Yj7RynPyBzn3FyNddGbtYqN9Hlo24X0K3auUsb6zhcZ_ye6C88hXhjyRbHVdLe0lbNrWSakSfo8uncuJy_HQx3SqlIwgtyCU97StDRoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d00b4012d.mp4?token=mVvBJqhVakH1NPUgGGfadmGsAQPSTGk3gjQ4p1yHPFGsbnha132iI0D50DHxHSqFHbBLGMSMblUSyUvR3QxpoCNhgkpuXZ2WwQksandm97megummKtUmdoFqfZ_Z9N2_HUhowWCFbFWQ688cqEhs2domfzzNOghe2IegrfyaOtKy6Nhc-qRkRLR4zgN4LAIVL-LYNuLyymxTs242aiLtai_HiUxGht2v_Sxz1xxTUdiHA3Yj7RynPyBzn3FyNddGbtYqN9Hlo24X0K3auUsb6zhcZ_ye6C88hXhjyRbHVdLe0lbNrWSakSfo8uncuJy_HQx3SqlIwgtyCU97StDRoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار در  شهر بوستون در آمریکا
🔹
به گزارش منابع خبری ، صدای انفجار در سراسر بوستون بزرگ‌ترین شهر در ایالت ماساچوست واقع در آمریکا شنیده شده است.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/654894" target="_blank">📅 22:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654889">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
ادعای سنتکام: برای اطمینان از اجرای کامل محاصره دریایی ایران، ۵ کشتی تجاری را از کار انداختیم و ۱۱۶ کشتی را تغییر مسیر دادیم
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/654889" target="_blank">📅 22:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654888">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی استاد رائفی پور</div>
  <div class="tg-doc-extra">مراسم دعای ندبه_جلسه 60</div>
</div>
<a href="https://t.me/akhbarefori/654888" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
مراسم دعای ندبه - جلسه شصتم
رائفی‌پور:
🔹
0:07:10 خاص و ویژه بودن کوروش
🔹
0:19:20 عزت اسلام و حیات زمین در گروی ۱۲ خلیفه بعد از پیامبر است
🔹
0:26:15 معنای لغوی عاشورا در عربی
🔹
0:41:00 روایتی از حسادت صحابه نسبت به حضرت علی(ع)
🔹
0:55:50 اموالی که باعث آتش در قلب ها می شود
🔹
1:01:20 وحی‌الهی در معراج با صدای حضرت علی(ع) برای پیامبر
🔹
1:26:00 پشیمانی ابوبکر از آتش زدن درب خانه حضرت زهرا(ص)
#دعای_ندبه
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/654888" target="_blank">📅 22:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654887">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
انفجار در  شهر بوستون در آمریکا
🔹
به گزارش منابع خبری ، صدای انفجار در سراسر بوستون بزرگ‌ترین شهر در ایالت ماساچوست واقع در آمریکا شنیده شده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/654887" target="_blank">📅 22:07 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654886">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e21b66fdb.mp4?token=ipG72VWYq6YKkcx3L0d5PXPTGcaGyKEQrGAX5rh75Inq3ssB5jjgJfWP16jQ7oWs-9XiIofFgE35Ol85vN0is5iaQvw-FCFqe2PM34-ENWvP_0wA5yf3FIO1djgKBxlUBzzVZj1EXZt8XynmB2DSXzkWWOTxFpzC3Nh8QevZFr-kZoHldzdUFe6MboIsbmyMHo5lOZI6y9B5CWehPAndEl-M5TIzv0SyF2mzxS_fPZjsXsKtlbbfvnL0fyCKvDX3RVqR0hU0PkrifCQYz54WxPDm47IMHHdpU3J2Zq38YXZF1XsHxURc55R3ActoqaDHx_QLo8X5Imw39J1hLQ38Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e21b66fdb.mp4?token=ipG72VWYq6YKkcx3L0d5PXPTGcaGyKEQrGAX5rh75Inq3ssB5jjgJfWP16jQ7oWs-9XiIofFgE35Ol85vN0is5iaQvw-FCFqe2PM34-ENWvP_0wA5yf3FIO1djgKBxlUBzzVZj1EXZt8XynmB2DSXzkWWOTxFpzC3Nh8QevZFr-kZoHldzdUFe6MboIsbmyMHo5lOZI6y9B5CWehPAndEl-M5TIzv0SyF2mzxS_fPZjsXsKtlbbfvnL0fyCKvDX3RVqR0hU0PkrifCQYz54WxPDm47IMHHdpU3J2Zq38YXZF1XsHxURc55R3ActoqaDHx_QLo8X5Imw39J1hLQ38Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پس از ۱۰ سال فینال به وقت اضافه کشید
🔹
آرسنال ۱ - ۱ پاریسن ژرمن
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/654886" target="_blank">📅 22:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654885">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سرانه مصرف لبنیات به کمتر از ۵۰ کیلو رسید
ظفری رئیس هیئت مدیره اتحادیه تعاونی‌های فرآورده‌های لبنی کشور در
#گفتگو
با خبرفوری:
🔹
سرانه مصرف لبنیات الان به کمتر از ۵۰ کیلو رسیده است. شیرخام حدود ۳۳ درصد افزایش قیمت داشته و به تبع آن محصولات لبنی نیز افزایش قیمت داشته‌اند.
🔹
قبلا ۱۲۰۰ واحد تولیدی بودند که الان کمتر از ۲۵۰ واحد مشغول به کار هستند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/654885" target="_blank">📅 21:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654884">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fb1GVyB8dOYzeMZB7-r7PtZSeLD3_9pVpFa4JaRJpeGLJAd10J0oThDw8k4hqA7QyPr-emsSEAAJcN_-J4RDwrND_PJ48K6yBhLvKNTdtAbZMnwDNC4rIuNeOiUbYuq3JrNT5dTDEu10R8mPZSVIWFDCkdFjtcxQtnPCaST0_IxV8D8Jk3Ep-_k08kUAxKxBQGMoJIwtd-Yf0HedkyRFWbn3KD1_Y5juhdUTCZ9Byah_4wkWQ-iwxHnDB9aqEg3glgs7IAPfHrJN5pRHTdbutdEb6F53xkbN-qQmXRsK1pQTMxr8h9al53eCFoeeJ0kJzgbwizTeYuZ3-gwJjsgThw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار‌ وزارت بهداشت درباره نوشیدن قهوه در تابستان
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/654884" target="_blank">📅 21:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654883">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f25bca53dd.mp4?token=QRwzKsRDpms6r6UtG8FKDHTRRphGD9QWmUWOxH5B4g9Di0DzMREMK7FQ3v6V5dT6OjpN3nmsSW-o_5NqkqDTCti8j2lfgC2wznZyWJmro7wl_dfxsXmgLEQqTXcVfVb8dCICobYxTVjuGtV_pLo0SG3bsWjRLVvynFUc3NzlLtHU934gHjZ57fy1lPFuScJId_RVKIDzTtzLBo2Twus7jGBd5TA8P8SpW2-DnbRgcqzBVBC9RPC7E-hz73XoFCQCuHGqX_F4vU9Q1tSr4a2bAZad4gH6G97JG4a-tuPn_U97-jKfJW4f_RITOjqHFAdifc7Ec9CjcVt-j74agzALiwQCHe7uD-yP-pNz5-7dI-1OAX3bzmP6Vpqzp81zRmYNLVWhXY_odod9CRa_LEyn8X5hT2bP_shyhOeMC1srz36TE6_DpK9iH6jCuMi-xopOA-Ugzq2HcEM8nxdWNpAlRi8EkiKbXBSXK3-cuc9EazadNfk1b2T90Thrc52G1la7q_0WDlpl7BeWWlL-ToRWSIOvsgx7NQsk0NcVfS1qUux0sHZvgHdXiGchDOqwQ7SFjzYd21_Z_kg9LbJTU-hrkeIUW9dsAQF_d_Vik6MFZ-TliqxVWLGnZbZqgvtW8bxVYtHiygPxoaE2VnKkEce4HLcjNyd9vrLway_aCEQGpeE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f25bca53dd.mp4?token=QRwzKsRDpms6r6UtG8FKDHTRRphGD9QWmUWOxH5B4g9Di0DzMREMK7FQ3v6V5dT6OjpN3nmsSW-o_5NqkqDTCti8j2lfgC2wznZyWJmro7wl_dfxsXmgLEQqTXcVfVb8dCICobYxTVjuGtV_pLo0SG3bsWjRLVvynFUc3NzlLtHU934gHjZ57fy1lPFuScJId_RVKIDzTtzLBo2Twus7jGBd5TA8P8SpW2-DnbRgcqzBVBC9RPC7E-hz73XoFCQCuHGqX_F4vU9Q1tSr4a2bAZad4gH6G97JG4a-tuPn_U97-jKfJW4f_RITOjqHFAdifc7Ec9CjcVt-j74agzALiwQCHe7uD-yP-pNz5-7dI-1OAX3bzmP6Vpqzp81zRmYNLVWhXY_odod9CRa_LEyn8X5hT2bP_shyhOeMC1srz36TE6_DpK9iH6jCuMi-xopOA-Ugzq2HcEM8nxdWNpAlRi8EkiKbXBSXK3-cuc9EazadNfk1b2T90Thrc52G1la7q_0WDlpl7BeWWlL-ToRWSIOvsgx7NQsk0NcVfS1qUux0sHZvgHdXiGchDOqwQ7SFjzYd21_Z_kg9LbJTU-hrkeIUW9dsAQF_d_Vik6MFZ-TliqxVWLGnZbZqgvtW8bxVYtHiygPxoaE2VnKkEce4HLcjNyd9vrLway_aCEQGpeE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار گروه هکری جبهه پشتیبانی سایبری به شهرک نشینان صهیونیست
‌
این گروه اعلام کرد:
🔹
منتظر حملات شدید سایبری ما باشید.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/654883" target="_blank">📅 21:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654882">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a6e036557.mp4?token=umLmo2cFDCax-QpAIg8eUTTwyh5yf3ElUvz2RD-N2GRvZJE3vReiqP1bRUE4_qjepSwUKDzSzrnFlGtDy0U2ng9LTBjEsFJvUnxwuomc3q5krzaSE54gPUr967Zhn3SSZ4A0Mzlyeh2zXIV75974Hte4rm2pFLbAojvG5ZzY5c3Ld7fdxLfNWuuAZo6BES2jiscepJn-oW0aWyOms7tHrSh99mm-6G-IZ6udHf2zKOU17rjC_aByT1rzTCYyFiV7BhkCUIFvb2b777R7sTbFiaKxfJiA-3aSlRZYxF2FQKpNUrkQN6YiWAgoFdRFVNv6nmv1PRQFQYp0ovnvoxJHlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a6e036557.mp4?token=umLmo2cFDCax-QpAIg8eUTTwyh5yf3ElUvz2RD-N2GRvZJE3vReiqP1bRUE4_qjepSwUKDzSzrnFlGtDy0U2ng9LTBjEsFJvUnxwuomc3q5krzaSE54gPUr967Zhn3SSZ4A0Mzlyeh2zXIV75974Hte4rm2pFLbAojvG5ZzY5c3Ld7fdxLfNWuuAZo6BES2jiscepJn-oW0aWyOms7tHrSh99mm-6G-IZ6udHf2zKOU17rjC_aByT1rzTCYyFiV7BhkCUIFvb2b777R7sTbFiaKxfJiA-3aSlRZYxF2FQKpNUrkQN6YiWAgoFdRFVNv6nmv1PRQFQYp0ovnvoxJHlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلم لو رفته از عوامل پشت صحنه جنگ ایران
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/654882" target="_blank">📅 21:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654881">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pV3p3e-f5b7I7ZJyWRwptWcC2tL6BhVnmXG9msWH8xsua8cjySTStbY0-bH4ZyuPfhqGJk2iUnfmnfYQ_HEUMosfD8qSx5EMdNqYPyHRTTv947YQGwzU87MbTfzEABLR0XbyoChLRGbRTPNKqzJFSBFTpysD5hZl9Xb_AYcNhFsD4pnGQ-79NVfyOw84CWdOgCM62vYmtdbJPGxq55Hg8bXCdKM8W7hcnenxQOhycv6OGvFtzGimG1YNsMPH9saGIueY2VN02iP0qnRTwSaIAq6wbtY2Hl5pqfcd_GLSc7M3KKD6LqQ7k4wbvJjaOpRwWjLGk24UnIlPg0zFPq0Q3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گل مساوی پاریسن ژرمن به آرسنال در دقیقه ۶۴ از نقطه پنالتی
🔹
آرسنال ۱ _ ۱ پاریسن ژرمن
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/654881" target="_blank">📅 21:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654880">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
انتشار جزئیات غیررسمی از یادداشت تفاهم ایران و آمریکا
🔹
یکی از مهمترین محورهای توافق ایران و آمریکا بازتعریف قواعد عبور و مرور در تنگه هرمز است
🔹
ایران مرجع انحصاری تشخیص ماهیت شناورهای عبوری است
🔹
هر شناوری که محموله آن تهدید آمیز تلقی شود یا بهره‌بردار…</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/654880" target="_blank">📅 21:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654879">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07cf2a505e.mp4?token=FrQnqGDLANIfgTs4llTWCK5klT41cidLH_rVZiWxY7qEeJFmXqAx182ET5zpH3hVJkg0xCYDf8wVsIMQlabyKbG_XfBbx_SaLWR4Au2F7NGq0O0ldkVUqiHcP1YCXuQ6j7knQcjq2qElkKOUQdrYRolVs6W3gvGUQVquAPx4H_Yi838_wXaiDRdiTGO2qmMyep2Tdh8TQIvf8AYYFINQ8Q9NKkAp2acrp3jXABzIdHlObZE7xKVDJ9DR_pze_MvqM-adOjYP5cCGP2zQbyFfKgEnkDCry8NxUHajmyiFhJ-pTVsjyOJ3dBtzNd3VwBRQ1Wdc0jhim5xqhZ7jYS9Wtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07cf2a505e.mp4?token=FrQnqGDLANIfgTs4llTWCK5klT41cidLH_rVZiWxY7qEeJFmXqAx182ET5zpH3hVJkg0xCYDf8wVsIMQlabyKbG_XfBbx_SaLWR4Au2F7NGq0O0ldkVUqiHcP1YCXuQ6j7knQcjq2qElkKOUQdrYRolVs6W3gvGUQVquAPx4H_Yi838_wXaiDRdiTGO2qmMyep2Tdh8TQIvf8AYYFINQ8Q9NKkAp2acrp3jXABzIdHlObZE7xKVDJ9DR_pze_MvqM-adOjYP5cCGP2zQbyFfKgEnkDCry8NxUHajmyiFhJ-pTVsjyOJ3dBtzNd3VwBRQ1Wdc0jhim5xqhZ7jYS9Wtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خنثی‌سازی بمب و موشک دو جنگ اخیر در تهران ۱۰۰ رقمی شد
@Tv_Fori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/654879" target="_blank">📅 21:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654878">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
انتشار جزئیات غیررسمی از یادداشت تفاهم ایران و آمریکا
🔹
یکی از مهمترین محورهای توافق ایران و آمریکا بازتعریف قواعد عبور و مرور در تنگه هرمز است
🔹
ایران مرجع انحصاری تشخیص ماهیت شناورهای عبوری است
🔹
هر شناوری که محموله آن تهدید آمیز تلقی شود یا بهره‌بردار نهایی آن در خصومت با ایران باشد به عنوان کشتی تجاری شناخته نمی‌شود و اجازه عبور از مسیرهای تعریف شده را ندارد
🔹
تعیین مسیر حرکت و تعیین هزینه خدمات ناوبری در حوزه تصمیم‌گیری ایران دیده شده/صداوسیما
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/654878" target="_blank">📅 21:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654877">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cczobadjQStpFB4PGLqR45mVgvO5rL91zgleHtPxAURxDNUxOdGLwb6ByFqI-NlZX9JlzdhJZA8I8u7cZuT9fmDDHdllanpflckplle_alUf9tUaiVclHBQWJ56VfH5KtGmHmjvyT4HoFNDeehbR-sGRxL_6LD3J8LDFf0puD4120B4Zk54O7op3lyhOlJY4sUZ5QHj9SEShLo0dZwn2L_ab-UnfzaGB6tPWDsyF-WRWNG3o3ZyECTUP8nsjsgEgIKtaptE7-4hpPQ7iuuyZshknpprLjq-o9Qp13pRKAwmyA3gutXU5SMFx0KtadMsmjxTLkFZ-LZ1VzwS_QLiw7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکانت سفارت ایران در آفریقای‌جنوبی: تنها راهی که کشتی‌ها می‌توانند بدون هماهنگی با ایران از تنگه هرمز عبور کنند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/654877" target="_blank">📅 21:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654876">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
تناقض کاخ سفید در توضیح علت کبودی دستان ترامپ
🔹
مجری CNN:  «در گزارش آمده که موضوع کبودی دست ترامپ با تحریک جزئی بافت نرم ناشی از دست دادن مکرر همخوانی دارد...»
🔹
دکتر راینر، استاد پزشکی دانشگاه جورج واشنگتن:  «این گزارش توضیح نمی‌دهد که چرا دست چپ او هم…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/654876" target="_blank">📅 21:07 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654875">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
نشست نتانیاهو و دیگر مقامات نظامی صهیونیست تا لحظاتی دیگر
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/654875" target="_blank">📅 21:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654873">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04f71830e2.mp4?token=EgL4S6zGG7P0TiPBxevjCRuiTrPBfcyidLkdB5SMP1X7s-WprpwEtpfKQLjYDdbWdcx2HY8pAKW12YdwfGevjYcSxxImSN3bTZ7RqQdUBZV6xP0LYEOeBBRb5rUXfzxg-vHW4TiZfIfntPOFdeUUZf2wdbZhlh3vfHeqApxdKkz-JlUOnvjQ8eUuC_Clbybe-Wc-yQwQMWl0dVLwuOU-EpaUMaxyRJ18LxAxzdogmeNRYNE8HBU-zh8WmS0su4tSYAPj9kdPJfQUJyg1ATRxXwC6gRctN8PjoogLiUtwFti0ckTfCM-hGVVADBgx14OZAFsg3W6pgICg8AbJWrH8yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04f71830e2.mp4?token=EgL4S6zGG7P0TiPBxevjCRuiTrPBfcyidLkdB5SMP1X7s-WprpwEtpfKQLjYDdbWdcx2HY8pAKW12YdwfGevjYcSxxImSN3bTZ7RqQdUBZV6xP0LYEOeBBRb5rUXfzxg-vHW4TiZfIfntPOFdeUUZf2wdbZhlh3vfHeqApxdKkz-JlUOnvjQ8eUuC_Clbybe-Wc-yQwQMWl0dVLwuOU-EpaUMaxyRJ18LxAxzdogmeNRYNE8HBU-zh8WmS0su4tSYAPj9kdPJfQUJyg1ATRxXwC6gRctN8PjoogLiUtwFti0ckTfCM-hGVVADBgx14OZAFsg3W6pgICg8AbJWrH8yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول آرسنال به پاریسن ژرمن در دقایق ابتدایی
🔹
آرسنال ۱_ ۰ پاریسن ژرمن
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/654873" target="_blank">📅 20:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654870">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rRfi7BnxHamO9qnINAEWYqs3MBN7fgOc_UbJSdom4JnYkVRTOx3FxJNE_DC0cU4mkr4yQSQ9m4u113AwKPIbtMm-gZMENMIrdHfQA_Qi2ByCpx9-aRHsb-GUeAiLfbMDzPvb3oiN5NU5q7hCH65AxEJoREFT1eZb_MnnKFcDThpo93D-hg-_-QuPRT_g24KsD9rvC_Z7q6Y8WlqJfoAf4Zn04PKq4_lryWx8DuRBJViAem3G4i6POZ2N-I6gLBxBk1V5mB0qdUw8R4q9IOZHFn6CCxvpBw1dJQvGWnXQvVnkNaXq6uhnVJchXEK4M4FDIV91Xi8NdY48n_EoU1JxrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HEkAnweMRo-fXrNk93Lf6J5lO6v8E8alMF1ldokwjspOrErcl_ok0l7ZOs8-s-g8xpwTDUK6EfCueQfFTKeTPIdzjinFrywEeJ0AS5Bu50wGtsJRlHM4oaeqrmAE2uRmn-st_8ZR-n-4rHIjcJx-MtooPcs3d-_-AyYnke16Dk2RvJ7taqRg1kVEDUZ14B6DQsndFsT372XZ_0mIxZI6Vt4ZgNzi9YiQD2IjE8OagD-JK0TNxB8AhThyXJikkxV12562t-VQQCim_-Ml1pJDd9HFt06i2A6_UIRYAh0GLFqM6zGFKm7AR91ZWM7WhX-khRTZeQqPlAFzlMj-yvMOjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q4zGggcGj2Q_llKgNukQVtbOwNp0y0sDr0yZt2pFynJusAcf8SPH0vUNJovrFLdBtrBXT6U84R_y1zoc1VcxFoLLIUzwCublfkCsIp68wnp8PpYrQOUlJ3f9dlyzJmyIqYtoMl3diGGE6A3zUOy-U8mNWPICTFkTh_QiY4CVrDDBJ1xqmldsvTFWxD8BhooaPF7xV4E1sQFhF_7rBUKK9ENEAAXcQDFyEVqS9kK5EOPfaxwlXVWUwvPLB5E6-Ppm9Hb6B89yXJedkx0eSy8FLddhdElw_m0wfaA4q9fJSEzinymMpJwqivcR0iy4Kvq_trUPM5ZaqzZGlHhH7skJ-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
رئیس‌جمهور برای مدیریت انرژی کت خود را درآورد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/654870" target="_blank">📅 20:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654869">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvQswiNkvT_NTTmmfueN5EZcI1Lngzx5HH10_U_MJqF7IQwX13WpUjSJ7oKXNzrvnv7Yx9fFtsZVdWCVs-qYEfo0T9LCt-DSnStKi_4R-SvQf6r7p_MbxReSAyrVxGGOY7qryOs4gK3CIzqB0FVWRG7U1MBk4NiZJwl_YSlvzjOVQZSw2pWPikCrrLYeNNHHX1eEP4vF5DfG-RwtuRR-LvQEd0IPpdHhd6gip6JfotbUY_mOy30kdhfYDavkBmcvuU8YjmhXFx8jGa-oUAeZCm0Uf5HSgHgd-UJzjXLOr6tHocj5_OAiyWJPScGvevJVcnOW319nE19bc-hNWin-cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این گروه‌های خونی بیشتر در معرض سکته مغزی در سنین پایین هستند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/654869" target="_blank">📅 20:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654868">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
۹۰ درصد پول پروازهای لغوشده تسویه شد
‌
معاون هوانوردی سازمان هواپیمایی:
🔹
طبق مستنداتی که شرکت‌های هواپیمایی ارائه می‌دهند بیش از ۹۰ درصد از بلیت‌ها تعیین‌تکلیف‌ شده است؛ ۱۰ درصد باقی‌مانده نیز کسانی هستند که اقدام به آغاز فرایند استرداد بلیت‌های خود نکرده‌اند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/654868" target="_blank">📅 20:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654867">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
در تجربه مرگ موقت، آینده‌ای تاریک از خود دید؛ تصویری که باعث ترک اعتیاد و تغییر شد
🔹
06:00 عذاب کسی که به نامحرم نگاه بد و دست درازی داشته
🔹
10:45 نوشیدن اشک دیگران توسط جهنمیان برای رفع تشنگی
🔹
18:50 رؤیت افرادی با چهره هایی بسیار زشت
🔹
22:50 کدامین گناهکاران مورد عنایت قرار می گیرند و بخشوده می‌شوند؟
🔹
28:30 چگونگی مورد شفاعت قرار گرفتن تجربه‌گر توسط حضرت زهرا
🔹
35:50 حس تولد دوباره بعد از  تجربه
🔹
47:50 سفارش اهمیت به مادر و همسرم در طبقه اول جهنم
🔹
01:07:40 ماجرای شنیدنی دعای هدایت شدن درحق بدهکار توسط طلبکار
🔹
قسمت دوم، (منفی هفت)، فصل چهارم
🔹
#تجربه‌گر
: دانیال قاسمعلی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/654867" target="_blank">📅 20:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654866">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ادعای آسوشیتدپرس: آمریکا یک کشتی فله‌بر را در خلیج عمان از کار انداخت
‌
خبرگزاری آسوشیتدپرس:
🔹
یک کشتی فله‌بر لیان استار که با پرچم گامبیا به سوی ایران در حرکت بود، هشدارهای مکرر نیروهای آمریکایی را در طول شب هنگام تلاش برای ورود به یک بندر ایرانی نادیده گرفت.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/654866" target="_blank">📅 20:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654865">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
آزمون‌ساز شبکه شاد پولی شد
🔹
در حالی وزارت آموزش‌ و پرورش اولویت برگزاری امتحانات را در سامانه شاد اعلام کرده است که آزمون‌ساز شاد بسته‌هایی با نرخ‌های متفاوت ارائه می‌دهد.
🔹
از بسته ۵۰۰ آزمون به قیمت ۷۴۹ هزار تومان تا بسته ۳ هزار آزمون به قیمت ۳ میلیون تومان در آزمون‌ساز شاد به فروش می‌رسد. / خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/654865" target="_blank">📅 20:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654863">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
اعلام آمادگی گروسی برای کمک به حل اختلافات بین ایران و آمریکا
‌
🔹
رافائل گروسی مدیرکل آژانس بین‌المللی انرژی اتمی اعلام کرد ذخایر هسته‌ای یک نقطه اختلاف بین ایران و آمریکا است و برای کمک به حل آن آماده‌ایم.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/654863" target="_blank">📅 19:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654862">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b21f9c1c3.mp4?token=R_hP2rzsASYrP8tWotLSCnzySRp3nPijpZ66RhFaCs5jY8v4s0HcpfOaswiHamgfMBtdSiKFNJTJ6kNuazCE8KLe1-LpiUCktVa2c2-4c9TLriFTsMEP-0ndoIs5FBig-k6Ygr1QnjdrkkPNYjUaBvcjk8mm2quIAaLYoHbX5SdH8iqGdaZK2yCkG9KZwZq93X4pySfGZSifdgb0q7ITY4Dn_R4nKWsfgGzfBWGqUG4LxfdMoau6ePavuH8OwRKPCS7Jt1i0CvzA0lm9xzxpJbONY2gsu-KXyiYpD73h09dK8PuTaVp_o1mr21tvP3ntCovS4g1UxhozdFKGDi4H0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b21f9c1c3.mp4?token=R_hP2rzsASYrP8tWotLSCnzySRp3nPijpZ66RhFaCs5jY8v4s0HcpfOaswiHamgfMBtdSiKFNJTJ6kNuazCE8KLe1-LpiUCktVa2c2-4c9TLriFTsMEP-0ndoIs5FBig-k6Ygr1QnjdrkkPNYjUaBvcjk8mm2quIAaLYoHbX5SdH8iqGdaZK2yCkG9KZwZq93X4pySfGZSifdgb0q7ITY4Dn_R4nKWsfgGzfBWGqUG4LxfdMoau6ePavuH8OwRKPCS7Jt1i0CvzA0lm9xzxpJbONY2gsu-KXyiYpD73h09dK8PuTaVp_o1mr21tvP3ntCovS4g1UxhozdFKGDi4H0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول آرسنال به پاریسن ژرمن در دقایق ابتدایی
🔹
آرسنال ۱_ ۰ پاریسن ژرمن
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/654862" target="_blank">📅 19:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654861">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
اعتراف نخست‌وزیر لبنان به جنایات گسترده رژیم صهیونیستی در خاک این کشور
نخست‌وزیر لبنان:
🔹
اسرائیل تنها مناطق مشخصی را هدف قرار نمی‌دهد، بلکه سیاست تخریب فراگیر را اجرا می‌کند. اسرائیل با این اقدامات، به کوچ اجباری و جمعی ساکنان نیز دامن می‌زند.
🔹
تصمیم گرفتیم به‌سوی مذاکرات برویم، زیرا این گزینه را مناسب‌ترین مسیر و کم‌هزینه‌ترین راهکار می‌دانیم.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/654861" target="_blank">📅 19:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654860">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38b51d87ca.mp4?token=vRnE97Sn32u7IOVT_E9R9AfZLXjnxIBZKZxr0IJ0hoy96gNG9b_bbFfsLp1lZVfcovo3SraWivT_LBRkzu2jZSqmmO4qUdSN4s5yiR90qqpUyCWOwWPTnSRwVuXK11KnZnLV-Y5ozemoBxp3wdg6ycpIvdZBL7To_rV90f7NjL3oHKLF4VjRIwzDo-BfiG5YQN1yaPbMZukaj0zBXZPuCPqk8nvHvoB0Z43raPyC96uCnbqLwlbQQgAE9hjZVV6hI3X2WuqDnq5IlwxZ1Wj6lrfhtN1ipDMjfrOTDZCdg5ajF3wf19X60pO_sJxm443FXatwhuEDxXOopvokeqWLxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38b51d87ca.mp4?token=vRnE97Sn32u7IOVT_E9R9AfZLXjnxIBZKZxr0IJ0hoy96gNG9b_bbFfsLp1lZVfcovo3SraWivT_LBRkzu2jZSqmmO4qUdSN4s5yiR90qqpUyCWOwWPTnSRwVuXK11KnZnLV-Y5ozemoBxp3wdg6ycpIvdZBL7To_rV90f7NjL3oHKLF4VjRIwzDo-BfiG5YQN1yaPbMZukaj0zBXZPuCPqk8nvHvoB0Z43raPyC96uCnbqLwlbQQgAE9hjZVV6hI3X2WuqDnq5IlwxZ1Wj6lrfhtN1ipDMjfrOTDZCdg5ajF3wf19X60pO_sJxm443FXatwhuEDxXOopvokeqWLxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جام قهرمانی اروپا راهی ورزشگاه شد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/654860" target="_blank">📅 19:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654859">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItS6Jg2qMkI-fCQqJIjvnToIU6c8gn70eflznkyCe9l8aRGahm2vg8v51okVAqAI71r4gacDClGhFpH1KjNquPTJuwt-N1eLlNnUsX9alvFvxfn-Gds3CwUuhFCWSsmfvVad9YSLZjBaNIDCvj5k3dci2E1EsP7MqIYtuChTOIbhA1S-2tXTKRd89rDZXP0oivBDtH94i_x0jST2q_xo8bchTumS4q7F6NohLjUFe9TQhutNoB5be4VHTz6ccdrPkV_gzteuborFGkY91U-yynsvHIfh7b6vJnYq9W1X9SN_2YhQ4evla1H5Gp7x7Ms2TA6y_hNwur6bdc_ZbU3QTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعایی درباره کمک نظامی چین به ایران در جنگ با آمریکا
🔹
برخی منابع به ان‌بی‌سی نیوز می‌گویند ایران ممکن است از موشک چینی برای سرنگونی جت جنگنده آمریکایی استفاده کرده باشد.
🔹
افراد آشنا به این موضوع گفته‌اند که چین ممکن است یک رادار هشدار اولیه دوربرد در اختیار ایران قرار داده باشد که هواپیماهای رادارگریز را که برای فرار از شناسایی طراحی شده‌اند، شناسایی می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/654859" target="_blank">📅 19:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654858">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQCfynls1vGMURgi_9dC8r6FMUZzfV55LCifaVpi-aAiGg7ZWeOoPEAAY5jlwBezBA07wtOHOFXQxzBNHdjTpOwADysOp6a2j58hBZ3Q_WCCghB6zdFErmri4ooR3N2S7zJcLwfiyvak2GEctsd4bn6Q4QlMn8p-KggVD-MLyFS0HAd3chkPDRqDIDiKXa5gcjhuqs4oz36iYa33IhuK2TbUvadnNgHXwCrzWE12mPPk8aKAqITTzBy8rFohhnEoXyXXDONXKOc6ycw0ENQfbM5vO7lDOOhQg-s3Bw6092X-5OYRjhJLVHvoAHPg9sPQnJndIUHykqfvgwl33nWlTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری تماشایی از رنگین‌کمان در ارومیه
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/654858" target="_blank">📅 19:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654857">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بارورسازی ابرها قیمت خورد؛ هر هزار متر مکعب حدود ۲۵ دلار!
جوادیان‌زاده، کارشناس ارشد توانیر و رییس سابق سازمان توسعه و بهره‌برداری فناوری‌های نوین آب‌های جوی در
#گفتگو
با خبرفوری:
🔹
افزایش بارشی که برای باروری‌سازی ابرها می‌تواند اتفاق بیفتد بین ۱۵ تا ۲۰ درصد است اما برای کل کشور اثرگذار نیست.
🔹
حدود ۳۰ تا ۴۰ درصد این افزایش بارش تبدیل به رواناب می‌شود که به شکل منابع آبی زیرزمینی یا پشت سدها ذخیره می‌شود و داخل رودخانه‌ها جریان پیدا می‌کند.
🔹
قیمت تمام شده بارورسازی ابرها برای هر هزار متر مکعب حدود ۲۵ دلار است و روش ارزانی نسبت به سایر روش‌ها است، اما روش پایداری نیست.
@Tv_Fori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/654857" target="_blank">📅 19:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654856">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ej4pXEYoyRA4gOW3ogS6tm7xFf0Yu9q4RzLQWMw3AP1BVwFKRHSdzhnJ93LueLLWmouzR0NaKelyUoSnOKqt-79KXYcFYF-ggRYTU4kviMavq-OOnDKWShbDIG-ViPE92ma9LhsU6-nyEtLSUa38vOWIqTvxhskbAhkrgUKk_Iar0_xaPO8UxokN6CZU6yragFHl_y6HjDmg1mD7Ez2BHjfkj3JjrNToc1DhLKfmJM5qWjJUxEE8kM4Et9UVqG6N5i8ExuAhEOcnr3gU8pNP7PXr1iPXA9FrgBrK4TRRZVPWpf9NDkjxN5p067ok8sI4GHkeHyiX4oZV_MwdQSbJ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خاندان بختیشوع؛ بنیان‌گذارهای پزشکی علمی در جهان اسلام
🔹
خاندان بختیشوع یکی از مشهورترین خانواده‌های پزشک در تاریخ ایران و جهان اسلام بود. ریشه‌های این خاندان به سنت پزشکی جندی‌شاپور در دوره ساسانی و پیش از اسلام می‌رسید؛ جایی که دانش ایرانی، یونانی و هندی در هم آمیخته بود. بختیشوعیان پس از فتح ایران این میراث علمی را حفظ کردند، به بغداد بردند و برای چند قرن پزشکان برجسته خلفای عباسی، استادان پزشکی و از پایه‌گذاران بیمارستان‌های علمی جهان اسلام شدند.
#نامداران_تاریخ
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/654856" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654855">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
مدیریت تنگه هرمز توسط نیروهای مسلح جمهوری اسلامی ایران با اقتدار کامل اعمال می‌شود
قرارگاه مرکزی خاتم الانبیا:
🔹
با توجه به یکپارچگی این مسیر، تأکید می‌شود کلیه کشتی‌ها، شناورهای تجاری و نفتکش‌ها صرفاً ملزم به تردد از مسیرهای تعیین‌شده و اخذ مجوز از نیروی دریایی سپاه پاسداران انقلاب اسلامی هستند. هرگونه تخلف از این ضوابط، امنیت تردد آن‌ها را با مخاطره جدی مواجه خواهد کرد.
🔹
همچنین هشدار داده می‌شود هرگونه اقدام شناورهای نظامی جهت مداخله در مدیریت تنگه هرمز یا ایجاد اختلال در تردد، مورد هدف نیروهای مسلح جمهوری اسلامی ایران قرار خواهد گرفت.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/654855" target="_blank">📅 18:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654854">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W615WHkIQkHaSMUMbFXQWCWrXX20akHwjOfIlPTfqh6GG2mQFniuqZ-K2aYhcJXHXTF6x5ZCQ5isC90zcKmduEol5HFydEqbAcZ6FqWrCdkUmXt0VG5uzHwnti9iCnE5DZY4dVhgQ7oUZ9Gy-Z_fx67ybAKMVIFr51CQw3LRWjS0xtRJmerUIi3G0-c2C04IGnUVcOQ4UWlObsnaRaNeYyIJ0hmkznNKf0zIARQAqc9QrKnXXpHxvKl9UAOtHmAp_CWtkFYccq6ONpf6WiYxSCjxGLJiwFVRtQKUu43w3XTbs3lLD49XrKUy2HX6FGBmmdc5ljkRg2qU_mFMXYMFJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ رکورددار تریدرها شد!
🔹
دفتر اخلاق دولت آمریکا فاش کرد که ترامپ در سه‌ ماهه اول ۲۰۲۶ نزدیک به ۳۹۰۰ معامله ثبت کرده است. یعنی روزی بیش از ۴۰ معامله که میانگین روزانه‌اش را از بسیاری از تریدرهای حرفه‌ای وال‌استریت هم بالاتر برده است.
🔹
در تمام سال ۲۰۲۵، او هر فصل حداکثر ۲۵۰ معامله انجام می‌داد. اما سه‌ ماهه اول ۲۰۲۶، ناگهان ۱۵ برابر شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/654854" target="_blank">📅 18:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654853">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
گمرک مهلت تردد خودروهای پلاک خارجی دارای مجوز ورود موقت را تا پایان تیرماه ۱۴۰۵ تمدید کرد
🔹
این تسهیلات شامل خودروهایی است که مجوز ورود موقت آنها تا ۲۹ اسفند ۱۴۰۴ صادر شده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/654853" target="_blank">📅 18:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654852">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/633f3ac517.mp4?token=NIiq-RHaBjvZ7725AJQJkcb3zijRNCwWbn88lAjMKOO370ty6Et-in1gLkPVwx4O7Jc4y5hQFetYX3sdnMy1jjvAN1LT2nOrqsp4xGLLWibGZPfQkFz7j6HzLYSPTyR2mFXZRAwdJRsm3d8tF9TDfovGJRO6IsEU21Ts1uWKX6lJPHyBFet6tWrhZpg67epwfJhJzZeF1UAGf1KjP0vmgAErJuvLLtcY5bp3uRCcOq9qQdEWWlIiVSASxWxx_arF912y1IYnJXZz3U8tCeoda_d63voOJUsQvXVJ-Cuj-uCOnIUlWSs10MB1GzUanYRRY0WwYjsUlmXnbJ4Q7fQyEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/633f3ac517.mp4?token=NIiq-RHaBjvZ7725AJQJkcb3zijRNCwWbn88lAjMKOO370ty6Et-in1gLkPVwx4O7Jc4y5hQFetYX3sdnMy1jjvAN1LT2nOrqsp4xGLLWibGZPfQkFz7j6HzLYSPTyR2mFXZRAwdJRsm3d8tF9TDfovGJRO6IsEU21Ts1uWKX6lJPHyBFet6tWrhZpg67epwfJhJzZeF1UAGf1KjP0vmgAErJuvLLtcY5bp3uRCcOq9qQdEWWlIiVSASxWxx_arF912y1IYnJXZz3U8tCeoda_d63voOJUsQvXVJ-Cuj-uCOnIUlWSs10MB1GzUanYRRY0WwYjsUlmXnbJ4Q7fQyEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حزب‌الله، شهرک‌نشینان صهیونیست را وادار به فرار کرد
🔹
موج شلیک موشک‌های انتقامی حزب‌الله به مناطق شمال فلسطین  اشغالی، سبب فرار صهیونیست‌های مهاجر به پناهگاه‌ها شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/654852" target="_blank">📅 18:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654851">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjFE8-KDrVvIWUPaZIp5BOBrsT94XUZBcomSsGVPf4vqXYCvH-O5FlJc5KWutoaNJ9SRGxNeSU83yddYSsSZR-s1S2pgQkBzVOMX-EPo_H1_zxbHbCluPominIiSPLmbLV9kSk1HkANHYqRpNbvdpu0aqpPZLBzMArb2BJnQ-2u5YKkVTcSNIsueLqbTOHesy9Sb5tn7O23VEYJDVn6RFXlUkpfeE06hNjKTb4V8q1hr0sfkkFR6gR9smRgM19r-W-7HypoH8RJj6kLQagtVk2jVN40wnsIdTFvVbQ33teH09mvFmUztwSjEukQfucUPp_JEBwPnZdib5n4x_KxzFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استقلال و تراکتور، نماینده ایران در رقابت‌های آسیایی
🔹
تیم‌های استقلال و تراکتور به عنوان تیم‌های اول و دوم جدول لیگ تا پایان هفته بیست و دوم، به عنوان نمایندگان ایران در لیگ نخبگان آسیا معرفی خواهند شد.
🔹
همچنین تیم سپاهان به عنوان تیم سوم لیگ به عنوان نماینده ایران در لیگ قهرمانان آسیا ۲ معرفی شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/654851" target="_blank">📅 18:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654849">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CaYuUHMCaeKFEVe0J33jfSZTW0XPk65P99RQrTYdtMPmiNy7SEW5eigXAqpaAoX-4BikuDQ9Baqiwv85-UIN3hSmRJQpotdwenSRqbfA_1SIfp_5Ks4OeTWfoQ7m0d6-Mmivx45KwOgZ30n7Q4oPaROSgfLY9vSCYEJAjeS25fz_eYXlbryeZwp1syiPlaQTCuPLnFJTg0XbAaW_hG4sXR_00TmZ8WFGLsIc7vmesGQnaBNd6mzEOo-tK_HOGjJJn7HpzZ3AelrtHD2LKQLISA4EWW2OzmQ5y29G_qZiyoOK-moF4wmlueRBOL-dSus2iNEAgKECUdz1GMPV6byFFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7s-7_sTtybFZeRNGl0h0LqqR8hyesAdVL34zJ5SaYBJlrlOxoKlIDl4kzU9MR9JVGRpFcu7FH31nH2DVxyyELIdGXIDPhNL8h8G5Vf_pK7bGgQJZ_JszGqjTDE72oZOre1IhV1BzLzrLQ3jPdAxpEY22WVMsyS9pwyLR67n5cmWDBv30hNyMW8sMxdP0_SQU48keHZQwsjafEUvevVO1GX8mhgDXBWIoVWmXa69UDaxWna9v1ntbZqnvSPPPyOhCjOeD4dqaqA16ijm4Y5Y07YEHnqjeAhJw0F2gu4cEPKMCCAnWd_GR6Drw1a8Zed6uKKDxNVva2sfXhvnAyEPAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
لونا، شیر ماده که در پارک حیات وحش در کره جنوبی زندگی می‌کند و بخاطر خوشگلی و قیافه منحصر به فردش در دنیا معروف شده است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/654849" target="_blank">📅 18:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654848">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
شبکه ۱۲ اسرائیل: از صبح امروز هر ۲۲ دقیقه صدای آژیر حملات موشکی در شمال اسرائیل به صدا در آمده است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/654848" target="_blank">📅 18:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654847">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIqHQ-AfCONHJmQxbpVTg5M1dHk7-N2Lz3e7KRFO_wNvzm5aHA0S1B3x4GbVwLiY7I543B2oHU8r5-Ub9ZVWLx4_eaM9XC_s5_kWYr3s-3cBW27z9zS8m9vzjvJkwQgs2jsvonubKhnDGWipt3dSocbK-emFlQIcVNDam-TOZwHYMrv54ydwAt8AYR6XGQSdLwBWLATnj1ST4zbtl_AnOEdaoKpQJVh1skSsR5hDGQx_uYWLQTFKkYntmotQ7jruxPICiLBdLCtUg5iPsTA8iVVglGOuOQQELaqxHDGOPwjfl4xIFQTCxcYrE9UDIAhxSzh6QUV7EHghWdTz_FyQUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرواز همای، خواننده: هزینه تاریخ نخوندن و اینترنشنال دیدنتون برای ایران خیلی گرون تموم شد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/654847" target="_blank">📅 18:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654846">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
سی‌ان‌ان: نقشه رژیم تغییر کرد/ تهران نه، واشنگتن!
سی‌ان‌ان:
🔹
نتانیاهو پشت درهای بسته اذعان کرده اسرائیل نفوذ محدودی بر نتیجه مذاکرات پایان جنگ با ایران دارد. او خواهان حمله به تأسیسات نفتی ایران بوده و کوشنر و ویتکاف را متهم کرده ترامپ را به سمت پایان دادن به خصومت‌ها برده‌اند.
🔹
اسرائیل آن‌قدر روی «تغییر رژیم در ایران» حساب کرده بود که احتمال «تغییرات سیاسی در واشنگتن» را ندید./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/654846" target="_blank">📅 18:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654845">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b05a6002ef.mp4?token=AjFIuFbc1R1ltZvAt0ye0DdxujbxQaiLnkdKCJMb7QoJ_mGtzvdVSBsjlAXtZnOyPcHFlPvgXQW8COO7q8wmu2h5CLtKxC8RQeNuviz2FOcqXGYi1rXfa3OHjfrrmP5FMEiZ7o6crYEWaAoIgOmw5wiwcyOapBFzw24i8fS_WDA-SDLKUflKuXbKQD9xvD3RddOvZWGvP9hTNokyINWlG6nemZeoV-DGtt2eViiHxnTIJSdzyM6qwvXPC6ofNFKB79vlXsoG35u3FQrtPVK8OAU_1j3gd6YSzLOE7JPpjEZoousSyO8nUceFOeTbpt36Gl80sOLpk_ns8pJeWd-uVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b05a6002ef.mp4?token=AjFIuFbc1R1ltZvAt0ye0DdxujbxQaiLnkdKCJMb7QoJ_mGtzvdVSBsjlAXtZnOyPcHFlPvgXQW8COO7q8wmu2h5CLtKxC8RQeNuviz2FOcqXGYi1rXfa3OHjfrrmP5FMEiZ7o6crYEWaAoIgOmw5wiwcyOapBFzw24i8fS_WDA-SDLKUflKuXbKQD9xvD3RddOvZWGvP9hTNokyINWlG6nemZeoV-DGtt2eViiHxnTIJSdzyM6qwvXPC6ofNFKB79vlXsoG35u3FQrtPVK8OAU_1j3gd6YSzLOE7JPpjEZoousSyO8nUceFOeTbpt36Gl80sOLpk_ns8pJeWd-uVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تجهیز جنگنده‌های سوخو ۳۰ ارمنستان به موشک‌های هدایت‌شونده ایرانی
🔹
به گفته کارشناسان نظامی، در رژه هوایی روز ملی ارمنستان در میدان جمهوری ایروان، جنگنده‌های سوخو-۳۰SM نیروی هوایی ارمنستان با بمب‌های گلایدر (هدایت‌شونده دقیق) ایرانی یاسین پرواز کردند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/654845" target="_blank">📅 17:54 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654844">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21774a84d5.mp4?token=crm1K8SJq3UehAb43ZsdUmGUbFEWXNuoXTvZYFoUJuhzfD2RG6SW58TRcrSHTw_5CK73GvIE6I7zD2ANYrX7yFNVQRGQv-bmkuB1Wv1o802P3fZhqWQvggUgUV_p-Uwwx9XlNifKXBovBAyJoui2c2Qp3wmZ-QF1LeUsQbUCDsde6SMoZQRwTe8mBBmQuiThcxNCHjhzt6NlWaTcz_hgcs0zg4r8XB0gkHBITl-1d-iqBY-ThWg8Y0SMqRjwevts9v4Dgw8BVGXd70uuE7HtcmOTpDsrHOZoSiOUIqMRdjZQMUgzwQB0prZGG5mI-sDmN5d9fc6ik5kc3ulL6Gwr3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21774a84d5.mp4?token=crm1K8SJq3UehAb43ZsdUmGUbFEWXNuoXTvZYFoUJuhzfD2RG6SW58TRcrSHTw_5CK73GvIE6I7zD2ANYrX7yFNVQRGQv-bmkuB1Wv1o802P3fZhqWQvggUgUV_p-Uwwx9XlNifKXBovBAyJoui2c2Qp3wmZ-QF1LeUsQbUCDsde6SMoZQRwTe8mBBmQuiThcxNCHjhzt6NlWaTcz_hgcs0zg4r8XB0gkHBITl-1d-iqBY-ThWg8Y0SMqRjwevts9v4Dgw8BVGXd70uuE7HtcmOTpDsrHOZoSiOUIqMRdjZQMUgzwQB0prZGG5mI-sDmN5d9fc6ik5kc3ulL6Gwr3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان وحشتناک در شهر بیکانر در هند
🔹
طوفان گرد و غبار عظیم، شهر بیکانر در ایالت راجستان در هند را تقریباً در تاریکی فرو برد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/654844" target="_blank">📅 17:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654843">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b84f533728.mp4?token=bYIGy1LiwZoJ0TTbnqILA8QvkmK8sxlhbGkrN7KJXnzluDkq9g-YFCQ3E950OghaZbg1Mp2OCWFX57au-6qkFDKrgJ2vh-xe1SRKNoE7bMG6RGb6_at7DzNMS-POpOZHr5wCbNj4JiTB4VQ5kPvb6-fCIOYOScna_cgA1qTRitHuAEeoeqwmbmITvSQvevUePJVbj9PGOjxufbRoOtWRfj_DjN31DD4A8b24zkVTLCuFnwK5MWAZ4tFh0otBNgwOPkl-kEe9Btew_1t46e5md1pH-Ujd8oZ2pxu5zVGWwB7ZVwhj19oWzIK0bnsRJUFwLDjsESvmWxNfvvjRC0lNPS-hMjGqF8c3HzXfGNnqgVRh9VowM85R9PxZy3vJGujAfFRyZ5vGL37pw1KGHW9Ay40y39QmizldjLV0Cj5r_uMWMtTW3fFKE6ODb1qYbBUmyyjs9ilmuMOzvDHcZpoLKFudQmGDcZWpJL28X4zoNIWHHInqo6X57jJXuJeq2Z_PiKDPKUs9If1cjs46eCYK601oNiRBpCNigmWvpHjWFL1Vwg9t-N0cGTgFqk5dqY7GMUmw6yx78mRXQntdTi2Z3cFZ3ZF71foBoIN3zFNgL1BrcpHg62a1_TNAhkZe6ZjCRbJEWMdS5l4DIZTKXPfoeBoN9UdPvYImzi8BE99yFP4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b84f533728.mp4?token=bYIGy1LiwZoJ0TTbnqILA8QvkmK8sxlhbGkrN7KJXnzluDkq9g-YFCQ3E950OghaZbg1Mp2OCWFX57au-6qkFDKrgJ2vh-xe1SRKNoE7bMG6RGb6_at7DzNMS-POpOZHr5wCbNj4JiTB4VQ5kPvb6-fCIOYOScna_cgA1qTRitHuAEeoeqwmbmITvSQvevUePJVbj9PGOjxufbRoOtWRfj_DjN31DD4A8b24zkVTLCuFnwK5MWAZ4tFh0otBNgwOPkl-kEe9Btew_1t46e5md1pH-Ujd8oZ2pxu5zVGWwB7ZVwhj19oWzIK0bnsRJUFwLDjsESvmWxNfvvjRC0lNPS-hMjGqF8c3HzXfGNnqgVRh9VowM85R9PxZy3vJGujAfFRyZ5vGL37pw1KGHW9Ay40y39QmizldjLV0Cj5r_uMWMtTW3fFKE6ODb1qYbBUmyyjs9ilmuMOzvDHcZpoLKFudQmGDcZWpJL28X4zoNIWHHInqo6X57jJXuJeq2Z_PiKDPKUs9If1cjs46eCYK601oNiRBpCNigmWvpHjWFL1Vwg9t-N0cGTgFqk5dqY7GMUmw6yx78mRXQntdTi2Z3cFZ3ZF71foBoIN3zFNgL1BrcpHg62a1_TNAhkZe6ZjCRbJEWMdS5l4DIZTKXPfoeBoN9UdPvYImzi8BE99yFP4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این فقط روایتِ حمله به یک کارخانه نیست...!
🔹
روایتِ حمله به قلبِ صنعت فولاد ایران است.
به جایی که هزاران کارگر شریف ، زندگی، نان و آینده‌ی خانواده‌هایشان را در دلِ آتش و فولاد ساخته‌اند.
🔹
وقتی زیرساخت‌های فولاد خوزستان هدف حملات آمریکایی‌صهیونیستی قرار می‌گیرد، فقط آهن و ماشین‌آلات آسیب نمی‌بینند...
بلکه معیشت کارگران، توسعه‌ی کشور و امیدِ یک نسل هدف گرفته می‌شود.
🔹
اما این داستان، داستانِ سقوط نیست...
داستان آنهایی‌ست که از میان دود، از دلِ آوار و از میان خاکسترِ کوره‌ها دوباره می‌ایستند.
کارگرانی که باور دارند:شاید بتوان کارخانه را ویران کرد..اما اراده‌ی ساختن را هرگز.
✅
روابط عمومی شرکت فولاد خوزستان این اثر را به ساحت کلیه کارگران شریف و خستگی ناپذیر صنعت فولاد ایران علی الخصوص همکاران خود در گروه فولاد خوزستان که به حق جانفدای جبهه اقتصادی ایران عزیز هستند، پیشکش می نماید.
🎬
We Rise From Ash
📱
@khouzestan_steel_co</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/654843" target="_blank">📅 17:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654842">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
ادعای وال استریت ژورنال: ده‌ها نظامی اسرائیلی همچنان در امارات هستند
🔹
این نیروها در اوایل ماه مارس برای اداره و حفاظت از سامانه‌های گنبد آهنین که رژیم اسرائیل به این کشور فرستاده بود، اعزام شدند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/654842" target="_blank">📅 17:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654841">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/860b737f92.mp4?token=Y_4fWYh-qHkNUMZOnv9pKwBtKdTWGLj4o0dDPBlS2qDbVH9mhhan0rLVH775PyVfWSZdTZoeJhlczHRAXUEQA0uOlBqUZMXgdU5V3w7sY5yp9u6WdRIOFGpbXNq5ZuANlCnQ5EXh3oJUHt6hd5P08LX2FLR2h01VT1WpnLs9w0wfnKB9SUWhQJDQM9xbZHC4Xx5WK6vFoPi3x9dFcORg2TriZRB2KLxTkxjbhn48iv6XcwHmEj9szx2_IXv_FmLD8diDvXlFEtKkOi1B1IHphhDPTCSWE-EV15zUiVW6T4hgl9QRr99GL31xkkftm_wVBqT25J82REJfApHxA-ZxZlxyJnFib8JkWwcfCjH4NKmD3QfisAfJTi1xcAoNKknmL6O_2PPmoDF4yRHjmZ9Aa6lidNcQju2JnM9KJrzJPumUG7YR_NUMK4d-R9F8HyluuBzRNxJMfv3O5gjeCQImtESQxKsRxnHbcgTfcsROyu8H2TsuRZA2Y_sAAcN9odWYtuM_t3BMW4M5vLMkyQMB_YS8txuXDKZp77IO4pohh8jQ62T02NOfmH0tVVdDvBb_mzEcymNeZQRnITLIdAzWqgfD0SUEbq6yfFjjTo8N0b-munLnWCIjnDSlF3OdvhMXCtisM6XEHwCAXXu2qtrjqxMBKlycc2hhGcLakCBbLr0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/860b737f92.mp4?token=Y_4fWYh-qHkNUMZOnv9pKwBtKdTWGLj4o0dDPBlS2qDbVH9mhhan0rLVH775PyVfWSZdTZoeJhlczHRAXUEQA0uOlBqUZMXgdU5V3w7sY5yp9u6WdRIOFGpbXNq5ZuANlCnQ5EXh3oJUHt6hd5P08LX2FLR2h01VT1WpnLs9w0wfnKB9SUWhQJDQM9xbZHC4Xx5WK6vFoPi3x9dFcORg2TriZRB2KLxTkxjbhn48iv6XcwHmEj9szx2_IXv_FmLD8diDvXlFEtKkOi1B1IHphhDPTCSWE-EV15zUiVW6T4hgl9QRr99GL31xkkftm_wVBqT25J82REJfApHxA-ZxZlxyJnFib8JkWwcfCjH4NKmD3QfisAfJTi1xcAoNKknmL6O_2PPmoDF4yRHjmZ9Aa6lidNcQju2JnM9KJrzJPumUG7YR_NUMK4d-R9F8HyluuBzRNxJMfv3O5gjeCQImtESQxKsRxnHbcgTfcsROyu8H2TsuRZA2Y_sAAcN9odWYtuM_t3BMW4M5vLMkyQMB_YS8txuXDKZp77IO4pohh8jQ62T02NOfmH0tVVdDvBb_mzEcymNeZQRnITLIdAzWqgfD0SUEbq6yfFjjTo8N0b-munLnWCIjnDSlF3OdvhMXCtisM6XEHwCAXXu2qtrjqxMBKlycc2hhGcLakCBbLr0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این لابی‌ها مانع ارتباط مطلوب ایران و آمریکا می‌شوند!
🔹
در آمریکا لابی‌های پرقدرتی وجود دارد که اساس سیاست خارجی آنها را شکل می‌دهند. دو لابی به شدت قدرتمند که جنگ با ایران از دل همین‌ها طرح‌ریزی شد.
🔹
کدام لابی‌ها؟ ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/654841" target="_blank">📅 17:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654840">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2ieizoR4qkX9ntX9EthEyh3FxRk8MjhG1V-FMM2Mr56ivoetuTt1s_TLhKUApO6IUzp0cxx-8_ctDR62HcmLga_v0FkvB_GZs_sy3AtAQHL5yMKOH8bYttalKUFbuWhVo-9Ap24zm5vbr1B_Z29AN22XXIg2ob8Psrs8LLvdSA32OqL_tjaB7Us9gabiCY-DLU9O4vflHOURxa9jvBhmSjgVmNF2kIgs47tpSaQQx32Tb-YFwCvEjMxHACoJYtKZQ9f_LkGl1xD4q-eWPTZCZvBIlJ4T7aZNenh4vV5f85eC9Q1cDtbXmvQSCAEQ2kSzpxsaKcv8s_YNH82phecQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاهش ۸ درصدی ذخایر نفت جهان
🔹
آمارهای ثبت‌شده حاکی از آن است که ذخایر نفت جهان که در هفته‌های دهم تا دوازدهم سال جاری میلادی در قله حدودی ۲ میلیارد و ۷۸۰ میلیون بشکه قرار داشت، با یک شیب تند و بی‌وقفه در مسیر نزولی قرار گرفته است.
🔹
طی تنها ۱۰ هفته این ذخایر با خروج و مصرف بالغ بر ۲۲۰ میلیون بشکه، به سطح ۲ میلیارد و ۵۶۰ میلیون بشکه سقوط کرده‌اند. دنیا همچنان تشنه نفت است و تقاضای فزاینده جهانی برای جبران کمبود عرضه، با سرعت در حال بلعیدن ذخایر روی خشکی است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/654840" target="_blank">📅 17:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654839">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
با اعلام سازمان لیگ: باشگاه‌ها براساس جدول لیگ به آسیا معرفی می شوند
مدیرعامل پرسپولیس تا ریاست جمهوری هم رفت! اما پرسپولیس به آسیا نمی‌رود
دبیر سازمان لیگ:
🔹
ادامه مسابقات ممکن نبود، طبق قانون و عرف به جدول ثابت شده رجوع کردیم.
· پیمان حدادی، مدیرعامل پرسپولیس، تا نهاد ریاست جمهوری هم برای دفاع از حقوق باشگاه پیش رفت و با انتخاب پیشکسوتانی مثل محسن خلیلی، برای حفظ جایگاه باشگاه تلاش زیادی کرد.
🔹
اما پرسپولیس در رتبه ششم است، بنابراین نمی‌تواند به آسیا برود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/654839" target="_blank">📅 17:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654838">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvIJlxVSwv-XIaaZXq-hZiAiVnqSbJk-U3jbNuUQqBa-rpVtGTwKH7E0OYxTuMbKPoPRpUYoFjP90zmmMEDJ--gzhqF20cUjGgAZ7vpd0VBOdul54tyboR1L32RkeTlHJ4E9EGAeSjYTsEeabjXLakodjg5NQFfxaGRGrEgy-5lwYag8J4EnNH22pmVrIO_Vqmu5Pb35FKb50wC-vgzU0mTscUjKfsly_rTj4Npg1WGlDXipIk5Fa05ZtXSDYqUASm2RfbSiLzTa9SGw1nsJP6h1p1WQy8cXd5r_S_Kd5jNZWQkgrfyOdh67IVCEREuBiVhTCQAvQxtkr7YnRsYICA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسکن با دلار ارزانتر از ۹ سال پیش شد
🔹
میانگین نرخ دلاری هر متر مسکن در تهران از ابتدای سال ۱۴۰۵ به حدود ۱۱۰۰ دلار رسیده است. این شاخص از ابتدای سال ۱۳۹۵ حدود ۱۱۹۰ دلار بود. یعنی مسکن امروز به دلار آزاد، از ۹ سال پیش هم ارزانتر شده است.
🔹
در شرایط تورم شدید، مسکن همیشه پناهگاه امن سرمایه بوده و این تقاضای اضافی می‌تواند قیمت دلاری را بالا ببرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/654838" target="_blank">📅 17:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654837">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIFmuRuTpcFoR0jmISQtBDmxZoo2F6jlfidcMNsta_LQENhopTsTWV7BI_rMsSW7EnqJqt4eJ-j8y2FcN8UzIXaqiH6Gd2Sz8vcnTcmgegLG3mWock96x7ZNFAFBaHIbmHgA56Af_sC5UN_HFYcYbFT9Kr9a5TwKZ11tEttXZ1OfUCCm6gD192f2StJ4slLW_U3wvmtnKBZU_VJ3fWCOB9bOCQTbjR1l93G8w2Q--szGSHZDLG0kJSg3HtN_mHvgz3RIvQ3V4iTpmI-81WeqT1Cvma1bl7dSc_7IUhJRgtY6PbCZmb7W9tIy2Y4bb2pTOdJDWf2tfkY425t0KFzX0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین نقشه از وضعیت جنوب لبنان پس از تحولات نظامی اخیر
اسرائیل
🔹
زرد:
منطقه تحت کنترل ارتش اسرائیل در چارچوب خط زرد
🔹
قرمز:
منطقه‌ای که ارتش اسرائیل پس از آتش‌بس به تصرف درآورده است
🔹
نارنجی:
منطقه‌ای که تحت تهدید و حملات ارتش اسرائیل است اما نیروهای زمینی به آن نرسیده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/654837" target="_blank">📅 17:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654836">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
در کشور آنفلوآنزا شیوع پیدا کرده؟
قباد مرادی، رئیس مرکز بیماری‌های واگیر وزارت بهداشت در
#گفتگو
با خبرفوری:
🔹
شیوع علائم عفونت‌های تنفسی تا ۲ خرداد در مراجعین سرپایی ۵٪ و در بستری‌ها ۷٪ گزارش شده است.
🔹
در میان افراد دارای علائم تنفسی، حدود ۸٪ مبتلا به آنفلوانزا هستند و ویروس غالب در گردش آنفلوانزای نوع B است.
🔹
طبق داده‌های نظام مراقبت، آنفلوانزای نوع B در گردش شدت یا تابلوی بالینی غیرطبیعی نسبت به حالت مورد انتظار ندارد.
🔹
برخلاف پیک قبلی که نوع A بیشتر کودکان را درگیر کرده بود، این بار درگیری بیشتر در بزرگسالان دیده می‌شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/654836" target="_blank">📅 17:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654835">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tk3UWEMad2Wsx1iwhNv_x4rdpSAfjNPdskxktav8sVZB6OGMpJhUjqorkZPtTcQTYSvZjsMVhgbJ-mggh4XnhUh-Ti_Xg9TQgvHdpWfXCGXYqR5jMCxpoV1kWlzbtBlle74TJFeUaS8Zq76QU-lasLlU4R-svGjEaCtuAUVubFzhyJoCGJMcv8z1R_755MEU71wQgVwSZcoUT2q95E1mRHRB4B7KNGO52ndebHB_PmWexonUZZF63J-5_egg5ls4155K5Os_Qm2n-5I2dMU5XlmngJamKeaAL1Eb3c06dfyL3-zKp546I-gAHtf9aBzlg3tpQMgWzw06AtkrIE78jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عمان از مشاهدۀ یک مین دریایی در غرب تنگۀ هرمز خبر داد
مرکز امنیت دریایی عمان:
🔹
درپی مشاهده یک شیء شناور مشکوک به مین دریایی در غرب مسیر تردد ساحلی کشتی‌ها در تنگۀ هرمز و در آب‌های سرزمینی عمان، از تمامی دریانوردان، ماهیگیران و شناورها درخواست می‌شود با نهایت احتیاط در این منطقه تردد کنند.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/654835" target="_blank">📅 16:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654834">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
گندم ایرانی قاچاق شد
یک منبع آگاه:
🔹
گندم کشاورزان در بازار عراق به قیمت کیلویی ۸۰ هزار تومان فروخته می‌شود؛ یعنی ۳۲ هزار تومان بالاتر از نرخ تضمینی. این اتفاق در شرایطی رخ داده که کشاورزان از فروردین‌ماه تاکنون ۱.۸ میلیون تن گندم را به سیلوهای دولتی تحویل داده‌اند، اما به گفته آن‌ها هنوز ریالی دریافت نکرده‌اند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/654834" target="_blank">📅 16:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654833">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
افشاگری تازه بلومبرگ از تلفات نیروهای آمریکا در حمله اخیر ایران
بلومبرگ:
🔹
در جریان حمله اخیر ایران به یک پایگاه نظامی در کویت که در واکنش به نقض آتش‌بس از سوی نیروهای آمریکا صورت گرفت، چند نظامی آمریکایی زخمی شدند و ۲ فروند پهپاد ام‌کیو ۹ ریپر نیز آسیب دید.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/654833" target="_blank">📅 16:44 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
