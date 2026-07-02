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
<img src="https://cdn4.telesco.pe/file/TOn3M6IjdpmkKHQ0QjtKns5ZMTMuCx2PponC68cHUk_vsqGpCYCiHB5BMvpH7pWxysMaHCbybOfYYK5yFBUSogP8-LoeUIuH_nxYdUvZfW3yg7x_IMowagBGDHqP2FnQ2Od5RE5wxObDOSdalcyCarG-xsh7J1iCBmhYoH5lMqXLJdGTKNGTZm8D68YUAHTrKoNC-RyyURgXIoRB-YiCpWYRhktO4DWRqOWujyYuwK1QF_Z3ZxUcCXeoOp5LLBuZoJkpccDcL8XOS89XsendHetu3OftIeeBigA20WfhgvHz-DyHs7MqfXDvFjaT_F3r61Vea7QPiCFVlcZbkDUYLQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.11M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 23:28:44</div>
<hr>

<div class="tg-post" id="msg-665739">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCE3BIt2PadXc4W2FEsb1HQmcp7ffJIvax6hSTJR2NiIGv85Jk_ldn12stHPbBDuYUbwivZ9Sfj_CvbbZKAZhNJdTV1JwtOixvFgdlXU9D0Q611tjMpAFaJLRo_bxy913qaRuICsZSlg0IdZ_UGBIgB5GCWo6-f55UfaVMoP5SwRgDSqHpOEtqdQT8BTvRjLCF-ztN8oTQHyiCUhonGOLzwrMR7xi2lfb7_zKRTiL9kq-dRAvxLa0ZoW2lw-1pvlh0bHPrlgfif0lt1hQgLBxldhFndTTj6EM79qYOXnao4Os1YUb_GDxgpuIosDFfrN932O9X8pla6IhhzVhlExcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تأکید توییتری پزشکیان بر نمایش همبستگی ملی در آستانه تشییع
رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/akhbarefori/665739" target="_blank">📅 23:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665738">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6fe6debe7.mp4?token=UCcSAUvuBCwry_e1JVvrmiisSF92nAuh0b23-gEa76k-TFoj8Ri8eFeJeSIh7vD75V3DyWd4SWuMOoKha-VGWdI6Kn9iZxhQXQC7xARv_CmXRFZOJnt_O8MXAv_ZydDYfeis99eSQHNPdGO1X-9GWi-tWgg-thdRHLjNVS1d-AMYVclBHBK8yH8qedQBsonlSindcbyxMRzZqx7UBTf1VGyisqp7bPBATbfHsyD0G3JtPiEDWf5J5btA-4kKkXDzGtuHL39JTbs_cX7qdgEmsXpjdl1-3cpOzmmZRvkFQmNZ-aFhOefcA71mOigEJMg9om81c_KuY8TGnu2hRj-q4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6fe6debe7.mp4?token=UCcSAUvuBCwry_e1JVvrmiisSF92nAuh0b23-gEa76k-TFoj8Ri8eFeJeSIh7vD75V3DyWd4SWuMOoKha-VGWdI6Kn9iZxhQXQC7xARv_CmXRFZOJnt_O8MXAv_ZydDYfeis99eSQHNPdGO1X-9GWi-tWgg-thdRHLjNVS1d-AMYVclBHBK8yH8qedQBsonlSindcbyxMRzZqx7UBTf1VGyisqp7bPBATbfHsyD0G3JtPiEDWf5J5btA-4kKkXDzGtuHL39JTbs_cX7qdgEmsXpjdl1-3cpOzmmZRvkFQmNZ-aFhOefcA71mOigEJMg9om81c_KuY8TGnu2hRj-q4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی مسی ناخواسته وارد ماجرای علی شد
🔹
بازنشر ویدیوی قدیمی لیونل مسی که در آن همسایه ایرانی‌اش در بارسلون از او درخواست می‌کند پیامی برای فردی به نام «علی» ارسال کند، بار دیگر در شبکه‌های اجتماعی پربازدید شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/akhbarefori/665738" target="_blank">📅 23:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665737">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_NSuXTiZtqKtCYmXBYMgu2ZNtKb5GLRJ3GJe4XAbiTogS_mperBf4bz8WcG_pp54BqplQTWUgscLiZh5WOkY58XnR8Q8O9RJ3k9fKnB5CbpkzNKCOPMZvNM26scRXJbP6BEJfd85oya6KVchinWgOaEWv_hR3FIq14fa40re7cI7zWUa1xeM48imWiPmKPDSK3Xappff61bVKojoere-rTE0nov98RBBWmaLV_K_9xeQbjCiUfcyU298LxopSBxVtnwZyTiSYGtwzhsGguFpXQnFnusVSW_5Pl036Dwz9nlPrnWMsyZwmcUDLYMg_hlMtTUf7Rmxf5_s2FcyVW2kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
به تو از دور سلام
چله زیارت عاشورا تا اربعین حسینی
#روز_هشتم
▫️
امروز با خواندن زیارت عاشورا به نیت شهیده  زهرا محمدی گلپایگانی  ، دل‌هایمان را به سوی امام حسین (ع) میبریم. امیدواریم که ایشان ما را پیش اربابمان شفاعت کنند
@Heyate_gharar</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/akhbarefori/665737" target="_blank">📅 23:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665736">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
تجاوز جدید رژیم صهیونیستی به جنوب لبنان
🔹
شبکه «المنار» گزارش داد که نیروهای اشغالگر رژیم صهیونیستی دقایقی پیش دست به عملیات انفجاری جدیدی در شهرک «بیت یاحون» در جنوب لبنان زدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/akhbarefori/665736" target="_blank">📅 23:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665735">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcac573db5.mp4?token=J9a9RHyEwwbjoGUpe-OtKAIEeTArpjZ1q5oJwyxT-l2l-dYVo9iVXJhGWK_v4DlvX1RT4UCLAuUeKfN3nmyFEQOmcRFoktTYIy9ExfnoFeew5EDVtcODAlPFK61AQGU8kcqaBeCpPvdvY2aTbMsMf6ZBsosAUn6DnmN4KQZEszi1UjIDvEajTOyZjAt1djGAMYibvSkvEf2EIqKRPyN59e_u5DnocZUsZFzT-ZGBzpHnWadDitM56V0-lBzkZEAahTvtg51mnfyX6vudv0kxXZ8l8W0GrNjh-3cNQh3NzNbBNaNm_-WerZ9Ofu2Yf69iErzS7xIS3kllOCyJRXToBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcac573db5.mp4?token=J9a9RHyEwwbjoGUpe-OtKAIEeTArpjZ1q5oJwyxT-l2l-dYVo9iVXJhGWK_v4DlvX1RT4UCLAuUeKfN3nmyFEQOmcRFoktTYIy9ExfnoFeew5EDVtcODAlPFK61AQGU8kcqaBeCpPvdvY2aTbMsMf6ZBsosAUn6DnmN4KQZEszi1UjIDvEajTOyZjAt1djGAMYibvSkvEf2EIqKRPyN59e_u5DnocZUsZFzT-ZGBzpHnWadDitM56V0-lBzkZEAahTvtg51mnfyX6vudv0kxXZ8l8W0GrNjh-3cNQh3NzNbBNaNm_-WerZ9Ofu2Yf69iErzS7xIS3kllOCyJRXToBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول اسپانیا به اتریش توسط اویارزابال
🇪🇸
1️⃣
🏆
0️⃣
🇦🇹
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/akhbarefori/665735" target="_blank">📅 23:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665734">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBTxeLUYQL1mu0hup-ohVBMjv27fs8h76tfqk3nT_LhJaOkQ7HNXdP_b8gTJcLF1MZUT8cK5rInrVgxaHc3EYZrPpe2fbEe17xcjKknas78gn26RbhZHzvmOcGz2GVb4WCrP-4NFWeCRgT1DQcWgkVfv29WOy13IV9Hmu0mHPMSAGrIJJmOsiGLczhBZ-9g0lCfEqUjBg64o6aGYI-LRe5ZzTe9RQqFjSmlh4trFE5o5ZO95XiNt8iVtejBoWxyEjQkm6fAS3XlqgovURd85u3q0D24-hUSWdxt9GdTdOZxjyD9wIqaG0ALnUSjO55hlRa_Oifdc-2RtuuTo4faN2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رستاخیز خونخواهی
🔹
۱۲۴ روز از شهادت رهبر انقلاب اسلامی می گذرد، اما اندوه فقدان آن بزرگوار همچون روز نخست بر دل و جان مردم ایران سنگینی میکند. اکنون که کشور در آستانه تشییع پیکر مطهر ولی امر مسلمین قرار گرفته است شعله های خون خواهی این امام شهید بیش از پیش برافروخته شده و دودمان قاتلان آن بزرگوار را در آتش خشم و عدالت خواهد سوزاند.
🔹
هفتصدوهشتادونهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/akhbarefori/665734" target="_blank">📅 23:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665733">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpJGgIBxfkDzguC1XUsX19yKR2hOghUw33DF-N2AHO7-DezRpVIptbqYorNw6f5l1mFIwDTvM_Eb-cYR5uBp2hwBVrzVgKEED6_VKWjUzpfExT5v6dYxSm32Yh4pZdqO3MolllFbV59XABbwByOWOstDjtU7U9kneH2NjG8MrZn4Hy3_8rjuAfZCzh7lEgTwwe-ud49bizkMRc75YuR7YPI7ZFw0lyDbbe5SE7GMBQra3Ih8FjTLFeEdxPA9jX6B8XhuylsoVHo1arDfHAKPx8QYX3Wf0f2UP-9PC2SgHDHloxSSCjOD9JiLmXRBI8QcF4RWvIMq9TMA44ibs1dZYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با وجود سرکوب، مردم شیعه بحرین امشب عزاداری باشکوهی برای شب هفتم محرم برگزار کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/akhbarefori/665733" target="_blank">📅 23:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665732">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/205a99b64c.mp4?token=Tcc4krOXbnxwlkD3K9rtTh_kXTvnQJqb-h8ph9wJ1O6ETPGalFm9qVUMCFUFUYEiqsq96jXS5QHVVJuzs1Sjk6IC9M2Cb43yzHsku-q-A8d58pHNhgpSQiECZiIZa0FMiJb0xKfhNXUdNaZit0GslSEbxdZ_zSDggUmhPxbDku63NzD7LsW7dPJ9dPUN4TyqxhfrY8yo7Q4Xcighw-pl37JXTnkqOvDKkrK4WrN9W1CPvTP6W2AFQj5Mhepoqw7g3PL5isn6Gmok4gR8jun9r1AVrKUSYInilVMC3_eTaF-QM7ok_tQxvMpRozSxEM3FRkftq7WXbqEwJkyD7eXKeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/205a99b64c.mp4?token=Tcc4krOXbnxwlkD3K9rtTh_kXTvnQJqb-h8ph9wJ1O6ETPGalFm9qVUMCFUFUYEiqsq96jXS5QHVVJuzs1Sjk6IC9M2Cb43yzHsku-q-A8d58pHNhgpSQiECZiIZa0FMiJb0xKfhNXUdNaZit0GslSEbxdZ_zSDggUmhPxbDku63NzD7LsW7dPJ9dPUN4TyqxhfrY8yo7Q4Xcighw-pl37JXTnkqOvDKkrK4WrN9W1CPvTP6W2AFQj5Mhepoqw7g3PL5isn6Gmok4gR8jun9r1AVrKUSYInilVMC3_eTaF-QM7ok_tQxvMpRozSxEM3FRkftq7WXbqEwJkyD7eXKeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیپلمات ارشد ژاپنی: «راهبرد شیر آب» ایران موفق است؛ آن‌ها با تنظیم قطره‌چکانی عرضه، مانع کاهش قیمت بنزین در آمریکا می‌شوند تا بحران داخلی برای ترامپ ایجاد کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/akhbarefori/665732" target="_blank">📅 23:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665731">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی فیلیمو</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b603dc349e.mp4?token=hybbE2AGZcahn_o-cUF2T33F_gCn944avgPruRRYqX3_xO8DhjP8FBJZjhxjhZL8y5Y51QgbFQd5702PRbi2UlmAknI9Jr4Ucr91LZB6XPCbYfyOlCweqLzUgicBRMoC83eXxStRi8rQ9nBEYpgQ4eXBOWSXUoh564OBP2DwKhq6pwiQwZdmgeAE8DHrOOSjHvbixhK5Liw7SQH5VcvI3JEcwgcMqSsqTaST9__lF2oKJBkNFXk7mOtB4OBZquEmo4jFvUZd44jr4P7Ak9JQDW_8Le3Cun5k3iSf189Q5vpIHbAxj38r4f4iJN-3AzSKOVl_HMmsT1i0fRlPF2qK0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b603dc349e.mp4?token=hybbE2AGZcahn_o-cUF2T33F_gCn944avgPruRRYqX3_xO8DhjP8FBJZjhxjhZL8y5Y51QgbFQd5702PRbi2UlmAknI9Jr4Ucr91LZB6XPCbYfyOlCweqLzUgicBRMoC83eXxStRi8rQ9nBEYpgQ4eXBOWSXUoh564OBP2DwKhq6pwiQwZdmgeAE8DHrOOSjHvbixhK5Liw7SQH5VcvI3JEcwgcMqSsqTaST9__lF2oKJBkNFXk7mOtB4OBZquEmo4jFvUZd44jr4P7Ak9JQDW_8Le3Cun5k3iSf189Q5vpIHbAxj38r4f4iJN-3AzSKOVl_HMmsT1i0fRlPF2qK0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه راست میگی الان سرشو ببر و منو بشون پای سفره‌ی عقد!
#
بدنام
، قسمت ۱۳، “داستان دو شب”
فردا ساعت ۸ صبح، به‌صورت اختصاصی در
#فیلیمو
با حضور حسن پورشیرازی، امیر آقایی، سینا مهراد، ستایش رجایی نیا، سولماز غنی، سید مهرداد ضیایی، به‌آفرید غفاریان و لعیا زنگنه
کارگردان: احسان سجادی حسینی
@filimo</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/akhbarefori/665731" target="_blank">📅 23:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665730">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔹
تیراندازی کور تروریستی در سراوان ناکام ماند
🔹
ساعتی قبل تیراندازی کور تروریستی در نزدیکی مسجد جامع شهر سراوان رخ داد که در پی آن تروریست‌ها سراسیمه از محل گریختند. این اقدام هیچگونه تلفاتی در پی نداشت و خوشبختانه شهروندی در پی آن آسیب ندید.
🔹
هم اکنون آرامش…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/665730" target="_blank">📅 22:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665728">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
تشکیل ائتلاف نظامی جدید در جنوب لبنان پس از مأموریت یونیفل
العربیه به نقل از یک مقام فرانسوی:
🔹
فرانسه، ایتالیا و آمریکا در حال برنامه‌ریزی برای تشکیل ائتلافی نظامی جهت استقرار در جنوب لبنان هستند؛ این اقدام پس از پایان مأموریت نیروهای حافظ صلح سازمان ملل (یونیفل) و با هدف حمایت از ارتش لبنان صورت خواهد گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/665728" target="_blank">📅 22:49 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665727">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSkUNRFrvU4ys3XrDEhOs1Mk2pF-PKdjTmtRpV6pKFv8ZqFt-qAUHTikhC8A9i0iu04wAXfs8TulReYxVGWReXLDy3kKhyRNrZN5nigsFVqab85KNAnAtPsDFEFVwiUvxj3wdvTaPsEORg9117lIXtHj84PsK6u8PaaFRxSO9wQzCKbTy7DnmDMoanbxick0Z7cgQof_FoQNgnu5YezIkBZebcyAJkkvI2tkVBou91O00cdcXCenwV1ODpUtf8Yvc1QTl0iJpnsQO6ffMXfeu-oc83NXr5J4xGKrIu_H3ekshEIq7ZNOBj1KAv6bYuOdKJnXncWZ-1usqpxfGV43Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خاموشی فقط چراغ‌ها را خاموش نمی‌کند؛ سفره مردم را هم کوچک‌تر می‌کند #برق_مردم_کجاست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/665727" target="_blank">📅 22:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665726">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f7a4b6ef.mp4?token=m5GLslT149q1qZuycfZNat3_gkQV3w4rrQj6o6YPwgci_OZNf61ncOKCNfxCcI8IBecWvpmiZ7EZAtqXaWWLhakaxPR7Fz0nU7HCiTilcacaziEAnwd2RTa69rH1oZDO2JxsHw1EXUdzPZJ9fysKAzoPCYN81uo_dVgsyHa6qpFHeJWol-UkdNklEMmbNGDUQxcLO4BJe9VosAWAK00efghqKfmIlDeOKHpzQk6HlADd_LYxTM2biRwcr3jjsxlve8rsZD9ASDp5GXHGAC_2Z1YJXoW-VN4hw1anc2wnY36ZK8pQcVthzwgJVFHPJLXe3yWZdERvmnFQSY9lIVAidA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f7a4b6ef.mp4?token=m5GLslT149q1qZuycfZNat3_gkQV3w4rrQj6o6YPwgci_OZNf61ncOKCNfxCcI8IBecWvpmiZ7EZAtqXaWWLhakaxPR7Fz0nU7HCiTilcacaziEAnwd2RTa69rH1oZDO2JxsHw1EXUdzPZJ9fysKAzoPCYN81uo_dVgsyHa6qpFHeJWol-UkdNklEMmbNGDUQxcLO4BJe9VosAWAK00efghqKfmIlDeOKHpzQk6HlADd_LYxTM2biRwcr3jjsxlve8rsZD9ASDp5GXHGAC_2Z1YJXoW-VN4hw1anc2wnY36ZK8pQcVthzwgJVFHPJLXe3yWZdERvmnFQSY9lIVAidA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت بحرانی بنزین در روسیه
🔹
تاثیرات جنگ به پشت فرمون روس‌ها رسید. قرار بود سوخت اهرم فشار روسیه علیه اوکراین و اروپا باشه
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/665726" target="_blank">📅 22:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665725">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c454c5ac8.mp4?token=fu3u8T2g-2iiLO0MoV_meOFk95zLksj8H5PMBrfpyKcABv8aiGrNpvKRRn7KmGEc0vyZoQamLNQQUFVfHuoT0K99nWQVDglwvwuYTkjhS2L4iwiAS0FF_o9kyj8krKkfZ1_PUvaiPBiYICKXtdTg_CkMbvlVT7cDapoTymLWk0J3sKoh46HayVgSK11zoAeDAVINTwaPJ_3cjjTjjp2-7CBY_45_0X5D8YSZ3fUALFsrxDr5SiOmHO6vOLBapj42ypjBCqcghTThf_8QzHLDeOO7iFdHvagfFGoiSPoHXm7N4E4l2yIH3Fz8v7Z7j4wvAY0BRXk_mGevhfEk_7Jj7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c454c5ac8.mp4?token=fu3u8T2g-2iiLO0MoV_meOFk95zLksj8H5PMBrfpyKcABv8aiGrNpvKRRn7KmGEc0vyZoQamLNQQUFVfHuoT0K99nWQVDglwvwuYTkjhS2L4iwiAS0FF_o9kyj8krKkfZ1_PUvaiPBiYICKXtdTg_CkMbvlVT7cDapoTymLWk0J3sKoh46HayVgSK11zoAeDAVINTwaPJ_3cjjTjjp2-7CBY_45_0X5D8YSZ3fUALFsrxDr5SiOmHO6vOLBapj42ypjBCqcghTThf_8QzHLDeOO7iFdHvagfFGoiSPoHXm7N4E4l2yIH3Fz8v7Z7j4wvAY0BRXk_mGevhfEk_7Jj7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نوین ایر در آستانه آغاز پرواز؛ ورود رسمی جدیدترین ایرلاین کشور
🔹
بر اساس اطلاعات بدست امده  « نوین ایر »،  به‌عنوان جدیدترین ایرلاین کشور، در آینده‌ای نزدیک فعالیت عملیاتی خود را آغاز خواهد کرد.
♦️
بر اساس اطلاعات موجود، هواپیمایی نوین ایر با پشتوانه‌ای توانمند و برنامه‌ریزی منسجم، در حال ورود به صنعت هوانوردی کشور است و از حضور جمعی از مدیران باسابقه، متخصص و شناخته‌شده این حوزه در ترکیب مدیریتی خود بهره می‌برد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/665725" target="_blank">📅 22:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665724">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در شهر دیرالزور سوریه
🔹
منابع خبری از شنیده شدن صدای انفجار مهیب در شهر دیرالزور سوریه در نزدیکی مرز عراق گزارش می‌دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/665724" target="_blank">📅 22:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665722">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e65499983.mp4?token=SblVSInpA0QUkFAwTk1gpRNlFWOCwDaL_4qhggL9YlTmMpZh6ax4uoQrcPDCPPdATwRO2c5aJCVgNVflWwJbg_JLtNMPXPUicH-W8vQkPlkR9mkaVAUp0xhiEoHWEdbfea1Zfqf2ovkv_Z8jyaV2MJzztp3Dypo8g5SrRWCxFJa4VhQM76l-tc4FXywK3CPn2NZuB5T77BctZMr1F0lLVwEcTSHv6mEzxTA2zy9cev-YmriePYgdISugRwuK4Qu0dw5KueDqXFXXcwWQfBOUGy_r5uJcK0PbTmJi4xWrYH_wg3Rup__KjSIbmab5FilU1UcNg2HS1k-fdk1udklaaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e65499983.mp4?token=SblVSInpA0QUkFAwTk1gpRNlFWOCwDaL_4qhggL9YlTmMpZh6ax4uoQrcPDCPPdATwRO2c5aJCVgNVflWwJbg_JLtNMPXPUicH-W8vQkPlkR9mkaVAUp0xhiEoHWEdbfea1Zfqf2ovkv_Z8jyaV2MJzztp3Dypo8g5SrRWCxFJa4VhQM76l-tc4FXywK3CPn2NZuB5T77BctZMr1F0lLVwEcTSHv6mEzxTA2zy9cev-YmriePYgdISugRwuK4Qu0dw5KueDqXFXXcwWQfBOUGy_r5uJcK0PbTmJi4xWrYH_wg3Rup__KjSIbmab5FilU1UcNg2HS1k-fdk1udklaaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازتاب شعارهای جدید در تجمعات شبانه پیرامون تنگه هرمز
🔹
گندم و جو ارزونیتون؛ تنگه نمیدیم بهتون
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/665722" target="_blank">📅 22:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665721">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس: کنار رفتن وزیر نیرو به وزارتخانه کمک جدی می‌کند
بهروز محبی نجم‌آبادی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
در صورت بازگشایی مجلس حتما این موضوع مطرح می‌شود که استان‌هایی که تولید آن‌ها از مصرف‌شان بیشتر یا مساوی است شامل خاموشی نشوند، اما امروز شاهد خاموشی برخی استان‌هایی هستیم که تولید آن‌ها از مصرف‌شان بیشتر است.
🔹
هزاران خاموشی‌ بدون اطلاع اخیر به کشاورزی، صنعت و مصارف خانگی جای گله‌مندی دارد.
🔹
شخص وزیرنیرو عامل جدی مشکلات وزارت‌خانه است و نقص مدیریتی او کاملا مسجل است و کنار رفتن او می‌تواند به وزارت خانه کمک جدی کند.
@TV_Fori</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/665721" target="_blank">📅 22:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665720">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a71c35768.mp4?token=hKAKGdChX9WLO-PpWGVYiYpjrIK-4XId3SmI-tQ5vK05uhFvTk0AmuWz-vIUe4Q9xfr_Hw7BGL3M5uu21dQIoUqYAcDsfuDkWqrDY7y4Q4A9fbvZ2SIgKZB_fXjUXjtD6CIHC-KXwPidod-uWZDqsu5xWQxkHRPU1tZ3I8PydxxJqQm0etDnA87zSPuuTXcPidEXEaEsgyn_SiT1sjzVL_mVYYQWhQIDuoumdAGXMtSF4uxeru4SRryFHu_czCqxlLSE59Gnh6noZwZ2PYwVqXnYCitwvOTJ0drYOlXwpClOaKZ1KTeqPyppjHw402klP2Qan2GdoK58W4BkZH5HDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a71c35768.mp4?token=hKAKGdChX9WLO-PpWGVYiYpjrIK-4XId3SmI-tQ5vK05uhFvTk0AmuWz-vIUe4Q9xfr_Hw7BGL3M5uu21dQIoUqYAcDsfuDkWqrDY7y4Q4A9fbvZ2SIgKZB_fXjUXjtD6CIHC-KXwPidod-uWZDqsu5xWQxkHRPU1tZ3I8PydxxJqQm0etDnA87zSPuuTXcPidEXEaEsgyn_SiT1sjzVL_mVYYQWhQIDuoumdAGXMtSF4uxeru4SRryFHu_czCqxlLSE59Gnh6noZwZ2PYwVqXnYCitwvOTJ0drYOlXwpClOaKZ1KTeqPyppjHw402klP2Qan2GdoK58W4BkZH5HDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تفاوت آشکار قیمت خودرو در بازار عمان و ایران
🔹
مقایسه قیمت‌ها در عمان با بازار داخلی، گویای فاصله معنادار هزینه‌ها و دسترسی به مدل‌های روز جهانی در این دو کشور است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/665720" target="_blank">📅 22:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665719">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBMbeeVHZNzidB-47-h8OQGHJhZSGj1QaiCEPxxOvJ5cJNI_42tsXTI7bAMiz_RUlpg8fyMANDhNZjidXjWxgMSacrKkWVGzDf8qVwXffzmWr1lb4kyim_hty6SAfCgA1N3CuPyy7hi8mVTDedVhCS9Hk1c7fyi7cJfTHDc0uipOmbYu3gBa2U7apjhDTq3WD9oNCoX_rbNpB68O-oY3f7y_5pKPS88W6LDno15k4Ki53o7WvvBIuF9qzaIna-XIXBwGlLRbp7olqhMUUth48dLASQS4UvzlyYUUkSlBBJJFP_byo-p2p1QqCHwPPfJ6MaOsATJRWc0Lmm16lMf0xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش عراقچی به سنتکام: صلح منطقه بدون مداخله خارجی پایدار است
عباس عراقچی در واکنش به پیام سنتکام، ضمن زیر سوال بردن نقش این فرماندهی در تأمین امنیت منطقه، تأکید کرد:
🔹
صلح پایدار تنها در سایه همکاری فراگیر و بدون مداخله نیروهای خارجی محقق می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/665719" target="_blank">📅 22:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665718">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
کوهکن: خونخواهی رهبر شهید اگر انجام نشود دشمن جسورتر می‌شود
محسن کوهکن، کارشناس سیاسی:
🔹
در ابعاد داخلی مطالبه خونخواهی رهبر شهید یک مطالبه صد درصدی و اجماعی در میان مردم است و حتی کسانی که مذهبی نیستند، ایشان را ایران دوست‌ترین رهبر تاریخ می‌دانند.
🔹
اگر خونخواهی رهبر شهید پیگیری نشود دشمن جسورتر می‌شود و مطالبه مردم از مسئولان این است که این موضوع را جدی بگیرند و آن را رها نکنند.
🔹
اگر خونخواهی انجام نشود، هیچ نقطه‌ای در دنیا برای صهیونیست‌ها و آمریکایی‌ها امن نخواهد بود و این پیام باید به دنیا برسد که با شهادت رهبر ایران موضوع تمام شدنی نیست و مطالبه خونخواهی ادامه خواهد داشت.
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/665718" target="_blank">📅 22:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665717">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4VygJfgIceZmC16DlUpAOAV9XR6vH8onLT24jhhQaYDBWqi20B6isDCEwrLp3msCWcH2CnxlCDgggOL6tErPK7T951iMo6_7tLni_a4lx_585F7pvY9nZ8x17vxV7U-odC58VPHR1aAvoj46E7mI80TGNBDZEEhsGyqCfWFRmwwtBDf_LVurJBC9aXd84zpB4lIbC3a0Mv1rkwcNcncucF_QhqZA3qTHTAZNCyHR-zU0NKhlIZVwhVBngtcdH-BvikZrHsS51rxE9oW9D3XFjqUuu1iw7KlrhJ-B2bqsv2kEQVuroCcMeKgTmrdBG4g8NcD09I_ovavNsoZRDaBjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیینهٔ روزگار؛ عبرت‌های فراوان و چشمان بسته
🔹
امام می‌فرماید: عبرت‌ها فراوان‌اند؛ اما عبرت‌گیرندگان اندک. نه‌تنها تمام تاریخ بشر بلکه طبیعتِ پیرامون، سرشار از نشانه‌های بیدارکننده‌اند. خداوند نیز در قرآن می‌فرماید چه بسيار نشانه‌‌هایی از خدا در آسمان‌ها…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/665717" target="_blank">📅 22:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665715">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d5af43285.mp4?token=kOQyJ_VZV-DSwlZb0j6W7oOK9YN51Hf5V-kgKRlkHoqbZHGqWhfJOPL-sMnsl3CG36L13db5DNnX6VoZqyRkwAW5khrQT-WlfMlpc9aEA5Qb4naZe3DJyg6Xc6sGo2_2f7OLlXDv_WGLbHqLJcNDRWkSlJ45VxvM5SVKOGtmH0FT_z6wCmBz3N4l05fmkdVQNiWZd6eE26cH4-bPuWtsCGU7vex9ddTx-HvltK4Wm96Dq1hnWM1DTzvliG-kIR_Z9LDEKB__6-gMMloT_XoUDQb0Vw6HsJ41sqmLBdxz0Wc4ccTvKxMP2NdL181tCYG2n1i7Nkh1kY95NosWKSfgow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d5af43285.mp4?token=kOQyJ_VZV-DSwlZb0j6W7oOK9YN51Hf5V-kgKRlkHoqbZHGqWhfJOPL-sMnsl3CG36L13db5DNnX6VoZqyRkwAW5khrQT-WlfMlpc9aEA5Qb4naZe3DJyg6Xc6sGo2_2f7OLlXDv_WGLbHqLJcNDRWkSlJ45VxvM5SVKOGtmH0FT_z6wCmBz3N4l05fmkdVQNiWZd6eE26cH4-bPuWtsCGU7vex9ddTx-HvltK4Wm96Dq1hnWM1DTzvliG-kIR_Z9LDEKB__6-gMMloT_XoUDQb0Vw6HsJ41sqmLBdxz0Wc4ccTvKxMP2NdL181tCYG2n1i7Nkh1kY95NosWKSfgow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طرح استیضاح دولت فرانسه در پی سوءمدیریت بحران گرما  رویترز:
🔹
نمایندگان «حزب سبز» پارلمان فرانسه در واکنش به عملکرد ضعیف دولت در مدیریت موج گرمای بی‌سابقه، طرح سلب اعتماد از کابینه را ارائه کردند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/665715" target="_blank">📅 21:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665714">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50013a127a.mp4?token=U4MhZL_oz-CpbsyACsn0-lj8z9AX1HwKDPR9sfNF7gcv1e9xRsv6HLqCv76MYPhhqPerefAM43tE80OFaXdKVaGbF1cJrfnlKuq-rRMfh-ZnTym8iQsM9SQzf-zWPb_SPgys2mjp5i1GRq9nospzXBpOVr3VjBL6ccn2OrZYtt_PT1DSCBbHfLF67nyowRenrOQAv_b-M3JaOkJWNdmNey_1J0kydHwMqw0HTumWbtp7TuwyOkS2a--Lof7AYk_7-gWfM8N0U1z8O9yLDDo7u0NT_CuTQFcfH5w2uMeSCOy3av2ONJ0-OjIiMiLLGpjI7hNzKY995_VUXjFIL9F3_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50013a127a.mp4?token=U4MhZL_oz-CpbsyACsn0-lj8z9AX1HwKDPR9sfNF7gcv1e9xRsv6HLqCv76MYPhhqPerefAM43tE80OFaXdKVaGbF1cJrfnlKuq-rRMfh-ZnTym8iQsM9SQzf-zWPb_SPgys2mjp5i1GRq9nospzXBpOVr3VjBL6ccn2OrZYtt_PT1DSCBbHfLF67nyowRenrOQAv_b-M3JaOkJWNdmNey_1J0kydHwMqw0HTumWbtp7TuwyOkS2a--Lof7AYk_7-gWfM8N0U1z8O9yLDDo7u0NT_CuTQFcfH5w2uMeSCOy3av2ONJ0-OjIiMiLLGpjI7hNzKY995_VUXjFIL9F3_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور کوبا: ما جنگ‌طلب نیستیم، اما از آن نمی‌هراسیم
🔹
رئیس‌جمهور کوبا با تاکید بر عدم تمایل هاوانا به درگیری، اعلام کرد که مردم این کشور برای دفاع قاطعانه از حاکمیت خود در برابر هرگونه حمله یا سناریوی احتمالی، در بالاترین سطح آمادگی قرار دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/665714" target="_blank">📅 21:54 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665710">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cMdoY2vDz7ZA9N5tpekQB76AwFBTaCBVO3H1k5qPqp64ZCdHSqq3UCz8-p3vfM3tKMl4_DjMrui7oOCLrcYvW0QdPKKW7H_TizZS_SatrCOV-fsBZ5x0AGtqXNKPqFXib4BSVmofcrix4tyPvWhbnHb7fUH_XZfS0dKGz1ICFTj_vorb33ZpZ34OtPHC2CTFlNeNm_nycXQUy7CxoT0hFagdXuHZ04PivGBivzS6kP7XQWJAP1gTSUmqNHYT3qdyTZwW95g0LXsj90RjDOCL4FBURVWYaQQHN-XXCYwZQHUgejVhm__RHf5y5JR-Tppi3ukXFYd2U8u8mx0aE15eCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Og5PgWIqIo5tYxwHCsqd3gDf__US_8ylLjkB0F9-Zf6y2wsRZgl270D8_dNLn2AWMO_iY78j5FAns8IQFtl0elBW81vGFMW7fpJQVSn26McsBRbS9gBey5uZcZ2-rNj0nwqbXh33NVyYS5n9xoEGgzguigAdXblADgHODBOS-88QSqVcWlqSgumbqxGFQXd05Z0oED-bhbMYoXnp1pmUorabVzmwA5URsAfRvremnFrBaS6EvARj6ANvcCLRQ55tCsMRqBgYpvumPYM_kIyF8TOg62cZlJVpJ13yHRavrj1lMjvrUFdP84kPK2rfEWSwJ2wtStIXTe2qliMu9Xtq1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iW_PtapFfzSTcVwNdBTOTA6zhITqlyNQ4ZAz6hSMhQFZUdAgO6WG_9QmI96ZYUSNVa0exI8o1B0IqJgrrSwfjdN7Ax0LBUOz79yjO1mSXJVh4mjYwXeOd_dM2ZaXMQdjU9a7rU8RJT9tU0VWo6wbcTL4K6HX8pvr24JNqOSusl7DHVPuK-DDtu-mKeX4Ak3Hv6n_yKF4_XY4Yu9fuvMCNV1EHKLZAJgpGPixwLoM11lJOki46gCaExAzHNf_seycFUwtnYZmxCIxyWLwLyId-tOMEF3RIB6sOvGGL0C9fdTOopdgNFaMgWtyvOlLK3DRA03u8aCauUehvcwsSYdAyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FvmBPm6tPYYSEqhQdOxDDV5Br7XRi55d_WXlSoaSmHsvtYcIrwwdCYv4YErZF6sjVbhR4fZtcJjlPiVhOuhxXaVrTyRMOP2osCm-lzCMLSYkXw0hq0L2m9pvs3ImiLYqK2wBtrv_2ldsNjQoiVI0F-Z1uoq5bv-EJKyxSx_jJUpuVUrF7A_sWDVWk3QeswS8qDsX6WZaAnQeyo9odlMcAGfxBQBT5K2m7HEj50aWCJzQaQSB_liRaD5oD0p9QXieN6EmQRp_f-8f-sxXCGWfNNZKiRXvVC9abbplC4mhh0FtUTnhVdUHXGAy1Pw22yFU-8ySrr5FtdDoRo4BCDp2Fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دیدار عضو ارشد جنبش امل لبنان با قالیباف
🔹
خلیل حمدان و هیئت همراه، ضمن سفر به تهران برای شرکت در مراسم تشییع رهبر شهید، با رئیس مجلس درباره تحولات منطقه دیدار و گفت‌وگو کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/665710" target="_blank">📅 21:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665709">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55a5b7b725.mp4?token=DjZBM0Nmiim3vmxZ2dSkcEL0YAPBsKLSfm2NMtbLtiDI7CuPKD89EE9HLcNQc4hRiKBZu9WbLbGFx1Xxn6pr7vJEsAVxprkn9r7QMubmTaIY1eD-4p2yi5AERFgXbK4N-EaDXhWjft3G9srSGuLgz2fnLr0CxbRISXLCH35L3vSyiiHWdXiUHLs_5Co4DcgE9AlKvKapMqMSDGZeJFXVNqNRnsErCg_8XsW5p_xIF9U05CM4AFrEYajbl14sGKOjteF04WDdZ8gWZCCodEUoaDpdUw5HAhn6TGV_TUif_v-1KIV-Ihgdg9V2GOOctAnOVHzRbBikLQm25fHLowAd6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55a5b7b725.mp4?token=DjZBM0Nmiim3vmxZ2dSkcEL0YAPBsKLSfm2NMtbLtiDI7CuPKD89EE9HLcNQc4hRiKBZu9WbLbGFx1Xxn6pr7vJEsAVxprkn9r7QMubmTaIY1eD-4p2yi5AERFgXbK4N-EaDXhWjft3G9srSGuLgz2fnLr0CxbRISXLCH35L3vSyiiHWdXiUHLs_5Co4DcgE9AlKvKapMqMSDGZeJFXVNqNRnsErCg_8XsW5p_xIF9U05CM4AFrEYajbl14sGKOjteF04WDdZ8gWZCCodEUoaDpdUw5HAhn6TGV_TUif_v-1KIV-Ihgdg9V2GOOctAnOVHzRbBikLQm25fHLowAd6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به نظرت مرکز دنیا کجاست‌؟!
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/665709" target="_blank">📅 21:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665708">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nh4UvZARN0RdXZj9Eb2J3POfZVNkJHP7Ss1uMBOmoXuoInrtdmx4yRU_6yBoKVT3iNcW9EjhpOzqE224Ls21k6anW_FuqzP7mdy8HEVQw9NccMXpUul7pgIQsr__y37s83COErKTEmJ2BZZl5DrVlIbeNADcikCuT0aTVJj8ZSOsvB-wWgozzE12QmXf_I1Ggv5VjUubaNtpd--kWUyTcfF__NGk6UQBwtWZcX3o8cN28ulK-TGzdFKbqvfKsJ8oWJAC9PBN8CT7Dowi8fxPw_kCD_UhzAMqksb7oDVtd9hYV0n0X2-GPRU8wNvlf4eiCtt0oPPAby9uTLI6dJz7TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مجله تایم: ایران شاید بدشانس‌ترین تیم ورزشی تاریخ
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/665708" target="_blank">📅 21:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665706">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCJWGeouaNkvXR7O6RrFnVO7A6n17h72nBPRKOLMKphojxukRMEZ9qBK5HwzbfRtc1Q_UZ5GvxhRFdoVVcZCNlrEKBBqRRfEKGHYUCbs_KM3VdsRWvWWcyxHdbWsbuCj6VoSKgWMZsmrlLZTD5fPg47sCC4jlQEPkJu35iAw90iWMY7mPFj7kysfFjco28Uzy3gTf25dCwA4jq-6hJ5tewTnalZ_ymZh48bkIx5X4fh6LktuT-iIkgLzv0JVSVuzFCgxLaQH68VkoCHZn5YNwLOSsOrNRmLqlE1gD7pNNuMRIwH5Hpm2VliGO3lDrBSK3HHkLjFREqm4x1VXohVB6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راز علاقه عجیب دستیار بلوند ترامپ به او فاش شد!
🔹
برادر «ناتالی هارپ»، از نزدیک‌ترین دستیاران «دونالد ترامپ»، مدعی شده است که وابستگی و وفاداری کم‌سابقه خواهرش به رئیس‌جمهور آمریکا ریشه در دوران کودکی، نوع تربیت خانوادگی و باورهای مذهبی او دارد؛ ادعایی که بار دیگر توجه رسانه‌های آمریکایی را به رابطه ویژه این دستیار با ترامپ جلب کرده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3227379</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/665706" target="_blank">📅 21:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665704">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
دعوت وزارت دفاع از مردم برای تشییع رهبر شهید و تجدید بیعت با رهبر جدید
🔹
وزارت دفاع با صدور بیانیه‌ای ضمن دعوت از عموم مردم برای حضور باشکوه در مراسم تشییع پیکر آیت‌الله سید علی خامنه‌ای، بر تجدید بیعت با جانشین ایشان، آیت‌الله سید مجتبی خامنه‌ای تاکید کرد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/665704" target="_blank">📅 21:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665703">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cbd09500c.mp4?token=iIXensPeTFESK0UWXbyuYN-tvs55h-mGnT2Bl0UwKNnpCK7Buss3YHJc21YLN8LGAJ3CBBMXi4BINcRQX_BufMIss0NqsBj93LkbzEVqVtqh1zz6LFVQCI3wpzONSBVF6CK1F3q38OSJqfE2Q3PRTSxSoqHxVI5eWCvWG9j-Lap_M4WHC096BwlwmHoQLyPXCV2cuaHzFM5KT3xdx_czXq6kvY6SphWtFYdmSCmY5BKJWludkOrjq0kUrBui7c2Mj71KCD-BCJUayRaqtV0si-Aacb9PzeaCEnnPZhFx_QKFB2Vcj1aFW9Sp2BF2Z8WCsyzmM5byoLjy3EsF-QvBNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cbd09500c.mp4?token=iIXensPeTFESK0UWXbyuYN-tvs55h-mGnT2Bl0UwKNnpCK7Buss3YHJc21YLN8LGAJ3CBBMXi4BINcRQX_BufMIss0NqsBj93LkbzEVqVtqh1zz6LFVQCI3wpzONSBVF6CK1F3q38OSJqfE2Q3PRTSxSoqHxVI5eWCvWG9j-Lap_M4WHC096BwlwmHoQLyPXCV2cuaHzFM5KT3xdx_czXq6kvY6SphWtFYdmSCmY5BKJWludkOrjq0kUrBui7c2Mj71KCD-BCJUayRaqtV0si-Aacb9PzeaCEnnPZhFx_QKFB2Vcj1aFW9Sp2BF2Z8WCsyzmM5byoLjy3EsF-QvBNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بارش عجیب تگرگ در عمان
‌
🇴🇲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/665703" target="_blank">📅 21:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665702">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcf88d31ae.mp4?token=h0xVB067vavt1qR_uHDGAFQDf-Vzr9IK54vBpwVhUt2N57jAGciwCQS7lyz0ag6DX-6gaB6j5p4FwO3WFNsys6OmKpSDswX2hLpt5IW0p-fJ85yirjVzED1Ih-Lt4LI3KblRIDJywRdEpKdTMi8v2tEpqKLA-jcm-j63VU3O7gMiE6Om3RjLqhgqQ7Z71FWS0joFByjcjTfCORiC-B47pVh-dJCehUE-W9FSuCcgZ9zQaoNoSUCKhjHz0byCfEbRVZjauAlgDeq_ZPe9rEl8Iv3sYj_xdc8ykFvbCvgACH1DFa7w2AHQWQLLfqDChy1NcZYNe2yvmXqNEMEKu-IoR1aGo-a6HCeBWnNtnYT9674FCpr0rV9kQK3qLzJ6sh4RRJGGGoFsMNqPcf-kLhAtgBpWOZT8UW3COIWO_leuvbzhs5zfA-HlB9Auv6gwNRRTXBC1t4hBId2cECpOgsZTnkoee_fGD3RoMQ_P4EifbvHC3txlxqqFpaHcl_SE1IO045i9T1jnK_NL7KWSpYiTLYnwOJFN8UJwcCKkpjhF2zDLe04e3xOu8Jfag55NAkxlOd2HYomeGRNSizx2YDElmAPAvmOAK5aLsXVvYUj4a2po7Lqrg6Igfd38Qk42maZbfFFP8QUxtmUZ-7iJc1BSeH55YnbMMG2ZJVo_URGzVb0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcf88d31ae.mp4?token=h0xVB067vavt1qR_uHDGAFQDf-Vzr9IK54vBpwVhUt2N57jAGciwCQS7lyz0ag6DX-6gaB6j5p4FwO3WFNsys6OmKpSDswX2hLpt5IW0p-fJ85yirjVzED1Ih-Lt4LI3KblRIDJywRdEpKdTMi8v2tEpqKLA-jcm-j63VU3O7gMiE6Om3RjLqhgqQ7Z71FWS0joFByjcjTfCORiC-B47pVh-dJCehUE-W9FSuCcgZ9zQaoNoSUCKhjHz0byCfEbRVZjauAlgDeq_ZPe9rEl8Iv3sYj_xdc8ykFvbCvgACH1DFa7w2AHQWQLLfqDChy1NcZYNe2yvmXqNEMEKu-IoR1aGo-a6HCeBWnNtnYT9674FCpr0rV9kQK3qLzJ6sh4RRJGGGoFsMNqPcf-kLhAtgBpWOZT8UW3COIWO_leuvbzhs5zfA-HlB9Auv6gwNRRTXBC1t4hBId2cECpOgsZTnkoee_fGD3RoMQ_P4EifbvHC3txlxqqFpaHcl_SE1IO045i9T1jnK_NL7KWSpYiTLYnwOJFN8UJwcCKkpjhF2zDLe04e3xOu8Jfag55NAkxlOd2HYomeGRNSizx2YDElmAPAvmOAK5aLsXVvYUj4a2po7Lqrg6Igfd38Qk42maZbfFFP8QUxtmUZ-7iJc1BSeH55YnbMMG2ZJVo_URGzVb0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گنجینه‌هایی که رهبر شهید انقلاب هیچ‌گاه فراموششان نمی‌کردند
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/665702" target="_blank">📅 21:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665701">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atlK49tS4RlLHj_iyEuddvlSyEDc-9JRJj6o9HfsEtLYyfPiChkVLvuwPXAt9Ne76L7uy_iFv5dj3S_KeTIoQQcvlXN_5nwu0meyXPJXXSBOUWpPwVAWHHddTbFuxHZhHFAhOyP29PH0DBakANzoMc_R2GrB8djnCXHTzZoB0EbHXBl3AhZ1UEnf88rnd-KTSYhEsaTY-h8WAl8eGOPz9pc7oLXKB4oSDvEjzFXr60tHjHWSdONyIdjnqWLJ_kWF8juJUXTMHkI5QJTrVmssd1GulQQSdiDPpSJmOzIG5YxppRVK3P_YXyHMdcPnuS-LR8cG3wpo47yvo9fzYi7waQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ قمارباز: به پای صندوق‌های رای بروید و در انتخابات میان‌دوره‌ای به حزب جمهوری‌خواه رای دهید، زیرا اگر کمونیست‌ها به قدرت برسند، دیگر هرگز نمی‌توانید ماهیگیری کنید!
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/665701" target="_blank">📅 21:22 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665700">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nso9kD1wzhOBVKgmbbbIifv8Hbg3qXNFGIUGZQUOmp-JdXyFAjZXz3geZK28R7cn1kIcgYoa206OU39PSF0r7yRCdiQL15HIFeZ4XDCTsXH2WOOQmEjfEiAzcQRnic4bkjuhfTee8ufmYi9dQFDPQ75VLp2W4VUb9KTPcQ7QigDrK1whw_264rb0ApEVMZzN0-wnUNy3B0on8pInIr_bRh6kCBExLN3cyo7t4Ctk95YvINasUtix3qLsRM-KMR1CBg50FGd_KOlByywK-Vsz540_zXmd8_yP5HG-BKtkZhD-09LEmvtjzqsz7Bi9g7O589wqQBRlmi0C6yGL4_kFjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معرفی فیلم: داستان ازدواج | (Marriage Story - 2019)
🔹
ژانر: درام
🔹
امتیاز (IMDb): ۷.۹
🔹
خلاصه:  «داستان ازدواج» روایت فروپاشی آرام زندگی زوجی است که هنوز همدیگر را دوست دارند؛ اما دیگر نمی‌توانند کنار هم بمانند. فیلم با بازی خیره‌کننده آدام درایور و اسکارلت…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/665700" target="_blank">📅 21:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665699">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9big_G9LtPX34i3G4Fxu5gCUakbs35r0jXmU1hHBcPNIabkAHajffJ6J63DAGObJxicLkeU-0onIAJu3jPV_uBjDQ3DpZwYjEqQeci_YYfCDw1dipYQoclkJ5YJIxfLQT03ZG_VGGUEFQszkfKYYIHedk4SH402dtMfFHCCFci8cEFCroTTnaAATHH6KKR-EoIn3t7SkvODkJ2z7YoSf352n6pKWwmPqVfbjfb8V06j59N4DiBFqW3_38AmAzEfZ3eP5dAIscTZog_6xJ4KzEjyJWWT_swTQvKj7E_V7FYX1xKrKYmAnft0VxXgwXW3fqPX8X-OeF-EAdvTqWx76w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رؤیت شیء ناشناس پرنده در رادارهای هوانوردی آمریکا
🔹
ادعای فلایت‌رادار از شناسایی یک شیء ناشناس در حریم هوایی آمریکا خبر داد که ماهیت آن هنوز تأیید نشده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/665699" target="_blank">📅 21:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665698">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GT8jK3vfpgz5sIk9JAFYD51_4KCn3m5eLUvAeKSjSF1bRYUp2zv2qbOM-sJgOBs9XP_NA10m0w3RKMYwRh-bimjZGhYxLQIV0rMhCEpi319IQMlTRQf3C0GGAs8RjYK5sWwDK6TGvRWzR9uYS9spFU9xUl2NQZblfIN2hHRoeAGlnSCU9Q2o9JpxJargozom-JBm8VDNZ4TFhWvll6NKKrWaVGFFgmEXrTxlFWKJ6OX7Rigp2-nol0uL3zCuTYj97MF9U4-rVRVTK69YTLPwmlAOFQI9gawzQTT00Hb_RYAsG55l9nqdgLmud5NtOxSpkrap7wN062djcWKYKCpHgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستیار رهبر انقلاب:امروز، عزتِ یک امت، بر دوشِ دلدادگانِ راهِ اوست
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/665698" target="_blank">📅 21:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665697">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
کشته‌های گرمایی در اروپا از ۲۱۲۹ نفر گذشت
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/665697" target="_blank">📅 21:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665696">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
آماده‌باش گسترده اورژانس برای مراسم تشییع رهبر شهید
شروین تبریزی، سخنگو اورژانس استان تهران در
#گفتگو
با خبرفوری:
🔹
در مراسم وداع با پیکر مطهر رهبر شهید، کمیته امداد و فوریت‌های پزشکی ستاد برگزاری مراسم، تمهیدات گسترده‌ای انجام داده از جمله ۱۵۰۰ نیروی عملیاتی اورژانس که در تمام این چند روز برگزاری مراسم به صورت پیاده و یا با ناوگان حضور دارند.
🔹
همچنین ۴۴۳ دستگاه آمبولانس، ۳۰۰ دستگاه موتورلانس، ۳۸ دستگاه اتوبوس آمبولانس،۷ فروند بالگرد نیز در نظر گرفته شده است.
🔹
برای نخستین بار قرار است انتقال ریلی برای مصدومین داشته باشیم و در ایستگاه‌های میرزای شیرازی و شهید بهشتی ظرفیت پذیرش داریم و از آن‌جا مصدومان انتقال پیدا می‌کنند و خروج نیز در ایستگاه جوانمرد قصاب و ایستگاه مترو سمت شهرری به عنوان ایستگاه پایانی می‌باشد.
🔹
قطار به صورت اختصاصی برای اورژانس درنظر گرفته شده و ۱۴ اتاق سرد و ۱۲ ایستگاه درمانی نیز برای شهروندان احداث می‌شود.
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/665696" target="_blank">📅 20:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665695">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87d68fa36a.mp4?token=rQLqHoyR9zCAcqUdcDckccMsvkx81KY3AcOnCtAbI6m-KTLCBUH3lDJGteMxBsZSJa-49WAvL64q3CVSBm_cI9seNhxSPo9mDiGp-q5S6LdW3Es_TIGU0bkZlzKVTMPPfT3-_ujWvjTtYfzN2CQYrXkLVUUHob4B6qqkuYfIzoQOPlfql4jfqmBy3Z9xhamBspzatK79n5ypZJ1bnjfUy1gU9J2c3lJLJZu7FnlMdYwAhdgbjJEJJAFVSb-zlg9t7Fm64727MYCAukQT_jJgwRcCsURvuuInoacxP-uxa1Q8k2p7IksG7HzXpxtkcMnHWIY7AFCC92TBw09yEGhxbIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87d68fa36a.mp4?token=rQLqHoyR9zCAcqUdcDckccMsvkx81KY3AcOnCtAbI6m-KTLCBUH3lDJGteMxBsZSJa-49WAvL64q3CVSBm_cI9seNhxSPo9mDiGp-q5S6LdW3Es_TIGU0bkZlzKVTMPPfT3-_ujWvjTtYfzN2CQYrXkLVUUHob4B6qqkuYfIzoQOPlfql4jfqmBy3Z9xhamBspzatK79n5ypZJ1bnjfUy1gU9J2c3lJLJZu7FnlMdYwAhdgbjJEJJAFVSb-zlg9t7Fm64727MYCAukQT_jJgwRcCsURvuuInoacxP-uxa1Q8k2p7IksG7HzXpxtkcMnHWIY7AFCC92TBw09yEGhxbIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خانه آنشرلی در دنیای واقعی
✨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/665695" target="_blank">📅 20:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665694">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3f1f62805.mp4?token=TGKdsWLTQ53l5NjQbnMNh7FI_k5PqE7WmjmvZq3ArLPn96ddsPvOKvHsLNXrCNJUVM_ei60UCxAY9_OUVjb8SSOetnn48e8VadmfTq1TZbUpx0agdBc7XHCFjLgIwPmh9rPYUAESCAxUTkaphlzgOrgn1LcHlhTixxFxtaRd0KdQa6I9MCJsDfEr4LZJgjvRHO0K-uLrniSpkBNeocidaQ9goMC0mLzdGSQXq709592CrwqJHUdMOXbfsW1ECBHIpR357Lvn86tGqWehv8PhGSJ50fd1gkf83YhfEB7HYsZGahK6DC8JkhHOVVNlr4SY6AgO-bmG09IxXvIfuahUQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3f1f62805.mp4?token=TGKdsWLTQ53l5NjQbnMNh7FI_k5PqE7WmjmvZq3ArLPn96ddsPvOKvHsLNXrCNJUVM_ei60UCxAY9_OUVjb8SSOetnn48e8VadmfTq1TZbUpx0agdBc7XHCFjLgIwPmh9rPYUAESCAxUTkaphlzgOrgn1LcHlhTixxFxtaRd0KdQa6I9MCJsDfEr4LZJgjvRHO0K-uLrniSpkBNeocidaQ9goMC0mLzdGSQXq709592CrwqJHUdMOXbfsW1ECBHIpR357Lvn86tGqWehv8PhGSJ50fd1gkf83YhfEB7HYsZGahK6DC8JkhHOVVNlr4SY6AgO-bmG09IxXvIfuahUQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: در شورای‌عای امنیت ملی از ۱۳ نفر ۱۲ نفر نه‌تنها به تفاهم رأی دادند، بلکه از آن دفاع هم کردند
رئیس‌جمهور:
🔹
هیچ گناهی بالاتر از اختلاف و تفرقه نیست؛ من خیلی حرف دارم که می‌توانم بزنم ولی وحدت مهم‌تر از این حرف‌هاست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/665694" target="_blank">📅 20:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665693">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
آغاز راهپیمایی اربعین حسینی از راس‌البیشه در فاو، جنوب عراق
🇮🇶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/665693" target="_blank">📅 20:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665692">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
چرا او از بازگشت به دنیا پشیمان شد؟
🔹
00:07:10 عدم اجازه ورود به هاله‌ای از نور
🔹
00:13:50 سوختن دردناک چشم و دهان با گرمای سوزان
🔹
00:26:00 درک شرایط فرزند سقط شده در برزخ
🔹
00:33:10 امر و ابلاغ به ملک‌الموت برای بازگرداندن من به دنیا
🔹
00:45:50 هم نوایی تمام ذرات هستی با بیان مفاهیم قرآنی
🔹
00:49:20 زنجیره‌ای از عشق میان اجرام آسمانی
🔹
00:53:10 درک عمیقی از تاریکی و موجودات اعماق دریا
🔹
01:14:10 مطلع بودن من از محرمانه‌های نظامی همسرم را برانگیخته کرد
🔹
قسمت بیست‌وهفتم (مرز نور)، فصل چهارم
🔹
#تجربه‌گر
: زهره ابراهیمی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/665692" target="_blank">📅 20:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665691">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee6fd3f9e1.mp4?token=MI7nOPf7WLl6v9xsCGqmJDJrAYWfNy0FBQ8WACZXLxkfqqgFx7XCSIWe5mZrhzaP8ZvNeDlftU01poV7oqcUwAkkOkKL8T3b9ivlnamfi0Teb1EQRvfFb5KhzFBAaeKIa4nKjLN9NyylIbxFCtB31m234GyavBtI2ATGkhDk8x-_WkAR9OGDxzGqrJfqnneOSkbUQPIHXyrNsYMhRBKOI8M1aKzTMJYVzkDFBrPUIkdyPo6oLJOcfBynFanWwdeXa-uKmAYgm-xY8-UxpA0HCsuylW6Ke9ebvt61NEmtnSM77ET7to_uArknqLuQQHRaW3lPNkav0fCFv3D1hjLkqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee6fd3f9e1.mp4?token=MI7nOPf7WLl6v9xsCGqmJDJrAYWfNy0FBQ8WACZXLxkfqqgFx7XCSIWe5mZrhzaP8ZvNeDlftU01poV7oqcUwAkkOkKL8T3b9ivlnamfi0Teb1EQRvfFb5KhzFBAaeKIa4nKjLN9NyylIbxFCtB31m234GyavBtI2ATGkhDk8x-_WkAR9OGDxzGqrJfqnneOSkbUQPIHXyrNsYMhRBKOI8M1aKzTMJYVzkDFBrPUIkdyPo6oLJOcfBynFanWwdeXa-uKmAYgm-xY8-UxpA0HCsuylW6Ke9ebvt61NEmtnSM77ET7to_uArknqLuQQHRaW3lPNkav0fCFv3D1hjLkqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرواز گسترده بالگردهای اسرائیلی در مرز لبنان
🔹
منابع خبری از فعالیت گسترده بالگردهای ارتش اسرائیل بر فراز مناطق مرزی لبنان و فلسطین اشغالی خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/665691" target="_blank">📅 20:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665690">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRBXiGgdHGR_o5UWiEPhvOjcc_ysxbgUiu8N8TY7yMMNtCavPKbl3KvUquUMeaoOZrYmFGR7N4fcSMYLOcS6YTPOrGzTIjH9nrMlfaq5hf1MSg61VuKO9oqTdWC9USr6lhvQnEdItGznvkKba2vIVE3KyIdvAi2Wv4DOI5EzjS2qziRnnhNt0nLXHC2vlJJUSahX5MP2jJCCUbJL8XHb_jWq45vTFRP0Bkwl2d93JkBFirHZH7eD7Xc-y1a3ATvrIx3m4olKeetoaYOSpfUuF0ria9Eq1x-BUI8doVkJSFni1EHXC5xiS8NhtHjs6MvQkXMgAze48emI_K_HNa1Oqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری | کمپین «جامانده»
🔹
اگر به هر دلیل امکان حضور در مراسم تشییع را ندارید و میخواهید در این مراسم حضور داشته باشید، یک فایل صوتی حداکثر ۱۵ ثانیه‌ای برای خبرفوری ارسال کنید تا یک همراهِ قلبی به نیابت از شما در مراسم شرکت کند.
🔹
در پیام صوتی، فقط نام خود، نام شهر محل سکونت و جمله‌ای کوتاه درباره همراهی و ادای احترام خود را بیان کنید.
🔹
منتخبی از پیام‌های صوتی ارسالی با عنوان «جامانده» در خبرفوری منتشر خواهد شد.
#بدرقه_یار
🔸
ویس خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/akhbarefori/665690" target="_blank">📅 20:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665689">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e6305f707.mp4?token=vRPhI25xG74dHEPBZP3sYCvesqCQGRidTdCwyS1ZbmzCDDTzPSDO_3I3K55-zTjQNPLzEvw0CNPfdfZcTfTDkNrQd8PPmudBlA3KZPBvaTzop3Z6_WxlqehBnblQI0XesvZV56CiQMnTkm8rp7lUZB1FlQRGrqYN3wT47rcHkPEnPOsW7QEhVJN64Su2RUC41J4oGGvV1izs2VMuqDASGm1BUoZSVsZHLIRuSVjRCWWOGnjDaZH8DBnPmQ9VoCLoP2YksEGFE8OwSU6bMLqL6oY5Lc7YUy3UpMMdobwfBdaDNkjyoNBQUWiLXUhxll2yWlfTXaL7SvUYWmI6XyOT9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e6305f707.mp4?token=vRPhI25xG74dHEPBZP3sYCvesqCQGRidTdCwyS1ZbmzCDDTzPSDO_3I3K55-zTjQNPLzEvw0CNPfdfZcTfTDkNrQd8PPmudBlA3KZPBvaTzop3Z6_WxlqehBnblQI0XesvZV56CiQMnTkm8rp7lUZB1FlQRGrqYN3wT47rcHkPEnPOsW7QEhVJN64Su2RUC41J4oGGvV1izs2VMuqDASGm1BUoZSVsZHLIRuSVjRCWWOGnjDaZH8DBnPmQ9VoCLoP2YksEGFE8OwSU6bMLqL6oY5Lc7YUy3UpMMdobwfBdaDNkjyoNBQUWiLXUhxll2yWlfTXaL7SvUYWmI6XyOT9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: من به عنوان مسئول دولت نمی‌توانم ببینم مردم مشکل دارند و بگویم همه چیز خوب است
🔹
در مقابل دشمن کوتاه نخواهیم آمد، تا پای جان می‌ایستیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/665689" target="_blank">📅 20:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665688">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKS_XuxM-NkXNRH8TR3tVU-rgmowr7NTMOZegOIgWlKf0wQi0WWTZZ9dyIz5dwtiuR9uRZ3UH8KTfzsq9wPngLmYj3zL696jVlF204_UWBsx6jZxjULISOuZzzd-OfWZUW7Qp2fHJHThSL69G9p6T8sA04sG0UDOW3IGvQG8aMR24D9E_Hk_l5gZ4COTZQLlfqS_870Ti6xzFOuydgXxmA34mf5QdxErmXBUirbdnlSCqNrzTSDcjow6OA2un_iwtmZeJzugDd59ldW0uk6RaxlFn-46EycbVDe1xemdl223UyhkkCvDUCfcLvbmsyJdKMXGhq28-mkl4t3K1L3OGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همه چیز درباره عملیات بزرگ بغداد/ چگونه تریلیون‌ها دلار دزدیده شد؟/ مطالبی عجیب از بزرگترین اختلاس خاورمیانه
🔹
در میان متهمان، فردی بازداشت شده که همسرش به‌تنهایی یک ملک ۵ میلیون دلاری در حومه دبی خریداری کرده بود، و دیگری بیش از ۵۰ قطعه زمین و آپارتمان به نام خود و فرزندانش ثبت کرده است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3227390</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/665688" target="_blank">📅 20:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665687">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
همه با هم با افتخار میزبان مهمانان رهبر شهید که مهمانان ایران هستند باشیم
🔹
گپ و گفتی با مردم مبعوث شده؛ حاضری برای میزبانی میهمانان مراسم تشییع آقای شهید ایران چیکار کنی؟
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/665687" target="_blank">📅 20:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665686">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزارت رفاه: واریز ماهانه ۲ میلیون تومان برای متولدین ۱۴۰۵ از فردا آغاز می‌شود.
🔹
رئیس مجلس سنای پاکستان: رهبری آیت الله شهید خامنه‌ای برای جهان اسلام همیشه به یاد خواهد ماند.
🔹
حزب‌الله: دولت لبنان فرصت ایجاد شده توسط ایران را غنیمت بداند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/665686" target="_blank">📅 20:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665685">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81adfe9f60.mp4?token=SCRog0JFZ44JaMeyENWhD6X8J5rmJOpQccR8QqWfctZlfTBumlfXRHieHlfzSRqp9rGMPZq6nQTco78T7wpdkoT7wrMIhcKhpmPDvaOwCVWnS2_K_egJ7NaJm-Xr1yHS7jpH4eU6ntjEmDLWaziDJSgYH9IoA8Cw5xNWFGAV6K-YWQ1ruQ_xlMGyPAoIC87pidIRqj_HqnfKfXV-a92Bs-bhT2uCGdveC5ZrGQ_Zm3y2VhaqL_alJmnkpMQuqMETohysnJgPaWTQ4BPa3FwztHk2C_z09OVFvhVbox5ehbEV6y28MY66hCpTmMTYhe7Gc2fhNX47CVDVYQ4-xbBiwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81adfe9f60.mp4?token=SCRog0JFZ44JaMeyENWhD6X8J5rmJOpQccR8QqWfctZlfTBumlfXRHieHlfzSRqp9rGMPZq6nQTco78T7wpdkoT7wrMIhcKhpmPDvaOwCVWnS2_K_egJ7NaJm-Xr1yHS7jpH4eU6ntjEmDLWaziDJSgYH9IoA8Cw5xNWFGAV6K-YWQ1ruQ_xlMGyPAoIC87pidIRqj_HqnfKfXV-a92Bs-bhT2uCGdveC5ZrGQ_Zm3y2VhaqL_alJmnkpMQuqMETohysnJgPaWTQ4BPa3FwztHk2C_z09OVFvhVbox5ehbEV6y28MY66hCpTmMTYhe7Gc2fhNX47CVDVYQ4-xbBiwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت عجیب آشپز سابق صداوسیما؛
وقتی کودک بودم لباس‌های دخترانه می‌پوشیدم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/665685" target="_blank">📅 20:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665684">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0539c154ff.mp4?token=rwlfdRo-UQe_yByaZ6ZV55Tt1siD34BxI7huMQYA5h36X2ju8rvN0g7-Z8KKZcE0oatAK239edEDSR6t44tO9OLBxxfk4IuMNug4FjjfHAEK-Nj4fcNR7cIglkaqG2Bs0iRQXMWSUCmGxAXt1iaUu0lfZ0a0B2T-qNZUbMY6tSrGB6wc9ql2qU7gSEngVjzA2YyhRe2gCQz7iWhfFJ_zW3nW7DVeXmzUUWpgGKGwqTgdv8VsmVcNb5GP_9naUIjv5QoZuOrRuVerR5PkWNNfwFKqvP0XIXmH0aTRklMVMyIjMW2bAUueutXWeLWnWG7Ua8KPEgFCD1MfSaW6hW0LV0loklyf9acaMR9FctkpP4XWw_1fgzPq5WFGCwbd874QhNPQw75EzIPcTHr4s7HhPPVtlIFa7MFwkKilmHUoL-Je1ajPH3iv7PND-O96BaB3OnUQfdzGvkczVp3ExFY03Q7XxVyDsAfNEvefeKURUPCqpnxmJh7g-AEVrQZVUQpJc3EoqaRoiLU8fCRYzHtFgzd1Xv9WWwe_kBFp3Si8I_E-Ks6i8JlnOWV5XV-TkmUrI3qdJbEtt6bOmwTc8U-yRCrVuxG66927Uj58H9DC80oVBFSyZ3kwyceBhvTr0cHh-U0hP-PQwjmwZqLhF_78F1T60uUyixFsPp5sdvv5hCk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0539c154ff.mp4?token=rwlfdRo-UQe_yByaZ6ZV55Tt1siD34BxI7huMQYA5h36X2ju8rvN0g7-Z8KKZcE0oatAK239edEDSR6t44tO9OLBxxfk4IuMNug4FjjfHAEK-Nj4fcNR7cIglkaqG2Bs0iRQXMWSUCmGxAXt1iaUu0lfZ0a0B2T-qNZUbMY6tSrGB6wc9ql2qU7gSEngVjzA2YyhRe2gCQz7iWhfFJ_zW3nW7DVeXmzUUWpgGKGwqTgdv8VsmVcNb5GP_9naUIjv5QoZuOrRuVerR5PkWNNfwFKqvP0XIXmH0aTRklMVMyIjMW2bAUueutXWeLWnWG7Ua8KPEgFCD1MfSaW6hW0LV0loklyf9acaMR9FctkpP4XWw_1fgzPq5WFGCwbd874QhNPQw75EzIPcTHr4s7HhPPVtlIFa7MFwkKilmHUoL-Je1ajPH3iv7PND-O96BaB3OnUQfdzGvkczVp3ExFY03Q7XxVyDsAfNEvefeKURUPCqpnxmJh7g-AEVrQZVUQpJc3EoqaRoiLU8fCRYzHtFgzd1Xv9WWwe_kBFp3Si8I_E-Ks6i8JlnOWV5XV-TkmUrI3qdJbEtt6bOmwTc8U-yRCrVuxG66927Uj58H9DC80oVBFSyZ3kwyceBhvTr0cHh-U0hP-PQwjmwZqLhF_78F1T60uUyixFsPp5sdvv5hCk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرگ تدریجی امپراتوری آمریکا از زبان تحلیلگر امنیت ملی آمریکا!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/665684" target="_blank">📅 20:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665683">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">محکم در آغوشم بگیر.pdf</div>
  <div class="tg-doc-extra">39 MB</div>
