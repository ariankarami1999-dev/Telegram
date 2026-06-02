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
<img src="https://cdn4.telesco.pe/file/FGjqPcU8YOWPvUzC2BW673iYimNRvn0NOiupHOmJ0VpygdazpHf1X-CNjmVvhp29kZ6UhZAqNI4EGTLMYNoFg3CxRmE02N6yPWXbX7GNHUSNs5EAnd9IScbpvstDp5DMjqjGIQ6d0N0bYNSMBt5l7ShhXiTYrcK3O090dWM8Jc6mu67GT__Uzh4V81wAqMcNRiJyXp17GyChvYyzRWLkPVeneeC99Zha4hcjmUoK4N9x7bVFtO0eLozhpZR9nwfFrwethXCDjO_-Dw1P4i8ZQugeRf1iaD9DPe7pp-1kJAqzqfi7oXoMwu3sPefIMacQf4NzA3ky-2h1Gax_s_o1Qw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 13:15:45</div>
<hr>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flmsoJJ9lkcp98hsmgYyz1Cq4iH-1gUuYD5eC1-GUdE7_3SvX9P6uLsK5SduEske3uPgzk0fK9Mj6WFhMABIjSiku098T8aKjQColm16Y7UyYwpOS0vwrb9wmgEpxFaECHGS_CfjdOZJyP5uyLPHjzybu9JbU4WRQ6lC2_2PMn1OG0ORP3AhJEVwpKlL35Kza0jMipXb2RddSbbMLpIVw5HS4o0792UhitYBHrgtBLbQU1jqOQtUOJSNLNuRO7GZAfUtFfs7vf_S65OKBLQpcDNqviu2MKRTrp1zGt6qio-MgzZ_a-lgpdKzZHFi1iNWFZdB-3JsNOaOjLPzd_OJcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k1nyaWc_y_tHnytXZe9Xzxfneo6UDlI_VeZBZj42wnDYoVz4UpiPDLXwDqwickG9TfjpYR5vjfgMuSiMUuQBHcekoP41dW59-PnD4nEtaj6Mq4VQF6iOdW7T9785EyODkXtA4Xg7rFVaOLoYXEd8HU3a0F3Pm-X1fbp6ISjKobmZENjTT440azKiL2Hq5j6DOVHabI76HGWSyE7xlura2sU6SkVgb8jK7Ef8rMeW0KssSrI2T2ta3rsihD7SzH4gKrvXxkoy2NPxHq5h8MoFFaejWJRX8javc-mMpxniCl1DAmfI9fjniwY1b1fBCd8w-5WPUtJy1jyssom9NxIvWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XeXxdLrRNMz1usORlDK1iffYbnOKusK1UdrKaKSSacPSKONLcPP676WMgEG8feTQBh3FTTIab4vwfyeBeo4QBwnYlid9-ZrtSKPnIAaCBNd6cYLruyQ3TjvXrK_GE0j1Czdb03xhESpT22Covzbi3CQB1Y47o1jhP8TONk5-gXyB92E7GhqmVJqzpeB4e0wc5QaqYcYeJOl4s97nNZ_lYT8Cq3EKBg7pIfToAnb4-32o7-d4oV-ku1-PQM99_3xWdBHenbKQmsVgqVpPPbrROWxraP64sLY99yiQDEcwproE6AsQqrcLfVIkEgnV7qz-5yOr6lCrfGMg7PRtN9ZDOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uhtJ2jYjj_8eiWbstmWo4cDW7WzZoXowYNP5dgg7P5DlDkEDOXVJ0O5M_XltkgtKihGV5pyMU0ATM21n1SybU8g6wz12OHHgMFs7ZqLqbOTwNbVXz7Mh_Tagd4-EP8Gh0Ruo4RtkgyAxuSUODOzw2TL3Q9LYY6TgTF1fPR4AIjWl6OUqcLW-aThKZpbR_NAvKPJR_VS3dvgsT2AZakmqVPBDyg_TDkz5aWSwCJkdnHkgcE8zVisriZ5DMvSfeEDdkHwwdMFLQQDjongX1-BvCVdsk53Lf--5pIW7T9aXRwe0IQZoIDsHCbBVsZdCNPikV_4jjgyxZe5xl1y_Tz7GEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l5ctTG4wQkKzMfWcMvAx5Alf5vkLuGNPFDf-UNYAnDrm_hRTBH1ftSdkah_-c_meAdamc59n96rd9qfu7r4_D06EFI7Gw_EBZkjOkugkdsx3ItsX0f4j51taWlj3uOuk4hrP9WeLXH9wZUObXy0mi6DpbYXp6S57LAcIMyCGmlL04CX-DtyJzUMiqHV7ASI31A3HHfVp4L7UM-KeMN2tK-_dEOwBwM8jnBuj7EJ-rw89e3J6vh95m-gZmnh9nGzfvAgiejmW_EFUDb29BK5sqQpfMvTTtQPdfQj_pubXnx06puYNQ8fqDPq1agzZnMHIbozTG4qnKhIfC1RaFHBnEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">و بعله! خامنه‌ای و پسرهاش
خیلی ساده زیست «بودن»!
فقط در زمان رهبری خامنه‌ای، برای خمینی مقبره‌ای ساخته شد که هیچ کدام
از اهرام فرعون‌های مصر،
حتی فرعون‌های مصر!
به این  هزینه و گرانبهایی ساخته نبودن و نیستن!
این فقط و فقط «یک قلم»! از ولخرجی
اینها از اموال ملت ایران بود!
در کشوری که هزاران مدرسه‌اش توالت نداره!</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/farahmand_alipour/5252" target="_blank">📅 12:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=k5XMzNxXoKxL5FjSE1ku02JvcZF9GXOO3EukrVWV_7z0qxK-zgbMrGAQuw242-7S6-YbnPE9aU_wKEu6JbWFxP2CHZER6xoincWc6t2hyWN5G-NDNxEH4GAaSiMhI78DDGcwpYhf2zQ0evVX-9_ss-g9PTSe0--Hi1T-81DXCKnd4XhsKnr6CKv-avhga3BQr3r5V0ZCuXYwrPc73Qh8JKOPK9S151A0M7lhyzO72QeaRKCjch1j-vDAHwZ2AboUqPTuDBA4M7wRAsID2HFvMWo_3sHd7bb3a7q-ZkYYzfG-W9lqc7PP_CY6EUIuKAohOJibVPCggfHIqqxd1hIdog7QAeGtqn_rPH6_qXwl1_b38hq3jceC94Ys2DIr6W5vQCb00xiBX6LKNnVEox6z4XY8Qn4w4CUUCcSxfD1hGhNjEtlJFWO0cKs_bZfdEAOg9GdFgI3nPIB0cfnq5M3JVcI4ZHXTe2YDPpoSZ-xw06rFDxC9ltFz48pbu6G6NDbRCGeLSuw7YqCcvsAxuW0YrEnflsW62Lq_0fPXMSaEZRUBY8ses6Q2sk2dr3Pe57ODjSyyqCgobWYJFuDV8nq0wOilRgKA_i5u0i_mv4k1knr9RodhKxnhT0rLGgW2oSMQSiy_rYBlhF6WKSMDITHe-6WykEUTqRYbd-KYVzsKpWk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=k5XMzNxXoKxL5FjSE1ku02JvcZF9GXOO3EukrVWV_7z0qxK-zgbMrGAQuw242-7S6-YbnPE9aU_wKEu6JbWFxP2CHZER6xoincWc6t2hyWN5G-NDNxEH4GAaSiMhI78DDGcwpYhf2zQ0evVX-9_ss-g9PTSe0--Hi1T-81DXCKnd4XhsKnr6CKv-avhga3BQr3r5V0ZCuXYwrPc73Qh8JKOPK9S151A0M7lhyzO72QeaRKCjch1j-vDAHwZ2AboUqPTuDBA4M7wRAsID2HFvMWo_3sHd7bb3a7q-ZkYYzfG-W9lqc7PP_CY6EUIuKAohOJibVPCggfHIqqxd1hIdog7QAeGtqn_rPH6_qXwl1_b38hq3jceC94Ys2DIr6W5vQCb00xiBX6LKNnVEox6z4XY8Qn4w4CUUCcSxfD1hGhNjEtlJFWO0cKs_bZfdEAOg9GdFgI3nPIB0cfnq5M3JVcI4ZHXTe2YDPpoSZ-xw06rFDxC9ltFz48pbu6G6NDbRCGeLSuw7YqCcvsAxuW0YrEnflsW62Lq_0fPXMSaEZRUBY8ses6Q2sk2dr3Pe57ODjSyyqCgobWYJFuDV8nq0wOilRgKA_i5u0i_mv4k1knr9RodhKxnhT0rLGgW2oSMQSiy_rYBlhF6WKSMDITHe-6WykEUTqRYbd-KYVzsKpWk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=oTC67vHCJiJkXI5KKYB8O9S5m2pSCVJ-_DmJdEjzg1cRz3VBbGJ_GaGZXVCa1zHAi72SrE9e2hsiK6HgmhogScQDZO7EYgryS7jZnUg0No0skL644ZTF8E9D8-X-AUVBwOgp2msRe0ojS8Y_vbiasLihLNWWJgSpU4GwYVpIfFgqwRD7GSumAYVY6OJBs6tuhm81W-XKm9IgqdjmRwNeK_4e8vcJeIWRJ6UkY8TbRqNW37xzaPR1rehpwrRXbMOaoWAlEBR4Q497ZSWtW8IrBRoH4oieh6yz3-48JTTttC_CuoEw1n7YBxDv11x2ykca-lHEK2BioOFvYUdY-iX4zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=oTC67vHCJiJkXI5KKYB8O9S5m2pSCVJ-_DmJdEjzg1cRz3VBbGJ_GaGZXVCa1zHAi72SrE9e2hsiK6HgmhogScQDZO7EYgryS7jZnUg0No0skL644ZTF8E9D8-X-AUVBwOgp2msRe0ojS8Y_vbiasLihLNWWJgSpU4GwYVpIfFgqwRD7GSumAYVY6OJBs6tuhm81W-XKm9IgqdjmRwNeK_4e8vcJeIWRJ6UkY8TbRqNW37xzaPR1rehpwrRXbMOaoWAlEBR4Q497ZSWtW8IrBRoH4oieh6yz3-48JTTttC_CuoEw1n7YBxDv11x2ykca-lHEK2BioOFvYUdY-iX4zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی
از فعل گذشته برای مجتبی خامنه‌ای
استفاده میکنه.
مجری : رهبر جدیدمون آیت الله آقا سید فلان!
حداد عادل :
ایشون از آقا سختگیرتر «
بود
» !</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farahmand_alipour/5250" target="_blank">📅 12:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoQwPKY0GMayoDIB_z3m4ikzgkkesTNaNYW5Ai442AgqpMSkyVkUctP89CkXBa62psNw6h3J51bWkj6QkiVUCToli0flnp3F1uVyyDRImwTr7WSu5RuykDVui72yGrPLeM_B3IbOdvzFXr-o0Z8sHe_wZ62PGx4Hxwpg7bvviGnKDoFKMtARqRQPeFsqls1lafUr6-cYl4szGWmosE4eB7xeCNrGatHGDe6hD2uuG4kgW-2vP_APiWszUt2yh3Id8i-s23wTl4mn4qiUAHNk0rWNndgXtnDjTM-22eTsk93AFsemhiw33FZo3Sa-mx0a9lPxbb2NdSuHaBnbrQeOCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف گفته که اگر حملات اسرائیل
به لبنان ادامه پیدا کنه، در مقابل
اسرائیل خواهند ایستاد
‌ و «زنده باد دفاع از سرزمین مادری»!!
میخوان وارد جنگ بشن
برای دفاع از سرزمین مادری!
حزب‌الله برای چی وارد جنگ با اسرائیل شد؟
برای خونخواهی خامنه‌ای! که
هیچ ربطی به لبنان و سرزمین لبنان نداشت!
اینها فقط برای فرقه خودشون میجنگن!
نه ایران و نه لبنان!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5249" target="_blank">📅 01:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">قالیباف در گفتگو با نبیه بری (چهره شاخص شیعه لبنان و رئیس پارلمان):
«جان ما و شما یکی است و پیوند ج.ا و لبنان ناگسستنی است.
در دو روز گذشته، ما به طور جدی توقف حملات اسرائیل را دنبال کرده‌ایم. اگر جنایات ادامه یابد، نه تنها روند مذاکرات را متوقف خواهیم کرد، بلکه در مقابل اسرائیل نیز خواهیم ایستاد.
ما مصمم به برقراری آتش‌بس در سراسر لبنان، به ویژه در جنوب این کشور هستیم.
اگر توافقی برای پایان جنگ بین ج.ا و آمریکا حاصل شود، شامل توقف حملات در همه جبهه‌ها، به ویژه لبنان، خواهد بود.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5248" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
به رغم گزارش و خبر ترامپ : حزب‌الله لبنان چند راکت به شمال اسرائیل شلیک کرد.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5247" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بیانیه سفارت لبنان در واشنگتن در خصوص توافق
بر
سر
آتش‌بس
متقابل
:
حزب‌الله با پیشنهاد آمریکا برای توقف متقابل حملات موافقت کرده است؛ به این صورت که حملات اسرائیل به ضاحیه بیروت متوقف شود و در مقابل، حزب‌الله نیز حمله‌ای علیه اسرائیل انجام ندهد.
اسرائیل به ضاحیه در بیروت حمله نکنه
حزب‌الله به اسرائیل!
یعنی : اسرائیل می‌تونه به حملاتش در جنوب لبنان ادامه بده، اما حزب‌الله نمی‌تونه به اسرائیل حمله کنه !</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5246" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
ترامپ :
«من تماس بسیار سازنده‌ای با نتانیاهو داشتم.  هیچ نیروی نظامی به بیروت اعزام نخواهد شد و تمام نیروهایی که در راه بودند، همین حالا بازگردانده شده‌اند. همچنین، از طریق نمایندگان عالی‌رتبه، تماس بسیار خوبی با حزب‌الله داشتم و آن‌ها موافقت کردند که تمام تیراندازی‌ها متوقف شود؛ یعنی نه اسرائیل به آن‌ها حمله خواهد کرد و نه آن‌ها به اسرائیل حمله می‌کنند.»
🔺
ادعاهای ترامپ شبیه برخی ادعاهاش در خصوص ایرانه.
اساسا اسرائیل قصدی برای ارسال نیرو به بیروت نداشت! بلکه نیروهاش در جنوب لبنان هستن!
🔺
دوم : بر اساس قرارداد آتش‌بس اسرائیل قرار بود که به بیروت حمله نکنه! ولی داره حمله میکنه
و در نوشته ترامپ هم اشاره نشده
به حملات هوایی اسرائیل به بیروت!
گفته : نیروی زمینی به سمت بیروت نره و برگشت کرده و…!
گویی ترامپ دست اسرائیل رو باز کرده که به‌ حملات هوایی‌اش به بیروت ادامه بده و به پیشروی‌اش در جنوب لبنان ادامه بده.
همزمان گفته بله من مانع شدن‌ نیروی زمینی ارتش اسرائیل به بیروت بره!
🔺
سوم:  ترامپ گفته با نماینده های حزب‌الله در تماس بوده و… عجیبه! بعیده!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5245" target="_blank">📅 21:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTKFRwykCe81o0z4NmeRxflVSlrkwvG5iWbiUGdDBPhbT92MhhfM7x0Er5dNuOYIneXXc5Ios1I6nU_rkaRwzdAVv38g74lMfYj1JvUZQvj-yogTnLbcW75yN37v9RZMwbsc-f4AaCXFqspzRNOw0qTelLmM4D4OBaQ0yo1WXfpFNYS6GaXRFY4lWfdrROYT1vDaPrRs_YnJlFtbN-nyfCEx6Dxia5cAac_zdz7eKF7aAJ9afMcNtQe_ipV3D3clXO3rNc9Y6sz3PMZ9J5htKnsCfgyWIsKcyM4GgCtG3mXRwdOZDvk3T-_LHTtOJL-Yp8FDr6mJR1MKeakFE7rCbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه جمهوری اسلامی اسرائیل رو متهم میکنه به «نقض حاکمیت ملی لبنان»
یادآوری :
دولت لبنان سفیر جمهوری اسلامی
رو اخراج کرده و گفته مسبب این جنگ جمهوری اسلامی است اما سفیر ج‌ا
لبنان رو ترک نکرد.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5244" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5243" target="_blank">📅 21:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1t3qGLXPPYSYQDKG3Ik_NSEHVIvqehPanKbmwfRFvjKms45b_cYe95iHq8zzrNfcaTyrmQkPAt3hu72Agg7rlkfA-acs8cTMZlHBf2JQHFgB8yKMeXq7xjFtC7qMMus8KuJeD9BMY8m0QrCGbXkj-aL0ANUahM0nprOWmvmUMBinywR-dSjHGXheDV9ZpOTdbCoyDf7hPoJjxvqeMIS_yv-ZYhnwM6tT7T5TkWrruCCSAaEiI6Kd2kzh_gPFFrB9nEUFo-JnGX9Z6nJbHy3fdHaAQlp6eK0jEFwRrhPjLdjD2UlJWEtrHValaJ03AzpklYAK8fHtjylOXWJOfBl2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qolsH6FJvRRzcI6L-9qb0zFud1_weD0X_OVRMbq_g58h2YNPzV9nAtyEpaK05LnG9zvbXcY-vItP-MWkBnX4fAo5lvhgV-shA4egWgNM0eNg5q1u4d6h094rU_LGUu-YJQAEAfNfLcku-uS3Rb86qDBWWDiY1t9UVpZ6e_XJa3WtzdDFJSLJxREenm3U5556OF5WaW6pJuwX2eWJf6O31D8wR3U08En3USm81BzJZzpk2qf08Z1WryjJzkGjJ5tMNGpPDRgWmdf0JnIM0ezFCw7XkjLcdUocKX0bQNZqwabFfsOEQQlZUSd2zdN1qy9Ew7ut_NFErYfNExtvj3UFzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lmtbipq5iTdA_OMWYYaf8NHjMIAekO2qYldJFEGacpxvUDQcg1JVl2_fYSCUpByxMhC4jFBqg2Dli-t5lNnGX_k957cfOjEqHHsWkafOHkwND-7tbvW-ANkZ_JDmThEQyc3kj17TTdDFv7R_hTR3QCGZNlExN3PSukWGULKHIYGQFlC15q61LM1uBc_iY95wQrsyK9_CYYLshItyPO-0LuZ1hLd3RYB4iWC_cdq7KmxceCqlMay36yCfBGYcyekkqbQ2WFKt937owkM-vR-dVovNRbz0yPvdrZPDZazq39LV_9DWKpg_hjEHH061RYrB6rf9aCjwqYrup4h9m3q3GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه خب ! اینها «وطن پرست» هستند
دغدغه‌شون «جمهوری اسلامی» نیست!
حفظ «ایرانه» و بحث «وطنه»!
فقط اولویت نخستشون
گروه تروریستی حزب‌الله لبنانه!
و توی مصاحبه‌هاشون هم میگن حاضریم ایران به خاطر حزب‌الله موشک بخوره!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5240" target="_blank">📅 20:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5239" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRxQ3GL7Rr_iQ31_xBU6WKXq77WPnD2KVBpPWidBnZ3-_bZ0BCutmvCjfcTPcDa0sn17yredtD8LOLYs86bjnNGcnnqToFZQjQdG79tqZMzF5kblA9e9BUZPSSMnXEFruUTXI9WPOoE3-lMXmWNviSXAWIdCaa3v4MkvkIacEEohf9GcUBp7WoWUhsrkfZIwV2oeewA1IrXjloYlEnv1bDw0n-2Z9Lj1syRJSRSREomGAzukEOamqWpwbKpj2CkCoGE0YYL9wO6UGBlg0buxVYj2B7t1ko814onRaf-Ae6xeOTd4m5k6nwzwl0C_8xb3MN4tW_kmMjxXqOL28N47uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتابهای اسلامی برای کودکان
(در مصر و تونس و….)</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5238" target="_blank">📅 17:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">این دو سال رو یک مدلی با ترامپ راه بیاییم و بعدش بزنیم زیر قرارداد!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5237" target="_blank">📅 15:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRDISfWdhFTcQ6zutISdPGBmHwvYeyOEil6XtRQL1PXdOnI_-ftnJZCCd9aZihz0TsG71O8CtTUKbr_SJQnympxndG5pmCybMQUVw8kn8GlYayJ4Rf9eeQcK1bSHDF50jUzp7L4jKYhKks86BS7TqTfi4KCUp1o0mxpKWHZT0CTvNQubVnXPUtvdWmznTwfTPXobGtF16zPsxawC4kdCRtk6bDtu3EAmk7uaSY83gXwVbbbKhbggu3y8x3FE6-dZUOrEsfWn8uZBuA7IEqXMHvgxz_b0NDIjV6lJi8HFg7JA9a13_xkfx64rGsvrY2F-w3gVRIiUS6NPgwLv09ffCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نتانیاهو دستور حمله به ضاحیه (بخش شیعه‌نشینِ بیروت) را صادر کرد.
🚨
بلافاصله پس از انتشار بیانیه نتانیاهو، پهپادهای اسرائیلی در ارتفاع پایین بر فراز ضاحیه به پرواز درآمدند و خیابان‌های خروجی این منطقه بند آمد؛ هزاران تن از ساکنان ضاحیه که پس از آتش‌بس نسبی به خانه‌های خود بازگشته بودند، دوباره در حال فرار از منطقه هستند.
🔺
نتانیاهو دیشب نیز در دستوری به ارتش اسرائیل خواستار  عمیق‌تر شدن و گسترده‌تر شدن عملیات زمینی ارتش اسرائیل شده بود.
باید دید واکنش جمهوری اسلامی چه خواهد بود.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5236" target="_blank">📅 15:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WmoBdfJ3Eps7x7Up04Dk98WrE6w24RofCeMmBpfN_mLWfCSBOI2S34keQkt7jmKx85mjChOdDhSnfe-GYhaCpdOc8z1VcKBjyKEhFJjWLlEllrs7veRRMEiY-dv-a0vU4XaMpKDR0rmaPiAM1-jof2TL_IkwxdfLdZF7pd9TSzcWL3t893EZ2r6Z_JmmibfspU02tOKehoWqpeRm4i4ObLOYAzjS-0zJj05tiKmv-oLLt_wwrTb1rk2xYanTvC5jDPVTlycaUoS17QcJvuKM1x1BemauNP0h3am225WlxLUn4mJC-zlfVaCrxKnZOpC33OJ31O3sV5gLyM5ZJdiZXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jdo3C-aUBNy2EQh2ybAzt69PdBhsCa3piHHPiO2kHMTTUDWT2k50xVHoksZ5Qvp51BtWDFUTgnRS_jI1sB74NHwIgpX0UVvX0_55jfHBXomi_frzujIxvW-ZUN76GVsTfbOPq5AZTt9CX2EznxiBjNY1RS0Lm5YoAPCwRaDL6Ay7GG8aRAb9HMOOAEVQLU8l33a1Zsu2t8ncONXu5PJE81RyPWYkFULnzZb7SmPhZZqK1Jo9rqYrUYbIL7pjf3l9xE-L8M11d3wEuAqo793cFyY2jKX54g1JcwyPvlv5Vj0x-cYPyKcnOkDwsigFwVMj8fEmxIlvSqYaWpJQkItAXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=PrC-TVDFGUz1J6MPNTm-n_sIu3PMvqVcsYXVxLrW80OtNDoBOEvfE0L1IQE-4_4pvx6LCoMrzjQjcredSS1h--336ZkfmUu3Ayn_HM9kWePN012iYAb2dLGzDQegM7z4PnBx3eKrcEo5wHWqtbgE0rwsprUUqSusskfqks9tPeuoD1y2uJHUHZf80pZHdo5Wbb7BA3KF06ffsEptfbyIk9MS8Fk3Y2daJ8haqjTjKV_T_sMqNxRLDgw1H4IFR8-_kzI9BpxS5O-wh7D9deaLCSmL61KRMjPkoZg_Zzn4EVt6G10uJX2N7zpmPmux7Z4efXPC_NZ3RiL9CD4hTiRPYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=PrC-TVDFGUz1J6MPNTm-n_sIu3PMvqVcsYXVxLrW80OtNDoBOEvfE0L1IQE-4_4pvx6LCoMrzjQjcredSS1h--336ZkfmUu3Ayn_HM9kWePN012iYAb2dLGzDQegM7z4PnBx3eKrcEo5wHWqtbgE0rwsprUUqSusskfqks9tPeuoD1y2uJHUHZf80pZHdo5Wbb7BA3KF06ffsEptfbyIk9MS8Fk3Y2daJ8haqjTjKV_T_sMqNxRLDgw1H4IFR8-_kzI9BpxS5O-wh7D9deaLCSmL61KRMjPkoZg_Zzn4EVt6G10uJX2N7zpmPmux7Z4efXPC_NZ3RiL9CD4hTiRPYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال «پاریسن ژرمن» قهرمان شد و پاریس و فرانسه رو به آتش کشیدن
قیافه‌هاشون که تابلوئه!
توی یکی از ویدئوها شعار الله اکبر هم‌ میدن!!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5232" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.
پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5231" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfCsU5Q6Y9V5TadEeCKt5hTLa6wDeaMDBNJ4E73qbASVk58KP1X3wMGT7l3WO7Uxtg_E7l3Kee5N8k_EMWzr_Uqr7lgKeTq11nGj-X7mf76T0GU3j0HjxpFIVJfYO4mraQqyNL-J6vdH8Dzk8-4gvd3vI7shxlpUrhxnKJMBxzhD3zpJCRn_7H512gvY99n7CEMA8mhZPFAAipFvRp9QCEiw_TEFEDdcf2c5kCp93aJRB9E4VZpP2f5cdxHMbsez7_TYpPAzqctCnB1V0qBx4R6ByopGXqmT4CkzHoVb95HM8zi4GWzUrfMlNqAUj0G5wjUkRpMjzc6VPXDegWpyMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش آمریکا رسما اعلام کرده
که چند حمله در دو روز اخیر به قشم
و گورک در نزدیکی تنگه هرمز انجام داده!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5230" target="_blank">📅 11:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=tpVK8YXpyC0VX4o_1MxVnvvEj_y9kBZe_o3n75E9MouI-iIHRdsA2Fw6dNlRrmC5XGn6bni_mROp8dJQ_oqD3LEtsn2ffehAdc82ixb_ssmaAoWO35jrWgySJszc8zT1X9PiaX55mKip27Xt7FJulOCN2CAZIrLDKECljAPW5sA6mTtLvHlOf1-wRruAkLb7p4kh-sfJbtBDyP-g37_3Zf60UilUSt9jMIEWeb1Msnvbs4BgJCcIZBahb8MsOvEiK1hII3tgwj-onA7JJFT05vJ1wi-Qgbd9YJsZe1H3rComM4BxtP3C6dcfLcuhvFNd5EHGas-PjljPkqQgRKImJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=tpVK8YXpyC0VX4o_1MxVnvvEj_y9kBZe_o3n75E9MouI-iIHRdsA2Fw6dNlRrmC5XGn6bni_mROp8dJQ_oqD3LEtsn2ffehAdc82ixb_ssmaAoWO35jrWgySJszc8zT1X9PiaX55mKip27Xt7FJulOCN2CAZIrLDKECljAPW5sA6mTtLvHlOf1-wRruAkLb7p4kh-sfJbtBDyP-g37_3Zf60UilUSt9jMIEWeb1Msnvbs4BgJCcIZBahb8MsOvEiK1hII3tgwj-onA7JJFT05vJ1wi-Qgbd9YJsZe1H3rComM4BxtP3C6dcfLcuhvFNd5EHGas-PjljPkqQgRKImJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=ebB3IfNDNkZ9x510kNh7cAgpJsgVXGBGNEeAFNu5YP-u6D8YDgg2UzfIz89nymCSCyPwgjRIj-AQqKK0TEiSrk_RFFYGJDvwm9iZV05v-7hSoYCkTJNXKJyinC7YIVvIs98Idh10a_br2y-Hj_p7zugtXqQl8nvrMM4JDNIzeowB_EIzKmcNwf8-z3WS4q9MkVGhopG3YxwWGIaRlQF6u1VEdS2FoKRNNCOfAlMHcGmS8L8Kt_G8BgypD63WwoYmCtJsYlEuTPS_HfH27trnjTQvLdyVUqllzHgBzYQ88xbTNFFR8XQbSx8wK9Xly-xv1M_qfiDqkLxdVYQNwprE7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=ebB3IfNDNkZ9x510kNh7cAgpJsgVXGBGNEeAFNu5YP-u6D8YDgg2UzfIz89nymCSCyPwgjRIj-AQqKK0TEiSrk_RFFYGJDvwm9iZV05v-7hSoYCkTJNXKJyinC7YIVvIs98Idh10a_br2y-Hj_p7zugtXqQl8nvrMM4JDNIzeowB_EIzKmcNwf8-z3WS4q9MkVGhopG3YxwWGIaRlQF6u1VEdS2FoKRNNCOfAlMHcGmS8L8Kt_G8BgypD63WwoYmCtJsYlEuTPS_HfH27trnjTQvLdyVUqllzHgBzYQ88xbTNFFR8XQbSx8wK9Xly-xv1M_qfiDqkLxdVYQNwprE7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما  از دولت لبنان خواسته بودن  که برای آتش‌بس، مذاکره نکنه و…..! به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره (که بعد بگن دیدید،…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5228" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlQsEiLpb2jOTt8nVE8Jo-raxtYUJ8BFA9hoeZCHQtEx0Xh-D79Tri8qySB3_Nr1OFlfYJ0aq1x0H7G0lakaoj7OIl_-Ot9R1AoIWb1bI-aQFrWwf44gtgUziF1SM1YpOP7VNQiePwIWt8qdjnJdH62RNbF9Kjr1wGmYQMOge-wx01wbVV2LgvVLwjwtzAqu8tf9mwcFsXEmhEbYzUGZz91GXrzYf4saLz8lYYoVJGq4p15mMOfDvWmSofAoe8UNfdUjLVx00S_bu-ql5UPMWdwAGB-RJQApyqxWgT_n2xvRaoLEg6BJQtzWvIIVJzWf1Pfw--GAsS5A-bPyfZHbtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما
از دولت لبنان خواسته بودن
که برای آتش‌بس، مذاکره نکنه و…..!
به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره
(که بعد بگن دیدید، همون کشوری که به ما پول و اسلحه و….. میده، آتش‌بس رو هم آورد؟)
ولی الان می‌بینن جمهوری اسلامی توان چنین کاری رو نداره!
ترامپ اساسا داره لفتش میده و سرزمین‌های تحت کنترل حزب‌الله هم داره می‌افته دست اسرائیل پ یک میلیون نفرشون هم آواره شدن!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5227" target="_blank">📅 11:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5226">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.  به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.، مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!  یا شهر‌ نجف!  برخی…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5226" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=TMBGA-UAhuhANp1HvJ6rOEtXwCebmDX-YSlr9Fxd54TxeHC0PdftH7HPaHWt2OdEjVIJjcGAlPsTm-QOCx0xN3GpTxu5-xYfa6DN8hV8w5Qx1zcrAd8jDU2gYyOhbMBycj4XT_RzqfWCtZhk7BQJptTnjddPz4ydd8-vHdhVUH8wyfibbRoPYFWg8uNfdKD4ZI0AsuOsGkye2J7guaBEeDr_mpYfyJCKMowb-rOvznsuX6ZubdMqRgTDLNiErvRx424vsTcu8UmmysuTSzxrwa2rbHVB00U4SLankBbEWS_zbrYfmwGlmmuQiHf9FI30AXhRXgpRemquPRUWiRc6lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=TMBGA-UAhuhANp1HvJ6rOEtXwCebmDX-YSlr9Fxd54TxeHC0PdftH7HPaHWt2OdEjVIJjcGAlPsTm-QOCx0xN3GpTxu5-xYfa6DN8hV8w5Qx1zcrAd8jDU2gYyOhbMBycj4XT_RzqfWCtZhk7BQJptTnjddPz4ydd8-vHdhVUH8wyfibbRoPYFWg8uNfdKD4ZI0AsuOsGkye2J7guaBEeDr_mpYfyJCKMowb-rOvznsuX6ZubdMqRgTDLNiErvRx424vsTcu8UmmysuTSzxrwa2rbHVB00U4SLankBbEWS_zbrYfmwGlmmuQiHf9FI30AXhRXgpRemquPRUWiRc6lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.
به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.،
مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!
یا شهر‌ نجف!
برخی از شهرها را اساسا به صورت شهرهای پادگانی عربی در وسط مناطق فارسی زبان و ایرانی ساختند،
پادگان شهرهایی چون : بصره و کوفه!
در قم اینقدر عرب ساکن کردند (از قبایل یمنی اشعری و از کوفه)  که برای چند قرن یک شهر با هویت عربی بود!
اصفهان اغلب یهودی بودند، یک شهر تجاری، عربها حتی بهش میگفتن دارالیهود
عربها شهر «جی» رو کنارش ساختند و اعراب رو ساکن اون کردن. تا نیمی از منطقه شهری اصفهان عرب باشه.
نیمی از قزوین، محلات عربی بود.
این حجم از استقرار قبایل عرب در قم، مرو، قزوین، اصفهان و… اغلب به خاطر قیام مردم در این شهرها علیه حکومت عربها و مسلمین بود. قیام های قم بسیار معروفه، اما اینقدر عرب ساکن قم کردند. که شهر برای قرن‌ها هویت عربی گرفت!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5225" target="_blank">📅 10:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_NYMIMP3mBL1llu5QOcr-U0WJLBnihTMLsFjKMlqX88dNp0u3YYW5sj9WiTzv39S4vD9yGNVUAXDDKlvkuCsqBn4Z0aCONNeGhMzMU3YNw0RW8IGUGmgA2uAHC7irPRIIPfyDl097aeCwJ6xRMiZEFpXDZ_dG7enP1fy3bj-pf0n6iLljhgB-D6mZltF_V6yy2SlXSi_Pk1CyrDavPqAqZWtnTJKzBdXAwGbdgUVhRxA9YPVd0JjgR0X-o9ZEprnxskkoXEAnveHddqBvC3oZm3gpE7UcBupUCX8WdD_gbKxSUkTd0deDeEP5l0-cMsSkP6X0Fo0m7kzUswegR8Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطور تریتا پارسی در آمریکا
متوجه یک «طرح پنهانی» برخی نهادهای امنیتی در تهران شده؟!
معلومه یا این طرح رو خودش داده
یا با این نهادهای امنیتی رابطه داره!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5224" target="_blank">📅 02:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
مایک والتز سفیر آمریکا در سازمان ملل : جمهوری اسلامی با حمله به کشورهای عرب همسایه‌اش اشتباه بزرگی مرتکب شد و تاوان آن را خواهد پرداخت.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5223" target="_blank">📅 00:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vjf9fLvS-dDmBufsPhVQAy7S1Qmvmvh32stpwyGsJ5-4JO5sRom64wb9RunG2LAr60DegJmwEN_09YExGAlgO0UjTir2fMLn4FPFqs44PP6NItIMbGWrwifUfPlNrrB3tVbiC6UYrR0JpowXFKzWZ0vcfZt7-xM27LRfAJVVljstOY8_yArvZ5lh8TC_exTyybCCdSd_qRnfP_mI6jdSx9NVAPKMLUIpdf76fIdq5f_zfoengL9Sv4TpJc0fcj2u1K7iux37Ds5Jsu26jJjTW9napOnjcEvpUn8fUewfkh-07hinQCxc8TGLEuOftLamXofPuPfsouvfUPXiRE3I7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌های ضد و‌ نقیض از استعفای پزشکیان از ریاست جمهوری</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5222" target="_blank">📅 00:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fn7FEDhrnldj6I1o1SI4OXuwGyjvN598nS5-Gepr71I3Ad1PQ4UpXdPvshO0Utw7tezC-LxqQ6gI2v79hEomwv0tVFhHFhRIPYoCnNazdz8yoG4-IsSMs4l9kyUvegvfhVsR91yum4rG6oR5k3Bdxfi3kN1iBCqwPOESOSa6pmezC3kfCvuKuWv8Zn9iN1iZ9d4BK05ACb5p0VaSERrHn30utL3kSXDM_nPyVmny2aqK_DDI4RKO_TzWDUs4VFjbXG0azegOIz9e5iTKQBuD6AJwawEKMn0VTfwAimRO4Ggaf8uwNB7Y-8hjuQwYlcWQqsNA8dhH-DTYPaRsHonmJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t0IOx4MeFRac8G7OHq4nr_2ZlvbLUnN4L9TZn69STn0F8S4Ox489_pyvdBvycrlErhasVN-SwDEMwWImXTp-LnJH_3M0TxI7r72Z037_0Uhm_Oiu6qXkYQ_OLWMEmj7hWCABC5xlKzKyOyCJqPiTnB7swczjQ11nlUrSxavIqRh8hbHywL5x_zZg8eVha6cSm_vgmhuoSjIt_pV27R4VgYAINLClB0SqbAxXsF3lXCtAvgmjvsFdmRuVM63niMmrgRkA4J97H6CXGABLg7AaKfAc-ax7ob78WIeIGY7JSw8SAQ7tkv1iaxLpp5RzWQ5M6SkLW949aocoda74cuKbRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L5R63ehjdsv6_PXDqqkhOYWMYfVWPKeL08NlPD4_aDUhDVlPmQAbqdAt5BhF7CyR_chvLQbcCQnTKeIsogYG8iaEfwVs6A60KX7cVegXCxOAEyjb2eFOJrsgDy5ii_L-FR5XcZjdClgLBqUCdd2EEksyB2oQ5IUeiH9thI2VZYNEhKhkX3gbsMTv9tM0CN9jzdiOC325GGfS332R0ZPnPm1apAMW_lTbDlt2G5bXg9NHq1qFUJgl9ynr8yl7oqJxG5Rx7nJcmgCTFQsgfycyBaTZuAotG6QW0WxhyYjkq4LvyyWnEOIuJ0kpIIzw8Xqak-1BsBKTwux35VRPFGSE4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتون رفته میخواستید برید
پشت سر خامنه‌ای در قدس نماز بخونید؟
که شما تاریخ خوندید نه؟
تاریخ جمال عبدالناصر و صدام و قذافی و بشار اسد رو لابد خونده بودید
که همین هوس‌ها رو داشتن!!!
و به همین نتایج هم رسیدن!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5219" target="_blank">📅 18:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5216">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PNQAyJ4ACcLzZAc7XsygNX4BCGLkCW3ArwldS2f6sPRZtjkI5mR-0xH6pl-k9EvyIFCcK3qd6c7YJQXLUT5tteiELQTNClO34mKg6qaWH8qxK8Io0N2MRuMA7MHOcZZu8JLaWb3hvZzCeHq-9X91yslW65Gup0dzaCj7DfSdo0KFpPPWz_kK5bgvxe731_mVdjA1WPsDjPj59tbYCxDQdhD8rjelQMbcV3_XUMgPivjkPkSEPOoX5aQhmksscThXjJ6LWmrz__BL0mZBOrKmgH7nPXH1iX5uYkvOoxx5X-boOx_gvzJQqI4auvlVZvZzqigzvgg9rrLK7mR-ykD4PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JGFK_UxlkZFcYL3RfzbrYgAj_ofvrw0zs2unvCBE5kQyCoCTXhceBcqWPzD1ZKGwRPyOtZ-jwVpg9tJVH2vylAMsnRPbj3tV57b3e69lrMVX9OuSyfoCReFOOblbMZIAMoLuCmcSSxQmHe5aV-OUZ-uR7I9IkFlwXysvAldbzgd9vu20loPiO7ahseQ1ELIsGAH6oTDsfZcejvyTz3Q1yiY7ngKoNwOkzeJAFez2GHtoFlNaBGVI908NekjodY94-J1cmmZt6tTeVx8OIyef42PzX0sheBV74mzMtwQeopxA5Se64LlCbe-IvQO-Z8hF7VJYklboZDDpAd6LBhM02g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a3ThTo5NU6lsmpDQx0ulAORPx8NEEFrDAcwzFc4x8bkzXgvj-POjqjny-PG4764Fh0QIZ6S6_9fVuDSh6ix-ttbZkvxK9N-zC9FSnSPC35S50aDao98iYOIHoQPuh6B4q688xnxvIqubcI6i2OejcDMHx8QqoE7GIWYdWQqjnGN8mCki4SxdtiXebo1cx3VROnTnL5JzK5MJ4vnBiDa7uujMl-WHyyojtlRxZh-hqhnBHMOP9nmGmLdgT8OnWdk_dH-5AI6D89yFZYxCPShEA1HtGN3ssjvnciJn6KxD-3FbyoLLyufjc4HtE2i8F8Hcly_zO46lQ7T8_2MMTVQ7lQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفسنجانی سالها پیش گفت من به خامنه‌ای گفتم پاسخ این همه ضررها در دشمنی با آمریکا رو شما به عهده میگیرید ؟؟ خامنه‌ای گفت بله! جواب خدا با من!!!  و خب این جنگ‌ها و تحریم‌ها و آسیب‌ها و کودکان میناب و... همه همون مسائلی است که خامنه‌ای گفته جواب خدا با من! یعنی…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5216" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db68225cef.mp4?token=NtmsEeheCAdVtL1_YawSW3tdvt3PR9kTVr5eqLl6GaalGJAu4_1jmzcHCsgJSPhwpbncQHuWB17RWgPpfDi128sy9QNf8FuiiDcwXmiJKd940pCubATgZi2V4yqgvFq6ggmtEGLpL_MXl1BpV1oPRkjmy0WRwk58RuzkvCAFGHd-fKbIKNL7UGnxrMq5LI7eWgnqqGC14pEpZH5QG3mlg_biNZ0p3oVPGvxzXcPVYJpGMR_VYi3sDAI6u-EUlQUYKGXPEGDqnw1TsWqzQn_2yQa6f3c8vHIzT0JOfFRJkdjqjby08L5aJAHrWsSh4eO_EHzTi3riNR-_Dei6iVzXjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db68225cef.mp4?token=NtmsEeheCAdVtL1_YawSW3tdvt3PR9kTVr5eqLl6GaalGJAu4_1jmzcHCsgJSPhwpbncQHuWB17RWgPpfDi128sy9QNf8FuiiDcwXmiJKd940pCubATgZi2V4yqgvFq6ggmtEGLpL_MXl1BpV1oPRkjmy0WRwk58RuzkvCAFGHd-fKbIKNL7UGnxrMq5LI7eWgnqqGC14pEpZH5QG3mlg_biNZ0p3oVPGvxzXcPVYJpGMR_VYi3sDAI6u-EUlQUYKGXPEGDqnw1TsWqzQn_2yQa6f3c8vHIzT0JOfFRJkdjqjby08L5aJAHrWsSh4eO_EHzTi3riNR-_Dei6iVzXjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴ در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته «دو گزینه بیشتر نیست» یا جنگ و خونریزی یا مذاکره مستقیم «برای از بین بردن غنی‌سازی و موشکی»  این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5215" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=TQ6HL8bKqfpf3w44OTuPIMzLs9zOeMIIDLFiDxQrXHwbbsk_2Ae4tM-V2s6Rgo--_4bcNwTLfM_7qbxop0lSJr91tZKyYbh70jrxPZcnKeMirxMKLFk0-wvPB3wtY5-k-7Vzt5bmY_6NdhTsD21r7H1BRecXBdvCcB2x-8lO6SiJWBR7u12lRom8TlxlGN0wy6NgOW6ps7SxG3lKIKmrVbhh-aVN4D9_-62BJHxqUza7KJFtcyC7s7xfwEl28sYt73b7fG6KENJUnzi2zucL5mgZC3Z5OPLEGSY9xW8uV_B8u_ecsdVTQ5KS4K_k3ejaxZHmGFx55NvF3pzszR2F3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=TQ6HL8bKqfpf3w44OTuPIMzLs9zOeMIIDLFiDxQrXHwbbsk_2Ae4tM-V2s6Rgo--_4bcNwTLfM_7qbxop0lSJr91tZKyYbh70jrxPZcnKeMirxMKLFk0-wvPB3wtY5-k-7Vzt5bmY_6NdhTsD21r7H1BRecXBdvCcB2x-8lO6SiJWBR7u12lRom8TlxlGN0wy6NgOW6ps7SxG3lKIKmrVbhh-aVN4D9_-62BJHxqUza7KJFtcyC7s7xfwEl28sYt73b7fG6KENJUnzi2zucL5mgZC3Z5OPLEGSY9xW8uV_B8u_ecsdVTQ5KS4K_k3ejaxZHmGFx55NvF3pzszR2F3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌نشستن و  با نخوت وعده «دردسرها»  میدادن برای آمریکا و دنیا!  «حالا حالا دردسرها» خواهیم داشت!  بعد که جنگ شد تقصیر مردم ایرانه که تاریخ نخوندن!!!  تقصیر تلویزیون اینترنشناله!</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/farahmand_alipour/5214" target="_blank">📅 17:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=IhqDcf_TjYg6ZSUbNN2VfR4oJOsTlaIeZnpoNhr4f7noy0l5NGkvoLLW1EcbC4Nu2xAmDFu6WkQkaNW7j3DkJCQId0YArYFoLrwF-14V_evwr4ZcYLdQekKgugnYcPLGGuxV971nGNqPyfEFvY1B6jpO8DoqWhYthl4bY813sFmOp8ZW7JYmV2rIBZHFrlsI38XySVUjS7jwOJfSUH3Lz5zJ2ZdHPzGDIqn8UQdGSsHvmG8K_db9jBx1212eoWIDYd2VjT5cUpxoMauCW-BtF9AHst9rlhSQZUiKVUCsZZQImAthAjd1zJfoaLDpLNPrJiKEbfJ_czH4jH5V9pHBkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=IhqDcf_TjYg6ZSUbNN2VfR4oJOsTlaIeZnpoNhr4f7noy0l5NGkvoLLW1EcbC4Nu2xAmDFu6WkQkaNW7j3DkJCQId0YArYFoLrwF-14V_evwr4ZcYLdQekKgugnYcPLGGuxV971nGNqPyfEFvY1B6jpO8DoqWhYthl4bY813sFmOp8ZW7JYmV2rIBZHFrlsI38XySVUjS7jwOJfSUH3Lz5zJ2ZdHPzGDIqn8UQdGSsHvmG8K_db9jBx1212eoWIDYd2VjT5cUpxoMauCW-BtF9AHst9rlhSQZUiKVUCsZZQImAthAjd1zJfoaLDpLNPrJiKEbfJ_czH4jH5V9pHBkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی! جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!  فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ، بی ایراد هستن…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5213" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUYvPECRXfSwbC5835pMfVml384evqacVZulTK2uMBviAnYoFqa4VynKS8MC_jg45jON5Z8OwPjVL0WBhC64vvBuWWJDz0uuhQYHFPJ21sEd_LGS1nbbec4122h9A-TiR-83zKqsYlceVYx_bokVNYUbSHucrfhwBMtb7ZM7r4I-fn9GaMovlOGC4nLNj-WerXMBeJ2Ot1tOxAzaFwYQE5oUj9JkMwhNmLH7kH6AMb48RpG3h9H39Inf2dnwaUbrtX4a-UQofL_084HSub7uanuWcu1GLlSI6oDQyt58NVZjzWm3lmv1qbYJDAEtJUQyLAhE9PCoWRwCIprouuLY9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی!
جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!
فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ،
بی ایراد هستن و مشکلی ندارن!
و همونطور که می‌بینید روی میز مذاکرات هم بحث ایران اینترنشناله و افغانستانی‌های ساکن ایران و دیاسپورا! مشکلات و دعوا سر اینهاست!
خوش به حال آخوند که چون شمایانی رو داره! هر بلایی که سرتون ببره، آغوش گرم آخوند رو رها نمی‌کنید!
شما اگه تاریخ خونده بودید راه شوروی و کره‌شمالی رو نمی‌رفتید! راه
صدام و بشار اسد رو نمی‌رفتید و چندین هزار نفر رو دو شب قتل عام نمی‌کردید! بی‌آبروهای تاریخ!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5212" target="_blank">📅 17:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmtzeFcOmXIao_AfNe92nHJk4vOAwAkDDWy3-wRj9FvywuJmtSORoJisPH-FTlBRECsZejSgDldIYoKJclg_SlVUTgwOaIB1Mn1ZeFaCnOHi6xS7iSlGD_awNwQfwOjjgrxXwPWwm5enfzYN2eFK8ATX-gb77rxaE5TYPJwS3BDpfhwJRN85FV8Gdtq7fJkLcXCvlttvq6JvtIYMojO8E6TMmNu69EVgy-xhpmIb6GSeUZO5I1DBsiLM2-40ZnjNNho7nmU4EZy4scMYOCM0CrhkJIeK4cq3yVTOx2iCFDhrvQEW_PBCwhMK7fQuZwfZkyP__RQ9eBOt2L6SQ4jywg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله جنگ  ۴۰ روزه به خاطر ایران اینترنشال بود و‌ دیاسپورای ایرانی!
جنگ ۱۲ روزه هم تقصیر افغانستانی‌های
ساکن ایران بود!!! یادمون هست!
فقط فعالیت هسته‌ای و موشکی و نیابتی‌های
جمهوری اسلامی  و ۴۷ سال آمریکا ستیزی و دنبال نابودی اسرائیل بودن ،
بی ایراد هستن و مشکلی ندارن!
و همونطور که می‌بینید روی میز مذاکرات
هم بحث ایران اینترنشناله و افغانستانی‌های ساکن ایران و دیاسپورا! مشکلات سر اینهاست!
خوش به حال  آخوند که چون شمایانی رو داره!
هر بلایی که سرتون ببره،
آغوش گرم آخوند رو رها نمی‌کنید!
شما اگه تاریخ خونده بودید راه شوروی
و کره شمالی رو نمی‌رفتید! راه صدام و بشار اسد رو نمی‌رفتید و چندین هزار نفر رو دو شب قتل عام نمی‌کردید! بی‌آبروهای تاریخ!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5211" target="_blank">📅 17:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7ahKElDtZJ4qAMicFNHv9IsGhk13oDv_1WNkazkwPeI3ze3HPMR03b-7XPSKHesM3BxdiEdqqG5hCOGvjH-7BnyIi81FQ5Ddx9Hple3RoIPObly-M23KTILN-qSl2yAvce3M6-F30aZq9jhFNW75tgXQK1_SaT69Wr3dd4ehJPboNX546y7NjW-7085PbFQ3Sl0y-0iiBPMEFs0gxV34N9XcPALfWdLJwmTzuTNDdbqM9rjICSfqY3Q70y09MPOa9z4v4zWSx8msX6mleDmFAfvYMhn37EEAaj6WSbT6V0x9jmeqp6ROFgUDx6Bk_PJFywyCst2n_UWonRSCQ6GnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5210" target="_blank">📅 15:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwDAk29oAwdTEmJTuyv8uDHunNdN9a1xNF5kJdKNzhXSmk_HvXsx4w78v68NFMcSMnqmVLgBWvBFcvW4VRCsZXOWkiRlwqbCk2d7Jk2ZbLcT0tpIwEZ4h8XIDQq46MBmO-BDn7YpfDRVPDn1wIYpmd9eB7Tush_Df3vaRspqbj2P9H6k3lLIdlAlHNmY8acTKR3C0GLBzleuxdDO--fuL0_stK_CNBBQ9Gujx_N5Gehcjbm3JWouNPj7w-VOZHDRnsz_9CnMc-BFiXRtXI4eZf0LSiuIpndM2P0wp72xeeh4ZuCLsY3Pdl5Jg2JUHP3CAhEBacumG2zTwkYc_S1iig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل قلعه شقیق در جنوب لبنان
را تصرف کرد، این مهم‌ترین پیشروی ارتش اسرائیل در جنوب لبنان از سال ۲۰۰۰ میلادی است!
گروه تروریستی حزب‌الله لبنان،
بدون اجازه گرفتن از دولت و مجلس و ارتش لبنان و در خونخواهی خامنه‌ای،
به اسرائیل حمله کردند، اسرائیل نیز در پاسخ دست به حمله گسترده به مناطق شیعه‌نشین لبنان زد، بیش از دو ماه است که حدود یک میلیون شیعه لبنانی آواره شده‌اند! بیش از سه هزار تن کشته شدند!
چند هفته پیش دولت لبنان قصد مداخله داشت و تلاش برای «آتش‌بس» اما این گروه تروریستی و حامیانش مخالفت کردند و گفتند که جمهوری اسلامی باید این آتش‌بس را برای ما بیاورد!
(که بعد تبلیغ کنن قدرت ج‌ا بود)
جمهوری اسلامی نیز توقف در جنگ لبنان را در صدر خواسته‌های خود از دولت ترامپ قرار داده ولی هنوز به تفاهم با آمریکا نرسیده و اسرائیل هم داره کار رو ادامه میده!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5209" target="_blank">📅 12:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=GVT1U6vWRji4ZA7hFnvmuDAHzE7PdaxTBigZXkgxzcGwhrda0N4H9O1m9GaY1xLKkXmmu5Aactff66gXsJCk9PWDV7jKgAcX6DfwvZ_NyjURDGvYtijnlO1kDBINiNLyaX5D7yxdNLGSXbc_vKuYAdhuIh7MFTns-uDqi090EMr18VBu-DTYGvEE1CS2rR0miKbfFiHvv0k1R9eCJEls3f4whz7TeA9SBXlkC2XnCNEVAElI0ETibuK5iNQx1mT_GqBKhHq8zPpCxpZbBX-JU15NTce0rWcu4LiazN8eUmVKwwy1sw3peu4FDEWboAHPlp4bIgRim4ukknq4ZEo9rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=GVT1U6vWRji4ZA7hFnvmuDAHzE7PdaxTBigZXkgxzcGwhrda0N4H9O1m9GaY1xLKkXmmu5Aactff66gXsJCk9PWDV7jKgAcX6DfwvZ_NyjURDGvYtijnlO1kDBINiNLyaX5D7yxdNLGSXbc_vKuYAdhuIh7MFTns-uDqi090EMr18VBu-DTYGvEE1CS2rR0miKbfFiHvv0k1R9eCJEls3f4whz7TeA9SBXlkC2XnCNEVAElI0ETibuK5iNQx1mT_GqBKhHq8zPpCxpZbBX-JU15NTce0rWcu4LiazN8eUmVKwwy1sw3peu4FDEWboAHPlp4bIgRim4ukknq4ZEo9rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، ۱۸ دی در جریان اعتراضات شهر قدس بازداشت و پس از ۶۰ روز پیکرش تحویل خانواده داده شد.
امیرمحمد ۱۸ دی‌ در اعتراضات ناپدید شد. خانواده‌اش به بیمارستان‌ها، سردخانه‌ها و پزشکی قانونی مراجعه کردند، اما هیچ اثری از او نیافتنند.
پس از دو روز و در ۲۰ دی، تلفن همراهش روشن شد و ماموران حکومتی از این طریق به خانواده اعلام کردند که امیرمحمد زنده است.
خانواده پس از این خبر، پیگیری‌های بیشتری در دادگستری انجام دادند و آنجا نیز به آنها اطمینان داده شد که پسرشان زنده است و حتی برایش حکم صادر شده است.
امیرمحمد دانش‌آموز مقطع هشتم بود و خانواده تلاش کرد از طریق آموزش و پرورش نیز این موضوع را پیگیری کند، اما در آنجا نیز با پاسخ‌هایی مبهم و با برچسب «پرونده محرمانه» روبه‌رو شد.
این بلاتکلیفی و بی‌خبری تا ۶۰ روز ادامه داشت؛ تا اینکه در نهایت پزشکی قانونی با خانواده تماس گرفت و اعلام کرد پیکر امیرمحمد شناسایی شده است.
پیکر این نوجوان با کد «ناشناس ۱۱۷۵۴» به خانواده تحویل داده شد.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5208" target="_blank">📅 10:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=mgiB5QMNvnuz_BywqETIV7G65SboB57WwXaoLTofFz8Nu-ZO3f20GRYVADe2CjAlze7XkMqfb0bTKr65iEd9g5YPIXfYvR039iPiebhf5FJdO0sI725-VtJqaLgrb5AifyB9LzJt4dhmFgTXDos-VCAZHDl_UeQ2KK6urMnvS5u6XpH4ncxgW2o2f5K6vTUsp4uxQ9RxfJVgP5E_uiAXBw9gPRlH3dYeBwzuVzrW8tNx1EmgaHmuYRqJMiiAFLepsmE3EDIZRsED0aX0Li3jneRtUfbpzBOwKMCIUvF0pH8kifszzFz8jnZ_eljgOWD-dSMcbHVUVfrCe7J1STMucA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=mgiB5QMNvnuz_BywqETIV7G65SboB57WwXaoLTofFz8Nu-ZO3f20GRYVADe2CjAlze7XkMqfb0bTKr65iEd9g5YPIXfYvR039iPiebhf5FJdO0sI725-VtJqaLgrb5AifyB9LzJt4dhmFgTXDos-VCAZHDl_UeQ2KK6urMnvS5u6XpH4ncxgW2o2f5K6vTUsp4uxQ9RxfJVgP5E_uiAXBw9gPRlH3dYeBwzuVzrW8tNx1EmgaHmuYRqJMiiAFLepsmE3EDIZRsED0aX0Li3jneRtUfbpzBOwKMCIUvF0pH8kifszzFz8jnZ_eljgOWD-dSMcbHVUVfrCe7J1STMucA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8ybo9UJAinI6mFJ9U01TV0JKjeBnh_buJ5BaqhgfM7padeiVnaY9nDOrQbEKJaPuW-YbGkners9oq4EWK7mqJsv02Y4vSQzCCRm-n7_IoqFVOPm3E-s2TdXcdl3NDBRj4c2IPA5KFCKe1GkmTLOGFfR4KAx_3-xpVzq6HNfNpLpJbAM-QsjMIal2P0Olkg0EwTEfBLgQaV7cGpvzaR2g-xdI8JNkLR2WevLPLDna3BvWLd8B-6hapwBtSO7TNzIjfLHHtUAv_qyZ0g-9ZrdHJwzuIV5yiUmIBym8JHKuEHSfQB1g47Xb42Mg0cEiFtudWFsGzQgKHRuj5WkxI2vqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی با آب و تاب می‌گفت
به امارات حمله موشکی و پهپادی کرده،
حملاتی که ۹۵ درصدشون توسط
سیستم دفاعی امارات خنثی میشدن!
اما امارات در عوض پنهانی با جنگنده‌هاش
حمله می‌کرد و جمهوری اسلامی هیچ سیستم تدافعی نداشت!
یعنی اگه به ایران ۱۰۰ جنگنده، یا ۱۰۰ موشک حمله می‌کرد، میشه با اطمینان گفت ۹۹٪ ماموریتشون
رو انجام میدادن و اهدافشون رو میزدن!
کما اینکه اسرائیل ۸۵۰۰ سورتی پرواز در آسمان ایران انجام داد حتی یک هواپیماش آسیبی ندید.
آمریکا هم ۱۳ هزار سورتی پرواز انجام داد.
آمریکا همچنین ۱۰۰۰ موشک تاهاماک به ایران شلیک کرد، جمهوری اسلامی قادر نبود حتی جلوی یکی از اونها رو بگیره! یک در هزار رو هم‌ نتونست!
جنگ با امارات رو جمهوری اسلامی کلید زد
و هنوز هم کامل مشخص نشده چه آسیب‌هایی
ایران در این جنگ متحمل شده!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5206" target="_blank">📅 10:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhgoQ_MRCd69S1O_dgO-a8J3AukeecVkpv4D31BlFBiAxTsZa7mlu0ijbqR-ScEMmqaXKG1qEETF-8Rsqp_0xhCs4v8LNDrzGKmPHNCkjGdnK79qOpWDJ9hjg2N2dO4g2_TCamQngNjppyqobhaPHksQsikWXdjbVCpjxBdPEIcppQ13NLWC6-ycG651IChQmtcQROv2P6UBFikhrzeg7XxD_E_BUXDIenOke52nyhkSEr_Z-NUQjDjyS47wDM9qf27h8CyjMUGr3N8QI3ZFFxDrzRFrb7LsLWoSX3nT0x3k5QbrSdpymY4hzvcbYrPpgc23hNqGYg-iKLwhUEzDEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1CAY60w7Sb89zMVY6qYFfsKkmFdZ6l1XJ-hkktWdvi5LCubROhsghTPfhoEBuUv_mlPLRLqaWGGYCrneh9BmTVESS5KF_uuyC3_NZP6xcf647Z5j7LIXfYi7KUzPl4do3N5pjysOKuE71ZDT8D1IB_MABKfzZinvIINcWVMhZWR0GH12dArQ3FxEWj5TDK1S7L501CMlPaeOXWdkKAEAd8Ry4zheIVV92evv2ZQ2LtzzLfw_WisfvTSZwjTLfc6PawrKaPjgmE9qoyhhcjHjTW-kJNQRv4HcbqABIknt8mp-08ZTMgzJbw_k5ZJBvqe0AXKF_abrbI0-7yAwVGxPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIq2OcUfeyv56qIslQL8XCpNnnHukYp-UbmloOWLjCMbvDfFzXcTLUSWyV76w8DskB7eWz3Va-I_ekIHoGwOzzHvOIKNbxuBlXslojbxD0cBIrN96y81f2lGQoDxT5C0UT1M1pMuS-sGpSKFF2aSKgUL9lk7iPKAk2-K1CIs2TaW7gbU8CDl-QRqp0FKW63xRW8XYrMaYtYSL4cbYlRrPqIEI4IvQW_48RL3KWr3drHw0Vqd0qt_E44cvudFjdpGeiYRS98U9kwH0psEp1oNQt5fP04C39Ob9rGufeC0M1EWh0f3SVdymb-Hv9F5eg_cCrDO1E65uEAv-eAf_lkMqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی بهتر برای جنگ بعدی …</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5202" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : برای اتخاذ تصمیم نهایی اکنون به اتاق وضعیت می‌روم.
«ایران باید موافقت کند که هرگز به سلاح یا بمب هسته‌ای دست نخواهد یافت.
تنگه هرمز باید فوراً باز شود؛ بدون دریافت هیچ‌گونه عوارض یا هزینه‌ای، و رفت‌وآمد کشتی‌ها در هر دو جهت به‌صورت آزاد و بدون محدودیت انجام گیرد.
تمام مین‌های دریایی (بمب‌ها)، در صورت وجود، باید از بین برده شوند. ما با استفاده از تجهیزات پیشرفته مین‌روب زیرآبی خود، تعداد زیادی از این مین‌ها را از طریق انفجار نابود کرده‌ایم. ایران نیز باید فوراً هر مین باقی‌مانده را جمع‌آوری یا منفجر کند؛ البته تعداد آن‌ها زیاد نخواهد بود.
کشتی‌هایی که به دلیل محاصره دریایی بی‌سابقه و فوق‌العاده ما در تنگه متوقف شده‌اند ــ محاصره‌ای که اکنون لغو خواهد شد ــ می‌توانند روند بازگشت به خانه را آغاز کنند!
از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدر و مادرها و خانواده‌هایتان سلام برسانید!
مواد غنی‌شده‌ای که گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌شود و در اعماق زمین دفن شده‌اند ــ زیر کوه‌هایی که تقریباً در نتیجه حمله قدرتمند بمب‌افکن‌های B-2 ما در ۱۱ ماه پیش فروریخته‌اند ــ توسط ایالات متحده از زیر زمین بیرون آورده خواهند شد. (طبق توافق، تنها آمریکا و چین توانایی فنی انجام چنین کاری را دارند.)
این عملیات با هماهنگی نزدیک جمهوری اسلامی ایران و همچنین آژانس بین‌المللی انرژی اتمی انجام خواهد شد و این مواد به طور کامل نابود خواهند شد.
تا اطلاع ثانوی هیچ پولی میان طرف‌ها رد و بدل نخواهد شد.
در مورد سایر موضوعات ــ که اهمیت بسیار کمتری دارند ــ نیز توافق حاصل شده است.
اکنون برای اتخاذ تصمیم نهایی به اتاق وضعیت می‌روم.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5201" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hOdZi-UD4vl29VVJzetxieU_tGOvioibjpy2J_yZo8be8OxhKDm4R6XyQGTq-MXDI86Z83vBGa8CDpqVeP_Idmg1UogD3-8F8KDrHc9f4eFQhBmf79tZcGwGFhw1I0xuzKvV-GvxOcYjnh9C7sVcQAk6iNHv7SR1BCqAMans0IpTgyLJMGwrHhcToPtEEaKBE8GaS7OEROdawuKI89JwdLvJWC10bV6EVNC844pOvwguQhVagR9Pbn6anxiVkpL-idx78Sy-rsRPlDGyj5-vjYlZB8DwlWPsDnfCddFIx5BWAvu0296JMVTMGCAOGlGnflPtDLeV6kW1G26m_urT9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H40fOUmVrMKAF3DbO_kVC0ps0oRmABb-aQ1QO29Z-3eZGC9GefBb0rFWgOAxxk9RY1mneTZoVnTV_3890yfj55wTToMKxFuKYbHwcCK1bjRNUFUBFXs751BE_2qTfolFIwYQdh6-qUXI0lPrFIxvrO3gAwCi7JF9Vq4VQnnpPb7tZUIQOnvqLq3LqJcGj-bYV9TgYkaTo_GuP0C3sKZ5lctIYilyd5dXUB-3Ojgf9_2Sg5rTqyIuTrX0y8Msfbm9e-NONKDgSz-UiZsERvBZIK8cUiIMWNIWlF6g3qXldsrnzH3hcqckqHEVOF68J-wZfBtmqWWE9pbJtofq-LPKlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
لبنان سفیر جمهوری اسلامی رو اخراج کرد!
گفت «عنصر نامطلوبه»! گفت که جمهوری اسلامی عامل وقوع جنگ در لبنان شده و جنگ
رو به مردم لبنان تحمیل کرده.
اما سفیر جمهوری اسلامی در درون سفارت خانه موند و گفت برنمیگردم ایران!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5199" target="_blank">📅 18:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D_7XB9h4qYzSWYycxhokkNqIsOlcPyGIg0PTiixWHNnYum8YN1hkYnYMuqRWSmvKhAxWsMjNPNei8JbsaxYbhydyvNlJ6ujmo9mbHCjDWM1_PigNCHtwKGSFWCZ4-gOW5MxQLu1047Nq2nX8QhH7DMWyAMmmdoc81CtMh-JC2ptoWS3ZH2GFe6sNJsVY5-pNjq4PbmFaUJj464eZdnUS6nMlPXa1PBzZ8-yA-g03mhCO6spYDvJRGclN-_lwRzoeno-Lgo1wW0cRJdayjfLE3mNg1K-p73ZQJ-a3Q5W5zTK7F_Lio2dfVM7UzJR0pyqCrGqZkKxX2jyrNeG1Xe4Hyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pmvH2n31uXCxIkEOEWe3ke_fgeW02x-YFdp6pj5NH3IbiMISL8kme-cQR6JW6HMMWwQM22AcjLsmgXEhtEWvSiNAI1hzmZpy2YqqulJuKdd0sGTrlk9oRRyq34Oz2EVS_PlgfSMMIQoEVorrkbLhRrk5tsKxBQdRndphskSFWKvYM34eyZ3kZahSq63CNiwjsZwCq6y5QtPQEE3M2n-9xr5dt11EO6Wfm3f6EhtdMl5UKXnzN-bv7DM2h7yPR9F3B1jRW1G4mlkiJFjK6mho0tpjnQddffNEkMb3f66fQc6N6qP-3wohHQtCdsGie6NHNR-rv0k0qoXv-mZNEnCLqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
درسته هر شب توی خیابون‌ها بزن و برقص و عروسی داشتن اما در افغانستان گدایی پول میکردن :)
سفارت جمهوری اسلامی در کابل در اواخر اسفندماه رسما تقاضا کرد که  مردم افغانستان به جمهوری اسلامی کمک مالی کنن!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5197" target="_blank">📅 13:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=SPh6em7KjpE7_aUCa44ncbQ8XlodosmjRRw6NG58BQ5XrfJWYM3bnrFxprVI1lDeXLclB9Bmbv7WalNjnG8nmBy4kPxQshogRK_hlNsUnuBjBvmt53CIatXcWarH5c8sv-4oVBpcKObbg18ieFxnPWnc0p-PwfHAGZCVgCG8BVQkZzFz07p3nVkNo4D8UJxtX1H3kbTsLjEenBSJDTFQsqFo3oU1k_dvJCBQquSnAzOxC2OhxziK942gDv_4E3MvpPMMGUh0EvzWhwgnW1m_3YdHrB9F2pmSrCnHovMLzpP9adrU_bqiEELpFbFPdoTm8HevaDSYFfmr1NH23SILDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=SPh6em7KjpE7_aUCa44ncbQ8XlodosmjRRw6NG58BQ5XrfJWYM3bnrFxprVI1lDeXLclB9Bmbv7WalNjnG8nmBy4kPxQshogRK_hlNsUnuBjBvmt53CIatXcWarH5c8sv-4oVBpcKObbg18ieFxnPWnc0p-PwfHAGZCVgCG8BVQkZzFz07p3nVkNo4D8UJxtX1H3kbTsLjEenBSJDTFQsqFo3oU1k_dvJCBQquSnAzOxC2OhxziK942gDv_4E3MvpPMMGUh0EvzWhwgnW1m_3YdHrB9F2pmSrCnHovMLzpP9adrU_bqiEELpFbFPdoTm8HevaDSYFfmr1NH23SILDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=s6atBobHxq3KS7WNC5sUJPxi847fAxbZJRcdX2zEj1sIbTAS2zogq7jg5X2QaQMqgnX7hRCaKo3VzftH5uzwyQcumm7B0hl0G2YZAvok8RbXFPw6rgQsG_Clt2Jmwnd4zuvMFRRcel5Bf9ZE3rhQocJobzk4jDMpzMV3IjXeS_WRqVA_V-coZqKEtPb3_QZnaV5I0LiUIYTg5x4ePsX-fmxZ6IU2KGuGeTlyOtmfBQQVEg4NKtlir-qUnPepCngssZE8zQA3CEKt4r37QPf2LdVqkM1xCwrjTN39El-TRItSYqHivjV19_LRMc4ckjOenr9bs9STN9q-tsmEaociqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=s6atBobHxq3KS7WNC5sUJPxi847fAxbZJRcdX2zEj1sIbTAS2zogq7jg5X2QaQMqgnX7hRCaKo3VzftH5uzwyQcumm7B0hl0G2YZAvok8RbXFPw6rgQsG_Clt2Jmwnd4zuvMFRRcel5Bf9ZE3rhQocJobzk4jDMpzMV3IjXeS_WRqVA_V-coZqKEtPb3_QZnaV5I0LiUIYTg5x4ePsX-fmxZ6IU2KGuGeTlyOtmfBQQVEg4NKtlir-qUnPepCngssZE8zQA3CEKt4r37QPf2LdVqkM1xCwrjTN39El-TRItSYqHivjV19_LRMc4ckjOenr9bs9STN9q-tsmEaociqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید
در اجتماعات حکومتی شون
هر شب عروسی داشتن!
«صیغه یک ماهه»! در برابر «یک سکه» :)
با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">وقتی شما نبودید پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،  پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!  حتی زودتر از پیام‌ شهردار تهران!  حتی زودتر از پیام جوادی آملی :)   پوتین در پیامش نوشته بود :…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5194" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i_GVyfYWaQZh_D9AdeV6OqaTWTPuDuE6VW8OgQC12RVlc8DqWI29ULdBvu5IGLCi2i-I7XgFK2tgdAa3SKYsGK2Z9E3qRPdmnh2xF9u5NWTPRGhfJNJBpKaLO3D5RK7RXA-hcDGgNx0SLeZRRJkzP_ghDMgfQO5SNLdGCx4sqQaneuUS4mJUZVJzGdDPvtrCk9ziI6qin_zz8a5XBwJmkPKcyyH_m4IZUeCJxDxTxvtfLcGI7VUpIV-tPaRxHEjghBUEzxmC2Xqu7K8U7fKAbVEurqA6GPM2oztWHOk3UbiBmrlBngB3oY4tGwOHROqGn5phxz0Ig2Xde1X_gPbxGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/daCsjkdFYC_g8U7S1RGHyzxeOfaKFQtnuWVw88Seza-Uk8nZYLVNGzq52vpUDX-qcnWjYIWbharJUuVAlOTZbHEzeUD7Z4WbWxYfV_nCwONapIPrM99lgQacU9CKqcpTTyfxdWIM8oeqzeqOtnb9tLEV7G1AEIOS7iwP0RD4f4MRB40Xh3pzAZMe4p6e2RufHO_aUu1kGd9T1Q8qwWTVgC9LFrCw2ykBse21r92tNlNMoXEch_92zDOmcRAHq19OqNoQazST7lK1ZbpKHJjXw1zSIQlALQFeP_ybMtZ8Ver5_v-Kma0mBbdjdLJvqOHRZ_DxBQKUNdM_AdZ2LYgOuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،
پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!
حتی زودتر از پیام‌ شهردار تهران!
حتی زودتر از پیام جوادی آملی :)
پوتین در پیامش نوشته بود :
«اطمینان دارم شما راه پدرتان
را با افتخار ادامه خواهید داد.»
پوتین راه پدر مجتبی خامنه‌ای رو دوست داره :)</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5192" target="_blank">📅 12:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=ffNbOS-v-vovaCwd5M87Yn00vGVexBKXi9qtHfV2v_LAQginVlxtlm32ROZpknxQhhOnz-4GiLb2ZvRnsapbj9SJsDDoK6LeGFn89woCFLE8WWT2CnzTK55FDk1x29_ES62FNjug4K-DY9cpPySdsZ1oQl-gs3GGpRcG8sIJOyfSebXGXpOQADJdOAWyTE_4FkUNeOl6XcSWKoMuP_PVi31bTvFTrmjvWbx3FpTfBLCW0g5JHT1Hm2mzcaYO_Z9Cg7t9uFUi5YgK47RYN1_oI0ehrl144-lSFRZiGRgrX4wGhS-rrB4N2IlokolyQWXuOysHRC-BLstd-1ahNpYfag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=ffNbOS-v-vovaCwd5M87Yn00vGVexBKXi9qtHfV2v_LAQginVlxtlm32ROZpknxQhhOnz-4GiLb2ZvRnsapbj9SJsDDoK6LeGFn89woCFLE8WWT2CnzTK55FDk1x29_ES62FNjug4K-DY9cpPySdsZ1oQl-gs3GGpRcG8sIJOyfSebXGXpOQADJdOAWyTE_4FkUNeOl6XcSWKoMuP_PVi31bTvFTrmjvWbx3FpTfBLCW0g5JHT1Hm2mzcaYO_Z9Cg7t9uFUi5YgK47RYN1_oI0ehrl144-lSFRZiGRgrX4wGhS-rrB4N2IlokolyQWXuOysHRC-BLstd-1ahNpYfag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم مشهد از خبر کشته شدن خامنه‌ای</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Va3rjzUwn8iJUQye4TN6aQ2_JGf0kJp4mAFoTp2oA3E2nzAmd3Pv9oDM86OXq9MtYr_kA1MXs_Z6ZqnFDAp-IX3xf_K7v0TDegW9FKcmn9KUAhdIs6TNdLDSF3iZpWdxsMvoTyT8DGQoMUqmHfW0IcFeCAoQ1jznRWlNw2fYYl1raJH7teeS6k8UX6Pt-W6d3xPyrNpmPKY9jsUkPO6zArzgnRc2o7aohGrSyJMTD8-OpAwJ-TJg21orVRUBQpG4IVBHWfz0bLyIk5Vja0Js9n8eql9M6uwJ_wFyEwW5VMYauC3Hvq8J845UVQ9tmz-32PtZsBH2uYfhInI3EBoT9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نکته جالب :)  امروز ۲۶ روز پس از کشته شدن خامنه‌ای  در کره شمالی هنوز خبر کشته شدن خامنه‌ای منتشر نشده!  فقط اعلام شد که مجتبی خامنه‌ای،  پسرش جایگزین او شده،  اما اعلام نشده که در طی یک حمله نظامی  خامنه‌ای کشته‌ شده.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5190" target="_blank">📅 11:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏حالا که تشریف آوردید:
‏از ۵۷ کشور اسلامی، فقط ۸ دولت کشته شدن «ولی امر مسلمین» رو تسلیت گفتن و ۴۹ کشور سکوت کردن!
‏عراق، آذربایجان، تاجیکستان، پاکستان، لبنان، الجزایر، عمان و قطر تنها کشورهایی بودند که تسلیت گفتند.
‏بزرگان جهان اسلام چون‌: ترکیه، عربستان، اندونزی، مصر، مالزی،ازبکستان و… سکوت کردن!
‏تروریست‌های طالبان هم حمله رو محکوم کردن اما تسلیت نگفتن!
دولت فلسطین حتی حمله رو هم‌ محکوم نکرد! سکوت کامل!
فقط تروریست‌های حماس محکوم کردن و تسلیت گفتن!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5189" target="_blank">📅 11:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
امروز : کشته شدن ۱۴ نیر‌وی سپاه زنجان بر اثر انفجار مهمات عمل‌نکرده</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5188" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5187">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های جمهوری اسلامی  از بستن تنگه هرمز خبر می‌دهند.
🚨
🚨
🚨
سخنگوی قرارگاه خاتم : به ۱۴ پایگاه نظامی آمریکا حمله کردیم و «صدها» ‌تن آمریکایی و اسرائیلی را کشته‌ایم.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5187" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5186">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پایکوبی مردم در تهران</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5186" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔺
شادی مردم ایران از شنیدن  خبر مرگ خامنه‌ای
🔺
بیانیه رسمی دولت اسرائیل تا دقایقی دیگر</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5185" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">حمله به بحرین
😅</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5184" target="_blank">📅 10:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">شاهکار جدید صدا و سیما  اینها رو باید تلوزیون‌های جهان در بخش سرگرمی نشون بدن</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5183" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5182">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">«دیشب مردم تهران در کوچه و خیابان  کل می‌کشیدن» مرسی از بابت این اعتراف و این مستند سازی از وضعیت تهران پس از انتشار خبر مرگ خامنه‌ای</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5182" target="_blank">📅 09:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5181">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=EQXAYZWUYNIL7mEC7fhb_d1M8EqAll_N_62pfy2pfenW3aKiu8HJ9kgR0bi4A6v2ddaqB5rxXciv2p3asUVmHgRbYg4tpp9lKw2yXfr5MatbLpaD6TS9hllBkYuIg5z95Ev-oiraj---Fg20_tN3xsKmfS5rJXcW6yThl1yq7bMQnAynQFJAjrLoCtGKzUBrHDUmaSPlPu9e3vNfDuiPGOZ_s0DHTPc751wYY_TPqacNrSGdg6_AsGWi5OpeQqMk5xuuOM6M0M68EvI_irQm08DN6oi-w6TgVLaXwoK-LQ8E5k03ZSECTG8NnfO-QbuprHRSlaAvj9p6kKiCLnG__Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=EQXAYZWUYNIL7mEC7fhb_d1M8EqAll_N_62pfy2pfenW3aKiu8HJ9kgR0bi4A6v2ddaqB5rxXciv2p3asUVmHgRbYg4tpp9lKw2yXfr5MatbLpaD6TS9hllBkYuIg5z95Ev-oiraj---Fg20_tN3xsKmfS5rJXcW6yThl1yq7bMQnAynQFJAjrLoCtGKzUBrHDUmaSPlPu9e3vNfDuiPGOZ_s0DHTPc751wYY_TPqacNrSGdg6_AsGWi5OpeQqMk5xuuOM6M0M68EvI_irQm08DN6oi-w6TgVLaXwoK-LQ8E5k03ZSECTG8NnfO-QbuprHRSlaAvj9p6kKiCLnG__Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پلیس پاکستان داره عزاداران خامنه‌ای رو با چوب میزنه  دیروز هم پلیس پاکستان ۶ تاشون رو کشت.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5181" target="_blank">📅 09:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5180">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بخش خبری ساعت ۱۴ شبکه یک و تکرار ادعای زدن ۳ جنگنده آمریکایی  در آسمان کویت و تکرار این سوال که چطور در آسمان ایران به این پهناوری نمی‌تونید ‌، در آسمان کویت تونستید؟؟</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5180" target="_blank">📅 09:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">فرماندار جم در استان بوشهر، می‌گوید که یک «پهپاد متخاصم» منهدم شده و وضعیت شهر به حالت عادی بازگشته است.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5179" target="_blank">📅 00:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از شلیک موشک از منطقه جم بوشهر به سمت چند کشتی که در تلاش برای عبور از تنگه هرمز بودند.
گفته می‌شود در جریان این حملات موشکی که از سوی سپاه صورت گرفته، به سوی یک کشتی آمریکایی نیز شلیک شده.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5178" target="_blank">📅 23:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5177">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=DHelvHuNasVZ_EPmR8W4aYqSKoMy7kG3rAMiBU8NwOdTxhz5lquuUsXVfqPM5HPNlE7vbHKhjXHP4n0734PZAjtPw4grJ-5LXp_oaRGzfKjzbiV304nTIgok22TWNs121Cli0Jx8m2zMFv_U8q3NImZYJ-9HS7S-DgfXsTdbQQEg14ufdqe5cS0n93ru5wCgCm8qgjcKyUdq_h1-wVBCo9mp7Ff8_tVvB7WAvs9iR_ZyAYxKPQgLcY5w3oSrwZ6ROT8oL4b8GUK8WoR1Mvvi7ncx_NQDZdmBO6fUtBi0Fx7w8dDOPH4chRA7RS77DvBk_JaJIVyzjYoSpOkGJK5nTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=DHelvHuNasVZ_EPmR8W4aYqSKoMy7kG3rAMiBU8NwOdTxhz5lquuUsXVfqPM5HPNlE7vbHKhjXHP4n0734PZAjtPw4grJ-5LXp_oaRGzfKjzbiV304nTIgok22TWNs121Cli0Jx8m2zMFv_U8q3NImZYJ-9HS7S-DgfXsTdbQQEg14ufdqe5cS0n93ru5wCgCm8qgjcKyUdq_h1-wVBCo9mp7Ff8_tVvB7WAvs9iR_ZyAYxKPQgLcY5w3oSrwZ6ROT8oL4b8GUK8WoR1Mvvi7ncx_NQDZdmBO6fUtBi0Fx7w8dDOPH4chRA7RS77DvBk_JaJIVyzjYoSpOkGJK5nTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف رهبر شهیدش رو پاره کردن :)</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5177" target="_blank">📅 20:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=WAhXWNQtyVs59uew106f1euL_TdlS4sAZOZ8hmts1KA9evrnAp9BteQfXzkZyep1PbxkFTH5CYy4040sdCoV9kdt-_smNaenJHht__t__CSsVnIQlKoe-AEmQCM2Wmnmr1fsdNMBdtUI5E9IjUvJB_j2p3ayWndsJYJWcnTO_sciLaa8aI9vGMyhwKLBgMPPkH6B-IWVoMcakuFCkC2eCuOsDeg19jJJOsdiDzndA4AIwlVsqcQIXwfSpVZLkNRXpICnLskgUmc1K2ekEs7A_YWTVjgss64x6auDw0vPP8vSzKmn99Qrc-QMyR4MyaDuBbcTMDSsEHa9v84zB3pjGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=WAhXWNQtyVs59uew106f1euL_TdlS4sAZOZ8hmts1KA9evrnAp9BteQfXzkZyep1PbxkFTH5CYy4040sdCoV9kdt-_smNaenJHht__t__CSsVnIQlKoe-AEmQCM2Wmnmr1fsdNMBdtUI5E9IjUvJB_j2p3ayWndsJYJWcnTO_sciLaa8aI9vGMyhwKLBgMPPkH6B-IWVoMcakuFCkC2eCuOsDeg19jJJOsdiDzndA4AIwlVsqcQIXwfSpVZLkNRXpICnLskgUmc1K2ekEs7A_YWTVjgss64x6auDw0vPP8vSzKmn99Qrc-QMyR4MyaDuBbcTMDSsEHa9v84zB3pjGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از ۹۰ روز صدا و‌سیمای جمهوری اسلامی می‌پرسه در حمله به بیت کیا کشته شدن؟
کمیل خجسته، برادرزاده منصوره خجسته باقرزاده، همسر علی خامنه‌ای، میگه  افراد خانواده خامنه‌ای که کشته شدند، همه در یک نقطه نبودن! در جاهای متفاوتی از منطقه بیت رهبری بودن که به همه اون جاها حمله شده.
این همون حمله‌ای است که پسر عبدالرحیم موسوی ،
رئیس ستاد کل نیروهای مسلح میگه ؛ ۳۰ روز گشتم و جسد رو پیدا نکردیم!
عجیبه در این حمله فقط مجتبی سالم مونده باشه!!
چرا خامنه‌ای در پناهگاه نبود
!؟</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5176" target="_blank">📅 19:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
آمریکا و جمهوری اسلامی به یک توافق ۶۰ روزه رسیده‌اند تا آتش‌بس را تمدید کنند و مذاکرات درباره برنامه هسته‌ای را آغاز کنند.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5175" target="_blank">📅 19:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/208f980645.mp4?token=gvQpdYaFLKBlk7qlcdpwgvUraUJsG-Btx8tKlsC8-hpEnhoiecGfwJN43l9xKvFhLf1Hhmb6-PNGfw0vRxG2NQ3dL2gAbd1U2aQsDwzfYKyGtyba4XlRAvZnJauAKiMCX-G1ZEouHqN-jz2NVRP1EFtHWKX3mZnvd1V0dBMTACV-Hm3M2i2PpBUwh2fXK3e-GvNvgrea2G2N9g5S9Y-Z69W8aiahf0bU-KXcWwqZLmeEqOEbTL8951L5faG1bwRtQS_7CNzKzmop_ciqzVzpLU1DLvzfaSEC5hM3ASwQFZVXAR00iT9KLE-PApXg8WWfV9R2uIuaTpm9D1yQaJzbuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/208f980645.mp4?token=gvQpdYaFLKBlk7qlcdpwgvUraUJsG-Btx8tKlsC8-hpEnhoiecGfwJN43l9xKvFhLf1Hhmb6-PNGfw0vRxG2NQ3dL2gAbd1U2aQsDwzfYKyGtyba4XlRAvZnJauAKiMCX-G1ZEouHqN-jz2NVRP1EFtHWKX3mZnvd1V0dBMTACV-Hm3M2i2PpBUwh2fXK3e-GvNvgrea2G2N9g5S9Y-Z69W8aiahf0bU-KXcWwqZLmeEqOEbTL8951L5faG1bwRtQS_7CNzKzmop_ciqzVzpLU1DLvzfaSEC5hM3ASwQFZVXAR00iT9KLE-PApXg8WWfV9R2uIuaTpm9D1yQaJzbuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش زدن ظریف :)
نوبت عراقچی هم میرسه!
این مسیر رو خیلی‌ها رفتن!
از منتظری و بنی‌صدر، تا موسوی،
خاتمی و روحانی، احمدی‌نژاد و…..</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5174" target="_blank">📅 19:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=cFkm0VGcsXKSDLmkTjp-PQfl_qFeZSkNae1KNHdjLbF5YQxv6EV9AZMKmKfM73Xl8FXLwXIr7f-fnXq4tZUmrmY8-_AheAJrM6IVuHISXY_2tLQlfEFK6285SZIg2LgKH7rKFXHadPQCnUR7c12s2NWQIeJvfteql4oLdkuNn0_XwpR5WAfUTwbVCn_NTCJP-bsMlXCWH3AV6J7gDCT96gaHW1XHN7EsIyXo8nkkJqAuS3GaGAUq6lUKFHoPjwGXnpSPAFUg4Uzrte2qoxefWhTboIUElycvIBAELEVKptUznYuUc1-YDsKBaidlopK9JBZ2zQnbkBzyGEztSI3S4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=cFkm0VGcsXKSDLmkTjp-PQfl_qFeZSkNae1KNHdjLbF5YQxv6EV9AZMKmKfM73Xl8FXLwXIr7f-fnXq4tZUmrmY8-_AheAJrM6IVuHISXY_2tLQlfEFK6285SZIg2LgKH7rKFXHadPQCnUR7c12s2NWQIeJvfteql4oLdkuNn0_XwpR5WAfUTwbVCn_NTCJP-bsMlXCWH3AV6J7gDCT96gaHW1XHN7EsIyXo8nkkJqAuS3GaGAUq6lUKFHoPjwGXnpSPAFUg4Uzrte2qoxefWhTboIUElycvIBAELEVKptUznYuUc1-YDsKBaidlopK9JBZ2zQnbkBzyGEztSI3S4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک مرد مسلمان چاقو به دست در محوطه یک ایستگاه قطار در سوئیس موجب زخمی شدن ۴ تن شد.
او با فریاد الله اکبر دست به این اقدام تروریستی زد.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5173" target="_blank">📅 14:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=GLryAkYNfN98oWN6HiDjsPqh1iTGY176UAMdZOiNjvgSj5tWMjiThoZ6QymMfUd3ipcozjtXWHxkbdD_VK9y6ew_-kI5S6yJeDdzVjVoNxUCSBIsldlh14gfE8spVvNGb_t9DSdemxto7jyuDSP1kLjke8gwohlYid6ufphF0L2ivfSMyooZmDBbU6WUi2rlnMN0N4QnDzLUfv4f_rwGfBQ0_5Ox8C_BvzptDOD89fYzH-dq-Pmhkb2ODscqF2Oyb1o4hboJHGtgxbgeGQFNxts7l708vFSk9MlzhFoJxCkt-F-xPF9nSZD2Q7VzerprlHBnTZpBnI94d7zPx2hAmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=GLryAkYNfN98oWN6HiDjsPqh1iTGY176UAMdZOiNjvgSj5tWMjiThoZ6QymMfUd3ipcozjtXWHxkbdD_VK9y6ew_-kI5S6yJeDdzVjVoNxUCSBIsldlh14gfE8spVvNGb_t9DSdemxto7jyuDSP1kLjke8gwohlYid6ufphF0L2ivfSMyooZmDBbU6WUi2rlnMN0N4QnDzLUfv4f_rwGfBQ0_5Ox8C_BvzptDOD89fYzH-dq-Pmhkb2ODscqF2Oyb1o4hboJHGtgxbgeGQFNxts7l708vFSk9MlzhFoJxCkt-F-xPF9nSZD2Q7VzerprlHBnTZpBnI94d7zPx2hAmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله هوایی اسرائیل به بیروت
🔺
آمریکا از دولت اسرائیل خواسته بود تا به بیروت حمله نکند
🔺
گفته می‌شود که در جریان این حمله، «علی الحسینی» مسئول ارشد موشکی حزب‌الله لبنان، که در واقع یک عراقی است از «فرقه الامام حسین» از گروه‌های نیابتی جمهوری اسلامی در عراق، کشته شد.
🔺
اسرائیل دیروز هم در حمله‌ای به غزه، فرمانده تازه منصوب شده برای «گردان‌های قسام» (نیروهای نظامی گروه تروریستی حماس) را حذف کرد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5172" target="_blank">📅 14:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">علی الحسینی‌ از فرماندهان ارشد و مسئول واحد موشکی «فرقة الإمام الحسین» حز‌ب‌الله عراق در حملات امروز اسراییل به لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5171" target="_blank">📅 14:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHHO3OVSkrcLte4PCeX9jCZhaUZY4sqEJG_ifzyur3T6m-p87mdXd5uMV_whsOt27Ea_2hUYjza73n1fV-LU-whEUBkNAPAuHnpjOkNZ6Os5ABRfFkJ5RPywi61vk045ryzswDhLk1qNCyXt2TZ7YDhyoCDDvNUSRBGxAMeuKucPKRfDgz6ebaEe20HzJgURnXkrhRNsH4W8oWX4ra1s0r1XsNqSxHh9AT78tfHpmeCtaKFBAgweu_Exyu3dIlnKcho6T3EZrlHj7tOAKCpvczW6Xnd1EEd0hhEgAQZnhZd8A6jvuvzr4wdBqyk0-ZMEO7c3KxtsrBcxUK7GxAUXJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام:
ساعت ۱۰:۱۷ شب به وقت شرقی آمریکا [۵:۴۷ صبح ایران] روز ۲۷ مه،
ایران یک موشک بالستیک به سمت کویت شلیک کرد که توسط نیروهای کویتی با موفقیت رهگیری و منهدم شد. این
نقض فاحش آتش‌بس
توسط رژیم ایران، چند ساعت پس از آن رخ داد که نیروهای ایرانی پنج پهپاد انتحاری را به پرواز درآوردند که تهدیدی جدی در تنگه هرمز و اطراف آن ایجاد کرده بودند.
همه پهپادها توسط نیروهای آمریکایی با موفقیت رهگیری شدند.
نیروهای آمریکایی همچنین از شلیک پهپاد ششم از یک مرکز کنترل زمینی ایرانی در بندرعباس جلوگیری کردند.
فرماندهی مرکزی ایالات متحده و شرکای منطقه‌ای همچنان هوشیار و با تدبیر عمل می‌کنند و به دفاع از نیروهای خود و منافع‌مان در برابر تجاوزات بی‌توجیه ایران ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5170" target="_blank">📅 14:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=Zen3VEcbODgzSHo7L3r1xPhTYW-Y5XG68HkY1O_4TNFi-xMwql87rbbnGppm5-UTkZqmtTcMkTjD_6uEfphoVj5npdogV9wq-s2X30-S4yLjd4Lxf_cIqSd2qBdnc3BfJTvjCnKNOl0R_V-vGC5vY45cIWJYXHxTR_Kolk-2ueRaCqYjIdXuUmC9_jTt_A-T4z5z90jJdyqWBK4QxqRiPfoAOo8xX0wzIiYgFHKAFU3RPEyYdSbrQyVjUgb3DR6KMWedV5cyCutSMpDkmpPCRcteyWj-4wnY2VJyd4DuANX9hBv_anNh-gFLbxYIWfadKzO2Ol49kaM-a-rmqoRhug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=Zen3VEcbODgzSHo7L3r1xPhTYW-Y5XG68HkY1O_4TNFi-xMwql87rbbnGppm5-UTkZqmtTcMkTjD_6uEfphoVj5npdogV9wq-s2X30-S4yLjd4Lxf_cIqSd2qBdnc3BfJTvjCnKNOl0R_V-vGC5vY45cIWJYXHxTR_Kolk-2ueRaCqYjIdXuUmC9_jTt_A-T4z5z90jJdyqWBK4QxqRiPfoAOo8xX0wzIiYgFHKAFU3RPEyYdSbrQyVjUgb3DR6KMWedV5cyCutSMpDkmpPCRcteyWj-4wnY2VJyd4DuANX9hBv_anNh-gFLbxYIWfadKzO2Ol49kaM-a-rmqoRhug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسلام یک دوره کوتاه از رشد علمی داشت،  که همیشه هم سنگش رو به سینه میزنن،  ولی حتی اسمش هم گویای همه چیزه!  «نهضت ترجمه!» رفتن شروع کردن به «خوندن» کتابهای دیگران!  کتابهای ایران باستان و یونان باستان و هند و روم و……  خوندن و ترجمه کردن و شدن باسواد !  اونهم…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5169" target="_blank">📅 10:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4d9UlUUVax62OvJRcMxyOedY--2KU7LJxIdCjFeFtKjwKb-7L3C-mbb-FgBT_G-bHSwrQ3OrIf69t8H2fGXzK5eIPZSFxBDBFI9w9D-VZSJbSVLYL9U0PXxmr-yAu8xvmalq0FgLaK-domwTSWYACKEGlwvhV9oI0XIhmj23FXRlyncRai26wvsZiVlxQtO4p2JXiNhderXCxyA9oRX7u9t72VT1BbarHL-cxt-GNTLODcb5d5QFHD0KcRqGasH1q8i1fpdidSECcsN1skV1oN2RWcumR1HVn6g95c3cck88kCLNdbAWVFO-0xaJFnYInMH4pHhgfnqR3y350nCUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !  جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،  انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5168" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5167">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=Y07XfelBELBy4q50RQLnDtG_gmhTaO0v0FOzyWb-vOMvHv1yke8lAKkBA25yLl_Q6Ecj5qpbSvv4tt_JgygZqmPjlcQQrI2jiVX1W4b1t9SMxPHK9CD4i_ZLFpPxIBF4-MFuzdpH16_ORUY92Rr84k3It_EmrNkiquZEBOP7VxC386BGILezf-RcffUZOxgkhMgGeNpRs8VqOI-ECxZIY620v618oJl3HrWQ6B4JnOUdZClKQSnCTJs2bohsjC0dRAJyBvDYIXK1VLR72BUDd_knaQyY0-4eYR5yYMHOrUKCQJoU9cNyetufM3mVGwKi5yr5-Lhne2soWciOvX0Pqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=Y07XfelBELBy4q50RQLnDtG_gmhTaO0v0FOzyWb-vOMvHv1yke8lAKkBA25yLl_Q6Ecj5qpbSvv4tt_JgygZqmPjlcQQrI2jiVX1W4b1t9SMxPHK9CD4i_ZLFpPxIBF4-MFuzdpH16_ORUY92Rr84k3It_EmrNkiquZEBOP7VxC386BGILezf-RcffUZOxgkhMgGeNpRs8VqOI-ECxZIY620v618oJl3HrWQ6B4JnOUdZClKQSnCTJs2bohsjC0dRAJyBvDYIXK1VLR72BUDd_knaQyY0-4eYR5yYMHOrUKCQJoU9cNyetufM3mVGwKi5yr5-Lhne2soWciOvX0Pqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !
جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،
انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره و مفهوم «شهروند»، دادگاه و وکیل و حقوق مدنی، پزشکی و بیمارستان مدرن، بروکراسی اداری، مفهوم حقوق فردی، مفهوم و ارزش آزادی بیان، مفهوم دولت و ملت، سرشماری و شناسنامه و داشتن فامیلی و..
صد مورد دیگه!
مسلمان‌ها در دنیای جدید چی داشتن؟ هیچی!
هیچی!! لباس سنتی بپوشیم بریم توی خیابون هاشون نماز بخونیم و بگیم خدای ما از خدای شما بزرگ‌تره!
با نخوت بگیم ما خیلی از شما بهتریم!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5167" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5166">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
سحرگاه امروز ارتش آمریکا به ‌منطقه‌ای در اطراف فرودگاه بندرعباس حمله کرد.
سپاه نیز در اطلاعیه‌ای اعلام کرده که در پاسخ به حمله آمریکا ، پایگاه هوایی مبدا این حمله را مورد هدف و حمله ‌قرار داده.
بیانیه سپاه اشاره‌ای به محل این پایگاه هوایی آمریکایی نکرده.
اما خبرهایی از فعالیت مقابله پدافند هوایی کویت در برابر حمله پهپادی منتشر شده.
🔺
برخی رسانه های حکومتی نوشته‌اند که یک نفتکش آمریکایی قصد عبور از تنگه هرمز داشت که مورد حمله سپاه قرار گرفت و در واکنش ارتش آمریکا دست به حمله‌ به اطراف فرودگاه بندرعباس زد که ظاهرا مبدا حملات بود،</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5166" target="_blank">📅 08:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5165">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ  به PBS News: «جمهوری اسلامی غنی‌سازی را کنار خواهد گذاشت و «هیچ» تحریمی هم برداشته نخواهد شد. هیچ خبری از لغو تحریم‌ها نیست. »</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5165" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrqIJDm6-oAzhpvWM0aEbUrxCX6K9Ik3luFfCJDxn7ulX25qu9oGWOgtlQByih20QL0Jieu87xkO8drfJETRewlhw7MBbUHv0VDFRNQdz1cUfv3azeSg4fm9u_-3eHVGZ0OtnNY-jZ41MQHUdBIGTQ_1m49xfkie4E7jZij94fwamKgW2oEyrsNIl4tEO-RjiFr2qecjGB179-Q4Ab5qqb04JF1XpVOAmthoB3TSEjxu7HwqOpiXknOd1ZqU901ZySIUd42xGOaMsmiLziEVJDkoyCL3zHNyHifRAbtnTL5qju5FJGVGNB66MjkogNRl2iIMZ4BAvhxshe6ePKBiBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۳۵۳ سن  حداقلی ازدواج برای دختران ایرانی از ۱۵ سال به ۱۸ سال ارتقا یافت.
جمهوری اسلامی اما سن حداقلی رو
به ۱۳ سال رسوند تا کودک همسری کاملا قانونی بشه! جمهوری اسلامی اما ازدواج زیر ۱۳ سال برای دختران رو هم مجوز میده.
فقط باید دور زده بشه، اول صیغه جاری بشه
بعد برن دادگاه و قانونی اش کنن! به همین سادگی!
در بهار ۱۴۰۰ ، حدود ۱۰ هزار دختر ۱۰ تا ۱۴ ساله در ایران شوهر داده شدند!</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/5164" target="_blank">📅 12:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZYmbwaOh_cU30sUtyw64zsRftpNXHbf9kEs9_to1UNR05xGWOnAzBDo8N-BlzGklbmwWRgwTrbIJ8X9BUVbEhTQKvZVFcgDxYEr0SpCA3NvxBJio0xaqhHxv19O6mtpaOfCKS_mlE0S3z_LTgf-R-4ce_iYrW_Um60FygSZGEiRTMf0iheX04Lmjzn4TXnbuk1ArfS4L44bcdXsegxgHRDpfYC-xhSgAhZFIJy1Je5Tnk83EDYs0XY9k0JdJJCyLydUiJ_5cLTdRNPWEBpNORlh9fYZFFCUyLSlpSsPWAupkioQIlW0j01sXnJjSFJ9AAI2271HjKqQSP8SkgqGyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5163" target="_blank">📅 11:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMT38qYT28xri335eMvPIuTD3HZhRaX8bwr5EBqrX57gn6QWgvPK9S2h-qsa9TIa2RZw9q5S784jTu-7hWqsT6frOpOWUjmcJx3jijh3JQAWSDaOzxC696ZQJgm1CKcLvsbSI-FWxxl2NGECgwfUPci0pdw9l7rYckHPqAH9cEkbGtkOszHZBU-a2Yl_7xdXPYtv-6-TrgCt9UWyYlUyMQNU58yU3p0tSPv1q90baCkbB1WWr140u53ZHOGjr_H0_CwTQmfTy0-uVv3ArqRRkalvw5lx7OYx5Il7WdGfL_Tqf44ufhVpaPSos7I_VK8cNsvTrPUeLaC_1ifOlNaFeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه هم که فکر می‌کرد زرنگی کرده و با حاتم بخشی از خاک چکسلواکی، کشورش را از ورود به یک جنگ رها کرده، هزینه بسیار سنگینی پرداخت!  به قیمت تصرف پاریس به دست آلمان نازی!  آلمانی‌ها دقیقا با سلاح‌هایی که  از کارخانه‌های عظیم نظامی چکسلواکی  به دست آورده بودند،…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5162" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKPxtpg_0vKDIAycvS3Y21OLZMQlaGL2yb1bWAaSqPrxHX-YBMWCC9QCCuS0heu8ebzB6pPDNT6mqCCfybHQ2U4vTI8Ld3bL5IieK7zZEGcVW9GlMrJaSoF_OKh8ntuLti6mPK5tC4zBkSQmIRmyi7369VKPvwRmX0vUCrchIfYGCcdDq0lZ0LSPYr7MX3ssy3BQsg6R-XorD8YHDw0xdCtgJoOZHyximx8IUrxFJtj6sKKh54f1vlkpGOsPuDxjnJU2PD8Cp7-0anxiuoSZMPlACzw-zb3a1Q-kkLBB8BouNnxnQ5LTYg9NMKy6h_Ov6JUYeWwX2Y0-fDjdhxziBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرچیل اون موقع نماینده مجلس بود.  دولت چمبریل رو سرزنش کرد و گفت :  «به شما حق انتخاب میان جنگ و ننگ داده شد. شما ننگ را انتخاب کردید،  و با این حال جنگ هم خواهید داشت.»  پیش بینی چرچیل خیلی سریع به واقعیت پیوست! آلمان این مناطق چکسلواکی را گرفت اما دقیقا…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5161" target="_blank">📅 10:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWOjdRnkHdfQl_r1lPFbFgo-tAIn8eiOLd5fw_ryGkba1o9hCWgN3AzYz9iZ2RhDGteEsi50SQn8hYyaCfBKjjIiLaP3wFL6NYZJbpeD50mVLfA987ECrHoWDFDcCg6ezzzwlXN89PHtgMOv6_-O5MMKxyrgWmH0s8TJ059JTq_qCVahe8d14NBgVItQSDOwTnj-4QEhBIu23oocK5vwhY_bt3UTiOg8qig05mec3hYaHp__LyCRdD8kqlRJgL5_TovBpNHVRAPv5eAm49KWdRPFDleM6adkSLqC_h8H3BQIJArmZ-rD1KJc30Y9HX30k3_vKtbVER47hnVtIFoGZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمبرلین، در صدر دولت بریتانیا،  به همراهی فرانسه، قراردادی را امضا کرده بودند که بر اساس آن، ۳۰٪ از خاک چکسلواکی به آلمان نازی داده می‌شد.  مناطقی که مردم آن آلمانی زبان بودند.  هیتلر میخواست همه مناطق آلمانی‌زبان در آلمان باشند .  بریتانیا و فرانسه، عامدانه،…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5160" target="_blank">📅 10:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLuk8yMJbOulXs-U51a5X6RQqFVZickSAPzYxDKQBoM2SmQnaCQyiPBdcL3TlPVqdIJ8f3TY5YSF4GfsivMiTfgv2lS5BtxAjr2NfFtKhefX_A59GAJWDCZ1HYL8xDAiEyDYryPbb1jxpMi6kxXozSdIcijSxAIb1DgPprrwZeDSUwKcCfsEOgXyWMinct_R8Ug2b8C4KzCJwoMYAFnNubQnl7FZVjlSwqCuYSgLHgnjbL9YDQF13NXqZ_9RJUYZzyZBoZdrvnFiDIWrTH73-ZOHFBaIA5a_4a8FaWN_UXniq4b-9TlrkrbhypzEZ0IVUbXjUAbm0xhveBCipZw7kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس  با این تیکه کاغذ به لندن برگشت. کاغذ را پیروزمندانه به خبرنگاران  و جمعیت انبوهی که جمع شده بودند نشان داد.  او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5159" target="_blank">📅 09:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZTCrK29EAlFiBAZxz62PeECehz6MuBOmKKpzZXjqAHoq_7EIXFVbsd6h4GZ252SQ9I0QLNZ3eQVDkYsVuGzePXi5r9i08j9y7Vc66t5o6QqgdHpFhYrpnmRxGK7771CLf-MpnxJTFex7Q0Uwcw-ceP4X-IwklDQx9TawNeHznu9dtx7jeDJ4xphy6j_QwloJySEYdlOxQIQPCJvQwZL-5zcJWJVCvP18nEs42GrS44ZV24YO7igr1fXyzde7-e1aNjX_WFaZWy3yxTrFVDGzmB3yTaFUJ4qqlRJMkLDM_qH2ukA1iScxyGSC3OP95brffpGiRdteyt7KizeDTh4JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس
با این تیکه کاغذ به لندن برگشت.
کاغذ را پیروزمندانه به خبرنگاران
و جمعیت انبوهی که جمع شده بودند نشان داد.
او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات داده. این تیکه کاغذ اما یکی از «خیانت‌بارترین» قراردادها بود.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5158" target="_blank">📅 09:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5156">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyrL7qejrwwmCN14L7sl_1QXBURvD2kYvYNUnj4M7nehjBvy5umHIJ_PEcvYTi9WGCdyPAoLn915LbPKELaiL87YUEhoCx_jjoHqAKwhjOujspDECoG4qbhUrwMN1ypt2cPbDN2oY-mBQo4hC5-IlFJGKEKyX-WSZCgIwtwhEQVy7Lalc4T_rXQewGVmim9gmzgYd08xll7evog9bql3UIfZCwpbysFifG5izSSMQ2un7Jxa1aafepkzZ7Vp5Ix0JKE2EJL0dnSuQvb3k3BHrDMwm4pQbnzu-Rlr2e5BV8bK37xs4Tb9BAXApEERDEY3Nn98fU5poWH46ZmwA_N-6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما دیشب بعد از انتشار خبر شنیده شدن صدای انفجار گزارشی تهیه کرد و گفت : منبع صداها مشخص نیست!
بعد صابرین‌نیوز و خبرگزاری دانشجو و… حتی اسامی کشته‌ها رو منتشر کردن
بعد سخنگوی سنتکام رسما گفت حمله کردیم و زدیم و…!
دیگه صدا و سیما در همون مرحله « منبع صداها مشخص‌ نیست» موند که موند و داستان رو ادامه نداد .
«مصلحت» نبود!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5156" target="_blank">📅 23:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=IQeM6mJlSyqD4x6J4cTxa57-KUr6jYNT65727Y7Z7btirwibuAuAKjiRBJmnD7kpj8tav0HkQHL5uAQac1gxRaT-spXXZR6izuK6TqAN_n3LG1dudinxWqMLGiquFkr7ADe8unEfQb2qbnWWe9w5K9Z0boDV_p5p8x7hVUxou-XPs_zPtZYGyi55bk1gKFrrJ8BcEum_GhVkAyjtZK2VpY7FavLgBlvj8QWqMjNvIkSKXmi9CDGuYT3qL0H8H9z0zJfDC-mSpUxiRnxbgnh3EqyqIf0QJtoMAzFvcbUUXa9tEXckAIWDZAR8y5R_h2mPKh1ChAmjekhhERG-HMpAjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=IQeM6mJlSyqD4x6J4cTxa57-KUr6jYNT65727Y7Z7btirwibuAuAKjiRBJmnD7kpj8tav0HkQHL5uAQac1gxRaT-spXXZR6izuK6TqAN_n3LG1dudinxWqMLGiquFkr7ADe8unEfQb2qbnWWe9w5K9Z0boDV_p5p8x7hVUxou-XPs_zPtZYGyi55bk1gKFrrJ8BcEum_GhVkAyjtZK2VpY7FavLgBlvj8QWqMjNvIkSKXmi9CDGuYT3qL0H8H9z0zJfDC-mSpUxiRnxbgnh3EqyqIf0QJtoMAzFvcbUUXa9tEXckAIWDZAR8y5R_h2mPKh1ChAmjekhhERG-HMpAjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا دبیر: کارمندان بهایی من‌وتو می‌تونن
در صورت بیکاری، تو پارک دانشجو مشغول کار بشن
مدیرِ تراز جمهوری اسلامی</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5155" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1Asu3HO69oJbEtGOf8QtOOJwInlaBvi5bR867IOl3dUqlvgGw0Ez51SDlUFMOIoqdzRAF-XzzSu3l91QDXDRsW9D7tv6r8tZWs4e43DtvGLiJ69umA0YfJgwWjvS-VPz1KsuiG7LeAGleyzVe-aWr5Dp6cMgIeSWbmmhif7X1IO_3o8RHIjm4ibk9U7yYQIcCkG3nkO3Te4NtWgJMwg7bTBoaVO3HS9UX1ttt3GN27xEfZuJllGPp3JHvqd2vFyjnLm7aPeq2COk1gSf6QHGyF3RSRia_i12ICXRoafdI4yGNArpYcHpiw57HohLy7bNbfRDtO5MDCgJD2bELEB3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاریکاتور شارلی ابدو
از قصد جمهوری اسلامی برای گرفتن پول برای عبور کشتی‌ها از تنگه هرمز.
آخوندی که میگه : به نظرت
چقدر کاغذ توالت بهمون میرسه؟
اشاره به پول ایران و بی‌ارزش بودن
ریال ایران که ارزشش در حد کاغذ توالته.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5154" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‏پیام منتسب به مجتبی خامنه‌ای به مناسبت حج: رژیم منحوس صهیونی ۱۵ سال آینده را نخواهد دید.
باعشه!
بابات هم همین‌ها رو میگفت که باعث شد امروز ۹۰ روزه که معلوم‌ نیست هستی یا نیستی، اگه هم هستی طوری قایم شدی که گویی هرگز نبوده‌‌ای :)</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5153" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdNn51FMa9cAa1mmt0HFFnbbOoRGSq3ieg-1Y3pOKD4MIHD-N6woaYhRUlSAQALXEgwD0eu2ociCxz-ZLJCwgJiVUN1yQ3UeAIckY8KOcqvV9RVeTLYQqNHERMPnRD6ABAhjR5yaL-P0MsaDU6X6hV7KsDR5AERBX8OCjPzMDVCGEUukWz4wi0U2yLPBi8MwwUqStXo2HznCVZGdcMT3vHhiocVxeqHvtRs1nMNKS3B5-pPifd-1jfzxhai-eQbStpPW1J4UCtQE_dleE5yX-VeJ7I1NKZ5clDxI51L1ZSoj4kwDwJB0VBikUpiU3W7hsk7Q2rS8RLRDq215lIdlEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذوالقدر دبیر شورای عالی امنیت ملی، میدان جدید رو معرفی کرده که هیچ کس نباید حرفی بزنه که وحدت شکن باشه!
دستور خفه شدن همگانی تا رسیدن به پیروزی!
اسمی هم از مجتبی خامنه‌ای نیست.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5152" target="_blank">📅 05:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVoEY_Uuy6xNA-10QDKNL0q__op4QYvS6YsYPYeBtSFUR52CZGhAUU64sob9dpEnaxpC4W9Fn3xJNXjrgXneZg0LCCLK-5qecDwwzvx11J7XP6WX75BkVg7bsMsv6ldCDpeMjnW4GnJRMWJ2SnabjOko6KU4qoI79fMexxdjTyPXmp0XZkk7z2OdZmiDiMAUbSp0WD8wYVvtZaZiNh2Kwjcn1hUTCNyY72Hyuu1gh8jw8R0L4ORm8XoRX5REhoRv3XKa22SKsZDZWGsxJ6HTQs98WO8ilWStXP5F92qSmH6VlTkRHu0ekSKhDuxQ2YtmNxq6Rymm2Nyf7N2T7UPHbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه.   سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است. خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5151" target="_blank">📅 04:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o43rjdPlagDtX6rvkGcasa0FrwypNPzMlgnRG0Jex3PYMSGkf4xbNBhY_r3h9rfxHSGgTw-PW4C2W5JyQBfLvJdgVhKp8uHPaMx1y7rMciNairkxkJvgZ21MnCF-hbkOb8ONxPs5-3sefDQERmmaMWcOXbRas-CV8YYsHf6gr9xtQUa59XuP4kXRZSo8wJVCVW6PZqtxQj6zXsYcqdUJevwsljiAhTR69NQlBqBZpKK5iQpVn_r-QIkU2-37r8TbUhMu2vHGB3WYFA5AzVGN_4J5g4DKHWJwJGCwwahgao4buU01xNN8s4q-wv9gc2o4_1s62btUySBt6EF-EFPoKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه
.
سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است.
خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها را نامشخص اعلام کرده اما اسامی سه تن  را نوشته.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5150" target="_blank">📅 04:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ : یا یک توافق عالی برای همه خواهد بود یا هیچ توافقی نخواهد بود.
اگر توافقی نباشد آمریکا به جنگ بازمیگردد.
کشورهای منطقه باید عضو پیمان ابراهیم شوند.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5149" target="_blank">📅 17:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">قیمت نفت : ۹۷ دلار</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5148" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWR_NnEO12BPO1HlMA9xIOJ6PBNFZxk7Ngc2tRV1kRYqZlwBH7y_tLXB2bMCPc8KY0Pp0-pEPhOg_YtLT5RxyPT4tlHD1WreOHAOFDRWXc5jYrg0vZrlsOmOlKjo90BMNp_W4sXKHwfvn3V-bgEInSDLnM1Vz6Ek8LiriPymB0n1yUn9iCs3Zd6gGIfBBnCTAE1SAy6eSlw2QL7e0PvqNJrzJZILyhA7yZRCPZxhQyoF3wK5FPpaxBi2mXsPogMcM0xa1kZP1C25DyGVuXAMdrNPLeRF8IQBovts_ZoLhSfOej0PQoKkSkEvfTWHSh_rXcEsgwEBWgeSctGiPLE1UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که صدا و سیما شیپور پیروزی میزنه و از موافقت آمریکا با هر ده پیش شرط جمهوری اسلامی میگه،
سخنگوی وزارت خارجه امروز گفته : کسی نمی‌تواند ادعا بکند به توافق نزدیک شده‌ایم!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5147" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔺
بقایی، سخنگوی وزارت خارجه:
آمریکا به عباس عراقچی، ویزا برای حضور در سازمان ملل نداد.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5146" target="_blank">📅 14:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b6861470.mp4?token=NZe2XrdpNdvJigz7Iq5xCcMtx2NQIZBht8YseevLQ-HA8L2XlMjQME_b7VWpwKszn4ucj2wz1oL4wwi4S40tnRd4QVMm5hNiE4pfOo8vZ6PQr1QJR2iNShOV6lt46VUUy4hJExmCUZr0-KZ_5PaKuHWWcaDwP-BP84qcZ_9GokQ-ZKu3BKm7eS6iJ7S0-84V307_weJYjtoIWUfgjSZseY7fCD9qqC3rdr_n5IWLHDzYX18BPWLcWmJ0Djthx_AsDTx0c0knVxo-cGLyd8wu2k4XbnqfBWOILnhNrlYd77PJXuJ3mzG_ddO9Yq5q0GSJ1cNd07Wxb_Cb15wZ0cTnOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b6861470.mp4?token=NZe2XrdpNdvJigz7Iq5xCcMtx2NQIZBht8YseevLQ-HA8L2XlMjQME_b7VWpwKszn4ucj2wz1oL4wwi4S40tnRd4QVMm5hNiE4pfOo8vZ6PQr1QJR2iNShOV6lt46VUUy4hJExmCUZr0-KZ_5PaKuHWWcaDwP-BP84qcZ_9GokQ-ZKu3BKm7eS6iJ7S0-84V307_weJYjtoIWUfgjSZseY7fCD9qqC3rdr_n5IWLHDzYX18BPWLcWmJ0Djthx_AsDTx0c0knVxo-cGLyd8wu2k4XbnqfBWOILnhNrlYd77PJXuJ3mzG_ddO9Yq5q0GSJ1cNd07Wxb_Cb15wZ0cTnOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمایی از شهر رفح در نوار غزه و پیروزی‌های محور مقاومت
قبل و بعد از  حمله تروریستی ۷ اکتبر</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5145" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل - توی این مایه‌ها -  گفته: «در پاسخ به هر حمله پهپادی انفجاری حزب‌الله، باید یکی از برج‌های بیروت رو هدف قرار بدیم.»
حملات حزب‌الله به اسرائیل رو یا دولت لبنان باید متوقف کنه، یا اسرائیل.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5144" target="_blank">📅 13:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQ_4yKP6EGWV8NcaMX4F1pXN6GGa82qvJneM2YhnJkKy7Fj9y4JQsk8qFyFQAAc37JvepAcFjQKqv9Zf_AoIf0IPzDCLJ9SECMV_9zrqHnzuIWWScUZKv1uC6juNEODQ1mrx5B_JclyVZs8dgOY7PR08j-Y-dGDeRrVcJ7okSU00FXGLcd1bVt1FdKnmBJfBH27jzEHFgxWRDdYfxqAPKRu1bZY5y9lvJgJtkW39fndUDgj2AcmnViXL4o9qECnb0t5MjdZyrPuOxSjJdAjsfxTDNZngZfN6fGWogtSaTdZw1hjCH88sgTgCCo_1MN4aYoL-PfA4OozoX0L4vdgiOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح در ایران با اذان و با اعدام جوانانش شروع می‌شود.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5143" target="_blank">📅 11:58 · 04 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
