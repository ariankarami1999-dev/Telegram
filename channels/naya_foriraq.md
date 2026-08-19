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
<img src="https://cdn4.telesco.pe/file/pNPAGrXuuVjyTqeCLAUcwR7lTPXv4dOs-R-s6wv9X3PVT78NPKm0rxijlzqplJkEjoQV2L7tpjRAofsK_11n4ZuoUHiGO1hvD-RqaTslV2GqQTk1HusAIxDo09JKLG933xTLWBiF7c2v0JlnmVw4ZjfxEltAcydxY6k1p0VdRk7rFZHlqVwpqLR6guHxrorUnPOQzQ00XKHkZMiIygAlCjJDJAjlCUULV3gBuepZKtyOG1lUZFvEQE9ssvoYKibBO_WilD0F952dsZcVNONssYEsBARiZjZ7oUHY0fdV2nuaNrvC8qdiXvRrFIv8apRAJb44dvltdOtgKpNaYx9Vkg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 271K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-28 15:56:47</div>
<hr>

<div class="tg-post" id="msg-88158">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇱
نفتالي بينيت:
سنحقق تطبيع العلاقات مع السعودية، وإندونيسيا، ومع دول أخرى وسنبني تحالفًا للقوى "المعتدلة" في المنطقة ضد القوى "الإسلامية" - ضد إيران، وضد قطر، وتركيا، وجميع القوى "الراديكالية".</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/naya_foriraq/88158" target="_blank">📅 15:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88157">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4y9Va-CCiZ648pCAr22EEohTls4jxDSadlnzT4yRUaIS-uPljG--MqGaBLHuRtREkJs5ZtIK7Y5GgIcpCoQSFEhnLje7wxJ3xLATF4UUY5X86HR6VBnVGHZw2K9yi15iIiMuHFZaM5j4iSlgJAkvKmtFXEHuwEnrtoNIi8bd384n-HUW45B2PCuEl5HgrywjePMY5XaSJcaeGCQgS4mVfkK0nSO44Tnfuf3w7tF-lLZTiLVnJWoVOrSaIKmFUYI9Z6J6BVJE1mWOvlotufUvwu85XAJ7tntbmFvdxypSU3-j4dA9m2ZXXA3oV7TI4-cS0BsP9a65XOFjlTogiW2xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
قاليباف
:
أبو مهدي والحاج قاسم العزيزان! ها هي ثمرة جهادكما ودمكما المبارك.
‏في النظام الإقليمي الجديد، أخذ تدخل القوى الأجنبية في المعادلات بين الدول ينحسر بشكل متسارع؛ فأمريكا تبحث عن مخرج مشرّفٍ لها من المنطقة وبات مشروع من النهر إلى البحر للكيان الصهيوني محضَ أضغاث أحلام. ‌
#أخوتنا_قوتنا
⁩</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/naya_foriraq/88157" target="_blank">📅 14:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88156">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCwU92vaDfCzh7SDdPgzbDZ-_oqRDg_zBBu5O2mIQREcKaJSkdjIuXsaVIUCZsSZcZ6mcmrdZENER0fCYn_tuXFLDxLYlc8hn15iIQRFOx4CzqN_0M54OcY5CcLiJJc4Q610j7G1lYgh-0VcpxRwdhsh5b7aE5ZjXmnh-eXUPvp8EHRpWlczrzuWb-U4fmelXRM48iKBgxWJcNM541cT6VPIIY-Y9tHJX2Heq9nsMOpdpswoNSoKCkzfCUB-DZO2fIhmB6jVCHX2lb-nfIkQQ2ECzrJIGhccEfSkLS7-3iXga3xEwaPWnfRMxi7Y1b3abJPWO1rTqivia8FbIbuFQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
رئيس البرلمان العراقي يدعو قاليباف إلى أن يكون للعراق خصوصية فيما يتعلق بتصدير النفط عبر مضيق هرمز بما يحفظ مصالحه الاقتصادية.</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/naya_foriraq/88156" target="_blank">📅 14:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88155">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">▫️
هجوم مسلح يطال مدير بنك سيد صادق في محافظة السليمانية ضمن اقليم كردستان العراق واصابته اصابة بليغة.</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/naya_foriraq/88155" target="_blank">📅 14:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88154">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇶
🇮🇷
التلفزيون الايراني:
بدء نقل النفط العراقي إلى تركيا وأفغانستان عبر السكك الحديدية من كرمانشاه. أول شحنة تزن 50 ألف طن.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/88154" target="_blank">📅 13:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88153">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mlfaj8OEc5Kdx9loKX7562toNU7RUue4SuoBemtHsJeKoL5QpGWv6IaLzAvDXIr7mqLFeXf3vPbqVOL4SNSQfwMoYkiK7RerAXvyThUp4s8p0BBazDh5ZuCjBf6wTzSqRORs6nlCC4W82J64-3GbFf4rq9WMyQRRgH4q1nnI1IbjxsAg-jy7S4PhKAgZmJTw_isNRct7BZ2ci2Uc0LxHRgUjZps4TLSoTTkibq06hlT38FSeB1NCDaj0rkhr0DRRAJJ736laXAQ8kKyrsDS8Pi7vNrv0rKH_mpauIvnQcqXi9tPFUuWEGxJnD4a-3ITeOyC12xWODS8luRAjGh02JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
القضاء هو طوق النجاة الأخير للدولة العراقية
استنكار سياسي وجماهيري بعد تسريب خبر محاولة استهداف قاضي قضاة العراق وحصن العراق الأخير .</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/88153" target="_blank">📅 12:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88152">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c0c38ef88.mp4?token=hJ07fAN99KcSJu_qcUQegaHoPNZ3LlSdmrXc6fU6iolxF2gv_5b2xPcvdMB6LJhLKcvWltG4xkPoQ3do--cZjxEI_oVcnnj_ioWTrJLJKcFt10knD4GZW0HGr7k0T6_EEUMuPeuoF8VqnH9dcQ8zss_Q4h9zgjcI6yafn1m79bPMs5s4y7RKCGqLPpyOMnIXlMpEh5jmmbGsb3ASu-qSS_yBkG-BNVP5DIEEuqzsl8U2ntsgpEi12IxMEzgadt5ChUjtpDMcTMjPepqERaPS3a5z-e31roGCe6bW0UMi1RO2FlE9eeeBMdX-03WFgkfaylQm1igUod5ZK64gPz8btGI8j3SRqy9ZE1sRac0GADgxNaR4b3POPle_e7BKw12pYvmoiL7YbeHTYxAy2zKFiIxp-48POBlHGWlrXFzXfKD01Pq1tibPspxQdU1a1WPKoyDSTNlOXCLvxWtelZjJZSFetWERZKAMLeybAReB4MpbZ29H_nHw3xF9u6uYCwddnKr2plWBFuFBdmCSHTlqoNRuM3yZT0vvY7zBRBdgIuMNsbbVgRIaG_U5Bo0giolDLfFIuAm9IiVddA4zr6mMdLjs9Z60EJxTJnYJOZ8XmkknHBWHlfw2cZV_y3SOfNKwbY6C7irxaQUZHfWTQqTEDipzqQVj2bcN1ALCH6yDAhE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c0c38ef88.mp4?token=hJ07fAN99KcSJu_qcUQegaHoPNZ3LlSdmrXc6fU6iolxF2gv_5b2xPcvdMB6LJhLKcvWltG4xkPoQ3do--cZjxEI_oVcnnj_ioWTrJLJKcFt10knD4GZW0HGr7k0T6_EEUMuPeuoF8VqnH9dcQ8zss_Q4h9zgjcI6yafn1m79bPMs5s4y7RKCGqLPpyOMnIXlMpEh5jmmbGsb3ASu-qSS_yBkG-BNVP5DIEEuqzsl8U2ntsgpEi12IxMEzgadt5ChUjtpDMcTMjPepqERaPS3a5z-e31roGCe6bW0UMi1RO2FlE9eeeBMdX-03WFgkfaylQm1igUod5ZK64gPz8btGI8j3SRqy9ZE1sRac0GADgxNaR4b3POPle_e7BKw12pYvmoiL7YbeHTYxAy2zKFiIxp-48POBlHGWlrXFzXfKD01Pq1tibPspxQdU1a1WPKoyDSTNlOXCLvxWtelZjJZSFetWERZKAMLeybAReB4MpbZ29H_nHw3xF9u6uYCwddnKr2plWBFuFBdmCSHTlqoNRuM3yZT0vvY7zBRBdgIuMNsbbVgRIaG_U5Bo0giolDLfFIuAm9IiVddA4zr6mMdLjs9Z60EJxTJnYJOZ8XmkknHBWHlfw2cZV_y3SOfNKwbY6C7irxaQUZHfWTQqTEDipzqQVj2bcN1ALCH6yDAhE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
عدسة نايا تستقبل رئيس البرلمان الإيراني   #اخوتنا_قوتنا</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/88152" target="_blank">📅 12:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88151">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇹🇷
🇮🇱
توم براك:
كنا أمس على بعد خطوة واحدة من مواجهة عسكرية مباشرة بين تركيا وإسرائيل.
قصف إسرائيل لمطار أبو الظهور ينذر بمواجهة عسكرية مباشرة بين إسرائيل وتركيا.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/88151" target="_blank">📅 11:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88150">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0774535f.mp4?token=P5Aa8f-b8aWzsiQsBoaNPlFlfEHHrGLQ1vOS2ytuLi1Fs7uIK6HoEzW7vPwh8RcVmkkB9yluNtoBXpXbICJlgeSj0fQDyGdXqd1UooPdK1ldSBPtSK2Em9HI-UOhu5VAAoKf5tpBtMtRveD5ItMH98UTMCT0KGjIHmdS5DpQxWmwT9_mBV76s5_IbmHYGvFK3xTEsB-LdVTZqT-rPQRaEyza-4ctHFgycLL9uhvvV63aq38XUP1cOlStl3yFLFW8ZvgdjJLUwgrO6Kn18URiielbfdD3mkwuE-7URgwBTvnMr8M5mGbbpk6NUjcahTsAMSUIsOM81_o188JjaVQ9Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0774535f.mp4?token=P5Aa8f-b8aWzsiQsBoaNPlFlfEHHrGLQ1vOS2ytuLi1Fs7uIK6HoEzW7vPwh8RcVmkkB9yluNtoBXpXbICJlgeSj0fQDyGdXqd1UooPdK1ldSBPtSK2Em9HI-UOhu5VAAoKf5tpBtMtRveD5ItMH98UTMCT0KGjIHmdS5DpQxWmwT9_mBV76s5_IbmHYGvFK3xTEsB-LdVTZqT-rPQRaEyza-4ctHFgycLL9uhvvV63aq38XUP1cOlStl3yFLFW8ZvgdjJLUwgrO6Kn18URiielbfdD3mkwuE-7URgwBTvnMr8M5mGbbpk6NUjcahTsAMSUIsOM81_o188JjaVQ9Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
إستهداف مركز شرطة بواسطة طائرة مسيرة في ولاية طرابزون التركية.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/88150" target="_blank">📅 11:11 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88149">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇷
في أعقاب ادعاء البيت الأبيض بخصوص تعليق المفاوضات مع إيران إلى أجل غير مسمى، قال مصدر مطلع مقرب من فريق التفاوض:
"لم تكن هناك مفاوضات مباشرة بين إيران والولايات المتحدة أساسًا."
أجريت محادثات مع سلطنة عمان بشأن فرض سيادة على مضيق هرمز. بعد انتهاك الولايات المتحدة لاتفاقية إسلام آباد، تم تعليق المحادثات مع الجانب الأمريكي، والمحادثات الأخيرة لم تكن لها أي صلة بالولايات المتحدة.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/88149" target="_blank">📅 10:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88148">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔻
إستهداف سفينة في باب المندب قبالة ميناء المخا اليمنية.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/88148" target="_blank">📅 10:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88147">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇷
🇮🇶
أخوّتنا قوّتنا  مع الزيارة الأولى للدكتور محمد باقر قاليباف، رئيس مجلس الشورى الإسلامي الإيراني، إلى العراق، وبعد المساندة المخلصة والمضحّية التي قدّمتها المقاومة العراقية في الحرب ضدّ أمريكا وإسرائيل، وكذلك التشييع المهيب لقائد الثورة في العراق، ستُفتح…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/88147" target="_blank">📅 10:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88146">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BE80_bkfoHgol5fWwnbsbMHfIO0rXGtLXJ_ufJLPXemswIwxprvy8yInpwG9_EjYLgn_kCuWIRUVo1J6HZ_moxZgQQqzX8CJkan_mjtA8MkoG7essR4PkmdxD0lqWV_P4XmjcsJ3DJC0usXIqIaTSjpoiZT3lHvjrdsRKx0trsqjOpuFkwkkKPVgRIvjQoEmoy20u4djAwZ5ylbu_lB1CY5y4z31cHg4c72OC40tODoetKu0I3CvWzM-vNWAwYseIyH9zpJi6TmA53Uw9CoMcCsmJIbBL2Ozyn3GHckOsHNJhB53HkL1QxffzuMEsMF0ZCIX6yFm9uHeG9Aptj29hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
أسعار النفط العالمية تستمر في الإرتفاع وتلامس 92 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/88146" target="_blank">📅 09:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88145">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نايا - NAYA
pinned «
رئيس البرلمان الإيراني   يستخدم مصطلح نايا الذي أطلقته امس ليلا ً  " اخوتنا قوتنا " ليطلقهُ رسميا اليوم من بغداد ..
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/88145" target="_blank">📅 09:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88144">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇷
🇮🇶
أخوّتنا قوّتنا  مع الزيارة الأولى للدكتور محمد باقر قاليباف، رئيس مجلس الشورى الإسلامي الإيراني، إلى العراق، وبعد المساندة المخلصة والمضحّية التي قدّمتها المقاومة العراقية في الحرب ضدّ أمريكا وإسرائيل، وكذلك التشييع المهيب لقائد الثورة في العراق، ستُفتح…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/88144" target="_blank">📅 09:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88143">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65250e4c36.mp4?token=ecTxvsxmS_a5cDil7vmOHHPXM49rroM10L731kIQVB5WG2EmBQTF0JUrHxjT9xwnoZ5yQ9sVgVnLK1dMGVLJBsAOQyqpWSlGJUgGvlbx_EveI61eVxznx7L3pDNToHDgSYL9oWWzsWqTXF5roMPFvhLVOww0JzaEth-Ol4-KFtzPTyVhZMhZ8U6G7wi-YBAFvqZPJQ8j5M23krHCmUbW7iNrqR8zTSIu3xyWXu2M0fDORRjV9aA9YYggBCIFStqSha-1JE3xkSTN0RjAQOEz1I1jLGNFfF2gVjuS-AKMvNlEdEK7MZk-NoKNU1urE5FhoHAhAt5-GNxOwaMAZ44kcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65250e4c36.mp4?token=ecTxvsxmS_a5cDil7vmOHHPXM49rroM10L731kIQVB5WG2EmBQTF0JUrHxjT9xwnoZ5yQ9sVgVnLK1dMGVLJBsAOQyqpWSlGJUgGvlbx_EveI61eVxznx7L3pDNToHDgSYL9oWWzsWqTXF5roMPFvhLVOww0JzaEth-Ol4-KFtzPTyVhZMhZ8U6G7wi-YBAFvqZPJQ8j5M23krHCmUbW7iNrqR8zTSIu3xyWXu2M0fDORRjV9aA9YYggBCIFStqSha-1JE3xkSTN0RjAQOEz1I1jLGNFfF2gVjuS-AKMvNlEdEK7MZk-NoKNU1urE5FhoHAhAt5-GNxOwaMAZ44kcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
قاليباف:  في حرب رمضان، أدركوا قوة صمود إيران.  المقاومة في العراق هي إحدى الركائز المهمة ونقطة قوة لهذا البلد.  المقاومة تجاوزت حدود إيران والعراق والمنطقة، وأصبحت عالمية.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/88143" target="_blank">📅 09:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88142">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3e6b038ce.mp4?token=ZOJNNuKExav3TvEw7pLSUmtaHISOwiQEzsXLz0IHR-8KlE86pORm4ULHrUhAqIDhbrqyaB3cHYWE97YPsePeIL7r-T9QDEcnjsBMq-x2N7wZIuXoognwumhmqinJrslRGZ14XTHuEa5PN_xG37iu-NvlAUlY9kFjOAOpceSB8XolGnXfWQVNdf4mKvHtwaTDjmxPJyR6lAQMlzqbX5q6OcFyaDPFxq7Ys9p_qdfWnXo2wqoBPJZBpa59LwHj36uvTzlKXKHYCT6lMxAmqU-8FEBod00-Hls3mIFS5SA81dEKrYyiasWObi5lgftgzgMaBonN8a2301n8V_xPrjJ_Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3e6b038ce.mp4?token=ZOJNNuKExav3TvEw7pLSUmtaHISOwiQEzsXLz0IHR-8KlE86pORm4ULHrUhAqIDhbrqyaB3cHYWE97YPsePeIL7r-T9QDEcnjsBMq-x2N7wZIuXoognwumhmqinJrslRGZ14XTHuEa5PN_xG37iu-NvlAUlY9kFjOAOpceSB8XolGnXfWQVNdf4mKvHtwaTDjmxPJyR6lAQMlzqbX5q6OcFyaDPFxq7Ys9p_qdfWnXo2wqoBPJZBpa59LwHj36uvTzlKXKHYCT6lMxAmqU-8FEBod00-Hls3mIFS5SA81dEKrYyiasWObi5lgftgzgMaBonN8a2301n8V_xPrjJ_Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
قاليباف من موقع استشهاد الحاج قاسم سليماني وأبو مهدي المهندس: لقد كانوا أبطالًا أنقذوا العراق وإيران والمنطقة بأكملها من شر داعش.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/88142" target="_blank">📅 09:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88141">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7fe5e0325.mp4?token=VvaXprgzSfAJQxw-vy9HFh9YLKUf-l6MwlCjNqdOQCHxgDMqh67MPGxagVz1qIPexyYDZJlv_-ptA7oe9NINuLvTsvUSSdudrwqr1KpSIaBMwJ_eAgPmVIxQdPyp8dHIhR0u_xDGbOdFrmLdSF41_J11YbhIpH5vfh95612VDQyZPQzjUnlhwPcAKdLHI8frHwc0VrKG2Sc7u2P5dL4U33ySVCw6V3LmPJsqd0dLL3Rz1orzNY7QzxOHsNb8c8waYn3Z70z_V8nZ9_gWmfBKvtl1Rv8i5jTozBz6kOLqNooT6CGPtpOMdCkn0JP6m74CndPE74goXI78dXOtjuafeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7fe5e0325.mp4?token=VvaXprgzSfAJQxw-vy9HFh9YLKUf-l6MwlCjNqdOQCHxgDMqh67MPGxagVz1qIPexyYDZJlv_-ptA7oe9NINuLvTsvUSSdudrwqr1KpSIaBMwJ_eAgPmVIxQdPyp8dHIhR0u_xDGbOdFrmLdSF41_J11YbhIpH5vfh95612VDQyZPQzjUnlhwPcAKdLHI8frHwc0VrKG2Sc7u2P5dL4U33ySVCw6V3LmPJsqd0dLL3Rz1orzNY7QzxOHsNb8c8waYn3Z70z_V8nZ9_gWmfBKvtl1Rv8i5jTozBz6kOLqNooT6CGPtpOMdCkn0JP6m74CndPE74goXI78dXOtjuafeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
قاليباف مخاطباً قادة النصر:  أبو مهدي وقاسم الأعزاء. انظروا إلى ثمار جهودكم ودمائكم الطاهرة.   اعلموا أننا وجميع المؤمنين بمبادئكم في إيران والعراق، لن نتوقف عن العمل حتى نحقق أهدافكم، ونحن على استعداد للتضحية بأرواحنا وأموالنا وسمعتنا في هذا المسار المقدس.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/88141" target="_blank">📅 09:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88140">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇷
🇮🇶
رئيس مجلس الشورى الإيراني من موقع استشهاد قادة النصر:  العراق دولة مهمة في المنطقة.  الحكومة الأميركية اغتالت البطلين في محور المقاومة اللذين أنقذا المنطقة من "داعش".   في هذه الظروف الراهنة الكل رأى قوة مقاومة إيران في حرب رمضان.   اليوم الجميع أصبح يعرف…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/88140" target="_blank">📅 09:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88139">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بدء المؤتمر الصحفي لرئيس البرلمان الإيراني عند موقع إستشهاد القادة بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/88139" target="_blank">📅 09:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88138">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUACGcuSHBXpDkVGPCzibhys2vqZjzUeINNpxOZoL0sIwgBmXMSt-YV-vQGkUjznVvH8i7BU86zXFaRDPxnuzgYUcjXLwNFsOVYC3f_1HNEHbYAHVqFbmJ2dgdLncshlOM5blrNWDOquJH2EuSOstRB7X4fZVBxqnT4dwdDOZWsFgceyfG8xHCd-riJYKEunjhdYpMPAWyKGcqkkOSvvvnxWwReHkFNna1eUnL5ml0HAjoHtsGKSNMz8CpCYz8FCcETEueUh_kXHbHiCpeAQ1PlrYQJ110l9ywhUsySNrYO-3piJkYib9MKmAP7O6nZh8TntURYSK84UIrUYamaYjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رئيس أركان القوات المسلحة الإيرانية:
الدول الواقعة على ضفاف الخليج الفارسي الجنوبي، التي تصدر بيانات مختلفة تعلن فيها أنها لن تسمح للولايات المتحدة باستخدام أراضيها ضد إيران، يجب أن تعلم أن لا شيء يفلت من أعيننا.
من غير المرجح أن يتواجد هذا العدد من الطائرات العسكرية، وخاصة طائرات التزويد بالوقود، في القواعد الإقليمية دون علم الدول المضيفة.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/88138" target="_blank">📅 09:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88137">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cO-V7xgnymsSIB9f8N9MmnKbUP4hoM1Pk-Zq_Ua8YeenmYbJZo8lGExSmk2K2QgEJgjjLtx72efDceA22aVfNglQ4YCtv2rUqR0Rh9Eh0OrseuO8LbR5eFvw4DSg8momAfILy23xniLR07uIvvnN4UoESTFkoWuezH1WfYEbJ-I4X85JWbzP33YqC_NSxw6v1SmtBA9BlHJ2lhWfz5noKq7z3Za8SxD_DvOwrE--JE4lqJ8UITnq3ZoFN-gv-zjYA5SVB1-MmutNg1bfnCZbbVRUeuJ9deFWNzGmTdm7ygLlKzsepmDs6juj6NFnx_5c2iZCaAoIIRgGNU1nbYTkgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وصول قالیباف إلى مكان استشهاد  الحاج قاسم سليماني والحاج أبومهدي المهندس بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/88137" target="_blank">📅 09:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88136">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdd61bb885.mp4?token=Nysa8S523Iqq_M7yvzfroUb0hhVStV3_laE8uq6-g6Qpu27S1XVFP9ivNS3lCve-Jvp-nkjOX-qfbXQF0SVZkXSQtDYSzfZrWA_XblQb7iuRlnHntMMlwjqNrdAkBMlHUQExVJzgEp99Dc8hnHvu2WxXA6k0zD5bgu-oQud1gZ_KAtQRFF_vTFWGHvnzBq__SaUtEhByHOJQKmE9LEZEQmsUChL57Xnfa2KMuZDayPYrw4Ghl4DRcGb2xVTYeqILNB9vPrq8Bq52zEc522tuXazdL3KwqYVx7nNLd1wrWaCOi75I60mNdfIp_--uRyoAjPMqstVCRn7LnmEdRWO_AIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdd61bb885.mp4?token=Nysa8S523Iqq_M7yvzfroUb0hhVStV3_laE8uq6-g6Qpu27S1XVFP9ivNS3lCve-Jvp-nkjOX-qfbXQF0SVZkXSQtDYSzfZrWA_XblQb7iuRlnHntMMlwjqNrdAkBMlHUQExVJzgEp99Dc8hnHvu2WxXA6k0zD5bgu-oQud1gZ_KAtQRFF_vTFWGHvnzBq__SaUtEhByHOJQKmE9LEZEQmsUChL57Xnfa2KMuZDayPYrw4Ghl4DRcGb2xVTYeqILNB9vPrq8Bq52zEc522tuXazdL3KwqYVx7nNLd1wrWaCOi75I60mNdfIp_--uRyoAjPMqstVCRn7LnmEdRWO_AIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
لحظة وصول رئيس البرلمان الإيراني محمدباقر قاليباف إلى مطار العاصمة بغداد وإستقباله من قبل المسؤولين العراقيين.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/88136" target="_blank">📅 09:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88135">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇷
🇮🇶
رئيس البرلمان الإيراني محمدباقر قاليباف يصل إلى العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/88135" target="_blank">📅 08:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88134">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ebabbf606.mp4?token=Pe0P1st5W0LnxqiyyvZ5Zq7pYlHTuI1JjARNkJGjly_nDJqJAna1wMo7B-feNFiTiDgcUtmDhnZqoMaeTLwZrxAeCm9TCOvxm2SwU3luLQknxuDjR6W5fZDHs4nF9JrTjqTdZvgX6JmiTFgB65Ov-r3iy3jSBMZ8KmzbvIrdeIFltW59FSgp1Dep47toYGiWfROAlAZ6z9rO-B7jC4nDADN0wDNzRNtpFNEVS_TzeLJpe88Vri7-J8p50PduVmGCM8o6oPX5tEYNE2CFmObaYW6ldxDOk2vntJiiHZlaTJEmiYthlxCdE3PUbr_J9KjQ9JMy4nZ9trALBqUg2TWARg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ebabbf606.mp4?token=Pe0P1st5W0LnxqiyyvZ5Zq7pYlHTuI1JjARNkJGjly_nDJqJAna1wMo7B-feNFiTiDgcUtmDhnZqoMaeTLwZrxAeCm9TCOvxm2SwU3luLQknxuDjR6W5fZDHs4nF9JrTjqTdZvgX6JmiTFgB65Ov-r3iy3jSBMZ8KmzbvIrdeIFltW59FSgp1Dep47toYGiWfROAlAZ6z9rO-B7jC4nDADN0wDNzRNtpFNEVS_TzeLJpe88Vri7-J8p50PduVmGCM8o6oPX5tEYNE2CFmObaYW6ldxDOk2vntJiiHZlaTJEmiYthlxCdE3PUbr_J9KjQ9JMy4nZ9trALBqUg2TWARg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
أخوّتنا قوّتنا  مع الزيارة الأولى للدكتور محمد باقر قاليباف، رئيس مجلس الشورى الإسلامي الإيراني، إلى العراق، وبعد المساندة المخلصة والمضحّية التي قدّمتها المقاومة العراقية في الحرب ضدّ أمريكا وإسرائيل، وكذلك التشييع المهيب لقائد الثورة في العراق، ستُفتح…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/88134" target="_blank">📅 08:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88133">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇷
🇮🇶
أخوّتنا قوّتنا  مع الزيارة الأولى للدكتور محمد باقر قاليباف، رئيس مجلس الشورى الإسلامي الإيراني، إلى العراق، وبعد المساندة المخلصة والمضحّية التي قدّمتها المقاومة العراقية في الحرب ضدّ أمريكا وإسرائيل، وكذلك التشييع المهيب لقائد الثورة في العراق، ستُفتح…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/88133" target="_blank">📅 08:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88132">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇰🇵
جمهورية كوريا الديمقراطية تدين التدريبات العسكرية المشتركة بين الولايات المتحدة وكوريا الجنوبية.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/88132" target="_blank">📅 05:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88131">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇸🇾
دوي إنفجارات مجهولة في مدينة طرطوس السورية.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/88131" target="_blank">📅 01:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88130">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/88130" target="_blank">📅 01:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88129">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kg8LFFSy1IPnels9e4MMAmxJctZIOWkzJUUdvtfExv8vVmTwpmsBqZYnBcokVcOWlgPZNAoUdu2SxRHpnf4uHcGDQVrWYG0Ub3ptnC0gNJyC10KQfezRKIIneTpfNdU30lPtn0yt3CF_e6nLvYDE06vHUBBC-_Xk2-3fzsJay1yV_D4WOUZDsy3f0qGnKn7uFmG3de4aeW1oIhu3VK4kvxGEw2sebBDgkwrMkg3I_ooK4JCNUH0rzXtoSrDH0wAXjoczF68pW4Lt2j4Fzx2Wt103ia-DyZ3sqPlnuApYf0FpJcZd1rncq5Sqe92_oxUWdT2qVG41SLWu817BM8XzMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
أخوّتنا قوّتنا
مع الزيارة الأولى للدكتور محمد باقر قاليباف، رئيس مجلس الشورى الإسلامي الإيراني، إلى العراق، وبعد المساندة المخلصة والمضحّية التي قدّمتها المقاومة العراقية في الحرب ضدّ أمريكا وإسرائيل، وكذلك التشييع المهيب لقائد الثورة في العراق، ستُفتح صفحة جديدة من التعاون والتآزر بين البلدين الشقيقين.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/88129" target="_blank">📅 01:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88128">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d822181f0.mp4?token=nST6bdCDZBmGA3tggIkq6vTX7QadpBucmQ-7GBUTi_4XIw7Tdsh-cLBGD1qioswEYRZ78gt5w2iNWEav9P2-LKwgA0KuyisQ5zM2n16lSvRCmRR7cmzdQpIKDXAtTFl9vxsg05nkrSRihPQNmVrpwpB_e5J1EilmRYt88u0mSZinCcmIYeC5TB91IMQWaV22xPdx0GNJ9W5fHe5k_7-KD8C3KUpN8aY1URlp3gpttXJ5gpDFzQhUkz5wdwWNs9g36vog_7iJ2yLkGHV6GgCBI3-eVkP8qsdhQAnz12b2oGmvPBgcTcgWRR-OM0Q5jUaEKeuUhpGRqU9F7zKrvART8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d822181f0.mp4?token=nST6bdCDZBmGA3tggIkq6vTX7QadpBucmQ-7GBUTi_4XIw7Tdsh-cLBGD1qioswEYRZ78gt5w2iNWEav9P2-LKwgA0KuyisQ5zM2n16lSvRCmRR7cmzdQpIKDXAtTFl9vxsg05nkrSRihPQNmVrpwpB_e5J1EilmRYt88u0mSZinCcmIYeC5TB91IMQWaV22xPdx0GNJ9W5fHe5k_7-KD8C3KUpN8aY1URlp3gpttXJ5gpDFzQhUkz5wdwWNs9g36vog_7iJ2yLkGHV6GgCBI3-eVkP8qsdhQAnz12b2oGmvPBgcTcgWRR-OM0Q5jUaEKeuUhpGRqU9F7zKrvART8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇱🇧
غارات اسرائيلية على الجنوب اللبناني.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/88128" target="_blank">📅 01:21 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88127">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇺🇸
🇮🇷
الاعلام الاميركي: ترمب طلب من كبار مبعوثيه وقف محادثاتهم مع إيران</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/88127" target="_blank">📅 01:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88126">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇺🇸
🇮🇷
الاعلام الاميركي:
ترمب طلب من كبار مبعوثيه وقف محادثاتهم مع إيران</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/88126" target="_blank">📅 01:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88125">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmcowgkjslLqfSR1XkWfj8D8KCt9E9LkbBlqInoCZPX_ffMPGH8CEV_LlO6WlekYxOAAjQUPVOFNNwdUB3LphiDOFCFVxUXEC4HngeO7RNLuDvfI0nEHy4oJ7KC2RIBcuMZDS5B1fOHX3o1j_Xzty_7Z147kAfvKqegm8PoXNPSTH2MYFwrzqjK_rA-SSd888Kob8TiLc9Yx4CsxqnzIfqzyK_EvWfq0h_sdGTfR4gJpdq1Ck061K625FeTpaTeu5eMgr8BP3mAMnWDpabxOj_NDApvxDyKdqUAQEpdO5KgidLPQPrQ9sqilDx54s_XI5ZtBzoQLu1oyMZirkvXM5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
مالذي حدث في جلسة الإطار التنسيقي الأخيرة
اين الشيخ همام ابو إبراهيم في الصور ؟!
شكرا للمجلس الأعلى</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/88125" target="_blank">📅 01:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88124">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇷
🇫🇷
مواقع اوربية : فرنسا ستقوم بطرد دبلوماسيين اثنين ايرانيين ردا على اتهامات لايران بترهيب لدبلوماسيين فرنسيون في طهران
بیا بچه خوشگل</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/88124" target="_blank">📅 00:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88123">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇰🇵
جمهورية كوريا الديمقراطية تدين التدريبات العسكرية المشتركة بين الولايات المتحدة وكوريا الجنوبية.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/88123" target="_blank">📅 00:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88122">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية:
نرفض الاتهامات بإطلاقنا صواريخ تجاه الإمارات.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/88122" target="_blank">📅 00:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88121">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aea4713aad.mp4?token=PZxeDN610PeigCTT-vOmrQC6Izh1_l1TxGHfz1ZN2_UiNdZTvC0HxORWOfbLTZD4hGNN821Isor2ez898oQRJpD32rfhWRChQVMKQ1O-mHcY4QBWfK-abP0SR3P4dtFnp7v-44qiVZVBa8U3ppTswG2tpffKysqIPxuliklCyAAbIfYBOWJHFhNI3iBZg9wQFG1MC2P8mcOY1_HDuniTKM6aIQTfYEORY82vtUWDrjN9Nx1YvPxlF9IgkMXZ620cW_uyX8Jx_rgm65vtDq6uxpb1XtSVyzP47LLQrPUJKQs4f3nqzzZeSXLLQjZ9kxKPrCchCxLB_mBKfzbCjfbKLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aea4713aad.mp4?token=PZxeDN610PeigCTT-vOmrQC6Izh1_l1TxGHfz1ZN2_UiNdZTvC0HxORWOfbLTZD4hGNN821Isor2ez898oQRJpD32rfhWRChQVMKQ1O-mHcY4QBWfK-abP0SR3P4dtFnp7v-44qiVZVBa8U3ppTswG2tpffKysqIPxuliklCyAAbIfYBOWJHFhNI3iBZg9wQFG1MC2P8mcOY1_HDuniTKM6aIQTfYEORY82vtUWDrjN9Nx1YvPxlF9IgkMXZ620cW_uyX8Jx_rgm65vtDq6uxpb1XtSVyzP47LLQrPUJKQs4f3nqzzZeSXLLQjZ9kxKPrCchCxLB_mBKfzbCjfbKLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇮🇱
إذاعة جيش العدو   بمعنى آخر، لا علاقة للهجوم بـ"تعزيز القوات الجوية السورية" كما ورد في بعض وسائل الإعلام مؤخراً، بل نُفِّذَ لإيصال رسالة إلى نظام أردوغان مفادها أن إسرائيل لن تسمح بوجود عسكري تركي على الأراضي السورية. كان الهجوم يستهدف التهديد التركي…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/88121" target="_blank">📅 00:14 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88120">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇱
مكتب نتنياهو: وافقت إسرائيل وسوريا على وضع قائم على "الوضع الراهن" في الأمور الأمنية، وهو الوضع الذي كانت سوريا على وشك انتهاكه بالسماح بنشر قوات تركية في قاعدة جوية بالقرب من حلب.  لقد حذرت إسرائيل سوريا مرارًا وتكرارًا من أن مثل هذا النشر يشكل تهديدًا…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/88120" target="_blank">📅 00:03 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88119">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇺🇸
توم باراك: تم رصد طائرات تتجه شمالا نحو أراضي ‌ تركيا⁩ وكان من الممكن أن تستعد للرد.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/88119" target="_blank">📅 23:56 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88118">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇦🇪
🇮🇷
‏
الخارجية الإماراتية:
وقف جميع الأنشطة التجارية والمعاملات المالية مع إيران حتى إشعار آخر.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/88118" target="_blank">📅 23:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88116">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو الاء الولائي- القناة الرسمية</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6ux7z5JKGV0tTtLTQN3pKqcwqZhGTYXp0rTXMMTCRkvWzzRPwbfftwSj-ewzJrdQv0YdYBxByW7XX4k0QHVDVGgn2h2UspMJIwLH9IJqIHjKfdK0SSdLtSzFDw7qPi-k-Xy9aLoTJCM5QgjzuLq45h7f9yUOj-huMn0_nohF-GyXHRm8Xfn0wJjcOfMkd4jttVI0KvG6fC704IadpkhLOUEk2OcKaoh90t7OT7fjlJBwkVu6McYz0674sV2Nh-uXkDe8NOZzwU-RDnx-5EltAOCYl-ca35Dh8nVFZXgiEPnPMUgefbW5V8Ozuz9cA8V0gPCHf04eYAcunsThj0Xiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">في بلادي، يُباع النفط، لكن ليس من حق العراق التصرف بأمواله، لأن هناك احتلالًا أمريكيًا لأموال العراق!
وطائراتنا كلفتنا الكثير، لكنها لا تحلّق في سمائنا إلا بإذن أمريكا، فهي تحتل أجواء العراق!
ولا تقبل أمريكا أن نشتري الكهرباء من تركيا أو إيران، ولا أن نعقد اتفاقيات مع الصين، وليس من حقنا إبرام عقود مع «سيمنس» أو غيرها لإصلاح وتطوير المنظومة الكهربائية، ولا هي تصلحها؛ يعني: «لا أنطيك ولا أخلي رحمة الله تجيك»!
الشعب يريد السيادة الكاملة للعراق.
فأين السيادة يا سادة؟!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/88116" target="_blank">📅 23:41 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88115">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
تسبب انقطاع التيار الكهربائي على متن مدمرة تابعة للبحرية الأمريكية تعمل في بحر الصين الجنوبي الشهر الماضي في حرمان طاقم السفينة من مياه الشرب والطعام الساخن والمراحيض العاملة وتكييف الهواء لمدة أربعة أيام.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/88115" target="_blank">📅 23:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88114">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇺🇸
توم باراك:
تم رصد طائرات تتجه شمالا نحو أراضي ‌ تركيا⁩ وكان من الممكن أن تستعد للرد.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/88114" target="_blank">📅 23:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88113">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">الإمارات
: الصاروخان الإيرانيان اللذان تم رصدهما اليوم استهدفا حركة الملاحة البحرية.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/88113" target="_blank">📅 23:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88111">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEqkk6ciD5uhMfQcOLqX6vyIW9neHrJK2OuPKqeZN-g5XVVnXQY5Cjkw_yHwPSRZ4Ja7QEy_qGTTsmGRKoS6gKARGowe_y6ofBYfl1C_jCBO3EpfWYIoVzuEONt6Xb7uDPAEpz_UKDL-gsJAdLI2SohyYavMiwv51pBgRVBQIvyGmLyWvqdiRuQhDhS8HvV-uqQDQVUN2dS14OMZ_CorJE_rqWoBRUXsSfr4y61ikjbtN6wU-AY7gkddMqfgZ_TFN4dj_ElcEqSn7tjVBYJvsIhg3CErHroMWttXSfIhNPBae-FI77oFe777QUnmMgkVoaJDbCvwfv1JevPwtX4IhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
إستهداف صاروخي لسفينة سعودية قبالة ميناء المخا اليمنية من قبل أنصار الله.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/88111" target="_blank">📅 22:42 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88110">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
عن مسؤولَيْن إقليميَّيْن: إدارة ترامب أبلغت عُمان معارضتها لأجزاء من الاتفاق الذي لم يُعلن بعد ويشمل إدارة إيرانية عُمانية مشتركة لمسار الخروج من مضيق هرمز.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/88110" target="_blank">📅 22:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88109">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EooZi1vY1pSZKOlu6sGewAYS-5LdQvrgaTFpbpBjy3vpRqr0p6Ml6QFtpjx-yFj1qqhxjGM5V2LYa9iswDZ2M52biSGtpLIlqai7ebTooosd1BdHyeBorwtyhUEHTDNWg_mUFchbf92hbaJWPBmsyBZLSutbhDIm0Loj6zRCtvLDh6q23WPVIDsM7FK1dU7vd4947d8-eSz-fBUl16x0s-K5g2kvE18bTt6BmGLxxtjCv1v7LFxDL_-3IU_WPJw25BZmgsK2W6sAI5aCGoCd3nJ58WqZIY6Ehn52wZRbCfEw0sZCl5LHkoEyBqQQ6khooZ0YnXKl-FDw6D1d3Pp5Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
ارتفاع العقود الآجلة لخام برنت إلى 91.02 دولارا للبرميل.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/88109" target="_blank">📅 22:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88108">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔻
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية خلال الأيام الأخيرة قبل وقف إطلاق النار تجمعات لجنود وآليات جيش العدو الإسرائيلي عند الأطراف الجنوبية لبلدة زوطر الشرقيّة بسربٍ من المسيّرات الانقضاضيّة.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/88108" target="_blank">📅 22:13 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88107">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇺🇦
🇷🇺
تنبيه الغارات الجوية في كييف والعديد من المناطق.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/88107" target="_blank">📅 21:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88106">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇺🇸
وزارة العدل الأمريكية:
توجيه اتهامات إلى 17 إيرانيا بتنفيذ حملة واسعة لسرقة البيانات عبر هجمات إلكترونية، المتهمون استهدفوا 144 جامعة أمريكية و178 جامعة أجنبية و42 شركة ووكالات حكومية.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/88106" target="_blank">📅 21:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88105">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔻
حزب الله: بالفيديو سِيري عَلَى اسمِ اللَّه</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/88105" target="_blank">📅 21:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88104">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMDe5F-QcSlSaK0IEWwdvR5ehQlA4s6ugTT4RAvB4tA4rr0uH55CGMRGXsgMI1zFq6PiNhSgl3MwdjN8wwZrV_DigzUCRnrri9jY69biWSJZBKa-WEMdkeR34dRJ2lTOsOScuLHdb4P3badTKu9plO4rg4D2Ch8AFplSn3-qi-vtuihgCr910jVjMsvXlsWEhTYP8WM7vw5yb0kuSW9DoezoukhOFYHDcFPmkSNLT4QcPTQWTX1eLE99m4coAEDbtnlZ_JwmzLZBU-mEFmGYzX0PXOKmFuAPoakHpeGzUpyyCNfxL3z6AlfhTky7IAi8Yo6YeaZ2YwVAXFA5crdC_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزير الخارجية الفرنسي على خلفية طرد موظفين اثنين من سفارة الفرنسية في طهران:
سيتم طرد اثنين من الدبلوماسيين الإيرانيين خلال الأيام المقبلة.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/88104" target="_blank">📅 21:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88103">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇾🇪
🇸🇦
إستهداف صاروخي لسفينة سعودية قبالة ميناء المخا اليمنية من قبل أنصار الله.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88103" target="_blank">📅 20:55 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88102">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YESug8b3ywsX8b-EXWmMj5q1HgbBcwZhbwd7fs7aZXTzZfB12xwlN6_zXiTkaqKKXwzd7Dsargt-JnQFRr-R9QNe006rcFdeYNeuy4xHgDEhev3H5wD7rnkNGCzEyS-FJweT_HmD5U6ZgCUBDZSYsjLn10t1tjA1GwqkXN3PWt6rn787hJL4drP5kQ-3X_MEWDIgsfI4e_OZSYaQUr2IeQYbCySrdRwiUsaI2i8e4gd1vsDnTjs8WTSGSCwAwPkPM0A7ScwOgwDKhtSZeeTAp92w8mVLsiUXibYF9m5xBsXoLe9aZIg--cvPkJNdrk3yliQjOLLyT6o6U3skmqoLCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
الولايات المتحدة تفرض عقوبات على رئيسة "المحكمة الجنائية الدولية" توموكو أكاني.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/88102" target="_blank">📅 20:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88101">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">#متابعات
🇮🇶
ازدحامات تشهدها معظم محطات الوقود في العاصمة العراقية بغداد بالتزامن مع فقدان البنزين المحسّن من عدد من المحطات ما أدى إلى توافد أعداد كبيرة من المركبات واصطفافها في طوابير طويلة.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/88101" target="_blank">📅 20:36 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88100">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2n3N8MeWg4OcyJLHYvldW5dRQm9Z9a8KyCow2qyiXijy6APmErIfq4EVsJrP2s7WDOICN1eiEm12UtFEKdr28knnwxvHx6M5pQzm_Nb4R0p2bKt1gywMXiCV0i2SW975RksMYdJMkUex0pZGxcOxEzA2TCy3vKF5rzXmpNLQJcPF1LJQXJkdo3urGcJEdBZmEZNNOYL_ttvTtKPv6mtWnRBxpKWWoWiQZNV8XG6nTA1i8wrOX1CiVLkt5e14tWOnnJLmxTjWCaRvSxwCl1VCWuNgLLlqYYXlsW8VVtOuRWCRV8PZAU_A4BmNogNdUYi7H4MDXIlJX-M80ytjjppew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالبياف
:
يعتقد الأمريكيون أن الضغط على إيران بشكل أكبر سيؤدي إلى انتزاع تنازلات لم تكن جزءاً من الاتفاق.
‏بيسنت وهيغسيث ليسا في مستواهم على الإطلاق. كفّوا عن انتظار هؤلاء المهرجين ليُخرجوا معجزة وينظفوا الفوضى التي أحدثتموها.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/88100" target="_blank">📅 20:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88099">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a206509c.mp4?token=W-oszVOITPqzuQWm8tEeY_iA-tcQWWNYiWtJrOlY8BBVrv202DCFJAK4nkiDhtL_bAoPdZv8KD-O2uo38L9GlVPM9plXXVn2og4oX3QW9eN3llKHVm-u9yfFRoZvFX3oVp4JYEe-yMPuJ8_xStT4xFp7lh3xoJOE5bbCK2WaS7wROhypMY-R2__y8_-yQ7_9dVbSl716GxnbWSwrvMQuMXC2u2lclao3ioPLP64mbtrUwnJ4JPrmgcs2KKOXNUzTWivWRaFspS_neLD1lTNUIGJnSJWvvhlkcnldOVgxU0oB8rD5fh_3JxTGump8tZMCCzdEkofPI_rMl6EPfgnnaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a206509c.mp4?token=W-oszVOITPqzuQWm8tEeY_iA-tcQWWNYiWtJrOlY8BBVrv202DCFJAK4nkiDhtL_bAoPdZv8KD-O2uo38L9GlVPM9plXXVn2og4oX3QW9eN3llKHVm-u9yfFRoZvFX3oVp4JYEe-yMPuJ8_xStT4xFp7lh3xoJOE5bbCK2WaS7wROhypMY-R2__y8_-yQ7_9dVbSl716GxnbWSwrvMQuMXC2u2lclao3ioPLP64mbtrUwnJ4JPrmgcs2KKOXNUzTWivWRaFspS_neLD1lTNUIGJnSJWvvhlkcnldOVgxU0oB8rD5fh_3JxTGump8tZMCCzdEkofPI_rMl6EPfgnnaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏انفجار هائل في مصنع فنلندي قرب الحدود الروسية</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/88099" target="_blank">📅 20:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88097">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y_XN8GOiANVwebFtGLAHjJ8nr8Hs2r3WBGJ61IwfrhT30MLSCf19D7OIRbAhqbDe9TkNjoRF1Fa1M0Zq_mf7s7RWcSSOkddEWBslfVzrZa8uZJGGKlRzKgoElEzk_xFd8V0mwXqmkXdAOD60s4Iywd8frrkSlkV8guxMyuCWK5lZDZziuzyv1yvlMPaGRPuOYl9VLSXjx_KQPUpifAMgydG5JGhhmuuTYiMVxS5RSwyb9y2z3u2TgVDZIQP_IhsThcS_ZVZxfZaG3hHxUM5oI9Fz0ECR4MxfMouV1MkP1TNojr5mlu5gnYfjFDb1EQ3qM_otNGiFSO8yF5JvB-HHoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fYZMQ8oQFL7B8yBBU5PcrCnpzmxhwChaOdaijdxR3bPRNPXhwlxS9YbPjtPjOmmX1sYiq-1UUzvywUKHF8r6_5jgpJu8x_2LBXiC5_UnSa2ub2QHBwvrypn7zKOhxZVUvIqIewW-mbEAy_LlnoyoP6iuDH-NaoaJL5flUSwouk0NAqChpaCmzS_MtoneMEjXtB3y9WgGDgKSp8DNqgteAKqSLnnaH5_BR3BD8ycRR0pe3ktt6kxs874k6ceKfGv-8RUEqkpUBbuvTMNNOSM_6ZeMyPkRwVMJ1v-M3hV_7E1q6JSeX2PgwpM22lOXVZMt32EnS64CcCnXnV2K9WBbvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
تسريب النفط الخام يضهر بوضوح من امام خليج عمان بعد استهداف عدة حاملات النفط لمخالفتها قوانين عبور مضيق هرمز.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/88097" target="_blank">📅 20:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88096">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">غارات اسرائيلية جديدة تهز مطار أبو الظهور في ريف إدلب الشرقي</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/88096" target="_blank">📅 20:13 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88094">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/897db561c3.mp4?token=iWha-UYNx3ijdU4psptJZPOeF4MbG4MquOXY0HBd4lIlkbrdSj86GB1Yq_NcqFDcxogW1Bfm-U9yi5-lrFJhzNYsWkBdrg2-LFo84czL7jYeN2YRkTaZXKEWwnur9B68Fq-4Q6F-bKwQi9qHlEQDg0iX9Xb64Ag5Loj5JVcsy29tLej03X4xlGp1OTl0qgDqbjHFFBubtQv06k9CDLbgoTGIPUV-MNxmpQBVuxbVg70QMn7COsLfIy-3FRfbp3Uv0ahqNjaaqsl8cGxdwLfIyJyKKexViihDulxdhvwMTA7qsrFP06Esm-MJDwZQq-yoOg1WSgTa21Y5-9mGi-_iiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/897db561c3.mp4?token=iWha-UYNx3ijdU4psptJZPOeF4MbG4MquOXY0HBd4lIlkbrdSj86GB1Yq_NcqFDcxogW1Bfm-U9yi5-lrFJhzNYsWkBdrg2-LFo84czL7jYeN2YRkTaZXKEWwnur9B68Fq-4Q6F-bKwQi9qHlEQDg0iX9Xb64Ag5Loj5JVcsy29tLej03X4xlGp1OTl0qgDqbjHFFBubtQv06k9CDLbgoTGIPUV-MNxmpQBVuxbVg70QMn7COsLfIy-3FRfbp3Uv0ahqNjaaqsl8cGxdwLfIyJyKKexViihDulxdhvwMTA7qsrFP06Esm-MJDwZQq-yoOg1WSgTa21Y5-9mGi-_iiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مقتل ستة نساء كحصيلة اولية نتيجة حادث عنيف قرب مطار المثنى بالعاصمة بغداد.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/88094" target="_blank">📅 19:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88093">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">إعلام أوربي يدعي :
تقوم روسيا بشحن المتفجرات ومكونات الطائرات بدون طيار والذخيرة إلى إيران عبر بحر قزوين لمساعدة طهران على إعادة بناء مخزوناتها التي تضررت في الضربات التي شنتها الولايات المتحدة وإسرائيل.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/88093" target="_blank">📅 19:47 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88092">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇶
سوالف الگهوة
اكو نائب حليو صغيرون مجكنم ؛ البارحة المالكي غاسلة بالكاع غسل ولبس ؛ خطية يحاول يقلد ابو عمار مصطفى سند من جان مهاجم بالحادلة بس مجتي بيده ؛ عمو بعدك صغيرون بعد لا تعيدها …</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/88092" target="_blank">📅 19:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88090">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b6184389.mp4?token=EHaHW1KoTxKg5-rtREd6Pq5XhJOOV0ss4d7GqFSKw64LgRCtJQlZBMzqS4Y-N8EkKFnYSLadBJFBB2w8xP2biZS7JDaFxMEVI4OB2M_b6BgNVY_PJbebqz6_8xm-7zeoDHHKN1eZWvBj8dTJz9TQReIT0DLCJaWOWHZQLGwcKB3AkyIV5ZYQ9Bs5mH1P_0SzwWRqoP06nj2L7QsRbPn13N7w-b_UApkQb04TyrSiq2pfHFpcTobp4GiAOb0ZvCn5k-2JvzSUwAax7mv0Z7xHEKsyvowDl3lKsxffU5vySiP2uERELMIO5Ahv35ZeNdYAX19FcajrYjIe-wgX2qR-fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b6184389.mp4?token=EHaHW1KoTxKg5-rtREd6Pq5XhJOOV0ss4d7GqFSKw64LgRCtJQlZBMzqS4Y-N8EkKFnYSLadBJFBB2w8xP2biZS7JDaFxMEVI4OB2M_b6BgNVY_PJbebqz6_8xm-7zeoDHHKN1eZWvBj8dTJz9TQReIT0DLCJaWOWHZQLGwcKB3AkyIV5ZYQ9Bs5mH1P_0SzwWRqoP06nj2L7QsRbPn13N7w-b_UApkQb04TyrSiq2pfHFpcTobp4GiAOb0ZvCn5k-2JvzSUwAax7mv0Z7xHEKsyvowDl3lKsxffU5vySiP2uERELMIO5Ahv35ZeNdYAX19FcajrYjIe-wgX2qR-fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان تشاهد من مختلف انحاء السليمانية</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88090" target="_blank">📅 19:20 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88089">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/352e85edac.mp4?token=Vw0B-D6yLvJ_OIkw3wj7U6TzGMhaFYI9b0ZiHCC7pGcV9FXrfRSuzkPsQxV9ulrl2XywrZtGxgnlsbMSTAi9KCDf_UJdPRZke6xlaTFPeERpl3lYHrW2ZTovQ9YHDLc337zArIz_ETSC2qP6VPKH4F0MFqwiOXZeSg3Df_0-uotD-pmKqnm1iaDOA31u555lBzpmQlRzSUayUsXr2Eu2iLr-efRDGLbhHtVf7GCoLmOFBpKIaGPFk7ji0EpuiD2NnScE-1YsHBfvSsEn6D38qXqKQU-qOOwUQm_iw0enhh3HKx3PeEqobsvPvX4jJgqtsTA3kMPUfGpGLBmTbt_MGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/352e85edac.mp4?token=Vw0B-D6yLvJ_OIkw3wj7U6TzGMhaFYI9b0ZiHCC7pGcV9FXrfRSuzkPsQxV9ulrl2XywrZtGxgnlsbMSTAi9KCDf_UJdPRZke6xlaTFPeERpl3lYHrW2ZTovQ9YHDLc337zArIz_ETSC2qP6VPKH4F0MFqwiOXZeSg3Df_0-uotD-pmKqnm1iaDOA31u555lBzpmQlRzSUayUsXr2Eu2iLr-efRDGLbhHtVf7GCoLmOFBpKIaGPFk7ji0EpuiD2NnScE-1YsHBfvSsEn6D38qXqKQU-qOOwUQm_iw0enhh3HKx3PeEqobsvPvX4jJgqtsTA3kMPUfGpGLBmTbt_MGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد كثيف لاعمدة الدخان من السليمانية</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/88089" target="_blank">📅 19:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88088">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17b671c100.mp4?token=H_bTnihsVHAOFzrLHZAnn96YbsB-RYnrEZyoIUAdQsw-pN_ugQl_wymSWJcEQtdKX--irrW70djncfGw2vwzmEv-4sk5C8iX_sfcJEvB4KnmcJNDESqHK5xrd24slY8hLzOAyTOlDyaf9oKThbJirIOinELi9zHSI6Caizq0nxB13WmJ5-EIezD6gwZccMeWKjLKY89IYwn3PzxaDXNyseYgPAssaYBahr__1IyXu-nLpd1ax2mZrccfP0ercWAuG-LFs3sTH7OLpGM0V9-uYQwo31wqPdv9fe0OeDSI5Kk4Wc_zVnuja_2tqu4H0aQNdz-tY2hrBw6_sNdh4HoJBF-jK-xpeO7qYu-wTbqrgclvrQy_JUL9CFP4baZQV7vQsIbtsrDNTIkIZQjp2rx6wqFB-xe6wbjG3XTFZbX9nPO9ivn_XscyvbOhA6t05yJV5aTUfyXMXhPZMPRiPM2Q85lXCSYpailRHuvqrqS8CvKcQuo3xOgwqL7kQU4CrspSr0b74Hs9anQxbyrjQzmUu3-gUy_6mtpiVfr4DU5_PRyEju80ItjCH8AphnvRKf06N4dJBdePfAmElh4KtiSB70C-doLUaJcpcciT0KNFzqoSHehTvrPtOIflNp4fCEuYozwSHVqURt_ttzNnPkG-FgmAFkpzGvyRziduAh_MPo0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17b671c100.mp4?token=H_bTnihsVHAOFzrLHZAnn96YbsB-RYnrEZyoIUAdQsw-pN_ugQl_wymSWJcEQtdKX--irrW70djncfGw2vwzmEv-4sk5C8iX_sfcJEvB4KnmcJNDESqHK5xrd24slY8hLzOAyTOlDyaf9oKThbJirIOinELi9zHSI6Caizq0nxB13WmJ5-EIezD6gwZccMeWKjLKY89IYwn3PzxaDXNyseYgPAssaYBahr__1IyXu-nLpd1ax2mZrccfP0ercWAuG-LFs3sTH7OLpGM0V9-uYQwo31wqPdv9fe0OeDSI5Kk4Wc_zVnuja_2tqu4H0aQNdz-tY2hrBw6_sNdh4HoJBF-jK-xpeO7qYu-wTbqrgclvrQy_JUL9CFP4baZQV7vQsIbtsrDNTIkIZQjp2rx6wqFB-xe6wbjG3XTFZbX9nPO9ivn_XscyvbOhA6t05yJV5aTUfyXMXhPZMPRiPM2Q85lXCSYpailRHuvqrqS8CvKcQuo3xOgwqL7kQU4CrspSr0b74Hs9anQxbyrjQzmUu3-gUy_6mtpiVfr4DU5_PRyEju80ItjCH8AphnvRKf06N4dJBdePfAmElh4KtiSB70C-doLUaJcpcciT0KNFzqoSHehTvrPtOIflNp4fCEuYozwSHVqURt_ttzNnPkG-FgmAFkpzGvyRziduAh_MPo0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من محافظة السليمانية بعد الانفجار المجهول</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88088" target="_blank">📅 19:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88087">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90c491d94.mp4?token=ihqmAL4ufnczuMZqeMZqrXh3LiLtnj9CLSJ0ofZhmvUDOcLi3RTLgVrkJZ27PN2DtUg5_2Hng90o1xA90Vk2bZt8Ns-6H4i1EOr8bA-Pm4ujKLU-L_2I3VwV8--p621jNdc76rFVWjqT8Ds-bXVSQR-XDGF_TAblPBDsk-Fj4qK_gDAnblImCT-PyZJsvIfTQpSDUTNCq2anglfKdApUOrOy9Nf-xHHB7mrVlUil1GrgjrDHUVk0fUKZ1dyENo7zzgv0-L1H6EewUL-7lupiObbgdMnZ7z5prGh1sln-8RvYU4DrwDoyclhJkdE14_B91N6Q-WyiFjd5zhbGB0yywQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90c491d94.mp4?token=ihqmAL4ufnczuMZqeMZqrXh3LiLtnj9CLSJ0ofZhmvUDOcLi3RTLgVrkJZ27PN2DtUg5_2Hng90o1xA90Vk2bZt8Ns-6H4i1EOr8bA-Pm4ujKLU-L_2I3VwV8--p621jNdc76rFVWjqT8Ds-bXVSQR-XDGF_TAblPBDsk-Fj4qK_gDAnblImCT-PyZJsvIfTQpSDUTNCq2anglfKdApUOrOy9Nf-xHHB7mrVlUil1GrgjrDHUVk0fUKZ1dyENo7zzgv0-L1H6EewUL-7lupiObbgdMnZ7z5prGh1sln-8RvYU4DrwDoyclhJkdE14_B91N6Q-WyiFjd5zhbGB0yywQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان تتصاعد من محافظة السليمانية</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/88087" target="_blank">📅 19:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88086">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دوي انفجار يهز محافظة السليمانية شمالي العراق تبعه حريق مجهول</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/88086" target="_blank">📅 19:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88085">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دوي انفجار يهز محافظة السليمانية شمالي العراق تبعه حريق مجهول</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/88085" target="_blank">📅 19:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88084">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1gyxX7d5vUhrGT04dz2s1RXTPxCuFxWPH5VbsrkTIojXhXyVaBBJtXTGlwhurmurFxYmosQA6Q8569UdCXRDsrEK94CSltgIYeeRn2bsJanEfSWJzXvy_g1w8s7z83L2dJXc1HP35_5JBrt7CoA5PvmY7UUMQVCr7vAPvRvLUtdFq5ySVPsC4SFK6AjDXa72THU_V5uWtQnLnwogeLM4n_GgDDL1DSH-y-mboGJ8zfGd2x2Cvx8kidz2pPgrI7k0U1xL8FIrhJLV-ZqRhnu6ieoRoKRRtW-6feUOYivsH94U_TqVcOnYiuxv1VJkX4FUNNLGIVpkCiGNumrq_Dcxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
منصات مقربة من حركة أنصار الله الأوفياء تدعو لوقفة احتجاجية في بغداد يوم غد ضد الفتنة والدعوات الخارجية التي يفرضها توم بارك حسب تعبيرهم .</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88084" target="_blank">📅 18:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88083">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">واشنطن بوست:
الولايات المتحدة تدرس تقليص وجودها العسكري في الخليج بمجرد انتهاء الحرب</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/88083" target="_blank">📅 18:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88082">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9cf316785.mp4?token=kZMECf2eEjfRcuxv7oxsgHK42u0Q4BguyQId6JgwFq7ZeY3FLF2PmTvJlGn9NEt_rmYNuQpg01fq6giOd24koLFQItF3EDGoJU-yz62iHAyEl7ps8PoPqObOqZ_I6sQ_yScT1X25VKh2j2IO-ClmcNYGkAeEPr3cRAz-RgRlaRKNcuQdMNhC4Umu5IBhSd9WuLELV4_34REBEVaBKyiZP5m-T6HI4kIhg9nQ2mUbJRPAbfKueSsKJ1WhuulsSMi_ns-quKqIT5uJrmRwuEIEiObaHbG-ZZPbR6I-sXovfMYZg0GupHe11V0en93WRxcdummElO6rhHteivq-JnkdVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9cf316785.mp4?token=kZMECf2eEjfRcuxv7oxsgHK42u0Q4BguyQId6JgwFq7ZeY3FLF2PmTvJlGn9NEt_rmYNuQpg01fq6giOd24koLFQItF3EDGoJU-yz62iHAyEl7ps8PoPqObOqZ_I6sQ_yScT1X25VKh2j2IO-ClmcNYGkAeEPr3cRAz-RgRlaRKNcuQdMNhC4Umu5IBhSd9WuLELV4_34REBEVaBKyiZP5m-T6HI4kIhg9nQ2mUbJRPAbfKueSsKJ1WhuulsSMi_ns-quKqIT5uJrmRwuEIEiObaHbG-ZZPbR6I-sXovfMYZg0GupHe11V0en93WRxcdummElO6rhHteivq-JnkdVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
قوات امنية كبيرة تدخل مدينة سامراء شمالي العراق لاسباب غير معروفة.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/88082" target="_blank">📅 18:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88081">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇶
خلية الاعلام الامني العراقي:
ما يتم تداوله من قبل البعض أو تضخيم الأجداث بخصوص 30 أيلول هو توصيف غير دقيق ولا يعكس حقيقة المسار الذي تتبناه الدولة.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/88081" target="_blank">📅 18:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88080">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">انفجارات عنيفة تسمع بسماء منطقة بر دبي</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88080" target="_blank">📅 18:33 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88079">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دوي صافرات الإنذار في دبي</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/88079" target="_blank">📅 18:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88078">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دوي صافرات الإنذار في دبي</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/88078" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88077">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">هجوم صاروخي على دبي</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/88077" target="_blank">📅 18:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88076">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRdosakbMm_fPMlXAq_v1gzazJ8wM__uNaRi4F_40XMjtWgY7qI6T-5S0UBAF72CHVTAVrHWCAJs3KgbgiykxF_yPrV5h7Ubf4pMYqwClNojWbZpM17zh7xNSo9hb5cofXNBmfkkOtQA8gs5O4raVSXB_hcYxagj8XRWcRXgWwFyrVmW6s_YeN_xYsoq4rxqHiZACUvOGNTlt5xxtdQl_Bnz_oWJpuGRNwZCwvZeDu-M7dNycPmJ1GzPsnTb-0PgWwmdm9lBZQm_VgjvRdByZBb3ESJwHNY9G5vyQGZFqnr2RtrwCFPcuhVe-4_znJObWzElad9BM0F9f3hTFTCGkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوي صافرات الإنذار في دبي</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/88076" target="_blank">📅 18:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88075">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دوي صافرات الإنذار في دبي</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88075" target="_blank">📅 18:23 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88074">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">حدث بحري قرب سواحل عمان</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/88074" target="_blank">📅 18:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88073">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/88073" target="_blank">📅 18:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88072">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">حدث بحري قرب سواحل عمان</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/88072" target="_blank">📅 17:55 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88071">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VA43BM8fCNiQdtQCRihtWGME5fh3CPjNiVW7TRVsF7kS8xwsAkWExq6lIdmLW2zLNO7uXqtP6Mk4TIB8IODZR7YCuM4pfdqOL3n84B4SD5lvtLxoydRGipJwL9TdtLRuXwRBk4pzoOKreN2o8BXWiu7O9RWayHw6rdS8ikMiDs-PKz7epvO6giGENV9ZALvJkzo5mVL_6qIpHE8KCz315SFWANKIMmKiXCyKq_vmh9SMxLHy1ArtEL4KDi157_Ko2eUwe1v2hlkwGI9juZ4OcZjcrLbOqwzdLS0uEuThg-YYuYbn2pIawBWTT8IA8Ou5ZvRuJLT7eOsE8rqHJa9oUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث بحري قرب سواحل عمان</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/88071" target="_blank">📅 17:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88070">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏مدير الوكالة الدولية للطاقة الذرية: تم العثور في سوريا على أطنان من المواد النووية التي يمكن استخدامها استخدامًا سيئًا.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/88070" target="_blank">📅 17:26 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88069">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">الكويت تقول ‏ان ثلاث مغذيات فرعية من محطة التحويل الرئيسية الرميثية (B) خرجت عن الخدمة .</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/88069" target="_blank">📅 17:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88068">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfZcIXsj6UwLV0SegijR_0hxGq6pCHVbtkpwYnR1Zb2ECS4vS3MJTtL10QYZenQ9vbEX9V74QwNUIDagOcW2yzmGs_qPTFQunCopLfQ6e3QbpQU02a0MUdEFMVlfcZZ1O_QTOnMk_N1f9bSxKXs_6TwblQolrJEy0Wb5vN4t8lGuBkd06DcGZ_9DgLrVjqqIYcskAjnyEBc11CZhMpnA4qDiM32mtPDGu5QBlKnxGj40Mz8kjkfgR-MKZHgdUtiah5rblrGSXZFOKlMPdZJDGbDejCaMw7ii3xy8RztPxgEHHbuKujRHEZPYcjXhRSA7zs-bWKy3soXD_ZlSw-qqJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🌟
‏
ترامب:
لا توجد أي محادثات أو حوارات جارية، أو مُجدولة، مع الجمهورية الإسلامية الإيرانية. الحصار البحري لا يزال ساري المفعول بالكامل. مضيق هرمز مفتوح ويعمل. جميع الألغام المائية قد أُزيلت أو فُجّرت.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88068" target="_blank">📅 17:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88067">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">الوكالة الدولية للطاقة الذرية:
انفجار لطائرة مسيرة في محطة زابوروجيا للطاقة النووية الاوكرانية، وذلك في حوالي الساعة 06:00 صباح اليوم. مما أسفر عن 16 إصابة، بما في ذلك وفاة شخص وإصابة ثلاثة آخرين بجروح خطيرة، بين العاملين والمقاولين. ولم ترد أي تقارير عن أضرار تتعلق بالسلامة النووية أو الأمن.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/88067" target="_blank">📅 16:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88066">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇸🇴
النائب الصومالي عبدي حاشي عبد الله: أصبحت الصومال ساحة معركة بين إسرائيل وتركيا.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88066" target="_blank">📅 16:47 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88065">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">والي العراق والشام توم باراك: ‏ نشعر بقلق بالغ إزاء الغارات الجوية الإسرائيلية المؤكدة على قاعدة أبو الظهور الجوية، والتي تشكل تصعيداً غير ضروري لا يساهم في تعزيز الاستقرار الإقليمي.  ‏لم تتبنَّ حكومة الشرع موقفاً عدوانياً، ولم تُبقِ على قواتٍ بالوكالة. بل…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/88065" target="_blank">📅 16:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88064">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇶
🔻
حماة الأرض .. حشد الأرض
مستعدون للدفاع عن العراق امام كل خطر</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/88064" target="_blank">📅 16:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88063">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5Q94UAehyZzL8G3BKf0IrS8Ru6KGMSYVW_p_O-NCD28jldfogLY9mixs4sJKELMbqZuzcJgkeWfJltw_zccdO3sQi3E508nM41uSRwq7DY6XVjmCKUfzdN_26FQ-hCNApCf8qYt0p1RuOwpcinjUid4M__crhjP5tXg7oaHThwIFMhoxXv8xmChJE0Jz4sCocqVGCV2QJL4JH53Sx1SYlFUvL_NX2OI60yijJgNZ9Fh_z7Ydow0wiMNcMARblHAIBoapnTXUauYWtDRLjwhOdjn6ryFHN64XDKxZKc6uYkCt-WP-6thouEXka6msswpfKmiHEclaVzohBrVerTCTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مطار أبو الظهور بعد الغارات الاسرائيلية</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/88063" target="_blank">📅 15:09 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88062">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryu33XsPoAvah_XurNR-x1q-w5-wyX1CUSGpE29qAoQs9qA9ylxwiV5J-3Ymwlq_2nlmzAMbg87yi_YJVNMwHFbZicbyDAQdNyxiyw0qTfEWCVDL37an1AQLMnxe4vWbBfkwL3PFvlLcIdSMY3RY3hwpSwOBFFoiOAz4HvbURVrtVgWXhrYY8Wd0ztyuiBbHnKsu8HlIm1WOYEdM6qo1AbsZ8xhkqltO5JT1By5kOw0rpgBkFT5eaAUNmcap2thHubShgjkEQo5vf0l-T6jjO0EmzK4c0v7osKKHj2hRs36UFKzhuqYxMzZ-EMFxSdpxwtHUQHohTEv3MN80HFAc6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد من الغارات الاسرائيلية على ريف ادلب</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/88062" target="_blank">📅 15:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88061">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/452a2d8719.mp4?token=Tugnx4aRbZUMLj9RD-SVYZEWs9jUJTgV5iKBfTDbOlyj1SKWw4Eg477bWTgNkwoHUBP_gvJbUYflqhIE57bPRU7RgUekgtukFb_s_HnPVHNqbiLmO2U0EmrCVTjseayxqX7lpDzNs9T9CS_dUCSrbSjmXy6kpcRtik1lgGhS2M_FlMi4pocadtqFb5pl84JB6Lo5we3ELjpahckqmAHdvICuwmGfA-LpJ0TqisJ_1H1w8W5-DZwMJTpX-OYnEhGvouSFlxUGo9DqYAsO4LQZ_Dk3KM_B-qBYwIj4-O8s8F_Dg8xXouwfWScKeZXCdifSDX8yxPefk2xs0eWaFkwcuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/452a2d8719.mp4?token=Tugnx4aRbZUMLj9RD-SVYZEWs9jUJTgV5iKBfTDbOlyj1SKWw4Eg477bWTgNkwoHUBP_gvJbUYflqhIE57bPRU7RgUekgtukFb_s_HnPVHNqbiLmO2U0EmrCVTjseayxqX7lpDzNs9T9CS_dUCSrbSjmXy6kpcRtik1lgGhS2M_FlMi4pocadtqFb5pl84JB6Lo5we3ELjpahckqmAHdvICuwmGfA-LpJ0TqisJ_1H1w8W5-DZwMJTpX-OYnEhGvouSFlxUGo9DqYAsO4LQZ_Dk3KM_B-qBYwIj4-O8s8F_Dg8xXouwfWScKeZXCdifSDX8yxPefk2xs0eWaFkwcuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غارات اسرائيلية جديدة تهز مطار أبو الظهور في ريف إدلب الشرقي</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/88061" target="_blank">📅 15:07 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88060">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">غارات اسرائيلية جديدة تهز مطار أبو الظهور في ريف إدلب الشرقي</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/88060" target="_blank">📅 15:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88059">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">#ترفيهي
🇺🇸
🌟
‏ترامب: مضيق هرمز - أرض أمريكية جديدة</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88059" target="_blank">📅 15:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88058">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jezGxB20DtYVK1P7eKL5KNHew7PoJ_BPTtWaH6m4lfhTU3ETamXJ8LOF11QjdWwyfXIyfLLRWWP__ucYNFI98o-cOpa7eo671V0EpAhNkIuSZgVKZ0PNR6Eo6pYCBBiHT0dNLUSvmePQGH6jC7zws0B94gGpjVydB7fnoBX6nhgAsRAUewo66GS7gJorBbMzGh6j7PdAIOMOwaorzx8esuyNJarPLCdYvUX0qZYKv69B4IOJtrRkUIN54WjGxHMbWiGP8OH4BF2S609jNgLmp-f0NosskXrjP2fN3mnK4m22Z9fesWlqluTYilMwpGW5LwuI4l2-ho0pj1xiPxhZYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#ترفيهي
🇺🇸
🌟
‏
ترامب:
مضيق هرمز - أرض أمريكية جديدة</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88058" target="_blank">📅 14:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88057">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇶
المرجع الديني السيد علي الأكبر الحائري
: فإنّنا نؤكّد أكثر من أيّ وقت مضى ضرورة الحفاظ على الطاقات والقدرات التي اكتسبها المقاتلون الذين شاركوا في مواجهة داعش، وعدم المساس بها، بل الاستفادة منها وتسخيرها في خدمة العراق والدفاع عن حدوده وأمنه، بما ينسجم مع الدستور والقانون وتحت سلطة الدولة.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88057" target="_blank">📅 14:20 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88056">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sb0Ci66nSEHQddEERe0WrGQ6w7yfBriCLYuMm2R4QASJmr2kuB5MjhCt5dijMEzYk5c3HiawS7_doTiURbcU_45RZBoDBWKRBeClY9Wwg1ClAAUpLrwX3LpXvWzccdEfU7hR6I6gbFw2gQAbCpAFWNWlEAtTVLdWMTzFovwIQKdw_MBck1UfCi7nAi2qD5as2j-qMxH52lOWxWIVrsjB7NAZ1srS_9vshsntLOWPlZB2wqAfqQ96rnNJu4t_QqrjJ2ETXCEVs2hEZmLKXLD69oAhHpeuAUPWMqb7Vz2Nghnla2SRSSoq-lAKIVRi6ipciiE9klpAc9oLnW6qrjSuHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">والي العراق والشام توم باراك:
‏
نشعر بقلق بالغ إزاء الغارات الجوية الإسرائيلية المؤكدة على قاعدة أبو الظهور الجوية، والتي تشكل تصعيداً غير ضروري لا يساهم في تعزيز الاستقرار الإقليمي.
‏لم تتبنَّ حكومة الشرع موقفاً عدوانياً، ولم تُبقِ على قواتٍ بالوكالة. بل إنها أبدت مراراً وتكراراً تفضيلها لخفض التصعيد مع إسرائيل. وقد استضافت الولايات المتحدة في الماضي، وستستمر في المستقبل، حواراتٍ لتشجيع الحوار الدبلوماسي بدلاً من اللجوء إلى العنف العسكري الذي يُحبط كلا البلدين.
‏تُبنى اتفاقيات خفض التصعيد الدائمة من خلال حوارات مستمرة مع جميع الدول والأطراف المعنية.
‏لا تزال الولايات المتحدة تؤمن بأن ضبط النفس والحوار هما المسار الأكثر بناءً. ونشجع جميع الأطراف على إعطاء الأولوية للحوار المنطقي على حساب المزيد من الحوادث العسكرية.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/88056" target="_blank">📅 14:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88055">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeee33539d.mp4?token=HljtKL7W52ZYCE1qBO3f0klTaGcU0332MQ6uaC16a4aD7kS_5OUeC9Rka1Ff6ZYGP4SvF-_F63CtNvznrYM0SO6rXKyinmB-o8MOuGkrpEsNWa3TMmoPxBTC_K2ghjmAo5zWD_EFufgXZ20puEOQC9rnr-1fMcGeBo-799g7kJyfGC9oTZea9Q7Jp4fojBHjOr4r5spC1TZeTFZytMZu5diqSrNOV_OqOuuV7c6aQhJqDtdx-o95oYIFS5CgftD0H9i1tPwAjts34R3Dbzn2EUaI8isem9L8aSB2sip6jwLKlH-6pkAQdC1EddZevVCy_LuzQiJdUrTaNVkDGjJn1WJ-u_c3nCufTIlXHnIXIgQmI0WmShDMNIJdTINXmdQqtyc4B33Uxs8a1IOCnG-pceynVi9hzFIJ4VoUe50QA8QXHDbo0UXYH-yfdhEVdoJ-gl-dN4qRK768V2WwL-ZiVfq-_y34yWRc4KGscpoUvx1omAk1h8zHMRvWHGvZasWRK8xYx7B-xe3xDXZgr5RCIlFEBMKNTlqH-vtZ33nXqtCmViZRkg87dh7CtUBYREXaQT_6Xqq4t9Qe62EV6tOZjjZhe2EP9W7bdjS3U2BZooXdznfWCN1USt7nQsVv839az7q9vsaYcsWtUmEYdxrz5CkR9ZRCCmSemgIcuD12gaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeee33539d.mp4?token=HljtKL7W52ZYCE1qBO3f0klTaGcU0332MQ6uaC16a4aD7kS_5OUeC9Rka1Ff6ZYGP4SvF-_F63CtNvznrYM0SO6rXKyinmB-o8MOuGkrpEsNWa3TMmoPxBTC_K2ghjmAo5zWD_EFufgXZ20puEOQC9rnr-1fMcGeBo-799g7kJyfGC9oTZea9Q7Jp4fojBHjOr4r5spC1TZeTFZytMZu5diqSrNOV_OqOuuV7c6aQhJqDtdx-o95oYIFS5CgftD0H9i1tPwAjts34R3Dbzn2EUaI8isem9L8aSB2sip6jwLKlH-6pkAQdC1EddZevVCy_LuzQiJdUrTaNVkDGjJn1WJ-u_c3nCufTIlXHnIXIgQmI0WmShDMNIJdTINXmdQqtyc4B33Uxs8a1IOCnG-pceynVi9hzFIJ4VoUe50QA8QXHDbo0UXYH-yfdhEVdoJ-gl-dN4qRK768V2WwL-ZiVfq-_y34yWRc4KGscpoUvx1omAk1h8zHMRvWHGvZasWRK8xYx7B-xe3xDXZgr5RCIlFEBMKNTlqH-vtZ33nXqtCmViZRkg87dh7CtUBYREXaQT_6Xqq4t9Qe62EV6tOZjjZhe2EP9W7bdjS3U2BZooXdznfWCN1USt7nQsVv839az7q9vsaYcsWtUmEYdxrz5CkR9ZRCCmSemgIcuD12gaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اختفاء وفقدان ثلاثة شبان من محافظة اربيل في اقليم كردستان العراق منذ ما يقارب الأسبوع بعد ان حاولوا الذهاب تهريب الى اليونان عبر الاراضي التركية وكان هذا اخر فيديو لهم. وتأتي موجة الهجرة المتواصلة في الاقليم بسبب الفساد والوضع الاقتصادي وانشغال العوائل الحاكمة بزيادة ثروتها وتكديسها وترك الشعب يعاني.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88055" target="_blank">📅 14:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88054">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇶🇦
وزارة الخارجية القطرية:
المبعوثون ينتظرون وصول سلطنة عمان وإيران إلى اتفاق ثنائي بشأن مضيق هرمز قبل العودة إلى المفاوضات الأوسع بين الولايات المتحدة وإيران.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/88054" target="_blank">📅 13:53 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
