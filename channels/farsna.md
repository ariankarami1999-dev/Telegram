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
<img src="https://cdn4.telesco.pe/file/l_rNjXhrYZbu5XOE3gIhsPhAWeNltRfwC4ZOsisHc6xyeJchykqrEq0RoMpTEmoizxaDx1CQ-_u3nVtlMssVInApA5HAnWeoK0fQHGtJstIowpZdbbPtGnhfWg3ahC6ISF2045S0ZKvMIqA30qZXXbZLhfkZprxaJCWiV8di6Bi9dBkkEHbg2xFACtbWvJZi_K1L7gGAoj1mtBvvnpHFqVJjvzOuw5gAI6ZyBufZjNo-SJIWsFU2RBeL3v5D4kD1URonARqWARbxy_Kxs1BKM7YHkAIvnHHsyfMGDe2IR6jPZqnvE9lFOA7HB1INXm46HZIg4H2Zfu7WtMieah9l5A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 01:02:14</div>
<hr>

<div class="tg-post" id="msg-449059">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1pg1V67FEltxUFkoYYXBkahwPWek3OM_Ruwo9OYNea9LyXMIqChq25KOfKfFOgHJQKBqHA8K_ZKvmthYldVu6b4Zuq6B-FQi1Xk5ad5rRlHc8g4RIBpmwlfGUljMGueaZUf-57bI-qF_h9QRGj66k9mHG3lZhWuSpH4AQsz5juaExkK9yxSUNZZJjXxKtLf2OAyqd2C5SjBINctf1kGIUmH5ioMb_zI173IyO48hsT5rZWGJpQVDnYS-hISjy7bKviDDckIizMoifRMYTpTt0aqenS_p3i5hr9M0JOFalc6tF42JHsn7SJdJnTsF061jBI-bkQkcaA9YXBrrYGbxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
واکنش معاون وزارت خارجه به نقش امارات در تجاوز آمریکا به ایران
🔹
غریب‌آبادی: وزارت بازرگانی آمریکا سند جدیدی را منتشر کرده: تسهیل مقررات کنترل صادرات و ارتقای جایگاه صادراتی به امارات به پاس حمایت آن از تجاوز نظامی علیه ایران.
🔹
این اعتراف رسمی واشنگتن و سند رسوایی ابوظبی، مسئولیت بین‌المللی و آثار حقوقی مستقیمی دارد. امارات عربی متحده باید پاسخگو باشد.
@Farsna</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/farsna/449059" target="_blank">📅 00:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449050">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ljAL-GKNmUv7qYNDRY2NgbNVT3lGRk1fX81KJ1c8imPyqxeA0zF4L9752RBgnJiQTRMWkPTryjZ0s7jdQh7vfPsl0ahKOvWGUNKuZp-2_uvD8KJhoksl9Ow4QFNr-ejFoVp7__Eli5PxVs65HKiHs5j4shUKL2JPxy-cYBIeLbpfHs2ug98ORQeHUww1o4ctM1wVboqsPG32JIyOJYMljtwA_vV6jcIdEDbirQlBu7k9CyMOQuQCdJhPzSRjrK1XkNw1gPTRiKwLx5iVfjRvmg3Gdcv_NqRFHzplAprB5wJOkUKF4TB1McT2nvJERKOWd3MyV8prov20JVhYiS7z0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nRaggFBeaFhUYVjNOtu3O6PbnlZiJ4JPa0DHiVa3FrbEQyvdzb0bkEWSrcn0R2Vfh-nsaNyqgOeqZnc_rtcsiUqgPyxeHTeEvaeqb3oVj4Jl0pe7L3CFA2HMY_QaqtaLWhX185cFW-VA7fgDjlrB_Pj4FKWjAsVX2ore3v2OghRIXWOnVe3U_-k1k-8_xANFhctvfrW86KZtzF6xtEkmYqCCZrlWaPX5pjK_fQ4xQIHQ1JjnlOumRYHXYStBWbVOb8chi3cWu_motz2IhI3aDAj8Jylu2ORcmO0QzesO-ydM1FAdXBLVN5DIpFlJondg4F5zZuTZDBAjy5D_euu86A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fOcDlfccc9t1ulVHBInSTt6b-Q0AI3Bh0S7b6_r_xH-YSaTTFVTkl_KDVcbxccEnZdXn5gPAeQ2KThXQp7eK4D6GmuXNwuSOCKo7l8TW1oYdAqftEOdprmYi1LvDNGKb7hLCNzga1EDZTysuDHDFkVyAOQe8Ur-3JI6kpSPLxSTv0N3nZZfc_Cd2uO4N_vdC74t9Ecjw0-Ab8PTo1xlYjdvKriqtGIcVFhOIlz9Q2CRhgdnyDa2eFXKQ7IiikxaaWuC3qi1H3R9QOg1CxccB5w3okb3MtF0t9Wo-Nl59tkk6Mtl8crMMZhLPxQlOp_eFirxwoyeEya5F5dUVKrj6dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EUFB00EhWtS1a2xJ1P8mrmBOhBfMMcmht3w8fBdfqfzXtB7khcfLfKwRQM2o7wTAq65qyAS0fJ8sx9SG50CvhU4_EhlO4o3W2RuiTKADzI7YuGm-IETm3B3vhfVy5jRPh8A3R8NF5qFmQgmW6Ec1xRDJ-vgO8ngSkW_GivL-wjOIbgSxAgQxZozyeVSCEpvcECJLK-D-LFiTC7eBB414z4rtd0a1fjqpipoik57bsOvzKu9YSC9Hj9yT4WlJsksa3zloM2l-p6otb400ytzm5x1ew0pTKO30Eurgq3NWFcwgjJlDA9tNbELZ9v49VRkY-fnw9op4ckTmJu0x_0bf_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rXRpFTmZtsp1Zix2Na-RVzb9idzo4xwBc3ahhFjq8znKkj8ucX2d4dv_1jcE2_25E2DN0QUcq_ZBBNHwPaD8KmQzszz-kRaUAgm-q-gC_NcYS1PXi7YXHyODVmEjHCKzWIyLfAV7UikywUVShVkBUowF0DWfrBx7xb2xa079XVREmhEOiRIxMcZEV_8-H8dF28iI0wV0SV0lSvYI6xCQKn9WwPkPHNPj8ZfMhwtc99KwMAkEIaOTOvqKu1QRnIkutAvS4qOT031ZdpOiobIi1XUCO0cCC53ibqKrDN3OreMTfcW9H5Fmlq34HmpCjHV3qpYF8lNnYm7L8Kj7raAqsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HlCRQHgRC7C77-Myl_v6uZoXz4XoFWdVU7ytqdAhDSuApg8rFDLsQVidRV7nUcsk3SYSJrvKYnJPHab93PCy-KlO9-tAGlZH29b8QbrVtWPPoroYMSos7jRJw3W1KepT10yHPslqd38a3wHjH9UtzOO8myfufA529_XQiuH5_0EDGXZShHHAOdfq4V2y6B26Mg1H2X5UnqB98T2FG6omcbENa1Do6g63D5Qn8AnTS5MetOzFoi06rpPTcqw6T9Gu2ZygkOpzZFbO0VKVIe8zWwxyMC8sro5_aa9tVr_qkbg8h0SACf1-wigcqKwb0HVWkQI-mtZBzoyb5PsAnTOLSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nzzn1EXXe8cuJbgUsDB7of-8jRZNkql7X5TE-yqhNVglb6PFqSRgX0Q7McvEYqMd8eJCj9cPlCMUQ4AjMO-lWjy-KIWcQpl6oHA3R1UHBLbGgibeOY7uMYDetjAOGuPAAe24FlE94-X7VelozmQgw6SGRf10QStInPmgoWFX-sDLQGWFmShrd14VFfScklDhdcTA0IwjgpiO1dxp2bH6iwyq4o2h5IP5Hij_knXMz2xmAYE1NndwLsEZv8frAVMecNDrfHd4iZZUjEKOUU67b8uWK-04CpNeMELMdAcNI87RQ1NFIUJSkM_Ot4Cq7ZssxJ9ADp2NY36rA4_vKvqMWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f3RjtoHNyx8-fpfKWdOhPWRNDZdDgTiVQpyLvnrjj97TS0iOnd-F7BIpBThTnykGiIM9fYYfHkE_EwzSNohikEeQZuCj1DScP6wp_ssxWdVPd6ufr6lHV9jzneaegP21dyR8FC04r1vQVqcWcNGajt-lU29hzYrVqH4r8wjSeXjQ7eTxSN_1ceXzLlIrWShFuQB1Zi5Q_vGT_amQk8vh07drMETUvadRrJfXJCDL8SLGYoFwtaVl7APhfgDtttLComLpNHlqnzOPE_F7fVUAQsALM_1p0k4lYxnZBUcbxRShigD-PE3wmHP05lUdv8CrwBA8WocI6s7y8dStRKwc6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hoSfux0N0KbMWqeSq4H26HPq97lVlztCw16OMKhwt918kLOygys4BL4zLdogJF-sg0qHkOkkOI2zbp4xSPodDqX-DZSSBnGV7QtopM89M84roQuv_VBeql160kJbe7qL92HHV5iFYz2gtPp0yVOHbylzyTViV0ccF7s14x15JB-P1E0l7APsHytHnYiKqXhLQy0ggeddXacqi0HnhZQb0Z48lyATyZfDD0tjrAfvqEdihWZ7F-auHF0vhZeNWN3x6pg60NOkAoSSJmecc7fgfEjBwT_cjh6lIed_RNKD0-X5TdHhZlOiQitHA8L3BOzMg9PEQKSVlThe05nZBdVwcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
شام‌غریبان امام شهید در بوشهر
عکس:
احمدرضا مجیدی
@Farsna</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/farsna/449050" target="_blank">📅 00:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449045">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HwNQdsoVnXdl8Hvi3ukUXWF0oXLIYZ50Ny6PzNq3yw_qptfM9iQamKDo63jfJZaX8OvTPVgV0gGP047vHLq44ticiNeue6zpFff-e3dT7b5UQbY2dJ9qoGBJPDDDUlLxsOq53SRmoxVUpoTfTLVoVLe0naFU49x3IR7DwB8pgEN4Hg7jajg5OmUxjt7w6AbAh1FCfUk2Iaima48sLTDR1CC2rlZDF6omtNF0ZDng7f2a9aZ6pMrRo9DCvfBKN-hfCdfNqv8ZtUsv2d0OMDy_uaRyEe93IOKq5Vp7JI9nCyllCxy75HRIPUFklIXeQ7Dnpd-Pf3R23ZWDFe1xLJrv9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LF1HW5ZQyMONu5Q6-9nHCK-_2o8MUXmnz1Fb5DDNrMqSyB1xTXCXIyhXyTyUxbI3q674ym2E-OPGrY0YXvGEHj7JR8zTRV59bT17pd5WqaNBUbfYiqW8NZoWORFnvmCpt-Mhk7wYA19nyjmFy0WoiACOeFCWVCeDfPG7UqMclxpUxCsFcXUilA94EaZYdRGsLthyuqaBDPSxPEqkPKppYriY6IzuBavCJNNYc7yF6cceCpPdoRWQlXP4eMtgksIPyVkJYJObw3kicWMU-R-uFUXHms89P6RbON5XgacPZvPLOnL6OJe4yBbwRonDSdF3A8INkHjD54PhbRQsKUcQ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YQS468UF7A9ztv7Jl_0WWlaUcrsOtka3lVXFjP7uB6wOnFilUjo0rGAtWdaYtQEZdfFA_t6XAAGAymRyrp-A1Baw_s3eprpqc8DrP56_qcggar5evvQQnLJg6YP-vEDFBeN5poXXUdDdhW83PmFZaraWVvD3KB2z8ZQ5b3JDXiBY-HMacxO3dkPuXIV74JqFiJfc-mqmvipVzkz29aMBCxL5mRjfFsLqNKt72F05QN1eFriOADQ1C8qmxTwwTCgWRUGJCps2ZMPKFc0G-HjL99WQVnC6OzhYix63E_CU_ixjGOXc7WTzHNluFZIbNQwrdO7S2kFnFLxevG7wH868Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aQG4giGrPze9Q2ivSFA8t4fiFyCoVpIRcD3XQJfcNzi5zaiYUgPv6zWek-kCQ_MO59Id2-1n_Bl_1DSpb1fX0X1lG0SLjON9wJkGv7L6Jltho7_ppTwr6aGQvhmqOHcgwtSzxDA3gGHfSuBDPCqsFmYgWOd_S4zXVS61w6_FiXoZimuFWU1nKtNnf-6HSjOP6JKNkzDosKHmfd3yZ30BWbyQVvQFblO1uJcd4uVbQZUP5TyIuaXGBVbigR_wMJOZADvM0_IuU9srN-KAs1vIU0miseFviK9fGBxgdMI6aoRA-I7uFkoTvhATRmHHPCnpJp4c3F-TYokoKyBjuCqTmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lt1ZeCd16wnPP2gedl3cuc4g7LRGEaiq_Yegth1sHJdOGUByP4ap5KkyFOOUw0RJOQyuVOfhNnYPhD0-8hvzUNkAkmkzQoNAuh7NUowxvIwXiUHVNu4fMDCb83EnvLLk2--00eHgzSH7ro7eOMFyRiv_r8WGAwH2g26m4fGM6svXOs8He54hhM1TwzwK6kRazNSnjE9BUBGlxbYePqCyoZH7whoxbl6HTxKuElrEeg7AfvGWOw-YIGi9bKm37UWLdNjRH1y21_WZogNBEQMbVEe7UCV_6aJe9XFaGKT3eTBSYN6PuOhSkfxlhBsGsDPI35c44QwNdNS6q0uye1747g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | شنبه ۲۰ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/farsna/449045" target="_blank">📅 00:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449038">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NlLuHnzGzbud3eGUWyjK1ZutDYJ6lu2dWCby78Cl6l-GEh91pE-vCceYRJLULuo3QtGY41KWjTpJnP6hxT68mScwfSnWWaOBLwHbBEmqN8zNgYQ4TUMpEddQ8Gc1opf9O4hnhWW4q_2lDf5xJd0U9du46Ih2aI-jr3QPwcoRfak4s29Mm_jxIEVOixrWRCsw85yqn-tcey_Q404zZW1OdhzVnf-5IClp0SmNUYnw0JA_KT9rl3OFCAc3IVKuFc0sTM1ww07Wj5RBVvCa7YIscfLohrGOxbfABd9FbiBgxbYggV3u3U0xdS3QLHDvMy97ppQbqvW0gXeisOf5TMr3KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oF0TCklrMpLD2RJMCh-FS6S69rtMYD4XMQ5-UrJRwIMAjRlEyb9j7ppReyl723tG_hqGhBT9d-POoCbnbl4vOZPTySpBq6f1NV4yW4BCvL50JIimLI92T2RTSnLqHhkDk7FjtHO2mH2dKttsU-8k8YP2DkfPT7LhHPqmrVuPBCJadi_l3CoztQuXPT2EB172obgDY9jAyyaC8LBgdSbyMc_0cUitXHX3_ymbnH_pS_B9glciKNZWGl9lG7HNSWQiju5EMitOfRPE0-PlJdpHWf-uDHjFXCZ16Yzh4KoEKzPZojE85MrDv7GduJhPFaqk85AMIqklS322_DKoeoE2nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Js4xYb9EnbvFNtQNM0D5XZ9AdXKPWBsyvC8yHjFTsctbrkPeQG9RR65XC1Vd7Lj6rc4mU-mxJkUTRx6WIV49ucwmRoON-ncED5a55JKd77GS5JTsuPtH4usHk0JL7hrAk4UockJwfXTvijsLaI-agwZPXUW-36qnEgcSXdNM5DETFPuXPlItrZWlQzI9-VIAAjxw52RGykMCPg3RythUowVzFhobiOvHzd7_vggInqVcj8JCZ3tQ05gTwN51euHh7PScdk7Z-Eq3XzuUXnx6M-02A36FhHhoPNhpJfcNODRYCTzTLLgo5m_vBbq88zi4E1pLR4xfnvjeQeCZcxlu0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WwRR71ILW6B331Zql-CKGCDkn8AyP-2sSRRWI0fhc7gEP7HByRS7JZAP_kHEiLZ3w2CkDR3lwX8zqRD1DnjlgWmFhCq_cM8cpgfbU17xrOQ3lYsWgwdKJYXvmkawee88tT2S0flgije8y-ZYRKVAgblajZhxzf2rH5QbB05rB7jwToiJLmApkJr8tZo6sO16HVKfHKXRozgyS9xmgUiO6zkxYRMZrKQsD5CC4DspN5Xk8ABiAsf9T9KgZb2wSt9ZL1NbojCO07ZvG3BsjIcMyDJ5KN58C2Zm3DBOeaJVHshvrKIhovyP3kHebvueGQEFgAQB4W-3pLEIeHDFMUIHiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pfoHXJU128k23aAx5CMdUeBKE6KBm9XZVvLInKQ9MeGlGujTSYoJAd7hkOA0hu6_Q-B_4J3nyFYDqz70qDCH0Ei0VoM3mEx8WNhLC_vxaRURk5AsRL1BdKAnCwB97AeXhz1p9kw2OoiFnm1gB9nNWQT6xojR_CO4TvIgOFQ2nBNab2XTkzMZY6Vmg4eLwGVOxhNoTQeJHBpk_v0uK-z-5W_Hu3p4K5ZlFgJ00XE9fMsQRC-JgXiFmn70x1PyutVE8iQLoJAzCKzkAszjMxsUkVSuKsOA53qqVGx5yEfWpvIPE56HIPQlO3QyFL7xZ9R_n0eOJPo9L2OlVScf3pKHYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F-EdKNmNpgcdvzk1ArrUaWCuYzLCthLYki8YkOAYGTzpAvFxghM87u-g1FnCeALlKW8e4PyZHCIqi6U93lkWl5Q5tBVmNkg7jxbVEPRTgRcnuNMM8kye40sAbqqYbbKyse07eK2VpyNhDytEuWLuiX_GJB0oXlZgWw2ROWZVolD2tSwT0sdfblVfywwQ_2cdJri0C0aY8LUMihP4DSS6OmNI5PBqHuR6fdKilByF8aSNv8kKwWT20VWdtQ_dmonz_9eDHfZfcvDeQow8lYFDtSdeJ1vIH_7_O9-OoVuJNOW0b6HjTpnwBO7OU4XAPIRG1PLbOxO7fTKfaKqMayQHMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cnvntUi8R7koTRaDjwDXuibE5m9epqeTauGKQNua-k4q157GDU9jkdUU8RX9Yn0OC9m9fag8Yuz_oGIEBjZC4pdhRMMdx9z0jf8nLYOigMnbHPBgZVRt5tz8_rMFSgPpSWlYoSdQKc_7CzP3hOyBB5LrV0O__e_vhdklC4v_0pMtZgGaPC-044E36MC5obPOIhdlpHOugZz-dQorm6nPXXjd9WnrDyjbM2adh6Mthkw-LCowICy00SrkZhuLQtu2YlwT1hhBkPuMxa4Eex1hjyqWeH_xM8g7cbI6l-vBaoW6AfEFoYjo5qHN6qjnUUl3um8WbzvGtfpOirOTEMoCGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/farsna/449038" target="_blank">📅 00:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449037">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKuA2xXhPp81YtfFv_ktnpHUP4GEQ3stBbWS5mVsoSns-2ivWmOUuDSnvkWe56JVS0YpCt8OxrN2xp6hYLA_3ftg2BoWOO1Qi7C0Cmb5tbjhytxhZ55BZViR890Mzq6BhbSop4opOh33ATRKUfcY9On4o4Er4ODMuvbySjdsn2xwYDyGR2FiN97c-1KdTW1NUf7WAY6ZJUsSY46GvFwEUj82AysngkHaNfH7s7J2VsC9PNAeiWCWJD1RYGlnsfh0YYTsQZOSnqbJA0vAeSoVOfCDNuiK1g7sFqVmcmx0WkogrOTb9R2SnTAvvxAbg6_Zsj_x68fwweCJkDFlpcs63g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلجی: تشییع ده‌ها میلیونی، پایگاه مردمی ایران در منطقه را به نمایش گذاشت
🔹
رئیس شورای اطلاع‌رسانی دولت سیزدهم: حضور مردم، چه در شب‌های حضور میدانی و چه در مراسم تشییع گستردۀ تهران، قم، مشهد و به‌ویژه عراق، پیام روشنی از ثبات جمهوری اسلامی و استمرار این مسیر با قدرت بیشتر دارد.
🔹
آمریکایی‌ها، صهیونیست‌ها و تحلیلگران جهان این واقعیت را درک کرده‌اند که ایران نه‌تنها تضعیف نشده، بلکه با اتکا به پشتوانۀ مردمی، قدرتمندتر از گذشته به مسیر خود ادامه می‌دهد.
🔹
این حضور گسترده، علاوه بر نمایش ثبات و استمرار انقلاب، بیانگر پایگاه مردمی جمهوری اسلامی نه‌تنها در داخل ایران، بلکه در سراسر منطقه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/farsna/449037" target="_blank">📅 00:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449036">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEAIVrm7Fe3S1hfhOJQJoHMlnkjx3GZV7KxfBDH9QoH6o_uhl28htL3BbDTsk6U7kqM9AXt-uwC3JXT_uZZohmo4-sqheJsw10HVreio_ZKsKykVxIgLYwltQzkOFdX_q6Jqsa5xgWVHGs2xaGA6B0x--1VwvZ_LwrwARRSqvVkdHvl-K0Bbj4_yG6GHCqwhpQ5fNlevd6Ws8fbmCgQ2sDJM763OVaQXRySnBqil9CcoQW2TIGxCjUqiLpPJWXqm2-ztXwnjopeJjTeTpdsJekUuqBKibDDnYTeweg_jKtC8GgNoUsUkeI0Qrngx5yJB8N3uViZNP6BFaylz5GRD6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
گل دوم اسپانیا در دقیقه ۸۸
⚽️
اسپانیا ۲ - ۱ بلژیک @Farsna</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/farsna/449036" target="_blank">📅 00:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449035">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de99893385.mp4?token=DaRILPOLFnAf2codxLkj8l-khDCnKZSwixIuLZwSE2o7jhyWwnxREKHTGlY9DJmoGwM9g1ic1KRLZHic4fJ9ebhBxWSEZXLrX213R3-VJGLwJz1FPR7RjwR44qxO2HKq9KWQ8bNt2V0y2GVihl932r0St5t2SqBY-jYT2l3qCt6JMRAmzVMI7iWNwd0sJshCZPSfrpc9wFtKdJs5DMYVUXnFChoiM3DJWprJp4ymF_UTg_sUhy2m3n7kCUgFOl0x4LQStKCyTJaPvIX8mava19yQ8EKBCMnB67Uh32mWfmALZ-7hkty3W9SW1koao9G9uXr4kKnVumBvs3ewGerIHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de99893385.mp4?token=DaRILPOLFnAf2codxLkj8l-khDCnKZSwixIuLZwSE2o7jhyWwnxREKHTGlY9DJmoGwM9g1ic1KRLZHic4fJ9ebhBxWSEZXLrX213R3-VJGLwJz1FPR7RjwR44qxO2HKq9KWQ8bNt2V0y2GVihl932r0St5t2SqBY-jYT2l3qCt6JMRAmzVMI7iWNwd0sJshCZPSfrpc9wFtKdJs5DMYVUXnFChoiM3DJWprJp4ymF_UTg_sUhy2m3n7kCUgFOl0x4LQStKCyTJaPvIX8mava19yQ8EKBCMnB67Uh32mWfmALZ-7hkty3W9SW1koao9G9uXr4kKnVumBvs3ewGerIHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرانجام دروازه اسپانیا در دقیقه ۴۱ باز شد
⚽️
اسپانیا ۱ - ۱ بلژیک @Farsna</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/farsna/449035" target="_blank">📅 00:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449034">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تصادف ۲ اتوبوس حامل زائران عراقی در محور سبزوار
🔹
اورژانس سبزوار: برخورد دو دستگاه اتوبوس با یکدیگر منجر به مصدومیت ۱۲ نفر شد که ۱۰ مصدوم در محل حادثه سرپایی درمان و ۲ نفر نیز به بیمارستان منتقل شدند.
🔹
اتوبوس حادثه دیده مربوط به زائران عراقی مراسم تشییع رهبر شهید بود که بعد از این حادثه، به موکب نماز جمعه جهت تکریم اعزام شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farsna/449034" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449033">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c53005e601.mp4?token=RI8WIRQD4-kkAXElZRZBYXZ8-jhDqKCCE6-w0RqTMl3VLBrI-uKUl4bQQn1W8IHLrYeowx_tyo448bHkp3MIxhrXgpopOtxbwWFqO9SrnSHet7Q6j2u9Jti1EMXU3VMqXw3YutqUMW2esPuUGbLIsdiGQ2i3zq9pQtDDsqpgzf3Gs0DJ-LMeh9Cjwln_3ZA4ttuDXYZJNSu13mqqaGXm7SAwj195SGkOl_LQ3wsKuCWxTUVqyFy_UQkCLi5yp43kjNLR13dVxSL7XaaaqK994Em51ofU7IJhVoZXalDnODeIcBv7tVcBRLN6mK2oTSuqyIla86b3M55XFcsnGV6mKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c53005e601.mp4?token=RI8WIRQD4-kkAXElZRZBYXZ8-jhDqKCCE6-w0RqTMl3VLBrI-uKUl4bQQn1W8IHLrYeowx_tyo448bHkp3MIxhrXgpopOtxbwWFqO9SrnSHet7Q6j2u9Jti1EMXU3VMqXw3YutqUMW2esPuUGbLIsdiGQ2i3zq9pQtDDsqpgzf3Gs0DJ-LMeh9Cjwln_3ZA4ttuDXYZJNSu13mqqaGXm7SAwj195SGkOl_LQ3wsKuCWxTUVqyFy_UQkCLi5yp43kjNLR13dVxSL7XaaaqK994Em51ofU7IJhVoZXalDnODeIcBv7tVcBRLN6mK2oTSuqyIla86b3M55XFcsnGV6mKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جلیلی: معیشت بدون امنیت و دفاع از حاکمیت کشور به‌دست نمی‌آید
🔹
قراردادن خط خون‌خواهی مقابل معیشت، نوعی تحجر است؛ تحجر یعنی شما یک پاسخی برای یک سوالی داشته باشید و اگر ۱۰ بار تجربه نشان داد که پاسخ‌تان غلط است بازهم آن را تکرار کنید.  @Farsna</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/449033" target="_blank">📅 00:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449032">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea766c1af2.mp4?token=t_AxHu4RxoIvTQJ2kkSQnYW9FIDYkZ2Q8FPMOmuarx0CbAJSmThrZILXeA7UcWLv22w7w4nJj6scykJlFq98pup_zs7C6JlRtjgFyumYZjUWXa-XBXV9WqI_R3OMYI0Z5Vwa9VNlcPO9FCfl4jH3ZueKnMRrlL0eVsX3fXupSUnPUTaIw_0C4S6sxZLsGUHA-jI6eV2yAwCkQ-9Um-LwuBff_c_cNr6tyDcpZtlJmSwvNIrClwWmwYzeulaBrsC9MpRVwDIHBmxkwj1zYuzIbTze3gkTZufhWNW5OueYDD24l9AchaAA8zp-PYfIrz0y-Y_FL5nY0PFxwA1K94TWOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea766c1af2.mp4?token=t_AxHu4RxoIvTQJ2kkSQnYW9FIDYkZ2Q8FPMOmuarx0CbAJSmThrZILXeA7UcWLv22w7w4nJj6scykJlFq98pup_zs7C6JlRtjgFyumYZjUWXa-XBXV9WqI_R3OMYI0Z5Vwa9VNlcPO9FCfl4jH3ZueKnMRrlL0eVsX3fXupSUnPUTaIw_0C4S6sxZLsGUHA-jI6eV2yAwCkQ-9Um-LwuBff_c_cNr6tyDcpZtlJmSwvNIrClwWmwYzeulaBrsC9MpRVwDIHBmxkwj1zYuzIbTze3gkTZufhWNW5OueYDD24l9AchaAA8zp-PYfIrz0y-Y_FL5nY0PFxwA1K94TWOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: آمریکا تفاهم‌نامه را نقض کرده و ما هیچ تعهدی را بدون مابه‌ازا اجرا نمی‌کنیم
🔹
رویکرد ما تعهد در برابر تعهد است. اگر طرف مقابل تعهداتش را نقض کند متقابلا ایران همان کار را انجام خواهد داد. @Farsna</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/449032" target="_blank">📅 00:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449031">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: ایران اجازه بازرسی از تاسیسات آسیب‌دیده ناشی از حملات آمریکا و رژیم صهیونیستی را نمی‌دهد
🔹
قطعنامه ۲۲۳۱ منقضی شده و عملا وجاهت حقوقی ندارد. @Farsna</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/449031" target="_blank">📅 23:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449030">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: پیمان‌شکنی آمریکا یک عادت است
🔹
آمریکا با حمله به ایران، لغو معافیت تحریم نفتی و اعمال تحریم‌های جدید تفاهم‌نامه را نقض کرده است. @Farsna</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/449030" target="_blank">📅 23:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449029">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: ما هیچ درخواستی برای مذاکره با آمریکا نداشتیم اما سفر میانجی را به ایران پذیرفتیم. @Farsna</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/449029" target="_blank">📅 23:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449028">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🖼
مرندی، کارشناس نزدیک به تیم مذاکره‌کننده: ترامپ و آکسیوس را نادیده بگیرید؛ تا وقتی دولت ترامپ به تعهداتش عمل نکند، هیچ مذاکره‌ای انجام نمی‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/449028" target="_blank">📅 23:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449027">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa65d719cf.mp4?token=BUYwUpWy9K3D9IpAdwDuvlE9QE24S99Lf9wNZpuhP2lRWS3zXItuAfyHqDf9z5_de5MM_kaCVxP05eL2vtvvFs67iJf0F2pTeF404U8wCEJSrmL-cqp2Y2G3VKeVbw-6GqhGgtsPiGEIc9OzYDTj2rAT0GkjJpbNoVy65Db99Ijn4Qsx_0IyQWZmfyReggkiMt9MkHHP5xdP9KioHUcUbfB9nUskz6fJPyHU3XRIXitg7K26Qn0LdHvzyzP25tCnevmxYIvv46Wqx0Mvb9VdtAhbussfV09LmEKLKutegckhrZ3yykotNa_q-gEwmziAhwDhfD2ujOyWkYw6XHGcPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa65d719cf.mp4?token=BUYwUpWy9K3D9IpAdwDuvlE9QE24S99Lf9wNZpuhP2lRWS3zXItuAfyHqDf9z5_de5MM_kaCVxP05eL2vtvvFs67iJf0F2pTeF404U8wCEJSrmL-cqp2Y2G3VKeVbw-6GqhGgtsPiGEIc9OzYDTj2rAT0GkjJpbNoVy65Db99Ijn4Qsx_0IyQWZmfyReggkiMt9MkHHP5xdP9KioHUcUbfB9nUskz6fJPyHU3XRIXitg7K26Qn0LdHvzyzP25tCnevmxYIvv46Wqx0Mvb9VdtAhbussfV09LmEKLKutegckhrZ3yykotNa_q-gEwmziAhwDhfD2ujOyWkYw6XHGcPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جلیلی: انتقام‌ و پاسخ به جسارت دشمن، کمکی به حق حاکمیت همه ملت‌هاست که آمریکا بداند چنین کاری بدون هزینه نیست.  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/449027" target="_blank">📅 23:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449026">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb55b22145.mp4?token=Aqrxu5Y_qRhKldwvsLB2qutZ64Fiy6VFZFgeQtJY_tUCgY0hdy6Fb49y0ypWo-r2kwu22lXqyqotIO95YKmX8h1ongeZVBa5eRms0Z5iM4vksM5HhHJqno3beTEGra8Qtc58BHh1SSh9Va8YFko6Jz96any0bg7dKIZQWbdcvf_BPIRf9xLghvMg_p_Yx36DRgZg5HE_P23dSWzP3qkHpiQKNQvlB_LpdeuXAHHLRDC5yj82WPhBVFECZUh3PrUdAOzUI37_lNOOig_6vj3QValFS6P6YaLsYPHCjLgUvJLXSHrzHWKpqUtmRcrg5utu7LyU728NKppdS3j1oW52YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb55b22145.mp4?token=Aqrxu5Y_qRhKldwvsLB2qutZ64Fiy6VFZFgeQtJY_tUCgY0hdy6Fb49y0ypWo-r2kwu22lXqyqotIO95YKmX8h1ongeZVBa5eRms0Z5iM4vksM5HhHJqno3beTEGra8Qtc58BHh1SSh9Va8YFko6Jz96any0bg7dKIZQWbdcvf_BPIRf9xLghvMg_p_Yx36DRgZg5HE_P23dSWzP3qkHpiQKNQvlB_LpdeuXAHHLRDC5yj82WPhBVFECZUh3PrUdAOzUI37_lNOOig_6vj3QValFS6P6YaLsYPHCjLgUvJLXSHrzHWKpqUtmRcrg5utu7LyU728NKppdS3j1oW52YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پدر زهرای ۱۴ ماهه در مراسم تشییع همسر و فرزندش به‌همراه امام مجاهد و شهید انقلاب  @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/449026" target="_blank">📅 23:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449025">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be1f11561f.mp4?token=KGYaFzVQw4zfBv82SkZTQ9Cz-ejBQYQUZKnwJt_dPQc6tKKRT6NRmPeYGhx6Zs6LM8awIvRn1O28pCGOzHa-Cn3xrkrd8DINUtbTng65T2ze8mphlDJvXjaHbNk2A-TLzz7Dn88eAk6QBuTfBwPA1yPiMDNO8RVB0j7HdnfXxEUofdFi_h4GLGjcmtyQ32ZzAL567UdMc5MOmvCZIpPOBp5UcN8gHUgxMdkV7pLws6cQDrKSWSXUaxoDSX7_maL-KNHDJ_grlyTbMDMJzrD2s6Lh1euj6Qa3zGiqH-aOGkVzpp_MRLcJZ_nkU-64ZKtcWElByW1a8ucgECOXoPtPUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be1f11561f.mp4?token=KGYaFzVQw4zfBv82SkZTQ9Cz-ejBQYQUZKnwJt_dPQc6tKKRT6NRmPeYGhx6Zs6LM8awIvRn1O28pCGOzHa-Cn3xrkrd8DINUtbTng65T2ze8mphlDJvXjaHbNk2A-TLzz7Dn88eAk6QBuTfBwPA1yPiMDNO8RVB0j7HdnfXxEUofdFi_h4GLGjcmtyQ32ZzAL567UdMc5MOmvCZIpPOBp5UcN8gHUgxMdkV7pLws6cQDrKSWSXUaxoDSX7_maL-KNHDJ_grlyTbMDMJzrD2s6Lh1euj6Qa3zGiqH-aOGkVzpp_MRLcJZ_nkU-64ZKtcWElByW1a8ucgECOXoPtPUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول اسپانیا به بلژیک توسط فابین رویز در دقیقه ۳۰
⚽️
اسپانیا ۱ - ۰ بلژیک @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/449025" target="_blank">📅 23:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449024">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔸
کسی که کشت امام مرا چرا نکشیم
🔸
که ننگ ماست اگر قاتل تو را نکشیم
🔸
از این به بعد کفن، جای جامه بر تن ماست
🔸
قسم به خون تو، قتل ترامپ گردن ماست
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/449024" target="_blank">📅 23:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449023">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35ff73123c.mp4?token=nn_PeWdFQuLNCY0fLxuPxYC_8auFcnStiThxPuHzL02ssPPVo570Wl5qhdLvvuG3-JiNLaQuEHEJSJgr5vWLMdX-V-Q8JLwQMoxy6By8m-usa5hK25mkCwbhMEeBDxdEQSs9sVtSzIvAgL5Ks_nDmEVhEoEjWnWuU1BRIiX4ptbgu-DaIZ3ETwOKqQzDvg1A2ahYCfba9G6mTaanqMKOpyHPBfaTwpw4_ESH7ecFkyxHxB_AbuS-rTyk71BEo2OtIHhHwLwtQNyq1qWGAXG3A5KOYBNolOBUm35jtKTvm-CbYRc9A--lwqIEooPl6tBpxjjrFO7_DmZLV7vths7c7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35ff73123c.mp4?token=nn_PeWdFQuLNCY0fLxuPxYC_8auFcnStiThxPuHzL02ssPPVo570Wl5qhdLvvuG3-JiNLaQuEHEJSJgr5vWLMdX-V-Q8JLwQMoxy6By8m-usa5hK25mkCwbhMEeBDxdEQSs9sVtSzIvAgL5Ks_nDmEVhEoEjWnWuU1BRIiX4ptbgu-DaIZ3ETwOKqQzDvg1A2ahYCfba9G6mTaanqMKOpyHPBfaTwpw4_ESH7ecFkyxHxB_AbuS-rTyk71BEo2OtIHhHwLwtQNyq1qWGAXG3A5KOYBNolOBUm35jtKTvm-CbYRc9A--lwqIEooPl6tBpxjjrFO7_DmZLV7vths7c7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهار آتش‌سوزی مینی‌پالایشگاه اکسین پلدختر
🔹
مدیر ایمنی شرکت شهرک‌های صنعتی لرستان اعلام کرد آتش‌سوزی مینی‌پالایشگاه اکسین پلدختر مهار شد.
🔹
آتش‌سوزی تنها بشکه‌های حاوی روغن سوخته را درگیر کرده و به تأسیسات و مخازن پالایشگاه سرایت نکرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/449023" target="_blank">📅 23:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449022">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مخالفت روسیه و چین با فشار غرب برای استفاده از شورای امنیت علیه ایران
🔹
روسیه و چین روز جمعه با برگزاری نشست شورای امنیت سازمان ملل درباره ایران که از سوی کشورهای غربی حمایت می‌شد، مخالفت کردند.
🔹
این دو کشور تأکید کردند که قطعنامه ۲۲۳۱ در اکتبر ۲۰۲۵ منقضی شده و این شورا دیگر هیچ مأموریتی برای بررسی پرونده هسته‌ای تهران ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/449022" target="_blank">📅 23:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449021">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b00339ed1a.mp4?token=hBr_7jBj6E6b2qqpz3aWuXfm8GNoPLesC3_3tPhB9rIF9XPyztKTM7BXZXcG_N1dH4zyWVDv2OHHfKrVDQdZh_Rm6nhwgaTOaKGdsohrSK0OcRY9VoGIm4rRP7XKhCM_qW09CjMKoA8bp2jKwpNBE6A5ktNqHl0yYdLEVjZOlGJAKp_aL_UIihD6p0Qga1NflLUtGq_WhuakHEO9ptmX-rV6GNKPY5bf3sZkEUShNy0Rtd808i_3KFr02_LiNSUHl-O7Nlj9yCxkDf9r-h5-HVoUAzrhli0sVqJ-AxhvbnG0-k3nYNo98VvbKYVd-Ai5xDJ-mZz_gInOFegdVkhTYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b00339ed1a.mp4?token=hBr_7jBj6E6b2qqpz3aWuXfm8GNoPLesC3_3tPhB9rIF9XPyztKTM7BXZXcG_N1dH4zyWVDv2OHHfKrVDQdZh_Rm6nhwgaTOaKGdsohrSK0OcRY9VoGIm4rRP7XKhCM_qW09CjMKoA8bp2jKwpNBE6A5ktNqHl0yYdLEVjZOlGJAKp_aL_UIihD6p0Qga1NflLUtGq_WhuakHEO9ptmX-rV6GNKPY5bf3sZkEUShNy0Rtd808i_3KFr02_LiNSUHl-O7Nlj9yCxkDf9r-h5-HVoUAzrhli0sVqJ-AxhvbnG0-k3nYNo98VvbKYVd-Ai5xDJ-mZz_gInOFegdVkhTYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جلیلی: رهبر شهید کاری کرد که کسی نتواند مثل جنگ جهانی دوم ایران را اشغال کند.  @Farsna</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/449021" target="_blank">📅 23:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449020">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94cbd0b246.mp4?token=nMQp17w2Fi6H6WX0xrswPdBDgLjIXsV37stUTRBsKihfuiAOWoareoAGa6HPpyiReIHTO4PE2izelhzUuSmTzNGgJgdh9omWuok1gI6JBP9vT74XPE2fUXe4ZS2wtPndmg0QWUHKGG8m7-2mkiH3OC25LgYtjKnu3ep81mnsHdwsXQ3D8gXApGv-CU3yroXwb1rNLgFXpaythL0Q6yZ4VB-nMFOa1Q4KBxVC86rRhgBIMMC28u648R0SMGZgcyeqfdVXLcPjqSDs9jA3AwMBVILTvyxWvQvahKxlVMLtx5I3BGfV74veqk4q17Gk-ydaap00P1fUqtfNUksjVNtttA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94cbd0b246.mp4?token=nMQp17w2Fi6H6WX0xrswPdBDgLjIXsV37stUTRBsKihfuiAOWoareoAGa6HPpyiReIHTO4PE2izelhzUuSmTzNGgJgdh9omWuok1gI6JBP9vT74XPE2fUXe4ZS2wtPndmg0QWUHKGG8m7-2mkiH3OC25LgYtjKnu3ep81mnsHdwsXQ3D8gXApGv-CU3yroXwb1rNLgFXpaythL0Q6yZ4VB-nMFOa1Q4KBxVC86rRhgBIMMC28u648R0SMGZgcyeqfdVXLcPjqSDs9jA3AwMBVILTvyxWvQvahKxlVMLtx5I3BGfV74veqk4q17Gk-ydaap00P1fUqtfNUksjVNtttA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول اسپانیا به بلژیک توسط فابین رویز در دقیقه ۳۰
⚽️
اسپانیا ۱ - ۰ بلژیک
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/449020" target="_blank">📅 23:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449019">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پزشکیان: احترام متقابل و التزام عملی به تعهدات، پیش‌شرط هرگونه توافق پایدار و موفق خواهد بود
🔹
رئیس‌جمهور در گفت‌وگو با نخست‌وزیر پاکستان: در شرایط کنونی، در کنار تلاش‌های دیپلماتیک برای تثبیت آتش‌بس و جلوگیری از گسترش بحران، روند دوگانه‌ای شکل گرفته که از یک سو رژیم‌صهیونیستی و جریان‌های حامی سیاست‌های تنش‌آفرین و از سوی دیگر دولت آمریکا با عدول از تعهدات خود درصدد برهم‌زدن روندهای موجود و جلوگیری از استقرار آرامش در منطقه هستند.
🔹
انتظار طبیعی آن است که سایر طرف‌ها نیز به تعهدات خود پایبند باشند و از اتخاذ مواضع یا اقداماتی که موجب تضعیف اعتماد و پیچیده‌تر شدن روندهای دیپلماتیک می‌شود، پرهیز کنند. احترام متقابل و التزام عملی به تعهدات، پیش‌شرط هرگونه توافق پایدار و موفق خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/449019" target="_blank">📅 23:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449018">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJRSqqg9ZyzB9R5L2WosoRW-cJkQlhZY9JvmmwUwrML5R0MWFtESyz1dkKZy7C9wIKhb0KFVxWY90CnhTuFiS2wjtQJAddC-KquudS57hckzZllNDmK_v7-3x8lo7ha91XjNYkiCvYXnCd2QcaGdTKvmkNycTWFwwkmuwSusgJMLGFWMYRxTgx_jguopFda2hzWsuNMSWdSrv93AW8Wy_oswtZzX4dxbqwASVO67bkZoq3kAlcEif1ESt_c8m5paoTXXqObOsCXqeR24sAaqR7pgy6hNykELp_JgFNNdKaZb-NNPKPESOaowh6BPy97gQVQLx-esP2c1OmkQZzaOyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
معاون وزیر خارجه: سند جدید آمریکا برای ارتقای رتبه تجاری امارات به پاداش پشتیبانی از تجاوز نظامی علیه ایران، مایهٔ رسوایی ابوظبی است؛ امارات باید پاسخگو باشد.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/449018" target="_blank">📅 22:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449017">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91e36e4e81.mp4?token=nXUXWxL9833H5Ta3JoH243OF6mESqao_gA4F9-a5J4-sCkq45iBuPW0tvy1by8YLGEYHjvtRvA6aTRxoybJuX9rhCki9gZWsgyOQikvFCivdPybRr5RT2hLPzUQIVLC4Ggo9mWpAkaQTIu60Oeta2YGmgQI_9kKuQQgYfJt1n2twSOIBzQ9R_PRanNMCw-ZMagGYiTwr-3cuXKu8FPlzm9p0h2Ae4Gq8VISnNOkn6oEDDy7Dl_PR5E43GdZb3ct7mT3KoV6KTIwG5KghVgclRnyIdGtrmdq-h1-Myq0IvpzhuZANE1koq_MIQ40K_x5A7nWTX2kIHh82ffr8LIHE2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91e36e4e81.mp4?token=nXUXWxL9833H5Ta3JoH243OF6mESqao_gA4F9-a5J4-sCkq45iBuPW0tvy1by8YLGEYHjvtRvA6aTRxoybJuX9rhCki9gZWsgyOQikvFCivdPybRr5RT2hLPzUQIVLC4Ggo9mWpAkaQTIu60Oeta2YGmgQI_9kKuQQgYfJt1n2twSOIBzQ9R_PRanNMCw-ZMagGYiTwr-3cuXKu8FPlzm9p0h2Ae4Gq8VISnNOkn6oEDDy7Dl_PR5E43GdZb3ct7mT3KoV6KTIwG5KghVgclRnyIdGtrmdq-h1-Myq0IvpzhuZANE1koq_MIQ40K_x5A7nWTX2kIHh82ffr8LIHE2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جلیلی: رهبر شهید کاری کرد که کسی نتواند مثل جنگ جهانی دوم ایران را اشغال کند.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/449017" target="_blank">📅 22:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449016">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c63629abe.mp4?token=aFi98Z86oVzs_qZ-aNw9BCT9r0QlQAlHxIeT2XiTk4kGMseSmxf_XoV7IWZSPdcKhKHach-fxGSTA1ITPimCUJ-3rb2E1qnzoWO-5GNxTF-tfMi6-C0497ZWwsJ59rRnfJwcooGh-UNIQWrQ7DcOQNdMtCT_mkQKvGvASPpbuX99B4UfHGZpE9oA4I9RNscnXtMwyCUrIHE2CFfK-dIV7sbbP1ZP_lqBEsi504Nm99Qzx87P0KLHhTRATbI_PqMRqtoJk1q52bUmIJ08pupB4xTdD3P6VPBpec1ijjDSmKnnVVzJZNakKXufsbNWqaIJTjBjodJn_TBwaDkMunTJNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c63629abe.mp4?token=aFi98Z86oVzs_qZ-aNw9BCT9r0QlQAlHxIeT2XiTk4kGMseSmxf_XoV7IWZSPdcKhKHach-fxGSTA1ITPimCUJ-3rb2E1qnzoWO-5GNxTF-tfMi6-C0497ZWwsJ59rRnfJwcooGh-UNIQWrQ7DcOQNdMtCT_mkQKvGvASPpbuX99B4UfHGZpE9oA4I9RNscnXtMwyCUrIHE2CFfK-dIV7sbbP1ZP_lqBEsi504Nm99Qzx87P0KLHhTRATbI_PqMRqtoJk1q52bUmIJ08pupB4xTdD3P6VPBpec1ijjDSmKnnVVzJZNakKXufsbNWqaIJTjBjodJn_TBwaDkMunTJNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
به رهبر شهید ایران سلام، سایه سیدمجتبی مستدام
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/449016" target="_blank">📅 22:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449015">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mhs5EunX7oJ12BhR_mOqi7oLIJoZWLcVvfGU447CmhRaZ0EjKhSA9kmn7ENjLQRhTs5G28sz_4N1FIu_fcbnfVsQBk2rLugz8srBacdnKG-u0KnRGs94lIGIVCwczWmohWkfOxMkWpv4nAqLWFS2Poi2oA3Ox0-NDFNTxUybMn_CP4aD-aVCygvApeuxgjz9pvMwkkLOu0FYQ-Zw9RAybKMOy509dDAL5O54wOyMuYfVrJtvOIKNia2ElpLzgjbAVVfnJfcrxSvmn7iEN6bPz_d61gxNqYZ4nJzo4a5BfahnHG-rWBQyD2FkGI490V8nY60nWb5mK6J-FL2FV6Qvzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ بازهم در جهان موازی درخواست ایران برای مذاکره را پذیرفت!
🔹
رئیس‌جمهور آمریکا مدعی شد که ایران از دولت او خواسته مذاکرات ادامه پیدا کند.
🔹
او مدعی شد: «ما با مذاکره با ایران موافقت کردیم اما به صراحت اعلام کردیم که آتش‌بس پایان یافته است». @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/449015" target="_blank">📅 22:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449014">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1efc24d831.mp4?token=ZVLA2Mm72_MNyYhlZh4f6MeXcwqlo3D3J_4VcIK3qnNSyuoFKEseHRDgfZkY-Ok0DRRmRqpt0KIPHe6EF6sjfK_s9pjq02sU7cfNQkD5KbAX-KY140lz2L2pEK2WHnnWMyetQTPQo-c3SSXaN_drih0Z49xqi9w7UfMVa1BoJbrjWXd-UpBoePUP9dxXIlqim8yR1KnG8XEwNl_WBaOvlxhdza0sc03mGPM0kQF34RJfvOB13wiyq_t5Sj7x15p0iPkZ_jONIb2FnHPxlDdfK369SCbGqK68SSEVPCneafKgGQl1-K1jL5qYGmBNTf3WvfHDQMBPSOkBZIC4lANCOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1efc24d831.mp4?token=ZVLA2Mm72_MNyYhlZh4f6MeXcwqlo3D3J_4VcIK3qnNSyuoFKEseHRDgfZkY-Ok0DRRmRqpt0KIPHe6EF6sjfK_s9pjq02sU7cfNQkD5KbAX-KY140lz2L2pEK2WHnnWMyetQTPQo-c3SSXaN_drih0Z49xqi9w7UfMVa1BoJbrjWXd-UpBoePUP9dxXIlqim8yR1KnG8XEwNl_WBaOvlxhdza0sc03mGPM0kQF34RJfvOB13wiyq_t5Sj7x15p0iPkZ_jONIb2FnHPxlDdfK369SCbGqK68SSEVPCneafKgGQl1-K1jL5qYGmBNTf3WvfHDQMBPSOkBZIC4lANCOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدای منتظرانت، صدای خونخواهی‌ است...
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/449014" target="_blank">📅 22:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449013">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58dcb9d425.mp4?token=OX7taRwoDSq06vs1zLzpEBKF0kPBCjTKU1_v2nOttK5RLENxyeRAxg5BT2YkLWr73xTG5Xf482383Ol-fu0qU-ZAnWRYouynfElv9UnRSYgXNlMwCEYlz90jo0muaTvLPSDj-Qqgd23lnTFL6xx_u7Ow6g6BM4bcqfylFyeU4o-m1p6bOMoA7W1a2Ug4Z9IGQhsE6H4g_xvt_ihakGcXftnn-8MMCuKSQ8s7XBJtt9OZ_hGnmNTe345yl62dt6rtM2OFqc_S4PjoMrFWfCVz_dgcQDK8j-i9wXHj7i_N-BJlJeCJop64aWU_ZbrR3ip-ocHxTBHFA2GIqkSEAL5XMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58dcb9d425.mp4?token=OX7taRwoDSq06vs1zLzpEBKF0kPBCjTKU1_v2nOttK5RLENxyeRAxg5BT2YkLWr73xTG5Xf482383Ol-fu0qU-ZAnWRYouynfElv9UnRSYgXNlMwCEYlz90jo0muaTvLPSDj-Qqgd23lnTFL6xx_u7Ow6g6BM4bcqfylFyeU4o-m1p6bOMoA7W1a2Ug4Z9IGQhsE6H4g_xvt_ihakGcXftnn-8MMCuKSQ8s7XBJtt9OZ_hGnmNTe345yl62dt6rtM2OFqc_S4PjoMrFWfCVz_dgcQDK8j-i9wXHj7i_N-BJlJeCJop64aWU_ZbrR3ip-ocHxTBHFA2GIqkSEAL5XMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سید علی خمینی: تا وقتی که رهبری معظم انقلاب در مورد پایان تجمعات چیزی نگویند، تجمعات خیابانی ادامه خواهد داشت.  @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/449013" target="_blank">📅 22:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449012">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1eb35161a.mp4?token=aSp1D8XNZHgE1CHbULxPevIxeHaJxINlTFCfvuLVJZ4LknfbiJmEqjSn5tVLdlOBxZeCLDXu9yldsduMtxA5ZlhW8pf4uLEa6D0gHrPpY06zwkayPx7Eh7FWkvPrKmDUKzQfBlrxK46o4kUbd-hr5P7P2lOVqKgddaw2w0wRfLHSHQ0bkgFG8FJjo2Nx-OUYrb9xc3zfv4IUv20WL-pN4obACENyCpk0SjJvDRjs80fjlk_RlK6sO_rs9Ej2-K-NHCCDI_gHo3sha2ZZDLw1vhZo9FTO-eAprhlNRth3wNZxAW-bWbHQXrnJactUUm3BxN-QkKRsDYwcNZEdrxMppA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1eb35161a.mp4?token=aSp1D8XNZHgE1CHbULxPevIxeHaJxINlTFCfvuLVJZ4LknfbiJmEqjSn5tVLdlOBxZeCLDXu9yldsduMtxA5ZlhW8pf4uLEa6D0gHrPpY06zwkayPx7Eh7FWkvPrKmDUKzQfBlrxK46o4kUbd-hr5P7P2lOVqKgddaw2w0wRfLHSHQ0bkgFG8FJjo2Nx-OUYrb9xc3zfv4IUv20WL-pN4obACENyCpk0SjJvDRjs80fjlk_RlK6sO_rs9Ej2-K-NHCCDI_gHo3sha2ZZDLw1vhZo9FTO-eAprhlNRth3wNZxAW-bWbHQXrnJactUUm3BxN-QkKRsDYwcNZEdrxMppA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرائت دست‌نوشته عاشقانه رهبر شهید انقلاب در وصف امام حسین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/449012" target="_blank">📅 22:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449011">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b20077aff3.mp4?token=Yb-AyW-83jZ3-xTFHka8qG6mfavwgd9b7Ir7R5_JV6o68bpMv4mJ8WZT24V28dH_nY_NX-c6ueBJZKIqZ20wqb-7ZoliK9K6Y4zjx--HR-F_BUnzcecCvib_fFqc-QRhYCfupP4h8YA0Adh6_lwjZp7EmO9WgX28LQ3WQxPvWzCEAqr9_PS3Nfaz2ALTDaSeJdHBsOS6cqSbvRg22NSFXXnz0IMJ34fzC342zb24esms_f-PaBFJCgTAADs7Di-MUDb8z66ZtxFYQtV97BJPjFhnnYemk6-9XcdMrgSwDcgD2rI3IrEztQAeVA5bYkk_dQImAXCeZVANz-8qdldamw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b20077aff3.mp4?token=Yb-AyW-83jZ3-xTFHka8qG6mfavwgd9b7Ir7R5_JV6o68bpMv4mJ8WZT24V28dH_nY_NX-c6ueBJZKIqZ20wqb-7ZoliK9K6Y4zjx--HR-F_BUnzcecCvib_fFqc-QRhYCfupP4h8YA0Adh6_lwjZp7EmO9WgX28LQ3WQxPvWzCEAqr9_PS3Nfaz2ALTDaSeJdHBsOS6cqSbvRg22NSFXXnz0IMJ34fzC342zb24esms_f-PaBFJCgTAADs7Di-MUDb8z66ZtxFYQtV97BJPjFhnnYemk6-9XcdMrgSwDcgD2rI3IrEztQAeVA5bYkk_dQImAXCeZVANz-8qdldamw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سید علی خمینی: مشکل ما با آمریکا از زمان کودتای ۲۸ مرداد آغاز شد و الان ما با آمریکا پدرکشتگی پیدا کرده‌ایم.  @Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/449011" target="_blank">📅 22:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449010">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9b1283110.mp4?token=TXpugDeMq0_3TLRk0fuKW23VUMXCHGgUQoIuyXOZSQMD1_bJ9jkxR56EbnITNc2fhat7GES5K9RKQnTeMSAipEW-IZUlG6xhzzuYeRFe3gU22JGjfFClYowINX9o34f5goEwleLfQq2m8sFAfi_1qfgklzGqFwxDoQAYnPn95aqed0TF1kUnpgzpryrfrrIpxLp8m-_IKCei2vzDYem2Zlevs75XY2J9lwGLMm_TcWacKRn_GRFmF1s53MhOZMoU8s4rrQqXGZFlMTjWtf-oLPmtv7Lexuivpb5yh__rP4sR1eoqYvKLv6btgaU2P6H69uFy8KuDUifNqECUeiwIqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9b1283110.mp4?token=TXpugDeMq0_3TLRk0fuKW23VUMXCHGgUQoIuyXOZSQMD1_bJ9jkxR56EbnITNc2fhat7GES5K9RKQnTeMSAipEW-IZUlG6xhzzuYeRFe3gU22JGjfFClYowINX9o34f5goEwleLfQq2m8sFAfi_1qfgklzGqFwxDoQAYnPn95aqed0TF1kUnpgzpryrfrrIpxLp8m-_IKCei2vzDYem2Zlevs75XY2J9lwGLMm_TcWacKRn_GRFmF1s53MhOZMoU8s4rrQqXGZFlMTjWtf-oLPmtv7Lexuivpb5yh__rP4sR1eoqYvKLv6btgaU2P6H69uFy8KuDUifNqECUeiwIqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سید علی خمینی: هرکس بخواهد مذاکره کند برای اینکه با آمریکا به صلح برسد او خائن است
🔹
هرکس پیام دوستی به آمریکا بفرستد دهانش خبیث و نجس است. @Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/449010" target="_blank">📅 22:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449009">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">آمریکا تحریم‌های جدیدی علیه ایران اعمال کرد
🔹
دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا اعلام کرد اسامی ۸ فرد و ۶ شرکت را در فهرست تحریم‌های مرتبط با ایران قرار داده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/449009" target="_blank">📅 22:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449008">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9575683bac.mp4?token=dxeWTA8RVfRT0AtKW-iW9asomIyTkwE5RPd8hPvz3C3XLIay2MSQapGohKQ0k5YCDBLBwB1gZy04ld_FgvPoZ9bdbPy5zlegKmoQiz8R2ysWZTBDJU-HG0uXTjo-EYFk9625kkJD8GInyWwZy6pOF1gmEbVA4gJZWkhKiagdCjhhbJeH5fZE3_5N7hFw0M5fPb5TCXXU2Bi2mXmetROH_b8L_6kvQz0AoXMZpJ25gIHjdBI8CDlbHtpW3lUMtSqfYobABuevAg9dOsU-SgLqgJSM8PHhYsEqTvM72OO_cJ6Lpa-Er8xOofymtJcMA38flc59p4x7juR2Vv27blunqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9575683bac.mp4?token=dxeWTA8RVfRT0AtKW-iW9asomIyTkwE5RPd8hPvz3C3XLIay2MSQapGohKQ0k5YCDBLBwB1gZy04ld_FgvPoZ9bdbPy5zlegKmoQiz8R2ysWZTBDJU-HG0uXTjo-EYFk9625kkJD8GInyWwZy6pOF1gmEbVA4gJZWkhKiagdCjhhbJeH5fZE3_5N7hFw0M5fPb5TCXXU2Bi2mXmetROH_b8L_6kvQz0AoXMZpJ25gIHjdBI8CDlbHtpW3lUMtSqfYobABuevAg9dOsU-SgLqgJSM8PHhYsEqTvM72OO_cJ6Lpa-Er8xOofymtJcMA38flc59p4x7juR2Vv27blunqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سید علی خمینی: برخی می‌گویند جنگ را ادامه دهید که جمهوری‌خواهان در انتخابات شکست بخورند
🔹
یعنی ما برای اینکه یک سگ زرد برود و شغال بیاید بجنگیم؟ ترامپ برود که چه کسی بیاید جایش؟ ما هم به دموکرات‌ها می‌گوییم مرگ و هم به جمهوری‌خواهان.
🔹
مگر می‌شود که امام…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/449008" target="_blank">📅 22:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449007">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d16ec0d64f.mp4?token=PFw-a2FZNLMFg4cHKxiblUhCy9GvO4FIO8_uqfvm3lEsZge30wK7xBWCAJpZPQZP9-RW1zQ35Psr9NVILbVGDQs7eupoqUsWa9iGJrmrKpftRCEKipw2lpP9Wp61_EGHLwv7ovrhBT3bb7eMLjSGT9iCdtLnEZV0l5uEnbsFNWAMmYDWxfa171BYpRRMYzDAJ3KhV89xyqm3NO4hV7Bds2-PMvRfd4vIK4mVAGPdfDfznaAZxkPXpxifJTg3edwZDW80vgyFakDv_NUhFPcN1F1aYbkRC9mG64ByJXnyWsooiiGtmy3ELa1XDBkBT6nufa_qpd5EgPBG7vJYwK04oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d16ec0d64f.mp4?token=PFw-a2FZNLMFg4cHKxiblUhCy9GvO4FIO8_uqfvm3lEsZge30wK7xBWCAJpZPQZP9-RW1zQ35Psr9NVILbVGDQs7eupoqUsWa9iGJrmrKpftRCEKipw2lpP9Wp61_EGHLwv7ovrhBT3bb7eMLjSGT9iCdtLnEZV0l5uEnbsFNWAMmYDWxfa171BYpRRMYzDAJ3KhV89xyqm3NO4hV7Bds2-PMvRfd4vIK4mVAGPdfDfznaAZxkPXpxifJTg3edwZDW80vgyFakDv_NUhFPcN1F1aYbkRC9mG64ByJXnyWsooiiGtmy3ELa1XDBkBT6nufa_qpd5EgPBG7vJYwK04oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سید علی خمینی: کسانی‌که از جنگ می‌ترسیدند فهمیدند که جنگ هزینه و مشکل دارد اما ترس ندارد؛ ترس از جنگ بدتر از خود جنگ است.  @Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/449007" target="_blank">📅 21:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449006">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ادعای رویترز: تیم مذاکره‌کننده قطر در تهران حضور دارد
🔹
رویترز به‌نقل از یک منبع آگاه مدعی شد هیئت مذاکره‌کننده قطر در تهران با مقامات ایرانی دیدار کرده است.
🔹
به ادعای این منبع، هدف این سفر کاهش تنش‌ها و فراهم‌کردن زمینه ازسرگیری مذاکرات ایران و آمریکا با…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/449006" target="_blank">📅 21:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449005">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a1cb9a4ea.mp4?token=SbOn3ec4f3V8jYe2shRLJJLAhBketdwAYZ95qsDrH1s3PU--tRqsIFmO5Yn_aBk6GyBQ0OZNzXrM3roamAvUOdNJ0SHPENsXA5tDiQ7JEwz5WFhnLieRummh6U87WUE4LzXxCu4MPd_lFj02ceVc2qESXM9kBAEqcwtJex06Pr4auHdh23czqzkQ5MDED5NBIeHkZGi8UU3ImnoIUJMRZOb9Cf-bOwFejzGNxOEmOAwEdd9k-1_qtjFoyj6EWTjcI71nBk4EffSKzXVWnrjawUC7J9-SVHBOBKpXb36WxyZO7blQQKoC-jxmLvbrxs1tliYPdses4VmnmpQOOFp0Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a1cb9a4ea.mp4?token=SbOn3ec4f3V8jYe2shRLJJLAhBketdwAYZ95qsDrH1s3PU--tRqsIFmO5Yn_aBk6GyBQ0OZNzXrM3roamAvUOdNJ0SHPENsXA5tDiQ7JEwz5WFhnLieRummh6U87WUE4LzXxCu4MPd_lFj02ceVc2qESXM9kBAEqcwtJex06Pr4auHdh23czqzkQ5MDED5NBIeHkZGi8UU3ImnoIUJMRZOb9Cf-bOwFejzGNxOEmOAwEdd9k-1_qtjFoyj6EWTjcI71nBk4EffSKzXVWnrjawUC7J9-SVHBOBKpXb36WxyZO7blQQKoC-jxmLvbrxs1tliYPdses4VmnmpQOOFp0Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سید علی خمینی: گفتنِ احمق به ترامپ، فحش نیست؛ این صفت اوست.  @Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/449005" target="_blank">📅 21:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449004">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0f81f965a.mp4?token=Xqdzpk0WDszHo7gdpyH60ReGNm0aF-ieU4xbzScpzs8EnZLQVmEKRR84yUQHW4GjfROeZH1lCEzqW7mToXrPPmCkh9ZkNTi55I9KL-X5g7tBwOeO5wcj8clxBCnxXGt12-Q2eZgiFYUwjo7NWZ792e25-bgV57qeR3_plr9VTiDvHscMmRXj0g_W7jGRKc7CWB_6RJxsBJWEFC9H8Dd36P_IrgWLKRQTt9DrtO1TRkB9otuBATdq5KqJHlBHRNLc9ivPIn_cmQByteDJ4C49ip6n4WvUUtmKgaH85hVCcnW1lZe3Z5Bma2YqXgSqfmDZraPnAXAVSEjD3hltzvK9Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0f81f965a.mp4?token=Xqdzpk0WDszHo7gdpyH60ReGNm0aF-ieU4xbzScpzs8EnZLQVmEKRR84yUQHW4GjfROeZH1lCEzqW7mToXrPPmCkh9ZkNTi55I9KL-X5g7tBwOeO5wcj8clxBCnxXGt12-Q2eZgiFYUwjo7NWZ792e25-bgV57qeR3_plr9VTiDvHscMmRXj0g_W7jGRKc7CWB_6RJxsBJWEFC9H8Dd36P_IrgWLKRQTt9DrtO1TRkB9otuBATdq5KqJHlBHRNLc9ivPIn_cmQByteDJ4C49ip6n4WvUUtmKgaH85hVCcnW1lZe3Z5Bma2YqXgSqfmDZraPnAXAVSEjD3hltzvK9Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سید علی خمینی: آن مسئولی که بخوابد و در فکر انتقام رهبر شهید نباشد، باید به وجدان خودش شک کند.  @Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/449004" target="_blank">📅 21:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449003">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14cfb7b2f7.mp4?token=upXKhJ1PN99BRvSc-wMjv4og9Mk9ZHFW5gO8gUnYtvY2FvutBjuXa96fJF8l7FPNfF1PrlwdcLTtMtGlkfgK8XQh3VKKYQ3MHBa3fId-LA1smlqkBYzV8t20OCCX4WL4xh7hdkhJUG3lvQyWNzMQvxMwuAL658e1nf6i9YdLSvbbFTi8QYVRqTz7drmz4se7z4DwxJaCTGAk-S8I7Sf1Hx9_Ps-EoEUlX1Mv9XKxdEyVTNzOa_9FL-imzwWghpXeGSXG0HdNW83CVJJy8q1dfI-c_nc-oapWgY2Hrni_fefJ2PNgHDsw_NZGwnymBihFnjS-XxhCm_bOI-vW-z5cmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14cfb7b2f7.mp4?token=upXKhJ1PN99BRvSc-wMjv4og9Mk9ZHFW5gO8gUnYtvY2FvutBjuXa96fJF8l7FPNfF1PrlwdcLTtMtGlkfgK8XQh3VKKYQ3MHBa3fId-LA1smlqkBYzV8t20OCCX4WL4xh7hdkhJUG3lvQyWNzMQvxMwuAL658e1nf6i9YdLSvbbFTi8QYVRqTz7drmz4se7z4DwxJaCTGAk-S8I7Sf1Hx9_Ps-EoEUlX1Mv9XKxdEyVTNzOa_9FL-imzwWghpXeGSXG0HdNW83CVJJy8q1dfI-c_nc-oapWgY2Hrni_fefJ2PNgHDsw_NZGwnymBihFnjS-XxhCm_bOI-vW-z5cmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سید علی خمینی: آن مسئولی که بخوابد و در فکر انتقام رهبر شهید نباشد، باید به وجدان خودش شک کند.
@Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/449003" target="_blank">📅 21:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449002">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0jPB1z0YPMGu7veKKOLJVqVz-jwMG-Kg9IE8HMbxYJBkSxwELxTJgY_-an_ZWuVkN_LqxSYVXU42Qcq3YEGcNH_-Qw4v-XHzDvCFiXYR5msRoEmjoCalDKXQZfMHjHlBxR025SyfOm_0zjDHA0zJfiZLVRjsnaR6E8r3I0CD9Gi00GQowpPh9vWa4s5IMJ3NBF3HBFWpJSXUrLME_goFYCwu9W_F3_cKujtsOuYHLvlR9cf8wyMwII7B-a-_wNEr86RheM6x6bIfEvH6mcetcYmV_9vkeSZ6ZA1LZ2KFQnZaTk0y1IGtk0lJ2zalHxx2J0vaJpWcea-LVJ2JuCWkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آثار فرزندان سیدحسن نصرالله برای رهبر شهید
🔹
گروهی از هنرمندان لبنانی برای شرکت در مراسم تشییع رهبر شهید و خلق آثاری با محوریت ایشان، مدتی را در ایران سپری کردند و آثار متعددی نیز تولید کردند.
🔹
این گروه با عنوان «پسران حسین» ابتدا راهی تهران و سپس مشهد شدند تا در مراسم تشییع و تدفین پیکر مطهر رهبر شهید نیز حضور داشته باشند.
🔹
اکنون علی نجدی، یکی از اعضای این گروه که در مقطع جنگ رمضان با آثار هنری خود درباره ترامپ در فضای هنری ایران شناخته و مطرح شد، تعدادی از آثار تولیدشده خود و دیگر اعضای گروه را برای خبرگزاری فارس ارسال کرده است؛ آثاری از تمارا فحص، احمد الحاج و علی الرز که در ادامه
اینجا
مشاهده می‌کنید.
@Farsnart</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/449002" target="_blank">📅 21:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449001">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">قالیباف: درگیری با آمریکا هرگز با تسلیم ایران تمام نمی‌شود
🔹
از دید من کسانی می‌توانند با آمریکا مذاکره کنند که آماده جنگ باشند.
🔹
در مذاکرات به معاون رئیس‌جمهور آمریکا تفهیم کردم که ما هیچ اعتمادی به شما نداریم
🔹
ما هرگز دست از آمادگی برای دفاع از کشورمان برنداشتیم و هرلحظه آمریکایی‌ها به تفاهم خیانت کنند ما آماده دفاع تمام عیار هستیم و قاطعانه مقابل آن‌ها می ایستیم و حق ملت ایران را می‌گیریم.
🔹
آن‌ها طعم قدرت و آمادگی نظامی ایران را چشیده‌اند و می‌دانند که ما یقه آمریکا را رها نمی کنیم.
🔹
پایان جنگ برای کشورهای دنیا اولویت است اما همه باید بدانند که این درگیری هرگز با تسلیم ایران پایان نخواهد یافت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/449001" target="_blank">📅 21:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448994">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FdYKAhOvlE1sdLa2_X1oIEcmdOIKKNx9p7Ml-uR0goLSgZSDKKJNiuQ__yBRkX3hitm8DZlR6xRDNv4XbxhtMvZoSEn0pqP-AbC5Xsfbo9QgY9nRaWrYdr7LwNMDEbqZicqKNwUVQv2DpmiMBIVFzH0maK6R9LOsuTV5jyilh2G0Ag7a9eBJCNXqb8T-JryX9sg0WWg5W74obEqxfWy0iDa-IhMbLy0u5ubkxKiPKSljilkp0WhhK9IxjSdBL8drcCHMbv3F4tBw2bbrhEUOEoMfgUwYMh9ulywpJLMGStTsHaGgZWANE4u5iZ23O2LYy7_hPuSNzJWxoUFRj3v9Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MtdqYuB88TrCTLZ1mxaYNcFWdOJ3ePj5Skhd9WkdQwbFTUoqg3EnatCjZZuXWjl7Xht4E_1_tE0RuSQcu1ItmbIR0I_pMU9K2LgWsmrc1JX9-rXBvAK4PAP5ZzAq3gtefp6DTRx5dshNK0RJNAOhZXJm1_zjzdgwA1MCVXyIokN0ZLl0ceqB8V6oZmdHbF4RMoqHyt7rLtU7jQ0XGPo3XK0lCc0HnUx-Hm3TpcqhvMJckIvjMvuLAZZQQAP9QSs0HeZ85i4fdHpIlKZnvFg0psLZAU7K8BU9uYYsuiQZDsm8nAGIDNR-s1lMbM2TLFZ_5TMElOSrJkCfevZV7-4w9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c9MbLr6Dh1nKmENokxOk8Nz2_WyjNz43cDxNFl4NZtsjBoca2_zq2SEwdFCedtAjjlMH3GInATGHf1wSDvb9HjUYYZAY46HbTK-jdQNiO7fHDMyHj8yMZ-wuQohETIAKxDAtU_7wRjCFH1aYULP6WnyMJxtVRQuTQjQS-evMG5Xj3b4gyCc5xdq0u4n7MWhKaNYVfLI04wd5DD__AuTj_cznl6leTGHtxAYDi2562YUBR4IrUQPCvRZmbD2BgeKuF62q24UIgMJkUjkNk8OFqECNmt05WuQwmH5diIFaZ1WLXlvy39ZkLUWVmZsJIIolzkLvs0ZMz6GT9kUECgJWIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JR9z7DK2_uQKEB4q0920h5C-3sxD2z58i_WygopF75fpJt_Tc163RVHWS7-tF-BJV9nz78oLI1x9aT3tTUUWxSPyEAc54KhLUBX_2koVGf0klRx_D6p_9Dg3ryIdiiGrUVsptS0JPVNiKkhUH-igff3jIzPw5LJoUDaM7WUtWPTNc6fq36O1fXJyfUUtAAL2Tlzo6IyyiOU2sMzWbQ4e3yxKKrBWhCeuFr29Dcy8B-gVQh-pBl2rbRH2VY8IJaHqKewUEGi1I-hP859rC9RMwYv3-JfKRcPmxqh2oRaOM5FcIWjvFXgFJ2wnMJ11-7YAkfM1jV_QT4Cg5VwjZF7Jkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HCGNQbHqGn-VK6Fy0m58Skpcr5jc8la3h_mgfx_e_kEj8Rem60gYlQfx-UB6HG30wXGPKdukuAhR_kaAapwR83Q_k1Br6gVF_P2cAwUCwxRK5DQpAmvriqBrR0zpecmJxVnBYePFudNN3xjeXOMThaCHpRcC9Hqe-eadE4-n9Z-AnZcg3HahsYPX1RIjqKzTpudEeDw8ZxAx7wJuMkgyv2BioJQP2jZ_yEBAThGKvCvlLieMAEda5pz3y1_OQqTK8xXvPjkSX0eHVI8_aKJ8tZE0UADiZ3IAosmEXoTgLHNqWmNl2rdY-wewt93W8k6Zy5NmzgYTk18av2FYGGgCoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r5QdCHeIF3oUyaTNNr0Ll024cB0FY5yBmV0Rm7gVZzKAyY1N0WxEDwXHhF17zPISyHV-EqyseZJnZ8I_YRrYli0pLIMambLVol4W3KVcAcuPUSdn1SGBmEG0kB_SpvCoKNRtjrZxbMETvqpsLJ3s89bT2Q-pE3ITIpwsm4ABbM2enaNqr3SjRjby2lcXBafuMCXkMD82AceByZQJZyI2dtI-m_A8U_0YMkuTeJJKqlx0FlRmeQk2RCyadtKAM7LBNsXDcWwDRw5xxtec9wZfgy4j4dFvEeckrtF8N6KHAj4M3VQriHmXnyyof7fqlFNwHT-MluSUZWXldSFf9t-ebg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/diLq9PvSASKy7_98i3G9MtGET4JM8rgdodvnx1fKxo04QCcQUZxzaoQIj2IMjPmmWqenhYfiFhl11L4mvD_33g8S40SpFgxQv4IyFq8iWdaLRfcG75S3q3wHbX2h3eISfH6BvRZnOEdbdypSHERECB3hdUzUzEAPoKCCFHRvqYAez_t6rgPZzYw6XdVfeMQoFYK1c_KvqWhIh_LlVQCoCSjA3wuHDVJhKXIZFdf-HKmlZfhAFJn2vMH4Ror78ATyBelumOXbD47IQEjk5Jvj0TmLNaF8VCfQJGCgfYlnxLxiPs5Vyj0I14u8phahxkzl6qqYdWL2uOdbl0VT0rsVrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مزار رهبر شهید میزبان حضور مردم شد
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/448994" target="_blank">📅 20:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448993">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d5222c635.mp4?token=GLRLS2xCgs7mccmmAb9isZ1TYbI9dpg3vec7JlLZg0Yy96TlMtNRl6R0vuzhSbpaR85uJcaE5tK4FapcS29o6e7mEp2PTBp7NMXOS1zJ6bvbzqgtKr_FxxGF5FbR2Kff-9xGSB-L5T5xOvUzABvKTBnMvFdk1jGSvOFjpAoQQAulgBPVyMXHR4gNH4iR4ymY3_CmDoeUJsU_3iRWZ-uBCYCtg6pCSPYPCqxNxH-yrrBSaLftjtkPFyymQsyL6bVK4vfxf2p0qxv-T87WHfnh3zr6gZuIOfEHhL4sHDJ1GjoVphRldEMRYVi0ti7kauqiDqDLCoWuQPizrxOA_h9YvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d5222c635.mp4?token=GLRLS2xCgs7mccmmAb9isZ1TYbI9dpg3vec7JlLZg0Yy96TlMtNRl6R0vuzhSbpaR85uJcaE5tK4FapcS29o6e7mEp2PTBp7NMXOS1zJ6bvbzqgtKr_FxxGF5FbR2Kff-9xGSB-L5T5xOvUzABvKTBnMvFdk1jGSvOFjpAoQQAulgBPVyMXHR4gNH4iR4ymY3_CmDoeUJsU_3iRWZ-uBCYCtg6pCSPYPCqxNxH-yrrBSaLftjtkPFyymQsyL6bVK4vfxf2p0qxv-T87WHfnh3zr6gZuIOfEHhL4sHDJ1GjoVphRldEMRYVi0ti7kauqiDqDLCoWuQPizrxOA_h9YvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرائت زیارت امین‌الله در اولین شب پس از تدفین رهبر شهید انقلاب در حرم مطهر امام رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/448993" target="_blank">📅 20:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448992">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiA63DaSts2dXYnYJiae8Cu4ciDyT0DF8tYhFlFqJQ1VYlF_GonEtLaWKLxHnC511Jrvfstqu1ubhVTYmKSedp7E4g35M0-hRf7fRFgSwVrjCLqu58LQ3i7YQ4y8YusyrZD49Amyjhm1b-9_pxML677UC5Tjc9QqrBtyfJsGxZkrGZ3oA1zgNXFug__m344k1FZZHD6XRYQ0IBYFYPqlBpJooM4c0LzjUPC2jgS7jNSjMSWz66OgWfo9R-1OmCS7Y6zEXgbC28RsdJp2_uAix6_MwDPcH86NSSPy1X4iZqqNu61DKGJk3fl_WQP9bA4M3jEKPmc5rRHbmbAMoyz_Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
بانک شهر برای جذب نیروی «بانکدار» آزمون استخدامی برگزار می‌کند
🔹
بانک شهر به‌منظور تأمین بخشی از نیروی انسانی مورد نیاز خود، از میان متقاضیان واجد شرایط، در رده شغلی «بانکدار» نیرو جذب می‌کند.
🔹
به گزارش روابط عمومی بانک شهر، بر این اساس، فرآیند جذب از طریق برگزاری آزمون کتبی و با همکاری مرکز سنجش دانشگاه آزاد اسلامی انجام خواهد شد و متقاضیان واجد شرایط، اعم از زن و مرد، می‌توانند در این آزمون شرکت کنند.
🔹
داوطلبانی که در آزمون کتبی حد نصاب لازم را کسب کنند، به مصاحبه‌های تخصصی و عمومی دعوت خواهند شد. در صورت موفقیت در مراحل ارزیابی، فرآیند به‌کارگیری آنان مطابق ضوابط، مقررات و آیین‌نامه‌های داخلی بانک شهر انجام می‌شود.
🔹
بر اساس شرایط اعلام‌شده، دارندگان مدرک کارشناسی با حداکثر ۲۸ سال سن و دارندگان مدرک کارشناسی ارشد با حداکثر ۳۰ سال سن (مدت خدمت سربازی آقایان به سقف سنی اضافه می شود) و همچنین داوطلبان صرفا دارای سابقه بانکی با حداکثر ۴۰ سال سن، مجاز به شرکت در این آزمون هستند.
🔹
متقاضیان برای اطلاع از شرایط ثبت‌نام و جزئیات آزمون می‌توانند از روز سه‌شنبه ۹ تیرماه به پایگاه اینترنتی مرکز سنجش دانشگاه آزاد اسلامی به نشانی:
https://azmoon.org
مراجعه کنند. همچنین این آزمون استخدامی در تاریخ 9 مردادماه برگزار خواهد شد.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/448992" target="_blank">📅 20:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448991">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/448991" target="_blank">📅 20:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448990">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ddc860633.mp4?token=XpMXlEd0mQFOgQXYsCrOG8X06vu1RhyD4SjVY4M8UzR5tUciHTvvhf0t69Blz0BraRvwSQ3ddiDsxXXY2CYPTWKTEZAYGDBz6W2w4cRnItllbyUiBjicKyI6g786wfyvu0bo4Qctpyk9MvQNUVH7Nk2VN2FVlpnpi7_8HilM7rC7bxhI0vnNWEoxnR9Qyd4tkJfH82IDt9X53CmBZyvVY-LFKVKskzNmApxX2UyZVUhBHvnYJciYpI4JbFjkwFiQXog9c9fOg8Y1K04nqPnS6b70ercLnyV4vFkV6s-6j5qwmpQcMcXdZMm94He6af3yjtDaK_SYq0TtwDe9KqapSx15bXXwEYYYThrVsDaaDpiGwROrUve4_9yllfvcVb6BfLu8X-bgKSN6cK9E0YzitSvuMcceWKUtomA2yi7GQM56mKI-hBNFMT_Ya6keI6-Y0p0gEdbhidk07kkDGMrbxK2gNK_Vovdv5NN93vIC0AbSy0O2hRpXffqb4g1yHDOfjLnsczedEFKvXx_wDo4R1Dd0cG527gl_Lie0ZXMxBE7x-oAU47tJY2Fy0kl0LifUIh0HrQwLwW70gbfw1S83QG7x_i1NV85CuHDbk0_9qZNABgS9tnN3jniUUolOUk2d2ywQJeuDj4ftPWaHj505Uv07iDSuMGeul1V0RAbzUEE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ddc860633.mp4?token=XpMXlEd0mQFOgQXYsCrOG8X06vu1RhyD4SjVY4M8UzR5tUciHTvvhf0t69Blz0BraRvwSQ3ddiDsxXXY2CYPTWKTEZAYGDBz6W2w4cRnItllbyUiBjicKyI6g786wfyvu0bo4Qctpyk9MvQNUVH7Nk2VN2FVlpnpi7_8HilM7rC7bxhI0vnNWEoxnR9Qyd4tkJfH82IDt9X53CmBZyvVY-LFKVKskzNmApxX2UyZVUhBHvnYJciYpI4JbFjkwFiQXog9c9fOg8Y1K04nqPnS6b70ercLnyV4vFkV6s-6j5qwmpQcMcXdZMm94He6af3yjtDaK_SYq0TtwDe9KqapSx15bXXwEYYYThrVsDaaDpiGwROrUve4_9yllfvcVb6BfLu8X-bgKSN6cK9E0YzitSvuMcceWKUtomA2yi7GQM56mKI-hBNFMT_Ya6keI6-Y0p0gEdbhidk07kkDGMrbxK2gNK_Vovdv5NN93vIC0AbSy0O2hRpXffqb4g1yHDOfjLnsczedEFKvXx_wDo4R1Dd0cG527gl_Lie0ZXMxBE7x-oAU47tJY2Fy0kl0LifUIh0HrQwLwW70gbfw1S83QG7x_i1NV85CuHDbk0_9qZNABgS9tnN3jniUUolOUk2d2ywQJeuDj4ftPWaHj505Uv07iDSuMGeul1V0RAbzUEE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ما را به سخت‌جانی خود این گمان نبود...
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/448990" target="_blank">📅 20:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448989">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/263f294669.mp4?token=LGTGhgNHTIxw-6fXoMv1rMzvIMjipd_wv0JCARbD7t925dNtmPqMiA9S47FaEnegTmQRm1KuRm6DbKBgylcjynJ8J36d7H-kYq3uQoll52QwymJM0y-lMaXB4EVKVwviAniJ4p0oNfvDUI_eHL_E6i0jE-yZtm6mqlPDqGpoBp0W0MyQE_yDp4jrgRK7lvNtR2QRC6XXjPCEKHGqPZDc-3oa8Ktph85zeJmgr7cBbJZ0BC9QtIk7W5sl7J8T7xJLODvfARnWEKp7xVgI_zejKCaibiKsfBLVsy5oAK7qRZgEdUfayl5u42ZPP7ymJ27BZHBN3CYV0o9u2XO9-Yz5-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/263f294669.mp4?token=LGTGhgNHTIxw-6fXoMv1rMzvIMjipd_wv0JCARbD7t925dNtmPqMiA9S47FaEnegTmQRm1KuRm6DbKBgylcjynJ8J36d7H-kYq3uQoll52QwymJM0y-lMaXB4EVKVwviAniJ4p0oNfvDUI_eHL_E6i0jE-yZtm6mqlPDqGpoBp0W0MyQE_yDp4jrgRK7lvNtR2QRC6XXjPCEKHGqPZDc-3oa8Ktph85zeJmgr7cBbJZ0BC9QtIk7W5sl7J8T7xJLODvfARnWEKp7xVgI_zejKCaibiKsfBLVsy5oAK7qRZgEdUfayl5u42ZPP7ymJ27BZHBN3CYV0o9u2XO9-Yz5-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلاوت آیاتی از کلام‌الله مجید در مراسم بزرگداشت رهبر شهید انقلاب در حرم مطهر امام رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/448989" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448988">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e24b27639.mp4?token=FRXgUqCj6YzyA2ZeO4TIb0BLxmgQGHZ8r_6FzKbpEPnlxhFtoSk_RvLR3-W2j9GmGC5paeDFr6JSjvBWKEmxqwIcFLtSqCeKjpB4voLkrDH2uBlIylBTnhdmHr_o3VcuDF5lkrOCj4u9NL_5EDdPYn7to1GsR-2kfEonvVhnj3ZQdm70mA6Lvg4U9pAlCohmWYFnjgjRDFshoM3ane5_4bdL_-yfjNcT-26O1xl4fGqM0iQHs9s_yscWzbT3cWQKU-Ed__PKwepW-IhpO6Wc2-ESlunMXhiBnuHzdcSfrjOmyTNto09NEYqfvkrkjpTW3vPJuVu4lO63pHkb0vvj_4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e24b27639.mp4?token=FRXgUqCj6YzyA2ZeO4TIb0BLxmgQGHZ8r_6FzKbpEPnlxhFtoSk_RvLR3-W2j9GmGC5paeDFr6JSjvBWKEmxqwIcFLtSqCeKjpB4voLkrDH2uBlIylBTnhdmHr_o3VcuDF5lkrOCj4u9NL_5EDdPYn7to1GsR-2kfEonvVhnj3ZQdm70mA6Lvg4U9pAlCohmWYFnjgjRDFshoM3ane5_4bdL_-yfjNcT-26O1xl4fGqM0iQHs9s_yscWzbT3cWQKU-Ed__PKwepW-IhpO6Wc2-ESlunMXhiBnuHzdcSfrjOmyTNto09NEYqfvkrkjpTW3vPJuVu4lO63pHkb0vvj_4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هم‌اکنون؛ اقامه دسته‌جمعی نماز لیلة‌الدفن برای رهبر شهید انقلاب در حرم مطهر رضوی.
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/448988" target="_blank">📅 20:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448986">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">تکذیب ادعای العربیه و فاکس‌نیوز درباره مذاکرات هفته آینده ایران و آمریکا
🔹
درپی انتشار اخباری از سوی العربیه و فاکس‌نیوز درباره برگزاری دور جدید مذاکرات ایران و آمریکا در هفته آینده، پیگیری‌های خبرنگار فارس از یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایرانی بیانگر این است که این ادعاها صحت ندارد.
🔹
این منبع آگاه در گفت‌وگو با خبرنگار فارس، اخبار منتشرشده درباره نهایی شدن مقدمات مذاکرات در اسلام‌آباد و همچنین ادعای ادامه گفت‌وگوهای فنی در هفته آینده را تکذیب کرد و گفت: این اخبار کذب بوده و هیچ مبنای واقعی ندارد.
🔹
وی تأکید کرد: اخبار مربوط به روند مذاکرات، در صورت وجود هرگونه تحول، صرفاً از مسیرهای رسمی جمهوری اسلامی ایران اطلاع‌رسانی خواهد شد و ادعاهای منتشرشده از سوی برخی رسانه‌های خارجی قابل استناد نیست.
🔹
گفتنی است، شبکه العربیه در ماه‌های اخیر نیز چندین بار اخباری درباره روند مذاکرات ایران و آمریکا منتشر کرده بود که پس از تکذیب از سوی منابع ایرانی، نادرستی آنها آشکار شد.
🔹
این ادعاها در حالی از سوی العربیه و فاکس‌نیوز منتشر شده که ترامپ روز گذشته در واکنش به برگزاری مراسم تشییع رهبر شهید، عصبانی شده و با فحاشی از پایان تفاهم سخن گفته بود.
🔹
با این حال، کمتر از یک روز بعد، برخی رسانه‌های وابسته به آمریکا از ادامه مسیر مذاکرات و گفت‌وگوهای فنی خبر دادند؛ تغییری که از نگاه برخی ناظران، نشان‌دهنده تناقض در مواضع اعلامی دولت آمریکا درباره روند تفاهم با ایران است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/448986" target="_blank">📅 19:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448985">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6f20a3c0d.mp4?token=hEQJmJ6zkeJqosky0WmFhgJkaOEAPaL3tuBFfaDMjoeaua4unNs0gJPb4GzzBwu_MnEFMAIN0G70teq5_NCMGMsRPl9cph02PHvDjWnCjbzenKFiHqCFFOT9Hcct2eHZU2t441XqbZlcbddm_p3cELH6hPY_qNXTm6RbUumAHm95urE6pMfmEw8alKlulJqxLiw6SB4SAXD2_3299qJB7l1yRauo5k8grsuz1_t6i2VB1qa5kWb946TyEfyWwxIah5BJcX6lQtAT40zvH9bf1pgy4d2gwMlyo778quy8xXG2Rl2jwKIbF_gcXQpa82CnSLA2Qq6f_Eg3wiOGqFkqNrSET7N1En4bI-ZUbmwrOsdWHOEdngmndt9T3NfZwdf0gpDZ-lC70JobzCEQYeLX7IlKeKYQKdTyouNETV0Gm1vSc_uYbBdCNlf21YuJX2JafCWXVIdwEPT24PDCRf04FbmYGuNtMncoB6Ro3FSYNaFqwDpq0DgpjolvNyRjIiCoiteQ6eRQ9ZRKVJsdSexfAk1p_B4IRkzJyh_7yL7fi2UwuU0384peuWa1MOkbw428bzV478pcfWwEzf3Ttm0jdpLlZEJe2ambDeAROy_yoTgVrReGTGzGg7OyndfuR1DrmzpzkTKGOgqDiZcDkdGaqfW4kYou2cG_ewLOlnJT6aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6f20a3c0d.mp4?token=hEQJmJ6zkeJqosky0WmFhgJkaOEAPaL3tuBFfaDMjoeaua4unNs0gJPb4GzzBwu_MnEFMAIN0G70teq5_NCMGMsRPl9cph02PHvDjWnCjbzenKFiHqCFFOT9Hcct2eHZU2t441XqbZlcbddm_p3cELH6hPY_qNXTm6RbUumAHm95urE6pMfmEw8alKlulJqxLiw6SB4SAXD2_3299qJB7l1yRauo5k8grsuz1_t6i2VB1qa5kWb946TyEfyWwxIah5BJcX6lQtAT40zvH9bf1pgy4d2gwMlyo778quy8xXG2Rl2jwKIbF_gcXQpa82CnSLA2Qq6f_Eg3wiOGqFkqNrSET7N1En4bI-ZUbmwrOsdWHOEdngmndt9T3NfZwdf0gpDZ-lC70JobzCEQYeLX7IlKeKYQKdTyouNETV0Gm1vSc_uYbBdCNlf21YuJX2JafCWXVIdwEPT24PDCRf04FbmYGuNtMncoB6Ro3FSYNaFqwDpq0DgpjolvNyRjIiCoiteQ6eRQ9ZRKVJsdSexfAk1p_B4IRkzJyh_7yL7fi2UwuU0384peuWa1MOkbw428bzV478pcfWwEzf3Ttm0jdpLlZEJe2ambDeAROy_yoTgVrReGTGzGg7OyndfuR1DrmzpzkTKGOgqDiZcDkdGaqfW4kYou2cG_ewLOlnJT6aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عضو ارشد انصارالله یمن در برنامه پرچمدار: آمریکا و اسرائیل تاوان به‌شهادت‌رساندن آیت‌الله خامنه‌ای را خواهند داد.
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/448985" target="_blank">📅 19:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448984">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21ce956558.mp4?token=diyZQyzxIGkaJmmEkkDjRJoCP1hdXUG0-vX73Sp72jhtcRqOHpRgEuU-WOjUWi8_UFcx_Mnoi_f_pnjXuDNfpbHql73GGmR_uf0c0bsbfTtBwCCRTBXHUZ-d7NtRQ-MwNXy-30i1X01kqkcW3Wm_g--afY4eqQyr3fHaSMVnS6wsUZb_TWxCMMCHhlhN_9PqB7qUpKHMm5w_sE0wNfmMnR1HKA1vfzUQz55vZGeXcaXk3elC4vG2cgQGoFQYNJ_bgR5tB39BHr2d8Z1UUNscm7YJglAMILyoRv3-osjr4y1DaCHsm32KsTZVEVU2HgYIJkxEu1aPs6QtRH3NRCHDKFznebM9EHfbxbpORvgXicyoy0NDkW5fnvbESqN6AAkA7BI2kZeS5anLwFNvuCDSr1_kqN7ykeB_1Chyne1E2OB06wiE7WtHuqyyy5-LV2S6PZIQ8WphzyUisk8YGrOGgz9QpJnAvWXeuE-DCmSDXyndsstPANp4CRvnKNIjP_xA8l6ReMR3JXDJpv1il1pDhstlRF6tKNlm1MFCO4lQRb6UdGQtdraV_u59agznJa5SbZvMIqSpEQetxOGxjkhAmAMNyYRSA9s17Btn9Pb3xKcE9gabsfCnvz-LKY7qE0KmHe2IJTiHejxbyXuDP7-RPjTLg6R1aaEwgxLrvoKROEc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21ce956558.mp4?token=diyZQyzxIGkaJmmEkkDjRJoCP1hdXUG0-vX73Sp72jhtcRqOHpRgEuU-WOjUWi8_UFcx_Mnoi_f_pnjXuDNfpbHql73GGmR_uf0c0bsbfTtBwCCRTBXHUZ-d7NtRQ-MwNXy-30i1X01kqkcW3Wm_g--afY4eqQyr3fHaSMVnS6wsUZb_TWxCMMCHhlhN_9PqB7qUpKHMm5w_sE0wNfmMnR1HKA1vfzUQz55vZGeXcaXk3elC4vG2cgQGoFQYNJ_bgR5tB39BHr2d8Z1UUNscm7YJglAMILyoRv3-osjr4y1DaCHsm32KsTZVEVU2HgYIJkxEu1aPs6QtRH3NRCHDKFznebM9EHfbxbpORvgXicyoy0NDkW5fnvbESqN6AAkA7BI2kZeS5anLwFNvuCDSr1_kqN7ykeB_1Chyne1E2OB06wiE7WtHuqyyy5-LV2S6PZIQ8WphzyUisk8YGrOGgz9QpJnAvWXeuE-DCmSDXyndsstPANp4CRvnKNIjP_xA8l6ReMR3JXDJpv1il1pDhstlRF6tKNlm1MFCO4lQRb6UdGQtdraV_u59agznJa5SbZvMIqSpEQetxOGxjkhAmAMNyYRSA9s17Btn9Pb3xKcE9gabsfCnvz-LKY7qE0KmHe2IJTiHejxbyXuDP7-RPjTLg6R1aaEwgxLrvoKROEc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوهٔ خردسال رهبر شهید انقلاب، شهید زهرا محمدی گلپایگانی همراه پدربزرگ خود، حضرت آیت‌الله العظمی شهید سیّدعلی خامنه‌ای در یک مزار به خاک سپرده شده است.
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/448984" target="_blank">📅 19:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448983">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس افغانستان</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4d3fe5d7.mp4?token=jaSCLZb_jwbodsUHIMPvyMl60rUqYBN9BJtVc4YbsGt2AsXCPDpTxJswfFgs1gEVAvWmxHeae5cQ6bHvupTMxA4Lkrs4hZFUivRamGrHCaZdrQ5Dj3oPlvyO7HrrMBmGhUv2dicNvuHC7rHu0yDwnaZ4k3Pq6Y9PD_6NL8CNP7UMzilOsZVeivTKZSUKrZ-bo1GYzbe8syybWVPF6ix736Kj3nvjC9Hw8kO0T7FRkDCjB5-uJsbRmsgCOgReL7We-2eV_onRBF-dt9C8cpDYBetShG77qVha9IpA-8HMD3NTuYrGWae7SS0G8mqSnjIXs63pOM7cSt7fh48GND1GwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4d3fe5d7.mp4?token=jaSCLZb_jwbodsUHIMPvyMl60rUqYBN9BJtVc4YbsGt2AsXCPDpTxJswfFgs1gEVAvWmxHeae5cQ6bHvupTMxA4Lkrs4hZFUivRamGrHCaZdrQ5Dj3oPlvyO7HrrMBmGhUv2dicNvuHC7rHu0yDwnaZ4k3Pq6Y9PD_6NL8CNP7UMzilOsZVeivTKZSUKrZ-bo1GYzbe8syybWVPF6ix736Kj3nvjC9Hw8kO0T7FRkDCjB5-uJsbRmsgCOgReL7We-2eV_onRBF-dt9C8cpDYBetShG77qVha9IpA-8HMD3NTuYrGWae7SS0G8mqSnjIXs63pOM7cSt7fh48GND1GwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▪️
گوشه‌ای از محبت افغانستانی‌ها به آقای شهیدان ایران
@Farsnews_af</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/448983" target="_blank">📅 19:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448982">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEg-33N8dYD1-lOfg40xyU7w2wk_67idXZmZSjcA80iOu7A5pJ5sgiQRR54X-aWpORTuZRL2Ig7x2J0a14E1JJItmSgNPRGTf2tkToaQpmeDAxTqDuEhxCOCNnv5mPHpPMDGK-eOqhIaPF3SUjjkqmc1HgjxWfCh_vV5tCnm13uYTCwOpYKgF46i1pM0IwhXJxnR7EsEcQbhC3BL7YwKDVBD3QDMnqeDid1fSqKuJRaoCu5X43AudEWjnwlte6hYHMEdeqfI121qC7Q8V626gI4p5_83k4jG0RoJrmeOBFG7siy89W7EySSR4vivfPVtH5gf6mlEEiP9pEqdwuBmaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدرالحسینی: تشییع ۴۰ میلیونی، منبع جدید قدرت ایران و جبهه مقاومت است
🔹
کارشناس مسائل بین‌الملل: حضور بیش از ۴۰ میلیون نفر در مراسم تشییع رهبر شهید سرمایه‌ای راهبردی برای جمهوری اسلامی و جبهه مقاومت است.
🔹
این حضور، قدرت بازدارندگی و نفوذ نرم ایران را تقویت کرده و در صورت بهره‌برداری صحیح، می‌تواند معادلات سیاسی و امنیتی منطقه را به نفع ایران تغییر دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/448982" target="_blank">📅 19:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448980">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2afac4232b.mp4?token=lHbV1bs0CVoAot_Evh2p6Li33Av25v1V5UfHjhWAXJOyUEXpcgbBIXtGN-JANcoDYjPCIrsBgxw-7-3Ffo8CdRk7nt5QFYamGSsBQ6HIULF5qKurAG1Qn3MQNYV-21DK-J19RMBclejE_h9VOxeKbMir8pdFiGuCyPtwEepGuZCeIxmXIWN6_S-QByRpDt6U9TPMRSmpda19ys6E8i2224JWBiwfazynhlLDBimXgzXJkv_pWrX0xHJKBK4GDKT56RKQ6isKzfoZOXAzpzdRdG7ZXAKqW7nBGkk5q4st74WXdZYPgChnPMGajEP0-hXVyHFFVdCZouco6nC7P_zSrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2afac4232b.mp4?token=lHbV1bs0CVoAot_Evh2p6Li33Av25v1V5UfHjhWAXJOyUEXpcgbBIXtGN-JANcoDYjPCIrsBgxw-7-3Ffo8CdRk7nt5QFYamGSsBQ6HIULF5qKurAG1Qn3MQNYV-21DK-J19RMBclejE_h9VOxeKbMir8pdFiGuCyPtwEepGuZCeIxmXIWN6_S-QByRpDt6U9TPMRSmpda19ys6E8i2224JWBiwfazynhlLDBimXgzXJkv_pWrX0xHJKBK4GDKT56RKQ6isKzfoZOXAzpzdRdG7ZXAKqW7nBGkk5q4st74WXdZYPgChnPMGajEP0-hXVyHFFVdCZouco6nC7P_zSrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هم‌اکنون؛ تشرف زائران عزادار به رواق دارالذکر برای زیارت مزار مطهر رهبر شهید انقلاب اسلامی  @Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/448980" target="_blank">📅 19:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448979">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12dee16225.mp4?token=GZOn7pE3cOdUfvdWGQEhuvDjPr_FRrrVIp2KqFWp2U9cRlOnDrY17jrTl4Eq9gtB7pvgTeBMgNpoy5FQz1qhNF-4-YcNnOLBcVwy2cGQAAq2-mXqvc8CMWRBu_7yLxq630Q_Cpsygzpfo0WO0IhmfvzNjnk2s8OiYapoEGmz20xj0aVhInw_4vSF4UtBeKExXD4bJ-BDn3SUwkW8GZaeTdZG6ncgbXvSAtePGcn_JV7XYZbOKXHcnTLrc0wvf8bJ5etDRI1gKn81LrAuBOG6a6_VF218uiLQ3FPuYi3_vS6ioZkEwt4qZ-c45qW5xuW9vN5gS9h96LQidyFecwQ1LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12dee16225.mp4?token=GZOn7pE3cOdUfvdWGQEhuvDjPr_FRrrVIp2KqFWp2U9cRlOnDrY17jrTl4Eq9gtB7pvgTeBMgNpoy5FQz1qhNF-4-YcNnOLBcVwy2cGQAAq2-mXqvc8CMWRBu_7yLxq630Q_Cpsygzpfo0WO0IhmfvzNjnk2s8OiYapoEGmz20xj0aVhInw_4vSF4UtBeKExXD4bJ-BDn3SUwkW8GZaeTdZG6ncgbXvSAtePGcn_JV7XYZbOKXHcnTLrc0wvf8bJ5etDRI1gKn81LrAuBOG6a6_VF218uiLQ3FPuYi3_vS6ioZkEwt4qZ-c45qW5xuW9vN5gS9h96LQidyFecwQ1LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ازدحام زائران حرم رضوی و انتظار برای زیارت مزار رهبر شهید  @Farsna - Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/448979" target="_blank">📅 18:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448976">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rOaVS2klrthZkmpiXvGBHNzqpP7IG1DygJiD7un1IWRGt0RErtlQkbtvSdurn9snOX5XIyWSwecPlrWg8QTNzoVwtK21XNS4mQtcrBUSU-ymjooDK49A1wiJTHMNgxRJBR6DCpiPKjc3zsmdL9rLZxRYuYEN_AmoegNgv1LaMBrZeQqfC6xeKgy6me7VNqGgn-HY0x-OWYwuRmqxcWTEOrN5JMFSiO5SxU2g8J0HKM1iIkEsSKCTWO2_HJP4OY7g0fVe8tG5m4lXFUAv9bs33vbVx38sLNfr4ocw6TBzQVpizNIhoSqkypotNZTnwuHow_iCOkcxcM-LpXedXbyp2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KkPhY63ylP83P12H48Yw49u5zlMpxvfiIBHCqW9VqiPyKVcwdXAmxsT5SKKjkf_EgFJYtrHe1W-qO9P9XYykYW6hTKk0xOCEn2F5dCoWzsD5ipL1IfdM-h5Kg8_hnewGaVGoUSBgvrnqSisin6Jr5lxazZI_Fa9FrRgQw2n2B_2Xg3Uh33_Ca-9BS0Lpta77RHOzyW41ID8w-MMVHF5S8YozvaepysHppBjph4SJ0l82gFdyjPKRL2Q3IleKJtBBdY5O7Jb2mWMR8YSti1f47deylYfbefzQ_XasQ27mzs5w7uB7-vpBfe8e-iObBYXrbomtyBctl-F101ImV9L-HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l2IHxpNS5U7xWdmXWG6r4zOzvPsxEVCCefrGGlt1aFJMXIQCOPIEGkqJvr3-8gYkL3QceknL16xlcRibq01Hab_8M5riALsVdUUp8FeXvUB5ic_VNz1dL39Okd1_kPcq3jHmFhOIjdwytbXBT50V_c-sFt2S40BrrvFCUy2A9yetLmoAVtgyHtOG0JOHktNxDCf8gDNSrx7eVt06k437SRtPfrzUsFvw6a1vQ9mMSec0HWtyDHugzvOfD1DqxNusv4pZN1-6WrZ4MfMKHpcO7Ru19F8mr4wqOJlR4xGDTTDQlTchOayGeQCJpZB1zGS2DU0eQ1XsjyjEtLfFIV6b9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
البخیتی، عضو ارشد انصارالله: یمن ملت ایران را تنها نخواهد گذاشت؛ ما دشمن دشمنان شما و دوست دوستان شما خواهیم بود.   @Farsna - Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/448976" target="_blank">📅 18:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448975">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLBoHSpaJDV6uyVrhb9lxZATzYYhp8ym43qmGBRogAyodnIXi5YX7CFflHJWd6lkZWeoeKA0IrToAsUyncNEVt_bgalvEfYUvmw847-08WpNMujp_DlaXOjR3yQgCswO_zySCYCg5PfMityP4C4eNJId_dyW-PDp38VeFJTTZ1-ZZXH4dKrY-oHQ7JRhNZSUHEoH4mH1zNCqYZ8KAHaUtgy9TXg1glpGiXMz76JLzREHETbgi6UaCymPF_rMNP8nWT189PxfS9WODmqPTSmtRWlDvc2vkG56eOCv3T8d466R-F9ZWY9Fp6fMH-beRcRW9mJulAZfQTivKCiDzVtiGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تغییر هواپیمای ترامپ از ترس ایران
🔹
روزنامه نیویورک‌تایمز به‌نقل از منابع آگاه گزارش داد همزمان با تشدید تنش آمریکا با ایران، سرویس مخفی آمریکا به ترامپ توصیه کرده بود هنگام ترک ترکیه، به‌جای استفاده از هواپیمای جدید ریاست‌جمهوری، با هواپیمای قدیمی «ایرفورس…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/448975" target="_blank">📅 18:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448974">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bac2dfc17f.mp4?token=UIj_bQiNcMWfdLf_qN2W7bsJX0mOm6BznEzWBwTj6B7OpYoRrIBDZWe3YCV9y09FI4ljlUcP3Fm8UyPBwSGHCXkX8GcWApbUU-9Vpu9JYtgNipeXuoVgILOeSQRj9JKqPJa4qjzGVbjctChq_5_C0XY_Fr7RJTRV_aBO4kQhcnAmr6vKRZ4rxw9OTBj4DBa1K1dmNaBuQdXI1ncrSA7HsQdz07z7QYnk_obS0CpmxPm4d6ayexoGtNgAQyENjRjXPkqj_pkMKlw9FxXf2k57k3kGEtc81nfZmBnLZo9e5IerU1EgVpBQfwtsHPSQCVmLDnSIB5mNoJdxuFwxlf2ZWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bac2dfc17f.mp4?token=UIj_bQiNcMWfdLf_qN2W7bsJX0mOm6BznEzWBwTj6B7OpYoRrIBDZWe3YCV9y09FI4ljlUcP3Fm8UyPBwSGHCXkX8GcWApbUU-9Vpu9JYtgNipeXuoVgILOeSQRj9JKqPJa4qjzGVbjctChq_5_C0XY_Fr7RJTRV_aBO4kQhcnAmr6vKRZ4rxw9OTBj4DBa1K1dmNaBuQdXI1ncrSA7HsQdz07z7QYnk_obS0CpmxPm4d6ayexoGtNgAQyENjRjXPkqj_pkMKlw9FxXf2k57k3kGEtc81nfZmBnLZo9e5IerU1EgVpBQfwtsHPSQCVmLDnSIB5mNoJdxuFwxlf2ZWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع با آقای شهید ایران از نگاه دوربین فارس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/448974" target="_blank">📅 18:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448973">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/823afc570e.mp4?token=INGHVjOa6avRo-wlzT7HvB_8Xe7RxNbWzHPUphJpXP5acXxjkV5ryGXQLJ9zs6STGZVKGf-2j_UNmznz6wR0Fdmfy9Ahj2yHmHWjXgtj4GilR6enbiMeoQ4nX2aFCfeiuVZIykzTO0Tmg0-pgq0EMlMB7IRqOHDGQXXrNXw3FjICWvVGHMC0d_mw3BoSkZMYprjmIpnywTGpWkz28JRt1IU0hB1gbRzLzNXJ_dSdLYzYwF9cIR6XspScx4UsAnYH6i2zvAeE4ZlOLB2FKsG1zT6JVnzHOkjlliVqKK5C-TUVF0UMuBOc0HXEtzRSOVfjaidIG4HiwEQEaf_WTu9tH4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/823afc570e.mp4?token=INGHVjOa6avRo-wlzT7HvB_8Xe7RxNbWzHPUphJpXP5acXxjkV5ryGXQLJ9zs6STGZVKGf-2j_UNmznz6wR0Fdmfy9Ahj2yHmHWjXgtj4GilR6enbiMeoQ4nX2aFCfeiuVZIykzTO0Tmg0-pgq0EMlMB7IRqOHDGQXXrNXw3FjICWvVGHMC0d_mw3BoSkZMYprjmIpnywTGpWkz28JRt1IU0hB1gbRzLzNXJ_dSdLYzYwF9cIR6XspScx4UsAnYH6i2zvAeE4ZlOLB2FKsG1zT6JVnzHOkjlliVqKK5C-TUVF0UMuBOc0HXEtzRSOVfjaidIG4HiwEQEaf_WTu9tH4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم چشم انتظار زیارت مزار اقای شهید ایران هستند  @Farsna - Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/448973" target="_blank">📅 18:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448972">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbmL7AJ74a3hYpAOiSx7tH-4jrcED6Bxo4H6ymA3zRFVpqc-iDCy4B3PeXf91MR-OT5LAusybBdCjVNSpv7lOpJQFGMDfiLFLh5NwctuHNp2GVkfpfgkINkQXRojJHKl_1gjrxhCmN2rU7HwV2WS0pvn6UEs5EKb-WUnmk_vYPe9zicYTjNzxvhkZ0GIWYAyNzjBpPhuGb7zDeW39Qklog3857YtvJmLtF1QLkNilx8Uc22un0lZUhSy0EYmNmZzcViOkRD5g8HCQwREnLfmPx6qkjQXz_ILt6vQJ0wtBIByuikead_WPKDCpbPOdafcQ3E5Q095c0LqFWp5QmMg8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ بازهم در جهان موازی درخواست ایران برای مذاکره را پذیرفت!
🔹
رئیس‌جمهور آمریکا مدعی شد که ایران از دولت او خواسته مذاکرات ادامه پیدا کند.
🔹
او مدعی شد: «ما با مذاکره با ایران موافقت کردیم اما به صراحت اعلام کردیم که آتش‌بس پایان یافته است».
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/448972" target="_blank">📅 18:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448971">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac1cb4c3a.mp4?token=C7p1fLgHt904SadTKIFctVlXyrHFPHnqZJM6aH66G62rmwHbAiIl1C9IVX55AhSyqodLdA44TYLA_4o5OJreCTkZsJ29xQZPNyEqXkGxqgJT4bm19tiwBXUDowIKy8sYj_wSbwYWvrKJxxmFceT0kJjQj_ZrOnDArVxgyO7fdCyJPrd1RtOvWaV9s3ekkx0VYIyfAXN1k_q3vMGNAkeGAc582u61GAkwHSFmexmp9vSa3wnO5EyOvfLtHYbZInsiRH391_KSftNLDar_KDkGYE3wVOvzYf-ojvDZXIFNM5_kF0j97u-Hk63iD73oMHpMaKi92AaqQreA0aFLzaJS0xw3cman0NNa5Dt2IvN2rUJrpd4nrHSBs9o7mE6h7yAvYze9uB5XYyLqv_wdVHdoseCuo6emShfBcW2xP5oCtiZYeDo5-h0h92zB6hosIlo7U2AeqUfKucTwWWPAZCG0BMeBQBC9kBVQCZswWQfXSF9Lk9eJOuzhpxaqzQYyOU9ENr2VCK_ekj6EedSxWpsrzxIuCHMmHEG2gWVsacH09c3NZt2g-wCsMRwbFw6R6EXXm1z93Go4Yu4OC5PJ9M1ZsIJXDnafOo5OcHfXF83szYwOu3-h93smQDUHK7e6rJhlw0gBpWO_wIlunLgE9AupxJzbYuoTEMFAWW06IlJHzdc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac1cb4c3a.mp4?token=C7p1fLgHt904SadTKIFctVlXyrHFPHnqZJM6aH66G62rmwHbAiIl1C9IVX55AhSyqodLdA44TYLA_4o5OJreCTkZsJ29xQZPNyEqXkGxqgJT4bm19tiwBXUDowIKy8sYj_wSbwYWvrKJxxmFceT0kJjQj_ZrOnDArVxgyO7fdCyJPrd1RtOvWaV9s3ekkx0VYIyfAXN1k_q3vMGNAkeGAc582u61GAkwHSFmexmp9vSa3wnO5EyOvfLtHYbZInsiRH391_KSftNLDar_KDkGYE3wVOvzYf-ojvDZXIFNM5_kF0j97u-Hk63iD73oMHpMaKi92AaqQreA0aFLzaJS0xw3cman0NNa5Dt2IvN2rUJrpd4nrHSBs9o7mE6h7yAvYze9uB5XYyLqv_wdVHdoseCuo6emShfBcW2xP5oCtiZYeDo5-h0h92zB6hosIlo7U2AeqUfKucTwWWPAZCG0BMeBQBC9kBVQCZswWQfXSF9Lk9eJOuzhpxaqzQYyOU9ENr2VCK_ekj6EedSxWpsrzxIuCHMmHEG2gWVsacH09c3NZt2g-wCsMRwbFw6R6EXXm1z93Go4Yu4OC5PJ9M1ZsIJXDnafOo5OcHfXF83szYwOu3-h93smQDUHK7e6rJhlw0gBpWO_wIlunLgE9AupxJzbYuoTEMFAWW06IlJHzdc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سوت‌و‌کوری مسیر جنوبی تنگه هرمز
🔹
پایش ماهواره‌ای کپلر نشان می‌دهد که دیروز پنجشنبه ۲۲ تردد در تنگه هرمز ثبت شده که فقط یکی از مسیر تحت حمایت آمریکا بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/448971" target="_blank">📅 18:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448970">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25fb41b7d9.mp4?token=k0Ap2REGghx3YGW8NBk77eB8Vfn9mpUfP0oED8fEn2BrkN5ahP2TaUoOt48gNgDhbhPMdniSnQul_bHp7kQauxzNE5cp2bmxwt6TXTjuTeGLDqT6V2mLX4rCdP65cAPCASTRPZ2PCodRxCMwfjaqXm3hKBX-ffjkTuIAWVlW_EavEFnxd4W5BE39ycJPTUN8V4Gdoeu_4KjZ4YMV2yEFtj6Mt_dhVdnDEc1L7xVzcNRIpRwLOEOJmy-JOoXzNikyeHK_v7HePISul2pOJEFdZsgaPKOJbliUpfWNiInHMVuDAFgspR_4Q5v0PaDe2QeEESxwN32Jr6SJ9s5mzpaGXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25fb41b7d9.mp4?token=k0Ap2REGghx3YGW8NBk77eB8Vfn9mpUfP0oED8fEn2BrkN5ahP2TaUoOt48gNgDhbhPMdniSnQul_bHp7kQauxzNE5cp2bmxwt6TXTjuTeGLDqT6V2mLX4rCdP65cAPCASTRPZ2PCodRxCMwfjaqXm3hKBX-ffjkTuIAWVlW_EavEFnxd4W5BE39ycJPTUN8V4Gdoeu_4KjZ4YMV2yEFtj6Mt_dhVdnDEc1L7xVzcNRIpRwLOEOJmy-JOoXzNikyeHK_v7HePISul2pOJEFdZsgaPKOJbliUpfWNiInHMVuDAFgspR_4Q5v0PaDe2QeEESxwN32Jr6SJ9s5mzpaGXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران قهرمان مسابقات بین‌المللی ریاضی چین شد
🔹
تیم ملی المپیاد ریاضی ایران در مسابقات بین‌المللی ریاضی چین با کسب ۴ مدال طلا و ۲ مدال نقره، عنوان قهرمانی را از آن خود کرد و بالاتر از لهستان و برزیل ایستاد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/448970" target="_blank">📅 18:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448969">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۸۹.pdf</div>
  <div class="tg-doc-extra">3.8 MB</div>
