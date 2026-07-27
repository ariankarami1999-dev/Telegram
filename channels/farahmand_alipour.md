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
<img src="https://cdn4.telesco.pe/file/sL_NSTxe-nqPzoH7vLM9GBFP3DNwJI7KoGl4yCTNWeXLwJdku6FM4oq6C4mFUT44g5zwpcBXVzytTBBE3M6kwjgAjVETGfuHgoRnlul14PjYw2gaVtO0NlIGtsIlUIt1_P0DYnnczzRJSU3SXbQQauYil9hfHRqyVrdwwuIj2P4ynnqPRLwz7tjuZZSTJKC0Vn8zh6LEH84r0r-3jCnLmNzSwa6E6ig1yOOn8q6zFq7x6spK_N0kq5AsEojU00o8MKkSmPFKhoGL1nLH7ax4QNdODgkag31qoqVqwdGpKEMNsvkFJ5sw0rYwlXOuNiiPg1-4IvEauzO0YvjBZIMJeQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 65K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 08:33:32</div>
<hr>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edDV9CjvDEqt0FpOCHD_yBMDypzmgXqWDY6dm2flpjbY66GvUL4sQSAyT3XYf8jk0beJZo-zX0dyZV818M6lxpZaAVMpjaK5cSjIzTimwOMvAl6FjMhBVPDCsROKEw4lITOYG6pfAxO-n5f4IP9JkXRt3yE_UrRjUqWMRc9EgERWhoKikDsN7ErGvFJqz2EQQvYoGHtiEYo7Ffpbe6NwDDk-8Cux1Fp9OkuJtYCF8iFDqdPRjgtwoc4CgP3fc_7_16dFtsZ-Wpv8SPuEntbB2OnohSG3WS67R6Xlz6QKF74CxWkraJ9hCNDHxQE4xM9BgfVQ9H1Mf5VfHnURQI69lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEgMOSHveFO1xJ4gaGdBP0WhAis7h53aEUtzooS6oZsV5BWmFapNHX5_q8raGiGFQgCNJ-t21nnuYkojlkvIDFL6fbCtNWF_oWtlr5BPhsrEamfepi-_ROQHb-BF0QdOAZKhyWnFUaLVnFIQVL54n1MFatBqWE7VosQ7LbnX7VORu9NAfcvu41FJ0YpuFsCoWRYo72zV4QkE5qgrPA57lUV_D8RmwNMmlfBocJMYeeCunRHitTslXVOLltk_7xu8jkVUepKElX3CuCnHev6ZKqdC6Hcm71Hq1jOaCqr1kSYtb52zbkcqXabLKsRR5NwJcrRgXSfxuZEYAJ1da8Hhqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVHNyHPeagSnxkwEfmIrKKeiocZOMLHac-Ampa5iYk4oKWnbnUQ5mmDpj43K9ZZi4ScMe-SFPpbMZp1b374940tv8hyRarAZClhCYlCNkGyTcpRQds0j95atYiMfifXFOZGGgkLPwwPfCRVRR0k1WTNcrkBJMJgZ6qvZk6wpv8qiVbtOlxQqaTASMiclI7q0gZK8jMWIL2hhoGbNqhuD_Jfle6Y9VBm_9GALlygBHfOXYwj9mjO04vM28hgbpjJbAiRy3v1y4AFppInFPv60GbmuRu8QnFNqagehXpjfvLfF9y6oQ41jn-rk4p8tS8jLs4_knXKQ7Fkm41mt_U8Nxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vU03JBBIUrINr83zJT82G-VOKqE8hOi6VDow9Vk_JrqmtdlDqAZ4VWG2z6kPYKYWnTvcu1ghQYhN8YxdE3WNEs-puYUx85kYY4Gj7TJ1HIHBl-Z1qC3StQRjFiHbT7CppiHHAE4v1oZPOpZUMXOfdcUN1h9ilzqqgRBd5aJhbmIOAabbejFL_KnA94YSUmqaZULOPgbThc7gMMVMBuJCRXVs-BoDbGEmpCSNmoXpnK2UBLLuvWLwEo0C_AmejZoVeeOOmnT1FrgCm600e-Zya7Q1SPA1SiH57ooZqksGRi7Mt7Z4_If_Z6p7vDT3ipcJFoN3pXnyeMra1mG0EJK7KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6uXN6AIS_5MoIUxC8Y7ktV9p3gNfFu3TR5dpzWtVtsp3ak8GY93NMY5gwTvkLt2EP0AgE26uNAI_5mZ3VS4yzWja7DE6sXcoE56ogTN57GbmcmCRrA99--Vl-uze9Smv4aNX1gBfVF6WnA2ku1E9ydTd69jXDbsfeB_G2edKTeEithmOACjtkYiRBGD__x46cvX0KjphzHYInXTjdn8nNCCb30QIS1IOCAXqrqHtx1rzduST8WOJdn3jn7vio-1fxqGa-uTmg-MMfU57p15zqKAnsO24gUa4ZDerk2oI7emoQCiqoFEElxZX4AGfdV1oK3aX-dd4PJd0FfIrBrWXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4W8C02ySscLJP7zUlcpOPFg51itb0CAPC88AR8e0Kd8VcLR7rZUm5IR4l6E3LnSMTn8o4unwp3MTKjhcZuEaDxoRHoCy9Cm6p-GoCcb2qV7cRaCcifKfQagVRLWozSKzl1oereigannpz18xeruLSpelSQ66x8Z83oZEvQmMV2_LZPclEbuZ9iXby2tBzoTCUeoeUKk4SkL5mb5osAgvP2eaGWOpDkV2hflyRAwPmLBRVmQllhFn508w_b2rCcFxoIJ7_kjBTZVdPbUTzN5QZkeFkbpoumH30PauZDn26oqgZfHFZnf7jJdRcEE_8Lby0umJSq8Y7nFtPJEvfF1-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VY7g2gz8Oq_5MTvtcAnZVmmh2oFIu4QDBROeywqvu9qAzKtxRJlcLKmC-p_fmftgV0VFqSQ1LrNKWQ1_y0mAETHzGaA7d9AnpqV_UI7jk0iQ4xh1_Tss7j4DlxFeHVGZPtfZZPUP_kS-HpvnVA5J0d4244kbMi-IuqUB0MCRJaKhiX5JxbKcGOQeImZ2WYzajoZr6tSC2rem8gfyQFksCS4qlF6Le8a_u8CEQRm28aIfJn8iU1Y_AfUpVpw7ULO8Q4NTpEBZZNjSRz1S6_4R2Lyxrihtbb0AS7sgdkyOIZntOYswcIgh88axcL6wI7AjkZeTKwSvBqiFbxqgxGCI4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMm_ESU-hX2-8muoQSdzXE_BM4NLEtcn5J7l0m8TdQcx2vkrotM2d1UQIKqF4jF0jExUa07Mh7uCHsUifRB_4a-jgzjPkW8lhcjRTf0yW93aZ2CS0u1DWAfniKXkWiNMIcx_wy3qONuzKNkNeDlimLYsq62QWADVyNtcFqwW5C2SRZOt-O5aZ0FsKNcP-n54YlavS9Sm-sH_xh1G8BxWiVWCZYquEPGjIT99eFkH9Hock734ZczLuRLgWBOPtQ6hRnkZtMgY5EuNecQRI0NpBMzBaRIOrljn6VqsaOvdDmQKpF47Zw8nXGllxmdADVzB9WBvfEUGZPxehtHw0yDfwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFPCHHqOA0FLfWFsNB2N51-dg8qUSGOlhsuoKp-5jQY-a9rgjxhh4bmBTxEd0O-KcE54kMUfOM0qU2JbgRqvFVkyy3F6Mn_h9XAC9VpzM2E-F6l0BYacv1QEE6KEaoJpsu3DZNCS8IKyV-utDLOZm1_XzQBwNOJHA8UzfBau6jkGfS1FosL_ZBJo9yETdN2ah_QvG3EJ8Jnp_z_FEipKp0aytyEL3BPNcMrpwqE95X1QjO07Gsxx8YJvG3RMlfNfe2EiMToxLXb5LIxaPKjEzxuFkeyuo89ztm8xQQkMxz2uoPvJRlnaejaWP7c51-TOtbFUcwn13jUiWHibNbzd8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dX3lDIW16FPJU83Bvv6zVFbO60tZuK8KZaF_YU8dZoY8u4qcH7c4dYwBQNZSsPhVROh2wiYYVjRLadhmNHldxBxlrr7yreJjekGwMXuCVJjnqa9tl04Se1F_4ModpzvzBOnfzu--w5nwF8C2sTadYMY7F953ndytL3HI6ZuAIkkDFWv3aFc1CxZvYzDWwKHiAemJfnQpV8JWA5Xkb-ILjPlxlQssQXnxoCwOGi483GGPHBoolDZnfNSmosJuMAqhRebNU20_ZEJR6lKZPmihvkUUdkMEYo4ZmIKDyyrM2UL_bo2V6PtviVgJw0qk_jG-v4S9bV0OJAHE_CkcLyQIvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-WXS37cqCHtvZrRKpaDDqWfp3wjNVD3FPfWa7Nx1HT6G4BHB8Pj_zTJ4jEt8v2aCYJVzIiOKk6S0lVP21txMnSHittMKp5CTiVb_oDGCCUUvw7jmx7aiYlboTYyghV65Rz6XUJQQcUhtFyjNHJlaEdCZO2NXUa7zyQw2J52DdbE5CN1zstXqBAVgUuuK2Ws_ndQoAJ0lch4Z1AwRvEsJrlfcvmGaZyD2o-kNCVEaJ8ft5ekejjhYcKTp2afeykxNhw5mJ3OpY9jFMlWpF1EAG_8CwfXs0BQLQ23ZOymuCQlh58iIZKTgusrA13jltDkvvSEiRnVrgGLjC7WaiPZNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hobp94WGyL0TjPiP80MviUJ29b_zN3UtWwCw_ocj7-ea36OaDkHKXNdbeYDMI7YBucQgckLbpwYiqrfV2ookAN4oQuHpSrCtokuzst6LcP4bxUcpVIrI7qg0Q0DM3z4HUaRB2Jhcsdc4ZPZQ_N3d0rToZDorWqO9oTN6bLwcB5g5x92JYnLo03ZsVL6_NK_8Mva7NZ11cMB7z4dDDB7-ywKU_hvbA7dBAHGPQOpJBZt725EFWmdFeetHhBsx0-WsKDQnTlqLUi__PhUtSTIcJt1v4vrCLTeOVyqsDBXB2uzoH1XyKjPwklfKfjTcv6AeYjdoSuVgdKnbZfNsCsLLAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ln1C_e-Jhz3xpsttJEGoZHfYAzAgk7M-qwAbsWJmNLRYSOzQyA0YRHQB_4pUI-GMrkIUoPYTqopBGl285JWJcbNpKH7Yvgz-Joo8jCW0hTmzMqkF8OzLavbs8n1xHJneacCuE5wS-U1ltizmM4woOv7F4UeRvXvfGIeH9NumHVWrqei3H7eZFqAdNCXZ9Wr8HOdPEN4wno3RSFC6wcglwoVITwfcOa76tdIKJdvAlx8PYsYjO-9hWz6YYTjIRZBZD9etsfONJsc2UWxxgxNrAJlOINaNHjXXZwQFzVsWF6SVcPVsNHk9SKxW47xxFPiwtO5rm5ynrS5ffH0N_tV9hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXdn4TJWpTV_y8d7_eAuR2QiWEtBRJJM0YWfFeD3EbCH2lRhUhGH23DAjTmQ08TWRX7bdeXwGWS8R7t_GPnwA_EUeXucFNro0W_HwkSWezES3LmQpFvCAyOYXt73Qo5JYVceYVE3r0KuqyIR27ohW_KP4H4FxTmntpPaWareNcGRUhc_ojUTk5ZI-DfT-fXygGZCeFfYT1pVWFhwQWnNRiiPAnQM23cr4XCbtQQ19SwjvzuNNOwOM1jewLV_scAe1n6UrW79diuApa3awYl2DNZZeDOPffcEJ-mGvzvDT06gd4pBukVRjnLxJ13hV4rglriktPDlDt6cey-cyGkeFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=teK51g5JX2zsd1uTPpyr1owPH4-RZs2_NLVQvPD4UTUsNzuR5ckN1Kn4aGlTEFQ9WcpbCMIK3eFB8IQqbhQzgwItWhBieimKrXdmTBzkzIDmuCrL85fslzS2khg4RRMrVp4lAhOGcm8OFKJ4Y20DynOKnGzMi3RRPYwABzFy7q7yS7qa3XDwV1YSZ1nJiLiSbFLIBQUaA35speUBTsn7mG5m_8TUuxP-gNXQoEWNW5C2VF2W9d8vF3ymlzzHG72IAUii8bQk0HAhib1_uKULqpiRojXaez7DlPSe8L0Uz2Dm_hpkuvT4HNswV3EJmt6L47HeIm6Oh6nRQVglY98BJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=teK51g5JX2zsd1uTPpyr1owPH4-RZs2_NLVQvPD4UTUsNzuR5ckN1Kn4aGlTEFQ9WcpbCMIK3eFB8IQqbhQzgwItWhBieimKrXdmTBzkzIDmuCrL85fslzS2khg4RRMrVp4lAhOGcm8OFKJ4Y20DynOKnGzMi3RRPYwABzFy7q7yS7qa3XDwV1YSZ1nJiLiSbFLIBQUaA35speUBTsn7mG5m_8TUuxP-gNXQoEWNW5C2VF2W9d8vF3ymlzzHG72IAUii8bQk0HAhib1_uKULqpiRojXaez7DlPSe8L0Uz2Dm_hpkuvT4HNswV3EJmt6L47HeIm6Oh6nRQVglY98BJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدال لفظی دو نماینده مجلس
بر سر تنگه هرمز
(پشت پرده دعوا : شهریاری اینجا داره میگه
که تنگه مال ما نبوده  که بگیم میخوایم بدیم بره،
و میگه تحت یکسری قوانین
بین‌المللی است و زمان جنگ می‌تونیم ببندیم برای فشار آوردن و….. ولی مال ما نبوده)</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCfNJ3W44BiTNwI_i_CzhsWcdedfZVckRIHjA9UiYzlyJmOaF55qnfNxci-ui-4nuv8ZIw7RhSfWVc61EW053zDgvSMX3p8Z_BqMqnzGoOrqNorfHAcxlev3pDq7YK7Z_q0HuXmgDxSMIFa3Lef41GR0rbIOMe5-V7VbC9o1rxorq2rq9ZMQaSkgk8aj4UFoaZ_7_sP6aO0LBB4mwCSxpPVVNJ6v2t0pUY1NL5OiSGSexy2S-or_eDK8OEfR2CGoNBlIUl-rZwnzf5io2o8fVeUOSAilpf5zMzmZx5UCJBf6ES2JOPo627u70-p-JL0FFts7sxkvWwGs1COxIVw4eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSdi2iAiJyj-cK5mPaZNKCNgA4nvWkjJVfDHR6qNJAXk3gQiW3JvnFZup0pS07Dmv2KY8R6ICICSoFWnQfy8P1bVBQ9QjY7_664-gW6vwCBlX-jSQ2NqVOXm8jKabTVUJt2GcJ3NTorvHrGg7nGjkCMSb6HhaBTnWC_i8LlZiOWIcQoksz9vbe5ZzcmRik792HcpSUQUHaBjug6bSzmaZUauiS-2dCx1S1N4zd2JAQBb9uhqChdOOcG9oC6okaa8Vbkv83kNaPx9KaaNwLzWoIGbdO4MOx7ZZEu23SwLYBF-ESTngIWmkWIbufe49bn7LAckzcC-96q-UXiF8vBtLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=MsYDK0tG_4npOhK8VesQuDK_cl-EYsHgBhDIuS26hyX9zi8orbbsnC6F7vrAXI0AhxIZ7HaNLUTQ3pKz-cBa3G_sM38rWvrTC6TigUA3GPnO5nMh6vLFllONKM2r4ySJhBTkeh8_UVUTSigtj-k8pBSikuYFcLX_TjkwTc8ChdnBZqlUNWL_fjnzyz793Qyn54XQNO1rlCYy0_tTUQ8n_49R56jM_gmYaAnl-1Iy7_Kbfe66IO_dkQZjLGbXreB6b787YVPZ2ZnCM3F0f73eL81flRBHjtdSFwUBexmavjSMOCGH2lOJtIOlDdru4OS5bKq1ZMLIL6ZrBgc_PDNGWTSYHcYFFMS2LfVqrPa82c5Z-Ha2Xby3uD9JkUaE0C6eV5Ea4H_0qkkr5dYDedxoqsuWtgbfPrikh5xux0nXPqFg7D59IIwXJLXgCm0Vkdxfq30gni0bTRtPbijFndlbN67WCmzt7D3cez7bgXekgAlPi0SwgKESc6BMALvQ0B888mbEDiIixyapQUsK07iBTx2fig79cmn7F327-21IytSlvjv2TNmUT-8gdKcxHGgEHGbWwnR4DV_Ax9vuh0DtPfe8tSURxRh77gjqPwBcwvM0i-L4bYdBUuKemPjHirFJt3U4ljWNo6nI4dVwp8eMF3N4c-Ipa1Mzi2c8E47fwQY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=MsYDK0tG_4npOhK8VesQuDK_cl-EYsHgBhDIuS26hyX9zi8orbbsnC6F7vrAXI0AhxIZ7HaNLUTQ3pKz-cBa3G_sM38rWvrTC6TigUA3GPnO5nMh6vLFllONKM2r4ySJhBTkeh8_UVUTSigtj-k8pBSikuYFcLX_TjkwTc8ChdnBZqlUNWL_fjnzyz793Qyn54XQNO1rlCYy0_tTUQ8n_49R56jM_gmYaAnl-1Iy7_Kbfe66IO_dkQZjLGbXreB6b787YVPZ2ZnCM3F0f73eL81flRBHjtdSFwUBexmavjSMOCGH2lOJtIOlDdru4OS5bKq1ZMLIL6ZrBgc_PDNGWTSYHcYFFMS2LfVqrPa82c5Z-Ha2Xby3uD9JkUaE0C6eV5Ea4H_0qkkr5dYDedxoqsuWtgbfPrikh5xux0nXPqFg7D59IIwXJLXgCm0Vkdxfq30gni0bTRtPbijFndlbN67WCmzt7D3cez7bgXekgAlPi0SwgKESc6BMALvQ0B888mbEDiIixyapQUsK07iBTx2fig79cmn7F327-21IytSlvjv2TNmUT-8gdKcxHGgEHGbWwnR4DV_Ax9vuh0DtPfe8tSURxRh77gjqPwBcwvM0i-L4bYdBUuKemPjHirFJt3U4ljWNo6nI4dVwp8eMF3N4c-Ipa1Mzi2c8E47fwQY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=sL3kQ8if1w_nzbmFI2GohGmsxUQ4ri4EgaS5MEAzCd5cm4hr5Xf5kaqDUGSsjylz8e3TUctBRFp3DoYJtC9uBho3YtDBwCKZeS_VfuWEc1tKXAPIm5m0NomWwxC90u9XoN5DqzQ4mo0A8sZLmDMiHjTQFoagb7NSyjFUogjdgDR7piBDPAiqr8w8EemPv1peX8UQTurK2R5Dn9H9nFw7qbJjFOXLaC5jlRxsn47Lif3lFVnxyGt5nnp-IkWS2qPNQ2pWkQggFUhuqwBNabpGAIqzV9pkH77YBU3p64Ts4Vsl6qMD6ZLRAHmp5PyWdGXKx-mWBPX8yi6JQ9db4rABEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=sL3kQ8if1w_nzbmFI2GohGmsxUQ4ri4EgaS5MEAzCd5cm4hr5Xf5kaqDUGSsjylz8e3TUctBRFp3DoYJtC9uBho3YtDBwCKZeS_VfuWEc1tKXAPIm5m0NomWwxC90u9XoN5DqzQ4mo0A8sZLmDMiHjTQFoagb7NSyjFUogjdgDR7piBDPAiqr8w8EemPv1peX8UQTurK2R5Dn9H9nFw7qbJjFOXLaC5jlRxsn47Lif3lFVnxyGt5nnp-IkWS2qPNQ2pWkQggFUhuqwBNabpGAIqzV9pkH77YBU3p64Ts4Vsl6qMD6ZLRAHmp5PyWdGXKx-mWBPX8yi6JQ9db4rABEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KChVNp7lx5UZ5Q-pD0tknNPhCwj9TAyqLr-4zaoZ3CP8P4a7aUM-4VaFi9ovmvraEbUmzGTQzd_2lEuckQT2bnob1edBayBPtg3ki76jlRTZ90zitIqJVtsRi5CryktUgEce4BspylrDKwFcuEQCqq6hqx66FMD7i-1xA3ZYw8PsfjfuQH413vXoqHxP49AWY0bprdWzoBUMY2oZ0Z_1PgCh9ypQXng0RGWuQJ9DSDYMoGw638yOd2BrKTElhQumm9c10O58MwN-8_SaBy5cnMn1l5f4Ib0isREcjMGgetK2QXvHKSvmhgHYvQM7V4tywwJujPGC3hvhgYGbu9RTZqQ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KChVNp7lx5UZ5Q-pD0tknNPhCwj9TAyqLr-4zaoZ3CP8P4a7aUM-4VaFi9ovmvraEbUmzGTQzd_2lEuckQT2bnob1edBayBPtg3ki76jlRTZ90zitIqJVtsRi5CryktUgEce4BspylrDKwFcuEQCqq6hqx66FMD7i-1xA3ZYw8PsfjfuQH413vXoqHxP49AWY0bprdWzoBUMY2oZ0Z_1PgCh9ypQXng0RGWuQJ9DSDYMoGw638yOd2BrKTElhQumm9c10O58MwN-8_SaBy5cnMn1l5f4Ib0isREcjMGgetK2QXvHKSvmhgHYvQM7V4tywwJujPGC3hvhgYGbu9RTZqQ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfxW1WMc1kHRgiNTrABM8ixFw18ZT28chgAcDVGYXK1vS61Q2HM3MmZ6RkQ6fHnGwtpTxtlSYmRje0uc8vERx3kfdztN7dXOpXAk3UknhJuwvYqTFXZbTxZsOLVy6q11fwasVpDEKs8XkQCZEy1nYjsgvurliXkJmtdmal3mb2iR7fTZiLPsYYh29sFnJ54iUCadL1aP0RD1dcz8BfCE2RGyjeflyWkjIvRWPMgfa_1aNnr3yr0D5mat-kScPET-RNJ59dAdmGB4yfGoJN3_z2xrtNHbg6IBmm8RbJP5FHFVBuJge1xBGhO7vgOZttSLGDoXrkqnLyNEW4DUQLP_cQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9dcS8Zy9wc-KeE8cEvA7_66m3X43uNMc3jLT6heAgN2RjCbGrh4RNAmgJB3P5UPw1gceaYOoMb6AyB3BvM5KqJDCfdIYQ0KRDrZ9bD78KyZQAOd3G3IeUU_zPUL-BNQQB2KSHSUldpTfHkt42WP6-VMEEkFVPr2RkLwBV4bswBOq9yD-kLV89PdktssX4HU_yxoGvc2syHAR9eeUIi3uQyUH64F65af2UW4aB_Khj8Ll3sLwkpqb-aK8b17D9b2MzMjQaCRVH7h7OqmjJfpNYRs-DqiJPvJQSVPX-vYQTMnZFu9tC5gP3RyoKKByBMWoE09ypGjnujblD5g7JFyFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTg1aI128P1GsvgIGj3meEMY18To9HN2WvMb64gCagxyv8ItOaWaiDgW8x2sP1VFTCFgm0D5CGHnWYAiuwAIevgRjNLZzzHFn59KxH-Lad6CUdFnXWaWZsYYZB8dwJoVriSIjhUgB2_vAgML7yx4tCTXQ-6ymhGFjMYaA-Lep3ft0mYNIyxM7E28t-7ZSz2Mji_6SXXhKyOcHmp_ACOqbdSDwefc1T7hBsvp840p2uAX4wvnJmg86kduk-M_m3m5_Nda89nzOn2NFHtyLgb1OVdVhAEIJIKXhOXwmQ5nP0AHmiCn2x4On-5qvYlA2JbymU62FUMeSfFVXXFGBtoahg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=RnKFThYYBwz7Ku62HxJrpG0HdeiQkEIflEqRf038HG3xGliM0P-D1H7_qIbMj9iNU3ZGQsj-Xve4SBQBmdouLUD1qwAQ4s1PVxuM8BYFqvYeYdTnN_Bmu6mlX2R02xASt2R8hru-sU3yJSacC6uoxux6B8mq3KAY3r2OFQgZz68MehW4Mh3LHSH52WZ6BTPHWrIdXzqA1iYhfSM4EQw17bLI-zJkuHmOcvfEBPQXAyRV5LVQrRcmsLCxwg8LghhC8dpJaKghvAyqSsfWlnJYK40_3lCU1zgQ4uxkhv-U_U0Ps_xv4Zh7h8aGc_7Lg54roZfLUSzmXJ8DudwvO2hPTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=RnKFThYYBwz7Ku62HxJrpG0HdeiQkEIflEqRf038HG3xGliM0P-D1H7_qIbMj9iNU3ZGQsj-Xve4SBQBmdouLUD1qwAQ4s1PVxuM8BYFqvYeYdTnN_Bmu6mlX2R02xASt2R8hru-sU3yJSacC6uoxux6B8mq3KAY3r2OFQgZz68MehW4Mh3LHSH52WZ6BTPHWrIdXzqA1iYhfSM4EQw17bLI-zJkuHmOcvfEBPQXAyRV5LVQrRcmsLCxwg8LghhC8dpJaKghvAyqSsfWlnJYK40_3lCU1zgQ4uxkhv-U_U0Ps_xv4Zh7h8aGc_7Lg54roZfLUSzmXJ8DudwvO2hPTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLT0zMENOGkPwvk8ozSzUBE942CN80wQZ60qQmKvhCNzrSjWSggbFhuxviMSlkJ6qL_zz6wMNaTZYNwva4HoBGq6QEerye0PKwINiFsOL5kwacKhfQTBe6QfVDRERyl7G1aGiEUs_5OQ6prPZxEELsG_7XlnzQadnmpvSc4h5Llcxfv-eTzJQp-ONbCDQ3KrOcQv0Orf_9-6WaAvpxw-ct6ckoeIepTTE8U6zRbZDFPmhBuYhBrFX4yjvOz8KxcDPx80uUazMKtJfgFbPUjlqwMLmf3PBumwGz6AFbgzPHIdrgePRR2KJ2mE50u-UAdulqtlZ2q14Gej70Nmf_WwIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LFoCmR7TUY40gfufaywpkRTwbqP5GLDblbB38YR7Vjb82ozOjljgE5QEXwQQm2BKzqJrpqhoO-mUJGieej0tM5qs-CXb3D3gtodoP5bL9Vd-Ikv35A8kgigeWf4F8SDPqN5vKUjQvI7-F1dxXsfdgYR-hzoC8S4c4LPOrhMRBKALKqizkyjyrAUAbC20mPWn2T7kN2jtYbET7pTXXLBUZhpGMTipbh4UWNL_91CpGzkNrqNVpBFkiPa5PajG2RrC3-UQZsbmutOkCqjV2jDKmT68yulHM7ihLdRFebCMH_0qpD8MlDhCFU3jdCQhhkm6aZe5t53gXrUOF9wOTIveoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cx2jSOabKLTMsxDM5rvqhKlzQaysx8KArmDyIfbY9HbETAFyQe36DbjBFhAFk5lgwE_Rl-yPsBb2fYlh27O4T17FlcsRrFbYrBmFe1QiIOzGyQzOyUY5qFS5gsL8ULsvE5JNHDpwRPYZHNM4BRtpVYAhqK3C2K3m5m4TjLXNFFt5m6ITEET19EtHDYq-iBkFws0SdRnt4W2kHNkYSFD9Xt-Xsa_52Vjg2tAik1jWB2vLrqtSWbVXf1lPWyDy8-PNLcy8FKSWnOvyMLbalrGpOorQXwHrQjd0AsFQh9X3MgS6EEKLUz85j2CVZ9MskX8P4AAyLUDo6_nT9pr6Cd52Kw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyBvka9Zyz-3WYtwZh9bFmAPSJMaNdvhcXvoYD_2Pg22oiQ7v9an0cMElT3w04XNcFAtQoR3kg87uU0y1HvoXOr6DkTHaROhTAM-hqww8fVDqu1-jsXHKza39QK--oUUI0o-ipaVJmAP6eR4JtJhtbnKKCgLt1OamkhLt4pjAxmFZFLWl8XFEl7zNo1YQaJMiElxlMJQg7rjNi_7R8pERPKbkp8z2lUXqIuugC5-vGNDPrUG6p5SCBRSTJFA59yL1dtHfLk6mE6xj7h1BV1_bkd2mQSfv6SXJiTxtcXOkZAQiP-CzzbYO31J8ht_lGufQBmLRzwZ8DkmKAfDUZZj-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=QBSpPQpfXG3mCq9wYMNac7c_H2ZLCsaQ8Tjy6Aw5W6wvFsJGHwu6SBaZfZ875D8SZvESR5sBFUjbN7ytbunZ5plU9NcUWnw-GkjQC7L9jBHOmuviePOeTpE9cygBpz0-Wx2U0AB7glnDIC8yfr-H5-vI367m9vizbXjeAz8f-FMS8QhGGPlqeWNgVt81zUjy4m1QYWy5d1fOIx5n2ZMfY3s_DFeyU7MvwLZKZGNcrHprhoi-KF9j9Vb8Z70rImNuY4QnCgBU9_8kkKpnEWKKl2Ad65TPuFt5vptYPj7PqWT8JRJ46dq1IEORuLpDfvma8fBwWFfuFueW7BkFUo9wwIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=QBSpPQpfXG3mCq9wYMNac7c_H2ZLCsaQ8Tjy6Aw5W6wvFsJGHwu6SBaZfZ875D8SZvESR5sBFUjbN7ytbunZ5plU9NcUWnw-GkjQC7L9jBHOmuviePOeTpE9cygBpz0-Wx2U0AB7glnDIC8yfr-H5-vI367m9vizbXjeAz8f-FMS8QhGGPlqeWNgVt81zUjy4m1QYWy5d1fOIx5n2ZMfY3s_DFeyU7MvwLZKZGNcrHprhoi-KF9j9Vb8Z70rImNuY4QnCgBU9_8kkKpnEWKKl2Ad65TPuFt5vptYPj7PqWT8JRJ46dq1IEORuLpDfvma8fBwWFfuFueW7BkFUo9wwIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=G1DJmnjv01CrbAz6vTf3kYz3WCPMlLJaPQxYuKQjpu9C7c65l215E9GoU9Gmg_wi4ZOlC9CzEdn4s_uBxIrtszoF_mLw5_u7kGFJ5rB9Iv3R6WLHQWiByBEFCIvpYnhPC4oB1Iruh4DubYoutpphHH6m_bram_7s8nQoGeTi88ckXkk_HIs4nHZG3P5Lc8t-x13SfYtRKZ-13s-fIjABLaHd6UrYU_X5LH1IZvhCoTdqGeAq7G38LeU3UpddBoHnInY6kX89hK0jvvOvSZosEamZ0PUje278RsH_3tT5dywt8HyodxpxGZ0QvFAK721G9r7Fj4Bzms5EL_HZgG-GZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=G1DJmnjv01CrbAz6vTf3kYz3WCPMlLJaPQxYuKQjpu9C7c65l215E9GoU9Gmg_wi4ZOlC9CzEdn4s_uBxIrtszoF_mLw5_u7kGFJ5rB9Iv3R6WLHQWiByBEFCIvpYnhPC4oB1Iruh4DubYoutpphHH6m_bram_7s8nQoGeTi88ckXkk_HIs4nHZG3P5Lc8t-x13SfYtRKZ-13s-fIjABLaHd6UrYU_X5LH1IZvhCoTdqGeAq7G38LeU3UpddBoHnInY6kX89hK0jvvOvSZosEamZ0PUje278RsH_3tT5dywt8HyodxpxGZ0QvFAK721G9r7Fj4Bzms5EL_HZgG-GZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=TG--reWxy2ZK3IZf3P1JM-cLUBE6F0qBgkDJxrsFFlmyGmlBmO_FrlXuCg_5TCHSsu4RNAFzaJ2B41H7ulqgho6wbZd3XRJ1aiIPv1J5OXVv5qrW4zBSxaaIQGIH6Ek6WYFEZgb4BOHZjTmW19iKo4xq0xAbMUYkqZi-lcq0fADk-YI2oYfPXOpoOuRX1odMBBFT-FKHFtGCRKlgDZLMaeC1SIbdRG37Z73AEMNGGMFmdAYJGrv8zryCvEH5j691B0qBD7DwDW04AbcX3EV-KrRdGmniP5kIlsFhyUS_IPfO7hT6mSxpDsMp_56tcpVebWqOTODN9UG-1icFAJd1qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=TG--reWxy2ZK3IZf3P1JM-cLUBE6F0qBgkDJxrsFFlmyGmlBmO_FrlXuCg_5TCHSsu4RNAFzaJ2B41H7ulqgho6wbZd3XRJ1aiIPv1J5OXVv5qrW4zBSxaaIQGIH6Ek6WYFEZgb4BOHZjTmW19iKo4xq0xAbMUYkqZi-lcq0fADk-YI2oYfPXOpoOuRX1odMBBFT-FKHFtGCRKlgDZLMaeC1SIbdRG37Z73AEMNGGMFmdAYJGrv8zryCvEH5j691B0qBD7DwDW04AbcX3EV-KrRdGmniP5kIlsFhyUS_IPfO7hT6mSxpDsMp_56tcpVebWqOTODN9UG-1icFAJd1qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SePLuCZbN2zvFiKIf8nyLXLI_Ac06CPYRsY43964-AXs-I2IPw0lr4zQgLuE6gOMkhzzp6cpbHhLyZs_T77UGRriwi3zexarkXsQpQv4BYsaj5JdThDdzXHCGRJP37yKzLvwlh7DHhs5rbXNboqinF2tkI1YPCgJE1iww95NoZNnrQBk5WmEUUkADRFhCi4hfii31rRVpJmYWfQaFq7GQO4vF7lTGAzb0Lo3Ioy7N6uVmco2NXWZR9Sf18K-i2NK22h9prfh0QCRc3aMKQqPwlRLUXdDIWzK--qNVWg7Uv5kLvzBE0-QQ2-qZp_jTvQSY8xCnofERiJiFvxTBJzU7A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=JnHb6fQSZlTnWv9cuOQjtkOZ1RnSovTQL2lOwYG0UrTEgfts6AhqKA7Obxfxw9oqsM1tlvJeZbZIq48zGjbbBJqtKir25t8IGrXQGibSkcKa-15n2xMFon6y09luClrDfxtrBFIRWUkq0sntbNzccbehfiHLJcah39ibP7ILz18h6nbf-XvzJIoLcCV44G6fH_glsXCLLzS0TSQekWf9QBDzZ3HPv6gqHeWBo-7LpzK-LeGf20sEbTEmR-Rv_qpfG5uEWxikWdhjJpp7znz362K40p-ezmrukRggzRqvIziPUQjD9jXvdGLQDvy95fUuNmWA7mQgaDtBV3iaUz8IEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=JnHb6fQSZlTnWv9cuOQjtkOZ1RnSovTQL2lOwYG0UrTEgfts6AhqKA7Obxfxw9oqsM1tlvJeZbZIq48zGjbbBJqtKir25t8IGrXQGibSkcKa-15n2xMFon6y09luClrDfxtrBFIRWUkq0sntbNzccbehfiHLJcah39ibP7ILz18h6nbf-XvzJIoLcCV44G6fH_glsXCLLzS0TSQekWf9QBDzZ3HPv6gqHeWBo-7LpzK-LeGf20sEbTEmR-Rv_qpfG5uEWxikWdhjJpp7znz362K40p-ezmrukRggzRqvIziPUQjD9jXvdGLQDvy95fUuNmWA7mQgaDtBV3iaUz8IEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=D4__aCKxgfTIAIaeNsjqE97Um6AvxxM6M-ul7kf87E8OeDfdyi1Il4AbJLywNyXaS3Lx5hYh--cSUaAR7HxyxxaVTp7RXxd0JpNpOe9cuJpFIUJs5km9tlw_es97ZHjQW2nHapXpSgarEICDoY8TgsVzjYil7zg0UXJKXmsQgUX3lyuXVQyychtRF4ZCqMaRY_fkRMhmMo8zbNE-XCTgZeaqxHsb-NyamfGR4xG2npFTppDV0UMatAzBeKiMmEsQea1vOBrQCkp7tqj1vnFTb68mV0-JRjBLYp0-tuBgUjpnkzhga3FT0XNITNW6Uo7flLCAyZd4tG9xPboSXGgxGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=D4__aCKxgfTIAIaeNsjqE97Um6AvxxM6M-ul7kf87E8OeDfdyi1Il4AbJLywNyXaS3Lx5hYh--cSUaAR7HxyxxaVTp7RXxd0JpNpOe9cuJpFIUJs5km9tlw_es97ZHjQW2nHapXpSgarEICDoY8TgsVzjYil7zg0UXJKXmsQgUX3lyuXVQyychtRF4ZCqMaRY_fkRMhmMo8zbNE-XCTgZeaqxHsb-NyamfGR4xG2npFTppDV0UMatAzBeKiMmEsQea1vOBrQCkp7tqj1vnFTb68mV0-JRjBLYp0-tuBgUjpnkzhga3FT0XNITNW6Uo7flLCAyZd4tG9xPboSXGgxGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=Xu2Lrw8m543a1TTL-I6D8cMPpN38Rzkod04m84fuRzt5F4ExABvWVJ5VN7jNo9i2hYelG4RkgwzYHbj_Sxq4lNkWsghUmheemn2mBruHpnvNNw9jOHJF1ZhFoZm_7OP_Xk8B_P7XyaqA7WP0INXS0Jrf8pOCxjuczJLeRftsbIkuLcmzDHFzeXEtWFDMxy1GN7x2vr6syIK6_4fAvrQRvqfjlMRTpIl22gMW-d0CEa-YCLiR1DCXBSi-kGeZh2GYEPI2DX7U-s33b1vo33VdcYqHJSw6f5FoZo692bqaZOeB_r7D7zIp_AB15YgwZJhjoqPDo-eia1tigEWkw75nWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=Xu2Lrw8m543a1TTL-I6D8cMPpN38Rzkod04m84fuRzt5F4ExABvWVJ5VN7jNo9i2hYelG4RkgwzYHbj_Sxq4lNkWsghUmheemn2mBruHpnvNNw9jOHJF1ZhFoZm_7OP_Xk8B_P7XyaqA7WP0INXS0Jrf8pOCxjuczJLeRftsbIkuLcmzDHFzeXEtWFDMxy1GN7x2vr6syIK6_4fAvrQRvqfjlMRTpIl22gMW-d0CEa-YCLiR1DCXBSi-kGeZh2GYEPI2DX7U-s33b1vo33VdcYqHJSw6f5FoZo692bqaZOeB_r7D7zIp_AB15YgwZJhjoqPDo-eia1tigEWkw75nWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=Ypc-5MEZ4qPm85ioKcl0iwRR-1qEFynhaZd1NM8WC1M7ndPCdYUXbVlYoQ9wtCjrxWCOdyl1TfQ0jGchNpwTVocq3VuEOyG3Pci7P8NQBSfDx9ew73UEqKDRSlu9HzfuuXns13eB3gN2wvhq2gzduDSJJJ6PcXUglDH4xu0vnjjxZsgl089uMcBSvj3l8Gt-rpX6fnveUBKc7sgO9myq0GMSKs4_e6zNo_IcOhBNV_MwK_IUxbvuYHbjP81dYO3RIGxWmeQiilazUQqEXEtYkGS9CKJdyIa3WN8uHyQ62DF1YIerbblMUfQDq8daFS0H2Lwj_2MWLeJK3WfcYZt5zkDCaf-viQq60GYJHkejY3G2Vxhu1r-c6seWVW1DD70mXafLGkmq6RQazQvkR3zti_EfrBDISVPq0oLLW04v-s3VbEaa93QqokzNEqwJ_CFdOUh8zz_ZSuQI-V1wmmO2AgDuLWSQNOIzZXxtlY5ClvTt9tIGQzjkCYqxURKxL4HEihY0hC6Kgh5mifa3PFBSgrUNGNeKoT_QzOmWe-k69PCbYcY45ERZEhRRcn_2qITruLeOdvBqvUHEna7veWLRowT3wKo-_zz-S7Q03TktRxFGp_yDb1t7apquIHJ7o2Cup5P_JT2Ifr7WkQwU__D1dHVgkI1umDeOXchYPcdTTo8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=Ypc-5MEZ4qPm85ioKcl0iwRR-1qEFynhaZd1NM8WC1M7ndPCdYUXbVlYoQ9wtCjrxWCOdyl1TfQ0jGchNpwTVocq3VuEOyG3Pci7P8NQBSfDx9ew73UEqKDRSlu9HzfuuXns13eB3gN2wvhq2gzduDSJJJ6PcXUglDH4xu0vnjjxZsgl089uMcBSvj3l8Gt-rpX6fnveUBKc7sgO9myq0GMSKs4_e6zNo_IcOhBNV_MwK_IUxbvuYHbjP81dYO3RIGxWmeQiilazUQqEXEtYkGS9CKJdyIa3WN8uHyQ62DF1YIerbblMUfQDq8daFS0H2Lwj_2MWLeJK3WfcYZt5zkDCaf-viQq60GYJHkejY3G2Vxhu1r-c6seWVW1DD70mXafLGkmq6RQazQvkR3zti_EfrBDISVPq0oLLW04v-s3VbEaa93QqokzNEqwJ_CFdOUh8zz_ZSuQI-V1wmmO2AgDuLWSQNOIzZXxtlY5ClvTt9tIGQzjkCYqxURKxL4HEihY0hC6Kgh5mifa3PFBSgrUNGNeKoT_QzOmWe-k69PCbYcY45ERZEhRRcn_2qITruLeOdvBqvUHEna7veWLRowT3wKo-_zz-S7Q03TktRxFGp_yDb1t7apquIHJ7o2Cup5P_JT2Ifr7WkQwU__D1dHVgkI1umDeOXchYPcdTTo8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=bjFHbQ8dJhEB8GsYloINVkALD0OJvprcaanTBaS6RmJv1lqp47BRzLUyapOW_EsJbZM2gbpGoPhbLgbBKjuacDF5I6B7DG3anJezQ4h5InekH3Q46Kbq2b7O2VU5Ao0evE0OyIYGoHZ384f2eQgZlusw6R4eScN6sSDnQ487QdCcQ3t9hyIMVPmI7HKCueaAf70eD9EjbkndzVgnpf6V7P88es8JMuEJ03tpwLuflwaZwBDwJYVq6vz0M9dLVIBmZL2ivBswd2m0ugdUXQp6kaPj2T214EYN4fB2unuAckEd0bbLCMfz4hrVZRlp78lgJE8yllrQOH716Y-0_3ueVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=bjFHbQ8dJhEB8GsYloINVkALD0OJvprcaanTBaS6RmJv1lqp47BRzLUyapOW_EsJbZM2gbpGoPhbLgbBKjuacDF5I6B7DG3anJezQ4h5InekH3Q46Kbq2b7O2VU5Ao0evE0OyIYGoHZ384f2eQgZlusw6R4eScN6sSDnQ487QdCcQ3t9hyIMVPmI7HKCueaAf70eD9EjbkndzVgnpf6V7P88es8JMuEJ03tpwLuflwaZwBDwJYVq6vz0M9dLVIBmZL2ivBswd2m0ugdUXQp6kaPj2T214EYN4fB2unuAckEd0bbLCMfz4hrVZRlp78lgJE8yllrQOH716Y-0_3ueVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=niKXJe9HCAg8FXXVUEHjTu8vosaeWG-cBJ_ly63b2HJLabcfez4kD5aNu6aalh7eIBQEZu_U6Xvog0yvBLyrowCu8yyke_0jZt2HbxVnWjb8rrKDUwVB_NJ7xqlYo-KvpPtw9ncZhjMsInqw9TB5PPVox9kym72QnSYNZczkPle4JVBSd7q9fQOnhtZjKQpyf9PNWuCdGZqwVABioQAAWHBHED1RuBJUcB2_cBqwlERL1ESK-t-pS2fvVlTMiMByj8smrx_o4YX15JX9LbRQ6HJiQdzaRQHFYt8EvscUUaw0p1nIwXZFiT6YlyIFv3eTUJ_esV6RzuI-vO2bjpNCqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=niKXJe9HCAg8FXXVUEHjTu8vosaeWG-cBJ_ly63b2HJLabcfez4kD5aNu6aalh7eIBQEZu_U6Xvog0yvBLyrowCu8yyke_0jZt2HbxVnWjb8rrKDUwVB_NJ7xqlYo-KvpPtw9ncZhjMsInqw9TB5PPVox9kym72QnSYNZczkPle4JVBSd7q9fQOnhtZjKQpyf9PNWuCdGZqwVABioQAAWHBHED1RuBJUcB2_cBqwlERL1ESK-t-pS2fvVlTMiMByj8smrx_o4YX15JX9LbRQ6HJiQdzaRQHFYt8EvscUUaw0p1nIwXZFiT6YlyIFv3eTUJ_esV6RzuI-vO2bjpNCqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxTHmYhpYQ8xM3sw4fP4QINjgjbTLCoV9yFL3BbGlAhMlg0kt8VBNSHKX5oYB4ybfwgsfHwpR7yrqaX4TuoLdstd8qsOd9BtdKh_Vco7eZ_3rpTdV1Den00SJB6_vMMVX1HUv_6ZEt904SibFcJKKgr2gy_1vEyB10V_XMl2Z6Lw9Cs7JyejccJR8RW3Qo9wkWfMBG-F4b-JRBH0S5h-7O_bj1OEsqzs-npQgg9e-rYXjvrWSVdBvXKx1xqrywA-uzCGCPvS6sntvIznXpTN6dp_VtQGQSxMQZmGZljRpExd6uuy8MPrxATqbg0tX96uKUS22Hpb74xBV1cOB1PZmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDLLr4XJjuUCQL_gN9Jxs4o2riQvfyei8lZVfp2IbYpBeIwype9P50HDrSRHnUKo-XRvfA3k018zaFoR58bhUn2MnGy24KL_zSSfnXdWB-ZuwoDYIySAcnhfNuRUuqOCw0lwAWm4y1V3vL-X5wO7CoBR01Wk2vK7s4kG51-0ovwWo8DWbYCF_jUzQyzDqOdQ1Cs_M1H6GhDD0cMV_hA-Qu43eCTyNarKMzX0B4t0xruTjqh6_NnZhj9MXTgFf42N3Qh4fC6yBVDcuMIHignp7vBN2FNbcrUesmVoSShSS4KCCkc0zkg0oUF5WPch80lzsPecHQS19hyuVylJJywxiw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=d-OQeCmSKSPEykI23pSVai1_rJtBMC8AwhOifrwTr-9DofE1-CQEWDvbMJseC92ZMMucCjNITpZA4xcOVt_Uzfry25t18MIDR6DGjJOchilHepIhxC3VoLYM-Qz4mPIPr1ZjhVAJNOy5d_qHGvr7p0u_fMkdWiBpjFFyYeTS2nQS0TfSkvjhHQfz9MNvGM_mQPB6OqyU4F5aA6kkZ-frFiJiaEiH1YOy5tM7QlGfmw4MEWO73DxJ19tpjZd_WdxqWmZ5kA3WxJyS3icJ2aUdIbQKfmvwX-6qcv8zDAwLy5onQTalDHJAlkZ3Alfcttal_x21W3I_BicE7mSe28MYCH3DyzZ4ZvvuOMASExi1a4ZoW_TWjz_Ye2t__PzQX3SBLqzsVB77Vl8aETbY9OPWlYMh-MFprT7zY--uYC2fp3vn0bb98ugQrK8EEZwoFZD0KJyeOAk_06_soQBg1rcskhdF9C_Ee2Ek-jERE_YgUpYDwYwvskumDbHWTy2Pd2rOfIoSDlDaph1aW3oE6UUCHKVWAB3UNhSkwI7mEk4NsFW52NFg40m_I7795-gUZJCvw-SKRuUuRN9GvtKdqabAJEFKH32CBfyi2Tuz9n7NV8VuFnurOA-VBZsISrAG03y9Mf2E-xkyI3FxTCEzRup_xLSNS1EMYB_4-MUsDfOqcqM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=d-OQeCmSKSPEykI23pSVai1_rJtBMC8AwhOifrwTr-9DofE1-CQEWDvbMJseC92ZMMucCjNITpZA4xcOVt_Uzfry25t18MIDR6DGjJOchilHepIhxC3VoLYM-Qz4mPIPr1ZjhVAJNOy5d_qHGvr7p0u_fMkdWiBpjFFyYeTS2nQS0TfSkvjhHQfz9MNvGM_mQPB6OqyU4F5aA6kkZ-frFiJiaEiH1YOy5tM7QlGfmw4MEWO73DxJ19tpjZd_WdxqWmZ5kA3WxJyS3icJ2aUdIbQKfmvwX-6qcv8zDAwLy5onQTalDHJAlkZ3Alfcttal_x21W3I_BicE7mSe28MYCH3DyzZ4ZvvuOMASExi1a4ZoW_TWjz_Ye2t__PzQX3SBLqzsVB77Vl8aETbY9OPWlYMh-MFprT7zY--uYC2fp3vn0bb98ugQrK8EEZwoFZD0KJyeOAk_06_soQBg1rcskhdF9C_Ee2Ek-jERE_YgUpYDwYwvskumDbHWTy2Pd2rOfIoSDlDaph1aW3oE6UUCHKVWAB3UNhSkwI7mEk4NsFW52NFg40m_I7795-gUZJCvw-SKRuUuRN9GvtKdqabAJEFKH32CBfyi2Tuz9n7NV8VuFnurOA-VBZsISrAG03y9Mf2E-xkyI3FxTCEzRup_xLSNS1EMYB_4-MUsDfOqcqM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6LGoic4r8mkBkFkwz1QNkkoyhl2xVgPxBxpTbYCRHyQoKFmksPq4n-72ww_uusGUc-vg69MhdeTQ1At9Izg5wG0dx4UbeFT4QUx7TOuY8YgMh1viCCGHR9fL-mOMfNMfsJ5WppPkCjKzgyrA11oPOyWGomft9skM4p6nUbQRCdYOA2ngvByp0xhBLJ_T_BXaFSy5H2rS5BpRbkgIOYo8MOnLSF8gQ8MCFEXOH5BgtWkKqk2ga6yblnKdL1dE68uQBF6BWNKZgl9F8oI0v7dh7dX55wdbVahf318IJ6CHdJ_2vdOHS0I_CR7Kf-aXJDpzLW6knZTZIJcJji6KwexkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2FsdH_sQTozxV_FLlfmLHcwDHJ_Pg2mGoMU2d4hfGPe9AuO9QX91kUrwZJSzzRRKSA0JcAzEtVSp1WsTUpcJ0kUO2_RMn5hNGAcnXDAuNHljqRHC1nV3JOv-7018JAmAXPaw4OW8q_inB26qQWhd-8iCMHY4PzFklSOxXPLbC466kN20xlAnVqRNvA5ilJ4UGf5Rhh3QhxEW8r5tK1q-M3BOdKXRnMEo_Lgv47Wk_JcZWC4Ke2grWmVzhLuGkNp5JSJTy2pgyUwgWVvUDe75I4Ybl8XSkQQr3f3nDjs9mfQBgldwn3YEuJDAwxjOeIem0u6B3bQbPCBVeYo39vB8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8wZXhXEekBanmEzEUFBVV6i1KFGJ2SCEL6xt_jDmkfIvB4sHvZy-bdn7EvMMQ6Lzi2eQCqT8_jtrATIkvKoDjve6IOp_B3D2fyZiKFYnRQ93ymnWtax1yMT5S0c4NK0svp25u7GIrw_h-iuEyGF_cbNfiX8miNLDuTk3HEZsCAukHvwbXkqmZ4cARZcL2KWIvAtyOu8wfGpfsgr5ygFEy-3HUvg4hNzRWkUSnaV9R9i0VdM9uIDEh1Qm8veTnAl_yoD2CbjW2spVBSQUEVNUH9_3nCWfqQCZLvAyxj5Y6XBOc6Vbfw19c8gyg2rEtpH3NJbxkJafqyzM9LbB2VNWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYCOY0CQAfHMM0Xbje_2JWUKehVRH_lieqqO5ghkeus18Vn-y7nkTY6-1b0_D2dKNT4HpZ-Hhni5sk2Lb4SemhCX6HyiV0Z_avuTrl--OW9XyPrV85i59o3USvGxkbn2G03_yVUtXMqNaM0Br194HIP2qRZbf3_mRJ9KMMVF3JJjiknG9otOvQ-DwQQ_H4vM9Cc2eGDGlDqZwiI0yNuAwoa5yFGOr_mhkfer3Kxcf9TO9k9GHZs20X31J06FgVvf1HRSPx3RDFuv_yEA-hMyRmuSf6Ov4sZgt_mS9ZvZIj0EW2FNm2-8o1y4E-XAmxPf1Zspp9J_j11RdSIm2nOe3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6277" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=okZxLFi_sLtgPGkrscMhm00gfG9wlmmFeVh8hgbiBhu0EvPwtK-Dlr38-cx1EP-rqVixS9L78mze-0zohbI0xzAodYzqTryetCPjHL5cFbPT60WgeKEGWxaXHCizhav3_NCOel5Yttc_Oto2kfashVdKD8moif-WkfHTFe4dBpm4NFOhecoi4GHPJoworog01P1TrwAQESyx2zjPs3KkLF37rE3Gsvb54DZqY94lPxl-zGZGSwnxG_mYjVpjrggRe-BFMJhybdKUl91_vp6dvH6D1PeR3aqo4Pnx0hEB31DWv3hfrFYRoqPNlNYxNoRylyolr5Jp5FTOcjKz7VnrnaucjbESyDH-NOdFa4ctXdBf0Z83EtPYvMc9k7DX-w_oQnVlsdOLuW00mg-d5gMtYpjGqps2jVV-vh7wgh8ScmZVdO5GptXnriL-AIxGpZJnITAJlQptFMpkRYswqBWS12Rd8s19_FaT4EMjFmSQ0I73w4ENbvV7O4T5BIW3tdsmnDBtFOQnLDNK-Vk2ssFoIH6YCMKOUe1pw7Zau1hfb_dBjIwtr56Yj-1uXCF5xYElXqCAn4ykSI3xVS27p-Auy6qU7uIwMHA604E3NvNZCvJ6KYXGsvtna_7NSFWqk-nw1QJwK00kf7TPX77IRiIn7dV-4komV77arFHUlZ9zi5U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=okZxLFi_sLtgPGkrscMhm00gfG9wlmmFeVh8hgbiBhu0EvPwtK-Dlr38-cx1EP-rqVixS9L78mze-0zohbI0xzAodYzqTryetCPjHL5cFbPT60WgeKEGWxaXHCizhav3_NCOel5Yttc_Oto2kfashVdKD8moif-WkfHTFe4dBpm4NFOhecoi4GHPJoworog01P1TrwAQESyx2zjPs3KkLF37rE3Gsvb54DZqY94lPxl-zGZGSwnxG_mYjVpjrggRe-BFMJhybdKUl91_vp6dvH6D1PeR3aqo4Pnx0hEB31DWv3hfrFYRoqPNlNYxNoRylyolr5Jp5FTOcjKz7VnrnaucjbESyDH-NOdFa4ctXdBf0Z83EtPYvMc9k7DX-w_oQnVlsdOLuW00mg-d5gMtYpjGqps2jVV-vh7wgh8ScmZVdO5GptXnriL-AIxGpZJnITAJlQptFMpkRYswqBWS12Rd8s19_FaT4EMjFmSQ0I73w4ENbvV7O4T5BIW3tdsmnDBtFOQnLDNK-Vk2ssFoIH6YCMKOUe1pw7Zau1hfb_dBjIwtr56Yj-1uXCF5xYElXqCAn4ykSI3xVS27p-Auy6qU7uIwMHA604E3NvNZCvJ6KYXGsvtna_7NSFWqk-nw1QJwK00kf7TPX77IRiIn7dV-4komV77arFHUlZ9zi5U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=C3ycyjnYrTnCQF5GeAo39tuOHXqzxelEZ2V0JUgZBcjvEFO0rH9m2pyGd7S0WWbt1x-7pkNlY56dTrY4KopgPZvGjYK3JP7RBcjOGhnKH8M4mLyOmR8eFOmBjfjdyPZ4aSOzSuSFp5YaXaBt5x19AHB0Hc1zMJ9Ul98DOxla-XZCSaDX4fZeUiZcwy3S9lsAcNBxWEzLxoxdavRnzZVtIuERrbyjCp2m-b8HvLuSKAmQPFhnJ-iFVKAbdNMbHtQ0eChSZ75TtGbZSanWqGSYdVweSP2JDUgJ-J0ZJ57zzdmFQXJwFOcxFEvWRA5YK_K42F6B2jwHWVURrykINa2rLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=C3ycyjnYrTnCQF5GeAo39tuOHXqzxelEZ2V0JUgZBcjvEFO0rH9m2pyGd7S0WWbt1x-7pkNlY56dTrY4KopgPZvGjYK3JP7RBcjOGhnKH8M4mLyOmR8eFOmBjfjdyPZ4aSOzSuSFp5YaXaBt5x19AHB0Hc1zMJ9Ul98DOxla-XZCSaDX4fZeUiZcwy3S9lsAcNBxWEzLxoxdavRnzZVtIuERrbyjCp2m-b8HvLuSKAmQPFhnJ-iFVKAbdNMbHtQ0eChSZ75TtGbZSanWqGSYdVweSP2JDUgJ-J0ZJ57zzdmFQXJwFOcxFEvWRA5YK_K42F6B2jwHWVURrykINa2rLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KxXihXdT0T4yTRAD2Ykp5n0Zi9XOpCOjilmerU4hobKsf4IfPLiAOqw1KtzfowjPR9T5twRFEYYZlDm4BfyA0Ta-h01E1MISB2wWwBZ7udPi3LaGDb_irrxt3HXg58j0QvEiszhXC-q_jTytKPeAucsYbP41DB-aiHdFEnA1PIUYvwE-hEke9dVL63p0xvsVvMqz2wxT-RJeOYMaxEhd56yutNeZGIkAMpu2ZkJPTJKD_KKzW_xPXDLkEOfsZUyx4kbETRHSEEj5oksS8SgPgsdv72wOGi9VO4W3_EoNXjsiVJ6unX1c6GaLKqjwzu36bZQKip3dINjp0iRMTLOS2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5Q2pnSgfh-tvnEtrASyejT79tEFovh9p5e5V-C7x1b13YoRsnjLFJxUtKuNfFQNiod67_iU34kx_R1tHJ6YeWuiCC7Q9LrhhWzqLcid9B6oAC8XNjMC7ddvMOkPEj2phhvu3DGy3KiWdE9eF132xjiPekFcnY8wnUUjYXfdCadKHcb_5QcXAsT81fvlYBEDBFMANg7Z33n3RXHSGWCyREfQTp73e8tHpJEEgeGFXz4iOdl1n-PhSGc8HkgkqT2tviErxrgUAceIE6cZTb9rVuYWVy9OTSAcZsPnlhZg8NcxbGmzUa65qAb_nYnQtznNFI6wCDPUXkIROXhKcR5s8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
