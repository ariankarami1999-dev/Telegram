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
<img src="https://cdn4.telesco.pe/file/uDgRk0cUxHiBF8KplU6gQyb9TUhTCFI3U-l7ys37VUNsc7pgPvLRBtjPzzpMwxIrg80w0-30v7BcnZwcBGk2l82MeKQXNHBrXjYxaRBHruV-wZ_1zaI84ZOUv9vDLaOaEjNPjIw9hpeqeeYlPjruJN6XOty3B7c_e_qLy_LCqALfRuHZ_6EulgIp6r8FDEsEPscPXvAi8HYoHWIor3Sv6FllgqPTK4Mr4UXf3FQqtl572KQzAdor-A0LIGRx4_7SJws9skZ2OEniOTk20C0pC5kM0-rgRSnV0i92MJbkq45goSi-MaMi0MZhkqgBPG_D3uGk_sEr3-I2ruambKa6sQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 264K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 02:39:50</div>
<hr>

<div class="tg-post" id="msg-92775">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دوي انفجار في مدينة عدن جنوب اليمن</div>
<div class="tg-footer">👁️ 255 · <a href="https://t.me/naya_foriraq/92775" target="_blank">📅 02:39 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92774">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇺🇸
🇮🇷
نائب الرئيس الأمريكي:
على إيران خفض قدراتها على تخصيب اليورانيوم لإنهاء الحرب.</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/naya_foriraq/92774" target="_blank">📅 02:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92773">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a856499b5d.mp4?token=u1fO0It6ygC6s4rrds5uKmT855JEDqKOBDEt69PxIBeN45Y6eUi2KSo8-YnJeGXidjwL-Jbw03rEgXr0ZWqHHgvFQtI7ICOmGOr3Rh80uUd8tm-dzk-n0G9z_PRer3lfOSSi1O-SVSTx-3m9sfFwK3X-KDkmxTos1zN_SFUS-5syXjAA3e9UECVuyxxmKsZGlynPf6G3ViRvp34wg_7G0EEcp6Yy0PIesCbrWxBPP6sMo7WQ4tiPr1kEtthQ5vCslCezuD4oDfmLa3tmj0k_BN5kqUYCnKtTupJE4HS7kxsP9ADy09XqqoXbG4bCtEnShlzIrwsc2F-Fy7dqsP-JM384R0OOXkhpwK1REpou184mQKmO1ucdVVFLgitj6t_nB7xVzva3DdwUkOc6PXf6RFIy7bHRLA-xFKTMJE1-uQiomGq64hVH1fnyDXADGq4ITZTGoEEbYyB0wPMNkhpULA2xMzITJCyNp7R-SiCWaxn-T3XRL0NzZ-_kZ_TozCUo4VSknYrfulWAcYjcnStSzXN2UY0udEQuXhTLnplQC73tUFmaaYa3VFpos6kDYrXlXxtUq05-qqijw1t93U4v1JffADgRom8-ErDhWcAT6-k7M9qWqTXJTqJppeA06cSpyEeKKoBZ168GPJCfs_H1x_nYrdHk9jizWNR-KD0ic7c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a856499b5d.mp4?token=u1fO0It6ygC6s4rrds5uKmT855JEDqKOBDEt69PxIBeN45Y6eUi2KSo8-YnJeGXidjwL-Jbw03rEgXr0ZWqHHgvFQtI7ICOmGOr3Rh80uUd8tm-dzk-n0G9z_PRer3lfOSSi1O-SVSTx-3m9sfFwK3X-KDkmxTos1zN_SFUS-5syXjAA3e9UECVuyxxmKsZGlynPf6G3ViRvp34wg_7G0EEcp6Yy0PIesCbrWxBPP6sMo7WQ4tiPr1kEtthQ5vCslCezuD4oDfmLa3tmj0k_BN5kqUYCnKtTupJE4HS7kxsP9ADy09XqqoXbG4bCtEnShlzIrwsc2F-Fy7dqsP-JM384R0OOXkhpwK1REpou184mQKmO1ucdVVFLgitj6t_nB7xVzva3DdwUkOc6PXf6RFIy7bHRLA-xFKTMJE1-uQiomGq64hVH1fnyDXADGq4ITZTGoEEbYyB0wPMNkhpULA2xMzITJCyNp7R-SiCWaxn-T3XRL0NzZ-_kZ_TozCUo4VSknYrfulWAcYjcnStSzXN2UY0udEQuXhTLnplQC73tUFmaaYa3VFpos6kDYrXlXxtUq05-qqijw1t93U4v1JffADgRom8-ErDhWcAT6-k7M9qWqTXJTqJppeA06cSpyEeKKoBZ168GPJCfs_H1x_nYrdHk9jizWNR-KD0ic7c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
مشاهد أخرى للحرائق الواسعة في مصفاة جدة السعودية التابعة لشركة أرامكو نتيجة الإصابات المباشرة للصواريخ اليمنية.</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/naya_foriraq/92773" target="_blank">📅 01:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92772">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇸🇦
🇾🇪
مشاهد حصرية لنايا.. إشتعال النيران في مصفاة جدة بعد إستهدافها من قبل القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/naya_foriraq/92772" target="_blank">📅 01:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92771">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81f2626a3.mp4?token=EIOAfFHP_5p2mJgJN2mvRtG-eZdoKgyWIiW-U3-vS5rsGipXDW865Kk29bugFl8tnS91yYnsjKJyOVTOpPaQLkZx9AciPwJsXi-FenGyaGppj1vaDn8KrP_F9HP4e5EFG83iZEz73VERSH321Y0A2ho8m4-dzey3BMzhpk1865HbFFFr_ekLaqdsLJYWqq9B1Yo4fFp2cdEjUGWJzYYXhRpMTfGpoKIuIPHmAKpwA5GYRCmOB30zinK1zTiylRuusnOQ2EsqqwVdgQW7RlbB-VCcl24_twKxi3ao6ktiH5-FLJcowCPCTdozRfhk8vrk4xJ9JADIUcSqDm8usnLK6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81f2626a3.mp4?token=EIOAfFHP_5p2mJgJN2mvRtG-eZdoKgyWIiW-U3-vS5rsGipXDW865Kk29bugFl8tnS91yYnsjKJyOVTOpPaQLkZx9AciPwJsXi-FenGyaGppj1vaDn8KrP_F9HP4e5EFG83iZEz73VERSH321Y0A2ho8m4-dzey3BMzhpk1865HbFFFr_ekLaqdsLJYWqq9B1Yo4fFp2cdEjUGWJzYYXhRpMTfGpoKIuIPHmAKpwA5GYRCmOB30zinK1zTiylRuusnOQ2EsqqwVdgQW7RlbB-VCcl24_twKxi3ao6ktiH5-FLJcowCPCTdozRfhk8vrk4xJ9JADIUcSqDm8usnLK6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
مشاهد حصرية لنايا..
إشتعال النيران في مصفاة جدة بعد إستهدافها من قبل القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/naya_foriraq/92771" target="_blank">📅 01:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92770">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromExplosive Media</strong></div>
<div class="tg-text">History didn’t begin on October 7!
Years of crimes. Years of plunder. Years of captivity.
All done by Israel.
Operation Al Aqsa Flood brought the dream of Palestine back to life,
and exposed you to the world for what you are...
Free Palestine
🇵🇸
✊
🆔
@explosivemedia</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/naya_foriraq/92770" target="_blank">📅 00:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92769">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ef29b835a.mp4?token=ikluoAuc1F1KqQn1AjzqWNULAkRXpHVxklGzbeupYbBA779lH60HJwwMXz-ItWHwumgrYb9Vym_0ZKITB71Dy9AtyZ51DueqWPcf5iIuG6Y2_WBiAJjg9Utmvrq0weGPdHHfk4Sj4HovNpn7-giE7txFuz0CPyQb3pX15YqZt4W_-HO_lA8gJ5xklzlH0z30m7p1qeOXQ2KP5KcqGTvPWn0F6IjnWYbBorFJ4dr9b8PV_KadkwSjKNYmL8XF6vEnomc_L9ezEuSEPB1i1PP2-LasGTOiCdABrMRlVThDI0rQKH2HqqvJSIIpxn8SmmvsyzU2WYD5kto-yOhLJVAjyQ1FER2fejkGCxdzacQOXYwtb-k6qrvkzl5BtJZmMSuSUYO1ZQlxeMiibb-7TPaPrU5Xd5SppmUIb8yVdmGQe-oDMa31SVSbhC1WwHIhLlRopNRLbQ9_zkwbJW6G3X4bdPp3y5VFIL2xDCRq78-NkFFWZVa3VTjUYcL3BVygpQjNvRM2odLSfcEjcMiztpkrZV2yJNDW321ePMbihWx_vRGiztBS_So0Fm0z8ylX7G45cQZUt5vUz4hJyD45F0DALOn3ghe6TK1iviL29rxCwUg4RiH4LI8VK1QE_fAHQ39MoHJxLTICSG-ch6Ksdv4H9EeVI-kHsFGKHNty_IXhxRk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ef29b835a.mp4?token=ikluoAuc1F1KqQn1AjzqWNULAkRXpHVxklGzbeupYbBA779lH60HJwwMXz-ItWHwumgrYb9Vym_0ZKITB71Dy9AtyZ51DueqWPcf5iIuG6Y2_WBiAJjg9Utmvrq0weGPdHHfk4Sj4HovNpn7-giE7txFuz0CPyQb3pX15YqZt4W_-HO_lA8gJ5xklzlH0z30m7p1qeOXQ2KP5KcqGTvPWn0F6IjnWYbBorFJ4dr9b8PV_KadkwSjKNYmL8XF6vEnomc_L9ezEuSEPB1i1PP2-LasGTOiCdABrMRlVThDI0rQKH2HqqvJSIIpxn8SmmvsyzU2WYD5kto-yOhLJVAjyQ1FER2fejkGCxdzacQOXYwtb-k6qrvkzl5BtJZmMSuSUYO1ZQlxeMiibb-7TPaPrU5Xd5SppmUIb8yVdmGQe-oDMa31SVSbhC1WwHIhLlRopNRLbQ9_zkwbJW6G3X4bdPp3y5VFIL2xDCRq78-NkFFWZVa3VTjUYcL3BVygpQjNvRM2odLSfcEjcMiztpkrZV2yJNDW321ePMbihWx_vRGiztBS_So0Fm0z8ylX7G45cQZUt5vUz4hJyD45F0DALOn3ghe6TK1iviL29rxCwUg4RiH4LI8VK1QE_fAHQ39MoHJxLTICSG-ch6Ksdv4H9EeVI-kHsFGKHNty_IXhxRk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
إنفجار كبير داخل مصفاة "كاردون" في فنزويلا، وهي ثاني أكبر مصفاة في البلاد بقدرة إنتاج تبلغ 310,000 برميل يوميًا، أدى إلى إغلاقها وخروجها عن العمل.</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/naya_foriraq/92769" target="_blank">📅 00:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92768">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية في مطارات الرياض وجدة والطائف بالسعودية.</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/naya_foriraq/92768" target="_blank">📅 00:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92767">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-9nqjLpkDkjI-u85-kviiMQJegzVT1tz6Qc9K8Nl8wfAihTITjftWweR1DrupDs8yJtghTrs0jIZPJwGCTmniUaf8Ahzgnb2t7KAYoXAmjQjpe_r25cLWg0esVfX9V7rKmi_DLvxE8itBxeQ25maBIK4U4EaeAvsql-cre5K4VdCV3IFFw7jANUhvRcExIKZ4k7uUIiCBl577usTrVoB_JYAs6QJUQ9twBf7ctHk1osqMFe8zZ97iK5cmt0igYGNXBYhkEu8WKq3UsqrqLwf5ODIOnL1GZKXa3Vs0ix_0eEJVjC_dDD2AXqvSioqBpczCaeiPRlbh1n1ExZx4OGsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
أسعار النفط العالمية تعاود الإرتفاع مجدداً وتتجاوز 101 دولاراً للبرميل الواحد.</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/naya_foriraq/92767" target="_blank">📅 00:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92766">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
الرصد اليومي لطلعات العدو الجوية التي يخرق بها السيادة العراقية.
الرصد بتأريخ
5
-10-2026</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/naya_foriraq/92766" target="_blank">📅 00:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92765">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6545acaa0a.mp4?token=ITNHKadC8fUwMR7xRPfyIMihJeqZJb7DlvP0wTiTptL3L7MKXYk2Tc247OkvkuKNO-c8Mf4Ib03lTrwKMnUNF1SGhl1-vimiY2jNNKFPoCt06vJymvOQBlpAby8AsQ6pUgyj6zq_Dqbm1D10h_R-j9466cCBC76RYgHikyMJpd_Lwd7YOGDfE-BUurXIZEkppL_c1UjXFr6l0ATgXpQYigvqHhEewDQAN8aHMBCrj1FDlL_tWHiQUj8jAjW_kJhN11Qi6gbTu0zEGu2FWLJJVOfbdz597xcVSf9eeRhSdSfO6fwb3Qem6GFvLyZLWcQrGeRAi8yMOBMO441IAPNCgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6545acaa0a.mp4?token=ITNHKadC8fUwMR7xRPfyIMihJeqZJb7DlvP0wTiTptL3L7MKXYk2Tc247OkvkuKNO-c8Mf4Ib03lTrwKMnUNF1SGhl1-vimiY2jNNKFPoCt06vJymvOQBlpAby8AsQ6pUgyj6zq_Dqbm1D10h_R-j9466cCBC76RYgHikyMJpd_Lwd7YOGDfE-BUurXIZEkppL_c1UjXFr6l0ATgXpQYigvqHhEewDQAN8aHMBCrj1FDlL_tWHiQUj8jAjW_kJhN11Qi6gbTu0zEGu2FWLJJVOfbdz597xcVSf9eeRhSdSfO6fwb3Qem6GFvLyZLWcQrGeRAi8yMOBMO441IAPNCgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: بشأن الحرب على إيران أتلقى اتصالات باستمرار من قادة العالم يشكرونني جزيل الشكر. قلت لهم: متى ستدفعون ثمنها؟</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/92765" target="_blank">📅 00:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92764">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf9a05a1e1.mp4?token=mEelLx6LcLQ0GiW3iMxIVUUJ1bWAW30wl8GYotV_MuXus7cYMfl-Ysx0tcLIiBztCpZROYQ7zqK8DC4aX0sYnPROEo2rlD4JA46ggej3HM8V-8lqNhdJccm75z-A_EqTO-R9apUF5AmijzbvF1Ph8Y3MigtrE6cqLG-tJ6nql_v32T2NPqhmQewA4F9d5A0JMRGa2LYJ3bz-pMfR-1VnI710FM_QP_XKShDjEZYrdmofERxB1uTX4Ws1UeToNOhCbH-lWZmAAIb39lBcpvq80sBf1bCEWSMXYJzuGj-EQCeTgrKSrlsDbWDoZVCSCcGAPjxKID4H6foHgamZIOOTVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf9a05a1e1.mp4?token=mEelLx6LcLQ0GiW3iMxIVUUJ1bWAW30wl8GYotV_MuXus7cYMfl-Ysx0tcLIiBztCpZROYQ7zqK8DC4aX0sYnPROEo2rlD4JA46ggej3HM8V-8lqNhdJccm75z-A_EqTO-R9apUF5AmijzbvF1Ph8Y3MigtrE6cqLG-tJ6nql_v32T2NPqhmQewA4F9d5A0JMRGa2LYJ3bz-pMfR-1VnI710FM_QP_XKShDjEZYrdmofERxB1uTX4Ws1UeToNOhCbH-lWZmAAIb39lBcpvq80sBf1bCEWSMXYJzuGj-EQCeTgrKSrlsDbWDoZVCSCcGAPjxKID4H6foHgamZIOOTVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب
:
بشأن الحرب على إيران أتلقى اتصالات باستمرار من قادة العالم يشكرونني جزيل الشكر. قلت لهم: متى ستدفعون ثمنها؟</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/92764" target="_blank">📅 00:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92763">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇸🇦
🇾🇪
عدوان سعودي  يستهدف صنعاء ومحافظات صعدة والجوف.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/92763" target="_blank">📅 23:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92762">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇺🇸
🇷🇺
السفارة الأمريكية في موسكو تصدر تحذيرًا صحيًا بشأن الاشتباه بمرض الطاعون الرئوي في إركوتسك.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/92762" target="_blank">📅 23:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92761">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde5dfbbff.mp4?token=XYF35PTu-O0_g7tRgLqL1112uXC_32klsT9uj-7g0k2otZT-BlS9pWaT1a7qWxS2D_iq0bR_GsrgZynk9ZbNdhfcQDlQ5L0EZrVQNJjqa8padPJleO20h0peyQvs6zYgJCqZVQFeoiFAjrdsB5QXxN5APF4Dt_jgNjjkKCR53qYVpkb4Um71Pp0OLn_HPy0PTa7EvKDihiUNoBxkcB1ZZyuMZGxICrbyeEexrn7giocBfLSwlxuFOq0XO8gIuZ1KCG16YwI83nwSYpW75kj1KflQsI2XBUmJn1BIBl_fVin13BjSgnld-FzVGzdTWUwiM17AZ1PcLMwJs4ub9dEYZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde5dfbbff.mp4?token=XYF35PTu-O0_g7tRgLqL1112uXC_32klsT9uj-7g0k2otZT-BlS9pWaT1a7qWxS2D_iq0bR_GsrgZynk9ZbNdhfcQDlQ5L0EZrVQNJjqa8padPJleO20h0peyQvs6zYgJCqZVQFeoiFAjrdsB5QXxN5APF4Dt_jgNjjkKCR53qYVpkb4Um71Pp0OLn_HPy0PTa7EvKDihiUNoBxkcB1ZZyuMZGxICrbyeEexrn7giocBfLSwlxuFOq0XO8gIuZ1KCG16YwI83nwSYpW75kj1KflQsI2XBUmJn1BIBl_fVin13BjSgnld-FzVGzdTWUwiM17AZ1PcLMwJs4ub9dEYZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇦🇪
اللاعب الإماراتي إسماعيل مطر يتعرض للإهانات من قبل الجماهير السعودية  عبر رمي قناني المياه عليه وسبّه وترديد شعارات عنصرية بحقه.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/92761" target="_blank">📅 23:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92760">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c6baed837.mp4?token=rrH4ZUHYGzQTfdb5sAl1h0cpgDoDQz-8ah_gXo_wb7S2No_pma10MVgJT9zkLDTBtCU_-0wAB63q1sXCvf6_LFqeWPWGQpS8h-HZvViCSBz_LjIx8iasIV8nxwsx-lNivEFCO0rz6iR62w4CdHldjvqLMqoWOICXWA3fKVJRA1VodASihR1YT6YAHz5w--N-0-nL6R0VuYPrNyuaQM_3MRoGWtTYgkKANrpnJbpzzV_n34puBxNRbCxkYiQ_nzFS2eV4ZvzhXQeFt67rKhrk5LtH8Zyp4qWCvMDQd2IHvE1pVTWpwuS05dfGG_Z0fRyz2bCF8nTcVnOZGhzAQ7gf5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c6baed837.mp4?token=rrH4ZUHYGzQTfdb5sAl1h0cpgDoDQz-8ah_gXo_wb7S2No_pma10MVgJT9zkLDTBtCU_-0wAB63q1sXCvf6_LFqeWPWGQpS8h-HZvViCSBz_LjIx8iasIV8nxwsx-lNivEFCO0rz6iR62w4CdHldjvqLMqoWOICXWA3fKVJRA1VodASihR1YT6YAHz5w--N-0-nL6R0VuYPrNyuaQM_3MRoGWtTYgkKANrpnJbpzzV_n34puBxNRbCxkYiQ_nzFS2eV4ZvzhXQeFt67rKhrk5LtH8Zyp4qWCvMDQd2IHvE1pVTWpwuS05dfGG_Z0fRyz2bCF8nTcVnOZGhzAQ7gf5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
الجمهور الاماراتي منزعج جدا من الاعتدائات التي حصلت عليه من قبل جماهير السعودية.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/92760" target="_blank">📅 23:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92759">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83df86dded.mp4?token=pJkMJnBHimol8-21HO0aHU2Y6xFTtMFW-Y9txKUjxhwIZc3Gjz1cJYJ050_h-zrw1djNCcQpejRGbzigzX2WEg2GbLShrkV7E0F3E90VG-t-krKdmgTnBPUjJZV5Q7jQXm54gJfjx5oL9vazQg_dteoK6rmM2kEeLntr2lQ59Ng7jNWrkoiGWM6QYbqB0sgvy8tio_dAsdEdAg_OwxNeZYwDqJLzFrb3jbvy6RMgYyh9AStHH1En9RSCKyLWYuwAv06xJ6yE5d7RbF47vUAUtJEjUZHZTHcCV3aHcmqaCvx5i63qFT4eCoGTMRO8WvkiaTqYbyywHp7U59Q-yQEr9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83df86dded.mp4?token=pJkMJnBHimol8-21HO0aHU2Y6xFTtMFW-Y9txKUjxhwIZc3Gjz1cJYJ050_h-zrw1djNCcQpejRGbzigzX2WEg2GbLShrkV7E0F3E90VG-t-krKdmgTnBPUjJZV5Q7jQXm54gJfjx5oL9vazQg_dteoK6rmM2kEeLntr2lQ59Ng7jNWrkoiGWM6QYbqB0sgvy8tio_dAsdEdAg_OwxNeZYwDqJLzFrb3jbvy6RMgYyh9AStHH1En9RSCKyLWYuwAv06xJ6yE5d7RbF47vUAUtJEjUZHZTHcCV3aHcmqaCvx5i63qFT4eCoGTMRO8WvkiaTqYbyywHp7U59Q-yQEr9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب حول إيران:
يجب أن ننهي الأمر؛ والسؤال هو كيف،قريبًا ستكتشفون كيف سننهي الأمر مع إيران.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/92759" target="_blank">📅 23:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92758">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWJ9lJ_cOhW90cbj03F6xyCLYyJrpk-mZB6AeX-Cgev8aSETHMkALGUpCBEGU6snlhdea0n4GY4WrnAq4e7CcLmlyuW1pF-kYT_qJKEQSke2NTseAkBtmCtV6YQttd5dkjpTM2UyXBwHUU4cIVDYXC0hnyfno9bglIjV3Hf2yYRanrbrq24YMHHTc0g8LmWghvnSX2yaJmjA8QvZeENbjRBMpt83WuntaviN7DylKlwPmE3i5DbzqNsMe5quCOs3tIzej-ELimqx7qFpkxdHCD3kWPjRYwR7pqPDFtF3PiQd0swOZL5dJ6MPl-gGYKPu8SQHVVtINPase_gasvg8MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇾🇪
مشاهد أخرى للحرائق الواسعة وتصاعد أعمدة الدخان في مصافي النفط بمدينة جدة السعودية.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/92758" target="_blank">📅 23:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92757">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇶
تحديث... سقوط عدد من الجرحى من الشرطة الاتحادية وتدمير عدد من الكاميرات الحرارية في نقطة تابعة للشرطة الاتحادية بمحافظة كركوك.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/92757" target="_blank">📅 22:54 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92756">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fcd631175.mp4?token=CjbCPeloO1qqVy7hS6Tm8VX-ESs8EPPa7I8lBTaDbotbfbWCxW1WvtbSGVnuNIOBlVcfjvuef1KdPPMRrGk7FhxiCb4r43dlVkUOoiOP0E84bI7Ten7LwaRsYmLQVeapuMRmMHeL-bdYxK4kPhtm_rcjTAMyNdB2Ip6-U_JDoPU9nKu4V8OW_m0ynuUCcshYJJBa62KOjfOSA85TuwcnoZol48UwYp0owO0hR-3iMY8I-ikHzWo30wwMd90wzqHU4jgFi2EgyZXqWS4ceRGoxnHmauOkI77U1i0Mznxf1GSL3_FguhL12IluBR93U72CHhEmDFHuVNCsiQVDuMLu3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fcd631175.mp4?token=CjbCPeloO1qqVy7hS6Tm8VX-ESs8EPPa7I8lBTaDbotbfbWCxW1WvtbSGVnuNIOBlVcfjvuef1KdPPMRrGk7FhxiCb4r43dlVkUOoiOP0E84bI7Ten7LwaRsYmLQVeapuMRmMHeL-bdYxK4kPhtm_rcjTAMyNdB2Ip6-U_JDoPU9nKu4V8OW_m0ynuUCcshYJJBa62KOjfOSA85TuwcnoZol48UwYp0owO0hR-3iMY8I-ikHzWo30wwMd90wzqHU4jgFi2EgyZXqWS4ceRGoxnHmauOkI77U1i0Mznxf1GSL3_FguhL12IluBR93U72CHhEmDFHuVNCsiQVDuMLu3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
الجمهور السعودي يقتحم مقصورات الجماهير الاماراتي ويرمي عليهم اكياس النفايات وبواقي الاكل وقناني المياه.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/92756" target="_blank">📅 22:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92755">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e5c9f983a.mp4?token=LVT1IWw4yUlV6hwyeOcJYP8asjyr0QeYWuh7rCSl5eemQBHQbccc6EPNyVA_2FX5EAlJkB4vE_S--ey01etNA03MC-PIK4OisCgxhJpLzt7yNpHi_gwfqyalxopctaUmZv8cxRTkg1PYfAUfYmQisI5c8HXnC21SH__dPYso0oM33rQeZSV3-vT-703NLf8Qz1L4MzWkpJImSmIALhXNkm0LeFTUPsVccYiULEYl5VXzPLMVCqT9SiE2eE8S1w9tzGkaE79Mmqz7rX8lBbCRE3pBmU3On00gVxXuhepIdBPNhM_x-6yFM7554nXxpqlLqac3qLApaSFPIBLlMNnsBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e5c9f983a.mp4?token=LVT1IWw4yUlV6hwyeOcJYP8asjyr0QeYWuh7rCSl5eemQBHQbccc6EPNyVA_2FX5EAlJkB4vE_S--ey01etNA03MC-PIK4OisCgxhJpLzt7yNpHi_gwfqyalxopctaUmZv8cxRTkg1PYfAUfYmQisI5c8HXnC21SH__dPYso0oM33rQeZSV3-vT-703NLf8Qz1L4MzWkpJImSmIALhXNkm0LeFTUPsVccYiULEYl5VXzPLMVCqT9SiE2eE8S1w9tzGkaE79Mmqz7rX8lBbCRE3pBmU3On00gVxXuhepIdBPNhM_x-6yFM7554nXxpqlLqac3qLApaSFPIBLlMNnsBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
الجماهير الاماراتية ترد على الجماهير السعودية بترديد الهتافات لتغطية على صوت النشيد السعودي.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/92755" target="_blank">📅 22:39 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92754">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0166d73c2f.mp4?token=fzcpCAIvW2iw3OZuNHMnT6UvYwNu0vUZgWsNbZPidUuu0Y1qgXkgw1drBumDLYfaq7sh4yfkxxo6tCSEP53wB6I9wRGOSPcgsjWql11Pj6sg2ZwEQEh0lZ1CvHFlIjh1Gx3jN4T6HqwJ0DKu2vc29P1YU3Wh5zoFscx4cAuAZvjsl_7sBbH9BPQhyNoNDuRqKiLKUiXGI8DbJmkqwf2mjDzyhoDNknDKPECqGwDOmPRUuapgtaL6rLXoA58LWKbs-9C1e-aqf7HwCzqG9BvxjmnEixizL_TKMKC6ZIwF-JXV-0Wa7re1nt2HPfpgrH7g-2cfNNvrIUFYANDw68cEPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0166d73c2f.mp4?token=fzcpCAIvW2iw3OZuNHMnT6UvYwNu0vUZgWsNbZPidUuu0Y1qgXkgw1drBumDLYfaq7sh4yfkxxo6tCSEP53wB6I9wRGOSPcgsjWql11Pj6sg2ZwEQEh0lZ1CvHFlIjh1Gx3jN4T6HqwJ0DKu2vc29P1YU3Wh5zoFscx4cAuAZvjsl_7sBbH9BPQhyNoNDuRqKiLKUiXGI8DbJmkqwf2mjDzyhoDNknDKPECqGwDOmPRUuapgtaL6rLXoA58LWKbs-9C1e-aqf7HwCzqG9BvxjmnEixizL_TKMKC6ZIwF-JXV-0Wa7re1nt2HPfpgrH7g-2cfNNvrIUFYANDw68cEPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
انزعاج واضح من المنتخب الإماراتي أثناء عزف نشيده الوطني حيث أطلق جمهور سعودي صافرات الاستهجان وردد الهتافات بصوت مرتفع في محاولة لتغطية صوت النشيد الإماراتي.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/92754" target="_blank">📅 22:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92753">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7ea07a170.mp4?token=D8NgnXo7l6JEGgS4HPwlYwv92c2uobf8DMHUSsj_e4r__sqMQ4jpGGSdwCVjErjP2iS-Znr-wXuDZyV1CX5a47aNmciuf40gRyh9fTQY26jmQmk3LIiJZ_b7GNWStn3b02I7Hby1ryzIpKxuGY0_Ke4PQ_7rdySlNERWbWJEjZSpYZ0lRvD39W6ueKQd9u9AtMb0AoOdRhEy-PC95ddc2jkD7_CUBj4niukuKmQWvQaKAmL77Dz9SlKLACaiZamRAxv8NWyF4VKbGup1yTzkAM_TIOVocZIerCyQ6mUG4xRk36mMgSSII6-_7tLWalhEWgN6RX5Wr4VWp-fiR1TZ7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7ea07a170.mp4?token=D8NgnXo7l6JEGgS4HPwlYwv92c2uobf8DMHUSsj_e4r__sqMQ4jpGGSdwCVjErjP2iS-Znr-wXuDZyV1CX5a47aNmciuf40gRyh9fTQY26jmQmk3LIiJZ_b7GNWStn3b02I7Hby1ryzIpKxuGY0_Ke4PQ_7rdySlNERWbWJEjZSpYZ0lRvD39W6ueKQd9u9AtMb0AoOdRhEy-PC95ddc2jkD7_CUBj4niukuKmQWvQaKAmL77Dz9SlKLACaiZamRAxv8NWyF4VKbGup1yTzkAM_TIOVocZIerCyQ6mUG4xRk36mMgSSII6-_7tLWalhEWgN6RX5Wr4VWp-fiR1TZ7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
انزعاج واضح من المنتخب الإماراتي أثناء عزف نشيده الوطني حيث أطلق جمهور سعودي صافرات الاستهجان وردد الهتافات بصوت مرتفع في محاولة لتغطية صوت النشيد الإماراتي.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/92753" target="_blank">📅 22:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92752">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8779c955b.mp4?token=gti1XeIcHvASxGWGYiTDxoxGUq5ICzYfRK5FEs1JQcr8Ewlqa6yUekVfkjzbsaPfz7nWlXUhJDPR8VyDaw0FEKM5k5AFp__8VmdEpib8g361Nun-rRdhes1iwbF_o_7Eug08juMVq0pM6wRX0ByipiAqibhGR_nFbgYe09D8i0ga9LhRK2mXgTvPPxqkMPh3czM_ixBYpJvjB5tRNDgFHsjntig1xnvLCEUmB5iAZIGFBfh1A1smoStn_P1Tf04QPrxERO0R_ZQGirs8_SvM-ccsSxQrL9x9N7XzrAxsOY4MNgbFiB2Ay0yZNDiwLnTUWQuVKNLIIkyP2KS1A89hoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8779c955b.mp4?token=gti1XeIcHvASxGWGYiTDxoxGUq5ICzYfRK5FEs1JQcr8Ewlqa6yUekVfkjzbsaPfz7nWlXUhJDPR8VyDaw0FEKM5k5AFp__8VmdEpib8g361Nun-rRdhes1iwbF_o_7Eug08juMVq0pM6wRX0ByipiAqibhGR_nFbgYe09D8i0ga9LhRK2mXgTvPPxqkMPh3czM_ixBYpJvjB5tRNDgFHsjntig1xnvLCEUmB5iAZIGFBfh1A1smoStn_P1Tf04QPrxERO0R_ZQGirs8_SvM-ccsSxQrL9x9N7XzrAxsOY4MNgbFiB2Ay0yZNDiwLnTUWQuVKNLIIkyP2KS1A89hoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
تحديث... سقوط عدد من الجرحى من الشرطة الاتحادية وتدمير عدد من الكاميرات الحرارية في نقطة تابعة للشرطة الاتحادية بمحافظة كركوك.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/92752" target="_blank">📅 22:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92751">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇶
سماع دوي انفجار في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/92751" target="_blank">📅 22:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92750">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
يقول مسؤولون أمنيون إسرائيليون إن هناك تحذيراً محدداً من أن حماس قد تحاول شن هجوم في حوالي 7 أكتوبر، وربما تستهدف موقعاً تابعاً للجيش الإسرائيلي داخل "الخط الأصفر" لغزة، بما في ذلك محاولة اختطاف محتملة.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/92750" target="_blank">📅 21:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92749">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇾🇪
🇸🇦
تعليق الدراسة في جازان غدًا الأربعاء خوفا من الاستهدافات اليمنية.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/92749" target="_blank">📅 21:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92748">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 66 غارة جوية وصاروخا، استهدف بها الأعيان المدنية في محافظات الجوف وتعز ومأرب والحديدة وحجة وصعدة وذلك من خلال طائرات "F-15" و "تايفون" وطائرات استطلاعية مسلحة، أقلعت من قواعده في خميس مشيط والطائف وقاعدة الملك فيصل البحرية، والعدوان الصاروخي من جيزان ونجران، وخلفت عددا من الشهداء والجرحى في صفوف المدنيين معظمهم نساء وأطفال.
ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد على بلدِنا 1642 غارةً جويةً وصاروخاً.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/92748" target="_blank">📅 20:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92747">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇷
انفجارات في قشم</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/92747" target="_blank">📅 20:53 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92746">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇷
انفجارات في قشم</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/92746" target="_blank">📅 20:53 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92745">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇾🇪
جولة جديدة لمراسل الإعلام الحربي من مديرية ذوباب تنفي ما يروج له العدو من بطولات وهمية.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/92745" target="_blank">📅 20:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92744">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🏴
سلسلة 7 اكتوبر
ابو إبراهيم يحيى السنوار حينما برز الإيمان كله إلى الشرك كله
🔻
انتاج نايا بالتزامن مع اعظم ثورة مسلحة للشعب الفلسطيني</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/92744" target="_blank">📅 20:39 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92743">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85f5267f02.mp4?token=A6RCEGwqz2O6SJurd21wmbHWzU79kXZILDugjb1TtQIR-UsXQSmzTB0iSfJnzO2uJCm6n04SKFq7MjDAnXahAxmzLdLaUUwoU-TF2dVQcOWtd4w5kYgAGOgYLzvje6aoXnEKI9GfbjpLEsGC4hgWmrApCBAuFT7CdBMikHmUafbZ-Itp6gkLHDGjHj3bPywR9aZkNJRboEypQuEvkhfuBSE4ii0VvczwXudaN_LODtsSUFnkopT6mst3L2kcP5NcgP0iKWfEE6uhSf1vic4R0pz-V_dQp9rcVc0u7f7ZvKZh4KurTPvMda5-2lfoCystz_zfrpp734JJnTHhHvMINA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85f5267f02.mp4?token=A6RCEGwqz2O6SJurd21wmbHWzU79kXZILDugjb1TtQIR-UsXQSmzTB0iSfJnzO2uJCm6n04SKFq7MjDAnXahAxmzLdLaUUwoU-TF2dVQcOWtd4w5kYgAGOgYLzvje6aoXnEKI9GfbjpLEsGC4hgWmrApCBAuFT7CdBMikHmUafbZ-Itp6gkLHDGjHj3bPywR9aZkNJRboEypQuEvkhfuBSE4ii0VvczwXudaN_LODtsSUFnkopT6mst3L2kcP5NcgP0iKWfEE6uhSf1vic4R0pz-V_dQp9rcVc0u7f7ZvKZh4KurTPvMda5-2lfoCystz_zfrpp734JJnTHhHvMINA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراقون لنايا
🇮🇶
-تحجيم للدور والمهام وتقليص للمديريات و جعله اشبه بشرطة حماية المنشاءات و الإطفاء وعمال أمانة بغداد .    - قانون الحشد الشعبي المعدل يثير لغط كبير ويجرد مقاتلي الحشد من روحه الحقيقة ويحوله لمؤسسة بلا إرادة و لا رادع وتعويم واضح للتضحيات…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/92743" target="_blank">📅 20:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92742">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مراقون لنايا
🇮🇶
-تحجيم للدور والمهام وتقليص للمديريات و جعله اشبه بشرطة حماية المنشاءات و الإطفاء وعمال أمانة بغداد .
- قانون الحشد الشعبي المعدل يثير لغط كبير ويجرد مقاتلي الحشد من روحه الحقيقة ويحوله لمؤسسة بلا إرادة و لا رادع وتعويم واضح للتضحيات والغرض الذي جاء به ..</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/92742" target="_blank">📅 20:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92741">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
تمكنت قواتنا المسلحة بفضل الله من التصدي لعدد من محاولات تحشيدات العدو السعودي التقدم باتجاه باب المندب وطردها وإجبارها على التراجع ولم تحرز أي تقدم، وتم استهداف تجمعات تلك التحشيدات بعشرة صواريخ باليستية وأدت عملية التصدي والاستهداف إلى مصرع وإصابة العشرات، وتدمير عدد كبير من الآليات.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/92741" target="_blank">📅 19:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92739">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vxr3eKTh28r1FvepLNoHy-o7esHGDcL-CqXXus3mI54ifcR0Zm1KHODYEM3K_9U9KQRvBBtAmM51mjAZXI-n0YoQRYn_ubOb3eXCxOWgLt8aOWBZAR_zFybtYasq-4KiNGBx1KOtortGPM-4CqUzty-ovpmFHX7X0BpSuebMXM79n86MgGvqbjytOzAbZVMTGFTc6umN36OsmzFZCHLxbt3fSBPLjXEVq5gsd8TSUfHadG8FkK9TLc8FnIUbatKKiLvaYZY3ASpkKVezseSdESapBw9JKKCPBoLyaSIBIESYq-U2JPzAqyQuhMPthXrC8ebpbpinkqdQ5fdWacvttg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hetHeAb-fxtLnr2974DhAOS1BgDPKq4VvRLZfStIAQHEiu-C7OveUfo_Xoz2faIWqXyLTJaioL0UBho2BJCRrjPPLCZ9fvdSGEEW6jOb1KY6d5Z7XhJju0__mLW30_QVmwtNC86BpDrkmBAl8BZL697ppm3S6zQVjcbvirqZ6zPWOJDI-EmsOdLJmasWnRrk7t0hyzCMmeGjEk8TLXlGmeOU1EDJ9ej2b-X4DMvlcMtVnsYAg6Fc8_nF-QvcswoMkaZhJNKl85qeiXkNnCvRuGSKwkAw-0nPwPcOpwqzLlLPxb4PhrpTEHy5AKwYjItPuBqwldTSG-jChDrawFp6iw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
سُجِّلت الليلة اضطرابات في حركة الطيران فوق عمّان بالأردن دون معرفة الأسباب.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/92739" target="_blank">📅 19:41 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92738">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nopmDXoU5-fKEA6ZUBnaVblSjIJQcSZQQF7TWy6HnmrNJoEnUgrdMEJ8_qsceHeUyVSZe3O0iJ_iAC3TP2khMNzVrakRlB5UEXhX8-6Ozl42HqHt68ngwCnF61EeC0LrnOqhoYsufbG_AwfjiU2JYSCpQp5gGpy7FNpJel0vrCGTNAEdhscWuE0OPLbLQSE2uaW7ooiS2_FiyBMaX6esuoo6kx4VnFdLrrD8i8fiSlrUdI8JzqdXkJyMFGbTn02ERKHi9unYDQdL5ZHHDxcph0kxtooLaJOossx2OkclrfmMMyn0LOPyATYhEOf1SYFwbB32gnCzf7vP58W5JUHFJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇾🇪
مشاهد أخرى للحرائق الواسعة وتصاعد أعمدة الدخان في مصافي النفط بمدينة جدة السعودية.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/92738" target="_blank">📅 19:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92737">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇾🇪
مشاهد نوعية لعمليات ضرب التحشيدات التابعة للعدو السعودي في عدة جبهات بطائرات شواظ الانقضاضية - 06 أكتوبر 2026م</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/92737" target="_blank">📅 19:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92734">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u7Q_vqvBq3mgRBUJpNX3AmEN_W4WSdoZNX3Abr8lGyPLTh3VF-70YLF5LBQ4No9a2_ucpDf8FoD-i4OrCrNiBT7k3WMCKD6M1g98n6SSjDYeeBvG5c06vrNrJnNdbiMRSK5I9FFeuOSZfs5CMaXnYUJHkXK33W9oMj_rn_HD4MVW5_C3ZqR9sDSN5VibEbmCdouUOG5IkuWFiMHS-hUeYAcitcLpqe1NPTdUR1Bqem-wipuk9_YwlMnQ7EhVhCmjIhSri1fnzjs8kKS7G4_VL08eLWWNVKrcDGeHWMQxTVZrawDCrgpP_gfaxQPAyCyNad1cQpXwm_1qYU4vtLOEHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uWRlzY65Vo6IEOBlxBqBSSjcsWT1ccGPzmYGC5FNdS94S1jXZ22G38uXJjOmuKpPD62wbSABj6WRAqRKo_7lec7xFi3D4DMTvP9rd0EX_rSlxCB6OV8fw66Q8JcEDDFVdC8LC79zOcESAAsBk_5weMgTJb8AVaTQsHt2IMiFhf6CJoroSTfNfdE9_nSj7TODo3QH2Iu4sbFTCoS8mrb3Psk6Lj7Xv3gToHRnSMJLLYAIIQRko3KZqGK9WFCGWt-Plq6WuxPvbFc0E4CwHT9Rs5iFreg8tWMbPgJFO-_ee9F8fcSbrk_C_Kumc3jY7nOA2IisOi5xp0W50UICjjDyyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇾🇪
🇸🇦
مصافي النفط التابعة لشركة أرامكو في جدة السعودية تشتعل نتيجة الضربات الصاروخية اليمانية.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/92734" target="_blank">📅 19:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92733">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:
تمكنت قواتنا المسلحة بفضل الله من التصدي وطرد تحشيدات العدو السعودي أثناء محاولتها التقدم باتجاه مواقع قواتنا جنوب غربي الوازعية ولم تحرز أي تقدم بفضل الله، وتم تدمير عدد من الآليات والمدرعات التابعة لها وسقوط العشرات بين قتيل وجريح. ‏وتم بعون الله استهداف التجمعات التي حاول العدو التعزيز بها لإنقاذ من تبقى من تحشيداته بعدد من الصواريخ الباليستية، وكانت الإصابات دقيقة ومباشرة بفضل الله وخلفت عددا من القتلى والجرحى.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/92733" target="_blank">📅 19:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92732">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇸🇦
🇾🇪
السعودية تعلن عن تعرض خميس مشيط لهجوم صاروخي من قبل القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/92732" target="_blank">📅 19:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92731">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fb6c9da6d.mp4?token=buqrNK_KMQAYJNL_j8_sJAhhFjv__6thpA-NmSfR85mAkIpd_ILeUU1fJBorANKNVRDruWAvRY-EEMXEy940G3MajV_c-zf1Wwn35gxLdMOGq-K_zSVgCZZkqGuUh8aAcs1chMcL4JzaiseVXIxToj8UV3lSts3bCyYpUGy5oewiO0Yws0I53eZoMCJFpLxh4BX3u0qKbAv4jCTIH8Mq9e6SgG7XOEp2739mDbzQu59TYJ-j-8G4vp5Sp1mp5KdoaJ22hTGSjn2f3ODA5BjqxH3KbaAvMRLqFyb4MUQ36eDRehhtXDfmH1cB_VyV8hFHRh69py7BIlNv86ysuDDOFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fb6c9da6d.mp4?token=buqrNK_KMQAYJNL_j8_sJAhhFjv__6thpA-NmSfR85mAkIpd_ILeUU1fJBorANKNVRDruWAvRY-EEMXEy940G3MajV_c-zf1Wwn35gxLdMOGq-K_zSVgCZZkqGuUh8aAcs1chMcL4JzaiseVXIxToj8UV3lSts3bCyYpUGy5oewiO0Yws0I53eZoMCJFpLxh4BX3u0qKbAv4jCTIH8Mq9e6SgG7XOEp2739mDbzQu59TYJ-j-8G4vp5Sp1mp5KdoaJ22hTGSjn2f3ODA5BjqxH3KbaAvMRLqFyb4MUQ36eDRehhtXDfmH1cB_VyV8hFHRh69py7BIlNv86ysuDDOFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
مشاهد من انتشار قوات المسلحة اليمنية في مدينة ذوباب.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/92731" target="_blank">📅 19:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92730">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449b21d287.mp4?token=oUUBLxz3OHzGE_p8_vh9cjeh5B8j1FWEtim16yL7D-_MlTWpvfKYLe_YA73xLma99PJvfB9KSSJD3p3ygIp7BQ820kbZgArfXXPd_5YQJr14aKd8_Pya2L5kv0elxtbeOxTxvhqLWIjJGHb2OM2s_p8M6eyB_UpAWdc2Y1jPIseLuxaoTXRE3jzO1D75RudC1Ke-hsLDQpLh7h7rOCWFN4X4kPBu5ecwkRVUjl2Uz94uzjqWe5y48-DqaU8iBLbMeY4SKknBn257yiiTLnl4odSs-kT1_r3pxuhYzGcIOhKOuo-HKjrfQl5wJqOI1khOUXNYCu9jBWw6ks7wHz--Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449b21d287.mp4?token=oUUBLxz3OHzGE_p8_vh9cjeh5B8j1FWEtim16yL7D-_MlTWpvfKYLe_YA73xLma99PJvfB9KSSJD3p3ygIp7BQ820kbZgArfXXPd_5YQJr14aKd8_Pya2L5kv0elxtbeOxTxvhqLWIjJGHb2OM2s_p8M6eyB_UpAWdc2Y1jPIseLuxaoTXRE3jzO1D75RudC1Ke-hsLDQpLh7h7rOCWFN4X4kPBu5ecwkRVUjl2Uz94uzjqWe5y48-DqaU8iBLbMeY4SKknBn257yiiTLnl4odSs-kT1_r3pxuhYzGcIOhKOuo-HKjrfQl5wJqOI1khOUXNYCu9jBWw6ks7wHz--Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اجواء ترابية في العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/92730" target="_blank">📅 18:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92728">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd72347f96.mp4?token=TJhr2ASdYWHrgrwYDvcAsCm2CPo1hxWuCwKMmdpoxCo8Q2MjhQOMvsQHJnsPgbXA7qn7ptSeodPgacJFKCWacXcgmBFCoB5xfndacbxuLK0h1TB60Y0LONrVwuDgvYc_FA_6vPr-pvhDjw3q3ozUb4fJTL8HAALa1tbxStRUnSkcyao-QhOBplwYAw6rilGFPJPyoogeMe1BaE3m-1IMRN6aPZ-0fYEjo1sVE86V6Vxe9aglknLB15cgKPNF-R0df9FNb2hPHTWihSKmozyaDD-tetRyMdQdjjj2UmR6ZrYLnYDwAJlofdZuoPvzzXUkdvEOsow6CHO5Dae9R3CK_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd72347f96.mp4?token=TJhr2ASdYWHrgrwYDvcAsCm2CPo1hxWuCwKMmdpoxCo8Q2MjhQOMvsQHJnsPgbXA7qn7ptSeodPgacJFKCWacXcgmBFCoB5xfndacbxuLK0h1TB60Y0LONrVwuDgvYc_FA_6vPr-pvhDjw3q3ozUb4fJTL8HAALa1tbxStRUnSkcyao-QhOBplwYAw6rilGFPJPyoogeMe1BaE3m-1IMRN6aPZ-0fYEjo1sVE86V6Vxe9aglknLB15cgKPNF-R0df9FNb2hPHTWihSKmozyaDD-tetRyMdQdjjj2UmR6ZrYLnYDwAJlofdZuoPvzzXUkdvEOsow6CHO5Dae9R3CK_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد للهجمات التي طالت منشأت ارامكو</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/92728" target="_blank">📅 18:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92727">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔻
امين عام حزب الله الشيخ نعيم قاسم:
نحيي العراق ومرجعيته وكافة أطيافه لأنهم نجحوا في طرد المحتلين ليكون البلد مستقلاً عزيزاً، الشعب العراقي مؤهل أن يطرد المحتلين كائنًا ما كانوا وفي أي اتجاهات ليكون العراق مستقلًا وعزيزًا وقويًا.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/92727" target="_blank">📅 18:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92726">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇶
🔻
بتدخل من الحاج ابو رائد الفياض تم إطلاق سراح جميع معتقلي الحشد الشعبي في الحوادث الأمنية الأخيرة</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/92726" target="_blank">📅 18:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92725">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpS6b4yHVja-6GpmIT9DSlFZTsZfXm7XnKieCS1d5ksVjFWfo3aThCuWvPF2nrXq_gHfATqJlnZ-RgNVdQCzueC7tkiNFgXRqhkAtqsJDwXPbnpYazaI4CqtGsNMSd8znFINWXN6mqJXUebvC-0qKEA6kfGGwPREyB_wdCDz6dTxj-sKXDgC8mY9ms0GWwMGsnDx7_cL3bhica7l8pA0xLDiS8kfv6cDctX7wVB6-0V9g-E9tJP_klx-9AztMtnKL_pJCuKlNixOURd7te512lGuFzmBE6pUtY9cnz445PYengdWcySVrbmBUMK-GwgKqCE_0NDPLbU6sRKMVHPAng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔻
بتدخل من الحاج ابو رائد الفياض تم إطلاق سراح جميع معتقلي الحشد الشعبي في الحوادث الأمنية الأخيرة</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/92725" target="_blank">📅 17:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92724">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/809c63099a.mp4?token=O5tqRUIpADf4VamZuzPxgEvXU3x72aCT-dAavVwDmGeKn8SMGRg6Jpv_d91I9dbBg-67vE6W5cposCZyRw6Jt82HYrg33kwiCySRf6khKJ-ePkRgqDwi8wGz8HZPqRltNlXh3kReZU5uQbwbT9iCJwt_ih5xiVgYUrKNk6v4fCKSPLtd8U_xmqbQvG3mcuY5kMFtxzlXXalbLG6aqJnwMVYiHvp5RzNWtUI9omvHniWuQ8F-wDpnCoG4CuGklCOv6k6Bj0kRtJw1acmH31rHnQZmV9vZ94nPwQqNbc3YoB8EP7_TtMm--NcdtB1WDMmhf4lSZ8RyykRgZJ_RIyDaWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/809c63099a.mp4?token=O5tqRUIpADf4VamZuzPxgEvXU3x72aCT-dAavVwDmGeKn8SMGRg6Jpv_d91I9dbBg-67vE6W5cposCZyRw6Jt82HYrg33kwiCySRf6khKJ-ePkRgqDwi8wGz8HZPqRltNlXh3kReZU5uQbwbT9iCJwt_ih5xiVgYUrKNk6v4fCKSPLtd8U_xmqbQvG3mcuY5kMFtxzlXXalbLG6aqJnwMVYiHvp5RzNWtUI9omvHniWuQ8F-wDpnCoG4CuGklCOv6k6Bj0kRtJw1acmH31rHnQZmV9vZ94nPwQqNbc3YoB8EP7_TtMm--NcdtB1WDMmhf4lSZ8RyykRgZJ_RIyDaWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دمار كبير يطال منشأت ارامكو في الرياض بعد هجوم القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/92724" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92723">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDDCSCeLwB0kO0W1GawvmQU8fmu1fqu4W6xK-qDg7detvN_EwCZQdUVknwRJI3b-VH3sfM_mEJwTbxxwUbYDeydG8uZgdc6Ai_73VlIbmOn781McqE5I_dzqWRLdGQAR2UJySXdadkdqW-kwXDoV-sfR4od_2bT3UN87x2qkxudQYYmth38mJ2Fmk_P7_4npLv2JwEKM5FlUSvV3Rj9UArYl0sn-YPzBd-YFcqEx7p_xh4pxcmSIRjiMWBw1c7PY_yTzksnyOSE4iVHm0ReSz8bImQcst-IIyRxJ2cRM8k0w97hUChTr9xtpapcUjsMQl1JwccJuPs4yYk2U2jsR8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔻
بتدخل من الحاج ابو رائد الفياض تم إطلاق سراح جميع معتقلي الحشد الشعبي في الحوادث الأمنية الأخيرة</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/92723" target="_blank">📅 17:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92722">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b4473bf24.mp4?token=PyoOUomPagFghRQeV-TT7dny61BwUWkOditaib85aPOu7fYM78a1zRiQqf5yvEnaHGmOZe3hAK6InHJhbfnphVazCp5-54wK3Fs_VYp4YbwECX_Ld4Q8iF-DkYtGiveCbKOW2Rz8ObcadglbxL1c51vvAVX-imzt2bsGGf6uLSXURqpWyzge0HZx_xjkZwly0gibDdOhVecHcqYKtQTPDytuWwlp4IGeyuxhbylzy8f6GPXW-5L_PAh3qXUhtqWd9OKFkc8RWOhrG3F_11Fc_PT3Gq7Od0Hxr05VIK_5tzI2_gQouZXIqvhNIrtlmVJmdXC-cDsEYBkyn7B4A8DiZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b4473bf24.mp4?token=PyoOUomPagFghRQeV-TT7dny61BwUWkOditaib85aPOu7fYM78a1zRiQqf5yvEnaHGmOZe3hAK6InHJhbfnphVazCp5-54wK3Fs_VYp4YbwECX_Ld4Q8iF-DkYtGiveCbKOW2Rz8ObcadglbxL1c51vvAVX-imzt2bsGGf6uLSXURqpWyzge0HZx_xjkZwly0gibDdOhVecHcqYKtQTPDytuWwlp4IGeyuxhbylzy8f6GPXW-5L_PAh3qXUhtqWd9OKFkc8RWOhrG3F_11Fc_PT3Gq7Od0Hxr05VIK_5tzI2_gQouZXIqvhNIrtlmVJmdXC-cDsEYBkyn7B4A8DiZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية من جزيرة ميون في مضيق باب المندب</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/92722" target="_blank">📅 17:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92721">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
استهداف التحشيدات التابعة للعدو السعودي في رأس العارة بصواريخ باليستية.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/92721" target="_blank">📅 16:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92720">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">الشرطة البريطانية تعلن اعتقال بريطاني عمره 22 عامًا بشبهة التحضير لعمل إرهابي متعلق بقاعدة "فيرفورد"</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/92720" target="_blank">📅 15:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92719">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41aff32781.mp4?token=DDJcLLd9SMP1GOFd7hksdX5U8vf9W6ZGBFn-Ayp_57kPpjeCuk3qGJ77DFcHwRI_WMTOA50dY-3tlitug0vavIhFaOFT0D33u6mgidSQNcuYFx_pcKBD22FhwaqSlNcxYK9I8EPyRWoAVr6SimvKfVNgS00x9ZfgKSpVNmLeiItlIaaeOE7p-xBWELuLjkem5HVLUngimKBNUHecwlOEOzd8PP0nzxFVeS8CRTrvvWBlFS0MXFpauOJe0QcHGba1O1HfZaTituAvvKflC_kpn6MvPWLFTmye8g91J1QpxS_qoS6QzJQ-N25M1pSCCZTW9H1w0j5tpmZbsVU3ITD2_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41aff32781.mp4?token=DDJcLLd9SMP1GOFd7hksdX5U8vf9W6ZGBFn-Ayp_57kPpjeCuk3qGJ77DFcHwRI_WMTOA50dY-3tlitug0vavIhFaOFT0D33u6mgidSQNcuYFx_pcKBD22FhwaqSlNcxYK9I8EPyRWoAVr6SimvKfVNgS00x9ZfgKSpVNmLeiItlIaaeOE7p-xBWELuLjkem5HVLUngimKBNUHecwlOEOzd8PP0nzxFVeS8CRTrvvWBlFS0MXFpauOJe0QcHGba1O1HfZaTituAvvKflC_kpn6MvPWLFTmye8g91J1QpxS_qoS6QzJQ-N25M1pSCCZTW9H1w0j5tpmZbsVU3ITD2_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تتقدم في تعز وسط انهيار دفاعات العدو السعودي ومرتزقته</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/92719" target="_blank">📅 15:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92718">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">حدث بحري في مضيق هرمز</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/92718" target="_blank">📅 15:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92717">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gR2t99lqwX5mwLOYmSvy_k0RpvNPUfAFwRsO7kqRv6kkpCT-maLusruxTsBL8q6zdIj1GsuKpf1ajXaDlEPQrGZCkBIGhPguDwOtqvr0cHxQ_3DYHfBadWuqYCyjhVegp4SjBlHmjDE1g9Mba3QoRkJyjUvvFlptIbqFuzRQVWl0T9AX0bays_lur1V1mwr53ofviitOfHWnS04ufIvHXdR6_HxXZEiONtgQWg47o3d5FOvPD2CN70n6WmhfjMb_blLgmXypdQlRS24L5J8PPBOriqspkVKB2Ugs2xCzmkWqoSnHVOYO0QAGR3Y3ACPM89aJvDByIu3G7RbhERq0Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث بحري في مضيق هرمز</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/92717" target="_blank">📅 15:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92716">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:
سيتم عرض مشاهد استهداف التحشيدات التابعة للعدو السعودي في رأس العارة الساعة 3:30م بعد قليل.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/92716" target="_blank">📅 15:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92714">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oD9f5VOEX0FGDf5QVpThzzJz9j1TBeC5I1X2gY8PpeQrfNluZvOTyCKe07nuCrA6DMe-gQN-OHfJn8Kx6z2hUV9sZHCj53jnltCE5WZGP8PzqaboMycrty49ErigIXGjKygGsEf6gpYXPxtbYPHx3k28jVVEpjav8D9irBHRiZifGwGHOzcx7vCi5PI6PlaSP9NqydE9dFBjCJlKTG4CsEvTtvv6qaNeszmcdV8wx3mZ-HmrC8dc1cGfDd4vHiAbQzpTbNExsvtRhMF5cFd0ygJUTwIDK4oPJr3PWjSNXpU5J9YRx1b_egMnTJPiWIYSqbXCC9lslmYqA_3CcuWoVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e778f783a6.mp4?token=sGQmWDUcJhROP7ZXPPAOdEzt7HFrsPUovUhxhP4WO3rdlsD1vmfPeyZcFvAh7Be155kc1d6J1lo6BnoMU7k2SuxzM2-wnvLdZkGaOIjYK3Hml-0TRSPTS2iQdGls9EwEHmoDFcJms7zq6gVKsOzJl7eEHBpY5sas54hiwpg5wqYUfYPuaNqtKfG2oDTchqxOyDydf6USJqWPXDRoCiYuBkTxIQu5S6pMiqC5VrsH1VjBfdJtOOGVBD8WsLqVF6fR3O1KtPMY62oWW1AvuAQ8AM5l6pWdRT1vITjc4hgp6SJ6GTvoc8Z0Jj78B34spRQJsTYW7aB67PAGqW5RvlChFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e778f783a6.mp4?token=sGQmWDUcJhROP7ZXPPAOdEzt7HFrsPUovUhxhP4WO3rdlsD1vmfPeyZcFvAh7Be155kc1d6J1lo6BnoMU7k2SuxzM2-wnvLdZkGaOIjYK3Hml-0TRSPTS2iQdGls9EwEHmoDFcJms7zq6gVKsOzJl7eEHBpY5sas54hiwpg5wqYUfYPuaNqtKfG2oDTchqxOyDydf6USJqWPXDRoCiYuBkTxIQu5S6pMiqC5VrsH1VjBfdJtOOGVBD8WsLqVF6fR3O1KtPMY62oWW1AvuAQ8AM5l6pWdRT1vITjc4hgp6SJ6GTvoc8Z0Jj78B34spRQJsTYW7aB67PAGqW5RvlChFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇾🇪
الاقمار الصناعية تظهر ان هجمات القوات المسلحة اليمنية استهدفت منشآت شركة إيسكو في مطار الملك خالد الدولي بالرياض، حيث تظهر آثار حروق على أحد المستودعات أو حظائر الطائرات. شركة إيسكو هي شركة تابعة لشركة سامي للإلكترونيات المتقدمة</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/92714" target="_blank">📅 15:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92711">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec18e4b397.mp4?token=GA2egOc1cceOVO1VRPKJ-DoyZnPKsMzJdJyHnrl-zm2jtdPVe8_6Xu-mg9wpNGBXFLidtvEylH2pT-igJJxE-F0eX4-PraRKmDhNMINoNf1BFfukQImOj3LA9RgJ17oDDvPs3yQcAL5z4qU2AV8RDxSVpG5Wrmo8j8r8MWMB1YGyYGW6AgFn9fDcC5kbXINiP2sCy_O6mk5Vl3rCHJjT9gfKFRCWJm3SpgjhpDbM9tSk_vy_wSMQRVF-Stklqzgcr_BaQfAE3fJsI-rZzSB9If_8xC5Wqln4jHtMHz4J9UCdavjPTaL6RuImkTUM19TXVdUTOVF9625fby7X3wzul6u798iEUBAPu5fvQx3U3JwvgE0-TnW17aY6lho2USfNLrc3RFuT-8nP2ye7YF8XVQk91eUp-qx2H7ynhCyVcdfkf678d9LBx1s-VaDjSI-q6WrVyFqk0nhfq7p_v8sE30eu_xZUOGw9ryWlL7us2qAc7_AUOG2oGTdwyFnm12hm4i5hVkXtJR2xlqgV0PcgnJFwthNKsd-0F3D5lkC0CgsvL-dnXDrqGoMd32DVmiIBMMbbahGq_RxRjOmYIGwMsrv1w9-wUz1juG-1_GmG5FJO7Wytcks0Dn22BtisLHMlCnBjN7JmEVpP0jVCAJv1qXJSV2800XMB0dK-SdRs6zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec18e4b397.mp4?token=GA2egOc1cceOVO1VRPKJ-DoyZnPKsMzJdJyHnrl-zm2jtdPVe8_6Xu-mg9wpNGBXFLidtvEylH2pT-igJJxE-F0eX4-PraRKmDhNMINoNf1BFfukQImOj3LA9RgJ17oDDvPs3yQcAL5z4qU2AV8RDxSVpG5Wrmo8j8r8MWMB1YGyYGW6AgFn9fDcC5kbXINiP2sCy_O6mk5Vl3rCHJjT9gfKFRCWJm3SpgjhpDbM9tSk_vy_wSMQRVF-Stklqzgcr_BaQfAE3fJsI-rZzSB9If_8xC5Wqln4jHtMHz4J9UCdavjPTaL6RuImkTUM19TXVdUTOVF9625fby7X3wzul6u798iEUBAPu5fvQx3U3JwvgE0-TnW17aY6lho2USfNLrc3RFuT-8nP2ye7YF8XVQk91eUp-qx2H7ynhCyVcdfkf678d9LBx1s-VaDjSI-q6WrVyFqk0nhfq7p_v8sE30eu_xZUOGw9ryWlL7us2qAc7_AUOG2oGTdwyFnm12hm4i5hVkXtJR2xlqgV0PcgnJFwthNKsd-0F3D5lkC0CgsvL-dnXDrqGoMd32DVmiIBMMbbahGq_RxRjOmYIGwMsrv1w9-wUz1juG-1_GmG5FJO7Wytcks0Dn22BtisLHMlCnBjN7JmEVpP0jVCAJv1qXJSV2800XMB0dK-SdRs6zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية من وسط المدن المحررة في الساحل الغربي تكشف زيف الاعلام السعودي الذي ادعى دخولها</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/92711" target="_blank">📅 15:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92709">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db9df5fb72.mp4?token=IRTlM77WkwpU-x_s0VqrgVOWcbts-p0cMuIf6jYVkwwmMwtYwUQGupGNBa9U6GGci_lrqlO5SXYb9ZYOMpdr_AAabj2SR0J9Ik3vlnwUFggdVL5OS9_TykPh8_Lnob9LiUDPlhskMPFYYVWuZQ-YzrnVpwIYJcC6Lg3xiuJeEKaLth9UwPz9lxzGaS8Bu96sR62ebb1x7RyZQ6M05ZNM5lG2Am2V1qcQTzsiKTGDaN88TfY9vZhkj4d9YQiz9p8b4Wr8baeXOeXXOWqLpO1aighRQEc3z3U5gdwkvktOZHur7u5BcE2gbQz_Ce8uk0OAv0rIMUGhPZnPGjuJuDgcD4KvSr3UTQyXTtVrKrh3nmYt6fogTK35QtUG4ar6jAhlyBkH9PNdMP4VotGlabuR1QOy4zDWrdTsnMHIBz3UHfsDrI95uyoRR2soD100seHxFPOjX455KeXRsyG3pN6STpikfaMSuMnXzkwz_RRZbvJfdpnMIRmn2yRBsySkhI-ErwvdFWm9KIxZ8zkm2bM7Hm4SCRokghJzYmOgnJMpHld6PC8SxP76qKf7Bmmueqi5jdQ6IjpPtnA6b6YmmTgLuV2B7QIUDtU0qC8Fc_uzk_wxppgGCdvuzMVYk1jV9fYDwJPAz9PR87vi4Ik0pkaJOnoJQzW8hX-xsjKou1FjMuM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db9df5fb72.mp4?token=IRTlM77WkwpU-x_s0VqrgVOWcbts-p0cMuIf6jYVkwwmMwtYwUQGupGNBa9U6GGci_lrqlO5SXYb9ZYOMpdr_AAabj2SR0J9Ik3vlnwUFggdVL5OS9_TykPh8_Lnob9LiUDPlhskMPFYYVWuZQ-YzrnVpwIYJcC6Lg3xiuJeEKaLth9UwPz9lxzGaS8Bu96sR62ebb1x7RyZQ6M05ZNM5lG2Am2V1qcQTzsiKTGDaN88TfY9vZhkj4d9YQiz9p8b4Wr8baeXOeXXOWqLpO1aighRQEc3z3U5gdwkvktOZHur7u5BcE2gbQz_Ce8uk0OAv0rIMUGhPZnPGjuJuDgcD4KvSr3UTQyXTtVrKrh3nmYt6fogTK35QtUG4ar6jAhlyBkH9PNdMP4VotGlabuR1QOy4zDWrdTsnMHIBz3UHfsDrI95uyoRR2soD100seHxFPOjX455KeXRsyG3pN6STpikfaMSuMnXzkwz_RRZbvJfdpnMIRmn2yRBsySkhI-ErwvdFWm9KIxZ8zkm2bM7Hm4SCRokghJzYmOgnJMpHld6PC8SxP76qKf7Bmmueqi5jdQ6IjpPtnA6b6YmmTgLuV2B7QIUDtU0qC8Fc_uzk_wxppgGCdvuzMVYk1jV9fYDwJPAz9PR87vi4Ik0pkaJOnoJQzW8hX-xsjKou1FjMuM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد خاصة لنايا تظهر تصاعد اعمدة الدخان من الرياض وجدة بعد هجمات للقوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/92709" target="_blank">📅 15:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92707">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf09f757cc.mp4?token=VhPXmuF3dtecmCwsd14QT9Ehzb3H18AuXyUs_Z8ivaTuhU3vh9AUr1al4F7IoZ0VhhpheK2drR3tYGr7wxleRs15vb-f6vkW2P5R1LhUU_Reuj3y1Nu1o83zghXHu-5KahwF3cKFQjtZFKItaMIoIwYIc8qwyOrr3BvaThH5bGFNwh_Yet3pzxEj2O3hvemSGHtfVs2T4qoXVQEafdIWpSLoZrnuJJe44nWNU-R4odYIVOjE9hb_AGlcvI5PeFLYihtsVxIuPmCukoOwjoN_HzBp20pe6Lwu2oKWthVuwnGBDhqKKEfLuPQ-jQg0MrXes7Gtg4VB2ZvRKFuH9XwrXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf09f757cc.mp4?token=VhPXmuF3dtecmCwsd14QT9Ehzb3H18AuXyUs_Z8ivaTuhU3vh9AUr1al4F7IoZ0VhhpheK2drR3tYGr7wxleRs15vb-f6vkW2P5R1LhUU_Reuj3y1Nu1o83zghXHu-5KahwF3cKFQjtZFKItaMIoIwYIc8qwyOrr3BvaThH5bGFNwh_Yet3pzxEj2O3hvemSGHtfVs2T4qoXVQEafdIWpSLoZrnuJJe44nWNU-R4odYIVOjE9hb_AGlcvI5PeFLYihtsVxIuPmCukoOwjoN_HzBp20pe6Lwu2oKWthVuwnGBDhqKKEfLuPQ-jQg0MrXes7Gtg4VB2ZvRKFuH9XwrXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية في ذو باب وباب المندب</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/92707" target="_blank">📅 15:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92706">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇱
وزير الحرب الصهيوني كاتس:
في حال وجهت أجهزة السلطة الفلسطينية أسلحتها ضد المستوطنين وقوات الجيش في الضفة الغربية ومستوطنات خط التماس سنعلن الحرب على السلطة الفلسطينية، وسنشن هجوما شاملا وفق خطة منظمة جرى إعدادها والمصادقة عليها مني ومن رئيس الحكومة نتنياهو. ستكون المعركة قصيرة وعنيفة، وستشمل استخدام قوات برية وجوية ووسائل خاصة، واغتيال مسؤولين كبار ونفيهم، وتدمير الأسلحة والعتاد الحربي، وإجلاء السكان على نطاق واسع، وتدمير البنى التحتية.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/92706" target="_blank">📅 15:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92705">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">القوات المسلحة اليمنية تسيطر على جبل مطران بمديرية الصلو بمحافظة تعز وتغتنم عتاد عسكري كبير من الآليات والأسلحة المتنوعة</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/92705" target="_blank">📅 14:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92704">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">مشاهد من جريمة العدو السعودي وإبادة أسرة المواطن علي عضلي في حرض بمحافظة حجة</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/92704" target="_blank">📅 14:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92703">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
ترقبوا الساعة الرابعة عصرا مشاهد لاستهداف التحشيدات التابعة للعدو السعودي في رأس العارة</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/92703" target="_blank">📅 14:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92702">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇶🇦
الخارجية القطرية:
من المبكر الحديث عن احتمال انضمام قطر لحلف مكة.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/92702" target="_blank">📅 14:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92701">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">أ ف ب عن مصادر هندية: إصابة 12 شخصًا بعد تعرض ناقلة لهجوم قبالة سواحل سلطنة عمان</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/92701" target="_blank">📅 13:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92700">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔻
الـ100 دولار امريكي تسجل ارتفاعا كبيرا في الاسواق العراقية وتصل لـ161,500 الف دينار عراقي</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/92700" target="_blank">📅 13:54 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92698">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇾🇪
مصدر يمني: مقتل عبد الرحمن الشمساني قائد اللواء ٣٥ مدرع في جبل مطران بمحافظة تعز.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/92698" target="_blank">📅 13:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92697">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇾🇪
🇸🇦
وسط إنكسارات وفرار مرتزقة السعودية.. القوات المسلحة اليمنية تستمر في تقدمها وتسيطر على مناطق شرجب وهيجة العبد ويافق والشوار وتبدأ دخول مديرية المقاطرة وبني يوسف بمحافظة تعز من عدة اتجاهات.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/92697" target="_blank">📅 13:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92696">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/685539bddd.mp4?token=S6-nSHz9n9qfOd8s7vOTg_nXL97IB6jbKygPkbwzPGsmIGcG-GhQdMreW5Fu5oFAOdam8iKkBmppxgjOFL_VN1ozooYy0xxmCgn3eQb-SLK9OLaShVaCbXnoWnvv2i26Vjt_-l3qVqNqPfKfMe_FybHKW08DP0QQlfruEBXPgsPfQN4igi1BnM6ftlFq5_xz0w06INYqNySBe2o1Du-V8wPmqQQOBz1AdVOADbzd1d5W29ClclBsCL1kq4nVMocojrTEwSrBGPQuj4iH1MZNneFzz2VtysPkn-0hhPgPKx0O4HaTPUypyd-bIabRTTJIFJM8Lny8WLEahNRfGepq3Z233y734OJ_VHqKuljIbSaXNOzUPHRwRwKyRcluiBRy0Mw95ateBYqDz9mso69eXjUaISTJwjnayB7XEydJFVziW5lKHzmrcjAT9jSQjP_Ndg5bGZEU96lvVWWnNsB7Bq16MNjmcgL1LvMr8j0ddA5ctNePg3JtfDAhjIpqPI-ZyIci-laOtgE5-bYd-Srakp3UUmdCBwEH3leO2cu_qu3-i3eaKuss95S3WulhvfyLW-ejhtdf7vHSTjrf54mEkxSkonUp5cbSHYPTuZO5TWBeW3NSbfn_UigxdSdSTRrrM51iXsdNI5LcSX9rYG3d35v4CLeSU8DnfymPikCRCjk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/685539bddd.mp4?token=S6-nSHz9n9qfOd8s7vOTg_nXL97IB6jbKygPkbwzPGsmIGcG-GhQdMreW5Fu5oFAOdam8iKkBmppxgjOFL_VN1ozooYy0xxmCgn3eQb-SLK9OLaShVaCbXnoWnvv2i26Vjt_-l3qVqNqPfKfMe_FybHKW08DP0QQlfruEBXPgsPfQN4igi1BnM6ftlFq5_xz0w06INYqNySBe2o1Du-V8wPmqQQOBz1AdVOADbzd1d5W29ClclBsCL1kq4nVMocojrTEwSrBGPQuj4iH1MZNneFzz2VtysPkn-0hhPgPKx0O4HaTPUypyd-bIabRTTJIFJM8Lny8WLEahNRfGepq3Z233y734OJ_VHqKuljIbSaXNOzUPHRwRwKyRcluiBRy0Mw95ateBYqDz9mso69eXjUaISTJwjnayB7XEydJFVziW5lKHzmrcjAT9jSQjP_Ndg5bGZEU96lvVWWnNsB7Bq16MNjmcgL1LvMr8j0ddA5ctNePg3JtfDAhjIpqPI-ZyIci-laOtgE5-bYd-Srakp3UUmdCBwEH3leO2cu_qu3-i3eaKuss95S3WulhvfyLW-ejhtdf7vHSTjrf54mEkxSkonUp5cbSHYPTuZO5TWBeW3NSbfn_UigxdSdSTRrrM51iXsdNI5LcSX9rYG3d35v4CLeSU8DnfymPikCRCjk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇾🇪
رجال أبوجبريل من مطار المخا الدولي ترد وتنفي مزاعم وأكاذيب إعلام دويلات الخليج حول تقدم المرتزقة نحو المدن اليمنية.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/92696" target="_blank">📅 13:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92695">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇷🇺
الكرملين:
روسيا سوف تضطر للتصرف لحماية أمنها إن استضافت ليتوانيا أسلحة نووية أو قاعدة على أراضيها.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/92695" target="_blank">📅 13:09 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92694">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇷
مقتل عدد من العناصر الإرهابية على يد القوات الأمنية في محافظة بلوشستان جنوب شرق إيران.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/92694" target="_blank">📅 13:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92693">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mW2SQSryB-42B5vXguO7qZ4f39mOni1ndAU0HLMo6xatc1fTX3aT4GIVOG02SVTLIMjYJdDQc5XvL-ji07swc-PBOtw4JfTtF_J33jQ9MiLCYwkySdu1XUGW340MY1VIMNeWt1CengZDAiLEVxtgxvRfMoBUpNDR-qr9tdf6CkTpO5VMFzfx_nmjSspiAkfoJaS_G29bazaxsiv8zci9fxuPYn77oBIi8eTJwb9kwGkEYV_EVdR-tXQhZci8QejSxpN_9RAFvIbGZY2u0YxDKSyvnc_Psf0YIo0pKAABOBK1IJK-NHryBAvG8WQLol3RlEWuR0i7DClGHTF3zkk2Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
مراسل قناة المسيرة في باب المندب يعلن سيطرة القوات المسلحة اليمنية عليه.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/92693" target="_blank">📅 12:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92692">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:  تمكنت قواتنا المسلحة بفضل الله من استهداف تحشيدات العدو السعودي في معسكر الدغارير في جيزان بعدد من الصواريخ الباليستية وكانت الإصابات دقيقة ومباشرة بفضل الله وخلفت عشرات القتلى والجرحى في أوساطهم وهروع سيارات الإسعاف إلى المكان المستهدف،…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/92692" target="_blank">📅 12:48 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92691">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:
تمكنت قواتنا المسلحة بفضل الله من استهداف تحشيدات العدو السعودي في معسكر الدغارير في جيزان بعدد من الصواريخ الباليستية وكانت الإصابات دقيقة ومباشرة بفضل الله وخلفت عشرات القتلى والجرحى في أوساطهم وهروع سيارات الإسعاف إلى المكان المستهدف، وسط حالة من الإرباك في صفوف العدو.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/92691" target="_blank">📅 12:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92690">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇮🇶
مسرور بارزاني:
لا نشعر بالقلق حيال أي مشاكل أمنية قد تنشأ (بعد انسحاب التحالف). القضية الوحيدة التي تهمنا هي تأمين أنظمة مكافحة الطائرات المسيّرة والحصول عليها، أي تعزيز قدرات الدفاع الجوي. أعتقد أننا بحاجة إلى مزيد من المساعدة من حلفائنا في هذا الشأن. ما زلنا على تواصل مع الحكومة الاتحادية، ونجري أيضًا مناقشات مستمرة مع حلفائنا لتأمين القوات وقدرات الدفاع الجوي."</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/92690" target="_blank">📅 12:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92689">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية تسيطر على مناطق شريع والمخعف وبلعان والميسار وجاحصه وجبل زنم في محافظة تعز.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/92689" target="_blank">📅 11:09 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92688">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇸🇦
هيئة الطيران المدني السعودية تزعم:
إصابة 3 أشخاص في استهداف مطاري نجران وجازان مساء أمس.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/92688" target="_blank">📅 11:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92687">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39a7d65637.mp4?token=DcOglo2qotzCKn19qyLRDbHUilzoC4atR0EXT-VxOC1JXZrqZQ3gTJ1TdoLA-NerSWj4w0jwkWhwEOcFVJ39EAhSZJZ6S-H5nPcgPzBrjfEv6vJvZiiS13nNsdU4GtjHzKVjkaRmIuTiswYFGvsknbsSN2dM2Jj4nlvGCSN0tZCgkqUMyC8FTj1_NLgHAVK0KGsrH3lsyJZV8PDLlVPVHUs61iFsLO7eEQnVUWG7uX0bXO_gXsW0me9iMFxn1bGUK_tLselIZBXe1St5GYvJeZOMwpJ72yQ9LXL3EYniYyXVIkyXU6gJb6KpkyXvyLQuquaptQzKgBmp0LfyLe4HEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39a7d65637.mp4?token=DcOglo2qotzCKn19qyLRDbHUilzoC4atR0EXT-VxOC1JXZrqZQ3gTJ1TdoLA-NerSWj4w0jwkWhwEOcFVJ39EAhSZJZ6S-H5nPcgPzBrjfEv6vJvZiiS13nNsdU4GtjHzKVjkaRmIuTiswYFGvsknbsSN2dM2Jj4nlvGCSN0tZCgkqUMyC8FTj1_NLgHAVK0KGsrH3lsyJZV8PDLlVPVHUs61iFsLO7eEQnVUWG7uX0bXO_gXsW0me9iMFxn1bGUK_tLselIZBXe1St5GYvJeZOMwpJ72yQ9LXL3EYniYyXVIkyXU6gJb6KpkyXvyLQuquaptQzKgBmp0LfyLe4HEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
مصدر يمني: عدد القتلى والجرحى في رأس الغارة يتجاوز 100 مرتزق.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/92687" target="_blank">📅 10:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92686">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a87fXXPV8HfRJTUxD0m8_nITQbc01aE6DsIp_sUYvlMw-jZsYau8CN3NqxbD0T9NC_ajrdWUoJGNIGKYW4bRuYM3cOgwxeqR8olFbCDO6BowiDeQDilE4KOdaiL-lZxGUbX6XgmGzh4_SxpOSOTgpopm1pu-q3QINYggAkewGQBfecDNP1mIIlWGW_D5o9Sih4vXq_Xe9IluaYsUcaD-jiRxbDP0LirEcyuNdnnp6I1MiDMWjVM72Vu86rKuGR6lZ2U7XBCDjaAMPTcVi9bwXEktYf0dG_VJw-i9vV8ULuvK_SrvuvYId0bdbytgJTCiUjlb5xW2_M17SYLv2vtaQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇦🇪
🇺🇸
بحرية الحرس الثوري تجبر سفينة إماراتية بالعودة عن مسارها أثناء محاولة عبور للممر الجنوبي في مضيق هرمز، وذلك بالتزامن مع مرافقة الطيران الأمريكي لها.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/92686" target="_blank">📅 10:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92685">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔻
‏إصابة سفينتين بمسيّرات في البحر الأسود قبالة سواحل بلغاريا.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/92685" target="_blank">📅 10:27 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92684">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZll4NYT4GA_VB4pNur91KSlkN8qSlRo8fEUNPAbQWn-lF3m-Pg1i6RyIw_yws274kXifCs6j0_umsCJPmoV5K0reFvoDHlVR6kl1M97gI5Hp0w1xPFx27XK7b155Ac3D083VHF5Z-hDBi7nq-3A5yoE90chIDUchHUdgjbuKvdGEc-3SH6gUCJCJrWfWJnlOSqiFgtUFpc8XDfI-J4J82790vtBo9I8NXZ8EiJ-VQaI0GJKxgvMv07FJ0ZxMgtoCJD9FFH_HZTnLROFQFU8snjM85zext5RpQwJrYxqgEH59vMXC586ioZ6xjip8SGz3-DmGuOBKzE5f36mF3U3Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية في مطار الملك خالد الدولي في الرياض.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/92684" target="_blank">📅 10:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92683">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvYPfurK412_UhTOImK4z20YiUcv5H2JLgRv_lD8e0o8Hw_AnjDZyYwt_UvCdOrVW-aYFjUfMGTfadAoCLy8FtjN6VUSu_tjDpyKAjr0C5UOjyZ_VjC-MsO88kKHcMUcuk2UIRRyjUzNEbKXEI47IqzlDifWUn053s45Nkisp-6_jbjYk6uHGGap73Ps0Q_uSNQtveWXUoED7lMzNVY2LG9ESQV_WWDwJlLSN5hufAZSYOghQK7BHBxrl0Vh3xfmCL_R0a4eXAyc01ovwKnmVZdRr12gcrBOENT4mWZIrouQ_eIscBmqEB4XObaKxKPm0sCq5RvxGQKSDNO3OpCdYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مقتل عدد من العناصر الإرهابية على يد القوات الأمنية في محافظة بلوشستان جنوب شرق إيران.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/92683" target="_blank">📅 10:23 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92682">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية: تواصل القوات المسلحة مطاردة تحشيدات العدو السعودي في ما تبقى من مديريات محافظة تعز وسط حالة إرباك كبيرة في أوساط تلك التحشيدات وهروب عدد منهم.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/92682" target="_blank">📅 10:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92681">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇾🇪
مباشر من مديرية ذوباب، وسط سيطرة تامة للقوات المسلحة اليمنية عليها.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/92681" target="_blank">📅 10:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92680">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇾🇪
🇸🇦
مجدداً..
مصافي النفط في جدة تحت رحمة الصواريخ اليمنية.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/92680" target="_blank">📅 09:24 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92679">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67d2663057.mp4?token=pAubpagVXxKdqsC6cwR8S6I4XF1o4IefzXeZ-thDsUbk4ysYfKmrY8xrC9e6dj6mHqF6HlIwDAawiBvG0WB9lglHER8hbbZm0JjFYyqhnnoDWanzeQThh48Bm_Wxl8DOeSx-cZWvhqAJH--2r5rLx64FfH98YoRD-84nkLaedtF4TSZtTMUIizwaI8ugzD20Fqc08TDMO6V4VJhhv7bQ16NGSHF8UiWwVYEA8XvTCfVW6OgJkCxcq4JXmvBcPHNgVAw9sPrvu2-qidzLIwcSxUoz2llT_i9PujNfAeQ3Imp7ibNxDpkLA4anDMbUj_bKnOZA98zBpWO6dfRCg_BbxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67d2663057.mp4?token=pAubpagVXxKdqsC6cwR8S6I4XF1o4IefzXeZ-thDsUbk4ysYfKmrY8xrC9e6dj6mHqF6HlIwDAawiBvG0WB9lglHER8hbbZm0JjFYyqhnnoDWanzeQThh48Bm_Wxl8DOeSx-cZWvhqAJH--2r5rLx64FfH98YoRD-84nkLaedtF4TSZtTMUIizwaI8ugzD20Fqc08TDMO6V4VJhhv7bQ16NGSHF8UiWwVYEA8XvTCfVW6OgJkCxcq4JXmvBcPHNgVAw9sPrvu2-qidzLIwcSxUoz2llT_i9PujNfAeQ3Imp7ibNxDpkLA4anDMbUj_bKnOZA98zBpWO6dfRCg_BbxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
إنفجار سيارة في القدس المحتلة؛ سقوط عدة إصابات كحصيلة أولية.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/92679" target="_blank">📅 09:02 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92678">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇾🇪
مناطق كحاح ونجد العود في محافظة تعز تحت سيطرة القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/92678" target="_blank">📅 08:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92677">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdc64f78bd.mp4?token=chjG2slC6_-WaMtuKrOdTCAab5LmMr6ah2Pb_hwAHgQQt9Wp_8WmIJYNZtaz7YaMYiyEee294PHyrZrcR7_aP3JMAGvSX6F3TWvsJWGyTZr_3KFL4nv3UUvCDwpUd135oaWEtnuurxt1JtqNxFV3byeNX1pdAajSd3H4djdATKHgDcYNPLgecfM9FCKegSOu43tUqbMetj0qXhfBfo8xRH5zYKMWp_On3hv_ci1wOxbZJ6Hz59AmLI6S3K1e8BoTZQ-llDjLyg2xD1-A20a74iea86pGIP3ekzz-zOR4HuILaVbR8kwpREJ38Uk7BBUthGwA3EUo_njnkhG1aC69eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdc64f78bd.mp4?token=chjG2slC6_-WaMtuKrOdTCAab5LmMr6ah2Pb_hwAHgQQt9Wp_8WmIJYNZtaz7YaMYiyEee294PHyrZrcR7_aP3JMAGvSX6F3TWvsJWGyTZr_3KFL4nv3UUvCDwpUd135oaWEtnuurxt1JtqNxFV3byeNX1pdAajSd3H4djdATKHgDcYNPLgecfM9FCKegSOu43tUqbMetj0qXhfBfo8xRH5zYKMWp_On3hv_ci1wOxbZJ6Hz59AmLI6S3K1e8BoTZQ-llDjLyg2xD1-A20a74iea86pGIP3ekzz-zOR4HuILaVbR8kwpREJ38Uk7BBUthGwA3EUo_njnkhG1aC69eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
مشاهد حصرية من داخل إحدى الطائرات التي تلقت تنبيهًا بعدم الهبوط في مطار الملك خالد بالرياض.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/92677" target="_blank">📅 04:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92676">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇾🇪
🇸🇦
وسط فرار مرتزقة السعودية.. منطقة بني حماد في محافظة تعز تحت سيطرة القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/92676" target="_blank">📅 03:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92675">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f0671c1b.mp4?token=PgUs-N4mmz8loFLcrzAPXOUKg2INT4M4fHrKM1RTUxzElsnCRWrPOqUJwQDfXAMv7PTrOxDTwNYzBhHN7aMRa3euO5dtvSJ0K6drDYTEqmfgJ6KAHa5uXRcjNup7PlX9PlcHvUVDQPF9RyOJiK3SKorngnmk6G_ZVwiVSI1C4_PzNgxEZ1vc9ep9M3Sdtbs5EXuAenLq6M8v_kZ3mbJw3XFNmS-4jy1aVq98bFBXqPvMBbK4vxAy3ms21exsYm_lcC2A0VOJ0tc4aOooRkrE0ApcLzYplhpIPRxiNNyr9dn-2C_UlPQNKqRC09bP7tHk-fa3JvJ_onw5ytZlblCK0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f0671c1b.mp4?token=PgUs-N4mmz8loFLcrzAPXOUKg2INT4M4fHrKM1RTUxzElsnCRWrPOqUJwQDfXAMv7PTrOxDTwNYzBhHN7aMRa3euO5dtvSJ0K6drDYTEqmfgJ6KAHa5uXRcjNup7PlX9PlcHvUVDQPF9RyOJiK3SKorngnmk6G_ZVwiVSI1C4_PzNgxEZ1vc9ep9M3Sdtbs5EXuAenLq6M8v_kZ3mbJw3XFNmS-4jy1aVq98bFBXqPvMBbK4vxAy3ms21exsYm_lcC2A0VOJ0tc4aOooRkrE0ApcLzYplhpIPRxiNNyr9dn-2C_UlPQNKqRC09bP7tHk-fa3JvJ_onw5ytZlblCK0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
بعد إستهداف 13 سفينة خلال أقل من إسبوع من قبل البحرية الإيرانية.. ترامب: استطعنا القضاء على قدرات إيران العسكرية وتأمين مضيق هرمز.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/92675" target="_blank">📅 03:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92674">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامب حول إيران: بالمناسبة، نحن نهزم إيران. ألا تعلمون ذلك؟</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/92674" target="_blank">📅 03:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92673">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e77dc63a0.mp4?token=mew7sj2WB_NkTkcmKePEUWzs8ENQPsrBeiGGsdP9RdTJGh0tlFIRvRt3pkQRtPMXYSHHe4BjjvKNWqg6MAIEmA-cVWbO9o2q2Iih7hn803fcK4IhiAm5FgAWgT6B4hdg94_F9mA16X9UgAu_wVo7WVLA6Mmjl6vIuBvXEEMb4z7eCkuXudaWpVCzM-8rSi5JPkuRibgQnTn9iqeuk99rPoHlwl8cWyDkZXzwpt96_rrbZP-_L5Pvp_W8WvBVC8HNeralQsTngBOc5WKvWGgnu9JvBDIij_n_cOxtBmqfPr7nF-wUhcNMiivuoZthvXTRbWSNWUncAiWYFqVx-UtGCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e77dc63a0.mp4?token=mew7sj2WB_NkTkcmKePEUWzs8ENQPsrBeiGGsdP9RdTJGh0tlFIRvRt3pkQRtPMXYSHHe4BjjvKNWqg6MAIEmA-cVWbO9o2q2Iih7hn803fcK4IhiAm5FgAWgT6B4hdg94_F9mA16X9UgAu_wVo7WVLA6Mmjl6vIuBvXEEMb4z7eCkuXudaWpVCzM-8rSi5JPkuRibgQnTn9iqeuk99rPoHlwl8cWyDkZXzwpt96_rrbZP-_L5Pvp_W8WvBVC8HNeralQsTngBOc5WKvWGgnu9JvBDIij_n_cOxtBmqfPr7nF-wUhcNMiivuoZthvXTRbWSNWUncAiWYFqVx-UtGCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب حول إيران: بالمناسبة، نحن نهزم إيران. ألا تعلمون ذلك؟</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/92673" target="_blank">📅 03:02 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92672">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇾🇪
🇸🇦
بعد قتل وأسر العشرات من مرتزقة السعودية.. مشاهد لسيطرة رجال أبوجبريل على منطقة رأس الغارة.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/92672" target="_blank">📅 02:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92671">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a73627067.mp4?token=O38USjE5XFIV2SPrIOuEBd0mR_t6g1nzSLOEq0ixxhrXYGb54rWreOmdO8ts_nRJL8y_7t1oQA-pqxUcQalgWM32YwjCgzp3YyeTbrTdp0BHOurjxasq8jbB_E6FCB2mVlfGuGtdiFyCAG5aC1nFL8Fu8DKIXAS1sQzDCc9O0BnTti4ixaipTxHQ1zaDHfZVyaFpma6poCfWP4MnZ-BiBToR9iZpTaKMXBkDGsNooQcWATOUWfsvF4NbNO9K5EZpPLl6Tos8g7ziI9A-jveUZaTFAbraVukbAv07HHHlfLObIKZX8six-cB5u53IzC_UR387qytXosM_kFH8rQR9bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a73627067.mp4?token=O38USjE5XFIV2SPrIOuEBd0mR_t6g1nzSLOEq0ixxhrXYGb54rWreOmdO8ts_nRJL8y_7t1oQA-pqxUcQalgWM32YwjCgzp3YyeTbrTdp0BHOurjxasq8jbB_E6FCB2mVlfGuGtdiFyCAG5aC1nFL8Fu8DKIXAS1sQzDCc9O0BnTti4ixaipTxHQ1zaDHfZVyaFpma6poCfWP4MnZ-BiBToR9iZpTaKMXBkDGsNooQcWATOUWfsvF4NbNO9K5EZpPLl6Tos8g7ziI9A-jveUZaTFAbraVukbAv07HHHlfLObIKZX8six-cB5u53IzC_UR387qytXosM_kFH8rQR9bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
قصف صاروخي عنيف للقوات المسلحة اليمنية على تجمعات مرتزقة السعودية في منطقة "رأس العارة"، والقتلى بالعشرات.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/92671" target="_blank">📅 02:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92670">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/92670" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قولو له الرياض اقرب</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/92670" target="_blank">📅 02:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92669">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88dade42c2.mp4?token=tsBg2XYj10n7QZeVp4aD1zX2NEv-xV1ieNTJa9KFS3saXihM3zoDukD97ffRHvoLBsIMMNi0O4MjwCyjcIL1PQYaP1YJMJLZcK3LrEY1y39s7NCRPMG3LciPF5yS-g9TonzCcnf5v8pwm6lFgWSODX8SavVJh3ILnjIfxNinNqjo4JwFp1eQQzxR-q0jqUcbfBhFXIzh0OVJnIaSzhzQ_4vpB6xYUev0nKI-rI-cL5EPat9qk046QJH58Uyy4yU4Wzg-0HJNJy0ViUTIpg3E6X7Jjv-Ua4-__qgvb6lQ4waCncC9mFLTZ-6M7j4lQJa-BGh2117FdPf3DCEDnGvCIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88dade42c2.mp4?token=tsBg2XYj10n7QZeVp4aD1zX2NEv-xV1ieNTJa9KFS3saXihM3zoDukD97ffRHvoLBsIMMNi0O4MjwCyjcIL1PQYaP1YJMJLZcK3LrEY1y39s7NCRPMG3LciPF5yS-g9TonzCcnf5v8pwm6lFgWSODX8SavVJh3ILnjIfxNinNqjo4JwFp1eQQzxR-q0jqUcbfBhFXIzh0OVJnIaSzhzQ_4vpB6xYUev0nKI-rI-cL5EPat9qk046QJH58Uyy4yU4Wzg-0HJNJy0ViUTIpg3E6X7Jjv-Ua4-__qgvb6lQ4waCncC9mFLTZ-6M7j4lQJa-BGh2117FdPf3DCEDnGvCIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله اكبر طائرات عدة تتلقى تنبيه جديد بعدم الهبوط في مطار الملك خالد في الرياض</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/92669" target="_blank">📅 02:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92668">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خروج مطار الرياض عن العمل وتوقف اغلب الرحلات عن الهبوط والاقلاع بسبب هجمات أنصار الله في اليمن</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/92668" target="_blank">📅 02:41 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92667">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ta61AWuBvdXx0X09bW4mBSAub1woEgTpzckDjNmcKl9ofQxJg_LRGEhx52__8gtHqxIXNbbfeTNROu90fJcKmQtdAzarFOpMie06Kpr0WnDHT2yfz2gNk0qGwQ0iCjkSSfQnFcw7aRGD3NVZgEgvq8Px4VoRySO0kZArJz4C1UTz0sciPWHZCcCkkmOO8MhP6UbMCWNQt_gHnRAvRsBHKU9BDHLc5tT229nMyIiHPZc42hZLimXb90qq1mKzTwSiwqkYvGeog208Z6CWDo1CQ0Qsf8BdJ9X1m0M3nuqvrN86vYEjNH9WvcD_8s1wUK9lULhV_GOGIxhvccCwNDI5BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اكبر   انفجارات عنيفة تهز الرياض مجددا</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/92667" target="_blank">📅 02:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92666">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">الله اكبر
انفجارات عنيفة تهز الرياض مجددا</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/92666" target="_blank">📅 02:28 · 14 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