</div>
<a href="https://t.me/akhbarefori/665683" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
فایل کتاب محکم در آغوشم بگیر
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/665683" target="_blank">📅 19:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665681">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IiKQROxgQymi4eTRkl_wS-FHZ0TSA1s92GlThO4asVkw0pMc3XW21XnhQ9Q2JlMRmmIIARcprULK3A6nCLuZcr9rSOSU8h1vAAcBpr4TjnMh17-hNjrLTdwwBNIkk0gzjmtkvPHpqEQbnCWepnIMoKwBE1s5TrQTRiVvNpUPJ3OyMwZA57Yw0i2ZstqIpFJ1BnR17UcMmUYdtce3CrFVyxrhnPE7QK-aTwQIhDk8RnjZkMeVUNxmU20arxiaVxrdD51-4w3hi-ezGoQTxMUr2y6ouCYNX6nRqRX6I8mGiDmN__UIP3j-7veqimXCAQxwMW1pID_1SOPEPPu1Koz90g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y892wUHbzrfFxYp6b7sbPA3B0WDIXL5VxotEl3dYKL-DZ7A0gDO0fM5EefQk-n4egCxuYhrNS1juMCo4LKhX0SHxwaveba2Fv_pNWxi1cubNDWFrZ4IEinfaxVJlXSRvU1RcFV2WtsD1BulfbM-61-xWFuF8GR_ZH5juIxuU1aSCLuqudRPaJf_uY0HOZo4aBnI-ljYoSh1iLsFJMpYYJ_0ryZPulB-bZvzGgrZ_wcUap8JGSrBgDFLQBwRvqVc2jPtYl_JIxPHVZ7hpL9eE_fqYEYmgYHQ3tUm0LNyNKCpd5kx-0A_asL3eQx62QMdXtq38sNEYWZRZqqZtDlaknA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر رابطه‌ات سرد شده و نمی‌دانی چرا، این کتاب جواب خیلی از سؤال‌هایت را می‌دهد!
🔹
«محکم در آغوشم بگیر» اثر سو جانسون، یکی از تأثیرگذارترین کتاب‌های روان‌شناسی روابط عاطفی است. نویسنده نشان می‌دهد ریشه بیشتر اختلاف‌های زوج‌ها، کمبود دلبستگی و احساس امنیت است نه نداشتن عشق. کتاب با مثال‌های واقعی و راهکارهای عملی، مسیر بازسازی اعتماد، صمیمیت و رابطه‌ای عمیق‌تر را آموزش می‌دهد.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/665681" target="_blank">📅 19:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665680">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
نشست شورای امنیت و تکرار اتهامات آمریکا و بحرین علیه ایران
🔹
نمایندگان آمریکا و بحرین در شورای امنیت، بدون اشاره به تجاوزات علیه ایران، تهران را به حملات «بدخواهانه» و «ایجاد ترس» متهم کردند.
🔹
این در حالی است که ایران پیش‌تر پایگاه‌های آمریکایی در بحرین…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/665680" target="_blank">📅 19:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665679">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8Ud5qP0_uF4t4FZrof5_axMbjlU9Q-PB__hkzMikMYVsrhAKpWEEt76hmuQf2KQHljxj6GNQ2vwmYh3GxKzcABJdObkB6a6fBzZCde6qqzFhPS4OHrL_ybTayarWZjQIpgVc6fg667wK3l_a31U9TfACWwpwZabKuZcqM7my3PAgCBx6GY__KScehpFnUOqGatTL65UfLGMO_KKuoF0_-vpWcv5gXfC28sfgmOPoeAURSZrD_6jkJXDjbjNAHV1eiaHVQj3vvT9wdzTumj2QkCeVR3S4PO3uUKiYB4qVdkj2c2SfU8Ukrbo9C0zrSekSVP__-Ie95_lQ8IVusmm8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنایت تازه در جنوب لبنان
🔹
نیروهای اسرائیلی خانه‌هایی را در «بیت یاحون» به آتش کشیدند و یک پهپاد این رژیم «النبطیة الفوقا» را هدف حمله قرار داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/665679" target="_blank">📅 19:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665678">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEqAGXXTZOmYsHu3suroRe4qV-ieaZmN5opPXahCOXkpy51MpHl9028KFNIa955wq6JLuV7UsuWlJleS5OkGLoxwvUOq_H7Zbminj4KlKUnbPnMkTquLtJUuzKWPIU_JEe1RCKkIbu-BNJIIlfj9DgF_iviTeIdzqtRqB9w7-BTvG_9GT3G8z4_a87qQc9GXtEFxvtCOJqIaCUtoROUE26sjbLTBBDa55AW96MdCqjgWDcUWCi--Wfg5Kb8wsfsKJEcsfme3dR4vtrssT69Xa80Wb2vwuvR3hc1QBQ5W6KKzDMq8nJ5atA5W-Rhxvf0fnkk_p26-y6BoiU7wQ1kJfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور سردار وحیدی در مصلی تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/665678" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665677">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
تلاش آمریکا برای جلوگیری از کنترل ایران بر تنگه هرمز
وال‌استریت‌ژورنال:
🔹
آمریکا و عمان در تلاش‌اند ایران را از دریافت عوارض و اعمال کنترل بر تنگه هرمز منصرف کنند و از وعده آزادسازی بخشی از دارایی‌های بلوکه‌شده به‌عنوان اهرم فشار استفاده می‌کنند.
🔹
تهران به این پیشنهادها پاسخ مثبت نداده و تأکید کرده هرمز «تحت فرماندهی ایران» است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/665677" target="_blank">📅 19:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665676">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
نشست شورای امنیت و تکرار اتهامات آمریکا و بحرین علیه ایران
🔹
نمایندگان آمریکا و بحرین در شورای امنیت، بدون اشاره به تجاوزات علیه ایران، تهران را به حملات «بدخواهانه» و «ایجاد ترس» متهم کردند.
🔹
این در حالی است که ایران پیش‌تر پایگاه‌های آمریکایی در بحرین را در پاسخ به حملات صورت‌گرفته از آن‌ها، هدف قرار داده بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/665676" target="_blank">📅 19:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665675">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZA6ZcwPK1KhbxkvfznfwIhMjjaEGyMXFWh0mLpXHQIo4sfjVFFvHw1ZXjDZ27jzvARX0wHoILWx_971F9eGSg6jIrbcH530lXYrR8NroKnrqXa9NZ4yIJzIib4e5Pis-aWxjpcHHCWnfmtJe3lre6N9PFA0ecopAmygbaxct3OZ03B7IHP6_REyPHzmXwwXa51CAL113Os3nNIdBNkXCyqp-gwL0r3xwuQ0ATJYhQkM1UgOVOOUQP7x6mFJrTUmpT9hC_leaoihKe905asb2wz2xeF2Nqe1DdYEsRx5WmTq5NWOM6o56hVwox5kTN01ZhD1WRioHl1Lhmr5Pa5Xag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تشییع‌ پیکر امام خمینی(ره)، ۱۴ خرداد ۱۳۶۸
🔹
عکس از علی فریدونی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/665675" target="_blank">📅 19:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665674">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7f19774de.mp4?token=ZC6LOBnET0_DWiMe6iHXU-7Nd0_VrQOR4D2SQsGb-QfY9UzzwTE_hKTnRAif5-5UNd2zJi0NMzWsMVqsUo4JSXC5hRg2xJueJ-Dh-Jl2oKKpxre1Dff3dlhmdLiDOZT15bjKy8mqUHfYrXqMhtlp2iMOw13X9JmWwkZ99jkENElX3uftyCK9IWbzCngwsvX0ln_7Nh4AhL77w6jMo1GqmJTlz32kP2B8culzP2aDcRXCizAEFZOF8L-u_vjwsk_7kTiv-zQ5jb3n5QSZoHnlBoKKezXIeJOmXuyWmezx8i-GQbY94omVjg17zPk0ZNAuOowEhP8Q06DL_cTKsxv2Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7f19774de.mp4?token=ZC6LOBnET0_DWiMe6iHXU-7Nd0_VrQOR4D2SQsGb-QfY9UzzwTE_hKTnRAif5-5UNd2zJi0NMzWsMVqsUo4JSXC5hRg2xJueJ-Dh-Jl2oKKpxre1Dff3dlhmdLiDOZT15bjKy8mqUHfYrXqMhtlp2iMOw13X9JmWwkZ99jkENElX3uftyCK9IWbzCngwsvX0ln_7Nh4AhL77w6jMo1GqmJTlz32kP2B8culzP2aDcRXCizAEFZOF8L-u_vjwsk_7kTiv-zQ5jb3n5QSZoHnlBoKKezXIeJOmXuyWmezx8i-GQbY94omVjg17zPk0ZNAuOowEhP8Q06DL_cTKsxv2Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا استفاده از داروهای روانپزشکی اعتیادآور است؟
/ تلویزیون اینترنتی مدار
این گفت‌وگو را اینجا ببینید
👇
https://aparat.com/v/jjy2nnk
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/665674" target="_blank">📅 19:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665673">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCi23Zulef5Ui9m9rGi6AsPM27yQcgBjLno194v15WwG-SIqXIiXMgV68UtC_OI8CGvJ0VjiOaWcBW19MyHEBeLskWrhn0V_44WPdEMc0gGSE1ScDTcXRGyUewVTGHT0n1I25mPxtZV2wHtEEmBY7GET_oKQ8g3t_qUlUcGVg6avMtGhYa7bNV2lJMgydfUl_hy-2Trx5Eg5RdyFTGUnRg9usefkASxo1F-Z4Dg20fx3wIQqwGaecXwAn8rpIUbHttPltPx07jiri3nHpKyCb5977RWblIZ8HRQwqcj1v-x6BAaSH-gCMobbQh2HdjleCprWg2PO3bM7LVPqNAdKYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قبل از خرید آپارتمان، این ۳ مورد را در پارکینگ چک کن
🇮🇷
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/665673" target="_blank">📅 19:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665671">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeM9lTgRZqoiBYJ9gJfwgDkhLvoOFu_ccVTvTLahVqdu7m2srmWKct_di-wkDCjrogHCIQ7zzQGI6NMYV61HicBMNcllXftU29963WqVHnqenzPijBIRzgboJzAGj-GWcbCyv1PskPIhkeaadfX4VhnIQvU_PagYD7lrS-WTeBKo6eEo6ZDBWS0ezV40BPdrms3VcftDS6skyGW-ulKiWS2h--X_rYD3S4nT9XJspN-xvlmxBlUAsYUgbH3_Azq_PkLliLcwX3m6aQ_0RVuNrNq_BSA9ja_b11nqED54kNQGV5QvkDAdt0FvXr1eeb_zXiXj66B7leR7y5rN8BZzyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه عواملی جان کودکان خردسال زیر ۵ سال را تهدید می‌کند؟
🔹
عفونت‌ها با حدود ۱۴٪ و تولد زودرس با ۱۳٪ از مهم‌ترین عوامل مرگ کودکان زیر ۵ سال در جهان هستند.
🔹
سوءتغذیه و بیماری‌های قابل پیشگیری همچنان سهم قابل توجهی در مرگ‌ومیر کودکان دارند.
@amarfact</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/665671" target="_blank">📅 19:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665670">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
هلاکت ۲ نفر از عاملان شهادت کارکنان فراجا در نوک‌آباد تفتان
🔹
در عملیاتی هماهنگ و منسجم یگان‌های عملیاتی فراجا با همکاری نهادهای امنیتی استان، ۲ نفر از عوامل اصلی به شهادت رساندن کارکنان پلیس استان سیستان و بلوچستان در نوک‌آباد شهرستان تفتان به هلاکت رسیدند.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/665670" target="_blank">📅 19:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665669">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7gkmBBRtDYnd2Ypz0vcsKs0aogVVQNqnaBfLWXiCyJo67RprqkApHT_LN9Eq3-Yzd7_0iwdqZG_MgbqEztkuo2d7I7CJcIFdX6fLRAMwK3PzHj0sl5_-eiGQTptFfeS1qjvV_SHesPyABcFL2V_Zp_UA1tDYxR50C-C6sdPJHZazBoKiRBbaLX6hOyTwyx0_mWvoqm-UJD9dHxFmIQ3xn6SH6MINupLEUukh2Sim4hKi-RckFhtf5M65XE4xJ184yOtyG1kosIlGqH4IR1k4woWC6nGzWr6E0L_WdTRPe6bDX9rxJxNnaw4HckoYAOxK4OZRGdnDoeWkC-gGeivrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقش شما در بدرقه (۲)
🔹
به عنوان یک کاربر فضای مجازی نقش شما در بدرقه رهبر شهید انقلاب بسیار مهم است اگر از آن تصاویر و ویدیوهای امیدوارانه منتشر کنید. امید پایان‌بندی این روایت است. امید یعنی خون شهید به ثمر نشسته است و فردا از آنِ کسانی است که امروز ایستاده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/665669" target="_blank">📅 19:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665668">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سفارت اتریش در تهران فعالیت خود را از سر گرفت.
🔹
سازمان هواپیمایی: پروازهای داخلی و خارجی شنبه و یکشنبه برقرار است.
🔹
تیپ «گیواتی» ارتش تروریستی اسرائیل از جنوب لبنان عقب‌نشینی کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/665668" target="_blank">📅 19:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665667">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9KYjFySi7HTce-hU7P1xGK9l5FmC7fspfMBlmmoOIn8jYCirz_VZ_kzqwjjUqZYveCR1cge_II9H40exZfXXRQVQisX2fYTeei5rv9OVWO1lCWOdNfQJSvIGqnUN1Zk9dlemOPRc2_H4EhqIT7lpC1Lx4xaQt8DcaZHTibU_J3IMXAqal76q2mFvKrrCk1UkxbgAtbEBkjFdNmCELFwPqmEvbRqqRgJjc-xjE2fzibLfO_DbZpe1eN1x9KHIEKP0uxA6nsYohB27hGHY3tuiRPiU4dpAC6NMh_xpUPAf6MzgwcjTBVdaEDfHFPN-rfBwgtiCEJT_GoQ1zGGFsFRwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/665667" target="_blank">📅 19:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665666">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbRN5XNJSPIYT5LdMKxfjgoF54KKniU2hBIk-5KDKmH91nhMh52OUDNS6y1ZjFdkqXFSfuFZrr-wbb9Dupx9U7Cz3KwNnAmk41ArA-fHZtNxW6grtND2N4zEFBioCXzrXPpcZrmeIZ7u4X0xn-KO8_UUdsasOhe7v_AfWUqe9rBaEvKu4f9G5HITDxmwU57U3ZyzfFrPkPCCcHxQll-ewybzpe5_6byCzE1_s_JJCaQBhvECAvllpQJBxG60FP_MRjZP4oBGnAxhOqL5CqDRj1CXd1ivRsvu0BZ7l9ex5jcn8DtWpd1KIalIsKknKNsgDeHoik7-ulk-GIdkfVEgHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
احتمال تغییر زمان برگزاری جام جهانی از تابستان به زمستان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/665666" target="_blank">📅 18:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665665">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">آیین نامه سوگواره بدرقه یار.pdf</div>
  <div class="tg-doc-extra">260.6 KB</div>
