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
<img src="https://cdn4.telesco.pe/file/FdIAWlFSCBICML9vV8hJlvgG7q5eTRbInBmhSXZ8CeCHBe-1Yn2uZo17fMFFT2FdIp3plK5Q2ZLL4lDSFc-7z-QuJTQEWREIve3hyqHfZUiOoJ5PvjhhKWUlGR0D9T9ro1BHsumxmM7sq6g5T5SR2OGen2q5mL-FYB93ckaz0aLDaKJ3OHfUbYFkzvYjIbGGY5zDHTF7whLr4fufr6Za5VH_jtoiwA7RIc98dCnJ0eJB219PKcHRqRjcd2AFiELjKe2TXX_957Da2e4CyV8W796AOe81JTjAl2hnng9W9C25k9qNrctRn_PrTnz9Vs2qYbiRc_N0M0kWdv9JLfbbGQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 17:07:54</div>
<hr>

<div class="tg-post" id="msg-465703">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vyu_YhRZye4SXSYYRQam5SC-xsJuoESzNGr2FLxj31XZyPtvbZ_70kSnsTj8XI1sMj63yfGH7k4vbFjvNC89mvMGeFUUyj3KtwJl7kosddKEByqonIf5LW1NvCRc7aA1qAH7oYWhj5vQMC7bA5fEaziq0ON5rVDxuhVkJKirKLcOlFv5w8ugWohi1YIsKVRyrkNdwo7H4OzsMTGwz8QZ9emGZ-HrxuBoOa90h-dwlC05o3lVgImpAf0uI6LGXHMUV1yhW_XyT10bgfmFoeZM0pB2TYtNUig7ksIpuMqxh0wMgTTkUd6vIMfcXiXb81alo_fQrsbB9b0v-TNRFtMn9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایی که یک اختلال در آن می‌تواند گوگل را بلرزاند
🔹
تنگهٔ هرمز فقط مسیر عبور نفتکش‌ها نیست و بخش مهمی از کابل‌های ارتباطی و انتقال دادهٔ منطقه نیز از این محدوده عبور می‌کند؛ مسیری که هرگونه اختلال در آن می‌تواند ظرفیت شبکه و کیفیت اینترنت را کاهش دهد.
🔹
براساس مستندات گوگل، این شرکت در شهرهای مسقط، فجیره، دبی، دوحه و دمام ۵ نقطهٔ کلیدی دارد که بخشی از زیرساخت ارتباطی و انتقال دادهٔ گوگل در منطقه را تشکیل می‌دهند.
🔹
آسیب به کابل‌های ارتباطی هرمز می‌تواند با افزایش تأخیر اینترنت، کاهش ظرفیت شبکه و اختلال در خدمات ابری و اقتصاد دیجیتال، هزینه‌های قابل‌توجهی ایجاد کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 675 · <a href="https://t.me/farsna/465703" target="_blank">📅 17:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465700">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BxeleqNYIGK8SbebSq6-9QyZLwQpgkvpWYmAV1ksamObeG9VbkzkUvTQN16Cu4qNt7RCqRItyDNHaLilcaDVA3HWnnqjHXqP3WKxyHu5zKkxI1-j7IwgrYsvphNA12A7hatQ66y679lmKqK0tA3bP0tVEvZzybXSAgEgMormdmf8mIaj_3ADJRk2cjPEUT9-HcA1CmHY4jSYvPgJGYtvDzd2ez-duAS6n0edEVFvpZorF92RNQKXDB18ip__K0U-TnYIFyT8eEN3yIYSabiZ9izmtJP6vur9trxTvjHtgFw2JMAxeaiDlyMmn3CmWFK1IJsU4YQ3Pp9todZXL9tbEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mUteLjya9Zx6J6jeJBGDXJQec93SDyUkZoCGyC81_D9aCtcaeqetlMj769G1F262Ik7A0kH9aMrwjQMMm4iMqKPi3tH_QE0aJCbYEJsvm7ulxclcqRhvKUSzcRR8LUyk6yZjkSNdISGzmNn0nfZuVLR9PBQdQGECqlybqSkYJK4pMJXvWM5sPa3tpvmB8r7_PALSFnYPkapO6Xxdnu4mOh-Xu2nLqCw267uO8WcjBZMpB3rHffWAH-OWR5frCupX9auKBbamiN1Yxr8BacfBsAMhgnuHEEEnqq5pwlwU-Hkc6gTB1QRUNZFE0B3xUWj6D_0MBLHGsi_adjOb2i7UVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T2OrYYmYkufRma6RSVH0s2DaTSee-S10e2y4CeM0X1rrPsw5o4dpDvsVGm07FDeUjnCbvrdeIu-Xa_u5uU4FvHACJxd2QXNOvkKmhrFGfacQZqN66wWua0ya9JhLt8cQMHfA7joTo-rvpNTkeBP0j7l4OIzm71YBPKBHQbZoDx1jn7bU4PjkJGdaXRwhGODVYn8NKo7ojrPBrf7uuiLX-_jF2rNvDwLsyhBugJ3AVmWkysLbXYDhedtuVtn3Qq1RW9tIsnT8Z86boQheYNVilg202Ckjd7UPifxpOQx7ghCLfWZAlPvs5PYVsuK38iPM1RLbRHeoGoyCc30MXUd0vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یامین‌پور از اهدای انگشتر متبرک رهبر انقلاب آیت‌الله سید مجتبی خامنه‌ای به خانواده شهید حسین هاشم: دیشب را به زیارت خانواده‌های شهدا گذراندیم.‌
🔹
الماس‌های درخشان در خانه‌های کوچک در کوچه پس کوچه‌های ضاحیه...
🔹
اینجا خانه‌ی شهید حسین هاشم است‌. سه فرزندش در سکوت آمدند و دل ما را آتش زدند.
🔹
این شهید به‌خاطر اینکه در ویدئوی وصیتش مکان و کیفیت شهادتش را توضیح داده، در بین شهدای اخیر مشهور است.
🔹
با خود چفیه و انگشتر متبرک رهبر عزیز انقلاب آیت‌الله سیدمجتبی خامنه‌ای را آورده‌ایم.
🔹
هربار نام امام سید مجتبی را می‌آوریم صلوات می‌فرستند. همسر شهید یک کلمه هم حرف نزد، چفیه را روی صورتش گرفت و اشک ریخت.
@Farsna</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/farsna/465700" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465694">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tVV7XR6rs1yLsqxrMfnphVL0LTOv2j0xWT5envj3Fdpj6HxK7gM3ErkIZBAn87FvMq3n8c_y8nuFJ9Tbv_KPA0UTmPvDpTxhENbq71qyaPb_DgoXf35X4-JtWDYAcXZ2m3q3IpksZ4IjTTnHYb7OJSBttI7ZgL4Mn-4DywvvkAIik2Gzcyf2gjoNbZTHlCs64v6HKk5B7DmRrG9U5_AulDs22kHojifIgXrfAUd_duW4MFs9BQILTDftuDoFCWTyIMvzGX7mpDANMOBR5yiNH8K67E3Fv4xGrm88qpesAxu0E2XEwdF80Nlu2gMTe_DhcGBHtdBSh0ZyTKoQM9qs0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KtIMXaetCfBtyjbcy8L_CI7hRiyUBungCITRI731wc35J0ZozOhIbjf7ytlA4STytlSDyhW7ZZoGcarnQu1IUssEHCyUD-ENV6NFEzevCA1AkMJaVS5hMAh8cBB6Hjfh8pxfYoODoj-7MGpts0zbKDLVmGphP83esWdv0RSjD2GMssjzheZGzqYS6tgwLh_v9GqGiDk4PvBIbYuuvAMaI0tmk54vg64fyecMrHyQtBBgG3izovBFn0GBSoAVrVz_jE8TgJ5r1X1NGAHtJcQGfdBWwVbIM8wLgk1m5E6RIzz7VXkJopwCF4QEA6zSf4mBAHyHRIgmuCrGzkc6YV-cGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MxYd_ywfSTSDypN7ve1qPEtWEpdWvysP_Z9apNd1efLlIxwMMt2zUcpz5J5fFDV2127rlhmHuRsUilM1BYyQV6Hf4cmugjWqc260HuEmYKu7F1IfyjaORGdxfChRohhbc1-GT0GE3cGbW6eIC-jTIvhzqh-PBgtm5ub7JvdfSCQAb6xWwBGDSO-MeftjV2vCphx38QcB5TNqw6qpAA_VF1cAdiziRWJ7RnDTPbRcgk1edvrD_oMvk5WVovrUncv0osXG_iht8-H-sGZnExVRWiIhxR783wokyFMyGHbmABBFh7LCYE_PJYcDAnepWqE4ho1owcUmgj_O7TLdB1MFDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YDx3EXnc2qhAQgXXFTCpkTOiAeNnWkoy73guUmHZiuq_82n1MJ4neZZRG2WdMPd3z698zJyv7tGQ94yPANqziPJqS1g2CT16Bb1AjIEHZ2Kxn1yp8uNLsHBsLatKO16B-a-0IMV-pT9GjnweIrceL04F7oMzBgWUTEPjAagWpSZZbIqWdI4irBmp8HNifj_HW-Cg2WM5AVOsirdoQuLYFy-zoKH4NT2h64Idv6Ushoyvk1JcOjbT5LK6OAh6kZWoTzfEDQRXB5PeeTEN-9-VjO5bDER0t1dg7qvL0fOnmRC7lbbjmql9XU3tjCa0U0bOcwYQg2cNEP2evSPoKgsS3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ppXwy3I8poM2KDPcgy0jxqcUtG_4bZBNjdybueqB05HR6Uz_IP-uAGysRGsFeXKEvkeEvRrT_LOliDE3f27wqcPXEYqqZX6WFSzpY7BsTOXJaMmrtryVvmskPRjR9acSZTlx8d1qJBkRUiuZ6FI6vNqdAKWvxbFgttQlj5nxwyhVi-h8kief-na0X68Zt9y5TpxNCPbBsQUTci-Iz8iJm737ab8FxqGP60rtCurVoCxXNn9six_BkA0B91-H3xZsQctk5s8IYAIhMDrosoh8TSVT1SK7L2UBFdD97jwbyh1JTBS0nSwHc_WbC7NNplDKfR4ix6THDiA81LFBZ4Ii5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KDZY5khLzN6tXhZTKmSzbvnfc0_5PZOLdkpmlCrbsOjVVa1LvgSu2-mG9txZJEeQg1f-LcdfCESi0rKWpDNY9bsTkWyR_8I082rszLXLTbEqgSJ0zTgr15NrlzdeG8-fZ2HoeEkW8W7WHhHXoK1aBuWPKMrm-4C9-izpZMd0eJVu7Ku7vs_alLrF8rtksurnQuxNE9ekT_n89HoXFquIyAM3nqfPDCQvqDv3mwdu8m6jc4pZ0DWtYzplUi9wBdlmpYqOTOHAfPv8rtMxFgyzuqJZ7E-roEod24y5TVWSqFDXeMPUoPpwgI11EYC6ZjlB2IQmJ2__8jxBbmdajjgDPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قرائتی: مهم‌ترین جلسات هم نباید نماز را به حاشیه ببرد
🔹
رئیس ستاد اقامهٔ نماز کشور در حاشیهٔ اجلاس سراسری نماز: نماز نباید صرفاً در قالب مجموعه‌ای از مطالب و معارف دینی مطرح شود؛ بلکه باید در متن زندگی انسان و مسائل روز جامعه حضور داشته باشد.
🔹
بررسی زندگی…</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/farsna/465694" target="_blank">📅 16:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465693">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8093416765.mp4?token=USEQ3RLurVILBJp5VOIPh2XCJGV1YfTN4Qa34TNCnCNyr7Xrl4lBC1ARWdvIy6lrTz7EGShgZLledktno0afk-Kqei7Prcfy6KYx4obm2vag_lZOoqCTbFexk6kBsowFBca1SbnsNsfl0AmJKIhURImtgGORenWKT-uk1UmIQW2CB-YOKzxtWzsjqL4vWYwPjsDoyfgkDGB3gbqLAGFEBam6V8o0eCOKddp39_uJMrSsjmPxnfyI-N4hzhOZP-qkTNfXyWqa3kMb_sdskLOPqBiIshv4e3_R5A-i0x7CyAd3Pdxr2UxB7P4TGK2VEtzspGJ0k7C2y0PD14QUf7HZIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8093416765.mp4?token=USEQ3RLurVILBJp5VOIPh2XCJGV1YfTN4Qa34TNCnCNyr7Xrl4lBC1ARWdvIy6lrTz7EGShgZLledktno0afk-Kqei7Prcfy6KYx4obm2vag_lZOoqCTbFexk6kBsowFBca1SbnsNsfl0AmJKIhURImtgGORenWKT-uk1UmIQW2CB-YOKzxtWzsjqL4vWYwPjsDoyfgkDGB3gbqLAGFEBam6V8o0eCOKddp39_uJMrSsjmPxnfyI-N4hzhOZP-qkTNfXyWqa3kMb_sdskLOPqBiIshv4e3_R5A-i0x7CyAd3Pdxr2UxB7P4TGK2VEtzspGJ0k7C2y0PD14QUf7HZIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چه رفتاری در مترو سالمندان را آزار می‌دهد؟  @Farsna - Link</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/farsna/465693" target="_blank">📅 16:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465692">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">۶ حملهٔ هوایی عربستان به شمال یمن
🔹
شبکهٔ المسیره از ۶ حملهٔ هوایی جنگنده‌های ارتش سعودی به مناطق مختلف استان صعده از صبح امروز تاکنون خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/farsna/465692" target="_blank">📅 16:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465691">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36647abbcd.mp4?token=tmZrEyMWgW7O1L5s4K3daCJIHMFnI54X5NLLZH6ww-6hfs-V9b6HPpKMeFHrBwzfuoZg0VuATMpDfBtDc72qugzRqtCMzMan-RkLCHQa32Bt9mEvSBIsoR98VDAOaW2BgITtsASoc4SMRiItX3NsVoVIVvQta1AsKDGJQUiw_fObneg388sS7VbBNSTza6u1s1afcEJbxDBhaNdFuqYGrCDcMUMl6ytsqLi_ZfGPb2pxvzWspvEKZdFvGoWAMSYBFnqUghGM-nCASmxUZzTtTNN8zsn5JBROFSmMBcZyzoaq25kGsg12Y2L4hn1ivu6dhPkOA-fjRTq87la3n6GpDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36647abbcd.mp4?token=tmZrEyMWgW7O1L5s4K3daCJIHMFnI54X5NLLZH6ww-6hfs-V9b6HPpKMeFHrBwzfuoZg0VuATMpDfBtDc72qugzRqtCMzMan-RkLCHQa32Bt9mEvSBIsoR98VDAOaW2BgITtsASoc4SMRiItX3NsVoVIVvQta1AsKDGJQUiw_fObneg388sS7VbBNSTza6u1s1afcEJbxDBhaNdFuqYGrCDcMUMl6ytsqLi_ZfGPb2pxvzWspvEKZdFvGoWAMSYBFnqUghGM-nCASmxUZzTtTNN8zsn5JBROFSmMBcZyzoaq25kGsg12Y2L4hn1ivu6dhPkOA-fjRTq87la3n6GpDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اصفهانی‌ها در رزمایش جان‌فدا حماسه آفریدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/farsna/465691" target="_blank">📅 16:40 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465690">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f49959e28c.mp4?token=UfS4vWn8pD-CpwfrhKZVOved1paJ8uWfEW2O08ftk5GpJdWDFswPfEGERZ3BMLPRUnCQuv7zljrKyw2t7UZXnq_72un7VroBoDzojWLhCEhJk-pr-3OyLmFX3Z39LGxPVpVfH-TL_8-qRiZvAqHq4u5EKK90rUDUSd0hcRQkHj9QrJZ-hGsS_H6dF9AjY-5KgEf-84xGms8bWP1uAgqhPwL_kDXtpBBVIMJ25QiCI83BrMuYSopDhKnvJQBkvFIW2KDYU_yJ3XBIy-z8atxv14Gmjpg5PafRKzqJFM4Ce6n_QCUVQKW4FUvRo8iyrhS11WeiuvbhYscE8rOeCOgtBnsIPN5OJiqp2wiuSNqMbzEckEP2BPl6vh33dFtWNpYRDt7FHHfeT9HqqkfFNFbgbXUDSCFjguqPH_eMxzhGV7FgUrMuYezIOR24N-ndRsrZlzNXxQuNZXkJsnllaI52hopbu0VdxNr1BkmfptnRz-9QJCnzFlUPS7xTJgIhY0mmamYCFNR0eEFqZIgLPIEjnw2JQpn8ULpohFDSx9sYQCkU8C7jR_5_Tczf1MJgFL5ur0vHmoH_QZ0DG8bfiqCQh_JJEVjNRCvUOKX_xu2lGyW9QE-H_zg6Z_NoyU6ymbaA2uVUzpZnuOBBmTCar2jwftIHrn1AD0JzK9RoHFzMy7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f49959e28c.mp4?token=UfS4vWn8pD-CpwfrhKZVOved1paJ8uWfEW2O08ftk5GpJdWDFswPfEGERZ3BMLPRUnCQuv7zljrKyw2t7UZXnq_72un7VroBoDzojWLhCEhJk-pr-3OyLmFX3Z39LGxPVpVfH-TL_8-qRiZvAqHq4u5EKK90rUDUSd0hcRQkHj9QrJZ-hGsS_H6dF9AjY-5KgEf-84xGms8bWP1uAgqhPwL_kDXtpBBVIMJ25QiCI83BrMuYSopDhKnvJQBkvFIW2KDYU_yJ3XBIy-z8atxv14Gmjpg5PafRKzqJFM4Ce6n_QCUVQKW4FUvRo8iyrhS11WeiuvbhYscE8rOeCOgtBnsIPN5OJiqp2wiuSNqMbzEckEP2BPl6vh33dFtWNpYRDt7FHHfeT9HqqkfFNFbgbXUDSCFjguqPH_eMxzhGV7FgUrMuYezIOR24N-ndRsrZlzNXxQuNZXkJsnllaI52hopbu0VdxNr1BkmfptnRz-9QJCnzFlUPS7xTJgIhY0mmamYCFNR0eEFqZIgLPIEjnw2JQpn8ULpohFDSx9sYQCkU8C7jR_5_Tczf1MJgFL5ur0vHmoH_QZ0DG8bfiqCQh_JJEVjNRCvUOKX_xu2lGyW9QE-H_zg6Z_NoyU6ymbaA2uVUzpZnuOBBmTCar2jwftIHrn1AD0JzK9RoHFzMy7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاسخ پلیس به ادعای میلی‌گلد
🔹
پلیس امنیت اقتصادی اعلام کرد نظارت بر سکوهای فروش آنلاین طلا، تکلیف قانونی این نهاد است و ادعای «کارشکنی» یا «محدودیت‌سازی» را رد کرد.
🔹
به گفته پلیس، اقدامات انجام‌شده پس از هشدارهای متعدد و در پی عدم‌تمکین میلی‌گلد به برخی مصوبات و ضوابط و در چارچوب قانون انجام شده است.
🔗
اگر شما هم جزو افرادی هستید که پول و طلایتان را از میلی‌گلد تحویل نگرفتید، برای حمایت از پویش فارس‌من
اینجا
کلیک کنید.
@Farsnews_My
-
Link</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/farsna/465690" target="_blank">📅 16:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465689">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJL1LNfHkmTUgLXzwCLiMpS2bstiyqM8VVlQ2eaGZsk1MZWZusOwH7tIJcmLeeQwBxvY9-MiyVpPJxaU8TYGGRYZguFbZbwDsoIe5DLpy9W1Dlw0heORWdVvVmE8fUWqBH2ZkVmxZcntHrg2wj4fx_cmVuLe0JHVqrh55z8UEpan4JkaAs6DUgWDWt4jgEKFCiY83IqNVLiiLSXVx2JJoJ368zCLDba2Fbf0iMRfIw9LvXB_P8Q2-MP8BB6sGO69DmnpL6K1JBAcOf6u3yZCCBcJrfP1waNItgoiJ9W5j2AHkGS-IUMtEUGWICFekvBHdk3tN51yZRpkQfc4Qw9U9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا اصلاح‌طلبان قواعد مذاکره را رعایت نمی‌کنند؟
🔹
مذاکره در سیاست خارجی صرفاً به‌معنای نشستن دو طرف پشت یک میز نیست؛ مذاکره زمانی معنا پیدا می‌کند که هر طرف با اتکا به ظرفیت‌ها و اهرم‌های خود، برای گرفتن امتیاز متقابل وارد میدان شود.
🔹
با این حال، بخشی از…</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/farsna/465689" target="_blank">📅 16:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465688">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">شناسایی ۵۱ صفحه و توقیف ۲۴ صفحهٔ مجازی فعال در قیمت‌گذاری کاذب ارز
🔹
قوه‌قضائیه: در طرح ضربتی برخورد با قیمت‌گذاری کاذب ارز در فضای مجازی، تاکنون ۵۱ صفحه فعال در این زمینه شناسایی و ۲۴ صفحه نیز توقیف شده است.
🔹
۱۱ نفر از گردانندگان این صفحات نیز تاکنون دستگیر شده‌اند.
🔹
در یکی از موارد شناسایی‌شده، فردی که در حوزهٔ قیمت‌گذاری کاذب ارز در فضای مجازی فعالیت داشته، دارای ۱۶ کانال تخصصی در زمینه قیمت‌گذاری بوده است.
@Farsna</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/farsna/465688" target="_blank">📅 16:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465687">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f67b218df.mp4?token=FNE9RQNhd0Tn3UCKfRql7KvY6knK8LF6k7FSC9IKAOPoq_9uRDf0paj4Tigno_u73SF-OLEzlI-CXn6oTL3vXFBrq9yxlf3MiysBWx-nl65FLbrv-Rdx2jyfb4WzBau8vM1vj0la3jeDcmP049MEr3gDcAAtHvwW0ceNDKfms3HTpIoqOo_KE0snX8EuYg1_Qq3E5KRAuT0iuCLl6_CUyoWbL-dMUMKDQIBpwLHlRevfC9Zp6eqDLRpKBmJPkubzv8NCAfX3yk0LywmMqlC5O43PwL7gnYBsskWsTg_BiMXI-bjMCP5oOrSgxsLyQ2IyovOc5M0oHTWoN8HykGbpNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f67b218df.mp4?token=FNE9RQNhd0Tn3UCKfRql7KvY6knK8LF6k7FSC9IKAOPoq_9uRDf0paj4Tigno_u73SF-OLEzlI-CXn6oTL3vXFBrq9yxlf3MiysBWx-nl65FLbrv-Rdx2jyfb4WzBau8vM1vj0la3jeDcmP049MEr3gDcAAtHvwW0ceNDKfms3HTpIoqOo_KE0snX8EuYg1_Qq3E5KRAuT0iuCLl6_CUyoWbL-dMUMKDQIBpwLHlRevfC9Zp6eqDLRpKBmJPkubzv8NCAfX3yk0LywmMqlC5O43PwL7gnYBsskWsTg_BiMXI-bjMCP5oOrSgxsLyQ2IyovOc5M0oHTWoN8HykGbpNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بهنام ابوالقاسم‌پور در منزل شهید حزب‌الله: قهرمان‌های واقعی اینجا هستند؛با وجود حضور در خط مرزی، خانواده شهید خانه و منطقه خود را ترک نکرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/farsna/465687" target="_blank">📅 16:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465686">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c459f0d9c.mp4?token=evYBhDnm_yQJfcnX7q5rN0yeFjjeiSH-zdoQnDVDCcJy5afzD43Ij0Hqws5LQCQmMKulMRTUtpvJ2qKocH3JMhXr2t-pbdcA1t9FN6VK2rnb-zDBf50Vyws6MCJCNXzhATUYh7ZQNxVcpstkRuq1SZwTwru2m6CP1HWl9PG7kS3NHSFIq4NhOFhU_2jS1UIIz6WBE_2jwgWQ5CQV5BwK74W2p1J7CYw-F5h_Nvdn2mTwe0r39fPFxpfK3INOg4cwEN-d9h9bP6jkfkg6pdOyBepUj9PhMiDMLDg8NcbFKQpgjsTE6HUuqqFK8kjyHjejuLrYuHqN3sqBJK7sx1DUtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c459f0d9c.mp4?token=evYBhDnm_yQJfcnX7q5rN0yeFjjeiSH-zdoQnDVDCcJy5afzD43Ij0Hqws5LQCQmMKulMRTUtpvJ2qKocH3JMhXr2t-pbdcA1t9FN6VK2rnb-zDBf50Vyws6MCJCNXzhATUYh7ZQNxVcpstkRuq1SZwTwru2m6CP1HWl9PG7kS3NHSFIq4NhOFhU_2jS1UIIz6WBE_2jwgWQ5CQV5BwK74W2p1J7CYw-F5h_Nvdn2mTwe0r39fPFxpfK3INOg4cwEN-d9h9bP6jkfkg6pdOyBepUj9PhMiDMLDg8NcbFKQpgjsTE6HUuqqFK8kjyHjejuLrYuHqN3sqBJK7sx1DUtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روسیه یک پل مهم کی‌یف را هدف قرار داد
🔹
خبرگزاری فرانسه: برای اولین‌بار «پل جنوبی» که شرق و غرب پایتخت اوکراین را از روی رودخانه به یکدیگر متصل می‌کند، هدف ۲ حمله پهپادی روسیه قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/farsna/465686" target="_blank">📅 16:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465685">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9cXQ76y7gK792k8Axe9H7nWqS3aIToJVXJ75BlC9KhER0MDpBMYrf7ZrU8_LE2nBDoPeebX5Hl50-DqSb7_Q2y1xjVzj-Xnd1x-kudre7BlL-5mmXsfHm_QXiMviUd-gxrmU2q_5C80F0X75UHrN38fJJ2rOWiKno_fgtYOnsb3kzSMNElxJc5JiObiPK6ieRSvVOmSIwbNl05q4Gyw1V4bUdvrzBQ4sVr0TmSWvK2LB8HHo8kyxB9wRA-0kWB9RlUzmNp2sY_cDHAY45PCbDf3_kjciDxABdJh4HN3EQKTcftsMNI_sCv98PXocuPpJ9v7YcsCREHMuf1CE5IPQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعات میلیون‌ها نظامی آمریکا هک شد
🔹
اطلاعات شخصی حدود ۲.۸ میلیون نیروی نظامی فعلی و نزدیک به ۳۰۰ هزار فرد فوت‌شده آمریکایی در یک حمله سایبری به سامانه اطلاعاتی پنتاگون به سرقت رفت.
🔹
هکرها از مهر ۱۴۰۴ تا تیر ۱۴۰۵ با سوءاستفاده از یک آسیب‌پذیری امنیتی، به اطلاعاتی مانند شماره تأمین اجتماعی، نام، تاریخ تولد و سوابق خدمت نظامی دسترسی داشتند.
🔹
پنتاگون اعلام کرده تاکنون نشانه‌ای از سوءاستفاده از اطلاعات سرقت‌شده پیدا نشده، اما هویت مهاجمان همچنان مشخص نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/farsna/465685" target="_blank">📅 15:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465684">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/619042ce0f.mp4?token=rKvcQX9pTFBc__nHyofojd8Mvr5Emt3L1CGU9gfDPF3tTSCv4FLsy1X8-JiUXBCCNida8qTOgnDBGTEXMYLbaSeKgvHjGCEXnfOT8QTR6OPZv2qDpAbWsev_mj76yP3EFEE9sPEoAYtHWTpE34Emb3yxQpAWt0YjEsxrQSeS-AAe4MaRWx1VsM1YW-7tBy-nDYvFQJ8n5j9lLWrGTYqNYoF62GHGoRyVW6P8i7dFTG8lK6AoZ5WKmzTa-nPOt__QEQei1_lYdDU7oJ1G_hP7-Y1VoKj7QpE58yfupCsmu1_4KuIPE734r6z-IWN5xE-U7LNjjOv6JDE7Ri-Riod28E0SfJeh6X3MfBp1bVPpo8Mq5I3Ljfgd4SGShmU-3B5Qsk6lGb0qWC7JjqvaC-za6P5U9xBFiSm3ZmqD6vqAfoQ3RO3R2JgKp66UHHjnChz9gf2zUpg83fnARpgwiYyKH3kcekxi8s_Xeky3Z75RYfRgN_5lYOFM7_ZA6hBXVHt4Ji--vPicXxA30Io5iv0gPwT4ax_A_mPP1zcGJRS4FBsYhHZRFGaIzVRM3C70H74S9lXLbBDPxP-Tb8zLSdbk-LDoctHJhfI_tvKukz1uUqZ2o4Zln9sF4nwg7gPD3UwYAHxTRvTsZRTqavvNV87n-_O2NgJijnC4yMMQJkMpOt8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/619042ce0f.mp4?token=rKvcQX9pTFBc__nHyofojd8Mvr5Emt3L1CGU9gfDPF3tTSCv4FLsy1X8-JiUXBCCNida8qTOgnDBGTEXMYLbaSeKgvHjGCEXnfOT8QTR6OPZv2qDpAbWsev_mj76yP3EFEE9sPEoAYtHWTpE34Emb3yxQpAWt0YjEsxrQSeS-AAe4MaRWx1VsM1YW-7tBy-nDYvFQJ8n5j9lLWrGTYqNYoF62GHGoRyVW6P8i7dFTG8lK6AoZ5WKmzTa-nPOt__QEQei1_lYdDU7oJ1G_hP7-Y1VoKj7QpE58yfupCsmu1_4KuIPE734r6z-IWN5xE-U7LNjjOv6JDE7Ri-Riod28E0SfJeh6X3MfBp1bVPpo8Mq5I3Ljfgd4SGShmU-3B5Qsk6lGb0qWC7JjqvaC-za6P5U9xBFiSm3ZmqD6vqAfoQ3RO3R2JgKp66UHHjnChz9gf2zUpg83fnARpgwiYyKH3kcekxi8s_Xeky3Z75RYfRgN_5lYOFM7_ZA6hBXVHt4Ji--vPicXxA30Io5iv0gPwT4ax_A_mPP1zcGJRS4FBsYhHZRFGaIzVRM3C70H74S9lXLbBDPxP-Tb8zLSdbk-LDoctHJhfI_tvKukz1uUqZ2o4Zln9sF4nwg7gPD3UwYAHxTRvTsZRTqavvNV87n-_O2NgJijnC4yMMQJkMpOt8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ژیلا صادقی در لبنان: مردم بیروت عاشق وطن، مقام معظم رهبری و سید حسن نصرالله هستند و اجازه زورگویی به باورها و سرزمینشان را نمی‌دهند.
🔹
مقاومت ادامه دارد چون هنوز شهید می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/465684" target="_blank">📅 15:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465683">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8aa171770.mp4?token=RMH1Jt20QLDBVNUNCMxjyjA9D9Rl_CE2WZTtCAERbWFpI2gmkC2C39R7I73ESJW8ML2NWfBLpIEpOj1cPXWAwlPU_JorNiSLrJe8Ki2AmtvbDNyaum0DEEMnvdbYcLO85Aac3wAeSrpHzgf4qdUAYVNDCleNSmYH9u5LSyTlTH5rSJgFx8NTeJUK-93VH9vrJQx0X-2-hY71ooakRbMsHb4lUT3kWOnv67zK6IuMSxf5kz4zjJNGv2Q1q5b4EjbnXSnG0Vh1axWDRuLVc6Wk1r-NSZ3QTOmne6m8ofC32p6IYABUks6yClFISD_Ih0mi51K2s-4k8JkWpcCJ_MTxiYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8aa171770.mp4?token=RMH1Jt20QLDBVNUNCMxjyjA9D9Rl_CE2WZTtCAERbWFpI2gmkC2C39R7I73ESJW8ML2NWfBLpIEpOj1cPXWAwlPU_JorNiSLrJe8Ki2AmtvbDNyaum0DEEMnvdbYcLO85Aac3wAeSrpHzgf4qdUAYVNDCleNSmYH9u5LSyTlTH5rSJgFx8NTeJUK-93VH9vrJQx0X-2-hY71ooakRbMsHb4lUT3kWOnv67zK6IuMSxf5kz4zjJNGv2Q1q5b4EjbnXSnG0Vh1axWDRuLVc6Wk1r-NSZ3QTOmne6m8ofC32p6IYABUks6yClFISD_Ih0mi51K2s-4k8JkWpcCJ_MTxiYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رضا علیپور پس‌از کسب مدال نقره: سرباز مردمم و پارتی من خداست.  @Farsna</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/farsna/465683" target="_blank">📅 15:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465682">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ca4b25d5.mp4?token=O9siD47w08NZ2fHky_89Fg0EDlUYCDstL-B9nH26zoJMqPKdxc4FSYUG33r8pxw6Rt3yTj4SsBkXn5wNbYWjY7srl3pKAc4iK4vRKhWpxHWea6OfP5ConX368Qs8GY0s5ISEHXXzewOwWb5HygLK6l9MDVx4ssFefyx4muj3Yp5YsWz5GIqbH8jhKdPMkwIi0_6QDMiODYqOK4g_Hy65tch8zwXA6aE9zVc6YRLAnBQpiUstLpI1YKKaDW1ylbq0eXcKAhCygDYT24Jbhxz0VktG6HQIxsnKASfmHxX31-_vmNsfdvKbOMrc9QLt5XpxcOGl4Ky3AtUNZvoVTVo8OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ca4b25d5.mp4?token=O9siD47w08NZ2fHky_89Fg0EDlUYCDstL-B9nH26zoJMqPKdxc4FSYUG33r8pxw6Rt3yTj4SsBkXn5wNbYWjY7srl3pKAc4iK4vRKhWpxHWea6OfP5ConX368Qs8GY0s5ISEHXXzewOwWb5HygLK6l9MDVx4ssFefyx4muj3Yp5YsWz5GIqbH8jhKdPMkwIi0_6QDMiODYqOK4g_Hy65tch8zwXA6aE9zVc6YRLAnBQpiUstLpI1YKKaDW1ylbq0eXcKAhCygDYT24Jbhxz0VktG6HQIxsnKASfmHxX31-_vmNsfdvKbOMrc9QLt5XpxcOGl4Ky3AtUNZvoVTVo8OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علیپور نقره‌ای شد
🔹
رضا علیپور با ثبت زمان ۵.۳۶۲ ثانیه به مدال نقرهٔ مسابقات صخره‌نوری آسیایی ناگویا رسید. @Farsna</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/farsna/465682" target="_blank">📅 15:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465681">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">شاکری: از امروز تا انتخابات آمریکا باید سطح تنش را بالا برد
🔹
مجید شاکری، اقتصاددان: تا زمان انتخابات میان دوره‌ای آمریکا یک گلدن تایم ۳۶ روزه باقی مانده است و جمهوری اسلامی باید سطح تنش را در این ۳۶ روز یا حفظ کند یا بالاتر ببرد.
🔹
تاکید می‌کنم که این افزایش…</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/465681" target="_blank">📅 15:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465680">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad297dc73.mp4?token=amzPwvI4Jsv1dAQc6ye4yfjBsbfHwhDAX3jU-7F0UjyggiGHc4-IPdpUJ4iU5SDhfEFk_bJl7SOyiXyTdrFlnAxMSsGwTVUfagCBFzV7vKLtDyZg4a5lGpNjBpLDWSdpXpn9ZKTfVURgwJvwWuRsd_JTvpT7kqRC7vS1p-3Gc5UTiGWo1XvKw4QXTHEeZb7rAeyCbz7c1M89l5Lk1LkXwrpuwWEIyPHLLAeBoUGSSPfz5GDeSBAaxehjYxJ2xxeWbA8StnsXOA3lHTivRCLItCH2DRtu1pfiUXH1dk0mAF8pPwyF7x2k5OqB0KsWPYid8C_bUgJY0LReeQoJ2tJXhB-uzKfeGqWycOqBsJu_BP7bjiPHFAhpMHZ9PYJwfJ4oXg5PLb76tknG-1msU3mafOO2rE8U7qJdlXTZyaub65qvDYM3YVXSKKc0ndqCqZb8lsV_tD-v5PPD9rDwjgIez2pKwN0Ov6_LAl2B8Ck1XCK9Byq7PWV3FV8RTzxt87RkoEp_BRtxL9CnPBYMHKa4Jwo00ktAcilkdsN_KWlNiJpJ5xoN0rJ0TdUAIuCBm1PtIKgXZxKtpsDg50DXK8iH6dzMbfKFuKW1PPvR_iQXP9XK8JYroRMTor6qBn1reIeVSjLcOyRTLU7JzcM958KZjWeGjxPdpKnLWdnFPxDVnk8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad297dc73.mp4?token=amzPwvI4Jsv1dAQc6ye4yfjBsbfHwhDAX3jU-7F0UjyggiGHc4-IPdpUJ4iU5SDhfEFk_bJl7SOyiXyTdrFlnAxMSsGwTVUfagCBFzV7vKLtDyZg4a5lGpNjBpLDWSdpXpn9ZKTfVURgwJvwWuRsd_JTvpT7kqRC7vS1p-3Gc5UTiGWo1XvKw4QXTHEeZb7rAeyCbz7c1M89l5Lk1LkXwrpuwWEIyPHLLAeBoUGSSPfz5GDeSBAaxehjYxJ2xxeWbA8StnsXOA3lHTivRCLItCH2DRtu1pfiUXH1dk0mAF8pPwyF7x2k5OqB0KsWPYid8C_bUgJY0LReeQoJ2tJXhB-uzKfeGqWycOqBsJu_BP7bjiPHFAhpMHZ9PYJwfJ4oXg5PLb76tknG-1msU3mafOO2rE8U7qJdlXTZyaub65qvDYM3YVXSKKc0ndqCqZb8lsV_tD-v5PPD9rDwjgIez2pKwN0Ov6_LAl2B8Ck1XCK9Byq7PWV3FV8RTzxt87RkoEp_BRtxL9CnPBYMHKa4Jwo00ktAcilkdsN_KWlNiJpJ5xoN0rJ0TdUAIuCBm1PtIKgXZxKtpsDg50DXK8iH6dzMbfKFuKW1PPvR_iQXP9XK8JYroRMTor6qBn1reIeVSjLcOyRTLU7JzcM958KZjWeGjxPdpKnLWdnFPxDVnk8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل در دبی زمین‌گیر شد
🔹
شرکت هواپیمایی «فلای‌دبی» امروز اعلام کرد که پروازهای رفت و برگشت به اسرائیل تا زمان تکمیل تحقیقات جاری دربارهٔ پرواز جنجالی دیروز به‌حالت تعلیق درآمده است.
🔸
روز گذشته پرواز فلای‌دبی با ۱۷۰ مسافر در مسیر دبی به تل‌آویو، پس از…</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/465680" target="_blank">📅 15:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465679">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f679fd6ff8.mp4?token=GPjdAFuWZbN81qCVjd_WU_hJ8e9ztksXEdW70ksrY4sIZQa_xXyXf60wp3kQavRLzz6lE7mS8ghNC3Qd1tA6GIpcOO18rYkGWaow7sjwqBFzaUra6bdY_RRN43uzJhk-edZIM8B7-bokxzXvXyciTIgETne01ADpEcRBMT12NgazTGQHCOshpyU-i9zo8gSGClXRQgzbi9GpAGdd6GdYtNi-IJXzNXmVIDDBjnWuKUOmGRr3IQioYlE1eTa2xvaG3IKpb0Mc1znWla7MRHsKc8SRcrD6Q58o-dgk-rEurPTOot3LU9ZD1fyfgHJcY-ECz1f_zmqXb9MuQBu11-2BcY2LF92k-oHbwhRf_g5KDVu3VF5o4kfGNPLPr_4UnbnaNoc6rXpE087CCR56XM5pZ6rEEdWR0Fq9hEm-uWAK8v8Ei7JdZwXFbbY6KzPuh_P9rwt1p8orwK2z92Fh-Jme8osyHLgWT-dXfY6bYN61TTTRQ3yXy9B9zK0uLi2TTYX0e6ylK-UZyLqUs5BH_Om13-2gVuO3wMDFz8R_6oJusfzEET46lU8MyW5bwhhM5miGUADV9Qom0XAbj9LL54mH6rOgVXjTc3eCP6uKc0ds60a288oC9lEow-mhTk2yOFbnspprm6McObdI3mziqM00RkYJzJsfYSAYxecd8DNGCvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f679fd6ff8.mp4?token=GPjdAFuWZbN81qCVjd_WU_hJ8e9ztksXEdW70ksrY4sIZQa_xXyXf60wp3kQavRLzz6lE7mS8ghNC3Qd1tA6GIpcOO18rYkGWaow7sjwqBFzaUra6bdY_RRN43uzJhk-edZIM8B7-bokxzXvXyciTIgETne01ADpEcRBMT12NgazTGQHCOshpyU-i9zo8gSGClXRQgzbi9GpAGdd6GdYtNi-IJXzNXmVIDDBjnWuKUOmGRr3IQioYlE1eTa2xvaG3IKpb0Mc1znWla7MRHsKc8SRcrD6Q58o-dgk-rEurPTOot3LU9ZD1fyfgHJcY-ECz1f_zmqXb9MuQBu11-2BcY2LF92k-oHbwhRf_g5KDVu3VF5o4kfGNPLPr_4UnbnaNoc6rXpE087CCR56XM5pZ6rEEdWR0Fq9hEm-uWAK8v8Ei7JdZwXFbbY6KzPuh_P9rwt1p8orwK2z92Fh-Jme8osyHLgWT-dXfY6bYN61TTTRQ3yXy9B9zK0uLi2TTYX0e6ylK-UZyLqUs5BH_Om13-2gVuO3wMDFz8R_6oJusfzEET46lU8MyW5bwhhM5miGUADV9Qom0XAbj9LL54mH6rOgVXjTc3eCP6uKc0ds60a288oC9lEow-mhTk2yOFbnspprm6McObdI3mziqM00RkYJzJsfYSAYxecd8DNGCvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علیپور فینالیست شد
🔹
رضا علیپور در نیمه‌نهایی سنگ‌نوردی با توجه به خطای ۲ حریف خود همراه با دیگر نمایندهٔ چین به فینال صعود کرد. @Farsna</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/465679" target="_blank">📅 15:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465678">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ed9d34d24.mp4?token=CUPUOvHyAbl3JYYiVsSmMhrKTE5PZZnWT-qd05GMBTzdgOYoNRrB7KWmW_u4KYPlynGGc-VJ2kYRkUzTkwa0SoFiBoHs4P8X3_4E8VjkF0vD3gnStKl2nfJaT7pBaHxFnI0lAVyfw2r_SadJondt_SSAjBcscxk9MkNkPRxwxC4wojxq5z7gyO9AJNeo5RHwJRauATj4Hwmh6jKXiH4gmOl_3Li56Yv8NhvCe4pROj3Xn2AqQESSk-bUwvAkuNttcRoNh938XoF2lOop-74XeCmwblwVbe2HUBVS-3PeNtUyQgYFKilA-qp-5Qs6euiVbeIYnecRQJvwApYi8pO3azVoClpHFoi3Kn7vKAseXK0YNXbnlnl3tR9IHtlSuCvIW7rtMY1Ii9Wxai82BTUv3AxwukZvaPCaO76GW5QE6waITgHz832SQqzPvpnrFrVy6krVUd_ClRb3qKfeXpifgb6Cmu-Txf14QKfBhJiT4R96qIKrFwxCvqKNqpT5dhR_xJdxhIWsnohmF0MgiZDL5UR-QgEgrgtDOghrnmIE_T4-0QGjtKVslPLkFEFttkbTQTHOgtDq-E0wXmMExV_d-xjdrfs69EpDEa7USpyMsr3gPFryRhsIvjgCNn7N7D4toAiUvr-wK6hfCRAhSkbPYYgWjpaSzZnLCq_-0NWdqVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ed9d34d24.mp4?token=CUPUOvHyAbl3JYYiVsSmMhrKTE5PZZnWT-qd05GMBTzdgOYoNRrB7KWmW_u4KYPlynGGc-VJ2kYRkUzTkwa0SoFiBoHs4P8X3_4E8VjkF0vD3gnStKl2nfJaT7pBaHxFnI0lAVyfw2r_SadJondt_SSAjBcscxk9MkNkPRxwxC4wojxq5z7gyO9AJNeo5RHwJRauATj4Hwmh6jKXiH4gmOl_3Li56Yv8NhvCe4pROj3Xn2AqQESSk-bUwvAkuNttcRoNh938XoF2lOop-74XeCmwblwVbe2HUBVS-3PeNtUyQgYFKilA-qp-5Qs6euiVbeIYnecRQJvwApYi8pO3azVoClpHFoi3Kn7vKAseXK0YNXbnlnl3tR9IHtlSuCvIW7rtMY1Ii9Wxai82BTUv3AxwukZvaPCaO76GW5QE6waITgHz832SQqzPvpnrFrVy6krVUd_ClRb3qKfeXpifgb6Cmu-Txf14QKfBhJiT4R96qIKrFwxCvqKNqpT5dhR_xJdxhIWsnohmF0MgiZDL5UR-QgEgrgtDOghrnmIE_T4-0QGjtKVslPLkFEFttkbTQTHOgtDq-E0wXmMExV_d-xjdrfs69EpDEa7USpyMsr3gPFryRhsIvjgCNn7N7D4toAiUvr-wK6hfCRAhSkbPYYgWjpaSzZnLCq_-0NWdqVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اهدای چفیهٔ متبرک رهبر انقلاب آیت‌الله سید مجتبی خامنه‌ای به رزمندگان مجاهد حزب‌الله لبنان در خط مقدم نبرد با ارتش رژیم صهیونیستی در کنار رودخانه لیطانی
@Farsna</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/465678" target="_blank">📅 15:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465676">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8830ec81.mp4?token=fyXSqp3r0wmKjNIfreFe0I1bV1pMwCeAIva4395hsoTsi3d-gr7F86_bxBCbcHg6yVyI0ai6uwZiJoW8j_4leh4aMHsTJj2XhHZ5l2LeD-XvF5uEJg61dqtDMxudCEikJvArqTnwHAGCv0rqAm98ETz00ZnCXTaVVeo5YKbI7pRV5HhIcySIFBJUuLSwitRIiwLpsoOHjPyIMD9bwCrkhZvaWvPlCu8_NJ_LFmn3uW4o9D488fpoEz_cFAXtKW0qtkmNjquMH-RrbWanx8lPBphXVJvckRC4FVbqPdJ7jceE4nNXVnVYtjRnesimkqKatkwU32hn2mjhaBQVoi4B2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8830ec81.mp4?token=fyXSqp3r0wmKjNIfreFe0I1bV1pMwCeAIva4395hsoTsi3d-gr7F86_bxBCbcHg6yVyI0ai6uwZiJoW8j_4leh4aMHsTJj2XhHZ5l2LeD-XvF5uEJg61dqtDMxudCEikJvArqTnwHAGCv0rqAm98ETz00ZnCXTaVVeo5YKbI7pRV5HhIcySIFBJUuLSwitRIiwLpsoOHjPyIMD9bwCrkhZvaWvPlCu8_NJ_LFmn3uW4o9D488fpoEz_cFAXtKW0qtkmNjquMH-RrbWanx8lPBphXVJvckRC4FVbqPdJ7jceE4nNXVnVYtjRnesimkqKatkwU32hn2mjhaBQVoi4B2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علیپور به نیمه‌نهایی صخره‌نوردی صعود کرد
🔹
در ادامهٔ رقابت‌های سنگ‌نوردی رضا علیپور، در مرحلهٔ یک‌چهارم نهایی ماده سرعت مردان، با ثبت ۵.۰۴ زمان و قرار گرفتن در جایگاه دوم گروه خود موفق به صعود به مرحلهٔ نیمه‌نهایی شد. @Farsna</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/465676" target="_blank">📅 15:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465672">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XGDcWYQbbIPFUVoiiSavKxp580f_K3NAau2wCufZMT8Us_MaAoLpPB3RUTfIz-ctp47aiaaN93e-x9850qS5ky-lHrgOkZiNoKbo_wPUIcaLVBe4pSDhjMY7IhMy1uXxILtRX72IakSrkQg6V_Bs9HoKho_B4o8zondsnNVxOU3r1ttwbGDV1eoMyulrShimtW9--LomR_S2F4saOEU6tQbFQLhruVZ9PR8xy2Ua4OjjObmBNc3mp1vckoPr1rUefbeo_P6FS4pFD4t4cBjtl7mzDkLen41NnHPHKr3QFD1xYsiA2Dxmk3FnLi8eb0Y1rfvl7POCaShFjUhTUkPRcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fzIJpDa8H6Ub-ows0VgtcgumrQs8bUvgHuDJTnmUOW4-_5sNT-LFBZ74JRcQtWkybEzRJSlV4fejzQQwWfvFcAhfpdfbuMtHvzjTYnrh7zFKrUcSHo0zsTFOp4ngdC3xFII7ZjYTLW8_HzjOGPAka1C26Wd8HEs6VsQ2PjYtphNAnI_7YXGMZpYe1stQV_xpSVzuFqDXGtwD3rhzcyOqyXaZijB_uCDPPqAqZqOQev8_kiBFQ_z1QAl_qcg_50zlq6ZRjC6m6vPkhZssF4g_aLYWMqd0hVEPSdJuH8SyXfIOwiI0UDKIekwKpVjevXrcxD1SblUIlkdy4aHy0LAWDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cXMWHRsLWWxT62rd0FuF5RWTL0aMydQVy44rzDk0Z3BRN_0WUPbWdG9Qklbj7t3WKbNf60uY5vLsiNuK2CR3gBy5qdbH6H1HwVZAF2zlNGe6OkW2CEC7_UXPHefe7vkKFbJBvg-93RBMYTZ2cz1ct31NnnqqB5Y2vIPwO9v9qEB_Sp0LkQkxj7MqH7silwvxK-ayeswJ2fwVY4pTj6CVkMliu7bS7ivl_B6JK4767DqdU0T2rbup8gbvgJ6fS_hSXC9u5_bgdjbpSklAFdqIEr1KEUxHH-C0D26xWkayQHcpBEewLpwRWGHzmyzWsBMscE5py_iIh_SNya4yXho3Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ns6qg4TmNieS4TRv3wbIx4uiHj3omCgV8NodQyEbEVF-vT6xwIkbvXnnYj10kxaoc3Hd5oHeOrVgY6N39kbzZG1hcaAnc6NOEHaBc6279vh4IXRTDcW4ByQsAtM7BDzNfA6Lh0ufbBypj4KTY-Xq1STWr-JxubGLlwt2Ph1o7Mn9jYwl4p8K2uFxC7TIwLHmWoG10KZaVC22Z7dpOdcaGSXu9Ev0UGtJ44ZZvZ_q6m7R-BdZ9n_9aOckY5PI8gTsNYqcFhBX8ezhiuOlyBVJCG8m1KBjURVEqjS7-PGaHEcQlbpOZyLz25Hr0yTcOgNeZzW4HFHwTF0GkX2XvA0NJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان: به‌طور جدی دنبال برطرف‌کردن موانع کسب‌و‌کارها هستیم
🔹
رئیس‌جمهور در جلسه با کارآفرینان و صاحبان فرایندهای اقتصادی: مبادا تصمیمات اقتصادی و مداخلاتی که انجام می‌شود، خارج از حد تحمل جامعه باشد، زیرا به ضرر خود عمل خواهد کرد.
🔹
به‌طور جدی به دنبال برطرف کردن تمام مسائل و مشکلات مرتبط با حوزه کسب‌وکارها هستیم.
🔹
بیشتر موانع را از میان برداشته‌ایم تا با وجود محدودیت در دریا، راه صادرات و واردات و تعاملات اقتصادی با کشورهایی همچون پاکستان، عراق، ترکمنستان و آذربایجان از مرزهای زمینی گسترش یابد.
🔹
برای آنکه در مقابل دشمنان سر خم نکنیم، همه باید دست به دست یکدیگر بدهیم و موانع را از سر راه برداریم؛ با هماهنگی و وحدت می‌توانیم دشمنان را ناامید کنیم.
🔹
سران قوا به دنبال این هستند تا مسیر فعالیت‌های اقتصادی و بهبود شرایط و معیشت مردم هموار شود؛ بنابراین از طرف سران قوا قول می‌دهم با تمام وجود موانع را در راه خدمت به جامعه برداریم.
@Farsna</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/farsna/465672" target="_blank">📅 15:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465671">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4e7deded0.mp4?token=J5dYhYLvmk4Thrh1V62g0rLon4Qd1xcrH5V9KDb3lJrS-0nikSwP42G7gQfVmiq-vlZ7QDozjAqDPffmxph17gdeeQYetlE9JsTtgfCUavaAMiHQ-lVSu-9sfkQG6fnNrQQSGT63sjbeYj4-Z4zqxKkKE4D4D49b8ADIPOymGRorLBwa8x7yxn-aXwHfGHy9J12CavJJjHBaHssXvX29ZHh7T-D1caC9jIBLY5wMIRBD7jJSjZUrTZVuSFNNqjiURjGFI-3xoS2eJu9aA_ShM52X1NMN-MMwyrMtSYri7afCzhflycvGZHQwO2mOStHSlvHNauX0sXO2iy4W4nt-3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4e7deded0.mp4?token=J5dYhYLvmk4Thrh1V62g0rLon4Qd1xcrH5V9KDb3lJrS-0nikSwP42G7gQfVmiq-vlZ7QDozjAqDPffmxph17gdeeQYetlE9JsTtgfCUavaAMiHQ-lVSu-9sfkQG6fnNrQQSGT63sjbeYj4-Z4zqxKkKE4D4D49b8ADIPOymGRorLBwa8x7yxn-aXwHfGHy9J12CavJJjHBaHssXvX29ZHh7T-D1caC9jIBLY5wMIRBD7jJSjZUrTZVuSFNNqjiURjGFI-3xoS2eJu9aA_ShM52X1NMN-MMwyrMtSYri7afCzhflycvGZHQwO2mOStHSlvHNauX0sXO2iy4W4nt-3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علیپور به نیمه‌نهایی
صخره‌نوردی صعود کرد
🔹
در ادامهٔ رقابت‌های سنگ‌نوردی رضا علیپور، در مرحلهٔ یک‌چهارم نهایی ماده سرعت مردان، با ثبت ۵.۰۴ زمان و قرار گرفتن در جایگاه دوم گروه خود موفق به صعود به مرحلهٔ نیمه‌نهایی شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/465671" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465670">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🎥
صحبت‌های شنیدنی حسین یکتا در خط مقدم و  نقطهٔ صفر  نبرد با رژیم صهیونیستی هنگام وضوگرفتن در رود لیتانی
@Farsna</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/farsna/465670" target="_blank">📅 14:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465669">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2906dbbe59.mp4?token=mfNBOLMoKnq69QzJJjXSxDtoFN-jpA4ksy_Bd25BW15rkwxVqLwaGRN1u82kBAYBASA3CEvvW1A78xtYa7lBxi8S3CKW_VdG066Q_8RYMvPScT5BIP5FjmGbpFZCuNefsboDHb8gA2fkwSOsIMKOyQRR5N7lsDVOSdXpuvORx9UlB0BNNnw4xH0oJGWcSXwClDT6PCrG0CqCsYgDBSoeAeJvEM-wOTuNSgbFGkRMdedpgQRR5stTYYx_qUYq0yCvBWY_efy2edTiQKMv4jYieTKxfE8lMwxaR7FscDxdUdmzUUXcNw8ddvPtB_hPlkWun6dZPvCqLQZYcYb_60mEi2rXSsjkkj243_9a8XvqHSb_SMsjb--ANc3e14iKMwC39vtKibLH5R5BuaKbkTuLXMsojBCrMBLSosRKhGsTDWMP59pDRt2FciA6ld7Aco4HUXZP6vLt6ObhuBrFEgC5swaUOGem73jQoyE-EsWJQThbgX-_sn7VTCUgBhn_ytLw_WwlIX7ST7SmqB8wXwaLPskf9CTBlASe1SHmJ8SFS8exGiayLDJ0Zg5J_hFlYsiZmQyP7Jrt_zKTmoXhZTeNBz8MTQ06XHs66thlf2k8nGVNh94hLV_k2VNOIIUfEpLBngrbOKaxP9qtzUTp1kYcCUZcpmNldND_dUP6jCW1__Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2906dbbe59.mp4?token=mfNBOLMoKnq69QzJJjXSxDtoFN-jpA4ksy_Bd25BW15rkwxVqLwaGRN1u82kBAYBASA3CEvvW1A78xtYa7lBxi8S3CKW_VdG066Q_8RYMvPScT5BIP5FjmGbpFZCuNefsboDHb8gA2fkwSOsIMKOyQRR5N7lsDVOSdXpuvORx9UlB0BNNnw4xH0oJGWcSXwClDT6PCrG0CqCsYgDBSoeAeJvEM-wOTuNSgbFGkRMdedpgQRR5stTYYx_qUYq0yCvBWY_efy2edTiQKMv4jYieTKxfE8lMwxaR7FscDxdUdmzUUXcNw8ddvPtB_hPlkWun6dZPvCqLQZYcYb_60mEi2rXSsjkkj243_9a8XvqHSb_SMsjb--ANc3e14iKMwC39vtKibLH5R5BuaKbkTuLXMsojBCrMBLSosRKhGsTDWMP59pDRt2FciA6ld7Aco4HUXZP6vLt6ObhuBrFEgC5swaUOGem73jQoyE-EsWJQThbgX-_sn7VTCUgBhn_ytLw_WwlIX7ST7SmqB8wXwaLPskf9CTBlASe1SHmJ8SFS8exGiayLDJ0Zg5J_hFlYsiZmQyP7Jrt_zKTmoXhZTeNBz8MTQ06XHs66thlf2k8nGVNh94hLV_k2VNOIIUfEpLBngrbOKaxP9qtzUTp1kYcCUZcpmNldND_dUP6jCW1__Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عبدولی طلای آسیا را صید کرد
🔹
علیرضا عبدولی در یک کشتی حساس در دیدار نهایی وزن ۷۷ کیلوگرم بازی‌های آسیایی ناگویا، با پیروزی ۵ بر ۳ مقابل قهرمان المپیک از ژاپن، مدال طلای مسابقات آسیایی را شکار کرد. @Farsna</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/farsna/465669" target="_blank">📅 14:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465668">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZS3E_bb6q5vI96EM2i-ckY1yVJ0CBSTeaJ4kj1mT6detJf12at6Pd5HCiwuvxjshbGTw5kOGZLa51-f5jiDLa0eSiQjQdS_ksAPVhIF9LxYnn3nbvPvWehd41EFQfy-GJTnH3f2Vbs2vOE0SKycDffLeW9lSOm1KH8kJU1Gk4mhdg7Vr8EGr_1BZWVB2A4nxUbLJjYFCH89Pffj4vKeOFTTkHmI4vg9FMwoM78nez7nmNYLRcAb-JXnEt1MXP4D8qlIw4wg6EBN1_lbSwbIhm5Vyovqz64MIawuFmpAb4Dus5MI4LgOX_E_wf8UizPVmlLDCspeI0RLqKrXehDsqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتراف نیروی دریایی آمریکا به خودکشی ۸ ملوان در پایگاه اوکلاهما
🔹
نیروی دریایی آمریکا تأیید کرده است که در فاصله سال‌های ۲۰۲۵ تا ۲۰۲۶، هشت ملوان این نیرو در پایگاه هوایی «تینکر» در اوکلاهما سیتی خودکشی کرده‌اند؛ رخدادی که بار دیگر نگرانی‌ها درباره وضعیت سلامت روان نیروهای نظامی آمریکا و شرایط کاری و زندگی آنها را افزایش داده است.
🔹
به گزارش «میلیتری تایمز»، این هشت مورد خودکشی در واحدهای وابسته به واحد «ارتباطات راهبردی یک» نیروی دریایی آمریکا رخ داده است؛ یگانی که مسئولیت بهره‌برداری و پشتیبانی از هواپیماهای E-6B مرکوری را بر عهده دارد. این هواپیماهای بوئینگ ۷۰۷ اصلاح‌شده که گاهی «هواپیمای روز قیامت» نامیده می‌شوند، در صورت وقوع بحران اتمی برای برقراری ارتباطات امن و فراهم کردن امکان فرماندهی و کنترل نیروهای هسته‌ای آمریکا مورد استفاده قرار می‌گیرند.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/farsna/465668" target="_blank">📅 14:39 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465667">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ec8467d36.mp4?token=sQsNsP6gMYx8v4eDDXb0_zYR17KlFTkPtkaxFEtsxWhEF14F7JjVVP7sFzfOEzVe6xw9J2v_Tp1-JrvXiAAqk7dPINC0FRrb_XYVm1yPkJA7onxulOp57OnT2EDlbVV2xwgk-oQ98UhZC0Ebz5g9UhWJZO9mDSCzV0NlqZldMGz9tAbRseWMDyyjMmjaCffmnh7mR4jl6fJlsfOJSSf21X5JZb-3lCq2etN0GtRwZlPKbde3R9DntgnmCyqFF1iOyfp72xXcr8-A9F1DsMYAQxorUe0AVZ3xtS6WXLhdULOGowj_Z5EHLgY0_XoPY3wU1ccwJhqYd1YU3azpBPPt_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ec8467d36.mp4?token=sQsNsP6gMYx8v4eDDXb0_zYR17KlFTkPtkaxFEtsxWhEF14F7JjVVP7sFzfOEzVe6xw9J2v_Tp1-JrvXiAAqk7dPINC0FRrb_XYVm1yPkJA7onxulOp57OnT2EDlbVV2xwgk-oQ98UhZC0Ebz5g9UhWJZO9mDSCzV0NlqZldMGz9tAbRseWMDyyjMmjaCffmnh7mR4jl6fJlsfOJSSf21X5JZb-3lCq2etN0GtRwZlPKbde3R9DntgnmCyqFF1iOyfp72xXcr8-A9F1DsMYAQxorUe0AVZ3xtS6WXLhdULOGowj_Z5EHLgY0_XoPY3wU1ccwJhqYd1YU3azpBPPt_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سقوط مرگبار بالگرد پزشکی در کالیفرنیا
🔹
سقوط یک بالگرد در کالیفرنیای آمریکا به کشته‌شدن ۲ نفر، انتقال ۲ نفر دیگر به بیمارستان و مفقودشدن یک نفر انجامید.
🔹
به گفتهٔ مقام‌های لس‌آنجلس این بالگرد اندکی پس از برخاستن از جزیره کاتالینا در نزدیکی لس‌آنجلس سقوط کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/farsna/465667" target="_blank">📅 14:39 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465666">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDtbewkIxLBTm5n-YG72m3QmiScOt17QIR65xcTdVBPB5dOJ5WtZeV887SzhRmgbvy-epOgBNBl6gY3O0UuScZ1HlMMwTrF_g7-goi-YgDcOvus0lPMR_bqu5bw5Nt76ee1Ds_BDlE76nCNmRBISW0wESRCWL059CI8zIqLthScL5wLn0G4HV38WaZHqc-R1ru6FyT9z075mCFzjNL0simgbUS2PllTmVsTS0DND1H2ftT1d4pIEAq7YbMmZBGGwcTeM5h2_qqPojg90NnKYtRZyNCzXQqjxoYx0SzwqSqn0eLXYO1PbC_hkhG948H_-iFxUe5q6QL9oSM3UUuxlVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
اجتماع گستردهٔ مردم زنجان در رزمایش جان‌فدایان  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farsna/465666" target="_blank">📅 14:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465664">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9669fdc33.mp4?token=R6JEmsTnzVSPvae2cTR217rOwSEXDanEOVVHiihT-rbGJEEnvQ7VP5c6tVzhzCr9aXELvWwQEkIwy_9tXG6bpI_iYcwT9dyD7XWRfKTRoRZXtdiEfSBh_HJkocSonZzE1RXCBsql0EzrxDXb-p7ibJlS4ak1d1WlzzHXXT8jmxTuZ3M2T5b86bba0U4vt6pTpIhAodsQvnG0hn2qgg6Mhqa1ie73qNMBGBVpQUuCozL-83GSmlxjpGoJ7x6BmyM2PsbL9hSgPC8C6FBvlwyj1xCTtB6mN5ZwGsw1jTc9h5cHS0M5fDJ8OGfWjT14EsaZydQDcbg1jvi04cWWIA6JGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9669fdc33.mp4?token=R6JEmsTnzVSPvae2cTR217rOwSEXDanEOVVHiihT-rbGJEEnvQ7VP5c6tVzhzCr9aXELvWwQEkIwy_9tXG6bpI_iYcwT9dyD7XWRfKTRoRZXtdiEfSBh_HJkocSonZzE1RXCBsql0EzrxDXb-p7ibJlS4ak1d1WlzzHXXT8jmxTuZ3M2T5b86bba0U4vt6pTpIhAodsQvnG0hn2qgg6Mhqa1ie73qNMBGBVpQUuCozL-83GSmlxjpGoJ7x6BmyM2PsbL9hSgPC8C6FBvlwyj1xCTtB6mN5ZwGsw1jTc9h5cHS0M5fDJ8OGfWjT14EsaZydQDcbg1jvi04cWWIA6JGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ کشتی‌کار ایران هم راهی رده‌بندی شد
🔹
مهدی بالی در نیمه‌نهایی وزن ۹۷ کیلوگرم کشتی فرنگی مقابل ناکازاتو، حریف ژاپنی‌اش ۵ بر چهار شکست خورد و به رده‌بندی رفت. @Farsna</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/farsna/465664" target="_blank">📅 14:28 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465663">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DL-1Ik8oDlNCo7iuvMXdrEVv-ijWbnY7T_c5pqnQhi_boP2-f9jREM9DvWtlnKuPIQq2wuc3mudaP2uoixRqrsCF43hdXOAS9DE1dnvDXqpdh73pOYCaI1tTjXjy7O10WBQfkju66tLU26vwoGRA35xC3mub-jJLbGtnf03K0jSZj2oS_0bqtZKbzrPkJPl7M00q2UH2hyVXPfNl2ALkX3U-mJQFjCG2jBm6op9y9jldcwvI708O4P9_SMYzbSQT7n2OLbdWM3UoAOIMA7rIW9oFvFzmK6HVwafMx1Smq61jwk0RHiPFasTgstZrkraBpGxSoiEOm39tfNBE-rDXtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام قاطع تهران به بغداد: برای صیانت از روابط تاریخی فوراً اقدام کنید
🔹
در حالی که آمریکا تلاش می‌کند با اهرم تحریم، روابط راهبردی تهران-بغداد را  محدود کند، سفارت ایران در بغداد با رویکردی قاطعانه از دولت عراق خواست با اتخاذ یک تصمیم فوری، از روابط دو کشور در برابر پیامدهای این تحریم‌ها صیانت کند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/465663" target="_blank">📅 14:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465662">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb78d8f11f.mp4?token=ZN-VbZu3lVKWwHZEaMt9SGImrdXW4f5pq3NXTUMd8IOxBBBq57XaBLLouMv2IzmGYtboFw8u1RBpx1zNwBhXoiRmOdLlSEpl6riH81sBEzUZXtUo0X-BN69mX4eV5nxf-ZW7a-0qIZoP6DRR-mt5j3JRRNp7zkVVEOS8y3NsXs6TcwpXNYnlLsnxdqQIcAxOXN0dsedF7iIKqZr7p9DDx0-bjResePO_vf_Xu46UCx2gwLreEKV4eZtwbiPn6tkBkPjYP3HQ_sCSFrlmCrmhWZDSldc7Kw6jmv8CQNkDM-wfuJdAkl4HfmfoR_9THwx0jBRU77LZYkxRhH4sVdngYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb78d8f11f.mp4?token=ZN-VbZu3lVKWwHZEaMt9SGImrdXW4f5pq3NXTUMd8IOxBBBq57XaBLLouMv2IzmGYtboFw8u1RBpx1zNwBhXoiRmOdLlSEpl6riH81sBEzUZXtUo0X-BN69mX4eV5nxf-ZW7a-0qIZoP6DRR-mt5j3JRRNp7zkVVEOS8y3NsXs6TcwpXNYnlLsnxdqQIcAxOXN0dsedF7iIKqZr7p9DDx0-bjResePO_vf_Xu46UCx2gwLreEKV4eZtwbiPn6tkBkPjYP3HQ_sCSFrlmCrmhWZDSldc7Kw6jmv8CQNkDM-wfuJdAkl4HfmfoR_9THwx0jBRU77LZYkxRhH4sVdngYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هلاکت ۶ نفر از اعضای گروهک تروریستی در زاهدان
🔹
قرارگاه قدس نیروی زمینی سپاه: ۶ نفر از اعضای گروهک تروریستی تکفیری به هلاکت رسیدند و تعدادی هم بسته‌های انفجاری از آنها کشف شد. @Farsna</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/465662" target="_blank">📅 14:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465661">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4de848d651.mp4?token=KOlwfJlZtcFLHx1XiTrMkwB2ohDtNKRCKqgZUp8uThANQ_c9k8xuwDq1g8_HPRhWTqgG1d0LBgiJZpLvAPyy3zriJHdnsN5ybPFwSncev8YMq1UWrvgArrylGtKQBS-f6Q2VS-jyShoYTT10YRCkt4sxxAdGDJkVBfkqVRTfnwTiRskzxpPqUYISIlM8NMJ-Au0LRYvGJKLyBUjoXIP8L9P2OPVgX8501Ajd_xlQ-auaYYBQcFTI7imS3khqU_rBEvRTUqfKlzqiykxyf3XFZ1S_qzp2c5faGRERrl2SJal9EVn42M9TWX0vNiKkbCP0fxC5JTpqIi8BKO1eUDpeICutIs7lwiNLN15Rk-ZyYD6LM4UyV6-es54wYK5rKn_R4yqFQOdBj5Rf-rcC1qKWMEeT5QJdUG4XbwjKx8PHjv5WKG9KkZEA_bBtiErKMSuyfjVFmYrRGeac2bYSmpuQJV6D9wZG9r3poYNyx6GidUKhLLMwTf5zi2W7d_mK8qEauR4M_2ziAC0ruLofqCXi5YBrFrQowTgP3yilI5x_MkoTwBBG3KE0CkaEz5rZr9PMC6hszrOW18rcbUexlzaURCHsqB_QkM3Lzs3ONT2C1qSyPRWTI1rsYjcILcdsCNn-6ywp_7MkBtV4ct9j9cV-P94gRoABRr4U8fi2gurwo2E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4de848d651.mp4?token=KOlwfJlZtcFLHx1XiTrMkwB2ohDtNKRCKqgZUp8uThANQ_c9k8xuwDq1g8_HPRhWTqgG1d0LBgiJZpLvAPyy3zriJHdnsN5ybPFwSncev8YMq1UWrvgArrylGtKQBS-f6Q2VS-jyShoYTT10YRCkt4sxxAdGDJkVBfkqVRTfnwTiRskzxpPqUYISIlM8NMJ-Au0LRYvGJKLyBUjoXIP8L9P2OPVgX8501Ajd_xlQ-auaYYBQcFTI7imS3khqU_rBEvRTUqfKlzqiykxyf3XFZ1S_qzp2c5faGRERrl2SJal9EVn42M9TWX0vNiKkbCP0fxC5JTpqIi8BKO1eUDpeICutIs7lwiNLN15Rk-ZyYD6LM4UyV6-es54wYK5rKn_R4yqFQOdBj5Rf-rcC1qKWMEeT5QJdUG4XbwjKx8PHjv5WKG9KkZEA_bBtiErKMSuyfjVFmYrRGeac2bYSmpuQJV6D9wZG9r3poYNyx6GidUKhLLMwTf5zi2W7d_mK8qEauR4M_2ziAC0ruLofqCXi5YBrFrQowTgP3yilI5x_MkoTwBBG3KE0CkaEz5rZr9PMC6hszrOW18rcbUexlzaURCHsqB_QkM3Lzs3ONT2C1qSyPRWTI1rsYjcILcdsCNn-6ywp_7MkBtV4ct9j9cV-P94gRoABRr4U8fi2gurwo2E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار بلالی: هر چقدر لازم باشد موشک می‌زنیم تا دشمن ادب شود
🔹
مشاور فرمانده نیروی هوافضای سپاه: نرخ شلیک موشک‌های ایران به‌گونه‌ای است که حتی در صورت تداوم رویارویی برای چندین سال، امکان ادامۀ عملیات با همین نرخ وجود دارد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/465661" target="_blank">📅 14:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465660">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d49320b4a.mp4?token=d7Rp1m5WaPL8prqb34zsg-qOy4gyLETIWqmXHOWAfeS-MhLMUoMpYNy2GKHV9bQSxbxM_t-6t8jdwxMQ_FhFiD6qWHNUSQJQnDKakrP8p88HO0_I759XBtKV_h5QNqIVoC9b9rgqxCrY_zwKcrUFGIuA5FgsMg9Zr_GLXxkuTTnHjIazcUnxzCdWxUpBALd-wwE4_7GPDzrxutrTMwmRu_HHM4PPwfpot6-W9pSokTZ4XSZd7JOkOFqYUcsji4hMGO1VOYWk-AilK-6zX5tpXhziWBDHkXec-muap4fPCdBrheF4JV5yV7Gs8FovfJGBfTKYkqa_QqBU8D_3Lf28dR3TNY-hyVqy14J9WBok-D22PmG2EPvWN_4G7YOXW1BTzjuqA8vCtTqq2MYyvyesxymdhihUB8os2pTROUA559Db9I92rpjd0VxPxiANnrtnDsP2eKEB9wFr_XmfepaXiBIXmKdZyKmFJecJLI9jQKJuFzE0DYTCVbxl6jcFkrFkfaPNkugxKrM3-eBZR3eHPAc_hChr9KBsIVCAh_srQ66diqFI8Jb9-k0SL_bKkL3wxOM8DAbMBOSNDDuRzCnPqSJkRZ5q7rbBkGbUduWxDLCa0CjmRaYn-qbt72LJyIneiQbQ3AW3ki_WJJX0vPrTbUd-m1KTf0_kyRWNYytd4QM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d49320b4a.mp4?token=d7Rp1m5WaPL8prqb34zsg-qOy4gyLETIWqmXHOWAfeS-MhLMUoMpYNy2GKHV9bQSxbxM_t-6t8jdwxMQ_FhFiD6qWHNUSQJQnDKakrP8p88HO0_I759XBtKV_h5QNqIVoC9b9rgqxCrY_zwKcrUFGIuA5FgsMg9Zr_GLXxkuTTnHjIazcUnxzCdWxUpBALd-wwE4_7GPDzrxutrTMwmRu_HHM4PPwfpot6-W9pSokTZ4XSZd7JOkOFqYUcsji4hMGO1VOYWk-AilK-6zX5tpXhziWBDHkXec-muap4fPCdBrheF4JV5yV7Gs8FovfJGBfTKYkqa_QqBU8D_3Lf28dR3TNY-hyVqy14J9WBok-D22PmG2EPvWN_4G7YOXW1BTzjuqA8vCtTqq2MYyvyesxymdhihUB8os2pTROUA559Db9I92rpjd0VxPxiANnrtnDsP2eKEB9wFr_XmfepaXiBIXmKdZyKmFJecJLI9jQKJuFzE0DYTCVbxl6jcFkrFkfaPNkugxKrM3-eBZR3eHPAc_hChr9KBsIVCAh_srQ66diqFI8Jb9-k0SL_bKkL3wxOM8DAbMBOSNDDuRzCnPqSJkRZ5q7rbBkGbUduWxDLCa0CjmRaYn-qbt72LJyIneiQbQ3AW3ki_WJJX0vPrTbUd-m1KTf0_kyRWNYytd4QM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقدامات قطعی دشمن در روزها و ماه‌های آینده!
این ۳ دقیقه به اندازه ساعت‌ها دوره عملیات روانی و سواد رسانه ارزش دیدن دارد
@Fars_plus</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/farsna/465660" target="_blank">📅 13:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465659">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GI1odwbmaWuYzahdVz1C3QEnAoMZCMvYSMIJLcr0e_TaNZqvnt2gIbuQfsybjBko1-lDjLTriMjmKWXwQ6UoAl2fhVTBMgw7gz_rLDIdOMPTU9YKDyQmc1jNTSY_Ps6jIPyNISg25lLb6ZZxJ6e1nPUg_0JD3ujxXuMuOD2-ntHvazOHF1J5_uyAl6p5HwPwLTJf0uMY4qPhyl0Cmb0RGzoFDqlK4XQ0wxUIq7YzuIAGY4dCMBMpxa6WfpbqTvEcPm70SRpdB0SzsGz4n3arG8OKtGTWc2xv7Gz-dq_v81JBubZ5zPMl8jmYLqLUeEtvRdDLNvFF04dq2BlxsxUi0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
عبدولی طلای آسیا را صید کرد
🔹
علیرضا عبدولی در یک کشتی حساس در دیدار نهایی وزن ۷۷ کیلوگرم بازی‌های آسیایی ناگویا، با پیروزی ۵ بر ۳ مقابل قهرمان المپیک از ژاپن، مدال طلای مسابقات آسیایی را شکار کرد. @Farsna</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/465659" target="_blank">📅 13:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465658">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b271ab9f73.mp4?token=PUZmqd0TbXADQoGiFQySkoMQuTPTkIKOWlvoTiCnJFJuzqHLB7xu6i8SIslfol1DtODeU_-ixu4Gs9S4g-obtV69Nd4CENBoKJSMLJ1g5Vz1wKtUYwOP-ZGSI997--8WY8ubppLQnjd_BxgseF5ENypjzOeBSMulhcS2V9HZdWgfiDPUEowAUZ2s7xwbkgRzhnZDiBamTNzU78v8zLCQQMN0f4wSh4ZgwtuF4lYe1LNSzxXY9VCcJc7RWcgJRMOEjuTN2BNSs4APffgpk-vFDtO-4ILPkieCTHPayUjDyt1g9E-F5aZHjN3wFdWi2Hbns9e7KC6E33gxVGcbkgvY2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b271ab9f73.mp4?token=PUZmqd0TbXADQoGiFQySkoMQuTPTkIKOWlvoTiCnJFJuzqHLB7xu6i8SIslfol1DtODeU_-ixu4Gs9S4g-obtV69Nd4CENBoKJSMLJ1g5Vz1wKtUYwOP-ZGSI997--8WY8ubppLQnjd_BxgseF5ENypjzOeBSMulhcS2V9HZdWgfiDPUEowAUZ2s7xwbkgRzhnZDiBamTNzU78v8zLCQQMN0f4wSh4ZgwtuF4lYe1LNSzxXY9VCcJc7RWcgJRMOEjuTN2BNSs4APffgpk-vFDtO-4ILPkieCTHPayUjDyt1g9E-F5aZHjN3wFdWi2Hbns9e7KC6E33gxVGcbkgvY2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ عبدولی همشهری‌اش را برد و فینالیست شد
🔹
سعید عبدولی در نیمه‌نهایی وزن ۷۷ کیلوگرم کشتی فرنگی بداغی، کشتی‌گیر ایرانی‌الاصل قطر را شکست داد و راهی فینال شد. @Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/465658" target="_blank">📅 13:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465657">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GOPuubrnGJSzNY8QWchdcC1U0vxwGdoNWkdMMvcvtO3a4lfkFp-4ni-HnJnOO3lBSW99J6b_UGT-8jMRdUfqoYjP8ad5yCAyhiZLmRI-EgHl9UG8aUPAO_TXKMRjZ9mxXgQqjdNtOYCmdypeXAQf71xRU58-r02Q6bGCa_6x9QZsJa_rUEWbBJu8O23nEc8J37uo3JhQmDitotiQPiER9p6TbQumilRdZfXYE5BZz1tHhpqFuInJTWJJ0oBn0sFOu6Sk5PazG8FLNINF75loTRZ1RRBy1j6iyVQwRnDSfB34NRh_fmWPZHL2bjR1VUPS4c8RlufaXqo5LD9tBN7QOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام ۷۸۰ باند قاچاق موادمخدر و کشف ۲۵۰ تن مخدر در کشور
🔹
رئیس پلیس مبارزه با موادمخدر فراجا: در ۶ ماهٔ نخست امسال بیش از ۲۵۰ تن انواع موادمخدر کشف شد.
🔹
در این مدت بیش‌از ۷ هزار قاچاقچی و توزیع‌کنندهٔ عمده دستگیر و بیش‌از ۷۸۰ باند فعال موادمخدر منهدم شده است.
🔹
همچنین حدود ۸ هزار خودروی مرتبط با قاچاق موادمخدر توقیف و بیش‌از ۳۳۰ سلاح غیرمجاز کشف شد.
🔹
۱۹۶ عنصر اصلی قاچاق موادمخدر در فضای مجازی نیز دستگیر و بیش‌از ۴۶۰ کیلوگرم موادمخدر از این افراد ضبط شد.
🔹
در یکی از عملیات‌های مهم، یک باند قاچاق شیشه که از شرق کشور به‌سمت مرکز و غرب فعالیت می‌کرد، منهدم و ۱۱ عضو آن دستگیر شدند. در این عملیات بیش از یک تُن شیشه و حدود ۸۰۰ کیلوگرم تریاک کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/465657" target="_blank">📅 13:40 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465656">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a8da3574.mp4?token=OQf9T-E0qLJfF8NIcbpM2aVeociRbkoAJSMP6dhaIwA1I7v5z45Tla9krPGcFSTUyEvRH3WDNKIm7_NvODOZNmnuBx0vSjttgln0nFu5H0A_TmSUmsce35b1q6F-VrsVmRxXCZmimvtr1a80R9qKJMnkoAQtlc6ARvX1EIvroSei0ZsEeST1ruH3L8V9PvP0vTgZmraTKM-daI9j0n34HOKmciy6BVyE8oLQspDW7-k5RFUXBT6bwMp3JyBwYsZnOTvaqLhQSVQ9SycaeFyxiZt3xPGxg6-aKSY3ApAQ-ZjnYdIKdEqGjKAB8Gvgxi_JvrBNsQQWPX5jvDajijuUrUPYI88FYC85-yQUt_njXdkTBJ-zb64rFyAoXgW_RRbOuT3lWRSWqzfMS-JILKo8ilViqRl_X6hOOBTg66hn7De4XN9VYfSqC1OE_NDidXBIekrPfFoiRlh2w1qS1VUGbMMc3k1XctLP2lC2zynFIDM9RN36_Z-RVsqLY7-NCUNDDS17mSXAIaLZ32ZHLtv0-pTro45VQzHfUFMDf1SFsQAfuR9bo3avM1vLkj--I1r5KW-H5i-ZdhOxRAaMjufBwlxNbb6YG2Q8nVz_69qQs5_mvC6slDHYLsJi8ZlotAi3tXnplGiNCaPRBSEjcCDbbt9UTYptlJtyROMfgyDIsQM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a8da3574.mp4?token=OQf9T-E0qLJfF8NIcbpM2aVeociRbkoAJSMP6dhaIwA1I7v5z45Tla9krPGcFSTUyEvRH3WDNKIm7_NvODOZNmnuBx0vSjttgln0nFu5H0A_TmSUmsce35b1q6F-VrsVmRxXCZmimvtr1a80R9qKJMnkoAQtlc6ARvX1EIvroSei0ZsEeST1ruH3L8V9PvP0vTgZmraTKM-daI9j0n34HOKmciy6BVyE8oLQspDW7-k5RFUXBT6bwMp3JyBwYsZnOTvaqLhQSVQ9SycaeFyxiZt3xPGxg6-aKSY3ApAQ-ZjnYdIKdEqGjKAB8Gvgxi_JvrBNsQQWPX5jvDajijuUrUPYI88FYC85-yQUt_njXdkTBJ-zb64rFyAoXgW_RRbOuT3lWRSWqzfMS-JILKo8ilViqRl_X6hOOBTg66hn7De4XN9VYfSqC1OE_NDidXBIekrPfFoiRlh2w1qS1VUGbMMc3k1XctLP2lC2zynFIDM9RN36_Z-RVsqLY7-NCUNDDS17mSXAIaLZ32ZHLtv0-pTro45VQzHfUFMDf1SFsQAfuR9bo3avM1vLkj--I1r5KW-H5i-ZdhOxRAaMjufBwlxNbb6YG2Q8nVz_69qQs5_mvC6slDHYLsJi8ZlotAi3tXnplGiNCaPRBSEjcCDbbt9UTYptlJtyROMfgyDIsQM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رزمایش جان‌فدایان با حضور پرشور مردم زنجان آغاز شد  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/farsna/465656" target="_blank">📅 13:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465655">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdd59013c8.mp4?token=SkJY9qsmNRq3sPyiQATgR53AXXMSOHyau9wDO5Nq4izZoZZbWVBzqsQNkQ8q_fWxhg0awsh92V9SN6mDd7LHk-x2_j592Vwri-9DeU-1iB_ElLCZe_8w5yZdniMQPgvlPqUWluEPd_Lok090gKV5bTl6GUHtu_iFCK0nrFCmdJDTxAoa0rHdtHycdqDxqF6qGwU0N9qEkO6pzMsSZ8vnaOgUpV2jTz_gq2LF3aD43c8EFGHVhzECZVD1okBS3_uchqCdNNpyUIf4pcZtypFaYg96DKzjzZcoCTaLagEB1k-_E_50s_mIsrcWJwkZVWyL8KmMvR69lMrHUYQUT3E2RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdd59013c8.mp4?token=SkJY9qsmNRq3sPyiQATgR53AXXMSOHyau9wDO5Nq4izZoZZbWVBzqsQNkQ8q_fWxhg0awsh92V9SN6mDd7LHk-x2_j592Vwri-9DeU-1iB_ElLCZe_8w5yZdniMQPgvlPqUWluEPd_Lok090gKV5bTl6GUHtu_iFCK0nrFCmdJDTxAoa0rHdtHycdqDxqF6qGwU0N9qEkO6pzMsSZ8vnaOgUpV2jTz_gq2LF3aD43c8EFGHVhzECZVD1okBS3_uchqCdNNpyUIf4pcZtypFaYg96DKzjzZcoCTaLagEB1k-_E_50s_mIsrcWJwkZVWyL8KmMvR69lMrHUYQUT3E2RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امضای سند راهبردی دیپلماسی قضایی تهران و مسکو در کازان
🔹
در حاشیهٔ اجلاس دادستان‌های کل کشورهای عضو سازمان همکاری شانگهای، سند رسمی «برنامهٔ همکاری بین دادستانی کل فدراسیون روسیه و دادستانی کل ایران برای سال‌های ۲۰۲۷ تا ۲۰۲۸» امضا شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/465655" target="_blank">📅 13:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465654">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYqm1Iqe6Ta68BxeskHevnQ6oPGG3N4EaTDOTTvqFmkbv-iVPVeO1Q9FNEQamLx3vHLHPOcUclF7Fz4H0ts4XjR8BpatZeZbGLXFZer8JHEzBl6amfaT8Vzs-gvTMJ8B4fS8R81hdTjaNoobQJSq_HhlP5fCqvIH8W1EcJ4Kx7ev1WYI85C8VgkblmTdUoSf74Fmzv205MMhxMQx98l_9JJnnXwmP3tOgNJt7XjCBJNV897u5JlOYhdMnzbIZGGJXJ4UtA24suv6GQoyqKlYR_t1YQuxHiNJ6jBPAFI_UsNRanWlygK6Sd4vZ58eNzLdSbhn7AZlQfuwUMpwaLxe6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۴۹ سلاح غیرمجاز در اصفهان
🔹
فرمانده انتظامی اصفهان: ۴۹ سلاح به‌همراه اقلامی که در کنار این محموله قرار داشت، کشف شد.
🔹
در این رابطه چندین نفر از قاچاقچیان سلاح دستگیر شدند و چند دستگاه خودرو نیز ضبط شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/465654" target="_blank">📅 13:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465652">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9Ioxnal8dQa07_ZvCZbzFm6IN9qnx28U9ZEAZwglfNh-N2O27eADJ-CPvVmVVWdMR_Bc3H-BquHaqc_d770_HwcoZHoq08CoGnUIdwI_iic-dmKxOtREUM6WU1MggNzhG2M5KPkwWYFDW9mkayL7KiWRbsg5EB037AS-AtFYoz8xAVUyJjebvAvJyTdOSii6b7-QA_aHll0tsvG4U1EadFakW4iFqEa-P2K0J-roX9ZSFDxx_54Wek94r7x_AvVXWPQeDLE-S0gW8gl8opvhq_u7Ox__mMWdBexToPVdOaydGrgXnE6RtThLXlw5pDog-rBz6uoRqJgAAMuVwpnOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ عباس‌پور به فینال نرسید
🔹
سجاد عباس‌پور در وزن ۶۰ کیلوگرم کشتی فرنگی ۸ بر ۴ به گانیف، نایب‌قهرمان جهان باخت و به فینال نرسید. @Farsna</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farsna/465652" target="_blank">📅 13:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465651">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBj0nVbZp1YsYg4SPPPKG4E06MQr3-J_CxvoON1lx6fnhwJynz_AknIxSFMI1fR6H67qTPXnG6C1-Au4WOG2toeENUd1ynkA10DmmTekQzDZTVqTtXEMmAmrlIczTjG4yfmpp9iAmGpcyxGL1GNHNxxB067yHutD2piM41XoZHf3WLHAvUVP5n0c86aNUxrMIjZiKRVe-c0WV6BwONv0hs3Ka-rJ_NWdTe936qaTOYBRPJR-crNbSqEq4u313l9Yf8V1uOlVSJBYKSYqTXHbli2Qr1aiFVu2CNDBXGaQma8s4dm5Vftssqf_xjcRkwtynyn7o_MUndOuKUZyG7KJ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ عربستان، مسافران صهیونیست را راهی اراضی اشغالی کرد
🔹
فرودگاه تبوک عربستان اعلام کرد که پرواز فلای‌دبی با ۱۸۰ صهیونیست ساعت ۵:۴۰ فرودگاه را به مقصد تل‌آویو ترک کرده‌ است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/465651" target="_blank">📅 12:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465650">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqTvUmdNF0u4AxgIOImwq100uFtCEpcVgaJtRj57dEvTroHoH6UPSLMp23kbTvCtW24N809O8IHffvcctzCwouwW2XEgnfwBtk7b5czz6UL72g4OT6MNCYlOjNm5LIiSq7YTRCDtncfm6GW-PNiTkXsF71hJZnN7891cmOtkGPtAEK0PckqYA2L8xstFia4WQyL0iIxGyAJLEfjCQyfyCqOBaMS-FXpeESgkdZZCSDlmCrp-ZE__z6yOU4uzXRd1rSBGfztr43X1OmCaFld0x10pZHpWxZy2lNQ0dI0huESV3q-2fypQnoEQcy7KizmtWCnHF_oyScEZZE7bLz0k1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیماها در آسمان عربستان سرگردان شدند
🔹
ترافیک ورودی فرودگاه ابها در جنوب غرب عربستان سعودی امروز متوقف شد و دست‌کم ۳ هواپیما در آسمان این فرودگاه در انتظار فرود ماندند.
🔹
علت این اختلال هنوز مشخص نیست و اطلاعات موجود نیز بسته‌شدن کامل فرودگاه یا وقوع حادثه‌ای مشخص را تأیید نمی‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/465650" target="_blank">📅 12:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465649">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">بازی ایران و گینه‌بیسائو منتفی شد
🔹
فدراسیون فوتبال برای برگزاری سومین دیدار تدارکاتی، با فدراسیون گینه‌بیسائو مذاکره کرد و تاریخ ۱۴ مهر برای برگزاری بازی توافق شد.
🔹
برگزاری این مسابقه در ترکیه به دلیل تحریم‌ها و محدودیت‌های منطقه منتفی شد. گینه‌بیسائو آمادگی سفر به تهران با پرواز چارتر را اعلام کرد، اما به‌دلیل عدم پرواز شرکت‌های هواپیمایی خارجی این گزینه هم به نتیجه نرسید.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/465649" target="_blank">📅 12:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465648">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IB6oHkyf02LrdEXytpxJqa55tv2gL9-FbhuOR1YVUz34aFMRuQE4XarDZMRB6d5jYOw2XiLzA8LNMIlUh4V8IAt9SF6avlqlsMo7_iqZQgEJUJd8kG1QLvudNTgpRT53lum5T_6qA26PMYheB3hW9TZWLpjR-jhZecSPEV7dM9iLRgfcSgDUtEgyw0FBmketHoj44t3t8NGYzCI6PAy0vfNo7D2kTmpR_1A6QzOhE52QrOKI7BQw39oJhY4GhOq77ZUh5XOuM_IEk1TgMk32dgZsHMcYNEzrNVeRXu79Txlia646K_ZYw7NfwC5kzX3uqWr9JP0u0tsXvOAZB2T5OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش بزرگ در تاسیسات گازی امارات
🔹
تصاویر منتشرشده آتش‌سوزی بزرگ در یکی از تأسیسات فرآوری گاز شرکت ادنوک در جنوب‌غرب ابوظبی را نشان می‌دهد و گمانه‌زنی‌هایی دربارهٔ احتمال هدف قرار گرفتن این تأسیسات به‌دنبال داشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/465648" target="_blank">📅 12:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465647">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsrv5SnnNhamBwkWkiiW5EvqhwAwSNJWO-ll2qNmFYkfGoUcuVOhrk-IK-7IrLrGGblv4bvC9tl_NyvN5ppsAEN7bG6bv0O0f3MEkMzMzN1LYbslPvQSn-WzJuYDEyBFtK68nA2hTWgGxeCrLgQoujtXjfmX-hTs1Gv1J4cLKUvstlNF60ELc_0uR4AyH5YME9aO_tpYFc55xwNi10YVQADMnjG0-5vy7YcIgOrIe0U2uop5DGmin15kkkY3acfeEwyq7CIPpkg0stt8l-64vQ6t8nobXn_uKJlDqol3MOhfIKKWv9hlYkEBiYc366lVuYNK_UF0RAgbGq4tGT-hAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترخیص کالاهای دارویی بدون تخصیص ارز کلید خورد
🔹
وزارت صمت ۸۰۳ ردیف تعرفه را به فهرست کالاهای مشمول ترخیص ۹۰ درصدی اضافه و گمرک آن را ابلاغ کرد.
🔹
با قرارگرفتن این ۸۰۳ ردیف در فهرست ترخیص ۹۰ درصدی، واردکننده می‌تواند ۹۰ درصد کالا را پیش‌از تکمیل همه تشریفات و بدون تخصیص ارز از سوی بانک مرکزی ترخیص کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/465647" target="_blank">📅 11:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465646">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ceH6xfTSu7ChvT1haxjQSqDFX3OIthhJROgyIvlsHSt_KLoXmbRfzigO7lm1Ei7YitCT0hBrImnJgqDlODq2uBiWFduFalmYxxgwE7_9pzfqtLtElCVGAPnNWKnxfZTmj8jvSJrBr3KoDiSjENKWsxqTTV5jwmvuKnJHA7JliBfie-vKJOoHuxi_Cex8Mh_4SrJ9aK43qD2_i_veZgPrOuHYcUWcFrCBELIXMgXsqDGgublAU0wHgtx-iyN_dz9WOS6rMNFhGLArZp0uum9BRT7Gy2VxSrNLcdQN9WH0_EVWWk0YUWDq4CtZrgvNN2qWPIAD2s4DIN4zrBtWU85Q3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرائتی: مهم‌ترین جلسات هم نباید نماز را به حاشیه ببرد
🔹
رئیس ستاد اقامهٔ نماز کشور در حاشیهٔ اجلاس سراسری نماز: نماز نباید صرفاً در قالب مجموعه‌ای از مطالب و معارف دینی مطرح شود؛ بلکه باید در متن زندگی انسان و مسائل روز جامعه حضور داشته باشد.
🔹
بررسی زندگی بزرگان دین نشان می‌دهد که نماز یک موضوع حاشیه‌ای در زندگی دینی نیست و از محورهای اساسی تربیت و هدایت انسان به‌شمار می‌رود.
🔹
حتی در مهم‌ترین گفت‌وگوهای علمی و اعتقادی نیز نباید نماز مورد غفلت قرار گیرد.
🔹
ممکن است انسان در یک جلسهٔ مهم علمی یا اجتماعی حضور داشته باشد، اما نماز جایگاه ویژهٔ خود را دارد و نباید مسائل دیگر باعث کنارگذاشته‌شدن این فریضه شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/465646" target="_blank">📅 11:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465644">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6_fBb-FqfS-29cjs61BGw9Fv97nXwrIJyZYoxx74dPGq54ysEm9rdPdUFINfyr_DQeYanYxmwVJF8uWpQyvw8G775ggl_vP6PBgJwQ6pWeJZgZvjsxvAfFcZ7pv5iJSnC5I0AyRJoafSEKDiNY6YWF1aOn4QSbmIuHM-XS-cWvnTmgFEHGlF5sWCvtES8WVmTLewK0B2EcjMef7oDJ8e2vOhdk-WBZb2BY3UoXplC9KvkRLTJfPKJSr24ufk6kFq7c6mbxTzjbQ41FMI__7NH_rN-xON3e4wg4sUiY1fNrebIJQhHrNVhwt5lJ7m6cRE72KuIVlJPbiNBK0cojxgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ برای پایین‌آوردن قیمت نفت باز هم دست به ذخایر برد!
🔹
قیمت نفت برنت بامداد امروز به کمتر از ۹۷ دلار ریزش کرد. این ریزش پس‌از آن اتفاق افتاد که آمریکا اعلام کرد ۴۰ میلیون بشکهٔ دیگر از ذخایر راهبردی نفت خود را آزاد خواهد کرد.
🔹
پیش‌تر اعلام‌شده بود که…</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/465644" target="_blank">📅 11:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465643">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RokarQOEPow1l7HnqAj47WiyVCZ74escDm5sQF4ya-1QsfvUbBx-L1Zw1lyNSjxlfvWli46s25x1_jutuvH8nHI0QJebvpEwlpEBAhcExRak-3b91pPN9x_UgKi1NwhcSVv7aLCrmBZ4ZEPRKp-FOoYZyKFflYl1-kX6w9xVip4AqEdJo33HG7wtJmiJiL6Uw1B2tLRN_FtVPzUeB3_-QD6B2E74lxjc6mVZGa99rN5WZ0Y9Ks_n9zUPcLHG3mzDyzvqJVzu9CFMjUwZsbLqlN2cfmbUWaPh4SQuw-QYOzS7wWgYJNAvGgdxBN7pxWRf_1pp4QI-4C9f568WZ_eKxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پکن قید صادرات بنزین را زد
🔹
چین صادرات فرآورده‌های نفتی از جمله بنزین و گازوئیل را تا اطلاع ثانوی به‌حالت تعلیق درآورده است.
🔹
این اقدام در راستای تلاش پکن برای حفظ منابع داخلی و با توجه به کاهش ذخایر سوخت این کشور به پایین‌ترین سطح در بیش‌از یک دههٔ گذشته انجام شده است.
🔹
در همین رابطه، شرکت دولتی پتروچاینا روز گذشته اکثر محموله‌های بنزین و سوخت جت خود را که برای ماه اکتبر برنامه‌ریزی شده بود را لغو کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/465643" target="_blank">📅 11:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465642">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMwby4cd0i9Tep1DqCzVO-GyoUV7ZI31oe8UPzkKWJpJr7ftJ0hMMnjrq8Io_9Nk0pB8JgvCby0a6599exrx6w3PgcxnrSHjh3kB7HznLhUqyR8bl77sBziUi1fMh95XZk9xbILJtlDC3gmf1v3Dx8lAAtKv7Nd1eCQ9VB8yTGMEeWPMaNFZBk4eLOCMIUmVmLEdlb-fchglEIdCthxNtM7KYczg2N9LZ3ceqLE_xp916j2o7a6_Y0PFn2esIFQl2rtv-ZAmUcs4B8booZRkqtZhmXmgRB6dSN-WMNw1uSC58LiOtl3Kc9xoPXnLGxyxnbJq_mPP2qrU_GAf3AyH5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
سیم‌کارت جونیور ایرانسل تجربه‌ای ویژه برای نوجوانان
🔸
سیم‌کارت جونیور ایرانسل، با امکان دسترسی به خدمات آموزشی، فرهنگی و سرگرمی و بسته‌های پرحجم ارتباطی، متناسب با نیازهای کودکان و نوجوانان عرضه شد و خریداران آن می‌توانند در قرعه‌کشی کمک‌هزینه ۹۰۰میلیون تومانی خرید خودرو شرکت کنند.
🔸
پیش‌شماره «۰۹۰۰»، آغازگر پیش‌شماره‌های شبکه تلفن همراه ایران و نماد ورود به نسل نوین ارتباطات و تمایز در تجربه کاربری است.
🔸
خریداران سیم‌کارت ۰۹۰۰ جونیور، نه تنها از این مزیت خاص و نیز بسته‌های اینترنت، مکالمه و پیامک پرحجم بهره‌مند می‌شوند؛ بلکه، به اشتراک‌های رایگان یا تخفیف‌های ویژه در پلتفرم‌های دیجیتال آموزشی و درسی، ورزشی و سرگرمی مانند فرادرس، فیلیمو مدرسه، تام‌لند، مکتب‌خونه، لینگانو، اپتیت، طاقچه، نوار و تیوال+ دسترسی دارند.
🔸
خریداران می‌توانند از اعتبار اسنپ‌پی تا ۱۰۰میلیون تومان و امکان خرید اقساطی سیم‌کارت با استفاده از اعتبار «جیب‌جت» یا اسنپ‌پی استفاده کنند.
👈
جزئیات بیشتر
@irancellnews1</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/465642" target="_blank">📅 11:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465641">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_aBPIZkT_lBDMdcBNFLjYSVuUYAFGi9E2PPYNHyv82hwxYB2EbULOLsvV5Gm1gCUO1puMwGXF0wxWn1U0sKYwEN3APUrNCXeiW7WKgcwtRcef6KHKocidzaBtySw1ls_TTbICz6vtzaD4UFiGEpv5KcbW4WR4Zf7EY2SeUpbj7r8_mulz3Z0drlbRYNRKhDopWLSbmlo509qeaZ8Ttvixorjq57vUmkbsuk1hqGDP_MwSfv7gvrxjvjKYJKC-1acAAZt9o2ufITjC-5NpUxUrLuAF9LFz8Y8Kl0N2pvWs6JUbQe5EiEXg6y0gfNsXYLRxt51zXqFg6dA3wzLhtLXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
نشست فعالان اقتصادی آبادان و خرمشهر با وزیر تعاون، کار و رفاه اجتماعی
دکتر للـه‌گانی: بانک رفاه کارگران بازوی تأمین مالی توسعه استان خوزستان است
🔹️
مدیرعامل بانک رفاه کارگران از آمادگی کامل این بانک برای تزریق نقدینگی و تأمین مالی پروژه‌های کلان تولیدی و زیرساختی در استان خوزستان خبر داد.
🔹️
دکتر اسماعیل للـه‌گانی طی سخنانی در نشست مشترک فعالان اقتصادی شهرستان‌های آبادان و خرمشهر با وزیر تعاون، کار و رفاه اجتماعی که در محل سازمان منطقه آزاد اروند برگزار شد، با اعلام این خبر به سیاست‌های بانک مرکزی مبنی بر تأمین مالی زنجیره‌ای اشاره و تصریح کرد: بانک رفاه کارگران با انتشار اوراق گواهی سپرده خاص برای پروژه‌های توسعه‌ای و سرمایه در گردش واحدهای تولیدی در مناطق آزاد استان و شهرستان‌های پرظرفیت مانند آبادان، خرمشهر و شوش، گام‌های اثربخشی برای تامین مالی بنگاه‌های اقتصادی برداشته است.
🔗
متن کامل خبر
...
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/465641" target="_blank">📅 11:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465640">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/farsna/465640" target="_blank">📅 11:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465639">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بغداد ضرب‌الاجل خلع سلاح را یک سال به‌تعویق انداخت
🔹
دولت عراق مهلت خلع سلاح گروه‌های مسلح را که قرار بود ۳۰ سپتامبر ۲۰۲۶ انجام شود را به ۳۰ ژوئن ۲۰۲۷ موکول کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/465639" target="_blank">📅 11:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465638">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgBv1yns-6cNGkxjC7xqCzFc5JCNFuYHVYf-xDYGKvO4xPsHMUtI5ZNeA13_Um3pmUfXFAMAKpWW0pMU1qXnR7664Ls_Zb9WWg1CG1kIkix2VnV1eZc5mfoe7R00bYuYFy6qS4GuVVvN6-O7eU5UOhKVTuSKqmLpLb88GmmW8KYMS5QKnQ-7s46HgVFTFAFY6vf2baW_QYXB7DXAleZR5uj3m22f65KW48iFaZIjGEhbjLAwziCXGw5wubBiT2nr7gKkWZLSxOMEm0aMD6bMFgdMlbOTBpr1MVH-H-j3jnPCnIhSCvTVHDsRPsnUVCJ_mttbkUhSw8oSQVIYjsF0_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ ایران به ادعای اخراج هیئت ایران از آمریکا: بی‌اساس است
🔹
نمایندگی ایران در سازمان ملل در واکنش به ادعای وبگاه «آکسیوس» مبنی بر اخراج هیئت ایرانی از آمریکا گفت که نمایندگان ایران طبق برنامه قبلی نیویورک را ترک کردند.
🔹
نمایندگی ایران در سازمان ملل با اشاره به گزارش‌های منتشرشده درباره اخراج هیئت ایرانی از نیویورک افزود: «وزارت امور خارجه آمریکا که به هیچ دستاوردی نرسیده است، اکنون به انتشار اخبار بی‌اساس و بی‌ارزش روی آورده است.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/465638" target="_blank">📅 11:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465637">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c74dc1056.mp4?token=jBp_cAi80Jdohi5Qxt-Ho6hKpGodKttXH8wqqZTTvtgyjGhykM3F8k6QSdYCEvhpORjtm682GFMFbh8r2h5JvOV1zcU00p1hRADxnj8vCDJkGh-UCTaR2_eyab4ikmmrFVuXDn4rmoVOWUEvNhMmchtj7djOXkBR2aXJ00QLa7eSNAZV0skac1uBigwx_jgFqkn_Z0P3g8yQtbzBEKiKWb-iJSsAS5cOfRhjAfSGwxUnU-rlLT1nr-hwB7lcOopUONWQj0RpiijjvuRCL0vLUiM6nGe2rX6GjCHhGgj_rUwR03KotP9yZ7WO5dJlHt-HPr-6bILqqONlRSUojuzHzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c74dc1056.mp4?token=jBp_cAi80Jdohi5Qxt-Ho6hKpGodKttXH8wqqZTTvtgyjGhykM3F8k6QSdYCEvhpORjtm682GFMFbh8r2h5JvOV1zcU00p1hRADxnj8vCDJkGh-UCTaR2_eyab4ikmmrFVuXDn4rmoVOWUEvNhMmchtj7djOXkBR2aXJ00QLa7eSNAZV0skac1uBigwx_jgFqkn_Z0P3g8yQtbzBEKiKWb-iJSsAS5cOfRhjAfSGwxUnU-rlLT1nr-hwB7lcOopUONWQj0RpiijjvuRCL0vLUiM6nGe2rX6GjCHhGgj_rUwR03KotP9yZ7WO5dJlHt-HPr-6bILqqONlRSUojuzHzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مادر همسر رهبر انقلاب: آیت‌الله سیدمجتبی خامنه‌ای در خاکسپاری رهبر شهید در حرم امام رضا(ع) حضور داشتند و ایشان در صحت و سلامتی کامل هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/465637" target="_blank">📅 10:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465636">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/707e140333.mp4?token=IeThW-dfkXKkL7DO8G87zJG6Q3eGKEIuGU7wUS1A9XDrTXc27nOMI64AL84LbkPWX84Vcf9cRPCZiZr4Eye6gzcbHYuZ_88pcRzu48VwzByZ7nylglZG6hqH9TiZooabDBqu_MOs5FL-xmgiufbbCG8LT1nOigrLBd6HPuW44zjK54hVaWnyT4HHHfsVcUdVUivyG9DmBVeu12cCa5UfVU7PLpBLBEfuokS_S-cD_bnq003NSxs_yIsZBc11ZOnzgLP8ZGPoWw16FVrLMOeD4srLVJqk0csd5m0Oh2wz-LR7BvgD0oDDxst_P3tH_ADnGTRNkyiSX7IJbd5Ijd2-2R87zuwHMDZqYGGwa69Zo8HY7obKle25zIEd001uY8OEwmiWHpX47ZzeRcVV1rQaSUjzzkr5K1OVWrQn2LSRNT5VxG5eAl2PZmPwHMm8ijW-glcPOaSvk_HdoxQoh5R2cKEdWM9y3eU9EAaFtGIztE5cKR8lXa1xmg-fuRzaWalNLtotJUyMXEHluLxK25766hsKVxjcCXSmMaTMkcL-H687z-etalF2BD8sApVXl_8ES8L3H3F8616-_03oNl0eR60zL_TR_Aw6u30fCEDE5kdu2Sedro652BICvIryxETEeF6DIhfJipvAe0nNw9k-EiM-iDZ-ym2lx_K1pUI7Wco" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/707e140333.mp4?token=IeThW-dfkXKkL7DO8G87zJG6Q3eGKEIuGU7wUS1A9XDrTXc27nOMI64AL84LbkPWX84Vcf9cRPCZiZr4Eye6gzcbHYuZ_88pcRzu48VwzByZ7nylglZG6hqH9TiZooabDBqu_MOs5FL-xmgiufbbCG8LT1nOigrLBd6HPuW44zjK54hVaWnyT4HHHfsVcUdVUivyG9DmBVeu12cCa5UfVU7PLpBLBEfuokS_S-cD_bnq003NSxs_yIsZBc11ZOnzgLP8ZGPoWw16FVrLMOeD4srLVJqk0csd5m0Oh2wz-LR7BvgD0oDDxst_P3tH_ADnGTRNkyiSX7IJbd5Ijd2-2R87zuwHMDZqYGGwa69Zo8HY7obKle25zIEd001uY8OEwmiWHpX47ZzeRcVV1rQaSUjzzkr5K1OVWrQn2LSRNT5VxG5eAl2PZmPwHMm8ijW-glcPOaSvk_HdoxQoh5R2cKEdWM9y3eU9EAaFtGIztE5cKR8lXa1xmg-fuRzaWalNLtotJUyMXEHluLxK25766hsKVxjcCXSmMaTMkcL-H687z-etalF2BD8sApVXl_8ES8L3H3F8616-_03oNl0eR60zL_TR_Aw6u30fCEDE5kdu2Sedro652BICvIryxETEeF6DIhfJipvAe0nNw9k-EiM-iDZ-ym2lx_K1pUI7Wco" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منظور: اقتصاد جنگی به فرمانده واحد نیاز دارد
🔹
رئیس سابق سازمان برنامه‌وبودجه: اقتصاد کشور در این شرایط به «وحدت فرماندهی» نیاز دارد و باید تصمیم‌گیری‌ها متمرکز و اجرای سیاست‌ها با اعطای اختیار بیشتر به وزرا و استانداران انجام شود.
🔹
شورای اقتصاد کشور هم…</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/465636" target="_blank">📅 10:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465633">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qaaqXg-dEpj8GbqGws2ZW0wQPoX2t8iYWo7U1smVPpjI5se5OqTdFPg3_Ct1ZXR9cAw8EdvYa0x8qEMTOUNLoYH4eS24oPmQPkT7aLNsDe7O-vTMwOHWES4FX49jyaMi3WlZaChJlMSPdVZTrc5eTaH2yyDvx7CHrA6Fxe91wEt3_VcRwRw98VdrjsU8F9iO3demTlkvpF_nGJcG1HDgSCRvv8O4G7dYO8qfV6e3GYQZjdn2sVN-D98wGKdkaXM_huwrHB8r_p3tSv5zeKjKTad9_ygGi4b1Az6o4TYBEiIVLPKO5u2FwFeD8qxlfilT33PKSxX9pqKtRcioddNLYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/URnfSVEq2dyhD7y9GycMVJeSPQOVZMQzFt0jY_r0ub8o_WcnVVs3WLl2DczofjR11UvbIPEbPG_u2-mT_uE66LPQOjH2LyG8mruKzBcGdWKq-Pwv6V5LL6wcVVkCcB4gncxit62h12qrRDn2olbOHCzDpn93M5juH6tCtuhDPsZsrWE_vsSdnMdHL7GoO6fhpuEHBLzG4kZhANNixVo_fdtEAPNgyX6bMu509qX3FcPpAjv_6iVLW2na-9NCWaBkxfEp0g82ifce7hxnUEo29btayVjcHTAj1kvhyYeuw8RGnw9jxejj00q_y5fmltLEvdCxsV0xcBGm4KELSuiIUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bqy5jlGoCBPkzezPbIfzkABz3Zj8KYPVSaCxVNHm-RjLnODtyfZlEeRQp28sMF9Nujte_gnLYPOY5Mn9en0joGirptpWhTFye_IDjd8xV5YPPOlzX-hbx3_mUK0O9UvZEy8CBLeBpbt_gcPwmilKg7gkU7aExkZtbOIYhaSpWDcxqR7uS3XzVVdUw3rrs8NPtBYRt5-rfafjrGWnZDVU1VnQE6ofO4bty7iIwtKDWSJbgyCRfSV1JF_39RrlIR53gHsd_uWEmn-Zz7nygV04LFazCK-_SoLYybAdwKRtIsDdTfSeJHRWSJPL7NK2hunfJ924xN1s9WdqjvCnfgXwLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تقدیم هدایای متبرک رهبر انقلاب به خانوادهٔ شهید نصرالله و شهید موسوی
🔹
جمعی از فعالان جبههٔ فرهنگی انقلاب اسلامی در جریان سفر به لبنان، با خانوادهٔ شهید سیدعباس موسوی و شهید سیدحسن نصرالله دیدار کردند.
🔹
در این دیدار، چفیه و انگشتر متبرک رهبر معظم انقلاب اسلامی، حضرت آیت‌الله سیدمجتبی خامنه‌ای، به خانوادهٔ شهدا اهدا شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/465633" target="_blank">📅 10:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465632">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سپاه: اخراج آمریکایی‌ها از عراق، طلیعهٔ آزادی غرب آسیا از یوغ سلطه شیطان بزرگ است
🔹
بیانیهٔ سپاه به‌مناسب خروج کامل آمریکا از عراق: سپاه پاسداران انقلاب اسلامی با گرامی‌داشت یاد شهدای سرافراز جبهه مقاومت اسلامی عراق و منطقه غرب آسیا، به‌ویژه سردار سپهبد شهید حاج قاسم سلیمانی و شهید ابومهدی المهندس، و همه مجاهدان مؤمنی که در دو دهه رویارویی با متجاوزان آمریکایی به فیض شهادت رسیدند، این پیروزی تاریخی را به ملت غیرتمند عراق، جبهه یکپارچه مقاومت اسلامی و مجاهدان انقلابی جهان اسلام تبریک می‌گوید.
🔹
اخراج آمریکا از عراق، نتیجه پایمردی ملت غیرتمند این کشور بر استقلال خویش بود. ملت عراق با ایستادگی تاریخی خود ثابت کرد که اراده ملی، برترین سلاح در برابر زیاده‌خواهی سلطه‌گران است. غلبه اراده مقاومت ضدسلطه عراق سربلند بر اشغالگری آمریکایی، برگ زرینی در تاریخ آزادی‌خواهی ملت‌های منطقه است.
🔹
اخراج اشغالگران آمریکایی، در حقیقت تحمیل عزم راسخ عراق قهرمان بر رژیم تروریست و جنگ‌افروز آمریکا و حاکمان بی‌خرد کاخ سفید است. آمریکا که همواره با زبان زور سخن گفته، امروز ناچار به عقب‌نشینی از سرزمینی شده که دو دهه آن را اشغال کرده بود.
🔹
آمریکا رفت؛ نه با مذاکره، نه با منت؛ بلکه با همت ملتی که ایستاد، با خون مجاهدانی که جان دادند و با اراده مقاومتی که هرگز شکسته نشد. اینک عراق، سربلند و آزاد، بر ویرانه‌های اشغال بیست‌ساله ایستاده و طلوع استقلال را نظاره‌گر است.
🔹
بی تردید این رخداد مبارک و تاریخی نخستین گام در خونخواهی شهیدان عراق علی‌الخصوص ابومهدی المهندس است و به فضل الهی انتقام خون این عزیزان با اخراج کامل آمریکا از منطقه تکمیل خواهد شد.
🔹
آمریکا باید از منطقه برود و مدیریت امنیت را به خود ملت‌ها بسپارد. تجربه دو دهه اشغالگری نشان داد حضور آمریکا نه‌تنها امنیتی به ارمغان نیاورد، بلکه خود منشأ ناامنی، تروریسم و بی‌ثباتی در غرب آسیا بود.
🔹
آمریکا پس از بیست سال مداخله نظامی، با حدود پنج هزار کشته به اذعان خودش و البته نه آمار واقعی و چهار هزار میلیارد دلار هزینه، در اوج نفرت و کینه مردم عراق اخراج شد. این ارقام، گویای شکست سنگین و رسوایی‌بار آمریکاست.
🔹
خروج نیروهای آمریکایی از عراق، رویدادی بزرگ و معنادار تاریخی و دستاوردی سترگ برای محور مقاومت است. شکی نیست که مردم غیرتمند عراق با ادامه این نهضت مقدس، به مداخله آمریکا در اقتصاد و نفت کشورشان نیز پایان خواهند داد و با وحدت و اراده ملی، آینده‌ای روشن برای خود رقم خواهند زد.
🔹
آمریکا هیچ‌گاه تکیه‌گاه قابل اعتمادی نبوده و نیست ؛حقایق و واقعیت‌های میدانی تصریح می‌کند آمریکا رفتنی است و این ملت‌ها هستند که باید کشورهایشان را بسازند.
🔹
با قاطعیت می توان گفت اخراج آمریکا از عراق، طلیعه اخراج آنان از سراسر غرب آسیا و جغرافیای امت اسلامی است.
🔹
این پیروزی بزرگ، محصول اراده ملی عراق، مجاهدت جریان‌های مقاومتی، حمایت مردمی و اقدامات مؤثر دولت این کشور است.
🔹
سپاه پاسداران انقلاب اسلامی در پایان با تاکید بر ضرورت هوشمندی و هوشیاری دولت ملت و نیروهای مقاومت عراق قهرمان در برابر توطئه‌ها و فتنه‌های محتمل طراحی شده توسط امریکا و دشمنان این کشور برای ایجاد ناامنی و بی‌ثباتی مجدد در این سرزمین مقدس، به عنوان فرزندان ملت ایران، قاطعانه اعلام می‌کند همچنان در کنار ملت‌های حق‌طلب و ظلم‌ستیز منطقه برای پاکسازی غرب آسیا از لوث بقایای پلید متجاوزان آمریکایی و نیز رژیم کودک‌کش و نژادپرست صهیونیستی ایستاده است و تا آزادی کامل قدس شریف از پای نخواهد نشست.
@Farsna</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/465632" target="_blank">📅 10:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465631">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یک تیم تروریستی در زاهدان منهدم شد
🔹
روابط عمومی قرارگاه قدس نیروی زمینی سپاه: یک تیم تروریستی که قصد اجرای عملیات تروریستی در منطقهٔ منزل‌آب را داشت شناسایی و مورد ضربهٔ قرار گرفت.
🔹
تاکنون تعدادی از تروریست‌ها به‌هلاکت رسیده‌اند و عملیات پاکسازی همچنان ادامه…</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/465631" target="_blank">📅 10:28 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465630">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یک تیم تروریستی در زاهدان منهدم شد
🔹
روابط عمومی قرارگاه قدس نیروی زمینی سپاه: یک تیم تروریستی که قصد اجرای عملیات تروریستی در منطقهٔ منزل‌آب را داشت شناسایی و مورد ضربهٔ قرار گرفت.
🔹
تاکنون تعدادی از تروریست‌ها به‌هلاکت رسیده‌اند و عملیات پاکسازی همچنان ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/465630" target="_blank">📅 10:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465629">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hn7q8GsED7N2JbCpY8fQQ8V2IH1s0edGexCx7160Udc2xBz96H362BP8y5M5bUkANzTvkVDSzEBfSB8VuxizxMfqjp-RFo0Gn4dfIv1EUEw6H5SW8gJZhXcQ7XqLcZPUlUZMLPODxt9GBkYn1obA6P5a22s7usm5iQlNDQwEQiHrRdfmwxzLKiBFhJi77vp2Xh3wr0PhqiOFwB-AYdfImeyfs335jO0Qhqmj-xvcXeb2KQDrGlWyowbLI11uxc0pkc-G6ma2T7A2f7lRIbXr2p-Yc4Z9vzlFeFtjS_rWUUz89zRJaCNPSwxCERlNMVFRIdJKtkMFyo_6VmOgQdX5UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائب: هوشیاری و همدلی همگان بیش‌از گذشته ضرورت دارد
🔹
پیام رئیس سازمان بسیج به‌مناسبت فرارسیدن هفتهٔ انتظامی: هفته انتظامی، فرصتی برای پاسداشت مجاهدت‌ها و تلاش‌های خالصانه مردان و زنان غیوری است که در مسیر تأمین امنیت، آرامش و آسایش مردم، مسئولیت سنگین حراست از نظم عمومی و صیانت از امنیت جامعه را بر دوش دارند.
🔹
فرماندهی انتظامی جمهوری اسلامی ایران با توان رزم و دفاع نیروهای جهادی و مخلص در طول سال‌های پس از پیروزی انقلاب اسلامی، با حضور مسئولانه و فداکارانه در میدان‌های مختلف، از مقابله با تهدیدات و ناامنی‌ها تا خدمت‌رسانی به مردم، نقش مؤثری در تحکیم امنیت کشور به ویژه مرزهای کشور عزیزمان ایفا کرده  و نیز با نثار جان خود، برگ‌های درخشانی از ایثار و فداکاری را در تاریخ پرافتخار ایران اسلامی به یادگار گذاشته‌اند.
🔹
امروز که دشمنان ملت ایران با بهره‌گیری از شیوه‌های نوین جنگ ترکیبی، امنیت، وحدت و انسجام اجتماعی کشور را هدف قرار داده‌اند، هوشیاری، همدلی و هم‌افزایی همه دستگاه‌های مسئول و آحاد مردم، بیش از گذشته ضرورت دارد. بی‌تردید تداوم امنیت پایدار، در گرو حضور مقتدرانه نیروهای انتظامی در کنار مردم و تقویت پیوند میان جامعه و حافظان امنیت و حمایت از مدافعین امنیت می باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/465629" target="_blank">📅 10:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465628">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">انهدام یک شبکهٔ قاچاق دارو‌های کمیاب
🔹
دادستان تهران: اعضای یک شبکه قاچاق دارو که از طریق خارج‌کردن دارو از شبکه توزیع، اقدام به قاچاق آن به یکی از کشور‌های همسایه می‌کردند، دستگیر شدند.
🔹
در این پرونده تاکنون ۴ متهم شناسایی و تفهیم اتهام شده‌اند و متهم ردیف اول این پرونده یک خانم از اتباع یکی از کشور‌های همسایه است که مقادیری داروی قاچاق و خارج از شبکه از وی کشف شده و تحقیقات از افراد مرتبط با وی ادامه دارد.
🔹
مشارالی‌ها با اشخاص متعددی در ارتباط بوده و یکی از شگرد‌های آنان برای خرید دارو‌های خاص ضد سرطان، خرید کارت ملی اشخاص و هماهنگی با پزشکان، جهت اخذ نسخه بود.
🔹
وی همچنین با یک داروخانه که اقلام دارویی را خارج از شبکه و به صورت عمده می‌فروخت، مرتبط بود.
🔹
متهمان پرونده دارو‌های خارج از شبکه را از طریق یک باربری به یکی از شهرستان‌های مرزی و از آنجا به یکی از کشور‌های همسایه قاچاق می‌کردند.
🔹
از باربری مرتبط با این شبکه مقادیر زیادی دارو به ارزش ۳۶۰ میلیارد ریال کشف و مالک باربری دستگیر و جهت تحقیقات در اختیار ضابط قضایی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/465628" target="_blank">📅 10:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465627">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpZNF8u2E4ge2DVkckh7oyUW-gQCxS1qM-hcFFaYUpz-VgnYtQOY6llb3RyNxI8dToltUo_Y5juIh6JxoQSYVAfzZZHt269kj8uL865UOhYL3uW5RiRwv8F5Vngav1SxiY6gu9wxAWQS4S0uxiDLaypIxDhzquyeu5klZSmDw0wa6gSdDCpR3fkoOkWpS3KU0D1IS1KN_uhJ1MCti6wDfOuEkWOdLY4inzWPE7lxqA5zj3gI-Iwkao9dLdzIlfqNqyB5gnrFzpU48FZJy0BEVPAHDvqMxS0sSrH-R1OLx7-_hwAXqOiFRipAEBeSROyY0BlcMqBWT2RbHm_1NlqHOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی‌های آسیایی ناگویا
🏐
کامبک ایران امید اندونزی به صعود را ناامید کرد  تیم ملی والیبال ایران، ۳ بر ۲ اندونزی را شکست داد.  صعود ایران قطعی بود اما اندونزی برای گرفتن جای تایلند در رتبۀ دوم گروه و صعود، به امتیاز این رقابت نیاز داشت.
🇮🇷
۲۲ | ۲۱ | ۲۵ | ۲۵|…</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/465627" target="_blank">📅 09:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465626">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c994da169a.mp4?token=upbQkwdxn-1vfX5LHmSbkBKnBJ7Xv7dnnaSgecSCftH8GXmsc2WuCg3PdlTWyn-ZA2gneePQxnkjboelTfD1HAb46PlzCfBTJP1QBtTLIc2tmIci8Irsiki6UAS1j73LZkuQor099MJzm17L55PmcPnqmgj6ZBafWZZ3bSaXD2bRVEEWK0VdKk8Fyu5WmUFH7iGLut88GkbTlma3gKFynZOmOTdtdTlREPbfyOeclarpO6rX585Xl7OCJCbL-s10BII2WIGzN8HxDVQRS0PxK0zm1JmFZgxDHLodUZuhitygK8X6xh4moVlD_WgtwaGkDtiC3D3CCMbFjq2CbeZwBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c994da169a.mp4?token=upbQkwdxn-1vfX5LHmSbkBKnBJ7Xv7dnnaSgecSCftH8GXmsc2WuCg3PdlTWyn-ZA2gneePQxnkjboelTfD1HAb46PlzCfBTJP1QBtTLIc2tmIci8Irsiki6UAS1j73LZkuQor099MJzm17L55PmcPnqmgj6ZBafWZZ3bSaXD2bRVEEWK0VdKk8Fyu5WmUFH7iGLut88GkbTlma3gKFynZOmOTdtdTlREPbfyOeclarpO6rX585Xl7OCJCbL-s10BII2WIGzN8HxDVQRS0PxK0zm1JmFZgxDHLodUZuhitygK8X6xh4moVlD_WgtwaGkDtiC3D3CCMbFjq2CbeZwBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تهران با تورم صفر به استقبال گرانی رفت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/465626" target="_blank">📅 09:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465625">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd9f4785c.mp4?token=GYO8KXGaI7192ukAZlPMeREfNuohPZyqLtqcMQrY2zYDESrCT1S0dW0DA3nLKm2yEhfYC7Gic_PNIEOVv6EXlAz5Vr04GZHRwmDzv_qVDxT0D3KAhjTZReQRQeA8DlRVYHKq52d6L84dEQzMvAU5uLl_1wW6hw-mkrlzCGXu8bQkfRM_B0WIFQI9ofA9ZIibew0Gp0eupO0nUKro-RyCpD0qbnY0NYXvvPnR1j5oCRcL3Ua8pwSmaggRtvp2fXilh6mBO21N6HyAxhPlWBwUNdFviEzadVUaiJLOPzFpU5R5gEb8cw3lWuTEU3lqU0MAqqJn4H_NO6tdZVnRvaKmcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd9f4785c.mp4?token=GYO8KXGaI7192ukAZlPMeREfNuohPZyqLtqcMQrY2zYDESrCT1S0dW0DA3nLKm2yEhfYC7Gic_PNIEOVv6EXlAz5Vr04GZHRwmDzv_qVDxT0D3KAhjTZReQRQeA8DlRVYHKq52d6L84dEQzMvAU5uLl_1wW6hw-mkrlzCGXu8bQkfRM_B0WIFQI9ofA9ZIibew0Gp0eupO0nUKro-RyCpD0qbnY0NYXvvPnR1j5oCRcL3Ua8pwSmaggRtvp2fXilh6mBO21N6HyAxhPlWBwUNdFviEzadVUaiJLOPzFpU5R5gEb8cw3lWuTEU3lqU0MAqqJn4H_NO6tdZVnRvaKmcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رزمایش جان‌فدایان با حضور پرشور مردم زنجان آغاز شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/465625" target="_blank">📅 09:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465624">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isfC4gGpq_GsnblWRmpnBfl-eCtG51FLrKIZlNhCiYStThCAR5dJfuXBMoPy5LurtW7ic7If9LrGUcHrssH1Qbhlz5KWflYeoXs6uRoEhzhF65dZjpPxT7CIku1q9UnNclJ6bbKr2bdKyWFdHK-3JdE0361dtRoaB743vHG_r2GJy4h7m2gKTggISCFPR6P5eY9wlhr4nxk2Eg8IvfOphe_OiDGmNZhESNgu9Z_Hn2xvYxkQdIX5I0SaR9vIhQ96sBoNMdlDdAsuDPpZm7-oDwtC0qIubO6wkHBcGwvZBOOl5jXuqXYib5WLnR-bj9rjDAwQkZNiPdh4PSpQ974sfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصلاح‌طلبان بیش‌تر از ترامپ نگران بسته‌بودن تنگۀ هرمز
🔹
خلاصۀ یک‌خطی نتیجه ۹ ماه جنگ ازاین‌قرار است: تنگۀ هرمز بسته شده، قیمت نفت زیاد شده، فشار به آمریکایی‌ها بالا رفته و ترامپ شکست خورده است.
🔹
تمام تلاش‌های آمریکا از فردای جنگ تاکنون، به‌جای براندازی در…</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/465624" target="_blank">📅 09:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465622">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K801MzYMj6Z4p1ufYyPUuvcMga0JXlPMCAAr1j8jTVIZQqyVXG_Iysl3GZdQ7vdz_iAycaJ5DDGkclCVGZ7RsHJLbXoxdNOCNEvFe4wmKjHCbJDH4F4B9LjvHJ-vPwbYc_ZQUWFVp_8cgfny1AI1qGLRA3Pz9v3JuEfBUAoJG0gfAvhH2PpIEupEUmuUpYYACQv1M6l4uaztzwZa-RTalser0cXY7s61v7PQ_ql-e-dNHdgbWXYqetllaymNap9cP8YNDabeUcdRFpJTUzzlrEDlRR9mFgZRc2lkfvTvIL4eklG7ve9P0sczzjlKeMG51hw-CgecJAS-ocnstFO5QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار جنجالی درباره کی‌یف: «شهر را ترک کنید»
🔹
اولگ سوسکین، مشاور سابق رئیس‌جمهور اسبق اوکراین، با هشدار درباره تضعیف شدید پدافند هوایی کی‌یف، از ساکنان پایتخت این کشور خواست هرچه سریع‌تر شهر را ترک کنند.
🔹
به گزارش ریانووستی، سوسکین در برنامه‌ای در کانال یوتیوب خود گفت: «دیگر کار تمام است؛ کی‌یف محکوم به نابودی است. دفاعی که قرار بود طی این سال‌ها برای شهر ایجاد شود، کاملاً از بین رفته است. همه‌چیز را غارت کرده‌اند و دیگر پولی برای پدافند هوایی وجود ندارد.»
🔹
وی با اشاره به آنچه «بی‌کفایتی زلنسکی» خواند، وضعیت کی‌یف را بسیار نگران‌کننده توصیف کرد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/465622" target="_blank">📅 08:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465621">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">‎⁨پیام_رهبر_انقلاب_اسلامی_به_سی‌وسومین_اجلاس_سراسری_نماز⁩.pdf</div>
  <div class="tg-doc-extra">527 KB</div>
