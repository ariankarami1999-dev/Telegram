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
<img src="https://cdn4.telesco.pe/file/QDr5NkpDVMaxV0aCFNqd7KzpH4L5mCDxMY8-AhORPkov8-m7PtMVgkWuac0lFoY3GiHFV0UdPO9ZzGkfagExYjMuMSE520wyt5HOGP6aiSHSKNhVayfyroqFxYDPq_JTBtJaVDvccVmiXdOjWfmF5RrXY-0sJVsPcZlPXXsUysWmhxODcbh5qhzbYNv-ITWanoa_BkShLOX70KMqnXZXWMzbuLF1CBG2ev1g8OoEVrJRt7Gm9no3XVR2P4BD4tp9bgBDK6bqBJqOMNi9uGJOBBC6ufEMXfIyHm-_kx10ksAst8AGnVYKGzWDfe9q1LIQPT73yw_7CJ_JUAEmHSRjxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 21:15:36</div>
<hr>

<div class="tg-post" id="msg-437281">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: یک هیئت قطری امروز به ایران آمد و مذاکراتی با وزیر خارجه داشت
🔹
کشورهای مختلف برای جلوگیری از تشدید تنش‌ها تلاش می‌کنند اما میانجی رسمی مذاکرات، همچنان پاکستان است. @Farsna</div>
<div class="tg-footer">👁️ 792 · <a href="https://t.me/farsna/437281" target="_blank">📅 21:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437280">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: در مورد مباحث هسته‌ای تکلیف خیلی روشن است؛ ما عضو NPT هستیم و حق داریم از انرژی هسته‌ای برای مقاصد صلح‌آمیز استفاده کنیم. @Farsna</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/farsna/437280" target="_blank">📅 21:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437279">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: فعلا فقط تمرکز ما روی خاتمهٔ جنگ است
🔹
در شرایط کنونی ما باید ابتدا با مختصاتی نگرانی‌ها و منافع‌ ما را تامین می‌کند به خاتمهٔ جنگ برسیم؛ اینکه در مرحلهٔ بعد در مورد سایر موضوعات صحبت نکنیم یا نکنیم بحث دیگری است. @Farsna</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/farsna/437279" target="_blank">📅 21:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437278">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: موضوعاتی مثل «خاتمهٔ جنگ در تمام جبهه‌ها، وضعیت تنگهٔ هرمز و خاتمهٔ راهزنی دریایی آمریکا» همچنان محل بحث است. @Farsna</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/farsna/437278" target="_blank">📅 21:02 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437277">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6HmGqlauDFXmEv5jxc2fa6B_t1znCz9CIHtqEJTvHTPTdg_6WITK2Ij0eQoqFVFyTKca35QBKKUhwyq_EdGIRDp0JPPsNCxP_yrCMPS_y9GQmfG4gTYTZVuNHELZmPPi3gf_VmAjp2gb7tXdPFaE9eH8vf_gk0PmJrGKIGe4L5sEZtBVzgazzXASmJZfgbglRSBfTAdoZbrYPNB_qv-zid6gk33NgxkDudhjNumgHxoeW2EO4uWWl_ZfdqaLlo72oEbYfDv_7Xb5vPiPonkaApC4JqQy3nTkLRAe4zLLhjbzr83jEornGNrfmOosBB7fcip3HVPKD3fZzr-aD3z7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیر اطلاعات ملی آمریکا استعفا داد
🔹
فاکس‌نیوز: تولسی گابارد، مدیر  اطلاعات ملی آمریکا از سمت خود استعفا کرد.
@Farsna</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/farsna/437277" target="_blank">📅 21:02 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437276">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: تمرکز این مذاکرات بر خاتمهٔ جنگ است و در این مرحله قرار نیست راجع‌‌ به مباحث مرتبط با موضوعات هسته‌ای بحث شود. @Farsna</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/farsna/437276" target="_blank">📅 20:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437275">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: اختلاف‌نظرها بین ایران و آمریکا آن‌قدر عمیق و زیاد است که نمی‌شود گفت با چندبار رفت‌وآمد یا مذاکرات ظرف چند هفته ما باید حتماً به نتیجه برسیم. @Farsna</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/farsna/437275" target="_blank">📅 20:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437274">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: نمی‌توانیم بگوییم که به‌جایی رسیده‌ایم که توافق نزدیک است؛ خیر این‌گونه نیست. @Farsna</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/farsna/437274" target="_blank">📅 20:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437273">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: سفر فرمانده ارتش پاکستان ادامهٔ روند دیپلماتیک است و نمی‌شود گفت که ضرورتا به این معناست که ما به یک نقطهٔ عطف یا وضعیت تعیین‌کننده رسیده‌ایم. @Farsna</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/farsna/437273" target="_blank">📅 20:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437272">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">فرمانده ارتش پاکستان وارد تهران شد
🔹
عاصم منیر، فرمانده ارتش پاکستان با استقبال اسکندر مومنی، وزیر کشور وارد تهران شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/farsna/437272" target="_blank">📅 20:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437265">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ci7usPDAwLjd7gEzpjzTcZOFu8uzTZEbPcTqudsjaD2b7TKvErQwUMq56mm5e7jcCp1eI_qXcqCBBFZGV-FtF2qvqbvTBrpMGEMksI4XSXVKZGKI_UsoiSTZ0C1l6Bgrozhm7xsYg614hbQvqBF18RrdHdp3OAfEBbttEcbZCmQ6EOP7JmxehJRY9HFEhTGeHenQRe2VntNjZH_RDHuFkOOFdkDCHyaEdPoUTBY6zm4ESDvWSRbtGDA1uFO72c8qiqWhUy7ad_D1fRkTbXu8VIMapLZcWCtY_MC6hkb-zdR-uYw1wQ21Ix_nH6kFUdlKtBZEM-KbPUcsMGiStW5eXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eeBetZzuyEuVZb4UBScjUyJh33uy5hN8djBIVa3wVAtXMhSpXyk2h0MuasRR3TdvDAZ95FY8kwuqJInuIwpWzisU7UlKcyZl0jYhc81VeY6ZgfTfFz_nGDZ1wh4w1E_KOpUC7hYpvTtSipxhIWt-edMoU-g2ekmmN6tsp8uM5E9DEs5d-YLV9buAUqdgbQp_mz3M2O7alvHpR5BjXgjkJTiufhyZrZhEa7oDxR-wEivRd6llGenjUTJZBVDuvYw-y2BK8_Ovp_397zo94CND-WCcl8Z1lANKJlsKKDbRLe2v4fZkFiPoTYJK4h9lJP6yfEA2E3zlQOMDiTQ58c8iOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vZrgneKfDy2WdpOGG8ToOyR1UEjbr0LZNfFDi4BGYwqSCGV2AXcOlzi0X0zfxsFaCRTU4P5F9nWfjSnhtOx6XTMvTzGR_pzaPlL81TejVwtugLECm4GYYQLoh9gNHxmKZIdRbePh76cdz4rVFxmNcs5DH3iyaxGpvBDI2cpWNbGM91LWk3yrvKaNV2u83n89_ECMmYPewDRA1PHr9U3aSh82gwMYAjsSdqMKTr62zivdl3nA-M1nb9AmydXILTSO8Y10NA5Nf2OgTw1JVpTj0DXKpTXnBCgg2PS_l_wfd2VkWhmvL24x14P2522_LnnXUZ-OGpuirIjFe5J_dHGbFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vTjUTeLsXVUajY_z_feHE4LsYR2WEEN3aQyGgY8SsGpt2YD1PABrsljqZ84pAUd3qWQJO2KwPJ4J0mLbkOZfmUo__RzKGdFaJoxtfvbUJAvteULX5m9OvK3gkoaXw0TwW4GYfbsz98BNKuL0YLeGe4wO6-aGcBocksNFKsXYcr9cGQPd8H601aJ7cnCiCx_ZCBTx8XFbYdZhQ_CS_zfEu3Y_PkjSNs7V7t8zbnHEjKNTFLgyvWdKVvcAnClASwiYsSf--MOaAG3hFqram4IN5m0_VDtaWQyRKJ9X83zJyXkEtlriFj9sy0mft1Ky12Zg1R1-mqH193NQC6F2QjugDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SotXNwXsvJyFJGUcnZz5OMZWzC36svceF5kol8IqN0_1wL_9YvobRcK_K3ghtnuXgnWUmbSarg9L67LYuqUJBfL2-uYw8mjzD4CRhFPcmnG7H5z4Nt44F1NgGBgsPmYp7njNbPkQjkYGT4BA3mKPKx4pOo7dgvJUd3K3iH4U0LpxbqPDQGY2AQkYjuWqOkTHTblEjVwg9z5sDhzBqpB4J5Ek2ipg7Rrg0oFmdTmcXngf1CF0JisaXEnuVCQWJ9ByQ4Wph23A25cWQ351J3hg352m9EGb8C7aSGjqgUkKTWczosZrIU_Zo0he1FQVge6BnFjleVJBWDF2-F6NY-ljCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PLG3ZR8s0QqM3oB4TejHJk4aqc_6nrb_JgVhudjpiZm0LTZrGMfXo1AIpIYNgsx9actT6uCKvEUhuOAZiN2SZ9XkgGz-YGzMmqKdvEiwB9vhp9qpNTzy-B03HVPjsTGA9J6Pr9X7zbs0MMdcF_2JLp-LJ78dj6QUufAtwyiJGxZ0COV5oNbFbioUjsczm5F9v6BfFbbk3CXPTNkvMhZcVucANSJvG1mqwcSJxpRm2ka791s_Ka2lJdfRhLEIHLjqG5CsZ3Adbb33ZR6u-mpeoMg8LfYdjINv0RrThUrv9d2xT53L9vrPKLT_5QgBQOSwXT9aHvOPjsKKEhv6hA_R2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xnh6b1zQ3Wd78ElwBNwEp5vANgYBOk0Q2_cIlauLn1X0v-I31T52uaYImzX_0XhggHIagEtiJgBwCfRUhjiEE0HHooZIH3JfvHyog0Bqejhgn-TWymLLbYYW7sdVItewmwH1yItMaHifN7o8ROt_P7KL5EzqS9_otxVDiwOZsda7QhWYACD5TDf6pe8ip2U29-WmVaLjK1s6F7SGlp-nnyjBWbnnCh0onOmFZNeZ9AdOK6xnzCf5kIxCd562hl6W0u3m5tx6IkUI4NGW130JOvLMudhWgwcgl-KIzqXJ1N02J8h7UsL-tjT_2jJRcYVS3vzr9I1H0A1i1r50WMHc0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سردار عباسعلی فرزندی به یاران شهیدش پیوست
🔹
سردار عباسعلی فرزندی، رئیس پیشین دانشگاه عالی دفاع ملی امروز به‌علت بیماری و جراحات ناشی از ۸ سال دفاع مقدس دعوت حق را لبیک گفت. @Farsna</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/farsna/437265" target="_blank">📅 20:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437264">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/993985f526.mp4?token=NlRUJaD5GDd96o1PriZMzper5-d_TAvqPdLf2Z80ZR5_V5666CZY49YyfDBXH-kThFfX5LLO1NZGdYLd3QhwvgA5uGGLwAHIaikFDmMKEKRMdvebJFs3DSMw6tBJWHICyJBzpwmZjt8MbY9pzaiWELKOap0VreU2vWybYhGVpz2xcQwAezaTQ09G1CKD6aXWVMHa1J9B5n2eZ9SOuHUBxAy6o9q0Y0dtksqa61FUyIuuTPXTJlAbAjBQrAAAllazcRG7CAP8yzZ9LIVNh83w6x72nguiURP-DvfMWS1dE38lKWX6jbDtCD4t7Mbkx3nZVc8UNScQToE4rapkuEDw1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/993985f526.mp4?token=NlRUJaD5GDd96o1PriZMzper5-d_TAvqPdLf2Z80ZR5_V5666CZY49YyfDBXH-kThFfX5LLO1NZGdYLd3QhwvgA5uGGLwAHIaikFDmMKEKRMdvebJFs3DSMw6tBJWHICyJBzpwmZjt8MbY9pzaiWELKOap0VreU2vWybYhGVpz2xcQwAezaTQ09G1CKD6aXWVMHa1J9B5n2eZ9SOuHUBxAy6o9q0Y0dtksqa61FUyIuuTPXTJlAbAjBQrAAAllazcRG7CAP8yzZ9LIVNh83w6x72nguiURP-DvfMWS1dE38lKWX6jbDtCD4t7Mbkx3nZVc8UNScQToE4rapkuEDw1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور گزارشگران و تصویربردار رسانه ITV در محل تمرین امروز تیم ملی
@Sportfars</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/farsna/437264" target="_blank">📅 20:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437263">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2hlUxSudmBZjdTUQSETrgi-ev40z6O_TklVjg3BeXmHxZolwFHxZc7daqKUlG9TASS38MxGKiA9EZlJjyBbUU23gFFnWdPGiDMYyMHvnW1ThJphxb6VjAtsVLC-XdZtSkBNIv9sl67vOV2fXS0XxF6XXVcRhi4V64H40_H6J6PT8K0gm4DWSR1yd8TwjvmBON1__tVGuqzN2g54yCzDDmOstkYnTtWgBUs9L-kSBpLUewSQFH16ywojaoEufpPZ4qdNqGHnXYCqeZNxZsT4zwdQ0xI_8PeZNyuFVIAMoGmb8dYyG3-TNcZkxLzR5jPnc23mYZzDx84NHPUIJIvkWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده ارتش پاکستان وارد تهران شد
🔹
عاصم منیر، فرمانده ارتش پاکستان با استقبال اسکندر مومنی، وزیر کشور وارد تهران شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/farsna/437263" target="_blank">📅 20:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437256">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N23x3ULqtIF35A0l8WnBSKsG-C77XaSjOAbos8o3UA-9eQHaFpxhB7eZPoRLE7c8XGb47uubNwOeIBOZy0M4w_c8RvCU4tzo27U1GTfnk-j2BiOYFpFt8dIY7mtkaHQIv_e6hMYLmk3ROq-2zFoK3mBmzs9Bf0n2yfGScjMQsxjEap4tGrs0hrDA0xNM84ZiWdInCUSWASY8DpzQrTa7wHU9du2EHJ4qLdDrbW0ENI-me36Jq_Z9PyOAgq0vyW4ufHZjmd3p990AApDv-tg0zyLi9eWUm9tOUG8IJed8RocLdpQhDOqXUKzmnuXDjBjky_TXhB1f1mKQfSTXquzvsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tsvr5KVGGn3Dx_3ggoAeMCQLSdZKjDENiJDwjsLhbJRjtwttmO5yVUs61J1i6NiAHPtsRacsCFv1xLzQ4QuueUtjLlmaGuMNY1h7v2ZXSwRV0PuJoS05dXlUk8Ox5OF--yaZdceyhR_UYjba233bmkDCE8vQjo-EaPDWyenCnBf_uYQGjTK5ujxmBC37EMLdOMI_RilYwYwdh0MXJa1gCahHY1lU7hivw1rmi5OtzX8Zw4h5ogRXewCUHzvQjPZgA7GC7TvltVDLyr3NDA9NS75fVuzzPYBKhdzYI3d-4E_IIWvLGfXUx1M4ZqU64JHRT1RHfzVyhe6XAj50bhk5Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G69j4Os5ejNAGQzA5YMl2X0_hHlTxQoZkXg0r6iyHZaF51S6Y02AyM3YAobkgdqaOymwd1ST_KXK-5LqnX2vnfAFSo4BOiCbbL867GIG40-s9QGvkZ1lc0qe53QKLtzZCdBVSEyYEeEC7FIRzX4CyDHzAMmlZCaKr1NDA8ILWanTRYrcLCZokVaNVpZF-BkHgUz6FvHu0whHIqeJdL0txbYlXosOhAO5f-deaSMU9uVARVm7nIAXuG4V3UivTWGPhbLiMMOCaF-ZKx_HLdsipyQsX93oeYkVjf3ybHvN6xJwGhYGPshtunn990VJFGBwn4q_29elM5805FUtiUTa4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TT6zNjg_rZakp1M4XGY8cLqGejOReb4GnFHyH4A_WVFlvud-aa21jkI4eOIMYrqEeTu07ACHFDSpfdaHkuSA2HT7ITTHFjR4okZkh1loyIXCjETAQzVqHMx52j6wV3_N5CRB5_e0nPdd6nngcUBYaqoWKt_midfKMEsGdCvjciBlUZoyETiRSgIsrXRxk85lULdQPmTP3g7eTX9KYTddbLxgMLkthI63zw6u1BtA2bj_RG-sVfIZgUjy8TCrpfiLwOSYWua3WxSidr4iqDq8-4DEV0az16WHVAK3uX2EXPRWuG43By4Q6QzGhOgsg8obH7nHn3vcPf_EiHTzSsp8nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J2kkyKrhaqlgZq6GCwrhBSw2Ym0Rui078BB-FHVHPJJNthJSgDgQzbvR7iy8OyE76Y07wU-rrWtskmGT1Ui4FU902xj_XeMpy_MdUz3xNwYha7DLiSfKtrT0f3vkZOqZgDNKjOflb--347PDRdvMi9vLwP87QWK7OUso_HcwRjCTbHIi2jNqLZ7tMyNFtDxnWuz7jz3URBwmyb5zGDMmxwnJ0vne3g62XdbIRyuPfF7ST5RZYwE5DnuExoQX8q0L1QhLscWytcRtjd97UWVnH6caKiuLEyA3PFdgQpTognL52XT_YsVrLmdr0tRsZ-6eD8ZEkKgXQaiHqFBUmVzszA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OMtUAnGZTBrDK68EbWE9VGzWftjlXtxmFx_9oj7ESz_6l3y9hdRoX9gb4LN1jFIL0ocq8HP2x4mJ3qosavKTgG7OmYWlumfyOZpp08y2KbpU6Mn9porEVhptwWtbb2uurxnAI6X4XkAGW9_RD2vjs-PpLjRIspOZ_K59TWnlPgsGiL_uZKVTGyoJ63MNZW9DvrJYN3l9HF6IPJb71hJp_P2a378jjdRaX6HwIp0UbkQyZBwDWL7-4VfWniRR0kkLfX_bdo4ucYA8-z9mNLX6Qn5a_UBYI5unehat1YxhSP4tM14zER0dZSXZdr7xZgME_Xdqr1xYOmeh34NO6IviBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N23x3ULqtIF35A0l8WnBSKsG-C77XaSjOAbos8o3UA-9eQHaFpxhB7eZPoRLE7c8XGb47uubNwOeIBOZy0M4w_c8RvCU4tzo27U1GTfnk-j2BiOYFpFt8dIY7mtkaHQIv_e6hMYLmk3ROq-2zFoK3mBmzs9Bf0n2yfGScjMQsxjEap4tGrs0hrDA0xNM84ZiWdInCUSWASY8DpzQrTa7wHU9du2EHJ4qLdDrbW0ENI-me36Jq_Z9PyOAgq0vyW4ufHZjmd3p990AApDv-tg0zyLi9eWUm9tOUG8IJed8RocLdpQhDOqXUKzmnuXDjBjky_TXhB1f1mKQfSTXquzvsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
گل‌های شقایق بهاری در همدان
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/farsna/437256" target="_blank">📅 20:12 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437255">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vW1fdOMZfiLY_JzazaVMf7Kb4bhYUsCxxIDgI6udheg0Rj5znbRUB5VnjS3h_iHJ72V5-0VEDnSd5plY9ra3PjQaKmDzBOuJ8kVC-nry95CRWDnBmDqR6_TExr3sAkIfb8s6KVOF2XXSFw21NIZQmntIFu15W76r3EwAe-mwQ0gm1uYhNdhp183hc5UlZhH6k-JAu_SbJo0TbM-GqqQ4aVW1MX-MjAg_KV0hl1Z6gHlGLeLPhzD_KPVu-ITNUuvT57rjEMczhzsRwwNVxfGElPNyGcvVuDanPLIYeZDNY3d43P-lw9FMK_xS8ysGBr7FgphHKkoj5V4tyg4t7LVuFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ: امارات از جنگ‌‌طلبی علیه ایران منصرف شد
🔹
رسانۀ آمریکایی بلومبرگ: دولت امارات در روزهای اخیر تلاش‌های فشرده‌تری را برای پایان‌دادن به جنگ علیه ایران آغاز کرده و با پیوستن به عربستان و قطر، از ترامپ خواسته تا به مذاکرات دیپلماتیک فرصت دهد.
🔹
موضع ابوظبی نشان‌دهنده چرخش در موضع کشوری است که همواره رویکردی جنگ‌طلبانه‌تر نسبت به ایران داشته اما بیش از همسایگان خود از حملات ایران آسیب دیده.
🔹
اگرچه امارات، عربستان و قطر در خصوص نوع توافق با ایران با یک‌دیگر اختلاف‌نظر دارند، اما هراس همه‌جانبه آن‌ها از تکرار وضعیت بحرانی دوران جنگ مشترک است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/farsna/437255" target="_blank">📅 19:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437253">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTYKgk9xrz2MFszw4vrYFklcPZCOYhgTZUcWFgEgwqhRMDYaPmkorIJfCVKH4Xt7xPL-PnjbwQbmvK09hGQ1bsT6BLS8kXHnTXqJkbTRAh6Kt0l5kSGlX4ffj6ojVhSWpIykorSyfWuyu6YVqEBNjlegvhey-36KCH67dCl5nNZFfFXfVJUdQLePQllwxKJgcFfVIDkmSlHsAr3bdEKsqTPYFCie-AO3FQdhKumFruMwAz-Wjv43sjdILehS5AuRbrr_rLmHsqC8vSxtun9_YW8-PL9rfuSkTvnFzU9NxiMIhUV0K5XNfqrZjD4e4hAfHVsTIwHjcgm7MwfJu-gIhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تگزاس امنیت واتساپ را زیر سؤال برد
🔹
دادستان ایالت تگزاس آمریکا از پیام‌رسان واتساپ و مالک آن یعنی شرکت متا، به‌ اتهام نقض حریم خصوصی شکایت کرد.
🔹
دادستان تگزاس گفته: ه واتساپ به دروغ به کاربران اطمینان می‌دهد که پیام‌ها رمزگذاری‌شده و امن هستند اما مسئولین واتساپ به ارتباطات خصوصی کاربران دسترسی دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/farsna/437253" target="_blank">📅 19:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437250">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GUqFRp_6LmWfTOjbGgoW2Pq_N2AUZKFpgN6Sp6PpTzOpIW0YQ2FYG4Me3TzEB5wbZ0x2m-YG38t72Wv-T2xMvcRg02uHxx4Q0TpG1dVe3rEwRwfH63Lgq28r1VB8lV1GI4mb-U2PLatiGPF3UsH0kN9O-QvqgeishWGYwUGuIr1nK20CdJiDg9g4xKS3VNOXbtsDD6FsOFt3UBsORL_kqaDP1XY88J68oGnffiKy9GLpY62yiMwypL7elqRnjtT3cURAueroMiU7Khkex9ziBSzbSul4QkQtoR4aV_L8VtAGnJv0GNbbdzXKuFsmxeAFtdmsa6DXTs-pjvMK92jYRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qyFqMdelbEReuMgwyYr_oXbdyTKgF4shBmoPTVaW4HklO5SgvIhFzxtenM1WBjDZDLK8X3NTIUgc0SCEfSlN0yRe1UvSas-og9qiuwTbx9d2059T4D6tT8esxnQkM0UlBmS2BBDQtWLrECiv9Z3SZ0Up8mj602SsYmvHuHPXSPXAHYbd36nWQDRzbcZ8xKQxbLxI_TUIlMYW3W9597UIAXo1rora_VXmr8CiiU6Z5Vs_kqYjrD8hGAQdVO-VBDjhpN1VC9lCF1klLu50hW2NJUvHH1RkQoFz-nW81dOiCoVSCOtzBFqgmmxUfT-9uf8Zc7rzGUlzvO1FynFQNGm89g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/erkHWQGutT7gJE7kCOkl0LFS9FIikeiMoPWkcc_BssFoK9x79sCaKH6-FQCTUa6ijj5XVtmuEtEfR46Q4sOr_RV9H0ZLIG0_lpj1Y068uHgTfMbMQsgrQK1l_BiwxCBVhCIbkbj7yAuzdWlLV9FIW7PEiUPsm8WSudDrSO9Qd9yYFC2KC2U4P3idAUmBgalEui7yUdjnV5UAE_YPclL0jLqq0VzpQv1uBkVcW9AG5fHLPNklLV32D98Cz1nV8Sx7jPsxWc3opfVogJK0nKzYW30OJ5yYp_dTmZTuB9vOLGx1_0X5s_3SLrp_1mNeFUpdxLSFsPw6nDnyaPIqT29hGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
حملهٔ وزیر امنیت داخلی رژیم صهیونیستی به اعضای دستگیرشدهٔ ناوگان صمود  @Farsna</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/farsna/437250" target="_blank">📅 19:14 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437249">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🎥
جنایت ترامپ به روایت کهنه‌سرباز آمریکایی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/farsna/437249" target="_blank">📅 19:07 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437248">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/878a398064.mp4?token=jiwM0uqEtbOiFofwiLeSUfvBWlAlPjRZyYrEtmmlHMvu5EF_dJhaGwSlU6S4kGbenUhyiiRIlGgfTkKmJT45yCKFf5RmJnemNY3OOiCwvIfqGymihAhjclaDuJ_LRihJqFAQyw0LDE5h7ccB9FITeFU-gwGrKZq7shVBtEbD58_7RFDULT_HjWamNkArZ2sPrtqe7hL0txDqdPVT5xsP8C89AS84aIdg4_ds3INikp0yWHG2A7zPEFE9l_wYg_ydC7soIJC74dh_UqKE--C8uLHyWp1-la1DTlzhb7xloy_SwuAR46VvnBpd9GxA4xC4txsGwKE7fYC1mSXPxdk7HnB-3asoU6Gts5SAxFBkMQgqGsOEzYP89apBru32IaKPWuGp9vzam9XeHiabe-AcT1NDiPtZvxZ55DZjPYFxH1VTZcHCYjJeM0JDnRf9C8DEljOeB_PCqfLI8PXXjZOvYKc-8U3nj3QWycoptBEv6dG0F0YL0upwtKCbF6smZ9JoEZjtlFytNazZM91BKl6XspS-198maXvm1MFuzWnon6qlCK2bsEoHDAlef72ziC9GJsZJtRFmNdRtLPsKb57TbfHmUdYOPZbL5QLrueHbAuBv06NfBwup9HSLPcXRefqhHyif5AhPgzYELdC2BmGsSSsQSo_gF8nsBCPTkzc1HPU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/878a398064.mp4?token=jiwM0uqEtbOiFofwiLeSUfvBWlAlPjRZyYrEtmmlHMvu5EF_dJhaGwSlU6S4kGbenUhyiiRIlGgfTkKmJT45yCKFf5RmJnemNY3OOiCwvIfqGymihAhjclaDuJ_LRihJqFAQyw0LDE5h7ccB9FITeFU-gwGrKZq7shVBtEbD58_7RFDULT_HjWamNkArZ2sPrtqe7hL0txDqdPVT5xsP8C89AS84aIdg4_ds3INikp0yWHG2A7zPEFE9l_wYg_ydC7soIJC74dh_UqKE--C8uLHyWp1-la1DTlzhb7xloy_SwuAR46VvnBpd9GxA4xC4txsGwKE7fYC1mSXPxdk7HnB-3asoU6Gts5SAxFBkMQgqGsOEzYP89apBru32IaKPWuGp9vzam9XeHiabe-AcT1NDiPtZvxZ55DZjPYFxH1VTZcHCYjJeM0JDnRf9C8DEljOeB_PCqfLI8PXXjZOvYKc-8U3nj3QWycoptBEv6dG0F0YL0upwtKCbF6smZ9JoEZjtlFytNazZM91BKl6XspS-198maXvm1MFuzWnon6qlCK2bsEoHDAlef72ziC9GJsZJtRFmNdRtLPsKb57TbfHmUdYOPZbL5QLrueHbAuBv06NfBwup9HSLPcXRefqhHyif5AhPgzYELdC2BmGsSSsQSo_gF8nsBCPTkzc1HPU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارندگی شدید باعث آب‌گرفتگی خیابان‌‌ها در گرمی اردبیل شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/farsna/437248" target="_blank">📅 18:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437247">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
انهدام یک سامانه گنبد آهنین توسط حزب‌الله
🔹
حزب‌الله: یک سامانه گنبد آهنین در پایگاه صهیونیستی برانیت در شمال سرزمین‌های اشغالی را با پهپادهای ابابیل هدف قرار دادیم. @Farsna</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/farsna/437247" target="_blank">📅 18:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437246">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🎥
حملهٔ پهپادی اوکراین به خوابگاه دانش‌آموزان در لوهانسک
🔹
حملهٔ پهپادی شبانهٔ اوکراین به یک خوابگاه دانش‌آموزی در منطقهٔ لوهانسک دست‌کم ۴ کشته و ۳۵ مجروح برجا گذاشت.
🔹
کمیسر حقوق بشر روسیه، گفت که ۸۶ نوجوان ۱۴ تا ۱۸ ساله در کالج استاروبیلسک دانشگاه تربیت…</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/farsna/437246" target="_blank">📅 18:29 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437245">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-43.pdf</div>
  <div class="tg-doc-extra">3 MB</div>