</div>
<a href="https://t.me/akhbarefori/665665" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">◼️
آغاز ثبت‌نام و ارسال آثار به سوگواره رسانه‌ای «بدرقه یار»
ثبت‌نام و ارسال آثار به سوگواره رسانه‌ای بین‌المللی «بدرقه یار» آغاز شد. این رویداد با هدف ثبت، بازنمایی و ماندگارسازی روایت‌های رسانه‌ای و هنری از مراسم تشییع رهبر شهید انقلاب اسلامی برگزار می‌شود و پذیرای آثار فعالان رسانه‌ای و هنرمندان از داخل و خارج از کشور است.
علاقه‌مندان می‌توانند پس از مطالعه آیین‌نامه، از طریق لینک زیر نسبت به ثبت و ارسال آثار خود در بخش‌های مختلف سوگواره اقدام کنند. همچنین در صورت عدم امکان ثبت از طریق سامانه، امکان ارسال آثار از طریق شناسه رسمی دبیرخانه نیز فراهم است.
#بدرقه_یار
◾️
لینک ثبت آثار:
https://survey.porsline.ir/s/aU5VZuaW
◾️
شناسه دبیرخانه:
@Badraghe_yar
@Badragheyar</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/665665" target="_blank">📅 18:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665663">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad90dc443f.mp4?token=V7aGcdcMOGZfV6s9RVVpyZ7azaoWQcm-nwFqn5RQaBla3r6s9eiy03pcssDmtRxg-L4ZTeuL-gm5mqcFTsEqjtm8UMFEVeeMDQPeXrJpwvMBrpMmFC_TH6QIlvn4mqtbhiW7ZSgVcXo2YPdOgmM922egrKIshdCeAMHnKxcQS5YLSaPRycre6gJP_ANg96mCHpoZoauIRcXVHFAj2uQQ5cj78PRV5oK98gn-zPcivdsJeWRCKKXD966WH7QBKsKOwySArH1OilFY0KIcE2o9K57vzt8DKlEtGKidMyKrSUdt_ZSMoP56eCVtM8eyLlZWhUN7BZBYYk5m-Bkfdmhvlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad90dc443f.mp4?token=V7aGcdcMOGZfV6s9RVVpyZ7azaoWQcm-nwFqn5RQaBla3r6s9eiy03pcssDmtRxg-L4ZTeuL-gm5mqcFTsEqjtm8UMFEVeeMDQPeXrJpwvMBrpMmFC_TH6QIlvn4mqtbhiW7ZSgVcXo2YPdOgmM922egrKIshdCeAMHnKxcQS5YLSaPRycre6gJP_ANg96mCHpoZoauIRcXVHFAj2uQQ5cj78PRV5oK98gn-zPcivdsJeWRCKKXD966WH7QBKsKOwySArH1OilFY0KIcE2o9K57vzt8DKlEtGKidMyKrSUdt_ZSMoP56eCVtM8eyLlZWhUN7BZBYYk5m-Bkfdmhvlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افزایش کارت‌های جایگاه‌ها برای مراسم تشییع
سخنگوی اتحادیه جایگاه‌داران سوخت:
🔹
مردم در صورت امکان از ظرفیت کامل خودروها و وسایل حمل‌ونقل عمومی برای جابجایی در مراسم تشییع استفاده کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/665663" target="_blank">📅 18:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665662">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
آغاز واریز ماهانه ۲ میلیون تومان برای متولدین ۱۴۰۵ از فردا
وزارت کار:
🔹
اعتبار ۲ میلیون تومانی
«کارت امید مادر»
برای بیش از ۱۹۰ هزار کودک تازه متولد شده از فردا(۱۲ تیر ماه) واریز می‌شود.
🔹
این اعتبار در روزهای هفتم هر ماه واریز می‌شود./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/665662" target="_blank">📅 18:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665661">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0yFTnTG0i-bveTIcKCoHyeerdFWqzzNfGTKbJ06RXNo3dZ9kcQFXDD5WLagR2XAhCwvexH0YEhqlYwo-yTEFfqwtUAY9YbPKbj7wzESrayGH3iRKcqUIl9f2X8zq9XW_drCVIsQK9QWD-3MzVgmkci_Iiw6FKrqdXau0_U2rmfrDQhcErx-7lJtZ9yVF9XxQQJZqI0IPT3p-ezwzeZhOeE0o7WOH8G_hUz1_hGpAuRHx2omDNg2H4Nn3bdVxvJRY2eG1GQWocC5W6MNgAiPA4xoiU_9l0hMtir3CvRDyq5JTHdKCETqUn7uFujgPXFeTzEJroWqgPXzZWTSAUk8Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشته‌های گرمایی در اروپا از ۲۱۲۹ نفر گذشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/665661" target="_blank">📅 18:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665660">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
بلومبرگ: توافق کشورهای اروپایی برای پرداخت عوارض عبور از تنگه هرمز به ایران و عمان
🔹
خبرگزاری بلومبرگ گزارش داد که چندین کشور اروپایی با تغییر رویکرد خود، موافقت کرده‌اند که کشتی‌های تجاری آن‌ها برای تردد از تنگه هرمز، عوارض تعیین‌شده را به ایران و عمان پرداخت کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/665660" target="_blank">📅 18:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665658">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F16jXr9-NpDUmTK8NlOVXd2iDIDlenFW8GieL3IdPUefDaK-gNmo-HVE6fsO7pQ6AGIQgJBbzJxqAAT4TOvZWesl29ccaCjumBAWKwCl2dPs4HgOJcbK2cS3ktrBwG8muSgzM0X06w22Xrc-XCOVXC4czt-oBwsRdPmnLSztGeJaN62em4R6yME7P8YCAXV92zwr00zhFCU3GB8A2coN1X4pXRbzUhSxNt2ZLBZ62KvGQlrIAfEEIIam5j6sBZZa2udBT9fr4bG1_3LyTTlEGOdEnT0MHbWaVRcplz7rtgpAogcG-ZH5er2fx_z8_OezH9CrZhZ8J-w1ECyGQ7fwBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بابک خرمدین؛ ایرانی که بیش از ۲۰ سال با قدرتمندترین حکومت زمانه‌اش جنگید
🔹
۱۰ تیر؛ سالروز تولد بابک خرمدین از نامدارترین رهبران جنبش خرمدینان، سال‌ها در برابر خلافت عباسی مقاومت کرد و نام خود را به‌عنوان نماد ایستادگی در تاریخ ثبت کرد. روایت مشهور لحظهٔ…</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/665658" target="_blank">📅 18:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665657">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cbbbe6d08.mp4?token=riHmn7aww6isU8293DkFfRXNIyadJBXdCjfp27Xf9gcXaH7As9SZUgAQkyf4PoDj_g4wM7-t6_Zt4hWrRBunKrB3Lb1UYvdld5n9rvX1fgt6ZKTwRRAjN7f9ioEsnFB7b8u_xJUbn4IPAPHVHud6yGuTu6H3s2uZkAn9OOYm91UKRojn0kHsqtR_Buzcr0VpeHz7xUe_CmdrKAve_26gWXoJEYJZQMW38ovS_xi_CsKie2nrDf2srGg6bhRQ8TBPwTL51b3c975VH40ewX-I69ET5yEnyGIPNVv-OzCgBAOIZpobBejbs7rMaa3X1GLC4-ahT5igPUbxj_kO9vz-dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cbbbe6d08.mp4?token=riHmn7aww6isU8293DkFfRXNIyadJBXdCjfp27Xf9gcXaH7As9SZUgAQkyf4PoDj_g4wM7-t6_Zt4hWrRBunKrB3Lb1UYvdld5n9rvX1fgt6ZKTwRRAjN7f9ioEsnFB7b8u_xJUbn4IPAPHVHud6yGuTu6H3s2uZkAn9OOYm91UKRojn0kHsqtR_Buzcr0VpeHz7xUe_CmdrKAve_26gWXoJEYJZQMW38ovS_xi_CsKie2nrDf2srGg6bhRQ8TBPwTL51b3c975VH40ewX-I69ET5yEnyGIPNVv-OzCgBAOIZpobBejbs7rMaa3X1GLC4-ahT5igPUbxj_kO9vz-dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسیرهای ورودی پایتخت برای وداع و تشییع پیکر رهبر شهید | هم‌وطنانی که از شمال تهران وارد می‌شوند از کدام مسیرها استفاده کنند؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/665657" target="_blank">📅 17:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665656">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouJeQ4TgDa5ExyEMvVIXGBuKtqpWdxQHP5SkX_m5mcX9RGX5wDZtCOMv_bCoQa2udT4dAGAF6BWBogKaZ-jdC-H7RAsIHE5y4LIQJp9y3rU-FRKjQYrmqPvwTbxu8NrdoytemrBxx90Zj7EqsOwj-OLFMSbUcoHAhJKePkpHsTPcMZFqPq84gCoerubq4a6NIw6STVycZRhr4nwfOFRCC27qjUKYfNRpT8nYgmI8UGQe0ywVwpXMICwm3BpYy432igEIWFvUh4DhavGeRyWs0iCk365GKGVKCLM7pFohAwVGN_JPAJc8fFYvzgOpCOSiBuT9sDf82mZ5Z_Fl9YZZ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: برگزاری نشست امنیتی با کشورهای منطقه، تلاش برای سرپوش‌گذاشتن بر سیاست‌های مخرب آمریکا علیه صلح و امنیت منطقه است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/665656" target="_blank">📅 17:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665655">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a09954aaaf.mp4?token=RkKqlhix2wlR43BA9Tr36CEMM9Pq-TPmDS3TKJPzzhViYRRzqaNxirfG4_KOzcijtvp01-j9pHVedkM6D7IFNqHUPA8fABLYrZTHY3WTW1OaCH1vma07fHtyBOWdthWel7qOJCPaiMFv6pURz2o-JVakCaRqdQpIdcIfFI2x4bW6RutmrT_aaVFBtic2xEiTI9ABzDQThJW8L5dgpBzTeg6Y1nLTt1mZ-D6hLGtIcAIY43w8ipE3Wd8jOOQdnkr2FS6SXLnwEIlySs2OdzlNIcLiIIoiWS4a6JH08uyIXA-taf8TkQjcAhprzxuwg3jRyejNWxwnkuoVYoQKiMRHwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a09954aaaf.mp4?token=RkKqlhix2wlR43BA9Tr36CEMM9Pq-TPmDS3TKJPzzhViYRRzqaNxirfG4_KOzcijtvp01-j9pHVedkM6D7IFNqHUPA8fABLYrZTHY3WTW1OaCH1vma07fHtyBOWdthWel7qOJCPaiMFv6pURz2o-JVakCaRqdQpIdcIfFI2x4bW6RutmrT_aaVFBtic2xEiTI9ABzDQThJW8L5dgpBzTeg6Y1nLTt1mZ-D6hLGtIcAIY43w8ipE3Wd8jOOQdnkr2FS6SXLnwEIlySs2OdzlNIcLiIIoiWS4a6JH08uyIXA-taf8TkQjcAhprzxuwg3jRyejNWxwnkuoVYoQKiMRHwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک ربات خانگی که برای انجام روتین‌ترین کارهای خانه طراحی شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/665655" target="_blank">📅 17:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665653">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcb692fdf5.mp4?token=oRvynlIEHctk5iuZWy-hPDYDmZrNRl40Kp_zsGR6CFi8GAvCCJaQlLKMvu7uNG63n_LCgvCrQkPPhDjJ4ADOT1iGYIUaHutT5hAv0tieb_6ZyzmcF34D9-5ek6ni2qK_Zr0nIQchPNs2yYTsWNRXUDRcq3gfZRauCNSBdDzPWmGDHSeD7czYWLyhc3EKNhrGKrmDCh9l6jfubc__w-jJ9ZcQjgzJ4SwCI4llGq-yLRDZf5RlbUI9OETa69C1k9byLWG3-lispMYEhOtMyNEQoyrW4ElUVdfzulnvpzcMYybcaWBf9AOzykh_LaRr8vi5SkPe7rUaUO5d2kVCiQq73A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcb692fdf5.mp4?token=oRvynlIEHctk5iuZWy-hPDYDmZrNRl40Kp_zsGR6CFi8GAvCCJaQlLKMvu7uNG63n_LCgvCrQkPPhDjJ4ADOT1iGYIUaHutT5hAv0tieb_6ZyzmcF34D9-5ek6ni2qK_Zr0nIQchPNs2yYTsWNRXUDRcq3gfZRauCNSBdDzPWmGDHSeD7czYWLyhc3EKNhrGKrmDCh9l6jfubc__w-jJ9ZcQjgzJ4SwCI4llGq-yLRDZf5RlbUI9OETa69C1k9byLWG3-lispMYEhOtMyNEQoyrW4ElUVdfzulnvpzcMYybcaWBf9AOzykh_LaRr8vi5SkPe7rUaUO5d2kVCiQq73A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راز سیب‌زمینی کریسپی رستورانی
🍟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/665653" target="_blank">📅 17:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665651">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c24c6a03e.mp4?token=T3OAWrt77hdewG5giRkPvooeB848IIl7hPONa78dfJbsGk-cSQJQ3zYJxcq5RgaqihXq8huKSmtL38i4buxgV2yX7huMPp2aXF7imOzd2f_-BdW7JEouMhzLWUUZQQN47nWLckkid2M7gBEKht20oGLx_frcwHUsLnXHkNPcLRXOKOshGbMrCYrUik1_4x7GKwbRZr2marUOtzB6Rf2myaelN55PDcqCJ2cGqEZQjrmN-mDaitOH3v25uGJ8mmKgRw5Gwyqh2CFYkzwFzvttGlVugcXBvqpuz2zsuQtC6Nv_pyssXY7dE84TVjSPREEw_655JtoOZCqNevn0adF-rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c24c6a03e.mp4?token=T3OAWrt77hdewG5giRkPvooeB848IIl7hPONa78dfJbsGk-cSQJQ3zYJxcq5RgaqihXq8huKSmtL38i4buxgV2yX7huMPp2aXF7imOzd2f_-BdW7JEouMhzLWUUZQQN47nWLckkid2M7gBEKht20oGLx_frcwHUsLnXHkNPcLRXOKOshGbMrCYrUik1_4x7GKwbRZr2marUOtzB6Rf2myaelN55PDcqCJ2cGqEZQjrmN-mDaitOH3v25uGJ8mmKgRw5Gwyqh2CFYkzwFzvttGlVugcXBvqpuz2zsuQtC6Nv_pyssXY7dE84TVjSPREEw_655JtoOZCqNevn0adF-rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در تجمعات شبانه: ما با آمریکا پدرکشتگی نداریم، امام کشتگی داریم؛ شما اگه پدرت رو کشته باشن خیلی راحت کنار میای دیه میگیری ولی ما امام‌مون رو کشتن کنار نمیایم
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/665651" target="_blank">📅 17:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665649">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64a828e1d4.mp4?token=IizGwvO1TaisQATMqKEXSBw4e5ojCEXDFRwLsZr0V-uQPNtMJm5HsNHUGmiHPJ2CAftU3MX1Nqh1SJP5TJwWM_4kJM-vyn72UwjRXFYnJ3RGbzhAddBsapDtBP2Cw3RHCBX9b4zjtL-rhkBaB1_oWn0Es1BEXWd5J-7wH9kwfljiNh7rJWdHmX4hZadOo5de9jdo9PMqMlLji6KO-MkhRYAJgWFhu-FCUUqYZcAYj5WHZ3Yk4WAJwU4Gp5nw34Xb8xLVs4-KbHQ1IuyzI7hy97aPuE8xRnbKKO4MHeG-qvdyQQ5BNUTfZX2btWQV77FmBWk5YGROYR1fxdlw2l1diBPjQLj31NJVMN9sWBZlp1UgB65PLvJleY6wZoj7ecB7rzSbyFFGRpgJefFnHsuEY971nrvfOEEgh_4c98oTRnz4mim_FfuvA3PuSrYljyUvCqNv5Kc7azgwGsnin2ZZ4ld_BiiiMDqc9h-JQAXBAqyaCrG8O-m0M_2_42aG_cQUdk0Fqo4GdFmNq5iOvsQPakXogGIjUcwk0GwGGqhUlQoxgvxbDKShJ4YPEBSptLDfpovJ-mQyysSeJVBu_9OaDv88k4TX5FUeUXKHRp-RSo8qOzgMAEvZzeDnhRHdD7W1wfCb_Q8STHb-gk9Ot7WeoJytE8xkTcWWx_Qc0THj1tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64a828e1d4.mp4?token=IizGwvO1TaisQATMqKEXSBw4e5ojCEXDFRwLsZr0V-uQPNtMJm5HsNHUGmiHPJ2CAftU3MX1Nqh1SJP5TJwWM_4kJM-vyn72UwjRXFYnJ3RGbzhAddBsapDtBP2Cw3RHCBX9b4zjtL-rhkBaB1_oWn0Es1BEXWd5J-7wH9kwfljiNh7rJWdHmX4hZadOo5de9jdo9PMqMlLji6KO-MkhRYAJgWFhu-FCUUqYZcAYj5WHZ3Yk4WAJwU4Gp5nw34Xb8xLVs4-KbHQ1IuyzI7hy97aPuE8xRnbKKO4MHeG-qvdyQQ5BNUTfZX2btWQV77FmBWk5YGROYR1fxdlw2l1diBPjQLj31NJVMN9sWBZlp1UgB65PLvJleY6wZoj7ecB7rzSbyFFGRpgJefFnHsuEY971nrvfOEEgh_4c98oTRnz4mim_FfuvA3PuSrYljyUvCqNv5Kc7azgwGsnin2ZZ4ld_BiiiMDqc9h-JQAXBAqyaCrG8O-m0M_2_42aG_cQUdk0Fqo4GdFmNq5iOvsQPakXogGIjUcwk0GwGGqhUlQoxgvxbDKShJ4YPEBSptLDfpovJ-mQyysSeJVBu_9OaDv88k4TX5FUeUXKHRp-RSo8qOzgMAEvZzeDnhRHdD7W1wfCb_Q8STHb-gk9Ot7WeoJytE8xkTcWWx_Qc0THj1tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میدان با تو؛ رسانه با ما
🔹
راوی بزرگترین بدرقه جهان باشید. توصیه‌هایی راجع به قالب و سوژه به حاضران وداع و تشییع
🔹
از هیچ قاب و صحنه‌ای، راحت نگذرید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/665649" target="_blank">📅 17:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665648">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f105af3509.mp4?token=lYbifZMt4Gpk1NyUOOBWUOJIq9iq9TkvWrxigIbjOc3MssfK8b1feSiXja8dNZ-b3Bew9imS2QOMseJmcl4bkq3NElG8PHt4zAlnucw2GeAD48Ozj4eMcJPMkL-nOjrCf54LhSMYWDJkiVFq6mN8fYp6nPofMYkWk1YQqJuDvIc2Y1TypK2RofEWnl-PGqsC9pG1d7nH1U-PPGcIinK_Gbfb_ryp-IJ-73LdoXivrYnPyNJ0CsH9O8cs766sRRAzXJBD_wfwro0GlPCMZ7-3BMclojykrEBT4eQ0kE-UqDxHoRECm6hnApJe7D3Ok04CdrGNh9dDwCINGgoiY8ECsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f105af3509.mp4?token=lYbifZMt4Gpk1NyUOOBWUOJIq9iq9TkvWrxigIbjOc3MssfK8b1feSiXja8dNZ-b3Bew9imS2QOMseJmcl4bkq3NElG8PHt4zAlnucw2GeAD48Ozj4eMcJPMkL-nOjrCf54LhSMYWDJkiVFq6mN8fYp6nPofMYkWk1YQqJuDvIc2Y1TypK2RofEWnl-PGqsC9pG1d7nH1U-PPGcIinK_Gbfb_ryp-IJ-73LdoXivrYnPyNJ0CsH9O8cs766sRRAzXJBD_wfwro0GlPCMZ7-3BMclojykrEBT4eQ0kE-UqDxHoRECm6hnApJe7D3Ok04CdrGNh9dDwCINGgoiY8ECsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت پردهٔ عجیبِ تعطیلی مدرن‌ترین کتابخانهٔ قم؛ تغییر کاربری از کتاب‌خانه به لباس فروشی!
/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/665648" target="_blank">📅 17:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665647">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a32c19f6ee.mp4?token=TLKRNJSMBBRQl1t5fXbWg1Mu9l0OiTfV0MTPsbGrmAvl3YqleUSIg8vE9cKfJFU1z5s0I_nRXKdx4I9A_Rw986P-3uCsHYB5SdGImTVL1mMahkTEkWlxwKBl0g6Y48P4d5LLx3IOX8q8aD2Ynwi3Q5rcQ5QlcSGeNa8VKQtmQdagh7x_xyVCoQ7ern8MVYKZlQVyijv9e-2VlQx995Ayfuo-AM3P8WIgshxgBOz_vAYsWL5wuj0kiXm9W0p3OPKnksF1j-y4TsBonBeU9Qtp_AnIqz1ApwqQ8N9GafXvRq9NiopJSQ_fd2Bgq5fIMkX3twKn112tDQ3Ago1M45jjhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a32c19f6ee.mp4?token=TLKRNJSMBBRQl1t5fXbWg1Mu9l0OiTfV0MTPsbGrmAvl3YqleUSIg8vE9cKfJFU1z5s0I_nRXKdx4I9A_Rw986P-3uCsHYB5SdGImTVL1mMahkTEkWlxwKBl0g6Y48P4d5LLx3IOX8q8aD2Ynwi3Q5rcQ5QlcSGeNa8VKQtmQdagh7x_xyVCoQ7ern8MVYKZlQVyijv9e-2VlQx995Ayfuo-AM3P8WIgshxgBOz_vAYsWL5wuj0kiXm9W0p3OPKnksF1j-y4TsBonBeU9Qtp_AnIqz1ApwqQ8N9GafXvRq9NiopJSQ_fd2Bgq5fIMkX3twKn112tDQ3Ago1M45jjhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصادف مرگبار در تایلند
🔹
رانندگی یک پسربچه ۱۱ ساله با خودروی وانت والدینش در استان «موک‌داهان» تایلند، به فاجعه‌ای انسانی منجر شد و جان ۹ راهب بودایی را گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/665647" target="_blank">📅 17:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665646">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
امتحانات نهایی روز شنبه ۲۰ تیرماه در سراسر کشور لغو شد
سلطانی، مدیرکل آموزش و پرورش خراسان رضوی:
🔹
با توجه به تداخل آزمون نهایی با تشییع و تدفین رهبر شهید در مشهد و اینکه اولین آزمون نهایی مربوط به پایه یازدهم است، طبق آخرین ابلاغیه آموزش و پرورش، روز شنبه ۲۰ تیرماه آزمون نهایی در سراسر کشور برگزار نخواهد شد./ اخبارمشهد
#اخبار_مشهد
در فضای مجازی
👇
🇮🇷
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/665646" target="_blank">📅 17:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665643">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwNs1gMCu59vmQjutxZ-ppJ8BZB6bMvcfjlsycVGK8AffhLmSFmrq1ThFkmUJ_Ly4r323yhXWtDFybOTvnSyrZQrIbkQxfubmM_2KW_WZNVtZb-QuioO1VrjjiNxK3WWEdYhNEt1Jkey-ms7x35LGzb5rwKT2irRcyzOzAOCO8JRINwB-ArcXubGh7XceMTispy1XhyyOZEc4_mW0RqOOJSTMH5GKWQVQDWWrmEX-Grzs5kohv6KFKG5YWHdmx052qrGe2jfb43R57PJv94xRRvFtH2PD1u1jMmDyduWqG-UcpVpfpkoJKgjpBnh3bt1mMjVeMmoIoEjdPOM5bNxxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بانک‌ها تاب‌آوری قابل‌قبولی در حملات سایبری داشتند
محمدصالح جوکار، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
در شرایط فعلی، دشمن تلاش می‌کند با ایجاد نارضایتی عمومی، وحدت و انسجام داخلی را خدشه‌دار کند و در این زمینه دست به بزرگ‌نمایی مشکلات می‌زند و یکی از این موارد مانور تبلیغاتی بر حملات سایبری به بانک‌هاست.
🔹
مجلس موضوع دولت الکترونیک را مورد توجه قرار داده و بر توسعه زیرساخت‌های فناوری اطلاعات و ارتباطات در کشور به‌گونه‌ای که از ایمنی و پایداری لازم برخوردار باشند، تاکید کرده است.
🔹
برخی از بانک‌ها تاب‌آوری خوبی در حملات سایبری اخیر از خود نشان دادند. ارزیابی‌ها نشان می‌دهد که برخی از این سامانه‌ها همچنان نیازمند تقویت و به‌روزرسانی هستند که به زودی مرتفع خواهد شد‌.
🔹
در کنار مسئولیت بانک‌ها برای مدیریت چالش، حاکمیت نیز باید نظارت و راهبری موثر خود را در این حوزه اعمال کند زیرا این موضوع مستقیما با زندگی روزمره مردم، اقتصاد و نظام پرداخت کشور در ارتباط است.
🔹
اقدامات موثری در زمینه ارتقای امنیت سایبری در حال انجام است و این روند باید به‌صورت مستمر ادامه یابد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/665643" target="_blank">📅 17:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665642">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
مراسم تشییع رهبر شهید در مشهد ‌قطعی شد/ مبدا شروع مراسم بلوار فرودگاه تعیین شد
سخنگوی ستاد تشییع رهبر شهید انقلاب در خراسان‌رضوی:
🔹
‌پیکر مطهر رهبر شهید انقلاب و اعضای خانواده ایشان پس از برگزاری آیین‌های وداع و تشییع در شهرهای مقدس نجف و کربلا وارد مشهد خواهد شد و مراسم اصلی تشییع، بدرقه و وداع با آقای شهید ایران روز پنجشنبه هجدهم تیرماه برگزار می‌شود.
🔹
مبدا مراسم بلوار فرودگاه خواهد بود؛ مسیر تشییع تا حرم مطهر رضوی امتداد خواهد داشت و تمامی خیابان‌های اصلی منتهی به حرم نیز جزو مسیرهای رسمی مراسم هستند.
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/665642" target="_blank">📅 16:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665639">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea1c88eb50.mp4?token=R0uQ9pvRdPXdQh9mKUoQkof7Gl2Hh2_xCS8EL7StshC1sMdJCEN0LotRrgFrJN6qHuvsVXaL4AKBC_rWFtCB_r1H0iXyVZXR3yVrV1dYyTyaMPyhLKiWNfhYLcB5NEFXNDm9EkxoavpzLxU35O5yIZRpMHkB0lK7WeWLA9NSXkIexkIhzWmSypOQDu84CLUj3wABSXoQ6fKUlyKdQhqFK81jmCzPJ_NEVoZa2cITygFHUhLgq-JRZ4NVyucJ_ydhHhc_KmsVAw-FWPJu8T0d69H_4L_rEZ-237po6-KnTummhRnLD8tAFZ5ayKX8xNJprKAL6abRe1gLlUj6bRvfmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea1c88eb50.mp4?token=R0uQ9pvRdPXdQh9mKUoQkof7Gl2Hh2_xCS8EL7StshC1sMdJCEN0LotRrgFrJN6qHuvsVXaL4AKBC_rWFtCB_r1H0iXyVZXR3yVrV1dYyTyaMPyhLKiWNfhYLcB5NEFXNDm9EkxoavpzLxU35O5yIZRpMHkB0lK7WeWLA9NSXkIexkIhzWmSypOQDu84CLUj3wABSXoQ6fKUlyKdQhqFK81jmCzPJ_NEVoZa2cITygFHUhLgq-JRZ4NVyucJ_ydhHhc_KmsVAw-FWPJu8T0d69H_4L_rEZ-237po6-KnTummhRnLD8tAFZ5ayKX8xNJprKAL6abRe1gLlUj6bRvfmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آموزش‌وپرورش: امتحانات نهایی به‌هیچ‌وجه به تعویق نمی‌افتد
رئیس مرکز ارزشیابی آموزش کشور در برنامه پرچمدار:
🔹
آزمون‌های نهایی طبق برنامه برگزار می‌شود. امکان برگزاری آزمون‌های نهایی پس از کنکور وجود ندارد.
🔹
در نیمه اول شهریور نتیجه امتحانات نهایی به سازمان سنجش اعلام می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/665639" target="_blank">📅 16:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665637">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUSsngudjH0HX4SFjHKVJvK0Z6veA_y27RDasbzRXSmCpMaIyIHLnrolCNFngNEm4gJgkl0AdYkJu5SKK-GtpKgZOdclr0SKhZjzYlnFhuGlGcLlgCkOIyeL8Y7zPCv_6maF8V9DaVpggWj-0nTVD_mBbWi9G5SWdjNCZ3IDt_aNqKqLz9I2z6N7jECX_WUFxXkAV8lybf3rpZqiGW4tEqnmJmfl6m4NfyXB8SexoMh_dxLZ4VL11WsZoNJpSz7A1x1uokacdwU-Xt7eAn00hRjeHHerjHzOHFlJBrIyV6pQLG9-6432i4QSu2j49Ee0DIoT-JhXxCYfEMLqsfHQHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بانک‌ها در خط مقدم جنگ سایبری
جعفر قادری، نایب رییس کمیسیون اقتصادی مجلس در
#گفتگو
با خبرفوری:
🔹
بانک‌ها اکنون در خط مقدم جنگ سایبری قرار دارند و این نشان می‌دهد که مراقبت ویژه‌ای باید از نظام بانکی صورت بگیرد.
🔹
اگر لازم باشد بانک‌ها باید برای بهبود وضعیت دفاعی و تاب‌آوری هر چه بهتر، مجوزهای لازم را برای استفاده از نیروهای متخصص دریافت کنند.
🔹
در ابتدای جنگ پدافندهای نظامی ما دچار مخاطرات شدند ولی با تقویت سامانه‌ها، چالش‌ها رفع شد و همان‌طور که چالش‌ها در این زمینه برطرف شد، در نظام بانکی هم با این چالش‌ها دارد به خوبی مقابله می‌شود تا به طور کامل برطرف شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/665637" target="_blank">📅 16:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665636">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
جنجال جدید در خانواده نتانیاهو؛ سارا نتانیاهو همسرش را در حضور اطرافیان تحقیر کرد
🔹
انتشار ویدئویی از برخورد تند سارا با بنیامین نتانیاهو، در استادیوم «تدی» قدس اشغالی، حاشیه‌ساز شد و بازخورد گسترده‌ای در شبکه‌های اجتماعی صهیونیست‌ها داشته است.
🔹
همسر نتانیاهو در این ویدئو با لحنی خشمگین به او می‌گوید: به خاطر تو مجبور شدم با دیگران بحث کنم!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/665636" target="_blank">📅 16:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665633">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZvQqzqRylVYXIyHolcBGKKJrGKkEjTrZqWjvy3TK3x8w4Nf5nrnB0qb2scBA-yhtKuCpP94j3fNckse8owaWMpPA3-LLzjqR6IQwOd6dxjBKW_qjWDjiLMrtW2DdVguF4PrwZjucQfQVQA9K7e9lK1xyou1WI0voDvd4ExBX2RrLd1WnbI6U3m2GU3hz5ll668F9xXtmH730m1k-vOddTCsznKTGGJDNM3FTsFoMKUFhiQFjSHxWmSJmp8KIH16NJbK8feFBnphbVPM4KpYjNpjZib9V4w-RmTB3y8JUVnHD8SCLUDQ80JUHScvV36G_4rwb8njO1CMA73DWkj204g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T7Qg0FWSeX_YOY_TWw5wkgLAnNFL16F2hngjl0mefn3OVSZZmsTk_nO0rZKne_RnH6M5-osukqdJUSU1kRgJrWlNQIw8PjQ9EiPpML45kVYHVPmnjoO92rnfF2XSIRzd4QCAz5ra-oho1ess7Zu56bb-lS8tmPrSVsfntx8T10lrk9uB8chp5_oqqH_emD4cGCanVr_3-RDKamKAGJoXrP-LoXRs6y7ihhU1byziSvW1iGMO8UIMXj66lbOkf4sDKO6WBfiACHDIjANxWtpJwybkltDmkrr2RhkS_72JYzYH0rsHz9iqVNw1zGbK6M0V7D9z1pPXdwbqlnEWtxjseA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cy5h5juBhgH3qMnMseeP0VRb_DXCIJ21DLioOo4LzgmcXRqXR4r8EzqT4WhrrlgIRBWHqF1PLIFn0176qkX8YrWIBdalgQv3nfSfV13WtcvtKilELPATPPJVBYQEGURPTRZIQXDcmEltTlXIaPHttsgKLMLzjs7tTzeVWrt1B46yPGx_yBDPtGd4EYYLtaRMhjymK8KiSKGarbln0LCkJFHrB1_UY9QTv4kQl33cr5lLSOFtGCXO-9iqYyhzxnyDOdh-tc0MtGyKhsXQym2KzuzXpDcBTqbtP5CtGC-I6dN99zdTTs1Pk0J084o1M5zNkHtsdbDj9UcfjustvvdgoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چه چیز‌هایی از پول به کودکان‌مون در هر مرحله سنی یاد بدیم؟
#دارایی_هوشمند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/665633" target="_blank">📅 16:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665632">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g24WmQl5kUVHBaYEWO6OtMybSMx3VDfIHU-YtKJnxu-YwBAFO1JGx4Et3kZPNGrMWn7MjcVT_45QBQs3VImkgyZerojyK9iQOj8iIaqbF7hFktoWfF7rVasLsb8zx0C9ItqbOqVU9WlLT1nlJjQYAmn7nT2KiQhRN0m0mLGfJrK9pBc43KWkSC1ntsogFmD_hrWKJbtq4KFdemEfs2qAkbVsKhKubSS7Z4kjRJsZMHJe6hnCKcTRaSHYhBofEOcCa_5nq1qpbfyzth6QYaUAj1dXeRr7Q-HwizjN4fOoJlZLcQNHh_2zdjmH15bqJ4OH1u_RER4FF-_Kho2e11YI9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر جهاد کشاورزی: در صورت تامین نشدن شروطمان توسط آمریکا، خریدها از مبادی دیگر انجام می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/665632" target="_blank">📅 16:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665630">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECt97H-amaolhUBMt_vWAXKE1BTxdJDvgcttQ2g_yBCPjm2lIcvX4q4qevrM01kWFMHre8NYh6Pf49yy2v9rgiGjrVcqk9KGGQnrdB3XsWMLhx6DrWsNSuCje4qF087JvLHwlB6SF3VLJ25B2Ip8rLquiBrarz-pwnmeXRryjQSzGZySd82vhr7FSkObik4v2-6MzZ-kEZhJaaP94qbYVwgySbRS7Qz1nXPJ0-IPQuk7K4mdIZPzogMXKytgt1JgsOduZL-T3ih-bc_SI8sWiNr_e_F_YqpycrDPzr3cgDm62s_st3gheeYTAYMdWeQ-Aoab6-ez62RddwWZsw1gpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری زیبا از شباهت مزارع برنج به تابلوی آینه‌کاری در اثر انعکاس نور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/665630" target="_blank">📅 16:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665626">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrwuwLaOVrx86h_5JuCmKjfDzZJlu0Ok6ofQMir7293IrOAgkKSWJ0YUpUcUG7f-EPHxhy8LhyN8ru0y-7zc-LFyKmZu1XQmjsZ63JgOaqXmVWrUJceSZCkk0cRl9EeFPHDyu23YWNhIz8DLOEyw6fJXgt-vCLT7VlelGv0wc8zQWUjtH8BCEihQf_V7b6kBEdClshDPCOBZoPDuAaMannDWgCqkwU8OmSXn15CjdVF0dvbl3g_LXtEG9CUfrhZ7oV3ZLXJLxO2u6E7zDV16jBtGFFx9s9SjBQypamvqPzjol40cJr0rzTvzKTHVmneErYGZYOUV5buvdxCRjk-MOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پل معروف به «بین دو بهشت»؛ پل ارتباطی دو استان کرمانشاه و کردستان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/665626" target="_blank">📅 16:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665625">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ade299394.mp4?token=e_vB3V6WCr6pIwEV2q5-OPX2S4afZ_sme5Wc4YiwxkPa2xOQqTperoTjAC5OZa4TZeMcuImvOxJSXEp8wFjwmRGZ9BhoxnU1Hk_3IEW9_p3eFjk1eSOv-vGH875LMMqL37SgGQ2yr4O7EptoAIywQycXW-NMwglFF3ZF4VvIlCy_445H4D7_oic5eI9wd7Hg7A7AbQO8RaApOpKF-lytlozuHNGQtxrg1CAWyHpt6jnayzuBnldpVmpHJqu71owrn2CjyZ_-42Up3F5Hiph4rlqKDu9J4L7Ex8WZf9kb97TNlVZTh4eKfjIsOlSx1CZu3E7dEjEc9jTI3tg8-4wWvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ade299394.mp4?token=e_vB3V6WCr6pIwEV2q5-OPX2S4afZ_sme5Wc4YiwxkPa2xOQqTperoTjAC5OZa4TZeMcuImvOxJSXEp8wFjwmRGZ9BhoxnU1Hk_3IEW9_p3eFjk1eSOv-vGH875LMMqL37SgGQ2yr4O7EptoAIywQycXW-NMwglFF3ZF4VvIlCy_445H4D7_oic5eI9wd7Hg7A7AbQO8RaApOpKF-lytlozuHNGQtxrg1CAWyHpt6jnayzuBnldpVmpHJqu71owrn2CjyZ_-42Up3F5Hiph4rlqKDu9J4L7Ex8WZf9kb97TNlVZTh4eKfjIsOlSx1CZu3E7dEjEc9jTI3tg8-4wWvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیس لاته انبه، نوشیدنی جذاب این فصل
🍹
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/665625" target="_blank">📅 16:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665624">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
دقایقی پیش ٢ عضو گروهک تروریستی جیش‌العدل در زاهدان دستگیر شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/665624" target="_blank">📅 16:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665623">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9uFb0R4WUbkty1ynTxTnJ7P-ztjm6W_kE9nG59FDPuwdyAzzqGXsI0RJEg3kz8I9vG2-QrdJjkbEaTHpOvb5crt6xAyEiNjQ6OxfrcKe-d-ru1Om_sgxORHNiaQ2LZWy5FG7Gw67GAbIyNIaWIHBUfLw-rk5rB-Jy0JM4PKOzHZPtZyAdtvhmgWFKXBrBnxshCx7mmPaguUYVVticRKCtEYABEGW7wMw9tp6XbI5HUPnAfATAo0XcyTbLD97l1qmI5bI67M2fkzTeDH15REoUCgBBdxJvOwGN62kOi8If1gsMVOh1tZ3mSP1Nf7NcAtqZ8PjQKwrel8XVLaVghohQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه راهنمای زائرشهر چهل‌سرا در جنوب مصلا
برای مراسم وداع با رهبر شهید انقلاب
🔹
استقرار مواکب پذیرایی، بیمارستان و آزمایشگاه سیار برکت در زائرشهر چهل‌سرا در ضلع جنوبی مصلا و خیابان بهشتی
🔹
تماس با سامانه تلفنی ۴۰۳۰ برای راهنمای مسیر، مراکز اسکان، درمان، ستاد گمشدگان و مشاوره روانشناسی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/665623" target="_blank">📅 15:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665622">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjGZqDUvS448HJjZzpjC51v0gbG4JquIPM7id3-590JpMSE54E9cq-q8tf0b5gy8r5gLIha3t46ceEvru9d8TQCW7suGhX3GRLjlWb_8PIXVXm9nDhj4Lv8RKV7e1RliV48vfbKutn6o-N2aAhf2E1miiabV65_OQ7RGz-V55NVXAViatRcKmFb3QDmZ_r1G8iPmIMueU7JQTRAv0a690iQ94yMWUAZlCHa39jRttJFJpFX4NIMGOg8yHZe45RyT5H8FVT0cSdlZnS4AOlZcg0BzqLhV2nsAxLtGvZJrN8V9ys8peaIr_Lp8dAhAdRd1KCH9bKi2yQ6M4mtHW6FKYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
رشدی ۱۵۳ درصدی سود خالص واسطه‌گری بانک اقتصادنوین
🔹
بانک اقتصاد نوین از ابتدای سال جاری تا پایان خرداد ماه موفق به کسب درآمدی معادل ۲۷۲.۱۵۷ میلیارد ریال از محل عملیات واسطه‌گری پولی شد.
🔻
اطلاعات بیشتر:
🔗
https://www.enbank.ir/s/mfa8De
☎️
02162740
🌐
www.enbank.ir</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/665622" target="_blank">📅 15:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665621">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f07b35cfb.mp4?token=WpZNk4aXjPXsRReS5mvgpuM-RUls0K6mgVFgG8h80b3TmXSoDjWMxUGdVIAdQGRKJS4CI5D-P4qiCJBSnzZul8f6n_N_XI8iySCXCXLifVJAm_KeQrY44PyydEcPys1FEdRVD8sGHqT68uBFBokQR_C4JCNd2oRzP8BS9TBNePmzhhe1ReIaXPNZaAaZ4d6zN2ubg6-ve8hHAc0__VbDV1d1CP49EHl_gLlhwsZ1Rdhom0Akvq3MTBFuEaxT9U5clt9xpTMBH-Fx4KtB1tDNg64FF2go91y9fEhb6aXJ_3WXF7AW9RJJb_bGZHJtn6_h5zoseiNHXlZwgxIjfqXWAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f07b35cfb.mp4?token=WpZNk4aXjPXsRReS5mvgpuM-RUls0K6mgVFgG8h80b3TmXSoDjWMxUGdVIAdQGRKJS4CI5D-P4qiCJBSnzZul8f6n_N_XI8iySCXCXLifVJAm_KeQrY44PyydEcPys1FEdRVD8sGHqT68uBFBokQR_C4JCNd2oRzP8BS9TBNePmzhhe1ReIaXPNZaAaZ4d6zN2ubg6-ve8hHAc0__VbDV1d1CP49EHl_gLlhwsZ1Rdhom0Akvq3MTBFuEaxT9U5clt9xpTMBH-Fx4KtB1tDNg64FF2go91y9fEhb6aXJ_3WXF7AW9RJJb_bGZHJtn6_h5zoseiNHXlZwgxIjfqXWAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نسل جدید سینماها؛ تجربه‌ای خیره‌کننده که مرزهای تماشا را جابه‌جا می‌کند
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/665621" target="_blank">📅 15:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665620">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9410720e62.mp4?token=LmMxfJbfwX3U-hNN7pSTkNosOGrKSzo6x10DGj5jpbfoTGA7B4zuLc-PXG-Hza1LGWyECiLtQzYVimQtiokg7YGO3wfvWgOV4BUST66ju19Qr4ky_xfJSIB1RHK2fRSNJRq0PH31MfrBm6JycIs77XWC1JFZ4cEuAEkZ-n9jR44FZ0yvWtU8i9M29dyiWfDdxVPwcUIYn-tZP_suGN8BGYUhKTNFXTKwMHcsMp2e_x26Vxz-QS8eGdBXMvWzIqs3EqPGIeFfXK2nayGD_Z_5Nh93X8NqboWswTZc0nXdH48dEf-Qxy31Id8mjXm7VlVjh47veNHFT5Cy6INvIFmT1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9410720e62.mp4?token=LmMxfJbfwX3U-hNN7pSTkNosOGrKSzo6x10DGj5jpbfoTGA7B4zuLc-PXG-Hza1LGWyECiLtQzYVimQtiokg7YGO3wfvWgOV4BUST66ju19Qr4ky_xfJSIB1RHK2fRSNJRq0PH31MfrBm6JycIs77XWC1JFZ4cEuAEkZ-n9jR44FZ0yvWtU8i9M29dyiWfDdxVPwcUIYn-tZP_suGN8BGYUhKTNFXTKwMHcsMp2e_x26Vxz-QS8eGdBXMvWzIqs3EqPGIeFfXK2nayGD_Z_5Nh93X8NqboWswTZc0nXdH48dEf-Qxy31Id8mjXm7VlVjh47veNHFT5Cy6INvIFmT1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار در یک کافه در دمشق
🔹
رسانه‌ها از وقوع انفجار در یک کافه در دمشق پایتخت سوریه خبر دادند. بنابر اعلام رسانه‌های عربی بر اثر این انفجار ۴ نفر کشته و ۱۰ نفر زخمی شدند
🔹
شبکه الاخباریه سوریه: انفجار در کافه‌ نزدیک کاخ دادگستری در دمشق، ناشی از یک وسیله انفجاری بوده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/665620" target="_blank">📅 15:49 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665619">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
صدور کارت سوخت‌المثنی ظرف ۲۴ ساعت
مدیرعامل شرکت ملی پخش فرآورده‌های نفتی ایران:
🔹
شرایط دریافت کارت سوخت المثنی به صورت یک روزه وجود دارد. اگر هموطنی کارت ندارد و درخواست دهد تا ۲۴ ساعت بعد کارت را میتواند دریافت کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/665619" target="_blank">📅 15:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665618">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37b5acf4c9.mp4?token=pffwyJ1BhuJ_f-eUJNouqvh5YX4LDyZy_V5vg115DKxTWk6vC_Wvo5x-ZeM7tOjDx6Pqqb1HW4aYvfKropK_OZ5uNjMV08ky2qc17y594gh88369L7wWEqIDSZxZi1nASA_ZqvTs0Fx7qVQea5XSM-eJib8G38netIvdWNO8g8IchNxYAWGX7Y2hezODM9K48xtNN3crD-ub0YL4Blgd2SsmUp-6AVztbnpEUZV37MESWPySz3roQtNgpeR_loaoNXw2b39jINe0dbXdxwYoHW80bTSNC7F6-M7ZEcmOF2xA3wZS5aktmNJTBsiFJtECCvw2WCTX_obpFVNI7eJxwjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37b5acf4c9.mp4?token=pffwyJ1BhuJ_f-eUJNouqvh5YX4LDyZy_V5vg115DKxTWk6vC_Wvo5x-ZeM7tOjDx6Pqqb1HW4aYvfKropK_OZ5uNjMV08ky2qc17y594gh88369L7wWEqIDSZxZi1nASA_ZqvTs0Fx7qVQea5XSM-eJib8G38netIvdWNO8g8IchNxYAWGX7Y2hezODM9K48xtNN3crD-ub0YL4Blgd2SsmUp-6AVztbnpEUZV37MESWPySz3roQtNgpeR_loaoNXw2b39jINe0dbXdxwYoHW80bTSNC7F6-M7ZEcmOF2xA3wZS5aktmNJTBsiFJtECCvw2WCTX_obpFVNI7eJxwjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پست جدید ترامپ؛ دکتر ترامپ
🔹
ترامپ در شیرین‌کاری جدید خود با هوش مصنوعی، این بار در نقش پزشکی ظاهر شد که منتقدان سرشناسش را درمان می‌کند.
🔹
ویدئو با تصویری از ترامپ آغاز می‌شود که با لباس پزشک از مخاطبان می‌پرسد «آیا شما یا یکی از اطرافیانتان به سندرم ترامپ‌هراسی مبتلا شده‌اید؟» سپس می‌گوید «علائم این بیماری می‌تواند بی‌وقفه ادامه داشته باشد. خوشبختانه، من دکتر ترامپ هستم و برای آن یک برنامه درمانی دارم».
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/665618" target="_blank">📅 15:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665617">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45eb86f977.mp4?token=EDOVDLz1IoQpxD8kBImk6UtF9qxEKiAVFacuaKZoRymko-z3UtPCXr3P9NbNUiQ34OCHDTfC4SoeKoivEqpn0AI5mQBn0GVj4m8a7bB4QgIyjXhAkcgMr1X6C912i6lphNJX8VIfggC2PeB_-jxoRLp5Bgnuqe4bD_fSfFLYBh2hSHsKUe3ozL51NQsl73gPZL6WiFM-PlqRowacsxyLcl4oDQjb0SGnqBctoByZtdvRDJHVd3SJ3cUmova1DHHswZr3i9W6yl8gi4XKCK8EnWkvqN-BN0lLI43VxwRC8tvSBnYbxwIvoRk7IT2IOM8YaF1xS6zkjnbr13POmkwpk3eXsMT-pJqBv-kFPGgkLRsHL4OWxdzvhnY0xykldXWzM3uLhILBpvN3dA1LhtirJqzjtqTRUBdwMs1j3SBcf5s0EoiCQhEZZV0oX0C_NKVGL5xAgkAYXPx8JjXmrdSLPkdpzicj4EuXer0jubJTzzDRGr3mZxzvvkjUvUMKKePC_2hG1Nl2bRc1I5ZwecHW1mytd8cQC2xaVHXk_1ZF7r26_y6nmwaOmKKFJ0fB8SR_MAJxt5_dDdhqWFJgVDLyTTUkIllCW0q3da8CUFDCQkiPxzGk3_AN3v1krwRBpGYGgcolMCWeWiWXyQu3bgQW2kKWRSitNp4DPfVz0-GDtEY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45eb86f977.mp4?token=EDOVDLz1IoQpxD8kBImk6UtF9qxEKiAVFacuaKZoRymko-z3UtPCXr3P9NbNUiQ34OCHDTfC4SoeKoivEqpn0AI5mQBn0GVj4m8a7bB4QgIyjXhAkcgMr1X6C912i6lphNJX8VIfggC2PeB_-jxoRLp5Bgnuqe4bD_fSfFLYBh2hSHsKUe3ozL51NQsl73gPZL6WiFM-PlqRowacsxyLcl4oDQjb0SGnqBctoByZtdvRDJHVd3SJ3cUmova1DHHswZr3i9W6yl8gi4XKCK8EnWkvqN-BN0lLI43VxwRC8tvSBnYbxwIvoRk7IT2IOM8YaF1xS6zkjnbr13POmkwpk3eXsMT-pJqBv-kFPGgkLRsHL4OWxdzvhnY0xykldXWzM3uLhILBpvN3dA1LhtirJqzjtqTRUBdwMs1j3SBcf5s0EoiCQhEZZV0oX0C_NKVGL5xAgkAYXPx8JjXmrdSLPkdpzicj4EuXer0jubJTzzDRGr3mZxzvvkjUvUMKKePC_2hG1Nl2bRc1I5ZwecHW1mytd8cQC2xaVHXk_1ZF7r26_y6nmwaOmKKFJ0fB8SR_MAJxt5_dDdhqWFJgVDLyTTUkIllCW0q3da8CUFDCQkiPxzGk3_AN3v1krwRBpGYGgcolMCWeWiWXyQu3bgQW2kKWRSitNp4DPfVz0-GDtEY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به ما اطلاع دادند که شهید کمال خرازی ترور بیولوژیک شده بود  صادق خرازی برادرزاده شهید کمال خرازی:
🔹
دکتر خرازی دو بار شهید شد!
🔹
من منکر تلاش‌های برادرمان آقای ظفرقندی نیستم، چند بار بالای سر شهید خرازی حاضر شد، آقای پزشکیان دستور مستقیم می‌داد.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/665617" target="_blank">📅 15:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665615">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
اطلاعیه شماره ۲ قرارگاه برگزاری آیین وداع و تشییع قائد عظیم‌الشأن شهید امت (تهران)
🔹
هموطنان عزیز تا حد امکان برنامه سفر خود به تهران را به گونه‌ای مدیریت کنند که از حداکثر ظرفیت اسکان و ارائه خدمات به زائرین در تهران استفاده شود به عنوان مثال سفر را کوتاه کنند تا تعداد بیشتری از مشتاقان شرکت در مراسم بتوانند حضور پیدا کنند
🔹
مبادی و جاده‌های ورودی به پایتخت همواره باز است و هیچگونه منعی برای ورود وجود ندارد
🔹
زائران گرامی اخبار و اطلاعیه‌ها را از مراجع رسمی پیگیری کنند و به ویژه مراقب شایعات و اخبار جعلی باشند.
🔹
پیش‌بینی و توجه به محدودیت‌های ترافیکی در سطح شهر تهران و حفظ آرامش در هنگام حرکت همواره توصیه می‌شود تا برنامه‌ریزی حضور هم وطنان دچار اختلال نگردد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/665615" target="_blank">📅 15:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665614">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3ClRF-hEi_gt82dWu7KZ8ESRszrR7eNInkmfTwkLe1gFJa6J5TwBjYgUfUNGvk3idkwJKPpvOv0bOZutpvC8bAiY2JecfY6mhAkM3LTOwCTx_Y6LLwWfvPVfEJb9QYYhA091eToDkAXFeSBvZprM-GfVe1GteKO7F5eNkWXavZP4WjCtJFG4KO4Wfl57ZCaSSTWBg83F93Uy0MG2tk-VmyWloC1OFhYj5kCOLoELGrB1j0KCVhvI6gDN6lf0gq4w5_OhhSOEF1dxgtZNM34rsJgG-48gxRTeeqgaZzh0pby9139OMfhebsvp-t80X3zpqsxMiB88EsejO5WKtziHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عبور نفتکش‌ها از کریدور عمانی- آمریکایی با سامانه شناسایی روشن
موسسه تحقیقاتی HFI:
🔹
اسکورت آشکار کشتی‌ها تحت حفاظت آمریکا در حال انجام است. در این مدت، ۴ نفتکش غول‌پیکر (VLCC) با سامانه شناسایی خودکار روشن وارد تنگه شدند.
🔹
در سمت ایران، ورود نفتکش‌ها به مقصد بنادر ایران همچنان محدود است. تاکنون هیچ‌گونه تشدید تنشی از سوی سپاه پاسداران انقلاب اسلامی رخ نداده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/665614" target="_blank">📅 15:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665611">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9d3ad0855.mp4?token=Da0UkATK1mkhZ-SxsYmZ7igrrEJTJmKWo4z7auuzP2Qn5UFzfLmw_MicO-hy4-9hZj_CM1iRRXoQBHLDrTh_M1ykJ8Huz62V3TeDWwwTuW80RDNzTWoX-0DH9cu2dhVrXZzLPeprk0WX3y9N2xl9syaVpPWn-Qs7A37DsdanVY1b6R4iPURYq0sP03WjPhDljymk_0fCeYU2RukdbdE_Dc-Ai3R7H3yjaqG5smd9huoXBqI7VEsMURg5IiCmfj9Yn5_uuJ2JgCXNvN5EoxgKmtVaI0tFDSdJAZYyQlu3rN8GEcXdzEuR_LjO9qFrt6m90qmU3A_TRqc4FYMS4TonV3QYfQbz9c3oFBglIVhcT1yJsdJWzV1wYJbbzA_CuWwaIUMOqpm5DKDZ5KZSW7I5nQ4FuUekGkIWJVWXUfIz2CAtUi5fgfn5aT0D2Az5aK2RfPA-c3emN33mqg_Z377rtr-SchZfcq4CDZ91dd7eq8jnaA0DNxdLUnAuH-dp21dWx39YxvDeYY1WiK7M1AU8Iof9DaFfG4l663D0_gV3GGIhhNSEmHjI6hX5rNZT-RW57cD2vOSz-6fE7o_bPPHnRUO-_57GSdVgT149tt2uA3JUg5cSM0kvVm1i_uUNzGNhGV-Gz7dmfjDDe23Ai5be6s5Dv9FqTPmQxFI4K-csoRU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9d3ad0855.mp4?token=Da0UkATK1mkhZ-SxsYmZ7igrrEJTJmKWo4z7auuzP2Qn5UFzfLmw_MicO-hy4-9hZj_CM1iRRXoQBHLDrTh_M1ykJ8Huz62V3TeDWwwTuW80RDNzTWoX-0DH9cu2dhVrXZzLPeprk0WX3y9N2xl9syaVpPWn-Qs7A37DsdanVY1b6R4iPURYq0sP03WjPhDljymk_0fCeYU2RukdbdE_Dc-Ai3R7H3yjaqG5smd9huoXBqI7VEsMURg5IiCmfj9Yn5_uuJ2JgCXNvN5EoxgKmtVaI0tFDSdJAZYyQlu3rN8GEcXdzEuR_LjO9qFrt6m90qmU3A_TRqc4FYMS4TonV3QYfQbz9c3oFBglIVhcT1yJsdJWzV1wYJbbzA_CuWwaIUMOqpm5DKDZ5KZSW7I5nQ4FuUekGkIWJVWXUfIz2CAtUi5fgfn5aT0D2Az5aK2RfPA-c3emN33mqg_Z377rtr-SchZfcq4CDZ91dd7eq8jnaA0DNxdLUnAuH-dp21dWx39YxvDeYY1WiK7M1AU8Iof9DaFfG4l663D0_gV3GGIhhNSEmHjI6hX5rNZT-RW57cD2vOSz-6fE7o_bPPHnRUO-_57GSdVgT149tt2uA3JUg5cSM0kvVm1i_uUNzGNhGV-Gz7dmfjDDe23Ai5be6s5Dv9FqTPmQxFI4K-csoRU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هجوم فرانسوی‌ها بر تهیه پنکه و دستگاه‌های تهویه
🔹
مردم فرانسه به دلیل گرمای شدید برای خرید پنکه و دستگاه‌های تهویه مطبوع به فروشگاه‌ها هجوم بردند. فروشگاه لیدل پاریس به میدان نبردی بر سر پنکه و دستگاه‌های تهویه مطبوع تبدیل شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/665611" target="_blank">📅 15:16 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
