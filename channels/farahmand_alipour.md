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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 22:28:22</div>
<hr>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEgMOSHveFO1xJ4gaGdBP0WhAis7h53aEUtzooS6oZsV5BWmFapNHX5_q8raGiGFQgCNJ-t21nnuYkojlkvIDFL6fbCtNWF_oWtlr5BPhsrEamfepi-_ROQHb-BF0QdOAZKhyWnFUaLVnFIQVL54n1MFatBqWE7VosQ7LbnX7VORu9NAfcvu41FJ0YpuFsCoWRYo72zV4QkE5qgrPA57lUV_D8RmwNMmlfBocJMYeeCunRHitTslXVOLltk_7xu8jkVUepKElX3CuCnHev6ZKqdC6Hcm71Hq1jOaCqr1kSYtb52zbkcqXabLKsRR5NwJcrRgXSfxuZEYAJ1da8Hhqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVHNyHPeagSnxkwEfmIrKKeiocZOMLHac-Ampa5iYk4oKWnbnUQ5mmDpj43K9ZZi4ScMe-SFPpbMZp1b374940tv8hyRarAZClhCYlCNkGyTcpRQds0j95atYiMfifXFOZGGgkLPwwPfCRVRR0k1WTNcrkBJMJgZ6qvZk6wpv8qiVbtOlxQqaTASMiclI7q0gZK8jMWIL2hhoGbNqhuD_Jfle6Y9VBm_9GALlygBHfOXYwj9mjO04vM28hgbpjJbAiRy3v1y4AFppInFPv60GbmuRu8QnFNqagehXpjfvLfF9y6oQ41jn-rk4p8tS8jLs4_knXKQ7Fkm41mt_U8Nxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vU03JBBIUrINr83zJT82G-VOKqE8hOi6VDow9Vk_JrqmtdlDqAZ4VWG2z6kPYKYWnTvcu1ghQYhN8YxdE3WNEs-puYUx85kYY4Gj7TJ1HIHBl-Z1qC3StQRjFiHbT7CppiHHAE4v1oZPOpZUMXOfdcUN1h9ilzqqgRBd5aJhbmIOAabbejFL_KnA94YSUmqaZULOPgbThc7gMMVMBuJCRXVs-BoDbGEmpCSNmoXpnK2UBLLuvWLwEo0C_AmejZoVeeOOmnT1FrgCm600e-Zya7Q1SPA1SiH57ooZqksGRi7Mt7Z4_If_Z6p7vDT3ipcJFoN3pXnyeMra1mG0EJK7KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6uXN6AIS_5MoIUxC8Y7ktV9p3gNfFu3TR5dpzWtVtsp3ak8GY93NMY5gwTvkLt2EP0AgE26uNAI_5mZ3VS4yzWja7DE6sXcoE56ogTN57GbmcmCRrA99--Vl-uze9Smv4aNX1gBfVF6WnA2ku1E9ydTd69jXDbsfeB_G2edKTeEithmOACjtkYiRBGD__x46cvX0KjphzHYInXTjdn8nNCCb30QIS1IOCAXqrqHtx1rzduST8WOJdn3jn7vio-1fxqGa-uTmg-MMfU57p15zqKAnsO24gUa4ZDerk2oI7emoQCiqoFEElxZX4AGfdV1oK3aX-dd4PJd0FfIrBrWXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4W8C02ySscLJP7zUlcpOPFg51itb0CAPC88AR8e0Kd8VcLR7rZUm5IR4l6E3LnSMTn8o4unwp3MTKjhcZuEaDxoRHoCy9Cm6p-GoCcb2qV7cRaCcifKfQagVRLWozSKzl1oereigannpz18xeruLSpelSQ66x8Z83oZEvQmMV2_LZPclEbuZ9iXby2tBzoTCUeoeUKk4SkL5mb5osAgvP2eaGWOpDkV2hflyRAwPmLBRVmQllhFn508w_b2rCcFxoIJ7_kjBTZVdPbUTzN5QZkeFkbpoumH30PauZDn26oqgZfHFZnf7jJdRcEE_8Lby0umJSq8Y7nFtPJEvfF1-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvHKMUEKubXR2lu4sGetHdIJdqxgmj9Xbt6jgglg-LH82RwYO7G6iXsPrphavx_mA8k8-Pfh-q874DdMZijI-3Wp5fxzYfJhx1IAcxk6uugbOHHLYCJtWvr7GeJGI-nH7Ok_Yi9fU0rawCW12DJvftT8fgbRWkMTHK_8lbf_kHBwp-CyArwlXi-rTZdUMf66-DCAPI5nLq4S-4kmHdcsihgiYMmFwoUBKjgX2uYpIZXWisSHFQCfHi9yhBiZJAZCRfO2uhQkBRJJhH6KWFJ3TTcv4Zr7T9vS6g0zbw0PsRCsOGkgX3q0DSEKY6cAXR2Rz7iWjk57DiOXuCl9ZX1aow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=Hk2xBXEnTLYUnsm9OO-WDZr4vypUVCzJ89F-ublZrUmn4ytOlC_ijd5k6ZISm1B7hqkE4fEEQQH9PtJrD_VnfGMY84vX2o_54e7gdDtrIsZZaZoni9dU5lZX7ZxgXgHFLf0dmRHcpXLQlZVbzyz1I7r6qRrutnOe7f8Jg3dkKhK0Q31uJezQ8jOwfYRVKcsk_3CPg_akzJnjND5wQIIl6seIz14ulZzp1-lWsbVIiQAg91VYgkrKrxmgUbEowDzeCrJfb0vviGd3gZ6QjY_J15cCioOmgijvnlfojAtxqaELS3BOPTyuUCb9HjRj0EuXlvGljnOUp31rR0mbGW3sbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=Hk2xBXEnTLYUnsm9OO-WDZr4vypUVCzJ89F-ublZrUmn4ytOlC_ijd5k6ZISm1B7hqkE4fEEQQH9PtJrD_VnfGMY84vX2o_54e7gdDtrIsZZaZoni9dU5lZX7ZxgXgHFLf0dmRHcpXLQlZVbzyz1I7r6qRrutnOe7f8Jg3dkKhK0Q31uJezQ8jOwfYRVKcsk_3CPg_akzJnjND5wQIIl6seIz14ulZzp1-lWsbVIiQAg91VYgkrKrxmgUbEowDzeCrJfb0vviGd3gZ6QjY_J15cCioOmgijvnlfojAtxqaELS3BOPTyuUCb9HjRj0EuXlvGljnOUp31rR0mbGW3sbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFPCHHqOA0FLfWFsNB2N51-dg8qUSGOlhsuoKp-5jQY-a9rgjxhh4bmBTxEd0O-KcE54kMUfOM0qU2JbgRqvFVkyy3F6Mn_h9XAC9VpzM2E-F6l0BYacv1QEE6KEaoJpsu3DZNCS8IKyV-utDLOZm1_XzQBwNOJHA8UzfBau6jkGfS1FosL_ZBJo9yETdN2ah_QvG3EJ8Jnp_z_FEipKp0aytyEL3BPNcMrpwqE95X1QjO07Gsxx8YJvG3RMlfNfe2EiMToxLXb5LIxaPKjEzxuFkeyuo89ztm8xQQkMxz2uoPvJRlnaejaWP7c51-TOtbFUcwn13jUiWHibNbzd8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTSGEA0Kar17Th1BqQv7Pkht3ObSOMGHqjQ7WflDJiVKL-l2QtZLyCnaEUKBklhOjEf-FUXRJpb_S2d8w1T2OL-TPI8jHFBNEz9UR_L5S5jwY9otJyDkS87XUA4UiqSEiwgPYlzo21pWGqfRoj-x2wIVkC57ovPPWJ_7MovbrnPH3PrxNkaheo-2IVpxHxuhHCOf45gvlN5moac4RxoTxzw_egpcQa2afVd0D_rEH1b_P8CKWP2mWvPzmTyq9rMwYsZkK_4qMOEL-WOufraC4hVYB5gkmS-U9oKq6QUYDQyG3OlNVKIF2xh9oofu2P53Pctf0YLbPbQsoY4PJSdrlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mp1qV_ZbOU5RtgiDariZacUPMAPBkt4p8eMqHXBbZeSTcMMA7fwQWLPz68VOQsTLWh0okjmpBxigppmYI8_roNDycy_CZflvPEtdtcLTmPkpSyPo09Sjba-4SErJVV1mC7hoiXlj_aTKwGqnfz-KQrEH68p74B5AMWXVOzLocK39Vs0VhowEPvWejWV5ahTt5rfZlAlsjU8hYKJ2G9TkKGXMU9Xihusm9PkkDOmO5jNA1F734I-uaKZbabsQMBywznfLe5RkofISCtLUXp1O72a7woTFoU96la16F7zarIh5q6FqdvC7WvSsi9U9mFUJUrv2AINlNcO8_wfXPhAi-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=We1qawLYm7JVT5WOkwMocUhVc6mEjFu8rgRqhkx51Ge6O9d_lg9CN74bI7db4XoSm2pMOpdb23-kV8B5SJYeUjWEUelIW-AbKYRt8kCRfgjbC9lvZwMphcjQa6n2dm1eiENUFjPjzXipZcMHp_MnujoELwE-2WuxlHLcrp29uXaGqzzP--U0hh4wv0gqS9LgiE7uB_c1xlf64PMA-a2pOH7Jd1UdmNRQbPm3hHJH4aIIzZzTa1-mD0TaM5-fSG9jrf7wl3WrtviC74F7caLNS_dNmvZ4gh2ROXWg8XX6yBXotKfMyhNFxiuzj2LsEcfHB526VHu4tRztDzQqcabVnzd77WxXgOW6Sev-Fm4BdPxnqHxb4UTPzuaptaE6nl9RD4gq-x4DdUKlrH3BwhoGBVp63PdwjcIv_aOImE667lTHnqdR1ztc8qzGDTPhMwXUFR5ljqpQbPFO32Pm6f6dv-kL6hWz0-jNwlDmjb_lS_aouc-9fjwdUtHsHGz5aZsYxqW_r28OdR70Iog1b31uzb2BY8ze8HFxyY3GeDHh3hIsSNxeH-ItVS6scQPr2x2MR7kJ6zJlOydQnK4hHx0fR_9BAHxWSiOp8SYMzqrGiULCySe8K4bfTGl1ksf-P5MW3knBmFgdBhhi2GZRLq0iyiIVf88RO4MZHyZQoY_aS_o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=We1qawLYm7JVT5WOkwMocUhVc6mEjFu8rgRqhkx51Ge6O9d_lg9CN74bI7db4XoSm2pMOpdb23-kV8B5SJYeUjWEUelIW-AbKYRt8kCRfgjbC9lvZwMphcjQa6n2dm1eiENUFjPjzXipZcMHp_MnujoELwE-2WuxlHLcrp29uXaGqzzP--U0hh4wv0gqS9LgiE7uB_c1xlf64PMA-a2pOH7Jd1UdmNRQbPm3hHJH4aIIzZzTa1-mD0TaM5-fSG9jrf7wl3WrtviC74F7caLNS_dNmvZ4gh2ROXWg8XX6yBXotKfMyhNFxiuzj2LsEcfHB526VHu4tRztDzQqcabVnzd77WxXgOW6Sev-Fm4BdPxnqHxb4UTPzuaptaE6nl9RD4gq-x4DdUKlrH3BwhoGBVp63PdwjcIv_aOImE667lTHnqdR1ztc8qzGDTPhMwXUFR5ljqpQbPFO32Pm6f6dv-kL6hWz0-jNwlDmjb_lS_aouc-9fjwdUtHsHGz5aZsYxqW_r28OdR70Iog1b31uzb2BY8ze8HFxyY3GeDHh3hIsSNxeH-ItVS6scQPr2x2MR7kJ6zJlOydQnK4hHx0fR_9BAHxWSiOp8SYMzqrGiULCySe8K4bfTGl1ksf-P5MW3knBmFgdBhhi2GZRLq0iyiIVf88RO4MZHyZQoY_aS_o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=uO9DrRvabXtYSebUWjfqkFphH3AXQ3Pb97w6aO_8hzzAzstdlKDIyqBZ8EdpO0h4ZqYQPA7gXZKGsn0uoEAZi5JwXnSkw1wxtUmt0qr5yhLJLRu0oEAIxqzWDRvt9y5_ZFHTfneKPzxzuMg1_yj4lnrx6zD_eF710KFznD-DmMDDMeu-HFCtSLgQGBA7PvGQlRKzTKbt7j7WkwkH13CWy5-LezoXKkleYi6SOh-o8UK52MRkWrRDJQHBbnysxYr5_PQFEVX_-OntUDFbezR6xOboylbSqZ-uu-0EhRudnPH4h12o7d27RfkWPFag-sPOJcTw7nn7H-m4x4C5c4ptQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=uO9DrRvabXtYSebUWjfqkFphH3AXQ3Pb97w6aO_8hzzAzstdlKDIyqBZ8EdpO0h4ZqYQPA7gXZKGsn0uoEAZi5JwXnSkw1wxtUmt0qr5yhLJLRu0oEAIxqzWDRvt9y5_ZFHTfneKPzxzuMg1_yj4lnrx6zD_eF710KFznD-DmMDDMeu-HFCtSLgQGBA7PvGQlRKzTKbt7j7WkwkH13CWy5-LezoXKkleYi6SOh-o8UK52MRkWrRDJQHBbnysxYr5_PQFEVX_-OntUDFbezR6xOboylbSqZ-uu-0EhRudnPH4h12o7d27RfkWPFag-sPOJcTw7nn7H-m4x4C5c4ptQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9aZv0Y7GVghmdTTBi76zG7NcYWnYJoxAZC7z1yBXdaLFCTCA0Qi_SeGocdk8HUu6EEskwl8n2Whl_Ty3XwNWkQKRb11jlB3nnu0N_VDDmkzHSvJaM1_5fStMMo_-7bF4UBIbPl28r_TZcHoeRsDWnX7SLIHxpgmGUamiyKGg0NktYx1_TuAdTwxERSNVWL5WUTj3xgeLC0M5pbg8m8gbFktMB8wHoKBQJJK3tFiZbbv1dfD3BkDzB-H6FO0HNs6KcRQ7qVT9jBdmljPUtbQlw-AZfw_cev9Hw2IS55TaSjt69Zsqq3Gxd3fLKRRn5nXD9WmgNG809xb3cTzi1o6Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=EWDffPoDxkY5NSRkEibQYLbM5DCZ6AMs-TWT22pVpCpkQGluwRjDVNxXgEnPpDr293UBx42b0izSpzhI4CH8KWmNocQokCXmhU0hv_-Uj1MSYDjdCHRQ7nwLvrEyoMubkEODy28ow8f09e6kgoSRuFuRlXCaPuaPnuGkvc3xjOzcRT3nsV4KyHZHTqizh3EtONATfHqKaZDd3OPUtYDG-zeGByUvCCee5kPZuCAUsCy_0bqtyePSSgxxmcpJ4O0Du0r5BZ8SY9KGzXHhu43MsF7rYQj_U1M4dhcik2m1K8cqR9arKJRDZVfZjFTmq0vO-HJJXDkLv4QQc9Mq1dj8hTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=EWDffPoDxkY5NSRkEibQYLbM5DCZ6AMs-TWT22pVpCpkQGluwRjDVNxXgEnPpDr293UBx42b0izSpzhI4CH8KWmNocQokCXmhU0hv_-Uj1MSYDjdCHRQ7nwLvrEyoMubkEODy28ow8f09e6kgoSRuFuRlXCaPuaPnuGkvc3xjOzcRT3nsV4KyHZHTqizh3EtONATfHqKaZDd3OPUtYDG-zeGByUvCCee5kPZuCAUsCy_0bqtyePSSgxxmcpJ4O0Du0r5BZ8SY9KGzXHhu43MsF7rYQj_U1M4dhcik2m1K8cqR9arKJRDZVfZjFTmq0vO-HJJXDkLv4QQc9Mq1dj8hTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZiEFF0JUZ6jOzB3mlf9R_ZuaHfdPbmUX0yGDutrjyDmpgzIyLcL3hKjwwH8Is-47Hy8VS_IQ_k4lRwco5cggth_bgJ_yvTb6VXFl3xTb_gizJfduM0RnDKdBD4t3oZq3TZNp3cHrfhA0WWm56_2rYYoDiHDj_iDnW94F5uSsIBoM6oX8TKWGzVhgebU_k25Qrk2kxPJcwYOLrj-MlIhUXA0Mq8eVbBwNPQXU9jWxItHnAnj_hQX-MFfmBZSUcVpy_vS_Xvhrff8SFLlVUbQ7rdUCBfLZLRErDfEriNtn0nO0WphB2ujOICPocKWBZGLjvoMH_zdFXbilOKBFirp_fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWZTNMU3Q4K6psnP0KAtECa-ncEORvtsYm82UhQjY6x1v1IjNlUe61v2AvzX_VCyHMpAQaApSaclOB38O75ymmWd9ICpLdwI73mcnbUQlN9jVYx7HqG1jzYGJ4fXMfV3N18t-KP6egMNDwqRdK8VtEF1ah-qT-yf7u6ZQQZ_YBVBMB9tB1--mSf3bFCgIcmCpBhCE3oPG7NkV1vYFNs78Oou0JeRB9W_eUgywbNl6uEzvmS_dTlHp_P1YDCIjXgQTFsoJqmx_-WdZ-3AL7B8_KMrY_ziXCoKFUkzA8qn6EVKDdCC7AhEVqTDBSVuPPFEaKBnN3gwRho-knk2vRbNtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TO7A1-vIQar0sRxbPPnImA-zxvDa8lvm0f9TI4hJ53QicPfuaVUvUbC--kUW7u4xOdga3wasTpZ9s6ui27I1i9yxDqFHZHQpFyi-CY64tgrzMVYLEn6DqDGcm9qCpizaWeLWAt7ko3g3BD05CtDVJs6FS7bBvvvtLjHbJLhiAWa0zmf0m3V494ACOmNqJ4c1O8jnRoNT312g_B52ANaPs6z55PqPDcYolSdiSr9QBVBb8nMAndnCWyC-qJT3O3-6ARk_PGNHupaq_vDPS4CkXFcMCHisp6HKZq87wBseq0PkWrrMSLArayUcgdRbrNtgMHAv6J6ybbMzRymJ7GgBlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=L2y7XO5c1r40yR8WqunxYXJy058Y1oe2NmEUYDuthZx5oh5aOICP1xdpaTYn47AxNbi6hPeo8Cu_2XXfvErDRe4OZ8cRkC9MB_cYBxMFhQqrjXtl3QVylcZszbXmX3QG4PZsQWj86gLYMaPXeO-liPVbi9yFtTIgMFu2HXOqhdLhX5AEA7qOqZm-Lgc0m-TeXPraxg6iUOeRVqxSuqcZpzvtgYBk-mA1Q7ZBQMaL_kFZnQ1NLUscml0sukhIbNL0b5ddyXhYh4yLvj9RT0troKu30CL-HnVMpDKK1aEPu8oHK3rNownBp3BHzUWTxQOxmEFzr18_8P45XofcyMHCvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=L2y7XO5c1r40yR8WqunxYXJy058Y1oe2NmEUYDuthZx5oh5aOICP1xdpaTYn47AxNbi6hPeo8Cu_2XXfvErDRe4OZ8cRkC9MB_cYBxMFhQqrjXtl3QVylcZszbXmX3QG4PZsQWj86gLYMaPXeO-liPVbi9yFtTIgMFu2HXOqhdLhX5AEA7qOqZm-Lgc0m-TeXPraxg6iUOeRVqxSuqcZpzvtgYBk-mA1Q7ZBQMaL_kFZnQ1NLUscml0sukhIbNL0b5ddyXhYh4yLvj9RT0troKu30CL-HnVMpDKK1aEPu8oHK3rNownBp3BHzUWTxQOxmEFzr18_8P45XofcyMHCvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvOcAVnWu-nT6YyjGBzzFUXIsk4wvozxS93rz0E_6wEsBn3V_3JKXozHL6S2pVKGNA8bCkkzfellILYccOSrCTqAUvtabIiTBFZpGZP4U8oIc_FZIWM2vzIjxZ4cZBLTRCueCfuZjJ4396ID-sPrxPasVm2gAEouM8qKfOZEky_WmlUyVMljCwgBxqGTEBQh0EQx1h2DwW4LFyCBwkx_RcMYEilo888AlGg8EpIgSz6dqO4mP1YAgv6L28O-dP9psgfaISY1QH9hYCTKWBtOxSmeVOM29n5At7xdPDs-ouh2aNOwSgmvSr-3sWOI7slk0_q6iyR3Aa6D0fpStLYfVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYbubre-yfHyRD2sOSIVfKu28NhkrA7-QsyA_IMvT4QqQwvo2YBrqmwCRPHw6XnD3NJFSL-k4mB2fqQlepga6-wIZEsGBNDwSduz-snJsld6steYC7-0lP4-S58cU0nhXHGc4qoe30WJn_eRHoQmdm2-z6D3_OPcNC2BmxfK971U4YJlQnmWSY45EA0xkGfNYkgNEFICWYUZ60DBAFa151WbgBf3Q5bcUNBrfALngVzZrlmDBqbxJ-bkOVx1MGaVHCg1aEGz7icztlVI3RPL5O5rHasQSYysrjzjO-uAIS1w6tYuiz4fHcXvBeuxUa6WWcB2RCU5l6MRB7s53maJdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=Nw2aOLug5WUgV3xV2iVnRbgu4Ga0GBlxQSglaFRVzEL-USMAWrF4TQeHpDH8BXaHRC-EHd-JVf2Uylvvy3ymQTsitJxpqi_aEaZyOREkfUPKUe1QX7Xxn36U9Mx2wO0tDAy-V9hTapX_Pxixm7lhXWus8njSMbhhaOMsl4RsR4XZESS6E8fykR-__jz14O8KdlHh2wnFDdslPBbgb6p0rKbVUf1uT-0GdMasgcljdHkpssFeRCjnVdUmjQaJM3_KznqLxoJW58ZUD_cWnSRuMyqu6KU147vtDX-CkCiY2FAH4ngTtlxz46XOr9VqVmas0-5p0G03U3h3ubpdaB1uxk40URhNsGeewPMKpGyRcD5T2s4LU6uLvyZCTHnak8ygwZXUc0DACREjEoZy8SYZauMzQ5xBiF95dCzo6LiNSWAA9089KgE_6YcMYo-3Cx4CDSXncfnBTzlfjbetbLON13vK9IzS3GuJT1ERNdt-XMGpjsKuqVmzSAcvCh5CZuLkOMDjBkooZ3u293ApuJW2i_1FL1iC10IQGrujiSuYMmf8qvPZHsdQmiEMeBEg-HA1uylkbrBn9p2DyL1k3686noFunRQOcT_fzIDYR21vlvyPMgplxcOsIJWXoUzfHWndmoaGjzLeyXNN77wYv_6gu4BKesW1q4pFZ1dQnd5ul2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=Nw2aOLug5WUgV3xV2iVnRbgu4Ga0GBlxQSglaFRVzEL-USMAWrF4TQeHpDH8BXaHRC-EHd-JVf2Uylvvy3ymQTsitJxpqi_aEaZyOREkfUPKUe1QX7Xxn36U9Mx2wO0tDAy-V9hTapX_Pxixm7lhXWus8njSMbhhaOMsl4RsR4XZESS6E8fykR-__jz14O8KdlHh2wnFDdslPBbgb6p0rKbVUf1uT-0GdMasgcljdHkpssFeRCjnVdUmjQaJM3_KznqLxoJW58ZUD_cWnSRuMyqu6KU147vtDX-CkCiY2FAH4ngTtlxz46XOr9VqVmas0-5p0G03U3h3ubpdaB1uxk40URhNsGeewPMKpGyRcD5T2s4LU6uLvyZCTHnak8ygwZXUc0DACREjEoZy8SYZauMzQ5xBiF95dCzo6LiNSWAA9089KgE_6YcMYo-3Cx4CDSXncfnBTzlfjbetbLON13vK9IzS3GuJT1ERNdt-XMGpjsKuqVmzSAcvCh5CZuLkOMDjBkooZ3u293ApuJW2i_1FL1iC10IQGrujiSuYMmf8qvPZHsdQmiEMeBEg-HA1uylkbrBn9p2DyL1k3686noFunRQOcT_fzIDYR21vlvyPMgplxcOsIJWXoUzfHWndmoaGjzLeyXNN77wYv_6gu4BKesW1q4pFZ1dQnd5ul2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=FZBU_aYf4uW9bkC-3M179mTPrhaunrhdgnxyl7VMtD9aVgZOuXyGGeL3qwXVvrkRP-ZuFtNY4mCpV-io7pOpODacngnfSEwSbkviRhAXrWffluS5n_krPZonCmsLh2vx5urB3MtRzf_Pt9CM3ZPy0rY4pJ7ACtpzxWrSygh_AWMS60T6zoDjQ4QOCDweh9Ye0xKU9aX9FC5y947-WUMDShB9LgdgBtj9LAzW51nBfwl_Ig01G9djcKA_r1z71LowchhvoUXeLa98L6Zwc0HH_Drh6YyQnzikTrjbTJ7zsQdooncZuo9y8LE8I6dH4QVLhKBufG4vC0EGa5aziRgfHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=FZBU_aYf4uW9bkC-3M179mTPrhaunrhdgnxyl7VMtD9aVgZOuXyGGeL3qwXVvrkRP-ZuFtNY4mCpV-io7pOpODacngnfSEwSbkviRhAXrWffluS5n_krPZonCmsLh2vx5urB3MtRzf_Pt9CM3ZPy0rY4pJ7ACtpzxWrSygh_AWMS60T6zoDjQ4QOCDweh9Ye0xKU9aX9FC5y947-WUMDShB9LgdgBtj9LAzW51nBfwl_Ig01G9djcKA_r1z71LowchhvoUXeLa98L6Zwc0HH_Drh6YyQnzikTrjbTJ7zsQdooncZuo9y8LE8I6dH4QVLhKBufG4vC0EGa5aziRgfHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCo7JPCD1P9lleN57w43H1JgwqKFmNj1yw94byAhhf92gI7Jlc6LS4Bo8y97snqvIZIjL1te-PSRrkTV4ju6LKklPP0lkyjpW59rF97u-ecc-6Y_QQ1iXqd4_kMkXldy6Xh9vNpK5ulR-epmg9uUcSsXQOjqT-xzlUIp5f2yiD_RPPEKTHETTIcTAWFl44PpkTLxoB1oJlvFHHJRMkNN9pmcrUH1vYaoRcrmvFPbRyvx4Unbcv9GDBYoWC85TeloDr9ieol7dID_hoJoiBFPaRif0EivO5q_-IXYNxw9z5-IGB1zJMrunlWeV7UfzSFvPV3vt5pHsEl12pPOuWwJvVzY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCo7JPCD1P9lleN57w43H1JgwqKFmNj1yw94byAhhf92gI7Jlc6LS4Bo8y97snqvIZIjL1te-PSRrkTV4ju6LKklPP0lkyjpW59rF97u-ecc-6Y_QQ1iXqd4_kMkXldy6Xh9vNpK5ulR-epmg9uUcSsXQOjqT-xzlUIp5f2yiD_RPPEKTHETTIcTAWFl44PpkTLxoB1oJlvFHHJRMkNN9pmcrUH1vYaoRcrmvFPbRyvx4Unbcv9GDBYoWC85TeloDr9ieol7dID_hoJoiBFPaRif0EivO5q_-IXYNxw9z5-IGB1zJMrunlWeV7UfzSFvPV3vt5pHsEl12pPOuWwJvVzY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYER7084xdcQDTDBhyGDlhfHwIJXV2tjmueJllCy2s_apKs7Ktez2JLqZbE67ul6Ndh4HLZe8T5lX_hREr_BdYqmj6PzZsLn_ejqlMEgrz96MgG3OgQ0xrZ40VBjOMCV1-f86Otd_X5Arnd1E9GbCuFNUOelUW5E7zIBoKQyy9M3Sug_lAyfilYX56IbxV0DfnAlH3DiE5GAwr-IsNpFbOTS8JHFNepuhccnaW87TPX61iFBiegjgrLWFgghhhDOe1PxestsFIeNQmOzVPKyCqa3W1jCQf3uxi8cDekgEg_Sb-92BKKw5buFNWmDWkYyaDF9062ZqgGXUO1xxSnfew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdKFyQlzPg38rizRGUxNZ_6mQafBmiBEalhWP5OV4Aqgzuz1w12CwSGIuU3pKp5gv9u4qJJxv04VPxi6LXzD-B12lGkSywwNjklevLo0mnyuvG0jvI28VgAYSbWzRXlO53IYcntabLGQ4t2M9bHVdZMwuNV_-j3svoglpJgQoRYfwjcJddYzIHji5FW14Pl2xqOkPg_zl0sqc5RdbZMcfSyYEbK-GmgcJD4K8za1L1pI5GA7Q77Gsnu2qmYpWs-LznU4QidV4VSL-C8dW_svr1D_qt4dWcFkac7ts4b6oesezhhQC1Tplb0dSxoiKe4hteFfi0QU8V0NgfClfF6MvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiDhk2YojHcr5fMlWJwLuTY6znqx1JcyMn6zALjrszzsFPQAS4Z71tDRfk1wUbp4BkiP58UfTeN8HwjHGkKQ8_D2RT8ROniHvVyWVKvGEYV_bF4QkAL_sVUJ1xOl_NRNCS_vYAll5RldrRUC0ei_1zGiQZ7B-dRX2rFfhUFCbYr0sS35V5dbCcfyaLzPya5p5D30RO5hpzAh8AvXz9W6lR3E2tWDXuJUlPKDUSKVTlfk7mHqSY7q17CpB1VKDc3HSusfHvqzbtRt3rYmvFq-5TWy2U7H8N2Afg_murtMWz8wzyRQf-5V9MOEJ0xPy9ayMONqqffUDeQeiD3Y1qgyvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=vLvwQfOSI5Uclujn8TyR1t5YZArSA9whnTav8qiisctJpwCeBr7OkVO4CITp9q-E9OLvDtM_F1doGqmM7TYGkKdUno4EwnerO6J5DBce4JIuxoDKX8l-t6T-GYP283I_lRfgC3zuKf5-lrr_SSQoPC2MIaJkqiEXdF27F19RyEJumd_rrATLLaSy17GUMvfSnFAGAKu8_BKoWhR2-DNF28UftEgu61EzVeu4P4aiNRwEZwnufhb8lEwLc-nPplr4uHOKT1pFjNfFkoOeriAz1w0ahzPJ8xxHRDiRZdMb1aSzxc2dxDvSNCiIVibImeombXV8KhBvoxboLtbDoL_KTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=vLvwQfOSI5Uclujn8TyR1t5YZArSA9whnTav8qiisctJpwCeBr7OkVO4CITp9q-E9OLvDtM_F1doGqmM7TYGkKdUno4EwnerO6J5DBce4JIuxoDKX8l-t6T-GYP283I_lRfgC3zuKf5-lrr_SSQoPC2MIaJkqiEXdF27F19RyEJumd_rrATLLaSy17GUMvfSnFAGAKu8_BKoWhR2-DNF28UftEgu61EzVeu4P4aiNRwEZwnufhb8lEwLc-nPplr4uHOKT1pFjNfFkoOeriAz1w0ahzPJ8xxHRDiRZdMb1aSzxc2dxDvSNCiIVibImeombXV8KhBvoxboLtbDoL_KTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFXDEYNyxcLJ6XyFUEUkViGbPGpKMhXUDSixpbiU9zEgrqNbBvKu6hv9BCWE9wR0bXsC4X1yRFN1pKiguERfVK75dg3uRsyBEpVXZAES8pRnG5u9MOLISnkh3cyVxARq-LbHx06xViuXaBrul21lY87oPvTBMuvyAjiAmp9aDFtTDT0mpgX2z9F9eo1MDTH9QHv18LUxBUBgPK-54vRV91xfpqIc3vgXTxPlKNFr-JPWOSBdRhFCs1zJMC1D-DBO2wLa8rcsPew8Yh5nuzrza3rLtSUe29ype7SkZbcghs0EK6arqWh3Z7EwgHIHKsa3HJhxVW5Jqizm5jAUCgHOcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/asn2cMF-H8FbPfr9zs7Fi5a7gAFXOT7aX7VwtQIwA_T_HzvqYk06YlXRLVT3w9lKcUqlrBUrjloEpPyHBL_94z6Tq1NXfwMU-2xKEb1nhqdGzWoy1eIWa-NPVYmepKDOrgbIDd4xGwCJ4cjrsYFyZdpllnuwLwN3tUhbUopbWS92NJn6qEHnx8-uuawbwBvA5L3hUrfTmH39qFe3gx4ATNzs5xGc9kx4gYl4ashQyCSXAW2OxM1v5o5io8DsEkmgzlxdQb9VHSCY1Iem0KwIi7hDbVRR7RWG_mYcyXzhxLtio6AP-AljFybzdbzd1FyU4R0KZPrU-rL4eAUp1Bh_xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YQnPLBiQaM_mOo7Ifv_Tm_K7qG01Lyc902vwea2fv6-3_waNe-G4_jux4imcmQ0Q_H8S-ixS6m4ExpubSSURXmy9zJoAiIEPzb7NQcjIktDv10fm4uXt7CfEyBbQXhlwtPTCQMqX2PbBqeao7HU6PATYMfBKKQn_Lclr6_xvofgHT-qV80pCkorYEwH_xtw4eP8VIMLrYuLLKA15NashvrP7wiHhjLkEtbhpGzL9n3he5qQcNraQ54SskkCetB9639kqGhPGBIDXgw5PEvt67gHJKM2BJADnD0mP1a54E9ZyPVHQ7b-HFIq6kwjSA1fvqPmHXisiglPEOOfg-krZ8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOIS9I_rm0joG_4XZBsL0J4ldCnUnxvcgPi8SSiF8P-P32OVoP6K4jZM__6ZrLpDam65A0H3vX3Tjms2BzhqPds8sIdPfXPWu0GZIjzDe-gGIJG-IxJTjxdSNcR1u5MVFDyJjHPQFyVqM-E_XmmhnbPShZ6dVUNJmjkj48Sa8STMHC6pz0rfV6kepdVU4pG36TjVFMqLzh3XLDVBw_pRdJeyXPKKxEZaSy30PTNVzdR3WzNVj14NR--Snnr8VUzsNWNncv_6itoIZ6W3I-iULYbyIHSMSitsjfSlyUqEElvGd-fPpM9ji5IhadFH6SWPC7fszjXp2kSIQ8jRpEFHAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=mvou6E0cARoM6Tl7u7VSVHsYQdgGBJvaSMYBitQ99Px5DANOaRc6jdW817pPoDjKWO2j1Nvc2BggXLQQ1Rbi4h03EDjRK4VGDmETmdYIAJ2gFTZtrLhTDvB8POY7D2xNMjzQDxusOFh7tVQaNwzKAg_PE0e2nswhGBA_2rj-4gZv4tw8fqf6-yGypc66-SVNhfa7l9FQR-ENyoD49XfFTTXMmdssXXdgCpmH1JA4g18h5li6PmquqOIhKtC9qdn7iK3s_BlUvP2ldbhQQ5_yZZ9mOoX5DUPr8jdRFh_LvFWYVhYer_-Fd3zAES2etTHkI7x8iMJuKEvvFnAq0osEY4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=mvou6E0cARoM6Tl7u7VSVHsYQdgGBJvaSMYBitQ99Px5DANOaRc6jdW817pPoDjKWO2j1Nvc2BggXLQQ1Rbi4h03EDjRK4VGDmETmdYIAJ2gFTZtrLhTDvB8POY7D2xNMjzQDxusOFh7tVQaNwzKAg_PE0e2nswhGBA_2rj-4gZv4tw8fqf6-yGypc66-SVNhfa7l9FQR-ENyoD49XfFTTXMmdssXXdgCpmH1JA4g18h5li6PmquqOIhKtC9qdn7iK3s_BlUvP2ldbhQQ5_yZZ9mOoX5DUPr8jdRFh_LvFWYVhYer_-Fd3zAES2etTHkI7x8iMJuKEvvFnAq0osEY4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=ijcGVvlsyiqmgkvyIW7LhBHpsXZaf5ntnY1wH2Jee5lAWgf69o6swkXp6ClxK-SYvgWiiC8GoLZnQMqeADSk7J0iwn_y66aN4N-7nBsmVc7ueYngywae9FeZRSTQkiPuwT_ZpsTiQuXswWi5k3OqlRkQCwICvWd7hELJfMViAFblvuSH4ah7L1YUBZBbr2qF0rBABgJt8eEwWDTltd6KBX0Pc5cd9Jzl4BHkPsI85Z1w9sMhhOCTd5vFQsIa-U-5lS1P_4H2c9axpEmFAsF1bY5ACcje1la2y4zT9VVUp-HKlUpfBfEhtI-sWb7hfAm2QmuotaGlxGOkHpNAaX_yJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=ijcGVvlsyiqmgkvyIW7LhBHpsXZaf5ntnY1wH2Jee5lAWgf69o6swkXp6ClxK-SYvgWiiC8GoLZnQMqeADSk7J0iwn_y66aN4N-7nBsmVc7ueYngywae9FeZRSTQkiPuwT_ZpsTiQuXswWi5k3OqlRkQCwICvWd7hELJfMViAFblvuSH4ah7L1YUBZBbr2qF0rBABgJt8eEwWDTltd6KBX0Pc5cd9Jzl4BHkPsI85Z1w9sMhhOCTd5vFQsIa-U-5lS1P_4H2c9axpEmFAsF1bY5ACcje1la2y4zT9VVUp-HKlUpfBfEhtI-sWb7hfAm2QmuotaGlxGOkHpNAaX_yJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=E94gpBhlMAsx6pkzFY_p4DqPWf6DiVeJQj2eWuNELPJfaYLbEGhDeF88_7qCYiNiHevfnw5xxjJQxlCJ2M1jfbn7MJY9BsJmqh17Ket2qz22oBK2aSA_HfMBMUIZd-a-rfmlFO59u89zA7Z81nfrWZtSpsP70R5Ut_Fl3Ylk8OgVc0ms5_wBp64qJsQL2TOT7GmizuaoIudN2fE28H9pVHjFaiK3uog-iC7SdaclgG-Huy6UFx3MH9CSZZWdUK4szydgzmeSxmiOZVAtr27qsyIz0gSZAgdZPh4W9lGt1erK7e9xqWA9bF0aeVmwfbtT_kkkQEl7YYR8dDj6DOTW8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=E94gpBhlMAsx6pkzFY_p4DqPWf6DiVeJQj2eWuNELPJfaYLbEGhDeF88_7qCYiNiHevfnw5xxjJQxlCJ2M1jfbn7MJY9BsJmqh17Ket2qz22oBK2aSA_HfMBMUIZd-a-rfmlFO59u89zA7Z81nfrWZtSpsP70R5Ut_Fl3Ylk8OgVc0ms5_wBp64qJsQL2TOT7GmizuaoIudN2fE28H9pVHjFaiK3uog-iC7SdaclgG-Huy6UFx3MH9CSZZWdUK4szydgzmeSxmiOZVAtr27qsyIz0gSZAgdZPh4W9lGt1erK7e9xqWA9bF0aeVmwfbtT_kkkQEl7YYR8dDj6DOTW8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyDULOY3Gv8vKlH5KAz047uM8VjUSfdmZDx5_ncEO38QJbf453nOkTGaKQTcS0POIzWl5v4aAsk9d1pA9QCONqFYZykoY9OS01jiHsJ6mvoXTxJxbFkI9RFDMcMTsruoq-rb7_276TRy8aEcqgBUZgDOEsJFlN3yhnysv2TnmqlA-TSLQDEaj_xascBFgGMPK5cNdirfEp2zIz4Aqy0s3b8OZqtOTqMwhG0_r8ARoEbBSFN_NUN9lMqEDrCJBtvs4iVfmxbH1tsr52cZ4q6rq6JEigVSKWatlBY4zFfdtlLw-XcgxweCVGfiUogN-QCwErLuWOagHyfcr5YvM9Bvzw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=gmMjaEKjl_PAOy9gXvjDIL8-wUOAxxH2RV-RX9jr3EVVzHqlcgrTKziIVUe_aeARnNJmdjQH7JIJJlDhfuxgt40UcwU8UR6glnUOsQVbSoFS-LDmqZOpOA5zNh1EKTAfSf_nlGgB2EAFhbPTMjnvgGcoXZNGsh6C3_DXIfW-TqHYkgemoc7cSa-c-HQcvDHEQyZr2_Y_lJedJGqmkOTS1jIOQcAO7dDl7TeaXYP5VbOxz_5hW9vzTK3vE7XpHKMGq08Zulr1rPnMNR3k4lwwisYmaRImxrusZmL23rIJnAmrIjluqXPz34k5HOSeKHFr06EA5oEVj96Y8auo2Jn0Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=gmMjaEKjl_PAOy9gXvjDIL8-wUOAxxH2RV-RX9jr3EVVzHqlcgrTKziIVUe_aeARnNJmdjQH7JIJJlDhfuxgt40UcwU8UR6glnUOsQVbSoFS-LDmqZOpOA5zNh1EKTAfSf_nlGgB2EAFhbPTMjnvgGcoXZNGsh6C3_DXIfW-TqHYkgemoc7cSa-c-HQcvDHEQyZr2_Y_lJedJGqmkOTS1jIOQcAO7dDl7TeaXYP5VbOxz_5hW9vzTK3vE7XpHKMGq08Zulr1rPnMNR3k4lwwisYmaRImxrusZmL23rIJnAmrIjluqXPz34k5HOSeKHFr06EA5oEVj96Y8auo2Jn0Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=o7z8SNla8wPiKn0Sf42T5k5cDO1mKH8TTzF5fSzlI8Wh6DKUI5IJ07-q0x7tIoTREmaSaaijPVZch03_8Rv7Q9FXk8G-rZ_HWEz2LPV93Y1-M5uRQHDSNUzqCU-DYx73OaHhjOZCBRIfrt5a3jIS_N0WozQW34-BCIQuPG9tGZD39HX1urkRjw5Mly_FHLJXuYn4N3_121FR2iq4rDqGj7_MwvRxcJSrDgowOd1i_lfsUEK3cQ2wcDYB4qew-cqVnCVq4V3ImjFxH-3tRJUviUQJFXixmi8nT0em1-PWHJnVlS5Rj9GaCy4oaQsqpbijXRB07yLfole6N6DkbSOr-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=o7z8SNla8wPiKn0Sf42T5k5cDO1mKH8TTzF5fSzlI8Wh6DKUI5IJ07-q0x7tIoTREmaSaaijPVZch03_8Rv7Q9FXk8G-rZ_HWEz2LPV93Y1-M5uRQHDSNUzqCU-DYx73OaHhjOZCBRIfrt5a3jIS_N0WozQW34-BCIQuPG9tGZD39HX1urkRjw5Mly_FHLJXuYn4N3_121FR2iq4rDqGj7_MwvRxcJSrDgowOd1i_lfsUEK3cQ2wcDYB4qew-cqVnCVq4V3ImjFxH-3tRJUviUQJFXixmi8nT0em1-PWHJnVlS5Rj9GaCy4oaQsqpbijXRB07yLfole6N6DkbSOr-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=W4u0EmUO0cRkjYaaPguEeQ2WZkH4yh-z-3D5pST0rXSseBl6lTGzIXgB7iVi4XKhq2upxHm-9bgs3yiwPuVeYLfHdfYMqoWCoL8Jl-RlbySgAZQ0SMF6q4_SfhFSaM_iM40RQqmnjxv0X9lVBF5SJ310XbebEq4_MAezJC7thnCQW6JzRvy_k7OZcerG-lTdj_tDaDzmsXtRgv5WHSo_IHFqqptv9XAL_QSkZtepvoKYWubR-3LjGzmqbOdx2spcWqpdzjTlo5uMLVec8ZHdK2f0KXRYcZK-OBtr2v8eswEbxp-TL2yk-B1psnCE65glp7fIA2_1E-SgHsnoU458Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=W4u0EmUO0cRkjYaaPguEeQ2WZkH4yh-z-3D5pST0rXSseBl6lTGzIXgB7iVi4XKhq2upxHm-9bgs3yiwPuVeYLfHdfYMqoWCoL8Jl-RlbySgAZQ0SMF6q4_SfhFSaM_iM40RQqmnjxv0X9lVBF5SJ310XbebEq4_MAezJC7thnCQW6JzRvy_k7OZcerG-lTdj_tDaDzmsXtRgv5WHSo_IHFqqptv9XAL_QSkZtepvoKYWubR-3LjGzmqbOdx2spcWqpdzjTlo5uMLVec8ZHdK2f0KXRYcZK-OBtr2v8eswEbxp-TL2yk-B1psnCE65glp7fIA2_1E-SgHsnoU458Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=t5w49Hmj6cd5j_KsTRczgr7Mn6-3esuBg5oXUCXrMTRai3jkIHfnjGNszunreYnKEO78qkdTkm5TJ2GLND-rYYjTmeA4id4HZFcii8MfSeR0xIqnXYQneeogSY0LHDkDmKJkfDt07XhW9Rv-wYYO7swDLK-sn4GRLKHn_Jjv-q03mnbtJrHNaLJQDs81Lc1N3PLy2d0cd6C-w3CpTseJ8RH95ZAtLaJPakAfGujhkYuiXJmTVXk9XNlfbeiSq4mEFvkJ3YIVijy-fuayCWFDs2m62WnXxBDyxtL82YhimEonvGoQ5ewhNfItsuG6uLj5fapqLTy3f2ipHit_FZGoLURTfi0SHfh_zzN0wurBRDb7VldI_8G9clE6g47UYQFc_LVwazgVNEJO2yz2bRG77IJGRhnc7h1zUxmBwzec_U6fO08QToPF1VHkdJqxrMis0mWQf-RtnRugijTgGkkcwp_cfWV81FYWganvxbap3pSGd25qQ-aEiB-rWtjF928to1MgP97YMdi_cKV6abojTKi5J1vyWTm3_7016QcJeSIfzLK1w5hcZgAuatmM8qmtPdJ6ryWJN5jUA5IFKqnEB4aC7SA7C9UzBTDIxC7iQRaHLECE7ggcYVrCbkMFJdc35ZLpcmkX09HHG1JtYOUFtCYAOyk_q9MU9DkBjrwkQiU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=t5w49Hmj6cd5j_KsTRczgr7Mn6-3esuBg5oXUCXrMTRai3jkIHfnjGNszunreYnKEO78qkdTkm5TJ2GLND-rYYjTmeA4id4HZFcii8MfSeR0xIqnXYQneeogSY0LHDkDmKJkfDt07XhW9Rv-wYYO7swDLK-sn4GRLKHn_Jjv-q03mnbtJrHNaLJQDs81Lc1N3PLy2d0cd6C-w3CpTseJ8RH95ZAtLaJPakAfGujhkYuiXJmTVXk9XNlfbeiSq4mEFvkJ3YIVijy-fuayCWFDs2m62WnXxBDyxtL82YhimEonvGoQ5ewhNfItsuG6uLj5fapqLTy3f2ipHit_FZGoLURTfi0SHfh_zzN0wurBRDb7VldI_8G9clE6g47UYQFc_LVwazgVNEJO2yz2bRG77IJGRhnc7h1zUxmBwzec_U6fO08QToPF1VHkdJqxrMis0mWQf-RtnRugijTgGkkcwp_cfWV81FYWganvxbap3pSGd25qQ-aEiB-rWtjF928to1MgP97YMdi_cKV6abojTKi5J1vyWTm3_7016QcJeSIfzLK1w5hcZgAuatmM8qmtPdJ6ryWJN5jUA5IFKqnEB4aC7SA7C9UzBTDIxC7iQRaHLECE7ggcYVrCbkMFJdc35ZLpcmkX09HHG1JtYOUFtCYAOyk_q9MU9DkBjrwkQiU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=d0xY46fDzTHNrnPB6RAHmuj29h91fF63wC-aqvnvTCiDImt29DRjbb8sEixLjnJfERK0GrvH0kkk2N7pR56J0E9xT7kA0nEexRsjcnpg1D637MWLdR2O5NuVwdDFE1NxSm1MXi_YONTdRErcjt76GpdN_9hBpr5JlV-exgpH7fAYYvdKncjauKQJH0pHlKuCV8hlG2EHp4_sHqtdjTZ36LE0WJMAmTRJagwykgD5EW6f9ewu4-x_WrqN7LyKrbNDSZ3-hb3tJRUeQQzLg2hskpEgephyLwYFutC8nAtWgKeRRrE6aAxUAtrmlIemis2PO-W1L4MlfnMqhJM6RMC04Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=d0xY46fDzTHNrnPB6RAHmuj29h91fF63wC-aqvnvTCiDImt29DRjbb8sEixLjnJfERK0GrvH0kkk2N7pR56J0E9xT7kA0nEexRsjcnpg1D637MWLdR2O5NuVwdDFE1NxSm1MXi_YONTdRErcjt76GpdN_9hBpr5JlV-exgpH7fAYYvdKncjauKQJH0pHlKuCV8hlG2EHp4_sHqtdjTZ36LE0WJMAmTRJagwykgD5EW6f9ewu4-x_WrqN7LyKrbNDSZ3-hb3tJRUeQQzLg2hskpEgephyLwYFutC8nAtWgKeRRrE6aAxUAtrmlIemis2PO-W1L4MlfnMqhJM6RMC04Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=L_fqsvm6v1Pb1kIKNo0NkZYrCX0FI6Vtx9wBYOTAbXjFZ-qCSSj3sJWGUwAEN0Go4WAGue2m219NKMYIU36JmmdaMv_89JjYMH2aZlRd72voItq9e3pYLMO9DIipbXMdN2wAxN_qvR3FuzFMmrBeTUMS1Yfn2njGCEH53z6FJSLaappiMWS-YoefHFFkd5HGHLVQeP1KbLU-T_j0_JteEaaE7PJ4uuudtaQOBu3RcIKU02r6ljFZz9T8Oild6ohanv4e9zW4N-UAukddtLI7pkwLkPMB524_-PvJ1n7iWDf9iSdWlxC7g2nktnvSdCusTSU8945oK4pMREoOPMsTMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=L_fqsvm6v1Pb1kIKNo0NkZYrCX0FI6Vtx9wBYOTAbXjFZ-qCSSj3sJWGUwAEN0Go4WAGue2m219NKMYIU36JmmdaMv_89JjYMH2aZlRd72voItq9e3pYLMO9DIipbXMdN2wAxN_qvR3FuzFMmrBeTUMS1Yfn2njGCEH53z6FJSLaappiMWS-YoefHFFkd5HGHLVQeP1KbLU-T_j0_JteEaaE7PJ4uuudtaQOBu3RcIKU02r6ljFZz9T8Oild6ohanv4e9zW4N-UAukddtLI7pkwLkPMB524_-PvJ1n7iWDf9iSdWlxC7g2nktnvSdCusTSU8945oK4pMREoOPMsTMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGq49bqH_53tw34sY9qzbnc8dfnOySthPRYkpjALq2rSMBXomNsowNaDkVtPZBdSvPrVZkPFVFVd1fv6gVLVV7-GLDBkS3Fcc17SIHxi8pq8rP3NiLNa4hEa-1XEmYtGYDhjXAYFPA92Abgci40C3ps7XdlhXcTU1JveaqB2L-RrctRxW7SIExfiZZRAf6pXJWsmZ35p2pfRSnEnFygisFUAzFenZiGMDYkoGb0V4mrLBWHhRG1_mmhh9RXo-dQQO5DWJ2fkIhGR1XV4l7Q2LoGpxa-M5GlEwMpulX692IwdlzmCM_7qCb5FD-31CgB76ed65NJrQewWAPzRD7X7aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_Cc49QzjUqHJDiM2JA5_TItS5p1w-uz772mYmNf97meZVQuk-x3YPyIuve1F2jawrn2Nk74e2kFTrdA8PYttjWhGD9vVNUAYMHvOA3_1dPfaPolammoxdQ6G6PbRZXEreAkWUji41HgURubNVYVEBryBPEN4XLAg8nAsapSkm7UcH4qucw4vTrdE_A_SHxN1UfRQhdOQTlvnprtMmUZrBpJxl2--baZ07koR5Qs4Ha05YgqJUDtTpsbOUoizoG9ZSKmYkGUI6EiwCBMEuPjhXNRMjPHHJh2ZncLvnYDMyE1U3c4AV-x82XrvhQbgN7lL1g9YYykLYdWNvKUuxklOw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=dDNjGy6id_Fwy0OTT79mE2MsE8bVilwH0XtK9djs_9oj1ZtPdL0tlNDmiHdDBnVZXW-8WkYjW7BpuATMAlOs-LBXoHBEQ1NWbVR6BjoB-c356erniPwfkT7Xjm9CHlHizdo9sdZUyrhfCKi0z_05VmWogMFEq6W7fLyaLF5pnmAe0wSgSxVs9c3qjqvs_3ErY3MIBOThjFCj-0CZq7JrqPQqIZ2PvDUT93IUtDgJMiv00Im97K99Sj2J_HIKiZ3Xy041DS00114RbRwz1mpX0XeXg04jl3hNm2h6U3sTLP17yPYTE5qVoWHpiWNcVzhjDZxAkK5GF1upkYK3s9RhBwvOGfJQwBaPL-UAtkBnG2dVdhu_o7gSnI3OGBpI2tppgvflv7hha7jDQRrmXRWYWVZlrNoYJK5hWnKyjVSxVPmof6jIsnjWTxMwc2TAnjKuaZx8UpdGLuzNUaGtEdGFwk0IcOKm7U3pDacUYOoqjJTS60b-p1z7tkoFVINwFX80p2bycRBhvdqhPDaTf2nqaduMKV1HUAgZMZSSzKEvirbfp3HqS9o5m2WzJJY9QQftwNLaK_AnRRgKM6-XQDn-8Qbb88COQ85uwiCJ8pbRqEPu9cmhUk6cB-Q82Q5ZL0cQeNYYJKswEmmKC9tklfq3hh3Mbs8Tf57A5wj7vsgt27w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=dDNjGy6id_Fwy0OTT79mE2MsE8bVilwH0XtK9djs_9oj1ZtPdL0tlNDmiHdDBnVZXW-8WkYjW7BpuATMAlOs-LBXoHBEQ1NWbVR6BjoB-c356erniPwfkT7Xjm9CHlHizdo9sdZUyrhfCKi0z_05VmWogMFEq6W7fLyaLF5pnmAe0wSgSxVs9c3qjqvs_3ErY3MIBOThjFCj-0CZq7JrqPQqIZ2PvDUT93IUtDgJMiv00Im97K99Sj2J_HIKiZ3Xy041DS00114RbRwz1mpX0XeXg04jl3hNm2h6U3sTLP17yPYTE5qVoWHpiWNcVzhjDZxAkK5GF1upkYK3s9RhBwvOGfJQwBaPL-UAtkBnG2dVdhu_o7gSnI3OGBpI2tppgvflv7hha7jDQRrmXRWYWVZlrNoYJK5hWnKyjVSxVPmof6jIsnjWTxMwc2TAnjKuaZx8UpdGLuzNUaGtEdGFwk0IcOKm7U3pDacUYOoqjJTS60b-p1z7tkoFVINwFX80p2bycRBhvdqhPDaTf2nqaduMKV1HUAgZMZSSzKEvirbfp3HqS9o5m2WzJJY9QQftwNLaK_AnRRgKM6-XQDn-8Qbb88COQ85uwiCJ8pbRqEPu9cmhUk6cB-Q82Q5ZL0cQeNYYJKswEmmKC9tklfq3hh3Mbs8Tf57A5wj7vsgt27w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJx0OgWVu-E-u63JcyDbwWNVbM_Na6imW8A2K5iITtEAKLrCg9r1MYvz-P5XCRRbA85kXwnfq_ATrLeVbSBnf0QJOYyEds8yHp0WB5bm425_ZoCnIGSqtjF8VfNKGRRH338AN-t2mKAxNYwBlfBOahjZiRVyGINPf8Mwmcn6SgLCeVv54Gixv4aKj-hiG6TzYMZ5yS3lJ-rplDi8SX6gM9M-DorSS8zAuQD8cUDrvzpVz_umS09XYBz3CUKoPfYOSB2KC4ZfH1YP918r4ae8srMM8Kzgrm3kmrRX7OV0kAJfKiBHjRgIEvkEyxLv_fNqOsVYUXwK3rsvhJjqLAmRdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uv_su1iMdDzBEdb2Xix2MVwu2Ebx178CsgQCBKPBUaYRyOfHxXB-skP5G0xobqdjBn8WrBx7fZq2bWfAWq67Oez_2PUcaNenIWd0w_EIWDyxvBMByntobSjlspPtOQ5FTkOeg4VY3vDwHGh3T1-mRMEIBfgfIOhG5u_aMFs42xmqYejKyHQrtP4jCgxYZtRU8x7AtBx4rHhYXqJpqLLyIekzRDOaGU47-guTPj7H9xUu7McX1WE2ljBd6fZpHl54BexQHVNt3g98muBienlWLQ0kW_faKNoMwzeeTyCx76H5JRQTep_wEhZ-mOfZMkP6VkAGTjkIexBjvshaiqnVOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCzZL5wmSLRftyTu9gahyBNSMTfrgBpcMBM5YpA2p26ubWgcM4XTDU1VQXk70cAOKn4zeGUtcdwuUCF1sE0fTZ2UkNDM6S8o3AMtPe7bgzeOiQ7J7bv4zJl8Ag35EDSrQ2Uj94g6sANTzxKZ3h7o1WAt98g5LU7EYjQHY2vuS5kkqlyz-WVL3TiLCRhz5hLaTOq_CJQffN9JT0PmQwYkY10P1YXacnOEk5kgOQk8Pa6xABqC_GXv__a5LFZSR77Tsw29j57aLiitPvWdmpaLHLn9smi0z4_2E8nU4lB442U459vM5brIhkUzk7LMrkzg3AMy878PciN18NU-vIOmAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoGrxeW48RQyeChKB4vYwTokNMBUACZVPviEgNxjIG3zXsSZM0lhWze-TE2YtFFd40l6hxwK-8Sl-2T3ouWYD_b222GkjDF7oq4lPSQtd4M3kEAUXfmOQhyjh180C0yvkreZ_q75nEhadOIneWcHlq_5XBZ5cauqvc1EZhPjcibp7bvm4ZLa60ncqF7uKE1lztn1aEX1mnyFfioizcnf9iMjL4RARWXlyvmsrgJMyKq1xPSmg2QqnBXKINgZFKlnLcFOIkg-mfO_5nyVcdk8bCWBJtcLHzGFtqIL3ukQmfUrlMI8wvQ99jQbVsxTx-PHakM6pIn0pdpj-lZo7NrcBQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=v9qkKkdau8vcZf18dF4kLOATVwnYwoehwwH1OycePv0BDfuHOJjpsjp2DGTQsVIW8-mN5xBKEnv1CTt49ez-OroAUEOJgn206BKt3UxPzGCR6Z3846YYaE5mqklA2f-6nqK-FWvs99GOkxfZpKsEEqZGvGZGo14LKMGxibCir47EGWV651XZToX8BYil3bUb32RmWN44JQ-Oo4xp5eOgulZ8yR6b7YXboGF3ig-cClpYF27N4NStQ-yufPVvWF4-FOqCNfoduG2IfTHE4akTuKBdFCASAX56aXscgvyHRofNVVu0dPRf6_njUPLQ3nRqzFiUMbQbQ0GWdMP-xBsrJR6LJ9ONhX3lvTmBiYU19ySGwndVk5AjEK8GrUuAAC4toJYQvhrrKWY1Wx8t_EiCWZeBoc7EMeCzx2vGdP7WXmEdGAEEqKA0T5bydKxah3p99hfIOH2iJSkE2TgodcUx5vPmRNSnAP5A7_Tznost5oQhlbbfXR85OPXzcNVwh7C1StqANVGWsm0GnQ9zcjE-mU5VPLq966Q4oX9svs-if3EUB6gq2EuliUBROUieNXaVT4Me359LN-Jn9nzz0l6l875y87YTZRClnkcohwGL_T2sA4Ea6WjMah0xSGX0A1SHKSRjQSvyz35e6sN9FkUOc5d2lmycsjUDNAy6cDiflqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=v9qkKkdau8vcZf18dF4kLOATVwnYwoehwwH1OycePv0BDfuHOJjpsjp2DGTQsVIW8-mN5xBKEnv1CTt49ez-OroAUEOJgn206BKt3UxPzGCR6Z3846YYaE5mqklA2f-6nqK-FWvs99GOkxfZpKsEEqZGvGZGo14LKMGxibCir47EGWV651XZToX8BYil3bUb32RmWN44JQ-Oo4xp5eOgulZ8yR6b7YXboGF3ig-cClpYF27N4NStQ-yufPVvWF4-FOqCNfoduG2IfTHE4akTuKBdFCASAX56aXscgvyHRofNVVu0dPRf6_njUPLQ3nRqzFiUMbQbQ0GWdMP-xBsrJR6LJ9ONhX3lvTmBiYU19ySGwndVk5AjEK8GrUuAAC4toJYQvhrrKWY1Wx8t_EiCWZeBoc7EMeCzx2vGdP7WXmEdGAEEqKA0T5bydKxah3p99hfIOH2iJSkE2TgodcUx5vPmRNSnAP5A7_Tznost5oQhlbbfXR85OPXzcNVwh7C1StqANVGWsm0GnQ9zcjE-mU5VPLq966Q4oX9svs-if3EUB6gq2EuliUBROUieNXaVT4Me359LN-Jn9nzz0l6l875y87YTZRClnkcohwGL_T2sA4Ea6WjMah0xSGX0A1SHKSRjQSvyz35e6sN9FkUOc5d2lmycsjUDNAy6cDiflqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=sPpdEBIRm4U4pLWedTES8-19jvrbY_Km1i8SMqAsbZVP4kUPOxkorGMgjxuNWquSG9xKsU6hbBeTanbJvaunBrCtcKNLaxX2v9mpMUaC0dOLUo9bcy1_aEBm_XqaFxTJjlCef-O3ifN9re0Sa48mOWeyN-iHgXr6OdYU9z7ppmRUyTQl-CdFEJnQ5w8jS-U1YTQXTr3icsSwXhJN3MigYSBcpQ4t8RWOOEImEbYXhyg6GKhSDI2EGW6hL-k4AYUM288tsolHn8_0q0lO-2KVlTdFeIN_iVuzc1XvhDqGZEbd2oFrtH4OgVRWv-s-h3OHC8Jc6dTC1fcqS1bWW0Mz5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=sPpdEBIRm4U4pLWedTES8-19jvrbY_Km1i8SMqAsbZVP4kUPOxkorGMgjxuNWquSG9xKsU6hbBeTanbJvaunBrCtcKNLaxX2v9mpMUaC0dOLUo9bcy1_aEBm_XqaFxTJjlCef-O3ifN9re0Sa48mOWeyN-iHgXr6OdYU9z7ppmRUyTQl-CdFEJnQ5w8jS-U1YTQXTr3icsSwXhJN3MigYSBcpQ4t8RWOOEImEbYXhyg6GKhSDI2EGW6hL-k4AYUM288tsolHn8_0q0lO-2KVlTdFeIN_iVuzc1XvhDqGZEbd2oFrtH4OgVRWv-s-h3OHC8Jc6dTC1fcqS1bWW0Mz5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5tca01-PW7qvuBVDmz3hlJhGna4o4ubA58aatk3YLuHN8NXyW-vZ4DHpjz0hYrcYoJWd_AxNL5nRVVS8-kQ3XjnbsdCOGvGsYGoi_PvjZgpbSIjwstoqHtcMYEm6veDlDaYZM200OgumOw0eHj91sv9_MzIokPJhu5890pSbvGbPcG53Ok_hl2ZX-sFflb68a6BYTQcQyLCVR7bJ6CUonBK8l6UCzZouzD7cJb3OwPxZ7XDR4hLZUCUE2hFbedcqKQ4eAQggmFJakKCFWaR6iBu_3MNh-SZTh0QODHd6JCvPtR27jZZ0fTx5QgomUcefzGtF9x9HtBb5uue4WSi1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhLI8cKEmS1DBOtz7Zy6fkSrPADAzkhNJt-G_q4n60KJticaHMgW6HLomilnuhEDhCfgj_3RktKCYDbl4pM07FBBNZznhZptwruLFjdpcC76qlYv0Vvh5YJhrn6GmzdtH6ygzI0ScJAvdUUtTO7IHwOTBh3xC3H5zPgiBr-G3KATUJ5_x1BIzLLAZiyYORyMAhcLKholpKSXFW92KrBA4Lv5L1chV_s8Ppz9S6Bhe_e_AW4Pi4O7qVlgVKCsp3ZbSpsJU3bwK0tX93cI9OoyVRbI4p0mvhLJWJtuVydetPLoEr6DH_TxnQdA97ZjFMyL_e5grX3JPKsPqOpHd9T5SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sucdx5A31LTyB9KFmrv15K2I26VyYaJJn19otdL-vjCS3aOMZxzjVdboTa0ZBM1qyp5LbkRq1OT7KEgpmY_rO3w3r-axzY15bAAtjYEhqkwyAtWP95Lc4Wsv_O6xIY0Gd_PB3MziAAxKaTey-TREBSCyyWIWNq6SOl1Y0oJlo9FmNNZ78Y3gX8opXh8ba1ZHkpux5Tti9vsYpK-0XaW2vIu2GQoNIjYY3Q_sa0exXyqCxmIsgx_LPouSze3BvkV4dB9a6tlbMNHbnr2cKE-zU4mxM7JjtHjCH1jmMtoPGkGfmyLmh7mPV-qfjb4V6ZoKLAC_p4LIEJhPy0eBxIFajg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FGSNfLkB1EPGW3UAaXf_vzLUo5ufMorAYF2cBoguA7z-N6-rOLmIkp0L_WP-cIjjbh5CHTXf6ZeGKSU4G3YAx-zm8z9GxCvJDxN_5zV2FAUq6rP7ET0dFXqCQzXrcW4y8TScdASwLEeTIFF6X0RxZL2cBB8SEQEg7CATt95YZhTgEWiKO_qoFfr0uCx2tPm9j1u4vqsDyE901opTgfKH7FDyy2B6J2CSi2Ls7I0ivLrZ6FcyAfnyYrqAMbGkJ6tTv7fX6YxtzWr2EQTZbG-4ZzYHw-aOGTIU4dBzdCbSKSIYVbChdRQKO39_jiIjgL8FqXtB2sTcFR5Y8evBKrU8Pw.jpg" alt="photo" loading="lazy"/></div>
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