</div>
<a href="https://t.me/farsna/465621" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎥
قرائت پیام رهبر انقلاب به اجلاس سراسری نماز در حرم رضوی  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/465621" target="_blank">📅 08:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465620">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eee080bf40.mp4?token=V7RCTObGtYHi48eg2hh5eHQ3mYSXylEDNni2g22bWwFNfheo-rSqRA75bOyM2QA8YusMysZJa22L5qMaHhMhexhVN0x7tdnFdX-RElJYh-mi-zrsepw0WfMH0Q0mWBisZWNvxXlL0kIfNb5OoqqybKe7NRod7avUL_Qi1i-uHT7Ehg-FqrAOysgjYTtxaW3mMHJs--nm50zv7QiqX2pCJhO-TvGX8oEXvu1OxlztPwtoLItwr-TSR60lwJVazokUtZ6gizxJr6Jni_WGM2wuZSoxwlzoPeNQEF5VbA8NtZDAyuwqnD-sjaYjyMHmdURflp7Pb8W84YUes59yU9_7Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eee080bf40.mp4?token=V7RCTObGtYHi48eg2hh5eHQ3mYSXylEDNni2g22bWwFNfheo-rSqRA75bOyM2QA8YusMysZJa22L5qMaHhMhexhVN0x7tdnFdX-RElJYh-mi-zrsepw0WfMH0Q0mWBisZWNvxXlL0kIfNb5OoqqybKe7NRod7avUL_Qi1i-uHT7Ehg-FqrAOysgjYTtxaW3mMHJs--nm50zv7QiqX2pCJhO-TvGX8oEXvu1OxlztPwtoLItwr-TSR60lwJVazokUtZ6gizxJr6Jni_WGM2wuZSoxwlzoPeNQEF5VbA8NtZDAyuwqnD-sjaYjyMHmdURflp7Pb8W84YUes59yU9_7Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رهبر انقلاب: رهبر شهید اهتمام ویژه به امر والای اقامهٔ نماز داشتند
🔹
توجّه به امر والای «اقامهٔ نماز» و به‌صورت خاص برگزاری اجلاس نماز، از جمله اقدامات ضروری و بایسته‌ای است که از ابتدای دههٔ هفتاد در کشور به همّت عالِم مجاهد و مردمی، استاد قرآن و مبلّغ زبردست…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/465620" target="_blank">📅 08:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465619">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">رهبر انقلاب: نهادینه و همگانی‌شدن نماز در جامعه، زمینه‌ساز رسیدن جامعهٔ اسلامی است
🔹
اقامهٔ نماز در همهٔ مراحل تکمیلی و سطوح تکاملی‌اش در پهنهٔ جامعه و کشوری که پرچم اسلام ناب محمّدی صلّی‌الله‌علیه‌و‌آله‌وسلّم را برافراشته و به حاکمیّت اسلام مفتخر شده، در…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/465619" target="_blank">📅 08:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465615">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oys-UOn5Hv33VIi5V60uwikzdV16J9DLpfqcpPBu06slr_CkocuL7wDkv-oJl7dModuAJPaO5GysVCYYR8YjIuRGo5eoxAddgij-fb_5YUdPWgTHcx6wGKaQwJDh-Fvtw7sU56uzIRzmiwUb0JdRbeB83YeUazFgQwMXKFOrYuOc3gY4Iuz2-6_z3J5P3phsCL1KgFcvfV_4F71FpXaAVsg8kslcZ3J1LZQdrdgNYV5s8FFfz7by75c3nr7TQfsDEXGk3Cx3GhGhrwxTvCY_yMYdr42Ffmx5PSMI4pXzH-1IjfUqbVicn7kyDkrNVYKGTXQQhIwtLOMxVvOb1whPuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر انقلاب: اقامه نماز در جامعه زمینه‌ساز رسیدن به جامعه و تمدن اسلامی است
🔹
اقامهٔ نماز در همهٔ مراحل تکمیلی و سطوح تکاملی‌اش... برای فراهم شدن زمینهٔ طیّ طریق از مرحلهٔ نهضت و انقلاب اسلامی تا مرحلهٔ جامعهٔ اسلامی، امری ضروری است و بعد از آن است که نِیل…</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/465615" target="_blank">📅 08:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465614">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0MEJpQcndAPujWWy6I3W_KfYQPB1lczokZsDiSB65-QRRN-dwZ6uPbNZh1LBAo_g8ZrYbrt4cQBoTPqJWzx342AWDn4P8JXWcDRnd8mQcQp_xeiTtnAvNFHx5ec5QVCVd7dWom8dj_YYPCg33lFUe39iHA3A64nVyveR6WvHG5xRVSOvkoZIO8KjvxkdZ9Z_IZTnOS-R5tFkuytKUpkxmUSBoJDYvtzOxfrfcXLPL3qOnldpUxwbJ8cSKv2Cs4uG95Sf1DnQd1IIiLkI7K9_5TNFYua0Ze3UWlvuBxq3al3syjgUD2c_lAi8taxEd72lGGLpgjS8BMAgRGjV2TXNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر انقلاب: اقامهٔ نماز اولین ثمره و نشانهٔ حکومت صالحان است و در جهاد و فتح ظفر نقش دارد
🔹
فریضهٔ نماز، تنها یک تکلیف فردی نیست و بنا بر آموزهٔ قرآن، برپاداشتن نماز، اوّلین ثمره و نشانهٔ حکومت صالحان است که «اَلّذینَ اِنْ مَکَّنّاهُم فی الأرضِ اَقاموا الصَّلاة».…</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/465614" target="_blank">📅 08:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465613">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7zTsHopjGDTAe8DK8wyl50NjgCt-pwb0zPvSEejAbOCBWLzHSYVv2WLB3XPYg3ZDkElgXTcak8TEyEt3UKAWGsIQ0lBtYWtlA5e9-bw5sOYlSfqa4RhAno2ijJsbj92RDzx8s2lmFwtiTZKfMhqo0moVz6Yz2VhI8WydHIlS8i9Ya_GGt0PJOdH6dqCMB0-AKgHBaAKuhnvcJsZ8kz4XaZyMvpmuAzGHidji9BIv4_AaqjOiBbTtst3wYVb5Hxk6tTVNuglN8xjoDj2UDIFxXx4SC5QQOotYqzlygucpjKRoQSEmoc0vXO7Cbv95sB6aguHkMdDk2sRMqEsWwj0-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر انقلاب: نماز تکیه‌گاه مستحکم امید و اعتماد به خدا است
🔹
اقامهٔ نماز به‌عنوان تکیه‌گاه مستحکم ذکر خدا و امید و اعتماد به او، نقش ویژه‌ای در جهاد و فتح و ظفر در میدان‌های مبارزه خصوصاً میدان مبارزه‌ای که امروز پیش روی ملّت ایران است، دارد. @Farsna</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/465613" target="_blank">📅 08:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465612">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CinEN15stRjDzMC2NgW1_rs6McIlH57OcDKauUa8X1EdDzIekfYJ7XMzD6WD4mwkeOtCgkrrVtsldOIrhJZ2H1jWw3uWBvqyeClnMyKJ22e6lAaFiDS2TGwbZB5v0RpHwTd6H8rsNnilytmdyHVX2AMaGRdZDUJa1eYnrs30leCuDzcFRI6YYaf-Y73l0wnVCxQuvcvnqLO4n-gX-dWYMczl6OZJA5XD7EHLks1-DKRYQ7Kuscfc2pS5tUDNoPvDW9Q25xsaiJA9KREI1p9s5B_l4vUntH5_RGNB4DKwNi15aI0a5sZMXjzxpE1CHphhpsJ_0l1L4o1ebTjfw8gHcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر انقلاب: نماز رکن حیات طیبه و پشتوانهٔ مستحکم مبارزه با شیاطین است
🔹
بخشی از پیام رهبر انقلاب اسلامی به سی‌وسومین اجلاس سراسری نماز: نماز از جمله زیباترین نعمت‌های بزرگ حضرت حق جلّ‌وعلا، برترین نهاد و نماد و ستون دین، رشتهٔ اتّصال هر یک از ما برای ارتباط…</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/465612" target="_blank">📅 08:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465611">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m93Vs3Umid7aSkenq2okkLhTvuM5iAz_NmJyImKnS-AjJVxzKb-FOknO0bLPX9a2_61tGkxu7uW4FFFmzVEpmQg241TjayHgAWHXsMzoLf88AvTuFoCS5eBcDqpyr_qaUogV80FRV1tps12wSJP7h7VyDohfMMVfTSquAn5EjPx6mKdppEt-a9TXs192boJUXCCCQbTJUrDDsFEsIcd1uBi0b5RbDPtdFGL4_Zw5XFTi_b94GJTyqedC8u-IcrZ8LA98Ygdanq4eNBxGocFhPgOpUyr29aUywLCRI5uPUs1mGD71o0RAO3Qt3aJSCMoB2oIxJaBCOOYC-7u_sP90Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام رهبر انقلاب به سی‌وسومین اجلاس سراسری نماز، صبح فردا همزمان با قرائت در محل برگزاری این اجلاس در حرم مطهر رضوی، منتشر خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/465611" target="_blank">📅 08:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465610">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEzPeeaMk1fRml6EniaaUkA4GJjLQbwQUyVV46_RgAl9SIRav4gMvB6lQdhvsipGJMfX7sbZOiQxGMSzdX5s2VQcp0IstPMT2ObQs_PlQKFPvMYas7x-OLr1ICYqm-6RkiQ32R4TWP3sQklPCdtmfKZwDHsEBS5vv2OVO-soYL_73MQunyi8OYBMhDhKbc4DZaEloiqFMCX0iD784k0dHrm1v0dJL7UVDabhdPjvCXTXsMcMkx7EX7fT9GocR5bF4vh99Ddv5JZz5EtPgyVxLo-ep60YsNYvXTgT3zhUj6cAb4EfiEZiEK_ZT5l04dhGbRkCcCMow5-P4yCeWtJeBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی: ایستگاه میدان شهرری خط ۶ مترو هفتۀ آینده تست گرم می‌شود.
🔹
حدود دو هفته پس از تست گرم نیز این ایستگاه افتتاح و به بهره‌برداری می‌رسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/465610" target="_blank">📅 08:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465608">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6a9c266f.mp4?token=eB1oLlH6J4E5k1USFr8eDkKXJg3QttgIvuIgUpJMr9yGPpoyLw6LTUKJH9Y-8pzcyLzMswA0g9iQGGZ9UCFT8CdKR5SyaFjhXdKPViNswBqDUORZOPpun7s2ggTsEYMKIFZMWvwEPrZPud2hWmWUFuyr4BfR9VUGbXAciOKc0RDVOjF7XctVtEmEanwCkElyfCsgGPozrN578y60A3SD80JXz2AJtcOYzUTeOt4k-fhbMXaBooTXo0r4tYs2yuUMLxG8fVS4iaJoAtLm4kygB19yCaHFkJZzSTW7m9q2F2MJBsJm_YMYTJ9-l7Q_57LxpmJW4M62Xx7QDAIsQvn3WkycflI8w9vJEH9sbaQh7xdKr0IEk8ww-KSalM8Gl6My3rPvjvmh6l-Ou5ZKUWJqwY5zQIZfLT6871dEU3v_hvnxjydJqGwigTvGJnqVVV0j9cQr3AqrmT9Ca0qhIeivQEzRCDlz5ZVfJl2H3_1Em-WQNB7yE9b_WFST8T1szoK8-etn7TvP0T2DvdToJPOzSYn1cFMh4ad6OJvqlwumTJigF2snnz7FygCTAkcJxqlpTEXROOO7_U3LA4CLwd0ntQZ5D1iAY1vFSWL_2EX6zEyeDnW5KlnX5498V0IteI7JBdNppvjtIvANgxbpQ9-_pnGEclUzyXpT4fujOYKfCwo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6a9c266f.mp4?token=eB1oLlH6J4E5k1USFr8eDkKXJg3QttgIvuIgUpJMr9yGPpoyLw6LTUKJH9Y-8pzcyLzMswA0g9iQGGZ9UCFT8CdKR5SyaFjhXdKPViNswBqDUORZOPpun7s2ggTsEYMKIFZMWvwEPrZPud2hWmWUFuyr4BfR9VUGbXAciOKc0RDVOjF7XctVtEmEanwCkElyfCsgGPozrN578y60A3SD80JXz2AJtcOYzUTeOt4k-fhbMXaBooTXo0r4tYs2yuUMLxG8fVS4iaJoAtLm4kygB19yCaHFkJZzSTW7m9q2F2MJBsJm_YMYTJ9-l7Q_57LxpmJW4M62Xx7QDAIsQvn3WkycflI8w9vJEH9sbaQh7xdKr0IEk8ww-KSalM8Gl6My3rPvjvmh6l-Ou5ZKUWJqwY5zQIZfLT6871dEU3v_hvnxjydJqGwigTvGJnqVVV0j9cQr3AqrmT9Ca0qhIeivQEzRCDlz5ZVfJl2H3_1Em-WQNB7yE9b_WFST8T1szoK8-etn7TvP0T2DvdToJPOzSYn1cFMh4ad6OJvqlwumTJigF2snnz7FygCTAkcJxqlpTEXROOO7_U3LA4CLwd0ntQZ5D1iAY1vFSWL_2EX6zEyeDnW5KlnX5498V0IteI7JBdNppvjtIvANgxbpQ9-_pnGEclUzyXpT4fujOYKfCwo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز همایش ۵۰ هزار جان‌فدای ایران در کرمانشاه
@Farsna</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/465608" target="_blank">📅 07:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465607">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار لرستان</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c921d0c509.mp4?token=K_nupvrLjLLcthNMFFywrISDJNU4zWXvG1o2wj1AOu5Up-9ztV6eLfXCyeu5moMCf1s0qczyPFFaRyXG9bt_1Csc2DCgoUrajPxDlgZyAHlnFyN3Nnen22KasX0BkcoA59bz3FWQUCnY-JPEE28EXxXpE1TY7eqHb7gSQXABqdN5Myp8k3JVOQiOoUOaOfW7VmlJ9bjgYuy3JTG8mxB_MecGrIo1gIZLuzeCXGRPMn0kmIuBcx1vuGixWdbzQKO5-VHGBjthsUq6nqhW-6yvGuahAuxoHSgUhlUlAxXVrmhnYq7iFfii6Tjm4Xh6BFkRYoGImCAjjIso5nOshyGV5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c921d0c509.mp4?token=K_nupvrLjLLcthNMFFywrISDJNU4zWXvG1o2wj1AOu5Up-9ztV6eLfXCyeu5moMCf1s0qczyPFFaRyXG9bt_1Csc2DCgoUrajPxDlgZyAHlnFyN3Nnen22KasX0BkcoA59bz3FWQUCnY-JPEE28EXxXpE1TY7eqHb7gSQXABqdN5Myp8k3JVOQiOoUOaOfW7VmlJ9bjgYuy3JTG8mxB_MecGrIo1gIZLuzeCXGRPMn0kmIuBcx1vuGixWdbzQKO5-VHGBjthsUq6nqhW-6yvGuahAuxoHSgUhlUlAxXVrmhnYq7iFfii6Tjm4Xh6BFkRYoGImCAjjIso5nOshyGV5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جلوه‌هایی از پائیز رنگارنگ در مسیر ریلی دورود
@Lorestanfars
-
Link</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/465607" target="_blank">📅 07:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465606">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFZystL_B78jL7kXySdG-qgF-gmxvcKrZ4VmF3qhQnEj9AvTvI0ZYGDx1Q1K38ggqOPii-a5An3u5GqtKhqn5YLCKlXwkcIQRz6xaJ1-Bt5yqOsSrkZJjkeMgoXaAkS_cXDNrHA8GiRDWTKtKPo430sYW1GtJOJehy_IGkG7Z3QAWUcpkmWnK2aY6EOeeye4yeo-kRXd6J8YW4AC51FSt0TDeKhQWtby1nMQDXqg8SSJLMH4E7Yff4hLSehWr2gAki-cImH6kiMbn_lFoqwelX8yWPvR-U5PwJBgHVVIuQUSL6pexOUcSCw_rrDM9Ys61oK-ugK-R9auSfsdru2Drg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات هوایی پاکستان در افغانستان ۹ کشته برجای گذاشت
🔹
خبرگزاری رویترز به نقل از طالبان افغانستان از حملات هوایی بامداد امروز پاکستان به مناطقی در افغانستان خبر داد که در پی آن دست‌کم ۹ نفر کشته و ۱۱ نفر دیگر زخمی شدند.
🔹
ذبیح‌الله مجاهد، سخنگوی طالبان افغانستان، با محکوم کردن این حملات ادامه داد «ما این اقدام را تجاوز و جنایتی در نقض تمامی اصول پذیرفته‌شده می‌دانیم.»
🔹
در مقابل، سخنگوی دولت پاکستان اعلام کرد که در این حملات هوایی ۲۲ «تروریست» کشته شده‌اند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/465606" target="_blank">📅 07:39 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465605">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‌ بالی به سرعت برق‌وباد برد
🔹
مهدی بالی در وزن ۹۷ کیلوگرم کشتی فرنگی ۸ بر صفر حریف قرقیزستانی، دارندۀ برنز المپیک را با ۳ فن فیتو برد و به نیمه‌نهایی رسید.  @Farsna</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/465605" target="_blank">📅 07:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465604">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🎥
لحظات آخر در ناو دنا دقیقا چه گذشت؟  @Farsna</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/465604" target="_blank">📅 07:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465603">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پومسۀ انفرادی زنان صعود کرد
🔹
یاسمن لیموچی، نمایندۀ ایران در پومسۀ انفرادی زنان به‌عنوان نفر دوم گروه خود به دور دوم صعود کرد. @Farsna</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/465603" target="_blank">📅 07:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465602">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‌ عبدولی هم به نیمه‌نهایی رسید
🔹
سعید عبدولی در وزن ۷۷ کیلوگرم کشتی فرنگی پس از استراحت در دور اول با برتری ۸ بر صفر مقابل سولامان از اندونزی به نیمه‌نهایی رسید.  @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/465602" target="_blank">📅 07:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465601">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">عربستان حریف کشتی‌گیر ایرانی نشد
🔹
مهدی بالی در وزن ۹۷ کیلوگرم کشتی فرنگی ۷ بر صفر حریف عربستانی را برد.  @Farsna</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/465601" target="_blank">📅 07:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465600">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‌ عباس‌پور‌ نفس‌گیر برد
🔹
سجاد عباس‌پور در وزن ۶۰ کیلوگرم کشتی فرنگی یک بر یک حریف هندی را برد.
🔸
عباس‌پور در نیمه‌نهایی مقابل علیشیر گانیف، دارندۀ مدال نقرۀ جهان قرار می‌گیرد. @Farsna</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/465600" target="_blank">📅 06:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465599">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">جودوکار ایران حریف اماراتی را ضربه کرد
🔹
الیاس پرهیزگار در مرحلۀ مقدماتی وزن ۸۱- کیلوگرم جودو، بر حریف اماراتی پیروز شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/465599" target="_blank">📅 06:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465598">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eh7a8pTYpQysIcx4o2mpUqc7xhFnh5OlAIjacuowq_46BuXnDmTDBbPihCifDRLvA-FHzwfycE2J19qRaJk6dyZkSjE02dm_2Iimai0CvovHzH1gk9xS38ABGY0_Q6OEwhyUFABTeQ06UPIZpEn4FBv9Uc0_yPeH-GlEe3g_kjbGd7g6wENIiiiDPdlou1wtxP3NVjMBs9TlANEeTF0DWUdb-qdoDxxYd4fnWnpeRMLoqSF67GVtz0d1d1yj8svRcR4HnIhqfWf2asRSTCjzulVU1CxEzL89_Wz3DDuFy9UnVLduVR6lA2QB0ypA9A9ArxE03kOmkpwnQmEyHDly1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت کار جدید بانک‌های خصوصی اعلام شد
ساعات پذیرش مشتریان:
🔸
شنبه تا چهارشنبه ۷:۳۰ تا ۱۴:۰۰
🔹
پنجشنبه ۷:۳۰ تا ۱۳:۰۰
🔹
تعیین ساعات کار کارکنان واحدهای ستادی بانک‌ها با تصمیم مدیریت هر بانک انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/465598" target="_blank">📅 06:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465597">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‌ عباس‌پور‌ نفس‌گیر برد
🔹
سجاد عباس‌پور در وزن ۶۰ کیلوگرم کشتی فرنگی یک بر یک حریف هندی را برد.
🔸
عباس‌پور در نیمه‌نهایی مقابل علیشیر گانیف، دارندۀ مدال نقرۀ جهان قرار می‌گیرد. @Farsna</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/465597" target="_blank">📅 06:28 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465596">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">تیم پدل زنان کنار رفت
🔸
صبا نجفی و ندا محمدتقی‌پور در یک‌چهارم نهایی با نتیجۀ ۲-۱ مقابل فیلیپین شکست خورد و حذف شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/465596" target="_blank">📅 06:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465595">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0zrq-naj6zwYLUGfXmL_Q_3LrwpYYVB_VnbvSKV0CWe1oLehudskvUt_eCwxaPljYwkwXB6qv4-e9FifO6zrqBnDCSTo7VmBNs1xhqQBWxeP6-r7Y8cnlaOmWk7DPc7gD0YLXJTI8CuCvo0TrWWSqryKiNMsjrOoAe-RXr9octSJlg8OKbDwSa0llEoag62FaclJSNvjIx1OS2XzS47SFCIhZtLG7yZVd2j9kIKzuhbhqfkceG1GjKA6_pemXYJ4m647H13q4NzfFdkkSo-_075KltYxa-3UiuYWG392fGeepL7xbX7Mv9kEIIvTxaiX5IxvmMCjEiAqYyxM6cuBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعلیق ۲ شرکت مسافربری پس از ۲ تصادف مرگبار
🔹
در پی وقوع ۲ تصادف خونین در آزادراه همدان-ساوه و سربیشۀ خراسان جنوبی ۲۰ نفر فوت و ۲۹ نفر دیگر مصدوم شدند.
🔹
حالا رئیس پلیس‌راه راهور فراجا از تعلیق ۲ شرکت مسافربری پس از بررسی کارشناسی این دو حادثۀ مرگبار خبر داد و گفت مقصران برای رسیدگی قانونی به مراجع قضایی معرفی شده‌اند؛ این شرکت‌ها هم تا تعیین تکلیف نهایی، حق ادامۀ فعالیت و صدور صورت‌وضعیت مسافری ندارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/465595" target="_blank">📅 06:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465594">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بازی‌های آسیایی ناگویا عباسپور با پیروزی استارت زد
✅
سجاد عباسپور در وزن ۶۰ کیلوگرم کشتی فرنگی با نتیجه ۵ بر ۳ از سد هادونگ تان از چین  گذشت و به مرحله یک چهارم راه یافت. @Sportfars</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/465594" target="_blank">📅 06:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465593">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نمایندۀ جودو از رقابت‌ها کنار رفت
🔹
سمیرا خاکخواه در رقابت‌های جودو برابر حریف چینی شکست خورد و از دور رقابت‌ها کنار رفت.
@Farsna</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/465593" target="_blank">📅 06:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465592">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/538d7617ea.mp4?token=tpNCgidoHxCNctVDfUXKExP3oNfqJ9Juho-ilqZaF7nw-pTb2Ix8v7VsuqfQH_dbvwNV-4SYydZAWcDB1Xul3ZUea_uFfIs5DOKur1YE_OxAt6XZiq62PWaslUj4X7ho5sawmtaVTO3a3naDGS5ci_bFPLJ9ukUh8QS_wZid4yjCc1wLale70hJjJ3tYDL_dQWJ_0USRuYm5Y2ot0HGaEcyqvnx_W_Ph0cCSVM6cwSdWP9EwMatc577YLSxjgcQ3Isq7T6q-OD6_WO0ICx6ZTA0LvMTu7wDXzkAH2XEQxRKZ0xc_7MjHyjQvM2xJdTtNDEupUgD3EHclJVZAAzjyYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/538d7617ea.mp4?token=tpNCgidoHxCNctVDfUXKExP3oNfqJ9Juho-ilqZaF7nw-pTb2Ix8v7VsuqfQH_dbvwNV-4SYydZAWcDB1Xul3ZUea_uFfIs5DOKur1YE_OxAt6XZiq62PWaslUj4X7ho5sawmtaVTO3a3naDGS5ci_bFPLJ9ukUh8QS_wZid4yjCc1wLale70hJjJ3tYDL_dQWJ_0USRuYm5Y2ot0HGaEcyqvnx_W_Ph0cCSVM6cwSdWP9EwMatc577YLSxjgcQ3Isq7T6q-OD6_WO0ICx6ZTA0LvMTu7wDXzkAH2XEQxRKZ0xc_7MjHyjQvM2xJdTtNDEupUgD3EHclJVZAAzjyYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربستان حریف کشتی‌گیر ایرانی نشد
🔹
مهدی بالی در وزن ۹۷ کیلوگرم کشتی فرنگی ۷ بر صفر حریف عربستانی را برد.
@Farsna</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/465592" target="_blank">📅 05:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465591">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e34a3dcd.mp4?token=dlJFvK65d-HLSPsFv8TSndd4NMjOiPWcS9QgCpkESssgBDcQmwsU6nKCDpvmNHBBXgUFf_wFAyn0NprVqzsxYr3phsRVqkuoS4Yd1FufNOfySGa36iSlPBo7Siirdfw6QED2XsQHhtFzp5lTI8D2UXcMHQjPryK0L8AwS0AZelJ7gPUV_TnTJwiQumVqU52mDAXrkGbFMfBKOKYI8bXcK5LTaOh7Ili9o8ET9tzeoIjrRz_-Dwk2jYD92jkRUiDjO8sDrCh4zYWwhaKDvomTHoXZNan7NYKE3_N7Yahpy3p37q78U8aeaPuwKI4aM7hs0Pl0sXgWtDfbPEeBO5J8vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e34a3dcd.mp4?token=dlJFvK65d-HLSPsFv8TSndd4NMjOiPWcS9QgCpkESssgBDcQmwsU6nKCDpvmNHBBXgUFf_wFAyn0NprVqzsxYr3phsRVqkuoS4Yd1FufNOfySGa36iSlPBo7Siirdfw6QED2XsQHhtFzp5lTI8D2UXcMHQjPryK0L8AwS0AZelJ7gPUV_TnTJwiQumVqU52mDAXrkGbFMfBKOKYI8bXcK5LTaOh7Ili9o8ET9tzeoIjrRz_-Dwk2jYD92jkRUiDjO8sDrCh4zYWwhaKDvomTHoXZNan7NYKE3_N7Yahpy3p37q78U8aeaPuwKI4aM7hs0Pl0sXgWtDfbPEeBO5J8vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پومسۀ انفرادی زنان صعود کرد
🔹
یاسمن لیموچی، نمایندۀ ایران در پومسۀ انفرادی زنان به‌عنوان نفر دوم گروه خود به دور دوم صعود کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/465591" target="_blank">📅 05:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465590">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edb7b65819.mp4?token=JDXCiQgsFMscb4bqS4W5asYjZKNy5TxYaTRmuch4oyKp4R7ig5zSdHNDJSP8iAR0HIbSOreKFp7GcW5ersosJ4QLj-YFWQBXvQfXUZ6bxqCvbSDgw5_0iUaZit2KxkD1sgVBc59wA-WEt-Nz5qSyiWWGvXdLFVUC1RZm6zhiAaxMi1qRoplwCqYNYAQIN1GAceA_oDjesaDCQERWOEjfut_MH1LJu43vVi6hsSKXRcUexPIc01Qs3sn8Ni33JI4H6x0r53JiK-RcI4Q-6QeVYWunaht2rfOVAVDwE0tngB1NhV3Arclipv1B0iZQ4pHS9j0sNaExONNvVz3I3e51U6jsGr7bwTAQCOdM2_eXU3h9f8RBwZbo0KlNfyx2mYtn-wrSmNJ14_uqoSF6dZX6JJ6whczQxBkzmic5Bd8hsEl7g591z2bhrEdDjOz1hOqKNeu_v8Y3SVF3x0rqYqoqoDkvdIUvCIyy7QZY2IW7PmnaMfg0CnWX8KmGjLlgeJqqH-UVtTcbsIKDIJ53EYzM5uIR3ModaqRy7Wzz7PjrH2Cpz_p8rKLY2L-NaC3pY2pNbPLrTuY_uh3VeOLPJRlPrBJTEcyPdKZIUI0TnP7csWs4Kff3CVyq2bdHDROSGGwb19cFjaI-zkdhn8F8D3I6ynpVCionZPxNiVCJCSsEX_0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edb7b65819.mp4?token=JDXCiQgsFMscb4bqS4W5asYjZKNy5TxYaTRmuch4oyKp4R7ig5zSdHNDJSP8iAR0HIbSOreKFp7GcW5ersosJ4QLj-YFWQBXvQfXUZ6bxqCvbSDgw5_0iUaZit2KxkD1sgVBc59wA-WEt-Nz5qSyiWWGvXdLFVUC1RZm6zhiAaxMi1qRoplwCqYNYAQIN1GAceA_oDjesaDCQERWOEjfut_MH1LJu43vVi6hsSKXRcUexPIc01Qs3sn8Ni33JI4H6x0r53JiK-RcI4Q-6QeVYWunaht2rfOVAVDwE0tngB1NhV3Arclipv1B0iZQ4pHS9j0sNaExONNvVz3I3e51U6jsGr7bwTAQCOdM2_eXU3h9f8RBwZbo0KlNfyx2mYtn-wrSmNJ14_uqoSF6dZX6JJ6whczQxBkzmic5Bd8hsEl7g591z2bhrEdDjOz1hOqKNeu_v8Y3SVF3x0rqYqoqoDkvdIUvCIyy7QZY2IW7PmnaMfg0CnWX8KmGjLlgeJqqH-UVtTcbsIKDIJ53EYzM5uIR3ModaqRy7Wzz7PjrH2Cpz_p8rKLY2L-NaC3pY2pNbPLrTuY_uh3VeOLPJRlPrBJTEcyPdKZIUI0TnP7csWs4Kff3CVyq2bdHDROSGGwb19cFjaI-zkdhn8F8D3I6ynpVCionZPxNiVCJCSsEX_0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی‌های آسیایی ناگویا
عباسپور با پیروزی استارت زد
✅
سجاد عباسپور در وزن ۶۰ کیلوگرم کشتی فرنگی با نتیجه ۵ بر ۳ از سد هادونگ تان از چین  گذشت و به مرحله یک چهارم راه یافت.
@Sportfars</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/465590" target="_blank">📅 05:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465589">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نمایندۀ تیراندازی با کمان کامپوند به جمع ۴ نفر برتر نرسید
🔹
بیتا عاشق‌زاده در یک‌چهارم نهایی تیراندازی با کمان کامپوند با نتیجۀ ۱۴۶ بر ۱۳۵ مقابل کماندار فیلیپینی باخت و به جمع ۴ نفر برتر نرسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/465589" target="_blank">📅 05:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465588">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‌ تعیین تکلیف آمریکا برای عراق علی‌رغم پایان حضور نظامی
🔸
باوجود پایان حضور نظامی آمریکا در عراق و تکمیل خروج نیروهای تروریست آمریکایی از خاک این کشور، واشنگتن همچنان برای بغداد تعیین تکلیف می‌کند.
🔹
المیادین به نقل از یک مقام آمریکایی گزارش داد که واشنگتن…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/465588" target="_blank">📅 05:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465587">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">میدل‌ایست‌آی: تنگۀ هرمز تکرار درس تلخ ویتنام برای آمریکاست
🔹
مدیر مرکز اسلام و امور جهانی دانشگاه زعیم استانبول در تحلیلی دربارۀ پیامدهای جنگ آمریکا علیه ایران و وضعیت تنگه هرمز نوشت: این آبراه بار دیگر محدودیت‌های قدرت نظامی آمریکا را آشکار کرده و درسی مشابه آنچه واشنگتن در جنگ ویتنام آموخت، پیش روی آمریکا قرار داده است؛ اینکه برتری نظامی به معنای توانایی تحمیل نتیجۀ سیاسی نیست.
🔹
کاهش شدید تردد کشتی‌های تجاری از تنگۀ هرمز نشان می‌دهد که حتی قدرت نظامی آمریکا نیز نمی‌تواند به‌سادگی امنیت و جریان عادی کشتیرانی در این آبراه را تضمین کند.
🔹
آمریکا ممکن است توانایی وارد کردن خسارت به زیرساخت‌ها و توان نظامی ایران را داشته باشد، اما مسئلۀ اصلی این است که آیا می‌تواند شرایط را به وضعیتی بازگرداند که تردد کشتی‌ها در هرمز بدون ریسک و در مقیاس معمول انجام شود یا خیر؟
🔹
ایران حتی بدون برخورداری از توان دریایی هم‌سطح آمریکا می‌تواند با ایجاد نااطمینانی درباره امنیت عبور و مرور، هزینه‌های اقتصادی و سیاسی قابل‌توجهی ایجاد کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/465587" target="_blank">📅 05:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465586">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8oKEDTMxnnekMsnKsk7d4U3wgIgNxRLqNSN5fnLFeodRLsk3y4I0P2TCrDyl4PbSXClz0dLWOWAdbtvc3u_aMTuIa4sztII1oO6VCNpVThUjEOoNCN-oqByW86AjlAyRCde8rYcGoFZm1utYbmOa_d8a3arP8UToNBoe_H09ThjnLTqwzbT5EjOa1JW35vJSy570gIIcNjWEjvbKPADAYlwAgPSC4OIqWJZshvFOuILtV3H0bjuHzdv7AAFFdl2pBtcnuhWSH6UbGGoA8C1VksQJDg7pGt-T1RPdUTy1likz6_RnFK832ANztvBkTShlit14XXXAMFuxOyASO8ojg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلاش آمریکا برای دخالت در انتخابات ریاست‌جمهوری برزیل
🔹
مقام‌های اطلاعاتی برزیل از تلاش‌ها و اقدامات آمریکا برای اثرگذاری در انتخابات ریاست‌جمهوری این کشور گزارش دادند.
🔹
درهمین رابطه، آژانس اطلاعاتی برزیل اعلام کرده که مداخلۀ آمریکا را از «جنگ قانونی تا دخالتی که آشکارا مورد اذعان قرار گرفته» شناسایی کرده است.
🔹
آمریکا پیش از این دخالت در انتخابات برزیل را رد کرده است. روز یکشنبه دور اول انتخابات ریاست جمهوری در این کشور برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/465586" target="_blank">📅 04:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465585">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/452d37f684.mp4?token=gHp0h17S25QeKgRLvJLjz7I2xjAZhqaX6QHIYxocy9bgzIrbcqhzT6spwCnFfAIKi3SnrJFa3FMldenJYOrngawndFX8vAxlEE06a6kWzgvQHNdksCw1EJzu1tP5axlVaEUeU69VVso4dZaMKX-1BHbFIx2pmWM8zcTWy21JWol6VmNUW9KzjSiF06P07DfgMvJz8GoOvJnib_5CQYUAn0j3EXUpBLew7JWJjHJCpS2poHemBxW_L3pNyNE-4ifjPiGKfRQ_Furgmx-wt---Zmiuqg8tClhra5HcSCwlOwypOpPmO8xWRd_GIRdKyfEtz8IqmgeSVTm35NiidjGRSYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/452d37f684.mp4?token=gHp0h17S25QeKgRLvJLjz7I2xjAZhqaX6QHIYxocy9bgzIrbcqhzT6spwCnFfAIKi3SnrJFa3FMldenJYOrngawndFX8vAxlEE06a6kWzgvQHNdksCw1EJzu1tP5axlVaEUeU69VVso4dZaMKX-1BHbFIx2pmWM8zcTWy21JWol6VmNUW9KzjSiF06P07DfgMvJz8GoOvJnib_5CQYUAn0j3EXUpBLew7JWJjHJCpS2poHemBxW_L3pNyNE-4ifjPiGKfRQ_Furgmx-wt---Zmiuqg8tClhra5HcSCwlOwypOpPmO8xWRd_GIRdKyfEtz8IqmgeSVTm35NiidjGRSYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی جبهۀ شریان: برخلاف ملت، احزاب هنوز مبعوث نشده‌اند
.
@Farsna
-
link</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/465585" target="_blank">📅 04:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465584">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf2aaf03ed.mp4?token=Cv7RW0zluG8au12o--D-hkx2xzxsJvdy5DuioELDvjAkv0J_JXwuwUQWJ8XhO5ZsFq_FKgsvMXC9nLqZsCc_RSheWh5Of0MmEBFuFiv6j-BAao7mGWyCvA8X6YbevswZhWcCqQT9Yks1Wx5Na6fecnE4k718HqRpBu4iBaHmx9rE4SLLEFltFOSOehvhPRxeQOpZO7OKlmKLcM2g5ZAYu2NYs7BNmSeQdDe-9pHigJSu_ZRnoUYG25kQ75gnvcZnJ1quYhuPMZJy0xDpI9SlHgOi8zVLec0mDmcHPWMiR7-CPMm8JHwX2IEykoVpkGadsQVzpX58AR2hiuPOA-GxhDFrNnkhj_8fgbzsMVSEDXXuts1BaC2r3PP7jDo674kz7tgYtVOMmiryeVzaicx2R2BqtVVH-uxNnpMV_EXqfe91hlMNLPzO8y6gUdVFV7iLjpqvE6s-PG8FiKjZdP5-09Fu5HQQq9DihKRPpavNtqLJ_my-KQP-2ozckM_q1hKndd7htcZQMZWCuKo2AtNM7Iezex_UDJEqpMyEBDXZiCjlQ4dmPpzPlohySUd404yOCxgvI_NoiAMgD1No0_g-htRtrWOpOuJvu2h8bbdqJ5yr9-lQXDa2VnABEso_Rq34E43cQUNdRMmdhcasTS9MxUHfmVBlKXrfvGUVslEdq-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf2aaf03ed.mp4?token=Cv7RW0zluG8au12o--D-hkx2xzxsJvdy5DuioELDvjAkv0J_JXwuwUQWJ8XhO5ZsFq_FKgsvMXC9nLqZsCc_RSheWh5Of0MmEBFuFiv6j-BAao7mGWyCvA8X6YbevswZhWcCqQT9Yks1Wx5Na6fecnE4k718HqRpBu4iBaHmx9rE4SLLEFltFOSOehvhPRxeQOpZO7OKlmKLcM2g5ZAYu2NYs7BNmSeQdDe-9pHigJSu_ZRnoUYG25kQ75gnvcZnJ1quYhuPMZJy0xDpI9SlHgOi8zVLec0mDmcHPWMiR7-CPMm8JHwX2IEykoVpkGadsQVzpX58AR2hiuPOA-GxhDFrNnkhj_8fgbzsMVSEDXXuts1BaC2r3PP7jDo674kz7tgYtVOMmiryeVzaicx2R2BqtVVH-uxNnpMV_EXqfe91hlMNLPzO8y6gUdVFV7iLjpqvE6s-PG8FiKjZdP5-09Fu5HQQq9DihKRPpavNtqLJ_my-KQP-2ozckM_q1hKndd7htcZQMZWCuKo2AtNM7Iezex_UDJEqpMyEBDXZiCjlQ4dmPpzPlohySUd404yOCxgvI_NoiAMgD1No0_g-htRtrWOpOuJvu2h8bbdqJ5yr9-lQXDa2VnABEso_Rq34E43cQUNdRMmdhcasTS9MxUHfmVBlKXrfvGUVslEdq-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اگر دنبال آخرتی باید در دنیا تلاشت بیشتر از بقیه باشد
🎙
حجت‌الاسلام نوروزی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/465584" target="_blank">📅 03:28 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465581">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MC43NXNEAgiWjWT_49Rfsq3PtXJeUOe2eassjreyyVWXmdLtq1iZ-mWmqZxyDr18ePcxXbvwJtGfKl3_FI-W4b-OTp2LNd_aDWxzu4OBQYdBwaozFPa8B9PcdDhn03Zw00hs1O-qSBrOjLxEBPXYqVdfSf8JbmfCZfd_b5qhdXaGc1jNpd9mOm0wYTt9OW1AlbWnI_5Cyq-7sry-wJVwPpUYzpgt9T0uql4tG2jZLYH-A9fSGlST04vqOgbkILti54kq9XjjfBxEFgDvkeCLg2l5k0BmrkWeZghFTq7ME9GI_O9ml09fZNT4mdazSmDTWzGLl7-oRUeI6d7y0_EQfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NOp0ZOSraciVWWSOgvmSN8j5P35y6Zyre2QX8ABoF4-v39fXjdYicLE_6FhdN-LB-IkGLYgIPlRi8bSt1WCWMmasYFSLW8XipAkbERL0pn6Z6cO0Y1NKX8_o4geNcTxpDmhdnli8700pB-zCvd8AoFoqhrbXICaxHA6DUvDJdiSeuWdYewvMNSI05j64nZCb-Uw1VLbBvoDITKLkr_cfSTKafV2X96mO38fz9ugPwTm6FR7_4ykl6rGvUKElR6EDWU0da48EqwZRMLtp83guts4uCwjFs7VHed90Ht2pZ3LtMSDyKHeUS4kS9IEQyWVSlH5hN_7aEheCa4dW1_w3Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ugAq0F0_vpzg0Cn56cQL1TlmJMB6YEbHe_M091CT0m623vjV6GSdUA5N2BpRWYs92CU-2-EvgrSXl8tRORuT1Oy5YJaM3-cQyaclKNpXTbFteNB6ZPSpvbq9YW2a-0H-yKuLhLGQ0yOtM5NNB8O8gu4Q2pKfgZItdFPwO2jBdEC4WF4B1J7ecIdpYh8WKK4UUIH5hTK_5AJRH2Y0hDCpq8zVY-co9F4GwNyo3aUa-rqSibuuHSRjs4lUNTEmfT_M8ZHxJitCLhMKWHx-ONq0oQPw__Vd0c0ZUcxJbRx8-UHM4ITYl9vmOufsykKzXha7LwyCTu4y-yjTkY3XpTIO1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اهدای چفیه و انگشتر متبرک آیت‌الله سیدمجتبی خامنه‌ای به خانوادۀ شهیدان سیدعباس موسوی و سیدحسن نصرالله
🔹
جمعی از فعالان جبهه فرهنگی انقلاب اسلامی در جریان سفر به لبنان، با خانواده شهید سیدعباس موسوی و شهید سیدحسن نصرالله دیدار کردند.
🔹
حجت‌الاسلام والمسلمین پناهیان، حاج حسین یکتا و حاج سعید حدادیان از جمله فعالان جبهه فرهنگی انقلاب حاضر در این دیدار بودند.
🔸
در این دیدار، چفیه و انگشتر متبرک رهبر معظم انقلاب اسلامی به خانوادۀ شهدا اهدا شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/465581" target="_blank">📅 03:18 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
