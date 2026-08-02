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
<img src="https://cdn4.telesco.pe/file/SO-jp_AnMUkUBJiEIUtyrPBL3SICCV6L8EjpuJG5g9JpdV0paAhdXoek4AS8c8VUIZsY-lli-xqShMGmJK8o6JAbRi5IVn_rKW-vYeHLJe9qETyDVqEBI6ppUq2mO3KE1v2_R2CKn85b3xH6t-LsTHrP9bxpe4LlrN3GTExkZGE7iqOzk_eNbxEgeNmY5OLsldXOd3VjVG_sklmCLEeVtQp3hs6MFAIiPv_sssfavcUVZ-0D868d5Yek5wQAsimK5JzlB0WoK-O4ihd2NuQ93Zz1R7Xa9SymPcPu9x1QRAF5Dc5WdCzFDYRfmq7_X0vnhlrZWUZQDZGRy_HmqmcXGA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.08M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 08:18:32</div>
<hr>

<div class="tg-post" id="msg-677587">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
رفیقدوست: امام من را صدا کرد و گفت بمب اتم نسازید / تنگه هرمز آبراه بین‌المللی نیست / جنگنده هم ساخته‌ایم و در حال تکثیرش هستیم  محسن رفیقدوست:
🔹
وزارت اطلاعات حدود ۱۰۰ گروه نفوذی را شناسایی و دستگیر کرده است.
🔹
هر نقطه‌ای که از آن به ایران حمله شود، هدف مشروع…</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/akhbarefori/677587" target="_blank">📅 08:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677586">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ffbb3d665.mp4?token=jOx6EoSN__6z8LP5QOoPwCsF35YdEHGCHtmo8SdS-P6fRXW3kuBezLHmR5N8lf8X_jmTNePJi8wwh22OzZTdSP2rCE8Z8fG5k80fZKHSqK_sLXcDU6KbofMYv931aBtNLQ_Wzn2u0pNU6ddMgCDteY6UcFHjYed8WZNpvmeC4eG8U_9RF8qOmuG9g1g7bR2HQVpIKCIrZhiQppdZHyudyRZYAhv_psDFIA5qlCpdCuytcTwkkd-DWSEA1VzJXyYOtECXN35KQ66vCUeIACeMIxQi_ark0WXqfWtMHyejmdduR0jfc43lskCtpHJobYGsoYkMHZ8GgzXEwTSDdz26UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ffbb3d665.mp4?token=jOx6EoSN__6z8LP5QOoPwCsF35YdEHGCHtmo8SdS-P6fRXW3kuBezLHmR5N8lf8X_jmTNePJi8wwh22OzZTdSP2rCE8Z8fG5k80fZKHSqK_sLXcDU6KbofMYv931aBtNLQ_Wzn2u0pNU6ddMgCDteY6UcFHjYed8WZNpvmeC4eG8U_9RF8qOmuG9g1g7bR2HQVpIKCIrZhiQppdZHyudyRZYAhv_psDFIA5qlCpdCuytcTwkkd-DWSEA1VzJXyYOtECXN35KQ66vCUeIACeMIxQi_ark0WXqfWtMHyejmdduR0jfc43lskCtpHJobYGsoYkMHZ8GgzXEwTSDdz26UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳ کشته و ۲ زخمی در تیراندازی در ایالت آیداهوی آمریکا
🔹
مقامات محلی در ایالت آیداهوی آمریکا از کشته شدن ۳ نفر و زخمی شدن دست‌کم دو تن دیگر در پی تیراندازی در شهر «توئین فالز» در این ایالت خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/akhbarefori/677586" target="_blank">📅 08:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677585">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f0205d5.mp4?token=eUVu2AqVJW78VuWiVSRMalOVLMsEIEQXm6snbE3gJ9x3GmBnZHfnROaSwdLiosflsDHySYAm2wSjozDSsg84M1P18UckyTeQAR_-VNAjHhvukTgNhabpxzTG7fumlwSUyx1jRG7R0f4gSlpByUnTIKxzqB0TO6abpz5pCeZyFZHrRjjlMjEZSEzqtcqkmeBuZb2DNj8HMjE2tSiD7Ecyi5v-6-n598WYDe2N95YuIDuuIZb8yKopchQafGjkKOL4iIgVoGgXuSpvTRmiCTgZog0FyBCIW-mkltpJMfOvjE46Be9Zl-TE5pFP7lTWsLGDeyE6CaXLiMf2oAUUnxlQCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f0205d5.mp4?token=eUVu2AqVJW78VuWiVSRMalOVLMsEIEQXm6snbE3gJ9x3GmBnZHfnROaSwdLiosflsDHySYAm2wSjozDSsg84M1P18UckyTeQAR_-VNAjHhvukTgNhabpxzTG7fumlwSUyx1jRG7R0f4gSlpByUnTIKxzqB0TO6abpz5pCeZyFZHrRjjlMjEZSEzqtcqkmeBuZb2DNj8HMjE2tSiD7Ecyi5v-6-n598WYDe2N95YuIDuuIZb8yKopchQafGjkKOL4iIgVoGgXuSpvTRmiCTgZog0FyBCIW-mkltpJMfOvjE46Be9Zl-TE5pFP7lTWsLGDeyE6CaXLiMf2oAUUnxlQCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تخلیه اجباری شهروندان به دليل اتش سوزی گسترده در ايالت واشنگتن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/akhbarefori/677585" target="_blank">📅 08:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677584">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a987ea5b89.mp4?token=v9ptQJ4BoxpnoSJ8RA1fB7f5Oq2cAUWkD0KyTRh9r3lkg76AMP5J_8itmmC_YNfA4g0i1eBSty0KQLK0CAOVrwzg25srPDmsvBZsn2nucfFKB-0_9RmeSs4p1J5R4DaO4UTa-4W9QajYAXjA4s4F_XunN0neCH24ca-DCvrWUbiK4aEkSsBUYRjgTbYKB_uS3g75m9aMFSKo5U0zjLbsD2dkLe6DvQb5PD_IJ6QGO1ejk8_vMhFdIne3c_TltJqEudjgxcZ2Sf9FOdQ9w3ml6hZ4lvjlQv4uesvNxm3GrGUgHFePRodA7hV6WF4xjCrGBPkoSKs0-QVdm2WhhHnveA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a987ea5b89.mp4?token=v9ptQJ4BoxpnoSJ8RA1fB7f5Oq2cAUWkD0KyTRh9r3lkg76AMP5J_8itmmC_YNfA4g0i1eBSty0KQLK0CAOVrwzg25srPDmsvBZsn2nucfFKB-0_9RmeSs4p1J5R4DaO4UTa-4W9QajYAXjA4s4F_XunN0neCH24ca-DCvrWUbiK4aEkSsBUYRjgTbYKB_uS3g75m9aMFSKo5U0zjLbsD2dkLe6DvQb5PD_IJ6QGO1ejk8_vMhFdIne3c_TltJqEudjgxcZ2Sf9FOdQ9w3ml6hZ4lvjlQv4uesvNxm3GrGUgHFePRodA7hV6WF4xjCrGBPkoSKs0-QVdm2WhhHnveA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فقط با یه صندلی و چند دقیقه وقت، بالاتنه‌ات رو قوی‌تر و خوش‌فرم‌تر کن
💪
#ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/akhbarefori/677584" target="_blank">📅 08:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677574">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E0xrgMdPCFfXuwCUUmjCgvEwk-ufVDDybDuSPFoYGysHCKJYm3nN0G5VctndL-V70tyY7oB5j9qUOictUSUhsWp96IP7B-HVW3b2EsQwL5t2RpaDUB6yr2GULIlmLzX9x8tb9hCwv8kO56enD3krcxxGqjnUgNcaDvwssRRDQEBKJqgQqK5oKFV9Z_8NJMt8r76O8TjNWFxUGmma4Klia6rird1gTIhPFxf9OiGaO10cNjwYcW6Tj8aMANR8yrUZGyTpGgvHGbJUfObTyZNBKoI3iE32Tv0NQoJfMcfioUL0S1MYGkulg1bQLvhswJJAD3AlrzR00_809PuG84xMSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z8hlhdIUHOdDxIR-bsATfHAzlaVtKdp7k0ZjLJ1zm4xnQ5kXgDT1D9ymfUzyFpO-aRiwj-Z21xhxUCtUCO7G55diviAMMP8Z7Od4v-I7vH_ILJu3dPy-5qOyD80ZiADsCZPmiVONl1DBKrROEbKaRxQmEiy2KMkGdIAg0FRHc3MaPCHwKy3Ef0JPwebr05IagsxS4Nik7mvrBap92ryE-EI4LceWB_NadvEl3k0NEIyX9PJk99fgDlf_TkAfXxIo7Vf9pokt_umisB7zIrmSJe2wU4GMWcOlHNH-c_-iUdxskb_nK3AiLkY-Iu_rkR6IGTgmALNUgWh6pUZbcxEa5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gIQI88XNBf0mt5Rm269pIrALENXg2TaTqj4Bq3Z9qZ4NdyKcP4KMYUnENgDxnVF7m8SJh_vJsHKBMCLgJW6vyA3UNR7rxlUMNlQJaJrdkVlK76iHf10-lhO_WI3RHCBm0_Rpo5fudy3Dz_pnxYySztx4GjbnVDXLWskKOSczzrM9uVM17CjssaxtOEp18c5DZ_VFf8IJcaP20w1vUiWNd1K7BqiAC_28VAqs7NaZBmIqk7cvWF2usQAfQO107HNCW4V1-z6VT5cwkzl2gkbTi6xEXxpIXCDmlUB7-ewH1UvB9K2Otf4rrZuWVJH_uqzq16zw48LdnuLVnPxi8zbNWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qS5mgFD9qSQAgibhozzn1MWO4EfV-vZxgAPWfFSaGD5ELrB_q0auU7WW-x5IS3Q86hNswpnL1KDiRaDmOsee7MFkpSOC0qD4CXkKdWrskEHsvPuaVNOGkuIHMk3YX77BXFZkPPW7t34RqWIeNBlO6a5uImp5RJd-TFjF3pjM7utjGaUEc0m2meT51uGe6LGdjFsNomN71-8jpQKESmInTiIlNrG-qs7OLVJEha5NWI8rMAkZRtKvh8u4wld6F3129QKs0_UolWeGciBiIZYP1LZ55KRRRk_auwjhyIG7E04hSn42he35fkK3CpVVtxYHBQcAgbL7r71zezWbexoP3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vCNTVAJxDH2s1MLl0uc9mrOZbEH0vVnoDnFEKERJ6UjNi2F93dh_i7vVGR-rPG5rvKjhDOnjjzG2Lk_aYCoRQR9z0nWSJ2ZP_FagbDnx9AkLlA3mQ9L01ZpPw1Liep6uCAdXgBu_PR5hwgO_HYdbexrVPPkQXj3ROz4tX6GltO-6f9Wl65Nq9uxFOYcaXoaW4skXDlIzR9YMJe_XPgpNALzpG98cwRuezntctki7NID5j7cMmKZ0F6Dbpg739KyD12ebvrFcXMlcryAvgFBMDn4WFUOFw3L4WDjQ_E4vpH38hL8SZCxbdDMh4-gRxNNpd2h6PQ7nEByjQBB4-w72DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VS8OIuxiypYDq-ah91Ab4sKhOluAw0H6I2h4ybW8pB--hpsF3HbrTIkFF89aGgA4cQz92yr3_pxHOBxkydTL3BiHB_0bH1ABPhrdXIyYz4aUmUusKrH3ab1C3fxGUY5S_mry8vAjjfBjwLZVoPMWHy8vUKIcKmccHmHzC542Ih4pLPhOfL9FhuP4THA11-FC0VUW3eI1xdrqoR_TL2uQti4OlJ0q7mAVlOoVNg45gXHmP-rNCaWrZdHh9ftpA-BL_sUIjZbNbzMOyyCWSJTRxJkkyLgZiVBeIY6wZ310y1U6aZFJ3YD0TkYr1Rv5R0NFK_ZrMUZlB7o-VNnQmyDoqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j1ag60hqz3kED4F6bMDjuUxR4aqYIk_A_nSjbnfb6Sgk3Wjd4ACE4UFqKcEVTHMaUnipWEQ8CVJMW3364hDU824qp-VC06WYAB4oyhEgj9MiGnaNemMF1vNLqoZiSrEbJa0Y5AYNWnhNUN1EZJdZH9COz9wqIpyHOdXX-0V1v9CXDwsityqELr1MYTlUvtxqLh4fRGvE-aRdD0rUQR-IfJqqXpeU1wfW1WB6zoEdAMxp5Vcx7N-uRLuPSEuwx5IvK7GAxBF8rSWFNFnLGAvlg4cyQ57P07G6C_I0IL8vYOsCjvDquqAkuYEXp47z2tpH2nloCGLkpFrlga4iLmkddg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gYWE-gIeqGwkdXHzBi8X-L1m07-Qiv_r2FZMduQJWuplBDYwAM19_tCpCZKCK71G3YO9K-zR7G7W1pcMV2XhgGeF5aykNY2C5QfwNM1EFycOpsaBqVKaPETvqZgBpczWupIa8VF4dhlGtSLOtATllULSuVLpdY9FGttZtHEYwc6dk1fglKO_YYUU3dCZZGpPLHzjIVN0JtAM0jdptYMHZjfeRur9xQqAh6LDGLIVqzcu6zny4DALq84Pa_gPNl0U6OzU_x3l0Cvfiovf3luoQu4fa4KitJMYENT4Py9Wjm-PwdqCuvXCTHvmanULaFNmT2-FbMis6FUuJ0QMNi1vAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTD8V4-lNO8cISMZQPpRlxZNqDEEbzcKkpSQTe8N72rRmJatiqRCfcG-FG2MV6uL1TtaDNHSf0F2physDFbPq4OGwpWFzrYUdfUg1G_cn7lWOqWkN_5Uue7bcuz8PhkpYzWs-IhqyiOyEBsDcpkzwENqO9S8rMXMOdeRy8QCqXOlHs4rR5fjgOXivjkXbMwJ1rP0JTBw2m3nMcjLQgExFfEUqmspp3sm4iCyiZpRk9W5bWtp9mVSslR6lC8zb8E9iNxvDdstI8KXaUF9ZYykFAwxFi1pb7ksTVTJTfA3vbhXNNse-XIQhJWkM-7fDG3B7VBkh-rRaSDGNhkC2jTxGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B1997XKkmBsOp9D-5yIBFqW5ol6kCFk3HDXLGLouF9RronSlq7-ma0t_nKec_M3wF76wBG0V60ANyL4YGJ6Dj1OC116VZ3lu_n1E4BFjs9KZ8_70sQUKWRK__UiUR7Ev1m2DRx_tCDx6D67ERgFn-U4K80aPmoe_nwsiaEoGeFC0DBMb4An_EDaOG4csU3NgYDU1k-YQwqNL2Qc0cV1CksOYutxsJ6bUCDBoVGR0libOFIB76YRYpZ8uxHkPAtYpRPq4LSdUhYb2OXhHjCxvazuZy85Lj1woCgV3tnVDBlf-L9nthUiiK3SpyeUJrQkN_b4aRnt9ggWQfV6YgYvO3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
با دانستن چند ترفند ساده، می‌توانید هنگام خرید میوه؛ شیرین‌ترین، رسیده‌ترین و خوشمزه‌ترین‌ها را انتخاب کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/677574" target="_blank">📅 07:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677573">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
تغذیه رایگان مدارس جایگزین برنامه شیر مدرسه
وزارت بهداشت:
🔹
برنامه «شیر مدارس» به «تغذیه رایگان مدارس» تغییر نام داده است. اولویت همچنان توزیع شیر است، اما تا ۳۰ درصد اقلامی مانند نان مغذی، خرما و بیسکوئیت سبوس‌دار نیز توزیع خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/677573" target="_blank">📅 07:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677572">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfc6fd47bf.mp4?token=LuzU75zzjm6xx-9Hvu-K93kwxXAfMa0nE6MEVWKw-V9nCW8ZK2mqQ375PL815h4zKloPXXd9YpgEDz0C0EMoPoau_LRAt1xIIbjp_au2liMKKaWkT3cfGaGhQuTfx9TZ-sRu37gXicj5AjPeEhuLI_37ZrFrZ0dv1NJxJ8we8rFPz3qdmpohPSUNelD23C_i3Jeeti1eYaFYTfIEMwflqJmNb84cNQIDCqDJN9OcA1tKgajb7X23fltcxRMVpTUaA800Nvbrbh4RBxRcWbGIYL8bSxmL-W4eY-lzQsog1czhtkwOkPYDtp-VrpfXjUQ2mU4cJaCo8Ye1_oC9WIIOTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfc6fd47bf.mp4?token=LuzU75zzjm6xx-9Hvu-K93kwxXAfMa0nE6MEVWKw-V9nCW8ZK2mqQ375PL815h4zKloPXXd9YpgEDz0C0EMoPoau_LRAt1xIIbjp_au2liMKKaWkT3cfGaGhQuTfx9TZ-sRu37gXicj5AjPeEhuLI_37ZrFrZ0dv1NJxJ8we8rFPz3qdmpohPSUNelD23C_i3Jeeti1eYaFYTfIEMwflqJmNb84cNQIDCqDJN9OcA1tKgajb7X23fltcxRMVpTUaA800Nvbrbh4RBxRcWbGIYL8bSxmL-W4eY-lzQsog1czhtkwOkPYDtp-VrpfXjUQ2mU4cJaCo8Ye1_oC9WIIOTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تظاهرات مکزیکی‌ها برای قطع روابط با اسرائیل
🔹
شرکت‌کنندگان در تظاهراتی در مکزیکوسیتی، پایتخت مکزیک، با سر دادن شعارهایی از فلسطین حمایت کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/677572" target="_blank">📅 07:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677570">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OAvgr72ctDnep5MRflaUjacLKADbMKFbVYHsNW0DqJid_WBHBBD0SVumYrEXQjVX94n-rNQ5nA7q7XsSl7ztrjpNpDj6yOiEgp1Lhad6lQhQA0ZCyFUxz4EIlxxAkhfYONJgl4vcUQpxgAUu0rZZX59JSxZAaHtU59Eef64IgVLHlAjlhwGDeIhkIhWc7GWUrf-atfdfwKNVCQdvkIO-ZJ5YLAx9V8Dje2ssx4CPMCfFYWtBcCPTAJZYJCdPGRwSWwDt5VjQ3GhpA7yhBv4DbLrIosm3dmwAHR0s1b2NOi4U6OIUH-DC73TK9V4qU3zBzmf5ZJ3jR8XFNpZ9prnmuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LjhFUhY6MYA4ZDi00olywJBF3nQt3VXC0FXKkdPI57LXoJE74GorlbcRxS6zOsgTqsWO1JGgFnfhsndMttwBUJYAwmtZvyRk-CZumjHRhIE6new-yZtp0MJyZN40wv0WFu79ijTz9otFARkGjwUKqdYoqa3Xv7GqjLJQqFhsmxHxMnv9fOxG3uWXmaX9AehwlM6afHWTreLT2zGV0Kl41p2Sm8khQROJbcGbe3lifpPUGD9iClbazAjWS4dRxeJfldrI_BtS7cxTFeeELOELl1c5_3urmdQ8cKgCWcBHfJL1upGHGjiJuqPi2i1Yb8t9iLNiEav133_TVA6xKtJTtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سدهای مهم کشور چقدر آب دارند؟
🔹
براساس آخرین آمار از وضعیت مخازن سدهای مهم کشور، میزان پرشدگی سدهای مهم کشور تا ۴ مرداد ۶۰ درصد است و در ۶ سد، درصد همچنان میزان پرشدگی کمتر از ۱۰ درصد است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/akhbarefori/677570" target="_blank">📅 07:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677566">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f86c80e059.mp4?token=j_S6xzKTX8PLsYLpfGMLwo3I0Bcjyj2qrbpKNd02ydFau_pCZ4lK9IODCM15JYkggyrRUGitHqNdS9e918tIROn-4-nqS5cmvcxymC53UreSO4iOJs4HL2ZCCE3lGC0st2alyNVXjeyMzBw5Fj8Vw0GyPVjFJeR6H5u6Q5KsiieSR4GFCEN7hMiOnJi5EJmMdiBqc4AnxXW9jXsj-OkxSWl2fkTAQIOc_msrJdpaAeacJun8zvuD7GttcipdFQ49HxZL6d4Ru0HwdQ6HutHoZKJH1pDo6pSG5u0xyQA_Ff0MXLrEZfGlVFv9_jfNxelVAm6jaduDR3BDL4cj7wVh5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f86c80e059.mp4?token=j_S6xzKTX8PLsYLpfGMLwo3I0Bcjyj2qrbpKNd02ydFau_pCZ4lK9IODCM15JYkggyrRUGitHqNdS9e918tIROn-4-nqS5cmvcxymC53UreSO4iOJs4HL2ZCCE3lGC0st2alyNVXjeyMzBw5Fj8Vw0GyPVjFJeR6H5u6Q5KsiieSR4GFCEN7hMiOnJi5EJmMdiBqc4AnxXW9jXsj-OkxSWl2fkTAQIOc_msrJdpaAeacJun8zvuD7GttcipdFQ49HxZL6d4Ru0HwdQ6HutHoZKJH1pDo6pSG5u0xyQA_Ff0MXLrEZfGlVFv9_jfNxelVAm6jaduDR3BDL4cj7wVh5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان آتش در شرق واشنگتن؛ هشدار تخلیۀ فوری صادر شد
🔹
در میان وزش بادهای سهمگین با سرعت بیش از ۷۰ کیلومتر بر ساعت، آتش‌سوزی مهیبی شرق واشنگتن را درنوردید و هزاران نفر را مجبور به فرار از خانه‌هایشان کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/677566" target="_blank">📅 07:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677565">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggyaFHQzrp9gzTTXTTHX9xulpd6vqA_hxr6SA1w81G3rw__sDeKlzSyVx_DH5J5yrI7oyVyNSI2H1sa8FZqysNQTX8jZa4YTzCWRGckxldPuh5L0hDCBKdaXPAcQK7Y_k3H0tEcAgPpZazs7gr6KjVdGlatBIZGVgMBC3phntJtjiV_0zL1TOllPoT91fha-AnjIy-OX4iAkX9KmT5njyvgAaZmy_6mFZKuEOiamhx6XHaMUgjipxhwzvbyweoSAHidfOrB_KCwB50NwuV0axMzpiho55P0Sqs3Nhxa4mars0dMzIoZPMy3Uz_TK9877ala7qPQoeoZ_eJWloQ5tHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای نیویورک تایمز: گسترش حملات سایبری به سامانه‌های آب آمریکا  نیویورک‌تایمز به نقل از مقام‌های آمریکایی:
🔹
دامنه حملات سایبری که سامانه‌های آب در ایالات متحده را هدف قرار داده، دست‌کم به هفت ایالت گسترش یافته و احتمال دارد شمار بیشتری از ایالت‌ها را نیز…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/677565" target="_blank">📅 07:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677564">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پادکست کافئین | فصل‌دو،قسمت‌ده</div>
  <div class="tg-doc-extra">عین القضات همدانی</div>
