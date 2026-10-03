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
<img src="https://cdn4.telesco.pe/file/scqhaPl9jwu5mwjC1WZNODqMg6kfuKMjMBWDo-jCSTBYtDrMgnqS76WiwH18VUDsqtElcx8j0vApmnxKXS-k5Yp72pb0LWu_jbsClQdHAQtYEq6zGLEGr1Co61TDP87CrJ33vWXSgIxHDrRwwXHwrWJXAtynSH6adsejdNUgyACAB6NVFBH6nUY-LyqqXRVJbTR0f_G26HkOZG7GeAVWHwPw-Xo4s82a5FVBj9n32lnTySRw9DtT3To3esZI4paZ9IrgsVzgixA2h6OG2-CyDKIQwc2b6_v4nomhT8BT-3GWqO-yrP2p2ffOGtO3SPXH9FXsj7cx3wJNh-OC2dv0mQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 265K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 12:49:04</div>
<hr>

<div class="tg-post" id="msg-92398">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇸🇦
🇾🇪
انظروا إليها تحترق.. من الحرائق الواسعة وتصاعد أعمدة الدخان في مصفى آرامكو النفطي بالعاصمة السعودية الرياض بعد أن طاله الإستهداف الصاروخي على يد رجال أبوجبريل.</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/naya_foriraq/92398" target="_blank">📅 12:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92397">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cad71f6a8.mp4?token=DYv0WA5wikvqoFK8BtwQwf8UwiCIVtNiDvIgqgoH_dTqUPzj2nb38xObUf8pu1FygRnP2lLvqZ1ozr7lwdX0DY8R83_IncZ7eyYSUIXZyCU0cG2XO1YLJvhkDKoRnNL9FciEW4qFP1jH5h0H88S1ltUOtlsTOjoRdyLKbkciuCfU_uP2jUkMLs-M3t2ILvRKdzmen8fCV5leQa0EvzUsXHDIXf6fN-akFNGqgk1yjexgFmaxm1TH0GRZyOoGqhBGrfBlPc6EiOutE5mvuLqjQFKa5rKk_vTKOjpXpKUAJHEJ0Nxg32E5cxOjjNqAPk1K8uhAtOoCiaPAUHTe45vQBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cad71f6a8.mp4?token=DYv0WA5wikvqoFK8BtwQwf8UwiCIVtNiDvIgqgoH_dTqUPzj2nb38xObUf8pu1FygRnP2lLvqZ1ozr7lwdX0DY8R83_IncZ7eyYSUIXZyCU0cG2XO1YLJvhkDKoRnNL9FciEW4qFP1jH5h0H88S1ltUOtlsTOjoRdyLKbkciuCfU_uP2jUkMLs-M3t2ILvRKdzmen8fCV5leQa0EvzUsXHDIXf6fN-akFNGqgk1yjexgFmaxm1TH0GRZyOoGqhBGrfBlPc6EiOutE5mvuLqjQFKa5rKk_vTKOjpXpKUAJHEJ0Nxg32E5cxOjjNqAPk1K8uhAtOoCiaPAUHTe45vQBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
من القصف الصاروخي للقوات المسلحة اليمنية على المصافي والمنشأت النفطية بالعاصمة السعودية الرياض.</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/naya_foriraq/92397" target="_blank">📅 12:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92396">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/251473a77d.mp4?token=R5wyhtpJ5Kl2riGxExJ1eVkMygFX9WJNrLIFL-LliJrFsbmNEGI1ddHUOMJWEXrX9AD6GnRXDge24m-_cIKKe6Hx64x2vdMaE5kf2J3bkK7fXEaq8ZVIyCUX4Gd9ftBPgCzlObuLcpcVBOCLBeIcGLQuBmfIg4DArpFSb-qFdeoBYX_afCJG6cFhg1ng83RtvoWv5jlz5niOr9YDgOr5neVG8whK98WQR_HfRP7rQ7heqjN9Qw6tOCab93x8ZCHA2f_hgWXjeHp7IslByHXCTLK8vm_cddzuGqfQZLfCdUkScqOiZ9o1xJbrtxGipqvZtXLrnkETrVj60XoUdSIfQX9DBCXIIsQj6f1aPL0atnNcPV57LzD20Dqhn0gLWiBxf0AfEArgfdNeik_kvtgSjJlGxsDUBKKnMkAXwmvHSv5UALNo0D2yxrYeLA04xr1c_lh9De4n0d4BxtfiTEUxy2T3YJOpFxzACYHA2oPl43nqpUTjuAzDtURve_ZXIKY__FYOXjOVwK40gqDJ3CRai7ik6lAYlhwuPQHu2uA3IBveUkVzRkjTMn0UFM6nvaxr2ZEn1wN4ffJ1L16xhqGGc1TK3yvRMXcAvXs_u4mtIFZJmJc9FU3ow6AzpCbcLJK0XOxdrVBbUtJMkfbCGSXd4fTO_CpIymUTgLLnk0EJUqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/251473a77d.mp4?token=R5wyhtpJ5Kl2riGxExJ1eVkMygFX9WJNrLIFL-LliJrFsbmNEGI1ddHUOMJWEXrX9AD6GnRXDge24m-_cIKKe6Hx64x2vdMaE5kf2J3bkK7fXEaq8ZVIyCUX4Gd9ftBPgCzlObuLcpcVBOCLBeIcGLQuBmfIg4DArpFSb-qFdeoBYX_afCJG6cFhg1ng83RtvoWv5jlz5niOr9YDgOr5neVG8whK98WQR_HfRP7rQ7heqjN9Qw6tOCab93x8ZCHA2f_hgWXjeHp7IslByHXCTLK8vm_cddzuGqfQZLfCdUkScqOiZ9o1xJbrtxGipqvZtXLrnkETrVj60XoUdSIfQX9DBCXIIsQj6f1aPL0atnNcPV57LzD20Dqhn0gLWiBxf0AfEArgfdNeik_kvtgSjJlGxsDUBKKnMkAXwmvHSv5UALNo0D2yxrYeLA04xr1c_lh9De4n0d4BxtfiTEUxy2T3YJOpFxzACYHA2oPl43nqpUTjuAzDtURve_ZXIKY__FYOXjOVwK40gqDJ3CRai7ik6lAYlhwuPQHu2uA3IBveUkVzRkjTMn0UFM6nvaxr2ZEn1wN4ffJ1L16xhqGGc1TK3yvRMXcAvXs_u4mtIFZJmJc9FU3ow6AzpCbcLJK0XOxdrVBbUtJMkfbCGSXd4fTO_CpIymUTgLLnk0EJUqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
من القصف الصاروخي للقوات المسلحة اليمنية على المصافي والمنشأت النفطية بالعاصمة السعودية الرياض.</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/naya_foriraq/92396" target="_blank">📅 12:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92394">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/965605401f.mp4?token=gPCPFr2Xlo6gfuvb0O-jXuTFTw5Ysw_NR0MowN-6haJHsgYSAZRCaAdzSudlf8p3O8j8DpKfH_LP8nm3Cu57-1NctoMYoBXWaGPMi7mQ7UZLKnRlf3vLE5_tUZtqlMXsmKkxpQqVgd7BfcVvSLQFeLZ3Q8426PrCSMWWwfxV2Q_bmgjSTFXTrXPowKCIc1veEdtM-tvES6FNsnBoegTS_8YEsj3n3R_p5I69zH5g0LQ6rScN-cw4y4DrUwxq9h6ETv56eIQI2vwvzzr4ozAM5iRjILxOb7dMbGKqmp9wa9Mr85ntgAgK2xvkZj_Ilfw9-0lb8_2EgtPJn4ISg0MObQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/965605401f.mp4?token=gPCPFr2Xlo6gfuvb0O-jXuTFTw5Ysw_NR0MowN-6haJHsgYSAZRCaAdzSudlf8p3O8j8DpKfH_LP8nm3Cu57-1NctoMYoBXWaGPMi7mQ7UZLKnRlf3vLE5_tUZtqlMXsmKkxpQqVgd7BfcVvSLQFeLZ3Q8426PrCSMWWwfxV2Q_bmgjSTFXTrXPowKCIc1veEdtM-tvES6FNsnBoegTS_8YEsj3n3R_p5I69zH5g0LQ6rScN-cw4y4DrUwxq9h6ETv56eIQI2vwvzzr4ozAM5iRjILxOb7dMbGKqmp9wa9Mr85ntgAgK2xvkZj_Ilfw9-0lb8_2EgtPJn4ISg0MObQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
مصفاة النفط التابعة لشركة آرامكو بالعاصمة السعودية الرياض تحترق بنيران صواريخ أبناء اليمن.</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/naya_foriraq/92394" target="_blank">📅 12:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92393">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇱
إعلام العدو:
فشل محاولة اغتيال علي العامودي خليفة السنوار المحتمل في غزة.</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/naya_foriraq/92393" target="_blank">📅 12:09 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92392">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a76c3a62fc.mp4?token=uzf6C1GRgMiMtpmREhuFtwhJSV_-I3UQPSMU_lXHOgcGBJBM0fpi79nvq4i5PgvRTnFHJRb0TMLt92b4xmdDCkV7T9qyBMWSPekPaHvQ8H370kyNz0hS1v8QbWTre4Ty4QRAqFI96xIQrfHkxCSk32XmlCJ5dks08lwacDWA-cNrF9KBEGiUCwK7lV_xEvm49WwqKYxXhp_oavsQf-RweVvIJLFl4b5-yZJ-fN6KBPbEcjwEPCdqbn2EcxMZTb2ThMdLfPTdmSxbjS-rmLku67pXSyWqgv4Xbas_E-31eo6q4unN8JO-TkMBwM2iGQil_5DibAZCXcOMDVPtjv0vX4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a76c3a62fc.mp4?token=uzf6C1GRgMiMtpmREhuFtwhJSV_-I3UQPSMU_lXHOgcGBJBM0fpi79nvq4i5PgvRTnFHJRb0TMLt92b4xmdDCkV7T9qyBMWSPekPaHvQ8H370kyNz0hS1v8QbWTre4Ty4QRAqFI96xIQrfHkxCSk32XmlCJ5dks08lwacDWA-cNrF9KBEGiUCwK7lV_xEvm49WwqKYxXhp_oavsQf-RweVvIJLFl4b5-yZJ-fN6KBPbEcjwEPCdqbn2EcxMZTb2ThMdLfPTdmSxbjS-rmLku67pXSyWqgv4Xbas_E-31eo6q4unN8JO-TkMBwM2iGQil_5DibAZCXcOMDVPtjv0vX4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
مصافي النفط في العاصمة السعودية الرياض تشهد تصاعد كثيف للدخان جراء الهجمات الصاروخية والطيران الإنقضاضي اليمني.</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/naya_foriraq/92392" target="_blank">📅 11:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92391">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcb6959801.mp4?token=T08FMMRuMR5glv5hHEC0YnJLTp_bxqztdfb0TCf0Kxqd02YmY-vn9xDrI8Zo9NGh6dWM6r_jVQF1w_Wouc3I_QIlBJebuTUDNhq_8bIgoHuYkLIKzaCqtLadHD0SURBzdjIMFZ9UZblATjHKiXmCdwy3M9xyWTxinVxoN9nMUAtopdmjOuzOuwBp7wz752t3GN79tSoXpjkT1d0fU8ceqGYF7AT7iExehYBRYpboOHcLtM4VPpF78q26X_5gcQ1AV7FsFuQnut4JNuGdo2ztpLwwTkYZbnnK008EWruUsGn4JDdYPzWy4xjiCHlpZOeFp1BlkTFCtyAIqQf6n4eDaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcb6959801.mp4?token=T08FMMRuMR5glv5hHEC0YnJLTp_bxqztdfb0TCf0Kxqd02YmY-vn9xDrI8Zo9NGh6dWM6r_jVQF1w_Wouc3I_QIlBJebuTUDNhq_8bIgoHuYkLIKzaCqtLadHD0SURBzdjIMFZ9UZblATjHKiXmCdwy3M9xyWTxinVxoN9nMUAtopdmjOuzOuwBp7wz752t3GN79tSoXpjkT1d0fU8ceqGYF7AT7iExehYBRYpboOHcLtM4VPpF78q26X_5gcQ1AV7FsFuQnut4JNuGdo2ztpLwwTkYZbnnK008EWruUsGn4JDdYPzWy4xjiCHlpZOeFp1BlkTFCtyAIqQf6n4eDaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
مشاهد تظهر دك مصافي النفط التابعة لشركة آرامكو في العاصمة السعودية الرياض من قبل رجال أبوجبريل، واعمدة الدخان تتصاعد من عدة نقاط.</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/naya_foriraq/92391" target="_blank">📅 11:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92389">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/njVoMxA3c2qiiP9JqYQB37-eIaryrSHCjfB2IBW3BrSvuusG_VxfBoMDaO14smegASFqRsX8I5rFbmVO9nHHFwq5mQwgYEkEHNpG_B87S9VcRGgzx8iSv_YRUu_sGsOaCoCJlD-uEjdXvkiAfYn-SGQ7YTkoiIiPTuLYpO2M3JXcvSP8YhEANCYKiArsqF2BaTvjx_z5Fir1cC7adXEZih5iKtOQi2Yn07hBgHa5BmaOBvt9Gr0aKUZxHzxHA2wqYSH0STkKCWH-NER2eEpBm5ZVUBa3V7b3IBdNoo6mO6yoW_9lOXEbfLyGnhYLxLrzhn-tw0maZl38oHnPg1BvBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Li8PzaHDlpkviKA_fv2pvggN3NzDW8n6bLgAVvHX1E2K_jYXQ7i8GfVZkQF8vTGIbdiyNQzHtA7eeAU_x7Fs1csp6hRmO_DJ51ZfJTlgpyonxnN6CxAg9G7HJCckpuakMzfFzzEkK-fl5HlJUa4XnpSZIw4Zz5qgD2sawVi12ELanzOZ1eNoxb8a1vEPA-HquwFhyG4GRcPXGAjGltnLzkiwBqTOT7ZIzws5IirWPm2f5-txpyz3rB8eztsIKBh37PqyiiBJMOdKuQY-NAqH-bQuW4duB9p5AN9gwkHDXvWy9CNs3k9h5lvmuxc9AyE9CEB-cnxeFObn2NTHyZP1TA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
سقوط طائرة استطلاع مسيرة من طراز "MQ-4C Triton" تابعة للبحرية الأمريكية على ضفة النهر في قاعدة "مايبورت" البحرية بولاية فلوريدا.</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/naya_foriraq/92389" target="_blank">📅 11:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92388">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔻
السلطات الليتوانية: إغلاق مطار فيلنيوس وإقلاع طائرات للنيتو بعد رصد مسيرة قادمة من بيلاروسيا.</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/naya_foriraq/92388" target="_blank">📅 11:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92387">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية في مطار الملك خالد الدولي في الرياض.</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/naya_foriraq/92387" target="_blank">📅 11:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92386">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgicUBZaGLu1s8PNlegP8uFQN1FFuWOy4WU41dP7XqRmpT9kN1yY6RaTRMFJImpSx3DtXFspX9gMZ9HjW2Rdk-gn0vJv5rHG2uCtXTT7P3k_2N24TNHlHsm5oC99khw0CoS4scjgrXvKZGVLB6BK8vSBmZQUmdsP_VK8d0BPYb_JcH87YpKmLLjoATN6331eUHpwpDsxPqpTNJqw5_bhkmRphqqMEj0wx5KSLUkd_WPHuIz5b-m1Pfjy-ycwAka2Oqls5M2s5heP5EP9vA1k0bYPVw92NQGCwUWYc09uWZ7Q-viLav1cGUuZ5Vygg0okEjAZzzTmhj50uFkzE6pinw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صواريخ تنطلق من صنعاء نحو المواقع السعودية</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/naya_foriraq/92386" target="_blank">📅 11:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92385">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGx_J7Vo9GqMa5O2CG0gzNbT8QNqzLjV7RbjQAG-gmmkmJgQ8exaeRDbRFsbmaSs2Ch2rCaBO_FhP73l6f3jO8nJxL48J8JCF_8GpMhKzGJ_Vehh8S3Kns6jm2RzI4Avs0hmOJOxZ8JZDQDFcusZ0gdVxKxBb0JaOMXoHZTlUAq6FLWcLNe06cHth2LIHgSaUQ_E8s_2tZLXHXZ1zjvOR1K7F97K0ml-5bO8c_MV5IuUzD2o5yHzxXazSLIhzkktzrPx2n_RY8WE6D3aIOJ9ShIvywKMW-RoJpm-NpRQczsbS__-YbD-C9jVLiBIhq9gWCrlDNJTGN_y_BBlc4Wa4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية بمطار الملك فهد في الدمام.</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/naya_foriraq/92385" target="_blank">📅 10:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92384">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔻
السلطات الليتوانية:
إغلاق مطار فيلنيوس وإقلاع طائرات للنيتو بعد رصد مسيرة قادمة من بيلاروسيا.</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/naya_foriraq/92384" target="_blank">📅 10:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92383">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية في مطار الملك خالد الدولي في الرياض.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/92383" target="_blank">📅 08:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92382">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aW1e_Hy2qu2EcViMIOND0PVGzr6plERpvclD6mlZYDX-B4-P86UVJv8Y96rFovz4-srvtkOctM3mIAwvkwvUsPAjfAyRHZrwoI0c6pK6AB619rwRy7-8QQRnz-F0DKNK_BbwrpbGdskj1Hy7aN-5PkBPW37rMcfrId2edlHpqTTswUeiHbWpzsG8biIs0xDCsMGY04CJAomwaL675XdGAHzE9oG_3-Ox-KH6CFY6-4nZjBXD1dmhxW9d9F9rRCz_BBrSHIVpaWFENXSneJdfocEyGsSqx4ip0_QKszEajYtq4paMo1YEPMnD6D0o5RlT8ndznpOl4-RexYENLMGhtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية في مطار الملك خالد الدولي في الرياض.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/92382" target="_blank">📅 08:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92381">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏ترمب: لم يعد لدى إيران سلاح جوي أو بحري، مسألة إيران ستنتهي مباشرة بعد الانتخابات</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/92381" target="_blank">📅 03:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92380">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORr5MdbGOu-ePKxJLkmN4nf2x19Zf9gkIcnHtLue2n3ZApFR-IiRZem8YP5baD7eBN1ze9qOLetDjq_HL19Gkp2iHVDEtThkSXg1kgdgCquXqTuwzpGOYm9PzHw4whLJ_1vOh1TQLf9MTCyA-0xWSeHET24IKYbQtGEgeELlQ5xcIvBsF27b7EtAERp1fLlNnJvUH3m4u9XBaxHu5hYZReUdRjmoakgm_6u_Xs12MvxZPXqNvG8Fn_mMtIIHm5cVF20YOj2s5wT59dSXjwKWVLyx3bbgMLZ6KZJq5vJxgaT1lk_OgSTQodCBDL-61TYVGkHygN4G1Stq9h5JioyYHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحرس الثوري يستهدف  سفينة مخالفة على بعد 4 أميال بحرية شرق سلطنة عمان.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/92380" target="_blank">📅 02:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92379">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">انفجارات في  منطقة عسير في السعودية نتيجة استهدافها بصواريخ بالستية</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/92379" target="_blank">📅 01:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92378">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇰🇵
جمهورية كوريا الشعبية العظمى تختبر صاروخ بالستي قبالة بحر اليابان</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/92378" target="_blank">📅 01:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92377">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsAD1mqk3d1eM5bW6J9R2ieQ3gBOX49Fy2u3dywqEEvwgA5c2m_WBZ3m9R8bySaMRD5lQw4y99OR_6ZQTCn2BPQZIqGb4twnM6SLukR3dYU0NtxJrYN3A1NA9-JekxQL9fv41wve6-vGJqwDrs9OVlYnjCYiZ4ZwsRYbv1FFY3C0BO96dQrdv15bn9dguKlZoFIWYcnGj8DaZrSN7xa-iY8b0XXNZWJbbom5XS9dRx5-RaEjX4xXR6a_6TzkL83OCsHQK5Gi7O2ymmuTD0_HC-eQBkjUKvtOC8L9pv3GZr-i4n40HvO0g5rH8CaPxoMRENQGQdJDWzp0tLBzGdcP7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔻
الأمين العام لكتائب سيد الشهداء، الحاج أبو الاء الولائي:
اعتراف ادارة الشر الامريكية،
على لسان رئيسها الأبستيني، بحجم خسائرهم البشرية في العراق وتشبيه وجودهم هنا بـ (المستنقع والجحيم)، يؤكد بما لا يقبل الشك فاعلية عمليات المقاومة العراقية وقوتها ودقتها وبأسها، بعكس ما كانت تحاول أن تصوره بعض الاصوات، عبر الاستخفاف بها والتقليل من شأنها.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/92377" target="_blank">📅 00:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92376">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPISSvMyAlh-LOdOP6VpMhUko1KaOhijn4mCzF3Nwfm0kmkBohlHhYYp7_SUwTRC45QtqteA-PdfbSGY3Hl1AfwZEfq0aWdjoN9RQIXUgx0aktiUHK1ULkeYK6n2WMTLeUMCoViXbFN519VznXiZFdqP6YasloI4mg_rnnKA9y87CLjFdNRjdteWOhfqnre-ZhiZR1ks5pB3SgJu-57_3TW0AGK7WKB-CUU8IMxSp1fJ29TfaHBAcymcZCQkLi16g3fkwMTlNVmImqYFmO00ntf1L81Kz7itLdJNx8pH7yMIyWJpG4pbF255lpnjEvNNr_UthexZ910Pl8mapB1ZRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
الرصد اليومي لطلعات العدو الجوية التي يخرق بها السيادة العراقية.   الرصد بتأريخ 1-10-2026</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/92376" target="_blank">📅 00:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92375">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇱
🇸🇾
الجيش الإسرائيلي يفرج عن أحد عناصر الأمن الداخلي السوري بعد احتجازه لأكثر من عشرين ساعة.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/92375" target="_blank">📅 23:41 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92374">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a23207838d.mp4?token=CUecc6KBCVCQTHxQpJmGd8sAEIKMrzoBmeYUtwng8b2iaP8yGJlL16GUAoZc5VP_FBb9vugmmJUuWa9rTX1tSL2oEk-C5JWKsonSy6o4hGLYHbbx3ZOsPi0kT6tuLXMQ2G7jW9NZwsh9ptWm6HSxh32gZCg3gttd_8JTUxy_I7Q9kDOLgU2J4VhSM1Za1EemdL3RR9PwYHGZ3ezY4iuMmPMe5uQhg4VFgW29z-zA5qOLsgGMd5E2chUR31-b4tn9FHlzXl8VKmzGxRCgJkDp30XZm7XKf3VcuUhquueNpganHBf3uwSzxVALQ7kX5wZmuIQUhav5_l2iquAcoIIc7VW82Wm7AUpvICB8oSmAyL_xUqvTQ3MY5VrehwHbPSg28crM_xnWQWY4yDI4BTrtJojNZRqzhtZWz6YkYqUcGsDIdFOY_oo2QzclHc5xl-Rt86LCEUiuu8mBI9jWs3zfHOxm5L63mzomKRx6t07JVbRSZXQtoK23d8_6TDXj6ZYxTwjTpgZ4xHGO1Gc_hvF9S_4WJomIubtzkEKNIKUSf10oBst4FXt4lb_1hc_Ak72x1PpdJ1rSG703GVGPag2vo2o3m8u7gHGkpxWSq9TVvuk1AQwftuI6yNVCfTjx0MkMYg3LJc2mXgNg6iZJgDNiAaMlV40ZD4vDTouOi1uRYfY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a23207838d.mp4?token=CUecc6KBCVCQTHxQpJmGd8sAEIKMrzoBmeYUtwng8b2iaP8yGJlL16GUAoZc5VP_FBb9vugmmJUuWa9rTX1tSL2oEk-C5JWKsonSy6o4hGLYHbbx3ZOsPi0kT6tuLXMQ2G7jW9NZwsh9ptWm6HSxh32gZCg3gttd_8JTUxy_I7Q9kDOLgU2J4VhSM1Za1EemdL3RR9PwYHGZ3ezY4iuMmPMe5uQhg4VFgW29z-zA5qOLsgGMd5E2chUR31-b4tn9FHlzXl8VKmzGxRCgJkDp30XZm7XKf3VcuUhquueNpganHBf3uwSzxVALQ7kX5wZmuIQUhav5_l2iquAcoIIc7VW82Wm7AUpvICB8oSmAyL_xUqvTQ3MY5VrehwHbPSg28crM_xnWQWY4yDI4BTrtJojNZRqzhtZWz6YkYqUcGsDIdFOY_oo2QzclHc5xl-Rt86LCEUiuu8mBI9jWs3zfHOxm5L63mzomKRx6t07JVbRSZXQtoK23d8_6TDXj6ZYxTwjTpgZ4xHGO1Gc_hvF9S_4WJomIubtzkEKNIKUSf10oBst4FXt4lb_1hc_Ak72x1PpdJ1rSG703GVGPag2vo2o3m8u7gHGkpxWSq9TVvuk1AQwftuI6yNVCfTjx0MkMYg3LJc2mXgNg6iZJgDNiAaMlV40ZD4vDTouOi1uRYfY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: إيران ليست في وضع جيد، وبمجرد انتهاء مسألة إيران سيعود النفط إلى أسعاره الطبيعية.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/92374" target="_blank">📅 23:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92373">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇬🇧
🇮🇷
‏
الشرطة البريطانية:
توجيه الاتهام إلى إيرانيَّين بالتخطيط لعمل إرهابي ضد الجالية اليهودية في مانشستر.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/92373" target="_blank">📅 23:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92372">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇺🇸
ترامب
: إيران ليست في وضع جيد، وبمجرد انتهاء مسألة إيران سيعود النفط إلى أسعاره الطبيعية.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/92372" target="_blank">📅 23:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92371">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZmAT8J_BQrS8aQzA-NZPCjTlm9QFKE_kPT4NwcZTtVYub0eS-Sc7NkVAc8CKEQ4O3enAqhPRFn1EiBKRdVH7F70LlnwXoUJrT9CDV-z6lUNf8Nc04XkzqWDC5Vl-pKQ8rWtEbAqzstfNeRlSm0w_97NQFdu6m87ikq8ALTgVXRpPrYoVtvem5gqDeE6C-YdHmq3i_L2liUqZqFqKOVcu6XgHdXUM6mxnPJOE5JzAPmt2WNOK-NgtquU_iiPsIheD3mfyDL58EYUCX7oV2MJfg_79abPyY4hMmsKiSBnVv5w5pGLARHLV1RaK8gUKBIfNh7ce-dqA2ShfAmzkEDNDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
النائب العراقي محمد الخفاجي: كتاب مرسل إلى وزارة النقل العراقية يبلغهم بإجراءات الجانب الامريكي بشأن العقوبات.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/92371" target="_blank">📅 23:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92370">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔻
الاعلام الاميركي بخصوص قضية فلاي دبي:
عُمان منعت منفذ هجوم فلاي دبي من السفر بسبب آرائه المتطرفة.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/92370" target="_blank">📅 23:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92369">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhFDzOJoH__iFEDt8Xr6OKm67CLiP_dn-_36fz3DfM0Gaf_yQRj9wt14CDM6-GXVgxgv5dnQ2n8MZsqcjaLXICNp_dHn83zBJ3CYT1zj4w1dRjmAfQx5vVfkeCZBb8GlqPGyuusb-1R6RofI0uPY5XrBo5LARa39M4kabIurlOVjoe-E08gHlP7mNgt5m9KNRA36RGdKJz8eZ_aVSk29AQ49uF5scVGpS-uqmLL_m9TRdcG1aiPhUeXCTqjnQ3vN5hGYQEVhK-S5V0Be5WQ8NA7KnOo9QBspB4xiq5qBN1lxcHOA8J9Hzf0rGsu62H6F6kE_5D6ySE9Zj9tSejqx7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
رئاسة الوزراء العراقية: الاتفاق على السماح بتسيير 40 رحلة جوية يومياً من وإلى مطار النجف الأشرف الدولي لشركات الطيران الإيرانية باستثناء شركة ماهان.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/92369" target="_blank">📅 23:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92368">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالإعلام الحربي</strong></div>
<div class="tg-text">🔴
الرصد اليومي لطلعات العدو الجوية التي يخرق بها السيادة العراقية.
الرصد بتأريخ 1-10-2026</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/92368" target="_blank">📅 23:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92367">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇶
الميادين عن المقاومة الإسلامية في العراق:
رصدنا أمس 4 طلعات جوية للطيران الأميركي في أجواء العراق.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/92367" target="_blank">📅 23:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92366">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bi6GtA-iGspRrLsQo94HDRu6JX-1b7PxBx8vsXQDnooBWZY-3X9tOOHsm9OBo1Y56dK4AMpNmzK-FcBwpQKuH0_VXDL7YDkzQnFVZVD5QT941hdG3PfvTZY7cT8a5MRutOhBONf_kav9P7g975Dyr0wNkKrWNhekMbl7awNVDhb4MwkBAr4oN0WjqBA9j6_EIWmS0KLLgJAiTECpgj20P_jb6diECrcF9HOAwRwsPoyMTtWNgkyEPdGlCPTXDzCQiw3LqNNwRBqTgt3TEMUrXMeREinA0pCNNDzSWBVX9dkBlkZcgTl9zwnm9puqu8U9k33HTRj5vo5jweDnawwSxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
انفجارات عديدة في نجران نتيجة استهدافات مباشرة للقوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/92366" target="_blank">📅 22:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92365">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇸🇦
انفجارات عديدة في نجران نتيجة استهدافات مباشرة للقوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/92365" target="_blank">📅 22:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92364">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇷🇺
زلزال بقوة 6.2 درجة قبالة سواحل منطقة كامتشاتكا بجمهورية روسيا.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/92364" target="_blank">📅 22:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92363">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇶
🇷🇺
الخارجية الروسية:
نرحب بانسحاب القوات الأمريكية وقوات التحالف الدولي من العراق، نثق بقدرة العراق على مواجهة التحديات وتعزيز أمنه واستقراره عقب انتهاء الوجود العسكري الأجنبي، الجيش العراقي وقوات الأمن قادران على تعزيز القدرات الدفاعية وضمان الأمن القومي</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/92363" target="_blank">📅 21:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92362">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwuRLin0y819xFUSCJqXxdVoO7avGi_FCz1AhPviSMA_-Diiaq8u0Lvc3a60cLgfR793XnvTXpBe_rC9MxMv9d1xqH660tb0CPD4UC7kYJWaQpt87k18xdqekchFCLDdSzAxVYgmhAfuY7e6cyHxmnn8TeDr__yhLh3Azj3elC2z2yvSxISOpRqxx1pzKmQgEFTsaOy1FxBYSZr_id-tQfZfazr2K49FS--KW0HKZ1gtzdglT4uNd3QAMZzqrlu2gkW9ycW1AY006uKtasrSzPGClFxFbRThsH-G-xDoc6WcNXTI7YgvadGRXIQBr5vJ8jz7piFJ31FIYaWNe3TY-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
اسعار النفط تصل الى 102 دولارات للبرميل الواحد.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/92362" target="_blank">📅 21:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92361">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇺🇸
إطلاق نار يستهدف ضباط إنفاذ القانون في طريق جونزتاون بمنطقة بينك هيل في كارولاينا الشمالية.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/92361" target="_blank">📅 21:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92360">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇶
شخص يقدم على قتل اطفاله الثلاث وزوجته في قضاء المجر بمحافظة ميسان جنوبي العراق.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/92360" target="_blank">📅 21:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92359">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇸🇦
🇵🇰
رويترز:
أن باكستان نشرت ما بين 30 ألف و 40 ألف جندي في السعودية للمساعدة في الدفاع عن المملكة، وذلك من خلال اعتراض الطائرات المسيرة والصواريخ. وقد وصل الجنود على دفعات، بدءًا من العام الماضي، وكذلك بعد التصعيد الأخير، ولكن لم تتخذ باكستان قرارًا بإرسال قوات إلى اليمن للمشاركة في العمليات القتالية.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/92359" target="_blank">📅 21:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92358">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇶
🇮🇷
رئاسة الوزراء العراقية: الاتفاق على السماح بتسيير 40 رحلة جوية يومياً من وإلى مطار النجف الأشرف الدولي لشركات الطيران الإيرانية باستثناء شركة ماهان.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/92358" target="_blank">📅 21:21 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92357">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇸🇦
🇾🇪
استهداف خميس مشيط من قبل القوات المسلحة اليمنية بثلاثة صواريخ باليستية.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/92357" target="_blank">📅 21:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92356">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
يقول المحققون إن مساعد الطيار في شركة فلاي دبي، المشتبه به في الهجوم، قد التقى بشخصيات دينية. والتقدير الحالي هو أنه تصرف بمفرده، بينما تحقق السلطات في احتمال انتمائه إلى أيديولوجية تنظيم القاعدة.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/92356" target="_blank">📅 20:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92355">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 94 غارةً جويةً وصاروخاً استهدف بها الأعيان المدنية في محافظات صنعاء وصعدة وتعز وحجة وعمران وإب وخلفت شهداء وجرحى من المدنيين، وذلك من خلال طائرات "F-15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف والعدوان الصاروخي من نجران وجيزان .
ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد 1350 غارةً جويةً وصاروخاً.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/92355" target="_blank">📅 20:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92354">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgxqbQrcWi6FZ1V62FTviIbQExvT9AvYSqm6pUbZukzAgYA_YUhB_hBm21ZBpEL8uXRw94y8vMUu3SnogmVykb2lovyX9_qfPKWn_ayvVIor8bPXhO9bHZYwyxShrcGcymiMM9etDvaAMTfWmIHG96OL62t0fZn__Naqjm2GPTL5gaB9aoc73LQjcoouRKMgyydcOy1VFUyyH9VAzzncv9-SgiekFtRCAKdgaG22h9MoHn1rJfQjMoPtnwIE7wvmgPHNDDBDpTvEyZW5jSUx4AStHyL3L6i56006LvTbeDdc2b05ZMbgYif33cSgeoH4dap28Rlaf94c1hsluIBVZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
رئاسة الوزراء العراقية: الاتفاق على السماح بتسيير 40 رحلة جوية يومياً من وإلى مطار النجف الأشرف الدولي لشركات الطيران الإيرانية باستثناء شركة ماهان.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/92354" target="_blank">📅 20:17 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92351">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gX7MTaTqiLP8mGtS204hqlTTpiIo4LgoVFyjqgNnhgyEnN1ewo6gFEgXiJJ86XvYdxkbPu4T1WCX2wW0P9Vxvaoo-8qaEVav6kWpvKHLeeCjAIO64qnbFPM2TrrEYsRgVmezX648qU-22ykJImrl1DT6wdZfiWKMV9J9ItPztRhVwq7YAMJDUKgbomTiME2PzRFcRqwvUj546R2mRsNMMROpaunyYXG31GFgW_rA64zovUp0Zn0PZP2i1uhcdPn9Ezo37M-bsyGZWOYCg7wvdr7SZWTiG62ntt8jwXfMbzSaiWbGN88IqnQlbz6Y8qpZUGv-Op-emECuIpNjrraS8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🔻
بدخول بريطانيا رسميًا في العدوان ضد اليمن بمشاركتها للسعودية، هل سنشهد تصعيدًا أكبر من الجانب اليمني خصوصًا فيما يتعلق بمنع الناقلات البريطانية من العبور عبر مضيق باب المندب؟!  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/92351" target="_blank">📅 19:41 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92350">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b94d41695f.mp4?token=BsbtJZMJyjqZk0RzriAfXD6MuShTpVVQLtRq6q_Mkr8tB9oeipIY2RO700FAb-8rgBFdI_5s73IvhJkZCtFD4fAjvUtntaAdrjxVijrhcvnmI0GZ1gga7FfzZy7AMQbjwPEqkdKd84TEq29ZidW5k5WjV_O4vn4Ase_qLmL0x_3LAbIXandAiOMU53mqcsyLUS6datkcx5dql2XM166mJ8o_IjqjCoadrVmrzdxzAKlQbW7lU10351_kXxwV0nO9j7YM1RnTt7Dv52dktDB-0BlkWCETRvNrVbV0XU0TcKAFi4uLjqxYco7w7kDRvyylI5IXsdthe-Rq4c-7bM6SSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b94d41695f.mp4?token=BsbtJZMJyjqZk0RzriAfXD6MuShTpVVQLtRq6q_Mkr8tB9oeipIY2RO700FAb-8rgBFdI_5s73IvhJkZCtFD4fAjvUtntaAdrjxVijrhcvnmI0GZ1gga7FfzZy7AMQbjwPEqkdKd84TEq29ZidW5k5WjV_O4vn4Ase_qLmL0x_3LAbIXandAiOMU53mqcsyLUS6datkcx5dql2XM166mJ8o_IjqjCoadrVmrzdxzAKlQbW7lU10351_kXxwV0nO9j7YM1RnTt7Dv52dktDB-0BlkWCETRvNrVbV0XU0TcKAFi4uLjqxYco7w7kDRvyylI5IXsdthe-Rq4c-7bM6SSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرائق واسعة تندلع في العاصمة السعودية الرياض فيما تكافح فرق الدفاع المدني لإخمادها عقب الاستهداف من قبل القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/92350" target="_blank">📅 19:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92349">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe53e872a4.mp4?token=utSJvWd_QlVHssi8g6YXdjZkN_UbSK05mA8iYSnfDlLh0_Zi1sfcOIq4I8glXYPVBkNO4bx5k7-1gq58zzhkgb1u0zuWUqi06lS_iq8prumR415EvK-PouDQQEaL7AtUU9ThArMKwMwJhmVb8MVbq1wky0nxM75wTpvE8QE4Y0Iklq6rIOnosgUlAuM9H1eJ7GiqftFBV0XqS4XMkyO63icDF6Lbz2hCHLSLlq9HDdAri7FyfJ0cBzrcusS2ykeLVDYF3emcg80JcgP-5hhscFQL5rA7gk6LI0wVMIYX95UejIYWkxHjSyWbPNtu_KuQiFk4FHyv9rxu7M5Agsmm0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe53e872a4.mp4?token=utSJvWd_QlVHssi8g6YXdjZkN_UbSK05mA8iYSnfDlLh0_Zi1sfcOIq4I8glXYPVBkNO4bx5k7-1gq58zzhkgb1u0zuWUqi06lS_iq8prumR415EvK-PouDQQEaL7AtUU9ThArMKwMwJhmVb8MVbq1wky0nxM75wTpvE8QE4Y0Iklq6rIOnosgUlAuM9H1eJ7GiqftFBV0XqS4XMkyO63icDF6Lbz2hCHLSLlq9HDdAri7FyfJ0cBzrcusS2ykeLVDYF3emcg80JcgP-5hhscFQL5rA7gk6LI0wVMIYX95UejIYWkxHjSyWbPNtu_KuQiFk4FHyv9rxu7M5Agsmm0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرائق واسعة تندلع في العاصمة السعودية الرياض فيما تكافح فرق الدفاع المدني لإخمادها عقب الاستهداف من قبل القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/92349" target="_blank">📅 19:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92348">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRHIA3A-IBiuaK7w43BFapurr7fM0twEYHD8gZIB8IDY8RrC3As5R89W1XN6wV6ES3fiVuSgpGci7hpv8udzykezX0xr0vQ4h-qevJikTa6eWWu808FtLCKxhliWUB5Cew2P2NjH9tLEpN-6YhkFOemErvR9deOT1-gaJxYbm-oLCATFUuOvA7tbcjpFmd4D3JNeD33UXvhW6clmeYEayT9lRLyaJ0ZbOrc1FXa_EyvNbkzNDULrguSOB3kR3ul0g4317RubZ-uMrTjbjp6k1x9mhxglinHeK2zZpmBpPntrUUItZ5Gt5DqgJsPKP3BlJvO9ZNY6YEwfvTj72w9-9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
‏
منظمة النقل البحري البريطانية:
ناقلة نفط تستهدف بصاروخ أثناء قيامها برحلة مغادرة داخل مضيق هرمز.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/92348" target="_blank">📅 19:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92346">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a52317416f.mp4?token=k0J0wsBrUANuUzEDf02AhVHqFnWg6ovsFMXZTqMKqkQz-cbwHzWNPh20x5EcmbDdlYcWjpLzzOGilF6Fpw8Lb5nhSLFNTSYalW9dg4LbTZOykQPyUeWaF6ujI-yMrh3P1ECiKgyF-vR5pb62XO1GuwCaogM9deSX78iRaPqmkn99CywV_18HT7krB0iDR8-4hTd97kxYQhOtk9lVxjP5QpGhkpWyKcn45g5NSCEx3H9c9ONW8o1EtsFeyhW0cBw0bR9Dyh6xkQB9Ix4HkZF5K3hYC_3RRV7PkMv2ACvqOXpOUphj5yee_2yW3UcXtDvufvpx_oC8xO1GXLGgyQEeBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a52317416f.mp4?token=k0J0wsBrUANuUzEDf02AhVHqFnWg6ovsFMXZTqMKqkQz-cbwHzWNPh20x5EcmbDdlYcWjpLzzOGilF6Fpw8Lb5nhSLFNTSYalW9dg4LbTZOykQPyUeWaF6ujI-yMrh3P1ECiKgyF-vR5pb62XO1GuwCaogM9deSX78iRaPqmkn99CywV_18HT7krB0iDR8-4hTd97kxYQhOtk9lVxjP5QpGhkpWyKcn45g5NSCEx3H9c9ONW8o1EtsFeyhW0cBw0bR9Dyh6xkQB9Ix4HkZF5K3hYC_3RRV7PkMv2ACvqOXpOUphj5yee_2yW3UcXtDvufvpx_oC8xO1GXLGgyQEeBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد للحرائق في العاصمة السعودية الرياض</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/92346" target="_blank">📅 19:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92345">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇶
🇮🇷
رئاسة الوزراء العراقية:
الاتفاق على السماح بتسيير 40 رحلة جوية يومياً من وإلى مطار النجف الأشرف الدولي لشركات الطيران الإيرانية باستثناء شركة ماهان.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/92345" target="_blank">📅 18:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92344">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مشاهد من الرياض بعد الهجوم اليمني</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/92344" target="_blank">📅 18:54 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92343">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsrqoN1QKXNEwypLfXj7TTYYXpOq4vvUb085ZkNTD37PKw0o_pA_GONMS1Ri872izARG78YW6QwJ9j6PXon3g534iUFksLZW5SBgnwn9DNgNUxvwtwYjnvsZqd9mjXWPfmTcz0ZePA4MXFmOsSJN3kaqbx_L7_ltoc8hvFujnb-kNh6Xs5YYwdZ9gO8WxX2Vo6GGYXWABLAVlJcZjv8f8gOhrDurdEZXIKPVwZsKHrzinQz1qWQp-h_e6whyQSdJLoV8ppVWwfGiC39bZT8f19bq6TmZhby5_2pAZMlfHqYHV4W2KEun3sSB-QIgaYr2rbJgZ8k0ReByhCFpe15Uvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇷🇺
روسيا تعود للعراق بعد الخروج العسكري الأمريكي
اول عرض لفلم سينمائي عراقي المنعطف داخل موسكو منذ عام ١٩٨٣</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/92343" target="_blank">📅 18:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92342">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed16bd6292.mp4?token=nc4QAtVzzdEMnwpOWGCS7v18BpxdhYS13DhbkPf0dwEkVgr7lQs3sNmLE5GBssZVQt-X7V1lFWDT1A3DeT3Uv3lIrjfTOAjOj8iEnTD4l5jnABXrsh2uGe5LJbTE2AA4ovB5vAl-gr4nduuqHNLO6SAL_yAAVeLC7eD71B8Yli8E2dMemlZCBL8XjCBDCLZC62M3nb1jvlCXi9dZTXKPca6yfTkCyzXGKzoEsemLP5u0Ot2Dq_JYDpiecfWzN9O9LNNX94uErIYzXOWVC9cN-t32hewCe0XjTKINBS6ggsTXjSsnoiKpzQA7IBQQUniDcOXViHS9QL7Wc_D3uvH7mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed16bd6292.mp4?token=nc4QAtVzzdEMnwpOWGCS7v18BpxdhYS13DhbkPf0dwEkVgr7lQs3sNmLE5GBssZVQt-X7V1lFWDT1A3DeT3Uv3lIrjfTOAjOj8iEnTD4l5jnABXrsh2uGe5LJbTE2AA4ovB5vAl-gr4nduuqHNLO6SAL_yAAVeLC7eD71B8Yli8E2dMemlZCBL8XjCBDCLZC62M3nb1jvlCXi9dZTXKPca6yfTkCyzXGKzoEsemLP5u0Ot2Dq_JYDpiecfWzN9O9LNNX94uErIYzXOWVC9cN-t32hewCe0XjTKINBS6ggsTXjSsnoiKpzQA7IBQQUniDcOXViHS9QL7Wc_D3uvH7mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الرياض تشتعل بعد هجوم للقوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/92342" target="_blank">📅 18:28 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92341">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مشاهد للحرائق في العاصمة السعودية الرياض</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/92341" target="_blank">📅 18:28 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92340">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8140b6c5d5.mp4?token=BvSwAf3LIoaZPfX4jANzLU6lz7TRT51MmQGIuyO6MOSOJ9vLnsxosSRbRSIveueI4kWiIYJFfi2Q4w0CnaAH5O2zLKdoYzjSCXklHezdxWhrKA9J7Tps1Ed28Eae6DpZU6mFfmcpUcu_-oRXpqhVUrJbtmq6JBqNJ6ZUe0mjWhBo8gewq0dnuSaIIaHjGPuwnpyiNaQ6thW0YX3MpNpxwMl29qtBf2sqqZJ2wCMfsvOxdKgmUbb27dJZglykNytMwqusH4cwVAArDyhLE66ST49THa1XuFs7X3wZp5xc978BGnPCRiRd_CzVUKBJPyw92c0wIBmu0w0E8HZGzDiVyEI7kpACrvXaG3cvPcrAXt3rXKL1BbJHEE_74lq4d0U23m0-nmf0C0YlRRb8O4ZE382V39um-HKnzgytVmS3ZzQtJ_8QyZoBDQ6DRkV9B4bbrrD5PlGSmyfejcbYNoFCYKWTGno5GNHdH_ZzzDrwWgkQD7ZYLD8ERGov1im42HDMUbwbCPYeOu7lLddXGB6f7Aa4Bcrs9EzuDrkiCzoehjSO23NpmtjQ0Ra8q72loh0VG_Vz0YTwMRMhdRgaDwAZIcePPYhOPgEaVQDFgqpd1kF5lpHgPs_1Xov1G4vq8baP6P_j7OmA8DrwSpDS6sDfYeo9Ygf_nDSnPby9TpKkwMs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8140b6c5d5.mp4?token=BvSwAf3LIoaZPfX4jANzLU6lz7TRT51MmQGIuyO6MOSOJ9vLnsxosSRbRSIveueI4kWiIYJFfi2Q4w0CnaAH5O2zLKdoYzjSCXklHezdxWhrKA9J7Tps1Ed28Eae6DpZU6mFfmcpUcu_-oRXpqhVUrJbtmq6JBqNJ6ZUe0mjWhBo8gewq0dnuSaIIaHjGPuwnpyiNaQ6thW0YX3MpNpxwMl29qtBf2sqqZJ2wCMfsvOxdKgmUbb27dJZglykNytMwqusH4cwVAArDyhLE66ST49THa1XuFs7X3wZp5xc978BGnPCRiRd_CzVUKBJPyw92c0wIBmu0w0E8HZGzDiVyEI7kpACrvXaG3cvPcrAXt3rXKL1BbJHEE_74lq4d0U23m0-nmf0C0YlRRb8O4ZE382V39um-HKnzgytVmS3ZzQtJ_8QyZoBDQ6DRkV9B4bbrrD5PlGSmyfejcbYNoFCYKWTGno5GNHdH_ZzzDrwWgkQD7ZYLD8ERGov1im42HDMUbwbCPYeOu7lLddXGB6f7Aa4Bcrs9EzuDrkiCzoehjSO23NpmtjQ0Ra8q72loh0VG_Vz0YTwMRMhdRgaDwAZIcePPYhOPgEaVQDFgqpd1kF5lpHgPs_1Xov1G4vq8baP6P_j7OmA8DrwSpDS6sDfYeo9Ygf_nDSnPby9TpKkwMs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العاصمة السعودية الرياض تحترق بعد هجوم للقوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/92340" target="_blank">📅 18:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92339">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92ab0c8c4e.mp4?token=k1gVigThzAE_KGUHmhKhpA3rcf1gdgYdaIbkq1pFwC9t1W7hOW2slgV9GKAd-scNJ0qWSbbcohjop0p4GvF1VjK_a3K8Wo2DkMHREH-sEUPgWdL2Yk7KcPBgzEWgmsdave0la667S41oU69IV1BZs5N--oe32sFlA4tGMFTkSOsoB2_vdX-DkhnGZVTCMMUVBKAdshoaed24CUWBjTUP8sgAFvUg4EtEKUXOmYs3Fwk_Eq8gDF6JJcHddJghhbqQjc2nQhgl2YLp_2GAqiR8HIcHcnfUPJ0IsQg22_ehgtJmGeCriRI5MHpiWtneosh4iCDP6JvAajoz8qB3h-URIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92ab0c8c4e.mp4?token=k1gVigThzAE_KGUHmhKhpA3rcf1gdgYdaIbkq1pFwC9t1W7hOW2slgV9GKAd-scNJ0qWSbbcohjop0p4GvF1VjK_a3K8Wo2DkMHREH-sEUPgWdL2Yk7KcPBgzEWgmsdave0la667S41oU69IV1BZs5N--oe32sFlA4tGMFTkSOsoB2_vdX-DkhnGZVTCMMUVBKAdshoaed24CUWBjTUP8sgAFvUg4EtEKUXOmYs3Fwk_Eq8gDF6JJcHddJghhbqQjc2nQhgl2YLp_2GAqiR8HIcHcnfUPJ0IsQg22_ehgtJmGeCriRI5MHpiWtneosh4iCDP6JvAajoz8qB3h-URIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العاصمة السعودية الرياض تحترق بعد هجوم للقوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/92339" target="_blank">📅 18:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92337">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfeNkJJwjiD3S_R97xp6xLQJMEsQexQ1xQLvyAwjRJBKQ8c2FegrN-vMCKjUjgNMyPK4-vyHdKOK_JPQdKCX9KDw1gkMoxIrSZFWJLAPOukbQHK8tqn0YAY2VkTP8hGC5_zgQHO6bM7h9AblPk6tAlselmY7yZUMg0wU3Q3yyI5glr1Kkq3RCB3LIf3tKi3Xq63nkTvo-FYarXRlPgGd4nQU3b19uUOktUJjWF11G4qwS4syoSAVtZOhrs2qBXFLXJB-Kkvg20KfgNibrRAFK5zLTG7SFgSFPiZJysL3CK7890URY4-NlqSgL3oECm5LRTzcsBJawCuy4xtB0VXHWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐖
🇺🇸
ترامب:
أوروبا وافقت للتو على إطلاق كمية هائلة من مخزونها الكبير من زيت الديزل. وستبدأ هذه العملية على الفور.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/92337" target="_blank">📅 17:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92336">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">إصابة ناقلة نفط ترفع علم بنما بمقذوف وتصاعد أعمدة الدخان منها أثناء مرورها عبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/92336" target="_blank">📅 17:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92335">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔻
مصدر يمني لنايا:
طيران العدو السعودي يبدأ بنقل جثامين وجرحى الجيش السعودي عقب استهداف مقر التحالف في عدن من قبل القوات المسلحة اليمنية بالصواريخ والمسيرات مما خلف 17 قتيلًا وجريحًا سعوديًا</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/92335" target="_blank">📅 16:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92334">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c980ec8562.mp4?token=CEqQ0RFTZK_Su9QhmZBXfT25oiPxuG03PLkkLcD1ZcFQB21l3M9Ny6me_WNYkmuNh7UQDPnyfC36lj0j-6kbvAov0A_oF6MgBZNLQEXcgnzvR4bZIVj0YZ2gr35Z7lxoQuupfSlcRR59n4Vp8dg6FgprQiR9wfxLW16fWt7N9pZ2onZ0eNhkwTaj7gCPl46BPJ-Ln0FLp3e-x1U8LyqXZB85mkDMgQMZGl8AiK07dqCMT43HUPWrb37kxo2Zcelt19PiMBh_BxGTyxkS3q5cmfw4wMjSkiyaRAdQRN3e2UF7ZKNJFiJ6tQbiLrMrh4hf1VMjjRGcZt7QC_YzUAgH5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c980ec8562.mp4?token=CEqQ0RFTZK_Su9QhmZBXfT25oiPxuG03PLkkLcD1ZcFQB21l3M9Ny6me_WNYkmuNh7UQDPnyfC36lj0j-6kbvAov0A_oF6MgBZNLQEXcgnzvR4bZIVj0YZ2gr35Z7lxoQuupfSlcRR59n4Vp8dg6FgprQiR9wfxLW16fWt7N9pZ2onZ0eNhkwTaj7gCPl46BPJ-Ln0FLp3e-x1U8LyqXZB85mkDMgQMZGl8AiK07dqCMT43HUPWrb37kxo2Zcelt19PiMBh_BxGTyxkS3q5cmfw4wMjSkiyaRAdQRN3e2UF7ZKNJFiJ6tQbiLrMrh4hf1VMjjRGcZt7QC_YzUAgH5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استعراض جوي كبير لمروحيات الجيش العراقي في سماء العاصمة بغداد</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/92334" target="_blank">📅 16:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92333">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نتنياهو: كلما مر الوقت، تتضح الصورة، والمنفذ تبين أنه متطرف إسلامي. لقد جاء لتفجير الطائرة وركابها. نحن بصدد التحقيق لمعرفة ما إذا كان قد أُرسل، وكل من أرسله سيدفع ثمنًا باهظًا للغاية</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/92333" target="_blank">📅 16:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92332">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نتنياهو:
كلما مر الوقت، تتضح الصورة، والمنفذ تبين أنه متطرف إسلامي. لقد جاء لتفجير الطائرة وركابها. نحن بصدد التحقيق لمعرفة ما إذا كان قد أُرسل، وكل من أرسله سيدفع ثمنًا باهظًا للغاية</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/92332" target="_blank">📅 16:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92331">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10465af39b.mp4?token=Y_u3UUwcBUUG2zWcResdIu7yDB5ewKrl7LBuCURpN6yyIWEN2yNEcAFeEZ0Oym4X8fASSsYA_t3dkoAdu9rI3jnIP__OhwZxGcTX64A9658rxG2yTgv-hEp-4xHr7TKDbVBPX_Sd1q7IzcdTqM6oFuBTUWYzbPegzRTkLacBIGhErmsiOUA8rXi4-Pez69Tn977U9epwCpg5Ch3Z82quTWtPN1zMfM-05yum87vPfzZbHWDZwy3SPmIoyEL9eQSqOziLL55IQQwhcvDbk1z47DMdHOr12cA3sctjfTHt0LeWW5nYa9_rl9SLLdgHvtbQIh3LfjWNdd_RbfQHDzB4BGuAMYIeVHd9cBP3RhwdeH8xGYPh_ODi9QX2JVqo0_2utVU0JQ8afemCfKdMRQ6e-GOHo56k_e5li5o6zYBEjDmmvH3aDJWvL5AET0Syvq5Qz4JAkvHgFjVXTPGYMHyeOOGQShxhak5efQ1Vs6VgIKXI76iEDAxYhQikFb_z8Zxn-jHpj7qja8idIDIwsFlKHJjaRte0faLeSb7EcrusfWDsjdK1jYMkcxIoCdR7qQuSMZBQXoY5guHM7HK_k2PxCCNxtZVN_kMllbp3bKOKwJDNMVFnEBD8LkmqkLxlpktIFSL3dFad75RutnQmQEEfCj30MzxdyXAf20BWHTZRMsU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10465af39b.mp4?token=Y_u3UUwcBUUG2zWcResdIu7yDB5ewKrl7LBuCURpN6yyIWEN2yNEcAFeEZ0Oym4X8fASSsYA_t3dkoAdu9rI3jnIP__OhwZxGcTX64A9658rxG2yTgv-hEp-4xHr7TKDbVBPX_Sd1q7IzcdTqM6oFuBTUWYzbPegzRTkLacBIGhErmsiOUA8rXi4-Pez69Tn977U9epwCpg5Ch3Z82quTWtPN1zMfM-05yum87vPfzZbHWDZwy3SPmIoyEL9eQSqOziLL55IQQwhcvDbk1z47DMdHOr12cA3sctjfTHt0LeWW5nYa9_rl9SLLdgHvtbQIh3LfjWNdd_RbfQHDzB4BGuAMYIeVHd9cBP3RhwdeH8xGYPh_ODi9QX2JVqo0_2utVU0JQ8afemCfKdMRQ6e-GOHo56k_e5li5o6zYBEjDmmvH3aDJWvL5AET0Syvq5Qz4JAkvHgFjVXTPGYMHyeOOGQShxhak5efQ1Vs6VgIKXI76iEDAxYhQikFb_z8Zxn-jHpj7qja8idIDIwsFlKHJjaRte0faLeSb7EcrusfWDsjdK1jYMkcxIoCdR7qQuSMZBQXoY5guHM7HK_k2PxCCNxtZVN_kMllbp3bKOKwJDNMVFnEBD8LkmqkLxlpktIFSL3dFad75RutnQmQEEfCj30MzxdyXAf20BWHTZRMsU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسراب كبيرة من طائرات الهيلكوبتر العراقية تستعرض في سماء العاصمة بغداد</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/92331" target="_blank">📅 16:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92330">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc43b2c991.mp4?token=dLm_X_Byi0LAJuhSR6PRKewFDmbBKaiRxoayqMtz0PdZ3XW2hUOs25eblQmJvOUx8JlgUVgv8M2w_3Iu8grkPPuqZi-V-2UGiztUEUVMdSQGsjHnxTH9XTgzwfnemkb4nSDymaZ5ZK0UMXyEbcBu1a2Q3CPd3J6FDnUD1bUETauRz88JP40HpkOdNPweRdRCPsFL-iDTmVPRh8ywZh-1L53IS9mwCs6L2fU20ZB4EYj6BihtdH4J8QRPnm2cdgCFdF49kCpqvtDgDUp_HjCz5LbBScwWGu0n3O_bdlvVkNWVpaH0V-JNNvx1Qw4au5SOfMBpdYDF_vUdU7Sje5n9MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc43b2c991.mp4?token=dLm_X_Byi0LAJuhSR6PRKewFDmbBKaiRxoayqMtz0PdZ3XW2hUOs25eblQmJvOUx8JlgUVgv8M2w_3Iu8grkPPuqZi-V-2UGiztUEUVMdSQGsjHnxTH9XTgzwfnemkb4nSDymaZ5ZK0UMXyEbcBu1a2Q3CPd3J6FDnUD1bUETauRz88JP40HpkOdNPweRdRCPsFL-iDTmVPRh8ywZh-1L53IS9mwCs6L2fU20ZB4EYj6BihtdH4J8QRPnm2cdgCFdF49kCpqvtDgDUp_HjCz5LbBScwWGu0n3O_bdlvVkNWVpaH0V-JNNvx1Qw4au5SOfMBpdYDF_vUdU7Sje5n9MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسراب كبيرة من طائرات الهيلكوبتر العراقية تستعرض في سماء العاصمة بغداد</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/92330" target="_blank">📅 16:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92329">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">المرجع الديني جواد الخالصي يطالب باستعادة أموال العراق واستقلال قراره: لا خضوع للإملاءات الأجنبية ولا حياد بين الحق والباطل</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/92329" target="_blank">📅 16:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92327">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9479b284ba.mp4?token=Z_ardiKbRytr4XWLRMJ6nS2SVtZRQCeBB_0nb6hVJYUiOOVK1I6DlXaUNC2ewbilsDPdKHbqQyEy0pislWGXRsudU2sg4pnMD-C93lIb3LcxaSM-a2zb1j6-Afnvjew5P-FbWpPA6EWpv5fTEAK-lxvTPCp6wkrCq1lvkCsngSnxp3SDs5V-6UPdT-gFKLA5zoFgGwoS7zxXQ-tu9pkKwJ11QgcfMldeG-UNA5JblztHlQ2hg2WgjdKPWzTgReP57efZbPpkeo5Rv9KknZCcTSuwr1RebnoULDWCFh1wKoI18yDztbP5hKEL16bwFs5XBCh-hAkxros5WmgO3OuGzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9479b284ba.mp4?token=Z_ardiKbRytr4XWLRMJ6nS2SVtZRQCeBB_0nb6hVJYUiOOVK1I6DlXaUNC2ewbilsDPdKHbqQyEy0pislWGXRsudU2sg4pnMD-C93lIb3LcxaSM-a2zb1j6-Afnvjew5P-FbWpPA6EWpv5fTEAK-lxvTPCp6wkrCq1lvkCsngSnxp3SDs5V-6UPdT-gFKLA5zoFgGwoS7zxXQ-tu9pkKwJ11QgcfMldeG-UNA5JblztHlQ2hg2WgjdKPWzTgReP57efZbPpkeo5Rv9KknZCcTSuwr1RebnoULDWCFh1wKoI18yDztbP5hKEL16bwFs5XBCh-hAkxros5WmgO3OuGzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توترات في مدينة الحسكة السورية: الاكراد يرفعون رايات كردية والعرب يرفعون رايات تنظيم داعش وسط مخاوف من التصادم فيما بينهم خلال الدقائق المقبلة وخروج المدينة عن السيطرة</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/92327" target="_blank">📅 15:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92326">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngArDXOu7oOjsAc9h4qZP9KvVgBhcvj0lw2IuPYPzzQwJi-cwmFu3kAyaIH-k1WNx1kh2NpMI_FMjYK9N0nqcVjW33_kHOFQ89NPSWSmGZZml3agkxdWIpi1i9RNDUD-RvdaHoJfQf2UpIjuroHKswebbn9wqmEbW1ZGHTNLcRGNiN4b6hI5V5P8Wbos2YH9dYcH57FrXsoiorgN1aQGo_VHI-o8P2hBDOcQLBAvwAChrMFFmtC7MYqpNZTPwBgdZUK7BfMXtd2BLghtYRo8T10kvlFY2ih3kqbFrwlcLzO8jyrgy5eUymG2hQnd1a9oYLRWRKezb5UdFYCDRAiuEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
جهاز مكافحة الارهاب يوضح بخصوص عملية التون كوبري: يوضح الجهاز أن العملية جاءت في إطار واجبه الوطني في ملاحقة العناصر الإرهابية وإحباط مخططاتها الرامية إلى استهداف المواطنين وتهديد أمنهم وسلامتهم تمكنت قوة من الجهاز من ملاحقة عنصرين إرهابيين في إحدى المناطق…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/92326" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92325">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇶
القضاء العراقي: السجن 7 سنوات بحق النائبة عالية نصيف بعد ادانتها بتهم فساد</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/92325" target="_blank">📅 13:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92324">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇷
إشتباكات بين القوات الأمنية وعناصر إرهابية في مدينة راسك جنوب شرق إيران؛ مقتل عدد من الإرهابيين كحصيلة أولية.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/92324" target="_blank">📅 11:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92321">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c4622935e.mp4?token=kMbR9mCKAOkprJiw0DE3gOUxiwm1fh9ebejrNSaAAgCWTG3q8Qn8fIgVmj4mw18Ru3d4fu_SBaEndELLrMvoZ72EF_5g7TNS-ZXlbGu66AtcrT9-YNpxzVMxUuQuTzgdt_JS6VL6WLmCma8wK80d1KiRcUtEzI0a3Xw2fyvUAoVfeS2ZILuGgnNXSISgvl-Ipyhti_7M5ujvMbldEEdd3Z6TU-yxYWPpfyvoqor4ufC_ZfNgDZXrkIr3UzDlQ9lUIhiE6JuFoHXITdFthjkzWeP6wFEY1KU4FeEqHMYIsYYW7G86OfZnnpWV3zSZ3rcoSPOCbXXuidBPSZejQc_HYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c4622935e.mp4?token=kMbR9mCKAOkprJiw0DE3gOUxiwm1fh9ebejrNSaAAgCWTG3q8Qn8fIgVmj4mw18Ru3d4fu_SBaEndELLrMvoZ72EF_5g7TNS-ZXlbGu66AtcrT9-YNpxzVMxUuQuTzgdt_JS6VL6WLmCma8wK80d1KiRcUtEzI0a3Xw2fyvUAoVfeS2ZILuGgnNXSISgvl-Ipyhti_7M5ujvMbldEEdd3Z6TU-yxYWPpfyvoqor4ufC_ZfNgDZXrkIr3UzDlQ9lUIhiE6JuFoHXITdFthjkzWeP6wFEY1KU4FeEqHMYIsYYW7G86OfZnnpWV3zSZ3rcoSPOCbXXuidBPSZejQc_HYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
طيران القوة الجوية يستعرض في سماء العاصمة بغداد ومدن عراقية أخرى بمناسبة طرد القوات الأمريكية من العراق.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/92321" target="_blank">📅 11:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92320">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e49c4705d.mp4?token=H-6HkbRhc2u7NTo8k-ikJFdIOYo2FbtZvDhwJivBoBukeazvPkvviJE2cksM_W-yRw09R496E7rqhRCUGe7E0CXw2OPx3-ibDwpC4XG7O2qC3SSaPjlWFye-lchm2MyjS4YP1Ha-xnQ6LW5Y7TmBV6XuYWHKWtXINHUjE52KGbJPvhEXFSjNRs1uDlrW5VPf2XKRmFCU1GaknqLvFwub5WeTCL1UdFqA0Y0QtWZkLCLNxrdr8hgW08w53Zu0Q-Vdu6LiWJ7IBvz28mmMNsHbYj1k0hlpOKQ8lQbocKmmOVBzQkTtkOTWVOEysDUdrgl0F5IG06-Hln377fdHEfieTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e49c4705d.mp4?token=H-6HkbRhc2u7NTo8k-ikJFdIOYo2FbtZvDhwJivBoBukeazvPkvviJE2cksM_W-yRw09R496E7rqhRCUGe7E0CXw2OPx3-ibDwpC4XG7O2qC3SSaPjlWFye-lchm2MyjS4YP1Ha-xnQ6LW5Y7TmBV6XuYWHKWtXINHUjE52KGbJPvhEXFSjNRs1uDlrW5VPf2XKRmFCU1GaknqLvFwub5WeTCL1UdFqA0Y0QtWZkLCLNxrdr8hgW08w53Zu0Q-Vdu6LiWJ7IBvz28mmMNsHbYj1k0hlpOKQ8lQbocKmmOVBzQkTtkOTWVOEysDUdrgl0F5IG06-Hln377fdHEfieTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب حول إيران:
كانوا يتعاملون بالمخدرات، ولكنهم كانوا أيضًا يجرون تجارب نووية. ولكن هذه المصانع التي تنتج المخدرات، وهذه المصانع النووية، تعرضت لضربات قوية للغاية.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/92320" target="_blank">📅 10:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92319">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/888df7398e.mp4?token=SYZkyA7kSxm-mvQoSE-3X9Ssq_8MCTKvFDqhErJcSZHNTP8IVAkl_17XBdiQ04gyXCHypv6c1PcmmB12674mV4NbyLlw9s8vBGGwdaNo6jwmB5N-SzHesKL35obqEDZVWorcS7CQWdrCVqHU0Qchvy39U4689CgMlo9eh-bAJkMOomE0ZaeJh-_DlJw2_-O075819gNq__geB-0dhDYXbrdRm1iqbFeF_i321isBS6CWQmiNpiRIMCQT_lqN_P_8l9-EFdRZZm1Eh-LH9el-_rM6ObjRuj36EQ4ZJj80sCL8iOuwq5M0ATY0v-RA7UBbK131UbaHo5kMFzC9fxTLVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/888df7398e.mp4?token=SYZkyA7kSxm-mvQoSE-3X9Ssq_8MCTKvFDqhErJcSZHNTP8IVAkl_17XBdiQ04gyXCHypv6c1PcmmB12674mV4NbyLlw9s8vBGGwdaNo6jwmB5N-SzHesKL35obqEDZVWorcS7CQWdrCVqHU0Qchvy39U4689CgMlo9eh-bAJkMOomE0ZaeJh-_DlJw2_-O075819gNq__geB-0dhDYXbrdRm1iqbFeF_i321isBS6CWQmiNpiRIMCQT_lqN_P_8l9-EFdRZZm1Eh-LH9el-_rM6ObjRuj36EQ4ZJj80sCL8iOuwq5M0ATY0v-RA7UBbK131UbaHo5kMFzC9fxTLVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
إعلام العدو:
تحطم طائرة إسرائيلية خفيفة في منطقة وادي عارة جنوبي حيفا؛ مقتل الطيار وإصابة أخر كحصيلة أولية.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/92319" target="_blank">📅 09:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92318">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b61da074c.mp4?token=TyN9UbXcYGY1sVYd9wU8rp2aJlieVNVccXn4XglTy6x5qSwvAkD1BryngW0u_DC0f546P8g77CD8DCsipy8HhAB-QR6UjZ3F-DhWyLi96imFKE_4um_aT6tY4gWuptsNPTeErKFAsDKIOe8lwFH-CDx2b9Mcc8eR-yy8oz7qP9pZXeeQju8s3-aK2LKYZOVa4Z31BeVvNHL_120emW7-25mIqQw0ou4c3IDwOrZf_R1uewVtzXawFeAtZtEWSn4sBDDjPTO321a2Vyb7-ImOD5ybsMQbBky07Df5KWSHCyBgVZbwha9SzE0nc9RN_KQSHkvjw3ee6PLtMpadStCmXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b61da074c.mp4?token=TyN9UbXcYGY1sVYd9wU8rp2aJlieVNVccXn4XglTy6x5qSwvAkD1BryngW0u_DC0f546P8g77CD8DCsipy8HhAB-QR6UjZ3F-DhWyLi96imFKE_4um_aT6tY4gWuptsNPTeErKFAsDKIOe8lwFH-CDx2b9Mcc8eR-yy8oz7qP9pZXeeQju8s3-aK2LKYZOVa4Z31BeVvNHL_120emW7-25mIqQw0ou4c3IDwOrZf_R1uewVtzXawFeAtZtEWSn4sBDDjPTO321a2Vyb7-ImOD5ybsMQbBky07Df5KWSHCyBgVZbwha9SzE0nc9RN_KQSHkvjw3ee6PLtMpadStCmXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ثاني يهز مطار تفتناز العسكري في ريف محافظة إدلب السورية.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/92318" target="_blank">📅 09:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92317">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔻
إنفجار ضخم مجهول وتصاعد أعمدة الدخان من مطار تفتناز العسكري في محافظة إدلب السورية.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/92317" target="_blank">📅 09:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92316">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb911b96c5.mp4?token=qHWAWcUeNyBZRXKFxcXBuZI3ObHGHiiY5dS6A3XTvVUVqq7zR8kHuhlysEeDOyv5RpiRvDV6pOGMIeN1xt7irfW8yDMmigaKF5JsCc2pqsnkXf9DbBAO9kHIxdIYv6kWPfNUTqI5jaRaLvMvWY8a3_CFF5vq1Jd00xvTpDruJ-pRDR6j7ocmy6A4TWUmZysQZ2G0-rVl-4cceRm8CjuXzkU8nW03B9ydSrfidE1fUWBA3ttFnLnUAJ9U6037m0tr2oenfTu2GzX3uei3Y6MPivpCPehYGTBYy83KlVbrBXKyaNRCP4jGbHWJHRnQMpT6zn_17R7kcsSObX_aGKo67w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb911b96c5.mp4?token=qHWAWcUeNyBZRXKFxcXBuZI3ObHGHiiY5dS6A3XTvVUVqq7zR8kHuhlysEeDOyv5RpiRvDV6pOGMIeN1xt7irfW8yDMmigaKF5JsCc2pqsnkXf9DbBAO9kHIxdIYv6kWPfNUTqI5jaRaLvMvWY8a3_CFF5vq1Jd00xvTpDruJ-pRDR6j7ocmy6A4TWUmZysQZ2G0-rVl-4cceRm8CjuXzkU8nW03B9ydSrfidE1fUWBA3ttFnLnUAJ9U6037m0tr2oenfTu2GzX3uei3Y6MPivpCPehYGTBYy83KlVbrBXKyaNRCP4jGbHWJHRnQMpT6zn_17R7kcsSObX_aGKo67w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
إنفجار ضخم مجهول وتصاعد أعمدة الدخان من مطار تفتناز العسكري في محافظة إدلب السورية.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/92316" target="_blank">📅 09:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92315">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edffd6bce5.mp4?token=mFKLEBahDLsAtaI1a6YrB-Ge8UCuKOfQOEXm3meHNVq-FY3mLYX7_8_jgR22ThOqmoOXE2UrFip7816qvPl2nfue2DZzAZ-KFlF9GWsyius_gvpf_hdPGpmQV_WBsC0mQ5dnv4GgGpjGvqHFSdT2OikhGQ5n6dSHlMOdh1YxqNb56pNEnhVQkZWY7nvSZK77aBrMgkrCnM4Y0rjf7W9wYEH0GwJ_P1RitekabBFNq7lqO1rbIda32ATTLhtid10jj1mg8HjbfNJG11nRqbJq6dSxPt1nVAd1y_36p_mj91QtuoUrUqvDILo_83rw-OX8ViOWW071FCGvKnC9mPZesQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edffd6bce5.mp4?token=mFKLEBahDLsAtaI1a6YrB-Ge8UCuKOfQOEXm3meHNVq-FY3mLYX7_8_jgR22ThOqmoOXE2UrFip7816qvPl2nfue2DZzAZ-KFlF9GWsyius_gvpf_hdPGpmQV_WBsC0mQ5dnv4GgGpjGvqHFSdT2OikhGQ5n6dSHlMOdh1YxqNb56pNEnhVQkZWY7nvSZK77aBrMgkrCnM4Y0rjf7W9wYEH0GwJ_P1RitekabBFNq7lqO1rbIda32ATTLhtid10jj1mg8HjbfNJG11nRqbJq6dSxPt1nVAd1y_36p_mj91QtuoUrUqvDILo_83rw-OX8ViOWW071FCGvKnC9mPZesQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف مستمر لتحشيدات مرتزقة التحالف من قبل القوات المسلحة اليمنية في عدن</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/92315" target="_blank">📅 04:41 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92314">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c39cddb5e2.mp4?token=EVIlyPnjLSiwpW5-Iw51m14QuEZbXXa4XGRW65mv_N60Nj_xYNE7F0kUYUaOcYcddheqlUJChpOc3gUaIcrMkxBaO5b82tHZBKzJn7XRokbofBfr9g7JYLiKzyK0sAfPTiMcFN42f4z_zjZbp-5v0f8M0sRmg_jkWmem4tZUV6nB7KWJJ2xK4GhzBf9UznbIS5q2X_GfND34QfbABu-MVoXDpQLHllyRcOttwo25sGWstMy1Lsws5ykuPwF_BY0bJvaqKZ8LNjIsaYr2Gd31BroKVmZCqXtmwIrS5ts3gSc-Cg7I9BMgxd_1MO0hpMuIaFxJUd49ciNMtimGW9cp0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c39cddb5e2.mp4?token=EVIlyPnjLSiwpW5-Iw51m14QuEZbXXa4XGRW65mv_N60Nj_xYNE7F0kUYUaOcYcddheqlUJChpOc3gUaIcrMkxBaO5b82tHZBKzJn7XRokbofBfr9g7JYLiKzyK0sAfPTiMcFN42f4z_zjZbp-5v0f8M0sRmg_jkWmem4tZUV6nB7KWJJ2xK4GhzBf9UznbIS5q2X_GfND34QfbABu-MVoXDpQLHllyRcOttwo25sGWstMy1Lsws5ykuPwF_BY0bJvaqKZ8LNjIsaYr2Gd31BroKVmZCqXtmwIrS5ts3gSc-Cg7I9BMgxd_1MO0hpMuIaFxJUd49ciNMtimGW9cp0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اللحظات الاولى لاستهداف مرتزقة قوات التحالف في في عدن</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/92314" target="_blank">📅 04:28 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92313">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">إعلام أجنبي:أرسلت الولايات المتحدة مؤخراً بطاريتين إضافيتين من صواريخ "باتريوت" لحماية منشآت حيوية للنفط والغاز في كل من السعودية وقطر، وذلك في ظل احتمالية شن ضربات أمريكية جديدة ضد إيران.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/92313" target="_blank">📅 04:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92312">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f52287c44.mp4?token=cJD-5agBBDw1SYTEoFFYmMzC7yKUjtscUR-QaUlMVDk0Ej4CPqGby6d_BCob9SEd6W9YaN6raPcy74zW-3gt8JjxJ8gVej3zEEi6Ywv7Axhf0isMTBeB0QrI1E8zmxJE-KOx5jkj0desG7Zgeq6qT_PJLea2B3TWabikVZox0msK7Ng7-Uug88xM_kX20zGZn_6dxIjejb78NejCk5y2DttocmcrLa8Npvo-34Ml_z-fl7WYKWx2V4lK0jnHQLcxCxs_jtZd2_ONKZguaqMdntt-9E__jk-K1FGCyZ3dDvyj44otui5yXQftLShxOMt16BWx3bA9T_E-RMt8eLshhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f52287c44.mp4?token=cJD-5agBBDw1SYTEoFFYmMzC7yKUjtscUR-QaUlMVDk0Ej4CPqGby6d_BCob9SEd6W9YaN6raPcy74zW-3gt8JjxJ8gVej3zEEi6Ywv7Axhf0isMTBeB0QrI1E8zmxJE-KOx5jkj0desG7Zgeq6qT_PJLea2B3TWabikVZox0msK7Ng7-Uug88xM_kX20zGZn_6dxIjejb78NejCk5y2DttocmcrLa8Npvo-34Ml_z-fl7WYKWx2V4lK0jnHQLcxCxs_jtZd2_ONKZguaqMdntt-9E__jk-K1FGCyZ3dDvyj44otui5yXQftLShxOMt16BWx3bA9T_E-RMt8eLshhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات مستمرة داخل معسكر قوات المرتزقة السعودية في عدن</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/92312" target="_blank">📅 04:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92311">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">قوات التحالف السعودية تعلن اعتراض صاروخ باليستي أطلقه انصار الله باتجاه خميس مشيط.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/92311" target="_blank">📅 03:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92310">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73d8b51349.mp4?token=QA8s6Pw5Ly8IaHIgqXGDx4xE9HBpvmUvjuafGe8MGBsM7qqDn52TJHWDJ9tvqtMi8WrSJSpHrh3RXN0n8kcsGglxHqci2WvECz6EJXc-6HyE2AO_KTGWtDq4eHLXkux7zDz7k0xUCIE7NnCkNMX2-3ew7y7X_xPRZzhelq21DfKTHYvdQPGAiQfnWuIXrEA1JFvJdTHTvFuZIFQqRBwBWGDUaTRFy0L1xMA_lMUiOmWUw4EcmZteLqa7B0kl1p0_3uU7Q23_mZi0_BVrTFpehwydsjbtIiZcf9L7P3-heiB7dqGf1gqu-Vs5i3PRu8IUKMMICIjG5FYzvvqfKyfefQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73d8b51349.mp4?token=QA8s6Pw5Ly8IaHIgqXGDx4xE9HBpvmUvjuafGe8MGBsM7qqDn52TJHWDJ9tvqtMi8WrSJSpHrh3RXN0n8kcsGglxHqci2WvECz6EJXc-6HyE2AO_KTGWtDq4eHLXkux7zDz7k0xUCIE7NnCkNMX2-3ew7y7X_xPRZzhelq21DfKTHYvdQPGAiQfnWuIXrEA1JFvJdTHTvFuZIFQqRBwBWGDUaTRFy0L1xMA_lMUiOmWUw4EcmZteLqa7B0kl1p0_3uU7Q23_mZi0_BVrTFpehwydsjbtIiZcf9L7P3-heiB7dqGf1gqu-Vs5i3PRu8IUKMMICIjG5FYzvvqfKyfefQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات مستمرة داخل معسكر قوات المرتزقة السعودية في عدن</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/92310" target="_blank">📅 03:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92309">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c47ccb5bca.mp4?token=jeL5BqbjGLcm_YTW6Ku9yewk8W0elDHadOJ1bTKsUdkd0QlsWW5tavFv3VanipDMRH520wbrcjRCnPsJeqKxrLEdHUjWyYsISJrLqpR4YMM40WuxXcMqjQjwt9Iq7bhhbzrwZ_dx5i7ZtS-fZCCT0xAX06Ugwb-s66T2ICChCRC7cKf6SR7Z1cJgEX95DL7olX57eHiRayG95JWRHJkEIXMqpfycuTi82sxdZBmL9nBes1UXEQqgOrNCMtZx3FwqnyhPWFUXqodv_Q6ekFIbLTGEUS8fVHG_tyeS6nsiYp8KLaSz7hjdOj3A9frDVXm1sFl8nJ5AAs8jj3Ji8c_nqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c47ccb5bca.mp4?token=jeL5BqbjGLcm_YTW6Ku9yewk8W0elDHadOJ1bTKsUdkd0QlsWW5tavFv3VanipDMRH520wbrcjRCnPsJeqKxrLEdHUjWyYsISJrLqpR4YMM40WuxXcMqjQjwt9Iq7bhhbzrwZ_dx5i7ZtS-fZCCT0xAX06Ugwb-s66T2ICChCRC7cKf6SR7Z1cJgEX95DL7olX57eHiRayG95JWRHJkEIXMqpfycuTi82sxdZBmL9nBes1UXEQqgOrNCMtZx3FwqnyhPWFUXqodv_Q6ekFIbLTGEUS8fVHG_tyeS6nsiYp8KLaSz7hjdOj3A9frDVXm1sFl8nJ5AAs8jj3Ji8c_nqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات مستمرة داخل معسكر قوات المرتزقة السعودية في عدن</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/92309" target="_blank">📅 03:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92307">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02a01896a2.mp4?token=WiHi63Y6PKvZ0enCcByMaK-MM6I_jZoUcYyEvRBecta_BlnystZW2h4ZfE4gqrp52-vOesjTSJV1rlYCtqgOFT6xADhg5UiTpu28yhjlBqz1ewdkUHA-wjvhoebEjzFkagvuUht_Y7_JxzsRhzDrGN4sbJPNm6KLsd4TNJtrvS_BaC13tOioX7dZUx4E3-PUxBfy0cZLtzTrDzAuN1znlKdCH5cWUz0KQjriqIrJK5pmqEEEfXyAmI23dvcmEv34lUOdrNFBZYKCtVsUWJcKTxaaekWVVBeC6hopxG2eHPwkMYHgzHbcUxdkR8Usk1-PO9HVxgvQqth2sLB1lZORNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02a01896a2.mp4?token=WiHi63Y6PKvZ0enCcByMaK-MM6I_jZoUcYyEvRBecta_BlnystZW2h4ZfE4gqrp52-vOesjTSJV1rlYCtqgOFT6xADhg5UiTpu28yhjlBqz1ewdkUHA-wjvhoebEjzFkagvuUht_Y7_JxzsRhzDrGN4sbJPNm6KLsd4TNJtrvS_BaC13tOioX7dZUx4E3-PUxBfy0cZLtzTrDzAuN1znlKdCH5cWUz0KQjriqIrJK5pmqEEEfXyAmI23dvcmEv34lUOdrNFBZYKCtVsUWJcKTxaaekWVVBeC6hopxG2eHPwkMYHgzHbcUxdkR8Usk1-PO9HVxgvQqth2sLB1lZORNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من استهداف القوات المسلحة اليمنية لمواقع مرتزقة التحالف السعودي في عدن</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/92307" target="_blank">📅 03:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92306">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇸🇦
مشاهد أخرى من الحرم المكي تُظهر إبعاد الحجاج عن شخص يُشتبه بحيازته مواد متفجرة.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/92306" target="_blank">📅 02:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92305">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LINjMDnJGXbzNLIOvCCfgt6v5wDDUtt6O_6UAfCS4-3btMP__Fs_WHG4kJ0wHbOM2WuX1vcLUJ5YX9qbtCsiGpEvCJlYrHGigyVI7_tX9d_U2fu5eCFsCw2QUy3vabXk3qKmtgJjDze7i1-_uzin2RyQmZj0k6iRahddxNw5bz4NhL0GopcNshUZsmpRQ7GB_iZRYMfS3iu-xT9O8rPNRMg07mmrvP7hbTXmFT0xg4rUBxN7rARAnCdpWvriobst1Z33fltUBfpOppTDhg1vGKhejoSmUH7JkisWHFlfuEzOqKZUO4AVnN7VvZnRredSdT3C7k--z19uoaALobGROA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد الرياض،توقف حركة الرحلات الجوية في الدمام شرق السعودية</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/92305" target="_blank">📅 02:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92304">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ec9b5c12.mp4?token=CKI2Gc0FLe7bmfP-ZXdiaApzkUfaD_yinylf-be_f866F8hDlIBdRUgVcVi8lZ5LpP6HMF5JNoOw3AAQzDarh3PqeKYpejwcKc7wQHHCI-OzslI0O6hOWoZyqMy2X6kJDaS12DcTUD2N5Qi9WrgmHn80LHT97gY3L4sFvdpoRISbSacIagM90SuUdrhm945NsHZmNwJRX6jxRqLjS-ZVmh8OOlmWafGbKWYJ99G_wbmGO7XEtMiyZ0fYvM96zKJxetDXsWbJf7lhLsjkIq6bh6gC13v4sU4PoPs19JnXvf0P6uX27wbGE2Qi1nDCllOQQ-e9zuiSq_xGo6Lb-q2ebg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ec9b5c12.mp4?token=CKI2Gc0FLe7bmfP-ZXdiaApzkUfaD_yinylf-be_f866F8hDlIBdRUgVcVi8lZ5LpP6HMF5JNoOw3AAQzDarh3PqeKYpejwcKc7wQHHCI-OzslI0O6hOWoZyqMy2X6kJDaS12DcTUD2N5Qi9WrgmHn80LHT97gY3L4sFvdpoRISbSacIagM90SuUdrhm945NsHZmNwJRX6jxRqLjS-ZVmh8OOlmWafGbKWYJ99G_wbmGO7XEtMiyZ0fYvM96zKJxetDXsWbJf7lhLsjkIq6bh6gC13v4sU4PoPs19JnXvf0P6uX27wbGE2Qi1nDCllOQQ-e9zuiSq_xGo6Lb-q2ebg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب عن إيران:  إيران مستعدة للاستسلام. سنحقق الفوز بسهولة بالغة في الوقت الراهن</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/92304" target="_blank">📅 01:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92303">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff0492e588.mp4?token=VraEsP2XYETZo6dlJm5NkTeMeHlxo5N-mPdP448g1shEIJLJnb_yuMotGKwse88kgQhIebpxsZr9nBazivk4NZGBW2k0Gip4oeTztqwkANkF_VirfPzGopWk-MVV-97cc504c6WNgEVBmAKQgVVWBEWNOw03J70icCeUsUT3nDwxKfGqWoMLnYds2uPVDpa9d8xVNpQ5nNlMeotVxEFo5jldd3W-_zmqg0cZkrM-a_WlLg5qTK3uzMuAH7DNzHyNG1DLBr-JLCUcaI5UOZd2SWW2zWtEPdOn-2gNWOX8jwP2SKJaK9LbK5QS3__bR865Ieyhdj3S98DNCxBkO-plzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff0492e588.mp4?token=VraEsP2XYETZo6dlJm5NkTeMeHlxo5N-mPdP448g1shEIJLJnb_yuMotGKwse88kgQhIebpxsZr9nBazivk4NZGBW2k0Gip4oeTztqwkANkF_VirfPzGopWk-MVV-97cc504c6WNgEVBmAKQgVVWBEWNOw03J70icCeUsUT3nDwxKfGqWoMLnYds2uPVDpa9d8xVNpQ5nNlMeotVxEFo5jldd3W-_zmqg0cZkrM-a_WlLg5qTK3uzMuAH7DNzHyNG1DLBr-JLCUcaI5UOZd2SWW2zWtEPdOn-2gNWOX8jwP2SKJaK9LbK5QS3__bR865Ieyhdj3S98DNCxBkO-plzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب عن إيران:
إيران مستعدة للاستسلام. سنحقق الفوز بسهولة بالغة في الوقت الراهن</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/92303" target="_blank">📅 01:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92302">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a92eaf392.mp4?token=pDynTgfzORgDg0bzNyWg15BA8yvmpoFhuCu655GAl1rutH6i37NISaWKugrX1EOSshdh6FDQ6xjAWTK3xP6LW3ddNzzeBn_v_AISJkRblCQ4cMyLr6_H9WnZFmoQsheguedbkKVrPWxUmlzWuDzagQlGRyivR1V5AfI_q4NPLxdETtewCDdrsIBVz7llGMjmegNA6Ic6fPPwt0CrI-3FEjzm2o6xcOa4ctgbHSmRTeKXSDZmsHZ5rWdk804_oes8VHIEijU5VFIq6lyJMhotwMIMa7torU_8B_5gXRSmIy-xYcsB0hko91A6CrVQyi6B1ee-sG0ws42hr66EvBNsHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a92eaf392.mp4?token=pDynTgfzORgDg0bzNyWg15BA8yvmpoFhuCu655GAl1rutH6i37NISaWKugrX1EOSshdh6FDQ6xjAWTK3xP6LW3ddNzzeBn_v_AISJkRblCQ4cMyLr6_H9WnZFmoQsheguedbkKVrPWxUmlzWuDzagQlGRyivR1V5AfI_q4NPLxdETtewCDdrsIBVz7llGMjmegNA6Ic6fPPwt0CrI-3FEjzm2o6xcOa4ctgbHSmRTeKXSDZmsHZ5rWdk804_oes8VHIEijU5VFIq6lyJMhotwMIMa7torU_8B_5gXRSmIy-xYcsB0hko91A6CrVQyi6B1ee-sG0ws42hr66EvBNsHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
بالفيديو المتداول من حالة الذعر التي اصابة الحجاج بعد الانباء عن امساك بشخص يحمل مواد متفجرة.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/92302" target="_blank">📅 00:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92301">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالإعلام الحربي</strong></div>
<div class="tg-text">🔴
الرصد اليومي لطلعات العدو الجوية التي يخرق بها السيادة العراقية.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/92301" target="_blank">📅 00:41 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92300">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇪🇬
مصر تعلن دبلوماسيًا إثيوبيًا "شخصًا غير مرغوب فيه"، وتأمر بمغادرته في غضون 48 ساعة</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/92300" target="_blank">📅 00:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92299">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0b57ca628.mp4?token=rplqEDL_sEN6kXz982oJ4GN6F_RfL5khd5gcC8LPwgQtu3BxBiLVTo23z0CSqPnv-LcvHK4lKDG7Plr0axlM2ibc3I2SKyaMysp1ToQIOcARzP4h2rwqlcDAPXz9HXhWTJ1auz_T2guNQG7wZDzRwoD7BV_bh7Ajaqu3vMtddFkfCOUA-nStYLKaCjGhH5x2tQvBT3tFYig5yUMuT_KKe2mX07l59kKoI21Mc8lSn5yOy5An-KcsLzw65lu8I1ngc1BY2_x4gpmM001DbL5wM-i6ATqc_hjLTvF1FYl1HQl4ViZ7Jo6422oPPCB1eYqORA93YvoaxclDFiJ801KbWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0b57ca628.mp4?token=rplqEDL_sEN6kXz982oJ4GN6F_RfL5khd5gcC8LPwgQtu3BxBiLVTo23z0CSqPnv-LcvHK4lKDG7Plr0axlM2ibc3I2SKyaMysp1ToQIOcARzP4h2rwqlcDAPXz9HXhWTJ1auz_T2guNQG7wZDzRwoD7BV_bh7Ajaqu3vMtddFkfCOUA-nStYLKaCjGhH5x2tQvBT3tFYig5yUMuT_KKe2mX07l59kKoI21Mc8lSn5yOy5An-KcsLzw65lu8I1ngc1BY2_x4gpmM001DbL5wM-i6ATqc_hjLTvF1FYl1HQl4ViZ7Jo6422oPPCB1eYqORA93YvoaxclDFiJ801KbWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
السلطات السعودية تلقي القبض على شخص  يحمل مواد متفجرة داخل الحرم المكي.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/92299" target="_blank">📅 00:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92298">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0add1fe8d9.mp4?token=N9zhrwFs-K7Oav5zSV7PvyIVipkeE5g2XEgZFOceeVWFshwXrodnvydjpaGV-967ISoWQvD_b3sw_wVp8qZnhAZzCTEnZ4w2yORHrBHAN99wZK2Ze6fRTxvfD6jTzX0TgKFn7_TymNjgcan4JuiTIz6qo_9ds_gO6Z_XZ-SoDPsFQ704sauRBZTbf2mxhnFG4EA1UEEQg9mormhezfmyWb8YQjq7w18f5GiZLVqtW0zG-ugHwl1WVleXLd-v63NOY0ceIA9ZEQTTcABLVQAlPQ51P2paKKnromAWPx-FAGUITvlJvO_tXKcKUBP662aDgskDaT_cc_QfIE19BICz_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0add1fe8d9.mp4?token=N9zhrwFs-K7Oav5zSV7PvyIVipkeE5g2XEgZFOceeVWFshwXrodnvydjpaGV-967ISoWQvD_b3sw_wVp8qZnhAZzCTEnZ4w2yORHrBHAN99wZK2Ze6fRTxvfD6jTzX0TgKFn7_TymNjgcan4JuiTIz6qo_9ds_gO6Z_XZ-SoDPsFQ704sauRBZTbf2mxhnFG4EA1UEEQg9mormhezfmyWb8YQjq7w18f5GiZLVqtW0zG-ugHwl1WVleXLd-v63NOY0ceIA9ZEQTTcABLVQAlPQ51P2paKKnromAWPx-FAGUITvlJvO_tXKcKUBP662aDgskDaT_cc_QfIE19BICz_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
السعودية تسمح بدخول انتحاري داخل الحرم المكي</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/92298" target="_blank">📅 00:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92297">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇸🇦
السعودية تسمح بدخول انتحاري داخل الحرم المكي</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/92297" target="_blank">📅 00:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92296">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇸🇦
🇾🇪
العدوان السعودي في وسط الاحياء المدنية بالعاصمة اليمنية صنعاء.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/92296" target="_blank">📅 00:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92295">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇷
‏إيران تعرض السماح لمفتشي الطاقة النووية بالدخول في حال تخفيف العقوبات.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/92295" target="_blank">📅 00:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92294">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWk9Qa1M88A4T1CagXU0oRdobHba7p7_4ArqsEQMmC4GDvVzfSkHNmAr_lgLEV9MWtKMGGoeUQZLFWzwsRqq_8M4we-doH5gfNd3YwLLNbTm6pdVt-5dwHbnBSJkTSDUUN_93SesdWUW78jcrZbleGqhPq_Az7r5XsRO0QgKYqbcU5YaJj2sJbygHDUm28_8Dq8yEUKDUO6CA8UFpfzVMHLHIAMGbnnvWtXDO52cK_yC13gWGsG4Qsm_ZP4vR2XMqAIAJDqP1I7FzODt6siz8HQ3qy8RpsWmsD0NRWoEbCEojeKWmBzyp261Ov355cumvj884-QksunBS-bEKBBmbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇾🇪
من العدوان السعودي الذي استهدف عاصمة اليمن صنعاء.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/92294" target="_blank">📅 00:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92293">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c75906a072.mp4?token=phmQAWWaxK0-1TpHyNcwNeEbYl75gUehY4UhwlW9HMFDRZ9UZAXuSqvd0Ek96mciC_DYUnNRrc-DQwaIfjo1ZAbT2F2x5wx5FQTrjBRfRpmtJmlKeLa3kXCx3hJld8y0X3EVO5pV1zANDpgYfEkZaqqq5p0PHOD8Vi4hBuAr_eb7gg5z1VKREGYWjop78h1pRaMGWGutvP9w0zvBmxGNZLeRBdhEaFz-PNfvexQz4IQCenegt5JYHXELtHmactksLBhKhKeWO7-nGuQuDAory61m6bE7Whlv9Z86-HnSSNWclnKXmp3bdJqPtB2mtRgO8TnPrVgY3busIj9p3zHE0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c75906a072.mp4?token=phmQAWWaxK0-1TpHyNcwNeEbYl75gUehY4UhwlW9HMFDRZ9UZAXuSqvd0Ek96mciC_DYUnNRrc-DQwaIfjo1ZAbT2F2x5wx5FQTrjBRfRpmtJmlKeLa3kXCx3hJld8y0X3EVO5pV1zANDpgYfEkZaqqq5p0PHOD8Vi4hBuAr_eb7gg5z1VKREGYWjop78h1pRaMGWGutvP9w0zvBmxGNZLeRBdhEaFz-PNfvexQz4IQCenegt5JYHXELtHmactksLBhKhKeWO7-nGuQuDAory61m6bE7Whlv9Z86-HnSSNWclnKXmp3bdJqPtB2mtRgO8TnPrVgY3busIj9p3zHE0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
عدوان سعودي على صنعاء الان.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/92293" target="_blank">📅 23:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92292">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwisCp2tkXE9q2rAiLUS4-8g7sEJyxWt46l2at1Denr-ykeDhBP8p3bRE07A2rRTbFKswk8UrHaj0uePF9_Tbmc1LAYhACglAYoBE_eMVC9uGGffhMmLUoTEUlIs5gTdDhfIxU1T5G9zxsOPuhM1NuvJdimFWZVVj8yTPomiz8y7Fbn4kb8-ZV3iDKrsC_L8BTly83wY2pv4QSbxv8HR-AJ_7aRJKrhNJdhjk0xvil3kEbwV-iJ8Q7PUnnefCMx71-cBzgze-cKY6z4SzQTDr3gOiCeyJdn-vuk-BofWp_bnePc8TuPX_N5s4Q1naBb2lfbrmlqdOPBx8MhQocp26Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇾🇪
عدوان سعودي على صنعاء الان.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/92292" target="_blank">📅 23:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92291">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-fmnV64Mw5sZ1QFYDKE0kRR0zX7Ym0Rnvg93EAUNhKONNUieW7Q2hgrgZsMq4Sg79zdg3894zZQmbBM8EPpi6omac5kHykytZYtlGx5Ii0gNjiDkR9xuvSJDiySrnQ9C9NCyndAJ1xNtGWzGxfvoxnwuLYL5SW1S1oN4Jk6K3kLWAM17JSSVP_4dztrAgJgFCCG-s0mlMaM7R6sGapNphvBts1xuvBjdNXd_KPPw41608rhovzrrJK73aadf2-8u4lZSZrEwR9_Wke6C0dQSXw8fVARZjznV-X60v7p7jRU3NXPzcr37KP8n8P4aK4mfrX2ez5wTcJBamC95fLSfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
تعرض سفينة في مضيق هرمز لإستهداف بصاروخ من قبل بحرية الحرس الثوري واشتعال النيران فيها.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/92291" target="_blank">📅 23:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92290">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drzGFCNOUBF9LL9wG6bMzNQsxf3dhvQifGHCatAB5YALMZ6EpUwiRi4Zc6CoAPI0K_VVyU7XHBksKnf66ThZ3d04Vsq8K4c7gPIczTZp7RCrixn8ALjThBFrkSL0BN8Z_ktaJSax92dyjNWDk8Fan6hI4WquCEpUqKmIrwiLrcAFyRbvWM2H2c3vhwzpvkJwxiEI6k-4QGz1AY7AYdHTH_PgpssiLMcaNm9AdZGn5XfA6O6tB-92tL3ofH1B48JH2foAskzIXADqsr6EXRKrdjbT4QqvjKLALTzzcm4EgxTuWJCYa_sgdlqK13FV9ifqC1bg6ysNcXWowtbWGNpr8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇾🇪
انفجارات اخرى في جازان نتيجة هجوم بصواريخ باليستية.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/92290" target="_blank">📅 23:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92289">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇸🇦
🇾🇪
صاروخين تستهدف جازان وخميس مشيط.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/92289" target="_blank">📅 23:28 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
