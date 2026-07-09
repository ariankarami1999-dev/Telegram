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
<img src="https://cdn4.telesco.pe/file/KSisxuQEB-UYgrSishDZdc30S7ysmSCzbss_C6hvjfeykzK2pJxtp5cScts1_z82RtaXAyeceNCD89Bg29rdjCh6fhb86Q8qZCIoGkKVOJVhfCg4DdQug0va-uw2hYi3P07AY6sGY6R-9y3O-hylduHPI9K5pRj0RFu10hmB9jKoAKDd2t310QrE0CLvE8WLBDm66-7bfTeM7ASYlAcL-OqNE4nwwiQYs1hY6y6bzxQs3bAgmK-XuashUbH6Bl55Jitv84yhHvdOdgE_Zh7HPu7dPkMkzKmUwDAO_W3eFmifuknKopYhNa7-Mlcnz-q6zNvxwado6TTuItgJMV4vKA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 15:21:46</div>
<hr>

<div class="tg-post" id="msg-448678">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3SmvBu2thgrSAQuNXXYxlgg8nOFVQFa4zplGod3nyYvfx2vnQCo3cXqDTxsvC0D8VQ3R2LOrwahbcHJzJhpaCtnvK4u5zpzMeW7_LB6sm2tYkRSJ2fj3_0lijhmYZxP0SGK2oKsfudEnnBHZE-6jour3KQwfe-RZA-VWcv_QkDrE6FI0lJfqC0GCYwXQQ8aYNzy_XH_CnbNUkbHp0CUiET7fWW_MQvldJbrBJ5Kjj_TzqR2HtJev17ZxsFsWwzqTGduULRi8_JcFSHpOYMXJjPSeh4IRkGWgsTDwcG4brJO6hSqkZtK8CmROfyv0Sr865Ol8GD4X1z16_KfJS7J5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نیروی دریایی سپاه: ماجراجویی‌های ارتش تروریستی آمریکا پاسخ کوبنده ما را به دنبال خواهد داشت و روند بازگشایی تنگه هرمز را با اختلال مواجه می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 95 · <a href="https://t.me/farsna/448678" target="_blank">📅 15:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448677">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNbaWJ2OlaB7PpCuADTNZqFskKBXz6SofW5kagqEiAU6-wjXrqQ0cGcAk4qboAdWyUtleqnhvpFeyQHShubdT3zYymajTq8Y9DNQ-JveV3g5Y2OzB_W9Y9HRjDXiaiGfIN35XhyVq9XgQY6fkvAiTszXuv_N2MgNB6v6UL_NNhCMKdW80S2BJH5r7DMpmvL08CRE748Gjx7x-8G2lu1g8sNiXnxkCn-pBf1qhiX1Zyj0Eq7oOj6Y8GL0F38CQH4KiTNFXX7BpfMN6g71bEJKIPWtYEdiZQngd5LROzy-cxa0_l3z_6fmdosovyxDazoWHVdgtsLkIp6UMtoc3zTpMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت یکی از نیروهای مرزبانی هرمزگان در حملۀ آمریکا
🔹
ستوان‌سوم حمید زارعی حاجی‌آبادی، از نیروهای مرزبانی استان هرمزگان، ساعت ۰۱:۳۰ بامداد روز هفدهم تیرماه، در جریان حملات هوایی رژیم صهیونیستی و آمریکا در محدوده بندرکوهستک، هنگام انجام مأموریت به شهادت رسید.
@Farsna</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/farsna/448677" target="_blank">📅 15:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448676">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgILGxcQIOeH75eAe97sNdSx7OLEgwg5F0hovV61Z0DlyB0ffNA0lmkumY7HXFr04e1nSiQxaEf57a35_GM5L-FNj9WTBUihUcasTXGd-v-q3F8j8_EJeaoIORsiDGvjLfDNb5OvVGxc1OT3QS1Ow7AZQqL-VvzZ2K_I0cX3WLbvti6EUC6VUQGEu45LMVnM71thHwIAGBJGtx3sqPPbfGdIF24psDh-qWv2bImN3KTIC3UbjQGwS4RrFWHZb5OW36Gb7PYfEpRSJvYGAu-zu0U377RH-OnA_yxVSXGJKNEBERkv2iFT56BbQMCFRkOIZMPD-cfHds3-Iqlbz2tZbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
شنیده‌شدن صدای چند انفجار در چغادک بوشهر
🔹
دقایقی پیش مردم شهر چغادک استان بوشهر صدای چند انفجار شنیدند. هنوز خبر رسمی در خصوص محل دقیق انفجارها مخابره نشده است.
🔸
ساعتی پیش هم مردم بخش‌هایی از بوشهر از شنیدن صدای انفجار خبر داده بودند. همچنین صبح امروز…</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/farsna/448676" target="_blank">📅 15:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448675">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6394a96b6.mp4?token=el3a5Xxyk2FVhxUltGC0kv4NR1WSNcl0OWM321NzTCzjM_ripTzzJ8J5TbikN9HNylLCx-1aMtYlfeWtf-vPTvmbpDCigq6w2KpO9hWe3yS5E44Ja5seI4KE9vXX1NiiakdVsDC0oBwQ4QSEUQB56uUu5Jcqc0L7sC1G5f4lwNkKsLhynTYAPexXfllSGWqqFtybi9IPCCrgFHH0A1gI5TDhFaAC8xYZujBtwmH7tnC8CVqhIJxZ2XIWtzolRLHJzd9R1VJCPQRCDSt7S9pysnMGJn73XP6D-0XWoect2ZTdWVwM6h-zyQmmkEFWaA3QVQn4uF2eIeDy_lpbIavXpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6394a96b6.mp4?token=el3a5Xxyk2FVhxUltGC0kv4NR1WSNcl0OWM321NzTCzjM_ripTzzJ8J5TbikN9HNylLCx-1aMtYlfeWtf-vPTvmbpDCigq6w2KpO9hWe3yS5E44Ja5seI4KE9vXX1NiiakdVsDC0oBwQ4QSEUQB56uUu5Jcqc0L7sC1G5f4lwNkKsLhynTYAPexXfllSGWqqFtybi9IPCCrgFHH0A1gI5TDhFaAC8xYZujBtwmH7tnC8CVqhIJxZ2XIWtzolRLHJzd9R1VJCPQRCDSt7S9pysnMGJn73XP6D-0XWoect2ZTdWVwM6h-zyQmmkEFWaA3QVQn4uF2eIeDy_lpbIavXpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی یک جنگنده F-16 نیروی هوایی یونان پس از فرود اضطراری در فرودگاه زاکینتوس
@Farsna</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/farsna/448675" target="_blank">📅 15:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448674">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6648536b.mp4?token=kFjuwURnje4oFitCe4xUA8fmI9uB4fHYFt5yQnhvOLmy_Y0ddzBNxS-t1xdv0xKmvixnWSCehQCQmD9kD7ueZtAvz8XvLFL4fyKSxI4yE0pT6b1r7XS6yppnTbU5_iaF97DHsfyIjxyoIpT94mucC2L8e17SwmuVWDOGPQHYBu1F2Zc2fUlNzYjJ1CWt7muRnzz4OhS5EzfyR74poTKqnkfHet0Q35iLQqyzgROdpvcic6ZSHtDZqKUHm6JeQkZB85bh7qNpOMGID1gXgUu6CzImgELb_f8dkVArfPQnxV91g1AKAKMH-myCl5JTKycle83YHYoac6kqM5l5_D0ONQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6648536b.mp4?token=kFjuwURnje4oFitCe4xUA8fmI9uB4fHYFt5yQnhvOLmy_Y0ddzBNxS-t1xdv0xKmvixnWSCehQCQmD9kD7ueZtAvz8XvLFL4fyKSxI4yE0pT6b1r7XS6yppnTbU5_iaF97DHsfyIjxyoIpT94mucC2L8e17SwmuVWDOGPQHYBu1F2Zc2fUlNzYjJ1CWt7muRnzz4OhS5EzfyR74poTKqnkfHet0Q35iLQqyzgROdpvcic6ZSHtDZqKUHm6JeQkZB85bh7qNpOMGID1gXgUu6CzImgELb_f8dkVArfPQnxV91g1AKAKMH-myCl5JTKycle83YHYoac6kqM5l5_D0ONQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نظم ایرانی در تنگۀ هرمز همچنان برقرار است.
@Farsna</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/farsna/448674" target="_blank">📅 15:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448673">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/788f652c2a.mp4?token=TDbXgnqqyg9qmRLpjjcTEDAhPziFF6dCDMyuCOKdEKskkIMzGK6txa6aB8ogv0gbsqycHmlbpBUGtoVi5KCqEr6tdGWsAw7JyokWnshQ__mqo8Syye-CywKJ7__dmBcwzfT69ZTy7w5S75P303tqA15E2vNzzGw2E_6hCXqPgThMVCw3Yhl0Ud0dfLgy78nAJghYbjG9RNr964ua60txEQKx3x0jCZGU5W0tFmLJEycprhQsagpsY2s-pQ3-ch37Fu7y5ZRJckXucIn7yAH5WgGPL5Q_nfot80x6ewKiBXRt1N0lDr5HIfeuPe5gwnC-HQzly8BQOAhbjGABn37ATw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/788f652c2a.mp4?token=TDbXgnqqyg9qmRLpjjcTEDAhPziFF6dCDMyuCOKdEKskkIMzGK6txa6aB8ogv0gbsqycHmlbpBUGtoVi5KCqEr6tdGWsAw7JyokWnshQ__mqo8Syye-CywKJ7__dmBcwzfT69ZTy7w5S75P303tqA15E2vNzzGw2E_6hCXqPgThMVCw3Yhl0Ud0dfLgy78nAJghYbjG9RNr964ua60txEQKx3x0jCZGU5W0tFmLJEycprhQsagpsY2s-pQ3-ch37Fu7y5ZRJckXucIn7yAH5WgGPL5Q_nfot80x6ewKiBXRt1N0lDr5HIfeuPe5gwnC-HQzly8BQOAhbjGABn37ATw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد خون‌خواهی مردم عزادار با مشت‌های گره‌کرده در مسیر تشییع پیکر مطهر رهبر شهید انقلاب در مشهد مقدس
@Farsna</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/448673" target="_blank">📅 15:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448672">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
الجزیره: آژیرهای خطر در چندین منطقه اردن فعال شد.  @Farsna</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/448672" target="_blank">📅 15:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448671">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
منابع عراقی: آژیرهای خطر در پایگاه آمریکایی «حریر» در استان اربیل در شمال عراق به صدا درآمد
.
@Farsna</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farsna/448671" target="_blank">📅 14:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448670">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🎥
همراهی جنگنده‌های ارتش با هواپیمای حامل پیکر رهبر شهید انقلاب و شهدای خانواده ایشان، لحظاتی قبل از ورود به فرودگاه شهید هاشمی‌نژاد مشهد.  @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/448670" target="_blank">📅 14:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448668">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7258b3fb74.mp4?token=R64H0qE6i5rCmcIjKuxfAJwYTjWrRmZjG1fqzinEZBzzhLZ86wcwqu66EMmVEwaqGgZUFmFmxZh4h8k7_pKURf_uVN4V8scB6NJlOKGVpYvDxIo78WrN-Pk0Zf2n2xe36Jn0J11PPiPLMXZnrnIjHwwweEs7_kZAt7GCcZKh9kIP0AjzQ1HJCSA6w0X1f10MuZR64x11B1_MnzxOo56183I7FJvMgPMulQOI3PY2OdVsbQTgmdYQpdEQAmQq6Jg0NTd5Qfb8T1AI0o12O77GbqKiU4nnAJ60ejpXsfhuEHagchi0SJSq-U4p8LrXBsP2uCokwuJKZXCwLjUcAp8KRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7258b3fb74.mp4?token=R64H0qE6i5rCmcIjKuxfAJwYTjWrRmZjG1fqzinEZBzzhLZ86wcwqu66EMmVEwaqGgZUFmFmxZh4h8k7_pKURf_uVN4V8scB6NJlOKGVpYvDxIo78WrN-Pk0Zf2n2xe36Jn0J11PPiPLMXZnrnIjHwwweEs7_kZAt7GCcZKh9kIP0AjzQ1HJCSA6w0X1f10MuZR64x11B1_MnzxOo56183I7FJvMgPMulQOI3PY2OdVsbQTgmdYQpdEQAmQq6Jg0NTd5Qfb8T1AI0o12O77GbqKiU4nnAJ60ejpXsfhuEHagchi0SJSq-U4p8LrXBsP2uCokwuJKZXCwLjUcAp8KRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج خون‌خواهی در مشهد؛ خیابان‌های امام‌رضا (ع) سرخ‌پوش شد
🔹
خیابان‌های منتهی به حرم مطهر رضوی مملو از جمعیتی است که از ساعات پیش برای تشییع پیکرهای مطهر شهیدان حضور یافته‌اند.
🔹
مردم با سر دادن شعار «لبیک یا حسین» و برافراشتن پرچم‌های سرخ خون‌خواهی، خیابان…</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/448668" target="_blank">📅 14:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448667">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3a84aaabb.mp4?token=tL-C4Jjr-QjLiN0RXzL8gZPbMMicHkjTIyJBB_9FRcAJomOAkDv_ZdCsilxVRjUGiGRKiyY0Tmu3Z_kO6thnx_zZmCYcy_fzpUHDcvDJ_PA5gcSpX5p_cnW-dUc-oO5T1J6n9DZjsbPgL4u_tSnyPUiJ46tfO2oMZLf_3AKEijmaojuhfiSoRWhfu5c2w7g0YdgCD82A6h91qAQXuGF5kbOXzwtBYniZYLCjyjQLaq91ajL6WVq5lLQwYphzoea73Yz5vHXYJoIX7ZWfoJRniisset_Y5Fs0tOUqF2Zln8HKV4bJtJoxTtiuYy1xhayQwTa9BAJv0GOEJ0Ye877HpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3a84aaabb.mp4?token=tL-C4Jjr-QjLiN0RXzL8gZPbMMicHkjTIyJBB_9FRcAJomOAkDv_ZdCsilxVRjUGiGRKiyY0Tmu3Z_kO6thnx_zZmCYcy_fzpUHDcvDJ_PA5gcSpX5p_cnW-dUc-oO5T1J6n9DZjsbPgL4u_tSnyPUiJ46tfO2oMZLf_3AKEijmaojuhfiSoRWhfu5c2w7g0YdgCD82A6h91qAQXuGF5kbOXzwtBYniZYLCjyjQLaq91ajL6WVq5lLQwYphzoea73Yz5vHXYJoIX7ZWfoJRniisset_Y5Fs0tOUqF2Zln8HKV4bJtJoxTtiuYy1xhayQwTa9BAJv0GOEJ0Ye877HpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج خون‌خواهی در مشهد؛ خیابان‌های امام‌رضا (ع) سرخ‌پوش شد
🔹
خیابان‌های منتهی به حرم مطهر رضوی مملو از جمعیتی است که از ساعات پیش برای تشییع پیکرهای مطهر شهیدان حضور یافته‌اند.
🔹
مردم با سر دادن شعار «لبیک یا حسین» و برافراشتن پرچم‌های سرخ خون‌خواهی، خیابان را کاملاً قرمز کرده‌اند و مطالبه اصلی آنان، خون‌خواهی رهبر شهید است.
🔹
هنوز خودروی حامل پیکرهای مطهر به خیابان نرسیده و به نظر می‌رسد رسیدن به حرم مطهر رضوی زمان‌بر باشد.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/448667" target="_blank">📅 14:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448666">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اقامۀ نماز بر پیکر آقای شهید ایران در صحن پیامبر حرم امام رضا (ع)
🔹
قابل توجه زائرین و شرکت‌کنندگان در مراسم تشییع و تدفین رهبر شهید، پس از تشییع پیکر رهبر شهید انقلاب اسلامی در مسیر خیابان امام رضا (ع)، نماز بر پیکر مطهر شهدا در صحن پیامبر اعظم (ص) و سایر اماکن حرم مطهر رضوی اقامه می‌شود.
🔹
با توجه به تکمیل ظرفیت حرم مطهر، اتصال به نماز از خیابان‌های شیرازی، نواب صفوی و طبرسی برقرار می‌شود.
🔹
از زائران عزیز تقاضا می‌شود از تشرف به حرم مطهر از ورودی های باب‌الرضا (ع) و باب‌الجواد (ع) خودداری فرمایند.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/448666" target="_blank">📅 14:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448665">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
الجزیره: آژیرهای خطر در چندین منطقه اردن فعال شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/448665" target="_blank">📅 14:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448664">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/981b2eee7a.mp4?token=Vsu8pLR387bw2X4WNxUlt_bucLhXHYCZHEUoGKZLUq1Zf0qsVG5E2DUK-X1k8S3kqQaIPQNrJg7bE0Hp2Hie7764hnMwc4geteBUaIwuI-LNnbC_jEmZKM039PZk3B1_z1FVRATEQ5lzzmdfqepD9R6HsD2Hx58RhYGnqXNTTJ98LYMxs2ojkqd0Cn1gUUrhD_8w-RBPEyALDC-dXqkqMjrucVr4Hs4ZubFv8DR9Fm0C3i6nBzsFWf5lCVTqnuXDHJNpw-ubY1q-VYZzsrJclcDOGnK2adT7Bmp_8XMoLIO6e0rQwn_L1mph2-mVX6r0FiBL3BtuE5HMTMJgWTXtmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/981b2eee7a.mp4?token=Vsu8pLR387bw2X4WNxUlt_bucLhXHYCZHEUoGKZLUq1Zf0qsVG5E2DUK-X1k8S3kqQaIPQNrJg7bE0Hp2Hie7764hnMwc4geteBUaIwuI-LNnbC_jEmZKM039PZk3B1_z1FVRATEQ5lzzmdfqepD9R6HsD2Hx58RhYGnqXNTTJ98LYMxs2ojkqd0Cn1gUUrhD_8w-RBPEyALDC-dXqkqMjrucVr4Hs4ZubFv8DR9Fm0C3i6nBzsFWf5lCVTqnuXDHJNpw-ubY1q-VYZzsrJclcDOGnK2adT7Bmp_8XMoLIO6e0rQwn_L1mph2-mVX6r0FiBL3BtuE5HMTMJgWTXtmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از خروش سرخ مشهد در انتظار تشییع پیکر امام شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/448664" target="_blank">📅 14:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448663">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تکذیب غیبت ناطق نوری در مراسم نماز بر پیکر رهبر شهید
🔹
در پی انتشار برخی شایعات درباره عدم حضور حجت‌الاسلام علی‌اکبر ناطق نوری در مراسم تاریخی
نماز بر پیکر مطهر رهبر شهید ایران
، پیگیری‌ها نشان می‌دهد وی در این مراسم حضور داشته است.
🔹
براساس اطلاعات به‌دست‌آمده، ناطق نوری صبح روز یکشنبه در مراسم نماز بر پیکر رهبر شهید و اعضای خانواده ایشان شرکت کرده، اما در صفوف نخست حضور نداشته است.
🔹
حجت‌الاسلام علی‌اکبر ناطق نوری از چهره‌های سیاسی کشور است که ریاست مجلس شورای اسلامی در دهه ۷۰، وزارت کشور در دهه ۶۰ و ریاست دفتر بازرسی دفتر رهبر انقلاب را در سوابق خود دارد.
🔸
نماز تاریخی بر پیکر رهبر شهید انقلاب اسلامی ۱۴ تیرماه با حضور میلیونی مردم در مصلای تهران و خیابان‌های اطراف آن برگزار شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/448663" target="_blank">📅 14:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448662">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sh4K3MyggoebN_Pnz91DJkJN2nAdfyhTUvClempzSHgSQOYmMFY73ea1Efd7oAsVAN8LRRcSDc5azWX-AgZFp8ILPHoKCbpshEYA2ntazkOtqVsxUsNAvcRqSOZKwzO12IeyfvHXTYoPz9t--R-N9w2vhdCwB5xMKEVbVf2DUY1me3190upJseU2Anx6u8B8QUIrgwyEPR8CJQ0M2YGSWXPiblWs4USdsXCRyCWzVQj8sgXnZwMtI_0ii_JIUAtOTn_9Hm11OmTjYQogCrExO_JLwaVHmFimf531k28ny08eINjN3KqIg-iX90EY3bVhvdNOf7fmnCQwiRs5JEf3EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
لحظاتی از تشرف سحرگاهی علمدار شهید انقلاب اسلامی به حرم حضرت عباس علیه‌السلام.   @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/448662" target="_blank">📅 14:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448661">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cadca97172.mp4?token=nonKsQzTFRpsNomVzb-HLwvDegQmOAHbwnx8EpEVZHoPTg2wbq867qNA4fXK9BN_ZShAM7Tdo6GwEQYyBE4tNfQSLXTnDjxKCvvAPD6OS3Gzas-X41IJ2_lzIl9Lbl__yQ-oYYB9YW9DQOlz34zA2_DXQPr4-kDD2Bjjv86UTD3g1fpENnF7Rt6ZWJ_4ZAGuDHMo1jD2M5ie00phnltcq20xU133CjYdHopo0s-3hyH5u8rtI0ea83iIPJ89EvqHbvlh2DkrFjxTF8_k63cJf4_Tc8kB0RsnKaVhxg0nSbtoIfJsd0D0UWEVgfAFOEoVor6zYGG6LGsfSO_bb0zong" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cadca97172.mp4?token=nonKsQzTFRpsNomVzb-HLwvDegQmOAHbwnx8EpEVZHoPTg2wbq867qNA4fXK9BN_ZShAM7Tdo6GwEQYyBE4tNfQSLXTnDjxKCvvAPD6OS3Gzas-X41IJ2_lzIl9Lbl__yQ-oYYB9YW9DQOlz34zA2_DXQPr4-kDD2Bjjv86UTD3g1fpENnF7Rt6ZWJ_4ZAGuDHMo1jD2M5ie00phnltcq20xU133CjYdHopo0s-3hyH5u8rtI0ea83iIPJ89EvqHbvlh2DkrFjxTF8_k63cJf4_Tc8kB0RsnKaVhxg0nSbtoIfJsd0D0UWEVgfAFOEoVor6zYGG6LGsfSO_bb0zong" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۸ قهرمان ارتش به شهادت رسیدند
🔹
روابط عمومی ارتش: به دنبال تجاوز جنایتکارانه ارتش تروریستی آمریکا به مناطقی از جنوب ایران اسلامی در بامداد امروز، ۸ نفر از دلاورمردان  نیروهای هوایی و دریایی ارتش جمهوری اسلامی ایران در بندرعباس و بوشهر، حین دفاع از میهن اسلامی،…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/448661" target="_blank">📅 13:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448660">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1ba311d91.mp4?token=GKcBjC_AKnsF_cWmID-KGb-1QHiIdNXH2FlXEtifKFh9sOSiw-uplGJQZBX1s5VSr21QXpAgzoczQDmhYcUWfKVgmP3MG_fnZ9Io1c46wAgojtsD046PUQ3y_iaUxaFHfMDVVAcv5l3X58tK7XZuDtWtKxERqaQVEM_41md9VsHCj0YxCyww-xQ0fl9FzRe8sqyLTh2EZs27i7jYpUpD0yc9Ec2b6iKatWXv0n16y4gsIKgUGBEnqa8jCpb7WmuT1rfmBePwK0yz_9Ftcm10q7LqF_k6jKLm-zgL_8pHueNoQqW8xezZuwYB5SgvI4f3vihHnOGBhEnGARFVwbXFnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1ba311d91.mp4?token=GKcBjC_AKnsF_cWmID-KGb-1QHiIdNXH2FlXEtifKFh9sOSiw-uplGJQZBX1s5VSr21QXpAgzoczQDmhYcUWfKVgmP3MG_fnZ9Io1c46wAgojtsD046PUQ3y_iaUxaFHfMDVVAcv5l3X58tK7XZuDtWtKxERqaQVEM_41md9VsHCj0YxCyww-xQ0fl9FzRe8sqyLTh2EZs27i7jYpUpD0yc9Ec2b6iKatWXv0n16y4gsIKgUGBEnqa8jCpb7WmuT1rfmBePwK0yz_9Ftcm10q7LqF_k6jKLm-zgL_8pHueNoQqW8xezZuwYB5SgvI4f3vihHnOGBhEnGARFVwbXFnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت الاسلام هاشم‌زروندی: از تمام کشور موکب‌ها برای خدمت به زائران در مشهد مستقر شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/448660" target="_blank">📅 13:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448658">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در بخش‌هایی از بوشهر
🔹
دقایقی پیش مردم در بوشهر صدای ۲ انفجار شنیدند که هنوز خبر رسمی در خصوص محل دقیق انفجارها مخابره نشده است.
🔹
صبح امروز هم دشمن آمریکایی نقاطی را در استان بوشهر هدف قرار داد.
🔹
همزمان اخباری در خصوص اصابت پرتابه‌های…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/448658" target="_blank">📅 13:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448657">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f21f58acd.mp4?token=WNoTTHOT1uWZXLYNP_vD1h6qI9BgxHdEAA2DB8mNCx9B4vB5jR2jgjXqOqTM8lxLXOURAvOGZXiwmLjKqNxBGz8_dRteQmIz2CUqxnUoJp1EbkjeInj2bZo_A4q3Ec7uai-S9lPT-siVveASprp6CPpH-lP8VIuYJZxxqkbLB108xlWsmLu4h89YGXUhzC8v0zHNr5cCUHOs3av9CfoJ2Ipb8mJrRFTZuA8dQA60hmFoyVlEOAnyFsdcuhrkJJY27HZd0-RU4h-4vYq9WkjczDoaAzlJc5VHyp9dW0_wxkldY23ikNsncA4EKtgB0_uxHFFfotXqA9UEdv7AvyCG9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f21f58acd.mp4?token=WNoTTHOT1uWZXLYNP_vD1h6qI9BgxHdEAA2DB8mNCx9B4vB5jR2jgjXqOqTM8lxLXOURAvOGZXiwmLjKqNxBGz8_dRteQmIz2CUqxnUoJp1EbkjeInj2bZo_A4q3Ec7uai-S9lPT-siVveASprp6CPpH-lP8VIuYJZxxqkbLB108xlWsmLu4h89YGXUhzC8v0zHNr5cCUHOs3av9CfoJ2Ipb8mJrRFTZuA8dQA60hmFoyVlEOAnyFsdcuhrkJJY27HZd0-RU4h-4vYq9WkjczDoaAzlJc5VHyp9dW0_wxkldY23ikNsncA4EKtgB0_uxHFFfotXqA9UEdv7AvyCG9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میزبانی موکب‌های کنار حرم رضوی از عاشقان رهبر شهید
🔹
آستان قدس رضوی با برپایی و تجهیز موکب‌ها در مسیرهای مراسم تشییع، خدمت‌رسانی به زائران و عزاداران را از نخستین ساعات آغاز کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/448657" target="_blank">📅 13:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448656">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f17395f.mp4?token=JdhgP4-XRTnPTpm3g1YqVnEQvk2LVX1gCRrTXXF9uqyZtYPhazcZl_QUbhauVoUZ68yhTRzwiIDqYgKIAOiQ25oBWpkhxDH08NYMgEYcOxXpGTVU1rJ9sflXpWecJCf6WTtBfsFORekxopH_KeHD58u6el_RJn8Y7jdJbQdKh73GXqrfI_v7usvIxvMZTvqAMcYVsPj3mDLGRtYnl3WfMaM3d_eisCH5DEfW3jbb0r5tW66kOu4iIdUiP9YwP3dFOJiQxgUu03m67HgzLjn_Z3oZo5V_zmTKK7uFJ20cWmFB4YhpJQp5E1dEAuvq2FtVJoEWyK8GDoHsNwGIt3jdnTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f17395f.mp4?token=JdhgP4-XRTnPTpm3g1YqVnEQvk2LVX1gCRrTXXF9uqyZtYPhazcZl_QUbhauVoUZ68yhTRzwiIDqYgKIAOiQ25oBWpkhxDH08NYMgEYcOxXpGTVU1rJ9sflXpWecJCf6WTtBfsFORekxopH_KeHD58u6el_RJn8Y7jdJbQdKh73GXqrfI_v7usvIxvMZTvqAMcYVsPj3mDLGRtYnl3WfMaM3d_eisCH5DEfW3jbb0r5tW66kOu4iIdUiP9YwP3dFOJiQxgUu03m67HgzLjn_Z3oZo5V_zmTKK7uFJ20cWmFB4YhpJQp5E1dEAuvq2FtVJoEWyK8GDoHsNwGIt3jdnTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کثیری، کارشناس برنامه پرچمدار: اگر پیکر رهبر شهید در سایر کشورهای همسایه مثل ترکیه و پاکستان یا هند هم تشییع می‌شد، آن‌جا هم شاهد جمعیت عظیمی ‌بودیم.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/448656" target="_blank">📅 13:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448649">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FK1boMXCLYT_BgXgBa08la_t0H8dQQDAMJceAaKfHYX5DachXqBd_4jDAPDf7mnFtuSxbBeNA0cIv5H_wXresttUlzzL7jjOrN-va3ey-2AqDuV4EUBI-o2LC2-zKM16R8u8sEd_MCnQY_CFGnOb-zGymkWDVQLe29otthwP_8IOpNQgBM-V1abo-zcEvBs4nYkj43SXfFtMcfzUQWwsR0ZB_xV7ffuskONEgHlUsEwHMIHNGQKUFEOW5KFZ-YLHuF3zznVZIRn-caFCExiWj3ZM6TBp6YsRikLONTOt3-1AG7fYGrchc4k0aY1NbtpYjNXJxyOnmcLCATOS7adW6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cspeP_z9-JBDl0ZKrMihZRNHTxZ6yzJ_S0fwi7dU0wpIncSBvftaqYxyikA1d3MnWxz89FykgnvQ0qfua4u_JB8meLovEBJFMIcWNiN059xogAd9OXRxHuiE5PstSEcRdmh2wU6uDZmn_9aQZtq70LInzYBueRZ28cBlaUMH_gDfDmqzA2f7nDjwMq2QXJsJMyEeE4pdLyxiqezGgNw3TTKa2iCNPoN-zFpehhCsj6OwfNLd6rFNxrJ6vwST6TMkpOnmpIVOrOvymRXB77eivBy2hP3I-Vjb-PJGaYtRaVtyA3OmPAM_irTsjAqKuwuGm7gG5JBlxqBI6Bt0kSJ6Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vxfkzap4Ad6Y6eA-nNpSaWwI0dwI9nNQ-a-PfFCQRXO89PYxuLyMdrytsco4Yk0yjqq3RITN_TJdd8jENrkqPrrz1tsGl5iVBQ4qvNDCLK7C_XMOck8oInnw-I4YsvQQsTKOy2GxVaXsls5cEtcRLpsZd4b8vJ4Qkn8heIEyg0josmHiEXiIceQ3z1V05DDFajrCP-pVt-yDvVK9MmqQBCjAICpqbUAKKd8euM8q1RXei_CJtah9aO3sT6DTxgB-5UIDK36yxhH9J43VomnMMUTxJE2pkTIJrBxfQjgniV9zXFT58CQJsQ93qotFoJ6KdQ04pXEUGZyfxt0yLAyyIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aT2AZ78KtbtJ_cgBXGanrPiYOybwKJ74f0tQ9TNdacxHnUOpxLtaLaJMOssj_mO8UbsjOmYUvwcUxBHFSRYsKKfakMQjAkRCG7oQmMH-RVg8piBPKQFV3fZqEc_jzgg_-5z6v_QAwAlEGXiNuOadkyfURxN4m2M6dEjJfmM5-9PTioo8UL9IcUm0P6E-WQWGdmZHi-rQO-1IDeTPpwGjDWXhprjhXVCdYF5VqI_QCLMPLF60R-s30_sb0cmNOaq4MP-ReRRfRND2bBZiwZjtoFidmnUuO3dRmiKwG-s5Ygm5Ba3LNUfSPm4wfxkg0_KBUSZ7oN6nAYya5_WHudyoqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fafyE5sZKGv1rZyIgwBL9SzqwphvRcV95EVccKGHARr9cuJmyInmNMX1GKc4Tc8m1IRj6hyLav5dvOj0Sgwr39FZ-m73Udn5IduyTvgdCX28Hi9EtmkuFmd5nVIjh9Fsdpj5t3VKRIcIWKXTRbOgVeBq_c-AbiLtPGMsM12f5ohB_Ej7dKZlAVlVNTPOBz8nvolTPZHRXNkQSJcpvyGTQm-U2vcyd-PNLFUKXUkOAMVd2rhSl_m9TU7lhK_6lTXX8mzq5YnW5fK6UGqVbqehdjAO1xN2JEJ-nYVfkUke9vQMSmajjj_gs8nQjWIwhOAd6UGhAVvjNqPCmbePyAaB3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OBYBpV6OkEzbHfHe2Lq25eQftA-WJYqefVyr2O427VvbojkHEnTvWAyp2X6xvNYRNFNJMvrxJ-nXiU9MgqQsjBUGR5cz8RbO7vCpH91BZ83b_8o9_apyXse7sM4I-z0FR5lJ1EH2CnoaWNfVeSkG2atsBGig8EBjVBWLdpGGqos2als-gN82eANML0WQS7k-DUYiAY03WuhsvuY47eGAslgaY4_DSkvuWVCVV8j2iH6MomvE_Cg4wAXB-S4JVpNAhKEph1iePrNLkrm3_tZnJHfZdbZjtD9R6P7fW9v4dq7JWeOf4o2q6_OjWJ2Eg9w25E0f6XS5EKolrfIQ9poQvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tvds9v9DGBeh0jatQ0cDj1XXZNde8REpNThbmUDEhZI2xJDVs4-Do7Dj_qnvTp0nJj7T3VyUTvd8fVXbE9SFXzH8ps-Qsju1fqZXUr8JcixddzwrBv43IRR8lvz87rk3EKC_7nE0Asw61ZpV8CMvn9cXjSBy1dEhnFAOX_4VAoml2jYolA27nIsf8S9-ewO9MXdsIYT-kvfcV9dWAbY5rtD0mSb5ua2NYCYR1LfvTjLKClIZgwkVe8y6vCMv6A4wZNvE6TRlh7OfsQkZm-RQNGrY3ipPTmzewRtAIh3T3wohZ3Ad2jHxjvDoPUlkumvb5xfNXm8C75aSTnxnUo-SaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خط‌ونشان مردمی برای ترامپ
🔹
در روزی که همه در انتظار تشییع پیکر رهبر شهید ایران در شهر مقدس مقدس هستند، شرکت‌کنندگان در این حماسه با حمل پلاکارد حاوی محکوم کردن جنایات رئیس‌جمهور جانی آمریکا نفرت و انزجار خود را مقابل مردم دنیا نشان دادند.
عکس:
غلامرضاشمس ناتری
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/448649" target="_blank">📅 13:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448648">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در بخش‌هایی از بوشهر
🔹
دقایقی پیش مردم در بوشهر صدای ۲ انفجار شنیدند که هنوز خبر رسمی در خصوص محل دقیق انفجارها مخابره نشده است.
🔹
صبح امروز هم دشمن آمریکایی نقاطی را در استان بوشهر هدف قرار داد.
🔹
همزمان اخباری در خصوص اصابت پرتابه‌های دشمن به نیروگاه اتمی بوشهر مخابره شد که فرماندار بوشهر آن را تکذیب کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/448648" target="_blank">📅 13:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448647">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی بیمه دانا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wkw2dfkj8OYaY7PUaMb0QWE9axDS0aF6PnypuiSlO5zp87je5BiYdNODq6JdduJ1EZS4ucA3Kdq8Zgfi6ss5VZESGKyZmd1Dae9VgUd4aMTSOEQ6_oz2A4BaJ-IHp4o66pokzGEqfRrFWd9h8aVRfKIrLuxzC0UI10RRiY9yXH3upuez2OjNIqCSNQKoBwW2Q73Lz_xDstunge9MDttpN5u8n4jq4uqpbAdN4x925UQE3AOwtCShDEwZIdtty1JMzAw8-rJSEXrsjxC5MFJTdx-xID6hIA5D1RsH8TLnZGCDhzAIcTJHDTNUcIQQJD7LDiQcaGu26oAHzuJRxW4_jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔰
حضور همکاران در ایام تشییع رهبر و آقای شهید ایران ؛
ارائه خدمات خسارت سیار بیمه دانا در سراسر کشور
🔺
همزمان با برگزاری آیین بدرقه، وداع و تشییع رهبر شهید انقلاب، شرکت بیمه دانا با هدف تسهیل خدمات‌رسانی به هموطنان و زائران، خودروهای خسارت سیار خود را در شهرها و مسیرهای منتهی به محل برگزاری مراسم مستقر نموده است.
🔺
به گزارش روابط‌عمومی بیمه دانا، خودروهای خسارت سیار شعب منتخب این شرکت در استان‌ها و شهرهای واقع در مسیر تردد زائران، به‌ویژه در مبادی ورودی و خروجی شهرها، مستقر شدند تا خدمات ارزیابی، تشکیل پرونده و رسیدگی به خسارت خودروها را در کوتاه‌ترین زمان ممکن به بیمه‌گذاران ارائه کنند.
🔺
این اقدام با هدف تسریع در فرآیند رسیدگی به خسارت‌ها، کاهش دغدغه هموطنان و تسهیل تردد زائران انجام می‌شود و بیمه دانا با بهره‌گیری از ظرفیت شعب و تیم‌های خسارت سیار خود، آمادگی کامل دارد تا در تمام ایام برگزاری مراسم، خدمات مورد نیاز بیمه‌گذاران را به‌صورت میدانی و در سریع‌ترین زمان ممکن ارائه دهد.
🏴
بدرقه آقای شهید ایران
#یالثارات_الحسین
(ع)
#باید_برخاست
☂️
بیمه دانا
📞
02182468
🔰
@dana24_insurance</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/448647" target="_blank">📅 13:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448646">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فعالیت موکب سازمان منطقه آزاد ارس در مشهد مقدس
سازمان منطقه آزاد ارس طی این روزها با برپایی موکب در مشهد مقدس خدمات مختلف پذیرایی، اسکان و تکریم به زائران و شرکت‌کنندگان در مراسم تشییع رهبر شهید انقلاب ارائه می کند.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/448646" target="_blank">📅 13:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448645">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/448645" target="_blank">📅 12:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448644">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7ec02ec64.mp4?token=D7Cq5sIi4ZQ1NZTaGdOokOqfjd7p51-7YvvFnKKfAjbdYWfkzbOpbBP9o5qqWqs2GyAQRd_xCY3OrHdbVyPGESLPNA_LUY2ymQ2FT7oyF7CasAbQ6NwhMECMzh5vEvrXGPt23cJFjPTkIA5f-EPr4S8EyruD2DVtmhNbvWqtve2wl7UetH1uoquPk_P0XwYBMLkS2oDDoyjiNxZincMgc5A_81ViBs5J8VtXDHkSigwE1V1HqgoPd8IJXdWFHTVnJt6yevTPqI_Z60XpPhvObUFBquqB2DA6qVnrXcyxOs_QXhSdj2A7_ewfs7FRaWNFnzOmJv8TAu3F-F6Rh7bNug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7ec02ec64.mp4?token=D7Cq5sIi4ZQ1NZTaGdOokOqfjd7p51-7YvvFnKKfAjbdYWfkzbOpbBP9o5qqWqs2GyAQRd_xCY3OrHdbVyPGESLPNA_LUY2ymQ2FT7oyF7CasAbQ6NwhMECMzh5vEvrXGPt23cJFjPTkIA5f-EPr4S8EyruD2DVtmhNbvWqtve2wl7UetH1uoquPk_P0XwYBMLkS2oDDoyjiNxZincMgc5A_81ViBs5J8VtXDHkSigwE1V1HqgoPd8IJXdWFHTVnJt6yevTPqI_Z60XpPhvObUFBquqB2DA6qVnrXcyxOs_QXhSdj2A7_ewfs7FRaWNFnzOmJv8TAu3F-F6Rh7bNug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همراهی جنگنده‌های ارتش با هواپیمای حامل پیکر رهبر شهید انقلاب و شهدای خانواده ایشان، لحظاتی قبل از ورود به فرودگاه شهید هاشمی‌نژاد مشهد.  @Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/448644" target="_blank">📅 12:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448643">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9c6f87502.mp4?token=TA8So-aDrRQQjd3cp91bi_ew9ZIYRbps3F67aI87NH-wz292Nhk1QIuhTyIH1InXwGU6Bi2Q_l7R_zkkRZnhM8duB45nA9kIaKCgY5LPykIu3E_QZ-y8JDevqBGPmgUzRPJIa024BPokgP05nDICmaCA4FoRzJuufg0rl3hYFKDZcC8LxwdCNokfD5-BgXGrMCQmbdMi4FLrrXdjiA0ZZ3tZa-1O7E9BvN9x6QRxITSmrdWIUkjKCOuUJpfotPvwE-VZPHNRgelZYDRBn4UVqdP4fTbW21yVXpApRrXh6oy0wVnKtFiz541rshc77Qr14d79hXPyv8TLECSQjvXRuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9c6f87502.mp4?token=TA8So-aDrRQQjd3cp91bi_ew9ZIYRbps3F67aI87NH-wz292Nhk1QIuhTyIH1InXwGU6Bi2Q_l7R_zkkRZnhM8duB45nA9kIaKCgY5LPykIu3E_QZ-y8JDevqBGPmgUzRPJIa024BPokgP05nDICmaCA4FoRzJuufg0rl3hYFKDZcC8LxwdCNokfD5-BgXGrMCQmbdMi4FLrrXdjiA0ZZ3tZa-1O7E9BvN9x6QRxITSmrdWIUkjKCOuUJpfotPvwE-VZPHNRgelZYDRBn4UVqdP4fTbW21yVXpApRrXh6oy0wVnKtFiz541rshc77Qr14d79hXPyv8TLECSQjvXRuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زائر پاکستانی: آقا فقط برای ایران نبود بلکه جهانی بود.  @Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/448643" target="_blank">📅 12:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448641">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‌
🔴
سپاه نینوای گلستان: دشمن آمریکایی در بامداد امروز با موشک کروز نقاطی از پل آق‌تکه‌خان واقع در شهرستان آق‌قلا را هدف قرار داد.
🔹
این حمله هیچ‌گونه تلفات جانی در پی نداشته است. مردم عزیز آرامش خود را حفظ کرده و به شایعات توجه نکنند. @Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/448641" target="_blank">📅 12:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448640">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1320feb57c.mp4?token=p4cJtTOPQ9tzE7tkg54v7NG-BR9LxaW04GRJaoEQOybv4sNelvqbi0qnqjoU-QHJ3xKRx_yxFqWuSuH6EmKiDCbtrn0IpWB0K9fRa4GCvX7LfyC62_j0EuL7hlDYJNymGyjfazxjkgYw89RbLGwPqv6cOXJ5STRw06x6p0yY5QzOvbKPYMs2cFQwR7YOUhp32Fi2UHJz5apHN7awRrhrnfIolG29LaJBbKNKEaVO6LiYY6h0WDptfg7hDxAqV-SwtFfXgtG_O45LuWgnj-2kLB_Ff7rGUsK5twgBMGWc92C-0-4B0YCKhS2iT013yyD6Xgj9ja0IZApohKvhl55hKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1320feb57c.mp4?token=p4cJtTOPQ9tzE7tkg54v7NG-BR9LxaW04GRJaoEQOybv4sNelvqbi0qnqjoU-QHJ3xKRx_yxFqWuSuH6EmKiDCbtrn0IpWB0K9fRa4GCvX7LfyC62_j0EuL7hlDYJNymGyjfazxjkgYw89RbLGwPqv6cOXJ5STRw06x6p0yY5QzOvbKPYMs2cFQwR7YOUhp32Fi2UHJz5apHN7awRrhrnfIolG29LaJBbKNKEaVO6LiYY6h0WDptfg7hDxAqV-SwtFfXgtG_O45LuWgnj-2kLB_Ff7rGUsK5twgBMGWc92C-0-4B0YCKhS2iT013yyD6Xgj9ja0IZApohKvhl55hKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور شیخ زکزاکی در مشهد برای مراسم تشییع رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/448640" target="_blank">📅 12:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448639">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acdd229a75.mp4?token=E7JBMpH42mK6htubiEVnrvkYPOu-qULazWLdbzJa4C-AYeJtomsPFcWPaYpkAj7ipZztYeLurRLq4sHetHPhGE2X9J0b5XiAsBCZPDAGtchih5HSBCLwjQ_GJa8941JMrfSkPyVX99N6ZaL0fJ2B5IZS1dC-gzPh7_sSY0f6uNz6WCJKDZdkr9SZCjuAFqn4Bsmy8tf9z8eIuSPNanpBOhK45qwjjBrqaa3O2KiVM8EI2GL8WqkmFftBksF6GXVXTwrLlXBdHNuQplEg--QU7rgBrDaimfJSHY1E4hF7jiIv96C23-6l-bm2SFfaB7g3e56_pUWIi0oehz5MoIJhVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acdd229a75.mp4?token=E7JBMpH42mK6htubiEVnrvkYPOu-qULazWLdbzJa4C-AYeJtomsPFcWPaYpkAj7ipZztYeLurRLq4sHetHPhGE2X9J0b5XiAsBCZPDAGtchih5HSBCLwjQ_GJa8941JMrfSkPyVX99N6ZaL0fJ2B5IZS1dC-gzPh7_sSY0f6uNz6WCJKDZdkr9SZCjuAFqn4Bsmy8tf9z8eIuSPNanpBOhK45qwjjBrqaa3O2KiVM8EI2GL8WqkmFftBksF6GXVXTwrLlXBdHNuQplEg--QU7rgBrDaimfJSHY1E4hF7jiIv96C23-6l-bm2SFfaB7g3e56_pUWIi0oehz5MoIJhVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در انتظار آقای شهید ایران
🔹
حضور گستردۀ مردم عزادار امام شهید ایران اطراف حرم مطهر رضوی ساعاتی پیش از آغاز رسمی مراسم تشییع   @Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/448639" target="_blank">📅 12:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448638">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/194e21f6b5.mp4?token=DUUamg8qLatwkHfPC-8lvkLvdGMzrImg9c6UGoFbAAuzJ-WdehOZY9OXo-Zx5BKrcX0yJN0s0y9oE8fssNuW2FnDys4gY3eQeqTecBDSyc7XP3qq6Ab6L09-z47dIT-PV3p6zeNYeLsRO2kJYlNKXaHgFCZb6zpEasM1Nh8hHJpqzFReHNS5Uhkc-IiwD1bGBOdlT6PsEJvQPS0VYWp4X6CPAy6cbIzPV8tfwFxgf0gF1i7kSl7nIftfMRxJSzMbg4_wI2QWctxsGYfLeV578n-Bj3pQlpbLzzGF2fQSqY_rm1N7vDArPAsfdVy9nHdmVbdFpNjDX2onKf56WHZ6Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/194e21f6b5.mp4?token=DUUamg8qLatwkHfPC-8lvkLvdGMzrImg9c6UGoFbAAuzJ-WdehOZY9OXo-Zx5BKrcX0yJN0s0y9oE8fssNuW2FnDys4gY3eQeqTecBDSyc7XP3qq6Ab6L09-z47dIT-PV3p6zeNYeLsRO2kJYlNKXaHgFCZb6zpEasM1Nh8hHJpqzFReHNS5Uhkc-IiwD1bGBOdlT6PsEJvQPS0VYWp4X6CPAy6cbIzPV8tfwFxgf0gF1i7kSl7nIftfMRxJSzMbg4_wI2QWctxsGYfLeV578n-Bj3pQlpbLzzGF2fQSqY_rm1N7vDArPAsfdVy9nHdmVbdFpNjDX2onKf56WHZ6Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظهٔ ورود هواپیمای حامل پیکر رهبر شهید انقلاب به مشهد و پایان آخرین سفر ایشان  @Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/448638" target="_blank">📅 12:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448637">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5f17605e.mp4?token=ul-rrtbmzP9OXVz3ONfvsknkTbDmIosAYtGGwH7u4twBIpsTKydGIXs8UX-g668VkRq5eyf-3G35B7A1LSXojrt9GsHfs9-wAdI0KzNVPeRikszmP_r6cK8A2c1GgamKSDVV-tkKgX_t1OcvNfsGKRy6syYgfUgHSCk58n4MhMCNuSE-ApJUIQGIAbkUPieglQ9p4mwwIT9OsmwI9M2FLt78xUbSjU1bLHh674OLxukelR5m3srhqtPFlPB83kz5i8BOa6lsh8V2RwefkZluxEXBAHeWCyr4UwWYQZGEo2QA9Nl89b_jDJmX2l-6JwpM4yqHmtnko5O0_bu0r4A2Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5f17605e.mp4?token=ul-rrtbmzP9OXVz3ONfvsknkTbDmIosAYtGGwH7u4twBIpsTKydGIXs8UX-g668VkRq5eyf-3G35B7A1LSXojrt9GsHfs9-wAdI0KzNVPeRikszmP_r6cK8A2c1GgamKSDVV-tkKgX_t1OcvNfsGKRy6syYgfUgHSCk58n4MhMCNuSE-ApJUIQGIAbkUPieglQ9p4mwwIT9OsmwI9M2FLt78xUbSjU1bLHh674OLxukelR5m3srhqtPFlPB83kz5i8BOa6lsh8V2RwefkZluxEXBAHeWCyr4UwWYQZGEo2QA9Nl89b_jDJmX2l-6JwpM4yqHmtnko5O0_bu0r4A2Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در انتظار آقای شهید ایران
🔹
حضور گستردۀ مردم عزادار امام شهید ایران اطراف حرم مطهر رضوی ساعاتی پیش از آغاز رسمی مراسم تشییع
@Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/448637" target="_blank">📅 12:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448636">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkdlZiD25aJ75iigfvEJ7gc5tXp0JMfEOlIw3sY4AjtD58XJFw5yJvMw8UDKxtD0eNpXsI3brdnC7xT4VfTJPC5wGD2yYy_ZATCserRdLfc_1b3NgyVknHdHBJVzCGJd9-D1V2tVWiAoGhGRioIUU2OOMnZIljC7OltAgP1aN4VmXbwlOJhoracyRp-mMpkqf_JVakjJJifBawWaHLM0nFsUCzepzUY8_lCwz9iQKrA6VSlgJwl36jTWrktGbihnBefE3OkJwI2IA0fEdXgvfHeUg-9ll48Zthgh0HZojHeYLbR6YgJOIMSX9HfqPLaos4tbUNpOXzw5n_JkSjvdHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلس ختم رهبر شهید انقلاب از طرف رهبر انقلاب فردا در قم برگزار می‌شود
🔹
مجلس ختم امام شهید امت، از طرف آیت‌الله سیدمجتبی خامنه‌ای، فردا بعداز نماز مغرب و عشا در شبستان امام خمینی حرم حضرت معصومه (س) با سخنرانی حجت‌الاسلام سید علی خمینی برگزار خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/448636" target="_blank">📅 11:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448635">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
انفجار در بحرین
🔹
وزارت کشور بحرین: آژیرهای خطر به صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیک‌ترین مکان امن بروند.
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/448635" target="_blank">📅 11:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448634">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">تردد نفتکش‌ها در تنگۀ هرمز به صفر رسید
🔹
درحالی که در مدت اخیر پس از تفاهم اسلام‌آباد میانگین روزانه ۳۲ نفتکش از تنگۀ هرمز عبور می‌کرد، با نقض مکرر آتش‌بس از سوی آمریکا، بلومبرگ امروز پنجشنبه از تعلیق تقریبی همه عبور و مرور دریایی در این منطقه خبر می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/448634" target="_blank">📅 11:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448633">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSEAoR-4l8D6GTgs3cBJWrzofziQatfGYT8-wmfg493fKqmjxTu8WqosnhMxjW-ZEF8tUnxQ_3UVo-kkvno-cPTtVROzoe1fhHJoL2KH5RNPN3KBvjRDxS4jKMCBaxjTgVp-Xlv5DtXicGDftiS6N63gOI4Hj3YoFhOsw5qi9IKmrQ--BkHd8GQNUCRiz48QdJBbWfFoVLJN1WQvzl_Z30Lmxn9dePnETxTdNkWi1gxzdzwBlRdrKXCZTnzd0uoY-xIjUvaSxAKCnn1ZV3d5Ma747wWB6BVBaUC9TR9eOWIUB7bAZmV9lrkGu3Ph1EwS498ZHtVbHvZyDc6LWZrrug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان در پیام‌هایی جداگانه به سران پاکستان، تاجیکستان، ارمنستان، گرجستان و رهبر ملی ترکمنستان، از حضور آنان در مراسم تشییع پیکر رهبر شهید انقلاب و ابراز همدردی با ملت ایران قدردانی کرد.
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/448633" target="_blank">📅 11:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448632">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d7c1b18d.mp4?token=E0rYpT9_6CVKfuyXk2XMprafvo_ljWjsum5BafdFxX5XzXq4F8qpzBqD-t_KzNv9-fZGDSPQTHJpwyL9vPHC7Stm0V8FT6xVzRQLZqATlSJwjAEa1mmb10qP5phRNa7UNj7eXhuppK8LV95HQS2tSBLkDnai897eryaQ9AkBCB-WldfVKAmRFg2bRLV77VIhF7BkQyBWE_s7DuvoGcLLl8hOm24eh7Nsgd8Uqa0JG8nugI1LrZUQPK4JIhYKuKQeKgciZADihcJ1aUD6a0mCzSN7x9Zmf2z3TgsQ5IUVD1pypEWM0MZ2jhPxtNBC3HSZbYhJWExXqOh2Q2IEq2Owtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d7c1b18d.mp4?token=E0rYpT9_6CVKfuyXk2XMprafvo_ljWjsum5BafdFxX5XzXq4F8qpzBqD-t_KzNv9-fZGDSPQTHJpwyL9vPHC7Stm0V8FT6xVzRQLZqATlSJwjAEa1mmb10qP5phRNa7UNj7eXhuppK8LV95HQS2tSBLkDnai897eryaQ9AkBCB-WldfVKAmRFg2bRLV77VIhF7BkQyBWE_s7DuvoGcLLl8hOm24eh7Nsgd8Uqa0JG8nugI1LrZUQPK4JIhYKuKQeKgciZADihcJ1aUD6a0mCzSN7x9Zmf2z3TgsQ5IUVD1pypEWM0MZ2jhPxtNBC3HSZbYhJWExXqOh2Q2IEq2Owtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
ورود هواپیمای حامل پیکر رهبر شهید به مشهد
🔹
هواپیمای حامل پیکر مطهر رهبر شهید انقلاب و خانوادهٔ ایشان وارد فرودگاه شهید هاشمی‌نژاد مشهد شد.
🔹
براساس اعلام ستاد تشییع رهبر شهید، با توجه به استقبال کم‌نظیر مردم عراق از پیکر مطهر امام شهید، ورود پیکرهای مطهر…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/448632" target="_blank">📅 11:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448631">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سفیر انگلیس به وزارت خارجه احضار شد
🔹
در پی تکرار اتهام‌های بی‌اساس مقام‌های انگلیسی دربارهٔ «تلاش ایران برای انجام اقدامات ضدامنیتی در انگلیس» سفیر این کشور به وزارت امور خارجه احضار شد و اعتراض جمهوری اسلامی ایران نسبت به رویکرد ناشایست دولت انگلیس در قبال ملت ایران، به او ابلاغ شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/448631" target="_blank">📅 10:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448629">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسِدخارجی</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CdzYDHf-TdL0kSJ4g7ZzTyx3G2VD4p9VN_fyTp_rH1ufzS98KvURKTqOgucJquXvYoI7yegxir8W7IrKdWBMCza-fPEJRUUheIdJ73nhRdtiPVv8SZQCaeqcSbxhy16Kqs2DiFY8RZLOOXNWNtwrxmu6KDRMM6xcdXLZ4371XNtFDB3Sn8JJ67PukHcwbGH6Efe6Q_eFcLWeTGVTY9WVck9J9AST0AWFS-41OYjeJjZa93fioUqa1gOa-yjMzU-vrhAnmS2H5VtQ8bp62JyhYyHprHonoMflgoCNUr76qYIU2SL3UwMcOyYIvDtFWci-Bbf58deUivbYlpMwp9wvLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام به همگی؛
خیلی از ما این روزها و روزهای آینده، بخشی از یک واقعه بزرگ تاریخی خواهیم بود.
«
به همین خاطر، برای ساخت یک مستند بزرگ و مردمی، به همکاری شما نیاز دارم.
»
از هر قشر، با هر نگاه و از هر کجای دنیا که هستید، می‌خواهم داستان و روایت خودتان را برای من بفرستید تا در کنار هم این تاریخ را ثبت کنیم. اگر خادم هستید، اگر میزبان، میهمان، مسافر و زائر هستید... یا حتی جامانده هستید...
📸
چه ویدئویی برای من بفرستید؟ هرچیزی که فکر میکنید!
🔻
اگر خواستید جلوی دوربین بیایید، اگر خواستید حرف بزنید، داستانتان را بگویید و از حس‌وحالتان در این روزها صحبت کنید. حتی اگر دوست داشتید باهاشون مصاحبه بگیرید. نیازی هم نیست حتما به پیکر مطهر شهدا نزدیک باشید.
🔻
ویدئوهایی که قبل‌تر هم گرفتید که مرتبط با مراسم‌های رهبر شهیدمون هست هم به کار می‌ایند. حتما بفرستید.
🔻
گاهی پشت‌صحنه‌ها و حاشیه‌ها از اصل جذاب‌تر می‌شوند.
🔻
فقط ویديو بفرستید. افقی فیلم‌برداری کنید (اگر قبلتر ویدئویی رو عمودی گرفتید هم مشکلی نداره بفرستید)
✉️
راه‌های ارسال ویدئوها:
سایت برای آپلود:
https://upload.sedkhareji.ir
تلگرام:
T.ME/SEDKHAREJIPM
اگر باز موردی یا سوالی بود بهم در
@SEDKHAREJIPM
پیام بدید
خاکم؛ سدخارجی
✔️</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/448629" target="_blank">📅 10:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448628">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPabHZ7Q64u_jg0TvhfxJ5_RIh7FdHQZrL0d1xOxRMrbuYtz6xv9AsLeSFlqfJvT6tQFYCp3Ix-Qo9VMHQOZFX-s-S0p_861BKOAFx8l26CaPZlkMgr0y6xrNlF6mdESieT072ji2oJE8Lw19cEivtgNOXzw-cJgmNmlaqdj_7451yB1zgrxZPGhh8ShomwFEvV822kWLdaiS0GBfxUwof77BQtv35i6alGJdYOvIX5-XAbH89aeX6PwC_e3eeg1Z5YmJvZ04BVNWE1qxf0N4xJ39zFyxBhcNu1FJFMfsqMiqyTDt6ebmfxNst5-9pEz5E2oXm_9ooKtxTlk1SkKog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/448628" target="_blank">📅 10:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448627">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/448627" target="_blank">📅 10:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448626">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🎥
هواپیمای حامل پیکر مطهر رهبر شهید در حال ترک فرودگاه نجف به مقصد مشهد  @Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/448626" target="_blank">📅 10:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448624">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b3efea6cc.mp4?token=iCrVlF_gxuKfg9UZGAiUNZmRTPyDIrb6ugwesACGV2Tdz_e8sItate-Xaukb7ZjIhDxmZpuBt2tsaGxZyt40ThjA1L08l4IONhXALnVlsRu9csQokAzh3Ap9SjKJGspAwS6L-ZFXhTed-ZRer_tG1CmP9ZixOhXh7oPwZygyqkJD6CYf9YKK2sNftCQTEon-WsVhBRtZqoF2B98_2FeXojLO2G7ne5BepooxzCDdXF6krcTfVeb4Na7_OfoVsjTV80ftYIuVGRvLdqpoWUb7vof_Rxr_x3JeWPIHUEhs_Tj7Znvb3K-MK6iYMSg4hF2tVIZf859zUpj5yZJvVze8nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b3efea6cc.mp4?token=iCrVlF_gxuKfg9UZGAiUNZmRTPyDIrb6ugwesACGV2Tdz_e8sItate-Xaukb7ZjIhDxmZpuBt2tsaGxZyt40ThjA1L08l4IONhXALnVlsRu9csQokAzh3Ap9SjKJGspAwS6L-ZFXhTed-ZRer_tG1CmP9ZixOhXh7oPwZygyqkJD6CYf9YKK2sNftCQTEon-WsVhBRtZqoF2B98_2FeXojLO2G7ne5BepooxzCDdXF6krcTfVeb4Na7_OfoVsjTV80ftYIuVGRvLdqpoWUb7vof_Rxr_x3JeWPIHUEhs_Tj7Znvb3K-MK6iYMSg4hF2tVIZf859zUpj5yZJvVze8nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیل جمعیت در مسیر منتهی به حرم مطهر رضوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/448624" target="_blank">📅 10:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448623">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سپاه: زیرساخت‌ها و تاسیسات مهم پایگاه‌های آمریکایی در کویت و بحرین مورد اصابت قرار گرفتند
🔹
سپاه پاسداران: ملت شریف ایران، ملت کریم و مجاهد عراق؛ آفرین بر شما مردمان مومن و بصیر و وفادار که با موقع شناسی و تشییع بی‌نظیر در تاریخ جهان قدر و منزلت ولایت الهی…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farsna/448623" target="_blank">📅 09:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448622">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17c1c4ac0e.mp4?token=hpZsBeMDqENSg2l9CbuekqdFBXCochs0xGpHcWIxyKuOhpptm4KORI2BhmKB_yfrp2ofM-_cZX5jJxuJqGOtG8ma5Qp863u7OTPLx2ti-yX-XV-h0lOJ5TcXPz5XSOLv24QV_VcaXr-TIwdg6i4wmMfpIsI5FESSUganARb8krjep9u9NhuaV3vWPpTpgSIUAT9t9112Ndn735kq3y_DXbFAzcQ6tE17w1Adx5Q-ec1rAE9Q-gjHzzh9r1pliGZjDk9uHhF5feJ38O4yip6qrIydmoxMx8ZjV7HVQM8pgolIqFw_0lTl-pkyJM5iWbPas8l_Un4CwHEkgZiG5uwwWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17c1c4ac0e.mp4?token=hpZsBeMDqENSg2l9CbuekqdFBXCochs0xGpHcWIxyKuOhpptm4KORI2BhmKB_yfrp2ofM-_cZX5jJxuJqGOtG8ma5Qp863u7OTPLx2ti-yX-XV-h0lOJ5TcXPz5XSOLv24QV_VcaXr-TIwdg6i4wmMfpIsI5FESSUganARb8krjep9u9NhuaV3vWPpTpgSIUAT9t9112Ndn735kq3y_DXbFAzcQ6tE17w1Adx5Q-ec1rAE9Q-gjHzzh9r1pliGZjDk9uHhF5feJ38O4yip6qrIydmoxMx8ZjV7HVQM8pgolIqFw_0lTl-pkyJM5iWbPas8l_Un4CwHEkgZiG5uwwWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواپیمای حامل پیکر مطهر رهبر شهید در حال ترک فرودگاه نجف به مقصد مشهد
@Farsna</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/448622" target="_blank">📅 09:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448615">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z3nkoHD8f3EgiBejcMG-HCagj5Yg3dvRfdVcGPqz3ofs3Dp_2n-VdNzsVVND60DuMVM0xlYrjnmmXD475BRJagjjM9z2RoHjKn4lbTvKj8dxondxoKZua9vu0Wf2eQFdLdEkBV_hCLW48eA0jvGSoV361fyYRFubtIw81anqGbdy2sxE1HQLVGcUV0Kc0BJuGeEClc2cjldXf-XOtJskT-wn2mbSyT-ICSZZeGNTQLhCcMLvuDVZ9FvgU3zl4UKKT1ZHyc5Ld7t2aBUhoMQl97_FCKjK5PeFsKZ1txvTxsNs_Sz8aN6HK3NyuVwLovPiGfHZbUz6HOKOmoq1LKbHmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gm3nVPmFnY8jpC9eM8WKaEIM5xuBuP5Es4STgTt9xePtD9lXvyVyb5YPE1pGoe99CE8qMKwlW-JOiZ4b4Y6GUzKimqdzpsuqqDUJzIermPce-O5X9Cf7m31HRqgdiFGRSOufzeHMnk-2PIacNbZGQYTBVXX8-Uw9p3SNrz8QGyUPQFdPyiLM273Oc1cqQUsbq_z1ysT0obDWFLJxD9S-0KHyTWvfSNJOG-vkBpPyHlDHwyxc18zJJ09XA-2GjpjgfmRcPAjJ7qkGxZzXtSTX7GJSi1UBSDy_fjOUYxbHJ7bw_Rm_7fcY2_1NK3nZO61FJOpRdF5_6Pdi5lU5nVpieA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T4UJhtUzs6hc4eNWdbuM34Z89Kdj3N0bnAcXJjJaZ3JV5o_ng9zOx-Vkp9B0IG9r1f-lYsti4jdYxZzNab2oy-QgKDw9z-2UYYXAgLwtk1yXhSC35ZF16N8K0OpAHWHXrTkV1yHpUoLssnJeCX7yNq0Y-cuokeMOseUXIi5_dhZwvQG_C-eirbX4_DBQ6QM47tAwAvnQL2j0WwrJalJVH1tocMhI-TEPpQBZ9uVQfKQ1luUBWqmUSX4r2J5YEhiq-tDpI3VxIujINE-3_irubsB61aVpSGWsug03_TlZiXW7Qkg8HlRP54P2MMV6lSWm15t_OkKwa9Axl2He6OdITQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JWnzUu4T7sY8vCxyzISdr72LnVk9MUpUUEKta3UdoWvvDEG7t0-7nispOC4VeFJ7Pn-t-MUV-sA4FL2tAYKyc7PP91FXM4Nr-5UjCumiGY03nnGbUDYeBtbD8MHgTMsYQkI73asxX6uN6ITOnsYhfjx0nzr1VfNxEiKzAvGJRJV-Bxv2BI43EzpCW_SfLEoiS7GRSkknzFFMLLKXU82o-PfbfZvor4ixOMN1c8ez0gfRNc5n_f3BMUuaIWa-QOam24qETbln5KEAKnuY3jDKOXo2MXYYZF3nMcT92ErBz6aXG3BYZ1SmmX6Wmsm3JP658_gJpjzOnhd7LjZY6GhnwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qomeM4gLFtGfjTUmURjLrbmVm6UporMdZmaEuRE8CzZ_XalFDGKhMyodqqxOVAQbuTH7-ORsjeHBDHilcR4KeKm2LS2eoB4NSuzOXWu3dQ_k6M3sIJdXMsg8ESF46d22N55URzebES-Ki8Xg6R1uecL3AhqodSM56_Zvdl1uJyM41n1O_OzvPIHR_s8txQD_AyAZb2fvT7cpCRbN4Z8Te5Lz1sLItV2EBka9bTG1dFZt4UiYePTqZmmQ3QHXMmqoEmBKvYDGvAYhW27-I0gFLZ0gpJ7RBsB39J-iRIZ4S4bsFtzWzTU4sJjcVPf5rEszUZ1j5bhvr7Vul8NNM86vDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gXJMMZaC8S8ZubiEl3qPHmQbo_LYC5OHePXKhnVQvd0Myfucphl_z7mpT6uS4myfeY9rZGFWFXd6Dx9VXGdAZ-XdLusF7aNVLBl6J5y_qD4xPOTHwCbJXoLSw8J4vZrZphdMj9GOqZ95OdhfPm21jBRvsUyh7lweBG0RtYDKQmjQKMj678KS01KOHfgZ2JI5IH8XAYHK1ol2EvfCgp8eWKaF7R4E-4pJ3x69GibQ26rWlwiOVu2HGFue-zNYSVQMTapmqokNgBTcWT5fphOhOPzvAbPGWH1gQINhphyb2cP4imlphKOPMYOP2fXcsfLZeBmQvHtgui1oGNPzCo4_Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZKhsnr8jRicTt6WizZfjcMdSV3UFLmqjRggrZdz4OuMIdmZaP2o28szup8_N1na89hCKizoAAMwOcLdMdWrjaLiIItvhzApSJ5guizQBdLimLTqN2nn17mH9opOi0fnwT9Ab2UJLjIwEcZRtsG-m2yQjyY7hymTMw5J3zbbYgkPUXzUXgJJ07Og3ND_-_NDUhLSvnZHL0atXXVwMcx_xFPaQ9PdyDe_-kl-c4QALVGUC3K8Wtld8RBwXtK3jLLWbWUIpfk-VK7kZ308XDEqxOuPeeWPOXPXrYywkwzbgoxeigoX3Pb2gQHHew1SC7--Z5TvARVeBEoK_flJLJT-FIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حب‌الخامنه‌ای یجمعنا
🔹
تشییع پیکر مطهر رهبر شهید انقلاب از قاب عکاس اعزامی فارس به کربلا  عکس: محمد آهنگر @Farsna</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/448615" target="_blank">📅 09:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448614">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5046daeb0.mp4?token=VvmD24CrT2UtvxV3OGJbmIXfmWmKjzALo1oKEaOFuShnregxhN1uoiXUUa_-vOCmB_VPhdsatbV9FmGhstAFjVsxozg9IFNiVfNDbwyE2LTsGWhPl2MRwVVRw8SonhkHYk77Hzsm7WxoYrpTED-bS5dfwd1sZUzzVIc1dlGVT9unz-ZA3cddWKFNqEEb5z_HlN1HSjrdkhWL4PAy9tduHgtKekXfq8RWwZcSLYrJYJn-8Ce7VxDK1X2A8k0GJIO0O5e8n09yZkQlo60ySFpGoG-k1FP7X-nk1L5HB3fZmQ_CGNMm91QTG6_8_mCWhti5mFR4DcrjGi5-ApPqPAdoVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5046daeb0.mp4?token=VvmD24CrT2UtvxV3OGJbmIXfmWmKjzALo1oKEaOFuShnregxhN1uoiXUUa_-vOCmB_VPhdsatbV9FmGhstAFjVsxozg9IFNiVfNDbwyE2LTsGWhPl2MRwVVRw8SonhkHYk77Hzsm7WxoYrpTED-bS5dfwd1sZUzzVIc1dlGVT9unz-ZA3cddWKFNqEEb5z_HlN1HSjrdkhWL4PAy9tduHgtKekXfq8RWwZcSLYrJYJn-8Ce7VxDK1X2A8k0GJIO0O5e8n09yZkQlo60ySFpGoG-k1FP7X-nk1L5HB3fZmQ_CGNMm91QTG6_8_mCWhti5mFR4DcrjGi5-ApPqPAdoVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایی خاص از طواف پیکر رهبر شهید انقلاب  بر گرد ضریح حضرت اباالفضل العباس(ع)  @Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/448614" target="_blank">📅 09:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448613">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">تردد قطارهای مسیر تهران-مشهد متوقف شد
🔹
راه‌آهن: به‌دنبال حملۀ جنایتکارانه دشمن صهیونیستی آمریکایی بامداد امروز به یکی از ‌نقاط مسیر ریلی تهران-مشهد، حرکت قطارهای مسافری در این مسیر با وقفه مواجه شده است.
🔹
تیم‌های فنی و عملیاتی راه‌آهن بلافاصله به محل اعزام شده و عملیات بازسازی محل آسیب‌دیده در دست اقدام است و تلاش می‌شود در کمترین زمان ممکن این مسیر ترمیم شود.
🔹
برنامه‌ریزی لازم برای جابه‌جایی مسافران قطارهای متوقف شده در این مسیر، از طریق ناوگان مسافری جاده‌ای به مشهد انجام شده است.
🔹
مسافران برای کسب اطلاعات بیشتر از آخرین وضعیت اعزام قطارها در این مسیر از سامانه صدای مسافر راه‌آهن با شماره تلفن 0215149 اطلاعات مورد نیاز خود را دریافت نمایند.
@Farsna</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/448613" target="_blank">📅 08:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448605">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fkqu2ub0E3qZYJg7PaRarqafO1ZdjLCTx0Y6FHkC-gEFPG5F7k-9F3O3-AQ0mZbryPOru2TGOPV7T16X6Ow-SlVoOLJr7gzPaGcCuWvdQe8AqQ66o6V2D2Q88gVWVVl0HhxeVB-5j0idHruNcgmdxTP0R4CB-w7undVX3-2SaFohfkx1XbO76fz6w8t75I-13s-Zcxx69NeKfn6msaimEvdxCKpnigscqRcjIpiADhrFcPVDd9A7zwZv5gorMl72uWGbOsNJJjzpScIbwJKakLDm6wzEKc8F0K1-YKy8aoNASxyasC6i9LAR4t5Pw544RkS9iSLV3kfa3u-LDBeACg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s1_5VxbY_hAlq1aQJlnmG4A8rk9bMEz80mlysU97XngF8NpULLyYDZ0GslLTtVX-rIwlwn69JJaz3iyI1b2miIvYsBT0ownpPBl0O9he6MoMT_gSrDKWyagD3VWhPIeia1tBQ57USFL_V0fGtkq6-P9KfafzpybF_FUrAnT2kLHo_fvBx-vvLSeh8PqWYs5VLR9vcsHrImw6elZsYYMQ6VZRpFnwyD8obgmBq3WFLcpE8IVKGtf80Fs1o1ehGTg3nAXupao2_KjiK_cQlXBBNubRoIDB8CunkmIQwzBuP2-JGc0pCKgqxZBfIjTzxUdPkYFnVpeuIoWqxW20t4R8jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JSJCOxqOLsKCyx2AyE7_mVL70jWycOOrPUaMUb2PXk6n0_UlTNRXi6pBxomYNZeW1Q0-dU9Swpx7n5R3WUBLUghC318LDEeFAgzOlEhPDMUX6_l488bbbxR8HxWKjypY0CPIKRkG70eu2xPxxAxHZl4GqM7wESLd5PT7C3oxnEKSZiI0Pt8Dwz0ZwjasKwaRm1X6zznqZLLWFHzAcKtFZrGQvtbhKbtMBEzsNfT_XxfhJ9rV5QeNrniLlw2-A84l7NMAbC01HApaHW5wE_QOewFDIsNmmdKYIj9bOIShpbebiFZGUuFfN5AUZoQtsLfC6L6-G6b8LwC7MfGVHRD7ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UZd_CiR6rZHSJBvi_ZWEE9QdhddJ8I_kSONALDAq6acsv_rHz0dzy1IGbRGNbQ3Pq8L3zv2mItSipmJuiyh0rQlZ8EhtjUDAs24yMCUePu-Cob6EwQ0BBZQ8Vb3Bq9P4KpIzrK8-3uYmoiiRQxjZh--5Ip1A-4--oDGA1msKt-71oZOInGU3j9AFY1JluWcihSv4Suom0VvotvfJR99Z9aMzpOPU-Yqj3IH2BkAkVhpoFNL39LdPUvsjGQANPBn0ABO9Zpb41NP6EIVhoh7ksYicjgtWn1-efzayp2-vcvEAT29iA1gs6tj_NvkgET112QQs39fWV7n4kxhr5Ig_3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fmQFatm3rW5dmGB9InjGm8J2dC1Sn_TzM3lyPq7lwu3G0azk-YhZvbqbw9YRrmb7cmN87wMzyGkJH8ZsicdjfRmPqijAIfb3qrJzJprmZNTJ8AdCiuUF2CdgYQY-Myi73noQOGpCZkMlC9DJdB2maVP9wFsHxXCl1ipLmpOK1y9nemuTW8KucyqFfqXvWGxg85E_a_bcVaYCZeqjaM8WqBnBYIDN53NVBupM_zFIE1rN-qkycf856Sv0mIKEPBEjkFAvORSdbUIW4RJfbUKQQ0xNYzsAMUQe-ET8ZOMKFIvOBDwd7elRjXL93CyX_wMJ3597c3lFt8UA4F-_FPtYkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ndsHOCsMDeLB1HeN7y68yqoaREYoQVnjAEyYeMnw9M1LJzhshOYSif9iXv2WLW5zE-fnZmb19iereM1Lc_bJklD1k1qjT4Z9Wk6J3tkDJlsUKP2a8qhQ44KSqJ6JNaPC1_rZUNu_fDbyNkRfJYufOmZgBjDWmZtXSfVZwXhHO7dTdRiPx66xG13zlOaJmvabgaysn-e_2-PDonouuYcipMBqbpoEQAHLQAm43pB2fPnh1hcTc0AL1Zj0Q2t78e-QNu24NmCXgbek5Cv6wE1rQ2pRQ3JqHjCE5LqDcKqcfY5XzfJgZKWp7lZqdqBZh6ichI3NGisCN1E0ogglSmhdyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mJUh0Q48q5DeCoh6fJjN-Avvpv5WzoP5sxBtHuqSWzJscnCo14QtVyn9ciLWxxbnt3aEXd1mjSUMmZsoDHtyIi89jzwyDyLxFKTwuGDZpE09ktWjv8Qi9xvZP7zhxUROEKBkl4rov5OzBtkkxm2OxpI8UwJGspy3VsK59nVTFt_vvTrqPl1k4Bs2hdbHXUDnYrdW2BGr4VwejXiQX9T1r-9fZJQ_xpaBBMM1w2whb07OslqBhCzkkppKBn311HP2zv0mTRCkBZW73EFD_Fzho2LpCbGWN5Jt8_si3mnujUX_lvJlaZkf-UVQ-3PZnAhjnHBCbhbhd1dNhmwZ0LYwRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حب‌الخامنه‌ای یجمعنا
🔹
تشییع پیکر مطهر رهبر شهید انقلاب از قاب عکاس اعزامی فارس به کربلا
عکس:
محمد آهنگر
@Farsna</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farsna/448605" target="_blank">📅 07:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448604">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb6c8a542d.mp4?token=m4bz2gN0ky9A5QUmci646u5fR0WUGQwJDEJxNayKdLWfO1E4LsfASYrpSPLANkS_56n-KWwSUIbC4Nsm3CeeBtUKVjoJw1L_ecfwlDpJqQmPCnVvlZQSbrqauZxlxfyCAWz0FBoYQzSsfESETzjLAFXeVfZ0-E3JxPInG47OkaMKFfsgSAFB7EtIwgdhBFd29BK4Pp1D9o8TN0JXDYcAjGlhki4chYVRjb7HxP657vYokq2bmLVfkfoZ5LACK6ws7gE8jAKg99ful7dYZyEd4fVOzfrj_u6r6_Yn5L6XxyeqXXsqFteKdlUQ3Wet2CRB0xf1RZLoTLbGkoKi-SFHAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb6c8a542d.mp4?token=m4bz2gN0ky9A5QUmci646u5fR0WUGQwJDEJxNayKdLWfO1E4LsfASYrpSPLANkS_56n-KWwSUIbC4Nsm3CeeBtUKVjoJw1L_ecfwlDpJqQmPCnVvlZQSbrqauZxlxfyCAWz0FBoYQzSsfESETzjLAFXeVfZ0-E3JxPInG47OkaMKFfsgSAFB7EtIwgdhBFd29BK4Pp1D9o8TN0JXDYcAjGlhki4chYVRjb7HxP657vYokq2bmLVfkfoZ5LACK6ws7gE8jAKg99ful7dYZyEd4fVOzfrj_u6r6_Yn5L6XxyeqXXsqFteKdlUQ3Wet2CRB0xf1RZLoTLbGkoKi-SFHAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طواف پیکر مطهر رهبر شهید بر ضریح حضرت عباس(ع)  @Farsna</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/448604" target="_blank">📅 07:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448603">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d31c105779.mp4?token=uTR-myjhuLFs23NY61GM7OqdS9Fc7WTFSxUY4BObDFg1GFdJ96aBr2i6y8Y7xkFB4k7gqa4Ru4LACPUD75JQmwVmzzxBrHnsbxp4fb4PSAh4XZ2T2VcVBotN6rAtkqHbPcSlY6BUuFu_wMedbB2mYl1V2VBwjaAjfL1ljtf8U9mE3gPsTyHz98f1qYAxT-s6-kETlda_Vs3MLGixxH5zps5N4P6HqCYHjUM4GjKT_SNulDSBho7vq2n1yGApuXSC_nYhm13cHvAqibyCl0hHJbLaWa9nqQpTX_3Nl51F66ShWqtScYWN67iqtXe5FWFJcKV_afFBdG8e9f6v2Y5zGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d31c105779.mp4?token=uTR-myjhuLFs23NY61GM7OqdS9Fc7WTFSxUY4BObDFg1GFdJ96aBr2i6y8Y7xkFB4k7gqa4Ru4LACPUD75JQmwVmzzxBrHnsbxp4fb4PSAh4XZ2T2VcVBotN6rAtkqHbPcSlY6BUuFu_wMedbB2mYl1V2VBwjaAjfL1ljtf8U9mE3gPsTyHz98f1qYAxT-s6-kETlda_Vs3MLGixxH5zps5N4P6HqCYHjUM4GjKT_SNulDSBho7vq2n1yGApuXSC_nYhm13cHvAqibyCl0hHJbLaWa9nqQpTX_3Nl51F66ShWqtScYWN67iqtXe5FWFJcKV_afFBdG8e9f6v2Y5zGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هم‌اکنون، فرودگاه نجف؛ پیکر رهبر شهید انقلاب راهی زیارت آخر امام هشتم می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/448603" target="_blank">📅 07:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448602">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/510637ca54.mp4?token=JInSipXSP2hP3NwZ_rMr-C0QvPZjGnT9OwxvubGDyVsfZdLoLg96APWBUbXVmMOOMPh1qeY0kRDDVSeY9Twq7tYyM0ALq_ZSn3wJN7KjdPFiCQUs4FPltj3y15DZx-qmFGC8KM9aZrf7pmzR4vIp5dvxil21cCnR25MOhc5mJF_4t2d1Rb5QyaoZQM0ePYLxga9arPP55n-0srOmQJHFJHZx2KeMIZXIU-gsPA43cmdZuXI6q499r1fT5WNtHgCuBFYsLNm9rPbZiv0Vma4_yxKTLaXbSk9sP3GEzvjci8IUrr3MoLOMeoeiEG4VPoeKtdTTHUIR629fmRFZcjLH1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/510637ca54.mp4?token=JInSipXSP2hP3NwZ_rMr-C0QvPZjGnT9OwxvubGDyVsfZdLoLg96APWBUbXVmMOOMPh1qeY0kRDDVSeY9Twq7tYyM0ALq_ZSn3wJN7KjdPFiCQUs4FPltj3y15DZx-qmFGC8KM9aZrf7pmzR4vIp5dvxil21cCnR25MOhc5mJF_4t2d1Rb5QyaoZQM0ePYLxga9arPP55n-0srOmQJHFJHZx2KeMIZXIU-gsPA43cmdZuXI6q499r1fT5WNtHgCuBFYsLNm9rPbZiv0Vma4_yxKTLaXbSk9sP3GEzvjci8IUrr3MoLOMeoeiEG4VPoeKtdTTHUIR629fmRFZcjLH1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سنتکام مدعی پایان حملات به ایران شد
🔹
فرماندهی مرکزی ارتش آمریکا بامداد امروز با انتشار ویدئویی از هدف قرار دادن مواضعی در خاک ایران، مدعی پایان دور جدید حملات به ایران شد.
🔹
در این بیانیه در توجیه این تعرض این‌گونه ادعا شده است «نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در تاریخ ۸ ژوئیه دور جدیدی از حملات را علیه ایران تکمیل کردند تا توانایی ایران برای حمله به کشتیرانی تجاری و دریانوردان غیرنظامی بی‌گناه در تنگه هرمز را هرچه بیشتر تضعیف کنند.»
🔹
سنتکام در خصوص اهدافی که مورد تعرض قرار داده، ادامه داد «نیروهای آمریکایی به حدود ۹۰ هدف نظامی ایران، از جمله سامانه‌های پدافند هوایی، دارایی‌های دیده‌بانی ساحلی، سایت‌های ذخیره‌سازی موشک و پهپاد، توانمندی‌های دریایی و زیرساخت‌های لجستیک نظامی در امتداد خط ساحلی ایران حمله کردند.»
🔸
سپاه پاسداران انقلاب اسلامی اعلام کرد که بامداد امروز، زیرساخت‌ها و تاسیسات مهم پایگاه‌های آمریکایی در کویت و بحرین را مورد اصابت قرار داده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/448602" target="_blank">📅 07:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448601">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">چند مجروح در حملۀ آمریکا به اطراف اهواز
🔹
معاون امنیتی و انتظامی استاندار خوزستان: آمریکا صبح امروز در جریان حمله به استان خوزستان یک نقطه را در اطراف اهواز هدف قرار داد.
🔹
متأسفانه در جریان این اصابت، تعدادی مجروح شده‌اند که اقدامات درمانی و امدادی برای آن‌ها…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/448601" target="_blank">📅 07:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448592">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IMEfUHqipW-wDWz2V5ufd0Km_ONR6HQ6mim5AB6jjdDTm9FjuTChpuekJzH367KzC5tVAgmiWriVHdx_hSaFqM8-RbKVGWZJj1N_b8KfcLQ6geWtyFEVjKjEzT9UFHoOfxaFxBmCJZ0U121IsQxAPdjem5TPAW7k-5cknoY-YqNGIqJJnwmdBx5sIRueGgdgmOeozc9nPCg2V_dcBItCvU_k0Oi2ylupyJy4CqVXK2K5l6wKb20WBC97e-oeY2v5damIy63feWwXPgM6owUrda6cKFqBAowYjl-D-ZHFs3kgbadvwq5RSmRhA9JqiNDhgbvCNt7Zs7Cbvp8KzYa97A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gpyVP3ie_-OTKq5TU3r7-tsFBFL9mjE9f7BoJTM0ftSIR93LFdbp6UoBDlXRZ4LH7I92zwNjg1DV6ZnxgDJllqxEnABVpLhPPb-5gHDzDVQm8TA5GTevyu2_Va3i9YQMENwx3ZHAihAaNagjD58lN53sA2NsbxXRbpVV-inBkDonIXjy8GrDF3bFU0YDRgN7ex6TyG2l-DrhoFw6SKjr26Ug1uULW5plKKzcRsf1rtMqdcxxAQ4KvntA8Kbh6o7Tp2NCtqHWU66lsKP0wm3SejPLrQFY1LDGsIu0IxLcyf5tGBbareD5n87jq9knfTZ6VZU7i5gNDRz9ivU3zV5Big.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oOz316KBb-RYzlTdqfShNofIxc5fPh5uALmLwJY048-Ev44KgnYfBCqxDd_NLuzcuKbsCmoMFbVPy7NRDicTLhabB4QWcM-3ugwvQxMKsxkcSZeK8LFacXkEMVCnqzy6-79UUzSedk6ywMFJc5dbvJ-JmdV3ryA8dIIfcX_FGqBmnBrACkiRovbjkZJ-Kg48LDeU7K1kVnyBnmKR3cwR4d95BxvtmAJWGyDMfeVpxrks9Nex3gnBwemAWThm0ZhA_nOZ_FGx5KRXuL2ahnrE0GEFn3aL86qGCZZzY6yEXEjaz7JM03lBFe_jKSfx6bgncuiHR6vYLwOHox6GmB_XFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H6666qytkJf8oZZba9vrqHtPR0K4Wj0MHL7nFmgVP_qz-oJsLYINphtMzs8gEU_euulOBevGTNQkO1EvZNvRPNollqvp3xfUt_6g6npuKQjzXWw-nrqqHX3mW5qW2XVTpodfW9L_7esV7S86_2Vk-kpVVj4bd39UorQAe5ZB5sCJCCes4vUpqvDVtjxJ77gQyEDTjdQbMXGVSowIDuBiW6wf0wzeVBvyQSuA7Tuo5sPzFWZzRC0UDrnQcBZUZhBo1OCNBKXVAZ-9kpImst7Rsl4tJkyVX8m4lT7gvxeDQUt8RIfOcCwPwrj_k22RlhsxiN-MP4CyESd5MclPr7k50Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NJb32UXkrYKb1tcHMyhn01aRVDRuGOwKlQsZ2f088IOcBVynz3HxePb4JfPfOWFpYo7qEDVbLkwA4ALGcI17VQfp01qtUNu-TXmSUrUenDcj4u2QGt6kJZrisNWvm8nKWsS5OAPVobxsCJrazZn505JAjQlNHXDjii6lhMucI66MxV-i7eC7BQZPnoE_uEIJR-do5feJr8q1HKdRUtqre642Cwl5XdHQZ1Zjlc5heiaUOUKpR3INmLSRuZ0tNjhl76VzXimuKdQyQ6gmB4W1QVT6U4_pCbPSldA58bubsaw15uaZQAmD03G1AsDR5EWnWyFWlzzMsaz88_Gc-RvGWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rorzHcE5VjEtZahDOntT6XbJYY520hXrYX4Q9ml4VoRPg5jR47DJx7MJgJxlXHe_Wcni5H87oR1gnX7CSXk8TSJ3-v98TsCkMssDXj4upCp0aTp4etzlXaRKL9K4okuikSY_1mNcYvhfIyc9MoA5iGm6h7SN5NQBcbDdWdj1AvsSlsrkeAWho08J9O3CzEtr-VzQuu9tzlr84e6I6PllxLfnL1DYg9uLpEm84g1mVpX5ubzSbOXVmJbUrb9kP-IGy4qhtMEFfS2IUQulaM3gKaXGUw5OxNu-A05UYu9mGMcVWLYN3lRM-vPM_XZzim9RCHmP4c20SKxXCKrb8C9V6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CCORDkoFZMuhgaymmHMPIwmToYKEsFiKTscIxLJMY_WeUNhae4o3yMUNRAWgG0rERx9nRqWeqOC9VqDFVzHE5kgHI68ozE1qs1oIN2nU3dS-6NjcaeaZ8vGL_BX4pgiE_i4Q9KPW_tkrhMXUypcqAAY-DGX1c5RA7jxmJQWj-lqQhmlPT1OmksJa1kYchpbltA5i8FmCABS38oOHYqY95Ue3Dbuaw9CjrwwzopPAR9S8zCCxb3IA9C-3JBxXAQxoJc3SE9UEwYHB4_KyccZJ6bVJwqrsFe9cr0ypMAqMX6OsqbGETGYpNxNSs5S7buYIpsrbUaGXkurVYFD5RLcuMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T_Pgs_TRrLaP9nTfYjnm-m7ftFCG-LAh3ne6qsT2YbWoV-yY6fvtR4PrsVcpxbDM9J8Wj18MCXw8v5gzl2PCscYPEFXT_uZkcEMBVUp_BkbnXAhqZEsTeDcwHpX-1WB59qjdPaZGdT1zQiY4KoQ296UcWL2J0dmLvBZZO3issoUDFcx3KAoHLtzuCZv1ujJjxz4rdXdLQ6khaCPc2lomVgOTdDSHSpg1P7lilTba41KuDw7fAQ_tvvrn7Uic_Upg6h9uwmnWu_ovXs7SN45LRUMu2fbExT4Dg56nzNtUcvClfKL61-t8z0hNzhKfNFETRS5SKspLoxL9OE3r2F2ZhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vHQ9K_jabHfcnSomtpTEZUxZzdirQwtfOXBwfl72XCrXkEVmypyD6FsVAT53FKtp3F85UwSplZXfxds4lvm9_8hxg5BqSa4znaAETbYd7dOveUt2y3UArn8a03iSV4l50SfTxUX1s-PEYsw-L8_MXxRNdwpS6Nm8-5MBbO2t7RuJmmCn_p3NeD3eoBskLv8SiGkfOXly64flC4HZZi8eYLPm8WHHrgmV5eFwCcXrUjnFRiuF73LwxMR948qKbxOIW0PZD9lthmPiuQHgSzCHDcmv4JVyy-hfCxDfLtonhHrq5OOJwrUmY0wmCbjPG04orcEsiOIUlMrKr1_qmrNGSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
زائران امام رضا(ع)، در انتظار آقای شهید ایران
عکس:
حسین توحیدی‌فرد
@Farsna</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/448592" target="_blank">📅 07:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448591">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">چند مجروح در حملۀ آمریکا به اطراف اهواز
🔹
معاون امنیتی و انتظامی استاندار خوزستان: آمریکا صبح امروز در جریان حمله به استان خوزستان یک نقطه را در اطراف اهواز هدف قرار داد.
🔹
متأسفانه در جریان این اصابت، تعدادی مجروح شده‌اند که اقدامات درمانی و امدادی برای آن‌ها آغاز شده است.
🔹
ابعاد دقیق این حادثه و میزان خسارات در دست بررسی است و اخبار تکمیلی و جزئیات بیشتر متعاقباً به اطلاع عموم خواهد رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/448591" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448590">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fb8c0537e.mp4?token=MwrYU97wQ_UeNK_sK1gENgSYw1BfWdl5gn7nKmcJNRiP9iU_IKV5F8qju1GqN9Pe7XxXh1rOO0NWCMilLNljBN-MZWbdhEl38Rqoqa6O9bWYB978mol_Qd1p1Sc-R49q-m6om1OyhJKyHdLZr473GaLw1EfWkmgsniPx7RLmw92h3SrrgdMh1Sv6Nj1hxWGGqRNKVyI4wWl3y6iQJyjR6cS8RkKIUuzq-Q0tpbAFmT3-ScdiHh4WLYKRJ_5ilnaPBuvrWIHDxeDLag1ELOaXSin3owH4XnZNfX-dyWH8dCzI6WvYioX8fMbxyQfWKhWrKlR_8T_Z9WvO-o7kJEpOQDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fb8c0537e.mp4?token=MwrYU97wQ_UeNK_sK1gENgSYw1BfWdl5gn7nKmcJNRiP9iU_IKV5F8qju1GqN9Pe7XxXh1rOO0NWCMilLNljBN-MZWbdhEl38Rqoqa6O9bWYB978mol_Qd1p1Sc-R49q-m6om1OyhJKyHdLZr473GaLw1EfWkmgsniPx7RLmw92h3SrrgdMh1Sv6Nj1hxWGGqRNKVyI4wWl3y6iQJyjR6cS8RkKIUuzq-Q0tpbAFmT3-ScdiHh4WLYKRJ_5ilnaPBuvrWIHDxeDLag1ELOaXSin3owH4XnZNfX-dyWH8dCzI6WvYioX8fMbxyQfWKhWrKlR_8T_Z9WvO-o7kJEpOQDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مشهد در انتظار آقای شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/448590" target="_blank">📅 07:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448589">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سپاه: زیرساخت‌ها و تاسیسات مهم پایگاه‌های آمریکایی در کویت و بحرین مورد اصابت قرار گرفتند
🔹
سپاه پاسداران: ملت شریف ایران، ملت کریم و مجاهد عراق؛ آفرین بر شما مردمان مومن و بصیر و وفادار که با موقع شناسی و تشییع بی‌نظیر در تاریخ جهان قدر و منزلت ولایت الهی و عشق عمیق متقابل مردم و والی اسلامی با مرام امیرالمومنین (ع) را به رخ جهان کشاندید و با شعارهایتان یادآور شدید که هزینه تعدی به مرجعیت و ولایت فقیه مسلمانان بسیار سنگین خواهد بود.
🔹
هرچند این تشییع باشکوه به ویژه ۲۳ ساعت تشییع عاشقانه در گرمای شدید، سرزمین عراق حبیب، مستکبران کاخ نشین را وحشت زده و آنها را به واکنش عجولانه به این قدرت نمایی مردم واداشت و آمریکای عهد شکن با زیر پا گذاشتن همه تعهدات بار دیگر نقاط متعددی از استان‌های ساحلی جنوب ایران و در اقدامی ضد مردمی دو پل در استان‌های شرقی به سوی مشهد مقدس را مورد تجاوز قرار داد تا اخبار این حماسه بی‌نظیر را تحت شعاع قرار دهد و این رویداد الهام بخش را از نظر مردم جهان پنهان دارد، غافل از اینکه این جنایات مردم جهان را بیدارتر و آنها را برای نقش آفرینی در مبارزه‌ با شیطان بزرگ مصمم‌تر خواهد کرد.
🔹
رزمندگان اسلام تجاوزهای ارتش کودک‌کش آمریکا را بی پاسخ نخواهند گذاشت.
🔹
در اولین مرحله از پاسخ تنبیهی علیه پیمان شکنان آمریکایی، رزمندگان نیروهای دریایی و هوافضای سپاه طی عملیات مشترک موشکی و پهپادی، ساعتی پس از حملات دشمن و نقاط مختلف کشور، زیرساخت‌ها و تاسیسات مهم دو پایگاه‌های استعماری اشغالگران آمریکایی در عریفجان و علی السالم کویت و جفیر و شیخ عیسی در بحرین را در هم کوبیدند.
🔹
سپاه پاسداران انقلاب اسلامی به ارتش کودک‌کش آمریکا اخطار می‌کند که در صورت تکرار تجاوز پاسخ‌های کوبنده ما به سایر پایگاه‌های آمریکایی در منطقه توسعه خواهد یافت.
@Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/448589" target="_blank">📅 06:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448587">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c672f18d3.mp4?token=pdRdHGfhOWTmM2n2AK7sxiH-yBD7UFFkGK5wUo962ie0GdQodjmtVsOgdb3MFP-KdCHUIBN08jEA8XcuXiLv4upS_Sxi0Kpd_Q6pW6WiEki2Zq0MElR9oQZ52WuLutxdL1Ud35jdQ4VBlG79BdKQfe6YIVTB4CpC_voblGZvqaRRA2kTlXkF82uUEb_6lnUWFQpxvwivZPbDHSyoFhVySjZFaWbCGOi32KeNJtV1fQrTwgZcOfc-0-AvW1xp2qKQVBOh97zVpVN_I1er76SOCcwJn-nfEB6AEm3vqgF6QVZJAQU6H4vLSt6Ftc0gTiEWi6hkGbfv6Z63trYnMnWYXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c672f18d3.mp4?token=pdRdHGfhOWTmM2n2AK7sxiH-yBD7UFFkGK5wUo962ie0GdQodjmtVsOgdb3MFP-KdCHUIBN08jEA8XcuXiLv4upS_Sxi0Kpd_Q6pW6WiEki2Zq0MElR9oQZ52WuLutxdL1Ud35jdQ4VBlG79BdKQfe6YIVTB4CpC_voblGZvqaRRA2kTlXkF82uUEb_6lnUWFQpxvwivZPbDHSyoFhVySjZFaWbCGOi32KeNJtV1fQrTwgZcOfc-0-AvW1xp2qKQVBOh97zVpVN_I1er76SOCcwJn-nfEB6AEm3vqgF6QVZJAQU6H4vLSt6Ftc0gTiEWi6hkGbfv6Z63trYnMnWYXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تکمیلی/
بارش موشک‌های ایرانی بر سر تروریست‌های آمریکایی در بحرین
@FarsNewsInt</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/448587" target="_blank">📅 05:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448586">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d6b93e28d.mp4?token=kQklqSP_Z9nWU4un638dI1Zy8CD0OXu87PktfdXmpsD12CkgjFOcq_O-k6FusshcqtFwgs-AhIaEcgkbKgyfBJ4dFS_Yl_-KTQXiAPcon-ALE02eBEmjot3LA1kjDbfZdfapDw-5aaSUNFidaVt_JtXpfh-kuljYvz3v0T5V2IPtAaBWfAt4LJNstX91zHPnG4i7KyNWXV9eFViCUaIe2T0VrdLHHHpJbAMuxpRFyip-ITonFqrcnHAD5An9plo2qmSA_44Fkq4XJiQw1D-SX5Z3sqPyRjIGfN08_0XUfEDfyF70HCqpY6qbEXI0BGIb1C7817iun0vocrcmy9VHDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d6b93e28d.mp4?token=kQklqSP_Z9nWU4un638dI1Zy8CD0OXu87PktfdXmpsD12CkgjFOcq_O-k6FusshcqtFwgs-AhIaEcgkbKgyfBJ4dFS_Yl_-KTQXiAPcon-ALE02eBEmjot3LA1kjDbfZdfapDw-5aaSUNFidaVt_JtXpfh-kuljYvz3v0T5V2IPtAaBWfAt4LJNstX91zHPnG4i7KyNWXV9eFViCUaIe2T0VrdLHHHpJbAMuxpRFyip-ITonFqrcnHAD5An9plo2qmSA_44Fkq4XJiQw1D-SX5Z3sqPyRjIGfN08_0XUfEDfyF70HCqpY6qbEXI0BGIb1C7817iun0vocrcmy9VHDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر مطهر رهبر شهید انقلاب از حرم حضرت عباس(ع) خارج شد
@Farsna</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/448586" target="_blank">📅 05:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448585">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
وقوع انفجارهای دوباره در بحرین
🔹
منابع خبری گزارش دادند که مقر ناوگان پنجم نیروی دریایی آمریکا در بحرین هدف اصابت حملۀ هوایی ایران قرار گرفته است.  @Farsna</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/448585" target="_blank">📅 05:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448584">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsGSYwm8TVdzRzPrXJsBE7cOg4n9HAHN1PnSVC-pawJ-zUr8AOPEeFHaXqq1cNPLeT4_aG8CURwAx2-4MK02UxO8_5RvCAlNEnfN20HibrvFc5OphaPnZSEF12gdR-O8VMoq2CcVh0fH0H86aTrk_wTv1ML2EMJKbBOXwvHTAM0KdQT6R19TlcfmJ7i6BkIRaGikf5K70FmbmM9kx6zKNOmNYKzirrST9KcSNYwb6p40amQ72WUZkziqvoQXdzhAVOFF4C2orVS94tUtN8Zr5nZ2MbBtKUKR_MY7r_EbEUw2lteFhqvE0DFLcmBbPvIbXY2qUm6RmcrJNgAkCWzQJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف خطاب به سران آمریکا: بزنید، می‌خورید؛ تنگهٔ هرمز فقط با «ترتیبات ایرانی» باز می‌شود نه با تهدیدات آمریکایی
.
🔹
آمریکا هنوز یاد نگرفته است که زورگویی و بدعهدی دیگر بی‌هزینه نیست. شفاف بگویم: بزنید، می‌خورید.
🔹
دست‌وپای بیهوده نزنید که بیشتر فرو خواهید رفت. تنگهٔ هرمز فقط با «ترتیبات ایرانی» باز خواهد شد نه با تهدیدات آمریکایی.
@Farsna</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/448584" target="_blank">📅 05:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448583">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f57edc40ec.mp4?token=qp3LeF0HPg2kLhTEU5v2zA0XZcj575o0FGaIqxprcVqUF2WBRFjnRXtMTVB4RCPNRa4XV3J5RiwEJDT4pKXEUHg1kqJWsPLt_BIfDpuB_aY12qABw3txSk_Bsg0quVdRfZrJYHZx_8SrUaswKd9Z5Sf3Xab2294Eq0X9O191W0787FpM4f8vPmdTVvxVxR9X92fWf52tUuNXEuGEqFTPd-dSpwag0Uu9POrEyxMzZu_DkExsAFW5PAQCxh8iqeJwF3iMvKQyCpOW-hM-li8Rp0vu2bTX0WdH7CJNePHbUm2RPO1leLKq0BpmSoNb5Bb17Utu7APXjDPUjeSqR_lDfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f57edc40ec.mp4?token=qp3LeF0HPg2kLhTEU5v2zA0XZcj575o0FGaIqxprcVqUF2WBRFjnRXtMTVB4RCPNRa4XV3J5RiwEJDT4pKXEUHg1kqJWsPLt_BIfDpuB_aY12qABw3txSk_Bsg0quVdRfZrJYHZx_8SrUaswKd9Z5Sf3Xab2294Eq0X9O191W0787FpM4f8vPmdTVvxVxR9X92fWf52tUuNXEuGEqFTPd-dSpwag0Uu9POrEyxMzZu_DkExsAFW5PAQCxh8iqeJwF3iMvKQyCpOW-hM-li8Rp0vu2bTX0WdH7CJNePHbUm2RPO1leLKq0BpmSoNb5Bb17Utu7APXjDPUjeSqR_lDfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طواف پیکر مطهر رهبر شهید بر ضریح حضرت عباس(ع)
@Farsna</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/448583" target="_blank">📅 05:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448582">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/363df94585.mp4?token=RKgvRcpJPNIxsrOcRhjAWCLP6vfQtAxQY9YV9NDiOj-IDmla0SWH-TzuJYijMu_5Sdn-g-7uKcawEI7-91ALHd_lunlLiY9iCrrOmtFV4uP76NTI0REsJACLfxluH_G6EQfdSd9EEz-33eHAtjHr2bwb7yGOaaUMrcxJvKmh4TmKFpcv-mRZuMMElGjSc6jGeTGx-RDs_9wo5ZEvQJVmCJqjxvE5pE7f5FuATDeUQ-PwrggGSTj4Rmshf3UO9DuGlojOJCEMklTdD1V8Ip6np0HelgAreixErGpvzDAvEm83VwiXw5Pc4Se2EfOgjgM4kwH4aQkEBOfWMh2HlJuh2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/363df94585.mp4?token=RKgvRcpJPNIxsrOcRhjAWCLP6vfQtAxQY9YV9NDiOj-IDmla0SWH-TzuJYijMu_5Sdn-g-7uKcawEI7-91ALHd_lunlLiY9iCrrOmtFV4uP76NTI0REsJACLfxluH_G6EQfdSd9EEz-33eHAtjHr2bwb7yGOaaUMrcxJvKmh4TmKFpcv-mRZuMMElGjSc6jGeTGx-RDs_9wo5ZEvQJVmCJqjxvE5pE7f5FuATDeUQ-PwrggGSTj4Rmshf3UO9DuGlojOJCEMklTdD1V8Ip6np0HelgAreixErGpvzDAvEm83VwiXw5Pc4Se2EfOgjgM4kwH4aQkEBOfWMh2HlJuh2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قابی متفاوت از مراسم بدرقه و گلباران پیکر رهبر شهید انقلاب، در جوار ضریح حضرت عباس علیه‌السلام
@Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/448582" target="_blank">📅 05:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448581">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f593534d88.mp4?token=kPH5g74jNpJn0XUuo38kv3zmdRoLqcdkSoNNrWeWK3ksTxjMeNOMtvaU1VjbEo5O0Y81h3kwukdbWyQgadpOEMWpUz-epW7Sldg_hLRJuPnKGPNP3IltsioD9hc7c-oXwrilePnm-35PfuIE7LDEtfbeltcUXb9lfxU0jzDs5G7b6mGEhuloHnOvHnwWBMKKNrqJ2FNrmMhZP--GWYVMXXp8pqqb6k4nA1kboi-PsktEDuPE6CRDOLdi_9D9SvpzbraGHyrVF9CJVFLuNAGlixVsUkX10oACwMHPojmPsCuV0rwLOK-CxE-stPXTy-XEocoTRS-CDnni02AW1CREE2yaXBbadPL7UiGB5_1Ymy9Xl0ZeARZLC87IFbbAK4BNL3VNnuVZNZDTpuEcSmBvDVm-jxorjYh0fXm2vpdrc31q59WCYchYMwrwnezFHbR_shnpKmmMcleWmF-1FpcNLOJJBNR2COAQMEbc8IyGkDPyJGvxDRdpnsj_DIji1Gko8DI-ZWyYrjvomKgaULYgCu06DR98Y7rdz-A3fVQMsVMRakRQTouV7DX1a5JKA1F1KEa3BRrXdKrS3BMDDN4vCzKlo9LrF0mErDJ3DQulReEE5cYHBzGmDpNrSXw0nmtRsfZ8U_-CU1O9vknk45_Rob-Rb4UUpysOmDea1XHRgng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f593534d88.mp4?token=kPH5g74jNpJn0XUuo38kv3zmdRoLqcdkSoNNrWeWK3ksTxjMeNOMtvaU1VjbEo5O0Y81h3kwukdbWyQgadpOEMWpUz-epW7Sldg_hLRJuPnKGPNP3IltsioD9hc7c-oXwrilePnm-35PfuIE7LDEtfbeltcUXb9lfxU0jzDs5G7b6mGEhuloHnOvHnwWBMKKNrqJ2FNrmMhZP--GWYVMXXp8pqqb6k4nA1kboi-PsktEDuPE6CRDOLdi_9D9SvpzbraGHyrVF9CJVFLuNAGlixVsUkX10oACwMHPojmPsCuV0rwLOK-CxE-stPXTy-XEocoTRS-CDnni02AW1CREE2yaXBbadPL7UiGB5_1Ymy9Xl0ZeARZLC87IFbbAK4BNL3VNnuVZNZDTpuEcSmBvDVm-jxorjYh0fXm2vpdrc31q59WCYchYMwrwnezFHbR_shnpKmmMcleWmF-1FpcNLOJJBNR2COAQMEbc8IyGkDPyJGvxDRdpnsj_DIji1Gko8DI-ZWyYrjvomKgaULYgCu06DR98Y7rdz-A3fVQMsVMRakRQTouV7DX1a5JKA1F1KEa3BRrXdKrS3BMDDN4vCzKlo9LrF0mErDJ3DQulReEE5cYHBzGmDpNrSXw0nmtRsfZ8U_-CU1O9vknk45_Rob-Rb4UUpysOmDea1XHRgng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر رهبر شهید انقلاب پس از اقامه نماز بر دستان عزاداران عراقی وارد روضه منورۀ ضریح حضرت عباس علیه‌السلام شد.  @Farsna</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/448581" target="_blank">📅 04:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448580">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a188a7226.mp4?token=cXioVXLxvePfmR_q_lOkXVz9vLvsfFsMzp9YzLOz8Ku4BrdIjzrbRJ4-GlmTTswxzDy6N13QS-JKDshYqejyLs1fMCu60jPMiL_rjMM8cSxCDHN09PHAvNa2Mt-arn-TSY-A3-CIx_NvgV-V8ha-mobMn_JHxHS4s9PXYh64-9ZyHFCBx1pk8ieY368UbMgWKz1YFsKz6B6JwcMprgmSHKrtgGp7akp-2ILVwYxy7qkbZQi6Y4wotU4iqK-ozo0U8VyGW4qyNVMp3PlxvUu2_MKIC_DyovQRDN8lSKX9FBZMAFjLVjz58ODEQV7oVmd8xsbJz1MBw0vibyN9JT6J13Tb1x3e53eVsscEUYdYNOIOS49_ZXNJu5MHhlnRqgzYRl08GbRZsFQOB9n0LNlMHxksHBBK3no7QQgQTJPOmQ5yn1AhE1eN2MEUycplrP6xus_uRAkUxaAwl2czeyGYa_mAOqOdyTw4buzzzRlKM6P5AtmstspA-Uwp4xWtmQyOjWd83GLOjvJf-93ERU4vXzFkWW5Sx5dq1BSjgljhfzskrMb2h51utpGqz4peR6A_4eLEQE8V-AkhfjjMPBk_kMUptMh3qnGu2eCJEp4KYJam9j9caMRVP6H2AJFaSBgegBMDf3W3ur5rZ9Be_jAg1EY4Yk1feKftp_CQJTETarI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a188a7226.mp4?token=cXioVXLxvePfmR_q_lOkXVz9vLvsfFsMzp9YzLOz8Ku4BrdIjzrbRJ4-GlmTTswxzDy6N13QS-JKDshYqejyLs1fMCu60jPMiL_rjMM8cSxCDHN09PHAvNa2Mt-arn-TSY-A3-CIx_NvgV-V8ha-mobMn_JHxHS4s9PXYh64-9ZyHFCBx1pk8ieY368UbMgWKz1YFsKz6B6JwcMprgmSHKrtgGp7akp-2ILVwYxy7qkbZQi6Y4wotU4iqK-ozo0U8VyGW4qyNVMp3PlxvUu2_MKIC_DyovQRDN8lSKX9FBZMAFjLVjz58ODEQV7oVmd8xsbJz1MBw0vibyN9JT6J13Tb1x3e53eVsscEUYdYNOIOS49_ZXNJu5MHhlnRqgzYRl08GbRZsFQOB9n0LNlMHxksHBBK3no7QQgQTJPOmQ5yn1AhE1eN2MEUycplrP6xus_uRAkUxaAwl2czeyGYa_mAOqOdyTw4buzzzRlKM6P5AtmstspA-Uwp4xWtmQyOjWd83GLOjvJf-93ERU4vXzFkWW5Sx5dq1BSjgljhfzskrMb2h51utpGqz4peR6A_4eLEQE8V-AkhfjjMPBk_kMUptMh3qnGu2eCJEp4KYJam9j9caMRVP6H2AJFaSBgegBMDf3W3ur5rZ9Be_jAg1EY4Yk1feKftp_CQJTETarI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر رهبر شهید انقلاب وارد حرم حضرت عباس(ع) شد. @Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/448580" target="_blank">📅 04:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448579">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/020d9e9fdd.mp4?token=UesY7dQcPLIuYb_Dp7OxhBUwm7HuWRxZfSczcgGUJqAxPTkdvd0ossmj8a0Zk9c7Is7wGqzrCyW0mkhZ-ZwWqCHMoJdknmznOuw5yktW3f4NF_t7UnB2ji1O__I_oQKz88o44M2Xmi3J-y5qDzOEhzzUdBNa1ZpbUL3Wsk3lBw_3WwqUcm30OIzcstImrAQA14pNcMJo-KZRfP14qLT2D8JkJJu5E5WRHaYzqc6Z11NoK-vK_pG2cRPDsRtcBGWVN0O2-jRgC8-QD2KyVp_fwKyIVz2pi3RNs0ph-dsqqJZSvDSXXcTWT1O92j7LjziTG9BnuoXWd3yPgRuIUtMq7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/020d9e9fdd.mp4?token=UesY7dQcPLIuYb_Dp7OxhBUwm7HuWRxZfSczcgGUJqAxPTkdvd0ossmj8a0Zk9c7Is7wGqzrCyW0mkhZ-ZwWqCHMoJdknmznOuw5yktW3f4NF_t7UnB2ji1O__I_oQKz88o44M2Xmi3J-y5qDzOEhzzUdBNa1ZpbUL3Wsk3lBw_3WwqUcm30OIzcstImrAQA14pNcMJo-KZRfP14qLT2D8JkJJu5E5WRHaYzqc6Z11NoK-vK_pG2cRPDsRtcBGWVN0O2-jRgC8-QD2KyVp_fwKyIVz2pi3RNs0ph-dsqqJZSvDSXXcTWT1O92j7LjziTG9BnuoXWd3yPgRuIUtMq7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تصاویر منتسب به اصابت مستقیم موشک ایرانی به مقر ناوگان پنجم نیروی دریایی آمریکا در بحرین
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/448579" target="_blank">📅 04:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448578">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‌
🔴
منابع خبری عربی از اصابت موشک‌های ایرانی به یک پایگاه آمریکایی در کویت، و ناتوانی سامانه‌های پدافند هوایی این کشور خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/448578" target="_blank">📅 04:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448577">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03a2cc3c78.mp4?token=H3n0XtVd5U91ORNa3IUzen9EKFlgwd3fUjfL5yKPM-eQ2dqdwMbCb0i7AiqcIc1Lb86sESvJg8wnfN4t2bgxYCJLfDkekMmQQspcPIHEhCkW36I194Mrn2emd7iPVds_NQXmB7bt17cQJDZQZ8Ezm1Op2O8Mxp5NPDF0y_2WozcTsSzrFJEtLTu7vp1Ha_sanlsI78EYmP2hsMgMVDPGG0OQtPDwuLg-AKFnGQ4MYboNE-f0hyF8eKecL7Y39Uw75SJBWS6Tx6ASwbLsmrdxnic2D0KWbq2oP-2Gr4UfvPwT89fRil-EOy7qrOuBLK-EPKO91Pp77E7gKyKsGve2XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03a2cc3c78.mp4?token=H3n0XtVd5U91ORNa3IUzen9EKFlgwd3fUjfL5yKPM-eQ2dqdwMbCb0i7AiqcIc1Lb86sESvJg8wnfN4t2bgxYCJLfDkekMmQQspcPIHEhCkW36I194Mrn2emd7iPVds_NQXmB7bt17cQJDZQZ8Ezm1Op2O8Mxp5NPDF0y_2WozcTsSzrFJEtLTu7vp1Ha_sanlsI78EYmP2hsMgMVDPGG0OQtPDwuLg-AKFnGQ4MYboNE-f0hyF8eKecL7Y39Uw75SJBWS6Tx6ASwbLsmrdxnic2D0KWbq2oP-2Gr4UfvPwT89fRil-EOy7qrOuBLK-EPKO91Pp77E7gKyKsGve2XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر رهبر شهید انقلاب وارد حرم حضرت عباس(ع) شد.
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/448577" target="_blank">📅 04:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448576">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
صابرین‌نیوز: موشک‌های ایرانی، پایگاه الازرق در شرق اردن را هدف قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/448576" target="_blank">📅 04:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448575">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/934748e258.mp4?token=TUmwADwwq5X8m-yS-jsJbml7-NrkqaQ4GP9AywiQjzYScpE8a-bQ6z18LEDtEjZ7kVXMV9Li9XskN_HE4jgzXTy2G-wso8-Xgk9br-wX6Wkf1Gkt3f3tBujrWIgAFtGqFDTqINuHIvGF-62whtKMTVdziOvY2T41hj1KPBUdQhEsUcOqOmFGbFV-_4kpbxLuVT-rMSeFJ3px633LLSF-EPT39MS4t8868GI5x0LJ-e8X9dLZ3OMLOAy83qnPA2jWpfiB7JqUevGfllRDwbDhTNTM-K-pptCy9hizluoGv0cSqFbWL11sweQga_F2yjuZkQs0pWhuzIJdOiNgId9Jswzhp_aZMI5CIJ9LRcjOzramKSwkHc-eYmW_hMvNO1jZX7TGPzgW9-cF4Rtd9vN85YtnXtoVipwsS5JetbP20BuS0OObJg4Hpg9ZlROSgW1leUvkOV9JjAltRpqC6fRpPgQT_aRG9y3FEmSOAaVNtRIc5EwNGPkWkLSqnRcw0Iyjpi5_gXm40Td1vwnp7O7QbrWM5f7fr2Q32aoeq9AHDh7u7v0O_pMt2-VA4BUYx_s9Slgc5d4z_u8m0bSi5H88G3VLyXwk9JUjlohfkrJz82jXHMbZ2_xQhvxzz4gsF6Gq57lOKemL61cFM87fWDIkc_tktQWXf974ekV-mbhjcyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/934748e258.mp4?token=TUmwADwwq5X8m-yS-jsJbml7-NrkqaQ4GP9AywiQjzYScpE8a-bQ6z18LEDtEjZ7kVXMV9Li9XskN_HE4jgzXTy2G-wso8-Xgk9br-wX6Wkf1Gkt3f3tBujrWIgAFtGqFDTqINuHIvGF-62whtKMTVdziOvY2T41hj1KPBUdQhEsUcOqOmFGbFV-_4kpbxLuVT-rMSeFJ3px633LLSF-EPT39MS4t8868GI5x0LJ-e8X9dLZ3OMLOAy83qnPA2jWpfiB7JqUevGfllRDwbDhTNTM-K-pptCy9hizluoGv0cSqFbWL11sweQga_F2yjuZkQs0pWhuzIJdOiNgId9Jswzhp_aZMI5CIJ9LRcjOzramKSwkHc-eYmW_hMvNO1jZX7TGPzgW9-cF4Rtd9vN85YtnXtoVipwsS5JetbP20BuS0OObJg4Hpg9ZlROSgW1leUvkOV9JjAltRpqC6fRpPgQT_aRG9y3FEmSOAaVNtRIc5EwNGPkWkLSqnRcw0Iyjpi5_gXm40Td1vwnp7O7QbrWM5f7fr2Q32aoeq9AHDh7u7v0O_pMt2-VA4BUYx_s9Slgc5d4z_u8m0bSi5H88G3VLyXwk9JUjlohfkrJz82jXHMbZ2_xQhvxzz4gsF6Gq57lOKemL61cFM87fWDIkc_tktQWXf974ekV-mbhjcyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقامۀ نماز بر پیکر مطهر رهبر شهید انقلاب در حرم حضرت عباس(ع)
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/448575" target="_blank">📅 04:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448574">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‌
🔴
وقوع انفجارهای مهیب در کویت
🔹
صابرین‌نیوز: علاوه بر بحرین و قطر، پایگاه‌های نظامیان تروریست آمریکایی در کویت نیز هدف حملات هوایی ایران قرار گرفت. @Farsna - Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/448574" target="_blank">📅 04:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448573">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a2d1ebda.mp4?token=p9u6gT2bXLrlKT2g9wGE-6sSm1KmB488mTPpgibaKukfiUfOrgWu_3Id5rb3Klx-0EBdw2vazXi2_QlmiCs-dK4k1wmZ7fd7jFqTRRzyonz1N8v6iSj6HV47cFs7ZE08UBpzTUeCLjAjs1qb7JRuu7Li0jwYOAAmaIP31YTVN-MXVssYND0469rnS8uba_WkWEYw7zLy7D8x9v4GnUJkMvtI6cS6VEyGnyMeYTTx_fgmMfGFyIEeXE9UhfKO0TitOrGq3m6L0pCgFfoDOHJUWdsEoztJjWjPszK8_Ic7IA51sVJhJBTKMqgWTO3C14Nitiy3TDF_0JEDoj6leAKxDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a2d1ebda.mp4?token=p9u6gT2bXLrlKT2g9wGE-6sSm1KmB488mTPpgibaKukfiUfOrgWu_3Id5rb3Klx-0EBdw2vazXi2_QlmiCs-dK4k1wmZ7fd7jFqTRRzyonz1N8v6iSj6HV47cFs7ZE08UBpzTUeCLjAjs1qb7JRuu7Li0jwYOAAmaIP31YTVN-MXVssYND0469rnS8uba_WkWEYw7zLy7D8x9v4GnUJkMvtI6cS6VEyGnyMeYTTx_fgmMfGFyIEeXE9UhfKO0TitOrGq3m6L0pCgFfoDOHJUWdsEoztJjWjPszK8_Ic7IA51sVJhJBTKMqgWTO3C14Nitiy3TDF_0JEDoj6leAKxDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
فعال‌شدن آژیرهای هشدار در بحرین و قطر
🔹
منابع محلی از به‌صدا درآمدن آژیرهای حملۀ هوایی در بحرین و قطر، بعد از شلیک موشک‌های بالستیک از ایران خبر دادند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/448573" target="_blank">📅 04:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448572">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23460b6fc2.mp4?token=XhGI91ZQIUGhgctZZUkYq1lE5LYBYoxn1tp2jJ93emo243Qd7G5WnTKVGGYKqSJ1pG5bopFmxM9fO54mb9-4PqzWJfACFeBV7Jo38HOXBJovF_cbbN1sQBlXN5lF0R6vnWSoswMDNDQJlQC0MyS5rlQdW-SomdYBEtuaC_ZTFl7kIdKA0OFE8jGbzxmO9crt7S5R3le_JCBdD441dNqIFeCYIxr4m_ugPC7Eb134__cDnVTuJ3Q2zD_8av8Wy7gD4zUBhFjJ7OR3AFxjX6sIfIWTFdYhV8xOZjZuG6w1QT-42ruKcTLuGXA04fRTtm8SG5VlZjs0LfbeedDZOdDn-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23460b6fc2.mp4?token=XhGI91ZQIUGhgctZZUkYq1lE5LYBYoxn1tp2jJ93emo243Qd7G5WnTKVGGYKqSJ1pG5bopFmxM9fO54mb9-4PqzWJfACFeBV7Jo38HOXBJovF_cbbN1sQBlXN5lF0R6vnWSoswMDNDQJlQC0MyS5rlQdW-SomdYBEtuaC_ZTFl7kIdKA0OFE8jGbzxmO9crt7S5R3le_JCBdD441dNqIFeCYIxr4m_ugPC7Eb134__cDnVTuJ3Q2zD_8av8Wy7gD4zUBhFjJ7OR3AFxjX6sIfIWTFdYhV8xOZjZuG6w1QT-42ruKcTLuGXA04fRTtm8SG5VlZjs0LfbeedDZOdDn-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی باشکوه از وداع با پیکر امام شهید در حرم حضرت عباس(ع)
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/448572" target="_blank">📅 04:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448571">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‌
🔴
وقوع انفجارهای مهیب در کویت
🔹
صابرین‌نیوز: علاوه بر بحرین و قطر، پایگاه‌های نظامیان تروریست آمریکایی در کویت نیز هدف حملات هوایی ایران قرار گرفت. @Farsna - Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/448571" target="_blank">📅 04:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448570">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f456a0004.mp4?token=Zba3Zuz9_Y5UkILkKT3lwu1jcS3vUWfmEkv1zTmMmKy0RcpuYGzwr2DFjDc4b1uk4ErcKpIX0_ArDrhx1KXbg4z3PvfXsq1BBD_AaWAiE5OSCztfSyCP6D3UaJ34Gqi55wPDbs69oMgxy6J_m04Dd5o9qBdQQDuQ7BfHpMw8iQD4wk31NI4h8s3Qw5vy88UZb_TXc4gWQZF3Yasbb419xkmMjYuniG_YXHP6LLKqY9R5YOOZUU-xT971JuCK2kd605ZI2gpFS90vf0ipG3BwQSlMeQDPYsmoedol8NlEcudwBg8eAodKCvwf6N6MgAGLXatP-X-l3oae6j14d6CXMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f456a0004.mp4?token=Zba3Zuz9_Y5UkILkKT3lwu1jcS3vUWfmEkv1zTmMmKy0RcpuYGzwr2DFjDc4b1uk4ErcKpIX0_ArDrhx1KXbg4z3PvfXsq1BBD_AaWAiE5OSCztfSyCP6D3UaJ34Gqi55wPDbs69oMgxy6J_m04Dd5o9qBdQQDuQ7BfHpMw8iQD4wk31NI4h8s3Qw5vy88UZb_TXc4gWQZF3Yasbb419xkmMjYuniG_YXHP6LLKqY9R5YOOZUU-xT971JuCK2kd605ZI2gpFS90vf0ipG3BwQSlMeQDPYsmoedol8NlEcudwBg8eAodKCvwf6N6MgAGLXatP-X-l3oae6j14d6CXMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلاش سید احمد الصافی، تولیت آستان حضرت عباس برای رسیدن به نزدیکی پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/448570" target="_blank">📅 04:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448569">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJAc9-jKwb3Qq32Lr5t-IAifkPBcPSQONl6EOJvNpnQ57KaHeTPf0957bUmhxfaCST4_VGJNcgxRB_xjXLSWw0HP9DiIBWDrwlfFWQ43qEkqRVDAglF0W8ByuueoBLdQ7acb-L0wgWgihKpQrx5E8-X2u3NTSCyAfn_m38zSNTnzhNMyr-7ypd7jttg-CL9XpcGlC4ZM6Iv3-uWaBRV1gDqSwi4F38KRp15ozZoQhvq7QFtkVZ3MInu0MQA5taS4xNX4qLy_9KQ6YR5mPXxBvlnDeMYQ8r2bRxWx24DXHFLaJpksD580O0-Pazv2NMsRSwinCRyYWjpbztafqlv9Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصاویری از بدرقۀ رهبر شهید انقلاب در حرم مطهر امام حسین(ع)  @Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/448569" target="_blank">📅 04:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448568">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693ba173db.mp4?token=OpRLhq2DcWLgI_Iu7hejCqyfXDx7Ng3DFlvgCN5yFppQFlDONMM_Me_zGn5hQU7zxpchOVvbDWlGLvqnagul2r-uNJYpvtlmkCXT7vg1VCQpfHfXtJHUJblMDAY4gdR374H2TP3pJrdjyU-Lr5ikZU7ZmfIrNCgQlojRK1LVCJZA3jJdho1weNDobVb4wEnUBW6SugL4c4QzoLxLmsqFoPOCO-GgPkm_afbh-iqoZUkBbW2bm0Eq7Y-LQQ5Bn45xktj_2gE4vBGHfYE-BFWA3WJqYUZtQCmlYfuFa-UV5wY8RD8AK7TNiv0XseK6usMi0ZiF9AIzj57nvyCQnqkjKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693ba173db.mp4?token=OpRLhq2DcWLgI_Iu7hejCqyfXDx7Ng3DFlvgCN5yFppQFlDONMM_Me_zGn5hQU7zxpchOVvbDWlGLvqnagul2r-uNJYpvtlmkCXT7vg1VCQpfHfXtJHUJblMDAY4gdR374H2TP3pJrdjyU-Lr5ikZU7ZmfIrNCgQlojRK1LVCJZA3jJdho1weNDobVb4wEnUBW6SugL4c4QzoLxLmsqFoPOCO-GgPkm_afbh-iqoZUkBbW2bm0Eq7Y-LQQ5Bn45xktj_2gE4vBGHfYE-BFWA3WJqYUZtQCmlYfuFa-UV5wY8RD8AK7TNiv0XseK6usMi0ZiF9AIzj57nvyCQnqkjKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقبال عزاداران عراقی در حرم حضرت عباس(ع) از پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/448568" target="_blank">📅 04:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448567">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‌
🔴
فعال‌شدن آژیرهای هشدار در بحرین و قطر
🔹
منابع محلی از به‌صدا درآمدن آژیرهای حملۀ هوایی در بحرین و قطر، بعد از شلیک موشک‌های بالستیک از ایران خبر دادند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/448567" target="_blank">📅 04:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448566">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9658ab1bf6.mp4?token=uRyCJAmORi_rLJMQv-X65exMm4-yNnhqi0WqWfaxvUGlRGms7IKhdheccFPnkNhZjg5qYHs2b4S-qMJjYe2zg0fo5nMG17aOxV_t_dc_yWrdzsJterXBl-OMdrUOMllNnSebgxkC1JlPuJoNRL8GOqvEquySM4a2TFaPdYqHCBrXrLcyPeJIeUp4KVAOEaGiB9oS3xU70-VY0OqYG7CRMGL3GPvTUegWFbvPj4LJ2l-uUF0ptKSf2tjZhVqOd4VQ5S_LXv662EH4PP_EM9S2sioycSvmmybqFnxWIbhbfimMcU-jhkAmkkksJqCKpKpLegp20w2zrlSU-EAMcAeAdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9658ab1bf6.mp4?token=uRyCJAmORi_rLJMQv-X65exMm4-yNnhqi0WqWfaxvUGlRGms7IKhdheccFPnkNhZjg5qYHs2b4S-qMJjYe2zg0fo5nMG17aOxV_t_dc_yWrdzsJterXBl-OMdrUOMllNnSebgxkC1JlPuJoNRL8GOqvEquySM4a2TFaPdYqHCBrXrLcyPeJIeUp4KVAOEaGiB9oS3xU70-VY0OqYG7CRMGL3GPvTUegWFbvPj4LJ2l-uUF0ptKSf2tjZhVqOd4VQ5S_LXv662EH4PP_EM9S2sioycSvmmybqFnxWIbhbfimMcU-jhkAmkkksJqCKpKpLegp20w2zrlSU-EAMcAeAdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر رهبر شهید انقلاب وارد حرم حضرت عباس(ع) شد.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/448566" target="_blank">📅 04:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448565">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‌
🔴
وزارت کشور قطر با اعلام سطح بالای تهدیدات امنیتی، اعلام کرد تمامی شهروندان و ساکنان در منازل و نقاط امن بمانند.  @Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/448565" target="_blank">📅 04:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448564">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
برخی منابع خبری از شنیده‌شدن صدای چند انفجار در بحرین گزارش می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/448564" target="_blank">📅 04:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448563">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
برخی منابع خبری از شنیده‌شدن صدای چند انفجار در بحرین گزارش می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/448563" target="_blank">📅 04:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448562">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09eb617d67.mp4?token=g1JRMGGQy6KXVZ_vVEdPD88vSdfJ9rlJ8gKm7bSPYA8oAniNdNoGE2RcVMdHJQ-Z0Mk8Sfsc__IWM0mbLzA63RAqZRccHMEI2gaqewdsITzK5gEu9ipqB8nr8Tr9cNbZkM_J7p8fokdCANKC5FzGJIDDw5b8xCxLHKsydN_g5IHccBFl1ODUBscvoCca7AgfjjcsAOPvwXibEgH8Hs17Xi01-cmTYVtBqL88HEh9_8WvLRGM7PicFJjEdjV8XsthW9vtY1myUswgyXpsDOhDa-ehyG2eErrvDiBZS9YHPTsMI_cIQCP6jgRfpehQpKlF_Z9_rPoMWbG8l-gnVfcPdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09eb617d67.mp4?token=g1JRMGGQy6KXVZ_vVEdPD88vSdfJ9rlJ8gKm7bSPYA8oAniNdNoGE2RcVMdHJQ-Z0Mk8Sfsc__IWM0mbLzA63RAqZRccHMEI2gaqewdsITzK5gEu9ipqB8nr8Tr9cNbZkM_J7p8fokdCANKC5FzGJIDDw5b8xCxLHKsydN_g5IHccBFl1ODUBscvoCca7AgfjjcsAOPvwXibEgH8Hs17Xi01-cmTYVtBqL88HEh9_8WvLRGM7PicFJjEdjV8XsthW9vtY1myUswgyXpsDOhDa-ehyG2eErrvDiBZS9YHPTsMI_cIQCP6jgRfpehQpKlF_Z9_rPoMWbG8l-gnVfcPdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
◾️
به‌دلیل ازدحام شدید جمعیت در بین‌الحرمین، پیکر رهبر شهید انقلاب به حرم امام حسین(ع) بازگشت.
◾️
تشییع پیکر رهبر شهید به سوی حرم حضرت عباس(ع) پس از اقامۀ نماز صبح ادامه خواهد یافت.  @Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/448562" target="_blank">📅 03:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448561">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGsZSfn12MNfwnZn3nWgsDAWylT70HopixDcBfiNZPAW0j_7ubAcIS6GGPzJWkUMabvuXImEHMzgkqHZtQnCxy2ZcC3FRXu2EI3JL-CPExa0w5OI0U8KhL-kvHheCQ7hnifK_GCTAdZHhFcyKWN8WWqLAPkXyjE0Xiw7JxUzG5ArsUZIs_tMksjV2vR7vi9i1jiJUe3jorPjU316A7jRCD08dA_aSzJeEorDEAPv-hC3wFNL8d5cP0yXl0DM2vyuYnNIloMLpi9-IcriwSpSi4NtO1VS-aEngwjfP4ZI-BE4EBkumXE6dqaoxmU9I-6U1gd1ptWhXxcsKvQLblSv_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله آمریکا به دو پل خط آهن در ایران
یک مقام آمریکایی بامداد پنجشنبه به وبگاه «آکسیوس» گفت که نیروی هوایی این کشور، دو پل راه‌آهن در ایران را بمباران کرد که اولین حملات به زیرساخت‌های غیرنظامی این کشور از زمان برقراری آتش‌بس است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/448561" target="_blank">📅 03:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448560">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🎥
پیکر رهبر شهید انقلاب از باب الشهدای حرم امام حسین(ع)،‌ رهسپار حرم عباس(ع) شد  @Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/448560" target="_blank">📅 03:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448554">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q7id4PABJF_W_DFeF6q_ei_2NhPMyXoMNLHGq0KNC32m13lRx6mvlSrAxyG1KaxMsfhygZeMoC9Ga_KA1rQIlDa-j85yO3BMUU0plooXZsM1wBPnOtlUoIGgRlCY5jODdXj38vQtD-xKIx42k_RrLvDGaFxLClXxKmqvaLT1MAcFFzgrc7boy-vdXd4tK5XrazOZTczTyr0H8UKu0y92lOMINEucnFGqq0Zk1WmEP7w9G26GvSeOFxXt-Ow2T1vpwKchVnLBpcHJmrAvx8-YSz56l3cQF5rrW0PvyFIo_bHLHAI3ENNO8TDvlM1W8wjwRlN1sX2FPmjEzgnvamUmQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q9qgrNdGf0jaTKvU0NgqbP4V7LkU313YnU3vEL97ABVLDH7SvkIrf5dc4qM4F1XwmtPq__hSDLa8CQDRTqdFVoPl7j4rrnGnGE09N93b7exhGthSyYhl9LGn17mwKw204Low6tM-WB1mC_XuGnJ_fi8LYE-pAGF1QizfJCnuKjeBgtdjcG0TxbqRVKDatuhZSO8VW70PuocBwK1B4Ee3Kh1eG9tuvywEEEK4NvP1uemg1xcqGEuCZikTEfbl_u7XKJs5QLG4igzaoJ-UL-QC4nCRsLUrUmVW5_zrJDXQuco6Z9Kro3oIEv8wVipipLqGl_5kveekC4CTtlpA9d2Dlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j4AyCchUZLgrloR87bKmAkosgg4PaXEYGNZ58fmmyWNzII5l2FcE7nwpehSDI25j7D7t5XXoJICSh11TOU5rwWrQMeplORbh3YS_Hhj_zEZNWFy9INFPAI7tdAp2iURHXD4YXN8330ExLHSen2TwJFExNbvk2wmDFr3RtzSf01VvhZJyAJ2auALNip7t4yYoh0XuYncn-5XwRFrsXztCstS67zpuLtic_8jG2Kt6c3hiNHnVgZZpRIKIxMZdC0GCPqaqRo7031y-b1rwwiQpmcTBtIx7wsi_IZ7QlmtO4FPtyx9a1ipyVFcEh68Miurx0glnyNpmkzFTwmU4katZew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gzMR9bJMsQTld4H0jK2FUAehM5rIyEgY4OionAc3fAh7TM-MPVSyCJ3zOYIAeG6-_m75H-t6SvPwZUKu4sPShuEhnuw5DoJ0ilQ20UZ1MUA1HyibX17afDBpqbOTVhiDH1sxRVxx-veseQBksgHghFASF-Oh1ZFLwhdKThRNdMtJff2S4hN2WzvN5d7GRTrnKNltK9CNQRdPdnbEjntr2qssq2-PipSgTw1x0Eb3HuOzXqy-bg93DbeTP1ItxtOMZexWCbbu_InNqMsHE83MhtsQbuXab8mdIz-lWLQZUNVtTBC7KKWFY3G-Bjl7BkA9WkfC7D2L5Ep8rzOozbCc-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N9hVZeAv-SnVA2glvW7LxmKVwTME5WUdM5QBI8Ogpn1KYGPZ07KL4TgUtifISc4-hp2e0x6yuqpvtlDzfT8a95XufJSwZ9oYKNDg0T44NAQ2FbyaDYBzDXSBz280Mpfv5ShKvvzrwiUNxHYJ8p0jLDWKy_5EhnId0aGzSK0HFgUiFgGw2bp5W2ADNrI2i9lGBTWuTcBmawZZ4qf1ZBkpMdYXLoiYFXc1gr4aqTQWLQkQOhyKQvvTBJ0CmAUBKzyvnb04OFeBurEmWrFZLWEXC_t4alIGvgJtino6ihnC0itwTL3oXWuUr2zxkmlqa5RUnK9UlFkFzwhpkn5sivstXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kt-2O7fFr2Gn6qXDSymiiSiqqOHBuDIKQpTSIrSyY-TgT9uXaB1Veua32SU9eGHcdPfIH51eO1RUwP62CwCIbAN_EsMkWifcOtehQoCtkpFq58rv8NQ6JLtVSrwUXKVXSbKAWK5lgu92nNVYbGNqNoCdSQKifALyAYrec3K3hBE3b7XLH7VRrLkPRGWLfw3mydsARv1lRmyfH60wqa9BI8Zm9OUUaAewCnVva90PhtSoC3Bk8ZrGzFbRIFTwKZ_uU7FdwBwqJvXCXo3UuzU6SXZ7_cG23oYuVggjr-uqCcQHsueMqxkj2nPK6u_9YcRnHPSZUfdBZtf_NawT6Z7gTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از بدرقۀ رهبر شهید انقلاب در حرم مطهر امام حسین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/448554" target="_blank">📅 03:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448553">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVBVYnOl4SqSvqx1-KXp8sec0c5azuCMEI_GiFGDWbhoBpMKhhmcV2ycRKLAxdx4ksgvERwr_It6DGZaDgDLeR7JB7-6LKHoiPvCpgEci290Ciiht-DGbnPEmgMfC38giqIwFFFQkMSZ5z_KuUo_1Cr_SmMjBtYe7E-oKezEk1qsxTJ0hia7Y8qZkJiGgKUauvBK4x-cmRPuRbgFoUjBLtlclnLa7Zxd8Zf-weAVbamVd-kCid6eCZAoRTJ83YG3ii3TGO3gdFO-iQ7tkd3GqAgHvqnhVWWnr5ujoMB3R89VxrpfgLhltLiB1d2lLmPCppP5W8E2el6K51SnKPj19g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی کمیسیون امنیت ملی مجلس: منتظر سیلی سخت ایرانی‌ها باشید.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/448553" target="_blank">📅 03:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448552">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/946390c5b4.mp4?token=S4nRpZLemECs6CkDqgJKB7hWwejtpiPEBoo38dH0SkOHb_66yuHxnmfZ8ZsqIoqoTGKAXTOiK3G8K2I35HGY0EpQrUE5xqp1wyl44lq0itP5exhAoXf73KGIKVYaIQy1sqi2paIOljvS0I_Nd70lKigCldCZPjhEd9MpccXSFl3l4wKCdkoX2rA6ko-PKLWSZ3F7URcyBCdLfo5zkF3cGM1giYxZWVRRMR2TXAQgTXSda-Wp-ST3QJymhjHfJS17yd9KKRI3rZYsbKUNpfQXV02TfH5TL9AYfzjV7k1k9tIBZcw4ZFbl7heBUHwV8qvysH6hPlXdVgoqV2s7TsRCWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/946390c5b4.mp4?token=S4nRpZLemECs6CkDqgJKB7hWwejtpiPEBoo38dH0SkOHb_66yuHxnmfZ8ZsqIoqoTGKAXTOiK3G8K2I35HGY0EpQrUE5xqp1wyl44lq0itP5exhAoXf73KGIKVYaIQy1sqi2paIOljvS0I_Nd70lKigCldCZPjhEd9MpccXSFl3l4wKCdkoX2rA6ko-PKLWSZ3F7URcyBCdLfo5zkF3cGM1giYxZWVRRMR2TXAQgTXSda-Wp-ST3QJymhjHfJS17yd9KKRI3rZYsbKUNpfQXV02TfH5TL9AYfzjV7k1k9tIBZcw4ZFbl7heBUHwV8qvysH6hPlXdVgoqV2s7TsRCWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر رهبر شهید انقلاب از باب الشهدای حرم امام حسین(ع)،‌ رهسپار حرم عباس(ع) شد
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/448552" target="_blank">📅 03:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448551">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
دقایقی پیش مردم آق‌قلا صدای چند انفجار از محدوده این شهر شنیدند.
🔹
هنوز محل دقیق این انفجارها مشخص نیست و هنوز دربارۀ این انفجارها جزییات رسمی منتشر نشده است.
🔹
برخی منابع محلی از اصابت چندین پرتابۀ دشمن به پل آق‌تکه‌خان در مسیر ریل قطار در محدودۀ غربی شهر…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/448551" target="_blank">📅 03:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448549">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7e08f738a.mp4?token=ALrJi2JsqSTol1KQOiyOn1FiyQI9yjv7OfH57AJRNK8_FechxRpK-b7ihw0XZ0u-sTIQL9rAZz27JzrB9O9z0FLvDCkr0KcBNj9aA9zgRoChPphtvoYIAX6QDtSrtQ8Q5sD-jP1sHUxg-Ah_Dzy-Ysrz32ogChPjofBycmlbVxAeWOqpnlkbdTRCJmc1uUs0_ZD5yPOzIWDpJFpd4PK1JA9Pr9AJUsCk0zVJfHTSvB62FQPT0qnlBXjxpRWtws8iZENpk_6Sga4lm4pOGrL5daphRr_-FbjCi_lMYWd10UtyWCO-X7b7xfofr3uNX4nk1_KBGy5DmejTxmbAUBiK3oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7e08f738a.mp4?token=ALrJi2JsqSTol1KQOiyOn1FiyQI9yjv7OfH57AJRNK8_FechxRpK-b7ihw0XZ0u-sTIQL9rAZz27JzrB9O9z0FLvDCkr0KcBNj9aA9zgRoChPphtvoYIAX6QDtSrtQ8Q5sD-jP1sHUxg-Ah_Dzy-Ysrz32ogChPjofBycmlbVxAeWOqpnlkbdTRCJmc1uUs0_ZD5yPOzIWDpJFpd4PK1JA9Pr9AJUsCk0zVJfHTSvB62FQPT0qnlBXjxpRWtws8iZENpk_6Sga4lm4pOGrL5daphRr_-FbjCi_lMYWd10UtyWCO-X7b7xfofr3uNX4nk1_KBGy5DmejTxmbAUBiK3oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طواف پیکر رهبر شهید انقلاب بر ضریح حضرت سیدالشهدا، امام‌حسین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/448549" target="_blank">📅 03:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448548">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b29e540c3.mp4?token=CJjPdoWdVNicrsQLJufWtFaD0ZuVULEEYwOswhcergHZ2vi2rFLV1fugSebi5MD5i3OYCbC_AkJao2ElndDCmHE5YOMCabslqEdyWWeYROHgKD96_6aGqjs41UbKfgwqCPIeWtJB-MCT6SlcwyLNuFi19m5e9ZS1StSYk9QeVU8rnWieqjr7It23o9csqewr64JOtR7malerBT3W5e4pD9B4UbBHwKO0-H8EppMwvF57KT6cGm6NjHcYonFLH6-Ho6T_2bVVI1JjAqCbuIrhYotj1KfRQ9Qxd7R9dZXaqQ6M6Cpy5uOpI9Bl0odeTN8z_4ln68mc9P4Ds2NNBeJTKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b29e540c3.mp4?token=CJjPdoWdVNicrsQLJufWtFaD0ZuVULEEYwOswhcergHZ2vi2rFLV1fugSebi5MD5i3OYCbC_AkJao2ElndDCmHE5YOMCabslqEdyWWeYROHgKD96_6aGqjs41UbKfgwqCPIeWtJB-MCT6SlcwyLNuFi19m5e9ZS1StSYk9QeVU8rnWieqjr7It23o9csqewr64JOtR7malerBT3W5e4pD9B4UbBHwKO0-H8EppMwvF57KT6cGm6NjHcYonFLH6-Ho6T_2bVVI1JjAqCbuIrhYotj1KfRQ9Qxd7R9dZXaqQ6M6Cpy5uOpI9Bl0odeTN8z_4ln68mc9P4Ds2NNBeJTKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روضه‌خوانی و عزاداری عراقی‌ها، در وداع با رهبر شهید انقلاب در حرم امام‌حسین علیه‌السلام
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/448548" target="_blank">📅 03:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448547">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a3c37a50.mp4?token=As2yljzdDaRu4IRfC7U4s68GZRVR9pZU_hICjoXxRPtWXQzFWYTnBAuEqY2mIQ6qPeeVLaxcZ6XqmXS4kJcR_VKjVUyzH_oqSpIutP-cRUDSrk03mLyCSTDTXBTRQ0eJDvroN9KQNeW4rxpPzl3HBZsjwBMGX3LEF3d-va6Xz3vorFCA86sHN4p-c2497Y4m0ETW3gYz_872pbmYUZ0sKUKzHDxb-i4AMVdVrpXEwez1pR_6jcuBbmfYRc7B8l6aTlKtAHAxFjejvOvC8GMoXmDfC_GcGoQmi0Nw7rDbZJIdXMDgiFYOqCh4CYGPJrxgRdgklGcRtmUYZI5braawxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a3c37a50.mp4?token=As2yljzdDaRu4IRfC7U4s68GZRVR9pZU_hICjoXxRPtWXQzFWYTnBAuEqY2mIQ6qPeeVLaxcZ6XqmXS4kJcR_VKjVUyzH_oqSpIutP-cRUDSrk03mLyCSTDTXBTRQ0eJDvroN9KQNeW4rxpPzl3HBZsjwBMGX3LEF3d-va6Xz3vorFCA86sHN4p-c2497Y4m0ETW3gYz_872pbmYUZ0sKUKzHDxb-i4AMVdVrpXEwez1pR_6jcuBbmfYRc7B8l6aTlKtAHAxFjejvOvC8GMoXmDfC_GcGoQmi0Nw7rDbZJIdXMDgiFYOqCh4CYGPJrxgRdgklGcRtmUYZI5braawxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چشم‌های گریان مردم مشهد در انتظار رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/448547" target="_blank">📅 03:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448546">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89c49b46eb.mp4?token=h4aU6tpiotibphoYmbT7LemV-8gg5g0yz_cSpUTDWmUzhtjETbw6yZ1GRavFg5R2GlxbuqyC6Gn0xvqyI2PqWesmBZRUB1TmTeK2CBpK6Fdw5kApJVyqYQIooYRAGisQhLhvX53G30aenooDFbhiVQ6xp8EIlR0zhm_QJ1Ig29KFXOX4i4mgGLi8vPq3HvPh3FsQc3PDSqdB90pnPDj7QkUEn_jpwNDyAKKMS-nBHRdfkX-y_qWGHUcG9KifS9UWINFsgkIlOs2PfiZymNErmfTpOLwJpUGxsX_uHHQoHxrnjpoz4bSHYP6aLltUWIrwxuOWgs3VU_NzWHqfy7ScAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89c49b46eb.mp4?token=h4aU6tpiotibphoYmbT7LemV-8gg5g0yz_cSpUTDWmUzhtjETbw6yZ1GRavFg5R2GlxbuqyC6Gn0xvqyI2PqWesmBZRUB1TmTeK2CBpK6Fdw5kApJVyqYQIooYRAGisQhLhvX53G30aenooDFbhiVQ6xp8EIlR0zhm_QJ1Ig29KFXOX4i4mgGLi8vPq3HvPh3FsQc3PDSqdB90pnPDj7QkUEn_jpwNDyAKKMS-nBHRdfkX-y_qWGHUcG9KifS9UWINFsgkIlOs2PfiZymNErmfTpOLwJpUGxsX_uHHQoHxrnjpoz4bSHYP6aLltUWIrwxuOWgs3VU_NzWHqfy7ScAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقامۀ نماز بر پیکر مطهر امام مجاهد شهید در حرم مطهر اباعبدالله(ع)
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/448546" target="_blank">📅 03:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448545">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/751494424f.mp4?token=ekYTQ2068IPgcIwyNBfyJOAJz_lJlqJzDLlzwZiDXh47Fvc3IWXfcE8Rw656V6or28C__SivYukgCrBAfFZVZcgY_wRhM1MX4JH0WY9IWnDnQDCuDAXmlARNsnQ6FkUuSXqC_51QKzaS4fqm4WRw9QCBDyc2QW8GQuj_se3aytWP4x4uVW271VP4-s8zqAu_0_k7h4qxqfv-FTdiXIMQrXcxt4cMRNGgtXrNjDe1xcT46Lz0jnG4x80dH9bNtz7xxhjtaJfKQpxq66_ur0vm_7OjoOBs2eNqmxmchM0PqTP5_ONvT2V0DzkhiHpek17ANQhzgo-hlkWOqopdTSs0zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/751494424f.mp4?token=ekYTQ2068IPgcIwyNBfyJOAJz_lJlqJzDLlzwZiDXh47Fvc3IWXfcE8Rw656V6or28C__SivYukgCrBAfFZVZcgY_wRhM1MX4JH0WY9IWnDnQDCuDAXmlARNsnQ6FkUuSXqC_51QKzaS4fqm4WRw9QCBDyc2QW8GQuj_se3aytWP4x4uVW271VP4-s8zqAu_0_k7h4qxqfv-FTdiXIMQrXcxt4cMRNGgtXrNjDe1xcT46Lz0jnG4x80dH9bNtz7xxhjtaJfKQpxq66_ur0vm_7OjoOBs2eNqmxmchM0PqTP5_ONvT2V0DzkhiHpek17ANQhzgo-hlkWOqopdTSs0zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌و‌هوای مشهد مقدس، ساعت‌ها پیش از آغاز مراسم تشییع پیکر رهبر شهید انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/448545" target="_blank">📅 03:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448544">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/158f4fd72e.mp4?token=jXbRS0rEemtP_qHedxZv38KDd2WBge--w86VB5wWRIwtTWyzZUFZYuYktG8-Fwsw8XBt5YigpVyNLJrYTuX4OgNEAaEprcuLMj3CPfz8uH3TveIFKCRYIthm5IE3pHQblvR8dlMPa31RnU9EpD3RqAwN3PwYHyQ3xsqZpJ8-DWLNYTl257fB3rXNmWUsCErYogRsLzjRb6EtEpaIa7rUpT9IWmc5NDqWENrZ1QsfAUOLWtO8BQxXwUA4V_H5CDSdjfULze0cMbXpTXXE-_xovAUnkqkc1M59AerJ3whOCrd99hr-UPkRk1EEu5wG-o1jf9dBXjsPW_QqME-5SHTr-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/158f4fd72e.mp4?token=jXbRS0rEemtP_qHedxZv38KDd2WBge--w86VB5wWRIwtTWyzZUFZYuYktG8-Fwsw8XBt5YigpVyNLJrYTuX4OgNEAaEprcuLMj3CPfz8uH3TveIFKCRYIthm5IE3pHQblvR8dlMPa31RnU9EpD3RqAwN3PwYHyQ3xsqZpJ8-DWLNYTl257fB3rXNmWUsCErYogRsLzjRb6EtEpaIa7rUpT9IWmc5NDqWENrZ1QsfAUOLWtO8BQxXwUA4V_H5CDSdjfULze0cMbXpTXXE-_xovAUnkqkc1M59AerJ3whOCrd99hr-UPkRk1EEu5wG-o1jf9dBXjsPW_QqME-5SHTr-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله جوادی آملی: مردان الهی اهل انتقام هستند
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/448544" target="_blank">📅 03:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448542">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yp8xCaEYwZfabWiIOXuac0dGj_65L0u_Mm2sPcLJi-BmrceOkbq_GhtDnyW8q2JVyvseMo_RuLU69fqIr6xz-eS5fc5S4cEZxpDaTHZQeV6KyUegqTc3KEsx54wyUjn2SxKp6YKO_-1ICH4Al-pNpfnbAlscif2cWKJAI8kJh5AgNG1WBQdXBpulro3Cpq3m6cPfSPPpzasvSjLIDuKABcwAM8bhSNhTI61U5VlD0rX5cpKkzcKZlKjvqCSsigTWkRx51NLYhDaeSVZQW7PG2X3xUeFgqgAERWpiiwJFhTtgNOd7z0IBwwbQk2aF9-VqLbuQg8-0VgM5RRv9hgbVCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RiPYzNJiYH_BmAI1eDqDV6B62bUhLpIi3DN2l2zRwpL1ZGU44ryt9VbK_b6UjHWy5SPO9M9U6xLjrU7_bGT8F4XlI9rDVT_2GLfbq4f-f2j0z0su5SfT7iTTKWpG9m0i6sfVYyg0cEF09ucWFULlc3aVEiTFzdj1SZlbJ3QHeBmcspVWAthFxgx72gENJOfC1pK4d6FKVMGNwTD6cTuF5fhZ8eo8SgIyTTdH0RnO7_Ry7xdNL1ZRkcOOo4XyFYjTPTphOeK0mAIvipE22qb719_JJmeVQj4d_CcvvKQzr78bdnofAnIY9tB1G1lI-CQnOUK6P7R0otOHP1ADi8hNqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از لحظۀ ورود پیکر رهبر شهید انقلاب بر دستان مردم عزادار به حرم مطهر سیدالشهدا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/448542" target="_blank">📅 03:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448541">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed101adfb2.mp4?token=RBHaIGXYw42J-8oR-tK5Lo--LUT18CjYixTU5yMSv3kZiSk1qVteIDvGqHKvtrB-0VB-t_4C0ZtS0glYxEy9YV-Dg3ELD7UIJMAd5UKW31FC5_apBEpYB9N3RXAnAFxOOJQDR88AA9NpDq1ZEH1BPL1monP0WUzIAyRFSnSYBKLFmQ-waIlRhpl6YGxJA8SoKDfOYGQUgWb0wQUa2xzT5QjdBgN4UQTiZnD6k8x0X-XyYuFkeW6oVzAYuxah4r8xpzF8hs8G3hAHCX6iCOYfS6bWjRtZeGCeqhHNFxP7wz0xX2iPh4Jk_kwgdtG3lzqKzhtczcV62YKyUiegxqM2Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed101adfb2.mp4?token=RBHaIGXYw42J-8oR-tK5Lo--LUT18CjYixTU5yMSv3kZiSk1qVteIDvGqHKvtrB-0VB-t_4C0ZtS0glYxEy9YV-Dg3ELD7UIJMAd5UKW31FC5_apBEpYB9N3RXAnAFxOOJQDR88AA9NpDq1ZEH1BPL1monP0WUzIAyRFSnSYBKLFmQ-waIlRhpl6YGxJA8SoKDfOYGQUgWb0wQUa2xzT5QjdBgN4UQTiZnD6k8x0X-XyYuFkeW6oVzAYuxah4r8xpzF8hs8G3hAHCX6iCOYfS6bWjRtZeGCeqhHNFxP7wz0xX2iPh4Jk_kwgdtG3lzqKzhtczcV62YKyUiegxqM2Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فی امان‌الله در پناه ابی‌عبدالله
◾️
پیکر مطهر امام مجاهد شهید پس از ساعت‌ها تشییع در کربلای معلی هم اینک در حرم امام حسین(ع) بر دستان مردم عزادار در حال تشییع است.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/448541" target="_blank">📅 02:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448540">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55902132cb.mp4?token=W4_QNPYge0xotEIZ6KoS3652Rmye-DxhJ191szpe3RP5BgytWmL_MleAYB-8W450-ju0kTh1zkUytvg8ktQZBGqnCOXhKteCS53IAchJeJFTBePQkHDtF1emYgSYCadtuDz25VwG0Sew64iaXdXHiFfH8jANSWbg7KtfcrY_bjIAI415ErAEpeCVMcI-PPsY85P3s86YXe0TmpgYHEIq8GZO8QujhVU0sJFouTe1ALDYBx8FkhMn5RAclb4Zp7D6RvR1chyE8ZQx86d8tO2TJ08owJ2ykgOJUqunPhY8Oe2LNLgGAYe-ZqWRcSip2pw5sw310W_57Ji8vP8FVwhzdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55902132cb.mp4?token=W4_QNPYge0xotEIZ6KoS3652Rmye-DxhJ191szpe3RP5BgytWmL_MleAYB-8W450-ju0kTh1zkUytvg8ktQZBGqnCOXhKteCS53IAchJeJFTBePQkHDtF1emYgSYCadtuDz25VwG0Sew64iaXdXHiFfH8jANSWbg7KtfcrY_bjIAI415ErAEpeCVMcI-PPsY85P3s86YXe0TmpgYHEIq8GZO8QujhVU0sJFouTe1ALDYBx8FkhMn5RAclb4Zp7D6RvR1chyE8ZQx86d8tO2TJ08owJ2ykgOJUqunPhY8Oe2LNLgGAYe-ZqWRcSip2pw5sw310W_57Ji8vP8FVwhzdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السّلام علیک یا سیدالشهدا...
◾️
پیکر مطهر امام مجاهد شهید پس از ساعت‌ها تشییع در کربلای معلی هم اینک در حرم امام حسین(ع) بر دستان مردم عزادار در حال تشییع است.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/448540" target="_blank">📅 02:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448538">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ccfcc8d8d.mp4?token=vb5znCFCytNBPtTU5tLRTt_N-N-UFoQtlLc-b-nF_U9DDLshj6p6ZyG2EcSAgQ4BJYRwFwe9TeWHm7KS4x4aGzmjxG_PhEYMtK3WZqwdhzvl3lPZwSvQZ2_yneskTBaXKAKS4c2T0O3L_kQMOkyw31BNH-xOp-iTKWOxYGQK0EPpL48IlAV1ylnixoIJqwUE5GmiyXqnKHXSNGoyhqyKZUvxfZQAJbwLiOhh5u1k3hObVleNbGCeV0cTj41m96OU2ZyWk914CYzIwQwlJORdg6x91iAoye3l-zRgRhsXkrNfrD76QvRFrGBx-EQ79mIM7mY4Q6HVUfgB5Lqfglvd7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ccfcc8d8d.mp4?token=vb5znCFCytNBPtTU5tLRTt_N-N-UFoQtlLc-b-nF_U9DDLshj6p6ZyG2EcSAgQ4BJYRwFwe9TeWHm7KS4x4aGzmjxG_PhEYMtK3WZqwdhzvl3lPZwSvQZ2_yneskTBaXKAKS4c2T0O3L_kQMOkyw31BNH-xOp-iTKWOxYGQK0EPpL48IlAV1ylnixoIJqwUE5GmiyXqnKHXSNGoyhqyKZUvxfZQAJbwLiOhh5u1k3hObVleNbGCeV0cTj41m96OU2ZyWk914CYzIwQwlJORdg6x91iAoye3l-zRgRhsXkrNfrD76QvRFrGBx-EQ79mIM7mY4Q6HVUfgB5Lqfglvd7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر رهبر شهید انقلاب بر دستان مردم عزادار وارد حرم مطهر امام حسین علیه‌السلام شد.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/448538" target="_blank">📅 02:55 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