</div>
<a href="https://t.me/akhbarefori/677564" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
🔹
عین‌القضات همدانی
🗓
در این قسمت، بزرگترین کلاس درس تاریخ را برای «پرداختِ هزینه‌ی صراحت کلام»، «شکستنِ تابوهای ساختاری در اوج جوانی» و «حفظ اصالتِ درونی در برابر سیستم‌های مسموم» مرور کرده‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/677564" target="_blank">📅 07:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677563">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cc1795597.mp4?token=SRqp3NxO9w_IOI5x_wzi1ypG26PfiuFn1VVlYe9MB5XMyiyQWR4o-zUY-M40GKEIwfwOhJnvytZflpe4tRIWhwmTdM7DAAsJbceLTXCR-ixjTXZ1qubREvJj1KDPnoDNGTxuGJO_nPu-4FeVCgQGYqLsjvY-OvcjIxwV6y7j68zDhtOCzSt5jla9gYXAX8yJV7OCcrbCAaBfxxDQtHIDyFdLAJvQfxrW1cZrftmZeYR0f0MUamUofQZndZ5KaxpWWHN9__PZ3FlkdsdvJaolZAHslgJK5MXQ0F_wFTU4iv1FCJGujbasDki3zi0VUu48EjSHU5x4Zsun5MC_Y55wpLOPtc5mzR9Fij-JfY88SIoAdNZQmOAxPlznV5gomyXkyjtljch9Z62Otb3u31c3rHzh60mbyqmcZ6w2T-6jf8jb7oQakJCTnlKuTRQBBnm37WtV3n81ENICZGeyy5Koa9pzy-7o-LNY-3ySMcLnvCjOAL4CRFJyKRIHALbWJTvv1GAsoDOVFaD8QbCivGu-mAGIDeu42DDlUfQj6Ipd-YaA2Y_Dm7_s9QuPW0TPqzfjq8pRwRlFxp9IqEWZX0jXtFxMaikj5pq2FLSBZzGnb7u7ncPoCcVDnMl15AHRqzfS4xgcgAklPU4ziHKrmciCZ9zmW_LiYsa9XDwAqwiJ2g4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cc1795597.mp4?token=SRqp3NxO9w_IOI5x_wzi1ypG26PfiuFn1VVlYe9MB5XMyiyQWR4o-zUY-M40GKEIwfwOhJnvytZflpe4tRIWhwmTdM7DAAsJbceLTXCR-ixjTXZ1qubREvJj1KDPnoDNGTxuGJO_nPu-4FeVCgQGYqLsjvY-OvcjIxwV6y7j68zDhtOCzSt5jla9gYXAX8yJV7OCcrbCAaBfxxDQtHIDyFdLAJvQfxrW1cZrftmZeYR0f0MUamUofQZndZ5KaxpWWHN9__PZ3FlkdsdvJaolZAHslgJK5MXQ0F_wFTU4iv1FCJGujbasDki3zi0VUu48EjSHU5x4Zsun5MC_Y55wpLOPtc5mzR9Fij-JfY88SIoAdNZQmOAxPlznV5gomyXkyjtljch9Z62Otb3u31c3rHzh60mbyqmcZ6w2T-6jf8jb7oQakJCTnlKuTRQBBnm37WtV3n81ENICZGeyy5Koa9pzy-7o-LNY-3ySMcLnvCjOAL4CRFJyKRIHALbWJTvv1GAsoDOVFaD8QbCivGu-mAGIDeu42DDlUfQj6Ipd-YaA2Y_Dm7_s9QuPW0TPqzfjq8pRwRlFxp9IqEWZX0jXtFxMaikj5pq2FLSBZzGnb7u7ncPoCcVDnMl15AHRqzfS4xgcgAklPU4ziHKrmciCZ9zmW_LiYsa9XDwAqwiJ2g4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عین‌القضات همدانی و جسارت بیان حقیقت
#پادکست_کافئین
| فصل‌دو،قسمت‌ده
☕️
🔹
اعجوبه‌ ۳۳ ساله‌ای که نشان داد وقتی یک مغزِ مستقل و جسور، خط‌ قرمزهایِ منجمدِ سیستم‌های متعصب را به چالش می‌کشد، چگونه می‌تواند با طغیانِ فکری‌اش خواب را از چشمِ حاکمانِ زمانه برباید؛ حتی اگر بهای آن شمع‌آجین شدن و مسلخِ جوانمرگی باشد.
🔹
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://youtu.be/hwciVLCsnpI?si=Sn7kIHdYXQ8FWRVS
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/677563" target="_blank">📅 07:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677562">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHvn1hoy1_qI04jev1SUQrv_uRu6-V3TD_Zlar1x_h2MWMDjhRnRQkUvBata08qgMXpJwCG2DQzZ5E4YNnbrOOCS7sFBv82FFfymiAJ9JksxirEkCoQvRHPv5QPE3ZnHfBGpRAAuyxnBN8Ufm_TFHo3HjqhKsKq_j3OxWBcsQwcv0WfArtZs_lr3GSt30vPotldbYfycJOoDTxLNtEWMup0w4YakG2R9n9HOMPLbVhK9IVBfogK8xdalp-nPkVZbeqfcGx063dwAllHHTqmS21E5cdoUA4dBuC93r1GIh068y0o0chtVml67CQfLx1hmPl_nWAMsczM-0rY0JJijPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۱۱ مرداد ماه
۱۸ صفر ۱۴۴۸
۲ آگوست ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/677562" target="_blank">📅 07:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677561">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
ادعای
منابع خبری به نقل از مسئولین نظامی: ادعاهای تروریستی رئیس‌جمهور آمریکا مبنی بر اینکه ایران خواسته است حملات را متوقف کند، صرفاً یک دروغ جدید و یک تلاش مذبوحانه برای باج‌گیری از حاکمان خلیج فارس و تحت فشار قرار دادن آن‌ها با تهدید است
🔹
چه او به تجاوز خود ادامه دهد و چه از آن عقب نشینی کند، نیروهای ما در بالاترین سطح آمادگی قرار دارند و برای هر احتمالی آماده شده‌اند. اگر مواجهه اجتناب‌ناپذیر شود، میدان نبرد تعیین‌کننده خواهد بود و در آن زمان، همه خواهند فهمید که چه کسی قدرت را در دست دارد و چه کسی کلام نهایی را خواهد گفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/677561" target="_blank">📅 06:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677560">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
ادعای المیادین: تعلیق حمله آمریکا به ایران پس از تلاش‌های جی‌دی ونس، معاون رئیس‌جمهور، و رئیس ستاد ارتش آمریکا برای منصرف کردن ترامپ از این کار صورت گرفت
/
موضوع کمبود ذخایر موشکی عامل کلیدی در تصمیم ترامپ برای تعلیق حمله به ایران بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/677560" target="_blank">📅 06:44 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677559">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flb3iM0STzAChgJJLrdcwCa7J8AS_i5wtrrpi3bGfGLKaUeEbkQ69R56yqjbVREAcoBSTnDjG1M_cbHhZVcKcEtz0B4BNLKA9PO-wadv9VEIVJrTtgGQ4MlZag62httEfCMQ7BX08tSs4uJ-Sp0MNNrcpA6HMhk5GmkcCGwtJ86AYks77iNyfZp89HvQVh9rQlzZDPrSFXnlT6daaWAFbkPdubqTh5hp74aLPQlzneUPyQaEt2txCnUKfPcfa3oIL-orbavaiG-dgiv4aK96NtKz1od-qs3egB7lI9JwhTYxAE1dLSHg9UlONkS8_ap0zaBNkG8swgQbIcXmhPuvqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای خوک هار: من با لغو حمله به ایران موافقت کردم
ترامپ:
🔹
ایران و دیگر کشورهای خاورمیانه از ما خواستند پس از توافق بر سر چارچوب‌های یک توافق، هرگونه حمله را به تعویق بیندازیم.
🔹
این توافق شامل بازگشایی فوری، کامل و همه‌جانبه تنگه هرمز و پایان دادن به تهدید هسته‌ای ایران خواهد بود.
🔹
با توجه به این درخواست، من موافقت کردم، به نفع همه جهان و همچنین برای اطمینان از اینکه ایران موفق و مرفه باقی می‌ماند، حمله را متوقف کنم، مشروط بر اینکه توافق به‌سرعت حاصل شود.
🔹
ایالات متحده در آمادگی کامل رزمی قرار دارد و برای اقدام علیه ایران آماده است.
🔹
اسرائیل به شرط دستیابی سریع به توافق، در پایبندی به لغو حمله به ایران با ما همراه می‌شود
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/677559" target="_blank">📅 05:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677558">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
اعتراف روبیو: ایران هنوز موشک و پهپاد دارد
🔹
روبیو، وزیر خارجه دولت تروریستی آمریکا، در یک اعتراف به شبکه فاکس‌نیوز گفت ایران همچنان موشک و پهپاد در اختیار دارد، اما بخشی از توان دفاعی متعارف خود را از دست داده است.
🔹
در حالی وزیر خارجه ترامپ مجبور به بیان قدرت موشکی و پهپادی ایران می‌شود که رئیس و وزرای کابینه تروریستی آمریکا بارها در اظهارات مختلف خود مدعی نابودی قدرت و توانمندی نظامی ایران شده بودند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/677558" target="_blank">📅 05:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677556">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba29a66c61.mp4?token=ZlIzSQCfB1l5QpPJzO4YxWiY_mjH_QoAjPDsDkz-aquejNGoth_gWYInLmPsoazN168IOKSpaDg64FRIbxdaKXIhY8nI2li5qBfcYdxPRivnMqYlob3eeuwQ9kiCtHbv_SKvmU46yNLIovDsU6AUVsT2sPUkJBS5FhLd_vw4sP3SKpX2c4e_7Lk9AIQJM5wm_itzbnwXlDU8Vi9RYZA4c-DxBkg4JpOpxnsqLWmpwH9YjO3iK8EjOIuZ3mhXF6S968FjjL2UoBLQq1uZPd3GT0OjxqR88ZqeS18DKYJZfynpleuFn2R9z6vvzYqKXDrb-Plp1DGNvw06BLyeWchoSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba29a66c61.mp4?token=ZlIzSQCfB1l5QpPJzO4YxWiY_mjH_QoAjPDsDkz-aquejNGoth_gWYInLmPsoazN168IOKSpaDg64FRIbxdaKXIhY8nI2li5qBfcYdxPRivnMqYlob3eeuwQ9kiCtHbv_SKvmU46yNLIovDsU6AUVsT2sPUkJBS5FhLd_vw4sP3SKpX2c4e_7Lk9AIQJM5wm_itzbnwXlDU8Vi9RYZA4c-DxBkg4JpOpxnsqLWmpwH9YjO3iK8EjOIuZ3mhXF6S968FjjL2UoBLQq1uZPd3GT0OjxqR88ZqeS18DKYJZfynpleuFn2R9z6vvzYqKXDrb-Plp1DGNvw06BLyeWchoSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درگیری بین نیروهای یمنی و نیروهای طرفدار سعودی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/677556" target="_blank">📅 05:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677555">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRBwzgwXzY7nQyxv4nD9Ggja7izOt4NXSj-kvQ5B8vkGyfc3pwsn05iloVo9X-XBrPrJ_oYl35sjAXboaR7gp5tZZDbhW3hcxhMIn8F1dPvYxyGmQI_1b_Ykz3p_AKAFl8PljR9sBcO5QNm2dYFWj1hL85o3CidzTi0k3wgqO-J_CldczigUUOodyh2uNPXrmcyLMUXy-kXcuRVIQdZnh2XVTC9QMw9d7vvJYTJOh7mwW4C0-oE6fx6R1H5X4ctQ_cohFkm_hEnkvOFtmXoP8h5Q20maQfFoV_gLJbXOO0d_CbOLMdXOLoowmvK30mrLp9Ed7zJaqmQCfCnjAHnhcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیست و نهمین پست سگ زرد در ۲۴ ساعت گذشته
🔹
دونالد ترامپ در ادامه پست‌های رگباری خود، تصویری از جلد مجله نیوزویک درباره ونزوئلا را منتشر کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/677555" target="_blank">📅 04:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677554">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
ادعای اکسیوس: میانجی‌های قطری روز شنبه در تلاش برای دستیابی به توافقی جهت بازگشایی تنگه هرمز، به‌طور جداگانه با عراقچی و ویتکاف، فرستاده ویژه کاخ سفید، و مقام‌های عمانی گفت‌وگو کردند
🔹
به گفته یک منبع آگاه از این مذاکرات، این گفت‌وگوها پیشرفت‌هایی داشته است، اما هنوز مشخص نیست که این پیشرفت‌ها برای کاهش تنش و مهار بحران کافی باشد یا خیر./ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/677554" target="_blank">📅 03:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677553">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
ادعای آکسیوس: بن سلمان، ولیعهد عربستان سعودی در گفتگو با ترامپ نسبت به طرح آمریکا برای حمله گسترده به ایران ابراز نگرانی کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/677553" target="_blank">📅 03:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677552">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
کپیتال وان: حساب‌های ترامپ به دلیل شناسایی تراکنش‌های مشکوک بسته شد
🔹
بانک «کپیتال وان» در یک پرونده قضایی جدید اعلام کرد بسته شدن حساب‌های ترامپ در سال ۲۰۲۱، نه به دلایل سیاسی، بلکه به دلیل شناسایی موارد مشکوک صورت گرفته است.
🔹
کارشناسان واحد ضدپولشویی این بانک پس از ماه‌ها بررسی، الگوهای تراکنش مشکوک در حساب‌های ترامپ را شناسایی کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/677552" target="_blank">📅 03:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677551">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ادعای رسانه‌های امریکایی: در پی درخواست‌های وزرای امور خارجه ترکیه، قطر و پاکستان مبنی بر آمادگی ایران برای برگزاری جلسه‌ای در ژنو، سوئیس، به منظور ادامه مذاکرات، فرماندهی مرکزی ایالات متحده به طور موقت به مدت ۴۸ ساعت، عملیات شبانه خود را متوقف کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/677551" target="_blank">📅 03:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677550">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
منابع عراقی: صدای انفجارهای جدید در سلیمانیۀ و اربیل در عراق به گوش رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/677550" target="_blank">📅 02:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677548">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d85ffc549.mp4?token=oY9jtBKzwMDQFRjw1zYQD2-tYs98oL-5JMRkeMY1L-L35Lrat8JJOrTHvm72PsDlpFfBo1OVxpVGXS3E9QmZ6MaAXKUaFVe6zNRlXvvEpBfb0Ls1Lhe_e2tmzkYhkfaOo6_o1YrC9_MXrzP341pZpZCrMC9f5ecnPY5rAOec0ReI9eehk44KTCvhoh8qrxsYq_eurRgosbCupxlSaIq0-7gVGOkXG5vt3UwtTo_jhGRZqOnXxx9StfTZS22c7fAuiyJEvGk-e7KRHf9IWUrL-R3SmKzPleMGJdQaEHFddFgrhHxXmvTVz0ig4Yqpy9u3BGDFCrCXGVUlBqb51BFfbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d85ffc549.mp4?token=oY9jtBKzwMDQFRjw1zYQD2-tYs98oL-5JMRkeMY1L-L35Lrat8JJOrTHvm72PsDlpFfBo1OVxpVGXS3E9QmZ6MaAXKUaFVe6zNRlXvvEpBfb0Ls1Lhe_e2tmzkYhkfaOo6_o1YrC9_MXrzP341pZpZCrMC9f5ecnPY5rAOec0ReI9eehk44KTCvhoh8qrxsYq_eurRgosbCupxlSaIq0-7gVGOkXG5vt3UwtTo_jhGRZqOnXxx9StfTZS22c7fAuiyJEvGk-e7KRHf9IWUrL-R3SmKzPleMGJdQaEHFddFgrhHxXmvTVz0ig4Yqpy9u3BGDFCrCXGVUlBqb51BFfbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ستون دود برخاسته از مقر تروریست‌های ضدایرانی در سلیمانیۀ عراق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/677548" target="_blank">📅 02:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677547">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b60f221b6b.mp4?token=umgMP99pKjjlTQe9MTDUA_8F897D66OMD2DRONahMTg84LGCPz3NrrZJKgd1fd87UBXsK1rP-WRto8whjToKLWK_gv3v7sd2o2Zm3rW0JI7_6XnJwAPYok8JXUqo3RB_HLGploEQgdO2iYpN9TfmKzRWJYdpNeEaZTNIhukCYJm9MU-mmHirN5gfJ16kZUkCWdCuwOsRG9DZ_ELkGj33EImGWj7Y0GNU_0v1k_AQuvVu_cEibzsX419rz4MEWCy5ouRbUu_xBq6k7S022XH7gdf3q0_JFc1rw38Sk560E4hDLwy2grvfx2QkY1hwXUGfq36XazmPIhatoufIVnRvwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b60f221b6b.mp4?token=umgMP99pKjjlTQe9MTDUA_8F897D66OMD2DRONahMTg84LGCPz3NrrZJKgd1fd87UBXsK1rP-WRto8whjToKLWK_gv3v7sd2o2Zm3rW0JI7_6XnJwAPYok8JXUqo3RB_HLGploEQgdO2iYpN9TfmKzRWJYdpNeEaZTNIhukCYJm9MU-mmHirN5gfJ16kZUkCWdCuwOsRG9DZ_ELkGj33EImGWj7Y0GNU_0v1k_AQuvVu_cEibzsX419rz4MEWCy5ouRbUu_xBq6k7S022XH7gdf3q0_JFc1rw38Sk560E4hDLwy2grvfx2QkY1hwXUGfq36XazmPIhatoufIVnRvwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرواز پهپادها در آسمان سلیمانیه به سمت اهداف خود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/677547" target="_blank">📅 02:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677546">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌شدن صدای انفجار در اربیل عراق خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/677546" target="_blank">📅 02:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677545">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d948585bf.mp4?token=chSxA2x9El1rad8ZpBJDJj2RndhVzmi6Fv4ybeJzDWI05IFPvVxbaAelMY-OPjwUnNIQdIG22z9NI5o7xpFh_bnkc47zostjtk4OkyqsooGJQu8pNuStq9f1tc6UO_qqh8Xz0e-F4u3h1HnlqL4-TSNqVkU_DQnuODVuvYN7SrPr-9FRUh-V0F99UwofofIeUNj2XdwrTrKf-exfFqjrBjStZGXoyIBClVOfIUdOfS72-3txawp_yThedNzx6MCz2NVb8SIPx_bbeRieTHXDech9128K5x838YXui1E1Xu1XNl1zJzrttGcoOn9AnTwPeDJ2bNGTER2IEG9DfaZHvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d948585bf.mp4?token=chSxA2x9El1rad8ZpBJDJj2RndhVzmi6Fv4ybeJzDWI05IFPvVxbaAelMY-OPjwUnNIQdIG22z9NI5o7xpFh_bnkc47zostjtk4OkyqsooGJQu8pNuStq9f1tc6UO_qqh8Xz0e-F4u3h1HnlqL4-TSNqVkU_DQnuODVuvYN7SrPr-9FRUh-V0F99UwofofIeUNj2XdwrTrKf-exfFqjrBjStZGXoyIBClVOfIUdOfS72-3txawp_yThedNzx6MCz2NVb8SIPx_bbeRieTHXDech9128K5x838YXui1E1Xu1XNl1zJzrttGcoOn9AnTwPeDJ2bNGTER2IEG9DfaZHvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زبانه‌ کشیدن شعله‌های آتش از پایگاه‌های تروریست‌های ضدایرانی در سلیمانیۀ عراق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/677545" target="_blank">📅 01:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677544">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌ شدن صدای انفجارهای پیاپی در مقر تجزیه‌طلبان تروریست در سلیمانیه عراق خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/677544" target="_blank">📅 01:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677543">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgS7JgROEyJ3UxTlziKDA4m7fKwHK_GMxh4nYD6A8BFbwpw5-_A14CzqiIvkt6SxC-TYp8l9jEuo6UH6STa5BEXg5m9fXNRWTCYm14ypa2AXyQtrYYOMZoOjLtEvLhOwf7ORT68lDCOhvU9CJlQPSWlNOkNCDFjUA1rCFTZKMfdhXmHxJ7ZlHxdH-S5JBdXK-LTRWBmzjmfN0x9kgeRNJMnK2JlXcsc1C1af6S1-1W_SsIkb5AQkaDfn_0ADElD6asv3vMjyAKOTBPs5iYvS1BeEW9BHuyIGxj68lKf_XTB43h98tX6L8g6YWWzL59wedQmeAotK8vuqTZrT7bbIKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/677543" target="_blank">📅 01:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677542">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dY21ulq2bo8rqMreM97TTLrnsXzIb4JVALNXu9EJUh5Z5Wo2PUcz8MFg6-mKfNfT336W583k9_dk8tmZafRdWMDmNv-k2o5QYNtPSklXwtyxSYIWWB-DDBtfZnRsgEzzVNmmsI_g_bLLmKw0ZTCGsbVGFsgiAekd4163HuLm7kr-G771Is2rFd1eDA1VCFRQsV7F1WdQMA3UaqEc6zB--BwmCPohn_jfyVXlszBfnBay6jUoswjEbYJI1F8o_CkgNuU3lHN0TQeJgK0dJEzvx0RHFi_FBqOB3iNAhPNV7yhORchFx6H0NLYvuwJple2KS37taKEKaSmw96C3KbUW5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دو سوم آمریکایی‌ها: جنگ با ایران ارزشش را نداشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/677542" target="_blank">📅 01:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677541">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
وقوع انفجار در یک کافه در مسکو
🔹
خبرگزاری فرانسه به نقل از پلیس روسیه از وقوع یک انفجار در کافه‌ای در شهر مسکو خبر داد که منجر به کشته و زخمی شدن شماری از شهروندان شد.
🇮🇷
✊
@AkhbareFori | Linkظ</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/677541" target="_blank">📅 01:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677540">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
هشدار رئیس کل دادگستری گیلان در خصوص کشت مواد مخدر در روستاها
🔹
رئیس‌کل دادگستری استان گیلان با تأکید بر برخورد قاطع و هوشمندانه با جرائم مواد مخدر، نقش دهیاران را در پیشگیری از کشت مواد مخدر کلیدی دانست و هشدار داد در صورت اطلاع از کشت این گیاهان و عدم گزارش آن، با متخلفان برخورد جدی و قانونی خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/677540" target="_blank">📅 01:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677539">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: لایحه کنوانسیون دریای خزر در انتظار رای نهایی مجلس است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/677539" target="_blank">📅 01:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677537">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">40 Rooz</div>
  <div class="tg-doc-extra">Mohsen Chavoshi</div>
