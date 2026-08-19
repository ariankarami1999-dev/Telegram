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
<img src="https://cdn4.telesco.pe/file/vKAhHmuKGiaJsIfz-tocpheCG9EviAs4TZaesIsvofgsBi_Atx7PyJLoeuHUjIURkatKMkz2_ODDBiPJQi5_DA35J1VW-Fua2dXsi3-mY7Q3sa7gBuZaJKEWPuv2Xtxhk7-a-MsFnX9d3994GKaNvTrH_fRznFUklKsrHW4OQPYG6ioft60RGK0bnvfPvnreDBkrXb3dck3mqJl4HF0f3J9wYUAPMA6JUxNOc54MIOtlCsqKUU_bsIo624v3lsWlbsEQsQJCagE3LAQmM73hLmK8d3hXnRoz3y3LKkxS9FaRsPOVZwKiseSPBf_qRz-u36Oz9dztKb5BbQlPGHiUqg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-28 09:57:51</div>
<hr>

<div class="tg-post" id="msg-456944">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVwTU7GAcRWNuijulrTufhMAFaN3whYAaRCFVdQeQcsQxRF3N7av2x61MdSUDkl0Ptteti2vjwlh8a9uIta0ojvZCzvLeVYEGHtuH4bRfcN_-rpHKsAjI3Cnl12qDRGrregHmvRNeLSv16V2Exyua6wrqp8Miz-3-7hRuzgfqeYfaXOI_lWJzk8e6UqhdVm96wMX8CDybtWs2PV05-bgvBbdWA8azpBqepz79mO1O87bX7rfE45Poz40RRT72cK19y6IEJlwYDLMMnNZZLmUUIPJ6Az3YJZb4ZHn6G4f-Vl_wYGiEeauUj7bvwK9hjN3gYuJfyDhdZDN_sYXN0V9yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژمانفر رئیس کمیسیون اصل ۹۰ مجلس ماند
🔹
در جلسۀ صحن علنی امروز مجلس، نصرالله پژمانفر با ۱۳۰ رای در ‌ِسمت رئیس کمیسیون اصل نود اجلاسیۀ سوم مجلس دوازدهم ابقا شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 351 · <a href="https://t.me/farsna/456944" target="_blank">📅 09:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456943">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۶ امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 684 · <a href="https://t.me/farsna/456943" target="_blank">📅 09:54 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456942">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2mTzGHfmicRFhCWZYPJVNOti79mztDUakB0NjOROz4k_685DFLnZqmKr5ghMZ4aIjomEZb_9heIeOgJw2XxPOnkNF8gHXPUjCh1pQNe0-i6vuHh7cOUAAZwB65G_1RBHBnviro4ULL7_dXRBbO5vGgTfs-UyzcBY7NwcKsp8e065KmiE39nfVQOVs8IweX6XugY6s0M7VrZwQA6iiR0cjsclxDLLtgwXsM0gisukH0fvXsAtTX2L1RUZGqTUFb6-V2ClrQ0v0qBFj3cFYi7PQwSPTf95eaqQJrtlRvhPgJjgtcxJKP_ZXcZJXmYnmQmcfGmPa_YbOVdakP89oHOwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: چین دارد کانادا را تصاحب می‌کند
🔹
چین دارد به‌طور موفق و کامل کشور کانادا که زمانی بزرگ بود را به دست می‌گیرد. دیدن این اتفاق واقعاً ناراحت‌کننده است. فقط امیدوارم هاکی روی یخ را دیگر دست‌کاری نکنند! @Farsna</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/farsna/456942" target="_blank">📅 09:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456941">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6fa069a80.mp4?token=vQq-__c4xvb8bXDnn6bHA9fEgwL3StJYCu6Pf9DuCJm_APWxuL3YPX1VzQ_sh0lSmM5D65v9Aqnjr5aj1tmRYaiVV6yIf_rSFT1giHGUKIzs4aSq47Os-ibiunIENKVO_wB87POmyjbh2NLmYbW9n7r3aZaw74pUmHZlWzZ6drkTuDgjXZbZbSnAUESNiR9C2yGlxec4jhekfIxpBFim8fTp-iiRO8YlPgqBvPb0y-vehpXPOX5PxnM17t4xUhmVWrNCRzUvnXW8-kU5Fx_FKoSEEkb9AnfjsTFIFgZdEVvoz4KrqNRFqiANmoFiHak9qUr7xMvtm3OPbrwNEc0z4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6fa069a80.mp4?token=vQq-__c4xvb8bXDnn6bHA9fEgwL3StJYCu6Pf9DuCJm_APWxuL3YPX1VzQ_sh0lSmM5D65v9Aqnjr5aj1tmRYaiVV6yIf_rSFT1giHGUKIzs4aSq47Os-ibiunIENKVO_wB87POmyjbh2NLmYbW9n7r3aZaw74pUmHZlWzZ6drkTuDgjXZbZbSnAUESNiR9C2yGlxec4jhekfIxpBFim8fTp-iiRO8YlPgqBvPb0y-vehpXPOX5PxnM17t4xUhmVWrNCRzUvnXW8-kU5Fx_FKoSEEkb9AnfjsTFIFgZdEVvoz4KrqNRFqiANmoFiHak9qUr7xMvtm3OPbrwNEc0z4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
ادای احترام قالیباف در محل شهادت حاج قاسم و ابومهدی در فرودگاه بغداد  @Farsna</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/farsna/456941" target="_blank">📅 09:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456940">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe28ef4b47.mp4?token=jjhczC0kw6mw8iphoKshNpEUFmpZahd08PGBa19G0gKq-lcFlK7gI1Q2KpTbgzWeHmrgvdVeub8gh0jinGrvKiQ8GDAvpiwXumOI5-y9kHcQ4eMVNYmZVfuWG2KybuoFTN3URviSIvzZ_7ANLjgSyt7IvqyWe9c0tX17T5X36gf8WS59WNKr0WFF4fKdeP-U7GVJ9EY_lnNhSRUAtjiDwCmnXTk7nKESNT4JGJalunineLx3sxpf38KRJe04vcyxHlXDGdgrCK2pxonrHf3jIWB9v6jmgQwNjFNBSkOjwevN_HdDPqA9_HxYq0D-EiEMRXVKAkNk30lyyEEL2Hgrig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe28ef4b47.mp4?token=jjhczC0kw6mw8iphoKshNpEUFmpZahd08PGBa19G0gKq-lcFlK7gI1Q2KpTbgzWeHmrgvdVeub8gh0jinGrvKiQ8GDAvpiwXumOI5-y9kHcQ4eMVNYmZVfuWG2KybuoFTN3URviSIvzZ_7ANLjgSyt7IvqyWe9c0tX17T5X36gf8WS59WNKr0WFF4fKdeP-U7GVJ9EY_lnNhSRUAtjiDwCmnXTk7nKESNT4JGJalunineLx3sxpf38KRJe04vcyxHlXDGdgrCK2pxonrHf3jIWB9v6jmgQwNjFNBSkOjwevN_HdDPqA9_HxYq0D-EiEMRXVKAkNk30lyyEEL2Hgrig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان سنجش: در کنکور امسال ۶۵ درصد خانم‌ها و ۳۵ درصد آقایان شرکت کردند
🔹
امروز آخرین مهلت دریافت کارت کنکور است. آزمون فردا و پس‌فردا برگزار خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/farsna/456940" target="_blank">📅 09:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456939">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">محکومیت ۷.۵ هزار میلیاردی برای یکی از متهمان پرونده‌های کلان اقتصادی
🔹
رئیس دادگستری تهران: در راستای اجرای منویات رهبر شهید انقلاب و تاکیدات ریاست قوه قضاییه مبنی بر حفظ و صیانت از حقوق بیت‌المال و دقت مضاعف در رسیدگی به پرونده‌هایی که با منابع عمومی در ارتباط هستند، با قاطعیت و بدون اغماض در دستور کار قرار دارد.
🔹
کارگزاری بانک کشاورزی دادخواستی مبنی‌بر مطالبه ضرر و زیان ناشی از جرم علیه سعید جابری مطرح کرده بود که پس از صدور حکم اولیه مبنی‌بر بطلان دعوی در دادگاه بدوی، پرونده جهت رسیدگی دقیق‌تر به دادگاه تجدید نظر ارجاع شد.
🔹
دادگاه تجدید نظر با بررسی دقیق ابعاد پرونده و با عنایت به سوابق محکوم علیه در محاکم کیفری از جمله اخذ رشوه، تحصیل مال نامشروع و ابطال ضمانت نامه‌های بانکی، ضمن نقض رای بدوی، حکم به محکومیت نامبرده صادر کرد.
🔹
فرد مذکور به پرداخت مبلغ بیش از ۷۵ هزار میلیارد ریال محکوم گردید که این مبلغ با توجه به لزوم تعیین آن بر اساس شاخص اعلامی بانک مرکزی، در زمان اجرای حکم محاسبه خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/farsna/456939" target="_blank">📅 09:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456936">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sKra7DQc1ZGXg81trWZuoswzPMfTe9nEQylQY3brx1NfqymbPmDubG1npvk2PVXjGFomI7BZZStfN0Ffzb3v_fwMa0cpKWbBWACLjJXaM5PoHC21sQbSKg9L4PnvpjCwZ7lrL2Do3jN_rPp5WPPfCQhFWus98iKe4Fl7EuoPVA8aF6NZAZjQ6ZzrPPxXXVvy2cAqEb37z2qNqrzlhCD6p_mUTNLRtoEM3S0WKO0GCgw3IVIn209ViCdUyR9EOk8TAXP6MVMqkXV2RoTcGZpJ_GqJjGC58SAo-vcK5sEoDB-PkTRP3SsS9_Rt1TL0Maf9Q1iqjUEvln2fisUfVfBUmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B2vtHlD0kPrbXhmn5w1I4M3i9W_gWusep3f5-KRdqQeF5Qwg9dndJqFTyVOeVMHePw2w_VChS70c0b0MbW_yrjZ_JmFoG1bfLMpCls8JVIcKzfozJQJt5rZmQakjYYmiFNJV03NgNIgje2xqVOd-sbH4_ZNctsn77FKDIrC_6-bfnsKzsy5jk_RSABk21QQE2XoppjVlkExliZm7gjJPGIgpGX8ZSNBrDqra6aFEMc3V7Cxwqjl0InlrR_okYBbWsjiIBJcL-E8GdQrVTq3enuEZsgr10Yr0msiJ6AnbnSvy0Rc3HFW19Z_xJyvAQx6eQhw3sLlbAcZSez0N1fg8Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h8zGB401EC02XwJdSsCEsr7aAsUlQAHoS7cILIgKLnpJatxuDNhLwjy-HpN8AUuCdsL6QxoGYtbi_uKcHhq5VUeGy1tuE51gWKmHz82cr-fwCPdcOJMVtAvAMAFqaZdz4EMG_k5j8jwClIakLOv2hhIO-dmBmXfWwt5woyWS15r-oBOVL7EKcA8qwlTDR_HTkSvimMArra07GcvH4R7wjR_sBxapQgrcqC2ZTusZ4a1v0La0SE-F6Mg75S16bAqhFURnnMOQmW40aJed6jkIVbZtO86iPFOgASHUkZhwDwkxrhhdV4hw-5323RekNuoZujztsvcFXvYuXA4yzoqGVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قالیباف: شاهد نظم جديدی در آینده منطقه خواهیم بود
🔹
در سفر به عراق با شخصیت‌های بلندپایه مانند رئیس‌جمهور و تعدادی از شخصیت‌های اقتصادی و فرهنگی عراق هم ملاقات خواهیم کرد.
🔹
به نمایندگی از رهبر انقلاب در مراسم چهلمین روز تدفین امام شهیدمان در کربلا حضور خواهم…</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/farsna/456936" target="_blank">📅 09:21 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456935">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JB-z1M_xZzhSy1_qNC9cwr0hsegDE88mCvvekC14CtewwzJQL1qD9ZGqPuDFextZw3NknuKwyw-uajKNk9eMpbsOmO2O3pIh__l1URgcb7eRSv9s0hvhS8HhDfWHh3vTbXfzAqOWjMjQzctx-nz5dejwBhQsRPiG-2BC3KsaIqxaeR0-hX6ydFBteOIP9SnbiZHyl1_cWXEBRYLmRIVgb2YjhGIi8g0yk167veWef95qJ06RrSJ324FfsT6Pfb44PZSk4vPoVD1zV-Gzz7AecR_E6K9jAsjpELTHp2Y-2vjxoW4qs2e-8xbFOa05pNyxinmyKucrl2AI8lFsk2nGdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
هشدار رئیس ستادکل نیروهای مسلح در خصوص کمک به ارتش متجاوز آمریکا
🔹
سرلشکر عبداللهی: کشورهای حاشیۀ جنوبی خلیج فارس که با صدور بیانیه‌های مختلف اعلام می‌کنند اجازۀ استفادۀ آمریکا از سرزمین‌هایشان علیه ایران را نمی‌دهند، باید بدانند که چیزی از چشم ما پنهان نمی‌ماند.
🔹
این میزان هواپیمای نظامی، به‌ویژه هواپیمای سوخت‌رسان، در پایگاه‌های منطقه‌ای بدون اطلاع کشورهای میزبان بعید به نظر می‌رسد.
🔹
هشدار می‌دهیم: هرگونه کمک و تسهیل‌گری به ارتش متجاوز آمریکا به منزلۀ مشارکت با نیروهای نظامی آمریکاست.
@Farsna</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/farsna/456935" target="_blank">📅 09:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456934">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dafae608c2.mp4?token=WJ-94JCorE9gPr-T2ZNPWxd_fkjdP9AoDuqL3QBNQdj2Xsghzp57IylzG_yqG9m7cktxFMztysBZGODYo60OYAZSlWYg6uudiOVm8e3IRq7PJIwtmhBnYcc98O1pLTPHIVcpcJ6BKp2YZmkl2B6lHkXDmq8nZtMNrCYtW1bb4HTDXh8JzluU3WCF8_tlmz5fFBNZs3bCGH_3zheMlvD4KgeBfQx6ugHA1TWPg6POF_Ufjf70qwkU4MJ3PvF6Vx2-zjLUkUKa3TsP4xU-YocMU1rnqm92G6dce98Axjl_l6kb25ywwvJ6MztpeOrJsm8cosfh6mUZ6S1xUjm8o-1SAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dafae608c2.mp4?token=WJ-94JCorE9gPr-T2ZNPWxd_fkjdP9AoDuqL3QBNQdj2Xsghzp57IylzG_yqG9m7cktxFMztysBZGODYo60OYAZSlWYg6uudiOVm8e3IRq7PJIwtmhBnYcc98O1pLTPHIVcpcJ6BKp2YZmkl2B6lHkXDmq8nZtMNrCYtW1bb4HTDXh8JzluU3WCF8_tlmz5fFBNZs3bCGH_3zheMlvD4KgeBfQx6ugHA1TWPg6POF_Ufjf70qwkU4MJ3PvF6Vx2-zjLUkUKa3TsP4xU-YocMU1rnqm92G6dce98Axjl_l6kb25ywwvJ6MztpeOrJsm8cosfh6mUZ6S1xUjm8o-1SAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آغاز توزیع کارت کنکور ۱۴۰۵
🔹
داوطلبان کنکور تا چهارشنبه ۲۸ مرداد فرصت دارند کارت آزمون خود را از سایت سازمان سنجش دریافت کنند.
🔹
آزمون تجربی صبح، هنر و زبان‌های خارجی بعدازظهر پنجشنبه ۲۹ مرداد، ریاضی، فنی و انسانی صبح جمعه ۳۰ مرداد برگزار خواهد شد.  @Farsna…</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/farsna/456934" target="_blank">📅 09:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456933">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cec90dc737.mp4?token=IWPkf3OiWCfppHDNWPmav_1DRRc-mlZhUhJsmaIlKe-SEQN2OBDWCThrmhTw_10W1ywaly4qKIZ-uh-ZkhfO4C3bt2SVGSYuRowzbt3W9TgCDNzsEQbjs07nVnE5YxrlAcxvANqjoLXGXtlrivN7UvZdLFFLPwh_LfXV2Tp2SIhGY3Z7-QHCv6Ls3yJn25RSjVpYG_NtGmDwsoGYVRsczyHRrLj1vq4qAfqMYtGqWu85TjBsfMzP5Wye_u2GyM3mV_rYR494yJkJUKMyH9cFaKVhAXIbSpRh5VlyQP6jjDhldhIwxAzvt9J8WPKsOmi-NV-ZtIVxPP0wcBjA27FHUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cec90dc737.mp4?token=IWPkf3OiWCfppHDNWPmav_1DRRc-mlZhUhJsmaIlKe-SEQN2OBDWCThrmhTw_10W1ywaly4qKIZ-uh-ZkhfO4C3bt2SVGSYuRowzbt3W9TgCDNzsEQbjs07nVnE5YxrlAcxvANqjoLXGXtlrivN7UvZdLFFLPwh_LfXV2Tp2SIhGY3Z7-QHCv6Ls3yJn25RSjVpYG_NtGmDwsoGYVRsczyHRrLj1vq4qAfqMYtGqWu85TjBsfMzP5Wye_u2GyM3mV_rYR494yJkJUKMyH9cFaKVhAXIbSpRh5VlyQP6jjDhldhIwxAzvt9J8WPKsOmi-NV-ZtIVxPP0wcBjA27FHUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: به نظر می‌رسد از جمعه به‌بعد تهران دمای ۳۸ درجه به خود نبیند
@Farsna</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/farsna/456933" target="_blank">📅 08:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456932">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwukuWqxcpu0CDvSZ4UsbFYdfm74Ry5NvGdaq74mgZWCDcF9d3KGjBA1GJOT03-UvO1P0jElaOT8hGCIgoXjtL03NngHvT88yx9LCuYCGcuN3fdXu_jeQ2bVpBTdN7pruIld94b9TkjHMImQQ8-vaoujt5l-6En82EZa-pV-6kDjisXIznaHWoJl3shuGg66WXefs3zxey54K5lb63JMx2TzYiP_YddAyXN6BCbN-VTL6Tr8uikmJoUM-70VA5mPTrdnirpy3sep17fKsCjlAg2KZLUH7jBFnZwqXjT1mjl3B_alXC1BKZMAp7dHIQa6vxsJ0lDxcwC0eisYRZ_Tfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف عازم عراق شد
🔹
رئیس‌مجلس با هدف گفت‌وگو دربارۀ تحولات منطقه، تقویت همکاری‌های راهبردی تهران و بغداد و بررسی راهکارهای مشترک برای کمک به برقراری ثبات و امنیت در غرب آسیا، تهران را به مقصد بغداد ترک کرد.  @Farsna</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/farsna/456932" target="_blank">📅 08:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456931">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlWjV9KBqiEpou_LcgCNEdgIfzN7C-qCwIY48tghfJ1f_eOWyzkQUU1uoerNgEoBqUEhrd4-Wkkq7N5_P_Ag9oQknglveUL8egTE8qdxrP2Xv1q7SQGDVzTMxLNRlwzNkZqV9KDgJsic6XQ8Csofo4JVd3Tz2hTT5vpqCYyRoZyLzZE5ARxGuVhdLOayIUADWptygE37lBqf6yGB1-0VK915XfH0hJds7vWz1BPMHTcYPidNsknBiKmHQgPVXt52oUG52j2ny7j9_77H4LKw0nD4j5XWEhtFlry-nCxylUGLeCGvo3KDif9enLs7W_rOcLvsHSaOERuxJMNK0Sl4Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پول نفت آمد؛ مخارج دلاری دولت تا دی‌ماه تامین شد
🔹
طبق اطلاعات کسب‌شده از وزارت نفت، ۷.۵ میلیارد دلار ارز نفتی مرتبط با فروش ۴ ماه اول سال در اختیار بانک مرکزی قرار گرفته است.
🔹
این رقم ۱.۵ برابر درآمد نفتی در ۴ ماه اول سال قبل است.
🔹
طبق روند بلندمدت هزینه‌های دلاری دولت، این رقم کفاف همۀ مخارج ارزی دولت از تیر تا دی‌ماه امسال را پشتیبانی می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/farsna/456931" target="_blank">📅 08:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456930">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZcDBrGwT_fVD67TIBhEt8goZR8hgck6opbQCArOZJBffWnsoWZ3jVoc3A39N0xzYOSTCWiBxYzOmadXcSjOFoJsVKecYaWzncWtZxGJRubvkN2qU7BJiSOiKEeZfPbQoiXkKeCnemKHIA6rknd-fxUamQO82tpEvrz77Z46dPg6SNtM2SaWrFgGyB5LdCrvfL7V8PkeRBZQSrtLeDwnVcMeOK0L_sxSG0HGF9Ha8f1e2lZ5-hksnRMErQ-84XZLaiu5mo3rLFpfmvCcKR9oKFsClfWiulQv9NTDFaAXxrdE-CmKx2C4idCm-OylAfnyIldFXKMjAYMTY8AKAiJ8Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتکش توقیفی امارات در راه بندرعباس
🔹
نفتکش توقیف شدۀ اماراتی که در کریدور شمالی تنگۀ هرمز توقیف شده بود، به سمت بندرعباس تغییر مسیر داد.
🔹
مقصد این نفتکش ابتدا بندرجبل‌علی تعیین شد اما حالا به سمت بندرعباس می‌رود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/456930" target="_blank">📅 07:52 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456928">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d41vgMQ0uVOHrON17QO3NyM5fO3Cfdw4vq60KmoA27MwtoI0oLBsxwntuh3PsyxqwuJ7z3x9MpeGH60KeCtl-CZ7bH0gM6yhPRDduPtvL2iihnKfM3FvrVM8HBkvXcJwyKEOnxnFCOrF4j7KSI9mwc71Xu4jxQy7CuPGMBUevoAagCulSdwOYaVOR5MN42DMWd9kyr9_1mFJflySOb0aV7mI5zBcwQ_bKe0neMmkQs_--DSviPTmrp1gYnn2Jhbm76TyKF5r0qwy_MOrb6bOsFthLGSHIyaGxm_Z0JzN6vjTYcYWlzfkCmadCDuhsJNzQuzQ6Tnu9qMG_LRA2bUPIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف فردا به عراق می‌رود
🔹
رئیس‌مجلس با هدف گفت‌وگو دربارۀ تحولات منطقه، تقویت همکاری‌های راهبردی تهران و بغداد و بررسی راهکارهای مشترک برای کمک به برقراری ثبات و امنیت در غرب آسیا صبح فردا عازم عراق خواهد شد.   @Farsna - Link</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/farsna/456928" target="_blank">📅 07:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456927">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwnoXEsi47IVIrWmZBE8axp3AcGfl0zSw80fYEokeivliak70SXK5AYsvPXMejgOSWl4dnXYGLmI-RDfwk3pDMmu66oYbKHFDw5cygoNPvt6FdoF51JEbNQBXyoIpoXBG1CC9jK8BFeZ3kgQQR6OZ6fbzhi4qy_yJkIMJ0Sw0qcauiTwm9YL3GCNmXQNMob31GlvDARQ_XlWCvvjBv_hHrFiCD_G_eUZmcQ6RldxVPRZfUU3IosPAFSSSCGAOkO2DpiSLpBBQ5ddka3AH8cbM4_Iz4WRdeAwKqTFqDUE00WAc8jjTlMBGTzkHOQudjhjIJs014W7I8nosrDovLJLUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: شواهد صریح از جمله بیان صریح زلنسکی نشان می‌دهد که حملهٔ اوکراین به کشتی ایرانی عمدی بوده
🔹
ما توضیحات مقامات اوکراینی را شنیده‌ایم و منتظریم که در عمل هم ادعایشان دربارهٔ غیرعمدبودن این جنایت را اثبات کنند؛ قطعاً هر اقدامی که لازم باشد…</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/456927" target="_blank">📅 07:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456926">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47a4be700f.mp4?token=en1YWbsvQBMmMm3z6XVvmL_wt0ReiBIqQpvn_fHEFK3t5RcFvEfU4LZLdSFz9OYC7L04o7qiQC3uF5YMpajhPn0mv3mXiwxZ8eoaxRdM9MuBG3ppYyS4CwQkin1YgelR0C1hJlFmBKFwM5KZzU5Z9vPbEFgjglKMQN0QoolJIZyJNI8kow0-fi9UtA5NAP4REz85Ax8kFdIVL1DMoN0YUXG1kirUknC8XZC0H33uCba6OQHKVLYj-Z3eIZRRahqoxppvCf2OFSCyYO59czY1yU3wER1Ct_nVKCxNBSS5VJnrl_bLnAFplARo7DvxpJg85D2vGXZczVmXj_teVLp3_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47a4be700f.mp4?token=en1YWbsvQBMmMm3z6XVvmL_wt0ReiBIqQpvn_fHEFK3t5RcFvEfU4LZLdSFz9OYC7L04o7qiQC3uF5YMpajhPn0mv3mXiwxZ8eoaxRdM9MuBG3ppYyS4CwQkin1YgelR0C1hJlFmBKFwM5KZzU5Z9vPbEFgjglKMQN0QoolJIZyJNI8kow0-fi9UtA5NAP4REz85Ax8kFdIVL1DMoN0YUXG1kirUknC8XZC0H33uCba6OQHKVLYj-Z3eIZRRahqoxppvCf2OFSCyYO59czY1yU3wER1Ct_nVKCxNBSS5VJnrl_bLnAFplARo7DvxpJg85D2vGXZczVmXj_teVLp3_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
داروی کودکان در ایران پاستیلی شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/456926" target="_blank">📅 04:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456925">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gq16RNVEI2k6KdNGJXQ7u7_AKfhewNQizuvwXC61Dn-ZEnWQOmFeL2HDRNMK_SYPpptjRSu-4dEQYthoU8RiZO0V0kjxU3Es_qrldWDTEOLJxx6fsMcpQ0Q_cxhKknxXmUmk1UkhBz3Lix_kXDaJiCydpBNE7q9_u-MyLSxNO_7SxVrPBsI8u8iOR5pjphTTc79uMP4nN9rgq0KJ7VxM1MYVIloMym1PVxmN9QdfCpYiYz6hwGMmvcMbZYmJ7Ae9tZwCc5b5IQOr3849XN2TphKKSwWhM6YhAI4mWjO4Fz7dCMEj1Uw1y7L-jWJZQetkC1spXHEWeXAEC69kY6DjKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
غریب‌آبادی: ملت ایران در برابر تحمیل و تهدید، محکم‌تر می‌ایستد
🔹
معاون بین‌الملل وزارت خارجه: کودتای ۲۸ مرداد، مداخلۀ مستقیم آمریکا و انگلیس در ارادۀ ملت ایران و حق تعیین سرنوشت آن بود. این تاریخ را نه می‌شود تطهیر کرد، نه فراموش. دخالت خارجی در سرنوشت یک ملت، نامش هرچه باشد، استعمار و تجاوز به حق حاکمیت مردم است.
🔹
نسل‌ها می‌گذرند، اما یک حقیقت تغییر نمی‌کند: کشوری که اختیار سرنوشتش را به بیگانه بسپارد، بهای سنگینی خواهد پرداخت. اما ایران امروز، سرنوشتش را خودش تعیین می‌کند؛ ملت ما در برابر فشار، عقب نمی‌نشیند و در برابر تحمیل و تهدید، محکم‌تر می‌ایستد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/456925" target="_blank">📅 04:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456924">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LaEOzaxrFDNxlY7BGgjTM1RpfEH8VE8sw1PbdroqLbmJ-tql1l2OarkgVrx4JVrYj9zHP59rUGXfoUvrsMD_HbkK5vCyNZ-2XQ54MEhul9DFwjfb4DN0-_ntaudbA_SO1RZ5ybzEN5IpJferqcNr9JXSyvHPRgc2a8lFXVyELXS4FkQfuSknDeyJRtpakx1bwTr0lKkobVlZL7ozP9cUJuJdSZUWd5H2IM8QHvCV7F1VfbM3TmWmc1O9iLFehlkCaucMANBT9nW1t7tNyfxQwAj1CJtuDoF_08qHnnAduE5-4i1LaY27fOPhJt7UjUmJIgy_z3EX20VbnwUCUyFxbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راز پست‌های اعصاب‌خردکن ایکس فاش شد
🔹
یک پژوهش جدید نشان می‌دهد الگوریتم شبکه اجتماعی ایکس ممکن است به‌جای نمایش محتوایی که کاربران واقعاً به آن علاقه دارند، پست‌هایی را تقویت کند که با ارزش‌ها و دیدگاه‌های آنها در تضاد است.
🔹
به زبان ساده‌تر، اگر کاربری با یک دیدگاه به‌شدت مخالف باشد، احتمال اینکه چنین محتوایی وارد فید او شود افزایش پیدا می‌کند.
🔹
یک پست توهین‌آمیز، افراطی یا خشم‌برانگیز ممکن است باعث شود کاربر به جای عبور از آن، وارد بحث شود و پاسخ بدهد. همین پاسخ می‌تواند از نگاه سیستم توصیه محتوا به‌عنوان یک سیگنال مهم تعامل ثبت شود.
🔹
به این ترتیب، چرخه‌ای شکل می‌گیرد که پژوهشگران آن را نوعی «حلقه بازخورد خشم» توصیف می‌کنند: کاربر محتوایی تحریک‌کننده می‌بیند، عصبانی می‌شود، به آن پاسخ می‌دهد، الگوریتم این رفتار را به‌عنوان نشانه‌ای از تعامل بالا ثبت می‌کند و سپس محتوای مشابه بیشتری در اختیار همان کاربر قرار می‌دهد.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/456924" target="_blank">📅 02:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456923">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0bd5a2c73.mp4?token=TLe616hiK8O06O9bNS6X6f9YI5MuljK19zDBCEgxLoNWAdSxzgdoFRxWPGoed9M7x53NQ2cZkONd3shWHESe5z8dOAUFTxIcZhtkcAbentgcSSMu3F6KynyvxldXCeVRwyF2VGSom40V1W74cdVIKXoAbjWWvRcmG9OxPKWGS_9EVv7RiIO4qu7fBqxlhTVil0OE40EAPFIEyAxu1MTUrDiJEysKHiJS7WHEd8k3r3giqeysQcR-zflOF-XN_eVvCllUQvO-71Q68WiNLxozMJe0d_MEsKv4jn8HGvB6WC02q4QNywJVzOJ-CZK8QSqnlwEkGQ_7wHWmmrPmfvYk7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0bd5a2c73.mp4?token=TLe616hiK8O06O9bNS6X6f9YI5MuljK19zDBCEgxLoNWAdSxzgdoFRxWPGoed9M7x53NQ2cZkONd3shWHESe5z8dOAUFTxIcZhtkcAbentgcSSMu3F6KynyvxldXCeVRwyF2VGSom40V1W74cdVIKXoAbjWWvRcmG9OxPKWGS_9EVv7RiIO4qu7fBqxlhTVil0OE40EAPFIEyAxu1MTUrDiJEysKHiJS7WHEd8k3r3giqeysQcR-zflOF-XN_eVvCllUQvO-71Q68WiNLxozMJe0d_MEsKv4jn8HGvB6WC02q4QNywJVzOJ-CZK8QSqnlwEkGQ_7wHWmmrPmfvYk7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قمی‌ها بیرق سرخ خون‌خواهی را به شب ۱۷۱ رساندند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/456923" target="_blank">📅 02:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456920">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hgYAgsWKt8jhSg5hy5qCm77jQMhHfu7BbbxInH2_uLhL8zFCO-TrIwwFQdwhmQZfU5RE93JRlNPHSPOZMjQEbYHZGFNc2xNTPOxhmIBMXl5v-mkUj_74dfjpbZ8K4o3XXHLzXSiCGqekyEMuqjpUNJo48xK-oAOuTgxc31wMAzV6fhb7WN5EbH4lqQovl5E6LMZhBGp-lYchkBGi531tAxrunLlJ-F0Vzwj-g5eegKQbKdv-XcvVCpWO6SKoeY31vWIeucJ2cLYqsOZLJob4SGG_Gmqi2D8BLhL_rFJMbiqzAJPJ4IBXp6hM3OUGeuxsFz0nFLO3rmHFjbAZUEUxYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jsDszFpqYseS4CR9YkjQ1Wbw2qcpvSGbVdWkYQdMLUsFnAFVe-sO8xcFBPVda_I8c7IPJz_s1Wo0tPEcwcgY9eR0zW-tDHsIGxo7XsDgiFEXFBfw8J6hWsX8EFmIT5S4qoZPALOvu9Koke1L5kXoUWrXeJXsFtwdRsAn7rqUscvAAjsYd6KAtWZEXsAnUF56M-bIpTwZIuOCoJ7Rn8xHtVEAirKLIlSoggTXJBH27YShqHZZUUzPF3Rd7tjFG4Qfbx1Iwu9DVM9inOHFHNmRxrr9P0HFGCptqegymZlQM_YVj5lgfJ5crmNDVaffjoXG-kRvCnX2AP6L9y-wxrBKHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9102233085.mp4?token=ev34MYn5WrP1zvdsx2a6JooM2uDAOuH8oViojJHO8ZdznnGs_JjLdPaMtO9nTaqi9aM-qL3PVcbNxNrPY1qcswD-ayagsmzlBDhbQtz8amKFWCuPvCrxe9fHksNUtVISmAsFmHwpREg3w-5M_xax0fpAcNDq3y63_8lQhn7aW2pB_63niGe8spMPEY8Bnbw6xtLCkcxU4cCYYpmUrXpvoF0Izo7v4PYtbJ9F7xt6acSIo40we6wb2mBkfTwuuiQ4wz0i-_qDOgrhvtMkpNL_AYmcDgcKhJ6Ru85EXDtLe-cZHm0_M53ZrG35UXWJQJMwNoI9VKYSP5C5SON7h-I_Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9102233085.mp4?token=ev34MYn5WrP1zvdsx2a6JooM2uDAOuH8oViojJHO8ZdznnGs_JjLdPaMtO9nTaqi9aM-qL3PVcbNxNrPY1qcswD-ayagsmzlBDhbQtz8amKFWCuPvCrxe9fHksNUtVISmAsFmHwpREg3w-5M_xax0fpAcNDq3y63_8lQhn7aW2pB_63niGe8spMPEY8Bnbw6xtLCkcxU4cCYYpmUrXpvoF0Izo7v4PYtbJ9F7xt6acSIo40we6wb2mBkfTwuuiQ4wz0i-_qDOgrhvtMkpNL_AYmcDgcKhJ6Ru85EXDtLe-cZHm0_M53ZrG35UXWJQJMwNoI9VKYSP5C5SON7h-I_Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات رژیم صهیونیستی به جنوب لبنان
🔹
شبکۀ «المیادین» بامداد چهارشنبه گزارش داد که جنگنده‌های رژیم صهیونیستی حملات هوایی شدیدی به مناطق مختلفی از جمله «نبطیه»، «علی الطاهر» و «کفر رمان» انجام دادند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/456920" target="_blank">📅 01:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456919">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">انحصار وراثت غیرحضوری و خودکار شد
🔹
ازین‌پس، برای متوفیانی که تاریخ ثبت فوت آن‌ها بعد از سوم مرداد ۱۴۰۴ باشد، نیازی به اقدام از سوی ذی‌نفعان برای صدور گواهی انحصار وراثت نیست و گواهی به‌صورت خودکار و حداکثر ظرف ۲۰ روز صادر می‌شود.
🔹
برای افرادی که تاریخ ثبت فوت آنها قبل از این تاریخ بوده، ذی‌نفعان باید از طریق سامانۀ «سهیم» درخواست خود را ثبت کنند و حداکثر پس از ۲۰ روز کاری با مراجعه به سامانۀ مربوط و انجام فرآیند پرداخت، گواهی را دریافت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/456919" target="_blank">📅 01:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456918">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‌
🔴
وزارت دفاع امارات مدعی شد موشک‌هایی که ساعتی پیش به‌سوی این کشور شلیک شده ازسوی ایران بوده است. @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/456918" target="_blank">📅 01:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456917">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9472fa504e.mp4?token=BnyPYdgnKsR8KQ7ZAoKtxHXqwkLipbKE3aYMHwjdQdCduOz-AYWojLKwtNMhzoU-bw0vF1TXI8wjiWQT_3n2VXQAaP9Xt6zFs9kdb25gOjZAQNHDKQFumNPrTvq5Un9qNwROeMfrsLuv2BljAJ0Bb498U9DdRUoTtuJn0FLTYpq0cKmMkDj9p7Y_-TlDWFVvVZpLno0_1MCkjcxM18cEUMTmwrUXRa1Z-MkP6QyqnXiJCJ3OMMHwxwsO1_OJbSAxYUw0nm8Y0QXW2yDVvMRk2mJi59YTsY33HEB6_WTZvYXHz1c3uwqe5N42rvBNQ1yoUg-3xCcDAb_CNatXOSIL7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9472fa504e.mp4?token=BnyPYdgnKsR8KQ7ZAoKtxHXqwkLipbKE3aYMHwjdQdCduOz-AYWojLKwtNMhzoU-bw0vF1TXI8wjiWQT_3n2VXQAaP9Xt6zFs9kdb25gOjZAQNHDKQFumNPrTvq5Un9qNwROeMfrsLuv2BljAJ0Bb498U9DdRUoTtuJn0FLTYpq0cKmMkDj9p7Y_-TlDWFVvVZpLno0_1MCkjcxM18cEUMTmwrUXRa1Z-MkP6QyqnXiJCJ3OMMHwxwsO1_OJbSAxYUw0nm8Y0QXW2yDVvMRk2mJi59YTsY33HEB6_WTZvYXHz1c3uwqe5N42rvBNQ1yoUg-3xCcDAb_CNatXOSIL7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شیراز، ۱۷۱ شب ایستاده در میدان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/456917" target="_blank">📅 00:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456916">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f570b23b8.mp4?token=g_c_xhS0-5EZpvqg4m-6la7m4hyv_mEYKZamQP2ll4SWxNytVvp5cKRP_Vyr1wHHkmgsBV8sc2F8yC0NzVqVmmaYwFGlYhUW59uhiRGJemd9BI8yIj2AfwAhhN4wtmZUuwD4gIgwJorGDgAPoqL6VuZayO9bfNc07M6Asuoko79LM5ByVbdMIJ2yUi_q2v4ozBAFhpmuCcXJ9lxauaKNozCytSC5CtKoq90D0_cX6xfx91L4xfMvi62BEiBMyPaPgiLm_fovul1qZgYph0z455i7-0th9jLrPvAU0ROwF_b8d4f6cmX865NUfyuQI9xB9Wf7sjIyILfMkr9seH0Nkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f570b23b8.mp4?token=g_c_xhS0-5EZpvqg4m-6la7m4hyv_mEYKZamQP2ll4SWxNytVvp5cKRP_Vyr1wHHkmgsBV8sc2F8yC0NzVqVmmaYwFGlYhUW59uhiRGJemd9BI8yIj2AfwAhhN4wtmZUuwD4gIgwJorGDgAPoqL6VuZayO9bfNc07M6Asuoko79LM5ByVbdMIJ2yUi_q2v4ozBAFhpmuCcXJ9lxauaKNozCytSC5CtKoq90D0_cX6xfx91L4xfMvi62BEiBMyPaPgiLm_fovul1qZgYph0z455i7-0th9jLrPvAU0ROwF_b8d4f6cmX865NUfyuQI9xB9Wf7sjIyILfMkr9seH0Nkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وعدۀ تازه مدیرعامل شرکت توسعه:
ورزشگاه آزادی آبان یا آذرماه آماده است.
@Sportfars</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/456916" target="_blank">📅 00:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456911">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EJRTXaCgjEFxUwWAiT-U1iLJlwlj_yImoMPyzwmd66UcZ1qOvPwD1D2zQnOzi7n62r1IK7HVU5X0J5G8Qj1a0KUio13BBPq5j1vMR7GXVqutDU1RCgvONnjEK-B50FjfJLFZ6ZsYfDpYMy6YdyDjGgfH3g8memo-J0fhfL1Yz1JygRnUX5ZaKB00vpWZUr0Cd4c5PDw_YT_mIC2n4Sz9rkGwV60EExkGVydKYuhUGe5aCyuhP6HxOttc3ZSE8GKnG8fHiv8_sEb3-x3vyj6UUZeWIDuQpphobvigTXdB8jNh6WvTAMTIInfyuCBWwBdos-eEMCbcHLqS0IVJjrfhTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gELNA6NtuD8xK-6na6HsR30PS3pcH8cz0PqL0T1Qr7CSMyZEwwAa6v2cykWKe7JIhCTYUhlp1AuEOVPW_lNlYssMfujc5f9VTgVVBt1y-nisfwi1Ve61xTR8rISv5XVbwArsTrU5W9W2kiv1mLHFC0XA5QOwjMDYnTbucL4epFTgOlcXnM8Gnke0NeXh0s_Pg106Yz0JB-_soBgV64TL9a3hbmXBhy1ALv5628ueKyi8JT3YjDmZrpBvwubjUakSCSRgjPvt-NADG0E0zD9kNZwNl9INX4mrZ6P8eY0ERcvps-yPYeaRXJZqXrLA9NC6uWT91S_5FsGtaNlho9cASg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lSJDRE8iBFql0WldVhkYCgN9S2sV9D-m9hX1CNMM5-SNIAS24ajCzO9MhI-eC0wME11Il37sN6scv06elKYxVXsBU0aBvH5etY1eFYN938_E2AZWzcP0WI1AbUqCzCdO44J9TGQpoklS2PkBWx1Yn7eQSvhOYT3RSANFLmIzqzCLxGfJv44ZSoYVp4PYYGFPFSJNwC3d-kCdNpgRUAqS6UCwTwKnUUS_fSKbGUAzPPU5P20kuPnsnjodIshtVt-bxRo9j8KBAHNrtW4WmF5XW6wumMgx4fK4EcOkWxDAhTuZ4VlqxW3RzJI7CilBwwrulwb0FT9xO6jZvclPYgMIWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/plYt2v8I3JqA5yZMZVOP3Fr7p6iNu-HQ2QpibGGT0xH16d7fRBINcnENVYmeVTiceRvYah-aN_kOHFPy1Kb_nX--lyTHAw1Sy3cjHBJxpAZDt51U1iv9CvP-Mpo1dGge8QYHQOxqTN3S_3B9eCxKVSdeDW7oFWNE26aoilUtWNcQvbMMLz_FEBOfPV5QnxZjPQmvQzd4lSvvPFEVmpS86eFBEb5AqlvpbSy3A86LnXUwVNP9hS1poLvaCLmiVEMrGf24K3dep9yEw_nUv1EYo9HQE0VRgU5ZMQD4mAoWYbDywnGB1qpGY6y5t5pw2_S5eziMw6-0ptoeTJz8HatGhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N5_1aqaBu4tjJYPnjsISPNRh9iuDoOt2zrSssOYETNEBfEDW6kx5NTaAzLAS7YRdHjMcojtWVDXAoKSobus7vW7H3ac4pYXhtkv_PrnyrjYOeswa7upl4oKf1-4zeAtB5rzJLHsVsfrNymBu5Eo_yu7TzpyOlByO_FFudu7p0JqwdWx07KSS1fsSQ0POvHkMis0PlqwFUSWP5SF0Bxx4-YSOE7nb1eUhenMx1uAS7D47STOiRX-pkf5ZGTmAC6C3SxKRfDWQcwQTKzOiGHpV-cgfjXea10Mnky0Xw9jSSruCYUCkbM8WhAuN0hp5mOpE0xexd2tTCsb56J3bq4wmnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | چهارشنبه ۲۸ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/456911" target="_blank">📅 00:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456901">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CMA1DM8OXNGKJIY01jVGwM7s4OGlf2WO8N2TNZ8e761MDTUmwFguhnqCZfPpGy6Isl6X868rvLNJre-eUni1TPetS1vVHsqBHTXt1qjM0ygbhmTJRq5kgrFhs1_hB6XDpzbS_auXhychxQGTRghYSEIyn4rVf9hz2BO9VWND592A4Lo6wGMiXQh1a0MCFyMUCF7hIq4QRrld-tOVTqimZE4ZPH_29Q5RLqKyc-t6Q2X5LPdPngr8Zk3K86wRSJmF4zJfWOs1thwQ3ovJz_gkm8eiE-yX7b15tO54WCtTIK_omXxiq6wIBC8ClX5koB3GUBTN9_HvulmnVF3lgs2jlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ozuk1DdgyeUiWSAihrMdOO6UpTTVZMjNV7gOhrJXO5W9fQ5eHlGYcD2wcm4SLBp1ST-_SWIcmGxigowacWS0a5qMx-_WoiZHod-LRc3OAQ7bxLzzxeHswyoPVcrFpLr9t91MXsqL_C9z7AQz1uizSSGvT4htnbY7OLORxKbTA_2LM12DBYx_a9wJ0e9GwpTrF5aMAdeoJR2ziyWAEinUC5pSxuhAAOq1_3UabahQU6YIMFYgzCoIsIKyI24YtSYk4Dq672ILjkTmJ5r9dWEYkuOyF7i1UHMdqfnF-P1hGSyFA3hioHX_lnNsGo7r1EIBnKogCTGJac3aNLIYSDhjxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cKtD817WiaX8JmefJ0Qr3qxlx3_Jpp_pi773fy1AQ3JJ_qwFyrT6gI70VTOBHTrPjFBlE9KaCg2IK2-e8QIWUajqRHixbVc8xuyKsgjTugQlPBlTwUSRC09MKMiDpl47Lojqjuiep4T3MUf6rQSgBRlvkybEIG6w0UyBO0dgfkpAU84cQOicjL2pka4kHRiJ29naHf5j2ophUiwo1rNdwQN-rRGAFiA0ziOgoLT_G_0BkwnD9mr1YWzX9oiu-cWN8E2rL3iMuRtaIxCSB6f3OlsDzcLXQb7H_U7BBKl4Z_rXN2bWARu9YRZ7wpbv_qjNvTV7mU-2-NpnJzyhUU688Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X9V3bqGATMjWXPGxlDHbBAhvT6CX1AQHrB5xSbrZvph57fJ7UCjp8OhEp0P0jLBIhbaLgAnZQYE_bKPAxk2dOlH_2lFgIVGMfoGpXr9NtLpHWSlxXYPtZp4sTU4K6y7HGIw-MhVe_-FDrs7vNXX_8ifzv_Vg0RQBGPtpAytgALUDppIT8kCumLsMXq7abaZF-AP0xzSJii3oBT_WTCcWrMsfX8Uxv_RkB5wtqWvhA_Wh6Ik13WKNJ3lbm3lxIXxrbc5YAUcg5jSBnTDa7XUCqZTnbeyK-n6RWqto_PBBnRXBrbxj0Z3TGAnGvhebpKLbIJIL3Djd0sVdxGN2ybsFMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tu304-GH0YKvNb_aJN1agvveHTPChwFdKtvdoIN1SHMDO0I3wnPtSgd_Ib3HUz9xs-n8rsrqWQ4uSke8yMDNOQtLznzOL2HVOHdig2kyJpRe4sE__scR-nbQda0FR2glBbLL7B-UxQGH1CaOYZEAZEG-1YeTfItgOGu65oVDvUoufBIYYWB9RPO0u5N9_01do7YFT4BEUfCAtDhrDQGVskWdNZEIkB9SmIn4PtBeVdmHPmsyMqmgQR6wgr0eABQLX5ko0rVKHKL5o-spA8LYJqve8pZdOe771PVXXpQUhlCE6TxVNZxaVOmTtyJQCErCc2Ps7w9m8UVdnaMoKUmWOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HNqcutWY_FW-LO2p77LD1KnqmJgxGP3IWmDXG52xGlpYQBnw25eEVlDU55OUxaQEnqE5Dv-bBhEpv-s6x2S3HebJEE4-zhsi8A_cvlhbSkGdmsvAhwdP9PcvIXO09WmxGC7ZD1cR66x0Hrn4MlsxeNrnXHH-36H-LrRHtXITqCMKM55v7JKkyB32riTdmmj2XUuiWHvmC4h2LmApazDh69DtiRapxFIZpARm9uQo0OmReYZbxhf2zHJknB7YtNXHF3Qx8k71ELjy28WpV-Tg3UNLGTw0yeaQzcUz1eGpZaPOJ7oSPzRolJSWa44vpDOtinw7Z7JArk1N69gYcKoF2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OSeEDGYsZJapsOdinu1t3EYWalJ2eIp7_y3FILBKfhCt-11-rJZY8d_rJIAWQU-7yeqLzdOtJ_YXMC8KyI1doMvcO5BucIySY5TqRzSTxJrzWd94h1K7j_PteIkwJxEagneFKf7-YFyTOmYRmvaEiiqgaN9C3-VM-DBAztrQF5aUdTUA4puDeS-iIIl7I8mT6VchtxcqSIbRAK68AFRUGsVg3D5X8KhboptA-yxygG3swnbDE8ICNebHZdJVbTcvJ8iG-MXA2zhy7U7YHGOu4S8hG4Ra9BucAldDo0N6F2H8qTyAyj8lYPC4qhoyR-9lkmKYZybvZqqPk78sgt-iUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OnUbMO7h_KHNMRAv3dYOyOhWcEZN2jXttrD0cqkroO7U8lhb52Nkig2ud9j8t7HdY0dO3pADBx8A1E3xzPwsavGQW4ZG3_6CiHDQNNkqrtwgxq3DAKIMiis1FglhVzJaCr4aulIHzaUkhLBzg95LFqaTBCmB6VO6F5dDXxjJ3iAiHb4UlV2C4IphUyiORmUC51xfZmsK-X9DINXPrq9-_Gr9BpMU1C3Kq704_uOuiKOl40AgYV9zJgDmqhzNqUNiCZjcPRrnUGe2Ex0IGu7F7K6XGCkR_VHlHs-Q8Am6Rxqsvt3ZTtmby_k8HI5CeIBTgMNiAczK-uM5_whc_Fgs7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LPPo31u_P5goWqvH89nAb1zJarc6ulaAfVLEJNZWSfAAGM24w2Td6eRRifgplUwUJGD8d7taQ7axe1YljpDP1sYEybfgqMUQJ_e2rArA0pls0Y6JWspYw5ken0hvSF3RLyvWujdWRswipSm206Ss7iLS3aInmV9VWH1GwYuwJxfNlY2mjU-asjFTkGqFMnCn0-iaPuL8_RiS89Afyz9oBzCqd5aTIdJoOQxDenslyIyjZ3LCSUDYDEih-MwYcMwYURw1lWJutNVkihaKz9CyHjnfoxne4TCqOVxB7f_PUL28IU5bIXSOQ3S_0o-3ZOgWp7VuMszM35zgbN2W_d2Mqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VGz9n-GDcYZ0SfQNt3ngXWqvuqI-m_kMTYm6qOdXuOycIu4kyq_t5ALM8xl6MDU7wbvvsbAaKwOvcUqGifYx1jIiz6BSMdlhG0Ntz97pnvB4LX-Hs3fA8Tslh6kXzjk1uldfACumWSAnUlxjLqUtqbIZsGh5i60cg-Z4CT4pvQn_4z1rxX6Jyv-SyAmVxzQCr8kYPLsoJW-5616JEGERvrHhN8pfQcn_KVGlfRHe68uJS7roYoPk_WJbXtZBkPVcoM2JEMun4mvoNUET5np6idwXkCTXUkzk-LSh_QMcdL1GTwcpZ8lpkQdYDaIuIzQwjoPSS4cX9oTOi7lIq5quww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/456901" target="_blank">📅 00:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456900">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgTE5H-jzPqODTuhk85-TVsq4S9iiiIGTKBnSBJejDf1O-tVcz4QJkF2EYbWEO1dgUh3k1Pn3KEz_oPNu03Tz08cvFnimNjuHyIqLWDklFGtcPjTohz5xdyIHoEsoKk4uKn5hsuJFjfdei47XqAeBj_aE9z1rE_QqICRB8ed5sHkXpyx9lctMiqciAcGwZg7MXm6mPyXVSmNUOX8Ie-58hEkm_koBsYsgCWS9ajjcWpUm0sDk4YGkj4YxK9bv6SE7hI-CwrHyYvRmQLxl9_vwsNTUBMGOIddnqIkp43QE17Rlsrwk8yyZyIdRZJnZR5OlKWaGZeMEAwSiIojlABczQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقائی ادعای امارات ‌مبنی بر پرتاب موشک از سوی ایران را رد کرد
🔹
سخنگوی وزارت خارجه ادعای امارات مبنی بر پرتاب موشک از سوی ایران به سوی این کشور را کاملا مردود دانست و با ابراز تاسف از اتهام‌زنی به جمهوری اسلامی ایران، این رفتار را خلاف اصل حسن همجواری و مخل تلاش‌های جاری برای تقویت اعتماد بین کشورهای منطقه و جلوگیری از تشدید ناامنی در منطقه دانست.
🔹
بقائی از همه طرف‌های منطقه‌ای درخواست کرد با در نظرگرفتن پیچیدگی‌های موجود به دلیل شرارت‌های ادامه‌دار آمریکا و رژیم صهیونیستی علیه صلح و امنیت منطقه، به‌ویژه سابقۀ عملیات‌های متعدد پرچم دروغین، از اتهام‌زنی‌ بی‌اساس علیه جمهوری اسلامی ایران خودداری کنند.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/456900" target="_blank">📅 00:20 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456899">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ملاقات سفیر ایران با ۴ ایرانی بازداشت شده در کویت
🔹
سفير ایران در كويت با چهار نفر از هموطنانمان ‌که سه ماه قبل بازداشت شده بودند ملاقات کرد، و در جريان سلامتی و آخرين وضعيت اين افراد قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/456899" target="_blank">📅 00:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456898">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoV9GB95uz39L1Ks7jUikb76A3ohvyXpQXmZHUFYJFY_EpDExDXUIVXZFuxs2neJydBHbsUngVWgBC24c5PUF5bQXeVEsvgLWAlzeqfM_p0MYCPpF7CuhUd9KaspY3YxdHgOCZKGDIRp7eCEwemWGUUj_sApKXqRyXggqyjvJVWnzUmDjyljGvla1HUBVSjiYrO647AJBj7SIHkn_r3XIJxvuIFlROx_mdoFaioEtKWqD9tSieiSd9I_U6_-FeACPQ0k67iAHyqheTcY2n6b918_fpwJ1YZ6YR4fsbRznHelzLTlEnEfHuJtIX3kuLq-IhedLRHkt5ShteJOGTLVGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دیری است زآشیانه جدا مانده‌ای «امین»
...
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/456898" target="_blank">📅 23:56 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456897">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb71618728.mp4?token=v_ObJL2nSiz0HoTIk9ek4CZZAl_V7-GQnq2cuFdNUy3T-dW-JLbaiH7V1TRvp3B1HotIUkNDjvdmfCUIrMmXh4M9-RsODTWhO2ip7iYlSQMgHwRYPjvz1b1qLcjCOM-3SavXZwStuwG5o01WZAHMJErOtWHEUM6xF9W-0dwDwjYExPp3Cvq24jT17hKh6wUa0Jm7yHayJWmJ0XA_ymCM7Vdr6pQxFVRi3SjXWnq7qhP_19wRXFflgjscpX_bt_svBa4EN3BFzHbkQaz-0xqrszVpxfiuBGVw5tdE7omdhWxV3ydHzrBErQKMYQb865im9b_tjZ1QPWynH56gOiB426vbu8mzM4QZOGkRStA37nz30Iqf8jQ05QizlHLs5iEY8LX7ZUXWgigNEAC65QMNOjzvQGP9yusT-t6QMHgO2LxK3cyR9nB83QMQiBlgsEFf9Kvg7HCQOLJZKhFirApIivVjEVhOcS9ILmQYQ2RgEv20hf5RodQEfqpdjixlRo3Slt5J_qe_mUS76xfcYX-ScCopZYrb4la3heY6OV5I41F2eXoh5e8EDFeZl7Ax82Mj1GkxgVhPttqfwKBuWUxq84aMWPlaX_SxDZPT_bKQV8PQT2iFjZzcHYLZGs34VNQIfiCKzF2CIUxc7PIB87WDtiSFXY_fSvWKFx2r_Z1YnTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb71618728.mp4?token=v_ObJL2nSiz0HoTIk9ek4CZZAl_V7-GQnq2cuFdNUy3T-dW-JLbaiH7V1TRvp3B1HotIUkNDjvdmfCUIrMmXh4M9-RsODTWhO2ip7iYlSQMgHwRYPjvz1b1qLcjCOM-3SavXZwStuwG5o01WZAHMJErOtWHEUM6xF9W-0dwDwjYExPp3Cvq24jT17hKh6wUa0Jm7yHayJWmJ0XA_ymCM7Vdr6pQxFVRi3SjXWnq7qhP_19wRXFflgjscpX_bt_svBa4EN3BFzHbkQaz-0xqrszVpxfiuBGVw5tdE7omdhWxV3ydHzrBErQKMYQb865im9b_tjZ1QPWynH56gOiB426vbu8mzM4QZOGkRStA37nz30Iqf8jQ05QizlHLs5iEY8LX7ZUXWgigNEAC65QMNOjzvQGP9yusT-t6QMHgO2LxK3cyR9nB83QMQiBlgsEFf9Kvg7HCQOLJZKhFirApIivVjEVhOcS9ILmQYQ2RgEv20hf5RodQEfqpdjixlRo3Slt5J_qe_mUS76xfcYX-ScCopZYrb4la3heY6OV5I41F2eXoh5e8EDFeZl7Ax82Mj1GkxgVhPttqfwKBuWUxq84aMWPlaX_SxDZPT_bKQV8PQT2iFjZzcHYLZGs34VNQIfiCKzF2CIUxc7PIB87WDtiSFXY_fSvWKFx2r_Z1YnTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیندگان دربارهٔ جنگ آمریکایی-صهیونی چه می‌گویند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/456897" target="_blank">📅 23:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456896">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b223f152f.mp4?token=imRmvyDkjA1IaUwN-sgw88GgkE9Tbclm-Jnqf_JjO625ID6RFy-EOsvYrzZkSNLp9LVSwt7sKPzAKSf6JzZatCcq-rcZD1c1_coTXE-Q7144t-iM2eWUAS14UiFK_w6i2keVFa88-9ktG9JmhTcvFQg7vHbtbtNxgQQMXfmDfa0Pf7IWHQ7J3isiJF3Uw4ndof9cOj5TPfV6yOfNgKV4OryVyB_Nr4Zj8Uq7_cJsqe00bIqJDJJyVEbyYc3roU7zVltF_bz4yi6PLnOMa85iig54SuNmKT0vqyKhWTPUC507j--36KiQfVJy47e9PX9laLAUNq4PGFHNqTtq7F7m6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b223f152f.mp4?token=imRmvyDkjA1IaUwN-sgw88GgkE9Tbclm-Jnqf_JjO625ID6RFy-EOsvYrzZkSNLp9LVSwt7sKPzAKSf6JzZatCcq-rcZD1c1_coTXE-Q7144t-iM2eWUAS14UiFK_w6i2keVFa88-9ktG9JmhTcvFQg7vHbtbtNxgQQMXfmDfa0Pf7IWHQ7J3isiJF3Uw4ndof9cOj5TPfV6yOfNgKV4OryVyB_Nr4Zj8Uq7_cJsqe00bIqJDJJyVEbyYc3roU7zVltF_bz4yi6PLnOMa85iig54SuNmKT0vqyKhWTPUC507j--36KiQfVJy47e9PX9laLAUNq4PGFHNqTtq7F7m6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دارالشّفای آتش و آب است این سرای؛ سوز دل مرا به نمی التیام کن
🔸
حال‌و‌هوای مزار رهبر شهید انقلاب در رواق دارالذکر
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/456896" target="_blank">📅 23:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456895">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6e6ad8a31.mp4?token=UsZJj4rLzNrK9ORz3-fBDSTwSA3D-YUhTd0mkYdnf3y5ZW_99yMtEk1EzsU2QvV03V4RlDpeXgcNkTwsT_SWTyOtOS-27Z_mq7oSL7b-lIr0LWQ6XTL1DH9L180I9JLTK7wO5ywendQVs-yMWrooj-D9DntDTic6_QUukc78LqbYuvYmo0MIKe1N7wHBLnlx9lqj9RWtjroq5JDLZnDH58BBnhNQAXE6NEN99MguU4uDCKRej_9yKu2rEywHlHrFbd59dEci9mvGHPOcDDcbzrlJTMFQK8CKbpSvb7NsTXLe1nNlmuR47if9mZQmGee_jCegtukbeYRIerIaPRLKkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6e6ad8a31.mp4?token=UsZJj4rLzNrK9ORz3-fBDSTwSA3D-YUhTd0mkYdnf3y5ZW_99yMtEk1EzsU2QvV03V4RlDpeXgcNkTwsT_SWTyOtOS-27Z_mq7oSL7b-lIr0LWQ6XTL1DH9L180I9JLTK7wO5ywendQVs-yMWrooj-D9DntDTic6_QUukc78LqbYuvYmo0MIKe1N7wHBLnlx9lqj9RWtjroq5JDLZnDH58BBnhNQAXE6NEN99MguU4uDCKRej_9yKu2rEywHlHrFbd59dEci9mvGHPOcDDcbzrlJTMFQK8CKbpSvb7NsTXLe1nNlmuR47if9mZQmGee_jCegtukbeYRIerIaPRLKkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلاوت نوستالژیک و معروف تیتراژ سریال یوسف پیامبر توسط استاد کریم منصوری در محفل اربعین قرآنی ترین رهبر جهان اسلام در مشهد مقدس
@Farsna</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/456895" target="_blank">📅 23:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456894">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvkKXha0mDH_4uWpAwGHE3TP0WqXxhlPWS4ry-IVzNGkj9dt7jdvNnJSnA1DPNBjTzG6VLfteF-d5G6hboCMNj00SPDDUxjUFgDehngRUrMzuBbUOeGxuK5GHGw-TgrxemBSzN8GlqHm88Dn7pjBK-CW2X0utISTnn7oI8_9dHpNIsVkn-73WGiUVuM4t3QYGtSZufqPHrRq6cbheJ_izR5IZZiA0hfiVtofTa5BWfMlKkPgVDZOcIn1wMx-eejy94GGhD1SdAc3EclGqKUtNiO_ZtuBY29lQoQNv33kx06tuqFi8utFr2gTkCdXhf2Abg41XuH12AGWc-hJaD09jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نایب‌رئیس کمیسیون اقتصادی مجلس: روایت واقعی از چالش‌های اقتصادی نداریم
🔹
بزرگ‌نمایی صرف چالش‌های اقتصادی و نادیده‌انگاری فرصت‌ها» و «برخورد سیاسی با مسائل اقتصادی»، ۲ اشکال جدی در فضای تحلیل و روایت رسانه‌ای است.
🔸
روایت واقعی از چالش‌های اقتصادی نداریم.
🔸
مدیریت روانی جامعه در شرایط سخت تعیین‌کننده خواهد بود.
🔸
مولدسازی در کشور تعطیل است.
🔸
باید مدل جدیدی را برای اداره اقتصادی کشور خلق کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/456894" target="_blank">📅 23:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456893">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/454ca97fd3.mp4?token=O3PiEhE6-yYrAfpswo6RGDUrgG1PLMWKXh4qLzhzhrRFXgtm38qOxkDc8_Lh8dLQ2EfNEooHCY8pVRY6PAG1HW6z8uXiLauTvwhP5tRc_TXrfZU8rApigdMfY_46QTguZ8vEPJ_-YI0Tn1wIfgjUlNt8H9JoVqcqLBGVvVIGsFIBZUqyA4IZbaABVBFbii4x4d73B8J-3wGBg84Im-UBAW0c1DAnjFF83Z9szjS9OfkrRg8SJVlDFK0000oXzlXH6uigto61gG0_D3E_Q5hHGK6AsGDYERJ4LGDBkXDhhX5NLTHtLEHlGEp9HDBKKw1yGXdep69EpqYDp78YL0wpOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/454ca97fd3.mp4?token=O3PiEhE6-yYrAfpswo6RGDUrgG1PLMWKXh4qLzhzhrRFXgtm38qOxkDc8_Lh8dLQ2EfNEooHCY8pVRY6PAG1HW6z8uXiLauTvwhP5tRc_TXrfZU8rApigdMfY_46QTguZ8vEPJ_-YI0Tn1wIfgjUlNt8H9JoVqcqLBGVvVIGsFIBZUqyA4IZbaABVBFbii4x4d73B8J-3wGBg84Im-UBAW0c1DAnjFF83Z9szjS9OfkrRg8SJVlDFK0000oXzlXH6uigto61gG0_D3E_Q5hHGK6AsGDYERJ4LGDBkXDhhX5NLTHtLEHlGEp9HDBKKw1yGXdep69EpqYDp78YL0wpOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایندهٔ محیط‌زیست ایران در بریکس از خجالت اماراتی‌ها درآمد
🔹
خورسند، نمایندهٔ سازمان محیط‌زیست در اجلاس بریکس به سخنان وزیر امارات دربارهٔ حملات ایران به مواضع آمریکایی در امارات واکنش نشان داد.
🔹
او گفت: هر کشوری با میزبانی از متجاوز و زمینه‌سازی برای حمله به ایران، بدون تردید با عواقب عمل خود روبه‌رو خواهد شد.
🔹
هرکس بذر دشمنی با ایران را بکارد، سرانجام میوهٔ تلخ آن را درو خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/456893" target="_blank">📅 23:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456892">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‌
🔴
وزارت دفاع امارات مدعی شد موشک‌هایی که ساعتی پیش به‌سوی این کشور شلیک شده ازسوی ایران بوده است. @Farsna</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/456892" target="_blank">📅 23:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456891">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwO_0SZovPuPJ57oNC7MKj57Bgd0wT3vEqy5KP7npLIgio0cUeD6kxKULnE687jt9FccERiEHnbO8D1imvpYpKYnOMAAYuP20HVVK-1BAu9ICaO1_02q4Ip_0_k_fVKT00TcBotufv1gSTuIGGDJEJ42ZEtl6xlgsxIjIBnu2N9em7rkzmTIgukFRWQrfaRxAxsRBSt2EboXu8IFOqzc8qiseN23WtK5qaJKt9t7Zy1RDnQP_BkSGk5FYjvxgVGaBwpOn_Ea5TYm6UgVjn7CHPr0tMjvaV1UN5Yc2YlEMFj_kRvu30pTuKISJlPlDFVkiIKBZm8u_nbYLbClgZREYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام درحال تبدیل حساب‌های کاربری به وب‌سایت است
🔹
مدیرعامل تلگرام در حساب شخصی خود نوشت که تلگرام برای گرفتن دامنهٔ سطح بالای «.gram» درخواست داده است.
🔹
اگر این درخواست از سوی سازمان آیکان (ICANN) تأیید شود، حدود یک میلیارد کاربر تلگرام می‌توانند دامنهٔ شخصی خودشان را داشته باشند.
🔹
کاربران می‌توانند فقط با نوشتن یک جملهٔ ساده، وب‌سایت تعاملی خود را بسازند و این وب‌سایت‌ها روی سرورهای خود تلگرام میزبانی شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/456891" target="_blank">📅 23:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456890">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96802d4300.mp4?token=WWWNOF5koXhWWqhZKJrpwDGu2QuW2iVk3Q-0Q_HmwNO2Tg5or-Tf2WmJUmE7MrcDk81CagCEQw74i8dZUFNUjVl0dJMbipalOjWNpa9825MAholHaBldjeRtUgu4T62CMjA90epyUeC7ZHix5nlkeIxaNVQgWeOxPiJ84bGLpBkYOQDHUy_Dd-EIOPqBHb-PH9sat9YReoZdwkAOFjnW9EUl42TjAL9dN0BTbT-MfGYGAaFarDJGDg3QDvB1dAu-sd9il623GIwv6lMPOjh4wPo9Hdn59jzOCwjaXGWTqSnP4MKT9OXux4DHq7lpy9bV3MH4OM_0CdICyGPAtGp7mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96802d4300.mp4?token=WWWNOF5koXhWWqhZKJrpwDGu2QuW2iVk3Q-0Q_HmwNO2Tg5or-Tf2WmJUmE7MrcDk81CagCEQw74i8dZUFNUjVl0dJMbipalOjWNpa9825MAholHaBldjeRtUgu4T62CMjA90epyUeC7ZHix5nlkeIxaNVQgWeOxPiJ84bGLpBkYOQDHUy_Dd-EIOPqBHb-PH9sat9YReoZdwkAOFjnW9EUl42TjAL9dN0BTbT-MfGYGAaFarDJGDg3QDvB1dAu-sd9il623GIwv6lMPOjh4wPo9Hdn59jzOCwjaXGWTqSnP4MKT9OXux4DHq7lpy9bV3MH4OM_0CdICyGPAtGp7mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم کرمان در موج ۱۷۱ خون‌خواهی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/456890" target="_blank">📅 23:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456889">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYQRyRYH6F6_O5q4TO1euYaYjID6ztuHDbTKMgbKDviSsI60ohMgROtuZmxwKORNzXVsbQSQ5RKyYAyqCJ5xxLKkpJ-E3eaXfYZaD0vm6Q6fIDnKLuGmj947Jw24VLBPXteTeDOsbThrelvjUO_bgEuAX1DzOEwlraGNvX8aXs4IJ4yuH3z8yLPBtAIwDUpfHJvLqtwNgesA-FQu2jTR0IQZ9YAB7Oq4eFvhwvnEbwWQTVWB2AlweeqexZN7_y5mWBCpCToR0ESNxfYqUl1fs5JXbwEjYWK-fagbgnf7_UwC00wtvw9SRJhsH6xrYHXm-sEnvNBNnRgXgU5Y-d-_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقوع حادثه برای یک کشتی در نزدیکی آب‌های یمن
🔹
سازمان تجارت دریایی انگلیس از وقوع حادثه برای کشتی در فاصله ۴۰ مایلی بندر المخا در استان تعز یمن خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/456889" target="_blank">📅 23:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456888">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd8d42719.mp4?token=FijIKHz6TelEWVwfAMVtcg0rxGeZxHIXEWdlKfYuamUSZexV1XCuO4FFf7Y2Okoj74FFoeKDcYzCXBtBryh1H-kvgkelJ47QXwP_3-6oQaP06BctFyxmPlO7brNOApXXcShPl6qjS-jTMRugar3-Rc3QQN6gFZzhPLblAbFgeToSSuyz3qJZsAyOyjhAoGb8TKb62SZxfnsl2_tbAXknMexyd-QWFZ5z4yKoMukMC_DHDn5Uuv_epqGFRuBT1W3GfJj7dv13OZY3YW7sFNix1QxRxSM9IiYl1ih6abjnSvAgvkGg32BXnjzjXSXJlXYo1BmBXPETxiHpl2suCm6YMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd8d42719.mp4?token=FijIKHz6TelEWVwfAMVtcg0rxGeZxHIXEWdlKfYuamUSZexV1XCuO4FFf7Y2Okoj74FFoeKDcYzCXBtBryh1H-kvgkelJ47QXwP_3-6oQaP06BctFyxmPlO7brNOApXXcShPl6qjS-jTMRugar3-Rc3QQN6gFZzhPLblAbFgeToSSuyz3qJZsAyOyjhAoGb8TKb62SZxfnsl2_tbAXknMexyd-QWFZ5z4yKoMukMC_DHDn5Uuv_epqGFRuBT1W3GfJj7dv13OZY3YW7sFNix1QxRxSM9IiYl1ih6abjnSvAgvkGg32BXnjzjXSXJlXYo1BmBXPETxiHpl2suCm6YMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سلامی به لبنان از بلندای بام ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/456888" target="_blank">📅 22:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456887">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NcOLwLkAqfedcHVhiZA0RNOECV4O8p-UgLcOvB613eW02GbQxNjd-e9qq6xsrweSnsK3ELXkt6VJdCzK7RQtLPu9J8lB39ySYUSXoV0waR6GNJhvMeU60-fJZGQjWyf0ObSB2YhQ5x5M2M6EWAwbiNmXnUq-qzol76YMHSLm_O0fQCNwlJMfFOyllmzUgSk_zoBiKThglqpUKu1kO0FPGgKO3tX4S2DNmvGZpZeyD9Jo9B0piRzcMKqNCWekMrY78JKKX0ibQbvvJkrpKA6LcAaTNhzJBa6vtRdEtJWER2No-zTDaYNrwuTVLg-IuiXuJ9OoaTJSWiHjVkB7pwo63Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
به قعر خلیج فارس فرو خواهید رفت  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/456887" target="_blank">📅 22:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456886">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpG-KckVB7GSDPibJKBQxrnt86tmQncxHUzXqSoFanHtdUAgP9Gx5Jn5gwNXZSdEkQHJDQSyPTe-IjOu2MgkA-lwJXq2JsLn_lPqGQH60o2rNJA3JTjZ3ZEpevq8YkDDw-5qsb-9wLwARv9Rb3jzPWAoYZSxgOi7Y68J3kulaTjJrjKmuthrrBMTRrZ72XfmV7kJAfuLuPKY21QI7Tl_G4uKvLMKLhyzqVTE23FAAgpz-ZVQmYXdtN1UqmHCGCXu0PSBVQltMspZaJcqveYVV8v949nvVhDL2Wn8Cf3-XQeUu15SqTMBBsC5gLRVzQ44kMIIDVNCHutd8nkU76RJVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علنی شدن شکاف میان ترامپ و ونس درباره ایران
🔹
ونس هفتهٔ گذشته در گفت‌وگو با فاکس‌نیوز گفت که اولویت نخست دولت در قبال ایران، پایین نگه‌ داشتن قیمت بنزین است و پس از آن، جلوگیری از دستیابی این کشور به سلاح هسته‌ای.
🔹
ترامپ روز دوشنبه در این باره نوشت: «هدف شمارهٔ یک این است و همیشه خواهد بود، اینکه ایران به هیچ‌وجه و به هیچ شکلی نتواند سلاح هسته‌ای داشته باشد.»
🔸
این شکاف نشان می‌دهد که این لحظات از نظر سیاسی برای ترامپ، ونس و حزب جمهوری‌خواه تا چه اندازه دشوار و پرچالش است.
🔸
نظرسنجی‌ها نشان می‌دهد که اقتصاد و قیمت‌ها از جمله قیمت بنزین، مهم‌ترین مسائل برای رأی‌دهندگان در آستانهٔ انتخابات میان‌دوره‌ای امسال هستند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/456886" target="_blank">📅 22:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456885">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc1ee44735.mp4?token=AB3vU6rlFsPdbN0ELOBq3wHSkMfVMEiMHwy8bba590OCclrg272cRTslIf_pTlyIg7EJaukk7JaXwCOiZYcYHe6934-5lAmSCUMQ_o7rulqz8iJR3v7A05rZSyxlBgn1OnnBwfMfSCFdmrPEr84Aifu9IIV60LJM0A1SeZoqcEa6vLtRB-sfKeE6J3zFoSasjs8jxp9uvTCAPEoZY0fAsvOth4P2fkmzXJuGgXW0ogA6YCVqtSi_fzYqBhUdpA_FgglM1MSEdg40rSN_ZxJNYE44rB4gSfvQqRJII_Y7Y0sGUj077DjmX-TTA45clRNn1RZZgFrPkk0Ct2YWG5thaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc1ee44735.mp4?token=AB3vU6rlFsPdbN0ELOBq3wHSkMfVMEiMHwy8bba590OCclrg272cRTslIf_pTlyIg7EJaukk7JaXwCOiZYcYHe6934-5lAmSCUMQ_o7rulqz8iJR3v7A05rZSyxlBgn1OnnBwfMfSCFdmrPEr84Aifu9IIV60LJM0A1SeZoqcEa6vLtRB-sfKeE6J3zFoSasjs8jxp9uvTCAPEoZY0fAsvOth4P2fkmzXJuGgXW0ogA6YCVqtSi_fzYqBhUdpA_FgglM1MSEdg40rSN_ZxJNYE44rB4gSfvQqRJII_Y7Y0sGUj077DjmX-TTA45clRNn1RZZgFrPkk0Ct2YWG5thaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۷۱ شب حماسه و اقتدار مردم گرگان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/456885" target="_blank">📅 22:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456884">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bd366c5a3.mp4?token=oVzIIitdC-EeBnjlHbdcaX-uB7zfGFSueTz2BitiBI_RvF8Czil0lzLAm_93mo4KwwPx5LEuXel3kLJ1qvwRvnNv95xi3Ngoa-Bm2iQ7kV4DzYvcoPKOb-GD8Ucu5SN25vGzC0d1uCEre2QQDjsGCGs4dmgOHpL17Yj5hMGUPVezjjgwW_-Q_7rBerRPH_JSDWitxs-Yhvk44aQp4PjCQ0nEt0bvCCJ__0M7KOn1duSsS2TCx8bqb19wGkAUpmBhRyZrOC2Zdmo6mzDJ6gYlPM9Z1P5tPaXEytSJ2YKHrVZJL8SpcAQaEEgbuc4LXyIqqprafTgdKDFSCkQVF8pBBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bd366c5a3.mp4?token=oVzIIitdC-EeBnjlHbdcaX-uB7zfGFSueTz2BitiBI_RvF8Czil0lzLAm_93mo4KwwPx5LEuXel3kLJ1qvwRvnNv95xi3Ngoa-Bm2iQ7kV4DzYvcoPKOb-GD8Ucu5SN25vGzC0d1uCEre2QQDjsGCGs4dmgOHpL17Yj5hMGUPVezjjgwW_-Q_7rBerRPH_JSDWitxs-Yhvk44aQp4PjCQ0nEt0bvCCJ__0M7KOn1duSsS2TCx8bqb19wGkAUpmBhRyZrOC2Zdmo6mzDJ6gYlPM9Z1P5tPaXEytSJ2YKHrVZJL8SpcAQaEEgbuc4LXyIqqprafTgdKDFSCkQVF8pBBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۷۱ شب حضور مردم مراغه در رزمگاه شبانه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/456884" target="_blank">📅 22:09 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456883">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnFYlt5yMc_d8WM1X15Bn6-laywr4NBBrmx1vjLhdemV9EzalPPj8NZ7eWunEqNso7uixeuIOZgipT6PJaxT9wwqMiftBHmPaSn1r71WNEW_LVAtdSBe-1n7A3He6ZCSXyguHt6tAJszO9-Ci9g_FxU-Ws5TOqyYipUsgL2NGyL3N9d5B_Z82kqP9vTsLZUF9_FpZ8c-emVxMzAkrztRPnuYYD99W22bMZmAoGm7YTKZI2dkRZTe7w-ZlmQGsHwWmrjgwEFrdGsCMcbtC-foixrZo-SFvJErw4tw0kakWNC_WcDfpY5ATAHL3Gl5AKgWqRjhkSxatI_AdsJfYO_zTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
گل دوم تراکتور به سپاهان توسط حسین‌زاده در دقیقۀ ۹۳
⚽️
سپاهان ۰ - ۲ تراکتور @Farsna</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/456883" target="_blank">📅 22:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456882">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17581cbfd2.mp4?token=N3k5Z39m85I6VqmNb1WTHnyXp4eESpFUbwlPn8K8G0otdA3fmbD5Mi1n2WVLa2Ra_pePyPI7n9NAGYQWoYZDzXPbdbWuwEbYsba6MM5tpB5R4pmGxxXVKliy24hpuNTgts822Syak_Swi6ZvUqleqwCQeGqARRCv_bSQII-0a-TQpWGfSQj-P3GZvO_WDIUUs2HUCdbjupRDvT8NIcA6S8dP5SAIVlj5fTN-bTu6WYMVYiZXRnnSYXH3y2tf6Rt7iM3KUT7Zchg99b4WveYPXajjVCA_t-5G6kQfihHsdTXPCuPdRbgBjSgoCSTiKLKwkBmkKDklJL5MwgBeEIzo2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17581cbfd2.mp4?token=N3k5Z39m85I6VqmNb1WTHnyXp4eESpFUbwlPn8K8G0otdA3fmbD5Mi1n2WVLa2Ra_pePyPI7n9NAGYQWoYZDzXPbdbWuwEbYsba6MM5tpB5R4pmGxxXVKliy24hpuNTgts822Syak_Swi6ZvUqleqwCQeGqARRCv_bSQII-0a-TQpWGfSQj-P3GZvO_WDIUUs2HUCdbjupRDvT8NIcA6S8dP5SAIVlj5fTN-bTu6WYMVYiZXRnnSYXH3y2tf6Rt7iM3KUT7Zchg99b4WveYPXajjVCA_t-5G6kQfihHsdTXPCuPdRbgBjSgoCSTiKLKwkBmkKDklJL5MwgBeEIzo2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول تراکتور به سپاهان توسط حسین‌زاده در دقیقۀ ۸۳ روی اشتباه حسینی
⚽️
سپاهان ۰ - ۱ تراکتور @Farsna</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/456882" target="_blank">📅 21:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456881">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/617832e930.mp4?token=sOGH4C6Klt180915Bydf3l8RghFrtvi8eHVmE5LQFoEQggCOXVWvpUGzbn4e7Hqxg5iPAGuC1Lb8ZNWIR1JWV1_hx29wCA3OjZlFfgg2TiwLZNOclOyRZYJIgTPAymN5tyiFP_xN44Tr6MoIB3TmdO1Bhg7BLiCAU_YlqUJrwC6osWtDsYHNJ_LLRUh4_6WPTL2luQOdycP8MFo1Pocvt92YFak2lA4bjQday2KhqhFpEn-_yZ_5mNYrj61eOn0N05xYVhPKxS6MmP52pAHHOuRdLqOXEHqvd9N2F-K7ljvE7A-FmVpQa6OdRPm_JhewJxSZwCgpekILrE7VwVpnoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/617832e930.mp4?token=sOGH4C6Klt180915Bydf3l8RghFrtvi8eHVmE5LQFoEQggCOXVWvpUGzbn4e7Hqxg5iPAGuC1Lb8ZNWIR1JWV1_hx29wCA3OjZlFfgg2TiwLZNOclOyRZYJIgTPAymN5tyiFP_xN44Tr6MoIB3TmdO1Bhg7BLiCAU_YlqUJrwC6osWtDsYHNJ_LLRUh4_6WPTL2luQOdycP8MFo1Pocvt92YFak2lA4bjQday2KhqhFpEn-_yZ_5mNYrj61eOn0N05xYVhPKxS6MmP52pAHHOuRdLqOXEHqvd9N2F-K7ljvE7A-FmVpQa6OdRPm_JhewJxSZwCgpekILrE7VwVpnoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای بیلبورد جنجالی در اسرائیل که در فضای مجازی سروصدا به‌پا کرد
@Farsna</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/456881" target="_blank">📅 21:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456880">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ورود ۲ دیپلمات فرانسوی به ایران ممنوع شد
🔹
وزارت امورخارجه: با توجه به فعالیت‌های خلاف حقوق بین‌الملل ازسوی ۲ مامور شاغل در سفارت فرانسه در تهران، وزارت خارجه این ۲ مأمور را به‌عنوان عنصر نامطلوب می‌شناسد و ورود آن‌ها به ایران ممنوع خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/456880" target="_blank">📅 21:55 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456879">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b59b18635.mp4?token=o5MxRhhzsMt9maOtWUE9goXizIFUA0xy80AcL0jglDh5CVfu8TfSJFiGOu1vr9ZsX-0LGiQsUlPvBdc_aJn7XHrboA8IdKTVt_PuX9_BU3JGjRJ3JbKbVPDaZygbctwm0YXmoRkXLjGva51BEdgs1QvpURNojmXC-1X2p_Eq6M-bI12wPvRqQq2_glmva9HGGtCFjK39X7FD-GqFtSwyzIhG7sDyOR9Cw1qIlUMTPDXEP0FRO1O3hA3HAnEA7TS-iSZ-x_SooailVr8I95szQxd_3F80dEKsLWqCBGA4PymAk69Zd1tNNOr0CFUoQ36SsSHsdC6BXt63IsqwzKaoUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b59b18635.mp4?token=o5MxRhhzsMt9maOtWUE9goXizIFUA0xy80AcL0jglDh5CVfu8TfSJFiGOu1vr9ZsX-0LGiQsUlPvBdc_aJn7XHrboA8IdKTVt_PuX9_BU3JGjRJ3JbKbVPDaZygbctwm0YXmoRkXLjGva51BEdgs1QvpURNojmXC-1X2p_Eq6M-bI12wPvRqQq2_glmva9HGGtCFjK39X7FD-GqFtSwyzIhG7sDyOR9Cw1qIlUMTPDXEP0FRO1O3hA3HAnEA7TS-iSZ-x_SooailVr8I95szQxd_3F80dEKsLWqCBGA4PymAk69Zd1tNNOr0CFUoQ36SsSHsdC6BXt63IsqwzKaoUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول تراکتور به سپاهان توسط حسین‌زاده در دقیقۀ ۸۳ روی اشتباه حسینی
⚽️
سپاهان ۰ - ۱ تراکتور
@Farsna</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/456879" target="_blank">📅 21:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456878">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9312fbcde3.mp4?token=Zjn-NlMBlHHx1hMuCo4DfutJhDW3Ixmzj5k4WfSVwVMMkhCuUwQWkhdwMyk9RG8C3096tHFbfi2k-UpqxuwdF4dT6MlUOQJ7CZXMcjeL5Ov3gwuMug9P_T5PhH_j-kSO4vwhZK0j1rbUNRXwSL2BFY2Ei9Jp5_uCEenyKej6gxrisHo-A__PrOTZy_SVST9Mk1p9yXZ3fbLJUBFmFt1Z2qyU5em3dR1-9wm3JYQk_agoeel94eTZsShpkXbDmtdChy9l5AaLWyIDy9y2FnRtRIbeqP-x8HTzxqR7yRX2WWJk36OEH9ldZowq6AR99mLNZgK5jewtuH4z6Hioaqn5Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9312fbcde3.mp4?token=Zjn-NlMBlHHx1hMuCo4DfutJhDW3Ixmzj5k4WfSVwVMMkhCuUwQWkhdwMyk9RG8C3096tHFbfi2k-UpqxuwdF4dT6MlUOQJ7CZXMcjeL5Ov3gwuMug9P_T5PhH_j-kSO4vwhZK0j1rbUNRXwSL2BFY2Ei9Jp5_uCEenyKej6gxrisHo-A__PrOTZy_SVST9Mk1p9yXZ3fbLJUBFmFt1Z2qyU5em3dR1-9wm3JYQk_agoeel94eTZsShpkXbDmtdChy9l5AaLWyIDy9y2FnRtRIbeqP-x8HTzxqR7yRX2WWJk36OEH9ldZowq6AR99mLNZgK5jewtuH4z6Hioaqn5Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس پلیس راهور: ملاحظات ترافیکی هر مجموعهٔ پرمخاطب، به‌ویژه مراکز تجاری، باید پیش از ایجاد آن دیده شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/456878" target="_blank">📅 21:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456871">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gIuYl1J8_Qku7CNkLj3jqRCdn2XJOL3Z5VbBA3pe9y-yvLdqt7QI4N5Qjiktiz_N9a8ujYv0hSblaLJazUrqcHYyv9Rvesx69ekSDd84GkvNAiYfd4ZwuOD-ssmyItJT75Jt-p3f1k24-8Bk_DCz0DubSIqwiOxJJpYTt1aKLLjLfYfrqHpD_XqFoH6dG6ei5Gj78bLC5Pd9Jsk0it5nSMnR8yq33E7mDpIA6KKMtl0JF-avIVZTB_ezkAk3wZYDI_jEmC_25ZyucPXxrM_wJ8sMldxXcWam_G5j7T8npq11LrroMkOwYzo9T1V8OgD45JPPfV2h5AvZP54J73hW9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U6rpjOgsFQaqNIMtoz8cMH6oFS93twZxsKl0sYf6aH6yuDZEiyL4djmK7XOObX84RNWL8c2qaVSigmffShQ56VV-NnJMaL11XNjoM7FMLduYYbErHJh_3Vo-ZwL66go6oyZo2U0Htixt1-0Nq_2gAeaRbEuemSMOD0A3147Hvy6mNQ8FFtDbkjGWySNe-c-lkuHoCWBTYBJvm9Z293e0bXC1vnqiriT-bu6nVOzXf37xCwNc63rwmT_sBy51prtijm4C3-MJoPGHCvh1KqkOELYUAEejlCKBrUcwv1jZrFj-3c6ZVoY5ouJ6CNcBuvJKs-hnP-wLJhKedQPDJkvQ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LsIXUewnFWKzMmKGva3A2rmRabThg25LPpbzyTpXB50l5-gfaFdM_jlGMupGPcF9Ypgaype3WKB4AWBuKdsheogHAC-LAaqLv1MqfaQn2nRJGnfg45jJpN0yoxtxQgAkG4mJcfBi9Vj1wePKGaAiEoi8e_5jmCBxA9hDFetaLTMJSnvZr-Obph_IOlJPU_0gxqNwFHxv7CxIjV_jUkiA6ALMJtZhF8yrGnI64sRe-4YYRV1UGkBf5S7C0iuyM795xrfSll_F8ozGk_9Z1Z5e8PW1SM37TBnpMekwthTWBV1rDRwYt_pSZqecg-QO0vq4G3Rw4qdQEBuJn5hgcS6ayw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pnPxqTTlG-RzyIX8kMAESzBN6JJlrsC1Q-9E6ecPz2Vqlog200lXIJhC1GwROm2KqPIpC01Y65LZH_X09sproWL9baej7gwIUiglaPmErC_YmW2UrPFJBPGfI9hgBaYJ3QNyUH-NVu2izGK4SlyG-ekBoqjSwDZTnmBFDVEfmrkCoKT6ZdOSeNNuCeOgQeNqNFhJWylrkOEHGr3h7_jiuA2CyCJJtecmkAjE9J3IBbG3HIYt_nLisl16c-jG13f2dAI6kEbtiBUGqfMyV4bt0tw5tTBxPu9cW9Bcn2vz3k9oV0eopvr9U2IJuyCvhrObJiJesOT5OeL1-qkw9gHwMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y4VrY8Pr1Cn4taHUyWM_Lnl_60kpWyjms7Ms4R192TGGCpCSAFfoBlOUR9adrzKb1TmoYzQPnClNJ9V0Ij1EgZpapyoP0s22XmZybCeZfPa6-hV4mGQjvHh7uhjBjdUFceZyzZ2FIWmwAsoZ7rEH4b8UYBicwpI8ErEu2q4RFpvb-vk6JqQDCS2hE05XPjvaCZAGSCssS-Qxq6QseDbLNpzPx2HTfkmBNdOU8yMOLLndB80CmtWt9AiXzBL7EXghVmwoHZHlKI9vwzrHL8NhKwxFnnOYl01SOUh7t6q4W9KVVNcgeRoGCnZ_lwVFsC0h7XGiiO_0X2SLq_hdIr1wCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NlCP3G-d29FI3aOS6DItxD1zaBPXLjC89rut1v4PpuuBwn-JurOr0CdMhCGryK-pV5ImHUalkyLTRq-nf1rXvtezKKqJCsfrdV9QKKIoU92RJ_qy52xypkN-sgVSO5aUd5jJOssxwrxtXIEmk6djYwVHbxZgYQwqQhsn9nKPIpU5AqyrSU27fmW85S5WwOoS8TiuB28IkhkP8-b1V6OMgGKrLSMIgG70T88hUcbumC-z4s9Vc8Iu3-I4SjBDFcdCKkDPIFsP5k4zpN-eXbPQoZbYUofI95ePUrlK23in0xRR904y2aIeHYJHRfSwLh6HbCiM2_NoP-iRsblzkvtgRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jv495AUZEzgHBVCNGHJz_KocI_bnINsi8hIu5zo7HTLhJ2Z-GCaDBAMWyey27lqXm0eVN5LUMXMVtvBg02ALdnykYhQ_AdR8yp9YGw9QMIad0XQfIHe_29Ysjo0EaRULZZ6GR7QRWzZb1MCwyugiMZzLZ8TCZ_NIwyeEzjgFnmCw8DZqj3VOnBrqOBEgTb4HdT1bTwAC19lpBn701k_zKrJPtmsKqcdLstws_9r0W6Di5etzZ6gkXC0BOA3dSrF0kiHWfQKg3pPkTehVJwqkRf4Y_5l-_mbeeWLexqII_dfRLOBPH0Gr-bNlnYIOepgi03NLENXnStpZUYf_uBlkCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم چهلمین روز خاکسپاری رهبر شهید
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/456871" target="_blank">📅 21:47 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456870">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5663417d8.mp4?token=uVxWbyBkzmd-v9JddMnxpUfNNWj0APfsSGeVDZoy-pRVg-L58_OJnRrIQkcMTFIc6kFHVLyCITC-bnChYLwMUO6R60fxl5i0heTx5rggYkdX-Xdy1fe87utymmsTDfDAQ1bCg3i6fDZ6ysJA7iF7HnnvxMK8n6nUgiqJB7HbiWmZIkGZWhkVBRQdWMiquQn_Myd8hcLRhQyqh4UhP9K1BxmgKfsjXMhukiwDIAalNpcYb2PlXPWkzt2pXdRZfTjUycpXuD4pSNiVeDuaApTG9DGyuZf3iDVfO_FHbWOM7PFP7ZpjjnvWrrg7AHR2kza-HwzDP4qTZxAaitFoBVYlAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5663417d8.mp4?token=uVxWbyBkzmd-v9JddMnxpUfNNWj0APfsSGeVDZoy-pRVg-L58_OJnRrIQkcMTFIc6kFHVLyCITC-bnChYLwMUO6R60fxl5i0heTx5rggYkdX-Xdy1fe87utymmsTDfDAQ1bCg3i6fDZ6ysJA7iF7HnnvxMK8n6nUgiqJB7HbiWmZIkGZWhkVBRQdWMiquQn_Myd8hcLRhQyqh4UhP9K1BxmgKfsjXMhukiwDIAalNpcYb2PlXPWkzt2pXdRZfTjUycpXuD4pSNiVeDuaApTG9DGyuZf3iDVfO_FHbWOM7PFP7ZpjjnvWrrg7AHR2kza-HwzDP4qTZxAaitFoBVYlAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
دیدار دبیر شورای‌عالی امنیت ملی با خانوادۀ شهید لاریجانی  عکس: هادی ه‍یربدوش @Farsna</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/456870" target="_blank">📅 21:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456869">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91104304cd.mp4?token=MRsuFeJUKZ58eEeJtpJzUqk6xI72S-ZlYcBcNRIJXX_TyFPnmDhp2rJR1Es5T497xWZ1RQIa6sKGc3lG-HFxU-GJmibxlbd3bEMfR5NdUn15xjNlITckYed-vL7w_vKsq5s5BgGxZnG0Tn9-f-vlis1cWrHaBFUDF49DuLn9W2VRFcYAwCKncZge3IX6q4_ZmmBHAuGoCGvzebRmNMDPGmXbubbo6ey5EPOn8X4DMfrs6i-n1pFyBJGkHx9BqIjs9LyTf32Oh_6AoRnvqnicF2CvqQSKEowPjhE2HnFbdl35W64c0n_cLZ8_oh-tj5mpn90sv4Obcw09R5CJYeP6pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91104304cd.mp4?token=MRsuFeJUKZ58eEeJtpJzUqk6xI72S-ZlYcBcNRIJXX_TyFPnmDhp2rJR1Es5T497xWZ1RQIa6sKGc3lG-HFxU-GJmibxlbd3bEMfR5NdUn15xjNlITckYed-vL7w_vKsq5s5BgGxZnG0Tn9-f-vlis1cWrHaBFUDF49DuLn9W2VRFcYAwCKncZge3IX6q4_ZmmBHAuGoCGvzebRmNMDPGmXbubbo6ey5EPOn8X4DMfrs6i-n1pFyBJGkHx9BqIjs9LyTf32Oh_6AoRnvqnicF2CvqQSKEowPjhE2HnFbdl35W64c0n_cLZ8_oh-tj5mpn90sv4Obcw09R5CJYeP6pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: وزارت خارجه تابع دستورالعمل‌هاست
🔹
کار خودمان را براساس فکر و عقلانیت مجموعه نظام انجام دادیم. @Farsna</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/456869" target="_blank">📅 21:40 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456868">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5IKO4pCbWqoUTiOQk0yY7fdtQEX7Gfoi2AIBgC2gKmX7Y7rpqkISlqxgrt2Q-abrGl51ppaBJ6Il20WrPfGufsVS9mjEs78hBfDqUL23JtOGBiEKOAlPFTtbealPDAOD9_QiLPGrhcElttWOUmVyw8-7z2U9ziXqhZPxxI-x3XS-8di6Zi_Cp1inX3NMY_SI6-8mMlE7yedO2QtqBrOxj2n3AExmyJBPz8UhyfadIY4Spx_48-XGa2YpBiq3aJIkTnBRTldqB9xrg5Ws5eZ3MHjhfrfPhuupMUWsR3tzP_uV4PP65sqfWp27J9eqLDlOChQnNDNd7FdsVaOa-KxGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان بسیج: رسانه دیگر «پیوست جنگ» نیست؛ خودِ میدان جنگ است
🔹
حجت‌الاسلام طائب: جنگ دیگر فقط در میدان‌های نظامی اتفاق نمی‌افتد. امروز میدان مواجهه، چندلایه و پیچیده است. یک تصویر، یک خبر، یک روایت و حتی یک سکوت می‌تواند بر ادراک میلیون‌ها انسان اثر بگذارد و مسیر شکل‌گیری افکار عمومی را تغییر دهد.
🔹
اگر تصویری ثبت نشود، روایتی گفته نشود و حقیقتی به‌موقع روایت نشود، میدان روایت در اختیار کسانی قرار می‌گیرد که می‌توانند واقعیت را آن‌گونه که می‌خواهند بازسازی کنند.
🔹
خبر می‌گوید چه اتفاقی افتاد؛ اما روایت می‌پرسد: چرا این اتفاق مهم است؟ چه معنایی دارد؟ چه درسی برای جامعه دارد و مردم در برابر آن چه نقشی دارند؟
🔹
رسانه زمانی می‌تواند مأموریت واقعی خود را انجام دهد که از «خبر» به «معنا» برسد؛ واقعیت را کشف کند، آن را درست روایت کند، به جامعه یاری برساند و نسبت خود را با آن واقعیت بشناسد. در این نقطه، رسانه از یک ابزار اطلاع‌رسانی به یکی از عناصر تولید قدرت ملی تبدیل می‌شود.
🔹
جنگ ممکن است در میدان نظامی متوقف شود، اما آثار آن در ذهن جامعه، اقتصاد، سیاست و رسانه ادامه پیدا می‌کند. پساجنگ، عرصه‌ای برای تبیین، تحلیل و ساختن آینده است. اگر واقعیت‌های این دوره درست روایت نشوند، امکان دارد روایت‌های ناقص، تحریف‌شده یا ناامیدکننده جایگزین حقیقت شوند.
🔹
رسانه باید بتواند واقعیت را کشف کند، حقیقت را روایت کند، تحریف را آشکار سازد، ابهام را کاهش دهد، اعتماد ایجاد کند، امید واقعی بسازد، تجربه‌ها را به دانش تبدیل کند و جامعه را برای نقش‌آفرینی آماده سازد.
🔹
رسانه‌ای که تنها خبر تولید می‌کند، بخشی از واقعیت را منتقل می‌کند؛ اما رسانه‌ای که بتواند میان واقعیت، تحلیل، اعتماد و کنش اجتماعی پیوند ایجاد کند، به یکی از زیرساخت‌های قدرت ملی تبدیل می‌شود.
🔹
شاید آینده جنگ‌های بزرگ، نه فقط با موشک و اقتصاد و دیپلماسی، بلکه با روایت‌هایی که در ذهن ملت‌ها ماندگار می‌شوند، شکل بگیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/456868" target="_blank">📅 21:33 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456866">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvuFt1jtFvoaKM2HfjHxq0phPPKILR9QnWhDtL3_FgfC3EAt5fxuNYqnQCZPGPLMEpVFSjyfkiIlGe9wmfyCTEcctaEtfbkOQwaEyOCvwF_d-6ReEWuor9HesVTVi-ufl6EmCy2Cq0dwxpvKt9bRELpq1yadbUB8b6DRcxWp-DavC-y-kU-MhMi2AEWlD7m_eKsow3eN30Kjd4tEGBOgWFQTn6s4T-8I_B5mT0O2SaaJQpEaNh9IfggPuHtpyBCoW9_kOb-Zhq56hUi_n8F3NcnJl1HHyH169yLHxX4Q4YuoTMfa8qfC9BzqQKP54rtWZu7aYoF6XYJMtKeqkaI1IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا رئیس دیوان لاهه را تحریم کرد
🔹
وزارت خزانه‌داری آمریکا، توموکو آکانه، رئیس ژاپنی دیوان کیفری بین‌المللی را تحریم کرد.
🔹
این تحریم‌ها هرگونه دارایی او در ایالات متحده را مسدود کرده و تا حد زیادی او را از سیستم مالی ایالات‌متحده محروم می‌کند.
🔸
دیوان کیفری بین‌المللی پیش‌از این حکم بازداشت نتانیاهو، نخست‌وزیر و گالانت، وزیر جنگ رژِیم صهیونیستی را صادر کرده بود.
@Farsna</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/456866" target="_blank">📅 21:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456865">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8bb41218d.mp4?token=u1jgWq2jP5dFYaSt1S9IgNxXdQK6465Z6PG02lAeUHhITlJ_b28dhB6exdByjytez4GNQzY2ItW0k1Wt2D8M8VFnq5kJO4u5BW6jtaUzWk0sh2ilgKWIPMrd7XJc_95gCGfCxvGPLEvRm6oDOnHwhaPRiuYzbFf7tR_nJMSwCKxBqZi-woqt3Y_ZEqq-jXCl1IyS5nUramgqGl2MeLyHhHgOFvJLawyKiJ91yRRBQ97VOQCgHgOnsEHYsSZL7rChAAeKJalhLRozdBzJya4KYbOEFl2RR-HIL6W4PmBqu1AEuHGpfBqI6Zkda6T3G4DORzFNBy7O4BWu3hr7_bB8pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8bb41218d.mp4?token=u1jgWq2jP5dFYaSt1S9IgNxXdQK6465Z6PG02lAeUHhITlJ_b28dhB6exdByjytez4GNQzY2ItW0k1Wt2D8M8VFnq5kJO4u5BW6jtaUzWk0sh2ilgKWIPMrd7XJc_95gCGfCxvGPLEvRm6oDOnHwhaPRiuYzbFf7tR_nJMSwCKxBqZi-woqt3Y_ZEqq-jXCl1IyS5nUramgqGl2MeLyHhHgOFvJLawyKiJ91yRRBQ97VOQCgHgOnsEHYsSZL7rChAAeKJalhLRozdBzJya4KYbOEFl2RR-HIL6W4PmBqu1AEuHGpfBqI6Zkda6T3G4DORzFNBy7O4BWu3hr7_bB8pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مطالبهٔ مردم روشن است؛ کالابرگ را بیشتر کنید
@Farsna</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/456865" target="_blank">📅 21:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456864">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f810380e22.mp4?token=dLabTk5e3_DgDNJkvJp8cC0HKx1PDyX81tDYjXY2orP2wr4yQWzXxjHmWplqfwGmw7lk--m4Jls1MRPguVFOSyZIBTOmIXaBNEHGBMiuQkEg3ead7yIS5z1ntKolm3NZ4n1UcNvzaI_MvuWQvalPpo-Y0eiZ-QWeJv69cBFxH3C0HOBS8E1fsA7AkpGUp3mONejLhZ2s_pCYmDujgAtoPYfAzhWInkr2ey-VRizm1uYAhTv6lGKTfH7asx51hRu7jSFyu7OPmPHwpQVTZGIJBQ9BDNbd11Y474cdpr4r3lq8p02k_HzFm4H6PJ7S05ETJwUR_QLK4_kHVQ4nT-bq-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f810380e22.mp4?token=dLabTk5e3_DgDNJkvJp8cC0HKx1PDyX81tDYjXY2orP2wr4yQWzXxjHmWplqfwGmw7lk--m4Jls1MRPguVFOSyZIBTOmIXaBNEHGBMiuQkEg3ead7yIS5z1ntKolm3NZ4n1UcNvzaI_MvuWQvalPpo-Y0eiZ-QWeJv69cBFxH3C0HOBS8E1fsA7AkpGUp3mONejLhZ2s_pCYmDujgAtoPYfAzhWInkr2ey-VRizm1uYAhTv6lGKTfH7asx51hRu7jSFyu7OPmPHwpQVTZGIJBQ9BDNbd11Y474cdpr4r3lq8p02k_HzFm4H6PJ7S05ETJwUR_QLK4_kHVQ4nT-bq-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان مدیریت و برنامه‌ریزی تهران: بیشترین شکایت مردم از نحوهٔ برخورد کارمندان و اختلال سامانه‌های دستگاه‌هاست
@Farsna</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/456864" target="_blank">📅 21:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456863">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dadb004324.mp4?token=lAKJRBmp3vTh0NtOCinTmjz6TQnkDXOG1QxD_QHHrEXzyZAeiC0j9x8k_DaLK4kbMwKEiISzPWToSlUXozsCvaDmrGOtVhC67kejgQhoZ0LuugCTK2Gtnk2bSn4mmCO78y_pYvK8VDLWg30H3Nhb0rEseaEXQE-2hAPIVH4pD1exGwb-zQwObj18E0K7bGsW0psPzSR00zZkJCYWCLTcS6os-dssm6kHwY39jxeTv70QpF9eb79O90bQSXadDKW7lmKS54LUenat0iPx--oxLhc_a5kC9225Lf-EqiTWj_WslooY-lpVHXT4f9CFfIx2xkuoWYhwVGUapmogUFVecA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dadb004324.mp4?token=lAKJRBmp3vTh0NtOCinTmjz6TQnkDXOG1QxD_QHHrEXzyZAeiC0j9x8k_DaLK4kbMwKEiISzPWToSlUXozsCvaDmrGOtVhC67kejgQhoZ0LuugCTK2Gtnk2bSn4mmCO78y_pYvK8VDLWg30H3Nhb0rEseaEXQE-2hAPIVH4pD1exGwb-zQwObj18E0K7bGsW0psPzSR00zZkJCYWCLTcS6os-dssm6kHwY39jxeTv70QpF9eb79O90bQSXadDKW7lmKS54LUenat0iPx--oxLhc_a5kC9225Lf-EqiTWj_WslooY-lpVHXT4f9CFfIx2xkuoWYhwVGUapmogUFVecA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش میدانی حسین پاک، خبرنگار حوزۀ مقاومت از تشدید حملات رژیم صهیونیستی در جنوب لبنان
@Farsna</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/456863" target="_blank">📅 21:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456862">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372393791c.mp4?token=SGtyxsx1HBhP_BFxyCYm_-Ui0SST0XVJbqfuQLqmwquyHMz9QTPaLChNH2c6uxg9xpQWtItUkKYay_mnKPVU5loCF7EESbj2i01GclukUKHkPWiPTrwwZdMjKhhZSpDpj_OCYg7IFtKWfHKws0xEBEwsRyxT6TUC9hqeJlhdPus7PLeteFLVIdwtBO6ck0sVbDg1Wug6isbkvA2RRh9fex9UQu9xxQyRFNkXc6aNyWjbcQ-ZE6lo1ndKw96_xoBqxqoMQ_TPA_9-RtMGw8u4_bfyamUKHsvRzERp1cPmvcLdz5AKsnDtzvP4Ee7-lRR9FkJfCgGK3hiH_J-sNkESiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372393791c.mp4?token=SGtyxsx1HBhP_BFxyCYm_-Ui0SST0XVJbqfuQLqmwquyHMz9QTPaLChNH2c6uxg9xpQWtItUkKYay_mnKPVU5loCF7EESbj2i01GclukUKHkPWiPTrwwZdMjKhhZSpDpj_OCYg7IFtKWfHKws0xEBEwsRyxT6TUC9hqeJlhdPus7PLeteFLVIdwtBO6ck0sVbDg1Wug6isbkvA2RRh9fex9UQu9xxQyRFNkXc6aNyWjbcQ-ZE6lo1ndKw96_xoBqxqoMQ_TPA_9-RtMGw8u4_bfyamUKHsvRzERp1cPmvcLdz5AKsnDtzvP4Ee7-lRR9FkJfCgGK3hiH_J-sNkESiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: ظهر روز اول جنگ ۴۰ روزه با کشورهای منطقه تماس گرفتم و گفتم پایگاه‌های آمریکا را در کشورتان هدف قرار خواهیم داد.  @Farsna</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/456862" target="_blank">📅 21:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456861">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81080e2344.mp4?token=dnYGzqfoYBDPwjd5M5eBNUiIFx86Unq1yVaLyXLstX7dqtqn5FM_0cAbx4QtsG1REcMv5RozZQFqLc2pmlWMrnttS10yYNqiLmbj-0_2HV5SiEPAdCRL1X797lKI5SKiB--rWgk3hcQlXizY1XycK0CbGmbeHlB3GX_HRlbgf66k9jox-zQy5XTbHtWPns0XfNRvI8ssWgO65PhEAB_u_79Xa0g9Wz76618VDKHYtscNm1ZNzzCNYNausG822Vr092P473Lo9lHR-_tt8A-yF23PldMoXccEvlmy2AtnLb_K1ZBtZMYHajsd3deen62S--QSnC1o444uFkYcVXtSIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81080e2344.mp4?token=dnYGzqfoYBDPwjd5M5eBNUiIFx86Unq1yVaLyXLstX7dqtqn5FM_0cAbx4QtsG1REcMv5RozZQFqLc2pmlWMrnttS10yYNqiLmbj-0_2HV5SiEPAdCRL1X797lKI5SKiB--rWgk3hcQlXizY1XycK0CbGmbeHlB3GX_HRlbgf66k9jox-zQy5XTbHtWPns0XfNRvI8ssWgO65PhEAB_u_79Xa0g9Wz76618VDKHYtscNm1ZNzzCNYNausG822Vr092P473Lo9lHR-_tt8A-yF23PldMoXccEvlmy2AtnLb_K1ZBtZMYHajsd3deen62S--QSnC1o444uFkYcVXtSIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: دوست و دشمن به اخلاص آقای پزشکیان اعتراف می‌کنند.  @Farsna</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/456861" target="_blank">📅 21:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456860">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSfpPJcALdHQo_sVlRuLvqLRHV0OtRf3hMbgI_Ii8_qGqBPJt1UeOkzNq-rX-Dcbs0C-z3L2-23nxpAgg8kGdX7FBbbZO_lrI0rrlAqv52MBcr4-DeylyT5sxx0PM8M9Nm8xfiBM1KnpdmRME8Y3X22nFyabTfbkRU4Bdt3RTYpwwCi8R5zoR2rX-G1kg0ZIRv117YX758r95mit9B4ahE1gydu6Z4OR8jsSKRJ-va9YBynmuHu5N1IDucLgJTptKCczWskzW2rn_9enXzWDEm1bu3rUxvU0JHFMH4yyHCThaUOAK9R5CujejvnRX3mS2ygOqTMFYCfkeN8mdWo6VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعویض طلایی بختیاری‌زاده جواب داد
آبی‌های پایتخت سه امتیاز را از قائمشهر دشت کردند
🔹
هفته دوم لیگ‌برتر ایران
نساجی ۰ - ۱ استقلال
@Sportfars</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/456860" target="_blank">📅 21:13 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456859">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وقوع حادثه برای یک کشتی در نزدیکی آب‌های یمن
🔹
سازمان تجارت دریایی انگلیس از وقوع حادثه برای کشتی در فاصله ۴۰ مایلی بندر المخا در استان تعز یمن خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/farsna/456859" target="_blank">📅 21:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456858">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b672ecc080.mp4?token=OamHfgXYAGqMLpRAQVQVcWOFtBj2xo2srvE1cbydnCepzmuE8cFr-Qwn62zLBeWBRUvmms9f1A--XUvVnyGKiJe-0DB_-0A3pmw4cQSejFJu_aC-_KGgfMI7O44sI5SdMz1bVyr6o4wcZVjX4DWY5s7LgqKk3B3mYzYtJlHdco-2SMfrD2m9XXuiASvR3FGTVuivPKcvqKQ1KnGJ8_0eKyDvgNlTDLTVh42pRco_RxE7jMMqFqcALcZcxgKmxFqG-fQFWgBhdSma19xMyvrfnstrztHZdjBY66PoIYUE08hStJaA7mFKSmW5moz16NxXNaS2A0DLkym0VphQgOjxBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b672ecc080.mp4?token=OamHfgXYAGqMLpRAQVQVcWOFtBj2xo2srvE1cbydnCepzmuE8cFr-Qwn62zLBeWBRUvmms9f1A--XUvVnyGKiJe-0DB_-0A3pmw4cQSejFJu_aC-_KGgfMI7O44sI5SdMz1bVyr6o4wcZVjX4DWY5s7LgqKk3B3mYzYtJlHdco-2SMfrD2m9XXuiASvR3FGTVuivPKcvqKQ1KnGJ8_0eKyDvgNlTDLTVh42pRco_RxE7jMMqFqcALcZcxgKmxFqG-fQFWgBhdSma19xMyvrfnstrztHZdjBY66PoIYUE08hStJaA7mFKSmW5moz16NxXNaS2A0DLkym0VphQgOjxBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون‌اول رئیس‌جمهور: جنگ‌طلب نیستیم، اما جنگجویان قدرتمندی هستیم
@Farsna</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/456858" target="_blank">📅 21:11 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456857">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdba671a94.mp4?token=rQ5Bw9gJrJdDF9hJYdB9tKK2M7gOIA33UipakiVbda7MThaxQ2c2HfW4eKn4Ig2UJrv9R989xs6lHiOW5ouX09d7USeYKZLG8Mp7LD-8PEyBY3ab2kAIrE7ygTpO0NDznHN3UFO-CYQAQf97qFz0EZec16iMAcBU0kqHRdeHucjSaj8qBBWB0Z_BNSTE9tMuj3cwfksiX9rauYVwuxS1dSNDdmfyPLPaFFl4Y8U8DZ6dzSvD922ZqsGxwSiSUl0VhjuCxOc5J922nrasIybiT_x1UI0AqoWgsifw8jWdfH_rHxq4K3X62LU0yG6gds1oDVfUIGg6GdYVoN7f0aGAWLxwfXueASSWozOk3PGgmsDp2XtIqzORmxKc_hZBlcPz5lgxwl3m1uZdhpdWwzfuPYtpJLIPS7u7OKcazdV143oAjPvQncEZxBnvLNeEkkAIM9U9CjZdTuqmQGGC7-a5MqeqMiGMbZOX0nCdAxXJtLlIVudclrX6eRuYS3UDggRZqUQIblo15e9a4TOCwSkMtUUh_O5xwwDWLtGgeG0pgjhalzi4V_ZYlShI7GbY21Dg4HIWCs69V1G9nq5tNPS7ud8TjbzhgvPwIBmwYoj4TnoWFNNcbCLnKkbY4UQRTmWD2jUCw93Qf1vcIPQ9M8KC6A-InASjS9HvkGvsfYtA4Q8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdba671a94.mp4?token=rQ5Bw9gJrJdDF9hJYdB9tKK2M7gOIA33UipakiVbda7MThaxQ2c2HfW4eKn4Ig2UJrv9R989xs6lHiOW5ouX09d7USeYKZLG8Mp7LD-8PEyBY3ab2kAIrE7ygTpO0NDznHN3UFO-CYQAQf97qFz0EZec16iMAcBU0kqHRdeHucjSaj8qBBWB0Z_BNSTE9tMuj3cwfksiX9rauYVwuxS1dSNDdmfyPLPaFFl4Y8U8DZ6dzSvD922ZqsGxwSiSUl0VhjuCxOc5J922nrasIybiT_x1UI0AqoWgsifw8jWdfH_rHxq4K3X62LU0yG6gds1oDVfUIGg6GdYVoN7f0aGAWLxwfXueASSWozOk3PGgmsDp2XtIqzORmxKc_hZBlcPz5lgxwl3m1uZdhpdWwzfuPYtpJLIPS7u7OKcazdV143oAjPvQncEZxBnvLNeEkkAIM9U9CjZdTuqmQGGC7-a5MqeqMiGMbZOX0nCdAxXJtLlIVudclrX6eRuYS3UDggRZqUQIblo15e9a4TOCwSkMtUUh_O5xwwDWLtGgeG0pgjhalzi4V_ZYlShI7GbY21Dg4HIWCs69V1G9nq5tNPS7ud8TjbzhgvPwIBmwYoj4TnoWFNNcbCLnKkbY4UQRTmWD2jUCw93Qf1vcIPQ9M8KC6A-InASjS9HvkGvsfYtA4Q8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا مرگ بر آمریکا؟ روایت دشمنی ۷۳ سالهٔ آمریکا با مردم ایران
@Farsna</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/456857" target="_blank">📅 21:07 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456856">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujLG_FCUzSbUzYNjc9x4pe-bxt1ZziJzQl4P3qORulG9HzivLfn77K8tdzoUesK1b-hBO_z2h6Ov2jKTe2ESK-gMSt480Z1yPF4C7GpXQtghzyUyrGzYwnA4kY4KLr1UZ9kdj1ZHQP6DyyA3iQI7cKGlrewnpeSq8bOlO6Zqi-70oQ4-OCjyBIAZJ8BPSGrIflO0HPLQHymvBQkI431uIFtbqm9DKWHrVJExH5uczEkJkxt8Db6QaVtB4WWVG8ZQ_qxm8a-kghXmzS2-USB7Lmo7PYTbATXG2lHVokOTxLDtJRPeE8ItMF045bbejZgUwamR6tER6jyYAsYxQD5fXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرلشکر رضایی:
به نظم پساآمریکایی در خلیج فارس خوش آمدید
🔹
شکاف بین ناتوانی آمریکا در بازگشایی تنگه هرمز و ادعای مالکیت آن، از فاصلۀ ۷۰۰۰ مایلی بین واشنگتن و خود تنگه بیشتر است.
@Farsna</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/456856" target="_blank">📅 21:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456855">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/557fc6e10d.mp4?token=ruNLcMwZu0OHQhP3ZYEqDnUqJGesW5m3bo1q9diST4q1QNs5KAG7Dfcqfbc3ed7vBVrFZ7Nc8asoeYqkvjmZdKyGMUU8Qsbr3IDNCwWxy-Nza5qcAOPnB9YCGeGMirMvGefPW8VeEUQDC2RVI9gh-6c_leL4zAdoHN4J137pb1ZXKtQ58xQ9JexFU_hx_zBB-1P1fORKXuCG688u88Ah3a6Id_G3piKJP76VOh38qOQIIC1rFWrssGiIpSlj89E5dpOR0wks44MyN5IpsmoAIu9KLDGfgpEO8wdp4BTTUke9-TuaZwU8GA0Zz5pKu1NyekC_kMRF8GLTJN9mPaeGcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/557fc6e10d.mp4?token=ruNLcMwZu0OHQhP3ZYEqDnUqJGesW5m3bo1q9diST4q1QNs5KAG7Dfcqfbc3ed7vBVrFZ7Nc8asoeYqkvjmZdKyGMUU8Qsbr3IDNCwWxy-Nza5qcAOPnB9YCGeGMirMvGefPW8VeEUQDC2RVI9gh-6c_leL4zAdoHN4J137pb1ZXKtQ58xQ9JexFU_hx_zBB-1P1fORKXuCG688u88Ah3a6Id_G3piKJP76VOh38qOQIIC1rFWrssGiIpSlj89E5dpOR0wks44MyN5IpsmoAIu9KLDGfgpEO8wdp4BTTUke9-TuaZwU8GA0Zz5pKu1NyekC_kMRF8GLTJN9mPaeGcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول استقلال به نساجی توسط آزادی در دقیقۀ ۸۲
⚽️
استقلال ۱ - ۰ نساجی
@Farsna</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/456855" target="_blank">📅 21:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456854">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-IErb_YwPRpwS1piHloYPyQ5vkm89Scs9Zw-zOk67IOM3X8Bl6iAIw7f2NmlDW0u-xcV9qpV_SYOWNR_RiyeLLSEgRthN8gJy5hVOnXcgCPkqDNnx2Orc1z_ktYe79Hsie7fqvTixeRqxy4Upn7VMQgo0-IdTWecb4GXt13N2896cK-MEfBL_bVQF5QVlVL1M0DtmI597yguauoNhbUSB-tJmI3fen5CZhwLG0jvEY6WfAqkD6TYb68aJCR8u0pGqx6dOS8T0_LTjDacKhkZNfNI8cWlLYI5tAbHVCoUf5yczQ4RHx6FW7juzSdEq3cFgDiKjI8bAAvwgvQp9PuIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان لیگ: استقلال باید میزبان دربی را اعلام کند
🔹
درباره اعلام مشهد، تبریز و یا اصفهان به عنوان گزینه‌های سازمان لیگ برای برگزاری دربی پایتخت که در هفته پنجم انجام می‌شود، باشگاه استقلال تصمیم‌گیرنده است و باید هرچه سریع‌تر گزینه خود را به ما معرفی کنند.…</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/456854" target="_blank">📅 21:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456853">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c91454bf7.mp4?token=M21_x9YVe8LkJoe_fScauVfIYqg_GiDTLQCD_tmJevFyDTMBv1p2E8jz9e0Hop9KvB2d4F0d8ZpxYRYdJtkM0-969d07BIU1XrTX6-pdn-4ubIRZqelN3eN7_DQbzqxgBrKswPTUvRCTsfYRSlwo8KTDSHi1bxGE7_6ZHbXIyGCb90llvrRspq5f3OkqQFIFAafp757R30wrPKqQahb3gXScxmvL72xQqmy-u_fHtNZtxteiBoG_cZfAlPoiin_-BOPXCgMUg1iuGJIfG-Vtxr0NiDTa5wQVY7sKIJmAxMxVL0lcKca-XMakqWnt82ISDK7fl5CWWtUk3l70NyjoWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c91454bf7.mp4?token=M21_x9YVe8LkJoe_fScauVfIYqg_GiDTLQCD_tmJevFyDTMBv1p2E8jz9e0Hop9KvB2d4F0d8ZpxYRYdJtkM0-969d07BIU1XrTX6-pdn-4ubIRZqelN3eN7_DQbzqxgBrKswPTUvRCTsfYRSlwo8KTDSHi1bxGE7_6ZHbXIyGCb90llvrRspq5f3OkqQFIFAafp757R30wrPKqQahb3gXScxmvL72xQqmy-u_fHtNZtxteiBoG_cZfAlPoiin_-BOPXCgMUg1iuGJIfG-Vtxr0NiDTa5wQVY7sKIJmAxMxVL0lcKca-XMakqWnt82ISDK7fl5CWWtUk3l70NyjoWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماینده مجلس:‌ با وجود این که ۲۵ سال است از مونتاژکاران خودرو حمایت می‌شود تنها ۲۰ درصد موفق به داخلی‌سازی شده‌اند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/456853" target="_blank">📅 20:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456852">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00feea9fca.mp4?token=I0E68CiKYmS1Lqr1zFsr4HpD453Z_eqvrATPLw1USqnNOe6Kabwh5WWEn1jTrLjsylFgBOoIjbv1kaUqVpMT48VcLI6N8hxue6xIp3TLFF7OPiVoCtqVfDx6WGgp7eHFYOVWAqWmhi_BcOQtZwlfUCkNnI2j7zrn1lorZFfm8feS0P_ZELHirGlPXpNL39asClgjKsm9frEsZ2dzyh_yqNo-BtFay-sCTGYOd4eMax9HVhv8a-rJEg5BlGal44AuqlH5efb0Hc7fRTX2CkWk7nrm0-tOglDOGAaCfqa2NJA8-Ss9HaM8eBosqQ9kQ5jUBH4CQzt1P3lz290OPsG9NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00feea9fca.mp4?token=I0E68CiKYmS1Lqr1zFsr4HpD453Z_eqvrATPLw1USqnNOe6Kabwh5WWEn1jTrLjsylFgBOoIjbv1kaUqVpMT48VcLI6N8hxue6xIp3TLFF7OPiVoCtqVfDx6WGgp7eHFYOVWAqWmhi_BcOQtZwlfUCkNnI2j7zrn1lorZFfm8feS0P_ZELHirGlPXpNL39asClgjKsm9frEsZ2dzyh_yqNo-BtFay-sCTGYOd4eMax9HVhv8a-rJEg5BlGal44AuqlH5efb0Hc7fRTX2CkWk7nrm0-tOglDOGAaCfqa2NJA8-Ss9HaM8eBosqQ9kQ5jUBH4CQzt1P3lz290OPsG9NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تهدیدهای ترامپ بی‌اثرتر از همیشه
@Farsna</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/456852" target="_blank">📅 20:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456851">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a2d8b476.mp4?token=f7fW2iArlswrbCNGjTg0jLZTCCkhQ6HGKyIhj9wAyF7PS9Iri6XzotrQx6GRKAx-CsW4XxnrZUYIFK47Y_de2nPBCDjFDDF5Gs4LjxMIfPFvaARmslMyej21xrpEn8OaQ68HtS9eWygbDpGEtGBqsgiZVpr4QYEiZehHP9wsbA1mBi5JbZo-Q-nbc2nwwBu8WMyKbcFedARuPARma8IPXbPrFjA9vSxqde8q7FWHggbI_U1P0WUBjCptSzc65qwlPcchZDalB6D4yfI4uF9fHOZnG3pqS9iSHHDc8K7J98PY13CwVCZnZoR1CHf3GzpFUHcVpmO1wRcxUbQqBx-zeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a2d8b476.mp4?token=f7fW2iArlswrbCNGjTg0jLZTCCkhQ6HGKyIhj9wAyF7PS9Iri6XzotrQx6GRKAx-CsW4XxnrZUYIFK47Y_de2nPBCDjFDDF5Gs4LjxMIfPFvaARmslMyej21xrpEn8OaQ68HtS9eWygbDpGEtGBqsgiZVpr4QYEiZehHP9wsbA1mBi5JbZo-Q-nbc2nwwBu8WMyKbcFedARuPARma8IPXbPrFjA9vSxqde8q7FWHggbI_U1P0WUBjCptSzc65qwlPcchZDalB6D4yfI4uF9fHOZnG3pqS9iSHHDc8K7J98PY13CwVCZnZoR1CHf3GzpFUHcVpmO1wRcxUbQqBx-zeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: زمانی‌که آمریکایی‌ها در جنگ درخواست مذاکره کردند، آقای پزشکیان معتقد بود باید به این درخواست‌ها توجه و راهی برای خاتمۀ جنگ از این راه پیدا کنیم
🔹
آقای قالیباف به پیشنهاد رئیس‌جمهور به ریاست تیم مذاکره‌کننده انتخاب شدند.  @Farsna</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/456851" target="_blank">📅 20:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456850">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a1c2c6fe9.mp4?token=fjKTX-8MQj5bE3Rafq57QM3dYCbP6dPdyJ3IeV6zAy4J6146GibSUj70hXzNnv7NsZmm-_LIkAhaZUCKc3FUsBIOUlnWSYpuh5Zm5oioQhE9TKziVAQccI6AqxWJqfxs28ZL2MACCUwY2Lzjbd8bnDCBnHFZAkEJEEo7oHIjMCDIC7aNS_hgQ0YkA3TsqLkSpF8N3PCahFh63xS5WNSq2gk2Z5Llni2gPBZxMybVHBQahpLfrO9LhUBfw5IQ6_V2ob90uH575WgKkfvLmZY0wYJX6ky15GRo41FcmaJABSJp0iY4ARARPL1QFFH4-2ZSvuK7t6kx-1geBbqjELTzyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a1c2c6fe9.mp4?token=fjKTX-8MQj5bE3Rafq57QM3dYCbP6dPdyJ3IeV6zAy4J6146GibSUj70hXzNnv7NsZmm-_LIkAhaZUCKc3FUsBIOUlnWSYpuh5Zm5oioQhE9TKziVAQccI6AqxWJqfxs28ZL2MACCUwY2Lzjbd8bnDCBnHFZAkEJEEo7oHIjMCDIC7aNS_hgQ0YkA3TsqLkSpF8N3PCahFh63xS5WNSq2gk2Z5Llni2gPBZxMybVHBQahpLfrO9LhUBfw5IQ6_V2ob90uH575WgKkfvLmZY0wYJX6ky15GRo41FcmaJABSJp0iY4ARARPL1QFFH4-2ZSvuK7t6kx-1geBbqjELTzyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر خارجه: به میانجی‌ها گفتیم آتش‌بس را قبول نمی‌کنیم، باید جنگ خاتمه یابد
🔹
ما می‌گفتیم جنگ باید به‌گونه‌ای تمام شود که دیگر تکرار نشود.
🔹
دشمنان درپی تسلیم ما بودند؛ به‌دنبال تغییر نظام، تجزیه و اغتشاشات داخلی رفتند اما به سراغ هر طرحی رفتند ناامید شدند…</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/456850" target="_blank">📅 20:47 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456849">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7effb7664.mp4?token=XvBpZWtI11BzMVXkM7BrVFUN9FIKmceDR62SFjp7Zht2ybdUkGWLgqwsUWGwWTDZoC2f39Jlr7HLLZ-3mNLexki4A1XnXQ8sRDJFzXiJSQ8uZcoOuQOg1hqiGH0judxJhW0XHNHeHp7gbcac0Zx7yUCNB_3SCeJHRSsGU7_WV-fzLBDmukmmzq3KRaL_W8ajwt9mVRH4BhuL0aLZFbmwz_sUHGEUmA_9aVHD6EoWPCtJ2V_EIyeJwN0tBi3TgcSrEYfb9Gj22mt45Ip0_TRmTcKJGydIQWXwp6NC2GdHfMz6u9gWm2pmAulz0U1OIPZg9Ywp368AUc8EgJBc-HRvOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7effb7664.mp4?token=XvBpZWtI11BzMVXkM7BrVFUN9FIKmceDR62SFjp7Zht2ybdUkGWLgqwsUWGwWTDZoC2f39Jlr7HLLZ-3mNLexki4A1XnXQ8sRDJFzXiJSQ8uZcoOuQOg1hqiGH0judxJhW0XHNHeHp7gbcac0Zx7yUCNB_3SCeJHRSsGU7_WV-fzLBDmukmmzq3KRaL_W8ajwt9mVRH4BhuL0aLZFbmwz_sUHGEUmA_9aVHD6EoWPCtJ2V_EIyeJwN0tBi3TgcSrEYfb9Gj22mt45Ip0_TRmTcKJGydIQWXwp6NC2GdHfMz6u9gWm2pmAulz0U1OIPZg9Ywp368AUc8EgJBc-HRvOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: نگاه کشورهای غرب آسیا به ساختار امنیتی منطقه بعد از جنگ رمضان تغییر کرد
🔹
پایگاه‌های آمریکا نه‌تنها امنیت نیاوردند بلکه مخل امنیت شدند. کشورهایی که میزبان پایگاه آمریکا نبودند کمتر از جنگ تاثیر گرفتند. @Farsna</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/456849" target="_blank">📅 20:42 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456848">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtXAV5VgOVFkPLTmWjIoCWrzVsIF-PxH8lT2_CbqaMAnziLx-YepnMIg1uXwI6jx-KhcaszcqdkFY9KctpucgHgQJE-6k_SDIedTCQGpaKpw-FQGAmpfAIi2pjaAmynIJWvZ172ryWmqNnM--OvPBylRuuGgIBgjpcyfZ9cTXhL849jQCa3sjV5ZaWFx1DqKjGREkFLPGsYK-2UNfjG9eP3WM_kmGALZ3R_GAwNIf0z7KSvvGp_eGoCJ2zcwyenu2GJWe35C2KKX3F_wtOBKfo4skSmsfHlLbflbQ79bkx2QkI01GrO9bLevrG8w3ZydanMwHx0v7ZS5qYgUTbenmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
آمریکایی‌ها خیال می‌کنند با فشار بیشتر بر ایران می‌توانند امتیازاتی بگیرند که اصلاً بخشی از توافق نبوده است
🔹
وزیر خزانه‌داری و وزیر جنگ آمریکا در حد و اندازهٔ این کارها نیستند.
🔹
منتظر نباشید که این تیم دلقک‌ها خرگوشی از کلاهشان بیرون بکشند و گندی که زده‌اید را پاک کنند.
@Farsna</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/456848" target="_blank">📅 20:40 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456846">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9996321ba.mp4?token=IKYz9uHLfQ3jhOb1tUOdsTToOXwxJc5M18ejsEJVRmpP7do0YU0dqlqtSwNq0CLMWCTVdZE3gRHpXHfNu_MlbUdVfJoH-vTSWGGWLjSbna-vNe_G_n964sVBw1rHWOYBWFMq0twh9ryrYTa0OCicDUnMX0wirbVVdI3x7QXKI9TcdTVOZBdQvbIdx6VCyvsjPHEKJB2cPker-ibPZBbFjkVmCjD2769ccTn7mYmVo8hDRpf81sS1M2OWSPveMxFappFgoYGVbO9f9YSrUa6uiIvLepgm3Q4MG8sr663-fgXOkd2k4qC4PDP6NQzLbs9IEcp0VvpfsrIzw6Q4y_9p3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9996321ba.mp4?token=IKYz9uHLfQ3jhOb1tUOdsTToOXwxJc5M18ejsEJVRmpP7do0YU0dqlqtSwNq0CLMWCTVdZE3gRHpXHfNu_MlbUdVfJoH-vTSWGGWLjSbna-vNe_G_n964sVBw1rHWOYBWFMq0twh9ryrYTa0OCicDUnMX0wirbVVdI3x7QXKI9TcdTVOZBdQvbIdx6VCyvsjPHEKJB2cPker-ibPZBbFjkVmCjD2769ccTn7mYmVo8hDRpf81sS1M2OWSPveMxFappFgoYGVbO9f9YSrUa6uiIvLepgm3Q4MG8sr663-fgXOkd2k4qC4PDP6NQzLbs9IEcp0VvpfsrIzw6Q4y_9p3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: کُردی صحبت‌کردن رئیس‌جمهور روابط ما با کردستان عراق را تکان اساسی داد
🔹
ارتباط کلامی آقای پزشکیان با رئیس‌جمهور آذربایجان روابط ایران با جمهوری آذربایجان را از این رو به آن رو کرد.
🔹
در جنگ ۴۰ روزه مشکلی پیش آمد که رابطۀ ۲ کشور را تلخ کرد اما یک…</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/farsna/456846" target="_blank">📅 20:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456845">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/031a3d2a3e.mp4?token=a0VSk3YvwKpSWKSqwrdUn3x1dP_m4Bbpen9I_7yHGFiTj806OJLiK2HncUwdM_LJB5YY_MvnKKKvgWobqfWH52TLGcQNCXY76Bmzkuhms559mk3DTCvTSzfpwIabBsAYiONMzXc2Imn4Hxt3TGN9vvLlPtHGMw9j5-r3Rb7nCl_Wc3_g8nsnpNrY9QwoVhFLYeFfKlaMwQ6slqqwyAE60CKSvFJ2f0ppnVSQcHtnnd65948H83ybKYBqppR-Ae66omUvikzGlMDxDMBnc5M5qsp_MB6j-OQB6StYnK8adqgo944y0q3HmTLC9Bb_h6auQPm-ypW_xXcQlyVXxk8GmwpFl_6YYTU8iSep5GXMNxBnToaV0sPIWt7JfJY4Rg834Qj7nCRELMBT7HyISI_GB8Z78uZoLltCGLDzVBnRnkf4ICIJUXnQV7MVRUukLO622G2T8fxA570Y5dT5TrU__eRWKMjXh-0LoU6nB9xyHwBk2gcEsd8IPP_J6LkcAZ9paJRcNAN305PWmwQaE9yChNlwBzph8ZHVCb2K9J_A-omDYgCwu79P3HKtXAJYFMvkWLD4t049Y5Gml6YEE4A8D5Ri2Yg-wZZ09rAenF4V2sEuJj7alyO3_VMZQLmO4M9flu29ey6DbLXFngJrFLpKEZn3XAhs-DlGJ0peFkQuDFU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/031a3d2a3e.mp4?token=a0VSk3YvwKpSWKSqwrdUn3x1dP_m4Bbpen9I_7yHGFiTj806OJLiK2HncUwdM_LJB5YY_MvnKKKvgWobqfWH52TLGcQNCXY76Bmzkuhms559mk3DTCvTSzfpwIabBsAYiONMzXc2Imn4Hxt3TGN9vvLlPtHGMw9j5-r3Rb7nCl_Wc3_g8nsnpNrY9QwoVhFLYeFfKlaMwQ6slqqwyAE60CKSvFJ2f0ppnVSQcHtnnd65948H83ybKYBqppR-Ae66omUvikzGlMDxDMBnc5M5qsp_MB6j-OQB6StYnK8adqgo944y0q3HmTLC9Bb_h6auQPm-ypW_xXcQlyVXxk8GmwpFl_6YYTU8iSep5GXMNxBnToaV0sPIWt7JfJY4Rg834Qj7nCRELMBT7HyISI_GB8Z78uZoLltCGLDzVBnRnkf4ICIJUXnQV7MVRUukLO622G2T8fxA570Y5dT5TrU__eRWKMjXh-0LoU6nB9xyHwBk2gcEsd8IPP_J6LkcAZ9paJRcNAN305PWmwQaE9yChNlwBzph8ZHVCb2K9J_A-omDYgCwu79P3HKtXAJYFMvkWLD4t049Y5Gml6YEE4A8D5Ri2Yg-wZZ09rAenF4V2sEuJj7alyO3_VMZQLmO4M9flu29ey6DbLXFngJrFLpKEZn3XAhs-DlGJ0peFkQuDFU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۴۰ روز از آن وداع تاریخی گذشت
@Farsna</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/farsna/456845" target="_blank">📅 20:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456836">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ae1cd0a6.mp4?token=D6xgkNNjZ5CvM33Csk8v4RG22OYBuUSQE4IRB0qwbdw6SeC2w2ip5lOhaqavJ7M3TxY0Re700BveD6YF0U3BJu9U7Autjpjf5-VkpjIqz9bBuvgmbY4q19ou7AwQ3g7f4BjpQyvHOPdfPPAuuDZpOxE4qVlrdd_Jv41MKSoiMJn6OSvkcHhgUH3KnqCPVJL51Nz4F2FseosWMFOOiMbwAm0ZMqNlC1IrNMzOGh4W9viLIOu2uoi2Le0hjTfQLl5B-LeaLLIPRxa9inu7xIhzJe77w6DdRypUtn450jloDhr2eqN_BA7lqTtblEaNHc0_TE10QbILpbBtUnJTScyJrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ae1cd0a6.mp4?token=D6xgkNNjZ5CvM33Csk8v4RG22OYBuUSQE4IRB0qwbdw6SeC2w2ip5lOhaqavJ7M3TxY0Re700BveD6YF0U3BJu9U7Autjpjf5-VkpjIqz9bBuvgmbY4q19ou7AwQ3g7f4BjpQyvHOPdfPPAuuDZpOxE4qVlrdd_Jv41MKSoiMJn6OSvkcHhgUH3KnqCPVJL51Nz4F2FseosWMFOOiMbwAm0ZMqNlC1IrNMzOGh4W9viLIOu2uoi2Le0hjTfQLl5B-LeaLLIPRxa9inu7xIhzJe77w6DdRypUtn450jloDhr2eqN_BA7lqTtblEaNHc0_TE10QbILpbBtUnJTScyJrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: کُردی صحبت‌کردن رئیس‌جمهور روابط ما با کردستان عراق را تکان اساسی داد
🔹
ارتباط کلامی آقای پزشکیان با رئیس‌جمهور آذربایجان روابط ایران با جمهوری آذربایجان را از این رو به آن رو کرد.
🔹
در جنگ ۴۰ روزه مشکلی پیش آمد که رابطۀ ۲ کشور را تلخ کرد اما یک تماس تلفنی رئیس‌جمهور با الهام علی‌اف و استفاده از چند مثل آذری ورق را برگرداند.
@Farsna</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/456836" target="_blank">📅 20:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456835">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1v_X3IkFZa8jGj6lSoLzfZO4a30_KYHnkPr4TPxmvUrnlzzj5OHe476IWLPPjfMWDCVH07KrLVypHWw6ilDUSvAwFShqD3xXObBmAIdoSqvSFlfz1pOSxOn7oQCw1qmNE-VGMOK7EESlZ1d8zVLbz6IPF5sr-a4F1s9DOuVQpll6NIfY3t1DrnixU5v8b9aBP0WRv0-7esupNZcVH94A5MXYzYzv83YCNUCUmvqXMW-wEjdNSd1b8na2S1MqlW9MBwWq6BogawuWoIyffE561ezVQJQwgSwkmh1ns67R3QxT86MLNN6E9bCjmCBjRmgr3PLTxA7-KJ9jbHToXzi-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چت‌جی‌پی‌تی دیگر برای همه یکسان نیست
🔹
رویترز: چت‌جی‌پی‌تی برای کاربران ۱۳ تا ۱۷ ساله، محدودیت‌های بیشتری در زمینهٔ خودآسیب‌رسانی، خودکشی، خشونت، اختلالات خوردن و محتوای جنسی خواهد داشت.
🔹
اپن‌ای‌آی همچنین امکان کنترل والدین، تعیین ساعات سکوت و ارسال هشدار در برخی موقعیت‌های پرخطر را اضافه کرده است.
🔹
این تغییر در شرایطی رخ می‌دهد که اپن‌ای‌آی با مجموعه‌ای از شکایت‌ها درباره ایمنی چت‌جی‌پی‌تی روبه‌روست.
🔹
والدین یک نوجوان ۱۶ ساله در سال ۲۰۲۵ این شرکت را مسئول مرگ فرزندشان دانستند و در پرونده‌ای دیگر، خانواده‌ای گفتند چت‌جی‌پی‌تی در ماجرای مرگ یک مادر و پسرش نقش داشته است.
🔹
حالا اپن‌ای‌آی تلاش می‌کند با جدا کردن تجربه نوجوانان از کاربران بزرگسال، بخشی از نگرانی‌ها درباره رابطه عاطفی با هوش مصنوعی و دسترسی نوجوانان به محتوای خطرناک را مهار کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/456835" target="_blank">📅 20:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456834">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKOZxEQAMMibVKTRQiCHtsL3z32hmskRAi3IC6rZpOmU-u212mmqz9AWjW1KknA3qUmoWabg-f2zoeh1hLMaD9Phr4No2pksrXsfkDRLNhDVKzbsw_EAkT6KyZ24fmkM6NoGJbirvuxNeG_Yde4p40GiYFPda2leCczvrIinC9uTf4oDiFUBJ-CItRPnDQTFroKn1j9AIaglow3v2jlr1-g1RNTtQVhQUf9OqE3zOwvzl45R40jmCK4h9p7S8lcP13pQ2WGEUkjZQeB02ptWiVIamEDVV9wcyWFZoqYpt9J5nlc3Gp177YoLbE7_VmqsE8FQcasPn1-Rhtq6G2jEwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رودری به بارسلونا پیوست
⚽️
با اعلام باشگاه بارسلونا، رودری، بهترین بازیکن جام‌جهانی ۲۰۲۶ و دارندۀ توپ طلای ۲۰۲۴ با قراردادی ۴ ساله به آبی‌اناری‌ها پیوست.
@Farsna</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/456834" target="_blank">📅 20:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456833">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJxHeCRXOWro6h47FUYspHQON2jifa05l3U-pZtbO3BYAyQmVnxap9G7cIjlOfCqe4lzt_AV_cjJuUSd9i-tSELfXUZE-6oFm-Kd_qP3VqpK6bZ-q_ZQ6W96zLJTVe5y0u8ubJVIUvtu2rvebxOSwMAHSz5HPrUSTgaxAHngySkBdSFBIIYXS0RRN0oP3PeLza6kTcHYQK_m-pXFOMyWNm135BBbMT3DWpCUIR2dScS75Uk-gn-pKQz0CliK1W8_R8C7HvHg1D_3W0p7FnTHImg8aGIBf85-gxQYxjoeVUkzuuqE3dlIvuvvmL4LDT8415GDZ_yUYnD4mcsLAGwweA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
قالیباف: افزایش قیمت بنزین توسط دولت تدبیر حساب‌شده نیست
🔹
دشمن برای سوء‌استفاده از اقدامات دولت جهت کاهش مصرف بنزین برنامه‌ریزی کرده است.
🔹
کاهش مصرف باید با بیشترین عدالت و کمترین نارضایتی انجام شود.  @Farsna</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/456833" target="_blank">📅 20:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456832">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4282992554.mp4?token=CmE3VNVAgVsvHSn6B85lD7xEZQdCTk41RIFV_Ma_cVdyP3HHBx3K4VVawNEW_cXDuDu35Ue5YZfVde1fOPnAhsHfP5rUxC5IWG2sk-kcHzLJHS3rSiI1S1yy2Ojlp0yBJ5cPFxzTc-3LRzBetIFNrF0JtSQccz-pSxUGiBIU-FKUEDclXRmLddSoclDFezM5V1-xdTQIvIqhVXGx75VAIgDoORkL4LkMMGy_m0NSXAf9E_gTz3HM2Ca-rHDbK1Xiw1W1xMN_PuZU8GPV6DloQGr03U9rivAioKqm3R0TTRP1oGQaLwkIhFJBVfA-C9kBV6ua1Poq_7CD_b_9GcvEZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4282992554.mp4?token=CmE3VNVAgVsvHSn6B85lD7xEZQdCTk41RIFV_Ma_cVdyP3HHBx3K4VVawNEW_cXDuDu35Ue5YZfVde1fOPnAhsHfP5rUxC5IWG2sk-kcHzLJHS3rSiI1S1yy2Ojlp0yBJ5cPFxzTc-3LRzBetIFNrF0JtSQccz-pSxUGiBIU-FKUEDclXRmLddSoclDFezM5V1-xdTQIvIqhVXGx75VAIgDoORkL4LkMMGy_m0NSXAf9E_gTz3HM2Ca-rHDbK1Xiw1W1xMN_PuZU8GPV6DloQGr03U9rivAioKqm3R0TTRP1oGQaLwkIhFJBVfA-C9kBV6ua1Poq_7CD_b_9GcvEZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیدرضا صدرالحسینی، کارشناس مسائل غرب آسیا: خروج نیروهای آمریکایی از عراق همچنان یکی از مطالبات اصلی بغداد است و نخست‌وزیر عراق هم بر آن تأکید دارد.
@Farsna</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/456832" target="_blank">📅 20:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456831">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خبرهایی از فعال شدن آژیرهای هشدار در دبی
🔹
وزارت کشور امارات با ارسال پیامی به شهروندان از حملهٔ احتمالی موشکی خبر داده و از آنان خواسته در اماکن امن پناه بگیرند. @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/456831" target="_blank">📅 20:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456830">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCfGzU-aRUIa7Bo3QmC2faE23gAfAzwLE-Z9SuBGCeEXBEPQH6n1ZDz_HQMRsyIJlTq6XLXm0ss4NoIjoxdo7VM87e2SjQWyB44xvgNUPQnqz3NHwzlvx5_WL4k_rba597CDxqSBmRztb_klUEq_MEDAu0pcWCJELCq0RRb7vfL-SqmpCELpkaNpnVuWlbWaaT_GDiT4BSEr2keXCpi4qBtdj7v_SJc08RuHZh1TSW27m742bSNQvHgEPA94U4I4jPrzMEpCGcmnHaFN3d5EDnao9eMspM_84h9OeEU8OwLW3JVctBXg_2CjDmtXGOJUTLxwfl1R4t8m36jFwFRcFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمسی‌پور تنها طلایی کشتی فرنگی ایران در رقابت‌های جهانی جوانان
🔹
آرمین شمسی‌پور فرنگی کار ۵۵ کیلوگرم کشورمان در رقابت‌های جوانان جهان موفق به کسب مدال طلا شد.
🔹
تیم ملی شب گذشته ۳ مدال برنز کسب کرد و فردا در آخرین روز این رقابت‌ها ۲ شانس مدال برنز دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/456830" target="_blank">📅 20:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456829">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afd6a9bba4.mp4?token=RXMHdR2t8NUlvt19l-NKrvUEZSN5QkYw_cUh5kPb8y10nBaoKQgPJX0Q7fgku9pc5VGy6EEEse9tR6wQitNEgh-4gv56g77RU8729tEBnNA3t2Pd4etvDonREy37Okq45XslhzJJeNxHCANZRWpnUvymcTQFp9uD-y974nP-nMhd1Pf43zlfmDxmDuI4hSgtqVGm4rY3BHAdFjq4Ve9MPN88MQLGi1LXJcGMoKVqnfjXxeHNZmj4yc3KG9-CxRca-_COfbSBIVqoUFowQXLlotvXH3R9aOi-g_BmZWBtr7uemuQV2HUqGeHOSXQOdmERLiXdUKrBSdvUYuJtXiegATzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afd6a9bba4.mp4?token=RXMHdR2t8NUlvt19l-NKrvUEZSN5QkYw_cUh5kPb8y10nBaoKQgPJX0Q7fgku9pc5VGy6EEEse9tR6wQitNEgh-4gv56g77RU8729tEBnNA3t2Pd4etvDonREy37Okq45XslhzJJeNxHCANZRWpnUvymcTQFp9uD-y974nP-nMhd1Pf43zlfmDxmDuI4hSgtqVGm4rY3BHAdFjq4Ve9MPN88MQLGi1LXJcGMoKVqnfjXxeHNZmj4yc3KG9-CxRca-_COfbSBIVqoUFowQXLlotvXH3R9aOi-g_BmZWBtr7uemuQV2HUqGeHOSXQOdmERLiXdUKrBSdvUYuJtXiegATzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چهلمین روز حضور مردم در کنار مزار رهبر شهیدشان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/456829" target="_blank">📅 19:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456828">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66d644e287.mp4?token=Zmi66yVzQX8P2ao3BnyV7YNz6uzc-BQ2XcVLdXFKsOBinM0zcMSd6ckq0WqkW14C8DUtfLORZGLljMpd3qnvZdUUBe1AydA1V6z6_O3DXgT2zhAfF5pWwYOBwo3GxGkiqDx1oSpOsUsCDGa2lB5ep_Z-TEensuG2MeTRi_7v2xY45uU-LCFUu1OMsOuM7wef4YPCn7AT-23vvxZ1PYcpv6cuD1NhCd8hhL03cbHZ2Q8Wo03dR1Jvhcalvy2qIglGy2Mj-_8x2H1Ftr3qPiW1BRkvpp8BhVrmHTWtco9rLq2k4BCg7LpezvCSFCeQjV8wAjL7wjvRVa9-RTIlGgxWjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66d644e287.mp4?token=Zmi66yVzQX8P2ao3BnyV7YNz6uzc-BQ2XcVLdXFKsOBinM0zcMSd6ckq0WqkW14C8DUtfLORZGLljMpd3qnvZdUUBe1AydA1V6z6_O3DXgT2zhAfF5pWwYOBwo3GxGkiqDx1oSpOsUsCDGa2lB5ep_Z-TEensuG2MeTRi_7v2xY45uU-LCFUu1OMsOuM7wef4YPCn7AT-23vvxZ1PYcpv6cuD1NhCd8hhL03cbHZ2Q8Wo03dR1Jvhcalvy2qIglGy2Mj-_8x2H1Ftr3qPiW1BRkvpp8BhVrmHTWtco9rLq2k4BCg7LpezvCSFCeQjV8wAjL7wjvRVa9-RTIlGgxWjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: ۲ موضوع کالابرگ و بحث نیروهای مسلح، موضوعات مهم و فوری ماست و باید به نحوی پیگیری کنیم که خدشه به آن‌ها وارد نشود.   @Farsna</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/456828" target="_blank">📅 19:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456827">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef9b951a73.mp4?token=iz53cpAEjaE-pH5lU4Qd6L2jtrYS23HoI8mgUyF9NyB30ocfXHkmvXVM7rn9tg12_KYQx36TNmuEvHIVkNPIud2-90tqD_0kwuGEsrptsNtzF7eEdO3aUhlVfUKN8FO8j-3xmYg10uAKReXowe8dlg9Bt_0acFSaK4TBffYCJLpQyfujqVceap-6U2BRvVx5ZVNt26Aq84JQVFXAIDf1deLQflf7aOe8KaumFq95c7fqhUvvfK3FN-4vXtuh4HKsFyzghe9NjLNDb1R2ahOhrujHxT3Wto7RLdRe19E0sDIqyDXH8ZujA8zsU9U1hWQwJU69E1Y_ThiQ-mQifZIvpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef9b951a73.mp4?token=iz53cpAEjaE-pH5lU4Qd6L2jtrYS23HoI8mgUyF9NyB30ocfXHkmvXVM7rn9tg12_KYQx36TNmuEvHIVkNPIud2-90tqD_0kwuGEsrptsNtzF7eEdO3aUhlVfUKN8FO8j-3xmYg10uAKReXowe8dlg9Bt_0acFSaK4TBffYCJLpQyfujqVceap-6U2BRvVx5ZVNt26Aq84JQVFXAIDf1deLQflf7aOe8KaumFq95c7fqhUvvfK3FN-4vXtuh4HKsFyzghe9NjLNDb1R2ahOhrujHxT3Wto7RLdRe19E0sDIqyDXH8ZujA8zsU9U1hWQwJU69E1Y_ThiQ-mQifZIvpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: قول می‌دهیم به اجرای کالابرگ خدشه وارد نشود
🔹
در نیمۀ دوم سال هم باید به افرادی که بیشتر نیاز دارند، با اولویت‌بندی پلکانی بيشتر کمک کنیم. @Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/456827" target="_blank">📅 19:47 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456826">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f95f594a69.mp4?token=jSlp4Uj_XysDZ7Zz-CXTe-lD7qmFRVyuWTB3Y2pZFwZYG3IqWtuviWGhOkMwKNgSw5vlGjYP0Ef1yTo-Xe9A4Y3Hpwhju4SQPO5zZjH03VFPDsILmi5xdrC5ubHpQyYkx1weos-x7N2AmM75OK5hRNUaL_cC9HuCKjmIDxdSXZvwoK7dHKompcW37WDr0FJJDgEWVQXno1WU_x3L6NRIpaWwjPCXeRNzOQrnCs02scFXSZ2pIRF51YgFMMmG-Lo8jurdIuZocwOdjRTV64foAIjr1Gfwq5uiHeJtHY-TUph0rczoDlF2r6Hn5q8ylxoKQQMAGFjo5eVD2wPiX3st1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f95f594a69.mp4?token=jSlp4Uj_XysDZ7Zz-CXTe-lD7qmFRVyuWTB3Y2pZFwZYG3IqWtuviWGhOkMwKNgSw5vlGjYP0Ef1yTo-Xe9A4Y3Hpwhju4SQPO5zZjH03VFPDsILmi5xdrC5ubHpQyYkx1weos-x7N2AmM75OK5hRNUaL_cC9HuCKjmIDxdSXZvwoK7dHKompcW37WDr0FJJDgEWVQXno1WU_x3L6NRIpaWwjPCXeRNzOQrnCs02scFXSZ2pIRF51YgFMMmG-Lo8jurdIuZocwOdjRTV64foAIjr1Gfwq5uiHeJtHY-TUph0rczoDlF2r6Hn5q8ylxoKQQMAGFjo5eVD2wPiX3st1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: تغییر شیوۀ‌ کالابرگ یا افزایش اعتبار آن ضروری است و باید هرچه سریع‌تر اجرایی شود
🔹
هر فرد یا دستگاهی که با گفتار، رفتار یا تصمیمات خود، باعث نارضایتی مردم شود خواسته یا ناخواسته در زمین دشمن بازی می‌کند.
🔹
مهم‌ترین وظیفه‌ای که ما مسئولین کشور خصوصاً…</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/456826" target="_blank">📅 19:41 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456824">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8c8d3623b.mp4?token=aks5Oq7ZIEf9VxZblpun5dxFFwu_Zbob7MMwWlbgqQX8fKRGZFwoKESDekeBB1ns2gEtso9lZl8NCn5F7EIEUPC0_5IoKqL_V4HmfEDmGNMj4RkxjjQWJ2CB5A3eVp1k5Tuf17GQSnPOfX-l-3tUwwv4EPwtrTOfGmao0no8UR8A_-FJcVH1DLLRx2lH6dYFTViDoQkbw3y8VZ-VDyfIjk8nivTIfqwJcZfLjmB8cN5FwTVbNLeY5EeK0aCqrydTeNgyf2oVK6habH1EmizZ0K3OhJzTC9pkx8ponxxTc6wcfXQmLW5r2-Iq9nicJSLeCE_qdz1h65oOdTjZ1guNqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8c8d3623b.mp4?token=aks5Oq7ZIEf9VxZblpun5dxFFwu_Zbob7MMwWlbgqQX8fKRGZFwoKESDekeBB1ns2gEtso9lZl8NCn5F7EIEUPC0_5IoKqL_V4HmfEDmGNMj4RkxjjQWJ2CB5A3eVp1k5Tuf17GQSnPOfX-l-3tUwwv4EPwtrTOfGmao0no8UR8A_-FJcVH1DLLRx2lH6dYFTViDoQkbw3y8VZ-VDyfIjk8nivTIfqwJcZfLjmB8cN5FwTVbNLeY5EeK0aCqrydTeNgyf2oVK6habH1EmizZ0K3OhJzTC9pkx8ponxxTc6wcfXQmLW5r2-Iq9nicJSLeCE_qdz1h65oOdTjZ1guNqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برخاستن ستون‌های دود با منشا نامشخص در سلیمانیه واقع در کردستان عراق
@Farsna</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/456824" target="_blank">📅 19:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456823">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1facc6a548.mp4?token=S-tEZX7utDV3eOlFJ_oafXK29p6-j4uv_kTLTnlBCqQOfDsICgRObZ7lEqWlBfb81Ja8Klc_hjApYRBMWRs9SE5sS_1bEhAwWJnQ-DIu36YhlASSjlgj2Z3hb9KztPM_98ZIJ02OtUToV2YtQ_h0rDE_T11c1s3dChG0JL70m8AlLHwjwacm30uU7XJXMYtTFbDtx3eQHWJKUnEw7mJ5H-aa-O5jE5lPKigiX_ZPOTc1OcV2FbUZUE9KsKU7rhu9eKtnt5rbZM1Rk9-LdbDtkLFbXw3CL2pJX6wxa_3RjoE9m3gR8cCOEf7_lzEDopfLdn9qbIZahfSAva22DcWKIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1facc6a548.mp4?token=S-tEZX7utDV3eOlFJ_oafXK29p6-j4uv_kTLTnlBCqQOfDsICgRObZ7lEqWlBfb81Ja8Klc_hjApYRBMWRs9SE5sS_1bEhAwWJnQ-DIu36YhlASSjlgj2Z3hb9KztPM_98ZIJ02OtUToV2YtQ_h0rDE_T11c1s3dChG0JL70m8AlLHwjwacm30uU7XJXMYtTFbDtx3eQHWJKUnEw7mJ5H-aa-O5jE5lPKigiX_ZPOTc1OcV2FbUZUE9KsKU7rhu9eKtnt5rbZM1Rk9-LdbDtkLFbXw3CL2pJX6wxa_3RjoE9m3gR8cCOEf7_lzEDopfLdn9qbIZahfSAva22DcWKIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار «لبیک سیدمجتبی» در مصلای تهران طنین‌انداز شد
@Farsna</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/456823" target="_blank">📅 19:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456822">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6107d8b0f3.mp4?token=U6W2KFRqSGr1OPUxkCp2QbMw_hmmDqHXHOLbtu2pSKw1Spu3vYqmNIMdvCEoVfsr-2HeSIZLIjEleW_d_oT614fNGkLCbcWG2Cl2tX6UPUof4_GMTB481P8xiMw7OXy2IkqEInSfEGvuRsMNmpkuI5KOCSk5W9eVWDJyU-MRuYP8Azvrtk1egkGjtzvz_aL63Be_M2XEvV1-kqQiYnmC1QzYczedtmhd7j8l4q_qCIHQuiw1MwHHmbS6ieEnEfhQ39phQvMieFe9eNcjI8be6-4sa_h_78_q5MbEYbbaHt8rXBkIgasZAZWPnNkzfPboV-jKU8q3B0JJqtKGBAUXzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6107d8b0f3.mp4?token=U6W2KFRqSGr1OPUxkCp2QbMw_hmmDqHXHOLbtu2pSKw1Spu3vYqmNIMdvCEoVfsr-2HeSIZLIjEleW_d_oT614fNGkLCbcWG2Cl2tX6UPUof4_GMTB481P8xiMw7OXy2IkqEInSfEGvuRsMNmpkuI5KOCSk5W9eVWDJyU-MRuYP8Azvrtk1egkGjtzvz_aL63Be_M2XEvV1-kqQiYnmC1QzYczedtmhd7j8l4q_qCIHQuiw1MwHHmbS6ieEnEfhQ39phQvMieFe9eNcjI8be6-4sa_h_78_q5MbEYbbaHt8rXBkIgasZAZWPnNkzfPboV-jKU8q3B0JJqtKGBAUXzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاج‌علی‌اکبری: از وقتی دارالذکر در مجاورت حریم عرشی امام رضا(ع) محل اقامت همیشگی رهبر شهید ما شد دلتنگی‌های ما بیشتر است  @Farsna</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/456822" target="_blank">📅 19:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456820">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53be270603.mp4?token=X2CWulayj5RC4pv4sfpDd9Vf-ZTyohBhf5sx2sjpJyOH96WB_7wJXlr4l9BxPINF6xAVORbeP6LwIra7wnT7f9BMiNA1G_xZeFlM_FCrxlgIGbi4Q3EYEKOCdTWrCXVN2HqG2EIsEcDBd1KP_nCE3Bkj_P0dkQ9J4GHtC6ptN8RxZKLecGu0VU0k6SnoonS0zpLGkzHKFoJf4jzMs--YADxu6F67oUKxRh8TVOhe0NTLNn5A9qq4EbNP-jHAoNfDhXDBCoqWpTmuwr9NFmVqOZxeCu7wMqH-ohng2vcwynTakFSucKuU4KzaOmpqKXkugy-UtpuGxj8oKAMo2dxFYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53be270603.mp4?token=X2CWulayj5RC4pv4sfpDd9Vf-ZTyohBhf5sx2sjpJyOH96WB_7wJXlr4l9BxPINF6xAVORbeP6LwIra7wnT7f9BMiNA1G_xZeFlM_FCrxlgIGbi4Q3EYEKOCdTWrCXVN2HqG2EIsEcDBd1KP_nCE3Bkj_P0dkQ9J4GHtC6ptN8RxZKLecGu0VU0k6SnoonS0zpLGkzHKFoJf4jzMs--YADxu6F67oUKxRh8TVOhe0NTLNn5A9qq4EbNP-jHAoNfDhXDBCoqWpTmuwr9NFmVqOZxeCu7wMqH-ohng2vcwynTakFSucKuU4KzaOmpqKXkugy-UtpuGxj8oKAMo2dxFYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام پناهیان در برنامۀ سمت خدا: مسائل تخصصی را نمی‌شود به رأی‌گیری گذاشت؛ مگر شیوۀ جراحی قلب یا وزنه‌برداری را با رأی مردم تعیین می‌کنند؟
🔹
مسائل کلان اقتصادی هم نیازمند گفت‌وگوی علمی و مراجعه به متخصص است، نه منازعات سیاسی و انتخاباتی.
@Farsna</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/456820" target="_blank">📅 19:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456819">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/492ccfeeb8.mp4?token=nQCjobsCov18FGnZK5XPZ_jyZrSmm9a8n9Zag6ZGqpzI5fwPaq7qmHi7CmE_qM3i332mbc5c2VxykmfvzqiEQaeD2yuzjaWg5ABdFQfTEmowRIGxUlO6TVzFn2yzJWBk8djHMezftV0sDr_KpEN7V9tTcKrFOmSkmFQ9g518ukTFzGyN8ejAc4kQzlMxCLnFFhIWlN2AA4v9GCQxN_FKPWeud-Rd744Jc4IEjRFZp6nRtqOJL0EunAAzcEvb4PI-6kewgtSQVB7zBWCskG2GuLznPZv-WsZrJj8treyG7wKAbMM56MNNkjdBv7jn-l_pCxAjySE1Xz3_Te_vYFAQNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/492ccfeeb8.mp4?token=nQCjobsCov18FGnZK5XPZ_jyZrSmm9a8n9Zag6ZGqpzI5fwPaq7qmHi7CmE_qM3i332mbc5c2VxykmfvzqiEQaeD2yuzjaWg5ABdFQfTEmowRIGxUlO6TVzFn2yzJWBk8djHMezftV0sDr_KpEN7V9tTcKrFOmSkmFQ9g518ukTFzGyN8ejAc4kQzlMxCLnFFhIWlN2AA4v9GCQxN_FKPWeud-Rd744Jc4IEjRFZp6nRtqOJL0EunAAzcEvb4PI-6kewgtSQVB7zBWCskG2GuLznPZv-WsZrJj8treyG7wKAbMM56MNNkjdBv7jn-l_pCxAjySE1Xz3_Te_vYFAQNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پزشکیان در مراسم چهلمین روز تشییع و تدفین آقای شهید ایران  @Farsna</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/456819" target="_blank">📅 18:55 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456812">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZEUJA8PP6GKO-nnGh45RDQkJ0bYxAc0Ge8u9UO4Tgo1N2s_UUD0tCMCtZBJr7Ip29BVssL-fo34GfQUEx6Aptr_OibtUpLBvsa5NjuBjzvvs3lO1kMjRLTeioNjqg6Ro2ofS26fomBovnUuEu1ieGnk1l_YwFu_IzpkgyCHJLTGwSQv2LR9NP7RVuBK50Cjd4vZuw3r2ZzBLiiwbIp0mCoOL6yBt-c4ZRZ0LLQbmxck6MfhwdiRmlsJTGtr_gK1K3JEy5SYcQLiPJNOisOufvZ3UsdUIty2_vyeVfP4Np22gFsHR9xOvqgBQzUK8ceOdvbiclTnasTk6oVjlVYg3qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kRDuI5_cSON4qUUTMam0yjWzXf-ffsofBB_-raAWRyGcgtAC8dlRZDS64pQ8RqRlPmTRnl_Cn3crxyeGPrOZHD8Z87Rw61jTxYLSncPwEQtbAxD_llYsknHzf5wdBnKeTHW0AOfHq-wHv3Inc3Z62lnu2lYabtfo0RkQ37_mOSOSm8GbwhBjY4ttcDUea1syY45xe2rPDQMCAsyVwbBTD4tL-zB5L5rIqWUpvFUk5VtMX_S-f8cVTUR1e1hBBq9JK2Jp4ggmwd7ZjgWMF8fGX4dC0kdsa4b1mL3-YzEFbfydirsIzXRL6uefd48KQp05mB4CQysXwRC-2zxROWGlSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JbmTraI8JX1b94w7IH90MUReCoKpK9EN8f7UeWqRgHl4Not7zT349ZToeKPgMrCKswDVMKyakn89YbzvMWuoWO4Tf15RbbtkyMivNILWxhWHMAQ-aA7Mvm-fKZGvl_a9vVq-QZWWvPdMqpQIMJm5R-rVU7smLCziQtLSTGZYVfLkTJpBxd81WdWNAJeOjQhRiUWqaraP1UJNOu4sTtqJCxtp6NyBCKOCJ8UnRHp82EUdV8QLeoVRb5uiCgOxK2ISLwUZpZr_9QccX15nnopLFIM4Gbsi2y5FmCnS9BZiL0GVAQo6lToEXayT6qu1B8jyg0hE0aScnqkSuKh0VTEQnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fwq_ASP58ipGBkMqn4QE6VQ0-M1VClk5CFuPL55Z-6LIVU9rB2TZpiMgE4n2ZN3CEDPgri17vdar1tWLDUjsl_wXw2A_cMNPc0gA8lxhkibisyWFAlaH6s6jrjfTObZnqKTwmYZsuJ8-Rtql3U7ksDl3Z5f3VLsvGBIC1aOrmchVtRDzbejoN7VXvv79e81uXQ3dDGUN-moSej0wiJO3S6-73qMlk8AZlJHRpAd4u6GzYnMOPCK8hGPSyDSrJEwKCw2ASrWTHAL-qbLz5I-rox6v1DNiXqHmdPi5sYmAXk4WMta3lFLYVj4kBM88PC5O8KeVNx9BjaPIRXyerYjTBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SfyLYTqDPim0KEIUncxK19aQUV_P3JS3DLWqGZIA-Ewe_n5SN6GxVYmDHFcuagxP_Kp_a4YrODMiEG9tZsj8XEcE-cXVQv0EoqzHPBuC0IS2upzpR9jnUhZeFgimkZUmlpnWWamE34wzC2kPTfCaRdevoJQs6HmXn4DejnwZJVpdsVHSnk0VUvnilfqA5MHR2YHj2tDreF0U1nXljkJYCRNIp5KKukAB-8iKQb2yXL1we8cUCGv5eFXUJg4XgHhj4oYIVrHqVCgp2AubTtZksOfG2lDFOD86dbkbjO2Py7h2HPLpZUMi52ZeojEgTfX-khaQYSwS7N1uCioTVPbYhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VjQRj5aY3sxHxUiybEI1rV-XiqKpf0Uwr75zeTGvBJiUfMKSiamZovHYi0cM4nDRtDVmHWSOAPIKNq-7U8a6P-l7wliZpf7a0NIAFC9dEsyS_w_Qym9xkQR00fSJWRNqVB3i2JNYOxpp-bv9N5hiblqJP90QTvv8MGDnw3O65sxJPMFVKQio4IafQfn5VBnuqEMYGeb4cUwkqiPBy52SdQZ8SFMqw7os4zie1bgoqfrLolmAdKBw6RBFAzBs1F3NizNnuTiw8WkGsbnKVFME20Y_i63kOU092xEPIC7AAJn094KmkNe_Ii_vCVBTYMZhmbrzfyQJbh1uCFCAL2KDVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cuTTB7XtV7IMjviM2usDiRjLwl4FgPgVSpmxlfwM0KwSpQ1SmrkZHRku9CJgokRpCjHRQlVNYRBY9w4fsXdo-pmkf6H2EYTw215RTm1flkaR-agIstFf2-O7m_q644jzhtRt1R2erb43AjuM5Bz6HW1ih4bv915BjIYipNZl2F36hm2eAu0Pkep8HWnQdJ05XNPNy8E3CFzBipN0pxUzy_KxShC3COq5MOMHRfE5Dk2JX7NmG1Rx5AE7BZ8cpajcKJFvRAmDHHWdnD1dBO73DIaCbDudMyhGeFBrVtnCLMIynsy28ICaOSKX9nAPLdubc3duPnuolwDVFW5rxOcPTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دستفروشان کتاب در خیابان انقلاب تهران
عکس:
مبین علی‌کرمی
@Farsna</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/456812" target="_blank">📅 18:47 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456810">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f575a34377.mp4?token=ZCwInr_emjFBzfZg92OgDs9Y7o4DsQxnbfwWUw3Sz5yRAjTihqrGBhba2zQ2r55gJo036rXFZ3JwS0_eLqduwtQTFGDlESU_xSwT_FEXVQNEHYkHw9AC8MiEe645Jc0d3oJnIPLGAhnW32znVRDcM5Wz8hus_9HF0idW8I09_Se9K3LO3HOF1zYuBfMKYifSHm363UXfKz756opvx20g2MAoG3mF3wNAg3HoYBQj0IR8WdZ0KtL3Hu2gSGkdJStX9XZOPLdq0zhtCGCHSbI73gPzAriZYD_WMJK0pazdUGAptaFPMvq2bUkh5hnRs-ayysw-TTPPLe5y0ZW8ic6oaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f575a34377.mp4?token=ZCwInr_emjFBzfZg92OgDs9Y7o4DsQxnbfwWUw3Sz5yRAjTihqrGBhba2zQ2r55gJo036rXFZ3JwS0_eLqduwtQTFGDlESU_xSwT_FEXVQNEHYkHw9AC8MiEe645Jc0d3oJnIPLGAhnW32znVRDcM5Wz8hus_9HF0idW8I09_Se9K3LO3HOF1zYuBfMKYifSHm363UXfKz756opvx20g2MAoG3mF3wNAg3HoYBQj0IR8WdZ0KtL3Hu2gSGkdJStX9XZOPLdq0zhtCGCHSbI73gPzAriZYD_WMJK0pazdUGAptaFPMvq2bUkh5hnRs-ayysw-TTPPLe5y0ZW8ic6oaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پزشکیان در مراسم چهلمین روز تشییع و تدفین آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/456810" target="_blank">📅 18:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456809">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vq77N08ufDoHYygLZKlf6eNkZmUxrMF4pHXHk6kER_vPs16okydzHwiaKN3x0-vvMcqyelFMqVYLEAFoXc5MBkija-qyMJnDv6No52Fu-9V0pMplDn3Ng7YXWnUpsQRFym0IbK64qYudhMsiyOdWuOBKYNGjE8xvTUnxzGR2-q2KL-QYkFg_S_8CRT96Ac1d7dEqwrDNjT3fwc1fg4jHwXc0pffxD1om7H0JRb1BSU5Jkid3h5OWTrTQYY0Xi5BO7mmtBOjCmB-o-EhAD7NSeNgFc7SB0pBX2883Fawj5fOLOa8SGY0LPS2k8vDGbIWbL5EkYdKXRny3eiThOCpKbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دعوای عربستان و امارات به روابط بانکی کشید
🔹
رویترز: عربستان برای نقل‌‌وانتقال‌های مالی به مقصد امارات نظارت‌هایی قرار داده است که مخصوص کشورهایی ا‌ست که جریان‌های مالی غیرقانونی دارند و در دستهٔ پرریسک قرار می‌گیرند.
🔹
یکی از این منابع می‌گوید این اقدام یک «پیام ظریف» به رهبران امارات برای اهمیت حفظ روابط خوب است.
🔹
بانک مرکزی عربستان به بانک‌های این کشور دستور داده که هنگام تسویه‌حساب با امارات بررسی‌های بیشتر حوزهٔ پول‌شویی، تامین مالی تروریسم و سایر جرایم مالی را انجام دهند.
🔹
چندین سال است که این ۲ کشور بر سر سهمیه‌های نفتی و نفوذ ژئوپلتیک اختلاف‌هایی دارند که از اواخر سال گذشته بر سر حمایت‌ از طرف‌های مخالف در جنگ یمن بیشتر شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/456809" target="_blank">📅 18:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456808">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b48df7e3a6.mp4?token=vu9Ox5RzgI2NwPmGjrgkxETxp1uO9kLmGvazQeY1wKTUaZLxq3RWSeaOmAncUKq_P7q5I7HnI0BdWDpjZe59WUu8z17tqQ1axNcKDesixHUMhAZNhO8k07_zd1AfL_HpYt5ITBAAxqVp8ZysxrHugGJFDOXoP1R7d_t2M_d4RtCkmh61dZ-LbiYGe2ozw7Fdri00MYNffS-90MyKb4D0xq0vZzPFWFjKMAUV--iizDgUsTJYggZHoBll6eANWvPeax2OWN0G6fU3obpjuqc3b2PbXKU8Z9566EBSVmqcBoYTBU0BByoVUydl6j3j4KjrQQ-UHw2gl3vdEb7DipCr4DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b48df7e3a6.mp4?token=vu9Ox5RzgI2NwPmGjrgkxETxp1uO9kLmGvazQeY1wKTUaZLxq3RWSeaOmAncUKq_P7q5I7HnI0BdWDpjZe59WUu8z17tqQ1axNcKDesixHUMhAZNhO8k07_zd1AfL_HpYt5ITBAAxqVp8ZysxrHugGJFDOXoP1R7d_t2M_d4RtCkmh61dZ-LbiYGe2ozw7Fdri00MYNffS-90MyKb4D0xq0vZzPFWFjKMAUV--iizDgUsTJYggZHoBll6eANWvPeax2OWN0G6fU3obpjuqc3b2PbXKU8Z9566EBSVmqcBoYTBU0BByoVUydl6j3j4KjrQQ-UHw2gl3vdEb7DipCr4DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور سردار قاآنی در مراسم چهلمین روز تدفین آقای شهید ایران  @Farsna</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/456808" target="_blank">📅 18:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456807">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">خبرهایی از فعال شدن آژیرهای هشدار در دبی
🔹
وزارت کشور امارات با ارسال پیامی به شهروندان از حملهٔ احتمالی موشکی خبر داده و از آنان خواسته در اماکن امن پناه بگیرند.
@Farsna</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/456807" target="_blank">📅 18:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456806">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d59c915308.mp4?token=YZ5_CVfZSFraCECEFmXAxkQwM3szOnWV7ryXAAgPDABznWMc58dGzk2dIR9MEAFbHXvsvrC-4dhLCJKNHmjCmygoVTaMqiKvvwls-QGH9Nvl6HJdoGpN7_KrYxg_qb1q-dLjv1GvxP_wn4LabWOckVp-I64iCMAsy0ASVfiI_pvjS2x0XFk8lTHVgqAD1zhLVfz-Se5L18hPURW-szFmFfPiqUBrTVOwmtUJeMqaURJyw6_5PR5xlUUKqgM921cMgC5MRzMfeylp2_42e74CHofVkBpbDYbH8hwPk_ZcWZzuipeaokpSXAU3Y2blEloamCkq2IB5wTt3UX6iOUvi_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d59c915308.mp4?token=YZ5_CVfZSFraCECEFmXAxkQwM3szOnWV7ryXAAgPDABznWMc58dGzk2dIR9MEAFbHXvsvrC-4dhLCJKNHmjCmygoVTaMqiKvvwls-QGH9Nvl6HJdoGpN7_KrYxg_qb1q-dLjv1GvxP_wn4LabWOckVp-I64iCMAsy0ASVfiI_pvjS2x0XFk8lTHVgqAD1zhLVfz-Se5L18hPURW-szFmFfPiqUBrTVOwmtUJeMqaURJyw6_5PR5xlUUKqgM921cMgC5MRzMfeylp2_42e74CHofVkBpbDYbH8hwPk_ZcWZzuipeaokpSXAU3Y2blEloamCkq2IB5wTt3UX6iOUvi_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار مرگ بر آمریکا، مرگ بر اسرائیل و هیهات منا الذلة مردم حاضر در مراسم بزرگداشت چهلم «آقای شهید ایران»  @Farsna</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/456806" target="_blank">📅 18:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456805">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anKcS95Pk_BU7RmKgwLSA_tdSqrsIuUcQPvTIF-ebX7yqmgb9zCeGgsUgbj6g6bM23ZWIoBsf1OchGOxlM5SjHwfdIxoi1SfNtiyP7UV4XnOEzOTTUSJyyRLBWT9tjeAZdIPWsZ2EuyYoRvNiNUchdo5Xp9ByJbAbLY5XbYKlennEltsIXLh4YMEtYz1TWxW3FoB0Y2SRcp27aoGmgS6S06LNABoBiY4iQhZA5VJdJZ_4wxYjn7XiEEKumLkskD0L9XYcRuvc7xpb8qAOFcxofyIc_gHSnX0K12qRG9E8Bm5cMl1ndQT3Br-mDS9OTeAELJP4cpiJYzB8g6BdhwPGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکایت نیمی از آمریکا از ترفند تنباکویی اینستاگرام!
🔹
دادستان‌های ۲۹ ایالت آمریکا از امروز متا، مالک اینستاگرام و فیسبوک، را به دادگاه کشانده‌اند تا ثابت کنند این شرکت با طراحی ابزارهای اعتیادآور، سلامت روان کودکان و نوجوانان را فدای سود کرده است.
🔹
دادستان‌ها می‌گویند ‌همانطور که شرکت‌های سیگار در پرونده دهه۱۹۹۰ خطر اعتیاد و سرطان‌زایی را پنهان می‌کردند، متا نیز خطرات پلتفرم‌هایش را انکار کرده است.
🔹
موارد اصلی مطرح شده توسط ایالت‌ها متوجه الگوریتم‌ها و ویژگی‌های فنی پلتفرم‌ها است. ابزارهایی مانند پیمایش بی‌انتها، اعلان‌های مداوم، لایک‌ها و فیلترهای زیبایی، تصادفی طراحی نشده‌اند؛ بلکه برای سوءاستفاده از آسیب‌پذیری‌های روان‌شناختی ذهن نوجوانان توسعه یافته‌اند.
🔹
اگر متا مجبور شود الگوریتم پیشنهاد محتوا، اعلان‌ها، سازوکارهای تعامل یا شیوه فعالیت حساب‌های کودکان را تغییر دهد، دیگر موضوع صرفاً پرداخت جریمه نیست؛ مدل کسب‌وکار شرکت تحت فشار قرار می‌گیرد و طراحی اینستاگرام و فیسبوک هم باید تغییر کند.
جزئیات بیشتر این پرونده جنجالی را از
اینجا
بخوانید.
@FarsnaTech</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/456805" target="_blank">📅 18:20 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456804">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سقف وام ساخت، خرید، جعاله و ودیعه مسکن افزایش یافت
🔹
هیئت عالی بانک مرکزی با افزایش سقف تسهیلات مسکن از محل اوراق گواهی حق‌تقدم موافقت کرد.
وام خرید و ساخت مسکن:
🔸
تهران: ۱ میلیارد تومان انفرادی | ۲ میلیارد تومان زوجین
🔸
مراکز استان و شهرهای بالای ۲۰۰ هزار نفر: ۸۰۰ میلیون تومان انفرادی | ۱.۶ میلیارد تومان زوجین
🔸
سایر مناطق: ۶۰۰ میلیون تومان انفرادی | ۱.۲ میلیارد تومان زوجین
🔹
سقف وام تعمیر مسکن از ۲۸۰ میلیون به ۴۰۰ میلیون تومان افزایش یافت.
وام ودیعه مسکن:
🔹
تهران: ۴۰۰ میلیون تومان
🔹
مراکز استان و شهرهای بالای ۲۰۰ هزار نفر: ۳۰۰ میلیون تومان
🔹
سایر مناطق: ۲۰۰ میلیون تومان
@Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/456804" target="_blank">📅 18:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456803">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ih3VQS_VAasE7-eUNjL1t3YKPaq-lcQmMVAvd5qZVudD8HA18RPu_ECH3jyXOUI5bhM0O5ZpCu2venZ_p69bygzipTXodWmkg0XYcudzWck6382RjTFy97g6i6gLo_fxWdVT44l1ywu6oDzvC4ux1f1vO50pkr72fSNfuGmtsw1dymcMOsCrVvrYmOcK1vBBu3GnO-Rhp3QMi5SoMUBtELCqRIb2H9Z1dPghpqVX-miTeF4fz38VHUE5EwWtJ6iyvSvGLjb7FZK5VYzKRshw_tIOjxx_w06TNH_ozx_BvTHc5gYs9XqPAuTLfMU0iHJSdGAGed2TlLXxyTWESCTWTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقوع حادثه برای یک کشتی در نزدیکی سواحل عمان
🔹
سازمان تجارت دریایی انگلیس از اصابت پرتابه‌ای به یک کشتی باری به هنگام عبور از بخش جنوبی تنگهٔ هرمز خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/456803" target="_blank">📅 18:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456802">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411b092225.mp4?token=vJRof2N3AckqDFarHX3H3HZeFJYlsXC1jDqnkQ-GH7vbTLn5HIgWXMM4McJwquNWk75H_k-imzUMgWgeZPvAiX1OUYP6MrpzpVeVFX4Aig7XBjXe6jYUw2dmZeWNKFKZlBCRrTwKfs0ZfA-dl8V10A4ONpQ8Y3gRiGbdrY8IA6tsk2qY7e6lO1lpEZYo0GqA-L48dZtC8nOeMrrDXN_WRgsAHEe71X1aZplezexRMfNY281zJ6ZCwj7txEhPWtpI1EJCO3vSEfTeB_iBPwfE2pebqJpM00OKyeHfi6MQJp48KWFoEX5S4rcpkoZhd-B_o164N_g4-3npBSGgvbQZwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411b092225.mp4?token=vJRof2N3AckqDFarHX3H3HZeFJYlsXC1jDqnkQ-GH7vbTLn5HIgWXMM4McJwquNWk75H_k-imzUMgWgeZPvAiX1OUYP6MrpzpVeVFX4Aig7XBjXe6jYUw2dmZeWNKFKZlBCRrTwKfs0ZfA-dl8V10A4ONpQ8Y3gRiGbdrY8IA6tsk2qY7e6lO1lpEZYo0GqA-L48dZtC8nOeMrrDXN_WRgsAHEe71X1aZplezexRMfNY281zJ6ZCwj7txEhPWtpI1EJCO3vSEfTeB_iBPwfE2pebqJpM00OKyeHfi6MQJp48KWFoEX5S4rcpkoZhd-B_o164N_g4-3npBSGgvbQZwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«عهد ما با امام، انتقام انتقام»  شعار مردم در مراسم چهلم رهبر شهید @Farsna</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/456802" target="_blank">📅 18:13 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
