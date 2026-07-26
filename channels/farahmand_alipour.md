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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 00:54:15</div>
<hr>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edDV9CjvDEqt0FpOCHD_yBMDypzmgXqWDY6dm2flpjbY66GvUL4sQSAyT3XYf8jk0beJZo-zX0dyZV818M6lxpZaAVMpjaK5cSjIzTimwOMvAl6FjMhBVPDCsROKEw4lITOYG6pfAxO-n5f4IP9JkXRt3yE_UrRjUqWMRc9EgERWhoKikDsN7ErGvFJqz2EQQvYoGHtiEYo7Ffpbe6NwDDk-8Cux1Fp9OkuJtYCF8iFDqdPRjgtwoc4CgP3fc_7_16dFtsZ-Wpv8SPuEntbB2OnohSG3WS67R6Xlz6QKF74CxWkraJ9hCNDHxQE4xM9BgfVQ9H1Mf5VfHnURQI69lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MGrnjk1HjFh0sQjWt1erjgerVUKmQwtCoOrtugTug8iBR0lte3ckwy_LfEktgD47Kdjagkzdmx-lmYYUCUyaTJDEFc_IBlZQxp2Ld0OXLW7o5_A-a8aYLU_IJ7RLpxzD-8EqeGHmIbHo2NaVDcfoUUGcapNMbnNUEKxy23ZrxcvHdUfwNNICL37KwYamjdsdPhHsk2frJx6EE4IfyAe84xk-NeDhA_QpKGJ7eZSDxPerT9CaZ2SLjkGnG2BNoylFVHHXplAVSrs1lC5QsAb4GWJLA1MnUAIj7TIkiuqneBD8y80PDF7UVAZ7O5ZOqY7PwO4ieUgX-z0_HurUmVhdMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BKZez46Xn4GI-SoA93oRq_kFbqKOx0FhD07p24HU9Yczv9sF3dSWgZP7hsZseQCXO5QKHI-cwbK4-Xhm7GCrz-xiB72zkRArw8zvULvhnW9-fVXA4OGqwPeenPm3cyBEe0sYCqmzzXU0KzjVmkmK_abxp58aZM40lN15bJlnzZlakqpsOXztFmWv8s0ClZj4fk54TycjiPxjeSoJ8Jx_i4Bn_ZRA2KFGKI-YGY5lJJ3FJCSqsc4qVJLZqIQ29vVuzZg9oxrWXawFVWqFkY_-U0KQ0Hl5I5709E_TENYb0Pbe2_NzBpuNA3fmjnYSkkS98oBJoDjtZyxNudnuj5cGmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IbVM70X_5_B7MbPQQs9gr8NsBiRoMGSEHdTFwlvfMy0y0W4ZStcGrD1IyTaIv3OLMU02GobSzguligzXBg2r0xyOi03HhLJISSbRW1j0XNWh-0n8UPiEqX6cj31FjiEFEHwTUkNHMvmLSEjTbERZqu_GqEpPLhKHfKDZowkYC69DMSQyyzrDtTnsWnUXGjvrOQ5nHP6_THjDyfSUc5cWeccv4Tvb4rz5LJlX73ijolFhRLbDBCYD0wyIOTz-FkwhddfyeCej9xL6NCOe4X6SyWWthLeBuZ0TKMrEBUuEXfOxfJ6F4g0APziCA9_nPaoud2nxPv5AaBM41aFnsJF63Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEgMOSHveFO1xJ4gaGdBP0WhAis7h53aEUtzooS6oZsV5BWmFapNHX5_q8raGiGFQgCNJ-t21nnuYkojlkvIDFL6fbCtNWF_oWtlr5BPhsrEamfepi-_ROQHb-BF0QdOAZKhyWnFUaLVnFIQVL54n1MFatBqWE7VosQ7LbnX7VORu9NAfcvu41FJ0YpuFsCoWRYo72zV4QkE5qgrPA57lUV_D8RmwNMmlfBocJMYeeCunRHitTslXVOLltk_7xu8jkVUepKElX3CuCnHev6ZKqdC6Hcm71Hq1jOaCqr1kSYtb52zbkcqXabLKsRR5NwJcrRgXSfxuZEYAJ1da8Hhqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qJVNluKjno2kvVW1LeJV789-qsdhlaDztbwc9_KE8uv3RdNNBy0BE0FcedZz7p3uj30UtywUjZJI88RQQ5ae5SQSfjUFsrzAYyErh4_lTeEj_3f_G6EVLcl9yh5Xb_ORh_ki6xB-aKgL5yLtkLrHEPtoRKyBmpDz4wRmeSG2flhTa61va8bhH90wf-UPgL7QIhLBxf-xdVgolrp4f_xOFvLtkWl7t0m-5eB92bRYMc0vAAsFoNG1GpPA3ZxpGso37cBIRsHA9cCOcormPNmPbqHKLPZZe5zDXVld72TB67F5JlGIf_5JKL6yqLDDg3LwEhJoeGw4SIvpquvm3VmCOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/km_yo_hOZjETIqxDOpoRwrn9pCGcx-Q7HgBzRaHt-bwDl2ZhP-lVKmNQWBFBq3PCm-saEqpdavmVwrIBoy7hHg25VZw79oBrBCrnaqjtRL3Gxaz5SeGCOgz5Vf9ySgnNI5R93hRJEsagVnmcejm9u-QicMGhKyqWcuz-GlWNr1xxxVaMMmA0Rz4u0Hsey3AKyyDFCEui3kBHd0uQf0cp9EHzSuXhWNzfdU2CnnQEpczyN6lTgDqHzBY6zXRB56lFvUtQzuJ8H1UhFYv5cbtXlsFY2EO8EZh1so-LXpmAnL73peLRi2ouXCgsdadEraDC73UoVXA3OEVOt28Grgg7xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U4JTaf0vHrdOtGcnXmHTq1egQcb3xOXdf_W1gw5uAiWtzNhNR2dlQ6HG946Tm2aCi7MqeO9drxwVv10XxZ23lTKz3u4LB-pmVFIfY9Hr9asa8sS6oWjsD0q23JwS5f0Gi0hZuf4TmFxy4AizAVisGkf8_TYrHIz2ioumaKVzKmEf321pRTKIbaI0DZSsEphn0BupyYqKQB9XjtLHAklpu3ZfHiBSvCr7iLsM3UDkU5u-UJYogGBUlexjdX7BTKgOry7u5v4dgqeZEjKVn8H8fjl6z0op5q08lgNwUEI1-8DFINnDL3efqLZ5P6H1t7p2rxp419HOuOtk_bgHbt-TvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zh4h0iRyK5zhTlNO47O1CQcmXb_9PkeeFOy69p9mN2_9OigEeGrjVpgHtviV5SvNDbsXIdK2JH-G5oI5LdSPHxI0J0fAZYlrDyZajhAiYO11uL0UxuNoKw0LPvs94wUIcuWDQeMNJWEtiJXYrfO6xXiMw87c2VW2yxPlbCQkKocjVZJRG7IP8LQ74h0kkPIuFi8KKqBMZOoyuKynugL6Bp0po_pOvKUyS2FRCrdrjvd34Z0BrPUjcyjA0Eivi1b3wT3ETXDTHJS6S8ygri5QjAcUxKR6rStIJQyuqS-BazXTC7tGsQJOneEb55VES5-JZSBb2YTr_ZpGRI5afZDCIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVHNyHPeagSnxkwEfmIrKKeiocZOMLHac-Ampa5iYk4oKWnbnUQ5mmDpj43K9ZZi4ScMe-SFPpbMZp1b374940tv8hyRarAZClhCYlCNkGyTcpRQds0j95atYiMfifXFOZGGgkLPwwPfCRVRR0k1WTNcrkBJMJgZ6qvZk6wpv8qiVbtOlxQqaTASMiclI7q0gZK8jMWIL2hhoGbNqhuD_Jfle6Y9VBm_9GALlygBHfOXYwj9mjO04vM28hgbpjJbAiRy3v1y4AFppInFPv60GbmuRu8QnFNqagehXpjfvLfF9y6oQ41jn-rk4p8tS8jLs4_knXKQ7Fkm41mt_U8Nxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vU03JBBIUrINr83zJT82G-VOKqE8hOi6VDow9Vk_JrqmtdlDqAZ4VWG2z6kPYKYWnTvcu1ghQYhN8YxdE3WNEs-puYUx85kYY4Gj7TJ1HIHBl-Z1qC3StQRjFiHbT7CppiHHAE4v1oZPOpZUMXOfdcUN1h9ilzqqgRBd5aJhbmIOAabbejFL_KnA94YSUmqaZULOPgbThc7gMMVMBuJCRXVs-BoDbGEmpCSNmoXpnK2UBLLuvWLwEo0C_AmejZoVeeOOmnT1FrgCm600e-Zya7Q1SPA1SiH57ooZqksGRi7Mt7Z4_If_Z6p7vDT3ipcJFoN3pXnyeMra1mG0EJK7KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">عراقچی در این بخش مصاحبه‌اش درست در خصوص آخرین روزهای منتهی به جنگ ۴۰ روزه صحبت میکنه. جنگ ۹ اسفند شروع شد و عراقچی از مذاکرات ۷ اسفند می‌گوید.
اینکه جمهوری اسلامی در مذاکرات به هیچ وجه کوتاه نیامد و آمریکا را به این یقین رساند که مذاکره نمی‌تواند گره منازعه هسته‌ای با جمهوری اسلامی را باز کند.
عراقچی به صراحت می‌گوید که چگونه جمهوری اسلامی تحت رهبری و افکار خامنه‌ای، جنگ را انتخاب کرد.
(با بی‌حاصل کردن گفتگوها و عدم انعطاف)
وقتی مجری به این نقطه می‌رسد که جمهوری اسلامی می‌توانست در مذاکرات، مانع جنگ شود (که می‌گوید باز ادامه میدادیم چند سال دیگر…) عراقچی می‌گوید : تصمیم گیری دست من و شما نیست.
این برنامه فتنه‌انگیز ۲۰ ساله هسته‌ای که هزینه ۲ هزار میلیارد دلاری بر ایران وارد کرد و حاصلش فقیرتر شدن مردم ایران بود، این سیاست ۴۷ ساله دشمنی با دنیا، این دشمنی کینه‌توزانه‌شان با مردم ایران، این جنگ‌ها را هم به ایران تحمیل  کرد، که عراقچی همین جا هم می‌گوید: مسئله ما زیرساخت و تاسیسات نیست!
«شکست در نابودی تاسیسات نیست!)</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6359">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پیام فرستاده برای «شیعیان» ایران
میگه اون روستای شیعی لبنانه که کاملا نابود شده،
اون یکی روستای مسیحی لبنانه،
که دست بهش نخورده! چون رفته متمدنانه داشتن.
این هم روستای اسرائیلی (یهودی) است
که با اینکه تحت حملات راکتی حزبالله بوده،
ولی داره زندگی‌اش رو‌ میکنه!
و میگه دست به اقدامات شامپانزه‌ گونه نزنید!
چون - مثل روستای شیعه لبنان - نابود میشید.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6uXN6AIS_5MoIUxC8Y7ktV9p3gNfFu3TR5dpzWtVtsp3ak8GY93NMY5gwTvkLt2EP0AgE26uNAI_5mZ3VS4yzWja7DE6sXcoE56ogTN57GbmcmCRrA99--Vl-uze9Smv4aNX1gBfVF6WnA2ku1E9ydTd69jXDbsfeB_G2edKTeEithmOACjtkYiRBGD__x46cvX0KjphzHYInXTjdn8nNCCb30QIS1IOCAXqrqHtx1rzduST8WOJdn3jn7vio-1fxqGa-uTmg-MMfU57p15zqKAnsO24gUa4ZDerk2oI7emoQCiqoFEElxZX4AGfdV1oK3aX-dd4PJd0FfIrBrWXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=sbQauYGK_yct5jSqSDekANSsBB45UeqmWBjTQl0jpMsc7SdKK9tjol9pdQSin9oM1UpGJ0o7cLiPL-dGpStISmubhe3cDjbVFVQaqge9799lsBzQgZXp-fXl4KE44RYMiKDJbrFlhqTEH09RfH71iL90oyZEKZhFrLSugXD75Rw0_8gZiH-ImM3j3mOjoqANpwebSmwmeZEoMEtZWl0YzfLBJhOhmAYSQAGsX1dEVN3jHjYTD1EJpXV5iweIWBPYyyb0jUHaPO0K0qIqvytlyFcVyeHr4xps1IfGRNgZAQVcWPwthFbacBEvF9ez2cnvunuBYUw4NB0ebHXfRCPvdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=sbQauYGK_yct5jSqSDekANSsBB45UeqmWBjTQl0jpMsc7SdKK9tjol9pdQSin9oM1UpGJ0o7cLiPL-dGpStISmubhe3cDjbVFVQaqge9799lsBzQgZXp-fXl4KE44RYMiKDJbrFlhqTEH09RfH71iL90oyZEKZhFrLSugXD75Rw0_8gZiH-ImM3j3mOjoqANpwebSmwmeZEoMEtZWl0YzfLBJhOhmAYSQAGsX1dEVN3jHjYTD1EJpXV5iweIWBPYyyb0jUHaPO0K0qIqvytlyFcVyeHr4xps1IfGRNgZAQVcWPwthFbacBEvF9ez2cnvunuBYUw4NB0ebHXfRCPvdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حمله موشکی اوکراین به کشتی حامل محموله نظامی روسیه برای جمهوری اسلامی در دریای خزر
زلنسکی با انتشار این ویدئو  در توییتر (ایکس) نوشت که نیروهای این کشور در حملات دوربرد در دریای خزر، شناورهایی را که برای انتقال محموله‌های نظامی مرتبط با جمهوری اسلامی استفاده می‌شدند، همراه با یک ناو جنگی هدف قرار دادند.
«با حملات دوربرد در دریای خزر - از جمله کشتی‌های مورد استفاده در حمل محموله‌های نظامی مربوط به ایران و همچنین یک کشتی جنگی - به نتایج بسیار قوی دست یافتیم.»</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4W8C02ySscLJP7zUlcpOPFg51itb0CAPC88AR8e0Kd8VcLR7rZUm5IR4l6E3LnSMTn8o4unwp3MTKjhcZuEaDxoRHoCy9Cm6p-GoCcb2qV7cRaCcifKfQagVRLWozSKzl1oereigannpz18xeruLSpelSQ66x8Z83oZEvQmMV2_LZPclEbuZ9iXby2tBzoTCUeoeUKk4SkL5mb5osAgvP2eaGWOpDkV2hflyRAwPmLBRVmQllhFn508w_b2rCcFxoIJ7_kjBTZVdPbUTzN5QZkeFkbpoumH30PauZDn26oqgZfHFZnf7jJdRcEE_8Lby0umJSq8Y7nFtPJEvfF1-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VY7g2gz8Oq_5MTvtcAnZVmmh2oFIu4QDBROeywqvu9qAzKtxRJlcLKmC-p_fmftgV0VFqSQ1LrNKWQ1_y0mAETHzGaA7d9AnpqV_UI7jk0iQ4xh1_Tss7j4DlxFeHVGZPtfZZPUP_kS-HpvnVA5J0d4244kbMi-IuqUB0MCRJaKhiX5JxbKcGOQeImZ2WYzajoZr6tSC2rem8gfyQFksCS4qlF6Le8a_u8CEQRm28aIfJn8iU1Y_AfUpVpw7ULO8Q4NTpEBZZNjSRz1S6_4R2Lyxrihtbb0AS7sgdkyOIZntOYswcIgh88axcL6wI7AjkZeTKwSvBqiFbxqgxGCI4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMm_ESU-hX2-8muoQSdzXE_BM4NLEtcn5J7l0m8TdQcx2vkrotM2d1UQIKqF4jF0jExUa07Mh7uCHsUifRB_4a-jgzjPkW8lhcjRTf0yW93aZ2CS0u1DWAfniKXkWiNMIcx_wy3qONuzKNkNeDlimLYsq62QWADVyNtcFqwW5C2SRZOt-O5aZ0FsKNcP-n54YlavS9Sm-sH_xh1G8BxWiVWCZYquEPGjIT99eFkH9Hock734ZczLuRLgWBOPtQ6hRnkZtMgY5EuNecQRI0NpBMzBaRIOrljn6VqsaOvdDmQKpF47Zw8nXGllxmdADVzB9WBvfEUGZPxehtHw0yDfwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=OoNh3p7yOiVPJOS5s3frux65EdEe4jlaDZgECsR5I6exSdf9MbXE4pGVnwZi7YWPNyZ__fij_d1Qp83wLtIMZDAv-KaiLiODyK6xe_UK2XHd5atXtD9u_qzk5lZAE9OLAgJbroCGR6OPDItN1NYpwAWpUPM7pi-5cNwYT4VEutL11GrIG5chsF-Iehlc-Kr1FEJInzM1-6NwQCqquUINWBIzU1kSm5kO2G6DcvUQlmUx6o_O386MhVLrExrNyDqmVzIMYB7ScyWX4UhyIiMa9lAPEWtcX3LpKxepyb-3GTqTEYeRNOTmrgWC6sh3ysXcsb2J3TWCgKN19gjs8aJNEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=OoNh3p7yOiVPJOS5s3frux65EdEe4jlaDZgECsR5I6exSdf9MbXE4pGVnwZi7YWPNyZ__fij_d1Qp83wLtIMZDAv-KaiLiODyK6xe_UK2XHd5atXtD9u_qzk5lZAE9OLAgJbroCGR6OPDItN1NYpwAWpUPM7pi-5cNwYT4VEutL11GrIG5chsF-Iehlc-Kr1FEJInzM1-6NwQCqquUINWBIzU1kSm5kO2G6DcvUQlmUx6o_O386MhVLrExrNyDqmVzIMYB7ScyWX4UhyIiMa9lAPEWtcX3LpKxepyb-3GTqTEYeRNOTmrgWC6sh3ysXcsb2J3TWCgKN19gjs8aJNEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFPCHHqOA0FLfWFsNB2N51-dg8qUSGOlhsuoKp-5jQY-a9rgjxhh4bmBTxEd0O-KcE54kMUfOM0qU2JbgRqvFVkyy3F6Mn_h9XAC9VpzM2E-F6l0BYacv1QEE6KEaoJpsu3DZNCS8IKyV-utDLOZm1_XzQBwNOJHA8UzfBau6jkGfS1FosL_ZBJo9yETdN2ah_QvG3EJ8Jnp_z_FEipKp0aytyEL3BPNcMrpwqE95X1QjO07Gsxx8YJvG3RMlfNfe2EiMToxLXb5LIxaPKjEzxuFkeyuo89ztm8xQQkMxz2uoPvJRlnaejaWP7c51-TOtbFUcwn13jUiWHibNbzd8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2KGSr0WMXfjZKUy2grzvts28sygJ_1b3MOpRMpeoCiMLj-mEU9GGHnUzjp24Qlc3okwQiYpB7J1pFtMyhByJkZOjRiwI0Mb0qJ3m7Xj2_EYwZqDTrYuJYqJ-yoTmpdVkl3AMn-OO8wI0k0Z7BSwQAm_nvmhl-e9gSRz0QXqbRLfZMd540vWa6A-rPN1iV8NN1Z-JfHidSpcY9WfsVI1rEmMVEqpdHOhe-1DWI8qIP-npFq9YaUYjg21YXtil1E7vO_HrvWH8eXEFiF74DTzAEiRbuVjiywGGJ4tWq6OvfghDOolWOkB1DgPv4H6ygvrwYAM95UDfNe5P0CO0PIpuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mp1qV_ZbOU5RtgiDariZacUPMAPBkt4p8eMqHXBbZeSTcMMA7fwQWLPz68VOQsTLWh0okjmpBxigppmYI8_roNDycy_CZflvPEtdtcLTmPkpSyPo09Sjba-4SErJVV1mC7hoiXlj_aTKwGqnfz-KQrEH68p74B5AMWXVOzLocK39Vs0VhowEPvWejWV5ahTt5rfZlAlsjU8hYKJ2G9TkKGXMU9Xihusm9PkkDOmO5jNA1F734I-uaKZbabsQMBywznfLe5RkofISCtLUXp1O72a7woTFoU96la16F7zarIh5q6FqdvC7WvSsi9U9mFUJUrv2AINlNcO8_wfXPhAi-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=jEo2LLS7YwDA2lBP6wXcX6QthEBhcdXce1nlFWopcAoKBKGZzTQV696hXMKZbp9_C6s5DxIRli2VqtsL1XN-2YEKWjM4GWDoTut6xTOL9sDEZ_-_pC14Xi6dT5nSNchfrlZT2nkykaMOKOy4Trl9AMuwSoYTXJmRcPKD1zJxoqZp016KpSHwLge2Kx25wY7LK1DQPZDszUM66mWy4ANQ2QxAaAwZeazkURpXSM40-JuJPBusAH_Glh4R92G21HN3AEwkcmIMvSFuEnidOosqlBcAyOelp-7ZkBjQxS53hwSIeD9yA8is3paZoe-k_DI-oWQPsmu_rLtBO9Dv_8XePQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=jEo2LLS7YwDA2lBP6wXcX6QthEBhcdXce1nlFWopcAoKBKGZzTQV696hXMKZbp9_C6s5DxIRli2VqtsL1XN-2YEKWjM4GWDoTut6xTOL9sDEZ_-_pC14Xi6dT5nSNchfrlZT2nkykaMOKOy4Trl9AMuwSoYTXJmRcPKD1zJxoqZp016KpSHwLge2Kx25wY7LK1DQPZDszUM66mWy4ANQ2QxAaAwZeazkURpXSM40-JuJPBusAH_Glh4R92G21HN3AEwkcmIMvSFuEnidOosqlBcAyOelp-7ZkBjQxS53hwSIeD9yA8is3paZoe-k_DI-oWQPsmu_rLtBO9Dv_8XePQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9aZv0Y7GVghmdTTBi76zG7NcYWnYJoxAZC7z1yBXdaLFCTCA0Qi_SeGocdk8HUu6EEskwl8n2Whl_Ty3XwNWkQKRb11jlB3nnu0N_VDDmkzHSvJaM1_5fStMMo_-7bF4UBIbPl28r_TZcHoeRsDWnX7SLIHxpgmGUamiyKGg0NktYx1_TuAdTwxERSNVWL5WUTj3xgeLC0M5pbg8m8gbFktMB8wHoKBQJJK3tFiZbbv1dfD3BkDzB-H6FO0HNs6KcRQ7qVT9jBdmljPUtbQlw-AZfw_cev9Hw2IS55TaSjt69Zsqq3Gxd3fLKRRn5nXD9WmgNG809xb3cTzi1o6Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=EWDffPoDxkY5NSRkEibQYLbM5DCZ6AMs-TWT22pVpCpkQGluwRjDVNxXgEnPpDr293UBx42b0izSpzhI4CH8KWmNocQokCXmhU0hv_-Uj1MSYDjdCHRQ7nwLvrEyoMubkEODy28ow8f09e6kgoSRuFuRlXCaPuaPnuGkvc3xjOzcRT3nsV4KyHZHTqizh3EtONATfHqKaZDd3OPUtYDG-zeGByUvCCee5kPZuCAUsCy_0bqtyePSSgxxmcpJ4O0Du0r5BZ8SY9KGzXHhu43MsF7rYQj_U1M4dhcik2m1K8cqR9arKJRDZVfZjFTmq0vO-HJJXDkLv4QQc9Mq1dj8hTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=EWDffPoDxkY5NSRkEibQYLbM5DCZ6AMs-TWT22pVpCpkQGluwRjDVNxXgEnPpDr293UBx42b0izSpzhI4CH8KWmNocQokCXmhU0hv_-Uj1MSYDjdCHRQ7nwLvrEyoMubkEODy28ow8f09e6kgoSRuFuRlXCaPuaPnuGkvc3xjOzcRT3nsV4KyHZHTqizh3EtONATfHqKaZDd3OPUtYDG-zeGByUvCCee5kPZuCAUsCy_0bqtyePSSgxxmcpJ4O0Du0r5BZ8SY9KGzXHhu43MsF7rYQj_U1M4dhcik2m1K8cqR9arKJRDZVfZjFTmq0vO-HJJXDkLv4QQc9Mq1dj8hTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0C-RE9hEvdQ-iYXpWE8HaB9xPAV0l2WDoGnfJO3f8LEaPxvpNVqpak7ZHcxfsleiwydSiZ0g3qpDgTBzGGR4i68Rct-Q1dR-YaSyxK3gqs8-v6nSIXLurQ_MRv4PzDzsjClM-7MHeHyGDSBv7RfQZ10xSHpzPG1IozUeySf-ADcHuJWeUrecyzQbL0AVAy0McHo1ObX_Fh6CDgMGTw7tFsqlPVjswYEsHqHs3Cp7zPV_hTH_GSot2rCGfD39iEmrypw8Hvd8xTseZpCFd5rZF1psWnkGkvhXy1aToeVpBtGUA5K04asulPIo-KgqmabgNqM0k0MDdL1-t-UhZHJvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c6c1wdROoPo6gH4mfU57AknhOTjq_DnTKb2WQ17GyB0tJ_7AziXLM59cwh89oziMHynXJIRHiUFSwd3hVcOD0wNcSbgo2MaCPZmpM3ZYJ6gSxbEovQwfxUDw98dCy_dUmeBAClhbiKRkmxlYHdEHCqs3E9e3yNj0uHiXdwNxWmkOaz44zJtG0chLHtyYkElLf8ztHE92qWIwAykhNXxSqaj71cNCOjIDwIgo9Qn5PR-C2e8_w2AagjZbw8r8ZVQP44_hlQK1RlyGugj9gkfbX4Jk33QCb8n6PqNvgZt_R1H_mtw7otSmlcjQyM5bJqDErnnUZVWFVjiEiggxUMC3Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZiEFF0JUZ6jOzB3mlf9R_ZuaHfdPbmUX0yGDutrjyDmpgzIyLcL3hKjwwH8Is-47Hy8VS_IQ_k4lRwco5cggth_bgJ_yvTb6VXFl3xTb_gizJfduM0RnDKdBD4t3oZq3TZNp3cHrfhA0WWm56_2rYYoDiHDj_iDnW94F5uSsIBoM6oX8TKWGzVhgebU_k25Qrk2kxPJcwYOLrj-MlIhUXA0Mq8eVbBwNPQXU9jWxItHnAnj_hQX-MFfmBZSUcVpy_vS_Xvhrff8SFLlVUbQ7rdUCBfLZLRErDfEriNtn0nO0WphB2ujOICPocKWBZGLjvoMH_zdFXbilOKBFirp_fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QI4D-WYItqoUTU-weLAAK9_qZMSLUsJAZ84F4gFJUYmE5sSIufGxdGhrCXVukkZ6EJvkb8dBMrq8B4AdgkrcX-8HljHzxF13drhU5ezL00NVEj0TMMUOB9G3q8SYuAnC3pcmxotN_jSyKQL-w_-rorHPXQzpR26lJpBPyw3-nQVgmZ-zWslqANf8JRyJnQq6rrE9an2o-zwQsGzRLq1VMYRadzBK44vwI3cIOxU4Y_ZpkfkINIaXQDfDrUGWCU7L29sn7R9afbhlsY4Jema2ldyXCDGYBbRojO4M7e1DjnqpcCongtBsUcSU0s-PgX38ctaPZGhleBHCMF3fJrTIBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwbLCCwq7Wm9GzyMWJwzkTg4zbxsXWTlcRl-jeOH2pwahS_zBWQpgcmENDLqM3behTxOkW_uN3e2t_iuJACr0LWXKU2hLCNiecIDg7pLd7vqeDiPsWKrDpwupNigCDDyGLPFppPP9daraWgtmO1siDXKr0FzanxdEFWCO2_pfvZ_Mv3avkqxQ7PdEQz1slHoyNgj1khVlZMcXI1sUvpAqGEHyn1Y7J4W_ZD2uydPXQZlQ0xB0CaI1NXNP3kbiGM8nklYTSDY257ObOZQG0SZrpJiSRthd-H8NX6KeeJK-TM8fx9ym6ez2aiMbUAOODgjWaiqK0P3XWGreqZL_2wHwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=K-6phBGRVo4leBNY7VzdUf_Ef_V2NiadVeN8EL8_rnPa2QAWxxt2KCcCCx1J0GOc7WKlPffOuz6I1ym4DNCb3USieKtFMJeYhs58oZMrFkR1MChYQ18zjqlXFTHp0ZlXEtf__AWxIdU6lfw7BiCOuurI1H07wRMcS7p5cBD_LBK5ADRm_uk25V3Nb91zfuf95x28qe8HACZQwa5ss1cSVtikfQJdlT4td-Krz5_x1-CvqLoLkaCSW6ymi0a9HRqrJ9g_WwNFJ_1ppFq6Vaj-juRNduDvIQSqZeKgzNdsNfwrfPP8MNlhLhEQFRJlTQBGmZ1jWd10225VWKvDczjAVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=K-6phBGRVo4leBNY7VzdUf_Ef_V2NiadVeN8EL8_rnPa2QAWxxt2KCcCCx1J0GOc7WKlPffOuz6I1ym4DNCb3USieKtFMJeYhs58oZMrFkR1MChYQ18zjqlXFTHp0ZlXEtf__AWxIdU6lfw7BiCOuurI1H07wRMcS7p5cBD_LBK5ADRm_uk25V3Nb91zfuf95x28qe8HACZQwa5ss1cSVtikfQJdlT4td-Krz5_x1-CvqLoLkaCSW6ymi0a9HRqrJ9g_WwNFJ_1ppFq6Vaj-juRNduDvIQSqZeKgzNdsNfwrfPP8MNlhLhEQFRJlTQBGmZ1jWd10225VWKvDczjAVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدال لفظی دو نماینده مجلس
بر سر تنگه هرمز
(پشت پرده دعوا : شهریاری اینجا داره میگه
که تنگه مال ما نبوده  که بگیم میخوایم بدیم بره،
و میگه تحت یکسری قوانین
بین‌المللی است و زمان جنگ می‌تونیم ببندیم برای فشار آوردن و….. ولی مال ما نبوده)</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5H0KFQf412D71ViNssqfKh-vHiWxZMseBMT_nxLdfKq7cXMo623GcNxuC0Lx1G3G_rGThTgI-SizVb6ZC-pK9bVXcBmkT-SRUXGMCBdn1B4JqZ2VySbbPl9tOpPu9TfXBF5wqX0VhG1RiQz5SDA1yuAc1kQHPjtet5wZbrwYOZs9d43wi7gpcKpK20J9EhBWSxxg-1gaYw0OcKdCqngQ0519NHqGA3wB_4Rm2437TFuhVnuPPL8ACAgKlUwmkwjyfH1dVh5LH2ptVXHWo-hOQo6bfNWRpDoukPQvXB31QzVeUEZ-wLUNiZem2FCrSlP7PCdtjfUsAMs-ULWwv5LoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfjRJl1hEI49OKWqVmpJVE-azFKd_H3L3V61xK1tfwurSRToLsKOZt31JVkiq5Vsr_e6YDW1FdyMwv5Qk2jgZQvkwNH7ohsfN5Vhh-56HYwD27k1fg6SotzslKNaK4wM2rV-LdEQ6EJtWoVKyvBGn5KRn6Q_1uMZSYRxu-e9_2-iV6wpTaMY7voVdtZrJ5sUhVuWCqdMnYcaopu2LNDPQWYEdHpkYtZwVv9-n2wUCVv4VjFJxjhNqb3b7wQr6dha6NgW177YexUYAsjGYC3pRvZAAaX15AKP9omVnC05x6VBOP1Oo-orkrVFh8kTLAe_ndt_9DXd_LQwNfiKgWIZBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=vwBr0_DG4eWhSBUZnicIrnCHmkgv9F_4h8MN8aoee4AEYtwxtxCydqiURXPJFuUSbclbXNi84rlhqC4PlXtzll7i8FPuBJGSufwsbl6m_HWHyX-kGAaynbU5eolSyoEb0PRKb1_IcC-9ahYZLMi7JhpliIjN4XCQGvdZyjxLi_L0hfs6Mal7A6uNLXTTE8diHcZKDo_7O2kxhpSKoGeSiOKAq3ZdA1iuFgxeDEWAIWflYVewVFN-jWRXn-c4oQtZpod65wm9u__ZPqXa43ODr6L8EtLLtpcUxcsgU3oh07Y407nZ3pDha6B8DZRjo6pS-ODTjqKRFCmt2e6VTLpMYzHMjasIYcx4r7bksFhGOyesI5-6_zTff4EFWN3_Ps0bZtmIp3GXw6jA5YT5XLOskUehwKZn1GOm3w80RUnrUl7fTT7gAXVVk-he8ZJtJugq8PS6qdLeVfKIvhYA8FvlrsqYc6wPpNlTSbRA-J7-NmgR4kdE1nvy6gOb6gKY5i8wnLWFg4gBFzq32eM3U7PekFEIQuDWiQPPuDhSOJx88_cUdw5ohapHrJCiNXW9gyvV5bBURqcGGgY3MSXeWyyaOu72Fzu5aBaPsM3_lX-2LZ8EDBRvK8iQLn3KoxZ_5-quJ-Jnhf0FhEGrwIFkiUXh0DN-TyaQZe0k5ubkhahxxHY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=vwBr0_DG4eWhSBUZnicIrnCHmkgv9F_4h8MN8aoee4AEYtwxtxCydqiURXPJFuUSbclbXNi84rlhqC4PlXtzll7i8FPuBJGSufwsbl6m_HWHyX-kGAaynbU5eolSyoEb0PRKb1_IcC-9ahYZLMi7JhpliIjN4XCQGvdZyjxLi_L0hfs6Mal7A6uNLXTTE8diHcZKDo_7O2kxhpSKoGeSiOKAq3ZdA1iuFgxeDEWAIWflYVewVFN-jWRXn-c4oQtZpod65wm9u__ZPqXa43ODr6L8EtLLtpcUxcsgU3oh07Y407nZ3pDha6B8DZRjo6pS-ODTjqKRFCmt2e6VTLpMYzHMjasIYcx4r7bksFhGOyesI5-6_zTff4EFWN3_Ps0bZtmIp3GXw6jA5YT5XLOskUehwKZn1GOm3w80RUnrUl7fTT7gAXVVk-he8ZJtJugq8PS6qdLeVfKIvhYA8FvlrsqYc6wPpNlTSbRA-J7-NmgR4kdE1nvy6gOb6gKY5i8wnLWFg4gBFzq32eM3U7PekFEIQuDWiQPPuDhSOJx88_cUdw5ohapHrJCiNXW9gyvV5bBURqcGGgY3MSXeWyyaOu72Fzu5aBaPsM3_lX-2LZ8EDBRvK8iQLn3KoxZ_5-quJ-Jnhf0FhEGrwIFkiUXh0DN-TyaQZe0k5ubkhahxxHY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=dDGfoAf4gTbab4O7WJR-8YenAt_ggQba6kcNUW4_f7kxutczzR9nEL9Bj3yajiCRTbN3MUbeqmpYIHaYF3UHzv1SMQLkWd4Rp2eBy3ii3Emu89UPha6S_WGiK9pasfDd7WARao69njqerNXqUk_6bTmFgc8JlW_VyeGsJkV4RvykgSa5gx4FaoKK7EaZZZe1E_Gkf7FfOqsy4ig3zXptVGKQy9EOJxhK_BPZ5qEEo9IjffFvUi3IRk7hC24aeuWUYqKmk2vNCyLa7aJ2zn8lN6cVAtQAU_DxwHzXXLJ3iRYK1JZpM1M8UX6WlYgr7fSg4nnngbF5kUuTJuOE6kYycg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=dDGfoAf4gTbab4O7WJR-8YenAt_ggQba6kcNUW4_f7kxutczzR9nEL9Bj3yajiCRTbN3MUbeqmpYIHaYF3UHzv1SMQLkWd4Rp2eBy3ii3Emu89UPha6S_WGiK9pasfDd7WARao69njqerNXqUk_6bTmFgc8JlW_VyeGsJkV4RvykgSa5gx4FaoKK7EaZZZe1E_Gkf7FfOqsy4ig3zXptVGKQy9EOJxhK_BPZ5qEEo9IjffFvUi3IRk7hC24aeuWUYqKmk2vNCyLa7aJ2zn8lN6cVAtQAU_DxwHzXXLJ3iRYK1JZpM1M8UX6WlYgr7fSg4nnngbF5kUuTJuOE6kYycg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=t-iLWePhESkLrxXqQiPfcAYeNYsh5QE8zXxwBYWtfApjSzcCSRHwjbHFZhRQVtwykJ7Ml0RMB4yvUkSH8WxNIORokDv4kdC29P0b-cGh_gwigY6geCIZsAHYZ06zy-vdHPlIppept9yUW2FnPvipDTmeY5mGn8oVTolfilTlxEhsE5cZB-zFST-8zDuj7U5aCztK3Vl0RuQ3TofNYjUPXKIPLw6E3kKA7GMtuZ55a8jyXS8yamkoNvk2n5EsqA0Ihs0cETXyla0T6SLuR2BzLpFrHsOS65mX84nvgzpkDz3a00OltxyqGkB5380U3ps4PZftv_2q_PXwtAvr_D7JIowHK8pwgpHE3J4gBxs8xnn5LARsAb9k9YqXbUZxZEI8CbUMPNeUOpxoCJSQw7bcaraf0P_QbXTgeN_kjhyCyjlQjM3--M7VWomRsqic-QedrLEMjYqBwAGhKAUO_DfKddnuQiUDQRXfn8YKdxt7JUoqzvzMmucePj0zgHcj9BrVdf-se_CxDzRqQ5ii-M0pwVzg445b3Oi4ly1BhcacCHlRZVlV2AWp3DmFBrK7VZ5rJVAbGpy6YkgNcDlW65Aso6l7FM_S46E3zwf3n748wTUy3e4Skzakl61ipxsRMYXnvsCgQJyN34RcXmV6ry4aL6hWKpSxdWl1NA49b-daRUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=t-iLWePhESkLrxXqQiPfcAYeNYsh5QE8zXxwBYWtfApjSzcCSRHwjbHFZhRQVtwykJ7Ml0RMB4yvUkSH8WxNIORokDv4kdC29P0b-cGh_gwigY6geCIZsAHYZ06zy-vdHPlIppept9yUW2FnPvipDTmeY5mGn8oVTolfilTlxEhsE5cZB-zFST-8zDuj7U5aCztK3Vl0RuQ3TofNYjUPXKIPLw6E3kKA7GMtuZ55a8jyXS8yamkoNvk2n5EsqA0Ihs0cETXyla0T6SLuR2BzLpFrHsOS65mX84nvgzpkDz3a00OltxyqGkB5380U3ps4PZftv_2q_PXwtAvr_D7JIowHK8pwgpHE3J4gBxs8xnn5LARsAb9k9YqXbUZxZEI8CbUMPNeUOpxoCJSQw7bcaraf0P_QbXTgeN_kjhyCyjlQjM3--M7VWomRsqic-QedrLEMjYqBwAGhKAUO_DfKddnuQiUDQRXfn8YKdxt7JUoqzvzMmucePj0zgHcj9BrVdf-se_CxDzRqQ5ii-M0pwVzg445b3Oi4ly1BhcacCHlRZVlV2AWp3DmFBrK7VZ5rJVAbGpy6YkgNcDlW65Aso6l7FM_S46E3zwf3n748wTUy3e4Skzakl61ipxsRMYXnvsCgQJyN34RcXmV6ry4aL6hWKpSxdWl1NA49b-daRUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/somxIOe-3_cTljzORdvBHwvvbGiMmFj-4a8ZZuwHNMoD99BUXTAT8QoWJI6IFvrPdkkwjRMY7PB3XK3vEifAcGIH0301kxw8QgTAhuR1KkKF226Q3AlKvyx-U-4FEABP-l5USxECKy7njHfOOctscaK8e3Ebv0Lf5JJvE4if9nJCSyaDEC-HTcM1Snw1uGh-AUxrULDce-qTDwAOEZ1GhPJ_cdncDS5iphNADpDFoxDMbimLLMsh5-e4JPr2Ov0mjwC83WlOxqs8lw2Gm-ru899hd0637H2WvoZuV9khdOoGvcLvTH052W79Fxkdfef5x5ZyhifsqEsm0alaBIK1yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDbF1ljY8wRZoJyESTfCBAneOaOcAjzVaOQ2wLJnKqZvowt8vsdy8gD565JNcC21OC9KNc5aKSM0wvF8HT8w0T-Pmk76cIYg0S0_OHLZav-lD_0Mbs4uruZUV0jXRog0OASNV11OcDIOEMjJjvEW6y-Pxr1BJDyTT_DDRZidQ7Hy-sekR-9WbFnz5PJ2I6hT7UBg-Fv3-g_oGn-RY0L_6ipMBL6T1OpfH_yclsSDKNJ4DGLVsBb6_95tQA_iVYumJTYvutC3_eawOkQ0owkTBt2f3k_5UahqxQn3pSIeSbDvr58ijo9yahmOvknU1EUYVOuxbcoFzybWtDFgJZoHAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTou6g-r6GVoHNjPQI2wPnlP1BS4CPB0ZSK82chvcAEqTELiCbKDKrHJiL_JE4cOv9W1ScY-r9PQarIW2WIjsA3zqew-lKTvvAiYHDFZ9x5d06mleCrrFqGbxUZ-CqDjK2pkiQ-UHWYgqJvY5ih53uAs6610OHM45YvAYbtEAwOI-KaNZkt_Pjf2B0Tv2B4xfiyShPkw8-TXTXV7hgDQktGLm7dFxQJ0AY68Zc70F8s3CDlUajks_OAaiFzySuneAu22qo6laiyK-QfxU7Kg8SadNGPoAtYdFlQD8g5aorgB9tMeLNohkVnDyV_MqTxxTmU8JMPM5q6QILzt9LfdHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=hDGBcudNMOzn-GZ017URcF2d3AjwRCDlK81rUZdpFolQJxxjk5U-mC6XkeQczIZZ783F2lmFHayE8Tw0_yfBcXXDqZRGmt9TiW0bFCaD58hFXndx_4vgJanbI1yJWam081qnGCWih5KYIhjG2oJ_oX5c8Z6bVx-cl_YR034wgFTwTFNYWTxt8u_ojC7UvowfiQYM-lBNDoMVle7nZhLukunboljbw9S5-6MnLJ0jSVr9w5X7_3N8NyDKC4SwvHVHHxGPhQKNZmHCihrKXDuW6wLf_ViBBkpf2iG9DqtpERBIr0voTkOBoBR5kNkbLipMTvzfVqdMHWa2nKfkpp0I8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=hDGBcudNMOzn-GZ017URcF2d3AjwRCDlK81rUZdpFolQJxxjk5U-mC6XkeQczIZZ783F2lmFHayE8Tw0_yfBcXXDqZRGmt9TiW0bFCaD58hFXndx_4vgJanbI1yJWam081qnGCWih5KYIhjG2oJ_oX5c8Z6bVx-cl_YR034wgFTwTFNYWTxt8u_ojC7UvowfiQYM-lBNDoMVle7nZhLukunboljbw9S5-6MnLJ0jSVr9w5X7_3N8NyDKC4SwvHVHHxGPhQKNZmHCihrKXDuW6wLf_ViBBkpf2iG9DqtpERBIr0voTkOBoBR5kNkbLipMTvzfVqdMHWa2nKfkpp0I8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovWDt6SJ2gworjO0zYLl2cErw-ZJepi2M_mJHJ0xmPGhCOVx42znYFdVgZVLI6vmoBatEhk3bWW2YttJRAgsKfaHN06NSS5u7ORC37LiSyMDhMyiRv887dBOjLLFLIZDYXshaQfGNVa9NrbAnZlMRV8wPpXMs7t5ZFzPjL0PLeRxvUTwOlNjzZ_mIeN2oG-eJoGNUaaNiq_EflJ_u28Jtwq2ijJyNX-J9BLIPVPAJ4KKfB9LBgBBwc8Jp3qh5dEd6gNke2DHHlJkay2p0FGFqc23NJ59HDW3TnWUZWXwfCV6JM-3Fr106jevD880rALrZHWf-lrzai4ykol8dBwBPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TtQz3Sj4prS-wWZ4GFCDQDfNg3_vrJ6jbKvQufMt-fApcfHKxlnnf0K6S4j8sUeL6obdjFIvRFzZSxt7iFYCaiOjK7Eyk-Dg0UsbPhu9bdYkXXqy_wEEX55kkPQZCoJAerz_Jwc-qO3nYF0ZgK5eCm6hhHe9NaZ-fc3ofMvgpSvtcgzok4eILyPsoi1oDmdxQt3lmyNCugTR2RCqeWqn5KfjzKkc2M_SHuN45jdciso4RHFU1j91CFHYELKddBsy2Q6dI17Ms1337Uw88BgYZQ1K8rkb3gAKcaioya9K4ldsZi-PknWI6xE_JgkjyvkNCdKWFJDt6ArlGHHlwsrPqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H8Cea9H0fij0KZFerza3Y_wS2HxtUjxe11doL0YY5uYQjc8KdoTqn7A5bpJh7obMH4DHUOZAE0NEaHfSpVwmyudy9A5qSRavwKcXkPItWOzEq_rG9sodqHVPlkdKDP60_G4xC5nLR7QtdJfIuMI4c0HJwFUFVI_mSLwWqZ6EzN7HMubsCKopPj2jjAw7ux5zuU-huGfBoXjLTGZnWiHeqH9ONfkiw0kx3geow-JVrtFwlAX3RCLJiGlqrVRFtmGjowr11g8ws2mQDz2LiMPfNdEcxIhzqMnRWvMY0-bnhCDrwooUimAB_VGsBiUP8Ixm8bTaNxk40UAR2xco8eMGbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTnUhM8ALbYs5sNYS9ru0asstD9liSWemy5zXC5sUIwzLtVcSwktumnClzvnoVl4XYbj2qsKeJCdDjCnybg1xkclPtwUWRMs6tbxmF6ab5HYs3c6GzzD3oHq6AUyhrqHahO2mYzk90REfGNE7oQe8xl-hntbY3knf97waw4ecvUViAXc7Jr_bG1AYAiyY3YHgpjr7JLvkbfLvNisQ9pNztPIo1yQrvWXoZJ-oR5PykBHR6gfJVRsypXk6nu9ao7pG1hXoIw-ESJ-EQVFzAtcn5ucIMa9Ye2HChYY17XkzCcOTFkiol-W4T_Y7KIM2NNiNyH9QdZBS01zHDd5yAC6mQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=Hy5VozfQrvxkXuCFFRMKCiK-qJV8YYzXzsCBLkbV_y8rmujy6quSHAdAuwFUPKyLufVdL2EgkfvcNasUkm0II-e_0i3AGhdv-9ruUucQEIS8UB7Q1zR2DSr3buEXWbpS910V6j5Hic-oiiIPh7052NiIamsx4xSvvbTeDzgQ0DOPVT6p7N72eOMzh9XGK7f_O4p1xW_JZ0lDdk33kir3KueEMg5qe5_f7k7GcG7d7dTF-fHAultRnhdnTW_RjFHnSWoXACNLps5R9tGpS6qrUn4-klaQRkB9-WQZm95VzpZGETyduTKVI7EK6IzxqG4YgryoJOqMDId9PnsOnpReW4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=Hy5VozfQrvxkXuCFFRMKCiK-qJV8YYzXzsCBLkbV_y8rmujy6quSHAdAuwFUPKyLufVdL2EgkfvcNasUkm0II-e_0i3AGhdv-9ruUucQEIS8UB7Q1zR2DSr3buEXWbpS910V6j5Hic-oiiIPh7052NiIamsx4xSvvbTeDzgQ0DOPVT6p7N72eOMzh9XGK7f_O4p1xW_JZ0lDdk33kir3KueEMg5qe5_f7k7GcG7d7dTF-fHAultRnhdnTW_RjFHnSWoXACNLps5R9tGpS6qrUn4-klaQRkB9-WQZm95VzpZGETyduTKVI7EK6IzxqG4YgryoJOqMDId9PnsOnpReW4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🚨
🚨
ترامپ: قطعا به زودی و با شدت زیاد به کوه کلنگ  در ایران حمله خواهیم کرد و هیچ کاری از دستشان برنمی‌آید.
‏ترامپ در دیدار با رئیس جمهور لبنان گفت: «ما قطعاً به سایت جدیدی که آنها در مورد آن صحبت می‌کنند (کوه کلنگ ) حمله خواهیم کرد.
آنها به دلیل سلاح‌های هسته‌ای در این وضعیت هستند و سعی در بازسازی یک سایت هسته‌ای دارند.
‏ما به آن سایت ضربه خواهیم زد. هر سایتی را که آنها حتی به سلاح‌های هسته‌ای فکر کنند، با قدرت بسیار بسیار زیادی خواهیم زد.
تا الان زیادی باهاشون راه اومدیم!»</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=ebulxj3UIPrY5ffU9QwZ6IpC4GGhFRSPNCgG37Q6KFSZZMp1gfWf18p5aRW7YRmISFIMsNahWphkhlU9aH2s6ogbRVx_jDhqIUO-_ZURf7AmWcUi6CchZjabk6aZdaHqdF5liLb1MjMKWJIMLGQ1eA0ME1nV4yaxZktQJqv5c1fdc6QjKGNqfEn0ya-6avEgb9cxMkv2BsLYFq9Q8pwaESXnu0WwcEDFbgz_jLGRHFlq8WVgNkK_gnHsWcDeYxVNHW3uzvOH0fHNLEdAfXEBFT01SKUFxk6iPYfsZ2JK5kRbgGikKmijD2Ws5NDCf56nt53xxUAYnbCIRnGHZIFSAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=ebulxj3UIPrY5ffU9QwZ6IpC4GGhFRSPNCgG37Q6KFSZZMp1gfWf18p5aRW7YRmISFIMsNahWphkhlU9aH2s6ogbRVx_jDhqIUO-_ZURf7AmWcUi6CchZjabk6aZdaHqdF5liLb1MjMKWJIMLGQ1eA0ME1nV4yaxZktQJqv5c1fdc6QjKGNqfEn0ya-6avEgb9cxMkv2BsLYFq9Q8pwaESXnu0WwcEDFbgz_jLGRHFlq8WVgNkK_gnHsWcDeYxVNHW3uzvOH0fHNLEdAfXEBFT01SKUFxk6iPYfsZ2JK5kRbgGikKmijD2Ws5NDCf56nt53xxUAYnbCIRnGHZIFSAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=P9De1NoSV5bw2zoD_MXS-6fakc8CXURLrn1G-iJN_TTf1DpLC_LyxSbcvVNTqNBLznA4NaGxzLxPKaSshjpHx9dB0zi1ZQHcVDLelqun6txDtkjnoMIcwnHdSC6SpJhjRuddvkJh-ErN3X6EbilCRJthvbGntMnm6yR24kAXDwwyFFBzWvYh5pK0He-OwgJf50m6AKy68RGTOP48OvXgoSc3LsFnR9pzlQlbcNlYd2L051IgiVYDXEMgZ7ANN2R4LdA-AIjsoLwBJdTBjJPfcfWrIsQaABnGECceRBX-SBZyNAlWoimYeAqW7LRwu6bLZd2c00fqNdM2RhJqDsKaKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=P9De1NoSV5bw2zoD_MXS-6fakc8CXURLrn1G-iJN_TTf1DpLC_LyxSbcvVNTqNBLznA4NaGxzLxPKaSshjpHx9dB0zi1ZQHcVDLelqun6txDtkjnoMIcwnHdSC6SpJhjRuddvkJh-ErN3X6EbilCRJthvbGntMnm6yR24kAXDwwyFFBzWvYh5pK0He-OwgJf50m6AKy68RGTOP48OvXgoSc3LsFnR9pzlQlbcNlYd2L051IgiVYDXEMgZ7ANN2R4LdA-AIjsoLwBJdTBjJPfcfWrIsQaABnGECceRBX-SBZyNAlWoimYeAqW7LRwu6bLZd2c00fqNdM2RhJqDsKaKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9vKGmmL-qM843ehqVYofRkADSJtnqbkH2pYI7D8r2CfADKw66kNQsE994yb5ywtFQHfUnhdqHUe2Rlg7oIp4GyxGDQIj60UPLiqyVYQ8OAm-AOQlsw7DWgpKNm7mbtutG5aHD0p75ekTMGK4Nkdpf5U89dSMZvOCEy6dPyn3XuPTijFsxGAFKJS9mQmZ3ty38MNh07hwUDGrr5kNgzQhv7WQfHepfdy9OMQVRDIJaqqvCc3JYg9LE5rtpFH-TeU0QuNTqQC66Fbljh2nYGE-uGuQ0SUgI7-yM5jH375Ltw2Dgw24sLRHxdhsMqVBZRifsT9QHiMxt4qaLLbTpO1_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=MnKnMGA5fD0GvKoyUIlC1hlaKqZUc9F_O2yTiea7y4Njap409IebbZucjkfzwcGZNWBcz3MLvnxmUne4GgJKlEzqiqBq8xHmFXrqW91sRrr_LFmovhEjcL_RfTwI7p6sjemfqMpc8X45fqPOaZJ_Cz3vq8zJbHpdmXcFN5IhrFFpIntZjmS5DUXhGRS3REvzPKaow4IuHqiNiTCIJtiMnqKPIx-0QfZqyrkLccshsTS2zNlYiYt9LfyffDSMRYHapxR1oMVkOTAyS0sIlyeMH7tL0mLMranUL5kD1Mnbm3-4atXWJ5ANDgZJhtwekAbZenhJZUKcAL0Z0Ew8hpTUmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=MnKnMGA5fD0GvKoyUIlC1hlaKqZUc9F_O2yTiea7y4Njap409IebbZucjkfzwcGZNWBcz3MLvnxmUne4GgJKlEzqiqBq8xHmFXrqW91sRrr_LFmovhEjcL_RfTwI7p6sjemfqMpc8X45fqPOaZJ_Cz3vq8zJbHpdmXcFN5IhrFFpIntZjmS5DUXhGRS3REvzPKaow4IuHqiNiTCIJtiMnqKPIx-0QfZqyrkLccshsTS2zNlYiYt9LfyffDSMRYHapxR1oMVkOTAyS0sIlyeMH7tL0mLMranUL5kD1Mnbm3-4atXWJ5ANDgZJhtwekAbZenhJZUKcAL0Z0Ew8hpTUmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=Pj0_1YheXqSZYWkm7VyWdbcBqbYg7BhKsbfDnusDIiJgxL1F1EGU8rt5DVffF_mFiOxxMRwIdYV67nrO1WlL_LfKshvOMQZYNAjlDT7FF8fRU0WORJwWoqow9C5Mc9SA--p-8ZMmp5YaraSOnecBUOyoP_5sTD61CPfA0cRK0idvp4T2TgvhVuEHkU6BIaNNVPTBJVnM-RaUVDY4mSpijhQ4HzRG7jclagqpE-OabNgMfRLrGIUBGawjml3i3mpZOfLPYr0q896tZJx7EDKQvSSEAFf_0EetoiQ7lVKZYaDfO0Yxn4V-exyESeSJbEULiNhlr7PZy1T_TauVL51IQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=Pj0_1YheXqSZYWkm7VyWdbcBqbYg7BhKsbfDnusDIiJgxL1F1EGU8rt5DVffF_mFiOxxMRwIdYV67nrO1WlL_LfKshvOMQZYNAjlDT7FF8fRU0WORJwWoqow9C5Mc9SA--p-8ZMmp5YaraSOnecBUOyoP_5sTD61CPfA0cRK0idvp4T2TgvhVuEHkU6BIaNNVPTBJVnM-RaUVDY4mSpijhQ4HzRG7jclagqpE-OabNgMfRLrGIUBGawjml3i3mpZOfLPYr0q896tZJx7EDKQvSSEAFf_0EetoiQ7lVKZYaDfO0Yxn4V-exyESeSJbEULiNhlr7PZy1T_TauVL51IQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=W_WOHA5LI_SASjhoEXrdK2m9fJcqu18qsEU7_-SXxvkgubm-Fpal6NBGE5_6I0WXefppf9Jpj8xk9zMU03TM0xu_XMI5TvPfAvjmjY8q4NCn3v5diSsI-DOtR3sbWT8oXN1VAMSAZvYtaljP1LHill0mEz1abMVgvvqRbN6C27YphSor5wzboV6sDndlyw3i0a-Y0rePD5hzPImsLFGi22TJPqr6yAwfB4DUEncelmpyWAfwhFpvaGJGtuDkimqBqMY2JRGqTT-Azia0SoMDXBifyoWDUq09EbhPIMB-iwtvEtR0Bk8TpjYMeSQN8yL_X-JD0BIs5GK4yP8iLq2ptQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=W_WOHA5LI_SASjhoEXrdK2m9fJcqu18qsEU7_-SXxvkgubm-Fpal6NBGE5_6I0WXefppf9Jpj8xk9zMU03TM0xu_XMI5TvPfAvjmjY8q4NCn3v5diSsI-DOtR3sbWT8oXN1VAMSAZvYtaljP1LHill0mEz1abMVgvvqRbN6C27YphSor5wzboV6sDndlyw3i0a-Y0rePD5hzPImsLFGi22TJPqr6yAwfB4DUEncelmpyWAfwhFpvaGJGtuDkimqBqMY2JRGqTT-Azia0SoMDXBifyoWDUq09EbhPIMB-iwtvEtR0Bk8TpjYMeSQN8yL_X-JD0BIs5GK4yP8iLq2ptQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=LoUfbs_hwBDi_KovtzlF3tENeLVPjyspAjYu8r83OxkjH9BjB5bn64oXItKcOBpAiclH3fDw7fTWIvCWCFSh4cJAyzxodwNn3S-5Uf2_iY9ZrQH9Pok3VCpwswYRwHUsyYbnCue6nNXCgOpoNfOgOMujCUDI0lb7r47i_JNgwR32hgWw-29b5SE95atJVIkF8fjgVa4Z2oZT0hvuG9DeFx3FTdahaxxYJevZklS-Zk5lIP7oyrjv59xGkWXLQKTG8q7Lovz7lbbepoJIfw5V3_aq8y4vEr6DyI9UX1_7Op8Nw36P75QyW7WVZ9DRxqorUSgXLZd-70EntCpeycKXzQfy015yIDbXDT4-CqktMAr2XRTRKVAS5fx6Vfdk1VnV5BGie6145Hq0PH7-tTUJ79ZFlg3d1OHugaqzPjIfCcW3Q08_yznrZflSgr0KLRCcUOUHTo4eywHsjNFlnbvXAMpHZZlA5s4P5qNZ98RoN7gEAnMaPlRnHDKxBvbVY4pe7NSaWMl4MrWmCRjM9S-YQLKCjQl232KKvL_a-RAT4IuIOShcKxEKbdaH07ab3qRQ_0fbtsQncqNE-YBPD5gFCnOGAXZUq9ifRYMg0gt9eSCkWf-1PDO6JPiilU0YKVsdeINug02ntfdgPIpjBJFLLuK7Xn14nLnBx3hSh8INchs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=LoUfbs_hwBDi_KovtzlF3tENeLVPjyspAjYu8r83OxkjH9BjB5bn64oXItKcOBpAiclH3fDw7fTWIvCWCFSh4cJAyzxodwNn3S-5Uf2_iY9ZrQH9Pok3VCpwswYRwHUsyYbnCue6nNXCgOpoNfOgOMujCUDI0lb7r47i_JNgwR32hgWw-29b5SE95atJVIkF8fjgVa4Z2oZT0hvuG9DeFx3FTdahaxxYJevZklS-Zk5lIP7oyrjv59xGkWXLQKTG8q7Lovz7lbbepoJIfw5V3_aq8y4vEr6DyI9UX1_7Op8Nw36P75QyW7WVZ9DRxqorUSgXLZd-70EntCpeycKXzQfy015yIDbXDT4-CqktMAr2XRTRKVAS5fx6Vfdk1VnV5BGie6145Hq0PH7-tTUJ79ZFlg3d1OHugaqzPjIfCcW3Q08_yznrZflSgr0KLRCcUOUHTo4eywHsjNFlnbvXAMpHZZlA5s4P5qNZ98RoN7gEAnMaPlRnHDKxBvbVY4pe7NSaWMl4MrWmCRjM9S-YQLKCjQl232KKvL_a-RAT4IuIOShcKxEKbdaH07ab3qRQ_0fbtsQncqNE-YBPD5gFCnOGAXZUq9ifRYMg0gt9eSCkWf-1PDO6JPiilU0YKVsdeINug02ntfdgPIpjBJFLLuK7Xn14nLnBx3hSh8INchs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=JE_yrH8eDeKlVUuowPWiohockNk6wg173p1G0gEAlBC3RxPpHZxBsOUSUSUPYpb3g0wHkvGK5iYkeEloP00ZghxtgytSx2fOCJIvrZebIUzzXWXMYU-AjM6Lgd3xkiUXqbWvnxGlkl6JiK50fadYOhhQRYvLuA0torL6DVvD7VjY_hSqITy4YyRxuYas9PDKy8MloW6BigR7o3laC3K9DWUJf0Y1yLUtkPxonRdx9fLwLd12W589-k7yI7S5z9F5B3EmTn8XQXOeN_pb6cru2ToEV_INudoF1LjNO8tKRh0rT455wYQNTR_FSffaTp5BH9XPnMVgoUBrRjM-VkQO1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=JE_yrH8eDeKlVUuowPWiohockNk6wg173p1G0gEAlBC3RxPpHZxBsOUSUSUPYpb3g0wHkvGK5iYkeEloP00ZghxtgytSx2fOCJIvrZebIUzzXWXMYU-AjM6Lgd3xkiUXqbWvnxGlkl6JiK50fadYOhhQRYvLuA0torL6DVvD7VjY_hSqITy4YyRxuYas9PDKy8MloW6BigR7o3laC3K9DWUJf0Y1yLUtkPxonRdx9fLwLd12W589-k7yI7S5z9F5B3EmTn8XQXOeN_pb6cru2ToEV_INudoF1LjNO8tKRh0rT455wYQNTR_FSffaTp5BH9XPnMVgoUBrRjM-VkQO1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=iX68symzzTmcM5HkbogIYP8G3hAngtSX6WZdiVsCl85MqnxqjnO-A73uDbCw3WjKme37C73MCwsnqukWX3DoTbwtNG2FtiICtTGHweyuidaWAlMhj3WA4nrczrx79rbzEeu_MpvjDiv8lWKYSGnb_03nXnMId2IUh_sFNEOryqMvWtowpLBoZ0na0GXZb-7_NA7PjQSvwQT2p68bXUQYgwGIZp0iR98xsPbNQidouS__Fu4VoJ2NNjbgCdv8DHr-EaszxHsBLgPPS_ReidQEgilXnAwNGx1lhPBSF37LEcRc5-aYSqv0EGCDb8lFqeTk20e1TmuUMNvZh81wmPNcFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=iX68symzzTmcM5HkbogIYP8G3hAngtSX6WZdiVsCl85MqnxqjnO-A73uDbCw3WjKme37C73MCwsnqukWX3DoTbwtNG2FtiICtTGHweyuidaWAlMhj3WA4nrczrx79rbzEeu_MpvjDiv8lWKYSGnb_03nXnMId2IUh_sFNEOryqMvWtowpLBoZ0na0GXZb-7_NA7PjQSvwQT2p68bXUQYgwGIZp0iR98xsPbNQidouS__Fu4VoJ2NNjbgCdv8DHr-EaszxHsBLgPPS_ReidQEgilXnAwNGx1lhPBSF37LEcRc5-aYSqv0EGCDb8lFqeTk20e1TmuUMNvZh81wmPNcFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfDn2l0vg3mx3vu7YyG4vkSxUM4PQEGYuZ_P2kq6A-rMjBQKzNZFRfySg59ZsoTh8ME8aig2JbFDIe0-TaOfOGiaeNjvzEB7gWV593IX1xeaFadON9Tde4hG7o8szfThEq7qDYKsrmIxPhN-yNyaTlDlbU33A_5j5dG5cig80Zw0wCKWNn2wMz18bDKJT2ANUg8CGQJ6jw4GbpzT3j0NR1UuY1vPulYLzq-XdeFZjn1Fb3Mt_kdhhXZrSa2S63rYpscROkoea_Sghta8eimfDB5DK2dNEVOH6zqAryDkyTuyzrb5oAvalfGP5-7fMqk0dU0CKpxND_fg4NXa-NcumA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFrqIgle9DjGPgSPg_RqlnEFblWEU7SzQdTxz6oc7mOckNYj8-M5B1O5jVT0ku0Iu05YhD_fVyHxIK8aJwqni5ZGBW3Dvi1hNDgFu8kfXAw3Ke4hyYRTxEIRb8x1cvpfeLQHoDbosOfu_U8JPhIIIA_dUAiqumWO6QWuNjbeDZMO7eVc9UXTbPry2H1BbZa645sJ2usRccCZMwCsnoI4J_yaQjDRVbcEDGJwqv5YMq892_Ec_ZkMv2M_lyRVPDR76b66eUzDoPUotSRU5aiX23iHRQO983gmmOi2TBSdVczhGbnNiGgcXbUlSEBpHk8IAl68NZccflDsKa-ipl9elQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=kop55_B44ZwbGWwS82z1BTOewwqNIX5EFuckQBj75ql-Uhoy8T18KilG3yxcoaM6TMd0Logcr2hQCARU9Dhxv2GI5Gx12QzbSPRwGfUcmMs5IitBhmx7EEOZ306z4KT4u7P561lo6gMEFnyOgpD9W6nCuiPrDlOaeBSah0t621vEWGCQLCbpAbbC3wDfUDIAxKJmTN9-Gh333URTA5ViJiPsstN3_jiKIFDpZy-OLJpzLkaAyMzYtczNZgNLD2bFJKe_3wQ2ZaixJkyj2Rz-hyk8hcED-C85jqwwHFE8i4DAORbacPuhNN6BUf801p8F-76e8FjvnUojYwJDYNf6LpPDYCsCgfqhYE-yZXSIn9Atf3TMhN_GIb-OHayhP_kOAXMERl7b95cvFCbk8WhoikH_oIG8c1SIRBqJ1f9C17PPnIzheo9epUJwCjw3V82L4rnvnxU-G15-00BhKkHe-UA2mZMH0tRj9MnexpUjAaLSnTxWcQEcqwBNqvFQ48X7PWzRK77hmTRk0SvQ_gAJXXkN6dxWZSWmM4jRS85-i-DbkojacS8yz2OLycT0jc2maxs34DmCNO4PIsZY2RnvLvgZIQkRdniFl9e4bC2fhAD1sRTpiVn6rUGagryBXfxDRWpuhzxXF3BE9Q10GG5iLWQpYhk-32MjmzeuHFuNvh4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=kop55_B44ZwbGWwS82z1BTOewwqNIX5EFuckQBj75ql-Uhoy8T18KilG3yxcoaM6TMd0Logcr2hQCARU9Dhxv2GI5Gx12QzbSPRwGfUcmMs5IitBhmx7EEOZ306z4KT4u7P561lo6gMEFnyOgpD9W6nCuiPrDlOaeBSah0t621vEWGCQLCbpAbbC3wDfUDIAxKJmTN9-Gh333URTA5ViJiPsstN3_jiKIFDpZy-OLJpzLkaAyMzYtczNZgNLD2bFJKe_3wQ2ZaixJkyj2Rz-hyk8hcED-C85jqwwHFE8i4DAORbacPuhNN6BUf801p8F-76e8FjvnUojYwJDYNf6LpPDYCsCgfqhYE-yZXSIn9Atf3TMhN_GIb-OHayhP_kOAXMERl7b95cvFCbk8WhoikH_oIG8c1SIRBqJ1f9C17PPnIzheo9epUJwCjw3V82L4rnvnxU-G15-00BhKkHe-UA2mZMH0tRj9MnexpUjAaLSnTxWcQEcqwBNqvFQ48X7PWzRK77hmTRk0SvQ_gAJXXkN6dxWZSWmM4jRS85-i-DbkojacS8yz2OLycT0jc2maxs34DmCNO4PIsZY2RnvLvgZIQkRdniFl9e4bC2fhAD1sRTpiVn6rUGagryBXfxDRWpuhzxXF3BE9Q10GG5iLWQpYhk-32MjmzeuHFuNvh4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4bzsdPQve9w-coAsdht0uSa4-tQ02dE2X3kJr9mo84RTShAUb-5ve3d-W7nxsrDZ4nhT2-iLyvQVAmifLbnTLf8OqtT84UjKEy0CiepdFr2GNVg0sXq18FnI51gQkXlYeVkZgyUrTzljqKqoneHMvmWbzFr98feh6HvlDu6O-wp9zLiDCMa8BIrapKZFujHFCq6ZjhOSEnSIKXl_z1e9TCaQIE1fSRa3cZxDVPw37EekbstcjPIHQaQLwx1BjZ5GMEmRlbXYvXvGAPEqAVaSbV-U4TEkYfxshHHdRNQNNIi3_BhiqWbHg23HQXGasYtYUQHzZJ44l4b0mTlybaLuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhO5cxxB1lcu0gjM82Ld2GUhNrEPm09_N9SGTMJIgxHHytItvYpqjd1aFT2_Ot3dp0cmVw_CLEp4uRxgbbXTfSV_We3NXG0ZSdiwKRfxQZl5ebL4Gv9knP3UXpeAY3Di4Ly34gsOstog2Fet4_hH0KF_0C4zfP4yE60NMPD0IgNSFS9FvHW7F1E4VrAu05DhcG4ChD_6zb7za8W2uMxYvEAFnR7PuAQ7GUxSXHdw6e1Lrzsyk7dpl72TU84Q1sXpNV7ApULFfg4aVHGeYo5mmwYASp9MGZnctRSPIQQ80NAX47RD2FeZlFLoQShJMWfDds8lhXILxdjCnokXMFMXSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlJ7iXYMMCU5UutqEDWj0xJZCgvnyxC85Aq1gP_b-Xo7oTRBLRzX1o75ZNC4AKndrtHQ6sddVjuaHwblYF673asQ8kGXU46L5wlRURI25-O586PgMaZI5YnvOfXl-gmFxL_phpM_NhDiAgWkCjsbGXU38cl7PhwMEP0wAHuxo4US9qPawY4TaCRHMy97zlBadKP4A80etGjENiZ2Eyzbjdeo9ZhEnQ4vUVVSFqrFPK68-EOtw50AMTO7zvJ-N8_fdAj_uKyEtXUZZ4MMLBBC9C2EqaHUMrhtZbBrH1FkvWYkLfHAwQynmeidfCWRgoXPn5ym6Ez5JdUGSmpUCQK9Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyZUPH8LWa688JPVnD1MFoY_3lsOE8rqn3ytq-fZwkvEoxsP45aJvWycS_cuWm-Ldd9E0qjumuAyoXl9i4APTQdfXmpVkeYyl8IEyruItVX6R18vGW98uZ17tEsXbD_odZ7y2Vln7LFl8w-vMEPoDTj3-bsM9C4vCOwwOf85D0tOkrdi0YfqQmjzRLxCbLW0Lq6_J2UD-6EO3YqgnZmyk8lRmTfgqBffRU7BX_EJevsv1OwSeh8By2WcrB--cf0Px902j_XVOuriQIfwWMXXPEZU4hrjac5fhocpERZoPQKCQHg7Vq3brrroKnXkKFBhaCLlpaXOvgXaqtr1e7BrvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=A5L89eJFlJJOhSmI56W9oX3VBO5Hc8wYtjW5vgq6upZ7funM90w2IN3XaxFtYhSk1zKCXIi_I64-1dFxWTPN-41q3r_Lx5pEaiDMOetIiuijRyntgLEW7dhT6do6bQm8va5BfV_GP59hB8y0q4ZJB1Y5-4mgsDmLXIytuVVGac4kH8cPWMhirq6XOafiSOR2Rz4JHwVSH1Ti0EVxlO7PegMXLh6MU4AhZ3APXbeMz4kPCQULBJNIrKmEx5YvrnxAZ3UbV141qckKHfxlTw-D8Ben8IsyJw-5MV988dcdbp-fyktGxJjIyAgt1L-ATj8wdEddYAzcgYbcFi9gjLr9Op18-XxzddAa2hXvO_sFqWGpWW1lnO94nIgd1Au7oYxekAekUQuPoO3w4Luz550IvAthh16GqeIf8vePX24fGPxDf7YQ1i5zzKXQkQ-MAE6cJALIJagi731rniMYIlUqWrjsaCLeT0DkTc6SdzPk3-Lce_YyWFx80w20IFMqapd8wIdxqJQ6SLXNt6lb1BkD5GHX9V02HcqKOR799vRvOSCm4K_S2PNaHTQdNdw2xO5CIPQYzTWme8dwu8UaK8NjtGKg26tVcHtkr1s0PtSsheEAnj8xjU1HPEaJb4syLB6E0R5P6iwu1UgxNjSeupDvQBW_Mp3FpFG8Xlcymnp4-0M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=A5L89eJFlJJOhSmI56W9oX3VBO5Hc8wYtjW5vgq6upZ7funM90w2IN3XaxFtYhSk1zKCXIi_I64-1dFxWTPN-41q3r_Lx5pEaiDMOetIiuijRyntgLEW7dhT6do6bQm8va5BfV_GP59hB8y0q4ZJB1Y5-4mgsDmLXIytuVVGac4kH8cPWMhirq6XOafiSOR2Rz4JHwVSH1Ti0EVxlO7PegMXLh6MU4AhZ3APXbeMz4kPCQULBJNIrKmEx5YvrnxAZ3UbV141qckKHfxlTw-D8Ben8IsyJw-5MV988dcdbp-fyktGxJjIyAgt1L-ATj8wdEddYAzcgYbcFi9gjLr9Op18-XxzddAa2hXvO_sFqWGpWW1lnO94nIgd1Au7oYxekAekUQuPoO3w4Luz550IvAthh16GqeIf8vePX24fGPxDf7YQ1i5zzKXQkQ-MAE6cJALIJagi731rniMYIlUqWrjsaCLeT0DkTc6SdzPk3-Lce_YyWFx80w20IFMqapd8wIdxqJQ6SLXNt6lb1BkD5GHX9V02HcqKOR799vRvOSCm4K_S2PNaHTQdNdw2xO5CIPQYzTWme8dwu8UaK8NjtGKg26tVcHtkr1s0PtSsheEAnj8xjU1HPEaJb4syLB6E0R5P6iwu1UgxNjSeupDvQBW_Mp3FpFG8Xlcymnp4-0M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=qq8e55uAxvjfZN1f4trQgle9fV7xtHRDQ9VgJCWD1KzyfxhtUnlDQUo7rr7uqnJLkvCM_-UGMsvdN4KEkmpXnmuc_vnAYHa6hXeruWORnrAVCCXMuJVD5NaGZ_SQyxXN9SFM_XrTqkL3HDXWRPj8Suk8hbgnHxGL_eWAXr6Gh5APt9gCm6CYCkUMHUcVKjHlGdCPIoxwZKpHLuzgyk3YoczGG6C5-MPBw7RIOjaAAjOdXKo8wYBxfmx4Y6aVNDmKBZPPBpg51xStGJQQD8DxoHup9jNF4ZVuUDNDhXdZldrRXz6D60L_MazC9P7CWHwaIGfLgJ205hoIG8cd9qiEEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=qq8e55uAxvjfZN1f4trQgle9fV7xtHRDQ9VgJCWD1KzyfxhtUnlDQUo7rr7uqnJLkvCM_-UGMsvdN4KEkmpXnmuc_vnAYHa6hXeruWORnrAVCCXMuJVD5NaGZ_SQyxXN9SFM_XrTqkL3HDXWRPj8Suk8hbgnHxGL_eWAXr6Gh5APt9gCm6CYCkUMHUcVKjHlGdCPIoxwZKpHLuzgyk3YoczGG6C5-MPBw7RIOjaAAjOdXKo8wYBxfmx4Y6aVNDmKBZPPBpg51xStGJQQD8DxoHup9jNF4ZVuUDNDhXdZldrRXz6D60L_MazC9P7CWHwaIGfLgJ205hoIG8cd9qiEEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVObcPRMEl7Q70rWyR46Ek8uskl_qTklf12xGVkqjKV609v6GHxwNNaILDvGSq2UaF822peGjzLH5Mt950nmRdFjOgkuNylIMAXBzLl9AOgSEL_3ehbSBdirSsFgfpmNFbtuQvxiX1XoyAkLe6CZcyly_DW3V1czsifPsnVcUJ_EC9TyDxmv39pi0pQ43VE0mzkmkTTADBWYhnAXoUSgjnIOHtpwmqiSlsvbw3eEmoogdtqI6WTEce2OI_LXVhbFt2DrsyslTcmJkOmYwMO60lrnVkBSB6AkKtWC_eZmsIAh0WxDLwItWixnK-GOO_-VbYsc1qu9CIgQdpGRyXByWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toP1H4kODtblf3lAhLVDT0_gWMEMVjTawGlrR6DkKSVpwjkoc4dB_w-4_ERVQmnriJOXML7Zj6jbyvj4d42UPDXLL96eF0jNBIct_ObLbJAdmx6BtGpYV1gVNOVqwftyf22UXS8YuOproRwoDMDXC7gqCog1pf858bridbL019I93HOSvHlhCkb3mVRUbeqsq40PMfhprRVSRGlYZPxTy7VCRZPKiYl0A2BwGbGdrAx85X9gN-wKxE7-quKH85BQKmtxPM7j1TfS4QcRfl6xbFKVCkopYENY50Fsb9gJaFVFjAex7HDKVR_Wra99cHBoImbVlgnD7CLMxoxPwv1G0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