</div>
<a href="https://t.me/akhbarefori/677537" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
۴۰ روز
🎼
چاوشی
🔹
موزیک جدید چاوشی به مناسبت اربعین حسینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/akhbarefori/677537" target="_blank">📅 00:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677536">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDRA1vdwii2NE4Egh4LI4G-tKc2ZLajNeZTPR_lDMgzBiGpmzTTyFRSD1xyHuVnOCGd2fRTxFw0nKXBPKsXyPXITiVJE8mPUjq_xzZJUtDg9_J2NgPq4ho6tsxOpoaJe59tfUNavFWl5DM3u3eiNhfUFJGh18FmQ-AOq4voEZkaN4JjyhIvkCQotkjfL769jk666IFYKs0FUTMt-oua-CUU1kxdtOWYuU98r-St4PXIi7p5IM8O955lbJQeljW-40etB-oIrLlgfmK52W40WOs4HYmTKtrqVhbsUhOMo3NyxQNQC9mm2VWVaq8XFAtZ1QOaMnre12-XNY4FJwvewFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزارت خارجه: تداوم محاصرۀ دریایی و حملات به اهداف نظامی، غیرنظامی و زیرساخت‌های ایران، مصداق «عمل تجاوزکارانه» و نقض منشور سازمان ملل است و ایران از حق دفاع مشروع خود استفاده خواهد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/677536" target="_blank">📅 00:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677535">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtVXEL0pDbX6YM5B5JM0ryxA6zrBXA34OCVP9vqfWrYIB00iAvha-7K4-Ru0Ba_jv9qLQvdlDu-tSbdSjpVXCU_iX_lBCDEbFEkstJqZ-D2fvUGPlZt9i1bfTbdG80ZrD3fKXaSyXFFmvLSiKkTHGCSQ_JfGyw6PikobN2FzElaWIaVSaKTKnRoNLAmUeFe4cNz9NovS1KP3BWYDtAllFK12apqqp-Dq2Dw32c2dH2D47tHz7rp1UmrFCzi4CWs-GwoThGUsGk7s9Tn0hC5h-junnx30luXE9B8qXRgZDAuP-JcmPDW2llFb3KB3e9mHS9cU9WmckcRsNk_XfB44bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تجاوزکار می‌بایست با تابوت برگردد
🔹
طی روزهای اخیر تب جنگ در منطقه بالا گرفته است و به نظر می‌رسد آمریکا قصد دارد بار دیگر دست به حماقت بزند. آمریکا اخیرا برای شهروندان خود در منطقه هشدار امنیتی صادر کرده است اما با این حال به نظر می‌رسد این هشدار صرفاً محدود به شهروندان آمریکایی نخواهد بود و در صورت تکرار خطای این کشور فراتر از شهروندان تمامی نظامیان و منافع آمریکا در منطقه و حتی سراسر جهان نیز در معرض هدف موشک‌های ایرانی قرار خواهند گرفت
🔹
هشتصدوبیست‌وپنجمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/akhbarefori/677535" target="_blank">📅 00:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677534">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zf3TMCj2DuLiu1YuqWHMyB5XKAveI19nbSDStKmmd-h1lYL_Q6ASeBzpGn77uCtRUTBjt7bdceXi40T9InCNkpaCNHdc1fxQCQBnYc_t6jPbAAwzvMrRu5-gbwOFI0yUhh0sSDmuO0bImK0Cr989sQ_IfaExq82xL1HjyIAWVUos5zm-uioMS65gAlcWammf8AIi0thLYKDsucjdPKkZwcMUvYPifFqBHBTEiV3KHKwEXNLTzqTEF1ZTuyNF4lg7Hv-oTi8U6ZUd3GroL4q2BmqH6E6vlgUqsvEPJajGAaNbUAa71--Xa2MIsGxLBnXoJjY0avCMFys041YupEL4Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعداد هواپیماهای سوخت‌رسان آمریکایی در رژیم صهیونیستی همچنان در حال افزایش است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/677534" target="_blank">📅 00:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677533">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIXZ76Jt2R0nJ6SdLEw3-0IJ3tgUzpmheI2Hr49s0GJ4gpfyAm2iUeG8xnusCYoAHGlcEXuNO9cwe_AlNgVQJ7Li4VIGN8dPhL8h032YLS5F8tPOkaw5LX8aEjFGN4_b6nO2pc0tZW1QfbwHdkaqvOduXNn3CbJF7iutmfvTcKfwkyzVNUN7kH8PaxO43a0XFoaQHNbl1DBQWazAdnvJbibLzcHzLAEbNaqQyFBSIkb9i62uHPaJNFaPuuZak9kGHCeSnP98o9v3b24GrWmXUVq_LrsBNKW4B-N2K24j2SKnbzcuVST0nJAWboDeZGB-MXF1k6FSz92eK_S5hzN9hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دو سوخت‌رسان آمریکایی از فرودگاه بن گورین برخاستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/677533" target="_blank">📅 00:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677532">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mq4RhFN_8xrTXSj3Pbwh7AaFPpGnvM-eUKtVSWblsL09fubDEHaLuqpnsBfL8pyIqSsQ4HxnkpNDa6x8IvxIsaDdeFEKxlOys2sucR7y4XwzA2qTABfIIjk1dDZ91VjptdiX-equtZT1W-il-qSzMw3pPvj2e28gkAV6jnVOu0G0d5JxEGLBXQ4bfrNyk5j0QFeRdrGXp3eeJ9-3Db_jV_y8vf5rmybTm7F4gfPkb58KqqI4SW_fEJj0QNFvp5ExHaxldfdRWneUt6ToKv66cCTMupDicHfQkwfvV5Xsq3V84S-l6WE1JdPMFHKWgAsYjhMu3K6pioUAenkfGWb-pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک هواپیمای شناسایی آمریکایی (آواکس) از پایگاه شاهزاده سلطان عربستان برخاست
🔹
براساس داده‌های ناوبری هوایی، دقایقی پیش یک فروند هواپیمای آواکس آمریکا در آسمان عربستان به مقصد یمن رصد شد.
🔹
آمریکا این هواپیما را از سال‌ها پیش برای جاسوسی هوایی و به عنوان رادار متحرک طراحی و استفاده می‌کند.
اخبار لحظه‌ای جنگ
👇
khabarfoori.com/fa/tiny/news-3234810</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/677532" target="_blank">📅 00:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677531">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
آماده‌باش سراسری در بیمارستان‌های فلسطین اشغالی
🔹
منابع عبری زبان گزارش دادند همزمان با افزاش تنش‌ها  در منطقه، تمام بیمارستان‌های فلسطین اشغالی در وضعیت آماده‌باش کامل قرار گرفته و به کادر پزشکی نیز دستور آمادگی فوری داده شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/677531" target="_blank">📅 00:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677530">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
کاظمی: برنامه‌ریزی‌ها برای بازگشایی به‌موقع مدارس انجام شده است
وزیر آموزش و پرورش:
🔹
سال تحصیلی جدید در شرایط فعلی، طبق برنامه از اول مهرماه و به‌صورت حضوری آغاز خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/677530" target="_blank">📅 00:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677529">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
چند پیشنهاد جایگزین برای گران کردن بنزین
اسماعیل حسینی، سخنگوی کمیسیون انرژی مجلس در
#گفتگو
با خبرفوری:
🔹
افزایش قیمت بنزین در سال ۱۴۰۴ نه مصرف سوخت را کاهش داد و نه وابستگی به کارت اضطراری جایگاه را از بین برد. شنیده‌ها حاکی از آن است که دولت دوباره به دنبال افزایش قیمت بنزین است.
🔹
پیشنهاد جایگزین این است که ابتدا باید سیاست‌های غیرقیمتی و عدالت‌محور اجرا شود. انتقال یارانه سوخت به کارت بانکی متصل به کد ملی، صدور صورتحساب الکترونیکی، توسعه سبد سوخت و توزیع عادلانه یارانه انرژی می‌تواند فعلا راه‌گشا باشد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/akhbarefori/677529" target="_blank">📅 00:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677528">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3af1f4879.mp4?token=TE80ialzJ5eakYfzxrunulnId8naxacv-BkB7fLYPJ_tUqmKSDolB1eBm8a5XhRGIWroBoDhhMmIoAPLBVnmYFyiV0XNn0sYanttr4sZQxHSGUrLer_fSmzaJQw8hc-DrTveNNVg-dFUhqGqA0t-1ulSYykOaTpvtaxTaScxu51biUhyXVZLbBFqtSeP76WuoJaEh_4PyPvlvLtcVGzITljPldPkf9wSQvYgU_tYw2WcafgVnwLb1rS9Eb3xpUss9DocrK4Uoy3LFXfCO9RAnv7WoDomXdZYF1wN5hYwP9cP095h4tJ0lpBX9ZEare5_RQ-xwvt2YTAKk_mamtszzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3af1f4879.mp4?token=TE80ialzJ5eakYfzxrunulnId8naxacv-BkB7fLYPJ_tUqmKSDolB1eBm8a5XhRGIWroBoDhhMmIoAPLBVnmYFyiV0XNn0sYanttr4sZQxHSGUrLer_fSmzaJQw8hc-DrTveNNVg-dFUhqGqA0t-1ulSYykOaTpvtaxTaScxu51biUhyXVZLbBFqtSeP76WuoJaEh_4PyPvlvLtcVGzITljPldPkf9wSQvYgU_tYw2WcafgVnwLb1rS9Eb3xpUss9DocrK4Uoy3LFXfCO9RAnv7WoDomXdZYF1wN5hYwP9cP095h4tJ0lpBX9ZEare5_RQ-xwvt2YTAKk_mamtszzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه‌ای که سوژه شد؛ شکستن صندلی کنعانی‌زادگان در میانه مصاحبه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/677528" target="_blank">📅 00:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677527">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66cf7e52d7.mp4?token=Xpi18RNH83g7ZafRstbJY62pzEhF33qMKjMrKmjPZW3x1zrqkFeWRSrWRBopX86-XMk2W9lmaQAMOwYHr9BtQ02uUamChwY7tkMd0TyyPEs8Xq-tsfyigXiSmWtfW3_e_bYlPeI5OYdBbsB9DKrYqz1Hg7TM6r4nWrxCdAsp-Ww8LiF_aqQvwXGEtuUd5ExyQeL6Gd3AzlsJyqx2YW7QVRJsxw0Bks5UIU00P3cOlSVM4WOnv9Y4L-Pc20UhRq3ApjlY1Dwp9ij3235OdDEIMlePmqTyKs8k4eVWc8vPOl-JXEAGEKyPRk7QptcJ0pzypMBquDrsI_X8e9IdLk7UGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66cf7e52d7.mp4?token=Xpi18RNH83g7ZafRstbJY62pzEhF33qMKjMrKmjPZW3x1zrqkFeWRSrWRBopX86-XMk2W9lmaQAMOwYHr9BtQ02uUamChwY7tkMd0TyyPEs8Xq-tsfyigXiSmWtfW3_e_bYlPeI5OYdBbsB9DKrYqz1Hg7TM6r4nWrxCdAsp-Ww8LiF_aqQvwXGEtuUd5ExyQeL6Gd3AzlsJyqx2YW7QVRJsxw0Bks5UIU00P3cOlSVM4WOnv9Y4L-Pc20UhRq3ApjlY1Dwp9ij3235OdDEIMlePmqTyKs8k4eVWc8vPOl-JXEAGEKyPRk7QptcJ0pzypMBquDrsI_X8e9IdLk7UGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رنگ‌های اصیل ایرانی؛ هویت بصری ماندگار در هنر و معماری ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/akhbarefori/677527" target="_blank">📅 00:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677526">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVXaagVgm5wyGmqob0_iZs_yrdtHeL1PCk20g0aq-iAu4wuDlhYCmNjrkikLmGLFK2fsVPLtJ_6dee6kE2ubIggeGnRMch22UnN14_cisced3G6-cgqdlrwTYsgI53dRWrLIG6bseCoOIzBJx7nB1Jzm34ZNWi56GDrs8V0CInewD9WqH8qmRD982Z67D5_L7bP4e8Js_f0squyMxXEWttFN02FJgC1SCisTqpBS4JQRmXBgMV__tSa_sY5RY4_5UwSqwr3p8IjlsB1FdggQ0R3MfXNllQTkGOIh5jbYv_f9iz5RCGP_ZvnBCTat9gJSvRPfgngxEQYAfGxeWC3E6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
هدیه سفر کربلا برای ۱۰۰۱ نفر از عاشقان حسینی؛ زیارت آقای شهیدان به نیابت از رهبر شهید انقلاب
✨
‼️
کافیست عدد
۲
را به سرشماری
۳۰۰۰۱۱۵۲
پیامک کنید.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/677526" target="_blank">📅 00:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677525">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
ادعای المیادین: اطلاعاتی وجود دارد که تأیید می‌کند گروه‌های تجزیه‌طلب برای انجام عملیات علیه ایران، از خاک عراق، در حال آماده‌سازی هستند./انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/akhbarefori/677525" target="_blank">📅 00:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677524">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8de4ff1be5.mov?token=l7FU43D-ZT66ZShEC8qDBojgIjcuhsgnhgKSXoJ_MvfV3gEFkAkxx88PYikCQ0trxnY_kzs7ZBDcfrj47GOsTFLf1av7OAWBclqirQ2GSQXp4E8F94IoJFGuxHJvVu8eBO5hyzsjezR-LpU-6x9F1HQ7inNbE7ZPhLE7MckOmIW4I1v3O0jacY6SVIfnBML04okssImsw4PKve2hQ63JOYrH9ccSEhlc_fdOKNQ-IuFYRHFhAsN2c3cPqoI64IVV9PYKvxmjZY78pDNM-oAk40KAYLSst2G2-oS2lxfAl7HqvTCovfmWfZF1qjr3NRez5Mz1wuBW_c46fqcP7Ilmcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8de4ff1be5.mov?token=l7FU43D-ZT66ZShEC8qDBojgIjcuhsgnhgKSXoJ_MvfV3gEFkAkxx88PYikCQ0trxnY_kzs7ZBDcfrj47GOsTFLf1av7OAWBclqirQ2GSQXp4E8F94IoJFGuxHJvVu8eBO5hyzsjezR-LpU-6x9F1HQ7inNbE7ZPhLE7MckOmIW4I1v3O0jacY6SVIfnBML04okssImsw4PKve2hQ63JOYrH9ccSEhlc_fdOKNQ-IuFYRHFhAsN2c3cPqoI64IVV9PYKvxmjZY78pDNM-oAk40KAYLSst2G2-oS2lxfAl7HqvTCovfmWfZF1qjr3NRez5Mz1wuBW_c46fqcP7Ilmcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم اکنون|یک بمب در محل جشن تولد ژنرال الکساندر چایکو،فرمانده نیروی هوافضای ارتش روسیه منفجر شد
🔹
چندین فرمانده نظامی روس کشته یا زخمی شده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/677524" target="_blank">📅 00:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677523">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
نخست وزیر عراق: هرگز اجازه استفاده از خاک عراق برای تهدید کشورهای همسایه را نخواهیم داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/677523" target="_blank">📅 00:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677522">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffPRpWRoS_FpV3aBwYvH_83pJTph6gitqX0NyasyCuIhwV5q6m-1nchpAs3TTAY2-u6VO9T1uic6KpxzHEMJrqs5Tk09O8RJXMch_DrUu8-ti-DpPeStHbIsO2uqJzSRMjZRh5wT0i33tqqpDJ8LbjKmHYatiF84UchTag6VKY65r2GkaJ2GX_vkUWKDkMaqDnmC4YkWjtdtsKhshHowjtUikYojIxazDLDnYQm9npdD8Vq0phdrcJiEQFhb6dcZ1L8e6nkuSmGXOqVTdP7InGuZL6qU9pke51QXHxp1NJA7ZJh0M5Vo4FNFrHeXoK97WGRlIaM38i0Yb47TPnmt8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/677522" target="_blank">📅 00:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677521">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را ازدست ندهید
🔹
🔹
جزئیات تازه از احتمال حمله قریب‌الوقوع آمریکا | نتانیاهو: دروازه‌های جهنم را به‌روی ایران باز می‌کنیم
👇
khabarfoori.com/fa/tiny/news-3234810
🔹
جنگ ایران در پیشگویی باباوانگا پیدا شد | او از چه گفته بود؟
👇
khabarfoori.com/fa/tiny/news-3234757
🔹
هدف از حملات احتمالی آمریکا به ایران چیست؟ | مدل جنگ عراق تکرار می‌شود؟
👇
khabarfoori.com/fa/tiny/news-3234815
🔹
افشاگری تازه مشاور پیشین احمدی‌نژاد از حمله به محل اقامت او + ویدئو
👇
khabarfoori.com/fa/tiny/news-3234644
🔹
ماجرای درگذشت فرمانده بسیج شرکت ملی گاز ایران در مسیر اربعین
👇
khabarfoori.com/fa/tiny/news-3234640
🔹
با نصب اپلیکیشن خبرفوری، از خبرها جانمانید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/677521" target="_blank">📅 00:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677519">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
چرا ایران با هیچ کشوری قابل مقایسه نیست؟
🔹
آمریکایی‌ها در مورد ایران اشتباه فکر می‌کنند و معادلات خود را به غلط چیده‌اند. به اذعان کارشناسان غربی ایران با همه کشورها فرق می‌کند. چرا؟ در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/677519" target="_blank">📅 23:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677518">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
الجزیره به نقل از منابعی در وزارت امور خارجه ترکیه: هاکان فیدان در تماس با عراقچی بر تلاش برای پایان دادن به درگیری‌ها و تثبیت صلحی پایدار تأکید کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/677518" target="_blank">📅 23:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677517">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltrqJulzUWsgMzOAsI0iSCajdaR0u1eu6capvO5qEq0qJ3MVLUOMmqvXKlKXoMkFtG6aUYTxkSBwOgw97nvbw10rBmgNd-OhfJZU-eSbuxfwuh0hTFhK4Ix0mzggNIA0ClIDq_arOs6bhNrhUn8uPnMCM74Zo-me4LAxX_BocjpBIYBK_OHl3P-aGdfJrqQA6EN7Ujmu9eiBkn4fehkReXz0bXtH9XCj0l5d_YSPdw-BX1WpHyHRHBPqfbprSuCVJ4oir372Ri-YMHlyxSNRJg8joXgpPOYyFkgwg_w5Wn-bmqnsRJzsRFqQ5qnSmZyelI6i_GNWckOAEei0-i5kPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هاآرتص: شکایت کارمند سابق از همسر نتانیاهو به اتهام آزار و توهین
🔹
یکی از کارکنان ۶۱ ساله پیشین در اقامتگاه رسمی نتانیاهو با طرح شکایتی حقوقی علیه دفتر نخست‌وزیری، سارا نتانیاهو، همسر او را به آزار و اذیت‌های مکرر متهم کرده است.
🔹
این شاکی مدعی است که فشارهای روانی و رفتارهای ناپسند همسر نتانیاهو در محیط کار، سلامت او را به شدت تحت تأثیر قرار داده و با آسیب جدی مواجه کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/677517" target="_blank">📅 23:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677516">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
باج‌گیری ۳ هزار میلیاردی ایران اینترنشنال از مدیران بلندپایه اقتصادی کشور
رئیس پلیس امنیت اقتصادی فراجا:
🔹
اعضای یک شبکه سازمان‌یافته موسوم به «باج نیوز» با جمع‌آوری اطلاعات شخصی و خانوادگی مدیران بلندپایه برخی صنایع بزرگ، به دنبال اخاذی و سوءاستفاده از این مستندات هستند.
🔹
بسیاری از این اطلاعات فاقد اعتبار لازم و ساختگی و دروغین هستند.
🔹
این شبکه تلاش می‌کرد ضمن تخریب هدفمند مدیران و فعالان اقتصادی و اخاذی از آنان، در روند سرمایه‌گذاری کشور اخلال ایجاد کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/akhbarefori/677516" target="_blank">📅 23:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677515">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/f15c065ae0.mp4?token=vAMCZBo1VsO1zlpsoU2BE-GsNZL7Ezlps8LNHSwqUjfywlSoO8jWwe4xh3WAss87Z5krzlWaZG5Q8Y87RoEe86w4V-hgzzZZs6yO9w19kRpOfALOAXvEH2RX_oxjMQGUjkxBLsf6DiWCQ2t-3CLQxc76dAyA-YUiBH9hZLGelYxW94RN4zSEaOuts4Uay2C10A_KnPcVTE9o1e6FM6g0LD0jWcU8irqMf-6l1PFozGxKjVpOHSqpa6Unx_QqYb00xx20NQQuU_EznlXGhjhCklIHNQMvSW6wiJpIrpMQzkjG92OKgnOeayXFp2GbhNAIT5ya5xZtf7i03n10_NXe3g" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/f15c065ae0.mp4?token=vAMCZBo1VsO1zlpsoU2BE-GsNZL7Ezlps8LNHSwqUjfywlSoO8jWwe4xh3WAss87Z5krzlWaZG5Q8Y87RoEe86w4V-hgzzZZs6yO9w19kRpOfALOAXvEH2RX_oxjMQGUjkxBLsf6DiWCQ2t-3CLQxc76dAyA-YUiBH9hZLGelYxW94RN4zSEaOuts4Uay2C10A_KnPcVTE9o1e6FM6g0LD0jWcU8irqMf-6l1PFozGxKjVpOHSqpa6Unx_QqYb00xx20NQQuU_EznlXGhjhCklIHNQMvSW6wiJpIrpMQzkjG92OKgnOeayXFp2GbhNAIT5ya5xZtf7i03n10_NXe3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط مرگبار هواپیمای گردشگرها در پرو
🔹
به گزارش خبرگزاری فرانسه، در پی سقوط هواپیمای حامل گردشگران در جنوب پرو دست‌کم ۱۳ نفر جان خود را از دست داده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/677515" target="_blank">📅 23:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677514">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
یک مقام آمریکایی به خبرگزاری آکسیوس گفت که ایران در روزهای اخیر بسیار تهاجمی عمل کرده است و برخی از مقامات آمریکایی از میزان آمادگی تهران برای تشدید جنگ شگفت‌زده شده‌اند
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/677514" target="_blank">📅 23:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677513">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
شنیدن صدای هواپیماهای بدون سرنشین در آسمان سلیمانیه در شمال عراق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/akhbarefori/677513" target="_blank">📅 23:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677512">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بدهی دولت به تامین اجتماعی ۱۲۰۰ همت شد
احمد فاطمی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
دولت حدود ۱۲۰۰ همت به سازمان تامین اجتماعی بدهکار است. در بودجه ۱۴۰۵، پرداخت ۲۷۵ همت از این بدهی در قالب اوراق پیش‌بینی شده که دولت تاکنون آن را پرداخت نکرده است.
🔹
بهانه‌ای برای عدم پرداخت بیمه بیکاری وجود ندارد و سازمان تامین اجتماعی باید از هر طریق ممکن و از طریق خط اعتباری دولت و بانک مرکزی، بیمه بیکاری را پرداخت کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/akhbarefori/677512" target="_blank">📅 23:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677511">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
تماس تلفنی عراقچی با فرمانده ارتش پاکستان و وزیر خارجه ترکیه
🔹
عراقچی در تماس های تلفنی جداگانه با فیلد مارشال عاصم منیر، فرمانده ارتش پاکستان و هاکان فیدان وزیر امور خارجه ترکیه، ضمن بررسی آخرین تحولات منطقه‌ای، درباره پیامدهای اقدامات تجاوزکارانه و بی‌ثبات‌کننده ایالات متحده آمریکا و خطر تشدید تنش‌ها و ناامنی در منطقه گفت‌وگو و تبادل نظر کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/akhbarefori/677511" target="_blank">📅 23:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677510">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff1e3182e6.mp4?token=EHajlRnrCqS-86phKRJ6y70BfXdowIxB-5MnOJb7-WvpycppOGTskwmac8EN8vmnIcyKKmrNWORS6aPENHXnaAuqIZKPx0AQFnhZW2z99fHdYYF8lK1AP8Li0iWodHxr52KBQ-o1KvwlNeHjml2cBeJ-lpZjOxepjNzA-lc0F2qEjQ6BT7OnXnhB9kQCQ5ak48uPlSMSVyUpuu1ctlw0IbYZEkfMGhrypXu8wimASG7HxkGtv5TLZ_LG-Mp7ptN1Z5yWotdROjbfqRQCTOs2O6yAZxKH2mWKj8pkB-CdxEbA5t45-OkFrCh3TpNjMa83RQuaa1HK-8v658JO4zd8BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff1e3182e6.mp4?token=EHajlRnrCqS-86phKRJ6y70BfXdowIxB-5MnOJb7-WvpycppOGTskwmac8EN8vmnIcyKKmrNWORS6aPENHXnaAuqIZKPx0AQFnhZW2z99fHdYYF8lK1AP8Li0iWodHxr52KBQ-o1KvwlNeHjml2cBeJ-lpZjOxepjNzA-lc0F2qEjQ6BT7OnXnhB9kQCQ5ak48uPlSMSVyUpuu1ctlw0IbYZEkfMGhrypXu8wimASG7HxkGtv5TLZ_LG-Mp7ptN1Z5yWotdROjbfqRQCTOs2O6yAZxKH2mWKj8pkB-CdxEbA5t45-OkFrCh3TpNjMa83RQuaa1HK-8v658JO4zd8BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع سیلاب شدید در هند
🔹
بارش شدید باران امروز در شهر ایدار، واقع در منطقه سابارکانتا در ایالت گجرات هند، موجب جاری شدن سیلابی قدرتمند شد و خسارت‌های فراوانی به اموال مردم وارد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/akhbarefori/677510" target="_blank">📅 23:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677509">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
وقوع انفجار مهیب در جنوب لبنان
🔹
منابع خبری گزارش دادند این انفجار در «شهرک کونین» رخ داده است، و هنوز علت این انفجار مشخص نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/akhbarefori/677509" target="_blank">📅 23:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677508">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0cf2384e8.mp4?token=JiZ_aZkfyJ-_3C-brg2JH7hRECTLG4qIJ4rTOYEn6qF89Tavhi41dCSVJCmV80JHGffynY77mBSl-OJ-1AnI3wA6CayaQviI_Ckmjxot7MyDIsbOjRExcMEfm_aw2Yq3uCkXPpieLXqMvVtpMbeaJq0k48yjGLCFO0N2zhRskPcH8QU5NBIm3dc0C7Q1MrbJe6o6aWDPjo3PnWneq_WI9slA_YcW41ONAQMVak5RPEu8VaNPywG_wuyjX7vw2LwkE81wkdKxskLp5TK4eDurxRcOXKcoW_kvDzKt0yKBNAo4LoSCbtKrSBIZMkBx8Szrm5fIpSw_3-d5YRmwG1-FaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0cf2384e8.mp4?token=JiZ_aZkfyJ-_3C-brg2JH7hRECTLG4qIJ4rTOYEn6qF89Tavhi41dCSVJCmV80JHGffynY77mBSl-OJ-1AnI3wA6CayaQviI_Ckmjxot7MyDIsbOjRExcMEfm_aw2Yq3uCkXPpieLXqMvVtpMbeaJq0k48yjGLCFO0N2zhRskPcH8QU5NBIm3dc0C7Q1MrbJe6o6aWDPjo3PnWneq_WI9slA_YcW41ONAQMVak5RPEu8VaNPywG_wuyjX7vw2LwkE81wkdKxskLp5TK4eDurxRcOXKcoW_kvDzKt0yKBNAo4LoSCbtKrSBIZMkBx8Szrm5fIpSw_3-d5YRmwG1-FaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متکی: یکی از استراتژی‌های آمریکایی‌ها این است که ما را تا آبان یا به مذاکره، یا این واسطه و آن واسطه، یا به حملات محدود و غیرمحدود، مشغول کنند تا به آنجا برسند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/akhbarefori/677508" target="_blank">📅 23:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677502">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m6WRgsqtZPsopiQ5I99oQGkrZzgx5zNOxjw4vp4o9dKRACk3bRcDjUxyhHgGwIVBXWpfh1moMtMifhxi1oK_xR5mBv9jaOek4lrb0H9MiooSp0O02qwXBPdNWvLRREZtVj0cHHm3IdTgtlpazGKUcvTXTztLn3qFbNgmDUepmwHphw3I645RBfx2-w7SVsTKgkNmHYJBpef3AS42uTkBLa7JzI6HMAeai3vR8uUogf1rk7FcBjE686PwJQPS7qi4N-RcBw7noK2YG2cOXKVmuOR3JyyDpjF5JBIUTm8fBGOqIhU1VSQn1ZYIUFEHMtumcQSxzDSkhcYLeTgydtq7uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L8A4zgwoNy2KHtAvgh89UedTvRRuZtH6AifW5-reGXoevI2bGJJImeO8aAhG1xYvOUvnbtIN-rdkOoxLJbUWaC9ddv6Lq9Ni998kQ-tPAa3Dp4dOxoKbbSwrrhxoWZ2n1WhulepzweYBxMJv3vKet24GgO1QwhdMNm7IGT0Gcx3VYVaPxS_EpvKa5bZ0t4XJbm5XQg1FYrcmi4D-Z4s6ejyLwlNAqHLUuGfbsIFxiij8KGZcG31zIRJRHYmd8DReLWpqVjRQC3b2my0BMVZaT4UhDH9lTfyYuL5NQtLY-scT3gYiqRJ1RAeC1Q2g0SFPQNAvXxm17cQQjh7jBi6kvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OgcfB7_ImMl-c8kHd2pO4eXNLsfLGTRaXqBDrYpzwMrcC851aAFpoKVdKG8PBtCIxpAPb4faO1wIWRkTM-ELWXxvDUz2v1OSRNFXQ4PHnAQSTVqGEe7i14TBNrpIMHHyB_GXIZF97z2ZMhgoDRLXrbti_bpgLQPQZfhYtSask8AD2i24mXcq5pV2TaiaHwKBI9pJKlYSje8myO4cJtsib8QHyau-PjQ8Py4tt0O8SUJ32bGXAWuD_dGW-C2AVd9VSMYX3XQ79z5lmQlbgPG0yR4DNRFHCubGEhHnyUkWWNxmJBxGoVmcWkni1P2pj401bL562sP_rOdFMLUjEExFYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tFeNnqT-fPBtX_i22H0_EQ_-DxQWmMk02AFRERNaDQs8-pR3FvYhw81rF5IX5dx3_PsrfkY2jQkZJVNEvf4kVgCaM80EHMe-rpMLT4CKlUsIeLvNlyzM0nSJcbKwOaYjdARoxQ7_Ux6x_5ZIgKM8jxnTGQtHnjZOGKOfpmOsySoGqt5BP1halfKtQENIzU471fBL4vWXJXGGf0p5bVEDlnh1g-6o_LZEfnVUo3MxUO_cODlUPPJwhqnQrC4VSzelwHVczaTTxJ7suX1UHKdvjy2Yy8XaQHy8wbyRiEL86n36slSceU9c7fI6c9Fpv4xg7y-MVljSwDD1A3KIvCpSnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iu8NSYiYfJgOj8M1meDaoHZRdoO6KgvgyAJI9XVW_GVhc_VmdZOsx6WqrW21zJE2lFkFbYIhuSSu3HEHvLWfY36cXhIikKRWQjDUERmlj_fvmwLf6Rymi1yADlPl2Omjehicw1AdIbqEYUjoiwekVuES8FEgshugjCYIQzE8JVWawX_fs_-kk_btO8IV71zchlFo5W6ff1Z6aF61ugpmSoHUfTaOkKfMS470fH1Q4vXlWmxOyBRUL40zR1UEk6wC9Jn_g9OASvVhoEHTZyQn02PplRpDlTDaFiEm1BzzsSobysrW__kNECc0q5C3gI6xWCH7aQYzlAYHrh6Zo8tz4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ONO9OikgMi3sPDugqT-BbyLOfZML-jhvc16RY_Uohy5BnyXtQzT8aVLfUF84aAchfZjQjSE7ZU8yGngOYh5MZLOlS1bjIpVpnekuPgoatAXr9XKzNGdAkhue8D0Trurp6hRssi2tZliXMwf8bYtY8uOCqRfLkHGkvAn6YCKMauBZr4ShHvDAdZg-8rNIVi26fZnURDGKzwkA6jEndxvkqhN2bs5LaKgPPhjJhb2_oAKhh5YNWN3zMfE1rHBbtu0eSHqHGLHfopkyh6q0jeV4uIaIiLmCryRKhVMO2N6R7RQfkcaJvNbkOFTs0lk5u23PHs1L4mEkWNaxpwDcv16taQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
این آمار اسرائیل را نگران کرد
🔹
اسرائیل برای ترمیم وجهه خود دست به کار شد و ۵۰ میلیون دلار بودجه رسانه‌ای در نظر گرفت. چون داده‌ها در آمریکا روایتی ترسناک را برای آنها ترسیم می‌کند.
🔹
اما چه شد اسرائیل تا این حد نگران شده؟ در این اسلایدها ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/677502" target="_blank">📅 23:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677501">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/331b6210f7.mp4?token=px-rRlBLFz6fHj1y2EIAGp0Tq2ZiuW_jaSLLcUFdbuWvsXBNTMB91XHM9zuxEsnvj6HoT1frC9dI53irIuqKTdGlKxWf4_90NxEj8-z2qHZmn7xQLcnZtfNPSQTch4LTYHaDqNSFxgXM1u4Y2o0WO3Dmix4fPWi4fyPgh1EEH2dKwPvHg9LcORPcMvZJSgZMIAwoh9mDx7c1zBUFGeuYFuLxSPGBP7eiRpG2p1ab-AWVlEZ_9VK_NB2R5T4tGuBo3LEuo7NrGRWGpgOB3HgFVIz6bNOodunMR1MZzrYnayskSmFUv2YjpZgUKGjUTHQoPrdNc3VZKlug-W3fc7y5_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/331b6210f7.mp4?token=px-rRlBLFz6fHj1y2EIAGp0Tq2ZiuW_jaSLLcUFdbuWvsXBNTMB91XHM9zuxEsnvj6HoT1frC9dI53irIuqKTdGlKxWf4_90NxEj8-z2qHZmn7xQLcnZtfNPSQTch4LTYHaDqNSFxgXM1u4Y2o0WO3Dmix4fPWi4fyPgh1EEH2dKwPvHg9LcORPcMvZJSgZMIAwoh9mDx7c1zBUFGeuYFuLxSPGBP7eiRpG2p1ab-AWVlEZ_9VK_NB2R5T4tGuBo3LEuo7NrGRWGpgOB3HgFVIz6bNOodunMR1MZzrYnayskSmFUv2YjpZgUKGjUTHQoPrdNc3VZKlug-W3fc7y5_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رکورد عجیب محبوبیت این پست در اینستاگرام طی ۲۴ ساعت اخیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/677501" target="_blank">📅 23:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677500">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/020f55f6c3.mp4?token=mGwe9GrFAd_5pfQ0NHCxKbRQ9l5elNiRi3srezxaRYhqk8Nky4bu6QkD8OiRih61QfRQ_rtOOsH0SjORCj6o1_zqtnLa9NoVvt4pfBKBhMJRMsevTgojE2cM9o7wtYb1RQNRAIC1z150PetwVYRcOLhNaKPYXZmS0GTLT9_AD9vwYvuf368s_GgxrZ_x2UWroCyvgvXlNJDp3uGqmErQ9exzs6hm0V9n7Nh71xNKMGnhQjpX8YlCiN0y-TP6QfVcblxqyEhHJ8ct0DUZzr9NO_pGeGvCcWespuK7eY-wC5wC_qrc3ljJaQHiTKAuT18CvQarE0SA6z-tFuPGRF8BYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/020f55f6c3.mp4?token=mGwe9GrFAd_5pfQ0NHCxKbRQ9l5elNiRi3srezxaRYhqk8Nky4bu6QkD8OiRih61QfRQ_rtOOsH0SjORCj6o1_zqtnLa9NoVvt4pfBKBhMJRMsevTgojE2cM9o7wtYb1RQNRAIC1z150PetwVYRcOLhNaKPYXZmS0GTLT9_AD9vwYvuf368s_GgxrZ_x2UWroCyvgvXlNJDp3uGqmErQ9exzs6hm0V9n7Nh71xNKMGnhQjpX8YlCiN0y-TP6QfVcblxqyEhHJ8ct0DUZzr9NO_pGeGvCcWespuK7eY-wC5wC_qrc3ljJaQHiTKAuT18CvQarE0SA6z-tFuPGRF8BYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرچم سرخ یالثارات الحسین در طریق العلما به یاد آقای شهید و طلب انتقام در مشایه اربعین حسینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/677500" target="_blank">📅 23:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677498">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61d35fedd0.mp4?token=rLcI9mNvAmyA012thl27BYSmaF6Ljz9DbC3k7n8P6a2z8h_mLXUocV-WUFv9oxiFYCGX6KsONVM3VaBe3TMyIYdhXx1GVqhfWLRJBToJSe8FpIvBNZ4xSA0AxlHnAZDdouOMHO9klJuAraoF8TBm41HL8tr2Nb5eaxDAbrpbIrmrSqa5VwkTCYNLh3exOuWuIEcZPudYnHhz8jJ2wGNtsEXbrtJqrIhEfYiNkMLCUMTkLIArE2KO64NSyv_O47X3gtKkSLrqUFTYZVkd9HICvjQTmMY8eLEefaeFNiDb_o860YXGGTc055JpjNfm2Wr6S1zjWgNbDmIhUHNyHJufcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61d35fedd0.mp4?token=rLcI9mNvAmyA012thl27BYSmaF6Ljz9DbC3k7n8P6a2z8h_mLXUocV-WUFv9oxiFYCGX6KsONVM3VaBe3TMyIYdhXx1GVqhfWLRJBToJSe8FpIvBNZ4xSA0AxlHnAZDdouOMHO9klJuAraoF8TBm41HL8tr2Nb5eaxDAbrpbIrmrSqa5VwkTCYNLh3exOuWuIEcZPudYnHhz8jJ2wGNtsEXbrtJqrIhEfYiNkMLCUMTkLIArE2KO64NSyv_O47X3gtKkSLrqUFTYZVkd9HICvjQTmMY8eLEefaeFNiDb_o860YXGGTc055JpjNfm2Wr6S1zjWgNbDmIhUHNyHJufcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس عراقی: انتقال تسلیحات از سوریه به عراق توسط آمریکا و با هدف حمایت از گروه‌های تجزیه‌طلب در اقلیم کردستان عراق انجام گرفته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/677498" target="_blank">📅 23:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677497">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
بازنده و برنده بازارها بعد از جنگ؛ کدام بازار در معرض ریزش است؟
🔹
بررسی روند بازارها نشان می‌دهد مسکن، بورس و سپس دلار پس از جنگ بیشترین رشد را تجربه کرده‌اند. طلا به دلیل افت قیمت‌های جهانی از این رقابت عقب مانده است. مسکن اکنون بیشترین ریسک اصلاح قیمت را دارد، زیرا رشد آن از تورم پیشی گرفته است.
🔹
بورس با وجود جهش اخیر، هنوز از تورم عقب‌تر است و کمترین ریسک تعدیل انتظارات تورمی را دارد. همچنین دلار و طلا در بلندمدت تقریباً همگام با تورم حرکت کرده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/677497" target="_blank">📅 22:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677496">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c39243dd5.mp4?token=ZrVxzNj2b8UBKbModyJ9r88a_8YFdexzHfbbqKugaMFh6l7evkkv71VAWY5ziITbJTOayq7bsz1OIj6PwBsFFTYWMvVvDSVbjNF-keefL2QU7sJRHurm5EAnz8FErRw3Tma5A7XN3E2LEoVHKoWz30bNP6F6FlokWCa8fXsljwjZtJfsPsceh2XmfiM0Ho5zskXVeptjLBQGwLidggEXb2SkZRPpXCdshbao35pGJGDX8Dg7Fhgdh95uopJlOldmhVnXs7aDnpNjCEAZFMtnvtUCe5ri41RrTWgl2lVPDTtQ67NZMbgSxg0Iapus2eQO27O9kUv1ZrklPmVUTaRM6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c39243dd5.mp4?token=ZrVxzNj2b8UBKbModyJ9r88a_8YFdexzHfbbqKugaMFh6l7evkkv71VAWY5ziITbJTOayq7bsz1OIj6PwBsFFTYWMvVvDSVbjNF-keefL2QU7sJRHurm5EAnz8FErRw3Tma5A7XN3E2LEoVHKoWz30bNP6F6FlokWCa8fXsljwjZtJfsPsceh2XmfiM0Ho5zskXVeptjLBQGwLidggEXb2SkZRPpXCdshbao35pGJGDX8Dg7Fhgdh95uopJlOldmhVnXs7aDnpNjCEAZFMtnvtUCe5ri41RrTWgl2lVPDTtQ67NZMbgSxg0Iapus2eQO27O9kUv1ZrklPmVUTaRM6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گفتگوی عربی رهبر شهید انقلاب با پسر شهید اسماعیل هنیه: بلِّغوا تعزيتي إلى جميعِ عائلته (تسلیت من را به همه خانواده ابلاغ کنید)...
🔹
پس از پایان اقامه نماز بر پیکر رهبر شجاع فلسطینی شهید اسماعیل هنیه در دانشگاه تهران. ۱۴۰۳/۵/۱۱
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/677496" target="_blank">📅 22:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677495">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54dc382f4d.mp4?token=RDUlkibWZx7HHTVIoevzyPUKM7uxoe_Z3ckPTnFFl0BVOxT_5oXpNFIZOOjSuIw2KsPJg_dbkDtUMnmIMVylAbxhIBi_NQgfxl1RfWXTkrlxs0m_iRrceUQL1gLmeFgtLt-mWrce6gBID_a7hM5nrYZaLqY09UtcM03g0RUwZ3mclF7tTpUw2g6QhKZw8eM4rlX0hvaQRqpEd9qFN5y-oA0A98QnjMK4-O_v-Ah9eS2cnfQTC22aJUkctSrcGgGhncwPcjEL8iSgqy_9jJ9KlcoWgfQ2w6aJ7lhu4sZaYucJoA9lstCHvLJVOKblg0QXxRxuck5QJEcj3FNwK_NVtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54dc382f4d.mp4?token=RDUlkibWZx7HHTVIoevzyPUKM7uxoe_Z3ckPTnFFl0BVOxT_5oXpNFIZOOjSuIw2KsPJg_dbkDtUMnmIMVylAbxhIBi_NQgfxl1RfWXTkrlxs0m_iRrceUQL1gLmeFgtLt-mWrce6gBID_a7hM5nrYZaLqY09UtcM03g0RUwZ3mclF7tTpUw2g6QhKZw8eM4rlX0hvaQRqpEd9qFN5y-oA0A98QnjMK4-O_v-Ah9eS2cnfQTC22aJUkctSrcGgGhncwPcjEL8iSgqy_9jJ9KlcoWgfQ2w6aJ7lhu4sZaYucJoA9lstCHvLJVOKblg0QXxRxuck5QJEcj3FNwK_NVtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز اجرای آزمایشی استفاده از کارت بانکی برای سوختگیری
معاون سیاست‌گذاری اقتصادی وزارت اقتصاد:
🔹
طرح انتقال یارانه سوخت به کارت بانکی، وارد مرحله اجرا شده و به تدریج در سراسر کشور گسترش می‌یابد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/677495" target="_blank">📅 22:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677494">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a6ae2e69.mp4?token=X4_dhEhzn0LA0TGFhYdX1vso-zaWE5eYfcLq-49pL7LkqrugGbSx62m1lBHXZX6TdCWAIuls7NE40BkCSiv9hAl-dJ1OrhLcLLREn7d0KZXccPPGsbc_j5kbYPzYudIhwPhplQIl4NOcjrdnT3Vq8kdEPAXIzw294z0eWaoEN3dFhwqZS85fdwHb3O0QAavr_mMidNkJshUZPcLG4Sw6AmTV13jM4F6Mk_ViYyLbD2A3nJeHEUj9GN8TuybRl8Cy0hzxtbonipRGXVnQQgnfDJZNSlZfJLDMspL84F08hHtSSK1kobcp1X96_7nTJuY1G4op-nUWd3cJhLLz6xS4Wxb6t4hbSc3LJv9DCelvtJ1I_K9HbMaiX7Kay7GwL96TzVD4-mstpkQS0B6SjbEwFFw5qlz8wAH-KmSSY3ZdOfCFSDUbNBruyIxDlflS4P79OI4FYL-NLezIKIXPqwNb5o3zfdOaLgSVgb4EcuK1_yUwrAKlE2NumHAr8E8M1ittu_XG15EwzNJkDWOPcgz97utS0qw-IdVzBXNzOfJNYKAqHIKU5fRppDfocNBZ-EVfNtvFATKUU6hS_N7XZeA0HMilGJvMYdy_pNzkP0Tva8TOu1Ho8-pMJcYiiDfDNFuQRJBfcsatJ5f-vBL58tnOBukTpXb-vl1zN2PzzAgXJr8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a6ae2e69.mp4?token=X4_dhEhzn0LA0TGFhYdX1vso-zaWE5eYfcLq-49pL7LkqrugGbSx62m1lBHXZX6TdCWAIuls7NE40BkCSiv9hAl-dJ1OrhLcLLREn7d0KZXccPPGsbc_j5kbYPzYudIhwPhplQIl4NOcjrdnT3Vq8kdEPAXIzw294z0eWaoEN3dFhwqZS85fdwHb3O0QAavr_mMidNkJshUZPcLG4Sw6AmTV13jM4F6Mk_ViYyLbD2A3nJeHEUj9GN8TuybRl8Cy0hzxtbonipRGXVnQQgnfDJZNSlZfJLDMspL84F08hHtSSK1kobcp1X96_7nTJuY1G4op-nUWd3cJhLLz6xS4Wxb6t4hbSc3LJv9DCelvtJ1I_K9HbMaiX7Kay7GwL96TzVD4-mstpkQS0B6SjbEwFFw5qlz8wAH-KmSSY3ZdOfCFSDUbNBruyIxDlflS4P79OI4FYL-NLezIKIXPqwNb5o3zfdOaLgSVgb4EcuK1_yUwrAKlE2NumHAr8E8M1ittu_XG15EwzNJkDWOPcgz97utS0qw-IdVzBXNzOfJNYKAqHIKU5fRppDfocNBZ-EVfNtvFATKUU6hS_N7XZeA0HMilGJvMYdy_pNzkP0Tva8TOu1Ho8-pMJcYiiDfDNFuQRJBfcsatJ5f-vBL58tnOBukTpXb-vl1zN2PzzAgXJr8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متکی: هیچ مذاکره‌ای تاکنون صورت نگرفته است، مگر اینکه اذن ولی در آن باشد
🔹
ما باید مذاکره با آمریکا را مشروط کنیم به اینکه ۴ گام عملی را بردارد، پیغام‌ها کارساز نیست و شبهه طرف مقابل را بیشتر می‌کند.
🔹
قطر باید خود را بدهکار حس کند.
🔹
آمریکا بدنبال ایجاد بازی‌ها متفاوت است تا ما مشغول آن شویم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/677494" target="_blank">📅 22:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677493">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
حمله پهپادی به اطراف منطقه دوکان در سلیمانیه
یک منبع محلی:
🔹
دو فروند پهپاد اطراف روستای گیچینه در توابع شهرستان دوکان در استان سلیمانیه عراق را هدف قرار دادند. این حمله منجر به وقوع آتش سوزی گسترده در منطقه شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/677493" target="_blank">📅 22:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677492">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uG297vyHFpIzN6fXqTzjtZaY0TxE5xlqamJ_kD6hC1DbdhCoQnWRXNV5MOK2nFNig-zO7bkXASo8EVCFyx29KSgsup1RBAJxG-haQE-4jbeeyZSjv8hO4RDs9KZaueK-6291Zs4m3L8SVZZ_geas4V9P4oF2Zvxb0bIO0z40T7YbltLyHbHr_1rdt5PQVa0zLSl5PK0cCzlgMfy7SLtyEUpgpuA6Zc3uGjJm8lVmxE0jutf0KVzK48wyr-OzMB36EFcXby8gl09du71u3MWeFXgTIIwtvnBM3-qNuhlNI6rfQ93XAqeFccbau-r7yMtz6dxBHgcJVHykeh95bbUdyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واتساپ قابلیت تماس صوتی و تصویری را به نسخه وب اضافه کرد
🔹
از این پس کاربران می‌توانند مستقیماً از طریق مرورگر و بدون نصب برنامه، تماس‌های فردی و گروهی برقرار کنند.
🔹
متا همچنین امکاناتی مانند انتقال تماس بین دستگاه‌ها، اتاق انتظار، حذف نویز پس‌زمینه، کیفیت بالاتر ویدئو (QuickHD)، اشتراک‌گذاری صفحه و واکنش حین تماس را نیز ارائه کرده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/677492" target="_blank">📅 22:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677491">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d147c1534.mp4?token=I1l4Fdye8id-H9hrKNTeu6ZXp8Hg0s0-KVCs68yZVL9Utj6_VQtA0EqPQJbyN1WUMwRtbk0xcMaJwzd0ytRzyof8C2FOIsp-_PAM2cUmsdd0ujI621cUDAr_6fCAf4GW7iKa6QO1fBNKxCQkma52BL6VDDAj6wyAFt6-5pRq72wsksV31FSICg-KxdHvS72c7-TWcJOzu4KpKKvnBXOMxa-DpJXxCy3olNZlt6wBo8xVFC_AMmHRY7_HUKOROX-KIeIj5cYC-k1aorHPaDhkvnva5Ry0j_eIDj0ADAnU_T4VimF7PSJPYlVIULlDajX-KP0rQxIDp1Vy3tTsoo-fpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d147c1534.mp4?token=I1l4Fdye8id-H9hrKNTeu6ZXp8Hg0s0-KVCs68yZVL9Utj6_VQtA0EqPQJbyN1WUMwRtbk0xcMaJwzd0ytRzyof8C2FOIsp-_PAM2cUmsdd0ujI621cUDAr_6fCAf4GW7iKa6QO1fBNKxCQkma52BL6VDDAj6wyAFt6-5pRq72wsksV31FSICg-KxdHvS72c7-TWcJOzu4KpKKvnBXOMxa-DpJXxCy3olNZlt6wBo8xVFC_AMmHRY7_HUKOROX-KIeIj5cYC-k1aorHPaDhkvnva5Ry0j_eIDj0ADAnU_T4VimF7PSJPYlVIULlDajX-KP0rQxIDp1Vy3tTsoo-fpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار «مرگ بر آمریکا» در مسیر کربلا هم از زبان مردم نمی‌افتد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/677491" target="_blank">📅 22:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677490">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‌
♦️
وزارت خارجه: دولت‌های منطقه وظیفۀ قانونی، دینی و اخلاقی دارند که از استفاده آمریکا و رژیم صهیونیستی از قلمرو و امکانات خود برای حمله به ایران جلوگیری کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/677490" target="_blank">📅 22:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677489">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hylnnnebjOr807EKgJDyWTu2Issf3fZtgNx6trO7B417qCwbc2wkVr_BD6Eq1w7w5pC8BQ75X25kgppk7enOzoq7hrozPfHz14PJxff6QL6BXuwrZCVOq4Ulp6szovwBZDvarJA9Q9EKcL2tuvRucNoIGeLPHCf-pGyOv3KYgqDJ1SLd5yS_XqtZV1ZsoS-2nSJ9coZzYW_SwD68JoYtmt-Sqqyve46N_LQOP_DQKdPwV4FPvVIXnjlSx9FboWHKXlEmy_itUTe5HZS695gNV_SCvFw0emNob_auMb1Od0VB1AZ1dj4Hk-CPcBQQFUyAhoBTKroKlL5j9JA4U-iRKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هدف از حملات احتمالی آمریکا به ایران چیست؟ / مدل جنگ عراق تکرار می‌شود؟
🔹
رسانه‌های غربی درحالی خبر از حمله قریب‌الوقوع الوقوع آمریکا به ایران می‌دهند که درباره اهداف حمله احتمالی اختلاف نظرهایی وجود دارد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3234815</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/677489" target="_blank">📅 22:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677488">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‌
♦️
وزارت خارجه: ضربات دفاعی ایران به مبدأ حملات غیرقانونی آمریکا، به‌هیچ‌عنوان حمله به کشورهای منطقه محسوب نمی‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/677488" target="_blank">📅 22:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677487">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJvPuh1a_iDxqPIlYYTwRSXwzYtHpm6HXNJ2lFvJCqe4X0zwpJeopHlBfAdf1rAzXJksb-VogwtGrPua3V_5ZgiAfucwaOMbQOu3acIc2iJOphL7vw_BeAyybrefKNCMnxI3uv3w54M3L6A80PxGInGoQ1JAIobCUF0Ge1NYt0eaRowY73qXz_63Q7kjRj0BKZ-Ca7q4sBrPwGMVXTNAS1_s9LeeO2IQ3Yr8I9y3f_c3yUwnjbFDu405YQwVF5O3y4tRPWnt4tPGTCBXGAQOtOTCNKcScEev86izvMxpIynVjcIahPVAYvtdevgMjxy2hebZ59zCN_U9zAmgAUPaeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزارت خارجه: تداوم محاصرۀ دریایی و حملات به اهداف نظامی، غیرنظامی و زیرساخت‌های ایران، مصداق «عمل تجاوزکارانه» و نقض منشور سازمان ملل است و ایران از حق دفاع مشروع خود استفاده خواهد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/677487" target="_blank">📅 22:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677486">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‌
♦️
وزارت خارجه: ضربات دفاعی ایران به مبدأ حملات غیرقانونی آمریکا، به‌هیچ‌عنوان حمله به کشورهای منطقه محسوب نمی‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/677486" target="_blank">📅 22:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677484">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45a52f306e.mp4?token=Pfk75FCXW-OZfEvU815qZWRA_eas6FntaK4b7DyWu0o2p-SejmJs9G08GPdAd6sk1zMxiUponXNfgBshpZf_rYF-jrTZKFEc8o7YfSd17c_47yYIX5Kq3hLC5TfS9XnGIRwJZo1KZlFDFUx7xMUU1wIxOPvt5380TEKje2lHxnPq9UDot9tvUNSY0a72dsUuXL2hZdWw4XWlO7b9X5pvaqIs2fjthcwGL1mLhDpESWAtzOhX3zQJheXJIzubKWBttcEQcQ1M4H4S47mLmxwj3qdscjwQadw92fcO9S5ClBI-__hHkFnmg0j_-unpRH-FEwjVjSi3efqRnXkVgs6QLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45a52f306e.mp4?token=Pfk75FCXW-OZfEvU815qZWRA_eas6FntaK4b7DyWu0o2p-SejmJs9G08GPdAd6sk1zMxiUponXNfgBshpZf_rYF-jrTZKFEc8o7YfSd17c_47yYIX5Kq3hLC5TfS9XnGIRwJZo1KZlFDFUx7xMUU1wIxOPvt5380TEKje2lHxnPq9UDot9tvUNSY0a72dsUuXL2hZdWw4XWlO7b9X5pvaqIs2fjthcwGL1mLhDpESWAtzOhX3zQJheXJIzubKWBttcEQcQ1M4H4S47mLmxwj3qdscjwQadw92fcO9S5ClBI-__hHkFnmg0j_-unpRH-FEwjVjSi3efqRnXkVgs6QLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع عربی از آتش‌سوزی گسترده در سلیمانیه عراق خبر می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/677484" target="_blank">📅 22:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677483">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMIPH0gtmT1x55Jl5Xk4QPDNz7F4t1h0OuMzJ74hSOOKF5YzYqRwr9hfnAnUqM-MYOHJd3AlVYpZkN-RqRxI6HTPj5OUdlgZ4gkRJurSVUELVOpXqXvZhHVlVKaqKHDYOLpx9Vw3guKrrJdWK4aoOpr7v-VyZ_6cbUwrqJqQY24eO5A1XPKwTR_mF6ArU3oDh-BgYWBBvPjZca8CPN0g8cUi2gtSaAXRNvYvgMjTVqLyEq39BSMVKqjQmaTlQvrSCFLe1NI2GHlBRmLrYTMuZlwZGrO8UHzWnuv-scQgqmtKabID7HTwPm6lZC_AG02tMjUY8Qnyl2lUDlHJq8827w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۵
نشانه هشداردهنده کمبود اکسیژن در خون
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/677483" target="_blank">📅 22:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677482">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
تصادف، یک کما و ادعایی متفاوت از آنچه پس از مرگ دیده شد
🔹
00:07:20 ناشکری کردن و راضی شدن به مرگ در هنگام داشتن یک زندگی خوب
🔹
00:20:00 خوشحالی شدید و عجیب با جدایی روح از جسم
🔹
00:34:20 صحت‌سنجی بی سابقه‌ترین رؤیت، در تجربه نزدیک به مرگ از داخل سقف بیمارستان
🔹
00:58:57 کشیده شدن به سمت پایین و بسته شدن روی یک تخته سنگ
🔹
01:08:25 پاسخ خداوند به شکوه و شکایت من در مورد دوره آفرینش‌ام
🔹
01:12:50 درک شرایط زندگی در دوران حضرت بنیامین
🔹
01:21:40 تجربه درک بالاترین عذاب الهی
🔹
قسمت هجدهم (درون سقف‌ها)، فصل پنجم
🔹
#تجربه‌گر
: حامد البرزیان
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/677482" target="_blank">📅 22:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677481">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPS2IkctXlxqVgMeJEpHfxYKKG2ps-nMlYWv4mWoY3oVjSpGakUNK6oDmH-xDBvg42JausU23Qw_5XOkM3OmkhhyxpMAzjIFgaxlp2_mI38nlGt53Y0fDe1xhi3M_f4qnUCURlYW-7SXvbCZHi1Uxv6jtXskwFRxn4YVfxgVVi9j_FLGbeFQ55UURCh9-KjdU29J17tGUuEYwnDBXpXMW_09SiP3uV63X7Dbu3XU2Dm-WKbgHbzWIBGhYKRtlwC_NWAZbu-pvlUCKdddaZo0jqh56hwWUoRISwlXzMo3nh1G65RtHVL_FNbvv0LuoOSuV4MVc6StJZDQBf0Mjkn3Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادامه توئیت‌های عجیب خوک زرد؛ این بار در لباس الویس پریسلی!
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/677481" target="_blank">📅 22:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677479">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cODH2uXFUa85qn9mgwtqK78LcmKd8FjhKBH3Mm5QtHI064Cr2PJdkJtQJHxoL8DE-WyZTFQQALWoBFczftIcq8OTZfCWqySFcmm-g-yN8-d9kUIjo8iaipU8xji2Ve_XCMsB31UtaOhVFTG0RTGVeAwizjsJn8ED_3e7mGD6etN6p7YFgDJ4AuX57L_hMMGxyd_OfMWGVeYZmzZQP5L2CniYaf9Jb4_XpjWJZO9qbvn8P93nd2fM4GL2w8DIYnKFE1iCM8VuRMrwla_zxCNU6Qv2aZxSlj4N4V5MfFoOiMrnhGhAcNxbyMTvbMy3b7jYsciBOXnREYQ0yJAnuhOOgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رضایی عضو کمیسیون امنیت ملی مجلس: پاسخ به حمله احتمالی دشمن محدود به منطقه خلیج فارس نخواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/677479" target="_blank">📅 22:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677478">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2Dx9tmcor6A3paLN-b_UfcHySc5dsxJvlb3UooxheO-srYxOTK6TsEQlue8_1rKiuM6-ZPTbiPL3r7v8xtuNOyq52xzlCZzaPsBsYT3GLq8l4ph0DsIW7Lvy8VQlEyLp5Xrdqwp9bBs0JuOsgR1H3Hyi9yyGdyfif5URR97qxwJRvkeAchATNIh4wdnh8gX-7oKmG8_XgQXFss9vbSCVlGGtb_19NOMZYTsFq0hvLTRlntqNjc_srYiW0G2BxIBRvvw0Wm7ahKHGFruvZW59-wLp_M-OcCONHglk2_TWjKHLYWv3mpAbFwEmqK79KVRXxyWADZ4NTxuAzTbrh5IuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش جنجالی رونالدو به لقب «مشهورترین ورزشکار تاریخ»: فقط یک کلمه، «ساده‌ست»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/677478" target="_blank">📅 22:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677477">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❇️
کمک فوری/حال این 2 پسر نوجوان، زجر کشیده خوب نیست
🔹
پسری ست نوجوان، به دلیل بیماری شریان ریوی تحت درمان قرار دارد، تاکنون خانواده اش هر چه در توان داشته اند برای پیوند ریه پسرشان هزینه کرده اند، و چند سال است به کمک شما عزیزان داروهای ایشان تهیه میشود در حال حاضر ماهانه بیش از6 میلیون برای دارو نیاز دارد..حالش خوب نیست وچندماه است که نتوانسته اند دارو هارا تهیه کنند..
✍
متاسفانه پدر ایشان نیز به دلیل شکستگی پا نیاز به جراحی دارد که هزینه آن نیز بیش از 8 میلیون تومان است، شغل ایشان مسافر کشی بایک پیکان قدیمی است ولی با توجه به شرایط جسمانی توان کارکردن ندارد ،وضعیت مالی خوبی ندارند و به کمک احتیاج دارد.
🔹
مورد بعدی پسری ست نوجوان، به دلیل بیماری دیابت تحت درمان قرار دارد و ماهانه دارو مصرف می‌کند و نیاز به کمک مالی دارد.
✔
پرداخت انلاین خیریه نسیم وصال:
http://www.nasimevesal.ir/payment-new
شماره کارت بانک ملت : ۶۱۰۴۳۳۷۸۱۱۴۱۶۲۳۷
شماره حساب بانک ملت: ۵۸۹۸۷۷۱۴۶۵
شماره کارت بانک ملی: 6037997599156198
شماره حساب بانک ملی: 0219934010000
شماره شبا: IR310120020000005898771465</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/677477" target="_blank">📅 22:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677476">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4bvfyNH_VOzM7wlOJ_TAtPvNMSYw9n8DI0UiKD-mEaiLA7nYwBzbjUf6tPYIe56K2ZDZgKKre19W2wQXMjnI2RmYVLRC5oVA_1hb1E7GjMYDkqs7SCRb-b09ZGWSdCkwQNB39LRyXFGv1Bp0PKUOi8sVkax5z-Q66pZRYyZQ68HnkicRCXgxL6cE_VtOvF6Ps_7NI0JFDyB1dOzYEWeELOxW1ey6mIJxymMau438M1z1Mn2h9U7QjYoeJ-1ZrFrP_TbcPx92Ib13HIgFzy7uQOtH6yHdX7btfvPikMvvGLzMalUdWUrN3sO22Q7RTbuxm18sa2E-tSNsMg4wPlQ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
خادمی فقط در موکب نیست…
گاهی جمع کردن یک لیوان، مرتب کردن یک جای استراحت یا حفظ پاکیزگی مسیر، خودش یک قدم در راه خدمت به زائران است
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/677476" target="_blank">📅 22:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677471">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TctE_hKiTba70PP-Uy0p_RMQ38upoR8kxpRrKOrUOTtuHG13VTdhE9H_nRqzydFwRvEa8QvuDaulFDS0DmSFBKzv38vd_kXQv7M17GzDhT411eJxuP8gnE1N4anZ1OcrZdEX0ABz9JHltxrMvz1zlA8Z0kPLc8TvoD_OKlQbE9qAPAJXlHMZ7WSpKdQd2XcvPhEqiCQnxGr1JZ6f27zIEBAqBbKblDZ_oSvxKo6HgFr7IE5iyoHdER6PMl3eMYNMw7__h8GlrS0Ha6RN9gT8D9u7snGZVejNvMx8FBQBwE3ytIW3gIeLGzbxQZ5-JHVZyBo9C0dvrbi6YrcCZNWCYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cyBLBpcVUtYwyC5PMnCiwrgqzuAFEAzPNRNLP7qYWg2Rh8OzKJ2X2QIw7wQxWG4efQ6Vtk0zSWzHupE7q0Gh4nl4wDpbJNT45lh5nqiK6NulIYASfKPi5ouVpJupWp_W69AY_vl34ktoN2MGBarOQMG4RPYpvfNK2SjOSA5rIO3oZnBkXQsoEiC_q9rIsSi6hVSeiw-lVxteZLbNhT4raMOAcTGatekimut0PhgMSN3tKKGOC6YhWwzAHl9PlR2MR0xmKlJwRrtXGLEMUuEOvhXMOy076oD6dJK3IhDJr9MOpU_IAKqcrvp1fAkvhw6eZe1Cwct-v57ZzyU--MdW_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l7X1TKagMJQWAT1u3c0UyjmFNJDOuW4fpivsiiPkS36Kv8cXe9gvnK3yGO183U4yKv4zRzAibkgTj7LIxea_oQbCawwphiv3zzKS-FcELCrbFnItWYKwF6Oa617PW7o3ISPm1b14N613QdWIufnxmEIJhquqYIuBccsU9QLi5noqSgu_2kgJBQHXlL0L4Z3l4zbkBqCLt8RkJzgZRIZYcBOZmz6xbDbKZdPsxacziz7Twxbn0uzMmz_6VfTG-Dfy02ss5M5xUKuyRqRia9yacek_TU3ci3YnZtAW0KGaVL1DkA92W9hQyxFbkxvJZUZePYIxngOuh171srMiLpujpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LNPyo8gAsbTU6iQMOgk0QHLPyyIXcSxYruFrEwrjfNZ-Xu55xMDggl81in3N85mbh8taR16D5_4EUBUNGvxfu80BCDChfjVGyHt8MEQp8T0mTXjdtP8NRhCEJ6iCsoQC5oJHvvhEFXPYV7ZE_eol2QEQtDiPEytN5yTugG4HLL9NtPkTBUstyz179h11GJHmnEg0vPwUwnojHoSTsh2yxOMc7nABV5UDcLwobhaJF9gM13XEd2B939o9CdElLcPwuaOVgTAzBq-zH4oinEAgXQNPHLAIi6H-qjqcuBUN2CjW-_acA5IXQw4Eue5vUMVU153Wu4j2w4e9DN3_I-eKUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/taob1a14AG-k9SVKyPUGdQq61iGN2KdR38YwNttXqrmyWcjlBaJrjCfpBobkg1yZhic6GnqoT5FWzp7QCpt4IdG8F2OiiNA-8utiIDTm_VO-oVsdS_Kknh9875DVngZXqjWMaPXniJCCmC_0jHXvLqwlnm4rLBHffLHqZEAMzK2xmL2A0oFyi9ZVC87S8PIViGEJatFP3oEnsy90sQOkZgrLu7kYAIze1RWZ5PRO_lQ09Dv-twJk_GcUMnEPbscxTBXwqRgqiBW7D8HoPgeK9MyH9tj4wDitJdBPo12hBGnh0bpEhyYrZeRyFejYS9yiJJBZWqDzbCq-d_7n-ly09A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شیطان زرد در حال نشر جفنگیات
🔹
سگ زرد ظاهرا رد داده!
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/677471" target="_blank">📅 22:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677470">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
نیمی از خبرنگاران امنیت شغلی خود را «کم» می‌دانند
🔹
بر اساس گزارشی که مرکز پژوهش‌های مجلس به آن استناد کرده، بیش از ۵۶ درصد خبرنگاران امنیت شغلی خود را در سطح «کم» یا «خیلی کم» ارزیابی کرده‌اند.
🔹
حدود ۵۴ درصد از فعالان این حوزه، احتمال ترک شغل خبرنگاری را «زیاد» یا «بسیار زیاد» اعلام کرده‌اند و تنها ۳۳ درصد از آنها در صورت بازگشت به گذشته، با قطعیت دوباره این مسیر شغلی را انتخاب می‌کنند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/677470" target="_blank">📅 22:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677466">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/setm6t2zVoSHQ6holBNh6gYlc-mhAcam9-iMvELwftbCm4NZm2_81AAyUmKr01N5UgRNZTXq3WavXQSgN0XyJjHysCzw6C50milDMt0rYR4EfzEALyaGfvxXMjFH6Wic4ZR8G7INfUOPcg5IU414EuaG2Oti4dYZXia5IkiPDq1uKkmAlyI-AMi2upA3DsziEjIXwfOCWPKq3YV7ZzuDGFF4oEfXMpmfzyspGXQHKAQ2pq6ETs5cDicWY59qTUSBlEUTMRz6qXZLVK-g9SJ56hVrivty1q-jabvI3--68-bebkOgowNc98a_lsRINX-OU5KNtDXVmjJrIOOLqZwUew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
علی قلهکی: زیرساخت در برابر زیرساخت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/677466" target="_blank">📅 22:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677465">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40c57ff11e.mp4?token=ilbk1Lwh5mcLV-JCRkxw-0LSv3lx9hOcoGdbEW3O757OTZfwJ0ssZwXFrguTvpxDzbf69sdeMV8Ck9bc1ciC-w1rqVTJFAhOQqE9v84SdeTqAsLIJBjuiKfW6TXQmLbliN2Pr_qSIhubQTp8i--MmAA98VymcL9fUG4ZzQJx7LZ0IaH9kVX-hbN3bQWJgbghJ3yF5YFBgOB-I-YYKI2BKKqHv9ONlZdfjRYFM1GD9hzJmDknKzNB0aofoONFWzR7s8jCHFdPNR-JZgzop3CrPYZUhOsktqAa7t3R-AH1fgV2ZubQI0UVeQEFC89v5IrPc1-OVsLTCuFWE7fD64oS-JAIxFhF8Ipqm7pnjy26mZsnEsv3TQu4oSMlnLzRr-hTvzrzWXmz4wR9u_JmilLCQHFP98rhbRNrDU7zXuRECmPnmnfbJ7qYcOEeyQ4W_nA5Q_rYgT0gifLz1eOUkebS3SSYq0rvpEqo7R1KE5zeTVNkMGjPF0bZw7NUZj3o4MIbvzUujiACYyE73G9wMmi6CWySWOWxBcY5xc_mOQes1b3Go7Y0rfgXL79t9p8RnfwYy_nkkO8k9WFyqXvJn7zBNJzIc75Ok3bx_q_WArSpjK5AFvTLp4MwC5SH0t5X9h16jE0lB2lRfIbmbHGLbjv5zciiLt-2noR1R__1eT8ISuI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40c57ff11e.mp4?token=ilbk1Lwh5mcLV-JCRkxw-0LSv3lx9hOcoGdbEW3O757OTZfwJ0ssZwXFrguTvpxDzbf69sdeMV8Ck9bc1ciC-w1rqVTJFAhOQqE9v84SdeTqAsLIJBjuiKfW6TXQmLbliN2Pr_qSIhubQTp8i--MmAA98VymcL9fUG4ZzQJx7LZ0IaH9kVX-hbN3bQWJgbghJ3yF5YFBgOB-I-YYKI2BKKqHv9ONlZdfjRYFM1GD9hzJmDknKzNB0aofoONFWzR7s8jCHFdPNR-JZgzop3CrPYZUhOsktqAa7t3R-AH1fgV2ZubQI0UVeQEFC89v5IrPc1-OVsLTCuFWE7fD64oS-JAIxFhF8Ipqm7pnjy26mZsnEsv3TQu4oSMlnLzRr-hTvzrzWXmz4wR9u_JmilLCQHFP98rhbRNrDU7zXuRECmPnmnfbJ7qYcOEeyQ4W_nA5Q_rYgT0gifLz1eOUkebS3SSYq0rvpEqo7R1KE5zeTVNkMGjPF0bZw7NUZj3o4MIbvzUujiACYyE73G9wMmi6CWySWOWxBcY5xc_mOQes1b3Go7Y0rfgXL79t9p8RnfwYy_nkkO8k9WFyqXvJn7zBNJzIc75Ok3bx_q_WArSpjK5AFvTLp4MwC5SH0t5X9h16jE0lB2lRfIbmbHGLbjv5zciiLt-2noR1R__1eT8ISuI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گاردریل، سپر نجات؛ پایان خوش یک تصادف هولناک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/677465" target="_blank">📅 22:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677463">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6553e33e7.mp4?token=nxyuQ1OXf2_hu1gd92WdOFpFHrHqJKLD0JTl1Gxh4Jsmsw_pBrQOJqrcJvkP4v3QweVQjznSJGh8h6BwO47NIUi3w_Eb_TKU75u7K0IZkUj_B6X90FBcBk2YJP-mEZfu1GY0n5SfxSlcNZHrtGnEpWuf4iFb6QdiWsKrKzeXXvliHkmFFoulX87SOjRvDW4TPQLgGlHIAnmVCM1uWx2bt0Gk3vaJTzymmKiVz6mM0IQVwv0GrHwA4_ZPCO97Kb0b-atCiQZKKifCrG2kpdw7dcXdeuoxQwZEmabbJ3bbUN3fDF0e6zq9dtH6T-shGuHv0iQYRjq8kbioInPhzVyIUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6553e33e7.mp4?token=nxyuQ1OXf2_hu1gd92WdOFpFHrHqJKLD0JTl1Gxh4Jsmsw_pBrQOJqrcJvkP4v3QweVQjznSJGh8h6BwO47NIUi3w_Eb_TKU75u7K0IZkUj_B6X90FBcBk2YJP-mEZfu1GY0n5SfxSlcNZHrtGnEpWuf4iFb6QdiWsKrKzeXXvliHkmFFoulX87SOjRvDW4TPQLgGlHIAnmVCM1uWx2bt0Gk3vaJTzymmKiVz6mM0IQVwv0GrHwA4_ZPCO97Kb0b-atCiQZKKifCrG2kpdw7dcXdeuoxQwZEmabbJ3bbUN3fDF0e6zq9dtH6T-shGuHv0iQYRjq8kbioInPhzVyIUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غم‌انگیزترین تصویر از دنیای حیوانات
💔
🔹
مادری که مرگ فرزندش را باور ندارد. دلفینی در استرالیا، هفته‌هاست پیکر بی‌جان فرزندش را رها نمی‌کند. پژوهشگران می‌گویند این دلفین در حال سوگواری است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/677463" target="_blank">📅 22:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677462">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
کانال ۱۲ اسرائیل: تصمیم ترامپ برای حمله گسترده هنوز قطعی نیست
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/677462" target="_blank">📅 22:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677458">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6nNbnAjwtDAohVPq38nefOcMmBahLI44cJXX-XyTAycPsWz3-7bAqW83TQj3N95JnNgbaFjntJ3UH7vuKHZ5yJTZOvodr19obZt-KV5AAKpDAM4pIoPARg-jKHM0iLyK8bON_cwG8DCLMQC2fAua4A8j9HPgSQAh4U8PrEzX3oeRF03qGa7K2LxBfHGniGKF6paKhSGvUZUdZ-H6y1ecS926Jf6klJQ2YRnoR2Y2vuCfmK25L1DStg_elHnD6nVjvZW_1exy_Kvz5KPDaZkXcJ-Bnf-aDI3hANB6qAlz0DAtqwTn-hWK8HYF9VQq6_0HQo8Ip1sjxWNPzRuy5ytVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عدالت از نگاه امام علی (ع) فقط اجرای قانون نیست
🔹
در نهج‌البلاغه، عدالت با چهار ویژگی تعریف می‌شود: فهم عمیق، دانش، داوری درست و بردباری. از نگاه امام علی (ع)، کسی که حقیقت را نشناسد یا در برابر سختی‌ها آرامش خود را از دست بدهد، نمی‌تواند عادل باشد. #نه…</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/677458" target="_blank">📅 22:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677456">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/010ea8b9ca.mp4?token=ILzCIokExCoBvZcjRHFLA2zp3_KBxurxshM_TEO65ONq9y7sHpDdkA_cGIxGu3HF80DSG5OU6wbhGvSQWVKlMWAoTErcm2iZe9gb87rwD6Auxqi7JA7sI8qzM_ZT0btpQBStP1zP2vLZRu-Cg-iyTigMHCTgqOLtu_9ftKqlH5UqYGTjGoVxSpiJSeARApTiVMpSmKbsLnsxWPsVaaOUJbUYm7UfU0Iim6JzCw5dyLCuTZW1db3-Vzvz37p0v584SedfHaf4XpBH5tTi3vACSVRtSMmsaamljYkVuWhWFytMLWdOz0r4qLMX9G_MJzKMO8KhsEKT29gddRCrDtuugg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/010ea8b9ca.mp4?token=ILzCIokExCoBvZcjRHFLA2zp3_KBxurxshM_TEO65ONq9y7sHpDdkA_cGIxGu3HF80DSG5OU6wbhGvSQWVKlMWAoTErcm2iZe9gb87rwD6Auxqi7JA7sI8qzM_ZT0btpQBStP1zP2vLZRu-Cg-iyTigMHCTgqOLtu_9ftKqlH5UqYGTjGoVxSpiJSeARApTiVMpSmKbsLnsxWPsVaaOUJbUYm7UfU0Iim6JzCw5dyLCuTZW1db3-Vzvz37p0v584SedfHaf4XpBH5tTi3vACSVRtSMmsaamljYkVuWhWFytMLWdOz0r4qLMX9G_MJzKMO8KhsEKT29gddRCrDtuugg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع انفجار در یک کافه در مسکو
🔹
خبرگزاری فرانسه به نقل از پلیس روسیه از وقوع یک انفجار در کافه‌ای در شهر مسکو خبر داد که منجر به کشته و زخمی شدن شماری از شهروندان شد.
🇮🇷
✊
@AkhbareFori
|
Linkظ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/677456" target="_blank">📅 22:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677455">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
نتانیاهو کودک کش: اسرائیل به زودی به همراه آمریکا دروازه‌های جهنم را برای آنها باز خواهد کرد
#Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/677455" target="_blank">📅 22:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677454">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f77975f3da.mp4?token=cKPFUmQOIvdaDVQ5Td589Ukj-tNqzIZi3jOaGpYT86mkxf5pmD4Q0pXbFal-3ydFP9iXsbLwg77oCVMAZlZqbXnTTbXOKyuQLgTVBmTk64qNQItZhDDxj2ZhRt5GZT3dcQCztSgFauD9ngTf7WMBHtd4LlKr8qXEir44nB8j38wxQEAJ9-XXuX2gS6ZY35xYirrKG7GAXdw-GGpcRs2H9S1DL53wdiglAfgLfbcOO4pCQpCzFQ8VoPfebnbeN3RGXdCz-5izy72AZ6Tni9o6xofTj8e-wJKqgfs8hnLxiXGcFYKKy13dTsSck-oxOzPN0u4MXdN_Vy5bZC95KoI-RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f77975f3da.mp4?token=cKPFUmQOIvdaDVQ5Td589Ukj-tNqzIZi3jOaGpYT86mkxf5pmD4Q0pXbFal-3ydFP9iXsbLwg77oCVMAZlZqbXnTTbXOKyuQLgTVBmTk64qNQItZhDDxj2ZhRt5GZT3dcQCztSgFauD9ngTf7WMBHtd4LlKr8qXEir44nB8j38wxQEAJ9-XXuX2gS6ZY35xYirrKG7GAXdw-GGpcRs2H9S1DL53wdiglAfgLfbcOO4pCQpCzFQ8VoPfebnbeN3RGXdCz-5izy72AZ6Tni9o6xofTj8e-wJKqgfs8hnLxiXGcFYKKy13dTsSck-oxOzPN0u4MXdN_Vy5bZC95KoI-RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتقادات نوید کرمانی نویسنده ایرانی- آلمانی در مقابل وزیر دفاع آلمان: حق حمله به تمدن ایرانی را ندارید، یکبار برای همیشه به اقدامات غیرانسانی ترامپ نه بگویید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/677454" target="_blank">📅 21:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677451">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مردم ایران روزی ۲۰ هزار تن میوه می‌خورند
اکبر یاوری، رئیس اتحادیه صنف بارفروشان تهران در
#گفتگو
با خبرفوری:
🔹
روزانه حدود ۲۰ هزار تن از محصولات کشاورزی داخل میدان میوه و تره‌بار توزیع می‌شود و نزدیک به ۱۵۰۰ تن از محصولاتی که ضروری نیست، دپو می‌شود.
🔹
به دلیل افزایش هزینه‌های تولید، میوه از سفره بخشی از مردم در حال حذف شدن است و دیگر مردم توان خرید میوه را ندارند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/677451" target="_blank">📅 21:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677448">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QQnCxz1z5kU21LPW1PWhxXQFbvDs28UYRr3SEtYhyn6iJCZ5098dbd8cfknzMJk2Z6G6RUfhPQYPxHavkWIb8t-dtsr_3v5V8bDDI5Ku65BBNli8J_1dhKat3ifa_-gWe7lEBAP3VE-bBso3mlGrrd7ZdFCbMQscSbl7PK08T9Q7kQpUE1WB4-J7123Jd47KUIh3_MCblVSO7kDqIyiQZAHWXDnkdNNEHoHeD6zJoPMQkGhkCQz1XkfLzXymKuuJvNjA-hdzFp4RTgVsppEsiwrfbLb1hxWSMGh1fA7BDYdu7Fy7A8SsJOcWMS96bl0NKgDOjpjsXYOZi_EiY7LWhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hVJKURMmCJ9TMWKeT6fyiFEU742r8bBURN4W8RwTHb60wyLjNkuf92Hs6WgSchkE6DQ8BIPYKZa1k_Pr8hKbP6wjzYj_uc5TVxfkPcMlnv87kOCW8nt-NcXgZFdplrf68SGmXaF3FCcrjOJm5vupR4iXxh9GSH9FJcfQ4jBA3mE0LuQvUIn_qIq-i1ZrdaNPsok10Aq0UfLddNgU-_Ho9tCfcjfcDcsqot0qjWFr3WQVtoXuiYFTcNQW4S5OwizPwVIhgiGc30Wh6OzRX4j3_QwTrShhUw5CpZvcXYSGgyUD3qrVu-8pBv_dd0FwlqTxIMsd6R31G6917VYJXCVoKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پست های بی مفهوم دوباره خوک کثیف
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/akhbarefori/677448" target="_blank">📅 21:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677447">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7d52c5baf.mp4?token=Bc22BUa1iVR_m-Rzkg50C6jLOwdNSf05HBCxok_5FZNxkKXQpTcKv4019dS9OIfx1wLVr0TiktYOA_WIL_a6actLkm75aygamflpOuAfpqYPusw_QSkxTKfT2ZAQpcq119z4zMgVv0RvX2-huh8aOuvh0o7h5SSqatO59WcnQ1w9POf3BtUcXkhIR6773gS-aSI4q49Pdv_zqexyzcdWwKhKXzng2uNjJ2sPC-SSQMDpbqG1lXcYM3t0c-A5zau5KKdaTiZm91f3XdLBQvhkvdkMWuCIzlt-zD_8PTZB40Krjg-TsiqGuh-Ti_0keVf95-nXSs7FnMK14tbaj2zUwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7d52c5baf.mp4?token=Bc22BUa1iVR_m-Rzkg50C6jLOwdNSf05HBCxok_5FZNxkKXQpTcKv4019dS9OIfx1wLVr0TiktYOA_WIL_a6actLkm75aygamflpOuAfpqYPusw_QSkxTKfT2ZAQpcq119z4zMgVv0RvX2-huh8aOuvh0o7h5SSqatO59WcnQ1w9POf3BtUcXkhIR6773gS-aSI4q49Pdv_zqexyzcdWwKhKXzng2uNjJ2sPC-SSQMDpbqG1lXcYM3t0c-A5zau5KKdaTiZm91f3XdLBQvhkvdkMWuCIzlt-zD_8PTZB40Krjg-TsiqGuh-Ti_0keVf95-nXSs7FnMK14tbaj2zUwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت شهادت جنین ۶ ماهه در حمله به مدرسه میناب در برنامه پرچمدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/677447" target="_blank">📅 21:40 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