</div>
<a href="https://t.me/farsna/448969" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۸۷.pdf</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/448969" target="_blank">📅 18:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448968">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c464275300.mp4?token=C4D8x9QH0s55nDMw8C19Xbe6fRR7maCpKUxCeaztIcTDDZ9AhI_SUShO-1Gim8GOvJQ20JEZdp_XMrcE6V0IdeCqQRzEPqTLrg3VENvkpekrxETeJAxZpmTXJe9KQvG7YgCtOSIo5vWnBPvwXALeSwZzTldjnx4vmr69nSUvQRFYM9VHus4yIIaMBhZR7ZQgokoP3EMlO4cbGEMykkSxJK3KdGiOQyp-GmcZXeQn-3y75_Z_lMcdQ0jYy_qnwB1A1fEEn5928MsItuNuj0fJAl4xtBdsCzddDUfuFwJuukf7tQU59Q9TOUSve2QXNpepzgzlAkUQ0mAbiZ-W-a7_HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c464275300.mp4?token=C4D8x9QH0s55nDMw8C19Xbe6fRR7maCpKUxCeaztIcTDDZ9AhI_SUShO-1Gim8GOvJQ20JEZdp_XMrcE6V0IdeCqQRzEPqTLrg3VENvkpekrxETeJAxZpmTXJe9KQvG7YgCtOSIo5vWnBPvwXALeSwZzTldjnx4vmr69nSUvQRFYM9VHus4yIIaMBhZR7ZQgokoP3EMlO4cbGEMykkSxJK3KdGiOQyp-GmcZXeQn-3y75_Z_lMcdQ0jYy_qnwB1A1fEEn5928MsItuNuj0fJAl4xtBdsCzddDUfuFwJuukf7tQU59Q9TOUSve2QXNpepzgzlAkUQ0mAbiZ-W-a7_HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم چشم انتظار زیارت مزار اقای شهید ایران هستند  @Farsna - Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/448968" target="_blank">📅 17:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448967">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRM-7JfIkmbS-_NI5aV6pqyCKzqaRRzS4Gkes4mVDN9kNtl5msqtqOxCsHPV0n_nMTuZNxwLNM0LQ4BXuPC2ukeNXFDNF_4xkzSfzbX2-D2XetTz8fFPdRnMbmejdiUi4BxbrWn55mULIJiva0XOBnAezrfyjFXfrCzszxSOXRW6PotUuMd__fod7nTmigPgU2gcEj6xpjt709PHWJuiqwSBDf-76Eg6RsD1Nnr7OLID2qQlRWMyEG8ljOQ79wY98rBGqQj2aPczuO4jnzdlpdK-WTY3AP2F_zDT_XQDUzc60RKTjXqyZ7TwN4QQZjuCA4xHZLB_Q3eoXAQDd_IkIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خاطره نایب‌رئیس مجلس از توصیه مقام عراقی به آمریکایی‌ها
🔹
نیکزاد: در عراق از نزدیک شاهد بودم که نخست‌وزیر فعلی عراق، نخست‌وزیران سابق، رؤسای فعلی و سابق مجلس، وزرای فعلی و اسبق و مسئولان عالی‌رتبه این کشور در مراسم تشییع رهبر شهید حضور داشتند.
🔹
در آن‌جا یکی از مقامات عراق به من گفت که به آمریکایی‌ها گفته در مذهب شیعه، هرکس در برابر شیعیان با تکبر رفتار کند، شیعیان متکبرتر و مقاوم‌تر می‌شوند و هر کس با تواضع رفتار کند، آنان نیز متواضع‌تر خواهند بود.
🔹
او به آمریکایی‌ها توصیه کرده بود که از غرور و تکبر در برابر ایران دست بردارند و با احترام و تواضع رفتار کنند تا پاسخ متناسب دریافت کنند.
🔹
بیش از ۴۳ میلیون در مراسم تشییع و‌داع با رهبر شهید انقلاب حضور داشتند. آحاد ۹۰ میلیون ایرانی خود را در این مراسم شریک می‌دانستند و اگر شرایط برایشان فراهم بود، در مراسم حضور پیدا می‌کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/448967" target="_blank">📅 17:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448966">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojkeLQWl0NMcQjpPiNXlt1cmLe9yqz3JzJDoza4Ww168rp2brbfluNRORdjAm4uplNqLmKUHg0VBD0Fco4dAh48nocR2Ln61nPLdkoRv-YVvFugBsz6BMJI575cMmU93h7U5jm8OX8foz93J4CG0cBa95z2e1p_PeavSNQMZb1S6w6zb8BCqqeMijIHFGamtNuCF0rfCegjiWu7Qy1YJexa830tnidN9sqOg5GSyjHe2QKR8iZTKxz8Sw9xOh7Ah9dbMevXfMjH2tfsrwCY9fYB6YXVBo2HS_8TX19_rY41U9e6qmjrBqsqn95kToyPwVB5gO-y9NcIeCbd9UQzzdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیلی: تشییع ۴۰ میلیونی رهبر شهید سرمایه اجتماعی جبهه مقاومت را به رخ کشید
🔹
وزیر سابق ارشاد: این حضور کم‌نظیر، پیام‌ها و دستاوردهای راهبردی مهمی در عرصه‌های داخلی، منطقه‌ای و بین‌المللی به همراه داشت.
🔹
مشارکت بی‌سابقه مردم، شکست پروژه چندساله جنگ شناختی دشمن را آشکار ساخت.
🔹
دشمن طی سال‌های گذشته با بهره‌گیری از عملیات رسانه‌ای و روانی تلاش داشت میان ملت و نظام فاصله ایجاد کرده و به‌ویژه نسل جوان را از آرمان‌های انقلاب اسلامی جدا کند، اما حضور بیش از ۴۰ میلیونی مردم نشان داد این پروژه با شکست مواجه شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/448966" target="_blank">📅 17:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448965">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb345674e.mp4?token=R02Gref30biOBxisp1fbvTiAHANzUAevHhIbkCqNr-QmDZzHfxaFLyLStwteo-E1dkm5DV3_mfDsdjumk84cXMcz_hv9vWiU-cPN9goE9--gChGVbHTwiAGMvROAoiipctKRL-wIUN8bZ9UfqtSysd-X9XJF8z1QlF50ZtG6joXsx0fG5WhJYVuDSAZ9f7dBO32Ja-yXruYuhlEP8KG9KLThTCsXnXc9uinPL-SFmkbE3RQEzHc7_8MDh4RBQ7KL1hfPcgPFKl9INrGOpgJzTyZaBy7pTxDaXuUon_bE5szF28h0zNISBQMwsUrMHP35DPXuRt-HM-mB4YMpp12pLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb345674e.mp4?token=R02Gref30biOBxisp1fbvTiAHANzUAevHhIbkCqNr-QmDZzHfxaFLyLStwteo-E1dkm5DV3_mfDsdjumk84cXMcz_hv9vWiU-cPN9goE9--gChGVbHTwiAGMvROAoiipctKRL-wIUN8bZ9UfqtSysd-X9XJF8z1QlF50ZtG6joXsx0fG5WhJYVuDSAZ9f7dBO32Ja-yXruYuhlEP8KG9KLThTCsXnXc9uinPL-SFmkbE3RQEzHc7_8MDh4RBQ7KL1hfPcgPFKl9INrGOpgJzTyZaBy7pTxDaXuUon_bE5szF28h0zNISBQMwsUrMHP35DPXuRt-HM-mB4YMpp12pLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
قاب ماندگار از مزار مطهر رهبر شهید انقلاب  @Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/448965" target="_blank">📅 17:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448964">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbwapkuvzoPMFmeYx6-BPTW-Q42m46JQ4dKHDg_UHb_u7_e22dSLaCqyqa3mLHVV6y0TvALC0GPDzurduj9WymzsR5jxXNR_hiaLAtF4weaRnpo2VpTniS6FE2K3dQQm1zfc4Bq4pw4KJabIDFJTZbbQf_P0WPSvku8E7S2ETRVzH9nWMOF0EAIPfrroN-98eNUfQRBbXhi2mFxh7ch4CezPs2ox1D8j-ZkKQLMu-iqM-VOGrde38J8rXGX009HoJHWDNmb8EkEcQQoRaFPnryM6LPFEZJLezeVes7xzzG01z8NuTQrZn2s569fanputZZAbHFXYhYQVOvs1fPcjJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
مزار مطهر رهبر شهید انقلاب اسلامی و شهدای خانواده ایشان در رواق دارالذکر حرم امام رضا(ع).  @Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/448964" target="_blank">📅 16:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448962">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JI3aYLysvylXti3LPrcSVNhuZtCaCzup_1PsnAWy6mnpoZ8USP-3iNLoaqXEHfDD-a3dhK9tYfhB2vKHXmYfMcH0xYY2VON1XzCIbjVmZImQM0IoYkgHPfXjQZqgn-WCY2KnBPG9GvCD0MvQIgmZe2o5HCfXIl5Pmsea2YtmFNkh3WkDUiz098-4g8Nj1prTj-owXDX2GSljDomNRfoCMFQVBkbmRRFBfUUI97bC2jL-MUzcFX9uUrULuYYWzEOMDmJv2QzDuJSGoHzx_lENi-UrT0xxkr5ryrBpLgbvhZH1oQhlDlHVrevXK0-fHhrhWr7FyS_kGmCyfCZ0s4TyWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه دفتر رهبر شهید انقلاب درباره اعمال مستحبی مربوط به شب اول دفن
🔹
با توجه به اینکه پیکر مطهر رهبر شهید، حضرت آیت‌الله العظمی سید علی خامنه‌ای اعلی‌الله‌مقامه‌الشریف، و شهدای خانواده ایشان سحرگاه جمعه ۱۹ تیرماه دفن شده‌اند، مؤمنین می‌توانند اعمال مستحبی مربوط به شب اول دفن از قبیل صدقه و نماز لیلةالدفن را به امید ثواب پس از اذان مغرب روز جمعه (شب شنبه) هم به‌جا آورند.
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/448962" target="_blank">📅 16:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448961">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUP2EgqNWcaWH1ZvqLd_B4Myi_AVFgvw7J63hcf_f_l5DKDD1_s041aTcEGnINurcims80SYan9jM7F1NzT-Riq_5k5ySWvf_dmyKpqzMJHKuc2dt-Qhn9SSa05kfZ_vMb4wfTp5M8tObayv1vh7q-EPOBSLhqnAJB5fK91yKLOOLAACqdh15nd93u6CsDchH_UKSfk0_O9Vl4Nt3H9_mr61hepDMwdrjj_UJABDDc50gGz54Ji9yrysRGnJnI60WZ5skO5Tswqmq18gUXIEeTPCKWUPtSNc8EIH7WNCMZ-DQOR82vFiyyVPcddOYLneeJLqGm2opkEnwWRDQvyteA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی: تشییع ده‌ها میلیونی رهبر شهید معادلات بین‌المللی را دگرگون کرد
🔹
این حضور، معادلات بین‌المللی را دگرگون کرد و نگاه جهان به ایران را که پس از جنگ ارتقا یافته بود، بیش‌ازپیش تقویت کرد.
🔹
حضور مردم نشان‌دهنده حمایت از انقلاب، ایستادگی در برابر آمریکا و بیعت با رهبر جدید است و پشتوانه‌ای مستحکم برای جمهوری اسلامی به شمار می‌رود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/448961" target="_blank">📅 16:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448960">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFBAPQYgBWYqEyF1jE5WfDqH9nbmUH5aMRrcbfzefPkbkR29Q3sWT3cfra75p8kCfQPtY1g5VMwdFLP5lX1kSo-_krWlcANIT-3uIRVYX4Xc9KZHy1kEnRNdh2CKIia3sq2wRdHXammRLCm0ZOOl8LTdU821RwCdMsLHVXi5AxAVPrxdLTBD44IdKqSLY-thn_mfR4aAmEYORWyg-mflmRdbMCsiJYLBoOJJ5MGRfjXwUWD9M9bcb4IPCWp22f020oJVgA-KzN5jgUuTWOxSW53iCVNV3LX7LBM7bf_JMTqZ2sTZqj-mgWfscQC5ouPpw53xlf2bnqJW5bbXLYqynw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم بزرگداشت رهبر شهید  انقلاب در میادین سطح شهر تهران برگزار می‌شود
🔸
۱۹،۲۰،۲۱ تیرماه از ساعت ۲۱
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/448960" target="_blank">📅 16:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448959">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXX5JCz36jgrFM684kOsxLdjZQTSyplKfoHWrigGb_NB8VBBHVXb1T4pUmOMA9OZsPFfU0fZNwO3VeCngTwV-fn4ioIuY-Fb7P1w53TGAZuWE8NMZt2QNK03JNd7wlpy8dlBNQR73PCG3bENVtPYzv0sm4RTMoG4mIvmVsM14pi_vLqa27gEM1wgqxevkgU-b00XD4ebxPIq9omfRIqqyiyrY7X8GN-s2h4YUZi0UGoZDhcKVtHCB7d0Efb9YZztZf--grMwBMkLj3Wq7lvUSIjN_GebCtCWEAwCoqiiitoCMQE91yqNjlsoK_pIA6vy4BOABpr1s-D1mY_ajnViVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
استوری مهران غفوریان برای آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/448959" target="_blank">📅 16:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448958">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd85be99fe.mp4?token=T6udk8TYqLjqHi62CwG8vUHxU64rB5zM1dY0EGwU48K34grJ7uZO_HgyDg0jhexlcHzRPyCCwGD4QdPEZ4aP41opH-kLkcimKJ3fLQpt6DxhBSnhFbzWkZzPcEI5QVEGR_gBhRCpq4fTmsYuK2f3iCQ4T714WX82n_eFeiyPrpVUVbmKuaJEAhalDAmg4a1874-hpYJynUv6mBki1pq8sTxB-3gkgFan16PhqywIv6RwDmcz3KURvYJ3EM5cRfmuAe6ej9elXYj8VpKZW76yB1DBRJn--zpXeBdtvjRmRR9x32Q3tRkY_R87KTxa8DPoicZMWOH1Sk0v1nd7wVlr4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd85be99fe.mp4?token=T6udk8TYqLjqHi62CwG8vUHxU64rB5zM1dY0EGwU48K34grJ7uZO_HgyDg0jhexlcHzRPyCCwGD4QdPEZ4aP41opH-kLkcimKJ3fLQpt6DxhBSnhFbzWkZzPcEI5QVEGR_gBhRCpq4fTmsYuK2f3iCQ4T714WX82n_eFeiyPrpVUVbmKuaJEAhalDAmg4a1874-hpYJynUv6mBki1pq8sTxB-3gkgFan16PhqywIv6RwDmcz3KURvYJ3EM5cRfmuAe6ej9elXYj8VpKZW76yB1DBRJn--zpXeBdtvjRmRR9x32Q3tRkY_R87KTxa8DPoicZMWOH1Sk0v1nd7wVlr4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری مردم پشت در رواق دارالذکر، محل تدفین رهبر شهید  @Farsna - Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/448958" target="_blank">📅 16:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448957">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNrj-aCoAjblkXnxcWIe28AVOBmg9FmzhjeTdwxfdVUm4o_ahlvmmTyyA057V9DW3eYUIpUJTw0UVEJ41Ye1cg4htGbpLtUi6N1w_7wcY6Km-fQp9BbbQ9tfiAqITIXOXQEPvXc4PTyty9XL7vzd2XTW-yHcZ3Vg5rBSt2GkM0THCrJmSy-OQ-8mpjGek9hX33KF8qgZaB67qzVMleIsweJtvzq211D8RtGEzwuge4HUZuEoCCjxtjoZJRbYMwxZgWfJcA372H5wHk1hPXSQgVQ72EYMO7hUjBcOR0_mpZ0ljQPFK3DnwkRUmeGV8LppslBThLQDFwKjIYpUdCJuVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسینی: تشییع ۱۰ میلیونی در عراق، ترامپ را عصبانی کرد
🔹
معاون پارلمانی دولت شهید رئیسی: عراق سال‌ها تحت اشغال و نفوذ آمریکا بوده است. حضور گسترده مردم در نجف و کربلا، ترامپ را عصبانی کرد و نشان داد نفوذ معنوی رهبر شهید انقلاب فراتر از مرزهای ایران است.
🔹
این مراسم، محاسبات دشمنان را تغییر داد و واکنش مقام‌های آمریکایی نشان‌دهنده تأثیر گسترده این حماسه بر افکار عمومی جهان بود.
🔹
حضور میلیون‌ها نفر در ایران و حدود ۱۰ میلیون نفر در نجف و کربلا، روایت رسانه‌های غربی درباره فاصله مردم با جمهوری اسلامی را با شکست مواجه کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/448957" target="_blank">📅 16:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448956">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ادعای رویترز: تیم مذاکره‌کننده قطر در تهران حضور دارد
🔹
رویترز به‌نقل از یک منبع آگاه مدعی شد هیئت مذاکره‌کننده قطر در تهران با مقامات ایرانی دیدار کرده است.
🔹
به ادعای این منبع، هدف این سفر کاهش تنش‌ها و فراهم‌کردن زمینه ازسرگیری مذاکرات ایران و آمریکا با هماهنگی واشنگتن است.
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/448956" target="_blank">📅 16:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448955">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWagyu4yjkYJuhymSare2j-hTMv7wrHNg1tc8E-_E8_rJ4cCBU2Jyvs6PjrBcCY34K7gj9Tdp7GCtFK9VnGCqY-fGsZb_23SnXBa78-lCUlDUVtsytFnoinqgECSKHaI2g2Yd-91FC0QD6QAMau9KDDJ8KZ6VhFaX1KF3HUT-xjW_7AlqiJnxGDCwcss0ZUQwXZo3sUvNLLEZpj2pOdIunByet6T6mK0_RhB4uocmr5fkSd4BgCGm_AB9J9Qh4DGgPYbj9fsUOpD0m42qDLf5rG-NvgQCAHUgUprdtWJjPDc6A389KYSj8m8sT0FEIacflPEPx5tBCJrTPwliX9woQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ترامپ: من هدف شماره یک ایران هستم.  @Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/448955" target="_blank">📅 16:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448954">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3dcf56223.mp4?token=NqSfQXjURZtp1jRoiq8NwtsWGNb_xC46Ucn-cetA-wlv82xJavia_u4yEaRzemiDy82YUn5lY_U1air11vLLithFklmCzFM1jRfRwQoy5zh7Wb2_1noLiLFmJU9k8Q2j_Q52gcmxb2h_xOefIYFIJqXIUeg6sA7B_Dvz5E4c4EFOPU0jcEMBuuQg_ZkIkBIUSJd9DnMxAJ3SABuqZIMvQvo9-fg2s8-aDohP7ybvenHFsumUyluOyxcrp9f1MsGCIS1PeAHjAWemLPdaCDwnhOnnTkY4MRwjmkHX1LpMsTmrlcZDDem2h7rWSe_HwuDDdFh7Zn9faRQE8lHFuKiojw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3dcf56223.mp4?token=NqSfQXjURZtp1jRoiq8NwtsWGNb_xC46Ucn-cetA-wlv82xJavia_u4yEaRzemiDy82YUn5lY_U1air11vLLithFklmCzFM1jRfRwQoy5zh7Wb2_1noLiLFmJU9k8Q2j_Q52gcmxb2h_xOefIYFIJqXIUeg6sA7B_Dvz5E4c4EFOPU0jcEMBuuQg_ZkIkBIUSJd9DnMxAJ3SABuqZIMvQvo9-fg2s8-aDohP7ybvenHFsumUyluOyxcrp9f1MsGCIS1PeAHjAWemLPdaCDwnhOnnTkY4MRwjmkHX1LpMsTmrlcZDDem2h7rWSe_HwuDDdFh7Zn9faRQE8lHFuKiojw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زارعان، کارشناس مسائل بین‌الملل: باید کاری کنیم که بازدارندگی به‌وجود بیاد و امام‌کُشی در ایران رایج نشود.
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/448954" target="_blank">📅 16:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448953">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/247c2a33c9.mp4?token=hq-ti7cKXSP2Sy3d9GgDcCsKav2RDv5Y0xCYRQDFTfM34m6OtPaSjIYLPTcwSlS_xBk3wrf30y8QhV4N6L6_kSGMYWQBUCCUa2KXe69_CAWqEUc6dBY5Rz1d8_TLeKG-BO_CXbqQ89Cb84CnHZ_DYgRhkDSjlrpghVE1glUGUqC1AWOB_-WL5AfreW231IONQBdfHhcDKyWjsHNHKMAuq3V5Etxmq5SmeRIEDQ_ps7qQeC7eE_-BHGX0lNG_D4SECrAIZaPBCkorozniD-mmugkW4ke06wX5_maHOa4p7VcDIF6EqM-zVuJ2vkZeamo3CAFvx8NDOXYYO5fKCarvmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/247c2a33c9.mp4?token=hq-ti7cKXSP2Sy3d9GgDcCsKav2RDv5Y0xCYRQDFTfM34m6OtPaSjIYLPTcwSlS_xBk3wrf30y8QhV4N6L6_kSGMYWQBUCCUa2KXe69_CAWqEUc6dBY5Rz1d8_TLeKG-BO_CXbqQ89Cb84CnHZ_DYgRhkDSjlrpghVE1glUGUqC1AWOB_-WL5AfreW231IONQBdfHhcDKyWjsHNHKMAuq3V5Etxmq5SmeRIEDQ_ps7qQeC7eE_-BHGX0lNG_D4SECrAIZaPBCkorozniD-mmugkW4ke06wX5_maHOa4p7VcDIF6EqM-zVuJ2vkZeamo3CAFvx8NDOXYYO5fKCarvmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمادهٔ روزهای داغ باشید
🔹
هواشناسی: از جمعه ۱۹ تیر تا پنجشنبه ۲۵ تیر ۱۴۰۵، با استقرار الگوی تابستانه، افزایش دما و تداوم هوای گرم در بخش‌های گسترده‌ای از کشور پیش‌بینی می‌شود.    کدام استان‌ها تحت تاثیرند؟
🔸
سمنان، تهران، قم، مرکزی، یزد، البرز، قزوین، لرستان،…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/448953" target="_blank">📅 15:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448950">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X0yNOkZTywr7bNOdUoAw_OvBEXaR8rv0qf-xkFHChShaHs1nfyD3cH-rpG_ZDGrzz9e4tXTG_KiQh5EmhOPyZ1qH8tBqWVD4gxyED_nnoAAM4xEWfCzsPTQKj7_BfQ0tuS_h24ScVt3fPZanY1ElzMoL21PdwyPqgqzH01FAm0NlUN44S55trtlOR8vt-rzrgNU-j35KbFe_IaVEbDlR11v-IhldgFXORaXDzfg0zvXTh-w35zDML-LYY2RCEXW7J-MnVTLjOJ1CHpQf0x233B4ZdXTwL16PgUj-HoM_L4_V08Eu-l57FPYigJCRvBot-BzTSstcX-yfO6P8QLEF3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R_wYwuNCWU3r9rWWDVaJZFMdVIWwpwNq2nsgWLsMOpMpUiwBhvjd_8drUMKtLKGbSNNkhXQhJWqydeXjW-F3McV2Vs619VV6C8tG7ixUa1XXn4tMC40N94HvLXq1DZtnQA19Qye_YMnM6Peo8xcQ9QWtvBhAUGTBE0X9SWQZZsArK73bV6mVoUQeigYHK55DS74t0j84JOzt4YtrXIPbNVHu3oeY2x1Zyk-VJEjzvwQKAFwh9uCuJhOYCpTSrbtK3wuFW-36B1jAFjwwuc3Cp298n6Mn9jYd_D1b7F7hJxMNFuiZNdJWs5Sc653D88JT3ZNmtCGG0yTQabixyK-ecA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72d7495a5d.mp4?token=i5_3-KKd8j70koynd5nD42n4aVx-j6WLiukRW7z_fXZXbvx7tYCTXX5lC1vASWnXakpY3tlnBkhLAbo6P-D9gSsZRgBmOeEbA7aupitFqod7do2TKeY_cfXT4Q3auqcpYBNI-Rsw6I8gayoZZ-w0wS5RCmGUjjdHh_Jkz6Qy1eRuP4wtA4wOMwQ24_e11kn5Xuxp842Wy2wRVpx3C0_vemma02PD-M6xv1YCVeMrGcw3zwoMaXOLEtz1ibAKaYR1oa7qL2lPxrnApzavCIR930cdAqhNbd5JZCbMibVCDWWslwrmXV2OjYssiiaCk8lg3NaMw7kDEiuiV5ZL1KkKeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72d7495a5d.mp4?token=i5_3-KKd8j70koynd5nD42n4aVx-j6WLiukRW7z_fXZXbvx7tYCTXX5lC1vASWnXakpY3tlnBkhLAbo6P-D9gSsZRgBmOeEbA7aupitFqod7do2TKeY_cfXT4Q3auqcpYBNI-Rsw6I8gayoZZ-w0wS5RCmGUjjdHh_Jkz6Qy1eRuP4wtA4wOMwQ24_e11kn5Xuxp842Wy2wRVpx3C0_vemma02PD-M6xv1YCVeMrGcw3zwoMaXOLEtz1ibAKaYR1oa7qL2lPxrnApzavCIR930cdAqhNbd5JZCbMibVCDWWslwrmXV2OjYssiiaCk8lg3NaMw7kDEiuiV5ZL1KkKeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حمله پهپادی رژیم صهیونیستی به یک خودرو در جنوب لبنان
🔹
شبکه الجزیره از حمله پهپادی ارتش اسرائیل به یک خودرو در نزدیکی شهرک کفررمان در منطقه نبطیه در جنوب لبنان خبر داد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/448950" target="_blank">📅 15:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448949">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c5a0f0c0d.mp4?token=DcPtlzqtLwoWRmi0XLraOk8HCgzVMR3epCke6AGocpXopm4DO3rMZz4XMkvqB1TD51eNEUhwv2YxUYdiStYQyQYCihnKCxt0pGnMoAM4HFzouPd_6Xmw114-kwcPAWQ3sXMxsA6sCEiIXLzWS4qpbrzoeAmqw-vTkJhljBuCAAho88GRzpTQ-OMjdhjO0ZQADQo632_Od_9wj5vOBnPiAduYjnNjWC2nMUYoTGS_ykuyWKbmzLkxElGvuWDmWTj5OFVQFMcuPjEm_prpGxRS9QeR_Rjl6BF_FPHANKcZyhwrnhB1Xp9Z0zLMyQOO6WPUEdJwlAfLz6pCFDoPYsMRMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c5a0f0c0d.mp4?token=DcPtlzqtLwoWRmi0XLraOk8HCgzVMR3epCke6AGocpXopm4DO3rMZz4XMkvqB1TD51eNEUhwv2YxUYdiStYQyQYCihnKCxt0pGnMoAM4HFzouPd_6Xmw114-kwcPAWQ3sXMxsA6sCEiIXLzWS4qpbrzoeAmqw-vTkJhljBuCAAho88GRzpTQ-OMjdhjO0ZQADQo632_Od_9wj5vOBnPiAduYjnNjWC2nMUYoTGS_ykuyWKbmzLkxElGvuWDmWTj5OFVQFMcuPjEm_prpGxRS9QeR_Rjl6BF_FPHANKcZyhwrnhB1Xp9Z0zLMyQOO6WPUEdJwlAfLz6pCFDoPYsMRMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آستان قدس: تا ساعاتی دیگر مردم می‌توانند به محل دفن پیکر رهبر شهید انقلاب بروند.  @Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/448949" target="_blank">📅 15:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448948">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‌ مراسم ترحیم امام مجاهد شهید از سوی رهبر معظم انقلاب اسلامی حضرت ‌آیت‌الله سید مجتبی خامنه‌ای جمعه ۱۹ تیر پس از نماز مغرب و عشاء در شبستان امام خمینی(ره) حرم حضرت معصومه(س) برگزار خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/448948" target="_blank">📅 15:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448947">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32bf9b3888.mp4?token=aW30tdy5TdMrocFqanRR29Wkc8l5uRRuFgsz0UmeoiUtq8JS3TMwdFMbkY5hPYCyWTCT-YLvVn9nWk36RZHkOIIlLUXr-XasuR7g4IHcGPWKGTbM05aJ_8fvwbn4sPxXTcmzQ65O7UiAFBQM3Sw1nD7Vsi-be1bSn_elEGAWJttjc3fG6p0JYTCkgnovbaMaRV_kO5dKi7MnVeAKHC5CUHqJS_L92SwBTwyhRFZeM_WSxfNcMqz0F-9BMHjQcbEBUGXU8YU47bZuc2LODYC95E1X4D_-QJXuftTZDegg98AgQhV8hlNFFAIAAcxG5bRPdUhL3Bmo2j49ec3CKN2Ssw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32bf9b3888.mp4?token=aW30tdy5TdMrocFqanRR29Wkc8l5uRRuFgsz0UmeoiUtq8JS3TMwdFMbkY5hPYCyWTCT-YLvVn9nWk36RZHkOIIlLUXr-XasuR7g4IHcGPWKGTbM05aJ_8fvwbn4sPxXTcmzQ65O7UiAFBQM3Sw1nD7Vsi-be1bSn_elEGAWJttjc3fG6p0JYTCkgnovbaMaRV_kO5dKi7MnVeAKHC5CUHqJS_L92SwBTwyhRFZeM_WSxfNcMqz0F-9BMHjQcbEBUGXU8YU47bZuc2LODYC95E1X4D_-QJXuftTZDegg98AgQhV8hlNFFAIAAcxG5bRPdUhL3Bmo2j49ec3CKN2Ssw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل راه‌آهن: تمام اراضی واقع در مسیر خط‌آهن رشت-آستارا خریداری شد
🔹
درحال حاضر بخش اعظم این اراضی در اختیار شرکت متولی احداث راه‌آهن قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/448947" target="_blank">📅 15:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448946">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe53a547a.mp4?token=Sd-01QG0Psf65ViCeIyij01oz5acNIL1giOyd8tcBd_EhR5WnRip9hTIbgyh9DDzvw2A8xCIxxt6TUKSVarKsFzBN_C2Z_AT06e3vvAWPv-zlySwVt1xaRSNctzNGc5ADTpvbz69NUvd-vrmutjT45Kg5JwOJbuCNls5VbrSQULkzNa1OJWt4-6MUR2_gM81tMGr1k6SdAEerr19BPX1rV0XA8vQe2gbxG1FbJAedz43Flr9tReK_puBPFGZCmhUnHjTw76d1NxoJjY1Y6eaD3DPGnTkSrnK4JG3OBo5qyk79vr-2BU7OiwIbmY4Bhtcoi6vHK_5XUTM76sluXe_Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe53a547a.mp4?token=Sd-01QG0Psf65ViCeIyij01oz5acNIL1giOyd8tcBd_EhR5WnRip9hTIbgyh9DDzvw2A8xCIxxt6TUKSVarKsFzBN_C2Z_AT06e3vvAWPv-zlySwVt1xaRSNctzNGc5ADTpvbz69NUvd-vrmutjT45Kg5JwOJbuCNls5VbrSQULkzNa1OJWt4-6MUR2_gM81tMGr1k6SdAEerr19BPX1rV0XA8vQe2gbxG1FbJAedz43Flr9tReK_puBPFGZCmhUnHjTw76d1NxoJjY1Y6eaD3DPGnTkSrnK4JG3OBo5qyk79vr-2BU7OiwIbmY4Bhtcoi6vHK_5XUTM76sluXe_Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آستان قدس: تا ساعاتی دیگر مردم می‌توانند به محل دفن پیکر رهبر شهید انقلاب بروند.
@Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/448946" target="_blank">📅 15:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448945">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNL0GyZcpFao4SlY2IJyqIv-qMk5dEDzAlGAIXSMVyjfD4s_g6xNFSl_Z7f7SV4NkxcsEETbPtOAVvMoTmJIRXKtxCjDe03_tNUDmfZTOS0aOcpzwH6V99noRhfZwyXT27rfpUPWfdTbTxK2gyEZEZcmapIEhec2BjBohD7Wm4pdyHhSk-StQ3_i4qveBSa3HoRcbHf8wTDfb90WIIWY8qYro8w2OS0lQ5dIGMeNu-vs8w1hZdQmXSTYrueeiN13AuVA4KEY_hmJHozwitXMO8KVFheV038yluVk7XhVU5v73D7LIbzQt0nZ4ql63J-rDRLgNddGVH87PMUfdrha-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دبیر شورای‌عالی امنیت ملی: با حمله به زیرساخت‌ها مقابله‌به‌مثل خواهد شد و رژیم تبهکار صهیونی هم از پاسخ رزمندگان در امان نخواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/448945" target="_blank">📅 14:53 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448944">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f38d90462.mp4?token=uL7cxqjdd2Z4V6URIxoPdHt3WQW18c9drjCYJ2qoG9oonwu3ZG0UN5SeZYBa7BssvG5XsPWWtEIvB5sOAhfABhuBfodcqSrrppHY2aSb3jIUshT7qRHyBetMAcE7YM-S7fSObZzbWu-xmK_2vLEkXK-qygOLJNiUu1nTm6xCLnvGsllVO6IKPq5pomXtOeq8A80KAENen5ISNy-g83jegJxThHCyR6CXywKqnoGG7NwygvMhGMcBafbHue8GjvTmzbbVEA2OGAL0q6NyKRQsO5SskN-3NqetV2DdoLIDkvxB5soPMndxzHDURQ-1GqSsjDETSyPqEJkFIX-8BRIIkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f38d90462.mp4?token=uL7cxqjdd2Z4V6URIxoPdHt3WQW18c9drjCYJ2qoG9oonwu3ZG0UN5SeZYBa7BssvG5XsPWWtEIvB5sOAhfABhuBfodcqSrrppHY2aSb3jIUshT7qRHyBetMAcE7YM-S7fSObZzbWu-xmK_2vLEkXK-qygOLJNiUu1nTm6xCLnvGsllVO6IKPq5pomXtOeq8A80KAENen5ISNy-g83jegJxThHCyR6CXywKqnoGG7NwygvMhGMcBafbHue8GjvTmzbbVEA2OGAL0q6NyKRQsO5SskN-3NqetV2DdoLIDkvxB5soPMndxzHDURQ-1GqSsjDETSyPqEJkFIX-8BRIIkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخورد ۲ پرتابه دشمن به اسکلهٔ صیادی بنود عسلویه
🔹
فرماندار عسلویه: ۲ پرتابهٔ دشمن به اسکلهٔ صیادی روستای بنود در ساعت ۹:۱۰ صبح اصابت کرد.
🔹
درپی این حادثه، ۱۰ قایق صیادی مردمی دچار آتش‌سوزی شد که با حضور به‌موقع نیروهای آتش‌نشانی شهرداری چاه‌مبارک، آتش مهار…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/448944" target="_blank">📅 14:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448943">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f02b60bfa8.mp4?token=IlHvCQ2U943-2-FOTTtWSKSwBa9AIrANHgdsD3R1ejhPNyjyjdEmMtrtmt0Cb-O1_WvTbEor-oXup-JGgixSg7WDwDEyzFUdLEiuzOun23R-EEaBzwosmwFg50NI6xhVuOBP8uJ_ATDOFp3RCqocD4UOqmeH-Ravan5NNTDjhyuqrEb6aUCSoxeGr4QfzupO6ogIxZddEzaxW1NUZ125z0YAdOdFjxO2MsGTVWK1zZaChSpcCUCmdY4D0PfSrXLeHFzOSXlAsYVfnD69o4217kB800mgjHaPegkCzPs7fvYKGaxT5ZwvbU0R42twDDTHgja1zHnvseLW4KvArdcnXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f02b60bfa8.mp4?token=IlHvCQ2U943-2-FOTTtWSKSwBa9AIrANHgdsD3R1ejhPNyjyjdEmMtrtmt0Cb-O1_WvTbEor-oXup-JGgixSg7WDwDEyzFUdLEiuzOun23R-EEaBzwosmwFg50NI6xhVuOBP8uJ_ATDOFp3RCqocD4UOqmeH-Ravan5NNTDjhyuqrEb6aUCSoxeGr4QfzupO6ogIxZddEzaxW1NUZ125z0YAdOdFjxO2MsGTVWK1zZaChSpcCUCmdY4D0PfSrXLeHFzOSXlAsYVfnD69o4217kB800mgjHaPegkCzPs7fvYKGaxT5ZwvbU0R42twDDTHgja1zHnvseLW4KvArdcnXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع نمادین پیکر رهبر شهید در پاکستان، تایلند، بحرین و نیجریه
@Farsna</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/448943" target="_blank">📅 14:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448942">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9Q3dds1lKCWyzjRGhi70Xs4uC6ie1iK3tN-Cb4kL9ralt7oBBWpQpysfq1svx9I84VShht_ZwavNOYqmLwju81cNjQFWRjKV-rInBFYeSJh0cUhCBkdrljfxm3NR2vh_AJVsSD1mlG_O9R2HdB8bFoXer4w5GmwFYJR_kPuaHyOfx4qeTDKcv1xoMP25oS9wgQhAA5C_TyVJJ1NCg8OiC-66ZS1h9ULSFcsSHC_-O_dZUrrK7QSgaOfsvGevI1kLYgzdcDuOeohHFLfWIMyvtpGI3zaggecvEQCO1s4AOSjwa4uAZDJ9x_dT35IRgaA9p8ezdW55EvG-cRUI5wF3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاغی جدید فوتبال ایران؛ جلالی پرسپولیسی شد
🔹
با اعلام باشگاه پرسپولیس ابوالفضل جلالی، مدافع چپ پای تیم ملی و چند فصل اخیر استقلال، با عقد قراردادی به مدت ۲ سال به این تیم پیوست.
@Farsna</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/448942" target="_blank">📅 14:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448940">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmPsqrtVvTzYi0RKdjA2SnYUtsxZz-Emk5PlF2cimEv5GIAZuJ2ThAYFvNcnJ4Kafw7EonNkkrg56Bi88vjAIeZ2aqkRXlFU2We87CbbFGqGoIzMuueKpGeinrmSQsE7w98BOLLKVvo-iaEOwZ_ovQV77OcURXaYD-47HJLCtLUr3JbrPHAC3NKfY6t-mZmxArjN0zyWpjc_uO51nvgxQnetpXqFPacrIyAfxiywsr35mxX4TFsSO0TuiUbWqWWcIpZs4GcD5AvUxGYMmsyRjxCMwL-u2ZO53fX2cF5xXdZ45VjrUzgEQSnme16Voe7QKZQ9QeC-VbSMlCY4L6y43g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیه اس-۴۰۰های روسیه را به کشورهای خلیج فارس فروخت!
🔹
یک روزنامه نزدیک به دولت ترکیه گزارش داده که آنکارا سامانه‌های پدافند هوایی اس-۴۰۰ خریداری‌شده از روسیه را به یکی از کشورهای حاشیه خلیج فارس واگذار کرده تا راه را برای دریافت جنگنده‌های اف-۳۵ از آمریکا…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/448940" target="_blank">📅 14:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448939">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8b35dd7c4.mp4?token=kwMXUaUIN_ISmKLy_Ll_K_9UwUQ79lyz3P_Xk8mzzFy7SvviLlklrIgBbpCRXWmiPb8R3zog8FGp_nYo2YoUrgmeaNFC0DSXeBbRpDVnmpwMMAcn-tEzd7zIB8pMNULHWiJXLcaKEmvtlAMnGZcYtzlmcOLf1zVU6tpPH-BXDRKE58TCJ-vdAsnoMUFxWxvy3I3sIfoEV9qO4zl5aQ8d05mlsT0PFATBnghXtDeolxbifJN0jiPUu2W-WNcGJR0Yjn1Cw32Kv5u0RNwcOboJkLeV1nCiK3etjTsVPWTpQj2PukOn4c47lfQU6u1rq7meCGP8tQFvix3gGsHxxlr2sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8b35dd7c4.mp4?token=kwMXUaUIN_ISmKLy_Ll_K_9UwUQ79lyz3P_Xk8mzzFy7SvviLlklrIgBbpCRXWmiPb8R3zog8FGp_nYo2YoUrgmeaNFC0DSXeBbRpDVnmpwMMAcn-tEzd7zIB8pMNULHWiJXLcaKEmvtlAMnGZcYtzlmcOLf1zVU6tpPH-BXDRKE58TCJ-vdAsnoMUFxWxvy3I3sIfoEV9qO4zl5aQ8d05mlsT0PFATBnghXtDeolxbifJN0jiPUu2W-WNcGJR0Yjn1Cw32Kv5u0RNwcOboJkLeV1nCiK3etjTsVPWTpQj2PukOn4c47lfQU6u1rq7meCGP8tQFvix3gGsHxxlr2sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حالا ما شما را نمی‌بینیم و دوستتان داریم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/448939" target="_blank">📅 14:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448938">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjqh9EBuLFt8-qtQEbUE0sWSIHTgbS9AZ34T3Jp9EyFhaBdcdpF19Xa6lBWEr0YK9F8iT8IHYtECSNDopdKqvnhvI-09272MpRqK3GJjrAA6uaSkoEHfZm1vCo2ZU0aCcRxeIlcY0zhQdBk6PK1nuXNAljJIvf8bM4RyMIY_7J4qIk23ue7bYiEMko95wsq84cNZIxlV6WI9dhUGPWm4PusVxJKM6CgBHbQ0RcY8dAY93dR6yQmu9kVKyfrA9Tw95O6_LF86RYCNHEU455NnJw0IszusHSCahoXg2UQhiKlvyi-Kaikomg5b5dSUfziI9rfig0BLzhIwlWKxDV95iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
وزیر خارجه، رئیس مجلس و شماری از علمای اندونزی برای ادای احترام به رهبر شهید انقلاب وارد مشهد شدند.
@Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/448938" target="_blank">📅 13:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448937">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57cc189e49.mp4?token=opA2LIWRhYiNgbqPpZrz7tiOmzUR3hlXurWVvQ57q1VzVd2iGahjMDoVtF8ZmPtj9hzsPLbnFBV3EAyFvbxDNGYuu9hLxCpt7TdQoo_pF7nIvK7KFNSaVrYIVoH4CWqS9cmlwWSx4oEhvw0aayQ3t1L0v0kX4MYRgDiJra1PVRj3iY6N8Go7rAa6g0xli_kymCfawuSViulicjRYxdUCWwLzps6l8ZhVt41PwxIa_wgdyb-dJPAUdJetTawsUJIk2rhukUdtuOEbt5IBB7lNRX-RQ568A_2FY_mZ4OxfIEdxIOA7ty38izoyEXSEryltyavWYGlQAupfLzL0NFbAYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57cc189e49.mp4?token=opA2LIWRhYiNgbqPpZrz7tiOmzUR3hlXurWVvQ57q1VzVd2iGahjMDoVtF8ZmPtj9hzsPLbnFBV3EAyFvbxDNGYuu9hLxCpt7TdQoo_pF7nIvK7KFNSaVrYIVoH4CWqS9cmlwWSx4oEhvw0aayQ3t1L0v0kX4MYRgDiJra1PVRj3iY6N8Go7rAa6g0xli_kymCfawuSViulicjRYxdUCWwLzps6l8ZhVt41PwxIa_wgdyb-dJPAUdJetTawsUJIk2rhukUdtuOEbt5IBB7lNRX-RQ568A_2FY_mZ4OxfIEdxIOA7ty38izoyEXSEryltyavWYGlQAupfLzL0NFbAYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع نمادین رهبر شهید در کارگیل هند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/448937" target="_blank">📅 13:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448936">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c410869c1.mp4?token=d8s_SWd_aTTzEDT4loXd66D2zitGO0R3URHU2jVyRycU9sihA4F_4ElGNjlcQ-qymptCopEXtXbVVvaTk7VdRHdX8MYh-nLPtCye4y3qj2v2mdG6viZHbk0O8W5jbHzDrc3I42xCU3YQUswz0Hp3ykN5IRCRnfCdjgFv4694O4TnplQfwa4UgwYd59dUqnHYAumdwnAeLo5VKMnlmDk316O9GYloLwVPBZOlvnFC5RWaDyu_1ammXhTSrN8AMpDzAGp5WLsTwc6vN6dgi2_4ZhNgR2a6zx1pO5WdumTZCNWKibHDtGmCeZbmaNRszCckTfjItvwkLt5OqvjWJSeYHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c410869c1.mp4?token=d8s_SWd_aTTzEDT4loXd66D2zitGO0R3URHU2jVyRycU9sihA4F_4ElGNjlcQ-qymptCopEXtXbVVvaTk7VdRHdX8MYh-nLPtCye4y3qj2v2mdG6viZHbk0O8W5jbHzDrc3I42xCU3YQUswz0Hp3ykN5IRCRnfCdjgFv4694O4TnplQfwa4UgwYd59dUqnHYAumdwnAeLo5VKMnlmDk316O9GYloLwVPBZOlvnFC5RWaDyu_1ammXhTSrN8AMpDzAGp5WLsTwc6vN6dgi2_4ZhNgR2a6zx1pO5WdumTZCNWKibHDtGmCeZbmaNRszCckTfjItvwkLt5OqvjWJSeYHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جلیلی: انتقام از دشمنان، حق ملت و وظیفه مسئولان است
🔹
ما در مقطعی حساس هستیم که آنچه فرجام این رویارویی را رقم می‌زند، میزان تاب‌آوری جبهه حق در این جنگ است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/448936" target="_blank">📅 13:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448935">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/209e6e3e83.mp4?token=YpurOzgbOccEAjWQGlokyMgocraYmShYJ1ELfooc7yuadY__p_MAUCb1MmfDA6X-p04gHDSv6FA7HsJ4hboyytbnTiTEh4T1TBCbJQCe-dfvGTYaz2vKzKdqC1Ps5QCVbIQoGSiPnwy7cx0GkcttiuHRqJOEP48RJecC3I6foFADCflkckPE8N4wXElJ8kUvJ0JL94dgY7cconJxeBSk2bLRPDcNr5BZ2Frz-v1-QjG398za4FiSExf1R7ind-tsjL8jv_bOceNFj3OlCHhXIW1IID45XE-MLcDkyZs6z5jRTW1yHUfAJS_Ltp34WLLEk_WtV9C0j-hwyV5Sw4EBbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/209e6e3e83.mp4?token=YpurOzgbOccEAjWQGlokyMgocraYmShYJ1ELfooc7yuadY__p_MAUCb1MmfDA6X-p04gHDSv6FA7HsJ4hboyytbnTiTEh4T1TBCbJQCe-dfvGTYaz2vKzKdqC1Ps5QCVbIQoGSiPnwy7cx0GkcttiuHRqJOEP48RJecC3I6foFADCflkckPE8N4wXElJ8kUvJ0JL94dgY7cconJxeBSk2bLRPDcNr5BZ2Frz-v1-QjG398za4FiSExf1R7ind-tsjL8jv_bOceNFj3OlCHhXIW1IID45XE-MLcDkyZs6z5jRTW1yHUfAJS_Ltp34WLLEk_WtV9C0j-hwyV5Sw4EBbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای این دقایق روضه منوره و حرم مطهر امام رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/448935" target="_blank">📅 13:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448934">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlocdPjLXZqld18CvTavrRWCCUNrOGB8RWtjLFshyQEhfuHZPlqiNfn9Ptdyb1r5vH8OSPHyKDddcimOwaxOvsrLbHXlTfv33AIFcMvstYTZS492E3t43Wrio85i5tFE924322J8R1BgJ8TYF1hdT4LIEqF5CcDZ-Dscea-jafk-NNA-v9RdrX2P-hbkP3E-jY6I7oikGkV4afSz8N8NAfO6O9B_Un5W2AnVHmdxpZRV5OgYdtxgZqHQ74VBlWhl29FDNdFMvaR3OJxcb4xGzZpQYKhpt3P_QgxOlHwMf_Ioo2yDvkaxUpO-wfhOPPlTbdNjZyT2uXsi0IPs2_r1Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوترابی‌فرد: تشییع رهبر شهید نماد «صبر جمعی» ملت ایران و عراق بود
🔹
امام جمعه موقت تهران: اجتماع و همبستگی مردم، قدرت‌آفرین است و اقتداری که امروز جهان اسلام از آن برخوردار است، با گذشته متفاوت است. این اقتدار، دستاورد صبر و ایستادگی جمعی ملت‌هاست.
🔹
دشمنان اسلام، به‌ویژه آمریکا، سال‌هاست با زیاده‌خواهی و سیاست‌های استعماری، ملت‌های منطقه را تحت فشار قرار داده‌اند. اگر ملت‌ها می‌خواهند از یوغ استعمار رهایی یابند، باید استقامت آنان بیش از دشمن باشد.
🔹
حضور گسترده مردم در تشییع رهبر شهید نمادی از صبر جمعی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/448934" target="_blank">📅 13:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448933">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f74d80bb.mp4?token=RzsPn552KnKBCsXEYZV_Jpgblqk_7mpkZvtnOpXellNZeFWuLnUs6jxqQ5CLwxhdMGFbIU7yxg6Ic1LPARJWI17Rt7f67C6dOmr0be3SjzeQaL8EWx8KTQxsQYSdWGy1N7e19CKC_J0svgGKjD23KexAMNWv4-OeOARnO90NUT4D6KN16_F7d8zjh7RJ6mVKtWp8FaQynpbHts8_mFt3k3aEwX35sOUXFmvqzCrqaC1YXcptnc2L506dUQtfBRhy18aSTtLC-ylZdtYX2wK2b6I61mR7ZVhDbJSbmMtUaX42o_ZKacLZUWHBz8Xost7Ly1dTJgs4A3ftAGXP6MQA6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f74d80bb.mp4?token=RzsPn552KnKBCsXEYZV_Jpgblqk_7mpkZvtnOpXellNZeFWuLnUs6jxqQ5CLwxhdMGFbIU7yxg6Ic1LPARJWI17Rt7f67C6dOmr0be3SjzeQaL8EWx8KTQxsQYSdWGy1N7e19CKC_J0svgGKjD23KexAMNWv4-OeOARnO90NUT4D6KN16_F7d8zjh7RJ6mVKtWp8FaQynpbHts8_mFt3k3aEwX35sOUXFmvqzCrqaC1YXcptnc2L506dUQtfBRhy18aSTtLC-ylZdtYX2wK2b6I61mR7ZVhDbJSbmMtUaX42o_ZKacLZUWHBz8Xost7Ly1dTJgs4A3ftAGXP6MQA6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت مردم از ماندگارترین سخنان رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/448933" target="_blank">📅 13:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448932">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaaa-sbE3-aajWx_MeKeclhQIGkpyXzxziJ5eKx8_bZjnTGfxkEF8UeAY7qK_hNue9sKBoDOw-yd4vzZC2b0kkUjOXujnCtJEvCQCbl4qpx1c5ajFOFLZKPW9t6RSbLg6TSQea6AreKMCIbBvkL4ur2XAvMAyMmMdwdE-8R6lyJdflq8C2MCx76pPH9UqnIq1g5fqru_tY7al5hQytAGfCyBch8Nxk7AmYdLtF9GyrSvodvb3SsfV3aJpyHbTkiVj8FSPrbdZWQdVwWBGAQGog7Hw2OHNLdHq28XPkM8_bOt8eIcxoUNR95QhS9mZYTYdFs60QQdIrtTOr0PVJIt2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز‌های فرودگاه مشهد از سر گرفته شد
🔹
بعد از محدودیت پرواز روز گذشته در فرودگاه مشهد همزمان با تشییع پیکر رهبر شهید، درحال حاضر پرواز‌ها به‌حالت عادی برگشته و درحال انجام است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/448932" target="_blank">📅 12:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448929">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mj9ZPe7qvxJqKOnorfSLHawyKu9d2M84syOwUKLuAXkZ4NmoJXbYXrq_zfkXuoNlJBeshKzuaLSz_WfUYQcfaLU6TIE8arb1lPlPV7wpRSeVWZTXhx8Fjfc2e4fRKirBFwSBsgZtHuTE5_w3cZ4eJrtsmJ_7iRFKayZ6PISWBRqE2XWR59VOeUdPIuRyuBFfH2kvkUe_8y5rEE6nJ_8fB5n434IQ7EKwUTRizKtWdj-eFLY1l3O43_3VEZ66AKvDpEqR4W58g4pYpy3q-mraL1_OP2TsqLRdC-wwxr2yW3NcJ8arr-E9SKx2usXuSAUUmx54mdYLdqxrS8Mcf8kykw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pafNMtrS5vVa59Qo-2HU_gOE-bYI3sGP-OpYlGHFWfJrCrC1X6YVM7B-_KDhX4TIfkT3M_4hIycRVvQdA4kr-ThGKW3ldNEZCUgVYV1JH5zccTt0vi5ClTEvkyRgXFGmpplvd51vEim_Loel2aAdobvADgzpQDT5uEqfPXmIx0dUTHdtPvNRg8c4WUoM6rkf6MPPecekVHKLhdvXLhMBJa4h8hAKIwQPMVMtnoEro_buPhDrCsLO7QObHq1LX5bD-h1E7lM24pTjyw6oJ8-0Nsn7LH-lr3nKFXjEcPVr2UOpPm_yCT1cyoRgL9zso9iQL7MVgPW3eMyYrds27EM5IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F3-njY6d3YzbVymKrt3EB19TLWwqUZoeYTm6YcXu4I_qUbv3B932jKKR-92B51GVlm2usyFBdzQ5JnZXfB4QZGTSncyUHHTE_XhVbZOlzPqnO-m1Lx0YH9laWknO0kAUEpdTiq7hyivUSWewCgPpyH1hUWaB9IeHMV8u8dAumbBKvqnaTdMCUmnUrkmRGZBpIa3VEy_C65JKNcGYd_rKlWxqUoI66fYawzinzKdWE95FgvJrXeqSxguSm2avkbTBefjdVqmY4aALbRyHQ2W86FylqQZyoD9CrvaXQ2AP1_ASobcLy5znp3Eg3_FJ3tQCiSic0DoLo0Tw1ZNe4UlIIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
کودکی که به زیارت زهرای ۱۴ ماهه رفت
@Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/448929" target="_blank">📅 12:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448928">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4926d659c.mp4?token=lNuJqSZ72mgUs62qZ3Cr08yrz5qzlbJT6SZiR00JVhofhWjz8EdrU3SSnRUXaoQI_MQVJe34INLSGN1iEsxjaYE76M_AQsYX6Li114kkY0j31rXO53M8JUEaYnsChW9FIlDTt60HFZafypbKx8z-K5Euj15lPD4z_KlwSYVkXccePv6kIqBHZF29zKKZEK1kdvS98LgDtvPZnrt00RCHxzt6HupKOdgwWi3V2XbvJU0WnLdvEBkcNABLEfmJAQXYsHHRXzVMajAqtr6vD_EfZq9MV1CCAZHtCccxVls5PA9DdYXZBm-5w2-JDFhMyxhi9rB5_3yuHutwfE0_4gFsPjtpmoVEMxjOJqyvxv7ikE85l48Gg8Eng6zA7NR-nM2NGeyZKvDTPWCSNnOPz9YvuZx5W3wF4E63LGZOuebheAh1zxJwMHQEYRGaukKl2VhwRqBeaG8EBG8J4k_68sXUstlho3ckMI2enOOhaISpkIAna2RMICcwXS036o-HLtB8hpgudOP7Q5CA4lVwB56Axfzp85QU6b-Aji6cfFiRx1l41XfUVUuKA7H4HUkEnWEMAydaN9pLDaiJ77oKfE4hqSIF22Agy_DkNAMTJIb9CIV7e7bYtWasG348FORHYtQCf7pbO2KpRlgv8xlQ5lqQ6tQAFAop3BzEhh6r7rLG7WU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4926d659c.mp4?token=lNuJqSZ72mgUs62qZ3Cr08yrz5qzlbJT6SZiR00JVhofhWjz8EdrU3SSnRUXaoQI_MQVJe34INLSGN1iEsxjaYE76M_AQsYX6Li114kkY0j31rXO53M8JUEaYnsChW9FIlDTt60HFZafypbKx8z-K5Euj15lPD4z_KlwSYVkXccePv6kIqBHZF29zKKZEK1kdvS98LgDtvPZnrt00RCHxzt6HupKOdgwWi3V2XbvJU0WnLdvEBkcNABLEfmJAQXYsHHRXzVMajAqtr6vD_EfZq9MV1CCAZHtCccxVls5PA9DdYXZBm-5w2-JDFhMyxhi9rB5_3yuHutwfE0_4gFsPjtpmoVEMxjOJqyvxv7ikE85l48Gg8Eng6zA7NR-nM2NGeyZKvDTPWCSNnOPz9YvuZx5W3wF4E63LGZOuebheAh1zxJwMHQEYRGaukKl2VhwRqBeaG8EBG8J4k_68sXUstlho3ckMI2enOOhaISpkIAna2RMICcwXS036o-HLtB8hpgudOP7Q5CA4lVwB56Axfzp85QU6b-Aji6cfFiRx1l41XfUVUuKA7H4HUkEnWEMAydaN9pLDaiJ77oKfE4hqSIF22Agy_DkNAMTJIb9CIV7e7bYtWasG348FORHYtQCf7pbO2KpRlgv8xlQ5lqQ6tQAFAop3BzEhh6r7rLG7WU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت آیت‌الله علم الهدی از ویژگی منحصربه‌فردی که رهبر انقلاب دارند
@Farsna</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/448928" target="_blank">📅 12:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448927">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f2fa10f04.mp4?token=Xa6IHbq9NmKMKDx8CcQICYCTLPBOSN8VtHFvVRcjwMz5Dn2dtGlxSvstr0NOuLYZrugFv-YykeiU6x7llK_kK9meiRbkhTc3j-Y7mipnpEZXs6yUpvN7JUVW3QiMZQXykHbIhgEJ6xI-SgfpeT0VaRMzxZ1fk-ZtxCYgKD3jlpY9Ld8zUYuVJJeF06JdT_QAOl2eBoyhVYnV5fOb0hXJWzx30H2GBfeSyT2rShmlP5IS1TUJGJYHz-zyj81UxUQbOugAziYpFMayh2txL0874WqGgrSp0JKYFrtI25DA3Ne4uUiTWAi4jHvJg472cMaBcKL6fH9iFZnqumJLAtGJjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f2fa10f04.mp4?token=Xa6IHbq9NmKMKDx8CcQICYCTLPBOSN8VtHFvVRcjwMz5Dn2dtGlxSvstr0NOuLYZrugFv-YykeiU6x7llK_kK9meiRbkhTc3j-Y7mipnpEZXs6yUpvN7JUVW3QiMZQXykHbIhgEJ6xI-SgfpeT0VaRMzxZ1fk-ZtxCYgKD3jlpY9Ld8zUYuVJJeF06JdT_QAOl2eBoyhVYnV5fOb0hXJWzx30H2GBfeSyT2rShmlP5IS1TUJGJYHz-zyj81UxUQbOugAziYpFMayh2txL0874WqGgrSp0JKYFrtI25DA3Ne4uUiTWAi4jHvJg472cMaBcKL6fH9iFZnqumJLAtGJjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
البخیتی، عضو ارشد انصارالله: یمن ملت ایران را تنها نخواهد گذاشت؛ ما دشمن دشمنان شما و دوست دوستان شما خواهیم بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/448927" target="_blank">📅 11:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448926">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uI5iqxzFZjbxVs5XksxPrnoxnoBSDf5BIgPTCb6HKvCpZqoaH8dOoZ9vF0wivjPOnQxFWd6BiYZ2k700oT3UhnYqGOacYGdbOi73HA8HYIbcQaAmnMfe5nlM3I-WWnq0Q8cb-BKzI5fB_PWyHRam5J3bA9sLUJHd-L_Efdu7-z8PxPbf3sYkkyjLSyxsBMquVMpIHefALx4o70mEyLmLWxMbb-hSThyo7xPjMyovQSsWY054WIwA5Z3i2J5Eabd88OgkEOuCfXjA-YRSST_oRKLd3gGva_nxcUDVmSm0HWou3IBQg2Xz2GinnbPyL_c1Y6qhEmB7_pHxlDCdj0jGMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیه اس-۴۰۰های روسیه را به کشورهای خلیج فارس فروخت!
🔹
یک روزنامه نزدیک به دولت ترکیه گزارش داده که آنکارا سامانه‌های پدافند هوایی اس-۴۰۰ خریداری‌شده از روسیه را به یکی از کشورهای حاشیه خلیج فارس واگذار کرده تا راه را برای دریافت جنگنده‌های اف-۳۵ از آمریکا هموار کند.
🔹
عبدالقادر سلوی، نویسنده روزنامه حریت ترکیه، افزود که امارات متحده عربی و قطر از جمله گزینه‌های مطرح به‌عنوان خریدار این سامانه‌ها هستند، اما تأکید کرد که باید منتظر اعلام رسمی ماند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farsna/448926" target="_blank">📅 11:25 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