</div>
<a href="https://t.me/farsna/437245" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خط-42.pdf</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/437245" target="_blank">📅 18:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437243">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
انهدام یک سامانه گنبد آهنین توسط حزب‌الله
🔹
حزب‌الله: یک سامانه گنبد آهنین در پایگاه صهیونیستی برانیت در شمال سرزمین‌های اشغالی را با پهپادهای ابابیل هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/farsna/437243" target="_blank">📅 18:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437236">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mNSLl6U0E-bnvhKLriir0rGih-GFqfz18hhYJ-KWGEZidlAGoDnA9rM1zMttetBJT9Ve8rJ4Bf8MwBvs5dGjk5RqPKWLHVo34xVRfYI-yGoWyz5ZUUEHOWBsd952ZNq9QH9DHVzGtIXknnUbfbTQ6ZRb5SsFMabspINHI4I5Tcxt5etpLppXgU2T1Gu3CfUPIE3E6FR50o9TmGezak9KpEq9fm312-1_uvVKG4TPPZxsmO4h10Hy8cBmc57cNW1nXyfzPZnRSlNMVjFoEGRL4guehSSeTQ4KpkSW37SsWcE1NrE1sF6FZJ-ybEIpraVqQ2XK2nMwNfP4N-kdsK_gOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L_EyMolbsJrD6PhooUmR2RgymD6zJ_jEhA193lRC6TZf8ny7HRd37oiTlvFTYc_U4tGRXXhIFfv8q_rO0H2so8OJahjrvCdA0yg4VIB5AcHWjAUg4MJLsg7Qn3ALkSuG3xpFg8ItYN6BrAaVEir9PgQE26IyscKdf5EvpCnmOXkXksBaPN3rZYhv7vK4lNN0nkHVKK8dM6WuiQ6eKKNYa66uOgip8KE89CP4nEemXpiIF0YTS3Bi00QpEFcDWhjuwlIL7Y6_TLlYyqGieYF7CMT9yln4d47XTD_hULoFpOkA6sWztglxyMTIScTqk-pdlyr03_DS2fON695dns-Swg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G2_PrUQihw2azAWgUDVCQtuopxR1GGBi0oirLya-Sb_2p9OrMsMxqXx50Yk5MyBY0Y9L6h86s2CxhuvrHeWclIbZhJjr3GZkhlvdtilhfw6KfpSRPQtq10aIvuCVxY7tgt5NakphQuz9Gu4qR8-wuMaTUhlP6dTNMSrvWpTMfuXMOn_sErRJG-mjsugo-8lGzbSmfoWKCnxo-OMS1yqX0-eh9VSmqjAdXz2btVnlUMulUZUkmDUdlfmXKtCml_FuoRGe9ciNPMj88VyrAmDagWo2A1AxAfbjTgVgjdfQocdZJQCaiEYCQpwVhw2LnBWUuZw-ssoy3a3-R9jmhi5EhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XvjGsyfmckytDQokYkHQA7rrBA57BtRNUhv9Fosz6g-Db1qruxEJudsfuWeUiSLc02chB7iadMXMPVfhVKCE4KfJY-xYQTuodQYPoOSfuD9Vtr-CpATsoLCfQENAX8lbC4nozzHA1uHQtloQtPcQm4Pt2_426E6qfb2GEFXeKBKh3bHd_AKeQdRXb1LcXtV14rxmrWEnl4c-VzwAklMD5MRCYg1eqx28CFSd5geQPNn8EPZPSyzN-tw4SvVhpvc3kCQdqQ5lzW7OdErccysDx0iMB50QQ6zRKO6Vg9t4zp10sN6c1FhmttucdOxYc7LgVyXhjyLhh14epPIMruC4yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eVJaPukA675BaQ9BUUSTQc9bgz6eM-OUJVHkWZWcdppoaxOhNCNIiH_6dirQ0zU56EqEr4LDfs-C9RYKPq8r2gMlr9YvG2e4FYXCAzC7hhPtJh-fbjAmJW1PR_Nlo7PCzarnYrVSPqWYbr75-5lsxgnAD3k3UiAVCusLXsv3Uko9tGEZpjJTl-Gqzd4wye0wVCz6awMLD-YrZwM8IqRrzYlYzvMTpNseIyoBamJx2r5mmxG2nFCTNssvLyQtiH20YSfhsFxp3UndnEh74TlhSWui-gpi1BRObq-6lX7HWlZEH01_uJCMWc4WO2YmdcRuPh6eRhwmUtxQgIs7gyxDQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YyBlctc82e12RlRjgTrrdsjTFdpkaa2d-C1zpXSvvxdasnj6a8jav8a7yUey9O8isj7U1GnBQ79pG-BFEngxlV7iLJkzxynkjYS5fjhqSfpct5zTzRpZW0JjDss7fUkepM_ES6famrznkEFPZwf_K4bY9LH0jxvR-piO4eI2FrEOXZuLSse49Mcb8YVzi9xtJoou-5ExRvF-kg9Fg920-175U1acUDmAHpn0dSpiyO1_vESS8H2WJ22bkZPW866kfwBdR_OBcop-nF0C-BCGfknHfHQf9fxY5DaesAcI3WvGRwM_eJCIUkf7kNLDh7bmueB5pCQxbxAPPMPe5U-lIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g6v0xEpWUGlpZZApIe1kdpaEGZjzm7k_EzlVtJ6oHaVXemfbU3vOuPEjOi7qe3lgqF6fEYaxf7k7CBTVcSkzkJm_1ZJad2AA2LP4Ozmn1gJ_jhOMddE-SUMN2bgIm_5y2Vnf7CvyiyP3QNB4PkilXWISCqMIp8mzOcuLdtbEz1NzKYClb2Mh-1-_9_5O5I5NvzUVsfrwPto7ruu2vwk1N7rX80BsZDUJzP9cIkEyRxpaNOiZ4SdPwPW8O8AzelP5bFUNJ3QdDp0SgmWq5fKNFVeASYozWS0ARim1Yzovw56g43FXJMBI2qtk8tFxB6V_WPfghX8y1uMhxgyrRGRZjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امام جمعه موقت تهران: دشمنان در صورت خطا، موشک‌های جدیدی را تجربه خواهند کرد
🔹
علی‌اکبری در خطبهٔ نماز جمعه: نیروهای مسلح آماده‌تر از همیشه هستند؛ دشمنان در صورت خطا، موشک‌های جدیدی تجربه خواهند کرد.
🔹
آن‌ها در صورت خطا، جنگ فرامنطقه‌ای را تجربه خواهند کرد…</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/farsna/437236" target="_blank">📅 17:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437235">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzFGVgF8g3xTmwBCoAl0NKbIU5724ZUl2CxTJ-0K5KT7OKdDksfdh5xeMRU980qHhtQRILHcDmB22M0r9h_DkkefoJa9zwCNoIodD3HU_8iwZo4HbIzo8QflYqPZg3hxhGRGDrrk6Tueqlgr5DVqEa-F_EOB3GQkIw5A3_QY4SifUZjUOVMAo00KPKWDtpZQ1e6nNblDCna4kBo1RRJLTmCjJaHnQ12tG3tFputHH5BxYUmeMWNOiNFESiilh8-5R7oB2Zk_S7wL7_P2GYsEQzwZavMDcwN3Emwu1Gq1M8fqN1vYtybKe1o1ysuyISkHZySZ_3gL7H10pufX2R9-wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مقام ایرانی: خبری از پیش‌نویس توافق با آمریکا نیست
🔹
روزنامه «العربی الجدید» به نقل از یک منبع نزدیک به مذاکرات جمهوری اسلامی ایران و آمریکا گفت که سفر فرمانده ارتش پاکستان، «عاصم منیر» به تهران به این معنی نیست که توافق نزدیک است.
🔹
وی همچنین خبر داد گزارش‌هایی که اخیرا درباره پیش‌نویس احتمالی توافق ایران و آمریکا منتشر شده، صحت ندارد و صرفاً گمانه‌زنی رسانه‌ای است.
🔹
این مقام ایرانی گفت که «محسن نقوی» وزیر کشور پاکستان حامل پیام جدید آمریکا برای ایران نبوده است.
🔹
وی می‌گوید سفرهای مسئولین پاکستان به ایران، در راستای تقویت میانجیگری اسلام‌آباد و نقش آن و تمایل برای جلوگیری از تشدید تنش‌ها است.
🔹
این منبع تأکید کرد که تهران همچنان خواسته‌های آمریکا را افراطی و غیرمنطقی می‌داند و بر این باور است که مشکل اصلی مذاکرات در واشنگتن است نه در تهران.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/farsna/437235" target="_blank">📅 17:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437234">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d9b283db6.mp4?token=pVGNMiF2WGoUTtk-wZj-nrpf6vDyrbHStiDv99Axh9Sw0g_od97yK8waTWfEHRoFW5hv7caXCOtXa4Qn8CIWrbh3HbF3ZyLzM3P92OJXhq8awJu_SOqLl8KYfNRFSBUZiOt2xC3aJmicimUXYOEAV6tsxZXdZGkgdz3bdfgYGGcfpW_NJhynW7K_Xh3TKa8DlYWgN_kxhYym-CV9QpmmHXgItZtTGVrZfqvX6Oy7FOLQXV1MPpD4nv3ZAbrfYPvlnzWAD_jhcX5qyPHncQXpfP-f_6Nrcogl9nNaijHbzDPCh7uGnpeJRKT0TcOLr-9w5PXvDQXSFweBR8CeyCTgG4NsIXwenxcwsrGrfmgxS-8xJpJxkMmIDw27AhzV61mOJqKrI8ajGmnQ7-_to5RRlIk3DwXBio-rJiAvnnNR1vHcvhututlSOAihkKN7hCz41Ojn18GPGbIuGgnYbgME1l1x93-206SraM3Qt1ZeCRw2f6YK-HxKcqHcSZ-Mcj2LX4o7Pnfa3ITU9ncN6ePOm6oDN05Djbgp4VgiikMnlTPfWa7Gk0V6tiy8MrwwwmTVtHodhNn9ceZfFf0o09BH1X154ZvqBfymIXXKxbdQBMnpCCV5bN4c4B5DakIZ3b0ZOr8PFxadZgFqOBQ-TweeGdFnr1noppK40MILOkP1H9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d9b283db6.mp4?token=pVGNMiF2WGoUTtk-wZj-nrpf6vDyrbHStiDv99Axh9Sw0g_od97yK8waTWfEHRoFW5hv7caXCOtXa4Qn8CIWrbh3HbF3ZyLzM3P92OJXhq8awJu_SOqLl8KYfNRFSBUZiOt2xC3aJmicimUXYOEAV6tsxZXdZGkgdz3bdfgYGGcfpW_NJhynW7K_Xh3TKa8DlYWgN_kxhYym-CV9QpmmHXgItZtTGVrZfqvX6Oy7FOLQXV1MPpD4nv3ZAbrfYPvlnzWAD_jhcX5qyPHncQXpfP-f_6Nrcogl9nNaijHbzDPCh7uGnpeJRKT0TcOLr-9w5PXvDQXSFweBR8CeyCTgG4NsIXwenxcwsrGrfmgxS-8xJpJxkMmIDw27AhzV61mOJqKrI8ajGmnQ7-_to5RRlIk3DwXBio-rJiAvnnNR1vHcvhututlSOAihkKN7hCz41Ojn18GPGbIuGgnYbgME1l1x93-206SraM3Qt1ZeCRw2f6YK-HxKcqHcSZ-Mcj2LX4o7Pnfa3ITU9ncN6ePOm6oDN05Djbgp4VgiikMnlTPfWa7Gk0V6tiy8MrwwwmTVtHodhNn9ceZfFf0o09BH1X154ZvqBfymIXXKxbdQBMnpCCV5bN4c4B5DakIZ3b0ZOr8PFxadZgFqOBQ-TweeGdFnr1noppK40MILOkP1H9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار سی‌ان‌ان: ادعای فرمانده سنتکام در مورد به‌عقب‌رفتن چند ساله صنایع نظامی ایران درست نیست
🔹
به ما گفته‌شده که ایرانی‌ها توانسته‌اند پهپادهای جدید زیادی تولید کنند و برنامه پهپادی آن‌ها در واقع می‌تواند ظرف ۶ ماه کاملاً احیا شود.
🔹
پهپادهای ایران به‌شدت…</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/farsna/437234" target="_blank">📅 16:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437233">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">شمار شهدای لبنان از مرز ۳۱۰۰ نفر عبور کرد
🔹
وزارت بهداشت لبنان: در جریان حملات رژیم صهیونیستی، ۳ هزار و ۱۱۱ نفر شهید و ۹ هزار و ۴۳۲ نفر هم زخمی شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/farsna/437233" target="_blank">📅 16:56 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437232">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پیام قدردانی سپاه پاسداران خطاب به برگزارکنندگان حماسهٔ اجتماعات شبانهٔ مردمی
🔹
مداحان گرانقدر، خطیبان ارجمند، هنرمندان متعهد، ورزشکاران غیرتمند، مدیران و تمامی نقش‌آفرینان تجمعات شبانه مردمی سراسر ایران اسلامی؛ بیش از هشتاد شب پیاپی، خیابان‌ها و میدان‌های ایران اسلامی در شهر و روستا، به تماشای شکوهی نشست، که شما با سرمایه ایمان، غیرت و هنر خویش، به زیبایی خلق کرده و صحنه‌هایی رقم زدید که در محاسبات دشمنان این کشور، به‌ویژه آمریکای جنایتکار و رژیم پلید صهیونیستی، «معجزه‌ای غیرقابل باور» تلقی می‌شود.
🔹
روابط عمومی سپاه پاسداران انقلاب اسلامی، عمیق‌ترین سپاس و قدردانی خود را تقدیم می کند به  شما خطیبان که با روشنگری در تریبون‌ها و سخنرانی‌های آتشین، چراغ بصیرت را در شبستان‌های این مرز و بوم روشن نگه داشتید.
🔹
شما مداحان شورآفرین که با نوای حماسی و مرثیه‌های روشنگرانه خود، روح غیرت و شهادت‌طلبی را در رگ‌های اجتماعات دمیدید.
🔹
شما هنرمندان متعهد که با قلم، تصویر، سرود و نمایش، زبان گویای اعتراض به قلدری‌های استکبار و همدلی و حمایت از نیروهای مسلح و مدافعان وطن و همچنین غزه و مقاومت اسلامی را بلند کردید.
🔹
شما ورزشکاران غیرتمند، که با حضور مقتدرانه و نمادین نشان دادید که میدان ورزش، عرصه دیگری از جهاد تبیین و نمایش وحدت ملی است.
🔹
شما مدیران، میدان داران، مجریان و خادمان گمنام در فراهم آوری امکانات و زمینه‌سازی حضور میلیونی مردم مبعوث‌شده ایران اسلامی نقش‌آفرینی کردید.
🔹
شما حافظان امنیت در کسوت انتظامی، امنیتی و بسیج که حریم مقدس حضور یافتگان در تجمعات را، از گزند اهریمنان و خیانت‌کاران به ملت و کشور پاس داشتید.
🔹
شما خادمان فرهنگی که با قریحه و ذوق مثال‌زدنی با متون فاخر و تصاویر ارزنده خیابان‌آرایی و جایگاه‌سازی کردید.
🔹
و شما مردم مبعوث‌شده بصیر و آگاهی که این هشتاد و چند شب پرشور که طوفانی از «سرمایه اجتماعی» و «وحدت ملی» بود، در برابر چشمان حیرت‌زده جهانیان، ماهیت مستحکم و بازدارنده نظام اسلامی را به رخ دشمنان کشیدید و با پیوند قلبی و رفتاری با نیروهای نظامی میدان نبرد سخت، ثابت کردید که حماسه‌آفرینی در جمهوری اسلامی، نه تصادفی، که برآمده از یک اراده اعتقادی و ایمانی، باورمند به منافع ملی و میهنی، هماهنگ و عاشقانه است.
🔹
امروز، به برکت مجاهدت پرشور شما و ملت لبیک گو به فرمان مقام عظمای ولایت و رهبری و فرماندهی کل قوا حضرت آیت‌الله سیدمجتبی خامنه‌ای (دام ظله العالی)، قدرت نرم انقلاب چنان در تار و پود جامعه رسوخ کرده که هیچ تهدید نظامی یا روانی دشمن توان مقابله با آن را ندارد.
🔹
بی‌تردید همه شما وعده داده‌اید که تا پایان راه و تحقق اهداف عالیه انقلاب و مقاومت تاریخ ساز، در صحنه هستید؛ چه در زمان نبرد نظامی و چه در زمان نبرد مذاکره، چه اینکه می دانید مذاکره، صحنه دیگری از کارزار میدان نبرد است که نیازمند استمرار حضور مقتدرانه و پرشور در خیابان و پشتیبانی از افسران عرصه دیپلماسی تا کسب پیروزی نهایی است و این "وعده صادق"، بزرگ‌ترین سپر دفاعی کشور عزیزمان ایران است.
@Farsna</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/437232" target="_blank">📅 16:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437229">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnEa5HrM0wgyxBtP5ofvSdv34z9Xys4Q3BzS1KAjCVKv8y3w8cvNCO_gmHO76prJU3iO3iRoeh1BKJXEPyj17daE8ioCd6gO1XQT09zrZkVOVGuR2WPODljT4iBAZENK-fVunyahnmo12eSlTRSYZy4eBCzedCtLrHdUoKbrSbBtWMq78B8vBbYUzXKHlp-G7IFOeG9MCZjxVDO6q5xpuZ7cD0oGOzVPHyuoQXekOqP9ZvehFb-n2B8fiDpctVHeV-NBzTPJkNrX2pg7A_ENLkRUN2LcMun6PyizgJcN3yMlhLcX278rv8gbSwcy4CErNMkWBeLj_5mnOT8ZxsRhOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کرکرهٔ من‌و‌تو باز هم پایین کشیده شد
🔹
تلویزیون من‌و‌تو، شبکهٔ تروریستی فارسی‌زبان مستقر در لندن، در اطلاعیه‌ای رسمی اعلام کرد که به‌دلیل محدودیت‌های مالی، ۳ خرداد به پخش برنامه‌های خود پایان می‌دهد.
📌
این شبکه تاکنون با دلایل مختلف ۳ بار اظهار تعطیلی کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/farsna/437229" target="_blank">📅 16:40 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437228">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130acd57d.mp4?token=K4HZD7-S5pywihhHeiYAAXw7wVyliDzTJeRvdkwcpHDiNQxiH2ATDpi0mvnXSQB7vSfQFbjR-OUS4z75k9_kDiwAVq1NN6jQULTNpSrl73Xxw53AJP4XuTBSYBn-Iz9R5iX2W3L-iJfhz0dsUb9BlCoq7iTcBmpdvRpQTyh8qI2uN-UI3grnlBGyIEADEiqDd1_cjnRxz4dI0_jyxqwDU8ifhLW4bhhsdGnJaa53qe1ccVaK8MvZ1DeLRLwY241TNRGav7wDdApw27VI9DCy9roVA4ZhiuB3LpXlQhwNozUfYP4kyhVelo3f5V2Pk9gpiOJ5T3IuXjGWIV7gjK_6oI3BqYeQcd-2vpCewikn9jIZ8l14e0FSrUzj50EYNT-Y3T3LynVrNX4z8y1idWDhq_XAp8TERWFhCX2F1nTUxm5gt7csYUdqKk-2iCcPkXgSphQ0bVPIQ6Bp71R5qpLJdkzyxlGackwqXVuJfGpO6qGk6ipZ7VFAAScfHx57H9uIrtxHRIbm0PomPdkA-ji5ziVDFhDIluy4e_ti5dDUd2qn0LxWiNagIDJHZm_4hbL7FtAhDOgN91j5nWqfuSUtnBhVxXJ7qsJe2Bham5ir-pXLGUVE0Z8UZTIepwCLbt5NXaixZfTxrXZ6-vNJhBvCR6LmNOAqix-jHC4i86b4wWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130acd57d.mp4?token=K4HZD7-S5pywihhHeiYAAXw7wVyliDzTJeRvdkwcpHDiNQxiH2ATDpi0mvnXSQB7vSfQFbjR-OUS4z75k9_kDiwAVq1NN6jQULTNpSrl73Xxw53AJP4XuTBSYBn-Iz9R5iX2W3L-iJfhz0dsUb9BlCoq7iTcBmpdvRpQTyh8qI2uN-UI3grnlBGyIEADEiqDd1_cjnRxz4dI0_jyxqwDU8ifhLW4bhhsdGnJaa53qe1ccVaK8MvZ1DeLRLwY241TNRGav7wDdApw27VI9DCy9roVA4ZhiuB3LpXlQhwNozUfYP4kyhVelo3f5V2Pk9gpiOJ5T3IuXjGWIV7gjK_6oI3BqYeQcd-2vpCewikn9jIZ8l14e0FSrUzj50EYNT-Y3T3LynVrNX4z8y1idWDhq_XAp8TERWFhCX2F1nTUxm5gt7csYUdqKk-2iCcPkXgSphQ0bVPIQ6Bp71R5qpLJdkzyxlGackwqXVuJfGpO6qGk6ipZ7VFAAScfHx57H9uIrtxHRIbm0PomPdkA-ji5ziVDFhDIluy4e_ti5dDUd2qn0LxWiNagIDJHZm_4hbL7FtAhDOgN91j5nWqfuSUtnBhVxXJ7qsJe2Bham5ir-pXLGUVE0Z8UZTIepwCLbt5NXaixZfTxrXZ6-vNJhBvCR6LmNOAqix-jHC4i86b4wWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم ایران ۴ هزار دقیقه در دستان مردم کرمانشاه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/437228" target="_blank">📅 16:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437227">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">زخمی‌شدن نظامیان صهیونیست در حملات حزب‌الله
🔹
برخی منابع صهیونیستی اذعان کردند در جریان حملهٔ پهپادی حزب‌الله به پادگان برانیت (مقر فرماندهی لشکر ۹۱)، چند نظامی صهیونیست زخمی شدند.  @Farsna</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/farsna/437227" target="_blank">📅 16:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437226">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اضافه‌کار بعد از ساعت ۱۳ ممنوع شد
🔹
سخنگوی سازمان اداری کشور: ساعت آغاز به کار و خاتمهٔ ادارات ۷ تا ۱۳ تعیین شده است؛ طبق بخشنامهٔ ابلاغی، تعیین حجم و درصد حضور کارکنان همچنان در اختیار استانداران است، اما ساعت آغاز به کار و خاتمه قابل‌تغییر نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/437226" target="_blank">📅 16:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437224">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AP9uZxW4LcRF-AWU9Fs5bB-ybb2QFY_u0A6QpjDSdW-C2OBngLmrFnraIL5r7atqKSO3QGlS_lJ7qL_He4g3F5xS7DxxPrlz2Mu1_xcYOduJ--j9K9bOVjZ92USvXMkJfzg-5zOR-DponNj2khQEsKWs6ig000K6fNeDiJf3iBRG0IB_hZ3MXVhzDyGfjGgHWm7HuAGCbPMDzKXr4mHuAvoweCooaxWiLfIzDb7Qz3r_nTO22BXGLn3LJ9WTO7nvsGlToiiDHQw_9xji0es9LT75c99R_eh_LuB_YoqUbXn69756TcRaLZyTLV3Z366UCN3ttTpD8MWOzy_bJhqFKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba3f4a10bd.mp4?token=sjXBaeo-P_Hnmrb8DVMfVppZ4VgPwUF8wnYAI7ZOeiJqJX0Z-FtyDKELZEDsbn8YSJmVSTP0NmIe2Wv7rtOG6n1f4N9ddsvYLG_wTsEZJqJiXfd_MZkkfSVl7L8Vk7XcVxwX7au7rOb5JpuJ5P3UZA85YmmZ7PKjE2LXMKV5mE_gFn4yXa9ZJSMWe1_EUTVlh2jhwFuqj914sBoQWBBWR-eCiKJUG3cl2LbwWigo0j4Xtdvfkc5T8zHQNomZyz8wL7wh0xnZRF4XNPkA0xfiyHnrs1TYIdfUxfFP_miD650l6yIG4GfqBod3lbl6wQQOyOblIdI-EvXF3AADX2touQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba3f4a10bd.mp4?token=sjXBaeo-P_Hnmrb8DVMfVppZ4VgPwUF8wnYAI7ZOeiJqJX0Z-FtyDKELZEDsbn8YSJmVSTP0NmIe2Wv7rtOG6n1f4N9ddsvYLG_wTsEZJqJiXfd_MZkkfSVl7L8Vk7XcVxwX7au7rOb5JpuJ5P3UZA85YmmZ7PKjE2LXMKV5mE_gFn4yXa9ZJSMWe1_EUTVlh2jhwFuqj914sBoQWBBWR-eCiKJUG3cl2LbwWigo0j4Xtdvfkc5T8zHQNomZyz8wL7wh0xnZRF4XNPkA0xfiyHnrs1TYIdfUxfFP_miD650l6yIG4GfqBod3lbl6wQQOyOblIdI-EvXF3AADX2touQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام اعضای مجمع شهرداران آسیایی به شهدای میناب
🔹
شرکت‌کنندگان نشست تخصصی مجمع شهرداران آسیایی در سیزدهمین اجلاس جهانی شهری به احترام شهدای میناب یک دقیقه سکوت کردند.
🔹
همچنین دبیرکل مجمع شهرداران آسیایی در این مراسم عضویت افتخاری این سازمان را به نمایندهٔ شهرداری میناب اهدا کرد.
🔹
دبیرکل سازمان متروپلیس، دبیرکل بخش خاورمیانه و غرب آسیای سازمان شهرها و دولت‌های محلی متحد از حاضرین این نشست بودند.
@Farsna</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/farsna/437224" target="_blank">📅 16:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437223">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5b1b1014c.mp4?token=akjJZ_PJh1zpBJyTNcyebC6kJVNQhFUAIgRHoYodQd_rwlrqGocCw7TTYWl--E5695U8KNwCvNbOu3yDG07Z9SE9okEp4gnBq4fu1AEYLSHgs_g9ss6GKzdNxQuYYFdBBr9erEvMZrwVqDaDSdeHNSFIQ9m0PEkgNchsJUpXLKQ5Q1rbJtpWvgPNcdr7nXRSfz5qcTFq06TdlY4gsZWHSlKUfk3mMHLrcIIJrdXQ44ZZhNgEu1H4Fj8D-WQ86cAtNrHqr-UTZOkNhf1wUS6TxH7bzNhwFd56392LEKH6tMrlyWN5J8VBYHeH4c_cU-E4XrLxpeOwIgFfTjxsoPUVgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5b1b1014c.mp4?token=akjJZ_PJh1zpBJyTNcyebC6kJVNQhFUAIgRHoYodQd_rwlrqGocCw7TTYWl--E5695U8KNwCvNbOu3yDG07Z9SE9okEp4gnBq4fu1AEYLSHgs_g9ss6GKzdNxQuYYFdBBr9erEvMZrwVqDaDSdeHNSFIQ9m0PEkgNchsJUpXLKQ5Q1rbJtpWvgPNcdr7nXRSfz5qcTFq06TdlY4gsZWHSlKUfk3mMHLrcIIJrdXQ44ZZhNgEu1H4Fj8D-WQ86cAtNrHqr-UTZOkNhf1wUS6TxH7bzNhwFd56392LEKH6tMrlyWN5J8VBYHeH4c_cU-E4XrLxpeOwIgFfTjxsoPUVgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تانک رژیم صهیونیستی در چنگ پهپاد حزب‌الله قرار گرفت
@Farsna</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/farsna/437223" target="_blank">📅 16:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437222">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">زخمی‌شدن نظامیان صهیونیست در حملات حزب‌الله
🔹
برخی منابع صهیونیستی اذعان کردند در جریان حملهٔ پهپادی حزب‌الله به پادگان برانیت (مقر فرماندهی لشکر ۹۱)، چند نظامی صهیونیست زخمی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/farsna/437222" target="_blank">📅 16:07 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437221">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/735faee829.mp4?token=JAJTGeh9UMYpHEgM74JtFbk06AtoMLtkF2AnaDIVREhbwQhoUrWyT_9DRWrItBsh3uIpMYeUeNQtaP_-9fCTOw2I2CeZZGrLSTUK6k9fMIQosY9retL8jQ6GbISEFxH0OdxwoQHi0gJ9Wt-3tqfAY6SywLYrAO6EDGMOl2Bm-Y0O6MWKOpyXWOPA3YK9NxdT9ktvBRxvlf0PiGV58E6t9ONXzJWyXTpFLVsFGA9g8uBdWVLLnVmeTEEovt7QuThvjnm5ZgACiy3PN3snrdacmQJTH0XLNm2ry-b45offuNDi-9Sim14ju46S1ikxEiFxlYoITqbSYxZ9aGYke988xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/735faee829.mp4?token=JAJTGeh9UMYpHEgM74JtFbk06AtoMLtkF2AnaDIVREhbwQhoUrWyT_9DRWrItBsh3uIpMYeUeNQtaP_-9fCTOw2I2CeZZGrLSTUK6k9fMIQosY9retL8jQ6GbISEFxH0OdxwoQHi0gJ9Wt-3tqfAY6SywLYrAO6EDGMOl2Bm-Y0O6MWKOpyXWOPA3YK9NxdT9ktvBRxvlf0PiGV58E6t9ONXzJWyXTpFLVsFGA9g8uBdWVLLnVmeTEEovt7QuThvjnm5ZgACiy3PN3snrdacmQJTH0XLNm2ry-b45offuNDi-9Sim14ju46S1ikxEiFxlYoITqbSYxZ9aGYke988xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درخواست رئیس‌جمهور برای بازنگری مصوبهٔ کنکوری شورای عالی انقلاب فرهنگی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/farsna/437221" target="_blank">📅 16:02 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437220">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eB1QoW22UwLBV0f6ivfN0JBe5FiYWjWgF6H5-FasqyjRNwl5Og9jMS3l-JMpPqxW5y6XSaTfD8AymljHmAIZ4s__GcO-jBCJhFABIhEldkVQ8Ri5VkXUGPicacQ8I8ol_vdLuboIqs5UUvkvy8fxKFb430xfu1rFmsVbmQpo00qrbBltaoFPtupjCUWueovWoLyufRCKuo6-udGLDSTKeG3KRUXmuZIrV1n1fxuX8yC_tFFXVcnIztgwN8ehKd2gWUYBhdhsZYQHuqN1qA9VdjXTHVkLLbS1W6VIH8ngvSUZJxJDmk2xYZ7EANrXI2825jjgTP9GmTwhjR5MPJJMxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه العربیه گزارش کرد که فرمانده ارتش پاکستان راهی تهران شده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/farsna/437220" target="_blank">📅 15:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437219">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
حزب‌الله: موضع توپخانه‌اى ارتش دشمن اسرائيلى در شهر العديسه را هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/farsna/437219" target="_blank">📅 15:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437218">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/490dbb67c4.mp4?token=Md2hYr9r5jrtyg5XosBiQ0JppLjbXhELweifNYDHd4Y5UI-6JwmsTXRMEZA0fgJXw5VCJ6BlPs1iJsg12UTrjXIPuznnDo1UT3pGq_kLaollQ245oIalOMZ94G4iSc8bDz7XMC9FlLDpMdQtp0KP-3vbvQBF1A1z1y3qnxhMiNd5zGMrjudbUHa9fyHUkCr2GR8rjP1TAeMM-83NOKkeOyRQxN10gQj9z9dJvR5B9EVfoAMPaTRMnf312jd8jSVt1EUcoukPZEHaNOfuG5BERfPabuO9ma2ZMgKep9kUzY70Qm7m6HWgjigZiBylO7UAbZd16TKupYgTRc-9YD08sIKLlHKBx1oq-64qx4uGaasb65Kn_pO_MhCMWf3elVYpb0ODRfH1C-U-pfPyAOVM-gLBV8gxQidC-tKWH_4vSbpSo6a-WscDcTSEIGjMtmEGHh9nFh4wyFt1rfRtBNhHhN0iXzO60NoWxncowU_16u0zg7Tjb3_zjSIQbuzN3uLUZzI-2vRS6tNoZhPrVbVeZQs2ZwGSZSZEoZd-pbzMu8Fbuo8d9bTc8v-IkrvytNMqxEBCPyxV5FJWSlW2e1wfSql8YXjM3R0nYQ1nNWHnrSBnbJdVgYYY98EORAFweY_VMGWfZ1QI7lwf0BdKu-z8rEXvYV9q6OOAO4yurlxN2-4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/490dbb67c4.mp4?token=Md2hYr9r5jrtyg5XosBiQ0JppLjbXhELweifNYDHd4Y5UI-6JwmsTXRMEZA0fgJXw5VCJ6BlPs1iJsg12UTrjXIPuznnDo1UT3pGq_kLaollQ245oIalOMZ94G4iSc8bDz7XMC9FlLDpMdQtp0KP-3vbvQBF1A1z1y3qnxhMiNd5zGMrjudbUHa9fyHUkCr2GR8rjP1TAeMM-83NOKkeOyRQxN10gQj9z9dJvR5B9EVfoAMPaTRMnf312jd8jSVt1EUcoukPZEHaNOfuG5BERfPabuO9ma2ZMgKep9kUzY70Qm7m6HWgjigZiBylO7UAbZd16TKupYgTRc-9YD08sIKLlHKBx1oq-64qx4uGaasb65Kn_pO_MhCMWf3elVYpb0ODRfH1C-U-pfPyAOVM-gLBV8gxQidC-tKWH_4vSbpSo6a-WscDcTSEIGjMtmEGHh9nFh4wyFt1rfRtBNhHhN0iXzO60NoWxncowU_16u0zg7Tjb3_zjSIQbuzN3uLUZzI-2vRS6tNoZhPrVbVeZQs2ZwGSZSZEoZd-pbzMu8Fbuo8d9bTc8v-IkrvytNMqxEBCPyxV5FJWSlW2e1wfSql8YXjM3R0nYQ1nNWHnrSBnbJdVgYYY98EORAFweY_VMGWfZ1QI7lwf0BdKu-z8rEXvYV9q6OOAO4yurlxN2-4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت معاون اجرایی دولت شهید رئیسی از کار انقلابی شهید جمهور در صنعت نفت  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/farsna/437218" target="_blank">📅 15:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437217">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvtGM92SKLbi1vvP4SNme0PPZN70THYwGhEmtoL1_dC60IbgW2pUMHCUqSICq9RXuOsR77RcqpVrd-b2A1pGdLyGsolPvqKXb-_3ud8BsznWPdTBIJ6tX0qT14bYYwhsgX5OIge3tzXWCg5Hp83w66JoYr_GWlGZwDChce-NqE6ohAl-Xr7EukZ9rzEoztS2ZjSfYr7EmyL6ZNh7LNHiFdiBjoTsblJFQBPEtz1k-OgO4PHESdLusfLjsprZnoKNQRo1FQAwdBfj5Y6JSwRHZ5RDqtuKvLy3hdmu42Hzrs2bv7X96Ve4eECJMHj9zAZMtLiEX4XsFsABX-Y7Dbe21w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقایی سخنگوی هیئت مذاکره‌کننده شد
🔹
قالیباف، رئیس هیئت مذاکره‌کنندهٔ «میناب ۱۶۸»، اسماعیل بقایی را به‌عنوان سخنگوی این هیئت مذاکراتی منصوب کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/farsna/437217" target="_blank">📅 15:37 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437216">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🎥
دانشمند علوم سیاسی: عبور کشتی‌ها از تنگهٔ هرمز یعنی جامعهٔ بین‌المللی واقعیت تحمیلی ایران را پذیرفته است
🔹
بسبوس: ایران به همسایگانش ثابت کرد آمریکایی‌ها توان شکست‌دادن این کشور را ندارند؛ کشورهای حوزهٔ خلیج فارس با خود می‌گویند بهتر است با دشمنی که آمریکا نتوانسته شکستش دهد، تعامل کنیم.
🔹
ایران ۴۷ سال تحت تحریم بوده، اما انعطاف‌پذیری و هوشمندی بیشتری از آمریکایی‌ها نشان داده است.
@Farsna</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farsna/437216" target="_blank">📅 15:30 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437215">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kD7Ht0YvdoYqN9SVBbKKWnPr_UxjD7-ARsDzRL4AEqnu5U4fxFSdxrYFrKcTgzdBIk02fP2ZFHs19WYCyUjOEpHsZq1NWKWTzJm43a0IcLXr5ILeHnX5gAaf5ywaEgp2wuj3TkAc9LFDhJ1Pp--h-Uwn8y7Uaj2eYu-SLnHuYghcZjQgQZfcUD2J5mgByy7hryAixZxdAp6NRWrHRnNLDi3PZE7c9tA1NsLmW06F8qmPCy37zzENLnFPgUN5HzIKp34jODmqcqXCKHck_Eq5F2-9xJMAOzcOebgfJS4SBEll22CvsSM7vvX-INi4Dg342OxlhmeERI0nY2rH-1Zdog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار به کاهش قیمت مرغ چراغ سبز نشان داد
🔹
دبیر انجمن تولیدکنندگان جوجه یک‌روزه امروز از افزایش تولید مرغداری‌ها و کاهش قیمت مرغ در روزهای آتی خبر داد.
🔹
قیمت مرغ در روزهای اخیر با ۱۰۰ هزار تومان افزایش تا کیلویی ۴۶۰ هزارتومان بالا آمده اما اتحادیه‌های تولید از افزایش جوجه‌ریزی در ماه اردیبهشت و کاهش قیمت در روزهای آینده خبر می‌دهند.
🔹
درحالی‌که جوجه‌ریزی در اسفند زیر ۱۰۰ میلیون قطعه بوده، در فروردین ۱۰۶ میلیون قطعه و اردیبهشت ۱۲۰ میلیون قطعه شده و پیش‌بینی شده در خرداد ۱۳۰ میلیون قطعه برسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/farsna/437215" target="_blank">📅 15:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437214">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPv4TnBhvw0mh48S6kEEDHO8K8mFwQdZ8UqnGpQ46ep5QvQyW4bIJHNATogRXgPU3tfOcEjJbafNuUzPN_2jPWM7yJgfBF6_h2t2tiYpFHoYkUCeLClwNWAVLi3lfObJPcsviSedFX2zDMwyyU1ZIQHqIqZfH4qCvmlvphgmmiuSss0FPlIagIe3Avm1Why63rugXhDZojRQNBjWZgUYJlhr9_Rxax95ZQ9HwMCIZYTkeMFGiDOcfjVVDc1BepgTUs8JQiiaYSu05R1yX-HYB-Ic_yyXTWT9nS4q47C189fVaQ4vSItsg0mLdkN8gFdqx5zEYF15p62_kKaXksdcyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ علیه ایران میزبانی یک جام جهانی را از عربستان گرفت
🔹
میزبانی عربستان برای سومین سال متوالی در جام جهانی ورزش‌های الکترونیکی طبق گزارش امروز نشریهٔ اکیپ فرانسه به‌دلیل جنگ در خاورمیانه لغو شد و این میزبانی به فرانسه داده شد.
🔹
این مسابقات ورزشی الکترونیکی در ۲ سال گذشته به میزبانی ریاض برگزار شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/farsna/437214" target="_blank">📅 15:01 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437213">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJDD1HAGCPwpM2B4wJ7SW-h6ND5wWh35TxPotJDaKtPhetcXtA42ATyg6fD5z4VU4MmHYmkcLEbuFppGfZVFNBlGDlPzS4BOVYxPQ5NppydsT2m-lzzj7vsIIq-JygXgnfOV9bk318YAeV1Gusj800sKEMCrLOBgSPS9W16-R1yEH1H1P1dyLZDm45GKDMWJI4dCamshj-HJcDw-ohwzjF0fNTfOAWvGTRpnQPZ3nyNBC2UPgvn32z9Qyt-XOd_9Kp3MtiKw952EteQjgOByyqxbJjFaFeznyusznSsbcR1Ij9sVA6tvC2NbIRPutYmpgO0EQ40As_Uoe9__FaDj4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه: حمله به ایران تجاوز نظامی آشکار علیه یک دولت مستقل بود
🔹
بقائی در واکنش به اظهارنظر اخیر رئیس‌جمهور آلمان که در یک مصاحبه پادکستی، با انتقاد از آمریکا به دلیل خروج از برجام در سال ۲۰۱۸ و متعاقبا توسل به زور علیه ایران، تجاوز نظامی آنها را «جنگ غیرضروری» نام نهاده است: آقای رئیس‌جمهور، درست است که بحران کنونی که منطقه ما و جهان با آن مواجه است در اصل به خروج یکجانبه غیرقانونی و خودسرانه آمریکا از برجام برمی‌گردد.
🔹
درست است که این جنگ تحمیلی می‌بایست و می‌شد که شعله‌ور نشود؛ با وجود این، در منشور سازمان ملل متحد هیچ مفهومی با عنوان «جنگ ضروری» وجود ندارد که دولت‌ها را صرفا بر مبنای هوا و هوس متجاوزان مجاز به توسل به زور علیه یک کشور صاحب حاکمیت کند.
🔹
ماهیت مجرمانه حملات آمریکایی و اسرائیلی علیه ایران را نباید صرفا در حد «جنگ غیرضروری» تقلیل داد یا قاب‌بندی کرد.
🔹
حملات آمریکا و رژیم صهیونیستی علیه ایران، نقض فاحش بند ۴ ماده ۲ منشور سازمان ملل و یک تجاوز نظامی آشکار علیه یک دولت مستقل بود.
🔹
هر کشوری که برای حاکمیت قانون و اصول منشور ملل متحد ارزش قائل است باید این تجاوز نظامی را صراحتاً محکوم کند و خواستار مواخذه متجاوزان شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/farsna/437213" target="_blank">📅 14:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437212">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خنثی‌سازی مهمات عمل‌نکرده در بندرعباس
🔹
سپاه هرمزگان: عملیات خنثی‌سازی مهمات عمل‌نکردۀ جنگ رمضان فردا شنبه از صبح تا عصر در بندرعباس انجام می‌شود؛ مردم نگران صدای ناشی از این انفجارها نباشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/farsna/437212" target="_blank">📅 14:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437211">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a424005de3.mp4?token=lp4jVXSIxMWVii0Jqa1TgTepfp6EF3NK5gDJ5lenrYRO4MI3v38mJG8gRgcoGT_KRSHFhryTdM5SvgYGUYINZV16JZdqiabEG7kEn4mBNZFRqk78IowWjFRiZ_uBgP6S71YO1BPr_dT67JAdtLXvVIXC4h5dE96vbN0BjDFzDXgs9w4t6cB2eREMjcfBCTjJMF_WmMU16lhaIZNPAeT5tkVxIMo56opaT-hFc03lQbzmRR1xj61JWuK_fgFL07nMprfZVSaWWbuYhzpRbUzek012q08rS8gTX1cIM7PuFfWQLOrTufL_P-UPsoqXnaOl1v3EaMmp0Hj18eksY0BX4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a424005de3.mp4?token=lp4jVXSIxMWVii0Jqa1TgTepfp6EF3NK5gDJ5lenrYRO4MI3v38mJG8gRgcoGT_KRSHFhryTdM5SvgYGUYINZV16JZdqiabEG7kEn4mBNZFRqk78IowWjFRiZ_uBgP6S71YO1BPr_dT67JAdtLXvVIXC4h5dE96vbN0BjDFzDXgs9w4t6cB2eREMjcfBCTjJMF_WmMU16lhaIZNPAeT5tkVxIMo56opaT-hFc03lQbzmRR1xj61JWuK_fgFL07nMprfZVSaWWbuYhzpRbUzek012q08rS8gTX1cIM7PuFfWQLOrTufL_P-UPsoqXnaOl1v3EaMmp0Hj18eksY0BX4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تست شوکر برقی شهردار پرو روی مشاورش!
🔹
کارلوس بروس، شهردار یکی از مناطق پرو، ظاهراً تصمیم گرفته است شوکرهای جدید پلیس را شخصاً آزمایش کند و در جریان این نمایش، به‌طور اتفاقی مشاور خود را دچار برق‌گرفتگی کرده است.
🔹
شهردار مدعی شده است که این آزمایش «کاملاً داوطلبانه» بوده است.
@Farsna</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/farsna/437211" target="_blank">📅 14:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437210">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8b42ad1d0.mp4?token=PkbcFrjlO52Nq4ihvXgxp8Turyg1ZQN0w8xkZ_rr1Bv-ULWvk2Zg2WTzroG2oQu8yOgn3Llkk441guvlxMirOl2yzlFdY4kfrkd5LVLZGjSCSBEL3YosJ6j56kO4yXYh2azkYP7XqhtNfWcOlMmDC-YEe4kIlCP9JJHvNXNcdfls77i6Vcxbj6kwpoNgJh2pOZyxAliM-gKxFnBNqZL4luBgyeKvC_9T7gYV7o7GQnPQZXVGtXyPBIxaZWYKFTuW-wwwMzX8zoI5rLrHDPySWk3hJzFNvIGEnUTHhQbSOVCw7mJLqLZ-Cn_HKlLUELCOLQtENxzJn-3HBq9fV9e9dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8b42ad1d0.mp4?token=PkbcFrjlO52Nq4ihvXgxp8Turyg1ZQN0w8xkZ_rr1Bv-ULWvk2Zg2WTzroG2oQu8yOgn3Llkk441guvlxMirOl2yzlFdY4kfrkd5LVLZGjSCSBEL3YosJ6j56kO4yXYh2azkYP7XqhtNfWcOlMmDC-YEe4kIlCP9JJHvNXNcdfls77i6Vcxbj6kwpoNgJh2pOZyxAliM-gKxFnBNqZL4luBgyeKvC_9T7gYV7o7GQnPQZXVGtXyPBIxaZWYKFTuW-wwwMzX8zoI5rLrHDPySWk3hJzFNvIGEnUTHhQbSOVCw7mJLqLZ-Cn_HKlLUELCOLQtENxzJn-3HBq9fV9e9dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اطلاعات آمریکا: ایران به‌سرعت در حال بازسازی توان نظامی‌‌اش است
🔹
به گزارش سی‌ان‌ان،‌ ارزیابی‌های اطلاعاتی آمریکا نشان می‌دهد که ایران سریع‌تر از انتظارات در حال بازسازی پایگاه صنعتی نظامی خود است و تولید پهپادها را از سر گرفته است.
🔹
«ایران در طول آتش‌بس…</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/farsna/437210" target="_blank">📅 14:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437209">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHOh5LKtUtYIPWsJaWoMXWbhIZDzbgDZpuTz52CrtggSjTiBy4L7pJiBh8NcfVanFtuEzTyIUP7v79Y-4iuAxZmRjvBYdgeYYmgFyehstZnRk2io85cGIjHv43oKM_Uw_QC8_Xq-fSb7xXzJLTBIf1nFa6DJBWvbyuADzxYsK7_RLs2mItWM3dU-1AdB5y7-ba06C1msMu0zYWkj8pYd_8KTBnvTrNALKfP7tOKxEwsSbpc3GVs35d3FytQLB-ik9OhpVb_qZ6ZftgS8qteNQn-XrHbHXDSgaB768WSeEYDWr3YRdbTvHVeRK8Ny5iHlbN85ivlK59KSsYe9nZ5Iaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ: پوتین در فکر پایان جنگ اوکراین تا انتهای سال است
🔹
پوتین می‌خواهد جنگ را تا انتهای ۲۰۲۶ پایان دهد؛ اما فقط با شرایطی که بتواند به‌عنوان پیروزی به مردم روسیه ارائه دهد.
🔹
بر این اساس، از جمله این شرایط می‌توان به تصرف کامل منطقهٔ «دونباس» و یک توافق امنیتی گسترده با اروپا اشاره کرد که عملاً «دستاوردهای ارضی» روسیه را به رسمیت می‌شناسد.
🔹
اوکراین و متحدانش به‌طور فزاینده‌ای مطمئن هستند که تهاجم روسیه درحال اتمام است؛ زیرا کی‌یف خط مقدم را تثبیت کرده و تهاجم بهاری مسکو را متوقف می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/farsna/437209" target="_blank">📅 14:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437208">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LS4B6WCqmS8web5uxPbelqCpQddz4JtGP4wS5BhbGrCJA9do6kEL8w3kPACLsG5Xd4uBieAvaSX75Sx-im04-o8Fy5oKmx8PmsTCPKPSEaIFd8LWZI4lrlEKd-q3NK23qvFFk2aY_RP154Xdz_G4vS3YGeu80ZmoRFhrQ0RXF-NT4WILH0JDHqhWVL0cnkE-T_TudIFkWlLapWSqH7-R6gf2lQUZ2119S7yROGDWzR8hI6bQN8qdLD8-ioqcaK8L_I04mdaFNcclgGJuy3b4pJqp_3pG5aI0_Oifb_TPzzTSVkuUEokw9gk5uuXsldIqH5IqVBQgN-XXc4U7hK-bHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گواردیولا از سیتی رفت
🔸
باشگاه منچسترسیتی، پس از ۱۰ سال جدایی گواردیولا را از این تیم اعلام کرد.
@Farsna</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/437208" target="_blank">📅 14:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437207">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029e0d7a1d.mp4?token=NGw-xxLoJaiQUtQCEu1BDz4ufcQm1CSEqL1oWaBYor1GcIKk_POOp3uRqY5nFLcWB8YcraPnFRgfCaaPE_V02RYhaTrvsaqLuiT96Gu43t-eTEUqqgos0ECROiw-bDfLvZOWeotfKnT2A0kyKXHh6VKbOl-R_hnefnDohuukO_Y66wDBNxtYiRQdSXWAJZ27P09Kn1Wm6KmUPE4qMJI5V2JVxx82C3R4AY9Jhei8O_FHAa8XuZl88ez681Vh0yGDQ6ySMGcsy7NSdvTFUjIdaiNM7IB8KPqBaNVHjqDfbjyx25PRUa6SIu1AelOr-ykrCmHZeAyHTnAUwkiK0EY0DYj9Ni6KCkNpMuI51AstNMm2nji45UakI1RG6-rBD6qmoLKEj2Uex_bzFrdZn535TUaysCscmAQyY1qx7TofEJhyL0eqViFP35dO3wQ_PUGf12AeYVm-S9DM48FUO2FrdPBVTHg0RbVmqSa3X3zDEw8tDxhAkqFhMibJjeZRRo9S6noLT6UH57ssJ39X5NwFWQntcBqag3LAN1dMJ6FmRW9n6tbUJOvuVWWIurXSU092n7aQbkre0aoOxETVYbM5GDUbSQGEXc65vQAZ_DQdfGSYSfQorrmh9bqFhyYGexq-X9dtgYyQk_kFPcia2gt9PstcOHBCinub3lQHYBCVDkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029e0d7a1d.mp4?token=NGw-xxLoJaiQUtQCEu1BDz4ufcQm1CSEqL1oWaBYor1GcIKk_POOp3uRqY5nFLcWB8YcraPnFRgfCaaPE_V02RYhaTrvsaqLuiT96Gu43t-eTEUqqgos0ECROiw-bDfLvZOWeotfKnT2A0kyKXHh6VKbOl-R_hnefnDohuukO_Y66wDBNxtYiRQdSXWAJZ27P09Kn1Wm6KmUPE4qMJI5V2JVxx82C3R4AY9Jhei8O_FHAa8XuZl88ez681Vh0yGDQ6ySMGcsy7NSdvTFUjIdaiNM7IB8KPqBaNVHjqDfbjyx25PRUa6SIu1AelOr-ykrCmHZeAyHTnAUwkiK0EY0DYj9Ni6KCkNpMuI51AstNMm2nji45UakI1RG6-rBD6qmoLKEj2Uex_bzFrdZn535TUaysCscmAQyY1qx7TofEJhyL0eqViFP35dO3wQ_PUGf12AeYVm-S9DM48FUO2FrdPBVTHg0RbVmqSa3X3zDEw8tDxhAkqFhMibJjeZRRo9S6noLT6UH57ssJ39X5NwFWQntcBqag3LAN1dMJ6FmRW9n6tbUJOvuVWWIurXSU092n7aQbkre0aoOxETVYbM5GDUbSQGEXc65vQAZ_DQdfGSYSfQorrmh9bqFhyYGexq-X9dtgYyQk_kFPcia2gt9PstcOHBCinub3lQHYBCVDkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از آخرین وضعیت تنگهٔ هرمز و کنترل آن توسط ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/farsna/437207" target="_blank">📅 14:02 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437206">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIRjB92-2Fp8RoDmm_QN0U9TumI01uVRSr1RHfe8TIj5UfrZy4aoTE1kLphPFlKhQxtFRztChOqRcVTvwFwlTx9EN10YIyMt9LdQGlmmiESt2hyWBDBrqrLLpOsPfie16YwgXSAHrGyoiyg5gF4l0rG7IuftiKs5qPZbyQqOMB9DmY_ZtuLsUkJTVZNuo0n_4nbRB_ImyRL5B026qttHLr3LEZSYGv21M_CVpJ3iyB97rFJcRZvVusrsABF2R3w6EPZ4kpDQvXiYEJZFMFaHUIGx_9M6U1nlsmlX5dQeYQxzB-9qDKNi-xeOHI4-VmORz-zRV2A82iBhiiOaDfQBAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امام جمعه موقت تهران: دشمنان در صورت خطا، موشک‌های جدیدی را تجربه خواهند کرد
🔹
علی‌اکبری در خطبهٔ نماز جمعه: نیروهای مسلح آماده‌تر از همیشه هستند؛ دشمنان در صورت خطا، موشک‌های جدیدی تجربه خواهند کرد.
🔹
آن‌ها در صورت خطا، جنگ فرامنطقه‌ای را تجربه خواهند کرد و به جای محدودکردن تنگهٔ هرمز، باب‌المندب نیز بسته خواهد شد.
🔹
اگر زیرساخت‌های ما را هدف قرار دهند، از تمام حامیان دشمن در منطقه زیرساخت‌زدایی خواهد شد.
🔹
پروندهٔ انتقام شهدا باز است و مطالبهٔ غرامت و شروط رهبری قاطعانه پیگیری می‌شود.
🔹
دستگاه حکمرانی کشور اولین مسئول در زمینهٔ صرفه‌جویی است و رفتار، شیوه‌ها و برنامه‌ها در تمام نهادها و دستگاه‌های دولتی باید اصلاح شود.
🔹
در شرایط فعلی هرگونه تفرقه‌افکنی خیانت به خون شهداست.
@Farsna
-
link</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/farsna/437206" target="_blank">📅 13:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437205">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdxOpQOIlzCkl7rpazGgEDBU9-I4-uf5OGn5qm23r363x2pTJLxlZQiE7BKeYxjr1gj4SOHY3YfRcKBtC1W0vAvDMicMHu52bOmfUTpK6fkI5tJomkVwypuC8w9sX0aGH6rjiipZaDgsQltvRsE_QllpqdOKmP67z_OYNsDAq1lfT7JfjSiqtz46dfMbim9raEx07Nv0klKaJHX3J2Y8jTwWtLZtdX_k3vGGqw8yyOiviie3l2QoacZcPeQTY4VEdLwLIq71gYY96uXxypHVFA4enLHzG0CHhUej0ojcny3_tq87mk3dvzbgbCxNnitLuvqu7_BMjjMuicPNOoZbrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسارت یک میلیارد دلاری ایران به ناوگان پهپادی MQ-9 آمریکا
🔹
درحالی‌که دونالد ترامپ مدعی است که توان نظامی ایران را «به صورت ۱۰۰ درصد» از بین برده است، رسانه‌های غربی از خسارت دست‌کم ۱ میلیارد دلاری ایران به آمریکا با نابودی شمار زیادی از پهپادهای MQ-9 ریپر خبر داده‌اند.
🔹
به گزارش بلومبرگ، ایران با ساقط کردن بیش از ۲۴ فروند پهپاد MQ-9 ریپر در طول درگیری‌ها با آمریکا، ۲۰ درصد از ذخایر این پهپادها را نابود کرده است؛ این درحالی‌ست که جایگزینی این تجهیزات نظامی کار دشوار است.
🔹
بلومبرگ همچنین به نقل از منابع آگاه گزارش داده که تعداد پهپادهای ساقط‌شده حتی تا ۳۰ فروند هم تخمین زده شده است.
🔹
تولید هر یک از پهپادهای ریپر حدود ۳۰ میلیون دلار هزینه روی دست آمریکا گذاشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farsna/437205" target="_blank">📅 13:41 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437204">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJSdb3UQBMsthw4-0l4Qb_IjW1ZotvBtOVyL2tAFlYGOY20wRcZZp_kYdLwc6kuaLwnIojzB3zL9tW94m-Pn4_GaxomM9ob09lpc3j7vAQ1DEoU0L0c_CVbFrDYrOq5qSsoPuFvWZK45qT4NvlFl4PkKI62NIEIbRQTePawU1Lqo7uIaW7mVWxoEB16r9ZeRqaBwETBp-IfgKCnGx0lq6zKfO8Yo-5yMrWMK8_zXm-NT8U3gMQW7suujqpJvJrApW2tj7eC_RS1n0hZd_rp8Mm31pFk2rQLXZdn3XBSgT93d37uTwUHUtl6Ud3v2i0Dk917cw1R58zC4C0qaIN0D0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرین سلیمی: خوشحالم با مدال طلا لبخند روی لب مردم ایران آمد
🔹
سلیمی پس از کسب طلای قهرمانی تکواندوی آسیا در گفت‌وگو با فارس: خدا را شکر در قهرمانی آسیا با کسب مدال طلا توانستم در این شرایط، لبخندی روی لب‌های مردم کشورمان بیاورم.
🔹
در قهرمانی آسیا همیشه کشورهای صاحب‌ سبک با تمام قوا حاضر می‌شوند.
🔹
ما در شرایط سخت و جنگی تمرین کردیم و هنوز هم ایرادهای زیادی وجود دارد تا به سطحی که در المپیک داشتم نزدیک شوم و حتی از آن هم فراتر بروم.
🔹
خیلی از تکواندوکاران خارجی ما را دلداری می‌دهند و حمایت می‌کنند. مدام دربارهٔ شرایط جنگی در منطقه از ما سوال می‌پرسند و اکثرشان نگران مردم ایران هستند.
🔹
به هر حال با اتحاد می‌توانیم این مسیر را ادامه دهیم و این سختی‌ها را پشت سر بگذاریم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farsna/437204" target="_blank">📅 13:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437201">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac353f693c.mp4?token=TZLysGzp1fMaSnMjlt0DuMJFgS5gD5Te0xcOXsTMxHMYSN6SYFtplFFhxsoW1jziZJUVPjUKfs4JWXV3-WSWF06uLytecJ3GdjAY6miC7i6M0axX8Y4ylYEQYdQoTd4NfTGL3oVPwRA3F3e4QU0YVeQK5zT9aSmqFB784Uj1ngEChKwQADTbcZbCX5eIAo1Mp1vmP4bwlNDN1tNjxhyo9F5syHOTpQ_uhXsfrFtyXJpOm_J8TTv1LCLq94ByTX4mEdeRt69-d3ZyL_35bVlhyoCfxacDmOUqBzhjuHmVenr114sUmDwrqTxEiSoB2CBCyhq6iGlr4G0TpCXxygHCIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac353f693c.mp4?token=TZLysGzp1fMaSnMjlt0DuMJFgS5gD5Te0xcOXsTMxHMYSN6SYFtplFFhxsoW1jziZJUVPjUKfs4JWXV3-WSWF06uLytecJ3GdjAY6miC7i6M0axX8Y4ylYEQYdQoTd4NfTGL3oVPwRA3F3e4QU0YVeQK5zT9aSmqFB784Uj1ngEChKwQADTbcZbCX5eIAo1Mp1vmP4bwlNDN1tNjxhyo9F5syHOTpQ_uhXsfrFtyXJpOm_J8TTv1LCLq94ByTX4mEdeRt69-d3ZyL_35bVlhyoCfxacDmOUqBzhjuHmVenr114sUmDwrqTxEiSoB2CBCyhq6iGlr4G0TpCXxygHCIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ماهواره‌‌ای خسارات به پایگاه‌های اسرائیلی در حملات ایران را فاش کرد
🔹
طبق یک گزارش منتشر شده، تصاویر ماهواره‌ای از وارد آمدن خسارت عمده به چندین پایگاه رژیم صهیونیستی در نتیجه حملات ایران حکایت دارد.
🔹
بر اساس تصاویر ماهواره «سنتینل-۲» که شرکت «Soar» منتشر کرده، پایگاه هوایی «رامات داوید» در جنوب‌شرق شهر حیفا، در هنگام جنگ در دو نقطه هدف قرار گرفته است.
🔹
همچنین تصاویر، تغییر ناگهانی در نقشه توپوگرافی را در ماه مارس، در کنار یک ساختمان داخل پایگاه «۸۲۰۰» نزدیک شهر صفد نشان می‌دهد. به‌گفته تحلیل شرکت، این تغییر در سطح زمین می‌تواند نشان‌دهنده وقوع حمله به پایگاه در تاریخ میان ۵ تا ۱۰ مارس باشد.
🔗
شرح کامل این خبر را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/farsna/437201" target="_blank">📅 13:07 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437200">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">عبور ۳۵ کشتی با هماهنگی سپاه از تنگهٔ هرمز
🔹
نیروی دریایی سپاه: در شبانه‌روز گذشته ۳۵ کشتی اعم از نفتکش، کانتینربر و سایر کشتی های تجاری پس از کسب مجوز با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگهٔ هرمز عبور کردند.
@Farsna</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/farsna/437200" target="_blank">📅 12:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437199">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c96a6d7d38.mp4?token=ilhxxSOwXTRzvVa8NNF-_4NKxFe4jbFF8buiqe0ypRrNgYic73G_c7Q6XEtRLtCmeJ7ZFfBq-z7XoeD-jfItEukFB7HqVEC8bN7SMi3kYC7NjkW3kYe9PlPPhbYbZcli1q428_kqIzREbUIweJ5VF4l-gCaELWYKGR-2CC28S8h3ILs1xEN0hVFjYtI7frmIbVx1AdFoLHV03smY9SNrcRL_dFxv9HrgilNtLyGsMfbW99vufhMbOXRQa3PBIJsNR064ecHGVDdrmQ5LfhQWC7EWV08Ob7mPe-teJ4bPba714msshud07Dv9yP28MINUXVPLUzhIqwZmV-7Yf7JZHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c96a6d7d38.mp4?token=ilhxxSOwXTRzvVa8NNF-_4NKxFe4jbFF8buiqe0ypRrNgYic73G_c7Q6XEtRLtCmeJ7ZFfBq-z7XoeD-jfItEukFB7HqVEC8bN7SMi3kYC7NjkW3kYe9PlPPhbYbZcli1q428_kqIzREbUIweJ5VF4l-gCaELWYKGR-2CC28S8h3ILs1xEN0hVFjYtI7frmIbVx1AdFoLHV03smY9SNrcRL_dFxv9HrgilNtLyGsMfbW99vufhMbOXRQa3PBIJsNR064ecHGVDdrmQ5LfhQWC7EWV08Ob7mPe-teJ4bPba714msshud07Dv9yP28MINUXVPLUzhIqwZmV-7Yf7JZHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ پهپادی اوکراین به خوابگاه دانش‌آموزان در لوهانسک
🔹
حملهٔ پهپادی شبانهٔ اوکراین به یک خوابگاه دانش‌آموزی در منطقهٔ لوهانسک دست‌کم ۴ کشته و ۳۵ مجروح برجا گذاشت.
🔹
کمیسر حقوق بشر روسیه، گفت که ۸۶ نوجوان ۱۴ تا ۱۸ ساله در کالج استاروبیلسک دانشگاه تربیت معلم لوهانسک در خواب بودند که پهپادهای اوکراینی به آنجا حمله کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/farsna/437199" target="_blank">📅 12:44 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437198">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aec72b07f5.mp4?token=bSmoqXwvjBpGKlWwF9UWuHAsH55HFop8bbCYOYUS8AsgHJfwPiUs6yEBiduW249PtPM5dvH74AIMFLGID5riU_WsSdNdfJjbY-rbXq522f10It68OQu-cRsWS9yLoiKk7VMDiEHQqaBBQdqhEPiWR7ubOdZNU9J5gQFT06HOp4IoAiNVUIcp-c1Cww-uIbtjBMA2qq7hHbBRLJ0zKQXiAXwVYLlA-h-RhgxA93om4Xkaf1Jn_LWl8LOVdTdIcsH_SmVIO2HoEE3hK9GGOnUMGvVBXn5CVSiyhTCKVdf7vxKLH5wK9u-y5ixmCzvUiY-51-oQ59FznoYkZjg7Xqzj2nllYwePOYwyAxVKJZjfpmyhDEh-aHk-hDu3gN8n1XZ8LXjZeVLGdTU4KKwUoZuTcoI0ZKazi1VY33coF0hqbbJG04yuh8T6Z3NyC_20lN4YQ1SaCqJeS3Ch1JYQSfsMG2HPZVPhPqn1HFVUEyGE0cbV49IWkNYS1IpOFrPDoFh8ggRnJ5xYEUFCaIGrHvpkajGPDPsvSwLZR7UVmPhiPH9BG9aFUQokR_qQyv3e3Zy_aPXjB2mX1VtjLP5F78RFVPW0EQvyE6WpU-DSJcSYjkAFcyzonOBlqLUoWb8mEuhEpc0GH7fvJK3PNhKkUVSdJwxDVIXmudGQRUKQLcNDOlM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aec72b07f5.mp4?token=bSmoqXwvjBpGKlWwF9UWuHAsH55HFop8bbCYOYUS8AsgHJfwPiUs6yEBiduW249PtPM5dvH74AIMFLGID5riU_WsSdNdfJjbY-rbXq522f10It68OQu-cRsWS9yLoiKk7VMDiEHQqaBBQdqhEPiWR7ubOdZNU9J5gQFT06HOp4IoAiNVUIcp-c1Cww-uIbtjBMA2qq7hHbBRLJ0zKQXiAXwVYLlA-h-RhgxA93om4Xkaf1Jn_LWl8LOVdTdIcsH_SmVIO2HoEE3hK9GGOnUMGvVBXn5CVSiyhTCKVdf7vxKLH5wK9u-y5ixmCzvUiY-51-oQ59FznoYkZjg7Xqzj2nllYwePOYwyAxVKJZjfpmyhDEh-aHk-hDu3gN8n1XZ8LXjZeVLGdTU4KKwUoZuTcoI0ZKazi1VY33coF0hqbbJG04yuh8T6Z3NyC_20lN4YQ1SaCqJeS3Ch1JYQSfsMG2HPZVPhPqn1HFVUEyGE0cbV49IWkNYS1IpOFrPDoFh8ggRnJ5xYEUFCaIGrHvpkajGPDPsvSwLZR7UVmPhiPH9BG9aFUQokR_qQyv3e3Zy_aPXjB2mX1VtjLP5F78RFVPW0EQvyE6WpU-DSJcSYjkAFcyzonOBlqLUoWb8mEuhEpc0GH7fvJK3PNhKkUVSdJwxDVIXmudGQRUKQLcNDOlM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رزمایش ۱۰۰۰ موتورسوار جان‌فدا در تهران برگزار شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/farsna/437198" target="_blank">📅 12:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437196">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6vaJeCXoGEkXzjOU-n9tv1itYtbs1VZIZG-cyYMynLoc50ubxe5cmNf4kG3HF6Q_7_BZK5uOe1n-zkmXj7Rs9ub3pPhtHT3gTFpx9smjPvkdQNNxVAngKjJiAg-1AcQi8X-eOig5GG1FovmdOFG-JMKqkj9y0HiOxPQQ_4hGzhYCuyKeTy6FHPjRRjlNx27VdBOZxSrZD6dKZeCiToKXn2DRPcEi7YBR8MBlEB2oQ8bic4DhTNB_D3egCsdbpcoCyjkFsY5p9GsuzQ6EvQmdRIn7ggkQM5uEtWEHuY14zxBAgX9raZVdz8x5rViVSBrWktdp4dhrsLJfYonbqefmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YVQu71MJCPEOGWze0BSyv0DZJw_y7Lx_UYKqJdkYZhhzlh1QspwwboXp_Tha9yTuWNFDj2mH4Mk-9A15daNJyUBXSy_bmGB2QlJrTFyoX-ECjuz9CYHbS9a0_Xad2GudMk_f2LPEiS8cxXt26Y9mm0OeeCE_UoMDZ4sq9XGwcGV_iCKkx_ZlFId8yslO6Jq-VYpSaqsDOLXWbjro-U-HlkYNJwAy-AaOt8gv2Ks4ViXzJxUBTdv3dnJDU2tzAEu4BAFM8dWeDvkzK0RcCUza-Opn1JdKZ0V2ZrlNzn_4zH1hl1eqeQCxpd7-KX3z76b8EYRENlhVFE-iEsBi2P6g-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تعرفهٔ گوشی‌های بالای ۹۰۰ یورو به ۳۰ درصد رسید
🔹
براساس بخشنامهٔ ابلاغی گمرک، نرخ ارز مبنای محاسبهٔ ارزش گمرکی گوشی تلفن همراه برابر با متوسط نرخ ارز بهمن ۱۴۰۴ در مرکز مبادلهٔ تعیین شده و هر یورو ۱۵۵ هزار و ۱۹۶ تومان اعلام شده است.
🔹
همچنین نرخ جدید حقوق گمرکی واردات گوشی‌های ۶۰۰ تا ۹۰۰ یورویی ۱۵ درصد و گوشی‌های بالای ۹۰۰ یورو ۳۰ درصد تعیین شده است.
🔹
این بخشنامه تأکید می‌کند که واردات تلفن همراه از مسیر مسافری نیز تابع آیین‌نامهٔ اجرایی قانون گمرکی خواهد بود؛ همچنین واردات از مناطق آزاد تجاری-صنعتی نیز مشمول این مقررات است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/437196" target="_blank">📅 12:25 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437194">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nl-ERu1OpoBrNmjLgUatF2uOuScLqz0sKmQd5Q9R2AgfuDs-P3wTURftuwTuz0qba4VwD3lvRjflIysnxO3jv82RoHh5rkX8jDa4QTylrA3jtGL4Tl9q8C6-6hzSW-yt6nlfRUDi3mNBFv8WHO7dBTq-1EEoeoBP3ivKpcd6-2JQbDGreXyIQwA5J-TI3PEodiVDjwEwEMYPyrmxMM0jT_olDX-Q0ucYLoxG8FIOK8qNBYW6lMo5uBP0fgCW6-HzKKTXWuUX4RfBzryD-n_flzXbR-jp3v81yzZvhrxtWs4OlN_11DZ2QFAnvC0HVMo85ih1vJcVGYat7pw0ORNFCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SFDlrdduWakOEC1FCwjs-EJJMx2R-JkVu4ywJbKlzTXuKrYJ7gPd2OMP_yWuyoUPpAEkfaKqm2w0rGMw8OjpCT1ek3p-YmL1S0MSfXP5wNdh2_9Ji50omrbWJuamPjBdeGi7Nz7FxGgdm_X_xveJgknSVqw_7ODZFSxJM9VRhcnYnjR5phqTmryJT9VrwbJQXo0byyMag6_8tTLTWhAWJF2JYb9XQ-T1PKgCtni7cj7PKDkCu1MZXlFt3pySClH6Llazzug1pfYWfHihE6jfrVTkyZ_JXyqixhK4ctSbAalLJ_MVTZVlsLSQjE6fyeNW3sRY2s3pBNjNYlUa8EcTQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انفجار مهیب در بزرگترین مجتمع پتروشیمی مجارستان؛ دست‌کم یک کشته و چندین مجروح بدحال
🔹
وقوع یک انفجار بزرگ در پالایشگاه «الفین-۱» متعلق به گروه MOL در شهر تیسائویواروش، مجارستان را لرزاند. این حادثه حین راه‌اندازی مجدد تجهیزات پس از اتمام عملیات تعمیر و نگهداری رخ داد.
🔹
مقامات محلی اعلام کردند در این سانحه دست‌کم یک نفر جان خود را از دست داده و هفت نفر دیگر دچار سوختگی شدید شده‌اند. هم‌اکنون آتش‌سوزی گسترده‌ای همچنان در محل حادثه ادامه دارد و یک خط لوله آسیب‌دیده در حال شعله‌ور شدن است.
🔹
شرکت MOL از طریق خط لوله دروژبا به منابع نفت روسیه متصل است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/farsna/437194" target="_blank">📅 12:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437193">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">توقیف اموال ۷ نفر از خائنین به وطن در ایلام
🔹
رئیس‌کل دادگستری ایلام از شناسایی و توقیف اموال و دارایی‌های تعداد ۷ نفر از خائنین به وطن در یکی از شهرستان‌های استان به نفع حقوق عامه خبر داد.
🔹
اموال توقیف‌شده از متهمین شامل مسکن، خودرو، دارایی های بانکی و سایر اموال بوده است.
@Farsna</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/farsna/437193" target="_blank">📅 12:16 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437191">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WTcUefUUGIY0XWDWq1ajPfxg2C3bf1LSvTVyiAo8qSmPAST9kYEu-4PFrr1nuebZq5lI5nm6FM4WqrStmY8QSzk2uJq_BmTbSlpKCYoKkwIo-B7g16w6eJ936x-5WmeyDvX1Lt5LlU3-yoRUeo9iDgvb7eTYUlrGvAqj88VIcUZhQeaPiQgM3VvmIJgpOeixRTnMPKEMkZRod__g-hhP-TvAPkzk1NtcXzlrOgRbWfImceZep-z1hIITG_WIBXyldX5lujBx1LgYBz4mCGpbDSyTkwVprZWK8rn1hB1ZFYbrarmJf6dBF8UGXPABFe_chH3ylaNYwg3r9Dl1_vJVyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M07-e1UEy-eY6bhtok-x4lDYZuYf8YFxnrU4j_u9BGNl6XXMc52lXR8MQwoKVexirEXWJEiBNhyvP4RrB1h5NYqrH_K1LSydNBytdl5NITm6vdu0FGkM-LBaUbDGYIRf6jCqLAqfyY_hviXsRX4dfZ5E2rEvU1c-epfQDirXOS8PdVHdLtDYzIF2IN_km273TEgi4Ju3wn0smguUCG1sfmvk5VwgtK_Wbgg1j49vb7p-FyAaWlguSBnUfAHho210KtimS5vnz473KQMDTKABpqTs6w8NCmRbHszAR1GoiddDCqgM7sARnNHM4uw5v28r6Zd4RDai0lpdZzvyYQEKwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سلیمی در ثانیه پایانی طلایی شد
🥇
آرین سلیمی در فینال وزن  ۸۴+ کیلوگرم تکواندوی قهرمانی آسیا مقابل رقیب ازبکستانی برنده شد و طلا گرفت.
📊
نتیجه: راند اول: ۷-۷ برنده ازبکستان راند دوم: ۶-۳ برنده سلیمی راند سوم: ۱۲-۱۰ برنده سلیمی  @Sportfars</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farsna/437191" target="_blank">📅 12:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437190">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlUT7Go471RcsNK9YPqgKjU-lbGAD4YFRJnxEOUERra2XtYW7p-Lw-9cUGGThGjD_1tf_wwjiivmIKEg1_svvAHNvZDOIZfIQySyLbTllMaL-1396YxWc3BhfTgVbqzX4eHn7OmfrxIDEo2azKUvh4kvz2Yu9xsC1Om76BeMcWmHS3oHA9ZznliDAJKN4c-dnRitrPrUfPITPjA8Zm3ro94Jb0nTgH2Z19HOqeqnVWAyntWrVI2C9xMrKGyYL1aFc0e2nBlC40rK5sqB1jJXo-w8Hc4AWtHLSuMQEm2AB1WwxDHhsy63QHD1Wv-zN4U1B4F2LDLVbAzPUYSHYkQt5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشنگتن‌پست: بار اصلی دفاع از اسرائیل در جنگ بر دوش آمریکا بود
🔹
روزنامهٔ واشنگتن‌پست: طبق ارزیابی پنتاگون، آمریکا بخش زیادی از موجودی پیشرفته‌ترین رهگیرهای پدافند موشکی خود را در جریان جنگ ایران از دست داده و حتی بیشتر از اسرائیل برای دفاع از آن‌ها از این موشک‌های پدافندی استفاده کرده است.
🔹
به‌گفتهٔ ۳ مقام آمریکایی، این کاهش پدافند موشکی آمریکا در منطقه به خوبی نشان می‌دهد که آمریکا تا چه حدی بار دفاع از اسرائیل در برابر موشک‌های ایرانی را به دوش کشیده است.
🔸
آمریکا بیش از ۲۰۰ رهگیر سامانه تاد را در دفاع از رژیم صهیونیستی شلیک کرده که تقریباً نیمی از کل موجودی پنتاگون است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/farsna/437190" target="_blank">📅 11:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437189">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/083c1c9cb6.mp4?token=iyUk7DDqmG6UI7BqNzSbUVAwRwTUFtl72bt1iyLaUEUVEl6CZuMxomuowdcFrlvTw-yTLm6h4LbVNe5FTISnIufrB_Q3WdpdC5yBu8cOHh8l5oT_tiykOrVctlWx8mR1AaLFT_nb4r3Dq3TdBauZHRnYAqiM9-vFgLDO4tvbgXsB3fMv8ecLOZkkPgkon2QdyzFbqpcv06QITP9W09_awfgQWw_msCzkg4h5XmQ4QhfrUApp9Po_WyKLkzjiqHJ8D0-pvqNHMs-02vEuAGeMeD8D_6DR59RSlIeyvQuL2K2rq3J4uRCIU1P81-xZg-r_fAa5Uklzsxxbmcr6PEHbZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/083c1c9cb6.mp4?token=iyUk7DDqmG6UI7BqNzSbUVAwRwTUFtl72bt1iyLaUEUVEl6CZuMxomuowdcFrlvTw-yTLm6h4LbVNe5FTISnIufrB_Q3WdpdC5yBu8cOHh8l5oT_tiykOrVctlWx8mR1AaLFT_nb4r3Dq3TdBauZHRnYAqiM9-vFgLDO4tvbgXsB3fMv8ecLOZkkPgkon2QdyzFbqpcv06QITP9W09_awfgQWw_msCzkg4h5XmQ4QhfrUApp9Po_WyKLkzjiqHJ8D0-pvqNHMs-02vEuAGeMeD8D_6DR59RSlIeyvQuL2K2rq3J4uRCIU1P81-xZg-r_fAa5Uklzsxxbmcr6PEHbZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت معاون اجرایی دولت شهید رئیسی از کار انقلابی شهید جمهور در صنعت نفت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/437189" target="_blank">📅 11:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437182">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t0hfofSnZr-xPGW9R-1gx1sTpPLB3exTHP0LmyCDWAxEWjjBRCarJ-3XtWqtIOl7UyS0iLIEyXEq-ob63pn7bF9Rf0bcAmJP-5zklaOIERSrEez3q1UDzTt2J0lesq10A0KYOPfgNZEIR2xkb0nC2lm1vvRo_hY_UEkkIujlcPvdUbKAN5ocfL2JPGb01j8LXXiGS1vTbz1h9rq6eAFN4eQoNhw1NosnAyzprDBmy9dgpdYnbqtxHV8meSauEQR89upc1p57IACXQVAu0fOVr3MTDdbsnynhyp5QXPamR_k4yp0-fA7OO60xYycOObZjyYdSkLhxgUfE194V-qWXhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NdYMLzmec4mLnwdmCJk1t469Ruzc6vN9ZBuaF--5s7Pwk0tbyfaEzQEFPoGeCwVxASWkTmbgbZ9SYxSbr5cBlwFM99nyPvcNurtO9faw1uUhTZaJy_avXjzCs76_vI3ao7-fnwl_prQ8Vl05WyYik9xxZjK89WKomYsgjXtxRMRFEkdOm3Xnx1vc4j7NLWZ7pCLilsssLGGjxEXMzmcQxhu2hw8qnPDUxYiG1FZkCM_ElUeSrRrwHGX7leGhgX2uTeQRbqTWZhbnK9TcwWht9JqxYa4l4bRVw37KnZt3YTjgPJy1ZS18O2-c1mc22-pewnsGGdrR_GzQWN7c5IgvRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L-85k1yXms3lPX0B9kgaZ4kHDcTqdB5Mdo1w8DP3HulWD7RojEBNK_O-nlP5ajuodu7Mc-Y4k3irBvZ4pz70OJMHS8Aen7356_SEetFfxUc9WQJ_-6efPseX5euR50-klBDMKv8JvDuTGy18s6rA99HgRvFGZMOJH6hedzM8cpy-cO30GQnXkqu7ax9EEx4sWRLB1zRzNM2yRNTkX7Pnbsy0nfa7SyplwIWpaVU_iUqzZutJhorap1C1ccXtWbLy0zKC7CNSujxQfwMSYOB65z3ePVXBt4ZQCpDqXV9GVa6TcAJcKx_owpwvEEEYSBr4s8OtLonAVSSQ5wSwLF30Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MWuipNwza3Y2wXJwY6JXZIY5KJk-r3bXFJNjJcRYI0kx9RM3Ks3JRGuMXdSKD0la32ppLiozrfUATCWu9M8GczieEgmq0y_PX9-Q5B9RTUprAnhcEFKsac6W7T5E9CIRo37xJHvVLdDmD8cFt0xxjxNCjGw9kczKQnYPdirETCFIUUTFEXgxAxLM4E5QAWZeLTCdcLWj378AB9kabZ_bh8yZZSiyDBRCiMwP0AWcF36qG2mG5ChNK4CUc2HWYLsHg1UlcztRj2Yr_o_DaxcfM9hmeoNjmYP6fXe7nSHlbHh1TqK97WOC1ZMHRd3fKMAJFkdu7H1le79Cdv6bKGMr4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/diN8WdXwS2JiZbkJ8taFtxYz0oUmpLBjkn66om7jzpxr8LVZPJOKbYx5G68eYwXMDI2Tb4ZOFbOjU7d2q1PwsDCOLxEsQc8kFR8Lfwg7JOc_19kIP7Ojgta8y68Yg2Xuz7i03Oy6k3_GJgB1hJzYQ5ABNywRKCj4VXwT8KwcYp2xmayd-VXhZGOzsbvXwb9kFAstFlf6DOmtTE6Vffhpoz2oCg_6HmwtIUtmmqVoIuiThI9TXH0GRIKTIA6vO7X8fk0sq7ORh3bu-HC7Ixg4qF5IaLYfZPLbuJMO3hH5Jz6XN708s8kPsaP7Bzjz2YHMwYADJAq3OhDypKKg2cSnEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eVPvALvEV0xFG9iokO51YLgqjDxD2CVOlNrN7VZ291ss6A9LPqttcMp7aQhR1DGrzrUbop-65n4fEfDlCg_MSf9LS2PXBML9DMiBTPItnfXI8aT8CexlYBl7B5_E8MAZgxxOXUmxRwJ693_wqvyr1LmQU731uMFc85QJfHjCQz2HmGjuwbW-ObJKrlCAzV062QCAqUo7ePheeGJpzN-z9z855TzsNlYudPr6ZbdPd7DXa3UUOqQsWkdyA8AKEbDZjC7aUoBxD88YSY3mpYKTjluwR0i4yxTmkljFLU-gBTWuohDFIbF5FNE8wl-BhkiAX9kjfHRBbNa3BNg_-MJQFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YJw7Axk3QefKazMM9UTSRebeBYMgpARnFpsdpQ6Sjc4DBxummQIZPdxP85mRBYbafRbLW7pbBo42QYAB50u7qJ81N9B0cb6q0LoWiqMjptk5z-p6YyWA4dsaEJDqlnD4ONI_bBBinnmBVWehazQW6DZzBX_oU-AX-qvj9Y3rmtcxjBgRFK-n1z6yq8KyaFQr6nWaz6lWjRT8nkHolq6RbO5UgCDXnJnzmaDM6TvQSOJIy4WqRHlYniRLadE65LqYtYT3xW4KmkOuqQsjiTVKNN_S8ytbFsrSdF_RFqnGbaY9Fj5bbI4Lr8e99hqoPyic1DO3PdBCzHTZ4ypiJAc1Fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بدرقهٔ طولانی‌ترین کاروان پیادهٔ کربلا از مشهدالرضا
🔹
کاروان پیادهٔ انصارالحسین(ع) امروز حرکت معنوی خود را برای بیست‌وپنجمین سال متوالی از مشهد مقدس به‌سوی کربلای معلی آغاز کردند.
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/437182" target="_blank">📅 11:38 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437181">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">یک‌طرفه‌شدن جاده‌های هراز و کندوان
🔹
پلیس‌راه مازندران: برای ساعت‌ ۱۴ مسیر جنوب به شمال کندوان برای اجرای محدودیت یک‌طرفه مسدود می‌شود.
🔹
حدود ساعت ۱۷ از پل‌زنگوله و حدود ساعت ۱۸ از مرزن‌آباد به‌سمت جنوب یک‌طرفه خواهد شد؛ جادهٔ هراز نیز از صبح امروز یک‌طرفه شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/farsna/437181" target="_blank">📅 11:28 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437180">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خنثی‌سازی مهمات عمل‌نکرده در خرم‌آباد
🔹
سپاه لرستان: عملیات خنثی‌سازی مهمات عمل‌نکردۀ جنگ رمضان فردا از ساعت ۸ صبح تا عصر در خرم‌آباد انجام می‌شود؛ مردم نگران صدای ناشی از این انفجارها نباشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farsna/437180" target="_blank">📅 11:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437179">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace2e0f59f.mp4?token=iV-wB31Q0ZzWnzK14JwJjerXPzIQwo4vD-0NuY6d9MpQzijoRLHssMH9zMAzqOJSjKpOWq9iJmabofC9cr7R0j-hZCWQJwNorYuEkU8chs1misMcdB99ERgEB8llwu_iNCBYsp6ZYZrXwftT8micDxfOyY5DClITBmf3AR88101XJNWy1bLmpwm-xSgZlAk7waZ4lxK-d-7NGHPbqwc0zOiZSd2lPALqhYDWSETgpnKE0Zh2IgWh3I68s2JttYDpWIWwKz3JKM69XM4p3ufj6EWIfF3I7FPXpv6W34yzk-oRKzMr3cOym8h55pYcwuAslo_kaAu_9lPs8GbHDQJ7HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace2e0f59f.mp4?token=iV-wB31Q0ZzWnzK14JwJjerXPzIQwo4vD-0NuY6d9MpQzijoRLHssMH9zMAzqOJSjKpOWq9iJmabofC9cr7R0j-hZCWQJwNorYuEkU8chs1misMcdB99ERgEB8llwu_iNCBYsp6ZYZrXwftT8micDxfOyY5DClITBmf3AR88101XJNWy1bLmpwm-xSgZlAk7waZ4lxK-d-7NGHPbqwc0zOiZSd2lPALqhYDWSETgpnKE0Zh2IgWh3I68s2JttYDpWIWwKz3JKM69XM4p3ufj6EWIfF3I7FPXpv6W34yzk-oRKzMr3cOym8h55pYcwuAslo_kaAu_9lPs8GbHDQJ7HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گرینلندی‌ها علیه کنسولگری آمریکا به خیابان آمدند
🔹
همزمان با افتتاح رسمی کنسولگری جدید آمریکا در مرکز گرینلند، شهروندان این جزیره با تجمع در مقابل ساختمان این نمایندگی، مخالفت قاطع خود را با گسترش نفوذ واشنگتن فریاد زدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/farsna/437179" target="_blank">📅 11:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437178">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U40XGPQNInJE3SnSNdJ-uiv-kJaUZrdKunzo4Bql8_I7IS4ZhhTP7GOA6rPGeJ6wAZ_LjiPC7M1LO2dIpkelQFosVPYUr5AVqKxcERuyIRsnlYYBqEK5nBhK8A_Nub1HKU24dNZMqRE4QHbHCB6M5ywoGdnYlJPRlMQeobzEZhQODebsFJU7gmuBIVc0qye4kupjbqxZHfdvFDOJxEXUPKPTIsP-pcBLe7Nxqbrd5nQ1ZvEIUfhTPRwcPv5ewNihnBLZZItvC2tkQmvqbzVXnMBSUoAGdqqCT8q94V9x2CQMO9wTGLZ8vIhvlWkmo1kjOK4qzrfZA3qhDYQhq1ecYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حادثهٔ امنیتی برای یک نفتکش در نزدیکی یمن
🔹
سازمان عملیات دریایی انگلیس: یک نفتکش در ۱۸۱ کیلومتری شمال سقطری، تأیید می‌کند که یک قایق کوچک حامل ۵ نفر به آن نزدیک شده است.
🔹
تیم امنیتی مسلح نفتکش با شلیک گلوله‌های هشداردهنده، قایق را مجبور به تغییر مسیر کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/farsna/437178" target="_blank">📅 11:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437176">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7AbOh24uRz0zyuHWZ9jDU6jECdXD03O3zLVa-XYeYGiv7Ckt0ZshXE58GSL1jEoJe_WelqfYuslxREk6yZbNfJKlf85gMjAm6og3A4_BW0ku3bsyk435bhP4LVwhp3vWGVqDYTLlAW60A7AItMHUQDrIdtWn0PZDR0LgHywveZys_4XMr4OXqtTIYJvSygwhhXIeUpXRUhs5wHuKHhYLKSzkYowxHh14aGmdUKl72h4CXi1DiTb3_SeX0qyjswKPS9MptgRVnKvMdqtm_ec92gWc3xmV1mpS8QwQVsYJj4FZrBWr1WxCHZkWZ5Mt-VseU1X-gavK8-i9ixuiF4qcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسابقات جهانی کشتی به‌تعویق افتاد
🔹
اتحادیه جهانی کشتی: به‌دلیل درگیری‌های منطقهٔ غرب آسیا مسابقات جهانی بزرگسالان در زمان دیگری برگزار می‌شود؛ تاریخ جدید و میزبان در روزهای آینده اعلام خواهد شد.
📌
پیش از این، زمان برگزاری این مسابقات ۲ تا ۱۰ آبان در بحرین اعلام شده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/farsna/437176" target="_blank">📅 10:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437175">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfQ1pdr5BZ6xrxoDhW8ViJddrYFbz-zgViszIvbHnM8DdgUEeB6TRM-0FEIRNAy5gHji_BeO2FQCa-XYoLRUjiYfWGtDIGn0ZFLtIJDCCjq0ltrUCanvaLcaQnTFpME0in6psPYhu4MqZcfTnyFkrEyY4WXIC9jj4VTGIcwF3F_hJZ-hW_dPKm9mIVGrxYaZFJKyRBHt1TCvXTHOY3YDHMhGbatvY6d259bbuCzTj6YA8PskdjlXdLkbo1Gfofly0ef9GR6uzJRauIBv4tq8YoFRJcJfFMl4W5Bww_0vq25tFE36_a4B-lAH921rC7DNM4r06TnkBT1fxbQYzHN0rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات میزان تأثیر سوابق تحصیلی در کنکور ۱۴۰۵ اعلام شد
🔹
براساس گزارش سازمان سنجش تاثیر سوابق تحصیلی گروه‌های آزمایشی ریاضی و فنی، انسانی و تجربی در نظام سالی واحدی، میزان تأثیر پایهٔ یازدهم ۱۷ درصد، دیپلم ۳۲.۲۵ درصد و پیش‌دانشگاهی ۱۰.۷۵ درصد اعلام شده است.
🔹
در نظام ۶-۳-۳ نیز میزان تاثیر پایهٔ یازدهم ۱۷ درصد و پایهٔ دوازدهم ۴۳ درصد در نظر گرفته شده است.
🔹
همچنین برای گروه‌های آموزشی هنر و زبان‌های خارجی نیز در نظام سالی واحدی تاثیر پایهٔ یازدهم ۱۰ درصد، دیپلم ۱۵ درصد و پیش‌دانشگاهی ۵ درصد اعلام شده است.
🔹
در نظام ۶-۳-۳ نیز تاثیر پایهٔ یازدهم ۱۰ درصد و پایهٔ دوازهم ۲۰ درصد در نظر گرفته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/farsna/437175" target="_blank">📅 10:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437174">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/794f13081f.mp4?token=BydrnQPGsaLE7HAFd88io74pgHj2_FVVaUm8DWcUO-ru0afabRiGA9RD2qgQp-r-vuYJmJQ7kVKAoPrhtYPRItoV1Xyzbd8Qhf5OoaSyzmnI7EycnQ3UEGXSJBIeQpE4Zf33P65utbTTmIKLMcmUN8-JhxAiqm-N1U3RLv-KoLrkS52yLHMcShpQWqQ-4S_IeWLoU1nek-ufrXq1B0R_DeDK87N8T8XTTl-8WpVm9wHFrSRYIdwFeieesewQ7xIza7fVClfFeAtgMw4CxMIFOvlD7Z81EZNoWgbgRkz5EhnHpWqhw9cUiJ6YryQ7ITAx8RYxyKE83InBfySdKGUikA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/794f13081f.mp4?token=BydrnQPGsaLE7HAFd88io74pgHj2_FVVaUm8DWcUO-ru0afabRiGA9RD2qgQp-r-vuYJmJQ7kVKAoPrhtYPRItoV1Xyzbd8Qhf5OoaSyzmnI7EycnQ3UEGXSJBIeQpE4Zf33P65utbTTmIKLMcmUN8-JhxAiqm-N1U3RLv-KoLrkS52yLHMcShpQWqQ-4S_IeWLoU1nek-ufrXq1B0R_DeDK87N8T8XTTl-8WpVm9wHFrSRYIdwFeieesewQ7xIza7fVClfFeAtgMw4CxMIFOvlD7Z81EZNoWgbgRkz5EhnHpWqhw9cUiJ6YryQ7ITAx8RYxyKE83InBfySdKGUikA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سوس، تحلیل‌گر ارشد سیاست خارجی: ترامپ برای انحراف افکار عمومی از شکست‌ها، به نمایش ساخت‌وساز در کاخ سفید روی آورده است.
@Farsna</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/437174" target="_blank">📅 10:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437173">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef93a6c3c8.mp4?token=sNKlN2LPqO38xwIEZg3Y3ADtWaKeza4nPbzmU3O0Q5TiRBAEOWhY3BesWxzW727c82k5lsbakFNf29n_KweAHSkGXWnHQsJDDCakltF_yF2XbdKbDzQf9hTtL5-7_vDeSWrqzPTUe-scYArMAVccqxQQCwV7YCtWI9EEcNihkmo-dxGLJsFZkWrwWp7bDuUF5jGRhil6UeY7xb7kiTZE9afwRHMW5pNEbvoqEWevnAfrQZwy2-ZdLoTplX7p-djuSl3xNE33yRmPaE4FC_8SwOQwERLfqM2BWnlftwmZE8So6VvnYKFTDnPHMKteGzXO3wewYEZa9xSagKf0wCJIYg3y4fxBbQqr8r1xLo1yOx_JQC7DVzOX9YJ-JkkeFW8W9dkiXJWXXlQfVVcXaf1JeZRudVU0dSOCZanWa6MGr1uD2nhmqHcTx6Bd35qk_s0oGr4HOYIfpE1TcNesEPfmsx1b03dgcyJUWY6uJhsQ6TesMVjJQsT0MKgUu7TVvHUAb8U1fH1qIGTIjwGo0wKbBVGJ5cc2uNYCzZY3DfOVubi6rCjmDFz7fg514YIXmo3cjueSEqUDQSeVfGmLyHgS47fezpbj6zo20wFi7wvZhrENHYbXE0S_f_dzC4uF_KQWglsin0MbqkodfyThHcZadt_SK9UP1bFgi71veesXs9s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef93a6c3c8.mp4?token=sNKlN2LPqO38xwIEZg3Y3ADtWaKeza4nPbzmU3O0Q5TiRBAEOWhY3BesWxzW727c82k5lsbakFNf29n_KweAHSkGXWnHQsJDDCakltF_yF2XbdKbDzQf9hTtL5-7_vDeSWrqzPTUe-scYArMAVccqxQQCwV7YCtWI9EEcNihkmo-dxGLJsFZkWrwWp7bDuUF5jGRhil6UeY7xb7kiTZE9afwRHMW5pNEbvoqEWevnAfrQZwy2-ZdLoTplX7p-djuSl3xNE33yRmPaE4FC_8SwOQwERLfqM2BWnlftwmZE8So6VvnYKFTDnPHMKteGzXO3wewYEZa9xSagKf0wCJIYg3y4fxBbQqr8r1xLo1yOx_JQC7DVzOX9YJ-JkkeFW8W9dkiXJWXXlQfVVcXaf1JeZRudVU0dSOCZanWa6MGr1uD2nhmqHcTx6Bd35qk_s0oGr4HOYIfpE1TcNesEPfmsx1b03dgcyJUWY6uJhsQ6TesMVjJQsT0MKgUu7TVvHUAb8U1fH1qIGTIjwGo0wKbBVGJ5cc2uNYCzZY3DfOVubi6rCjmDFz7fg514YIXmo3cjueSEqUDQSeVfGmLyHgS47fezpbj6zo20wFi7wvZhrENHYbXE0S_f_dzC4uF_KQWglsin0MbqkodfyThHcZadt_SK9UP1bFgi71veesXs9s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تاکید ویژه شهید سپهبد موسوی بر تکمیل زیرساخت‌های سواحل مکران
🔹
امیر دریادار فرامرز بمانی، جانشین فرمانده نیروی دریایی ارتش از توجه ویژه شهید سپهبد موسوی به توسعه و تکمیل زیرساخت‌های سواحل مکران سخن می‌گوید.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/farsna/437173" target="_blank">📅 10:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437167">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F0P2Y_E0nMUQn6lR4PoLnv0jNmSih7h5d_GzM_nNs9_vj320zGY3Os7r-z3114Q5rzXdzkUfLsfuuQSbu666k0L56aRwwqPme8kdypFoRAZeb9xICNiioGs8Qkrdd30HwbrdegB3zFb8LZ8oX4Sh_8MYM2BZkd_kmeACxI03uZqqZNPTK3Hy0ARELng5V_rC-eymQ2UEIcaL9LGNNMABWuRjdjRCgXDPN-Jz_NSgAANA2lui1F4Le8u6dfVdqzjON1TB8UDKl7Myjq4OxwazVOhDPxSSowwLQn6hiyTf2qJAMSjc9PNNqXzc79Z_yr2UOlSEcbm7cbQJLCapS21wUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YLcYsVd3VTUKns_3KIaE6i1keX_ANerYBOjT0LyzUBbuE7R_OUfR4suOMXLQBWS-p91c5M18mGUEoKf1Jy5g8DN8FKqDm3GbkD4DKIzxxcKDBBIrpT9bzmANPNuRPFN_HB3ecUoEcQ-GP9xP6i15X9aNP31Zz6Scrhdz-Hv4bLCqcUwWR4M7eY7YGglSlsCrnfg339_wx0H4GoCKwYWkk1HFkLcjHnGrTZyjZE9Vt0F03DGbGyVWpzh1Pp3DIU6UVvSpvtvU4yK70Jwtts9cSCYwbcECXyjAR4crtYy4kOOAfWOg2Bgv7MQOGL7OLwEf_YcI9giBi1cI4GERgStRDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sZRwepihcZOxxLqZOcTDkpX846AkfiSpFCSSWIJN1uSjfMWIGh9V89jlyD_UfPnHBTWDsNVzOGK7-FaOcrxfC6uJGULSaBJlHeuxvIl5z8SNdVsLS9AlRole0I64nslCt5cLVVfd8NigWvpanxbCnX7NSsd2NA9Nm02cbDc4axNuU0QP0Yn8I01KsKHm_UsBaV5e_uIi49SZ8SZxOBq9Se9ovUQat_6LGRjscuk3gPhfaCEKjXw1JhZl0CqDPNpNgDr1eVlY8-dGVFZh5KkGLK5N75EWnpEamQAvkmvmkRD3SIunZlQO2P20SlTaF1tZtKkSkU7VZq24jSbFdOMAMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K-EaQ_1OGMFKj55b77loqU_NTr5vowlX28QEIY_IqI2iRvDqsb2o0De68DA8w9mRR4sVsdDUEHD4I9356tDQO91dnQyh3wOsNOMxGndrxEqfCzKkRmprtyg41EkYx0FAWwt3t_P-LCGw453E0S208gpHiBgmFmOPXwR0AEBKPh0jwxedpsZ8aNqT9SC7q9PfcIOINbpRDFyi8O-3FbSvFpV89alufsjbSnCHVp0zaUVjGiLufD-jpo9tmQVCcdcZucmI9gyGFpsXYzDgyfNHKDuO5uk3T0J0Kx33gxnpsgwwP18AMMd3ye0zOvna56b5wBXnqoKngTe7GlNAwZ2vIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p07dpAqjzny15sHM2Kuh_5E-oeEpQV31iVsWGDn7mo0BKYUuTr3d-OA_w59aVLvaeMOERkLhtxQVwFxAYy-w5nOqp9I_vw-s2KkVboZ6O9Nup-TWez-XZ0iD9ASS3iPVWwRzPKA5umTNVBNVLUCXQqwm9wlgTSl_UXQXNWHycdZH3kZsfPq5Z7WrddSzLCoeJE4Y8QgmvX58VLa3ikxUXvqBICeH6ezREpkpyU2dJfZTT5-4vh6xdNtWp1838ZnSf4CfcqRotsSQtS9mdJtwiWfMBIulDdDIpKHoX99gCp8u-3J4M4o7Jk3WGGTFT_GPHKW8dON67pSVgq8GAl0wzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hKdyp8pirRUBWGnkFl6nwn3be0gD8yAe0T9n7gK4GVF1iG5bnNwbZnl_YWR5VWwNTm-jgs-1D0peekuLmdd7UKcweXhzuxkmWdHCdMlqG3kYspGI1wa_2SsKa_PeArevcom-9XNShiEUrnDrzlfx5fm5P1gTrjLXNUyL6_0OCDn6DyjzXiFq6fFkVI-4gZHCwnfgGaMDFHzTKCwGKJqQ5kSiLpKSL3snrO67EtZDUh-7btpcEuQa5voS0Nw0qsDSuJH9WPf2tlZGmOMyn9-xGLM2gp_woZYNVB6Q8zNyr7iHIgQMDbZGUU8t3DIFfnrGawwOf37Y5iuM_9Z6vQU4DA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
اعتراف تلخ کهنه‌سرباز آمریکایی روی آوار مدرسهٔ میناب
🔹
کن اوکیف، خطاب به افکار عمومی جهان: فرض کنید همین موشک‌های تاماهاوک که در توسان آریزونا ساخته می‌شوند، بر سر کودکان شما فرو می‌ریختند.
🔹
تصور کنید ایران، ۱۳۲ فرزند شما را به قتل می‌رساند. آن وقت چه…</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/farsna/437167" target="_blank">📅 09:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437166">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba890d62c3.mp4?token=q0NiTHsX1KtSdjixdk35-Lb0SbqTi7WwiInHKEun2gRXI8O7i_Nj579zA4DC7IK54eB0cJtXVzgmlX6tiXe4-zDhk48KizLOxV8rnTNpxARXY8-sIzne8lRsR6SrwNFGaRcGZDGQt3lseDhxXlF6sblB4DWdxl-9GlAGa-SQ0Igj8Ka-kwhJce11hm0ByzOKvuxSr8nRtQ9adKBZ6zsenwR1SG2Px3-hY6wo7cw5UVkjq3-f-UmEG57hq_zpLV1JI_561fjfYt8Tda0TsJwDGAB-km0FUQjXngUIgMsF3S0NS64KqpDgyQSCL0WUwFYcHw_0q_mBMvOVxI4mkWnaqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba890d62c3.mp4?token=q0NiTHsX1KtSdjixdk35-Lb0SbqTi7WwiInHKEun2gRXI8O7i_Nj579zA4DC7IK54eB0cJtXVzgmlX6tiXe4-zDhk48KizLOxV8rnTNpxARXY8-sIzne8lRsR6SrwNFGaRcGZDGQt3lseDhxXlF6sblB4DWdxl-9GlAGa-SQ0Igj8Ka-kwhJce11hm0ByzOKvuxSr8nRtQ9adKBZ6zsenwR1SG2Px3-hY6wo7cw5UVkjq3-f-UmEG57hq_zpLV1JI_561fjfYt8Tda0TsJwDGAB-km0FUQjXngUIgMsF3S0NS64KqpDgyQSCL0WUwFYcHw_0q_mBMvOVxI4mkWnaqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعتراف تلخ کهنه‌سرباز آمریکایی روی آوار مدرسهٔ میناب
🔹
کن اوکیف، خطاب به افکار عمومی جهان: فرض کنید همین موشک‌های تاماهاوک که در توسان آریزونا ساخته می‌شوند، بر سر کودکان شما فرو می‌ریختند.
🔹
تصور کنید ایران، ۱۳۲ فرزند شما را به قتل می‌رساند. آن وقت چه حسی داشتید؟ آیا باز هم اشتباه بود اگر فریاد می‌زدید مرگ بر ایران؟
🔹
چطور جرئت می‌کنید این دروغ‌ها را به خورد دنیا بدهید؟ شما به من بگویید، جمهوری اسلامی ایران کدام اقدام تروریستی علیه شما انجام داده است؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/farsna/437166" target="_blank">📅 09:38 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437165">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🎥
گزارش اسپوتنیک از بازار بزرگ تهران؛ ايرانی‌ها امیدوار به آینده
🔹
خبرگزاری اسپوتنیک روسیه در گزارشی از بازار بزرگ تهران نوشت، زندگی پس از جنگ به بازار بزرگ تهران بازگشته است و با وجود آسیب‌ها و خسارات، ایرانی‌ها می‌گویند که کشورشان را دوست دارند، به نیروهای مسلح خود اعتماد دارند و به صلح و ثبات امیدوارند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/farsna/437165" target="_blank">📅 09:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437164">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">فعال‌شدن آژیر خطر در اراضی اشغالی
🔹
منابع رسانه‌ای اسرائیلی: آژیرهای هشدار در رأس‌الناقوره در جلیل غربی به‌دلیل نگرانی از نفوذ پهپادها به‌صدا درآمدند.
@Farsna</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/farsna/437164" target="_blank">📅 09:17 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437163">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🎥
وزیر کشور پاکستان با وزیر خارجۀ ایران دیدار و گفت‌وگو کرد.  @Farsna</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farsna/437163" target="_blank">📅 09:07 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437162">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mH_AiDdD3dqj2rVrD5sPYARYwn8Ho2UVzo7DfMCNQemKfuXAlOg-G_o06bGHsulVD4Jak0fqSC3dOjfGW79TgiHzFVTKPsI4Rb3MejUFRcZUdq5svUGYVHMd8EV8F2CY8IkdZjDa5svL2AT2gqCxaewpVpC2sZX6S9GgoQWsRxIoxIfo9RxSp1e3lDKsk-EKXcH3-GRHTQ6kVY9rrYTmzh44LaTOEbxDPSA4-f9AtFfEKpysVciJO-_0oLGJ-Jjh-QLNuXs5Sa_tKSahTbMJWdIeC-jW9eORCcW53JNiSz-yXrjzvzzUil-eyJo24foYZB0wnSrsMKLOCZD1InYkqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوای قابل‌قبول مهمان این روزهای تهران
🔹
براساس اعلام شرکت کنترل کیفیت هوای تهران، شاخص کیفیت هوای پایتخت امروز روی عدد ۷۲ قرار گرفته و در شرایط قابل‌قبول است.
🔹
همچنین در ۲۴ ساعت گذشته میانگین شاخص کیفیت هوا عدد ۶۱ را نشان می‌داد و وضعیت هوا قابل‌قبول بود.
🔹
تهران از ابتدای سال جاری تاکنون، ۱۱ روز هوای پاک، ۴۹ روز هوای قابل‌قبول و ۲ روز هوای ناسالم برای گروه‌های حساس را تجربه کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/437162" target="_blank">📅 09:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437159">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozV0OF8UNeS8VBicBlZIBYc6Tealy_6PGVjBlbyv09Rkp78acmVVxEIsJDYjCBmKpJxV7Pb1eljd3eUFcK4VI9VofyciL26txJlnHP2pqRqVApuDtqpfYe7f1Bt5ULFwVWHIGyDtvTG0QTZ9-n99N3B99_4I2KMKOjStt7U1GJbHGCcTORdU7aiSPFOEpjrXqabmSKYiW0gf3ljIbGDAv_dLokxb2PGVvVIaRl6T6fQnGyvgUXBoxExlOgRIPi-3WiTAY48o9BTLhzTyKjq6d9XfImkZXeVYiUQi5WjnR1f9Gi5j1k9i-wNAQO4zKJOHjcGooSGNGctBJOHfB__cjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهادت چهار نیروی امدادرسان در حمله هوایی رژیم اشغالگر به منطقه حناویه در شهرستان شهر صور در جنوب لبنان
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/437159" target="_blank">📅 08:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437158">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139d77e05b.mp4?token=Rxr2uXRrOXlJS3Eq62MLd9is_nyeNbFm6eEq-DqtDqsSD1n82yET6Aifnlhh8yRtzjN18XEW_7aGXCkisoq8GcOHJ2zL3PfGRo6HH2qqQwftBhfzCxDCQAq1rro3zQxv7ZB0x6vUz_hG0XweZrDz6DkJPHg8lHIi09xx4U8_L1hNmTfL7ayMV6UvWb7lgsqmmthhmpS5RccdzApL4is66WdANRuOj2IBYtMydjKOQbX1MwX4kZZlFzMptDLqKjGdZ7_dOEt3ug-xyEfW6lQt7pjdHjWl3P1WklizTvXHwSrdG8XY395jyRJAKuN9tiCJjpVwObsnUsYua48Z0X2DRUNn66A-N9yLaPnp1lFGZf_N6sU69NFE4x9c-eIAYZqsIUrk5cuu7hwPqsduO2mw9-4PcmmpaweAYyYINYXDiQWluhP3biEqTW5rakNMjFb2F65ELCHGI9efAOqb6HJGYB2tT2DmS6u7D3pNSdCVzfkdu9UZdrqvFnCzJ_Cl9IOWk5cQZYuzEqBPhvAMkMQpf03KEOGZxoWD1n37macC6bCZbgnytg3d6_LbpGNl6FTx7kVIA-9ubnUSTRknxrrWgg0CXuoU5Uq_qlmVyxCDiRxK_4P1TfEcdaM_vjrp0NLdXx2y_wtfeLvJ4ru2qCfwKtkobehGCU-bAffV5qNpfzk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139d77e05b.mp4?token=Rxr2uXRrOXlJS3Eq62MLd9is_nyeNbFm6eEq-DqtDqsSD1n82yET6Aifnlhh8yRtzjN18XEW_7aGXCkisoq8GcOHJ2zL3PfGRo6HH2qqQwftBhfzCxDCQAq1rro3zQxv7ZB0x6vUz_hG0XweZrDz6DkJPHg8lHIi09xx4U8_L1hNmTfL7ayMV6UvWb7lgsqmmthhmpS5RccdzApL4is66WdANRuOj2IBYtMydjKOQbX1MwX4kZZlFzMptDLqKjGdZ7_dOEt3ug-xyEfW6lQt7pjdHjWl3P1WklizTvXHwSrdG8XY395jyRJAKuN9tiCJjpVwObsnUsYua48Z0X2DRUNn66A-N9yLaPnp1lFGZf_N6sU69NFE4x9c-eIAYZqsIUrk5cuu7hwPqsduO2mw9-4PcmmpaweAYyYINYXDiQWluhP3biEqTW5rakNMjFb2F65ELCHGI9efAOqb6HJGYB2tT2DmS6u7D3pNSdCVzfkdu9UZdrqvFnCzJ_Cl9IOWk5cQZYuzEqBPhvAMkMQpf03KEOGZxoWD1n37macC6bCZbgnytg3d6_LbpGNl6FTx7kVIA-9ubnUSTRknxrrWgg0CXuoU5Uq_qlmVyxCDiRxK_4P1TfEcdaM_vjrp0NLdXx2y_wtfeLvJ4ru2qCfwKtkobehGCU-bAffV5qNpfzk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون پیشین رئیس موساد: ما به هیچ‌یک از اهدافی که داشتیم دست نیافتیم
🔹
ایگرا: حملهٔ آمریکا و اسرائیل ایرانی‌ها را به هم نزدیک کرد. اگر از من بپرسید که هدف و راهبرد این جنگ چه بود و ما چه به‌دست آوردیم، باید بگویم: آن اهداف اشتباه تعیین شدند و یا دست‌نیافتنی بودند و ما به آن اهداف دست نیافتیم.
@Farsna</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/farsna/437158" target="_blank">📅 08:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437157">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kd3eUePgHfeGhRqcVjFHnUBSeZQVz4LJTHSmkLg9L3GrhTw387qZZ2A1Jk1gzQBxoDdcNmE_YFaI9ZZUT_3iPIdbzTn-j3bjPKzjIHJ0io48RFMeduA_vDZZeW2lL_RC_rhnMypxLAZEU_JxoCakkq4jUrsz6--OJEY1uylYVesz9KAS30QSQ7vDSMlTuS5NiQU9Hs2D0kHhM5lzSeXOCrY_d3M0pVEp0nBobi5yRhIsT4veFPozpjFCIB8ITx4mpdqUdUS-knhH065Ss57ZbNWvbR9TqWCW3oxfdqF-Fwd_TA3-VUtLuEGxJlLD6NFHLKhNqpbQdFAHVGYcfI5SHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
بیانیۀ وزارت خارجه در محكوميت اقدام آمریکا در تحریم سفیر ایران در لبنان و تعدادی از مسئولان و شهروندان لبنانی
@Farsna</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/437157" target="_blank">📅 07:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437156">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VljCB8STuwgAQkq29zc6hGokA4yHMyl8Oser01ZoayhWDX-r9DHjWBeRvqKgeqQOI4JKF2SOap959tWZobJWZzWWBCBXJs1e6hKJMrr1D6gCWLKRLmZnYcRwWN6IeAxHBqwtNfTwYjs79M6XuV_8dG-8ID7BZy9_BYjngv5PHyQW3enN2ufFHt2nQ63AsmjncIK7z8Tsz9wfFaYt36JDPuOI3vMD5YTMpNi7REGjyBWXoXyYbSL7FeD6zsei5796i3OCbad5mCCam3trBALWAFhzlfJclAe5hOwgooEDzfTYS4wjJQwNpO8lbYVPr2X0gbypNg--PFHN-LbdavhR9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهم‌ترین ابزار نفتی ترامپ، در جنگ با ایران آب رفت!
🔹
ترامپ پس از یک هفته باز هم گفت در مورد ایران عجله ندارم؛ اما آمار ذخایر نفت آمریکا از واقعیت دیگری خبر می‌دهد.
🔹
جدیدترین آمار مخازن نفتی آمریکا نشان می‌دهد که ذخایر تجاری و ذخایر راهبردی آمریکا، در هفتۀ گذشته، حدود ۱۸ میلیون بشکه کم شده که بزرگ‌ترین کاهش هفتگی در تاریخ این کشور محسوب می‌شود.
🔹
بیشتر از ۸۰ روز است، عرضۀ نفت عبوری از تنگۀ هرمز به‌خاطر حملۀ آمریکا و اسرائیل به ایران متوقف شده و  ترامپ با همان ابزاری که با آن از بایدن انتقاد می‌کرد یعنی آزادسازی ذخایر راهبردی، تلاش می‌کند بازار نفت را کنترل کند اما هنوز نفت بالای ۱۰۷ دلار در هر بشکه معامله می‌شود.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/farsna/437156" target="_blank">📅 06:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437155">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0b2d423a7.mp4?token=fs4A81ZqBnaKaEMZsKBNO-ND4Dky_tdrNEYYz-mw5zd9_3ivl39xyFPXfR8ETEVB4icI8IvhN8tImmaVncrbkmpiJIjqtNlh9Kj_jRnWaUg0wRdHHWcNUhuHqvjv2abxNV5rssnBeHQwT9cDGh6LznytO6dLCy74Y3-egAJ2ULdVGCKLv0GNmyEIF0KT0PFWh1aqn3Yg2FgcIhF2jyvbSE82DzUDTPTCnWuCMbZQwTIOOoWorU-tcjAbE5gwMnkXQUV0m-ffb-JibSPqwTpIA0mvw3zPAVkrdt1pMQVo-ALp6xvC3znOmBEk__03KFwd-1U8BmE3jlWwCcV6Omfl1w6BlGjqdtGBflPATpvyei9KZA9BccFcroBirlAMrU4knBUnm88HUkZ33oN1MNq7zLx5Sq8G5iceNSj1IASuG5c3Zt0LX7vXaxWRcfi5yw1CC1hNhOUyUergwn12kwyb4oSSTaG3rfG1TxXxg3zS9R_ko6zpYqMm1sNCpcXitUVcyea1VKdTTcwnOahWKh2P7Lxqv0HoMQPIPklGLGsPpnulmFC61p0yYfD6Y65h0YSrk-tUD5Djr9zyFDgaDWoUA3487_4rDnBMBwCB7Y_BPqQeIhsmbdPslu1yfSPpZFGZyRITypKX8qomXpolYjZaMbJQEUUbQPKkwobvj6pIml0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0b2d423a7.mp4?token=fs4A81ZqBnaKaEMZsKBNO-ND4Dky_tdrNEYYz-mw5zd9_3ivl39xyFPXfR8ETEVB4icI8IvhN8tImmaVncrbkmpiJIjqtNlh9Kj_jRnWaUg0wRdHHWcNUhuHqvjv2abxNV5rssnBeHQwT9cDGh6LznytO6dLCy74Y3-egAJ2ULdVGCKLv0GNmyEIF0KT0PFWh1aqn3Yg2FgcIhF2jyvbSE82DzUDTPTCnWuCMbZQwTIOOoWorU-tcjAbE5gwMnkXQUV0m-ffb-JibSPqwTpIA0mvw3zPAVkrdt1pMQVo-ALp6xvC3znOmBEk__03KFwd-1U8BmE3jlWwCcV6Omfl1w6BlGjqdtGBflPATpvyei9KZA9BccFcroBirlAMrU4knBUnm88HUkZ33oN1MNq7zLx5Sq8G5iceNSj1IASuG5c3Zt0LX7vXaxWRcfi5yw1CC1hNhOUyUergwn12kwyb4oSSTaG3rfG1TxXxg3zS9R_ko6zpYqMm1sNCpcXitUVcyea1VKdTTcwnOahWKh2P7Lxqv0HoMQPIPklGLGsPpnulmFC61p0yYfD6Y65h0YSrk-tUD5Djr9zyFDgaDWoUA3487_4rDnBMBwCB7Y_BPqQeIhsmbdPslu1yfSPpZFGZyRITypKX8qomXpolYjZaMbJQEUUbQPKkwobvj6pIml0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت‌هایی از زندگی دانش‌آموزان میناب پیش از شهادت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/farsna/437155" target="_blank">📅 05:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437154">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">هشدار بلومبرگ؛ احتمال رکود بزرگ در نتیجۀ بسته‌ماندن تنگۀ هرمز
🔹
بلومبرگ به نقل از مؤسسۀ انرژی راپیدان هشدار داد تداوم وضعیت تنگۀ هرمز تا ماه اوت (مردادماه)، خطر وقوع یک رکود اقتصادی ویرانگر در سطح جهان را به‌شدت افزایش می‌دهد.
🔹
رکودی که ابعاد و قدرت تخریب…</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/farsna/437154" target="_blank">📅 05:14 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437153">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qj4a-V8Blt4Me9kdyxdbDeQh4o6TbhwFE98tT7D5CTiUhgyF9I77-XW9pj18MYjelA_JZBtWT9Z9jEwS_tlPg_-wqsfe9g8v2n9k74G24yM9yIe4dA3_b7M0KSoPBeWRQuqySlj0Cpbcf2JmgymqUy0jucmMvC0PBjudSLd6-GNaYmEK0cRr2f4l2H0BmJXyIfm8s42EtVaSWrdBlTwuq9ZITXgJVdzZK8SPRXVWwUlnktIEulfFd3YNeAnbmYFhDzAAjddOv4rI8ok5Lqw8rSWNKtyf6PYVx81A7ayuUHrfUYJnXVOFliqbYBnQaNpdOTYOSYfTnnw_GTYl_Mu3Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقش حیاتی انستیتو پاستور برای منطقه در نگاه نشریهٔ پزشکی جهانی
🔹
نشریهٔ پزشکی بین‌المللی «لنست» با انتشار مقاله‌ای با عنوان «آسیب به انستیتو پاستور ایران، امنیت سلامت منطقه را تهدید می‌کند» تضعیف این نهاد را نه تنها یک مسئله ملی بلکه تهدیدی جدی برای امنیت…</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/farsna/437153" target="_blank">📅 04:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437152">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pc_eaIeWhqDKYANSBf_WRgpLC4uNrkp9disi01EWeVrd-98ZGUARhaxbBrrnDx943VQFhKivOg-fHh0Jmfgd_zg00KvYpdIqL7P71SXkwNsYKe2tAmjXySmiSW0UsZwUcJs85e9G_duWxWlkxQcO5uOM38JXcRGTJpyBVbPtSaSpnjWo38763Nr843eosyZCKSkN178PmjaX1xz-fml-k_Z86rD006-NwKheSuMjCyp37xskhWeKAeyGxh5hbFhw_NSExXEreK3KEhch7XeTyFZUstEPHLYYy2JC8C0dt7IkL6p0cU_vsaTh9KGYV2-CqqaNKzZIHffQY1IEZhijVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدافع ملی‌پوش در پرسپولیس به آخر خط رسید
🔹
میلاد محمدی که همراه با تیم‌ملی در تعطیلات نوروز به ترکیه رفته بود، بعد از این اردو، به یونان رفت و پس از آغاز تمرینات پرسپولیس در دوران آتش‌بس، حاضر به بازگشت به تهران نشد، تا باشگاه پرسپولیس او را جریمه کند.
🔹
رفتار عجیب محمدی آنجا بود که او پس از دعوت به اردوی تیم‌ملی، خیلی زود خود را به تهران رساند تا شانس حضور در جام‌جهانی را از دست ندهد. اتفاقی که عصبانیت مسئولان پرسپولیس را درپی داشت.
🔹
حالا قرارداد محمدی در پایان فصل با پرسپولیس به پایان می‌رسد و در شرایط فعلی بعید به نظر می‌رسد که این قرارداد تمدید شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/farsna/437152" target="_blank">📅 03:29 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437151">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🎥
حماسۀ ۸۲ دامغانی‌ها در میدان دفاع ملی
@Farsna</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/farsna/437151" target="_blank">📅 03:01 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437150">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">تعویق رأی‌گیری دربارۀ اختیارات جنگی ترامپ در مجلس نمایندگان
🔹
مجلس نمایندگان آمریکا رأی‌گیری دربارۀ قطعنامۀ موسوم به «اختیارات جنگی» را به تعویق انداخت.
🔹
این قطعنامه را اعضای دموکرات این مجلس با هدف محدود کردن اختیارات دونالد ترامپ در جنگ علیه ایران پیشنهاد داده‌اند.
🔹
نشریۀ هیل نوشته به نظر می‌رسد رهبران جمهوری‌خواه در این مجلس این رأی‌گیری را به‌دلیل به‌حد نصاب نرسیدن شمار نمایندگان حاضر خود عقب انداخته‌اند.
🔹
اگرچه اعضای جمهوری‌خواه در مجلس نمایندگان هفتۀ گذشته توانسته بودند قطعنامۀ مشابهی را با اختلافی بسیار اندک رد کنند، اما روند تحولات در کنگره نشان از شکاف در بدنۀ حزب حاکم دارد.
@Farsna</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/437150" target="_blank">📅 02:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437149">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">هشدار بلومبرگ؛ احتمال رکود بزرگ در نتیجۀ بسته‌ماندن تنگۀ هرمز
🔹
بلومبرگ به نقل از مؤسسۀ انرژی راپیدان هشدار داد تداوم وضعیت تنگۀ هرمز تا ماه اوت (مردادماه)، خطر وقوع یک رکود اقتصادی ویرانگر در سطح جهان را به‌شدت افزایش می‌دهد.
🔹
رکودی که ابعاد و قدرت تخریب آن می‌تواند با بحران مالی بزرگ سال ۲۰۰۸ میلادی برابری کند.
@Farsna</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/437149" target="_blank">📅 02:25 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437148">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpgjdt_F90jTlirAp9g9M2yGkEye6NwGcFoHwhoiMDqReMo64tMyLOP70OTAI1jywMgLkzK1uE2tzQ_AXPIC4oRggVjLOmj-9OAcRukSt8lz-lmmDNbhEW3HwYtz_bx526cNiA8pg0Gc30G1g-HSfISdTKDDyt7NVEiXmpI7JX-ZU0_F2FSqzOCBcn4tAuQeTpH08pMxNUOdaMlkYYcjiVbKOHBaQ09Pty8ITW11elGaSmJc6Gjqr8mbP1xYO51przYlgoqFrm1Ntn9jc2noST45n7p-jAWOfzxGoNS5hK2Rp3ag0uiudQ2C46K9Dpoii5g-KCXu-7EVxrBRrDcWmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان موقت استفاده از کارت‌سوخت اضطراری در جایگاه‌های هرمزگان
🔹
فرماندار بندرعباس: از بامداد یکم خرداد به مدت ۱۰ روز کارت‌های سوخت اضطراری جایگاه‌ها جمع آوری می‌شود.
🔹
در این مدت شرکت پخش فرآورد‌های نفتی نسبت به فعال‌سازی سیستم پایش تصویری و پلاک‌خوان در جایگاه‌ها اقدام خواهد کرد.
🔹
دوجایگاه برای خودروهای اداری یا فاقد کارت‌سوخت در نظر گرفته شده است. اما وسایل نقلیۀ فاقد کارت‌سوخت باید برای صدور کارت اقدام کنند، که ۴۸ ساعته صادر خواهد شد.
🔗
جزئیات کامل خبر را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/437148" target="_blank">📅 02:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437147">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🎥
بندرعباسی‌ها در ساحل خلیج‌فارس هشتادودومین شب اقتدار ملی را حماسه‌ساز کردند
@Farsna</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/437147" target="_blank">📅 02:01 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437146">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🎥
مداحی جدید مهدی رسولی برای میدان
🔸
میدان خداقوت، خیابان خداقوت
🔸
جمهوری‌اسلامی‌ایران خداقوت
🔹
خودش را دیده سلطان زمانه؟
🔹
تو برگردی ازاینجا فاتحانه؟
🔹
شتر در خواب بیند پنبه‌دانه!
@Farsna</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/437146" target="_blank">📅 01:37 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437145">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🎥
۱:۲۰ | حاج قاسم سلیمانی: در حرکت امام حسین(ع) از صحرای عرفات تا گودی قتلگاه، اصول و هدف سیدالشهداء هیچ تغییری نکرد
@Farsna</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/437145" target="_blank">📅 01:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437144">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حملات هوایی رژیم‌صهیونیستی به جنوب لبنان
🔹
خبرنگار المیادین در جنوب لبنان گزارش داد جنگنده‌های اسرائیلی مناطق «زوطر»، «کفرا» و «حناویه» را بمباران کرده‌اند.
🔹
هنوز جزئیاتی دربارۀ تلفات و خسارت‌های احتمالی این حملات منتشر نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/farsna/437144" target="_blank">📅 01:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437143">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGFv3lG38-6rg0x1UHuI4uYerOiLJtkFgx9zovkDQaWuQwFnqV7NTtJqZMeWCUDtuFSCWDLPbLvG0fqo8lMWqXkzrDZuAfPQXTU8exNOFtl-ZlO0GBhtTydgJq0SOeO_yg9wp6qu3DXNCGi9YCIqWgLql9jzNVAw2zPMQPXRJaVeSRDoVihwR5F7EcF3ZkoAruHbAhb3omGivWi-UHqxoDiNFirVY44J1FRlyw_DJwas5ghZjEAYA1nQY4xchiBKOqCRyH9MTzszUPJfmTivuQpW7X7Wxk9sKMMr6XaBnE3vxfBgj98Mz5Hninux2KNSbHRgxyujNxbvqoDR7mehnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قصد آمریکا برای اعزام نظامی به لهستان؛ پاداش به ورشو پس از تنبیه برلین
🔹
دونالد ترامپ، رئیس‌جمهور ایالات متحده با انتشار پیامی در «تروث سوشال» اعلام کرد که مایل است ۵,۰۰۰ سرباز آمریکایی دیگر به کشور لهستان اعزام کند.
🔹
او به جزئیات بیشتری از جمله زمان دقیق اعزام نیروها و اینکه آنها از کدام پایگاه‌ها منتقل خواهند شد، اشاره‌ای نکرد.
🔹
ترامپ دلیل این تصمیم را روابط بسیار خوب و نزدیک خود با «کارول ناوروکی»، رئیس‌جمهور راست‌گرای محافظه‌کار لهستان، عنوان کرد.
🔹
ناوروکی که در اواسط سال ۲۰۲۵ در دور دوم انتخابات ریاست‌جمهوری لهستان پیروز شد، پاییز گذشته در دفتر بیضی کاخ سفید با ترامپ دیدار کرد.
🔹
حدود سه هفته پیش وزیر دفاع آمریکا دستور خروج حدود ۵,۰۰۰ سرباز آمریکایی از خاک آلمان را صادر کرد؛ تصمیمی که پس از انتقادات تند «فریدریش مرتس»، صدراعظم آلمان، از اقدامات نظامی و سیاست‌های ترامپ در قبال جنگ ایران اتخاذ شد.
🔹
بلافاصله پس از تنبیه انضباطی برلین توسط کاخ سفید، دولت لهستان آمادگی خود را برای پذیرش این سربازان رانده‌شده از آلمان اعلام کرد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/437143" target="_blank">📅 01:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437141">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45f0cd0b59.mp4?token=b_TuLZcNMxeRHaDYFTOtjxxJ7Yz6ZryqWMtCVTK8DEozVIxwFfWuaJISDA4uO4IwAjLsbi9jzOzj_fLwMEfcjgN0_keMuibTE9opeVBY8N5Woxu96WbO72piSMNzsOJskDlzVDJTnz1ODyp_NCcbHic80svbQCyUuaJ0d-J4bYR5-NLP-0tfPgKIZSO2AjfVhjE2eoaA2CFOB2tnOxY5fezIR_M_dm74gud_T9zyKQNnUD3ae-HzLledL4Gn3Bf7QE0Puwnkjj8qGnCWVO5QxikBvLxR-y6B46T_yw-8N-G54vbe187Vt92pbqb1uag7DQWxxcu-it8U5kYkma20noi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45f0cd0b59.mp4?token=b_TuLZcNMxeRHaDYFTOtjxxJ7Yz6ZryqWMtCVTK8DEozVIxwFfWuaJISDA4uO4IwAjLsbi9jzOzj_fLwMEfcjgN0_keMuibTE9opeVBY8N5Woxu96WbO72piSMNzsOJskDlzVDJTnz1ODyp_NCcbHic80svbQCyUuaJ0d-J4bYR5-NLP-0tfPgKIZSO2AjfVhjE2eoaA2CFOB2tnOxY5fezIR_M_dm74gud_T9zyKQNnUD3ae-HzLledL4Gn3Bf7QE0Puwnkjj8qGnCWVO5QxikBvLxR-y6B46T_yw-8N-G54vbe187Vt92pbqb1uag7DQWxxcu-it8U5kYkma20noi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان‌داری کرمانی‌ها به شب ۸۲ رسید
@Farsna</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/farsna/437141" target="_blank">📅 00:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437140">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oiiDun9y4EL9oXvT8cNffH_OVzf5sMjbZbEJ3wnjs8E2dCV0Bqvcol81w49s5SDZXR7wUuLB1OWhULBS10vEdQgISP2Wdx1ab1-f9i0xPwukl11RRoci9dLSJEFKANYlZ6K358Q-aDOzOpfVj47aWjW9KEGkZaJ-hSlm5LM7Ja299rUdrS1jQHhbp0g-NHLtdBke1RlLPb3reENXnWOO5ESRFwyo3rPOLassRXM0DbNTMQIJLbDtKCZaLCrYfqyiCShJE3rObgyincV7adGWnUqUsCtySvANcxPTbWb2gcEpKd388MlhaiQPXqIFIooZyoyjy8ec0yCxsrTLdZbocg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان‌: ترامپ شکست مقابل ایران را در کوبا تلافی می‌کند
🔹
سی‌ان‌ان، صدور کیفرخواست علیه رائول کاسترو، رئیس‌جمهور پیشین کوبا را تلاشی از سوی ترامپ برای جبران شکست در پیگیری براندازی در ایران توصیف کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/437140" target="_blank">📅 00:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437138">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKZwVSUwQ5Ci2vlrPqLrJCjem9c3NXkNKTX_RB_n6WqSVOLsD2PKqk2TfrMR-Y0vlyGTFW_Ocmj0tJgrhloiKoJseoSznp6O139aNbZzHRNVuZJYd2tHIn1qPNPRQLlQpcgR8OQIBcPOFq4TAnfD51ZXYVK9gNzQ2zzCfFVl3FbU8GbhaGEaREH9EZLfHd7KfxiwqxsggQkH7rZvNQGSJpcFWthQdAqDO1nhrl0dQYMmop-tZpEegUo71bY7zHPLkwFLHfyY1oU0TKSVLyuby4wIjzeMbnqlK4MmqFwzoc9LKZbTR3355J0cxut6zLR7diwTmkelllJ1mxc8kIQzkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گریز به سایهٔ تقدیر
🔹
روزی شخصی پریشان و رنگ‌پریده به درگاه حضرت سلیمان(ع) پناه برد. سلیمان از او پرسید: «ای مرد، چرا چنین هراسانی؟ چه بر سرت آمده است؟»
🔹
آن مرد با لرز گفت: «در راه، ملک‌الموت را دیدم که با خشمی عجیب و نگاهی تند به من می‌نگریست؛ گویی قصدِ جانم را داشت. ای پیامبر خدا، تو بر باد فرمان‌روایی؛ از تو خواهش می‌کنم به باد دستور دهی مرا به دورترین نقطه در هند ببرد تا شاید از چنگال مرگ رهایی یابم.»
🔹
سلیمان دلش بر او سوخت و به باد فرمان داد تا مرد را بی‌درنگ به اعماق سرزمین هند ببرد.
🔹
مدتی بعد، سلیمان(ع) فرشتهٔ مرگ را دید و از او پرسید: «چرا آن روز به آن بندهٔ خدا با خشم و غضب نگریستی که چنان هراسان شد؟»
🔹
عزرائیل پاسخ داد: «ای سلیمان، نگاه من از سرِ خشم نبود، بلکه از روی تعجب و شگفتی بود! خداوند به من فرمان داده بود که جانِ آن مرد را در همین ساعت در خاک هند قبض کنم. وقتی او را اینجا دیدم، با خود گفتم اگر او ۱۰۰ سال هم بدود، به هند نمی‌رسد؛ پس چگونه مأموریتم را انجام دهم؟ اما وقتی به هند رفتم، او را همان‌جا یافتم که به پای خود آمده بود و در زمانِ مقرر، جانش را گرفتم!»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/437138" target="_blank">📅 00:02 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437137">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVUJdXaq6tmAw0TDL9XqWtm_r2A5fGNCVaAg3g1RfSLhL1NEgMwkG-f_xlz36AU0oomJlUp27jiJMUupLvjhIkA9uxIm0FXq4HfVbV7S-mblnzTFf94vuI6L3jKRLBqJIS3goem74__ih-1M8e0XbDIuurDXSTGblwsmUWG407CPOpD7z5BECtoVd5xLLxYsA1wGxMXxl-tXGI5rmesa6bRbeoqn3k25Qua1hjji8xktPQAX98YEaA8b-NTINSeWIl9veUVytpCu3PicCb6ehkEXWYjbBGn4ApeL4GTluH_Q6SLhJWpoYejNC7il9DotRQO0iqafKT1OSM9KD9Smiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان انتظار CR7
النصر قهرمان لیگ عربستان شد
🔸
با برد ۴ بر یک النصر مقابل ضمک در هفتۀ آخر لیگ عربستان این تیم به مقام قهرمانی رسید. رونالدو در این بازی دو گل به ثمر رساند.
🔸
این اولین جام رونالدو پس از سه سال حضور در النصر است
@Sportfars</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/farsna/437137" target="_blank">📅 23:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-437136">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e61794309.mp4?token=jBtzOwLUBfIOwfP5BIJDyfO0GW4d0sDc1xmlfh1Spxr1DYlf05Kzw6JC5vBROocSYhm_Jr9_-IqXh0XYc5hQRTtn6aeavvWJXyMyqqa5rA03N2oTY6jNMGBlJNdn3QdLxN4HiA37cYkgLTNM5EElG_JhBlvApr9W16RidixWJ9UkXRp-dGzjELaGPYTTRFX79GBq2ndPRBRTxKzgAvQhCLtqQaBKX4xOHiJbuLlik3NA_hukTUDABRS72wL9BV0H7ZcZxaQwqt2OI3920xVcvigapZXr7mxHNzaqxMN_PRa60xE5V_y92GbEqcM55iAymQ7cubm_wopa7bxUqCSBozzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e61794309.mp4?token=jBtzOwLUBfIOwfP5BIJDyfO0GW4d0sDc1xmlfh1Spxr1DYlf05Kzw6JC5vBROocSYhm_Jr9_-IqXh0XYc5hQRTtn6aeavvWJXyMyqqa5rA03N2oTY6jNMGBlJNdn3QdLxN4HiA37cYkgLTNM5EElG_JhBlvApr9W16RidixWJ9UkXRp-dGzjELaGPYTTRFX79GBq2ndPRBRTxKzgAvQhCLtqQaBKX4xOHiJbuLlik3NA_hukTUDABRS72wL9BV0H7ZcZxaQwqt2OI3920xVcvigapZXr7mxHNzaqxMN_PRa60xE5V_y92GbEqcM55iAymQ7cubm_wopa7bxUqCSBozzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یاسوج همچنان عزادار رهبر شهید امت است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/farsna/437136" target="_blank">📅 23:53 · 31 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
