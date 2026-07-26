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
<img src="https://cdn4.telesco.pe/file/OX6DepYrEZtE4USHcYdSCC7rfBhVkMRR_uMs6kDD1_Tqd--MvFG5LGXQCOzLCcNHcnym2iAMSSCixByR2TOA1ocrIPqR0e0w9iMzfzWw4hzFnChi1vP7ZYkmtpF5J3jYkfin_TSBJychEPPEZ4HcfQMxx2l_19Yan4NRlY5MNHoGM5zkyF74X8LPf4I6DNixgsHcUuw7cUdLUicdnxAthAMk2ftJbltCBCoMnhClntKXnGmSgMYFFJBYdBYC6tsOCo3x-O1cBalAUsfDfu7mr_lEgnYa9FPt49Az6uR_JCz2AtJ1V08virF4d8XFxTG42GRur_OUiVvnioPi-yr41A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 65K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 21:25:13</div>
<hr>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEgMOSHveFO1xJ4gaGdBP0WhAis7h53aEUtzooS6oZsV5BWmFapNHX5_q8raGiGFQgCNJ-t21nnuYkojlkvIDFL6fbCtNWF_oWtlr5BPhsrEamfepi-_ROQHb-BF0QdOAZKhyWnFUaLVnFIQVL54n1MFatBqWE7VosQ7LbnX7VORu9NAfcvu41FJ0YpuFsCoWRYo72zV4QkE5qgrPA57lUV_D8RmwNMmlfBocJMYeeCunRHitTslXVOLltk_7xu8jkVUepKElX3CuCnHev6ZKqdC6Hcm71Hq1jOaCqr1kSYtb52zbkcqXabLKsRR5NwJcrRgXSfxuZEYAJ1da8Hhqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qJVNluKjno2kvVW1LeJV789-qsdhlaDztbwc9_KE8uv3RdNNBy0BE0FcedZz7p3uj30UtywUjZJI88RQQ5ae5SQSfjUFsrzAYyErh4_lTeEj_3f_G6EVLcl9yh5Xb_ORh_ki6xB-aKgL5yLtkLrHEPtoRKyBmpDz4wRmeSG2flhTa61va8bhH90wf-UPgL7QIhLBxf-xdVgolrp4f_xOFvLtkWl7t0m-5eB92bRYMc0vAAsFoNG1GpPA3ZxpGso37cBIRsHA9cCOcormPNmPbqHKLPZZe5zDXVld72TB67F5JlGIf_5JKL6yqLDDg3LwEhJoeGw4SIvpquvm3VmCOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/km_yo_hOZjETIqxDOpoRwrn9pCGcx-Q7HgBzRaHt-bwDl2ZhP-lVKmNQWBFBq3PCm-saEqpdavmVwrIBoy7hHg25VZw79oBrBCrnaqjtRL3Gxaz5SeGCOgz5Vf9ySgnNI5R93hRJEsagVnmcejm9u-QicMGhKyqWcuz-GlWNr1xxxVaMMmA0Rz4u0Hsey3AKyyDFCEui3kBHd0uQf0cp9EHzSuXhWNzfdU2CnnQEpczyN6lTgDqHzBY6zXRB56lFvUtQzuJ8H1UhFYv5cbtXlsFY2EO8EZh1so-LXpmAnL73peLRi2ouXCgsdadEraDC73UoVXA3OEVOt28Grgg7xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U4JTaf0vHrdOtGcnXmHTq1egQcb3xOXdf_W1gw5uAiWtzNhNR2dlQ6HG946Tm2aCi7MqeO9drxwVv10XxZ23lTKz3u4LB-pmVFIfY9Hr9asa8sS6oWjsD0q23JwS5f0Gi0hZuf4TmFxy4AizAVisGkf8_TYrHIz2ioumaKVzKmEf321pRTKIbaI0DZSsEphn0BupyYqKQB9XjtLHAklpu3ZfHiBSvCr7iLsM3UDkU5u-UJYogGBUlexjdX7BTKgOry7u5v4dgqeZEjKVn8H8fjl6z0op5q08lgNwUEI1-8DFINnDL3efqLZ5P6H1t7p2rxp419HOuOtk_bgHbt-TvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zh4h0iRyK5zhTlNO47O1CQcmXb_9PkeeFOy69p9mN2_9OigEeGrjVpgHtviV5SvNDbsXIdK2JH-G5oI5LdSPHxI0J0fAZYlrDyZajhAiYO11uL0UxuNoKw0LPvs94wUIcuWDQeMNJWEtiJXYrfO6xXiMw87c2VW2yxPlbCQkKocjVZJRG7IP8LQ74h0kkPIuFi8KKqBMZOoyuKynugL6Bp0po_pOvKUyS2FRCrdrjvd34Z0BrPUjcyjA0Eivi1b3wT3ETXDTHJS6S8ygri5QjAcUxKR6rStIJQyuqS-BazXTC7tGsQJOneEb55VES5-JZSBb2YTr_ZpGRI5afZDCIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVHNyHPeagSnxkwEfmIrKKeiocZOMLHac-Ampa5iYk4oKWnbnUQ5mmDpj43K9ZZi4ScMe-SFPpbMZp1b374940tv8hyRarAZClhCYlCNkGyTcpRQds0j95atYiMfifXFOZGGgkLPwwPfCRVRR0k1WTNcrkBJMJgZ6qvZk6wpv8qiVbtOlxQqaTASMiclI7q0gZK8jMWIL2hhoGbNqhuD_Jfle6Y9VBm_9GALlygBHfOXYwj9mjO04vM28hgbpjJbAiRy3v1y4AFppInFPv60GbmuRu8QnFNqagehXpjfvLfF9y6oQ41jn-rk4p8tS8jLs4_knXKQ7Fkm41mt_U8Nxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vU03JBBIUrINr83zJT82G-VOKqE8hOi6VDow9Vk_JrqmtdlDqAZ4VWG2z6kPYKYWnTvcu1ghQYhN8YxdE3WNEs-puYUx85kYY4Gj7TJ1HIHBl-Z1qC3StQRjFiHbT7CppiHHAE4v1oZPOpZUMXOfdcUN1h9ilzqqgRBd5aJhbmIOAabbejFL_KnA94YSUmqaZULOPgbThc7gMMVMBuJCRXVs-BoDbGEmpCSNmoXpnK2UBLLuvWLwEo0C_AmejZoVeeOOmnT1FrgCm600e-Zya7Q1SPA1SiH57ooZqksGRi7Mt7Z4_If_Z6p7vDT3ipcJFoN3pXnyeMra1mG0EJK7KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nNiv87_bgx5Ib-4XrZoyPa1gkl--4Co8SXGWhFNdA3adZ4pKAdUmsw0nR4xgsHjZUuX5gsQVPFO5KezOwqWO3L1xbbmdEuQDBWHS8vjNdqL2hlpRK63tguR3E_cSuXXme-5saFXyw7fqXkvbeDe1AxXkD0-ULc-PEqXiVAowBx1jCqpP6dTtSajdGs7XnUUcLv5xPe-BJPkKDQCqbcGk3jEbZbQmffsyFrgzecKtTxHvJq4TnWU7vdfUUk1dtd6Ihua427Zs25w1xlxi0pNEGYQ6z2nKnwV6v8ew46_Oa32ikzchZl3UC-xEMjcfdBaDhab_meJ88qqQcqjjIXuC3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gkgFVC2gkf8pqf4xXWGIqRs15T_ThzjijgL5KfqRa1nkceAFIjhVbaFg4h0rbMEH2CpLI61Q7pthGfKmKPY_XkgcG8TyInsFRFs9XbuO0DZxkKLuIYEZTUTL2vcMo6mx3UYDHpq2emDvv6D6R11ZH47f8OCx-zShi-e8MNE8Cjw3YEw-W0_UNpSUMyCHSSpeJEWIEyEjcpwnSGaT3LNKrgODkmKAxcYSy-c-lDPivjdjBWT0MzhNiymqbM1vnpRUNZ4aRv0K7SoinrBK3LP0hEBVBSWwqhory546xk5jz9J1vZ1Tz4_jZq_3LpkTvzRMWXbZGDkVrxUPx7-ZbWpfMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اینکه بارها نوشتم، چپ‌ها، با اینکه گروه گروه توسط ج‌ا «اعدام» شدند، آواره شدند،  نابود شدند و ماهیت سرکوبگر جمهوری اسلامی را به خوبی می‌شناسن،
اما نوبت به تقابل جمهوری اسلامی
و آمریکا که میرسه، یهو مصمم و قاطع
میرن کنار جمهوری اسلامی می‌ایستن
و ازش دفاع میکنن،
این یک نمونه‌اش!
به خاطر اینکه برای اینها مبارزه با آمریکا
مهمتر است! اولویت اصلی است و اینگونه است که جمهوری اسلامی تبدیل به یک متحد میشه براشون که باید ازش حمایت کرد!
و این روزها خشمگین هستن
از مردم ایران،  که چرا کنار آخوندها و سپاه علیه آمریکا نمی‌ایستید؟
تصویری از پست ایشون و یکی
از هایلایت‌های ایشون.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">عراقچی در این بخش مصاحبه‌اش درست در خصوص آخرین روزهای منتهی به جنگ ۴۰ روزه صحبت میکنه. جنگ ۹ اسفند شروع شد و عراقچی از مذاکرات ۷ اسفند می‌گوید.
اینکه جمهوری اسلامی در مذاکرات به هیچ وجه کوتاه نیامد و آمریکا را به این یقین رساند که مذاکره نمی‌تواند گره منازعه هسته‌ای با جمهوری اسلامی را باز کند.
عراقچی به صراحت می‌گوید که چگونه جمهوری اسلامی تحت رهبری و افکار خامنه‌ای، جنگ را انتخاب کرد.
(با بی‌حاصل کردن گفتگوها و عدم انعطاف)
وقتی مجری به این نقطه می‌رسد که جمهوری اسلامی می‌توانست در مذاکرات، مانع جنگ شود (که می‌گوید باز ادامه میدادیم چند سال دیگر…) عراقچی می‌گوید : تصمیم گیری دست من و شما نیست.
این برنامه فتنه‌انگیز ۲۰ ساله هسته‌ای که هزینه ۲ هزار میلیارد دلاری بر ایران وارد کرد و حاصلش فقیرتر شدن مردم ایران بود، این سیاست ۴۷ ساله دشمنی با دنیا، این دشمنی کینه‌توزانه‌شان با مردم ایران، این جنگ‌ها را هم به ایران تحمیل  کرد، که عراقچی همین جا هم می‌گوید: مسئله ما زیرساخت و تاسیسات نیست!
«شکست در نابودی تاسیسات نیست!)</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6359">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پیام فرستاده برای «شیعیان» ایران
میگه اون روستای شیعی لبنانه که کاملا نابود شده،
اون یکی روستای مسیحی لبنانه،
که دست بهش نخورده! چون رفته متمدنانه داشتن.
این هم روستای اسرائیلی (یهودی) است
که با اینکه تحت حملات راکتی حزبالله بوده،
ولی داره زندگی‌اش رو‌ میکنه!
و میگه دست به اقدامات شامپانزه‌ گونه نزنید!
چون - مثل روستای شیعه لبنان - نابود میشید.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/batrqa-JWqraiFwD3KPlrEOHk1skX1abuwhSA-BayhhwthlyUOMWdGEywcfzJenXr43KrHXigS2UUQXHuhiKXKrQ8ezlmG8mRvAS1WOk08tVmBPEoNh9v2Kc8P1thzJPU_vx-IE58voSzUu8QMelQEFHm8S5DCi1MTZ8K5Wfltle-2J4Jfef_WGnkUDtVhYaJwPGsoipjBuRoWtHy4sHsoFFCQOS1BgJZ6PgrXFzHBg6J0s2_A1i9GMKwNVA5x60slsPdbSeSQD86sVdh6aQNftoqL7HQe55igtTBL3kr6iDuBRFAGssuKZvPU_2gC7g9qUOAIG-SqZD-bmt0vyhKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pKeDKf_6UkXDzui1SPIv2Yns23AqkFa-q2K00Wrtt5S7GKAjgPuyg5CINOoxCIZYcL-JTbenWHelM_gFjS7U-GoDec1y9kxjRnLBVqt2OXznl-HR635_epM7uDmZ5-vAykOUOucht9pb0ngUYeusO_sz5782HhYNe2NM0EMCFJPMv7edGEks1WOseytAEY98UpyGIqW3zNGiP2IF_2Q-kgiQ9q_2AjLbFTIJAb19_Zv-VJmqw3iRAQ07x37ENQomOgyHa1eBqQyTgmnk_QHHaUs-hTHOjtWEhZVEhwnnhE3wUIyI8RsUSC7ZeI_PUjuzxCDgooZh3Bp1dTJsH3vrTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این متن رو کامل بخونید.
در  بخش سوم می‌نویسه اصل این
بحران ۱۵ روز اخیر از اونجایی
بود که کشتی‌ها از سمت عمان عبور کردن و جمهوری اسلامی حمله کرد به کشتی‌ها
موردی که ۲-۳ روز پیش کامل توضیح دادم.
جنگ رو ج‌ا شروع کرده و دارند زور میگن به عمان
بخش ۵ هم بسیار مهمه، در خصوص کوه کلنگ، ج‌ا در عمق این کوهِ سنگ، غنی سازی میکنه که حتی با یک بمب اتم تاکتیکی هم نمیشه نابودش کرد! و چون خیالش راحت شده از اینکه غنی سازی‌اش متوقف نخواهد شد داره رو تنگه هرمز هم فشار میاره. اگه امریکا بخواد برنامه هسته‌ای ج‌ا رو جمع کنند، باید هزینه زیادی بده (جنگی بسیار بزرگ)</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6uXN6AIS_5MoIUxC8Y7ktV9p3gNfFu3TR5dpzWtVtsp3ak8GY93NMY5gwTvkLt2EP0AgE26uNAI_5mZ3VS4yzWja7DE6sXcoE56ogTN57GbmcmCRrA99--Vl-uze9Smv4aNX1gBfVF6WnA2ku1E9ydTd69jXDbsfeB_G2edKTeEithmOACjtkYiRBGD__x46cvX0KjphzHYInXTjdn8nNCCb30QIS1IOCAXqrqHtx1rzduST8WOJdn3jn7vio-1fxqGa-uTmg-MMfU57p15zqKAnsO24gUa4ZDerk2oI7emoQCiqoFEElxZX4AGfdV1oK3aX-dd4PJd0FfIrBrWXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=iuWPbpNHxteVCOXDv0dz-k8blWi8I1ib-851yw-ShhpLeT3PD3Y4kEguP5A-47eNYNGagLPIsswDM-5QDvDgyKEFdhs-9KVvvELve5pXwbjjid86noLSsE4ab2c4uwvoNnQXbusiIIT6qTmcVmSbQwnQhHQ7-fNgoJJVF51P2vZsVMakF5zsvNr3dFpVGhCQOmEvjKYsfSSw12sjUUOFoCxTR0GNMPm1HztEdVUEU4qmOm7hJnAXWyNuvz5PGq5xN229-MnvtAYUy9Bkq72iBgY4eBlpc5Awh5Ie09iU47XDX6Dy3CxMNMcK9y18s79wxSOznCqhJsOm7xjKQVkc6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=iuWPbpNHxteVCOXDv0dz-k8blWi8I1ib-851yw-ShhpLeT3PD3Y4kEguP5A-47eNYNGagLPIsswDM-5QDvDgyKEFdhs-9KVvvELve5pXwbjjid86noLSsE4ab2c4uwvoNnQXbusiIIT6qTmcVmSbQwnQhHQ7-fNgoJJVF51P2vZsVMakF5zsvNr3dFpVGhCQOmEvjKYsfSSw12sjUUOFoCxTR0GNMPm1HztEdVUEU4qmOm7hJnAXWyNuvz5PGq5xN229-MnvtAYUy9Bkq72iBgY4eBlpc5Awh5Ie09iU47XDX6Dy3CxMNMcK9y18s79wxSOznCqhJsOm7xjKQVkc6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حمله موشکی اوکراین به کشتی حامل محموله نظامی روسیه برای جمهوری اسلامی در دریای خزر
زلنسکی با انتشار این ویدئو  در توییتر (ایکس) نوشت که نیروهای این کشور در حملات دوربرد در دریای خزر، شناورهایی را که برای انتقال محموله‌های نظامی مرتبط با جمهوری اسلامی استفاده می‌شدند، همراه با یک ناو جنگی هدف قرار دادند.
«با حملات دوربرد در دریای خزر - از جمله کشتی‌های مورد استفاده در حمل محموله‌های نظامی مربوط به ایران و همچنین یک کشتی جنگی - به نتایج بسیار قوی دست یافتیم.»</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWTwy7qFQ2leTVpbUv0pOGtqMnDhsmyLo4z-o-7nBI2Z9F-kTUxcrkDAT5LqcUt552dWvAEuWPEpjjnmmQXYZbj6mfmjnjmLYNLWSqh7t_nZiOrsD4hbTQOJ3bPFLJOFM4rY3aS03vNsSYxBaPY98YeUarOaw5NYg--fxUelxAu6kTC0VqWTmUs5mx6BMIScMXFqhTYuPA0aZeumcBVXiLhD_TRtTPrn2kv9ji9Id8Zw7LmmRqigFMptRZ1imxhuFRpwcq4cDbVXFeeDgRFabmVzuiMwHPHiKXCXGuf_jr8lhUkRNi-yVFxHjvTrbzGru2gea75qwjg1ZN8aGho74g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_DtuJ1GxtyiAwRtP-_0onUwXua2jBmK614t4txgytXgYl4ZSDs4NfiL1bH6rVK0hkN3wQyUK8IXcX_rUfJf_1eLxFG3PTpLN7UueFEkgjVkToAZTJMfjGV09WLZ83b3TGrlXo6Cv4xmXEdRoSxEaFeAqsYKxgng0yOO8P4i5sIvN31nlgIQKEX-BAB9Fm_V9nwj0o7ReN75SEni9tawF0tqwurQD0XL2Qio5DZxLBUePlEXGCWU0_qlfDvQ9N44_CE02y0jfsmUhhLZdRcPiAxhYsBvxkN1dzQDOajRn2dfbYPMeQyvvHYDVDhyhbtipwoJS_3Nte5__RyVPTbMbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMm_ESU-hX2-8muoQSdzXE_BM4NLEtcn5J7l0m8TdQcx2vkrotM2d1UQIKqF4jF0jExUa07Mh7uCHsUifRB_4a-jgzjPkW8lhcjRTf0yW93aZ2CS0u1DWAfniKXkWiNMIcx_wy3qONuzKNkNeDlimLYsq62QWADVyNtcFqwW5C2SRZOt-O5aZ0FsKNcP-n54YlavS9Sm-sH_xh1G8BxWiVWCZYquEPGjIT99eFkH9Hock734ZczLuRLgWBOPtQ6hRnkZtMgY5EuNecQRI0NpBMzBaRIOrljn6VqsaOvdDmQKpF47Zw8nXGllxmdADVzB9WBvfEUGZPxehtHw0yDfwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دو روز پیش صدا و سیما،
بخشی از سخنان پزشکیان رو سانسور کرد!
اونجایی که اشاره کرد که خامنه‌ای در نهایت
طرفدار مذاکره شد و کوتاه اومد!
وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که
صدا و سیما مطالبش رو درست پوشش نمیده!
و میگه یک گروهی خط می‌دن به سخنرانان و مداحان
در خیابان تا علیه «تفاهم‌نامه» صحبت کنن
در حالی که به قول عراقچی،
این تفاهم‌نامه، بهترین تفاهم ممکن بود!
[همونهایی که موشک به کشتی‌ها میزنن
همونهایی هستن که این تجمعات رو سازماندهی میکنن،
اینو عراقچی هم می‌دونه،
همون‌هایی هستن که در صدا و سیما هستن!]
قبلش هم صدا و سیما،
بخشی از حرفهای قالیباف که مسئول اصلی مذاکراته و رئیس مجلسه رو سانسور کرد!
(یادآوری : هم قالیباف و هم عراقچی خودشون  از مجموعه ۳ پ هستند! و باهاشون اینطور برخورد میکنن!)
این دعوا از اول انقلاب به وجود اومد!
صدا و سیما شد ملک طلق
و منبر اصلی «ولی فقیه» و شد چاقویی
علیه دولت!
حتی علیه خود دولت خامنه‌ای! وقتی
خامنه‌ای رئیس جمهور بود،
رادیو علیه‌اش یک برنامه پخش کرد و‌
رفت گریه کرد و قهر کرد و…..!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=RipCCYDxm-s2TV30o9dzwDWvOIqXt1RRezF3hfQMNeLzm7W-NszKjLO6IX_LwCzMneYWzytSpKydtYJHM_E0M1zG45vd9qtjF52ZaKZaAduwektlEefuh_kHOOhMG0m_NsepXmF0VwnkL_R9JZfVBc6eZyJdSlTtochUi-QZm8iyUzJtrtWmo72AGoZ7NO6DRW1siEE49GokPC0zYZWUQ3sPWipq3emTbn_7SfDVAzPsY8ne4QLhRkgbFmnuY-K4YphiPFvroQkAYyOnXMoraQoi61sdWsEYVUXG-kydi8jAuYNM3gv2f1cBWSx4Pr5xqciH3aiSeIDNfaQQiX3Qvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=RipCCYDxm-s2TV30o9dzwDWvOIqXt1RRezF3hfQMNeLzm7W-NszKjLO6IX_LwCzMneYWzytSpKydtYJHM_E0M1zG45vd9qtjF52ZaKZaAduwektlEefuh_kHOOhMG0m_NsepXmF0VwnkL_R9JZfVBc6eZyJdSlTtochUi-QZm8iyUzJtrtWmo72AGoZ7NO6DRW1siEE49GokPC0zYZWUQ3sPWipq3emTbn_7SfDVAzPsY8ne4QLhRkgbFmnuY-K4YphiPFvroQkAYyOnXMoraQoi61sdWsEYVUXG-kydi8jAuYNM3gv2f1cBWSx4Pr5xqciH3aiSeIDNfaQQiX3Qvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6sRUgfRdndYhOks_GiWBu-B2LGfMhgnXtY0OCCOXGF4Zj6fpou-DYBy7G-KCO2xzODNp3ETM93U0pWbAuZ18-nzTRX5asgNSN--Q1NceQ-GOeouGVtBOqogB48sVTMoQgZZjKTdGv5_5L-rIn9LqpTTtnoQk-9fKinoVHT_kkOZVdg7n30FDVqyM5U8PkFeCAdJVl30WbqOE9u6WuEas4QlqQQF4BedZJDjTqEZN95l4hVEz4yF86Owu6WM2fsmV-9X3RsjREzUfyncBbMTR6N9rr_4ET1t6-VJWbrONCGRD5fGhkHlhtgjOVLPxmEyR9H92grv0ZqAB9TUFpGP9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=oNeAEXzDJ6_o67xxlxezFSHE4WFNvA_nOT9bUPe1UmcJbo95jAGXLQmQfbTLbuTuh4ALy2QF4VVnwpGckhSaltJjRE-715eIC0yxMvCH-ipG6dDj7nkt5EyL9Al3uOe9qV6xA6DjaU29kzY9v06cLJVQPsKVvmH3_aoAJrQpLS_BGO_M8IaEs2w07iUWE5N4CBrllRKU6wTbX-BJM5S80n2MxFMg5mn-e-CtWg5OYofKKz080GAW03YjJo3-VIazJQqWjqTgm00mxQvE8E1P6DcVuJrapY40i_dkFa1sB522aoxn1sRoYAsG7CDyUKnsncaF8o7J5M83iMQkHkc1aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=oNeAEXzDJ6_o67xxlxezFSHE4WFNvA_nOT9bUPe1UmcJbo95jAGXLQmQfbTLbuTuh4ALy2QF4VVnwpGckhSaltJjRE-715eIC0yxMvCH-ipG6dDj7nkt5EyL9Al3uOe9qV6xA6DjaU29kzY9v06cLJVQPsKVvmH3_aoAJrQpLS_BGO_M8IaEs2w07iUWE5N4CBrllRKU6wTbX-BJM5S80n2MxFMg5mn-e-CtWg5OYofKKz080GAW03YjJo3-VIazJQqWjqTgm00mxQvE8E1P6DcVuJrapY40i_dkFa1sB522aoxn1sRoYAsG7CDyUKnsncaF8o7J5M83iMQkHkc1aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در سراسر این رجز خوانی
نه اسمی از ایرانه، نه دفاع از میهن!
نه رستم تهمتن!
شعارهاشون اینها بود!
تهاجم و حمله!
تا ظهور مهدی «در راه فتح فلسطین» میخواستن با اسرائیل‌و آمریکا مبارزه کنن و حیفا رو نابود کنن.
نه در راه ایران! نه برای ایران!
بلکه برای فلسطین!
https://x.com/farahmandalipur/status/2080726571627774147?s=46</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfT5F5hZ5xwq_tn92E4_1v1eJdQvEIjEQjNZbY0YpBfHKhXagLCT9ctwy0ZZ0tDVuCN7RbGaCdyxVQol13XmhVp5fWCnbvNPqB6H1rCUQtwPbrrDm6T5fPaReOG6hDsVK_atNcyQaN5y_fqgID8ZmBLIikJAZFpeeBKwROH0_soDoXbPcfZ8LqtbI9zZHwLh7zgh9JfGR7sT5B-3HCaP2MXJ1qD4h2JB1IkrtlVaTtOQZEppdhu6LTchiBVfoAN0m9L46pm08AStaArwTcWHrlT-9i6MXsdHNrBmkTTYpzcEziWFcdGtvOAYxYtzvrDLCqC50laBEXdEHJ93uPO5Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lrc0aTRKqTdb9pcvNzElKG1M6nPdhpI0hgFxI-2FaJPB40lYqKLVHzES31MV4zuIifkDkFXdkC_JGK2lACYbYNGYQyiV3OkBKjP0wnUD3UDUMdRiYPNJGZUBTnSibBT_0pNVRJogzPWdW7aPB5Y6ZmMjNYX4DpYXV3p4rqoj4ERkwnZXvLNaU2xkdI1_hDru4vn90E9jCImP3ivSwkWz6snkuFHQ5pyUiXUWJrn9X2vJgv1PsEoDWJjz_rGlclOqxYODwClEdGiLDv3IUs7dTWviXXmwEG4N2Yf332nkZuoS-89llHU9_O5dfWfr66ZZJemaOPGf9_7tOkkdDpZ9HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=c-sOdimjNMuoR2pcC_SQQrEd4BaaPMtELRYJxMBBQ_TuoOgS9rXfglJsEF7ONt_KE5MdTqW-e-R2FzG--doHaOd5m1f2VriGOcsY3D99IwxgkPa_4hCc4m399WBqzXxi8WHnXjUc0a5vscvhwBccCh4nNEG1q1jWIUE-jSMfy1F-Q2hAXu-kgsgTOPHgxP07LLNyuG9wr3NjCiWgTl_SRVwepVoyXXiUeVza_r4eKMh9UlUUmKF50DkWMJd-c1GD7ifUGD7NmSfQz8w8aSe6NmoJ09C13o4bVcOTxgZ_aiuDEGIfiG4IwhovRGPR1tqNrjdAJDrtAjTFpTQ4FYZzXzOwBKNd84oLFqjVcwcFi9uE-E-23IxtZ1HbhwD4BpLmj0H_nx6w4H7HPXmkMzZeWkBeNufnw1w35AihGgbG0vWYSW1eNKs93XsEg5N4U5uSfvxgJdHUZgQCzI8FW8nuPLDHCDY_FHuoCNlTJRhTGgrhFNFsPc2kaIsT-otOSMTLJQC9kbKv5WLbQxvq27QJO1NEKp9jjZiVRNKOFWjbOZB3LALxtUs7zerLTs2Xg5IAb3RhP3xTh-K5_fYdo6-lYEKyZn-2vBkL9FcrFewZklua-pw47HMsZFXJAiUHxF_yvIbVvMYkmGVBUs_NcvEPcyA28JLGEVOAk8pJ2UGz_bk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=c-sOdimjNMuoR2pcC_SQQrEd4BaaPMtELRYJxMBBQ_TuoOgS9rXfglJsEF7ONt_KE5MdTqW-e-R2FzG--doHaOd5m1f2VriGOcsY3D99IwxgkPa_4hCc4m399WBqzXxi8WHnXjUc0a5vscvhwBccCh4nNEG1q1jWIUE-jSMfy1F-Q2hAXu-kgsgTOPHgxP07LLNyuG9wr3NjCiWgTl_SRVwepVoyXXiUeVza_r4eKMh9UlUUmKF50DkWMJd-c1GD7ifUGD7NmSfQz8w8aSe6NmoJ09C13o4bVcOTxgZ_aiuDEGIfiG4IwhovRGPR1tqNrjdAJDrtAjTFpTQ4FYZzXzOwBKNd84oLFqjVcwcFi9uE-E-23IxtZ1HbhwD4BpLmj0H_nx6w4H7HPXmkMzZeWkBeNufnw1w35AihGgbG0vWYSW1eNKs93XsEg5N4U5uSfvxgJdHUZgQCzI8FW8nuPLDHCDY_FHuoCNlTJRhTGgrhFNFsPc2kaIsT-otOSMTLJQC9kbKv5WLbQxvq27QJO1NEKp9jjZiVRNKOFWjbOZB3LALxtUs7zerLTs2Xg5IAb3RhP3xTh-K5_fYdo6-lYEKyZn-2vBkL9FcrFewZklua-pw47HMsZFXJAiUHxF_yvIbVvMYkmGVBUs_NcvEPcyA28JLGEVOAk8pJ2UGz_bk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=CH6ZAKFuKL4m09cN0v5p4bENNfm_HqGozGAe4Se4OvQJhRUGYSySZQRA7KfHc7poQmB5RoXTtmKN7deFgYDsIm8cqaAu-mFdyFl5VtLBgYMFmcpbKFXPAVYEqhnAC9GK-EL05AatKgG_EHOQLBOM7ukjtPVH8ynamEi5IG4sKHTCj3Jp9bP97Z-SnlBZwYBBJ6Pxaus3-5w1poZE5yzD27Ob5uC4ZYKhZEpLzPNimctBn8Iz0VY35yqI5MI-21reGIp7C0-PzrOSCtwHOggss7IVsJ8U3w67KtMFS-xH7PeXm83ImnVWjFj_mIM-whHIswU7JRa6aiGRdW3hUyV95g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=CH6ZAKFuKL4m09cN0v5p4bENNfm_HqGozGAe4Se4OvQJhRUGYSySZQRA7KfHc7poQmB5RoXTtmKN7deFgYDsIm8cqaAu-mFdyFl5VtLBgYMFmcpbKFXPAVYEqhnAC9GK-EL05AatKgG_EHOQLBOM7ukjtPVH8ynamEi5IG4sKHTCj3Jp9bP97Z-SnlBZwYBBJ6Pxaus3-5w1poZE5yzD27Ob5uC4ZYKhZEpLzPNimctBn8Iz0VY35yqI5MI-21reGIp7C0-PzrOSCtwHOggss7IVsJ8U3w67KtMFS-xH7PeXm83ImnVWjFj_mIM-whHIswU7JRa6aiGRdW3hUyV95g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRH_WHpGMnrgDWQF89Krovix75W1xTcgtPpRV-4q1SNywdDGRGQ7Vs5QcHCbLbPva8Mid9WhSzMdkhuJj3mDLNybx3qElfnoo5gtV00z7K3iZ97TJh6MKFZzw2uC0nAUTDuNplYqRF0xNUTYdIoBtDoFGmoZlOneGUoQ5ZWvMz-waL8yO13ppCEjF5KZH0mM6n63K94bTlnVZNGJFvGSADsyb1zIZilUfJPuIqX1c0D7OvNRqcUGKbJE-HeZmtVsl6vZKH2ERC9cPVYVwen3qUgu7cGSszhyK_4gOX7aI6vVLMDytXYqOjvIIGwKWYkKqzc7azAMiNoQsTWkx4XAXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=REJnCrCM7PASO4ldYeP7lnUm76mjZGaQNhJDKH9BwEid5Hom4o9w-tKoKIhiuQWDtw54phrSo96R3uSyDRQBVWHxX4JgzxIIVJUMnosbMJDl_PgDnD2Xvjsg63GOSEoCuBneRsfJPnvMjjtO4NSxjuMOV2TO_u0-FbLc7cikqblwKxO9ahEbdBC8u8PyGpj4oCy48UrAvLf3Rz20b9KXuE227iIN9WXJ9mphHU_ve6vmfpAstpaQfC88uMlnncq1HgiDsw5GBum2PuVuwmc3gQ9n6xnYHcH7RBuwCJjd6xitLrNVLOEF-4IJt_e1RLIjaFCpjPTRE2R-2EV7LwwhwzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=REJnCrCM7PASO4ldYeP7lnUm76mjZGaQNhJDKH9BwEid5Hom4o9w-tKoKIhiuQWDtw54phrSo96R3uSyDRQBVWHxX4JgzxIIVJUMnosbMJDl_PgDnD2Xvjsg63GOSEoCuBneRsfJPnvMjjtO4NSxjuMOV2TO_u0-FbLc7cikqblwKxO9ahEbdBC8u8PyGpj4oCy48UrAvLf3Rz20b9KXuE227iIN9WXJ9mphHU_ve6vmfpAstpaQfC88uMlnncq1HgiDsw5GBum2PuVuwmc3gQ9n6xnYHcH7RBuwCJjd6xitLrNVLOEF-4IJt_e1RLIjaFCpjPTRE2R-2EV7LwwhwzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0C-RE9hEvdQ-iYXpWE8HaB9xPAV0l2WDoGnfJO3f8LEaPxvpNVqpak7ZHcxfsleiwydSiZ0g3qpDgTBzGGR4i68Rct-Q1dR-YaSyxK3gqs8-v6nSIXLurQ_MRv4PzDzsjClM-7MHeHyGDSBv7RfQZ10xSHpzPG1IozUeySf-ADcHuJWeUrecyzQbL0AVAy0McHo1ObX_Fh6CDgMGTw7tFsqlPVjswYEsHqHs3Cp7zPV_hTH_GSot2rCGfD39iEmrypw8Hvd8xTseZpCFd5rZF1psWnkGkvhXy1aToeVpBtGUA5K04asulPIo-KgqmabgNqM0k0MDdL1-t-UhZHJvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c6c1wdROoPo6gH4mfU57AknhOTjq_DnTKb2WQ17GyB0tJ_7AziXLM59cwh89oziMHynXJIRHiUFSwd3hVcOD0wNcSbgo2MaCPZmpM3ZYJ6gSxbEovQwfxUDw98dCy_dUmeBAClhbiKRkmxlYHdEHCqs3E9e3yNj0uHiXdwNxWmkOaz44zJtG0chLHtyYkElLf8ztHE92qWIwAykhNXxSqaj71cNCOjIDwIgo9Qn5PR-C2e8_w2AagjZbw8r8ZVQP44_hlQK1RlyGugj9gkfbX4Jk33QCb8n6PqNvgZt_R1H_mtw7otSmlcjQyM5bJqDErnnUZVWFVjiEiggxUMC3Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMnA0hT91oyCAUWA8Hyjvrknh1OFncmKe4Z6nMXwHIfabDHtplK_BgMaxIELDq5-KatvTHVk6fsT5HYlh0kBd36pvNlB4_SEJSVIASAdir8x8FAddCHEE1H6rgl1xfisxYevniovWZ6WqPa6E_wh05YavJZCKet1c0rTMCxV6bik01ASytdVjhiIj-VaJzYsk4b4jrVCs5R0qdG-LDyNRlJepOOTedzfkJJwkib1YpBBRNtg43Sy2KAqvmf7uJbQ2BkNZVNERn6q-w5332N0YhBDFS_ZhhcGi_qvEmAm2Cv6rZyVqNHaEklXsVr0m4KuliSlwe95wq3uRxuoO-_TPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t27cl_VWZDCfnKRP1Elzg7lrM9h1EwOTkVAg_OKM4Ro8xJJq5JdmYARgHQxU1iaKzu17HGgZPsZRRtA7zcdDY6moLGydsflSRCnc4qigb82NPRW3FbCD03gb0uru459Pk4Jv2K43jf09ozAGY2UsccdPM0uuxo31u645g3UwjZPaTix5sBH_YNObcNz-nbjSKajqhanHaeYuMxI_vSt7Fjx_wFvEtyJjsE0D4Jj2bIuamr2Wm2tbFtf3VumJiwUX8UubTv0ry249W9bKuToXtaa44YRo5hcTwBHAUFakvHj8xc4uAG50OqRYoZ9Nul0xDqfXHnv6MseXDJTRHjxpHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Le-3y_P1gkpbgq_hAyrZuJ_G8IxOLu1PBQQW34GDeBAM_EuTJkULuvrEd_PI7T8ma7mlrOMmnYUF_P2Xs7MfasbfQWysVgEOsJ8mXrhA75aKKBKttbqDwrxtd8W46Y9Yak1Gn7lJijV8_KTDla4pD2VSKWR-cFf7or9QQMQlOCIA8ZVPUmPE1tRgvK4GR7uIfgELfsTQTb8WXeVW0syP8zSFAMkc6pc2yfjTP9nf1tJdnfiaNkrcjqGoKm1_A0UT2zANUBAhjJsKmmUdVfo7imlhyeqELY92wbJObG5iR2YLGDV9Dej-FMyACEOQw3rjXZN482VRaIdy-RGJVV6ygA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=LLQiv6wqU9UGghVJnVogwMb52zNeTWn4ePQsLw4g6sAylSVTlfY7LMs9XrFA440x4dDpjyT1LwNCkw2NCjXrsSu15uEj-DVqnr765FKhR91darBjIL2egzZ_7_Ms4kQrPV_-bQZj-BOP69K5TSL0yRZNaCwl3UqwKRRoJSWapDbaB-u1MMBNrFJ33N-eZB0VtveD-JbBnYsEXfwOoEKU45-FEN4nUbEdhBY4u_by_jLbMOXnLGikQ8tdM1OB9au-LgBiAIZS4HTOhUf7QmoS0jOlpjgCS9ItuAH5RQOqIs9wobuSS5FdiWiMQCgmr4cACCWrbpFdUKXFW7naRfdKnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=LLQiv6wqU9UGghVJnVogwMb52zNeTWn4ePQsLw4g6sAylSVTlfY7LMs9XrFA440x4dDpjyT1LwNCkw2NCjXrsSu15uEj-DVqnr765FKhR91darBjIL2egzZ_7_Ms4kQrPV_-bQZj-BOP69K5TSL0yRZNaCwl3UqwKRRoJSWapDbaB-u1MMBNrFJ33N-eZB0VtveD-JbBnYsEXfwOoEKU45-FEN4nUbEdhBY4u_by_jLbMOXnLGikQ8tdM1OB9au-LgBiAIZS4HTOhUf7QmoS0jOlpjgCS9ItuAH5RQOqIs9wobuSS5FdiWiMQCgmr4cACCWrbpFdUKXFW7naRfdKnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدال لفظی دو نماینده مجلس
بر سر تنگه هرمز
(پشت پرده دعوا : شهریاری اینجا داره میگه
که تنگه مال ما نبوده  که بگیم میخوایم بدیم بره،
و میگه تحت یکسری قوانین
بین‌المللی است و زمان جنگ می‌تونیم ببندیم برای فشار آوردن و….. ولی مال ما نبوده)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtFt74SJW-68dzzABi7jcsSpc-eHR_z94WxG2WeZN4J2QiuX6i4sgq7lCWarNBRFhXA6NDK4x_adFhy_4PZTcPjLOVjgLgmnJc3ukftKknioVCuz1dCv89yhlgTOb-mmz47-x-aUyuEhQQFvp31gdIKkmGukEA8IhVgyFqF5UuXx2kusgY5q6aCx6NvJTOxKwdQizT_0N7joxW9yzNpVdHrULGnOIRwoBCIjocPhUGLmf-XmcJ079R5zi5e6QdD32kvx9MJeL5dkxTFIoqzDeEFaOajROS-touwqdpPh6Kwtw3y3LlghzjFsXm3FxZPsMJ4Ue5bILBND01o3n2w23A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rO2TsKF2kPwzxsLRQJInmuCUnW-y-csMeYUxp3F3U5SctG3KDP4QEo4bwsWuh_GowoSrobxIr0sWenr03yXbyEU6Epj0ACRB5mvsyKGjtly9XOmO4Jjjmpax8Z4jNt2cT0H6FuIdTwIjpQ4-kuRtC22FyCoHZIoER-g0g5qBx9LL3j_81FfP3_nxJcQQrq--KdlEe_65_UoRrMqeXDU2ECJMEeJnQOtA_QdyxHdLd7UOK975X2lcdzLV_AAH3Hh0UEYSUqaUFgXO9mlXEHIsoJ-ld_iQRv9PYih9VB3YvncZSpBzPtZe6jACzI9Et95QATdl4MfHwxq4517NIbQnNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=QWpE2S1vf17bZyVbtHbN1Td5nA7OPeIYj_uXH6PaDKeutyD-g1pAoTWiAGzeMP8r8fvGKBqHK1h1F_aRdEehoToq5wvWQfnds-hQU4wGnJf4WOFCNIUr22QhyT9NWDgW5FmrpsN2937__Hy_zN4WXc2a--p3XQdesxH0I1gURIU_l_zSqRM_5etNSfL2DRoDX7DOtGPszcZXHZnkZrq_Wf4zlip_dOwqyP8jJ9iSJpkGDD56wrIfeEc82yQWyXAmzv-JzVonzgZSD6kStQqaGkSWoh9W9sjelBwJVS9wfecMwWxYYnTj1S4O3tc3mE2-c3J2JGZDxMKOQyybZ_7-zUiLgYk2g_Qh7OYECW47WQV_vaz9y67gMyHCQ3YIkeoxEUcdmcfE30zUR-ULnOvEmkgJVqMSNz1-dICsDB4MOYMzqvV8Z-kKPVU-bTVfsW3HiyM4tEi2slIqC05PBsqKMAw4nYuqYI7siMpt4es7gc5sRYeyu_RXA5pRaKY1NSs6K_6LspP2sPopWP4GTCw4qdumgIAUA239HK9pyvMiHHF0qpO8lCIre6buMaFvFQA05MLbbRNGIroNXTC6t4VXg4eFtbBgw-M1GLrt845jvpSTKQnDSaNK1MwAz0UhMiQAWyfqy6T9fokmtSXORkL6ASkbFHGLkFi0KPx39YcwXkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=QWpE2S1vf17bZyVbtHbN1Td5nA7OPeIYj_uXH6PaDKeutyD-g1pAoTWiAGzeMP8r8fvGKBqHK1h1F_aRdEehoToq5wvWQfnds-hQU4wGnJf4WOFCNIUr22QhyT9NWDgW5FmrpsN2937__Hy_zN4WXc2a--p3XQdesxH0I1gURIU_l_zSqRM_5etNSfL2DRoDX7DOtGPszcZXHZnkZrq_Wf4zlip_dOwqyP8jJ9iSJpkGDD56wrIfeEc82yQWyXAmzv-JzVonzgZSD6kStQqaGkSWoh9W9sjelBwJVS9wfecMwWxYYnTj1S4O3tc3mE2-c3J2JGZDxMKOQyybZ_7-zUiLgYk2g_Qh7OYECW47WQV_vaz9y67gMyHCQ3YIkeoxEUcdmcfE30zUR-ULnOvEmkgJVqMSNz1-dICsDB4MOYMzqvV8Z-kKPVU-bTVfsW3HiyM4tEi2slIqC05PBsqKMAw4nYuqYI7siMpt4es7gc5sRYeyu_RXA5pRaKY1NSs6K_6LspP2sPopWP4GTCw4qdumgIAUA239HK9pyvMiHHF0qpO8lCIre6buMaFvFQA05MLbbRNGIroNXTC6t4VXg4eFtbBgw-M1GLrt845jvpSTKQnDSaNK1MwAz0UhMiQAWyfqy6T9fokmtSXORkL6ASkbFHGLkFi0KPx39YcwXkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=MsoEggnj-4MPqm3ItKwev5CYosulxsx6VWmCrjeKpTjVToLAQHMNLisWj8rIyWcjtXU_8M9VEvU3hDv3g1aFezX_fblVjblbJawgrWNqSudXysUK6YTLw9tiScOZ0OsMLUjomwQ5DKU0al2tgkhQ9NKc_2Z8rcZarUWDbcyvsLVqAQZcJyLCv77BCGyPrNu_dEtC3p8iYVNUICDbYRVTWM51to695abDpHsNtWBh5srA_K09CEHFc5KS6ilPpw6Cqyi5HmJYkalidY6j0TJ_mf501K7jBXHVvEHifYRi3QF7gQKZyAOisUQM8EYXQhtkuJT-1v0xEyxTjL2oLV21og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=MsoEggnj-4MPqm3ItKwev5CYosulxsx6VWmCrjeKpTjVToLAQHMNLisWj8rIyWcjtXU_8M9VEvU3hDv3g1aFezX_fblVjblbJawgrWNqSudXysUK6YTLw9tiScOZ0OsMLUjomwQ5DKU0al2tgkhQ9NKc_2Z8rcZarUWDbcyvsLVqAQZcJyLCv77BCGyPrNu_dEtC3p8iYVNUICDbYRVTWM51to695abDpHsNtWBh5srA_K09CEHFc5KS6ilPpw6Cqyi5HmJYkalidY6j0TJ_mf501K7jBXHVvEHifYRi3QF7gQKZyAOisUQM8EYXQhtkuJT-1v0xEyxTjL2oLV21og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCrU-ET536H2OA0BrHwoeT8L3kLTz1krwfMBb1bwIBGnwK3FFJlAsvvzTMcjzUB53Ri58Of7C67_VaZCbDQHYV3U3Uj2uGRbwuDHYKFGss7w7JVR445eS2WDbeKa7O_Bt1rNANqpA79E_-7rqvHSp8XLsPyGH23rZIzu6U--EITQu7L14ha9AMkLTt3_7KgPxKQ32LZ45tfwNcjF_JF6RuAvMAPfELcXEj5HGKVgN209fsYzXDMPVLDdjTb8nlnQ_xfczt3sWiIm5OZXm5H05E04UwTACDSKKBC7fNCVIYM2bp0s7BraNb8qnh1D9v9dC98DE4uFEMkJeZWFEt36aj5s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCrU-ET536H2OA0BrHwoeT8L3kLTz1krwfMBb1bwIBGnwK3FFJlAsvvzTMcjzUB53Ri58Of7C67_VaZCbDQHYV3U3Uj2uGRbwuDHYKFGss7w7JVR445eS2WDbeKa7O_Bt1rNANqpA79E_-7rqvHSp8XLsPyGH23rZIzu6U--EITQu7L14ha9AMkLTt3_7KgPxKQ32LZ45tfwNcjF_JF6RuAvMAPfELcXEj5HGKVgN209fsYzXDMPVLDdjTb8nlnQ_xfczt3sWiIm5OZXm5H05E04UwTACDSKKBC7fNCVIYM2bp0s7BraNb8qnh1D9v9dC98DE4uFEMkJeZWFEt36aj5s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XL3p1xuHBjsH6GdjMF8W1TG-uHtVYZWTkKIKK1JCbRe6uNIFM41PEGB6nrdpH-psGeT67sHYmKzmHNPKTvYurSu0SCega96a7mUsgTFTc6nev4kGwAwbKNOFQL5nRRKLiKCPt3mpR1vkgILsynJqy0AXEI1Mk9F_VYvJG3qAs6KSFAdouv731P03HyPtRUzxW_SWHrCv8YJ0hyKADvTUn6ml8WhE8QUZazQpYZSD4ff7w_5g80QjGgXi61pOhG0plKll7xe6lFc3ZD357_gEfMuDSWwIIeQ4DeppD0fMOMIWOSuJo6IV8kBUvS32EEw0kkHFDkxq1WthnLljhQZstw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzBtOdKA2pZU7EC_foZxdcMzUJ_OXyZktXMlt2xGEYGmf5gb195Ed_uNKDGtyl1v5beHwGKgdB_bak1-XyXLU7G9wBiHNNbombTr00sveLa0G6TvS95Xi8-eBiRIzGCoKeOJVDsffm_MifNDVhwowWVXpN1j9t-s8bJ_cZZiLPysWd3QEox4h7qTvR6MeU6p8yUmRQQh-dY6gUmh9KxwvOVGbA_pik0eYFiYRB2oTpDNPfeXBsqCbhoUXunHuCyWggQ_Q7yHUNDaYvxgDR2of02_wXO0gMfmTK7i0JLHvYeZeciy_1tN_qOfrvcP2rLRU-4wooOW_Aul07AvKEf6fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4lx5Eb_aD1s5qShsOX7Z6sHUKl9Wc9TWo2lyq1A8ssyIPIkYTfEIiRrq7KDOuMxOSsaDVuTU07q64hI5vE1bQbk5o7xc08tw9MVf3Tn3imuPwf0twPqEo8R0AaPncMmufmYU-uTPpTz5-a_qTsKNMoWxwi2-iSN8RSEiQ2IDjhYU6mfHJxPCz-AIfFCiRBNKCm6RkU3RKhlpAsxCUbjynmNA-pOUG0K0f5-B21_vYzSlGuMRPqJ8PtHrwulwEo185SOiAMBPvuLFcPg0dUW9hTQLezbsnpDjemF3w-bBHSE8x835blSjEX3E896YisMItQmlip8NfHR5cyPh0JdGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=M7C-9DTsjGnCqjwTjVPmDBbpX3s38oYlqHKMIf4Sq17zME3U3r--Lbh5Wjzq7WGkquaKOTTAD4or0cVIcKWI3N_cG0A1nfnSBCCgQoRh_Q0sCOgq98dKXbKqR1hWTsh1IH5EGSSRiZDtPGBMR8Hsqvlx60OIY8p9Ti6k7YORT1JuErKxH3wDhY48brfSDsoeonihXJYfEAxjDKSZ_fK-Vx_d6WCu14hIc7U7phdvFcHxTfxgA4CmnRczbmBuOQfso6Ei6u_wPJqBfudVwq19WBMQ8PRPEVx6of9IqoSa9EBkIbNkg6FG_4YHmlt_xex8zCF1v4d8zkOaT-OHqx0aTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=M7C-9DTsjGnCqjwTjVPmDBbpX3s38oYlqHKMIf4Sq17zME3U3r--Lbh5Wjzq7WGkquaKOTTAD4or0cVIcKWI3N_cG0A1nfnSBCCgQoRh_Q0sCOgq98dKXbKqR1hWTsh1IH5EGSSRiZDtPGBMR8Hsqvlx60OIY8p9Ti6k7YORT1JuErKxH3wDhY48brfSDsoeonihXJYfEAxjDKSZ_fK-Vx_d6WCu14hIc7U7phdvFcHxTfxgA4CmnRczbmBuOQfso6Ei6u_wPJqBfudVwq19WBMQ8PRPEVx6of9IqoSa9EBkIbNkg6FG_4YHmlt_xex8zCF1v4d8zkOaT-OHqx0aTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TS3Zxdtc82YQ6H6Sm7BA-N6LM8CzacEnPTPM1bKy9sdUcSghgqVH6---vd1CXNS6njbnShJovoCRekNtUa3GLRdLf3RsXeV4JDeCWPh28WEkq39OAhhrm79GpRVJYUgAn60OVV1A7y1rkW11pxOE-gUczssXL-JIvNQ02jt1PycnXc80eZ9k0c7p66DnEV8ImJcXF5MXeDV8k5GwhGnSXL3kqqFItEUVR-pjun2bo8wwTXXupyqY4kjJJVzbk7G576-4fzuXnQOKEsptXHRxUHnFJrlFofl17xGvz8NLRckws8dILmDcSGHICp6oO-fCHTMnxQlEtoSoZQyc8RoZZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d4zvzCO9eNQcRA7ub7uq9HWKOLF1aFmD2qvdV5yoQkA-DUIckbymAQm7rZrH18FrP7eV1luOcGS17-TbqeULhepUXGbUlGJVx0SsZYFDveczxpnExWgA7RzTV7bu39VdS709XNiV8pru1aWjKLnyB8gnHVHSXi62bCsrUrydKnZxGTQORARSKzauHJgNmZIXfA98TBX2z1py7Uol5IH4YBYsAgjmq1APDdS3butKnbPy-S1OJEUNpUttn9VS-80kBx-0_2rLIgtvowgY8U6XLlpONKRZkF0P3BDKG0wg2Q5Z6kIq61Uh9HNm3vjHWoe2P_tvLLYaC1xrUHUUqPkNFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YbJqKfPrWgIrUVXt2yQwRNbapLyx9Zp_0w5YrDZXsp4fSsgCppUnhPeko9CxuKb5XYw7hxV_vkCXKPJRinP2PZCRkk_kXVfnGPzCHFHmqApU3Ze5SIFuiiIYn5K-GNZjv9HuYLqGEHchp1o21CImMkkWkj7C_FNeLrhaMMr_Fh-YkJXHqw_cbY_CTQnsUMJU0oNjVKGWT18EMq__G2jhRmh0z4kmtZdOJT8N-pk4wnteBBM58zgDXVe4h3mAHDZMF1isx85KHNge5Xg6KzCNCzOwrzq-ThsVtMwD2FHHodDl0aYoP_Yr4LiAPzUFOKeSN30-uSks98XJp8Hb3pSLVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jujm-p7ZXpN35S1JXLaQdiXqrLlXCmdXTr_aTnqV-A0DpuoAT7ODbF-i-o7_uS2LBTYNkRjXjBvCmwzYbspkDJBrk7uMyuTxjoVdwzSST4GUrLpYFBlc8-CkIcpkZcLNqbtWdtfenft0Ro_jeWru5TPh7gLxglvPEjqOXZ71lZWPG6KYW9qr7kquULKsEqrjQe-hdlJAjGbxWy6sYzXtdGQZsjLXRH9nw8o8J2wTARRBZMzo_WMNenkV2Fen_nbxIgc1U8CWfwlc77_Iublju9poLW6Fn3zjk90Ub7oOyNl-ARNiVhhjbFcm6wUaunDPugDBmXvND3p3A8P8MkSKKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=G_zP2np5CsWJ69rS2s-MegbuwZlhmwaK3B2Gq99Z1tMJSJ9LTGJSyNP7jBV-s_Tgft11gRE6maAvDlMwLAkl3W_bBupRm_LFB-CzOWowxMycKQd_fBhImtgbf7ZAqvEEx_ZoKj0sr6T3mOPTQujlQsfbnZZ42QU8zAEYtO7G0XR5dBL1ceq7KeitFLqeBq325tqWMyrVjA8a1X4S4fZ0GiIZbabP7_2bZPbsbilBsOXR-dzvwikYuFPHj1UD7PZ_SmyofJwhY3VrkaQnnIl10ubvHI_BgDJUOTahZwstfP0uVEDpcJdspEvd75JW_tZAcoTAi5ZUaMzcra_2RmIG-YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=G_zP2np5CsWJ69rS2s-MegbuwZlhmwaK3B2Gq99Z1tMJSJ9LTGJSyNP7jBV-s_Tgft11gRE6maAvDlMwLAkl3W_bBupRm_LFB-CzOWowxMycKQd_fBhImtgbf7ZAqvEEx_ZoKj0sr6T3mOPTQujlQsfbnZZ42QU8zAEYtO7G0XR5dBL1ceq7KeitFLqeBq325tqWMyrVjA8a1X4S4fZ0GiIZbabP7_2bZPbsbilBsOXR-dzvwikYuFPHj1UD7PZ_SmyofJwhY3VrkaQnnIl10ubvHI_BgDJUOTahZwstfP0uVEDpcJdspEvd75JW_tZAcoTAi5ZUaMzcra_2RmIG-YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🚨
🚨
ترامپ: قطعا به زودی و با شدت زیاد به کوه کلنگ  در ایران حمله خواهیم کرد و هیچ کاری از دستشان برنمی‌آید.
‏ترامپ در دیدار با رئیس جمهور لبنان گفت: «ما قطعاً به سایت جدیدی که آنها در مورد آن صحبت می‌کنند (کوه کلنگ ) حمله خواهیم کرد.
آنها به دلیل سلاح‌های هسته‌ای در این وضعیت هستند و سعی در بازسازی یک سایت هسته‌ای دارند.
‏ما به آن سایت ضربه خواهیم زد. هر سایتی را که آنها حتی به سلاح‌های هسته‌ای فکر کنند، با قدرت بسیار بسیار زیادی خواهیم زد.
تا الان زیادی باهاشون راه اومدیم!»</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=Tm4EAXCQbN-lATl8ruKSM8XxH81tySiYodi0obJAEbMTGn1xAV9VshazxRm8Betrv_wlh-liDLEgVCoXcAfPMA1CcXrVptqUaN6vwnTqfoNN-7eOfYJ4VQbJHTfKoxyhGYBlDiAdKaExFlCHkXAoxB9UIo9LpUSgkxJbO7DG9zo5vAqzpAXt_wQe5xgiduEFmijy0ePv_sZ91X7rQpaNKWNPbshzjAKcs5k9UNFj4avHyjIvJndl_ZiPEhQMzEMXGQ_ELQh4HDg10gOs29sy-0MmimNwoaWpF3vTlYqWYWAuBk27adMRgy-T54z15dnOHtf6ivlW5oFnIazB-t4rhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=Tm4EAXCQbN-lATl8ruKSM8XxH81tySiYodi0obJAEbMTGn1xAV9VshazxRm8Betrv_wlh-liDLEgVCoXcAfPMA1CcXrVptqUaN6vwnTqfoNN-7eOfYJ4VQbJHTfKoxyhGYBlDiAdKaExFlCHkXAoxB9UIo9LpUSgkxJbO7DG9zo5vAqzpAXt_wQe5xgiduEFmijy0ePv_sZ91X7rQpaNKWNPbshzjAKcs5k9UNFj4avHyjIvJndl_ZiPEhQMzEMXGQ_ELQh4HDg10gOs29sy-0MmimNwoaWpF3vTlYqWYWAuBk27adMRgy-T54z15dnOHtf6ivlW5oFnIazB-t4rhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=CVU5n5LwV9zv5AHphmjpPtnsqgbuPTNBv3xlOGHZsrGBrhqUYQyHQaDivU-Cpizr63IBVdXIaRe4cMZgPm0wCXO05LPzPaKOKpv8e44WudURDszzmsr7zxJV3gDLRmUQWdkFikEbaxUmdQuOg0SuKSwDoMr5NgQ6oGdkMl5bNhyPEj5TwoMg9XL-0xc8h1-JNhAH05TIs6DN-V-48UxG9LnGkQIkMctTfYFpC5NKOQEU39VahtQJDncXl8iRwYuslU1E9vQ4b96K6gC88-E5pWIJAuovTCtau88cek0mWMuLORVLUN1p1BTaeLkGgkswrZxjBlc3d2YhyVkW1GPc6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=CVU5n5LwV9zv5AHphmjpPtnsqgbuPTNBv3xlOGHZsrGBrhqUYQyHQaDivU-Cpizr63IBVdXIaRe4cMZgPm0wCXO05LPzPaKOKpv8e44WudURDszzmsr7zxJV3gDLRmUQWdkFikEbaxUmdQuOg0SuKSwDoMr5NgQ6oGdkMl5bNhyPEj5TwoMg9XL-0xc8h1-JNhAH05TIs6DN-V-48UxG9LnGkQIkMctTfYFpC5NKOQEU39VahtQJDncXl8iRwYuslU1E9vQ4b96K6gC88-E5pWIJAuovTCtau88cek0mWMuLORVLUN1p1BTaeLkGgkswrZxjBlc3d2YhyVkW1GPc6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">در مصاحبه عراقچی
حرف از تونل‌های زیادی میشه
که سران حکومت به اونجاها پناه میبردن،
سایت‌های موشکی‌شون هم،
که همه در پناه تونل‌ها عمیق در دل کو‌ه‌هاست!
جمهوری اسلامی فقط برای سرانش
و برای موشک‌هاش، پناهگاه ساخته!
ولی برای مردم حتی آژیر هم نمیکشد!
چه برسه به پناهگاه!
اینترنتشون رو هم‌ قطع کرد!
خامنه‌ای رو هم غافلگیر کردن و الا
مثل جنگ ۱۲ روزه که تا دو هفته بعدش
به «کمین ‌گاه» رفته بود، به مخفی‌گاهش میرفت.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3GL7tybnvMlE9BbCeFp3fqNVQ7U77LtYev22-FBZp-eO42E81YWrNl-723Q1Nsv9gnRNqgPDGJa2rZPRqAEBop11TcAAxyRa09GzJz1kqaKLf9zZqZdawNltaCOw9YwRLmNGgbQ_4mA2r9MOAPVEiCl4aNHZd3c_M0QnLkNV7igYElxkhaR6l6mN2eVWZc8DDzA9ijMIQ7LIn3SL5LnRYCjzSc4KDItQuuz6aVdYjgMEymhlDeQhMg_ez2Ay0OlXyZR60cMFmE7klybP6qR7cPllaKW97XzMx2N3itD6jk5aI1s02efSBU7Ie7qvn1eEUOm22te-2HepmxS6HlNhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=b971UAfX4t2FyTWDvWXwWdzvaMqiHIbLB_kp32JLaWDsHQYMB3nBJfxx1cXBXtdRU4hjLfdDtxldbAFcZ9YJBvTjaFBZ7WfMeZ03wGRF9lBRdfDL1I6Hz1cCVzmk1uOoNVYWJQf9qEusB5zy2e4-UuzdvIcoMjWwZbXgnSy2Cum4Be5GngwwM-qQVEYW8h6ciK1JFHJbWcHewO_K7eOOKVJKk9sbJTdSUCH6R02cKFfO_NGLNIB7TWPLiPY0StjwFLLalV1qkF2v0wg-k9KDsf-78Nv_kSgdos2TWqRB4OdkUbTEkn8TY5phhl_60CfJEvIQMzV86j9TMBnNs3qdvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=b971UAfX4t2FyTWDvWXwWdzvaMqiHIbLB_kp32JLaWDsHQYMB3nBJfxx1cXBXtdRU4hjLfdDtxldbAFcZ9YJBvTjaFBZ7WfMeZ03wGRF9lBRdfDL1I6Hz1cCVzmk1uOoNVYWJQf9qEusB5zy2e4-UuzdvIcoMjWwZbXgnSy2Cum4Be5GngwwM-qQVEYW8h6ciK1JFHJbWcHewO_K7eOOKVJKk9sbJTdSUCH6R02cKFfO_NGLNIB7TWPLiPY0StjwFLLalV1qkF2v0wg-k9KDsf-78Nv_kSgdos2TWqRB4OdkUbTEkn8TY5phhl_60CfJEvIQMzV86j9TMBnNs3qdvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=cCrwTxVStJYNvvLUIgu80eJRkEzjJu_3dgsVjMZp-j7ZRjIfm9XwMzsWBaPKbYl76m0S7uraWF7xyNnTng24aBAySQ074O4cClszNWVWeKsInqMT6aFwo6jiz96sI4_a7SZhXsNs1yxprL5fsOvlwjEZ8sGg7bEIGe-m5gvdLGuJqYduvT0U108NV8f0Pe2yZMq0InmwA6jx0UMBlLOVSPGBXndoxp4dOibbhA7EWfobT1IaZA_A7H1Gg5Yf1wusgrZ5y1rGX3Fhm4MsKIAVichWeLW2gT8vgQtjnkHOg9XqMQbqWGiTcJhOVxHwRT6L4xj5MQqZ3rC7J7L-Y0xhMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=cCrwTxVStJYNvvLUIgu80eJRkEzjJu_3dgsVjMZp-j7ZRjIfm9XwMzsWBaPKbYl76m0S7uraWF7xyNnTng24aBAySQ074O4cClszNWVWeKsInqMT6aFwo6jiz96sI4_a7SZhXsNs1yxprL5fsOvlwjEZ8sGg7bEIGe-m5gvdLGuJqYduvT0U108NV8f0Pe2yZMq0InmwA6jx0UMBlLOVSPGBXndoxp4dOibbhA7EWfobT1IaZA_A7H1Gg5Yf1wusgrZ5y1rGX3Fhm4MsKIAVichWeLW2gT8vgQtjnkHOg9XqMQbqWGiTcJhOVxHwRT6L4xj5MQqZ3rC7J7L-Y0xhMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=k5_IHUhNyA4JOKhvE9Ir5D6W_prhPSx48khZB0rJeUjucYzHRQik6nYWRgow99o8ZdXT0va8lJzZDiIcc5oxyhG3eXOJxblRaN8oV08-KTurE18ZkuNcoc_u3KMlZLQY9jQxj1iVGYRw6xzok40EkIuAPrj4PuDopEdLwMx4GaQlSUTjElL-iEz4ZqrDLc7e0FpTLN7ARkAr_nFJRYRVCRhElBNuSsntTR6X50DSt34VeDmRZj9Vm8eCrZEsicr_054QFABM9dfIKXAbie6YYv__drzkk7xWWEYVSELYOOe2rTkRydBC2m8fTR2ea76jwUwxF27cMDZSiGYmlTDNVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=k5_IHUhNyA4JOKhvE9Ir5D6W_prhPSx48khZB0rJeUjucYzHRQik6nYWRgow99o8ZdXT0va8lJzZDiIcc5oxyhG3eXOJxblRaN8oV08-KTurE18ZkuNcoc_u3KMlZLQY9jQxj1iVGYRw6xzok40EkIuAPrj4PuDopEdLwMx4GaQlSUTjElL-iEz4ZqrDLc7e0FpTLN7ARkAr_nFJRYRVCRhElBNuSsntTR6X50DSt34VeDmRZj9Vm8eCrZEsicr_054QFABM9dfIKXAbie6YYv__drzkk7xWWEYVSELYOOe2rTkRydBC2m8fTR2ea76jwUwxF27cMDZSiGYmlTDNVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=bohD1Izm6nytZewB27Lx98N-8DBp1w3K2wNJNlAqhBGvGp2zqwWfqp_Jp97pzICZitjDe3orfuvA9m1dVeQVma1Nh0skdxVpNDRW42KnaQNJf_5Snpha1KyWnr-U9abejxu-qXoC0OpeHZTEuG5TD9kxL5Jfl8awlIG9SnoqOLBOvSVX-M-BbLxulumQbrGOfLLNSFftRnRRcTrS74xkpgjbC4PAVjM1cjQdGZ5KqyB3uGa0rFgk2RQ9LQ8FR9xeMw_xL8IMz5cqtJDiJLkRbVLJj9DcEBPlGSRGXnLosFfsC2lrww2z4SMSg3ZIwPr5RdQI_DKeWb1xn4HAG2QizFHVQmdi5i0Fok_Rt1AavcMTK6aY4xbOf7-zGFMuFzQp80op3S6kTXOgvsKyrKYfMqsv6XBthYUcsL5DB_6yZmndd0q5QbPbjmp8wJ0InLn3FE6OfIA9OTC0rsc7fC45w38rIsNQfGQdW2JhYV_NZy0PiRAL4ZL3l7d8XtR_KM-1BnkcpaEtq3N8S_FqkgzD_n8rgwdGVHH44NlDnipLnsuxMJwfEQVGKZ1Cd8BITxcNUVfyJNR9J_hjgivowhloosNTJznkzwjXEqa7GtA0hL4heqjeVugz5ABCF44wDlVZxS_8sCubOOLqvMdzK6od_wjKDH-ugvHsHxoVmnBtDjM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=bohD1Izm6nytZewB27Lx98N-8DBp1w3K2wNJNlAqhBGvGp2zqwWfqp_Jp97pzICZitjDe3orfuvA9m1dVeQVma1Nh0skdxVpNDRW42KnaQNJf_5Snpha1KyWnr-U9abejxu-qXoC0OpeHZTEuG5TD9kxL5Jfl8awlIG9SnoqOLBOvSVX-M-BbLxulumQbrGOfLLNSFftRnRRcTrS74xkpgjbC4PAVjM1cjQdGZ5KqyB3uGa0rFgk2RQ9LQ8FR9xeMw_xL8IMz5cqtJDiJLkRbVLJj9DcEBPlGSRGXnLosFfsC2lrww2z4SMSg3ZIwPr5RdQI_DKeWb1xn4HAG2QizFHVQmdi5i0Fok_Rt1AavcMTK6aY4xbOf7-zGFMuFzQp80op3S6kTXOgvsKyrKYfMqsv6XBthYUcsL5DB_6yZmndd0q5QbPbjmp8wJ0InLn3FE6OfIA9OTC0rsc7fC45w38rIsNQfGQdW2JhYV_NZy0PiRAL4ZL3l7d8XtR_KM-1BnkcpaEtq3N8S_FqkgzD_n8rgwdGVHH44NlDnipLnsuxMJwfEQVGKZ1Cd8BITxcNUVfyJNR9J_hjgivowhloosNTJznkzwjXEqa7GtA0hL4heqjeVugz5ABCF44wDlVZxS_8sCubOOLqvMdzK6od_wjKDH-ugvHsHxoVmnBtDjM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=enuXyMmP7_HwEylNCLXgXMitn4tVna797caO-E0nysERSbhZy6A49KZr78QNF7ccuLQdmiU5VWwR5JWfJfLiRe2f2ZPQOIGPvlXsA-K2Ep0Sx0ZuDxCGxKlnC0XMdvhq0M9FD1A0bdJArKZdSuHhngbO3Sja0ztgERhHJehXmLCWDRfw9o7-KQhGS5nipwWh4wi9f40lFb156M_IZefbHOiXfkJxhhdKAffeVknJMe8715Pw3x30NtLn2cBwN9MV7dDKSYxdHKWGUHWv73wNggzTl9JOlOg0Uk4Otxl7AQcUm9Z2OT4c3L3vdcF75rQDDZdnw_SP3d2BVi83nzBMhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=enuXyMmP7_HwEylNCLXgXMitn4tVna797caO-E0nysERSbhZy6A49KZr78QNF7ccuLQdmiU5VWwR5JWfJfLiRe2f2ZPQOIGPvlXsA-K2Ep0Sx0ZuDxCGxKlnC0XMdvhq0M9FD1A0bdJArKZdSuHhngbO3Sja0ztgERhHJehXmLCWDRfw9o7-KQhGS5nipwWh4wi9f40lFb156M_IZefbHOiXfkJxhhdKAffeVknJMe8715Pw3x30NtLn2cBwN9MV7dDKSYxdHKWGUHWv73wNggzTl9JOlOg0Uk4Otxl7AQcUm9Z2OT4c3L3vdcF75rQDDZdnw_SP3d2BVi83nzBMhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=JuiuLtJRAD5uuLnFQzS3bAc4zHzGH8L282tF3Q0Jkmm5ylSB-jzFyOgvxr53p8yWqvNr8kmj-XHSruVH0mopGB5S5-9vJcV0bW8ioDoHc4UVQC43J4S77yucmsuZXMQkEg2qwB1476JAjwo-6JromJ0KHpugazUxv48mUXJT8iTL4hDZ2b2TGvjroTjhE8DXi0EuCWvxU7HsQAZ1PhS8zRcuZlmLqODSNlLTInDr06REX8m5ks2NXZDvSOfRBeLRpuV6Dm42KotKzCon3PZ8YA2w3khuxqCJuhzaoTn2L6NIMHW3VMq-bO1ZtdLAU3_3Kkon7UXpfpYXR9bokTxWkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=JuiuLtJRAD5uuLnFQzS3bAc4zHzGH8L282tF3Q0Jkmm5ylSB-jzFyOgvxr53p8yWqvNr8kmj-XHSruVH0mopGB5S5-9vJcV0bW8ioDoHc4UVQC43J4S77yucmsuZXMQkEg2qwB1476JAjwo-6JromJ0KHpugazUxv48mUXJT8iTL4hDZ2b2TGvjroTjhE8DXi0EuCWvxU7HsQAZ1PhS8zRcuZlmLqODSNlLTInDr06REX8m5ks2NXZDvSOfRBeLRpuV6Dm42KotKzCon3PZ8YA2w3khuxqCJuhzaoTn2L6NIMHW3VMq-bO1ZtdLAU3_3Kkon7UXpfpYXR9bokTxWkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ju6I9bW7cEcPgOjY8TZiHa9nlVvV-b8ggUMoGZ-5LLD8UCJmXmCw_fxi1zTmBOmF3Wc5oYAmvhVsQWKxmz-D6ZV3VE2WcDyyA5HoDi72Ee3kK6mm0zb8DzwhON2GdVNa8ijOe-pPLuBz8rrihHY4PkBxtwv0H2q2jjA4Jq0PD4APwLelEADIcPdSzes6Yn1S4dGLMHPOWAuUZs5KYBIFBv0Bh2jqkl118gOwwfcAEQy7Q66T04cf1QvKDTfPQ2gfxLnUBzoF5aqzfyj5JK66OKh1dpMTokW8TU8kplpISpiGIAa7VME63g_vAryQ4hVD2Rtw5nIYk89djhHnaaPidw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLu320sy6dTkvtPWw7cpsYhlKZ9dLWkQWHzZ7sXWYUDrAgbBOLF-IyeL_gJ4jmVeje3mIaknUW7ETxEhvIVUCojapi6aGSFnXeVmd_J9vapYqKx-Gg84kxAj2uQQu1EA0NK5By7r-AHLHQ9e8YhtKVj6QJENahZxQ3fuAxQAckoG0IcwBaO3nxuBW1KYAUfS1wQMMaknjRIMXJKxIy_hNPg993Ad3CgkrYPqK8yam7Xho8K3JCdAcwOx1pkZGpTTfd0SqUGLQkLTSm5hKAmW_M1J1PS2QK2gdgqZZk8MrSHHfo-knJuwrVaol8eAd1nqdRloRU_SSaRCVTnp1NPxRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">یک ارزیابی جدید از نهادهای اطلاعاتی آمریکا به نتیجه‌ای رسیده که ظاهراً مطابق میل ترامپ نیست:
حملات اخیر بعید است رفتار ایران را تغییر دهد و جنگ در وضعیتی از
«بن‌بست نامحدود میان جنگ و صلح»
گرفتار شده است.
به نوشته
واشنگتن پست
، تحلیلگران اطلاعاتی به این نتیجه رسیده‌اند که دولت ایران احتمالاً نه فشار قابل‌توجهی از موج جدید حملات احساس خواهد کرد و نه موضع خود در مذاکرات را نرم‌تر می‌کند. این گزارش که توسط سازمان اطلاعات مرکزی آمریکا (CIA) تهیه شده، پیش‌تر در اختیار دولت آمریکا قرار گرفته است.
نهادهای اطلاعاتی معتقدند واشنگتن و تهران در وضعیتی
«نامشخص و طولانی‌مدت میان صلح و جنگ»
قرار گرفته‌اند. همچنین در یک ارزیابی CIA در ماه مه آمده بود که ایران حتی در صورت اعمال محاصره دریایی، می‌تواند
سه تا چهار ماه
دوام بیاورد و تنها پس از آن با مشکلات شدید مواجه شود.
Jonathan Panikoff
افسر پیشین اطلاعاتی آمریکا، درباره این فرض دولت که «حملات شدیدتر نتیجه خواهد داد» گفت:
«این ارزیابی تقریباً به‌طور قطع نادرست است؛ زیرا اولویت اصلی حکومت ایران بقاست و حتی اگر این حملات به مردم و اقتصاد کشور آسیب جدی وارد کند، باز هم حکومت حاضر است این هزینه‌ها را تحمل کند.»
مارکو روبیو
نیز آشکارا به اختلافات داخلی در ایران اشاره کرد و گفت: مقام‌های ایرانی به آمریکا می‌گویند که خواهان توافق هستند،
«اما میان آنها و جناح تندرو تنش وجود دارد»
و او نمی‌داند اگر تندروها دست بالا را پیدا کنند، چه اتفاقی خواهد افتاد.
هم مجتبی خامنه‌ای و هم قالیباف آخر هفته بر ضرورت
«وحدت»
به‌عنوان شرط پیروزی تأکید کردند؛ نشانه‌ای از اینکه حکومت در حال بستن صفوف داخلی خود است.
این ارزیابی دقیقاً در نقطه‌ای منتشر شده که وب‌سایت
Axios
نیز از آن به‌عنوان یک دوراهی یاد کرده بود:
ده شب بمباران، سه کشته آمریکایی، و در نهایت این جمع‌بندی تحلیلگران خود دولت آمریکا که مسیر کنونی به بن‌بست منتهی می‌شود، نه به وادار شدن ایران به تسلیم یا عقب‌نشینی.
به تعبیر نویسنده، جامعه اطلاعاتی آمریکا عملاً به این نتیجه رسیده است که
«گزینه دوم»
ــ یعنی یک عملیات نظامی گسترده و مشترک ــ تنها مسیر نظامی است که می‌تواند وضعیت را به‌طور اساسی تغییر دهد؛ در مقابل،
آتش‌بس ۱۰ روزه
تنها راه خروج از بحران است که نیازی به چنین عملیات گسترده‌ای ندارد.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=R0D737EQ4Y0j0v8O6vmFOFMpH8aAPpwwd5TcAivaf_vEwir930yrTTV3c11t5nMkfsuo9rScabIVx0nhzJzoVfwYNkehr-ty8NvOOkZbW-tD8avnv9T78082dKXP-5pA_ojZAeyosIYBbkYUSYJ_UvsexEmIDgFz6V6_HXTNEr6P9iLFKBjTPM3bUmm9IHfZUhN8OdNkcAcxt2aTVusrl67eK6D5A4f3bpn9FT44Pz17OqBWm4tLlHjcosm7JOu4N6WJeHItLtZo1fqqwWlcrAmrvVQGrdcj-62dvvEYlVrgVcJrutJ972ZxLwTANhLwpKxmtMd4oI32TWgsiIa572BUfMeTNDhX0UQM8Pb-kSGvaWElbws8B_lIVGSI9qQk0vdKRcrYJjryq_7ks2xB16D_x6c9WGdnvOmSkYjslWkLzUaGV5PoL5eDFVBE19SdrER3Sym9XutruiEvgvJX4jN0qk2y3GtZpW8_TdBxNTITuGFwIaBXUd3HgG_ipo3hq3Jj0eTLQlTBpp-5JNzOcN0Mh9WWfvWWdyT-slU6SeyEMryYF-U1VD1Q4mZgTQdLZbwDbGOdemkU_PGzTUlXLqEH0wYR-0F8NLKON_0rQPow7WgvQXoNJGeLl5pp4rlDaVtyqPdx3D0pJYR8acK9mkry9kgW56q802C0eggy-Oc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=R0D737EQ4Y0j0v8O6vmFOFMpH8aAPpwwd5TcAivaf_vEwir930yrTTV3c11t5nMkfsuo9rScabIVx0nhzJzoVfwYNkehr-ty8NvOOkZbW-tD8avnv9T78082dKXP-5pA_ojZAeyosIYBbkYUSYJ_UvsexEmIDgFz6V6_HXTNEr6P9iLFKBjTPM3bUmm9IHfZUhN8OdNkcAcxt2aTVusrl67eK6D5A4f3bpn9FT44Pz17OqBWm4tLlHjcosm7JOu4N6WJeHItLtZo1fqqwWlcrAmrvVQGrdcj-62dvvEYlVrgVcJrutJ972ZxLwTANhLwpKxmtMd4oI32TWgsiIa572BUfMeTNDhX0UQM8Pb-kSGvaWElbws8B_lIVGSI9qQk0vdKRcrYJjryq_7ks2xB16D_x6c9WGdnvOmSkYjslWkLzUaGV5PoL5eDFVBE19SdrER3Sym9XutruiEvgvJX4jN0qk2y3GtZpW8_TdBxNTITuGFwIaBXUd3HgG_ipo3hq3Jj0eTLQlTBpp-5JNzOcN0Mh9WWfvWWdyT-slU6SeyEMryYF-U1VD1Q4mZgTQdLZbwDbGOdemkU_PGzTUlXLqEH0wYR-0F8NLKON_0rQPow7WgvQXoNJGeLl5pp4rlDaVtyqPdx3D0pJYR8acK9mkry9kgW56q802C0eggy-Oc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNEFT0nbw8cfsfdDl4lxvuxB_Xa-1flcvClNky_0TluVsrGbYgM10bkc0oAkqyjyD4PgZK7jlEjyUcP8CpxH5fvo-YlP1HYeacph3JJHOykWw1l9y0NdM-r2kTdKEzWP3zMzecDeEG6q7TWzB359zFvvqnpJfIt8u6gFZn_Vtidvk6IKOwwMoTr7a8cieg8M8BES3XcObVF415flDabtg9a_BAU7CoBGwhRQFERbROgw6rC-k_ot__lHasomsmcqsiWLvOhEYbKXUg87f4F8-mjXzWfyhv9vaHwKLJ-Ls28xGombpVk-pZ3SHjjjJj1eTQjFZU3X_bHKivc9flcpdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdxrPrkauKIKJnCR_H9ycK9h9Zq8ZseibmjjjgyGYyFTFU1S125F6Ru1V6argCT2O8qe8PydQEu9kBLT-kuz9Q2RAXuCk-FwWlk4xqhAgaxcA72c94EmB6uo3xP-fWKPwof-uG825Q2rN6aR0IR0SXTquntL7IEFDhIha9tYgkZhOpMfrfMUEYnC-j_MncN9WPL2oFoXiKxqi1NJ1RXwOrgZMLLU3nZlEw2FRVIbD1abvSbVTH4ShPTamdpPoDThxdjkt0rmepv1xPmUMbDsx0909u2cNGaQ0Q9hY1gjNbJWH0u0Wn2ajFI8CGcV5eDg9QCgmuDdStWV5ysrR95wDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSfMeTdhM83tBKrLw34fWruXgdyF7xMhOA5FObu2-ZtYUHL34IWO08wowQkkGbwQDFVOdsaXoEppAWQBn9nT0EKN_VCxQfau_V94f_5piITdq5XtTLYGw2U50EMzcCXhZSNAy7eymWjYozpFqkRNsC7qfzsnrOxY4cVRFTrlJUdI0DFeqoMne5HH23a0ZBrwgBMZf0iVTNsB8RSpKedRAwEGG3x1M4EzePvOxBMzGhdLCXlpYGIsJRqcaBHv9MxKq2ClwoBJ7rKB9V9kxrVahsE6NAC49qRMeE5mgykvPBsQN_pIecyzNvQo7h2pO_UH1pG7ojVhFf2MAALf6WXugw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEgEfLbvJ66WQ0GYXeKx1UDbTjJc1YfzT0mYt-pqNs72FRTOW3VKuh85BNF6_f3y1m2W-US61pKTSKJJM-6iTL6pcZLhT3JvsIbjFqQtgIUNN8rRZCNwenRHEALdci0QvVOSLXadthG_tpCuzYCNTYfzmDGuS6QrgIQbB7xr_A-_1kDbpVzP8PbM30jNOStFebmHrZqsBxXxT_CzmkgJqCu70M88ywm4ZWMEEd2nHM5xefkNJfrkEhxNswOLO4KvwYRKU5X8OpqBNwuJZZ27ietN8ccqG4hRoDg2xsfWy0mk6G49X3_uoTv4AnKt5Acb_DIF3YDNVTPYSbOALUHCPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تروریست‌های حوثی‌ تحت حمایت جمهوری اسلامی یک
«
ممنوعیت
دریانوردی
»
را علیه عربستان سعودی اعلام کرده‌اند.
آن‌ها همچنین فراخوان‌هایی برای بسیج عمومی صادر کردند:
«از همه می‌خواهیم که به بسیج عمومی، فراخوان همگانی برای مسلح شدن و آمادگی کامل برای تمامی سناریوها و تحولات ادامه دهند و جبهه‌ها را با جنگجویان پشتیبانی کنند
هرگونه حماقتی که دشمن بی‌پروا، یعنی سعودی، از طریق تشدید تنشِ همه‌جانبه مرتکب شود، ما با تشدید تنشِ همه‌جانبه و شدید با آن مقابله خواهیم کرد.»</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6277" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=HQj4IxJar-J5dUUakFQ5AxiREAVMrlvE48wlzTLSyxxvw9GX28XsIeqz1K-GYP7NhPC5RTjfB-QVTtmpoGp7wwkTTjqinVM9HmHFoZJD0HNnyv1tBYQOHAUOGg-mujUfxsJyzYPHQWwSghPvdRB0n_7HPVFRgFRkBOjlvNeLTrlA20MeIYC30hiTSIZzfoa1rD9mCGU-QaTZzOkHUikb0VUYlgw9EvRzBPB46-nUHvJMJ5Ol_b_o6HkiKoZou-WBgtFBIlZdbfYexit-bChftzFcGDUtstO8X53Iw1-Y1_dnYA-hh-_SjK2pyiBdQJOYXQKQZsI-vjMBN0stenZAaIoFbTXdEIYFgKgguvMnxzcIXtDvO0m3U-bKiZN4VjJzWN9dm5p6vvWCyD1ynyfxig4hv7fs-1p8rMU0bkh5q6Sd5q_K397OaXRsc0INGjlgAuxYBfpNs4K3wXCfuYDLqkzm09oRXMFOUTFWLyBvl2Kbjx0eWXbBvm3q1lW_cMzIWGbDlJ1hWqU-5RH6nmPdFnRltxDwmuhSC9ufETEIB5LSLbGxFEnAXlDnUtILzEfNg3PK_yIYkP85IKtWrg33P4A8aj3xgVIsarweoiQdWxqJxVeuZyqxuSuSVc1TnWXqaKPt-K4tCkI5BAbY2Gacc2xtMXjExyFyCrjsHe25r8E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=HQj4IxJar-J5dUUakFQ5AxiREAVMrlvE48wlzTLSyxxvw9GX28XsIeqz1K-GYP7NhPC5RTjfB-QVTtmpoGp7wwkTTjqinVM9HmHFoZJD0HNnyv1tBYQOHAUOGg-mujUfxsJyzYPHQWwSghPvdRB0n_7HPVFRgFRkBOjlvNeLTrlA20MeIYC30hiTSIZzfoa1rD9mCGU-QaTZzOkHUikb0VUYlgw9EvRzBPB46-nUHvJMJ5Ol_b_o6HkiKoZou-WBgtFBIlZdbfYexit-bChftzFcGDUtstO8X53Iw1-Y1_dnYA-hh-_SjK2pyiBdQJOYXQKQZsI-vjMBN0stenZAaIoFbTXdEIYFgKgguvMnxzcIXtDvO0m3U-bKiZN4VjJzWN9dm5p6vvWCyD1ynyfxig4hv7fs-1p8rMU0bkh5q6Sd5q_K397OaXRsc0INGjlgAuxYBfpNs4K3wXCfuYDLqkzm09oRXMFOUTFWLyBvl2Kbjx0eWXbBvm3q1lW_cMzIWGbDlJ1hWqU-5RH6nmPdFnRltxDwmuhSC9ufETEIB5LSLbGxFEnAXlDnUtILzEfNg3PK_yIYkP85IKtWrg33P4A8aj3xgVIsarweoiQdWxqJxVeuZyqxuSuSVc1TnWXqaKPt-K4tCkI5BAbY2Gacc2xtMXjExyFyCrjsHe25r8E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=BQuUVTnHa160m1u_F8PQ8hzjtSv5MmRefCu54fB-bzhrFLTQ0hFNWl1-UtuU-EAjQOadSa8Wy2kOtqfQHl-HwVjSQE156XSH8CaiI2DPttkWNWHIPi-lVGfMWakyAE0O-yw9FJtbf6Z1YmFzEW9cLfGHOIfWcxqABBEgNqmAJB9mJrpxSfnF-g-XbEfL89ikfLzg59WpPJlsDVC_yeyKU0scqH8RPtBrr6XXh9Q5GURxSwJUY7dEVFp8_SyBn9gXWbTu4l2YcnBEeuZGj7rjY-D3LFCbXGLCyqakfluzLlLrwoEvBjryoCirnmMBHb-Eo196uNzCQN4_ddPFHWZ3kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=BQuUVTnHa160m1u_F8PQ8hzjtSv5MmRefCu54fB-bzhrFLTQ0hFNWl1-UtuU-EAjQOadSa8Wy2kOtqfQHl-HwVjSQE156XSH8CaiI2DPttkWNWHIPi-lVGfMWakyAE0O-yw9FJtbf6Z1YmFzEW9cLfGHOIfWcxqABBEgNqmAJB9mJrpxSfnF-g-XbEfL89ikfLzg59WpPJlsDVC_yeyKU0scqH8RPtBrr6XXh9Q5GURxSwJUY7dEVFp8_SyBn9gXWbTu4l2YcnBEeuZGj7rjY-D3LFCbXGLCyqakfluzLlLrwoEvBjryoCirnmMBHb-Eo196uNzCQN4_ddPFHWZ3kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-T6hZqr22UfUmre7L_N0ea3C9NeHbAssA2Ai3pbBli2d78SpkXV_H1CvK2T3HBwsCgDOtXy9UkJh4ULLesB3L8lwNsP3llpR7SzbHAWAwcnq4uAMj5DlYot3iCFClgL7_kFc02hhNTR8Os0Hh7ijC89Iqq8xDXmgORZ9CcxfXi8T-pNGgM4XqtPTltmFkjv7tri5N3OW-cFJO7UfJvDsQrpaGEcqnQogzdpUxjOC9ABa-SZhWrxvQubt2xTIblR71mL6qm--CmE5XUfhwKyPiIMuXqd6fK4BIlSCUicPztHOuPKQLy_i_oAWsE1t9Kh3JaGAQ875QrjiuwMut9vvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u__a8LB26aIt1ssY-cQOV4j5ojWB4ln2FgpDSFQ8dnvl-Rb-YA9oW-jtL-8VLuaqWlbO9-0JuGkdPdQLOjGo6SR30JajnE1mSQH9mY2iHo_87sq4i7wYrhIrYb3np-Kkyq-2GR7gZx4WH8hkewPph9GA39I7xQ-fT5jO4tkK7TCv93HakuhSgkcYNeQZaPzNHtff8lgD00XYXFev4ncrzOP7iXMbmeRkzBA6-tDrnKZQfop8Ho-mOQCn48TzMaP0hth2XMXjlEY3yR3R9_U1Sq9nVqJXihSGI5QEvoq0dHAM10DROfTLYA3QidLndPoVabyRiITDX4YmCGYGMpwQgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iZ1TBT4_FlChq91eemWkt27mP05h_IGq5_np_i4_XewvWPZS1KdG3-bEe3hm9MHPxca8rBGLSXpaRAv7cjStWEL-n6EzeRN9fUNzaywIjnoIPQuF1gl_EMVOjOboxgvIMm4kQaD2OkyLuHLObSW7hkNEg9U1yoV1d2DIqgIag0VzG8RcKR8IUMlwIalLv1efCo4pxEMtuhjVg8zxQBcBxs-uqt8E72FiF8A1SRQZ7uneb9I3vBnjAV0KzG0S76TfQSTftB6czrL9twsrQ3uLgq1ISNJzF5N-YM3gMIHsKni7dL_cjTdH77p6iWf74ZPE3mrvYvAxFGlqEkncf7dWsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i9EGglmSuEayDNJNYCubkWELNT9655ZpTzXZVq6wzOmuCM4QBBFW_VbK3irIohqz6rPH5ErDPv7JZ0cN10C7Xr3xfrH9dQl0mqKNhwQ4X3KiV-UtMG9bX2vots_E4M162aNjaAE4HOqXS2fw4N4ILkVTghurFprnVfPlZmkKWDBOz0f6dBfndVPoZORRDCuKQ61VnbyDpcxze-a0LGg0ofzFCz0eabkcqJX2GCe7BFjav-WzSvvXUesFZLKsrClVnetCekpQWxl36tSKNtWp87nD9BN6zltNyOCX-y3TQOLbrOnJjyVydsLXGUfBG7xlqgsuqoSRRY27w3RJ3nkR4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
یک نظامی آمریکایی در عراق کشته شد
به‌ گزارش سنتکام :
یک نظامی آمریکایی در شمال عراق دیروز  ۱۸ ژوئیه، هنگام انجام عملیات انفجار کنترل‌شده مهمات منفجرنشده باقی‌مانده از یک پهپاد تهاجمی یک‌طرفه ایرانی که سرنگون شده بود، در جریان عملیات کشته شد.
روز گذشته نیز سنتکام اعلام کرد که در پی حمله ایران در تاریخ ۱۷ ژوئیه،
دو نظامی آمریکایی در اردن کشته شدند و یک نظامی دیگر در وضعیت مفقودی قرار دارد
.
پس از یک عملیات جست‌وجوی گسترده، نیروهای ارتش آمریکا امروز بقایای ناشناس یک فرد را در محل حادثه پیدا کردند. روند بررسی برای تأیید هویت این بقایا همچنان ادامه دارد.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6261" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
